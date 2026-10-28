# Uniform sparse-selector obstruction to growing-lag differencing

Status: **PROVED** (paper argument); the imported irrationality-exponent statement is **CLASSICAL**. No normality proof, original-source counterexample, or new academic priority is asserted.

## Exact statement and scope

Keep the authentic four-pole forcing and its positive future Green tail:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad 0<T_n<\frac1{64n^2}\quad(n\ge1).
$$

Let

$$
\xi=\sum_{j\ge0}16^{-2^j},\qquad V_n=16^n\xi-T_n.
$$

The sequence obeys **exactly** `V_(n+1)=16 V_n+r(n+1)`, for all `n>=0`.
Its initial value is the single fixed number `V_0=xi-pi/16`, which is
strictly negative: `xi<1/15<3/16<pi/16`. Thus it deliberately changes the
zero initial selector. The countermodel does not carry a passport as the
original rational BBP states, their odd conductors, or their 2-adic state
clock. Its forcing, poles, signs, Green tail and forcing conductors are
unchanged.

For any finite tuple of positive integer lags, including the empty tuple,
put

$$
P(E)=\prod_{i=1}^k(E^{\ell_i}-1),\qquad d=\sum_i\ell_i.
$$

For `N>=1` and a nonzero integer `h`, define integers

$$
w=\max\{1,\min\{j\ge0:16^j\ge |h|2^kN\}\},\quad D=d+w,
\quad J=\min\{j\ge0:2^jD\ge N+D\},\quad m=\lceil\sqrt{|h|}\rceil.
$$

Then

$$
\boxed{\left|\sum_{n=1}^Ne(hP(E)V_n)-N\right|
\le 2\min\{N,D(2+J)\}+\frac{44}{105}+2m+\frac{11|h|}{112m}.}
\tag{SM-1}
$$

Every quantity in the bound can be computed with integer comparisons and
rational arithmetic. An empty tuple means `P(E)=1`, `k=d=0`.

In particular, for any positive schedules `d_N=o(N)` and `H_N=o(N^2)`,

$$
\boxed{\sup_{\substack{1\le |h|\le H_N\\\sum\ell_i\le d_N}}
\left|\frac1N\sum_{n=1}^Ne(hP(E)V_n)-1\right|\longrightarrow0.}
\tag{SM-2}
$$

The conclusion allows the order `k` to grow up to the span `d`, and does
not bound individual completed frequencies `hP(16)` polynomially in `N`.
Indeed those frequencies can be exponential in the sublinear span.

## Proof

### 1. All orders have a uniform Green budget

The inherited integral is

$$
T_n=\int_0^1 t^{8n}\frac{4-2t^3-t^4-t^5}{16-t^8}\,dt.
$$

Its density is positive, since its numerator equals
`(1-t)(4+4t+4t^2+2t^3+t^4)` on `(0,1)`. Therefore

$$
(-1)^kP(E)T_n=\int_0^1t^{8n}
\frac{4-2t^3-t^4-t^5}{16-t^8}
\prod_i(1-t^{8\ell_i})\,dt,
$$

and `|P(E)T_n|<=T_n`; equality is allowed for the empty tuple. This is the
same inherited positive-kernel fact used in #319, not a new source identity.
Using `|e(x)-e(y)|<=min(2,2pi|x-y|)` and `2pi<44/7`,

$$
\begin{aligned}
\sum_{n=1}^N|e(hP(E)V_n)-e(hP(16)16^n\xi)|
&\le\sum_{n=1}^N\min\left(2,\frac{11|h|}{112n^2}\right)\\
&\le2m+\frac{11|h|}{112}\sum_{n>m}n^{-2}\\
&\le2m+\frac{11|h|}{112m}.
\end{aligned}
\tag{SM-3}
$$

This pays the entire Green tail and every order, with no factor `2^k`.
It also remains valid when `m>N`.

### 2. A sparse-digit union estimate

Write `P(X)=sum_(j=0)^d c_j X^j`, with integer coefficients. Expanding
products and combining equal powers gives

$$
\sum_j|c_j|\le2^k.
\tag{SM-4}
$$

For every `t>=0`, the actual radix fractional part is

$$
s_t=\{16^t\xi\}=\sum_{2^a>t}16^{t-2^a}.
$$

There is no carry: all digits are zero or one. Declare `n` bad exactly if
there exists a power of two in `(n,n+D]`. If `n` is good, then for every
`0<=j<=d` no sparse exponent lies in `(n+j,n+j+w]`. Every remaining
exponent is at least `n+j+w+1`, so comparison with *all* later integer
exponents gives

$$
0\le s_{n+j}\le\sum_{v\ge w+1}16^{-v}
=\frac{16^{-w}}{15}.
\tag{SM-5}
$$

For a fixed sparse exponent `a`, the bad indices are contained in the
integer interval `[a-D,a-1]`, of length `D`. All powers `a<=D` contribute
indices only in `[1,D]`, a total of at most `D`. The later powers in
`(D,N+D]` number at most `1+J`, because successive powers double and
`2^J D>=N+D`. Consequently the union has size

$$
\#\{\text{bad }n\in[1,N]\}\le\min\{N,D(2+J)\}.
\tag{SM-6}
$$

This avoids the weaker `D log N` bound. It is the step that permits every
sublinear span `d=o(N)`, rather than only `d=o(N/log N)`.

### 3. The signed correlation estimate

Modulo an integer,

$$
hP(16)16^n\xi=h\sum_jc_js_{n+j}.
$$

At a good index, (SM-4), (SM-5), and the chosen `w` imply

$$
|e(hP(16)16^n\xi)-1|
\le\frac{44}{105}|h|2^k16^{-w}\le\frac{44}{105N}.
$$

At every bad index use the bound two. Summing and adding (SM-3) proves
(SM-1).

For (SM-2), `k<=d` and the definition of `w` give

$$
D\le\frac54d+2+\log_{16}(H_NN)=o(N)
$$

once `H_N>=1`, since `H_N=o(N^2)` in particular eventually gives
`log H_N=O(log N)`. Furthermore
`J<=1+log_2(1+N/D)`. The function
`x(3+log_2(1+1/x))` tends to zero as `x->0+`; hence the bad-index bound
is `o(N)` uniformly. Finally, `m=O(1+sqrt(H_N))=o(N)`, and
`|h|/m<=sqrt(|h|)`. Every term in (SM-1), divided by `N`, tends to zero
uniformly. QED.

## What this actually obstructs

For the empty tuple, (SM-2) implies that every fixed nonzero real Fourier
mean tends to one. Thus this single fixed same-forcing sequence is
maximally nonnormal in these observables.

For a one-lag filter, `e(h(E^ell-1)V_n)` is the genuine autocorrelation
`e(hV_(n+ell)) conjugate(e(hV_n))`. Iterating differencing gives the general
mixed product above. All these correlations stay near one uniformly over
**every sublinear total lag span**, even when the order grows. The same
holds for the usual truncated correlation ranges by replacing `N` with
`N-d`; because `d=o(N)`, that change does not affect the conclusion.

More explicitly, let `z_n=e(hV_n)` and
`C_ell=sum_(n=1)^(N-ell) z_(n+ell) conjugate(z_n)`. For any
`H=H_N->infinity` with `H=o(N)`, the classical zero-extension
van der Corput inequality is

$$
\frac{|\sum_{n=1}^Nz_n|^2}{N^2}
\le\frac{N+H-1}{NH}
\left[1+\frac2N\sum_{\ell=1}^{H-1}
\left(1-\frac\ell H\right)\mathop{\mathrm{Re}}C_\ell\right].
$$

Our theorem implies `C_ell/N=1+o(1)` uniformly for `ell<H`, at every
fixed nonzero frequency. Since the weights sum to `(H-1)/2`, the
right-hand side tends to **one**. Thus the standard differencing
inequality is asymptotically saturated on this same-forcing control,
including any diverging sublinear lag budget. The uniform higher-order
result shows that merely repeating this operation does not obtain a
missing decorrelation estimate for this family.

### An elementary finite-type certificate, independent of the imported exponent-two theorem

For `m>=0`, let `Q_m=16^(2^m)` and truncate
`xi_m=sum_(j=0)^m 16^(-2^j)`. Its reduced denominator is exactly `Q_m`,
because its numerator is congruent to one modulo 16. Its positive tail obeys

$$
0<\xi-\xi_m
=\sum_{r\ge1}Q_m^{-2^r}
\le\sum_{s\ge2}Q_m^{-s}
\le\frac{16}{15}Q_m^{-2}.
$$

Given any integer `p` and any integer `q>=1`, choose the least `m>=0`
with `Q_m>=3q`. If `m=0`, `Q_m=16<=16q^2`. If `m>=1`, minimality and
`Q_m=Q_(m-1)^2` give `Q_m<9q^2<=16q^2`. Because `Q_m>q` and the
truncation is reduced, `xi_m` cannot equal `p/q`; hence

$$
|\xi_m-p/q|\ge\frac1{qQ_m},\qquad
\xi-\xi_m\le\frac{16}{45qQ_m}<\frac1{2qQ_m}.
$$

The reverse triangle inequality yields the fully explicit bound

$$
\boxed{|\xi-p/q|\ge\frac1{32q^3}\quad
(p\in\mathbb Z,\ q\ge1).}
\tag{SM-7}
$$

In particular `xi` is irrational and has irrationality exponent at most
three. Rational rescaling gives a finite-type bound for `16xi`, which is
already strictly stronger than the exponent `15/2` required by #319's
argument. Thus the new obstruction and its compatibility with that
Diophantine mechanism need **no external irrationality-exponent theorem**.
The sharper classical value two below is optional inherited context.

The existing scalar sparse-selector result in
`research/2026-10-26/SELECTED_BRANCH_ANALYTIC.md`, Section 5, imports the
classical theorem `mu(xi)=2` for this exact Kempner-type number. Its cited
primary chain is Hone--Varona, Section 4, equation (4.2), DOI
`10.1007/s00605-018-1244-1`, referring to Bugeaud--Han--Wen--Yao,
*Hankel determinants, Pade approximations, and irrationality exponents*,
IMRN 2016, 1467--1496. The present argument does not reprove that theorem
and does not infer it from digits. Rational affine invariance gives
`mu(16xi)=2<15/2`.

Consequently #319's Diophantine/template proof applies to the completed
carrier `16xi` after a carrier-dependent onset: at each **fixed nonzero h**,
it gives bounded positive loss on each eligible geometric block and a
logarithmic global loss, with the same growing mixed-lag schedules. No
uniform-in-h logarithmic-loss comparison is asserted here; (SM-2) has its
own separate growing-frequency budget. Such logarithmic loss is compatible
with all the normalized correlations tending to one. The earlier
scalar `O(log N)` control is inherited; the new part is the **uniform
all-sublinear-span, growing-order, and growing-frequency obstruction**.

This refutes a deduction of vanishing mixed correlations from the package
of full authentic forcing, positive mixed Green kernels, finite
irrationality type, and the established logarithmic coercivity alone.
It does **not** refute a proof using the actual zero initial state or a
new arithmetic property of the rational authentic BBP history. It does
not show that all van der Corput strategies are impossible. Any successful
one must independently exclude this surviving coherent pattern by a
property genuinely specific to the selected `U_0=0` orbit.

## Falsifiable attempts and next proof obligation

Attempted implication: the uniform #319 mixed-lag logarithmic deficits,
iterated across more lags, force a fixed fractional or `o(N)` cancellation.
Predicted success: a growing collection of differenced correlations must
have means bounded away from one, or exhibit signed mutual cancellation.
Counterexample: the fixed `V` above makes *all* sublinear-span means tend
uniformly to one, while the finite-irrationality argument still gives
its inherited logarithmic deficits. Verdict: **REFUTED with this explicit
scope**.

Next verdict-changing input: prove for the exact zero-selected `U` an
estimate on averaged autocorrelations that is not inherited merely from
finite irrationality type. For instance, an independently justified
bound tending to zero on the weighted van der Corput correlation average
at some diverging sublinear lag scale would suffice through the standard
van der Corput inequality. That estimate remains **OPEN**; writing it
as a conditional criterion is not itself a research advance.
