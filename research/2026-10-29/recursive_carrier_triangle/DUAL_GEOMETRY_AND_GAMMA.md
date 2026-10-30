# The dual field: exact information geometry, source interaction bounds, and the Gamma boundary

**Date:** 2026-10-29. **Baseline:** SUCC main
`ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc`.
**Authority:** complete paper derivations below; executable validation is recorded
separately by this research round. No Lean authority or academic priority is
claimed. The source is the original signed four-pole BBP forcing, viewed through
its already established positive Laplace carrier. The actual zero-seeded BBP
orbit is not replaced by a random draw from that carrier.

The author's proposed dual construction has a precise realization: the
logarithm of the source normalization is a potential, its first differential is
the carrier's mean, and its second differential is its variance. A source shift
changes the normalized carrier. Composing two such shifts while remembering
the changed carrier differs from resetting the carrier between them by a
strictly positive, explicitly bounded interaction. This is a constraint on how
the proposed sheet can move. It is not an antisymmetric gauge curvature or a
physical gluon interaction.

## 1. Source, inheritance, and the new comparison

For every real `a>0`, let

$$
 Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x},\qquad
 R(a)=\int_0^\infty e^{-ax}Q(x)\,dx
     =\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}.
$$

The density

$$
 \mu_a(dx)=\frac{e^{-ax}Q(x)}{R(a)}\,dx
$$

is a probability law: `Q(x)>0` for `x>0`, and the exponential tail makes all
polynomial moments finite. For the original clock `a_n=8n-7`, `R(a_n)=r(n)`.
This source identity and the update

$$
 \mu_{a+s}(dx)=\frac{e^{-sx}}{Z_a(s)}\mu_a(dx),\qquad
 Z_a(s)=\frac{R(a+s)}{R(a)}\quad(s\ge0)
$$

were already established in
[OILY_POSITIVE_FIELD_GAMMA_COCYCLE.md](../../2026-10-26/OILY_POSITIVE_FIELD_GAMMA_COCYCLE.md).
The overlap and Fisher identity were already established in
[OILY_LOG_CLOCK_HILBERT_TRANSPORT.md](../../2026-10-26/OILY_LOG_CLOCK_HILBERT_TRANSPORT.md).
That dossier proved `Var_mu_a(X)<8/a^2` for `a>=16`, and then
`1-H(a,b)<=log(b/a)^2` on that restricted domain.

This round supplies a sharper source-specific comparison valid for **all**
positive parameters, its finite-step interaction bounds, and its consequences
for dual information cost and signed representation transport. The underlying
exponential-family and convex-duality identities are classical. The exact
four-pole assembly is new to this round, without a claim of scholarly novelty.

We use the factorization from
[ATOMIC_SOURCE_AND_INTERACTIONS.md](ATOMIC_SOURCE_AND_INTERACTIONS.md):

$$
 R(a)=\frac{15(a+\alpha)(a+\beta)}{a(a+3)(a+4)(a+5)},\qquad
 \alpha=\frac{121-\sqrt{241}}{30},\quad
 \beta=\frac{121+\sqrt{241}}{30},
 \tag{DG-1}
$$

where `3<alpha<4<beta<5`. Those inequalities follow, for example, from
`15<sqrt(241)<16`. They do not require decimal approximations. The companion
dossier gives the positive atomic and convolution interpretation; it is not
assumed that the BBP digit phases inherit independence from those atoms.

## 2. The source differential and the all-parameter variance squeeze

Set `F(a)=log R(a)` and `m(a)=E_mu_a X`. Differentiation under the integral
is valid on every compact subinterval of `a>0`, since each polynomial in `x`
is dominated by an integrable exponential there. Thus

$$
 F'(a)=-m(a),\qquad F''(a)=\operatorname{Var}_{\mu_a}(X)=:V(a),
 \qquad
 \partial_a\log\mu_a(x)=-(x-m(a)).
 \tag{DG-2}
$$

The last expression is the density's score. Its mean is zero and its squared
mean is `V(a)`. It is a concrete field differential; the centering term is
forced by probability normalization.

**Theorem DG-3 (source variance bounds, PROVED LOCAL (paper)).** For every `a>0`,

$$
 \boxed{
 \frac1{a^2}+\frac1{(a+5)^2}
 <V(a)<
 \frac1{a^2}+\frac1{(a+3)^2}
 <\frac2{a^2}.}
 \tag{DG-3}
$$

The coefficient `2` is asymptotically sharp: `a^2 V(a)->2` as `a->infinity`.

**Proof.** Differentiate the logarithm of (DG-1) twice:

$$
 V(a)=\frac1{a^2}+\frac1{(a+3)^2}+\frac1{(a+4)^2}
       +\frac1{(a+5)^2}-\frac1{(a+\alpha)^2}-\frac1{(a+\beta)^2}.
$$

For the lower bound, group the positive differences indexed by `(3,alpha)`
and `(4,beta)`. For the upper bound, group the negative differences indexed
by `(4,alpha)` and `(5,beta)`. All inequalities are strict by interlacing.
Multiplying the exact formula by `a^2` and taking the limit gives `4-2=2`.
This proves the universal statement without an experimental extrapolation.

The same argument also bounds the mean:

$$
 \frac1a+\frac1{a+5}<m(a)<\frac1a+\frac1{a+3}.
$$

More generally, each integer-order cumulant of `X` is obtained by
`kappa_k(a)=(-1)^k F^(k)(a)`. The companion atomic dossier treats the full
hierarchy. The variance theorem here is its second-order geometric face.

## 3. Two subpaths: a coherent interaction rather than naive reset additivity

Define the logarithmic evidence increment

$$
 K_a(s)=F(a+s)-F(a)=\log Z_a(s).
$$

**Exact conditioned composition** is

$$
 K_a(s+t)=K_a(s)+K_{a+s}(t),\qquad
 Z_a(s+t)=Z_a(s)Z_{a+s}(t).
 \tag{DG-4}
$$

It is essential that the second segment starts at `a+s`. Replacing that
term by `K_a(t)` resets the field. The resulting discrepancy is

$$
 \begin{aligned}
 I_a(s,t)
 &=K_a(s+t)-K_a(s)-K_a(t)\\
 &=\log\frac{R(a+s+t)R(a)}{R(a+s)R(a+t)}\\
 &=\int_0^s\int_0^t V(a+u+v)\,dv\,du.
 \end{aligned}
 \tag{DG-5}
$$

This uses the fundamental theorem of calculus twice. For `s,t>0` it is
strictly positive. For either increment zero it is exactly zero. At rational
`a,s,t`, the exponentiated interaction is an exact rational number, allowing
comparison without evaluating any logarithms.

For `c>=0` put

$$
 J_c(a;s,t)=\log\frac{(a+c+s)(a+c+t)}{(a+c)(a+c+s+t)}.
$$

**Corollary DG-6 (finite-step bounds, PROVED LOCAL (paper)).** For every `a,s,t>0`,

$$
 \boxed{J_0(a;s,t)+J_5(a;s,t)<I_a(s,t)
       <J_0(a;s,t)+J_3(a;s,t).}
 \tag{DG-6}
$$

Indeed `J_c` is exactly the double integral of
`1/(a+c+u+v)^2`; apply (DG-3). Equalities at a zero increment must be handled
separately. These are explicit constraints on the nonlinear reset discrepancy.

For fixed `s,t>0`, `I_a(s,t)~2st/a^2` as `a->infinity`. For fixed positive
`sigma,tau` and increments `s=sigma*a`, `t=tau*a`, the exact rational form
of `R` gives

$$
 I_a(\sigma a,\tau a)\longrightarrow
 2\log\frac{(1+\sigma)(1+\tau)}{1+\sigma+\tau}.
$$

Thus microscopic shifts have vanishing interaction, while shifts at the
scale of the current carrier parameter have a nonzero limiting interaction.
These are analytic consequences of the source identity, not fitted limits.

The same potential enforces the associative triangle constraint

$$
 I_a(s,t)+I_a(s+t,u)=I_a(t,u)+I_a(s,t+u),
 \tag{DG-7}
$$

as direct cancellation of the four potential terms verifies. This identity
compares two parenthesizations of the same three segments. It does not say
that the interaction vanishes, and it does not provide an order-sensitive
physical gauge holonomy. The scalar shifts in this model commute.

## 4. Exact overlap bounds and sharper signed representation transport

Let `f_a(x)=sqrt(d mu_a/dx)` and define its real Hilbert overlap

$$
 H(a,b)=\langle f_a,f_b\rangle
       =\frac{R((a+b)/2)}{\sqrt{R(a)R(b)}}.
$$

For `c>=0`, put

$$
 A_c(a,b)=\frac{2\sqrt{(a+c)(b+c)}}{a+b+2c}.
$$

**Theorem DG-8 (source overlap comparison, PROVED LOCAL (paper)).** For all `a,b>0`,

$$
 \boxed{A_0(a,b)A_3(a,b)\le H(a,b)
                  \le A_0(a,b)A_5(a,b).}
 \tag{DG-8}
$$

Both inequalities are strict for `a!=b`; all terms equal one for `a=b`.

**Proof, including directions.** The lower variance bound makes
`F(a)+log a+log(a+5)` strictly convex. Its midpoint inequality gives
`log H<=log A_0+log A_5`. The upper variance bound makes
`F(a)+log a+log(a+3)` strictly concave; its reversed midpoint inequality
gives `log H>=log A_0+log A_3`. Exponentiation preserves the inequalities.

Since adding a positive `c` increases `A_c`, we have `A_3>=A_0`. Therefore

$$
 \boxed{
 0\le1-H(a,b)
 \le\frac{(a-b)^2}{(a+b)^2}
 =\tanh^2\!\left(\frac12\log\frac ba\right)
 \le\frac14\left(\log\frac ba\right)^2.}
 \tag{DG-9}
$$

The first bound is rational when `a,b` are rational. The stronger bounds
(DG-8) can also be checked exactly by squaring all positive quantities.
The coefficient `1/4` in the last bound is optimal over the whole positive
parameter domain. To see this, for fixed `a` take `b->a` and obtain the ratio
`a^2 V(a)/8`; then let `a->infinity` and use (DG-3).

This sharpens the earlier overlap bound by a factor of four in its logarithmic
coefficient and removes the `a,b>=16` restriction. The local improvement is a
constant and domain improvement. The better global error rate below comes
from summing local errors with a different block schedule.

In detail, let `z_n` be **any** complex numbers with `|z_n|<=1`, and let
`B={m,...,m+L-1}`, where `m,L>=1` are integers. On the authentic clock,

$$
 \begin{aligned}
 &\left|\frac1L\sum_{n\in B}z_n
       -\frac1L\sum_{n\in B}z_n H(a_n,a_m)\right|\\
 &\quad\le
 \left(\frac{8(L-1)}{2(8m-7)+8(L-1)}\right)^2
 \le\frac14\left(\frac{8(L-1)}{8m-7}\right)^2.
 \end{aligned}
 \tag{DG-10}
$$

For each summand apply (DG-9), and maximize the increasing ratio
`8(n-m)/(2a_m+8(n-m))` over the block. For `L=1` the error is zero.
Choosing `z_n=exp(2*pi*i*h*U_n)` preserves the actual signed BBP phases,
but the bound remains equally true for the coherent control `z_n=1`.
Consequently it is a stronger **representation error** bound, not a
cancellation estimate.

### 4.1 An exact budget for any block schedule

Partition `1,...,N` into consecutive blocks, with each block `B` starting
at `m_B`. Define

$$
 A_N=\frac1N\sum_{n=1}^N z_n,\qquad
 \widetilde A_{N,\mathcal P}
 =\frac1N\sum_{B\in\mathcal P}\sum_{n\in B}z_n H(a_n,a_{m_B}).
$$

Then for every such partition and every `|z_n|<=1`,

$$
 \boxed{|A_N-\widetilde A_{N,\mathcal P}|
 \le\mathcal B(N,\mathcal P)
 :=\frac1N\sum_{B\in\mathcal P}\sum_{n\in B}
       \left(\frac{8(n-m_B)}{2a_{m_B}+8(n-m_B)}\right)^2.}
 \tag{DG-10a}
$$

The right side is an exact rational certificate. It follows by applying
(DG-9) to each term before taking the triangle inequality. No source values
or initial phases are dropped.

The executable budget functions use the efficient **block endpoint budget**
`N^(-1) sum_B |B| [(a_max(B)-a_min(B))/(a_max(B)+a_min(B))]^2`.
Each summand in (DG-10a) increases with `n` inside its block, so this
endpoint budget is at least `B(N,P)`. It is also an exact rational upper
certificate, requires only one calculation per block, and obeys the same
uniform and cubic simple bounds proved below. The code does not claim that
this endpoint budget equals the finer term-by-term budget or the actual
transport error.

For uniform blocks of length `k`, truncated at the end, the first block
contributes at most `k/N`. Block `j>=1` starts at `m=1+j*k`, so its
individual deficits are at most `1/(4j^2)` and its total normalized
contribution is at most `k/(4Nj^2)`. Since
`sum_(j>=1) 1/j^2 <= 1+integral_1^infinity x^(-2) dx=2`,

$$
 \mathcal B(N,\mathcal P_{\rm uniform})\le\frac{3k}{2N}.
 \tag{DG-10b}
$$

This holds for every pair of integers `1<=k<=N`. It illustrates why summing
the actual sequence of local budgets improves on a single worst-case bound
after a cutoff. This summation idea does not depend on the factor-four
constant improvement alone.

### 4.2 Cubic blocks: fewer source anchors with a smaller total error

**Theorem DG-10c (cubic source transport, PROVED LOCAL (paper)).** For an integer
`N>=1`, set `J=floor((N-1)^(1/3))`, interpreted as an exact integer cube root.
Use the consecutive blocks

$$
 B_j=\{1+j^3,\ldots,\min((j+1)^3,N)\},\qquad 0\le j\le J.
$$

There are `J+1` nonempty blocks. The first is the singleton `{1}`. For
every complex sequence `|z_n|<=1`,

$$
 \boxed{|A_N-\widetilde A_{N,\mathcal P_{\rm cubic}}|
       \le\mathcal B(N,\mathcal P_{\rm cubic})
       \le\frac{27J}{4N}
       \le\frac{27}{4}N^{-2/3}.}
 \tag{DG-10c}
$$

At `N=1`, the middle bound is zero. The theorem uses at most
`N^(1/3)+1` source reference vectors and preserves every selected phase.

**Proof.** The singleton's deficit is zero. For `j>=1`, the full block
has length `L=3j^2+3j+1`, starts at `m=1+j^3`, and has
`a_m=1+8j^3`. Write `r=n-m`, so `0<=r<=3j(j+1)`. Then

$$
 \left(\frac{8r}{2a_m+8r}\right)^2
 =\left(\frac{r}{2j^3+1/4+r}\right)^2
 \le\left(\frac{3(j+1)}{2j^2+3j+3}\right)^2.
$$

The ratio is increasing in `r`, and dropping `1/4` only enlarges it.
The complete block budget is therefore at most

$$
 L\left(\frac{3(j+1)}{2j^2+3j+3}\right)^2<\frac{27}{4}.
$$

The last inequality has the positive polynomial receipt

$$
 3(2j^2+3j+3)^2-4(3j^2+3j+1)(j+1)^2
 =23j^2+34j+23>0.
$$

Truncating a block decreases its nonnegative budget. There are `J` blocks
with `j>=1`, giving `27J/(4N)` after normalization. Finally `J<=N^(1/3)`.

This is a quantitative improvement over the inherited cutoff-plus-uniform
window argument: that construction gave `O(N^(-1/3))` representation error
with about `N^(2/3)` source anchors, whereas cubic blocks give
`O(N^(-2/3))` with about `N^(1/3)` anchors. The improvement is in **source
compression and representation transport**. It contains no saving in the
size of the signed sum. For the hostile control `z_n=1`, the theorem implies
`tilde A -> 1`, demonstrating that this carrier geometry alone does not
force cancellation.

## 5. A genuine dual construction: energy versus information

Let `a>0`, `s>=0`. For any probability `nu` absolutely continuous with
respect to `mu_a`, with finite relative entropy and first moment,

$$
 D(\nu\Vert\mu_{a+s})
 =D(\nu\Vert\mu_a)+s\mathbb E_\nu X+\log Z_a(s).
$$

This is immediate by substituting the logarithm of the density ratio. Since
relative entropy is nonnegative and vanishes only for equal probability laws,

$$
 \boxed{-\log Z_a(s)
  =\inf_\nu\{s\mathbb E_\nu X+D(\nu\Vert\mu_a)\},
  \qquad\nu_{\rm unique}=\mu_{a+s}.}
 \tag{DG-11}
$$

The competitor class can equivalently include infinite-cost laws, with the
usual extended-real convention. The optimizer has all required finite
moments and finite relative entropy. For `s=0` it is `mu_a`.

This supplies an exact dual answer to the author's proposal: the changed
carrier minimizes a source-relative sum of a linear field cost and an
information cost. It is the classical Gibbs variational identity specialized
to this authenticated source. No optimization principle for actual human
reasoning or physical matter has been deduced.

There is also a complete finite cost comparison. For every `a,b>0`,

$$
 D(\mu_a\Vert\mu_b)=F(b)-F(a)-(b-a)F'(a).
 \tag{DG-12}
$$

Let `d(r)=r-1-log r` for `r>0`. Integrating the variance bounds in Taylor's
formula with integral remainder yields

$$
 \boxed{
 d(b/a)+d((b+5)/(a+5))
 \le D(\mu_a\Vert\mu_b)
 \le d(b/a)+d((b+3)/(a+3)).}
 \tag{DG-13}
$$

The inequalities are strict for `a!=b` and equalities hold at `a=b`.
For either orientation, the relevant integral is
`integral_a^b (b-u) V(u) du`, with oriented integration when `b<a`.
Its value for the comparison term `1/(u+c)^2` is exactly
`d((b+c)/(a+c))`; this verifies the direction in both cases.

## 6. A contrasting auxiliary triangle: Beta/Pólya evidence

This section is a **classical auxiliary model**, not a replacement for the
four-pole carrier. It shows that coherent interactions need not all have the
same sign when different event types are available.

Start with a `Beta(alpha_0,beta_0)` latent bias, with both parameters positive.
The probability of any one ordered binary word containing `k` successes and
`l` failures is

$$
 \frac{B(\alpha_0+k,\beta_0+l)}{B(\alpha_0,\beta_0)}.
$$

This is the word probability, without a binomial multiplicity. It follows
directly by integrating the Bernoulli likelihood against the Beta density.
It reproduces the Pólya next-success probability
`(alpha_0+k)/(alpha_0+beta_0+k+l)`.

Write

$$
 G(k,l)=\log B(\alpha_0+k,\beta_0+l)-\log B(\alpha_0,\beta_0).
$$

For count vectors `p,q` in `N^2`,

$$
 C(p,q)=G(p+q)-G(p)-G(q)
$$

obeys the exact cocycle identity
`C(p,q)+C(p+q,r)=C(q,r)+C(p,q+r)`. The conditional log evidence of the
second segment is `G(p+q)-G(p)`, so subtracting the reset value `G(q)` gives
this interaction. Exchangeability makes this example order-insensitive even
though predictions update after each event.

At state `(k,l)` set `A=alpha_0+k`, `B=beta_0+l`, and `S=A+B`. The elementary
finite mixed differences are

$$
 \Delta_k\Delta_lG=\log\frac S{S+1}<0,
 \qquad
 \Delta_k^2G=\log\frac{(A+1)S}{A(S+1)}>0.
 \tag{DG-14}
$$

The second inequality follows because the numerator minus the denominator
is `B>0`. A repeated event and an opposing event therefore yield different
interaction signs. This is a concrete mathematical account of interactions
between subhistories; it is not evidence of a gauge force.

These formulas follow from the Beta integral and the Gamma successor law.
The established repository history comparison in
[REALIZED_PATHS_AND_FIELD_FEEDBACK.md](../../2026-10-26/REALIZED_PATHS_AND_FIELD_FEEDBACK.md)
already warns that the same finite Pólya word law can arise from learning a
static Beta bias. The new cocycle notation does not distinguish physical
reinforcement from Bayesian updating by itself.

## 7. What Gamma and Oily–Macaroni can and cannot weight

Two different claims must be kept separate.

### 7.1 Affine normalization does not create interaction curvature

Replace `F(a)` by `F(a)+c*a+d`, for arbitrary real constants `c,d`. Every
second or higher derivative, every interaction (DG-5), and the midpoint
overlap expression in (DG-8) is unchanged. The cost (DG-12) is also
unchanged. This is direct cancellation of affine terms.

The same statement holds for `G(p)` replaced by `G(p)+v dot p` in the
Beta/Pólya cocycle. Thus inserting the scalar
`Omega=phi^(-1)-gamma` as a linear centering or normalization term cannot
by itself change any of these interaction observables. A scalar multiplying
an entire density is also removed by probability normalization.

The classical expansion of `log Gamma(1+z)` has Euler's constant in its
linear coefficient; higher derivatives remove that particular affine term.
This does **not** assert that gamma disappears from every nonlinear model,
parameter choice, or regularization. It says exactly which proposed use is
invisible to the current probes. A genuine gamma-dependent interaction
requires a declared non-affine coupling or a different source law, followed
by a source-faithfulness test. It cannot be obtained by renaming an affine
gauge.

### 7.2 A genuine source-relative Gamma finite part already exists

The inherited source cocycle has the exact finite identity

$$
 \sum_{n=1}^{N-1}\left(\log\frac{r(n)}{r(n+1)}-\frac2n\right)
 =\log\frac{r(1)}{r(N)}-2H_{N-1}.
$$

Since `r(1)=47/15`, `r(N)~15/(64N^2)`, and
`H_(N-1)-log N -> gamma`, its limit is

$$
 \log\frac{3008}{225}-2\gamma.
 \tag{DG-15, inherited}
$$

This is the result of
[OILY_POSITIVE_FIELD_GAMMA_COCYCLE.md](../../2026-10-26/OILY_POSITIVE_FIELD_GAMMA_COCYCLE.md),
not a new theorem of this round. Gamma is produced by a specified comparison
of a harmonic clock and a logarithmic source clock. The choice of comparison
is part of the statement. It does not force a golden normalization or supply
a signed arithmetic phase.

The exact finite interaction (DG-5), in contrast, is the logarithm of a
rational expression at rational parameters. No numeric gamma or golden
constant is inserted in its construction. Both facts can hold together:
gamma is a legitimate global regularized boundary value, while the local
interaction geometry is fixed by the complete rational source.

## 8. Discriminators, proof boundary, and provenance

The main finite checks should use the original partial-fraction formula for
`R,R',R''`, independent of the interlacing proof, and exact rational arithmetic
for (DG-3), exponentiated (DG-6), and squared (DG-8). Include parameters below
one, authentic clocks, nonintegral parameters, unequal-scale pairs, the
diagonal, and zero increments. A mutant `R(a)=1/a` violates the strict
two-term lower variance bound; the endpoint Gamma(2) approximation
`R(a)=15/a^2` violates the shifted upper variance bound. This prevents the
test suite from silently replacing the authenticated source by an endpoint
model. The approximation does satisfy the weaker universal coefficient
`V<=2/a^2`, illustrating why that coefficient alone does not identify the
source.

The exact source identity is stronger than this family of inequalities.
Other sources can share some or all inequalities. The controls are therefore
calibration and source-preservation checks, not a uniqueness proof.

Every positive-source construction here is unchanged by altering the initial
condition of `U_n=16U_(n-1)+r(n)`. In particular, the existing `U_n=-T_n`
changed-seed control still has its coherent selected Fourier behavior.
Consequently no theorem in this dossier establishes selected BBP cancellation,
pi normality, RH, or a physical quantum dynamics.

The next verdict-changing task must supply a source-labelled **signed**
coupling involving the actual zero-seeded orbit that distinguishes that
control. Stronger information or overlap bounds alone do not perform that
selection.

### Primary-source and repository provenance

- Original source and prior normalization cocycle: the two 2026-10-26 dossiers
  linked in section 1, read at the exact baseline above. Their historical
  files are preserved.
- Classical exponential-family derivatives and entropy duality:
  M. J. Wainwright and M. I. Jordan, *Graphical Models, Exponential Families,
  and Variational Inference*, sections 3.5–3.6,
  [author-hosted text](https://people.eecs.berkeley.edu/~jordan/sail/readings/wainwright-jordan-fnt.pdf),
  DOI [10.1561/2200000001](https://doi.org/10.1561/2200000001).
  The source-specific variational statement here has a full direct proof,
  so no unverified transfer of general-family hypotheses is needed.
- Classical Beta integral and Gamma ratio:
  [NIST DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1), for positive real
  parameters. This is the integral used in section 6.
- Euler's constant in the logarithmic Gamma expansion:
  [NIST DLMF 5.7.3–5.7.4](https://dlmf.nist.gov/5.7).
  The stated series have their displayed convergence domains; this dossier
  uses them only to identify the affine normalization term.
- Positive trigamma series and higher derivatives:
  [NIST DLMF 5.15.1–5.15.2](https://dlmf.nist.gov/5.15).
  No general claim that Euler's constant controls the higher derivatives is
  made.

All external sources above were opened during this round. Shared source
provenance is not independent evidence. Proof checks, finite exact controls,
and the inherited source are distinct kinds of support with the scopes stated
above.

## 9. The apex preserves exactly the source-tilt information under subdivision

The convolution construction in
[ATOMIC_SOURCE_AND_INTERACTIONS.md](ATOMIC_SOURCE_AND_INTERACTIONS.md),
Theorem C, supplies probability measures `mu_(a,t)` for every `a>0`,
`t>=0`, with

$$
 \int_0^\infty e^{-sx}\mu_{a,t}(dx)
 =\left[\frac{R(a+s)}{R(a)}\right]^t,
 \qquad s\ge0,
 \tag{DG-16}
$$

`mu_(a,1)=mu_a`, `mu_(a,0)=delta_0`, and
`mu_(a,t)*mu_(a,u)=mu_(a,t+u)`. The parameter `t` measures convolution
subdivision; it is not identified with arithmetic source time or elapsed
physical time.

For `t>0`, the explicit construction includes independent
`Gamma(t,a)` and `Gamma(t,a+5)` summands. Their convolution has a strictly
positive density on `(0,infinity)`. The other two compound-Poisson summands
have a positive probability of being zero, so the complete law also has a
strictly positive density there. Its entire law is absolutely continuous,
because it is a convolution with that density. Thus, for fixed `t>0`, the
measures at any two positive source parameters are mutually absolutely
continuous. At `t=0`, all source parameters give the same point mass.

### 9.1 Exact affinity and information scaling

**Theorem DG-17 (PROVED LOCAL (paper)).** For every `a,b>0` and every `t>=0`, the
Hellinger affinity satisfies

$$
 \boxed{H_t(a,b)=H(a,b)^t.}
 \tag{DG-17}
$$

The relative entropy, cumulants of every positive integer order, and
source-normalizer interactions satisfy

$$
 \boxed{
 D(\mu_{a,t}\Vert\mu_{b,t})=tD(\mu_a\Vert\mu_b),\qquad
 \kappa_k(\mu_{a,t})=t\kappa_k(\mu_a),\qquad
 I_{a,t}(s,u)=tI_a(s,u).}
 \tag{DG-18}
$$

Here `s,u>=0`, and `I_(a,t)` is the same reset interaction as in (DG-5),
formed from the tilt normalizers of `mu_(a,t)`. Every higher finite mixed
source difference also scales by `t`. The affinity exponent should not be
confused with linear scaling of squared Hellinger distance:
`1-H_t=1-H^t`, which is generally not `t(1-H)`.

**Proof.** Let `c=min(a,b)`. Exponential tilting in Theorem C gives the
common-reference densities

$$
 \frac{d\mu_{a,t}}{d\mu_{c,t}}(x)
 =\frac{e^{-(a-c)x}}{[R(a)/R(c)]^t},\qquad
 \frac{d\mu_{b,t}}{d\mu_{c,t}}(x)
 =\frac{e^{-(b-c)x}}{[R(b)/R(c)]^t}.
 \tag{DG-19}
$$

For `t>0`, integrate the square root of their product and use (DG-16) at
`s=(a+b)/2-c>=0`. The result is

$$
 H_t(a,b)
 =\frac{[R((a+b)/2)/R(c)]^t}
        {[R(a)R(b)/R(c)^2]^{t/2}}
 =\left[\frac{R((a+b)/2)}{\sqrt{R(a)R(b)}}\right]^t.
$$

The resulting likelihood ratio between the two source parameters is

$$
 \frac{d\mu_{a,t}}{d\mu_{b,t}}(x)
 =e^{(b-a)x}\left[\frac{R(b)}{R(a)}\right]^t.
 \tag{DG-20}
$$

The explicit Gamma and compound-Poisson construction has finite exponential
moments for real exponents less than `a`. Its cumulant generating function
on a neighborhood of zero is therefore
`t[F(a-v)-F(a)]`. Differentiation gives every cumulant scaling statement,
including `E_(mu_(a,t)) X=t*m(a)`. Taking the expectation of the logarithm
of (DG-20) gives

$$
 D(\mu_{a,t}\Vert\mu_{b,t})
 =t\{(b-a)m(a)+F(b)-F(a)\}.
$$

All terms are finite. Log tilt normalizers are `t*K_a(s)`, so their finite
differences scale by `t` as well.

At `t=0`, use the common reference `delta_0`. Both densities in (DG-19)
equal one on its support, the affinity equals one, relative entropy and
all cumulants equal zero, and every tilt normalizer equals one. Thus every
formula holds without positing a Lebesgue density for `delta_0`.

As an additional differential statement, for fixed `t>0` the source score is
`-X+t*m(a)` and its Fisher information is `t*V(a)`. At `t=0` the law does
not depend on `a`, so the information is zero. This is the precise sense in
which source-parameter distinguishability is compatible with arbitrary
convolution subdivision.

### 9.2 Summation loses no information about this one source parameter

Fix an integer `k>=1` and **known, fixed** nonnegative subdivision amounts
`t_1,...,t_k`. Set `t=sum_i t_i`. Consider the family of product measures

$$
 P_a=\bigotimes_{i=1}^k\mu_{a,t_i},\qquad a>0,
 \qquad S(x_1,\ldots,x_k)=\sum_{i=1}^k x_i.
$$

The law of `S` under `P_a` is `mu_(a,t)`. Coordinates with `t_i=0` are
deterministically zero and may be omitted.

**Theorem DG-21 (source-parameter sufficiency, PROVED LOCAL (paper)).** For this
family, `S` is a sufficient statistic for `a`. For every `a,b>0`,

$$
 \boxed{\frac{dP_a}{dP_b}(x_1,\ldots,x_k)
 =e^{(b-a)S}\left[\frac{R(b)}{R(a)}\right]^t.}
 \tag{DG-21}
$$

Consequently summing the microvariables preserves their relative entropy
and Hellinger affinity **for comparisons of the parameter `a`**:

$$
 \begin{aligned}
 D(P_a\Vert P_b)
 &=\sum_i D(\mu_{a,t_i}\Vert\mu_{b,t_i})
  =D(\mu_{a,t}\Vert\mu_{b,t}),\\
 \operatorname{Aff}(P_a,P_b)
 &=\prod_i H_{t_i}(a,b)
  =H_t(a,b).
 \end{aligned}
 \tag{DG-22}
$$

**Proof.** Multiply (DG-20) over the independent coordinates. The product
is (DG-21) and depends only on `S`. Choose any fixed reference parameter,
for example `b=1`. All `P_a` are mutually absolutely continuous, and
their likelihood ratios relative to `P_1` are functions of `S`. Hence a
regular conditional law of the microvariables given `S` under `P_1`
also serves for every `P_a`; equivalently, the likelihood factorization
criterion gives sufficiency. Such conditional probability kernels exist
on these finite-dimensional Borel spaces. No parameter-dependent
conditioning kernel is smuggled into this conclusion.

The relative entropy identity follows either by taking expectations of
(DG-21), or by finite product additivity and (DG-18). Affinity factors
under products by Tonelli's theorem, and (DG-17) gives
`product_i H^(t_i)=H^t`. If `t=0`, every `t_i=0`, both product laws are
the same point mass, and `S=0` carries no information about `a`; all
identities remain valid with entropy zero and affinity one.

**Exact boundary of losslessness.** The result concerns only the
source-tilt parameter `a`, with the subdivision amounts fixed and known.
It does not recover an ordered tuple from its sum, retain an individual
realization's ordering, identify unknown subdivision parameters, or preserve
arbitrary microstate observables. It does not preserve arithmetic selected
phases unless a separate phase-aware sufficient-statistic theorem supplies
that conclusion. The actual BBP phase sequence is not a draw from the
product family above.

This gives a restricted, exact realization of the proposed apex: many
microstates can be compressed into one sum while retaining **all likelihood
information for this source parameter**. The compression remains lossy for
general labelled history. A discriminating failure probe is to attach an
observable of one individual microvariable, or of the order of several
microvariables, and ask whether its conditional value is determined by
`S`; the theorem makes no such prediction. The changed-seed arithmetic
control in section 8 remains unchanged by this sufficiency result.
