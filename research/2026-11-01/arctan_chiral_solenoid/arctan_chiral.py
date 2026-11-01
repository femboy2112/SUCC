"""Research-only exact classical carrier for SUCC's four-pole BBP source.

Original source r(n), literal U0=0. No Fourier cancellation, normality,
quantum tunneling, or analytic proof is presumed. All rational computation is
exact. Odd-torsion solenoid lifts are source-labeled; arctan inversion is a
Möbius involution, not an independent Fourier measurement.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, gcd, lcm


def source(n: int | Fraction) -> Fraction:
    x = Fraction(n)
    if any(f == 0 for f in (2*x-1, 4*x-1, 8*x-7, 8*x-3)):
        raise ValueError("Source pole")
    return (4/(8*x-7) - 2/(8*x-4) - 1/(8*x-3) - 1/(8*x-2))


def source_combined(n: int | Fraction) -> Fraction:
    x = Fraction(n)
    a = 120*x*x-89*x+16
    d = (2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
    if not d:
        raise ValueError("Source pole")
    return a/d


def source_derivative(n: int | Fraction) -> Fraction:
    x = Fraction(n)
    a = 120*x*x-89*x+16
    ap = 240*x-89
    factors = (2*x-1, 4*x-1, 8*x-7, 8*x-3)
    if 0 in factors:
        raise ValueError("Source pole")
    d = factors[0]*factors[1]*factors[2]*factors[3]
    dp = sum(v*__prod(factors[:i]+factors[i+1:]) for i,v in enumerate((2,4,8,8)))
    return (ap*d-a*dp)/(d*d)


def __prod(parts):
    p=1
    for x in parts: p*=x
    return p


def odd_denominator_mod(z: Fraction, modulus: int) -> int:
    z=Fraction(z)
    if modulus<2 or gcd(z.denominator,modulus)!=1:
        raise ValueError("Fraction not invertible at this clock")
    return (z.numerator*pow(z.denominator,-1,modulus)) % modulus


def source_residue(n:int,level:int)->int:
    if not (isinstance(n,int) and isinstance(level,int) and level>=1):
        raise ValueError("integer arguments and positive level required")
    q=16**level
    a=120*n*n-89*n+16
    d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return (a*pow(d,-1,q))%q


def source_base16_closed(n:int)->int:
    return (-n+2*(n%2))%16


def derivative_base16_closed(n:int)->int:
    return (11+4*n*(n-1))%16


def lifted_derivative(n:int)->int:
    return odd_denominator_mod(source_derivative(n),16)


def source_slope_congruence(n:int,level:int,t:int)->bool:
    if level<2: raise ValueError("At least two 16-adic levels")
    L=16**(level-1)
    q=16**level
    return (source_residue(n+L*t,level)-source_residue(n,level)-L*t*lifted_derivative(n))%q==0


def root_vector_16(exponent:int)->tuple[int,...]:
    """Coefficient vector of zeta_16^exponent in Z[X]/(X^8+1)."""
    m=exponent%16
    return tuple(((-1)**(m//8) if i==m%8 else 0) for i in range(8))


def add_vec(a,b):return tuple(x+y for x,y in zip(a,b))


def scale_vec(a,s):return tuple(x*s for x in a)


def source_fourier16_numerator(k:int,ell:int)->tuple[int,...]:
    """16*K(k,ell), enumerated in the exact cyclotomic ring Z[zeta16]."""
    out=(0,)*8
    for n in range(16):
        out=add_vec(out,root_vector_16(ell*n-k*source_residue(n,1)))
    return out


def source_fourier16_closed_numerator(k:int,ell:int)->tuple[int,...]:
    """Closed source-specific two-channel kernel, scaled by 16."""
    diff=(ell+k)%16
    v=scale_vec(root_vector_16(0),8)
    w=scale_vec(root_vector_16(-2*k),8)
    if diff==0: return add_vec(v,w)
    if diff==8: return add_vec(v,scale_vec(w,-1))
    return (0,)*8


def higher_fourier_support(k:int,ell:int)->bool:
    return ((ell-3*k)%16==0 or (ell-11*k)%16==0)


def finite_orbit(nmax:int,seed:Fraction=Fraction(0)) -> tuple[Fraction,...]:
    if nmax<0 or nmax>200:raise ValueError("bounded finite orbit")
    state=Fraction(seed)
    states=[state]
    for n in range(1,nmax+1):
        state=16*state+source(n)
        states.append(state)
    return tuple(states)


def mod_one(x:Fraction)->Fraction:
    x=Fraction(x)
    return x-(x.numerator//x.denominator)


def inverted_circle_phase(x:Fraction)->Fraction:
    """On circle x=theta/2pi, arctan tangent inversion is x->1/2-x."""
    return mod_one(Fraction(1,2)-Fraction(x))


def chiral_forcing(n:int)->Fraction:
    return Fraction(1,2)-source(n)


def chiral_orbit(nmax:int)->tuple[Fraction,...]:
    state=Fraction(1,2)
    out=[state]
    for n in range(1,nmax+1):
        state=16*state+chiral_forcing(n)
        out.append(state)
    return tuple(out)


def chiral_integer_carry(n:int)->int:
    return 8*(16**n-1)//15


def odd_torsion_coordinate(x:Fraction,level:int)->Fraction:
    """Unique odd-order 16^(-level) root of e(x) in the circle."""
    x=mod_one(Fraction(x))
    if x.denominator%2==0 or level<0:
        raise ValueError("Requires exact odd-order torsion and nonnegative level")
    q=x.denominator
    if q==1: return Fraction(0)
    k=(x.numerator*pow(pow(16,level,q),-1,q))%q
    return Fraction(k,q)


def odd_torsion_tower(x:Fraction,levels:int)->tuple[Fraction,...]:
    if levels<1: raise ValueError("positive tower height")
    return tuple(odd_torsion_coordinate(x,j) for j in range(levels))


def half_turn_tower(levels:int)->tuple[Fraction,...]:
    if levels<1:raise ValueError("positive tower height")
    return tuple(Fraction(1,2*16**j) for j in range(levels))


def compatible_tower(xs:tuple[Fraction,...])->bool:
    return bool(xs) and all(mod_one(16*xs[j+1])==mod_one(xs[j]) for j in range(len(xs)-1))


def tower_add(a,b):
    if len(a)!=len(b):raise ValueError("tower heights must match")
    return tuple(mod_one(x+y) for x,y in zip(a,b))


def tower_scale(a,k:int):
    return tuple(mod_one(k*x) for x in a)


def tower_source_step(state, forcing:Fraction):
    src=odd_torsion_tower(forcing,len(state))
    return tower_add(tower_scale(state,16),src)


def tower_four_inverse(state):
    """Requires one extra coordinate, returns [4]^-1 at all available levels."""
    if len(state)<2 or not compatible_tower(state):raise ValueError("compatible tower >=2 needed")
    return tuple(mod_one(4*state[j+1]) for j in range(len(state)-1))


def tower_chiral(state,halfturn):
    if len(state)!=len(halfturn):raise ValueError("tower heights")
    return tower_add(halfturn,tower_scale(state,-1))


def tower_chiral_source(state,halfturn,forcing):
    """J_t F_r J_t, its true levelwise source = (1-16)t-iota(r)."""
    src=odd_torsion_tower(forcing,len(state))
    transformed=tower_add(tower_scale(halfturn,-15),tower_scale(src,-1))
    return tower_add(tower_scale(state,16),transformed)


def tower_character(state,numerator:int,level:int)->Fraction:
    """Returns angle modulo 1 for chi_(numerator/16^level)."""
    if level<0 or level>=len(state):raise ValueError("character level outside tower")
    return mod_one(numerator*state[level])


def dual_shift_phase(state,forcing:Fraction,numerator:int,level:int):
    """Exact source-labelled Fourier dual: chi_q(F state)=chi_(16q)(state)*chi_q(source)."""
    future=tower_source_step(state,forcing)
    src=odd_torsion_tower(forcing,len(state))
    return (tower_character(future,numerator,level),
            mod_one(tower_character(state,16*numerator,level)+tower_character(src,numerator,level)))


def finite_chiral_torsor_map(index:int,modulus:int,step:Fraction)->int:
    """Honest block permutation of A plus J(A) in even 2Q clock.

    Index even = original odd torsion k/Q; index odd = dual halfturn coset.
    The two sectors use different source labels and are not the naive map
    y->16y+b on the whole 2Q clock.
    """
    if modulus<3 or modulus%2!=1:raise ValueError("Q odd")
    qq=2*modulus
    if index<0 or index>=qq:raise ValueError("index outside clock")
    step=mod_one(Fraction(step))
    if modulus%step.denominator:
        raise ValueError("Q must contain the complete source denominator")
    b=(step.numerator*(modulus//step.denominator))%modulus
    if index%2==0:
        return (16*index+2*b)%qq
    return (16*index+modulus-2*b)%qq


def finite_chiral_j(index:int,modulus:int)->int:
    return (modulus-index)%(2*modulus)


def fourier_squared_reflection(index:int,even_modulus:int)->int:
    """DFT_Q^2|x>=|-x>; S_(Q/2) times F^2 realizes arctan J."""
    if even_modulus%2:raise ValueError("need even clock")
    return (even_modulus//2-index)%even_modulus


def arctan_ratio_machin_factor()->tuple[tuple[int,int],tuple[int,int]]:
    """(5+i)^4 = 2(1+i)(239+i), exact Gaussian integer identity."""
    def times(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    p=(5,1)
    for _ in range(3):p=times(p,(5,1))
    q=times((2,2),(239,1))
    return p,q


def arctan_alternating_bounds(inv:int,terms:int)->tuple[Fraction,Fraction]:
    if inv<=1 or terms<=0:raise ValueError("inv > 1; terms positive")
    sumv=sum(((-1)**k*Fraction(1,(2*k+1)*inv**(2*k+1)) for k in range(terms)),Fraction(0))
    nextterm=Fraction(1,(2*terms+1)*inv**(2*terms+1))
    return (sumv,sumv+nextterm) if terms%2==0 else (sumv-nextterm,sumv)


def machin_pi_bounds(terms:int)->tuple[Fraction,Fraction]:
    a,b=arctan_alternating_bounds(5,terms)
    c,d=arctan_alternating_bounds(239,terms)
    return 16*a-4*d,16*b-4*c


def odd_register_fourier_step(momentum:int,conductor:int,source_term:Fraction)->tuple[int,Fraction]:
    """DFT_Q P_(16,r) DFT_Q^-1 on |p>, exponent as Fraction mod 1.

    P|x> = |16x + Q*r modQ>, Q odd and multiple of den(r).
    DFT_Q|x>=1/sqrt(Q)sum_k e(-kx/Q)|k>.
    Returns output |p/16> times e(-p*16^-1*(Q*r)/Q).
    """
    source_term=mod_one(Fraction(source_term))
    if conductor<3 or conductor%2==0 or conductor%source_term.denominator:
        raise ValueError("Odd conductor must contain source denominator")
    inv=pow(16,-1,conductor)
    rlabel=(source_term.numerator*(conductor//source_term.denominator))%conductor
    return ((momentum*inv)%conductor,
            mod_one(Fraction(-momentum*inv*rlabel,conductor)))


def cauchy_unnormalized(t:Fraction)->Fraction:
    t=Fraction(t)
    return 1/(1+t*t)


def cauchy_inversion_density_identity(t:Fraction)->tuple[Fraction,Fraction]:
    """J:t->1/t preserves dt/[pi(1+t^2)] as a probability measure."""
    t=Fraction(t)
    if not t:raise ValueError("Use projective endpoint chart at 0/infinity")
    return cauchy_unnormalized(t), cauchy_unnormalized(1/t)/t**2


def cauchy_rotation_density_identity(t:Fraction,angle_tangent:Fraction)->tuple[Fraction,Fraction]:
    """Möbius angular isometry of standard Cauchy measure, exact rationals."""
    t=Fraction(t);a=Fraction(angle_tangent)
    if 1-a*t==0:raise ValueError("Use reciprocal projective chart at pole")
    tnew=(t+a)/(1-a*t)
    jac=(1+a*a)/(1-a*t)**2
    return cauchy_unnormalized(t), cauchy_unnormalized(tnew)*jac


def projective_circle_double(t:Fraction)->Fraction | None:
    """tan(2 atan(t)); None = point at infinity."""
    t=Fraction(t)
    if 1-t*t==0:return None
    return 2*t/(1-t*t)


def original_positive_polynomial(t:Fraction)->Fraction:
    t=Fraction(t)
    return 4-2*t**3-t**4-t**5


def completed_mellin_density(t:Fraction)->Fraction:
    t=Fraction(t)
    if t**8==16:raise ValueError("Mellin denominator singular")
    return original_positive_polynomial(t)/(16-t**8)


def completed_mellin_reduced(t:Fraction)->Fraction:
    t=Fraction(t)
    d=(2-t*t)*(t*t-2*t+2)
    if not d:raise ValueError("Reduced source pole")
    return (1-t)/d


def geometric_angular_eighth(t:Fraction)->Fraction:
    """The density (1/8)*eta(t-1), eta(u)=2du/(1+u²)."""
    t=Fraction(t)
    return Fraction(1,4)/(1+(t-1)**2)


def log_coboundary_derivative(t:Fraction)->Fraction:
    """d/dt [ log((2-t²)/(t²-2t+2))/8 ]."""
    t=Fraction(t)
    if (2-t*t)*(t*t-2*t+2)==0:raise ValueError("Outside boundary chart")
    return (Fraction(1,8)*(-2*t/(2-t*t)-(2*t-2)/(t*t-2*t+2)))


def log_boundary_ratio(t:Fraction)->Fraction:
    """Positive log argument at endpoints; exact 1 at t=0,1."""
    t=Fraction(t)
    return (2-t*t)/(t*t-2*t+2)


def beta_8_9()->Fraction:
    from math import factorial
    return Fraction(factorial(7)*factorial(8),factorial(16))


def positive_mutant_period_bounds(epsilon:Fraction)->tuple[Fraction,Fraction]:
    """Added source eps * Beta(8n,9) shifts completed period by interval.

    15<=16-t^8<=16 gives the exact, strict positive Beta bounds.
    """
    epsilon=Fraction(epsilon)
    if epsilon<=0:raise ValueError("Positive mutation only")
    return epsilon*beta_8_9()/16,epsilon*beta_8_9()/15
