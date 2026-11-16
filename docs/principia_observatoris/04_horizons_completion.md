# Liber Quartus — De Limitibus et Defectibus

## Scope and contract

This book separates a finite bound on **where a distinguishing response exists**
from the cost and lawfulness of acquiring it. The response laws below are
mathematical objects. Their authenticity, exact accessibility, and applicability
to an external carrier are separate premises. No theorem below upgrades finite
sampling to a universal claim about an unrestricted source.

**Status.** The finite-state and linear results are classical mathematics,
reproved here with explicit observer interfaces. The completion statements are
elementary continuity results. The sharp examples and the assumption audit are
local derivations, without a claim of scholarly priority. No proof-assistant
certification is asserted for this book.

The founding [PR #618 note](../../research/2026-11-13/causal_relevance_proximity/RESEARCH_NOTE.md)
§9 asks what additional source promises defeat delayed falsification. The answer
developed here is an authenticated bound on **behavioral state complexity**,
together with lawful access to a separating response. Mere short descriptions,
finite data rank, and repeated agreement are insufficient substitutes.

## 1. Finite machines: a bound on distinguishing futures

A deterministic Moore carrier consists of a nonempty finite state set `S`, a
finite action alphabet `A`, total maps `T_a:S→S`, and a present readout `o:S→Y`.
For `w=a₁…aₖ`, write `T_w=T_aₖ∘…∘T_a₁`; the empty word has identity transition.
The readout after `w` is `o(T_w(s))`. Rejection, charged cost, or source labels
must be included in `o` or in an explicit enriched contract if they are targets.
They are not preserved merely because ordinary readouts match.

Let `N=|S|` and let `k` be the number of distinct present readouts. Two separate
machines can be compared by taking their disjoint union with the same action and
readout alphabets; then `N=n+m`.

**PO-H1 — finite Moore discrimination.** If any word distinguishes states `s,t`,
some word of length at most `N−k` distinguishes them. If `k=1`, no word
distinguishes any pair; otherwise `N−k≤N−2`. The bound in total `N` is sharp.

**Proof.** Let `E_j` identify states whose readouts agree after every word of
length at most `j`. Thus `E_0` has `k` classes, and

\[
sE_{j+1}t\iff sE_jt\ \text{and}\ T_a(s)E_jT_a(t)\quad\text{for every }a.
\]

Every strict refinement increases the number of classes by at least one. Once
`E_{j+1}=E_j`, its classes are transition invariant; induction on word length
then gives equality for all future words. There can be at most `N−k` strict
refinements, so `E_{N−k}` is stable. For sharpness take a unary chain of `N−1`
states, initially at its first state, with readout zero except at its final
absorbing state, which has readout one. Compare it with a separate absorbing
zero-readout state. The first distinction has length `N−2`, and `k=2`. ∎

This is finite behavioral-equivalence refinement, already used by
[SUCC's future-safe quotient implementation](../../observational_succ/future_safe_quotient.py).
The new book does not rename that algorithm as a new theorem. It supplies an
explicit horizon and its scope. For instrument outputs occurring *before* each
transition, an additional final readout action may be needed; an action count
must respect that convention.

**Execution boundary.** The theorem identifies an experiment separating a known
pair of initial states. It does not imply that one adaptive policy identifies
an arbitrary target on a single disturbed carrier. The three-state destructive
probe in [Carrier-relative targets §3](../CARRIER_RELATIVE_TARGETS.md) remains an
all-horizon counterexample to that stronger conclusion.

## 2. Linear and switched carriers: a rank-controlled horizon

Fix a field `F`, a finite alphabet `A`, a finite-dimensional state space `V`,
linear updates `L_a:V→V`, an allowed preparation/perturbation map `B:U→V`, and a
readout `C:V→W`. Define `L_w=L_aₖ…L_a₁`. The calibrated response is

\[
M(w)=CL_wB\in\operatorname{Hom}(U,W).
\]

This includes ordinary autonomous outputs (`dim U=1`), LTI Markov parameters
(`|A|=1`), and switched linear response laws. For an impulse applied in
`z_{t+1}=Lz_t+Bu_t`, the coefficient at output time `t=k+1` is `CL^kB`.
Hence word length `k` and elapsed impulse-response time `k+1` are distinct.

Put

\[
R_j=\operatorname{span}\{L_w\operatorname{im}B:|w|\le j\},\qquad
R=\bigcup_{j\ge0}R_j,\qquad b=\operatorname{rank}B,\quad r=\dim R.
\]

**PO-H2 — accessible-rank discrimination.** If `B=0`, every response is zero.
Otherwise the following statements are equivalent:

1. `M(w)=0` for every finite word `w`.
2. `C` vanishes on `R`.
3. `M(w)=0` for every word with `|w|≤r−b`.

In particular a nonzero response has a witness of length at most `r−b`.

**Proof.** By construction

\[
R_{j+1}=R_j+\sum_{a\in A}L_aR_j.
\]

If two consecutive spaces agree, the common space is invariant under every
`L_a`, contains `im B`, and therefore equals `R`. Before stabilization its
dimension grows strictly. Since `dim R_0=b`, stabilization occurs by index
`r−b`: if all preceding steps are strict, that index already has dimension
`r`. Consequently `R_{r−b}=R`. Vanishing on its displayed generators is
equivalent to vanishing on `R`; this is equivalent to all responses vanishing.
∎

**PO-H3 — comparison of two authenticated realizations.** Suppose two response
laws have state dimensions `n,m`, the same typed input/output spaces and action
alphabet, and are generated by their declared linear maps. If the responses
agree for every word of length at most `n+m−1`, they agree for every word.
If they disagree, a witness exists within that bound. It is enough to use the
sharper bound `r−b` for the joint reachable difference representation.

**Proof.** On `V₁⊕V₂` use

\[
L_a=\begin{pmatrix}L_{1,a}&0\\0&L_{2,a}\end{pmatrix},\quad
B=\binom{B_1}{B_2},\quad C=(C_1\; -C_2).
\]

Its response is precisely `M₁(w)−M₂(w)`. If `B≠0`, then `r−b≤n+m−1`; if
`B=0`, both laws are zero. Apply PO-H2. ∎

This is the standard weighted-automaton equivalence bound, not a new discovery
in automata theory. A primary research account states the span lemma and
short-witness result as Proposition 3.1 in
[Kiefer–Murawski–Ouaknine–Wachter–Worrell](https://www.cs.ox.ac.uk/james.worrell/fossacs12-journal.pdf).
The earlier algorithmic source is
[Tzeng, 1992](https://doi.org/10.1137/0221017).
The independent derivation here makes preparation rank, observational typing,
and source authentication explicit.

### Sharpness, including two nonzero-size models

Let `N=n+m≥2`, choose distinct rational numbers `λ₀,…,λ_{N−1}`, and set

\[
d_j=\frac1{\prod_{\ell\ne j}(\lambda_j-\lambda_\ell)}.
\]

Lagrange interpolation of `x^k` at the `N` nodes, followed by comparison of the
coefficient of `x^{N−1}`, gives

\[
\sum_jd_j\lambda_j^k=0\ (0\le k<N-1),\qquad
\sum_jd_j\lambda_j^{N-1}=1.
\]

Take the first `n` diagonal modes as the first model with output coefficients
`d_j`, and the remaining `m` modes as the second model with coefficients `−d_j`.
Both preparation vectors are all ones. Their first different coefficient is
exactly `k=N−1`. This proves sharpness even with both dimensions positive.
These are rational linear systems; signed output coefficients are permitted.
No positivity or probability interpretation is asserted for the example.

For `n=m=2`, use

\[
L_1=\operatorname{diag}(0,1),\ C_1=(-1/6,1/2),\qquad
L_2=\operatorname{diag}(2,3),\ C_2=(1/2,-1/6),\quad B_1=B_2=(1,1)^T.
\]

The two outputs are respectively `(1/3,1/2,1/2,1/2)` and
`(1/3,1/2,1/2,−1/2)` at `k=0,1,2,3`. A horizon shortened by one fails.

### A finite certificate, not an infinite experiment list

Given exact rational matrices, construct a basis of `R` by retaining linearly
independent columns among `B,L_aB,L_aL_bB,…`. At most `r` columns are retained.
A closure certificate can consist of a basis matrix `V_R`, matrices `K,J_a`,
and the exact identities

\[
B=V_RK,\qquad L_aV_R=V_RJ_a\ (a\in A),\qquad CV_R=0.
\]

These identities alone prove `CL_wB=0` by induction, even without trusting the
search that produced them. To obtain a nonzero witness, retain the word and
original input column for every retained basis vector. If `C` is nonzero on
`R`, some retained vector has nonzero readout. This is a proof from an
authenticated finite source law. It is not a claim that the observer physically
performed all possible words. Over arbitrary real coefficients, an exact
equality oracle is not silently available; the executable claim here is for
exact rational data or another specified effective field.

## 3. Recurrences, Hankel rank, and the missing promise

**PO-H4 — global recurrence discrimination.** A scalar sequence satisfying a
given monic homogeneous recurrence of order `d` is determined by its first `d`
values. Two sequences whose recurrence coefficients may differ but whose
globally valid orders are bounded by `d₁,d₂` agree everywhere if they agree at
indices `0,…,d₁+d₂−1`.

**Proof.** With known coefficients, apply the recurrence inductively. With
different coefficients, use companion-state realizations of dimensions
`d₁,d₂` and PO-H3, or apply the product of the two annihilating polynomials to
the difference and induct from its first `d₁+d₂` zero values. ∎

A global Hankel-rank promise supplies the same realization bound. For
`H_s=(s_{i+j})_{i,j≥0}`, suppose `rank H_s≤d`. Let `v_j=(s_{i+j})_{i≥0}` and
let `V` be their span. Coordinate shift maps `v_j` to `v_{j+1}` and respects
every linear relation, since shifting a zero sequence still gives zero.
Thus it defines `L:V→V`. Evaluation of coordinate zero gives `C`, and `B(1)=v_0`;
then `s_k=CL^kB` with `dim V≤d`. This is a direct proof of the needed direction
of classical finite realization theory, not an inference from observed rank.

**PO-H5 — finite Hankel rank cannot authenticate the global rank.** For every
finite Hankel block `H=(s_{i+j})_{0≤i≤p,0≤j≤q}`, the zero sequence and the
delayed spike `s^{(J)}_k=1[k=J]`, with `J>p+q`, give the same zero block.
The full Hankel matrix of the delayed spike has rank exactly `J+1`.

**Proof.** The sampled indices are less than `J`. In the leading
`(J+1)×(J+1)` block, the ones lie on the antidiagonal, so its determinant is
`±1`. All rows and columns after index `J` vanish. ∎

Consequently, finite low-rank observations do not certify a recurrence-order
bound. A source theorem, an authenticated realization, or an independently
justified global model-class restriction must pay that debt. There is also no
dimension-only lower bound on the amplitude of a nonzero witness: multiplying
`C` by any positive rational `ε` preserves its first distinguishing horizon
and makes the response arbitrarily small. Exact discrimination and robust
physical detection are different statements.

## 4. Witnesses, detection, and hidden horizons

For an initial intervention channel `x`, target `y`, and specified context,
define its **effect horizon** as the least clock time at which two admitted
interventions at `x` yield different mathematical target laws; use infinity if
none do. Define its **detection horizon** as the least budget at which an
admissible observer policy can distinguish the competing sources under its
declared correctness criterion. These clocks can have different units. A
comparison requires a supplied budget-to-time/resource map.

**PO-H6 — consequence before detection.** There are finite deterministic
carriers with finite effect horizon and infinite detection horizon for a
restricted toolkit. Take source state `(h,y)∈{0,1}²`, update `y←h`, and let the
only accessible instrument report zero and leave state unchanged. Two allowed
preparations `h=0,1` change `y` after one update, but every accessible transcript
is the same. Adding an authenticated readout of `y` makes the distinction
accessible. The consequence is source-defined; it is not secretly an already
observed consequence. ∎

For a finite restricted-horizon version, permit reading `y` only after clock
time `L>1`. Effect occurs at time one; first detection is `L`. This is access
latency, not an extra signal-propagation mechanism. No relativity claim follows.

**PO-H7 — small witnesses can require large search.** In the black-box class of
`N`-bit vectors, deciding the target “all bits are zero” requires `N` exact
coordinate queries in the worst case for a deterministic guaranteed-correct
algorithm. A false instance has a one-coordinate certificate.

**Proof.** Follow the all-zero transcript. If the algorithm stops after fewer
than `N` distinct queries, change an unqueried coordinate to one. All received
answers are unchanged but the target changes. A known nonzero coordinate is
verified by one query. ∎

The bound concerns this query model, not all encodings or algorithms. For
randomized algorithms, a new error criterion and lower-bound argument are
required; the deterministic bound is not automatically a randomized bound.

**PO-H8 — computability and short description do not bound hidden horizons.**
There is no computable function of source-program length bounding the first
nonzero index for every nonzero total computable Boolean sequence.

**Proof.** Given an arbitrary machine `T`, construct the total sequence
`s_T(n)=1` if `T` halts within its first `n` steps and zero otherwise. Its
program length is computable from the finite description of `T`. A proposed
computable bound `B` would decide whether `T` ever halts: evaluate `s_T` at
`B(length(s_T))`. If `T` ever halts, a first nonzero term must occur by that
bound; if it does not, every term is zero. This contradicts the halting
undecidability theorem. For completeness, a total halting decider would produce
a machine `G(p)` that loops when the decider says program `p` halts on input
`p`, and halts otherwise. Running `G` on its own program description contradicts
the decider in both cases. Inputs can be hard-coded when comparing machines
with no external input. ∎

This standard reduction does not make an individual sequence evaluation
uncomputable. A known finite-state/linear realization bound in PO-H1–H4 is a
stronger promise than “computable with a short source description.”

### Distribution distinction is not outcome certainty

Even a one-step mathematical distinction need not permit finite zero-error
identification from outcomes. Under independent Bernoulli draws with parameter
`1/3` or `2/3`, every finite binary transcript has positive probability under
both sources. Any terminal transcript assigned a certain source is therefore
possible under its rival. No policy that always terminates with a finite
transcript can be both always correct and identify the parameter exactly.
With an allowed error probability, ordinary statistical tests become available;
their sample budgets need a separate theorem. PO-H2–H3 compare exact laws,
not finite stochastic samples.

## 5. Finite failure and completion are different quantifier patterns

The founding note's pair is retained exactly:

\[
a(n)=1/(n+1),\qquad b_H(n)=
\begin{cases}1/(n+1)&n\le H,\\1&n>H.\end{cases}
\]

They agree at all indices through `H`; `a` is nonzero at every finite index
and tends to zero; `b_H` first violates the displayed finite law at `H+1` and
tends to one. For a deterministic adaptive readout protocol that terminates
on `a`, choose `H` beyond all its queried indices. Induction along that actual
transcript gives the same actions and answers on `b_H`. This proves a
no-guaranteed-finite-discriminator result for the unrestricted readout family.
It does not apply after the generating formula is authenticated and a sound
proof of its behavior becomes an allowed instrument.

**PO-H9 — source-faithful metric completion.** Let `X,Y` be metric spaces,
`x_n→x` in `X`, and `f:X→Y` be continuous at `x`. Then `f(x_n)→f(x)`. More
quantitatively, suppose

\[
d_X(x_n,x)\le\delta_n,\quad
d_Y(f(u),f(x))\le\omega(d_X(u,x)),\quad
d_Y(y_n,f(x_n))\le\eta_n,
\]

where `ω` is nondecreasing, `ω(t)→0` as `t↓0`, and `δ_n,η_n→0`. Then

\[
d_Y(y_n,f(x))\le\eta_n+\omega(\delta_n).
\]

**Proof.** The qualitative conclusion is the epsilon-delta definition of
continuity. The quantitative conclusion is the triangle inequality followed
by the two supplied bounds. ∎

Computable moduli for `δ_n`, `η_n`, and `ω` yield an effective stage for a
requested positive error. Bare convergence does not supply that algorithm.
In the Lipschitz case `ω(t)=Lt`, the bound is `η_n+Lδ_n`. The same named source,
observation, and limit must occur in all three premises. Substituting a fitted
model or a different source sequence is not justified by the inequality.

The hypotheses do not imply finite-stage equality: `x_n=1/(n+1)`, `f=id`,
`x=0` has a known effective modulus and no finite zero. Nor do arbitrarily
small error bars decide an exact zero test without an additional separation
promise. If a target is promised to lie in a discrete set with minimum
separation `γ>0`, an error radius below `γ/2` allows unique rounding whenever
the candidate set and chart are effective. The discreteness is doing real work.

### Two explicit failures of commuting observation and completion

**Discontinuous fixed observation.** Take `x_n=1/(n+1)→0` and
`f(x)=1[x>0]` on `[0,1]`. Then `lim f(x_n)=1`, whereas `f(lim x_n)=0`.
Continuity at the limiting source cannot simply be omitted.

**Moving continuous observation.** In `X={0,1}^N` with the product topology,
let `x^{(n)}` have a single one in coordinate `n`. Then `x^{(n)}→0`, and every
fixed coordinate readout is continuous and eventually zero. But the moving
readout `f_n(x)=x_n` satisfies `f_n(x^{(n)})=1` and `f_n(0)=0` for all `n`.
Pointwise continuity of each probe does not supply uniform control of a growing
instrument family. In the usual product metric, these probes have no common
modulus at zero. This is a concrete noncommuting diagonal limit, not evidence
that completion itself is inconsistent.

The earlier [compact target-completion theorem](../CARRIER_RELATIVE_TARGETS.md)
already proves convergence of extrema on nested compact surviving-model sets.
Its finite-stage Boolean consequence requires target continuity. This book
reuses that result; it does not count it as a new discovery. On a Scott domain,
the corresponding positive statement is equally typed: a Scott-continuous
map to the Sierpiński order `{⊥<true}` preserves directed suprema, so if the
limit is `true`, some approximant is `true` (a directed set of only `⊥` cannot
have supremum `true`). This is a finite **positive witness** rule; it is not
a rule certifying arbitrary negations from finite absence of a witness.

## 6. Dependency and verdict map

| Result | Indispensable added premises | What is obtained | Tempting overstatement defeated |
|---|---|---|---|
| PO-H1 | Complete finite deterministic source, common action/readout types | Bounded distinguishing word | Single-copy target identification follows automatically |
| PO-H2–H3 | Finite-dimensional linear law, authenticated maps, common typed responses | All-future response equality from a bounded bank | Sampled near-equality proves exact equality |
| PO-H4 | Globally valid recurrence/rank bound | Bounded sequence comparison | A finite low-rank Hankel block authenticates its own continuation |
| PO-H6–H8 | Explicit toolkit, clocks and cost model | Hidden-access examples and exact impossibility bounds | Consequence entails accessible detection; short code entails short horizon |
| PO-H9 | Same-source convergence and continuity/moduli | Limit transport and finite error certificate | A limit identity occurs at a final physical tick |

## 7. A quantitative repair: stable finite response banks

Exact coefficient equality is too strong for ordinary noisy access. A finite
bank can nevertheless certify a uniform approximate conclusion if stability
and conditioning are paid separately.

**PO-H10 — stable response-bank extension.** In PO-H2 take the field to be
`R` or `C`, and specify norms on `U,R,W`. Let `v₁,…,v_r` be a basis of the
reachable space `R`, with coordinate map `J:R→F^r` defined by
`v=Σ_i(Jv)_i v_i`. Suppose certified constants `κ,K,β,ε≥0` satisfy

\[
\|Jv\|_1\le\kappa\|v\|_R,
\qquad \|L_w|_R\|_{R\to R}\le K\quad(\text{every finite }w),
\qquad \|B\|_{U\to R}\le\beta,
\qquad \|Cv_i\|_W\le\epsilon\quad(1\le i\le r).
\]

Then every finite response satisfies

\[
\boxed{\|CL_wB\|_{U\to W}\le\epsilon\kappa K\beta.}
\]

**Proof.** For `v∈R`, linearity, the triangle inequality and the coordinate
bound give

\[
\|Cv\|_W
 =\left\|\sum_i(Jv)_iCv_i\right\|_W
 \le\epsilon\|Jv\|_1
 \le\epsilon\kappa\|v\|_R.
\]

Apply this to `v=L_wBu` and then use the other two bounds; take the supremum
over `||u||_U≤1`. ∎

For the difference representation in PO-H3, this is a uniform bound on model
discrepancy. The basis must be certified to span the reachable space; selecting
well-fitting observed vectors does not certify closure. If the bank readouts
are only known to error `η_i`, replace `ε` by a valid upper bound on
`max_i(||measured_i||_W+η_i)`. Rational coefficient intervals or calibrated
measurement errors can enter here; a numerical rank threshold cannot replace
the exact source/closure premise.

One sufficient way to prove `K=1` is to exhibit a norm on `R` for which every
`L_a|_R` is contractive. A uniform semigroup bound can hold more generally.
With an authenticated bound only through horizon `T`, the conclusion holds
only through `T`. The weak kernel does not establish any of these bounds.

**Why the factors matter.** Without stability, the one-dimensional system
`L=2, B=1, C=δ` has a one-vector bank of size `δ`, but response `δ2^k`.
Without coordinate conditioning, the perfectly stable scalar system
`L=B=C=1` and basis `v₁=δ` has bank response `δ` while its true response is
one; its coordinate constant is exactly `κ=1/δ`. These exact models exclude
dropping either factor. The chosen basis in the second example is a reachable
vector under preparation input `δ`, but it is badly normalized as a bank for
unit inputs.

The [minimal predictive completion in Book II](02_causality_geometry.md),
CG-04, constructs the dual observable subspace. PO-H2 constructs the reachable
subspace, and PO-H10 controls response propagation on it. Neither construction
grants physical preparation or measurement access.

The **next theorem that would change practical applicability** must combine
these algebraic certificates with a realizable preparation policy and certified
input/measurement costs. Exact target identification additionally needs a
lower separation promise for nonzero responses. An arbitrarily small signed
witness or destructive access can otherwise make a finite mathematical
horizon operationally useless. For BBP, no authenticated finite-dimensional
realization of the required asymptotic signed statistics has been established
here; these finite-closure theorems therefore do not settle normality.
