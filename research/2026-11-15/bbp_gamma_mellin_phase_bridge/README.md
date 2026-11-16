# OPERATION GAMMA INTERFEROMETRY — BBP complex-depth and causal scale transport

**2026-11-15 · RESEARCH-ONLY, additive stacked candidate on SUCC #651.**

## User hypothesis, kept separate from established mathematics

The proposal is that Gamma is an analytically accessible *computational-form window*: a continuous source volume, observed with scale-dependent complex Fourier characters, can retain signed phase geometry after integration even when naive expectation/Fourier reordering destroys the real-circle signal. The source's discrete successor and its analytic depth extension should have an exact transport law, and correlations at nested scales should produce identifiable defects.

This folder supplies the strongest immediately defensible theorem and hostile controls, **without claiming that Gamma already proves pi normality**.

## Actual source passport

Preserve exact original four-pole forcing, zero seed and imported classical BBP identification:

- `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U0=0`, `U_(n+1)=16 U_n+r(n+1)`.
- `Q(t)=4-2t^3-t^4-t^5`, `g(t)=Q(t)/(16-t^8)=(1-t)/((2-t^2)(t^2-2t+2))`.
- `x=pi/16=int_0^1 g(t)dt` (**classical imported identity**), `T_n=int_0^1 t^(8n)g(t)dt`, `16^n x=U_n+T_n`.
- Define `v=-8 log t`, `K(v)=exp(-v/8)g(exp(-v/8))/8`. Then `T_n=int_0^infinity exp(-n v)K(v)dv`.

## Results

1. **Exact computational-depth successor square:** `H(z,beta+1)=H(z,beta)-H(z+1,beta)`, with `H(z,beta)=int exp(-zv)(1-exp(-v))^beta K(v)dv`. It respects complex clock transport; it coexists with `r(n+1)=16 T_n-T_(n+1)`.
2. **Complex two-axis Gamma window with source corrections:** after normalized scaling `64 n^(beta+2) H(n(1+i xi),beta)`, the first three terms are Gamma moments whose coefficients `7` and `55` come from all four BBP poles. The additive error is uniform in real xi for beta on compact subsets of `Re beta>-2`.
3. **Source-normalized all-frequency phase transport:** the original positive Green density conditioned at n induces `Y=-8 n log X`. In total variation `Law(Y)` is within `1-64 n^2 T_n <= 7/(8n)` of Gamma(2,1); hence **every** complex joint phase `exp(-i xi Y)Y^(i omega)` has an error at most `7/(4n)` uniformly over real xi,omega. The two frequency types are not silently identified.
4. **Four-time causal-lag crossover:** `D_(n;q,ell)` constructed from original Green moments has a fourth-order law for `q=o(n)` and a third-order law when `q/n` is nonzero. At actual circle critical lags `q~n^2`, `n^3 D_(n;q,2)->1/16`. A complex Gamma(3+i omega) phase window emerges in this regime.
5. **Reconstructability and its price:** the full complex vertical Mellin/Fourier response recovers the original positive Green density; the limiting Gamma log-Fourier response is zero-free yet exponentially damped in high log-frequency, making inverse recovery ill-conditioned.
6. **New proved high-frequency source cancellation:** For fixed k,ell, the positive original Green difference `D_(k,ell)(n)=(-1)^k Delta_ell^k T_n` has Gamma factorial leading coefficient, and the signed mean of `exp(2pi i h_B D_(k,ell)(n))` over n in [B,2B) is `O(1/c_B+c_B/B)` whenever `c_B=h_B/B^(k+2)->infinity` and `c_B=o(B)`. This is real signed cancellation on the SOURCE TAIL, not on the complete pi circle.
7. **No-go controls:** source-only Gamma moments cannot distinguish zero seed from coherent wrong seed `s=-x`, whose completed real circle is identically zero. Gaussian/Gamma attenuation, Gram positivity and fixed-source low-frequency phase corrections do NOT give Weyl cancellation automatically.

**Source and theorem genealogy:** Maintained Main XXV, `observational_succ/duck_bbp.py`, #634 Gamma Genesis (positive source Gamma/TV, Oily bridge), #638 Gamma suspension, #646 source zero/circle, #648 source chiral clock, #649 randomized norm, #651 source-preserving pi-slot/Poisson lifting. Classical Gamma facts cross-checked against NIST DLMF §5.2, §5.11.

The finite-source test calibration/recovery record is in [REPAIR_HISTORY.md](REPAIR_HISTORY.md).

## Validation

- `python -m unittest -v test_gamma_phase.py`
- `python independent_audit.py`
- `python -m compileall -q gamma_phase.py gamma_signed_shell.py test_gamma_phase.py independent_audit.py`

Finite tests are not a proof of the infinite asymptotic assertions. The latter have paper derivations in [THEOREMS.md](THEOREMS.md). Original source, provenance manifest, historical files, production defaults and main are untouched. No merge, tag, release, Lean proof, full repository gate or external referee is claimed.
