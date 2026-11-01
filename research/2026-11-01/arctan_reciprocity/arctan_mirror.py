"""Source-faithful arctan-reciprocity mirror gate for original four-pole BBP.

Exact Fraction arithmetic for source, orbit, arithmetic error budgets and
Machin/Taylor interval certificates. Complex finite observables are diagnostics.
No numerical statement of an all-horizon signed Weyl saving is made.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial


class ReciprocityError(ValueError):
    pass


def require_int(x: int, lo: int = 0) -> int:
    if type(x) is not int or x < lo:
        raise ReciprocityError(f"integer >= {lo} required")
    return x


def forcing(n: int) -> F:
    require_int(n, 1)
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def forcing_combined(n: int) -> F:
    require_int(n, 1)
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def rational_orbit(n: int, seed: F = F(0)) -> tuple[F, ...]:
    """Exact original real-circle states U1..Un; input seed rational only."""
    require_int(n)
    if type(seed) not in (int, F):
        raise ReciprocityError("rational seed required for finite register")
    x=F(seed) % 1
    result=[]
    for j in range(1,n+1):
        x=(16*x+forcing(j))%1
        result.append(x)
    return tuple(result)


def source_axis_bracket(m: int) -> tuple[F,F]:
    """Exact ORIGINAL source bound alpha=pi/16, using r(j)>r(j+1)>0.

    alpha=sum_{j>=1}16^-j r(j). The known BBP identity alpha=pi/16
    is an input, NOT rederived by this bracket.
    """
    require_int(m,1)
    lower=sum((forcing(j)*F(1,16**j) for j in range(1,m+1)),F(0))
    upper=lower+forcing(m+1)*F(1,15*16**m)
    return lower,upper


def rotated_axis_bracket(m: int) -> tuple[F,F]:
    """Selected reciprocal axis beta=1/2+alpha, alpha=pi/16."""
    lo,hi=source_axis_bracket(m)
    return lo+F(1,2),hi+F(1,2)


def axis_midpoint_error(m:int) -> F:
    lo,hi=rotated_axis_bracket(m)
    return (hi-lo)/2


def arctan_bracket(q:int,terms:int=22)->tuple[F,F]:
    """Alternating rational bounds for arctan(1/q), q>=2."""
    require_int(q,2);require_int(terms,1)
    partial=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(terms)),F(0))
    nextterm=F((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return min(partial,partial+nextterm),max(partial,partial+nextterm)


def pi_bracket(terms:int=22)->tuple[F,F]:
    """Machin pi=16atan(1/5)-4atan(1/239), outward exact fractions."""
    a,b=arctan_bracket(5,terms)
    c,d=arctan_bracket(239,terms)
    return 16*a-4*d,16*b-4*c


def source_step_sum(n:int)->F:
    require_int(n,1)
    return sum((forcing(j+1) for j in range(1,n+1)),F(0))


def radix_discrepancy_bound(n:int,h:int, *, sharp:bool=True)->F:
    """Safe rational upper bound for |A_N(16h)-A_N(h)|.

    Exact source: 16 U_j=U_{j+1}-r(j+1), so
    |E| <= [2+2*pi*|h| sum_{j<=N}r(j+1)]/N.
    Use pi<22/7. For sharp=False, use sum r(j+1)<15/32.
    """
    require_int(n,1)
    if type(h) is not int or h==0:raise ReciprocityError("nonzero integer Fourier harmonic")
    s=source_step_sum(n) if sharp else F(15,32)
    return (F(2)+F(44,7)*abs(h)*s)/n


def uniform_radix_bound(n:int,h:int)->F:
    """Universal exact rational: (2+165|h|/56)/N."""
    require_int(n,1)
    if type(h) is not int or h==0:raise ReciprocityError("nonzero integer Fourier harmonic")
    return (F(2)+F(165*abs(h),56))/n


def mirror_axis_discrepancy_bound(m:int,h:int)->F:
    """For beta_m midpoint of source bracket, |M(h;beta)-M(h;beta_m)|.

    derivative wrt beta bounded pi*abs(h), and pi<22/7.
    """
    if type(h) is not int or h==0:raise ReciprocityError("nonzero integer Fourier harmonic")
    return F(22*abs(h),7)*axis_midpoint_error(m)


def geometric_axis_discrepancy_bound(m:int,h:int)->F:
    """For beta_geom=1/2+Pi_{4m}/16, imported PR #447 geometry.

    0<pi-Pi_{4m}<8/(3*256^m), hence axis error <1/(6*256^m).
    """
    require_int(m,1)
    if type(h) is not int or h==0:raise ReciprocityError("nonzero integer Fourier harmonic")
    return F(11*abs(h),21*256**m)


def _rational_taylor_sin(x:F,terms:int=19)->tuple[F,F]:
    """Taylor polynomial and exact Lagrange error |x|^(2m+1)/(2m+1)!."""
    require_int(terms,1)
    s=sum((F((-1)**k)*x**(2*k+1)/factorial(2*k+1)
           for k in range(terms)),F(0))
    return s,abs(x)**(2*terms+1)/factorial(2*terms+1)


def certified_mirror_denominator(h:int, *,terms:int=25, taylor_terms:int=22,
                                  axis:str="rotated")->dict:
    """EXACT rational lower bound for |sin(15*pi*h*beta)|.

    beta=1/2+pi/16 ('rotated') or pi/16 ('direct'). The Machin
    rational interval encloses pi; evaluate sin by Taylor/Lipschitz.
    A positive returned lower certifies no denominator singularity.
    """
    if type(h) is not int or h==0:raise ReciprocityError("nonzero integer Fourier harmonic")
    if axis not in ("rotated","direct"):raise ReciprocityError("unknown axis")
    require_int(terms,1); require_int(taylor_terms,1)
    pl,pu=pi_bracket(terms)
    if not F(3)<pl<pu<F(22,7):raise ArithmeticError("pi interval invalid")
    hh=abs(h)
    c=F(1,2) if axis=="rotated" else F(0)
    # Phi=15*pi*h*(c+pi/16); pi>0, h>0 after evenness.
    phil=15*hh*(c*pl+pl*pl/16)
    phiu=15*hh*(c*pu+pu*pu/16)
    # k nearest integer to Phi/(2pi); beta/2 = c/2+pi/32.
    kcenter=15*hh*(c/F(2)+ (pl+pu)/F(64))
    k=(kcenter.numerator*2//kcenter.denominator+1)//2
    dl=phil-2*k*pu
    du=phiu-2*k*pl
    if not -F(22,7)<dl<=du<F(22,7):
        raise ArithmeticError("phase reduction was not certified; refine Machin")
    midpoint=(dl+du)/2
    radius=(du-dl)/2
    poly,err=_rational_taylor_sin(midpoint,taylor_terms)
    total=err+radius
    lower=max(F(0),abs(poly)-total)
    upper=min(F(1),abs(poly)+total)
    return {"lower":lower,"upper":upper,"k":k,"phase_interval":(dl,du),
            "pi_interval":(pl,pu),"polynomial":poly,"error":total,
            "axis":axis,"harmonic":h}


def predicted_real_quadrature_bound(n:int,h:int,m:int,*,axis:str="rotated")->dict:
    """Exact rational coefficient for a conditional inequality:

    |A_N(h)| <= (|M_N(h;beta_m)|+|M_N(16h;beta_m)|
              + E_N(h)+error_h+error_16h)/denom_lower
    when beta_m is a source-certified rational midpoint. Positivity of
    denominator is independently certified by Machin/Taylor arithmetic.
    """
    require_int(n,1);require_int(m,1)
    if axis!="rotated":raise ReciprocityError("certified midpoint is source-rotated")
    den=certified_mirror_denominator(h,axis=axis)
    if not den["lower"]:raise ArithmeticError("denominator not resolved")
    err=radix_discrepancy_bound(n,h)+mirror_axis_discrepancy_bound(m,h)+mirror_axis_discrepancy_bound(m,16*h)
    return {"denominator_lower":den["lower"],"additive_error":err,
            "coefficient":1/den["lower"],"axis_midpoint":sum(rotated_axis_bracket(m),F(0))/2,
            "m":m,"n":n,"h":h}


def reciprocal_digit_action(d:int, *,first:bool)->int:
    """Digit maps for y=1/2-x modulo1, on nonterminating radix16 expansions.

    First digit: (7-d) mod16; later digits: 15-d. Every input digit valid.
    """
    require_int(d)
    if d>15:raise ReciprocityError("base16 digit outside range")
    return (7-d)%16 if first else 15-d


def conditional_green_bound(n:int,h:int)->F:
    """PR #445 inherited Green tail: sum_{j>=1} T_j <1/32.

    Normalized average of sin(h U_j-theta) and sin(h 16^j alpha-theta)
    differs by strictly less than pi|h|/(16 N); pi<22/7 yields this bound.
    """
    require_int(n,1)
    if type(h) is not int or h==0:raise ReciprocityError("nonzero integer Fourier harmonic")
    return F(11*abs(h),56*n)  # pi/16 < 22/(7*16)=11/56


# A SOURCE-NATIVE irrational angular mirror with rational projective coefficients:
# q=r(2)=106/819; gamma=exp(2*i*atan(q))=(819+106i)/(819-106i).
_MIRROR_A=819
_MIRROR_B=106
_MIRROR_D=_MIRROR_A*_MIRROR_A+_MIRROR_B*_MIRROR_B


def rational_mirror_label() -> dict:
    """Exact q and unit-circle factor gamma in Q(i); gamma has infinite order.

    Every root of unity in Q(i) is +/-1 or +/-i, whereas gamma has both
    nonzero real and imaginary rational parts. No pi approximation is needed.
    """
    q=forcing(2)
    if q != F(_MIRROR_B,_MIRROR_A):raise ArithmeticError("original source label mutated")
    gre=F(_MIRROR_A**2-_MIRROR_B**2,_MIRROR_D)
    gim=F(2*_MIRROR_A*_MIRROR_B,_MIRROR_D)
    if not gre or not gim or gre*gre+gim*gim!=1:
        raise ArithmeticError("invalid Gaussian rational infinite-order generator")
    return {"source_index":2,"q":q,"gamma_real":gre,"gamma_imag":gim,
            "norm":_MIRROR_D,"root_of_unity":False}


def projective_rational_mirror(a:int|F,b:int|F)->tuple[F,F]:
    """Homogeneous Möbius matrix for t=a/b, including infinity and t=0.

    J_q([a:b])=[-819a+106b:106a+819b]. Projective involution:
    J_q^2=D*identity, D=681997. Projective coordinates need not be reduced.
    """
    if type(a) not in (int,F) or type(b) not in (int,F) or (a==0 and b==0):
        raise ReciprocityError("nonzero exact rational homogeneous coordinate")
    return F(-_MIRROR_A*a+_MIRROR_B*b),F(_MIRROR_B*a+_MIRROR_A*b)


def gaussian_integer_power(a:int,b:int,n:int)->tuple[int,int]:
    """Exact (a+ib)^n by binary exponentiation, integer components."""
    require_int(n)
    if type(a) is not int or type(b) is not int:raise ReciprocityError("integer Gaussian coefficients")
    re,im=1,0
    while n:
        if n&1:re,im=re*a-im*b,re*b+im*a
        a,b=a*a-b*b,2*a*b
        n>>=1
    return re,im


def mirror_sine_squared(h:int)->F:
    """EXACT rational sin^2(15*h*arctan(106/819)), strictly positive h!=0.

    Im((819+106i)^(15|h|))^2 / 681997^(15|h|).
    The nonzero integer numerator is a certificate, since gamma is not a root
    of unity; this is an integer-arithmetic denominator for the mirror gate.
    """
    if type(h) is not int or h==0:raise ReciprocityError("nonzero harmonic")
    m=15*abs(h)
    _,imag=gaussian_integer_power(_MIRROR_A,_MIRROR_B,m)
    if not imag:raise ArithmeticError("irrational mirror denominator vanished")
    d=F(imag*imag,_MIRROR_D**m)
    if not 0<d<=1:raise ArithmeticError("invalid exact sine square")
    return d


def gaussian_commutator_distance_squared(h:int)->F:
    """Exact |gamma^(15h)-1|^2 = 4*sin^2(15h atan(q))."""
    return 4*mirror_sine_squared(h)


def signed_gaussian_quadrature_coefficients(h:int)->tuple[int,int]:
    """Exact coefficients (real, imag) of (819-106i)^h for h>=1.

    B_N(h)=Im((a+ib) A_N(h))=a Im A_N(h)+b Re A_N(h).
    Its vanishing is equivalent to the arctan-mirror sine quadrature M_N(h).
    """
    require_int(h,1)
    return gaussian_integer_power(_MIRROR_A,-_MIRROR_B,h)


def exact_mirror_gate_coefficient(h:int)->dict:
    """Exact RATIONAL squared reciprocal condition number of the source mirror.

    |A_h|^2 <= reciprocal_squared * (|D_h|+|D_16h|+2|E_h|)^2,
    D_h=A_h-gamma^h conjugate(A_h).
    """
    den=gaussian_commutator_distance_squared(h)
    return {"h":h,"q":F(_MIRROR_B,_MIRROR_A),"denominator_squared":den,
            "inverse_denominator_squared":1/den,"nonzero":den>0}


if __name__=="__main__":
    for h in (1,2,3,5,7,11):
        cert=certified_mirror_denominator(h)
        print(h, float(cert["lower"]),float(cert["upper"]))
