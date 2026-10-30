"""SUCC research: exact BBP source Gaussian-rational and selected-seed/carry probes.

All claims are scoped to the original four-pole rational forcing; positivity
and analytic logarithm theorems appear in RESEARCH.md. This exact finite
instrument does NOT prove pi normality.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import comb

POLES=((0,4),(3,-2),(4,-1),(5,-1))

def rational(x,name='parameter'):
    if type(x) not in (int,Q):
        raise ValueError(f'exact rational {name} required')
    return Q(x)

def source_R(a):
    a=rational(a,'positive source clock')
    if a<=0: raise ValueError('positive source clock required')
    return sum((Q(c,a+d) for d,c in POLES),Q())

def source_r(n):
    if type(n) is not int or n<1: raise ValueError('positive source index required')
    return source_R(8*n-7)

def source_normalized_fourier(a,z):
    """Exact pair (real, imag) for E[exp(i*z*a*X)] with rational z.

    Gaussian rational arithmetic: inv(x+i*y)=(x-i*y)/(x²+y²).
    """
    a,z=rational(a,'clock'),rational(z,'Fourier frequency')
    if a<=0:raise ValueError('positive source clock required')
    re=Q(); im=Q()
    for d,c in POLES:
        x,y=a+d,-a*z
        denom=x*x+y*y
        re+=Q(c)*x/denom
        im+=-Q(c)*y/denom
    norm=source_R(a)
    return re/norm,im/norm

def source_inversion_ratio(a):
    """R(16/a)/R(a) on the positive continuous source clock, exactly."""
    a=rational(a,'positive source clock')
    if a<=0:raise ValueError('positive source clock required')
    return source_R(Q(16)/a)/source_R(a)

def oily_inversion_exponential(a):
    """Exact exp(D(a)) where D=log[R(16/a)/R(a)]-3log(a/4)."""
    a=rational(a,'positive source clock')
    if a<=0:raise ValueError('positive source clock required')
    return Q(16)*(a+3)*(a+5)/((3*a+16)*(5*a+16))

def oily_inversion_tanh_half(a):
    """Exact tanh(D(a)/2): source-specific bounded, odd inversion twist."""
    a=rational(a,'positive source clock')
    if a<=0:raise ValueError('positive source clock required')
    return (a*a-16)/(31*a*a+256*a+496)

def source_scaled_moment(a,m):
    """Exact E[(a X)^m] for natural m under the original positive source."""
    a=rational(a,'clock')
    if a<=0: raise ValueError('positive source clock required')
    if type(m) is not int or m<0:raise ValueError('nonnegative moment order required')
    from math import factorial
    return a**m*factorial(m)*sum((Q(c,(a+d)**(m+1)) for d,c in POLES),Q())/source_R(a)

def bbp_history(length,seed=0):
    if type(length) is not int or length<0:raise ValueError('nonnegative horizon required')
    u=rational(seed,'seed'); out=[u]
    for n in range(1,length+1):
        u=16*u+source_r(n)
        out.append(u)
    return tuple(out)

def seed_phase_shift(seed,step,h=1):
    """Argument modulo 1 of e(h U_step(seed))/e(h U_step(0))."""
    seed=rational(seed,'seed')
    if type(step) is not int or step<0:raise ValueError('nonnegative index required')
    if type(h) is not int or not h:raise ValueError('nonzero integer mode required')
    return (h*(16**step)*seed)%1

def literal_carries(length,seed=0):
    """Exact principal [0,1) logarithm branch and literal integer carries."""
    hist=bbp_history(length,seed)
    residues=tuple(u%1 for u in hist)
    carries=[None]
    for n in range(1,length+1):
        raw=16*residues[n-1]+source_r(n)
        carry=raw.numerator//raw.denominator
        assert raw-carry==residues[n]
        carries.append(carry)
    return residues,tuple(carries)

def mirror_phase_product_residue(n,seed=0,h=1):
    """Literal phase-product relative to two neutral-seed phases, exactly 0."""
    seed=rational(seed,'seed')
    if type(n) is not int or n<0:raise ValueError('nonnegative time required')
    if type(h) is not int or not h:raise ValueError('nonzero integer frequency required')
    base=bbp_history(n,0)[n]
    plus=bbp_history(n,seed)[n]
    minus=bbp_history(n,-seed)[n]
    return (h*(plus+minus-2*base))%1

def mirror_source_density_product_ratio(a,t):
    """Exact p_(a+t)(x) p_(a-t)(x)/p_a(x)^2, independent of x."""
    a,t=rational(a,'a'),rational(t,'t')
    if a<=0 or not 0<=t<a:raise ValueError('0<=t<a required')
    return source_R(a)**2/(source_R(a+t)*source_R(a-t))

def mirrored_branch_disagreement(n,midseed,perturbation):
    """Exact signed integer from principal logarithms of two seed shifts.

    J_n(delta)=frac(U_n(c+delta))+frac(U_n(c-delta))-2 frac(U_n(c)).
    This is in {-1,0,1} and retains the actual central BBP branch.
    """
    if type(n) is not int or n<0:raise ValueError('nonnegative time required')
    c=rational(midseed,'midpoint seed')
    delta=rational(perturbation,'perturbation seed')
    central=bbp_history(n,c)[-1]%1
    plus=bbp_history(n,c+delta)[-1]%1
    minus=bbp_history(n,c-delta)[-1]%1
    jump=plus+minus-2*central
    if jump.denominator!=1 or jump not in (-1,0,1):
        raise ArithmeticError('invalid logarithmic branch label')
    return int(jump)

def mirrored_branch_probabilities(central_fraction):
    """Exact law of J under uniform seed perturbation over [0,1].

    Keys -1,0,+1. By integer base16 windings, theta={16^n delta}
    is Haar uniform whenever delta is Haar uniform.
    """
    x=rational(central_fraction,'central phase')
    if not 0<=x<1:raise ValueError('fractional phase must be in [0,1)')
    plus=max(Q(0),1-2*x)
    minus=max(Q(0),2*x-1)
    return {-1:minus,0:1-plus-minus,1:plus}

def mirrored_branch_q3_character(central_fraction):
    """Exact q=3 expectation as (a,b) representing a+i*sqrt(3)*b.

    Re=1-3/2*abs(1-2x), Im=sqrt(3)*(1-2x)/2.
    """
    law=mirrored_branch_probabilities(central_fraction)
    re=law[0]-Q(1,2)*(law[-1]+law[1])
    im_sqrt3=Q(1,2)*(law[1]-law[-1])
    return re,im_sqrt3

def grade_weights(n,a):
    if type(n) is not int or n<0:raise ValueError('nonnegative trial count')
    a=rational(a,'source clock')
    if a<=0:raise ValueError('positive source clock')
    return tuple(Q(comb(n,j))*sum((Q((-1)**k*comb(j,k))*source_R(a+8*(n-j+k))
                  for k in range(j+1)),Q())/source_R(a) for j in range(n+1))

def score_weights(n,a):
    """Exact signed derivative of the source-conditioned Pascal coefficients."""
    if type(n) is not int or n<0:raise ValueError('nonnegative trial count')
    a=rational(a,'clock')
    if a<=0:raise ValueError('positive clock')
    def deriv(x):return sum((-Q(c,(x+d)**2) for d,c in POLES),Q())
    Z,Zp=source_R(a),deriv(a)
    ans=[]
    for j in range(n+1):
        val=sum((Q((-1)**k*comb(j,k))*source_R(a+8*(n-j+k)) for k in range(j+1)),Q())
        prime=sum((Q((-1)**k*comb(j,k))*deriv(a+8*(n-j+k)) for k in range(j+1)),Q())
        ans.append(Q(comb(n,j))*(prime/Z-val*Zp/Z**2))
    return tuple(ans)

def signed_pascal_log_derivative_group(n,a,seed=0,h=1):
    """Group-algebra coefficient map for d/deta log E exp(eta M)|eta=0.

    Each key is the exact phase residue; finite coefficients are nonnegative.
    """
    if type(h) is not int or not h:raise ValueError('nonzero integer mode')
    states=bbp_history(2*n,seed)
    weights=grade_weights(n,a)
    out={}
    for j,w in enumerate(weights):
        residue=(h*states[n+j])%1
        out[residue]=out.get(residue,Q())+w
    return {k:v for k,v in out.items() if v}

def signed_pascal_log_cross_group(n,a,seed=0,h=1):
    """Group algebra for d_a d_eta of the root-free signed log generator."""
    if type(h) is not int or not h:raise ValueError('nonzero integer mode')
    states=bbp_history(2*n,seed)
    weights=score_weights(n,a)
    out={}
    for j,w in enumerate(weights):
        residue=(h*states[n+j])%1
        out[residue]=out.get(residue,Q())+w
    return {k:v for k,v in out.items() if v}

if __name__=='__main__':
    assert source_r(1)==Q(47,15)
    assert source_normalized_fourier(Q(1000),Q(1))[0]>0
    assert mirror_phase_product_residue(10,Q(1,7))==0
    print('OILY_LOGARITHM_EXACT_CORE_PASS')
