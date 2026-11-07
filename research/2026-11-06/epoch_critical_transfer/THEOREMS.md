# Critical Fejér transport on BBP *epochs*: vanishing Hilbert error and an all-radius gate

**Date:** 2026-11-06. **Scope:** authenticated original four-pole BBP recurrence and literal `U_0=0`, child of PR #536 (critical collision). `PROVED LOCAL` = derivation here, *not* external scholarly priority, Lean kernel verification, or a proof of π normality. The origin of the source tail estimates and Fejér energy is inherited from PRs #525 and #536. PRs #532 (larger denominator sieve) and #535 (time-Fejér return fibers) are read-only sibling context.

## Source and definitions

Use exactly

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Set \(x_n=\{U_n\}\), \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\) and \(z_n=\{U_n+T_n\}=\{16^n\pi/16\}\). The original source proves \(0<T_n<1/[15(n+1)^2]\) for integer \(n\ge1\). In the epoch \(I_A=[A,2A)\), define

\[
W^{y}_{A}(h)=A^{-1}\sum_{n=A}^{2A-1}e(hy_n),\qquad
\mathcal C^y_{A,H}=\sum_{|h|\le H}(1-|h|/(H+1))|W^y_A(h)|^2,\quad e(t)=\exp(2\pi i t).
\]

The weighted norm \(\sqrt{\mathcal C}\) is an actual Hilbert ℓ² norm, so a reverse triangle bound is valid. For every sequence of circle phases, \(\mathcal C_{A,H}\ge1\) and is exactly the positive Fejér pair energy.

## ET1 — source-specific epoch Hilbert transport: PROVED LOCAL

**Theorem.** For **every** integer \(A,H\ge1\), the original zero-seeded BBP history satisfies

\[
\boxed{\left|\sqrt{\mathcal C^z_{A,H}}-\sqrt{\mathcal C^x_{A,H}}\right|
\le \frac{\pi}{15A^2}\sqrt{\frac{H(H+1)(H+2)}6}.}\tag{ET1}
\]

**Proof.** The pointwise character bound is \(|e(hz_n)-e(hx_n)|\le2\pi|h|T_n\). The original source tail gives

\[
\frac1A\sum_{n=A}^{2A-1}T_n
<\frac1{15A}\sum_{n=A}^{2A-1}(n+1)^{-2}
\le\frac1{15A}\int_A^{2A}t^{-2}dt=\frac1{30A^2}.
\]

Hence \(|W^z_A(h)-W^x_A(h)|\le\pi|h|/(15A^2)\). The exact Fejér-weighted square frequency identity is

\[
\sum_{|h|\le H}\left(1-\frac{|h|}{H+1}\right)h^2
=2\sum_{h=1}^{H}\left(1-\frac{h}{H+1}\right)h^2
=\boxed{\frac{H(H+1)(H+2)}6}.
\]

The reverse triangle inequality in this weighted Hilbert space proves ET1. In particular, at **full critical resolution \(H=A\)**,

\[
\left|\sqrt{\mathcal C^z_{A,A}}-\sqrt{\mathcal C^x_{A,A}}\right|
\le \frac{\pi}{15A^2}\sqrt{\frac{A(A+1)(A+2)}6}
=\frac\pi{15\sqrt6}A^{-1/2}(1+O(A^{-1})).\tag{ET1c}
\]

Unlike the inherited CC1 bound for prefixes beginning at time 0, this **unconditionally tends to zero** at H=A. The difference of UNSQUARED energies need not tend to zero without an additional bound on either energy; avoid claiming that. The estimate requires the real source T_n bound and is not a 2-adic-to-real signed cancellation law. ∎

## ET2 — frequency-ray rigidity for individual epochs: PROVED LOCAL

For the EXACT completed orbit, \(z_{n+1}=16z_n\pmod1\). Thus, for fixed integer \(h\),

\[
W_A^z(16h)-W_A^z(h)
=\frac{e(hz_{2A})-e(hz_A)}A,
\quad |W_A^z(16h)-W_A^z(h)|\le\frac2A.\tag{ET2a}
\]

For \(h\ne0\), and \(A\ge2|h|\), set \(J=\lfloor\log_{16}((A+1)/(2|h|))\rfloor\). For \(0\le j\le J\), frequencies \(|16^j h|\le(A+1)/2\) have Fejér weight at least 1/2, and \(|W_A^z(16^j h)-W_A^z(h)|\le2j/A\le2J/A\). Accounting for both ± frequencies in the nonnegative energy therefore yields

\[
\boxed{|W^z_A(h)|\le
\sqrt{\frac{\mathcal C^z_{A,A}-1}{J+1}}+\frac{2J}{A}.}\tag{ET2b}
\]

This implication requires the ×16 completed orbit, not a generic circle-point sequence. Positive Fejér boundedness by itself does not imply Haar for arbitrary point arrays (finite half-circle grids are a countermodel). ∎

## ET3 — conditional epoch collision theorem => base-16 π normality: PROVED CONDITIONAL, premise OPEN

Suppose the **original zero-seeded** rational orbit satisfies

\[
\boxed{\mathcal C^x_{A,A}=o(\log A)\quad (A\to\infty)\ \text{for EVERY integer }A\ge1.}\tag{ET3-OPEN}
\]

Then ET1 shows \(\mathcal C^z_{A,A}=o(\log A)\): its square-root is bounded by \(\sqrt{\mathcal C^x}+O(A^{-1/2})\). ET2b forces \(W^z_A(h)\to0\) for every fixed \(h\ne0\). To pass from epochs to ALL prefix horizons, put \(S_N(h)=\sum_{n<N}e(hz_n)\). The relation \((S_{2A}-S_A)/A\to0\) for all A, plus \(|e(hz_n)|=1\), implies \(S_N/N\to0\) by recursively cutting an arbitrary [0,N) into blocks [floor(N/2),N), [floor(N/4),floor(N/2)), ... (each differs from an exact [A,2A) block by O(1) endpoints); fix the number of leading blocks, then make the remaining length arbitrarily small relative to N. Weyl's criterion now proves π normal in base16. **The hypothesis is still OPEN.**

**Relatively dense checkpoints.** More generally the premise need only be verified at a sequence \(A_j\to\infty\) satisfying \(A_{j+1}/A_j\to1\). ET1/ET2 imply \(W^z_{A_j}(h)\to0\). For \(A_j\le A\le A_{j+1}\), boundedness of summands gives \(|W_A(h)-W_{A_j}(h)|\le4(A-A_j)/A_j\to0\). The all-A argument then applies. A sparse doubling-only sequence does **not** suffice by this reasoning. ∎

## ET4 — exact source-epoch all-radius anti-clustering gate: PROVED CONDITIONAL, premise OPEN

Let \(B_A(\delta)\) count ordered pairs \((n,m)\in I_A^2\) with circular distance \(\|x_n-x_m\|_\mathbb T\le\delta\), INCLUDING the A diagonal pairs. Suppose **some fixed K≥2** has, for all sufficiently large A,

\[
\boxed{B_A(\delta)\le A+K A^2\delta\quad
\forall\delta\in[1/(A+1),1/2].}\tag{ET4-OPEN}
\]

The Fejér majorant \(F_A(t)\le\min(A+1,1/[4(A+1)\|t\|^2])\) and the central/annular geometric summation of parent PR #536 CC4 (which depends only on counts, not the starting time) gives

\[
\boxed{\mathcal C^x_{A,A}\le2K+\frac{4(A+1)}{3A}.}\tag{ET4a}
\]

The antecedent therefore implies ET3 and π normality. This is a single **source-selected, all-radius, all-epoch** arithmetic hypothesis, not an estimate we have proved. It may be stronger than normality. The source- and zero-seed-specific rational carry/odd-denominator lag constraints remain necessary to derive it.

**Original-to-completed pair-count robustness.** Put \(t_A=1/[15(A+1)^2]\). Circle triangle inequality gives \(B_A^z(\delta)\le B_A^x(\delta+2t_A)\). Under ET4-OPEN (extended trivially to radii ≥1/2 for K≥2), this yields

\[
\boxed{B_A^z(\delta)\le A+K A^2\delta+\frac{2K}{15}\quad
\forall\delta\in[1/(A+1),1/2].}\tag{ET4b}
\]

The same assertion holds reversing x and z if the bound is assumed for z instead. The critical-scale completion shift adds only a bounded number to the pair-count upper budget. It does not supply ET4-OPEN. ∎

## ET5 — finite exact all-radius certificates, not proof of an all-A bound

An all-real-radius finite certificate requires no floating grid: B_A(delta) is a right-continuous step function; between two consecutive distinct pair distances its value is constant while A+KA²delta is increasing. It is enough to test the initial radius 1/(A+1) and all pair-distance jumps up to 1/2 with EXACT rational comparisons. The standalone `all_radius.py` does this.

**Exploratory already-seen values (not blind holdouts):** the exact maximum required K on ALL radii was approximately 2.37745 at A16, 2.04761 at A32, 1.97651 at A64, 2.06922 at A128 and 2.25129 at A256.

**Post-registration holdouts:** `PREREG_ALL_RADIUS.md` was pushed before the exact all-radius A191 and A319 runs. Both PASS the declared K=3 claim for every real radius: maximum required K approximately 2.052575313 and 2.136958765 respectively. The displayed K values are float diagnostics, but the truth value K<=3 is certified by exact Fraction comparisons. `ALL_RADIUS_HOLDOUT.json` and source code preserve scope.

Finite Fourier diagnostics at A16/32/64/128/256/191/319 have \(\mathcal C^x_{A,A}\) around 1.65–2.47, and the observed critical epoch norm shifts are far below the theoretical bounds; they use floating cosine and are not independent rigorous Fourier interval bounds. No extrapolation is permitted.

**Hostile controls:** a coherent real-periodic β=1/5 completion has constant phases and \(\mathcal C=A+1\). The rational nonnormal 2-adic-isometric H-shadow \(H(n)=n/(2n-1)^4\to0\) places all sufficiently late epoch phases inside a tiny circle arc and fails the K3 near-pair bound. A half-circle uniform grid has Fejér energy <3 in finite tests but is not Haar; this shows why expanding-orbit frequency rigidity in ET2 is indispensable. The fixed four-pole source and literal zero seed are unchanged.

## How this interacts with the newest sibling work

- **#536:** The new epoch critical transport ET1 replaces the inherited O(1) full-prefix Hilbert-loss at H=N by unconditional O(A^-1/2) for late epochs H=A. The all-radius gate remains OPEN; our test sites differ from #536's prefix sites.
- **#532:** Independent sibling prime genealogy proves \(5\le\liminf\log d_n/n\le\limsup\log d_n/n\le8\), strengthening #534's older lower coefficient 2. This proves the **linear high-resolution arithmetic readout**, but does not make small real gaps impossible. No prime-valuation ⇒ real-distance inference is claimed.
- **#535:** The time-return Fejér/Gamma split and dyadic coherence martingale preserve the signed source lag correlations; ET1 provides a sharper *real-completion transfer* for any epoch-local critical norm used in that framework, not a new signed lag bound.
- **#537:** The classical golden quadratic Galois/Tate bridge has authentic \(\chi_5\), Mellin parity and regulator \(\log\varphi\), but it is not an intertwiner into the silver/Gaussian BBP source nor an original-zero selected signed estimate. Treat as a separate typed research track.

## What would actually change the theorem status?

Prove ET4-OPEN uniformly in all sufficiently large original-zero epochs and all critical-to-macroscopic radii, or directly prove ET3-OPEN along sufficiently dense original-zero epochs. Require the true carry chronology and source-specific signed pair information; preserve the rational shadow, wrong completed seed, and source mutation controls. This research package proves the *transfer and sufficiency*, not the remaining arithmetic premise, π normality or RH.
