# DUCK — Structural recognition as a theorem-producing heuristic

**Branch:** research/duck-principle-pi-proof-first-2026-10-21. **Origin:** user's 2026-10-21 mathematical "Duck Principle" intuition. **Detailed research and literature map:** [Operation DUCK → PROOF → π](../research/2026-10-21/DUCK_PRINCIPLE_AND_PI_PROOF_FRONTIER.md). **Status:** proposed new-to-SUCC research family; entries are NOT yet admitted in docs/CLAIM_NAMESPACE_REGISTRY.json. No assertions of novel mathematical priority, π normality, RH, or ABC.

**Evidence boundary:** [formal/DuckPrinciple.lean](../formal/DuckPrinciple.lean) is a standalone Lean 4.14 candidate compiled by [duck-principle-lean.yml](../.github/workflows/duck-principle-lean.yml). Its claims become LEAN_KERNEL_PROVED only after a successful actual pinned kernel job and proof-dependency audit. They are elementary finite-action facts, not proofs of a physical-source claim.

| Draft ID | Exact statement and hypotheses | Status / proof route | Falsification / boundary |
| --- | --- | --- | --- |
| DUCK-01 | A declared commuting action factor B→A transports every finite action word exactly. | CLASSICAL, paper proof by induction; Lean candidate | A single failed square kills the candidate. Without such a map resemblance is not enough. |
| DUCK-02 | Two declared action factors compose to another action factor. | CLASSICAL, paper algebra; Lean candidate | Unmatched action alphabet or source context disallows composition. |
| DUCK-03 | An injective target observation, together with equality of each observed one-step square, certifies the actual squares. | CLASSICAL, paper proof by injectivity; Lean candidate | A noninjective / erasing observer invalidates the inference. |
| DUCK-04 | If target states are distinguished by word probes of length ≤k, agreement of target-word observations of both sides of each candidate square for those words implies a factor. | CLASSICAL, paper proof by separation; Lean candidate | The finite separating-family hypothesis must itself be proved; empirical probe coverage cannot be substituted. |
| DUCK-05 | If full finite target-word probes separate target states, failure of the factor law implies existence of a distinguishing action, source state and target word. | CLASSICAL, classical existence proof; Lean candidate | No stated efficient algorithm without effective finite/equivalence assumptions; dark pairs without separation. |
| DUCK-06 | Flip-versus-idle Bool with erased Unit readout has identical readout along every finite action word but the *identity* projection is not a factor. | CLASSICAL negative model; Lean candidate | Refutes the naive "looks the same ⇒ the proposed factor exists", not all possible quotient factors. |
| DUCK-07 | D(t)=2t mod1 on R/Z factors onto L(x)=4x(1−x) via sin²(πt). | CLASSICAL, elementary double-angle identity; not Lean | Projection is generally not injective; not a conjugacy; no π digit theorem. |
| DUCK-08 | All sufficiently similar finite observations imply source identity or a nontrivial common quotient. | REFUTED AS GENERAL INFERENCE by erased and arbitrarily delayed distinguishers; restricted source category may change verdict | Constant maps give vacuous shared quotients; demand source-relevant nontriviality. |
| DUCK-09 | Existing SUCC polygon intervals and finite orbit estimates imply π is b-normal without an independent source-derived Fourier bound. | REFUTED AS INFERENCE by POL-02/05/08 | Noncommuting limits and exceptional paths survive Haar-like polygon averages. |
| DUCK-10 | Equidistribution of the specific Bailey–Crandall rationally forced base-16 π orbit implies π is normal to base 16, hence base 2. | CLASSICAL CONDITIONAL IMPORT, Bailey–Crandall (2001); not new SUCC proof | The orbit equidistribution is the open, unproved input. Not base 10. |
| DUCK-11 | RH or ABC alone entails a π-specific normality theorem. | UNVERIFIED, no supplied transfer theorem | Must derive π-specific o(N) Fourier cancellation from the named hypothesis rather than assuming a restatement of normality. |
| DUCK-12 | Construct a nontrivial, source-justified bridge circle→Γ→Euler/prime jets→base-b digit dynamics producing new global estimates. | CONJECTURED PROGRAM, not a result | Prove every square and an actual new exponential-sum estimate; test fake-Euler/composite and known nonnormal sources. |

## Status transition gate

DUCK-01–06 are sound elementary mathematical arguments at paper level but were added as **Lean candidates, not pre-certified Lean results**. Inspect actual CI logs before promoting. DUCK-07/10 are classical imports, with their distinct hypotheses. DUCK-08/09 record false general inferences, not refutations of every possible repaired construction.

No claim in this supplement permits a short-circuit of the original source record, completed Gamma/Weil forms, quantifier scope, or observational tools. The purpose is to turn creative analogy into an exact morphism + distinguishing-probe + trusted-proof loop.
