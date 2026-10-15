# CLAIM SUPPLEMENT — ONE OBJECT contact / relative-Neumann residual

**2026-10-15. Research branch:** research/one-object-residual-schur-2026-10-15. **Exact mathematical parent:** PR #104 at 88eca261bae1381b83d018163d0945c3434a3385, original integrated main 03db44203147a7b28d445bb9f970fa71360e78c4. **Sibling read-only primary work:** Tate conductor/Fourier PR #103 and Connes contact/Weil–Suzuki PR #106. **RH OPEN.** All proof and test boundaries: [ONE_OBJECT_RESIDUAL_SCHUR.md](../research/2026-10-15/ONE_OBJECT_RESIDUAL_SCHUR.md).

| Claim | Status | Exact hypothesis / essential limitation |
|---|---|---|
| ORS-01 | CLASSICAL SUZUKI / PROVED LOCAL identity | \(W_c=W+c\delta_0\implies g_c=g-c|t|/2\implies G_{a,c}=G_a+cK_a\) on L0²; \(Q_{W_c}(v)=Q_W(v)+c\|v\|²\). Contact coefficient c is a hypothetical **mutation**, not a second genuine Euler place or claimed Connes-normalized value. |
| ORS-01b | PROVED LOCAL with genuine inverse-Neumann source | At a=1/2, P=Legendre modes 1..30, \(QKP\) has rank exactly 2 with raw entries \(K_{29,31}=-1/906948\), \(K_{30,32}=-1/999180\). Contact changes A, B and D blocks together. No finite off-origin prime trace can determine contact coefficient c. |
| ORS-01c | PROVED CONDITIONAL | If genuine high D≥κQKQ, contact mutant D_c≥(κ+c)QKQ. When κ+c≤0 the certificate loses positive margin; no conclusion that D_c itself is negative. |
| ORS-02 | PROVED MATHEMATICALLY, classical Hilbert duality | For bounded compact self-adjoint G with finite low/high split, D≥κQKQ, r=B-DY∈H1, \(L_Y=Y^*B+B^*Y-Y^*DY\) and \(T_r=(\langle r_i',r_j'\rangle)\), the zero-shift variational response \(R_0\) is finite and \(L_Y\preceq R_0\preceq L_Y+\kappa^{-1}T_r\). No infinite D^-1 inversion is taken. |
| ORS-02a | PROVED LOCAL exact Fraction toy | Partial Galerkin Y improves an otherwise inconclusive sign margin; full finite rational inverses and exact principal minors independently verify bounds, including negative controls and singular PSD. **Synthetic matrices are not original signed Weil.** |
| ORS-02b | PROVED toy obstruction | D=K=diag(n^-2), b_n=n^-2: zero-shift scalar response is finite but D^-1b not in ℓ²; residual H1 tail <=1/N. b_n=1/n is ℓ² but lacks H1 range and its response diverges. Exact mathematical countermodels, NOT Euler mutations. |
| ORS-03 | PROVED CONDITIONAL on original ancestor high coercivity | Main's authentic source κ=369/10000 at a=1/2, genuine Gamma derivative-tail δ_J=963[(4J+1)^-1+4(4J+1)^-2], independent source-authenticated derivative residual Gram T_J implies \(R_0\preceq L_Y+\kappa^{-1}[(1+\eta)T_J+(1+\eta^{-1})\delta_J²(I+Y^*Y)]\). Parent high/range theorem is imported, source SHA rechecked. **Authentic T_J and Y are NOT computed here**; input Gram merely being PSD is no source certificate. |
| ORS-03b | PROVED LOCAL exact rational source schedule | Given separately verified \(\|Y\|\le M\) and ε>0, \(J=\max(1,\lfloor1926(1+M)/(4ε)\rfloor+1)\) yields source Γ tail response ≤ε. Does not prove residual itself vanishes, or that supplied M is genuine. |
| ORS-04 | UNVERIFIED source-specific approximation | There exists a finite, efficiently authenticated genuine parity-preserving Galerkin response Y_N with derivative residual Gram upper→0. Not implied by Douglas range or finite tests. |
| ORS-05 | UNVERIFIED original local sign | Actual original source A, low/high B,D, finite-J derivative Gram T_J and a positive 15+15 parity Schur lower matrix at a=1/2. No source-identified successful sign matrix was produced. |
| ORS-06 | UNVERIFIED global | All-a uniform source-specific high-positive complements/short matrices and a Tate–Connes globally normalized trace identity on full correct Schwartz–Bruhat common test space. |
| RH | UNVERIFIED/OPEN | Weil positivity on all proper H0¹ tests, all support radii. No nontrivial zero ordinates are used as source inputs, no circle/Hilbert covariance or Tate symmetry is called proof of RH. |

**Primary papers:** Suzuki arXiv:2606.09096v3 equations (1.3),(1.5),(1.8),(8.2); Connes arXiv:math/9811068 local Theorem 3 and principal-value normalization; Tate original adelic harmonic-analysis thesis (classical), conductor-sensitive representation from sibling PR #103; ONE OBJECT finite contact gluing from sibling PR #106 is not silently merged. All signed source arguments preserve true Λ(p^k)/sqrt(p^k), one Gamma, exact contact and pole signs, half-density, proper meanzero derivative domain and source-vs-model labeling.

**Reproduction**:
- observational_succ/one_object_relative_residual.py — exact principal-minor finite relative-Schur toy proof/negative cases;
- observational_succ/one_object_source_residual.py — pinned original source range/κ, conditional source Gamma residual, exact resource schedule;
- observational_succ/one_object_contact_neumann.py — independent contact antiderivative/absolute-kernel identity, actual K rank-two channels;
- tests/test_one_object_relative_residual.py, tests/test_one_object_source_residual.py, tests/test_one_object_contact_neumann.py;
- scripts/one_object_residual_probe.py --verify research/2026-10-15/ONE_OBJECT_RESIDUAL_RECEIPT.json;
- dedicated .github/workflows/one-object-relative-schur.yml on Python 3.10 and 3.13 with PR #104 ancestor + original source regressions/provenance.

**Status of CI/Lean:** verify the exact branch SHA and GitHub Actions; no Lean kernel proof claimed, full repository suite is independent of dedicated feature CI. No main modifications, releases, cross-repo publication or academic priority claims.


**ORS-01d — PROVED ALGEBRAIC / finite exact hostile example:** The original genuine contact shift satisfies the *whole* generalized Suzuki pencil identity \((G+cK)-\mu K=G-(\mu-c)K\). Thus wherever the high-block Schur complement is lawfully defined, it must transform by exact parameter translation; correcting only low matrix A while keeping cross B and high D fixed violates the SAME arithmetic-object representation. Rational 3×3 SPD-K example with nonzero K cross tests the wrong-low-only difference; source is a declared toy, not a new result that the actual high compact D has bounded inverse.
