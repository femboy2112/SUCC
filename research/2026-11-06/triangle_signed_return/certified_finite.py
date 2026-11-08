"""Finite rigorous rational energy enclosure; NOT an asymptotic BBP/normality bound.

Proves a uniform absolute error for finite R by Machin bounds, exact quantization,
Taylor's theorem, and a rational fiber energy.  Only the printed decimal is float.
"""
from fractions import Fraction as F
from math import factorial
import json
from experiment import raw_orbit


def arctan_bounds_inverse(a: int, terms: int):
    assert a>=2 and terms>=1
    value=sum(((-1)**j*F(1,(2*j+1)*a**(2*j+1))
               for j in range(terms)),F(0))
    rem=F(1,(2*terms+1)*a**(2*terms+1))
    return (value,value+rem) if terms%2==0 else (value-rem,value)


def pi_interval():
    low5,high5=arctan_bounds_inverse(5,8)
    low239,high239=arctan_bounds_inverse(239,4)
    lower=16*low5-4*high239
    upper=16*high5-4*low239
    assert lower<upper<F(22,7)
    assert upper-lower < F(1,10**10)
    return lower,upper


def error_budget():
    lo,hi=pi_interval()
    angle=(F(44,7)*F(1,1<<16)+(hi-lo))
    # x floor quantization, plus pi midpoint uncertainty 2*Epi=(hi-lo)
    tail_cos=F(44,7)**29/factorial(29)
    tail_sin=F(44,7)**30/factorial(30)
    total=2*angle+tail_cos+tail_sin
    assert total<F(1,5000)
    eps=F(1,5000)
    R_err=eps*(2+eps)
    assert R_err<F(1,2400)
    return (lo+hi)/2, eps, F(1,2400), total


def approximate_real_character(x,h,pi_mid):
    # For h integer, {h*x} is an exact rational in [0,1).
    z=(h*x)%1
    quant=(z.numerator*(1<<16))//z.denominator
    theta=2*pi_mid*F(quant,1<<16)
    p=F(1)
    factor=theta*theta
    c=F(0);s=F(0)
    for j in range(15):
        term=(-1)**j*p
        c+=term/factorial(2*j)
        s+=term*theta/factorial(2*j+1)
        p*=factor
    return c,s


def certified_energy(phases,Q,M,h, pi_mid, R_err):
    assert Q*M<=len(phases)
    # All rational operations; no floating evaluation enters the verdict.
    approx=[approximate_real_character(x,h,pi_mid) for x in phases[:Q*M]]
    R=F(0)
    for j in range(Q):
        re=sum((approx[j+t*Q][0] for t in range(M)),F(0))
        im=sum((approx[j+t*Q][1] for t in range(M)),F(0))
        R+=(re*re+im*im)/M**2
    R/=Q
    diag=F(1,M)
    if R+R_err<diag:
        verdict='CERTIFIED_BELOW_DIAGONAL'
    elif R-R_err>diag:
        verdict='CERTIFIED_ABOVE_DIAGONAL'
    else:
        verdict='AMBIGUOUS'
    return {'Q':Q,'M':M,'N':Q*M,'h':h,'R_center_float':round(float(R),12),
            'R_abs_error_less_than':'1/2400',
            'diagonal_exact':f'1/{M}',
            'verdict':verdict,
            'signed_gap_center_float':round(float(R-diag),12)}


def run():
    pi_mid,eps,err,component=error_budget()
    phases,_=raw_orbit(769)
    targets=[(512,1,4),(512,1,8),(512,1,16),
             (768,2,4),(768,2,8),(768,2,16)]
    cases=[certified_energy(phases,Q,N//Q,h,pi_mid,err)
           for N,h,Q in targets]
    return {'certificate':'RIGOROUS_FINITE_RATIONAL_INTERVAL',
            'original_four_poles':True,'literal_zero_seed':True,
            'machin_arctan_terms':{'inverse5':8,'inverse239':4},
            'quantization_bits':16,'taylor_max_cos_degree':28,
            'taylor_max_sin_degree':29,
            'single_phase_error_less_than':'1/5000',
            'energy_error_less_than':'1/2400',
            'predeclared_uniform_component_bound_less_than':str(component.numerator)+'/'+str(component.denominator),
            'cases':cases,'pi_base16_normality':'OPEN',
            'scope':'finite only; analytic Taylor/Machin bounds justify each sign, not infinite cancellation'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
