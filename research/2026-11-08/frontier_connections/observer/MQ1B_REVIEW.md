# Incremental independent review of MQ1b and the stronger controls

Verdict: **SURVIVES**, for the exact hypotheses stated in the arithmetic
front. This review was added after the first MQ1–5 cross-review; its exact
proof-file hash is in [the receipt](MQ1B_REVIEW.json).

For degree D, expanding the 2D-th power produces two ordered D-tuples.
The p^D character sum is nonzero exactly when their first D power sums
agree. The condition p>D makes every Newton divisor1,...,D invertible, so
the two monic root polynomials agree. Their root multisets therefore agree,
including repeated roots. For multiplicities k(x), each tuple has exactly
D!/product k(x)! orderings; two independent orderings give the square in
MQ1b. Their complex weights multiply to product |B(x)|^(2k(x)). The
normalization p^D/m^(2D) is correct. D=1 gives Parseval and D=2 gives MQ1.
This proves the displayed general formula and its pointwise phase blindness.
It does not extend that blindness to arbitrary higher moments or the labelled
intensity chart, and the text correctly avoids that extension.

The amplitude-matched control B_coh(x)=|B(x)|e_p(-h x) preserves every
pointwise magnitude, and its target is mean|B|. The inequality mean|B|>=E
uses precisely |B|<=1. It is a valid observer control, not an alternative
source-authenticated zero history.

Multiplication by e_p(c x) shifts the b coordinate of the complete quadratic
chart bijectively. Hence B0=e_p(-h x) and B1=e_p((c-h)x), c!=0, have identical
unordered intensity multisets; their selected targets are1 and mean e_p(c x).
The stated subgroup character bound min(1,sqrt(p)/m) is the existing arithmetic
bound. It is nontrivial when m>sqrt(p); the text does not require strict saving
for every smaller subgroup. Preserving the chart without its target label
therefore does not preserve a cancellation verdict.

As a finite algebra cross-check, independent enumeration grouped ordered
tuples by their power-sum vectors for p=3,5,7 and D<=min(4,p-1), using
S={0,1,2}. All10 cases (252 ordered tuples) had one multiset per fiber and
the required multinomial cardinality. Nonconstant positive amplitudes x+1
also reproduced the weighted collision sums, recorded in the receipt.
These finite checks are supplementary; the Newton argument supplies the
universal quantifiers. No source test or new normality evidence is claimed.
