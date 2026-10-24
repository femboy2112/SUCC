# CYC-03 / BBP four-pole source — CORRECTED audit (2026-10-24)

**The former "BBP four-pole lane CLOSED" verdict is WITHDRAWN.**
The original historical document is preserved at
[CYC03_LANE_CLOSED_HISTORICAL.md](CYC03_LANE_CLOSED_HISTORICAL.md).
The full repaired proofs appear in
[BBP_SOURCE_MEMORY_REPAIR.md](../2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md).

**π NORMALITY OPEN; RH NOT PROVED; no academic priority asserted.**

## Source-derived statements retained

1. The four forcing-index poles and their signed rational residues are
   exact. Their nonzero weighted invariants exclude a specified
   rational-function coboundary solution class, not all analytic
   cancellation methods.
2. The authentic BBP forcing has coefficient 15/64 at n^-2, and its
   backward Green tail has coefficient 1/64 at n^-2.
3. CYC-01' remains a valid source-generic conditional lag inequality.
4. The unforced T_16 fixed orbit 1/3 is a generic circle-dynamics
   negative control, but not a member of the fully authenticated
   BBP source with y0=0.
5. Finite precision and modular-resonance controls retain their scope.

## Eight corrected assertions

**R1 — Wrong carrier.** The forcing's four poles lie in the
complex time/index variable, not in the state space of circle
multiplication by 16. An artificial signed pole measure has
T_16 pushforward zero, but its Stieltjes readout is NONZERO.
There is no authenticated commuting diagram between them.

**R2 — Wrong source membership.** Retain r(n), change y0 from
zero to 1/3: the first forced state is y1=7/15, not 1/3.
The authentic y0=0 produces y1=2/15. The full π source
also has a unique bounded backward tail t0=π/16.
The original 1/3 counterexample cannot close this source lane.

**R3 — Pole residues are NOT invisible.** Their signed moments
satisfy m0=0, m1=15/64. That m1 determines the leading
forcing coefficient. A positive Green/Hausdorff kernel
g(t)/(16-t^8), g(t)=4−2t^3−t^4−t^5, reconstructs the
entire backward tail with positive Hankel Grams of all orders.
The pole source contains infinitely ranked memory.

**R4 — Invalid geometric coboundary example.** r(n)=16^-n
is an exact sequence coboundary with q(n)=16^-n/255.
It is only outside the rational-function-in-n q class.
For genuine positive RATIONAL forcing controls instead use
r_K(n)=K!/[n(n+1)...(n+K)]. Their rational pole
invariants are (1−16)^K !=0 for every K, while their
tails decay at arbitrarily high polynomial orders.

**R5 — False prime-path cost bound.** The universal statement
(2/R²) Σ_(d<R) (R−d) d_(16^d−1) <= 2(R−1)/R
is false. For actual circle source δ_(1/8), N=1,R=3,
the left side equals 4sqrt(2)/3, the claimed right
side is 4/3. The correct generic bound is
d_n<=2Ω(n), and does not imply vanishing cost.

**R6 — Quantifier order.** Fits in R at fixed N do not
numerically refute an N→∞ limit along R_N→∞. Any
frozen-N power fit is FINITE EXPERIMENT evidence only.

**R7 — Commuting maps do not authenticate π orbit symmetries.**
T_p and T_16 commute, but their action on π's empirical
measures differs from invariance under every prime p.

**R8 — Re-encoding is not a universal no-go.** Chebyshev/chord
and Fourier energies are algebraically equivalent; a NEW
source-specific inequality could still be easier to prove
in either representation. No one has proved impossibility.

## The surviving difficult theorem

For each fixed nonzero integer h, we require noncircular
source-derived cancellation of the actual signed lags

    C_d(N;π) = Σ_(j=0)^(N-1-d)
       exp(2π i h(16^d−1)16^jπ)

on a genuinely unbounded admissible two-scale horizon.
Neither positive Hankel matrices nor finite normal-looking
Fourier samples prove this. The original π-selected
normality question remains OPEN.

Authority: paper-proved source-specific positive Green
moment theorem and independent exact Fraction tests,
with no new Lean declaration or signed Weil positivity.
Companion code: observational_succ/bbp_source_memory.py,
tests/test_bbp_source_memory.py. Original false report is
preserved verbatim in the HISTORICAL file and Git history.
