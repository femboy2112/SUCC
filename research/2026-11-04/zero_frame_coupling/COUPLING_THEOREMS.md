# What the zero boundary, angular phase and radial observer jointly determine

The original recurrence and every time label are fixed. Write
`e(x)=exp(2 pi i x)`, `alpha=pi/16`, and

\[
U_n(s)=16^n(s+\alpha)-T_n,\qquad
Y_n(s)=U_n(s)-Z_n.
\]

Only s=0 is the authenticated original. The radial completed zero period
selects the small positive tail Z; it does not set the angular completion
`s+alpha` to zero. Setting that completion to zero gives the expressly wrong
coherent seed. These are different boundary conditions.

## Exact information and what survives transport

The inherited gauge `G_n(x)=x+Z_n` intertwines the two affine source maps
exactly. Its equal-character link is `W_(n,m)(H)=e(H(Z_m-Z_n))`.
The radix-covariant link instead is
`D_(n,m)(h)=e(h(Z_m-16^(m-n)Z_n))`, with
`D_(n,k)(h)=D_(m,k)(h)D_(n,m)(16^(k-m)h)`.
An observer cannot omit the transported frequency. Neither identity averages
the angular phase or changes a correctly transported source measurement.

For the coupled columns `v_ell(n)=e(H(Y_n+Z_(n+ell)))`, their Gram entries
are exactly `A^-1 sum e(H(Z_(n+ell)-Z_(n+k)))`. The common angular factor
cancels. Inverse Wilson transport of each column gives the *same* column
`e(HU_n)`; its Gram is then the all-ones matrix of rank one and norm L+1.
Keeping the former near-orthogonality while using the latter common-frame
identification is an invalid operation. [Full proof](front_cf/PROOFS.md).

The exact seed-annihilator classification is stronger than saying these
identities fail to identify the seed. An integer-character stencil P(E) at
time n responds to a seed change s by `e(16^n P(16)s)`. A finite family sees
seeds only modulo the annihilator of the gcd of those integers. Ward stencils
with P(16)=0 erase every homogeneous seed. Conversely, the full literal carry
word identifies the seed in [0,1); agreement through N carries gives
`|s-s'|<16^-N`. Identification supplies no distribution estimate for the
selected word. [Proofs AD-5/6](front_ad/PROOFS.md).

## A signed coupled inequality that does survive

Let M_ell be the maximum of `A^-1|sum_I v_ell(n)|` over all consecutive
I in [A,2A). For A>=128, integer H>0, `1<=Lambda=H/A^2<=A/2`, and
`0<=L<=floor(A/Lambda)`,

\[
\boxed{\sum_{\ell=0}^{L}M_\ell^2
\le 1+\frac{1728}{\Lambda}\sum_{d=1}^{L}\frac1d.}
\]

This is a new paper bound on the actual coupled family, including separately
chosen maximizing intervals. Its proof uses rational radial derivative
bounds, discrete cotangent summation and Bessel's inequality. It holds for
arbitrary angular data, hence does not select lag zero. At the mission schedule
some lag among `0,...,floor(log^3 A)` has `M_ell=O(log^-3/2 A)`. This is
explicitly **not** a result at the required observer. [CF-1/2](front_cf/PROOFS.md).

## The source-jet coupling is signed, and its limits do not commute

Set `tau=2-sqrt(2)`, `sigma=1-tau^8`, `K=8(16-tau^8)`. With
`v(s)=1-(1-s)^(1/8)`, define positive rational coefficients by

\[
\frac{4v(s)(16/(1-s)-1)}{1-2v(s)-v(s)^2}
=\sum_{k\ge1}b_ks^k.
\]

The unique m-delay jet polynomial is
`P_m(E)=-sum_(k=1)^m b_k(1-E)^k`. For every n,m>=1,

\[
\boxed{\varepsilon_m(n):=r_o(n)+P_m(E)Z_n>0,\qquad
\varepsilon_m(n)\sim\frac{(m+1)!b_{m+1}}{32n^{m+2}}
\quad(n\to\infty,\ m\text{ fixed}).}
\]

But for every fixed n, writing a=n+1/8,

\[
\boxed{\varepsilon_m(n)\sim
\frac{K\Gamma(a)}{64\sigma(1-\sigma)}
\sigma^{-m}m^{-a}\longrightarrow+\infty.}
\]

The same interior zero of the authenticated radial Mellin density proves a
broader impossibility: no fixed coefficient stencil with finite lookback and
an ordinarily convergent infinite future can reconstruct `-r_o(n)` from
radial differences for every sufficiently large n. Conditional convergence
is included. Time-dependent coefficients and other summation domains are
outside that no-go theorem. [AD-1–3](front_ad/PROOFS.md),
[BE-03](front_be/PROOFS.md).

There is also a positive joint-order theorem, so the divergence must not be
overstated. With one absolute C, for all n,m>=1,

\[
0<\varepsilon_m(n)\le C\sigma^{-m}
\left[\mathrm B(n+\tfrac18,m+2)+256^{-n}\right],\qquad
\varepsilon_n(n)\le C(4\sigma)^{-n}.
\]

The last choice uses n future delays and coefficients whose absolute sum is
of order `(2/sigma)^n`. It is a controlled source approximation, not a
convergent fixed infinite observer. Even then, putting `B(n)=P_n(E)Z_n`,

\[
\sum_{n=A}^{2A-2}|e(H_AB(n+1))-e(H_AB(n))|
\sim\frac{45\pi}{128}\Lambda_A.
\]

Exponential Ward accuracy therefore leaves the critical variation cost.
[Uniform proof AD-3b](front_ad/PROOFS.md), [variation BE-04](front_be/PROOFS.md).

The direct signed-Weyl attempt retains both angular and radial factors in
van der Corput's correlation. The coherent same-forcing seed gives two
decaying marginal lag means, yet their mixed covariance tends to one.
The missing original-zero-seed estimate concerns realized signed carry-cell
visits, not an uncomputed transport error. [Attempt and falsifier](SIGNED_WEYL.md).
