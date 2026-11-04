# Operational foundations — source-labelled empirical-to-proof interface

**Research proposal, 2026-11-04.** Neither a replacement for ZFC nor an empirical derivation of quantum mechanics. Reuse existing SUCC \`docs/FOUNDATIONS.md\`, \`docs/OPERATIONAL_TRIANGLE.md\`, \`docs/PRINCIPIA_CONNECTION.md\`, \`docs/METHOD.md\`, \`contextual_zero_navigation.py\` and \`operational_yoneda_descent.py\`; do not mint a second competing category implementation.

## Objective

Start with **what a finite embodied observer may register, retain, distinguish, predict and prove**, rather than with unrestricted abstract objects. Separate three layers:

1. **Proof/typing rules:** records, source-provenance, admissible composition, finite witness transport and mathematical deduction.
2. **Empirical postulates:** contingent regularities such as persistence, stationarity, repeatability, or noise calibration; revisable when observations contradict them.
3. **Optional physical theories:** classical dynamics, probabilistic models, quantum instruments, purification, etc.; require distinguishing experiments and explicit mathematical axioms.

These are not interchangeable. A formal axiom may be useful without being an established law of nature; a recurring empirical pattern may be a good hypothesis without becoming a logical theorem.

## Exact finite instrument

Let a **declared synthetic source** be
\[
\mathcal O=(S,\mathcal A,\{r_a:S\to Y_a\},\{T_a:S\to S\},\{c_a>0\},\lambda).
\]
A state in S is a candidate **within the chosen model**, not an externally verified hidden entity. A realized action a emits readout r_a(s) and then advances to T_a(s), at cost c_a, with declared provenance λ.

For finite word w, write tr_w(s) for its chronological readouts, preserving order and transitions. For toolkit \(\mathcal T\), maximum depth k and budget b, define
\[
\mathrm{Sig}_{\mathcal T,k,b}(s)=
\{(w,\operatorname{tr}_w(s)):w\in\mathcal T^*, |w|\le k,\mathrm{cost}(w)\le b\}.
\]
Operational indistinguishability means \(\mathrm{Sig}(s)=\mathrm{Sig}(t)\).

**OF-01 — PROVED (elementary finite model):** equality of these signatures is an equivalence relation. Enlarging the toolkit, depth or budget can only refine its equivalence classes; it cannot create a new equality between previously distinguishable states.

**OF-02 — PROVED (elementary finite model):** for a fixed declared source and a realized history with readouts z, the compatible *initial* candidates \(B(w,z)=\{s:\operatorname{tr}_w(s)=z\}\) can only shrink under consistent extension of the same history. This does not assert monotonicity of **current** physical states under interventions or after revision of the source model.

These statements concern distinguishability permitted by tools, not ontological uniqueness or actual instrument calibration.

## Proposed operational principles and status

| Label | Core principle | Boundary |
|---|---|---|
| OF-P0 | **Contact must be source-labelled**: distinguish permitted action, observed result and independently attested external event | Strings and synthetic test worlds are not empirical attestation |
| OF-P1 | **Realized-history preservation**: append evidence; revise interpretation separately, not by rewriting witnessed history | Human memory/sensor errors are possible source failures |
| OF-P2 | **Typed causal composition**: lawful arrows compose associatively with identity; outcomes can depend on action order | No assumption all processes commute |
| OF-P3 | **Object identity via transport**: persistence is a documented tracking relation through intervening contexts | Repeated appearance does not prove persistence; it is a revisable empirical hypothesis |
| OF-P4 | **Toolkit-relative uncertainty**: source possibilities are equivalent only against admissible distinguishing procedures | Failure to distinguish is not a quantum uncertainty principle |
| OF-P5 | **Finite resource/precision contact**: probes have budgets, provenance, calibration, and error statements | No unrestricted or infinitely precise actual observer |
| OF-P6 | **Defeasible induction**: extrapolation needs a declared source class, regularity premise, and falsification tests | Finite history alone does not imply a universal future |
| OF-P7 | **Model repair**: contradiction must update source hypotheses, calibration or claim status | No synthetic source-map labels posing as Nature |
| OF-P8 | **Finite-to-global firewall**: general theorems need mathematical proof of quantifier transfer | No automatic ω-rule from endlessly accumulating observations |
| OF-P9 | **Physics remains optional**: Bayesian priors, Born rule, purification, locality, and noncontextuality require additional explicit assumptions | “I experience uncertainty” does not uniquely choose quantum mechanics |

This is currently an **axiom proposal** for *what the observer is licensed to claim*, not an experimentally confirmed catalogue of laws of nature.

## Hostile controls (model-relative mathematical receipts)

**C1 — Permanence is not readout identity.** Synthetic states \`original\` and \`replacement\` both produce \`red-box\` on repeated cheap \`see\` actions; a paid \`tag\` probe distinguishes them. Source identity cannot be deduced from a mere shared appearance. More toolkit access is only a *potential* refinement.

**C2 — No finite-prefix universal induction.** For any finite k, deterministic computable laws f(n)=0 and g_k(n)=0 for n≤k, g_k(n)=1 for n>k, agree throughout all observed times n≤k and diverge immediately after. A source restriction is necessary to prove all-time stationarity.

**C3 — Classical processes already fail to commute.** Deterministic classical bit writes \`write0;write1;read\` produce 1 while \`write1;write0;read\` produce 0. Measurement-order dependence is not by itself evidence for quantum physics, contextuality, or ontic randomness.

**C4 — A minimal zero is not mixing.** In the classical ×16 map x↦16x mod 1, initial x_0=0 stays 0 forever. Neither a zero initial condition nor an empty observer journal implies future statistical normality. These two zeroes are also different typed objects.

**C5 — No unperformed evidence.** Even when a finite model has a distinguishing probe, a journal earns new evidence only when it is performed and a source-attested outcome is appended. The possible test is virtual; its outcome is not already realized.

The tested \`operational_probe.py\` is an independent **calibration script** on synthetic finite processes, not a new SUCC categorical core. Eight focused tests cover these classical claims and rejection cases; this is not empirical external-world validation or independent mathematical refereeing.

## Relationship to quantum foundations

The empirical intuition that many phenomena are underobserved is a legitimate source of hypotheses. But it does not single out quantum mechanics. Operational reconstruction programs show what additional assumptions do: Hardy (2001) https://arxiv.org/abs/quant-ph/0101012 ; Chiribella, D'Ariano, Perinotti (2011) https://doi.org/10.1103/PhysRevA.84.012311 (purification is a distinct postulate). Spekkens (2005) https://doi.org/10.1103/PhysRevA.71.052108 formalizes operational contextuality and no-go conditions for certain noncontextual hidden-variable models. No general ban on every possible hidden-variable ontology is asserted.

The classical problem of induction remains: https://plato.stanford.edu/entries/induction-problem/ .

## Foundation and application boundaries

An eventual fully foundational system would need a formal judgment language, source-soundness, admissible composition, semantics, and comparison with existing type-theoretic or categorical foundations. This draft proves none of those universal claims; it can be embedded in today's mathematical metatheory without an ontological commitment that “all reality is sets.”

**π:** A selected zero seed \(U_0=0\) and an empty journal are distinct, and neither gives a source-selected Weyl saving. Normality requires a new theorem about the exact original four-pole orbit, its numerator/carry history and the real nearpair escape statistics. **RH:** Positive model covariance is not the completed signed Weil positivity criterion.

**Status:** finite observational equivalence/refinement and explicit synthetic countermodels PROVED/TESTED in the declared finite model; universal physical axiomatization, full alternative foundations, quantum reconstruction, π normality and RH **OPEN / UNVERIFIED**.
