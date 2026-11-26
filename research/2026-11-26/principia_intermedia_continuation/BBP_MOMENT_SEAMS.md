# Original BBP source: null constraints force real crossings

This is a concrete application to SUCC's existing source. It starts with a retained source field and null constraints; its Gram determinant is derived from those constraints. The proofs are classical orthogonal-polynomial and finite-dimensional arithmetic arguments, specialized exactly to the original four signed BBP poles.

**Critical scope:** these source moments depend on the forcing r, not on the homogeneous seed. We preserve the canonical U_0=0, but the moment family alone cannot discriminate it from a changed-seed orbit with the same forcing. The next source-to-statistics bridge must retain the seed and chronological carry data separately.

## BM-01: positive source representation and exact Gram nondegeneracy

Keep

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}
       -\frac1{8n-3}-\frac1{8n-2},\qquad
 U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Let

\[
 Q(t)=4-2t^3-t^4-t^5
 =(1-t)(4+4t+4t^2+2t^3+t^4).
\]

On 0<t<1 this is strictly positive. With u=t^8 set

\[
 d\mu(u)=\frac{Q(u^{1/8})}{8u^{7/8}}\,du,\qquad 0<u<1.
\]

The measure is finite, positive and gives positive mass to every nonempty open subinterval. Substitution gives, for every integer k>=0,

\[
 m_k:=\int_0^1u^k\,d\mu(u)
 =\int_0^1t^{8k}Q(t)\,dt
 =r(k+1)\in\mathbb Q.
\]

For N>=1 let H_N=(m_{i+j})_{0<=i,j<N}. Every nonzero real vector c satisfies

\[
 c^\mathsf{T}H_Nc
  =\int_0^1\Big(\sum_{j=0}^{N-1}c_ju^j\Big)^2d\mu(u)>0.
\]

**Proof of strictness.** A nonzero polynomial is nonzero on some open interval; the integrand is strictly positive there and the measure gives it positive mass. Thus H_N is positive definite and det H_N>0 for every N. This is a proof for all N, not an inference from finite positive determinants.

The positive Mellin representation reexpresses a signed arithmetic forcing. It does not make BBP digits random or confer temporal independence.

## BM-02: N source-null moments force N simple seams

For every N>=1 there is a unique monic polynomial

\[
 P_N(u)=u^N+\sum_{j=0}^{N-1}c_ju^j\in\mathbb Q[u]
\]

such that

\[
 \int_0^1 u^kP_N(u)\,d\mu(u)=0
 \quad(0\le k<N).
\]

Moreover P_N has **exactly N simple real roots in (0,1)**, and it changes sign at each one.

**Existence, uniqueness and rationality.** The null equations are the invertible rational system

\[
 H_N(c_0,\ldots,c_{N-1})^\mathsf{T}
 =-(m_N,\ldots,m_{2N-1})^\mathsf{T}.
\]

**Forced-crossing proof.** List the distinct roots z_1,...,z_s in (0,1) where P_N changes sign, and let A(u)=product_{j=1}^s(u-z_j). If s<N, the continuous polynomial P_N A has one constant sign on (0,1) except at its finitely many roots, and is not identically zero. Its integral against the positive full-support measure is therefore nonzero. But deg A<N, so the null moment equations force that integral to be zero. Contradiction. Hence s>=N. Degree N then forces exactly N distinct roots, all simple and all inside (0,1). QED.

This is an IVT-shaped theorem stronger than one endpoint sign test: **many independent null constraints force many crossings**. The observer family

\[
 O_t=(\mu,\text{source certificate},P_N,t,P_N(t)),\qquad 0\le t\le1,
\]

retains the same source and polynomial, with continuous relative readout P_N(t). The common comparison target is the retained source structure; the numerical last coordinate is allowed to vary.

**First exact instance.** m_0=47/15 and m_1=106/819, so

\[
 P_1(u)=u-\frac{530}{12831}.
\]

The negative readout at u=0 and positive readout at u=1 cross at the exact source-selected rational value 530/12831. Higher P_N have rational coefficients, with generally algebraic seam locations.

## BM-03: an actual source-resolvent null jet of exact order N

Define

\[
 G_N(z)=\int_0^1\frac{P_N(u)}{16-uz}\,d\mu(u),
 \qquad |z|<16.
\]

The compact support permits uniform geometric-series expansion on smaller disks:

\[
 G_N(z)=\sum_{k\ge0}\frac{z^k}{16^{k+1}}
             \int_0^1u^kP_N(u)\,d\mu(u).
\]

Consequently the first N Taylor coefficients vanish. The next one is strictly positive:

\[
 [z^N]G_N(z)=\frac{h_N}{16^{N+1}}>0,\qquad
 h_N=\int_0^1P_N(u)^2\,d\mu(u).
\]

**Proof.** u^N-P_N has degree <N and is orthogonal to P_N, giving

\[
 \int u^NP_N\,d\mu=\int P_N^2\,d\mu=h_N>0.
\]

Thus G_N has a zero of **exact order N**, not an identically zero germ. The norm is rational; with det H_0=1,

\[
 h_N=\frac{\det H_{N+1}}{\det H_N}.
\]

The determinant formula follows by the Schur complement of the moment Gram, or by changing the monomial basis to the monic orthogonal basis with unit triangular determinant. A determinant appears here because it measures the source-null linear system; it was not inserted as an unexplained extra oracle.

**Fixed-degree capacity.** If a real polynomial P of degree at most D satisfies all D+1 moment nulls of orders 0,...,D, then P=0. Expand P in monomials to get integral P^2 dmu=0 and use positivity. Therefore a nonzero degree-D field can sustain at most D consecutive initial null moments.

Letting N grow changes P_N. An arbitrarily long null prefix spread across different fields does not imply one nonzero field has an infinite null tower. The degree is the capacity paid by this construction.

## BM-04: a rational arithmetic threshold for approximate source-nullness

Fix D>=0 and let H=H_{D+1}. Define the exact positive rational constant

\[
 C_D=\|H^{-1}\|_{\infty\to\infty}
   =\max_i\sum_j |(H^{-1})_{ij}|.
\]

Let P(u)=sum_{i=0}^D c_i u^i be nonzero with rational coefficients. Suppose Q and M are positive integers and

\[
 Qc_i\in M\mathbb Z\quad\text{for every }i.
\]

Then

\[
 \boxed{\max_{0\le j\le D}
   \left|\int_0^1u^jP(u)\,d\mu(u)\right|
       \ \ge\ \frac{M}{Q C_D}>0.}
\]

**Proof.** Some coefficient has absolute value at least M/Q. For the moment vector b=Hc,

\[
 M/Q\le\|c\|_\infty
       =\|H^{-1}b\|_\infty
       \le C_D\|b\|_\infty.
\]

Rearrange. QED.

This gives a strict incompatibility test: a nonzero field in the declared coefficient lattice cannot have every tested moment smaller than M/(Q C_D). Q pays the coefficient denominator. M can be a genuine simultaneous coefficient divisibility gain, but repeated or dependent constraints do not multiply it automatically. The field, moment matrix and analytic upper bounds must refer to the same retained source.

**Necessary controls.**

- P=0 has all moments zero and is explicitly excluded from a nonzero contradiction.
- Without Q, P=epsilon for a tiny rational epsilon violates an incorrectly claimed integer threshold.
- Scaling P by M/Q scales both its moment residual and its valid threshold.
- Dropping signed cross terms changes integral P^2 dmu and destroys the derived Gram geometry.
- A wrong source moment can destroy the exact null equations; a near-zero after such a change is not a certificate for the original forcing.

The constants may deteriorate rapidly with D. No useful D-to-shell asymptotic bound is claimed here. In particular, a valid finite positive threshold is not automatically strong enough to defeat a late-shell R0 counterhypothesis.

## BM-05: the same source exposes non-simultaneous scalar seams

For k>=0 consider

\[
 D_k(t)=\int u^k(u-t)\,d\mu(u)=m_{k+1}-tm_k.
\]

Each D_k has exactly one zero

\[
 \tau_k=m_{k+1}/m_k\in(0,1).
\]

The sequence is strictly increasing and tends to 1.

**Proof.** Strict Cauchy–Schwarz on the positive full-support measure gives

\[
 m_{k+1}^2<m_km_{k+2},
\]

so tau_{k+1}>tau_k. Because 0<u<1, each ratio is less than one. If its limit L were less than one, choose L<a<1. Positive mass above a gives m_k>=mu([a,1]) a^k, whereas the ratio bound gives m_k<=m_0 L^k, a contradiction. QED.

Thus every scalar channel crosses, but two adjacent channels never vanish at the same t. This is a source-exact crucible for the invalid quantifier swap

    for every channel, there is a seam point
    therefore there is one seam point for every channel.

The full all-channel theorem needs simultaneous finite-block feasibility, a common scalar factor, or a genuine multidimensional construction such as PI-07.

## 6. Relation to the existing null-seed tower

### BM-06: the null tower's capacity has a provable scale cost

The preceding construction can be tested beyond qualitative existence. Let m_0=47/15. For N>=1,

\[
 \boxed{0<h_N\le 4m_0\,16^{-N}.}
\]

**Proof.** Among monic degree-N polynomials, P_N minimizes the L2(mu) norm: any other such polynomial is P_N+R with deg R<N, and orthogonality gives squared norm h_N+integral R^2 dmu. The monic Chebyshev comparison

\[
 C_N(u)=2^{1-2N}T_N(2u-1)
\]

has supremum norm at most 2^{1-2N} on [0,1]. Therefore h_N<=m_0 times its squared supremum norm, giving the bound. QED.

For |z|<=r<16, Cauchy–Schwarz consequently gives

\[
 |G_N(z)|\le\frac{\sqrt{m_0h_N}}{16-r}
       \le\frac{2m_0\,4^{-N}}{16-r}.
\]

These nonzero, increasingly flat fields converge to zero locally uniformly on their common analytic disk. They do not converge to one nonzero analytic field with all jets zero.

The Schur complement also yields (H_{D+1}^{-1})_{DD}=1/h_D. Hence, for D>=1, the particular exact gap from BM-04 obeys

\[
 \frac{M}{QC_D}\le\frac{M}{Q}h_D
       \le\frac{4Mm_0}{Q}\,16^{-D}.
\]

For bounded M/Q this instrument has no degree-uniform positive threshold. Additional source-derived divisibility can change that ratio; the theorem does not rule it out. It says explicitly which growing arithmetic budget must be paid.

**Retaining norm changes the limit topology.** Normalize Q_N=P_N/sqrt(h_N). The Q_N are orthonormal. Every fixed polynomial probe pairs to zero for all sufficiently large N, while each Q_N retains norm one and distinct Q_N have L2 distance sqrt(2). Polynomial density in L2(mu) implies weak convergence to zero, but there is no strongly convergent subsequence. Thus a weak-null completion can hide a persistent norm/coupling signal; it cannot be used as a compact strong limit that preserves nonzeroness. This is a source-specific realization of the existing SUCC distinction between a null local report and retained global coupling.

PR [#689](https://github.com/femboy2112/SUCC/pull/689) already supplies the analytic source-null germ, nested seed cylinders, signed digit-seam currents and Hasse-jet/height distinctions. Its pinned [theorem dossier](https://github.com/femboy2112/SUCC/blob/d6fde02a8d810d361b8f7b97fbf3eb029ec6a7d3/research/2026-11-23/null_seed_virtual_tower/THEOREMS.md) is a provenance dependency, not silently assumed merged into #690.

This round adds a concrete null-constrained field P_N, forces its crossings, identifies the first surviving jet and supplies an exact approximate-null threshold. All definitions use the existing forcing. There is no need to invent a different arithmetic source.

The next step is a proved map from the **time-ordered, zero-seeded BBP shell** to one such nonzero field with sufficiently small simultaneous moments or sufficiently strong coefficient divisibility. The current moment data alone are seed-insensitive, so that map must preserve the seed/carry history rather than discard it. The coherent counterseed -pi/16 and the rational alias 1/16 remain mandatory controls.

No normality inference is made from orthogonal-polynomial crossings. Arbitrary positive full-support measures have the same classical mechanism; no temporal radix equidistribution follows from it.

## 7. Verification and attribution

Native [principia_bbp_seams.py](../../../observational_succ/principia_bbp_seams.py) uses exact Fraction Gaussian elimination and full signed pairings. The independent [source_moment_oracle.py](source_moment_oracle.py) constructs P_N through a SymPy determinant and uses exact Sturm root isolation, then checks capacity via a separately inverted matrix.

The [receipt](SOURCE_MOMENT_RECEIPT.json) contains the actual rational coefficients, Gram determinants, squared norms and isolating rational intervals for N=1,...,8, plus 119 independent integer-coefficient capacity specimens. These are finite implementation checks. The universal statements are established by the proofs above.

The simple-root and Gaussian-quadrature theory is classical; see NIST DLMF [18.2(vi)](https://dlmf.nist.gov/18.2.vi) and [3.5(v)](https://dlmf.nist.gov/3.5.v). The present paper rederives the required root theorem directly and makes no historical novelty claim. SUCC's signed source and the author's null-first research framing are retained explicitly.
