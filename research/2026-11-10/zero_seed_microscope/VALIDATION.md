# Execution, provenance and exact status

Date: 2026-11-10. Branch `research/zero-seed-radix-microscope-2026-11-10`,
created from `41bbbe56bbb36bcbf2a171669bf508caea6f688b` (draft #591).

## Actually executed in this work session

- Python 3.13 standard-library unit tests: **22 methods passed**, ~0.77 s.
- Positive controls: several rational alpha choices, exact orthogonality,
  exact integer counts, zero-cell Fourier DFT reconstruction, independent
  midpoint Riemann quadrature, independent closed-form formula for first
  `h=8` detail, exact rational source-prefix and Machin interval overlap.
- Hostile controls: coherent completed zero alpha=0 has nonnormal Weyl mean
  1 despite annealed Parseval; injected wrong forcing term or tail budget is
  rejected at each tested finite clock; invalid booleans/float frequencies
  rejected; nonmonotone signed microscope increments observed.
- Strict rational analytical proof receipt:
  `certify_first_weyl8_detail()` mechanically verifies exact Machin arctan
  bounds, `3/8<pi(15pi-47)<2/5`, `sin delta>1093/3000>1/3`,
  and the geometric series `sum_(n>=2) 1/(16^n-1)<1/225`.
  This yields a *paper* theorem valid for all `N>=2`, not an
  extrapolation from the sample table.
- Python source compile check: `python -m compileall` succeeded.
- Finite diagnostics from genuine four-pole source for N=2,4,8,16,24
  at h=8; see `receipts/seed_microscope_receipt.json`.

**Important execution boundary:** this workspace did not have a full
network Git checkout. For local tests it used a small, disclosed scratch
compatibility module defining `duck_bbp.forcing` by its exact authenticated
rational polynomial and `source_tail_budget(n)=forcing(n+1)/15`.
That scratch shim is **not** included in the PR. On the actual repo the
module imports the inherited canonical `observational_succ.duck_bbp`.
These focused tests are not the ~13k inherited native SUCC suite and do
not certify the branch against all dependency combinations; hosted PR
checks must be evaluated on their own SHA. The implementation's exact
source check cross-computes the original four signed pole expression.

The first failure in development was the floating kernel conjugacy test
at tolerance `2e-14`, with observed residual `2.82e-14`. We eliminated
negative-frequency numerical cancellation by defining the negative-q
kernel as the exact complex conjugate of its positive-q implementation.
Reran full focused suite after repair. No mathematical sign was inferred
from the prior floating failure. Similar finite resolution and witness
checks remain explicitly numerical where trig functions are evaluated.

## Claims by scope

- **PROVED PAPER:** MS-01 to MS-04 exact identities and all-N
  signed first seed-cell h=8 detail, conditional on the classical BBP
  and Machin identities. No new external referee/Lean proof.
- **OBSERVED FINITE:** float complex microscope energy values; these
  have separately certified exact rational BBP phase-source truncation
  budgets, but no rigorous floating transcendental rounding enclosure.
- **UNVERIFIED:** any source-specific signed estimate driving the deep
  zero-cell tower to zero; the main dyadic statistical contraction
  for authentic pi; digit parity; pi base-16 normality.
- **REFUTED:** inference from source-blind spatial annealed cancellation,
  or from a single O(N^-2) signed packet, to actual selected normality.

## Reproduce in an installed SUCC checkout

```bash
python -m unittest discover -s tests -p 'test_seed_microscope.py' -v
python research/2026-11-10/zero_seed_microscope/probe.py
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

The last four lines are mandatory repository gates for an eventual merge,
**not** claims about commands executed in this work session.

## Additive fixed-depth infinite-series fingerprint, second pass

- **22/22 focused tests PASS** (Python 3.13, 0.714 s on the last clean
  run) after adding fixed-depth coefficient evaluation and hostile checks.
  The unchanged canonical source shim was still needed for the isolated
  local testing workspace; no full-repo suite is claimed.
- Proved on paper the absolutely convergent signed kernel coefficient
  `A_(K,h)(alpha)` for every fixed K, with rational omitted-tail certificate
  `512*K*16^(K-N)/(675*|h|)`. The identity follows from the same exact
  high/high orthogonality as MS-01 and not from fitted source data.
- An independent **mpmath 100-digit evaluation** of the closed-form genuine
  `h=8,K=1` sine series agreed with the separate complex-cell-kernel
  implementation at N=4,8,12,20 to the prescribed analytic tail bound
  plus a `1e-12` floating allowance. The approximate limit was
  `0.0336650405099602078179239647489392279333`. The result is a
  numerical calibration, **not** a rigorous mpmath enclosure or an
  asymptotic normality proof. Full receipt:
  `receipts/fixed_depth_fingerprint.json`.
- The first attempted ad hoc mpmath import omitted registering its
  dataclass module in `sys.modules`, producing a Python dataclass import
  error before executing any mathematical assertion. Registering the
  module correctly fixed this local harness state; the actual unit-test
  loader already used the correct setup. The successful rerun was retained.
- `python -m compileall -q` succeeded on both changed Python files.
- All proof-status labels remain: fixed-depth fingerprint PROVED PAPER,
  numerical phase data OBSERVED FINITE, and signed *deep*-scale BBP
  cancellation, statistical contraction, pi digit parity and pi normality OPEN.
