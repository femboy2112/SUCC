# A finite constructive successor presentation of the SU(2) Wilson state

Parent: `3929e30930438881bebcb371646389d9e66bfbde`. Date: 2026-11-13.
Status: **classical representation theory, explicit source adapter and proved
finite approximation algorithm**. No priority claim and no full 4d reproduction.

The companion [QM/YM interface](QM_YM_INTERFACE.md) gives the representation,
finite-lattice extension, primary sources and physical-domain boundaries. This
file specifies and proves the exact finite algorithm implemented in
[ym_succ_character.py](../../../../observational_succ/ym_succ_character.py).

## 1. The existing carrier has a literal SU(2) character interpretation

The existing intrinsic carrier is H = ell2(N at least 1), with S e_m=e_(m+1)
and S*e_1=0. Reindex e_(n+1) as f_n for this proof and the Python arrays. Then

\[
J=(S+S^*)/2,\qquad
Wf_n=U_n(x),\qquad x=\operatorname{Tr}(g)/2.
\]

For normalized Haar measure on SU(2), the central trace law is

\[
d\nu(x)=\frac2\pi\sqrt{1-x^2}\,dx,
\qquad x\in[-1,1].
\]

One way to check the normalization directly is to identify SU(2) with the
unit 3-sphere and x with its first coordinate. Its normalized slice density
is the displayed semicircle law. Under x=cos(theta), the density becomes
(2/pi) sin²(theta) dtheta for 0<=theta<=pi.

Since U_n(cos(theta))=sin((n+1)theta)/sin(theta), sine orthogonality proves
that the U_n are orthonormal. They span all polynomials by degree and leading
coefficient, and polynomials are dense in this L2 space. Therefore W is unitary
onto the **central** Haar space, not onto every matrix-coefficient sector of
L2(SU(2)). The recurrence

\[
2xU_n=U_{n+1}+U_{n-1},\quad U_{-1}=0
\]

gives W J W* = M_x. This is exactly the fundamental-representation fusion
rule. The fuller product is

\[
U_mU_n=\sum_{j=0}^{\min(m,n)}U_{m+n-2j}.
\]

Reindexing transports the old multiplier too: V_p f_n=f_(pn+p-1).
Replacing that by f_(pn) would change the established operator.

### 1.1 The existing multiplication operator is weighted Chebyshev composition

This second map connects both of the established integer operations to the
same SU(2) representation. For every integer p>=1, let T_p be the Chebyshev
polynomial of the first kind. In the original positive-integer indexing,

\[
V_p e_m=e_{pm},\qquad
(WV_pW^*f)(x)=U_{p-1}(x)f(T_p(x)).
\]

To prove the identity, use x=cos(theta) and the sine formula to obtain

\[
U_{pm-1}(x)=U_{p-1}(x)U_{m-1}(T_p(x)).
\]

This is a polynomial identity, so the apparent sine denominators at special
angles are removable. It proves the formula on the character basis. There
is also a direct check on the entire L2 space: with w_p=U_(p-1),

\[
\begin{aligned}
\|w_p(f\circ T_p)\|_{L^2(\nu)}^2
&=\frac2\pi\int_0^\pi\sin^2(p\theta)|f(\cos p\theta)|^2\,d\theta\\
&=\frac2{p\pi}\int_0^{p\pi}\sin^2u|f(\cos u)|^2\,du
=\|f\|_{L^2(\nu)}^2.
\end{aligned}
\]

The integral on each successive interval of length pi agrees by reflection
and 2pi periodicity. The identity applies to nonnegative measurable
integrands, so it also proves well-definedness modulo Haar-null sets. In sine
coordinates g(theta)=sin(theta)f(cos(theta)), extended as an odd 2pi-periodic
function, the map is exactly g(theta) -> g(p theta).

Writing C_p=WV_pW*, the basis formula immediately gives

\[
V_pJ=T_p(J)V_p,\qquad C_pC_q=C_{pq},\qquad
C_p^*U_m=
\begin{cases}
U_{(m+1)/p-1},&p\mid(m+1),\\
0,&\text{otherwise}.
\end{cases}
\]

For almost every y in (-1,1), the same adjoint has the concrete inverse-branch
formula

\[
(C_p^*g)(y)=\frac1p\sum_{T_p(x)=y}\frac{g(x)}{U_{p-1}(x)}.
\]

There are p simple interior preimages; their denominators are nonzero.
This follows from T_p'=p U_(p-1) and
1-T_p(x)^2=(1-x^2)U_(p-1)(x)^2. The character-basis adjoint specifies its
bounded extension, including all measure-zero endpoint conventions.

**The weight is essential.** For p=2 the map is 2x f(2x²-1). Bare pullback
already sends the squared norm of f(x)=x from 1/4 to 1/2. More strongly,
f(y)=[2(1+y)]^(-1/2) has Haar norm one, but f(2x²-1)=1/(2|x|) is not in
L2(nu). The weighted expression is sign(x), again of norm one. Thus omitting
the weight can destroy even the operator's domain.

Together with the existing unique-factorization occupation map, these give
explicit presentations of one carrier:

\[
\mathcal F_s(\ell^2(\mathcal P))
\cong\ell^2(\mathbb N_{\ge1})
\cong L^2_{\mathrm{central}}(SU(2)).
\]

For prime p, V_p is a normalized creator in the first presentation and C_p
in the last. Composite p has the same weighted-composition formula; this
does not provide a prime detector, an arithmetic-source identification,
or a Yang–Mills dynamics claim. Exact polynomial and norm controls for
p=1,...,7 and m=1,...,8 are recorded by the committed reproduction probe.

## 2. The Wilson state, with its source attached

For real beta, put

\[
Z_\beta=\langle f_0,e^{\beta J}f_0\rangle
       =\int e^{\beta x}\,d\nu(x),\qquad
\psi_\beta=Z_\beta^{-1/2}e^{\beta J/2}f_0.
\]

Then for every bounded measurable f of the trace coordinate,

\[
\langle\psi_\beta,f(J)\psi_\beta\rangle
=\frac{\int f(x)e^{\beta x}\,d\nu(x)}{Z_\beta}.
\]

For one square plaquette, the product of four independent Haar link matrices,
with the prescribed orientation inverses, is Haar: hold three links fixed
and integrate the fourth using Haar invariance. A class observable and the
single plaquette action depend only on that holonomy.

This is the actual one-plaquette Wilson law: the native action is 1-x, and
the constant exp(-beta) cancels in the normalized expectation. It is a chosen
source instantiation; an existing arithmetic vector need not equal psi_beta.

The relation to a source-adapted Haar basis is also exact. Let
dmu_beta=e^(beta x)dnu/Z_beta. The unitary

\[
R_\beta:L^2(\mu_\beta)\longrightarrow L^2(\nu),
\qquad R_\beta f=Z_\beta^{-1/2}e^{\beta x/2}f
\]

sends the commutative GNS cyclic vector 1 to W psi_beta and intertwines
multiplication by x. Thus W* R_beta is a source-preserving identification
between the Wilson GNS representation and the successor carrier. Composing
with a complete source-weighted Haar transform gives a third representation
of the same observable-state system. This does not identify a finite Haar
truncation with the full representation.

## 3. Exact finite paths and their first failure

Let P_N project onto f_0,...,f_N and J_N=P_N J P_N on that finite space.
Every edge has amplitude 1/2. A length-k vacuum return path cannot visit N+1
unless k>=2N+2. Hence

\[
\langle f_0,J_N^k f_0\rangle
=\langle f_0,J^k f_0\rangle\quad(0\le k\le2N+1).
\]

At length 2N+2 precisely the path that rises monotonically to N+1 and then
returns is first omitted. Its weight gives

\[
\langle f_0,J^{2N+2}f_0\rangle
-\langle f_0,J_N^{2N+2}f_0\rangle=4^{-N-1}.
\]

All odd moments vanish. Counting nonnegative return walks by reflection gives
the Catalan number at length 2k, and therefore

\[
\langle f_0,J^{2k}f_0\rangle
=\frac1{4^k}\frac{\binom{2k}{k}}{k+1}.
\]

This recovers the preceding round's Haar formula by an independent path
construction. The boundary is essential: the bilateral successor instead
gives binomial(2k,k)/4^k. Even the second moments differ: 1/4 versus 1/2.

Compression is not a product-preserving map:

\[
P_NJ^2P_N-J_N^2=\frac14|f_N\rangle\langle f_N|.
\]

Every use of a polynomial observable must therefore pay its path horizon.

## 4. A finite rational pure state and a universal error budget

Let beta be rational, K>=0, and

\[
u=e^{\beta J/2}f_0,\quad
v_K=\sum_{j=0}^{K}\frac{(\beta J/2)^j}{j!}f_0,
\quad \phi_K=v_K/\|v_K\|.
\]

The unnormalized vector has rational coefficients and support in 0,...,K.
Its normalized density |v_K><v_K|/||v_K||² also has rational entries. A
square-root extension is needed only if normalized amplitude coordinates are
explicitly requested. This is a positive state on the full finite matrix
algebra, not merely a list of moment values.

Set b=|beta| and a=b/2. Since ||J||<=1, the exponential tail gives

\[
\|u-v_K\|\le\delta_K
 :=e^a\frac{a^{K+1}}{(K+1)!}.
\]

The odd Haar moments are zero and the even ones nonnegative. Thus
\(\|u\|^2=Z_\beta\ge1\) and \(\langle f_0,v_K\rangle\ge1\),
so v_K is never zero. For nonzero u,v,

\[
\left\|\frac u{\|u\|}-\frac v{\|v\|}\right\|
\le\frac{2\|u-v\|}{\|u\|}.
\]

It follows for every bounded operator A with ||A||<=M that

\[
|\langle\psi_\beta,A\psi_\beta\rangle
-\langle\phi_K,A\phi_K\rangle|
\le4M\delta_K
\le\boxed{4M\,3^{\lceil a\rceil}
                 \frac{a^{K+1}}{(K+1)!}}.
\]

The last expression is rational for rational beta and M. The middle statement
uses A on the common infinite carrier and the finitely supported phi_K; it
does not declare arbitrary finite observable truncations exact.

For a real rational polynomial f of degree d, take M=sum_j |f_j| and

\[
N\ge K+\lfloor d/2\rfloor.
\]

The numerator <v_K,f(J)v_K> is the vacuum moment of the polynomial
P_K(beta x/2)^2 f(x), of degree at most 2K+d. The denominator has degree
at most 2K. Because 2K+d<=2N+1, both equal their finite J_N evaluations.
Consequently the exact rational finite-graph expectation has the displayed
error from the genuine Wilson expectation. This degree condition is a
uniform sufficient horizon; extra parity or zero coefficients can reduce
the minimum in individual instances.

**Constructive conclusion.** Given rational beta, a rational polynomial f,
and a positive rational epsilon, increase K until the rational error bound
is at most epsilon, choose N as above, and evaluate the finite path graph.
The search terminates: the tail-bound ratio is a/(K+2), eventually at most
1/2. At beta=0 the approximation is already exact at K=0. At f=0 the bound
and expectation are zero. No unknown moment, physical oracle or infinite
operation is an input to this procedure.

## 5. Complete Haar transport is different from a recorded measurement

The integration tests build J_N from the new graph compiler applied to the
existing successor convention, then evaluate the Wilson ray. For an 8-entry
character-coordinate vector, the complete rational Haar transform T has a
retained diagonal output metric D and satisfies T*DT=I. Transporting

\[
v\mapsto Tv,\qquad A\mapsto TAT^{-1}
\]

preserves the normalized expectation exactly. This finite character-coordinate
Haar transform is a basis change; the source-adapted configuration-space Haar
transform in section 2 is another basis change with its own specified metric.

A calibrated different operation is the existing quantum_records Z-measurement
with its outcome discarded. For beta=1, K=N=1, the Wilson approximation has
ray v=(1,1/4) and <J_1>=4/17. Dephasing this ray in the character basis gives
<J_1>=0. Normalization and positivity survive, but the state changes. This
refutes treating discard as a harmless change of computational presentation.

## 6. Claim boundary and novelty tax

The proved connection is central SU(2) representation theory plus an explicit
Wilson source, an exact finite graph algorithm and quantified approximation.
These do not make J a physical energy operator: its spectrum is [-1,1],
Jf_0=f_1/2, and exp(beta J) is not trace class. Z_beta is a matrix element,
not a Gibbs trace. Haar positivity does not identify the continuum OS quotient.

The observable algebra C*(J) is commutative. The rest of SUCC's operator
algebra can be conjugated by W, but those conjugated operators are not thereby
identified as local Yang–Mills fields. The finite-link nonabelian extension
requires matrix coefficients, representation labels and vertex intertwiners;
the continuum extension requires the actual source family, reflection domain,
scaling and uniform estimates described in the companion interface.

The old Haar moments, wavelet gates and standard representation theory retain
their classical attribution. The new work is their source-typed assembly,
constructive error contract, implementation and falsification controls.

## 7. Classical references

- NIST DLMF, [orthogonality and normalization](https://dlmf.nist.gov/18.3),
  Table 18.3.1, and [three-term recurrences](https://dlmf.nist.gov/18.9),
  Table 18.9.1. The polynomial convention here is the standard U_n(x), with
  U_1(x)=2x and x=Tr(g)/2.
- J.-B. Zuber, [Invariances and Group Theory](https://www.phys.ens.fr/sites/default/files/2024-09/zuber_invariances_and_group_theory.pdf),
  chapter 2, appendix E: SU(2) characters, orthogonality and completeness.
- The companion [interface](QM_YM_INTERFACE.md) cites the primary
  Peter–Weyl/spin-network and nonabelian lattice-duality sources, and pins the
  actual upstream Wilson action.
