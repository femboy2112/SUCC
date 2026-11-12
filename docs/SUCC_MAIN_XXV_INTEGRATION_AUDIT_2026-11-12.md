# Main XXV — frontier rungs integration audit

**Scope:** exact-history integration of the open research fronts onto Main XXIV, and the round of
theorem building and audits that preceded it. π normality, R0, R1, digit-change density (CH),
original-zero parity, Goldbach and RH remain OPEN. See the
[manifest](SUCC_MAIN_XXV_INTEGRATION_MANIFEST_2026-11-12.json),
[governing corrections](CLAIM_SUPPLEMENT_MAIN_XXV.md), [frontier](PI_NORMALITY_FRONTIER.md) §9 and
[handoff](MAIN_XXV_HANDOFF.md).

## Baseline and graph

Baseline: Main XXIV `071ce1e0ee6ab8f8c07113e901131aa646d6b95d` (merge of #598), tree
`666d586c1827380f58f11eea1862e3703b983e9e`, equal to `origin/main` throughout. All remote
branches were fetched. Open pull requests at the time of integration:

| PR | Branch | Head integrated | Own base | Disposition |
|---|---|---|---|---|
| #599 | `research/innovation-arithmetic-decoupling-2026-11-11` | `8de33430` (its head) | `071ce1e0` | integrated in full |
| #602 | `research/frontier-rungs-restricted-exponent-2026-11-12` | `29ecc96d` (its head) | `8de33430` (stacked on #599) | integrated in full |
| #601 | `research/prime-fixed-point-observer-2026-11-12` | `836d0380` — **audited snapshot**, not the head | `071ce1e0` | integrated at the snapshot; the branch received a further commit (`b3ddf81c`) during the audit; that commit is not integrated and the pull request stays open |
| #600 | `research/prime-fixedpoint-cylindrical-interferometer-2026-11-12` | `8bf797d7` — **audited snapshot**, not the head | `071ce1e0` | integrated at the snapshot; the branch received a further commit (`f8142d02`) after the audit; not integrated; the pull request stays open |

The integration branch `integration/succ-main-xxv-frontier-rungs` is the #602 head plus two
`--no-ff` merges of the pinned snapshots, plus integration documents. Every integrated head is an
ancestor. No shared history was rewritten, nothing was force-pushed, no tag or release was made.
The only merge conflict was in the generated `docs/math_memory/CLAIM_CATALOG.json` (#601 against
#599/#602), resolved by regeneration; the catalog is regenerated last.

Older unmerged remote branches (dispositions recorded by Main XX–XXIV) were not revisited. The
PR-less branches `research/prime-three-channel-phase-tomography-2026-11-08` and
`research/cayley-inverse-pi-two-sheet-2026-11-09` remain outside main, as Main XXIV left them.

## What was built before integrating (#602)

Starting from a reading of the Main XXIV frontier and of #599's named next probe, five parallel
bearings, then one audit of each new theorem file (all separate instances of the same model
family; none is external refereeing):

| Bearing | Outcome |
|---|---|
| Limit-measure faces and thresholds | LMF-01…06. Three provisional constants of the preregistration were wrong and were corrected by the bearing itself, with counterexamples |
| Restricted-exponent transference | RDT-01…08. The round's provisional criterion (`α + σ − δ > 0`) and "series criterion" were wrong and were replaced |
| Literature verification | Rivoal 2007 found and read at source (the import of RDT-07); the recollected "Rhin 0.79" bound for `log 2` refuted as a misattribution; grades in the dossier's SOURCE_MAP |
| Re-audit of #599's repaired passages | no displayed theorem blocked; three false prose sentences fixed |
| Lean check | 33 exact statements kernel-checked, 9 mutants refuted; re-run by the integrator |
| Audit of LIMIT_FACES | all displayed statements approved; two false summary sentences, one proof gap, repaired |
| Audit of RESTRICTED_EXPONENT | nothing blocked; headline numbers recomputed independently; four false or unsupported sentences repaired |

Theorem files were committed before their audits; every repair is a separate commit. Repairs made
after an audit were not audited again. Details and what was not done: the dossier's
[VALIDATION](../research/2026-11-12/frontier_rungs/VALIDATION.md).

## Review of the contributed snapshots (#600, #601)

Each snapshot was checked out in a throwaway worktree by a read-only auditor: scope (only their own
`research/2026-11-12/` directories; no path under `provenance/`, `observational_succ/`, `formal/`,
`tests/`, `scripts/`, `.github/`; no licence file; no binary; no new file above 1 MB), claim
discipline (every statement labelled proved was re-derived, with explicit matrices for the operator
identities of #600), executable checks, mutation controls, repository gates and hosted checks.

| Snapshot | Dossier tests | Receipts | Mutants | Hosted checks at the snapshot | Verdict |
|---|---|---|---|---|---|
| #601 `836d0380` | 47 OK; probe 74 229 checks, 0 failures | `FINITE_REPORT.json`, `CYLINDER_REPORT.json` reproduced byte for byte; 42 manifest hashes match | 7 of 9 informative mutants killed by tests; one survivor is a boundary flag, one was semantically equivalent; one stopped for machine load and rejected by a substitute check | 19 of 19 success | integrate with corrections |
| #600 `8bf797d7` | 28 OK; two asserting probes pass | three receipts byte-identical; two differ by a trailing newline from the documented command | 11 of 14 killed; two tests cannot fail and one is tautological | 19 of 19 success | integrate with corrections |

All corrections are wording, labelling, citation and test-hygiene points; none affects a proof.
They are recorded in the [claim supplement](CLAIM_SUPPLEMENT_MAIN_XXV.md) §3 and govern the
interpretation; the contributed files were not rewritten, because both pull requests are still
being developed by their authors. One cited number in #600 is wrong (an explicit Chen threshold
quoted as `exp(36)`; the literature has `exp(exp(32.7))`); nothing depends on it.

Tautological assertions noted in #601 (not evidence, harmless): `test_prime_observer.py` lines 21,
52–54, 144, 146; `test_cylinder.py` lines 51, 102–105; constant fields written by `cylinder.py`
lines 184–191, 202. In #600: `test_prime_cylinder.py` lines 203–204, 249–262; `test_carrier.py`
lines 255–263, 304–306; `carrier_probe.py` lines 89–93; `test_scott_defect.py` lines 322–329 never
calls the function under test.

## Protected bytes

The 83 protected paths of the Main XXIV manifest (frozen sources, archives, original tests and
probes) have the baseline blobs at the candidate; `scripts/main_xxv_manifest.py --check` verifies
this together with ancestry and contribution bytes. `provenance/`, `observational_succ/` and
`formal/` are untouched. The Main XXIV frontier and README are archived byte for byte under
`docs/archive/`.

## Machine note

During the audits a peer session on the same machine reported sustained load; subsequent heavy
runs of this integration (Lean check, research gate, native suite) were serialised through the
shared lock and run at reduced priority. One mutation run of the #601 audit was stopped for that
reason and replaced by a bounded check, as recorded above.

## Validation

Recorded in the final documentary commit of this integration (the section below), for the exact
content candidate named there, and in the pull request description.
