# The zero-seed differential seam: signed source response, infinite parity currents, and analytic observer conditioning

**Research-only, 20 November 2026.** Proposed SUCC draft stacked on #682 (`8372048dff415c47da120afdff5df7696820dfe7`) above the causal-origami / constructive-Fourier / Collatz-parity sequence. This note does **not** replace the authentic four-pole forcing, the literal original seed `U_0=0`, or any original archive. Classical moment/positive-measure, distribution/Fourier, and rank theory are antecedents; no worldwide mathematical priority is claimed. **R0, π base-16 normality, all-positive-integer Collatz, RH, nonclassical physical energy: OPEN.**

## Source and observer types

Use `e(v)=exp(2πiv)`. The **target** source is

\[
r_0(j)=\frac4{8j-7}-\frac2{8j-4}-\frac1{8j-3}-\frac1{8j-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r_0(n),\quad
x=\sum_{j\ge1}16^{-j}r_0(j)=\pi/16.
\]

Here the final identity uses the **classical BBP theorem**. Set `Q(t)=4-2t³-t⁴-t⁵=(1-t)H(t)` with `H(t)=4+4t+4t²+2t³+t⁴>0` increasing on `[0,1]`. The **declared matched-jet family**, used only for source discrimination, is

\[
Q_\tau(t)=Q(t)+\tau(1-t)^2=(1-t)[H(t)+\tau(1-t)],\quad 0\le\tau\le1.
\]

Write `r_τ(j)=∫_0^1 t^(8j-8)Q_τ(t)dt`, `δr(j)=∂_τr_τ(j)=2/[(8j-7)(8j-6)(8j-5)]>0` and `c_j^τ=16^{-j}r_τ(j)`. **No statement about the real π phase is applied to τ≠0.** The selected original seed is zero; separate seed `s` is an explicit counterfactual source-identification coordinate.

At clock `n`, the **analytic future journal** is

\[
G_{n,\tau}(z)=\sum_{k\ge0}c^\tau_{n+k+1}z^k,\qquad
G_{n+1,\tau}(z)=\frac{G_{n,\tau}(z)-G_{n,\tau}(0)}z.
\]

Let `m=n+1`; define `q=1/16`, normalized probabilities and characteristic functions

\[
w_{n,k}(\tau)=\frac{q^k r_\tau(m+k)}{\sum_{j\ge0}q^j r_\tau(m+j)},\quad
\Phi_{n,\tau}(\omega)=\frac{G_{n,\tau}(e^{i\omega})}{G_{n,\tau}(1)}
=\sum_{k\ge0}w_{n,k}(\tau)e^{i\omega k},\quad
\mu_n(\tau)=\frac1i\Phi'_{n,\tau}(0)=\sum k w_{n,k}(\tau).
\]

These are *probabilities on source-time lags*, not probabilities of π digits or independent prime encounters.

## ZSD-01 — Strictly signed source-response differential at every clock (PROVED PAPER)

For every integer `n≥0` and `τ∈[0,1]`, including one-sided derivatives at endpoints,

\[
\boxed{\partial_\tau G_{n,\tau}(1)>0,\qquad
\partial_\tau\mu_n(\tau)<0.}
\]

**Proof of the nontrivial sign.** Put `g_m(τ)=δr(m)/r_τ(m)`. The positive measure on `(0,1)` with density proportional to `t^{8m-8}(1-t)[H(t)+τ(1-t)]` represents `g_m(τ)` as the expectation of

\[
\psi_\tau(t)=\frac{1-t}{H(t)+\tau(1-t)}.
\]

Its derivative is `ψ'_τ(t)=-[H(t)+(1-t)H'(t)]/[H(t)+τ(1-t)]²<0`. Raising `m` by one tilts the distribution by strictly increasing `t^8`, so `g_{m+1}(τ)<g_m(τ)` by the elementary covariance inequality. Differentiating the normalized positive weights gives

\[
\boxed{\partial_\tau\mu_n
=\operatorname{Cov}_{w_{n,\tau}}(k,\,g_{m+k}(\tau))<0.}
\]

A strictly increasing `k` and strictly decreasing `g_{m+k}` have strictly negative covariance because every weight is positive. Meanwhile the unnormalized derivative is the sum of positive terms `Σ16^{-j}δr(j)`.

**Source-identity/precision verdict.** For every `n`, the scalar lag head `μ_n(τ)` is strictly injective on `[0,1]`. Together with an independent unwrapped root/seed head `U_0=s`, `(s,τ)↦(s,μ_n(τ))` has oriented Jacobian determinant `∂_τμ_n<0` and identifies this *declared two-parameter family*. The lag head alone is **seed-blind**. Obtaining `G_{n,τ}` exactly is an ideal analytic-observer premise; finite approximations require explicit tail bounds (ZSD-04).

## ZSD-02 — A fading source retains an order-one analytic Fourier lag (PROVED PAPER)

For all `n≥0,τ∈[0,1]`, the Mellin-positive sequences `r_τ(j)` are strictly decreasing and strictly log-convex. Consequently

\[
\boxed{0<\mu_n(\tau)<\mu_{n+1}(\tau)<1/15,\qquad
\lim_{n\to\infty}\mu_n(\tau)=1/15.}
\]

Let `g_k=(15/16)16^{-k}` be a geometric probability. Since `H_τ(t)=H(t)+τ(1-t)` is positive and increasing on `[0,1]`, for `m=n+1` the Mellin distribution gives

\[
0\le1-\frac{r_\tau(m+k)}{r_\tau(m)}
\le8k\,\mathbb E_{m,\tau}[1-t]
\le \frac{16k}{8n+3}.
\]

The last inequality uses negative covariance of increasing `H_τ` and decreasing `1-t` against the Beta density proportional to `t^{8m-8}(1-t)`, whose mean of `1-t` is `2/(8m-5)`. The geometric mean `Σk g_k=1/15` then gives

\[
\boxed{\|w_{n,\cdot}(\tau)-g\|_{\mathrm{TV}}
\le\frac{16}{120n+29},\qquad
\sup_{\omega\in\mathbb R}\left|\Phi_{n,\tau}(\omega)-\frac{15}{16-e^{i\omega}}\right|
\le\frac{32}{120n+29}.}
\]

*Proof of normalization bound:* put `u_k=r_τ(m+k)/r_τ(m)≤1`, `δ=Σ g_k(1-u_k)≤16/[15(8n+3)]<1`, and `w_k=g_ku_k/(1-δ)`. Then `TV(w,g)≤δ/(1-δ)`. Strict log-convexity follows from Cauchy–Schwarz on the positive Mellin measure; it implies `r(m+k+1)/r(m+k)` increases strictly with k, so the normalized late-journal family increases in monotone-likelihood-ratio order. The strict lag inequalities follow. Absolute `G_n(1)~16^{-n}/(64n²)→0` for the authentic source, although its **normalized spectral derivative** approaches `i/15`. Moreover the **unmodified actual-source forward differential**, not a comparison between sources, is strictly positive for every n and obeys `μ_(n+1)(0)−μ_n(0)=32/[225(n+1)²]+O(n^(−3))` by ZSD-03.

**Source phase firewall:** uniform convergence of this *source-lag* Fourier profile is not convergence of the selected π orbit's Weyl spectrum. The unchanged forcing with seed `s=-π/16` has exactly the same profile while its completed real phase locks at zero.

## ZSD-03 — Sharp second-order matched-jet separation and precision cost (PROVED PAPER)

With `m=n+1`, uniformly for `τ` in `[0,1]`,

\[
\begin{aligned}
r_\tau(m)&=\frac{15}{64m²}+\frac{151+2\tau}{512m³}+O(m^{-4}),\\
\mu_n(\tau)&=\frac1{15}-\frac{32}{225m}
+\frac1{m²}\left(\frac{182}{1125}-\frac{4\tau}{3375}\right)+O(m^{-3}),\\
\partial_\tau\mu_n(\tau)&=-\frac4{3375m²}+O(m^{-3}).
\end{aligned}
\]

Therefore the exact authentic and matched-jet mutant lag heads satisfy

\[
\boxed{\mu_n(1)-\mu_n(0)=-\frac4{3375(n+1)²}+O(n^{-3})<0.}
\]

**Derivation.** For fixed k, `r_τ(m+k)/r_τ(m)=1-2k/m+[3k²-β_τ k]/m²+O((1+k³)m^{-3})`, with `β_τ=(151+2τ)/120`. The geometric moments of order 1,2,3 are `1/15,17/225,107/1125`, respectively. Expanding the quotient `E_g[k u_k]/E_g[u_k]` gives the displayed coefficients; `dβ_τ/dτ=1/60` and geometric variance `16/225`, hence the signed `−4/3375` sensitivity. The expansion is rigorously summed by splitting `k≤m/2` (uniform Taylor bound with polynomial k) and `k>m/2` (exponentially small geometric tail). **No finite same-data fit is used as a proof.** The `Θ((n+1)^2)` inverse sensitivity is a precise *relative conditioning cost in fixed lag units*, not an information-theoretic Shannon cost or a quantum energy estimate.

## ZSD-04 — A finite subjective observer can certify the analytic differential (PROVED EXACT)

For every integer `m≥1`, source deformation `τ∈[0,1]`, and terminal depth `K≥1`, let

\[
S_j^{[K]}=\sum_{k=0}^{K-1}\frac{k^j}{16^k}r_\tau(m+k),\quad j=0,1.
\]

Monotonicity gives explicit rational omitted tails `E_0≤16^{-K}r_τ(m+K)/(1-1/16)` and

\[
E_1\le16^{-K}r_\tau(m+K)\left(\frac{K}{1-1/16}+\frac{1/16}{(1-1/16)^2}\right).
\]

Thus the exact analytic mean satisfies the **outward rational enclosure**

\[
\boxed{\frac{S_1^{[K]}}{S_0^{[K]}+E_0}
\le\mu_n(\tau)\le
\frac{S_1^{[K]}+E_1}{S_0^{[K]}}.}
\]

The executable probe uses these inequalities, never identifying a finite moment sum with the complete analytic answer. For `m∈{1,20,100,1000}` and `K=43`, its rational intervals **strictly separate** `τ=0` and `τ=1`. This is a finite source-authenticated source-identity witness even at very late clocks, not a phase-orbit saving.

## ZSD-05 — Completed phase derivatives collapse the source; the chronological journal does not (PROVED / inherited SA-02)

In the declared five-real-parameter family `ϑ=(s,c_1,c_2,c_3,c_4)`, with poles `a=(7,4,3,2)`, define

\[
r_\vartheta(j)=\sum_{i=1}^4\frac{c_i}{8j-a_i},\quad
x(\vartheta)=s+\sum_{j\ge1}16^{-j}r_\vartheta(j),\quad
Y_n(\vartheta)=16^nx(\vartheta).
\]

Write `β=(1,β_1,...,β_4)`, `β_i=Σ_{j≥1}16^{-j}/(8j-a_i)`. Every completed phase head has Jacobian row

\[
D_\vartheta e(hY_n)=2π i h16^n e(hY_n)\,β.
\]

**All** such rows, even with every clock and every integer harmonic, span at most the **same one-dimensional real parameter cotangent line**. The completed phase cannot separate the four-dimensional source/seed fiber `ker β`; this is true at the original zero seed. Yet unwrapped chronological state readings `U_t` at any five distinct increasing clocks have full rank by the Cauchy determinant theorem SA-02 of [#671](https://github.com/femboy2112/SUCC/pull/671). The missing source directions reside in the exact compensating-tail differential `D(U_n-Y_n)=-D T_n`. This is a rank collapse caused by the **observation quotient**, not by cessation of causal evolution. A source-order Jacobian or prime response must retain extra readouts/anchors; taking more derivatives of the same terminal scalar alone cannot repair the rank defect.

## ZSD-06 — Every finite Collatz bit is locally flat; the all-time seam derivative is singular (PROVED EXACT)

Let `q(y)=1_{\{y\}\in(1/4,3/4)}`, with endpoint status declared separately. Under the authenticated BBP zero-seeded phase `x=π/16`, put

\[
q_n(s)=q(16^n(x+s)),\quad
q_n(0)=\epsilon_{4n+2}\oplus\epsilon_{4n+3}
\]

where the Collatz parity relation uses the **classical Bernstein–Lagarias** four-bit 2-adic representation and the chosen real expansion. Since `x` is irrational, each fixed `q_n(s)` is constant on some neighborhood of the original `s=0`: its ordinary derivative at the authentic seed is **zero**. For any finite `N`, a common positive neighborhood exists for all `0≤n≤N`. However no fixed neighborhood protects all future depths: the preimage threshold meshes have spacing `1/(2·16^n)` in s, so arbitrarily small nearby changes of seed alter a sufficiently late bit. The complete journal is continuous in the *product topology* at nonthreshold points, but not in the uniform sup metric of infinite bit sequences.

The correct **distributional differential** is the signed current

\[
\boxed{D_s q_n(s)=\sum_{j\in\mathbb Z}\left[
\delta_{s=(j+1/4)/16^n-x}
-\delta_{s=(j+3/4)/16^n-x}\right].}
\]

On one full unit interval of seed space, its total variation is exactly `2·16^n`. **So finite bits have zero ordinary local derivative, while their singular seam currents have exponentially growing total variation as causal depth increases.** This is an exact observer-resolution distinction, not a phase-probability theorem. The first and last terms depend on the orientation/endpoint convention, which is immaterial for the authentic irrational seed but mandatory in finite controls.

## ZSD-07 — Constructive Fourier atoms of the signed seam current; Gaussian observer blinding (PROVED EXACT)

With the Fourier convention `\widehat f(h)=∫_0^1 f(s)e(-hs)ds`, before translating the seed coordinate by x, the source-independent quarter head has

\[
\widehat{Dq_n}(h)=
\begin{cases}
2i\,16^n(-1)^{(\ell+1)/2},&h=16^n\ell,\quad \ell\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\]

Translating by x multiplies each coefficient by `e(hx)` without changing its magnitude. With the normalized periodized Gaussian heat kernel `\widehat K_λ(h)=\exp(-λh²/2)` of #672,

\[
\boxed{\|K_λ*Dq_n\|_2^2
=4\cdot16^{2n}\sum_{\ell\text{ odd}} e^{-λ16^{2n}\ell^2},}
\]

and as `n→∞`, this norm is asymptotic to `2√2·16^n\exp[-λ16^{2n}/2]→0` for fixed λ>0. Thus the exact same family has **unbounded sharp seam-current variation and vanishing fixed-width Gaussian readout**. This is an explicit, source-typed caution against mistaking Gaussian smoothing for a dynamical loss or creation of information, or for π equidistribution.

## ZSD-08 — Signed prime-square differential current has all three outcomes (SOURCE-SPECIFIC FINITE; PROVED CERTIFICATES)

Let `p≥7` be prime, `j=(p²−1)/8`, and let the *separate counterfactual* interchange the original consecutive inputs `r_0(j),r_0(j+1)` while retaining the **same** zero seed. The original-minus-swapped completed source value is `D_j/16^(j+1)`, where `D_j=15(r_0(j)−r_0(j+1))>0`. At the first `d≥0` for which `Δ=16^dD_j≥1/64`, the inherited bound `Δ<1/4` holds, and the observation clock is `N=j+1+d`.

The exact signed quarter-sector response is the **oriented threshold-crossing number**

\[
\boxed{q(16^Nx)-q(16^Nx-Δ)
=\int_{16^Nx-Δ}^{16^Nx}(\delta_{k+1/4}-\delta_{k+3/4})\,du,}
\]

with the sum over all integer k and no endpoint coincidences. Rational original-source terminal intervals independently certify:

| Prime | Observation N | Signed quarter response |
|---:|---:|---:|
| 7 | 7 | 0 |
| 79 | 787 | +1 |
| 131 | 2153 | −1 |

These are **three distinct outcomes for a strictly positive source-order phase shift**. They require actual source/carry/absolute-phase orientation to interpret the parity head. They conclusively refute `positive cross-source phase differential ⇒ positive signed Collatz-parity response`, even on the authentic zero-seeded original arm. The source-order perturbation is not the unperturbed π orbit.

## ZSD-09 — Explicit remaining R0 proof obligation (UNVERIFIED)

The signed results are real and source-derived but concern **variation of the source** (`∂_τ`) or **variation of the pinned root** (`D_s`) or **comparisons between original and swapped source**. The target remains the *unmodified* zero-seeded orbit

\[
\mathcal A_B=\frac1B\sum_{n=B}^{2B-1}
[1-\cos(2π16^n\pi/16)]>\eta\quad\text{for all sufficiently large }B.
\]

The source-only normalized-lag differential is identical under the explicit wrong seed `s=-π/16`, whose completed phase is locked. The all-depth singular seam current is universal to every hexadecimal source, including constant/periodic points. Therefore no unconditional π anti-lock theorem follows from either alone.

**Next genuinely source-selected instrument:** construct a predeclared, bounded, signed **cross-current** between (i) the source root `s=0` and its unwrapped carries, (ii) the strictly oriented original source lag/covariance and primary 4/p² marks, and (iii) the *actual* real-phase quarter-seam / Gaussian observer, with correct common phase and a quantitative lower bound on every late shell. Demand positive/negative/null/mutation controls, fresh held-out clocks, no fitted q_n, and a proof that the source-law constraints prohibit asymptotic phase concentration at zero. Infinite dimensionality, derivative nonvanishing, or a valid Yoneda embedding alone is insufficient.

### Ledger verdict

- **Disclosed / PROVED within boundaries:** ZSD-01–07; ZSD-08's exact oriented finite receipts; original four-pole and literal zero contract retained. The first/second source-lag asymptotics and sharp signed matched-jet derivative are a new-to-SUCC mathematical assembly, without academic priority claim.
- **Refuted with receipts:** terminal completed-phase derivatives recover the five-dimensional source; pointwise parity derivatives at the original seed are nonzero; positive original-vs-swapped phase current implies positive signed quarter response; fixed Gaussian width preserves fine current strength.
- **OPEN:** all-large-shell π R0, base-16 normality, positive-integer Collatz, RH, physical quantum/energy interpretations.
