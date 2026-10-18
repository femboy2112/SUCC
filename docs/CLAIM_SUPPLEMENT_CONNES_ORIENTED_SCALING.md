# COT — Connes local scaling, orientation, and missing global trace

**Pinned parent:** research/direct-quotient-pontryagin-transfer-2026-10-17@c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d.

**Evidence:** research/2026-10-18/CONNES_ORIENTED_LOCAL_TRACE_BRIDGE.md; observational_succ/connes_oriented_scaling.py; tests/test_connes_oriented_scaling.py. Imported local-field analysis, Tate/product formula, Connes (math/9811068 §V Theorem 3), Connes–Consani (arXiv:2006.13771 Theorem 1) remain attributed classical mathematics.

| ID | Status and precise claim |
| --- | --- |
| COT-01 | **PROVED EXACT**: source SUCC x↦x+1 fails descent to multiplicative X=A_Q/Q^× (diagonal -1~-1/2 gives inequivalent 0 and 1/2). Distinguish additive A/Q from multiplicative A/Q^×. |
| COT-02 | **PROVED EXACT SOURCE CHART**: rational diagonal p is gauge (idèle norm 1); one-place idèle p has norm 1/p and is a different class, checked via inherited RationalChartIdele. |
| COT-03 | **PROVED LOCAL**: finite delta fixed-point coefficient on bZ_p is p^-vp(b) p^min(vp(a-b),r), which equals |1-a/b|_p^-1 at r>=vp(a-b). Nonunit denominators retained; inadequate depth falsified. |
| COT-04 | **PROVED LOCAL**: C_p(u)^2=|u|_p/|1-u|_p² is invariant under u↔1/u. Bare fixed-point coefficient generally isn't. |
| COT-05 | **PROVED CLASSICAL**: for rational u≠0,1, the all-place diagonal product of C_v(u)^2 is exactly 1. This is not Connes trace/Weil positivity. |
| COT-06 | **PROVED LOCAL; GLOBAL UNVERIFIED**: p^k yields half-density p^-k/2; log(p) primitive length and correct signed full trace remain separate obligations. |
| COT-07 | **PROVED TOY COUNTERMODEL**: C_3(4)=3 and artificial identity contact c=1 yield Gram [[1,3],[3,1]] with negative eigenvalue -2, unchanged by orientation inversion. This does not apply to zeta's true contact. |
| COT-08 | **UNVERIFIED**: global Connes cut-off principal-value trace, analytic operator-domain control, test-distribution identity with source-authentic completed Weil, positive factorization and RH. |

**Mutations/controls:** fake p=6, real p=2 and p=3, u=1 singular contact, depth below stabilization, rational nonunit, inverse without half-density, non-descending affine event, diagonal-versus-one-place idèle, improper source ID/epoch, diagonal all-place cancellation, arbitrary contact negative Gram. Only positive/refutation statements with proof scopes listed above.

**Run:** python -m unittest discover -s tests -p 'test_connes_oriented_scaling.py' -v. Local dry run with two strict upstream interface adapters: ten tests OK; actual GitHub integrated CI separately required and not presumed. **RH PROVED: NO.**
