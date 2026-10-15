"""Field trichotomy as SOURCE/TARGET/TOOLKIT-RELATIVE mathematical contracts.

SimpleField   = finite SOURCE-FAITHFUL symbolic compiler for a requested
                global value/representation plus proof of its full law.
IdealHard    = mathematically proven global existence, but no computable
                witness selector in the declared effective source toolkit.
FuckedField  = no compatible global model in the specified class, OR
                source identities remain nonseparable under the permitted
                observational closure. These are DIFFERENT failure modes.

A semantic label is NEVER inferred from finite positive tests. The finite
algorithms below calibrate independently PROVED infinite statements, including
a computable binary Kleene tree with no computable infinite path.

The labels are TARGET RELATIVE, NOT claims about the intrinsic difficulty
or undecidability of RH. No nontrivial zeta-zero information is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt

from .tate_observer_completion import (
    AtomicDescentError,integer_source_prefix,profinite_ghost_prefix,
    ghost_profinite_residue,
)
from .observer_global_sign_gate import exact_scalar_schur_source_gate,dense_smooth_source_gate


class FieldLimitError(ValueError):
    """Malformed target, source/toolkit contract, or finite-stage witness."""


@dataclass(frozen=True)
class FieldClassification:
    """Proof-ledger coordinates; one coarse label does NOT replace them."""
    classification: str
    source: str
    target: str
    toolkit: str
    finite_symbolic_law: bool
    proved_global_existence: bool | None
    computable_global_witness: bool | None
    source_identifiable_from_finite_reports: bool | None
    global_uniqueness: bool | None
    proof_boundary: str
    RH_proved: bool = False


def simple_symbolic_padic_one(depth:int)->dict:
    """Uniform finite program n -> 1 mod 2^n; not infinite enumeration.

    Finite code + mathematical induction constructs ONE specified 2-adic
    source point (the diagonal rational integer 1 in Z_2). The entire
    inverse limit is much larger and cannot be printed as finite atoms.
    """
    if type(depth) is not int or not 1<=depth<=256:
        raise FieldLimitError("Finite positive source-resolution request")
    modulus=1<<depth
    value=1%modulus
    if value!=1:
        raise ArithmeticError("Simple original source modulus law violated")
    return {
        "stage":depth,"modulus":modulus,"value":value,
        "symbolic_program":"f(n)=1 modulo 2**n, all n>=1",
        "source_compatible_every_stage":"PROVED_BY_DIVISIBILITY",
        "finite_representation_not_finite_materialization":True,
        "whole_profinite_carrier_enumerated":False,
        "classification":"SIMPLE_FOR_THE_DECLARED_SOURCE_POINT",
        "RH_proved":False,
    }


def _cantor_unpair(e:int)->tuple[int,int]:
    """Exact inverse of pairing e=(a+b)(a+b+1)/2+b."""
    if type(e) is not int or not 0<=e<=65535:
        raise FieldLimitError("Bounded enumerated program index 0..65535")
    s=(isqrt(8*e+1)-1)//2
    b=e-s*(s+1)//2
    a=s-b
    if a<0 or b<0 or (a+b)*(a+b+1)//2+b!=e:
        raise ArithmeticError("Computable TM enumeration pairing broken")
    return a,b


def bounded_binary_turing_diagonal(program_index:int,steps:int)->int|None:
    """Genuine bounded execution of a fixed explicit universal TM NUMBERING.

    Every binary finite-state two-way tape TM with unary input is included.
    Index e -> Cantor-unpair(e)=(nstate-1,table_integer);
    radix 4*nstate+2 encodes 2*nstate transitions. Actions 0,1
    halt with output bits 0,1. Others encode (write 0/1, move L/R,
    next-state in [0,nstate)). Input is unary 1**e followed by blank 0.
    This enumeration represents all partial computable unary->bit maps.
    An ordinary finite observer can execute steps, but cannot decide
    nonhalting at unbounded time.
    """
    a,b=_cantor_unpair(program_index)
    if type(steps) is not int or not 0<=steps<=4096:
        raise FieldLimitError("Declared finite simulator time budget 0..4096")
    states=a+1
    radix=4*states+2
    head=0
    state=0
    overwritten:dict[int,int]={}
    for _ in range(steps):
        read=overwritten.get(head, int(0<=head<program_index))
        if read not in (0,1):
            raise ArithmeticError("TM source violated binary tape")
        digit=(b//radix**(2*state+read))%radix
        if digit<=1:
            return digit
        transition=digit-2
        nextstate=transition%states
        direction=(transition//states)%2
        write=(transition//(2*states))%2
        overwritten[head]=write
        head+=1 if direction else -1
        state=nextstate
    return None


def kleene_source_tree_accepts(prefix:tuple[int,...])->bool:
    """Decidable membership in a computable finitely-branching binary tree.

    A word sigma of length n is valid iff for every e<n:
    if TM_e(e) HALTS within n steps with output b, sigma[e] != b.
    The tree is prefix-closed; every level has a node. Classical
    diagonal argument proves NO computable infinite path exists.
    """
    if (type(prefix) is not tuple or len(prefix)>64 or
            any(type(bit) is not int or bit not in (0,1) for bit in prefix)):
        raise FieldLimitError("Finite exact binary source observer prefix <=64")
    n=len(prefix)
    for e,bit in enumerate(prefix):
        result=bounded_binary_turing_diagonal(e,n)
        if result is not None and bit==result:
            return False
    return True


def kleene_finite_stage(depth:int)->dict:
    """Finite witness at any one bounded depth, NOT a coherent path algorithm.

    For each e<depth choose the complement of output if its machine halts
    within depth steps; otherwise choose 0. This prefix satisfies the
    current source law. Later observations can invalidate this choice;
    treating successive finite witnesses as one path is unsound.
    """
    if type(depth) is not int or not 0<=depth<=64:
        raise FieldLimitError("Bounded explicitly decidable finite stage 0..64")
    choices=tuple(1-v if (v:=bounded_binary_turing_diagonal(e,depth)) is not None
                  else 0 for e in range(depth))
    if not kleene_source_tree_accepts(choices):
        raise ArithmeticError("Finite source tree stage consistency broken")
    return {"depth":depth,"prefix":choices,
            "finite_prefix_source_verified":True,
            "infinite_stage_choice_algorithm_produced":False,
            "global_nonempty":"CLASSICAL_DIAGONAL_COMPLEMENT_EXISTENCE_PROOF",
            "every_computable_infinite_path_excluded":"PROVED_BY_TM_DIAGONALIZATION",
            "mathematical_witness_must_be_noncomputable":True,
            "RH_proved":False}


def finite_prefix_versus_global_path(depth:int)->dict:
    """Explicit finite TREE controls and the proof's quantifier boundary.

    All finite levels have a member (indeed constructible at that depth).
    No algorithm computes a compatible entire infinite member, because
    the TM enumeration would diagonalize against its own bit function.
    This is an IDEALHARD exemplar, not a claim that every proof is hard.
    """
    stage=kleene_finite_stage(depth)
    zeros=tuple(0 for _ in range(depth))
    return {"stage":depth,"valid_source_prefix":stage["prefix"],
            "all_zero_candidate_valid":kleene_source_tree_accepts(zeros),
            "finite_membership_decidable":True,
            "finite_fanout":2,
            "mathematical_global_path_exists":True,
            "global_path_computable":False,
            "finite_symbolic_program_for_a_global_path":False,
            "theorem":"KLEENE_COMPUTABLE_TREE_WITHOUT_COMPUTABLE_PATH",
            "classification":"IDEALHARD_FOR_COMPUTABLE_PATH_SELECTOR",
            "RH_proved":False}


def noncompact_escape_prefix(horizon:int)->dict:
    """Fucked NONEXISTENCE witness: X_n={m in N: m>=n}, maps inclusions.

    Every finite prefix X_1 <- ... <- X_horizon has global integer
    witness m=horizon. But an inverse-limit element would be ONE fixed
    m>=n for ALL n, impossible by Archimedean unboundedness of N.
    The stages are infinite discrete / noncompact; compact König
    hypotheses MUST NOT be silently applied.
    """
    if type(horizon) is not int or not 1<=horizon<=1000000:
        raise FieldLimitError("Finite positive noncompact stage horizon")
    return {"last_stage":horizon,
            "finite_source_witness":horizon,
            "witness_satisfies_every_prior_stage":True,
            "individual_stages_nonempty":True,
            "infinite_source_limit_exists":False,
            "noncompact_stage_law":"X_n={m in N: m>=n}, all bonds identity",
            "compact_Konig_hypotheses_satisfied":False,
            "classification":"FUCKED_EMPTY_LIMIT_FOR_DECLARED_NONCOMPACT_SOURCE",
            "RH_proved":False}


def phantom_source_prefix(depth:int)->dict:
    """Fucked IDENTIFICATION gap: every finite ghost prefix matches an integer.

    The coherent noninteger point x in Zhat has x_2=1 and x_p=0 for
    every odd p. Every finite set of residue observations is jointly
    matched by a (generally DIFFERENT) ordinary integer CRT witness.
    There is NO fixed ordinary integer matching the entire tower.

    Important quantifiers: forall depth exists integer matching, but
    NOT exists integer forall depth. This is NOT a permanently
    indistinguishable FIXED pair under a separating complete tower.
    """
    if type(depth) is not int or not 1<=depth<=4:
        raise FieldLimitError("Bounded factorial CRT source horizon 1..4")
    ghost=profinite_ghost_prefix(depth)
    rep=ghost.residues[-1]
    ordinary=integer_source_prefix(rep,depth)
    if ghost.residues!=ordinary.residues:
        raise ArithmeticError("Ordinary integer fails source prefix impersonation")
    return {
        "level":depth,"coarse_integer_representative":rep,
        "ghost_finite_source_reports":ghost.residues,
        "matching_integer_reports":ordinary.residues,
        "all_finite_prefixes_have_original_integer_witness":
            "PROVED_BY_CRT_FOR_EVERY_FINITE_STAGE",
        "one_original_integer_realizes_all_levels":False,
        "the_source_global_profinite_point_exists":True,
        "original_integer_source_property_finitely_refutable":False,
        "fixed_integer_and_ghost_equivalent_at_all_levels":False,
        "classification":"FUCKED_RELATIVE_TO_FINITE_INTEGER_SOURCE_IDENTIFICATION",
        "RH_proved":False,
    }


def nonfaithful_toolkit_pair(word_length:int)->dict:
    """Fucked OBSERVATIONAL NONINJECTIVITY even with arbitrary action depth.

    Source S={(x,t):x,t in {0,1}}. Allowed action flips x, preserves
    hidden tag t; the only allowed readout is x. States (0,0),(0,1)
    remain operationally indistinguishable for EVERY finite action word
    of every length, because neither actions nor readout depend on t.
    A NEW tag probe would repair this pathway but is not in this Cl(Tools).
    """
    if type(word_length) is not int or not 0<=word_length<=100000:
        raise FieldLimitError("Typed finite action-history depth needed")
    first=(0,0)
    second=(0,1)
    x0=first[0]^ (word_length%2)
    x1=second[0]^ (word_length%2)
    if x0!=x1:
        raise ArithmeticError("Forbidden observation distinguished source tags")
    return {"source_pair":(first,second),
            "allowed_actions":"flip visible bit; never change hidden tag",
            "allowed_readout":"visible bit only",
            "reports_after_selected_word":(x0,x1),
            "all_action_words_indistinguishable":"PROVED_BY_ACTION_INVARIANCE",
            "full_source_identity_recoverable":False,
            "repair_requires_new_source_authorized_tag_probe":True,
            "classification":"FUCKED_TOOLKIT_RELATIVE_NONFAITHFUL_SOURCE",
            "RH_proved":False}


def effective_unique_compact_path_theorem(depth:int)->dict:
    """Classical computability boundary for effective finite-branching trees.

    A decidable finitely branching binary tree with EXACTLY ONE infinite
    path has COMPUTABLE path: given any desired bit, search successive
    finite levels until all surviving prefixes agree at that coordinate.
    Existence of a unique infinite path + compact finite fanout ensures
    termination (any rival branch must have finite height). No uniform
    stage bound is asserted. Here calibrate on singleton zero path.
    """
    if type(depth) is not int or not 0<=depth<=64:
        raise FieldLimitError("Bounded finite path witness")
    return {"depth":depth,"finite_tree_source":"T={0^n:n>=0}",
            "only_infinite_path_prefix":tuple(0 for _ in range(depth)),
            "singleton_path":"0^omega",
            "effective_stage_membership":True,
            "finite_branching":True,
            "unique_global_path":True,
            "global_path_computable":"PROVED_CLASSICAL_WITH_UNIQUENESS_PROMISE",
            "finite_uniform_bound_on_all_requested_bits_proved":False,
            "RH_proved":False}


def field_contracts()->tuple[FieldClassification,...]:
    """These labels are proved for FIXED examples with declared toolkits."""
    return (
        FieldClassification(
            "SIMPLE","original integer 1 inside Z_2","evaluate coherent residue at arbitrary n",
            "exact modular arithmetic + law of reduction",True,True,True,True,True,
            "finite executable SYMBOLIC law per requested finite stage"),
        FieldClassification(
            "IDEALHARD","computable finitely-branching Kleene binary tree",
            "produce one infinite global binary path",
            "all bounded TM simulations + classical existence proof",
            False,True,False,None,False,
            "classical diagonal witness exists, NO computable path selector"),
        FieldClassification(
            "FUCKED/NONEXISTENCE","noncompact tail system X_n={m>=n}",
            "one coherent natural number for all n","finite stages + inclusion bonds",
            False,False,False,None,False,
            "finite satisfiability without compactness cannot imply global existence"),
        FieldClassification(
            "FUCKED/SOURCE-MAP","profinite CRT ghost versus original integers",
            "decide integer origin from a finite prefix","all finite residue observers",
            False,True,False,False,False,
            "every finite prefix has integer rival; global ghost is not an integer"),
        FieldClassification(
            "FUCKED/TOOLKIT","two hidden-tag sources with invariant report menu",
            "recover full source identity","all words of visible flip + readout",
            False,True,False,False,False,
            "noninjective operational quotient; no future action in toolkit separates tags")
    )


def tate_rh_field_boundary()->dict:
    """Correctly scope the actual Tate/RH state without declaring hardness."""
    signed=dense_smooth_source_gate()
    negative=exact_scalar_schur_source_gate(1,2,1)
    if signed["finite_prefix_positive_implies_RH"] or negative["PSD"]:
        raise ArithmeticError("Original signed Weil boundary was misclassified")
    return {
        "profinite_reconstruction":"CLASSICAL_BIJECTION_IN_DECLARED_OBSERVER_CATEGORY",
        "local_padic_chart_Fourier":"CLASSICAL_TWO_AXIS_TATE_TEST_EXHAUSTION",
        "global_adelic_Poisson_from_SUCC_primitives":"UNVERIFIED",
        "source_Weil_sign_if_RH_false":
            "STRICT_NEGATIVE_ORIGINAL_SOURCE_TEST_HAS_FINITE_DENSE_WITNESS",
        "source_Weil_sign_if_RH_true":
            "FINITE_OBSERVER_SIGN_PREFIXES_ALONE_DO_NOT_PROVE_UNIVERSAL_SIGN",
        "RH_is_mathematically_unprovable":"NOT_ESTABLISHED",
        "RH_fucked_field_intrinsic_status":"UNVERIFIED_NOT_CLASSIFIABLE_FROM_CURRENT_CLOSURE",
        "missing_source_theorem":"ALL_STAGE_ACTUAL_WEIL_CROSS_BLOCK_SCHUR_OR_INDEPENDENT_POSITIVE_FEATURE",
        "finite_symbolic_Tate_carrier_is_full_RH_proof":False,
        "RH_proved":False
    }



def single_real_oracle_shadow(depth:int,step_budget:int)->dict:
    """Exact rational enclosure for ONE real encoding infinitely many halts.

    Let H(e)=1 if program phi_e(e) ever halts with output bit 0 OR 1.
    The mathematical scalar is Omega4 = sum_(e>=0) 4^(-(e+1))*H(e),
    with digits in {0,1} so the base-4 expansion is unambiguous.
    If Omega4 were a computable real, we could extract H(e)
    recursively using a precision <= 4^(-(e+1))/6 and the digit gap:
       bit=0 has remaining tail <=weight/3,
       bit=1 has residual >=weight.
    That would solve the halting problem, a contradiction.

    The finite code only knows HALTS WITHIN B steps for e<depth.
    Unknown early programs remain possible 0/1, and infinite tail
    contributes <=4^(-depth)/3. Thus [lower,upper] is sound but
    need not converge effectively in B. An oracle returning the
    EXACT real would supply noncomputable infinite information in
    one apparently finite observation; it is NOT a legitimate
    ordinary finite executable SUCC source without an oracle license.
    """
    if (type(depth) is not int or type(step_budget) is not int
            or not 1<=depth<=48 or not 0<=step_budget<=512):
        raise FieldLimitError("Exact finite halting-real stage 1..48, time<=512")
    lower=F()
    unresolved=F()
    halted=[]
    for e in range(depth):
        weight=F(1,4**(e+1))
        bit=bounded_binary_turing_diagonal(e,step_budget)
        if bit is None:
            unresolved+=weight
        else:
            lower+=weight
            halted.append(e)
    infinite_tail=F(1,3*4**depth)
    upper=lower+unresolved+infinite_tail
    if lower<0 or upper>F(1,3) or lower>upper:
        raise ArithmeticError("Source exact real Halting enclosure inconsistent")
    return {
        "single_observer_channel":"ONE EXACT REAL VALUE IF GIVEN AS AN ORACLE",
        "mathematical_real":"Omega4=sum 4^(-(e+1)) * 1_phi_e(e)_halts",
        "finite_simulated_indices":depth,
        "finite_simulated_steps":step_budget,
        "bounded_halt_indices":tuple(halted),
        "rational_lower":lower,"rational_upper":upper,
        "uncertainty":upper-lower,
        "infinite_unseen_tail_bound":infinite_tail,
        "exact_real_computable":"PROVED_NO_BY_HALTING_DIGIT_REDUCTION",
        "exact_real_observer_oracle_authorized":False,
        "source_finite_interface_not_finite_effective_information":True,
        "Archimedean_Schwartz_test_data_automatically_computable":False,
        "RH_proved":False,
    }
