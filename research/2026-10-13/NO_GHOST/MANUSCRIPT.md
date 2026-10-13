# Source-indexed causal descent without ghost histories

## Exact finite gluing, chosen-transport coherence, and operational probability

**Operation NO-GHOST, 13 October 2026.** Research contribution to Observational
SUCC, based on carrier PR #53 at `9e7589e522aff990189aa8a14f6ee2fa5a28dd81`.
The immutable intake record is [SNAPSHOT.json](SNAPSHOT.json). Claims use the
branch-local `NG` namespace. No result here authenticates a physical source.

### Abstract

We separate three questions: whether observations have a common lawful source
history, whether different schedules have the same complete observable law,
and whether selected private-history comparisons are path independent. In a
finite source-indexed instrument model, complete labelled two-event kernel
equality characterizes all-prior distributional interchange. Under continuation
compatibility it implies schedule invariance. Private-history interchange
requires more: an explicit three-instrument example has lawful,
source-preserving, weight-preserving pair comparisons but nontrivial braid
holonomy, while a different comparison family is coherent. We give sufficient
and necessary coherence relations for the full finite-poset schedule graph.

For gluing, we extend the existing F48 constraint-incidence construction by
descent through coherent schedule presentations, explicitly requiring
restriction naturality. Probability introduces a further obstruction: a
distribution supported on lawful paths may violate prescribed instrument
probabilities or require a hidden-source oracle. We characterize finite
public-policy-realizable laws by an exact rational realization-plan polytope,
and distinguish it from the larger support-only marginal polytope. Finite
repair menus admit certifiable minimum cost, but generally no least repair.

These are scoped mathematical theorems, countermodels, and implementations.
The ingredients have substantial classical prior art. No academic priority
claim is made; a universal causal sheaf or universal physical repair is not
established. Formal and computational scopes are separately recorded below.

## 1. Frontier, provenance, and semantic contracts

The [frontier audit](FRONTIER_AUDIT.md) distinguishes four unmerged inputs.
F48 at the pinned rolling PR #49 already proves an incidence sheaf on a fixed
run and the injective-interface criterion for arbitrary relation gluing.
Its phase-two extendable-prefix construction must retain its own acceptance
status. PR #50 and PR #53 already contain C22's complete-kernel commutation
and fixed-schedule theorem. CAR already proves unnormalized source/current
transport and finite stable quotient repair. VOYAGER already distinguishes
completion from source realization; nonabelian graph descent and nonregular
deck counterexamples also predate this contribution. Reconstructing them
does not create a new theorem of academic priority.

Our additions are the explicit lawful chosen-map coherence experiment;
the typed extension with continuation/restriction obligations; the separation
of support coupling from operational realization; a public-policy exact
compiler and certificates; and new formal refinement. See [prior art](PRIOR_ART.md)
and [integration map](INTEGRATION.md) for exact attribution and boundaries.

Fix a finite declared source/instrument contract. Original labels
`sigma in Sigma` never change. A public history `h` records occurrence IDs,
actions and receipts, retaining their order and basis/epoch contract. A private
prefix additionally records the initial current state, each intermediate
current state and each genuinely supplied branch token. A complete current
state includes every apparatus, memory, resource and calibration coordinate
needed to determine the declared next-step law. Hidden original dependence
may equivalently remain an explicit index.

An initial law `J_0(sigma,c)` and enabled row
`K_(h,a)(sigma,c;z,beta,c')` are nonnegative rational and normalized. Aggregating
over beta gives the user's kernel. A disabled action has no executable row.
Policies use public history only. Unless an explicit access-report instrument
is part of the contract, an action must be enabled for *every* positive-weight
private possibility at that public history. Menus cannot act as undeclared
source sensors. Mathematical all-prior results quantify only over the stated
admissible starting states; a fixed preparation is a strictly weaker test.

A possible private path has weight

`W(tau) = J_0(sigma,c_0) product_i K_(h_i,a_i)(sigma,c_i;z_i,beta_i,c_(i+1))`.

For a prescribed public action/receipt sequence its source/current law is

`J_(h(a,z))(sigma,c') = sum_(c,beta) J_h(sigma,c) K_(h,a)(sigma,c;z,beta,c')`.

This remains unnormalized: its total mass is evidence for that receipt
sequence under those interventions. Positive support means *possible*, not
*performed*. An actual observation needs a separate delivered-event record;
enumerating paths never performs experiments. Conditioning on a positive
receipt is permitted, but discarding unwanted runs is an additional selection
protocol, not an unconditional change of the source law.

## 2. Exact causal diamonds and their limits

**NG-D (typed all-prior diamond).** Fix a prefix contract and incomparable
occurrences a,b. Assume both orders are publicly admissible, including the
second action after every positive first branch. Identify the two final
carrier types by a specified bijection preserving the complete continuation
interface, or use one common final type D. Align receipts by occurrence.
Let

`L_ab(sigma,c;z,w,d) = sum_(m,beta,gamma) K_(h,a)(sigma,c;z,beta,m)
 K_(h(a,z),b)(sigma,m;w,gamma,d)`

and similarly `L_ba(sigma,c;w,z,d)`. Equality of these rows for all admissible
sigma,c,z,w,d is equivalent to equality of the unnormalized joint
`(sigma,receipt_a,receipt_b,final current)` law for every admissible
nonnegative initial law J, provided its domain includes the corresponding
Dirac laws. Without all Diracs the forward implication still holds, while
necessity concerns only the linear span of permitted preparations.

*Proof.* For each final coordinate, multiply row equality by J(sigma,c) and
sum over c. Conversely evaluate the proposed equality at the unit mass on
each (sigma,c). Enabledness is an additional gate, not a consequence of
numeric equality between unused rows. This is finite linear algebra and a
typed history-dependent extension of C22/CAR, not a new kernel theorem. QED.

The theorem preserves full labelled *public* receipts and endpoint, not the
summed-out intermediate private history. It preserves posterior original
support after positive evidence and predicates of the retained variables.
It preserves future instruments/claims only when their complete laws,
enabledness and interpretation are transported through the supplied final
interface. A history-sensitive future device may distinguish h(a,z)(b,w)
from h(b,w)(a,z) even when the two-event endpoint laws coincide.

The following implications are strict:

| Comparison | What is required | What can still fail |
|---|---|---|
| Equal endpoint value/distribution | Forget all receipts | Different evidence and original posterior |
| Equal separate marginals | Each retained coordinate separately | Receipt/state and source/state correlation |
| Equal summed channel | Sum over receipts | Complete event law |
| NG-D joint law | Every aligned receipt plus source and endpoint | Private path multiplicity or weights |
| Weighted private bijection | Match individual paths and their weights | Chosen family path independence |
| Coherent private bijections | All schedule relations and restrictions | Global source existence or operational frequency |

For example, `(z,d)` laws assigning 1/2 to (0,0),(1,1), respectively
(0,1),(1,0), have identical separate fair marginals and different joint laws.
One instrument pair can expose the first bit then copy it, while the reverse
order exposes a bit then complements the next receipt. Both finish in the
same erased endpoint. Likewise, one private path of weight 1 and two paths
of weight 1/2 have the same constant public law, but no weighted bijection.
The example suite checks these failures at exact rational precision.

For finite weighted fibers a semantic-preserving weight-preserving bijection
exists iff, for every semantic value and exact atom weight, the two fibers
have equal multiplicities. Equal total masses alone are weaker. The proof is
finite matching within the indicated classes. Such a bijection remains a
mathematical comparison, not authorization to replace the recorded branch.

## 3. A lawful three-event comparison with holonomy

Consider two original payload labels, retained unchanged, and three one-use
event occurrences a,b,c. Each event adds its ID to the completed-set current
state, publicly returns `ok`, and supplies a fresh private fair bit. Each
order has eight private bit histories of weight 1/8 for each fixed original;
all six orders are executable. No instrument reads the hidden payload,
resets the carrier, or changes a previous receipt.

A neighboring swap changes the schedule and applies a selected involution
to the two positional bits. Taking `R(x,y)=(x,y xor x)` gives a lawful weighted
bijection of complete private path fibers: it preserves original, public
occurrence-indexed receipts, endpoint, total and individual weights, and
every token outside the exchanged pair. Applying it twice returns the input.
Nevertheless, from positional bits (0,1,0) in schedule abc, the paths 121 and
212 both reach schedule cba and produce (0,1,1) and (0,1,0), respectively.

**NG-H.** Individually lawful source/report/endpoint/weight-preserving
involutive private-history comparisons need not be coherent.

This is a genuine typed stochastic carrier example, but its conclusion must
not be inflated. The comparison *relabels the two private branch values*.
If the requested preservation contract fixes each occurrence's branch value,
R is inadmissible already at the pair level. The token-preserving swap
`S(x,y)=(y,x)` is admissible under that stronger contract and satisfies braid.
Thus the example refutes automatic coherence of a **chosen** family, not
existence of a coherent family for this carrier, and not stochastic
commutation of these independent instruments. It does not retroactively
replace a performed record.

The experiment is [no_ghost_coherence.py](../../../observational_succ/no_ghost_coherence.py).
Its verifier checks every pair bijection and independently replays the failed
paths; forged outputs and stricter token-preservation claims are rejected.
This specializes established asynchronous permutation-tile/cube phenomena;
the conceptual distinction itself is not claimed new.

**NG-I (rigid invariant eliminates holonomy).** Let each schedule fiber H_l
have an injective map e_l into one complete invariant space W. Suppose every
selected edge comparison R_lm satisfies `e_m R_lm = e_l`. Then any two
comparison paths with the same start and end agree. If all e_l are bijections
onto one common image, there is a unique such coherent family,
`R_lm = inverse(e_m) e_l`.

*Proof.* Along either path the invariant is e_l(x). Injectivity at the final
fiber equates the outputs. Existence and uniqueness in the second assertion
follow from the displayed formula, whose middle inverse cancels in every
composition. QED. A complete event-indexed private token assignment supplies
such an invariant in the independent-bit example. Merely naming a quantity
an invariant does not supply injectivity or realizability.

## 4. Finite schedules: weak and strong theorems

Fix a finite event poset P with distinct occurrence IDs. Every linear
extension considered must be lawful under the contract. Adjacent incomparable
occurrences generate the schedule graph. One unlawful branch or missing
permutation removes the corresponding claim of full schedule invariance.

**NG-W (weak law independence).** Assume NG-D for every adjacent swap at every
reachable prefix, use fixed common terminal coordinates rather than arbitrary
path-dependent endpoint identifications, and require the identified final interfaces to have the
same law for every permitted suffix, including equal public enabledness and
the same occurrence-indexed policy/target interpretation. Then every linear
extension has the same source-indexed law of all occurrence-labelled receipts
and the final complete interface.

*Proof.* Condition on the common prefix. NG-D equates its next-pair joint
law, keeping every earlier receipt. The suffix continuation hypothesis
preserves equality after composition. Any two linear extensions are linked
by adjacent incomparable swaps: successively move the first required event
leftward past the events preceding it, all necessarily incomparable, and
repeat on the suffix. Repeated equalities prove the result. QED. This extends
the existing C22 fixed common-kernel statement only by explicit typing and
history/continuation hypotheses. It is not a theorem for arbitrary adaptive
policies, nor an isomorphism of private fibers.

**NG-S (strong finite-poset coherence).** Assign a private fiber to each
linear extension and a bijection to each legal adjacent swap. There is a
path-independent family of those transports iff the following diagrams
commute: a swap followed by its reverse; two disjoint swaps in either order;
and the 121/212 hexagon on three pairwise incomparable adjacent events.
For a restriction-aware causal interpretation require, in addition,
naturality under all specified context restrictions. The hexagon is the
braid relation associated with a three-event cube, not literally a square.

*Proof of sufficiency.* Choose a target linear extension and orient each
swap to reduce the number of inversions relative to it. This nonnegative
integer strictly decreases. Any unsorted extension has an adjacent inversion;
that pair is incomparable because both the current and target words are
linear extensions. Two simultaneously available reductions either are
disjoint, giving the square, or overlap in three descending events. All three
pairs are incomparable, since their relative order reverses in the target;
the two three-step reductions therefore give the allowed braid hexagon.
Induction on inversion number now shows that every reduction path to the
target gives the same map: join the first reductions by the square/hexagon,
then apply the inductive assertion below the starting inversion number.
Every unoriented edge is either a reduction or the inverse of one. The
unique maps to the target therefore factor every edge transport; arbitrary
path composites telescope and are equal. Necessity follows by applying path
independence to each displayed loop. Restriction naturality is a separate
equation and does not follow from this graph argument. QED.

If only a subset of swaps/schedules is authorized, the remaining graph may
have holes not generated by these local relations. One must certify its
actual path-groupoid relations, or use NG-I. The theorem does not silently
complete the allowed graph by adding unavailable executions.

## 5. No-ghost descent on constraint-complete contexts

A finite constraint schema consists of typed variables V and constraints t
with finite scopes S_t contained in V. Variables include original preparation,
current boundary state, branch token, epoch, resource, action-occurrence and
ancestry data whenever they are load-bearing. The preparation relation and
every global resource condition are constraints too. A context is a
subschema: chosen variables and constraint cells, containing the scope of
every chosen cell. Restriction forgets assignments, not their values on
retained variables. A context may contain explicit boundary variables for an
omitted event; it is not thereby an independently executable subexperiment.

Let F(U) be the typed assignments satisfying every constraint cell of U.
A cover jointly covers every variable and **every constraint cell**, not only
every event name. These covers and their pullbacks form a Grothendieck
pretopology: intersection gives pullback, identity covers, and covering all
cells is stable under cover composition.

**NG-G (constraint-complete no-ghost gluing).** For such a cover, a family
of local private assignments has a unique global assignment iff it agrees
on every exact overlap. If full-schema satisfying assignments are, by a
separately checked contract encoding, exactly lawful source histories, the
glue is a lawful history of that same original source.

*Proof.* Necessity is restriction. For sufficiency assign each variable its
value in a covering member. Matching makes this well-defined. Every
constraint has a covering member containing its entire scope, so the union
satisfies it. Coverage makes it unique. The last assertion uses the explicit
sound-and-complete encoding, not an inference from sheafness. QED. This is
F48's mechanism extended to arbitrary finite constraint scopes; it is
classical and explicitly attributed, not a newly discovered sheaf theorem.

**NG-Q (coherent schedule-presentation descent).** Suppose the full context
has at least one allowed lawful schedule presentation. Its restriction to
each context U is allowed, and every allowed local presentation is connected
to that restriction by **authorized** comparison paths. For each fixed full
presentation l, require the assignments `U -> F_(l|U)(U)` and their restrictions
to form a sheaf of the preceding kind. Presentation restrictions and history
restrictions obey identity and composition laws. Suppose comparisons are
invertible, preserve source and all stipulated evidence, are path independent,
and are natural with those restrictions. Then the presentation classes form a sheaf on the same complete
coverage. Its sections are represented by lawful histories, and changing
presentation adds no new original-source witness.

*Proof.* Choose an allowed full presentation. Transport each local class
to its restricted presentation. Path independence makes that representative
well-defined; restriction naturality makes exact overlap equalities survive.
NG-G gives a unique lawful global representative. Changing the full
presentation transports the glued representative, because its restrictions
are the transported locals and the global glue is unique. Therefore its
class is independent of the choice. Conversely a global class restricts
to a matching family. QED. Existence of compatible charts, completeness of
the constraints and naturality are assumptions with independent content.
Neither pairwise diamonds nor a braid test establishes them automatically.

The authorized-connectedness assumption is essential. On two disjoint patches,
give each nonempty context a red and a blue presentation, each carrying a
singleton section, with only identity comparisons. Give the empty context one
presentation. All available comparisons are coherent and natural. The local
red and blue sections match on the empty overlap but have no common global
presentation class. This counterexample was found during manuscript review;
the original weaker formulation is withdrawn and this repaired hypothesis is
retained explicitly in the review record.

This theorem is a conditional construction on a specified site. A global
history can exist when orders fail to commute: a lawful a;b run needs no b;a
comparison. Consequently diamond/coherence conditions are not necessary for
bare gluing. They are necessary for the claimed canonical presentation
invariance. There is no honest universal yes/no hierarchy that conflates
these different requested properties.

### Mandatory obstructions

The [countermodel dossier](GLUING_REPAIR.md) gives detailed proofs and provenance.

* **Destructive execution:** on original bits 11, A returns the first and
  erases the second; B returns the second and erases the first. Separately
  observed receipts 1,1 cannot be collected in either one-carrier order.
* **Projected interface:** left transition ends in state 0; right begins
  at state 1. A constant public quotient matches them, exact pullback is empty.
* **Odd parity:** pair contexts require x xor y = y xor z = z xor x = 1.
  The xor of these equations is 0=1. Pairwise marginal compatibility is weaker
  than a matching family of exact assignments on the full incidence site.
* **Missing global resource cell:** three consumptive events have budget two.
  Every singleton and pair can execute and reorder, all pair-overlap reports
  can agree, yet the triple cannot execute. A purported cover omitting the
  triple budget condition is not constraint complete.
* **Nonregular descent:** the transitive S3 action on three sheets has trivial
  deck centralizer. Every sheet function is deck invariant, but a nonconstant
  one does not descend to the base. Fiber equality, not deck invariance alone,
  is the general descent test. This reprises the prior A04/Cambrian example.
* **Chosen transport:** Section 3 supplies the lawful braid failure.
* **Realization:** eventually-zero binary original streams realize every finite
  all-one observation set, but no admissible original is the all-one stream.
  This is VOYAGER's existing nonclosed-source example. A genuinely finite
  original space with a complete compatible family cannot exhibit that same
  finite-intersection failure; infinite realization adds different hypotheses.

**NG-N (no realization retraction for ghost sheafification).** Let F be a
separated presheaf and let a matching family have no F-glue. Its images glue
in the sheafification aF. There is no natural map r:aF -> F satisfying
`r eta = id_F`, where eta is the sheafification unit.

*Proof.* Apply r to the formal glued section. Naturality makes its restriction
to each member equal the original local section by `r eta = id`; this would
be the forbidden F-glue. QED. The counterexample is not that the valid
constraint-incidence sheaf invents assignments. It is that sheafifying a
weaker report/source-image presheaf does not supply a source-realization map.

## 6. Two different probability polytopes

### 6.1 Source-supported marginal feasibility

Let Omega be a complete enumerated finite set of positive lawful private
executions, and r_i their *specified* local observation restrictions.
For exact rational local laws mu_i, form A with rows (i,u), columns omega,
and entry `[r_i(omega)=u]`, adding a normalization row and any prescribed
source-marginal rows. Then a source-supported coupling exists exactly when

`A p = b, p >= 0`.

This is a classical finite marginal problem with a restricted atom set.
It yields a rational primal witness when feasible. If infeasible, rational
Farkas duality gives y with `A^T y >= 0` and `b^T y < 0`. These signs imply
the contradiction `0 > b^T y = p^T A^T y >= 0`. Verifying either witness
uses only rational sums and comparisons. Finite basic-solution enumeration
is an exact bounded algorithm; a search limit returns UNRESOLVED. Exhaustive
rejection is not reported unless supported by a valid dual or complete proof.

For three pairwise perfect binary anticorrelations, every full assignment
satisfies `Pr[x!=y]+Pr[y!=z]+Pr[z!=x] <= 2`, whereas the proposed marginals
give 3. This is a classical contextuality inequality. On actual legal
histories the matrix may have fewer columns, producing stronger source- or
resource-specific inequalities; arbitrary Cartesian tuples must not be added.

### 6.2 Why support is insufficient for an experiment

**NG-P0 (support-only operational characterization is false).** A prescribed
fair coin has two legal positive histories. Delta(Omega) contains the point
mass at zero, which its prescribed unconditional kernel cannot generate.
Even preserving all source frequencies is insufficient: let hidden sigma
be fair, let the initial public history be empty, and let a blind policy
choose guess 0 or guess 1. Each (sigma,guess) path is lawful; the law assigning
1/2 to (0,0) and (1,1) is supported and has the correct prior. It achieves
success one, whereas every public source-blind randomized policy has success
exactly 1/2. Selecting those correlated branches demands forbidden source access.

Thus the user's support-coupling target is valid as a *coupling* theorem,
but cannot alone characterize operational execution under fixed kernels.
All incoming marginal/prior constraints can pass while this gate fails.

### 6.3 Exact public-policy realization theorem

Build the complete finite public history tree to a declared terminal horizon,
using only public menus safe on every compatible private state. A terminal
node is publicly determined; hidden-state-dependent stopping is disallowed.
Include stop as an explicit action if desired. Assume perfect public recall
and ordinary source-independent controller randomization. The private
tree supplies known rational chance weights W(tau), excluding controller
probabilities. It is a tree of possible histories, not a record that all ran.

For each public node h use a nonnegative controller realization factor r_h;
for each action use r_ha. Impose

`r_empty = 1, sum_(a in A(h)) r_ha = r_h,
 r_(h(a,z)) = r_ha` for every feasible successor receipt z.

At terminal private paths set `p_tau = W(tau) r_(public(tau))`. An explicit
stop edge is included in public(tau) when it terminates the process.

**NG-P (operational gluing iff public realization-plan feasibility).** Under
the preceding finite complete contract, an unconditional family of local
laws is produced by a public randomized policy exactly when these linear
equations, the local marginal equations, and nonnegativity have a solution.
Equivalently the local law lies in the convex hull of local laws induced by
all deterministic public policies under the fixed source/kernels.

*Proof, policy to equations.* Put r_h equal to the product of action
probabilities along h. Summing possible actions gives r_h; chance outcomes
do not change that controller product. Multiplication by W supplies exactly
the full path probability, so the marginal equations follow.

*Proof, equations to policy.* At r_h>0 define `pi(a|h)=r_ha/r_h`. These form
a probability distribution. At r_h=0 choose any declared action when the menu
is nonempty; if the menu is empty, leave the policy undefined at this unreachable
node. All outgoing r_ha are zero, so neither case affects a positive-probability run.
Induction down the public tree gives its controller factors r_h. Multiplying
the declared chance probabilities gives p_tau, proving operational realization.
Normalization follows from normalized preparation, normalized chance rows and
finite termination, not an arbitrary reweighting of leaves.

For the convex-hull assertion, independently sample the prescribed action
for every public decision node in advance. This selects a deterministic
public policy with a source-independent seed and reproduces the behavioral
law. Conversely, a mixture of deterministic policies is implemented with
such a seed; with perfect recall its conditional action probabilities depend
only on the recorded public history. The chance likelihood for a fixed
private path is the same for every deterministic policy consistent with
that public history, so conditioning the seed on the public record does not
leak hidden sigma. This is the finite classical perfect-recall/sequence-form
argument, here explicitly tied to source/carrier atoms. QED.

This supplies a correct narrower operational iff theorem and rational Farkas
certificates. It does not cover arbitrary decentralized controllers,
imperfect recall, restricted private randomness, conditioning chosen after
seeing outcomes, unbounded horizons, incomplete instruments, or an empirical
claim that the declared source is physically true. Such changes require new
constraints and may destroy the stated polytope description.

## 7. Lawful repair, memory, and noncanonicity

Fix a finite menu M of source-backed modifications, their costs, resource
contracts, and exact verification obligations. A candidate may refine a
representation, retain available memory, weaken an independence assertion,
restrict a cover, or perform a genuinely provided extra experiment. It may
not change an original fact or install an omniscient sensor. A menu element
specifies its *effect on the requested task*: restricting a task is not the
same outcome as accomplishing the original unrestricted experiment.

**NG-R (bounded repair).** With decidable finite validation, feasible repairs
are exactly `{m in M : V(m)}`. If nonempty, their finite costs attain a minimum;
enumerating all declared candidates and checking V certifies feasibility and
optimal cost. Failure can be certified only relative to this complete menu,
with a checked rejection for every candidate. A budget/search interruption
is unresolved. This is elementary finite optimization, not universal invention.

Minimum cost is not a least object in an information/resource partial order.
Two legal ways to preserve a receipt may use incomparable memory devices or
different permitted acquisition orders; either can solve the stated task
while their common less-informative predecessor fails. No procedure can
return a lawful *least* repair for every menu because some menus have none.
The prior SUCC tolerance counterexamples already demonstrate noncanonicity;
our exact menu example retains that boundary without changing their result.

For exact deterministic demanded distinctions, let q be the old report and
f the required complete signature. If an extra k-symbol memory m makes f
factor through (q,m), then

`k >= max_y |{f(x):q(x)=y}|`.

*Proof.* States with different required signatures inside one q-fiber must
receive different memory symbols. Conversely, with arbitrary lawful access
to the signature, enumerate its distinct values separately in each q-fiber,
attaining the bound. Without such access this converse is only a mathematical
encoding, not an executable repair. Fixed-width bits therefore require at
least `ceil(log2 k)` bits. General pairwise confusability yields a coloring
bound rather than this special complete-signature count.

Canonical coarsest repairs do exist in restricted full-table categories:
when admissible information equivalences are closed under the appropriate
intersection/refinement construction and the resulting signature is an
available lawful report, the complete signature gives the least adequate
refinement. CAR's stable probabilistic refinement already supplies the
mathematical version. Physical availability is an additional hypothesis.

## 8. What the obstruction structure actually says

| Gate | Certificate/falsifier | Distinct logical role |
|---|---|---|
| Source/interface | Empty exact witness join; disagreeing retained labels | Common original and boundary evidence |
| Executability | Missing safe action/resource constraint; absent complete path | Existence under one contract |
| Diamond | Dirac row and aligned joint law discrepancy | Weak exchange invariance |
| Higher coherence | Two typed comparison paths with unequal images | Canonical chosen private transport |
| Restriction naturality | Compare-then-restrict differs from restrict-then-compare | Descent across contexts |
| Support coupling | Exact rational Farkas inequality on legal atoms | Existence of a nonnegative joint law |
| Likelihood/public policy | Failed realization-plan equations/dual | Actual declared probabilistic protocol |
| Limit realization | Compatible finite profile outside source image | Infinite completion versus original source |

This is a diagnostic list, not a proved independent or exhaustive taxonomy.
Strong weight-preserving private transport implies weak law equality after
pushforward. Weak law equality need not lift to a private bijection; a chosen
bijection family need not be coherent. Operational realizability implies
support feasibility; neither converse holds. Coherence need not imply source
existence, and one lawful global execution need not be reorderable. F48
constraint completeness reduces finite exact gluing to interface matching;
NG-I removes chosen-map holonomy under a faithful common invariant. Finite
source compactness can remove the VOYAGER-type limit obstruction only under
the corresponding continuous/closed-source hypotheses.

Source-preserving isomorphisms of the *whole contract* preserve all these
properties by transporting witnesses, maps and weights; quotienting only
reports need not. A root label or a basis string without preservation laws
is not such an isomorphism. Semantic target predicates transport when the
underlying maps preserve them; syntactic proof objects require a separate
inference-preserving translation.

## 9. Verification and research verdict

The exact examples, independent certificate verifiers, adversarial mutations,
and bounded solver live in the NO-GHOST Python modules and tests. The
[formal report](FORMAL_VERIFICATION.md) records the exact Lean declarations,
compiler version, axiom dependencies and scope; the
[validation receipt](VALIDATION.json) records actual commands and results.
Neither an enumerated finite sample nor a passing unit suite replaces any
universal paper proof. The [claim supplement](../../../docs/CLAIM_SUPPLEMENT_NO_GHOST.md)
distinguishes reconstruction, new-to-SUCC formal/code work, refutation and
unresolved claims.

The broad proposed characterization fails as stated: canonical order
comparison is stronger than bare executability, complete constraints cannot
be inferred from pairwise tests, and support-supported probability need not
be operational. The corrected result is modular: NG-G/NG-Q give conditional
source-backed descent, NG-W/NG-S give the two schedule invariances, and NG-P
characterizes finite public-policy stochastic realization. Finite exact
repair search addresses a declared menu only.

**Novelty verdict:** useful rigorous SUCC integration, a calibrated private
holonomy example, an operational hidden-source countermodel, exact public
policy/coupling certificates, and formal refinement. Academic originality
of a broader theorem remains UNVERIFIED. Existing contextuality, causal
presheaf, asynchronous graph and sequence-form results are too close for a
priority assertion. The smallest consequential next target is a proved
decomposition of the operational realization-plan polytope along causal
interfaces that preserves the controller's information sets. Ordinary
separator/marginal consistency is insufficient unless it also transports
those policy factors. A theorem reducing exact policy feasibility without
enumerating the complete public tree would add leverage beyond repackaging
finite LP feasibility; it is not claimed here.
