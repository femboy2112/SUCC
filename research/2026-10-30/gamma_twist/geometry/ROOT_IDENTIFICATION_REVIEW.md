# Complementary review of the root 2-adic identification proof

Reviewed: `../TWO_ADIC_IDENTIFICATION.md`, `../two_adic_identification.py`,
`../independent_identification_oracle.py`, and the saved symbolic minor receipt.
Reviewer: geometry subagent, same model family and shared project context.
This is a complementary algebraic check, not blind peer review or a kernel proof.

**Verdict:** no blocking algebraic issue found in TI-01–TI-05 as currently scoped.
The source/phase authority boundary is maintained.

1. **TI-01:** clearing denominators gives a cubic over Z with a common factor 4
   and an odd residual denominator at every integer time. The four initial
   values-to-forward-differences transform is unimodular; the Newton binomials
   are integers on all positive integer times. Both directions of the orbit
   equivalence use U0=0. Four exact rational observations were correctly marked
   inherited rather than new.
2. **TI-02:** the inverse matrix in the oracle really has maximum 2-denominator
   valuation 11: entries `-17/10240` and `-455/2048` attain it. The sample ideal
   is 2^(k+2), so the coefficient loss is 9, not 11. The stated vector has two
   odd coordinates and Cw=(0,0,0,30720), v2(30720)=11; at n4 the Newton binomial
   is1, giving source valuation9 exactly. Scaling proves sharpness. The height
   repair uses the difference bound2H and is sufficient, as claimed.
3. **TI-03:** at derivative order j the offset4 valuation is
   j-2+v2(j!), strictly below offset6's 2j-1+v2(j!) even at j0, and below the
   odd-offset terms. In the unit pair the denominators are both1 modulo4, so
   the sum of inverse powers has valuation1 at every order. The product is5
   modulo8; repeated squaring gives v2(a^(2^m)-1)=m+2 for m>=1. Here m=k+2,
   hence k+4. No fractional-argument Gamma2 domain was smuggled in.
4. **TI-04:** the backward boundary direction converges because term j has
   valuation4j-2. Its j0 term alone has the least valuation, so no cancellation
   is possible. The authentic boundary zero is explicitly inherited. Exact
   boundary identifies this one-parameter family; it does not claim uniqueness
   in the full four-coefficient space. The prime13 caveat is correct.
5. **TI-05:** substitute B=4z-2D before dividing the cubic numerator by4.
   The resulting numerator is integral; its linear coefficient modulo2 is D,
   and all degree>=2 coefficients are even. The odd denominator has constant
   reduction1. Thus the divided difference is D modulo2. D odd is sufficient
   for an isometry of Z2; D even maps both input parities to one output parity.
   Stationary F differences have their uniquely least-valuation term at j0,
   so the same isometry follows. U_n=F(n)-16^nF(0) proves eventual finite
   permutation cycles but no identification from those cycles.

**Adversarial assessment:** no contradiction comes from t=2^(k+2) age mutants,
integer/dyadic seed aliases, or the coherent real changed seed. The last is not
an element of the rational source-identification domain and cannot be reduced
as a rational p-adic phase. A proposed real mixing corollary would still fail
this review: the proof supplies no estimate of selected real characters.

Reviewed SHA256 values:

- TWO_ADIC_IDENTIFICATION.md: `97ed7047fdff939224ed9bd06107072e7e0a222032467f2c93b541a1a561b670`
- two_adic_identification.py: `5fb1608513a07e17bfb8e18f4de067dcf68a7a18b58d54bcb0ed6a683182590a`
- independent_identification_oracle.py: `52ab2f860c3814068a4fe13cb3bdd45bf55c286b61995adfc6aaa68b24a84f6d`

## Addendum: DF-01/DF-02 direct-diagonal obstruction

Reviewed `../DWORK_AND_ADELIC_BOUNDARY.md` and `../direct_diagonal_probe.py`.
**Verdict:** the stated direct representation obstruction is sound, conditional
on the explicitly inherited AT-04 birth theorem and CG-01 sharp conductor law.

- A rational function over Q regular at the origin has its entire multivariate
  Taylor series over one fixed Z[1/M]. Normalize its nonzero constant denominator
  coefficient first, then apply the formal geometric expansion; no convergence
  theorem is needed. Taking a diagonal cannot introduce new denominator primes.
- Authentic births have valuation−a at p^a for every odd p. Taking a=1 already
  excludes fixed finite prime support. Repeated a excludes a fixed p-adic
  scalar integralization at each odd p.
- For a fixed rational function R(n), write integer polynomials P/Q after
  clearing a fixed scalar denominator. Rational multiplication changes log of
  the reduced denominator by at most O_R(log n), away from finitely many zeros
  and poles. Thus 6n+o(n) survives.
- The finite-prime contradiction in the multiplier extension needs BOTH height
  growth and the source-LCM prime-exponent bound. The proof supplies both:
  each fixed prime valuation in den U_n is O(log n), and polynomial evaluation
  adds only O_R(log n). Therefore fixed finite support would force O(log n)
  total log denominator. Height growth alone would not justify this step.
- Multiplying by a time-dependent factorial/LCM, differentiating/reindexing
  into a different auxiliary series, using nonrational generating functions,
  or a different p-integral motive is outside the theorem. The paper explicitly
  preserves those possibilities and demands the selected-phase transport cost.

This is a scope/domain theorem, not a no-go for all Dwork or adelic methods and
not a selected signed estimate. No unsupported stronger conclusion found.

Addendum reviewed SHA256 values:

- DWORK_AND_ADELIC_BOUNDARY.md: `1d90d6b850f37190d7304ba6a1a9da1b3701031ec99a6dc53f3cd511c98ce538`
- direct_diagonal_probe.py: `ce88204ef719ff76af3a22ed419a525738f9dc0be88289045b8ba9407ddaf4fb`
