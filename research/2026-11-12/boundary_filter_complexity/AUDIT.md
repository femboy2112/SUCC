# Independent-method hostile audit

Date: 2026-11-12. Scope: the new boundary-filter-complexity dossier and its
rational Gram implementation. This is a separate reasoning pass and numerical
implementation **within the same model family**, with shared repository/source
provenance. It is not external peer review, independent research provenance,
formal-kernel verification, or a statistical estimate for all epochs.

## Files inspected and proof verdict

- `FILTER_TRANSPORT.md`: checked the order and signs in FT-01/02 by direct
  substitution into `R_a f(u)=f(u+a)`, then taking adjoints. In particular
  `K_n L_n=Q` and `L_n K_n=I` have the stated orientation. Verified the source
  bound in FT-04 against IAD-03(b), the `pi/32` constant in FT-08, the depth
  requirements, and the fixed-depth/common-terminal-horizon identities.
- FT-13 follows by a two-factor telescoping bound and domination by
  `eta 1^T+1 eta^T`. FT-15 has the correct endpoint cost: the j-shifted mean
  differs from the original by at most `2j/B`, whose average is `(m-1)/B`.
  Cauchy--Schwarz and `trace G=m` give the displayed spectral bound. Its
  uniform source-specific premise remains open.
- `HANKEL_THEOREMS.md`: checked all HBC-01--06 quantifiers. The polynomial
  `sum c_j z^(b^j)`, divided by z, has degree at most `b^d-1`; the proposed
  `b^d` distinct roots therefore give the claimed rectangular rank. A
  nonconstant finite Fourier filter retains a unique extreme frequency in
  its last nonzero recurrence summand. The worst-clock Frobenius estimate
  correctly cancels the row-count normalization. For the sparse irrational
  control, at most two powers of two occur in `(B,2B+w]` when `w<B`, giving
  at most `2w` exceptional clocks and the stated `4w/B` contribution.
- `DUAL_CERTIFICATE_BARRIER.md`, especially DC-05: the combined forcing
  denominator divides D(j), so the unreduced lcm grids nest and are preserved
  by the source transitions. The residual has Lipschitz bound
  `2pi+16 Lip(V_(n+1))+Lip(V_n)`. A nearest grid point is at distance at most
  `1/(2Q_n)`, giving the correct negative residual allowance at the coherent
  history. Summing yields **plus** `sum ell_n/(2Q_n)` in (7). Monotonicity of
  Q and the shell maximum of the two adjacent potential Lipschitz bounds
  give `2pi+17K_A` in (8); rearrangement gives (9). Whole-circle oscillation
  and controlled extensions are essential hypotheses and are stated.
- `observational_succ/boundary_filter_complexity.py`: inspected exact
  integer square-root rounding, rational source scaling, negative-harmonic
  orientation, interval averaging, conjugate symmetry, exact diagonal, and
  the cap `|G_jk|<=1`. A positive lower bound is sound under the imported
  character-enclosure theorem. Zero is correctly inconclusive. The code
  does not accept an external matrix/certificate as authenticated source
  input.

No load-bearing mathematical or certificate-soundness error was found.
This verdict is scoped to the displayed proofs and inspected implementation;
finite numerical checks below do not establish their universal correctness.

## Repairs raised and verified

1. The frozen-calibration section initially did not explicitly restate
   `n>=1` before the bound containing `n^-2`. The section now declares it.
2. The finite resource guard initially omitted lookahead. It now checks the
   actual completed-source horizon against 8192 before constructing the
   source. The persisted hostile script checks rejection at horizon 8193.

These were a domain clarification and resource-budget repair, respectively;
neither was a demonstrated false positive in the rational rank certificate.

## Executed differential checks

`oracle.py` evaluates the phase orbit with high-precision mpmath pi, without
using the rational BBP backend. It separately computes the Gram through
Hankel products and the Weyl difference-frequency identity. The 13 prescribed
pi cases comprise starts 17, 37, 73 at degrees 1--4, plus the predeclared
start-109/degree-4 holdout. Every differential error is below `1e-65` and all
numerical Gershgorin margins are positive. The exact selected cases were
declared before that oracle ran; this is not an externally blinded holdout.

The four controls are completed zero, rational 1/15, rational 1/17, and an
irrational point extremely close to 1/15. Their mathematical ranks are not
inferred from floating output. The near-rational control required raising
precision from 160 to 700 decimal digits to resolve its very small positive
numerical eigenvalue (approximately `1.84e-421`). Tiny negative numerical
eigenvalues in exactly rank-deficient controls are roundoff, not negative
Gram witnesses. Results are retained in `receipts/oracle.json`.

`audit_intervals.py` reproduces the additional hostile check with seed
20261112 and 100-decimal-digit mpmath arithmetic. It constructs 16 rational
interval cases, including width-three intervals, circle-seam crossings,
negative harmonics, and deliberately fewer rows than columns. All 16 return
`INCONCLUSIVE`; all 216 selected complex-entry evaluations lie within their
computed rational boxes, allowing `1e-90` numerical comparison slack. The
script also tests the repaired actual-horizon resource guard. These sampled
interior checks are **not** proof that every point of each interval is
enclosed; the analytic enclosure proof and exact outward rounding carry
that claim. Receipt: `receipts/interval_oracle.json`.

Reproduce from the repository root:

```sh
python research/2026-11-12/boundary_filter_complexity/oracle.py
python research/2026-11-12/boundary_filter_complexity/audit_intervals.py
```

The full native suite was already running in the integrating session and
was not duplicated by this audit. Its outcome belongs to that session's
validation record. No normality, R0, R1, Goldbach, RH, or external-review
status is promoted by these checks.

## Integrating proof audit of the grid refinements

The integrating reviewer checked the reduced denominator variant separately:
the lcm of reduced forcing denominators is nested and contains every forcing,
so multiplication by 16 followed by the next forcing preserves the declared
grids. Neither reduced state denominators nor an unproved growth estimate
are substituted for that lcm.

For the C² refinement, on each lifted mesh cell the function
`R-J+(M/2)(x-a)(b-x)` is concave with zero endpoint values, hence nonnegative.
This gives the negative allowance `M/(8q²)` with the stated sign. A periodic
potential composed with the degree-16 circle map has second derivative bound
256 times its own; together with the current potential the shell maximum
factor is 257. The completed escape has curvature at most `4pi²`.
The exact quadratic calibration tests cell-local sharpness only, as stated.
The final 16-test dual-certificate replay passed. This additional review is
also within the same model family and supplies no external proof authority.

## Indirect-observation continuation audit

A separate reviewer re-derived the effective-effect scope, retained-record
factor `c^2`, the sign and order of the Duhamel integral, and the operator
derivative constants in `INTERVENTION_TRANSDUCERS.md`. In particular, the
two ordered `H'` insertions give `tau^2 h_1^2` in the second derivative
of the unitary, and the response curvature bound has coefficient 4.
Variable-input trace-norm costs and the factor-257 grid link also checked.
The nonzero-coupling hypothesis was made explicit in the half-time spectral
visibility example. No load-bearing defect was found in this pass.

Root replay passed all 11 exact Gaussian-rational intervention tests; raw
output is in `receipts/intervention.log`. Those finite tests calibrate the
supplied channels and do not prove the universal derivative statements.
The reviewer and author share a model family; the review adds a separate
derivation, not independent external authority or a physical experiment.
