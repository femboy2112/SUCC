"""Independent replayable finite exact receipt; not an asymptotic proof."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from hashlib import sha256
from json import dump,load
from math import gcd,log
from pathlib import Path
import importlib.util

HERE=Path(__file__).resolve().parent
MODULE=HERE/'frobenius_prime.py'
spec=importlib.util.spec_from_file_location('prime_echo',MODULE)
f=importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)


def sieve(n:int):
    p=[True]*(n+1);p[0]=p[1]=False
    for j in range(2,int(n**.5)+1):
        if p[j]:
            for k in range(j*j,n+1,j):p[k]=False
    return [j for j in range(n+1) if p[j]]


def digest(x:str):return sha256(x.encode('ascii')).hexdigest()

def digest_large_rational(a:int,b:int)->str:
    aa=a.to_bytes((a.bit_length()+8)//8+1,'big',signed=True)
    bb=b.to_bytes((b.bit_length()+7)//8+1,'big')
    return sha256(len(aa).to_bytes(8,'big')+aa+len(bb).to_bytes(8,'big')+bb).hexdigest()


def receipt()->dict:
    tab={str(a):[[m,str(C)] for m,c,w,C in f.universal_pulse_states(a,7)]
         for a in f.ALLOWED_CLASSES}
    big=[]
    for N in (128,257,509,911,1511):
        A,M,D=f.integer_lcm_state(N)
        allp=sieve(8*N+1)
        eligible=[]; missing=[]; comparisons=[]
        for p in allp:
            if p<=5 or p<=N//10 or p*p<=8*N or not f.eligible_source_prime(p,N):continue
            eligible.append(p)
            if D%p:missing.append(p)
            predicted=f.predicted_p_residue(p,N)
            if (predicted==0)!=(D%p!=0):
                raise AssertionError('independent denominator and prime shadow disagree')
            comparisons.append((p,predicted))
        big.append({
            'N':N,'denominator_binary_bits':D.bit_length(),
            'cumulative_LCM_binary_bits':M.bit_length(),
            'log_den_per_N_FLOAT_DIAGNOSTIC':format(log(D)/N,'.13f'),
            'log_lcm_per_N_FLOAT_DIAGNOSTIC':format(log(M)/N,'.13f'),
            'denominator_divides_LCM': M%D==0,
            'source_lift_sha256':digest_large_rational(A,M),
            'eligible_large_source_primes':len(eligible),
            'cancelled_large_source_primes':missing,
            'prime_residue_sequence_sha256':digest(str(comparisons))
        })
    delta=[]
    U=V=Q(0)
    for n in range(1,258):
        U=16*U+f.source(n)
        V=16*V+f.dual_source(n)
        if n in (1,3,17,101,257):
            e=2*U-V
            if not Q(0)<e<Q(1,8*n+4):raise AssertionError('harmonic bound fails')
            delta.append({'N':n,'positive_defect_sha256':digest(str(e)),
                          'under_exact_bound':str(Q(1,8*n+4))})
    import sys
    sys.path.insert(0,str(HERE))
    from symbolic_oracle import verify
    return {
        'source':'original BBP four poles, U_0=0; no pi digits',
        'claim':'universal pulse and sharp log denominator exponent, paper theorem',
        'novelty_priority':'UNVERIFIED; new-to-SUCC',
        'pi_normality_proved':False,'RH_proved':False,
        'development_first_pulse_normalizers':tab,
        'fresh_declared_source_holdouts':big,
        'strict_finite_null_defects':delta,
        'independent_sympy_exact_oracle':verify(),
        'finite_sign_checks_not_universal_proof':
           {str(a):all((1 if c>0 else -1)==f.pulse_sign(a,m)
                       for m,_,_,c in f.universal_pulse_states(a,808))
            for a in f.ALLOWED_CLASSES},
        'observed_negative_controls':{
            'N128_missing_p':37,'N257_missing_p':47,
            'N509_missing_p':[113,151],
            'no_uniform_N_exception_free_claim':True,
            'p_squared_regime_unclaimed':True,
        }
    }

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true')
    args=ap.parse_args()
    data=receipt()
    dst=HERE/'FINITE_RECEIPT.json'
    if args.verify:
        with dst.open(encoding='utf-8') as h:expected=load(h)
        assert data==expected,'receipt mismatch'
        print('ORIGINAL_BBP_FROBENIUS_RECEIPT_REPLAY_PASS')
    else:
        with dst.open('w',encoding='utf-8') as h:dump(data,h,indent=2,sort_keys=True);h.write('\n')
        print('FINITE_RECEIPT_WRITTEN',dst)
