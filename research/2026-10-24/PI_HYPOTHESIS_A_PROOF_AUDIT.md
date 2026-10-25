# Hypothesis A round: proof audits and resolved corrections

**Date:** 2026-10-24. **Parent:** #274 at
`d942c4707d750f788f39acb137a04e871a93e0a6`.
**Authority:** independent workstreams and cross-checks by agents of the same
model. This is not external refereeing or a formal proof-kernel certificate.
The source-specific statistical premises and pi normality remain OPEN.

## Reviewed proof obligations

| Dossier | Reviewer | Result and load-bearing checks |
|---|---|---|
| [Trimmed joint entropy](PI_TRIMMED_JOINT_ENTROPY.md) | Root; constructor's independent derivation | PASS. Collision chain conditions on the full history; the entropy argument uses the original consecutive window. Removing an arbitrary subset does not create stationarity. The positive tail transfers collision with sharp factor two, including wraparound. |
| [All-gain rigidity](PI_ALL_GAIN_RIGIDITY.md) | Translator | PASS. The Haar coefficient includes irrational atoms. Equality of the gain limit forces all nonzero rational atoms to vanish by comparison at zero. Fixed Q precedes the horizon limit; weak discontinuity of the infinite gain map is retained. Composite W1 constants and finite Fourier constants checked. |
| [All-length rank process](PI_ALL_RANK_OBSERVERS.md) | Root | PASS. The four-phase skew shift is stationary and ergodic. A complete block has binomial rank by coordinate-swap cancellation; proper contiguous pieces are uniform. Every window decomposes into independent pieces. The four-word witnesses are 9/128 and 7/128; full joint prefix ranks would recover the bits and are not refuted. |
| [Joint primary controls](PI_JOINT_PRIMARY_OBSERVERS.md) | Constructor | PASS. Exact full supported tuple agreement, local precision, denominator identity, general factorial schedule, proper-CRT marginal control and flat Green-tail variant checked. The initial E_0=alpha-C and the n>=2 error bound are explicit. |
| [Rational-source authentication](PI_RATIONAL_SOURCE_AUTHENTICATION.md) | Translator | PASS. One negative valuation persists on a positive-density progression. Full absolute convergence at one prime is a stronger observation. Properness eliminates integer-valued ambiguities. Neither statement proves real equidistribution. |
| [Adelic compactness boundary](PI_JOINT_ADELIC_COMPACTNESS.md) | Translator's late derivation; root | Paper deduction from classical restricted-product topology and the pinned inherited denominator theorem. Exact residue constraints from sibling #277 give a separate density proof. The real circle and finite-adelic topology are distinguished. |

## Corrections made before publication

1. A missing plus sign in the displayed trimmed KL inequality was restored.
   The proof, executable budget and subsequent terms always use addition.
2. The gain-limit formula uses the entire mass on irrational points, including
   irrational atoms. It does not identify that mass with the nonatomic mass.
3. At n=1 in the moving-prime forcing proof, it is delta_0 that vanishes;
   the full forcing difference is delta_1. The dossier now says this explicitly.
4. The generalized factorial schedule requires nonnegative integers
   `0<=m_n<=n`. The executable schedule already satisfies this domain.
5. Fixed negative valuation on a progression does not imply a constant primary
   phase there. The authentication proof uses a lower bound on nonzero phase
   distance, not constancy. An explicit varying-phase example is retained.
6. Unweighted averages of disagreement densities over larger and larger prime
   sets do not authenticate a source. The counterexample `1/(n+1)` has
   prime-p disagreement density `1/p`. Per-prime conditions or fixed positive
   summable weights have the stated stronger consequence.

These changes concern mathematical scope or wording; the twelve executable
inputs remained unchanged throughout the successful full-suite run.

## Countermodels that determine the verdict

- Even-parity and base-five sum-zero laws have uniform proper marginals but a
  nontrivial final conditional collision factor. Replacing the full joint law
  with a product of its marginals fails the declared mutation checks.
- The infinite block process has every rank law and every pair law correct,
  but retains opposite signed positional triple interactions. It refutes
  all separate rank laws as a sufficient normality premise.
- A rational short-arc ensemble has all proper CRT marginals close to uniform
  while its full real phase concentrates. This is a finite-ensemble result,
  not an authenticated BBP trajectory.
- Moving-prime histories retain all supported primary phases and all fixed
  local limits. The stronger paper variant retains every algebraic-order
  real forcing coefficient. Both introduce extra prime support and change
  the exact rational-function forcing, so neither is a counterexample to
  Hypothesis A or to the authentic source.
- The zero measure is invariant under all gains and must be excluded by an
  origin condition. A fixed finite set of gains can preserve non-Haar torsion
  grids. The finite Fourier certificate explicitly accounts for every needed
  prime divisor.
- Irrational sparse-digit constants distinguish a finite orbit attractor from
  an atomic occupation limit. Irrationality alone cannot remove the latter.

## What the audits do not promote

The trimmed criterion and all-gain criterion have proofs of sufficiency;
their actual BBP premises have no proof here. The finite measurements certify
only their stated finite quantities. No rate fitting, extrapolation, new Lean
authority, claimed scholarly priority or foundational independence result is
used to bridge that gap. See [validation](PI_HYPOTHESIS_A_VALIDATION.md).
