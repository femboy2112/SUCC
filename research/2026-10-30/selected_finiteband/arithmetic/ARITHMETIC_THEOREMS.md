# Positive rational quadrature can spoof every finite prefix and finite source jet

**Authority: PROVED LOCAL (paper proof), with exact finite witnesses and a separate
implementation. Same model family; not an external referee or Lean certificate.**
No scholarly priority claim. The authentic four BBP poles and U_0=0 are untouched.
The theorem constructs **changed sources**, not a counterexample to π normality.

## Provenance correction and exact increment over PR408

PR408 at `7b5a2b4534aa5e71865046ca8d3f723d8002b9fe`,
[`triangle_fabric/signed/SIGNED_FABRIC.md`](https://github.com/femboy2112/SUCC/blob/7b5a2b4534aa5e71865046ca8d3f723d8002b9fe/research/2026-10-30/triangle_fabric/signed/SIGNED_FABRIC.md)
SF-02–04 **already proves** positive completely monotone zero-seed nonnormal
sources matching arbitrary prescribed finite source prefixes and endpoint jets.
It also gives all-index relative bounds to the original source/tail and a dyadic
completed constant, stronger coherence than the generic rational period here.
Therefore the blanket finite-prefix/finite-jet obstruction below is credited
reproduction in a different representation, **not a newly discovered no-go**.
This overlap was identified by the principal researcher during live sibling
provenance review; the final theorem scope is corrected before delivery.

The distinct mathematical output here is the **positive rational atomic
order-two Stieltjes architecture**, with at most M+J+1 atoms, the lower bound
ceil((M+J+1)/2), exact unchanged Green upper-bound constants, a rational target
vector with exact witnesses, and full-moment determinacy. These architecture
results do not strengthen the existing selected BBP signed saving.

## AQ-01. The authentic Green tail is an order-two Stieltjes transform

Put

\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\quad n\ge0.
\]

The elementary identity

\[
r(n)=\sum_{(d,w)=(3,2),(4,1),(5,1)}w\int_0^d(8n-7+t)^{-2}dt
\]

follows by integrating each term. Define the positive measure on b>0 by

\[
\int f(b)d\nu(b)=\frac1{64}\sum_{j\ge1}16^{-j}
 \sum_{(d,w)}w\int_0^d f(j-7/8+t/8)dt.
\tag{1}
\]

Then, by positive summation,

\[
\boxed{T_n=\int_0^\infty(n+b)^{-2}d\nu(b),\quad
16T_{n-1}-T_n=r(n),\quad \nu(\mathbb R_+)=1/64.}\tag{2}
\]

The support is the union of intervals [j−7/8,j−1/4], j≥1. Its density is
strictly positive on each interval's interior. In particular b≥1/8; T_0 is
finite and equals π/16 by the original BBP identity. The measure has finite
exponential moments for every real t<log16, because b≤j and the weights are
16^−j. Every polynomial moment μ_k=∫b^k dν is **rational**:

\[
\mu_k=\frac1{64}\sum_{\ell=0}^k{ k\choose\ell}
 \left(\sum_{j\ge1}\frac{j^{k-\ell}}{16^j}\right)
 \sum_{(d,w)}\frac{w[(d-7)^{\ell+1}-(-7)^{\ell+1}]}{(\ell+1)8^\ell}.
\tag{3}
\]

The inner geometric-power sum is (q d/dq)^(k−ℓ)(q/(1−q)) at q=1/16.
For example μ_0=1/64. No supplied π digits enter any target vector below.

## AQ-02. Arbitrarily long exact prefix plus arbitrarily many exact jets

**Theorem.** For every pair of integers M≥1, J≥0 there are positive rational
nodes b_i≥1/8 and positive rational weights w_i, with at most M+J+1 nodes, such
that

\[
g(n)=\sum_i\frac{w_i}{(n+b_i)^2},\qquad
r_*(n)=16g(n-1)-g(n)\quad(n\ge1)
\tag{4}
\]

has all these properties:

1. r_*(n)>0 for every n≥1; it is completely monotone as a function of n−1.
2. r_*(n)=r(n) for n=1,...,M, **exactly**.
3. ∑_i w_i b_i^k=μ_k for k=0,...,J. Consequently
   g(n)−T_n=O(n^(−J−3)) and r_*(n)−r(n)=O(n^(−J−3)) as n→∞.
4. Its literal zero-seed trajectory is
   U_n^*=16^n g(0)−g(n); hence U_n^*=U_n for 0≤n≤M.
5. Its exact Green tail is g(n), and its completed selected constant is
   α_*=16g(0)∈Q. Its radix-16 completed orbit is eventually periodic and
   **not normal**, even though the source is positive, has the authentic
   n^−2 leading term, and matches any prescribed finite source jet.
6. The mutant has the **same all-horizon Green upper bounds** as the authentic
   source: g(n)≤(8n+1)^−2, 0<g(n)−g(n+1)≤16/(8n+1)^3, and
   Σ_(n≥1)g(n)≤17/648<1/32.

**Proof of rational positive cubature, including noncompact support.** Set
D=M+J+1 and

\[
F_n(b)=16/(n-1+b)^2-1/(n+b)^2,\quad
V(b)=(F_1(b),...,F_M(b),1,b,...,b^J)\in\mathbb R^D.
\]

These D rational functions are linearly independent: in a vanishing linear
combination, the double pole at b=0 first forces the F_1 coefficient to vanish;
the poles at −1,...,−(M−1) force each following F_n coefficient to vanish;
then the polynomial part vanishes. Their restrictions to any open interval
remain independent by the rational-function identity principle.

Let C be the convex cone of finite nonnegative **real** combinations of V(b)
for rational b in the support of ν. This cone is full dimensional. The vector

\[
y=\int V(b)d\nu(b)=(r(1),...,r(M),\mu_0,...,\mu_J)\in\mathbb Q^D
\]

belongs to the interior of C. Here is the boundary argument explicitly.
Integrability of all coordinates and finite rational-node approximations place
y in the closure of C. If y were not interior to that closure, a supporting
linear functional ℓ≠0 would satisfy ℓ(V(b))≥0 on all rational support nodes
and ℓ(y)=0. Continuity extends nonnegativity to the support. The integral of
this nonnegative function is zero, so it vanishes throughout an open interval
where ν has positive density. Rational-function independence forces ℓ=0,
a contradiction. A full-dimensional convex set and its closure have the same
interior; thus y is in C itself, not merely its closure.

Choose a finite representation y=∑w_iV(b_i) with the fewest nonzero positive
weights. Its columns are linearly independent: a dependence permits moving
weights along it until one becomes zero while keeping all others nonnegative.
Thus there are at most D columns. The independent rational columns and the
rational vector y have a unique solution on their column space; Gaussian
elimination makes all w_i rational. This proves the claimed **exact positive
rational** cubature, not just an approximation or floating LP feasibility.
The separation/finite-cone ingredients are classical; this source-specific
application is locally derived. Related cubature provenance is Bayer–Teichmann,
[The proof of Tchakaloff's theorem](https://arxiv.org/abs/math/0502473).
The above argument supplies the rational-node refinement needed here directly.

Property 1 follows from b_i>0 and, more strongly,

\[
r_*(n)=\int_0^\infty e^{-(n-1)x}
 x(16-e^{-x})\sum_iw_i e^{-b_ix}dx>0.\tag{5}
\]

The cubature constraints give properties 2 and 3. To justify the asymptotic
remainder despite unbounded support, Taylor's formula for (1+t)^−2 at t=0
has remainder of absolute value at most (J+2)t^(J+1) for t≥0.
Both measures have finite moment J+1, so integrating after multiplication by
n^−2 gives the asserted O(n^−J−3). Iterating (4) proves property 4, including
U_0^*=0. Finally,

\[
\sum_{j=1}^K16^{-j}r_*(n+j)
 =g(n)-16^{-K}g(n+K)\longrightarrow g(n).
\]

Thus property 5 follows. Rational constants have eventually periodic base-16
expansions; an eventually periodic word cannot have the uniform frequency of
every word length. For property 6, total mass 1/64 and b_i≥1/8 give the
first bound. Integrating the derivative 2(n+b+t)^−3 over 0≤t≤1 gives the
second. The integral test gives Σ_(n≥1)(n+1/8)^−2≤64/81+8/9=136/81;
multiplication by 1/64 gives 17/648. No irrationality/normality statement about the original π
trajectory was used in constructing the mutant. ∎

## AQ-03. Exact finite-band, carry, and CRT blindness is simultaneous

For the mutant in AQ-02, **every function of the exact list U_0,...,U_M**
agrees with the authentic source: all finite-band energies (all H, not only a
fitted band), all two-time differences, all digit masks, all literal update
carries defined from that list, every prime-primary and complementary rational
projection, and every finite cylinder statistic of the rational states.
This is exact equality of the inputs, not independent marginal matching.

Completed states are a different claim: α_* is rational, so its completed
states cannot be asserted equal to π states. The corrections g(n) and T_n
also need not agree at small n. Since r is matched for M steps, however,

\[
\alpha_* -\pi=16^{1-M}[g(M)-T_M].\tag{6}
\]

The moment-0 match and b≥1/8 yield g(M),T_M≤(1/64)(M+1/8)^−2; therefore

\[
|\alpha_*-\pi|\le\frac{16^{1-M}}{64(M+1/8)^2}.\tag{7}
\]

This is a quantitative finite-prefix approximation theorem. It does not make
α_* an authentic π source. A matching finite rational data set and any finite
rank/jet data cannot, within the larger positive source class, certify the
selected asymptotic Fejér bound.

For every rational α_*=A/D in lowest terms the completed orbit has ≤D points.
At any large hexadecimal depth q, its hard collision energy is at least q/D
by Cauchy–Schwarz on the occupied cells. Applying the universal hard/Fejér
comparison gives F_H(completed)≥(2/π²)q/D, H=q/2.
Moreover ∑g(n)<∞, so the usual O(H²/N) Green transfer sends this to the rational
U_n^* energy whenever H²/N=o(1). At the launchpad H_N≈N^(1/3),

\[
\lim_{N\to\infty}\frac{\log\mathcal F_{H_N,N}(U^*)}{m_N}=\log16.
\tag{8}
\]

The lower bound and trivial F_H≤H prove the limit. At the fixed frequency
h=D, the completed characters are all 1, so the actual signed sum also obeys
|Σ_(n≤N)e(D U_n^*)−N|≤2πD Σ_(n≥1)g(n)<∞. Thus this is an analytic
fixed-frequency coherence countermodel, not just eventual periodicity language.
D is fixed for each mutant;
there is no illicit choice of a different mutant at every N in this assertion.
This supplies an explicit asymptotic FAIL control for the finite-band target.

## AQ-04. Precisely what the finite jet preserves, and what repairs identification

The positive source kernel in (5) has the same Taylor coefficients through
order J+1 as the authentic kernel written in the n−1 clock. Its leading term
is (15/64)x, giving the same Gamma shape-two scaling limit after large-age
normalization. Consequently rank-two harmonic/golden/Euler limiting observer
geometry, including the author's Oily–Macaroni anchor λ−γ **when that same
observer is applied**, cannot by itself exclude this nonnormal positive source.
The anchor and triangle retain Leah / femboy2112 provenance. No new golden
clock is claimed to be arithmetically selected.

This is **not** equality of the complete original four-shift Gamma cocycle,
all p-adic Gamma data, all source values, or all asymptotic jets. The mutant
has finitely many double poles instead of the four prescribed simple poles.
That exact structural difference is available to a source-authentic theorem.

Two precise repairs of source identification are available, but neither is a
signed distribution estimate:

* With prior knowledge that the source lies in the original four-pole linear
  family, four distinct native times determine all four coefficients. The
  evaluation matrix is a nonsingular Cauchy matrix (distinct times and poles).
* Matching **all** μ_k identifies ν among positive measures on [0,∞).
  Indeed for any such rival and 0<t<log16, monotone convergence gives
  ∫exp(tb)dν_* = Σ_k t^k μ_k/k! = ∫exp(tb)dν <∞. Thus the rival
  also has a finite exponential moment; this regularity is derived, not assumed.
  Both moment generating functions are analytic near zero. Equal coefficients
  imply equal Laplace transforms, hence equal measures. An atomic ν_* cannot equal the
  authentic positive-density ν. Finite J admits AQ-02; the full jet does not.

**Source-aware atom lower bound.** Every positive atomic quadrature satisfying
all M prefix constraints and J+1 moment constraints needs at least

    ceil((M+J+1)/2) atoms.                            (9)

Thus the present rational construction has complexity between ceil(D/2) and D,
D=M+J+1. No optimality claim for the rational-node upper bound is made.
Here is a self-contained proof of the lower bound.

Order the function basis as 1,b,...,b^J,F_1,...,F_M. Every leading Wronskian
is nonzero on b>0. For a prefix ending in F_m, eliminate the polynomial block:
up to the positive constant ∏_(j=0)^J j!, the determinant is that of
F_n^(J+1+i)(b), 0≤i<m, 1≤n≤m. Since

    F_n(b)=∫_0^∞ x(16−e^−x)e^−(b+n−1)x dx,

removing row signs reduces this determinant to

    det[∫_0^∞ x^i (e^−x)^(n−1) ρ_b(x) dx],
    ρ_b(x)=x^(J+2)(16−e^−x)e^−bx >0.

Expand the determinant into permutations and use Fubini (all moments are
finite). Symmetrizing gives 1/m! times the integral of

    det[x_j^i] det[(e^−x_j)^(n−1)] ∏_j ρ_b(x_j).

For 0<x_1<...<x_m the first determinant is a positive Vandermonde and the
second has sign (−1)^(m(m−1)/2), with neither zero. The integrand has the
same sign in every permutation chamber. Restoring derivative row signs gives
Wronskian sign (−1)^(m(J+1)), so the determinant is strictly nonzero.
This is the classical determinant-of-integrals identity, derived here by
finite permutation expansion; no unverified total-positivity premise enters.

For completeness, nonzero leading Wronskians imply that each nonzero
combination of the first d basis functions has at most d−1 zeros counting
multiplicity. Induct on d: divide by the first nonvanishing function f_0,
then differentiate. The leading Wronskians of the derivative basis
(f_i/f_0)' equal W(f_0,...,f_k)/f_0^(k+1), so the induction hypothesis applies.
Rolle's theorem, including repeated zeros, restores the lost one zero. A
combination proportional to f_0 has no zeros. This proves the required
extended Chebyshev property without assuming a quadrature theorem.

If a positive atomic quadrature had s nodes with 2s<D, choose a nonzero
combination of the first 2s+1 basis functions that vanishes with its derivative
at every node (2s homogeneous constraints). The zero bound makes these exactly
its zeros, all of multiplicity two. Hence, after changing sign, the function
is nonnegative on (0,∞), positive except at the s nodes. Its atomic integral
is zero, but its ν integral is strictly positive. Exactness for the basis
contradicts this. Thus 2s≥D, proving (9). This also recovers the simpler
floor(J/2)+1 bound from polynomial moments alone.

## AQ-05. Signed CRT attacks and what remains unresolved

The inherited exact cofiber recurrence is retained, including p19 and p73
conductor disappearances. Prior papers already refute cofiber-free marginal
transport and establish dyadic seed aliases, Gauss-completion identities,
and huge-step frequency averages. Those are **reproduced controls**, not new
claims here. This round tests fresh actual joint lag distances and retains
both primary and complementary factors. Positive finite quadrature is a
materially different attempted route: it demonstrates that a hypothetical
bound using only positive Green transport, finitely many source values/jets,
and a zero initial condition still has nonnormal countermodels.

The smallest useful remaining selected obligation is still an inequality
excluding source-specific **joint** primary/cofiber restoration on enough
actual windows. The stronger source input must retain the globally prescribed
four-pole rational function (or an equally discriminating exact condition).
AQ-02 does not show such a theorem impossible; it identifies a broad family
of finite-data proof attempts that cannot establish it.
