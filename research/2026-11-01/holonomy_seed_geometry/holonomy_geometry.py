"""Original four-pole BBP: source-labelled affine Wilson echoes, curvature
reconstruction, positive Hausdorff source mutants, and control-state geometry.

Source facts are never inferred from a surrogate model. All finite computations
are exact Fraction/int. Complex phases enter ONLY in separately proved paper
identities; numerical roots of unity are never treated as exact certificates.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, factorial


def integer(n: int, lower: int = 1, upper: int = 2000):
    if type(n) is not int or not lower <= n <= upper:
        raise ValueError(f"exact integer required in [{lower},{upper}]")
    return n


def r(n: int) -> F:
    """The four unchanged signed BBP poles, for n >= 1."""
    integer(n)
    return F(4,8*n-7) - F(2,8*n-4) - F(1,8*n-3) - F(1,8*n-2)


def r_combined(n: int) -> F:
    integer(n)
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def affine_compose(f: tuple[F,F],g:tuple[F,F]) -> tuple[F,F]:
    """Composition f ∘ g, with x -> a x+b."""
    a,b=f; c,d=g
    return (a*c,a*d+b)


def affine_inverse(f:tuple[F,F]) -> tuple[F,F]:
    a,b=f
    if a==0: raise ValueError("noninvertible affine path")
    return (1/a,-b/a)


def source_step(n:int)->tuple[F,F]:
    return (F(16),r(n))


def affine_order_commutator(i:int,j:int)->tuple[F,F]:
    """F_j F_i F_j^{-1} F_i^{-1}; pure translation by 15(r_i-r_j)."""
    fi=source_step(i); fj=source_step(j)
    return affine_compose(affine_compose(affine_compose(fj,fi),affine_inverse(fj)),affine_inverse(fi))


def curvature(n:int)->F:
    """Adjacent non-Abelian affine path-order displacement d_n."""
    integer(n,1,1999)
    return F(15)*(r(n)-r(n+1))


def orbit(n:int, seed:F=F(0))->F:
    integer(n,0,1000)
    if not isinstance(seed,F):raise TypeError("seed must be an exact Fraction")
    u=seed
    for j in range(1,n+1):u=16*u+r(j)
    return u


def curvature_reconstruction(n:int,seed:F=F(0))->F:
    """Exact path reconstruction from adjacent commutators + boundary."""
    integer(n,1,400)
    if not isinstance(seed,F):raise TypeError("seed must be an exact Fraction")
    return (F(16**n-1,15)*r(n)
        +sum((F(16**n-16**(n-j),225)*curvature(j) for j in range(1,n)),F())
        +16**n*seed)


def integrated_curvature(n:int)->F:
    """Unweighted sum of d_j over 1<=j<n; equals 47-15*r(n)."""
    integer(n)
    return sum((curvature(j) for j in range(1,n)),F())


def curvature_prefix(k:int)->F:
    integer(k,0,200)
    return sum((F(curvature(n),16**n) for n in range(1,k+1)),F())


def pi_upper(k:int)->F:
    """A rational, strictly greater than pi, from signed Wilson curvature."""
    integer(k,0,200)
    return F(16,225)*(47-curvature_prefix(k))


def pi_error_bound(k:int)->F:
    """0 < pi_upper(k)-pi < this source-only rational bound, k >= 0.

    The future curvature d_{k+j} is decreasing because the original source
    is a strict Hausdorff moment with nonnegative density on (0,1).
    """
    integer(k,0,199)
    return F(16,225)*curvature(k+1)*F(1,15*16**k)


def partial_pi(k:int)->F:
    integer(k,0,200)
    return sum((F(16*r(j),16**j) for j in range(1,k+1)),F())


def sharp_tail_upper(k:int)->F:
    """0<T_k<1/[(8k+1)(8k+2)] for k >=1."""
    integer(k)
    return F(1,(8*k+1)*(8*k+2))


def source_prefix_q(k:int)->F:
    """q_k=sum_{j<=k}16^{-j}r(j), rational completed seed shadow."""
    integer(k)
    return sum((F(r(j),16**j) for j in range(1,k+1)),F())


def seed_mode_mean(n:int)->F:
    integer(n)
    return F(sum(16**j for j in range(1,n+1)),n)


def seed_mode_variance(n:int)->F:
    integer(n)
    mean=seed_mode_mean(n)
    return F(sum(256**j for j in range(1,n+1)),n)-mean**2


def exact_qfi_divided_by_pi_sq(n:int,h:int)->F:
    """F_Q/pi^2 =16*h^2*Var(16^n)."""
    integer(n); integer(abs(h),1,100000)
    return 16*h*h*seed_mode_variance(n)


def finite_shadow_norm_upper_sq(n:int,h:int)->F:
    """Strict rational square bound for distance of N-control states.

    |-delta| = alpha-q_n = 16^-n*T_n;
    T_n<1/[(8n+1)(8n+2)], and 2pi<44/7.
    """
    integer(n);integer(abs(h),1,100000)
    tail=sharp_tail_upper(n)
    # Drop geometric factor (1-256^-n) to simplify bound; remains strict.
    return F(44*44*h*h,7*7)*tail*tail*F(256,255*n)


def min_copies_lower_for_helstrom_3_4(n:int,h:int)->F:
    """Necessary copies m > this value for Helstrom success >= 3/4.

    Uses |Psi_q-Psi_qn|^2 < finite_shadow_norm_upper_sq.
    Pure tensor m-copy trace distance <=sqrt(m)*sqrt(bound).
    """
    return 1/(4*finite_shadow_norm_upper_sq(n,h))


def _solve_linear(matrix:list[list[F]], rhs:list[F])->list[F]:
    n=len(rhs)
    if len(matrix)!=n or any(len(row)!=n for row in matrix):
        raise ValueError("square system required")
    a=[list(map(F,matrix[i]))+[F(rhs[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:raise ArithmeticError("moment matrix singular")
        a[j],a[pivot]=a[pivot],a[j]
        scale=a[j][j];a[j]=[v/scale for v in a[j]]
        for i in range(n):
            if i!=j:
                fac=a[i][j]
                a[i]=[a[i][k]-fac*a[j][k] for k in range(n+1)]
    return [row[-1] for row in a]


def orthogonal_monic(m:int)->tuple[F,...]:
    """Original-source monic degree-m polynomial orthogonal to lower monomials.
    Return c0,...,cm, cm=1. All coefficients are exact rationals.
    """
    integer(m,1,9)
    mat=[[r(i+j+1) for j in range(m)] for i in range(m)]
    rhs=[-r(i+m+1) for i in range(m)]
    return tuple(_solve_linear(mat,rhs))+ (F(1),)


def moment_poly(coeff:tuple[F,...],power:int=0)->F:
    """int_0^1 u^power P(u) dmu(u) where mu is ORIGINAL BBP mu."""
    integer(power,0,40)
    if not coeff or any(not isinstance(c,F) for c in coeff):
        raise TypeError("exact Fraction polynomial")
    return sum((c*r(i+power+1) for i,c in enumerate(coeff)),F())


def poly_evaluate(coeff:tuple[F,...],z:F)->F:
    if not isinstance(z,F):raise TypeError("exact coordinate")
    res=F()
    for c in reversed(coeff):res=res*z+c
    return res


def poly_mass_square(coeff:tuple[F,...])->F:
    return sum((a*b*r(i+j+1) for i,a in enumerate(coeff) for j,b in enumerate(coeff)),F())


def poly_sup_bound(coeff:tuple[F,...])->F:
    """Simple safe sup norm on [0,1]."""
    return sum((abs(c) for c in coeff),F())


def stieltjes_pole_response_bounds(m:int)->tuple[F,F]:
    """Rational strict lower/upper for J=int P_m(u)/(16-u) dmu(u)>0.
    Identical J=(int P_m^2/(16-u)dmu)/P_m(16).
    """
    coeff=orthogonal_monic(m)
    assert all(moment_poly(coeff,k)==0 for k in range(m))
    mass_sq=poly_mass_square(coeff)
    pole=poly_evaluate(coeff,F(16))
    if mass_sq<=0 or pole<=0:raise ArithmeticError("positive orthogonal source failed")
    return mass_sq/(16*pole),mass_sq/(15*pole)


def mutated_source_moment(m:int,t:F,n:int)->F:
    """Finite positive-measure mutant: dmu_t=(1+t P_m(u))dmu.
    Require |t|*sum|coeff|<1; retains original first m r values.
    """
    if not isinstance(t,F):raise TypeError("rational perturbation required for exact probe")
    coeff=orthogonal_monic(m)
    if abs(t)*poly_sup_bound(coeff)>=1:raise ValueError("positivity budget violated")
    return r(n)+t*moment_poly(coeff,n-1)


def source_mutation_probe(m:int)->dict:
    coeff=orthogonal_monic(m)
    norm=poly_sup_bound(coeff)
    t=F(1,2)/norm
    lo,hi=stieltjes_pole_response_bounds(m)
    return dict(degree=m,coefficient_strings=[str(x) for x in coeff],
        sup_bound=str(norm),perturbation=str(t),
        zero_moments=[str(moment_poly(coeff,k)) for k in range(m)],
        first_changed_moment=str(mutated_source_moment(m,t,m+1)-r(m+1)),
        response_lower=str(t*lo),response_upper=str(t*hi))


def machin_pi_interval(terms:int=40)->tuple[F,F]:
    """Exact rational enclosure from π=16atan(1/5)−4atan(1/239).

    A positive-z alternating arctan series has remainder bounded by the
    magnitude of the first omitted term, with sign of that term.
    """
    integer(terms,1,100)
    def atan_interval(d):
        s=sum((F((-1)**j,(2*j+1)*d**(2*j+1)) for j in range(terms)),F())
        rem=F((-1)**terms,(2*terms+1)*d**(2*terms+1))
        return min(s,s+rem),max(s,s+rem)
    a,b=atan_interval(5);c,d=atan_interval(239)
    return 16*a-4*d,16*b-4*c


def rational_nonnormal_mutant_certificate(m:int,terms:int=60)->dict:
    """Construct a SPECIFIC rational completed q for a positive M-jet fake.

    The actual change in source weight is t=(q-pi/16)/J_m with
    J_m=int P_m/(16-u) dmu>0. The exact rational bounds prove 0<t<1/C,
    preserving all original first m source moments while giving completed
    rational q and hence a nonnormal base16 orbit at fixed frequency den(q).
    This is a SYMBOLIC source change, not unchanged literal BBP poles.
    """
    coeff=orthogonal_monic(m)
    C=poly_sup_bound(coeff)
    Jlo,Jhi=stieltjes_pole_response_bounds(m)
    pil,pih=machin_pi_interval(terms)
    alo,ahi=pil/16,pih/16
    tmax=F(1,2*C)
    space=tmax*Jlo/4
    if not ahi-alo<space:
        raise ValueError("pi interval too weak for this source-mutation certificate")
    q=ahi+space
    epslo=(q-ahi)/Jhi
    epshi=(q-alo)/Jlo
    if not F(0)<epslo<epshi<tmax:
        raise ArithmeticError("strict positive density not certified")
    return dict(m=m,q=q,pi_interval=(pil,pih),epsilon_interval=(epslo,epshi),
                C=C,response_interval=(Jlo,Jhi),
                exact_prefix_equal=True,non_normal_harmonic=q.denominator)


def k5_shadow_norm_upper_sq(n:int,h:int)->F:
    """Universal explicit O_h(n^-5) squared pure-state distance bound."""
    integer(n); integer(abs(h),1,100000)
    return F(121*h*h,12495*n**5)


def k5_copies_lower_for_3_4(n:int,h:int)->F:
    """Necessary m > (12495/(484*h^2))*n^5 independent echo copies."""
    integer(n); integer(abs(h),1,100000)
    return F(12495*n**5,484*h*h)


def local_wilson_tilt_rational_error_bound(n:int,h:int)->F:
    """For any unit phases z_1..z_n, bound absolute difference of MEANS
    between z_j and z_j*exp(2πi h d_j), using 2π<44/7:
        < 47*(44/7)*|h|/n.
    This is NOT a claim that either mean is small.
    """
    integer(n);integer(abs(h),1,100000)
    return F(47*44*abs(h),7*n)


def finite_curvature_mass(n:int)->F:
    """Sum d_j for j=1..n, strictly <47 and exactly 47-15r(n+1)."""
    integer(n)
    return 47-F(15)*r(n+1)
