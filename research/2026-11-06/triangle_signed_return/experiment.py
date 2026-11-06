"""SUCC triangle/source-spectrum tests: stdlib only; no infinite real cancellation claimed."""
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction
from math import cos, sin, pi, log, sqrt
import json


def source(n: int) -> Fraction:
    return Fraction(120*n*n - 89*n + 16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def four_poles(n: int) -> Fraction:
    return (Fraction(4,8*n-7) - Fraction(2,8*n-4)
            - Fraction(1,8*n-3) - Fraction(1,8*n-2))


def mod_odd(q: Fraction, modulus: int) -> int:
    q = Fraction(q)
    assert modulus > 1 and (modulus & (modulus-1)) == 0
    assert q.denominator % 2 == 1
    return (q.numerator * pow(q.denominator, -1, modulus)) % modulus


def raw_orbit(N: int):
    x = Fraction(0); C = 0
    xs = [x]; Cs = [C]
    for n in range(1,N):
        t = 16*x + source(n)
        b = t.numerator // t.denominator
        x = t-b
        C = 16*C+b
        xs.append(x); Cs.append(C)
    return xs, Cs


def isometric_v_mod(n: int, modulus: int) -> int:
    # Independent past-directed 2-adic source, truncated at exact valuation.
    k=modulus.bit_length()-1
    return sum(pow(16,j,modulus)*mod_odd(source(n-j),modulus)
               for j in range((k+3)//4))%modulus


def overlaps(v: int,c: int,x: int, modulus:int):
    return ((v+c)%modulus, (c+x)%modulus, (x+v)%modulus)


def triangle_tests():
    counts=[]
    for k in (1,2,3):
        Q=1<<k
        image=Counter(overlaps(v,c,x,Q) for v in range(Q)
                      for c in range(Q) for x in range(Q))
        assert len(image)==Q**3//2
        assert set(image.values())=={2}
        assert all(sum(key)%2==0 for key in image)
        counts.append({'k':k, 'image_count':len(image),'fiber_cardinality':2})
    for k in range(1,13):
        Q=1<<k; flip=Q//2
        for v,c,x in ((0,0,0),(7,43,19),(Q-1,11,99)):
            assert overlaps(v,c,x,Q)==overlaps(v+flip,c+flip,x+flip,Q)
            # Constrained plane V = C+X: integral inversion, no /2.
            v=(c+x)%Q
            a,b,d=overlaps(v,c,x,Q)
            assert (a+d-3*b)%Q==0
            assert (b,(a-b)%Q,(d-b)%Q)==(v,c%Q,x%Q)
            # A HALF-MODULUS wrong-carry shift COUNTERFEITS the closure test!
            # This red negative control repairs an initially false expectation.
            a2,b2,d2=overlaps(v,c+flip,x,Q)
            assert (a2+d2-3*b2)%Q == 0
            # With one extra bit, the same false seam is exposed.
            assert (2*(v-c-flip-x))%(2*Q)==Q
            # A unit wrong-carry shift is detected at K>=2 (not at K=1).
            if k>=2:
                aa,bb,dd=overlaps(v,c+1,x,Q)
                assert (aa+dd-3*bb)%Q != 0
    return counts


def frequency_tests():
    cases=[]
    for b,Q,M in ((2,2,4),(3,3,3),(16,4,3)):
        freqs=[]
        for j in range(Q):
            for t in range(M):
                for u in range(M):
                    if t!=u:
                        freqs.append(b**(j+t*Q)-b**(j+u*Q))
        assert len(freqs)==len(set(freqs))==Q*M*(M-1)
        cases.append({'base':b,'Q':Q,'M':M,
                      'frequency_count':len(freqs),
                      'expectation_R':f'{1}/{M}',
                      'variance_R':f'{M-1}/{Q*M*M*M}'})
    return cases


def energy(xs, Cs, Q, M, h=1):
    assert len(xs)>=Q*M
    s=[complex(cos(2*pi*h*float(x)),sin(2*pi*h*float(x))) for x in xs[:Q*M]]
    avgs=[sum(s[j+t*Q] for t in range(M))/M for j in range(Q)]
    E=sum(abs(z)**2 for z in avgs)/Q
    W=abs(sum(s)/(Q*M))**2
    # Explicit isometric-source relabeling using exact rational 2-adic V(n).
    state_groups=defaultdict(list)
    for n in range(Q*M):
        state_groups[(mod_odd(xs[n],Q)+Cs[n])%Q].append(s[n])
    assert set(state_groups)==set(range(Q))
    assert all(len(group)==M for group in state_groups.values())
    E_v=sum(abs(sum(group)/M)**2 for group in state_groups.values())/Q
    assert abs(E-E_v)<1e-12
    assert E+1e-9>=W
    return {'Q':Q,'M':M,'N':Q*M,'h':h,'R_float':round(E,12),
            'W_abs_squared_float':round(W,12),
            'relabel_difference_float':round(abs(E-E_v),14)}


def borrow_test(xs,Cs):
    results=[]
    for k in (2,3,4,5):
        Q=1<<k;twoQ=2*Q
        groups={False:[],True:[]}
        for n in range(128,512):
            dv=(mod_odd(xs[n+Q],twoQ)+Cs[n+Q]
                -mod_odd(xs[n],twoQ)-Cs[n])%twoQ
            assert dv==Q
            dc=(Cs[n+Q]-Cs[n])%twoQ
            dx=mod_odd(xs[n+Q]-xs[n],twoQ)
            assert (dc+dx)%twoQ==Q
            L=dc%Q
            carry_bit=dc//Q
            phase_bit=dx//Q
            assert phase_bit==(carry_bit^(1 if L==0 else 0))
            dis=abs(float(xs[n+Q]-xs[n]))
            dis=min(dis,1-dis)
            phase=complex(cos(2*pi*float(xs[n+Q]-xs[n])),
                          sin(2*pi*float(xs[n+Q]-xs[n])))
            groups[L==0].append((dis,phase))
        out={'k':k,'Q':Q,'sample_first':128,'sample_last':511,'cases':384}
        for flag,data in groups.items():
            key='lower_carry_agrees' if flag else 'lower_carry_differs'
            out[key]={'count':len(data),
                     'fraction_distance_ge_quarter_float':
                     round(sum(d>=0.25 for d,_ in data)/len(data),8) if data else None,
                     'mean_return_character_abs_float':
                     round(abs(sum(p for _,p in data)/len(data)),8) if data else None}
        results.append(out)
    return results


def source_mass():
    closed=pi/4 + 5*sqrt(2)*pi/16 + 5*log(2)/8 + 5*sqrt(2)*log(1+sqrt(2))/8
    checks=[]
    for N in (128,512):
        exact=sum((source(n) for n in range(1,N+1)), Fraction(0))
        tail=closed-float(exact)
        assert 0<tail<1/N
        checks.append({'N':N,'rational_partial_float':round(float(exact),14),
                       'closed_minus_partial_float':round(tail,14),
                       'rigorous_tail_upper_bound':f'1/{N}'})
    for n in range(1,257):
        assert source(n)==four_poles(n)
    return {'closed_float':round(closed,14),'finite_checks':checks,
            'symbolic_proof_required':True}



def arbitrary_lag_clone():
    cases=[]
    for q in (3,5,6,10,12,24,40):
        ell=(q&-q).bit_length()-1
        mod=1<<(ell+1)
        for n in (0,7,43):
            old=isometric_v_mod(n,mod)
            new=isometric_v_mod(n+q,mod)
            source_block=0
            for j in range(1,q+1):
                source_block=(16*source_block+mod_odd(source(n+j),mod))%mod
            assert (new-old)%mod==(1<<ell)
            assert (source_block-old)%mod==(1<<ell)
            cases.append({'q':q,'n':n,'ell':ell,'holds':True})
    return {'cases':len(cases),'all_pass':True,'representative':cases[::3]}


def dyadic_shell_energy(xs,Q,M):
    assert len(xs)>=Q*M
    phases=[complex(cos(2*pi*float(x)),sin(2*pi*float(x))) for x in xs[:Q*M]]
    shell_sum=defaultdict(complex)
    for d in range(1,M):
        ell=(d&-d).bit_length()-1
        for j in range(Q):
            for t in range(M-d):
                shell_sum[ell]+=phases[j+(t+d)*Q]*phases[j+t*Q].conjugate()
    shell_contrib={str(a):2*val.real/(Q*M*M) for a,val in sorted(shell_sum.items())}
    R=1/M+sum(shell_contrib.values())
    avgs=[sum(phases[j+t*Q] for t in range(M))/M for j in range(Q)]
    e=sum(abs(v)**2 for v in avgs)/Q
    assert abs(R-e)<1e-10
    return {'Q':Q,'M':M,'N':Q*M,'diagonal':round(1/M,12),
            'real_signed_shell_contribution_float':{k:round(v,12) for k,v in shell_contrib.items()},
            'reconstructed_R_float':round(R,12),'direct_R_float':e}


def shadow_energy_controls():
    xs=[Fraction(n,(2*n-1)**4) for n in range(512)]
    data=[]
    for Q in (4,8,16):
        M=512//Q
        phases=[complex(cos(2*pi*float(x)),sin(2*pi*float(x))) for x in xs]
        e=sum(abs(sum(phases[j+t*Q] for t in range(M))/M)**2 for j in range(Q))/Q
        assert e>0.8
        data.append({'Q':Q,'M':M,'R_shadow_float':round(e,12)})
    return data


def run():
    # Main original rational trajectory. All x,C are exact Fractions/integers.
    xs,Cs=raw_orbit(545)
    for k in range(1,9):
        mod=1<<k
        for n in (0,1,7,73,128,293):
            assert (mod_odd(xs[n],mod)+Cs[n])%mod==isometric_v_mod(n,mod)
    return {'status':'OBSERVED-FINITE, exact-identity-controls plus floats',
            'source_original':True,'U0':'0',
            'triangle':triangle_tests(),
            'haar_seed_frequency_null':frequency_tests(),
            'source_mass':source_mass(),
            'real_original_energies_float':[energy(xs,Cs,Q,512//Q)
                                           for Q in (4,8,16)],
            'source_carry_borrow':[ *borrow_test(xs,Cs)],
            'arbitrary_lag_clone':arbitrary_lag_clone(),
            'dyadic_signed_shells_float':[dyadic_shell_energy(xs,Q,512//Q)
                                          for Q in (4,8,16)],
            'nonnormal_shadow_return_energy_float':shadow_energy_controls(),
            'normality':'OPEN',
            'warning':'Exact theorem proofs are separate. Circle characters and transcendental source mass are float diagnostics only; no certified asymptotic saving.'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
