# TATE REFLECTION DIODE — finite prime clocks, the real Gamma contact, and the half-density jet obstruction

**2026-10-15 · Research branch:** \`research/tate-central-reflection-prime-jet-2026-10-15\`, born from draft PR #122 exact \`bf1bb848cfc9076b954d530b7a4ce255a4d70d5f\`. Parent source lineage: Tate #103, ONE OBJECT #106/#109, APOLLO #110, DYSPON I #112, eta/Tate #114, true Suzuki high #116, field closure #117. Original zeta source blob imported SHA \`0cc8510b71d178fc79e8d410a86d8b6014cf9178\`. **No main edits, publication, external RH-repo changes, or nontrivial-zero construction inputs. RH OPEN.** All classical functional-equation, Tate, Euler and Gaussian ingredients credited; independent scholarly priority of integration UNVERIFIED.

## 0. Maintainer hypothesis, preserved and strengthened

Maintainer: the finite prime-place arithmetic currents and the actual Archimedean Gamma factor seem to couple through \(1-s\) in a particularly orderly way, perhaps where finite source-local successor processes become IdealHard under global observation. From the preceding APOLLO source-first theorem, Brownian contact is not a random pool of independent freedom: it is a source normalization against positive features, with a contraction criterion still RH-hard.

Our precise steelman:

> Find the exact LOCAL and GLOBAL reflection maps, identify the source derivative at the self-dual point \(s=1/2\), track the true \(\Lambda(p^k)/p^{k/2}\) jets with no counterfeit source, and determine which finite→global operation is actually lawful.

The surprise is an identity binding the APOLLO Brownian-contact coefficient to the central reflection derivative **AND** a sharp no-go to obtaining that derivative from the raw finite-prime product. A normally convergent high-jet reflection residual survives, leaving only explicitly identified low-jet/global-Poisson debt.

## 1. TRD-01: local ratios and Gamma are simultaneously unitary on the center line (CLASSICAL TATE)

Use exactly the original Tate zeta unramified source chart from \`observational_succ/tate_local_contract.unramified_ball_pair\`:
\[
Z_p(s,\mathbf1_{\mathbb Z_p})=\frac1{1-p^{-s}},
\qquad
Z_p(1-s,\widehat{\mathbf1_{\mathbb Z_p}})=\frac1{1-p^{s-1}},
\]
with \(\psi_p(x)=e^{2\pi i\{x\}_p}\), additive Haar \(\mathrm{vol}(\mathbb Z_p)=1\), and multiplicative Haar \(\mathrm{vol}^{\times}(\mathbb Z_p^\times)=1\).

**Convention** (load-bearing!): define the *forward-over-dual* local reflection ratio
\[
\boxed{
R_p(s):=\frac{Z_p(s)}{Z_p(1-s)}
=\frac{1-p^{s-1}}{1-p^{-s}}.
}\tag{TRD-01}
\]
This is the **INVERSE** of the local \(\gamma_p\) in the common convention \(\widehat{Z}_p(1-s)=\gamma_p(s)Z_p(s)\). A standard normalized local epsilon factor is 1 at unramified conductor-zero self-dual places, but **R_p is not that epsilon factor**, and infinitely multiplying unnormalized R_p has no a priori functional-equation justification.

On the critical line \(s=\frac12+it\), the numerator is the complex conjugate of the denominator:
\[
\boxed{|R_p(1/2+it)|=1,\qquad R_p(1/2)=1.}\tag{TRD-02}
\]

The corresponding unique real Archimedean Tate Gaussian Mellin factor is
\[
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),\qquad
R_\infty(s)=\frac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(1-s)}.
\]
Since \(\Gamma_{\mathbb R}(\overline{s})=\overline{\Gamma_{\mathbb R}(s)}\), \(|R_\infty(1/2+it)|=1\). This is precisely a set of local **phase** transport laws; modulus 1 alone is neither global phase convergence nor Weil positivity.

For actual primitive \(\chi_{-3}\) with conductor 3 and odd parity, the genuinely unramified component is
\[
R_{p,\chi}(s)=\frac{1-\chi(p)p^{s-1}}{1-\chi(p)p^{-s}}\quad(p\ne3).
\]
At p=2, \(\chi_{-3}(2)=-1\), so its central phase slope has the opposite sign from zeta. At p=3 the character is RAMIFIED: applying an unramified formula there would fabricate a local place. The full twisted functional equation also needs its conductor, Gauss phase and \(\Gamma_{\mathbb R}(s+1)\), not the zeta even Gamma.

## 2. TRD-02: ALL local center values are 1, but their first derivatives reveal authentic prime jets (PROVED EXACT)

Differentiate (TRD-01). With \(A=p^{s-1}\), \(B=p^{-s}\),
\[
\frac{d}{ds}\log R_p(s)
=-\log p\left(\frac{A}{1-A}+\frac{B}{1-B}\right).
\]
At the reflection fixed point:
\[
\boxed{
R_p(1/2)=1,\quad
\left.\frac{d}{ds}\log R_p(s)\right|_{1/2}
=-\frac{2\log p}{\sqrt p-1}
=-2\sum_{k\ge1}\frac{\log p}{p^{k/2}}.
}\tag{TRD-03}
\]

These are **exactly** the true SUCC/FUCC/Suzuki half-density prime-power jet weights
\[
\boxed{
w_{p^k}=\frac{\Lambda(p^k)}{\sqrt{p^k}}
=\frac{\log p}{p^{k/2}}.
}\tag{TRD-04}
\]

This is not an analogy: the actual derivative of Tate's local forward/dual REFLECTION produces the same authenticated arithmetic impulse labels and coefficients already built into APOLLO's signed Weil distribution and SUCC's \(B_{\mathrm{jet}}^*B_{\mathrm{jet}}\). The factors of 2 arise from differentiating two reflected local channels. In the local reflection logarithm, the k-th power carries \(1/k\), and the Mellin derivative multiplies by k and \(\log p\), cancelling the 1/k exactly.

The fixed-point *value only* is an **observer/probe gap**: \(R_p(1/2)=1\) for all genuine unramified real \(\omega=\pm1\). But the FIRST JET distinguishes the true twisted \(\omega=-1\):
\[
\boxed{
\left.\partial_s\log R_{p,\omega}(s)\right|_{1/2}
=-\frac{2\omega\log p}{\sqrt p-\omega}.
}\tag{TRD-05}
\]
Thus the original zeta local slope is NEGATIVE, while the true \(\chi_{-3}\) unramified p=2 slope is POSITIVE. Exact-rational outward intervals in \`tate_central_reflection.py\` use immutable original \(\log p\) and \(p^{-1/2}\) source evaluators; no irrational is guessed from floats.

**RH caution:** \(\delta\) or \(\delta'\) prime "jets" in Suzuki are distributional wavefronts at \(\log p^k\), not the derivative in an evolving physical time of a negative energy well. The relation TRD-03 is Mellin/functional equation calculus, not a causal equation of motion.

## 3. TRD-03: completed zeta pins the SAME original Brownian contact as the 1-s central one-jet (CLASSICAL + SOURCE-IDENTIFIED)

Take the unmodified Tate completed zeta with its REAL Gamma factor:
\[
\boxed{
\Lambda(s)=\Gamma_{\mathbb R}(s)\zeta(s),\qquad
\Lambda(s)=\Lambda(1-s).
}\tag{TRD-06}
\]

Its original APOLLO/Suzuki Brownian contact is (pinned PR85 source)
\[
\boxed{
C_\infty=-\psi(1/4)+\log\pi
=\gamma+\frac\pi2+3\log2+\log\pi.
}\tag{TRD-07}
\]
Here \(\psi\) is the digamma function, not the Tate additive character.

As a **zero-independent** premise, \(\zeta(1/2)\ne0\) follows from \(\eta(s)=\sum_{n\ge1}(-1)^{n-1}/n^s>0\) on real \(s>0\), and \(\zeta(s)=\eta(s)/(1-2^{1-s})<0\) for \(0<s<1\). Differentiate the true completed functional equation at its fixed point: \(\Lambda'(1/2)=0\). But
\[
\frac{\Gamma_{\mathbb R}'}{\Gamma_{\mathbb R}}(s)
=-\frac12\log\pi+\frac12\psi(s/2).
\]
Consequently
\[
\boxed{
\frac{\zeta'}{\zeta}(1/2)
=-\frac{\Gamma_{\mathbb R}'}{\Gamma_{\mathbb R}}(1/2)
=\frac{C_\infty}{2}.
}\tag{TRD-08}
\]
Equivalently the source-global reflection slopes are
\[
\boxed{
(\log R_\infty)'(1/2)=-C_\infty,\qquad
\left[\log\frac{\zeta(s)}{\zeta(1-s)}\right]'_{s=1/2}=+C_\infty.
}\tag{TRD-09}
\]

**This is the key newly surfaced SUCC connection:** The same ORIGINAL normalized scalar \(C_\infty\) that appears as the negative Brownian contact in the APOLLO signed kernel is precisely the central reflection jet required by the completed zeta's real Gamma. It is not a free energy reservoir and not an arbitrary regulator fitted to a calculation. However, identifying this scalar does NOT prove that the original Brownian operator is dominated by the positive Gamma/prime source on all admissible tests.

## 4. TRD-04: the naive all-prime reflection inverse limit is a DIODE, not analytic completion (PROVED / classical Euler divergence)

For a finite true-prime cutoff P define
\[
R_{\le P}(s)=\prod_{p\le P}\frac{1-p^{s-1}}{1-p^{-s}}.
\]
Every finite prime stage satisfies \(R_{\le P}(1/2)=1\), exactly. Yet
\[
\boxed{
(\log R_{\le P})'(1/2)
=-2\sum_{p\le P}\frac{\log p}{\sqrt p-1}
\xrightarrow[P\to\infty]{}-\infty.
}\tag{TRD-10}
\]
This divergence follows from classical \(\sum_p p^{-1}=\infty\): for p≥2, \(\log p/(\sqrt p-1)\ge(\log2)/p\). No finite sample alone proves the all-prime divergence; it is an imported elementary number-theoretic theorem.

The obstruction is stronger than a divergent derivative. For real \(0<\sigma<1\),
\[
\boxed{
\lim_{P\to\infty}R_{\le P}(\sigma)=
\begin{cases}
+\infty &0<\sigma<1/2,\\
1&\sigma=1/2,\\
0&1/2<\sigma<1.
\end{cases}
}\tag{TRD-11}
\]

Proof on the right half: for \(\sigma>1/2\), \(A_p=p^{-(1-\sigma)}>B_p=p^{-\sigma}\), so \(0<R_p<1\). Also \(-\log R_p=\int_{B_p}^{A_p}\frac{dt}{1-t}\ge A_p-B_p\). Since \(A_p-B_p=p^{-(1-\sigma)}(1-p^{-(2\sigma-1)})\), its sum diverges by comparison with \(\sum_p1/p\). On the left the reciprocal relation \(R_p(1-\sigma)=R_p(\sigma)^{-1}\) yields +∞.

**Gamma cannot fix this raw product by pointwise multiplication:** \(\Gamma_{\mathbb R}(\sigma)/\Gamma_{\mathbb R}(1-\sigma)\) is nonzero/finite throughout \(0<\sigma<1\). Multiplying it by 0 or +∞ does not produce the meromorphic analytic \(\zeta(\sigma)/\zeta(1-\sigma)\), which is finite and positive throughout the same real strip. The two half-plane Euler products for \(\zeta(s)\) and \(\zeta(1-s)\) have **no common domain of absolute convergence**. The local functional equations, correctly normalized adeles, and **global Poisson summation** construct analytic completion through a DIFFERENT, lawful operation—not the ordinary inverse limit of these ratios.

At the center, stage values converge *trivially* to 1 but their derivatives diverge. Hence there is no locally uniform holomorphic convergence of raw \(R_{\le P}\) near \(s=1/2\) to the analytic global ratio. This is a rigorous source-specific SimpleField/IdealHard-type **representation obstruction**, not a proof that completed zeta or RH is mathematically uncomputable. In fact Tate's theta Poisson construction gives a finitely stated global analytic identity. The RH-hard missing arrow remains **signed Weil positivity**.

## 5. TRD-05: remove FINITELY MANY low prime jets, and the remaining reflection product IS analytic and computable (PROVED)

The formal exact expansion for each original unramified prime is
\[
\boxed{
\log R_p(s)
=\sum_{k\ge1}\frac{p^{-ks}-p^{-k(1-s)}}{k},
\qquad 0<\Re s<1.
}\tag{TRD-12}
\]
For integer \(N\ge7\), remove the FIRST N prime-power counterterms at EACH genuine place:
\[
C_{p,N}(s)=\sum_{k=1}^N
\frac{p^{-ks}-p^{-k(1-s)}}{k}.
\]

The high-jet product
\[
\boxed{
H_N(s)=\exp\left(
\sum_{p}\sum_{k>N}
\frac{p^{-ks}-p^{-k(1-s)}}{k}
\right)
}\tag{TRD-13}
\]
is an **absolutely and normally convergent**, nonzero holomorphic function on the closed vertical strip \(1/4\le\Re s\le3/4\) (indeed on a small open neighborhood, since \((N+1)/4\ge2>1\)). It retains exact reflection and unitary center properties
\[
\boxed{
H_N(1-s)=H_N(s)^{-1},\qquad
|H_N(1/2+it)|=1,\quad H_N(1/2)=1.
}\tag{TRD-14}
\]

**A completely rational, all-heights analytic remainder certificate:** For integer P≥16, any N≥7, every s in that strip,
\[
\boxed{
\left|
\log H_N(s)-
\sum_{p\le P}\sum_{k>N}
\frac{p^{-ks}-p^{-k(1-s)}}{k}
\right|
\le\frac1{2P}.
}\tag{TRD-15}
\]
Indeed \(p^{-1/4}\le1/2\) for p≥16 and for k≥8,
\[
\sum_{k\ge8}\frac{2p^{-k/4}}k
\le\frac14\,\frac{p^{-2}}{1-p^{-1/4}}
\le\frac12p^{-2}.
\]
Summing actual primes p>P is bounded by summing all integers n>P, yielding \(\frac12\sum_{n>P}n^{-2}\le1/(2P)\). **Composite n in the estimate is only a numerical majorant, never a fake arithmetic place.** Both the analytic normal convergence and the tail bound work for ALL imaginary heights at once.

This is an effective, source-true, high-prime-jet reflection carrier. It is NOT \(\zeta(s)/\zeta(1-s)\). The removed low powers k≤N have individually divergent all-prime sums near the critical line, and defining their lawful global analytic continuation is a separate mathematical obligation. Positivity of the completed signed Weil form remains another separate obligation.

### Sharper distinction right at s=1/2: only the FIRST TWO jet powers diverge

By differentiating (TRD-12) and setting s=1/2,
\[
(\log R_p)'(1/2)
=-2\sum_{k\ge1}\frac{\Lambda(p^k)}{\sqrt{p^k}}.
\]
But the high powers k≥3 satisfy the ABSOLUTELY CONVERGENT source identity
\[
\boxed{
J_{\ge3}=\sum_p\sum_{k\ge3}\frac{\log p}{p^{k/2}}
=\sum_p\frac{(\log p)p^{-3/2}}{1-p^{-1/2}}
<\infty.
}\tag{TRD-16}
\]
By contrast, k=1 and k=2 both diverge upon summing over genuine primes, by \(\sum_p1/p=\infty\). Thus at the **center first derivative**, the only non-absolutely-summable prime-power layers are the first and second. For a WHOLE strip 1/4≤Re s≤3/4, our safe uniform analytic bound uses k≥8 instead. Keep these two very different quantifiers distinct.

Define, using the already proven analytic zeta continuation,
\[
\mathcal L_N(s):=
\frac{\zeta(s)/\zeta(1-s)}{H_N(s)}.
\]
At center where all terms are nonzero,
\[
\boxed{
(\log\mathcal L_2)'(1/2)
=C_\infty+2J_{\ge3}.
}\tag{TRD-17}
\]

**CAUTION:** \(\mathcal L_2\) is DEFINED USING THE GLOBAL COMPLETED ZETA. Equation TRD-17 is a valid *identification of what the low-jet transducer must reproduce*, not an independent source-only construction of that missing transducer or proof of sign. It should be used as a target/negative-control oracle, not inserted as an RH proof premise.

## 6. TRD-06: theta reflection FIXES a quarter-density in heat time, and 1/2 in Dirichlet time (CLASSICAL / SOURCE NORMALIZATION)

Recall \(\Theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t}\), with true self-dual Poisson
\[
\boxed{\Theta(t)=t^{-1/2}\Theta(1/t).}\tag{TRD-18}
\]

Put \(t=e^x\), and define a family of possible centered source charts \(H_w(x)=e^{wx}\Theta(e^x)\). Then
\[
\frac{H_w(-x)}{H_w(x)}
=e^{(1/2-2w)x}.
\]
Consequently
\[
\boxed{H_w(x)=H_w(-x)\ \forall x\iff w=1/4.}\tag{TRD-19}
\]

This **canonical 1/4** is the log-HEAT normalization needed to turn Poisson inversion into reflection \(x\mapsto-x\). The corresponding multiplicative zeta Mellin source reflects \(s\leftrightarrow1-s\) around **s=1/2**, yielding \(p^{-k/2}\) when the Euler/Dirichlet source is evaluated at the center. Different coordinates, related original source; do not identify the numerical fractions without the theta/Mellin map.

At the self-dual heat clock x=0, ALL w give ratio 1, but the first derivative of its log is \(1/2-2w\), uniquely determining w=1/4. This is another genuine source-indexed **observer probe-gap repair**, analogous to the DYSPON eta modular 1/24 story but with a different canonical exponent.

## 7. TRD-07: a hostile reflection-symmetric NON-EULER mutant destroys the false RH implication (PROVED EXACT)

Reflection, Gamma, canonical center and even the FULL polar residues cannot force RH by themselves. For any positive integer m define the exact polynomial
\[
\boxed{
M_m(s)=1+\frac{16\cdot4^{2m}}3\,s(s-1)
\left(s-\frac12\right)^{2m}.
}\tag{TRD-20}
\]

It has properties, proved directly by rational algebra:
- \(M_m(1-s)=M_m(s)\) (reflection);
- \(M_m(0)=M_m(1)=M_m(1/2)=1\) (same pole residues of the underlying completed \(\Lambda\), unchanged central value);
- derivatives \(M_m^{(j)}(1/2)=0\) for EVERY \(1\le j<2m\) (any arbitrarily long chosen finite center jet);
- \(M_m(1/4)=M_m(3/4)=0\) (explicit OFF-CRITICAL-LINE zeros in the critical strip).

Thus \(\Lambda_{\mathrm{mut}}(s)=\Lambda(s)M_m(s)\) retains the same \(s\mapsto1-s\) functional equation, the SAME original real Gamma factor if we define \(\zeta_{\mathrm{mut}}(s)=\zeta(s)M_m(s)\), the SAME principal polar residues and arbitrary fixed finite central jet data, but deliberately **fails the original Euler multiplicativity law** and acquires off-line zeros. This is a countermodel to the implication

\[
\boxed{
\text{reflection + Gamma + pole data + finitely many center jets}\Rightarrow\mathrm{RH},
}
\]
NOT a counterexample to RH for actual zeta. The genuine prime-source data are a load-bearing additional constraint. A framework whose proofs treat \(\zeta_{\mathrm{mut}}\) as an admissible original prime source is invalid.

## 8. TRD-PARITY: the real reflection separates polar signs and admits a 15-dimensional first-prime low carrier (PROVED SOURCE ANALYTIC)

The full completed original Weil form on \(I=(-1/2,1/2)\), in its already authenticated log-clock \(L^2\) test coordinate \(f\), is

\[
Q_\zeta(f)=\sum_{j\ge0}\beta_j\langle f,(I-R_{\alpha_j})f\rangle
-C_\infty\|f\|^2
+2\Big|\int_I f\cosh(t/2)dt\Big|^2
-2\Big|\int_I f\sinh(t/2)dt\Big|^2
-w_2\langle f,(S_{\log2}+S_{-\log2})f\rangle.
\]

Here \(\alpha_j=(4j+1)/2\), \(\beta_j=4/(4j+1)\), \(w_2=\log2/\sqrt2\). Gamma OU, scalar contact and symmetric prime shifts **COMMUTE WITH PARITY** \(Jf(t)=f(-t)\). The cosh rank-one channel is even; the sinh rank-one channel is odd. Therefore the TRUE original completed signed source splits into even and odd quadratic subspaces with no mixed cross term.

In particular, for **even** \(f\), the entire negative polar sinh channel vanishes. We can improve the original unconditional negative source bound on that subspace to

\[
\boxed{
Q_\zeta(f)>
\left[m_J(\Omega)(1-\varepsilon_m(1/2,\Omega))
-\frac{47}{8}\right]\|f\|^2
}
\tag{TRD-P1}
\]
for even smooth f annihilating its first m power moments, where 47/8 = 43/8 contact +1/2 original true p2 prime-shift upper. Positive cosh pole remains a correct nonnegative contribution.

Choose the EXACT rational Fourier clock \(\Omega=217/20\), **256 TRUE original real Gamma modes** and \(m=14\). Source-tested Fraction arithmetic proves

\[
\boxed{Q_\zeta(f)>\frac1{140}\|f\|^2
\quad\text{for EVERY even smooth compact f with moments }0,\dots,13=0.}
\tag{TRD-P2}
\]

For **odd** f, the positive cosh polar term vanishes, while the genuine negative sinh pole remains. The already proven source Fourier result (PR #116, J=32, Omega=12) gives

\[
\boxed{Q_\zeta(f)>\frac1{20}\|f\|^2
\quad\text{for EVERY odd smooth compact f with moments }0,\dots,15=0.}
\tag{TRD-P3}
\]

**A source-faithful NONCONTIGUOUS low Legendre selector now appears.** In the original Suzuki derivative-coordinate carrier \(H=L^2_0(I)\), let \(f=Vu\) and \(K=V^*V=(-\Delta_N)^{-1}\). The primitive V reverses parity: odd u→even f, even u→odd f, with both boundary traces zero. Orthogonality against \(P_j(x/a)\) for j=1..m implies vanishing first m power moments of f (Legendre derivatives span the polynomial test space).

Therefore choose the **15-dimensional** low source space
\[
\boxed{
F_{15}^{\mathrm{ref}}=
\mathrm{span}\{P_1,P_2,\dots,P_{14},P_{16}\}
}
\tag{TRD-P4}
\]
with 7 odd-derivative modes \(P_1,P_3,\dots,P_{13}\) and 8 even-derivative modes \(P_2,P_4,\dots,P_{16}\). On its true high orthogonal complement:

- odd u has no \(P_1,P_3,\dots,P_{13}\) component; all EVEN P_j vanish automatically by parity. Its even primitive f annihilates first **14** moments and obeys TRD-P2.
- even u has no \(P_2,P_4,\dots,P_{16}\) component; all ODD P_j vanish automatically. Its odd primitive f annihilates first **16** moments and obeys TRD-P3.

Since the genuine signed original quadratic and the Neumann K metric both preserve parity, the two positive high bounds sum:

\[
\boxed{
Q_{15}^{\mathrm{ref}}GQ_{15}^{\mathrm{ref}}
\succeq\frac1{140}
Q_{15}^{\mathrm{ref}}KQ_{15}^{\mathrm{ref}}.
}
\tag{TRD-P5}
\]

This is a **genuine first-prime original-source 15-dimensional low Schur reduction**, split into 7+8 parity blocks. It is mathematically stronger as a *smaller-dimensional low description* than the earlier 16/18/30 cutoffs, but quantitatively MUCH weaker than PR #116's \(r=18,\kappa=1/16\). The inherited signed \(g'\) source norm <11/40 only gives the coarse zero-shift cross bound

\[
\boxed{0\preceq R_0\prec\frac{847}{80}I_{15}
\quad (\approx10.5875 I),}
\tag{TRD-P6}
\]
which is far too large to certify the source LOW signed Schur \(S_0=A-R_0\).

This exposes a real research tradeoff: one can reduce the low-sector dimension by exploiting \(s\leftrightarrow1-s\)-compatible reflection parity and its polar channel signs, but the spectral positivity **margin** can deteriorate and make residual shorting harder. The 15-dimensional source trial \(U\) would also need a new noncontiguous source projection; the rank-two K boundary-channel formula for the contiguous 30-dimensional split cannot be reused without rederivation. None of these results proves even first-window all-test positivity, let alone RH.

**Executable source certificate:** \`observational_succ/tate_reflection_parity_schur.py\`; exact tests \`tests/test_tate_reflection_parity_schur.py\`. The Γ/contact/p2 and original PR109 derivative sources are SHA checked, and the source claims carry no zero inputs.

## 9. Observer taxonomy and exactly what would move RH

**SimpleField aspects:** fixed local Tate rational charts, every declared unramified reflection ratio and finite source-prime tape, real theta Poisson/globally completed zeta by a finite mathematical functional equation, a certified high-prime-jet residual with \(1/(2P)\) truncation cost.

**IdealHard / source-toolkit-hard aspects:** ordinary ratio-products and naive central derivatives are genuinely nonconvergent, although every finite local stage is lawful; a new source-compatible global Poisson/analytic continuation map must change the representation. This is a proof of ONE failed inverse-limit route, not of absolute Turing noncomputability of the target. The full original Weil **sign** remains an unresolved independent low Schur/positive-feature contraction gate.

**FuckedField no-go for malformed sources:** fake primitive composite 6, omitted half-density, wrong \(\chi_{-3}\) conductor parity, ordinary raw local product claimed as analytic \(\zeta(s)/\zeta(1-s)\), non-Euler off-line symmetric mutant, or a purported global negative/positive Hilbert form deduced from unitary local phases. Such proposed proof ARROWS fail; the original zeta carrier is not proved impossible, phantom or undecidable.

The next genuinely proof-bearing candidate is a **source-first renormalized reflection low-jet transducer** that:
1. reads the ACTUAL first/second prime-power half-density currents and one real Gamma \(\Gamma_{\mathbb R}\) with both global poles;
2. produces the correct central contact \(C_\infty\) and the full original Weil distribution WITHOUT defining the unknown map by inserting \(\zeta\)-continuation as an oracle;
3. has explicit conductor/phase/normalization and analytic test-domain continuation (Tate Schwartz–Bruhat/adelic Poisson);
4. independently dominates the true negative Brownian/prime-polar features by the positive original source (K4 contraction) or certifies the actual zero-shift source Schur low form across every finite a.

Steps 1–3 are source-completion work, and Tate supplies the global functional equation already; step 4 is RH-hard. A finite original-source negative witness would also be decisive but requires severe independent audit. Finite “phase alignment” and reflection do not automatically imply spectral sign.

## Executable proof instruments and primary literature

- \`observational_succ/tate_central_reflection.py\`: SHA-pinned original real contact, p-local reflection and true prime jets, exact rational interval slopes, finite-prime phase sign, renormalized strip tail, source-type hostile mutants.
- \`tests/test_tate_central_reflection.py\`: independent exact arithmetic, genuine odd chi3 unramified negative control, false Euler 6, false infinite prime product, high-jet, central Brownian identity, theta gauge and infinitely extendable symmetric off-line mutant.
- \`scripts/tate_central_reflection_probe.py --verify\` and \`research/2026-10-15/TATE_CENTRAL_REFLECTION_RECEIPT.json\`: deterministic source-gated mathematical receipt. 
- \`.github/workflows/tate-central-reflection.yml\`: Python 3.10/3.13 original Tate/Suzuki, DYS, APOLLO, immutable source proof replays.
- **Primary classical Tate:** original thesis (1950; Cassels–Fröhlich 1967); Stephen Kudla, *Tate's Thesis*, local epsilons and global functional equation, https://www.math.columbia.edu/~avizeff/quals/Tate.pdf ; Tao, *Tate's proof of the functional equation*, https://terrytao.wordpress.com/wp-content/uploads/2009/01/whatsnew.pdf ; background source \`research/2026-10-14/TATE_SOURCE_FOURIER_CONDUCTOR_BRIDGE.md\`.
- **Weil/Suzuki:** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (2026); imported SUCC original source PR85, APOLLO PR110 and PR122. The physical "negative prime energy drives jets" metaphor has no identified causal generator in these sources.

**VERDICT:** The author's coupling intuition identifies a REAL, EXACT central contact/reflection identity and an original prime-power half-density jet law. A naive finite-prime inverse limit is rigorously WRONG; an analytic high-jet part exists with an explicit small remainder. The outstanding arithmetic low-jet/positivity transport is sharply localized but remains RH-hard. **RH PROVED: NO.**
