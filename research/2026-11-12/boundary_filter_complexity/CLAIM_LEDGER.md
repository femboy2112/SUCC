# Claim ledger and hole contract

Date: 2026-11-12. Universal claims below are paper proofs in their stated
domains; finite probes do not provide their universal quantifiers.

| ID | Claim and domain | Status | Evidence / next falsifier |
|---|---|---|---|
| HBC01 | For integer b>=2,h!=0, phase Hankel rank of e(h b^n x) is finite iff x is rational | PROVED LOCAL, elementary | HANKEL_THEOREMS HBC01; attack distinct-point and polynomial assumptions |
| HBC02 | For irrational x, b^d consecutive rows give full rank d+1 | PROVED LOCAL, sufficient horizon | HBC02 root-count proof; no optimality or square-section claim |
| HBC03 | Every fixed nonconstant finite Fourier readout of an irrational expanding orbit has infinite rank | PROVED LOCAL | Extreme-frequency proof; constant readout excluded |
| HBC04 | Irrationality/full rank supplies no uniform stability or R0 | REFUTED inference | Explicit near-rational conditioning bound and sparse irrational shell control |
| FT01 | Full chronological source/Koopman/preimage transport is conjugate with correctly indexed tail frames | CLASSICAL ALGEBRA / REUSE + synthesis | FILTER_TRANSPORT FT01/02; remove intermediate frame to falsify |
| FT02 | Per-time calibrated finite Lipschitz/Fourier packets have paid sum-of-local-errors bound | PROVED LOCAL instrument | FT07/11; rounded-state propagation, unbudgeted high frequency and discontinuous masks excluded |
| FT03 | Finite Gram eigenvalue bound implies quantitative finite recurrence residual bound | PROVED LOCAL instrument | HBC05, FT12/14 and exact rational implementation; malformed/negative controls |
| FT04 | A uniform all-large-shell fixed-m Gram gap implies (CH), and gives the explicit R1 bound | PROVED CONDITIONAL | First-difference Rayleigh vector and FT15; gap for pi remains OPEN |
| FT05 | All-depth positive Gram conditioning implies normality | REFUTED inference | Invariant mixture law (1-c)Haar+c delta0 |
| DC01 | Pointwise local certificate sums to a finite-window lower bound | CLASSICAL telescoping / exact instrument | DUAL_CERTIFICATE_BARRIER DC01; omitted error mutation |
| DC02 | Admitted zero-cost rival bounds certificate by endpoint separation | PROVED LOCAL | DC02; equality calibration on two fixed states |
| DC03 | Authentic BBP circle law has exact coherent zero-cost rival at seed -pi/16 | REUSE source identity | DC03 and APH archive; zero-source domains may exclude it |
| DC04 | Small-oscillation certificate on denominator grids needs denominator-scale Lipschitz budget | PROVED LOCAL source-grid theorem | DC05 equations 7--9; sharp off-grid residual calibration |
| OBS01 | 13 specified finite original-zero BBP windows have positive certified Gram margins | FINITE CERTIFICATES | receipts/certified_gram.json and probe.py; independent numerical comparisons are supplemental |
| CAT01 | Over all density matrices in finite dimension, target expectation is identified by the complete allowed probability data iff its Hermitian observable lies in the real accessible-effect span | CLASSICAL / REUSE specialization | CARRIER_ACCESS_AND_TRANSDUCTION CAT01; explicit I/d plus/minus epsilon Delta counterpair; not single-copy certainty |
| CAT02 | Target approximation plus coefficient-weighted observation errors gives a paid expectation certificate | PROVED ELEMENTARY instrument | CAT02; source transport and joint confidence remain assumptions |
| CAT03 | A larger authenticated intervention family can repair passive boundary nonidentifiability | REUSE exact models | All-depth Witt geometry/carry contrast and resistor-network intervention 7/6 versus 49/41 |
| IT01 | Effective meter effects identify precisely their real target span; protocols within a closed accessible algebra stay there | CLASSICAL / PROVED finite specialization | INTERVENTION_TRANSDUCERS IT01; target-orthogonal density counterpair |
| IT02 | A declared controlled meter reveals population, leaves coherence hidden, preserves source Z-energy and attenuates off-diagonals | EXACT MODEL | IT02/03 and 11 exact tests; fresh preparation and calibrated rotations needed for all three coordinates |
| IT03 | Matched noncommuting cancellation yields a transported interaction integral with first-order spectral zeros | CLASSICAL Duhamel / synthesis | IT04; first-order zeros do not imply equality at finite coupling |
| IT04 | Smooth indirect sensors obey derivative budgets and therefore inherit the declared grid certificate's curvature requirement | PROVED CONDITIONAL instrument bound | IT05 plus DC05; periodic responses, fixed preparation and actual arithmetic source realization required |
| OPEN | Uniform source-selected Gram gap, R0, R1, pi normality, Goldbach, completed Weil positivity, RH | OPEN | No asymptotic source estimate is supplied |

## Hole contract

**Exact next statement:** for a specified fixed m>=2, there exist gamma>0
and integer A0 such that every integer A>=A0 has
`lambda_min(G_A)>=gamma`, where
`G_A[j,k]=A^-1 sum_(n=A)^(2A-1)e((16^k-16^j)16^n pi/16)`
for `0<=j,k<m`, with the authentic four-pole source and literal zero pin.

**Truth state:** OPEN. Its weakest useful form is a uniform lower bound
for one fixed m; no growth in m is required to reach R1. It closes
`source estimate -> finite Gram inequality -> (CH) -> R1 -> R0`; it does not close
normality. It is a conditional sufficient target with unpaid arithmetic
debt, not a proved advance on the signed rung.

**Novelty tax:** generic observability, tail conjugacy, Fourier collapse,
polynomial root counting and Gram inequalities are elementary or inherited.
The contribution is their source-locked compatibility analysis, the
grid-resolution budget, and executable finite certificates. In m=2 the
uniform gap is exactly `1-|W_A(15)|`; at every m>=2 the first-difference
direction already makes the full gap stronger than (CH). This must not be
advertised as an easier solved problem or a new rung below R0. No academic
priority is asserted for any formula.

**Controls:** coherent -pi/16 seed; rational fixed and period-two completed
points; sparse irrational failing R0; near-rational irrational with arbitrarily
bad conditioning; finite Haar grid; invariant non-Haar mixture with good Gram
conditioning; omitted source frames and errors; grid-only domain restrictions.

**Probe/holdout boundary:** A=17,37,73 and reserved A=109 with degrees
1--4 were specified before the two implementations. This is a same-session,
same-model numerical crosscheck, not an external blind validation. All finite
results can coexist with failure of an all-large-shell estimate.

**Candidate proof languages:** source-sensitive lower bounds for lacunary
polynomial energy; selected carry/prime-birth constraints sharper than the
full denominator grid; target-specific dual inequalities with paid endpoint
and resolution budgets. No use of a generic Haar/preimage law as the law of
the selected orbit is permitted.

**Next lamp if unresolved:** test an actual proposed local source inequality
against the coherent path or its grid-nearest residual. Report its exact
endpoint oscillation, Lipschitz cost and source-domain membership proof.
Reject it if these budgets cannot support its proposed uniform margin.
