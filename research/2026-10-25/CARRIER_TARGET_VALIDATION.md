# Carrier-relative target descent — validation and authority

Pinned parent: `461942c0bf616518e668d236d1c6b1596665a7dd` (PR #296).
Branch: `research/carrier-relative-target-descent-2026-10-25`.
Research date: 2026-10-25. This branch adds a foundational observer instrument;
it does not modify either concurrent mathematical attack in PR #297 or #298.

## Executed local checks

Python 3.13, isolated local package staging, no original-source API shims:

- `python -m unittest discover -s tests -p test_carrier_relative_targets.py -v`: **23 passed** (1.589 s on the recorded run).
- `python -m unittest discover -s tests -p test_carrier_finite_part_observer.py -v`: **6 passed** (0.012 s).
- `python scripts/carrier_relative_targets_probe.py --write research/2026-10-25/CARRIER_TARGET_RECEIPT.json`: receipt generated.
- `python scripts/carrier_relative_targets_probe.py --verify`: exact replay passed.
- `python -m compileall -q observational_succ tests scripts`: passed.
- Mutation: change the receipt's `pi_normality_proved` from false to true; verifier exits nonzero with `receipt/source mismatch`. The failed mutation is retained in `CRT_MUTATION.log`.

Raw targeted logs: `CRT_LOCAL_TESTS.log`, `CRT_FINITE_PART_TESTS.log`.
The JSON receipt binds both production modules by SHA-256. Algebra witnesses
separately bind their entire declared source by a deterministic model digest.
A digest is not independent proof of empirical source adequacy.

## Independent finite oracle scopes

| Instrument | Exact scope | Result |
|---|---|---|
| Word enumeration vs partition/algebra closure | All 234 one-instrument binary-output models on 1, 2, 3 states | Same behavioral partition; algebra dimension equals class count |
| Target row-span vs quotient constancy | All 1,796 Boolean target tables in those models | Same target-identifiability verdict; returned obstruction pair checked |
| Separate policy tree search | All 4,096 two-state/two-instrument/binary-target/budget cells, budgets 0..3 | Same policy existence; independent execution verifier and minimal cost check |
| Finite-part corner and interior controls | 200 declared remainder pairs | Target enclosed; two boundary remainder choices attain the sharp endpoints |
| Destructive-measurement counterexample | Three states, two erasing instruments | Full observable algebra but an explicit all-first-action merge witness forbids any single-copy identification policy |
| Common-state observer controls | Hidden-tag XOR, incompatible triple, altered units, wrong source/chart, forged recipes | Expected positive and negative controls pass |

These are finite implementation checks. The general finite-carrier and analytic
claims have separate paper proofs in `docs/CARRIER_RELATIVE_TARGETS.md`.
Two algorithms executed in the same assistant environment are independently
implemented checks, not independent researchers or external peer review.

## Claim authority

| Claim | Authority | Still required / boundary |
|---|---|---|
| Target factorization through observation quotient | Classical elementary proof; finite exact implementation | Common interpretation and nonempty fiber |
| Finite observable algebra equals class-constant functions | Classical finite algebra/behavioral equivalence; paper proof and two computational routes | Function algebra across counterfactual experiments is not one-copy executable access |
| Finite-budget policy correctness and optimum | Induction on positive cost; exhaustive finite oracle comparisons | Model-defined tools and actual carrier availability |
| All-horizon destructive access obstruction | Explicit finite witness covering every first action | Only the declared three-state model, not a general no-go for mathematical proof |
| Minimax target-error radius | Exact endpoint proof | Not a truth probability |
| Compact target oscillation shrinks without full identification | Classical compactness proof | Compact closed fibers, continuous target; no automatic effective modulus |
| Profinite continuous Boolean target is finite-stage | Classical compactness/cylinder proof | Normality is not continuous in unrestricted prefix topology |
| Abel finite-part two-scale certificate | Classical extrapolation and hyperbolic partial fractions; exact rational finite enclosures | Stated remainder/normalization law; divergent ordinary sum is unchanged |
| Native SUCC adapters and phase-purity regression | Tests committed | **NOT run locally**; actual original modules required |
| Pi normality, RH, physical carrier attestation | **NOT CLAIMED** | Separate source-specific proof/instrument obligations |

## Explicit unrun gates

A full Git clone was attempted but the local container could not resolve
`github.com`. GitHub connector reads and writes remain available, and original
repo interfaces were read there. The local staging contains an empty package
initializer only to run the new self-contained modules; that initializer is
NOT part of the commit. No existing SUCC code was copied with an API shim.

The three tests in `tests/test_carrier_relative_native.py` require the actual
CZB, compact-fiber and IMW modules. They were inspected against live interface
signatures but were not executed in this isolated staging. No native/full-suite
pass, Lean kernel result, provenance gate, or hosted CI completion is inferred.

Before promotion, run the native test and the required AGENTS.md checks in an
installed full checkout:

```sh
python -m unittest discover -s tests -p 'test_carrier_relative_native.py' -v
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

No historical namespace IDs or archival originals were altered. No academic
novelty claim, merge permission, or release authority is asserted.
