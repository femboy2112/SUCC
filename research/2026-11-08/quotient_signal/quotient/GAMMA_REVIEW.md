# Independent scoped derivation review of the Gamma residual

Reviewer: `/root/quotient_signal`, separate from the Gamma derivation author.
Read-only target: sibling `gamma/THEOREMS.md`, SHA256
`f9993d356f27aaf4fed00f9ac28d7a15560c3b252c8e713321262c6c429de6b2`.
Scope: GQ2--4 proof, constants, signs and relation to the learned quotient.
Status: **SURVIVES this independent derivation review**. This is not an
external referee, a kernel check, or verification of every inherited theorem.

1. Re-expanded the original four-pole integral independently:
   `(1-x)Q(x)=4-2x³-x⁴-x⁵`. Summing the geometric future weights gives
   `T_n=int_0^1 x^(8n)(1-x)Q(x)/(16-x^8) dx` with nonnegative integrand.
   The original exponent shift and factor16 are correct.
2. Checked `Q(1)=15`, `Q'(1)=22` and the monotone bound `Q'<=22` on[0,1].
   With denominator>=15, the numerator bound30(1-x) yields
   `0<=1-f<=2(1-x)`. The two beta integrals give the stated lower bound
   `(m-1)/[(m+1)(m+2)(m+3)]`, m=8n.
3. Recomputed the rational inequality: subtracting the lower bound from
   `1/m²` has numerator `7m²+11m+6`. The required strict comparator gap is
   `7(m+1)(m+2)(m+3)-m(7m²+11m+6)=31m²+71m+42>0`.
   Thus the coefficient7/512 in GQ3 is correct for every n>=1.
4. Re-indexed both finite recurrences independently. They give
   `R_N=pi+15S_N-16T_N` and
   `A_N=pi+15Q_N+16S_N-16(N+1)T_N`.
   Passing to the declared harmonic finite part yields
   `C=B/15-16R/225+pi/225`; all four displayed coefficients of pi,
   sqrt(2)pi, log2 and sqrt(2)log(1+sqrt(2)) agree algebraically.
   The values of inherited R and B were treated as the cited inputs;
   their archival proofs were not independently re-audited in this review.
5. Direct differentiation gives `f'(1)=22/15+8/15=2`. Taylor's uniformly
   bounded second derivative on[0,1] supplies the O(m^-4) integral remainder.
   Expanding the first two beta integrals gives
   `1/m²-7/m³+O(m^-4)`, hence the sharp limit7/512 in GQ2.
6. Checked the harmonic estimate using the trapezoid bound for the strictly
   convex function1/x. Adding64 times the Green-tail bound gives
   `1/(2N)+7/(8N)=11/(8N)`. Thus GQ3's explicit gamma calibration is valid.
7. Checked the phase sign and normalization directly:
   `q_n=e(-hT_n)`, so the product with the positive log counterphase is
   `e(-h[sum nT_n-logN/64])`. The chord inequality changes an error
   `<11/(512N)` in the scalar finite part into
   `<11 pi |h|/(256N)` in phase. The h=0 case is correctly separated.
8. Re-derived `sum_(n<=N)n16^n=[16+(15N-1)16^(N+1)]/225`.
   The fixed-zero-reference unwrapped defect therefore isolates s=0;
   transporting the completed reference with s makes q seed-blind.

The source calibration is a productive, precisely scoped realization of an
Euler--Mascheroni residual. It is **not** the same quotient as QS1--6:
there `z=ab=e(hU_n)` survives, whereas GQ4 divides z by `e(hX_n)` and
retains `e(-hT_n)`. No identity equating the learned conditional covariance
to this calibrated product is supplied or implied. In particular the bad
coherent seed retains the same GQ4 product while its full Weyl mean tends1.
The requested bridge still needs a source-selected signed estimate.

No mathematical correction was found within this scope.
**Original-zero signed covariance: OPEN. Pi base-16 normality: OPEN. RH: OPEN.**
