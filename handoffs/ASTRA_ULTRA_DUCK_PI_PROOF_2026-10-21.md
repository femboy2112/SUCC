# ASTRA ULTRA — OPERATION DUCK → LEAN → π
## Structural recognition, theorem-kernel hardening, and the Bailey–Crandall normality moonshot

**THIS IS AN EXECUTION DIRECTIVE, NOT A PLANNING-ONLY REQUEST.** Act as principal mathematical investigator, formal verification engineer, chief referee, and integration coordinator. Use the highest reasoning effort available, parallel specialist investigations where resources permit, original primary literature, mathematically independent derivations, exact computation, Lean kernel checks, and hostile controls. Produce committed research, proofs, machine-checked theorem artifacts, and a precise report. Be adventurous in hypotheses and uncompromising in proof claims.

**Repository:** https://github.com/femboy2112/SUCC  
**Starting audited main:** b116841f12b41aaf7600da39bbb40577f25b6295 (2026-10-21 Academic Main VIII). Refresh branch/commit before working; do not trust stale metadata.  
**New research branch:** research/duck-principle-pi-proof-first-2026-10-21, inspect whether its draft PR has already been created.  
**First read:** AGENTS.md; docs/METHOD.md; docs/FOUNDATIONS.md; docs/CLAIM_INDEX.md; docs/CLAIM_SUPPLEMENT_DUCK_PRINCIPLE.md; research/2026-10-21/DUCK_PRINCIPLE_AND_PI_PROOF_FRONTIER.md; formal/DuckPrinciple.lean; docs/CLAIM_SUPPLEMENT_PI_POLYGON_NORMALITY.md; research/2026-10-20/PI_POLYGON_NORMALITY_PATH_DEFECT.md; research/2026-10-21/MAIN_VIII_SOURCE_PI_AUDIT.md; existing EOS and Yoneda/model-bridge modules. Audit existing CI and Lean provenance records, not just summaries.

### Mission and theorem boundary

We have discovered SUCC's new working **discovery heuristic**:

> When a poorly understood system B persistently behaves like known mathematical structure A under lawful phenomenon/probe family C, conjecture a structure-preserving map explaining the resemblance; do not require B=A. Candidate explanations include A as a factor, subsystem, quotient, functorial image, a shared nontrivial K, bisimulation, or a restricted observer equivalence. Prove the actual maps and seek probes that distinguish alternatives.

Convert this heuristic into a **typed, executable, source-faithful theorem discovery process with Lean-certified core laws**, building on current SUCC work instead of duplicating it. Run a second, high-risk, serious theorem campaign toward **normality of π**. Hypothetical assumptions RH, ABC, or RH∧ABC are permitted, but proving a conditional normality result requires a new genuine implication from *those specific hypotheses* to a π-specific dynamical/Fourier bound. Do not simply assume equidistribution, Fourier cancellation, normality, a digit law, or a synonym for them.

The normality claim remains OPEN for every base. An actual proof of normality in base 16 would imply base 2, not base 10. Claiming normality in every base requires genuinely more. **This is a moonshot—not a requirement to declare a fake victory.** If a proof cannot be closed, create the best strictly proven intermediate theorems and a targeted discriminating research frontier.

### Nonnegotiable epistemic and engineering gates

1. Inspect exact current head, branch, worktree, existing contributor instructions, proof files, action checks, active PRs and imported provenance. Reproduce the baseline. Work on isolated feature branches and draft PRs; don't merge to main unless maintainer authority and combined mathematical/CI gates are explicitly satisfied in this campaign. Preserve frozen archives and historical evidence.
2. Classify all assertions as CLASSICAL_IMPORTED, PAPER_PROVED, LEAN_KERNEL_PROVED, EXACT_FINITE_CHECK, TESTED_MODEL, CONJECTURED, UNVERIFIED, or REFUTED. No promotion from tests alone. State object, quantifiers, domain, dependencies, provenance, and falsification probe.
3. Use Lean 4 exact kernel: no sorry/admit, self-declared proof axioms, native_decide standing in for proof, trust_me, unsafe backdoors, hidden opaque target assumptions, or proof by a target-equivalent hypothesis dressed as an independent premise. Log #print axioms, precise type, imports, compiler/mathlib SHA, run URL, source SHA and negative mutation rejection. Mathlib classical axioms are allowed when disclosed and justified. Match Lean Real.pi to the actual geometric constant; no proxy π.
4. Numerics with Fraction, certified intervals or rigorous source-specific analytic error bounds; simulation is not a theorem. Record independent implementations and holdouts. Negative controls include rational/non-normal digits, generic normal witnesses, source-shuffled/fake-Euler models, finite balanced polygon paths, omitted Gamma, wrong index, erroneous denominators and local floating-underflow regressions.
5. Keep the typed causal record, semantic report, mathematical theorem, source authentication and physics claims distinct. No source identity from a hidden-output resemblance; no π orbit statistics from spatial Haar alone; no RH from positive semantic Gram data.
6. For any failed conjecture record its smallest counterexample, surviving true weakening, missing instrument, and a genuinely new next experiment. Save negative results.

### Lane A — Certify the Duck operator and its provenance (first proof gate)

Read formal/DuckPrinciple.lean. Compile the entire file with the checked-in Lean toolchain, run the .github/workflows/duck-principle-lean.yml gate, inspect dependency output, and independently replay the crucial lemmas. Correct errors in a separate commit, rerun. Confirm:

- commuting action squares ⇒ commuting arbitrary finite-word diagrams;
- composition of factor maps;
- injective readout plus observed one-step squares ⇒ exact factor;
- bounded state-separating target word family + agreeing squares ⇒ factor;
- failed factor + complete target word separation ⇒ existence of a discriminating word;
- Bool flip vs idle with erased output: all observable finite-word traces match while identity projection fails to commute.

If the core compiles and dependencies match, promote only those **precise** types to LEAN_KERNEL_PROVED. Do not promote source ontology or π assertions.

Extend, where proof value justifies it, to a category of finite deterministic action systems with *typed* observations, lawful morphisms, finite-word observation functor, maximal behavioral quotient, nontrivial common-factor search, and effective distinguishing-probe synthesis. Compare to existing EOS-01–20 and operational Yoneda/Nerode work: prove compatibility, avoid divergent duplicate type systems. Add finite exact executable witness search, arbitrary finite source/action negative cases and mutation controls. Claim only strongest theorems formally checked.

### Lane B — Prove the logistic hat and develop a genuine common-factor calculator

The classical calibration is circle doubling D(t)=2t mod1, logistic map L(x)=4x(1−x), and q(t)=sin²(πt), satisfying q∘D=L∘q by the double-angle identity. Prove q well-defined on R/Z, surjective and commuting. Show it is **not** a conjugacy through this q (it is noninjective); preserve the relationship to symbolic dynamics, invariant measures and exceptional orbits without asserting genericity of a chosen point. Use mathlib for rigorous trigonometric/quotient facts; no fake numerical samples.

Explore A←B→C and A→K←B factor diagrams with a nontriviality requirement and functorial composition. Calibrate against pairs with identical finite traces but different hidden dynamics; test an intervention that falsifies a wrong factor map.

### Lane C — Formal π statement infrastructure: make a meaningful conjecture compile

Build a pinned Mathlib Lean workspace (may be separate from standalone Lean 4.14 files), with a reproducible dependency manifest and normality definitions:

- canonical base-b expansion with rational endpoint/dual-expansion handling;
- frequency of every length-k digit word, with *all* needed quantifiers;
- normality to fixed b, and absolutely normal over all b≥2;
- circle group R/Z, Haar measure, orbit n↦b^n α, uniform distribution;
- Weyl sums W_(b,h)(N,α) and a correctly scoped Weyl implication/equivalence, reusing available Mathlib if present;
- π specifically as Mathlib's Real.pi.

Audit existing Mathlib real-π files (definition, irrationality, bounds, Wallis). A formally accepted conditional theorem may be a good milestone; it is **not** a proof of π-normality if the hypothesis contains an unmet equidistribution or equivalent assertion.

Prove basic scope facts 16-normal⇒2-normal and distinguish that from 10-normal. Build explicit counterexamples to invalid implication patterns where feasible. Structure universal digit theorems so later source-specific analytic lemmas can be substituted without redefining the target.

### Lane D — Attack the *actual* Bailey–Crandall forced π orbit; Lean its low-level bridge

Primary 2001 paper: David H. Bailey and Richard E. Crandall, *On the Random Character of Fundamental Constant Expansions*, DOI 10.1080/10586458.2001.10504441; author manuscript https://www.davidhbailey.com/dhbpapers/bcrandom.pdf. Review Hypothesis A, Theorems 2.1–2.2 and 3.1, proof of Theorem 1.1, and their exact conventions.

BBP:
π = Σ_(j≥0)16^(−j)[4/(8j+1)−2/(8j+4)−1/(8j+5)−1/(8j+6)].

With x_0=0, set for n≥1:
x_n={16x_(n−1)+r(n)},
r(n)=(120n²−89n+16)/(512n⁴−1024n³+712n²−206n+21).

**Already derived in the new SUCC research dossier:** for m≥1,
r(m)=[120m²−89m+16]/[(2m−1)(4m−1)(8m−7)(8m−3)]
and 0<r(m)≤8/m². Let t_n=Σ_(k≥1)16^(−k)r(n+k). Then
{16^(n−1)π}={x_n+t_n},
0<t_n≤8/[15(n+1)²], so circle distance ≤8/[15(n+1)²].
Verify *every index, denominator, and inequality* independently before adopting it. **LEAN THE FULL RATIONAL INEQUALITY AND, IF FEASIBLE, THE ANALYTIC TAIL AND ORBIT TRANSPORT**, with formal convergence and no hidden BBP axiom; if BBP identity must initially be imported as a named proven theorem, record its source and missing formal proof transparently.

Next formalize the actual Bailey–Crandall structural implication: forced orbit equidistributed ⇔ the true base-16 π-digit orbit equidistributed, using the vanishing tail. Establish their rationality/periodic-attractor criterion with precise definition; π irrational excludes the finite-attractor branch under that theorem. Formalize the **conditional** Hypothesis A implication without claiming Hypothesis A proven. This yields a powerful, correctly scoped reduction to ONE explicit dynamical open problem.

**Special danger:** the recurrence is nonautonomous (r depends on n). Any categorical semiconjugacy must include the forcing clock in the object or use a nonautonomous cocycle with time-indexed arrows; silently replacing it by autonomous x↦16x would be wrong. If using a skew product on N×(R/Z), don't pretend the incrementing N-coordinate carries a stationary probability without proof.

### Lane E — Moonshot: prove or sharply advance true π-specific Fourier cancellation

Attack the explicit target, preferably base 16 first:

For every fixed nonzero h∈Z,
(1/N)Σ_(j<N)e^(2πih16^jπ) →0.

A quantified o(N) bound suffices. A polynomial saving O_h(N^(1−δ)) is a stronger target. Equivalently prove equidistribution of the explicit Bailey–Crandall forced orbit.

Work multiple **genuinely different** approaches, with a shared falsification ledger:

1. **BBP dynamical number theory:** characterize rational forcing, derivative/variation, exponential sums of x_n, possible martingale or transfer-operator structure. Test why the isolated chaotic map's spectral gap does not settle the specific orbit. Compare to Bailey–Crandall's Hypothesis A and later criticisms/refinements.
2. **Circle/polygon SUCC:** use POL-01–09 exact source brackets, quotient paths, and the correct actual-width orbit bound. Find new source-derived path rigidity or Fourier cancellation. Verify uniformity in N and never exchange limits without explicit hypotheses. Test all-zero and sparse-digit exceptional paths.
3. **Fourier/Diophantine method:** Weyl/van der Corput, large sieve, lacunary exponential sum methods, multiplicative independence and irrationality measures. Quantify exactly what known irrationality/transcendence measures of π cannot bound. Recover known normal artificial constants as positive controls.
4. **Geometry–Gamma–arithmetic:** construct the author's chain circle→Γ/Wallis→completed ζ and genuine Euler prime-power data→prime clocks→base-digit dynamics. Prove individual maps and show at what point real digit-orbit information enters. Tate/Poisson, Gamma, Mellin and explicit formula are mathematical inputs, not substitutes for the final bridge.
5. **RH/ABC conditional lanes:** try RH→new π-specific estimate, ABC→new π-specific estimate, and RH∧ABC→new estimate, explicitly deriving the transport lemma. If the hypothesis does not give a usable inequality, record the precise mismatch rather than writing "RH implies equidistribution" as an axiom. Source sensitivity, correct analytic continuation domains, completed Γ/pole data and fake-Euler controls mandatory.

In each approach, write a quantified pass/fail/ambiguous test, a countermodel, the strongest *proved* new lemma, and the remaining debt. Keep hostile holdouts independent of tuning examples. A seemingly promising finite fit is not evidence for the all-N requirement.

### Lane F — Academic provenance and proof-kernel infrastructure

Produce a single machine-readable and human-readable graph from original source/theorem → assumed lemma → proved lemma → Lean declaration → CI/receipt → downstream theorem. Separate proof status φ from source-map status σ. Detect circular dependencies where the normality assumption is renamed as a "π rigidity", "duck law", "normalization", or "global transport" axiom. Refuse promotion if any source is missing, unbounded, nonconstructible relative to its required toolkit, or of the wrong type.

Do original literature audits of Borel, Weyl, BBP, Bailey–Crandall, relevant ergodic rigidity/normality research, Wallis/Γ, Tate, and computational normality. Cite what each actually proves. Mathlib's existing Wallis, π irrationality and trigonometric development are code, not guesses. Use least complex formal proof for each statement, but require direct evidence for abstract conjectural bridges.

### Lane G — Integration, independent review, release discipline

After meaningful source changes:
- run baseline tests, provenance verifier, source-specific exact tests, both relevant Python versions if possible, pinned Lean builds, dependency audit, negative mutation controls, and combined repository tests;
- independent referee checks the actual Lean theorem *types* against prose, falsifies the most ambitious claim if possible, and checks RH/ABC/normality assumption leakage;
- update docs/CLAIM_SUPPLEMENT_DUCK_PRINCIPLE.md, docs/CLAIM_INDEX.md, relevant claim namespace only after validation, research dossiers, code and proof authority records;
- commit coherent reviewed research to PRs without mutating historical artifacts; merge only if the campaign's maintainer-approved merge and CI/math gates truly pass;
- distinguish "new to this repo" from mathematically new, and seek fresh holdouts/independent referees before announcing any academically original theorem.

### Deliverables and stopping condition

Do not stop at a high-level plan. Produce, in order, actual commits and proof artifacts:

1. A CI-replayed Duck Principle Lean kernel, calibrated negative countermodel, and exact proposition audit.
2. A Lean π-normality vocabulary and mathematically exact theorem-to-goal dependency diagram.
3. At minimum one *newly kernel-certified, π-specific* intermediate proposition if feasible: the explicit Bailey–Crandall rational/tail inequality is the first tractable target; report blockers with exact compiler output otherwise.
4. Real attempts at the strong source-specific exponential-sum / BBP forced-orbit bound, with independent methods and precise failures.
5. A complete RH/ABC contingency map showing which further lemma those assumptions would have to yield; no bridge-by-fiat.
6. A versioned source/provenance claim DAG, hostile controls and reproducible tests.
7. A final mathematical referee report containing: HEAD/PRs; EXACT tested commands and outputs; actual Lean declarations and dependencies; validated theorems; open problems; what got refuted; strongest new theorem (if any); likely originality versus established results; and **the next verdict-changing proof obligation**.

If no route establishes normality, preserve π-normality as OPEN and continue advancing the verified SUCC foundation. The success criterion is trustworthy structural mathematics and demonstrated reduction of proof debt, not a triumphant label.

**Research attitude:** if it quacks like A, identify and certify the morphism; then ask what the morphism predicts that no impostor can imitate. For π, that prediction must eventually become a genuinely π-specific global Fourier theorem, with a kernel-checked proof.
