# PSF — Selected pi phase: signed loss, sparse carry transport, and selector controls

Primary source: unchanged four-pole BBP with $U_0=0$.
Base: PR #301, `b792caae40dfe777cf7e9d3301b61f1ac0adac41`.
[Full dossier](../research/2026-10-25/PI_SELECTED_PHASE_FORGE.md).
**Pi normality and RH remain OPEN. Scholarly novelty is unverified.**

| ID | Claim and domain | Authority | Exact boundary |
|---|---|---|---|
| PSF-01 | $\mu(\pi)<15/2$ and existence of a global rational $C>0$ in $\lvert\pi-p/q\rvert\ge Cq^{-15/2}$ | CLASSICAL published theorem and elementary consequence | Zeilberger--Zudilin v2; no numerical $C$ extracted or analytic Lean claim. |
| PSF-02 | Finite inverse seed arcs under the strict integer-branch spread condition | Inherited PAPER-PROVED; independent EXACT FINITE replay | PR #297 source SHA is pinned. Arc membership is necessary, not sufficient, for extreme coherence. |
| PSF-03 | One threshold gives absolute loss $>1/1250$ on every authentic $(m,8m]$ block, uniformly for $1\le\lvert h\rvert\le m^2$ | PAPER-PROVED from original source and PSF-01 | Uses exact Green cancellation and zero anchor; threshold exists but is not numerically certified. |
| PSF-04 | All-$N$ selected Fourier bound $N-K(N,h)/1250$, hence logarithmic absolute loss for each fixed mode | PAPER-PROVED | Normalized upper bound still tends to one; no $o(N)$ saving. |
| PSF-05 | Uniform selected spectral upper bound $(H-1)(1-K(N,H)/(1250N))^2$, including prescribed $H=1+\lfloor\sqrt N\rfloor$ | PAPER-PROVED | Remains order $H$, so cannot prove spectral purity. |
| PSF-06 | Numerical evaluation of the block budget for a supplied threshold | CONDITIONAL / EXACT FINITE arithmetic | The tool explicitly leaves the numerical threshold uncertified; finite arc tests cannot validate it. |
| PSF-07 | Sharp root-energy transport $\sqrt{H/2}\Vert\mu-\nu\Vert_1$; sufficient clock budget $\sqrt H Q=o(N)$ | PAPER-PROVED / EXACT FINITE sharpness | Bounds the comparison, not either energy. Every clock residue must actually occur. |
| PSF-08 | Exact forcing and arbitrary finite local state congruences permit nearly maximal finite-window energy for all weights and partitions | PAPER-PROVED / EXACT FINITE; universal seed shortcut REFUTED | Changed rational initial seed, horizon-dependent family, possibly new denominator places. |
| PSF-09 | One fixed positive forcing retains all carries, common conductors, zero anchor and scaled sum $\pi/16$, with all Fourier means tending to one | PAPER-PROVED / EXACT FINITE; carry/tower/positivity shortcut REFUTED | Forcing and Green tail do not vanish; the original four-pole law is not retained. |
| PSF-10 | Common carries plus vanishing forcing difference imply asymptotic phase agreement, with quantitative backward remainder | CLASSICAL recurrence / PAPER-PROVED / EXACT FINITE | Does not establish the statistics of either trajectory. |
| PSF-11 | Sparse carry changes have an explicit saturated per-frequency past cost and complete future-boundary cost | PAPER-PROVED / EXACT FINITE | Bounded carry tape and the future boundary are mandatory; zero-density editing alone does not assert cancellation. |
| PSF-12 | Erasing authentic conductor-birth carries has vanishing root-spectral error at prescribed width $H\asymp(\log N)^{3/2}$ | PAPER-PROVED / EXACT FINITE rational budgets | Derived observable of original source. Its purity is OPEN; no changed forcing is labelled authentic. |
| PSF-13 | Eight finite integer/real Lean declarations and three rejected false-claim controls | LEAN KERNEL, pinned 4.14/mathlib | Scalar block bounds are hypotheses; no complex Fourier, irrationality-measure, or infinite theorem formalization. |
| PSF-14 | Original or derived flat-carry spectral purity, hence base-16 normality of pi | OPEN | Neither logarithmic absolute loss, positive carriers, nor comparison inequalities discharge it. |

The [validation record](../research/2026-10-25/PI_SELECTED_PHASE_VALIDATION.md)
records actual executions. The sparse finite-irrationality-type control in
the Diophantine dossier refutes promotion of even exponent two to normality.
The exact-forcing changed seed and the positive changed forcing preserve
different features; they must not be merged into one fictional countermodel.
