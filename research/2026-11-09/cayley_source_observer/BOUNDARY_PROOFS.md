# Parity observation with boundary payment and finite source certificates

**Truth state:** the statements proved below are finite inequalities, conditional
limit theorems, and explicit counterexamples. Original-zero hexadecimal parity
balance and base-16 normality of pi remain **OPEN**.

**Provenance:** the Fourier support is inherited from
`scott_omega_causal_weld/SOURCE_SELECTED_ARITHMETIC.md`, F-10, and the earlier
unshifted digit-character calculation. The positive-kernel boundary estimate is
already present, with a different cutoff convention, in
`floor_layercake_prime_carry/THEOREMS.md`, FLP-04. The rational source cone is
CW-03/04 of `scott_omega_causal_weld/THEOREMS.md`. This note supplies a sharp
parity Lipschitz coefficient, their combined source-certified estimate, a
two-fiber boundary recursion, and a conditional stationary-limit consequence.
It does not claim to invent Fourier or Fejer theory. The imported archival
files and original four-pole source are not changed.

## Definitions and conventions

Write `T = R/Z`, `e(t)=exp(2 pi i t)`, and let `d` be the circular distance.
The radix map is `R(t)=16t mod 1`. Set

$$
f(t)=(-1)^{\lfloor16\{t\}\rfloor},\qquad
\mathcal B=\{j/16:0\le j<16\}.
$$

Thus `f` is right-continuous at each cut, takes values in `{-1,1}`, and equals
`sign(sin(16 pi t))` off `B`. Every open boundary strip below uses the strict
inequality `d(t,B)<delta`. A conservative computable upper count may instead
use a non-strict inequality; the resulting extra equality cases only enlarge
the bound.

The exact source-clock connection is `f(U_n+T_n)=s_(n+1)` for the
PPP-02/TFH sign `s_n=(-1)^floor(U_n+T_n)`. A comparison of their means on
the same epoch pays `(s_(2A)-s_A)/A`, at most `2/A`; see NEXT.md. No finite
CRT table is identified with this dossier's circle-parity table without
that shift.

For an integer `H>=0`, use the degree-H Fejer mean

$$
F_H(t)=\sigma_H f(t)
=\sum_{|m|\le H}\left(1-\frac{|m|}{H+1}\right)\widehat f(m)e(mt).
$$

The denominator is `H+1`. FLP-04 calls the corresponding kernel order `H+1`;
its denominator-H convention must not be silently mixed with this one.

## CBO-B01 — exact support and sharp Lipschitz coefficient (PROVED)

For every integer `m`,

$$
\widehat f(m)=
\begin{cases}
16/(\pi i m),&m\equiv8\pmod {16},\\
0,&\text{otherwise}.
\end{cases}
$$

There is no `m=0` exception to interpret: zero belongs to the second case.
Indeed `f(t+1/16)=-f(t)` forces the stated support. On that support, the
sixteen cell integrals are equal after multiplication by their signs and
Fourier phases, and their sum is
`16 integral_0^(1/16) e(-mt) dt = 16/(pi i m)`.

Let

$$
K_H=\left\lfloor\frac{H+8}{16}\right\rfloor,\qquad
L_H=64K_H-\frac{512K_H^2}{H+1}.
$$

Then the exact Lipschitz constant of `F_H` in circular distance is `L_H`, and

$$
L_H\le2(H+1).
$$

For `0<=H<8`, both `K_H` and `F_H` are zero. Otherwise differentiate the finite
sum. Its nonzero derivative coefficients are the positive real numbers
`32(1-|m|/(H+1))`. Hence the maximum absolute derivative is their sum, achieved
at `t=0`. The positive frequencies are `m=16j+8`, `0<=j<K_H`, and

$$
\sum_{j=0}^{K_H-1}(16j+8)=8K_H^2.
$$

Adding the two signs gives exactly `L_H`. Completing the square in `K_H`
proves the upper bound. Equality in `L_H<=2(H+1)` holds whenever
`H=16K-1`, `K>=1`; thus the coefficient 2 cannot be uniformly reduced.

The same observer in the Cayley chart is obtained by replacing `e(mt)` with
`((1+ix)/(1-ix))^m`, where `x=tan(pi t)`. Its derivative with respect to the
Euclidean coordinate `x` is a different quantity. The coefficient above uses
the circular metric, including the compactification seam.

## CBO-B02 — paid boundary reconstruction (PROVED; Fejer bound inherited)

For any points `t_1,...,t_N` on the circle and `0<delta<=1/32`, define

$$
B_N(\delta)=\#\{n:d(t_n,\mathcal B)<\delta\}.
$$

Then

$$
\left|\frac1N\sum_n f(t_n)-\frac1N\sum_nF_H(t_n)\right|
\le\frac{2B_N(\delta)}N
+\frac{4\cot(\pi\delta)}{\pi(H+1)}
\le\frac{2B_N(\delta)}N+\frac1{(H+1)\delta}.
$$

**Proof.** The kernel

$$
\mathcal K_H(u)=
\frac{\sin^2(\pi(H+1)u)}{(H+1)\sin^2(\pi u)}
$$

is nonnegative and has integral one, so `|F_H|<=1`. If
`d(t,B)>=delta`, then `f(t-u)=f(t)` for `|u|<delta`; equality of the distance
with `delta` is allowed. Therefore

$$
|F_H(t)-f(t)|
\le2\int_{\delta\le|u|\le1/2}\mathcal K_H(u)\,du
\le\frac{4\cot(\pi\delta)}{\pi(H+1)}.
$$

The last integration uses the elementary antiderivative of `csc^2(pi u)`.
Alternatively `sin(pi u)>=2u` for `0<=u<=1/2` gives directly the rational
upper bound `1/((H+1)delta)`. On the exceptional points the error is at most
2. Summing proves the assertion. The values chosen at the actual jumps cause
no problem because every jump lies in the exceptional set.

### Why a uniform sharp truncation claim fails

Let `S_K` retain the first `K` positive odd harmonics of the square wave:

$$
S_K(t)=\frac4\pi\sum_{j=0}^{K-1}
\frac{\sin(16\pi(2j+1)t)}{2j+1}.
$$

Choose the irrational point `t_K=sqrt(2)/(64K^2)`. It lies strictly inside the
first digit cell, so `f(t_K)=1`, whereas `|sin u|<=|u|` gives

$$
|S_K(t_K)|\le64K t_K=\frac{\sqrt2}{K}.
$$

Consequently the error is at least `1-sqrt(2)/K` and tends to one. A uniform
`O(1/K)` pointwise error is false even when all evaluation points are
irrational. A finite orbit avoiding the digit cuts has pointwise Fourier reconstruction as the cutoff
increases; that fact supplies no unproved interchange with growing orbit
length.

For completeness, away from the cuts, summation by parts in the geometric
odd-frequency sum yields the valid sharp-partial-sum bound

$$
|f(t)-S_K(t)|
\le\frac4{\pi(2K+1)|\sin(16\pi t)|}.
$$

This has the necessary distance-to-jump denominator. The proof bounds every
partial exponential sum starting at the first omitted index by
`1/|sin(16 pi t)|` and then sums the decreasing coefficient differences.
It is not the unsupported uniform estimate.

## CBO-B03 — a rational source certificate and its exact average cost (PROVED)

Suppose rational lifts `a_n` and rational errors `epsilon_n>=0` satisfy
`|y_n-a_n|<=epsilon_n`. A lower endpoint with its full width is one choice;
the implementation uses the interval midpoint and half-width. Define the
computable upper count

$$
\widehat B_N(\delta)=
\#\{n:d(a_n,\mathcal B)\le\delta+\epsilon_n\}.
$$

Distance from a rational number to the sixteen rational cuts is exactly
computable. The non-strict test is deliberately conservative. The distance
triangle inequality gives `B_N(delta)<=Bhat_N(delta)`, and CBO-B01 gives

$$
\left|\frac1N\sum_n f(y_n)-\frac1N\sum_n F_H(a_n)\right|
\le\frac{2\widehat B_N(\delta)}N
+\frac1{(H+1)\delta}
+\frac1N\sum_n\min\{2,L_H\epsilon_n\}.
$$

The weaker last term `L_H average(epsilon_n)` is also valid. The coefficients,
boundary count, and displayed error budget are rational whenever `delta` is
rational. Evaluation of the trigonometric readout itself needs certified
interval arithmetic if its numerical value is to be called a certificate;
floating evaluation alone remains a diagnostic.

### The implementation's rational trigonometric enclosure

`sine_turns_enclosure` first reduces a rational phase to `[-1/2,1/2]`.
It obtains a strict rational enclosure of pi from the canonical 24-term BBP
certificate, multiplies by twice that phase, and rounds outward to a dyadic
interval. Let its midpoint be `z` and its radius be `rho`. Sine is
1-Lipschitz, so evaluating at z costs at most rho. The code checks
`|z|<=22/7`. For an integer `J>=1`, use

$$
p_J(z)=\sum_{j=0}^{J-1}\frac{(-1)^jz^{2j+1}}{(2j+1)!}.
$$

This is also the Taylor polynomial through degree `2J`, whose even
coefficient is zero. Taylor's theorem, with all derivatives of sine bounded
by one on the real axis, gives

$$
|\sin(z)-p_J(z)|\le\frac{(22/7)^{2J+1}}{(2J+1)!}.
$$

Adding rho therefore gives a fully rational outward enclosure. Multiplying
the sine intervals by the positive weights and an interval for `1/pi`,
then summing, encloses the finite Fejer mean. No floating sine or decimal pi
is a premise. Intersecting the sine interval with `[-1,1]` is sound.
The final Fourier-mean interval plus the rational error budget encloses the
actual completed parity mean. This is a finite certificate, with the BBP
identity and the analytic bounds as explicit mathematical dependencies.

For the authentic source, retain the inherited definitions

$$
P_L=\sum_{j=1}^L16^{-j}r(j),\qquad
B_L=\frac4{15(L+1)^2 16^L},\qquad
a_n=16^nP_L,\quad\epsilon_n=16^nB_L.
$$

CW-04 proves the strict enclosure
`a_n<16^(n-1)pi<a_n+epsilon_n`. For an epoch `A<=n<2A`, `L>=2A-1`, its exact
average width is

$$
\overline\epsilon_{A,L}
=\frac{B_L16^A(16^A-1)}{15A}.
$$

In particular,

$$
\overline\epsilon_{A,2A}
=\frac{4(1-16^{-A})}{225A(2A+1)^2},\qquad
\overline\epsilon_{A,2A-1}
=\frac{16-16^{1-A}}{225A^3}.
$$

Thus the unclipped Fejer transfer error is `O(H/A^3)`, improving the
maximum-width comparison by a factor of order `A`. This concerns the
Green-completed common-horizon endpoints `16^n P_L`, not the raw states `U_n`.
It does not remove the separate FLP-08 order-`A^2` resolution threshold for
seeing the direct forcing translation at each time.

There is a stronger bounded-observer statement. Set
`Emax=16^(2A-1)B_L` and `gamma=L_H Emax`. The exact clipped payment is

$$
\frac1A\sum_{j=0}^{A-1}\min\{2,\gamma16^{-j}\}.
$$

If `gamma=0`, it is zero. Otherwise put
`q=max(0,ceil(log_16(gamma/2)))`. Splitting off the first `q` terms and summing
the remaining geometric tail bounds it by

$$
\min\left\{2,\frac{2q+32/15}{A}\right\}.
$$

This bound also holds when `q>=A` because of the leading cap 2. For every
integer cutoff schedule satisfying `log(1+H_A)=o(A)` and every
`L_A>=2A-1`, the clipped source transfer tends to zero. This conclusion has a
proved finite-to-asymptotic lift: `Emax<=1/(15A^2)`, so `q=o(A)`. It pays for
source completion only; neither the signed spectral sum nor its boundary
occupation has thereby been estimated.

## CBO-B04 — two-fiber finite boundary recursion (PROVED)

This is applicable to the actual completed orbit and also **exactly** to the
finite common-horizon orbit `a_n=16^nP_L`, before passing to a limit.

Let `t_0,...,t_A` satisfy `t_(n+1)=R(t_n)` on the circle. Put

$$
\mu_A=\frac1A\sum_{n=0}^{A-1}\delta_{t_n},\qquad
\nu_A=(t\mapsto8t)_*\mu_A.
$$

For each integer `j>=0`, take the **open** arcs

$$
r_j=\frac1{4\cdot16^j},\quad
I_j=\{u:d(u,0)<r_j\},\quad J_j=I_j+\tfrac12,
$$

and define

$$
b_j=\nu_A(I_j)+\nu_A(J_j),\qquad
q_j=\nu_A(I_j)-\nu_A(J_j).
$$

The open convention matters at `j=0`: the arcs exclude `1/4` and `3/4`, are
disjoint, and give `b_0<=1`. Closed radius-`1/4` arcs overlap at those two
points and cannot be substituted without an extra boundary term.

The disjoint `I_(j+1)` and `J_(j+1)` are two of the sixteen inverse-image
arcs of `I_j`. Write the mass in the omitted fourteen arcs as

$$
a_j=\nu_A\big(R^{-1}I_j\setminus(I_{j+1}\cup J_{j+1})\big)\ge0.
$$

With `u_n=8t_n mod 1`, the endpoint discrepancy is exactly

$$
e_j=\frac{1_{I_j}(u_A)-1_{I_j}(u_0)}A.
$$

Telescoping the actual finite orbit proves the identity

$$
b_{j+1}=\frac{b_j+q_j}{2}+e_j-a_j.
$$

Consequently, for every integer `J>=0`,

$$
b_J\le2^{-J}b_0
+\sum_{j=0}^{J-1}2^{-(J-j)}q_j
+\frac{2(1-2^{-J})}{A}.
$$

Replacing `q_j` by `|q_j|` and `b_0` by 1 gives a more conservative bound.
All counts, signs, and endpoint terms are exact rational quantities for a
finite rational common-horizon orbit. Equality of a point with an arc endpoint
is decided by the strict inequality, not floating tolerance.

Finally the elementary distance identity
`d(8t,{0,1/2})=8d(t,B)` gives

$$
b_J=\mu_A\left\{t:d(t,\mathcal B)<\frac1{32\cdot16^J}\right\}.
$$

Thus the boundary payment can itself be decomposed into finitely many signed
two-fiber contrasts and an explicit endpoint error. This is a proved reduction
with additional structure. No bound on the original-zero contrasts `q_j` is
asserted. These are real signed observations, not prime-side proxies.

## CBO-B05 — all fixed parity pins imply strip tightness and parity (PROVED CONDITIONAL)

Let `mu_A` be empirical measures of consecutive length-A orbit segments for
`R`; their starting points may depend on `A`. Suppose that, for **every fixed
odd integer** `k`,

$$
\int e(8kt)\,d\mu_A(t)\longrightarrow0\qquad(A\longrightarrow\infty).
$$

Then:

1. For every positive sequence `delta_A -> 0`,
   `mu_A{d(t,B)<delta_A} -> 0`.
2. The parity mean `integral f dmu_A` tends to zero.

The hypothesis is a family of genuine signed arithmetic estimates for the
selected orbit. It is **not established here for pi**. It is stronger than
unconditional parity balance, but strictly weaker than full normality.

### Proof of the stationary-limit step

Compactness of the circle supplies subsequential probability-measure limits
`mu`. For every continuous test function `g`,

$$
\left|\int g\circ R\,d\mu_A-\int g\,d\mu_A\right|
\le\frac{2\|g\|_\infty}A.
$$

Every limit is therefore `R`-invariant. Put `nu=(times 8)_*mu`. It too is
`R`-invariant, and the assumed pins make every odd Fourier coefficient of
`nu` zero. Translation by `1/2` multiplies the kth coefficient by `(-1)^k`.
Hence `nu` and its half-translate have identical Fourier coefficients and
are equal. Uniqueness here follows from approximation of continuous circle
functions by trigonometric polynomials; no arithmetic input is hidden in it.

For any probability measure `nu` invariant under both `R` and translation by
`1/2`, and any closed ball of radius `0<r<=1/32`, the two disjoint balls at
0 and `1/2` lie in `R^-1 B_(16r)(0)`. Therefore

$$
\nu(B_r(0))\le\tfrac12\nu(B_{16r}(0)).
$$

Iteration, or the trivial bound when `r>=1/32`, gives the convenient universal
bound

$$
\nu(B_r(0))\le\min\{1,(32r)^{1/4}\}.
$$

For example, iterate `k=floor(log_16(1/(32r)))+1` times when `r<=1/32`;
each applied small-radius step is valid and `2^-k<=(32r)^(1/4)`.
In particular `nu({0})=nu({1/2})=0`. Independently, atomlessness at those
two points follows immediately because invariance and equal atom masses
force `nu({0})>=nu({0})+nu({1/2})`.

Under `u=8t`, the closed original strip of width `delta<1/32` maps to the
union of the two closed balls of radius `8delta`. Thus every such limit
measure satisfies

$$
\mu\{t:d(t,\mathcal B)\le\delta\}
\le\min\{1,8\delta^{1/4}\}.
$$

The constant 8 is convenient, not claimed optimal. At the discrete open
radii of CBO-B04 the sharper statement is
`mu{d(t,B)<1/(32*16^J)}<=2^-J`.

For fixed `delta`, subsequence compactness and the closed-set bound give
`limsup_A mu_A{d(t,B)<=delta}<=min(1,8delta^(1/4))`. Monotonicity and then
`delta downarrow 0` prove assertion 1 for **any** shrinking sequence, without
claiming a convergence rate. Each limit gives no mass to the discontinuities
of `f`. Moreover `f(t)=g(8t)` away from them, where
`g(u)=sign(sin(2 pi u))` and `g(u+1/2)=-g(u)`. Half-translation invariance
therefore gives `integral f dmu=0`. Passing bounded functions whose
discontinuities have zero limit mass through weak convergence, or using
CBO-B02 with successive limits, proves assertion 2.

### Stationarity cannot be dropped

The nonstationary measure `mu=(delta_0+delta_(1/16))/2` annihilates every
`e(8kt)` with k odd but assigns all its mass to digit cuts. Its image under
R is `delta_0`, so it is not R-invariant. This is a negative control for
using the pin hypothesis on arbitrary clouds: the consecutive-orbit
endpoint argument, or separately established stationarity, is essential.

### Strict weakness relative to normality

Take independent equiprobable base-16 digits in `{0,1}`. Their product law
`mu` is `R`-invariant and is not Haar: fourteen first digits have probability
zero. For every odd `k`, independence and just the first digit give the factor

$$
\frac{1+e(8k/16)}2=\frac{1+e(k/2)}2=0
$$

in `integral e(8kt) dmu`. Thus the entire parity-pin hypothesis holds in an
explicit non-Haar invariant model. Almost every digit sequence for this
Bernoulli law realizes its averages (the usual ergodic theorem), so it also
supplies nonnormal orbit witnesses; the measure countermodel alone already
shows the asserted invariance conditions do not force Haar.

The exponent `1/4` has the correct scale: for this law, `nu=(times 8)_*mu`
has digits in `{0,8}` with equal probabilities. At
`r=(8/15)16^(-j)`, `j>=1`, its mass near zero is `2^-j` (endpoint ambiguities have zero
measure), exhibiting the scaling `r^(1/4)`. No universal larger exponent can
hold over this whole invariant class.

This is an exact formal connection between the Cayley eighth-power phase,
the involution `w -> -w`, the radix-16 successor, and the two-fiber contrasts.
It does not replace the remaining source-selected signed estimate.

### Future-conditioned parity and all finite parity words

The same hypothesis in fact implies uniformity of **every fixed finite
parity word**, not only the one-bit mean. This uses the future-conditioned
recursion already developed for all sixteen digits in
[`recursive_haar_pinbed/THEOREMS.md`](../recursive_haar_pinbed/THEOREMS.md),
RHY-01/#565, applied here to the retained binary factor. It is not a new
principle turning an unconditional marginal into independence.

Use canonical representatives in `[0,1)`, and define
`epsilon(t)=floor(16t) mod 2` and `y=R(t)`. Exactly, including the half-open
digit convention,

$$
u=8t\pmod1=\frac{\epsilon(t)+y}{2}.
$$

The map `u -> (floor(2u),2u mod1)` is a Borel bijection between `[0,1)`
and `{0,1} times [0,1)`. Half-translation of u flips the first coordinate
and preserves the second. Therefore, for **any** probability law mu,

$$
(\times8)_*\mu\text{ is invariant under translation by }1/2
\quad\Longleftrightarrow\quad
\Pr_\mu(\epsilon=b\mid R(t))=\tfrac12
\quad(b=0,1),\quad R_*\mu\text{-almost everywhere}.
$$

Stationarity is not needed for this equivalence. It is needed to iterate
the statement: if `R_*mu=mu`, then for every `k>=1` and word
`w=(w_0,...,w_(k-1))` in `{0,1}^k`, conditioning the first bit on the
entire real future gives

$$
\mu\{\epsilon(R^jt)=w_j:\ 0\le j<k\}
=\tfrac12\mu\{\epsilon(R^jt)=w_{j+1}:\ 0\le j<k-1\}
=2^{-k}.
$$

The first equality uses conditional fairness and stationarity; the second
iterates it, with the empty-word probability equal to one. No ergodicity
assumption is required. The parity process under mu is a fair Bernoulli
process even though the complete hexadecimal digit process need not be Haar.

Apply this to every stationary weak limit in CBO-B05. The earlier proof
gives `mu(B)=0`, and invariance gives `mu(R^(-j)B)=0` for every j. The
indicator of a fixed length-k parity word has discontinuities only in
`union_(j<k) R^(-j)B`, a mu-null set. Weak convergence therefore transports
its integral. Since every subsequential limit gives the same value, the
full empirical frequency tends to `2^(-k)` for every fixed k and every
word. Restricting to starts whose k digits fit inside a length-A block, or
using cyclic block conventions, changes only `O(k/A)` of the frequency.
This conclusion is conditional on the signed pins and supplies no rate or
uniformity for a word length growing with A.

**The converse from fair parity words to the signed pins is false.** Let
`(X_n)_(n in Z)` be independent fair bits and define the stationary
hexadecimal digit process

$$
D_n=2X_{n-1}+X_n\in\{0,1,2,3\},\qquad
t=\sum_{n\ge0}D_n16^{-(n+1)}.
$$

Its circle law mu is R-invariant. Its parity sequence is exactly the iid
sequence X_n, so every finite parity word has probability `2^(-k)`.
Nevertheless, the first future digit `D_1=2X_0+X_1` reveals the current
parity `X_0=floor(D_1/2)`. Current parity is thus deterministic given the
entire real future, rather than conditionally fair. The canonical radix
coding causes no positive-mass endpoint ambiguity in this model.

An explicit failed pin is available. Expanding the independent-bit source,

$$
\int e(8t)\,d\mu(t)
=\prod_{j\ge0}\frac{1+e((9/16)16^{-j})}{2}\ne0.
$$

The contribution from X_(-1) is `e(X_(-1))=1`. The j=0 factor is nonzero;
for j>=1 the moduli are positive cosines with summable deficits from one,
so their product is strictly positive. For example,
`sum_(j>=1) (1-cos(pi (9/16)16^(-j))) <= 81 pi^2/130560 < 1`,
and the product is bounded below by one minus this sum. This is an explicit
stationary countermodel to the converse, not merely an absence of proof.

The hierarchy is therefore strict: full sixteen-digit future-conditioned
Haar implies these parity pins; these parity pins imply all fair parity
words; the reverse implication from fair parity words fails. The iid
`{0,1}`-digit example above shows that the parity-pin condition remains
strictly weaker than full hexadecimal normality. This is the binary-factor
specialization of #565's conditional recursion, with its weaker hypothesis
and its limits stated explicitly.

## CBO-B06 — boundary control alone is strictly weaker than parity (REFUTED shortcut)

Choose a non-eventually-periodic digit sequence using only `2` and `4`, for
example `d_j=4` at square indices and `d_j=2` elsewhere, and let
`alpha=sum_(j>=1) d_j 16^(-j)`. This number is irrational by the elementary
eventual-periodicity characterization of rational radix expansions.

Every shifted tail `v` lies in `[2/15,4/15]`. If `t=(a+v)/16` is an orbit
point, its first digit `a` is 2 or 4 and its distance from the left digit cut
is at least `1/120`; the distance from the right cut is larger. Hence

$$
d(R^n\alpha,\mathcal B)\ge\frac1{120}\quad\text{for all }n\ge0,
\qquad f(R^n\alpha)=1.
$$

All sufficiently narrow strip counts are zero, while the parity mean is
identically one. This disproves boundary avoidance implies parity balance,
even for irrational exact radix orbits. Taking the coherent initial seed
`s=alpha-pi/16` realizes this completed orbit with the same BBP forcing; it
does not realize the required original zero seed.

An opposite coherent control is `s=-pi/16`. Its completed orbit is exactly
zero, and its finite forced states are `U_n^(s)=-T_n` with `T_n>0` and
`T_n=O(n^-2)`. Consequently strips wider than the source-tail scale can
contain every sample. No source-forcing-only, Cayley-only, or
Scott-continuity-only theorem can remove this control without using seed
selection.

## CBO-B07 — finite termination is not a uniform irrationality-rate theorem (PROVED)

Fix any finite set of original-zero indices. For each index, the nested
rational cone shrinks to `16^(n-1)pi`, which is irrational and hence lies on
no rational digit cut. Enumerating increasing rational source horizons must
eventually put the interval strictly inside one digit cell. For finitely many
indices there is a finite horizon at which all cells, and hence all parity
values, are certified. This is a terminating search with a mathematical
termination proof, using the established irrationality of pi and the source
enclosure theorem. It does not require a supplied quantitative irrationality
measure.

Similarly, to distinguish the zero seed from a **given distinct rational
seed** in the unwrapped source computation, comparing the marked seeds or
the exact difference `16^n s` already suffices. A circle observer can alias
some seeds, such as `s=1/16` after time zero; that is lost observational
information, not a need for a transcendence exponent.

An a priori resource bound on the search, a prescribed common horizon that
works at all increasing indices, and an all-epoch signed asymptotic estimate
are different requirements. They may need quantitative separation estimates;
their necessity cannot be inferred from finite distinguishability. This is
the precise correction to an unqualified F-9 necessity claim.

## Source references and remaining lamp

The kernel facts are classical; an accessible author-source derivation is
Philip Gressman's [Summability Methods](https://www2.math.upenn.edu/~gressman/analysis/08b-summability.html),
especially the kernel formula, positivity and unit integral. The analogous
primary course source is Casey Rodriguez's
[MIT 18.102, Lecture 16](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/resources/18102-sp21-lecture-16/).
All constants and model-specific inequalities in this file have direct proofs
above; the external references do not supply the original-zero arithmetic
estimate.

**Next verdict-changing probe:** bound the authentic real two-fiber contrasts
in CBO-B04 or the fixed signed pins in CBO-B05 with the marked zero seed and
the full original source history retained. Reject the `{2,4}` orbit,
`-pi/16`, and the existing p-integral wrong-seed shadows. A finite certificate
or a bounded source-transfer error cannot promote the missing all-epoch
estimate. No proof of pi parity balance or pi normality is claimed.
