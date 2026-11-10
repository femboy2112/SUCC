# Origin-locked spectral fingerprints: arithmetic seed sidebands, π-source cohomology and digit-resolution thresholds

**2026-11-08. Research-only additive child of SUCC draft #554, exact parent `90711d2e9dc73020acbc4cde1ad058b62ef54a4d`; main baseline `43a607818907120d4cdab73d240f5b4d7700b63f`.** The original four signed poles, literal zero seed and frozen provenance are unchanged. Classical material is explicitly identified. None of the claims proves π base-16 normality or RH, or worldwide academic priority. Source-preserving and seed-changing statements must not be conflated.

## Typed objects and the user's strongest hypothesis

The proposed spectral-fingerprint observer should remember *which source and which origin produced* a time-labelled circular observation. It should work with stratified digit/clock readings and calibrate a phase against relative paths on the **same** carrier. The difficult demand is not injectivity of arbitrary complete observations: it is a bound on the original-zero **signed real** character, not supplied by exact reconstruction.

For all integers n≥1, preserve

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0(s)=s,\quad U_n(s)=16U_{n-1}(s)+r(n).
\]

Let \(P(r)=\sum_{j\ge1}16^{-j}r(j)=\pi/16\), \(T_n(r)=\sum_{j\ge1}16^{-j}r(n+j)\), \(e(t)=e^{2\pi it}\). Distinguish: (i) source period P; (ii) completed expanding-orbit point \(\alpha=s+P\); (iii) finite source/carry history; (iv) a time/seed-labelled **complex** character; (v) a source-mutant's own genuine prime passport. Under arbitrary seed changes, P is fixed, but \(\alpha\) generally **is not**.

## OSF-01 — exact pointed π invariant and seed cocycle (PROVED ALGEBRAIC)

For every real s and n≥0, with T_0=P,

\[
\boxed{U_n(s)=16^n(s+P)-T_n,\qquad 16^{-n}(U_n(s)+T_n)-s=P=\pi/16.}\tag{1}
\]

Thus a seed translation by q acts exactly as

\[
\boxed{U_n(s+q)-U_n(s)=16^nq,\quad
 e(hU_n(s+q))=e(h16^nq)e(hU_n(s)).}\tag{2}
\]

The **pointed, gauge-corrected character**

\[
Z_{n,h}^{\rm pin}(s)=e(h[U_n(s)-16^ns])=e(hU_n(0))\tag{3}
\]

is independent of s for any real seed q; it is precisely the original selected character, not an independently proved cancellation. The correction requires knowing the source-time origin s to an accuracy amplified by 16^n. If its uncertainty is ε, the phase error is at most \(2\pi|h|16^n\varepsilon\). This is the origin-precision cost; it cannot be removed by a gauge-invariant norm.

**Proof:** finite expansion of the recurrence; add the future geometric tail and subtract the origin. Equation (3) is an exact change-of-frame identity. **Control:** s*=−P gives \(U_n(s*)=−T_n\to0\), so \(e(hU_n(s*))\to1\) while the corrected character remains the authentic (still unproved) zero-seed character. Thus unpointed arbitrary-real-seed invariance of orbit statistics is FALSE.

### Finite source paths already carry the same invariant, with a paid tail

For n,L≥0, replace T_n by \(T_{n,L}=\sum_{j=1}^{L}16^{-j}r(n+j)\). Then for every rational (indeed real) seed,

\[
\boxed{16^{-n}(U_n(s)+T_{n,L})-s
 =\sum_{j=1}^{n+L}16^{-j}r(j)=:P_{n+L}.}\tag{4}
\]

This is *exact at finite horizon* and independent of the split n versus L; relative paths reconstruct the same authenticated partial source. From the original positive Laplace density \(Q(x)=2(1-e^{-3x})+(1-e^{-4x})+(1-e^{-5x})\) we have \(0<Q(x)<15x\). Hence for n≥2, \(0<r(n)<15/(8n-7)^2<15/[64(n-1)^2]\). Therefore, for every M≥1,

\[
\boxed{0<P-P_M=16^{-M}T_M<\frac{16^{-M}}{64M^2}.}\tag{5}
\]

A finite *rational interval* certifies the first k hexadecimal digits of P if its two endpoints occupy the same base-16 cylinder of depth k. Exact Fraction replay at (M,k)=(40,32) certifies `3243f6a8885a308d313198a2e0370734`; an independent Machin arctangent rational interval selects the same cylinder. The result is **32 finite digits of π/16**, not a proof of any frequency.

## OSF-02 — exact tail-observer alias tower (PROVED ALGEBRAIC)

Observe all the phase characters \(e(hU_n(s))\) for n≥N and a finite set \(\mathcal H\subset\mathbb Z\setminus\{0\}\) with gcd g>0. A rational seed difference q is **exactly invisible** to all these observations iff

\[
\boxed{g16^Nq\in\mathbb Z.}\tag{6}
\]

For the full frequency set (or just h=1), the alias subgroup of the seed circle is \(16^{-N}\mathbb Z/\mathbb Z\), with **16^N different initial seeds**. For a single h it has \(|h|16^N\) elements. Necessity follows from n=N; sufficiency from the recurrence's integral 16 multiplier. Thus an arbitrary infinite *tail* of exact phase observations does not reconstruct discarded origin digits: the missing history is an exact finite deck group, not a numerical conditioning artifact. Observing a full lifted origin fixes it. A finite block of **digit cells**, rather than exact phases, leaves an interval of possible origins, not merely a finite alias set.

## OSF-03 — rational seed spectroscopy has finitely many pure-point sidebands (PROVED; DFT CLASSICAL)

Write q=a/(2^v m) reduced, with m odd. Set \(n_0=\lceil v/4\rceil\), and d=ord_m(16), or d=1 for m=1. Then \(e(h16^n q)\) is periodic after n_0, with minimal *phase* period dividing d (d is the seed's multiplicative-clock period; the character h can shorten it). For each fixed integer h,

\[
\boxed{e(h16^{n_0+j}q)=\sum_{\ell=0}^{d-1}c_\ell(q,h)e(\ell j/d),\qquad
 c_\ell=\frac1d\sum_{t=0}^{d-1}e(h16^{n_0+t}q-\ell t/d),\quad\sum_\ell|c_\ell|^2=1.}\tag{7}
\]

The last equality is finite Parseval. These are literal time-frequency *spectral lines* of a rational seed transform, not the unknown absolute spectrum of π. For q=1/17, d=2 and 

\[
(c_0,c_1)=\bigl(\cos(2\pi h/17),\ i\sin(2\pi h/17)\bigr).
\]

At q=1/5 the modulation is constant; q=1/7 has d=3, q=1/257 has d=4. No irrational seed is assigned a fictitious finite period.

## OSF-04 — clock-stratified, rational-seed-invariant spectral power (PROVED ALGEBRAIC)

For A≥max(d,n_0), let \(I_j=\{A\le n<2A:n\equiv n_0+j\pmod d\}\), \(N_j=|I_j|\), and \(C_j(h;s)=N_j^{-1}\sum_{n\in I_j}e(hU_n(s))\). Every stratum is nonempty when A≥d. Formula (2) and the period yield

\[
\boxed{C_j(h;s+q)=e(h16^{n_0+j}q)C_j(h;s),\quad
 \mathscr E_{A,d}(h;s):=\sum_j\frac{N_j}{A}|C_j(h;s)|^2
 =\mathscr E_{A,d}(h;s+q).}\tag{8}
\]

Hence \(|W_A(h;s)|^2\le\mathscr E_{A,d}(h;s)\) by Cauchy–Schwarz; the *invariant spectral power* is unchanged by the rational q, but the full complex Weyl mean generally is not. For each fixed rational q and h, this is an **exact finite-epoch theorem**, not an asymptotic prediction. As A varies, stages must remain time-labelled and the seed's preperiod must be paid.

**Classical Wall theorem (external input):** for any rational q, \(\alpha\) is normal to base 16 iff \(\alpha+q\) is. One proof uses the normal orbit's arithmetic-progression subsequences: every weak limit of the d residue-class orbit measures is invariant under x↦16^d x, and their average is Haar; ergodicity of Haar for 16^d forces every component to be Haar. The finite periodic translations then preserve Haar on each residue class. This proof needs normality of the *whole* orbit, not a superficial one-digit uniformity assertion. For the original BBP source, \(\alpha_s=s+\pi/16\), so **all rational seeds have the same base-16 normality verdict as s=0**, although that verdict remains OPEN. An arbitrary real seed can destroy it.

## OSF-05 — stratified digit spectra and exact new-line budget (CLASSICAL finite Fourier / SUCC Tesla-style valve)

For any finite cyclic digit record of length N, let \(p_k(w)\) be the frequency of each k-word w in \((\mathbb Z/16\mathbb Z)^k\), and \(\widehat p_k(\tau)=\sum_w p_k(w)e(\tau\cdot w/16)\). Then by finite-group Parseval,

\[
\boxed{E_k=16^k\sum_w\bigl(p_k(w)-16^{-k}\bigr)^2
=\sum_{\tau\ne0}|\widehat p_k(\tau)|^2.}\tag{9}
\]

Because cyclic empirical laws have exactly consistent marginals, \(p_k(w)=\sum_a p_{k+1}(wa)\). Completing the square gives

\[
\boxed{E_{k+1}-E_k
=16^{k+1}\sum_{w,a}\left(p_{k+1}(wa)-\frac{p_k(w)}{16}\right)^2\ge0.}\tag{10}
\]

This is the existing SUCC *digit refinement / Tesla-valve* grammar in spectral coordinates, not a novel entropy theorem. Each deeper word layer adds the square power of its newly resolvable Fourier lines. No finite depth is sufficient for normality.

**Exact hostile control:** the periodic cyclic digit word `0123456789abcdef` has E_1=0 and **E_2=15**, with the (1,−1) two-digit spectral character of modulus 1. It is simply normal, not normal to base 16. An equal one-digit spectrum does not authenticate a higher-layer source. The 32 certified finite digits of P have empirical cyclic E_1=25/32, E_2=17/2 and E_3=127; these are *small-sample diagnostics*, not asymptotic values or π-normality evidence. Cyclic counting is essential to make (10) exact without a boundary correction; linear-window samples have unequal denominators at successive word depths.

## OSF-06 — complete same-period source representation class is a vanishing coboundary (PROVED ALGEBRAIC)

Allow positive-time sources r,r' tending to 0, and whose weighted periods \(P(r),P(r')\) converge. For their **zero-seeded** states, the following are equivalent:

1. \(P(r')=P(r)\) exactly;
2. \(g_n=U_n^{r'}(0)-U_n^r(0)\to0\);
3. \(r'(n)-r(n)=g_n-16g_{n-1}\), with g_0=0 and g_n→0.

Proof: the difference recurrence gives the coboundary formula. Completing both sources gives \(g_n=16^n(P(r')-P(r))-[T_n(r')-T_n(r)]\). Both tails tend to 0 because the sources tend to 0; equality of periods implies g_n→0. Conversely telescope \(\sum_{n≤N}16^{-n}[g_n-16g_{n-1}]=16^{-N}g_N\to0\). For *every* fixed h,

\[
\boxed{|W_A^{r'}(h;0)-W_A^r(h;0)|\le
\frac{2\pi|h|}{A}\sum_{n=A}^{2A-1}|g_n|\to0.}\tag{11}
\]

This equivalence class is an exact source cohomology of the completed π invariant, not an assertion that every representative has the **original four-pole forcing**. A digit-only observer, even with **all digits of π**, cannot identify a unique forcing inside this class. SUCC's already-established rational-source/p-primary passport can distinguish distinct members when the source function class is fixed and local values are observed.

## OSF-07 — explicit positive odd-denominator same-π mutant and spectral separation (PROVED)

Choose the **unfitted exact rational** vanishing gauge

\[
\boxed{g_0=0,\quad g_n=\frac{n}{257(2n+1)^3}\ (n\ge1),\quad r'(n)=r(n)+g_n-16g_{n-1}.}\tag{12}
\]

Then \(r'(n)\in\mathbb Q_{>0}\) for every n≥1, and each r'(n) has **odd denominator**. Indeed, the authentic pole combination has an odd reduced denominator, as do both g terms. For n≥2, the exact original four-pole bound \(r(n)>15/(64n^2)\) and \((2n-1)\ge3n/2\) give

\[
16g_{n-1}<\frac{128}{27\cdot257\,n^2}<\frac{15}{64n^2}<r(n),
\]

while r'(1)=r(1)+g_1>0. The original bound follows directly by clearing denominators: its positive numerator is \(9664(n-1)^3+19336(n-1)^2+12770(n-1)+2783\) over an everywhere-positive positive-integer denominator. No numerical positivity check is needed.

The exact finite period discrepancy is

\[
\boxed{P_N(r')-P_N(r)=16^{-N}g_N\longrightarrow0.}\tag{13}
\]

So **P(r')=P(r)=π/16**, although r'≠r and its pole passport changes (already \(r'(1)-r(1)=1/6939=1/(27\cdot257)\), with a nonzero 257-primary circle component). Furthermore \(U_n^{r'}=U_n^r+g_n\), and \(0<g_n<1/(2056n^2)\). Consequently for every A≥1, every integer h,

\[
\boxed{|W_A^{r'}(h;0)-W_A^r(h;0)|<\frac{\pi|h|}{1028A^2}.}\tag{14}
\]

Thus **every** fixed h, and even every growing h_A=o(A²), has vanishing signed difference between the two sources. The mutant cannot change π normality, but its extra source poles are detected locally; it is NOT a new original-BBP source identity. This calibrates a source-class **σ** defect of purely digit-based fingerprinting.

### OSF-07b: a nonzero critical relative spectral line at h_A=2056A²

Set \(h_A=2056A^2\), and use the *relative-path* character, not an unknown absolute π phase:

\[
\boxed{D_A=\frac1A\sum_{n=A}^{2A-1}e(h_A[U_n^{r'}-U_n^r])
=\frac1A\sum_{n=A}^{2A-1}e\left(\frac{A^2}{n^2}\left(1+\frac1{2n}\right)^{-3}\right).}\tag{15}
\]

For all A≥24, \(\boxed{\operatorname{Re}D_A\le13/16}\), a **strict uniform contrast** proven with rational inequalities and a basic cosine bound: there are at least A/8 integers with \(4A/3\le n\le3A/2\). For them the exact phase argument lies in [3/8,5/8], where \(\cos(2\pi t)\le-1/2\). Outside them the cosine is at most 1; therefore the mean is at most \(1-(3/2)(1/8)=13/16\). The phase interval follows from \((1+u)^{-3}\ge1-3u\) and A≥24.

Also, with \(D_\infty=\int_1^2e(1/x^2)\,dx\), the explicit **all-A** rate is

\[
\boxed{|D_A-D_\infty|\le\frac{5\pi}{A}.}\tag{16}
\]

Indeed replacing the finite phase by \((A/n)^2\) costs at most 3π/A; the left Riemann sum for \(e(1/x^2)\) has Lipschitz constant ≤4π and costs ≤2π/A. Hence \(\operatorname{Re}D_\infty\le13/16<1\), without numerical quadrature. At fixed h the relative phase tends instead to 1, with uniform difference O_h(A^-2). **This is a mathematically decisive spectral-resolution threshold on a controlled source mutant, not a new signed estimate on the original π orbit.**

## OSF-08 — why the stratified fingerprint still does not prove normality (PROVED BOUNDARY / OPEN)

- A genuinely unmarked real seed has no invariant nonconstant absolute circle character under *all* real translations: the action of R/Z is transitive. Source/origin *relative* information is what can be invariant.
- A finite digit prefix defines a nontrivial base-16 cylinder of width 16^-k. It contains continuum-many possible completed seeds and both rational nonnormal completions and normal completions. Thus no finite digit prefix, even when certified by the source, proves π normality. Inside a **finite, externally bounded source candidate class**, sufficiently deep digits can distinguish distinct completed constants; if two source models share P, no number of digits of P alone distinguishes them.
- For the same-π mutant with phase shift \(g_n=O(A^{-2})\), fixed-depth digit cells agree except at observations within O(A^-2) of their boundaries. To infer that a *growing-depth* digit word is preserved, one needs a source-selected boundary-hotspot bound. None is derived by OSF-01…07. The critical digit resolution is \(k\approx2\log_{16}A\), where the cell width is comparable with \(g_n\). This is a discriminating **probe target**, not a statement that actual π digits differ at positive density.
- The genuine #554 three-channel prime-phase Gram and #544 signed chronology remain mathematically separate from this Archimedean relative spectroscope. Independent source-fingerprint identification and complete observer reconstruction do not imply the real signed covariance \(R_{A,h}(H_A)\to0\).

**π base-16 normality: OPEN. RH: OPEN.**
