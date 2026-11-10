# Connection audit: finite moment memory, source arithmetic and circle geometry

Baseline: research head `525d7c87dd1016aeeea4ac9cd1366cbb935a0441`.
The following actual proofs and implementations were inspected read-only.
This is a local connection audit, not a claim of exhaustive historical or
worldwide novelty search.

| Existing SUCC object | Actual connection | What is not transported |
|---|---|---|
| [Hidden-memory Schur HM05](../../../2026-10-17/HIDDEN_MEMORY_SCHUR_AND_TEMPORAL_OBSERVERS.md) | Finite hidden modes can be reconstructed by moment recurrences; insufficient moments can conceal opposite signed targets. Known equal replica weights here make Newton recovery shorter. | No equality of Suzuki high modes and BBP phase replicas; no Schur positivity or RH theorem. |
| [Factorial Borwein hologram](../../../2026-10-19/FACTORIAL_BORWEIN_HOLOGRAPHIC_CLOCK.md) | Fourier log-sinc data encode power sums, and Newton identities recover a finite multiset. The present carrier is a circle-phase multiset with known empirical weights. | Widths are not phases; an analytic germ is not automatically an available finite sensor. |
| [Two-wire source observer](../../../../observational_succ/twisted_pair_transport.py) | Label transport is part of the observer contract; discarding labels creates a target-dependent ambiguity. Existing even-radix antiphase bounds agree with the q=2 singular locus. | No hidden phase randomization and no automatic source cancellation. |
| [Learning Yoneda LY2](../../../2026-11-07/learning_yoneda/LEARNING_THEORY.md) | Equal observations form a declared fiber; required memory depends on the target and admissible candidate family. OMC4 computes that radius explicitly for two assignments. | A two-assignment information lower bound cannot be applied to a known deterministic source with unrestricted replay. |
| [Folded source laws CBM1–2](../../complement_budget/model/THEOREMS.md) | Their actual law has known finite equal weights. OMC1–2 close its moments algebraically within that class; they do not use the invalid M16=M1^16 closure. | Exact finite support and known weights cannot be assumed for an arbitrary positive model or infinite limiting law. |
| [Quotient signal QS](../../quotient_signal/quotient/THEOREMS.md) | Both constructions separate retained signed signal from a quantified information-loss term. Here the loss is chronology under unequal forcing, bounded directly by the four poles. | A small loss does not imply a small retained signal. |
| [Root's replica energy](../ENERGY_THEOREMS.md) | The invariant unordered pair at angles +/-4/17 has mean sin(pi/34), matching the sharp even-radix energy floor. | An average energy floor cannot supply pointwise conditioning away from the antipodal chart. |

## External primary references and exact scope

- Chunaev and Safiullin, *Data fitting by exponential sums with equal weights*
  (2020), [author conference paper](https://www.iccs-meeting.org/archive/iccs2020/papers/121380353.pdf),
  section2, equations6–10: Newton power-sum reconstruction with known equal
  weights. We use the classical exact algebra, not their numerical fitting
  guarantees or a new priority claim.
- Diederichs, Kolountzakis and Papageorgiou, *How many Fourier coefficients
  are needed?* (2023), [primary paper](https://link.springer.com/article/10.1007/s00605-022-01792-0),
  section2: Newton–Girard conversion from selected Fourier/power data to
  polynomial coefficients. Their source class is not our authenticated BBP
  history. This is a related finite-observation mechanism.
- Yang and Xie, *Frequency-selective Vandermonde decomposition of Toeplitz
  matrices with applications* (2017), [primary preprint](https://arxiv.org/abs/1605.02431):
  positivity and a finite moment matrix supply another route to realizing
  finite circle measures. This paper is context for possible future positive
  moment instruments; no unimplemented Toeplitz solver or SDP result is claimed.
- Kunis, Möller and von der Ohe, *Prony's method on the sphere* (2016),
  [primary preprint](https://arxiv.org/abs/1603.02020): finite atomic recovery
  requires specified interpolation/separation hypotheses. Its abstract was
  checked as a connection lead. We do not import a stability constant from it.

The proofs in THEOREMS.md are complete elementary derivations; references
identify classical ancestry and future instruments. No literature reference
is used to waive a source-map or quantifier obligation.

## Rival claims and falsifiers

| Proposed shortcut | Receipt and verdict |
|---|---|
| One first moment never determines a multi-atom law | Too broad: two known equal unit atoms are determined when their mean is nonzero; original odd-denominator two-replica means meet that condition. |
| Arithmetic nonvanishing yields a uniformly stable decoder | REFUTED by epsilon and a*epsilon with a=(3+4i)/5; output separation stays nonzero as input separation vanishes. |
| Odd denominators make every even-replica half-moment chart nonsingular | REFUTED by angles0,0,1/3,2/3, with e2=0. |
| An unordered law always requires one extra chronology bit | REFUTED without a two-assignment fiber: the literal-zero source with unlimited replay is a singleton. Degenerate next targets also need no bit. |
| Exact moment closure forces zero signed signal | REFUTED by the invariant pair at +/-4/17 and by the coherent inverse graph. |

No arbitrary first-moment or energy control has been promoted to an
original-zero signed estimate. The latter remains the missing theorem.
