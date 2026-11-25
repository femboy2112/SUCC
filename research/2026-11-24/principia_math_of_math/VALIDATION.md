# Validation receipts — Principia mathematics-of-mathematics vertical slice

**Date:** 2026-11-24. **Code environment:** local isolated source-shaped overlay with CPython and Python standard library; optional independent SymPy spot check. This was not a full SUCC checkout. No hosted CI, Lean, full-root test suite or external mathematical referee was executed during this round.

## Scope and baseline

Repository source: femboy2112/SUCC. Pinned baseline Main XXVI at 81be6b897ae980b801a3b9de9e22ef81e8360bfb.

Current research branch: research/principia-math-of-mathematics-2026-11-24. All additions are opt-in and additive. No original BBP forcing, zero seed, archival theorem, frozen import, main/release history, or source checksum was modified. General root AGENTS.md gates remain required before any integration/claim promotion.

## Executed tests

Run from the local source-shaped root:

    PYTHONPATH=. python -m unittest discover -s tests -p 'test_principia_*.py' -q

**Observed output:**

    ----------------------------------------------------------------------
    Ran 24 tests in 0.006s

    OK

The 24 focused tests include source-typed affine path construction and exact cochain pairing; missing/fake composite prime; malformed and forged path; exact rational root/division/checker; source-zero and nonzero requirement; false p-power coefficient divisibility; forged quotient path; changed source ID; nonintegral polynomial; no fictitious gain from duplicate root; finite exact rational knowledge volume; hidden-coordinate activation by swap; nilpotent three-stage row-space ascent; duplicated/identity report rank stabilization; forged knowledge rank rejected by replay; full-rank but weakly conditioned 1/N determinant; and malformed source dimensions.

Run from the source-shaped root, with SymPy additionally installed:

    PYTHONPATH=. python research/2026-11-24/principia_math_of_math/independent_spotcheck.py

**Observed output:**

    INDEPENDENT_SYMPY_SPOTCHECK_PASSED 360 polynomial cases 100 knowledge-rank cases

The independent script uses a deterministic Random(20261124) stream. It constructs 360 nonzero integer-polynomial fixtures over radices 2, 3, 10, 16, genuine primes 2, 3, 5, 7, multiplicities and distinct-null depths, and checks exact roots and leading-coefficient bounds through SymPy's separate polynomial implementation. It also checks 100 independent exact rational row-space profiles via SymPy Matrix rank against the native Principia source-path enumeration.

**Fresh controls:** source mismatch and missing exact root are distinct from malformed code; the fake-composite case is a source-passport rejection, not a claim the integer identity fails for composite multipliers. No statistical distribution of π or \(\zeta\)-zeros was sampled.

## Exact uploaded-source identity audit

All five newly uploaded executable files were fetched through the GitHub connection from the research branch and their Git blob identities compared to the actually tested local source-shaped files via git hash-object:

| Path | Exact blob SHA-1 | Match |
| --- | --- | --- |
| observational_succ/principia_semantic_core.py | 949cd521841d15583aeb3853c14b8c94bc271187 | MATCH |
| tests/test_principia_semantic_core.py | 5202071bfe48842393dae6025716d13b96972a0d | MATCH |
| observational_succ/principia_knowledge_volume.py | 11e0fe5c7f13609f5061cacf4f99df2dcaa9a8de | MATCH |
| tests/test_principia_knowledge_volume.py | 3ae495e3c23b38d88ddd78dbc94ea2fd93c48a34 | MATCH |
| research/2026-11-24/principia_math_of_math/independent_spotcheck.py | db95049924ee7ae77051b660239b5ca77a943100 | MATCH |

The standalone SymPy test is an optional independent research script, **not** a root-test discovery dependency or an additional claimed 460 independent scientific experiments.

Also executed in the isolated overlay:

    python -m compileall -q observational_succ/principia_* tests/test_principia_*

Observed: exit status 0.

## Mathematical proof versus finite runtime

The universal source-null arithmetic capacity bound and the path/cochain algebra are supported by explicit classical derivations in THEOREMS.md, not by treating 360 finite randomized examples as a proof. The native code generates and checks finite certificates, and the independent implementation tests the arithmetic identities on held-out instances.

The conservative derivation-tagging and exact target-factorization theorems have classical proofs in THEOREMS.md; no independent formal-kernel certification is claimed. The full RH semantic reconstruction is a **research specification only**; there is no native theta-period integral map, no recovered global error estimate (M), and no SUCC-original RH proof.

## Required root gates NOT run in this environment

The repository's AGENTS.md demands these on an actual full checkout before integration:

    python scripts/verify_provenance.py
    python -m unittest discover -s tests -p 'test_*.py'
    python scripts/observer_foundations_probe.py
    python scripts/ordinal_succ_report_probe.py

They were **not** run here. Neither 24 focused passes nor cross-checks of uploaded bytes authorize a statement that full SUCC CI or the original RH Lean proof was rebuilt in this session.

## Most useful independent reproduction

On the exact branch HEAD, a future independent agent should first replay the above native and SymPy scripts, then perform root AGENTS gates, check branch/source fingerprints and existing PR #619/#633 source compatibility, and inspect THEOREMS.md without relying on code as mathematical authority. Most importantly, its first native RH reconstruction must supply an actual *two-place CM theta-period minor* whose p-adic and Archimedean bounds are proved in the same source model, or a precise counterexample to the proposed route.
