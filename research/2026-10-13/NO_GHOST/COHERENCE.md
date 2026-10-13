# NO-GHOST: labelled diamonds, continuations, and chosen-map coherence

**Status.** The results below are paper proofs over finite declared models.
The private-token experiment is independently replayed using exact rational
arithmetic in `observational_succ/no_ghost_coherence.py` and
`tests/test_no_ghost_coherence.py`. That finite test is not a Lean proof of the
general theorems. No experimental history is asserted physically performed.

**Provenance and novelty boundary.** SUCC already proves the fixed-carrier,
fixed-instrument all-prior labelled-kernel diamond and distributional schedule
theorem in `research/2026-10-13/SWARM_ATLAS/C22.md`; its exact negative control
already shows that forgetting outcomes is unsound. PR #53's
`CARRIER_INDEXED_HISTORY_THEORY.md` proves all-prior carrier descent and
all-history naturality. Those are premises and baselines, not discoveries
claimed here. This note adds an explicit history-dependent continuation gate,
a full chosen-map coherence theorem for finite-poset schedules, a lawful
stochastic branch realization of noncoherent selected comparisons, and its
precise token-identity boundary. The general algebra is classical finite
kernel algebra and symmetric-group coherence; academic priority is not claimed.

## 1. Three objects that must remain separate

Fix finite original labels `Sigma`, finite current states, and a declared
instrument contract. The original is immutable; action selection uses public
history only. A positive atom is a *lawful possible history*, not a declaration
that it happened. Actual event logs need independent provenance.

For a public history `h`, the complete event kernel is

\[
K_{h,a}(\sigma,c;z,c')\geq0.
\]

Its row sums are one on enabled states. Enabledness and resources are separate
predicates: a disabled action is not an enabled action with an impossible
receipt. Under SUCC's robust access convention an action is legal only when
enabled on every currently supported alternative. No hidden source-dependent
choice is made available by writing a source-indexed kernel.

The following data have different strengths:

1. The law of the current endpoint.
2. The joint law of the **event-labelled** receipts and endpoint, indexed by
   the original source and retaining unnormalized event likelihood.
3. A branch refinement: finite complete private paths with their weights,
   occurrence IDs, intermediate states, source/basis/epoch metadata and receipts.
4. A specified bijection of such paths, with an explicit list of preserved
   predicates and token identities.
5. A coherent family of those bijections, independent of the exchange path.

Summing private paths defines (3) -> (2); it does not generally invert.
One weight-one private atom and two weight-one-half atoms have the same public
law but admit no weight-preserving atom bijection. A probability-law equality
therefore does not even imply existence of the strong private-path comparison.

## 2. Typed all-prior diamond theorem

Let `D` be the declared set of legal initial original/current pairs. Assume
both orders `a;b` and `b;a` are robustly legal on `D`: the first action is
enabled, and every positive branch of it permits the second action. Endpoints
are identified with one specified carrier `C'`, or transported into it by
specified **bijections** preserving the required source and metadata. If
only endpoint quotients are supplied, all following conclusions hold only
after that quotient, not for complete carrier histories.

For event receipts `z,w`, define

\[
L_{ab}^{z,w}(\sigma,c;d)=\sum_m
 K_{h,a}(\sigma,c;z,m)K_{h(a,z),b}(\sigma,m;w,d),
\]
\[
L_{ba}^{w,z}(\sigma,c;d)=\sum_m
 K_{h,b}(\sigma,c;w,m)K_{h(b,w),a}(\sigma,m;z,d).
\]

**NG-DIAMOND (PROVED, finite algebra).** The following are equivalent:

* For every nonnegative initial original/current law `J` supported on `D`,
  the two orders have identical unnormalized joint laws of immutable original,
  event-labelled receipts `(a:z,b:w)`, and final current state `d`.
* For every `(sigma,c)` in `D`, all `z,w,d` satisfy
  `L_ab^{z,w}(sigma,c;d)=L_ba^{w,z}(sigma,c;d)`.

**Proof.** The atom after `ab` is
`sum_c J(sigma,c)L_ab^{z,w}(sigma,c;d)`. Row equality gives the result by
linearity. Conversely choose the normalized Dirac preparation concentrated at
any `(sigma,c)` in `D`; equality of every `z,w,d` atom gives the row equality.
Normalized original posteriors agree only on common positive-mass receipts.
The conclusion makes no inference from a zero-evidence branch. QED.

Only source/current pairs in the declared test domain are necessary. A claim
for one fixed prior cannot be upgraded to the all-Dirac theorem; averaging can
hide source-indexed discrepancies. If enabledness is included in the semantic
equivalence rather than assumed, equality of the two robust legal domains is
an additional necessary condition. Kernel equations alone do not establish it.

This theorem preserves all predicates of the retained original, receipts and
endpoint, not arbitrary predicates of forgotten private branch paths. It does
not by itself preserve future action access or proof-support queries depending
on discarded order or private data.

### Exact hostile examples

**Endpoint and summed-channel failure (already in C22).** Let the current
state be one bit. Action `a` reads it nondestructively; `b` flips it and reports
`ok`. Both orders end at the same flipped bit and have equal summed channels.
At initial bit zero, `ab` records `a:0`; `ba` records `a:1`. If original equals
initial bit, averaging over a fair original also makes the unindexed `a`
marginal fair in both orders, while source/report correlation differs.

**Even separate report marginals fail.** From a single prepared state, the
first instrument draws a fair bit and stores it; the second resets the
endpoint to a common terminal state. In order `ab`, `a` reports the drawn bit
and `b` reports the same stored bit. In order `ba`, `b` reports the drawn bit
and `a` reports its complement. These are legitimate history-indexed kernels
with both orders enabled. Both report marginals are fair, and endpoints are
equal, but the event-labelled pairs are respectively `{00,11}` and `{01,10}`,
each with probability one half. Intermediate memory and order are explicitly
present in the carrier/history; there is no hidden reset operation.

**Interior replacement failure.** Actions `a,b` each report `ok` and leave the
current endpoint unchanged. A later enabled action `c` reports whether the
public history contains `a` before `b`. Every two-event labelled row for `ab`
and `ba` agrees; their three-event laws differ. A history-indexed contract is
allowed to read that public order. Thus a two-event equality cannot be composed
with arbitrary history-sensitive suffix kernels.

## 3. A sufficient continuation contract and weak schedule independence

Let `P` be a finite poset of **distinct event occurrences**, with a fixed
event/instrument contract. An ideal `I` is a set of completed occurrences
closed under predecessors. A reachable summary is

\[
q=(\sigma,I,r_I,c),
\]

where `r_I` assigns the retained receipt to each completed occurrence.
Basis, current epoch, resource state and any necessary branch memory are
included in `c` or explicitly in the summary. The observer does not read
`sigma`; it is a semantic index of the law.

Assume:

* Every prefix's enabledness and complete future kernels factor through
  `(I,r_I,c)` and the immutable original index, rather than the chronological
  order chosen to reach that summary. Alternatively provide explicit
  continuation intertwiners with the same effect.
* Each next event in any proposed linear extension is robustly available on
  every positive current alternative. In particular adjacent incomparable
  events remain mutually enabled after every positive branch of the other.
* At every reachable summary, each pair of currently minimal unperformed
  incomparable events has the exact NG-DIAMOND row identity, with occurrence
  labels retained.

**NG-WEAK-SCHEDULE (PROVED, classical concurrency specialization).** Every
linear extension of `P` has the same original-indexed joint law of the entire
occurrence-labelled receipt assignment and final carrier. All event likelihoods
and positive-evidence original posteriors agree.

**Proof.** Compare two extensions differing by an adjacent incomparable pair.
Their common prefix yields the same current law. NG-DIAMOND identifies the
joint law immediately after the pair. The continuation hypothesis makes the
remaining suffix a common kernel on the common summary, so multiplying it
preserves equality. Any two finite-poset linear extensions are connected by
adjacent swaps of incomparable events: move the desired first event left;
anything crossed is incomparable because both total orders extend the poset;
then induct on the remaining events. Transport equality along that chain. QED.

The reachable-summary qualification permits a smaller verification domain
than the whole Cartesian product. It is still necessary to verify all reached
states, not a few fitted preparations. This theorem reconstructs and extends
C22's fixed-instrument result; it is not a new trace theorem.

**Adaptive boundary.** Outcome-dependent presence or choice of an occurrence
can change the event configuration. Such dependencies must enter the poset,
event structure or public-policy contract. The theorem compares schedules of
one fixed configuration; it does not claim schedule invariance for arbitrary
adaptive policies, nor supply a nonhidden policy realizing an arbitrary
distribution over supported histories.

## 4. Strong schedule coherence with exact hypotheses

For each linear extension `lambda` of `P`, let `H_lambda` be a finite private
history space, including source labels and exact weights. For every adjacent
incomparable swap `e:lambda->mu`, suppose a specified bijection
`T_e:H_lambda->H_mu` preserves all declared invariants. These can include
source, public receipts, endpoints, weights, branch identity, resource use,
and future-proof support; the theorem preserves exactly the stated list.

Impose three *typed* relations:

* **Backtrack:** `T_(reverse e) T_e = id`.
* **Disjoint square:** exchanging two disjoint adjacent pairs in either order
  gives equal maps, whenever all four schedules are legal.
* **Triple hexagon:** for three adjacent pairwise incomparable occurrences,
  the two length-three exchange routes reversing them give equal maps:
  `T_12 T_23 T_12 = T_23 T_12 T_23`, with every map interpreted in its actual
  intermediate schedule, not as an untyped endomorphism.

**NG-STRONG-SCHEDULE (PROVED, finite rewriting).** These conditions are
necessary and sufficient for the composite `H_lambda -> H_mu` to be
independent of the exchange path. Consequently they produce a unique coherent
family extending the selected adjacent comparisons.

**Proof of sufficiency without an unproved topological premise.** Fix a target
linear extension `tau`. Orient each legal swap to decrease the number of
inversions relative to `tau`. A schedule different from `tau` has an adjacent
inversion; its pair is incomparable, since a comparable pair has the same
order in every linear extension. Thus every nonnormal schedule has a reduction,
and inversion count proves termination at the unique normal form `tau`.

Consider two first reductions. If they act on disjoint adjacent pairs, they
complete to a two-step diamond; the square hypothesis identifies its maps.
If they overlap, the three entries are in decreasing `tau` order. Every pair
among the three is incomparable: either direction of a comparable pair would
contradict one of the two linear extensions. Both three-step routes sorting
this block are therefore legal reductions and the hexagon identifies them.
These are all possibilities for two adjacent swaps.

Induct on inversion count to prove that every reduction from any `lambda` to
`tau` induces the same map `N_lambda`. After the common peak completion, all
remaining schedules have strictly smaller inversion count, so induction makes
their tails equal. For an oriented edge `e:lambda->mu`, this gives
`N_lambda=N_mu T_e`; backtracking gives the corresponding equation for reverse
edges. Hence any path from `lambda` to `mu` has map
`N_mu^{-1} N_lambda`, independent of the path. Necessity follows by comparing
the two paths in each backtrack, square and hexagon. QED.

The proof establishes the needed two-dimensional presentation, rather than
assuming an entire permutohedral subcomplex is simply connected. No extra
higher-dimensional equations are needed for strict set-bijection valued
transport after these relations hold. A weak higher-category target would
require its own higher coherence analysis; this theorem does not cover it.

## 5. A genuinely lawful stochastic model with noncoherent chosen maps

Use original labels `Sigma={0,1}`. The prepared carrier is
`(payload=sigma, completed=empty)`. There are three distinct one-use event
occurrences `a,b,c`, with no causal dependencies. Action `e` is enabled exactly
when `e` is not completed, a condition known from public occurrence history.
Its branch-refined kernel is

\[
(u,I)\xrightarrow[e,\;z=\mathrm{ok},\;t]{\;1/2\;}(u,I\cup\{e\}),
\qquad t\in\{0,1\}.
\]

Here `t` is an actual stochastic branch variable in the **declared model**,
fresh and independent at each enabled action. The public receipt is `ok`.
The branch variable remains in the complete private history, but not the
current endpoint; no later instrument reads it. Source, payload, basis and
occurrence identity remain fixed, and epoch is the completed-event count.
All six schedules are legal from each source and have eight paths of weight
`1/8`. The ordinary public/source/endpoint diamonds hold exactly.

The complete private history consists of the original and ordered sequence
of `(occurrence,bit,receipt,before-state,after-state,weight)` steps. When two
adjacent occurrences are exchanged, update their two private bit values by

\[
R(x,y)=(x,y\oplus x)
\]

in **positional coordinates**, then replay the path in the swapped schedule.
The pair's intermediate completed-set state changes lawfully; endpoints and
all other event tokens are unchanged. Every output is a positive path of the
same contract. The map is involutive, bijective, exact-weight preserving,
source preserving, receipt preserving, endpoint preserving and pair-local.
Disjoint swaps commute. It does not preserve the individual event's private
bit value; it is a selected relabelling of two branch coordinates.

Starting with schedule `abc` and private bits `010`, both exchange routes end
at schedule `cba`, but

\[
T_{12}T_{23}T_{12}(010)=011,
\qquad
T_{23}T_{12}T_{23}(010)=010.
\]

The exact certificate checker first checks lawfulness, all pair maps and their
inverses on every schedule/source/branch, then independently replays both raw
tuple routes. The seven tests include source-ID, output, path and comparison
table mutations; they also check the stronger token-preservation condition
and reject this map when that condition is requested.

**Exact verdict.** Valid chosen isomorphisms of fully retained private path
spaces, even pair-local ones preserving weights and all public/source/endpoint
data, need not be coherent. This is a real stochastic-history realization of
the algebraic obstruction, not evidence that the instruments fail to commute.
Neither route causes another physical experiment to be performed. It compares
two mathematical representations of possible branches, not factual logs of
the same run with arbitrary bits rewritten.

### The load-bearing token boundary and a lawful repair

If the required comparison must preserve the **value attached to each private
branch occurrence**, the CNOT family is disallowed. The canonical map is the
ordinary coordinate swap `(x,y)->(y,x)`, retaining `(event,bit)` pairs. It is
pair-local, preserves all complete records apart from their schedule, and
satisfies backtracking, squares and hexagons. Thus this example refutes
automatic coherence of an arbitrary selected family; it does **not** refute
existence of some coherent family. The repair adds no sensor and no memory to
the experiment; it selects the comparison determined by retained identities.

**NG-RIGIDITY (PROVED).** Suppose each `H_lambda` has an injective invariant map
`q_lambda:H_lambda->X`, all with the same image, and every permitted comparison
must preserve `q`. Then every comparison is uniquely
`q_mu^{-1} q_lambda`, so all coherence relations hold automatically.

**Proof.** Preservation determines the only possible image by injectivity;
common image provides existence. Composites telescope. QED.

In the token model choose `X` as `(original, occurrence-labelled token vector)`.
The maps are bijections and do not identify physically different branch
records. In a source-deterministic model a unique private path per original
can supply the same rigidity, provided each compared schedule is legal and
preserves the required reports. One cannot obtain this premise for free by
silently putting an undeclared omniscient random seed in the original source.

If arbitrary invariant-preserving bijections are allowed, existence of a
coherent family is often trivial once every fiber is isomorphic: choose one
base fiber and a bijection from each fiber to it, then telescope. Such choices
can violate locality, naturality or retained token identities. Therefore an
intrinsic obstruction to **existence** of coherent lawful comparisons needs
additional restrictions on the allowed comparison groupoids. Failure of one
family's braid equation is not that stronger no-go theorem.

## 6. Integration and next discriminator

* **C22:** retain its exact complete receipt kernel test. Add the continuation
  summary/intertwiner gate for history-dependent instruments; do not rebrand
  its theorem as new.
* **Carrier adapter:** branch-refined paths sit over `ActualHistory` by summing
  private atoms. This experiment is a separate exact calibration, not a
  replacement carrier. Existing actual receipts remain ordered factual logs.
* **F48:** prefix restriction and fixed-run incidence gluing remain intact.
  Add exchange arrows only with their declared preserved invariant and
  verified square/hexagon relations; quotienting them without this check can
  erase genuine private-path distinctions.
* **Nonabelian holonomy:** compose actual typed bijections around loops and
  compare maps on fibers. Neither parity nor one scalar loop score suffices.
* **Proof support:** original-target claims transport because the original is
  fixed. Fixed branch-value claims require token-preserving maps; arbitrary
  branch predicates otherwise need explicit pullback along the bijection.
* **Operational probability:** law equality and support do not solve whether
  a policy can realize a proposed distribution. The policy/kernel feasibility
  theorem belongs to a separate layer.

The next verdict-changing problem is a model whose *permitted* pair
comparisons cannot be replaced by any coherent, local, source/branch-preserving
family, while every required pair comparison exists. The present example has
a coherent alternative and deliberately makes no such existence claim.
