"""Source-authentic well-conditioned adaptive arctangent Fourier frame.

Proof of uniform |sin(phi_{16h}-phi_h)|>1/8 is in PROOFS.md.
All source coefficients and finite orbit values use exact rational arithmetic.
Theorem is an EQUIVALENT signed-cancellation criterion, not its proof.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt, factorial


class FrameError(ValueError):
    """Invalid arithmetic source/harmonic/probe domain."""


def positive_integer(value: int) -> int:
    if type(value) is not int or value < 1:
        raise FrameError('positive integer required (no bool)')
    return value


def source(n: int) -> F:
    positive_integer(n)
    return F(4, 8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def source_combined(n: int) -> F:
    positive_integer(n)
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def valuation16(h: int) -> int:
    positive_integer(h)
    v=0
    while h % 16 == 0:
        h//=16
        v+=1
    return v


def ceil_sqrt(n: int) -> int:
    positive_integer(n)
    k=isqrt(n)
    return k+(k*k != n)


def source_index(h: int) -> int:
    """A deterministic integer source index, alternating along each 16-ladder."""
    positive_integer(h)
    return ceil_sqrt(h if valuation16(h)%2==0 else 4*h)


def source_axis(h: int) -> F:
    return source(source_index(h))


def gaussian_power(a:int,b:int,n:int) -> tuple[int,int]:
    if type(a) is not int or type(b) is not int or type(n) is not int or n < 0:
        raise FrameError('Gaussian integer power needs exact integer inputs')
    x,y=1,0
    while n:
        if n&1:x,y=x*a-y*b,x*b+y*a
        a,b=a*a-b*b,2*a*b
        n>>=1
    return x,y


def signed_coefficients(h: int) -> dict:
    """B_N(h)=Im((a-ib)^h A_N(h))/d^(h/2): exact integer coefficients.

    This function certifies the algebraic projection, not the value of a
    transcendental phase-sum without additional interval arithmetic.
    """
    positive_integer(h)
    q=source_axis(h)
    a,b=q.denominator,q.numerator
    real,imag=gaussian_power(a,-b,h)
    return {'h':h,'source_index':source_index(h),'source_value':q,
            'real':real,'imag':imag,'norm_squared':a*a+b*b,
            'normalizer_power':h}


def frame_cross_integer(h:int) -> dict:
    """Exact Gaussian-integer determinant numerator for the two projections.

    δ = phi_16h - phi_h. Im((a_h-i b_h)^h *
      (a_16h+i b_16h)^(16h)) / sqrt(d_h^h*d_16h^(16h))
    equals sin(phi_16h-phi_h). We return the signed integer numerator and
    rational squared determinant, with a proof-based UNIFORM lower bound 1/8.
    """
    positive_integer(h)
    left=signed_coefficients(h)
    right=signed_coefficients(16*h)
    a,b=left['real'],left['imag']
    c,d=right['real'],-right['imag']
    numerator=a*d+b*c
    norm_left=left['norm_squared']**h
    norm_right=right['norm_squared']**(16*h)
    determinant_square=F(numerator*numerator,norm_left*norm_right)
    if not determinant_square>F(1,64):
        raise ArithmeticError('exact uniform frame theorem violated')
    return {'h':h,'numerator':numerator,
            'determinant_squared':determinant_square,
            'uniform_abs_lower':F(1,8),
            'h_source_index':left['source_index'],
            '16h_source_index':right['source_index']}


def original_phase_states(n: int, *,seed:int|F=F(0)) -> tuple[F,...]:
    positive_integer(n)
    if type(seed) not in (int,F):raise FrameError('rational seed for exact finite register')
    x=F(seed)%1
    out=[]
    for j in range(1,n+1):
        x=(16*x+source(j))%1
        out.append(x)
    return tuple(out)


def source_radix_error(n:int,h:int) -> F:
    """Inherited original-four-pole bound for |A_N(16h)-A_N(h)|."""
    positive_integer(n);positive_integer(h)
    return (F(2)+F(165*h,56))/n


def frame_paper_bound(n:int,h:int,absolute_projection_h:F,
                      absolute_projection_16h:F) -> F:
    """An exact rational upper bound on |A_N(h)| from certified projection bounds.

    The caller must certify the two nonnegative real signed-projection upper
    bounds separately. This function does not pretend to calculate them.
    """
    positive_integer(n);positive_integer(h)
    if any(type(x) not in (int,F) or x < 0 for x in
           (absolute_projection_h,absolute_projection_16h)):
        raise FrameError('nonnegative certified rational projection bounds needed')
    return F(8)*(F(absolute_projection_h)+F(absolute_projection_16h)
                 +source_radix_error(n,h))


def arithmetic_source_polynomial_certificates() -> dict:
    """Int coefficients in increasing powers of t for the PROOFS shifted polynomials.

    No floating test is used to establish their positivity on t>=0.
    The last special quadratic n>=3 is handled separately (all positive).
    """
    return {
        'source_lower_n_ge_2':(44553,80434,48328,9664),
        'source_upper_n_ge_2':(576,11364,19418,11511,2296),
        'source_upper_n_ge_8':(248013,442690,147976,18208,768),
        'weighted_lower_n_ge_3':(1090,641,621,435,88),
        'weighted_lower_n_eq_2':723,
    }


def _atan_positive_interval(x:F,terms:int=22) -> tuple[F,F]:
    """Exact alternating interval for 0<=x<=1 (strict for x>0)."""
    if type(x) not in (int,F) or not 0<=x<=1:raise FrameError('arctan input in [0,1]')
    positive_integer(terms)
    t=F(x)
    val=sum(((-1)**j)*t**(2*j+1)/F(2*j+1) for j in range(terms))
    nxt=(-1)**terms*t**(2*terms+1)/F(2*terms+1)
    return min(val,val+nxt), max(val,val+nxt)


def pi_interval(terms:int=22) -> tuple[F,F]:
    """Machin 16 atan(1/5)-4 atan(1/239), exact rational interval."""
    x0,x1=_atan_positive_interval(F(1,5),terms)
    y0,y1=_atan_positive_interval(F(1,239),terms)
    return 16*x0-4*y1,16*x1-4*y0


def axis_angle_interval(h:int,terms:int=22)->tuple[F,F]:
    """theta_h=atan r(source_index(h)), exact rational lower and upper."""
    q=source_axis(h)
    if q<=1:return _atan_positive_interval(q,terms)
    assert source_index(h)==1
    pl,pu=pi_interval(terms)
    a,b=_atan_positive_interval(1/q,terms)
    return pl/2-b,pu/2-a


def _nearest_integer(x:F)->int:
    return (x+F(1,2)).numerator//(x+F(1,2)).denominator


def sin_interval(lo:F,hi:F,terms:int=24)->tuple[F,F]:
    """Rational Taylor enclosure using |sin'|<=1 and the Taylor remainder."""
    positive_integer(terms)
    if lo>hi:raise FrameError('invalid interval')
    mid=(lo+hi)/2
    rad=(hi-lo)/2
    poly=sum(((-1)**j)*mid**(2*j+1)/F(factorial(2*j+1))
             for j in range(terms))
    error=abs(mid)**(2*terms+1)/F(factorial(2*terms+1))+rad
    return max(F(-1),poly-error), min(F(1),poly+error)


def cos_interval(lo:F,hi:F,terms:int=24)->tuple[F,F]:
    positive_integer(terms)
    if lo>hi:raise FrameError('invalid interval')
    mid=(lo+hi)/2
    rad=(hi-lo)/2
    poly=sum(((-1)**j)*mid**(2*j)/F(factorial(2*j))
             for j in range(terms))
    error=abs(mid)**(2*terms)/F(factorial(2*terms))+rad
    return max(F(-1),poly-error),min(F(1),poly+error)


def phase_angle_interval(state:F,h:int,*,theta_harmonic:int|None=None,
                         atan_terms:int=24)->tuple[F,F]:
    """Enclose 2*pi*h*state - h*theta_axis with exact rational phase reduction.

    theta_harmonic is h for the default adaptive frame; pass None to
    calculate the usual e(h*state) phase with NO mirror rotation.
    """
    positive_integer(h)
    if type(state) not in (int,F):raise FrameError('exact rational phase state required')
    pl,pu=pi_interval(atan_terms)
    if not F(3)<pl<pu<F(22,7):raise ArithmeticError('invalid pi interval')
    tl,tu=(F(0),F(0)) if theta_harmonic is None else axis_angle_interval(theta_harmonic,atan_terms)
    if theta_harmonic is not None and theta_harmonic!=h:
        raise FrameError('mirror must match the harmonic under test')
    residue=F(h)*F(state)
    offset=h*((tl+tu)/2)/((pl+pu))
    k=_nearest_integer(residue-offset)
    x=residue-k
    lo=(2*pl*x if x>=0 else 2*pu*x)-h*tu
    hi=(2*pu*x if x>=0 else 2*pl*x)-h*tl
    if not lo<=hi or not -F(4)<lo<=hi<F(4):
        raise ArithmeticError('uncertified periodic angle reduction')
    return lo,hi


def projection_interval(states:tuple[F,...],h:int,*,atan_terms:int=24,
                        taylor_terms:int=24,mirror:bool=True)->tuple[F,F]:
    """Exact rational enclosure of signed mean, no floating cos/sin computation."""
    positive_integer(h)
    if not states:raise FrameError('nonempty source history required')
    lo=hi=F(0)
    for x in states:
        a,b=phase_angle_interval(x,h,theta_harmonic=h if mirror else None,atan_terms=atan_terms)
        l,u=sin_interval(a,b,taylor_terms)
        lo+=l;hi+=u
    return lo/len(states),hi/len(states)


def real_character_interval(states:tuple[F,...],h:int,*,atan_terms:int=24,
                            taylor_terms:int=24)->tuple[F,F]:
    positive_integer(h)
    if not states:raise FrameError('nonempty source history required')
    lo=hi=F(0)
    for x in states:
        a,b=phase_angle_interval(x,h,theta_harmonic=None,atan_terms=atan_terms)
        l,u=cos_interval(a,b,taylor_terms)
        lo+=l;hi+=u
    return lo/len(states),hi/len(states)


def certified_original_frame_probe(n:int,h:int,*,terms:int=24)->dict:
    """Compute exact rational enclosures and a nontrivial consistency check.

    Input is regenerated internally from the AUTHENTIC four-pole zero-seed
    trajectory; mutation of the arithmetic source is not silently permitted.
    """
    positive_integer(n);positive_integer(h)
    states=original_phase_states(n)
    bh=projection_interval(states,h,atan_terms=terms,taylor_terms=terms)
    b16=projection_interval(states,16*h,atan_terms=terms,taylor_terms=terms)
    re=real_character_interval(states,h,atan_terms=terms,taylor_terms=terms)
    im=projection_interval(states,h,atan_terms=terms,taylor_terms=terms,mirror=False)
    upper_b=lambda b:max(abs(b[0]),abs(b[1]))
    bound=frame_paper_bound(n,h,upper_b(bh),upper_b(b16))
    # A true upper bound on |A|^2 from the independent real and imaginary enclosures.
    magnitude_squared_upper=upper_b(re)**2+upper_b(im)**2
    if magnitude_squared_upper>bound*bound:
        raise ArithmeticError('independent interval oracle contradicts frame inequality')
    return {'n':n,'h':h,'mirror_h':bh,'mirror_16h':b16,
            'original_real':re,'original_imag':im,'upper_A_squared':magnitude_squared_upper,
            'frame_bound':bound,'frame_lower_det':F(1,8)}


def finite_positive_counterfeit_source(n:int, matching_depth:int)->F:
    """Hostile positive strictly decreasing source; NOT the four-pole source after L.

    Matches original r(1)..r(L), then takes rational geometric tail
    r(L)*2^-(n-L). The completed BBP-type sum is exactly RATIONAL.
    """
    positive_integer(n);positive_integer(matching_depth)
    if n<=matching_depth:return source(n)
    return source(matching_depth)*F(1,2**(n-matching_depth))


def finite_positive_counterfeit_completed(matching_depth:int)->F:
    """Exact rational completed point of positive monotone finite mimic."""
    positive_integer(matching_depth)
    return sum((source(j)*F(1,16**j) for j in range(1,matching_depth+1)),F(0)) \
        + source(matching_depth)*F(1,31*16**matching_depth)


def finite_positive_counterfeit_states(n:int,matching_depth:int)->tuple[F,...]:
    positive_integer(n);positive_integer(matching_depth)
    x=F(0);out=[]
    for j in range(1,n+1):
        x=(16*x+finite_positive_counterfeit_source(j,matching_depth))%1
        out.append(x)
    return tuple(out)
