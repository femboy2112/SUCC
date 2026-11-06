# TS-10 — the original BBP Gamma/Harmonic/Silver first-moment theorem

**2026-11-06 · PROVED LOCAL by exact partial fractions, digamma identities, polynomial inequalities.** The finite observations were preregistered after the symbolic derivation; they are not the proof or a blind discovery. This theorem is source-specific for the authentic four signed poles and **independent of any hypothetical real-digit distribution of π**.

## The source-specific renormalization identity

Let
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
H_N=\sum_{n=1}^N\frac1n,\quad a=\frac{15}{64}.
\]
Define the original first-moment harmonic renormalization
\[
B_N=\sum_{n=1}^N\left(nr(n)-\frac{a}{n}\right).
\]
Then **for every N≥2**, \(B_N\) increases strictly to the finite constant
\[
\boxed{
B=\frac{(27+31\sqrt2)\pi}{128}
+\frac{39}{32}\log2
+\frac{31\sqrt2}{64}\log(1+\sqrt2)
=3.1872129896451079923900811167107348\ldots
}\tag{TS10a}
\]
with the **effective certified real bound**
\[
\boxed{0<B-B_N<\frac{241}{288N}.}\tag{TS10b}
\]
It follows that
\[
\boxed{\sum_{n=1}^N nr(n)=\frac{15}{64}H_N+B-E_N,\quad
0<E_N<\frac{241}{288N},}\tag{TS10c}
\]
and since \(H_N-\log N\to\gamma\), the exact Euler–Mascheroni renormalization is
\[
\boxed{
\lim_{N\to\infty}\left(\sum_{n=1}^N nr(n)-\frac{15}{64}\log N\right)
=\frac{15}{64}\gamma+B.
}\tag{TS10d}
\]

## Proof 1: the leading harmonic divergence is forced by the original four poles

Write \(c=(4,-2,-1,-1)\), \(e=(7,4,3,2)\), so
\[
r(n)=\sum_{i=1}^{4}\frac{c_i}{8n-e_i},\quad
\sum_i c_i=0,\quad\sum_i c_i e_i=15.
\]
The geometric expansion \(1/(1-u)=1+u+u^2/(1-u)\) gives, for n≥2,
\[
r(n)=\frac1{8n}\sum_i c_i+\frac1{64n^2}\sum_i c_i e_i+
\sum_i\frac{c_i e_i^2}{512 n^3(1-e_i/(8n))}.
\]
Thus \(r(n)=15/(64n^2)+O(n^{-3})\) with its **precise source-determined** coefficient \(a=15/64\). Since \(e_i/(8n)\le7/16\) and \(\sum|c_i|e_i^2=241\), for all n≥2,
\[
\left|nr(n)-\frac a n\right|
\le\frac{241}{512n^2}\frac{16}{9}
=\frac{241}{288 n^2}.
\]
Summing over n>N and \(\sum_{n>N}n^{-2}<1/N\) proves the upper tail bound.

**Strict positivity** does not follow from the absolute bound alone; verify the exact rational identity
\[
nr(n)-\frac{15}{64n}
=\frac{9664n^3-9656n^2+3090n-315}
{64n(2n-1)(4n-1)(8n-7)(8n-3)}.
\]
For every integer n≥1, the numerator equals
\(n^2(9664n-9656)+3090n-315>0\), and all denominator factors are positive. Thus the remainder is positive at every n, so B_N increases strictly and the tail E_N is positive.

## Proof 2: digamma/Gamma reconstructs the exact silver-ratio finite part

Let \(\alpha=(1/8,1/2,5/8,3/4)\), \(d_i=c_i(1-\alpha_i)=(7/2,-1,-3/8,-1/4)\). The identity
\[
nr(n)=\frac18\sum_i c_i\left(1+\frac{1-\alpha_i}{n-1+\alpha_i}\right)
=\frac18\sum_i\frac{d_i}{n-1+\alpha_i}
\]
uses \(\sum c_i=0\). Since \(\sum d_i=15/8\), the digamma recurrence and \(H_N=\psi(N+1)+\gamma\) give
\[
\begin{aligned}
B_N
&=\frac18\sum_i d_i\left[\psi(N+\alpha_i)-\psi(\alpha_i)\right]
-a[\psi(N+1)+\gamma].
\end{aligned}
\]
As \(N\to\infty\), \(\psi(N+\alpha)-\psi(N+1)\to0\), hence
\[
B=-\frac18\sum_i d_i\psi(\alpha_i)-a\gamma.
\]
Insert the classical Gauss rational digamma evaluations already used in TS5:
\[
\begin{aligned}
\psi(1/8)&=-\gamma-4\log2-\frac\pi2(1+\sqrt2)-\sqrt2\log(1+\sqrt2),\\
\psi(1/2)&=-\gamma-2\log2,\\
\psi(5/8)&=-\gamma-4\log2-\frac\pi2(1-\sqrt2)+\sqrt2\log(1+\sqrt2),\\
\psi(3/4)&=-\gamma-3\log2+\frac\pi2.
\end{aligned}
\]
Because \(\sum_i d_i/8=a\), the gamma terms cancel **inside B**, yielding the exact claimed expression. In contrast, subtracting \(a\log N\) rather than the canonical harmonic \(aH_N\) leaves \(a\gamma\) as the universal harmonic/archimedean counterterm.

This is a **typed**, source-grounded realization of a *harmonic ↔ Gamma ↔ silver-Pisot* triangle. It does not canonically identify φ, γ or real phase as elements of Q₂ or establish a Fourier signed-saving inequality.

## A genuinely discriminating gauge counterexample

Use parent SUCC #527's rational isometric shadow \(H(z)=z/(2z-1)^4\), with \(H(0)=0\), \(H(n)>0\), \(H(n)=O(n^{-3})\). Define the *nonoriginal* coboundary-mutant source \(r_*(n)=r(n)+2H(n)-32H(n-1)\). Parent #527 shows this retains literal zero, the real completed π orbit and 2-adic boundary/isometry.

Because \(n[r_*(n)-r(n)]=O(n^{-2})\), the leading original harmonic \(a=15/64\) and thus the gamma counterterm **are unchanged**. Yet the finite source remainder is NOT invariant:
\[
\boxed{
B_*-B=2\sum_{n\ge1}n[H(n)-16H(n-1)]
=-2\sum_{n\ge1}(15n+16)H(n)<0.
}\tag{TS10e}
\]
The shifted summation is justified by absolute convergence of \(nH(n)\). Therefore the silver analytic B **fingerprints source choice**, but is **not** a source-coboundary invariant of the completed real π orbit; it cannot alone certify normality. This is an essential hostile source-map distinction, not a defect.

For the pure H-shadow source \(\widetilde r(n)=H(n)-16H(n-1)\), we have \(\widetilde r(n)=O(n^{-3})\), so its weighted \(n\widetilde r(n)\) is summable and its harmonic/logarithmic leading coefficient is **zero**. This rules out inferring the same analytic triangle from 2-adic isometry alone.

## Provenance, execution, limitations

- The authenticated four poles and zero seed were read from #527/#528; the digamma identity and harmonic expansion are classical. This exact weighted calculation is locally derived, **not claimed as a world-priority discovery**.
- PREREGISTRATION_GAMMA_MOMENT.md froze N=128,512,1024 **after the derivation**, before fresh numeric checks. first_moment.py performs exact Fraction prefix computations, stdlib Decimal display via a tighter rational Machin enclosure, exact positive remainder tests; an optional independent SymPy audit verifies rational/digamma reduction. All observed finite gaps lie inside the analytically proved \(241/(288N)\) envelope.
- No external peer review, Lean kernel, source-selected real phase correlation asymptotic, or π normality proof. These analytic source moments are *not* real Weyl signed cancellations. A phase transport satisfying the precise BBP zero boundary remains OPEN.
