# EODCS III — Set-valued source transport and optimal modal envelopes

**Date:** 2026-10-13. **Stack:** draft PR #47 above PR #46 at initial head 00bc0d44cb011b1d333aa0fa8549d6b402662317. Source contracts are complete explicitly declared finite tables, typed epochs, old/new reports and nonempty successor relations. These are mathematical simulators, NOT authenticated physical sources, quantum claims, stochastic probability distributions, original scholarly mathematical discoveries or an RH/Weil positivity result.

## RC1. Source can have multiple lawful successors (classical source semantics)

For states S and T, a serial source relation R is a map S to nonempty subsets of T. Old and new observations are q:S→O and r:T→P. Its observable successor support is

K_R(s) = { r(t) : t∈R(s) } ⊆ P.

A support is a SET of mathematical possibilities, not one selected outcome or a probability law. Replacing R with an unobserved determinized branch would rewrite the source.

## RC2. Exact set-valued observation transport criterion (classical; Lean kernel verified)

A lawful set-valued observer successor V:O→powerset(P) satisfies V(q(s))=K_R(s) for every s. With q surjective onto O=im(q), V exists **if and only if**

for all s,t∈S, q(s)=q(t) implies K_R(s)=K_R(t).

Necessity follows because V is a function on the current report. Sufficiency chooses any representative s_o of each report and defines V(o)=K_R(s_o); the condition ensures choice independence. V is unique on im(q). A state pair with the same original report and different successor supports is a finite negative witness, not a success.

**Machine-checked:** formal/EODCS_RelationalChoice.lean verifies the iff as equality of predicates on P. The same Lean file constructs the canonical augmented report (q(s),K_R(s)), with its universal factorization property: any alternative report sufficient to decode both q and K must also decode their ordered pair. Neither theorem constructs an actual physical sensor.

If each source transition is inhabited and all its allowed successor states have the same *new observable report*, K_R(s) is a singleton. That permits a deterministic OBSERVED report even if the hidden original source remains nondeterministic. Lean verifies the singleton result.

## RC3. Sharp modal abstraction from transport obstruction (classical; Lean kernel verified)

For each original observed report o define its hidden source fiber S_o={s:q(s)=o}. The tight envelopes are

MAY(o) = union of K_R(s) over all s∈S_o,
COMMON(o) = intersection of K_R(s) over all s∈S_o.

For every hidden s in S_o, COMMON(o) ⊆ K_R(s) ⊆ MAY(o). MAY is the *least sound overapproximation* of every support in that fiber. COMMON is the *greatest sound underapproximation*. They are source-relative bound objects, not the precise outcome set for every hidden state.

**Exactness theorem:** MAY(o)=COMMON(o) for every realized report o **if and only if** the whole successor-support law descends through q. Proof: if each K_R(s) is the same in a fiber, its union and intersection coincide; conversely each support squeezed between equal bounds must equal them. The two envelope optimality theorems and this exactness equivalence passed the pinned Lean 4.14 kernel in the EODCS workflow.

**Witness:** S={s0,s1} with q(s0)=q(s1)=0; T={u0,u1} with r(u0)=cold, r(u1)=warm. Source R(s0)={u0}, R(s1)={u1} yields MAY(0)={cold,warm} and COMMON(0)=empty. No exact observed successor support exists. MAY is a sound upper bound; asserting MAY equals both actual hidden supports is false. COMMON empty does NOT imply an impossible transition.

**Positive nuance:** if R(s0)=R(s1)={u0,u1}, MAY=COMMON={cold,warm}. The set-valued update descends, but the next observed report is NOT deterministic; neither cold nor warm is guaranteed to occur. “Common possible” means possible from every hidden source state, never necessary occurrence under every successor transition.

## RC4. Three-valued safety claims from MAY (classical; conditional)

Given any target-report property G⊆P and a known old report o:
- If MAY(o)⊆G, G is guaranteed within the complete *declared* transition relation.
- If MAY(o) and G are disjoint, G is impossible within that declared source relation.
- Otherwise the available source model leaves the property undecided.

These are universal/existential possibility judgments. No probability, confidence, statistical calibration, causal reset or physical prediction is inferred.

## RC5. Probability identification is genuinely missing (exact counterexample)

Two hidden source states share current report 0 and both have K={cold,warm}. One declares normalized transition probabilities (1/4,3/4), the other (3/4,1/4). Their observable possibility laws match exactly but their observed probability laws differ. Therefore source-conditional probability CANNOT be inferred from a possible-outcome set alone. The missing probability kernel is separate from the missing joint coupling among known marginals studied in GF/HS. No posterior truth probability is claimed.

## RC6. Lawful relational composition (classical, exact)

For an R:S→powerset(T) followed by Q:T→powerset(W), (Q∘R)(s)=union_{t∈R(s)} Q(t). The finite implementation composes those relations only across matching source ID, versioned intermediate state chart and basis. A multivalued intermediate process can produce a deterministic terminal OBSERVABLE without implying deterministic hidden evolution. It never multiplies cardinalities into probabilities.

## RC7. Falsifiers and reproducibility

- 343 full 3-state serial relation tables checked against independent enumeration of every possible output-support map V on the two old report classes.
- Another 2058 relation/report source cases checked against independently computed exact unions and intersections, including equality-of-envelopes iff source support transport and all three safety verdicts.
- 200 seeded two-step relational source-composition examples checked against direct intermediate-path union semantics.
- Three-state observational refinement partitions checked against the universal minimality of the paired-report representation.
- Mutations: empty source-successor set, missing source, wrong epoch/basis, inconsistent or unnormalized positive rational likelihood, impossible target property, false empirical attestation, incomplete source coverage.
- The reproducible script is scripts/eodcs_relational_probe.py. Commit a frozen exact receipt only after actual execution and version-checked replay, never from a guessed number.
- The Lean kernel formally certifies the abstract transport, universal repair, and modal order-theoretic theorems; it does not verify every Python implementation branch, external empirical source, probability density or RH.

## RC8. Next verdict-changing probes and walls

(1) Stochastic source change: law-valued Markov kernels, original-source interventions and history-dependent noise; distinguish source-relative Bayes transport from mere support transport. (2) Source reports with missing possible outcomes or destructive interventions: track coverage and reset/access separately rather than assuming complete possibility sets. (3) Finite modal bisimulation depth: one-step identical envelopes can conceal longer action-word distinctions. (4) Fully formalize finite cardinal Nerode bounds and nonabelian graph-cover minimal-degree theorem in Lean. (5) Test truly new mathematical representation constructors on tasks independent of the developer's grammar.

**Verdict:** This is a precise finite demonstration that E can repair a failed function-valued explanation using a relational abstraction with independently provable optimal information bounds. Its mathematical constituents are classical; academic priority, physical experiment and RH implications are UNVERIFIED.
