# Inertial information boundary: zero preparation, a rich field, and exact observation quotients

**Date:** 2026-10-29 (America/New_York).
**Parent:** draft [PR #367](https://github.com/femboy2112/SUCC/pull/367),
`b6a3815ceb505de0b1f570eae3ff5be75cdbe99c`.
**Branch:** `research/inertial-information-boundary-2026-10-29`.
**Authority:** scoped paper proofs, classical identities, and separately
reported finite exact checks. This is a research continuation, with no claim
of physical validation, Lean certification, academic priority, or pi normality.

The author's qualification **relative to the inertial base carrier** is the
mathematically decisive part. A declared carrier can make zero the unique
actualized boundary requiring no preparation, while its neutral fiber retains
an entire virtual field. The resulting preparation order is compatible with
an explicit information code and a sharp relative-entropy bound. Each requires
its reference structure to be stated.

The strongest new observation is that preparation and observation can disagree
about what they distinguish. The exact arithmetic trajectories started at
`0`, `-1`, and `-16` differ, but their integer-frequency phases are identical
at every time. A phase statistic cannot recover the preparation choice that
it has erased. Selecting the intended zero seed therefore remains meaningful
without supplying a cancellation theorem for that selected trajectory.

## 1. The precise inertial preparation axiom

Let a carrier have states `Omega`, an actualized observable `q:Omega->A`, and
a marked neutral value `0`. Its neutral fiber is `F=q^(-1)({0})`. Declare a
preparation grammar with additive nonnegative costs and assume:

1. The unprepared initial state lies in `F`.
2. Every free operation preserves all of `F`.
3. Every paid operation costs at least a fixed `delta>0`.

Then zero has minimum preparation cost zero. Every reachable nonzero
actualized value has minimum cost at least `delta`. The proof is induction
through the free operations: leaving the neutral fiber requires a paid step.
The positive gap matters when an infinite instruction family is allowed.

This is a pointed model: it includes a designated neutral preparation.
It does not infer a preferred origin from an unmarked affine space. The
virtual fiber can have many states, and free operations may rearrange them.
Paid instructions can also cancel, so a program ending at zero need not
itself have zero cost.

An exact arithmetic realization starts at zero, allows `u->16u` and `u->-u`
for free, and charges one unit for `u->u+1` or `u->u-1`.
Zero is the unique common fixed point of these declared free operations:
`16u=u` forces `u=0`. This identifies the neutral point relative to the
arithmetic carrier, while a change of coordinates transports the carrier
operations and that point together.

| Boundary | Example preparation | Minimum intervention cost | Explicit framed code | Code length |
|---|---|---:|---|---:|
| `0` | empty preparation | 0 | `0` | 1 bit |
| `-1` | one negative unit injection | 1 | `111` | 3 bits |
| `-16` | one negative unit injection, then a free radix step | 1 | `11000010000` | 11 bits |

The prefix code uses `0` for zero and `1 + sign bit + Elias-gamma magnitude`
for every nonzero integer. Its Kraft sum is exactly one. Thus it also defines
a probability reference `p(c)=2^(-length(c))`; its deterministic surprise is
the displayed bit length. Relative to the zero codeword, the two nonzero
examples require two and ten extra bits in this code.

Preparation cost and code length have different units. In particular,
infinitely many distinct states `-16^k` have preparation cost one, so the
counting-measure weights `exp(-beta*cost(c))` do not normalize. A probability
reference must be supplied separately. An empty word also cannot be one
member of a multiclass prefix code; a silent default needs external framing.

The universal-language strengthening is false. An optimal universal prefix
machine can reserve program `0` for `-1`, program `10` for `0`, and `11p`
for a universal simulation. Reversing the two reserved outputs reverses
their complexity order. This does not attack the author's relative claim;
it identifies why the carrier and its coding convention must remain explicit.
The deterministic Shannon entropies of all three point masses are zero.

Full derivations: [pointed preparation](POINTED_PREPARATION_AND_CAUSALITY.md),
PPC-01/02; [information and coding](INFORMATION_GEOMETRY_AND_CODING.md),
IGC-01--04 and section 3.1.

## 2. Causal neutrality selects the original retarded response

For a fixed integer radix `b>=2`, consider the exact recurrence

$$
U_n=bU_{n-1}+r_n.
$$

Require a response rule for every forcing stream, prefix causality including
time zero, and an unprepared zero-forcing response equal to zero. At time
zero every stream has the same empty observed history, so causality makes
its initial value independent of the future source. Neutrality then sets
that value to zero. Induction gives the unique response

$$
U_0=0,\qquad U_n=\sum_{k=1}^n b^{n-k}r_k.
$$

No separate linearity assumption is needed. In contrast, the homogeneous
coordinate `Y_n=b^(-n)U_n` preserves any constant seed in the absence of
forcing. Inertia alone therefore preserves an existing boundary; the
unprepared neutral reference selects which boundary is meant.

Minimizing a future terminal amplitude is a different optimization. Enforcing
`U_N=0` selects the anticipatory boundary

$$
c_N^{\rm adv}=-\sum_{k=1}^N b^{-k}r_k.
$$

A pulse after an observed prefix changes this seed and the earlier response.
For the authentic infinite BBP source the analogous compensating seed is
`-pi/16`, rather than the repository's original zero. The exact finite-prefix
test separates minimal initial preparation from future cancellation.

Coordinate changes also retain their hypotheses. A fixed translation by
`a` changes the forcing to `r_n+(b-1)a`; a moving homogeneous origin
`U_n-b^n a` preserves the forcing but changes the marked neutral reference.
There is no unqualified coordinate-free preference for the numeral zero.

Proofs: PPC-03 and sections 4--5 of
[POINTED_PREPARATION_AND_CAUSALITY.md](POINTED_PREPARATION_AND_CAUSALITY.md).

## 3. Minimal boundary information can preserve a nonempty field

In a joint space `(c,omega)`, the law `delta_0(dc)*nu(domega)` has exactly
zero actualized seed and any specified virtual law `nu`. That law need not
be symmetric: its supplied structure can be retained. A symmetric mixture
of nonzero seeds would instead have zero mean without having zero actual
seed. These are different mathematical states.

Let `N` be the neutral event in a joint boundary/virtual state space. Suppose
a declared reference `P_epsilon` assigns its complement probability
`epsilon`, with `0<epsilon<1`. For another law `Q`, set
`q=Q(N^c)`. Natural logarithms give costs in nats. The exact chain rule is

$$
D(Q\Vert P_\epsilon)
=d(q\Vert\epsilon)
 +(1-q)D(Q_0\Vert P_{\epsilon,0})
 +qD(Q_1\Vert P_{\epsilon,1}),
$$

where zero-mass conditional terms are omitted and

$$
d(q\Vert\epsilon)
=q\log\frac q\epsilon+(1-q)\log\frac{1-q}{1-\epsilon}.
$$

Consequently a fixed information budget `D(Q||P_epsilon)<=B` gives

$$
\boxed{q\le q_{\max}(B,\epsilon)
\le\min\left\{1,\frac{B+\log2}{\log(1/\epsilon)}\right\}.}
$$

The exact optimum `q_max` is the upper solution of `d(q||epsilon)=B`, unless
the budget already permits `q=1`. Its limiting scale is sharp:

$$
\boxed{q_{\max}(B,\epsilon)\log(1/\epsilon)\longrightarrow B}
\qquad(\epsilon\downarrow0,\ B\ge0\text{ fixed}).
$$

These are paper results for all stated parameters. The probe also certifies
finite examples with rational logarithm enclosures. At budget one nat:

| Reference nonneutral mass | Certified interval for maximum allowed nonneutral mass |
|---|---|
| `1/16` | `[0.594727889138, 0.594727889153]` |
| `1/65536` | `[0.123956463987, 0.123956464002]` |
| `1/2^64` | `[0.025193390887, 0.025193390903]` |

The displayed decimals are rounded outward from exact rational endpoints.
They also show that a finite budget need not force exact neutrality at a
fixed positive reference mass. The asymptotic theorem specifies the limit.

For a prescribed sector mass `q`, the least-information law is exactly

$$
Q_q^*=(1-q)P_\epsilon(\cdot\mid N)
       +qP_\epsilon(\cdot\mid N^c).
$$

It preserves both within-sector conditional laws, including the complete
virtual neutral field. Arbitrary laws in the information ball can spend
budget changing those conditionals, so exact field preservation is a
property of this minimizing lift. A hard reference with `P_0(N)=1` makes
any outside mass have infinite KL cost while still allowing a rich law
inside `N`.

A normalized operational realization is also available. If `P(N)=p0>0`,
cost `g` vanishes on `N`, and `g>=delta>0` outside, then
`dP_beta=exp(-beta*g)dP/Z_beta` preserves `P(.|N)` exactly and obeys

$$
P_\beta(N^c)\le
\frac{(1-p_0)e^{-\beta\delta}}
     {p_0+(1-p_0)e^{-\beta\delta}}.
$$

This uses a declared probability reference, so the infinite free-radix cost
shell causes no normalization failure.

Proofs: [INFORMATION_GEOMETRY_AND_CODING.md](INFORMATION_GEOMETRY_AND_CODING.md),
IGC-05/06/08. Exact receipts: [production probe](receipts/production_probe.json).

## 4. The exact boundary information lost by phase observation

Two solutions with the same forcing and seeds `c,d` satisfy

$$
U_n(c)-U_n(d)=b^n(c-d).
$$

For fixed integer frequency `h!=0`, the ratio of their phases is
`exp(2*pi*i*h*b^n*(c-d))`. For an observation starting at `N`, this gives
two different complete classifications:

| Observation | Necessary and sufficient condition for equality at every time from `N` |
|---|---|
| Absolute phases | `h*b^N*(c-d)` is an integer |
| All pairwise relative phases | `h*(b-1)*b^N*(c-d)` is an integer |

For all integer frequencies, the eventual absolute kernel is `Z[1/b]` and
the eventual relative kernel is `(1/(b-1))*Z[1/b]`. These statements concern
literal phases; a coarser Gram spectrum can erase still more information.

At radix 16 this implies:

- `0`, `-1`, and `-16` have identical absolute phases at every time.
- A seed offset `1/256` first becomes absolutely invisible at time two
  for frequency one.
- A seed offset `1/15` produces a constant phase rotation; it preserves
  every pairwise relative phase from time zero.
- A tiny offset `1/(2*h*16^K)` gives exactly opposite phases at time `K`,
  then identical phases from time `K+1`. An expanding real-state difference
  does not imply monotone phase separation.

The full real state with its known source prefix still recovers the seed:

$$
c=b^{-n}U_n-\sum_{k=1}^n b^{-k}r_k.
$$

Thus the preparation distinction is retained by one observable and erased
by another. Neither information geometry nor a phase statistic may silently
substitute one observation for the other.

Proofs: [OBSERVATION_QUOTIENT_AND_CONTROLS.md](OBSERVATION_QUOTIENT_AND_CONTROLS.md),
OQ-A/B/C and sections 1, 4.

## 5. What reaches the selected path, and where the proof stops

For fixed forcing and any seed-dependent observables `|A_N(c)|<=1`,

$$
\sup_{N\ge1}\left|\mathbb E_Q A_N(C)-A_N(0)\right|\le2Q(C\ne0).
$$

The bound is uniform in path length. It therefore transfers the information
boundary theorem to the authentic signed means

$$
A_N(c)=\frac1N\sum_{n=1}^N e^{2\pi i hU_n(c)}.
$$

It approximates the selected zero-seed mean; it does not make that mean
small. For a law supported on integer seeds the ensemble already equals
`A_N(0)` exactly, by the observation quotient above. Any claimed cancellation
from such an ensemble would need an independent source of signed control.

The coherent controls preserve the force of this limitation. For `d>=0`,
set

$$
R_d(a)=\frac{16}{(a+d)^2}-\frac1{(a+d+8)^2},\qquad
r_n^{(d)}=R_d(8n-7).
$$

Its zero-seeded solution is

$$
U_n^{(d)}=\frac{16^n}{(d+1)^2}-\frac1{(8n+d+1)^2}.
$$

The source is positive, has a full-support Laplace density, shares the
authentic leading scale `15/(64*n^2)`, and satisfies the parent's sufficient
criterion for arbitrary convolution roots. Yet `d=3` makes every nonzero
integer-frequency phase tend to one. Its forcing is strictly smaller than
the authentic forcing at every time. The `d=4` control retains odd reduced
state denominators and is coherent at frequency 25. These deliberately
changed sources refute generic positivity/minimality-to-cancellation claims;
they are not counterexamples to the authentic BBP conjecture.

The genuine remaining edge is a source-specific signed estimate for the
original four-pole forcing and its selected zero boundary. No new positive
field construction, entropy prior, or stronger origin preference supplied
here proves that estimate.

## 6. Relationship to the triangle and Gamma source work

The parent positive source remains

$$
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},\qquad
\mu_a(dx)=\frac{e^{-ax}(4-2e^{-3x}-e^{-4x}-e^{-5x})}{R(a)}\,dx,
\quad a>0.
$$

The no-information update preserves this law. A source tilt by `exp(-sX)`
gives `mu_(a+s)` and the exact Gibbs variational identity inherited from
the parent. A neutral actual seed can coexist with this nonempty virtual
field as `delta_0(dc)*mu_a(dx)`. Setting the positive source coordinate
`X` itself to zero would be a different, singular operation.

For an explicitly declared product coupling, boundary and source KL costs
add. A source-only tilt then leaves the boundary law unchanged. This identifies
the next missing interaction: a derived relation between the selected
arithmetic phase and the updating carrier. It cannot be supplied by an
unstated independence assumption. The source clock still starts at `a_1=1`;
no invalid positive density at `a_0=-7` is introduced.

The parent's nonlinear composition and convolution results and the siblings'
Gamma/Pascal constructions remain useful representations. This continuation
adds a boundary preparation theory and an exact observation quotient, without
claiming that those representations close the selected signed estimate.

## 7. Reading and reproduction map

| File | Purpose |
|---|---|
| [HOLE_CONTRACT.md](HOLE_CONTRACT.md) | Original relative claim, frontier, rejection controls, and stop condition |
| [POINTED_PREPARATION_AND_CAUSALITY.md](POINTED_PREPARATION_AND_CAUSALITY.md) | Preparation theorem, code, causal uniqueness, coordinate changes, and controls |
| [INFORMATION_GEOMETRY_AND_CODING.md](INFORMATION_GEOMETRY_AND_CODING.md) | Sharp KL bound, coding limitations, preserved neutral law, and source dual |
| [OBSERVATION_QUOTIENT_AND_CONTROLS.md](OBSERVATION_QUOTIENT_AND_CONTROLS.md) | Exact absolute/relative phase kernels and hostile coherent sources |
| [CLAIMS.md](CLAIMS.md) | Canonical scoped claim ledger |
| [VALIDATION.md](VALIDATION.md) | Commands, rational certificates, audit correction, and raw receipts |
| [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) | Exact source and executed-code pins |
| [NEXT.md](NEXT.md) | The remaining signed theorem and a finite falsification contract |

Executable implementations are
[`observational_succ/inertial_information_boundary.py`](../../../observational_succ/inertial_information_boundary.py),
the [production probe](../../../scripts/inertial_information_boundary_probe.py),
the [separate oracle](../../../scripts/inertial_information_boundary_oracle.py),
and [24 focused tests](../../../tests/test_inertial_information_boundary.py).
The oracle reconstructs its mechanisms without importing the new production
module. Both implementations share the pinned native arithmetic source;
their agreement is code separation, not independent scientific provenance.
