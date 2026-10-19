"""Prime-two normalized directional inverse on a FRESH high-mode holdout.

TARGET C of the Academic Main IV continuation frontier. The single number
that is supposed to "move S4" is the B-normalized minimum eigenvalue of the
#181 full-prime-two corrected first-window signed Schur lower, evaluated on a
high-mode window that was NOT used to fit the comparator metric B.

We read the two frozen #181 full-prime certificates
(research/2026-10-18/ROUND2_FULL_PRIME_J8.json  -> FIT window, M=80,
 research/2026-10-18/ROUND2_FULL_PRIME_J24.json -> HOLDOUT window, M=192).
The comparator metric B is the source high-mode Gram (continuum_residual_Gram)
of the FIT window; it is strictly positive definite, so the B-normalized
spectrum has the same sign pattern as the ordinary spectrum (independent-metric
cross check). The holdout corrected lower is old_lower + the single BETTER
enclosure of the operator excess C = D - kappa*I.

CRITICAL never-sum rule (Academic Main IV audit): the #181 center/edge
resolvent saving  C >= w0 (I - A_b)  (JSON key "gain") and the #182-style
directional inverse  C >= Z G^-1 Z*  (JSON key "source_inverse_saving_lower")
are BOTH lower bounds on the SAME excess C. They MUST NOT be added; adding them
is a refuted double-count. This module only ever uses a single enclosure (the
one with the larger exact Gershgorin floor) and raises if asked to use the sum.

Everything that enters a certificate is exact (fractions.Fraction). A negative
B-normalized min-eigenvalue is a VALID conservative lower that leaves the S4
first-window sign AMBIGUOUS; it is never a negative Weil witness and never a
statement about RH.
"""
import json
import os
import sys
from fractions import Fraction as F

from . import clamped_k_residual_bridge as B
from . import original_continuum_residual as R


class PrimeTwoHoldoutError(ValueError):
    pass


_HERE = os.path.dirname(os.path.abspath(__file__))
_RESEARCH = os.path.join(_HERE, os.pardir, "research", "2026-10-18")
FIT_CERTIFICATE = os.path.join(_RESEARCH, "ROUND2_FULL_PRIME_J8.json")
HOLDOUT_CERTIFICATE = os.path.join(_RESEARCH, "ROUND2_FULL_PRIME_J24.json")
_SECTORS = ("odd_derivative", "even_derivative")
_BUDGET_KEY = {"odd_derivative": "odd", "even_derivative": "even"}


def _raise_int_parse_limit(digits):
    """Only ever RAISE the process int<->str digit cap (0 means unlimited)."""
    if type(digits) is not int or digits < 1:
        raise PrimeTwoHoldoutError("positive digit budget")
    cur = sys.get_int_max_str_digits()
    if cur and cur < digits:
        sys.set_int_max_str_digits(digits)


def _mat(rows):
    m = tuple(tuple(F(v) for v in row) for row in rows)
    if len(m) != 2 or any(len(row) != 2 for row in m):
        raise PrimeTwoHoldoutError("source signed lower is 2x2")
    return m


def _strmat(m):
    return tuple(tuple(str(x) for x in row) for row in m)


def _add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def _sym(a, msg):
    if a[0][1] != a[1][0]:
        raise PrimeTwoHoldoutError(msg)


def _det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def _gershgorin_floor(a):
    """Exact rational lower bound on the smallest (ordinary) eigenvalue."""
    _sym(a, "signed 2x2 lower asymmetric")
    return min(a[0][0] - abs(a[0][1]), a[1][1] - abs(a[1][0]))


def _is_psd(a):
    _sym(a, "signed 2x2 lower asymmetric")
    return a[0][0] >= 0 and a[1][1] >= 0 and a[0][0] * a[1][1] >= a[0][1] * a[1][0]


def _load_certificate(path):
    with open(path, "r") as fh:
        raw = fh.read()
    # Every stored integer has fewer digits than the whole file.
    _raise_int_parse_limit(len(raw) + 64)
    data = json.loads(raw)
    if data.get("RH_proved") is not False:
        raise PrimeTwoHoldoutError("#181 certificate must assert RH_proved False")
    if data.get("source_blob") != R.SOURCE_SHA:
        raise PrimeTwoHoldoutError("certificate source provenance SHA mismatch")
    for key in ("J", "M", "P", "sectors", "source_high_budget_audit"):
        if key not in data:
            raise PrimeTwoHoldoutError("certificate missing field %r" % key)
    return data


def _sector_pieces(cert, sector):
    if sector not in cert["sectors"]:
        raise PrimeTwoHoldoutError("certificate missing sector %r" % sector)
    s = cert["sectors"][sector]
    old = _mat(s["old_lower"])
    gain = _mat(s["gain"])                         # C >= w0 (I - A_b)
    direct = _mat(s["source_inverse_saving_lower"])  # C >= Z G^-1 Z*
    published = _mat(s["new_lower"])               # #181 published = old + gain
    gram = _mat(s["continuum_residual_Gram"])      # high-mode source Gram
    for m, msg in ((old, "old"), (gain, "gain"), (direct, "direct"),
                   (published, "new"), (gram, "Gram")):
        _sym(m, "certificate %s block asymmetric" % msg)
    if _add(old, gain) != published:
        raise PrimeTwoHoldoutError("certificate new_lower != old_lower + gain")
    return {"old": old, "gain": gain, "direct": direct, "published": published,
            "gram": gram, "kappa": F(s["kappa"]), "w_floor": F(s["w_floor"])}


def build_comparator_B(fit_cert, sector):
    """Source-valid high metric B = FIT-window high-mode Gram (strictly PD)."""
    gram = _sector_pieces(fit_cert, sector)["gram"]
    if not (gram[0][0] > 0 and _det(gram) > 0):
        raise PrimeTwoHoldoutError("fit high-mode Gram metric B not positive definite")
    return gram


def better_single_enclosure(resolvent_saving, directional_saving):
    """Pick the BETTER single lower bound on C = D - kappa*I; NEVER the sum.

    Both arguments bound the same excess; the never-sum rule forbids adding
    them. Selection is by the larger exact Gershgorin floor.
    """
    fr = _gershgorin_floor(resolvent_saving)
    fd = _gershgorin_floor(directional_saving)
    if fd > fr:
        return directional_saving, "directional_inverse", fd
    return resolvent_saving, "center_edge_resolvent", fr


def reject_double_count(saving, resolvent_saving, directional_saving):
    """Guard: refuse any bound equal to resolvent + directional (double count)."""
    summed = _add(resolvent_saving, directional_saving)
    if saving == summed and summed != resolvent_saving and summed != directional_saving:
        raise PrimeTwoHoldoutError(
            "never-sum rule violated: C cannot be bounded by the summed "
            "resolvent + directional inverse (refuted double-count)")
    return saving


def b_normalized_spectrum(lower, metric_B):
    """Exact sign of the B-normalized spectrum of a symmetric 2x2 lower.

    For B PD, `lower` is PSD in the B metric iff it is PSD. The generalized
    eigenvalues solve  det(B) lam^2 - T lam + det(lower) = 0  with
    T = trace(B^-1 lower) * det(B). Decision is exact (det + trace signs); a
    rational LOWER bound on the min generalized eigenvalue is reported via a
    rigorous rational over-estimate of the discriminant square root.
    """
    _sym(lower, "signed lower asymmetric")
    _sym(metric_B, "metric asymmetric")
    detB = _det(metric_B)
    if detB <= 0 or metric_B[0][0] <= 0:
        raise PrimeTwoHoldoutError("B-normalized metric must be positive definite")
    detL = _det(lower)
    T = (lower[0][0] * metric_B[1][1] + lower[1][1] * metric_B[0][0]
         - lower[0][1] * metric_B[1][0] - lower[1][0] * metric_B[0][1])
    disc = T * T - 4 * detB * detL
    if disc < 0:
        raise PrimeTwoHoldoutError("symmetric pencil must have real spectrum")
    root_up = B.sqrt_up(disc)                       # rational >= sqrt(disc)
    min_eig_lower = (T - root_up) / (2 * detB)       # <= true min generalized eig
    psd = detL >= 0 and T >= 0                        # <=> both gen-eigs >= 0
    return {"det_metric_B": detB, "det_lower": detL, "trace_pencil_T": T,
            "discriminant": disc,
            "min_generalized_eigenvalue_rational_lower_bound": min_eig_lower,
            "psd_in_B_metric": psd,
            "min_eigenvalue_sign": "nonnegative" if psd else "negative",
            "RH_proved": False}


def _spectrum_strings(spec):
    return {"det_metric_B": str(spec["det_metric_B"]),
            "det_lower": str(spec["det_lower"]),
            "trace_pencil_T": str(spec["trace_pencil_T"]),
            "min_generalized_eigenvalue_rational_lower_bound":
                str(spec["min_generalized_eigenvalue_rational_lower_bound"]),
            "psd_in_B_metric": bool(spec["psd_in_B_metric"]),
            "min_eigenvalue_sign": spec["min_eigenvalue_sign"],
            "RH_proved": False}


def _source_attested_budget(cert, sector):
    audit = cert["source_high_budget_audit"][_BUDGET_KEY[sector]]
    return {"source_blob": audit["source_blob"],
            "prime_surplus_weight_floor":
                audit["prime_surplus_weight_floor"]["outward_lower"],
            "kappa_outward_lower": audit["kappa"]["outward_lower"],
            "prime_upper_outward_upper": audit["prime_upper"]["outward_upper"],
            "contact_upper_outward_upper": audit["contact_upper"]["outward_upper"],
            "negative_pole_upper_outward_upper":
                audit["negative_pole_upper"]["outward_upper"],
            "derivative_L2_gap_claimed": bool(audit["derivative_L2_gap_claimed"]),
            "RH_proved": False}


def prime_two_directional_holdout(fit_path=FIT_CERTIFICATE,
                                  holdout_path=HOLDOUT_CERTIFICATE,
                                  fit_cert=None, holdout_cert=None):
    """Evaluate the #181 prime-two corrected first-window lower on a holdout.

    B is fit on `fit_path` (default J8/M80); the corrected lower is evaluated on
    the DISTINCT holdout window `holdout_path` (default J24/M192). Expected
    honest outcome: the fresh-holdout B-normalized min-eigenvalue stays negative
    in both parity sectors, so the S4 first-window sign is uncertified and S4
    remains OPEN -- which REFUTES the hope that a fresh holdout flips the sign.
    """
    fit = fit_cert or _load_certificate(fit_path)
    hold = holdout_cert or _load_certificate(holdout_path)
    if (fit["J"], fit["M"], fit["P"]) == (hold["J"], hold["M"], hold["P"]):
        raise PrimeTwoHoldoutError(
            "holdout window must be distinct from the window used to fit B")

    sectors = {}
    any_psd_event = False
    all_psd = True
    for sec in _SECTORS:
        metric_B = build_comparator_B(fit, sec)
        hp = _sector_pieces(hold, sec)

        chosen, which, floor = better_single_enclosure(hp["gain"], hp["direct"])
        reject_double_count(chosen, hp["gain"], hp["direct"])
        corrected = _add(hp["old"], chosen)         # old + BETTER single bound

        spec_corrected = b_normalized_spectrum(corrected, metric_B)
        spec_published = b_normalized_spectrum(hp["published"], metric_B)

        # Independent-metric (ordinary, identity) recomputation as a cross check:
        # for B PD the B-metric verdict must agree with the plain PSD verdict.
        ordinary_psd = _is_psd(corrected)
        if ordinary_psd != spec_corrected["psd_in_B_metric"]:
            raise PrimeTwoHoldoutError(
                "B-metric and ordinary PSD verdicts disagree under PD metric")

        psd_here = spec_corrected["psd_in_B_metric"]
        all_psd = all_psd and psd_here
        any_psd_event = any_psd_event or psd_here

        sectors[sec] = {
            "source_kappa": str(hp["kappa"]),
            "inherited_prime2_surplus_weight_floor": str(hp["w_floor"]),
            "source_attested_budget": _source_attested_budget(hold, sec),
            "comparator_B_metric_fit_high_mode_Gram": _strmat(metric_B),
            "comparator_B_is_positive_definite": True,
            "resolvent_saving_Gershgorin_floor": str(_gershgorin_floor(hp["gain"])),
            "directional_inverse_saving_Gershgorin_floor":
                str(_gershgorin_floor(hp["direct"])),
            "chosen_single_enclosure": which,
            "chosen_enclosure_Gershgorin_floor": str(floor),
            "savings_were_never_summed": True,
            "corrected_holdout_first_window_Schur_lower": _strmat(corrected),
            "corrected_holdout_B_normalized_spectrum":
                _spectrum_strings(spec_corrected),
            "corrected_holdout_ordinary_PSD_cross_check": bool(ordinary_psd),
            "published_181_new_lower": _strmat(hp["published"]),
            "published_181_B_normalized_spectrum":
                _spectrum_strings(spec_published),
            "holdout_first_window_PSD": bool(psd_here),
            "RH_proved": False}

    return {
        "target": "C_prime_two_directional_holdout",
        "fit_window": {"J": fit["J"], "M": fit["M"], "P": fit["P"]},
        "holdout_window": {"J": hold["J"], "M": hold["M"], "P": hold["P"]},
        "fit_and_holdout_windows_distinct": True,
        "source_blob": hold["source_blob"],
        "comparator_B_is_fit_window_high_mode_Gram": True,
        "never_sum_rule_enforced": True,
        "lambda_power_is_log_p": True,
        "no_zeta_zero_ordinate_input": True,
        "parity_sectors": sectors,
        "fresh_holdout_first_window_S4_PSD": all_psd,
        "fresh_holdout_flips_S4_sign": any_psd_event,
        "S4_first_window_sign_certified": all_psd,
        "S4_sign_status": "FIRST_WINDOW_PSD_CERTIFIED" if all_psd else "OPEN",
        "status_label": "VERIFIED-EXACT-MODEL",
        "verdict": (
            "PSD event on fresh holdout: stress with independent metric before "
            "any claim (still only first-window, never RH)." if any_psd_event else
            "REFUTED: the fresh high-mode holdout does NOT flip the S4 first-"
            "window sign; the B-normalized minimum eigenvalue stays strictly "
            "negative in both parity sectors, so S4 remains OPEN."),
        "RH_proved": False}
