"""Source-indexed nonvanishing transport: a finite->global CRITERION, exact.

A compact source kernel has NO fixed positive spectral gap in infinite
dimensions, and strong operator convergence need not be norm convergence.
So the object we transport from finite sections to the global limit is a
MATRIX-COEFFICIENT survival -- a single fixed rank-one coefficient
<v, T_J v> that stays bounded away from zero -- NOT a spectral gap.  Matrix
coefficients survive strong convergence (<v,T_J v> -> <v,T v> for fixed v);
spectral gaps do not.  That asymmetry is the whole point of the criterion.

CRITERION (stated precisely in NONVANISHING_TRANSPORT_CRITERION.md).  Let
{T_J} be finite sections of a fixed bounded operator and v a fixed vector.
If the rank-one coefficients c_J = <v, T_J v> satisfy

    (i)   UNIFORM boundedness      : |c_J| <= B for a fixed finite B,
    (ii)  COMPATIBLE sections      : the c_J are nested / monotone with a
                                     certified Cauchy remainder, so a single
                                     global limit value is consistent,
    (iii) PERSISTENT positive floor: c_J >= f for a fixed rational f > 0,
                                     justified STRUCTURALLY for all J,

then the transported global coefficient c_inf exists and c_inf >= f > 0:
it is NONVANISHING.

This module (1) finite-certifies the criterion on a specific rank-one
coefficient of the authentic original Gamma finite section for J=16,32,64
(VERIFIED-EXACT-MODEL), and (2) runs the REQUIRED atomic-Haar hostile
control, where the analogous coefficient VANISHES, and shows the criterion
correctly REFUSES it (hypothesis (iii) fails -- no persistent floor).

All certificate arithmetic is exact (fractions.Fraction) via the outward
exponential brackets of infinite_gamma_carleman.exp_negative_interval and the
exact rational masses of institute_atomic_haar.  float is never a certificate.
No nontrivial zeta-zero ordinate is used: alpha_j=(4j+1)/2 is the one real
Archimedean Gamma ladder, Lambda(p^k)=log p untouched.  A persistent positive
matrix coefficient is NOT a completed Weil form and does NOT prove RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .infinite_gamma_carleman import alpha, exp_negative_interval


class TransportError(ValueError):
    pass


def _rat(x):
    if type(x) not in (F, int):
        raise TransportError("exact int/Fraction required; floats cannot certify transport")
    return F(x)


def _outward(x, den=10**36, upper=False):
    """Round a Fraction OUTWARD to a multiple of 1/den (soundness preserved)."""
    x = _rat(x)
    n = x.numerator * den // x.denominator
    if upper and F(n, den) < x:
        n += 1
    return F(n, den)


# --------------------------------------------------------------------------
# Authentic Gamma rank-one matrix coefficient and its certified lower bound.
# --------------------------------------------------------------------------

def _window_shift(J, s):
    """Validate the exact-exp Taylor window alpha_(J-1)*s <= 1, s>0, 2s<=1."""
    if type(J) is not int or J < 1:
        raise TransportError("positive integer finite-section order required")
    s = _rat(s)
    if s <= 0 or 2 * s > 1:
        raise TransportError("source Taylor window needs 0 < 2s <= 1")
    if alpha(J - 1) * s > 1:
        raise TransportError("finite section exceeds the exact-exp Taylor window")
    return s


def gamma_rank_one_coefficient(J, s=F(1, 128), pairs=8):
    """Exact bracket of the rank-one coefficient c_J = <v, K_s^(J) v>.

    K_s = diag(exp(-alpha_j s)) is the original one-real-Gamma heat kernel in
    the authentic rung basis (alpha_j=(4j+1)/2); K_s^(J)=P_J K_s P_J is its
    J-th finite section.  The FIXED vector is v_j = 1/(j+1), an honest ell^2
    vector (||v||^2 = sum 1/(j+1)^2 < pi^2/6), independent of J and of s.  So

        c_J = sum_{j<J} exp(-alpha_j s)/(j+1)^2 .

    Returns exact rational endpoints enclosing c_J, the structural first-term
    floor (valid for every J because terms are nonnegative => c_J nondecreasing),
    and a certified GEOMETRIC Cauchy remainder bounding c_inf - c_J from above.
    All numbers are exact Fraction; float is never used as a certificate.
    """
    s = _window_shift(J, s)
    if type(pairs) is not int or not 1 <= pairs <= 40:
        raise TransportError("Taylor pair budget out of range")
    c_lo = F(0)
    c_hi = F(0)
    last_exp_hi = None
    for j in range(J):
        elo, ehi = exp_negative_interval(alpha(j) * s, pairs)
        w2 = F(1, (j + 1) ** 2)
        c_lo += w2 * elo
        c_hi += w2 * ehi
        last_exp_hi = ehi
    # Structural floor: first term (j=0) is w_0^2 exp(-alpha_0 s) = exp(-s/2).
    floor_lo, _ = exp_negative_interval(alpha(0) * s, pairs)
    # Geometric Cauchy remainder: alpha_{j+1}-alpha_j = 2, so with r=exp(-2s),
    # and using w_j^2 = 1/(j+1)^2 <= 1/(J+1)^2 for every omitted index j >= J,
    #   c_inf - c_J = sum_{j>=J} w_j^2 exp(-alpha_j s)
    #              <= (1/(J+1)^2) sum_{j>=J} exp(-alpha_j s)
    #               = (1/(J+1)^2) exp(-alpha_{J-1}s) * r/(1-r)
    #              <= (1/(J+1)^2) last_exp_hi * r_hi / (1 - r_hi).
    r_lo, r_hi = exp_negative_interval(2 * s, pairs)
    if not 0 < r_hi < 1:
        raise TransportError("geometric ratio bracket must be a strict contraction")
    remainder_upper = F(1, (J + 1) ** 2) * last_exp_hi * r_hi / (1 - r_hi)
    if not (0 < floor_lo <= c_lo <= c_hi and remainder_upper > 0):
        raise TransportError("Gamma coefficient bracket is not a valid outward enclosure")
    global_upper = c_hi + remainder_upper
    return {
        "J": J,
        "shift_s": str(s),
        "fixed_vector": "v_j = 1/(j+1)  (ell^2, independent of J and s)",
        "operator": "K_s = diag(exp(-(4j+1)s/2)); finite section P_J K_s P_J",
        "coeff_lower": c_lo,
        "coeff_upper": c_hi,
        "structural_floor": floor_lo,
        "cauchy_remainder_upper": remainder_upper,
        "global_coeff_lower": c_lo,
        "global_coeff_upper": global_upper,
        "RH_proved": False,
    }


# --------------------------------------------------------------------------
# The general finite->global transport criterion (matrix-coefficient survival).
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Section:
    """One finite-section matrix coefficient as an exact outward enclosure."""
    order: int
    coeff_lower: F
    coeff_upper: F
    remainder_upper: F

    def __post_init__(self):
        for v in (self.coeff_lower, self.coeff_upper, self.remainder_upper):
            if type(v) is not F:
                raise TransportError("sections carry exact Fraction coefficients only")
        if self.coeff_lower > self.coeff_upper or self.remainder_upper < 0:
            raise TransportError("ordered enclosure with nonnegative remainder required")


def transport_criterion(sections, uniform_bound, floor):
    """Decide whether a persistent matrix coefficient transports to nonvanishing.

    sections       : iterable of Section, in increasing-order (nested) order.
    uniform_bound  : fixed rational B for hypothesis (i).
    floor          : fixed rational f claimed to hold for ALL J (hypothesis (iii)).

    This is a MATRIX-COEFFICIENT survival test, NOT a spectral-gap test.  It
    returns certified_nonvanishing=True only when all three hypotheses hold on
    the supplied data AND the coefficients are monotone nondecreasing (the
    structural witness that the first-term floor persists to the limit) AND the
    enclosures are Cauchy-consistent with a single limit value.  Otherwise it
    REFUSES and names the failing hypothesis.  It never asserts RH.
    """
    secs = tuple(sections)
    if len(secs) < 2:
        raise TransportError("need at least two nested sections to test transport")
    B = _rat(uniform_bound)
    f = _rat(floor)
    orders = [s.order for s in secs]
    if orders != sorted(orders) or len(set(orders)) != len(orders):
        raise TransportError("sections must be strictly increasing in order")

    reasons = []
    # (i) uniform boundedness: the enclosures (incl. remainder) stay under B.
    uniform_ok = all(s.coeff_upper + s.remainder_upper <= B for s in secs)
    if not uniform_ok:
        reasons.append("uniform_boundedness_failed")
    # (ii) compatible/Cauchy: nondecreasing lowers, and a common limit value
    #      exists in the intersection of all enclosures [c_lo, c_hi+rem].
    monotone = all(secs[k].coeff_lower <= secs[k + 1].coeff_lower for k in range(len(secs) - 1))
    inter_lo = max(s.coeff_lower for s in secs)
    inter_hi = min(s.coeff_upper + s.remainder_upper for s in secs)
    cauchy_ok = inter_lo <= inter_hi
    if not monotone:
        reasons.append("no_persistent_floor_coefficient_not_monotone")
    if not cauchy_ok:
        reasons.append("enclosures_inconsistent_no_common_limit")
    # (iii) persistent positive floor.
    floor_positive = f > 0
    floor_respected = all(s.coeff_lower >= f for s in secs)
    if not floor_positive:
        reasons.append("floor_not_positive")
    if not floor_respected:
        reasons.append("floor_not_respected_by_finite_data")

    certified = uniform_ok and monotone and cauchy_ok and floor_positive and floor_respected
    # Honest vanishing signature: strictly decreasing coefficients heading down.
    nonincreasing = all(secs[k].coeff_lower >= secs[k + 1].coeff_lower for k in range(len(secs) - 1))
    vanishing_signature = nonincreasing and secs[-1].coeff_lower < secs[0].coeff_lower
    return {
        "certified_nonvanishing": certified,
        "uniform_boundedness": uniform_ok,
        "compatible_monotone": monotone,
        "cauchy_consistent": cauchy_ok,
        "floor_positive": floor_positive,
        "floor_respected": floor_respected,
        "certified_global_floor": str(f) if certified else None,
        "transported_coeff_lower": str(inter_lo),
        "transported_coeff_upper": str(inter_hi),
        "vanishing_signature": vanishing_signature,
        "refusal_reasons": reasons,
        "survival_object": "rank-one matrix coefficient (NOT a spectral gap)",
        "RH_proved": False,
    }


def gamma_transport_certificate(orders=(16, 32, 64), s=F(1, 128), pairs=8):
    """VERIFIED-EXACT-MODEL: the authentic Gamma coefficient transports nonzero.

    Builds the rank-one coefficient of the original Gamma finite section for
    each order, checks it is monotone and bounded away from 0 by the structural
    first-term floor exp(-s/2), and feeds it to transport_criterion, which
    certifies the global transported coefficient is nonvanishing at finite J.
    """
    if not (isinstance(orders, tuple) and len(orders) >= 2 and list(orders) == sorted(orders)):
        raise TransportError("orders must be an increasing tuple of >=2 section orders")
    data = [gamma_rank_one_coefficient(J, s=s, pairs=pairs) for J in orders]
    floor = min(d["structural_floor"] for d in data)
    # Uniform bound: every coefficient (plus remainder) is <= the fattest global
    # upper, so take that as the exact finite uniform bound B.
    B = max(d["global_coeff_upper"] for d in data)
    sections = [Section(d["J"], d["coeff_lower"], d["coeff_upper"], d["cauchy_remainder_upper"])
                for d in data]
    verdict = transport_criterion(sections, B, floor)
    if not verdict["certified_nonvanishing"]:
        raise TransportError("authentic Gamma model unexpectedly failed its own criterion")
    # Monotone strictly increasing check across the tested orders (receipt).
    lowers = [d["coeff_lower"] for d in data]
    strictly_increasing = all(lowers[k] < lowers[k + 1] for k in range(len(lowers) - 1))
    return {
        "status": "VERIFIED-EXACT-MODEL",
        "model": "diagonal original Gamma heat kernel K_s = diag(exp(-(4j+1)s/2))",
        "fixed_vector": "v_j = 1/(j+1)",
        "shift_s": str(F(s)),
        "orders": list(orders),
        "coefficient_lowers": [str(d["coeff_lower"]) for d in data],
        "coefficient_uppers": [str(d["coeff_upper"]) for d in data],
        "cauchy_remainders_upper": [str(_outward(d["cauchy_remainder_upper"], upper=True)) for d in data],
        "structural_first_term_floor": str(_outward(floor)),
        "uniform_bound_B": str(_outward(B, upper=True)),
        "strictly_increasing_across_orders": strictly_increasing,
        "transported_global_coeff_lower": str(_outward(F(verdict["transported_coeff_lower"]))),
        "transported_global_coeff_upper": str(_outward(F(verdict["transported_coeff_upper"]), upper=True)),
        "certified_global_floor": verdict["certified_global_floor"],
        "criterion_verdict": verdict,
        "RH_proved": False,
    }


# --------------------------------------------------------------------------
# REQUIRED atomic-Haar hostile control: the criterion must REFUSE a vanisher.
# --------------------------------------------------------------------------

def atomic_haar_vanishing_coefficients(sizes=(4, 16, 64, 256), period=2):
    """Exact analog coefficients from institute_atomic_haar, which VANISH.

    Two independent atomic witnesses, each the matrix-coefficient analog of our
    persistent diagonal coefficient but in the atomic-Haar regime:

      - harmonic_graph_witness(size).source_norm_squared = 1/H_size -> 0, the
        squared mass of the graph sequence tending to (0, Haar);
      - haar_unit_mass((2,3,...,p)) = prod (q-1)/q -> 0, the atomic vacuum mass
        as the prime family grows (the divergent Euler product).

    Both are exact rationals that decrease toward 0: the hypothesis (iii)
    persistent positive floor is STRUCTURALLY absent (atomic dilution).
    """
    from .institute_atomic_haar import harmonic_graph_witness, haar_unit_mass
    if not (isinstance(sizes, tuple) and len(sizes) >= 2 and list(sizes) == sorted(sizes)):
        raise TransportError("sizes must be an increasing tuple of >=2 entries")
    harmonic = [harmonic_graph_witness(n, period)["source_norm_squared"] for n in sizes]
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23)
    families = [primes[:k] for k in range(1, len(sizes) + 1)]
    haar = [haar_unit_mass(fam) for fam in families]
    return {
        "harmonic_graph_sizes": list(sizes),
        "harmonic_source_norm_squared": harmonic,
        "haar_prime_families": [list(fam) for fam in families],
        "haar_unit_masses": haar,
        "RH_proved": False,
    }


def atomic_haar_refusal(sizes=(4, 16, 64, 256), period=2):
    """Feed the vanishing atomic coefficients to the criterion; it must REFUSE.

    A criterion that does NOT refuse atomic-Haar is overclaimed.  We claim the
    first (largest) observed value as a would-be positive floor and show the
    criterion refuses because the coefficients are not monotone-up and the floor
    is not persisted -- the honest, correct verdict, since the true limit is 0.
    """
    co = atomic_haar_vanishing_coefficients(sizes, period)
    receipts = {}
    for name, values in (("harmonic_graph_witness", co["harmonic_source_norm_squared"]),
                         ("haar_unit_mass", co["haar_unit_masses"])):
        orders = list(range(len(values)))
        # Exact point enclosures (lo=hi=value, zero remainder: these are exact).
        sections = [Section(k, F(v), F(v), F(0)) for k, v in zip(orders, values)]
        # A would-be positive floor: the largest observed value.  No structural
        # floor exists, so the criterion must still refuse.
        claimed_floor = max(values)
        bound = max(values) + 1
        verdict = transport_criterion(sections, bound, claimed_floor)
        decreasing = all(values[i] > values[i + 1] for i in range(len(values) - 1))
        receipts[name] = {
            "coefficients": [str(v) for v in values],
            "strictly_decreasing": decreasing,
            "tends_to_zero_signature": verdict["vanishing_signature"],
            "claimed_floor": str(claimed_floor),
            "criterion_refused": not verdict["certified_nonvanishing"],
            "refusal_reasons": verdict["refusal_reasons"],
            "verdict": verdict,
        }
        if verdict["certified_nonvanishing"]:
            raise TransportError(
                f"atomic-Haar control FAILED: criterion wrongly certified {name}")
    return {
        "status": "HOSTILE-CONTROL-REFUSED",
        "meaning": "criterion correctly refuses the vanishing atomic-Haar coefficient",
        "receipts": receipts,
        "RH_proved": False,
    }


def nonvanishing_transport_report(orders=(16, 32, 64), s=F(1, 128),
                                  sizes=(4, 16, 64, 256), period=2):
    """Full receipt: authentic Gamma model certified, atomic-Haar refused.

    Honest boundary: the GENERAL criterion is an elementary theorem (a monotone
    bounded matrix coefficient transports to a nonvanishing limit under strong
    convergence).  It is CERTIFIED here only for the diagonal Gamma heat-kernel
    model at finite J=16,32,64, where monotonicity and the first-term floor are
    exact.  It is NOT a proof that the genuine non-diagonal Suzuki S4 / Weil
    coefficient satisfies hypothesis (iii); that persistence is OPEN.  Matrix-
    coefficient survival is deliberately weaker than a spectral gap (a compact
    kernel has none), carries no completed Weil positivity, and proves no RH.
    """
    authenticated = False
    source_blob = None
    try:
        from .infinite_gamma_carleman import original_source_infinite_gamma_contract
        contract = original_source_infinite_gamma_contract()
        authenticated = contract.get("true_prime_power") == ((2, 2),)
        source_blob = contract.get("source_git_blob")
    except Exception:
        authenticated = False
    gamma = gamma_transport_certificate(orders=orders, s=s)
    hostile = atomic_haar_refusal(sizes=sizes, period=period)
    return {
        "criterion": (
            "finite sections {T_J} of a fixed operator, fixed vector v: if "
            "c_J=<v,T_J v> are (i) uniformly bounded, (ii) compatible/Cauchy, "
            "(iii) bounded below by a fixed f>0, then the transported c_inf>=f>0."
        ),
        "survival_object": "rank-one matrix coefficient, NOT a spectral gap",
        "no_go_respected": (
            "compact kernel has no fixed positive spectral gap in infinite "
            "dimensions; strong convergence need not be norm convergence; only "
            "matrix coefficients survive strong convergence."
        ),
        "source_authenticated": authenticated,
        "source_git_blob": source_blob,
        "gamma_model_certificate": gamma,
        "atomic_haar_hostile_control": hostile,
        "finite_J_only": True,
        "global_limit_requires": (
            "strong convergence of the ACTUAL source finite sections plus a "
            "STRUCTURAL persistence of the chosen coefficient; certified here "
            "only for the diagonal Gamma model, OPEN for the genuine S4/Weil "
            "operator. This is finite-J + a hostile control, NOT a global proof."
        ),
        "RH_proved": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(nonvanishing_transport_report(), indent=2, default=str))
