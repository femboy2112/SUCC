# Cylinder-front validation and scoped route ledger

All commands ran in the new PR411 child worktree, with parent Git HEAD
fa598e3a5a1111c3445200f1ddf48dcdea6bdc09, Python 3.13.13 from the existing
`../SUCC-zero-dispersion/.venv/bin/python`. No packages were installed and no
historical file was changed. The bounded runner is copied unchanged from
PR405's `zero_boundary_dispersion/run_receipt.py`; each command records argv,
working directory, start/end UTC, exit status, one-thread setting, 1024 MiB
limit, and raw-log hash. Repeated runs are not added to the test count.

| Run | Actual result | Authority |
|---|---|---|
| `receipts/focused-final.*` | 10 unit tests PASS | Exact finite regression |
| `receipts/exact-probe-final.*` | 320 BBP digits, 20 source blocks, 1021 rational transducer cases, 432 constant-word reverse cases; 0 ambiguities | Exact rational plus bounded Green intervals |
| Same exact probe | 7 Stoneham complete grids, conductor-2 failure, period-two all-slip control, 10 context-resolved Walsh rows with all 15 masks | Exact finite controls |
| `receipts/oracle.*` | 320 independently certified Machin digits and combined-source slips; 3 fresh Stoneham stages; 25 Gram identities | Distinct exact algorithms |
| Same oracle | 5 periodic Fejer values and 3 completed Stoneham energies at 90 decimal digits | Numerical calibration, **not** interval evaluation of trigonometric functions |
| `receipts/kernel-review.*` | 5 fresh spectral moments, 7 source-tail cases, symbolic K01 constant and K02 Mellin value | Same-model complementary proof check |
| `receipts/arithmetic-review.*` | 3 rational quadrature holdouts; 6 moments from geometric shifting; a new exact two-node witness | Same-model complementary proof check |

`receipts/probe.json` is the initial exact data payload; its bytes equal the
final exact-probe log. The final producer adds checks for C1's lower transition
bound and the h=17 resonance without changing the data. Initial passing
focused/exact-probe receipts remain retained. No test failure was suppressed.
A read-only inspection guessed an absent filename `positive_quadrature.py`;
the actual `quadrature.py` was then opened. This was not a mathematical run.

The oracle's Stoneham truncation has an independently bounded omitted energy
below 10^-100 in all three rows. This bounds the omitted series only; mpmath
arithmetic still is not certified interval arithmetic. The universal upper
bound is established by the paper proof, not by those decimal values.

## Executed proof-route verdicts

| Candidate | Result | Surviving obligation |
|---|---|---|
| Identify low-slip and hex cylinders literally | REFUTED as equality; exact source-shifted multiplication-by-15 preimage retained | Use C1's inclusions and full tail correction |
| Relate low-slip budgets to selected word organization | PROVED LOCAL: (K-2)/2<=C<=2K for h=1, A>=2, delta=1/20 | Prove a new arithmetic lower density for C if pursuing this weaker target |
| Positive-density lag-one slips bound moving collisions | REFUTED universally by period-01 same-forcing changed seed; every late position slips but F>=H/2-o(1) | Retain multiple frequencies and context; h=17 reveals this control |
| Balanced short Walsh contexts imply all-depth contraction | REFUTED by periodic order-two de Bruijn | Source-verified all-context signed inequality |
| Stoneham direct modular grid yields moving finite-band bound | PROVED LOCAL recovery with improved leading constant c | BBP lacks the bounded-multiplicity grid premise |
| Source tail, finite jets and zero seed isolate pi's arithmetic | AQ02 countermodels pass complementary reconstruction | Must retain globally prescribed four-pole structure |
| Stronger positive-density pi dispersion from this front | DARK | No such all-horizon bound proved |

This front does not claim new Lean authority, hosted CI, a root-suite run, or
an external referee. Root integrates its own validation separately. Main,
the authentic source, original zero boundary and author provenance are intact.

## Replay

From repository root, using the same existing Python environment:

```sh
../SUCC-zero-dispersion/.venv/bin/python -m unittest discover -s research/2026-10-30/selected_finiteband/cylinders -p 'test_*.py' -v
../SUCC-zero-dispersion/.venv/bin/python research/2026-10-30/selected_finiteband/cylinders/cylinder_probe.py
../SUCC-zero-dispersion/.venv/bin/python research/2026-10-30/selected_finiteband/cylinders/independent_oracle.py
../SUCC-zero-dispersion/.venv/bin/python research/2026-10-30/selected_finiteband/cylinders/kernel_review.py
../SUCC-zero-dispersion/.venv/bin/python research/2026-10-30/selected_finiteband/cylinders/arithmetic_review.py
```

For fresh command receipts use the same runner with a new `--name`; it rejects
overwriting historical receipts.
