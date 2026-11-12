# Typed channels, amplitudes, and implementation cost

**Date:** 2026-11-12. **Verdict:** a basis can name distinguishable channels;
typed arrows specify their couplings; a separate path grade can record a
declared resource cost. These three roles can be combined without identifying
their different kinds of numbers. This note supplies an exact finite model,
not a theorem that channel count or coefficient size measures general
computational hardness.

## 1. A basis does not imply independent dynamics

Let `I` be a finite set of channel labels. For each `i` choose a finite-dimensional
real or complex vector space `V_i`, and put

\[
V=\bigoplus_{i\in I}V_i,\qquad x=(x_i)_{i\in I}.
\]

A basis in each summand gives coordinates for its state. Linear independence
means those coordinates are unique. It does not say that the time evolution
of one coordinate is independent of the others.

For example, the two standard basis vectors in `R^2` are linearly independent,
but the matrix `[[0,1],[1,0]]` exchanges them. More generally, for a linear
update `A`, the chosen channels evolve independently exactly when its
off-diagonal blocks `A_ij:V_j->V_i` vanish for `i != j`. Indeed,
`(Ax)_i=sum_j A_ij x_j`, so independence from every other input component
is equivalent to the vanishing of those blocks. For continuous-time linear
evolution the analogous condition is block diagonality of its generator,
relative to the chosen decomposition. **TYP-01 — PROVED LOCAL.**

Nor is the number of chosen basis vectors automatically a count of irreducible
dynamic channels: a different decomposition can reveal invariant subspaces,
and even those need not be one-dimensional. The decomposition is part of the
model to be tested.

## 2. Types constrain couplings but do not generate them

Give each channel a unit type `u_i`. In a coordinate convention where `x_i`
has units `u_i`, the discrete update coefficient `A_ij` has units

\[
[A_{ij}]=u_i/u_j.
\]

The summands `A_ij x_j` then have the same units and can be added in channel
`i`. A continuous-time generator `G`, defined by `dx/dt=Gx`, instead needs
`[G_ij]=u_i/(u_j * time)`.

For position `x` and velocity `v`, the types are length and length/time.
A discrete coefficient mapping velocity to position therefore has units
time. A generator coefficient in `dx/dt=v` is dimensionless. This difference
prevents a hidden time factor from entering the definition of the arrows.

Equivalently, one can attach the unit to a basis vector and make its scalar
coordinate dimensionless. Either convention is valid; attaching the same
unit independently to both factors would double-count it. A precise version
uses a one-dimensional space of quantities of type `u_i` tensored with the
numerical coordinate space. **TYP-02 — exact typing convention.**

Composing a typed arrow `j->i` with `i->k` multiplies its unit ratios:
`(u_k/u_i)(u_i/u_j)=u_k/u_j`. Thus paths with the same endpoints can be
compared dimensionally. This permits a coupling. It does not assert that
the coupling exists, has a nonzero coefficient, or has a particular physical
mechanism. Those are additional declarations or measurements.

The categorical version likewise retains the actual morphisms and their
composition. A unit label alone cannot provide all the relationships used
by the representable functor `Hom(-,X)`. Any use of Yoneda reconstruction
must preserve those morphisms and their naturality, not only the string
used to name a type.

## 3. Values and resource annotations use different algebra

A coefficient `x_i` can be a signed or complex amplitude. A computation
annotation might instead be a vector in `N^s`, counting additions,
multiplications, memory accesses, or another declared resource. Such
nonnegative integer annotations are not automatically a vector space:
they generally lack additive inverses and division by scalars.

For example, two histories with amplitudes `+1` and `-1` may cancel when
observed coherently. Their resource expenditure does not become zero
because of that cancellation. Similarly, scaling a numerical state by two
does not prove that twice as much computation was required to produce it.

Keep a numerical state `x`, typed maps `A_e`, and resource grades `c_e` as
separate data. A declared rule may relate them, but that rule needs its own
proof or calibration. In particular, a unit type times a scalar supplies a
quantity; it does not supply a complete interconnection graph or a general
complexity measure. **TYP-03 — exact distinction and countercontrol.**

## 4. A finite description can organize all cost-graded paths

Choose a finite directed graph with possibly parallel arrows. For each
arrow `e:j->i`, specify a linear map `A_e:V_j->V_i` and an integer cost
`c_e>=1`. The cost is measured in declared abstract resource units; it is
not inferred from the amplitude or the unit type. Introduce a formal variable
`z` and the block matrix

\[
W(z)_{ij}=\sum_{e:j\to i}A_e z^{c_e}.
\]

Our matrix convention puts the target in the row and source in the column.
For a path `p=(e_1,...,e_k)` in traversal order, define

\[
A_p=A_{e_k}\cdots A_{e_1},\qquad
c(p)=c_{e_1}+\cdots+c_{e_k}.
\]

**TYP-04 — CLASSICAL transfer-matrix construction, with an explicit graded
derivation.** The formal inverse exists and has expansion

\[
\boxed{F(z)=(I-W(z))^{-1}=\sum_{k\ge0}W(z)^k.}
\]

Its coefficient is

\[
\boxed{[z^N]F(z)_{ij}=
\sum_{\substack{p:j\to i\\c(p)=N}}A_p.}
\]

The empty path supplies the identity when `N=0` and `i=j`. To prove the
formula, expand a product of block matrices: each compatible chain of
indices selects a path, and the operator product has precisely its traversal
order. Powers of `z` add the costs. Since every edge costs at least one,
a path of total cost `N` has at most `N` edges. A finite graph has only
finitely many such paths. Each coefficient is therefore a finite sum.
The geometric-series cancellation now proves both
`(I-W)F=I` and `F(I-W)=I` coefficient by coefficient.

The ungraded scalar-weight version is Stanley's *Enumerative Combinatorics*,
volume 1, second edition, §4.7, Theorems 4.7.1–4.7.2; see the
[author's text](https://math.mit.edu/~rstan/ec/ec1.pdf). The typed block and
positive-cost formulation here has the direct proof above. No academic
novelty is claimed.

This is a **formal power-series identity**. It does not require numerical
convergence at a chosen complex value of `z`, and it does not establish such
convergence. An analytic evaluation needs a separate domain and convergence
argument. With complex amplitudes it computes a coherent sum, not a physical
probability or the number of histories. Counting histories is a different
choice of coefficients.

Several resource counters can replace `c_e` by a vector and `z^{c_e}` by a
monomial. A positive integer valuation of each edge grade supplies the same
local-finiteness argument. Without such a condition, a fixed resource grade
can contain infinitely many histories.

### Two calibrated failure controls

**Parallel cancellation.** Put two parallel edges with identical source,
target, and cost, having amplitudes `+1` and `-1`. Their contribution to
`W` cancels. The coherent path amplitude is zero, although there are two
histories and their separate squared amplitudes sum to two. This is ordinary
linear cancellation under the declared common observation.

**Zero-cost cycle.** A single zero-cost self-loop of amplitude one has
infinitely many histories of cost zero. The proposed geometric sum would
have constant coefficient `1+1+1+...`, which is not a coefficient in the
ordinary formal power-series ring. The model rejects that input. Positive
edge costs are sufficient, not necessary: a zero-cost subgraph with suitable
nilpotence can sometimes be treated separately. No claim that every
zero-cost edge is inherently invalid is made. **TYP-05 — PROVED LOCAL
countercontrols.**

## 5. Implementation cost need not survive arithmetic identification

In the arithmetic carrier, write `S(n)=n+1` and `V_2(n)=2n`, and read
operator products right to left. The source identity

\[
\boxed{S V_2 S=S^3 V_2}
\]

holds because both sides send every `n` to `2n+3`. The left word uses
three primitive operations; the right word uses four. They are different
histories representing the same affine map. At the unit both end at five.

**TYP-06 — PROVED LOCAL.** Primitive history length does not descend to an
additive cost on the quotient that identifies equal affine maps. More
generally, if `S` is assigned positive additive cost `s` and `V_2` cost `v`,
the equivalent words would force `2s+v=3s+v`, hence `s=0`, contradicting
positivity. The resource must therefore stay attached to the implementation
history, or a different quotient-compatible notion must be supplied.

A minimum implementation cost is possible after fixing generators and their
prices. It satisfies

\[
C(g\circ f)\le C(g)+C(f)
\]

because concatenation supplies one implementation, but the inequality can
be strict. For generators `S,V_2`, with unit prices,

\[
C(V_2)=1,\quad C(S^3)=3,\quad C(S^3V_2)=3<4.
\]

The last minimum is attained by `SV_2S`; no word of length at most two has
affine coefficients `(2,3)`. Thus recording the least available cost is not
the same thing as assigning an additive functorial grade to every semantic
arrow. It also depends on the allowed instruction set.

## 6. Compatible roots are an additional naturality condition

View the channel representation as a functor from the graph's free path
category to vector spaces over its scalar field `K`. Choose a nonzero vector
`r_i` in each channel. The equations

\[
\boxed{A_e r_j=r_i\quad\text{for every edge }e:j\to i}
\]

say exactly that the maps `eta_i:K->V_i`, given by `eta_i(lambda)=lambda r_i`,
form a natural transformation from the constant functor `const(K)` to the
channel representation. The constant functor sends every arrow to the identity
of `K`. Naturality is therefore the displayed equation. Applying it successively
along a path proves `A_p r_j=r_i`; in particular, every closed path at `i`
fixes its local root `r_i`. **TYP-07 — PROVED LOCAL.** Compatible unit types
alone do not imply these equations.

For one-dimensional channels with invertible unit-modulus edge transports on
a connected underlying graph, a nonzero compatible family exists exactly
when every closed walk has holonomy one. A traversal against a declared
edge uses its inverse transport; this convention matters when the original
directed graph is not strongly connected. Necessity follows by transporting
a nonzero root around a closed walk. For sufficiency, choose a nonzero root
at one vertex and transport it to every other vertex along any connecting
path. Two choices give the same result because following one path and the
reverse of the other has holonomy one. The resulting roots satisfy every
edge equation. It suffices to check a cycle basis after choosing a spanning
tree. This is the same classical flat-transport condition used in
[TRIADIC_TRANSPORT.md](TRIADIC_TRANSPORT.md), with the path-independence proof
given explicitly here.

Two exact scalar controls expose the condition. With transports `+1` in
both directions between channels A and B, roots `r_A=r_B=1` are compatible.
Changing only the return transport to `-1` requires both `r_B=r_A` and
`r_A=-r_B`, so only the zero family remains. The two-equation coefficient
matrix has determinant `uv-1` for edge transports `u,v`; the twisted case
has determinant `-2`. All unit transports equal to one admit the positive
family of local scalar roots one. The earlier toy's negative self-loop
prevents such a nonzero compatible family, as intended.

These are **local roots related by arrows**, not a claim that every arrow
operator, embedded into the full direct sum, fixes the same global vector.
Even their aggregate needs a separate normalization. If

\[
B_{ij}=\sum_{e:j\to i}\lambda_e A_e,
\]

then the direct-sum vector `r=(r_i)` obeys
`(Br)_i=(sum_{e:target(e)=i} lambda_e) r_i`. Thus `Br=r` requires each
incoming weight sum to equal one. For example, a two-channel matrix of all
ones carries `(1,1)` to `(2,2)` even though every constituent scalar edge
preserves its local root. Dividing this aggregate by two fixes `(1,1)`.

The formal resource variable is also separate: the matrix `W(z)` above has
zero constant coefficient because costs are positive. It consequently cannot
satisfy `W(z)r=r` as a formal identity for a nonzero constant vector `r`.
Root compatibility concerns the edge maps `A_e`; the cost tags record an
additional observation and do not silently change that naturality condition.

## 7. Finite executable model and status

`typed_channels_probe.py` implements a two-channel scalar-fiber graph, exact
rational amplitudes, integer costs, and unit exponents for length and time.
It compares literal path enumeration with formal coefficient recurrence,
checks both inverse identities, and retains the controls above. The toy has
position and velocity types, reciprocal cross-channel unit ratios, and
two cancelling parallel loops. A cost-three return to the position channel
has amplitude two: one direct loop and one two-edge loop each contribute
one. The model is a declared algebraic example, not a physical measurement.
Separate scalar-root controls test flat and twisted two-channel transport,
the incompatible negative self-loop, and normalized versus unnormalized
aggregation.

Actual finite execution results are recorded in
`receipts/TYPED_CHANNEL_REPORT.json`. They validate this implementation and
its controls; the proofs above establish the quantified statements.

| Claim | Earned scope | Remaining boundary |
| --- | --- | --- |
| TYP-01 | PROVED LOCAL criterion for independent linear channel evolution | A basis alone does not establish this criterion. |
| TYP-02 | Exact dimensional typing convention | Compatible units do not force a nonzero coupling. |
| TYP-03 | Amplitudes and resource annotations are distinct data | A quantitative bridge needs a declared, validated model. |
| TYP-04 | CLASSICAL formal path-resolvent construction with finite coefficients | No numerical convergence, probability interpretation, or speedup follows automatically. |
| TYP-05 | PROVED LOCAL interference and zero-cost-cycle controls | Other admissible zero-cost models require separate hypotheses. |
| TYP-06 | PROVED LOCAL failure of additive history cost on the affine quotient | Minimum implementation cost is generator-dependent and subadditive. |
| TYP-07 | PROVED LOCAL compatible-root naturality and flat scalar transport criterion | Types do not guarantee roots; a direct-sum aggregate needs additional normalization. |

The next useful bridge is to choose which path histories, typed maps, and
resource observations the prime-carrier observer actually uses. A claim
about proof or computation difficulty then requires a quantified task and
resource bound beyond the existence of these channels.
