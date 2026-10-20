# Carrier-relative LEM / FuckedField discriminating probe contracts

**2026-10-20 — PREREGISTERED PLAN, NOT EXECUTED.** This plan is intentionally independent of the RH proof program. Primary dossier: [authority/logic](CARRIER_RELATIVE_LOGIC_AUTHORITY.md); local ledger: [CRL IDs](CARRIER_RELATIVE_LOGIC_CLAIMS.md). Start with exact finite tables, full transition histories, and at least one independent implementation; do not report test passes until executed.

## Probe A — permanent observational alias (CRL-07 / CRL-10)

**Carrier:** S={(v,h):v,h∈{0,1}}, known initial v=0, h hidden. Allowed source-preserving actions: flip_visible maps (v,h)↦(1−v,h); read_visible outputs v and leaves S unchanged. The proposition P is h=1. Neither original action touches/reveals h.

**Prediction:** For any (possibly adaptive/randomized) policy over these actions and every finite n, sources (0,0) and (0,1) have identical history distributions; direct induction on history gives the certificate. New separately licensed read_hidden emits h and splits the pair. A tool change must carry a new epoch and cannot retroactively certify an old decision.

- **PASS:** exact bisimulation or fully enumerated finite policy cases under each bound, plus induction proof; no old-tool classifier claims h; read_hidden splits.
- **FAIL:** a classifier returns h from a legal old history with claimed universal correctness, or a tool change is erased.
- **AMBIGUOUS:** a finite exhaustive test without a full behavioral proof supports only a bounded statement.
- **Negative/mutation:** leak h in read_visible, allow illegal reset-to-hidden preparation, or forge source epoch; these MUST change the verdict. Null: repeated read_visible adds no hidden information.

## Probe B — moving phantom vs genuinely compatible limit (CRL-08 / CRL-09)

**Negative source:** X_n={m∈N:m≥n}, inclusion maps. Every finite horizon H has the consistent choice m=H. The inverse limit is empty since no fixed natural exceeds all n.

**Positive compact source:** X={0,1}^N with closed cylinder constraints “the first n bits are 0.” All finite intersections are nonempty, and the intersection is the single all-zero stream. Compactness certifies existence, but implementation must distinguish that theorem from an arbitrary physical infinite execution.

- **PASS:** finite negative witnesses, proof of empty full limit, compact positive witness, distinct outcome labels.
- **FAIL:** promotes ∀n∃m_n to ∃m∀n; claims compactness for noncompact X_n.
- **AMBIGUOUS:** bounded enumeration only, without the universal proofs.
- **Controls:** replace X_n by a fixed finite set with a genuine decreasing compatible family; source-identity mismatch must be rejected. Supplement with SUCC's already proven profinite integer ghost: finite matching integers are not a single original integer witness.

## Probe C — backaction and temporal honesty (CRL-15)

**Two instrument variants:** initial state 0, silent action always outputs 0. In Hold, silent maps state to itself; in Flip, silent maps state to 1−state. A subsequent authorized read_state yields the current state and is nondisturbing.

**Prediction:** One silent observation cannot distinguish variants. The ordered policy silent→read_state distinguishes Hold from Flip with certainty. A direct read_state without the silent predecessor does not. The report concerns the **post-action state**, not automatically the pre-action one.

- **PASS:** exact transition kernels and complete action/output traces reproduce predictions; time/source epoch preserved.
- **FAIL:** the first silent output is advertised as informative, or the later readout is attributed to the earlier state without a reconstruction map.
- **Controls:** both variants Hold (null); read_state removed (dark); wrong action-order mutation (should not produce separation); fake foreknowledge is refused.
- **Optional quantum extension:** use two explicit trace-preserving instruments, calibrate their completely positive maps, compare adaptive joint outcome probabilities. No quantum-specific statement is earned by the classical model alone.

## Probe D — logic, choice, and source-realization firewall (CRL-02–04)

**Formal targets:** (i) check P∨¬P as classical syntax without extracting a proof of P or ¬P; (ii) prove a restricted witnessed finite-choice operation in a chosen constructive calculus; (iii) do not promote it to “all epis split” absent explicit epimorphism-quantified construction. For the genuine Diaconescu route, construct q_P:2↠Q_P and a lawful section for each arbitrary P *under full AC*, then derive internal LEM with the correct quotient eliminator.

- **PASS:** formal results retain exact logic, type, quotient, and choice assumptions; legal local witness cannot masquerade as full categorical choice.
- **FAIL:** admits blanket AC⇒LEM without mentioning setting, equates classical LEM to an effective external-world decision, or silently posits all sections from checked examples.
- **Controls:** restricted fragment whose P are decidable; arbitrary P cannot be silently instantiated. Model-theory or Lean theorem used as authority must be attributed and independently checked.
- **Boundary:** finite Python cannot prove a quantified elementary-topos statement.

## Probe E — source map and relative consequence (CRL-06 / CRL-11)

Let q:X→Y forget hidden bit h and let P(v,h)=[h=1]. q-fibers mix opposite P, so the descended function \bar P does not exist. A second property R(v,h)=[v=1] is fiber-constant and descends.

Then construct two observation/model classes: one nonempty class in which every compatible carrier satisfies R; one class containing both P and ¬P variants; and an intentionally empty class.

- **PASS:** R exports, P refuses, mixed-model P stays unresolved, empty class cannot issue source-relative certificate, source-map identity must be checked.
- **FAIL:** any of P, empty-class vacuity, or model-only implication promotes to source truth without additional authority.
- **Controls:** swapped observation labels (basis mismatch), duplicate transcripts counted as independent, and false source calibration that fits old data but fails new independent holdout.

## Probe F — first-person warrant is not numerical LEM (CRL-01 / CRL-13 / CRL-14)

Treat “I am I” as a **quoted author-origin phenomenological anchor**, not a truth-probability oracle. Reflexivity of a named index is a formal theorem; personal continuity/external world are not derivable from that alone. Require a narrow proposed preorder on contingent claims, not a universal strict order.

- **PASS:** tautologies and definitional equivalents remain logically co-valid, no numerical probability emitted without prior/likelihood/calibration, subjective report remains explicit hypothesis.
- **FAIL:** global theorem “all other statements have p<1,” a numeric φ/κ-to-posterior conversion, or personal/physical mechanisms inferred without evidence.
- **Controls:** x=x, P→P, and two syntactically different equivalent tautologies must defeat proposed universal strict ranking.

## Required execution receipt, once implemented

Record exact main/branch SHA, dependencies, source schema, admissible action/preparation policy, raw event traces, proof/certificate hashes, independent oracles, mutant outcomes, pass/fail/ambiguous statuses, and unperformed tests. One same-model verifier plus one same-model review is NOT a blind independent witness. All new claims inherit the weakest source/identification premise. No RH/ABC/Weil positivity claims from these probes.

**Recommendation:** first implement A/B/E as exact finite models with independent exhaustive oracles; C next with time-indexed kernels; D in Lean; F as a documented logical counterexample/interpretation gate. Positive, negative, null, and mutation controls are mandatory.
