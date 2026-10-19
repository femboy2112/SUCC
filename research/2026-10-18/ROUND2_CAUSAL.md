# Round II: nondeterministic source descent and public-belief safety

**Base:** `e42096ec0186228dd0f748767599e470f2ca2e1d` (PR #178 nucleus).
**Status:** general kernel-checked policy/quotient theorems, paper operational
interface theorem and exact obstruction family. **Novelty:** classical
specializations with new project proofs/artifacts; independent academic novelty
is not established. **RH PROVED: NO.**

## 1. Typed source and public grammar

Let S be private states, A permitted action names, O retained outcome labels,
and \(E\subseteq S\times A\times O\times S\) an authorized transition
relation. O may include an outcome, exact cost, and next state observation;
the Python implementation retains exactly these three components. Each
state has an immutable original tag \(\sigma:S\to\Sigma\), and every edge
preserves σ. This is equivalently a disjoint union of source-indexed carriers.
Neither source tags nor private branch identities are available to the public
controller unless explicitly included in O. No missing transition is replaced
by an invented failure outcome, reset, or source switch.

For a complete initial support I in one current-observation fiber, define
\(B(\epsilon)=I\) and
\[
B(h\cdot(a,o))=\{t:\exists s\in B(h), E(s,a,o,t)\},\qquad
\operatorname{En}(s)=\{a:\exists o,t,E(s,a,o,t)\}.
\]
The universal public menu is
\(M(B)=\bigcap_{s\in B}\operatorname{En}(s)\), not the union of private
menus. Reachability of t∈B(h) means one consistent complete private path
exists; the previous `InstituteCausal.reachable_iff_single_source_path`
applies with labels (a,o). Every such path retains its original tag.
An element of B(h) is a mathematical possibility, not evidence that it was
physically visited. Empty beliefs denote impossible public histories.

## 2. General public-policy iff (R2-C1)

A public policy is a tree `stop` or `act a (o ↦ P_o)`. Its branches depend
only on retained outcomes. Define source sure-safety recursively:
\[
\operatorname{Safe}_S(\mathrm{stop},s)=\top,
\quad\operatorname{Safe}_S(a.P,s)\iff
a\in\operatorname{En}(s)\ \land\
\forall o,t\,[E(s,a,o,t)\Rightarrow\operatorname{Safe}_S(P_o,t)].
\]
Define belief sure-safety using the complete support:
\[
\operatorname{Safe}_B(a.P,B)\iff a\in M(B)\ \land\
\forall o\,\operatorname{Safe}_B(P_o,\operatorname{Post}(B,a,o)),
\]
with stop always safe. For every relation E, every belief B, and every
well-founded public policy tree P,
\[
\boxed{\operatorname{Safe}_B(P,B)\iff
       \forall s\in B\;\operatorname{Safe}_S(P,s).}
\]
In particular, for every integer n≥0 a single public controller of exact
horizon n exists iff there is **one same** exact-horizon P satisfying the
right side. The policy existential stays outside the private-state universal.

**Proof.** Induct on P. Stop is immediate. At an action node, safety on B
is exactly simultaneous enabledness at its states. By the induction
hypothesis the o-child is belief-safe iff it is safe at every t for which
there exists s∈B with E(s,a,o,t). Expanding that existential gives exactly
the source universal successor condition. Reverse the same implication
to obtain the converse. Adding the same predicate `Horizon n P` under the
same existential proves the controller corollary. ∎

**Lean:** `belief_safe_iff_all_sources` and `uniform_controller_iff`.
The generic inductive `Policy` allows well-founded trees with unbounded
finite branch lengths when O is infinite; it is not silently asserted to
have one finite height. The `Horizon` corollary explicitly imposes uniform
finite depth. Unsupported outcomes have empty successor beliefs; their
safety obligations are vacuous, not invented executions. Python restricts
requests to nonempty beliefs and uses finite exact-horizon trees.

This is sure nondeterministic safety. It is neither an almost-sure winning
theorem nor a claim that belief alone suffices for all stochastic objectives.

## 3. Exact representative-wise causal quotient (R2-C2)

Let q:S→Q be any map. A quotient relation \(\bar E\) is exact on q(S) if
\[
\bar E(qs,a,o,y)\iff \exists t\,[E(s,a,o,t)\land qt=y]
\tag{1}
\]
for every s,a,o,y. This means every quotient edge lifts from **each fixed
representative** s, and every actual edge is retained. Such a relation
exists iff the right side of (1), as a predicate of a,o,y, is constant on
every q-fiber. No finiteness, choice, or surjectivity assumption is needed.
Off-image behavior of an arbitrary \(\bar E\) is unconstrained; no uniqueness
or source credential is asserted there. The canonical construction below
has no edges out of points outside q(S).

**Proof.** Necessity follows by substituting q(s)=q(t) in the left side.
For sufficiency set
\(\bar E(x,a,o,y)\iff\exists s,t\,[qs=x\land E(s,a,o,t)\land qt=y]\).
Uniformity on fibers transports any witness to each representative of x,
giving (1). ∎

For every exact quotient, every public policy P and every B⊆S,
\[
 q(\operatorname{Post}_E(B,a,o))
  =\operatorname{Post}_{\bar E}(q(B),a,o),\qquad
 \operatorname{Safe}_{B,E}(P,B)
  \iff\operatorname{Safe}_{B,\bar E}(P,q(B)).
\tag{2}
\]
**Proof.** Expand the existential image and use (1) in both directions.
For policy safety, (1) gives equivalence of enabledness at s and qs.
Induct on P: lift each abstract successor back from that same s for one
direction, and project each concrete successor for the other. Apply R2-C1
to pass from states to their entire beliefs. ∎

**Lean:** `exact_quotient_exists_iff`, `quotient_enabled_iff`,
`image_post_iff`, `source_policy_descent_iff`, `belief_policy_descent_iff`.
Current state observations must separately factor through q when they are
claimed as quotient observations. A source-indexed quotient can keep σ as
a component; otherwise original identity remains in the lifted concrete
history, not necessarily in q(s). A mathematical quotient does not create a
new physical sensor.

This exact quotient criterion is a bisimulation-style condition. It is
**sufficient but not necessary** for preserving the public safety interface.
R2-C4 below is the weaker operational iff; the two claims are not conflated.

## 4. Required split/combined discriminator (R2-C3)

Source A: root executes a with the same public outcome `ok`, privately reaching
either u or v. At u only b is available; at v only c is available. Each leads
to a common terminal report. Source B: root executes a to m, where both b and
c are available. All costs are one and original tags remain fixed.
The implementation calls b,c `b0`,`b1` for its parameterized family.

| Relation/property | A versus B |
| --- | --- |
| Possible public finite traces | Equal: ε, a, ab, ac, with the corresponding labels |
| Ordinary simulation | B simulates A; A does not simulate B |
| Bisimulation | Fails: m cannot match either private menu of u,v |
| Public menu after a | A: empty; B: {b,c} |
| Exact-horizon two-action public controller | A: impossible; B: exists |
| Individual source histories ab and ac | Both exist in A, on different private paths |
| Original probability laws | Not specified by nondeterministic support |

The failure is the illicit exchange
\(\forall s\in B\,\exists a\) for \(\exists a\,\forall s\in B\).
`private_choices_do_not_glue` proves the Boolean quantifier obstruction
in Lean. The complete A/B systems are checked by the exact finite oracles.

For stochastic comparison we **add** explicit full-support chance laws:
A chooses u,v with probabilities 1/2,1/2 and B reaches m with probability 1.
The existing public-policy compiler at horizon two gives an exact Farkas
obstruction for A and a verified realization plan for B. In A the raw flow
equations can be written
\[
r_\epsilon=1,\quad -r_\epsilon+x_a=0,\quad r_a-x_a=0,\quad-r_a=0.
\]
Their coefficient-row sum is zero while their right-hand-side sum is one;
the dual multiplier (-1,-1,-1,-1) is an exact contradiction. The replay
also stores the compiler's marginal-normalized system and verified dual.

A forced b at A's hidden v state is unavailable. It has **no original lawful
chance law**, rather than a silently inferred half-success/half-failure law.
Adding a failure transition would change the source and requires its own
contract. Separately, two fully legal coin kernels with probabilities
1/3,2/3 versus 2/3,1/3 have identical support and different exact report laws.
Thus neither traces, simulation nor public safety identifies stochastic weights.

## 5. Weakest retained finite public interface (R2-C4)

Assume the same initial public observation (otherwise the empty experiment
already distinguishes the sources). For finite declared sources compare
their nonempty public beliefs by the
following deterministic interface: the safe menu M(B), and, for each safe
action a, the set of possible retained reports together with their successor
beliefs. Explore only prefixes realized by a **common safe public policy**.
Two initial beliefs have the same such interface behavior iff:

* every public policy with stopping allowed is sure-safe from one exactly
  when it is sure-safe from the other; and
* for each policy safe in both, its possible public transcripts agree.

The quantification is over finite policy experiments; the finite product
search is complete because only finitely many pairs of belief subsets exist.

**Proof.** Interface agreement inductively preserves each chosen action,
its report branches, and continuation obligations, so it preserves safety
and transcripts. Conversely take the first separating safe prefix in the
product exploration. Follow its actions on that prefix and stop off-branch.
If safe menus differ, append a distinguishing menu action on that branch:
the policy is safe in just one source. If report sets differ, take the same
safe next action and stop; the resulting possible transcript distinguishes
the two sources. Every constructed policy uses only declared public history.
Finite product exhaustion supplies a closed relation for the forward proof. ∎

**Authority:** paper proof plus exact finite product oracle,
`compare_interfaces(..., public_safe=True)`; not separately Lean-formalized.
This is not a claim that inaccessible unsafe traces are physically testable.
The `public_safe=False` mode separately compares all mathematical may-traces.

Strictness control: move the b/c difference from *chosen actions* to *outputs*
of one always-enabled action `tick`. A privately selects u/v after output a;
u emits b and v emits c. B reaches m capable of emitting either output.
Terminal tick loops emit z. These sources have the same public safety
interface and possible traces but are not bisimilar. Therefore R2-C2 must
not be advertised as necessary for R2-C4.

## 6. Exact exponential interface obstruction (R2-C5)

For every n≥1 there is an n-state source-preserving model with 2n actions
and **2^n−1 reachable pairwise distinguishable public beliefs**. The initial
support contains all n states and all have the same public observation.
At private state s, `test_j` always executes, keeps s unchanged, and reports
`hit` iff s=j, otherwise `miss`. `guard_j` keeps s unchanged and is enabled
exactly when s≠j. Costs are one; each s has its own immutable original tag.

Every nonempty B⊆S is reachable by a sequence of safe `test_j` actions for
j∉B with `miss` outcomes. Its uniform menu contains `guard_j` exactly when
j∉B. Thus different B have different menus. Any deterministic monitor that
exactly returns every reachable safe menu must assign different internal
states to all 2^n−1 beliefs. This supplies a lower bound on exact explicit
interface state size, matched by the ordinary subset upper bound. ∎

`guard_safe_iff_absent` and `differing_beliefs_have_separating_guard` are
Lean-kernel proofs of the separating implication. The arbitrary-n construction,
reachability and finite counting are paper proofs, with all 120 nonempty
subsets for n=1,…,6 checked exactly. This is the classical worst case of
subset/interface determinization in a source-faithful grammar, not a new
complexity-class result. It does not prove exponential memory is needed for
a winning controller: repeatedly choosing a test is a safe memoryless policy.
Symbolic representations can be compact despite this explicit-state bound.

## 7. Algorithms, certificates and connection to previous NO-GHOST work

`synthesize` is exact finite-horizon AND/OR dynamic programming on (B,n).
A winning certificate records one public action and a continuation for every
possible retained report. A losing certificate records, for **each** action,
either a compatible private state where it is unavailable, or one possible
report leading to a certified losing smaller-horizon belief. A failed budget
returns `UNRESOLVED`, never a theorem of impossibility. A verifier checks
winning policies by direct private-path replay and losing certificates by
raw edge checks; it does not call the synthesis recurrence or support helper.

Certificates bind the complete declared model digest, including original
tags, source ID, basis, grammar, costs and transitions. Tests reject a forged
source ID/basis, same-ID changed table, unavailable branch deletion, counterfeit
controller, missing outcome branch and cross-original transitions. Digests
authenticate bytes of a supplied mathematical model, not a physical source.

The independent oracle enumerates full public decision trees and checks them
directly from each private state. It agrees on all 2,304 cases from every
two-state/two-action/one-outcome transition relation at horizons 0–2 and all
three nonempty initial supports, plus 192 seeded two-outcome adaptive cases.
The existing rational public-policy LP independently checks the required
A/B example; its equations preserve chance weights and source preparation.
These are distinct implementations within one authoring/model lineage.

The preserved `no_ghost.py` Farkas machinery handles exact nonnegative
probability constraints, whereas the new losing certificate is logical
AND/OR exclusion. They have different mathematical meanings. Existing
`no_ghost_coherence.py` and `formal/NoGhost.lean` retain cube/hexagon and
private-history path-comparison obligations. No action exchange is authorized
by belief equivalence: the new policies retain action order, and no diamond,
braid relation or private branch bijection is inferred. The source grammar
must supply any action-order transformations and their coherent laws.

## 8. Prior art and claim boundary

Trace, simulation, failures/readiness, and bisimulation belong to established
process semantics. Van Glabbeek's *The linear time—branching time spectrum*
systematizes these distinctions; [primary CWI record](https://ir.cwi.nl/pub/5685)
and the [author's paper](https://www.cse.unsw.edu.au/~rvg/pub/spectrum90.pdf).
At a fixed public prefix, unsafe availability of one action is exactly an
existential singleton refusal; the safe menu is its complement. Restricting
R2-C4 to lawful prefixes records the authorization constraint, not a claim
to have invented failure semantics.
The displayed A/B system is a classical branching-versus-trace discriminator.
R2-C2 is a relational coalgebra quotient/bisimulation specialization; see
[Silva–Bonchi–Bonsangue–Rutten (2013)](https://arxiv.org/html/1302.1046v2).

Observation-based strategies and knowledge-set constructions predate this
work; [Chatterjee–Doyen–Henzinger–Raskin (2007)](https://arxiv.org/abs/0706.2619)
treat much stronger omega-regular objectives. The public-policy iff is a
carefully typed sure-safety instance, not a new solution of those games.
Its stochastic limits matter: [Chatterjee–Doyen (2011)](https://arxiv.org/abs/1107.2141)
exhibits settings where belief-based strategies fail for quantitative winning
objectives. None of those objectives is imported into R2-C1.

New project capability: an actual nondeterministic public controller theorem,
a verified logical obstruction engine, an operationally exact finite safe
interface comparison, an explicit exponential menu-interface obstruction,
and authentic integration with the old probabilistic source constraints.
No academically new general theorem is claimed. The proposed extension
"may-trace equivalence suffices for public-safe source descent" is **REFUTED**,
with the required source-bound A/B and LP receipts.

## 9. Provenance, validation and remaining work

New files leave the old source/kernel/provenance artifacts unchanged.
Dependencies at the base commit include `no_ghost.py` blob
`e9c6f479f51ef2ccf08ae0b1eb1b0fb259b37d11`, `no_ghost_policy.py` blob
`1a84ff3c0dfa1c9dbeea8d47e80da8ef2d39e52b`, and `InstituteCausal.lean` blob
`360ba66fc1a271d2411fb7c7a0942e350b9fa8ad`.

Kernel file: `formal/round2/PublicBelief.lean` (core Lean 4.14).
All ten public theorems print exact axiom reports; nine use no axioms,
`belief_policy_descent_iff` uses only `propext`. Verifier:
`python scripts/round2/verify_causal_lean.py`. It checks the pinned compiler,
rejects forbidden proof escapes, calibrates by rejecting a false proof,
and compares all actual declarations/axioms with the explicit manifest.
The first draft's stop-case tactic failed; the repaired proof uses explicit
introductions, and only subsequent clean compilation supports kernel claims.

Replay: `python research/2026-10-18/round2/causal/replay.py`. Exact commands,
versions, test outputs, source hashes, LP primal/dual data, the repaired failed
proposal and resource limits are stored beside the script. Full-suite
integration and remote CI belong to the principal's separate delivery gate.

Next discriminator: extend R2-C4 from finite-horizon sure safety to an explicitly
chosen quantitative stochastic objective, preserving original kernels and
public randomization semantics. Equal supports alone must fail the legal coin
control before any stochastic equivalence claim can be accepted. Another
formal debt is mechanizing R2-C4's weakest-interface theorem and R2-C5's full
arbitrary-n counting argument; only the policy/quotient core and guard
separation presently carry kernel authority.
