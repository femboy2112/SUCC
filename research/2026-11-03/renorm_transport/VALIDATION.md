# Validation — RENORM transport

**Branch parent:** merged main `a673ec95` (Operation Selected-Current). Built off fresh main,
add-only. Preregistered held-out epochs/frequencies declared in `renorm_transport.py`
(`HELDOUT_A`, `HELDOUT_H`) before measurement; the grid deliberately extends past the
selected-current fit set (A=40/80/160) to fresh A=50/100/200/256 and h up to 200.

**Executed (compliant env: mpmath 1.3.0, PYTHONPATH=repo, not `python -I`):**

- `python -m unittest tests.test_renorm_transport -v` → **7/7 OK**, 0 skipped: immutable-source
  first terms + U₀=0 anchoring; `c_A(0)=1` calibration; two blind sources (zero-seed vs
  odd-conductor) identical phases and coefficients; RENORM-1 bound on held-out A∈{40,64,128},
  h∈{1,3,8,50,100}; non-vacuity (residual > 0.3·bound); barrier transports-not-shrinks;
  `build_receipt` 0 violations and π status OPEN.
- `renorm_transport.py --write FINITE_RECEIPT.json` then `--verify` ×2 → **deterministic**
  (`RECEIPT VERIFIED` both times). Receipt: `rigorous_bound_violations=0`,
  `worst_residual_over_rigorous_bound=0.980873`, `blind_source_max_abs_diff=0.0`.

**Instrument discipline.** `c_A(h)` is measured at a pinned `dps=50`; a fixed-precision
exponential sum is an instrument, calibrated on the known case `c_A(0)=1` and cross-checked by
a second exact source. The RENORM-1 *identity and bound* are exact/rigorous paper results; the
numerics only confirm the bound is satisfied and tight on the held-out grid — they do not
upgrade any status by accumulation.

**Falsification attempt (negative, recorded).** I tried to use RT-2 as a *source discriminator*:
a wrong-source mutant with scaled forcing `r'(n)=s·r(n)` (`s=3,5`) should, if RT-2 were a source
fingerprint, violate the BBP-calibrated bound. It does **not** — over `A∈{40,64}`, `h∈{100,200,400}`
the mutant residual stays well under the bound (e.g. A=40,h=200: mutant `0.065` ≪ bound `0.243`),
because the forcing term enjoys its own signed cancellation that the worst-case triangle bound
discards. **Conclusion:** RT-1/RT-2/RT-3 are *general* — they hold for any sequence
`U_n=16U_{n-1}+f(n)` with small `f` — and are **not** a source-selected cancellation law; the
source only enters through the constant in RT-2's derivation. This is consistent with the whole
firewall: the transport is structure, not a BBP-specific saving.

**Boundary (what this does NOT establish).** No fixed-scale `|c_A(h)|<1` improvement beyond the
inherited DC-1 modulus loss; no bound on `Σ_{|h|≤q_A²}|c_A(h)|²`; no π normality. The barrier is a
no-go for one method (iterating RENORM-1), not a size theorem. No native whole-repo suite, Lean,
or hosted CI claim is made for this draft branch beyond the focused test above; the consolidation
that it sits on was separately validated (see `docs/SUCC_SELECTED_CURRENT_MEGAROUND_INTEGRATION_AUDIT_2026-11-03.md`).

**π base-16 normality remains OPEN. RH remains OPEN (separate program).**
