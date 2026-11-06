"""Separate formulations of source, dynamic update, and Gamma source potential.
Uses direct polynomial source and convolution, not hologram.py's state builder.
The optional mpmath probes are numerical calibration (never rigorous proof).
"""
from fractions import Fraction
import json

def original_pole(n):
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def rational_source(n):
    return Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def direct_state(n):
    return sum((16**(n-j)*rational_source(j) for j in range(1,n+1)),Fraction(0))

def check():
    c=0
    for n in (1,2,3,4,5,13,31,61,127,307):
        assert original_pole(n)==rational_source(n)
        c+=1
    for n in (0,1,2,3,7,17,37,73):
        u=direct_state(n)
        d=u.denominator
        b=u.numerator//u.denominator
        x=u-b
        for k in (max(1,d.bit_length()),max(1,d.bit_length()+7)):
            m=2**k
            v=u.numerator*pow(d,-1,m)%m
            cc=b%m
            # Different-formula shadow: q-s = U - floor(U), d(q-s) = numerator.
            reconstructed=(d*(v-cc))%m
            assert reconstructed==x.numerator,(n,k,reconstructed,x.numerator)
            c+=1
    prime_witnesses=[]
    for N,p,n in [(9,11,3),(16,17,3),(31,37,5),(64,67,17),(127,131,33),(257,263,66)]:
        # IMPORTANT: predeclared p,n guesses are validated against actual first poles.
        assert N<p<2*N
        u=direct_state(n)
        assert u.denominator%p==0 and u.denominator>N,(N,p,n)
        # first occurrence found by checking all prior states.
        assert all(direct_state(j).denominator%p for j in range(n))
        prime_witnesses.append((N,p,n,u.denominator.bit_length()))
        c+=1
    r={"exact_fraction_oracle_checks":c,"prime_witnesses":prime_witnesses}
    try:
        import mpmath as mp
        mp.mp.dps=85
        weights=(4,-2,-1,-1);poles=(7,4,3,2)
        errors=[]
        for n in (1,2,5,13,29):
            h=sum((rational_source(j) for j in range(1,n+1)),Fraction())
            hmp=mp.mpf(h.numerator)/h.denominator
            psi=sum((mp.mpf(w)/8*(mp.digamma(n+1-mp.mpf(a)/8)-mp.digamma(1-mp.mpf(a)/8)) for w,a in zip(weights,poles)),mp.mpf(0))
            err=abs(hmp-psi)
            assert err<mp.mpf('1e-76'),(n,err)
            errors.append(mp.nstr(err,5))
        analytic=-sum((mp.mpf(w)/8*mp.digamma(1-mp.mpf(a)/8) for w,a in zip(weights,poles)),mp.mpf(0))
        silver=(4+5*mp.sqrt(2))*mp.pi/16+mp.mpf(5)/8*mp.log(2)+5*mp.sqrt(2)/8*mp.log(1+mp.sqrt(2))
        assert abs(analytic-silver)<mp.mpf('1e-76')
        r['mpmath_gamma_calibration']={'precision_dps':mp.mp.dps,'finite_H_errors':errors,'silver_difference':mp.nstr(abs(analytic-silver),5),'unweighted_source_sum':mp.nstr(analytic,38)}
    except ImportError:
        r['mpmath_gamma_calibration']='unavailable; analytic proof in THEOREMS.md'
    return r

if __name__=='__main__':print(json.dumps(check(),sort_keys=True,indent=2))
