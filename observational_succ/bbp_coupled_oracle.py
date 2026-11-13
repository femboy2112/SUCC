"""Source-locked BBP finite-to-analytic oracle: exact rational certificates.

The only trusted arithmetic source is observational_succ.duck_bbp, literal U_0=0.
The known analytic BBP evaluation and upper tail inequality are **imports**;
this module checks their finite rational consequences. Its outputs cannot
prove all-N signed cancellation or base-16 normality. Every reconstructed
sample shares ONE root interval; independent per-time completion is forbidden.

Threat model: untrusted certificate values versus fixed installed checker code.
An adversary replacing installed Python/code itself is outside this boundary.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from . import duck_bbp


class OracleError(ValueError):
    """Malformed, forged, or unjustified finite source certificate."""


class UnresolvedAtPrecision(OracleError):
    """The declared BBP interval cannot yet certify this hex cylinder."""


SOURCE_ID = 'bbp-four-pole-zero-seed-v1'


def natural(x: int, label: str, minimum: int = 0) -> int:
    if type(x) is not int or x < minimum:
        raise OracleError(f'{label} must be an integer >= {minimum}')
    return x


def floor_q(x: Q) -> int:
    return x.numerator // x.denominator


def closed_root_enclosure(source_depth: int) -> tuple[Q, Q]:
    """For alpha=pi/16, strict P_L<alpha<P_L+B_L by the imported BBP law.

    We use a closed rational enclosure for safe verification. Both endpoints
    are finite and exact, and neither endpoint is identified with alpha.
    """
    depth = natural(source_depth, 'source_depth')
    return duck_bbp.tail_interval(0, depth)


@dataclass(frozen=True)
class PrefixSignal:
    """Monotone knowledge capacity, not confidence/proximity to normality."""
    source_depth: int
    budget: int
    certified_digits: int
    budget_saturated: bool


def finite_prefix_signal(source_depth: int, budget: int = 64) -> PrefixSignal:
    """Count stable hexadecimal digits without ever guessing at a boundary.

    A fixed-budget signal is nondecreasing with source depth because certified
    source intervals are nested. Its value says nothing about signed cancellation.
    """
    source_depth = natural(source_depth, 'source_depth')
    budget = natural(budget, 'budget', 1)
    lo, hi = closed_root_enclosure(source_depth)
    base = 1
    certified = 0
    for digits in range(1, budget + 1):
        base *= 16
        if floor_q(base * lo) != floor_q(base * hi):
            break
        certified = digits
    return PrefixSignal(source_depth, budget, certified, certified == budget)


@dataclass(frozen=True)
class RootPrefixCertificate:
    """A checked common root interval certifying a finite base-16 prefix.

    The *same* root prefix determines all shifted windows n+k <= digits.
    Fields are all recomputed under the installed original source on creation;
    source_id metadata alone never authenticates a caller-supplied prefix.
    """
    source_depth: int
    digits: int
    prefix: int
    lower: Q
    upper: Q
    source_id: str = SOURCE_ID

    def __post_init__(self) -> None:
        natural(self.source_depth, 'source_depth')
        natural(self.digits, 'digits', 1)
        lo, hi = closed_root_enclosure(self.source_depth)
        if (self.source_id != SOURCE_ID or type(self.prefix) is not int
                or type(self.lower) is not Q or type(self.upper) is not Q
                or (self.lower, self.upper) != (lo, hi)
                or not 0 <= lo < hi < 1):
            raise OracleError('Root certificate is not bound to the exact source')
        radix = 16 ** self.digits
        low_cell, high_cell = floor_q(radix * lo), floor_q(radix * hi)
        if low_cell != high_cell or low_cell != self.prefix:
            raise UnresolvedAtPrecision('Root interval crosses a hex boundary')

    def word(self, n: int, k: int) -> int:
        """Exactly floor(16^k * {16^n alpha}), using one shared root.

        n=1 is the first pi orbit sample {pi}; n=0 is alpha itself.
        """
        natural(n, 'n')
        natural(k, 'k', 1)
        if n + k > self.digits:
            raise UnresolvedAtPrecision('Requested word exceeds certified prefix')
        return (self.prefix // 16 ** (self.digits - n - k)) % (16 ** k)


def certify_root(source_depth: int, digits: int) -> RootPrefixCertificate:
    """Certify when both rational interval endpoints share a length-k prefix."""
    source_depth = natural(source_depth, 'source_depth')
    digits = natural(digits, 'digits', 1)
    lo, hi = closed_root_enclosure(source_depth)
    prefix = floor_q(16 ** digits * lo)
    return RootPrefixCertificate(source_depth, digits, prefix, lo, hi)


@dataclass(frozen=True)
class DefectSnapshot:
    source_id: str
    source_depth: int
    digits: int
    n_samples: int
    k: int
    counts: tuple[tuple[int, int], ...]
    variation: Q
    energy: Q
    coverage_lower: Q


def snapshot(root: RootPrefixCertificate, n_samples: int, k: int) -> DefectSnapshot:
    """Finite exact word frequencies; no float, no independent continuations.

    D=1-sum_w min(c_w/N,16^-k). E=16^k sum(c_w/N)^2-1.
    Both are exact identities for the original orbit's certified samples.
    """
    if not isinstance(root, RootPrefixCertificate):
        raise OracleError('Require a source-verified root certificate')
    # Recheck: modified/forged dataclass instances do not become authorities.
    RootPrefixCertificate(root.source_depth, root.digits, root.prefix,
                          root.lower, root.upper, root.source_id)
    N = natural(n_samples, 'n_samples', 1)
    k = natural(k, 'k', 1)
    if N + k > root.digits:
        raise UnresolvedAtPrecision('Need one root prefix of length N+k')
    M = 16 ** k
    histogram: dict[int, int] = {}
    for n in range(1, N + 1):
        w = root.word(n, k)
        histogram[w] = histogram.get(w, 0) + 1
    counts = tuple(sorted(histogram.items()))
    D = Q(1) - sum((min(Q(c, N), Q(1, M)) for c in histogram.values()), Q())
    E = Q(M * sum(c * c for c in histogram.values()), N * N) - 1
    coverage = max(Q(), Q(1) - Q(N, M))
    if D < coverage or E < 0:
        raise ArithmeticError('Universal finite-support bounds were violated')
    return DefectSnapshot(SOURCE_ID, root.source_depth, root.digits, N, k,
                          counts, D, E, coverage)


def _authenticate_snapshot(record: DefectSnapshot) -> None:
    """Treat the entire supplied record as untrusted, not just its label."""
    if not isinstance(record, DefectSnapshot):
        raise OracleError('Exact defect snapshot required')
    root = certify_root(record.source_depth, record.digits)
    actual = snapshot(root, record.n_samples, record.k)
    if actual != record:
        raise OracleError('Snapshot does not equal source-recomputed data')


def refinement_energy(coarse: DefectSnapshot, fine: DefectSnapshot) -> Q:
    """Exact Haar/conditional-expectation increment; nonnegative."""
    _authenticate_snapshot(coarse)
    _authenticate_snapshot(fine)
    if (coarse.source_id, coarse.source_depth, coarse.digits,
            coarse.n_samples, coarse.k + 1) != (
            fine.source_id, fine.source_depth, fine.digits,
            fine.n_samples, fine.k):
        raise OracleError('Refinement needs one source/root and adjacent depths')
    old, new = dict(coarse.counts), dict(fine.counts)
    for w, cnt in old.items():
        if sum(new.get(16 * w + a, 0) for a in range(16)) != cnt:
            raise OracleError('Refinement map lost/misassigned observations')
    if set(w // 16 for w in new) != set(old):
        raise OracleError('Refinement contains unmatched parent cells')
    increment = Q(16 ** coarse.k, coarse.n_samples ** 2) * (
        16 * sum(c*c for c in new.values()) - sum(c*c for c in old.values()))
    if increment < 0 or increment != fine.energy - coarse.energy:
        raise ArithmeticError('Finite Haar energy identity failed')
    return increment


def temporal_energy(before: DefectSnapshot, after: DefectSnapshot,
                    new_word: int) -> Q:
    """Exact signed time increment, recomputed from certified source counts.

    ΔE = M[(Q+2c_w+1)/(N+1)^2 - Q/N^2], Q=sum c_j^2.
    Its sign is not intrinsically positive: more observations may help or harm.
    """
    _authenticate_snapshot(before)
    _authenticate_snapshot(after)
    if (before.source_id, before.source_depth, before.digits, before.k,
            before.n_samples+1) != (after.source_id, after.source_depth,
            after.digits, after.k, after.n_samples):
        raise OracleError('Time edge needs one source, one resolution, N -> N+1')
    M, N = 16**before.k, before.n_samples
    if type(new_word) is not int or not 0 <= new_word < M:
        raise OracleError('New sample must lie in its declared partition')
    old = dict(before.counts)
    expected = old.copy()
    expected[new_word] = expected.get(new_word, 0) + 1
    if dict(after.counts) != expected:
        raise OracleError('Time edge is not the authenticated single new sample')
    Q0 = sum(c*c for c in old.values())
    increment = M * (Q(Q0+2*old.get(new_word,0)+1,(N+1)**2) - Q(Q0,N*N))
    if increment != after.energy-before.energy:
        raise ArithmeticError('Signed time energy identity failed')
    return increment


@dataclass(frozen=True)
class SquareReceipt:
    source_id: str
    N: int
    k: int
    source_depth: int
    root_digits: int
    horizontal_refinement_N: Q
    horizontal_refinement_N1: Q
    temporal_increment_k: Q
    temporal_increment_k1: Q
    square_energy_commutator: Q
    exact_word_square_commutes: bool


def certify_square(root: RootPrefixCertificate, N: int, k: int) -> SquareReceipt:
    """Two routes through (N,k)->(N+1,k+1) agree exactly.

    Time extension and partition refinement commute on *counts*, not because
    of gravitational curvature but because both are functions of one source.
    Energy increments depend on the state and need not be monotone in time.
    """
    N = natural(N, 'N', 1)
    k = natural(k, 'k', 1)
    if N + 1 + k + 1 > root.digits:
        raise UnresolvedAtPrecision('Not enough common-root digits for full square')
    a = snapshot(root, N, k)
    b = snapshot(root, N, k+1)
    c = snapshot(root, N+1, k)
    d = snapshot(root, N+1, k+1)
    inc_ab = refinement_energy(a, b)
    inc_cd = refinement_energy(c, d)
    time_ac = temporal_energy(a, c, root.word(N+1,k))
    time_bd = temporal_energy(b, d, root.word(N+1,k+1))
    # Fine endpoint after one new sample, then coarse aggregation = same endpoint.
    old_k, new_k, old_f, new_f = (dict(s.counts) for s in (a,c,b,d))
    w = root.word(N+1, k)
    wf = root.word(N+1, k+1)
    if (new_k != {key: val + (key == w) for key, val in old_k.items()} |
            ({w: 1} if w not in old_k else {})):
        raise ArithmeticError('Time update at k was not a one-cell increment')
    if (new_f != {key: val + (key == wf) for key, val in old_f.items()} |
            ({wf: 1} if wf not in old_f else {})):
        raise ArithmeticError('Time update at k+1 was not a one-cell increment')
    commutator = inc_ab + time_bd - time_ac - inc_cd
    if commutator:
        raise ArithmeticError('Path-independent energy difference failed')
    return SquareReceipt(SOURCE_ID, N, k, root.source_depth, root.digits,
                         inc_ab, inc_cd, time_ac, time_bd, commutator, True)


def verify_green_transport(n: int, depth: int) -> tuple[Q, Q]:
    """Exact interval naturality: 16(U_n+I_{n,d+1})=U_{n+1}+I_{n+1,d}.

    The right and left endpoints agree separately for EVERY n,d >= 0.
    """
    n, depth = natural(n, 'n'), natural(depth, 'depth')
    u = duck_bbp.lifted_orbit(n)
    u_next = 16 * u + duck_bbp.forcing(n+1)
    if u_next != duck_bbp.lifted_orbit(n+1):
        raise ArithmeticError('Original zero-seed forward recurrence failed')
    old = duck_bbp.tail_interval(n, depth+1)
    new = duck_bbp.tail_interval(n+1, depth)
    left = tuple(16 * (u + x) for x in old)
    right = tuple(u_next + x for x in new)
    if left != right:
        raise ArithmeticError('Source-locked oracle transport failed')
    return left


def pure_gauge_holonomy(n: int, h: int) -> Q:
    """Finite Fourier time/frequency plaquette is FLAT for a phase potential.

    Taking phi(n,h)=h U_n modulo 1, oriented edge differences must sum
    to zero around every loop. This obstructs claiming that the BBP forcing
    alone induces gauge-invariant curvature in this particular connection.
    """
    n = natural(n, 'n')
    if type(h) is not int:
        raise OracleError('Frequency must be an exact integer')
    u = duck_bbp.lifted_orbit(n)
    delta = 15 * u + duck_bbp.forcing(n+1)
    u1 = u + delta
    if u1 != duck_bbp.lifted_orbit(n+1):
        raise ArithmeticError('Unbound gauge edge')
    time_then_freq = h * delta + u1
    freq_then_time = u + (h+1) * delta
    return (time_then_freq - freq_then_time) % 1
