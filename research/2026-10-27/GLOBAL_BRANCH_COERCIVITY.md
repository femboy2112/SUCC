# Whole-block branch coercivity and a stronger selected Fourier bound

**PAPER-PROVED, with exact finite instruments.** For the original zero-selected
BBP trajectory the eventual logarithmic absolute Fourier loss improves from
$1/29$ to $1/14$ per eligible geometric block. This changes the coefficient,
not the asymptotic order. The numerical onset is not computed. No relative
cancellation, spectral purity, or normality theorem is claimed.

The earlier two-transition inequality and inverse argument are credited to
[PR #311](https://github.com/femboy2112/SUCC/pull/311), source commit
`a34c4484059e667202b97d5ab4102560987b1406`, dossier
`research/2026-10-26/OILY_DIRECT_ARITHMETIC.md`. That branch is not imported
here. The new inequality uses a transition whose energy is small because it
belongs to a long block; this additional comparison improves the limiting
quadratic constant from $546$ to $257$. Academic priority is unverified.

## 1. The source-selected theorem

Keep exactly

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

There exists an integer $J_2\ge4$ such that, for every integer $N\ge1$ and
every integer $h\ne0$,

$$
\boxed{
\left|\sum_{n=1}^N e(hU_n)\right|
\le N-\frac1{14}\max\left(0,\lfloor\log_8N\rfloor-
\max\left(J_2,1+\lceil\log_{64}|h|\rceil\right)\right).
}
\tag{GB-1}
$$

In particular, each fixed nonzero frequency satisfies

$$|S_N^U(h)|\le N-\frac{\log_8N}{14}+O_h(1).\tag{GB-2}$$

The eventual leading coefficient improves by $29/14$ over the $1/29$ theorem.
The old and new onset constants are both unspecified, so a comparison at
every finite $N$ does not follow. The normalized upper bound still tends to
one. The theorem is substantially weaker than the cancellation needed for
normality.

## 2. A finite whole-block lemma

Let $T\ge2$, let real states and real forcing obey
$X_{t+1}=16X_t+r_{t+1}$ for $0\le t<T$, and let $h\ne0$ be an integer. Set

$$
D=(T+1)-\left|\sum_{t=0}^T e(hX_t)\right|,
\qquad R=|h|(\max_jr_j-\min_jr_j).
$$

Suppose $0\le R<1$ and a rational $u\ge0$ satisfies

$$
u^2T\ge2,
\qquad \frac{19(1-R)^2}{257(1+u)^2}>\frac1{14}.
\tag{GB-3}
$$

Then $D\le1/14$ implies that all lifted integer branches are equal.
Consequently some integer $p$ satisfies

$$
\boxed{
\left|X_0+\sum_{j=1}^T16^{-j}r_j-\frac p{15|h|}\right|
\le\frac{16/5+|h||r_T|}{15|h|16^T}.
}
\tag{GB-4}
$$

The arc is a necessary condition for extreme coherence, not a sufficient
condition. This finite lemma permits arbitrary real seeds and forcing. Its
application to the original zero seed is a separate argument below.

### Proof of the new inequality

Under $D\le1/14$ the resultant is nonzero. Choose its direction $e(\theta)$
and lifts $y_t=\theta+q_t=hX_t+\ell_t$ with $\ell_t\in\mathbb Z$ and
$q_t\in[-1/2,1/2]$. The resultant identity and the circle chord bound give

$$
D=\sum_t[1-\cos(2\pi q_t)],\qquad
8Q\le D,\qquad Q:=\sum_tq_t^2\le\frac1{112}.
\tag{GB-5}
$$

Thus each $q_t^2\le1/112$. Taylor's inequality gives

$$
1-\cos(2\pi q_t)
\ge\left[2\left(\frac{157}{50}\right)^2
-\frac23\left(\frac{22}{7}\right)^4\frac1{112}\right]q_t^2
\ge19q_t^2.
\tag{GB-6}
$$

The bracket minus $19$ equals $8725979/63026250>0$. The bounds
$157/50<\pi<22/7$ need no floating oracle: the classical Machin identity
$\pi=16\arctan(1/5)-4\arctan(1/239)$ and alternating arctangent bounds give

$$
\frac{281476}{89625}<\pi<\frac{670143059704}{213311234375}.
$$

The lower endpoint exceeds $157/50$ by $107/179250$; the upper endpoint is
below $22/7$ by $1845738322/1493178640625$. The local coefficient $19$ is
not asserted on the whole centered circle: $q=1/2$ falsifies that extension.

Put $a_t=q_{t+1}-16q_t$ and $d_t=a_t-hr_{t+1}$. The exact recurrence yields

$$d_t=15\theta+\ell_{t+1}-16\ell_t,$$

so every difference of branch residuals is an integer. The new observation
is the finite endpoint inequality

$$\sum_{t=0}^{T-1}(q_t^2+q_{t+1}^2)\le2Q.$$

Choose $t_*$ with $q_{t_*}^2+q_{t_*+1}^2\le2Q/T$. Since the squared norm
of $(-16,1)$ is $257$, Cauchy--Schwarz gives

$$|a_{t_*}|\le\sqrt{257Q}\sqrt{2/T},\qquad
|a_t|\le\sqrt{257Q}\quad\text{for every }t.$$

If the branches are not all equal, some $d_t$ differs from $d_{t_*}$ by a
nonzero integer. Keeping the forcing difference gives

$$
1-R\le|a_t-a_{t_*}|
\le\sqrt{257Q}(1+\sqrt{2/T})
\le\sqrt{257Q}(1+u).
$$

Together with $D\ge19Q$ this proves the quantitative implication

$$
\boxed{
D\le1/14\text{ and distinct branches}
\quad\Longrightarrow\quad
D\ge\frac{19(1-R)^2}{257(1+u)^2}.
}
\tag{GB-7}
$$

Condition (GB-3) rules out distinct branches. This is an additional bound
using the entire block, rather than an optimization of the earlier adjacent
coefficient $546$. The selected transition is justified by the finite
averaging inequality; it is not a circular good-step classification.

For the inverse conclusion, write the common branch as
$d_t=15\theta+k$ with $k\in\mathbb Z$, and set $f=-k/15$. Then

$$
y_{t+1}-f=16(y_t-f)+hr_{t+1},
\qquad
y_0-f+h\sum_{j=1}^T16^{-j}r_j=16^{-T}(y_T-f).
$$

The last transition also gives
$y_T-f=[16(q_T-q_{T-1})-hr_T]/15$.
Since $|q_t|\le1/\sqrt{112}<1/10$, its absolute value is at most
$(16/5+|h||r_T|)/15$. Divide by $h$ and absorb the integral lift of $y_0$
to obtain (GB-4), including negative $h$. QED.

### Fixed rational margins

For $T\ge20000$, take $u=1/100$. If $R\le15/4096$, then

$$
\frac{19(1-R)^2}{257(1+u)^2}-\frac1{14}
\ge\frac{9907077909}{19243046273024}>0.
\tag{GB-8}
$$

These constants are effective finite bounds. They do not compute the
arithmetic onset in the next section.

## 3. Authentic source exclusion and all-N assembly

The unchanged four-pole source and its actual Green tail satisfy

$$
0<r(n+1)<\frac{15}{64n^2},\qquad
0<T_n<\frac1{64n^2},\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
U_n+T_n=16^{n-1}\pi.
\tag{GB-9}
$$

These are inherited paper proofs, not new assumptions about cancellation;
see [the complete source derivation](../2026-10-25/BBP_DIOPHANTINE_COHERENCE.md).
The last equality uses precisely $U_0=0$.

Let $m\ge4096$ and $1\le|h|\le m^2/64$. On the states
$X_t=U_{m+1+t}$, $0\le t\le T:=7m-1$, the forcing is
$r_j=r(m+1+j)$. Its positive decreasing range satisfies

$$
R=|h|[r(m+2)-r(8m)]<\frac{15}{4096},\qquad T\ge20000.
$$

If this block had loss at most $1/14$, (GB-4) and the exact identity

$$
U_{m+1}+\sum_{j=1}^T16^{-j}r(m+1+j)
=16^{-T}U_{8m}=16^m\pi-16^{-T}T_{8m}
$$

would give a rational with denominator $q=15|h|16^m$ satisfying

$$
\left|\pi-\frac pq\right|
\le16^{-8m}16\left[
\frac{16}{75|h|}+\frac1{64(8m-1)^2}+\frac1{64(8m)^2}\right]
<4\,16^{-8m}.
\tag{GB-10}
$$

The coefficient is at most $3219739/940800<4$, already at $m=|h|=1$.
No large odd-conductor partial source sum remains in the approximation
center: it was cancelled by the exact full lifted Green identity.

**Classical arithmetic input.** Zeilberger and Zudilin prove
$\mu(\pi)\le7.103205334137\ldots<15/2$ in their corrected
[primary paper, arXiv:1912.06345v2](https://arxiv.org/abs/1912.06345v2),
published in *Moscow Journal of Combinatorics and Number Theory* **9** (2020),
407--419. We use no exponent-two claim for $\pi$.
Consequently some rational $C\in(0,1]$ obeys

$$|\pi-p/q|\ge Cq^{-15/2}\qquad(p\in\mathbb Z,\ q\ge1).$$

Irrationality absorbs the finitely many exceptional reduced denominators
into $C$; unreduced denominators then satisfy the same inequality. The
constant is not extracted numerically. The upper bound (GB-10) is impossible
when

$$C^2 16^m>16(15|h|)^{15}.\tag{GB-11}$$

The factor $16$ is the square of the approximation coefficient bound $4$.
Since $16^m/m^{30}\to\infty$, one integer $m_2\ge4096$ makes (GB-11)
hold for every $m\ge m_2$ and every $1\le|h|\le m^2/64$. For example,
it suffices that $C^2 16^{m_2}>16(15m_2^2)^{15}$: the ratio
$16^m/m^{30}$ is increasing for $m\ge64$, since Bernoulli's inequality
gives $(m/(m+1))^{30}\ge1-30/(m+1)>1/16$ there.

We have proved the uniform selected block bound

$$
\boxed{
\left|\sum_{n=m+1}^{8m}e(hU_n)\right|<7m-\frac1{14}
\quad(m\ge m_2,\ 1\le|h|\le m^2/64).
}
\tag{GB-12}
$$

Set $J_2=\lceil\log_8m_2\rceil$. Complete disjoint blocks
$(8^j,8^{j+1}]$ inside $[1,N]$ have $j<\lfloor\log_8N\rfloor$.
They satisfy the uniform frequency band exactly when
$j\ge1+\lceil\log_{64}|h|\rceil$. Apply (GB-12) on eligible blocks and
the trivial estimate to the rest; the triangle inequality proves (GB-1).
This includes every $N\ge1$ and the case of zero eligible blocks.

For a prescribed maximum mode $H-1\ge1$, use the same block count with
$|h|=H-1$ to control all $0<|h|<H$. The exact Fourier Gram identity yields
only

$$\frac{D_{N,H}}H\le(H-1)\left(1-\frac{K_2(N,H)}{14N}\right)^2.$$

This remains of order $H$. No predetermined growing frequency schedule is
proved spectrally pure, and no equivalence is presented as an arithmetic saving.

## 4. Adversarial controls and the method's finite ceiling

**A universal threshold cannot exceed a boundary excursion.** With zero
forcing, take $X_0=1/16$ and $X_t=16^{t-1}$ for $t\ge1$. Its phases are
$1/16,0,\ldots,0$, and the lifted branches are not constant. Its loss is

$$
D_T=T+1-\sqrt{T^2+2T\cos(\pi/8)+1}
\longrightarrow1-\cos(\pi/8).
\tag{GB-13}
$$

The limit is about $0.07612$, between $1/14$ and $1/13$. Thus a generic
long-block constant-branch lemma cannot use any threshold strictly greater
than $1-\cos(\pi/8)$. This is an upper obstruction to the optimal threshold,
not a proof that this value is attainable by a universal lemma. Observations
before the block are absent: adding a backward geometric tail and charging
its action would impose an extra, unauthorized boundary condition.

**The same obstruction retains the entire BBP forcing.** For each $m$ choose
the changed real initial value
$V_0=16^{-m-2}-\pi/16$. Then

$$V_n=16^{n-m-2}-T_n$$

satisfies the original forcing at every time. On $(m,8m]$ its first phase
approaches $1/16$ and all subsequent phases approach zero. The sum of phase
errors relative to the preceding boundary control is at most

$$2\pi\sum_{n=m+1}^{8m}T_n<\frac{11m}{16(m+1)^2}\to0.$$

Hence its block loss has the same limit (GB-13). For all sufficiently large
$m$, the centered lifts have first branch residual $15\theta-1$ and all
later residuals $15\theta$. The branches remain distinct. This family uses
one changed seed per block; it is not the zero-selected rational trajectory
and is not advertised as preserving the original finite odd conductors.

**Fixed same-forcing coherent control.** The single seed $V_0=-\pi/16$
gives $V_n=-T_n$, so every fixed-mode Fourier mean tends to one. Its loss on
$(m,8m]$ is at most
$121m h^2/[3584(m+1)^4]$, which tends to zero for fixed $h$. It is allowed
by the generic inverse arcs. It defeats an extension of (GB-12) to arbitrary
seeds because the zero-selected Green identity (GB-9) then changes.

**Why the logarithmic order has not improved.** The inherited sparse
same-forcing controls have finite irrationality type and only logarithmic
absolute loss. They rule out deriving a superlogarithmic loss merely from
the forcing law plus generic finite irrationality type; see the precise
[changed-seed controls](../2026-10-26/SELECTED_BRANCH_ANALYTIC.md). They do
not refute a stronger theorem using genuinely new arithmetic of the zero
selector. Neither this proof nor the changed-seed obstruction supplies it.

Additional finite falsifiers retain the exceptional hypotheses: too short
a block invalidates $u^2T\ge2$; an enlarged forcing range can destroy the
strict margin; a nonintegral residual mutation breaks the branch identity;
$q=1/2$ breaks the illicit global coefficient $19$; and removing factor
$16$ changes the Diophantine comparison on an exact rational fixture.

## 5. Instruments, authority, and the exact remaining statement

The native module
[`global_branch_coercivity.py`](../../observational_succ/global_branch_coercivity.py)
uses only exact integers and `Fraction`. Its original-forcing adapter checks
the literal four poles at large source scales without constructing enormous
rational states. It explicitly does not authenticate an arbitrary initial
value. The generic inverse certificate retains the ordered forcing and the
full rational initial state. Arc membership is never mistaken for coherence.
The combinatorial all-$N$ budget explicitly reports that its supplied onset
is not numerically certified.

The focused command
`python -m unittest tests.test_global_branch_coercivity -v` passed **11 tests**
in 1.098 seconds. The tests independently reconstruct source ranges,
Machin sums, the backward telescope, the block count, a nonconstant-branch
witness, and a rational enclosure of the boundary obstruction. No floating
Fourier sum is promoted to proof authority. The principal records the
combined-tree required gates and any separately checked Lean declarations.

Authority labels:

- **CLASSICAL:** Machin's identity, the chord and Taylor bounds, and the
  published irrationality measure of $\pi$.
- **PAPER-PROVED:** (GB-1)--(GB-13), with the domains and conditional finite
  hypotheses stated above.
- **EXACT FINITE:** rational margins, literal source parameter holdouts,
  inverse-arc computations, and adversarial fixtures.
- **CONDITIONAL:** a numerical onset supplied to the executable budget;
  no value of the global Diophantine constant $C$ is certified here.
- **REFUTED:** an arbitrary-seed version of the selected block theorem,
  a global coefficient $19$ on the circle, and a universal constant-branch
  threshold exceeding $1-\cos(\pi/8)$.
- **OPEN:** any superlogarithmic selected absolute loss, relative fixed-mode
  cancellation, spectral purity, and base-16 normality of $\pi$.

The next statement must extract a growing amount of signed loss within a
single growing block, or combine block phases with a quantitative signed
bound. The present argument excludes one constant-branch configuration per
eligible geometric scale. Paying at most one bounded excursion per scale
cannot itself improve the logarithmic order. A theorem using the density
or arrangement of authentic integer branch events must retain the selected
zero anchor and supply new arithmetic beyond the finite irrationality input.
