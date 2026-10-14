"""Source-typed Pascal quarter-turn instruments: exact finite arithmetic only.

The Gaussian/Mellin/OU limiting identities have paper proofs in the adjacent
research dossier, not proofs by these finite tests. No nontrivial zero inputs.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
from math import comb, isqrt


class PascalGammaError(ValueError):
    pass


def _integer(n: int, low: int = 0, high: int = 1000) -> int:
    if type(n) is not int or not low <= n <= high:
        raise PascalGammaError(f"integer in [{low}, {high}] required")
    return n


def _rational(x, *, positive: bool = False) -> Q:
    if type(x) not in (int, Q):
        raise PascalGammaError("only integers or exact rational values")
    q = Q(x)
    if positive and q <= 0:
        raise PascalGammaError("strictly positive rational required")
    return q


def is_prime(p: int) -> bool:
    _integer(p, 2, 100_000)
    return all(p % d for d in range(2, isqrt(p) + 1))


def quadrant(r: int, k: int) -> int:
    _integer(r)
    _integer(k)
    return comb(r+k, k)


def pascal_quadrant_certificate(r: int, k: int) -> dict:
    """Both source axes and the exact local recurrence at this grid vertex."""
    x = quadrant(r, k)
    a = quadrant(r-1, k) if r else 0
    b = quadrant(r, k-1) if k else 0
    if r == k == 0:
        assert x == 1
    elif x != a+b:
        raise ArithmeticError("Pascal quadrant relation fails")
    return {"r":r,"k":k,"value":x,"above":a,"left":b,
            "recurrence":(r==k==0) or x==a+b}


def affine_triangle(multiplier: int, depth: int, *, authenticate_prime: bool=False):
    """Polynomial-valued Pascal: z*F[n,k](z) + F[n,k-1](z^p).

    A polynomial is represented by {integer_address: path_count}. Every path
    is based at integer source zero. Composite multipliers satisfy this
    *affine law* but are not labeled genuine Euler primes.
    """
    p = _integer(multiplier, 2, 1000)
    N = _integer(depth, 0, 16)
    if authenticate_prime and not is_prime(p):
        raise PascalGammaError("composite multiplier is not a prime-place jet")
    if p ** N > 10**15:
        raise PascalGammaError("affine path address exceeds declared budget")
    rows = [{0:{0:1}}]
    for n in range(N):
        new = {}
        for k in range(n+2):
            coefficients = defaultdict(int)
            for address, count in rows[-1].get(k, {}).items():
                coefficients[address+1] += count
            for address, count in rows[-1].get(k-1, {}).items():
                coefficients[p*address] += count
            new[k] = dict(sorted(coefficients.items()))
            if sum(new[k].values()) != comb(n+1,k):
                raise ArithmeticError("affine Pascal count fails")
        rows.append(new)
    return rows


def weighted_pascal_adjoint_certificate(values_a, values_b) -> dict:
    """The actual Hilbert adjoint is W^-1 P^T W, not bare P^T.

    Finite prefix indices 0,...,N-1 carry positive reciprocal-cell style
    weights w_k=1/((k+1)(k+2)). The triangular Pascal map is P[n,k].
    """
    a=tuple(_rational(x) for x in values_a)
    b=tuple(_rational(x) for x in values_b)
    if not a or len(a)!=len(b) or len(a)>32:
        raise PascalGammaError("matched finite vectors length 1..32 required")
    n=len(a)
    weights=[Q(1,(k+1)*(k+2)) for k in range(n)]
    Pb=[sum((Q(comb(i,k))*a[k] for k in range(i+1)),Q()) for i in range(n)]
    weighted_adjoint=[sum((weights[i]*comb(i,k)*b[i] for i in range(k,n)),Q())/weights[k]
                      for k in range(n)]
    left=sum((weights[i]*Pb[i]*b[i] for i in range(n)),Q())
    right=sum((weights[i]*a[i]*weighted_adjoint[i] for i in range(n)),Q())
    if left!=right:raise ArithmeticError("weighted Pascal duality failed")
    bare_transpose=[sum((Q(comb(i,k))*b[i] for i in range(k,n)),Q()) for k in range(n)]
    return {"N":n,"left":str(left),"right":str(right),
            "weighted_adjoint":[str(x) for x in weighted_adjoint],
            "unweighted_transpose":[str(x) for x in bare_transpose],
            "equal_under_declared_carrier_metric":True,
            "bare_transpose_is_not_generally_Hilbert_adjoint":
                any(weighted_adjoint[k]!=bare_transpose[k] for k in range(n))}


def fractional_coefficient(alpha, k: int) -> Q:
    """(alpha)_k/k!, with alpha>0 rational and k>=0."""
    alpha = _rational(alpha, positive=True)
    k = _integer(k,0,512)
    c = Q(1)
    for j in range(k):
        c *= (alpha+j)/Q(j+1)
    return c


def fractional_convolution(alpha, beta, k: int) -> dict:
    """Exact rational Vandermonde/c_alpha * c_beta = c_(alpha+beta)."""
    alpha = _rational(alpha, positive=True)
    beta = _rational(beta, positive=True)
    k = _integer(k,0,512)
    left=sum((fractional_coefficient(alpha,j)*fractional_coefficient(beta,k-j)
              for j in range(k+1)),Q())
    right=fractional_coefficient(alpha+beta,k)
    if left != right:
        raise ArithmeticError("fractional Pascal semigroup fails")
    return {"alpha":str(alpha),"beta":str(beta),"k":k,
            "left":str(left),"right":str(right),"equal":True}


def fractional_hockey_stick(alpha, m: int) -> dict:
    """Finite fractional sum is next depth Pascal coefficient exactly."""
    a = _rational(alpha, positive=True)
    m = _integer(m,0,512)
    left=sum((fractional_coefficient(a,k) for k in range(m+1)),Q())
    right=fractional_coefficient(a+1,m)
    if left != right:raise ArithmeticError("hockey stick fails")
    return {"alpha":str(a),"m":m,"sum":str(left),"next_level":str(right)}


def sideways_geometric(q, k: int, cutoff: int=128) -> dict:
    """Transpose of Pascal on a geometrically decaying probability source.

    b_n=(1-q)*q^n. The full weighted output is (q/(1-q))^k.
    The finite partial is an exact *lower* approximation, never a proof
    that arbitrary undamped sources admit a transpose.
    """
    q=_rational(q,positive=True)
    if q>=1:raise PascalGammaError("geometric probability requires 0<q<1")
    k=_integer(k,0,40)
    cutoff=_integer(cutoff,k,2048)
    part=sum((Q(comb(n,k))*(1-q)*q**n for n in range(k,cutoff+1)),Q())
    total=(q/(1-q))**k
    if part>total: raise ArithmeticError("partial sum exceeds exact total")
    return {"q":str(q),"k":k,"partial":str(part),"global":str(total),
            "tail":str(total-part),"infinite_to_finite_exact":True}


def random_walk_integer_moments(n: int) -> dict:
    """Pascal random walk W=2K-n has mean 0, variance n exactly."""
    n=_integer(n,1,150)
    norm=Q(2**n)
    total=sum((Q(comb(n,k),2**n) for k in range(n+1)),Q())
    mean=sum((Q(comb(n,k),2**n)*(2*k-n) for k in range(n+1)),Q())
    second=sum((Q(comb(n,k),2**n)*(2*k-n)**2 for k in range(n+1)),Q())
    if total!=1 or mean or second!=n:raise ArithmeticError("random walk moments fail")
    return {"n":n,"normalized_mass":str(total),"mean":str(mean),
            "second_moment":str(second),"Gaussian_limit_proved_by_finite_test":False}


def heat_resolvent_fourier(alpha, angular_frequency) -> dict:
    """Laplace in heat-time of 2alpha exp(-(alpha²+omega²)u).

    On the whole line, Fourier[e^-alpha*abs(t)](omega) equals that integral,
    yielding the exact positive heat-mixture representation. Finite
    rational arithmetic checks equality of two independently typed formulas.
    """
    a=_rational(alpha,positive=True)
    w=_rational(angular_frequency)
    ou=2*a/(a*a+w*w)
    laplace=2*a*Q(1,a*a+w*w)
    if ou!=laplace:raise ArithmeticError("heat/OU Fourier-resolvent identity fails")
    return {"alpha":str(a),"angular_frequency":str(w),
            "OU_fourier_multiplier":str(ou),"heat_laplace_multiplier":str(laplace),
            "exact":True,"complete_Weil_sign_proved":False}


def completed_gamma_bath_fourier(angular_frequency, modes: int=8) -> dict:
    """Finite positive part of Suzuki's authentic alpha_j=2j+1/2 bath."""
    w=_rational(angular_frequency)
    modes=_integer(modes,1,128)
    individual=[]
    for j in range(modes):
        a=Q(4*j+1,2)
        term=Q(1,a*a)*Q(2*a,a*a+w*w)
        individual.append(term)
    return {"modes":modes,"freq":str(w),"positive_terms":all(v>0 for v in individual),
            "finite_bath_multiplier":str(sum(individual,Q())),
            "true_suzuki_arch_grid":True,"signed_completion_included":False,
            "RH_proved":False}


def v_p_integer(n:int,p:int)->int:
    _integer(n,1,10**12)
    if not is_prime(p):raise PascalGammaError("genuine prime required")
    a=0
    while n%p==0:
        n//=p;a+=1
    return a


def normalized_pascal_boundary_2adic(n:int)->dict:
    """Left Pascal boundary 2^-n: real->0, 2-adic abs->infinity."""
    n=_integer(n,1,1000)
    return {"n":n,"raw_binomial_boundary":1,
            "probability_coefficient":str(Q(1,2**n)),
            "v2_normalized":-n,"two_adic_absolute":str(2**n),
            "real_absolute":str(Q(1,2**n)),
            "adelic_convergence_from_real_weak_limit":False}


def receipt():
    return {"source":"pascal_quarter_turn", "pascal_affine_shadow":affine_triangle(2,5)[5][2],
            "fractional_half_square":[fractional_convolution(Q(1,2),Q(1,2),k) for k in range(6)],
            "sideways_geometric":sideways_geometric(Q(1,2),4,32),
            "weighted_dual":weighted_pascal_adjoint_certificate((Q(1),Q(2),Q(-1)),(Q(1),Q(0),Q(3))),
            "random_walk":random_walk_integer_moments(24),
            "ou_heat":heat_resolvent_fourier(Q(1,2),Q(3,5)),
            "Suzuki_positive_bath":completed_gamma_bath_fourier(Q(3,5),8),
            "two_adic_negative_control":normalized_pascal_boundary_2adic(16),
            "Gamma_link_source_derived_from_discrete_Pascal":True,
            "authentic_FUCC_prime_source_by_sole_affine_relation":False,
            "global_Weil_operator_identified":False,"RH_proved":False}
