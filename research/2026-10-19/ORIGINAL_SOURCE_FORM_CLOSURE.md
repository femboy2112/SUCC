# Original first-window form: closure, constrained core and response domains

**CLASSICAL / PROVED (paper), source formula explicitly identified below.**
This note discharges a form-closure premise for the displayed original
first-window operator. It does not prove the inherited numerical high
coercivity estimate, its source identification, the sign of the low Schur
form, or RH. No Lean verification is claimed. It is a principal derivation
for Theorem Forge II, independent of the finite inverse-response calculation.

## 1. Exact source and scope

Let `I=(-1/2,1/2)`, `H=L²(I)`, and let `Zh` denote zero extension to the real
line. Use the unitary angular-frequency Fourier transform. Put

\[
d_j=4j+1,\quad
(E_jh)(x)=\int_I e^{-d_j|x-y|/2}h(y)\,dy,\quad
\Gamma_j=\frac4{d_j}I-E_j.
\]

On smooth compactly supported primitives the authentic source form is

\[
q(h,k)=\sum_{j\ge0}\langle\Gamma_jh,k\rangle+
\langle Kh,k\rangle,
\quad K=-C I-w A_b+2(c\otimes c)-2(s\otimes s),
\]

where `b=log 2`, `w=(log 2)/sqrt 2`, `c(x)=cosh(x/2)`,
`s(x)=sinh(x/2)`, and
`A_bh(x)=Zh(x+b)+Zh(x-b)` restricted to `I`.
The contact is the canonical source constant
`C=log(8π)+EulerGamma+π/2`. A rank-one term means the self-adjoint map
`h ↦ <h,c> c`, using the inner product linear in its first argument.
Every term in `K` is bounded and self-adjoint. For example `||A_b||≤2`;
the stronger first-window disjoint-support bound is unnecessary here.

This is precisely the primitive action recorded in
`observational_succ/original_continuum_residual.py::exact_piecewise_primitive_action`
at PR179, with the **infinite** Gamma sum in place of its finite evaluator.
The underlying source is blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`.
The constant above incorporates the conversion of the source's Gamma contact
to the rungs `4/d_j I-E_j`; it is not a freely chosen contact perturbation.

Primary comparison: Suzuki, *Weil's quadratic form via the screw function*,
[arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3), §1–2, already treats
the localized lower-bounded closed Weil form and canonical operator, with
attribution to Connes–Consani and Connes–Consani–Moscovici. Thus closure itself
is **classical**, not a new SUCC theorem. The point here is an explicit
core/domain argument for the repository's rung expansion and four-moment
restriction. Equality with that canonical Weil source is a separate analytic
identification, not something a file hash or this abstract argument proves.

## 2. Closed positive Gamma form

**Theorem C1.** Define

\[
m(\xi)=\sum_{j\ge0}\frac{16\xi^2}{d_j(d_j^2+4\xi^2)},\qquad
\mathcal Q=\{h\in H:\int_{\mathbb R}m(\xi)|\widehat{Zh}(\xi)|^2d\xi<\infty\}.
\]

Then `qΓ(h)=∫m|hat Zh|²`, with domain `Q`, is densely defined, nonnegative
and closed. The full form `q=qΓ+<K·,·>` is closed and bounded below on the
same domain. It has its canonical self-adjoint form operator `H∞`.

**Proof.** The Fourier multiplier of convolution by the full exponential kernel is
`4d_j/(d_j²+4ξ²)`. Consequently each rung has the displayed nonnegative
multiplier, and its form agrees with the restricted kernel operator on `I`.
Monotone convergence sums the nonnegative integrands. The weight `1+m` is
finite and continuous: the rung tails converge locally uniformly by comparison
with a constant times `ξ² sum d_j^-3`. The weighted Fourier space is complete;
the zero-extension support condition is closed under its stronger-than-L²
norm. This proves closedness. Moreover

\[
0\le m(\xi)\le |\xi|\sum_{j\ge0}4d_j^{-2}\le5|\xi|,
\]

using `(d_j-2|ξ|)²≥0` and an integral bound on the series. Thus smooth compact
functions lie in `Q`, proving density. Bounded self-adjoint perturbation
preserves closedness and lower boundedness, and the representation theorem
gives `H∞`. None of these steps asserts positivity of the complete signed form.
QED.

## 3. Compact smooth and constrained form cores

**Theorem C2.** `C_c^∞(I)` is a form core. If `E` is the common kernel of
finitely many linearly independent polynomial moment functionals on `H`, then
`C_c^∞(I)∩E` is a form core of the restricted form on `Q∩E`.

**Proof.** For `0<a≤1`, direct comparison of each rung gives
`m(ξ/a)≤a^-2 m(ξ)`. Inward dilation `h_a(x)=h(x/a)` therefore satisfies

\[
\|h_a\|_{q_\Gamma+I}^2
=a\int(1+m(\eta/a))|\widehat{Zh}(\eta)|^2d\eta
\le a^{-1}\|h\|_{q_\Gamma+I}^2.
\]

These dilation operators converge strongly to the identity in the weighted
Fourier norm as `a↑1`: first check smooth compact Fourier transforms by
dominated convergence, then use their density and the uniform bound for
`a≥1/2`. The support of `Zh_a` lies strictly inside `I`. Convolution with a
nonnegative, unit-mass, compactly supported smooth approximate identity of sufficiently small support
keeps it inside `I` and converges in the same norm, by dominated convergence
of Fourier multipliers bounded by one. Diagonal choice of dilation and
mollification proves the first core claim. The full form norm is equivalent
after adding a sufficiently large multiple of the L² norm because `K` is
bounded.

For the constrained claim choose compact smooth functions `ψ_1,...,ψ_r`
whose moment matrix is invertible. They exist: otherwise a nonzero linear
combination of the independent polynomial functionals would vanish on the
L²-dense compact smooth space. Given `h∈Q∩E`, approximate it by compact
smooth `h_n` in form norm. Their moments tend to zero by L² continuity.
Subtract the unique combination of the fixed `ψ_i` canceling those moments.
Its coefficients tend to zero, hence the correction tends to zero in form
norm. The resulting sequence belongs to `C_c^∞(I)∩E`. QED.

**Consequence.** Suppose an independently proved estimate
`q(h)≥κ||h||²`, with `κ>0`, holds for every compact smooth `h∈E`.
It then holds on the entire closed high form domain `Q∩E` by core
approximation. The high form operator `D` is self-adjoint and satisfies
`D≥κI`, so `D^-1` exists boundedly with norm at most `κ^-1`.
This transfers an **all-input core estimate**. A finite polynomial matrix
estimate cannot substitute for that premise.

The repository's relevant `E` is the orthogonal complement of polynomial
moments of degree at most three, with its parity decomposition. The same
argument works in each parity: use parity-preserving dilation/mollification
and symmetrized fixed moment correctors for the independent constraints
(moments 0,2 for even primitives and 1,3 for odd primitives). Thus it supplies the closure step
needed for the inherited parity bounds `63/500` and `153/500`, **conditional
on the correctness of those independently derived source/core inequalities**.

The inherited derivative statement covers this entire constrained compact core.
For any `f∈C_c^∞(I)∩E`, set `u=f'`. Integration by parts gives `∫u=0` and
`<u,P_k(2x)>=-<f,(P_k(2x))'>=0` for `k=1,...,4`, since those derivatives
have degree at most three. The primitive map satisfies `Vu=f` by the left
endpoint condition. Thus the derivative `Q4` quantifier includes every such
`f`; primitive parity reverses derivative parity. This proves core coverage,
not the inherited numerical Bessel bound or the signed-source identity.

## 4. Actual response domains and nonorthogonal low coordinates

For `h∈H¹_0(I)`, the bound `m≤5|ξ|` shows that the full-line Gamma multiplier
applied to `Zh` belongs to L². Pairing with form-domain tests proves that
`h∈Dom(H∞)` and that the operator action is the restricted multiplier plus
`Kh`. In particular, the original low primitives `F_i=V(P_i)`, `i=1,...,4`,
and the clamped polynomial response packets lie in the operator domain.
For `h∈Dom(H∞)∩E`, restriction of the form gives `h∈Dom(D)` and
`Dh=Q_E H∞h`.

The span of the four primitives is **not literally `E^⊥`**: the third and
fourth primitives contain degree-four/five polynomial parts. Work instead in
the original finite coefficient space. Let `F:c↦sum c_iF_i`, define
`A=F*H∞F`, `B=Q_EH∞F`, and keep the actual derivative-coordinate metric when
quoting eigenvalue bounds. Then, whenever the preceding positive high bound
holds,

\[
\inf_{x\in\mathcal Q\cap E} q(Fc+x)
=c^*(A-B^*D^{-1}B)c.
\]

Indeed, complete the square in the closed positive `D` form; its minimizer is
`x=-D^-1Bc`. This derivation needs no false primitive-space orthogonality.
For any finite response map `U` into `Dom(D)`, expand the square to obtain

\[
A-B^*D^{-1}B
=A-B^*U-U^*B+U^*DU-(B-DU)^*D^{-1}(B-DU).
\]

The signed source identity and high coercivity remain distinct obligations.
This note establishes closure and the transfer/domain steps for the specified
operator. It does not establish the missing positive Schur margin.

## 5. Hypothesis controls and authority

Replacing nonnegative rungs by arbitrary signed terms invalidates monotone
positive-form summation. A merely densely defined positive quadratic expression
need not be closable: on finite sequences in ℓ², `q(a)=|sum_n a_n|²` has vectors
`a^(N)=N^-1 sum_{n≤N}e_n` tending to zero, mutually zero in q-distance, but
`q(a^(N))=1`. Thus positivity alone was not our closure argument.

Closedness of the ambient form does not make an arbitrary dense subset a form
core; the inward-dilation/moment-correction proof is load-bearing. The moment
functionals used here are bounded on L² and have fixed compact smooth
correctors. No passage from numerical finite matrices to uniform coercivity
occurs. No topology, source channel, coordinate metric, or endpoint condition
has been silently strengthened.
