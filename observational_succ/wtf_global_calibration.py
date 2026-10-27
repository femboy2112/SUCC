"""WTF (Within-Source Fourier Test): exact coincidence and global-calibration firewalls.

Research-only continuation of Seinfeld coherence/checkpoint PR #314. The two
coordinate forms share the SAME input. Their independent-copy agreement is a
comparator, never a p-value or an automatic evidence multiplier.

Classical source: normalized Ramanujan sums; character orthogonality; exact
finite change of measure; predictable nonnegative test martingales.
The actual BBP source enters ONLY through the existing authenticated history
and carry witness, not through a synthesized stochastic BBP path.

All results here are finite algebraic/probabilistic identities and a new-to-this-
program failure certificate. They do NOT prove signed selected Weyl decay or
base-16 normality of pi. RH is unrelated and remains open.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import gcd
from typing import Callable

RADIX = 16


def _nat(value: int, label: str, lower: int = 1, upper: int = 1_000_000) -> int:
    if type(value) is not int or not lower <= value <= upper:
        raise ValueError(f"{label}: integer in [{lower},{upper}] required")
    return value


def _rational(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact int/Fraction required, not float or bool")
    return Q(value)


def mobius(n: int) -> int:
    """Classical Moebius mu(n), with exact trial division."""
    _nat(n, "Mobius argument")
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            sign = -sign
            n //= p
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign


def totient(q: int) -> int:
    _nat(q, "modulus")
    return sum(gcd(a, q) == 1 for a in range(q))


def ramanujan(q: int, d: int) -> int:
    """Exact Kluyver divisor formula: c_q(d)=sum_{a|(q,d)} a mu(q/a)."""
    _nat(q, "modulus")
    if type(d) is not int:
        raise ValueError("discrepancy must be an integer")
    g = gcd(q, d)
    return sum(a * mobius(q // a) for a in range(1, g + 1) if g % a == 0)


def primitive_projection(q: int, d: int) -> Q:
    """Normalized primitive-character average, NOT full compatibility."""
    return Q(ramanujan(q, d), totient(q))


def full_projection(q: int, d: int) -> Q:
    """The full frequency sum is precisely 1_{q|d}."""
    _nat(q, "modulus")
    if type(d) is not int:
        raise ValueError("discrepancy must be integer")
    return Q(1 if d % q == 0 else 0)


@dataclass(frozen=True)
class ResonanceReceipt:
    q: int
    agreements: int
    anti_agreements: int
    same_variable_probability: Q
    independent_copy_probability: Q
    naive_independent_copy_ratio: Q | None
    full_projection_mean: Q
    primitive_projection_mean: Q
    null_family_selected: bool = False
    new_weyl_saving_proved: bool = False


def resonance_receipt(q: int, F: Callable[[int], int],
                      G: Callable[[int], int]) -> ResonanceReceipt:
    """Observe forms on a COMMON uniform input, with a separate independent-copy comparator.

    The comparator has marginals F(X),G(Y) for independent uniform X,Y.
    It is generally NOT the source-null law for F(X),G(X); the ratio is not
    an e-value, valid p-value or proof of a novel arithmetic relationship.
    """
    _nat(q, "modulus", upper=4096)
    if not callable(F) or not callable(G):
        raise ValueError("two declared source functions required")
    left = tuple(F(x) for x in range(q))
    right = tuple(G(x) for x in range(q))
    if any(type(x) is not int for x in left + right):
        raise ValueError("integer-valued arithmetic forms required")
    agreements = sum(full_projection(q, a - b) for a, b in zip(left, right))
    if agreements.denominator != 1:
        raise ArithmeticError("full-projector count failed")
    anti = sum((a - b) % q == q // 2 for a, b in zip(left, right)) if q % 2 == 0 else 0
    marg_F = [0] * q
    marg_G = [0] * q
    for a, b in zip(left, right):
        marg_F[a % q] += 1
        marg_G[b % q] += 1
    independent = Q(sum(a * b for a, b in zip(marg_F, marg_G)), q * q)
    primitive = sum((primitive_projection(q, a - b) for a, b in zip(left, right)), Q()) / q
    same = Q(agreements, q)
    return ResonanceReceipt(q, int(agreements), anti, same, independent,
                            same / independent if independent else None,
                            same, primitive)


def quadratic_exact_roots(k: int) -> tuple[int, ...]:
    """ALL x(x-2)==0 mod 2^k for k>=4; only 0,2 extend coherently forever."""
    _nat(k, "power-of-two depth", 4, 22)
    half = 1 << (k-1)
    return (0, 2, half, half + 2)


def quadratic_antipodal_roots(k: int) -> tuple[int, ...]:
    """ALL x(x-2)==2^(k-1) mod 2^k for k>=4."""
    _nat(k, "power-of-two depth", 4, 22)
    quarter = 1 << (k-2)
    return (quarter, quarter + 2, 3 * quarter, 3 * quarter + 2)


def stable_lifts(k: int) -> tuple[int, ...]:
    """Which roots mod 2^k possess ANY root lift mod 2^(k+1)."""
    _nat(k, "power-of-two depth", 4, 21)
    old = set(quadratic_exact_roots(k))
    finer = quadratic_exact_roots(k + 1)
    return tuple(sorted(old.intersection({x % (1 << k) for x in finer})))


def fixed_frame_evalue(q: int, observed: int, frame: int) -> Q:
    """Predeclared point null at a fixed frame: q*1_{X=frame}."""
    _nat(q, "modulus", upper=4096)
    if type(observed) is not int or type(frame) is not int:
        raise ValueError("integer state and frame required")
    return Q(q if observed % q == frame % q else 0)


def global_frame_mixture(q: int, observed: int, prior: tuple[Q, ...]) -> Q:
    """Predeclared mixture of frame e-values, sum prior_j E_j; E0=1.

    The prior MUST be committed before viewing the outcome. An output-based
    choice of the frame is NOT admissible as a new unit-expectation e-value.
    """
    _nat(q, "modulus", upper=4096)
    if type(observed) is not int or type(prior) is not tuple or len(prior) != q:
        raise ValueError("integer observation and q-element prior tuple required")
    if any(type(v) not in (int, Q) or Q(v) < 0 for v in prior):
        raise ValueError("nonnegative exact prior weights required")
    weights = tuple(Q(v) for v in prior)
    if sum(weights, Q()) != 1:
        raise ValueError("frame mixture prior must have total mass one")
    return q * weights[observed % q]


def expected_postselected_frame_score(q: int, copies: int = 1) -> Q:
    """INVALID reuse of the same observed input: E0[(q 1_{X=a})^copies].

    copies=1 has expectation 1, but copies>=2 inflates it to q^(copies-1).
    This is not a legitimate product e-process without conditional new data.
    """
    _nat(q, "modulus", upper=4096)
    _nat(copies, "number of repeated frames", 1, 30)
    return Q(q ** (copies - 1))


def linear_constraint_rank_gain(existing_rows, candidate) -> int:
    """Exact Seinfeld SS-02 rank guard for LINEAR source-state claims.

    A zero rank gain proves a linear candidate is redundant given the
    declared previous rows. A positive gain is NOT stochastic independence
    or evidence for pi normality; nonlinear dependence remains unchecked.
    """
    from .seinfeld_succ import rational_rank
    if type(candidate) not in (tuple, list) or not candidate:
        raise ValueError("nonempty linear candidate required")
    row = tuple(_rational(x) for x in candidate)
    if type(existing_rows) not in (tuple, list):
        raise ValueError("linear constraint rows required")
    rows = tuple(tuple(_rational(x) for x in r) for r in existing_rows)
    if any(len(r) != len(row) for r in rows):
        raise ValueError("constraint row lengths must agree")
    old = rational_rank(rows) if rows else 0
    new = rational_rank(rows + (row,))
    if new - old not in (0, 1):
        raise ArithmeticError("single-row rank gain impossible")
    return new - old


def predictable_bet_factor(p: int | Q, stake: int | Q, outcome: int) -> Q:
    """Nonnegative martingale factor 1+lambda*(I-p), conditional null P(I=1)=p.

    Stakes must be chosen from PREVIOUS checkpoints; this function does not
    authorize outcome-dependent stakes or imply a probability law for pi.
    """
    p, stake = _rational(p), _rational(stake)
    if not Q() <= p <= 1 or type(outcome) is not int or outcome not in (0, 1):
        raise ValueError("Bernoulli null probability and binary outcome required")
    if stake < 0 or (p > 0 and stake > 1 / p):
        raise ValueError("predictable stake would give negative test mass")
    return 1 + stake * (outcome - p)


def exact_binary_checkpoint_audit(depth: int, policy: Callable[[tuple[int, ...]], tuple[Q, Q]],
                                 threshold: Q = Q(4)) -> dict:
    """Exact null tree audit (<=12 steps): E[L_t]=1 and Ville crossing bound.

    policy(prefix)->(P0(I_next=1|prefix),lambda(prefix)) MUST be predictable.
    At each tree node both outcomes and their true conditional null weights
    are considered; choose no prediction after seeing the next outcome.
    """
    _nat(depth, "tree depth", 1, 12)
    threshold = _rational(threshold)
    if threshold <= 1:
        raise ValueError("threshold >1 required")
    if not callable(policy):
        raise ValueError("declared predictable policy required")
    nodes = [((), Q(1), Q(1), False)]
    checkpoint_expectations = []
    for _ in range(depth):
        new = []
        for history, mass, evidence, crossed in nodes:
            p, stake = policy(history)
            p = _rational(p)
            for outcome, chance in ((0, 1-p), (1, p)):
                if chance == 0:
                    continue
                fac = predictable_bet_factor(p, stake, outcome)
                latest = evidence * fac
                new.append((history + (outcome,), mass * chance, latest,
                            crossed or latest >= threshold))
        nodes = new
        checkpoint_expectations.append(sum((mass * evidence for _, mass, evidence, _ in nodes), Q()))
    total_mass = sum((mass for _,mass,_,_ in nodes), Q())
    crossing_mass = sum((mass for _,mass,_,crossed in nodes if crossed), Q())
    if total_mass != 1 or any(v != 1 for v in checkpoint_expectations):
        raise ArithmeticError("reference martingale normalization failure")
    if crossing_mass > 1 / threshold:
        raise ArithmeticError("Ville inequality unexpectedly fails")
    return {"depth":depth,"threshold":threshold,"expected_each_checkpoint":tuple(checkpoint_expectations),
            "crossing_probability":crossing_mass,"ville_upper":1/threshold,
            "tree_leaves":len(nodes),"only_under_declared_null":True}


@dataclass(frozen=True)
class BBPCarryCalibration:
    horizon: int
    full_agreement: Q
    primitive_agreement: Q
    spill_count: int
    source_forcing_identical: bool
    original_seed_authenticated: bool
    pi_normality_proved: bool = False


def _same_forcing_relabelled_states(horizon: int, seed_offset: Q):
    """Changed-seed adversary V_n=U_n+16^n delta, same forcing, nonzero seed."""
    from .lambda_source_duality import original_history
    original = original_history(horizon + 1)
    return tuple(u + Q(16**(i+1)) * seed_offset for i, u in enumerate(original))


def authentic_carry_resonance(horizon: int, *, seed_offset: int | Q = 0) -> BBPCarryCalibration:
    """Exact j_n-vs-c_(n+1) compatibility on actual four-pole source.

    For n>=1: c_(n+1)=j_n+s, s in {0,1}. Therefore BOTH the full
    compatibility projector and normalized primitive Ramanujan_16 projector
    equal 1-s. #313 proves s=1 has asymptotic density zero for EVERY
    initial seed under the same forcing. Thus BOTH scores approach 1 even
    for changed-seed histories: source-specific false-positive detector.
    """
    _nat(horizon, "BBP source horizon", 1, 512)
    offset = _rational(seed_offset)
    from .lambda_source_duality import original_history, witness_selected_branches
    if offset == 0:
        original = original_history(horizon + 1)
        witnesses = witness_selected_branches(original)
        pairs = tuple((w.digit, w.literal_carry) for w in witnesses)
        authenticated = True
    else:
        states = _same_forcing_relabelled_states(horizon, offset)
        pairs = []
        for before, after in zip(states[:-1], states[1:]):
            x = before % 1
            j = (16*x).numerator // (16*x).denominator
            c = after.__floor__() - 16*before.__floor__()
            pairs.append((j, c))
        authenticated = False
    spills = 0
    for j, c in pairs:
        s = c - j
        if s not in (0, 1):
            raise ArithmeticError("forcing not source-compatible with 0/1 spill")
        if full_projection(RADIX, j - c) != Q(1 - s):
            raise ArithmeticError("full character compatibility violated")
        if primitive_projection(RADIX, j - c) != Q(1 - s):
            raise ArithmeticError("primitive character compatibility violated")
        spills += s
    agree = Q(horizon - spills, horizon)
    return BBPCarryCalibration(horizon, agree, agree, spills, True, authenticated)


def status_flags() -> dict:
    return {"source_original_four_poles_preserved": True,
            "global_frame_preselection_required": True,
            "same_variable_dependence_retained": True,
            "source_selector_specific_saving_proved": False,
            "nontrivial_selected_weyl_bound_proved": False,
            "pi_base16_normality_proved": False}
