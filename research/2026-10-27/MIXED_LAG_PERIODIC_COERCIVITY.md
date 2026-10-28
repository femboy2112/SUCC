# Uniform signed loss for moving mixed lags and periodic observers

**PAPER-PROVED with CLASSICAL arithmetic input; exact finite instruments.**
This extends the scalar logarithmic Fourier loss to a supremum over periodic
unit templates, arbitrary mixed-difference order, and moving lag spans.
The absolute-loss order is still logarithmic. The onset is not numerically
computed. Base-16 normality of π remains **OPEN**.

The original four-pole forcing, its literal signs and indices, unwrapped
integer lifts, and $U_0=0$ are unchanged. No source channels are averaged.

## 1. The joint theorem

Let $E$ be forward shift in the authentic time index, $e(x)=\exp(2\pi ix)$,
and let $\boldsymbol\ell=(\ell_1,\ldots,\ell_k)$ be any nonempty tuple of
positive integers. Put

$$
P(X)=\prod_{i=1}^k(X^{\ell_i}-1),\qquad
d=\sum_i\ell_i,\qquad A=P(16)=\prod_i(16^{\ell_i}-1).
$$

Thus $1\le A<16^d$; all coefficients of the signed filter are retained.
For a positive period $p$ and nonzero integer $h$, define

$$
\mathcal L_N(p,h,P)=
\sum_{a=0}^{p-1}
\left|\sum_{\substack{1\le n\le N\\n\equiv a\pmod p}}
 e\bigl(hP(E)U_n\bigr)\right|.
\tag{ML-1}
$$

There is one integer $J\ge4$, independent of $p,h,k,\boldsymbol\ell,N$,
with the following property. Set

$$
b=d+\lceil\log_{16}|h|\rceil,
\quad j_{\ast} =\max\left\lbrace J,\left\lceil\log_8(4096p)\right\rceil,
\left\lceil\log_8(60b)\right\rceil\right\rbrace ,
\quad M=8^{j_{\ast}},
$$

$$K=\max\lbrace 0,\lfloor\log_8N\rfloor-j_{\ast}\rbrace .$$

Then, for every such input,

$$
\boxed{
\mathcal L_N(p,h,P)\le
\min\left\lbrace N,\ N-\frac K{14}
 +\boldsymbol 1_{K>0}\frac{11|h|}{112M}\right\rbrace .
}
\tag{ML-2}
$$

In particular, fix $h\ne0$ and $0<\delta<1$. Uniformly over **every**
choice of period and mixed lag tuple with $p+d\le N^\delta$,

$$
\boxed{\mathcal L_N(p,h,P)
\le N-\frac{1-\delta}{14}\log_8N+O_h(1).}
\tag{ML-3}
$$

Here $O_h(1)$ may include the one uncomputed universal arithmetic onset;
it is uniform in the lag tuple, its length, its span and the period.
The statement permits a new tuple at each $N$, order $k$ growing up to $d$,
and completed frequency $hA$ as large as $|h|16^{N^\delta}$.
No fixed-lag passage is smuggled into this moving-parameter conclusion.

The residue sum in (ML-1) equals

$$
\sup_{|w_0|=\cdots=|w_{p-1}|=1}
\left|\sum_{n=1}^Nw_{n\bmod p}e(hP(E)U_n)\right|.
\tag{ML-4}
$$

The upper bound is the triangle inequality. Equality follows by choosing
each $w_a$ to align its residue sum, with any unit value for zero sums.
Thus the theorem survives even a template chosen after the observations.
This is a uniform supremum theorem, not a stochastic inverse-branch model.

**Blockwise adaptive corollary.** The template may also be chosen separately
on each eligible geometric block. In fact the stronger observable

$$
N-\sum_{j=j_{\ast}}^{j_{\ast}+K-1}7\cdot8^j
+\sum_{j=j_{\ast}}^{j_{\ast}+K-1}\sum_{a=0}^{p-1}
\left|\sum_{\substack{8^j<n\le8^{j+1}\\n\equiv a\pmod p}}
e(hP(E)U_n)\right|
$$

obeys the same upper bound as (ML-2). This follows by taking the attained
template supremum separately on each finite block. No probabilistic
adaptation assumption or union-bound penalty is needed. The result does not
rely on cancellation between different geometric blocks.

## 2. A positive tail pays every mixed difference at once

The inherited exact Green identity is

$$
U_n+T_n=16^{n-1}\pi,\qquad
T_n=\int_0^1t^{8n}\frac{4-2t^3-t^4-t^5}{16-t^8}\,dt,
\qquad 0<T_n<\frac1{64n^2}\quad(n\ge1).
\tag{ML-5}
$$

The numerator is $(1-t)(4+4t+4t^2+2t^3+t^4)>0$ on $(0,1)$.
Multiplying the integrand by each forward-difference factor gives

$$
R_n:=(-1)^kP(E)T_n
=\int_0^1t^{8n}\frac{4-2t^3-t^4-t^5}{16-t^8}
\prod_i(1-t^{8\ell_i})\,dt.
$$

Every extra factor lies strictly between zero and one on $(0,1)$.
Consequently $0<R_n<T_n$, with no factor depending on $k$ or $d$.
This positive-kernel mixed-lag transport is inherited from
[BBP_RESONANT_LAG_DESCENT.md](../2026-10-25/BBP_RESONANT_LAG_DESCENT.md);
it is not counted as a newly discovered identity.

The exact signed relation is

$$P(E)U_n=A16^{n-1}\pi-(-1)^kR_n.$$

Using $|e(x)-e(y)|\le2\pi|x-y|$, $2\pi<44/7$, and
$\sum_{n>M}n^{-2}\le1/M$, we get the **complete infinite** error bound

$$
\sum_{n>M}
\left|e(hP(E)U_n)-e(hA16^{n-1}\pi)\right|
<\frac{11|h|}{112M}.
\tag{ML-6}
$$

This bound is uniform in every mixed lag tuple. Multiplication by any unit
template does not change it. No exchange of an unbounded-order limit with
an integral is needed: each finite tuple has the same pointwise domination
and the same explicit infinite tail bound.

**The comparison target matters.** Replacing the completed orbit by $AU_n$
would leave the error $AT_n-P(E)T_n$, usually of size $A/n^2$.
The present argument never makes that replacement. It retains the entire
original zero-selected Green boundary, then applies the arithmetic theorem
directly at the large integer frequency $hA$.

## 3. The completed orbit admits a much wider frequency schedule

We use the new finite periodic-template lemma proved independently in
[PERIODIC_TEMPLATE_COERCIVITY.md](PERIODIC_TEMPLATE_COERCIVITY.md).
For a block $(m,8m]$, $m\ge4096p$, suppose a period $p$ unit template gives
loss at most $1/14$ on $e(H16^{n-1}\pi)$, $H\in\mathbb Z\setminus\lbrace 0\rbrace $.
The forcing here is exactly zero. The lemma produces an integer numerator
and denominator

$$q=|H|(16^p-1)16^m$$

such that

$$\left|\pi-\frac{a}{q}\right|<4\,16^{-8m}.$$

The proof retains the arbitrary periodic template phases in the centered
lifts. Their differences cancel only when comparing the same residue class;
the resulting integer branches are $p$-periodic. Their rational periodic
solution has denominator dividing $16^p-1$. The last $p$ transitions remove
the template from the endpoint bound. The separate dossier supplies every
finite step; scalar coherence alone would not justify this conclusion.

The corrected [Zeilberger–Zudilin paper](https://arxiv.org/abs/1912.06345v2)
gives $\mu(\pi)<15/2$. Hence some $C\in(0,1]$ satisfies
$|\pi-a/q|\ge Cq^{-15/2}$ for all integers $a$ and positive integers $q$.
Irrationality absorbs finitely many exceptional reduced denominators;
unreduced denominators only weaken the lower bound. No value of $C$ is
extracted here. The preceding approximation is impossible if

$$C^2 16^{m-15p}>16|H|^{15}.\tag{ML-7}$$

Take $H=hA$. Since $|H|<16^b$, $m\ge4096p$ and $m\ge60b$ imply

$$m-15p-15b\ge\left(\frac34-\frac{15}{4096}\right)m>\frac m2.$$

One universal $m_{\ast}$ with $C^2 16^{m_{\ast}/2}>16$ therefore makes (ML-7)
hold at every $m\ge m_{\ast}$ obeying those two schedules.
Choose $J\ge4$ so $8^J\ge m_{\ast}$. We have proved the period-template
block loss $>1/14$ on the completed orbit at frequency $hA$ for every
eligible scale. The original-source restriction $|h|\le m^2/64$ from
the previous forcing-range argument is **not** imposed on $H$ here:
the completed orbit has zero forcing, and its frequency cost is paid in
(ML-7). Calling this a forcing-zero orbit does not change the source;
(ML-5) and the explicit error (ML-6) are the comparison map.

## 4. Assembly and the moving-parameter conclusion

For $K>0$, the $K$ eligible disjoint blocks $(8^j,8^{j+1}]$ begin at $M$
and end at $8^{\lfloor\log_8N\rfloor}$. Apply the completed-orbit bound
on each, sum the losses, and pay (ML-6) **once** over their union.
Bound all remaining observations trivially. This proves the weighted sum
version of (ML-2) for every template; (ML-4) proves the residue version.
For $K=0$ the trivial bound is used and no transport debt is charged.

If $p+d\le N^\delta$, the explicit schedules give
$j_{\ast}\le\delta\log_8N+O_h(1)$, including the fixed $J$.
Therefore $K\ge(1-\delta)\log_8N-O_h(1)$, and the positive transport
term is bounded by a constant depending on $h$. This proves (ML-3).
For fixed $h$ and $d\to\infty$, its transport debt actually tends to zero.

## 5. What is stronger, and what still fails

The new conclusion is signed loss for **all moving mixed-lag characters
and all periodic observers in the declared joint schedule**. The older
mixed-lag report identified the completed frequency but did not establish
such a uniform signed estimate. The scalar sum alone cannot control the
residue supremum: $z_n=e(n/p)$ sums to zero over complete periods, while
the template $e(-n/p)$ restores the maximal sum. The new periodic rigidity
argument is indispensable for that strengthening.

These are new results within the inspected repository lineage; academic
priority outside that lineage is not asserted. The positive integral,
irrationality measure, and scalar $1/14$ coercivity are explicitly inherited.
No repeated identity is counted as independent arithmetic evidence.
The estimates for different periods share the same source and Diophantine
argument. Their losses cannot be added as if they were independent events.
At period $p=N$, a template can undo every observed phase individually and
restore the exact sum $N$; the prescribed schedule then has $K=0$, as it must.

The fixed same-forcing seed $V_0=-\pi/16$ yields $V_n=-T_n$.
For any fixed mixed lag tuple, $P(E)V_n=-(-1)^kR_n\to0$ with a summable
phase error. Its constant-template sum has bounded absolute loss, so it
violates the logarithmic conclusion. It fails the zero-selector identity
(ML-5), exactly where the Diophantine input is applied. A zero-forcing
zero-seed orbit fails for the same reason. A rational periodic source
can be unwound by its matching template and likewise lacks the π anchor.

Conversely, the inherited sparse-digit finite-irrationality controls can
still have logarithmic absolute loss and nonnormal limiting bias.
This theorem does not improve that order or rule out those controls merely
by its generic Diophantine mechanism. The bound divided by $N$ still tends
to one. No large-sieve, van der Corput or entropy step turns it into $o(N)$.

## 6. Instruments and the next arithmetic obligation

[`mixed_lag_coercivity.py`](../../observational_succ/mixed_lag_coercivity.py)
replays unwrapped mixed histories from all four poles and $U_0=0$, checks
exact schedule margins, and computes conditional budgets. A supplied $J$
is never called a numerically certified onset. The finite tail holdouts
include an outward remainder for the entire infinite tail.

The sharp remaining obligation is stronger than another transport identity:
prove growing loss within authentic blocks, or quantitative signed
combination of their residue sums, uniformly in a useful moving-lag regime.
The new theorem makes mixed lag differencing available with a paid error
and a nonzero signed saving. That saving is still too small for a
van der Corput iteration to force normality.
