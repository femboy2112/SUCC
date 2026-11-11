# Uniform escape budgets from a classical transcendence measure

**Truth state:** derived mathematical bounds, conditional only on the named
classical theorem and the already proved beta-matrix source. These are
deliberately enormous upper bounds. No computation was run to their stated
horizons, and no new transcendence measure is claimed.

This complements the source-adaptive certificate interface: adaptive
refinement normally establishes a vastly sharper certificate, while the
following bounds quantify its eventual success before any such search.

## 1. Imported quantitative theorem and conventions

Let P be a nonzero integer polynomial of degree at most two. Its height is
the largest absolute value of its coefficients. Set

\[
 H=\max(16,\operatorname{height}(P)),\qquad
 K=2^{43}=8\,796\,093\,022\,208,
 \qquad B=\operatorname{bit\_length}(H).
\]

Thus `H<2^B`, and B is a positive integer.

Waldschmidt's **Corollary 3.2** gives

\[
 \log |P(\pi)|>
 -2^{40}D(\log H+D\log D)(1+\log D)
\]

for nonzero integer P of degree at most `D>=2`, with `H>=16`.
The original is *Transcendence measures for exponentials and logarithms*,
J. Austral. Math. Soc. 25 (1978), pp445–465, Corollary3.2 at p452:
<https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/JAustralMS25-1978-445-465.pdf>.
Its formula is also reproduced in Table1 of Gallego-Hernández and Mansutti,
STACS2025:
<https://drops.dagstuhl.de/storage/00lipics/lipics-vol327-stacs2025/html/LIPIcs.STACS.2025.37/LIPIcs.STACS.2025.37.html>.

Take `D=2`. The height hypothesis holds because H is at least16. Since
`log H>=4 log2`, the exponent's magnitude is strictly less than

\[
 2^{41}\cdot\frac32\log H\cdot2
 =3\cdot2^{41}\log H<2^{43}\log H.
\]

Consequently the convenient conservative bound is

\[
 \boxed{|P(\pi)|>H^{-K}.}
\]

Using degree two as an upper bound is valid for degree-one P as well. It
does not require P to be irreducible, primitive, monic, or square-free.

## 2. A uniform source-stage budget

Write `P(X)=uX^2+vX+w`, with zero leading coefficient allowed. On `[3,4]`,

\[
 |P'(t)|\le8|u|+|v|\le9H.
\]

The geometric beta-matrix source provides strict intervals `I_k` containing
pi, with

\[
 |I_k|=W_k=\prod_{j=1}^k\frac{j}{2j+1}<2^{-k}
 \quad(k\ge1).
\]

Set the symbolic stage budget

\[
 \boxed{k_*=(K+1)B+4.}
\]

Because `H<2^B`,

\[
 W_{k_*}<2^{-k_*}
 =\frac1{16\,(2^B)^{K+1}}
 <\frac1{16H^{K+1}}.
\]

The exact image range of P on `I_{k_*}` has width at most

\[
 9H W_{k_*}<\frac9{16}H^{-K}<|P(\pi)|.
\]

It contains `P(pi)`. A real interval containing both zero and `P(pi)` would
have width at least `|P(pi)|`; therefore this range excludes zero. Thus the
source-derived polynomial separation search has succeeded **by stage
`k_*`**, irrespective of its actual sign.

The range-computation convention matters. This proof applies directly to
the exact quadratic range computed from both endpoints and, when interior,
the vertex. It also applies to the elementary monomial interval enclosure
`u*I^2+v*I+w`: on positive `I=[ell,h]` its width is exactly

\[
 |u|(h^2-\ell^2)+|v|(h-\ell)
 \le9H(h-\ell).
\]

An arbitrary sound but needlessly wide enclosure has no such stage guarantee
until its width is bounded. Soundness alone is insufficient for this
particular quantitative statement.

The integer `k_*` itself has a short representation. Actually refining the
source through that many stages is not practical. The interface should
compute the adaptive certificate and retain `k_*` as a theorem-backed bound.

### The independent rotation source satisfies the same stage budget

The paired alternating-series source has stage counter `k>=1`. Its exact
interval width is

\[
 W^{\mathrm{rot}}_k=
 \frac4{4k-1}\left(2^{-(4k-1)}+3^{-(4k-1)}\right)
 <\frac{2^{4-4k}}{4k-1}<2^{-k}.
\]

For the final inequality, `2^(4-3k)<=2<4k-1` for every `k>=1`.
Its intervals are also strict enclosures in `[3,4]`. Therefore the same
stage budget `k_*` applies when the generated certificate names the
rotation source. The counters of the two sources retain their own meanings;
this shared upper bound does not assert equal precision at equal stages.

## 3. Uniform distance from every candidate periodic point

Let alpha be any real root of P in `[3,4]`. The mean value theorem and the
previous bounds give

\[
 |P(\pi)|=|P(\pi)-P(\alpha)|
 \le9H|\pi-\alpha|.
\]

Hence

\[
 \boxed{|\pi-\alpha|>\delta_H:=\frac1{9H^{K+1}}.}
\]

Every nonempty candidate period in the Farey observer supplies such a
degree-at-most-two nonzero integer polynomial. Mixed periods select a
quadratic root in the bracket; pure periods select a rational endpoint.
This distance bound therefore covers both, even though a degree-one or
source-adaptive estimate is usually far sharper for pure periods.

The global polynomial must use the actual prefix endpoint matrix:
`F=EWE^{-1}`, `P(X)=F_21 X^2+(F_22-F_11)X-F_12`.
The primitive integer polynomial can reduce H without changing its roots.
Bounds built from a local polynomial in a normalized residual cannot be
silently substituted for this global `[3,4]` estimate.

## 4. A 1/5 mixed-block width bound

Let W be a nonempty word containing both L and R. Every entry of W is a
positive integer and its determinant is one. In
`W=[[a,b],[c,d]]`, the equation `ad-bc=1` implies `ad>=2`. Thus at least one
diagonal entry is at least two. Entrywise, W dominates either

\[
 LR=\begin{pmatrix}2&1\\1&1\end{pmatrix}
 \quad\text{or}\quad
 RL=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]

Use `(q,s)` for the current positive denominator pair to avoid conflating
matrix entries with denominator symbols. Under LR, the new product is

\[
 (2q+s)(q+s)=5qs+q^2+(q-s)^2>5qs.
\]

Under RL it is

\[
 (q+s)(q+2s)=5qs+s^2+(q-s)^2>5qs.
\]

Entrywise dominance preserves these inequalities. Therefore one complete
mixed block contracts the Farey interval width by **strictly less than
1/5**. Iterating r blocks gives

\[
 |J_NW^r|<\frac1{qs\,5^r}\le5^{-r}\quad(r\ge1).
\]

This is stronger than the simpler valid 1/4 bound. Neither bound asserts
a pointwise Euclidean Lipschitz constant for the global Möbius map.

Choose

\[
 \boxed{r_*=(K+1)B+4.}
\]

Since `5^{-r_*}<2^{-r_*}<1/(16H^{K+1})<delta_H`, the actual pi path cannot
follow r_* complete copies of the candidate mixed block. The same budget
would remain valid with the weaker 1/4 proof.

## 5. Pure-period budget without materializing it

Let the period be `L^p` or `R^p`, `p>=1`, at denominators `(q,s)`.
After r complete blocks their exact widths are respectively

\[
 \frac1{q(s+rpq)},\qquad \frac1{s(q+rps)}.
\]

Because `q,s,p>=1`, either is at most `1/(1+r)`. Formally take

\[
 \boxed{r_*=9H^{K+1}.}
\]

Then

\[
 |J_NW^{r_*}|\le\frac1{1+r_*}
 <\frac1{r_*}=\delta_H<|\pi-\alpha|.
\]

So r_* complete copies cannot survive. Store this bound as an exact symbolic
expression, for example coefficient9, baseH, exponent`K+1`. Its ordinary
integer expansion would have trillions of digits even for the smallest H.
No code should materialize this optional theorem bound as part of normal
certificate generation. The adaptive rational separation yields a much
smaller practical r via the same exact denominator formulas.

## 6. Translating a block budget into a witness index

Suppose the proposed tail begins at zero-based position `N>=0`, has block
length `p>=1`, and its first block has actually been observed. If r_* full
blocks cannot survive, its **first** divergence j satisfies

\[
 N+p\le j\le N+r_*p-1.
\]

The preceding p-shift still agrees with the candidate pattern, so

\[
 w[j-p]\ne w[j].
\]

The period-witness start index is `j-p`, bounded by
`N+(r_*-1)p-1`; it is not j itself. The statement about the first divergence
is needed if the verifier compares against the candidate block rather than
directly checking p-shifted output letters.

## 7. Dominance boundary

These imported bounds strengthen a qualitative termination proof into a
uniform theorem in terms of polynomial height, but their constants make
them unsuitable as an operational schedule. The useful executed algorithm
remains the exact source-adaptive separator, followed by an exact cylinder
escape computation and independent witness verification.

The research target left open is a substantially sharper effective bound
for this structured family of candidate polynomials, or another new
statistical theorem with its own proof. The existence of a general uniform
pi separation bound is not open. These estimates supply no normality,
digit-frequency, parity-cancellation, or RH conclusion.
