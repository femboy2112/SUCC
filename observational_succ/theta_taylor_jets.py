"""Certified even Taylor jets from the authentic Gaussian integer-theta source.

Only rational arithmetic bounds, no zeta/xi or zero-list oracle.
Proved in research/2026-10-14/THETA_EVEN_JETS_CAVE.md.
Pure Python stdlib; numerical decoders are explicitly separate.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import factorial, isqrt
from functools import lru_cache
from dataclasses import dataclass

class JetError(ValueError):
    pass

SCALE = 10**44
S = Q(SCALE)

def exact(v):
    if type(v) not in (int, Q):
        raise JetError('only exact rational inputs are admissible')
    return Q(v)

def down(x):
    x=exact(x)
    return Q((x.numerator*SCALE)//x.denominator, SCALE)

def up(x):
    x=exact(x)
    return -down(-x)

@lru_cache(maxsize=10000)
def log_interval(t:Q, order=48):
    t=exact(t)
    if not Q(1)<=t<=Q(16):
        raise JetError('log t certified only on 1<=t<=16')
    if type(order)!=int or not 1<=order<=120:
        raise JetError('invalid log order')
    scale=0
    while t>=2:
        t/=2
        scale+=1
    def log_unit(u):
        z=(u-1)/(u+1)
        zl,zh=down(z),up(z)
        xlo,xhi=zl,zh
        total_lo,total_hi=Q(),Q()
        for j in range(order):
            total_lo+=down(2*xlo/Q(2*j+1))
            total_hi+=up(2*xhi/Q(2*j+1))
            xlo=down(xlo*zl*zl)
            xhi=up(xhi*zh*zh)
        remainder=up(2*xhi/(Q(2*order+1)*(1-zh*zh)))
        return down(total_lo),up(total_hi+remainder)
    v0,v1=log_unit(t)
    c0,c1=log_unit(Q(2))
    return down(v0+scale*c0),up(v1+scale*c1)

@lru_cache(maxsize=10)
def pi_interval(order=36):
    if type(order)!=int or not 4<=order<=70:
        raise JetError('invalid pi order')
    def atan(z):
        a=sum(((-1)**j*z**(2*j+1)/Q(2*j+1) for j in range(order)),Q())
        n=(-1)**order*z**(2*order+1)/Q(2*order+1)
        return min(a,a+n),max(a,a+n)
    a,b=atan(Q(1,5));c,d=atan(Q(1,239))
    return down(16*a-4*d),up(16*b-4*c)

@lru_cache(maxsize=25000)
def exp_minus_point(x: Q):
    """Outward rational e^-x via dyadic scaling + fixed-decimal interval series.

    Each positive Taylor term is bounded with directed floor/ceiling.
    The geometric first-omitted-term envelope bounds the infinite tail.
    """
    x=exact(x)
    if not 0<=x<=2000:
        raise JetError('exp argument outside declared certificate domain')
    m=0
    y=x
    while y>Q(1,2):
        y/=2
        m+=1
    yl,yh=down(y),up(y)
    lo,hi=Q(1),Q(1)
    termlo,termhi=Q(1),Q(1)
    order=48
    for j in range(1,order+1):
        termlo=down(termlo*yl/j)
        termhi=up(termhi*yh/j)
        lo+=termlo
        hi+=termhi
    next_hi=up(termhi*yh/(order+1))
    hi+=up(next_hi/(1-yh/Q(order+2)))
    for _ in range(m):
        lo=down(lo*lo)
        hi=up(hi*hi)
    return down(1/hi),up(1/lo)

def exp_minus_interval(lo,hi):
    lo,hi=exact(lo),exact(hi)
    if lo<0 or lo>hi:
        raise JetError('negative or swapped exp interval')
    return exp_minus_point(hi)[0],exp_minus_point(lo)[1]


def exp_interval_nonneg(x):
    x=exact(x)
    if not 0<=x<=60:
        raise JetError('exp positive-range certificate exceeded')
    elo,ehi=exp_minus_point(x)
    if elo==0:
        raise JetError('positive exp inverse needs tighter precision')
    return down(1/ehi),up(1/elo)


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q
    def __post_init__(self):
        if self.lo>self.hi:
            raise JetError('reversed certified interval')
    def __add__(self,other):
        other=iv(other)
        return Interval(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __sub__(self,other):
        other=iv(other)
        return Interval(self.lo-other.hi,self.hi-other.lo)
    def __mul__(self,other):
        other=iv(other)
        vals=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return Interval(min(vals),max(vals))
    __rmul__=__mul__


def iv(obj):
    if isinstance(obj,Interval):return obj
    return Interval(exact(obj),exact(obj))

@lru_cache(maxsize=6000)
def source_weight(t:Q,modes:int):
    """Finite sum psi_modes(t)*t^-3/4, exact rational outer interval."""
    t=exact(t)
    if not Q(1)<=t<=Q(12):
        raise JetError('quadrature endpoint outside domain')
    if type(modes)!=int or not 1<=modes<=5:
        raise JetError('unsupported Gaussian mode cutoff')
    ll,lh=log_interval(t)
    p0,p1=pi_interval()
    total_lo,total_hi=Q(),Q()
    for n in range(1,modes+1):
        x0=p0*n*n*t+Q(3,4)*ll
        x1=p1*n*n*t+Q(3,4)*lh
        lo,hi=exp_minus_interval(x0,x1)
        total_lo+=lo
        total_hi+=hi
    return Interval(total_lo,total_hi)


def time_tail_upper(j:int,T:Q):
    # 2 e^-3T / (4^j(2j)!) int upper polynomial t^j with log t<=sqrt(t)
    T=exact(T)
    e=exp_minus_point(3*T)[1]
    s=sum((T**k/(factorial(k)*3**(j+1-k)) for k in range(j+1)),Q())
    return up(Q(2)*e*factorial(j)*s/(4**j*factorial(2*j)))


def mode_tail_upper(j:int,N:int):
    # n>=N+1: psi_tail(t) <=2 exp(-3(N+1)^2 t), t>=1,
    # log t <= t-1, t^-3/4 <=1, and Gamma moments integrate exactly.
    rate=3*(N+1)**2
    return up(2*exp_minus_point(Q(rate))[1]/(4**j*rate**(2*j+1)))


@lru_cache(maxsize=10)
def jets(degree:int=16,modes:int=3,T:int=8,cells:int=384):
    """Enclose a_0..a_degree of F(z)=xi(1/2+z), via original theta.

    All bound widths are rational from source-prefix monotone cell bounds,
    plus missing t>T and n>modes analytic tails. Terms never read xi or zeros.
    """
    if type(degree)!=int or not 0<=degree<=24:
        raise JetError('invalid requested jet degree')
    if type(modes)!=int or not 1<=modes<=5:
        raise JetError('invalid mode cutoff')
    if type(T)!=int or not 2<=T<=12:
        raise JetError('invalid integration endpoint')
    if type(cells)!=int or not 8<=cells<=4096:
        raise JetError('invalid quadrature resolution')
    xs=tuple(Q(1)+(Q(T-1)*i/cells) for i in range(cells+1))
    ws=tuple(source_weight(x,modes) for x in xs)
    ls=tuple(log_interval(x) for x in xs)
    step=Q(T-1,cells)
    lower=[Q() for j in range(degree+1)]
    upper=[Q() for j in range(degree+1)]
    for k in range(cells):
        left_log_lo=ls[k][0]
        right_log_hi=ls[k+1][1]
        pow_lo=pow_hi=Q(1)
        for j in range(degree+1):
            if j:
                pow_lo*=left_log_lo**2
                pow_hi*=right_log_hi**2
            denom=Q(4**j*factorial(2*j))
            lower[j]+=step*ws[k+1].lo*pow_lo/denom
            upper[j]+=step*ws[k].hi*pow_hi/denom
    b=tuple(Interval(down(lower[j]),
                     up(upper[j]+time_tail_upper(j,Q(T))+mode_tail_upper(j,modes)))
            for j in range(degree+1))
    a=[Interval(Q(1,2),Q(1,2))-Q(1,4)*b[0]]
    for j in range(1,degree+1):
        a.append(b[j-1]-Q(1,4)*b[j])
    return {'source':'authentic_unweighted_integer_Gaussian_theta',
            'degree':degree,'modes':modes,'T':T,'cells':cells,
            'b':b,'a':tuple(a),'RH_proved':False,'nontrivial_zero_inputs':False}


def _authenticated(data:dict):
    """Replay source/tail certificate, refuse substituted coefficient arrays.

    This protects provenance WITHIN the stated mathematical model; it is
    not physical authentication or a claim that Python dictionaries are secure.
    """
    if type(data) is not dict or data.get('source') != 'authentic_unweighted_integer_Gaussian_theta':
        raise JetError('unknown original theta source')
    try:
        args=tuple(data[k] for k in ('degree','modes','T','cells'))
        replay=jets(*args)
    except (KeyError,TypeError,ValueError) as exc:
        raise JetError('invalid source replay contract') from exc
    if data.get('a')!=replay['a'] or data.get('b')!=replay['b']:
        raise JetError('source coefficient forgery or stale certificate')


def global_B_bound(x:Q):
    """B(x) <= exp(x^2/8) for real x>=0, from source Gaussian tail."""
    x=exact(x)
    if not 0<=x<=21:
        raise JetError('global source bound at unsupported comparison radius')
    return exp_interval_nonneg(x*x/8)[1]


def rouche_center_certificate(data:dict,R, comparison=10):
    """Certified zero-free |z|<=R via a0 dominance; source theta, not zero list.

    Remainder after D even F-jets uses b_D + positive B-tail, bounded from
    the independently proven entire-source majorant B(comparison).
    """
    _authenticated(data)
    R=exact(R)
    comparison=exact(comparison)
    if not 0<R<comparison<=21:
        raise JetError('comparison radius must strictly exceed contour radius')
    D=data['degree']
    b=data['b'];a=data['a']
    known=sum((max(abs(x.lo),abs(x.hi))*R**(2*j)
               for j,x in enumerate(a) if j>0),Q())
    B_bound=global_B_bound(comparison)
    unseen_B_tail=B_bound*(R/comparison)**(2*(D+1))
    # F(z)-sum_(j=0)^D a_j z^(2j)=b_D z^(2D+2)+(z²-1/4) sum_(j>D)b_j z^(2j)
    rem=b[D].hi*R**(2*D+2)+(R*R+Q(1,4))*unseen_B_tail
    margin=a[0].lo-known-rem
    return {'radius':R,'degree':D,'a0_lower':a[0].lo,
            'known_nonconstant_upper':known,'analytic_tail_upper':rem,
            'margin_lower':margin,'certified_zero_free':margin>0,
            'zero_count':0 if margin>0 else None,'RH_proved':False,
            'nontrivial_zero_inputs':False}


def general_taylor_disk(data:dict,R, comparison=10):
    """Certified bound on F-P_D everywhere in |z|<=R."""
    _authenticated(data)
    R=exact(R);comparison=exact(comparison)
    if not 0<=R<comparison<=21:raise JetError('comparison radius/domain')
    D=data['degree'];b=data['b']
    tail=b[D].hi*R**(2*D+2)+(R*R+Q(1,4))*global_B_bound(comparison)*(R/comparison)**(2*(D+1))
    return {'radius':R,'degree':D,'remainder_absolute_upper':tail,
            'nontrivial_zero_inputs':False}


def certified_midpoint_polynomial(data:dict,R,comparison=13):
    """Source-certified rational P_D, with a UNIFORM complex disk error radius.

    Polynomial coefficient uncertainty and true analytic truncation are
    accumulated separately; neither may be silently thrown away.
    """
    _authenticated(data)
    R=exact(R)
    tail=general_taylor_disk(data,R,comparison)['remainder_absolute_upper']
    coeffs=tuple((v.lo+v.hi)/2 for v in data['a'])
    observer_error=sum(((v.hi-v.lo)/2)*R**(2*j)
                       for j,v in enumerate(data['a']))
    return {'degree':data['degree'],'radius':R,
            'coefficient_midpoints':coeffs,
            'finite_observer_error':observer_error,
            'analytic_tail':tail,
            'uniform_complex_error':observer_error+tail,
            'true_source_is_unique':True,
            'finite_observer_identifies_full_curve':False,
            'RH_proved':False}


def stieltjes_moments(data:dict,up_to:int=3):
    """m_j=4^j(2j)! b_j = ∫ (log t)^(2j) psi(t)t^-3/4 dt."""
    _authenticated(data)
    if type(up_to)!=int or not 0<=up_to<=data['degree']:
        raise JetError('invalid Stieltjes moment depth')
    return tuple(iv(4**j*factorial(2*j))*data['b'][j] for j in range(up_to+1))


def source_hankel_two_by_two(data:dict):
    """Hankel PSD margins, certified interval for first and shifted minor."""
    moments=stieltjes_moments(data,3)
    det=moments[0]*moments[2]-moments[1]*moments[1]
    shifted=moments[1]*moments[3]-moments[2]*moments[2]
    return {'moment_intervals':moments,
            'hankel_det':det,'shifted_hankel_det':shifted,
            'both_strictly_positive_certified':det.lo>0 and shifted.lo>0,
            'full_Hankel_PSD_proved_analytically':True,
            'completed_Weil_PSD_proved':False,'RH_proved':False}



def unseen_moment_lower(data:dict,k:int=0):
    """Predictive Stieltjes constraint from only m_k and m_(k+1).

    For the authentic theta pushforward measure y=(log t)^2>=0,
    m_(k+2) >= m_(k+1)^2/m_k by Cauchy-Schwarz. The m_(k+2)
    measurement is NOT used to construct this lower bound.
    """
    if type(k)!=int or not 0<=k<=data['degree']-2:
        raise JetError('next moment outside finite observer horizon')
    m=stieltjes_moments(data,k+1)
    prev,nxt=m[k],m[k+1]
    if prev.hi<=0 or nxt.lo<0:
        raise JetError('source positivity is not certified')
    floor=nxt.lo*nxt.lo/prev.hi
    return {'observed_moments':(k,k+1),'predicted_next_index':k+2,
            'certified_lower':floor,'genuine_positive_theta_source':True,
            'all_global_curves_unique_from_finite_data':False,
            'completed_Weil_PSD_proved':False}


def B_real_interval(data:dict,x,comparison=13):
    """B(x) on REAL x, using its source-nonnegative even coefficients."""
    _authenticated(data)
    x=abs(exact(x));comparison=exact(comparison)
    if not 0<=x<comparison:raise JetError('real kernel comparison domain')
    prefix_lo=sum((v.lo*x**(2*j) for j,v in enumerate(data['b'])),Q())
    prefix_hi=sum((v.hi*x**(2*j) for j,v in enumerate(data['b'])),Q())
    tail=global_B_bound(comparison)*(x/comparison)**(2*(data['degree']+1))
    return Interval(prefix_lo,prefix_hi+tail)


def theta_source_kernel_real(data:dict,x,y,comparison=13):
    """K_theta(x,y)=1/2[B(x+y)+B(x-y)] for REAL x,y.

    This is a theta-source Gram kernel, NOT the signed Weil kernel.
    """
    x,y=exact(x),exact(y)
    comparison=exact(comparison)
    if abs(x+y)>=comparison or abs(x-y)>=comparison:
        raise JetError('source kernel outside analytic comparison circle')
    return Q(1,2)*(B_real_interval(data,x+y,comparison)
                   +B_real_interval(data,x-y,comparison))


def positive_shadow_countermodel():
    """Two different genuine POSITIVE atomic measures matching m0 and m1.

    Neither measure is the authentic theta source; this tests the local-data
    ambiguity even after requiring positive moment/Hankel structure.
    """
    left={1:Q(1,2),3:Q(1,2)}
    right={2:Q(4,5),3:Q(1,5)}
    moments=lambda law:[sum((w*u**(2*j) for u,w in law.items()),Q()) for j in range(3)]
    ml,mr=moments(left),moments(right)
    if not ml[:2]==mr[:2] or ml[2]==mr[2]:
        raise ArithmeticError('positive shadow alias control invalid')
    return {'left_mass':left,'right_mass':right,
            'shared_m0_m1':ml[:2],
            'distinct_m2':[ml[2],mr[2]],
            'first_different_B_coefficient':Q(ml[2]-mr[2],4**2*factorial(4)),
            'both_sources_positive':True,
            'neither_is_authentic_integer_theta':True,
            'finite_moments_prove_unique_source':False,'RH_proved':False}



def fake_offline_zero_with_same_early_jets(data:dict,m:int=20):
    """Explicit Fock-budget impostor with a prescribed off-line zero.

    Let w=m*(1+i). Its fourth power equals -4*m^4. For ANY real true
    a0,a1 in the two certified source intervals, the even polynomial
      G(z)=(a0+a1*z^2)*(1+z^4/(4*m^4))
    agrees with the authentic first two even jets but vanishes at w,
    -w and their complex conjugates. It does NOT preserve full Euler germ.
    """
    _authenticated(data)
    if type(m)!=int or not 2<=m<=1000:
        raise JetError('invalid finite impostor location')
    a0,a1=data['a'][:2]
    hi0=max(abs(a0.lo),abs(a0.hi))
    hi1=max(abs(a1.lo),abs(a1.hi))
    k=4*m**4
    squared=hi0**2+2*hi1**2+factorial(4)*(hi0/Q(k))**2+factorial(6)*(hi1/Q(k))**2
    return {'chosen_off_critical_location':(m,m),
            'polynomial':'(a0+a1*z^2)*(1+z^4/(4*m^4))',
            'first_two_even_jets_match_exactly':True,
            'source_uniform_Fock_norm2_upper':squared,
            'inside_prior_Fock_budget':squared<Q(260,27),
            'this_is_not_original_xi':True,
            'full_original_Euler_germ_preserved':False,
            'RH_proved':False}


def one_point_shadow_blindspot(data:dict,d:int,seed=Q(1,1000)):
    """Source-observer ambiguity: f and f+eps*z^(2d+2) match low jets.

    This perturbation does NOT satisfy the complete original Euler/theta germ;
    'possible curve' here is relative to a finite observation menu only.
    """
    _authenticated(data)
    if type(d)!=int or not 0<=d<=data['degree']:
        raise JetError('invalid observer horizon')
    eps=exact(seed)
    if not eps:raise JetError('nonzero shadow required')
    return {'invisible_through_even_jet':d,'perturbation_power':2*d+2,
            'nonzero_perturbation':eps,'all_past_jets_preserved':True,
            'same_original_Euler_germ':False,'RH_proved':False}


def display_interval(x):
    return [str(x.lo),str(x.hi)]


def receipt():
    data=jets(degree=20,modes=3,T=8,cells=1536)
    radius=Q(11,2)
    cert=rouche_center_certificate(data,radius,13)
    hankel=source_hankel_two_by_two(data)
    obs=certified_midpoint_polynomial(data,radius,13)
    return {
        'source':data['source'],
        'parameters':{k:data[k] for k in ('degree','modes','T','cells')},
        'even_xi_coefficients':[display_interval(x) for x in data['a']],
        'positive_B_moments':[display_interval(x) for x in data['b']],
        'rouche_radius_11_over_2':{k:str(v) if isinstance(v,Q) else v for k,v in cert.items()},
        'rational_midpoint':{
             'coefficient_error':str(obs['finite_observer_error']),
             'analytic_tail':str(obs['analytic_tail']),
             'combined_uniform_disk_error':str(obs['uniform_complex_error'])},
        'unobserved_moment_2_lower_from_0_1':str(unseen_moment_lower(data,0)['certified_lower']),
        'theta_stieltjes_Hankel':{
            'moments':[display_interval(x) for x in hankel['moment_intervals']],
            'Hankel_det':display_interval(hankel['hankel_det']),
            'shifted_det':display_interval(hankel['shifted_hankel_det']),
            'both_strictly_positive_certified':hankel['both_strictly_positive_certified'],
            'completed_Weil_PSD_proved':False},
        'off_critical_finite_shadow_impostor':{
            k:str(v) if isinstance(v,Q) else v
            for k,v in fake_offline_zero_with_same_early_jets(data).items()},
        'positive_shadow_alias':{
            'shared_m0_m1':[str(x) for x in positive_shadow_countermodel()['shared_m0_m1']],
            'different_m2':[str(x) for x in positive_shadow_countermodel()['distinct_m2']]},
        'RH_proved':False,'zero_coordinates_used':False,
        'fully_evaluated_weil_form':False,
        'analytic_source_germ_requires_all_place_compatibility':True,
    }
