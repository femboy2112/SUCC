# Operation Spacetime Triangle — extrude, rotate, tile, Fourier

**DRAFT research, not a π-normality or RH proof.** Starts at Main XVI (`e18ba565ca540adb7edf3292f5593929e76d91c5`). The user's **finite-path update / superposed endpoint / observation** triangle is now a Pascal-spacetime fiber with exact posterior-preserving transport. The author's **Harmonic / Golden Ratio / Euler–Mascheroni** triangle and **Oily–Macaroni** remain preserved as a source-derived, separately marked rank-two/branching specialization.

Most significant NEW connection: with one retained `X~mu_1`, conditioning successive zero Bernoulli outcomes produces **exactly** `mu_(8n-7)`, SUCC's native original four-pole BBP source clock. This glues previously separate source snapshots along an actual finite path-event spine. That spine is rare (`P~225/(3008n^2)`), and its infinite zero event has probability zero; conditioning is NOT a model of actual pi digit selection.

[**RESEARCH.md**](RESEARCH.md) proves:

1. A triangular Pascal tiling and grade Fourier transfer `f+(1-f)e^{i eta}`, with **no uniform grade spectral gap** (`||M_eta||=1`).
2. Exact rare zero-spine / conditional posterior law and harmonic/Euler finite part `log(3008/225)-2gamma`; authentic-vs-Gamma-fake source hazard difference `-59/(120n^2)`.
3. A fan glued at every spine tile, with exact original four-pole finite polynomial `B_n(z)`; normalized parity mode tends to `1/9`, *not* zero. Uniform high-grade occupancy `P(J_n>=L | zero spine)<= (256/81)L^2 2^(-L)` for integers `L>=4`.
4. A time Fourier/Lerch symbol whose **sharp cusp** at frequency 0 (the rank-two Fourier regularity threshold) is `i(225/3008)t log(1/|t|)+O(|t|)`.
5. **Joint time x grade cusp:** a separable symbol `i(225/3008)(2-z)^(-2)t log(1/|t|)`, with golden PGF evaluation `z=lambda²` selecting the old triangle inside the extrusion. This is positive-field Fourier arithmetic, not a Weyl gain.
6. The remaining source-to-selected-signed-phase coupling obstruction, explicit coherent counterseed, and related negative controls.

Reproduce focused source calculations from this directory:

```
python -m unittest -v test_extruded_triangle.py
python independent_oracle.py   # optional scipy for independent quadrature
python -m compileall -q extruded_triangle.py test_extruded_triangle.py independent_oracle.py
```

The independently reviewed local receipts and proof authority boundaries are documented in [VALIDATION.md](VALIDATION.md) and [CLAIMS.md](CLAIMS.md). Root SUCC suite, CI on this exact branch, Lean and peer review are NOT claimed. `main`, historical proof status, source poles, BBP zero seed, and workflows are unchanged.
