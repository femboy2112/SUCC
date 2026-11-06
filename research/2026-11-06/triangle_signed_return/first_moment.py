"""Authentic BBP first-moment harmonic/gamma renormalization (stdlib exact controls).

The analytic digamma theorem and positivity proof appear in FIRST_MOMENT_THEOREM.md.
Floating high-precision values are displays only and are not proofs of limits.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
import json
from certified_finite import arctan_bounds_inverse
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
    # Independent stdlib-only high precision DECIMAL display: not proof arithmetic.
    # Machin bounds now have >75 digits of rigorously controlled input precision.
    l5,u5=arctan_bounds_inverse(5,64)
    l239,u239=arctan_bounds_inverse(239,20)
    pi_lo=16*l5-4*u239;pi_hi=16*u5-4*l239
    assert 0<pi_hi-pi_lo<F(1,10**78)
    with localcontext() as context:
        context.prec=75
        middle=(pi_lo+pi_hi)/2
        pi_dec=D(middle.numerator)/D(middle.denominator)
        radical=D(2).sqrt()
        B=(D(27)+31*radical)*pi_dec/128+D(39)/32*D(2).ln()+D(31)*radical/64*(1+radical).ln()
        out=[]
        for N in (128,512,1024):
            p=exact_prefix(N)
            pdec=D(p.numerator)/D(p.denominator)
            tail=B-pdec
            # Decimal checks corroborate; analytic B and rational tail bound prove.
            assert tail>0 and tail<D(241)/(D(288)*N)
            out.append({'N':N,'rational_prefix_decimal_diagnostic':format(pdec,'.25g'),
                        'B_minus_prefix_decimal_diagnostic':format(tail,'.25g'),
                        'rigorous_tail_bound':f'241/{288*N}',
                        'symbolic_theorem_required':True})
        B_display=format(B,'.40g')
    # H-shadow has source decay O(n^-3); its n-weighted source has no log divergence.
    shadow=[source_shadow(n) for n in (4,8,16,32)]
    return {'original_U0':'0', 'original_four_poles':True,
            'linear_harmonic_coefficient_exact':'15/64',
            'source_renormalized_residue_B_numeric':B_display,
            'B_symbolic':'((27+31*sqrt(2))*pi)/128 + (39*log(2))/32 + (31*sqrt(2)*log(1+sqrt(2)))/64',
            'gamma_coefficient_in_log_N_renormalization':'15/64',
            'exact_source_moment_tail_results':out,
            'shadow_source_weighted_moment_coefficient':'0',
            'shadow_source_samples':[[n,str(s)] for n,s in zip((4,8,16,32),shadow)],
            'claim_status':'PROVED LOCAL symbolic theorem / OBSERVED FINITE rational controls',
            'real_weyl_saving':'OPEN'}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
