# Validation and reproducibility

Universal claims are justified by [the written proofs](THEOREMS.md).
These receipts audit their finite implementations, endpoint signs,
source identity and numerical coordinate changes. They are not an
infinite empirical proof, new Lean certificate, or hosted-CI result.

## Actual executed checks

| Check | Result and exact scope |
|---|---|
| Full inherited discovery suite | **13,288 tests PASS**, 1058.645 seconds, exit 0. Discovery started at pinned parent `55bcde3d0c5ceb47d50cb499bd39f4a97c96bfc5`, before either new test file existed. |
| Final focused suite | **143 tests PASS**, 2.500 seconds, exit 0, including **44 new tests**: 30 causal-order/Mellin tests and 14 complete-source inverse tests. |
| Required source provenance | **PASS**, exit 0; 72 registry items, including 17 byte-identical research archives. |
| Required observer-foundations probe | **PASS**, exit 0; raw structured output retained. |
| Required ordinal-report probe | **PASS**, exit 0; raw structured output retained. |
| Independent Fraction audit | **PASS**, exit 0, no production imports; 1,375 source-face identities, 275 native-source identities, 11 first contacts, 468 stencil identities, 36 variation identities, 32 attained-noise identities, 18 finite-sample rivals, 192 entire-noise controls, eight negative-distribution controls. |
| Deliberately false rules | **8/8 distinguished** by the independent audit: difference orientation, positivity replacement, lost initial value, erased Gamma contact, native even-zero claim, extra endpoint zero, deleted original channel, and erased noise amplification. |
| Independent SymPy polynomial oracle | **PASS**, exit 0; global cleared inverse identity for every implemented depth 0..8, plus 33 native endpoint values from a separate Euler-derivative recurrence. SymPy 1.14.0; exact QQ arithmetic. |
| Positive-kernel coordinate diagnostic | Root replay: **30 numerical rows** and **10 labelled analytic zeros**, 40 decimal digits, mpmath 1.3.0, depths 8,32,128,512,2048. Two coordinates agreed within `1.3776e-40`. Numerical quadrature is **not** an interval certificate. |
| Proof review | Constructor, adversary and translator reviews closed at theorem SHA-256 `112634fd9d370be421b5ca4d9619c9ea01fd259b8cdbd4ecef6f97f422db04f1`. Same-model/shared-source dependence is disclosed. |
| Concurrent suspension appendix | Root read the complete pinned #638 theorem file. Adversarial follow-up checked the supplied quotient/path/variance construction and closed three scope qualifications. No companion code was imported or executed, and its test counts are excluded. |

Counts across full, focused, and agent baseline runs overlap and must
not be added as distinct tests. The final focused log lists the nine
included filename patterns. The parent baseline and the final focused
run are not described as one final-tree full-discovery run.

## Meaningful controls in the new tests

The causal stencils annihilate lower-degree polynomials, recover the
correct distributional sign, attain the smooth-test error bound on the
next monomial, and attain the worst-case noise bound. Tempered negative
orders obey the binomial convolution law. Input validation rejects
floating-point, boolean, noncausal, and out-of-budget inputs.

The original inverse is checked against literal four-pole fractions,
raw pole-factor multiplication, and actual convolution endpoint jets.
For depths 1..4, convolving the source power with its inverse yields
exactly the unit delta and zero regular jets through order 18. Omitting
the highest delta derivative, the regular remainder, or a source pole
is detected. These are finite controls of a universal rational identity
proved in CN-03.

Negative-order source values are computed both through exact geometric
power sums and independently through local exponential-series division.
The root SymPy oracle differentiates the literal rational heat kernel
in its exponential coordinate, using neither of those algorithms.
The exact source-face tests include 0..24 Taylor degree, several
regulators and rational ages, the implemented maximum order 64, and
the face-depth boundary 24.

The late Hasse/Pascal addition is tested against independently computed
Bose heat coefficients for orders 0..48. Applying identical positive
grade weights to the original BBP faces yields exactly 8 at order -2,
while eta and zeta yield zero. The universal grade family and its
truncation theorem are credited to the inherited dossier.

## Numerical limit is slow, and the receipt preserves that

For `C_k(s)=((log k)/8)^(1-s) B_k(s)/B_k(1)`, the diagnostic gives
`C_8(2)=5.3375437...` and `C_2048(2)=2.1072468...`, while the proved
limit is one. We do not call these depths asymptotically accurate or
infer an all-depth error rate from them. The proof instead establishes
eventual uniform positive and inverse moment control on each compact
complex order set.

The two numerical coordinates use different expressions for the same
source: positive exponential differences in causal time and the
factored polynomial in the exponential coordinate. They share mpmath
arithmetic, so their agreement is a consistency probe, not independent
experimental confirmation. Exact negative-integer zeros in the receipt
are explicitly labelled algebraic consequences rather than measured
quadrature values.

## Invocation history and artifact review

An initial ad hoc SymPy check repeatedly differentiated uncollected
rational expressions and expanded excessively. It was interrupted with
exit 130 before reporting a pass or failed assertion. The final
`root_symbolic_audit.py` keeps polynomial numerators and completed its
larger exact scope in 0.136 seconds; both the interruption metadata and
successful receipt are retained. This was a representation-cost issue,
not a failed mathematical identity.

An intermediate documentation scan ran before this validation file
existed and also mistook inline Mellin notation for Markdown links.
The final scan excludes mathematical/code spans and checks actual file
links. No theorem was changed to satisfy that formatting check.

The closed proof-review clarifications are: eventual inverse-moment
bounds, distinction between source depth and derivative order, an
explicit fixed-radius Hankel branch, the compact-parameter proof of
the entire source group, and explicit provenance for the late
Pascal/Hasse recovery. Raw review history remains in the agent notes.

## Reproduction

Run from the repository root with Python 3.12 or a compatible interpreter:

```bash
PYTHONPATH=. python scripts/verify_provenance.py
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=. python scripts/observer_foundations_probe.py
PYTHONPATH=. python scripts/ordinal_succ_report_probe.py
PYTHONPATH=. python -m unittest discover -s tests -p 'test_causal_negative_orders.py'
PYTHONPATH=. python -m unittest discover -s tests -p 'test_bbp_causal_inverse.py'
PYTHONPATH=. python research/2026-11-15/causal_negative_orders/independent_audit.py
PYTHONPATH=. python research/2026-11-15/causal_negative_orders/root_symbolic_audit.py
PYTHONPATH=. python research/2026-11-15/causal_negative_orders/face_limit_probe.py
```

The two production modules and their ordinary tests use the Python
standard library. The separate symbolic and quadrature audits require
SymPy and mpmath respectively. The original source files are not edited.

## Receipt index

- `receipts/full_baseline.log`: inherited full-discovery raw output.
- `receipts/focused.log`: final 143-test run.
- `receipts/focused_initial.log`: initial 26-test causal-order run,
  preceding the four Hasse additions and separate 14-test inverse run.
- `receipts/provenance.log`, `foundations.log`, `ordinal.log`: required
  native probes with their exact outputs.
- `receipts/independent.json`: production-free exact controls.
- `receipts/root_symbolic.json`: exact global polynomial identities and
  native Euler derivatives.
- `receipts/symbolic_invocation_history.json`: interrupted exploratory
  expression form and successful replacement explanation.
- `receipts/face_limit.json`: translator's quadrature run.
- `receipts/face_limit_root.json`: root replay of the same declared grid.
- `receipts/proof_review.json`: final reviewed hashes and closed fixes.
- `receipts/environment.json`: versions and pinned baseline.
- `FILE_HASHES.json`: final payload manifest, excluding itself.
