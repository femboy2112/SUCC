# Arithmetic transport experiment contract

This contract was fixed after exploratory hand calculation and a small direct
Fraction scratch pass at primes below 100, before the executable suite and its
fresh holdouts were run. It is not a claim that those exploratory examples were
blind. All new files are additive to PR #398, head
`1a1524de28b155139d8fe84ea90fc2f117fbb9f3`.

| Candidate | Pass | Fail | Ambiguous / excluded |
|---|---|---|---|
| All-class prime-power shadow | Exact rational recurrence, valuation-layer sum and derived source map agree for every declared case | One exact mismatch | A denominator containing more than the allowed power, non-prime input, or non-p-integral coefficients is outside the theorem |
| Native self-shadow at every even exponent | Exact equality modulo p, including primes in classes 3 and 7 | One admissible mismatch | Vanishing shadow is allowed and means conductor loss, not theorem failure |
| First lift to modulus p² | Exact correction using the half-Fermat quotient and the next valuation layer agrees | One mismatch | An uncorrected lift is a separate candidate and is expected to fail |
| Higher precision | Retained valuation layers reproduce direct rational reduction modulo p^r | One mismatch | This is an exact decomposition, not an analytic improvement |
| First-power conductor births | First residue is 4, −1, or −1/2 and exact valuation is −a | One mismatch | p=2 is excluded, with a separate integral passport |
| Reflected packet | Four derived residues hold; p=19 has a zero third residue and returns at fourth | One mismatch | No prediction of a full local period for classes 3 and 7 |
| Coefficient identification | J plus three prescribed source moments identifies the four coefficients uniquely | Another rational solution | Identification is restricted to these fixed four poles |
| Seed controls | p-integral rational seeds are invisible modulo p; at modulus p² their shift is p^a 16^N s | A discrepancy | Coherent irrational seed has no rational p-adic reduction; it is a real-circle control elsewhere |

Fresh prime holdouts are 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
181, 191, 193, 197, 199. Prime-power holdouts include even exponents in all four
prime classes and exponent four at p=7. Coefficients include authentic
`(4,-2,-1,-1)`, wrong-ratio `(5,-2,-1,-1)`, same-ratio `(4,0,-1,0)`, arbitrary
`(5,7,2,-3)`, and rational `(1/2,-2/3,7/5,-11/4)` where p-integral.

The intended conclusion is an exact arithmetic constraint. No finite pass
licenses a universal proof without the separate derivation, and no p-adic pass
licenses signed real-circle cancellation, normality, or scholarly priority.

Literature follow-up, declared before its committed exact tests: the parent
identified the published BBP null vector `(-8,8,4,8,2,2,-1,0)`. The added
candidate predicts the reflected constant is exactly `2*pi`, and
`-1/(8k+1)<W_k-2U_k<0` for k>=1. Pass requires exact polynomial identity and
finite rational tail comparisons; failure is one exact mismatch. Numerical
agreement with pi would be calibration only. The source relation is published,
not new; the proof above the finite checks is supplied separately.

Before the final null-source birth tests, the root agent proposed a stronger
control: the seven-pole published null source, with zero seed, is coherent in
the real circle despite having every odd-prime conductor depth. Predicted pass:
for Q=p^a>=7 its first Q-denominator is at ceil(Q/8), with exact valuation -a;
its phase is in (-1/(8n+1),0). One rational mismatch refutes the claimed domain.
Q=3,5 are not included in the unique-first-denominator argument. This is an
explicitly changed source family, never a counterexample to authentic BBP.

Final rigidity control, before its exact test: c=(2,11/4,-1/2,-17/4) is predicted
to pass J, Q(0)=0, Q'(0)=15 and positivity, while failing Q''(0)=-59. The
declared positive factorization in the dossier is checked as a polynomial
identity. This tests whether the arithmetic ratio plus the leading Gamma
rank/amplitude would falsely identify the authentic source.
