# AV-08: signed folding of the original BBP shear and its sharp positive total

**Date: 2026-11-04. Status: proved paper identity/asymptotic; exact rational tests.** Addendum to AV-01..AV-07. This derives a sharper bound for the *source forcing part* of the valve. It does not prove any absolute-flow or near-collision decay.

For \(A\ge2\) define the total positive chronological shear over all eligible distinct-pair transitions in epoch [A,2A):
\[
S_A=\sum_{d=1}^{A-1}\sum_{n=A}^{2A-d-2}
[r(n+1)-r(n+d+1)].
\]
(When the inner range is empty its sum is zero.) This is strictly positive, but it folds into the **signed** single sum
\[
\boxed{S_A=\sum_{k=A+1}^{2A-1}(3A-2k)r(k).}\tag{AV-13}
\]
**Proof:** For each fixed d, telescope the inner difference to \(\sum_{j=1}^d r(A+j)-\sum_{j=1}^d r(2A-d-1+j)\). On summing d, the first sum counts each r(k) \(2A-k\) times and the second counts it \(k-A\) times. Their coefficient is \(3A-2k\). Thus a positive two-time integral reduces to a signed one-time sum, with the sign flipping near \(k=3A/2\). No cancellation of selected real phases is inferred.

The original four-pole rational function has the independently verifiable Laurent expansion
\[
r(k)=\frac{15}{64k^2}+O(k^{-3})
\quad(k\to\infty).
\]
Uniformly on \(k\in[A+1,2A-1]\), substitute this into AV-13. The total error is \(O(A^{-1})\), because each coefficient \(3A-2k=O(A)\), each forcing remainder is \(O(A^{-3})\), and there are \(O(A)\) summands. The leading sum is a Riemann sum for the continuously differentiable function \(f(x)=(3-2x)/x^2\) on [1,2], with error \(O(A^{-1})\). Therefore
\[
\begin{aligned}
S_A
&=\frac{15}{64}\int_1^2\frac{3-2x}{x^2}\,dx+O(A^{-1})\\
&=\boxed{\frac{15}{64}\left(\frac32-\log4\right)+O(A^{-1})}.
\end{aligned}\tag{AV-14}
\]
The constant is positive, approximately \(0.0266497591125\). The limit uses ordinary real calculus and no hypothesis about zeta zeros.

This sharpens the absolute signed-source flux budget in AV-03 **exactly at every A**:
\[
\boxed{
\left|\frac q{A^2}\sum_{d=1}^{A-1}\sum_{n=A}^{2A-d-2}
(L_q-I_q)(\delta_{n,d})\right|
\le\frac{q(A-1)}{A^2}+\frac{q^2}{A^2}S_A.}\tag{AV-15}
\]
For the logarithmic q schedule, the right side is \(q/A+(15/64)(3/2-\log4)\,q^2/A^2+o(q^2/A^2)\). The \(S_A\) term is a sharp **total positive shear budget**; it is not asserted to be the exact net signed arc flux, whose sign can vary. In particular, this is **not** a new bound on the positive leakage or lateral reinjection separately.

Two independent Fraction computations—original double sum and folded signed one-dimensional sum—agree exactly for A=8,12,24,40,64. Additional finite values approach the limit from below in the development grid, but this empirical observation is neither needed nor promoted into a monotonicity theorem. No π digits and no Galois averaging enter.

**Open after AV-08:** source-selected early escape/near-pair upper bounds at q_A≈log A. All prior firewalls survive; π-normality, signed Weyl, RH OPEN. No originality priority.
