# A Fourier–Yoneda pin bed with lawful dynamics

**Research date:** 2026-11-07. **Parent:** main
`d32342d375f44ddf62221ad6aff2f534abdc0a03`.
**Scope:** classical mathematics, proved here with explicit constructions;
finite exact implementation checks. No Lean certificate or scholarly-priority
claim. Original four-pole BBP forcing and literal zero seed remain fixed.

## 1. What the pin bed is intended to do

The author's metal-pin analogy is retained literally at the mathematical level:
a family of probes produces a surface; its shape is the internal representation.
The goal is to make that representation adequate for specified questions and
compatible with carrier dynamics. It need not identify irrelevant hidden data.

There are three different input types:

1. a **point/state**, such as a circle phase x;
2. a **law**, such as a probability measure mu on circle phases;
3. a **source history**, including time, forcing, seed and ordered observations.

A single character e(x) identifies a circle point and has the exact nonlinear
update e(x) -> e(a)e(x)^b. A single moment integral e(x) dmu does not identify a
law, and generally integral e(bx) dmu != (integral e(x) dmu)^b. Empirical laws
are constructed from actual histories; their definition does not assume random
sampling. We never discard the history when claiming source authentication.

Existing SUCC already proves target descent and finite behavioral closure in
[`CARRIER_RELATIVE_TARGETS.md`](../../../docs/CARRIER_RELATIVE_TARGETS.md), and
source-circle representation in [YO-01](../../2026-11-05/yoneda_circle/PROOFS.md).
The additions here are a **realizable continuous surface**, sharp dynamical
conditioning, and a constructive quantitative completion of an inadequate bed.

## 2. Carrier-relative truth is an exact positive output

Let C be a declared admissible source class, q:C -> S an observation map onto
its **realized image**, and P a property on C. For s in S define

\[
\operatorname{may}_P(s)\iff \exists x\in C:\ q(x)=s\land P(x),
\qquad
\operatorname{must}_P(s)\iff \forall x\in q^{-1}(s):P(x).
\]

**Proposition 1 (relative truth and target descent).** The statement
“indistinguishable from a P-true model under this carrier and toolkit” is exactly
`may_P(q(x))`. It is itself a well-defined, observation-invariant truth claim.
A certificate consists of an admissible witness y with P(y) and q(y)=q(x).
It remains valid if a P-false representative shares the same fiber.

The original property P descends to S iff it is constant on every fiber. In that
case may and must agree. An empty proposed fiber is OUT_OF_MODEL, not vacuous
proof of either truth value. Proof: evaluate the definitions on equal fibers;
for descent define Pbar(s) to be their common value. This reuses main's theorem.

Operational outputs are therefore separate:

| Output | What is proved |
|---|---|
| TRUE_COMPATIBLE | A target-true representative has this same imprint |
| INVARIANT_TRUE | Every admissible representative has the target |
| AMBIGUOUS_TARGET | True and false representatives both have the imprint |
| OUT_OF_MODEL | No admissible realization has the proposed readings |

TRUE_COMPATIBLE and AMBIGUOUS_TARGET can both hold; they answer different
questions. This is not a probability or a weakened proof of P. It is a proof of
the explicitly relative proposition the author requested. The code retains both
witnesses and fingerprints the source tables and the exact target table.

The quotient must be formed from a declared toolkit and closure. Selecting only
constant pins after seeing the desired answer creates a mathematically valid
but uninformative quotient. Source-map adequacy remains a separate obligation.

## 3. A literal continuous surface and its explicit inverse

Let T=R/Z with Haar probability lambda, and use
`m_h(mu)=integral exp(-2*pi*i*h*x) dmu(x)`. Set

\[
\kappa(t)=(\{t\}-1/2)^2,
\qquad B_2(t)=t^2-t+1/6,
\]
\[
H_\mu(t)=\int\kappa(t-x)\,d\mu(x),
\qquad F_\mu(t)=H_\mu(t)-1/12=\int B_2(\{t-x\})\,d\mu(x).
\]

H is the raw nonnegative pin height, between 0 and 1/4. F is its centered
surface. Haar gives the flat height 1/12, hence F_lambda=0. A source point zero
gives F_delta0=B2, a nonflat surface. **Zero source coordinate and zero
distributional discrepancy are different typed zeros.**

**Theorem 2 (surface reconstruction and realization).** On probability laws,
mu -> F_mu is injective. Its exact image consists of real continuous periodic
functions f of mean zero for which

\[
\boxed{\lambda-\tfrac12D^2 f\ \text{is a nonnegative Borel measure}.}
\]

The inverse is the explicit curvature rule

\[
\boxed{\mu=\lambda-\tfrac12D^2F_\mu.}
\]

Here D is the distributional derivative on the circle, not a sampled finite
difference. Proof: the periodic B2 is continuous, its derivative is 2t-1 off
integers, and that derivative jumps by -2 at each integer. Thus
`D^2 B2 = 2 lambda - 2 delta0`, giving `D^2 F_mu=2 lambda-2 mu`.
Conversely, the proposed measure has mass one because the derivative pairs to
zero with constants. Its surface and f have identical second derivatives;
their difference is a periodic affine function, hence constant, and their
equal zero means kill that constant. This proves both sufficiency and uniqueness.

Equivalently, the classical Bernoulli Fourier series gives

\[
\widehat F_\mu(0)=0,
\qquad
\boxed{\widehat F_\mu(h)=\frac{m_h(\mu)}{2\pi^2h^2}\quad(h\ne0).}
\]

No nonzero character is lost. Probability mass one supplies the omitted zero
mode. For arbitrary finite signed measures one must retain mass separately:
adding a Haar multiple leaves the centered B2 surface unchanged.

The map is a homeomorphism from weak probability convergence onto its image
with the L2 metric: coefficient convergence and summable squared multipliers
give forward continuity; compactness and injectivity give the inverse. This is
identification of laws, not automatic numerical stability for every functional.

**Hostile realization control.** Nonnegative raw heights alone are insufficient.
For `f(t)=cos(20*pi*t)/100`, the height f+1/12 is everywhere positive, but its
putative inverse has density `1+2*pi^2 cos(20*pi*t)`, which becomes negative.
The curvature/positivity constraint is load-bearing.

## 4. Exact affine dynamics and a genuine natural isomorphism

For b>=1 integer and a in T define `T_(b,a)(x)=bx+a`. Define on surfaces the
explicit operator

\[
\boxed{(L_{b,a}f)(t)=b\sum_{j=0}^{b-1}f((t-a+j)/b).}
\]

**Theorem 3 (naturality and composition).** For every probability law mu,

\[
\boxed{F_{T_{b,a*}\mu}=L_{b,a}F_\mu,\qquad
L_{c,d}L_{b,a}=L_{cb,ca+d},\qquad L_{1,0}=I.}
\]

Proof of naturality: the Bernoulli multiplication formula is
`sum_(j=0)^(b-1) B2({(u+j)/b})=B2({u})/b`. Substitute u=t-a-bx and integrate.
It also follows from `m_h(T_*mu)=exp(-2*pi*i*h*a)m_(bh)(mu)` and the ratio
of the B2 multipliers. Composition follows by writing the double sum with
indices k+cj, which run once through 0,...,bc-1. These identities hold at seams
because B2 is continuous there.

Let the affine monoid have multiplication `(c,d)(b,a)=(cb,ca+d)` and regard it
as a one-object category. Its action on probability laws and its explicitly
specified action on the realizable surfaces of Theorem 2 are two functors to
Set. The maps mu -> F_mu form an objectwise bijective natural transformation:
**a natural isomorphism of dynamical representations**. The image condition and
surface arrows were independently specified and proved, so this is not a
reconstruction defined merely by transporting an unknown inverse.

This is the precise Yoneda-shaped interface. Literal Yoneda concerns compatible
Hom-functors; scalar Fourier readings are not silently identified with Hom-sets.
In the category of affine-monoid actions and equivariant maps, the constructed isomorphism induces
the corresponding isomorphism of representables by ordinary Yoneda. Restricted
pins require a separate sufficiency/density or behavioral-quotient proof.
No second incompatible finite-category class is introduced into SUCC.

**Sharp norm.** For b>=2 on mean-zero L2,

\[
\widehat{L_{b,a}f}(h)=b^2e^{-2\pi iha}\widehat f(bh),
\qquad \|L_{b,a}\|=b^2.
\]

Parseval gives the upper bound. Equality holds for actual probability
differences, not merely arbitrary Hilbert vectors: uniform b-grids separated
by d/b are sent to Dirac masses separated by d, and the distance formula below
gives the squared ratio b^4. BBP's one-step constant is 256, not a contraction.
Explicitly, `F_eta_b(t)=b^-2 B2({bt})`, and a shift by d/b replaces bt by bt-d.
The map t->bt preserves Haar, so the input squared distance is b^-4 times the
Dirac squared distance. This proves sharpness using realized probability laws.

## 5. Exact spatial energy and target-error transport

Let `B4(t)=t^4-2t^3+t^2-1/30`. Its classical Fourier expansion gives

\[
C(t):=\int B_2(\{u\})B_2(\{u-t\})\,du=-\tfrac16B_4(\{t\}),
\]
\[
\boxed{E(\mu):=\|F_\mu\|_2^2
=-\tfrac16\iint B_4(\{x-y\})\,d\mu(x)d\mu(y)
=\sum_{h\ne0}\frac{|m_h(\mu)|^2}{4\pi^4h^4}.}
\]

Thus E>=0, E=0 iff mu=Haar, and E(mu_j)->0 iff mu_j converges weakly to Haar.
The last equivalence follows by isolating each fixed positive-weight term in
one direction, and dominated convergence in the other. These are classical
characteristic-kernel facts; no new normality estimate is hidden in them.

For rational empirical phases the spatial expression is **exact rational**.
Calibrations: `E(delta)=1/180` and `E(uniform q-grid)=1/(180 q^4)`.
For sorted weighted atoms `(x_i,p_i)`, an exact fast formula is

\[
E=\frac1{180}-\frac13\sum_{i>j}p_i p_j
[(x_i-x_j)^4-2(x_i-x_j)^3+(x_i-x_j)^2].
\]

Prefix moments through degree four evaluate it in linear arithmetic after
sorting. Bit complexity depends on the rational denominators. An independent
oracle integrates the piecewise quadratics directly, without using B4.

**Theorem 4 (metric and target control).** For circle distance d in [0,1/2],

\[
\|F_{\delta_x}-F_{\delta_y}\|_2^2=d^2(1-d)^2/3,
\quad
\frac{d}{2\sqrt3}\le\|F_{\delta_x}-F_{\delta_y}\|_2\le\frac d{\sqrt3}.
\]

Proof: expand the square as `2[C(0)-C(d)]` and use B4. By integrating coupled
point differences and applying the triangle inequality, any coupling pi of mu
and nu yields

\[
\|F_\mu-F_\nu\|_2\le\frac1{\sqrt3}\int d_T(x,y)\,d\pi(x,y).
\]

For periodic g in H2, integration by parts in the distributional inverse gives

\[
\boxed{|\mu(g)-\nu(g)|\le\tfrac12\|g''\|_2\|F_\mu-F_\nu\|_2.}
\]

In particular `|m_h(mu)-m_h(nu)| <= 2*pi^2*h^2 ||F_mu-F_nu||_2`.
A margin exceeding this bound certifies a corresponding threshold target.
This is a stated target-error modulus, not a truth probability. Discontinuous
targets require additional hypotheses; surface similarity alone is insufficient.

## 6. Which Fourier beds support stable dynamics?

Let nonnegative symmetric weights w_h, h!=0, have finite positive total W.
Define

\[
D_w(\mu,\nu)^2=\sum_{h\ne0}w_h|m_h(\mu)-m_h(\nu)|^2.
\]

Its zero relation is a valid observer equivalence even when some frequencies
are missing. For all-positive weights it is a metric and determines the law.

**Theorem 5 (sharp stability).** For all-positive w and fixed b>=2,

\[
\boxed{\sup_{\mu\ne\nu}
\frac{D_w(T_{b,a*}\mu,T_{b,a*}\nu)}{D_w(\mu,\nu)}
=\sup_{h\ne0}\sqrt{w_h/w_{bh}},}
\]

including infinity. The translation a does not affect this constant.
The upper bound follows by substituting the Fourier update and reindexing.
For necessity use genuine probability densities
`dmu_±=(1±epsilon*cos(2*pi*b*h*x))dx`, 0<epsilon<=1. Their difference has
coefficients epsilon exactly at +/-bh, so the before and after squared
distances are `2 epsilon^2 w_bh` and `2 epsilon^2 w_h`.

If weights have zeros, a finite bound C is equivalent to
`w_h <= C^2 w_bh` for every h. In particular observable support must be closed
under h -> bh. The same cosine witnesses prove necessity at missing modes.

Examples:

- Sobolev weights `w_h=|h|^(-2s)`, s>1/2, give sharp constant b^s.
- The continuous surface above has `w_h=1/(4*pi^4*h^4)` and constant b^2.
- An irrational aperture alpha has `w_h=sinc^2(pi*alpha*h)>0` but ratio
  `b^2 sin^2(pi*alpha*h)/sin^2(pi*b*alpha*h)` is unbounded: density of h alpha
  modulo one permits approach to 1/b, where the numerator stays nonzero and
  the denominator tends to zero. Thus the golden aperture in PR #540 remains
  characteristic but has **no global one-step Lipschitz bound in its own
  L2 discrepancy metric**. Its previously proved source-tail estimates remain
  valid. This is not discontinuity: continuous pushforward is uniformly
  continuous on compact probability space in the weak topology.

No nonzero summable weights can make this affine expansion nonexpansive on all
probability differences. A bound <=1 would force `w_h<=w_bh` and hence a
nondecreasing positive sequence on an infinite b-ray, contradicting summability.
There is no universal stronger lower bound: the completion below can approach
one as closely as desired. Keeping the original pin sensitivities while
approaching nonexpansion increases the completed weight budget.

## 7. Construct the missing pins: discounted future completion

**Theorem 6 (constructive quantitative completion).** Fix 0<rho<1. For h!=0
let v_b(h) be the largest nonnegative j with b^j dividing h, and set

\[
\boxed{V_h=\sum_{j=0}^{v_b(h)}\rho^j w_{h/b^j}.}
\]

Then

\[
V_{bh}=w_{bh}+\rho V_h,\quad V_h\ge w_h,\quad
\sum_{h\ne0}V_h=W/(1-\rho),
\]
\[
\boxed{D_V(T_{b,a*}\mu,T_{b,a*}\nu)\le\rho^{-1/2}D_V(\mu,\nu).}
\]

Proof: the recurrence separates the j=0 summand. Tonelli and the injective
substitution h=b^j k give the total weight. The recurrence gives
`V_h/V_bh<=1/rho` wherever V_h>0; apply Theorem 5, including its zero-weight
form. Nothing assumes an originally characteristic bed.

For any fixed affine sequence with multiplier b, let T^(j) denote the actual
common j-step evolution of two laws from the same starting time. Its known
translation contributes only a unit phase. Reindexing the nonnegative series
therefore gives the exact meaning of the new geometry:

\[
\boxed{D_V(\mu,\nu)^2
=\sum_{j\ge0}\rho^jD_w(T^{(j)}_*\mu,T^{(j)}_*\nu)^2.}
\]

**The bed contains the original probes and all their future pullbacks.** Its
zero relation means agreement on every original probe at every finite future
time. On an autonomous invariant class this is the greatest forward-invariant
equivalence contained in the original observer equivalence: any such relation
must preserve each future reading; conversely equality of all those readings
is preserved by one more step. The quotient is therefore an autonomous model
relative to the selected toolkit, even when full law reconstruction fails.

This construction specifies probes. It does not pretend to have performed
future experiments or create reset access to an invasive physical source.

### Least stable majorant, and finite error certificates

The sum V has the exact future-distance interpretation, but is not the least
majorant. The pointwise least family satisfying `M>=w` and `M_bh>=rho M_h` is

\[
\boxed{M_h=\max_{0\le j\le v_b(h)}\rho^j w_{h/b^j}.}
\]

Indeed `M_bh=max(w_bh,rho M_h)`, and iterating either required inequality
forces any competing family to dominate every term in the maximum. Also
M<=V, so it is summable and has the same Lipschitz bound. Both supports are
exactly `union_(j>=0) b^j supp(w)`. They do not invent off-ray information.

For a finite depth J, truncating the future-distance sum has a uniform squared
error at most

\[
\boxed{4W\rho^{J+1}/(1-\rho).}
\]

Each coefficient difference has modulus <=2. If the original spectral bed is
also truncated to finite symmetric H, add at most
`4(sum_(h outside H) w_h)(1-rho^(J+1))/(1-rho)` to this error. These are
mathematical error certificates; equality within a tolerance is not promoted
to an exact quotient relation. Increasing rho makes the dynamics bound closer
to one but raises total weight and the depth needed for a fixed tail error.

### The precision price of almost nonexpansive dynamics

For the B2 surface weights `w_h=1/(4*pi^4*h^4)`, the base point-translation
bound is Lipschitz because `4*pi^2 sum_h h^2 w_h=1/3`. After completion,

`sum_h h^2 V_h = (sum_h h^2 w_h)/(1-rho*b^2)` if rho*b^2<1,

and the series diverges otherwise. This follows by the same nonnegative
reindexing as the weight budget. In the convergent regime the point bound
becomes `d/sqrt(3(1-rho*b^2))`. Consequently the later BBP norm-transport
bound acquires the factor `(1-rho*b^2)^(-1/2)` in that regime.

For all 0<rho<1, any displacement 0<delta<=1 and any integer J>=0 give

\[
D_V(\tau_{\delta*}\mu,\mu)^2
\le \frac{\delta^2}{3}\sum_{j=0}^J(\rho b^2)^j
 +\frac{\rho^{J+1}}{45(1-\rho)}.
\]

Proof: use the base translation bound on the first J+1 future terms and
`D_w^2<=4W=1/45` on the remainder. Choosing
`J=floor(log_b(1/delta))` gives a Hölder modulus above the threshold, with
distance exponent `-log(rho)/(2log(b))<1`; at the threshold a logarithmic
factor occurs. This is an explicit cost: a more nearly nonexpansive dynamic
metric increases sensitivity to small source translations and weakens their
error modulus. The B2 bed's
O(A^-2) norm transfer must not be assigned unchanged to arbitrary completions.

This loss is necessary in the worst case. If rho*b^2>=1, Fatou's lemma gives
`liminf_(delta->0) D_V(delta_delta,delta_0)^2/delta^2
 >=4*pi^2 sum_h h^2 V_h=infinity`; no global Lipschitz point-translation bound
can hold. More sharply, for delta_N=1/(2b^N), the exact point-distance formula
implies `D_V(delta_delta_N,delta_0)^2 >= (delta_N^2/12)
sum_(j=0)^N(rho*b^2)^j`. This matches the upper Hölder exponent above the
threshold and the logarithmic loss at equality. These are worst-case statements;
Haar itself is unchanged by translation.

## 8. Finite harmonic completion, and two different closures

For a real convolution profile k on G=Z/m, its full translated surface reveals
exactly the law moments with `khat(h)!=0`, plus the known mass at zero. Define
`S={0} union {h:khat(h)!=0}` explicitly. Under x -> bx+a, a next-surface map exists on all probability
laws **iff bS is contained in S**. Sufficiency follows from the Fourier update.
For necessity take the same cosine perturbations in a missing mode of the finite
group; sufficiently small perturbations of the uniform law stay nonnegative.
Thus finite future completion is `union_(j>=0) b^j S`, computed until stable.
The criterion concerns all laws, and allows b noninvertible modulo m.

Exact failure witness on Z/6:

`k=(1/3,1/3,1/3,0,0,0)`;
`u=(1/6,...,1/6)`;
`v=(1/4,1/8,1/8,1/4,1/8,1/8)`.

Both initial surfaces are uniform. After x -> 2x their surfaces are
`(2/9,1/9,2/9,1/9,2/9,1/9)` and
`(1/4,1/6,1/4,1/12,1/6,1/12)` respectively. Hence no function of the static
surface, even nonlinear, predicts every successor. The initial support
{0,1,3,5} completes to every mode after one step.

**Point-state analogue.** For a finite abelian G with affine actions
`T_a(x)=L_a x+b_a`, let Lambda be the least subgroup of the dual containing
the initial characters and closed under every dual pullback L_a^*. Equality
of all finite character experiments is exactly
`x-y in Lambda^perp`. Thus G/Lambda^perp is the coarsest autonomous quotient
preserving those point readings. A target f descends iff its Fourier support
is contained in Lambda. Proof: the phase from b_a cancels when comparing
states; characters multiply to their dual-group sum and separate the quotient.
Fourier inversion then identifies exactly the functions constant on its cosets.

For law moments, products of measured means do not supply means of products.
The state subgroup closure and the linear law-moment closure must remain
distinct. On Z/4, opposite-point pairs have equal first moment zero and second
moments +1 and -1, although a single point character distinguishes all states.

The F2^3 example `T(x1,x2,x3)=(x2,1,x3+1)`, initial pin (-1)^x1, retains x1
and x2 after completion and permanently forgets x3. The target x2=0 becomes
invariantly decidable; x3=0 is TRUE_COMPATIBLE in every fiber while remaining
ambiguous. This is a nontrivial, dynamically closed instance of the user's
requested relative truth output. The implementation reuses SUCC's existing
behavioral partition and target resolver. A separate exhaustive checker compares
dual closure with direct transition refinement on all stated small affine cases.

### A finite surface bed can be exactly Haar-like for all future steps

For odd q let eta_q be uniform on the q-grid, and let

`nu_q=(1/4)eta_q+(3/8)tau_(1/(3q))*eta_q+(3/8)tau_(2/(3q))*eta_q`.

The Bernoulli multiplication formula gives
`F_eta_q(t)=q^-2 B2({qt})`. Hence every one of the q sampled pin heights
at t=i/q has `F_nu_q(i/q)=q^-2[(1/4)B2(0)+(3/4)B2(1/3)]=0`, exactly matching
Haar. Moreover nu_q is invariant under x ->16x: 16 permutes each q-grid
coset, and 16=1 modulo3 preserves the three offsets. It follows that these
sampled pins match Haar at **all future times**, not just a fitted horizon.
Yet nu_q is atomic and `E(nu_q)=1/(6480 q^4)>0`; the covariance formula or
the q-scaling of the complete profile proves this value.

This is a concrete valid relative equivalence for the finite sampled toolkit,
with an explicit P-true Haar representative for P="law is Haar" and a P-false
atomic representative. It demonstrates exactly what TRUE_COMPATIBLE means.
It is a source-free law control; it does not impersonate the selected BBP seed.

## 9. Authentic BBP application and the remaining arithmetic estimate

Keep the original source exactly:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

The instantaneous profiles satisfy
`F_delta{x_n}=L_(16,r(n)) F_delta{x_(n-1)}` with x_n={U_n}. This gives an
exact source-indexed internal model with a fixed initial profile and explicit
arrows. A common source label is insufficient: the executable receipt checks
the actual zero start, integer conductors, numerators, and every transition.

**Clock guard:** an empirical law averaging different n generally cannot be
updated by one common translation r(n). Preserve the time–forcing–phase joint
history when applying the nonautonomous formula. The completed phases below
do have the common autonomous x ->16x evolution.

For n>=1 put `T_n=sum_(j>=1)16^-j r(n+j)` and
`z_n={U_n+T_n}={16^n*pi/16}`. The original BBP series identity is a previously
authenticated source theorem, not an assumption about digits. We reproduce
the useful tail bound here. For n>=2, r(n)>0 and r(n)<1/n^2: if A(n) and D(n)
are its combined numerator and denominator, then, with m=n-2,

`D(n)-n^2 A(n)=392m^4+2201m^3+4494m^2+3902m+1185>0`.

Consequently `0<T_n<1/[15(n+1)^2]`. For the epoch [A,2A), Theorem 4 gives

\[
\boxed{\|F_{\mu_A^z}-F_{\mu_A^U}\|_2
\le\frac1{A\sqrt3}\sum_{n=A}^{2A-1}T_n
\le\frac1{30\sqrt3 A^2}.}
\]

The last inequality uses `sum_(n=A)^(2A-1)(n+1)^-2<=integral_A^(2A)t^-2dt`.
This is an **unconditional source-to-completed-pi O(A^-2) surface-norm bound**.
The squared error bound used in code is `1/(2700 A^4)`. It is distinct from
PR #540's O(A^-2) bound on its different, unsquared golden-aperture energy.

We obtain the exact criterion

\[
\boxed{\pi\text{ normal base 16}
\iff E(\mu_A^U)\longrightarrow0\quad\text{for every integer }A\to\infty.}
\]

Proof: section 5's positive-weight argument identifies
E->0 with weak Haar convergence. The tail bound transfers to the completed
orbit. Epoch convergence implies full-prefix convergence by dyadic halving
and a geometric weighted sum of the uniform large-A errors. Conversely prefix
Haar convergence implies all-epoch Haar convergence by subtracting prefixes.
Weyl's base-16 orbit criterion then gives the assertion.

**Classification:** this last criterion is a REFORMULATION. The actual
source-specific inequality E(mu_A^U)->0 is OPEN. The construction, stability
theorem, completion and source-tail bound are proved instrument/transport steps;
none is a new signed cancellation estimate. In the explicit linear surface
dynamics, the original source phases remain in the multipliers. Linearization
does not silently average them away.

## 10. Hostile boundaries and the next decisive probe

- Same forcing with a changed seed obeys U_n(s)=U_n(0)+16^n s. A coherent seed
  s=-pi/16 yields phases tending to zero, so its energy tends to 1/180, not zero.
  It is a hostile comparison, not an admissible replacement for the zero source.
- For any finite joint character packet along x_n=b^n x0, each tested history
  reduces to an initial frequency `sum_j h_j b^j`. Choose q coprime to b greater
  than every nonzero tested absolute frequency. The uniform q-root law and
  circle Haar agree on the entire packet and satisfy the same tested dynamics,
  but one is atomic. The counterfeit depends on the packet; it does not match
  all frequencies at once. Known common affine phases preserve this example.
- Uniform q-grids have energy 1/(180q^4): finite smallness is not exact Haar,
  and a horizon-dependent choice of q changes the source.
- Continuous surfaces can identify laws while badly conditioning high-frequency
  inversion. Our target modulus explicitly contains h^2. No claim of stable
  recovery of every discontinuous target is made.
- Matching marginal pin surfaces does not recover all history correlations;
  joint action/observation pins and the source clock remain necessary.

**Next arithmetic lamp:** a bound on the exact rational quartic pair energy of
the original zero-seeded source that tends to zero at all sufficiently large
epochs, or a sharper source-specific estimate on its individual signed pins.
The finite fresh epochs in the receipt calibrate an instrument. They cannot pay
this asymptotic proof debt.

## Primary sources and prior SUCC work

- Emily Riehl, *Category Theory in Context*, Corollary 2.2.8 (Yoneda) and
  Definition 6.5.11 (density/restricted Yoneda):
  https://emilyriehl.github.io/files/context.pdf .
- Sriperumbudur, Gretton, Fukumizu, Schölkopf and Lanckriet, *Hilbert Space
  Embeddings and Metrics on Probability Measures*, section 3.3 on the torus:
  https://arxiv.org/abs/0907.5309 . Characteristic kernels and their limitations
  are classical prior art, not invented here.
- NIST DLMF 24.4.18 (Bernoulli multiplication) and 24.8.1/24.8.3 (Fourier
  expansions): https://dlmf.nist.gov/24.4 and https://dlmf.nist.gov/24.8 .
- Brunton et al., *Koopman invariant subspaces and finite linear
  representations of nonlinear dynamical systems for control*:
  https://arxiv.org/abs/1510.03007 . Used for context on observable dynamics;
  the exact constants and constructions above are proved directly.
- Main's carrier-relative target descent, operational Yoneda, dynamic Fourier
  tower, integer BBP carrier, and source-circle pressure work; exact provenance
  and read-only post-main comparisons are in [SOURCE_MAP.md](SOURCE_MAP.md).

**Final truth state:** the pin-bed construction and stated transport theorems
are PROVED LOCAL; finite receipts are OBSERVED EXACT in their stated scope;
novel priority is UNVERIFIED; the authentic surface-flattening estimate and
base-16 normality of pi remain OPEN.
