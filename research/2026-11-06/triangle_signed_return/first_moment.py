"""Authentic BBP first-moment harmonic/gamma renormalization (stdlib exact controls).

The analytic digamma theorem and positivity proof appear in FIRST_MOMENT_THEOREM.md.
Floating high-precision values are displays only and are not proofs of limits.
"""
from fractions import Fraction as F
import json
from experiment import source

COEFFS=(4,-2,-1,-1)
DENOM_SHIFTS=(7,4,3,2)
ALPHAS=(F(1,8),F(1,2),F(5,8),F(3,4))
A=F(15,64)


def weighted_pole_coefficients():
    d=tuple(F(c)*(1-alpha) for c,alpha in zip(COEFFS,ALPHAS))
    assert sum(COEFFS)==0
    assert sum(d)/8==A
    assert sum(c*e for c,e in zip(COEFFS,DENOM_SHIFTS))==15
    assert sum(abs(c)*e**2 for c,e in zip(COEFFS,DENOM_SHIFTS))==241
    return d


def positive_remainder(n):
    if n<1:raise ValueError('n>=1')
    residual=n*source(n)-A/F(n)
    assert residual>0
    return residual


def exact_prefix(N):
    if N<1:raise ValueError('N>=1')
    total=F(0);harmonic=F(0)
    for n in range(1,N+1):
        total+=n*source(n)
        harmonic+=F(1,n)
    return total-A*harmonic


def source_shadow(n):
    def H(k): return F(k,(2*k-1)**4)
    return H(n)-16*H(n-1)


def run():
    weighted_pole_coefficients()
    for n in range(1,1025):positive_remainder(n)
    # Display constants from *analytically proved* expression, not fitted to samples.
    import mpmath as mp
    mp.mp.dps=65
    radical=mp.sqrt(2)
    B=(27+31*radical)*mp.pi/128+mp.mpf(39)/32*mp.log(2)+31*radical/64*mp.log(1+radical)
    out=[]
    for N in (128,512,1024):
        p=exact_prefix(N)
        pmp=mp.mpf(p.numerator)/p.denominator
        tail=B-pmp
        assert tail>0 and tail<mp.mpf(241)/(288*N)
        out.append({'N':N,'rational_prefix_decimal_diagnostic':mp.nstr(pmp,25),
                    'B_minus_prefix_decimal_diagnostic':mp.nstr(tail,25),
                    'rigorous_tail_bound':f'241/{288*N}',
                    'symbolic_theorem_required':True})
    # H-shadow has source decay O(n^-3); its n-weighted source has no log divergence.
    shadow=[source_shadow(n) for n in (4,8,16,32)]
    return {'original_U0':'0', 'original_four_poles':True,
            'linear_harmonic_coefficient_exact':'15/64',
            'source_renormalized_residue_B_numeric':mp.nstr(B,40),
            'B_symbolic':'((27+31*sqrt(2))*pi)/128 + (39*log(2))/32 + (31*sqrt(2)*log(1+sqrt(2)))/64',
            'gamma_coefficient_in_log_N_renormalization':'15/64',
            'exact_source_moment_tail_results':out,
            'shadow_source_weighted_moment_coefficient':'0',
            'shadow_source_samples':[[n,str(s)] for n,s in zip((4,8,16,32),shadow)],
            'claim_status':'PROVED LOCAL symbolic theorem / OBSERVED FINITE rational controls',
            'real_weyl_saving':'OPEN'}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
