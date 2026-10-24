"""Source-faithful BBP Green-tail and signed-pole moment certificates.

The four poles belong to the *forcing-index* variable, not states of the
hexadecimal circle covering. All executable checks use exact Fraction values.
The strict all-order moment/Hankel claims have paper proofs in the companion
dossier. No pi-normality theorem, Weil positivity, or physical access follows.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction as Q
from math import isqrt

# r(n) = sum_i residue_i / (n - pole_i), n >= 1.
POLE_DATA = (
    (Q(7, 8), Q(1, 2)),
    (Q(1, 2), -Q(1, 4)),
    (Q(3, 8), -Q(1, 8)),
    (Q(1, 4), -Q(1, 8)),
)
BBP_INITIAL = Q(0)


def _natural(x, lower=0):
    if type(x) is not int or x < lower:
        raise ValueError(f"expected integer >= {lower}")
    return x


def forcing(n: int) -> Q:
    _natural(n, 1)
    return sum((w / (n - a) for a, w in POLE_DATA), Q())


def pole_moment(k: int) -> Q:
    """Signed forcing-index moment. In particular m0=0 and m1=15/64."""
    _natural(k)
    return sum((w*a**k for a, w in POLE_DATA), Q())


def positive_source_kernel(t: Q) -> Q:
    """4-2t^3-t^4-t^5; positive on [0,1) despite signed input poles."""
    t = Q(t)
    if t < 0 or t > 1:
        raise ValueError("requires source integration variable in [0,1]")
    return 2*(1-t**3)+(1-t**4)+(1-t**5)


def forcing_integral_exact(n: int) -> Q:
    """Exact elementary integral int_0^1 t^(8(n-1))*g(t) dt."""
    _natural(n, 1)
    s = 8*(n-1)
    return Q(4, s+1)-Q(2, s+4)-Q(1, s+5)-Q(1, s+6)


def tail_interval(n: int, terms: int = 8) -> tuple[Q, Q]:
    """Strict source-only rational enclosure of t_n=sum_{k>=1}16^-k*r(n+k)."""
    _natural(n); _natural(terms, 1)
    lo = sum((forcing(n+k)/16**k for k in range(1, terms+1)), Q())
    hi = lo + forcing(n+terms+1)/(Q(15)*16**terms)
    return lo, hi


def first_hankel_interval(terms: int = 2) -> tuple[Q, Q]:
    """Certified interval for det [[t0,t1],[t1,t2]] from positive source tails."""
    a, b, c = (tail_interval(i, terms) for i in range(3))
    return a[0]*c[0]-b[1]**2, a[1]*c[1]-b[0]**2


def cauchy_matrix() -> tuple[tuple[Q, ...], ...]:
    """Known source-pole Cauchy readout at n=1,2,3,4."""
    return tuple(tuple(1/(Q(n)-a) for a, _ in POLE_DATA)
                 for n in range(1,5))


def fraction_determinant(matrix) -> Q:
    """Independent exact Gaussian determinant for square Fraction matrices."""
    a = [list(map(Q,row)) for row in matrix]
    n=len(a)
    if any(len(row)!=n for row in a):
        raise ValueError("square matrix required")
    out=Q(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]), None)
        if pivot is None:
            return Q()
        if pivot != j:
            a[j],a[pivot]=a[pivot],a[j]
            out=-out
        q=a[j][j]
        out*=q
        for i in range(j+1,n):
            c=a[i][j]/q
            for k in range(j+1,n):
                a[i][k]-=c*a[j][k]
            a[i][j]=Q()
    return out


def recover_pole_weights(observations) -> tuple[Q,...]:
    """Four samples distinguish four unknown signed weights at FIXED poles."""
    if len(observations)!=4:
        raise ValueError("exactly four source-index readouts required")
    mat=[list(row)+[Q(y)] for row,y in zip(cauchy_matrix(),observations)]
    for j in range(4):
        pivot=next((i for i in range(j,4) if mat[i][j]),None)
        if pivot is None:
            raise ArithmeticError("unidentifiable specified pole source")
        mat[j],mat[pivot]=mat[pivot],mat[j]
        scale=mat[j][j]
        mat[j]=[x/scale for x in mat[j]]
        for i in range(4):
            if i!=j:
                s=mat[i][j]
                mat[i]=[a-s*b for a,b in zip(mat[i],mat[j])]
    return tuple(row[4] for row in mat)


def forced_step(state: Q, n: int) -> Q:
    """Lawful BBP forward map at n>=1; do not replace by unforced doubling."""
    return (16*Q(state)+forcing(n))%1


def source_alpha_interval(initial: Q, terms: int=8) -> tuple[Q,Q]:
    """The circle orbit selected by forcing AND initial, not by forcing alone."""
    l,u=tail_interval(0,terms)
    return Q(initial)+l, Q(initial)+u


def rational_counterfeit_tail(n: int) -> Q:
    """Positive continuous Hausdorff moment source, but t0=1/2 is rational."""
    _natural(n)
    return Q(1,(n+1)*(n+2))


def rational_counterfeit_forcing(n: int) -> Q:
    _natural(n, 1)
    return 16*rational_counterfeit_tail(n-1)-rational_counterfeit_tail(n)


def cosine_sign_pi_over_four(n: int) -> int:
    """For odd n, cos(n*pi/4) is +/-sqrt(2)/2."""
    _natural(n, 1)
    if n%2==0:
        raise ValueError("odd source frequency required")
    return 1 if n%8 in (1,7) else -1


def _prime_divisors(n):
    return tuple(p for p in range(2,n+1)
                 if n%p==0 and all(p%d for d in range(2,isqrt(p)+1)))


@lru_cache(None)
def exact_prime_path_flips(n: int) -> int:
    """Exact min-plus path cost / sqrt(2) for source delta_{1/8}, odd n."""
    _natural(n, 1)
    if n%2==0:
        raise ValueError("only odd frequencies in this exact witness")
    if n==1:
        return 0
    return min(exact_prime_path_flips(n//p)
               + (cosine_sign_pi_over_four(n)!=cosine_sign_pi_over_four(n//p))
               for p in _prime_divisors(n))


def false_deepseek_cost_bound_witness() -> dict:
    """R=3: exact LHS=4*sqrt(2)/3 versus falsely claimed RHS=4/3."""
    a,b=exact_prime_path_flips(15),exact_prime_path_flips(255)
    if (a,b)!=(2,2):
        raise AssertionError("source-specific minplus path witness changed")
    return {"source":"delta_{1/8}", "R":3,"d15_over_sqrt2":a,
            "d255_over_sqrt2":b,"lhs_over_sqrt2":Q(2*(2*a+b),9),
            "claimed_upper":Q(4,3), "refuted_by":"sqrt(2)>1"}
