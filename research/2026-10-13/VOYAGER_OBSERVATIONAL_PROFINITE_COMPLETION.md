# VOYAGER — an observational completion theorem, a source-realization no-go, and unbounded finite-horizon memory debt

**Checkpoint:** 2026-10-13. **Stack:** original-source SUCC → EODCS I PR #44 → causal/Nerode EODCS II PR #46 → support-valued EODCS III PR #47 → **draft PR #48** on research/voyager-observational-profinite-completion-2026-10-13, initial parent b17c357e2aa6aee17ae87115b8620a51a262e1fc.

**Question:** When can an observer reconstruct a single source from an entire compatible tower of finite observations? What if every finite tower level is realizable, but different levels may demand different original source states? How does source complexity constrain the resolution frontier?

**Steelman:** The observer should be permitted to reason mathematically about an ideal all-future report, but not to claim it has physically executed infinitely many observations, that a formally compatible ideal state belongs to its original carrier, or that unknown source completeness/compactness is automatic. The desired theorem must survive *both* positive finite-source models and hostile nonclosed-source models.

**Verdict preview:** There are TWO distinct completions: (i) a mathematical completion of observable profiles under every finite probe and (ii) a proof that one genuine original source realizes an ideal profile. The first always exists in the finite-alphabet inverse-system setting; the second needs source-completeness/closedness/compactness. A finite exact source class has a certified finite-refutation dichotomy. An unbounded family of finite machines can fake every finite initial trace of an intrinsically non-ultimately-periodic sequence. These are classical automata/coalgebra/compactness ingredients, assembled in a newly source-typed SUCC implementation. **Independent mathematical priority is not established.**

## V0. Inventory and preserved countermodels

The prior stack already supports source-typed observations, causal updates, exact finite proof-support transport, finite stationary Nerode stabilization, set-valued source transitions, action-congruence darkness, holonomy/descent and Bayesian coupling uncertainty. The EODCS III baseline has green Python 3.10/3.13, full repository CI and Lean kernel checks at exact commit b17c357e2aa6aee17ae87115b8620a51a262e1fc. Main remains separate. No prior RH failure or archive is rewritten. This VOYAGER branch adds only source-type-specific mathematical modules, proof files, tests, frozen receipts and claims.

## V1. Universal full behavioral trace (CLASSICAL / LEAN-KERNEL PROVED)

Let S be a source state set, A an alphabet of **authorized** deterministic interventions, U_a:S→S the source dynamics and q:S→O the permitted original-state readout. For a finite action word w=a1...ak, U_w performs those actions in order. Define the full behavioral trace

\[
\Phi:S\longrightarrow O^{A^*},\qquad
\Phi(s)(w)=q(U_w(s)).
\]

The operation w is a *mathematical query context*. No physical right to reset a single carrier to evaluate every w is implied. An actual feasible policy and probe menu must be audited separately.

**Causal shift law:** for any a,w, \(\Phi(U_a(s))(w)=\Phi(s)(aw)\). The full trace kernel is an action congruence: if \(\Phi(s)=\Phi(t)\), then \(\Phi(U_a(s))=\Phi(U_a(t))\). Any truly source/readout-preserving morphism f that commutes with every U_a transports the entire trace naturally. These claims are proved as general Lean4 statements in formal/EODCS_VoyagerTrace.lean, independent of a finite machine bound.

**Universal observed quotient:** \(S/\ker\Phi\) is the mathematically finest equivalence-class description the authorized entire action grammar can distinguish. The map \(S/\ker\Phi\to\Phi(S)\) is a bijection, and the image inherits a lawfully shifted transition system. This is classical deterministic Moore automata / final coalgebra theory, not a new theorem priority. Names of hidden states are not recovered merely because their traces have canonical representations.

**Provenance:** all source IDs, basis versions, action menus and original readout conventions are prerequisites. A mere syntactic isomorphism between report labels does not establish actual source transport.

## V2. Projective completion of finite observational knowledge (CLASSICAL / GENERAL PROOF, NOT YET LEAN-KERNEL)

Assume O is finite and discrete. For each finite set F of authorized action words, define the finite stage
\[
 X_F=\{\Phi(s)|_F:s\in S\}\subseteq O^F.
\]
Whenever \(F\subseteq G\), the restriction \(X_G\to X_F\) is **surjective**: each finite profile in \(X_F\) came from an actual s and extends to \(\Phi(s)|_G\). The system therefore gives an inverse limit
\[
 \widehat X=\varprojlim_F X_F.
\]

**Trace-completion theorem (CLASSICAL).** There is a canonical bijection between \(\widehat X\) and the set of complete profiles \(z:A^*\to O\) such that
\[
 \forall F\subseteq A^*\ \text{finite},\quad
 \exists s_F\in S:\ \Phi(s_F)|_F=z|_F.
 \tag{V2}
\]
A compatible inverse-limit family determines z by its singleton coordinates; compatibility makes each X_F-coordinate equal to z|_F. Conversely, each finitely compatible z determines a compatible family. The actual map \(S\to\widehat X\) sends s to all its restrictions.

Give \(O^{A^*}\) the product topology. Finite-cylinder sets form a base. Thus V2 is exactly the characterization of the topological closure \(\overline{\Phi(S)}\). Therefore
\[
\boxed{\widehat X\ \cong\ \overline{\Phi(S)}}.
\]
Because O is finite discrete, \(\widehat X\) is a closed subspace of a compact Hausdorff product (a profinite space), with \(\Phi(S)\) dense. This is a structural theorem about finite-compatible *possible observational reports*, not a property of the physical original carrier.

**Source-actualization gate:**
\[
 S\to\widehat X\ \text{surjective}
 \quad\Longleftrightarrow\quad
 \Phi(S)\ \text{closed in }O^{A^*}.
 \tag{V2a}
\]
If S is finite, its image is finite hence closed. More generally, if S is a compact topological source and every \(s\mapsto q(U_w(s))\) is continuous into finite-discrete O, \(\Phi(S)\) is compact hence closed; then every finitely compatible profile has an original-state realizer. No free-standing appeal to the label "physical" or "quantum" supplies this compactness/continuity.

The fully general topological theorem is an established result from inverse-limit/Stone/profinite theory; it is *proved in mathematics and described here*, but **not** yet translated entirely into the local Lean files. Do not reclassify a software finite-image assertion as its kernel proof.

## V3. Finitary compactness with a quantitative finite refutation (CLASSICAL / LEAN-KERNEL PROVED)

Let an original source set S be exhausted by a supplied finite list of N source states. Let W be *any* set of authorized probe contexts, q_s:W→O each state's mathematical report, and z:W→O a proposed completed profile.

**Finite-refutation theorem:** Exactly one of the following possibilities holds:
- A single source state s satisfies q_s(w)=z(w) for every w∈W.
- For each listed source s, one can choose a finite probe \(w_s\) with \(q_s(w_s)\ne z(w_s)\). The collected list of at most N probes refutes ALL sources simultaneously.

This is a finite-list exhaustive-source theorem; probes may require arbitrarily expensive experiments, and the lemma does not assert that the carrier physically survives them. Completeness of the source list is a mathematical premise and must not be inferred from a tested sample.

**Proof:** If no source state realizes all z, each source has at least one mismatching w; collect one per enumerated state. Conversely, if *every finite family* of probes has some single source reproducing z on that family, the refuting family is impossible, so some one source realizes z globally.

Both sides—including existence of a refuting probe list of length N by one witness per state—are Lean 4.14 kernel-checked without mathlib in formal/EODCS_VoyagerTrace.lean. **Effectivity caveat:** the Lean proof uses `Classical.choose` to select a mismatching probe for each nonrealizing source; the abstract theorem gives finite **existence**, not an algorithm or time bound unless W, source evaluations, and a suitable search are independently computable. For the power-two pulse case the code separately provides an executable explicit witness formula. This also gives a precise repair to claims that every finite agreement merely approximates an impossible ideal: under a **complete finite original source**, compatible observations DO imply original realization.

**Scope trap:** N is a bound on the NUMBER of probes in the certificate, not their action-word lengths or executable costs, and not a theorem about an unknown infinite S.

## V4. A fully explicit nonactualized ideal profile (CLASSICAL / LEAN-KERNEL REFUTATION)

Let the original source class S consist of all binary streams \(x:\mathbb N\to\{0,1\}\) that are EVENTUALLY ZERO:
\[
 \exists N\quad\forall n\ge N,\ x(n)=0.
\]
The permitted instrument reads x(0), and the lawful source successor shifts the sequence left: \(U(x)(n)=x(n+1)\). S is closed under that successor. Its full future trace is just x itself.

Consider the ideal profile \(z(n)=1\) for every n. For **any finite observation horizon h**, the original eventual-zero source
\[
 s_h(n)=\begin{cases}1&n<h\\0&n\ge h\end{cases}
\]
reproduces exactly the first h outputs of z. In fact, for **any arbitrary finite list** of requested times F, the finite source \(s_F(n)=1\) for n∈F and 0 otherwise reproduces all reports in F.

But no eventual-zero stream equals z globally: beyond its source-specific cutoff, one of its reports is zero. Thus
\[
 \boxed{
  \forall F\text{ finite}\ \exists s_F\in S:\Phi(s_F)|_F=z|_F,
  \quad\text{but}\quad
  \nexists s\in S:\Phi(s)=z.
 }
 \tag{V4}
\]
The first quantifier depends on F; it cannot be exchanged with the second to invent one original s. The **strong arbitrary-finite-family** version and source-closure under shift were formalized in formal/EODCS_VoyagerPhantom.lean, subject to the exact Lean CI checkpoint.

As a positive mutation control, the one-state automaton outputting 1 forever DOES realize z in the larger class of unrestricted finite-state machines. V4 refutes original-source realization for this specific eventually-zero class, not the existence of every conceivable model of the infinite word. Mistaking that distinction would create a false theorem.

**Topological interpretation:** the eventual-zero streams form a dense, proper, nonclosed subset of the Cantor space \(\{0,1\}^{\mathbb N}\). Every finite binary prefix occurs in S, so \(X_h=\{0,1\}^h\) for each finite horizon h; their inverse limit is the full Cantor space. The profile z belongs to that mathematical completion, not S.

## V5. Arbitrary unbounded finite-state models cannot be globally certified from a finite prefix (CLASSICAL / CONSTRUCTIVE)

The previous V4 source class was narrow. To make a stronger operational obstruction, consider the infinite binary profile
\[
 u(n)=1\iff n=2^k\text{ for some }k\ge 0.
 \tag{V5}
\]

**Lemma: every fixed finite deterministic stationary machine outputs an ultimately periodic infinite trace.** Its finite set of states forces a repeated state along any infinite original-source orbit, after which deterministic evolution repeats a cycle. If it has at most N states, a repeated state occurs among its first N+1 orbit positions. Its report becomes periodic after some preperiod μ with positive period p.

**Lemma: u is NOT ultimately periodic.** Given any proposed μ≥0 and p≥1, select \(q=2^k>\max(\mu,p)\). Then u(q)=1 while \(q<q+p<2q\), so u(q+p)=0. This explicitly contradicts an allegedly valid period. In \`power_two_period_refutation\`, q and q+p are exact finite integer witnesses for every candidate μ,p; the generality rests on the elementary power-of-two gap argument, not on checking finitely many candidates.

**Consequence:** No one fixed finite deterministic stationary machine realizes the entire u profile.

**BUT** for every h, the completely ordinary \((h+1)\)-state chain that outputs the first h bits of u and then 0 forever realizes its entire finite observed prefix. Therefore, with NO declared bound on original-source state count, finite binary observation histories cannot refute the rival model class "some finite deterministic machine generates these observations." The mathematical source of the profile u is a separate infinite-shift object. This is a source-model-class and observational identifiability no-go, not a claim that a particular observer cannot *prove* nonperiodicity by pure mathematical reasoning about a supplied formula.

## V6. Quantitative *finite* source memory debt (CLASSICAL / LEAN-KERNEL PROVED)

There is a finite-horizon lower bound, substantially stronger than the qualitative nonperiodicity argument.

**No-repeat gap theorem:** Let (S,U,q) be ANY stationary deterministic source, with Boolean q. Suppose for integers a<b the observed output q(U^t(s))=0 at every t in [a,b), and q(U^b(s))=1. Then the source states at times t=a,a+1,...,b are **pairwise distinct**.

**Proof:** If two source states at i<j in this interval coincided, determinism would force their successors to agree after the same number of steps k=b−j. The output at time j+k=b is 1, while the output at earlier time i+k lies in [a,b), where it is 0. Contradiction. The final endpoint differs from the earlier zero-output states immediately.

Take a=2^k+1, b=2^(k+1) for V5. The interval has b−a+1=2^k time positions, so any source matching the observed finite pulse word through time 2^(k+1) has at least
\[
 \boxed{N_\mathrm{states}\ \ge\ 2^k.}\tag{V6}
\]
The map from the finite index type Fin(2^k) to these source states is injective. \`formal/EODCS_VoyagerMemoryDebt.lean\` kernel-checks the *general* no-repeat gap theorem and injectivity with explicit deterministic-source premises. The instantiation to powers of two uses the elementary finite pulse pattern. The cardinal lower bound follows by finite pigeonhole. This is genuinely finite observation-to-source complexity: no ideal infinite trace, postulated probabilistic confidence or guessed internal topology is involved.

The Python controlled family verifies k=1..7; certified state lower bounds 2,4,8,16,32,64,128 at horizons 5,9,17,33,65,129,257. These finite tests are independent oracles/receipts, not universal proofs. The underlying theorem's statement is universally quantified and Lean-checked.

**Caution:** The source must be deterministic/stationary and its original observable output sequence must really contain the stipulated gap. A noisy, resettable, nonstationary or hidden-state-incomplete carrier requires different laws; the code rejects mutated gaps rather than smuggling the same lower bound into them.

## V7. The observational resolution metric (CLASSICAL / EXACT FINITE TESTS)

For distinct binary streams x,y, let \(d(x,y)=2^{-k}\) where k is their first differing index; let d(x,x)=0. This is the standard first-difference ultrametric. Equality through horizon h guarantees only d≤2^(-h), not d=0.

An exact finite truncated implementation takes typed equal-length binary prefixes and returns Fraction(1,2**k) on the first difference or 0 for identical prefixes. All 32^3 ordered triples of five-bit finite profiles were checked against the ultrametric triangle inequality, symmetry and separation at the finite level.

**Epistemic use:** the metric expresses **resolution** under legal finite report contexts. It is not a posterior probability that two ontologies are equal and cannot by itself settle original-source actualization. A sequence of actual source profiles can be Cauchy/convergent in observational topology while escaping the original nonclosed source class, as in V4.

## V8. Cross-domain transport and genuine theorem boundaries

The previous GF/EODCS research already discovered new mathematical representations by repairs: finite typed functors, source-conditional categorical pullbacks, nonflat connections, minimal holonomy covers, generated experiments, observer-congruence quotients, set-valued modal MAY/COMMON bounds. VOYAGER gives these mechanisms a **common host surface**: actual source histories map into compatible families of finite-context outputs, source-preserving morphisms commute with that image, and observational completion is a separate object that might add ideal nonactualized threads.

This yields a rigorous three-way obstruction classification:
1. **Pathway/probe gap:** the observer lacks a separating context in its declared toolkit; enlarge the toolkit with a legitimately source-backed action.
2. **Source-realization gap:** each finite reported profile is possible but their mathematically compatible whole is not realized in the original source class; audit closure/compactness/physical preparation.
3. **Complexity debt:** finite source candidates may explain a prefix, but the required state/memory budget increases with horizon; impose a genuine state cap to obtain a finite refutation.

These axes are independent of Bayesian posterior width or tool-relative darkness. The framework's κ/contact, φ/probe-relative indistinguishability, σ/source completeness, μ/instrument availability, ρ/identity coupling and causal backaction cannot be collapsed into one confidence score.

**RH firewall:** No finite-prefix positivity, prime analogue, or abstract inverse-limit identification demonstrates the completed Weil/Suzuki form is source-derived and positive. Compactness of a mathematical test-function/profile space, where true, does not by itself imply RH; analytic/archimedean Gamma terms, Euler multiplicativity, half-density normalization, valid topological test domains and genuinely new sign mechanisms remain load-bearing missing ingredients.

## V9. Falsification, reproducibility and actual scopes

**Lean 4.14 kernel modules:**
- \`formal/EODCS_VoyagerTrace.lean\`: legal action-word trace shift/naturality; congruence; finite-N refuting-probe dichotomy and finite-compatibility original realization.
- \`formal/EODCS_VoyagerPhantom.lean\`: actual eventual-zero source closure under shift, all-ones finite-horizon witnesses, arbitrary finite-index probes matched by an eventually-zero source and no global realization.
- \`formal/EODCS_VoyagerMemoryDebt.lean\`: deterministic later-output repeat lemma; no repeated source states across a zero-to-one gap; injective Fin(p) state sequence.

**Source runtime modules:** \`observational_succ/voyager_profinite_frontier.py\`, \`scripts/voyager_observer_probe.py\`; independent hostile source tests \`tests/test_eodcs_voyager_profinite.py\` and frozen receipt test. Execute \`python -m unittest discover -s tests -p 'test_eodcs_*.py'\`, \`python scripts/voyager_observer_probe.py\` and mandatory full \`AGENTS.md\` suite. New CI globs include the Voyager branch, pin Lean 4.14 and replay the saved receipt byte-for-byte on Python 3.10 and 3.13.

**Executed data scope:** 126 dedicated tests per Python 3.10 and 3.13 passed at the pre-frozen checkpoint; 125 random complete finite sources with projection-surjectivity checks; 170 independently seeded machine-cycle test tables; 85 machine-wise constructive profile-refutation checks; 250+ independently sampled eventual-period mutants; all binary source prefixes through length ten and their stage projections; 32^3 exact dyadic ultrametric triples; k=1..7 pulse memory debt and typed invalid source/probe mutations. The exact cross-version saved JSON receipt was taken from actual successful CI logs; check *the final pushed SHA* before promoting these to final status.

**Limits:** pen-and-paper general V2/topological compactness is NOT kernel-formalized; physical source-identity correctness, empirical source completeness, an independent mathematical priority claim, quantum carrier applicability, analytic smoothness and arithmetic Weil positivity all remain UNVERIFIED. Finite-source theorem is kernel-verified, not mechanically proof of all possible mathematical theorems.

## V10. Next verdict-changing Voyager probes

- **Topological proof assistant stage:** formalize the full finite inverse system and its closure/source realization iff using a pinned topology library, including the continuous compact source positive theorem and the explicit nonclosed eventual-zero negative source; keep the source-class identification honest.
- **Observation-dependent sources:** move from stationary deterministic words to state-changing/noncommuting/noisy instruments and original-source conditional histories. The right limit is of causal *histories with provenance*, not merely terminal readout strings.
- **Physical access/debt:** model one nonresettable carrier and finite probe costs. A purely simulated all-branches prefix oracle does not establish physical measurement availability; compare adaptive policy and legal reset assumptions.
- **Uniform analytic regularity:** for infinite test-function sources, construct actual topology and derive certified quantitative continuity/equicontinuity (or produce hostile counterexamples) before reporting limiting correlations/positivity.
- **Independent originality:** audit Rutten coalgebra, Myhill–Nerode, finite automata density/Stone spaces and classical inverse-limit compactness as known results; only promote new theorems after truly independent mathematics and external source tests. The current rigor resides in scoped formulation, formal verification and reproducible architecture.

## Prior mathematical sources — attribution, not validation by citation

1. J.J.M.M. Rutten, **Universal coalgebra: a theory of systems**, *Theoretical Computer Science* 249 (2000), 3–80; https://ir.cwi.nl/pub/48 ; DOI 10.1016/S0304-3975(00)00056-6 . Provides general coalgebraic finality/behavioral equivalence context.
2. J.J.M.M. Rutten, **Elements of Stream Calculus**, *ENTCS* 45 (2001), 358–423; DOI 10.1016/S1571-0661(04)80972-1 . Stream coinduction and behavioral derivatives.
3. Nichols & Underwood, **Algebraic Myhill–Nerode Theorems**, *Theoretical Computer Science* 412 (2011), 448–457; DOI 10.1016/j.tcs.2010.10.016 . Algebraic/coalgebraic generalizations of minimal automata and finite-index behavior.
4. Fried & Jarden, **Field Arithmetic**, 3rd ed., Springer (2008), section 1.1 inverse limits / profinite spaces; basic compact-source realization from the finite intersection property. This mathematical classical result is cited as background, not owned research.
5. Classical finite-product topology, finite intersection property, Cantor/Stone spaces, eventually periodic finite automata, pigeonhole and first-difference ultrametrics.

**Claim ledger targets:** O610–O630; every statement is to be scoped as CLASSICAL/LEAN-KERNEL, CLASSICAL/DERIVED, TESTED SIMULATOR, REFUTED WITH WITNESS or UNVERIFIED. An author's commitment, a simulator flag, a Lean test compiled once, and an independently authenticated scientific measurement are not interchangeable sources.


## V11. A true finite-probe impossibility theorem, including adaptive schedules (CLASSICAL / LEAN-KERNEL)

The previous nonrealization witness V4 used one specific target, all ones. The strengthened theorem in \`formal/EODCS_VoyagerPhantom.lean\` is **uniform over EVERY target binary stream z and EVERY finite list F of queried coordinates.**

Define two explicit mathematical streams:
\[
 x_F(n)=\begin{cases}z(n)&n\in F\\0&n\notin F,\end{cases}
 \qquad
 y_F(n)=\begin{cases}z(n)&n\in F\\1&n\notin F.\end{cases}
\]
Since F is finite, x_F eventually becomes zero and y_F eventually becomes one. Both exactly reproduce z on EVERY index in F, even if the query times are irregular and nonconsecutive. Thus:
\[
\boxed{
  \forall z\in 2^{\mathbb N}\ \forall F\subset\mathbb N\text{ finite},
  \ \exists x_F,y_F:\quad
  E(x_F),\ \neg E(y_F),\quad
  x_F|_F=y_F|_F=z|_F,
}
\]
where E(x) means x is eventually zero. The finite bound beyond F is one plus its largest queried index, and all original/source values beyond that are explicitly specified. The type-correct proof, including the existence of finite bounds from a finite list and both opposite tail properties, was kernel verified under Lean 4.14.

**Stronger topological inference (CLASSICAL):** the eventually-zero source class and its complement are BOTH dense in Cantor space. Neither class contains a finite-cylinder neighborhood, and the class-membership indicator is discontinuous at every infinite stream. No finite set of head/shift coordinate readings can certify either branch.

**Adaptive finite policy corollary:** suppose a deterministic, nonanticipatory policy chooses each next coordinate only from previously observed coordinates and outcomes and eventually terminates after finitely many queries on an actual run. The actual sequence of queried indices F is finite. Construct x_F,y_F from the same observed target z. By induction over query steps, the source alternatives give exactly the same observed response history, hence the same future actions and terminal label. Because E(x_F) and E(y_F) differ, any Boolean terminal label is false on at least one. Therefore **no everywhere-terminating finite-coordinate observation policy can correctly decide E for every binary stream** unless it uses new prior/source laws or a strictly more powerful instrument.

The Lean theorem proves the exact pointwise finite-probe statement for arbitrary F; the nonanticipatory policy corollary is a short mathematical induction with a separate source-sensitive Python implementation in \`voyager_adaptive_no_go.py\`. Python exhaustively checks all depth-two binary policies (two probe labels), 80 independently seeded history-dependent policy trees with three different report sources, repeated-coordinate consistency and forged-source mutations. The source patch is a *hypothetical alternative original stream*, not a second physical specimen actually measured. No Turing undecidability for a specific arithmetic statement, Gödel independence, or physical-instrument impossibility beyond the coordinate-query model is claimed.

The result is stronger than a mere finite-horizon statistical impossibility. It is a deterministic **logical indistinguishability under every finite legal coordinate experiment**. Classical source assumptions, not an unbounded computational score, are what determine its boundary.

## V12. The closed-source frontier is an additional *assumption*, not a free theorem

Combining V2, V3 and V11:

- If S has an **externally justified complete finite state list**, every finitely compatible report has an actual source and every nonrealizable report has ≤|S| explicit discriminating probes. A universal source report can sometimes be certified by finite reasoning.
- If S is compact with appropriate continuity and finite-discrete reports, closedness supplies global realization as a classical topological result. Compactness/continuity must be *proven about the actual source*, not about a guessed global model.
- If S is an unbounded nonclosed class, all finite reports can be consistent while a completed profile escapes S. If the target is intrinsic non-ultimately-periodic behavior, the finite machine complexity required to match prefixes can grow without a fixed source-state cap.
- If a proposition has both truth classes dense under the available finite report topology, even **adaptive finite** coordinate queries cannot decide it on every source. More precise source data, a bound, continuity or a new instrument is required.

This is a four-way useful SUCC proof-control map: finite exhaustive source, compact continuous source, nonclosed source-completion defect, and toolkit-level source-eventuality indistinguishability. None is a scalar truth probability. In the TLICA vocabulary σ/source-map adequacy, φ/toolkit-relative discriminability, μ/probe access, κ/contact and topological regularity are independent gates; the finite proofs do not collapse them into a single certification score.

**New appendix sources:** \`observational_succ/voyager_adaptive_no_go.py\`, \`tests/test_eodcs_voyager_adaptive.py\`, \`scripts/voyager_adaptive_probe.py\`, and frozen cross-version receipt when the matching CI jobs have actually run.

**Next decisive challenge:** Build the smallest multi-action source in which an observer's *own instruments change the original carrier*, then determine whether the projective-limit object should be a source of histories and allowed actions, a sheaf of preparation-dependent traces, or a causal stochastic presheaf. Test a genuine compact positive case and a noncompact no-go case with independent source producers, not only a programmer-declared simulator.
