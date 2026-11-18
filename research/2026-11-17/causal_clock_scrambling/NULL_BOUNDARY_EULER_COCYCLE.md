# The Null-Boundary Euler-Shaped Cocycle — A Vanishing Product with a Nonvanishing Source Jet

**SUCC / Principia / original four-pole BBP, 2026-11-17**

**User's discovery:** the multiplicative transport product for the original BBP zero-seed computation has a **literal initial zero**, but the subsequent factors are coherent and retain source-derived information. Is the null boundary truly featureless, or does an observer probing a changed seed reveal a differential "0*J" support?

**Scope and verdict:** NBC-01–05 are **PROVED PAPER / elementary classical** identities and a calibrated first-jet observation. NBC-06 is an exact *locked zero-seed countermodel*. The Euler-product-at-s=-1 comparison is a shared algebraic product/transport form, **not an identification of prime factors with BBP clock steps**. The missing BBP all-shell terminal norm bound, R0, and π base-16 normality remain **OPEN**.

## 1. One original source, literal null homogeneous input

Retain without modification the authentic source
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0(0)=0,\quad U_{n+1}(0)=16U_n(0)+r(n+1).
\]

Its original rational partial sum and completed endpoint are
\[
P_N=\sum_{j=1}^N16^{-j}r(j),\qquad
P_N\to x:=\pi/16,\qquad
P_1=47/240,\quad U_1(0)=47/15.
\]
The last completion is the classical BBP identity, independently derived from the original signed impulse/Mellin kernel in [BBP Impulse/Mellin Filter](BBP_IMPULSE_MELLIN_FILTER.md).

To probe the selected null seed without altering the forcing, introduce an *explicit counterfactual* homogeneous input s:
\[
U_n(s)=U_n(0)+16^n s=16^n(P_n+s).
\]
For s≥0 every finite denominator below is strictly positive. Analytic/meromorphic identities at other complex s are to be read where all original factors are defined; no silent cancellation through an actually undefined factor is permitted.

## 2. Correct normalization and exact finite multiplicative product

The original additive recurrence implies
\[
16U_n(s)-U_{n+1}(s)=-r(n+1).
\]
For nonzero \(U_{n+1}(s)\), define the *normalized chronological transfer*
\[
\boxed{\Lambda_n(s)=1-\frac{r(n+1)}{U_{n+1}(s)}
=\frac{16U_n(s)}{U_{n+1}(s)}.}\tag{NBC1}
\]
The factor is a ratio of state-dependent source transfers; it is not an Euler factor of a prime.

### NBC-01 (EXACT telescoping identity)

For finite N≥1 and admissible s,
\[
\begin{aligned}
G_N(s)&:=\prod_{n=0}^{N-1}\Lambda_n(s)
=\prod_{n=0}^{N-1}\frac{16U_n(s)}{U_{n+1}(s)}\\
&=\boxed{\frac{16^Ns}{U_N(s)}
=\frac{s}{s+P_N}.}
\end{aligned}\tag{NBC2}
\]

Because P_N>0 and P_N→x>0, for each fixed s≥0,
\[
\boxed{G_\infty(s)=\lim_{N\to\infty}G_N(s)=\frac{s}{s+x}
=\frac{s}{s+\pi/16}.}\tag{NBC3}
\]

Uniform holomorphic convergence holds on compact subsets of \(|s|<P_1\), since \(P_N\ge P_1>0\); it licenses passing fixed-order derivatives through the N→∞ limit near s=0. The raw product at s=-x does not have a finite limit, and exceptional negative seeds may cause original intermediate denominators to vanish: those are separate access/domains, not regular zeros.

## 3. The first factor is exactly zero; its continuation is not

The entire product decomposes into an initial boundary factor and a suffix:
\[
\boxed{
G_N(s)=
\underbrace{\frac{s}{s+P_1}}_{\Lambda_0(s)}
\underbrace{\frac{s+P_1}{s+P_N}}_{\prod_{n=1}^{N-1}\Lambda_n(s)}.
}\tag{NBC4}
\]

### NBC-02 (EXACT zero-boundary and nonzero continuation)

At the authentic literal seed s=0:
\[
\boxed{
\Lambda_0(0)=1-\frac{r(1)}{U_1(0)}=0,
\qquad
\prod_{n=1}^{N-1}\Lambda_n(0)=\frac{P_1}{P_N}>0.
}\tag{NBC5}
\]
After completion,
\[
\boxed{\prod_{n=1}^{\infty}\Lambda_n(0)
=\frac{P_1}{x}=\frac{47}{15\pi}.}\tag{NBC6}
\]

A zero total product hides a nonzero **conditioned suffix**. This is not an entropy/quantum measurement or an actual information-free forcing: the chosen r(n), clock, denominator normalization and initial section are supplied data.

### NBC-03 (EXACT source-dependent tangent and higher jets)

Differentiate the finite identity \(G_N(s)=s/(P_N+s)\):
\[
\boxed{
G_N(0)=0,\quad
G_N'(0)=1/P_N,\quad
G_N^{(k)}(0)=(-1)^{k-1}k!/P_N^k\ (k\ge1).
}\tag{NBC7}
\]
On the completed source,
\[
\boxed{
G_\infty'(0)=1/x=\frac{16}{\pi},\qquad
G_\infty^{(k)}(0)=(-1)^{k-1}k!(16/\pi)^k.
}\tag{NBC8}
\]

There is an explicit chain-product decomposition of the first response:
\[
\boxed{
G_\infty'(0)
=\underbrace{1/P_1}_{\text{boundary jet}}
\underbrace{P_1/x}_{\text{nonzero source suffix}}
=\frac{16}{\pi}.}\tag{NBC9}
\]
The first jet is an exact source-dependent observable beyond the zero-valued product. **This is a mathematically faithful interpretation of the user's tagged \(0*J\):** ordinary base evaluation sees 0, while the *declared seed-direction derivative* is nonzero.

For a nilpotent formal parameter \(\epsilon^2=0\), the corresponding dual-number formula is
\[
\boxed{G_\infty(\epsilon v)=\epsilon\,v/x.}\tag{NBC10}
\]
Literal \(0\cdot J\) remains zero in an ordinary ring; the nontrivial structure resides in the tagged **first-jet/probe direction** and its source-defined transport.

## 4. Crucible: the product is not a normality inequality

**NBC-04 (EXACT generality boundary):** the algebraic telescoping identity works for *any* forced radix-16 recurrence \(U_{n+1}=16U_n+f(n+1)\) with zero initial seed and positive completed endpoint \(x_f=\sum16^{-n}f(n)\). The entire product's nonzero first jet is \(1/x_f\); it only encodes the **completed scalar endpoint**, not a new inequality controlling its digit distribution.

**NBC-05 (EXACT locked control):** take a different null-seeded forcing \(f(1)=16,\ f(n)=0\ (n>1)\). Then \(x_f=1\), the completed circle orbit is identically phase 1, and the raw zero-seed product is still 0. Its source-continuation suffix is 1, and \(G_\infty'(0)=1\ne0\). Thus
\[
\boxed{\text{null boundary + coherent suffix + nonzero jet}\not\Rightarrow\mathrm{R0}.}\tag{NBC11}
\]
The control is a *changed source* and does not refute the literal BBP four-pole conjecture.

A second obstruction: the entire multiplier product for fixed N depends only on \(P_N\); different forcing histories sharing the same terminal value are indistinguishable to this scalar readout. The affine source-history rank-one tomography no-go remains active. A complete proof needs an additional source-selected signed carry/cofactor constraint, not just an ever-higher derivative of \(s/(s+x)\).

## 5. Typed comparison to the Euler product at s=-1

[SUCC Prime Compensation PR #661](https://github.com/femboy2112/SUCC/pull/661) uses genuine-prime Euler factors \(\chi_p(z)=1-p^{-z}\). At z=-1, each factor is \(1-p\ne0\) for actual rational prime p≥2. Finite insertion multiplies an Euler register by \((1-p)^{-1}\) and a complementary coprime/Hurwitz register by \(1-p\), preserving their product \(\zeta(-1)=-1/12\) **after analytic continuation**.

Our chronological BBP factors have the analogous *form* \(1-\lambda_n\) and likewise telescope as multiplicative transport, but \(\lambda_n=r(n+1)/U_{n+1}\) depends on the evolving source state. It is **not** a prime, a multiplicative arithmetic Euler factor, or independently distributed. Its first factor at the literal null seed has \(\lambda_0=1\), and so it really **vanishes**, unlike every prime factor at -1. These are two exact products with **different source labels, index sets, normalizations, endpoints and continuation laws**.

**Verdict:** the useful shared structure is a source-typed multiplicative cocycle, plus an observer-sensitive boundary section. A prime-to-BBP comparison needs an actual source-valid transport of factors and a discriminating prediction. Merely noting \(1-\lambda\sim1-p\) cannot establish such a transport.

## 6. Next proof-directed intervention

The original all-late-shell gate still reads
\[
\boxed{
\exists\delta>0,B_0\ \forall B\ge B_0:\quad
R_B(0)=\frac1B\sum_{k=1}^{B}\left\|\frac{U_{2B}(0)}{16^k}\right\|_{\mathbb T}^2\ge\delta.
}\tag{NBC12 — OPEN}
\]
Its proof would establish R0, not full base-16 normality. The new derivative NBC8 is a new *observation layer of the same endpoint x*, not a source-derived positive lower bound in NBC12.

**Next decisive lamp:** supplement the seed-derivative jet with a **chronological, source-passported cross-response** depending on the full four-pole/carry/cofactor ancestry. Find a finite invariant whose nonzero source-residue memory forces a positive density of genuinely separated original zero-seeded integer windings on each late shell; reject the coherent locked seed, changed-source locked forcing, dyadic seed aliases and impulse/history rivals. Avoid treating randomized seed averages as π digit statistics or substituting one scalar endpoint for source history.

### Reproducibility and ledger

- **PROVED PAPER, source-selected algebra:** NBC1–10, with the classical BBP evaluation as a stated imported premise.
- **EXACT CONTROL:** the locked different-forcing example NBC11.
- **REFUTED implication:** zero initial factor, nonzero conditioned suffix or nonzero jet would imply R0.
- **OPEN:** original source R_B all-shell coercivity, R0 and π base-16 normality.
- **Execution:** [tests/test_bbp_null_boundary_product.py](../../../tests/test_bbp_null_boundary_product.py), [validation receipt](NULL_BOUNDARY_EULER_VALIDATION.md); exact rational finite controls, separate SymPy derivatives and matched hash verification.

**Dependencies:** [original BBP impulse filter](BBP_IMPULSE_MELLIN_FILTER.md), [source-null homogeneous-input invariant](SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md), [original endpoint coercivity report](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), [seed resonance/jet layer](SEED_RESONANCE_AND_NULL_SUPPORT.md), [original source/carry interfaces](../../../docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md), and [prime compensation](https://github.com/femboy2112/SUCC/pull/661). These are overlapping SUCC source lines, not independently verified copies of the π source.
