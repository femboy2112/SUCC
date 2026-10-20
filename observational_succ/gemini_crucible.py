"""Operation Gemini Crucible (Part II): a hostile, exact theorem-by-theorem audit
of the supplied Gemini local-to-global rigidity manuscript.

The manuscript file itself was NOT present in the research workspace, so -- per the
operation's explicit instruction ("Do not pretend to have inspected an unavailable
source") -- this audit works from the exact claim descriptions and countermodels
provided in the operation brief (claims 1.1-1.8). Every refutation here is an EXACT
rational computation, reproduced in the tests; no floating point enters any verdict.

Verdict vocabulary (audit statuses, distinct from the proof_contracts status set):
    REFUTED       -- an exact counterexample to the claim as stated
    MISLEADING    -- a true-but-misused statement (sufficient test read as necessary)
    VACUOUS       -- hypotheses cannot be met by any nontrivial object
    MISCLASSIFIED -- attributed to the wrong theorem / strength class
    NOT_ADOPTED   -- an unjustified synthesis; its pieces are triaged individually

The exact Schur / coercivity machinery lives in :mod:`quantitative_rigidity`; this
module reuses it so the refutations and the positive theory share one code path.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Callable, Dict, List, Optional, Tuple

import sympy as sp

from observational_succ.quantitative_rigidity import (
    Rat,
    conservative_surrogate,
    coupling_negative_vector,
    inverse_decay_block,
    is_positive_definite,
    is_positive_semidefinite,
    schur_complement,
    uniform_gap_profile,
)

_VALID_VERDICT = {"REFUTED", "MISLEADING", "VACUOUS", "MISCLASSIFIED", "NOT_ADOPTED"}


@dataclass
class CrucibleVerdict:
    claim_id: str
    title: str
    gemini_statement: str
    status: str
    mechanism: str             # WHY it fails / is misused
    witness: Dict[str, object]  # the exact numbers
    replacement: str           # the minimal correct statement

    def __post_init__(self):
        if self.status not in _VALID_VERDICT:
            raise ValueError(f"bad verdict {self.status!r}")

    def as_record(self) -> dict:
        return {
            "claim_id": self.claim_id, "title": self.title,
            "gemini_statement": self.gemini_statement, "status": self.status,
            "mechanism": self.mechanism,
            "witness": {k: str(v) for k, v in self.witness.items()},
            "replacement": self.replacement,
        }


# --------------------------------------------------------------------------- #
# 1.1  Restricted Douglas-Schur transfer  -- REFUTED
# --------------------------------------------------------------------------- #
def claim_1_1_restricted_coercivity() -> CrucibleVerdict:
    """The compression <D e1, e1> = 1 does NOT control the inverse response
    B D^{-1} B^* because span(e1) is not D-invariant."""
    A = sp.Matrix([[2]])
    B = sp.Matrix([[1, 0]])
    D = sp.Matrix([[1, Rat(9, 10)], [Rat(9, 10), 1]])
    M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))

    compression = (D[0, 0])                               # <D e1, e1> = 1
    surrogate = conservative_surrogate(M, 1, kappa=1)     # A - 1^{-1} B B^T = 1 > 0
    true_schur = schur_complement(M, 1)                   # 2 - 100/19 = -62/19 < 0
    neg_vec = coupling_negative_vector(M, 1, [1])         # exact negative direction
    neg_val = (neg_vec.T * M * neg_vec)[0, 0]

    assert compression == 1
    assert surrogate == sp.Matrix([[1]]) and surrogate[0, 0] > 0
    assert true_schur == sp.Matrix([[Rat(-62, 19)]]) and true_schur[0, 0] < 0
    assert neg_val == Rat(-62, 19)

    return CrucibleVerdict(
        claim_id="1.1",
        title="Restricted Douglas-Schur transfer (Gemini Thm 3.5)",
        gemini_statement=("Coercivity restricted to the coupling subspace (kappa=1 "
                          "from <D e1,e1>=1) certifies A - kappa^{-1} B B^* = 1 > 0, "
                          "hence an inverse-response positivity bound."),
        status="REFUTED",
        mechanism=("span(e1) is NOT invariant under D, so the compression <D e1,e1> "
                   "is not a lower bound for the inverse response. The true Schur "
                   "complement A - B D^{-1} B^* = 2 - 100/19 = -62/19 < 0, with an "
                   "explicit negative vector v=(1; -D^{-1}B^T e) giving v^T M v = "
                   "-62/19."),
        witness={"compression <D e1,e1>": compression,
                 "surrogate A-kappa^-1 BB^*": surrogate[0, 0],
                 "true schur A-BD^-1B^*": true_schur[0, 0],
                 "negative_vector": neg_vec.T.tolist(),
                 "v^T M v": neg_val},
        replacement=("Use the TRUE inverse response A - B D^{-1} B^* (exact), a "
                     "reducing subspace actually invariant under D, or the Douglas "
                     "factorization with its stated range/domain. Never substitute "
                     "the compression of D for a bound on D^{-1}."),
    )


# --------------------------------------------------------------------------- #
# 1.2  Scalar Schur obstruction misread as a negative witness -- MISLEADING
# --------------------------------------------------------------------------- #
def claim_1_2_sufficient_not_necessary() -> CrucibleVerdict:
    A, D, B, kappa = sp.Matrix([[1]]), sp.Matrix([[100]]), sp.Matrix([[2]]), 1
    M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
    surrogate = conservative_surrogate(M, 1, kappa)[0, 0]   # 1 - 4 = -3
    true_schur = schur_complement(M, 1)[0, 0]               # 1 - 4/100 = 24/25
    assert surrogate == -3 and true_schur == Rat(24, 25) and true_schur > 0
    return CrucibleVerdict(
        claim_id="1.2",
        title="Failure of A - kappa^{-1} B B^* >= 0 implies nonpositivity",
        gemini_statement=("If A - kappa^{-1} B B^* is not PSD then the source form "
                          "is actually nonpositive."),
        status="MISLEADING",
        mechanism=("The surrogate is only a SUFFICIENT lower certificate (valid when "
                   "D >= kappa I). Here A=1,D=100,B=2,kappa=1 gives surrogate "
                   "1-4 = -3 < 0, yet the true Schur complement 1 - 4/100 = 24/25 "
                   "> 0. Failure of a sufficient test is NOT a negative witness."),
        witness={"surrogate": surrogate, "true_schur": true_schur},
        replacement=("A negative witness requires an actual vector v with v^T M v<0 "
                     "(equivalently the TRUE Schur complement being non-PSD), not the "
                     "failure of a conservative lower bound."),
    )


# --------------------------------------------------------------------------- #
# 1.3  Observer memory-debt: quotient autonomy  !=  unique source lift ; and the
#      vacuous spectral-leakage hypothesis -- REFUTED / VACUOUS
# --------------------------------------------------------------------------- #
@dataclass
class TwoStateCollapse:
    """A source with states {s0,s1}, both observed as the single visible state o;
    identical report/actions/costs/quotient-successor. Quotient evolution is
    autonomous; a source history has no unique lift."""
    states: Tuple[str, str] = ("s0", "s1")
    visible: str = "o"

    def observe(self, s: str) -> str:
        return self.visible

    def quotient_successor(self, o: str) -> str:
        return self.visible                      # autonomous on the quotient

    def source_lifts(self, observed_history: List[str]) -> List[Tuple[str, ...]]:
        """All source trajectories consistent with an observed history: 2^len,
        hence NOT unique (for length >= 1)."""
        import itertools
        n = len(observed_history)
        return list(itertools.product(self.states, repeat=n))


def spectral_leakage_min_norm(gamma: sp.Expr, dim: int, proj_rank: int) -> sp.Expr:
    """For E = gamma I (so E >= gamma I) and any proper orthogonal projection P of
    rank proj_rank < dim, the leakage norm ||(I-P)E(I-P)|| = gamma (attained on a
    unit vector of ran(I-P)). So the hypothesis ||(I-P)E(I-P)|| < gamma is
    unsatisfiable -- vacuous for every nontrivial observer."""
    assert 0 < proj_rank < dim, "need a proper projection"
    E = gamma * sp.eye(dim)
    P = sp.diag(*([1] * proj_rank + [0] * (dim - proj_rank)))
    leak = (sp.eye(dim) - P) * E * (sp.eye(dim) - P)
    # operator norm of a PSD diagonal block = largest diagonal entry = gamma
    return max(leak[i, i] for i in range(dim))


def claim_1_3_memory_debt() -> CrucibleVerdict:
    c = TwoStateCollapse()
    lifts = c.source_lifts(["o", "o", "o"])
    leak = spectral_leakage_min_norm(sp.Symbol("gamma", positive=True), 3, 1)
    gamma = sp.Symbol("gamma", positive=True)
    assert len(lifts) == 8                           # 2^3: lift not unique
    assert sp.simplify(leak - gamma) == 0            # leakage norm == gamma, not < gamma
    return CrucibleVerdict(
        claim_id="1.3",
        title="Observer memory-debt transfer (Gemini Thm 3.2)",
        gemini_statement=("Autonomous quotient descent yields a unique lifting of "
                          "source histories; a small spectral-leakage ||(I-P)E(I-P)|| "
                          "< gamma transfers a bound while E >= gamma I."),
        status="REFUTED",
        mechanism=("Autonomy of the quotient transition does NOT give a unique source "
                   "lift: the two-state collapse has an autonomous quotient yet 2^n "
                   "source lifts of any length-n observed history. Separately, the "
                   "leakage hypothesis is VACUOUS: for E >= gamma I and any proper "
                   "projection P, a unit vector in ran(I-P) gives ||(I-P)E(I-P)|| >= "
                   "gamma, so '< gamma' is unsatisfiable."),
        witness={"source_lifts_of_ooo": len(lifts),
                 "leakage_norm": leak, "required": "< gamma (impossible)"},
        replacement=("Separate five notions: (i) existence of a quotient transition, "
                     "(ii) autonomy on the quotient, (iii) existence of a source lift, "
                     "(iv) uniqueness of a source lift, (v) original-source "
                     "realization. A nonvacuous transfer needs genuine leakage "
                     "strictly inside a gapped subspace, which a proper observer "
                     "projection does not provide; otherwise preserve it as a NO-GO."),
    )


# --------------------------------------------------------------------------- #
# 1.4  Data-processing strict contraction -- REFUTED
# --------------------------------------------------------------------------- #
def total_variation(p: List[sp.Expr], q: List[sp.Expr]) -> sp.Expr:
    return sp.Rational(1, 2) * sum(abs(a - b) for a, b in zip(p, q))


def merging_channel(p: List[sp.Expr]) -> List[sp.Expr]:
    """C(x1,x2,x3) = (x1+x2, x3) on distributions."""
    return [p[0] + p[1], p[2]]


def claim_1_4_data_processing() -> CrucibleVerdict:
    p = [Rat(2, 5), Rat(1, 10), Rat(1, 2)]
    q = [Rat(0), Rat(0), Rat(1)]
    tv_in = total_variation(p, q)
    tv_out = total_variation(merging_channel(p), merging_channel(q))
    # p-q has a nonzero component along ker C = span((1,-1,0))
    diff = [a - b for a, b in zip(p, q)]
    ker_component = (diff[0] - diff[1])            # proportional to <diff,(1,-1,0)>
    assert tv_in == Rat(1, 2) and tv_out == Rat(1, 2) and ker_component != 0
    return CrucibleVerdict(
        claim_id="1.4",
        title="Strict TV contraction whenever diff has a kernel component",
        gemini_statement=("A channel strictly contracts total variation whenever the "
                          "distribution difference has a nonzero projection onto the "
                          "observation kernel."),
        status="REFUTED",
        mechanism=("Deterministic merge C(x1,x2,x3)=(x1+x2,x3): p=(2/5,1/10,1/2), "
                   "q=(0,0,1) have TV(p,q)=TV(Cp,Cq)=1/2 although p-q has component "
                   "3/10 along ker C = span((1,-1,0)). TV collapses only when the "
                   "merged fiber mixes BOTH signs of p-q; here the merged coordinates "
                   "{1,2} carry same-sign mass so no cancellation occurs."),
        witness={"TV_in": tv_in, "TV_out": tv_out, "ker_component": ker_component},
        replacement=("TV(Cp,Cq) = sum_y |sum_{x in fiber(y)} (p-q)(x)|. Strict "
                     "contraction holds iff some output fiber y has (p-q) taking both "
                     "signs on fiber(y) (sign cancellation within that fiber). "
                     "Distinguish classical stochastic channels from quantum CPTP "
                     "maps (the fiber-cancellation criterion is the classical case)."),
    )


# --------------------------------------------------------------------------- #
# 1.5  Primitive prime-clock probabilities -- REFUTED (missing factor 3)
# --------------------------------------------------------------------------- #
def primitive_valuation_law(p: sp.Symbol, k: sp.Symbol) -> sp.Expr:
    """Pr(v_p(abc)=k | primitive a+b=c) = 3(p-1)/((p+1) p^k), derived from the
    conditional-Haar model, not assumed."""
    return 3 * (p - 1) / ((p + 1) * p ** k)


def derive_primitive_valuation_law():
    """Symbolic derivation from the Haar model (returns the simplified closed form).

    Under independent Haar a,b in Z_p (c=a+b), primitivity E = not p|gcd(a,b,c).
    If v_p(a)>=1 and v_p(b)>=1 then v_p(c)>=1, violating E; so under E at most one
    slot has positive valuation. Hence v_p(abc)=k>=1 means exactly one slot has
    v_p=k and the others 0; by the a,b,c symmetry of a+b-c=0 there are 3 such slots.
    """
    p, k = sp.symbols("p k", positive=True, integer=True)
    P_va_k = (p - 1) / p ** (k + 1)        # Pr(v_p = k) for a single Haar coordinate
    P_vb_0 = (p - 1) / p                    # Pr(v_p = 0)
    # v_p(a)=k>=1 and v_p(b)=0 forces v_p(c)=v_p(a+b)=0 automatically
    joint_one_slot = P_va_k * P_vb_0        # = (p-1)^2 / p^(k+2)
    P_k_and_E = 3 * joint_one_slot
    P_E = 1 - sp.Rational(1, 1) / p ** 2    # 1 - Pr(both a,b divisible) = 1 - 1/p^2
    law = sp.simplify(P_k_and_E / P_E)
    return p, k, law


def ris_local_moment(p: sp.Symbol, t: sp.Symbol) -> sp.Expr:
    """Local p-factor of E[ris(abc)^t | primitive], ris local factor = p^{v-1} for
    v>=1 else 1. Converges iff t<1. (A LOCAL per-triple law -- NOT to be transported
    into a one-variable integer average or bounded-box joint law without a separate
    argument.)"""
    k = sp.symbols("k", positive=True, integer=True)
    P0 = (p - 2) / (p + 1)                  # Pr(v_p(abc)=0 | primitive)
    term = primitive_valuation_law(p, k) * p ** (t * (k - 1))
    tail = sp.summation(term, (k, 1, sp.oo))
    return sp.simplify(P0 + tail)


def claim_1_5_prime_clock() -> CrucibleVerdict:
    p, k, derived = derive_primitive_valuation_law()
    claimed = primitive_valuation_law(p, k)
    assert sp.simplify(derived - claimed) == 0
    # normalization at concrete primes (exact; the symbolic infinite sum returns a
    # convergence Piecewise, a presentation artifact only): sum_{k>=1} = 3/(p+1),
    # and at p=2 it is 1 -- "exactly one even entry among a,b,c".
    norms = {}
    for pr in (2, 3, 5, 7, 11):
        tot = sp.summation(claimed.subs(p, pr), (k, 1, sp.oo))
        assert tot == sp.Rational(3, pr + 1)
        norms[pr] = tot
    at_p2 = norms[2]
    assert at_p2 == 1
    return CrucibleVerdict(
        claim_id="1.5",
        title="Aggregate primitive prime-clock valuation probability",
        gemini_statement=("Pr(v_p(abc)=k) = (p-1)/((p+1) p^k) for primitive a+b=c "
                          "(omitting the three valuation slots)."),
        status="REFUTED",
        mechanism=("The correct law has a factor 3 for the three slots a,b,c: "
                   "Pr(v_p(abc)=k) = 3(p-1)/((p+1) p^k), k>=1, derived from the "
                   "conditional-Haar model (exactly one slot carries positive "
                   "valuation under primitivity). Normalization sum_{k>=1} = 3/(p+1), "
                   "which at p=2 equals 1 -- matching 'every primitive pair has "
                   "exactly one even entry among a,b,c'. Gemini's version sums to "
                   "1/(p+1) and fails this check (1/3 at p=2)."),
        witness={"derived_law": derived, "normalization_at_primes": norms,
                 "at_p=2": at_p2},
        replacement=("Pr(v_p(abc)=k) = 3(p-1)/((p+1) p^k). This is a LOCAL per-triple "
                     "law; do NOT transport it into a one-variable integer average or "
                     "a bounded-box joint distribution without a separate argument. "
                     "Preserve the existing ABC-CLK-02 Dirichlet-convolution "
                     "derivation."),
    )


# --------------------------------------------------------------------------- #
# 1.6  Prime-weight asymptotic misattributed to PNT -- MISCLASSIFIED
# --------------------------------------------------------------------------- #
def abel_weighted_to_psi_error(psi_error_exp: sp.Expr, psi_log_power: sp.Expr):
    """Abel summation link: if psi(x) = x + O(x^alpha log^beta x) then
       sum_{n<=x} Lambda(n) n^{-1/2} = 2 x^{1/2} + O(x^{alpha-1/2} log^beta x) + C.
    Conversely the weighted error O(log^2 x) (x=e^{2a}, a^2=(1/4)log^2 x) forces
    alpha = 1/2, i.e. psi(x) = x + O(x^{1/2} log^2 x) -- RH-strength.

    NOTE: the load-bearing conclusion is the EXPONENT alpha = 1/2 (the sqrt(x) term)
    -- that is what makes it RH-strength and beyond PNT. The log-power beta is
    transported schematically; a careful Abel summation / IBP can shift log^2 <-> log^3,
    which does not affect the exponent conclusion."""
    a, b = psi_error_exp, psi_log_power        # psi error x^a log^b
    weighted_exp = a - sp.Rational(1, 2)       # weighted-sum error exponent
    return {"weighted_error_exp": weighted_exp, "weighted_log_power": b}


def claim_1_6_prime_weight_asymptotic() -> CrucibleVerdict:
    # weighted error O(a^2) with x=e^{2a} is O(log^2 x); invert the Abel link:
    # weighted_exp = alpha - 1/2 = 0  => alpha = 1/2 (RH strength).
    alpha = sp.Rational(1, 2)
    fwd = abel_weighted_to_psi_error(alpha, 2)
    assert fwd["weighted_error_exp"] == 0         # x^0 = O(1)*log^2 -> O(log^2 x)
    return CrucibleVerdict(
        claim_id="1.6",
        title="sum_{n<=e^{2a}} Lambda(n) n^{-1/2} = 2 e^a + O(a^2) 'by PNT'",
        gemini_statement=("The estimate sum_{n<=e^{2a}} Lambda(n) n^{-1/2} = 2 e^a + "
                          "O(a^2) is a consequence of the prime number theorem."),
        status="MISCLASSIFIED",
        mechanism=("With x=e^{2a} the error O(a^2)=O(log^2 x). By Abel summation this "
                   "is equivalent to psi(x)=x+O(sqrt(x) log^2 x), an RH-STRENGTH error "
                   "term. PNT only gives psi(x)=x+o(x), hence the weighted sum "
                   "2 sqrt(x) + o(sqrt(x)) -- never O(log^2 x). So the claim is "
                   "RH-level, not a PNT consequence."),
        witness={"x": "e^{2a}", "weighted_error": "O(log^2 x)",
                 "implied_psi_error": "x + O(sqrt(x) log^2 x)",
                 "strength": "RH (CONJECTURED/open), not CLASSICAL (PNT)"},
        replacement=("Classify as RH-strength. Distinguish arithmetic weight sums, "
                     "operator-norm upper bounds, operator-norm asymptotics, and "
                     "signed cancellation in the Weil form -- they are different "
                     "objects. Also: the prime-window threshold 2a=log n is a "
                     "measure-zero support-intersection point for L^2 zero-extension "
                     "shifts, so equality-at-threshold carries no L^2 mass."),
    )


# --------------------------------------------------------------------------- #
# 1.7  Float 'is_globally_rigid' ignores high-block positivity -- REFUTED
# --------------------------------------------------------------------------- #
def naive_rigidity_diagnostic_is_unsound(A, D, B) -> dict:
    """Mimic the Gemini diagnostic that only checks the (pseudo)Schur complement
    A - B D^+ B^* and ignores whether D (the high block) is positive. On
    A=(1),D=(-1),B=0 it declares 'rigid' though M=diag(1,-1) is indefinite."""
    A, D, B = sp.Matrix([[A]]), sp.Matrix([[D]]), sp.Matrix([[B]])
    M = sp.Matrix(sp.BlockMatrix([[A, B], [B.T, D]]))
    pseudo_schur = A - B * D.pinv() * B.T          # = A = 1 > 0
    naive_rigid = is_positive_semidefinite(pseudo_schur)   # True (WRONG)
    truly_psd = is_positive_semidefinite(M)                # False
    high_block_ok = is_positive_semidefinite(D)            # False -> the missing check
    return {"naive_rigid": naive_rigid, "truly_psd": truly_psd,
            "high_block_psd": high_block_ok, "pseudo_schur": pseudo_schur[0, 0]}


def claim_1_7_float_diagnostic() -> CrucibleVerdict:
    r = naive_rigidity_diagnostic_is_unsound(1, -1, 0)
    assert r["naive_rigid"] is True and r["truly_psd"] is False
    assert r["high_block_psd"] is False and r["pseudo_schur"] == 1
    return CrucibleVerdict(
        claim_id="1.7",
        title="Float pseudoinverse diagnostic labelled is_globally_rigid",
        gemini_statement=("A floating-point diagnostic computing a pseudo-Schur "
                          "complement and finding no finite counterexample declares "
                          "'is_globally_rigid=True'."),
        status="REFUTED",
        mechanism=("On A=(1),D=(-1),B=0 the pseudo-Schur complement is A=1>0 and the "
                   "diagnostic declares global rigidity, but M=diag(1,-1) has an "
                   "explicit negative high direction e_2. The diagnostic never checks "
                   "D >= 0 (or the D>=0 range condition). No float tolerance converts "
                   "'no finite counterexample found' into a global certificate."),
        witness=r,
        replacement=("A global PSD certificate requires BOTH the high block condition "
                     "(D > 0, or D >= 0 with ran(B^*) in ran(D)) AND the TRUE Schur/"
                     "shorted complement PSD, all in exact arithmetic (see "
                     "quantitative_rigidity.finite_schur_certificate)."),
    )


# --------------------------------------------------------------------------- #
# 1.8  Master identity + five obstruction classes -- NOT_ADOPTED
# --------------------------------------------------------------------------- #
def vanishing_uniform_coercivity_witness(Ns=(2, 4, 8, 16, 32)):
    """D=diag(1,1/2,1/3,...): every finite block strictly coercive (PD), inf
    spectrum -> 0, no uniform gap. The missing obstruction class."""
    return uniform_gap_profile(inverse_decay_block, list(Ns))


def defect_additivity_fails_example():
    """A master identity that sums 'defect budgets' into one Schur gap is not valid
    in general: the inverse response ``B D^{-1} B^T`` (the amount subtracted from A)
    is QUADRATIC in the coupling, so with a coupled (non-diagonal) high block the
    true joint defect is not the sum of the one-at-a-time defects. All quantities
    below use the SAME high block D, so the comparison is apples-to-apples."""
    A = sp.Matrix([[3]])
    D = sp.Matrix([[1, Rat(1, 2)], [Rat(1, 2), 1]])   # one coupled high block
    Dinv = D.inv()
    B1 = sp.Matrix([[1, 0]])
    B2 = sp.Matrix([[0, 1]])
    B_full = sp.Matrix([[1, 1]])

    def defect(B):   # amount this coupling subtracts from A in the Schur complement
        return (B * Dinv * B.T)[0, 0]

    d1, d2 = defect(B1), defect(B2)          # 4/3, 4/3  (one-at-a-time, same D)
    naive_sum_defect = d1 + d2               # 8/3
    coupled_true_defect = defect(B_full)     # 4/3  (joint, same D) != 8/3
    return {"per_source_defects": (d1, d2),
            "naive_sum_defect": naive_sum_defect,
            "coupled_true_defect": coupled_true_defect,
            "additivity_holds_when_coupled": coupled_true_defect == naive_sum_defect}


def claim_1_8_master_identity() -> CrucibleVerdict:
    prof = vanishing_uniform_coercivity_witness()
    add = defect_additivity_fails_example()
    assert prof[-1][1] < prof[0][1]                      # gap -> 0
    assert add["additivity_holds_when_coupled"] is False  # defects not additive
    return CrucibleVerdict(
        claim_id="1.8",
        title="Master identity + five-fold obstruction theory (Gemini Thm 3.6)",
        gemini_statement=("A single Schur identity absorbs memory-debt, cocycle, and "
                          "arithmetic-cumulant terms as additive defect budgets, with "
                          "five independent, exhaustive obstruction classes."),
        status="NOT_ADOPTED",
        mechanism=("No shared quadratic form / common carrier is derived, so the terms "
                   "are not known to share units, functional type, sign, or a "
                   "source-derived map; and the inverse response is QUADRATIC in the "
                   "coupling, so defects are not additive once the sources interact "
                   "(exact example: coupled true defect != naive sum). Independence "
                   "and exhaustiveness of the five classes are unproven, and at least "
                   "one class is missing: vanishing uniform coercivity "
                   "D=diag(1,1/2,...) (every finite block PD, no uniform gap)."),
        witness={"gap_profile": [(N, str(g)) for N, g in prof],
                 "defect_additivity": add},
        replacement=("Keep the five classes only as a DIAGNOSTIC taxonomy, not a "
                     "theorem. Each defect must separately exhibit: common carrier, "
                     "units, functional type, a source-derived map into the target "
                     "form, a valid sign, a justified decomposition, no duplicated "
                     "contribution, and a convergence theorem when infinite. Replace "
                     "the master identity with the per-term transport theorems of "
                     "Part III (finite Schur, shorted complement, form-core "
                     "transport)."),
    )


def run_full_crucible() -> List[CrucibleVerdict]:
    return [
        claim_1_1_restricted_coercivity(),
        claim_1_2_sufficient_not_necessary(),
        claim_1_3_memory_debt(),
        claim_1_4_data_processing(),
        claim_1_5_prime_clock(),
        claim_1_6_prime_weight_asymptotic(),
        claim_1_7_float_diagnostic(),
        claim_1_8_master_identity(),
    ]
