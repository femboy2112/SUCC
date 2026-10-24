# All Pascal rank laws can be exact while positional frequencies fail

**Date:** 2026-10-24. **Parent:** draft #274 at
`d942c4707d750f788f39acb137a04e871a93e0a6`.
**Status:** elementary paper construction and exact finite calibration;
classical product probability, Bernoulli ergodicity and Birkhoff's theorem
are used for the infinite process. No new formal-kernel authority or claim
of scholarly priority. This is a synthetic binary process, not the BBP
source and not a counterexample to Hypothesis A. Pi normality remains OPEN.

## 1. The distinction this construction tests

The author's suggestion to use observers **jointly** is mathematically
material. A collection of correct marginal laws need not determine their
joint law. This remains true even if the collection includes the exact
Pascal/binomial rank distribution at every contiguous window length,
the process is stationary and ergodic, every pair of bits is independent,
and every contiguous word of length at most three has its fair frequency.

We construct a process with all those properties whose four-word
frequencies are wrong. Thus merely extending the rank-observer menu to
all lengths does not remove the positional fiber found in
[the Pascal/Lucas quotient dossier](PI_PASCAL_LUCAS_QUOTIENT.md).
The genuinely joint law of all prefix ranks would recover the bits; that
stronger claim is not refuted here.

## 2. One four-bit block

For a word $x=(x_1,x_2,x_3,x_4)$ in $\{0,1\}^4$, put
$s_i=(-1)^{x_i}$ and

$$
F(x)=s_1s_2s_4-s_1s_3s_4=s_1s_4(s_2-s_3).
$$

For a rational parameter $t$ with $|t|\le1/2$, define

$$
P_t(x)=\frac1{16}(1+tF(x)).
$$

Because $F$ takes only the values $-2,0,2$, this is nonnegative.
Each nonconstant Walsh character sums to zero under the uniform law,
so $\sum_xP_t(x)=1$. We will take $t=1/4$, where all sixteen words
have positive mass: four have mass $3/32$, four have mass $1/32$, and
eight have mass $1/16$.

### Every proper contiguous subblock is uniform

Each term of $F$ contains both positions 1 and 4. A proper contiguous
subinterval of $\{1,2,3,4\}$ omits at least one of these endpoints.
Summing over that missing bit kills both perturbation terms. Therefore
any proper contiguous subblock of length $r$ has exactly the uniform
law on $\{0,1\}^r$.

Every two-coordinate marginal, including noncontiguous pairs, is also
uniform: the perturbation has Walsh degree three, and integrating out
any coordinate present in a term kills that term.

### The full rank law is exactly Pascal

The transposition of positions 2 and 3 preserves the number of ones and
sends $F$ to $-F$. Hence the perturbation sums to zero on each rank level:

$$
\sum_{x_1+x_2+x_3+x_4=k}P_t(x)=\frac{{4\choose k}}{16}.
$$

All symmetric functions of the block therefore have exactly their fair
expectation, although $P_t$ is nonuniform whenever $t\ne0$.

## 3. An explicitly stationary and ergodic infinite process

Let $(B_j)_{j\in\mathbb Z}$ be independent four-bit blocks of law $P_t$.
Let $R$ be independent and uniform on $\{0,1,2,3\}$. Define the
two-sided binary process

$$
X_n=(B_{\lfloor(n+R)/4\rfloor})_{(n+R)\bmod4+1}.
$$

Uniform alignment alone is not a proof of ergodicity, so we give the
underlying transformation. On the space of alignment/block pairs define

$$
S(r,B)=
\begin{cases}
(r+1,B),&r<3,\\
(0,\sigma B),&r=3,
\end{cases}
\qquad (\sigma B)_j=B_{j+1}.
$$

This transformation preserves the product measure and satisfies
$X_n\circ S=X_{n+1}$. Thus the process is stationary. Also
$S^4(r,B)=(r,\sigma B)$. If an event $A$ is $S$-invariant, each
alignment slice $A_r$ is invariant under the Bernoulli block shift
$\sigma$, so its probability is zero or one. Invariance under $S$
makes the probabilities of all four slices equal. Consequently
$\Pr(A)$ is zero or one. This proves ergodicity of $S$, and its binary
factor is therefore ergodic.

No claim of mixing is needed. Indeed the alignment extension has a
four-cycle factor. This does not prevent ergodicity.

## 4. Exact Pascal rank distributions at every window length

Fix any alignment $r$ and any finite contiguous window of length $n$.
It breaks into an initial partial block, some complete blocks, and a
terminal partial block. If the window lies within one block, it is a
single contiguous segment. Distinct pieces coming from different blocks
are independent. A partial piece of length $a$ has a binomial
$\mathrm{Bin}(a,1/2)$ rank by the uniform-subblock result; a full block
has binomial rank by the rank-level cancellation just proved.

The sum of independent binomial variables with the same success
probability is binomial with the summed number of trials. Equivalently,
their probability generating functions multiply to
$((1+z)/2)^n$. This holds for every alignment separately, so averaging
over $R$ changes nothing. Therefore, for **every** integer $n\ge0$,
every starting time $a\in\mathbb Z$, and every $0\le k\le n$,

$$
\boxed{\Pr\!\left(\sum_{j=0}^{n-1}X_{a+j}=k\right)
={n\choose k}2^{-n}.}
$$

The theorem is not inferred from the finite probes. It follows from
the block factorization for arbitrary $n$.

By ergodicity, for almost every individual binary realization and
simultaneously for all the countably many pairs $(n,k)$, the sliding
window rank frequencies converge to exactly these Pascal probabilities.
Pairwise independence at arbitrary time separations also follows:
conditional on alignment, two bits are either in independent blocks or
in a uniform two-coordinate marginal of one block.

## 5. A signed positional interaction survives

For a stationary four-word window, one of the four alignments is a full
block of law $P_t$. In each of the other three alignments, the window
is the concatenation of two independent proper contiguous pieces, hence
is uniform. Thus its exact law is

$$
Q_t(x)=\frac14P_t(x)+\frac34\frac1{16}
=\frac1{16}\left(1+\frac t4F(x)\right).
$$

Walsh orthogonality gives

$$
\boxed{\mathbb E[s_1s_2s_4]=\frac t4,
\qquad \mathbb E[s_1s_3s_4]=-\frac t4.}
$$

They cancel when positional labels are discarded. They survive as
opposite signed correlations in the joint positional law.

At $t=1/4$ the finite witness is:

| Observable | Aligned independent-block law $P_t$ | Stationary sliding law $Q_t$ | Fair target |
|---|---:|---:|---:|
| word 0010 | $3/32$ | $9/128$ | $1/16$ |
| word 0100 | $1/32$ | $7/128$ | $1/16$ |
| word 0000 | $1/16$ | $1/16$ | $1/16$ |
| triple character on positions 1,2,4 | $1/4$ | $1/16$ | $0$ |
| triple character on positions 1,3,4 | $-1/4$ | $-1/16$ | $0$ |

Every contiguous one-, two-, and three-word frequency is uniform, but
the four-word law fails. Even checking the zero four-word probability
alone would miss the defect. Birkhoff's theorem gives deterministic
realizations with these wrong limiting four-word frequencies, so they
are not binary normal. Base-16 normality would imply binary normality,
and hence fails as well.

### A concrete computable realization is available

For the default parameter, form a 32-symbol alphabet map by assigning
each four-bit word $x$ exactly $32P_{1/4}(x)$ symbols. These
multiplicities are integers 1,2,3. Feed any fixed normal base-32 digit
sequence, for example the classical Champernowne construction, into
this map and concatenate its four-bit outputs.

For each fixed string of input symbols, base-32 normality gives its
uniform limiting frequency. Summing over the finite preimages of
output block strings gives the product block law $P_{1/4}$.
Averaging the four possible starting positions gives $Q_{1/4}$ and
the general stationary window laws above. This constructs a specific
computable nonnormal binary sequence with every Pascal rank law exact
in the limit. The code's symbol table records the finite map; the
normality of the input construction is a classical ingredient, not a
finite test result. See Kozachinskiy--Shen, Section 4.3, for the
classical construction and its normality criterion.

## 6. Entropy and the proposed weaker Hypothesis A criterion

This process has positive entropy arbitrarily close to the maximum.
With entropy measured in bits, the block entropy is

$$
H(P_t)=4-\frac14\left[(1+2t)\log_2(1+2t)
+(1-2t)\log_2(1-2t)\right].
$$

Interpret $0\log_2 0$ as zero. The process entropy per bit is
$H(P_t)/4$. To see this directly, conditional on the alignment, a long
window consists of independent complete blocks plus at most two partial
blocks. Its entropy is $NH(P_t)/4+O(1)$. Forgetting alignment changes
entropy by at most two bits, which disappears after division by $N$.
Thus every nonzero parameter gives entropy strictly below one even
though every window-rank distribution is the fair one.

The strong Piatetski--Shapiro upper-block criterion correctly rejects
this process. Choose a maximally weighted block and repeat it. At binary
length $\ell=4k+r$, $0\le r<4$, the stationary word probability is
at least the aligned contribution

$$
\frac14\left(\frac{1+2|t|}{16}\right)^k2^{-r}.
$$

Its excess over the fair probability $2^{-\ell}$ is at least
$\frac14(1+2|t|)^k$, which grows exponentially for every $t\ne0$.
There is therefore a nonzero asymptotic rate of positional concentration,
even though rank data at all lengths are perfect.

The strong upper-block criterion is classical: see Piatetski--Shapiro
as stated and proved in Kozachinskiy--Shen, Section 4.2, Theorem 3 and
the following remark. The latter explicitly allows subexponential
loss along an unbounded subsequence of block lengths.

## 7. The scope of “all”

This result separates two claims:

1. **All individual rank distributions.** For every window length,
   the distribution of its number of ones matches the fair law.
   This is insufficient, as proved above.
2. **The full joint law of prefix ranks.** If
   $R_j=X_1+\cdots+X_j$, then $X_j=R_j-R_{j-1}$.
   The joint law of $(R_1,\ldots,R_k)$ determines every positional
   $k$-word probability. Nothing here refutes the usefulness of that
   genuinely joint information.

Similarly, this is not a simultaneous countermodel to the authenticated
BBP source, all primary phases, or all source-specific Pascal/Lucas
observations. It establishes a narrower but strong failure mechanism:
even exact rank marginals at all scales plus stationarity, ergodicity,
pair independence and high entropy can leave signed positional
correlations. A source proof must constrain those correlations rather
than averaging them out.

## 8. Exact calibration and authority

The [module](../../observational_succ/pascal_rank_process.py) implements
rational block laws, independent-block rank convolution, whole-block
window enumeration, the separate four-word formula and the deterministic
symbol map. The [tests](../../tests/test_pascal_rank_process.py) compare
these constructions, verify shifted marginal consistency and retain the
uniform mutation $t=0$ which removes the positional defect while leaving
every rank law unchanged.

The [probe](../../scripts/pascal_rank_process_probe.py) records direct
enumeration for lengths 0--10, separate binomial/convolution comparison,
and additional parameters $-1/2$ and $1/3$ at lengths through 64. The
[receipt](PI_ALL_RANK_RECEIPT.json) labels this POST_DISCOVERY: the
Walsh kernel was chosen analytically before these finite checks.
Fourteen focused unit methods passed locally. Root integration may
record further required repository gates separately.

No infinite probabilistic statement is certified by those finite ranges.
The mathematical proof is above; classical probability/normality imports
remain explicit, and external mathematical review has not occurred.

**Primary reference:** Alexander Kozachinskiy and Alexander Shen,
*Automatic Kolmogorov complexity, normality, and finite state dimension
revisited*, arXiv:1701.09060v6 (2020), Sections 4.2--4.3:
https://kozmath.github.io/papers/1701.09060.pdf.
