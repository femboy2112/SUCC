# Validation and independent source audit

Executed from the campaign worktree; both commands exited zero:

    python3 research/2026-11-04/zero_frame_coupling/front_ad/probe.py > research/2026-11-04/zero_frame_coupling/front_ad/FINITE_RECEIPT.json
    python3 -m unittest discover -s research/2026-11-04/zero_frame_coupling/front_ad -p 'test_*.py' -v

Four focused tests passed. Exact receipt checks:

- 193 positive algebraic-series coefficients; source-jet weights and first
  residuals agree with independent Laurent/geometric-moment linear solves at
  m=1,2,3,4,7,11. The first three are inherited calibration; 4,7,11 were named
  before execution.
- 30 strictly positive exact residuals at n=1,2,13,37,83 and those six orders.
- At n=1 the exact finite differences at orders 64,128,192 are negative.
  The corresponding residuals are approximately 2.576926732, 2.818179962,
  3.514022771. The strict worsening and last value exceeding r_o(1)=47/15
  are checked as exact Fraction inequalities; the decimals are display only.
- After deriving the joint-order theorem, an additional slate was declared
  before execution: n=m=13,37,83. Each residual is strictly positive and
  smaller than the m=3 residual at the same source time. These are new
  configurations on already used times, not independent source holdouts.
- 504 exact coupled seed-rotation checks; lag-annihilator gcds; 1/7 nonresonant
  rejection; all 30 literal carry telescope identities. Seed 1/5 first differs
  from the original literal carry at step 1, despite equal absolute character
  and pair statistics.

Finite records support arithmetic and implementation, not the asymptotic
proofs. The fixed-n divergence and joint-order convergence have distinct
quantifiers, both retained. No external referee, formal kernel, full-suite or
hosted-CI status is claimed here; the coordinator owns those checks.

## Read-only audit of the coordinator's instrument

Read `../coupling_probe.py` and `../certified_phase.py`. The independent
integer-LCM recurrence correctly rescales the previous numerator when the
modulus grows; all three unwrapped sources are retained. Literal carries use
fractional previous state plus the actual signed injection. Negative H and
phase interval radius use the right sign/absolute-value conventions.

Executed a separate import audit against this front's independent source code:
`coupling_probe.states(40)` matches the original and radial Fraction streams,
all U=Y+Z identities, and all 40 original literal carries. Its twelve radial
Laurent coefficients agree with the independent geometric-moment oracle; its
jet weights at m=1,4,7,11 agree with the algebraic generating-function oracle.
The command printed `INDEPENDENT_COUPLING_SOURCE_CARRY_AND_JET_AUDIT_PASS`.

The reciprocal weight is at most 8/3; its error budget 3*CHAR_ERROR+2/OUTPUT
covers character error and component rounding. The global prefix-chord error
covers every subinterval, including the maximizing witness. Exact seed 1/5
transport is explicitly recorded; its aligned mean grid is reconstructed from
the proved identity, not a second numerical trigonometric implementation.
The raw seeded maximal intervals are separately required to overlap.
