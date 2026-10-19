# Minimal stable repair versus lawful acquisition

**Base:** PR179 `81684b4b8956f9f5da56c376ba7e4339277eb665`.
**Sibling audited separately:** PR178 `e42096ec0186228dd0f748767599e470f2ca2e1d`.
**Verdict:** classical stable refinement and coding bound; proved finite
cost-sensitive acquisition/coloring characterization; academic priority of
the combined formulation **UNVERIFIED**. No physical energy, authentication,
source restoration, or RH conclusion.

## 1. Compatible interfaces, not a merger of semantics

PR178 `INSTITUTE_CAUSAL_DESCENT.md` §§1–5 and `InstituteCausal.lean` were read
from the separate reference extraction; `git show` verified its commit.
Its quotient preserves a partial action label and successor class. Its
original-source tag is private and invariant. Its failed run returns `none`,
discarding the successful prefix. PR179's `future_safe_quotient.py` preserves
source identity as an output and retains the successful prefix before
rejection. Those are different interfaces. Their common local requirement is
constant output/domain/label/successor-class data on each quotient fiber.
Only that requirement is reused below; no sibling history was imported.

The acquisition model deliberately has **no refusal oracle**. A probe is
permitted only when enabled at every currently possible private carrier.
Consequently PR179's pair-distance theorem, which allows a specified rejection
interface, cannot be inserted unchanged into this model. Even when every
relevant pair has a lawful distinguishing probe, joint identification can
fail, as §6 proves.

## 2. Coarsest autonomous repair and optimal label alphabet

Let finite nonempty \(X\) carry a deterministic partial source system with
output \(o:X\to O\), partial maps \(\delta_a:D_a\to X\), and exact
nonnegative rational edge costs. Source identity, proof-task results and
other preserved fields are part of \(o\) if the application requires them.
Let \(q:X\to Y\) be the representation already retained.

An equivalence \(R\) is stable if related states have equal outputs, equal
enabledness for every action, and, on enabled actions, equal costs and
\(R\)-related successors. Let \(R_*\) be the greatest stable equivalence
contained in \(\ker q\). More explicitly it also refines \(\ker o\) by
the definition of stable. It is behavioral equivalence for the same machine
with enriched output \((q,o)\).

**Theorem R (CLASSICAL specialization).** \(R_*\) exists. Starting at
\(\ker(q,o)\) and refining by every action's availability, cost and
previous successor class reaches it after at most
\(|X|-|(q,o)(X)|\) strict refinements. For any surjective autonomous repair
\(r:X\to Z\) from which \(q\) and the designated outputs factor,
there is a unique map \(f:Z\to X/R_*\) with \(\pi_*=f\circ r\).

**Proof.** The successive finite-word equivalences form a decreasing chain.
An equality of two consecutive partitions makes that partition stable, and
each strict refinement increases the number of classes. Every stable
equivalence refining \((q,o)\) refines every stage by induction. Thus the
stable terminal partition is greatest. For a proposed repair \(r\), its
kernel is stable and refines \(q\), hence is contained in \(R_*\).
Define \(f(r(x))=[x]_{R_*}\); kernel containment proves well-definedness,
and surjectivity gives uniqueness. This is the enriched Moore/Nerode
construction, not new general coalgebra. \(\square\)

**Important:** \(R_*\) need not be \(\ker q\) intersected with the
unenriched behavioral relation. Constant-output states \(u,v,w\) with
one zero-cost action \(u\mapsto u,v\mapsto w,w\mapsto w\) all have the
same old behavior. Set \(q(u)=q(v)=0,q(w)=1\). Their intersection is
\(\ker q\), which is not stable; the true repair separates all three.

For each nonempty \(q\)-fiber set
\(k_y=|q^{-1}(y)/R_*|\), and \(K=\max_y k_y\).

**Theorem M (CLASSICAL finite coding/counting).** The minimum alphabet size
for an auxiliary label \(\alpha:X\to\{0,\ldots,k-1\}\) such that
\((q,\alpha)\) is an autonomous sufficient repair is exactly \(K\).
The minimum fixed-width supplemental memory is

\[
 b_{\rm final}=\left\lceil\log_2 K\right\rceil.
\]

**Proof.** Theorem R forces the kernel of any admissible \((q,\alpha)\)
inside \(R_*\). Inside a fixed \(q\)-fiber, representatives of its
\(k_y\) distinct classes therefore require distinct auxiliary labels:
\(k\ge k_y\). Conversely enumerate the \(R_*\)-classes separately
inside each \(q\)-fiber and reuse labels \(0,\ldots,k_y-1\) in each
fiber. The combined pair then has kernel exactly \(R_*\), so its update
descends. A binary alphabet of width \(b\) has \(2^b\) possible labels,
giving the stated ceiling. \(\square\)

The encoder is allowed to inspect \(x\); its mathematical existence is not
a sensor. The decoder/update knows \(q\), so label reuse across different
fibers is permitted. The auxiliary label alone need not update autonomously.
The bound is for exact fixed-width retained state after repair, not expected
entropy, variable-length coding, controller workspace or acquisition cost.

## 3. A separate lawful acquisition problem

Fix original sources \(X_0\), finite current carriers \(Z\), an initial
map \(i:X_0\to Z\), and an immutable target \(t:X_0\to T\), normally
the original \(R_*\)-class. The observer initially knows \(q(x)\).
Each probe \(a\) is a deterministic partial table

\[
 z\longmapsto (\rho_a(z),c_a(z),d_a(z)),\qquad c_a(z)\in\mathbb Q_{\ge0}.
\]

Only the receipt and exact charged cost are observed. A belief is a nonempty
finite set \(B\subseteq X_0\times Z\), with at most one current carrier
per original source. It retains the **original** source coordinate through
all destructive evolution. A probe is lawful at \(B\) iff it is enabled
at every carrier in \(B\). For outcome \(h=(\rho,c)\),

\[
 B_{a,h}=\{(x,d_a(z)):(x,z)\in B, (\rho_a(z),c_a(z))=h\}.
\]

Empty outcomes are ignored. Success means all original coordinates in the
terminal belief have the same \(t\)-value. All branches must terminate.
The objective is the worst total charged cost over the possible original
sources. Policies may use their entire transcript; no bound is imposed on
temporary controller memory or retained policy description.

This obtains knowledge of the original repair class. It does **not** restore
the original carrier after probing or certify that its future actions remain
available. To continue the original task dynamics, supply a separately proved
restoration/simulation bridge. Changing the target to a current postprobe
class would be a different, sometimes trivial, problem.

## 4. Exact proper-policy cost and local certificates

For a given family of starting beliefs, close under all lawful probe outcomes
until reaching successful beliefs, where stopping is permitted. This finite
arena has \(N\) beliefs; one coarse bound is
\((|Z|+1)^{|X_0|}-1\). Let \(V(B)\) be the least worst-case cost of a
terminating lawful identification tree, or \(\infty\) if none exists.
Set \(V_0(B)=0\) on success and \(\infty\) otherwise, and

\[
 V_{n+1}(B)=\min\!\left(V_n(B),
       \min_{a\ {
m lawful}}\max_{h:B_{a,h}\ne\varnothing}
       [c(h)+V_n(B_{a,h})]\right)
\]

on nonterminal beliefs. Empty action minima mean infinity.

**Theorem A (PROVED LOCAL, classical finite decision-tree specialization).**
\(V_N=V\). Every finite optimum is attained and rational. An exact value
certificate consists of a value \(L(B)\in\mathbb Q_{\ge0}\cup\{\infty\}\)
for every arena belief, with:

1. Successful beliefs have value 0 and stop.
2. For every lawful action,
   \(L(B)\le\max_h[c(h)+L(B_{a,h})]\).
3. At each nonsuccessful finite-value belief, a selected lawful action has
   finite children and \(\max_h[c(h)+L(B_{a,h})]\le L(B)\).
4. A nonnegative integer rank decreases strictly along every selected outcome,
   and successful beliefs have rank 0.

These local conditions imply \(L=V\), including losing beliefs labelled
infinity. They can be checked without solving the optimization again.

**Proof.** Induction on \(n\) identifies \(V_n\) with minimum cost among
trees of height at most \(n\). Any successful finite tree containing the
same belief twice on a branch can replace the earlier subtree by the later
one. The later subtree is valid from the identical origin/current belief;
all removed costs are nonnegative, so no original source's cost increases.
Repeated deletion terminates and leaves no repeated belief on a branch.
Thus a successful tree can be chosen of height at most \(N\). There are
finitely many labelled trees of bounded height, so a finite minimum is
attained and rational, proving \(V_N=V\).

For certificate soundness, induction on any terminating policy tree proves
\(L(B)\) at most its worst-case cost by condition 2 and the terminal
condition. This includes infinity: a belief labelled infinity cannot have a
finite terminating tree. Conditions 3–4 construct a terminating tree of cost
at most \(L(B)\), by induction on rank. Hence \(V\le L\le V\).
For completeness take optimal values. Call an action optimal if all its
children have finite value and its cost-plus-optimal-child maximum is at most
the parent's value. Form the finite goal attractor using only optimal actions.
If some finite-valued states remain outside it, choose their minimum value
\(m\), then a state of value \(m\) with a shortest optimal tree. Its root
action is optimal, so some outcome child lies outside the attractor. Its value
is at least \(m\); nonnegative cost forces that value to equal \(m\) and the
entering cost to be zero. The corresponding subtree has cost at most \(m\),
hence is optimal, but has smaller height: contradiction. The attractor thus
contains every finite-valued state and supplies decreasing ranks and one proper
positional policy. An arbitrary root-optimal tree can have suboptimal slack
branches; local optimality of all its subtrees was not assumed. \(\square\)

Nonnegative costs and exact finite models are load-bearing. In particular
the equation \(v=0+v\) at a zero-cost nonidentifying loop permits the false
fixed point \(v=0\). The rank condition rejects it. These are proper
terminating policies, not infinite probing declared successful at no cost.
State-cap exhaustion is `UNKNOWN`, never a losing proof.

## 5. Hereditary feasibility and the exact advice/cost frontier

Let \(\mathcal F_C(y)\) be the nonempty subsets of \(q^{-1}(y)\) whose
initial beliefs \(\{(x,i(x)):x\in S\}\) can be identified with cost at
most \(C\). This is a hereditary family: restricting a successful policy
to fewer possible originals keeps every selected probe lawful, removes
possible outcomes, preserves terminal correctness and cannot increase its
worst-case cost. Every singleton is feasible at cost zero.

Let \(\mathcal H_C(y)\) consist of the inclusion-minimal infeasible
subsets. A weak hypergraph coloring assigns colors to original sources with
no hyperedge monochromatic. Denote its chromatic number by \(\chi\),
with \(\chi=1\) for an empty hyperedge family on a nonempty vertex set.

**Finite hereditary-family lemma.** For any hereditary nonempty-subset family
containing all singletons, a set is feasible iff it contains no minimal
infeasible subset. The minimum number of feasible blocks partitioning its
vertex set is the weak chromatic number of the minimal-infeasible hypergraph.

**Proof.** An infeasible finite set has an inclusion-minimal infeasible subset.
Conversely a feasible set cannot contain an infeasible subset by heredity.
A coloring's color classes are exactly a partition into sets containing no
monochromatic forbidden subset, hence exactly feasible blocks. \(\square\)

**Theorem P (PROVED LOCAL specialization; priority UNVERIFIED).** Suppose a
label \(\alpha(x)\) is **already retained before probing** and \(q(x)\)
is known. The smallest common alphabet for this prior advice which allows
cost-\(C\) identification is

\[
 K_{\rm prior}(C)=\max_y\chi(\mathcal H_C(y)),\qquad
 b_{\rm prior}(C)=\lceil\log_2 K_{\rm prior}(C)\rceil.
\]

**Proof.** On observing \((y,k)\), the observer must handle every original
in that joint fiber. It is feasible exactly when that color class lies in
\(\mathcal F_C(y)\). Apply the lemma separately on each \(q\)-fiber.
Colors can be reused between fibers, giving the maximum rather than sum.
For the upper bound, use a successful policy for each colored block. For the
lower bound, any working advice code supplies precisely such a coloring.
Binary encoding gives the final equality. \(\square\)

Initial advice is allowed to split *inside* a repair class; it is any licensed
already-known source statistic. The theorem does not create it for free.
This Pareto frontier concerns **prior advice versus paid acquisition**.
The final autonomous repair still requires Theorem M's storage, and neither
the transcript nor controller workspace is counted in the prior advice.
If one requires a single hard memory cap throughout acquisition and future
operation, that is a separate finite-controller synthesis problem.

Only finitely many budget thresholds matter: the finite values \(V(S)\)
of all initial subsets, plus zero. Enumerating these, computing minimal bad
sets and enumerating partitions gives the exact finite Pareto frontier. This
is potentially exponential; no polynomial complexity claim is made.

The same hereditary-family lemma also explains the games lane's probe
augmentation theorem. With a **fixed menu of truthful nondestructive probes**,
a selected bundle must split every minimal bad hyperedge; minimum additive
bundle cost is a weighted hitting-set problem. This is a different choice
space and cost model from arbitrary prior advice plus adaptive destructive
acquisition. The common lemma does not identify their policies or costs.

## 6. A sharp destructive obstruction invisible to every pair

There are three originals \(x,y,z\), initially reporting the same \(q\),
with distinct target labels. Two unit-cost probes behave as follows:

| Original/current | probe a | probe b |
|---|---|---|
| x | receipt alone, stays x | receipt merged, goes to v |
| y | receipt merged, goes to u | receipt merged, goes to v |
| z | receipt merged, goes to u | receipt alone, stays z |

At carriers \(u,v\), every probe emits the same receipt and stays put at
zero cost. The immutable original coordinate is not forgotten by the model.

Every pair is identifiable at cost 1: use a for \(\{x,y\}\), b for
\(\{y,z\}\), and either for \(\{x,z\}\). But from all three,
choosing a has a branch irreversibly merging y and z, and choosing b has a
branch irreversibly merging x and y. No later probe distinguishes either
merged original pair. Every first action therefore has a losing branch:
the full set has value infinity. This is a complete impossibility proof,
not a finite-horizon failure to find a strategy.

At budget 1 the unique minimal bad set is \(\{x,y,z\}\). Its pairwise
conflict graph is empty, yet its weak hypergraph chromatic number is 2.
Hence one prior bit is necessary and sufficient for unit-cost identification.
Without probing, three prior labels (two bits) are necessary. Add a truthful
nondestructive `reveal` probe of cost 2 at x,y,z, emitting their distinct
identities. The exact nondominated pairs are

\[
 (b_{\rm prior},C)=(2,0),\ (1,1),\ (0,2).
\]

The construction refutes the claim that all pairwise minimum distinguishing
costs determine joint acquisition feasibility. A current-carrier-only goal
would incorrectly declare the merged u or v branch resolved; the original
target formulation rules out this deletion of the task.

## 7. Prior art and novelty tax

* Moore/Nerode minimization and Rutten's coalgebraic quotient theory already
  contain Theorem R. See the primary references and detailed comparison in
  [the preceding report](../2026-10-18/FUTURE_SAFE_FORGETTING.md). Theorem M is
  finite injective coding with known side information, not a new information
  theorem.
* G\"uni\c cen, Jourdan and Yenig\"un, *Using Multiple Adaptive Distinguishing
  Sequences for Checking Sequence Generation*, primary author copy
  [PDF](https://www.site.uottawa.ca/~gvj/papers/C52.pdf), §§1–2, uses adaptive
  decision trees and notes nonexistence in some deterministic machines. Our
  destructive example is an active-identification obstruction, not the first
  discovery that adaptive distinguishing sequences may fail to exist.
* Hierons and T\"urker, *Incomplete Distinguishing Sequences for Finite State
  Machines*, *The Computer Journal* 58 (2015), 3089–3113,
  [primary institutional record](https://bura.brunel.ac.uk/handle/2438/11127),
  DOI `10.1093/comjnl/bxv041`, studies subsets admitting distinguishing
  sequences and smallest collections covering all states. This is close
  prior art to our feasible-block covering/coloring formulation. The primary
  abstract was inspected; its PDF endpoint returned an unsupported content
  type, so no full-paper priority clearance is claimed.
* Witsenhausen, *The zero-error side information problem and chromatic
  numbers*, *IEEE Trans. Information Theory* 22 (1976), 592–593,
  [publisher record](https://ieeexplore.ieee.org/document/1055607/), is the
  classical zero-error/coloring comparison. The source metadata was verified;
  no full-text re-audit is claimed. Our cost-feasibility hyperedges can have
  size three even with no forbidden pairs, so replacing them with a static
  pair-confusability graph is unsound for this acquisition contract.

The demonstrated contribution is an explicit source/task distinction, exact
rational cost and termination certificates, and a single finite interface
connecting autonomous repair to acquisition obstructions. It is not presently
an established new academic theorem beyond the cited theories. The closest
unresolved literature question is whether the precise budget-parametrized
minimal-infeasible hypergraph characterization has already been stated for
partial destructive diagnosis with arbitrary retained advice.

## 8. Validation, certificates and claim ledger

Before development, the 18 PR179 `test_future_safe_quotient.py` tests passed.
The new `test_information_repair.py` has 10 passing tests: 160 fresh four-state
models against exhaustive partition enumeration and shorter-code searches;
90 fresh two-origin probe systems against independent stationary-policy
enumeration simulating every fixed original source; exact three-way and
frontier controls; and float, cap, false value and zero-cycle rank mutations.
Seeds are `202610194307` and `202610196109`. These checks exercise finite
implementations; the universal finite-model conclusions rely on the proofs.

`INFORMATION_REPAIR_CERTIFICATE.json` contains the complete cost-2-reveal
fixture and exact policy/value/rank certificate on 13 beliefs, including all
seven nonempty original subsets. Rationals are numerator/denominator pairs;
`null` value means infinity. Reproduction:

```sh
python -m unittest discover -s tests -p 'test_information_repair.py'
python -m unittest discover -s tests -p 'test_future_safe_quotient.py'
```

| Claim | Status and scope | Next verdict-changing probe |
|---|---|---|
| R/M stable repair and exact auxiliary alphabet | CLASSICAL, full finite deterministic contract | Omit q from future outputs; three-state countermodel must fail |
| A exact proper acquisition value and rank checker | PROVED LOCAL, classical finite decision trees | Independent implementation with adversarial zero-cost cycles and state-dependent prices |
| P budget-feasibility hypergraph/advice equality | PROVED LOCAL specialization, priority UNVERIFIED | Full comparison with incomplete adaptive-distinguishing-sequence literature |
| Every pair identifiable implies joint identifiable | REFUTED | Three-original destructive fixture |
| Label encoding supplies an acquisition instrument | Not entailed | Supply lawful probe table and run original-class acquisition synthesis |
| Original-class diagnosis restores future source dynamics | Not entailed | Prove a postprobe-to-original simulation/restoration bridge |

The next mathematical extension should impose a total controller-memory cap
or a restoration/simulation requirement. Both alter the feasible family; they
cannot be folded into the present bit count without another theorem.
