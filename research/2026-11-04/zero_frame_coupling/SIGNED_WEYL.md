# Direct signed-cancellation attempt: keep the mixed term

For the original source, `u_n=e(HU_n)=e(HY_n)e(HZ_n)`. On any consecutive
interval I of N points, classical Cauchy differencing gives, for 1<=D<=N,

\[
\left|\sum_Iu_n\right|^2\le\frac{N+D}{D}
\left[N+2\sum_{d=1}^{D-1}(1-d/D)
\Re\sum_{n,n+d\in I}e(H\Delta_dY_n)e(H\Delta_dZ_n)\right].
\]

This was the first serious attempted selected saving. The radial difference
has a monotone oscillatory phase. Replacing the mixed mean by the product of
its two marginal means would give a useful bound **if** a sufficiently small
source-conditioned covariance were proved. It is not a valid general step.

For the same four-pole forcing with coherent seed `s*=-pi/16`, let
`a_n=e(H Delta_dY*_n)`, `b_n=e(H Delta_dZ_n)`, and E average over
[A,2A-d). For each fixed positive d at the actual critical schedule,

\[
|Ea_n|=\Theta_d(1/\Lambda),\quad |Eb_n|=\Theta_d(1/\Lambda),\quad
\boxed{E(a_nb_n)-(Ea_n)(Eb_n)
=1+O_d(\Lambda^{-2}+\Lambda/A).}
\]

The proof is exact: `a_n b_n=e(-H Delta_dT_n)` and
`0<T_n-T_(n+d)<d/(32n^3)`. The two separately dephasing marginals compensate
almost perfectly. The changed initial condition is the precise hypothesis
excluding this control from the original theorem. Forcing identities,
radial repayment, all jets and lag Gram spectra do not exclude it.

The second attempt kept the full carry word. With `x_n={U_n}` and the
literal carries c, put

\[
S_d(n)=\sum_{j=1}^d16^{d-j}r_o(n+j),\quad
K_d(n)=\sum_{j=1}^d16^{d-j}c_{n+j}.
\]

Then `x_(n+d)=16^d x_n+S_d(n)-K_d(n)` exactly. Integer characters remove
K_d from the exponential, but the simultaneous inequalities
`0<=16^j x_n+S_j(n)-K_j(n)<1` retain the actual allowed carry cell.
Partitioning by these cells is exact. Bounding their *realized* signed visit
counts is the first missing estimate. Equating their counts to their lengths
assumes distribution that has not been proved; using worst-case counts gives
no saving. The new lag Bessel theorem cannot fix this, because the angular
amplitude `e(H Delta_dY_n)` changes with d and is not one common test vector.

A third attempt compensated the leading tail with
`W_n=U_n-(Z_(n+1)-Z_n)/2`. It gives
`W_n=16^n alpha-11/(512n^3)+O(n^-4)` and an additive O_h(log A/A)
comparison of the compensated high-frequency maximal mean with the original
fixed-h maximal mean. The latter is still unknown. Undoing the compensation
restores the nonconstant phase multiplier. This is exact useful transport,
not contraction. [Complete derivations CF-3/4](front_cf/PROOFS.md).

No source-selected little-o has been obtained through these attempts.
The analytic stencil obstruction is separately proved in [BE-03](front_be/PROOFS.md);
it does not prohibit a nonlinear arithmetic argument using the actual carries.
