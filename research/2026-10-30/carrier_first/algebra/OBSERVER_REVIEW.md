# Hostile reconstruction of the parent observer bounds

The review is by another agent of the same model lineage. The following
algebraic reconstruction and separate executable check are complementary
bearings, not an external referee or independent mathematical authority.
Reviewed source byte hashes are in `receipts/observer-review.log`.

**O1 survives.** An exact report of L consecutive m-digit observations
must refine the length m+L-1 half-open digit cylinder. Greedy coding makes
the infinite refinement injective; no ambiguity at terminating expansions
has been discarded. A finite autonomous quotient of the full circle cannot
preserve the first digit for all future times.

**O2 survives with the stated constants.** Each future midpoint move has
distance at most b^(-k-1)/2 after inverse-branch contraction. The two moves
therefore cost at most b^(-k-1). The conditional grid has spacing 1/b, which
explains the 1/(bN) factor in rho. The endpoint replacement costs 1/N before
the fair operator, hence 1/(bN) after it. Solving the contraction inequality
gives exactly `(b rho+b^-k+1/N)/(b-1)`. Pinsker's conditional bound and Jensen
give the O2a coefficient one in front of sqrt(D/2). The support-entropy floor
O2b correctly treats empirical counts, not a stationary disintegration.

**O3 survives.** The Green-tail sum bound follows from T_n<1/(64n^2) and
sum n^-2<2. Complex periodic characters are 2pi|h|-Lipschitz on the ordinary
interval. The Green error is paid as a periodic chord, so a circle seam
does not invalidate the estimate. The signed Fourier square sum has
`sum weights*h^2=H(H^2-1)/6`; multiplying by 4pi^2 gives the stated Fejer
coefficient 2pi^2/3. These bounds retain an unproved empirical-cost input.

**O4 and O4a survive.** An S-state clockless deterministic emitter has a
lasso with preperiod a and period p, a+p<=S. The rational denominator is
at most b^a(b^p-1)<b^S. The global finite-exponent lower bound and N common
digits therefore force `S>=(N+log_b c)/mu`. The bound is on states, not bits,
and does not cover an external integer clock. O4a uses zero-based indices:
the last mismatch between w_i and w_(i-p) must precede a+p. Minimizing over
p gives the stated formula. The finite-exponent input remains classical,
not proved by these tests, and linear state cost is insufficient for normality.

**Exact independent execution.** `observer_review.py` independently
integrates the empirical CDF rather than using the parent's quantile
algorithm, reconstructs conditional counts from rational orbits, and checks
768 exact interval-W1 cases at bases 2,3,5,16. It enumerates candidate lassos
directly for all 2,046 nonempty binary words of lengths at most ten; all
minimal state values and returned witnesses agree. Both checks pass.

**Minor API issue sent to parent:** `ArithmeticState` originally admitted
an arbitrary `source_id` while always applying the original forcing. That
label should be validated or documented as descriptive-only. This does not
invalidate O1–O4; it matters for a source-typed executable interface.

**Resolved in the final reviewed version:** the parent added source-id,
nonnegative clock and carry-history-length validation. A fresh replay in
`receipts/observer-review-refreshed.log` passes the same768 and2,046 cases;
the earlier receipt remains historical. Final hashes and the further
analytic/frame review are in REVIEW_NEW_TRANSPORT.md.
