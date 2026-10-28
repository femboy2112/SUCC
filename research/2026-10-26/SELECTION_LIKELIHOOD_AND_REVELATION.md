# Selection likelihood, reverse revelation, and adaptive phase feedback

**Research round:** 2026-10-26. **Baseline:** PR #313 at
`79344c62c39c96755b742700b3d4d22fa60d86da`.
**Authority:** CLASSICAL finite probability and operator theory, with
PAPER-PROVED applications and EXACT FINITE implementation checks.
**Selected Weyl cancellation and pi normality remain OPEN.**

The useful inverse of an average must retain the information that the
average erased. For a declared reference law and a selected law, the
missing signed expectation is exactly a pairing between their likelihood
innovations and the observable's innovations. On a uniform radix inverse
fiber, a Fourier character has just one nonzero innovation, at an
explicit reverse-revelation level. Selection restores the character
there; its probability cost alone says nothing about normality.

Two further boundaries are quantitative. The odd-torsion inverse
character has optimal uniform continuous-approximation error one, except
at the frequencies that descend through multiplication by sixteen.
Adaptive local phase losses also need not multiply: an exact positive
two-state model retains a unit twisted eigenvalue while every local
conditional phase mean has modulus one half. A finite reconvergence
criterion identifies the extra signed path information that can prove
operator contraction in a declared stochastic model.

## 1. Provenance, objects, and authority

The following constructions are inherited, rather than rediscovered:

- [Seinfeld SS-01/02 and SS-05/06](../2026-10-25/SEINFELD_SUCC_NOTHING_THEOREMS.md)
  retain formal recurrence relations, the initial selector, the unique
  odd-torsion inverse, and its discontinuity.
- [PR313's operator dossier](SELECTED_BRANCH_OPERATOR.md) gives the
  quantitative conditional-resolution obstruction and constructs every
  inverse label near every real tail. Its exact-conditioning energy-one
  theorem is not a new result here.
- [Source-faithful bidirectional histories](../2026-10-22/SOURCE_FAITHFUL_BIDIRECTIONAL_HISTORIES.md)
  and [the native module](../../observational_succ/bidirectional_source_histories.py)
  already implement labelled path laws, Bayes reversal, and terminal-event
  Doob conditioning.
- [The existing likelihood module](../../observational_succ/heuristic_evidence_martingales.py)
  already uses classical likelihood martingales. General information
  chain rules also belong to the existing
  [entropy transport module](../../observational_succ/entropy_transport.py).

The implementation added in
[path_likelihood.py](../../observational_succ/path_likelihood.py) supplies
exact signed innovation certificates, compact radix-resolution
certificates, authenticated BBP windows, and the controls below. Rational
real observables are certified directly; the complex identity holds
componentwise. The compact Fourier certificate stores a unit phase as an
exact rational argument, and a vanishing conditional expectation as a
distinct value. It does not approximate transcendental values by floats.

The general probability and spectral facts are classical. The explicit
source interface, revelation-order accounting, and finite witnesses are
the project contribution; no scholarly-priority claim is made. The
proofs provide the universal quantifiers. Finite checks calibrate the
implementations and reject false variants. Same-model delegated review
is not external mathematical peer review.

## 2. The signed cost of changing a path law

Let $\Omega$ be finite, let $P,Q$ be probability laws with $Q\ll P$,
and let $\mathcal F_0\subseteq\cdots\subseteq\mathcal F_d$ be a
filtration. Assume the likelihood $R=dQ/dP$ and the complex observable
$F$ are $\mathcal F_d$-measurable. Ignore points of zero $P$ mass.
Define

$$R_t=\mathbb E_P[R\mid\mathcal F_t],\qquad
M_t=\mathbb E_P[F\mid\mathcal F_t],\qquad
\Delta R_t=R_t-R_{t-1},\quad\Delta M_t=M_t-M_{t-1}.$$

### Theorem SL-1: selection and observable innovations

For every such finite law,

$$\boxed{\mathbb E_QF-\mathbb E_PF
=\mathbb E_P[(R_0-1)M_0]
+\sum_{t=1}^d\mathbb E_P[\Delta R_t\,\Delta M_t].}$$

If the initial sigma-field is trivial, or the two laws have the same
restriction to it, then $R_0=1$ and the initial term vanishes. The product
in the displayed formula is **bilinear**: there is no complex conjugation
on the observable increment.

**Proof.** Write

$$\mathbb E_QF-\mathbb E_PF=\mathbb E_P[(R_d-1)F]$$

and expand $R_d-1=(R_0-1)+\sum_{t=1}^d\Delta R_t$. Conditioning
the initial term on $\mathcal F_0$ replaces $F$ by $M_0$.
Conditioning the $t$th term on $\mathcal F_t$ replaces $F$ by $M_t$.
Finally,

$$\mathbb E_P[\Delta R_tM_{t-1}]
=\mathbb E_P[M_{t-1}\mathbb E_P(\Delta R_t\mid\mathcal F_{t-1})]=0.$$

Subtracting this zero term gives the formula. All sums are finite.

For a trivial initial sigma-field, martingale orthogonality gives

$$\sum_{t=1}^d\mathbb E_P|\Delta R_t|^2=\chi^2(Q\Vert P),
\qquad
\sum_{t=1}^d\mathbb E_P|\Delta M_t|^2=\operatorname{Var}_P(F).$$

Consequently,

$$|\mathbb E_QF-\mathbb E_PF|
\le\sum_{t=1}^d
\sqrt{\mathbb E_P|\Delta R_t|^2\,
      \mathbb E_P|\Delta M_t|^2}
\le\sqrt{\chi^2(Q\Vert P)\operatorname{Var}_P(F)}.$$

This is a sensitivity bound, not a signed saving. For selection of an
atom $\omega$ with reference probability $p>0$, it becomes

$$|F(\omega)-\mathbb E_PF|^2
\le(1/p-1)\operatorname{Var}_P(F).$$

The coefficient is sharp: equality holds for a nonconstant observable
that is constant off $\omega$.

### Why the signed pairing must be retained

On the four equally likely words $00,01,10,11$, select $00$ and assign
observable values $(0,2,-1,-1)$. Reveal the first letter, then the second.
The two signed pairings in SL-1 are $1$ and $-1$. Their sum is zero,
as are both the selected expectation and the reference expectation.
The observable increment energies are positive. Replacing $F$ by $-F$
reverses the pairings while leaving those energies unchanged.

Thus positive innovation energies alone do not reconstruct the missing
selected expectation. The implementation preserves both kinds of data.
The reference laws at different levels must also be restrictions of one
law: unrelated normalized likelihood tables do not automatically form
the martingale used in SL-1.

## 3. A radix character becomes visible at exactly one reverse revelation

Fix integers $b\ge2$, $d\ge1$, an arbitrary real offset $a$, and an
integer frequency $h$. Let $J$ be uniform on $\{0,\ldots,b^d-1\}$ and
put

$$X_J=\frac{a+J}{b^d}\pmod1,\qquad F(J)=e(hX_J),\qquad
e(s)=\exp(2\pi i s).$$

Reveal the low radix digits first:

$$J_t=J\bmod b^t,\qquad\mathcal F_t=\sigma(J_t),\qquad0\le t\le d.$$

### Theorem SL-2: exact conditional character and visibility level

At every level,

$$\boxed{M_t=\mathbb E[F\mid\mathcal F_t]
=\mathbf1_{\{b^{d-t}\mid h\}}
e\!\left(\frac{h(a+J_t)}{b^d}\right).}$$

**Proof.** Given $J_t$, write $J=J_t+b^tL$, where $L$ is uniform on
$\{0,\ldots,b^{d-t}-1\}$. The conditional expectation is the stated
phase times

$$\frac1{b^{d-t}}\sum_{L=0}^{b^{d-t}-1}e\!\left(\frac{hL}{b^{d-t}}\right).$$

This finite geometric sum is one if $b^{d-t}$ divides $h$, and zero
otherwise. Integer $h$ makes the choice of circle representative irrelevant.

If $h=0$, then $F=1$ and every innovation vanishes. More generally, if
$b^d\mid h$, then $F$ is constant on this fiber: every $M_t=F$ and
selection changes none of its values.

Otherwise, define

$$v_b(h)=\max\{q\ge0:b^q\mid h\}<d,\qquad t_*=d-v_b(h).$$

For negative $h$, divisibility refers equivalently to $|h|$. When $b$
is composite this notation denotes the stated radix divisibility order,
not a prime valuation. Then

$$M_t=0\quad(t<t_*),\qquad M_t=F\quad(t\ge t_*).$$

There is exactly one nonzero observable innovation:

$$\boxed{\Delta M_{t_*}=F,\qquad
\mathbb E|\Delta M_{t_*}|^2=1,\qquad
\Delta M_t=0\ (t\ne t_*).}$$

Depth zero is the separate singleton case: $J=0$, $X=a\pmod1$, and
there are no innovations at any frequency.

### Selection cost and its exact location

Fix $j_*\in\{0,\ldots,b^d-1\}$ and let $Q=\delta_{j_*}$.
The prefix likelihood is

$$R_t=b^t\mathbf1_{\{J\bmod b^t=j_*\bmod b^t\}}.$$

Direct finite summation gives

$$\mathbb E R_t^2=b^t,\qquad
\mathbb E|\Delta R_t|^2=(b-1)b^{t-1},\qquad
\chi^2(Q_t\Vert P_t)=b^t-1,$$

$$D(Q_t\Vert P_t)=t\log b.$$

The entropy uses the natural logarithm. These costs are identical for
every selected word. They distinguish selection from averaging, not a
normal word from a periodic word.

When $b^d\nmid h$, the exact signed pairing is

$$\boxed{\mathbb E[\Delta R_t\Delta M_t]
=\begin{cases}F(j_*),&t=t_*,\\0,&t\ne t_*.
\end{cases}}$$

Indeed $F$ is constant on the selected $t_*$ cylinder, so
$\mathbb E[R_{t_*}F]=F(j_*)$. The preceding conditional expectation
vanishes, hence $\mathbb E[R_{t_*-1}F]=0$. All other observable
increments are zero. The complete selected unit character is restored
at that one revelation. At constant-fiber frequencies, every pairing
is zero and the reference character already equals the selected one.

## 4. Forced backward paths and three distinct digit conventions

Fix a prescribed forcing schedule and terminal point:

$$x_i=bx_{i-1}+f_i\pmod1\quad(1\le i\le d),\qquad x_d=y.$$

Write

$$A_s=\sum_{i=1}^s b^{s-i}f_i,\qquad a=y-A_d.$$

The initial inverse fiber is exactly $X_J=(a+J)/b^d\pmod1$.
After $d-t$ forward steps, the state issued from $X_J$ is

$$x_{d-t}=\frac{a+J}{b^t}+A_{d-t}\pmod1.$$

This state depends only on $J\bmod b^t$, and different residues give
different states. Its subsequent forward segment determines all the
$t$ states already traversed backward from $y$. Therefore the first
$t$ backward choices generate precisely $\mathcal F_t$ from SL-2.
This proves the filtration identification for arbitrary prescribed
forcing, without assuming a convenient digit-label convention.

With unwrapped inverse lifts

$$u_{i-1}=\frac{u_i-f_i+\varepsilon_i}{b},\qquad
0\le\varepsilon_i<b,$$

the backward choices $\varepsilon_d,\varepsilon_{d-1},\ldots$ construct

$$J=\varepsilon_d+b\varepsilon_{d-1}+\cdots+b^{d-1}\varepsilon_1.$$

Reducing intermediate states to $[0,1)$ can cyclically relabel later
choices. Separately, canonicalizing the common offset also changes the
fiber index: if $a=m+\tau$ with $m=\lfloor a\rfloor$ and
$0\le\tau<1$, then

$$J'=(J+m)\bmod b^d,\qquad
X_J=\frac{\tau+J'}{b^d}\pmod1.$$

The low-prefix partitions are unchanged under this fixed relabeling.
The compact native certificate uses the canonical $\tau,J'$ convention.
None of these observations licenses equality of the different digit strings.

### An authentic first-step convention control

The original first forcing is $r(1)=47/15$, and the zero-seed terminal
circle state is $2/15$. Refine one multiplication-by-sixteen step into
four doublings, putting this forcing on the last microstep and zero on
the other three. With the reduced terminal representative,

$$a=2/15-47/15=-3.$$

The selected initial state zero has raw fiber index $J=3$. Its raw
low-first bits are $(1,1,0,0)$. If every intermediate inverse state is
reduced immediately to $[0,1)$, the literal backward labels are instead
$(1,0,0,0)$: the first inverse lift is

$$\frac{2/15-47/15+1}{2}=-1\equiv0\pmod1,$$

and the next three choices are zero. Canonicalizing $a$ gives
$\tau=0,J'=0$. All three descriptions yield the same selected state and
the same revelation filtration. Their labels carry different conventions.

For $k$ BBP macrosteps, the direct certificate uses $b=16,d=k$.
A declared binary refinement uses $b=2,d=4k$. For a nonconstant fiber
character its binary visibility level is

$$t_*=4k-v_2(h),$$

and the containing macrostep is
$\lceil t_*/4\rceil=k-\lfloor v_2(h)/4\rfloor$.
At binary depth eight, frequencies $1,2,4,8,16,24,128,-8$ become visible
at levels $8,7,6,5,4,5,1,5$, respectively. Frequencies zero and 256 are
constant on that fiber.

The authenticated wrapper retains all four original forcing poles,
unwrapped states, source indices, and the zero anchor. The uniform law
on the other inverse points is a declared comparison law; it is not the
empirical distribution of alternative BBP histories.

## 5. Infinite selection requires a separately consistent reference law

There is a precise infinite symbolic statement, but it must not be
silently attached to horizon-dependent inverse boundaries.

Fix once and for all the product space
$\{0,\ldots,b-1\}^{\mathbb N}$ with independent uniform coordinates,
and fix one infinite word $w$. Let $C_t$ be its length-$t$ cylinder.
Then

$$P(C_t)=b^{-t},\qquad R_t=b^t\mathbf1_{C_t},\qquad\mathbb E_PR_t=1.$$

The decreasing intersection is the singleton $\{w\}$, of probability
zero. Almost every reference word eventually leaves these cylinders,
so $R_t\to0$ almost surely. The martingale is not uniformly integrable:
otherwise its limit would retain expectation one. The infinite point
law $\delta_w$ is singular relative to $P$, although every finite
prefix law is absolutely continuous and has the finite costs above.

This conclusion is independent of which word was fixed. It supplies no
normality information. Moreover, uniform inverse-fiber laws anchored at
different authentic terminal states need not project to one another.
The existence of each finite law does not establish the consistent
infinite product model just used. SL-1 and SL-2 are valid separately at
each finite horizon without making that additional identification.

## 6. A sharp continuous-approximation barrier for the odd selector

Let $D_{\mathrm{odd}}\subset\mathbb Q/\mathbb Z$ be the odd-denominator
subgroup, and let $S$ be its inherited inverse to multiplication by
sixteen. For $t=a/q\in[0,1)$ with $q$ odd, one may use any common
odd-denominator presentation:

$$j(t)\equiv-aq^{-1}\pmod{16},\quad0\le j(t)<16,
\qquad S(t)=\frac{j(t)+t}{16}.$$

Define $g_h(t)=e(hS(t))$ for an integer $h$.

### Theorem SL-3: optimal uniform error

If $16\nmid h$, then

$$\boxed{\inf_{f\in C(\mathbb T;\mathbb C)}
\sup_{t\in D_{\mathrm{odd}}}|g_h(t)-f(t)|=1.}$$

For an $L$-Lipschitz candidate with respect to circle distance, the
following sixteen explicit witnesses give a finite lower bound. Choose
an integer $m\ge1$, let $Q=16m+1$, and set

$$t_j=\frac{16-j}{Q},\qquad0\le j<16.$$

Then

$$\boxed{\max_j|g_h(t_j)-f(t_j)|
\ge1-\frac{2\pi|h|+16L}{Q}
\ge1-\frac{(44/7)|h|+16L}{Q}.}$$

One may replace a negative lower bound by zero.

**Proof.** The common-denominator congruence gives $j(t_j)=j$, even
when a fraction reduces. Put $\zeta=e(1/16)$. Since
$S(t_j)=(j+t_j)/16$,

$$|g_h(t_j)-\zeta^{hj}|
\le\frac{2\pi|h|}{Q}.$$

Because $16\nmid h$, the sixteen roots have zero average. Thus for
every $c\in\mathbb C$,

$$\frac1{16}\sum_{j=0}^{15}|\zeta^{hj}-c|^2=1+|c|^2.$$

Take $c=f(0)$ and use continuity as $m\to\infty$. The maximum error
is at least one, while $f=0$ attains one. In the Lipschitz case,
$|f(t_j)-f(0)|\le16L/Q$ gives the stated finite bound. The rational
version uses $\pi<22/7$.

PR313's every-label-near-every-tail construction strengthens the result.
At every $t_0$, the cluster values include
$e(h(j+t_0)/16)$ for all sixteen labels. Applying the same mean-square
identity at a point where $|f|$ is maximal gives

$$\sup_{D_{\mathrm{odd}}}|g_h-f|
\ge\sqrt{1+\|f\|_\infty^2}.$$

In particular, zero is the **unique** optimal continuous approximant.
The exception is exact: if $h=16k$, then

$$g_h(t)=e(kt),$$

so the best continuous-approximation error is zero.

**Source boundary.** These are uniform statements on the whole
odd-denominator carrier. The witnesses need not occur along the
particular zero-selected BBP orbit. The theorem does not exclude a
source-specific averaged, weak, or restricted-orbit transport estimate.
It rules out a uniformly accurate continuous replacement of this entire
arithmetic selector character at the non-descending frequencies.

## 7. Adaptive local losses do not automatically multiply

Let $X_0=1$. For $n\ge1$, let $X_n$ be independent signs with
$P(X_n=1)=p$, where $0<p<1$, and write $\beta=2p-1$. Define

$$Z_n=X_{n-1}X_n,\qquad
\mathcal F_n=\sigma(X_1,\ldots,X_n).$$

Then

$$\mathbb E[Z_n\mid\mathcal F_{n-1}]=\beta X_{n-1},
\qquad
|\mathbb E[Z_n\mid\mathcal F_{n-1}]|=|\beta|.$$

Nevertheless,

$$\prod_{t=1}^nZ_t=X_n,\qquad
\mathbb E\prod_{t=1}^nZ_t=\beta.$$

For $p\ne1/2$ and $n\ge2$, the actual modulus $|\beta|$ strictly
exceeds the proposed product $|\beta|^n$. At horizon one, or at the
fair value $p=1/2$, those moduli agree. The executable receipt therefore
distinguishes the false universal bound from whether a particular input
is a strict counterexample.

In state order $(1,-1)$, the reference and twisted matrices are

$$P=\begin{pmatrix}p&1-p\\p&1-p\end{pmatrix},\qquad
T=\begin{pmatrix}p&p-1\\-p&1-p\end{pmatrix}.$$

All reference transition probabilities are positive, and the reference
chain mixes in one step. Yet $T^2=T$ and $T(1,-1)^T=(1,-1)^T$.
At $p=3/4$, $T\mathbf1=(1/2,-1/2)^T$ and the product expectation is
$1/2$ at every positive horizon.

This is a coboundary phase: $Z_n=\phi(X_n)/\phi(X_{n-1})$ with
$\phi(x)=x$. The phase product telescopes to its endpoints.
The unit eigenvalue obstructs uniform operator-power contraction.
It does **not** prohibit every observable from cancelling. In particular,
the fair case has expectation zero from the first step despite the
same unit eigenvalue.

### The exact feedback covariance

For any adapted unit phases $Z_n$, set

$$W_n=\prod_{t=1}^nZ_t,\qquad
\kappa_n=\mathbb E[Z_n\mid\mathcal F_{n-1}],\qquad
\mu_n=\mathbb EW_n,\quad\overline\kappa_n=\mathbb E\kappa_n.$$

Conditioning gives the exact recursion

$$\boxed{\mu_n=\overline\kappa_n\mu_{n-1}+c_n,\qquad
c_n=\mathbb E[(W_{n-1}-\mu_{n-1})
              (\kappa_n-\overline\kappa_n)].}$$

This covariance is bilinear. Iteration yields

$$\mu_N=\mu_0\prod_{n=1}^N\overline\kappa_n
+\sum_{j=1}^Nc_j\prod_{n=j+1}^N\overline\kappa_n.$$

Its magnitude has the legitimate bound

$$|c_n|\le
\sqrt{(1-|\mu_{n-1}|^2)
      \mathbb E|\kappa_n-\overline\kappa_n|^2}.$$

In the $p=3/4$ counterexample, for every $n\ge2$,
$\overline\kappa_n=1/4$ and $c_n=3/8$. Thus
$\mu_n=(1/4)(1/2)+3/8=1/2$. The feedback covariance is exactly the
term that the false multiplicative argument discarded.

For one consistently declared infinite process, a sufficient repair is
$|\overline\kappa_n|\le\rho<1$ and $c_n\to0$. The convolution formula
then proves $\mu_N\to0$: an old finite prefix is geometrically damped,
and the remaining contribution is bounded by a vanishing supremum of
$|c_n|$ times $1/(1-\rho)$. This is a statement about that ensemble
phase product. It is not a transport theorem to the selected arithmetic
Weyl average.

## 8. What a finite twisted-kernel contraction really requires

Let $V$ be a finite state set with a finite set of distinct labelled channels
$(x,\ell,y)$ with probabilities $p(x,\ell,y)>0$, whose sum over outgoing
channels is one at every $x$. Assume the underlying directed state
graph is irreducible. Assign a unit phase $g(x,\ell,y)$ to each
supported channel, retaining parallel labels. Define

$$T_gf(x)=\sum_{\ell,y}p(x,\ell,y)g(x,\ell,y)f(y).$$

### Theorem SL-4: the unit spectral-radius case

The spectral radius satisfies $\rho(T_g)\le1$. Equality holds exactly
when there exist $|\lambda|=1$ and a unit-valued function $z$ on $V$
such that, on every supported channel,

$$\boxed{g(x,\ell,y)=\lambda\frac{z(x)}{z(y)}.}$$

**Proof.** The row triangle inequality gives
$\|T_g\|_{\infty\to\infty}\le1$. If the spectral radius is one,
the finite matrix has an eigenvalue $\lambda$ of modulus one. Choose a
nonzero eigenvector and a state where its modulus is maximal. Equality
in the triangle inequality forces every positive-probability successor
to have the same maximal modulus, and every supported summand to have
phase $\lambda z(x)$. Irreducibility propagates this equality to all
states. Rescale the common modulus to one; the channel identity follows.
Conversely, that identity gives $T_gz=\lambda z$.

For the coboundary $g(x,\ell,y)=\phi(y)/\phi(x)$, this says

$$T_g=D_\phi^{-1}PD_\phi,$$

where $P$ is the reference transition matrix. Path products telescope,
and the twisted operator retains a unit eigenvalue. This obstructs a
uniform bound $\|T_g^n\|\to0$. Individual matrix coefficients may
still decay or vanish if their observables do not see the surviving
eigenspace; the fair sign control demonstrates that distinction.

### A quantitative reconvergence certificate

Suppose there are an integer $m\ge1$ and constants $\varepsilon>0$,
$\delta>0$ such that from **every** starting state two distinct
length-$m$ labelled paths reach the same endpoint. Assume each path
has probability at least $\varepsilon$, and their accumulated phases
$\alpha,\beta$ satisfy

$$1-\operatorname{Re}(\alpha\overline\beta)\ge\delta.$$

Then

$$\boxed{\|T_g^m\|_{\infty\to\infty}
\le1-\varepsilon\delta/2<1.}$$

To prove it, let $a,b$ be the two path probabilities. Their contribution
at the shared endpoint loses at least

$$a+b-|a\alpha+b\beta|
=\frac{2ab(1-\operatorname{Re}(\alpha\overline\beta))}
       {a+b+|a\alpha+b\beta|}
\ge\frac{ab\delta}{a+b}\ge\frac{\varepsilon\delta}{2}.$$

All remaining contributions are bounded by their probability masses,
which together with $a+b$ sum to one. This bounds every absolute row sum
of $T_g^m$. Submultiplicativity then gives

$$\|T_g^n\|_{\infty\to\infty}
\le(1-\varepsilon\delta/2)^{\lfloor n/m\rfloor}.$$

There is a useful finite irreducible corollary. Suppose just **one**
pair of length-$r$ paths reconverges with phase gap $\delta>0$.
Let $s=|V|$ and let $p_{\min}>0$ be the smallest supported channel
probability. From each state choose a path of length at most $s-1$
to the pair's starting state. Prepend this common prefix to both paths,
then append the same arbitrary supported suffix to equalize their
total lengths at $m=r+s-1$. Such a suffix exists because each state
has an outgoing supported channel. The two paths still reconverge and
retain the phase gap, and each has probability at least $p_{\min}^m$.
Hence

$$\boxed{\|T_g^m\|_{\infty\to\infty}
\le1-\frac{\delta p_{\min}^m}{2}.}$$

This gives a concrete finite falsification test for a proposed phase
mechanism. Equal endpoints alone do not suffice: the transported phases
must differ. Coboundary phases give identical products on equal-length
paths with the same endpoints, so they fail the test.

**Arithmetic boundary.** These theorems concern a declared finite
stochastic kernel and a declared path-product observable. They do not
identify that product with a selected BBP character or a time average.
The authentic odd-conductor step is a deterministic permutation, and
hidden labels preserving the same arithmetic phase do not create the
required phase-separated reconvergence. Changing the state space,
kernel, source time, or horizon would additionally require uniform
control of the constants. A generic spectral-radius condition is not
the remaining pi theorem; source-authenticated signed transport is.

## 9. Reproduction, discriminating controls, and the remaining gate

The standalone
[revelation oracle](seinfeld_revelation_oracle.py) imports only the
Python standard library, not production modules or tests. Its
[raw JSON receipt](seinfeld_revelation_oracle.json) pins its source
hash and records:

| Exact finite check | Count |
|---|---:|
| Conditional root sums | 15,390 |
| Selected likelihood–observable covariance increments | 1,722 |
| Likelihood increment means and squared norms | 1,722 |
| Forced backward-filtration comparisons | 880 |
| Coboundary matrix identities | 2 |
| Complete biased-sign paths | 126 |

The root calculations use polynomial reduction in
$\mathbb Q[X]/(X^{N/2}+1)$ for the declared power-of-two fiber sizes.
The forcing tests use exact rational state trajectories, including the
first-step convention control above. Sign paths are enumerated through
depth six. Receipt generation and replay, including replay from an
external working directory, exited successfully. These are finite
checks of the paper statements, not proofs by extrapolation.

Reproduce the independent oracle and the assembled native receipt with:

```sh
python research/2026-10-26/seinfeld_revelation_oracle.py --verify research/2026-10-26/seinfeld_revelation_oracle.json
python scripts/seinfeld_realization_probe.py --verify
```

The native integration tests are in
[test_path_likelihood.py](../../tests/test_path_likelihood.py).
The assembled round's results and validation are summarized in
[Seinfeld inverse averaging and realization](SEINFELD_INVERSE_AVERAGING_AND_REALIZATION.md).
This dossier does not pre-claim hosted CI or new Lean authority.

The required controls are substantive: reverse the revelation order;
test a frequency divisible by the entire fiber conductor; change the
sign of an observable while preserving its positive energies; erase the
initial likelihood term when initial laws differ; identify raw digits
with literal reduced-state labels; use the fair coboundary case to
reject an assertion that a unit eigenvalue prohibits every observable
cancellation; or replace a selected arithmetic phase by a uniform
inverse average. Each changes a mathematically specified part of the
claim and has an explicit discriminator above.

The surviving next obligation is a signed estimate for the authentic
source and selector, with a proved transport identity and a controlled
residual. SL-1 identifies the missing signed pairing; SL-2 locates it
inside a finite inverse fiber; SL-3 limits a uniform smooth replacement;
and SL-4 tests one possible stochastic contraction mechanism on its
own declared domain. None of these steps proves that the corresponding
selected arithmetic time averages are small.
