# Validation and authority

Pinned parent: `5f350af7808532e55d74e80c948c02bb385c6e70` (PR #403).

Executed in this directory using the copied, unchanged PR #401 bounded receipt
runner, Python 3.12.3, one numerical thread and 1024 MiB limit:

- `receipts/focused.json` / `.log`: **12 tests passed**.
- `receipts/focused_extended.json` / `.log`: **16 tests passed** after adding the Kempner calibration. The earlier 12-test receipt is preserved.
- `receipts/kempner.json` / `.log`: **36 folding-versus-Euclidean exact comparisons** and **3 entire coherent windows** passed. Shallit 1979 supplies the infinite bounded-partial-quotient authority.
- `receipts/probes.json` / `.log`: **18 fresh authentic exact Fraction windows**
  passed the preregistered distance-1/20 test; **12 sparse control rows** used
  rational interval arithmetic, with **zero ambiguous classifications**;
  **9 entire sparse windows** passed the analytic uniform distance bound.
- `receipts/oracle.json` / `.log`: separate implementation imports no primary
  probe functions. It checked **18 direct-prefix witnesses**, **4 rational
  Machin/Green intervals**, **24 exact rational-separation cases**, **9 direct
  digit-convolution budgets**, and **2 SymPy identities** (SymPy 1.12).
- `receipts/lean_checked.json` / `.log`: standalone **Lean 4.14.0** compiled
  `NoWrap.lean` successfully. The two theorem declarations report only
  `propext` and `Quot.sound`. They formalize the integer no-wrap core and its
  finite iteration, not real pi or the infinite Diophantine results.

The initial Lean attempt used the nonexistent theorem name `Int.neg_one_mul`.
It exited 1. `NoWrap.initial.lean.txt` and `receipts/lean_initial.log` preserve
that failed source and output. Replacing that simplification by the actual
core lemmas `Int.neg_mul, Int.one_mul` compiled successfully. The extra
`receipts/lean_final.log` is the immediate successful rerun; the bounded
`lean_checked` receipt then rechecked the final source. Initial metadata is
explicitly retrospective; it does not invent an unrecorded execution time.

The receipt runner is byte-identical to the inherited gamma_twist runner and
is listed as a reused input, not an independent implementation. The independent
oracle takes the primary receipt's declared first witness indices as test
inputs but recomputes each phase by a separate direct sum. It does not provide
blind data independence, and same-model derivations are not external referees.

A decimal display in sparse rows is not a certified upper endpoint. The
corresponding `energy_upper_integer` is an exact ceiling of the rational
upper bound; all slip classifications use rational endpoints.

The published Zeilberger–Zudilin result is the only outside irrationality
input for the authentic pi theorem. The endpoint countermodel additionally
uses Shallit 1979 bounded partial quotients, with its exact proof mechanism
recovered and tested. The local proof of `mu(beta_m)=m` is elementary and supplied in full.
The 2026 pi exponent claims encountered during literature search are unused.
The existing parent README seed-translation wording defect is recorded
additively in THEOREMS.md; no historical file was modified.

These checks support the declared code and proof components. They do not
prove positive-density selected dispersion, SC-06 or pi normality. Repository
wide checks and hosted CI are owned by the root campaign and must be reported
from their own receipts.
