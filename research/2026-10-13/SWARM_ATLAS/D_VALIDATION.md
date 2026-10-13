# Cohort D reproducibility and status receipt

Branch: `research/swarm-d-2026-10-13`.
Frozen parent: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.
One real investigator owns eight dossiers; these are eight assignments, not
eight independently spawned agents. No other cohort's initial conclusions were
used to formulate this cohort's proofs. An independent-agent review was
requested from the principal; it is **not** claimed completed here.

## Assignment states

| ID | Verdict | Concrete surviving result | Unresolved target |
|---|---|---|---|
| D25 | CLASSICAL / PROVED LOCAL | Factor criterion and source-relative phase ablation | Natural logistic acim branch identification |
| D26 | CLASSICAL / PROVED LOCAL; BLOCKED for broad target | Typed refinement/time square and missing-bit no-go | Generic source-faithful logistic renormalization |
| D27 | CLASSICAL / PROVED LOCAL | Factor/Koopman/lumpability equivalences; nδ marginal and history bound | Incomplete/nonstationary/destructive source contract |
| D28 | CLASSICAL / PROVED LOCAL | Sharp full-tent precision/horizon budget | Certified analogous bound on specified other source |
| D29 | REFUTED broad target; PROVED LOCAL repair | General quotients erase Conley H₀; conjugacy preserves index pairs | Noninjective index-pair equivalence class |
| D30 | PROVED LOCAL | Invisible smooth velocity gives visible solenoidal LES force | Invariant class or stress/memory closure law |
| D31 | CLASSICAL / PROVED LOCAL | Covariant causal-cut restriction | Authenticated physical source or curved geometry |
| D32 | CLASSICAL / PROVED LOCAL | Sharp N−1 delay quotient and Hamming-noise margin | Fixed continuum sensor embedding and source completeness |

Eight dossiers delivered; seven broad missions have concrete theorem or no-go
verdicts. D26's broad renormalization theorem remains BLOCKED, with a proved
typed symbolic substitute and named missing construction. No Lean files were
added, no kernel proof was run, and no academic novelty, RH advance, physical
validation, or NS global regularity is asserted.

## Executed commands

All commands ran in the cohort worktree.

```sh
python -m unittest tests.test_logistic_observer_tree tests.test_chaos_source_quotient tests.test_misiurewicz_phase_quotient tests.test_relativistic_shadow_tower tests.test_galilean_lorentz_succ
python -m unittest tests.test_swarm_dynamics -v
python scripts/swarm_dynamics_probe.py > research/2026-10-13/SWARM_ATLAS/D_RECEIPT.json
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
git diff --check
python -m compileall -q observational_succ/swarm_dynamics.py tests/test_swarm_dynamics.py scripts/swarm_dynamics_probe.py
```

- Relevant immutable baseline: **143 tests, passed**.
- New targeted suite: **21 named tests, passed** after repairing a false
  midpoint fixture; the original run correctly reported one failure.
- Full local suite: **1,623 tests, passed**, 91.711 seconds in the observed run.
- Provenance: **72 imported items verified**, 17 byte-identical archives and
  55 namespace migrations. Frozen import commit
  `ba075348b7bcc66d938b3e0ca96c26e95bba340a` was inspected before adding code.
- Foundation and ordinal probes: **passed with exit zero**; their own RH and
  incomplete-formalization firewalls remain intact.
- Compilation and whitespace validation: **passed**.
- Probe JSON was independently reloaded and compared with a fresh `receipt()`
  result: **exact parsed equality**.

These are local checks. No GitHub CI result, remote push, PR creation, merge,
or release is implied.

## Exact calibration coverage

- 4,330 complete binary-readout deterministic source tables, N≤4, compare
  factor certificates with independently computed indicator-invariance tests.
- The same 4,330 tables compare N−1 delays with N² future expansion.
- 512 rational stochastic tables × three original states × five horizons:
  **7,680** marginal defect inequalities.
- A separate direct hidden-source path enumerator checks five full-history
  TV bounds; it does not call the marginal comparison helper.
- Full-tent cylinders through depth six, including every dyadic folding point
  needed by the direct iterate oracle, test exact interval images.
- Fourier convolution for N=2,…,11 independently checks retained LES tensors;
  additional N=19 and 101 controls check high-frequency hostile regimes.
- 735 exact event/observer/boost covariance checks.
- Positive, negative, null, malformed-input and transition/readout mutations
  are preserved. These computations certify finite implementations, not the
  continuum/general quantifiers, which are proved in the dossiers.

## Artifact hashes

| Artifact | SHA-256 |
|---|---|
| observational_succ/swarm_dynamics.py | b5da683b81fa83fa4ec120cbe29f6da3b9840345af7383f20364a2e3861eba52 |
| tests/test_swarm_dynamics.py | ce4f22c6d21d9ae200f0dba00a2b503fbf4b4f5d1e461156b6076f1590a5d063 |
| scripts/swarm_dynamics_probe.py | df2d21eccf69efcca3663be18062f9adfaf0e96bedabb65823f4cbcaa2a61a8c |
| D_RECEIPT.json | b919eed02342fc2289ee318728ec9c5ee577546c4ba80d5051b45cc328579e21 |

## Primary-source access record

Read 2026-10-13: Koopman 1931 original paper; Milnor–Thurston original interval
paper introduction/semiconjugacy context; Takens original Theorem 1 and its
precise compact manifold/C²/generic-pair hypotheses; Germano 1992 §2 filtering
assumptions and stress equation; Einstein 1905 introduction and §§1–2.
URLs and scopes are in their owning dossiers. All arguments actually used from
those sources are either carefully scoped context or rederived here.

Kemeny–Snell chapter scan was located but timed out on opening. Conley's
publisher/full-text routes failed or returned 403. Full texts are **not claimed
read**; their source-independent local proofs and exact countermodels carry
the conclusions. These provenance limits must not be erased at integration.

Commit identity is supplied by the branch's semantic implementation commit and
the principal's integration registry, avoiding a self-referential file hash.
