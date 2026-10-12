# Carrier-relative meta-SUCC: checkpoints, distributed dovetailing, policy order and provable knowledge boundaries

**Date:** 2026-10-12. **Branch:** `research/carrier-relative-identifiability-realization-2026-10-12` stacked on Shadow-SUCC PR #35 at `65f79f306770085b74dcc2cf101d910c592316f9`.

**Origin:** The maintainer asks whether, at finite checkpoints, E can dispatch finite automata that grow many E-towers and enumerate possible orders of observation, logical inference and model update, while retaining a single original carrier and avoiding hidden-source overclaims. This follows the earlier insight that one can establish carrier-relative lower bounds without deducing ultimate 'inside/outside' ontology.

**Epistemic contract:** Below are precise classical theorems, finite model witnesses and honest resource boundaries. No source-id, trusted-message label, transition table, or simulator audit is empirical authentication. No actual infinite execution, physical cloning, quantum entanglement, novel RH proof, new theorem-priority claim or completed Weil-form identification follows. The new work is a reusable SUCC exact-certificate interface, not a replacement for established proof theory or active automata learning.

## CT1. An E meta-tower is a double-indexed *finite* process (CLASSICAL)

Let \(X\) be a declared original-source class, \(C\) its mutable carrier, and let \(A\) be the finite set of executable actions. A source-changing instrument has type

\[
 a:C\rightharpoonup O_a\times C,\qquad c\mapsto(o_a(c),\delta_a(c)).
\]

Original claims \(t:X\to Y\) are evaluated at the original source, not silently reinterpreted on the modified current carrier. E's checkpoint \(n\) has an immutable receipt set \(E_n\) and a finite ordered list of program/proof-search tasks \(W_n\). A fair task policy eventually considers every *finite* program and proof permitted by its recursively enumerable language. For example, with \(b\) primitive actions, the full length-bounded list is

\[
 W_n=\bigcup_{j=0}^{n}A^j,\quad |W_n|=\sum_{j=0}^{n}b^j.
\]

At every finite checkpoint, this list, all receipt queues, and the number of generated towers are **finite**. The ideal limit \(\bigcup_nW_n=A^*\) is a mathematical union, not a supertask completed in finite physical time. The network must pay for exponentially growing work, storage, communication and original-state preparations.

**Finite automaton firewall.** A strictly autonomous deterministic controller with finitely many internal states and no external tape/input eventually revisits a state, after which its output word is periodic. Therefore it cannot issue an unbounded stream of pairwise novel complete finite program descriptions with no external memory. A *finite control program* coordinating arbitrarily expandable towers/tape is different: the collective system has unbounded memory as \(n\to\infty\). The tested `FiniteController` returns an exact prefix/cycle certificate rather than pretending its own internal machine state grew.

## CT2. Fair checkpoint proof discovery, not automatic truth discovery (CLASSICAL / PROVED LOCAL)

Fix a finitary, sound, effectively decidable proof checker for theory \(T\). Assume evidence sets \(E_0\subseteq E_1\subseteq\dots\) and an effective, fair dovetail enumeration of all finite proof strings together with all finitely used evidence premises, after those premises arrive. Then

\[
 \boxed{T\cup\bigcup_nE_n\vdash\varphi\ \Longleftrightarrow\
 \text{a sound finite proof of }\varphi\text{ is accepted at some finite checkpoint}.}
 \tag{CT2}
\]

**Proof:** If accepted, the checker has validated all finite inferential links, source premises and rules, so the displayed syntactic derivability holds. Conversely a finite derivation has a maximum evidence arrival checkpoint and a finite code. Fairness eventually schedules it and the checker accepts. The theorem is about derivability, not standard-model truth or real sensor authenticity. In a merely recursively enumerable theory, fair proof enumeration semidecides positive instances, not arbitrary absence of proof. No inference of \(\omega\)-rule/reflection/Con(T) from elapsed time occurs.

## CT3. Every finite proof arises at a finite observation stage (CLASSICAL)

For a fixed finitary calculus and increasing evidence, deductive closure commutes with directed increasing unions:

\[
 \boxed{\operatorname{Cn}_T\bigl(\bigcup_nE_n\bigr)
 =\bigcup_n\operatorname{Cn}_T(E_n).}\tag{CT3}
\]

The \(\subseteq\) direction follows because every proof needs only finitely many evidence premises; select their maximum arrival stage. The other direction follows by monotonicity. A logically new theorem cannot appear *only* at stage \(\omega\) if it has an ordinary finitary proof from the increasing union. Conversely, having every numerical instance \(P(n)\) in the union does not by itself authorize \(\forall nP(n)\); this requires an additional justified proof principle.

**SUCC consequence:** E's final one-step epistemic assimilation can absorb an arbitrarily deep **finite** proof certificate once it arrives, but the certificate had to be physically transmitted or mathematically constructed, and its rule authority remains independently sourced.

## CT4. Reasoning-order confluence has a precise logical scope (CLASSICAL / PROVED LOCAL)

For a finite set of positive ground Horn implications \(P_1\wedge\cdots\wedge P_k\Rightarrow Q\), define the inflationary immediate consequence map

\[
 \Phi(U)=U\cup\{Q: (P_1,\ldots,P_k\Rightarrow Q)\in R,\ \{P_i\}\subseteq U\}.
\]

Every fair ordering of rule applications stabilizes at the same least fixed point \(\mu\Phi\), after at most the number of attainable distinct atoms many strict additions. **Proof:** Soundness under a declared truth interpretation is preserved by each rule, if each axiom is true and all rule implications are true. Every reachable application is contained in \(\mu\Phi\) by induction. Fairness prevents stopping with an applicable conclusion missing, so any terminal result is a fixed point containing the premises; by leastness it equals \(\mu\Phi\).

`HornTheory` produces individually replayable inference witnesses, exhausts all rule permutations for small rulesets, and `finite_source_soundness` gives an **independent truth-table counterexample** if a declared axiom or rule is false on any admitted model. A syntactically correct derivation alone is not proof that its starting interpretation is the actual carrier.

**Nonmonotone falsifier:** Defaults *A if B not known* and *B if A not known* yield different extensions under opposite order. One cannot union the two branches and proclaim both true. E must track the branch's assumptions, order, source version, and compatibility; merely enumerating all orders detects the ambiguity, it does not settle it.

## CT5. Adaptive executable policy is an AND/OR fixed point, not a list of words (CLASSICAL / PROVED LOCAL)

For a known finite source/current-carrier model let \(B\subseteq X\times C\) be a nonempty belief. Let \(G(B)\) hold iff the original-target labels \(\{t(x):(x,c)\in B\}\) are a singleton. Let \(B_{a,o}\) be the legal successor under actual observation \(o\). Define

\[
 W_0=\{B:G(B)\},\quad
 W_{k+1}=W_k\cup\{B: \exists\text{ executable }a\;\forall\text{ possible }o,\ B_{a,o}\in W_k\}.
 \tag{CT5}
\]

**Claim:** The root belongs to \(W_k\) iff there is a *uniform* deterministic, outcome-adaptive policy deciding the ORIGINAL target in worst-case at most \(k\) actions. Induct on \(k\); the nonterminal root must choose one executable action, and every resulting public outcome must carry a winning continuation of depth \(k-1\). Finiteness of reachable beliefs makes the least fixed point decidable; failure to enter it is a **model-relative full no-policy certificate**, not an unbounded empirical proof about unknown reality.

`proof_policy_checkpoint` enumerates all preset words up to length \(k\) and independently constructs/validates one adaptive AND/OR proof tree. Its rank is independently cross-checked against `ControlledCarrier.adaptive_original_claim`, including an exhaustive **256** two-state/two-action machine check.

**Strict adaptive advantage:** In a four-state two-bit source, action Q reports a and reversibly transforms current b to original parity. The next action must be selected from R0 or R1 based on Q's observed a; two steps solve original parity. Every fixed two-action word fails. Conversely, when READ_A destroys b and READ_B destroys a on a single physical source, every pair of original states has *some* distinguishing experiment, but **no** adaptive policy resolves original parity. Enumerating all orders cannot undo lost original-state information.

## CT6. Model branching is not physical branching (PROVED NEGATIVE)

From a single current carrier \(c\), two mutually exclusive first actions \(a\neq b\) cannot BOTH be performed as the first transition of the same event history. A symbolic meta-observer may explore their counterfactual branches using the stipulated full transition table. That is mathematical *simulation*, not source-authenticated measurement of both alternatives.

A physical execution network requires separate source-preparation tokens or a verified lawful reset preserving the target's original state; any such operation has resource and provenance obligations. `certify_parallel_roots` rejects reuse of a single preparation lease across rival first-action histories and rejects mismatched carrier IDs. The function does **not** certify two purported copies really began in the identical hidden original state, and it does not evade quantum no-cloning constraints.

## CT7. Meta-towers do not penetrate observational equivalence (CLASSICAL / NO-GO)

Suppose source hypotheses \(x,y\) induce the SAME probability distribution of PUBLIC outcomes for every admissible action at every common prior public history, including the dynamics of every lawful source-changing instrument. Let a meta-controller choose its next action, spawn request, proof-order task and final report using only public histories and independently randomized coins. Then the full distribution of its public meta-history is the same under \(x,y\).

**Proof:** Induct on checkpoint depth. The controller's action distribution is the same under a common public history, and by hypothesis each next source-output distribution is the same. Hence the extended joint law agrees; deterministic proof search and message relays are postprocessing and cannot introduce a new distinction. If an original-source claim \(t(x)\ne t(y)\), no sound observation-only meta-policy can decide it for both with zero error. This assumes the expanded tower possesses no new physical probe independent of the declared observation family. Distinguishable new instrumentation changes the theorem's premise and may break the alias.

`ontology_alias_model` gives a finite `inside`/`outside` pair whose available probes all return `same`; adding a previously unavailable source-separating instrument makes them distinguishable in one step. This is a precise condition on accessibility, not a metaphysical claim about what is ultimately outside the universe.

## CT8. Statistical certainty is different from asymptotic identification (CLASSICAL)

For two declared hypotheses with public outcome distributions \(P,Q\) and equal priors, the minimum single-shot classification error is

\[
 \boxed{R^*=\tfrac12(1-\|P-Q\|_{TV}).}\tag{CT8}
\]

It is zero iff their supports are disjoint. Under n independent copies of the SAME nontrivial experiment, strict-positive shared support makes the finite-n optimal error positive even if it tends to zero asymptotically. If \(P=Q\) then all iid repetition laws coincide and the error remains 1/2. Adding postprocessing/observer-tower relays cannot improve total variation. Tests use exact rational laws such as Bernoulli 3/4 versus 1/4, and finite nonanticipating stochastic controlled histories.

## CT9. Compactness can force a finite observer family (CLASSICAL / EXACT SOURCE ASSUMPTIONS)

Let \(X\) be compact Hausdorff; let \(t:X\to Y\) be CONTINUOUS with \(Y\) finite discrete; and let \(\mathcal P\) be a family of CONTINUOUS finite-valued tests. Assume for every \(x,y\in X\) with \(t(x)\ne t(y)\), there is a test \(p\in\mathcal P\) with \(p(x)\ne p(y)\). Then some **finite** subfamily \(p_1,\ldots,p_m\) jointly determines the target on all X.

**Proof:** The cross-target locus \(D=\{(x,y):t(x)\ne t(y)\}\) is closed in compact \(X^2\), hence compact. Every test's separation set \(D_p=\{(x,y):p(x)\ne p(y)\}\) is open, by continuity to discrete values. The sets \(D_p\) cover D by hypothesis. Compactness gives a finite subcover. Therefore if those finitely many reports agree at x,y, target values agree. This is topological **static** observation; it does not grant simultaneous execution of destructive instruments.

**Failure control:** \(X=\{0\}\cup\{1/n:n\ge1\}\) is compact. Tests detecting each isolated point \(1/n\) are continuous, but the target \(t(0)=0, t(1/n)=1\) is NOT continuous at 0. Every rival is eventually distinguishable from 0, yet no finite selected tests certify the source to be 0. The existing `DelayedSeparatingTower` is an exact finite simulator of this missing-target-regularity phenomenon.

## CT10. Observable structure can give lower bounds without ontology (CLASSICAL / EXACT)

For an autonomous linear realization \(y_n=c^TA^nb\) of dimension d, its Hankel block \(H_{ij}=y_{i+j}\) factors as \(H=\mathcal O\mathcal R\) with d columns/rows in the middle. Hence **every** Hankel minor of order d+1 vanishes. A nonzero exact r-by-r minor therefore certifies d>=r. For \(y_n=1+(-1)^n\), H_2=diag(2,2), giving d>=2. These are CLASS-RELATIVE truths, not proof that the actual carrier follows LTI dynamics.

For any horizon h, the delayed pulse sequence \(y_n=\mathbf1_{n=h}\) has a nilpotent shift realization of dimension h+1 and an antidiagonal Hankel minor certifying the same lower bound. Its first h observations are zero. Thus no finite all-zero prefix proves a universal small carrier dimension without a justified horizon/model-class condition.

## CT11. Four separate epistemic verdicts

At a declared checkpoint, a checker must distinguish:

1. **PROVED_FROM_TRUSTED_EVIDENCE** — a finite proof uses correct source/basis labels, verified rule applications, and actual accepted evidence, all under explicit attestation assumptions.
2. **NO_POLICY_WITHIN_DEPTH** — an exhaustive, finite, per-depth negative result; a deeper or different-source instrument might succeed.
3. **MODEL_CERTIFIED_NO_FINITE_POLICY** — the root lies outside the least winning fixed point for a COMPLETE *known finite carrier model*; no conclusion about unknown external models.
4. **UNRESOLVED_RESOURCE_OR_SOURCE_CLASS** — a finite memory/time/probe budget or missing source attestation blocks the checker; never silently report philosophical impossibility.

**Ontological darkness** is a separate positive negative witness: a pair of source models with different target labels and identical observation laws under every permitted policy. The checker may certify that fact only relative to the stated instrument class.

## CT12. The actual research frontier is source-aware program growth

The meta-observer can indeed enumerate **all finite logical orderings** within a fixed effective calculus. It can enumerate all finite fixed action words and all finite adaptive policy trees in a fully declared finite model. But it cannot convert those representations into real causal experiments without independently justified execution resources. Nor can it infer the truth of all arithmetic propositions: computably enumerable proofs are not a decision procedure for arbitrary unprovability/nonhalting and cannot bypass incompleteness.

For RH, the correct task type is to grow test-function domains, provenance-valid prime/Euler/Gamma readings, analytic continuation/zero-free estimates and source-specific positivity certificates. If a finite checked RH proof is derivable from sound axioms and is fairly enumerated, the network eventually finds it. That tautologically does NOT supply a reason such a proof exists or prevent fake-polarization evidence from being mistakenly accepted if source rules are unsound. **The meaningful research upgrade is an audited, progressively widening source-and-proof category**, with exact resource and model-assumption labels.

## Numerical reproducibility and hostile checks

- `carrier_observational_frontier.py`: exact deterministic Mealy trace equivalence, minimal behavioral quotient, pair separator vs original adaptive target, ontology alias controls.
- `carrier_shadow_fibers.py`: exact source-fiber target descent, minimal nondestructive test suites, infinitely delayed rival witness.
- `carrier_hankel_bounds.py`: exact rational Hankel rank/minor and delayed-impulse source-complexity lower bound.
- `carrier_statistical_limit.py`: total variation, zero-error, finite iid risk and finite-horizon internal simulator equivalence.
- `checkpoint_meta_tower.py`: checkpoint evidence ledger, positive Horn proof receipts and order audit, independent truth-table audit, fixed-word dovetail, adaptive AND/OR policy trees, physical branching leases, finite-controller periodicity and nonmonotone defaults.
- Test modules independently exercise semantically bad rules, false basis/version, public-history source alias, resource exhaustion, physical branching misuse, signed original target, and exhaustive 256 two-state two-action automata. Every test is on a **mathematical model**, not a measurement of the real universe.

## Background / prior art

These are established mathematical ideas reorganized for SUCC. Related primary directions include Mealy-machine equivalence/minimization, Ho–Kalman realization theory, compactness of continuous maps into discrete finite targets, Gács–Körner common information, finite-ground Horn closure and monotone inductive definitions, dovetail proof enumeration, automata active learning and adaptive distinguishing sequences. For active distinguishing sequences and the necessity of a reset/symbol-query contract, see:

- Frohme, *Active Automata Learning with Adaptive Distinguishing Sequences* (2019), https://arxiv.org/abs/1902.01139.
- Vaandrager et al., *A New Approach for Active Automata Learning Based on Apartness* (2021), https://arxiv.org/abs/2107.05419.
- Hierons et al., *Using adaptive distinguishing sequences in checking sequence constructions* (2008), https://doi.org/10.1145/1363686.1363850.

No claim of a new classical decidability result, experimentally attested fundamental carrier, physical supertask or RH proof is made. **Potential new academic results** would require a source-derived nontrivial invariant or resource lower bound surviving comparison with these existing theories, or a new independently checked arithmetic lemma such as Weil-form positivity.
