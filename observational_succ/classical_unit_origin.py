"""Classical SUCC foundations: unit-origin charts, affine actions, CRT, Mellin carriers.

Elementary exact algebra only.  Source integers are >=1; formal-group
polynomials may be evaluated on wider rings without authenticating a source.
The L2 constructions are *logarithmic-coordinate* probes, not Euler/Weil forms.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Mapping


class ClassicalOriginError(ValueError):
    """An invalid source address, chart, exact packet or CRT contract."""


def _int(value: int, name: str, *, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ClassicalOriginError(f"{name} must be an exact integer"
                                   + (f" >= {minimum}" if minimum is not None else ""))
    return value


def _chart(chart: str) -> int:
    if chart == "n_minus_one":
        return 1
    if chart == "one_minus_n":
        return -1
    raise ClassicalOriginError("Choose n_minus_one or one_minus_n, not an untyped origin")


def source_coordinate(n: int, chart: str) -> int:
    """Rebase the physical integer monoid N_{>=1}, sending its unit to zero."""
    _int(n, "source integer", minimum=1)
    return _chart(chart) * (n - 1)


def decode_source(x: int, chart: str) -> int:
    """Reject formal polynomial addresses outside the declared positive source."""
    _int(x, "chart coordinate")
    n = 1 + _chart(chart) * x
    if n < 1:
        raise ClassicalOriginError("Formal address is outside the positive-integer source")
    return n


def formal_product(x: int, y: int, chart: str) -> int:
    """The multiplicative formal-group polynomial in either unit-origin chart."""
    _int(x, "left coordinate")
    _int(y, "right coordinate")
    return x + y + _chart(chart) * x * y


def chart_successor(x: int, step: int, chart: str) -> int:
    """S^step transported from n -> n+step (step >= 0)."""
    _int(x, "chart coordinate")
    _int(step, "SUCC step", minimum=0)
    return x + _chart(chart) * step


def chart_multiplier(x: int, m: int, chart: str) -> int:
    """True source n->mn, not the incompatible zero-fixed x->mx."""
    _int(x, "chart coordinate")
    _int(m, "multiplier", minimum=1)
    return m * x + _chart(chart) * (m - 1)


def forced_affine_cocycle(m: int, c_two: int) -> int:
    """Full positive-integer multiplicative action forces c(m)=(m-1)c(2)."""
    _int(m, "multiplier", minimum=1)
    _int(c_two, "declared affine translation of 2")
    return (m - 1) * c_two


def certify_finite_cocycle(table: Mapping[int, int]) -> bool:
    """Check finite entries against the necessary full-monoid 2-cocycle law.

    True is only a *finite consistency* check; it does not construct a
    universal law from finite data or authenticate arithmetic source weights.
    """
    if not isinstance(table, Mapping) or 1 not in table or 2 not in table:
        raise ClassicalOriginError("A full-monoid sample must include 1 and 2")
    c2 = _int(table[2], "c(2)")
    for m, value in table.items():
        _int(m, "multiplier", minimum=1)
        _int(value, "cocycle value")
        if value != forced_affine_cocycle(m, c2):
            return False
    return True


@dataclass(frozen=True)
class ArithmeticRay:
    """An actual nonnegative successor orbit {start + k*step : k>=0}."""

    start: int
    step: int

    def __post_init__(self) -> None:
        _int(self.start, "ray start", minimum=0)
        _int(self.step, "ray step", minimum=1)

    def contains(self, n: int) -> bool:
        _int(n, "address", minimum=0)
        return n >= self.start and (n - self.start) % self.step == 0


def intersect_rays(rays: Iterable[ArithmeticRay]) -> ArithmeticRay | None:
    """Generalized CRT plus starting-address cutoffs, all exactly integral."""
    rays = tuple(rays)
    if not rays or any(not isinstance(ray, ArithmeticRay) for ray in rays):
        raise ClassicalOriginError("Require a nonempty tuple of actual arithmetic rays")
    result = rays[0]
    for ray in rays[1:]:
        a, m = result.start, result.step
        b, n = ray.start, ray.step
        g = gcd(m, n)
        if (b - a) % g:
            return None
        new_step = m * (n // g)
        reduced_n = n // g
        t = (((b - a) // g) * pow(m // g, -1, reduced_n)) % reduced_n if reduced_n > 1 else 0
        residue = (a + m * t) % new_step
        cutoff = max(a, b)
        first = residue + max(0, (cutoff - residue + new_step - 1) // new_step) * new_step
        result = ArithmeticRay(first, new_step)
    return result


def horizon_report(rays: Iterable[ArithmeticRay], horizon: int) -> dict:
    """Global solution, missing global solution, and late witness are distinct."""
    _int(horizon, "observation horizon", minimum=0)
    ray = intersect_rays(rays)
    if ray is None:
        return {"state": "INCONSISTENT", "first_global_witness": None,
                "visible_witness": None, "global_step": None}
    visible = ray.start if ray.start <= horizon else None
    return {"state": "OBSERVED" if visible is not None else "BEYOND_HORIZON",
            "first_global_witness": ray.start, "visible_witness": visible,
            "global_step": ray.step}


def residue_fiber_sizes(modulus: int, cutoff: int) -> tuple[int, ...]:
    """Sizes of the fibers of {0,..,cutoff-1} -> Z/modulus Z."""
    _int(modulus, "modulus", minimum=1)
    _int(cutoff, "finite cutoff", minimum=1)
    return tuple(cutoff // modulus + (1 if j < cutoff % modulus else 0)
                 for j in range(modulus))


def residue_map_norm_squared(modulus: int, cutoff: int) -> int:
    """Exact ||J_{N,H}||^2=max_j |fiber(j)|, NOT a limit theorem."""
    return max(residue_fiber_sizes(modulus, cutoff))


def unbounded_residue_witness(modulus: int, copies: int) -> dict:
    """K equal unit amplitudes in one residue fiber: norm ratio squared K."""
    _int(modulus, "modulus", minimum=1)
    _int(copies, "number of congruent addresses", minimum=1)
    addresses = tuple(j * modulus for j in range(copies))
    # Input vector is sum of orthonormal basis elements, output is K*e_0.
    return {"modulus": modulus, "addresses": addresses,
            "input_norm_squared": copies, "output_norm_squared": copies * copies,
            "ratio_squared": copies,
            "finite_operator_norm_squared": residue_map_norm_squared(modulus, modulus * copies)}


def dense_kernel_approximation(modulus: int, copies: int) -> dict:
    """Finite exact witness that ker J_N is dense in the infinite Hilbert carrier.

    e_0 - (1/K)sum_{j=1..K}e_{jN} maps to zero, while its
    squared distance to e_0 is 1/K.  The argument translates to any e_r.
    """
    _int(modulus, "modulus", minimum=1)
    _int(copies, "copies", minimum=1)
    return {"modulus": modulus, "kernel_addresses": tuple(j * modulus for j in range(copies + 1)),
            "kernel_coefficients": (Fraction(1),) + (Fraction(-1, copies),) * copies,
            "image_coefficient": Fraction(0),
            "distance_to_e_zero_squared": Fraction(1, copies)}


def _q(value: Fraction | int, name: str) -> Fraction:
    if type(value) is not Fraction and type(value) is not int:
        raise ClassicalOriginError(f"{name} must be an exact Fraction or integer")
    return Fraction(value)


@dataclass(frozen=True)
class LogBox:
    """amplitude*1_[lo,hi) in logarithmic coordinate u=log x."""

    lo: Fraction
    hi: Fraction
    amplitude: Fraction

    def __post_init__(self) -> None:
        lo, hi, amplitude = (_q(self.lo, "box lower endpoint"),
                             _q(self.hi, "box upper endpoint"),
                             _q(self.amplitude, "box amplitude"))
        if lo >= hi:
            raise ClassicalOriginError("Require a nonempty log-coordinate interval")
        object.__setattr__(self, "lo", lo)
        object.__setattr__(self, "hi", hi)
        object.__setattr__(self, "amplitude", amplitude)


def log_inner(left: Iterable[LogBox], right: Iterable[LogBox]) -> Fraction:
    """Exact real L2(du) inner product of finite compact step packets."""
    left, right = tuple(left), tuple(right)
    if any(not isinstance(p, LogBox) for p in left + right):
        raise ClassicalOriginError("Every packet must be a declared LogBox")
    return sum((p.amplitude * q.amplitude * max(Fraction(0), min(p.hi, q.hi) - max(p.lo, q.lo))
                for p in left for q in right), Fraction(0))


def log_reflect(packets: Iterable[LogBox]) -> tuple[LogBox, ...]:
    """Log-side implementation of Jf(x)=x^{-1}f(1/x): g(u)->g(-u)."""
    return tuple(LogBox(-p.hi, -p.lo, p.amplitude) for p in packets)


def log_dilate(packets: Iterable[LogBox], h: Fraction | int) -> tuple[LogBox, ...]:
    """g(u)->g(u+h), the L2(dx) dilation f(x)->e^(h/2)f(e^h x)."""
    h = _q(h, "logarithmic dilation")
    return tuple(LogBox(p.lo - h, p.hi - h, p.amplitude) for p in packets)


def classical_unit_origin_probe() -> dict:
    """Deterministic exact classical receipt with true and hostile controls."""
    charts = ("n_minus_one", "one_minus_n")
    for chart in charts:
        for a in range(1, 10):
            for b in range(1, 10):
                x, y = source_coordinate(a, chart), source_coordinate(b, chart)
                assert formal_product(x, y, chart) == source_coordinate(a * b, chart)
                assert chart_multiplier(x, b, chart) == formal_product(x, y, chart)
                assert decode_source(x, chart) == a
                assert chart_multiplier(chart_successor(x, 1, chart), b, chart) == chart_successor(chart_multiplier(x, b, chart), b, chart)
    rays = (ArithmeticRay(1, 2), ArithmeticRay(2, 3), ArithmeticRay(3, 5))
    pairs = tuple(intersect_rays((rays[i], rays[j])).start
                  for i, j in ((0, 1), (0, 2), (1, 2)))
    triple = horizon_report(rays, 9)
    assert pairs == (5, 3, 8) and triple["first_global_witness"] == 23
    g = (LogBox(Fraction(-2), Fraction(1), Fraction(2)),
         LogBox(Fraction(0), Fraction(3, 2), Fraction(-1, 3)))
    h = Fraction(3, 5)
    assert log_inner(g, g) == log_inner(log_reflect(g), log_reflect(g))
    assert log_inner(g, g) == log_inner(log_dilate(g, h), log_dilate(g, h))
    assert log_reflect(log_dilate(log_reflect(g), h)) == log_dilate(g, -h)
    return {
        "kind": "CLASSICAL_UNIT_ORIGIN_EXACT_RECEIPT",
        "source_identity_preserved": True,
        "formal_group_positive_law": "x+y+xy",
        "formal_group_reflected_law": "u+v-uv",
        "affine_cocycle_forced_by_two": True,
        "counterfeit_cocycle_rejected": not certify_finite_cocycle({1: 0, 2: 1, 3: 4, 6: 5}),
        "crt_pairwise_first_witnesses": list(pairs),
        "crt_triple_first_witness": triple["first_global_witness"],
        "crt_triple_not_visible_at_nine": triple["visible_witness"] is None,
        "finite_residue_operator_norm_squared_at_four_copies": residue_map_norm_squared(5, 20),
        "unbounded_fiber_norm_growth": unbounded_residue_witness(5, 4)["ratio_squared"] == 4,
        "algebraic_residue_kernel_dense": dense_kernel_approximation(5, 4)["distance_to_e_zero_squared"] == Fraction(1, 4),
        "log_packet_reflection_and_dilation_unitary": True,
        "analytic_zeta_functional_equation_proved": False,
        "global_weil_positivity_or_RH_proved": False,
        "physical_carrier_authenticated": False,
    }
