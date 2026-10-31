# Selected finite-band round: sharper transport and stricter arithmetic tests

Draft child of PR411, exact parent
`fa598e3a5a1111c3445200f1ddf48dcdea6bdc09`. All work is additive here.
The authentic four signed poles, U0=0, historical contracts and author
provenance remain unchanged. **Pi normality and RH remain OPEN.**

The principal improvement is a stronger, sharp-in-order comparison of the
actual rational and completed Fejer energies. It allows the full sampling
scale H proportional to N. It does **not** bound either selected energy.
The missing original-source signed upper bound was attacked through complete
CRT products, positive source interpolation, digit transitions, Stoneham grids
and finite interval calculations; none established an unbounded selected saving.

## Surviving mathematics

1. **[K01–K02](kernel/KERNEL_TRANSPORT.md):** for every real seed, with the
   authentic source and C²=pi/(8 sqrt(3)),
   `|sqrt(F_H(y))-sqrt(F_H(U))| < C H/N`.
   At the coherent changed seed, if H tends to infinity and N/sqrt(H) tends
   to infinity, the difference is asymptotic to `(pi/15) H/N`.
   The constant is derived from a Gamma-half/Mellin integral. It is not a
   golden parameter or a zero-seed cancellation constant.
2. **[C1–C2](cylinders/CYLINDERS_AND_STONEHAM.md):** at threshold 1/20 and
   starts A>=2, the lag-one slip count K and adjacent hexadecimal transition
   count C satisfy `(K-2)/2 <= C <= 2K`. The same-forcing period-01 counterseed
   slips at every late time but has completed Fejer energy at least H/2.
   Frequency17 exposes its exact coherent organization.
3. **[AQ01–AQ04](arithmetic/ARITHMETIC_THEOREMS.md):** an order-two Stieltjes
   representation gives positive rational atomic source controls matching M
   original source values and J+1 exact moments. Their atom count lies between
   `ceil((M+J+1)/2)` and `M+J+1`; every such finite atomic control has rational
   completed boundary. All moments, unlike any finite subset, identify the
   original measure. **PR408 already proved the broad positive-prefix/jet
   countermodel conclusion**, with stronger relative-closeness and dyadic
   properties. The new contribution is this construction and its complexity
   bounds, not rediscovery of that no-go.
4. **[C3](cylinders/CYLINDERS_AND_STONEHAM.md):** an explicit all-horizon
   Stoneham c3/c5 grid argument yields `limsup F_(H_N,N)<=c` for
   H_N=O(N^(1/3)), improving the launchpad's 3c calibration constant.
5. **[K03–K04](kernel/KERNEL_TRANSPORT.md):** half the launchpad's frequencies
   suffice for the same cylinder constant; another ratio improves the
   constant. A normal digit sequence can fail every prescribed polynomial
   moving-band test maximally along a subsequence. These are instruments and
   quantifier controls, not source-specific dispersion.

## Actual selected signed computations

[CERTIFIED_EXPERIMENTS.md](CERTIFIED_EXPERIMENTS.md) proves the integer-interval
algorithm and describes the distinct direct-rational oracle. At N=8192,H=512:

    1.059243283524 < F_(512,8192)(U(0)) < 1.059243283525.

Twelve complete primary-times-complementary character sums at six declared
prime clocks and fresh frequencies11,13 have certified squared normalized
modulus below1/4. They are finite, overlapping windows, not independent samples
or a coverage theorem. Prime-only and full values differ substantially.

Read [CLAIMS_AND_ROUTES.md](CLAIMS_AND_ROUTES.md) for failures and open debts,
[ROOT_REVIEW.md](ROOT_REVIEW.md) for provenance-dependent review scope,
[VALIDATION.md](VALIDATION.md) for raw execution receipts, and
[NEXT_HANDOFF.md](NEXT_HANDOFF.md) for the next falsifiable obligation.

The Harmonic/Golden/Euler–Mascheroni triangle and
`Omega_OM=phi^(-1)-gamma` retain Leah / femboy2112 provenance. Their positive
observer geometry and the selected arithmetic phase are explicitly different
objects. No new arithmetic role for the golden or Fibonacci constants was
established in this round; PR413 remains a read-only sibling.
