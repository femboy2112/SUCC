# Operational Yoneda and Source-Relative Proof-Policy Descent

**2026-10-11 | Draft research branch:** research/operational-yoneda-policy-descent-2026-10-11, stacked on PR #21 head \`1c1a83d5194f0541fd85e77d3f90bd2fec376e8e\`.

**Origin:** maintainer asks for Yoneda to become load-bearing in SUCC after exact source-relative precision transport (PR #19), proof-support/Zeno debt (PR #20) and noncommuting causal histories plus adaptive proof planning (PR #21).

**Verdict and priority:** This round constructs a genuinely composable finite **category of source-labeled legal observation histories**, checks actual Yoneda natural transformations, proves an exact restricted-context **arrow-separation criterion**, and independently proves a **source- and target-preserving coalgebra morphism theorem** transporting optimal finite winning proof policies. The mathematics is CLASSICAL/PROVED LOCAL with reproducible finite examples and adversarial oracles; combining these interfaces in SUCC is an architectural and mathematical research synthesis, **not an academic-priority claim**. No physical observer, empirical source authentication, quantum dynamics, infinitely executable procedure, adelic Gamma completion or RH proof follows.

## 1. The objects; why ordinary category theory and observation reach are DIFFERENT

A source-dependent finite experimental field is a total finite state set \(S\) and named PARTIALLY EXECUTABLE deterministic instruments

\[
a:S\rightharpoonup O_a\times S,\quad
q\mapsto \left(o_a(q),\,\delta_a(q)\right).
\]

Actual historical records are public action names, outcomes and ordered epochs. A separate simulator audit contains actual hidden carrier states, **not** supplied to the deciding agent. An original-source claim \(t:X\to Y\), \(X\subseteq S\), is evaluated at the original source \(s\), not at a modified post-measurement carrier \(q\).

An observer belief is an exact compatible possibility class

\[
B\subseteq X\times S,\qquad (s,q)=
(\text{original source},\text{current carrier}).
\]

The initial belief is \(B_0=\{(s,s):s\in X\}\). The named instrument a is admissible at B iff it is enabled at **every** q occurring in B. Given a public observation o,

\[
\boxed{B_{a,o}=\{(s,\delta_a(q)):(s,q)\in B,\quad o_a(q)=o\}.}
\tag{Y1}
\]

The target is established on a belief precisely when \(\{t(s):(s,q)\in B\}\) is a singleton. Otherwise no legitimate source-claim conclusion may be manufactured by using hidden simulator truth.

**Probe menus matter:** in this model enabled-action menus are NOT an extra unrecorded sensor. A separate earlier model treated offered menus as public and gave a different bisimulation notion. Equating these two tool closures without an explicit extra observation violates the source contract.

## 2. An ACTUAL Yoneda category of legal histories

Fix a belief-game and nonnegative budget h. Define a small category \(\mathcal C_h\) by:

- **Objects:** distinct reachable contexts \((n,B)\) with \(0\le n\le h\), where n is the remaining step budget and B is a lawfully source-derived belief from the selected original source class.
- **Generating arrows:** \((n,B)\xrightarrow{(a,o)}(n-1,B_{a,o})\) for every admissible action and every possible reported outcome, when \(n>0\).
- **General arrows:** entire ordered words of such actual lawful action/outcome edges, retaining different paths even if their context endpoints agree. Identity is the empty word. Composition is path concatenation.

Budget decreases strictly along every nonidentity arrow, so \(\mathcal C_h\) is a finite free path category, not an arbitrary list of reports or a physical realization of a supertask. The implementation verifies type/endpoints, identity, concatenation and associativity, rejects fabricated paths and raises on exhausted enumerative budgets. Keeping the original source/claim context fixed within a category is a premise.

For \(c\in\mathcal C_h\), use the **genuine** representable presheaf

\[
y(c)=\mathcal C_h(-,c)
\]

whose arguments are PRECURSOR context objects and whose values are lawful full history morphisms into c. The classical Yoneda lemma gives

\[
\boxed{\operatorname{Nat}(y(a),y(b))\cong\operatorname{Hom}_{\mathcal C_h}(a,b).}
\tag{Y2}
\]

The code reuses the existing SUCC implementation of literal finite natural transformations, including naturality checks; **this is a verified instance of an existing theorem**, not a novel Yoneda proof. Background: Tom Leinster, *Basic Category Theory*, Cor. 4.3.7, [author-hosted text](https://people.math.rochester.edu/faculty/doug/otherpapers/leinster-book2.pdf).

### Restricted observer contexts and the precise failure of faithfulness

For a selected FULL observer-context subcategory \(\mathcal J\subseteq\mathcal C_h\), restrict each representable to \(\mathcal J\). For two distinct actual arrows \(f,g:a\to b\), they become equal restricted natural transformations **iff**

\[
\forall j\in\mathcal J\ \forall u:j\to a,\qquad
f\circ u=g\circ u.
\]

Consequently restricted Yoneda is **faithful on this particular hom-set** iff

\[
\boxed{
\forall f\neq g\in\mathcal C_h(a,b)\quad
\exists j\in\mathcal J,\ u\in\mathcal C_h(j,a):
f\circ u\neq g\circ u.
}
\tag{Y3}
\]

This is a rigorous probe/context availability criterion, not merely an appeal to the word Yoneda. The proof follows by evaluating each restricted natural transformation at every j and u; the full case takes \(j=a,\ u=1_a\). Note **faithfulness is not fullness**: a restricted observer family may also admit spurious natural transformations not generated by any actual path, a separate phenomenon already calibrated in SUCC's existing divisibility-category tests.

**Exact example from REAL legal histories:** one known carrier source, two actions A and B both returning the same report and same next carrier. With budget h=1, there are two distinct arrows from root to the shared final belief-context, despite identical current belief/target. Full Yoneda yields exactly two natural transformations. The restricted observer category containing only the final context sees precisely ONE transformation, collapsing the two lawfully distinct histories. The root context is the minimum one-object separating family: its identity arrow reads the difference between A and B. An enumerated finite hitting-set diagnostic identifies this minimum and reports when a context budget prevents exhaustive certification. Having a mathematical root context is **not** the same as possessing an actual physical ability to reset to it after a destructive probe.

This construction directly improves provenance adequacy \(\sigma\) without mistaking high observational indistinguishability \(\phi\) for truth or physical access.

## 3. Full finite continuation semantics: goal-labeled coalgebraic bisimulation

Fix a finite rooted observer belief game \(G\). At each reachable B retain (1) its original-source homogeneous target label \(g(B)\in Y\cup\{\bot\}\), and (2) for every currently admissible action a, the complete finite labeled outcome-transition map \(o\mapsto B_{a,o}\).

Between two games G and H, a relation \(R\) is a **target-labeled observational bisimulation** if \((B,C)\in R\) implies:

1. their terminal original-source claim labels match, including the nonterminal value \(\bot\);
2. their publicly selectable ACTION NAMES agree exactly;
3. for every action, their POSSIBLE PUBLIC OUTCOMES agree exactly and each matched-outcome successor pair again belongs to R.

The greatest such relation is obtained by starting with all equal-goal cross-game belief pairs and repeatedly deleting violating pairs. As the games are finite, pair deletion terminates; no arbitrary finite depth is mistaken for a complete source equivalence.

**Theorem (rank invariance):** If initial beliefs are related under the greatest target-labeled bisimulation, their exact least AND/OR winning sets agree stage by stage:

\[
\boxed{
B\in W_n^G \Longleftrightarrow C\in W_n^H
\qquad\forall n\ge0.
}
\tag{Y4}
\]

Thus both have the SAME minimum worst-case finite proof-completion rank, or both have no finite winning policy. Proof: induction on n. Base n=0 is equality of terminal target labels. Inductive step is equality of available actions, report branches and related successor beliefs, so the existential-action/universal-observed-outcome clause of the least fixed point is preserved in BOTH directions. The source labels behind g remain declared premises.

**Constructive policy transfer:** retain a virtual G belief while an actual H observer runs, select G's winning action, read H's lawful outcome, and update both beliefs along the matching labeled successor edges. The R invariant is maintained. When the G policy reaches a homogeneous target, H's terminal target matches and the actual H original source has that label. Every H compatible source is replayed in the tests. This is a behavioral proof transfer; without a verified source map it is NOT an assertion that physically distinct initial carriers encode the same true mathematical object.

Prior art: finite bisimulation and the preservation of fixed-point/modal semantics are classical coalgebraic theory, not a new SUCC discovery; see [Coalgebraic Semantics of Modal Logics: an Overview](https://citeseerx.ist.psu.edu/document?doi=2afd2ea4c5219d6c5fbd0c9bfc5fc2a7efe964fb&repid=rep1&type=pdf).

## 4. Source-preserving coalgebra morphism: a stronger, typed policy-descent theorem

Require a declared map \(h:S_{\rm concrete}\to S_{\rm abstract}\), source classes \(X_C,X_A\), and original-source predicates \(t_C,t_A\). We CHECK all of:

\[
h(X_C)=X_A,\qquad
t_C(s)=t_A(h(s))\ (s\in X_C);
\tag{Y5}
\]

for EACH instrument a and EVERY concrete current carrier q,

\[
\boxed{
\begin{aligned}
\mathrm{enabled}_C(a,q)&=\mathrm{enabled}_A(a,h(q)),\\
o^C_a(q)&=o^A_a(h(q))\quad\text{(when enabled)},\\
h(\delta^C_a(q))&=\delta^A_a(h(q))\quad\text{(when enabled)}.
\end{aligned}}
\tag{Y6}
\]

Action names, original-source target interpretations and declared basis/source maps must all be typed. A counterexample to ANY square rejects certification rather than trying to infer a convenient partial transport from successful tests.

**Theorem (exact policy descent/lift):** Y5–Y6 induce an ONTO homomorphism on every reachable compatible belief and every legal outcome branch:

\[
\overline h(B)=\{(h(s),h(q)):(s,q)\in B\},\quad
\overline h(B_{a,o})=\overline h(B)_{a,o}.
\tag{Y7}
\]

The initial map is onto because \(h(X_C)=X_A\). Assuming onto at B and Y6, exactly the same actions are available over both beliefs, exactly the same output labels occur, and each output fiber is mapped ONTO the abstract output fiber. Thus onto continues after every finite history by induction. Y5 ensures homogeneous ORIGINAL-target labels coincide. Y7 is a bisimulation of all reachable belief contexts, so by Y4:

\[
\boxed{
\mathrm{rank}_{C}(t_C,X_C)=
\mathrm{rank}_{A}(t_A,X_A)\in\mathbb N\cup\{\infty\}.
}
\tag{Y8}
\]

Any finite winning policy on the abstract model can be run on the concrete source using ONLY its actual public observation outcomes and a virtual abstract belief. Conversely, any concrete policy's observable behavior can be reproduced on the image abstract source because all abstract source histories are covered and their reports/claims agree. This is an exact preservation of finite *ability to prove*, not equality of hidden physical states or identical implementation costs.

**Noninjective positive:** duplicate every state of the previous conditional-original-parity SUCC carrier into two physically separate implementation labels with an unobservable hidden tag. Source map h forgets the tag (8 concrete states -> 4 abstract states); all instruments and state effects respect the quotient. Optimal rank=2 in both, despite h NOT injective and despite a reversible state-changing Q action. Replay all eight concrete original sources and compare reported original parity.

**Noninjective negative:** duplicate every state of the destructive single-carrier original-XOR problem; neither model has a winning policy. Faithful source abstraction must NOT invent a completion path when the physical instruments cannot access the original source bits.

**Mutation controls:** forged source target, unsound source-class image, wrong total state mapping, mutated response, mutated state effect, altered action availability or wrong instrument name EACH invalidates a load-bearing commuting square. The examples do not authenticate h as a law of actual physics, but they stop mathematical decoder code from silently treating a guessed map as certified.

## 5. The hostile delayed-separator model: one-step agreement is NOT proof-equivalence

Use two possible original sources s=0,1, plus two possible post-action carrier states 2,3. Both deterministic systems have exactly the same public action names and SAME outcomes for every zero- and one-step fixed experiment started at either original source.

In GOOD: action A produces no distinguishing report but transports 0 to 2 and 1 to 3; action B returns 0 on original 0,1 and separates at the post-A states, reporting 0 on 2 and 1 on 3. The source claim t(0)=0,t(1)=1 wins after word (A,B), minimum rank 2.

In BAD: the same A reports 0 but sends BOTH sources to state 2; B and all subsequent actions cannot distinguish the merged sources. There is no finite winning original-source policy.

Therefore

\[
\boxed{\text{identical all depth-1 probe responses}\quad
\not\Rightarrow\quad\text{equal finite proof capability}.}
\tag{Y9}
\]

The honest two-step test (A,B) provides an explicit source-discriminating mutation witness. The greatest goal-labeled belief bisimulation correctly rejects the root pair. Source-report agreement is a test/truncation observation, not an identification of full Yoneda representables nor a source-preserving coalgebra morphism.

**Important terminological guard:** \`shallow_probe_agreement\` tests fixed-word public response tables on the same DECLARED numerical source chart, not natural transformations of the Yoneda functor. This finite operational test is deliberately distinct from the ACTUAL representable-presheaf Yoneda construction of §2.

## 6. Claim ledger and negative routes

- **PROVED LOCAL/CLASSICAL:** Y1–Y9 within their exact finite deterministic scopes; the existing Yoneda lemma and finite goal-bisimulation proof explain correctness, while exhaustive mathematical controls calibrate the source map/program implementations.
- **TESTED MODEL:** literal small Yoneda arrow-natural-transform counts; context separator hitting set; quotient source-tag 8->4 win/loss transfer; source-history replay; independent color-partition bisimulation and existing source-policy game; delayed-separator counterexample.
- **REFUTED:** "all local one-step reports match, so any future proof will match"; "a noninjective change of source coordinates must lose all source proof capacity"; "full Yoneda for an abstract category means every embedded physical observer has all probe objects"; "a restricted observer context automatically determines all morphisms"; "a matching present belief/claim count implies equality of future instrument behavior".
- **UNVERIFIED:** true instrument tables/source map, external source authentication, experimentally measured physical world, quantum backaction/probability, nonflat REAL connection beyond small arithmetic, category of all possible mathematical theories, any p-adic/Archimedean RH source-to-Weil positivity identification.

The actual obstruction to claiming a physical/comprehensive Yoneda theorem is **adequacy of the source and admissible-probe maps**, not absence of an abstract mathematical Yoneda lemma. No finite source-class test can justify those unproved maps without independent data.

## 7. Reproducibility and next verdict-changing probe

- \`observational_succ/operational_yoneda_descent.py\`: finite actual belief-path category, exact restricted-hom faithfulness criterion, minimal context hitting sets, target-labeled cross-game greatest bisimulation, explicit policy replay, source/coalg action/effect/claim morphism, finite delayed-source mutation.
- \`tests/test_operational_yoneda_descent.py\`: at least 18 named hostile tests; all 16 predicates on original 4-state carrier; up to all 256 two-state two-instrument systems lifted through noninjective source representations; separate independent colored bisimulation oracle; genuine naturality/associativity; corrupted source ID/effects/outcome/menus/claim/table controls, resource exhaustion, finite delayed separator and genuine full/restricted Yoneda.
- \`scripts/operational_yoneda_descent_probe.py\`: machine-readable strict proof boundary receipt in CI on Python 3.10 and 3.13.

**Next:** seek SOURCE-CERTIFIED instruments in a mathematically consequential family (e.g. finite quotient of an actual arithmetic SUCC/FUCC prime-jet system) where Y5–Y6 are not stipulated but derived independently. Develop a *nonflat, path-indexed proof strategy descent* with actual budgeted instruments and noncommuting path composition. Demand that a newly derived class of strategies survives one fresh source-family holdout and an authentic-versus-mutated-prime control. Do NOT claim Yoneda by itself gives completed Weil positivity, recovers unknown RH zeros, or proves universal source truth.

**Foundational sources:** Leinster, *Basic Category Theory*, §§4.2–4.3 [author-hosted](https://people.math.rochester.edu/faculty/doug/otherpapers/leinster-book2.pdf); existing SUCC \`yoneda.py\` and \`tests/test_category.py\`; coalgebraic bisimulation semantics and modal fixed-point preservation [overview](https://citeseerx.ist.psu.edu/document?doi=2afd2ea4c5219d6c5fbd0c9bfc5fc2a7efe964fb&repid=rep1&type=pdf). These are classical authorities, not independent confirmation of claimed new academic priority.
