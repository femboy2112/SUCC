# SUCC Spectral Boundary Rigidity: observable geometry earned from return histories

**Research date:** October 22, 2026. **Stacked on** observation-anchored total boundary PR #242 at `146ddf514f05928158b38f0d8216b45df13dc92b`, descendant of SUCC PRs #240/#238/#236/#235/#234. **Research-only non-main branch.** Classical Jacobi inverse-spectral, Cauer/Stieltjes fraction and Kalman system-identification results are imported and attributed. The specific exact source-aware tests and the SUCC round-trip depth/epistemic interpretation are **new to this repository**, not established academic novelties. No physical measurements, gravitational ER=EPR or RH/Weil proof.

## The principal discovery

**Dynamic boundary response can force a unique *minimal observable* interior geometry under declared source restrictions, even though one scalar or the complete static response generally cannot.** The appropriate mathematical object is the **cyclic Krylov/Jacobi realization of the boundary observable**. It is determined by the response under classical minimality assumptions, but it need not equal the complete physical interior if dark modes or additional topology are present.

The observation pin is **a separately calibrated model discriminator**, not an axiomatic demand that a given constant be universally derivable from SUCC. A physical measurement of a dimensionless boundary response at one frequency may select one of finitely many predeclared branches. Recovering all parameters in an open high-dimensional model class requires stronger jointly separating data and a stability/error budget.

## 1. Declared physical toy carrier: positive passive RC path

Let the geometry class consist of a **rooted one-port path with a grounded opposite endpoint**, unknown positive rational edge conductances
\[
g_0,g_1,\dots,g_n>0
\]
and **unit-valued known shunt capacitance at each hidden vertex** `1,…,n`, with no boundary shunt. The one boundary and ground are two physical terminal vertices. For the n hidden coordinates, the positive Jacobi matrix is
\[
A_{jj}=g_{j-1}+g_j,\qquad
A_{j,j+1}=A_{j+1,j}=-g_j,\quad 1\le j<n.
\]
Dirichlet energy proves \(A>0\): for any nonzero interior vector, \(u^TAu=\sum_{i=0}^{n}g_i(u_i-u_{i+1})^2>0\) with grounded end values \(u_0=u_{n+1}=0\).

Eliminate all hidden coordinates in the Laplace-domain response:
\[
\boxed{Y(s)=g_0-g_0^2m_1(s),\quad
m_1(s)=\langle e_1,(sI+A)^{-1}e_1\rangle.}
\]
The domain `s≥0` has no poles. This is a **real Laplace response**, not an unlicensed identification of a positive real s with an AC drive frequency. A time-domain experiment or analytic continuation to frequency data requires independent physical instrumentation and proofs.

For n=0, the model is a direct resistor to ground of conductance `g_0` and `Y(s)=g_0`.

## 2. SBK-01 — conditional uniqueness by exact continued-fraction inversion

**Theorem (CLASSICAL / constructive derivation).** Within the declared positive path class with unit hidden capacitances, the **complete rational function** `Y(s)` uniquely determines n and every ordered conductance `g_0,…,g_n`, with the boundary/ground order fixed.

**Proof.** For n≥1, \(m_1(s)\sim1/s\) and
\[
g_0=\lim_{s\to\infty}Y(s)>0,\qquad
m_1(s)=\frac{g_0-Y(s)}{g_0^2}.
\]
Let \(m_j\) denote the diagonal resolvent of the tail beginning at hidden node j. The Schur complement at the next vertex gives the exact **source-driven recursion**
\[
\boxed{
m_j(s)^{-1}=s+(g_{j-1}+g_j)-g_j^2m_{j+1}(s)
}
\]
for j<n, terminating with \(m_n(s)^{-1}=s+g_{n-1}+g_n\).

The large-s asymptotic extracts \(a_j:=g_{j-1}+g_j=\lim_{s\to\infty}(m_j^{-1}-s)\). Starting with g0, recover `g_j=a_j-g_{j-1}>0`. For j<n, obtain
\[
m_{j+1}(s)=\frac{s+a_j-m_j(s)^{-1}}{g_j^2}.
\]
The process terminates at the unique final reciprocal affine function; irreducible tridiagonal Jacobi \(A\) with every \(g_j>0\) makes e1 **cyclic** (the deepest coordinate of \(A^{n-1}e_1\) is \((-1)^{n-1}\prod_{j=1}^{n-1}g_j\ne0\)). Hence the rational boundary m-function has exactly n visible poles and no hidden polynomial cancellation. It uniquely determines the length. Conversely, the recovered source conductances reproduce Y exactly and each inferred squared Jacobi link satisfies \(\lvert A_{j,j+1}\rvert^2=g_j^2\). QED.

This is a specialized, explicitly constructive case of classical finite Jacobi/Weyl inverse spectral theory, not a new physical theory. We independently implement polynomial Euclidean inversion and compare the recovered Y against a *separate full graph Schur-elimination oracle*.

**Exact calibration.** For g=(2,3,5), the two hidden-node interior is
\[
A=\begin{pmatrix}5&-3\\-3&8\end{pmatrix}
\]
and
\[
\boxed{Y(s)=\frac{2s^2+22s+30}{s^2+13s+31}}.
\]
The exact source-ordered inverse recovers (2,3,5) and n=2; neither graph topology nor source parameters were fit post hoc.

## 3. SBK-02 — a *finite* number of exact boundary frequencies suffices with a complexity cap

**Theorem (CLASSICAL exact rational identity).** If every admissible transfer response is proper rational `Y_i=P_i/Q_i` with numerator and denominator polynomial degrees at most a predeclared d, and if two models give the same exact readings at **2d+1 distinct common nonpole points** `s_j`, then `Y_1\equiv Y_2` as functions.

**Proof.** The numerator of `P_1Q_2-P_2Q_1` has degree at most 2d and vanishes at 2d+1 distinct points, so it is identically zero. QED.

Because the finite RC chain's response has numerator and denominator degree n, the combination of this identity theorem and SBK-01 shows that **2d+1 exact Laplace-domain responses** identify the entire chain in the class n≤d. The executable module reconstructs the rational transfer by exact overdetermined Gaussian interpolation (testing minimal possible degree), then obtains the conductances by Weyl/Schur inversion.

**Critical bounds:** \(2d+1\) is a sufficient uniform sample count, not necessarily minimal for this constrained class. These are **exact mathematical readouts**. For noisy physical observations, model-parameter intervals, pole conditioning and a genuine stability bound must be supplied. If unmodelled modes violate the degree cap, finite samples cease to certify global equality.

## 4. SBK-03 — the first return-history witness of a deeper hidden layer is exactly moment 2r

Define the boundary moments
\[
\mu_k=\langle e_1,A^ke_1\rangle,\quad
m(s)=s^{-1}\sum_{k\ge0}(-1)^k\mu_k s^{-k}
\]
for large \(\lvert s\rvert\) (analytic Laurent expansion outside the operator spectrum). These are exact sums of **source-labeled closed walks** of length k.

Take an existing path with r≥1 hidden nodes and conductances g0,…,gr. Create an extended path with r+1 hidden nodes by replacing its final grounded edge gr with a connection to a new vertex *of the same conductance gr*, and adding a new independent grounded edge g_{r+1}>0. The first r×r principal part of A is unchanged. Every boundary-return history visiting the new vertex requires **at least r forward edges and r backward edges**. Exactly one shortest topological path realizes this at length 2r, with scalar weight ∏_{j=1}^r(-g_j)^2. Thus

\[
\boxed{
\mu_k^{\rm extended}=\mu_k^{\rm original}\ \ (0\le k<2r),
\qquad
\mu_{2r}^{\rm extended}-\mu_{2r}^{\rm original}
=\prod_{j=1}^{r}g_j^2>0.
}
\]

This is a **mathematical causal-depth/round-trip theorem**. It does not prove reverse physical time, gravitational curvature, or the source's original physical layout. It is especially suited to SUCC's source-history requirements: the new depth becomes visible *exactly* at the shortest lawful return-history length. Our exact tests cover depths r=1,2,3, rational weight mutations and a new-terminal-weight independence holdout; the universal result follows from the walk proof.

## 5. SBK-04 — a stronger positive result: boundary response determines *operational* Krylov geometry

For a finite real symmetric positive operator A and source-selected boundary vector b, let
\[
\mathcal K(A,b)=\operatorname{span}\{b,Ab,A^2b,\ldots\}
\]
be the cyclic boundary-accessible subspace. Gram–Schmidt/Lanczos applied to successive Krylov vectors yields an **intrinsic finite Jacobi chain** on \(\mathcal K(A,b)\), with positive offdiagonal convention fixed up to the boundary sign/gauge. The scalar Weyl function \(m(s)=\langle b,(sI+A)^{-1}b\rangle\) uniquely determines that canonical *minimal observable chain* via its Stieltjes continued fraction. Different full physical graphs may share that same boundary-visible chain and must not be called physically identical.

An exact connected **dark-mode** witness:
\[
A_{\rm star}=
\begin{pmatrix}3&-1&-1\\-1&2&0\\-1&0&2\end{pmatrix},
\quad b=e_1.
\]
The antisymmetric mode \(d=(0,1,-1)\) obeys \(Ad=2d\) and \(\langle b,d\rangle=0\), so it is *invisible* under every boundary resolvent observation. The visible minimal Jacobi chain has **two** modes:
\[
a=(3,2),\quad b_1^2=2,\qquad
m(s)=\frac{s+2}{s^2+5s+4}.
\]
It is not the original three-mode star. A generic source can therefore force a unique operational Krylov geometry **without** forcing its hidden physical topology. The implementation now independently reconstructs the exact a-values, link squares and visible dimension; the stricter positive physical-chain inverse correctly rejects this fake as not satisfying its conductance/source constraints.

This is the correct application of the classical Kalman minimal-realization firewall: boundary input/output data determine **only the controllable and observable subsystem** up to similarity, unless a stronger canonical realization class is justified.

## SBK-07 — Hankel determinants are exact operational-depth witnesses

There is a stronger, *finite moment* signature of the minimal visible geometry. Define the source-boundary moment Hankel matrix

\[
H_r=(\mu_{i+j})_{0\le i,j<r},\qquad
\mu_k=\langle e_1,A^ke_1\rangle.
\]

It is **exactly the Gram matrix of the Krylov vectors** \(e_1,Ae_1,\ldots,A^{r-1}e_1\). For the strictly positive path Jacobi matrix with n hidden nodes,

\[
\boxed{\det H_r=\prod_{j=1}^{r-1}g_j^{2(r-j)}
\quad(1\le r\le n),\qquad \det H_{n+1}=0.}
\]

**Proof.** The kth Krylov vector \(A^ke_1\) is supported only on coordinates 1 through k+1. Its coordinate at depth k+1 is the product \((-1)^k\prod_{j=1}^k g_j\), the unique shortest path from the boundary-facing state to that depth. Thus the n×r Krylov matrix has an upper-triangular first r×r block with diagonal \(1,-g_1,g_1g_2,\ldots,(-1)^{r-1}\prod_{j=1}^{r-1}g_j\) and all deeper rows zero. Its Gram determinant is the square of the triangular determinant, namely \(\prod_{j=1}^{r-1}g_j^{2(r-j)}\). Since there are only n states, the (n+1)st Krylov matrix has dependent columns and zero determinant. QED.

This makes the **observable source depth** a family of boundary-computable exact invariants, *without assuming which interior state labels were used by a model builder*. Each additional nonzero principal Hankel minor establishes a new boundary-reachable dynamical layer. It also shows precisely why weak links are difficult to distinguish: \(\det H_r\) collapses rapidly as any \(g_j\to0\), although strict positivity keeps the mathematical rank unchanged.

For g=(2,3,5,7), the exact Hankel determinants are \(1,9,2025,0\); visible dimension is 3. For the connected three-state dark star in SBK-04, the corresponding exact Hankel determinants are \(1,2,0\); visible dimension is **2 despite three physical states**. The exact code independently constructs Krylov vectors, their Gram matrices and these determinants; 5 new adversarial tests accompany the earlier 23.

**Source caveat:** finite exact rank is not a physically certified rank under measurement error. To infer operational depth from noisy moments, establish spectral lower bounds for \(H_r\), conditioning, sensor calibration, and a prior admissible family. A tiny strictly positive determinant may be indistinguishable from zero within practical uncertainty.

## 6. SBK-N1 — no uniform physical stability without a coupling gap

For `0<eps<1`, compare the one-hidden-node chain g=(1,eps) and the two-hidden-node chain g=(1,eps,1). Both have strictly positive conductances and are individually boundary-minimal. But for any real s≥0,
\[
\boxed{
\big|Y_{\rm extended}(s)-Y_{\rm original}(s)\big|
=
\frac{\epsilon^2}{(s+1+\epsilon)((s+1+\epsilon)^2-\epsilon^2)}
<\epsilon^2.
}
\]
As eps→0, their entire nonnegative real Laplace response graphs converge uniformly on any fixed bounded s range (in fact the displayed bound is global), while the number of hidden physical nodes remains different. At eps=1/1000 and s=1 the exact response discrepancy is \(1/8012004\).

Thus a bounded number of noisy boundary measurements cannot uniformly determine topology over the full open family of arbitrary positive conductances. A rigorous stable inverse demands a **source-derived lower bound on coupling strength and suitable spectral/gap priors**; otherwise nearly dark modes look absent. This is a parameter-identifiability countermodel, not evidence that physical reality hides such a mode.

## 7. SBK-N2 — interface gluing and source factoring are distinct questions

Schur elimination is associative under the usual invertibility hypotheses, and independent subsystems glued by a common potential/flux interface add their DtN responses. However **the sum does not uniquely determine its summands**: a constant response g admits infinitely many positive parallel decompositions g=u+(g-u), 0<u<g. Even a fully measured boundary transfer function may identify the **composite response** without identifying every original constituent source. Prime-source labels, independent probes, source passports or an a priori **restricted** factorization law must be recovered separately.

## 8. Mathematical reality pins: one constant versus an independently separating response

Define a dimensionless, experimentally calibratable boundary response ratio, for example
\[
\eta_M(s)=Y_M(s)/Y_M(\infty),
\]
within this exact RC class. Competing *predeclared* models may predict distinct values at a held-out scale s. A measured dimensionless scalar can pick a member of a **finite mutually exclusive family** if the predicted bands separate sufficiently; the value need **not** have been derived as a universal constant from SUCC. A physical low-energy fine-structure alpha may play this role only after a source-honest SUCC realization produces a model-specific **physical coupling prediction** at a declared scale; setting a free parameter equal to measured alpha does not identify a geometry.

Euler–Mascheroni gamma is independently computable in mathematics but not itself a physical observation of spacetime geometry. A model claiming gamma as a *physical* pin needs a genuine measurable quantity whose predicted value equals gamma and an independent way to test that relation.

The response family encodes more data than a scalar. If the model class has d unknown continuous parameters, a scalar generally leaves a nontrivial prediction fiber. Full-rank Jacobians and inverse-function/stability criteria are appropriate local rigidity checks. One constant may suffice for a **discrete** family with separated predictions but not for arbitrary smooth high-dimensional families.

## 9. Exact claims and further source obligations

| ID | Status | Result |
|---|---|---|
| SBK-01 | CLASSICAL/PAPER PROVED/EXACT TESTED | Complete Y(s) uniquely recovers positive finite unit-capacitance path length and all ordered conductances, boundary/ground fixed |
| SBK-02 | CLASSICAL/PAPER PROVED/EXACT TESTED | Bounded rational degree d + 2d+1 exact distinct response values suffice to identify whole response and hence chain in declared path family |
| SBK-03 | CLASSICAL WALK THEOREM/PAPER PROVED/EXACT TESTED | Added hidden depth r first appears in boundary moment 2r, with exact positive squared-product signature |
| SBK-04 | CLASSICAL MINIMAL REALIZATION/PAPER PROVED/EXACT TESTED | Boundary function yields minimal observable Krylov/Jacobi geometry but not necessarily physical full graph |
| SBK-N1 | REFUTED global uniform-noise inverse | Arbitrarily weak positive new coupling makes distinct depths uniformly close under all fixed s≥0 probes |
| SBK-N2 | REFUTED unique component-factorization inference | Composite DtN gluing does not identify constituent interiors/source passports |
| SBK-05 | UNVERIFIED | SUCC source physical apparatus supplies a canonical cyclic boundary vector and measurement response, or actual gravity/quantum entanglement reconstructed |
| SBK-06 | OPEN RESEARCH | Compatible spectral construction across genuine prime-source charts, Archimedean completion, SUCC/FUCC reciprocity, and inverse-limit operator topology |

### Reproduction and references

- Exact source: `observational_succ/spectral_boundary_rigidity.py` (pure stdlib/Fraction), no polynomial black box. Independent graph Schur baseline: earlier `observational_succ/boundary_realization_selection.py`.
- Hostile tests: `tests/test_spectral_boundary_rigidity.py` (28 exact cases, including rational inverse, weak/dark modes and all source domains). Source-hashed receipt `scripts/spectral_boundary_rigidity_probe.py` with frozen JSON.
- **Provenance:** finite Jacobi m-functions and inverse spectral analysis: Fritz Gesztesy and Barry Simon, *M-Functions and Inverse Spectral Analysis for Finite and Semi-Infinite Jacobi Matrices*, Journal d'Analyse Mathématique 73 (1997), https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=96-395. Kalman, *Mathematical Description of Linear Dynamical Systems*, SIAM J Control (1963), https://doi.org/10.1137/0301010. Finite passive ladder/continued fractions is classical network theory. These results are not presented as newly discovered mathematics.

**Next verdict-changing target:** a **non-tautological source-faithful SUCC/FUCC spectral boundary functor** whose return-history Jacobi chain has interpretable intrinsic geometry, and which admits a real independently calibrated, predeclared dimensionless observable and a second held-out response. If source provenance fails, record that as a rigorous obstruction instead of asserting Einstein–Rosen geometry or RH.
