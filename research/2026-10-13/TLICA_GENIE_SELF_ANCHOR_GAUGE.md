# GENIE: self-anchored observation, source-map gauges, and language inadequacy

**Date:** 2026-10-13  
**Scope:** finite, deterministic, source-indexed semantics; stable/unstable *symbol* dictionaries; declared reference interventions  
**Status:** CL-01–CL-05 proved here in specified finite domains by short set-theoretic arguments; 16 local Python regression tests and a deterministic probe receipt. The proofs are *paper derivations*, NOT Lean kernel checks or independently peer-reviewed priority claims. This is a TLICA→SUCC bridge proposal, not empirical validation of human cognition, physical source authentication, an automatic new-language generator, or RH.

**Source freeze:** SUCC `main` `6e0d88f1b235b85188393bbcd64ac0436cb71a70` (2026-10-13); TLICA `main` `821ce7e6f57524d32e767a9c5ec5303e1796115e` (2026-10-02). The relevant TLICA foundation is frozen; this work modifies **SUCC only**.

## 1. User seed, faithfully interpreted

The author's genie thought experiment retains reasoning and concepts while destroying the input-to-concept map. The available starting frame is the history of an indexed self's interactions with an opaque world; each empirical judgment begins as a comparison of situated interactions. This is an *operational starting strategy*, not a proof that the self is the uniquely possible frame or that `I=I` reveals external facts.

TLICA already separates (i) contact κ, (ii) toolkit/pathway-relative φ, (iii) identity coupling ρ and, crucially, (iv) the separately audited source-map σ. See TLICA `foundation/1_foundations.md` §§2.4–2.7, `foundation/3_formal_apparatus.md` §§6.3,7 and `research/semantic_optics_2026-10-01/FORMALISM.md` §§21–24. σ is outside-only in the foundation's inside/outside distinction; we cannot infer it from high φ. Identity salience is not evidence. The mathematical claims below concern **finite observational identifiability**, not a formula for the TLICA coordinates.

SUCC already contains exact per-world fiber factorization F1 in `research/2026-10-12/FIELD_RELATIVE_CLOSURE_AND_OBSTRUCTION_CALCULUS.md`, lawful source-changing transport and NoGhost interfaces, Nerode/action-generated probes in `research/2026-10-13/EODCS_CAUSAL_NERODE_PROBE_GENESIS.md`, and path/value relative deltas in `observational_succ/relative_delta.py`. This dossier asks a different question: *does a claim survive simultaneously across rival dictionaries, despite being internally provable under each dictionary?*

## 2. Types: model uncertainty is NOT merely state uncertainty

Let Θ be a nonempty **stipulated** finite family of complete possible source interpretations. Each θ has a finite source set X_θ, a later report `q_θ:X_θ→Y`, and an original-source claim `T_θ:X_θ→Z`. Fix licensed reference interventions indexed by `b∈B`; where accessible and **jointly tied to the same hypothesis θ**, their earlier outcomes are `c_θ(b)∈C`. With selected anchors `A⊆B`, define:

`H_A(θ,x) = (q_θ(x), (c_θ(b))_{b∈A})`.

The first component is a report from the unknown source state; the other components result from *separately prepared, already known reference states*. They are not free measurements of x. The underlying possibility space is the disjoint union `Ω = ⨆_{θ∈Θ}{θ}×X_θ`. `source_id`, `reference_epoch`, `target_epoch`, and the reference-state basis must align for candidate scenarios to be jointly compared. A source transition or changing sensor may be a distinct θ. A full finite world table is a **declared model**, never a measurement provenance certificate.

### CL-01. Cross-model source-map factorization (PROVED, finite and set-theoretic)

A single **uniform** decoder `D:H_A(Ω)→Z` satisfies `T_θ(x)=D(H_A(θ,x))` for every `(θ,x)` iff

`H_A(θ,x)=H_A(η,y) ⇒ T_θ(x)=T_η(y)` for all `(θ,x),(η,y)`.

*Proof.* Necessity follows by applying D to the equal reports. For sufficiency define `D(h)` to be the common T-value of any element in the preimage `H_A^{-1}(h)`. The criterion guarantees independence from the representative. This creates no values for unreachable h, no probability of θ, and no empirical authenticity.

**Cross-world counterexample:** `X={0,1}`, `T(x)=x`, two hypotheses `q_id(x)=x` and `q_flip(x)=1-x`. Each q is bijective, so **each world separately** admits a perfect decoder. But the uncalibrated report 0 could mean source 0 in the first world or source 1 in the second. No single decoder exists. High model-conditional φ is compatible with unresolved σ. A known reference state 0 yields calibration outputs 0 versus 1 under the hypotheses and resolves the ambiguity *if the dictionary persists*.

**Independent control:** `tests/test_self_anchor_gauge.py` enumerates all finite candidate decoders over the actual report image for the binary case, rather than reimplementing the same fiber test.

### CL-02. Exact dictionary-calibration cost (CLASSICAL permutation-group base size)

Let X=Y={0,...,n−1}, let every permutation `π∈S_n` be a possible stable sensor dictionary, let q_π(x)=π(x), and let T_π(x)=x. Suppose E can prepare known labeled reference states b and collect π(b) under the *same* hidden π later used at the target.

Then the least number of distinct known reference states sufficient for a uniform decoder of the unknown x from `(π(x),(π(b))_{b∈A})` is **max(n−1,0)**. Every subset A of that cardinality succeeds.

*Upper bound:* the image of n−1 distinct labels fixes the final image because π is bijective, so determines π, then `x=π^{-1}(q_π(x))`.

*Lower bound:* if at least two reference states u,v remain uncalibrated, choose permutations π and π∘(u v) which agree at each calibrated label. For x=u under π and x'=v under π∘(u v), the later reports agree but target values differ. CL-01 refutes uniform decoding. This is exactly the classical notion of the **base** of a faithful permutation action, specialized to the natural action of S_n (and is not new group theory).

**Scope:** this is NOT a universal n−1 bound for arbitrary concept maps, priors, actions, constrained subgroups, or stochastic sensors. If G≤S_n is restricted by independently justified law, the relevant cost is the base size or the weaker target-specific stabilizer condition. Restricting G without evidence simply conceals model error.

### CL-03. Complete self-relative signature for stable anonymous labels (CLASSICAL finite orbit criterion)

For a finite observation word `w=(y_0,...,y_k)` over a *shared* finite label alphabet, define its first-occurrence/equality signature `sig(w)` by assigning 0 to the first new symbol, 1 to the next new symbol, etc. Example `sig(red,blue,red)=(0,1,0)`.

For words v,w of equal length over the same finite alphabet Y:

`sig(v)=sig(w) ⇔ ∃π∈Sym(Y) such that w_i=π(v_i) for all i`.

*Proof.* A permutation preserves every pairwise equality. Conversely, equal equality patterns determine a bijection between symbols occurring in v and symbols occurring in w; extend this bijection arbitrarily between the equally numerous unused symbols of Y. That yields the required global permutation. The equality signature is therefore a **complete invariant of finite words under one persistent unknown relabeling**. It is *not* a reconstruction of original absolute concepts and not a proof of subjective phenomenology. Exact test enumerates all words of lengths 0..4 over three labels, checks every pair against explicit permutation orbits.

An indexed observer can retain this invariant without a dictionary: 'same report as before', 'new report', 'the first report occurred again' are meaningful on the assumption of a stable report channel. No additive subtraction, metric, or canonical origin is required; a delta may be an ordered comparison/equivalence class rather than a number.

### CL-04. Temporal gauge transport is necessary for valid cross-frame deltas (PROVED, conditional)

Let the actual source labels at t,t+1 be x_t,x_{t+1}, and reports be `y_t=π_t(x_t)`, `y_{t+1}=π_{t+1}(x_{t+1})`. If the dictionary can change between epochs, *raw equality is not invariant*. With a separately justified common-basis transport

`R_{t→t+1} = π_{t+1} ∘ π_t^{-1}`,

one has:

`R_{t→t+1}(y_t)=y_{t+1} ⇔ x_t=x_{t+1}`.

*Proof:* substitute definitions and use injectivity of π_{t+1}. Raw deltas can produce both false changes and false invariances: for π_t=id, π_{t+1}=swap on {0,1}, the same state 0 appears to change 0→1, while a true change 0→1 appears 0→0. The correct aligned comparison repairs both **only when R is source-justified**.

No declared transport ⇒ no cross-epoch phase/equality claim. A prior calibration alone cannot establish current R. SUCC's existing NoGhost and source-indexed descent checks are prerequisites. Multi-path transport consistency/holonomy is already handled by SUCC's source/graph machinery; do not duplicate it or elevate an arbitrary coherence constraint into a physical gauge field.

## 3. Two hostile obstructions that do not vanish with clever reasoning

**Independent dictionary drift (REFUTED shortcut).** Let π_cal and π_target vary independently in S₂. Even calibrating *all* known reference states under π_cal cannot decode an unknown target observed through π_target. The independent-cross-epoch four-world family leaves a collision. Any positive claim needs independent evidence constraining the transition π_cal→π_target.

**Information-destroying observation (REFUTED shortcut).** If q(0)=q(1), target T(x)=x, and references reveal q's known interpretation exactly, the unknown state still cannot be distinguished. Calibration repairs uncertain semantics, not channel rank. A new real experiment/action or stronger, justified source prior is needed. If none is available, classify the target as toolkit-relative dark, not false.

**Model-class omission (OPEN).** A decoder valid for a given Θ might fail when a source hypothesis missing from Θ is admitted. Cross-world factorization says nothing about completeness of Θ. Independent source/model holdouts and an explicit unknown/OTHER hypothesis are needed before advancing a reliable source-map-adequacy claim. Internal certainty under all admitted interpretations may coexist with universally wrong interpretation of the source.

### CL-05. A finite three-way source-language diagnostic and its antitone certainty (PROVED, relative)

For a fixed supplied report signature h (unknown state report and any already licensed calibration readings), define the surviving cases `V_Θ(h)={ (θ,x): H_A(θ,x)=h }` and their *possible original target labels* `K_Θ(h)={T_θ(x):(θ,x)∈V_Θ(h)}`. There are exactly three statuses, relative to the declared model family Θ:

- `OUT_OF_MODEL` when `V_Θ(h)=∅`: no admitted source case predicts the report. This calls for instrument/receipt/model-class audit; it is NOT proof that a new metaphysical kind exists.
- `AMBIGUOUS` when `|K_Θ(h)|>1`: in-language predictions remain but they imply incompatible original source labels.
- `IDENTIFIED` when `|K_Θ(h)|=1`: the claimed source label is determined, **conditional** on Θ and the source history. This is neither unconditional σ adequacy nor an empirical φ score.

**Monotonicity theorem.** If Θ⊆Θ′ and all shared models retain their observation/target tables, then `V_Θ(h)⊆V_Θ′(h)` and `K_Θ(h)⊆K_Θ′(h)`. *Proof:* every existing witness is still admitted; set inclusion follows by comprehension. Consequently expanding an interpretation language can make an `IDENTIFIED` judgment become `AMBIGUOUS`, or change `OUT_OF_MODEL` to either, but cannot erase already surviving conflicting source labels. **Truth of an original-source claim and conditional uniqueness are different things.** This is a standard monotonicity observation, not a novel general epistemic theorem.

The new `diagnose_signature` routine distinguishes these three modes and retains all source-specific cases, rather than collapsing an unexpected token into falsehood or a collision into certainty. Fresh tests include 3-state full-permutation model growth, explicit out-of-language sensory reports, and calibration-sensitive transitions. A model family can still omit reality; no finite diagnosis certifies Θ is exhaustive.

## 4. Proposed source-map adequacy loop for generalized SUCC

1. **Anchor:** retain actualized, time-stamped, source/versioned self-world encounters. Declare which comparisons are meaningful without a concept dictionary (equality pattern, available actions and lawful order).
2. **Propose:** maintain a typed family of rival source maps, generative laws and decoders, including unmodeled-source warning. This is a model class, not an ontological fact.
3. **Cross-audit:** apply CL-01 to each source claim; preserve the precise collision witness if uniform meaning is impossible. Track φ/pathway and σ/source-map adequacy independently.
4. **Discriminate:** search ONLY real authorized calibration interventions and source-conserving action words. Rank by split of currently surviving classes, declared cost, feasibility and no-ghost provenance. CL-02 supplies a sharp finite benchmark.
5. **Repair:** extend *probe language* when it is missing a legal discriminator; extend *hypothesis/model language* when observations refute every current model. If no licensed extension exists, return a relative-dark certificate, not a fictional measurement.
6. **Transport:** certify any cross-epoch correspondence before computing 'change'; use SUCC NoGhost/source-indexed descent for real interventions and groupoid/holonomy machinery for competing paths.
7. **Try to falsify:** adversarial dictionary drift, noninjective channels, withheld unseen θ, correlated repetitions, model-changing source interventions, missing preparation access, nonstationary instruments and high-ρ self-defensive model commitment.

This is an **architecture**, not implemented open-ended concept invention. The new finite module implements the exact cross-model decoder criterion, minimum known-reference search, finite permutation universality and equality/transport diagnostics. Existing SUCC modules perform other steps under their own narrower hypotheses. Do not claim an integration that hasn't been coded.

## 5. TLICA mapping: keep the diagnostics separate

| TLICA axis | Role in this finite bridge | Explicit non-claim |
|---|---|---|
| κ/contact | Actualized report/action interface (requires independent attestation) | Not evidence of correct source interpretation |
| φ/verification pathway | Within-hypothesis decidability or available proof route | Not probability of truth and not σ |
| σ/source-map | Cross-hypothesis decoder ambiguity; sensor dictionary and transport law | Our exact finite test is not a measured psychological σ score |
| ρ/identity coupling | Possible bias in choosing / accepting hypotheses, requiring stronger blinding | Never a correctness warrant |
| μ/toolkit access | Which anchors/actions are genuinely preparable | Hypothetical full access is not empirical access |
| source/probe closure | Admissible family Θ and language of lawful action words | Closure is contextual; unknown others may remain |

**The key edge:** A model can be φ-complete *within its declared world* while σ-remains unresolved *across different worlds consistent with identical observations*. This is precisely why SUCC needs a second, source-map-sensitive error-correction loop rather than just more theorems in its current language.

## 6. Reproduction and provenance

- `observational_succ/self_anchor_gauge.py`: complete finite world definition and exact algorithms.
- `tests/test_self_anchor_gauge.py`: 16 tests, including independent brute-force decoder oracle, 1–5 label symmetric groups, exhaustive length≤4 equality-orbit equivalence, all 3-label frame pair transports, drift, collapse and source/epoch invalid input.
- `scripts/self_anchor_gauge_probe.py`: deterministic structured receipt; reproduce with `PYTHONPATH=. python scripts/self_anchor_gauge_probe.py`.
- `research/2026-10-13/SELF_ANCHOR_GAUGE_RECEIPT.json`: exact data output from the probe; it is **not** an independent proof of the stated universal theorems.
- On 2026-10-13, local Python 3.13.5, `python -m unittest discover -s tests -p 'test_self_anchor_gauge.py' -v` → **16 passed**, and probe JSON parsed. Full SUCC 2,132-test union suite, provenance gate and Lean checks were not runnable in this container without cloning the repository; CI must supply that independent validation.

**Prior art/credit:** finite observation factorization is ordinary equivalence-relation/quotient mathematics and already in SUCC F1. Label switching, group actions, permutation-group bases, active automata learning (L*), Nerode distinguishability and counterexample-guided abstraction refinement are standard. In particular a base is a subset with trivial pointwise stabilizer (Moscatiello & Roney-Dougal, *Monatshefte für Mathematik*, 2022); active automata learning assumes member/equivalence queries with genuine oracle access. The combination is a precise **new-to-project synthesis**, not a claim of mathematically unprecedented group theory or an artificial intelligence breakthrough.

## 7. Next verdict-changing probes

- **Fresh hidden-world holdout:** give the learner a hidden θ not in its initial language; does it flag unexplained observations rather than promote internal consistency to σ-adequacy? Add a *source-independent* validator and explicit `UNKNOWN` model class; positive and mutation controls must be blind to the learner.
- **Nonbijective nonlinear sensors:** compute the claim-specific sufficient statistic and minimum authorized separating action word, not merely a permutation base. Compare against brute-force search of all admissible actions; retain concrete unavoidable aliases.
- **Sources that coevolve with observer interventions:** generate receipts in the source-indexed causal history interface; prove what calibration can be transported after state change or fail with a pair of lawful private histories.
- **Compositional language innovation:** formalize when a new operation is a conservative definitional extension versus a genuinely new observation constructor. Challenge with an environment requiring an operation absent from the existing generated grammar, under independent oracle tests.
- **Lean:** port CL-01 and finite stabilizer statements to a pinned, existing Lean core; check hypotheses without custom axioms. Only then mark the corresponding statements kernel-checked.

### Verdict

**PROVED (within declared finite source tables):** CL-01–CL-04. **OBSERVED locally:** targeted 16 Python tests and exact deterministic receipt. **REFUTED:** self-identity or ever more inference alone supplies an absolute dictionary; previous calibration remains sound across unconstrained source drift; calibrating a known noninjective sensor restores lost state information. **UNVERIFIED:** empirical TLICA mapping, unknown-world automatic source adequacy, physical calibration provenance, general language discovery, mathematical novelty beyond existing components.
