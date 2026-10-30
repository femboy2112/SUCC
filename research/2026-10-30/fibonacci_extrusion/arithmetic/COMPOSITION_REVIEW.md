# Complementary paper review: FIC01 and FIC05

Reviewed `../composition/FIBONACCI_COMPOSITION.md`, SHA256
`6a7df2ce932b9251ca546878118ba4238c83947bff2c93aa3e36feea6263db4c`.
Scope is only FIC01's uniform-in-rank remainder and FIC05's entire common-age
classification, not blanket certification of every composition statement.
This is a same-model sibling review, not an independent external referee.

**FIC01 survives.** The source-mixture representation makes the difference
exactly an expected log-sum-exp minus the coordinate mean. Its linear term
cancels by exchangeability, independently of k. The second-order coefficient
is (1-E sum w_i²)/2=(k-1)/(2k+1), so no hidden k factor remains. The third
derivative is the third centered moment of a law in an interval of lengthL;
its absolute value is at mostL³. This supplies a uniform remainderL³/6.
For the variance comparison, the tilted density bounds imply
(1+x)^(-2) sigma²<=Var_nu T<=(1+x)^2 sigma² by the infimum-over-centers
formula. The pairwise formula and the derivative range of log(a+T) add
another (1+x)^(-2) only to the lower bound. Therefore the paper's
sigma²(1+x)^(-4) lower bound is justified, rather than an accidental square
of an unjustified comparison. For x=5/a<=1, the stated constant1627/45
is correct. Consequently the joint growing-k,growing-a limit is paid for
by a uniform estimate; it is not an exchange of unproved limits.

**FIC05 survives for the exact stated nonnegative-weight domain.** Positivity
and Q(x)->4 force the source mgf convergence boundary exactly at a. A weighted
sum with largest positive weightw therefore has boundarya/w. Output equality
after tilting forces t=sw. At that t, strict monotonicity m'_a=-v_a<0 makes
any smaller positive weight give a strictly positive mean discrepancy. This
rules out accidental equality of the endpoint laws, not merely a mismatch
of proposed input ages. Equal positive weights are sufficient by exponential
tilt factorization. A zero weight contributes no endpoint information and is
correctly excluded from the equality requirement. Signed weights would need
another proof and are not claimed. The source-age clock is declared; none
of these arguments identifies it with the BBP selected phase clock.

**Fresh exact checks, executed.** `composition_review.py` imports neither
composition implementation. It reconstructs the bounded-rate moments by
polynomial integration, obtains variance1379/900, checks the exact remainder
constant, and derives Dirichlet moments from factorial Gamma ratios at
k2,3,7,29,101. Four rational clock families test both endpoint means and
Laplace transforms at a fresh positive frequency: unequal weights2/3,7/5
and3,8 differ; zero/nonzero weights0,9/4 and equal weights5/3,5/3 agree at
the uniquely forced clock. Raw rational gaps and the reviewed hash are in
`composition_review_receipt.json`; stdout is in `composition_review.log`.

No defect requiring a theorem correction was found in these two claims.
Their source-only scope remains decisive: they survive the coherent changed
seed and provide no source-selected normality proof on their own.
