# Duck → Lean → π: execution contract

Recorded during the 21 October 2026 campaign, after its initial exploratory
calculations. This is a prospective decision record for the remaining work,
not a claim that those calculations were preregistered.

The pinned starting point is PR #232 at
`9894d39250021bbbc2615c33dee0d286ddf0950f`; main is
`b116841f12b41aaf7600da39bbb40577f25b6295`. The existing eight Duck declarations
are checked facts about declared actions on arbitrary types and finite words.
They do not authenticate a physical source or assert finite state spaces.

## Targets, dependencies and discriminating probes

| Hole | Exact desired conclusion | Independent input still owed | Decisive probe / falsifier |
|---|---|---|---|
| Observable structure | An observation-preserving commuting map descends uniquely through the behavioral quotient into a separated target. | Explicit action/readout data and the separation hypothesis. | Erasing readouts, delayed distinguishers, two- versus three-cycles; inspect the actual exported Lean type. |
| Executable recognition | A complete finite closed relation certifies agreement for every finite word; a failed finite comparison returns a shortest distinguishing word. | Kernel theorem for relation closure; separate implementation correctness for the search. | Independent exhaustive word/partition oracles and mutation of a successor/readout. |
| Authentic π transport | The exact Bailey–Crandall rational forcing shadows the base-16 orbit of `Real.pi` with a proved vanishing tail. | An analytic BBP identity identifying the sum with π, beyond the rational identity and tail theorem. | Wrong denominator, missing clock increment, wrong geometric normalization, sharp-bound violation at the first term. |
| Normality semantics | Equidistribution of the actual digit orbit implies canonical overlapping block frequencies. | Half-open cylinder identity; a separate Weyl theorem if Fourier cancellation is used as input. | Rational endpoints, zero orbit, single-digit versus all-block frequency substitutions. |
| Global cancellation | For each nonzero integer h, N⁻¹Σ_{n<N}exp(2πih16ⁿπ)→0. | A new source-specific global estimate; no generic ergodic theorem identifies this one orbit. | Positive smooth rational forcings with the same decay and noncancelling orbits; finite-prefix counterfeits. |
| Conditional prime route | Under a quantified Chebyshev error, explicitly bound the difference between π and genuine prime-power approximant Fourier means. | Imported RH implication with its exact threshold; cancellation of the approximant mean remains separately open. | Fake prime atoms, missing prime-power weights, a fixed cutoff at growing digit horizon. |

The cancellation target is not accepted as an auxiliary “geometry” or
“source-rigidity” axiom. Proving an equivalent formulation is a transport
result, not a solution of the target. Rational telescoping, scalar
approximation, and generic forcing decay are separate candidate mechanisms;
their failure does not refute π normality.

## Evidence discipline

* Universal Lean claims require a successful build of the exact source,
  exported types and inspected axiom dependencies. A Python receipt alone
  supplies no authority. New exports are not automatically admitted to the
  installed proof-authority catalogue.
* Paper arguments, imported results, conditional implications, exact finite
  certificates and exploratory computation retain separate statuses.
* Constructor and referee agents are separate investigations using the same
  model family. Algebraic cross-checks, independent algorithms and kernel
  checking are identified by mechanism; model agreement is not external review.
* Local Lean startup is blocked by this environment's process-path access
  restriction. The official hash-checked binary is executed in hosted CI;
  that restriction is not bypassed and local compilation is not claimed.
* Work advances the existing draft PR #232 after validation. Historical
  receipts and frozen source archives remain intact. No main merge is part
  of this research checkpoint.
