"""Exact controls for R0_INVERSE.md; no finite-to-asymptotic inference.

All arithmetic certificates use integers and fractions.  The original
completed orbit is enclosed by the full four-pole BBP prefix and its
proved positive tail.  Pi enters only through rational cosine bounds.
Running this file prints a deterministic JSON report and writes no file.
"""

from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json


PI_LO = Q(157, 50)
PI_HI = Q(22, 7)
FRESH_SHELLS = (17, 43, 89, 179, 359)
SHALLIT_SHELLS = (64, 128, 256, 512)
PROPER_NULL = (8, -8, -4, -8, -2, -2, 1, 0)


def _integer(n, name, minimum=None):
    if type(n) is not int or (minimum is not None and n < minimum):
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return n


def v2(value):
    value = Q(value)
    if value == 0:
        return None
    a, b = abs(value.numerator), value.denominator
    return (a & -a).bit_length() - (b & -b).bit_length()


def source(n):
    _integer(n, "n", 1)
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def source_polynomials(n):
    _integer(n, "n", 1)
    return (120*n*n-89*n+16,
            (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


@lru_cache(maxsize=None)
def source_states(depth):
    _integer(depth, "depth", 0)
    result = [Q(0)]
    for n in range(1, depth+1):
        result.append(16*result[-1] + source(n))
    return tuple(result)


@lru_cache(maxsize=None)
def completed_interval(depth):
    """Enclose x=pi/16 by P_depth < x < P_depth+16^-depth/(64 depth²)."""
    _integer(depth, "depth", 1)
    low = source_states(depth)[-1] / (16**depth)
    return low, low + Q(1, 64*depth*depth*16**depth)


def gram_minimizer(left, right, jump=1):
    """Exact one-defect minimizer; left/right count extra states."""
    _integer(left, "left", 0)
    _integer(right, "right", 0)
    _integer(jump, "jump")
    if jump == 0:
        raise ValueError("jump must be nonzero")
    a = sum((Q(1, 256**k) for k in range(left+1)), Q())
    b = sum((Q(256**k) for k in range(right+1)), Q())
    denominator = Q(256)/a + Q(1)/b
    x, y = -Q(16*jump)/(a*denominator), Q(jump)/(b*denominator)
    states = tuple(x / 16**k for k in range(left, -1, -1))
    states += tuple(y * 16**k for k in range(right+1))
    return {"a": a, "b": b, "denominator": denominator,
            "x": x, "y": y, "energy": Q(jump*jump)/denominator,
            "states": states}


def rational_certificates():
    c, lam, u, span = Q(3, 40), Q(973, 50), Q(1, 2000), Q(15, 4096)
    taylor = 2*PI_LO**2 - Q(2, 3)*PI_HI**4/256
    # Sufficient rational bounds for the two square roots in RI-1.
    sqrt_upper, inverse_sqrt_lower = Q(621, 10000), Q(62499, 1000000)
    epsilon, transitions = Q(1, 512), 7*2**20-1
    d = Q(256) + Q(1, 257)
    margins = {
        "taylor_minus_lambda": taylor-lam,
        "fallback_3_over_40": lam*(1-span)**2/(257*(1+u)**2)-c,
        "boundary_local_loss_minus_c": lam/256-c,
        "sqrt_c_over_lambda_upper": sqrt_upper**2-c/lam,
        "inverse_gram_sqrt_lower": 1-d*inverse_sqrt_lower**2,
        "all_c_specialization_triangle": inverse_sqrt_lower-sqrt_upper-2*epsilon/15,
        "quiet_transition": transitions*epsilon**2-257*c,
        "two_defects_exceed_one_tenth": 38*Q(7, 128)**2-Q(1, 10),
        "kappa_upper_below_one_tenth": Q(1, 10)-PI_HI**2/128,
        "inverse_pi_coefficient_below_three": Q(3)-16*(Q(2, 15)+Q(1, 64*7**2)+Q(1, 64*8**2)),
    }
    if not all(value > 0 for value in margins.values()):
        raise ArithmeticError("a preregistered strict rational margin failed")
    return {name: str(value) for name, value in margins.items()}


def nearest_integer(value):
    """Half-up convention; none of the authenticated pi values are ties."""
    value = Q(value) + Q(1, 2)
    return value.numerator // value.denominator


def centered(value):
    value = Q(value)
    return value-nearest_integer(value)


def balanced_carries(values):
    """For completed, exactly rational orbit values, retain integer lifts."""
    values = tuple(Q(value) for value in values)
    if not values:
        raise ValueError("at least one state is needed")
    for first, second in zip(values, values[1:]):
        if second != 16*first:
            raise ValueError("values must follow the exact completed recurrence")
    lifts = tuple(nearest_integer(value) for value in values)
    errors = tuple(value-lift for value, lift in zip(values, lifts))
    carries = tuple(second-16*first for first, second in zip(lifts, lifts[1:]))
    return errors, carries


def carry_energy_certificate(values):
    errors, carries = balanced_carries(values)
    energy = sum((value*value for value in errors), Q())
    carry_energy = sum(value*value for value in carries)
    lower_margin = 289*energy-carry_energy
    upper_margin = carry_energy+256*errors[-1]**2-225*energy
    if lower_margin < 0 or upper_margin < 0:
        raise ArithmeticError("finite carry energy inequality failed")
    return {"errors": errors, "carries": carries, "energy": energy,
            "carry_energy": carry_energy, "lower_margin": lower_margin,
            "upper_margin": upper_margin}


def _dyadic_outward(low, high, bits=64):
    scale = 1 << bits
    left = (low.numerator*scale)//low.denominator
    right = -((-high.numerator*scale)//high.denominator)
    return Q(left, scale), Q(right, scale)


def _distance_interval(low, high):
    lower = Q(0) if low <= 0 <= high else min(abs(low), abs(high))
    return lower, max(abs(low), abs(high))


def interval_orbit_report(label, point_interval, shell, include_raw=True):
    """Rigorous, intentionally coarse first-mode loss bounds and exact carries."""
    _integer(shell, "shell", 1)
    lo, hi = map(Q, point_interval)
    if lo > hi:
        raise ValueError("reversed interval")
    loss_lo, loss_hi = Q(), Q()
    lifts, raw = [], []
    for n in range(shell, 2*shell):
        left, right = lo*16**n, hi*16**n
        k0, k1 = nearest_integer(left), nearest_integer(right)
        if k0 != k1:
            raise ArithmeticError(f"nearest integer remains ambiguous at {n}")
        lifts.append(k0)
        el, eh = _dyadic_outward(left-k0, right-k0)
        dl, dh = _distance_interval(el, eh)
        loss_lo += 8*dl*dl
        loss_hi += min(Q(2), 2*PI_HI*PI_HI*dh*dh)
        if include_raw:
            raw.append([n, str(el), str(eh)])
    carries = [b-16*a for a, b in zip(lifts, lifts[1:])]
    if any(abs(value) > 8 for value in carries):
        raise ArithmeticError("a balanced carry left [-8,8]")
    carry_energy = sum(value*value for value in carries)
    packet = {
        "label": label, "B": shell,
        "actual_mean_loss_enclosure": [str(loss_lo/shell), str(loss_hi/shell)],
        "nonzero_internal_balanced_carries": sum(value != 0 for value in carries),
        "balanced_carry_energy": carry_energy,
        "balanced_carries": carries,
        "carry_lower_bound_on_mean_loss": str(Q(8*carry_energy, 289*shell)),
        "carry_upper_bound_on_mean_loss": str(2*PI_HI**2*Q(carry_energy+64, 225*shell)),
        "nearest_integer_lifts_sha256": hashlib.sha256(
            "\n".join(hex(value) for value in lifts).encode()).hexdigest(),
    }
    if include_raw:
        packet["signed_phase_enclosures"] = raw
    return packet


def shallit_interval(cutoff):
    """Enclose sum_{k>=0}16^(-2^k); bound omitted powers by all later integers."""
    _integer(cutoff, "cutoff", 1)
    low, exponent = Q(), 1
    while exponent <= cutoff:
        low += Q(1, 16**exponent)
        exponent *= 2
    return low, low + Q(1, 15*16**(exponent-1))


def proper_null_states(depth):
    """Declared failed strengthening: the inherited proper null source / 8."""
    _integer(depth, "depth", 0)
    result = [Q()]
    for n in range(1, depth+1):
        forcing = sum((Q(a, 8*(8*(n-1)+j+1))
                       for j, a in enumerate(PROPER_NULL)), Q())
        result.append(16*result[-1]+forcing)
    return tuple(result)


def hostile_tail(t):
    _integer(t, "t")
    return Q(t, (8*t+1)*(8*t+3)*(8*t+5))


def hostile_state(t):
    return -hostile_tail(t)


def hostile_source(n):
    _integer(n, "n", 1)
    return 16*hostile_tail(n-1)-hostile_tail(n)


def hostile_integral_source(n):
    """Integral of z^(8n-8)*(16-z^8)*(-1+6z²-5z⁴)/64."""
    _integer(n, "n", 1)
    h = ((0, Q(-1, 64)), (2, Q(3, 32)), (4, Q(-5, 64)))
    return sum((a*(Q(16, 8*n-7+k)-Q(1, 8*n+1+k))
                for k, a in h), Q())


def cleared_source_trajectory(depth, completed_lifts):
    """Return actual integer Gamma-denominator residuals, never a new seed."""
    _integer(depth, "depth", 0)
    lifts = tuple(completed_lifts)
    if len(lifts) != depth+1 or any(type(k) is not int for k in lifts):
        raise ValueError("one integer lift is required for every n=0,...,depth")
    denominator, numerator = 1, 0
    rows = [(0, denominator, numerator, numerator-denominator*lifts[0])]
    for n in range(1, depth+1):
        p, q = source_polynomials(n)
        numerator = 16*q*numerator+p*denominator
        denominator *= q
        rows.append((n, denominator, numerator, numerator-denominator*lifts[n]))
    return tuple(rows)


def report():
    """Pure deterministic JSON-serializable report; all controls are finite."""
    margins = rational_certificates()
    gram_cases = 0
    for left in range(9):
        for right in range(9):
            witness = gram_minimizer(left, right)
            if witness["y"]-16*witness["x"] != 1:
                raise ArithmeticError("one-defect constraint failed")
            if sum((q*q for q in witness["states"]), Q()) != witness["energy"]:
                raise ArithmeticError("inverse Gram equality failed")
            k = max(left, right)
            if witness["denominator"] > 256+Q(255, 256**(k+1)-1):
                raise ArithmeticError("inverse Gram boundary estimate failed")
            gram_cases += 1
    depth = 2*max(FRESH_SHELLS)+24
    original_interval = completed_interval(depth)
    original = [interval_orbit_report("original_zero_selected_pi_over_16",
                                     original_interval, b) for b in FRESH_SHELLS]
    controls = []
    for label, point in (("coherent_changed_seed_completed_zero", Q()),
                         ("dyadic_alias_one_over_16", Q(1, 16)),
                         ("periodic_one_over_15", Q(1, 15))):
        controls.append(interval_orbit_report(label, (point, point), 43))
    for b in SHALLIT_SHELLS:
        controls.append(interval_orbit_report("Shallit_Kempner", shallit_interval(2*b+24), b))
    failed = []
    null_states = proper_null_states(64)
    for n in range(1, 65):
        if v2(null_states[n]) != v2(n):
            failed.append({"n": n, "U_n": str(null_states[n]),
                           "observed_v2": v2(null_states[n]), "candidate_v2": v2(n)})
    hostile_pairs = 0
    for s in range(-37, 38):
        for t in range(-37, s):
            if v2(hostile_state(s)-hostile_state(t)) != v2(s-t):
                raise ArithmeticError("hostile full 2-adic isometry failed")
            hostile_pairs += 1
    for n in range(1, 65):
        if hostile_source(n) != hostile_integral_source(n):
            raise ArithmeticError("hostile polynomial source mismatch")
        if hostile_state(n) != 16*hostile_state(n-1)+hostile_source(n):
            raise ArithmeticError("hostile source recurrence mismatch")
        if n >= 2 and hostile_source(n) <= 0:
            raise ArithmeticError("hostile eventual positivity failed")
    return {
        "status": "exact finite controls; asymptotic claims require the paper proofs",
        "source_base": "db9fb4b84672050efa79b13377f1e73364598a14",
        "pi_normality": "OPEN", "R0": "OPEN", "restricted_exponent_below_one": "OPEN",
        "rational_strict_margins": margins,
        "inverse_gram_cases": gram_cases,
        "relaxed_two_coordinate_energy": str(gram_minimizer(0, 0)["energy"]),
        "local_coefficient_global_mutation": {"q": "1/2", "actual_F": "2",
                                               "false_19q_squared": "19/4", "verdict": "REFUTED"},
        "original_completed_interval_depth": depth,
        "original_source_shells": original,
        "hostile_completed_controls": controls,
        "failed_conjectures": [{"claim": "proper null source / 8 has v2(U_n)=v2(n)",
                                "verdict": "REFUTED", "raw_failures": failed}],
        "nonproper_null_isometry_control": {
            "identity": "U_n=-n/((8n+1)(8n+3)(8n+5))", "completed_value": "0",
            "pairs_checked": hostile_pairs, "source_indices_checked": 64,
            "first_forcing": str(hostile_source(1)), "eventual_positive_from": 2,
            "source_degree": 12, "zero_seed": True,
            "first_forcing_positive": False, "original_four_poles": False,
            "proof_scope": "all integer pairs for the isometry; all n>=2 for positivity"},
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
