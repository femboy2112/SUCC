# Final scoped review: causal-history certificate and growing chirps

Review targets and content hashes are in `HISTORY_GROWING_REVIEW_HASHES.json`.
This was a bounded independent source/proof pass by the spectral agent, within
the same model family. It did not rerun the full epoch probe or supply external
peer review. The four root unit tests were independently rerun and passed;
the raw output is `HISTORY_REVIEW_TEST_LOG.txt`.

**Verdict: no substantive defect found in the reviewed scope.**

## Finite history certificate

For unit characters a,b and the cell-average projection P, the code computes

- `ea=E|E(a|cell)|^2` and `eb=E|E(b|cell)|^2`;
- `d^2=ea-|Ea|^2`, `r^2=1-ea`;
- `t^2=eb-|Eb|^2`, `eta^2=1-eb`.

These are exactly the centered projected and residual energies in CFS-5.
The resulting expression `|Ea Eb|+sqrt(d^2 t^2)+sqrt(r^2 eta^2)` is a sound
upper bound for the full real mean. Intersecting each energy enclosure with
[0,1] is justified by the declared unit-character contract. The generic Box
API does not authenticate unit modulus; the root probe constructs all these
boxes from exact rational phases and separately verifies the full source.

Square roots are outward: with denominator S, the lower numerator is
floor(sqrt(lo*S)) and the upper is ceil(sqrt(hi*S)). Multiplication and
subtraction are outward before this step. Centering can widen the interval,
but subtracting independently enclosed moments remains sound.

The source gate checks exact Fraction states, literal zero and every unwrapped
four-pole transition. It rejects changed seeds, wrapped-only paths and isolated
state mutations. Carries are computed as floor(U_n)-16 floor(U_(n-1)). A memory
length j uses precisely indices n-j+1 through n; thus the current carry is
available after the current source update. This is a causal contemporaneous
feature map, not a strict-past martingale predictor. The Hilbert certificate
needs no probabilistic independence assumption.

Taking the minimum lower endpoint and the minimum upper endpoint across the
four fixed models encloses the minimum **certificate expression**. A lower
endpoint above1/2 refutes the fixed menu's proposed half-bound certificate;
it is not a lower bound on |W|. The preregistration makes this distinction
explicitly and includes singleton cells only as a diagnostic. The registered
file was verified at commit0d0d57a98b7aff4e0b66a5e605071e0c94bb60d0.

## Growing-degree corollary

From `2^d=o(log p)`, one has d=O(log log p). With m>p^(1/3) and
H=floor(sqrt(m/d)), eventually H>=2 and d(H-1)<m. The CFS-7 bracket is at most
`3sqrt(d/m)+p^(-gamma)`. For fixed c<min(gamma,1/6), this is eventually at
most p^(-c), absorbing the constants into the strict exponent margin.
Taking the 2^d-th root of `5^(2^d-1)p^(-c)` gives exactly the stated bound
`5exp(-c log(p)/2^d)`, which tends to zero. Uniformity in coefficients and
h survives complete-cycle averaging and the exact epoch-weight transfer.
No power-rate claim for the latter transfer, effective BK threshold, or
unlicensed arbitrary polynomial interpolation is made.

The original complement approximation premise remains unproved. Its being
stronger than cancellation alone can be illustrated analytically: on J_A,
choose the changed complement `b_n=conj(a_n)e(n/A)`. Then its full mean is
exactly zero, yet an accurate degree-budget chirp approximation with variation
K obeys `1<=rho_A K+error`, by testing against `a_n e(-n/A)`. This control
changes the complement and is not an authenticated original BBP trajectory.

**Full real covariance / pi normality: OPEN. RH: OPEN.**
