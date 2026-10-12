"""Exact finite coverage certificates for observational SUCC.

Classical chi-square/data-processing and Doeblin-minorization theorems are
recast as typed source-relative proof obligations. All probabilities and
bounds here are exact Fractions. Source identifiers and independence flags
are declarations, NOT authentication of empirical measurements.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt
from typing import Hashable, Iterable, Sequence


class CoverageError(ValueError):
    """Malformed source law, reference, instrument, or arithmetic factor."""


def _fraction(value: object) -> F:
    if type(value) is int or type(value) is F:
        return F(value)
    raise CoverageError("Use exact integers or Fractions, never floats")


@dataclass(frozen=True)
class CoverageFrame:
    """Source-relative finite observable P with strictly positive reference pi.

    Every atom must be listed even when its actual probability is zero.
    A source_id records the *declared* source, not physical verification.
    """
    source_id: str
    observable: str
    atoms: tuple[Hashable, ...]
    masses: tuple[F, ...]
    reference: tuple[F, ...]
    epoch: int = 0

    def __post_init__(self) -> None:
        if not isinstance(self.source_id, str) or not self.source_id:
            raise CoverageError("A nonempty source identifier is mandatory")
        if not isinstance(self.observable, str) or not self.observable:
            raise CoverageError("A nonempty observable name is mandatory")
        if type(self.epoch) is not int or self.epoch < 0:
            raise CoverageError("Invalid causal epoch")
        if not self.atoms or len(set(self.atoms)) != len(self.atoms):
            raise CoverageError("Outcome labels must be nonempty and distinct")
        if len(self.masses) != len(self.atoms) or len(self.reference) != len(self.atoms):
            raise CoverageError("Masses and reference must match the full alphabet")
        p = tuple(_fraction(x) for x in self.masses)
        pi = tuple(_fraction(x) for x in self.reference)
        if any(x < 0 for x in p) or any(x <= 0 for x in pi):
            raise CoverageError("Actual masses must be nonnegative; reference strictly positive")
        if sum(p, F(0)) != 1 or sum(pi, F(0)) != 1:
            raise CoverageError("Both measures must sum exactly to one")
        object.__setattr__(self, "masses", p)
        object.__setattr__(self, "reference", pi)

    @property
    def chi2(self) -> F:
        return sum(((p - q) ** 2 / q for p, q in zip(self.masses, self.reference)), F(0))

    def bound(self, tau: F) -> dict:
        """Sharp limiting lower bound on reference mass with P(x)>=tau*pi(x)."""
        tau = _fraction(tau)
        if not F(0) < tau < F(1):
            raise CoverageError("Coverage threshold must be strictly between zero and one")
        exceptions = tuple(x for x, p, q in zip(self.atoms, self.masses, self.reference)
                           if p < tau * q)
        good_mass = sum((q for p, q in zip(self.masses, self.reference)
                         if p >= tau * q), F(0))
        c2 = (1 - tau) ** 2
        lower = c2 / (self.chi2 + c2)
        if good_mass < lower:
            raise AssertionError("Impossible: the proved coverage bound was violated")
        return {"chi2": self.chi2, "tau": tau, "good_mass": good_mass,
                "lower_mass": lower, "exceptions": exceptions,
                "exception_count": len(exceptions)}

    def push(self, outputs: Sequence[Hashable], rows: Sequence[Sequence[F]],
             name: str) -> CoverageFrame:
        """Push BOTH P and pi through a declared stochastic source instrument.

        Unreachable outputs with zero reference mass are discarded; an output
        having positive actual mass but zero reference is impossible here.
        """
        outputs = tuple(outputs)
        if not outputs or len(set(outputs)) != len(outputs):
            raise CoverageError("Outputs must be nonempty and distinct")
        if len(rows) != len(self.atoms):
            raise CoverageError("One stochastic row required per source state")
        kernel = []
        for row in rows:
            if len(row) != len(outputs):
                raise CoverageError("Wrong stochastic row width")
            vec = tuple(_fraction(t) for t in row)
            if any(t < 0 for t in vec) or sum(vec, F(0)) != 1:
                raise CoverageError("Every row must be stochastic")
            kernel.append(vec)
        new_p = [sum((self.masses[i] * kernel[i][j]
                      for i in range(len(self.atoms))), F(0))
                 for j in range(len(outputs))]
        new_q = [sum((self.reference[i] * kernel[i][j]
                      for i in range(len(self.atoms))), F(0))
                 for j in range(len(outputs))]
        keep = [j for j in range(len(outputs)) if new_q[j] > 0]
        result = CoverageFrame(self.source_id, name, tuple(outputs[j] for j in keep),
                               tuple(new_p[j] for j in keep),
                               tuple(new_q[j] for j in keep), self.epoch + 1)
        if result.chi2 > self.chi2:
            raise AssertionError("Chi-square data processing unexpectedly violated")
        return result


def uniform_frame(source_id: str, observable: str,
                  masses: Sequence[F]) -> CoverageFrame:
    masses = tuple(_fraction(p) for p in masses)
    n = len(masses)
    if not n:
        raise CoverageError("Nonempty alphabet required")
    return CoverageFrame(source_id, observable, tuple(range(n)), masses,
                         (F(1, n),) * n)


def collision_index(counts: Sequence[int]) -> F:
    """q Pr(X=X')-1 for independent draws from the same empirical law."""
    if not counts or any(type(x) is not int or x < 0 for x in counts):
        raise CoverageError("Counts must be nonnegative integers on full alphabet")
    n = sum(counts)
    if not n:
        raise CoverageError("At least one observed sample required")
    return F(len(counts) * sum(c * c for c in counts), n * n) - 1


def independent_product(left: CoverageFrame, right: CoverageFrame, *,
                        declared_independent: bool = False) -> CoverageFrame:
    """Tensor is lawful only under a separate independence hypothesis."""
    if declared_independent is not True:
        raise CoverageError("Independent source product requires declared independence")
    combined = CoverageFrame(left.source_id + "x" + right.source_id,
        left.observable + "x" + right.observable,
        tuple((a, b) for a, b in product(left.atoms, right.atoms)),
        tuple(a * b for a, b in product(left.masses, right.masses)),
        tuple(a * b for a, b in product(left.reference, right.reference)))
    if 1 + combined.chi2 != (1 + left.chi2) * (1 + right.chi2):
        raise AssertionError("Independent tensor law failed")
    return combined


def translation_audit(joint: Sequence[tuple[int, int, F]], modulus: int,
                      source_id: str) -> dict:
    """Y+U mod q, where U may depend on Y; exact conditional-energy ledger.

    The reference Haar measure is invariant under each FIXED shift U=u;
    it is not generally invariant under a source-dependent random shift.
    """
    if type(modulus) is not int or modulus <= 1:
        raise CoverageError("Modulus must exceed one")
    mass = {(x, u): F(0) for x in range(modulus) for u in range(modulus)}
    for x, u, value in joint:
        if type(x) is not int or type(u) is not int or not (0 <= x < modulus and 0 <= u < modulus):
            raise CoverageError("Translation outside declared finite clock")
        value = _fraction(value)
        if value < 0:
            raise CoverageError("Negative joint mass")
        mass[x, u] += value
    if sum(mass.values(), F(0)) != 1:
        raise CoverageError("Joint source/update law must be normalized")
    by_x = [sum((mass[x, u] for u in range(modulus)), F(0)) for x in range(modulus)]
    by_u = [sum((mass[x, u] for x in range(modulus)), F(0)) for u in range(modulus)]
    by_z = [sum((mass[x, u] for x in range(modulus) for u in range(modulus)
                 if (x + u) % modulus == z), F(0)) for z in range(modulus)]
    source = uniform_frame(source_id, "original source", by_x)
    terminal = uniform_frame(source_id, "source after declared translation", by_z)
    conditional_energy = sum((F(modulus) * sum((mass[x, u] ** 2 / by_u[u]
                           for x in range(modulus)), F(0)) - by_u[u]
                       for u in range(modulus) if by_u[u] > 0), F(0))
    if terminal.chi2 > conditional_energy:
        raise AssertionError("Conditional-energy bound failed")
    independent = all(mass[x, u] == by_x[x] * by_u[u]
                      for x in range(modulus) for u in range(modulus))
    if independent and terminal.chi2 > source.chi2:
        raise AssertionError("Independent convolution cannot increase chi2")
    return {"source": source, "terminal": terminal,
            "conditional_energy": conditional_energy,
            "independent_update": independent}


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    return all(n % d != 0 for d in range(2, isqrt(n) + 1))


def gaussian_coordinate(point: tuple[int, int], factor: tuple[int, int]) -> int:
    """For prime norm p=a^2+b^2, pi=a+bi divides x+iy iff bx-ay=0 mod p."""
    a, b = factor
    p = a * a + b * b
    if not is_prime(p) or p % 4 != 1:
        raise CoverageError("Only authentic split Gaussian prime norms are accepted")
    x, y = point
    return (b * x - a * y) % p


def gaussian_frame(points: Iterable[tuple[int, int]], factor: tuple[int, int],
                   source_id: str) -> CoverageFrame:
    points = tuple(points)
    if not points:
        raise CoverageError("Empty sampled source")
    p = factor[0] ** 2 + factor[1] ** 2
    if not is_prime(p) or p % 4 != 1:
        raise CoverageError("Gaussian factor must have split rational prime norm")
    counts = [0] * p
    for point in points:
        counts[gaussian_coordinate(point, factor)] += 1
    result = uniform_frame(source_id, f"Gaussian residue mod {factor}",
                           tuple(F(c, len(points)) for c in counts))
    if result.chi2 != collision_index(counts):
        raise AssertionError("Projection pair-collision identity failed")
    return result


def lattice_snake(width: int) -> tuple[tuple[int, int], ...]:
    """A finite unit-step self-avoiding full-grid control; NOT a prime walk."""
    if type(width) is not int or width < 1:
        raise CoverageError("Positive integral width required")
    return tuple((x, y) for y in range(width)
                 for x in (range(width) if y % 2 == 0 else range(width - 1, -1, -1)))


def bernoulli_succ_block(q: int, bias: F = F(1, 2)) -> tuple[CoverageFrame, F]:
    """Exactly q-1 independent +0/+1 SUCC steps cover all residues mod q.

    The returned uniform minorization coefficient is q*min(bias,1-bias)^(q-1).
    Independence is a premise defining this mathematical experiment.
    """
    if type(q) is not int or q < 2:
        raise CoverageError("Clock order must be >= 2")
    bias = _fraction(bias)
    if not F(0) < bias < F(1):
        raise CoverageError("Bernoulli increment must have both possibilities")
    n = q - 1
    masses = tuple(F(comb(n, k)) * bias ** k * (1 - bias) ** (n - k)
                   for k in range(q))
    frame = uniform_frame(f"independent-Bernoulli-SUCC-q{q}", "clock residue", masses)
    alpha = q * min(bias, 1 - bias) ** n
    if alpha <= 0 or alpha > 1 or min(masses) < alpha / q:
        raise AssertionError("SUCC block minoration failed")
    return frame, alpha


def signed_succ_block(q: int) -> tuple[CoverageFrame, F]:
    """Nonzero +/-1 independent SUCC increments on an odd cyclic clock.

    After q-1 steps, possible sums 2k-(q-1) cover all residues because
    2 is invertible modulo odd q. DOES NOT imply a self-avoiding walk.
    """
    if type(q) is not int or q < 3 or q % 2 == 0:
        raise CoverageError("Signed-step certificate requires odd clock order >=3")
    n = q - 1
    masses = [F(0)] * q
    for k in range(q):
        masses[(2 * k - n) % q] += F(comb(n, k), 2**n)
    frame = uniform_frame(f"independent-signed-SUCC-q{q}", "clock residue",
                          tuple(masses))
    alpha = F(q, 2**n)
    if min(masses) < alpha/q:
        raise AssertionError("Nonzero-step lower bound failed")
    return frame, alpha


def amplify_minorization(alpha: F, blocks: int) -> F:
    """Exact independent-block Doeblin amplification: 1-(1-alpha)^blocks."""
    alpha = _fraction(alpha)
    if not F(0) <= alpha <= F(1) or type(blocks) is not int or blocks < 1:
        raise CoverageError("Invalid minorization coefficient or block count")
    return 1 - (1 - alpha) ** blocks


def cyclic_convolution(left: Sequence[F], right: Sequence[F]) -> tuple[F, ...]:
    if len(left) != len(right) or not left:
        raise CoverageError("Cyclic laws must have equal nonzero length")
    a = tuple(_fraction(x) for x in left)
    b = tuple(_fraction(x) for x in right)
    if any(x < 0 for x in a + b) or sum(a, F(0)) != 1 or sum(b, F(0)) != 1:
        raise CoverageError("Each cyclic law must be a probability distribution")
    q = len(a)
    return tuple(sum((a[x] * b[(z - x) % q] for x in range(q)), F(0))
                 for z in range(q))


def block_coverage_audit(q: int, blocks: int, bias: F = F(1, 2)) -> dict:
    """Independent convolution experiment, with exact pointwise floor receipt."""
    first, alpha = bernoulli_succ_block(q, bias)
    law = (F(1),) + (F(0),) * (q - 1)
    for _ in range(blocks):
        law = cyclic_convolution(law, first.masses)
    target = amplify_minorization(alpha, blocks)
    if min(law) < target / q:
        raise AssertionError("Amplified SUCC coverage false")
    return {"law": law, "alpha": alpha, "tau": target,
            "frame": uniform_frame(f"independent-block-{q}-{blocks}", "terminal", law)}


def batch_coverage_lower_bound(frames: Sequence[CoverageFrame], tau: F,
                               failure_mass: F) -> dict:
    """Joint-source coverage of a fraction of coordinates; no independence.

    A coordinate FAILS if the reference mass of outcomes below tau*pi is
    >= failure_mass. Its collision energy is at least
    (1-tau)^2*failure_mass/(1-failure_mass). Thus Markov's inequality
    yields the fraction of coordinates that MUST pass from mean energy.
    Context (source_id,epoch) must match: never add unrelated proof debts.
    """
    frames = tuple(frames)
    tau, failure_mass = _fraction(tau), _fraction(failure_mass)
    if not frames or not F(0) < tau < 1 or not F(0) < failure_mass < 1:
        raise CoverageError("Nonempty frames and thresholds strictly in (0,1) required")
    if len({(f.source_id, f.epoch) for f in frames}) != 1:
        raise CoverageError("Cannot combine coordinate budgets from different source epochs")
    mean_energy = sum((f.chi2 for f in frames), F(0)) / len(frames)
    witness_energy = (1 - tau) ** 2 * failure_mass / (1 - failure_mass)
    upper_bad = min(F(1), mean_energy / witness_energy)
    bad = sum((1 - f.bound(tau)['good_mass']) >= failure_mass for f in frames)
    actual_good = F(len(frames) - bad, len(frames))
    if actual_good < 1 - upper_bad:
        raise AssertionError("Exact batch coverage lower bound violated")
    return {"mean_chi2": mean_energy,
            "failure_mass": failure_mass,
            "coordinate_fraction_lower": 1 - upper_bad,
            "coordinate_fraction_observed": actual_good,
            "actual_bad_coordinates": bad}
