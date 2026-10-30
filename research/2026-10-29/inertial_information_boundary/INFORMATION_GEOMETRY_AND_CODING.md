# Relative information, explicit boundary codes, and a rich neutral field

**Date:** 2026-10-29. **Parent:** draft PR #367,
`b6a3815ceb505de0b1f570eae3ff5be75cdbe99c`.
**Branch:** `research/inertial-information-boundary-2026-10-29`.
**Authority:** complete paper proofs and explicit counterconstructions below.
The identities use classical information theory; their assembly is a scoped
SUCC construction, with no academic-priority claim. This file reports no
executable-test count, hosted CI result, or formal-proof certificate.

The author's relative claim survives in a precise form: a declared carrier can
make its neutral preparation least costly while preserving a nonempty virtual
fiber. The reference carrier, admissible preparations, communication protocol,
and reference probability must be stated. Preparation cost, Shannon entropy,
code length, and relative entropy measure different objects. Their differences
do not refute the relative claim; they determine which version is proved.

The principal quantitative result is this. If a reference assigns probability
`epsilon` to leaving the neutral fiber, every law within a fixed KL budget `B`
assigns that event probability at most

$$
 \min\left\{1,\frac{B+\log 2}{\log(1/\epsilon)}\right\}.
$$

The exact optimum has leading behavior `B/log(1/epsilon)` when `B>0` is fixed.
The complete law inside the neutral fiber can remain nontrivial. This theorem
controls a probability law on boundary choices; it supplies no signed
cancellation theorem for the selected zero-seeded arithmetic trajectory.

## 1. Contract, live frontier, and conventions

The governing local statement and rejection controls are in
[HOLE_CONTRACT.md](HOLE_CONTRACT.md). The original forcing and zero seed remain
those of the parent: `U_0=0`, `U_n=16U_(n-1)+r(n)`, with the authentic four-pole
function `r(n)=R(8n-7)`. The inherited positive source and its exact information
dual are established in
[DUAL_GEOMETRY_AND_GAMMA.md](../recursive_carrier_triangle/DUAL_GEOMETRY_AND_GAMMA.md),
especially DG-11 and DG-12. No imported theorem or archival original is edited.

The following sibling drafts were read as frontier context, **not imported as
premises**:

| Sibling and exact inspected head | Relevant context | Remaining boundary stated there |
|---|---|---|
| [PR #369](https://github.com/femboy2112/SUCC/pull/369), `95f368719a1e020e8bf5b9312b10260a94a0a519` | [Scalar source reweighting and diagonal-unitary Gram obstruction](https://github.com/femboy2112/SUCC/blob/95f368719a1e020e8bf5b9312b10260a94a0a519/research/2026-10-29/triangular_harmonic_gamma_bbp/TRIANGULAR_HARMONIC_GAMMA_BBP.md), sections E-F; [exact positive Green-mixture update](https://github.com/femboy2112/SUCC/blob/95f368719a1e020e8bf5b9312b10260a94a0a519/research/2026-10-29/triangular_harmonic_gamma_bbp/CROSS_SOURCE_GREEN_SHEET.md), sections 2-3 | Positive source identities and gauge-invariant spectra do not select or control the genuine signed seed. |
| [PR #370](https://github.com/femboy2112/SUCC/pull/370), `4d4d49b575b476cc33f762d2b6a7fd6d1b924655` | [Positive Pascal/Oily observation and bounded-sequence inverse](https://github.com/femboy2112/SUCC/blob/4d4d49b575b476cc33f762d2b6a7fd6d1b924655/research/2026-10-29/pascal_oily_bbp/PASCAL_OILY_SIGNED_LIFT.md), sections 5-7 | The transfer preserves the original signed-mean problem, including coherent controls. |

This round therefore treats boundary selection and its information cost
directly. It does not invoke a stronger positive field as a substitute for a
boundary rule.

Except where a subscript `2` or the word **bits** appears, logarithms are
natural and KL costs are in **nats**. Binary strings are finite. A prefix code
contains no distinct pair for which one string is a prefix of the other. For
probability measures, use

$$
 D(Q\Vert P)=\int\log\frac{dQ}{dP}\,dQ
$$

when `Q` is absolutely continuous with respect to `P`, and `+infinity`
otherwise. The usual extended-real conventions apply, including `0 log 0=0`.
Total variation is `sup_E |Q(E)-P(E)|`, half the density `L1` distance when
densities exist.

## 2. What information about a fixed boundary actually means

**IGC-01 — deterministic entropy and relative surprise (CLASSICAL, proof
included).** For every fixed value `c`, the categorical random variable that
equals `c` with probability one has Shannon entropy zero:

$$
 H_2(\delta_c)=-1\log_2 1=0.
$$

In particular, the deterministic laws at `0`, `-1`, and `-16` all have zero
Shannon entropy. This says nothing about their relative preparation or
description costs. If a declared reference law `P` assigns a positive atom to
`c`, then

$$
 D(\delta_c\Vert P)=-\log P(\{c\}).
 \tag{IGC-1}
$$

Indeed the density ratio at that atom is `1/P({c})`. If `P({c})=0`, the
relative entropy is infinite instead. For a nonatomic real reference this
happens for every exact point, including zero. No differential entropy of a
Dirac mass is used here. Shannon's original entropy definition and its
zero-entropy characterization are in [S1], section 6.

This distinction permits the author's intended ordering: a reference that
privileges neutral preparation can make zero less surprising than a paid
displacement. The ordering is relative to that reference. It is not obtained
by comparing the three zero values of categorical Shannon entropy.

### 2.1 Universal description complexity does not give a fixed-numeral ranking

**IGC-02 — explicit universal countercoding (PROVED LOCAL (paper); classical
algorithmic framework).** Fix an optimal universal prefix machine `V` whose
outputs use a fixed effective encoding of integers. Define two partial
machines by the following complete rules:

| Program | `M_minus` output | `M_zero` output |
|---|---:|---:|
| `0` | `-1` | `0` |
| `10` | `0` | `-1` |
| `11p`, for `p` in the domain of `V` | `V(p)` | `V(p)` |

They are undefined on every other program. Both domains are prefix free:
the first branches `0`, `10`, and `11` are mutually incompatible, and the
last branch inherits the prefix property of `V`. Both machines remain
optimal universal machines because they simulate `V` with two extra bits.
An optimal universal prefix machine cannot halt on the empty string: that
would exclude every other program and prevent universality. Thus every
simulation branch here has length at least three. It follows exactly that

$$
 \begin{aligned}
 K_{M_{\rm minus}}(-1)&=1,& K_{M_{\rm minus}}(0)&=2,\\
 K_{M_{\rm zero}}(0)&=1,& K_{M_{\rm zero}}(-1)&=2.
 \end{aligned}
 \tag{IGC-2}
$$

This is a literal reversal between two universal prefix machines, not an
appeal to arbitrary nonuniversal lookup tables. The invariance theorem bounds
the difference between optimal-machine complexities by a machine-dependent
additive constant; it does not fix the order of particular short numerals.
Chaitin's original prefix-machine definition and optimal-universality theorem
are in [S2], section 2. The two machines above are fully specified here.

The faithful carrier-relative statement can still fix its own machine or
preparation grammar and prove a zero preference there. IGC-02 rejects only
the stronger assertion that every universal description language must rank
zero ahead of every nonzero boundary.

### 2.2 A silent default needs an agreed frame

**IGC-03 — empty-code obstruction (PROVED LOCAL (paper)).** A prefix code containing
the empty word can contain no other word, because the empty word is a prefix
of every word. Equivalently, its one Kraft contribution is already `2^0=1`.

A protocol can still declare that no message during an agreed observation
slot means “leave the carrier at its neutral default.” The slot, termination
event, or other framing must then be supplied by the protocol. An empty
payload and a self-delimiting zero-length member of a multiclass prefix code
are different constructions. Zero physical preparation cost also need not
equal zero transmitted bits.

## 3. An explicit integer code that favors the declared neutral boundary

For `m>=1`, let `k=floor(log_2 m)`, write `bin(m)` for its `k+1` binary digits,
and define the Elias-gamma word

$$
 \gamma(m)=0^k\,\operatorname{bin}(m),
 \qquad |\gamma(m)|=2k+1.
$$

Here the first nonzero bit tells the decoder how many following bits to read.
Define a signed-integer code `C` by

$$
 C(0)=0,\qquad
 C(z)=1\,\sigma(z)\,\gamma(|z|)\quad(z\ne0),
 \tag{IGC-3}
$$

where `sigma(z)=0` for positive `z` and `sigma(z)=1` for negative `z`.
Elias's original integer-coding paper is [S3]. The length, decoding, and
normalization properties needed here are proved directly below; no external
average-performance theorem is assumed.

**IGC-04 — exact lengths and Kraft mass (PROVED LOCAL (paper)).** The code is
prefix free, is uniquely decodable by the displayed rule, and has lengths

$$
 \ell(0)=1,\qquad
 \ell(z)=2\lfloor\log_2|z|\rfloor+3\quad(z\ne0).
 \tag{IGC-4}
$$

| Boundary | Codeword | Length in bits | Induced reference mass |
|---|---|---:|---:|
| `0` | `0` | 1 | `1/2` |
| `-1` | `111` | 3 | `1/8` |
| `-16` | `11000010000` | 11 | `1/2048` |

**Proof.** The initial bit separates zero from nonzero values; the second
bit separates the two signs. In each sign branch, reading `k` initial zeros
of `gamma(m)`, then its leading one and exactly `k` more bits, recovers one
positive integer with no ambiguity. Thus no word extends another. For each
`k>=0`, there are `2^(k+1)` signed integers with magnitude in
`[2^k,2^(k+1)-1]`, each of length `2k+3`. Consequently,

$$
 \sum_{z\in\mathbb Z}2^{-\ell(z)}
 =\frac12+\sum_{k=0}^{\infty}
   2^{k+1}2^{-(2k+3)}
 =\frac12+\sum_{k=0}^{\infty}2^{-(k+2)}=1.
 \tag{IGC-5}
$$

The exact partial Kraft sum through magnitude `2^(K+1)-1` is
`1-2^(-(K+2))` for every integer `K>=0`. More generally, for `M>=1`, put
`K=floor(log_2 M)` and `t=M-2^K+1`. The sum through `|z|<=M` is

$$
 1-2^{-(K+1)}+t\,2^{-(2K+2)}.
 \tag{IGC-6}
$$

These formulas provide exact finite rejection receipts for a wrong sign bit,
wrong gamma length, or incorrect normalization. QED.

Because the Kraft sum equals one, `p_C(z)=2^(-ell(z))` is a probability law.
Its point surprise in bits is exactly `ell(z)`. For any probability `rho`
with finite mean code length, direct expansion gives

$$
 \sum_{c\in\mathbb Z}\rho(c)\ell(c)
 =H_2(\rho)+D_2(\rho\Vert p_C).
 \tag{IGC-7}
$$

For a deterministic boundary, the first term is zero and the whole code
length is its relative divergence from this declared reference. Zero is the
unique shortest codeword in this code. The excess lengths relative to the
neutral code are `0`, `2`, and `10` bits for the three displayed boundaries;
those excess lengths are not themselves a multiclass prefix code with an
empty zero word. IGC-02 explains why this useful construction is not a
machine-independent simplicity theorem.

### 3.1 Preparation cost does not automatically supply a coding prior

Suppose the preparation grammar starts at zero, counts unit injections at
cost one, and allows sign changes and radix multiplication by 16 for free.
Free operations preserve zero, while one unit injection followed by a sign
change and `k` radix multiplications reaches `-16^k`. Thus, for every `k>=0`,
the minimal injection cost of `-16^k` is exactly one. These are infinitely
many distinct states in one cost shell. Therefore, for every finite
`beta>=0`,

$$
 \sum_{c\in\mathbb Z}e^{-\beta\,\operatorname{cost}(c)}
 \ \ge\ \sum_{k=0}^{\infty}e^{-\beta}=+\infty.
 \tag{IGC-8}
$$

The uniform-counting Gibbs expression cannot be normalized. By contrast,
the explicit code above assigns length `8k+3` to `-16^k`. The preparation
cost counts paid interventions; the code also describes which free radix
operations were used. Their differing costs are consistent. A separately
declared probability reference makes a Gibbs update well defined, as proved
in section 6.

## 4. The quantitative information boundary

Let `S` be a measurable state space, `mathcal N` a measurable **neutral
fiber**, and `P_epsilon` a probability with

$$
 P_\epsilon(\mathcal N^c)=\epsilon,
 \qquad 0<\epsilon<1.
$$

The fiber can contain arbitrarily many virtual states. For example, in a
space of pairs `(c,omega)`, take `mathcal N={0} x Omega`. Write
`P_(epsilon,0)` and `P_(epsilon,1)` for the two conditional probability laws
on `mathcal N` and `mathcal N^c`. Let `Q` be any probability and set
`q=Q(mathcal N^c)`. Define

$$
 d(q\Vert\epsilon)
 =q\log\frac q\epsilon
 +(1-q)\log\frac{1-q}{1-\epsilon},
 \qquad 0\le q\le1.
 \tag{IGC-9}
$$

### 4.1 Exact chain rule, equality, and support

**IGC-05 — binary coarse-graining with retained fibers (PROVED LOCAL (paper);
classical KL identity).** With conditional laws `Q_0,Q_1` on positive-mass
sectors,

$$
 \boxed{
 D(Q\Vert P_\epsilon)
 =d(q\Vert\epsilon)
 +(1-q)D(Q_0\Vert P_{\epsilon,0})
 +qD(Q_1\Vert P_{\epsilon,1})
 \ \ge\ d(q\Vert\epsilon).}
 \tag{IGC-10}
$$

A zero-mass conditional term is omitted. The equality is valid in the
extended-real sense. Equality in the final inequality holds exactly when
the conditional laws agree on every sector given positive mass by `Q`.

**Proof.** For `0<q<1` and `Q` absolutely continuous with respect to
`P_epsilon`, the density ratio on `mathcal N` is
`[(1-q)/(1-epsilon)] dQ_0/dP_(epsilon,0)`. The corresponding ratio on the
complement is `[q/epsilon] dQ_1/dP_(epsilon,1)`. Integrate their logarithms
against the two components of `Q`. This gives IGC-10. If either conditional
law has a singular component, both the corresponding conditional divergence
and the full divergence are infinite. For `q=0` or `q=1`, the same computation
has only one component. Nonnegativity and its equality condition finish the
proof. QED.

In particular, for any prescribed `q`, the unique least-information law with
that sector mass is

$$
 Q_q^*=(1-q)P_{\epsilon,0}+qP_{\epsilon,1},
 \qquad D(Q_q^*\Vert P_\epsilon)=d(q\Vert\epsilon).
 \tag{IGC-11}
$$

It retains the complete conditional virtual law in the neutral fiber. At
`q=0`, that conditional law remains a probability, not an empty state space.
The exact cost of this hard conditioning is
`D(P_(epsilon,0)||P_epsilon)=-log(1-epsilon)`.

If instead a reference `P_0` already satisfies `P_0(mathcal N)=1`, then every
law assigning positive mass outside the neutral fiber has
`D(Q||P_0)=+infinity`. Finite relative entropy can still modify the law inside
the fiber. Thus a hard neutral reference is a declared support restriction;
it does not erase virtual states that lie within that support.

### 4.2 A uniform finite-budget bound

Put `L_epsilon=log(1/epsilon)` and
`h_b(q)=-q log q-(1-q)log(1-q)`. Expanding IGC-9 gives

$$
 d(q\Vert\epsilon)
 =qL_\epsilon-h_b(q)
 +(1-q)\log\frac1{1-\epsilon}
 \ \ge\ qL_\epsilon-\log2.
 \tag{IGC-12}
$$

The last step uses the elementary binary-entropy maximum `h_b(q)<=log 2`.
Therefore, for every `B>=0`,

$$
 \boxed{D(Q\Vert P_\epsilon)\le B
 \quad\Longrightarrow\quad
 q\le\min\left\{1,\frac{B+\log2}{L_\epsilon}\right\}.}
 \tag{IGC-13}
$$

For fixed `B`, every such family `Q_epsilon` has nonneutral mass tending to
zero as `epsilon` tends to zero. The same conclusion holds for varying
budgets `B_epsilon=o(L_epsilon)`. At any fixed positive `epsilon`, finite
budget does not generally imply exact zero mass: the unchanged law
`Q=P_epsilon` has zero KL cost and nonneutral mass `epsilon`.

Concentration of the sector label also need not force
`Q_0=P_(epsilon,0)`: the remaining budget can be spent inside the neutral
fiber. For `q<1`, IGC-10 gives the explicit bound

$$
 D(Q_0\Vert P_{\epsilon,0})
 \le\frac{B-d(q\Vert\epsilon)}{1-q}.
 \tag{IGC-14}
$$

Field preservation is exact for the minimizing lift IGC-11; arbitrary
finite-budget laws have the weaker statement IGC-14.

### 4.3 The optimal mass and its sharp asymptotic scale

**IGC-06 — exact budget optimization (PROVED LOCAL (paper); classical binary-KL
specialization).** Define

$$
 q_{\max}(B,\epsilon)
 =\max\{q\in[0,1]:d(q\Vert\epsilon)\le B\}.
 \tag{IGC-15}
$$

This is also the exact largest nonneutral mass among all laws satisfying
`D(Q||P_epsilon)<=B`, because IGC-11 realizes every feasible binary mass.
Its complete characterization is:

- If `B>=L_epsilon`, then `q_max=1`.
- If `0<=B<L_epsilon`, it is the unique solution in `[epsilon,1)` of
  `d(q||epsilon)=B`; at `B=0` it equals `epsilon`.
- For every fixed `B>=0`,

$$
 \boxed{\lim_{\epsilon\downarrow0}
 q_{\max}(B,\epsilon)\log(1/\epsilon)=B.}
 \tag{IGC-16}
$$

**Proof.** The feasible set is closed and nonempty, since it contains
`epsilon`. On `(epsilon,1)`,

$$
 \frac{\partial}{\partial q}d(q\Vert\epsilon)
 =\log\frac{q(1-\epsilon)}{\epsilon(1-q)}>0.
$$

Moreover `d(epsilon||epsilon)=0` and `d(1||epsilon)=L_epsilon`.
This proves the characterization. For the limit, IGC-13 first forces
`q_max` to zero at fixed `B`. Rearranging IGC-12 before its last estimate
gives

$$
 q_{\max}L_\epsilon
 \le B+h_b(q_{\max})\longrightarrow B
$$

as an upper-limit bound. If `B>0`, then for sufficiently small `epsilon`,

$$
 q_\epsilon^-
 =\frac{B+\log(1-\epsilon)}{L_\epsilon}
$$

lies in `[0,1]`. Since `-h_b(q)<=0` and
`(1-q)log(1/(1-epsilon))<=log(1/(1-epsilon))`,

$$
 d(q_\epsilon^-\Vert\epsilon)
 \le q_\epsilon^-L_\epsilon+\log\frac1{1-\epsilon}=B.
$$

Hence `q_max>=q_epsilon^-` and the lower limit of `q_max L_epsilon` is at
least `B`. At `B=0`, `q_max=epsilon` and `epsilon log(1/epsilon)->0`.
This proves IGC-16. QED.

For fixed positive budget the `1/log(1/epsilon)` scale is therefore optimal
over all laws in the KL ball. A generic faster rate cannot follow from that
budget assumption alone.

## 5. What the boundary bound transfers to a selected arithmetic path

Fix one forcing sequence and its deterministic trajectory for each seed `c`.
For every integer `N>=1`, let `A_N(c)` be any measurable complex observable
with `|A_N(c)|<=1`. On the joint seed/virtual state space, assume the neutral
fiber is exactly the event `C=0`. The observable here depends on the seed
through its deterministic path, not on an arbitrary additional virtual
coordinate.

**IGC-07 — uniform bounded-observable transfer (PROVED LOCAL (paper)).** If
`q=Q(C!=0)`, then

$$
 \boxed{\sup_{N\ge1}
 \left|\mathbb E_Q A_N(C)-A_N(0)\right|\le2q.}
 \tag{IGC-17}
$$

**Proof.** The difference is
`integral_(C!=0) [A_N(C)-A_N(0)] dQ`, whose integrand has modulus at most
two. The bound is independent of `N`. QED.

The constant two is optimal for unrestricted bounded observables: choose
`A_N(0)=1` and `A_N(c)=-1` for every nonzero seed. No optimality claim for
the actual BBP Weyl observables is made. If the observable varies within the
neutral fiber, its neutral conditional expectation must be retained; IGC-17
cannot silently replace it by one chosen microstate.

In particular, fix the original forcing and an integer frequency `h`, and
take

$$
 A_N(c)=\frac1N\sum_{n=1}^{N}
        e^{2\pi i hU_n(c)},
 \qquad U_n(c)=16^n c+U_n(0).
 \tag{IGC-18}
$$

Combining IGC-13 and IGC-17 gives an all-`N` approximation to the genuine
selected mean:

$$
 \sup_{N\ge1}\left|\mathbb E_Q A_N(C)-A_N(0)\right|
 \le 2q_{\max}(B,\epsilon)
 \le2\min\left\{1,\frac{B+\log2}{\log(1/\epsilon)}\right\}.
 \tag{IGC-19}
$$

This transports an ensemble toward the chosen zero seed. It does not bound
`|A_N(0)|` by a quantity tending to zero in `N`: the ensemble mean might
have the same coherence as the selected path. Even the choice `Q(C=0)=1`
leaves the signed-mean problem unchanged. An independently proved
cancellation estimate for a suitable ensemble could be transferred through
IGC-19, but the information-budget theorem supplies no such estimate.

There is a particularly direct observation guard for the integer code of
section 3. For every integer seed `c`, every integer frequency `h`, and every
`n>=0`, `h16^n c` is an integer. Thus the phases in IGC-18 are exactly the
zero-seed phases. Any prior supported on integer seeds gives
`E A_N(C)=A_N(0)` without any concentration argument. Code-length distinctions
among `0`, `-1`, and `-16` are real distinctions of unwrapped preparation;
this particular phase observation erases them. It cannot certify their
preparation costs.

Algorithmic simplicity has a separate boundary as well. For the fixed
computable rational source and a fixed rational seed, an exact rational
`U_n(c)` can be produced by a fixed program given `n`; its conditional
description length is bounded independently of `n`. For a computable real
seed, the analogous statement concerns approximations given `n` and a
precision request. Neither statement supplies empirical digit frequencies,
Martin-Lof randomness, or a lower bound on output complexity. The special
seed `-pi/16` also has a short description relative to the full known source;
its dependence on that source's future tail is a different question from
prefix causality. A short formula is not a free causal preparation rule.

## 6. A normalized reference-weighted Gibbs realization

The divergence in IGC-8 shows why a resource cost requires a reference before
it can define a probability law. The following construction supplies a
compatible realization and retains the neutral fiber exactly.

**IGC-08 — Gibbs selection with preserved neutral conditionals (PROVED LOCAL (paper); classical variational identity).** Let `P` be a probability, let
`mathcal N` be measurable with `p0=P(mathcal N)>0`, and let `g:S->[0,infinity)`
be finite `P`-almost everywhere. Suppose

$$
 g=0\ \text{on }\mathcal N,\qquad
 g\ge\delta>0\ \text{on }\mathcal N^c
 \quad(P\text{-almost everywhere}).
$$

For every `beta>0`, define

$$
 Z_\beta=\int e^{-\beta g}\,dP,
 \qquad
 dP_\beta=\frac{e^{-\beta g}}{Z_\beta}\,dP.
 \tag{IGC-20}
$$

Then `p0<=Z_beta<=1`, so this is always normalized. Its nonneutral mass
satisfies

$$
 \boxed{\epsilon_\beta:=P_\beta(\mathcal N^c)
 \le\frac{(1-p_0)e^{-\beta\delta}}
             {p_0+(1-p_0)e^{-\beta\delta}}.}
 \tag{IGC-21}
$$

Furthermore,

$$
 P_\beta(\,\cdot\mid\mathcal N)=P(\,\cdot\mid\mathcal N),
 \qquad
 \operatorname{TV}\bigl(P_\beta,P(\,\cdot\mid\mathcal N)\bigr)
 =\epsilon_\beta.
 \tag{IGC-22}
$$

It uniquely minimizes

$$
 \beta\mathbb E_Q g+D(Q\Vert P),
 \qquad \inf_Q\{\beta\mathbb E_Q g+D(Q\Vert P)\}=-\log Z_\beta.
 \tag{IGC-23}
$$

**Proof.** Write `T_beta=integral_(N^c) exp(-beta g)dP`. Then
`Z_beta=p0+T_beta` and `T_beta<=(1-p0)exp(-beta delta)`. The map
`t/(p0+t)` increases in `t`, proving IGC-21. The weight is constant one on
the neutral fiber, which proves the conditional identity. When
`epsilon_beta>0`, the mixture
`P_beta=(1-epsilon_beta)P(.|N)+epsilon_beta P_beta(.|N^c)` has disjoint
sectors, proving the exact total variation formula. At `epsilon_beta=0`,
the two probability laws coincide and that formula is immediate.

For competitors with finite displayed cost, the logarithmic density ratio
gives

$$
 D(Q\Vert P_\beta)
 =D(Q\Vert P)+\beta\mathbb E_Q g+\log Z_\beta.
$$

The optimizer is admissible: `g exp(-beta g)<=1/(e beta)` makes its mean
cost finite, and its logarithmic density ratio then makes its KL cost
finite. Nonnegativity of relative entropy proves the optimum and uniqueness.
Infinite-cost competitors cannot improve it. QED.

If `g=delta` on the entire complement, IGC-21 is an equality. The construction
therefore gives an explicit rare-intervention reference without equating
intervention cost and code length. The source of `P`, the definition of `g`,
and their units remain declared data. For example, one may choose the
integer code law of section 3 and a source-provided conditional virtual law;
the choice of that code law is not forced by the BBP recurrence.

## 7. The exact authentic-source information update

For every `a>0`, retain the parent's original positive source

$$
 Q_{\rm src}(x)=4-2e^{-3x}-e^{-4x}-e^{-5x},\qquad x>0,
$$

$$
 R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},\qquad
 \mu_a(dx)=\frac{e^{-ax}Q_{\rm src}(x)}{R(a)}\,dx.
 \tag{IGC-24}
$$

The source is strictly positive on `x>0` because
`Q_src(x)=2(1-exp(-3x))+(1-exp(-4x))+(1-exp(-5x))`. For `s>=0`,

$$
 Z_a(s)=\frac{R(a+s)}{R(a)},\qquad
 \mu_{a+s}(dx)=\frac{e^{-sx}}{Z_a(s)}\mu_a(dx).
 \tag{IGC-25}
$$

**IGC-09 — authentic field update (CLASSICAL; inherited specialization;
proof restated).** For all `a>0,s>=0`,

$$
 \boxed{-\log Z_a(s)
 =\min_\nu\{s\mathbb E_\nu X+D(\nu\Vert\mu_a)\},
 \qquad\nu_{\rm unique}=\mu_{a+s}.}
 \tag{IGC-26}
$$

The domain consists of probability laws with finite first moment and finite
KL cost, with infinite-cost laws admitted without changing the infimum.
For finite-cost competitors,

$$
 D(\nu\Vert\mu_{a+s})
 =D(\nu\Vert\mu_a)+s\mathbb E_\nu X+\log Z_a(s).
$$

The optimizer has finite moments and finite divergence, so nonnegativity
proves the statement, including `s=0`. Every finite tilt preserves the
positive density on `x>0`. The no-information update returns `mu_a` exactly.
This is DG-11 of the parent, not a new entropy principle.

The source coordinate `X>0` is a virtual microstate, not the arithmetic seed.
The probability `delta_0(dc) mu_a(dx)` has a neutral actual seed and a rich
source microfield simultaneously. Identifying arithmetic neutrality with
the event `X=0` would instead choose a `mu_a`-null event and change the model.
The valid source clock starts with `a_1=1`; this construction does not
introduce a positive law at the invalid parameter `a_0=-7`.

### 7.1 An exact budget split for a declared product coupling

**IGC-10 — boundary and source information add (PROVED LOCAL (paper); product
coupling explicitly assumed).** Let `nu` be any fixed probability on real
seeds with `nu({0})=0`. For `q in [0,1]`, define

$$
 \rho_q=(1-q)\delta_0+q\nu.
$$

For `a,b>0` and `0<epsilon<1`, set

$$
 P_{\epsilon,a}=\rho_\epsilon\otimes\mu_a,
 \qquad Q_{q,b}=\rho_q\otimes\mu_b.
$$

These are declared joint models; independence between seed and microstate
has not been derived from arithmetic digit dynamics. Nevertheless, their
relative information cost is exact:

$$
 \boxed{D(Q_{q,b}\Vert P_{\epsilon,a})
 =d(q\Vert\epsilon)+D(\mu_b\Vert\mu_a).}
 \tag{IGC-27}
$$

If `F(a)=log R(a)` and `m(b)=E_mu_b X=-F'(b)`, then the second term is

$$
 D(\mu_b\Vert\mu_a)=F(a)-F(b)+(a-b)m(b).
 \tag{IGC-28}
$$

**Proof.** The logarithmic product density ratio is the sum of a seed term
and a source term. Integration splits their expectations. The seed term is
IGC-11 because both laws retain the same nonneutral conditional `nu`.
The source ratio is `exp(-(b-a)x)R(a)/R(b)`, which gives IGC-28. All source
first moments and divergences are finite for positive parameters. QED.

Thus, within this declared family, a fixed source move from `a` to `b`
spends a known amount of budget. If the total available budget is `B` and
the source cost is `J<=B`, the sharp remaining boundary bound is
`q<=q_max(B-J,epsilon)`. If `J>B`, no member of that family satisfies the
budget. This is a new comparison within this dossier, not a proof that the
authentic arithmetic path samples this product law.

There is also an exact information-loss control. Observing only `X` in this
model gives the same marginal `mu_a` for every seed law `rho`. An update
whose density is only the source tilt `exp(-sX)/Z_a(s)` sends
`rho x mu_a` to `rho x mu_(a+s)` and leaves `rho` unchanged. Positive-field
observation or source tilt alone therefore cannot choose among those seed
laws. A source-derived correlation with the actual seed would be additional
mathematical structure; it cannot be supplied by an unstated product
assumption or by the positivity of `mu_a`.

## 8. Primary literature and precise claim scopes

The proofs above are included to make their hypotheses independently
auditable. These references ground the classical terminology and inference
framework. They do not establish SUCC's carrier choice or pi normality.

| Reference | Primary source and verified location | Scope used here |
|---|---|---|
| S1 | C. E. Shannon, *A Mathematical Theory of Communication*, Bell System Technical Journal 27 (1948), 379-423 and 623-656; [original-paper reprint](https://home.csulb.edu/~cwallis/382/readings/482/shannon.mathematical.theory.communication.1948.pdf), section 6, reprint p. 11 | Shannon entropy is a functional of a distribution. Every certain categorical outcome has entropy zero; binary entropy is at most one bit. It does not rank named certain outcomes by preparation cost. |
| S2 | G. J. Chaitin, *A Theory of Program Size Formally Identical to Information Theory*, Journal of the ACM 22 (1975), 329-340; [original paper](https://users.cs.fiu.edu/~giri/teach/5420/f01/papers/p329-chaitin.pdf), section 2, especially the optimal-universal-computer definition and Theorem 2.2; [author-institution record](https://research.ibm.com/publications/a-theory-of-program-size-formally-identical-to-information-theory) | Prefix programs and universality with additive simulation overhead. IGC-02 supplies its own explicit machine pair, so no language-independent short-numeral ranking is attributed to the paper. |
| S3 | P. Elias, *Universal Codeword Sets and Representations of the Integers*, IEEE Transactions on Information Theory 21 (1975), 194-203; [original publisher record](https://ieeexplore.ieee.org/abstract/document/1055349), DOI [10.1109/TIT.1975.1055349](https://doi.org/10.1109/TIT.1975.1055349) | Primary provenance for universal integer prefix coding. The publisher abstract was verified; the exact signed code, its gamma convention, all lengths, and Kraft identities used here are explicitly proved in section 3. No uninspected average-performance theorem is invoked. |
| S4 | E. T. Jaynes, *Information Theory and Statistical Mechanics*, Physical Review 106 (1957), 620; [original publisher abstract](https://journals.aps.org/pr/abstract/10.1103/PhysRev.106.620) | Maximum entropy is inference from specified partial information. The state space and known properties precede the probabilistic inference. This does not mean maximum structured complexity or justify replacing a known source law by an unconstrained uniform one. |
| S5 | J. E. Shore and R. W. Johnson, *Axiomatic Derivation of the Principle of Maximum Entropy and the Principle of Minimum Cross-Entropy*, IEEE Transactions on Information Theory 26 (1980), 26-37; [original paper](https://bayes.wustl.edu/Manual/AxiomaticDerivation.pdf), sections I-III; DOI [10.1109/TIT.1980.1056144](https://doi.org/10.1109/TIT.1980.1056144) | A declared prior, expectation constraints, and consistency conditions for inference. Their term “cross-entropy” here denotes the relative entropy `D(Q||P)`, not merely the modern cross-entropy `-E_Q log p`. The general discrete claim must be read with S6. |
| S6 | R. W. Johnson and J. E. Shore, *Comments on and Correction to “Axiomatic Derivation of the Principle of Maximum Entropy and the Principle of Minimum Cross-Entropy”*, IEEE Transactions on Information Theory 29 (1983), 942-943; [original correction PDF](https://zenodo.org/records/1281600/files/article.pdf), section II, Axiom V; [record](https://zenodo.org/records/1281600), DOI [10.1109/TIT.1983.1056747](https://doi.org/10.1109/TIT.1983.1056747) | The authors corrected the discrete sufficiency claim and added null-information invariance `p o 1=p`. The primary PDF's indexed text and article metadata were verified; direct PDF retrieval was unreliable. The unchanged-prior assertion used here is also proved directly by KL nonnegativity. |

The correction's succinct motivation is: “In the absence of new information,
we should not change our prior estimate.” This supports a relative
information-update axiom, with its prior explicitly retained. It is not a
derivation of classical inertia or of the arithmetic zero seed.

Maximum support or maximum Shannon entropy also need not mean maximum
structured complexity. Independent fair bits maximize binary entropy rate
while their past and future are independent. If the source already supplies
correlations, erasing those correlations by an unjustified independence
assumption changes the reference information. The operative prescription
here is to preserve supplied possibilities and relations, then change the
reference only as required by the declared constraints.

## 9. Claim ledger, receipts, and the remaining edge

| Claim | Earned status and supporting receipt | Cheapest falsification opportunity / scope guard |
|---|---|---|
| IGC-01 | CLASSICAL; direct entropy and point-divergence calculation | Compare `delta_0`, `delta_-1`, `delta_-16`; do not substitute one differential entropy for categorical entropy. |
| IGC-02 | PROVED LOCAL (paper); two explicit optimal universal prefix machines | Check domains and the exact one-bit/two-bit programs; a simulation branch cannot undercut them. |
| IGC-03 | PROVED LOCAL (paper); empty word prefixes every word | Add any second codeword and prefix-freeness immediately fails. |
| IGC-04 | PROVED LOCAL (paper); decoder, lengths, full and partial Kraft sums | The contract's signed-integer holdouts must agree with IGC-4 and IGC-6; no run is claimed in this file. |
| IGC-05 | PROVED LOCAL (paper)/classical; exact conditional density factorization | Change a within-sector conditional: the omitted nonnegative KL term must reappear. |
| IGC-06 | PROVED LOCAL (paper)/classical; monotonic binary divergence and matching asymptotic bounds | `B=0` gives `q=epsilon`; `B>=log(1/epsilon)` permits `q=1`. |
| IGC-07 | PROVED LOCAL (paper); integral over the nonneutral event | A neutral-fiber-dependent observable violates the stated reduction unless its conditional expectation is retained. |
| IGC-08 | PROVED LOCAL (paper)/classical; normalized reference-weighted Gibbs identity | Counting measure on the free-radix unit-cost shell fails by IGC-8; dropping the positive cost gap removes IGC-21. |
| IGC-09 | CLASSICAL; inherited specialization; parent DG-11 and its density identity | A tilt with the wrong normalizer is not a probability; arithmetic seed and positive source coordinate must remain distinct. |
| IGC-10 | PROVED LOCAL (paper); exact product likelihood factorization | Correlating seed and microstate changes the product premise and can change the budget split. |
| “Zero is simplest in every universal language” | REFUTED by IGC-02 | This stronger claim is not the author's carrier-relative claim. |
| “Bounded KL proves exact neutral mass at fixed positive epsilon” | REFUTED by `Q=P_epsilon` | The actual theorem is a quantitative rare-reference limit. |
| “Neutral boundary selection proves the original signed Weyl cancellation” | UNVERIFIED; OPEN; IGC-17 is a transport bound | Setting `q=0` leaves the selected mean itself. The same coherent-source controls remain necessary. |

**Verdict:** the relative-information construction survives, with a sharp
quantitative neutral-mass theorem and an explicit nonempty neutral fiber.
Coding and operational preparation provide compatible but distinct
realizations. The genuinely missing edge is still a source-specific estimate
on the signed selected carry observable that yields cancellation for the
original forcing and selected zero seed. Neither a more concentrated seed
law nor a richer positive source field supplies that estimate by itself.
