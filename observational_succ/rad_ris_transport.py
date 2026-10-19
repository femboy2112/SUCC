"""Finite exact RAD/RIS arithmetic and prime/successor probes.

This is a bounded, source-free arithmetic chart, not an observer's unobserved
source data, an ABC theorem, a Weil-positive form, or a model of electric current.
Mathematical propositions have unrestricted positive-integer domains in the
accompanying dossier; runtime caps are resource guards, not theorem hypotheses.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, prod

MAX_INTEGER = 1_000_000
MAX_CRT_MODULUS = 200_000
MAX_CRT_CLASSES = 4_096


class RadRisError(ValueError):
    """Malformed arithmetic source, nonprime action, or exceeded finite cap."""


def _bounded_positive(n: int, label: str, upper: int = MAX_INTEGER) -> int:
    if type(n) is not int or not 1 <= n <= upper:
        raise RadRisError(f"{label}: integer in 1..{upper} required (bool rejected)")
    return n


def prime_powers(n: int) -> tuple[tuple[int, int], ...]:
    """Trial factorization, deliberately bounded and independently checkable."""
    m = _bounded_positive(n, "factorization input")
    factors = []
    p = 2
    while p * p <= m:
        if m % p == 0:
            exponent = 0
            while m % p == 0:
                m //= p
                exponent += 1
            factors.append((p, exponent))
        p = 3 if p == 2 else p + 2
    if m > 1:
        factors.append((m, 1))
    return tuple(factors)


def is_prime(p: int) -> bool:
    return type(p) is int and 2 <= p <= MAX_INTEGER and prime_powers(p) == ((p, 1),)


def rad(n: int) -> int:
    """Squarefree prime support product; rad(1)=1."""
    return prod(p for p, _ in prime_powers(n))


def ris(n: int) -> int:
    """Excess prime multiplicity; ris(1)=1."""
    return n // rad(n)


@dataclass(frozen=True)
class RadRis:
    """Canonical admissible pair (r,t), n=r*t, supp(t) subset supp(r)."""

    radical: int
    residual: int

    def __post_init__(self) -> None:
        _bounded_positive(self.radical, "radical")
        _bounded_positive(self.residual, "residual")
        _bounded_positive(self.radical * self.residual, "decoded integer")
        rf = prime_powers(self.radical)
        tf = prime_powers(self.residual)
        if any(exponent != 1 for _, exponent in rf):
            raise RadRisError("radical must be squarefree")
        if not {p for p, _ in tf}.issubset({p for p, _ in rf}):
            raise RadRisError("residual cannot introduce new prime support")

    @classmethod
    def from_integer(cls, n: int) -> RadRis:
        n = _bounded_positive(n, "input integer")
        return cls(rad(n), ris(n))

    @property
    def value(self) -> int:
        return self.radical * self.residual

    def multiply(self, other: RadRis) -> RadRis:
        if not isinstance(other, RadRis):
            raise RadRisError("multiplication requires another canonical pair")
        _bounded_positive(self.value * other.value, "product")
        overlap = gcd(self.radical, other.radical)
        return RadRis(self.radical * other.radical // overlap,
                      self.residual * other.residual * overlap)

    def prime_step(self, p: int) -> tuple[str, RadRis]:
        if not is_prime(p):
            raise RadRisError("FUCC generator must be a genuine bounded prime")
        _bounded_positive(self.value * p, "prime product")
        if self.radical % p:
            return "support", RadRis(self.radical * p, self.residual)
        return "multiplicity", RadRis(self.radical, self.residual * p)


def radical_layers(n: int) -> tuple[int, ...]:
    """Successive radicals of iterated RIS; omits the trailing unit layers."""
    factors = prime_powers(n)
    height = max((e for _, e in factors), default=0)
    return tuple(prod(p for p, e in factors if e > j) for j in range(height))


def from_radical_layers(layers: tuple[int, ...]) -> int:
    """Reconstruct a unique n from a finite nested squarefree chain."""
    if type(layers) is not tuple or len(layers) > 32:
        raise RadRisError("finite tuple of at most 32 layers required")
    if layers and layers[-1] == 1:
        raise RadRisError("trailing unit layers are not canonical")
    previous = None
    n = 1
    for layer in layers:
        _bounded_positive(layer, "layer")
        if layer == 1 or rad(layer) != layer:
            raise RadRisError("every retained layer must be nonunit squarefree")
        if previous is not None and previous % layer:
            raise RadRisError("support layers must be nested by divisibility")
        n *= layer
        _bounded_positive(n, "layer product")
        previous = layer
    return n


def successor_balance(n: int) -> tuple[int, int]:
    """Exact discrete product rule: t_n * delta(r) + r_(n+1) * delta(t) = 1."""
    n = _bounded_positive(n, "successor input", MAX_INTEGER - 1)
    current = RadRis.from_integer(n)
    next_state = RadRis.from_integer(n + 1)
    support_change = current.residual * (next_state.radical - current.radical)
    residual_change = next_state.radical * (next_state.residual - current.residual)
    assert support_change + residual_change == 1
    return support_change, residual_change


@dataclass(frozen=True)
class ABCSnapshot:
    """One primitive a+b=c triple: exact quality>1 decision, never global ABC."""

    a: int
    b: int
    c: int
    radical_a: int
    radical_b: int
    radical_c: int
    ris_c: int

    @property
    def radical_abc(self) -> int:
        return self.radical_a * self.radical_b * self.radical_c

    @property
    def quality_above_one(self) -> bool:
        return self.ris_c > self.radical_a * self.radical_b

    @property
    def excess_ratio(self) -> Fraction:
        return Fraction(self.ris_c, self.radical_a * self.radical_b)


def abc_snapshot(a: int, b: int) -> ABCSnapshot:
    a = _bounded_positive(a, "a")
    b = _bounded_positive(b, "b")
    c = _bounded_positive(a + b, "a+b")
    if gcd(a, b) != 1:
        raise RadRisError("ABC chart requires gcd(a,b)=1")
    return ABCSnapshot(a, b, c, rad(a), rad(b), rad(c), ris(c))


@dataclass(frozen=True)
class CRTSignature:
    """Exact positive-valuation conditions for n and n+1 at fixed primes."""

    modulus: int
    residues: tuple[int, ...]

    @property
    def density(self) -> Fraction:
        return Fraction(len(self.residues), self.modulus)

    def matches(self, n: int) -> bool:
        return _bounded_positive(n, "CRT target") % self.modulus in self.residues

    def count_up_to(self, n: int) -> int:
        n = _bounded_positive(n, "counting horizon")
        whole, remainder = divmod(n, self.modulus)
        return whole * len(self.residues) + sum(1 <= r <= remainder for r in self.residues)


def crt_successor_valuations(left: Mapping[int, int], right: Mapping[int, int]) -> CRTSignature:
    """CRT classes with exact v_p(n)=e, v_q(n+1)=f for specified e,f>=1.

    Left/right prime sets must be disjoint. Does not assert that unspecified
    primes are absent from either endpoint. Uses no probabilistic oracle.
    """
    if not isinstance(left, Mapping) or not isinstance(right, Mapping):
        raise RadRisError("prime-valuation dictionaries required")
    if set(left).intersection(right):
        raise RadRisError("a prime cannot divide both consecutive endpoints")
    specification = []
    for side, values in (("left", left), ("right", right)):
        for p, exponent in values.items():
            if not is_prime(p) or type(exponent) is not int or not 1 <= exponent <= 16:
                raise RadRisError("prime keys and positive exponents <=16 required")
            specification.append((p, exponent, side))
    modulus = 1
    residues = (0,)
    for p, exponent, side in sorted(specification):
        local_modulus = p ** (exponent + 1)
        if modulus * local_modulus > MAX_CRT_MODULUS:
            raise RadRisError("CRT finite modulus budget exceeded")
        if len(residues) * (p - 1) > MAX_CRT_CLASSES:
            raise RadRisError("CRT finite class budget exceeded")
        local_base = p ** exponent
        local_residues = tuple((local_base * u - (side == "right")) % local_modulus
                               for u in range(1, p))
        inv = pow(modulus, -1, local_modulus)
        new_modulus = modulus * local_modulus
        residues = tuple(sorted((r + modulus * (((a - r) * inv) % local_modulus))
                                % new_modulus
                                for r in residues for a in local_residues))
        modulus = new_modulus
    return CRTSignature(modulus, residues)


def prime_window_successor_witness(primes: tuple[int, ...], outsider: int) -> tuple[int, int]:
    """Construct a finite-P observer indistinguishability witness by CRT.

    Both positive inputs have v_p=0 at every listed p; precisely one successor
    is divisible by outsider. The finite cap limits runtime, not the theorem.
    """
    if type(primes) is not tuple or len(primes) > 128 or primes != tuple(sorted(set(primes))):
        raise RadRisError("finite sorted distinct prime window required")
    if not all(is_prime(p) for p in primes) or not is_prime(outsider) or outsider in primes:
        raise RadRisError("genuine distinct observed and unseen primes required")
    product = prod(primes)
    _bounded_positive(product * outsider, "CRT witness modulus")
    inverse = pow(product, -1, outsider)

    def solve(residue: int) -> int:
        n = (1 + product * (((residue - 1) * inverse) % outsider)) % (product * outsider)
        return n if n else product * outsider

    hit, miss = solve(outsider - 1), solve(0)
    assert all(hit % p == miss % p == 1 % p for p in primes)
    assert (hit + 1) % outsider == 0 and (miss + 1) % outsider != 0
    return hit, miss


def joint_rad_ris_local_factor(p: int, support_power: int, excess_power: int) -> Fraction:
    """Exact p-Euler factor for sum_n rad(n)^(-s) ris(n)^(-u), real s>1,u>0.

    The proof of the infinite Euler product is analytic; this returns only
    one factor for integer s>=2,u>=1, not its unproved analytic extension.
    """
    if not is_prime(p):
        raise RadRisError("Euler factor requires genuine bounded prime")
    _bounded_positive(support_power, "support exponent", 12)
    _bounded_positive(excess_power, "excess exponent", 12)
    if support_power < 2:
        raise RadRisError("support exponent >=2 required in finite exact API")
    q_support = Fraction(1, p ** support_power)
    q_excess = Fraction(1, p ** excess_power)
    return 1 + q_support / (1 - q_excess)


def gibbs_prime_moments(primes: tuple[int, ...], beta: int) -> tuple[tuple[int, Fraction, Fraction, Fraction], ...]:
    """Finite prime Gibbs factors: (p, P(support), E(excess exponent), covariance).

    These are exact rational coefficients for beta>=2. An infinite prime
    identity requires the separately proved beta>1 analytic convergence.
    """
    if type(primes) is not tuple or len(primes) > 128 or primes != tuple(sorted(set(primes))):
        raise RadRisError("sorted, distinct finite tuple of primes required")
    _bounded_positive(beta, "inverse temperature", 12)
    if beta < 2 or not all(is_prime(p) for p in primes):
        raise RadRisError("integer beta>=2 and genuine primes required")
    return tuple((p, q, q * q / (1 - q), q * q)
                 for p in primes for q in (Fraction(1, p ** beta),))
