# Anchored oscillatory paths versus seed-blind temporal holonomy

**2026-11-07 · DRAFT · source-specific negative theorem and quantitative finite-observer alias.** Depends on the exact original four-pole/source gauge in main, and on the two-channel arc metric in TWO_TONE_STABLE_ARC.md. Uses earlier SUCC #518 finite periodic-completion controls; extends them with an explicit driven-observer error budget. No π-normality proof.

## APH-01: every finite source-corrected temporal oscillator loop is seed-blind — PROVED LOCAL

For any real initial seed s and the **unchanged original four-pole** forcing, let \(U_0(s)=s\), \(U_{n+1}(s)=16U_n(s)+r(n+1)\). For integers n≥0, d≥1 define

\[
S_d(n)=\sum_{j=1}^d16^{d-j}r(n+j).
\]

Induction gives the **exact unwrapped equality**
\[
U_{n+d}(s)=16^d U_n(s)+S_d(n)\quad\text{for EVERY seed }s.
\]

For a phase-locked harmonic readout \(z_n^{(s)}(h)=e^{2\pi i h U_n(s)}\), therefore

\[
\boxed{
z_{n+d}^{(s)}(h)\;\overline{z_n^{(s)}(16^dh)}
=e^{2\pi i h S_d(n)},\qquad \forall n,d,h,s.
}
\]

A 'corrected temporal holonomy' divides the left side by the explicit right side; it is **1 for every seed**, not merely zero. Consequently **every statistic that depends only on a finite collection of such corrected closed-path readouts and the same source forcing is seed-uniform**. If one claimed it forced Haar on the authentic s=0 history, it would also force Haar on the coherent same-forcing wrong seed \(s_*=-\pi/16\); but the latter has \(\{U_n(s_*)\}=\{-T_n\}\to0\), so it is not Haar. This decisively refutes the source-corrected temporal-holonomy-only π proof strategy.

The corrected loop can still authenticate the **four-pole recurrence** against source mutations. It cannot authenticate **which seed** generated a source-compatible orbit. To retain the zero selector, keep open paths anchored by the independently declared initial boundary s=0 and pursue nonlocal signed sums of their unclosed phases, not merely transport-flatness identities. An anchored path is mathematically reconstructible from the forcing; it is **not** automatically equidistributed.

**Receipt:** all-depth exact Fraction test for d=1..8, n+d<55 and seed controls 0, 1/3, -1/11; 1,092 exact congruences, all zero. An earlier local one-step mutation breaks the plaquette at its boundary. The proof, not the sample, supplies universal n,d quantifiers.

## APH-02: arbitrarily accurate finite-horizon two-tone impersonation by periodic sources — PROVED LOCAL

Write \(\alpha=\pi/16\). For any positive integer p choose the closest rational \(\beta_p=k_p/(16^p-1)\) to α; then
\[
|\beta_p-\alpha|\le\frac1{2(16^p-1)},
\quad 16^p\beta_p\equiv\beta_p\pmod1.
\]

Set the same-forcing hostile seed \(s_p=\beta_p-\alpha\). Authentic original-zero and altered-seed forced phase paths differ at time n by exactly \(16^ns_p\) mod 1, **because the identical future-tail/source terms cancel**. For a prescribed finite horizon n=0,…,N, put
\[
\delta_{N,p}=\frac{16^N}{2(16^p-1)}.
\]
Their circle displacement at every recorded time is at most \(\delta_{N,p}\), which tends to zero as p→∞ at fixed N.

In the two-tone \(D_{a,2}\) metric, source points satisfy for any circular distance 0≤d≤1/2,
\[
\boxed{
D_{a,2}(\delta_x,\delta_y)
\le \frac{2\sqrt d}{a}+\frac{2\pi d}{\sqrt a}.
}
\]

**Proof:** each underlying normalized arc has symmetric-difference length at most 2d; thus the unmodulated channel has L² difference ≤√(2d)/a. The modulated channel differs by the same shifted-support term plus a known phase rotation of modulus ≤2πd, which contributes at most \(2\pi d/\sqrt a\) in L². Combine two channels by the triangle inequality. Applying this to every paired time and then using convexity/Minkowski for empirical laws gives

\[
\boxed{
D_{a,2}\bigl(\mu^{U(s_p)}_{[0,N]},\mu^{U(0)}_{[0,N]}\bigr)
\le \frac{2\sqrt{\delta_{N,p}}}{a}
+\frac{2\pi\delta_{N,p}}{\sqrt a}
\longrightarrow0\qquad(p\to\infty)
}
\]
when \(\delta_{N,p}≤1/2\). The same applies to any bounded linear functional of the two recorded profiles. The completed βp orbit is periodic of period at most p. Since the future-tail correction tends to zero, the empirical law of the altered seed tends to a **finite atomic**, non-Haar periodic-orbit measure as the observation horizon goes to infinity. It is therefore a valid same-forcing nonnormal countermodel.

**Interpretation:** for every fixed finite horizon and any positive observation tolerance, there are nonnormal same-forcing periodic completions whose entire observed driven pin-bed histories are that close to the real s=0 history. This is a genuine *finite-resolution identification obstruction*. It does **not** defeat a separately authenticated **exact** initial seed s=0: those hostile seeds have s_p≠0. It also does not imply that π-normality is unprovable from the exact original formula.

**Receipt:** exact rational prototype independent of π, with α=123456789/1000000000, N=9 and p=N+18, verifies nearest-grid denominator, period and every finite-time distance inequality using Fraction; the universal proof uses nearest-integer arithmetic and the analytic two-channel translation modulus. The rational prototype is **not** an experimental demonstration about π digits.

## APH-03: implication for a carrier-relative Yoneda observer

The correct independent verdict dimensions remain:

- **Source/action compatibility:** legal four-pole forcing, transport/naturality squares and all phase plaquettes.
- **Surface realization:** cross-channel syzygies and probability positive-definiteness from REALIZATION_AND_DYNAMIC_YONEDA.md.
- **Observation-relative equivalence:** exact or approximate profiles with precisely declared probe family, horizon and error budget.
- **Target descent:** whether the claimed target is constant over every admitted observational fiber (PR #541 and main carrier-relative targets).
- **Source selector:** literal U0=0 and its provenance; not deduced from flat temporal holonomy.
- **Signed asymptotic gate:** zero-seed all-epoch Fourier/energy decay; presently OPEN.

If a proposed proof uses only the first three but concludes the sixth, the coherent wrong seed is an explicit counterexample. If the claim is **only** that a model is observationally indistinguishable under those carrier probes, that can be a fully legitimate, rigorously qualified truth output. The pin-bed should disclose what it cannot distinguish rather than pretending that its loss of information did not occur.

**Next discriminating research target:** use the actual zero-seed odd-denominator/carry/prime-birth genealogy to prove an *all-epoch signed* source-specific bound. Test the bounded but noncontracting driven surface action against PR #527's 2-adic Haar/nonreal-Haar shadow and PR #518's periodic completions. No amount of phase-locked local flatness, characteristic kernel positivity or exact reconstruction is by itself a substitute for the open estimate.
