"""Factorial prime-power Borwein windows, cardinal sampling, and exact SUCC transport.

The prime-power windows are SOURCE-LABELLED by Legendre valuations of N!.
Convolving them with U[-1/2,1/2] yields the SAME integer-lattice delta
at every N, despite different off-grid variances and Fourier moments.

This is classical probability / arithmetic as a new-to-SUCC realization.
It is not a fast primality oracle, ABC bound, Green--Tao transference,
positive Weil form, or RH evidence. Full exact off-grid density queries
have a declared exponential subset-enumeration budget.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial, prod
from typing import Iterable

from .borwein_prime_clock import prime, uniform_sum_cdf

MAX_FACTORIAL_HORIZON = 256
MAX_OFF_GRID_WINDOWS = 11
MAX_POISSON_DEGREE = 80


class FactorialHologramError(ValueError):
    """Bad arithmetic provenance, input type, or finite resource bound."""


def _horizon(n: int) -> int:
    if type(n) is not int or not 1 <= n <= MAX_FACTORIAL_HORIZON:
        raise FactorialHologramError("N must be an integer in 1..256")
    return n


def _fraction(x: F, name: str) -> F:
    if type(x) is not F:
        raise FactorialHologramError(f"{name} must be a Fraction")
    return x


def legendre_exponent(n: int, p: int) -> int:
    """Exact v_p(n!) by repeated floor division; validates actual prime p."""
    n = _horizon(n)
    if not prime(p):
        raise FactorialHologramError("Legendre source must be an actual prime")
    exponent = 0
    while n:
        n //= p
        exponent += n
    return exponent


@dataclass(frozen=True)
class PrimePowerWindow:
    prime: int
    depth: int

    def __post_init__(self) -> None:
        if not prime(self.prime) or type(self.depth) is not int or self.depth < 2:
            raise FactorialHologramError("actual prime and repeated depth >=2 required")

    @property
    def half_width(self) -> F:
        return F(1, 2*self.prime**self.depth)


def windows(n: int) -> tuple[PrimePowerWindow, ...]:
    """p^k labels with 2<=k<=v_p(N!), ordered by actual p and k."""
    n = _horizon(n)
    return tuple(PrimePowerWindow(p, k)
                 for p in range(2, n+1) if prime(p)
                 for k in range(2, legendre_exponent(n, p)+1))


def increment_windows(n: int) -> tuple[PrimePowerWindow, ...]:
    """All newly created repeated-prime windows in the N-1 -> N SUCC step."""
    n = _horizon(n)
    if n == 1:
        return ()
    return tuple(PrimePowerWindow(p,k)
                 for p in range(2,n+1) if prime(p)
                 for k in range(max(2,legendre_exponent(n-1,p)+1),
                                legendre_exponent(n,p)+1))


def repeated_width_sum(n: int) -> F:
    """Sum 1/p^k (twice half-width); uniformly <11/12<1."""
    return sum((2*w.half_width for w in windows(n)), F())


def plateau_radius(n: int) -> F:
    """B_N(x)=1 for |x| <= plateau_radius, positive uniform lower bound >1/24."""
    return (F(1)-repeated_width_sum(n))/2


def support_radius(n: int) -> F:
    """B_N(x)=0 for |x|>=support_radius, and support_radius<1."""
    return (F(1)+repeated_width_sum(n))/2


def kernel_variance(n: int) -> F:
    """Exact variance of U_(1/2)*prod U_(1/(2p^k))."""
    return (F(1)+sum(((2*w.half_width)**2 for w in windows(n)),F()))/12


def variance_increment(n: int) -> F:
    """Exactly zero iff N is prime (for N>=2); no primality speedup."""
    n = _horizon(n)
    if n < 2:
        raise FactorialHologramError("increment requires a SUCC step N>=2")
    inc = sum(((2*w.half_width)**2 for w in increment_windows(n)),F())/12
    assert inc == kernel_variance(n)-kernel_variance(n-1)
    return inc


def spectral_power_sum(n: int, order: int) -> F:
    """Power sums of squared sinc widths: sum_j a_j^(2*order)."""
    _horizon(n)
    if type(order) is not int or not 1<=order<=32:
        raise FactorialHologramError("moment order must be integer 1..32")
    return F(1,2)**(2*order)+sum(
        (w.half_width**(2*order) for w in windows(n)),F())


def reconstructed_sinc_polynomial(n: int, max_factors: int = 12) -> tuple[F, ...]:
    """Recover all finite squared window widths from their power sums.

    If t_j = a_j^2, Newton's identities determine prod_j(z-t_j).
    Nonzero coefficients of log Fourier sinc supply the power sums, so
    the full local Fourier germ recovers widths despite identical Z samples.
    This does not prove that one measured off-grid point determines N.
    """
    n = _horizon(n)
    m = len(windows(n))+1
    if type(max_factors) is not int or m > max_factors or m > 32:
        raise FactorialHologramError("finite Newton reconstruction budget exceeded")
    p = [F()] + [spectral_power_sum(n,k) for k in range(1,m+1)]
    e = [F(1)]
    for j in range(1,m+1):
        e.append(sum(((-1)**(k-1)*e[j-k]*p[k]
                      for k in range(1,j+1)),F())/j)
    return tuple([F(1)]+[(-1)**j*e[j] for j in range(1,m+1)])




def infinite_tail_budget(n: int) -> F:
    """Certified upper bound on SUM of missing 1/p^k widths beyond N!.

    For p<=N, omitted k start at v_p(N!)+1 and sum to
    1/[p^v(p-1)]. For p>N, sum_{k>=2}p^-k <=1/[p(p-1)],
    which is bounded by the integer telescoping tail 1/N.

    For N>=4, ||B_infinity-B_N||_infty <= 2*infinite_tail_budget(N)
    by a uniform 4-Lipschitz bound (the 2^-2 box halfwidth 1/8).
    """
    n = _horizon(n)
    return (sum((F(1, (p-1)*p**legendre_exponent(n,p))
                 for p in range(2,n+1) if prime(p)), F()) + F(1,n))


def spline_density(widths: tuple[F, ...], x: F) -> F:
    """Exact generalized Irwin--Hall PDF by signed subset inclusion-exclusion.

    Independent implementation from the upstream CDF used by kernel_at.
    This oracle is exponential and restricted to <=12 nonzero widths.
    """
    if (type(widths) is not tuple or not 2 <= len(widths) <= 12
        or any(type(w) is not F or w<=0 for w in widths)):
        raise FactorialHologramError("2..12 positive Fraction widths required")
    _fraction(x, "spline point")
    m = len(widths)
    h = sum(widths,F())
    signed = F()
    for mask in range(1<<m):
        z = x+h-2*sum((widths[j] for j in range(m)
                         if (mask>>j)&1),F())
        signed += (-1 if mask.bit_count()%2 else 1)*max(F(),z)**(m-1)
    result = signed/(2**m*factorial(m-1)*prod(widths))
    if result<0:
        raise AssertionError("B-spline signed count unexpectedly negative")
    return result


def exact_continuous_gram(n: int) -> dict[str,F]:
    """Two nonzero Gram diagonals for cardinal translates in L²(R).

    g_j = int B_N(x)B_N(x-j) dx = (B_N*B_N)(j).
    Since support(B_N) subset (-1,1), g_j=0 when |j|>=2.
    The partition-of-unity identity gives g0+2*g1=1.
    IMPORTANT: g1>0 for N>=4, so the cardinal lift is NOT an
    orthogonal/Weil-positive Hilbert identification.
    """
    n = _horizon(n)
    w = (F(1,2),)+tuple(item.half_width for item in windows(n))
    if len(w)*2>12:
        raise FactorialHologramError("double convolution exceeds 12-width budget")
    full = w+w
    diag = spline_density(full,F())
    adj = spline_density(full,F(1))
    if diag+2*adj != F(1) or adj<0:
        raise AssertionError("cardinal partition Gram identity failed")
    lower = diag-2*adj
    if lower < 1-repeated_width_sum(n):
        raise AssertionError("uniform core-island Riesz bound failed")
    return {"diagonal":diag,"adjacent":adj,"min_symbol":lower,
            "certified_lower":1-repeated_width_sum(n)}


def partition_unity_at(n: int, x: F) -> F:
    """Exact finite support version of sum_m B_N(x-m)=1."""
    n = _horizon(n)
    x = _fraction(x,"query point")
    m = x.numerator//x.denominator
    result = sum((kernel_at(n,x-F(k)) for k in range(m-1,m+3)),F())
    if result != F(1):
        raise AssertionError("integer translates do not partition unity")
    return result

def kernel_at(n: int, x: F) -> F:
    """Exact cardinal kernel density at a rational point.

    The base U[-1/2,1/2] is convolved with nonempty smooth windows for
    N>=4. At N<=3, the box representative uses half-value at endpoints.
    Analytic plateau and support bounds are checked BEFORE the exponential
    finite CDF evaluation, allowing exact integer samples for every N.
    """
    n = _horizon(n)
    x = _fraction(x,"query point")
    a = abs(x)
    flat = plateau_radius(n)
    if a < flat:
        return F(1)
    if a > support_radius(n):
        return F()
    w = windows(n)
    if not w:
        return F(1,2) if a == F(1,2) else F(int(a<F(1,2)))
    if len(w) > MAX_OFF_GRID_WINDOWS:
        raise FactorialHologramError("off-grid CDF needs <=11 repeated windows")
    widths = tuple(item.half_width for item in w)
    result = (uniform_sum_cdf(widths,x+F(1,2))-
              uniform_sum_cdf(widths,x-F(1,2)))
    if not F()<=result<=F(1):
        raise AssertionError("convolution density violates normalized uniform bound")
    return result


def interpolant(n: int, coefficients: tuple[tuple[int,F], ...], x: F) -> F:
    """I_N(c)(x)=sum_m c_m B_N(x-m), finitely supported cardinal lift."""
    _horizon(n)
    x = _fraction(x,"query point")
    if (type(coefficients) is not tuple or
        any(type(m) is not int or type(c) is not F for m,c in coefficients)
        or len({m for m,_ in coefficients}) != len(coefficients)):
        raise FactorialHologramError("unique integer sites with Fraction coefficients")
    return sum((c*kernel_at(n,x-m) for m,c in coefficients),F())


def source_clock_gate(site: int, p: int, kind: str) -> bool:
    """Authentic integer q-clock gate, including negative SUCC addresses."""
    if type(site) is not int or not prime(p) or kind not in (
            "one", "minus_one", "nonzero"):
        raise FactorialHologramError("integer site and actual prime phase source needed")
    residue = site % p
    return {"one":residue==1, "minus_one":residue==p-1,
            "nonzero":residue!=0}[kind]


def lifted_prime_gate(n: int, coefficients: tuple[tuple[int,F], ...],
                      p: int, kind: str, x: F) -> F:
    """I_N P_{p,kind} c: authenticate integer residues BEFORE lifting."""
    if not prime(p) or kind not in ("one","minus_one","nonzero"):
        raise FactorialHologramError("genuine prime and correct clock gate required")
    if type(coefficients) is not tuple or any(type(m) is not int or type(c) is not F
                                               for m,c in coefficients):
        raise FactorialHologramError("malformed source sequence")
    return interpolant(n,tuple((m,c) for m,c in coefficients
                               if source_clock_gate(m,p,kind)),x)


def poisson_wheel_polynomial(start: int, gates: tuple[tuple[int,str],...],
                             t: F, degree: int) -> tuple[F,F]:
    """P_M(t)=sum_{k<=M} t^k/k! 1_{start+k passes every clock}.

    The actual Poissonized probability equals exp(-t)*infinite sum,
    with truncation error <=t^(M+1)/(M+1)! for t>=0 by the
    Poisson factorial-moment bound. Unlike the Borwein 1/m! from simplex
    volume, this 1/k! counts ordered SUCC jump times.
    """
    if type(start) is not int or type(gates) is not tuple or not gates:
        raise FactorialHologramError("integer starting point, nonempty clock-gate tuple")
    if (len({p for p,_ in gates})!=len(gates)
        or any(not prime(p) or kind not in ("one","minus_one","nonzero")
               for p,kind in gates)):
        raise FactorialHologramError("distinct genuine prime gates required")
    _fraction(t,"Poisson time")
    if t<0 or type(degree) is not int or not 0<=degree<=MAX_POISSON_DEGREE:
        raise FactorialHologramError("nonnegative time and degree 0..80 required")
    poly = sum((t**k/factorial(k) for k in range(degree+1)
                if all(source_clock_gate(start+k,p,kind) for p,kind in gates)),F())
    return poly,t**(degree+1)/factorial(degree+1)
