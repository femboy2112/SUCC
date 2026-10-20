# Carrier-relative logic, FuckedFields, and inference authority

**Research handoff — 2026-10-20. Status: proposed synthesis plus scoped classical proofs; NOT a new foundational theorem, empirical ontology, psychology result, or result on RH/ABC.**  
**Source:** maintainer's philosophical proposal in the 2026-10-20 discussion, interpreted under the SUCC steelman → crucible → verdict discipline.  
**Parent:** Academic Main V, main at 455600a2e013895c36238a3a97e0f470fd7ba197. **No mainline modification intended.**

> Every abstraction should declare what it preserves, what it forgets, and which conclusions remain valid after the forgetting.

The author's central distinction is **not that excluded middle is false**. It is that classical mathematical truth conditions, the effective ability to make an observation, the availability of a choice witness, and the authority to assert something about an original carrier have different interfaces. When the carrier is discovered from within, none of those interfaces may silently impersonate another. SUCC seeks an operational, source-indexed accounting system for those transfers—an RAII / borrow-checker analogy for **inference authority**, not a literal revocation of mathematical truths.

## 0. Explicit author-origin philosophical commitments

These are **author's framing; HYPOTHESIS / phenomenological posture**, not theorems about physical observers.

1. **First-person anchor.** “I am I” is experienced as the most immediate self-verifying contact within the author's field. A thin self-indexed reflexivity is the starting point, not proof of memories, body, past, identity continuity, external entities, or physical mechanisms.
2. **All further source claims owe evidence.** Claims about the remainder of the field are mediated by perception, model-building, interventions, and remembered provenance. The author describes them as less certain than that immediate anchor.
3. **Determinacy before identification.** “Is or isn't” concerns whether a state of affairs obtains; “value a versus value b” is a finer description or decision, potentially inaccessible to a probing observer. This is an *ontic–epistemic distinction*, not a claim that physical dynamics are deterministic.
4. **Maximal coverage does not certify the original source.** Every available probe may support a model, even under an infinite-horizon idealization, while an unmodeled, adversarial, or source-mismatched realization remains compatible with the observer's lawful reports.
5. **Probing may modify the carrier.** Measurement is an interaction with a source, not automatically an innocent look. This effect can be absent, classical, or quantum depending on the instrument; it must be modeled, never simply assumed.

**Epistemic precision correction:** Universal strict *probabilities* for “everything else < I am I” do not follow. Formal reflexivity x=x, P→P, and other tautologies already defeat a claim that every *other proposition* has strictly lower logical certainty; definitional equivalents tie. Without a declared probability space, priors, likelihoods, and calibration, assigning numerals to certainty is unjustified. The faithful recoverable claim is a **pretheoretic priority / confidence preorder for non-tautological, contingent world claims** relative to a first-person contact anchor. Even that ordering is phenomenological and must not be exported as objective statistical authority.

## 1. Separate the five objects that informal reasoning collapses

| Layer | Mathematical or operational object | What it does **not** buy |
| --- | --- | --- |
| **Logic** | Derivability of P∨¬P under a specified calculus | A chosen disjunct, a finite decision algorithm, a physical measurement |
| **Semantics** | Truth of P in a particular model/carrier interpretation | Source-map adequacy or privileged access to the actual world |
| **Ontology / actualization** | A specified property obtaining in a declared source state | An observer who can identify its value |
| **Dynamics** | A transition law (possibly stochastic or nondeterministic) | LEM or empirical decidability, either direction |
| **Inference authority** | Source, witness, provenance, transformation, and hypotheses that license transporting a conclusion | Unrestricted claims on forgotten fibers, unseen interventions, or undeclared carriers |

Classical ZFC **uses classical first-order logic** and hence LEM as part of its ambient logic. ZFC's axiom of choice is not its derivation of LEM. A deterministically specified transition F:S×A→S is a separate dynamical property. Classical stochastic Markov processes can have perfectly classical proposition logic while their future outcomes are random. Deterministic evolution with an unknown initial state need not let an observer decide the current hidden proposition.

This sharpens, rather than rejects, the author's complaint: *truthfulness requires typing the exact passage from a syntactic bivalent or choice-bearing mathematical model to claims about an original probed source.*

## 2. Choice versus excluded middle: the precise Diaconescu boundary

**CLASSICAL IMPORT (Radu Diaconescu 1975):** In an elementary topos, the strong internal choice principle “every epimorphism splits” entails that the internal logic is Boolean (LEM). This requires **full** choice in that categorical setting; witnessed, finite-context, dependent or type-theoretic choice is not automatically that assumption. No external privileged observer is required for the theorem.

Sketch, with effective quotients: for an arbitrary proposition P, put on 2={0,1} the equivalence x~_P y iff (x=y)∨P; form q_P:2↠Q_P. Full choice supplies s_P with q_P∘s_P=id. Decidable equality of two elements of 2 distinguishes s_P(q_P(0)) and s_P(q_P(1)). Equality yields P by the effective quotient kernel; inequality yields ¬P. Thus P∨¬P for arbitrary P.

**Operational missing arrow:** A situated observer's ability to produce a witness for every *encountered* task does not supply a section of **every** such q_P, especially when its language/toolkit cannot even form, instantiate, or observe all relevant P. “Locally I can select” is weaker than “all epimorphisms split.” The latter is not conferred by maximal success over an unproved set of accessible tasks.

**Important nonclaim:** This does not undermine Diaconescu or establish that full internal AC coexists with internal failure of LEM in an elementary topos. SUCC should formalize restricted choice/section interfaces and their source boundaries, not redefine established logical theorems.

## 3. Formal carrier/probe system with backaction

A **source-indexed instrumented carrier** is a declared tuple

\[
\mathcal C=(S,A,O,\{K_a\}_{a\in A},\lambda,\mathsf{Adm}),
\]

where S is a state space, A available interventions, O possible reports, \lambda is an initial-state distribution or declared preparation relation, and \mathsf{Adm} specifies lawful preparation, sequencing, and reset permissions. For each a,

\[
K_a(s',o\mid s)\ge0,\qquad
\sum_{s',o}K_a(s',o\mid s)=1
\]

in a finite stochastic model; K gives **both** observations and post-observation states. Infinite/measurable spaces require kernels and the relevant measurability hypotheses. A deterministic instrument is a special case.

An adaptive policy \pi selects each next action from the **lawfully acquired** history, not from hypothetical future outputs. For horizon n, let \mu_{\mathcal C,n}^{\pi} be its report-history law, including chosen actions when required.

Define equivalence **relative to an explicitly declared toolkit** \mathcal T:

\[
\mathcal C\equiv_{\mathcal T}\mathcal D
\quad\Longleftrightarrow\quad
\forall \pi\in\mathsf{Policies}(\mathcal T),\ \forall n<\infty,\ \
\mu_{\mathcal C,n}^{\pi}=\mu_{\mathcal D,n}^{\pi}.
\tag{CRL-EQ}
\]

This is an operational *idealized* quantifier, not an executable completion achieved by running all tests. A physical instrument could instead be a quantum instrument \{\mathcal I_{a,o}\} of completely positive trace-nonincreasing maps with trace-preserving outcome sum; \rho'_o=\mathcal I_{a,o}(\rho)/\mathrm{tr}(\mathcal I_{a,o}(\rho)) when the denominator is positive. No quantum-specific inference follows without that declared source.

### Theorem A — exact static forgetting criterion (CLASSICAL / scoped derivation)

For a surjection q:X↠Y and a property f:X→Z in ordinary Set, **there exists a unique** \bar f:Y→Z with f=\bar f∘q iff

\[
q(x)=q(x')\Longrightarrow f(x)=f(x')
\quad\text{for all }x,x'\in X.
\tag{CRL-DESCENT}
\]

*Proof:* necessity follows from applying \bar f. For sufficiency, define \bar f(y)=f(x) for any x with q(x)=y; the condition makes this independent of choice of representative. In constructive implementations the *availability of a representative or effective quotient eliminator* remains a separate obligation. If q maps onto its image rather than all Y, the conclusion is only on im(q).

This is the mathematical heart of the “borrow checker” analogy: **a property that varies on forgotten fibers has no licensed export from the quotient**.

### Theorem B — indistinguishability blocks universal correct decision (PROVED LOCAL under stated model)

Let P be a Boolean property of whole carrier models. If \mathcal C\equiv_{\mathcal T}\mathcal D but P(\mathcal C)\ne P(\mathcal D), no decision rule based solely on permitted finite transcripts can be almost surely correct under both sources (including randomized postprocessing).

*Proof:* every such decision has the same output distribution under the two indistinguishable sources, but correctness demands opposite point masses. Contradiction. Under consistent path measures, the same obstruction extends to almost-surely terminating adaptive procedures whose decisions are measurable from the path. The result concerns **identification from probes**, not whether the proposition has a truth value in the mathematical model.

**Maxwell-demon rival:** permit an adversarial hidden controller as an *explicit lawful stateful transducer* inside the carrier-model class. If its controlled outputs match every allowed history of two source variants, the theorem applies. An unconstrained “demon that can fake anything” is not testable and cannot itself certify a real demon or a false proposition; it states a chosen model-class boundary.

### Theorem C — moving finite phantoms do not imply one persistent rival (CLASSICAL)

\[
\forall n\;\exists C_n:\mathrm{Matches}_{\le n}(C_n,C)
\quad\not\Longrightarrow\quad
\exists C':\forall n\;\mathrm{Matches}_{\le n}(C',C).
\tag{CRL-QUANTIFIERS}
\]

Explicit noncompact witness: X_n={m∈\mathbb N:m≥n}. Every finite initial family admits m=n, while the total intersection is empty. Conversely, for a **fixed compact source space** with closed constraints and the finite-intersection property, compactness supplies a global point; a computable point requires stronger effective premises. Compactness cannot be silently imported by calling each finite source observation “finite.”

This is already developed in SUCC's [source-field limit calculus](../2026-10-15/SOURCE_FIELD_INVERSE_LIMIT_CALCULUS.md) and [field limit trichotomy](../2026-10-15/FIELD_LIMIT_TRICHOTOMY.md). Preserve the three distinct “Fucked” mechanisms: (i) no global realization, (ii) pointwise-completable finite prefixes with no original-source point, (iii) genuine indefinitely nonseparating observation classes. Do **not** label RH intrinsically Fucked, undecidable, or proven unprovable.

## 4. Three endpoints, not a single “true enough” score

For evidence history E, admissible models \mathfrak M, and a source/probe protocol \mathcal T:

**(a) Observational saturation:** no currently licensed probe splits the surviving models under their declared laws. This can include mutually incompatible truth assignments for P. No truth conclusion follows merely from lack of a discriminator.

**(b) Carrier-relative model consequence:** the compatible class is **nonempty** and

\[
\forall C'\in\mathrm{Compatible}_{\mathfrak M,\mathcal T}(E),\quad C'\models P.
\tag{CRL-RELATIVE}
\]

This licenses P *relative to the class and verified source constraints*, if the universal statement itself is proved. It does **not** establish that the model class includes the real source, or a computable P-decider.

**(c) Source-certified claim:** in addition, a lawfully established source→model interpretation transports P without losing required meaning/provenance, and source adequacy has been calibrated against independent probes/holdouts. This is a stronger evidence status, not automatic metaphysical finality.

A high toolkit-relative indistinguishability coordinate (\varphi) can coexist with an inadequate source map (\sigma). Keep probe availability (\mu), actual contact (\kappa), identity/commitment coupling (\rho), causal history and source independence as separate ledger axes. Neither \varphi nor a coherence score is a Bayesian posterior probability without a calibrated statistical model.

**Strong restriction:** Properties constant on observational equivalence classes need not be *computably* decidable from the reports. Extensional identifiability, effective extraction, model truth, and source truth are distinct obligations.

## 5. First-person reflexivity as an index, not an oracle

For a declared subject-index i in a logical context, the judgement i=i is reflexivity—intuitionistically valid. It does not, by itself, demonstrate an independently verified externally existing or persistently identical embodied subject. The phenomenal starting point “present self-reference is occurring” is recorded as the author's **pretheoretic contact postulate**; its physical realization and stability are separate questions.

A suitable formal candidate is a **preorder of source-relative warrant** W_{\mathcal T,E} on contingent, non-tautological claims, with the first-person present-contact judgement treated as a distinguished epistemic anchor. Whether this anchor dominates any given empirical claim is a *hypothesis requiring an explicit comparison protocol*, not a universal axiom or probability assignment. In particular:

- Do not assign a formula such as “certainty=1−δ” without defining δ operationally.
- Do not declare all non-anchor mathematical tautologies less true.
- Do not infer one's body, history, personal continuity, or mechanism from i=i.
- Do not infer global LEM, physical deterministic evolution, or a probability for every proposition.
- Do preserve the author's phenomenological priority as the motivating source statement, rather than deleting it because it is not itself an empirical theorem.

This permits serious analysis without laundering first-person experience into a universal neuroscience or ontology claim.

## 6. Proposed effect system for inference authority (DESIGN / UNVERIFIED)

Every abstraction arrow would carry a proof obligation record

\[
\mathcal A =(\mathrm{source\ identity},\ \mathrm{domain},\ \mathrm{law},\
\mathrm{preserved},\ \mathrm{forgotten},\ \mathrm{evidence},\
\mathrm{transport},\ \mathrm{unpaid\ obligations}).
\]

Examples of **type-level capabilities** (names are provisional): WitnessedChoice, LocalSection, GlobalSection, Decidable(P), ObsEquivalent(T), ModelConsequent(P), SourceCertified(P), CarrierTransitionWithReceipt.

Reject:

- exporting a P that varies inside a forgotten observation fiber;
- treating a locally witnessed selection as a full topos AC section;
- treating saturation of a probe class as LEM or empirical source truth;
- changing carrier/source/epoch while retaining an untransported proof;
- assuming a post-probe result describes the pre-probe state without state reconstruction;
- converting a conditional compactness existence theorem into a terminating selector;
- counting duplicated observations from a single provenance family as independent witnesses;
- identifying a positive auxiliary Gram with the authentic signed completed Weil form.

The analogy with RAII is **scope and authorization**, not literal linear consumption of proofs. Ordinary theorems can be reused; duplicating one test trace does not create independent evidence. Authority moves only with the declared assumptions and their source-preserving interpretation.

## 7. Next research plan and integration boundary

This is **docs-only**; there are NO new tests, CI receipts, Lean proofs or physical measurements claimed on this branch. See [probe contracts](CARRIER_RELATIVE_LOGIC_PROBES.md), [claim ledger](CARRIER_RELATIVE_LOGIC_CLAIMS.md), and [implementation handoff](../../handoffs/2026-10-20-CARRIER_RELATIVE_LOGIC_INTEGRATION.md).

First build exact finite positive/negative controls for observational aliasing, moving versus persistent rivals, probe backaction, and failure of source-relative transport. Then mechanize finite quotient factorization and restricted-choice interfaces in Lean (cross-check against the existing [generative choice dossier](../2026-10-19/SUCC_META_GENERATIVE_CHOICE_DESCENT.md) and [MetaChoice Lean module](../../formal/MetaChoiceRelationalDescent.lean)). Only after an independent data/source map exists should an interpretation about actual physically embedded observers be attempted.

**Explicit boundary:** No new LEM theorem beyond attributed logic; no denial of classical LEM, no objective first-person probability law, no quantum mechanism inferred from introspection, no simulation proof about all realities, and no RH / ABC / original signed Suzuki S4 promotion.

## 8. References and provenance

1. Radu Diaconescu, “Axiom of Choice and Complementation,” *Proceedings of the American Mathematical Society* **51** (1975), 176–178. [Source scan](https://conceptualmathematics.wordpress.com/wp-content/uploads/2023/07/choice_complement.pdf). Classical topos choice/LEM boundary.
2. *Stanford Encyclopedia of Philosophy*, [Intuitionistic Logic](https://plato.stanford.edu/entries/logic-intuitionistic/) and [Intuitionism in the Philosophy of Mathematics](https://plato.stanford.edu/entries/intuitionism/). Logic/constructivity and restricted choice background.
3. Existing SUCC [field-limit calculus](../2026-10-15/SOURCE_FIELD_INVERSE_LIMIT_CALCULUS.md), [field trichotomy](../2026-10-15/FIELD_LIMIT_TRICHOTOMY.md), and [generative choice/descent](../2026-10-19/SUCC_META_GENERATIVE_CHOICE_DESCENT.md). Internal derivations and fixed source boundaries; shared internal provenance is not independent literature validation.
4. SUCC [AGENTS.md](../../AGENTS.md), [METHOD](../../docs/METHOD.md), and [claim ledger](../../docs/CLAIM_LEDGER.md) govern promotion/acceptance.

*Source/probe formalizations are proposals, while the explicitly labeled quotient, compactness, and logical facts are classical results with their declared assumptions. This document is a reviewable future-integration record, not a completed scientific theory.*
