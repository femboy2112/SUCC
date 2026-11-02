# GF-07 — a single PERFECT-SQUARE finite arithmetic bound suffices

**2026-11-02, research-only paper proof.** Addendum to GF-02/GF-04, not a claim of π normality. It is a sharper quantifier target, using an elementary density-one checkpoint interpolation. The original four signed source poles, literal U_0=0 and all Gamma/Fejér claims remain unchanged.

## Statement: prove only an L × L energy inequality

For each integer L≥2 set N=L², H=L, and define the exact original rational completion
\[
\alpha_{L^2}=\sum_{j=1}^{L^2}16^{-j}
\left(\frac4{8j-7}-\frac2{8j-4}-\frac1{8j-3}-\frac1{8j-2}\right).
\]
Define the finite arithmetic-positive pair energy
\[
\boxed{\mathscr Q_L=
\frac1{L^4}\sum_{0\le n,m<L^2}
F_L\big(16^n\alpha_{L^2}-16^m\alpha_{L^2}\big).}
\]
This is a concrete real trigonometric expression of exact rational source states, with NO circular π-digit observation in the definition.

**GF-07 — rigorous conditional theorem.** If there is some real constant C<∞ such that
\[
\boxed{\mathscr Q_L\le C\qquad\text{for every sufficiently large integer }L,}
\tag{SQUARE-GATE}
\]
then π is normal to base 16.

**Proof.**
1. GF-04 and the original positive Gamma source give
\[
|\mathcal E_{L^2,L}(\pi/16)-\mathscr Q_L|
\le\frac{4\pi L(L+2)}
{45L^2(8L^2+1)(8L^2+2)}
<\frac{\pi(L+2)}{720L^5}=O(L^{-4}).
\]
The final strict bound uses (8L²+1)(8L²+2)>64L⁴. This error is also bounded strictly by the *rational* 11(L+2)/(2520 L^5), using π<22/7.
2. For each fixed h≠0, put K_L=floor(log_16(L/(2|h|)))+1 for all sufficiently large L. Then K_L→∞, K_L<L², and 2|h|16^(K_L−1)≤L. GF-02 yields
\[
|c_{L^2}(h)|\le\sqrt{(C-1+O(L^{-4}))/K_L}+(K_L-1)/L^2\longrightarrow0.
\]
3. For an arbitrary N, choose L=floor(sqrt N) and L²≤N<(L+1)². The unnormalized difference between the length-N and length-L² character sums has modulus at most N−L²≤2L. Thus
\[
|c_N(h)|\le |c_{L^2}(h)|+\frac{2L}{L^2}\longrightarrow0.
\]
Classical Weyl criterion completes the **conditional** proof. QED.

The conditional effective rate is O_{h,C}((log N)^{-1/2}). The all-prefix extension uses consecutive-square spacing, not an unjustified conclusion from the much sparser geometric sequence N=16^j.

## Why this is a worthwhile reduction—and what remains open

A single TWO-INDEX finite arithmetic expression, \mathscr Q_L, and ONE absolute constant C would replace infinitely many separate signed h-specific limits and the all-N hypothesis of GF-GATE. The grid L×L is a convenient finite checkpoint geometry (consistent with SUCC's carrier/triangle intuition), not an asserted mathematical identity forced by 4²=16. The Gamma tail certifies comparison to the analytic global π orbit with O(L^−4) cost. None of these facts supplies the upper bound.

**Exploratory noncertified L values** from exact original α_{L²} residues followed by double trigonometry:

| L | N=L² | observed Q_L |
|--:|--:|--:|
| 4 | 16 | 1.211481446 |
| 8 | 64 | 1.242204894 |
| 16 | 256 | 1.048075484 |
| 32 | 1024 | 1.025627056 |

This finite pattern is NOT an asymptotic bound. The exact coherent same-original-source altered real seed s=1/5−π/16 yields \mathscr Q_L=L+1 and violates SQUARE-GATE, while preserving the four poles and all Gamma/Pisot source identities. The selected original off-diagonal, joint prime/cofactor real-phase upper bound is the remaining UNVERIFIED arithmetic premise.

**Recommended next attack:** do not aim for \mathcal E→1 or every fixed h separately. Seek a direct source-specific, uniform-in-L estimate \mathscr Q_L=O(1) by splitting the Fejér collision kernel into exact p-primary newborn-prime and Archimedean cofactor contributions; preserve signed real embedding and U_0=0 throughout. Maintain sibling #469's 2-adic/real distinction and #468's signed dyadic cascade as separate alternatives.
