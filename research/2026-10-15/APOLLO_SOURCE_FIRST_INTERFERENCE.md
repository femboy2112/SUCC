# APOLLO — Source-first determinacy, forced Brownian correction, and phase-sensitive prime births

**Research checkpoint:** October 15, 2026. **Branch:** research/apollo-prime-interference-source-determinacy-2026-10-15, born at PR #117 head \`a7a5cd92ce004e1f689fddd9268ed9a04a40d5eb\`. Ancestors: original APOLLO #110 source K1–K7, DYSPON I #112, Tate completed eta #114, original Suzuki high/Schur #116, source-field calculus #117, and frozen original Suzuki PR85 blob. **Main and the separate RH repository untouched. RH PROVED: NO.** Classical Hilbert-space identities and discrete shifts credited; scholarly priority of this combination not established.

## 0. The author's hypotheses, not silently repaired

1. The existing positive Hilbert channel may "actualize first"; the Brownian channel then accounts for what the positive channel pins down, leaving **no genuinely independent degrees of freedom**.
2. Prime births might create negative energy wells below/inside Brownian; those wells might be what "drives" the prime jets.

Our strongest operational reading does NOT assume physical time order: **construct a positive source feature first, and ask whether the source Brownian correction can be reconstructed uniquely from it**. Separately test whether the prime contribution is genuinely nonpositive (a one-sign well) or an indefinite phase-sensitive interaction. Distinguish full original Weil sign from a single prime component.

**Result (in brief):** Brownian correction is uniquely SOURCE-NEUTRAL for each prime in APOLLO's K1 difference factorization. A compact-window positive prime-difference feature determines its Brownian input by finitely many shifts at EVERY finite window, not only before a birth. More strongly the first true real Gamma-positive feature is injective and provides a bounded deterministic whole-negative feature graph on each finite window. None of this proves that graph is CONTRACTIVE. The prime-only signed form has BOTH positive and negative directions: real phase/interference, not an always-negative energy well.

## 1. SOURCE-EXACT mathematical object (API-01)

The original APOLLO source has for each genuine n=p^k:

\[
b=\log n,\quad w=\frac{\log p}{\sqrt n},\quad
B(x,y)=\frac{|x|+|y|-|x-y|}{2},
\]

and the triangular centered kernel \(E_b(x,y)=T_b(x-y)-T_b(x)-T_b(y)+1\), where \(T_b(t)=(1-|t|/b)_+\). APOLLO K1 is the exact signed identity

\[
\boxed{K_{\mathrm{prime},b}
=w\,bE_b-2w\,B.}\tag{API-01}
\]

This does NOT assert that either term is the complete original completed Weil form. Full \(K_g\) retains original real Gamma, polar signs, the independent \(C_\infty\) Archimedean Brownian contact, and every genuinely active prime power. Do not separate infinitely many inactive primes into individually divergent Brownian and triangular channels.

Let \(I=(-a,a)\), \(v\in L^2(I)\) with zero extension to \(\mathbb R\); one may take \(v=\sum_i z_i I_{x_i}\) as the dense oriented-Brownian indicator span. Define \(S_bv(t)=v(t-b)\). The normalized interval feature of \(E_b\) is exactly

\[
\phi_{b,x}(t)=b^{-1/2}\left[I_x(t-b)-I_x(t)\right].
\]

Consequently, by elementary Hilbert-space algebra,

\[
\boxed{\begin{aligned}
bE_b(v)&=\|(S_b-I)v\|_2^2,\\
B(v)&=\|v\|_2^2,\\
Q_{\mathrm{prime},b}(v)&=
w\|(S_b-I)v\|_2^2-2w\|v\|_2^2\\
&=-2w\,\mathrm{Re}\,\langle v,S_bv\rangle.
\end{aligned}}\tag{API-02}
\]

The extra Brownian term is not random noise: it removes precisely the two self-energies \(\|S_bv\|^2+\|v\|^2=2\|v\|^2\). What survives is a directed prime-clock autocorrelation. Algebraically, these two channels are generated from THE SAME \(v\); independent Brownian randomness is an optional probabilistic representation, not an intrinsic datum of this exact kernel.

**First falsifier:** set \(a=1/2,b=3/4,w=1\). Two rational nonoverlapping interval pulses a distance b apart, with equal phase, give Q=-1 after L² normalization; change one sign and Q=+1; rotate one phase by \(i\) and Q=0. This is exact continuum L² integration, not a finite matrix approximation. A one-sign "all negative prime well" conjecture is REFUTED. The surviving phase-sensitive interpretation is meaningful.

## 2. API-03 — The Brownian coefficient is forced by pre-wavefront neutrality (PROVED EXACT)

If \(b\ge2a\), \(I\cap(I+b)\) has Lebesgue measure zero. Hence for every v∈L²(I),

\[
\|S_bv-v\|_2^2=2\|v\|_2^2.
\]

For ANY attempted Brownian subtraction \(cw\|v\|_2^2\) attached to this exact difference feature,

\[
w\|S_bv-v\|^2-cw\|v\|^2=(2-c)w\|v\|^2.
\]

As there are nonzero v, no pre-wavefront prime interaction exists for ALL v **if and only if**

\[
\boxed{c=2.}\tag{API-03}
\]

Thus Brownian is a **forced source correction**, given this specific positive prime-difference factorization and genuine onset law. Mutating c=1 or c=3 invents nonzero prime energy on an observation interval where the true prime source must be completely inactive; an exact-rational mutation exposes it. Other mathematically equivalent Krein factorizations of a fixed signed kernel are not claimed unique.

For \(b>2a\), the map \(U_{b,a}:v\mapsto(S_b-I)v/\sqrt2\) is itself a true isometry on L²(I); the PLUS prime feature and the Brownian negative feature have equal Gram, and their minimal spans are canonically isometric through \(U_{b,a}^*\) restricted to the appropriate range. This is an **unconditional constructive gluing result on the old observation window**. It does not extend unchanged to the prime-active interval.

## 3. API-04 — Positive prime features reconstruct the Brownian input at EVERY finite a (PROVED EXACT)

The preceding isometry can fail when the clock's translated support overlaps I. But **injective determinacy survives**.

For any fixed finite \(a>0,b>0\), define

\[
F_b=(S_b-I)v,\quad m=\left\lfloor\frac{2a}{b}\right\rfloor.
\]

The telescoping identity \(\sum_{k=0}^m S_b^k(S_b-I)=S_b^{m+1}-I\), together with \((m+1)b>2a\), proves for almost every \(x\in I\),

\[
\boxed{
v(x)=-\sum_{k=0}^m F_b(x-kb).
}\tag{API-04}
\]

This is a **FINITE** exact inverse reconstruction in the source-window carrier, not a formal inverse \((S_b-I)^{-1}\) asserted on unrestricted L²(\(\mathbb R\)). Translations preserve the ambient L² norm, so

\[
\boxed{\|v\|_2\le(m+1)\|F_b\|_2.}\tag{API-04b}
\]

In particular, the Brownian input is uniquely determined by the positive PRIME-DIFFERENCE feature even after source birth. The inversion cost grows with a/b and need not be uniform as a→∞ or b→0. **Identity/reconstruction is not energy domination**: the positive feature can have lower energy than the forced Brownian subtraction in coherent configurations.

**Field-classification boundary:** API-04 is a finite symbolic inverse with finitely many shifts at fixed a,b, but its positive input F remains an arbitrary L2 function with potentially infinite source information. Injectivity/reconstructibility of the mathematical source map does not grant a physical or bounded observer finite access to all values of F. In SUCC this resolves a pathway/identity claim, not automatically a SimpleField resource or an all-RH positivity proof.

The code \`source_first_prime_interference\` proves this pointwise-a.e. on the FULL rational piecewise-constant continuum model by partitioning at every breakpoint of the source and its finite shifted copies. It also computes exact positive energy, Brownian correction, and phase correlation with disjoint complex-rational coefficients; no sampled quadrature is promoted to universal proof.

## 4. API-05 — EVEN THE COMPLETE SOURCE NEGATIVE CHANNEL is a unique bounded graph of positive features (PROVED ANALYTIC)

This is the strongest response to "there really aren't any unpinned degrees of freedom."

For every finite \(a>0\), the true APOLLO K2 factorization has source-positive energy

\[
E_+(v)
=\sum_{j\ge0}\beta_j\langle v,(I-R_{\alpha_j})v\rangle
+8|\langle v,s'\rangle|^2
+\sum_{n\in P_a}w_n\|(S_{b_n}-I)v\|^2,
\]
where \(\alpha_j=(4j+1)/2,\ \beta_j=4/(4j+1)\), \(s'(t)=\cosh(t/2)/2\), and \(R_\alpha\) convolves with \(\frac\alpha2e^{-\alpha|t|}\).

The negative feature energy is

\[
E_-(v)=
\left(C_\infty+2\sum_{n\in P_a}w_n\right)\|v\|^2
+8|\langle v,h'\rangle|^2,\qquad h'(t)=\sinh(t/2)/2.
\]

The single FIRST genuine real Gamma rung is already uniformly coercive on the declared finite observation window. Its restricted Schur kernel integral is maximal at t=0, so

\[
\|1_I R_{1/2}1_I\|_{2\to2}
\le1-e^{-a/2}
\]
and therefore

\[
\boxed{
E_+(v)\ge4\langle v,(I-R_{1/2})v\rangle
\ge4e^{-a/2}\|v\|^2.
}\tag{API-05a}
\]

Meanwhile Cauchy–Schwarz and the exact pole integral give

\[
8|\langle v,h'\rangle|^2
\le2(\sinh a-a)\|v\|^2,
\]
hence

\[
\boxed{
E_-(v)\le M_-(a)\|v\|^2,\qquad
M_-(a)=C_\infty+2\sum_{n\in P_a}w_n+2(\sinh a-a)<\infty.
}\tag{API-05b}
\]

Let \(\Phi_+\) and \(\Phi_-\) be the *actual source-derived minimal Hilbert feature maps* of these two positive forms. Because API-05a makes \(\Phi_+\) injective, the rule

\[
\boxed{
T_a\Phi_+(v)=\Phi_-(v)
}\tag{API-05c}
\]

is **UNCONDITIONALLY** well defined on the positive-feature span, extends uniquely as a bounded graph map, and satisfies

\[
\boxed{
\|T_a\|^2\le\frac{M_-(a)}{4e^{-a/2}}.
}\tag{API-05d}
\]

Thus every component of the FULL negative Brownian/contact/polar source, as a deterministic mathematical feature, is uniquely fixed by the complete positive source v on each finite window. This eliminates an alleged *independent kernel/nullspace freedom* in this particular K2 realization.

**THE REMAINING WALL:** \(\|T_a\|\le1\) is **NOT** established by existence or boundedness; it is APOLLO K4's actual completed-Weil positivity criterion, RH-equivalent over all a. A real negative source contribution can be fully determined and still overpower the positive energy. The genuine independent Archimedean contact coefficient \(C_\infty\) is SOURCE DATA and is not deduced merely from the prime-difference map. Nor does this algebra prove a physical chronology in which Gamma appears before Brownian.

The executable \`authentic_full_negative_feature_transfer_bound\` on rational \(0<a\le2\) retains every true active \(\Lambda(n)/\sqrt n\) coefficient via pinned rational intervals, both original poles, one real Gamma and the source contact. It gives a conservative exact rational norm upper, normally greater than one; it does **not** manufacture a contraction.

## 5. API-06 — Prime birth is an INDEFINITE interaction with source-defined derivative jets

For \(a<b<2a\), the source-anchored two-point restriction to \(\{a,-a\}\) is

\[
K_{\mathrm{prime}}=
w\begin{pmatrix}0&2a-b\\2a-b&0\end{pmatrix}.
\]

Its eigenvalues are \(\pm w(2a-b)\), so it is mathematically **indefinite**. There is a negative trough only in a phase-aligned direction; the complementary antiphase direction is positive. This exactly refutes a prime birth interpreted as a strictly negative-semidefinite "energy well".

In the derivative-coordinate real clock \(t\), the genuine source piece \(g_b(t)=w(|t|-b)_+\) has the distributional derivatives

\[
g_b''(t)=w(\delta_{b}+\delta_{-b}),\qquad
g_b'''(t)=w(\delta_b'+\delta_{-b}').
\tag{API-06}
\]

APOLLO K3 yields the **negative** signed Weil source impulses \(-w(\delta_b+\delta_{-b})\) after taking the correct mixed derivatives and prime/Brownian contact cancellation. Thus the prime "jet" is a source-defined wavefront/impulse of the arithmetic clock, not evidence that a negative physical potential causally accelerated some object. A legitimate SUCC causal model would have to DECLARE its evolving state, generator and allowed energy conversion first.

### The genuine \(\log2\) triple discrimination

Take any nonzero smooth \(\phi\) supported on \(J=(-31/64,-29/64)\) and \(b=\log2\). All three are genuine compact Weil-domain functions on \(a=1/2\):

\[
v_+=\phi+S_b\phi,\qquad
v_-=\phi-S_b\phi,\qquad
v_i=\phi+iS_b\phi.
\]

With source-true \(w_2=\log2/\sqrt2\), their **prime-only** Rayleigh values are respectively

\[
\boxed{
\frac{Q_2(v_+)}{\|v_+\|^2}=-w_2,\quad
\frac{Q_2(v_-)}{\|v_-\|^2}=+w_2,\quad
\frac{Q_2(v_i)}{\|v_i\|^2}=0.
}\tag{API-06b}
\]



**Completed source control (pre-existing DYS-04):** Each of the three genuine prime-2 phase tests has support measure at most 1/16 on a=1/2. Thus independently proved authentic completed Weil sparse positivity gives Q_zeta(v)>||v||²/24 for all three classes, including the in-phase class whose prime-only energy is negative. The 1/24 is a conservative inequality threshold, not a canonical eta normalization. This proves compensation on the declared restricted smooth-test family, NOT original all-window positivity or RH.
These signs follow symbolically from support geometry and source-pinned outward rational \(\log2\) bounds, not from numerically fitting zeta zeros. The same genuine prime impulse is present in all three; phase determines the quadratic sign. The FULL completed Weil form adds Gamma, contact, poles and other active primes (at a=1/2 only the true n=2 prime). No RH counterexample follows.

## 6. API-07 — Operator boundary at a prime birth: strong/weak information versus norm

Let \(a=1/2,\ b_m=1-m^{-2}\uparrow 2a\), \(m\ge2\), with \(\ell_m=1/(2m^2)\). Define two narrow rational cells \(J_m=(-a,-a+\ell_m)\) and \(J_m+b_m\subset I\) and

\[
v_{m,\pm}=m\bigl(1_{J_m}\pm1_{J_m+b_m}\bigr).
\]

These test vectors have **exact** L² norm 1 and, with synthetic rational weight \(w=1\), yield

\[
Q_{b_m}(v_{m,+})=-1,\qquad
Q_{b_m}(v_{m,-})=+1
\]
for EVERY m, even though the signed operator on any fixed test converges strongly to zero when \(b_m\uparrow2a\). The source is moving: \(v_m\) concentrates near opposite interval boundaries as the birth threshold is approached.

This is the exact SUCC **probe-topology** distinction: finite fixed observations can see the impending interaction vanish, while the operator-norm worst phase stays order one. It is neither a mathematical negative RH witness nor an actual finite-time Zeno supertask. \`normalized_birth_boundary_wells\` certifies every rational test cell algebraically.

## 7. Honest TLICA/SUCC taxonomy, falsifiers and next verdict-changing probe

**Established in this branch:** the finite-window Brownian input is uniquely reconstructible from its positive prime difference; pre-wavefront Brownian subtraction coefficient 2 is source-forced; first real Gamma yields unconditional bounded negative-channel graph for the COMPLETE APOLLO source; prime interactions possess positive and negative phase directions; genuine prime jets are distributional source events, and their onset is strong-vs-operator-norm discontinuous.

**Not established:** that there is *literally no independent physical freedom* in nature; that a positive energy physically appears earlier in time than Brownian energy; a canonical ordering among ALL equivalent signed Hilbert factorizations; that every genuine prime creates a strictly negative well; that the bounded full negative graph has norm ≤1; or that RH is proved.

**Negative controls (pass/fail defined):**
- Mutate per-prime Brownian coefficient \(2\to3\): produces ghost old-window energy, FAIL correct source.
- Keep the true clock but rotate second bump by \(\pi\) or \(\pi/2\): predict positive/zero prime energy; FAIL a one-sign well hypothesis.
- Kill the real Gamma or replace \(4j+1\) by \(4j+3\): the complete source graph is no longer authenticated.
- Insert a fake primitive composite 6 or wrong \(\sqrt n\) half-density: fail original Euler/source identification.
- Permit negative feature along \(\ker\Phi_+\) in a synthetic rank-two Gram: no well-defined correction map, refuting naïve "Brownian lives in positive-null freedom".
- Add a TRUE source prime on an old carrier: paired nonzero positive/negative features remain isometric, but no all-window independent-nesting contraction is inferred.
- Demand \(\|T_a\|\le1\) for the actual completed kernel: **UNVERIFIED**, original low Schur \(A-R_0\) remains the honest RH-hard gate.

**Next computational/math campaign:**
1. Tie the explicit per-prime shift inverse and Gamma-source positive graph into PR #109/#116's *actual* low/high Neumann Schur form. Derive a **source-specific local cross-channel residual** \(C_U\) rather than generic \(\|g'\|\)-only norm; test the genuine first-prime 18×18 9+9 parity low sector.
2. Seek a lawful *paired gluing* across each real \(b_n=\log(p^k)\) that transports the graph \(T_a\), preserving original Gamma/contact and the full signed distribution. Prewavefront isometry is a base case; inside active wavefront a **contraction** must be derived from arithmetic, not assumed.
3. Distinguish a semantic/physical dynamics version from the spectral theorem by writing a genuine state evolution law in SUCC and showing what, if anything, the prime clock causes. Until then use "interference" instead of empirically unsupported negative-energy mechanics.
4. Independent holdouts: exact source p2 in-phase/antiphase/quadrature and additional p3/p² wavefront windows with preserved half-density, plus fake source and wrong-character controls.

**Artifacts:** \`observational_succ/apollo_source_first_interference.py\`, \`tests/test_apollo_source_first_interference.py\`, \`tests/test_apollo_source_first_authentic.py\`, frozen receipt/probe and Python 3.10/3.13 CI on this isolated branch. Parent APOLLO and genuine Tate source provenance remain mandatory regressions.

**RH PROVED: NO. Academic originality of the constructed source interface unverified.**
