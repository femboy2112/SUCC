"""Deterministic source-pinned exact development/heldout receipts; --verify replay.

Preregistration happened before these p-class and Y/Z holdouts. Source
coefficients are exact Fraction and no pi digits are imported anywhere.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import gcd, log, isqrt
from hashlib import sha256
from pathlib import Path
import json
import sys
import prime_character as p
from symbolic_oracle import run_oracle

HERE=Path(__file__).resolve().parent
PREDECLARED_PRIMES=(29,37,43,47,61,67,71,73,83,89,101,103,107,113,127,131,137,139,149,151,157)


def stable_hash(value):
    return sha256(str(value).encode('utf-8')).hexdigest()


def ratio_hash(x):
    x=Q(x)
    return stable_hash(f'{x.numerator}/{x.denominator}')


def tent(x, q):
    x=Q(x)%1
    d=min(x,1-x)
    return max(Q(0), 1-q*d)


def current(phases,q):
    size=len(phases)
    return Q(q,size*size)*sum((tent(x-y,q) for x in phases for y in phases),Q(0))


def event_receipt():
    preds=[]
    for prime in PREDECLARED_PRIMES:
        for k in (1,2,3):
            if prime>8*k:
                full=p.direct_p_local_state(prime,k)
                expected=p.prime_quotient_prediction(prime,k)
                assert full==expected
                ang,rad=p.angle_radial()
                x=p.direct_p_local_state(prime,k,ang)
                y=p.direct_p_local_state(prime,k,rad)
                assert x==p._fmod(p.chi_minus4(prime%8)*p.state(k,ang),prime)
                assert y==p._fmod(p.state(k,rad),prime)
                assert (x+y)%prime==full
                preds.append({'p':prime,'class':prime%8,'k':k,
                              'pU_modp':full,'pY_modp':x,'pZ_modp':y})
    return preds


def source_state_receipt():
    out=[]
    a,r=p.angle_radial()
    for n in (97,191,373):
        u=p.state(n);y=p.state(n,a);z=p.state(n,r)
        assert y+z==u
        assert 0<z<p.radial_defect_bound(n)
        assert y.denominator%2==1
        out.append({'n':n,'u_sha256':ratio_hash(u),'primal_sha256':ratio_hash(y),
                    'radial_sha256':ratio_hash(z),'primal_denominator_bits':y.denominator.bit_length(),
                    'original_denominator_bits':u.denominator.bit_length(),
                    'radial_bound':str(p.radial_defect_bound(n))})
    return out


def current_receipt():
    out=[]
    a,_=p.angle_radial()
    for A,q in ((32,2),(32,8),(96,2),(192,2)):
        sx=list(p.states(2*A-1))[A:]
        sy=list(p.states(2*A-1,a))[A:]
        U=current(sx,q);Y=current(sy,q)
        error=abs(U-Y)
        ceiling=p.epoch_triangle_current_error_ceiling(A,q)
        assert error<ceiling
        out.append({'A':A,'q':q,'energy_original':str(U),'energy_primal':str(Y),
                    'exact_difference':str(error),'certified_ceiling':str(ceiling)})
    return out



def primal_denominator_receipt():
    out=[]
    a,_=p.angle_radial()
    for n in (128,257,509,911,1511):
        original=p.state(n)
        x=p.state(n,a)
        A,M,x2=p.angular_integer_lcm_state(n)
        assert x==x2==Q(A,M)
        out.append({'n':n,
                    'original_log_den_per_step':format(log(original.denominator)/n,'.12f'),
                    'primal_log_den_per_step':format(log(x.denominator)/n,'.12f'),
                    'primal_denominator_bits':x.denominator.bit_length(),
                    'primal_lcm_bits':M.bit_length(),
                    'primal_denominator_be_sha256':sha256(x.denominator.to_bytes((x.denominator.bit_length()+7)//8,'big')).hexdigest(),
                    'source_lcm_matches_independent':True})
    return out


def angular_fresh_pulse_receipt():
    items=[]
    for a in p.CLASSES:
        for mul in (17,37,71,113,191):
            x=p.prime_angular_event_normalizer(a,mul)
            y=p.direct_angular_event_normalizer(a,mul)
            assert x==y and x!=0
            assert (1 if x>0 else -1)==p.angular_pulse_sign(a,mul)
            items.append({'class':a,'m':mul,'sha256':ratio_hash(x),'sign':1 if x>0 else -1})
    return items


def angular_actual_p_survival():
    def primes_below(upper):
        sieve=[True]*upper
        sieve[0]=sieve[1]=False
        for d in range(2,isqrt(upper-1)+1):
            if sieve[d]:
                for j in range(d*d,upper,d):sieve[j]=False
        return [v for v in range(7,upper) if sieve[v]]
    ang,_=p.angle_radial()
    out=[]
    for n in (128,257,509):
        x=p.state(n,ang)
        tested=[];canceled=[]
        for prime in primes_below(8*n-6):
            if prime*prime<=8*n or p.angular_last_p_event(prime,n) is None:
                continue
            observed=p._fmod(prime*x,prime)
            predicted=p.predicted_angular_p_residue(prime,n)
            assert observed==predicted
            tested.append(f'{prime}:{observed}')
            if observed==0:canceled.append(prime)
        out.append({'n':n,'simple_pole_primes_tested':len(tested),
                    'finite_canceled_primes':canceled,'complete_residue_digest':stable_hash(';'.join(tested))})
    return out


def receipt():
    sym=run_oracle()
    results=event_receipt()
    states=source_state_receipt()
    energies=current_receipt()
    new_denoms=primal_denominator_receipt()
    new_pulses=angular_fresh_pulse_receipt()
    new_pchecks=angular_actual_p_survival()
    return {'authority':'exact finite observation and symbolic/paper; no pi normality',
            'source':'original four signed BBP Mellin poles, literal zero initial state',
            'preregistration_commit':'f41b75c8fbb28ef52e6e696f492ec7e6193e0c65',
            'parent_497_sha':'4383bd31340af700e312f13d7ef28af090c152d5',
            'tested_prime_events':len(results),
            'prime_receipts':results,'state_receipts':states,
            'current_receipts':energies,'symbolic':sym,
            'primal_denominator_receipts':new_denoms,
            'angular_new_pulse_receipts':new_pulses,
            'original_angular_full_p_residue_checks':new_pchecks,
            'negative_base4_first12':[str(p.negative_base4_source_term(k)) for k in range(12)],
            'source_never_replaced':True,
            'original_angular_primal_2_state':True,
            'pi_base16_normality':'OPEN','academic_world_first':'UNVERIFIED'}


if __name__=='__main__':
    got=receipt()
    path=HERE/'FINITE_RECEIPT.json'
    text=json.dumps(got,indent=2,sort_keys=True)+'\n'
    if '--verify' in sys.argv:
        assert path.exists() and path.read_text()==text, 'Exact receipt mismatch'
        print('PRIME_CHARACTER_PRIMAL_RECEIPT_VERIFIED',len(got['prime_receipts']),len(got['current_receipts']))
    else:
        path.write_text(text)
        print('PRIME_CHARACTER_PRIMAL_RECEIPT_WRITTEN',len(got['prime_receipts']),len(got['current_receipts']))
