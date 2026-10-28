# Finite forcing-energy core and two limits of source approximation

**Scope:** finite real algebra checked by Lean; the complex application and
two approximation obstructions below are PAPER-PROVED. No infinite analytic
theorem, BBP normality theorem, or new scholarly priority is claimed.
The primary source remains the original four signed poles with $U_0=0$.
No production forcing or historical proof artifact is changed here.
The factor-289 norm argument in §1 is inherited from PRK-02 of
[the prime-clock report](../2026-10-25/PRIME_CLOCK_RESONANCE_REPORT.md),
commit `eca4462ee4d62642b15c4af672136aa5bcacd00b`.
Its formalization here is new; its mathematical identity is not.
The unit-center modulus comparison strengthens the prior unconstrained
variance comparison as quantified in `GLOBAL_SOURCE_CURVATURE.md`.

## 1. Exact finite real energy transport

Let $T\ge0$, $u_0,\ldots,u_T\ge0$ and $w_0,\ldots,w_{T-1}\ge0$.
Assume only the explicit comparison

$$w_i\le u_{i+1}+16u_i\qquad(0\le i<T).$$

The weighted square identity is

$$17a^2+272b^2-(a+16b)^2=16(a-b)^2.$$

Therefore

$$
\boxed{\sum_{i<T}w_i^2
\le289\sum_{i=0}^{T}u_i^2-17u_0^2-272u_T^2
\le289\sum_{i=0}^{T}u_i^2.}
\tag{1}
$$

The boundary coefficients follow by summing
$17u_{i+1}^2+272u_i^2$: an interior state has coefficient 289,
the first state 272, and the last state 17. The constant 289 is optimal
uniformly in $T$ under these hypotheses. Set every $u_i=1$ and every
$w_i=17$. The ratio of the two unweighted sums is $289T/(T+1)$,
which tends to 289. The explicit finite instance $T=289$ already
violates coefficient 288, by exactly one.

For unit complex phases obeying $z_{i+1}=f_i z_i^{16}$, choose a unit
phase $a$. The elementary telescoping bound for sixteenth powers gives

$$|f_i-a^{-15}|\le |z_{i+1}-a|+16|z_i-a|.$$

Apply (1) with these three nonnegative distances. If $a$ minimizes the
sum of phase squared distances, that sum is
$2(T+1-|\sum_{i=0}^T z_i|)$. The minimum forcing squared distance is
$2(T-|\sum_{i<T}f_i|)$ and is at most the forcing distance to the
particular center $a^{-15}$. Hence the paper-level application is

$$
T-|\sum_{i<T}f_i|
\le289\bigl(T+1-|\sum_{i=0}^{T}z_i|\bigr).
\tag{2}
$$

The finite Lean source proves (1) from its stated real hypotheses and
the scalar consequence $F\le289(L-A)\Rightarrow A\le L-F/289$.
It does not formalize the complex factorization, optimal circle center,
or identification of these phases with the BBP source.

## 2. Rational core of the quiet-transition improvement

The accompanying analytic argument supplies nonnegative total squared
phase deviation $Q$, modulus loss $D$, forcing range $R$, and a quiet
transition comparison. Its finite scalar implication is

$$
19Q\le D,\qquad
(1-R)^2\le257Q(1+u)^2,
\qquad u\ge0
\quad\Longrightarrow\quad
D\ge\frac{19(1-R)^2}{257(1+u)^2}.
\tag{3}
$$

With at least 20000 transitions, $u=1/100$ satisfies $u^2T\ge2$.
At $R\le15/4096$, the exact rational margin is

$$
\frac{19(4081/4096)^2}{257(101/100)^2}-\frac1{14}
=\frac{9907077909}{19243046273024}>0.
\tag{4}
$$

Thus the hypotheses in (3), $R\le15/4096$, and $D\le1/14$ are
inconsistent. Lean checks this scalar contradiction and (4).
It separately checks the rational local-cosine coefficient

$$
2(157/50)^2-\frac23(22/7)^4\frac1{112}
=\frac{1206224729}{63026250}>19.
\tag{5}
$$

The global chord estimate, existence of a quiet transition, the integer
branch comparison, cosine/Taylor estimates, and the irrationality-measure
step are hypotheses or paper arguments outside this kernel file. In
particular, (5) is a rational numerical theorem, not a Lean theorem about
the transcendental cosine function.

## 3. Fixed-frequency ceiling of the forcing-defect method

This is a quantitative limitation of the particular comparison (2), not
an impossibility theorem for other source-sensitive methods. Keep

$$r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.$$

For $h\ne0$ an integer and $J\ge1$, define its forcing defect

$$F_J(h)=J-\left|\sum_{n=1}^{J}e(hr(n+1))\right|.$$

The inherited four-pole inequality
$0<r(n+1)<15/(64n^2)$ gives

$$
0\le1-\operatorname{Re}e(hr(n+1))
\le\min\left(2,\frac98\frac{h^2}{n^4}\right).
\tag{6}
$$

Indeed $1-\cos x\le x^2/2$, and
$2(22/7)^2(15/64)^2<9/8$. Since the modulus of a sum is at least
its real part, put $L=\lceil\sqrt{|h|}\rceil$ and sum (6). The
decreasing-integral comparison gives
$\sum_{n>L}n^{-4}\le1/(3L^3)$. Therefore, uniformly in every $J$,

$$
\boxed{0\le F_J(h)\le2L+\frac38\frac{h^2}{L^3}
\le\frac{19}{8}\sqrt{|h|}+2.}
\tag{7}
$$

For any finite block supported in $n\ge m$, the same real-part bound
is at most $3h^2/(2m^3)$, using
$\sum_{n\ge m}n^{-4}\le m^{-4}+1/(3m^3)\le4/(3m^3)$.
Thus the right-hand forcing deficit in (2) remains bounded for a fixed
$h$, and becomes small on late blocks. The displayed forcing-defect
comparison alone cannot yield an unbounded fixed-mode modulus loss.
This does not preclude improvements from other information about the
actual orbit. A genuine critical-band result with $h$ comparable to
$m^2$ has different quantifiers: moving the frequency into that range
does not itself transfer its saving back to a fixed nonzero mode.

The missing additional statement is a quantitative comparison connecting
those moving-frequency signed phase statistics to fixed-frequency
statistics of the original selected orbit. The source recurrence's
ordinary $h\mapsto16h$ time shift does not by itself supply such a
uniform comparison at a moving number of shifts.

## 4. A prime-jet discriminator for inherited positive real surrogates

This appendix records an exact arithmetic discriminator, without claiming
a selected signed saving. The inherited
[SP-M1 construction](../2026-10-25/SPECTRAL_PURITY_MULTISCALE.md) already
produces positive even polynomial Green kernels matching any specified
finite authentic prefix and finite endpoint jet, with zero initial state,
odd denominators, and a rational nonnormal endpoint. Those are inherited
countermodels, not newly constructed here. They expressly do not preserve
the entire original forcing law or its global prime channels.

Let $R(t)=\sum_{i=0}^{d}c_it^{2i}\in\mathbb Q[t^2]$ be any such
polynomial, and define its rational Green forcing

$$
r_R(n)=\sum_{i=0}^{d}c_i
\left(\frac{16}{8n+2i-7}-\frac1{8n+2i+1}\right).
\tag{8}
$$

Fix a finite difference order budget $B\ge0$. Choose a prime
$p>8B+2d+5$ dividing none of the denominators of the $c_i$.
Such primes exist; a proposed prime and its finitely many denominator
conditions can be checked independently. For every $a\ge1$, choose
$k_a\in\{1,3\}$ so that $k_ap^a\equiv3\pmod4$, and set

$$n_a=\frac{k_ap^a+1}{4}.$$

Then for every $0\le b\le B$, writing $\Delta f(n)=f(n+1)-f(n)$,

$$
\boxed{v_p\!\left(\Delta^b(r-r_R)(n_a)\right)=-a,}
\tag{9}
$$

and the scaled residue is explicit:

$$
p^a\Delta^b(r-r_R)(n_a)
\equiv\frac{(-1)^{b+1}}{2k_a}\pmod p.
\tag{10}
$$

**Proof.** At $n=n_a+j$, the denominators in (8) reduce modulo $p$
to $8j+2i-5$ and $8j+2i+3$. They are nonzero odd integers of absolute
value strictly less than $p$, for $0\le j\le B$ and $0\le i\le d$.
Thus the entire surrogate stencil is $p$-integral. The four original
denominators reduce to $8j-5$, $8j-2$, $8j-1$, and $8j$. For $j\ge1$
all are nonzero and smaller than $p$; for $j=0$ only the last vanishes.
The exceptional original pole is exactly

$$-\frac1{8n_a-2}=-\frac1{2k_ap^a}.$$

Since $p\ge7$, its numerator and $2k_a$ are units. Every other stencil
term is integral. The forward difference coefficient at $j=0$ is
$(-1)^b$, a unit, which proves both (9) and (10). QED.

For the inherited SP-M1 surrogates, their proved real difference bounds
give $\Delta^b(r-r_R)(n_a)\to0$ in the real norm for each fixed $b$,
while (9) gives $|\Delta^b(r-r_R)(n_a)|_p=p^a\to\infty$ at this one
fixed prime. Thus arbitrarily accurate real endpoint-jet and positive
moment approximation does not supply uniform prime-channel fidelity.
The discriminator identifies the missing original $8n-2$ pole, with its
sign and an explicit all-depth sequence, instead of merely saying that
the counterfeit changes some unspecified source data.

This result is restricted to the stated finite even-polynomial class.
It neither gives a theorem about all source mutations nor proves that
retaining the prime stencil forces circle cancellation. It shows a
specific all-depth arithmetic test that the inherited real surrogates
fail. The original Gaussian coefficient clock is also not preserved by
these finite polynomial surrogates; no Gaussian/prime independence is
claimed from the two ways to detect that changed source.

## 5. Formal authority and replay

New files are `formal/GlobalSigned.lean` and
`scripts/check_global_signed_lean.py`. The checker verifies the pinned
Lean 4.14.0 toolchain and every dependency revision against mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, with one compiler thread
and a 2048 MB compiler memory cap. It exports exact declaration types,
hashes, and axiom lists, and runs paired true/false arithmetic controls.
The source and observation receipt identify the exact final formal scope.
The completed run is **KERNEL_CHECKED: 13 declarations and seven paired
positive/false controls**. Every recorded source hash and exported type
hash was rechecked afterward. The only axioms are `propext`,
`Classical.choice`, and `Quot.sound`; no analytic conclusion inherits
kernel authority from those finite declarations.

```sh
python scripts/check_global_signed_lean.py \
  --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge \
  --output research/2026-10-27/global_signed_validation/lean
```

The first local elaboration failed because a sum-rewrite targeted the
wrong occurrence in the endpoint identity. The rewrite was restricted
to the intended range before the successful kernel check. The initial
log was overwritten by the replay checker; this record preserves the
failure and its cause without presenting a reconstructed log as raw output.
Neither that failed elaboration nor the paper-only appendices receive
kernel authority. No historical Lean receipt or imported source was altered.

## 6. Classical completeness of the finite polynomial zero relations

This is a **CLASSICAL / PAPER-PROVED application**, not a new arithmetic
inequality. It extends the scope of the inherited linear completeness in
[SS-01/02](../2026-10-25/SEINFELD_SUCC_NOTHING_THEOREMS.md) to every
polynomial in the same finite state variables. The general ideal-membership
framework is already recorded in
[CZR-01](../../docs/CLAIM_SUPPLEMENT_COHERENT_ZERO.md).

Fix $N\ge0$ and the exact rational forcing values $r(1),\ldots,r(N)$.
In $A_N=\mathbb Q[u_0,\ldots,u_N]$, write

$$
E_i=u_i-16u_{i-1}-r(i),\qquad
J_N=(E_1,\ldots,E_N),\qquad I_N=(u_0,E_1,\ldots,E_N).
$$

Let $U_0=0$ and $U_i=16U_{i-1}+r(i)$ denote the exact selected states.
Then

$$
\boxed{A_N/J_N\simeq\mathbb Q[t],\qquad
A_N/I_N\simeq\mathbb Q,\qquad
I_N=(u_0-U_0,\ldots,u_N-U_N).}
\tag{11}
$$

In particular, a polynomial $F\in A_N$ vanishes on the authentic finite
trajectory if and only if $F\in I_N$. Without the initial-state relation,
$F\in J_N$ if and only if the polynomial
$F(t,16t+U_1,\ldots,16^Nt+U_N)$ is identically zero. Vanishing at the
one selected seed is not sufficient for membership in $J_N$; $F=u_0$
is the simplest counterexample.

**Proof.** The exact identities

$$
u_i-U_i=16^iu_0+\sum_{j=1}^i16^{i-j}E_j,
\qquad
E_i=(u_i-U_i)-16(u_{i-1}-U_{i-1})
$$

give the claimed equality of ideals. The triangular change of coordinates
$(u_0,\ldots,u_N)\mapsto(u_0,E_1,\ldots,E_N)$ is a polynomial
automorphism over $\mathbb Q$: its inverse is the first displayed
identity with the known rational $U_i$ added. Quotienting by the last
$N$ coordinates leaves $\mathbb Q[u_0]$; quotienting by all $N+1$
coordinates leaves $\mathbb Q$. Thus $I_N$ is the maximal point ideal,
whereas $J_N$ retains the free seed parameter.

There is also an explicit certificate for every selected polynomial zero.
Replace the arguments of $F$ by $U_i$ one at a time. Each successive
difference is divisible by $u_i-U_i$, so for rational polynomials $G_i$,

$$
F(u)-F(U)=\sum_{i=0}^N(u_i-U_i)G_i(u)
=u_0\sum_{i=0}^N16^iG_i(u)
 +\sum_{j=1}^NE_j\sum_{i=j}^N16^{i-j}G_i(u).
\tag{12}
$$

When $F(U)=0$, this gives the required ideal-membership witness. Conversely,
every generator evaluates to zero at $U$, so every ideal element does.
No algebraic closure or Nullstellensatz is required. QED.

The scope is exactly finite rational polynomials in these state variables
with the full original forcing already supplied. Additional polynomial zero
presentations cannot cut down this singleton further. Their provenance and
certificate complexity can still matter, and they may help prove useful
inequalities. This statement does not cover extra transcendental phase
variables without their comparison maps, real-distance estimates, or bounds
uniform in $N$. In particular it is not a no-go theorem for discovering a
quantitative signed estimate from the recurrence. It locates the missing
work: a useful new relation must provide quantitative information beyond
the mere vanishing of another polynomial at the already selected point.
