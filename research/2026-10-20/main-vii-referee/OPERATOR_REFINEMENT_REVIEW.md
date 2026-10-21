# Referee review: exact two-moment constrained inverse

Status: **PROVED LOCAL** for the reviewed finite-rank inequalities; **TESTED
MODEL** for the finite integration and certificate arithmetic. This is a
separately tasked same-model review, not an external referee or formal proof.
The subject is the operator lane's `CLOUD_EXACT_MOMENT_INVERSE.md`, its new
`cloud_exact_moment_inverse.py`, and its exact J=10, M=96 source receipt. The
reviewed implementation and receipt are pinned by SHA256 in
`operator-symbolic-holdout.json`.

## Proof reconstruction

Let `B` be bounded self-adjoint on a Hilbert space, `B>=kappa I>0`, and let
`L` have finitely many linearly independent columns. Write `E=ker L*`,
`G=L*L`, and `M=L*B^{-1}L`. For `r in E`, completing the square subject to
`L*u=0` gives

\[
 u=B^{-1}r-B^{-1}LM^{-1}L^*B^{-1}r,
 \qquad
 \sup_{u\in E}\{2\Re\langle r,u\rangle-\langle Bu,u\rangle\}
 =\langle r,B^{-1}r\rangle-z^*M^{-1}z.
\]

The error from any other admissible `u` is its positive `B`-energy distance
from this maximizer. A densely defined closed coercive form on a closed
subspace `E' subset E`, with a larger energy than `B`, has an inverse
quadratic form bounded by the displayed supremum. This follows directly from
its variational representation, including an unbounded associated operator.
It does not authenticate an arithmetic realization of that form.

If `U>=M>0`, inverse order gives `M^{-1}>=U^{-1}`. Therefore the claimed
additive saving is valid when the *checked* difference
`R=U^{-1}-kappa G^{-1}` is PSD. Keeping only the positive part of an
indefinite difference would be invalid; the implementation rejects that route.

For the shift operator on `[-1/2,1/2]` with `1/2<b<1`, its edge cells form
disjoint two-point pairs. On each pair the comparison operator is exactly
`[[kappa+w,-w],[-w,kappa+w]]`; its eigenvalues are `kappa` and `kappa+2w`.
The middle scalar is `kappa+w`. Inverting those matrices independently
recovers the stated piecewise inverse coefficients. This establishes both
`B^{-1}<=kappa^{-1}I` and `B<=(kappa+2w)I` in the relevant realization.

Moving `b` by at most `db` changes the cell designation on measure at most
`2db`. There the difference of two inverse values is at most `2 sup|h|/kappa`.
On the remaining set only the translated polynomial changes, by at most
`beta db sup|h'|`. Integrating against bounded `p` gives precisely
`db sup|p| (4 sup|h|/kappa + beta sup|h'|)`. The argument does not demand
continuity of a piecewise residual at its nominal boundaries.

The Gram error is Hermitian. Symmetrized entry bounds give its row-sum norm
bound and hence the Loewner upper `M_b<=M_b0+rho I`. Upward rounding by less
than one grid unit per entry plus the two-grid-unit diagonal safety charge
preserves that upper. The *total* increase on a diagonal is less than three
grid units; the operator lane corrected its function docstring accordingly.

For moment error matrix `Delta` and PSD `R`, reverse Young gives

\[
 (Z_0+\Delta)^*R(Z_0+\Delta)
 \succeq(1-\theta)Z_0^*RZ_0-(\theta^{-1}-1)\Delta^*R\Delta.
\]

The last matrix is PSD and at most its trace times the identity. Replacing
the trace summands by `|R_jk| e_ji e_ki` gives the claimed uniform matrix
penalty, including its indices and coefficient. For actual residual errors
with norms `delta_i`, ordinary Young and the constrained inverse norm bound
give the separate penalty `(1+1/eta) sum_i delta_i^2/kappa`. Thus improving
the nominal inverse saving increases the Schur *lower* by `1+eta` times the
new saving. No source-action error is removed or counted as a signed gain.

## Method ceiling

The upper bound `B<=(kappa+2w)I` implies
`M>=G/(kappa+2w)` and therefore
`M^{-1}<=(kappa+2w)G^{-1}`. The constraints are orthogonal, so the diagonal
of the complete possible two-moment correction is at most

\[
 (\kappa+2w)\sum_j
 \frac{(|Z_{0,ji}|+e_{ji})^2}{\|h_j\|^2}.
\]

With the ambient comparison certificate, trials, Young parameter, and
source-action error budget fixed, adding `1+eta` times this cap bounds the
largest possible corrected *certificate diagonal*. A negative cap rules out
a PSD lower certificate from this refinement alone. It says nothing about
the sign of the true source Schur complement. The four reported ceilings
are strictly negative and have been recomputed from outward rational parents
recorded in the source receipt.

## Independent computational checks and dependencies

The referee's `main_vii_operator_holdout.py` constructs the edge/middle inverse
formula afresh and uses SymPy polynomial integration, rather than the project
antiderivative or Simpson implementations. At three rational nominal shifts,
two parities, positive and zero prime weights, and five shifted test points,
all 60 exact Gram checks pass. A separate `Fraction` principal-minor oracle
checks both Loewner upper constructions. This finite sample supports the
implementation; the moving-boundary argument is the uniform proof.

The same oracle verifies strict positive definiteness of both exact and
Simpson additional gain matrices, exact additivity to the prior certificate,
negative definiteness of the resulting *lower* matrices, and all four
method-ceiling computations. Every implementation hash recorded in the source
receipt is checked against the files actually inspected.

The original signed-source identification, the all-high comparison
`D>=B_b`, fitted trials, and original source-action/Gamma-tail error estimates
remain shared dependencies. This review does not pretend that another finite
integration algorithm independently proves those analytic facts. No zero
ordinate, synthetic PSD replacement, or changed source coefficient enters
the new refinement. The gain and the ceiling theorem are accepted in their
stated conditional source setting; the authentic signed S4 sign and RH remain
open.
