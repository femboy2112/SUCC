# Ordered weaving hidden from every symmetric pair observable

**Status:** PROVED LOCAL constructions and countermodels. These are classical
probability models, not a proved law for the BBP source. Parent source commit:
`fec5cdda24ca36328e123b0b367a0628491e1eb8`.

## 1. The root/maximum identity has a constructive coupling

For independent uniform variables on `[0,1)`, `P(max(U,V)<=r)=r^2` for
`0<=r<=1`; this is the distribution of `sqrt(U)`. Equality in distribution
alone specifies neither an ordered pair nor its temporal law.

There is nevertheless an explicit constructive strengthening. Draw independent
uniform `R0,V`, put `R=sqrt(R0)` and `L=R V`. The pair `(L,R)` has density 2
on `0<l<r<1`, exactly the sorted pair of independent uniforms. An additional
orientation rule determines whether the ordered output is `(L,R)` or `(R,L)`.
A fair independent orientation produces independent uniform coordinates.
Other orientation rules can retain the *entire sorted-pair law* while producing
dependence with a signed response. Thus the root can be the maximum pathwise
under a specified construction, as well as having the same marginal law.

## 2. A quarter-cell coupling with an invisible orientation parameter

Let `j(x)=floor(4x)` for `0<=x<1`, and define

\[
a=(1,1,-1,-1),\qquad b=(1,-1,1,-1),\qquad
c=ab=(1,-1,-1,1)
\]

on the four consecutive quarter intervals. These are Walsh/Rademacher
observables, expressible in the dyadic Haar algebra. Specifically `a` is the
first Haar sign, while `b` is the normalized sum of the two next-level Haar
functions. Products and linear combinations remain in this finite dyadic
observable algebra. The functions `a,c` have mean zero, squared norm one, and
are orthogonal in uniform measure.

Define the ordered wedge and density

\[
G(x,y)=a(x)c(y)-c(x)a(y),\qquad
p_\epsilon(x,y)=1+\epsilon G(x,y),\quad |\epsilon|\le\tfrac12.
\tag{1}
\]

The quarter-cell matrix of `G` is

\[
\begin{pmatrix}
0&-2&0&2\\2&0&-2&0\\0&2&0&-2\\-2&0&2&0
\end{pmatrix}.
\]

Its range is `{-2,0,2}`, so (1) is nonnegative. Its rows and columns integrate
to one because `a,c` have mean zero. It therefore defines a joint probability
law with uniform marginals.

For any bounded measurable **swap-symmetric** observable `H(x,y)=H(y,x)`,

\[
\int H(x,y)p_\epsilon(x,y)\,dx\,dy=\int H(x,y)\,dx\,dy.
\tag{2}
\]

Proof: `G(y,x)=-G(x,y)`, so the extra integral equals its own negative.
The assertion extends to integrable `H` by truncation when appropriate. Taking
`H` to be indicators proves equality of laws for every symmetric observable:
the full unordered pair, minimum, maximum, sum, product, and every norm
invariant under exchanging the two coordinates. In particular

\[
\Pr_\epsilon(\max(X,Y)\le r)=r^2.
\tag{3}
\]

This does not assert invariance for a norm with unequal coordinate weights.

The orientation rule in section 1 realizes (1) constructively: given sorted
`(L,R)`, choose `(X,Y)=(L,R)` with conditional probability

\[
\frac{1+\epsilon G(L,R)}2,
\tag{4}
\]

and otherwise choose `(R,L)`. The allowed parameter range makes (4) a valid
probability. Multiplying the sorted density 2 by (4) gives precisely (1).

The ordered probes, unlike (2), respond:

\[
\mathbb E_\epsilon[a(X)c(Y)]=\epsilon,\qquad
\mathbb E_\epsilon[c(X)a(Y)]=-\epsilon,\qquad
\mathbb E_\epsilon G=2\epsilon.
\tag{5}
\]

Even the squared ordered response is blind to the parameter:
`E_epsilon[G^2]=2` for every allowed epsilon, since `G^2` is symmetric.
Thus `epsilon=1/4,-1/4,0` have the same symmetric laws and the same squared
response, but respective signed wedge means `1/2,-1/2,0`.

## 3. A stationary causal law with a literal quarter-turn mode

Use (1) as a transition kernel:

\[
P_\epsilon(x,dy)=p_\epsilon(x,y)\,dy.
\tag{6}
\]

Uniform measure is stationary. In the quarter partition this is the exact
four-state transition matrix `T_ij=(1+epsilon G_ij)/4`, followed by a uniform
draw within the destination quarter. No limiting argument is needed for its
existence. Start the process in uniform measure.

As an operator on functions,

\[
P_\epsilon a=-\epsilon c,\quad P_\epsilon c=\epsilon a,
\quad \phi=a+ic,\quad P_\epsilon\phi=i\epsilon\phi.
\tag{7}
\]

For every integer `k>=0`,

\[
\mathbb E[\overline{\phi(X_0)}\phi(X_k)]=2(i\epsilon)^k.
\tag{8}
\]

The common basis and phase orientation are declared by (7); (8) is a classical
complex correlation. It is not evidence of quantum mechanics or entanglement.
The pointwise squared norm `|phi|^2=2` is constant.

If `s(k)=(-1)^floor(k/2)=(1,1,-1,-1,...)`, then

\[
\frac12\mathbb E[a_0a_k+c_0c_k+a_0c_k-c_0a_k]
=\epsilon^k s(k).
\tag{9}
\]

This follows by taking the real part plus the imaginary part of (8). The
generating function is `(1+epsilon z)/(1+epsilon^2 z^2)` whenever
`|epsilon z|<1`. The phase rotates a quarter turn per transition while its
amplitude contracts by `|epsilon|`; for negative epsilon the signed formula
still applies.

Writing `Pi` for averaging and `Q=a tensor a+c tensor c`, kernel multiplication
gives

\[
P^{2m}=\Pi+(-1)^m\epsilon^{2m}Q\quad(m\ge1),\qquad
P^{2m+1}=\Pi+(-1)^m\epsilon^{2m+1}G\quad(m\ge0).
\tag{10}
\]

Every odd-lag unordered-pair law is independent-uniform. Even-lag pair laws
need not be independent. Nevertheless the `+epsilon` and `-epsilon` chains
have identical symmetric pair laws at **every** lag, since their transition
kernels are time reversals. The oriented wedge separates them:

\[
\mathbb E G(X_0,X_{2m+1})=2(-1)^m\epsilon^{2m+1},\qquad
\mathbb E G(X_0,X_{2m})=0.
\tag{11}
\]

Equations (7)--(11) are an exact example joining the user's root/max law,
coherent temporal weaving, and period-four sign. They do not identify this
Markov transition with the deterministic BBP source.

## 4. Carry alignment is an additional, testable choice

For integer residues `j,k mod 4`, let

\[
w(d)=(1,-1,-1,1)_{d\bmod4},\qquad W_{jk}=w(j-k).
\]

Direct evaluation of the sixteen entries gives

\[
W=\tfrac12(a\otimes a+c\otimes c-a\otimes c+c\otimes a).
\tag{12}
\]

Equivalently `phi(j)=(1+i)(-i)^j`, and

\[
\tfrac12\overline{\phi(j)}\phi(k)=i^{j-k}.
\tag{13}
\]

Consequently the density (1) has

\[
\mathbb E_\epsilon W=-\epsilon,\qquad
\Pr_\epsilon(j(X)-j(Y)\bmod4\in\{1,2\})=\tfrac{1+\epsilon}{2}.
\tag{14}
\]

These different signed carry-like responses occur with all the identical
symmetric laws in (2). At lag `k`, the Markov model gives
`E W(X_0,X_k)=epsilon^k w(k)` by taking real minus imaginary parts in (8).

### A positive consequence of the maximum law

The construction above proves nonuniqueness of the signed response, **not**
that symmetric data can never bound it. In fact the user's maximum law has
the following useful consequence when attached to the correct coordinates.

For arbitrary random residues `J,K in {0,1,2,3}`,

\[
\Pr(J-K\bmod4\in\{1,2\})
\ge \Pr(K=1)+\Pr(J=K=0)-\Pr(J<2,K<2).
\tag{14a}
\]

This is a pointwise inequality. Its right-side indicator combination is
positive only at `(J,K)=(2,1),(3,1)`, where the selected event holds, and
negative only at `(1,0)`. It is zero at the other thirteen cells.

If `J=floor(4X)`, `K=floor(4Y)`, both coordinates are uniform, and
`Pr(max(X,Y)<=r)=r^2`, then

\[
\boxed{\Pr(J-K\bmod4\in\{1,2\})\ge\tfrac1{16}.}
\tag{14b}
\]

Indeed the three probabilities on the right of (14a) are respectively
`1/4`, `(1/4)^2`, and `(1/2)^2`. Only those two values of the maximum CDF
and one marginal cell are needed. More generally, if these three quantities
have respective lower/lower/upper errors `eta1,eta2,eta3`, the lower bound
is `1/16-eta1-eta2-eta3`.

The finite inequality was found by a linear-program dual and then proved
directly by the sixteen-cell argument above. No solver correctness or
floating-point optimality claim is needed for (14a)--(14b). No claim of
sharpness under the *full* continuous maximum law is made here.

For the stronger hypothesis that the whole unordered residue-pair law is
independent-uniform, the opposite-residue event alone has probability `1/4`
and is always selected; thus the lower bound improves to `1/4`. The epsilon
family (1) attains its endpoints `1/4` and `3/4` accordingly.

**Orientation control.** The initially proposed wedge
`F=a tensor b-b tensor a` also gives a valid same-maximum coupling and the
same rotation construction using `a+ib`. But `sum(W_ij F_ij)/16=0`: its
signed response is orthogonal to this particular carry gate. Replacing `b`
by `c=ab` is therefore essential for (14). A generic detected dependence is
not automatically the dependence required by the source.

## 5. Exact source transport and remaining obligation

For the authentic BBP source the inherited source-clock theorem says
`[U_n]_4=n mod 4`, where brackets mean reduction of an odd-denominator rational
in the 2-adic ring. Put

\[
j_n=n\bmod4,\quad k_n=[y_n]_4,\quad y_n=U_n-C_n.
\]

Then `C_n mod4=j_n-k_n`, so (13) is an actual source-attached transport:

\[
i^{C_n}=\tfrac12\overline{\phi(j_n)}\phi(k_n).
\tag{15}
\]

These discrete source coordinates are not asserted to be samples of (6).
For the empirical shell average over `B<=n<2B`, define

\[
H_B=\mathbb E_B[a(j_n)a(k_n)+c(j_n)c(k_n)],\quad
F_B=\mathbb E_B[a(j_n)c(k_n)-c(j_n)a(k_n)].
\]

The selected density satisfies exactly

\[
d_B=\tfrac12-\tfrac14H_B+\tfrac14F_B.
\tag{16}
\]

Thus the remaining signed restriction is `H_B-F_B<=2-4delta` eventually
for some `delta>0`. This is a diagnostic decomposition of the existing
obligation, not its proof. In fact `H_B=2 E_B cos(pi C_n/2)` and
`F_B=2 E_B sin(pi C_n/2)`, so it is not a new independent theorem.
Normality would force both quantities to zero; a fixed positive-current
lower bound is therefore not a suitable normality-consistent next target.

Equation (14a) also applies directly to the empirical source residues
`(j_n,k_n)`. It gives a concrete sufficient three-cell-mass criterion:
`P_B(k_n=1)+P_B(j_n=k_n=0)-P_B(j_n<2,k_n<2)>=delta` eventually.
If the source can establish the approximate root/maximum values in (14b)
at those two cuts with total error less than `1/16`, the original selected
density is positive. The required source estimates remain unproved; the
comparison model does not supply them.

## 6. The exact defect when a floor gate crosses an integral

Let `A(x)=1_{floor(x) mod4 in {1,2}}` on all real `x`, right-continuous at
integer boundaries. For any integrable real random variable `Y` and any
finite real anchor `m`,

\[
\mathbb E A(Y)-A(m)
=\sum_{j\in\mathbb Z}(-1)^j
\left(\Pr(Y\ge2j+1)-1_{m\ge2j+1}\right).
\tag{17}
\]

Proof: `A` has jumps `+1,-1,+1,-1,...` at the successive odd integers.
For a fixed sample, only thresholds between `Y` and `m` contribute to the
difference. Their number is at most `|Y-m|/2+1`, which is integrable; Tonelli
on absolute values justifies taking expectations. This proves absolute
convergence of the series in (17).

For `m=E Y`, (17) is the exact signed boundary-flux correction needed before
replacing a gate of a volume integral by an integral of gates. No uniform
smallness follows without control of the probabilities crossing these odd
thresholds. In particular, let `Y=0` or `4`, each with probability one half.
Then

\[
\lfloor\mathbb E Y\rfloor=\mathbb E\lfloor Y\rfloor=2,
\qquad A(\mathbb E Y)=1,\qquad\mathbb E A(Y)=0.
\tag{18}
\]

The ordinary floor-averaging defect is zero while the carry-gate defect is
maximal. For `g=1-2A`, the corresponding values are `g(E Y)=-1` and
`E g(Y)=1`. Thus even exact commutation of an ordinary floor with expectation
does not justify commutation of the signed carry response.

## 7. Provenance, audit scope, and verdict

The constructions and proofs above were derived directly from finite
quarter-cell algebra and probability integration. The first pass used the
`(a,b)` wedge without access to another agent's report. A second pass checked
the translator's carry-aligned `(a,c)` suggestion independently entry by
entry; the two reports consequently are not blind independent discoveries
of that alignment.

A standalone exact `fractions.Fraction` check tested 155 identities for the
initial wedge at epsilon `-1/2,-1/4,0,1/4,1/2`, including lags 0 through 12,
stochasticity, symmetrization, the period-four correlation, and both moments
of the wedge; all passed. Root's dossier audit should reproduce and extend
these checks for the carry-aligned model. This finite receipt calibrates the
formulas; the displayed algebra is the proof for all permitted parameters.

**Verdict:** the coherent-weaving intuition survives as an explicit classical
construction. Distributional radial data can hide an ordered quarter-turn
mode even when every symmetric pair observable is known exactly. The
carry-aligned probe detects precisely the correct four-residue projection.
Conversely, the correctly aligned uniform-marginal maximum law itself
implies a positive `1/16` selected probability by a finite inequality.
Deriving an eventually positive selected density for the authentic zero seed
and four poles remains OPEN; no Markov or independence assumption has been
transferred to that source.
