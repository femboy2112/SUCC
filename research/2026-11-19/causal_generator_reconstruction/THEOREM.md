# The causal generator reconstruction theorem: precise forms and limits

**Status:** proved paper statements on the declared domains; classical ingredients
and source-specific additions are separated in [PROVENANCE.md](PROVENANCE.md).
This document is a synthesis, not a proof that every carrier has a finite
identifying family or that the selected BBP orbit is normal.

## 1. Specify the global object before asking for its minimum

Let $\mathcal M$ be a declared class of carrier models, $\mathcal P$ a
family of lawful probes, and $O:\mathcal M\to\mathcal Y$ the target. The
target space may already be a quotient by a declared gauge. For a finite probe
list $P=(p_1,\ldots,p_k)$, write

$$
E_P(M)=(p_1(M),\ldots,p_k(M)).
$$

**Separation** means

$$
E_P(M)=E_P(M')\quad\Longrightarrow\quad O(M)=O(M')
\quad(M,M'\in\mathcal M).                                      \tag{T1}
$$

Equivalently, the target is constant on every compatible-model fiber of the
observation map. Its reconstruction map exists on the image of $E_P$.
This set-theoretic equivalence is immediate: define the value at a transcript
using any compatible model; (T1) makes the choice immaterial. It does not
provide an algorithm, precision bound, physical access or convergence proof.

For an adaptive observer the entire transcript, including chosen clocks and
stopping rule, replaces $E_P$. The five-state lower bound in SA-03 uses
that transcript and therefore does not assume fixed probe choices.

A minimum number of probes is meaningful only after declaring their output
type, accuracy, allowed source interventions, preparation/replay rules and
time cost. One exact real can contain infinitely many bits; one path may carry
many readouts. Query count, state dimension, number of independent parameters,
and physical resource cost are different optimization problems.

## 2. A complete finite-bank-to-path-sum theorem

The following concrete theorem pays all three obligations on a nonempty class.
It combines the classical realization proof in CGR-R03 with an explicit analytic
completion. It is not presented as a new theorem of weighted automata.

### CGR-01 — accessible finite realization and absolutely convergent completion

Let $\Sigma$ be a finite action alphabet and $f:\Sigma^*\to\mathbb C$
an authenticated response from a specified preparation. Assume:

1. A source theorem establishes a global bound
   $\operatorname{rank}(f(uv))_{u,v\in\Sigma^*}\le d$, with $d\ge1$.
2. Lawful observations supply $H=(f(p_iq_j))_{i,j=1}^d$ with
   $\det H\ne0$, every $H_a=(f(p_i a q_j))$,
   $h_Q=(f(q_j))$, and $h_P=(f(p_i))^T$.
3. Fix scalar tags $z_a$ and a subordinate operator norm. For the matrices
   reconstructed below, an actual bound gives
   $q=\sum_{a\in\Sigma}|z_a|\|M_a\|<1$.

Define

$$
\alpha=h_QH^{-1},\qquad M_a=H_aH^{-1},\qquad \beta=h_P,
\qquad A=\sum_a z_aM_a.
$$

Then:

- For **every** word $w=a_1\cdots a_n$,
  $f(w)=\alpha M_{a_1}\cdots M_{a_n}\beta$.
- The dimension $d$ is minimal among all stationary linear weighted
  realizations of the entire response. The minimal realization is unique up to
  simultaneous similarity and transported endpoint vectors.
- The absolute word sum converges and equals
  $$
  \boxed{\sum_{w\in\Sigma^*}z_w f(w)
       =\alpha(I-A)^{-1}\beta,\qquad z_w=\prod_{a\text{ in }w}z_a.} \tag{T2}
  $$
- Truncating at word length $L$ has error at most
  $$
  \boxed{\|\alpha\|_*\|\beta\|\frac{q^{L+1}}{1-q}.}             \tag{T3}
  $$
  Here the row norm is dual to the state-vector norm. Empty words have tag one.

**Proof.** Let $r_u(v)=f(uv)$. The global rank bound and invertible block
make $r_{p_1},\ldots,r_{p_d}$ a basis of the full residual-function space.
Append is well-defined on this space: if a linear relation vanishes on every
suffix, evaluate it on $av$ to preserve the relation after appending $a$.
Restriction to $Q$ is injective, and the coordinates of $r_u$ are
$(f(uq_j))_jH^{-1}$. Appending $a$ therefore multiplies this row by
$M_a$, while empty-suffix evaluation is $\beta$. Induction proves
the all-word formula. Any $m$-state realization factors the full Hankel
table through $\mathbb C^m$, so $m\ge d$. Two minimal reachable and
observable realizations identify the same residual functions, giving an
invertible intertwiner; CGR-R04 spells out the similarity proof.

For each length $n$, distributivity with the order retained gives
$\sum_{|w|=n}z_w f(w)=\alpha A^n\beta$. Submultiplicativity gives
$$
\sum_{|w|=n}|z_w f(w)|\le\|\alpha\|_*\|\beta\|q^n.
$$
The geometric series establishes absolute convergence, the Neumann inverse,
and the explicit remainder (T3). QED.

**What each premise pays.** The nonsingular bank resolves the relevant residual
coordinates; the global rank law closes them under every generator; $q<1$
pays completion with a usable modulus. A merely observed finite rank does not
pay the first premise. A formal generating function needs no analytic $q$,
but then no analytic convergence is asserted. The sufficient norm condition is
not a necessary criterion for scalar cancellation or convergence.

The reconstructed object is the minimal **target response realization**.
Similarity can change graph support. A hidden mode can alter the full carrier
without changing any accessible response. Therefore “global structure exactly”
means the declared structure up to its proved equivalence, not every possible
hidden extension of the source.

## 3. Completion for other targets, and the order of the quantifiers

### CGR-02 — uniform target-fiber completion

Fix a transcript $y$ and its nonempty compatible class
$\mathcal M_y$. Let $O_L(M)$ and $O(M)$ lie in a metric space.
Suppose a computed finite report $a_L(y)$ and certified budgets satisfy

$$
\sup_{M\in\mathcal M_y}d(a_L(y),O_L(M))\le\delta_L,
\qquad
\sup_{M\in\mathcal M_y}d(O_L(M),O(M))\le r_L.                    \tag{T4}
$$

Then
$$
\sup_{M\in\mathcal M_y}d(a_L(y),O(M))\le\delta_L+r_L.            \tag{T5}
$$
If the right side tends to zero, every compatible model has the same target,
and $a_L(y)$ converges to it. For every $M,M'$ the target-fiber diameter
is at most $2(\delta_L+r_L)$.

**Proof.** Apply the triangle inequality for (T5), then use the same computed
center for any pair of compatible models. Sending $L$ to infinity makes
their distance zero and proves convergence. QED.

This is a transparent transport lemma, not the missing estimate itself. To use
it, one must actually establish $r_L$ and $\delta_L$. Setting
$r_L$ equal to an unknown desired error merely restates the problem.

There is a logical distinction worth preserving. If
$O_L(M)=O_L(M')$ for **every** truncation depth $L$, and each sequence
converges to its stated target, those targets agree without a uniform modulus.
A common fixed finite prefix would not suffice. Uniformity supplies a finite
error certificate over a class of compatible models. Identification of an
infinite sequence, existence of its limit, and effective certified evaluation
of that limit are three distinct conclusions.

For the BBP source, truncation depth $M$ approximates its endpoint and each
fixed finite chronological shell. The shell length $B\to\infty$ is a
different limit. An error estimate as $M\to\infty$ at fixed $B$
does not establish cancellation as $B\to\infty$. Choosing $M=2B$
in the inherited terminal transport does pay the approximation error uniformly;
the actual terminal signed sum still needs an arithmetic bound.

## 4. How the three recent threads meet

### Fibonacci supplies a completed positive model

With the authenticated order-two law, the readings $1,1,2,3$ recover
$$
\alpha=(1,0),\quad M=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\quad\beta=(1,1)^T.
$$
The identity $M^2=M+I$ generates every later response and
$\alpha(I-zM)^{-1}\beta=(1-z-z^2)^{-1}$. As a power series its actual
complex convergence radius is $1/\varphi$, $\varphi=(1+\sqrt5)/2$.
A finite fit alone would also allow a delayed nilpotent perturbation; the
source-derived order law is the decisive difference.

### Jacobians supply closure only when their integration constants are paid

On a connected open domain, suppose a feature map and every generator are
$C^1$, and throughout that domain
$$
D\psi(T_a x)DT_a(x)=A_aD\psi(x).
$$
Then $\psi(T_a x)-A_a\psi(x)$ has zero derivative and is constant.
An anchored value at one point fixes that constant. With a zero constant the
features close linearly; with a known nonzero constant they close affinely and
one extra constant coordinate homogenizes the law. This is CGR-R05.

Thus a global differential coherence identity and anchors can prove an actual
finite generator law. Sampled derivatives, a single orbit, or a convenient
moving chart do not establish the identity over all unobserved states.

### Knowledge volume measures the remaining fiber in declared units

For the five-state source family the sampling map is linear and invertible.
Bounded raw errors produce an exact parallelotope, not an unspecified belief
score. Its volume is the raw error-box volume divided by $|\det R|$,
while each parameter's worst error uses its corresponding inverse row.

The late-consecutive theorem makes the distinction decisive: volume tends to
zero exponentially up to a polynomial factor, while the largest uncertainty
grows polynomially. Gauge changes or readout normalization must carry the
error units along. Extra retained observations intersect the fiber; changing
coordinates alone does not supply another constraint.

## 5. The linear-rank obstruction is compatible with a small causal rule

For irrational real $x$, an integer $b\ge2$, and a nonzero integer
$h$, the sequence $z_n=\exp(2\pi i h b^n x)$ has no finite stationary linear
realization. The inherited HBC proof turns any putative recurrence into a
nonzero polynomial vanishing at infinitely many distinct phases. Nevertheless
$z_{n+1}=z_n^b$ is one exact nonlinear generator.

The new finite inequality CS-05 makes the approximation question quantitative.
For integer dimensions $0\le d<m\le L$, a length-$L$ record,
$N=L-m+1$, and delay Gram
$G=H(z)^*H(z)/N$, every approximation whose delay matrix has rank at most
$d$ satisfies
$$
\frac1L\sum_{k<L}|z_k-y_k|^2
\ge\frac{N}{mL}\sum_{j=1}^{m-d}\lambda_j(G).
$$
The eigenvalues are in increasing order. The proof projects onto a nullspace
of the approximating Hankel matrix and counts how often each scalar error
appears. It holds for arbitrary complex finite data.

If $x$ is normal, each fixed-width Gram tends to identity by Weyl's
criterion. First taking $L\to\infty$, then taking $m\to\infty$,
shows that the best fixed-dimensional stationary linear approximation has
asymptotic MSE one, even if its model is freely refitted at every horizon.
For $x=\pi/16$ this specialization is conditional on the very normality
that remains open. The finite inequality itself is unconditional.

This points toward a target-specific signed certificate: accurately predicting
every phase is stronger than accurately determining its mean. A zero predictor
has phase MSE one yet the correct limiting mean for a normal signal. The useful
certificate can preserve the signed target without compressing the entire
phase trajectory into fixed linear rank.

## 6. Signed transport gives a concrete remaining obligation

For any retained dictionary $q_n$, transport $A_n$, covectors
$\ell_n$, residual $r_n=q_{n+1}-A_nq_n$, and target error $e_n$,
suppose
$$
z_n=(\ell_n-\ell_{n+1}A_n)q_n+e_n.
$$
Then the exact identity is
$$
\boxed{\frac1B\sum_{n=B}^{2B-1}z_n
=\frac{\ell_Bq_B-\ell_{2B}q_{2B}}B
+\frac1B\sum_{n=B}^{2B-1}\ell_{n+1}r_n
+\frac1B\sum_{n=B}^{2B-1}e_n.}                                   \tag{T6}
$$
Substitution and telescoping prove it. Correctly transported moving frames
leave each scalar term invariant. Only the **signed projected residual** is
charged; an absolute bound on every coordinate error would be stronger.

This identity supplies a workable source-specific research target: construct
the dictionary and prove sublinear boundary cost, vanishing signed residual
mean, and vanishing target approximation cost for all required shells. The
actual zero seed and source law must enter the proof. The unchanged-forcing
seed $-\pi/16$ has completed phase one, so it must leave a nonvanishing
budget or stationary component. No such original-source bound is asserted here.

## 7. What survives the “reverse Feynman” analogy

The literal mathematical direction is
**lawful observations -> identified generators -> composed response -> certified
completion**. Matrix multiplication sums coordinate paths without observing
each path separately. Coherent forward comparisons retain relative phases that
intensity-only reports would discard.

Feynman's [1948 formulation](https://authors.library.caltech.edu/records/9h858-5hv71)
starts with specified quantum dynamics and action-weighted histories. A generic
Jacobian diagram does not supply that action, a continuum integration measure,
unitarity, or the required limiting construction. Feynman diagrams organize
perturbative contributions rather than being the individually observed paths
in this acquisition problem. The analogy identifies an inverse generative
question; the actual theorems here are the finite algebraic and analytic ones
spelled out above.

There is a further information-loss test at the final arrow. A closed-walk zeta
does not determine every anchored response: a scalar diagonal matrix and a
Jordan perturbation have the same traces and determinant but different
off-diagonal transfer. Conversely, an invisible direct summand changes the
carrier zeta without changing a selected boundary response. PG-07 proves both.
Each compression must preserve the user's chosen target, and its equivalence
relation must be stated.

The earned conclusion is a finite set of exact reconstruction theorems and a
sharper infinite-observable boundary. Within a declared model, separation can
be resolved while the adequacy of that model as a map of the intended source
remains a separate question. Neither diagnostic is a single truth probability.
