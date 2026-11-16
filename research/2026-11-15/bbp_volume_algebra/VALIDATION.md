# Validation and reproduction

## Executed results

| Check | Result | Receipt |
|---|---|---|
| Full inherited discovery suite | **13,257 tests PASS**, runner time 1057.332 s, process exit 0 | `receipts/full_baseline.log`, `receipts/full_baseline.json` |
| Final focused algebra and source suites | **104 tests PASS**, including **31 new tests** | `receipts/focused.log`, `receipts/focused.json` |
| Independent exact Green/carry/Gamma audit | **PASS**, all **11** false-rewrite controls distinguished | `receipts/independent.json`, `receipts/independent_run.json` |
| Independent prime-birth audit, budget 2048 | **69** primes, **253** source times, **343** separating frequency/prime pairs and **2 expected nulls**, PASS | `receipts/prime_birth.json`, `receipts/prime_birth_run.json` |
| Original source/archive provenance | **PASS**, 72 items, including 17 byte-identical archives | `receipts/provenance.log`, `receipts/provenance.json` |
| Observer foundations probe | **PASS**, exit 0 | `receipts/foundations.log`, `receipts/foundations.json` |
| Ordinal SUCC report probe | **PASS**, exit 0 | `receipts/ordinal.log`, `receipts/ordinal.json` |

The discovery suite was started at parent `e14d46c17a65e1e5f231c619657b9332caa181c0` **before either new test module existed**. The final focused run separately includes both new modules and their relevant inherited source dependencies. These are overlapping test scopes; the counts are not combined into a fabricated monolithic final-tree run. No hosted CI or new Lean result is claimed.

The full discovery output contains successful child-process summaries and JSON after the final `OK`. Its metadata uses the **last complete unittest summary**, not the first nested report and not an `endswith('OK')` check. An initial metadata parse selected the four-test child summary; this reporting selector was corrected against the raw log. There was no failing root test run. Python optimization was disabled for the independent assertion-based audit.

## What the 31 new tests establish

The **23 word/carry tests** compare the new normalizer with direct products and independent ordered-index enumeration, preserve distinct source labels, check formal associativity and distributivity on finite cases, and reconstruct the actual first 48 BBP states without supplied digits of pi. Full four-channel powers through degree four are compared with exact state powers. The product-radix, diagonal, initial seed and chronological-order controls distinguish false rewrites. Separate tests exercise the triangular polynomial lift, second-order rational state recurrence, exact carry cocycles, fundamental-phase lift moduli, Gamma cascade weights, increasing carry denominators and the tempering convergence gate.

The **8 kernel tests** reconstruct the literal source numerator separately and clear the complete polynomial denominator for **every power 1 through 12**. This is a different decomposition from production's local Laurent expansions. A direct Beta convolution of literal source Taylor series checks all twelve kernels through Taylor degree 28, including both the first nonzero coefficient and its next source-dependent correction. There are 72 exact positive-rational Laplace holdouts, a degree-64 endpoint coefficient, known powers one and two, highest-pole residue checks, immutable-source/type/budget controls, and false positive-residue, moved-pole and pointwise-product substitutions. The additional SymPy `apart` oracle ran successfully for powers 1,2,3,5; it was not skipped in this environment.

The general theorems are justified by the written proofs. Testing all powers up to the implementation budget certifies that bounded implementation, not an extrapolation to all positive integer powers.

## Independent arithmetic instruments

`independent_audit.py` imports no new or inherited SUCC production module. It uses exact integers and Fractions, with no random seed or floating tolerance. Its frozen domains are recorded in `ADVERSARY_NOTES.md`.

| Instrument | Exact cases |
|---|---:|
| Seeded graded Green product | 23,814 |
| Gamma cascade coefficient | 208 |
| Additive carry cocycle | 64 |
| Affine carry composition | 4,500, at three integer lifts each |
| Actual BBP chronological block | 1,330 |
| Gamma lift denominator | 820 |
| Defeated fixed carry modulus | 120 |
| Growing raw-BBP Gamma summand | 72 |
| Independent polynomial tail integral | 240 |
| Retained finite Green boundary | 240 |
| Tempered geometric partial enclosure | 136 |
| Critical integer-shape partial sum | 68 |
| Critical half-shape partial sum | 256 |

The audit's negative/zero radix samples check the elementary algebra on a wider scalar domain. The production word interface intentionally accepts positive rational radices, and the circle-compatible affine interface accepts positive integer radices. The wider audit is not a claim that the production interface exposes those extra cases.

`prime_birth_audit.py` reconstructs the source by both literal four poles and a combined rational expression, compares recurrence and direct convolution at birth endpoints, and constructs an exact CRT exponent fixing all earlier phases and the p-free cofactor while moving the newborn phase. At the root's budget 2048 it checks 69 prime endpoints and five fixed frequencies. Two cases deliberately have p dividing h and correctly fail to separate. It also checks 252 positive degree-one recurrence centers. Deleted-pole, changed-sign, changed-seed, zero-frequency and composite controls are explicit. These local automorphism certificates support the premises of VA-06; its universal conclusion requires the number-field and coefficient-descent proof.

## Mathematical review and provenance

The constructor, adversary and translator produced separate derivations and then cross-reviewed them. The parent independently reviewed the core formulae, implementation and exact receipt outputs. The checks found and resolved several scope/wording issues before publication: the power hierarchy needs k>=1; lift descent must specify fundamental input phases and a finite coordinate set; the formal associativity proof multiplies **all** active head grades; integration by parts needs its endpoint and regularity conditions; the cyclotomic conductor must be chosen p-free, here as the least common multiple. Historical review snapshots and the final LCM repair receipt remain in `CONSTRUCTOR_NOTES.md`.

The reviewed kernel constructor uses no symbolic runtime dependency. Its exact higher-power coefficients are computed from the complete signed source; the vanished jets are not hard-coded. Source labels are preserved even when a coefficient is zero.

All methods use shared source data, and all agent reviewers are from the same model family. This is code/decomposition diversity and mathematical cross-checking, not external peer review. Concurrent #636 was inspected by exact commit; its 29 tests and numerical diagnostics are not counted here.

## Reproduction commands

From the repository root:

```sh
PYTHONPATH=. python -m unittest tests.test_bbp_volume_algebra tests.test_bbp_gamma_kernel_algebra tests.test_gamma_source_volume tests.test_gamma_observer_descent tests.test_bbp_cyclotomic_birth tests.test_pascal_carry_joint tests.test_pisot_gamma_gluing -v
PYTHONPATH=. python research/2026-11-15/bbp_volume_algebra/independent_audit.py
PYTHONPATH=. python research/2026-11-15/bbp_volume_algebra/prime_birth_audit.py --max-prime 2048
PYTHONPATH=. python scripts/verify_provenance.py
PYTHONPATH=. python scripts/observer_foundations_probe.py
PYTHONPATH=. python scripts/ordinal_succ_report_probe.py
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
```

Environment details and pinned parent are in `receipts/environment.json`. Script hashes are included in each independent run metadata file. `FILE_HASHES.json` binds the deliverable payload except itself with SHA-256 and Git blob SHA-1. Publication verifies equality of the staged local Git tree and the created remote tree before opening the draft PR.
