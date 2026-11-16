# Provenance and independence

**Second Forge, 2026-11-14.** Which arguments were imported, which were derived here and by whom,
which were mechanically checked, and which remain unresolved.

## 1. Independence protocol

- **No contact with the Astra campaign.** No Astra definition, theorem, proof, branch or message
  was read or used by the principal session or by any delegated agent. Each delegated brief
  carried the same prohibition.
- **Shared premises.** The only shared input is the founding note in
  [PR #618](https://github.com/femboy2112/SUCC/pull/618)
  (`research/2026-11-13/causal_relevance_proximity/RESEARCH_NOTE.md` at
  `ab31057590a59b2bfbd5dbcd7126b2aefc7a2b55`), read as a hypothesis source and never used as a
  validation witness. PR #618 was not modified.
- **Repository base.** Main XXV, `db9fb4b84672050efa79b13377f1e73364598a14`. Existing SUCC
  material is cited where used and is listed in §2; no archival original, ledger entry or
  historical default was changed.

Exactly what was inherited from the note: the working principle "closer = more causally
relevant"; finite contrasts and the impulse-response identity `C A^{t−s−1} B`; the calibrated
relevance and optional path-geometry constructs; the adversaries (common cause, two-path
cancellation, no-signalling, saturation); the boundary-as-threshold idea; the classical-appearance
hypothesis and its five adversaries; the two-regime distinction with the pair `a`, `b_H`; the
unseen causal set `U` and the defect derivative `D^source − D^model`.

## 2. Imported from SUCC (attributed)

| Source | Used for |
|---|---|
| `docs/CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md`, `formal/PrincipiaAncestral.lean`, `observational_succ/ancestral_observer.py` | starting point of all quotient-geometry results; Boolean instance; ghost and chain receipts; 2,594-model census reproduced |
| `docs/CARRIER_RELATIVE_TARGETS.md`, `observational_succ/carrier_relative_targets.py` | `Carrier`/`Instrument` contract, behavioural partition, observer algebra, target descent, destructive A,B,C carrier, oscillation radius, `plan_target` |
| `observational_succ/future_safe_quotient.py` | `Machine`/`State`/`Edge` contract; cross-checks |
| `docs/METHOD.md`, `AGENTS.md` | steelman–crucible–verdict method, receipt rule, status vocabulary |
| `docs/CLAIM_SUPPLEMENT_BOUNDARY_PORT_GEOMETRY.md` (BPGS-04/07/08) | cited as an unaudited analogy only |

Classical mathematics is named at the point of use in each proof document (Moore, Nerode, Kalman,
Cayley–Hamilton, Cauchy, Harary, Engel–Schneider, Fiedler–Pták, Kemeny–Snell, Larsen–Thomsen,
Lawvere, Gold, Kelly, Skolem–Mahler–Lech, Möbius/Rota, Fine–Wilf, among others). **Citations were
written from memory and were not checked against the primary sources**; several are flagged as
uncertain inside the reports. No scholarly novelty is claimed for any result.

## 3. Who derived what

| Workstream | Model / effort (as configured) | Product | Independence from the PI's own argument |
|---|---|---|---|
| Principal investigator | principal session, high effort | `formal/ObservatorisQuantale.lean`; `observatoris_response_geometry`; `observatoris_classical_appearance`; integration tests; all top-level documents | — |
| OPUS I Finite Observer | Opus, high | FO-1…FO-10, lab and 42 tests | brief stated targets without proofs; four PI conjectures refuted |
| OPUS II Causal Geometer | Opus, high | Geometer CG-1…CG-13, lab and 45 tests | brief stated conjectures without proofs; did not see the Lean file; eight corrections |
| OPUS III Horizon Hunter | Opus, high | FH-1…FH-14, lab and 45 tests | brief stated targets without proofs; five corrections of constants and hypotheses |
| OPUS IV Hostile Referee (two seats) | Opus, high | adversarial reports with executable receipts | reviewed finished text and code; no access to the PI's reasoning |

The delegated agents ran through the session's sub-agent mechanism with the Opus model class
and high effort set explicitly on each invocation (not merely requested in prose). The resolved
model of each agent was not separately read back, so "Opus, high" is the **requested**
configuration. No agent was run at maximum effort, and none needed escalation beyond high.

**What counts as an independent witness here.**

- *Quotient geometry:* the PI proved QG-1…QG-4 and formalised them in Lean **before** the
  Geometer's report existed; the Geometer proved the same statements on paper from a brief that
  contained no proofs, and tested them exhaustively. Two authors, two routes, one kernel check.
- *Balance (RG-4):* proved by the PI; proved independently, in a stronger form, by the Geometer.
- *Free observation (CA-1 / FO-10(b1)):* proved by the PI and, separately, by the Finite Observer.
- *Finite-horizon constants:* proved by the Horizon Hunter; three headline constants re-computed
  by the PI with separate code (linear sharpness pairs, machine horizon, the closed-form miss).
- *Finite-observer claims:* the Möbius expansion, the essential-variable criterion and the
  `x₃·NAND` refutation re-computed by the PI with separate code.
- *Geometer claims:* condition 5, join-closure and the meet-failure receipt re-computed by the PI.

**What does not count.** Agents agreeing with a statement they were shown; tests in which one
function computes both sides; numerical agreement on sampled models. Where only such evidence
exists the register says OBSERVED.

## 4. Mechanically checked

| Artifact | Checker | Result |
|---|---|---|
| `formal/ObservatorisQuantale.lean` | Lean 4.14.0 core, no imports; `scripts/check_observatoris_lean.py` | 18 exported declarations, none depends on any axiom; two mutated statements rejected; receipt `receipts/lean-kernel.json` |
| exact finite models | Python `unittest`, exact rationals | counts in §6 |

A Lean compilation proves the encoded statements relative to their (empty) axiom dependencies.
It does not show that the encoding describes any physical or arithmetic source, and it does not
certify any Python implementation.

## 5. Adversarial review

Two hostile referees were run against finished text and code, with no access to the authors'
reasoning and an explicit instruction that agreement without attack is failure.

**Seat 1** ([agents/OPUS_IV_HOSTILE_REFEREE.md](agents/OPUS_IV_HOSTILE_REFEREE.md), 29 findings,
29 executable receipts in `tests/test_observatoris_referee_receipts.py`) reviewed the principal
investigator's causal-geometry document, the Lean encoding, the response-geometry and
classical-appearance code, and the finite-horizon report.

| Outcome | Count | Items |
|---|---|---|
| Refuted as stated, then repaired | 8 | HQ-3; HQ-4 (two links); HQ-2(b); RG-3 "no transform"; CA-4; one FH-6 clause; the Lean must/may control |
| Overclaim withdrawn or statement repaired | 7 | RG-3 "derived"; RG-3 "Lawvere distance"; §2 asymmetry; C-6 labelled refuted without a receipt; RG-4 criterion; RG-1(c) scope; QG-3(5) off the image; CA-3 |
| Tests that could not fail, replaced | 2 | two finite-horizon tests |
| Attribution corrections | several | existential abstraction, signature similarity, gain graphs, stabiliser fragment, Moore, Massey |
| Survived, with the attack recorded | 14 | Lean core; QG-5 (strengthened); HQ-1 (sharpened); RG-1(a,b); RG-2; RG-5 (weakened hypothesis); RG-6; CA-6; FH-3; FH-7; FH-8; FH-9; FH-6(d); FH-11 and the paper re-derivations |

Every refuted statement is kept as a corpse (COUNTERMODELS §5) and every live document carries
the repaired form. The principal investigator accepted all findings; none was contested.

**Seat 2** ([agents/OPUS_IV_REFEREE_ROUND2.md](agents/OPUS_IV_REFEREE_ROUND2.md), 19 findings,
39 executable receipts in `tests/test_observatoris_referee_round2.py`, which does not import the
modules under review) attacked the finite-observer and quotient-geometry reports. **Every
theorem it could test survived**, including over a value structure and a graph shape the authors
had not used. The damage was at the edges: one false "no example exists" observation (a
three-state counter-receipt), one receipt that did not show what it was cited for, one grading
hypothesis the lab's own example cannot satisfy, one wording error, one non-sharp depth bound,
census numbers that no test pinned (now pinned by independent code), two circular or vacuous
tests in the delegated suites, and missing classical citations. These are recorded as errata
appended to the two delegated reports and as C-52…C-57.

**What the reviews could not check** (and therefore remains unverified): statements about
infinite carriers (paper only); exhaustive three-state models over the larger value structures
(sampled only); and the exact statements of
the cited classical sources (diagonal similarity, the probabilistic-automaton bound, the
abstract-interpretation completeness literature, the descriptive-set-theoretic completeness
result), all written from memory.

## 6. Receipts

**Repository state**

- Repository `femboy2112/SUCC`; branch `ccr-db6a5bf5-l6g6wu` (the session's designated
  non-main branch); base `db9fb4b84672050efa79b13377f1e73364598a14` (Main XXV).
- Draft pull request: [#620](https://github.com/femboy2112/SUCC/pull/620). Not merged, not
  tagged, not released.
- Last commit that changed code or tests: `b7616bc7db5ed15422adfe7111152d61a515700a`. Commits
  after it, up to and including `5bd0cd2ba1501eb36618a17c1cdebc484185f82c` and the commit adding this section, change documentation
  only.

**Local validation (this session's container, Python 3.13 unless stated)**

| Command | Result |
|---|---|
| `python scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED` |
| `python scripts/observer_foundations_probe.py` | exit 0 |
| `python scripts/ordinal_succ_report_probe.py` | exit 0 (after installing the test extras) |
| `python -m unittest discover -s tests -p 'test_*.py'` at `b7616bc7` | **13,305 tests, OK** (23 min 41 s) |
| same command, earlier intermediate tree | 13,227 tests, 1 error: an existing test shells out to a probe that imports the package, which was not yet installed in the container; it passes after `pip install -e .`, as CI does |
| `python -m unittest discover -s tests -p 'test_observatoris_*.py'` | 255 tests: 15 classical appearance, 45 finite horizons, 42 finite observer, 7 integration, 45 quantale quotient, 29 + 39 referee receipts, 33 response geometry |
| the same 255 tests under Python 3.11 | OK (run before the last test edits; counts unchanged) |
| `python scripts/check_observatoris_lean.py` (Lean 4.14.0) | `KERNEL_CHECKED`; 18 declarations; no axioms; both controls pass; source sha256 prefix `b326f653bc84dcda` |

**Continuous integration on the pull request** (read once, at the time this section was written;
not a claim about later pushes): 20 of 21 check runs had completed, all successful, including
the dedicated exact-model jobs on Python 3.10 and 3.13, the pinned-Lean kernel job, and the full
suite on Python 3.13. The full suite on Python 3.10 was still in progress. Python 3.10 was not
available locally.

**Not done**

- No independent check of the cited literature.
- No proof-assistant formalisation of the delegated paper proofs beyond the declarations listed
  in §4 (the finite-observer, finite-horizon, response-geometry and causal-horizon theorems are
  paper proofs with exact tests).
- No comparison with, or use of, the parallel axiomatic campaign.
