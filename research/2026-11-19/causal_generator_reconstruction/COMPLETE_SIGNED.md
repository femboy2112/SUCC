# Completion, signed certificates, and the cost of linear reconstruction

**Date:** 2026-11-19. **Status:** elementary paper theorems with exact finite
implementation checks recorded separately. No new source-selected BBP cancellation,
R0, normality, quantum dynamics, or academic-priority claim is made.

This is the analytic part of causal generator reconstruction. It separates three
questions: whether finite generators compose correctly, whether their infinite
completion is controlled, and whether a particular signed chronological average
is small. A finite description can answer the first question without answering
the other two.

## Provenance and domain

The original source is unchanged:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\qquad U_n=16U_{n-1}+r(n),
$$

with the inherited completion
$U_n+T_n=16^n\pi/16$. The mathematical results below apply to the stated
matrix, vector, or radix models; application to this source always retains its
literal seed and chronological weighting.

The following are **inherited**, not rediscovered here:

- [HBC-01--03](../../2026-11-12/boundary_filter_complexity/HANKEL_THEOREMS.md)
  already prove that an irrational expanding-circle phase has infinite Hankel
  rank, with a finite root-count horizon, and that this persists for nonconstant
  finite Fourier filters.
- HBC-04--05 in that same file give the exact phase-delay Gram matrix and its
  conditioning boundary. Irrationality supplies no uniform lower eigenvalue.
- [AL-01--04](../../2026-11-13/joint_time_lag_response/ABSOLUTE_LAGS.md)
  already distinguish aggregate lag control from the maximum of moving lags.
- [IS-3--7](../../2026-11-13/joint_time_lag_response/INVERSE_STABILITY.md)
  already give clock-resolved inverse stability, the fifteenfold ambiguity,
  source anchoring, and the failure of averaged lag accuracy.
- [CFS-3--6](../../2026-11-08/covariance_forge/spectral/THEOREMS.md) already
  give predictor-error/signed-correlation tradeoffs for authentic prime factors
  and their folded complements. Those are different models from the whole-phase
  Hankel approximation theorem CS-05 below.

The additional synthesis here is a gauge-covariant signed residual certificate
and an explicit finite compression-distortion inequality. The latter implies a
sharp obstruction to **horizon-refitted, fixed-dimensional stationary linear
approximation** of a normal radix phase signal. Its proof is finite linear
algebra plus the inherited Weyl characterization, not a new normality theorem.

## CS-01. Finite path composition has an explicit error budget

Let $A_0,\ldots,A_{N-1}$ and $\widehat A_0,\ldots,
\widehat A_{N-1}$ be matrices on the same finite-dimensional normed space.
All norms below are subordinate operator norms. Empty products are identity.
Put $P_N=A_{N-1}\cdots A_0$, and define $\widehat P_N$ similarly.
Then, for every integer $N\ge0$,

$$
P_N-\widehat P_N
=\sum_{j=0}^{N-1} A_{N-1}\cdots A_{j+1}
 (A_j-\widehat A_j)\widehat A_{j-1}\cdots\widehat A_0.                 \tag{CS1}
$$

Consequently, if $\|A_j-\widehat A_j\|\le\delta_j$,

$$
\|P_N-\widehat P_N\|
\le\sum_{j=0}^{N-1}\delta_j
 \prod_{k=j+1}^{N-1}\|A_k\|
 \prod_{k=0}^{j-1}\|\widehat A_k\|.                                \tag{CS2}
$$

**Proof.** Insert one approximate factor at a time, starting from the right,
and telescope the differences. Submultiplicativity and the triangle inequality
give CS2. This includes $N=0$, where both sides are zero. The identity sums
all state-index paths implicitly through matrix products; there is no assumed
independence between paths. QED.

If both factor norms are at most $M$ and each error is at most $\delta$,
CS2 is $N\delta M^{N-1}$ for $N\ge1$. Accurate local Jacobians therefore
need not give uniform long-time accuracy when $M>1$.

For stationary matrices $A,\widehat A$ with both norms at most $M$,
the two weighted path sums converge in operator norm whenever $|z|M<1$:

$$
R_A(z)=\sum_{n\ge0}z^nA^n=(I-zA)^{-1}.
$$

The resolvent identity or summation of CS2 proves

$$
\|R_A(z)-R_{\widehat A}(z)\|
\le\frac{|z|\delta}{(1-|z|M)^2}.                                  \tag{CS3}
$$

This is a genuine finite-to-infinite completion theorem on its stated disk.
Analytic continuation of a rational expression past that disk is a separate
operation; it is not convergence of the original path series there. The
scalar control $A=1$ has a perfectly identified generator but its unweighted
sum diverges. The control $\widehat A=1-\epsilon$ also shows why a resolvent
budget near a pole cannot be made uniform by finite identification alone.

## CS-02. A finite stationary signed mean detects the eigenvalue-one component

Let $A\in\mathbb C^{d\times d}$ be **power bounded** in a declared norm:
$K=\sup_{n\ge0}\|A^n\|<\infty$. Let $\Pi$ be its spectral projection
onto $\ker(I-A)$. If one is not an eigenvalue, $\Pi=0$. Then

$$
\frac1N\sum_{n=0}^{N-1}A^n\longrightarrow\Pi,
\qquad
\frac1B\sum_{n=B}^{2B-1}A^n\longrightarrow\Pi.                    \tag{CS4}
$$

Thus a scalar realization $g_n=cA^nv$ has mean zero exactly when
$c\Pi v=0$. The condition concerns the selected input and output; an
unobserved stationary component need not be absent from the entire operator.

**Proof.** In Jordan form, power boundedness excludes eigenvalues outside the
unit disk and excludes nontrivial Jordan blocks at its boundary. Blocks strictly
inside the disk have powers tending to zero with summable norm. Boundary blocks
are scalar $\lambda^n$; their averages tend to zero if $\lambda\ne1$, by
the geometric-series formula, and equal one if $\lambda=1$. This proves
the first limit. Alternatively, restrict to the invariant complementary space
$Q=\operatorname{ran}(I-\Pi)$, where $I-A_Q$ is invertible. There

$$
\sum_{n=B}^{2B-1} A_Q^n
=(I-A_Q)^{-1}(A_Q^B-A_Q^{2B}),
$$

whose norm divided by $B$ is at most
$2K_Q\|(I-A_Q)^{-1}\|/B$, with
$K_Q=\sup_n\|A_Q^n\|<\infty$. The fixed space contributes exactly
$\Pi$. This proves the shell version and its explicit conditioning cost.
QED.

The power-boundedness premise must be checked on an actual accessible
realization, or on its minimal reachable/observable quotient. Boundedness of
one scalar output does not make an arbitrary larger matrix power bounded:
$A=\operatorname{diag}(2,-1)$, $v=(0,1)^t$, and $c=(0,1)$
give the bounded output $(-1)^n$. A Jordan block at one supplies a separate
failure: $A=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$
has a Cesaro off-diagonal entry $(N-1)/2$.

There is an exact converse for a **minimal scalar realization**. If
$g_n=cA^nv$ is bounded and the $d$-by-$d$ observability and reachability
matrices

$$
O=\begin{bmatrix}c\\cA\\\vdots\\cA^{d-1}\end{bmatrix},\qquad
R=\begin{bmatrix}v&Av&\cdots&A^{d-1}v\end{bmatrix}
$$

are invertible, then $(OA^nR)_{ij}=g_{n+i+j}$ is uniformly bounded
entrywise. Thus $A^n=O^{-1}(OA^nR)R^{-1}$ is power bounded. It follows
that a bounded scalar signal with an authenticated finite minimal stationary
realization always has a Cesaro limit, and that limit is exactly $c\Pi v$.
This statement uses an actual all-time realization; a finite observed Hankel
block cannot certify the hypothesis by itself.

Full observability does not force signed cancellation. The one-dimensional
systems $A=1$ and $A=-1$, both with nonzero input and output, are each
completely observed. Their means are respectively one and zero. Both have
unit-modulus trajectories and completely coherent transitions. The spectral
position relative to one, rather than matrix rank alone, determines the mean.

## CS-03. A moving-frame signed certificate only needs the target residual

Let $q_n\in\mathbb C^d$, $B\le n\le2B$, be a retained finite observer
dictionary. Choose matrices $A_n$, covectors $\ell_n$, and define

$$
r_n=q_{n+1}-A_nq_n,\qquad
f_n=\ell_n-\ell_{n+1}A_n,\qquad
z_n=f_nq_n+e_n.                                                  \tag{CS5}
$$

No smallness is assumed. For every integer $B\ge1$,

$$
\boxed{
\frac1B\sum_{n=B}^{2B-1}z_n
=\frac{\ell_Bq_B-\ell_{2B}q_{2B}}B
 +\frac1B\sum_{n=B}^{2B-1}\ell_{n+1}r_n
 +\frac1B\sum_{n=B}^{2B-1}e_n.}                                  \tag{CS6}
$$

**Proof.** Substitute $A_nq_n=q_{n+1}-r_n$ into CS5. Each term is
$\ell_nq_n-\ell_{n+1}q_{n+1}+\ell_{n+1}r_n+e_n$. The middle boundary
terms telescope exactly. QED.

This identity is covariant under **every** sequence of invertible changes of
coordinates $S_n$. Indeed, set

$$
q'_n=S_nq_n,\quad A'_n=S_{n+1}A_nS_n^{-1},\quad
\ell'_n=\ell_nS_n^{-1},\quad f'_n=f_nS_n^{-1}.
$$

Then $r'_n=S_{n+1}r_n$, and every scalar boundary, residual, and target
term in CS6 is unchanged. Holding $A_n$ or its compensator fixed while
changing an arbitrary moving frame is not this coordinate change. Norm bounds
must transport the norm with the frame, or explicitly pay its condition number.

For constant $A_n=A$, $\ell_n=\ell$, the certificate asks for the
finite-dimensional Poisson equation $f=\ell(I-A)$. Its mean bound is

$$
\left|\frac1B\sum z_n\right|
\le\frac{|\ell q_B|+|\ell q_{2B}|}{B}
 +\left|\frac1B\sum\ell r_n\right|
 +\frac1B\sum|e_n|.                                               \tag{CS7}
$$

Only the **signed projected residual** is charged in the second term. Accurate
reconstruction of all dictionary coordinates is stronger than needed. The
matrix, dimension, and covectors may even depend on the shell, provided the
displayed three budgets tend to zero on every required shell. CS6 remains a
separate exact identity for each shell; no uniform bound is imported for free.

For $z_n=e(h16^n\pi/16)$, such a construction with independently proved
vanishing budgets for every integer $B\to\infty$ would give the corresponding
signed Weyl limit. For bounded targets, the prefix limit follows by recursively
halving a prefix into these shells, with bounded odd-length remainders.
Control only at selected dyadic endpoints requires additional control of
partial shells. No such
source-specific budgets are established here. Taking $q_n$ to be the
unbounded partial sum of the very target merely relocates the unknown mean
into its boundary term and is a circular reformulation.

There is also a concrete obstruction to a source-blind certificate. On the
whole circle, the function $f(t)=e(ht)$, $h\ne0$, cannot have an exact
coboundary representation $f=g-g\circ T_b$, $T_b(t)=bt\pmod1$, by
any single-valued $g$: at the fixed point zero its left side is one and
its right side is zero. The original source and seed must therefore enter a
certificate or its nonzero residual. The same-forcing seed $-\pi/16$
produces the completed constant phase one and exposes this stationary
component directly. It is rejected by the authentic zero-seed condition.

## CS-04. Finite nonlinear description and infinite linear rank coexist

For reference, the inherited HBC root argument can be stated in one paragraph.
Let $b\ge2$, $h\in\mathbb Z\setminus\{0\}$, and irrational $x$.
The phases $z_n=e(hb^nx)$ are all distinct: a collision makes
$h(b^n-b^m)x$ an integer. A nonzero recurrence
$\sum_{j=0}^da_jz_{n+j}=0$ would make the nonzero polynomial
$P(t)=\sum_{j=0}^da_jt^{b^j}$ vanish at infinitely many distinct phases.
That is impossible. In fact, if the first and last nonzero coefficients are
at $j_0,j_1$, such a relation can hold at at most
$b^{j_1}-b^{j_0}$ distinct source phases, after dividing by
$t^{b^{j_0}}$. Hence $b^d$ distinct starting positions always defeat a
nonzero order-$d$ relation. This is HBC-01--02, with all its hypotheses.

Nevertheless the same signal has the **one-coordinate nonlinear generator**

$$
z_{n+1}=z_n^b.                                                    \tag{CS8}
$$

Its exact initial value and precision still cost information. The linear
Koopman pullback sends each character $e_k$ to $e_{bk}$. The infinitely
many distinct characters generated from $e_h$ cannot fit in a finite
linear invariant observation space, even though the underlying circle state
has one coordinate. See the primary discussion of the distinction between
state variables and finite linear invariant observable spaces in
[Brunton et al. (2016)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0150171).
Our radix conclusion uses the explicit proof above, not an unrestricted
inference from that paper's examples.

For rational $x$, the phase orbit is eventually periodic and a finite
linear shift realization exists. At $x=0$ it has rank one and mean one.
For the authentic completed BBP phase, imported irrationality of $\pi$
puts every nonzero frequency in the infinite-linear-rank class. This does not
imply normality: the inherited sparse irrational counterexample in HBC-06
has infinite phase rank and shell means tending to one.

The reconstruction question therefore needs its **model language** stated.
Finite nonlinear programs, finite time-dependent matrices, growing linear
dictionaries, and finite stationary linear realizations have different costs
and different closure theorems. No general impossibility of finite causal
description follows from HBC-01.

## CS-05. Finite Hankel compression has a quantitative distortion floor

This theorem is a finite statement about arbitrary complex sequences. It
needs neither normality nor a radix law.

Let $z_0,\ldots,z_{L-1}$ and $y_0,\ldots,y_{L-1}$ be complex vectors.
Choose integers $0\le d<m\le L$, put $N=L-m+1$, and form their
$N$-by-$m$ delay matrices

$$
H(z)_{n,j}=z_{n+j},\quad H(y)_{n,j}=y_{n+j},\qquad
0\le n<N,\quad0\le j<m.
$$

Assume $\operatorname{rank}H(y)\le d$. Put
$G=N^{-1}H(z)^*H(z)$, with eigenvalues ordered
$0\le\lambda_1(G)\le\cdots\le\lambda_m(G)$, including zeros. Then

$$
\boxed{
\frac1L\sum_{k=0}^{L-1}|z_k-y_k|^2
\ge\frac{N}{mL}\sum_{j=1}^{m-d}\lambda_j(G)
\ge\frac{N}{L}\left(1-\frac dm\right)\lambda_1(G).}                \tag{CS9}
$$

**Proof.** The nullspace of $H(y)$ has dimension at least $m-d$. Choose
orthonormal vectors $v_1,\ldots,v_{m-d}$ in that nullspace and extend them
to an orthonormal basis of $\mathbb C^m$. By the basis invariance of the
Frobenius norm,

$$
\begin{split}
\|H(z)-H(y)\|_F^2
&\ge\sum_{a=1}^{m-d}\|(H(z)-H(y))v_a\|_2^2\\
&=\sum_{a=1}^{m-d}\|H(z)v_a\|_2^2\\
&=N\sum_{a=1}^{m-d}v_a^*Gv_a
\ge N\sum_{j=1}^{m-d}\lambda_j(G)
\ge N(m-d)\lambda_1(G).
\end{split}
$$

For completeness, the middle inequality needs no approximation theorem.
Write the orthonormal $v_a$'s in an orthonormal eigenbasis $u_j$ of
$G$, and set $w_j=\sum_a|u_j^*v_a|^2$. Orthogonal projection gives
$0\le w_j\le1$ and $\sum_jw_j=m-d=k$. Then
$\sum_av_a^*Gv_a=\sum_j\lambda_jw_j\ge\sum_{j=1}^{k}\lambda_j$:
the weight missing from the first $k$ positions equals the weight placed
after them, where every eigenvalue is at least $\lambda_k$.

On the other hand each scalar error $|z_k-y_k|^2$ occurs in the delay
matrix at most $m$ times, so its squared Frobenius norm is at most
$m\sum_k|z_k-y_k|^2$. Divide by $mL$. QED.

Both versions remain valid for $N<m$, when the smallest-eigenvalue
version may simply be zero. The spectral-sum version can remain positive
even when the smallest eigenvalue vanishes.

An exact rational or interval lower bound $\gamma\le\lambda_{\min}(G)$
can replace the eigenvalue in CS9. For example, the elementary Gram bound

$$
\gamma=\max\left(0,\min_i\{G_{ii}-\sum_{j\ne i}|G_{ij}|\}\right)
$$

is valid. Positivity of a determinant alone does not provide a useful
$\gamma$. This preserves the inverse-conditioning lesson of HBC-04--05.

### Normality consequence, including horizon-refitted models

Suppose $x$ is normal in integer base $b\ge2$, fix $h\ne0$, and put
$z_n=e(hb^nx)$. For every fixed $m$,

$$
G_{ij}=\frac1N\sum_{n=0}^{N-1}e\big(h(b^j-b^i)b^nx\big)
\longrightarrow\delta_{ij}.                                     \tag{CS10}
$$

For $i\ne j$ the frequency is a fixed nonzero integer, so the limit
follows from the classical Weyl characterization of normality. For $i=j$
it is exactly one. There are only finitely many entries, hence
$\lambda_{\min}(G)\to1$. This also holds for dyadic shells, by writing
a shell average as a difference of two prefix averages.

Fix any finite state budget $d$. For **each** $L$, an observer may choose
a new model $A_L\in\mathbb C^{d\times d}$, row $c_L$, and state
$v_L$, with no coefficient bound and with full knowledge of that observed
window. Let $y^{(L)}_k=c_LA_L^kv_L$ for $0\le k<L$. Then

$$
\boxed{\liminf_{L\to\infty}\frac1L
\sum_{k=0}^{L-1}|z_k-y^{(L)}_k|^2\ge1.}                            \tag{CS11}
$$

**Proof.** Every such delay matrix factors as
$H(y)_{n,j}=(c_LA_L^n)(A_L^jv_L)$, so its rank is at most $d$, even
when the model changes with $L$. Fix $m>d$ before sending $L$ to
infinity. CS9 and CS10 give a lower limit at least $1-d/m$. This holds
for every fixed integer $m>d$; now let $m$ grow. The lower limit is
at least one. The zero model has error exactly one, so the infimum over all
models of budget at most $d$ actually tends to one. QED.

Thus fixed-dimensional stationary linear reconstruction cannot asymptotically
beat zero prediction in mean-square error on a normal radix phase signal,
even if it is refitted at every horizon. This does **not** say that no useful
short-horizon fits exist, that no nonlinear generator exists, or that growing
dimension fails. No quantitative growth rate for the required dimension
follows from normality alone. Taking $m=m(L)$ in CS10 without a uniform
estimate would be an invalid exchange of quantifiers.

Nor does the obstruction prohibit computing the signed mean. The zero
approximation has unit squared phase error at every time but correctly predicts the
asymptotic mean of a normal signal. This is precisely why CS6 aims at the
target's signed residual instead of requiring a full finite linear phase
reconstruction.

For $x=\pi/16$, CS11 is **conditional on unproved normality**. The finite
CS9 is unconditional and may be evaluated on any source-certified window.
It produces an approximation lower bound, never a lower bound on the
original signed Weyl mean.

### A fixed-order recurrence residual as a simpler corollary

For every fixed coefficient vector $a=(a_0,\ldots,a_d)$, CS10 gives

$$
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}
 \left|\sum_{j=0}^da_j z_{n+j}\right|^2=\sum_{j=0}^d|a_j|^2.         \tag{CS12}
$$

Even if the earlier coefficients are chosen separately at every horizon,
the least residual with $a_d=1$ tends to one: it is bounded below by
$\lambda_{\min}(G)\|a\|_2^2\ge\lambda_{\min}(G)$, and choosing
$a_d=1$, all other coefficients zero, gives exactly one. This statement
retains the fixed order. It does not prohibit moving coherent lag maxima,
whose different quantifiers are handled by AL-01--04.

## CS-06. Controls, paid conclusions, and the next source obligation

| Claim under test | Positive or hostile control | Earned conclusion |
|---|---|---|
| Accurate local matrices imply accurate arbitrary products | Scalar factors $1+\epsilon$ versus 1 | CS2 charges accumulated growth; a uniform claim without it fails |
| Complete phase rank implies a vanishing mean | Sparse irrational HBC-06; or the rank-one fixed orbit | Refuted |
| A finite linear phase generator can describe the genuine completed orbit | HBC-01 and imported pi irrationality | Impossible in the stationary finite-linear category |
| A finite nonlinear generator is also impossible | $z\mapsto z^b$ | Refuted; model language changes the answer |
| Finite LTI models approximate a normal phase arbitrarily well at fixed dimension | CS9--11, including refitted models | Refuted under the explicit normality premise |
| A target certificate must reconstruct every phase | CS6 with signed projected residual | False as a general requirement; full reconstruction is stronger |
| A moving gauge may omit its transported compensator | Rational moving-frame mutation in the exact tests | Refuted |
| A universal source-blind coboundary cancels every radix phase | Fixed point zero; same-forcing counterseed | Refuted |
| Source-specific signed residual budgets hold for the actual zero seed | No proof supplied | OPEN; this is the remaining arithmetic obligation |

The exact calibration implementation uses rational matrices, sign sequences,
and finite character orthogonality. The root-of-unity **grid** averages are
explicit reference measures, not a claim that a selected radix orbit traverses
that grid. Rational periodic orbit controls authenticate only their own seeds.
No pi phase sample is used as evidence for the all-horizon conditional theorem.

The grid calculation is exact: for integers $q\ge1$ and $k$,

$$
\frac1q\sum_{a=0}^{q-1}e(ka/q)=\mathbf1_{q\mid k}.                 \tag{CS13}
$$

If $q\mid k$, every summand is one. Otherwise the finite geometric sum
has numerator $1-e(k)=0$ and nonzero denominator $1-e(k/q)$. Thus the
delay Gram averaged over **all initial grid points** $a/q$ has entry
$\mathbf1_{q\mid h(b^j-b^i)}$. For $b=16,h=1,q=257,m=3$, the
three frequencies $1,16,256$ are distinct modulo $257$, so this grid
Gram is exactly identity. The selected zero grid point instead gives the
constant phase and the all-ones Gram. This pair is an exact calibration of
the ensemble-to-selected-orbit failure.

For a positive periodic control take $x=1/(b^p-1)$, where
$b^px=x+1$. Its phase sequence obeys $z_{n+p}=z_n$, so a $p$-state
cyclic shift realizes it linearly. The rational tests verify this relation
using turns modulo one, without floating-point trigonometry. Auxiliary
binary de Bruijn cycles supply sign records whose fixed-width delay Gram
is exactly identity: each binary word of the chosen order occurs once per
cycle, so each pair of distinct bit positions has the four equiprobable
values and zero sign correlation. These finite records calibrate CS9; their
periodic continuation does not satisfy its infinite normality premise.

The next decisive construction is a dictionary and covector family derived
from the actual source and its retained history, together with a signed bound
for the middle term of CS6 and a sublinear boundary budget. It must distinguish
the unchanged-forcing seed $-\pi/16$. Failing that test means the apparent
cancellation has been obtained by discarding the stationary source component.

**Primary literature context.** Weyl's original character criterion is
H. Weyl, *Ueber die Gleichverteilung von Zahlen mod. Eins*, Math. Ann. 77
(1916), 313--352, [DOI](https://doi.org/10.1007/BF01475864),
[primary scan](https://zenodo.org/records/2425535).
The finite Koopman distinction is discussed in the cited
[Brunton et al. paper](https://doi.org/10.1371/journal.pone.0150171).
CS1--7 are elementary composition, resolvent, spectral, and telescoping
identities. CS9 is proved above without importing a low-rank approximation
black box. No worldwide novelty search or formal-kernel verification is claimed.
