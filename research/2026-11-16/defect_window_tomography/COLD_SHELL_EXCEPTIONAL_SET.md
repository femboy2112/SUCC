# Cold-shell geometry and the arithmetic boundary

Independent translator bearing, 2026-11-16. Starting repository head:
`1f04b869182ad68deb764637034d72b19352ca48` (SUCC draft #657).
The root audit checked the complete paper proof and a second mathematical bearing
reviewed it. This is not independent external refereeing, a global novelty claim,
or a theorem that the endpoint pi/16 avoids the exceptional set.

## 1. An exact exceptional-set theorem

Fix a real aspect ratio lambda > 1. Put M_B = floor(lambda B),
L_B = M_B-B, and restrict to integers B with L_B >= 1. For x in [0,1], define

\[
E_{B,\lambda}(x)=\frac1{L_B}\sum_{n=B}^{M_B-1}\|16^n x\|_{\mathbb T}^2,
\qquad
\mathcal E_\lambda=\{x:\liminf_{B\to\infty}E_{B,\lambda}(x)=0\}.
\]

**CSE-01 (PROVED PAPER; scope below).**

\[
\boxed{\dim_H\mathcal E_\lambda=1/\lambda.}
\]

Moreover, E_lambda is a dense G_delta subset of [0,1]. Thus the exact bad
set for the dyadic-shell R0 target has Hausdorff dimension 1/2, despite being
topologically residual. Its complement has full Lebesgue measure and is
meagre. This differs from the previously proved dimension 7/8 for failure of
the particular sufficient carry gate: those are different exceptional sets.

No conclusion concerning membership of pi/16 follows from the dimension.

## 2. A finite balanced-carry cover

For a real y let N(y)=floor(y+1/2), choosing this convention also at ties.
Set

\[
q_n=N(16^n x),\qquad t_n=16^n x-q_n\in[-1/2,1/2),
\qquad a_n=q_{n+1}-16q_n=16t_n-t_{n+1}.
\]

The a_n are integers in {-8,-7,...,8}: the real interval for
16t_n-t_{n+1} is contained in (-8.5,8.5), whose only integers are those.
Write K for the number of nonzero a_n on B <= n < M_B. Pointwise,

\[
(16u-v)^2\le17(16u^2+v^2),
\]

because the difference of the right side and the left side is 16(u+v)^2.
Therefore

\[
\begin{aligned}
K\le\sum_{n=B}^{M_B-1}a_n^2
&\le289\sum_{n=B}^{M_B-1}t_n^2
  +17(t_{M_B}^2-t_B^2)\\
&\le289L_BE_{B,\lambda}(x)+17/4.
\end{aligned}
\tag{CSE1}
\]

This is a deterministic count of nonzero integer branches. No distribution
or independence hypothesis is used.

**CSE-02 (finite cover).** For epsilon >= 0, put

\[
J_B=\min\{L_B,\lfloor289L_B\epsilon+17/4\rfloor\}.
\]

Then {x in [0,1]: E_(B,lambda)(x) <= epsilon} can be covered by at most

\[
\boxed{(16^B+1)\sum_{j=0}^{J_B}\binom{L_B}{j}16^j}
\tag{CSE2}
\]

closed intervals of diameter 16^(-M_B).

**Proof.** q_B has at most 16^B+1 possible values. Choose at most J_B
nonzero positions and one of 16 nonzero signed digits at each. The recurrence
q_(n+1)=16q_n+a_n determines q_(M_B). The inequality
|16^(M_B)x-q_(M_B)| <= 1/2 places x in the interval centered at
q_(M_B)/16^(M_B) of diameter 16^(-M_B). Some codes are unrealizable or produce
the same interval; overcounting only strengthens this upper bound. QED.

## 3. Upper Hausdorff bound

Let h(p)=-p log p-(1-p)log(1-p), with 0 log 0=0. Fix small epsilon > 0
and a number delta with 289 epsilon < delta < 1/2. For all sufficiently
large B, J_B <= delta L_B. The elementary binomial estimate gives

\[
\sum_{j\le\delta L_B}\binom{L_B}{j}16^j
\le(L_B+1)\exp[L_B(h(\delta)+\delta\log16)].
\tag{CSE3}
\]

For every x in E_lambda the epsilon sublevel is visited at infinitely many
B. The total s-power of the above covers, summed over B >= N, is bounded
by a polynomial in B times a geometric series whose logarithmic exponent
per B tends to

\[
\log16+(\lambda-1)[h(\delta)+\delta\log16]
-s\lambda\log16.
\]

It is negative when

\[
s>\frac{1+(\lambda-1)[h(\delta)/\log16+\delta]}\lambda.
\]

Consequently the Hausdorff dimension is at most that expression. Let delta
decrease to 0, taking epsilon < delta/289 at each step, to obtain
dim_H E_lambda <= 1/lambda. This proof does not assert a finite bound at the
critical Hausdorff exponent.

## 4. Matching lower bound, including the measure estimate

Choose integers B_j increasing so fast that the intervals
[B_j+1,M_(B_j)] are disjoint and

\[
\frac{\sum_{i<j} M_{B_i}}{B_j}\longrightarrow0.
\]

For example choose a sufficiently large integer c > lambda+1 and use
B_j=ceil(c^(2^j)). Fix every radix-16 digit at positions B_j+1 through
M_(B_j) to zero, allowing all sixteen digits elsewhere. Let C_lambda be the
compact image of this product digit space in [0,1].

For x in this set and B=B_j, the fractional part of 16^n x on
B <= n < M_B is at most 16^(n-M_B), because all intervening digits vanish.
Hence

\[
E_{B_j,\lambda}(x)
\le\frac1{L_{B_j}}\sum_{k=1}^{L_{B_j}}16^{-2k}
<\frac1{255 L_{B_j}}\longrightarrow0.
\tag{CSE4}
\]

Thus C_lambda is a subset of E_lambda. Let F(N) count forced zero positions
among the first N digits and f(N)=N-F(N) count the free positions. During a
forced block F(N)/N increases and during a free block it decreases. At the
end of the jth forced block,

\[
\frac{F(M_{B_j})}{M_{B_j}}
=\frac{M_{B_j}-B_j+o(B_j)}{M_{B_j}}
\longrightarrow1-1/\lambda.
\]

Therefore liminf_N f(N)/N=1/lambda.

Choose independent uniform digits at free positions and deterministic zeros
elsewhere. This defines a Borel probability measure mu on C_lambda. Every
admissible symbolic depth-N radix cylinder has mass exactly 16^(-f(N)). Infinite free
positions ensure every individual endpoint has mass zero, so expansion
ambiguities do not affect the calculation. For every 0 < s < 1/lambda,
f(N) >= sN for every sufficiently large N. If
16^(-(N+1)) < |I| <= 16^(-N), then the interval I meets at most two depth-N
cylinder interiors. Thus, for all sufficiently small intervals,

\[
\mu(I)\le2\,16^{-sN}\le2\,16^s|I|^s.
\tag{CSE5}
\]

For any fine cover of C_lambda, summing (CSE5) gives a strictly positive
lower bound on the sum of the s-powers of its diameters. The Hausdorff
dimension is therefore at least every s < 1/lambda, proving the lower bound.

## 5. Residuality

Each E_(B,lambda) is continuous on the circle, since torus distance squared
is continuous. Consequently

\[
\mathcal E_\lambda=
\bigcap_{m\ge1}\bigcap_{N\ge1}
\bigcup_{B\ge N,\,L_B\ge1}
\{x:E_{B,\lambda}(x)<1/m\}.
\tag{CSE6}
\]

Every union in (CSE6) is open and dense: any radix rational p/16^k is in
that union, because E_(B,lambda)=0 for B >= k, and radix rationals are dense.
Baire's theorem proves density of the displayed G_delta intersection.
This argument is independent of the Hausdorff calculation.

## 6. Exact relation to the SUCC terminal norm

For x=pi/16, the existing VFM shadow estimate implies that

\[
R_B=\frac1B\sum_{k=1}^B\|U_{2B}/16^k\|_{\mathbb T}^2
\quad\hbox{and}\quad E_{B,2}(x)
\]

differ by a quantity tending to zero. Directly, the function
t -> ||t||_T^2 is 1-Lipschitz on the circle; its two source arguments differ
by 16^(-k)T_(2B). Thus

\[
|R_B-E_{B,2}(\pi/16)|
\le\frac{T_{2B}}{15B}(1-16^{-B})
<\frac{r(2B+1)}{225B}.
\tag{CSE7}
\]

So the actual target is exactly the exclusion pi/16 not in E_2. CSE-01
calibrates the size and topology of that exceptional set; it does not perform
this source-specific exclusion. The metric theorem remains a reduction.

## 7. Novelty tax and prior frontier

- Main XXV already characterizes R0 by positive binary-change density and
  supplies controls with restricted exponent zero that nevertheless fail R0.
  Repeating that density formulation would add no proof leverage.
- The preceding three-count dossier proves dimension 7/8 for failure of a
  stronger sufficient carry event. The present dimension 1/2 concerns
  *failure of R0 itself*, and the aspect ratio law 1/lambda identifies exactly
  how moving the shell boundary changes the failure-class dimension.
- The new finite cover (CSE2) is independently useful: it enumerates a class
  containing every cold endpoint at precision 16^(-M_B), with an exact
  finite support budget. It changes a per-orbit statistic into an explicitly
  countable family of sparse integer forms. This is a proved failure-class
  theorem, not a new pi saving.
- No global novelty is claimed. Moving-average multifractal spectra, digit
  frequency spectra and irregular/residual sets have extensive prior art.

## 8. Literature audit and limitations

Read primary-source text on 2026-11-16:

1. Jeffrey C. Lagarias, *On the Normality of Arithmetical Constants*,
   Experimental Mathematics 10 (2001), 355-368,
   https://arxiv.org/pdf/math/0101055 (arXiv v2, 2002).
   Theorem 3.1 establishes the perturbed-radix/true-radix tail comparison for
   arbitrary real forcing tending to zero. Hypothesis A adds a particular
   rational-function, literal-zero-seed restriction; it remains an assumed
   normality mechanism in that paper. Theorem 5.2 characterizes the G-function
   subclass by rational linear factorization of the denominator. This prevents
   treating holonomicity or tail shadowing alone as a statistical theorem.
2. Haibo Chen, *Hausdorff dimensions of level sets related to moving digit
   means*, https://arxiv.org/abs/1809.08000 and
   https://doi.org/10.1016/j.jmaa.2019.123649.
   Primary abstract read; full PDF not retrieved. It studies lower/upper
   moving digit means and their level-set dimensions. Exact transfer to the
   present fixed aspect-ratio liminf energy set is NOT asserted. It is a
   priority-check lead, not a load-bearing theorem.
3. Haibo Chen, Xiaohua Wang and Zhixiong Wen, *Multifractal analysis on the
   level sets described by moving averages*, International Journal of Number
   Theory 11 (2015), 2175-2189,
   https://doi.org/10.1142/S1793042115500967.
   Publisher full-text access failed; indexed abstract located. Not imported.
4. Lars Olsen, *Extremely non-normal numbers*, Math. Proc. Cambridge Phil.
   Soc. 137 (2004), publisher abstract at
   https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/extremely-nonnormal-numbers/F94676C5ECF93D68338480958C6BE17B .
   The abstract states residuality for an all-bases/all-word-frequency
   divergence class. This is context for the topology distinction; the
   present residuality proof is self-contained and does not import its theorem.
5. Doron Zeilberger and Wadim Zudilin, *The irrationality measure of pi is
   at most 7.103205334137...*, Moscow J. Comb. Number Theory 9 (2020), 407-419,
   https://arxiv.org/abs/1912.06345v2.
   Primary abstract and corrected-v2 bibliographic record checked. This is
   the historical input used in SUCC's existing logarithmic absolute-loss
   theorem; no claim that it is the latest bound is needed here.

## 9. Next genuinely weaker arithmetic rung

The direct sufficient target is to prove a positive density of nonzero
balanced branches for the authentic endpoint. That is equivalent to R0
(up to negligible endpoints), so calling it a new theorem target adds no
leverage by itself. A genuinely weaker and discriminating next claim is:

> Along the literal original zero-seeded BBP source, the minimum number of
> nonzero balanced branches on the window [B,2B) tends to infinity as
> B tends to infinity.

This would rule out all bounded-defect cold shells, but still allow
K_B=o(B), so it does not imply R0. Its precise finite formulation is:
for every integer K there is B_K such that every B >= B_K has more than K
nonzero branches. A useful proof must exploit the source numerator/cofactor
or analytic identity to exclude the finite union of sparse-form families
from (CSE2). Ordinary irrationality bounds do not do so: a shell with no nonzero balanced branches
only yields a denominator approximately 16^B and error approximately
16^(-2B), whereas the published input used in SUCC has exponent above 7.
This weaker rung is OPEN, not claimed established by the dimension theorem.
