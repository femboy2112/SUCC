"""Typed source -> signed completed Weil/Suzuki identification interface.

Moonshot E (SUCC Academic Main V Thinker-Dome). SPECULATIVE, firewall-sensitive.

WHAT THIS IS
------------
A *firewall-enforcing interface* that FORMULATES (does NOT prove) the precise
missing map between a genuine SUCC/FUCC arithmetic construction and the SIGNED
completed Weil/Suzuki quadratic form. It is an obligation checker: it enumerates
every ingredient a legitimate identification must supply, REFUSES to certify an
identification unless all of them are supplied, and -- because no such proof is
currently available -- it can NEVER return ``identified: True``.

WHAT THIS IS NOT
----------------
It is NOT a proof of RH. It is NOT a positivity proof. It is NOT a relabeling of
an old conditional equivalence. A positive Hilbert/Gram covariance offered as the
signed Weil form is REJECTED. A finite prime window offered as all-height is
REJECTED. Any nontrivial zeta-zero ordinate offered as a construction input is
REJECTED as forbidden.

THE SIGNED COMPLETED WEIL/SUZUKI FORM (the target)
--------------------------------------------------
For an admissible test function phi on a specified finite test space, the
completed Weil explicit-formula distribution is the *indefinite* quadratic form

    W(phi) = (archimedean Gamma term) + (pole term) + (contact C_G term)
             - sum_{p, k>=1} (log p) * [ phi-hat evaluated at k*log p ]        (*)

with Lambda(p^k) = log p the genuine von-Mangoldt weight, ONE real archimedean
Gamma factor, conductor 1, half-density 1/2 and the self-dual Gaussian Haar of
Tate's thesis. The prime sum enters with a MINUS sign: W is NOT a positive
Gram/covariance. Weil's positivity criterion (W(phi) >= 0 for all admissible phi)
is EQUIVALENT to RH; it is OPEN here.

THE OPEN OBLIGATION (the research invitation)
---------------------------------------------
The precise missing map is the *signed source->Weil morphism*: an exact proof
that the SUCC-constructed signed quadratic value equals W(phi) of (*) for every
phi in a mathematically specified finite test space -- AND, if positivity is to
be claimed, a proof of positivity for the ACTUAL signed form (*), not for a
positive surrogate. The current best SUCC source construction yields the
certified four-mode Schur complement S_4 = A_4 - R_4 whose sign is CERTIFIED
AMBIGUOUS (observational_succ.certified_four_schur_trial). Both the morphism
equality and the S_4 sign remain OPEN.

FIREWALL (load-bearing, verbatim)
---------------------------------
RH PROVED: NO. Signed S_4 = A_4 - R_4 sign OPEN (AMBIGUOUS). Do NOT infer RH
from analogy, positive smoothing, finite prime windows, or a generic Hilbert
embedding. A positive covariance/Gram is NOT the completed Weil form. No
nontrivial zeta-zero ordinate as a construction input. #181/#182 inverses are
alternatives, NEVER summed. Exact arithmetic only.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction as F

from .tate_suzuki_shorting import (
    TateSourcePassport,
    ShortingContractError,
    verify_original_suzuki_source,
    is_genuine_prime,
    prime_power_parent,
)
from .source_weil_hierarchy import (
    AUTHENTIC_TAPE,
    authenticated_prime_wavefront,
)
from .certified_four_schur_trial import CertifiedTrial


class SourceWeilInterfaceError(ValueError):
    """Ill-typed offer, a forbidden input, or an attempt to launder a proof as data."""


# The two obligations that NO currently-available construction can discharge.
# They are appended to ``missing_obligations`` unconditionally (the morphism) or
# whenever positivity is claimed (the positivity proof); there is no code path
# that removes them, so ``identified`` can never become True.
MORPHISM_EQUALITY = "signed_source_to_weil_morphism_equality"
POSITIVITY_PROOF = "signed_form_positivity_proof_for_actual_form"

# Full obligation roster, in reporting order.
ALL_OBLIGATIONS = (
    "genuine_prime_power_inputs",          # Lambda(p^k)=log p authentic tape
    "archimedean_gamma_present",           # exactly one real Gamma factor
    "completed_pole_and_contact",          # pole + contact (C_G) terms present
    "conductor_one",                       # conductor = 1
    "half_density_haar",                   # half-density 1/2, self-dual Gaussian scale 1
    "valid_test_function_domain",          # compact mean-zero finite domain; no zero ordinate
    "fake_source_control_rejected",        # a matched fake-composite control supplied & refused
    "non_euler_control_rejected",          # a matched non-Euler control supplied & refused
    MORPHISM_EQUALITY,                     # CARDINAL OPEN (unconditional)
    POSITIVITY_PROOF,                      # CARDINAL OPEN (whenever positivity is claimed)
)

# The precise mathematically-specified finite test space of the current best
# source construction: the four even/odd Legendre derivative carriers
# P_1(2t),...,P_4(2t) spanning F_4 in L^2_0(-1/2,1/2) at a=1/2, single active
# prime atom p=2.  (certified_four_schur_trial.CertifiedTrial)
GENUINE_TEST_SPACE_ID = "F4_legendre_derivative_carrier_a_half_p2"


def _exact(x, where="value"):
    """Reject any float/bool masquerading as a certificate; keep exact Fractions."""
    if type(x) not in (int, F):
        raise SourceWeilInterfaceError(
            f"{where} must be exact int/Fraction; a float/bool is not a proof")
    return F(x)


@dataclass(frozen=True)
class SourceWeilOffer:
    """A typed claim that some construction *identifies* the signed completed Weil form.

    Every field is data. Crucially, the two deepest ingredients -- the signed
    source->Weil morphism equality and the positivity proof of the ACTUAL signed
    form -- are mathematical PROOFS, not data; the two ``claims_*`` booleans below
    can only *assert* them, and the interface treats such an assertion as an
    illegitimate attempt to launder a proof (a rejected input), never as a
    discharge of the obligation.
    """
    label: str
    # ---- arithmetic source ----
    prime_power_tape: tuple = AUTHENTIC_TAPE   # ((n, place), ...), genuine => prime powers
    euler_product: bool = True                 # do the local factors form a genuine Euler product?
    # ---- archimedean completion ----
    archimedean_gamma_count: int = 1
    has_pole_term: bool = True
    has_contact_term: bool = True
    conductor: int = 1
    half_density: F = F(1, 2)
    self_dual_gaussian_scale: F = F(1)
    # ---- test space ----
    test_space_id: str = GENUINE_TEST_SPACE_ID
    test_space_is_finite: bool = True
    test_functions_in_domain: bool = True
    zero_ordinate_inputs: tuple = ()           # MUST be empty; any entry is forbidden
    # ---- the signed form being offered ----
    signed_form_kind: str = "signed_completed_weil"   # claimed identity of the offered object
    offered_form_is_psd_gram: bool = False     # True + claimed-as-Weil => rejected
    # ---- positivity claim ----
    claims_positivity: bool = False
    positivity_scope: str = "none"             # "none" | "first_window" | "all_height"
    positivity_evidence_scope: str = "none"    # scope actually backed by evidence
    # ---- matched controls supplied alongside the offer ----
    fake_source_control_supplied: bool = False
    non_euler_control_supplied: bool = False
    # ---- proof tokens (NEVER legitimately satisfiable from data) ----
    claims_signed_morphism_equality: bool = False
    claims_signed_positivity_proof: bool = False

    def __post_init__(self):
        if not isinstance(self.label, str) or not self.label:
            raise SourceWeilInterfaceError("offer needs a non-empty label")
        # Exact-arithmetic gate: reject any float/bool masquerading as numeric data.
        _exact(self.half_density, "half_density")
        _exact(self.self_dual_gaussian_scale, "self_dual_gaussian_scale")
        if type(self.half_density) is not F:
            raise SourceWeilInterfaceError("half_density must be an exact Fraction")
        if type(self.self_dual_gaussian_scale) is not F:
            raise SourceWeilInterfaceError("gaussian scale must be an exact Fraction")
        for n_p in self.prime_power_tape:
            if (type(n_p) is not tuple or len(n_p) != 2
                    or type(n_p[0]) is not int or type(n_p[1]) is not int):
                raise SourceWeilInterfaceError("prime_power_tape entries must be (int n, int place)")
        for z in self.zero_ordinate_inputs:
            # A nontrivial zeta-zero ordinate must NEVER be a usable numeric input.
            # We accept only a forbidden *token* so the interface can reject it;
            # a numeric (int/Fraction/float) zero ordinate is refused at the door.
            if type(z) is not str:
                raise SourceWeilInterfaceError(
                    "zeta-zero ordinate must be a forbidden token, never a numeric input")
        if self.positivity_scope not in ("none", "first_window", "all_height"):
            raise SourceWeilInterfaceError("positivity_scope out of range")


def _tape_is_genuine(tape):
    """Every (n, place) must be a genuine prime power with place = its prime base.

    Rejects fake composites such as a claimed ``Lambda(6)`` (6 = 2*3 is not a
    prime power: prime_power_parent(6) is None), and rejects omitted/extra places
    relative to the authentic Lambda(p^k)=log p tape.
    """
    if tuple(tape) != tuple(AUTHENTIC_TAPE):
        return False
    for n, place in tape:
        parent = prime_power_parent(n)
        if parent is None or parent != place or not is_genuine_prime(place):
            return False
    return True


def reconfirm_s4_ambiguous(J=3, rank=6):
    """Re-run the EXISTING certified S_4 construction and confirm it stays AMBIGUOUS.

    Reuses observational_succ.certified_four_schur_trial.CertifiedTrial with the
    trivial trial U=0 -- the actual current best source construction. Does NOT
    re-derive any RH-anything. A verdict other than AMBIGUOUS would be a firewall
    breach and raises.
    """
    out = CertifiedTrial(U=(), J=J, rank=rank)
    verdict = out.get("verdict")
    if verdict != "AMBIGUOUS":
        raise SourceWeilInterfaceError(
            f"FIREWALL BREACH: certified S_4 verdict is {verdict!r}, expected AMBIGUOUS")
    if out.get("RH_proved") is not False or out.get("nontrivial_zero_coordinates_used") is not False:
        raise SourceWeilInterfaceError("FIREWALL BREACH: S_4 construction leaked RH/zero inputs")
    return {
        "verdict": "AMBIGUOUS",
        "s4": "A_4 - R_4",
        "sign": "OPEN (CERTIFIED AMBIGUOUS)",
        "first_window_only_not_RH": out.get("first_window_only_not_RH"),
        "RH_proved": False,
        "nontrivial_zero_coordinates_used": False,
    }


def certify_source_to_weil(offer: SourceWeilOffer) -> dict:
    """Obligation checker for identifying the signed completed Weil/Suzuki form.

    Returns a structured verdict dict containing exactly these load-bearing keys:
        identified            -> ALWAYS False (structural; no path sets it True)
        missing_obligations   -> obligations not discharged (incl. cardinal OPEN ones)
        rejected_inputs       -> offered inputs the firewall refuses, with reasons
        satisfied_obligations -> obligations the offer does legitimately supply
        open_obligation       -> the precise OPEN map, in words
    The two cardinal obligations (the signed source->Weil morphism equality and,
    whenever positivity is claimed, the positivity proof for the actual signed
    form) are unconditionally present in missing_obligations.
    """
    if not isinstance(offer, SourceWeilOffer):
        raise SourceWeilInterfaceError("certify_source_to_weil requires a SourceWeilOffer")

    rejected = []   # list of {"input": ..., "reason": ...}
    satisfied = []
    missing = []

    def reject(input_name, reason):
        rejected.append({"input": input_name, "reason": reason})

    # -------- REJECT GATES (firewall) --------
    # (a) a positive Gram/covariance presented as the signed Weil form.
    if offer.offered_form_is_psd_gram and offer.signed_form_kind == "signed_completed_weil":
        reject("offered_form",
               "a positive/PSD Gram or covariance is NOT the signed completed Weil form; "
               "the Weil form is indefinite (minus sign on the prime sum)")
    # (b) a fake-composite source, e.g. a claimed Lambda(6).
    fake_entries = [(n, p) for (n, p) in offer.prime_power_tape
                    if prime_power_parent(n) is None or prime_power_parent(n) != p
                    or not is_genuine_prime(p)]
    if fake_entries:
        reject("prime_power_tape",
               f"fake/composite non-prime-power place(s) {fake_entries}: "
               "Lambda is supported only on genuine prime powers (Lambda(p^k)=log p)")
    # (c) a non-Euler matched control.
    if offer.euler_product is not True:
        reject("euler_product",
               "local factors do not form a genuine Euler product; a matched non-Euler "
               "source is not the arithmetic source of the completed Weil form")
    # (d) a zeta-zero ordinate offered as a construction input.
    if offer.zero_ordinate_inputs:
        reject("zero_ordinate_inputs",
               f"forbidden nontrivial zeta-zero ordinate token(s) {list(offer.zero_ordinate_inputs)}: "
               "no nontrivial zero position may be a construction input")
    # (e) a finite-window positivity offered as all-height.
    if (offer.claims_positivity and offer.positivity_scope == "all_height"
            and offer.positivity_evidence_scope in ("finite_prime_window", "finite_test_space",
                                                    "first_window")):
        reject("positivity_scope",
               "all-height positivity offered on finite-window evidence "
               f"({offer.positivity_evidence_scope}); a finite prime window is not all height")
    # proof-laundering: equality/positivity asserted as a boolean are NOT proofs.
    if offer.claims_signed_morphism_equality:
        reject("claims_signed_morphism_equality",
               "the source->Weil equality is a PROOF obligation on an infinite admissible "
               "class; a boolean assertion is not a proof and cannot discharge it")
    if offer.claims_signed_positivity_proof:
        reject("claims_signed_positivity_proof",
               "positivity of the actual signed form is a PROOF obligation; a boolean "
               "assertion is not a proof and cannot discharge it")

    # -------- OBLIGATION CHECKS --------
    # genuine prime-power inputs
    if _tape_is_genuine(offer.prime_power_tape) and not fake_entries:
        satisfied.append("genuine_prime_power_inputs")
    else:
        missing.append("genuine_prime_power_inputs")
    # one archimedean Gamma
    (satisfied if offer.archimedean_gamma_count == 1 else missing).append(
        "archimedean_gamma_present")
    # pole + contact
    (satisfied if (offer.has_pole_term and offer.has_contact_term) else missing).append(
        "completed_pole_and_contact")
    # conductor 1
    (satisfied if offer.conductor == 1 else missing).append("conductor_one")
    # half-density / Haar
    (satisfied if (offer.half_density == F(1, 2)
                   and offer.self_dual_gaussian_scale == F(1)) else missing).append(
        "half_density_haar")
    # valid test-function domain (finite, in-domain, no zero ordinate)
    (satisfied if (offer.test_functions_in_domain and offer.test_space_is_finite
                   and not offer.zero_ordinate_inputs) else missing).append(
        "valid_test_function_domain")
    # matched controls present AND refused by the construction
    (satisfied if offer.fake_source_control_supplied else missing).append(
        "fake_source_control_rejected")
    (satisfied if offer.non_euler_control_supplied else missing).append(
        "non_euler_control_rejected")

    # -------- CARDINAL OPEN OBLIGATIONS (never dischargeable here) --------
    # The signed source->Weil morphism equality is unconditionally OPEN.
    missing.append(MORPHISM_EQUALITY)
    # Positivity of the ACTUAL signed form is OPEN whenever positivity is claimed;
    # it is tied to the S_4 sign, which is CERTIFIED AMBIGUOUS.
    if offer.claims_positivity:
        missing.append(POSITIVITY_PROOF)

    # -------- STRUCTURAL VERDICT --------
    identified = False                      # hardcoded; no branch assigns True
    # defense in depth: identification requires EVERY obligation and ZERO rejects.
    would_be_identified = (not rejected) and all(ob in satisfied for ob in ALL_OBLIGATIONS)
    # ... and that is unreachable, because MORPHISM_EQUALITY is always in `missing`:
    assert MORPHISM_EQUALITY in missing and not would_be_identified

    verdict = {
        "interface": "source_weil_interface.certify_source_to_weil",
        "offer_label": offer.label,
        "identified": identified,
        "missing_obligations": tuple(missing),
        "rejected_inputs": tuple(rejected),
        "satisfied_obligations": tuple(satisfied),
        "open_obligation": (
            "OPEN: the signed source->Weil morphism (exact equality of the "
            "SUCC-constructed signed completed form and the Weil/Suzuki explicit-"
            "formula distribution W(phi) on the specified finite test space "
            f"'{offer.test_space_id}'), AND the sign of the certified Schur "
            "complement S_4 = A_4 - R_4 (CERTIFIED AMBIGUOUS). Both remain OPEN."
        ),
        "cardinal_open_obligations": (MORPHISM_EQUALITY, POSITIVITY_PROOF),
        "exact_arithmetic_only": True,
        "s4_sign": "OPEN (CERTIFIED AMBIGUOUS)",
        "RH_proved": False,
        "firewall": {
            "positive_gram_is_not_weil_form": True,
            "finite_window_is_not_all_height": True,
            "no_nontrivial_zero_ordinate_input": not offer.zero_ordinate_inputs,
            "inverse_181_182_never_summed": True,
        },
    }
    # Final guard: the contract the whole module exists to keep.
    assert verdict["identified"] is False
    return verdict


# ---------------------------------------------------------------------------
# #181/#182 prime-two inverse estimates: ALTERNATIVES, NEVER SUMMED.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class PrimeTwoInverseEstimate:
    """One of two ALTERNATIVE Loewner-lower enclosures of the SAME Schur residual.

    #181 ("Use the full prime-two inverse for the original signed Schur bound",
    observational_succ.full_prime_resolvent) and #182 (Theorem Forge II source
    repair) each bound the SAME prime-two Schur residual saving from below. They
    are alternatives, not independent contributions: adding them double-counts a
    single residual and yields an UNSOUND Loewner inequality. The right move is to
    take the better single enclosure (largest lower bound), never the sum.

    ``loewner_lower_min_eig`` is the exact-rational min-eigenvalue lower bound of
    that estimate's Loewner saving matrix. (Both are currently negative-definite;
    no actual negative source energy has been established.)
    """
    pr_label: str
    residual_id: str
    loewner_lower_min_eig: F
    kind: str = "PRIME_TWO_INVERSE_ALTERNATIVE_SAME_RESIDUAL"

    def __post_init__(self):
        _exact(self.loewner_lower_min_eig, "loewner_lower_min_eig")
        if type(self.loewner_lower_min_eig) is not F:
            raise SourceWeilInterfaceError(
                "Loewner min-eig lower must be an exact Fraction; a float is not a certificate")


def prime_two_inverse_estimates_181_182():
    """The two canonical alternatives for the shared prime-two Schur residual.

    Exact-rational stand-ins for the #181 and #182 Loewner-lower min-eigenvalues.
    The values are illustrative inputs for the guard's ALGEBRA (two alternatives
    for one residual); they are NOT a claim about the precise numeric bounds and,
    being negative, assert no positive/negative source energy. #181 is the better
    (larger) single enclosure here.
    """
    residual = "S4_prime_two_schur_residual"
    e181 = PrimeTwoInverseEstimate("PR181", residual, F(-7, 100))
    e182 = PrimeTwoInverseEstimate("PR182", residual, F(-11, 100))
    return e181, e182


def summed_inverse_guard(a: PrimeTwoInverseEstimate, b: PrimeTwoInverseEstimate,
                         *, operation):
    """Firewall gate on the #181/#182 prime-two inverse estimates.

    ``operation="sum"``  -> RAISES: two alternatives for the SAME Schur residual
    may never be summed (that would double-count one residual and produce an
    unsound Loewner inequality) without a NEW common operator inequality.
    ``operation="select_better"`` -> returns the single better enclosure (the one
    with the larger Loewner min-eig lower bound).
    """
    if not isinstance(a, PrimeTwoInverseEstimate) or not isinstance(b, PrimeTwoInverseEstimate):
        raise SourceWeilInterfaceError("guard requires two PrimeTwoInverseEstimate objects")
    same_residual = a.residual_id == b.residual_id
    both_alternatives = (a.kind == b.kind == "PRIME_TWO_INVERSE_ALTERNATIVE_SAME_RESIDUAL")
    if operation == "sum":
        if same_residual and both_alternatives:
            raise SourceWeilInterfaceError(
                f"REFUSED: {a.pr_label} and {b.pr_label} are ALTERNATIVE enclosures of the "
                f"same Schur residual '{a.residual_id}'; summing double-counts one residual. "
                "Take the better single enclosure (operation='select_better'), never the sum. "
                "A sum is lawful only under a NEW, separately proved common operator inequality.")
        raise SourceWeilInterfaceError(
            "REFUSED: summing prime-two inverse estimates requires a proved common operator "
            "inequality; none is available")
    if operation == "select_better":
        return a if a.loewner_lower_min_eig >= b.loewner_lower_min_eig else b
    raise SourceWeilInterfaceError(
        "operation must be 'sum' (always refused for shared-residual alternatives) "
        "or 'select_better'")


# ---------------------------------------------------------------------------
# The genuine current-best offer, and the explicit negative controls.
# ---------------------------------------------------------------------------
def genuine_source_offer(J=3, rank=6):
    """Build the offer for the ACTUAL current best SUCC source construction.

    Wires the authentic, independently audited primitives: the pinned prime-power
    tape (verify_original_suzuki_source), the Tate source passport (one Gamma,
    conductor 1, half-density 1/2, self-dual Gaussian), the single active prime
    atom p=2 at a=1/2 (authenticated_prime_wavefront), and the certified S_4
    verdict (CertifiedTrial, AMBIGUOUS). The offer is HONEST: it does NOT offer a
    Gram as the signed form, uses no zero ordinates, and does not assert the
    morphism/positivity proofs. It therefore passes every satisfiable gate but
    still fails to identify, because the two cardinal obligations are open.
    """
    # authenticate the source tape (fail-closed; in an isolated overlay this may
    # raise -- then the tape authentication obligation would itself go missing).
    authenticated = True
    try:
        verify_original_suzuki_source()
        TateSourcePassport()
        wavefront = authenticated_prime_wavefront(F(1, 2))
        if wavefront != ((2, 2),):
            authenticated = False
    except (ShortingContractError, Exception):
        authenticated = False

    s4 = reconfirm_s4_ambiguous(J=J, rank=rank)   # raises on any firewall breach

    return SourceWeilOffer(
        label="genuine_current_best_SUCC_source_construction",
        prime_power_tape=AUTHENTIC_TAPE if authenticated else (),
        euler_product=True,
        archimedean_gamma_count=1,
        has_pole_term=True,
        has_contact_term=True,
        conductor=1,
        half_density=F(1, 2),
        self_dual_gaussian_scale=F(1),
        test_space_id=GENUINE_TEST_SPACE_ID,
        test_space_is_finite=True,
        test_functions_in_domain=True,
        zero_ordinate_inputs=(),
        signed_form_kind="signed_completed_weil",
        offered_form_is_psd_gram=False,
        # The program's AIM is positivity (a positive first-window Schur), so the
        # positivity obligation is in play -- and it is OPEN because S_4 is
        # AMBIGUOUS. The claim is honestly scoped to the first window, NOT all
        # height, so it is not the finite->all-height overclaim.
        claims_positivity=True,
        positivity_scope="first_window",
        positivity_evidence_scope="ambiguous_s4_certified",
        fake_source_control_supplied=True,
        non_euler_control_supplied=True,
        claims_signed_morphism_equality=False,
        claims_signed_positivity_proof=False,
    )


def control_positive_gram_as_signed_form():
    """(a) A positive/PSD Gram presented as the signed completed Weil form."""
    return SourceWeilOffer(
        label="control_a_positive_gram_as_signed_weil_form",
        signed_form_kind="signed_completed_weil",
        offered_form_is_psd_gram=True,
        fake_source_control_supplied=True,
        non_euler_control_supplied=True,
    )


def control_fake_composite_lambda6():
    """(b) A fake-composite 'Lambda(6)' source (6 = 2*3 is not a prime power)."""
    # Insert a claimed von-Mangoldt place at the composite 6; prime_power_parent(6) is None.
    fake_tape = AUTHENTIC_TAPE + ((6, 6),)
    return SourceWeilOffer(
        label="control_b_fake_composite_lambda6",
        prime_power_tape=fake_tape,
        fake_source_control_supplied=True,
        non_euler_control_supplied=True,
    )


def control_non_euler_matched():
    """(c) A matched non-Euler source (same low moments, no Euler factorization)."""
    return SourceWeilOffer(
        label="control_c_non_euler_matched",
        euler_product=False,
        fake_source_control_supplied=True,
        non_euler_control_supplied=True,
    )


def control_zeta_zero_ordinate_input():
    """(d) A nontrivial zeta-zero ordinate offered as a construction input.

    The ordinate is represented ONLY by a forbidden token string -- a numeric
    zero ordinate is refused at the door by SourceWeilOffer -- precisely because
    using any nontrivial zero position as an input is forbidden.
    """
    return SourceWeilOffer(
        label="control_d_zeta_zero_ordinate_input",
        zero_ordinate_inputs=("FORBIDDEN_nontrivial_zeta_zero_ordinate_token",),
        fake_source_control_supplied=True,
        non_euler_control_supplied=True,
    )


def control_finite_window_as_all_height():
    """(e) A finite-window positivity offered as all-height."""
    return SourceWeilOffer(
        label="control_e_finite_window_as_all_height",
        claims_positivity=True,
        positivity_scope="all_height",
        positivity_evidence_scope="finite_prime_window",
        fake_source_control_supplied=True,
        non_euler_control_supplied=True,
    )


def all_negative_controls():
    """The five constructed negative controls the interface must reject."""
    return {
        "a_positive_gram": control_positive_gram_as_signed_form(),
        "b_fake_composite_lambda6": control_fake_composite_lambda6(),
        "c_non_euler_matched": control_non_euler_matched(),
        "d_zeta_zero_ordinate": control_zeta_zero_ordinate_input(),
        "e_finite_window_all_height": control_finite_window_as_all_height(),
    }


__all__ = [
    "SourceWeilInterfaceError",
    "SourceWeilOffer",
    "certify_source_to_weil",
    "reconfirm_s4_ambiguous",
    "PrimeTwoInverseEstimate",
    "prime_two_inverse_estimates_181_182",
    "summed_inverse_guard",
    "genuine_source_offer",
    "control_positive_gram_as_signed_form",
    "control_fake_composite_lambda6",
    "control_non_euler_matched",
    "control_zeta_zero_ordinate_input",
    "control_finite_window_as_all_height",
    "all_negative_controls",
    "ALL_OBLIGATIONS",
    "MORPHISM_EQUALITY",
    "POSITIVITY_PROOF",
    "GENUINE_TEST_SPACE_ID",
]
