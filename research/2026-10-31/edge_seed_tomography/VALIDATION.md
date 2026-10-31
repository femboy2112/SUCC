# Validation, exact boundaries, and reproducibility

**Baseline:** Main XVII `e8598cfa5d32fd1de8e94a3e458a366a0850d59e`; stacked parent #431 `cf23b8cfc39f56935c432ed764adf0a33efb0d7e`. This package is all-additive. The original four-pole function and authentic `U_0=0` were read from the repository and preserved. All source simulations with changed initial state carry explicit counterfactual seed labels.

## Local runs (actual execution, no assumed CI)

Execute from repository root:

```sh
python -m unittest discover -s tests -p 'test_edge_seed_tomography.py' -v
python research/2026-10-31/edge_seed_tomography/independent_oracle.py
python research/2026-10-31/edge_seed_tomography/edge_seed_tomography.py
python research/2026-10-31/edge_seed_tomography/probe.py > /tmp/edge_seed_finite_diagnostics.json
```

**Local stdlib test result:** 21 / 21 discoverable `unittest` methods PASS. Distinct implementations: recurrence vs direct finite BBP convolution; Gaussian-binomial-free integer fourth collision enumeration vs formula; prime grid sparse label map vs brute modular sums; independent exhaustive 73-point line/point incidence; exact phase classes vs numeric 73-point DFT *sanity only*. The finite graph/path measures from parent #431 were not modified.

**All-horizon paper proof claims** are separate from these local checks: ESM-01/03 source edge transport, ESM-02 invariant Haar reflection, ESM-04/05/06 phase Fourier and 73-geometry, ESM-07/08 lacunary moments, ESM-09 rational hostile control. No Lean kernel receipt for these claims. No external referee. Do not infer anything asymptotic about selected π digits from local finite samples.

**Explicitly NOT RUN locally:** `python scripts/verify_provenance.py`, root full `python -m unittest discover -s tests -p 'test_*.py'`, `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py` on a full repository checkout (the container holds the research package, not the complete SUCC tree). These are mandatory integration/CI gates. The 21 focused tests and the parent #431 tests do not substitute for them.

## Independent controls retained

- h=73 at modulus 73: ALL phase frequencies alias; the exact tomography API raises rather than claiming recovery. Modulus 17 at N=9 similarly fails.
- `f(x)=1+cos(2πx)` is non-Haar yet multiplication by 15 maps it to Haar; false positive without dynamics.
- Original changed rational seed `s_K=-c_K` maintains nearly coherent finite source phases while changing the initial condition. The fixed nonnormal `s*=-π/16` is an independent all-horizon hostile control from CRPM.
- Root-of-unity phase models have identical averaged 2nd/4th moments as source phases without proving selected cancellation; the full off-diagonal intensity and the chosen seed do distinguish them.
- Fourth moments and phase-recovery are exact finite group-algebra identities. Approximate numerical DFT / complex amplitudes are quarantined under `FINITE_DIAGNOSTIC_ONLY_NOT_PI_PROOF` in the JSON receipt.

## Source provenance and external mathematical checks

Original-source specification: SUCC Main XVII `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`; CRPM PR #431 `PROOFS.md`; triangle selected sensor PR #426; source 3-adic pole-depth PR #430. Governing rules: `AGENTS.md`, `docs/METHOD.md`. Classic normality-preserving multiplication is due to Wall; finite cyclic difference sets and projective planes are classical. References and precise mathematical derivations live in `PROOFS.md`.

**Do not extrapolate:** local prime sampling p is a Fourier information-preserving *measurement grid*, not an independent p-adic Euler factor, a quantum state, or a proof that arithmetic cofibers transfer to π. This research provides a better instrument and an equivalent edge gate, not the missing source-specific signed estimate.
