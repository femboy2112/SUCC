# Operation DUCK → PROOF → π: structural recognition, trusted foundations, and a normality moonshot

**Date:** 2026-10-21. **Starting main:** b116841f12b41aaf7600da39bbb40577f25b6295 (Academic Main VIII). **Status:** research programme plus classical paper proofs and an independently CI-compiled standalone Lean 4.14 kernel for finite-action factor lemmas ([successful run 39605851189](https://github.com/femboy2112/SUCC/actions/runs/39605851189), source blob `4d72da20f41b0ff06305b6f19acd7fa864b87924`); not a claim that π-normality, RH, or ABC is proved. **Author's initiating intuition:** if B repeatedly looks, sounds, and behaves like A under a phenomenon C, B may *encode an A-shaped structure* in its interactions, without B being identical to A.

This dossier is governed by [AGENTS.md](../../AGENTS.md), [METHOD.md](../../docs/METHOD.md), [FOUNDATIONS.md](../../docs/FOUNDATIONS.md), the [claim index](../../docs/CLAIM_INDEX.md), and the existing [POL-01–09 programme](../../docs/CLAIM_SUPPLEMENT_PI_POLYGON_NORMALITY.md). Preserve history and existing negative controls. RH is a downstream application; SUCC must be independently useful.

## 1. Steelman: the Duck Principle is abductive, not deductive

Given a source/model B, a recognized mathematical structure A, a probe family P, a phenomenon C, and a causal/action context, persistent similarity motivates a typed **search for an explanatory structure-preserving map**. Candidate shapes:

* **Factor/semiconjugacy** q:B→A satisfying q∘T_B=T_A∘q; if q is onto, A is a dynamical factor of B.
* **Embedded subsystem** i:A→B with T_B∘i=i∘T_A; this is a different arrow and does not follow from a factor.
* **Conjugacy**: a bijective map with commuting dynamics (stronger still).
* **Shared nontrivial quotient or invariant** B→K←A, with specified observations/structure; the terminal one-point common quotient is vacuous and must be rejected as a discovery.
* **Functor/natural transformation** with declared objects, arrows, typing and naturality squares.
* **Coalgebraic behavioral quotient** or a source-faithful simulation/bisimulation; forward simulation, bisimulation, trace equality and source identity are different.
* **Statistical/effective equivalence** under declared instruments, horizons, approximation norms and causal costs; this is not by itself an exact isomorphism.

A resemblance score or Bayesian prior chooses candidates and discriminating tests; it does not assign a probability that a theorem is true, nor does it prove existence of a map.

### A falsifiable operational statement

Fix an action alphabet Act, a state set B with transitions S_B(a,-), a candidate target A with S_A(a,-), and projection q:B→A. The proposed factor law is

    ∀a∈Act ∀b∈B, q(S_B(a,b)) = S_A(a,q(b)).

**All-word transport theorem (classical; standalone Lean candidate):** this implies for every finite action word w,

    q(S_B^w(b)) = S_A^w(q(b)).

For each target readout o:A→R, applying o gives identical observed reports. The proof is induction on the word. Composition of such maps preserves the law. A faithful, injective target readout conversely upgrades observed equality of *all one-step squares* to exact factor equality; a separating family of target action words can replace injectivity, including at a finite certified budget when it distinguishes every target-state pair. See [formal/DuckPrinciple.lean](../../formal/DuckPrinciple.lean). **Formal authority for its exact finite-action statements is verified by the pinned kernel; this does not formalize the motivating analogy or general inference from resemblance.**

**Constructive-probe principle (conditional theorem):** if target states are separated by the full family of finite action-word readouts, a failed candidate factor has an action, source state, and finite target word that distinguishes the two sides. This is an existence theorem; executable search further needs a finite/effectively enumerable model and a terminating state-equivalence decision procedure.

### Crucible: no resemblance-to-ontology shortcut

Take B=A=Bool, the candidate map q=id, with B toggling the bit and A keeping it unchanged. Let the only readout send both states to the same unit value. **Every finite experiment agrees at the readout**, but q does not commute with a single toggle. The Lean countermodel proves both facts. The correct diagnosis is insufficient probe separation, not that the underlying maps are equal. Conversely, full behavioral separation may only identify the minimal *observable quotient*, not the internal physical mechanism or source identity.

A shared factor B→K←A is meaningful only after:
1. K has a nontrivial specified structure, not a one-state discard map.
2. The maps preserve the declared operations/actions and original-source constraints.
3. The discovery predicts a fresh lawful observation not used to fit it.
4. Competing maps have independent discriminating probes or are explicitly contextually saturated.
5. The proof distinguishes factor, subobject, conjugacy, equivalence of categories, simulation, and only finite trace agreement.

**TLICA state:** record κ/contact, φ/toolkit-relative indistinguishability, σ/source-map adequacy, ρ/identity coupling, μ/probe availability, Cl(Tools), provenance, and holdouts separately. A large observable agreement class is not automatically a small source-identity class. The use of a metaphor is a heuristic prior; the law and its provenance carry the mathematical authority.

## 2. First exact illustration: circle doubling wears a logistic-map hat

Let D(t)=2t (mod 1) on the circle R/Z, let L(x)=4x(1−x) on [0,1], and define q(t)=sin²(πt). The angle-doubling identity gives

    q(D(t)) = sin²(2πt)
            = 4sin²(πt)cos²(πt)
            = L(q(t)).

The map q is surjective and generally two-to-one. Hence L is a **factor** of circle doubling; it is not conjugate to it via q. This is an exact elementary theorem on actual maps and a promising calibration target for a later mathlib Lean file. Do not confuse its phase-circle coordinate t with the geometric construction of the special number π: the existence of this factor gives **no theorem** about digit normality of π.

This interpretation fits SUCC's logistic observer-tree work: a map can reveal one faithful dynamical quotient while erasing other source distinctions. To link with actual prior modules inspect observational_succ/operational_yoneda_descent.py, categorical_model_bridges.py, heuristic_bridge_discovery.py, contextual_heuristics.py, and the EOS-01–20 dossier; avoid reinventing their semantics and existing obstructions.

## 3. π-normality: write the theorem we genuinely need

For integer b≥2, normality of a real α to base b means that each finite length-k base-b digit word occurs with limiting frequency b^(−k). This is equivalent to uniform distribution mod 1 of the orbit ({b^nα})_n. Weyl's criterion further makes it equivalent to

    ∀h∈Z\\{0}, lim_{N→∞} (1/N)Σ_{n=0}^{N−1} exp(2π i h b^n α) = 0.       (W)

For α=π this cancellation is **OPEN for every base**. Density of spatial angles, polygon symmetry, irrationality, transcendence, computability, probability-one normality of generic α, or mixing of Haar-typical orbits do not establish (W) for the source-selected orbit α=π. An upper bound tending to zero, derived for all N and every fixed h using source-specific information, would do so. For example |Σ_{n<N}exp(2πihb^nπ)|≤C_h N^(1−δ_h), with δ_h>0, is stronger than needed; even genuine o(N) suffices.

### Existing SUCC results are valuable but insufficient

[POL-01–09](../../docs/CLAIM_SUPPLEMENT_PI_POLYGON_NORMALITY.md) provide exact circle→π rational polygon intervals, a Lipschitz transport estimate between a π-orbit and a finite midpoint orbit, a noncommutation of spatial and orbit limits, and explicit exceptional paths in a balanced polygon inverse limit. Main VIII repaired floating underflow and the false identification of ideal geometric widths with finite-precision outward enclosures: [audit](MAIN_VIII_SOURCE_PI_AUDIT.md).

**Exact precision frontier:** for a midpoint y_N of a certified rational bracket [L_N,U_N] for π and a periodic L-Lipschitz observable F,

    |(1/N)Σ F(b^jπ) − (1/N)Σ F(b^j y_N)|
      ≤ L (U_N−L_N)/2 · (b^N−1)/(N(b−1)).

If one separately proves uniform-in-N cancellation of the *approximant* Fourier means while the right side tends to zero, (W) follows. This is a **conditional reduction** already essentially POL-07. A bracket of width O(m^(−2)) therefore requires m increasing exponentially with N to control the expanding dynamics; arbitrary precision *per N* supplies no o(N) bound on the approximant orbit. Rational midpoints alone remain eventually periodic.

**Prioritized missing lemma:** a source-sensitive, globally quantified cancellation bound for the exact π-orbit or an equidistribution theorem for a *genuinely equivalent π-specific orbit*, **not** merely a finite certificate for a chosen N.

## 4. The strongest concrete existing route: Bailey–Crandall / BBP

D. H. Bailey and R. E. Crandall, *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10 (2001), 175–190, DOI 10.1080/10586458.2001.10504441, preprint https://www.davidhbailey.com/dhbpapers/bcrandom.pdf, develop a direct dynamical criterion and an explicit Hypothesis A.

The BBP formula gives

    π = Σ_{n=0}^∞ 16^(−n) ·
        [4/(8n+1) − 2/(8n+4) − 1/(8n+5) − 1/(8n+6)].

Their specific **π iteration**, with x_0=0, is

    x_n = {16x_(n−1) + r(n)},     n≥1,
    r(n) = (120n² − 89n + 16) /
           (512n⁴ − 1024n³ + 712n² − 206n + 21).

The cited paper states: if this sequence is equidistributed in [0,1), then π is normal to base 16, hence base 2. The paper also formulates general Hypothesis A asserting a finite attractor or equidistribution for a family of rationally forced recurrences, and derives the conditional base-2 normality of π. **Hypothesis A is not established in the needed generality.**

**Important:** 16-normal ⇒ 2-normal; it does NOT establish 10-normality or absolute normality. Every target base must retain its quantifier and its own compatible route.

A productive precision programme:
1. Recover the BBP identity, prove denominator nonvanishing and exact coefficient/index transport, and prove the orbit/series tail relation with uniform error estimates.
2. Formalize the transfer of equidistribution under a circle-distance error →0, then the standard equivalence between equidistribution of {b^nα} and normality in base b.
3. Obtain or falsify a source-specific bound on the BBP orbit's discrepancy or Fourier sums; distinguish conditional results from solving the input.
4. Compare the actual BBP recurrence to SUCC's circle/successor transport and prime clock representations by genuine commuting diagrams. The forced term r(n) is NONAUTONOMOUS; an unjustified autonomous factor is a category error.
5. Use artificial and known-normal controls, plus rational/irrational non-normal controls, to test whether the proposed instrument discriminates real arithmetic structure from convenient uniform averages.

**Do not** use a guessed unique stationary measure or generic chaoticity of x→16x mod1 to certify this single forced orbit. This is exactly where a Duck-style resemblance needs a separating probe.

## 5. Geometry → Γ → ζ / prime jets → base-b words: the proposed bridge

We retain the user's preferred discovery route:

    Euclidean circle/nested SUCC polygons
      → π and Archimedean normalization
      → Γ / Wallis / factorial geometry
      → zeta completed source + genuine Euler prime-power coefficients
      → source-sensitive transfer across prime clocks
      → {b^nπ} Fourier sums / BBP orbit
      → base-b normality.

This is a **research dependency graph**, not an established implication chain.

The Wallis product and Γ functional equation are mathematical giants for the first stages; [mathlib Wallis](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Pi/Wallis.html) is a real theorem available for reuse. Tate's thesis / Poisson summation, the completed ζ/Gamma factor, the Euler product on its convergence domain, and explicit-formula machinery supply rigorous prime/Archimedean interfaces. SUCC already has many such source-typed pieces. **But the resulting analytic identities are not known to control the lacunary π-digit orbit.** An exact, source-derived bridge that produces a fresh nontrivial estimate for (W) is mandatory. Merely inserting Γ and the primes into a diagram does not improve (W).

Separate three source states:
- **Classical identity imported:** Γ(1/2)=√π, Wallis, standard completed ζ and Euler factors, and the BBP formula, with precise conventions and proof obligations.
- **New SUCC diagram:** source-indexed map comparing these with digit dynamics; currently CONJECTURED until its squares and test domains are proved.
- **Desired genuinely new theorem:** a nontrivial, π-specific exponential-sum estimate (or a different equivalent normality criterion) derived without assuming normality itself.

## 6. RH and ABC are legal conjectural inputs, not free normality certificates

RH and integer ABC are unproved. There is **no established implication here from RH alone or ABC alone to π normality**, nor is ABC generally known to imply RH. Treat them as named assumptions in *distinct* proof environments:

    T_RH : RH → π-normal-base-16
    T_ABC : ABC → π-normal-base-16
    T_BOTH : RH ∧ ABC → π-normal-base-16.

None is established by stating the arrow or introducing an equivalent named axiom. For each, demand a genuinely new, proven **transport lemma** that converts the stated hypothesis into a π-specific Fourier/discrepancy bound. Identify exactly where prime-counting or Diophantine-height estimates enter and why they control the sequence 16^nπ modulo 1. A result that merely says RH ∧ (π orbit equidistributed) → π normal is a formal tautology relative to the target and not a proof of the sought implication. Keep RH/ABC normality lanes separate from unconditional SUCC proof infrastructure.

If all valid routes fail, certify the largest true intermediate theorem and the precise missing inequality, not an invented proof.

## 7. Stand on established giants *operationally*

| Giant / machinery | Licensed mathematical service | Necessary SUCC proof debt |
| --- | --- | --- |
| Yoneda lemma and observational equivalence / Myhill–Nerode | reconstruct fully probed represented structure; build minimal observable quotients | restrict contexts honestly; never infer underlying source identity from a coarse Hom/test family |
| Semiconjugacy, symbolic dynamics, Markov partitions | transport orbit properties through commuting maps | prove map onto, measure/exceptional-orbit conditions; dynamics must actually commute |
| Weyl equidistribution criterion, Fourier analysis, discrepancy | reduce base-b normality to explicit sums | show *π-specific* o(N) cancellation; quantitative inequalities must be valid at all N |
| Bailey–Crandall (2001), BBP / digit extraction | concrete equivalence/reduction for hexadecimal π digits | prove forced-orbit equidistribution or a strong enough Fourier/discrepancy estimate |
| Borel and ergodic theory | establish a.e. normality and measure-theoretic baseline | a.e. result does not identify π's orbit |
| Wallis / Γ, theta/Mellin, Tate, Euler product | connect archimedean and finite arithmetic source identities | construct justified map to lacunary digit dynamics, not a vocabulary association |
| RH/ABC and sharp prime/distribution methods | possible conditional estimates in source-specific lanes | exhibit the NEW inequality transferring these hypotheses to the desired orbit; no known automatic implication |
| Lean 4/mathlib and independent kernel audit | certify definitions, quantifiers, finite lemmas and conditional implications | compile real proof, inspect axioms, test mutants, check source-to-spec correspondence |

One potentially useful hostile comparison is Adamczewski–Bugeaud's work on combinatorial complexity of algebraic numbers (Annals 165, 2007): its result is about irrational **algebraic** numbers and cannot be transferred to transcendental π without a new argument. The complexity, automata and entropy lenses are nevertheless useful as **candidate probes**, not evidence of normality.

## 8. Trusted-kernel transition: proof-first acceptance criteria

**Policy change proposed for future work (this dossier does not change global repository policy by itself):** any new foundational definition, universal arrow, theorem, or proposed π implication becomes PROOF-DEBT until its strongest stated proposition has passed its intended proof authority. Expository diagrams remain hypotheses until mathematical maps are certified.

1. For each theorem: exact Lean type, source of assumptions, theorem name, mathlib/Lean version, proof compile log, #print axioms, source commit and digest, and correspondence to the paper statement. No syntactic imitation of the theorem via an unproved parameter.
2. Preserve distinction **PAPER_PROVED / LEAN_KERNEL_PROVED / EXACT_FINITE_CHECK / TESTED_MODEL / UNVERIFIED / REFUTED**. The exact finite-action Duck source compiled in pinned Lean CI with proof-dependency introspection (run 39605851189); deeper system-specific and π claims still need separate proofs.
3. No sorry, admit, unsafe proof authority, undeclared axioms, trust_me, or native_decide substitution for proof. Imported classical axioms must be listed rather than pretended absent.
4. Keep original-source provenance, non-Euler/fake-composite controls, and matched null tests; a proof using zero positions as inputs must not become an RH result.
5. Make the *claim dependency DAG* executable: an unproved lemma blocks its descendants' promotion, regardless of how many tests pass.
6. Run all repository policy checks and both source-specific and combined tests before proposing a main integration. Avoid altering frozen receipts or unrelated historical archives.
7. Current milestone: one tiny trusted Duck kernel and one accurate, type-correct **π normality conjecture statement** with genuinely discharged lower-level reductions. An unproved normality statement in Lean is progress only when it is labeled a statement, not a theorem.

## 9. Proof-frontier ledger / prioritized probes

| ID | Hypothesis or test | Predicted success | Failure / negative control | Status |
| --- | --- | --- | --- | --- |
| DUCK-01 | proposed factor q commutes with every declared action | all finite words transported | one failed action square | LEAN_KERNEL_PROVED, CI run 39605851189 |
| DUCK-02 | target probe is state-separating and one-step reports agree | factor law follows | erasing readout; target aliasing | LEAN_KERNEL_PROVED, CI run 39605851189 |
| DUCK-03 | candidate factor fails, target word probes separate | finite separating word exists | no separating probes ⇒ dark pair | LEAN_KERNEL_PROVED, CI run 39605851189 |
| DUCK-04 | logistic map is a factor of circle doubling | exact sin double-angle diagram | inverse/conjugacy claim false | classical proof, not Lean |
| PI-DUCK-01 | Bailey–Crandall BBP orbit equals π digit orbit asymptotically | quantified orbit-distance→0 and equidistribution equivalence | wrong indexing, denominator zeros, missing tail | classical source, local formalization TODO |
| PI-DUCK-02 | polygon precision controls all infinite-digit tests | uniform N cancellation from precision schedule | POL-02/05/08, finite-stage nonnormal rational | UNVERIFIED; naive form refuted |
| PI-DUCK-03 | Γ/prime source entails a π-specific bound (W) | new o(N) theorem on 16^nπ | same property on fake sources / generic numbers | CONJECTURED; missing bridge |
| PI-DUCK-04 | RH or ABC alone implies π-base-16 normality | separately proven hypothesis→(W) implication | circular auxiliary assumption equivalent to normality | UNVERIFIED; not a known consequence |
| PI-DUCK-05 | 16-normal implies 2-normal, and maybe 10-normal | 2-normal follows | 10-normal not established by this implication | classical first assertion; false automatic transfer to base 10 |

**Next verdict-changing experiments:** (i) complete all-declaration axiom audit and mutation controls for the now-compiled Duck kernel; (ii) build a faithful formal Bailey–Crandall recurrence with exact coefficient proofs and a tail estimate; (iii) construct a new analytic/probe input yielding even a nontrivial bound on its Fourier sums; (iv) test against rational, deliberately biased irrational, known-normal, and fake-Euler source controls; (v) only then attempt RH/ABC as supporting hypotheses, never as magical force fields.

## Sources and explicit scope

- Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions* (2001), DOI https://doi.org/10.1080/10586458.2001.10504441; author preprint https://www.davidhbailey.com/dhbpapers/bcrandom.pdf, especially Hypothesis A and Theorem 1.1; conditional.
- Bailey's account of recurrence and normality criterion: https://www.davidhbailey.com/dhbtalks/dhb-normal-nonnormal.pdf.
- Mathlib primary library source on π: https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Analysis/SpecialFunctions/Trigonometric/Basic.lean; irrational π: https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Analysis/Real/Pi/Irrational.lean; Wallis: https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Pi/Wallis.html.
- Adamczewski–Bugeaud, Annals 165 (2007), https://annals.math.princeton.edu/2007/165-2/p04. Scope: algebraic irrationals, **not π**.
- SUCC's original POL dossier and Main VIII [source/pi audit](MAIN_VIII_SOURCE_PI_AUDIT.md) determine source-derived existing achievements and limitations. No imported paper's author is claimed to endorse SUCC's proposed extensions.


## 10. Exact source-derived Bailey–Crandall tail lemma (paper proof; Lean TODO)

The π recurrence admits a useful **unconditional, explicit** orbit-transport bound—stronger than merely saying its BBP tail vanishes. This bound is elementary and must not be mistaken for a Fourier cancellation theorem.

Write, for every integer m≥1,

    r(m) = 4/(8m−7) − 2/(8m−4) − 1/(8m−3) − 1/(8m−2)
         = (120m²−89m+16) /
           [(2m−1)(4m−1)(8m−7)(8m−3)].

The numerator is positive since m²≥m and

    120m²−89m+16 ≥ 31m+16 >0.

All denominator factors are positive, and

    2m−1≥m, 4m−1≥3m, 8m−7≥m, 8m−3≥5m.

Thus the denominator is at least 15m⁴. The numerator is at most 120m², so

    0 < r(m) ≤ 8/m².                                            (TAIL-1)

The BBP identity with the n-index shifted gives

    π/16 = Σ_{m=1}^∞ 16^(−m)r(m).

Let x_0=0, x_n={16x_(n−1)+r(n)} and let

    t_n = Σ_{k=1}^∞16^(−k)r(n+k).

Exactly (modulo 1),

    {16^(n−1)π} = {x_n+t_n}.

Since every term is positive, for n≥1 the ordinary tail and the circle distance obey

    0 < t_n ≤ Σ_{k=1}^∞16^(−k)·8/(n+k)²
            ≤ 8/[15(n+1)²],                                   (TAIL-2)

    d_circle(x_n,{16^(n−1)π}) ≤ 8/[15(n+1)²].                   (TAIL-3)

(The geometric series Σ_{k≥1}16^(−k)=1/15 is exact.) Therefore the specific forced orbit and the base-16 π-digit orbit are pointwise asymptotic on R/Z. Continuous circle observables have asymptotically equal Cesàro averages by uniform continuity and a finite-prefix/tail split, yielding the **equidistribution equivalence** underlying Bailey–Crandall's classical criterion.

**Proof status:** TAIL-1–3 are direct paper derivations using the established BBP identity, not yet Lean formalizations. Their numeric constant is not claimed optimal; their academic novelty is not asserted. They furnish precise first Lean targets: prove the rational polynomial identity and inequalities, then the convergent series and circle-distance estimate. Critically, an O(n^(−2)) **distance between two orbits** does not establish that either orbit is equidistributed. The remaining normality debt is a global π-specific cancellation theorem.
