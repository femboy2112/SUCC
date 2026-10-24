# The theorem needed to make observer-history averaging useful

**Date:** 2026-10-24. **Parent:** #272 at
6e8fa8b77886b13f1f533ed8083fd88c849d14b3.
**Authority:** paper proofs, explicitly classical inputs, exact finite checks.
**Open:** the authentic-source asymptotic premises and pi normality.

This dossier makes the proposed infinitely many observers into a positive
history average and identifies the precise source-preservation requirement.
It proves a quantitative bridge to the inherited tripling route, including
its converse at an existential slow schedule. The existential formulation is
an equivalence, not a weaker arithmetic achievement.

## 1. The finite preservation inequality

On the circle of circumference one, write \(U=(T_3)_*\), where
\(T_3x=3x\bmod1\). For a Borel probability \(\mu\) and integer \(J\ge1\), set

$$
A_J\mu=\frac1J\sum_{j=0}^{J-1}U^j\mu,\qquad
\epsilon_J(\mu)=W_1(A_J\mu,\mu),\qquad
\beta(\mu)=W_1(U\mu,\mu).
$$

**Theorem.** Every such probability and depth satisfy

$$
\boxed{\quad
\beta(\mu)\le4\epsilon_J(\mu)
+\frac{W_1(U^J\mu,\mu)}J
\le4\epsilon_J(\mu)+\frac1{2J}.
\quad}
\tag{1}
$$

**Proof.** Tripling is 3-Lipschitz in the geodesic metric. The triangle
inequality through \(UA_J\mu\) and \(A_J\mu\) gives
\(\beta\le3\epsilon_J+W_1(UA_J\mu,A_J\mu)+\epsilon_J\).
The signed zero-mass difference telescopes:

$$
UA_J\mu-A_J\mu=\frac{U^J\mu-\mu}{J}.
$$

The Kantorovich--Rubinstein norm is homogeneous on such differences, so the
middle distance equals \(W_1(U^J\mu,\mu)/J\). The circle diameter is \(1/2\).
This proves (1). QED.

At \(J=2\), homogeneity gives the stronger exact identity

$$
\epsilon_2(\mu)=\frac{\beta(\mu)}2.
\tag{2}
$$

For integer multiplier \(q\ge1\), the identical argument replaces 4 by
\(q+1\). All history coefficients are nonnegative. Signed filters require
different hypotheses; a positive final output does not make their
coefficients positive.

## 2. What the schedule does, and does not, buy

For any sequence \(\mu_p\), (1) proves

$$
J_p\longrightarrow\infty,\quad
\epsilon_{J_p}(\mu_p)\longrightarrow0
\quad\Longrightarrow\quad
\beta(\mu_p)\longrightarrow0.
\tag{3}
$$

Conversely, telescoping one step at a time gives

$$
W_1(U^j\mu,\mu)\le\frac{3^j-1}{2}\beta(\mu),
$$

and hence

$$
\epsilon_J(\mu)\le
\beta(\mu)\left(\frac{3^J-1}{4J}-\frac12\right).
\tag{4}
$$

If \(\beta(\mu_p)\to0\), choose \(J_p\to\infty\) slowly enough that
\(\beta(\mu_p)3^{J_p}\to0\). Formula (4) supplies (3)'s preservation premise.
If some defects vanish exactly, use any increasing depths on those indices.
Therefore the **existence** of a suitable diverging schedule is equivalent
to the inherited same-law tripling condition.

It is still useful to seek an independently specified source-derived schedule
and an explicit arithmetic bound for its preservation error. That proof
would pay the symmetry obligation. Naming a schedule without estimating its
error does not.

### Too-fast histories can erase the limiting law

Let \(\mu_K\) be uniform on the \(3^K\)-point circle grid. Multiplication by
16 permutes this grid, so \((T_{16})_*\mu_K=\mu_K\). Also

$$
\mu_K\to\lambda,\qquad
\beta(\mu_K)=\frac2{3^{K+1}}\to0.
\tag{5}
$$

The transport formula follows either from nearest coarse-grid coupling,
or the distance-to-coarse-grid 1-Lipschitz dual observable: two thirds of the
fine grid points are at distance \(3^{-K}\) from the \(3^{K-1}\)-grid.

But \(U^j\mu_K=\delta_0\) for \(j\ge K\). At \(J_K=K^2\),

$$
A_{J_K}\mu_K\to\delta_0,\qquad
\epsilon_{J_K}(\mu_K)\to W_1(\delta_0,\lambda)=\frac14.
\tag{6}
$$

There is no contradiction with (3) or (4). A chosen long schedule is a
stronger demand than existence of a sufficiently slow one. This grid control
is a post-discovery mathematical counterexample, not a purported BBP source.

## 3. Exact sufficient theorem for the authentic source

Let \(p=8m+1\) run through the inherited good primes from
[the source-collision dossier](PI_SOURCE_COLLISION_ENTROPY.md).
Their starts satisfy consecutive ratios tending to one. The good-prime
condition is ord_p(16)>sqrt(p)/log(p). All limits and hypotheses below range
over all sufficiently large good primes, not an arbitrary subsequence.
Use the original
four-pole recurrence with initial zero, and the actual probability

$$
\mu_p=\frac1{3m}\sum_{n=m+1}^{4m}\delta_{y_n}.
\tag{7}
$$

The inherited estimates already show asymptotic \(T_{16}\)-invariance.
Suppose the following **two currently open arithmetic properties** hold.

1. **Positive collision exponent at all fixed scales.** There are fixed
   \(C<\infty,s>0,\rho_0>0\) such that, for every fixed
   \(0<\rho\le\rho_0\),

   $$
   \limsup_{p\to\infty}Q_{\mu_p}(\rho)\le C\rho^s,\qquad
   Q_\nu(\rho)=(\nu\otimes\nu)\{d(x,z)\le\rho\}.
   \tag{8}
   $$

   This is one direct sufficient version. The inherited real conditional
   carry contraction at all prescribed scales, or its prefix-uniform
   positive-density weakening, implies a bound of this form.

2. **Source preservation under histories.** For some integers \(J_p\to\infty\),

   $$
   W_1(A_{J_p}\mu_p,\mu_p)\to0.
   \tag{9}
   $$

**Conditional theorem.** Under (8) and (9), pi is normal in base 16, and
therefore in bases 4 and 2.

**Proof.** By (1), every weak subsequential limit of \(\mu_p\) is invariant
under tripling. Inherited radix invariance gives its second symmetry.
For \(0<\rho<r\le\rho_0\), use the open set \(\{d<r\}\) and Portmanteau,
then let \(r\) decrease to \(\rho\), to pass (8) to the limiting measure.
This avoids reversing the inequality for a closed set.

A radix-invariant law with this collision bound has entropy at least
\(s\log16\), by the collision-entropy lower bound on its radix partitions.
The classical nonergodic Rudolph--Johnson theorem says that a jointly
invariant law of entropy \(\eta\log16\) dominates \(\eta\lambda\).
Decrease \(s\) if necessary to \(0<s<1\). Subtract \(s\lambda\) and normalize.
The residual stays jointly invariant and inherits the same collision exponent
with a larger finite constant. Repeat: the Haar mass is at least
\(1-(1-s)^k\) for every \(k\). Thus every limit equals Haar.
The full entropy and subtraction proof is inherited in
[PI_BASE_THREE_RIGIDITY.md](PI_BASE_THREE_RIGIDITY.md), section 4.

For completeness, the exact source-to-orbit and window-to-prefix steps are
also needed. The tail identity

$$
\{16^{n-1}\pi\}=\{y_n+T_n\},\qquad 0<T_n<((8n+1)(8n+2))^{-1}
$$

transports (7) to the true pi orbit at times \(m,\ldots,4m-1\), with error
tending to zero. Haar convergence gives centered block sums \(W(m)=o(m)\)
on good-prime starts, since digit-block boundaries have zero Haar mass.
Consecutive good-prime ratios tend to one, and for a bounded block observable
\(f_j\),

$$
|W(m)-W(u)|\le5\|f\|_\infty|m-u|.
$$

This extends the estimate to every large integer start. For
\(S(L)=\sum_{j<L}f_j\), one has
\(S(4m+r)=S(m)+W(m)+O(1)\), \(0\le r<4\).
Repeated division by four and a geometric sum give \(S(L)=o(L)\).
Every fixed hexadecimal block therefore has its correct frequency. QED.

The collision depth and history depth are distinct parameters; they need not
grow at the same rate. A terminal collision estimate alone is insufficient:
the inherited alternating-random/zero-block control has a strong terminal
exponent and asymptotic tripling invariance, but tends to
\((\lambda+\delta_0)/2\). Likewise, preservation alone admits \(\delta_0\).

This proves a conditional route, not either authentic arithmetic premise.
It proves binary-family normality, not decimal or absolute normality.

## 4. An exact transport instrument, with independent certificates

For rational atomic probabilities, classical optimal circle transport gives

$$
W_1(\mu,\nu)=\min_{c\in\mathbb R}
\int_0^1|F_\mu(x)-F_\nu(x)-c|\,dx.
\tag{10}
$$

See Delon--Rabin--Gousseau,
[Transportation Distances on the Circle and Applications](https://arxiv.org/pdf/0906.5499),
equation (10) and the following weighted-median computation. This is a
classical formula, not a new SUCC result.

The exact implementation retains the CDF difference on each interval between
atoms. A weighted median minimizes (10). The resulting circle flow is feasible:
its successive differences equal the signed atom masses. Routing transport
along circle edges gives the flow upper bound; canceling cycles and shortening
paths relates it back to ordinary couplings.

A separate dual witness takes slope \(+1\) where the CDF difference is below
the median and \(-1\) where it is above. On the median set choose the slope
in \([-1,1]\) so the total integral of the slope is zero. The median
inequalities permit that choice. Integrating yields a periodic 1-Lipschitz
potential whose pairing with \(\mu-\nu\) equals the flow cost. The validator
checks both witnesses without recomputing the median.

Independent all-permutation matching calibrates 374 small measure pairs and
2,715 assignments. In particular, \(W_1(\delta_0,\delta_{9/10})=1/10\);
the sorted-line cost \(9/10\) is rejected.

Implementation: [source_history_transport.py](../../observational_succ/source_history_transport.py).
Machine receipt: [PI_HISTORY_TRANSPORT_RECEIPT.json](PI_HISTORY_TRANSPORT_RECEIPT.json).

## 5. All nine prespecified authentic measurements

The primes \(137,281,521\) and histories \(2,4,8\) were fixed in the
[hole contract](PI_PATH_SELECTION_HOLE_CONTRACT.md) before measurement.
Each decimal below is the lower endpoint of an exact enclosure of width
\(10^{-8}\). No fitted rate, monotonicity, or asymptotic claim is attached.

| p | State indices | J | Tripling defect beta | Preservation defect epsilon | Exact boundary term |
|---:|---|---:|---:|---:|---:|
| 137 | 18 through 68 | 2 | 0.08481398 | 0.04240699 | 0.02585494 |
| 137 | 18 through 68 | 4 | 0.08481398 | 0.04442570 | 0.01362860 |
| 137 | 18 through 68 | 8 | 0.08481398 | 0.04464150 | 0.00395234 |
| 281 | 36 through 140 | 2 | 0.01999126 | 0.00999563 | 0.01250971 |
| 281 | 36 through 140 | 4 | 0.01999126 | 0.01146029 | 0.00441535 |
| 281 | 36 through 140 | 8 | 0.01999126 | 0.00903975 | 0.00285079 |
| 521 | 66 through 260 | 2 | 0.02471385 | 0.01235692 | 0.00680435 |
| 521 | 66 through 260 | 4 | 0.02471385 | 0.01482365 | 0.00250219 |
| 521 | 66 through 260 | 8 | 0.02471385 | 0.01199697 | 0.00274572 |

All 351 measured states were independently reconstructed by the literal
four-pole recurrence. Every row satisfies the sharper bound (1), and every
\(J=2\) row has exact \(\epsilon=\beta/2\). Values are not monotone in either
prime or history depth.

If \(B\) is the inherited positive tail bound for a window, the corresponding
true pi-orbit defects differ by at most

$$
|\beta_\pi-\beta_y|\le4B,\qquad
|\epsilon_{\pi,J}-\epsilon_{y,J}|
\le\left(1+\frac{3^J-1}{2J}\right)B.
\tag{11}
$$

These errors are in the receipt. For asymptotically growing \(J\), their
amplification must not be dropped. The conditional theorem uses the exact
rational source law directly and first obtains its tripling invariance by
(1); it transports to the true orbit only afterward.

## 6. Stop rule and next discriminating proof

An additional observer formula is useful if it bounds (9) for the same
authenticated law, or proves (8) by a real carry-frequency saving. A history
ensemble becoming Haar, a unique source projector, or an existential restating
of tripling does not settle either condition.

The next source-specific target can be stated with a fixed positive history
polynomial \(P\), with finitely many coefficients p_j>=0 summing to one
and at least one positive supported history length: bound, for every nonzero
fixed integer \(h\),

$$
\frac1{3m}\sum_{n=m+1}^{4m}
\left(\sum_jp_j e^{2\pi ih3^jy_n}-e^{2\pi ihy_n}\right)\longrightarrow0.
$$

The [operator dossier](PI_HISTORY_OPERATOR_BOUNDARY.md) proves that this is
equivalent, in the limit, to invariance under \(3^d\), where \(d\) is the
gcd of the positive supported history lengths. It also proves the global
L2 telescoping obstruction and supplies signed and singular-law controls.
These statements isolate the missing arithmetic; they do not assume it.
