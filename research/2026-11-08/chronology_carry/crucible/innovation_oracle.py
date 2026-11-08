"""Independent exact root-of-unity and interval checks of EI1--5.

For power-of-two M, Q[X]/(X^M+1) is the exact field of the 2M-th root.
No learned table, source holdout, or inherited phase evaluator is imported.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json


def add(*polys):
    out = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = out.get(exponent, Q(0))+coefficient
    return {e:c for e,c in out.items() if c}


def scale(poly, c):
    return {e:v*c for e,v in poly.items() if v*c}


def root(exponent, M):
    if M < 1 or M & (M-1):
        raise ValueError('power-of-two root field required')
    exponent %= 2*M
    return {exponent % M: Q(1 if exponent < M else -1)}


def shift(poly, exponent, M):
    return add(*(scale(root(e+exponent,M),c) for e,c in poly.items()))


def mean(polys):
    polys = list(polys)
    return scale(add(*polys), Q(1,len(polys)))


def code(word, base):
    out = 0
    for digit in word:
        out = base*out+digit
    return out


def direct_compiler(base, k, h):
    M = base**k
    words = list(product(range(base+1), repeat=k))
    powers = [{w:root(h*(2*code(w,base)+1), M) for w in words}]
    for _ in range(k):
        previous = powers[-1]
        powers.append({w:mean(previous[w[1:]+(d,)] for d in range(base)) for w in words})
    mu = powers[-1][words[0]]
    assert all(powers[-1][w] == mu for w in words)
    psi = {w:add(*(powers[j][w] for j in range(k)),scale(mu,-k)) for w in words}
    Ppsi = {w:mean(psi[w[1:]+(d,)] for d in range(base)) for w in words}
    assert all(add(psi[w],scale(Ppsi[w],-1)) == add(powers[0][w],scale(mu,-1)) for w in words)
    return words, powers, mu, psi, Ppsi


def closed_coefficients(base,k,h):
    M=base**k
    return [mean(root(h*(2*a+1),M) for a in range(base**j)) for j in range(k+1)]


def closed_innovation(word,d,base,k,h,coefficients,retain=None):
    M=base**k
    K=code(word,base)
    start=0 if retain is None else k-retain
    pieces=[]
    for j in range(start,k):
        common=2*h*base**(j+1)*K
        pieces.append(shift(coefficients[j],common+2*h*base**j*d,M))
        pieces.append(scale(shift(coefficients[j+1],common,M),-1))
    return add(*pieces)


def exact_cases():
    rows=[]
    for base,k in ((2,1),(2,2),(2,3),(4,1),(4,2),(16,1),(16,2)):
        for h in (1,3,-5,base**k):
            words,powers,mu,psi,Ppsi=direct_compiler(base,k,h)
            coefficients=closed_coefficients(base,k,h)
            selected=words if base<16 else sorted(set(words[::max(1,len(words)//17)]+[words[-1]]))
            exact_checks=reference_checks=locality_checks=0
            local={}
            for w in selected:
                innovations=[]
                for d in range(base+1):
                    direct=add(psi[w[1:]+(d,)],scale(Ppsi[w],-1))
                    closed=closed_innovation(w,d,base,k,h,coefficients)
                    assert direct==closed
                    exact_checks+=1
                    if d<base:
                        innovations.append(direct)
                    for R in range(1,k+1):
                        partial=closed_innovation(w,d,base,k,h,coefficients,R)
                        key=(R,code(w,base) % base**(R-1),d)
                        if key in local:
                            assert local[key]==partial
                            locality_checks+=1
                        else:
                            local[key]=partial
                assert mean(innovations)=={}
                reference_checks+=1
            for d in range(base+1):
                w=(d,)*k
                eta=closed_innovation(w,d,base,k,h,coefficients)
                assert eta==add(powers[0][w],scale(mu,-1))
            # Literal base digit propagates; coordinatewise reduction loses it.
            if k>=2:
                w=(0,)*(k-1)+(base,)
                assert code(w,base) % base**k == base
                assert code(tuple(x % base for x in w),base)==0
            rows.append({'base':base,'depth':k,'h':h,'state_count':len(words),
                         'exact_innovation_checks':exact_checks,
                         'reference_zero_checks':reference_checks,
                         'memory_locality_checks':locality_checks,
                         'constant_digit_controls':base+1})
    return rows


def interval_cases():
    from mpmath.ctx_iv import MPIntervalContext
    from independent_phase_check import endpoint_fraction
    iv=MPIntervalContext();iv.dps=70
    def e(x):
        arg=2*iv.pi*x
        return iv.cos(arg)+iv.j*iv.sin(arg)
    def contains_zero(x):
        lo,hi=map(endpoint_fraction,x._mpi_)
        return lo<=0<=hi
    rows=[]
    for base,k,h in ((2,3,1),(2,4,3),(4,2,-1),(4,3,3),(16,1,3),(16,2,1),(16,3,-5)):
        M=base**k
        assert M>=4*abs(h)
        theta=iv.pi*h/M
        ck=theta/iv.sin(theta)
        for l in range(1,k+1):
            count=base**(k-l)
            finite=sum((e(iv.mpf(h)*(2*a+1)/(2*M)) for a in range(count)),iv.mpc(0))/count
            arg=iv.pi*h/base**l
            limiting=e(iv.mpf(h)/(2*base**l))*iv.sin(arg)/arg
            difference=finite-ck*limiting
            assert contains_zero(difference.real) and contains_zero(difference.imag)
            rows.append({'base':base,'depth':k,'h':h,'level':l,
                         'common_factor_identity_interval_contains_zero':True})
        lo,hi=map(endpoint_fraction,ck._mpi_)
        assert lo>=1 and hi<=1+Q(2*h*h,M*M)
    return rows


def source_compression_cases():
    from carry_controls import unwrapped, floor
    states,carries=unwrapped(80)
    checks=0
    for n in range(1,81):
        for k in range(1,min(n,8)+1):
            K=code(carries[n-k:n],16)
            assert K==floor(states[n])-16**k*floor(states[n-k])
            assert K % 16**k == floor(states[n]) % 16**k
            checks+=1
    return checks


def mode_covariance_cases():
    checks=0
    for base,k in ((2,2),(2,3),(4,2),(16,2)):
        M=base**k
        for h in (1,3,-5):
            large=closed_coefficients(base,k,base*h)
            small=closed_coefficients(base,k-1,h)
            positive=closed_coefficients(base,k,h)
            negative=closed_coefficients(base,k,-h)
            words=[(0,)*k,(base,)*k,(base-1,)*k,
                   tuple((i*7+base) % (base+1) for i in range(k))]
            for word in words:
                for d in (0,base-1,base):
                    high=closed_innovation(word,d,base,k,base*h,large)
                    low=closed_innovation(word[1:],d,base,k-1,h,small)
                    embedded=add(*(scale(root(base*e,M),c) for e,c in low.items()))
                    assert high==embedded
                    plus=closed_innovation(word,d,base,k,h,positive)
                    minus=closed_innovation(word,d,base,k,-h,negative)
                    conjugate=add(*(scale(root(-e,M),c) for e,c in plus.items()))
                    assert minus==conjugate
                    checks+=2
    return checks


def run():
    here=Path(__file__).resolve().parent
    exact=exact_cases()
    intervals=interval_cases()
    return {'status':'EXACT FINITE ALGEBRA AND SEPARATE INTERVAL CHECKS; paper proof separate',
            'later_source_holdout_read':False,
            'exact_root_field':'Q[X]/(X^M+1), M a power of two',
            'exact_cases':exact,'interval_common_factor_checks':intervals,
            'source_integer_lift_compressions':source_compression_cases(),
            'exact_mode_covariance_checks':mode_covariance_cases(),
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'proof_sha256':sha256((here/'EXPLICIT_INNOVATION.md').read_bytes()).hexdigest(),
            'pi_normality':'OPEN','RH':'OPEN'}


if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();result=run()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'exact_configurations':len(result['exact_cases']),
                      'exact_innovations':sum(r['exact_innovation_checks'] for r in result['exact_cases']),
                      'interval_common_factors':len(result['interval_common_factor_checks']),
                      'mode_covariances':result['exact_mode_covariance_checks'],
                      'source_compressions':result['source_integer_lift_compressions']}))
