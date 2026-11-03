# Möbius reflection and the actual SUCC mesoscopic Fejér sheet

**Research-only exact Fourier algebra, ORIGINAL BBP zero seed retained.** This note supplies the positive two-time/sheet audit requested after the little-bird Möbius proposal. It does NOT prove source-selected cancellation or π base-16 normality. Prior art: classic Fejér positive kernel and SUCC #296 Gram purity, #471 Fejér ladder, #474 holomorphic disk, #475 mesoscopic energy.

For a finite source-selected phase list \(x_n=\{U_n\}\), \(0\le n<N\) (or any strict original epoch [A,2A)), write

\[
c_h=\frac1N\sum_n e(hx_n),\quad e(t)=e^{2\pi it},
\qquad
F_H(t)=1+2\sum_{h=1}^H w_h\cos(2\pi h t),\quad
w_h=1-\frac{h}{H+1}.
\]

The existing (selected, real-circle) positive pair **DIFFERENCE** energy is

\[
\boxed{E^-_H=\frac1{N^2}\sum_{n,m}F_H(x_n-x_m)
=1+2\sum_{h=1}^H w_h|c_h|^2.}\tag{MF-01}
\]

For any real mirror axis \(a\in\mathbb T\) let \(J_a(x)=a-x\), and build the positive pair **MIRROR** energy

\[
\boxed{E^+_H(a)=\frac1{N^2}\sum_{n,m}F_H(x_n+x_m-a)
=1+2\sum_{h=1}^H w_h\operatorname{Re}(e(-ha)c_h^2).}\tag{MF-02}
\]

Each kernel value is nonnegative, hence each averaged energy is nonnegative. **But** the matrix with entries \(F_H(x_n+x_m-a)\) need not be positive semidefinite (unlike the difference Gram); do not conflate pointwise positivity with Hilbert Gram positivity.

Put the complex Fourier mirror discrepancy
\(\Delta_a(h)=c_h-e(ha)\overline{c_h}\). Then a direct rearrangement gives the exact **nonnegative defect sheet**

\[
\boxed{E^-_H-E^+_H(a)
=\sum_{h=1}^{H}w_h|\Delta_a(h)|^2\ge0.}\tag{MF-03}
\]

For a=0 this becomes

\[
\boxed{E^-_H-E^+_H(0)
=4\sum_{h=1}^Hw_h(\operatorname{Im}c_h)^2,}
\]
while the complementary even/real part satisfies

\[
\boxed{E^-_H+E^+_H(0)-2
=4\sum_{h=1}^Hw_h(\operatorname{Re}c_h)^2.}\tag{MF-04}
\]

**No one-mirror normality shortcut:** take the coherent completed orbit \(x_n=0\) for all n (real counterseed \(s=-\pi/16\) with the EXACT SAME four-pole forcing). Then \(E^-_H=E^+_H(0)=H+1\) and the mirror defect MF-03 is identically ZERO, while the orbit is maximally nonnormal. One conjugation involution can eliminate the imaginary sector but leaves the real/cosine sector.

With the golden irrational axis \(\eta=(\sqrt5-1)/2\), the exact two-mirror Fourier identity from MM-06 gives for every integer \(h\ne0\)

\[
|c_h|^2\le\frac{9h^2}{8}\big(|\Delta_0(h)|^2+|\Delta_\eta(h)|^2\big).
\]

Summing these nonnegative weights yields an exact **conditional instrument**

\[
\boxed{E^-_H-1\le\frac{9H^2}{4}
\big[(E^-_H-E^+_H(0))+(E^-_H-E^+_H(\eta))\big].}\tag{MF-05}
\]

For a wholly FINITE rational Fibonacci axis \(\eta_k=F_{k-1}/F_k\), choose \(F_k\ge3H\); the Diophantine comparison gives \(|1-e(h\eta_k)|\ge2/(3|h|)\) on 1≤|h|≤H, and the analogous coefficient in MF-05 becomes **\(9H^2\)**. Everything in this finite instrument is a rational original BBP phase or a rational Fibonacci axis before evaluating the final character; it is compatible with exact interval/cyclotomic checks.

**Critical unpaid premise:** to obtain the mesoscopic condition of #475 \(E^-_{A,H_A}=o(\log A)\), it would be enough to prove the combined two-mirror source-selected gap \(E^-_H-E^+_H(0)+E^-_H-E^+_H(\eta)=o(\log A/H_A^2)\). This is a much stronger and potentially worse estimate than original Fejér energy; it is NOT supplied by algebraic reconstruction. Both discrepancies are functions of the same \(c_h\), so they are NOT independent witnesses of source cancellation. The value lies in exposing exactly which symmetry sector remains and providing two well-conditioned finite probes.

**Finite source reflection path:** the true intertwiners \(J_n(x)=-x-2T_n\) are *moving*, not fixed J_0; their distance to fixed reflection on a late window is bounded by the authentic positive Gamma tail. Replacing \(J_n\) by fixed J_0 in chronological statistics incurs the recorded O(1/A) phase budget for fixed h, but **moving axes vary across times and do not define the same single empirical-measure pushforward.** Source/mirror cross-pairs require a separate typed map; do not infer statistical invariance of the original measure from exact cocycle gluing.

**Next falsifying probe:** at preregistered fresh original dyadic epochs and harmonics, compute the exact rational source phase once; evaluate Fejér \(E^-\), the reflected \(E^+(0)\), the finite-golden \(E^+(\eta_k)\), and their two nonnegative defects using independent interval oracles. Compare same-original-four-pole coherent seed, rational 1/5 and 1/7 periodic controls, and q-sheet seed Haar controls. Prove an all-epoch signed/near-pair saving or admit the instrument merely reconstructs the old gate. No π normality or physical quantum claim is inferred.
