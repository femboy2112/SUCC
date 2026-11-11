# Zero-anchored Lambda–Haar: exact hole contract and finite protocol

Date: 2026-11-10. Parent: Main XXIII integration candidate
`50481e49592af00d87c602f671a28f3503709de0` (PR #584).
The user authorizes construction, research, commits and a pushed draft PR.
This round does not merge the integration candidate or change main.

## Object and requested theorem

Keep the literal source
`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`,
`U_n=16 U_(n-1)+r(n)`, and `alpha=pi/16` through the classical BBP identity.
The completed phase is `z_n={U_n+T_n}={16^n alpha}` for `n>=0`.
Let `T(x)={16x}`, `C nu=(1/16) sum_a ((a+y)/16)_*nu`, `Q=C T_*`,
`mu_N=N^-1 sum_(n=0)^(N-1) delta_(z_n)`, and
`D_N=W1(mu_N,Q mu_N)` in the ordinary interval chart `[0,1)`.

**Requested statement, OPEN:** derive from the exact four-pole source a fixed
`0<=theta<1`, an independently specified nonnegative error `epsilon_N -> 0`,
and a threshold `N_0`, such that for every integer `N>=max(2,N_0)`,
`D_N <= theta D_floor(N/2) + epsilon_N`.

The inherited sharp theorem is
`W1(mu_N,lambda) <= 16 D_N/15 + |z_N-z_0|/(15N)`.
The requested inequality would therefore close the normality problem.
The unspecified existence of *some* error tending to zero is equivalent to
normality; this is a reformulation until an arithmetic bound on that error
is supplied. A residual fitted from the same measured defects is not such
a bound. The compiler's finite semantic preservation is a separate theorem.

## Assault and falsifiers

1. Constructor: source-specific signed descent, exact adjacent-block
   cancellation, and a transfer-operator/Poisson decomposition.
2. Adversary: seed shadows, exact-zero hostile sources, circular errors,
   observational aliasing, and false promotion of beta confluence.
3. Compiler: typed finite lambda source terms, capture-free beta plus
   explicitly declared arithmetic delta rules, exact seed and tail certificates.
4. Root: exact source-only phase enclosures, conditional Pascal observables,
   independently calibrated Wasserstein and signed-overlap measurements.

These are same-model agents with different assignments, not independent
external referees. Root reviews all claims and code before publication.

## Preregistered finite probe

The experiment is fixed before reading its resulting defect values.
Generate new exact integer BBP enclosures directly from the source, not a
pi numerical oracle or imported digits. Use start clock 0; retain 10
hexadecimal phase digits; use 16 additional source guard digits. Test
adjacent blocks of lengths `M=64,128,256,512,1024,2048,4096`.
Treat `64,128,256` as calibration and `512,1024,2048,4096` as untouched
holdouts for this specific instrument, not previously unseen pi data.

Record the exact rational ranges for `D_M`, `D_late`, `D_(2M)`, the signed
CDF overlap, and the residual `D_(2M)-theta D_M` for
`theta in {1/16,1/2,3/4}`. Do not fit a power law or infer an all-N limit.
Separately test the tempting *strong extrapolation*
`D_(2M) <= D_M/16 + 1/(15M)` at the declared lengths. This extrapolation
is not an inherited theorem or the only version of the user's conjecture.
A positive rigorous residual falsifies that specified finite inequality
at that M; it does not refute an eventual inequality with a different
threshold, error, or coefficient.

Pass/fail/ambiguous for any proposed finite upper bound means respectively
upper residual <=0, lower residual >0, or a certified interval meeting both
half-lines. Precision ambiguity must trigger refinement or remain reported.

Controls: constant-zero orbit (defect `15/32`, no overlap), uniform 16-grid
(zero Q defect but nonzero stationarity), periodic balanced digits, exact
two-point Wasserstein examples, and deliberately mutated source/seed/index/
certificate payloads. A compiler budget exhaustion is UNRESOLVED, not false.

## Boundary and next lamp

No finite sample, formal syntax identity, source hash, or contraction of
the analytic tail can certify the universal statistical error.
If the requested theorem remains open, deliver a functioning finite compiler,
proved exact identities, preserved counterexamples, all executed receipts,
and the precise original-zero signed estimate still owed.
