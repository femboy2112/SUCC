# Reflection order: a failed global approximation and its local repair

**Status:** elementary paper proofs with exact rational regression witnesses.
These are adaptations of classical orthogonal-polynomial, compact-group and
reflection-positivity arguments; no priority claim is made. They extend the
fixed-source instruments in [WILSON_REFLECTION_SLICE.md](../WILSON_REFLECTION_SLICE.md)
and [HAAR_SOURCE_BRIDGE.md](../qm_graph_bridge/HAAR_SOURCE_BRIDGE.md).
They do not reproduce the continuum construction or prove a mass gap.

Implementation: [`ym_reflection_order.py`](../../../../observational_succ/ym_reflection_order.py).
Checks: [`test_ym_reflection_order.py`](../../../../tests/test_ym_reflection_order.py).
Existing `ym_succ_character.chebyshev_character` supplies the character
polynomials; existing Haar moments and exact PSD checks are reused.

## RO-01: global polynomial approximation can destroy reflection positivity

Let \(d\nu(x)=2\sqrt{1-x^2}\,dx/\pi\) be the law of the SU(2)
half-trace under Haar measure. Two disjoint reflected plaquettes have
independent half-traces \(x,y\) under their reference product Haar measure.
Reflection exchanges them. Gauge transformations preserve each loop trace.

**Theorem.** Let \(Q\) be a real polynomial of degree \(d\ge1\), with
leading coefficient \(c_d\ne0\), nonnegative on \([-2,2]\), and let
\(Z=\iint Q(x+y)d\nu(x)d\nu(y)>0\). The positive, gauge-invariant,
reflection-invariant probability density \(Q(x+y)/Z\) is **not** reflection
positive on the algebra of positive-half polynomial loop observables.

**Proof.** The characters \(U_j(x)\) are orthonormal in \(L^2(\nu)\).
Indeed, writing \(x=\cos t\), their inner products become
\((2/\pi)\int_0^\pi\sin((j+1)t)\sin((k+1)t)dt=\delta_{jk}\).
Their leading coefficient is \(2^j\). Thus

\[
\int U_d(x)x^j d\nu(x)=0\quad(j<d),\qquad
\int U_d(x)x^d d\nu(x)=2^{-d}.
\]

The reflected form is \(q(f,g)=Z^{-1}\iint\overline{f(x)}g(y)Q(x+y)d\nu(x)d\nu(y)\).
In the basis \((1,U_d)\), it is

\[
\begin{pmatrix}1&b\\b&0\end{pmatrix},\qquad b=c_d/(2^dZ)\ne0.
\]

For the lower-right entry to survive orthogonality, a monomial of
\(Q(x+y)\) would need degree at least \(d\) in each variable, hence
total degree at least \(2d>d\). The cross entry receives only the
\(c_dx^d\) term. The determinant is \(-b^2<0\); explicitly
\(q(1-U_d/b,1-U_d/b)=-1\). ∎

This is a statement about a **specific approximation operation**, not a
counterexample to Wilson reflection positivity. The exact source
\(e^{\beta(x+y)}=e^{\beta x}e^{\beta y}\), for \(\beta>0\), is reflection
positive: its form is the absolute square of a single weighted half-integral.
Applying a polynomial to the summed action loses that pairing.

### Exact hostile certificate at positive coupling

Take \(\beta=1\), and square the even Taylor amplitude of half the action:

\[
Q(s)=(1+s/2+s^2/8)^2,
\quad Z=645/512,
\quad h(x)=U_4(x)=16x^4-12x^2+1.
\]

The amplitude is strictly positive for every real \(s\), so this is a
strictly positive ordinary probability state. Exact Haar arithmetic gives

\[
\iint Q(x+y)h(x)d\nu(x)d\nu(y)=1/1024,
\quad \iint Q(x+y)h(x)h(y)d\nu(x)d\nu(y)=0.
\]

Hence its normalized reflected Gram matrix is
\(\left(\begin{smallmatrix}1&1/1290\\1/1290&0\end{smallmatrix}\right)\),
and \(f=1-1290h=-1289+15480x^2-20640x^4\) has reflected square **−1**.
Every entry is rational and is checked by the executable receipt.

This also applies to every nonconstant global Taylor-square order. It does
not say that every positive polynomial density fails RP: a factorized
polynomial density and a polynomial in a cross-plaquette holonomy have
different reflected kernels, as shown next.

## RO-02: the factorwise repair has a quantified source error

Consider any finite collection of SU(2) loop half-traces \(x_p\in[-1,1]\)
formed from a common set of Haar links. Shared links are allowed. Let
\(\beta_p\ge0\), let \(K_p\) be nonnegative even integers, and set

\[
w=\exp(\sum_p\beta_px_p),\qquad
w_{\mathbf K}=\prod_pP_{K_p}(\beta_px_p),\qquad
P_K(t)=\sum_{j=0}^K t^j/j!.
\]

The constant part of the Wilson action cancels in normalized expectations.
Every factor is strictly positive: for negative \(t\), the odd Taylor
remainder has negative sign, and for nonnegative \(t\) all terms are
nonnegative. For rational couplings these are rational polynomials in the
quaternion link coordinates. Their integrals are exact rational numbers.

**Theorem.** For every bounded complex observation \(|f|\le M\), writing
\(S=\sum_p\beta_p\) and
\(\tau_p=\beta_p^{K_p+1}/(K_p+1)!\),

\[
|\mathbb E_w f-\mathbb E_{w_{\mathbf K}} f|
\le 2M e^{2S}\sum_p\tau_p
\le 2M3^{\lceil2S\rceil}\sum_p\tau_p.
\tag{1}
\]

**Proof.** On \([-1,1]\), \(|P_K(\beta x)|\le e^\beta\) and
\(|P_K(\beta x)-e^{\beta x}|\le e^\beta\tau\). Product telescoping,
with no independence assumption about the \(x_p\), gives
\(\|w-w_{\mathbf K}\|_\infty\le e^S\sum_p\tau_p\).
The exact partition satisfies \(Z\ge e^{-S}\). If \(Z_K,N_K\) are
the approximate partition and numerator, positivity gives
\(|N_K|\le MZ_K\). Therefore
\(|N/Z-N_K/Z_K|\le2M\|w-w_K\|_\infty/Z\), proving (1). ∎

At fixed source and finite graph, its factorial tail tends to zero and an
exact rational algorithm can select a sufficient degree. Its volume-dependent
constant is not a uniform ultraviolet or thermodynamic estimate. The scalar
implementation of (1) is deliberately separately written from the coupled
quaternion engine's budget; agreement is an implementation cross-check,
not an independent proof or an independent external witness.

## RO-03: a precise reflection split preserves RP

The error bound above holds without a reflection split. The following
additional hypotheses are what buy exact RP.

* The configuration space is \(Y_-\times Y_+\), where each copy is a
  finite product of SU(2) groups with normalized product Haar measure \(m\).
  Reflection exchanges the two copies, and the positive-half algebra consists
  of bounded functions of \(y_+\) alone.
* Boundary data, if present, are **fixed**. There are no silently integrated
  continuous boundary variables in the finite-rank claim below.
* The density has the source-verified split
  \[
  w_K(y_-,y_+)=B(y_-)B(y_+)
   \prod_{p=1}^r P_{K_p}\bigl(\beta_p\operatorname{ReTr}
         [A_p(y_-)^{-1}A_p(y_+)]/2\bigr),
  \tag{2}
  \]
  with \(B\ge0\) bounded, not zero almost everywhere, \(\beta_p\ge0\),
  and even \(K_p\). Each \(A_p:Y\to\mathrm{SU}(2)\) is a declared
  measurable half-path holonomy. They may share links arbitrarily within
  the same half. Paired half-plaquette weights contribute to \(B\).
  A graph or lattice application must actually exhibit these maps.

**Theorem.** The normalized density (2) is reflection positive.

**Proof.** For the spin-\(j/2\) character \(\chi_j=U_j\), tensor powers
of the fundamental representation give

\[
x^n=2^{-n}\sum_{k=0}^{\lfloor n/2\rfloor}
 \left[{n\choose k}-{n\choose k-1}\right]\chi_{n-2k}(x),
\tag{3}
\]

where \({n\choose-1}=0\). The multiplicities are nonnegative; (3)
also follows inductively from \(2xU_j=U_{j+1}+U_{j-1}\), with \(U_{-1}=0\).
Consequently \(P_K(\beta x)=\sum_{j=0}^K c_j\chi_j(x)\) with \(c_j\ge0\).
For a unitary matrix representation \(D_j\),

\[
\chi_j(g_-^{-1}g_+)
 =\sum_{a,b=0}^j\overline{D_j(g_-)_{ab}}D_j(g_+)_{ab}.
\]

Multiplying the finitely many kernels gives
\(w_K(y_-,y_+)=\sum_\alpha\lambda_\alpha
\overline{F_\alpha(y_-)}F_\alpha(y_+)\), with
\(\lambda_\alpha\ge0\) and
\(F_\alpha=B\prod_pD_{j_p}(A_p)_{a_pb_p}\).
The same variables may occur in different factors; they are not averaged
independently. Integrating the two halves yields

\[
q_K(f,g)=Z_K^{-1}\sum_\alpha\lambda_\alpha
 \overline{\int f F_\alpha\,dm}\int g F_\alpha\,dm,
\tag{4}
\]

which is positive semidefinite. Strict positivity of the cross weights
and nontrivial \(B\) give \(Z_K>0\). ∎

This proof uses the finite character expansion directly; no unproved
exchange of an infinite Peter–Weyl series is needed. Negative coupling,
arbitrary global polynomial truncation, undeclared reflection support, or
an arbitrary graph without the split do not inherit the theorem.

### Shared links do not break the argument

For a concrete common-link kernel take \(Y=\mathrm{SU}(2)^2\),
\(y=(u,v)\), \(A_1(y)=u\), \(A_2(y)=uv\), and \(B=1\).
The two cross loops share \(u_-\) and \(u_+\). In edge-word notation
\((u_-,v_-,u_+,v_+)=(1,2,3,4)\), their words are
\((-1,3)\) and \((-2,-1,3,4)\).
At \(\beta_1=\beta_2=1\), \(K_1=K_2=2\), each factor has
\((c_0,c_1,c_2)=(9/8,1/2,1/8)\). Formula (4) has at most
\(14^2=196\) features and proves RP for every bounded half-observable.
This is a source-declared finite Wilson-loop graph, including a two-edge
loop; it is not advertised as a four-dimensional hypercubic plaquette.
No claim of independent plaquette distributions is used.

**Executed source check.** Give the four edges endpoints
\(((0,1),(1,2),(0,1),(1,2))\), so both listed words are closed paths.
Before direct integration the character calculation predicted partition
\(Z_K=(9/8)^2=81/64\) and reflected Gram
\(\operatorname{diag}(1,1/18,1/81)\) on
\((1,\operatorname{Re}u_+,\operatorname{Re}v_+)\).
To derive the prediction, change coordinates within each half to
\((a,b)=(u,uv)\); Haar invariance gives product Haar in these coordinates.
Each character-convolution factor has eigenvalues \(c_j/(j+1)\).
The test \(\operatorname{Re}u\) lies in representation types \((1,0)\),
while \(\operatorname{Re}v=\operatorname{Re}(a^{-1}b)\) lies in
\((1,1)\); both have ordinary squared norm \(1/4\).
After dividing by \(Z_K\), their reflected norms are
\((1/4)(1/4)(9/8)/(81/64)=1/18\) and
\((1/4)(1/4)^2/(81/64)=1/81\); cross entries vanish by orthogonality.
The quaternion engine integrated all **19,593** density monomials with
shared variables retained, reproducing these exact rational entries.
This verifies the declared common source in two calculation presentations;
it is not independent external mathematical review.

## RO-04: finite reflected features give a finite OS Hilbert quotient

Under exactly the split of RO-03, let
\(D=\prod_{p=1}^r\sum_{j=0}^{K_p}(j+1)^2\).
The map
\(f\mapsto (Z_K^{-1/2}\sqrt{\lambda_\alpha}\int fF_\alpha dm)_\alpha\)
has at most \(D\) coordinates, and (4) is its ordinary inner product.
Its kernel is exactly the OS null space. The OS quotient and its completion
are thus isometric to the image in \(\mathbb C^D\), of dimension at most
\(D\). The image is a linear subspace of a finite-dimensional space, hence
closed. This is an actual finite quantum-state-space presentation of the
specified reflected source approximation.

For rational polynomial half paths and weights, square roots need not be
introduced to compute it. In \(\operatorname{Sym}^j\mathbb C^2\), use
the averaged tensor-word basis \(v_k\) with \(k\) ones. Its metric is
\(H_j=\operatorname{diag}({j\choose k}^{-1})\); the raw representation
matrices have \(\mathbb Q(i)\)-polynomial quaternion entries and obey
\(D_j^*H_jD_j=H_j\). Therefore

\[
\chi_j(g_-^{-1}g_+)=\sum_{a,b}
 (H_{j,aa}/H_{j,bb})\overline{D_j(g_-)_{ab}}D_j(g_+)_{ab}.
\]

The feature weights are nonnegative rational numbers. Product Haar moments
of polynomial entries are rational-complex. Exact Gaussian elimination
with the declared positive metric computes null spaces and finite Gram
representations. An orthonormal basis may require algebraic square roots;
the raw metric presentation does not.

**Boundary:** this supplies no Hamiltonian or dynamical law. Time translation
must separately preserve the null space and satisfy the required semigroup
and positivity contracts before it acts on this quotient. Continuous shared
boundary integration can introduce infinitely many features; integrating
finite-rank conditional kernels does not generally retain a finite-rank bound.
The full untruncated Wilson source has infinitely many representation types.
Finite quotient dimensions at every approximation do not prove a uniform gap.

The continuous-boundary caveat has an explicit countermodel. On the circle
with normalized Haar measure let
\(B_z(t)=P_r(t-z)\), where \(0<r<1\) and
\(P_r(t)=(1-r^2)/(1-2r\cos t+r^2)>0\) is the Poisson kernel.
For each fixed \(z\), the density \(B_z(t_-)B_z(t_+)\) has reflected
rank one. Averaging \(z\) gives
\(P_{r^2}(t_--t_+)\), whose Fourier eigenvalues are
\(r^{2|n|}>0\) for every integer \(n\). Thus the averaged reflected
form has infinite rank. Reflection positivity survives the convex mixture;
the uniform finite-rank conclusion does not.

## RO-05: fixed tests and moving hostile tests are compatible

For a reflection-invariant exact RP probability \(\mu\), suppose an
approximation \(\mu_K\) satisfies
\(|\mathbb E_{\mu_K}F-\mathbb E_\mu F|\le\varepsilon_K\|F\|_\infty\).
Then every fixed bounded half-test satisfies

\[
q_K(f,f)\ge-\varepsilon_K\|f\|_\infty^2.
\]

If \(\varepsilon_K\to0\), this suffices to pass RP for that fixed
test to the limit. The RO-01 witness changes its degree and coefficients
with \(K\). Its reflected square −1 is obtained by rescaling by the
inverse of a vanishing cross entry; its supremum norm is uncontrolled.
There is no contradiction with fixed-test convergence. Finite tomography
and asymptotic positivity have different quantifiers, paid explicitly here.

## Two further exact hostile controls

**Gauge invariance and ordinary Gram positivity are insufficient.** On two
reflected Z2 triangles let \(W_+,W_-\) be their loop products and give all
64 edge configurations mass \((1-aW_-W_+)/64\), \(0<a<1\).
This is strictly positive, gauge invariant and reflection invariant. Its
ordinary Gram matrix on \((1,W_+,W_-)\) is
\(\left(\begin{smallmatrix}1&0&0\\0&1&-a\\0&-a&1\end{smallmatrix}\right)\),
with positive eigenvalues \(1,1-a,1+a\). But the reflected square of
\(W_+\) is \(-a\). The exact test uses \(a=1/2\).
This is not the positive-coupling Wilson action; it isolates the missing
signed source hypothesis.

**Reflection-equivariant CP maps still need positive-time localization.**
On uniformly distributed \((a,b)\in\{0,1\}^2\), swapping coordinates
is reflection and the fine positive-half form is \(|\mathbb E f(a)|^2\).
The deterministic map \(\pi(a,b)=(a(1-b),b(1-a))\) commutes with swap.
Its pullback is a unital *-homomorphism, hence completely positive.
Yet the coarse joint distribution is
\(\left(\begin{smallmatrix}1/2&1/4\\1/4&0\end{smallmatrix}\right)\).
For \(f=(1,-2)\), the coarse reflected square is −1/2, whereas the
fine one is 1/4. The coarse positive coordinate reads both fine halves.
Thus this does not contradict YT-02, which explicitly requires preservation
of the positive-time algebra.

## Scope ledger and the next falsifier

| Claim | Status and authority | Remaining obligation |
|---|---|---|
| Every nonconstant positive global polynomial in two reflected half-actions fails RP | PAPER PROVED; exact degree-four witness | Scope is this operation and full half-polynomial algebra. |
| Factorwise even Taylor weights approximate the actual finite Wilson state | PAPER PROVED; rational budget | Coupling/volume-dependent bound; no uniform continuum estimate. |
| The declared reflection split preserves RP and gives finite feature rank | PAPER PROVED | Supply and verify the split for each new source; dynamics are separate. |
| Gauge averaging, ordinary Gram positivity or CP alone gives RP | REFUTED | Exact signed and support countermodels above. |
| This construction reproduces 4D continuum Yang–Mills or its mass gap | NOT ESTABLISHED | Renormalization, common-source limits, field domains and uniform physical spectral estimates. |

The next discriminating probe is a new reflected lattice with an explicitly
listed cross-plaquette decomposition and a nontrivial shared-link observation.
Predict the reflected feature Gram and its source normalization *before*
direct quaternion integration. A mismatch refutes the proposed source map
or implementation. Agreement checks that finite interface only; it does not
promote a finite matrix to an all-scale field theory. Tests use exact rational
receipts; universal statements are justified by the displayed proofs.

Classical background: K. Osterwalder and E. Seiler, *Gauge field theories
on a lattice*, Annals of Physics 110 (1978), 440–471,
[doi:10.1016/0003-4916(78)90039-8](https://doi.org/10.1016/0003-4916(78)90039-8).
The finite split and proofs used here are stated explicitly; the reference
does not replace verification of a source-specific decomposition.
