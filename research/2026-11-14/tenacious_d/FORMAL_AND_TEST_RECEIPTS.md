# Proof authority and validation receipts

## Git provenance

The published integration object `df5bd184403abf9cfed452c396c6047074a485b9` has ordered parents `f9efa624da06a28e1a8ac99a56499acd11197928` (#619) and `5b7470c677135600c39f817064695308b86756f9` (#620). Its tree matches the local integration object byte for byte. All 86 paths changed across the parent packages matched their respective Git blobs at integration, including the nine-section founding note. All 53 entries of the Astra artifact manifest matched the pre-synthesis integrated tree. The present discovery catalog is regenerated to include the new research. Each historical catalog remains available at its originating revision. The containing synthesis commit binds every receipt below. [Full ancestry and input blob IDs](receipts/ancestry.json)

## Repository execution

The commands were run from the combined repository root. The full suite used `PYTHONPATH="$PWD"` so that scripts launched in subprocesses could import the checkout. The Python environment was 3.12.14. The six standalone synthesis probes use exact finite comparisons and require only Python and the supplied source modules. [Compiler, interpreter, Git and dependency versions](receipts/environment.json)

| Run | Exit and scope | Complete output |
|---|---|---|
| `python scripts/verify_provenance.py` | 0. Verified 72 declared provenance items. | [Provenance output](receipts/provenance.log) |
| `python -m unittest discover -s tests -p 'test_*.py'` | 0. 13,325 tests in 1,210.203 seconds. Two Lean-dependent skips passed on the separate replay below. | [Native discovery output](receipts/full_native.log) |
| `python scripts/observer_foundations_probe.py` | 0. Observer and epistemic controls. | [Observer output](receipts/observer.log) |
| `python scripts/ordinal_succ_report_probe.py` | 0. Ordinal and source-report controls. | [Ordinal output](receipts/ordinal.log) |
| Targeted discovery on `test_principia_observatoris.py`, `test_observatoris_*.py`, and `test_tenacious_acquisition.py` | Each exit 0. Astra 15, Fable 255 including two initial Lean skips, and five new acquisition tests. | [Astra](receipts/astra_targeted.log) · [Fable](receipts/fable_targeted.log) · [Acquisition](receipts/synthesis_targeted.log) |
| `python -m unittest -v tests.test_observatoris_referee_receipts.LeanEncodingReceipts` with pinned Lean on PATH | 0. Both cases skipped by targeted discovery were run and passed. | [Lean-dependent Python tests](receipts/lean_python_replay.log) |
| Six inherited standalone probes | All exit 0. Exact commands and durations recorded. | [Replay index](receipts/predecessor_replays.json) · [Astra](receipts/astra_exact.log) · [Separate implementation](receipts/astra_independent.log) · [Sharp rival](receipts/astra_sharp.log) · [Scale](receipts/astra_scale.log) · [Adaptivity](receipts/astra_adaptive.log) · [Ancestral](receipts/ancestral.log) |
| Six synthesis probes | All exit 0. A fresh execution reproduced all six JSON receipts byte for byte. | [Commands and SHA-256 values](receipts/synthesis_replays.json) |
| `python scripts/build_math_memory.py --check` and `python scripts/verify_math_memory_graph.py` | Both exit 0. 3,053 source documents. All 172 catalog warnings matched their parent values exactly. The curated graph has 51 nodes and 60 edges. | [Catalog](receipts/catalog_check.json) · [Graph](receipts/relation_graph.log) |

## What was independently compared

* [Descent](receipts/descent.json) compares the rooted relation instrument to literal partial-action tables and path languages, including 2,965 action/partition pairs, 2,594 independently labelled graph/partition pairs, small quantale products, and 961 word comparisons.
* [Stochastic and signed models](receipts/defect_gauge.json) compare endpoint hitting bounds with direct recursion, signed telescoping with explicit products, and 64 acyclic sign patterns with exact rational path sums.
* [Warning and classicality](receipts/warning_classicality.json) checks 512 information-set/control tables, 408 timing configurations, and 31,280 branch comparisons between density-matrix predictions and the two declared classical encodings.
* [Polyhedral interception](receipts/polyhedral_interception.json) checks destructive sensing and continuous commands against rational intersection tests, including Helly and simplex failures.
* [Weighted source forcing](receipts/weighted_forcing.json) compares Hankel matrices with exact four-pole samples, masking controls, and a held-out index. [Joint precision](receipts/joint_precision.json) compares a Jacobi sum with independent Gram elimination at 60 finite parameter settings, including onset 1200.
* [Acquisition tests](../../../tests/test_tenacious_acquisition.py) include a finite hidden-state policy game as a separate check of the rational optimal-recovery solver.

Alternate constructions and exact computations provide different evidence for the mathematical statements. The two forge histories share the founding conjectures. Multiple same-model reviewers do not establish independent external replication or historical priority.

## Kernel scope

The archive SHA-256 is `320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`. Lean 4.14.0, compiler commit `410fab728470`, replayed Fable's 18 public exports and both comparator/mutation pairs byte for byte. Inspection of all 63 explicitly named Fable declarations, including all 45 named theorems, found empty axiom dependencies. The bridge compiles the actual SUCC and Fable modules together. Its five axiom-free declarations include filtered endpoint exactness and the one-sided-unit countermodel. The sixth, combining endpoint exactness with the inherited ordered-word lift, inherits `propext`. A positive control compiled and a proposed false left-unit inequality was rejected. A second fresh compilation reproduced the audit and compiler output exactly. The minimality of four values, the arithmetic estimates and the wider operational results have paper proofs and finite controls. [Replay instructions and declaration inventory](lean/README.md) · [Compiler output](lean/compiler.log) · [Full typed audit](lean/audit.json) · [Fable export receipt](lean/fable_kernel.json)

The committed workflow replays the six synthesis receipts and formal bridge on changes to their sources. Hosted CI is an external observation at the PR head. Its live result is recorded on the draft PR.
