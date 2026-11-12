# Scoped claim ledger: adaptive boundary resolution

These are local research-draft identifiers. **PROVED LOCAL** means a
checkable mathematical derivation with stated assumptions, not worldwide
novelty or proof-assistant verification. **CLASSICAL IMPORT/TRANSFER**
identifies the outside arithmetic authority. **VERIFIED FINITE** refers
only to actually executed cases. All claims inherit their weakest premise.

## Integer information and movable damping

| ID | Status and exact scope | Claim and evidence | Boundary / next falsifier |
|---|---|---|---|
| II-01 | PROVED LOCAL; finite-mass nonnegative integer histograms, known exact common mass, fixed integer base `b>=2` | A packet difference is divisible in `Z[z]` by `(1-z) product_(r=1)^d(1-b^r z)`. For `d>=1`, any nonzero packet difference needs mass at least `b^[d(d+1)/2]+1`; below that the entire histogram is unique. [Proof](INTEGER_INFORMATION.md) | Arbitrary finite support is covered, but fractional counts or an omitted exact mass change the claim. No efficient full-histogram decoder is supplied. |
| II-02 | PROVED LOCAL / VERIFIED FINITE; same family | Positive/negative annihilator coefficients give zero-count twins of mass `product_(r=1)^d(b^r+1)`, within a factor below `153/64` of the sufficient uniqueness mass. [Exact witnesses](INTEGER_RESULTS.json) | The product is not an optimum: `b=2,d=2` has a smaller mass-14 witness. Exact minimum remains open. |
| II-03 | PROVED LOCAL; fixed-base prefix observation family | Worst-case zero-count channel cost is `sqrt(2 log_b M)+O_b(1)`; explicit channel bounds differ by at most one and the old even-degree rule is within two of optimum. [Proof](INTEGER_INFORMATION.md) | Not a universal bound on arbitrary or mass-dependent nodes, bit complexity, or arithmetic algorithms. |
| II-04 | PROVED LOCAL; exact known mass and deterministic coordinatewise normalized error | Explicit common noisy packets force precision of order `1/M`; an additional witness matches all but the last channel. [Proof and controls](INTEGER_INFORMATION.md) | Worst-case adversarial error, not a random-noise/statistical lower bound. Full-histogram uniqueness has no uniform high-grade stability. |
| AA01 | PROVED LOCAL; nonnegative integer grades, integral zero count, known positive integer mass bound | One node with `Ms<1` gives `c0=floor F(s)`. An authentic interval of width `w` gives unique integer recovery when `w+Ms<1`; `s=1/(4M), w<=1/2` suffices. [Proof](ADAPTIVE_APERTURE.md) | Moving the node changes access requirements. Normalization must use a known scale. Authenticating and acquiring the response remain assumptions. |
| AA02 | PROVED LOCAL; same source contract, and genuine arithmetic specialization | `(F(s)-sM)/(1-s)` is a lower certificate. Under `Ms<1` its positivity is equivalent to `c0>0`; with `M=n-1,s=1/[4(n-1)]`, the criterion is exactly `F_n(s)>1/4`. [Proof](ADAPTIVE_APERTURE.md) | Universal positivity is a reformulation of Goldbach. Fixed `s` remains subject to the complex-bank obstruction. |

## Fixed phases and adaptive arithmetic

| ID | Status and exact scope | Claim and evidence | Boundary / next falsifier |
|---|---|---|---|
| CB01 | PROVED LOCAL; nontrivial finite conjugation-paired nonzero nodes, eventual nonpositive real grade response | The largest-radius circle contains its positive real node `R` with `b_R <= -sum |b|^2/sum |b| <0`. [Cesaro proof](COMPLEX_BANKS.md) | A finite grade check cannot establish eventual nonpositivity; long-prefix impostors are explicit. |
| CB-SD | CLASSICAL IMPORT; every fixed `0<|z|<=1` | Complex Selberg–Delange bounds for `sum z^Omega(m)`, with exact parity prefixes, including `z=-1`. [Source/hypothesis audit](COMPLEX_BANKS.md) | Constants depend on the fixed node. No uniformity as nodes move or coalesce is inferred. |
| CB02 | PROVED LOCAL from CB-SD; authentic Omega grading | The complex ordered triangle and cumulative response are `O_z(X² log^(Re z+|z|-2) X)`. A square-root endpoint split controls the boundary; the diagonal is algebraic, without conjugation. [Proof](COMPLEX_BANKS.md) | A positive-measure convergence argument cannot silently replace the complex bound. |
| CB03 | PROVED LOCAL from CB01/02 and the positive-node mean | Every fixed finite all-grade minorant bank with `0<|z|<=1` has cumulative response asymptotic to `b_R K_R X² log^(2R-2) X<0`, and a negative response in each sufficiently large fixed-ratio shell. [Proof](COMPLEX_BANKS.md) | Does not imply each midpoint is negative or cover adaptive banks, continuum profiles, zero-node projectors or other observables. |
| PG01 | PROVED LOCAL; every nonnegative integer histogram of mass at most `M` | The sharp uniform positivity/recovery threshold is `epsilon(M-1)<1`, with `c0=max(0,ceil B)`. Worst-noise positive lower reports require sharply `epsilon(M-1)+2E<1`. [Proof](POINTWISE_GAP.md) | Necessity is for the mass-only class. Failure of the budget need not mean failure on a particular arithmetic packet. |
| PG02 | PROVED LOCAL; extra authentic masked-tail response | `B+lambda U<=c0<=B+K U`, intersected with mass and uncertainty bounds, can repair a failed certificate. [Proof and API](POINTWISE_GAP.md) | The mask `1_(h>=d)` is additional information, not a free combination of the old unmasked bank. |
| PG03 | PROVED LOCAL using classical PNT; genuinely per-midpoint even degrees | `epsilon_n=o(log^-2 n)` implies `sum_(n<=X) B_(d_n,t)(n)~X²/log²X`, without requiring a monotone degree schedule. [Proof](POINTWISE_GAP.md) | Positive aggregates allow infinitely many exceptional targets. No varying-node Selberg–Delange substitution is used. |
| PG04 | CLASSICAL RESULT TRANSFER; quantitative mean-square Goldbach theorem imported | The same resolution gives at most `O_A(X/log^A X)` nonpositive certificates for every fixed `A>0`. [Primary import and deduction](POINTWISE_GAP.md) | No improved exceptional-set result or effective threshold. Quantitative count size, not just almost-all existence, is essential. |
| PG-OPEN | OPEN; every sufficiently large authentic midpoint | A source-derived pointwise positive certificate outside imported almost-all results. | At complete integer resolution it is equivalent to Goldbach; at coarse resolution it is an additional unproved assertion. |

## Constructive phase projection and finite receipts

| ID | Status and exact scope | Claim and evidence | Boundary / next falsifier |
|---|---|---|---|
| PA01 | CLASSICAL IDENTITY / LOCAL ACCESS ANALYSIS; authentic complete angular response profile | Angular averaging extracts `c0` with operator norm one. [Proof](PHASE_APERTURE.md) | A continuum of responses is a stronger interface; extraction supplies no arithmetic positivity. |
| PA02 | PROVED LOCAL from root-of-unity orthogonality; nonnegative grade masses | A finite phase average retains grades divisible by `L`. The explicit `R^L` alias payment gives a sound lower certificate and authentic interval bounds. [Proof](PHASE_APERTURE.md) | Unpaid aliases produce false zero counts. The corrected fixed bank still obeys CB03. |
| PA03 | PROVED LOCAL access trade-off; movable phase order or authenticated support bound | Growing phase order can recover an integer count; at unit radius a valid grade ceiling below the order gives exact projection. [Proof](PHASE_APERTURE.md) | Neither finite source interpolation nor continuum inversion is a pointwise arithmetic theorem or a speedup. |
| AR-FINITE | VERIFIED FINITE; four frozen midpoints and three degrees | Twelve damped packets: ten positive, eight exact counts from observed packet intervals, seven meeting the uniform mass-only count budget. Four moving-node packets recover counts `6,15,22,34`. [Exact output](AUDIT_RESULTS.json) | These are finite integration observations, not asymptotic evidence. |
| AR-CONTROLS | VERIFIED FINITE / elementary counterexamples | Eighteen integer twins, long-prefix phase traps at `N=8,32,64`, 726 single-channel histogram/noise cases, and explicit contract mutations reproduce. [Receipt](VALIDATION_RESULTS.json) | Designed controls are disclosed; repeated execution is reproducibility, not independent source evidence. |

## Research diagnostics

The arithmetic boundary is a **pathway/probe gap**, not a demonstrated
impossibility of Goldbach or holographic inference. Contact with the source
is explicit in the actual Omega responses and checked primary imports.
The toolkit distinguishes fixed-bank failure, integer information loss,
noise ambiguity, and moving-parameter recovery. Source-map adequacy is
separately conditional on authentic response acquisition; algebraic
consistency does not certify that acquisition.

All three initial derivations and two later paper audits use the same
model family. Different mathematical decompositions and exact
implementations supply triangulation, not blind external consensus.
No scalar truth score is assigned. The closed proof steps above do not
resolve the remaining source-specific all-midpoint inequality, BBP R0,
pi normality, or RH.
