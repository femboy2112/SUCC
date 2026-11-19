# Independent audit of the five-reading source theorem

**Date:** 2026-11-19. **Scope:** [SOURCE_ACQUISITION.md](SOURCE_ACQUISITION.md),
its exact rational implementation, and the explicitly declared four-pole source
family. The paper argument survives this audit. The independent implementation
passed 116 exact assertions, including hostile seeds, missing observations,
adaptive clocks, and the large-clock conditioning asymptotic.

“Independent” here refers to a separate derivation and implementation route.
The audit does not import `source_acquisition.py`: SymPy propagates raw symbolic
states, differentiates them, and computes a direct five-by-five inverse. The
implementation under review forms normalized interval sums and uses its own
Fraction Gaussian elimination. These routes still share the declared source
formula and the research context. Their agreement is not independent physical
authentication or a proof that an unrestricted source follows that formula.

## 1. Determinant sign without a Cauchy-formula convention

The sign is load-bearing: the block determinant must be a positive sum, so a
column-orientation mistake would invalidate the all-schedules theorem. It can
be checked by polynomial interpolation rather than recalling a Cauchy formula.

Put $d=(7,4,3,2)$, $q(z)=\prod_a(z-d_a)$, and
$p_a(z)=q(z)/(z-d_a)$. In increasing powers of $z$, the coefficient
matrix of the four $p_a$ is

$$
K=\begin{pmatrix}
-24&-42&-56&-84\\
26&41&50&61\\
-9&-12&-13&-14\\
1&1&1&1
\end{pmatrix},\qquad \det K=120.
$$

For $x_i=8j_i$, multiply row $i$ of
$C_{ia}=1/(x_i-d_a)$ by $q(x_i)$. The resulting matrix is $VK$,
where $V_{ik}=x_i^{k-1}$ is a Vandermonde matrix. Hence

$$
\det C
=\frac{120\prod_{i<k}(x_k-x_i)}{\prod_i q(x_i)}
=\frac{120\,8^6\prod_{i<k}(j_k-j_i)}
       {\prod_{i,a}(8j_i-d_a)}.
$$

When $1\le j_1<\cdots<j_4$, both numerator and denominator are strictly
positive. Multilinearity on four nonempty ordered disjoint time intervals now
gives the claimed positive block expansion. Every term has the same sign;
there is no cancellation assumption. This establishes the universal sign
argument independently of numerical examples.

The raw-to-normalized row scaling has determinant
$16^{-\sum_i t_i}$. The subsequent difference operation is lower
triangular with diagonal one: it subtracts each **original normalized** row
from its successor. Consequently
$\det R_t=16^{\sum_i t_i}\det B$, with no additional sign or radix
factor. For consecutive clocks $N,\ldots,N+4$, the four interval weights
contribute $16^{-(4N+10)}$, leaving
$\det R_N=16^N\det C_N$. Both factors were checked exactly.

**Quantifier boundary.** The theorem covers every strictly increasing
five-tuple of finite nonnegative integer clocks in the stated family. Over a
characteristic-zero field, the rational determinant remains nonzero; its
positivity is a statement in the real embedding used in the proof. Repeated
clocks, altered poles, and additional forcing are different hypotheses.

## 2. The adaptive lower bound is stronger than parameter counting

The transcript argument is valid without continuity of the acquisition policy.
For any fixed run with $k\le4$ readings, its observation matrix has a
nonzero kernel vector $u$. A sufficiently small nonzero displacement
$\theta+\varepsilon u$ remains in any stipulated open neighborhood of
$\theta$. It reproduces the first reading. Inductively it then reproduces
the next chosen clock, reading, and stopping decision, because those choices
depend only on the already identical transcript. The two sources therefore
produce the same output, although the target parameter vectors differ.

This proof does not assume that the entire adaptive measurement map is linear.
Only the observation rows on the fixed transcript are linear, which is enough.
Clock labels cannot encode additional source information when the policy
computes them solely from prior readings. Source-triggered event times or other
unrecorded measurements would be additional observations outside this model.

The lower bound is for recovery of the whole freely varying five-dimensional
parameter vector. It is not automatically a lower bound for every scalar target
or smaller prior class. The rational version works on all $\mathbb Q^5$
because the observation matrix and a nonzero kernel vector are rational.
The real open-set theorem and the all-rational-source theorem are distinct
domain statements.

The audit includes a discontinuous policy whose next gap depends on the parity
of $\lfloor|U_t|\rfloor$, and which can stop after three negative-state
readings. A positive case takes four readings at $(1,4,7,9)$; a negative
case takes three at $(1,3,6)$. In each case a nonzero rational kernel
perturbation reproduces the entire adaptive transcript exactly. These two
controls illustrate the proof; they are not substitutes for its quantifiers.

## 3. A concrete separation of volume and directional accuracy

For consecutive clocks, define
$(C_N)_{ia}=1/(8(N+i)-d_a)$, $1\le i,a\le4$, and let $D$ be
the four-by-five innovation matrix with $-16,1$ in consecutive columns.
The coefficient part of the raw inverse is exactly $C_N^{-1}D$.

The Cauchy determinant gives

$$
\lim_{N\to\infty}N^{16}\det C_N
=\frac{1440}{8^{10}}=\frac{45}{2^{25}}.
$$

Each three-by-three cofactor has a fixed nonzero numerator and nine denominator
factors asymptotic to $8N$. Consequently every entry of $C_N^{-1}$
has order $N^7$. More precisely, with indices $a,i\in\{1,2,3,4\}$,

$$
L_{ai}:=\lim_{N\to\infty}N^{-7}(C_N^{-1})_{ai}
=(-1)^{a+i}\frac{8^4 W_a V_i}{1440},
$$

where $V=(2,6,6,2)$ are the Vandermonde products after deleting one
clock, and $W=(2,20,30,12)$ are the pole products after deleting one
column. Every constant is nonzero. In fact, the cofactor ratio cancels nine
of the determinant's sixteen denominator factors, leaving a product of seven
affine factors divided by a fixed nonzero constant. Each inverse entry is
therefore a polynomial in $N$ of degree seven. The symbolic audit verifies
the degree and all sixteen
leading coefficients.

Because the signs alternate across a row of $C_N^{-1}$, adjacent terms
in the product with $D$ reinforce their absolute values. Its row absolute
sums are exactly 17 times those of $C_N^{-1}$. The largest leading row
is the third, giving

$$
\boxed{\lim_{N\to\infty}N^{-7}\|C_N^{-1}D\|_\infty
=\frac{69632}{3}.}
$$

The four singular values of $C_N$, in decreasing order, give a more complete
description of this directional loss:

$$
\boxed{\sigma_k(C_N)=\Theta\!\left(N^{-(2k-1)}\right),\qquad
k=1,2,3,4.}
$$

**Exterior-power proof.** For each $k$, every $k$-by-$k$ Cauchy
minor has a fixed nonzero Vandermonde numerator and $k^2$ denominator
factors asymptotic to $8N$. Each minor therefore has order $N^{-k^2}$.
These minors are the matrix entries of the exterior power
$\bigwedge^k C_N$. In this fixed finite dimension, its operator norm is
bounded above and below by constant multiples of its largest absolute entry,
so $\|\bigwedge^k C_N\|_2=\Theta(N^{-k^2})$. Applying exterior powers
to a singular value decomposition shows that this norm equals
$\sigma_1(C_N)\cdots\sigma_k(C_N)$: the exterior powers of the two
unitary factors preserve norms, and the largest diagonal product is the product
of the largest $k$ singular values. Dividing consecutive products gives
$\sigma_k=\Theta(N^{-k^2+(k-1)^2})$, as asserted. Thus the determinant
exponent is $16=1+3+5+7$, while the weakest coefficient-to-innovation
direction has exponent seven. No numerical singular-value estimate is used.

For fixed positive raw error widths $\epsilon_0,\ldots,\epsilon_4$, the
whole parameter fiber nevertheless has volume

$$
\boxed{\operatorname{vol}(\mathcal K_y)
\sim\frac{8^{10}}{45}\left(\prod_{i=0}^4\epsilon_i\right)
N^{16}16^{-N}.}
$$

For a uniform width $\epsilon$, the sharp worst-case coefficient error
is therefore asymptotic to $(69632/3)\epsilon N^7$, even as this volume
tends to zero exponentially. The seed row is also $O(N^7)$, because
$s=16^{-N}U_N-a_Nc$ and $a_N$ is uniformly bounded. Thus the full
inverse norm has order $N^7$, as claimed in SA-04.

The apparent tension disappears once the compatible set is regarded as a
parallelepiped with unequal directional widths. Volume records their product;
the inverse rows record the target-coordinate widths. All these statements
refer to fixed raw readout and parameter units. They compare different
five-clock schedules, not the accumulation of every earlier observation.
Retaining additional honest readings still intersects compatible sets and
cannot enlarge them.

## 4. Held-out exact checks and hostile controls

The audited schedules differ from those in the original acquisition test file:

| Five raw clocks | Extra prediction clock | Purpose |
|---|---:|---|
| $(4,9,21,44,67)$ | 74 | Large unequal gaps |
| $(8,13,21,34,55)$ | 62 | Fibonacci clocks after a nonzero start |
| $(7,8,9,10,11)$ | 18 | Consecutive-clock determinant |
| $(3,5,8,10,13)$ | 20 | Explicit 36-term positive block expansion |

For every schedule, the script constructs raw symbolic states from the
recurrence, extracts all five derivative columns, and directly inverts the
resulting matrix. A separate interval-sum construction gives the same inverse
and determinant. It then reconstructs a signed rational parameter vector and
checks a subsequent state.

The hostile controls distinguish the actual hypotheses:

- **Seed $-x$.** The formal symbol $x$ is retained exactly, giving
  recovered vector $(-x,4,-2,-1,-1)$. All four normalized innovations
  agree with the zero-seeded source, while the retained first reading separates
  them. The symbolic identity holds under the substitution $x=\pi/16$;
  no floating equality test or numerical value of pi is used.
- **Wrapped alias.** The seed $1/16$ produces integer raw differences
  $16^{t-1}$ at every sampled positive clock. Fractional readings agree,
  while raw reconstruction returns the distinct seed exactly.
- **Four readings.** A nullspace calculation on the first four raw rows
  supplies a source perturbation whose independently evolved sampled states
  are exactly $(0,0,0,0,1)$. The fifth reading sees the missing direction.
- **Signed determinant expansion.** All 36 terms in the small irregular
  schedule are individually positive, and their exact sum equals the direct
  block determinant.

The implementation under review accepts rational data. Symbolic $x$ handling
belongs to this independent audit; it is not a claim that `Fraction` can store
an arbitrary exact real number. Exact source identification is an ideal
observation theorem; the paid precision bounds govern finite-error readings.

## 5. Findings, limits, and reproduction

No load-bearing error was found in the acquisition, adaptive lower bound,
fiber-volume, or conditioning arguments. During review, SA-05 was clarified to
require the authentic zero seed in $U_n+T_n=16^nx$, and now states the
general identity $U_n+T_n=16^n(s+x)$. The chronological definition of
$W_B(h)$ is also explicit. These corrections prevent an anchor or shell
convention from disappearing inside the completion statement.

The audit gives no proof of source-selected signed cancellation, pi normality,
or authenticity of an unrestricted source. A delayed forcing impulse remains a
countermodel outside the declared family. This is the exact location at which
finite identification would cease to justify extrapolation.

Run from the repository root with SymPy available:

```sh
python research/2026-11-19/causal_generator_reconstruction/source_independent_audit.py \
  --output research/2026-11-19/causal_generator_reconstruction/receipts/source_independent_audit.json
```

**Observed:** SymPy 1.14.0; all 116 assertions passed. The
[JSON receipt](receipts/source_independent_audit.json) records exact symbolic
outcomes, determinant signs and bit lengths, matrix and inverse digests, and the
audited implementation hash. Digests use canonical rational strings `p/q` in
row-major JSON with compact separators, so another rational implementation can
reproduce them without importing this audit. The finite controls corroborate
the implementation; the universal conclusions rest on the stated paper proofs.
