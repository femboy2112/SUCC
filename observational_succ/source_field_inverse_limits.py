"""SimpleField / IdealHard / FuckedField: source-indexed inverse-limit instruments.

Three separate questions:
    E: is the inverse limit mathematically inhabited?
    C: can the declared finite toolkit compute its particular witness?
    I: is the actual source history identifiable by the declared reports?

This module supplies EXECUTABLE EXACT FINITE CALIBRATIONS, not a decision
algorithm for these questions in unrestricted infinite systems.

Relevant classical imports:
- finite-branching Koenig/WKL; computable infinite binary trees can have
  no computable infinite path (Kleene diagonal tree).
- well-foundedness of natural numbers.
- inverse-limit coordinate projections jointly separate distinct points,
  even if a restricted observer report family does not.
- dense-core / bounded-operator finite negative witness principles.

RH remains open: original Weil high-sector positivity is NOT full sign.
No zeta-zero locations, fake primes, or physical observer access are inputs.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from fractions import Fraction as F


class FieldClosureError(ValueError):
    """Invalid source, closure assumptions, or advertised infinite proof."""


def _nat(n, *, cap=None):
    if type(n) is not int or n < 0 or (cap is not None and n > cap):
        raise FieldClosureError("Nonnegative exact integer within declared budget required")
    return n


@dataclass(frozen=True)
class FieldSourcePassport:
    source: str
    observer: str
    epoch: int = 0

    def __post_init__(self):
        if not isinstance(self.source, str) or not self.source.strip():
            raise FieldClosureError("A nonempty actual/model source label is required")
        if not isinstance(self.observer, str) or not self.observer.strip():
            raise FieldClosureError("A nonempty observer/probe closure is required")
        _nat(self.epoch)


def simple_residue_inverse_limit(seed, horizon=8):
    """Finite name and total query algorithm for x_n=seed mod 2^n.

    The mathematical global point is a 2-adic inverse-limit element.
    A finite source parameter and program compute ANY requested coordinate,
    and the elementary modular law proves compatibility for all n.
    We do NOT claim all infinitely many digits were physically emitted.
    """
    source=_nat(seed)
    n=_nat(horizon, cap=64)
    stages=tuple(source % (1 << k) for k in range(n + 1))
    if any(stages[k+1] % (1 << k) != stages[k] for k in range(n)):
        raise ArithmeticError("Finite residue model violates actual quotient maps")
    return {
        "source":"FIXED_NATURAL_INTEGER_EMBEDDED_IN_Z2",
        "observer":"ALL_QUOTIENT_RESIDUES",
        "finite_name":source,
        "observed_stages":stages,
        "all_levels_rule":"x_n = seed mod 2^n for every n>=0",
        "global_compatibility_by_modular_identity":True,
        "relative_to_declared_seed_unique":True,
        "uniform_requested_stage_algorithm":True,
        "all_infinite_coordinates_physically_executed":False,
        "field":"SimpleField",
        "RH_proved":False,
    }


def _normalize_halts(records):
    """Finite synthetic bounded-halting transcript, NOT a universal machine."""
    if type(records) not in (tuple, list):
        raise FieldClosureError("Finite declared U(e,e) stage records required")
    out={}
    for rec in records:
        if type(rec) not in (tuple, list) or len(rec)!=3:
            raise FieldClosureError("Use records (index, halt_step, binary_output)")
        i,t,b=rec
        _nat(i)
        if type(t) is not int or t<1 or type(b) is not int or b not in (0,1):
            raise FieldClosureError("Finite source records need positive time and binary value")
        if i in out:
            raise FieldClosureError("One definite bounded-halting record per index")
        out[i]=(t,b)
    return out


def _prefix_avoids_bounded_diagonal(bits, halts):
    n=len(bits)
    return all(not (i<n and t<=n and bits[i]==b)
               for i,(t,b) in halts.items())


def finite_kleene_tree_calibration(horizon, records=()):
    """Decidable finite toy trace of the Kleene diagonal tree law.

    TRUE IDEALHARD THEOREM (paper, not execution): take U(e,e) from a
    fixed acceptable UNIVERSAL numbering of all partial binary-valued
    computable functions. T contains s of length n if each U(e,e)
    observed to halt within n steps has s[e]!=U(e,e). Every level of T
    is nonempty; Koenig gives a path, but NO path is computable, since
    its own program index e would compute its e-th bit.

    This executable probe uses a supplied FINITE synthetic transcript,
    never pretends to have simulated the universal numbering or certified
    the absence of a computable path by bounded enumeration.
    """
    h=_nat(horizon,cap=11)
    logs=_normalize_halts(records)
    levels=[]
    for n in range(h+1):
        nodes=tuple("".join(str(b) for b in bits)
                    for bits in product((0,1),repeat=n)
                    if _prefix_avoids_bounded_diagonal(bits,logs))
        if not nodes:
            raise ArithmeticError("A finite diagonal tree level is unexpectedly empty")
        levels.append(nodes)
    if any(s[:-1] not in levels[n-1]
           for n in range(1,h+1) for s in levels[n]):
        raise ArithmeticError("Bounded-diagonal tree is not prefix closed")
    return {
        "source":"SYNTHETIC_FINITE_BOUNDED_DIAGONAL_TRANSCRIPT",
        "levels_sizes":tuple(len(x) for x in levels),
        "last_level_nodes":levels[-1],
        "finitely_branching":True,
        "every_checked_level_nonempty":True,
        "every_checked_node_has_valid_prefix":True,
        "mathematical_infinite_theorem_requires_universal_U_and_WKL":True,
        "finite_transcript_proves_no_computable_path":False,
        "classical_universal_U_theorem_has_no_computable_path":True,
        "classical_universal_U_tree_has_infinite_path":True,
        "field_if_universal_U_and_WKL":"IdealHard",
        "RH_proved":False,
    }


def noncompact_descending_field(depth):
    """Nonempty EVERY finite level but no global history; infinite branching.

    T is the tree of strictly decreasing finite tuples of naturals.
    For each depth n, (n-1,n-2,...,0) is valid, but any infinite
    decreasing natural sequence contradicts well-foundedness.
    This is a concrete FuckedField/IMPOSSIBLE witness, not a refutation
    of Koenig: the root has INFINITELY many immediate successors.
    """
    n=_nat(depth,cap=4096)
    witness=tuple(range(n-1,-1,-1))
    if not all(witness[k]>witness[k+1] for k in range(max(0,n-1))):
        raise ArithmeticError("Source noncompact strict decrease law violated")
    return {
        "source":"NATURAL_STRICTLY_DESCENDING_HISTORY",
        "finite_level":n,
        "finite_level_witness":witness,
        "all_finite_levels_have_such_witnesses":True,
        "branching_at_root_finite":False,
        "global_inverse_limit_nonempty":False,
        "global_no_path_proof":"No infinite strictly decreasing sequence of naturals",
        "field":"FuckedField/PROVED_NO_REALIZATION",
        "RH_proved":False,
    }


def hidden_coordinate_phantom(horizon):
    """Two fixed distinct lawful sources; even-bit observer never separates.

    X_n = {0,1}^(2n), bonds are prefix truncation.
    Actual x=000..., phantom y=010101... .
    Observer O_n keeps coordinates 0,2,...,2n-2. Its output agrees
    for EVERY n, not only for the first horizon we sample.
    All full projections DO distinguish by coordinate 1 at stage n=1.
    A newly justified odd-coordinate probe repairs the source map.
    """
    n=_nat(horizon,cap=128)
    actual="00"*n
    phantom="01"*n
    observed=lambda s:s[::2]
    return {
        "source":"FULL_BINARY_HISTORY_WITH_HIDDEN_ODD_COORDINATES",
        "observer":"EVEN_COORDINATES_ONLY",
        "full_actual_prefix":actual,
        "full_phantom_prefix":phantom,
        "even_reports_equal":observed(actual)==observed(phantom),
        "even_report":observed(actual),
        "full_projection_distinguishes_if_n_positive":n>=1,
        "all_n_even_only_nonseparating_by_symbolic_source_law":True,
        "first_hidden_odd_probe_distinguishes":n>=1,
        "source_rule_allows_both_histories":True,
        "field":"FuckedField/PROVED_OBSERVER_NONIDENTIFICATION",
        "finite_query_existence_implies_global_identity":False,
        "RH_proved":False,
    }


def moving_impostor(depth):
    """Quantifier-scope control: every finite prefix has another completion.

    x=000..., y_n agrees for n bits but differs at bit index n.
    This proves (forall n exists y_n) of bounded indistinguishability;
    it does NOT establish (exists y neq x for all n) permanent phantom.
    Full-prefix observations are jointly separating for fixed x,y.
    """
    n=_nat(depth,cap=4096)
    return {
        "source":"FULL_BINARY_CANTOR_INVERSE_LIMIT",
        "actual_prefix":"0"*(n+1),
        "moving_rival_prefix":"0"*n+"1",
        "reports_equal_up_to_depth":n,
        "next_full_prefix_separates":n+1,
        "forall_n_exists_rival_matching_first_n":True,
        "exists_one_fixed_rival_matching_all_prefixes":False,
        "full_prefix_observers_jointly_separate_points":True,
        "finite_uniform_identification_of_all_Cantor_points":False,
        "FuckedField_phantom_inferred":False,
        "RH_proved":False,
    }


def remote_negative_sign_shadow(probe_depth, negative_index):
    """Classical IH-01 control for bounded original-style operator probes.

    A+=I, A-=I-2|e_M><e_M| on ell²(N), with M=negative_index.
    Every compression to coordinates [0,..,k-1] is identical for k<=M,
    yet the fixed A- has a negative finite witness at k=M+1.
    The required witness depth has NO universal bound across M.
    This is not the actual Weil source operator or an RH negative zero.
    """
    k=_nat(probe_depth,cap=100000)
    M=_nat(negative_index,cap=100000)
    return {
        "source":"SYNTHETIC_DIAGONAL_SELFADJOINT_SIGN_CONTROL",
        "negative_coordinate_index":M,
        "observer_tested_first_k":k,
        "finite_compressions_appear_identical":k<=M,
        "negative_direction_is_visible":k>M,
        "actual_negative_eigenvalue":-1,
        "some_finite_distinguishing_observation_always_exists":True,
        "uniform_cutoff_independent_of_hidden_index_exists":False,
        "permanently_invisible_negative_direction":False,
        "RH_proved":False,
    }


def rh_inverse_limit_interface():
    """Report the genuine Tate/Suzuki frontier WITHOUT inferring RH status.

    Imported rigorous source paper theorems prove a K-positive high sector
    on the first-prime window and at each fixed radius with a finite
    moment cutoff; NO sign has been proved for the corresponding original
    low Schur matrices at ALL radii. Thus no license to brand the actual
    zeta Weil inverse system as impossible, computationally nonselectable,
    or observationally phantom without a discriminating theorem.
    """
    from .tate_suzuki_fourier_schur import source_first_prime_spectral_budget
    from .tate_suzuki_all_radii import all_radius_formal_high_certificate
    first=source_first_prime_spectral_budget(18)
    any_a=all_radius_formal_high_certificate(F(1,2),F(1))
    if not (first["true_prime_power_labels"]==(2,)
            and first["original_Weil_L2_gap_strict_lower"]>F(1,16)
            and any_a["finite_high_source_positive_for_this_radius"]):
        raise ArithmeticError("Original source high-sector provenance gate failed")
    return {
        "source":"SHA_PINNED_ORIGINAL_COMPLETED_ZETA_WEIL_SUZUKI",
        "first_prime_radius":F(1,2),
        "first_prime_legendre_high_rank":18,
        "first_prime_K_relative_high_coercivity_proved":True,
        "all_finite_radii_some_high_sector_coercivity_proved":True,
        "finite_stage_index_does_not_make_smooth_test_space_finite":True,
        "first_prime_actual_low_Schur_positive_certified":False,
        "all_radii_actual_low_Schur_positive_certified":False,
        "each_strict_negative_original_test_would_be_a_finite_mathematical_witness":True,
        "negative_witness_effectively_findable_requires_certified_dense_probe_enumeration":True,
        "uniform_finite_global_RH_positive_test_cutoff_proved":False,
        "global_Weil_positivity_or_RH_proved":False,
        "field_classification":"UNRESOLVED_TOOL_CLOSURE",
        "not_authorized_to_label_RH_FuckedField":True,
        "RH_proved":False,
    }
