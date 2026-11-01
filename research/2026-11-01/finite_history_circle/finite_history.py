"""Finite-history/source-rigidity and constant-curvature BBP circle bridge.

Only exact rational/std-library algorithms. This is research, not a normality proof.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt
from typing import Sequence

B = 16
_A = (16, -89, 120)
_D = (21, -206, 712, -1024, 512)
_P6 = (-10222908432, 27261099545, 2560)
_Q6 = tuple(9*z for z in (-1497394413, 10286815366, -21109033272, 12923803584))
_EPS = F(1, 10**8)


def poly_eval(coeffs: Sequence[int | F], x: int | F) -> F:
    z = F(0)
    for v in reversed(coeffs):
        z = z * x + v
    return z


def source(n: int | F) -> F:
    x=F(n)
    if x < 1:
        raise ValueError("original source only on x>=1")
    return F(poly_eval(_A,x), poly_eval(_D,x))


def source_four_poles(n: int | F) -> F:
    x=F(n)
    return F(4,8*x-7)-F(2,8*x-4)-F(1,8*x-3)-F(1,8*x-2)


def spoof_six(n: int | F) -> F:
    x=F(n)
    if x < 1:
        raise ValueError("positive source control only x>=1")
    numerator=poly_eval(_A,x)+_EPS*poly_eval(_P6,x)/1310720
    denominator=poly_eval(_D,x)+_EPS*poly_eval(_Q6,x)/1310720
    return numerator/denominator


def polynomial_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            out[i+j]+=ai*bj
    return tuple(out)


def polynomial_add(a,b,coef=1):
    return tuple((a[i] if i<len(a) else 0) + coef*(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b))))


def spoof_polynomial_certificate():
    """P6*D - A*Q6 = 1310720*prod_{j=1}^6(x-j), integer identity."""
    lhs=polynomial_add(polynomial_mul(_P6,_D),polynomial_mul(_A,_Q6),-1)
    rhs=(1,)
    for j in range(1,7):
        rhs=polynomial_mul(rhs,(-j,1))
    return lhs, tuple(1310720*z for z in rhs)


def _solve_fraction(matrix:list[list[F]], rhs:list[F])->tuple[F,...]:
    n=len(rhs)
    if len(matrix)!=n or any(len(row)!=n for row in matrix):
        raise ValueError("square linear system required")
    a=[[F(v) for v in row]+[F(rhs[i])] for i,row in enumerate(matrix)]
    for col in range(n):
        pivot=next((i for i in range(col,n) if a[i][col]),None)
        if pivot is None:
            raise ValueError("sampling geometry does not uniquely identify source")
        a[col],a[pivot]=a[pivot],a[col]
        t=a[col][col]
        for j in range(col,n+1):
            a[col][j]/=t
        for i in range(n):
            if i==col:
                continue
            t=a[i][col]
            if t:
                for j in range(col,n+1):
                    a[i][j]-=t*a[col][j]
    return tuple(a[i][n] for i in range(n))


def fit_type_24(observations:Sequence[tuple[int,F]])->tuple[tuple[F,...],tuple[F,...]]:
    """Recover numerator degrees 0..2 and monic denominator degrees 0..4.

    Exactly 7 DISTINCT non-pole exact observations are required.  A singular
    rational interpolation system fails closed; do not infer a source family.
    """
    if len(observations)!=7 or len({int(x) for x,y in observations})!=7:
        raise ValueError("seven distinct time observations required")
    rows=[];rhs=[]
    for ix,y in observations:
        if not isinstance(ix,int) or ix<1:
            raise ValueError("positive integer source clock required")
        y=F(y); x=F(ix)
        rows.append([F(1),x,x*x,-y,-y*x,-y*x*x,-y*x*x*x])
        rhs.append(y*x**4)
    ans=_solve_fraction(rows,rhs)
    # The monic denominator is D(x)=x^4+b3*x^3+...+b0.
    return ans[:3],ans[3:]+(F(1),)


def rational_eval(model:tuple[tuple[F,...],tuple[F,...]],x:int|F)->F:
    num,den=model
    d=poly_eval(den,F(x))
    if d==0:
        raise ZeroDivisionError("reconstructed source pole")
    return poly_eval(num,F(x))/d


def original_seven_model():
    return fit_type_24(tuple((i,source(i)) for i in range(1,8)))


def frac_mod_one(x:F)->F:
    x=F(x)
    return x-(x.numerator//x.denominator)


def source_orbit(n:int,seed:F=F(0),source_fn=source)->tuple[F,...]:
    if n<0 or n>10000:
        raise ValueError("finite nonnegative horizon required")
    out=[F(seed)]
    for j in range(1,n+1):
        out.append(16*out[-1]+source_fn(j))
    return tuple(out)


def circle_phase_history(n:int,seed:F=F(0),source_fn=source)->tuple[F,...]:
    return tuple(frac_mod_one(u) for u in source_orbit(n,seed,source_fn))


def source_from_eight_circle_phases(phases:Sequence[F]):
    """Eight exact circle observations z_1..z_8, encoded as Q/Z rational.

    Each n>=2 cocycle recovers source r(n) mod 1, uniquely unwrapped by
    0<r(n)<1. Model prior: rational type (2,4) with no poles at 2..8.
    DOES NOT identify the time-0 preimage seed.
    """
    if len(phases)!=8:
        raise ValueError("eight consecutive phase observations 1..8 required")
    ph=tuple(frac_mod_one(F(z)) for z in phases)
    observations=[]
    for n in range(2,9):
        y=frac_mod_one(ph[n-1]-16*ph[n-2])
        if not 0<y<1:
            raise ValueError("source unwrapping interval or nonzero hypothesis violated")
        observations.append((n,y))
    return fit_type_24(observations)


def inverse_branches(next_phase:F,source_value:F)->tuple[F,...]:
    """16 exact distinct preimages in the circle of x -> 16*x + r mod1."""
    return tuple(frac_mod_one((F(next_phase)-F(source_value)+j)/16)
                 for j in range(16))


def normalized_bbpfuture(n:int,J:int)->F:
    """Source-tail T_(n,J) of the known four-pole source, rational finite."""
    if n<0 or J<1:
        raise ValueError("n>=0 and J>=1 required")
    return sum((source(n+j)/16**j for j in range(1,J+1)),F(0))


def future_tail_lower_upper(n:int,J:int)->tuple[F,F]:
    """T_n in (T_(n,J), T_(n,J)+16^-J/[64(n+J)^2])."""
    partial=normalized_bbpfuture(n,J)
    return partial,partial+F(1,16**J*64*(n+J)**2)


def refinement_plan(N:int,power:int=2)->tuple[int,int,int]:
    """Circle depth k=2N+L, source tail J; certified 4^L,16^J>=N^power."""
    if type(N)!=int or N<1 or type(power)!=int or power<1:
        raise ValueError("positive integers N,power required")
    target=N**power
    L=0
    while 4**L < target:
        L+=1
    J=1
    while 16**J < target:
        J+=1
    return 2*N+L,L,J


def absolute_weyl_transport_bound(N:int,h:int,power:int=2)->F:
    """Rigorous unnormalized Weyl error, using 2*pi<44/7 and circle bound."""
    if type(h)!=int or h==0:
        raise ValueError("nonzero integer Fourier character required")
    k,L,J=refinement_plan(N,power)
    # Shape term geom_delta * sum_{n=1}^N 16^(n-1); tail source sum
    shape=F(8,3*4**k)*F(16**N-1,15)
    tail=F(1,64*16**J*J)
    return F(44,7)*abs(h)*(shape+tail)


def universal_power_bound(N:int,h:int,power:int=2)->F:
    """Simple O_h(N^-power) upper for the full UNNORMALIZED N-term error."""
    if type(h)!=int or h==0 or N<1 or power<1:
        raise ValueError("invalid quantifiers")
    return F(44,7)*abs(h)*(F(8,45)+F(1,64))/N**power


def sqrt_dyadic_bounds(q:F,bits:int=256)->tuple[F,F]:
    if q<0 or bits<8:
        raise ValueError("nonnegative radicand and >=8 bits required")
    Q=1<<bits
    floor_squared=(q.numerator*Q*Q)//q.denominator
    a=isqrt(floor_squared)
    l=F(a,Q)
    return l,l if l*l==q else F(a+1,Q)


def circle_polygon_interval(k:int,bits:int=256)->tuple[F,F]:
    """Exact outward rational bounds for length quotient Π_k=2^k*c_k."""
    if type(k)!=int or k<0 or k>256:
        raise ValueError("finite circle refinement needed")
    lo=hi=F(4)
    for _ in range(k):
        root_lo,root_hi=sqrt_dyadic_bounds(1-lo/4,bits)
        lower=lo/(2*(1+root_hi))
        root_lo_hi,root_hi_hi=sqrt_dyadic_bounds(1-hi/4,bits)
        upper=hi/(2*(1+root_lo_hi))
        lo,hi=lower,upper
    l,_=sqrt_dyadic_bounds(lo,bits)
    _,u=sqrt_dyadic_bounds(hi,bits)
    return 2**k*l,2**k*u


def wilson_curvature(n:int,source_fn=source)->F:
    if n<1:
        raise ValueError("successor index n>=1 required")
    return 15*(source_fn(n)-source_fn(n+1))


def finite_wilson_future(n:int,J:int,source_fn=source)->F:
    """Source future from strictly ordered curvature plus required boundary residue.

    Equals sum_{j=1}^J 16^-j r(n+j), not the infinite tail.
    """
    if n<0 or J<1:
        raise ValueError("n>=0,J>=1")
    result=sum(((1-F(1,16**k))*wilson_curvature(n+k,source_fn)
                for k in range(1,J+1)),F(0))/225
    result+=(1-F(1,16**J))*source_fn(n+J+1)/15
    return result


def geometric_predictor_interval(n:int,N:int,power:int=2,bits:int=512):
    """Finite geometry - finite curvature, interval with rational endpoints.

    No real π is supplied. Identifies the ZERO-SEEDED source orbit only.
    """
    if not (1<=n<=N):
        raise ValueError("predicting only original realized prefix")
    k,L,J=refinement_plan(N,power)
    pi_lo,pi_hi=circle_polygon_interval(k,bits)
    tail=finite_wilson_future(n,J)
    return 16**(n-1)*pi_lo-tail,16**(n-1)*pi_hi-tail


def controlled_echo_operator_bound(N:int,h:int,power:int=2)->F:
    """Maximum of N scalar loop differences, hence diagonal unitary norm."""
    if type(h)!=int or h==0:
        raise ValueError("nonzero harmonic")
    _,L,J=refinement_plan(N,power)
    return F(44,7)*abs(h)*(F(1,6*4**L)+F(1,64*J**2*16**J))


def universal_controlled_echo_bound(N:int,h:int,power:int=2)->F:
    return F(44,7)*abs(h)*(F(1,6)+F(1,64))/N**power


def n_step_preimage_formula(n:int,end_phase:F,j:int,source_fn=source)->F:
    """Full n-step circle inverse branch of the actual zero-seeded forcing.

    Does NOT claim the true initial seed can be inferred from the endpoint.
    """
    if n<1 or not 0<=j<16**n:
        raise ValueError("proper finite inverse branch index")
    original_end=source_orbit(n,F(0),source_fn)[-1]
    return frac_mod_one((F(end_phase)-original_end+j)/16**n)


def source_from_seven_zero_seed_phases(phases:Sequence[F],first_step_integer_part:int=3):
    """Seven circle observations at n=1..7, with AUTHENTICATED z0=1 and
    r1 in (first_step_integer_part, first_step_integer_part+1).

    Without the first-step lift this is not a phase-source identification.
    """
    if len(phases)!=7 or type(first_step_integer_part)!=int:
        raise ValueError("seven phases and declared first-step lift required")
    ph=tuple(frac_mod_one(F(z)) for z in phases)
    r1=ph[0]+first_step_integer_part
    if not F(first_step_integer_part)<r1<F(first_step_integer_part+1):
        raise ValueError("first-step integer branch or zero-seed mismatch")
    obs=[(1,r1)]
    for n in range(2,8):
        value=frac_mod_one(ph[n-1]-16*ph[n-2])
        if not 0<value<1:
            raise ValueError("unsupported source increment range")
        obs.append((n,value))
    return fit_type_24(obs)
