# X10 independent adversarial review of D27, D30 and D32

Reviewed source: cohort D `159172c63c1e426ad65420c9d1f273310c84c930`, integrated
as `e49dc2f`, against A06's order convention in cohort A
`34904661c721ea9140c5994be5ca964f4a806268`. Reviewer X10 used no cohort Python
imports. Exact arithmetic and explicitly different algorithms live in
`scripts/swarm_cross_x10_probe.py`; frozen outputs are `X10_RECEIPT.json`.

## D27 — factor, strong lumpability, and path perturbation

**SURVIVES.** For deterministic factors on arbitrary sets, indicators of report
values detect precisely whether qF is constant on q-fibers. Surjectivity onto
the specified report image is needed for uniqueness on that image. The invariant
algebra identity uses all functions on the report image, not just a small
selected feature span. X10's swapped-bit example shows that distinction matters.

For finite Markov kernels, indicator pullbacks are the projected row
probabilities. Their constancy on q-fibers is precisely strong lumpability.
Conditional hidden laws given an actual visible history stay in the current
q-fiber; averaging identical projected rows gives the same observed transition
kernel for every initial law. Conversely point masses recover every source row.
The requirement of the **same kernel K for all initial laws** is stated and
used correctly.

For the perturbation bound, let E_j mean equality of coupled visible histories
through time j. Given E_j and its common history, the actual source's conditional
next-report law is a mixture of source projected rows in the observed fiber.
Its TV distance from the candidate row is ≤δ, by convexity and the uniform
source supremum. Maximal coupling at that history gives
`P(E_(j+1)|E_j)≥1−δ` after averaging. Thus
`TV(path laws through n)≤1−(1−δ)^n≤min(1,nδ)`.
The source need not be Markov after observation. The source itself is Markov,
and the candidate is Markov; that distinction is sufficient. Initial report
laws must agree, as D27 specifies. Positive-probability conditioning suffices;
zero-probability histories can be assigned arbitrary coupling kernels.

Independent direct hidden-path expansion and aggregation verifies both bounds
in 6,912 exact cases: 64 source kernels, 9 candidate kernels, 3 point initial
laws and horizons 0 through 3. There are 24 zero-defect source/candidate pairs.
This exhaustive family is a code control, not the proof of the universal bound.

## D30 — filtered quadratic forcing survives Leray projection

**SURVIVES.** The divergence convention is `(div M)_i=Σ_j ∂_j M_ij`; the stress
is symmetric, so transposition would not alter this witness. Assign exact
velocity Fourier coefficients a/2 at ±k and b/2 at ±l, convolve them, and retain
integer frequencies of squared norm ≤1. Only 0 and ±(1,0) remain. At frequency
(1,0), the tensor coefficient is `(abᵀ+baᵀ)/4`; contracting its first column
and applying `I−eeᵀ` with e=(1,0) produces sine amplitude
`(0,(2N−1)/2)`. This has the stated sign for the displayed stress divergence;
the Navier–Stokes generator contains its negative. The linear viscosity term
vanishes after projection because the original velocity modes are all removed.

The 100 direct Fourier convolutions N=2,…,101 independently verify the report
null, divergence-free modes, retained modes and nonzero projected solenoidal
force. The theorem is local at the generator level. It does not require a
global smooth Navier–Stokes solution. Appending stress is a necessary extra
report for this witness but does not establish a closed stress evolution.

## D32 — N−1 delays and sharpness

**SURVIVES.** Let R_m compare m reports including time zero. Equality of two
successive partitions makes the current partition F-stable, including the
special case m=0 when q is constant. Before stabilization each strict step
increases block count, starting from one. After at most N−1 strict steps the
partition is discrete, proving the bound with the claimed indexing. For N=1,
D_0 is a singleton report and correctly already suffices. Sharpness applies to
N≥2; the endpoint-pulse chain first distinguishes states 0 and 1 at time N−2,
so exactly N−1 reports are needed.

Independent pair-orbit searches inspect 4,330 full source/report tables and
25,240 pairs. Each orbit either encounters unequal reports or repeats a pair;
the latter proves permanent equality for that finite table. Every finite first
separation occurs before time N−1. Chains N=2,…,16 attain time N−2. This does
not rely on D's partition algorithm or its chosen long finite delay cutoff.
The Hamming-noise criterion is the usual disjoint-ball condition; the paper's
necessity construction correctly partitions the actual disagreeing coordinates.

## One terminology issue, no mathematical counterexample to the stated theorems

D27 §9 says the trace kernel is the “finest action-congruence refinement”, and
D32 §9 says “finest future behavioral quotient”. A06's precise order convention
shows this should be the **coarsest lawful refinement**, equivalently the
**greatest stable equivalence contained in ker(q)**. Identity is always a finer
lawful equivalence. Two fixed source states with a constant report give a
concrete distinction: the trace kernel is indiscrete, while identity is the
finest refinement. The parent was informed so the wording can be corrected in
integration. The factor and delay proofs themselves use the correct direction.

## Verdict and limitations

All three load-bearing theorems survive this review with their stated source
contracts. One descriptive order-wording correction was requested. Neither
passing finite probes nor this review upgrades the results to Lean-verified,
empirically authenticated, novel, or applicable outside the listed hypotheses.
X10 contributes a separate complete algebra/repair proof and finite hierarchy
obstruction, both recorded in `X10.md`.
