# Orbit Pauli exclusion: Fourier frame purity and a quantitative antisymmetric Fekete certificate

**2026-11-05; research-only child of SUCC #512 at immutable SHA \`effbd923578a160ddbb792265a6a5ed311ff342f\`.** The original four signed BBP poles, literal U0=0, historical theorem contracts, archived source, Lean, production, workflows, licensing, and main are untouched. This is CLASSICAL harmonic analysis and logarithmic potential theory, specialized here to SUCC's actual source points. **It is not an independently proved signed BBP normality estimate, a physical Pauli principle, or a new mathematical priority claim.**

Write \(e(x)=e^{2\pi ix}\). Given arbitrary \(N\ge2\) real phases \(x_1,\dots,x_N\), let \(z_j=e(x_j)\), and let
\[
c_N(h)=N^{-1}\sum_{n=1}^N e(hx_n),\quad h\in\mathbb Z.
\]

## PF-01: Fourier-mode "occupancy" is exactly the fixed-band Welch/frame-purity excess

For any integer M>=1 form the normalized character vectors
\[
v_M(x)=M^{-1/2}(1,e(x),e(2x),\ldots,e((M-1)x))^T\in\mathbb C^M,
\]
and the positive empirical frame operator
\[
S_{N,M}=\frac1N\sum_{n=1}^Nv_M(x_n)v_M(x_n)^*,
\quad S_{jk}=\frac1M c_N(j-k).
\]
It has \(S\ge0,\operatorname{Tr}S=1\). By Cauchy–Schwarz on its M eigenvalues, \(\operatorname{Tr}S^2\ge1/M\). Computing its entries gives the **EXACT** identity
\[
\boxed{
\operatorname{Tr}S_{N,M}^2
=\frac1M+\frac2{M^2}\sum_{h=1}^{M-1}(M-h)|c_N(h)|^2.
} \tag{PF1}
\]
Equality to 1/M holds iff \(c_N(h)=0\) for all \(1\le h<M\), equivalently \(S=I_M/M\). Thus for every fixed M, \(\operatorname{Tr}S_{N,M}^2\to1/M\) iff the first M-1 Fourier characters decay; doing so for ALL fixed M is EXACTLY the Weyl criterion. This is an **operational finite-band mode-exclusion certificate**, not a new source-derived bound. A family of phases can be pairwise distinct and still have highly nonuniform Fourier occupancy.

## PF-02: fermionic antisymmetry yields a stronger, genuinely ALL-MODE sufficient condition

Form the N×N Vandermonde/Slater matrix \(V_{jn}=z_n^j\), \(j=0,\ldots,N-1\), and its determinant \(\Delta_N\). Vandermonde factorization gives
\[
\boxed{|\Delta_N|^2=\prod_{1\le i<j\le N}|z_j-z_i|^2.} \tag{PF2}
\]
Its columns have Euclidean norm \(\sqrt N\), so Hadamard yields
\[
\boxed{|\Delta_N|^2\le N^N,\qquad
\mathcal E_N:=N^{-2}\log|\Delta_N|^2\le(\log N)/N.} \tag{PF3}
\]
If any phases coincide, define \(\mathcal E_N=-\infty\). Equality in PF3 occurs for a rotated complete set of Nth roots of unity: their Fourier columns are orthogonal. This is the classical Fekete problem on S¹.

**A quantitative direct bridge to Weyl.** For any fixed \(0<r<1\), the regularized logarithmic kernel
\[
K_r(t)=-\log|1-r e(t)|=\sum_{h\ge1}\frac{r^h}h\cos(2\pi h t)
\]
converges absolutely. Therefore
\[
\boxed{
\frac1{N^2}\sum_{i,j=1}^N K_r(x_i-x_j)
=\sum_{h\ge1}\frac{r^h}h|c_N(h)|^2\ge0.
} \tag{PF4}
\]
For \(i\ne j\), write \(d=|z_i-z_j|\in(0,2]\). Then
\(|1-r e(x_i-x_j)|^2=(1-r)^2+r d^2\).
The function \(d^2/[(1-r)^2+r d^2]\) increases with d² on [0,4], and its maximum at d²=4 is \(4/(1+r)^2\). Consequently,
\[
K_r(x_i-x_j)\le-\log|z_i-z_j|+\log\frac2{1+r}
\quad(i\ne j),
\]
while each diagonal \(K_r(0)=-\log(1-r)\). Summing ALL terms and using PF2 gives, with the convention of a vacuous inequality if \(\mathcal E_N=-\infty\),
\[
\boxed{
\sum_{h\ge1}\frac{r^h}h|c_N(h)|^2
\le-\mathcal E_N+
 (1-\tfrac1N)\log\frac2{1+r}
 +\frac{-\log(1-r)}N.} \tag{PF5}
\]
Choose \(r_N=1-1/N\) for N>=2. Then
\[
\boxed{
\frac{r_N^h}{h}|c_N(h)|^2
\le-\mathcal E_N+\frac{\log N+1}N
\quad\text{for every integer }h\ge1.} \tag{PF6}
\]
Every step is a finite exact inequality between elementary kernels; the only continuum Fourier series is absolutely convergent for r<1. No unproved equidistribution or Haar sampling enters.

**Theorem (Fekete exclusion ⇒ equidistribution).** If for an ordered infinite orbit \(x_n\)
\[
\boxed{\liminf_{N\to\infty}\mathcal E_N\ge0,} \tag{PF7}
\]
then PF3 implies \(\mathcal E_N\to0\). PF6 implies \(c_N(h)\to0\) for every fixed nonzero integer h. By Weyl, the orbit is equidistributed on the circle. More quantitatively, if \(\mathcal E_N\ge-\varepsilon_N\) with \(\varepsilon_N\ge0\), then
\[
\boxed{
|c_N(h)|^2\le\frac h{(1-1/N)^h}
\left(\varepsilon_N+\frac{\log N+1}N\right).}\tag{PF8}
\]
This is a coherent "Pauli-like" antisymmetric **SUFFICIENT** equidistribution mechanism. It is not NECESSARY: a normal sequence can contain sparse equal points (then \(\mathcal E_N=-\infty\) for all subsequent prefixes), or sparse extremely close but distinct points, without changing its limiting distribution. Also PF7 is stronger and potentially **harder** than the original Weyl limit.

To use this theorem on SUCC epochs \(n=A,\ldots,2A-1\), replace N by A and \(x_j=U_{A+j-1}\bmod1\). A source-derived proof of \(\inf_{A\to\infty}\mathcal E_A^{\rm orig}\ge0\) for ALL sufficiently large integer epochs A would give uniform Haar limits on every such epoch. Geometrically decomposing long prefixes into dyadic-length consecutive epochs then implies the full original Weyl criterion, with bounded initial blocks negligible. The theorem does not assert this new source inequality.

## PF-03: local "hard core" exclusion is NOT enough

Take \(x_{N,j}=j/(2N)\), j=0,...,N-1. All phases are distinct, with minimum circular spacing exactly \(1/(2N)\). The empirical measure nevertheless converges to twice Lebesgue measure on HALF the circle, not Haar on all of S¹. In particular
\[
\boxed{
\left|\lim_{N\to\infty}c_N(1)\right|=2/\pi>0.
}\tag{PF9}
\]
Moreover direct pair-distance counting gives
\[
\mathcal E_N
=\frac2{N^2}\sum_{d=1}^{N-1}(N-d)
\log\!\left(2\sin\frac{\pi d}{2N}\right).
\]
The integrable-log-endpoint Riemann sum tends to
\[
2\int_0^1(1-t)\log(2\sin(\pi t/2))\,dt
=-\frac4{\pi^2}\sum_{\substack{k\ge1\\k\ \mathrm{odd}}}k^{-3}
=\boxed{-\frac{7\zeta(3)}{2\pi^2}\approx-0.4262784.}\tag{PF10}
\]
The identity follows from the classical \(\log(2\sin(\vartheta/2))=-\sum_{k\ge1}\cos(k\vartheta)/k\) in an Abel-regularized form; the cosine integral vanishes for even k and is \(2/(\pi^2k^2)\) for odd k. The endpoint logarithm is integrable, so the discrete-to-integral limit is justified by truncating its neighborhood and bounding that tail using \(\log t\) integrability.

Thus eliminating exact or microscopic collisions does not enforce global uniform occupancy. SUCC #501's microscopic collision theorem is relevant, but cannot by itself provide PF7 without genuinely broader scale control.

## PF-04: the coherent same-four-pole WRONG seed fails drastically

Use the authenticated original forcing \(r_o(n)\), but choose \(s_*=-\pi/16\) instead of its literal original \(s=0\). The exact completed solution is \(U_n(s_*)=-T_n\), where \(T_n=\sum_{k\ge1}16^{-k}r_o(n+k)\). The earlier SUCC #503/#505 source theorem supplies
\[
0<T_n<\frac1{64n^2}.
\]
For the A selected times \(n=A,\ldots,2A-1\), all wrong-seed phases lie in a circle arc of length at most \(T_A<1/(64A^2)\). Every chord therefore has length at most \(2\pi T_A<\pi/(32A^2)\), and
\[
\boxed{
\mathcal E_A^{(s_*)}
\le\left(1-\frac1A\right)
\left(\log\frac\pi{32}-2\log A\right)
\longrightarrow-\infty.} \tag{PF11}
\]
The wrong seed is not excluded merely for violating a source-contract word: it VIOLATES a precise global anti-concentration determinant condition by an amount growing with log A. The forcing (and radial source) is the same; the initial seed differs. This is a genuinely discriminating prospective source-level theorem, but PF7 remains unproved for the original zero seed.

## PF-06: the exact multiscale exclusion/current identity

This identifies **precisely** how SUCC's pair-count technology could bear on the new Fekete sufficient condition, without assuming any distribution theorem.

For arbitrary N distinct phases let \(\delta_{ij}=\|x_i-x_j\|_{\mathbb R/\mathbb Z}\in(0,1/2]\), and define the normalized **ordered off-diagonal** close-pair count
\[
C_N(t)=\frac1{N^2}\#\{(i,j):i\ne j,\ \delta_{ij}\le t\},
\qquad 0\le t\le\tfrac12.
\]
Because \(d_{ij}=|z_i-z_j|=2\sin(\pi\delta_{ij})\) and
\[
\log[2\sin(\pi\delta)]=\log2-\int_\delta^{1/2}\pi\cot(\pi t)\,dt,
\]
interchanging a FINITE sum and the nonnegative integral (all phases distinct) yields
\[
\boxed{\mathcal E_N=
(1-\tfrac1N)\log2-\int_0^{1/2}\pi\cot(\pi t)\,C_N(t)\,dt.}\tag{PF12}
\]
Now use the elementary exact identity
\[
\int_0^{1/2}\pi\cot(\pi t)\,2t\,dt=\log2.
\]
It follows that
\[
\boxed{
\mathcal E_N=
-\int_0^{1/2}\pi\cot(\pi t)
\Big[C_N(t)-2(1-\tfrac1N)t\Big]dt.
}\tag{PF13}
\]
The weight is positive, behaves like \(1/t\) near zero, and vanishes at t=1/2. This is an **exact multiscale excess-collision budget** relative to a finite-mass Haar reference \(2(1-1/N)t\). If phases repeat, both the full logarithmic energy and the improper collision integral diverge in the appropriate direction.

Thus a SUCC source-derived **UPPER bound on the weighted positive excess of \(C_A(t)-2(1-1/A)t\) by o(1)** would immediately yield \(\mathcal E_A\ge-o(1)\), and therefore original Weyl equidistribution by PF6. This is a rigorous alternative sufficient obligation stated entirely in terms of pair occupancy across ALL scales. A small-scale collision estimate alone does NOT suffice.

**Half-circle mutant exposes the scale issue exactly.** The limiting empirical measure \(2\mathbf1_{[0,1/2]}(x)\,dx\) has close-pair distribution
\[
C_{\rm half}(t)=4t-4t^2,\quad 0\le t\le1/2,
\]
whereas Haar has \(C_{\rm Haar}(t)=2t\). Their difference \(2t(1-2t)>0\) for ALL interior scales, producing the negative energy PF10. Every finite half-grid nevertheless has separation \(1/(2N)\): hard-core separation **does not pay the mesoscopic/macroscopic collision excess**.

**Critical research boundary.** PF12–PF13 are classical layer-cake rewritings of the determinant energy. They move the source proof obligation from an Archimedean determinant lower bound to a global signed pair-count inequality. They do NOT prove either inequality for the selected original π orbit. Existing #501 near-collision saving at microscopic widths is valuable input, but it does not control the entire positive weighted excess. No source- or π-specific generalization of Haar has been assumed.

## PF-05: source arithmetic and the missing bridge

At every n the actual original zero-seeded U_n is rational, and the phase z_n=e(U_n) is a root of unity. On a finite epoch one can clear denominators with a common LCM L and regard each z_n as a power of a primitive Lth root. However a Galois norm of \(\Delta_N\) averages ALL cyclotomic embeddings; a lower bound on that integer norm does NOT bound the original selected real/complex embedding unless the other conjugates are controlled. This is the same **source-selected Archimedean orientation problem** exposed by #505's cofactor/carry mutants. A crude lower bound from minimum distinct Lth-root spacing of order 1/L only gives \(\mathcal E_N\gtrsim-\log L\), hopeless when L grows exponentially.

The next source-bearing proof would need a **multiscale pair-distribution bound**, or a direct arithmetic lower bound on the ORIGINAL selected Vandermonde determinant of strength \(N^{-2}\log|\Delta_N|^2\ge-o(1)\), or source-specific flattening of finite Fourier frame operators without assuming Haar. Every claim must distinguish the literal U0=0 and fail for same-forcing coherent wrong seed. A Pauli/Slater representation with no such source bound is a valid mathematical lens, not a normality proof.

**Verdict:** PF1–PF11 exact classical proofs within their stated scope; fresh finite original source measurements are OBSERVED with exact rational phase inputs but finite floating logarithms. Original selected determinant asymptotics, original signed Weyl decay, original critical sharp-interval rate, base-16 π normality and RH remain OPEN.

### Primary references (classical theorems, not newly proved globally)

E. Saff, *Logarithmic Potential Theory with Applications to Approximation Theory* https://www.math.vanderbilt.edu/saffeb/texts/230.pdf — Vandermonde/Fekete points and logarithmic energy.

*Mutually asymptotic Fekete sequences* (Mathematische Annalen, 2025), https://doi.org/10.1007/s00208-024-03088-0 — modern asymptotically Fekete/equidistribution context.
