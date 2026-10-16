"""Exact Tate local Fourier/Mellin normalization and conductor-probe laboratory.

All evaluations are of declared Q_p test functions and exact rational/algebraic
quantities. Theorems are classical local Tate theory, NOT RH positivity, an
adelic global proof, or an authenticated physical observer. No zero data.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .all_places_zeta import place_primes, PlaceModelError


class TateContractError(ValueError):
    """Missing valid prime, test-function chart, character, or domain."""


def _integer(n: int, *, lo: int | None = None) -> int:
    if type(n) is not int or (lo is not None and n < lo):
        raise TateContractError("Exact integer in declared domain required")
    return n


def _place(p: int) -> int:
    try:
        place_primes((p,))
    except (PlaceModelError, TypeError) as exc:
        raise TateContractError("A local place must be a genuine rational prime") from exc
    return p


def _sign_power(omega: int, n: int) -> int:
    if type(omega) is not int or omega not in (-1, 1):
        raise TateContractError("This exact local chart supports omega=+/-1 only")
    return omega if n % 2 else 1


@dataclass(frozen=True)
class UnramifiedTatePair:
    p: int
    ball_exponent: int
    sigma: int
    omega: int
    zeta: Q
    dual_zeta: Q
    forward_over_dual: Q
    inverse_tate_gamma: Q


def unramified_ball_pair(p: int, ball_exponent: int, sigma: int,
                          omega: int = 1) -> UnramifiedTatePair:
    """Compute Z_p(s,1_{p^a Z_p},chi) and Z_p(1-s,Fphi,chi^-1).

    psi_p(x)=exp(2pi i {x}_p), dx(Z_p)=1, d*x(Z_p^*)=1,
    Fphi(y)=p^-a 1_{p^-a Z_p}(y), chi(p)=omega in {+1,-1}.
    sigma>=2 integer keeps both meromorphic expressions finite and rational.
    The ratio Z(s)/Z(1-s) is the *inverse* of a common Tate gamma convention.
    """
    _place(p)
    a = _integer(ball_exponent)
    s = _integer(sigma, lo=2)
    phase = _sign_power(omega, a)
    common = phase * Q(p) ** (-a * s)
    zeta = common / (1 - omega * Q(p) ** (-s))
    dual = common / (1 - omega * Q(p) ** (s - 1))
    ratio = Q(1 - omega * Q(p) ** (s - 1),
              1 - omega * Q(p) ** (-s))
    assert zeta == ratio * dual
    return UnramifiedTatePair(p, a, s, omega, zeta, dual,
                              ratio, 1 / ratio)


def chi_mod3(n: int) -> int:
    """Primitive odd quadratic Dirichlet character mod 3, extended by zero."""
    _integer(n)
    return 0 if n % 3 == 0 else (1 if n % 3 == 1 else -1)


@dataclass(frozen=True)
class QRootMinus3:
    """a+b*delta, delta^2=-3; exact arithmetic in Q(sqrt(-3))."""
    a: Q
    b: Q = Q(0)

    def __post_init__(self):
        if type(self.a) not in (int, Q) or type(self.b) not in (int, Q):
            raise TateContractError("Exact rationals only in conductor-one cyclotomic ring")
        object.__setattr__(self, "a", Q(self.a))
        object.__setattr__(self, "b", Q(self.b))

    @staticmethod
    def of(x: QRootMinus3 | int | Q) -> QRootMinus3:
        return x if isinstance(x, QRootMinus3) else QRootMinus3(x)

    def __add__(self, other):
        other = self.of(other)
        return QRootMinus3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return QRootMinus3(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.of(other)

    def __mul__(self, other):
        other = self.of(other)
        return QRootMinus3(self.a * other.a - 3 * self.b * other.b,
                           self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def conjugate(self):
        return QRootMinus3(self.a, -self.b)

    def norm(self) -> Q:
        return self.a * self.a + 3 * self.b * self.b

    def __truediv__(self, other):
        other = self.of(other)
        if not other.norm():
            raise ZeroDivisionError("zero algebraic divisor")
        top = self * other.conjugate()
        return QRootMinus3(top.a / other.norm(), top.b / other.norm())

    def __rtruediv__(self, other):
        return self.of(other) / self

    def __pow__(self, exponent: int):
        _integer(exponent, lo=0)
        result, base, n = QRootMinus3(1), self, exponent
        while n:
            if n % 2:
                result = result * base
            base = base * base
            n //= 2
        return result


DELTA = QRootMinus3(0, 1)
ZETA3 = QRootMinus3(Q(-1, 2), Q(1, 2))  # exp(+2pi i/3)


def gauss_sum_mod3(unit: int) -> QRootMinus3:
    """sum_{v=1,2} chi_3(v) * exp(2pi i unit*v/3), exact."""
    _integer(unit)
    if not chi_mod3(unit):
        raise TateContractError("Only unit cosets modulo the ramified place 3")
    return sum((chi_mod3(v) * ZETA3 ** ((unit * v) % 3)
                for v in (1, 2)), QRootMinus3(0))


@dataclass(frozen=True)
class RamifiedTatePair:
    unit: int
    sigma: int
    zeta: Q
    dual_zeta: QRootMinus3
    forward_over_dual: QRootMinus3


def ramified_mod3_coset_pair(unit: int, sigma: int) -> RamifiedTatePair:
    """p=3, primitive chi_3, phi=1_{unit+3Z_3}, exact local Tate pair.

    At conductor one, Fphi(y)=(1/3) psi_3(unit*y) 1_{3^-1 Z_3}(y).
    d*x assigns each unit residue coset mass 1/2. Only valuation -1
    survives in the twisted dual integral; integral is algebraic, not float.
    """
    _integer(unit)
    s = _integer(sigma, lo=2)
    if not chi_mod3(unit):
        raise TateContractError("Residue must be a unit modulo 3")
    zeta = Q(chi_mod3(unit), 2)
    dual = gauss_sum_mod3(unit) * Q(1, 2 * 3**s)
    ratio = QRootMinus3(zeta) / dual
    assert ratio == QRootMinus3(0, -3 ** (s - 1))
    return RamifiedTatePair(unit % 3, s, zeta, dual, ratio)


def coarse_ramified_unit_zeta() -> Q:
    """Z(s,1_{Z_3^*},chi_3)=0 for every s, by exact unit orthogonality."""
    return Q(chi_mod3(1) + chi_mod3(2), 2)


def finite_twisted_log_jets(primes: tuple[int, ...],
                            depth: int, sigma: int,
                            character: str = "trivial") -> dict[int, Q]:
    """Exact coefficients of log(p) in -L'/L at finite prime-power depth.

    Each p supplies sum_{k=1}^depth chi(p)^k p^(-k*sigma).
    Ramified chi_3 at p=3 has NO Euler local factor. This does not
    analytically continue a truncated Euler product or assert positivity.
    """
    try:
        ps = place_primes(primes)
    except (PlaceModelError, TypeError) as exc:
        raise TateContractError("Distinct ordered genuine prime places required") from exc
    d, s = _integer(depth, lo=1), _integer(sigma, lo=2)
    if d > 24:
        raise TateContractError("Exact finite jet budget depth<=24")
    if character not in ("trivial", "chi3"):
        raise TateContractError("Source character must be declared")
    out = {}
    for p in ps:
        omega = 1 if character == "trivial" else chi_mod3(p)
        if omega:
            out[p] = sum((Q(_sign_power(omega, k), p ** (k * s))
                          for k in range(1, d + 1)), Q(0))
    return out


def fake_composite_local_factor(sigma: int) -> tuple[Q, Q]:
    """Exhibit fake 6-adic Euler place != two genuine p=2,3 places."""
    s = _integer(sigma, lo=2)
    fake = 1 / (1 - Q(6)**(-s))
    actual = 1 / ((1 - Q(2)**(-s)) * (1 - Q(3)**(-s)))
    return fake, actual


def symmetric_offline_mutant(s: int | Q) -> Q:
    """P(s)=1-(16/3)s(1-s): symmetric, P(0)=P(1)=1, zeros 1/4,3/4.

    A completed zeta multiplied by P retains FE and its 0/1 pole residues,
    but has off-critical zeros. It FAILS authentic Euler source identification.
    """
    if type(s) not in (int, Q):
        raise TateContractError("Exact rational analytic probe required")
    t = Q(s)
    return 1 - Q(16, 3) * t * (1 - t)


def _mp(dps: int):
    _integer(dps, lo=30)
    if dps > 200:
        raise TateContractError("Numerical calibration uses 30<=dps<=200")
    try:
        import mpmath as mp
    except ImportError as exc:
        raise TateContractError("mpmath research extra required") from exc
    mp.mp.dps = dps
    return mp


def chi3_odd_theta(t: int | Q, terms: int, dps: int = 70):
    """Finite theta_3(t)=2*sum_{n>=1} n chi_3(n) exp(-pi*n^2*t/3).

    The Poisson identity theta_3(t)=t^(-3/2)theta_3(1/t) is CLASSICAL;
    this evaluation is a numerical calibration, not its independent proof.
    """
    if type(t) not in (int, Q) or Q(t) <= 0:
        raise TateContractError("Theta heat time must be an exact positive rational")
    N = _integer(terms, lo=1)
    mp = _mp(dps)
    tval = mp.mpf(Q(t).numerator) / Q(t).denominator
    return 2 * mp.fsum(n*chi_mod3(n)*mp.exp(-mp.pi*n*n*tval/3)
                       for n in range(1, N + 1))


def chi3_completed_theta(s, terms: int, dps: int = 70):
    """Zero-independent two-chart analytic completion of primitive chi_{-3}.

    Lambda_chi(s)=sum_{n>=1} n*chi_3(n) * (
       a_n^(-(s+1)/2) Gamma((s+1)/2,a_n)
      +a_n^(-(2-s)/2) Gamma((2-s)/2,a_n)), a_n=pi*n^2/3.

    The full equality with Gamma_R(s+1)L(s,chi) is a CLASSICAL consequence
    of conductor-3 Poisson summation + Mellin transform. At finite N the sum
    is entire and exactly symmetric in s<->1-s by construction, which alone
    does NOT identify the arithmetic source or prove a Weil sign inequality.
    """
    N = _integer(terms, lo=1)
    mp = _mp(dps)
    if type(s) is bool:
        raise TateContractError("Boolean is not a complex Mellin argument")
    ss = mp.mpc(s)
    u, v = (ss + 1) / 2, (2 - ss) / 2
    result = []
    for n in range(1, N + 1):
        c = chi_mod3(n)
        if not c:
            continue
        a = mp.pi*n*n/3
        result.append(n*c*(mp.power(a, -u)*mp.gammainc(u, a, mp.inf)
                           + mp.power(a, -v)*mp.gammainc(v, a, mp.inf)))
    return mp.fsum(result)


def chi3_strip_tail_rational(terms: int, taylor_order: int = 40) -> Q:
    """Rigorous source tail bound on 0<=Re(s)<=1, all Im(s).

    |Lambda_chi(s)-Lambda_chi,N(s)| <= exp(-N^2)/N^2
    <= 1/[N^2 sum_{k=0}^K (N^2)^k/k!].
    This follows from the full classical theta/Mellin identity, pi/3>=1,
    and a monotone integral majorant; it is NOT float/interval arithmetic.
    """
    from math import factorial
    n = _integer(terms, lo=1)
    kmax = _integer(taylor_order, lo=0)
    if kmax > 160:
        raise TateContractError("Rational bound budget taylor_order<=160")
    lower_exp = sum((Q(n**(2*k), factorial(k)) for k in range(kmax+1)), Q(0))
    return 1 / (n*n*lower_exp)
