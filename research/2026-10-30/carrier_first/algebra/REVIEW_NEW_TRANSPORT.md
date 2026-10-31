# Independent reconstruction of the new analytic and prime-frame transport

This is a same-model review with a separately written exact probe, not an
external referee. The reviewed bytes are pinned in
`receipts/new-transport-review.log`:

* analytic/ANALYTIC_TRANSPORT.md:
  `447de1597b52e1363fb4422faea080627ed1b3c78dc3d3169906f0a435cf9b7d`
* selected/HIGH_ORDER_FRAMES.md:
  `8c0d2fa3e27ad68095ddf6237e10c04524c112f19e409ab0d6cd5f123ef2c32a`
* OBSERVER_THEOREMS.md:
  `22becab5c35fde90f7780294d984fa18cab6d41c0803d7bfb9c23234c8c788f1`
* observer.py:
  `118a4a3b1d1d21de85be84c86c482351bbb3b7505fa4db6d7ed3e02d8ccd5a98`

## Analytic transport: A01–A05 survive

1. **Markov identity and moment count.** Multiplication of the first
   resolvent remainder by p_d(t), followed by orthogonality of
   `(p_d(t)-p_d(x))/(t-x)`, gives the stated square-polynomial remainder.
   The p_d linear system uses moments through2d-1; q_d needs only the
   first d, but depends on p_d. The norm h_d needs moment2d. Thus center
   versus sharp interval costs are respectively2d and2d+1 source samples.
   Strict positivity of the density makes both inequalities in A2 strict.
2. **Uniform constant.** The monic shifted Chebyshev factor is
   `2^(1-2d)`. Combining its squared supremum with mass47/15 and
   `p_d(16)>15^d` yields exactly188/(225*3600^d). The claimed improvement
   is asymptotic in degree; the dossier correctly does not claim that the
   coarse envelope wins for every small degree. Chord transport multiplies
   this by2pi|h|16^n, as stated.
3. **Gaussian countermodel.** Positive weights and real nodes follow by
   orthogonality/interpolation. Rational polynomial coefficients and initial
   moments give all future moments rational by recurrence. The first
   unmatched moment differs by h_d, since p_d^2 is monic of degree2d and
   vanishes on the Gaussian nodes. The sum of future tails uses
   `x/[(1-x)(16-x)]=[1/(1-x)-16/(16-x)]/15`, giving exactly B_d.
   The Hankel rank argument needs d atoms and is valid. Its coherent fixed
   frequency depends on the rational denominator and is properly declared.
4. **Theta strip certificate.** The factor-of-two accounting yields
   `1/[s(s-1)]` in Lambda, with no extra half in the summed integral.
   Differentiating ell times contributes2^(-ell); summing the two powers
   and bounding the Gaussian denominator yields2^(2-ell). With
   C=3(M+1)^2, integration by parts and exp(-C)<2^-C give A7. The pole
   terms cancel in the remainder. This controls truncation, not rounding.
5. **Prime germ and its finite-jet counterfeit.** The normalized functional
   equation contains cos(pi z/2), not sin or a negative sign. Its corrected
   k-th derivative is moment k-1 of the stated positive measure. Complete
   moment uniqueness follows from positive exponential integrability and
   analytic Laplace uniqueness. The finite perturbation changes every
   mass by at most half the smallest affected original mass; its first K
   moments vanish by Pascal differences and the next does not. It violates
   the exact von Mangoldt divisor identity already at2, so it is a weighted
   fake, not a counterexample with the original arithmetic source. A10's
   cutoff X>=2^k ensures log X>=k log2>k/2, enough for the integral test.

## High-order frames: ST1–ST6 survive

The even derivative source bound is
`4(2m)!/(1/2)^(2m+1)=8*4^m(2m)!`; summing chronological powers gives
the required geometric factor. In the Hermite proof, the center zero is
double, so the total multiplicity is2m+2 and Rolle gives a zero of the
derivative of order2m+1. This justifies the differentiated remainder
without differentiating an unspecified intermediate point. The sign
`(-1)^m` and the factor h^(2m)(m!)^2 are correct.

The factorial bound gives2^(1-m), and the chosen
`m_n=4n+ceil(log2((n+1)^2))+4` gives the stated n^-3 envelope and1/315
total budget. Cubing the Hilbert comparison constant independently gives
`9pi/(80sqrt6)`, so the H^(5/6)/N estimate and vanishing H~N error are
correct. These are transport errors, not upper bounds on selected energy.

The total variation4mH_m, source-power amplification, and signed prime-log
error are retained. The denominator passport is valid because every
forcing denominator divides D_n and the multiplier16 is integer. The
one-sided Hermite enlargement has width less than1/D_n and contains U_n,
so exactly one grid point exists. That proof establishes finite exact
readout under the specified initial germ, not a universal identification
of arbitrary germs from the same finite observations.

## Executed checks and remaining scope

`new_transport_review.py` imports neither new front implementation. It
uses rational-function identities for two finite measures, rational
orthogonal-polynomial reconstruction of the authentic source at d2,4,6,
a separate80-term BBP interval, exact Gaussian moment defects,90 prime-germ
moment cases and180 Hermite monomials. All pass. These finite checks
corroborate the implementations and the independent algebraic derivations;
they do not replace the unbounded proofs above.

Parent observer validation was refreshed after adding the source-id,
nonnegative clock and carry-length checks. The previous API concern is
resolved. All768 CDF-W1 and2,046 brute lasso cases still pass in
`receipts/observer-review-refreshed.log`; the older receipt is preserved.
No required mathematical revision was found. None of the reviewed
theorems closes the original selected signed-cancellation obligation.
