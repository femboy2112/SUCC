# Scoped claim ledger: holographic boundary filters

This is a research-draft namespace, local to this dossier. `PROVED LOCAL`
means a mathematical derivation within the stated hypotheses; it does not
mean worldwide novelty, proof-assistant verification or an arithmetic
conjecture solved. `VERIFIED FINITE` records actual finite computations.
The paper proofs, source imports and executable checks are separate forms
of evidence. All final theorem scopes inherit their weakest premise.

## Reconstruction and target adequacy

| ID | Status and exact domain | Claim and evidence | Boundary / next falsifier |
|---|---|---|---|
| OBR-01 | PROVED LOCAL; one Hilbert source, bounded stationary labelled filters, independent reachable word states including the boundary state | `R_i=Q_i-H_i*G^-1 H_i` is the Gram matrix of missed directions; all residuals zero iff the observed span is invariant under every generator. Then all ordered responses in the cyclic sector are reconstructed. [Proof](ORDERED_REALIZATION.md) | Authentic joint cross-responses and `G>0` required. Test an added generator or a hidden reachable direction. |
| OBR-02 | PROVED LOCAL; complete word families through two consecutive lengths | Exact rank plateau implies closure; all subsequent word states lie in the same space. [Proof](ORDERED_REALIZATION.md) | A fitted or sampled Hankel rank is insufficient. Missing words or omitted cross-responses invalidate the premise. |
| OBR-03 | PROVED LOCAL; exact input tables and separately known global contractions | Gram-normalized leakage bounds finite-word error by accumulated per-step leakage. [Proof](ORDERED_REALIZATION.md) | Small unnormalized residuals can hide order-one leakage; `lambda_min(G)` matters. No unproved noisy-matrix inverse bound is claimed. |
| OBR-04 | PROVED LOCAL counterexample; two-dimensional Pauli systems | `(X,Y)` and `(X,-Y)` have equal individual spectra and all word-return powers, but opposite signed `XY` return. [Proof and exact controls](ORDERED_REALIZATION.md) | REFUTES universal signed reconstruction from powers. Calibrated coherent sums can recover the missing cross-responses. |
| OBR-05 | PROVED LOCAL counterexample; cyclic observation interface | An invisible direct summand changes the ambient interior without changing any reachable boundary response. [Proof](ORDERED_REALIZATION.md) | Reconstruction is only up to accessible-sector equivalence. An intervention reaching the summand changes the interface. |
| PT-01 | PROVED LOCAL / CLASSICAL linear algebra; finite probability carrier, explicit mass row | Universal target identifiability iff target lies in the filter row span. Outside it, a kernel vector gives two actual indistinguishable laws. [Proof](PHASE_AND_TARGET.md) | Universal over laws; positivity can make one particular fiber more informative. Code returns a witness, not a universal optimizer. |
| PT-02 | PROVED LOCAL / CLASSICAL norm duality; same domain | Worst indistinguishable target gap equals twice the uniform distance to the filter row span. [Proof and separate audit](PHASE_AUDIT.md) | A declared target and full probability domain are required; restricted source families can reduce ambiguity. |
| PT-03 | PROVED LOCAL; known coordinatewise observation errors | Target certificate pays both uniform approximation residual and coefficient-weighted measurement error. [Proof](PHASE_AND_TARGET.md) | Source and error authentication are premises. Coefficient growth cannot be ignored. |
| PT-04 | PROVED LOCAL specialization / CLASSICAL bispectrum context | Full Fourier support plus power and bispectrum determines a signal up to translation; general supported complex signals require the support presentation map to have zero kernel. [Proof](PHASE_AND_TARGET.md) | Rank alone misses finite torsion; q=21 gives `Z/63 -> Z/21`. The general group criterion is for complex signals, with positivity an extra constraint. |
| PT-05/06 | PROVED LOCAL / VERIFIED FINITE counterexamples | Z/12 equal-power laws hide different sums; Z/6 nonnegative signals share every second and third correlation but are not translates. [Explicit vectors](PHASE_AND_TARGET.md) | REFUTES unqualified power/triple completeness; a larger adequate probe family can distinguish them. |
| PT-07 | PROVED LOCAL; explicit full-support perturbations of the uniform Z/3 law | Quotient signal distance is `18 epsilon`; triple-data separation is `3078 epsilon^3`. No uniform inverse Hölder exponent above `1/3` holds nearby. [Proof](PHASE_AND_TARGET.md) | Does not establish a general inverse at exponent `1/3`. Fixed-signal stability can depend on its minimum nonzero Fourier magnitude. |

## Zero-sector filters and genuine arithmetic

| ID | Status and exact domain | Claim and evidence | Boundary / next falsifier |
|---|---|---|---|
| GBF-01/02 | PROVED LOCAL / CLASSICAL finite separation; finite nonnegative grade support, feasible response packet | A signed combination equal to one at grade zero and nonpositive elsewhere lower-bounds the zero mass; such separation is complete for excluding zero-ground **real** completions. Signed interval endpoints pay uncertainty. [Proof](GOLDBACH_FILTERS.md) | Real relaxation, not integer/source feasibility. A source label does not authenticate the support ceiling. |
| GBF-03 | PROVED LOCAL arithmetic specialization / VERIFIED FINITE n=10 | Grade `Omega(n+a)+Omega(n-a)-2` has zero count equal to unordered Goldbach count; moments `(9,16,46)` and ceiling four give lower bound `1/2`. [Proof](GOLDBACH_FILTERS.md) | Forged ceiling three yields false lower bound three even though a counterfeit packet is feasible. Fixed quadratic positivity is observed at only nine midpoints through 257. |
| GBF-04/05/06 | PROVED LOCAL counterexamples | Every fixed moment degree has positive/zero-ground twins; homometric finite sets hide sum coefficients; modulo-four prime sums include wrap aliases. [Proofs and controls](GOLDBACH_FILTERS.md) | Counterfeit histograms are not asserted to be actual prime-pair sources. Carry/winding and source coupling must be retained. |
| DF-01 | PROVED LOCAL; all nonnegative finite-mass laws on integer grades, even d>=2, 0<t<=1/2 | Damped filter annihilates grades 1 through d-1 and has tail in `[-t^[d(d+1)/2],0]` at every higher grade; bounds the zero mass. [Proof](DAMPED_FILTERS.md) | No upper grade ceiling needed. Fractional grades, signed mass and an uncertified damping range break the bound. |
| DF-02 | PROVED LOCAL; same domain, authenticated absolute response errors | Coefficient l1 norm `<527/63<9`; exact signed error intervals enclose the target. [Proof](DAMPED_FILTERS.md), [separate derivation](DAMPED_DERIVATION_AUDIT.md) | Bounded amplification is not bounded acquisition cost. Normalized one-count resolution still costs order `1/M` absolute precision. |
| DF-03 | PROVED LOCAL; zero mass integral in addition | With exact responses and `epsilon_d M<1`, ceiling of the lower response recovers the exact count. Noisy recovery uses the feasible integer interval. [Proof and API controls](DAMPED_FILTERS.md) | General real masses cannot be assigned an integer promise. The fractional-wrapper mutation was found, repaired and retained. |
| DF-04 | PROVED LOCAL; mathematical filter for all d>=1 | Even degrees increase to the zero mass; odd degrees decrease to it. Consecutive same-parity tail ratios are at most one-third. [Proof](DAMPED_FILTERS.md) | Monotone information refinement; not physical time, entanglement or monotonicity of arbitrary noisy point estimates. |
| DF-FINITE | VERIFIED FINITE; six frozen midpoints, three fixed degrees | All 18 response vectors/certificates replayed independently; 14 positive lower bounds, 11 exact counts, every degree-six count recovered. [Results](DAMPED_RESULTS.json), [audit](DAMPED_AUDIT.md) | Source responses were acquired by finite factorization. No all-midpoint estimate or computational speedup is inferred. |
| FR-01 | PROVED LOCAL using an explicit CLASSICAL mean-value import; fixed 0<s<1 | Authentic midpoint-averaged response has asymptotic `K_s X^2(log X)^(2s-2)`, with positive explicit parity-corrected constant. [Proof](FIXED_RESOLUTION.md), [audit](FIXED_RESOLUTION_AUDIT.md) | Averages over midpoints, not a product-of-marginals formula at a fixed midpoint. Classical Selberg--Delange import is load-bearing and separately cited. |
| FR-02/03 | PROVED LOCAL using FR-01; fixed finite damped-response banks | The cumulative lower response is eventually negative, hence fails at infinitely many genuine midpoints. Applies to every fixed bank giving a pointwise zero-grade minorant. [Proof](FIXED_RESOLUTION.md) | Does not say every sufficiently late midpoint fails. Adaptive nodes/order, other observations and source-specific inequalities outside the pointwise-minorant class are not excluded. |
| FR-04 | PROVED LOCAL / known-result recovery using PNT and DF-01; fixed damping and a common even degree d_X at each cutoff | If `epsilon_X=o(log(X)^-2)`, aggregate filtered response is asymptotic to `X^2/log(X)^2`; a sufficient degree is of order `sqrt(log log X)`. [Proof](FIXED_RESOLUTION.md) | Same d_X for all midpoints in the sum. Mean positivity is not positivity at every midpoint, and this is not the stronger worst-case count-recovery scale. |

## BBP source and frontier

| ID | Status and exact domain | Claim and evidence | Boundary / next falsifier |
|---|---|---|---|
| PF-01 | PROVED LOCAL; authentic four-pole source, zero seed, genuine cell counts | The cell minorant of `8 dist(x,Z)^2`, with future-tail payment `376/[225(B+1)^2]`, lower-bounds `1-Re W_B(1)`. [Proof](PI_FILTERS.md) | Needs the joint selected source. A same-forcing rational counterseed makes every frozen lower bound zero. |
| PF-02 | PROVED LOCAL; integer fixed-point interval recurrence | Accumulated rounding width is propagated under multiplication by 16 and encloses the rational source modulo one. [Proof and precision mutants](PI_AUDIT.md) | Resetting width after each recurrence is false. Discarding ambiguous cells can break resolution monotonicity. |
| PF-FINITE | VERIFIED FINITE; six shells, three resolutions, 48 guard bits | Eighteen exact source certificates, no ambiguous cells, all independently replayed by unwrapped four-pole Fractions. [Results](PI_RESULTS.json) | Newly fixed shells are not externally blinded. Finite positive margins do not supply the all-late-shell quantifier. |
| OPEN-G | OPEN | Source-derived adaptive coupled-response lower estimates sufficient for every sufficiently large Goldbach midpoint. [Next contract](NEXT.md) | Exact source enumeration or an equivalent counting premise does not close the gap. |
| OPEN-P | OPEN | Uniform positive R0 shell margin for the authentic selected BBP source; full pi normality is stronger. [Next contract](NEXT.md) | Power vanishing would suffice for Weyl cancellation, but it has not been proved here. |

## Diagnostic separation and verdict

The proposed boundary family now has specific **pathways** to finite
reconstruction and target certification. Its source-map adequacy remains
a separate issue: genuine prime-pair responses and the zero-anchored BBP
orbit must be supplied, rather than substituted by convenient ensembles.
The finite phase aliases are disclosed probe limitations; they are not
falsehood of the intended arithmetic statements. The fixed-resolution
result is a genuine source-specific boundary for the stated filter class.

No numerical truth score combines contact, pathway state, source adequacy,
commitment, probe availability, independence or coherence. The finite proofs
are disclosed within scope; the arithmetic all-target estimates remain
open. Separate same-model audits improve implementation/derivation coverage
but do not constitute independent external mathematical corroboration.
