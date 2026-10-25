# Conservative boundary flux — finite error transport, hidden graph energy and source-typed limits

**2026-10-24; stacked on SUCC draft #285 at** \`f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad\`.
**Branch:** \`research/conservative-boundary-flux-2026-10-24\`.
**Author's conjectural motivation:** when reasoning crosses representations and limits, both sides should carry finite correction boundaries. Correlating the corrections may expose invariant information; a complicated graph should appear as a point when viewed externally. The word “energy” is literal **only** in a declared physical network model and mathematical for positive quadratic error forms.

**Relevant predecessors (do not promote their unresolved claims):** SUCC #285 generalized Euler–Adelic Boundary, source-faithful renormalization SFR-06, observer/Schur OS-01–07, hidden memory HM-01, #285's finite-source and fake-six controls. Classical precedents: Dörfler–Bullo, *Kron Reduction of Graphs with Applications to Electrical Networks*, IEEE TCAS I 60 (2013), DOI 10.1109/TCSI.2012.2215780, https://arxiv.org/abs/1102.2950 ; standard orthogonal projections/conditional expectation and RC network power balance. New contribution **relative to this repo** is the explicit two-ended flux interface, source-typed exact finite probes and their link to the authenticated EAB source. No independent scholarly priority claimed.

## I. A finite error *identity*, not two unrelated estimates

For real \(r>1\), write

\[
G(r)=\zeta(r)-\frac1{r-1},\quad
D_N(r)=\sum_{n=1}^Nn^{-r}-\int_1^Nx^{-r}dx,\quad
P_X(r)=\prod_{p\le X}(1-p^{-r})^{-1},
\]

with **genuine primes only** and integer \(1\le N\le X\), \(X\ge2\). Define

\[
\delta_N=D_N-G,\quad R_X=\zeta-P_X,\quad
C_{N,X}=D_N-\left(P_X-\frac1{r-1}\right).
\]

### CBF-01 (classical mathematics assembled into a source-typed bridge; paper proof)

\[
\boxed{C_{N,X}=\delta_N+R_X,\quad
0\le\delta_N\le\frac1{2N^r},\quad
0\le R_X\le\frac{X^{1-r}}{r-1}.}
\]

The **observable finite gap** is the sum of two nonnegative unknown errors. The finite SUCC readout is an upper bound and the finite FUCC readout a lower bound:

\[
\boxed{
\max\left(P_X-\frac1{r-1},D_N-\frac1{2N^r}\right)
\le G(r)\le
\min\left(D_N,P_X-\frac1{r-1}+\frac{X^{1-r}}{r-1}\right).
}
\]

**Proof.** Convex decreasing \(x^{-r}\) gives, cellwise,
\(0\le\int_n^{n+1}x^{-r}dx-(n+1)^{-r}
\le(n^{-r}-(n+1)^{-r})/2\).
Summing \(n\ge N\) and using the identity
\(D_N-G=\int_N^\infty x^{-r}dx-\sum_{n>N}n^{-r}\)
gives the \(\delta_N\) bound. The authentic finite Euler product expands into positive X-smooth integer terms and contains every \(n\le X\); its missing terms are a subset of \(n>X\), bounded by the integral tail. The gap identity is exact subtraction. All inequalities rely on **r real and >1**; do not silently transport them through analytic continuation or signed Weil kernels. QED.

**Finite rational example, \(r=2,N=4,X=5\):**

\[
D_4=\frac{97}{144},\quad P_5-\frac1{2-1}=\frac9{16},\quad
C_{4,5}=\frac19.
\]

There is no need to evaluate \(\pi\) or \(\zeta(2)\) to certify this gap. The exact one-sided caps are \(1/32\) and \(1/5\).

**Refutation control:** inserting composite 6 as an independent Euler factor into the \(p\le11\) product gives an adjusted purported lower bound **above** \(D_{11}(2)\), violating the true-source ordering. A structural flux ledger is not permitted to absorb fake sources by changing labels.

### CBF-02: monotone budget flux and the source square

For \(X'\ge X\) the unseen prime mass decreases exactly by the positive newly included smooth terms:

\[
R_X-R_{X'}=P_{X'}-P_X.
\]

For \(N'\ge N\), \(\delta_N-\delta_{N'}=D_N-D_{N'}\), a nonnegative sum of right-endpoint cell defects. The two cutoff operations are independent, so

\[
C_{N,X}-C_{N',X}-C_{N,X'}+C_{N',X'}=0.
\]

This zero mixed finite difference is a **flatness / consistency diagnostic**, not a magic detector of true primes: even a separable fake-source product has this property. Source-specific violations require separate controls.

### CBF-03: cofinal finite boundary at the zeta pole

Use the existing EAB schedule \(s_q=1+1/q\), \(X_q=q^{2q}\), integer \(q\ge2\), and take the SUCC cutoff \(N=q\). The previous theorem gives

\[
\boxed{
0\le D_q(s_q)-[P_{X_q}(s_q)-q]
\le \frac1{2q^{s_q}}+\frac1q
\le \frac{3}{2q}.
}
\]

Thus the **cross-domain finite observable gap vanishes with an explicit rate**, while both endpoints tend to Euler–Mascheroni gamma by the EAB continuation and cofinal product estimate. This certifies a legal pathway across the pole on **these declared cofinal cutoffs**. It is not a universal license to exchange limits.

## II. The exact two-domain error-transport theorem

Let \(H,K\) be Hilbert spaces, \(F:H\to K\) a bounded linear transport, \(P:H\to H\) a source projection and \(Q:K\to K\) a target projection. For \(x\in H\),

\[
\boxed{Fx-QFPx=(I-Q)Fx+QF(I-P)x.}
\]

The identity is algebraic and remains true for nonorthogonal idempotents. Put \(a=(I-Q)Fx\), \(b=QF(I-P)x\); the **exact** error-energy balance is

\[
\|Fx-QFPx\|^2=\|a\|^2+\|b\|^2+2\operatorname{Re}\langle a,b\rangle.
\]

If \(Q\) is orthogonal then \(a\perp b\) and **the interaction term vanishes**. Consequently

\[
\boxed{\|Fx-QFPx\|^2=\|(I-Q)Fx\|^2+\|QF(I-P)x\|^2.}
\]

This is CBF-04, a classical projection identity newly deployed as a two-domain SUCC boundary interface. For orthogonal Q, \(\|QF(I-P)x\|\le\|F\|\|(I-P)x\|\). If \(P_n\to I_H\), \(Q_m\to I_K\) strongly, then \(Q_mFP_nx\to Fx\) jointly as \(n,m\to\infty\) for every fixed x; **proof:** each squared residual term vanishes by the stated hypotheses and boundedness. A finite effective convergence algorithm additionally requires quantitative certified tail moduli. An unbounded F needs valid domains plus graph-norm rather than bare source-norm estimates.

**Exact hostile finite matrices:** source \(x=(1,2,3)\), F rows \((1,2,1),(0,1,1)\), P=diag(1,1,0), Q=diag(1,0). Then
\(Fx=(8,5)\), \(QFPx=(5,0)\), and \(34=25+9\) is an exact squared-error split. Change Q to the **oblique idempotent** \(\left(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\right)\). Then the two error pieces are \((-5,5)\) and \((6,0)\), and

\[
26=50+36-60.
\]

Dropping the negative cross term would falsely claim an error energy of 86 instead of 26. These are exact rational witnesses; no probabilistic interpretation is inferred from algebra alone.

## III. Complicated network as a boundary object (with exact hidden energy)

Let \(L=L^\top\) be the graph Laplacian of a finite connected undirected positive-conductance network, with visible ports B and nonempty interior I; assume every hidden component meets B, so \(D=L_{II}\) is positive definite. Let \(C=L_{BI}\), \(A=L_{BB}\), and \(L_{\rm eff}=A-CD^{-1}C^\top\).

For potentials \(u=(b,z)\), let \(z_*=-D^{-1}C^\top b\), interior current \(j_I=C^\top b+Dz=D(z-z_*)\), and boundary current \(j_B=Ab+Cz\).

### CBF-05 — energy and current correction (classical Schur/Kron theorem)

\[
\boxed{
u^\top Lu=b^\top L_{\rm eff}b+
(z-z_*)^\top D(z-z_*)
=b^\top L_{\rm eff}b+j_I^\top D^{-1}j_I.
}
\]

\[
\boxed{j_B-L_{\rm eff}b=CD^{-1}j_I.}
\]

**Proof:** complete the quadratic square in z, and substitute the interior-current equation. All identities are exact for any u; positivity of the hidden term uses **positive definite** D. Because Laplacian rows sum to zero, \(\sum j_B+\sum j_I=0\). At interior equilibrium j_I=0: the condensed network preserves its **static boundary energy and current** exactly. Away from equilibrium, the discarded interior does not disappear—it induces measurable boundary correction and positive hidden energy. **Only the external port observable, not every internal path/history, is preserved.**

**Three-node path \(0-1-2\)** with unit edges, B=(0,2), interior=1 and \(u=(1,0,0)\):
raw \(u^\top Lu=1\), effective energy \(1/2\), hidden energy \(1/2\), interior current \(-1\), and boundary correction \((1/2,1/2)\). All are exact rationals. Replacing u by the harmonic \((1,1/2,0)\) gives hidden energy and current correction **zero**.

**CBF-06 — nested coarse-graining associates** if the relevant interior blocks are invertible: eliminating disjoint interior regions sequentially or simultaneously gives the same final Schur complement, since both minimize the same strictly convex interior energy. The hidden corrections telescope without loss. In a four-node unit path, eliminating interior node 1 then node 2 gives \(L_{\rm eff}=\frac13\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\). For u=(1,2,0,0), raw energy 5, final energy 1/3, discarded energy 14/3. The sequential contributions are 9/2 and 1/6, whose sum is 14/3.

**CBF-07 — one-port/static no-go.** A connected ungrounded Laplacian reduced to **one** boundary vertex has L_eff=(0). Distinct interiors can be indistinguishable to that static one-port observer. “It looks like a point” is not equivalent to faithful reconstruction of its internal source. Nontrivial port measurements or an additional dynamical probe are necessary.

## IV. Dynamic conservation forces memory

Equip interior vertices with positive capacities M_I; for no interior forcing impose

\[
M_I\dot z(t)+(Lu(t))_I=0.
\]

The exact instantaneous **physical RC-network energy balance** is

\[
\boxed{
b(t)^\top j_B(t)=u(t)^\top Lu(t)
+\frac{d}{dt}\left(\frac12z(t)^\top M_Iz(t)\right).
}
\]

Here input electrical power equals resistive dissipation plus the rate of stored capacitor energy. **Proof:** \(u^\top Lu=b^\top j_B+z^\top j_I\), and \(j_I=-M_I\dot z\). Integrate over time for cumulative input = dissipation + storage change. This is a genuine source-defined conservation law; it is not a theorem that arbitrary mathematical error estimates are physical energy.

For a unit 3-node chain with only its interior having capacitance m>0, the static effective Laplacian remains \(\frac12\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\), regardless of m. But its **Laplace-domain port operator** for real s>0 is

\[
\boxed{K_{\rm eff}(s)=I_2-\frac1{2+ms}
\begin{pmatrix}1&1\\1&1\end{pmatrix}.}
\]

At s=1, m=1 gives \(\left(\begin{smallmatrix}2/3&-1/3\\-1/3&2/3\end{smallmatrix}\right)\); m=2 gives \(\left(\begin{smallmatrix}3/4&-1/4\\-1/4&3/4\end{smallmatrix}\right)\). Both have identical **static** response but observably different **dynamic** response. In time domain \(m\dot z+2z=b_1+b_2\), with kernel \(m^{-1}e^{-2t/m}\) for zero initial condition: one must preserve a memory operator when crossing domains if future responses matter. This is classical elimination/Mori–Zwanzig-type memory specialized to an exact finite graph. Source history/capacities are not reconstructed by static Schur alone.

## V. Correlation of corrections: the metric and source must be real

For a declared common source metric and a decomposition x=a+e,

\[
\|x\|^2=\|a\|^2+\|e\|^2+2\operatorname{Re}\langle a,e\rangle.
\]

The covariance/cross-energy can be nonzero, and ignoring it is **not** conservative. For normalized source weights 1/2,1/2 and x=(1,1), a=(2,2), the exact budget is \(1=4+1-4\); assuming independent errors incorrectly yields 5.

**CBF-08 — finite conditional-expectation / observer refinement.** For a finite source probability distribution and nested observation partitions, the conditional expectation projections \(P_c\le P_f\) satisfy

\[
\boxed{\|x-P_cx\|_2^2=\|x-P_fx\|_2^2+\|(P_f-P_c)x\|_2^2.}
\]

In a nested infinite observer tower, if \(P_n\to P_\infty\) strongly then \(\sum_n\|(P_{n+1}-P_n)x\|^2=\|x-P_0x\|^2-\|x-P_\infty x\|^2\). The **dark residual** \(\|x-P_\infty x\|^2\) need not be zero if available probes are not dense. This separates improvement from full recovery. The finite rational model with x=(1,2,3,4) under uniform weights has exact \(\frac54=\frac14+1\) (coarse residual = fine residual + innovation). Two nonnested partitions cannot be treated as a telescoping tower without a new comparison map.

## VI. Transport gates, falsifiers, next work

| Gate | What must be produced | Decisive failure or boundary |
| --- | --- | --- |
| Common carrier | Same source ID, clock, valuation data and normalization on both sides | Fake p=6, shifted cell origin, distinct probabilistic source laws |
| Defined comparison map | Finite map, exact domain, declared metrics and orientations | “Same shape” is not a typed morphism |
| Conservative budget | Signed/positive flux identity, or full cross term, not just two unrelated norms | Oblique Q counterexample: cross = −60 |
| Uniform finite tail | Endpoint/coupling bound independent of the path of approximation | Fixed-prime subtraction diverges at s=1 |
| Coarse-graining invariant | Ports, interface flux, effective energy, and when needed memory | One-port static alias; m=1 vs m=2 dynamic alias |
| Faithfulness/selection | A probe distinguishes genuine source from matched mutant | Source-blind positive Gram and flatness fail |
| Limit passage | Joint Cauchy/convergence theorem in actual topology | Unbounded transports need graph-norm bounds |
| Pi/RH transfer | Genuine signed Weil source or BBP phase/carry Fourier estimate | No such theorem follows from graph energy or scalar zeta bounds |

**Next targeted research:** Build a common-source cross-boundary test on authentic SUCC prime jets and finite Tate characters, and independently on actual BBP base-16 carry dynamics. Measure the *interaction* term only after a common Hilbert/measure and source map are established. For nonzero signed Weil terms, positive network energy is a nonmatching model and cannot justify RH. For pi normality, the missing deliverable remains a pi-selected long-range Fourier/carry cancellation estimate, not another independently computed rational value of pi.

## Reproduction/provenance

New Python implementation: \`observational_succ/conservative_boundary_flux.py\`.
New exact rational tests: \`tests/test_conservative_boundary_flux.py\`; models cover true/fake primes, flatness, hidden energy/current, nested Schur, dynamic memory, literal RC power, nested conditional expectations, correlation debt, orthogonal/oblique two-domain transport and malformed source controls. All numbers are exact Python Fraction, not numerical fits.

**Isolated local 18-test run:** Python unittest with local module, all 18 passed; not a hosted repo-wide check. No original frozen Weil/Tate source files modified. To promote, run repo AGENTS.md required checks and independent hosted CI. **No RH proof, no pi normality proof, no physical universal conservation theorem.**
