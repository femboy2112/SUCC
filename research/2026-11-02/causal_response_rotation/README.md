# Causal response rotation: a coherent circle can be weakly Haar along a causal axis

**Research-only** — exact parent SUCC #463 at 43adc90badfc6b8abc1631a4332c09cda007ccb7 (stacked on #462→#460→#459, rooted in merged Main XIX). No original BBP source, zero seed, production, archives or main changes. No π-normality or RH claim.

The user's proposed rotation has a faithful operational meaning: rotate **the observer's independent variable** from chronological time to the counterfactual initial-seed perturbation s, measuring how the same fixed source changes with that initial condition. This is a source/seed-labelled Fourier representation in the *causal input* direction, not the ordinary DFT of the time series.

## The correct line/circle/solenoid diagram and structural differential

The honest maps are real-line causal lifts into the **inverse-limit solenoid**, then projection to a single circle:
\[
\mathbb R\xrightarrow{\ \iota\ }\Sigma_{16}\xrightarrow{\ \pi_0\ }\mathbb R/\mathbb Z.
\]
There is no canonical inverse from a single circle point into its whole branch-history solenoid. Multiplication by 16 is invertible on the real line and on \(\Sigma_{16}\), but **16-to-1 on the circle**. This is prior SUCC #452 topology applied to the new causal observer; no topological novelty claim.

The causal intervention differential and dilation satisfy
\[
\mathcal D_h\mathcal C_{16}=16\mathcal C_{16}\mathcal D_h.
\]
This is an exact source-independent q-commutation law, and the source enters through the separately retained phase/time cocycle. See CR-01B in PROOFS.md.

## Three exact theorems

Let b=16, h≠0, original U0=0 and the unchanged four-pole forcing. Then
\[
Z_{n,h}(s)=e^{2\pi ih(U_n+16^n s)},\quad
\Phi_{N,h}(s)=\sum_{n=0}^N Z_{n,h}(s),\quad
d\mu_{N,h}(s)=\frac{|\Phi_{N,h}(s)|^2}{N+1}ds.
\]

**1. Universal causal weak Haar, even for a coherent nonnormal orbit.** For EVERY choice of unit phases, and every integer causal Fourier mode k≠0,
\[
|\widehat\mu_{N,h}(k)|\le\frac1{N+1}\longrightarrow0.
\]
Hence \(\mu_{N,h}\Rightarrow ds\) weakly. This is *not* selected temporal normality: the coherent same-four-pole counterseed and the positive zero-seeded changed-source shadow share it. Indeed
\[
\int_0^1\left(\frac{|\Phi|^2}{N+1}-1\right)^2ds
=\frac N{N+1}\to1,
\]
so weak-Haar flatness is not L2 convergence to a constant density.

**2. Moving-mode phase retrieval from nonnegative causal INTENSITY.** The integer frequencies \(16^n-16^m\) are unique for n>m. With U0=0,
\[
\boxed{(N+1)\widehat\mu_{N,h}(h(16^n-1))=e^{2\pi ihU_n},\quad1\le n\le N.}
\]
The entire selected phase record survives at causal Fourier frequencies that grow like \(16^n\), even though every fixed mode vanishes in the weak limit. The zero-seed *anchor* is essential.

**3. The causal differential operator exactly selects each time.**
\[
\mathcal D_h=(2\pi ih)^{-1}\partial_s,\quad
\mathcal D_h Z_{n,h}=16^nZ_{n,h}.
\]
For each n≤N use the rational Lagrange polynomial
\[
L_{n,N}(X)=\prod_{m\ne n}\frac{X-16^m}{16^n-16^m}.
\]
Then
\[
\boxed{[L_{n,N}(\mathcal D_h)\Phi_{N,h}](0)=e^{2\pi ihU_n}.}
\]
This makes the higher unit–unit SUCC differential an **actual causal-generator spectral projector**. It is exact finite phase reconstruction, not a new signed bound or computational speedup.

## Circle↔line is the actual universal covering

The lifted line phase is \(\Theta_{n,h}(s)=h(U_n+16^n s)\). The circle map \(e(\Theta_{n,h})\) has winding \(h16^n\), with \(\Theta(s+1)-\Theta(s)=h16^n\). A circle is a quotient of the real line here; this is not a homeomorphism or proof of intrinsic Riemannian curvature. The original integer lift and carry must be retained.

## First source-sensitive 34th moment: credited, not rediscovered

SUCC #404 previously proved the first balanced radix-16 phase resonance occurs at 17 vs 17 factors (34th moment). A representative exact identity is
\[
16\cdot16^n+16^{n+2}=17\cdot16^{n+1},
\quad
16U_n+U_{n+2}-17U_{n+1}=r_{n+2}-r_{n+1}.
\]
The source appears, but the seed cancels. Every Haar seed-integrated moment is translation invariant, so none can by itself distinguish the selected zero seed from the coherent same-source counterseed.

## The actual remaining gate

If \(\delta_N=16^{-(N+1)}\) and \(\rho_N=|\Phi|^2/(N+1)\), then
\[
S_N(h)=o(N)
\quad\Longleftrightarrow\quad
\frac1{\delta_N}\int_0^{\delta_N}\rho_N(s)ds=o(N),
\]
for each fixed h≠0 on the original zero-seeded orbit. This is the already-known shrinking-seed selection problem expressed using a nonnegative causal intensity; **it does not prove the bound**. The global causal Haar theorem sees fixed windows and discards the exponentially shrinking zero-seed aperture.

## Reproduce and audit

- [PROOFS.md](PROOFS.md) — exact typed maps, no-go controls, causal intensity phase retrieval and differential projectors
- [CLAIMS.md](CLAIMS.md) — factored claim ledger
- [SOURCE_MAP.md](SOURCE_MAP.md) — attribution to #404/#461/#463 and original source
- [VALIDATION.md](VALIDATION.md) — executed exact and independent numerical tests, CI scope
- [NEXT.md](NEXT.md) — next genuinely source-selecting signed probe
- [causal_rotation_probe.py](causal_rotation_probe.py) — exact Fraction tests; [causal_direct_oracle.py](causal_direct_oracle.py) — direct numerical seed quadrature, float-only

**Status:** new SUCC causal-axis observer and fidelity theorem with strict limitations; no signed real cancellation, no π normality or RH.
