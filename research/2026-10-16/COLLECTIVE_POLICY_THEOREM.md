# Chronological collective original-target policies

**Status:** PROVED LOCAL, PAPER for the finite theorem and counterexamples below;
TESTED MODEL for Python and exact enumerations. No kernel formalization is
claimed. This dossier contains no arithmetic or physical realization theorem.

**Owned implementation:** `observational_succ/collective_policy.py`,
`tests/test_collective_policy.py`, `scripts/collective_policy_probe.py`.
Receipts: `collective_observer_receipts/policy_*`. The principal owns Git and
the separate effects/status layer; this module does not duplicate that layer.

## 1. Contract and faithful statement

There are finite nonempty sets of original sources S and current joint states C,
and a finite action set A (possibly empty). A current state explicitly contains
the current carrier, one local memory/control value for each registered E, and
a vector of physical resource stocks. The complete initial relation I ⊆ S×C is
nonempty and covers S. Multiple realizations per source, multiple sources at one
current realization, destructive operations and resource replenishment are
allowed. **A source name is not a physical realization or an observation.**

An immutable original-target map τ:S→L is given. Target winning means computing
τ(s), not identifying s. For example, two distinct sources with the same τ are
certifiable immediately with one terminal certificate and no observation.
Source identification is the special case where τ is injective.

Each action a has actor, kind, complete finite support rows
R_a(c) ⊆ Y_a×V_a×C, and a nonnegative integer cost vector. An empty row means
disabled. Y is public; V is an optional actor-private readout (None is a genuine
absence of additional readout). Tables depend on CURRENT c, never on the
original s separately. Supports may contain multiple outcomes and multiple
poststates at the same public outcome. There are no probabilities or fairness
assumptions. Private readouts are audit values, never public branch keys.

A policy is a deterministic tree whose node is determined solely by the full
public action/outcome history h=((a₁,y₁),…,(a_k,y_k)). It either reports a target
label or selects an action. Action selection does not receive actual source,
current state, private readouts, or a state-specific menu. The policy is legal
only when its action is enabled at EVERY current realization compatible with h.
Thus selecting an unavailable action cannot be used as a free sensor. Models
needing failure observations must supply an executable action and explicit
failure outcome, with its costs.

The contract is a **public coordinator** with E-owned actions, private registers,
and explicit reliable message actions. It is not a completeness theorem for
arbitrary decentralized strategies conditioned on private histories. Public
probe outcomes are explicitly visible; private outcomes require messages.

## 2. Independent metrics and source assumptions

The coordinate order of `Cost.vector` is
`(depth, actions, messages, communication_bits, observation_bits, certificate)`.

| Coordinate | Exact interpretation in this model |
|---|---|
| depth | One per chosen action/macro, guaranteeing well-founded search |
| actions | Declared number of physical primitives; a macro can exceed one |
| messages | One per explicit reliable send, zero for physical operations |
| communication_bits | Fixed-width message-payload alphabet width; framing excluded |
| observation_bits | Fixed-width joint (public outcome, private readout) alphabet width per physical action |
| certificate | Declared additive verification work per actual path, plus terminal work |

For a finite nonempty alphabet of size n, its minimum fixed-width binary code
length is ceil(log₂ n)=(n−1).bit_length(): length b has 2^b distinct words, so
2^b≥n is necessary; assigning distinct words when 2^b≥n is sufficient. Validation
requires at least this width over the action's entire declared alphabet. Thus a
known constant report costs zero bits but its performed action/event still has
depth and action/message cost. These are code lengths, not entropy, raw analog
bandwidth, conditional compression optima or lower bounds on physical energy.

All budgets bound worst-case sums along **each actual execution path**.
`Replay.policy_nodes` separately counts nodes of the unfolded public tree; it is
not the path certificate cost or serialized byte length. Certificate units are
declared by the model, not a claim of minimal proof complexity. Physical resource
stock is in C and can change independently of cumulative cost; unused budget
does not imply possession of a physical resource. Search/replay expansion limits
are a further computational constraint and raise `SearchLimit`, never LOSS.

A message is deterministic on sender memory, updates receiver memory only from
(old receiver memory, payload), and preserves carrier and all other local
memories. It has no new sensor readout. Nonmessage local updates must factor
through old local memory and public outcome, plus the private readout only for
the acting observer. This prevents a purported zero-readout operation from
silently installing distinguishable private measurements in local registers.
The checks compare all enabled rows, not one favorable representative. Payload
and readout bit charges are separate; observing and transmitting one bit costs
one in each coordinate. For macros, observation bits encode the complete public
report word, not the sum of independently encoded intermediate reports.

**Premises, not conclusions:** completeness/accuracy of S, I, τ, all jointly
enabled transition rows, resource effects, sensor alphabets, local memory
interpretation and message delivery. No source passport authenticates the world.
There are no automatic products of individually certified E models. Every joint
coupling must already appear in C and the rows. Without an actual source law,
these are declared table realizations; passing tests cannot pay that source debt.

## 3. Belief lemma, soundness and completeness

Let B(h) be all pairs (s,c) realized by some concrete run from I with public
history h; discard neither original source nor current joint state/resources.
For uniformly enabled a and public y define

    U(B,a,y) = {(s,c') : (s,c)∈B and (y,v,c')∈R_a(c) for some v}.

Only nonempty U are branches. Distinct public outcomes are distinct children;
hidden nondeterministic poststates at the same outcome are UNIONED in one child.

**Lemma (exact public belief).** Starting with B(ε)=I and applying U gives
exactly B(h) for every legal public history.

**Proof.** The empty-history statement is the definition of I. Suppose it holds
at h. Every concrete extension emitting y has a predecessor (s,c)∈B(h) and an
atom (y,v,c') in that action row, hence is in U. Conversely any member of U has
such a predecessor; by induction a concrete run realizes it, and appending the
witness atom realizes the claimed extension. Original s is unchanged. Both
inclusions hold, including merged poststates and multiple preparations. ∎

Let ℓ be a fixed terminal cost with only a certificate coordinate. A belief is
terminal for label t iff every (s,c)∈B has τ(s)=t. Costs are componentwise ordered.
With remaining budget r, define W(B,r) by:

* a terminal label exists and ℓ≤r; or
* some a is uniformly enabled with c(a)≤r, and for EVERY public y with
  U(B,a,y)≠∅, W(U(B,a,y),r−c(a)) holds.

Every action has depth cost one. Thus this is a well-founded definition by
remaining depth, including zero-cost moves in any other coordinate.

**Theorem (finite-budget exactness).** For every model satisfying the contract,
every nonempty belief B and natural vector r, W(B,r) iff a legal public-history
policy terminates with the correct ORIGINAL target on every supported concrete
run, using at most r on each path. The implemented solver returns such a policy
iff W(I,r), provided its search limit is not reached.

**Proof, soundness.** Induct on r.depth. A terminal node is correct for all
compatible originals by homogeneity and is affordable by ℓ≤r. At an action node,
uniform legality permits execution for every compatible state, and affordability
pays c(a). Every concrete outcome belongs, by the lemma, to one of the nonempty
children whose remaining depth is smaller. The induction hypothesis certifies
that child's original target and residual path costs. All supported outcomes
are included, so the guarantee is universal, not an existential lucky run. ∎

**Proof, completeness.** Induct on remaining depth for any winning policy at B.
If it stops, correctness on every possible source implies homogeneity, and the
terminal cost is affordable. If it acts, its root action is one fixed public
choice, hence uniformly legal and affordable. Every nonempty U has at least one
supported realization. Its continuation must win for ALL realizations in U,
or the original policy would have a failing run. Each continuation has depth
at most r.depth−1 and budget r−c(a), so induction gives W for every child. Thus
the action satisfies the recurrence. At depth zero only stopping is possible. ∎

**Implementation and termination.** Forward exploration stores (B,r), explores
every affordable uniformly legal action, and stops exploring homogeneous beliefs.
This pruning loses nothing: stopping there is safe when ℓ≤r; if ℓ≰r, no further
nonnegative expenditure can make the same mandatory ℓ affordable. With
N=|S||C| and initial vector b, there are at most

    (2^N−1) ∏ᵢ(bᵢ+1)

distinct belief/budget nodes. Every edge strictly decreases depth. Sorting nodes
by increasing remaining depth therefore computes the recurrence without cyclic
assumptions. A winning node stores one action and all winning outcome children;
a losing node has no such action. The public tree forgets the hidden audit state.
Merging two equal (B,r) nodes is safe because the recurrence depends only on that
pair and the fixed model; retaining the full public history in tree position
still permits history-dependent strategies. These observations and the two
inductions prove the solver claim. Selection is deterministic lexical feasible
choice, not a shortest-policy or Pareto-optimality assertion. ∎

**Independent replay.** The interpreter enumerates concrete run prefixes, without
the planner's edge/belief helpers or state-merging cache. At each public node it
checks every raw row, affordability, exact branch coverage and every original
target at termination. Induction on interpreted nodes proves that accepted
leaves are precisely all executions of the submitted tree within the budget.
Its count of public nodes includes counterfactual branches; its path metrics do
not sum costs across mutually exclusive branches. This is algorithmic redundancy,
not an independent author or physical evidence source.

## 4. Hostile examples and strict collective advantage

**Cross-enabled ladder.** Two sources s0,s1 have original target 0,1. The only
chronological path is

    p0(A), send A→B, p1(B), send B→A,
    p2(A), send A→B, p3(B), send B→A.

The first three probes perform constant observations and install prerequisite
tokens. Predictions do not install those tokens. Each following message updates
the recipient's enabled local control state. Probe p3 records the private source
bit; its public acknowledgement is the same at both sources. Only the last send
publishes that bit. All steps consume the finite joint resource counter.

**Proof of strict advantage and exact costs.** The full coalition executes this
path and the final message distinguishes the original target. Before that send
the two sources have identical public histories, so no earlier leaf can certify
the target. At each phase only the displayed action is enabled, proving that
every winning policy must perform all eight decisions. Each of the four probes
costs one physical action; each relay costs one message. Only p3 has a two-valued
readout alphabet, and only the final relay has two payloads. There are eight
declared step verification units and one terminal unit. The necessary and
sufficient vector is (8,4,4,1,1,9). A alone gets through p0 at most; B alone cannot
start. Communication endpoints outside the coalition are removed too. Hence the
complete availability ablation is W(∅)=W(A)=W(B)=0, W(A+B)=1. Its mixed difference
is 1, demonstrating non-additivity of this binary score, not a physical mechanism
inferred from the score. The explicit transition construction supplies the model
mechanism. Private source bits in replay are audit values, not policy inputs. ∎

**Mutually exclusive unperformed histories.** Source (a,b)∈{0,1}², target a XOR b.
Either probe reads its own bit and consumes the only token. Pooling both possible
one-probe histories would determine parity, but a real path can read only one.
After reading a, sources (a,0),(a,1) collide; after reading b, sources (0,b),(1,b)
collide. No token and no action remain, so no chronological policy can win at any
horizon. Capacity two is the positive control and wins in two decisions. ∎

**Pairwise but not joint availability.** Three source bits, target their parity,
three probes and two shared tokens. Every pair can be executed, in either order.
After any two probes, flipping the unmeasured bit preserves the entire performed
history and all enabledness facts but reverses the target. This also refutes an
adaptive policy: its successive choices are functions of the unchanged history.
No triple is executable. Thus pairwise feasibility does not establish collective
target feasibility. Capacity three wins in three decisions. These are explicit
joint models, not products inferred from pair certificates. ∎

**Other preserved hostile controls.** Resetting two opposite-target originals
to one carrier never identifies their original target. Same actual state with
different original labels need not identify anything. An action available only
at one hidden source is not an allowed initial choice. A nondeterministic retry
instrument can have arbitrarily long constant retry histories; favorable outcomes
do not make it win under any finite bound. Same public outcome with two hidden
poststates cannot be replaced by one representative. A recorded random flip
followed by a read is the positive backaction control: its public coin and current
bit together determine the original bit. Missing AND branches, undercharged
alphabets and private readings smuggled into memory updates are rejected.

## 5. Actual dependencies, MiniPort and limits

Read and retained boundaries from actual current sources: `knowledge_ladder`
(performed tokens and strict relay), `absorbing_frames` (prediction vs event),
`adaptive_proof_policy` and `noncommuting_proof_transport` (original/current
transport), `miniature_stochastic` (joint outcome/poststate support, not marginal
projections), `interobserver_channels` (fixed-width coding and source premises),
`consensus_lambda` (potential portfolios vs chronological execution),
`miniature_carrier` (all-state factor squares), `operational_yoneda_descent`
(continuation-sensitive policy transport). No archival source was modified.

`miniport_model` calls the actual `MiniPort.validate` and thus `compile_factor`.
It executes each compiled word on the actual parent action table, translates
parent PUBLIC reports at primitive endpoints, and snapshots an immutable model.
It never reports the hidden factor decoder. Empty words explicitly read the
current report. The receipt retains passport, all-state factor validation and
macro execution audit. The tested two-state flip produces current carrier 1 for
original 0 and conversely; the policy correctly certifies T0/T1 from translated
R1/R0. Primitive counts and full public report-word alphabet costs are recorded.
This is a verified finite table integration with an explicit endpoint-sampling
convention. Hardware, sensor calibration, network realization, physical
independence, and faithful source identification remain external debts.

**Scope of negatives.** General solver LOSS means no winning target policy under
that exact budget and declared full joint model. It is not an all-continuations
no-go, a source-identification result, or invariance under new actions. The two
capacity examples have separate all-horizon proofs above. Agreement of current
target labels/compatible sources is weaker than continuation equivalence: the
one-token and two-token models start with the same source/target semantics but
have different future winning behavior. No new bisimulation engine is claimed;
existing `operational_yoneda_descent` covers its stated deterministic transport
domain. Extending such equivalences here must preserve joint enabledness,
outcome/current-resource coupling, original targets and costs, not just labels.

## 6. Exact evidence and remaining debts

The exhaustive oracle enumerates public binary-outcome trees and evaluates each
directly against raw concrete runs; it does not use the solver recurrence,
belief updater or replay interpreter. It covers all 625 two-action deterministic
two-state support tables and all 256 one-action nondeterministic two-state
support tables (including disabled rows), all four binary original-target maps,
and depths 0,1,2: **3,524 models and 10,572 budget comparisons**. Every winning
comparison is additionally replayed. These finite checks corroborate code; the
inductive theorem above supplies the quantified finite-budget proof.

Run `python -m unittest discover -s tests -p test_collective_policy.py` and
`python scripts/collective_policy_probe.py`. `policy_probe.json` records exact
policies, every ladder replay, all six one-coordinate shortage controls, hostile
collision histories, factor receipt, exhaustive counts and source hashes.
`policy_validation.json` and its logs retain execution commands and statuses.
Probe bytes are deterministic for identical source files; wall-clock validation
metadata is deliberately separate. Principal-owned integration gates remain
distinct from these scoped checks.

| Claim | Status and boundary | Next falsifier/debt |
|---|---|---|
| Finite-budget AND/OR exactness | PROVED LOCAL, PAPER; above contract | Formalize recurrence or expose an omitted legal policy |
| Python realizes that recurrence | TESTED MODEL; exact small exhaustive controls and hostile cases | Larger independent solver, fresh resources/nondeterminism |
| Strict collective ladder advantage | PROVED LOCAL, PAPER plus TESTED MODEL; explicit finite joint table | A legal isolated path or smaller cost vector |
| Accessible-history union / pairwise feasibility suffices | REFUTED by concrete collision histories | Repair with chronological joint execution |
| MiniPort realizes the planner's finite flip | TESTED MODEL using actual factor and parent macros | Alter a report/action square; physical validation is separate |
| Original table corresponds to actual external source | UNVERIFIED | Authenticated preparations, joint instruments and calibration |

κ here is direct access to repository tables/executions, not physical contact.
φ is bounded target-policy distinguishability; σ remains the declared source map.
The paper, implementation and controls share author/table lineage and are not
three independent empirical witnesses. ρ/commitment is controlled by preserving
the losing and mutation cases. No phasor or probability interpretation is used.
