# Uniform phase slips and the sharp finite-exponent barrier

**Status:** PROVED LOCAL paper derivations using the published Zeilberger–Zudilin
2020 theorem where explicitly indicated. The small integer no-wrap kernel was
checked in Lean; the real asymptotic statements were not formalized. Finite
certificates corroborate implementations, not infinite quantifiers. No scholarly
priority is asserted. The original four poles and `U_0=0` are unchanged.

Use `e(x)=exp(2 pi i x)`, the authentic source `r`, and the inherited identity
`U_n(s)=16^(n-1)(pi+16s)-T_n`. Write

\[
 E_{n,\ell}(h,s)=1-\Re e(h(U_{n+\ell}(s)-U_n(s))),\quad
 S_N(h,s)=\sum_{n=1}^N e(hU_n(s)),\quad \eta=1-\cos(\pi/10).
\]

## DP-00. Independent source-tail reconstruction

This proof uses elementary positive rational fractions rather than the parent's
Laplace integral. With `a=8k-7`, direct subtraction gives

\[
 r(k)=\frac6{a(a+3)}+\frac4{a(a+4)}+\frac5{a(a+5)}.
\]

For `a,d>0`,

\[
 \frac2{a^3}-\frac{2a+d}{a^2(a+d)^2}
 =\frac{d(3a+2d)}{a^3(a+d)^2}>0.
\]

Thus the negative derivative with respect to `a` of each `1/[a(a+d)]`
is at most `2/a^3`. Integrating over an increment of eight and adding the
weights proves `0<r(k)-r(k+1)<240/(8k-7)^3`. Summing with weights `16^-j`
proves exactly the inherited bound

\[
0<T_n-T_{n+1}<\frac{16}{(8n+1)^3}.
\]

Telescoping over a positive integer lag gives

\[
0<T_n-T_{n+\ell}<\frac{16\ell}{(8n+1)^3}.                 \tag{1}
\]

Also `r(k)<15/(8k-7)^2`, whence `T_n<(8n+1)^-2` and
`sum_(n>=1) T_n < 1/32`. The last rough constant follows from
`sum n^-2<=2`. These are source-specific error estimates, not signed
cancellation. DP-00's lag-one result is inherited, independently reconstructed.

## DP-01/02. One threshold for growing frequencies and lags

**Theorem.** There is one integer `A_0` such that for every integer `A>=A_0`,
every integer `ell,h` satisfying

\[
1\le\ell\le A/26,\qquad 1\le |h|,\qquad |h|\ell\le A^3/6,
\]

there is an integer `n` with `A<=n<8A` and

\[
\boxed{E_{n,\ell}(h,0)\ge\eta.}                         \tag{2}
\]

The quantifier is `exists A_0 for all A,h,ell`, stronger than choosing a
new unspecified threshold for each frequency and lag. It is still only
one definite slip in a long window, not positive-density dispersion.

**Proof.** Suppose every energy is smaller than eta. The exact selected lag is

\[
U_{n+\ell}(0)-U_n(0)=(16^\ell-1)16^{n-1}\pi+T_n-T_{n+\ell}.
\]

By (1), its source correction after multiplication by h has magnitude
less than `1/192`. Consequently the nearest-integer residues of
`(16^ell-1)h16^(n-1)pi` have absolute value less than
`1/20+1/192<1/18`. Let these signed residues be `epsilon_n`.
The integer `16 epsilon_n-epsilon_(n+1)` has magnitude below `17/18`,
so it vanishes. Repeatedly applying this elementary fact yields
`abs(epsilon_A)<(1/18)16^(-(7A-1))`.

Put `q=(16^ell-1)|h|16^(A-1)`. A rational `p/q` then satisfies

\[
0<|\pi-p/q|<\frac{1}{18q16^{7A-1}}.                    \tag{3}
\]

The published bound `mu(pi)<=7.103205334137...<15/2` supplies one
`c_pi>0` such that `abs(pi-p/q)>=c_pi q^(-15/2)` for every integer p
and positive q. Reduced and unreduced fractions are both covered: reducing
a fraction can only strengthen the lower bound, and finitely many small
reduced denominators can be absorbed into the positive constant.
Combining (3) with `q<A^3 16^(A+ell)` forces

\[
16^{7A-1}<C_\pi A^{39/2}16^{(13/2)(A+\ell)}.
\]

Because `ell<=A/26`, the difference between the two exponential exponents
is at least `A/4-1`. Exponential growth exceeds the fixed polynomial
uniformly for all sufficiently large A, a contradiction. All constants
are independent of h and ell in the declared region. QED.

**Authority.** The load-bearing result is Doron Zeilberger and Wadim Zudilin,
*The Irrationality Measure of Pi is at most 7.103205334137...*, Moscow J.
Combinatorics and Number Theory 9 (2020), 407–419. The
[authors' publication page](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html)
and [primary paper](https://arxiv.org/abs/1912.06345) were checked. No 2026
improvement or exponent-two claim is used. The Diophantine threshold here
remains non-effective as stated; no numeric value is invented.

## DP-01a. A frequency-uniform all-horizon signed inequality

There is one constant C, independent of integers `N>=1` and `h!=0`, such that

\[
\boxed{N-|S_N(h,0)|\ge
\frac{\eta}{4\log8}\log^+\!\left(\frac{N}{|h|^{1/3}}\right)-C.} \tag{4}
\]

Here `log^+(x)=max(0,log x)`. Start the disjoint geometric windows at
`A_h=max(A_0,26,ceil((6|h|)^(1/3)))`. Equation (2), with ell=1, supplies
eta energy on each complete window before N. There are at least
`log_8(N/A_h)-O(1)` such windows. Since
`log A_h <= (1/3) log |h|+O(1)` with a uniform constant, the total lag
energy is at least `eta/log8 * log^+(N/|h|^(1/3))-O(1)`.
The inherited unit-complex variance inequality

\[
N-|S_N|\ge\tfrac14\sum_{n=1}^{N-1}E_{n,1}
\]

proves (4). In particular, for each `0<epsilon<3`, the same bound gives a
logarithmic saving uniformly over `1<=|h|<=N^(3-epsilon)`.
This does not yield a useful vanishing discrepancy bound: the saving
is still logarithmic rather than proportional to N. It does not verify
SC-06's much shorter prime windows.

## DP-03. An elementary sharp finite-exponent countermodel

For every integer `m>=3`, define

\[
\beta_m=\sum_{j\ge0}16^{-m^j},\qquad
s_m=(\beta_m-\pi)/16.
\]

This is an explicitly **changed irrational seed**, never a replacement for
the authentic zero seed. The forcing, all four coefficients, and every Green
correction remain original. Its base-16 digits are 1 at the positions `m^j`
and 0 elsewhere, so it is irrational and not normal.

### Exact irrationality exponent

Let `Q_j=16^(m^j)` and `P_j/Q_j=sum_(i=0)^j 16^(-m^i)`.
The numerator is odd, hence this is reduced, and the remainder obeys

\[
Q_j^{-m}\le R_j=\beta_m-P_j/Q_j<2Q_j^{-m}.             \tag{5}
\]

This gives `mu(beta_m)>=m`. For a large positive denominator q, choose the
smallest j such that `Q_j^(m-1)>4q`. Then `j>=1` and
`Q_j<=(4q)^(m/(m-1))`. If the reduced fraction p/q differs from P_j/Q_j,
integer determinant separation and (5) give

\[
|\beta_m-p/q|>\frac1{2qQ_j}
\ge\frac1{2\,4^{m/(m-1)}}q^{-(1+m/(m-1))}
\ge c_m q^{-m}.                                      \tag{6}
\]

The last inequality uses `m>=3`. If the two fractions are equal, q=Q_j
and (5) itself gives the lower bound `q^-m`. Finitely many small denominators
can again be absorbed into a constant. Thus

\[
\boxed{\mu(\beta_m)=m.}                              \tag{7}
\]

This is a local elementary reconstruction of a classical lacunary phenomenon,
not a priority claim. The proof is self-contained and does not assume a
continued-fraction formula for the Kempner number.

### Only logarithmically many total character deviations

Put `x_n={16^(n-1) beta_m}` and `J_m(N)=1+floor(log_m N)` for `N>=1`.
Every completed sparse digit contributes at most 1/15 to `sum_(n<=N) x_n`.
The not-yet-completed digits contribute at most 1/225, because their exponent
positions are a subset of the integers larger than N. More explicitly,

\[
\sum_{n=1}^N x_n
=\frac1{15}\sum_{j\ge0}
 (16^{\min(N,m^j)-m^j}-16^{-m^j})
\le\frac{J_m(N)}{15}+\frac1{225}.                      \tag{8}
\]

Since `U_n(s_m)=16^(n-1)beta_m-T_n`, the elementary chord inequality gives

\[
\sum_{n=1}^N|e(hU_n(s_m))-1|
\le2\pi|h|\left(\frac{J_m(N)}{15}+\frac1{225}+\frac1{32}\right). \tag{9}
\]

In particular `S_N(h,s_m)/N -> 1` for **every fixed integer h**: there is
maximal asymptotic coherence, despite the finite exact exponent (7).
For any fixed positive lag ell, `E_(n,ell)` is bounded above by the sum
of the two endpoint chord distances to 1. Hence its cumulative energy
is `O_(h,ell,m)(log N)`. Applying the parent finite-exponent no-wrap lower
bound to beta_m proves

\[
\boxed{\sum_{n<N}E_{n,1}(h,s_m)=\Theta_{h,m}(\log N),\qquad
N-|S_N(h,s_m)|=\Theta_{h,m}(\log N).}                 \tag{10}
\]

For the second assertion the lower bound is the parent variance inequality;
the upper bound follows from `N-|S_N|<=|N-S_N|` and (9).
Thus the logarithmic scale is **optimal** for the entire finite-exponent +
original-summable-source-error argument. No improvement to `omega(log N)`
can follow from those hypotheses alone. A stronger theorem for authentic
pi must use an additional selected arithmetic property.

## DP-04/05. Sharp window scale, simultaneous frequencies, periodic targets

For each j, throughout the integer window

\[
A=m^j+1\le n\le B=m^{j+1}-2,
\]

all already completed sparse digits are integers, and the remaining
homogeneous lag phase has distance at most `1/256`. Equation (1) therefore
bounds the actual original-forcing lag distance at h=1 by

\[
\|U_{n+1}(s_m)-U_n(s_m)\|
\le\frac1{256}+\frac{16}{(8A+1)^3}<\frac1{20}.         \tag{11}
\]

The final inequality holds already for A>=1. The window length divided by
its starting time tends to `m-1=mu(beta_m)-1`. Consequently the strict
`kappa>mu(beta)-1` in the parent no-wrap theorem is sharp as a general
finite-exponent statement: any smaller multiplier fails for this family.
These are all-index analytic bounds, not extrapolation from a finite sample.

For any fixed finite set of frequencies and lags, (9) still bounds the sum
of all their lag energies by O(log N). Thus finitely many simultaneous
frequency or lag tests do not repair the finite-exponent barrier.

Rational translations preserve irrationality exponent and integer-base
normality. Set `gamma=beta_3+1/17` and `s=(gamma-pi)/16`. Since
`16=-1 mod17`, the limiting orbit measure is supported on `{1/17,16/17}`,
with equal weights. Equation (9), after multiplying by the corresponding
periodic phase, proves

\[
\frac{S_N(h,s)}N\longrightarrow\cos(2\pi h/17),
\quad
\frac1N\sum_{n<N}E_{n,1}(1,s)\longrightarrow1-\cos(4\pi/17)>0. \tag{12}
\]

Lag-two energy is only O(log N), and `mu(gamma)=3`. This is a finite-exponent,
original-forcing **positive-density lag-one slip control that is nonnormal**.
It refutes treating positive lag-one energy alone as a normality certificate.
More generally, adding a fixed rational with denominator coprime to 16 gives
an asymptotic finite periodic orbit and logarithmic deviation from that
periodic template. This is not a counterexample to rational-translation
preservation of normality: beta_3 was already nonnormal.

**Historical wording correction.** PR #403's README says its theorem also
holds for rational translations “of that seed” immediately after naming the
coherent seed `-pi/16`. Read literally this is false: such translations make
beta rational, and e.g. a translation by `1/15` retains coherent lag phase.
Its THEOREMS.md correctly applies the theorem to rational translations of
the authentic seed `s=0`, equivalently rational translates of pi. The
historical file is untouched; this paragraph records the precise correction.

## DP-08. Even bounded partial quotients do not break the barrier

The classical endpoint `m=2` is stronger than merely finite exponent.
Jeffrey Shallit, *Simple continued fractions for some irrational numbers*,
J. Number Theory 11 (1979), 209–217, proves the folding law and bounded
partial quotients in Theorems 1, 8 and 9. We checked the
[author-hosted primary paper](https://cs.uwaterloo.ca/~shallit/Papers/scf.pdf).
For base 16, the continued fraction of
`beta_2=sum_(j>=0)16^(-2^j)` has partial quotients at most 18. The law starts
with `[0;15,17]` and replaces an even-index ending `[a0;...,an]` by

\[
[a_0;\ldots,a_{n-1},a_n+1,a_n-1,a_{n-1},\ldots,a_1].
\]

Standard continued-fraction best-approximation inequalities then give
`abs(beta_2-p/q)>1/(20q^2)` for every rational p/q with q positive: choose
consecutive convergent denominators `q_k<=q<q_(k+1)`; the approximation
error numerator is at least that of the k-th convergent, greater than
`1/(q_k+q_(k+1))`, and `q_(k+1)<19q_k`. Thus `mu(beta_2)=2`.

All digit-budget and coherence arguments (8)–(11) hold unchanged at m=2.
Consequently the original-forcing seed `s_2=(beta_2-pi)/16` is badly
approximable at its selected beta, yet has `S_N(h,s_2)/N -> 1` and
`N-|S_N(h,s_2)|=Theta_h(log N)`. This is a **classical-input countermodel**,
not a new irrationality theorem. Even proving exponent two, or bounded
partial quotients, for pi would not by itself turn the Green-transport
argument into positive-density dispersion. Additional arithmetic is needed.
The folding-versus-Euclidean calibration verifies 36 finite cases and three
whole coherent windows; it is not the authority for the infinite classical
statement.

## Formal and analytic boundaries

`NoWrap.lean` proves denominator-cleared integer no-wrap and finite iteration
for arbitrary positive integer denominator. It was compiled by Lean 4.14.0,
with only `propext` and `Quot.sound` reported. There are no `sorry`s or added
axioms. It does **not** formalize real nearest-integer residues, the published
irrationality result, Green analysis, or the theorems (2)–(12). The initial
compiler error and source snapshot are retained separately.

The uniform growing band is a genuine extension of the parent selected theorem,
but still transfers Diophantine information through the source error budget.
The exact countermodel demonstrates why this method cannot supply positive
density at fixed frequency. It leaves open which additional property of the
original rational zero-seed arithmetic controls the actual CRT cofiber.
