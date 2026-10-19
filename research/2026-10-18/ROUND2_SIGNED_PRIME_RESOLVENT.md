# A whole-residual inverse bound for the original first-prime Weil window

**Status:** paper proofs and exact rational instance certificates. No Lean
kernel authority is claimed here. This is a strict improvement of a sufficient
lower enclosure for the original signed form; its sign remains unresolved.
**RH PROVED: NO.**

## 1. Source, carrier and relation to earlier drafts

The base is PR177, commit `f309d9104ba480c1999c962af1df7c50f19e1bfe`.
The archived `observational_succ/source_weil_hierarchy.py` is Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, originating in the imported
FuckingRH source at commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`.
The unchanged continuum residual module has blob
`f5dd37fa99a109ca614ae52dd6b67d2cadcb4f48`; the inherited Bessel budget module
has blob `273260238ab1d345ab176329ade8231ac6e2ee26`; the polynomial bridge
has blob `60faf47809fb2b55f4a48f12fbae8aec7b06007b`.

The primary source is [Suzuki, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3),
especially its original screw function and primitive quadratic form.
The source normalization below is derived directly from that screw function
and checked against the frozen code. A Git hash authenticates retained bytes;
it does not prove the analytic identity. The derivation is paper authority.

PR161, head `eb62620300add80f8b38ebf0f7cd54c2a3c5ae36`, already derives
`D >= kappa I + w(I-A_log2)` from the scalar Bessel budget and the exact
prime mismatch. PR177 uses a few test moments of the residual to exploit
that comparator, while explicitly leaving its source proof as a sibling
paper premise. We independently replay the underlying rational budget with
a separate factorial implementation and supply the source, moment and form
closure argument here. This is not independent provenance or a blind audit.

PR179, head `81684b4b8956f9f5da56c376ba7e4339277eb665`, was inspected.
Its retained leading Gamma-tail Laplacian is a different method and is not
imported. No code or new Gamma constants from PR178 are imported. The new
calculation uses precisely PR177's original trials, finite source errors,
Gamma action errors, energy tail and fixed Young parameter `eta=1/4`.

The new step is to apply the non-scalar inverse to the **whole nominal
continuum residual first**, and then pay the existing source errors in that
inverse norm. It avoids the loss of observing only a few residual moments
and the additional loss of paying those source errors again inside the
saving terms. The inverse identity and Young inequality are classical. The
source-specific strict signed enclosure below is a project result; no
academic novelty beyond this explicit application is asserted.

## 2. Exact signed source and primitive completion

Let `I=(-1/2,1/2)`, `b=log(2)`, `w=b/sqrt(2)`, and
`C=-psi(1/4)+log(pi)`. Extend functions by zero outside `I`. Set
`A_b F(x)=1_I(x)(F(x-b)+F(x+b))`. Let `c(x)=cosh(x/2)` and
`s(x)=sinh(x/2)`. The source has one real Gamma factor and its original two
completed poles; there is no character or conductor substitution.

For a zero-mean derivative input `u`, write
`F(x)=int_{-1/2}^x u(t)dt`. Thus `F in H^1_0(I)` and
`<u,Ku>=||F||_2^2`, where `K=V*V`. The high derivative subspace is
orthogonal to Legendre modes `P_0,...,P_4` (on `2x`). Integration by parts
shows exactly that its primitive lies in

`E={F in L2(I): <F,x^j>=0, j=0,1,2,3}`.

Indeed `P'_1,...,P'_4` span these four polynomials; endpoint terms vanish.
Derivative odd parity gives primitive even parity; derivative even gives
primitive odd. The latter automatically has a fifth vanishing moment,
`<F,x^4>=0`. These are actual orthogonal projections, not high-mode indices
on the derivative carrier reused without transport.

For `d_j=4j+1`, direct distributional differentiation of the original screw
channels yields the primitive finite-Gamma operator

`H_J=(sum_{j<J}4/d_j-C)I - sum_{j<J}E_{d_j/2} - w A_b +2|c><c|-2|s><s|`,

where `E_a F(x)=int_I exp(-a|x-y|)F(y)dy`. The checks are:

- pole `-8(cosh(t/2)-1)` gives `-g''=2cosh(t/2)`;
- contact `C|t|/2` gives `-C delta_0`;
- prime `w(|t|-b)_+` gives `-w(delta_b+delta_-b)`;
- Gamma rung `-4/d^2+4 exp(-d|t|/2)/d^2` gives
  `(4/d)delta_0-exp(-d|t|/2)`.

At this window `|x-y|<1`: `log2<1<log3`, so the prime-2 hinge is the
complete prime-power source. No omitted prime or composite label enters.
The factor `w=log2/sqrt2` is the original half-density.

With Fourier transform `Fhat(xi)=int exp(-ixi x)F(x)dx`, the positive Gamma
multiplier is

`m_J(xi)=sum_{j<J} (4/d_j) xi^2/(xi^2+d_j^2/4)`.

The infinite increasing limit `m` defines the closed nonnegative form
`(2pi)^-1 int m |Fhat|^2`. Its domain `Q` consists of the zero-extended
`L2(I)` functions for which this integral is finite. The signed source form
`q` is this form plus the displayed bounded contact, prime and rank-two
pole terms. Thus it is closed and lower semibounded on `Q`.

Here is an explicit core argument, so passing from smooth experiments to
this completion is an obligation with a proof. Shrink the support by
`F_r(x)=F(x/r)`, `r<1`, and then mollify inside `I`. Dilation is strongly
continuous in the weighted Fourier norm because
`m(lambda xi)<=max(1,lambda^2)m(xi)`, term by term, and compact-frequency
functions are dense in that weighted space. Mollification converges by
dominated convergence. Hence `C_c^infinity(I)` is a form core. To retain
four zero moments, fix a nonnegative smooth interior bump `eta`, positive
on an interval, and subtract linear combinations of `eta x^j`, `j<=3`.
Their moment matrix is strictly positive definite: a nonzero degree-three
polynomial cannot vanish on an interval. The correction coefficients tend
to zero because moments are L2-continuous; their form norms therefore tend
to zero. Reflection symmetrization gives the parity cores. Consequently
`E intersect C_c^infinity(I)` is a core for the high restricted form.

This is a primitive `K`-Hilbert completion. It is **not** a claim that the
original derivative `L2` operator has a positive spectral gap. The original
smooth signed Weil form agrees with `q` by the channel calculation; closure
then fixes the extension used here.

## 3. Independent all-high budget and retained arithmetic surplus

**Theorem 1 (source-specific high form bound).** On `Q intersect E`,
with the parity convention just given,

`q(F)>= kappa ||F||^2 + w ||F_C||^2 + w ||F_R-T_b F_L||^2`,

where `kappa=63/500` for even primitives and `153/500` for odd primitives,
`L=(-1/2,1/2-b)`, `C=(1/2-b,b-1/2)`, `R=(b-1/2,1/2)`, and the edge
translation identifies `L` with `R`.

Proof of the all-high scalar part. The normalized Legendre Fourier
coefficients give, for a high primitive of the specified parity,

`|Fhat(xi)|^2 <= ||F||^2 sum_active (2ell+1) j_ell(xi/2)^2`.

For even primitives the active modes are `ell=4,6,...`; for odd primitives
they are `5,7,...`. Bessel's inequality is on the complete infinite tail,
not a finite Galerkin positivity claim. Monotonicity of `m_256` gives

`q_Gamma(F)>= [m_256(Omega)-W]||F||^2`,

`W=(2/pi) int_0^(Omega/2) [m_256(Omega)-m_256(2z)] sum_active (2ell+1)j_ell(z)^2 dz`.

The independent verifier uses `Omega=16, L=20` in even primitive parity,
`Omega=18,L=21` in odd parity, 128 spectral cells, Taylor order14, slack
`1/2000`. On each cell it exactly integrates each squared mode polynomial
and uses the multiplier gap at the left endpoint. Its coefficient formula

`j_ell(z)=sum_{k>=0} (-1)^k 2^ell(ell+k)! z^(ell+2k)/(k!(2ell+2k+1)!)`

follows the [NIST spherical Bessel expansion](https://dlmf.nist.gov/10.53.E1).
The absolute coefficient remainder is bounded by its first omitted term
over `1-r`, with
`r=Z^2/[2(K+2)(2ell+2K+5)]<1` at each right endpoint `Z`.
The Young slack bounds the exact square. Modes beyond `L` are bounded by
`|j_ell(z)|<=z^ell/(2ell+1)!!`; after integration their entire tail is at
most `Z^(2L+1)/[(2L+1)!!^2(1-(Z/(2L+3))^2)]`.
This includes unused opposite parity modes, which is conservative.

The source contact and `w` use outward intervals from the frozen module.
The negative sinh pole is zero for even primitives. For odd primitives
its Taylor moments through degree4 vanish, and its total negative leakage
is at most `8(1/4)^10/(5!)^2`. Discard the positive cosh pole. Subtracting
contact, `w`, and this pole budget leaves exact rational margins whose
outward displays include

- even primitive: `0.12610039071948304... > 63/500`;
- odd primitive: `0.3062210359479094... > 153/500`.

The separately coded factorial/integral verifier agrees **exactly**, as
Fractions, with the inherited recurrence/global-antiderivative calculation.
This rotates implementation; both still share the source and analytic
Bessel theorem. The tests do not confer Lean authority.

Finally `A_b` swaps the two edge intervals and vanishes at the center, so

`||F||^2-<F,A_bF>=||F_C||^2+||F_R-T_bF_L||^2`.

The scalar budget replaced the prime term by `-w||F||^2`; retaining the
identity adds exactly the displayed nonnegative mismatch. This is not a
second use of the same prime term. Core continuity proves the bound on
`Q intersect E`. QED.

## 4. Whole-residual inverse certificate

Fix primitive reflection parity `sigma`, and write `E_sigma` for the
intersection of `E` with that parity subspace. Choose its corresponding
`kappa` from Theorem1. Let `w0=12/25<=w`,
`B=kappa I+w0(I-A_b)` on ambient `L2(I)`, and let `D` be the high closed
source operator on `E_sigma`. Theorem1 gives `D>=B_(E_sigma)` as forms.
Although `E_sigma` does not reduce `A_b`, variational maximization over
`E_sigma` is bounded by maximization over all of `L2(I)`. Thus for
`r in E_sigma`,

`<r,D^-1r> <= <r,B^-1r>`.

No commutation of the high projection with `A_b` is assumed.
Inverting the center scalar and the edge two-by-two block gives exactly

`<p,B^-1p>=kappa^-1||p||^2-alpha||p_C||^2-beta||p_R-T_b p_L||^2`,

`alpha=w0/[kappa(kappa+w0)]`, `beta=w0/[kappa(kappa+2w0)]`.

**Theorem 2 (complete residual bound with nominal inverse first).** Let
`r_i=p_i+e_i in E_sigma`, `i=1,2`, with `p_i,e_i in L2(I)` and
`||e_i||<=delta_i`. For every `eta>0`
and every coefficient vector `z`,

`<sum z_i r_i,D^-1 sum z_i r_i>`

`<= (1+eta)<sum z_i p_i,B^-1 sum z_i p_i>`

` + (1+1/eta) kappa^-1 (delta_1^2+delta_2^2)||z||^2`.

Proof: Young in the `B^-1` inner product, `B^-1<=kappa^-1 I`, then
Cauchy--Schwarz on `sum z_i e_i`. This pays each original action error
once. The full nominal center/edge norms need no further original-action
error correction. QED.

For PR177's lawful clamped trials, `h_i` and `h_i'` vanish at both endpoints;
the zero extension is `H2`, justifying its selected H1/H2 Gamma action
bounds. Set `r_i=Q_E H_infinity h_i`. The exact piecewise polynomial
`p_i=Q_E approximate(H_J h_i)` has exactly the inherited full continuum
residual Gram `M`; code requires exact equality, not matching diagonals.
The residual errors are unchanged finite source plus infinite Gamma errors.
The original outward finite signed trial matrix and valid whole energy-tail
matrix remain unchanged as well.

The original Schur quantity is interpreted as the variational shorting,
not as an assumed bounded inverse on derivative L2. If `h_z` is a clamped
representative of a fixed low derivative vector and `r_z=Q_(E_sigma)Hh_z`,
then completion of the square in the closed high form gives

`inf_(v in Q intersect E_sigma) q(h_z+v)=q(h_z)-<r_z,D^-1r_z>`.

The original high derivative experiments map to `H1_0 intersect E_sigma`,
which contains the form core established in Section 2. Hence their infimum
is the same: completing the carrier introduces no smaller hidden
variational value. The clamped representative differs from the original
low primitive only by a lawful high derivative combination, so the
infimum is the original low Schur/shorted form. This justifies applying
Theorem 2 to the original `S4` even when no derivative-L2 inverse exists.
The statement is per parity block; reflection symmetry gives their direct
sum.

For clarity, the inherited infinite error allowance also has an elementary
source proof. Each authentic Gamma rung satisfies
`m_j(xi)/|xi|<=4/d_j^2` and `m_j(xi)/xi^2<=16/d_j^3`.
Integral comparison of the progression tails therefore gives
`||Gamma_tail h||<=min((1/d+4/d^2)||h'||,(2/d^2+16/d^3)||h''||)`
for these clamped trials, with `d=4J+1`. The second bound requires the
zero extension to be H2; the first only H1. For the energy,
`1/(1+t)>=1-t` gives the valid matrix lower
`(2/d^2)Gram(h')-(4/d^4+64/d^5)Gram(h'')`.
The calculation selects that entire matrix only if its exact minors are
nonnegative; otherwise it selects the independently valid zero lower.
It never clips an indefinite matrix to its positive part. The finite
signed source entries are outward intervals, and their symmetric radius
matrix is bounded by subtracting its row sums from the diagonal. These
choices give a Loewner lower for every linear combination, not merely
separate diagonal tests.

We integrate the entire nominal center functions on
`C0=[-3/16,3/16]` and entire nominal edge differences on
`R0=[1/5,49/100]`. These lie strictly within the correct source regions for
every allowed `b`. Omitting the rest only discards nonnegative savings.
The only new uncertainty is translating the known nominal left polynomial
at exact `b`, rather than its rational center `b0`. If `|b-b0|<=db`,

`||p_L(. - b)-p_L(. - b0)||_(L2(R0)) <= db ||p_L'||_(L2(L0))=:epsilon_i`.

Every intermediate translated point lies in the same nominal left cell
`L0`; the code verifies this geometry before using the derivative bound.
Cauchy--Schwarz and integration of the fundamental theorem of calculus
prove the estimate. For `theta=1/1024`,

`E_true >= (1-theta)E_nom -(1/theta-1)sum epsilon_i^2 I =: E_lower`.

No positive-part clipping of this potentially indefinite lower matrix is
allowed. With exact full center Gram `C_nom`, the saving matrix is
`G=alpha C_nom+beta E_lower`. Therefore the new original signed Schur
lower is exactly

`L_new=L_PR177+(1+eta)G`.

This statement is valid even if `G` is indefinite. The reported strict
improvement requires both exact leading principal minors of `G` positive.
All matrix entries in the receipts are exact rational strings. The bulky
all-high audit rationals are exported as outward rational brackets and
exact signed-hex numerator/denominator hashes; verification itself uses
unrounded Fractions. Decimal summaries are illustrative only.

## 5. Replays, limits and next discriminator

`ROUND2_FULL_PRIME_J8.json` records the full actual J8/M80/P18 computation.
The matrix coordinates are the unnormalized derivative modes
`(P1(2x),P3(2x))` and `(P2(2x),P4(2x))`, respectively, in that order.
Both exact saving matrices are positive definite. Their approximate gains,
in derivative parity order, are

```
odd:  [[0.0001347423913, 0.0000523934359],
       [0.0000523934359, 0.0000258750274]]
even: [[0.0003104342092, 0.0002185365241],
       [0.0002185365241, 0.0001548767719]]
```

Both new signed lower matrices are still negative definite. That is failure
of this sufficient enclosure to prove positivity, not a negative-energy
witness for the true source form. It does not refute source positivity or
RH. No prime3/square extension is attempted before this first window is
settled.

The deeper fresh J24/M192/P18 replay also strictly improves both blocks,
with all inherited source errors unchanged:

| Derivative parity | Old lower diagonal | New lower diagonal | Old / new off-diagonal |
|---|---|---|---|
| odd | -0.0009810781, -0.0005687345 | -0.0006774810, -0.0004401199 | -0.0004125703 / -0.0002164644 |
| even | -0.0012647738, -0.0009414402 | -0.0006133623, -0.0004961893 | -0.0008437744 / -0.0003067837 |

`ROUND2_FULL_PRIME_J24.json` holds exact rational matrices. Both gains are
positive definite by exact Sylvester minors; both new lower matrices are
negative definite by the same exact criterion applied to their negatives.
The first diagonal shortfall falls by approximately 31% in the odd sector
and 51% in the even sector. These are improvements of this particular
sufficient lower bound, not probabilities or estimates of true energy.
The fresh J24 run completed in 177.09 seconds with 43,316 KiB peak memory,
inside its 240 CPU-second and 1 GiB address-space limits. J8 completed in
18.67 seconds with 27,400 KiB peak memory. Neither computation reads any
nontrivial zero location.

The hostile paper audit identified a necessary exposition repair: the
larger `153/500` constant must be applied only on the odd-primitive parity
space. Section 4 now explicitly fixes `E_sigma`, and the residual theorem
requires its true residuals to lie in that same space. The code always
separated the two parity blocks; no numerical result changed. Another
agent reconstructed all J8 center/edge/error/gain identities from exact
receipts and independently rederived the source, core, Bessel and inverse
arguments. These checks share the source and team context; they are not
independent source authentication or blind external peer review.

The initial actual J8 calculation returned but saving its huge audit
rationals exceeded Python's integer-to-text safety cap. The failure receipt
is retained; the repaired successful run records its command, interpreter,
resource bounds and elapsed time. The repair changes serialization only.
The next discriminating experiment is to fit lawful clamped trials against
the non-scalar inverse metric itself, rather than against the old scalar
proxy. Any such attempt must retain the whole signed energy and the full
continuum residual; a smaller nominal Gram alone is not sufficient.
