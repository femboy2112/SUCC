# Spectral purity: simultaneous prefix, jet, positivity and odd-conductor obstruction

**Authority:** PAPER-PROVED, with EXACT FINITE rational witnesses. No Lean
authority is claimed here. The authentic BBP source is not changed by this
module: the construction is explicitly a family of changed-source controls.
Base-16 normality of pi remains OPEN.

The inherited [Green dossier, G9](../2026-10-24/PI_SOURCE_GENESIS_GREEN.md)
already gives positive rational controls matching any finite endpoint jet.
The [non-coboundary dossier](../2026-10-24/PI_SOURCE_GENESIS_NONCOBOUNDARY.md)
additionally preserves a nonzero pole-coboundary invariant. The new result
below is a different, simultaneous strengthening: **any prescribed exact
authentic source prefix, arbitrary finite endpoint jets, globally odd
denominators, and all strict positive moment inequalities** coexist with a
nonnormal selected orbit. It does not also preserve the non-coboundary
invariant; its rational Green tail makes that distinction explicit.

## 1. Statement and source passport

Keep the authentic four-pole source $r(n)$, $U_0=0$ and
$U_{n+1}=16U_n+r(n+1)$. Set

$$
P(t)=4-2t^3-t^4-t^5,
\qquad F(t)=\frac{P(t)}{16-t^8},
\qquad T_n=\int_0^1t^{8n}F(t)\,dt.
$$

Thus $T_0=\pi/16$, $r(n+1)=\int_0^1t^{8n}P(t)\,dt$, and
$U_n=16^nT_0-T_n$ by the already proved Green identity.

**Theorem SP-M1.** For every pair of fixed integers $M\geq0$, $K\geq1$,
there is an explicitly constructible even polynomial $R\in\mathbb Q[t^2]$
and a single fixed changed source

$$
T_n^*=\int_0^1t^{8n}R(t)\,dt,
\quad r^*(n+1)=16T_n^*-T_{n+1}^*,
\quad U_n^*=16^n\beta-T_n^*,\quad \beta=T_0^*,
$$

with all of the following properties simultaneously:

1. $R(t)>0$ for $0\leq t<1$, $R(1)=0$, and $\beta$ is rational with odd
   denominator. Every $T_n^*$, $r^*(n+1)$ and $U_n^*$ has odd denominator.
2. $U_0^*=0$, $r^*(j)=r(j)$ for $1\leq j\leq M$, and $U_j^*=U_j$ for
   $0\leq j\leq M$. Hence all exact prime channels, lift values, rational-recurrence carries,
   source matrices and finite source differences supported inside that prefix
   agree, without substituting a marginal law.
   These are not automatically certified true pi digit indicators, which
   require the original future Green correction and boundary checks.
3. Every finite difference of the forcing and tail has the strict Hausdorff
   sign: $(-1)^b\Delta^b r^*(n+1)>0$ and
   $(-1)^b\Delta^b T_n^*>0$ for all $n,b\geq0$. Every finite Hankel matrix
   of either sequence is strictly positive definite.
4. $R-F$ vanishes to order at least $K+1$ at $t=1$. In particular all
   endpoint derivatives through order $K$ agree. An explicit rational $C>0$
   gives, for every $n,b\geq0$,

$$
\left|\Delta^b\bigl[r^*(n+1)-r(n+1)\bigr]\right|
\leq
16C\,4^b\,
\frac{2^{K+b+1}(K+b+1)!}
{\prod_{j=0}^{K+b+1}(8n+2j+1)}.
\tag{1}
$$

5. At the fixed nonzero frequency $h=\operatorname{den}(\beta)$,

$$
\frac1N\sum_{n=1}^N e(hU_n^*)\longrightarrow1.
\tag{2}
$$

Consequently this source is nonnormal. For **every** integer schedule
$H_N\to\infty$, its normalized Fourier excess $D^*_{N,H_N}/H_N$ tends
to $+\infty$, rather than zero.

The quantifiers are $\forall M,K\ \exists$ one fixed counterfeit, followed
by $n\to\infty$. There is no assertion that a single counterfeit matches
the infinite authentic prefix or the whole analytic endpoint jet. The exact
four-pole identity fails; the original global conductor law is not asserted
preserved.

## 2. Explicit positive approximation in the even variable

Put $s=t^2$. A direct algebraic factorization gives

$$
F(t)=(1-t^2)A(t^2),\qquad
A(s)=\frac{(s+2)\left(2+s/(1+\sqrt s)\right)}{16-s^4}.
\tag{3}
$$

For $m\geq1$ define

$$
a_m=\frac{\binom{2m}{m}}{4^m(2m-1)},\qquad
B_L(s)=\sum_{j=0}^L a_{j+1}(1-s)^j,
$$

$$
J_L(s)=\frac1{15}\sum_{j=0}^L
\left(-\frac{1-s^4}{15}\right)^j,
\qquad A_L(s)=(s+2)(2+sB_L(s))J_L(s).
\tag{4}
$$

The binomial series for $\sqrt{1-z}$ proves
$1/(1+\sqrt s)=\sum_{j\geq0}a_{j+1}(1-s)^j$. Its coefficients are
positive and their sum at $s=0$ is $1$. For $0\leq s\leq1$,
$0<B_L\leq1$. The alternating geometric series in $J_L$ has ratio in
$[-1/15,0]$, so, for $L\geq1$,

$$
\frac{14}{225}\leq J_L\leq\frac1{15},\qquad
\boxed{\frac{56}{225}\leq A_L\leq\frac35.}
\tag{5}
$$

Both truncations agree with their target Taylor series through order $L$
at $s=1$. Define

$$
\tau_L=\frac{\binom{2L+2}{L+1}}{4^{L+1}},\qquad
c_L=\frac{\tau_L}{5}+\frac35\left(\frac4{15}\right)^{L+1}.
$$

The identity $\sum_{m\geq L+2}a_m=\tau_L$ follows by telescoping
$a_m=\binom{2m-2}{m-1}/4^{m-1}-\binom{2m}{m}/4^m$.
The exact geometric remainder and $1-s^4\leq4(1-s)$ now give

$$
|A(s)-A_L(s)|\leq c_L(1-s)^{L+1}.
\tag{6}
$$

In particular $A_L\to A$ uniformly. Here $\tau_L\to0$ can be seen
directly from $\tau_L=\prod_{j=1}^{L+1}(1-1/(2j))$ and the divergence
of the harmonic series; no asymptotic normality input is present.

## 3. Exact interpolation without losing odd denominators

Let $T_n^{(L)}=\int_0^1t^{8n}(1-t^2)A_L(t^2)\,dt$.
**Every one of these rationals has odd denominator.** This does not follow
merely from even exponents: the coefficients themselves have dyadic
denominators, which must be accounted for.

For integers $n,i,m\geq0$,

$$
\int_0^1t^{8n+2i}(1-t^2)^m\,dt
=\frac{2^m m!}{\prod_{j=0}^m(8n+2i+2j+1)}.
\tag{7}
$$

For $m\geq1$, $a_m2^m m!=(2m-3)!!$ is an integer, with
$(-1)!!=1$. Expanding (4), the terms involving $B_L$ are exactly
$a_m(1-t^2)^m$ times polynomials in $t^2$ whose coefficients have odd
denominators. Equation (7) cancels all their dyadic denominator debt.
The remaining terms already have odd denominators. This proves the claim.

Choose an odd-denominator rational $\beta_L\to T_0$ with exponentially
small error. One explicit source-only choice, used by the code, is

$$
D=L+M+4,\quad p_D=\sum_{j=1}^D16^{-j}r(j),\quad q_D=16^D+1,
\quad \beta_L=\frac{\lfloor q_Dp_D\rfloor}{q_D}.
$$

Positivity and monotonicity of $r$ give

$$
0<T_0-\beta_L<q_D^{-1}+\frac{r(D+1)}{15\,16^D}.
\tag{8}
$$

Set $d=M+K+1$, $D_d(x)=\prod_{i=0}^d(8x+2i+1)$, and for
$j=0,\ldots,M$ put

$$
\epsilon_j=16^j\beta_L-U_j-T_j^{(L)},\qquad
y_j=D_d(j)\epsilon_j.
$$

These numbers all have odd denominator. Let $P_L(x)$ be their degree
at most $M$ Newton interpolant:

$$
P_L(x)=\sum_{j=0}^M(\Delta^j y)_0\binom{x}{j}.
\tag{9}
$$

For **every integer $n\geq0$**, $P_L(n)$ has odd denominator: its Newton
coefficients do, and $\binom nj$ is an integer. Thus

$$
\delta T_n=\frac{P_L(n)}{D_d(n)}
\tag{10}
$$

has odd denominator for every $n$, and equals $\epsilon_n$ for
$0\leq n\leq M$. This is an all-time proof, not a finite denominator test.

All poles of (10) are simple. Partial fractions give

$$
\delta T_n=\sum_{i=0}^d\frac{c_i}{8n+2i+1},\qquad
c_i=\frac{P_L(-(2i+1)/8)}{\prod_{j\ne i}2(j-i)}.
\tag{11}
$$

Define $\delta R(t)=\sum_i c_it^{2i}$. The degree bound on $P_L$ makes
$\delta T_n=O(n^{-K-2})$. Equivalently,

$$
\delta R(t)=(1-t^2)^{K+1}C_L(t^2)
\tag{12}
$$

for a rational polynomial $C_L$ of degree at most $M$. To verify this
equivalence without an analytic guess, expand (11) at $n=\infty$.
The coefficients of $n^{-1},\ldots,n^{-K-1}$ vanish, so
$\sum_i c_i(2i+1)^j=0$ for $0\leq j\leq K$. The polynomials
$(2i+1)^j$ span polynomials in $i$ through degree $K$, including every
falling factorial $i(i-1)\cdots(i-j+1)$. Hence the derivatives through
order $K$ of $\sum c_is^i$ vanish at $s=1$, proving (12).

Since $M,K$ are fixed, (6) and (8) imply $\epsilon_j\to0$. Every map
from these finitely many residuals through (9), (11), and polynomial
division (12) is fixed and linear. Therefore the sum $c=\|C_L\|_1$ of
absolute monomial coefficients tends to zero. Increase $L\geq K$ until
the **exact rational test** $c<1/10$ succeeds. It eventually does.

Now define

$$
R(t)=(1-t^2)\bigl[A_L(t^2)+(1-t^2)^KC_L(t^2)\bigr].
\tag{13}
$$

Equations (5) and $|C_L(s)|\leq c$ prove global positivity, with margin
$56/225-c>0$. The tail moments are $T_n^{(L)}+\delta T_n$, so they
remain odd-denominator at every integer time. Equations (9)--(10)
prove $T_j^*=16^j\beta_L-U_j$ through time $M$. They give the exact
zero anchor and the full authentic prefix. They also prove
$T_0^*=\beta_L$; the seed is not freely reassigned after constructing
the source.

## 4. Quantitative jets, positivity and low-frequency failure

From (6), (12)--(13), $L\geq K$ and $0\leq1-s\leq1$,

$$
|R(t)-F(t)|\leq C(1-t^2)^{K+1},\qquad C=c+c_L.
\tag{14}
$$

Multiply by $16-t^8\leq16$, and by
$(1-t^8)^b\leq4^b(1-t^2)^b$, then apply (7). This proves (1)
with no limit exchange. For each fixed $b$ the bound is
$O_{M,K,b}(n^{-K-b-2})$.

The positive densities $R(t)$ and $(16-t^8)R(t)$ prove every strict
Hausdorff difference sign by inserting $(1-t^8)^b$ into the integral.
For a nonzero polynomial $p$, the corresponding Hankel quadratic form
is the integral of $|p(t^8)|^2$ against a density positive on $(0,1)$,
and is strictly positive. This is an all-order argument, not extrapolation
from sampled determinants.

The authentic rational source satisfies, for every fixed $b\geq0$,

$$
n^{b+2}(-1)^b\Delta^br(n+1)
\longrightarrow\frac{15}{64}(b+1)!.
\tag{15}
$$

For example, expand its rational function at infinity and apply the
finite binomial difference: the first nonvanishing difference of $n^{-2}$
is $(-1)^b(b+1)!n^{-b-2}$. The convergent rational expansion also bounds
the remaining terms after any fixed number of differences. Equation (1)
shows that the **same fixed counterfeit shares (15) for every fixed $b$**.
It therefore shares both the $n^2$ angle $15/64$ and the $n^3$ angle
$15/32$, and the whole sequence of fixed-order leading critical bands.
It matches only finitely many subleading endpoint terms; do not confuse
these two quantifiers.

On the other hand, (5) and (13) give

$$
0<T_n^*\leq\left(\frac35+c\right)
\frac2{(8n+1)(8n+3)},\qquad
\sum_{n\geq1}T_n^*<\frac{3/5+c}{16}.
\tag{16}
$$

The sum uses $(8n+1)(8n+3)>64n^2$ and
$\sum_{n\geq1}n^{-2}<2$. Write $\beta=a/q$ in lowest terms. Since
$q16^n\beta\in\mathbb Z$,

$$
e(qU_n^*)=e(-qT_n^*),\qquad
\left|\frac1N\sum_{n=1}^Ne(qU_n^*)-1\right|
<\frac{7q(3/5+c)}{16N}.
\tag{17}
$$

This proves (2), and the same argument applies to every fixed multiple
$\ell q$. For any fixed integer $J$, the spectral identity yields

$$
\liminf_{N\to\infty}\frac{D^*_{N,H_N}}{H_N}\geq2J
\quad(H_N\to\infty),
$$

by retaining the frequencies $q,2q,\ldots,Jq$. As $J$ is arbitrary,
the normalized excess diverges. If also $H_N=o(N)$, the exact sequential
identity implies that the normalized signed innovation debt diverges
as well. Thus its cancellation cannot follow from the matched data.

## 5. A lawful comparison map and its exact missing boundary

For two forcings with the same zero initial state, define
$\delta r_j=r_j^*-r_j$ and $\delta U_n=U_n^*-U_n$. Iteration gives

$$
\delta U_n=\sum_{j=1}^n16^{n-j}\delta r_j.
\tag{18}
$$

Therefore, for a fixed integer $h$,

$$
|a_N^*(h)-a_N(h)|
\leq\frac{7|h|}{15N}
\sum_{j=1}^N(16^{N-j+1}-1)|\delta r_j|.
\tag{19}
$$

This bound follows from the character Lipschitz estimate followed by a
finite geometric sum; no outgoing Fourier channel is discarded. The
critical-band errors in (1) are polynomially small in time. They do not
pay the exponentially weighted propagation budget in (19).
The Green decomposition identifies the boundary exactly:

$$
\delta U_n=16^n(\beta-T_0)-(T_n^*-T_n).
\tag{20}
$$

Here $\beta-T_0\ne0$, because $\beta$ is rational and $\pi$ is irrational.
Arbitrarily accurate finite endpoint agreement controls the last term,
but does not remove the selected homogeneous component. This is the
precise high-to-low transfer obstruction furnished by the construction.

## 6. What fails in the source passport

The changed forcing is the moment sequence of an even polynomial
$(16-t^8)R(t)$. As a rational function of $n$ in $r^*(n+1)$, its poles
can occur only at negative **odd eighths**. Authentic $r(n+1)$ has the
nonzero poles at $n=-1/2$ and $n=-3/4$ as well. The two rational
functions cannot be identical. The authentic global pole positions,
residues and rational non-coboundary invariant are therefore excluded
hypotheses. Exact conductor evolution is not asserted preserved; a different
pole law alone would not prove different cumulative conductors.

The theorem refutes a coupling deduced only from the simultaneous
coarse data listed in SP-M1, even with every fixed-order leading moving
band. It does not refute a theorem using the entire exact four-pole law.
The next arithmetic argument must use that global law quantitatively
to constrain selected real-circle correlations. Prefix authenticity and
asymptotic source curvature, even strengthened as above, cannot supply
that constraint by themselves.

## 7. Exact execution and claim boundaries

Implementation: `observational_succ/spectral_purity_multiscale.py`.
Tests: `tests/test_spectral_purity_multiscale.py`.

The $(M,K)=(2,2)$ witness succeeds at $L=2$, with density degree
$13$ in $s=t^2$ (degree $26$ in $t$), selected seed
$\beta=843314856/4294967297$, and correction norm

$$
c=\frac{98307994236796565663999659127}
{4267972546102664804192325120000}<\frac1{10}.
$$

The independently larger holdout $(M,K)=(6,6)$ succeeds at $L=24$,
with degree $123$ in $s$ and the same exact positivity rule. The tests compare
literal four-pole values, complete unwrapped recurrence states, independent
beta expansion, derivative jets against the literal polynomial
$4-2t^3-t^4-t^5$, signed finite differences and (1), new times through
$65537$, and the exact formal character identity behind (17).
Wrong source signs, shifted anchors, and insufficient refinement budgets
are retained rejection controls.

Command: `python -m unittest discover -s tests -p 'test_spectral_purity_multiscale.py' -v`.
Observed result: **14 tests passed**. Finite tests support the implementation;
the universal claims depend on the proofs above. No numerical spectra,
random source averaging, cyclotomic equality shortcut, or pi digit oracle
is used. The module's resource cap can fail to find a witness; that is
reported as an access/work-budget outcome, not nonexistence.

| Claim | Status | Scope |
|---|---|---|
| SP-M1: simultaneous prefix/jet/positive/odd-conductor nonnormal controls | PAPER-PROVED; EXACT FINITE witnesses | One fixed changed source for each finite $M,K$ |
| SP-M2: explicit all-order forcing difference bound (1) | PAPER-PROVED; EXACT FINITE checks | Every $n,b\geq0$; constants depend on the constructed source |
| SP-M3: all fixed leading derivative bands coexist with divergent purity | PAPER-PROVED | Global exact BBP pole law is excluded |
| SP-M4: propagation comparison (18)--(20) | CLASSICAL / PAPER-PROVED | Explicit homogeneous boundary retained |
| Moving-band/prefix/positivity/odd-denominator data alone imply purity | REFUTED | Concrete family, fixed nonvanishing frequency (17) |
| Exact authentic four-pole innovation saving | OPEN | Not decided by the counterfeit theorem |
