# Audit extension: nonlinear delayed-observer bispectrum and a weaker critical carry gate

**2026-11-04 research audit, additive child of draft PR #507** at exact parent \`c49cc0951981883c8f9a66e3b9c27be18c4fd4b1\`. Original signed BBP poles and literal \`U_0=Y_0=Z_0=0\` unchanged. This audit is a **new algebraic representation and sharpened sufficient condition**, NOT a new original signed-Weyl bound, theorem of π normality, or an independently externally refereed result.

## AB-01: an odd-order observer recovers the lost angular phase (EXACT, elementary)

On the authenticated original BBP stream \`U_n=Y_n+Z_n\`, with genuine \`Z_n\` from #499/#504/#506/#507, define at any integer Fourier frequency H the forward delayed character
\[
v_j(n;H)=e(H[Y_n+Z_{n+j}]),\qquad j\ge1,\quad e(x)=\exp(2\pi i x).
\]
For each integer m>=1 let \`c_j=(-1)^(j-1) binom(m,j)\` for j=1,...,m. As \`sum_j c_j=1\`, the nonlinear observation
\[
Q_m(n;H)=\prod_{j=1}^m v_j(n;H)^{c_j}
\]
retains exactly ONE angular factor (negative powers mean complex conjugates). The binomial formula gives the exact identity
\[
\boxed{Q_m(n;H)=e(HU_n)e\big((-1)^{m+1}H\Delta^m Z_n\big),\quad
\Delta^m Z_n=\sum_{j=0}^m(-1)^{m-j}\binom mj Z_{n+j}.}
\tag{AB1}
\]
No real π digits or distribution hypothesis enter. This works for any common angular sequence, so it is a **representation**, not an automatic original-seed mixing inequality. It is nonlinear in the delayed characters; the #507 raw Gram erases Y because its second-order products have total angular exponent 0. Here the total exponent is 1, so **the angular phase survives**.

The first nontrivial curvature-corrected case is the **cubic bispectrum**
\[
\boxed{Q_2(n;H)=v_1(n;H)^2\overline{v_2(n;H)}
=e(HU_n)e(-H\Delta^2 Z_n).}\tag{AB2}
\]
The two linear radial delays reconstruct the time-zero radial phase with a second-difference defect, avoiding a separate large-variation linear multiplier inversion. This is an *observer-phase identity*, not a phase-mixing estimate.

## AB-02: the genuine original-source m=2 critical error is negligible (EXACT BOUND)

The inherited **source-derived** #507 CF4 curvature bound gives, for all real x>=128,
\[
0<z''(x)\le1/(8x^3).
\]
The second finite difference has the positive integral representation
\[
\Delta^2 Z_n=\int_0^1\!\int_0^1 z''(n+s+t)\,ds\,dt,
\]
hence \`0<Delta²Z_n<=1/(8n³)\` for integer n>=128. Therefore by the chord bound \`|e(x)-e(y)|<=2π|x-y|\`,
\[
\boxed{\sup_{I\subseteq[A,2A)}\frac1A
\left|\sum_{n\in I}\big[Q_2(n;H)-e(HU_n)\big]\right|
\le\frac{\pi |H|}{4A^3}=\frac{\pi\Lambda}{4A}.}\tag{AB3}
\]
Here I ranges over every consecutive subinterval and \`Lambda=|H|/A²\`. In particular the corresponding maximal mean **magnitudes** differ by at most the same bound. At the actual #501/#503 critical schedule \`Lambda_A ~ log A\`, so
\[
\boxed{\Lambda_A\,|M_A^{\rm bispec}(H_A)-M_A^{(0)}(H_A)|
\le\pi\Lambda_A^2/(4A)\to0.}\tag{AB4}
\]
This is a **sharp-target-compatible nonlinear observer**: proving the little-o critical ratchet for the authentic Q2 bispectrum would suffice for the original source. Crucially, Q2 **still contains the unknown Y**, so this does not itself prove a saving. The same-forcing coherent seed remains coherent under Q2, since the discrepancy bound is seed-independent. The simple linear Gram/no-phase-selection obstruction no longer applies to Q2, but the deeper source-selected signed-correlation problem remains.

For each **fixed** higher m, source differentiation gives \`|Delta^m Z_n|<=C_m/A^(m+1)\`, so \`Q_m\` offers higher-order critical approximations \`O_m(Lambda/A^(m-1))\`. This is not uniform for m growing with A; binomial coefficients and observer order grow.

## AB-03: source-specific high-order cumulants, not the Y-blind Gram (NEW PROBE, UNVERIFIED)

The second-order Gram \`A^-1 sum_n v_j(n) conjugate(v_k(n))\` cancels the common angular phase. By contrast the cubic moment \`A^-1 sum_n v_1(n)^2 conjugate(v_2(n))\` preserves one angular phase and differs from the original signed Weyl mean by O(Lambda/A).

**Proposed probe:** Seek an original-source arithmetic/carry restriction on this cubic moment, with a genuine signed saving at the high-depth schedule. Use the literal zero boundary, prime-Frobenius signs, and full 16-adic/odd-denominator/real numerator synchronization. This is more discriminating than a second-order Gram-only attempt. It is, however, nearly **equivalent** in difficulty to the original Weyl estimate unless one proves a fresh source-specific trilinear inequality. A universal cubic estimate is refuted by the coherent same-four-pole changed seed; it must exclude that source member via a load-bearing initial-boundary/arithmetic hypothesis.

Recommended controls: true zero-seed U, coherent wrong seed s*=-π/16, the genuine radial-only Z, source-change cofactor mutants #505, and different lags. Do not claim that complex triple moments are physical quantum interference.

## AB-04: optimize #507 NEXT's sufficient carry-correlation target (EXACT IMPLICATION)

Define the original selected \`u_n=e(H_A U_n)\` and for a given lag depth D<=A,
\[
K_{A,D}(I)=\frac1{DA}\sum_{d=1}^{D-1}\left(1-\frac dD\right)
\Re\sum_{\substack{n,n+d\in I}}u_{n+d}\overline{u_n},
\]
where every I is consecutive in [A,2A). This is the **source-authentic** mixed lag statistic; it is exactly expressible with literal rational carry cells as in #507 SIGNED_WEYL.md. Van der Corput gives for all I
\[
\left(A^{-1}|\sum_{n\in I}u_n|\right)^2
\le(1+D/A)\left(D^{-1}+2K_{A,D}(I)\right).
\]
Choose any integers \`D_A\` satisfying
\[
D_A=o(A),\qquad \frac{\Lambda_A^2}{D_A}\to0;
\]
e.g. \`D_A=ceil((log A)^2 log log A)\` at the fixed-h critical schedule. Then the **weaker prospective condition**
\[
\boxed{\max_{I}\max(0,K_{A,D_A}(I))=o_h(\Lambda_A^{-2})}
\tag{AB5}
\]
already implies \`Lambda_A M_A^{(0)}(H_A(h))→0\`, hence the inherited sufficient normality gate. #507 NEXT instead proposed the stronger \`D=ceil(log³A)\` and \`K=O_h(log^-3 A)\`. Nothing proves either. The corrected target can guide a lower-cost signed carry-sieve attempt but does not create a new source-selected bound.

The coherent wrong-seed remains a falsifier: on the full epoch its bounded-lag correlations tend to 1 for \`D_A Lambda_A/A→0\`, and K tends to 1/2. This source-specific discrimination is qualitative; the original selected K bound remains UNVERIFIED.

## Audit scope and verdict

- AB1–AB4: exact elementary observer algebra plus inherited **source-derived** radial curvature; valid for genuine original source, no independent external normality proof. Exact finite Fraction calibration in \`tests/test_zero_frame_bispectrum_audit.py\`.
- AB5: a logically weaker sufficient condition extracted from #507's already proved van der Corput inequality. NO claim that it is known to hold.
- The nonlinear observer escapes only the **Y-erasure** of the linear lag Gram. It does **not** supply a new bound on the authentic angular phase and does not refute #507's negative results about linear infinite stencils and arbitrary-multiplier inversion.
- π base-16 normality, selected fixed-h Weyl, original critical ratchet, and RH remain OPEN. No worldwide scholarly novelty claim, no new Lean proof, no hosted CI certification of this audit.
