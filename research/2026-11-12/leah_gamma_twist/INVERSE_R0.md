# Inverse R0: an exact rational boundary current and its Green shadow

Baseline: Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`.
Status: **PROVED LOCAL** for the elementary finite inequalities below; **OPEN**
for every all-large-shell positive-density assertion about the authentic orbit.
The new material is a quantitatively stable, carry-only realization of R0 and a
source-scale consequence of sufficiently rapid locking. It is **not an arithmetic
saving**, and worldwide novelty is not claimed.

## 1. What the backward attack found

The Main XXV archive already establishes:

* R0 is equivalent to positive lower shell density of binary digit changes
  (`frontier_rungs/LIMIT_FACES.md`, LMF-03).
* R0 requires a radix-restricted exponent below 1, but a restricted exponent of
  zero does not imply R0 (LMF-03, ZSC-01, ZSC-05).
* Literal floor-carry changes represent the stronger hexadecimal-change rung
  after paying an `O(1/log B)` seam error (ZSC-03 in
  `innovation_arithmetic_decoupling/CARRY_FLUX.md`).
* Centered carries already occur for **pairs of nearby states** in DBT-09/12.

The comparison below instead uses the centered carry of the **single original
rational trajectory**, targets R0 directly, and needs no real-digit seam test.
It exploits the stable inverse of `16 - shift`, not a new dynamical hypothesis.

## 2. Exact observable and hypotheses

Keep the four-pole source and literal seed:

\[
U_0=0,\quad U_{n+1}=16U_n+r(n+1),\quad
r(m)=\frac{120m^2-89m+16}{(2m-1)(4m-1)(8m-7)(8m-3)}.
\]

For each integer `n >= 0`, set

\[
J_n=\lfloor U_n+\tfrac12\rfloor,\qquad
\epsilon_n=U_n-J_n\in[-\tfrac12,\tfrac12),\qquad
a_{n+1}=J_{n+1}-16J_n\in\mathbb Z.
\]

These are exact rational/integer operations. `J` is **not** the archive's literal
floor carry `C`; `a` is a new notation for a different observable. In particular
the old convention retaining literal carry 16 is unchanged.

For every integer `B >= 1`, define

\[
E_B=\sum_{n=B}^{2B-1}\epsilon_n^2,\quad
K_B=\sum_{n=B}^{2B-1}a_{n+1}^2,\quad
R_B=\sum_{n=B}^{2B-1}(a_{n+1}-r(n+1))^2,
\quad d_B=\frac{\#\{B\le n<2B:a_{n+1}\ne0\}}B.
\]

`K_B` is a nonnegative integer obtained from the full original rational state.
It retains the old-prime cofactor and ordered integer winding implicitly through
`J_n`; no prime projection or independent CRT sampling enters.

The algebra below also holds for every real initial seed with this same forcing.
The constants do not establish selection: the source-specific open question is
their application to `U_0=0`.

There is an exact boundary response, not merely a bound:

\[
\epsilon_n+T_n=\sum_{j\ge1}16^{-j}a_{n+j}.                       \tag{0}
\]

To prove it, telescope the recurrence to depth `L` and let `L` grow; the
remaining term `16^(-L) epsilon_(n+L)` tends to zero. For the original seed,
`J_0=epsilon_0=0`, so `x=sum_(j>=1)16^(-j)a_j`. The bounded current is
therefore an exact source-derived signed radix response. Its ordering is
essential. Replacing it by magnitudes, frequencies, or a prime marginal
discards the signed convolution in (0). This identity is still a coordinate
representation; it does not estimate those frequencies.

## 3. LGT-R0-01: finite spectral coercivity, with exact endpoints

Put `Delta_B = epsilon_(2B)^2 - epsilon_B^2`. Then, exactly,

\[
\begin{aligned}
R_B&=225E_B+16\sum_{n=B}^{2B-1}(\epsilon_n-\epsilon_{n+1})^2-15\Delta_B,\\
R_B&=289E_B-16\sum_{n=B}^{2B-1}(\epsilon_n+\epsilon_{n+1})^2+17\Delta_B.
\end{aligned}
\]

Consequently

\[
225E_B-\frac{15}4\ \le R_B\le\ 289E_B+\frac{17}4.                 \tag{1}
\]

**Proof.** The source recurrence gives
`a_(n+1)-r(n+1)=16 epsilon_n-epsilon_(n+1)`.
Expand its square and use
`sum epsilon_(n+1)^2 = E_B + Delta_B` in each displayed expression. Finally
`|Delta_B| <= 1/4`. The bulk constants are `(16-1)^2` and `(16+1)^2`.
They are sharp for unrestricted bounded residual sequences: constant and
alternating residuals attain the respective bulk values. Sharpness is **not**
claimed within the authentic BBP orbit. ∎

The original source satisfies, for every integer `n >= 1`,

\[
0<r(n+1)<\frac{15}{64n^2},\qquad 0<T_n<\frac1{64n^2}.             \tag{2}
\]

The first upper bound follows by subtracting the rational functions: its
numerator is `5696n^3+7672n^2+2910n+225`, over the positive denominator
`64n^2(2n+1)(4n+3)(8n+1)(8n+5)`. The tail bound follows from
`T_n < r(n+1)/15`, already established in the source contract.

Since `16 epsilon_n-epsilon_(n+1)` lies strictly between `-8.5` and `8.5`
and `r(n+1)<15/64`, the integer `a_(n+1)` lies in `[-8,8]` for `n >= 1`.
In particular

\[
Bd_B\le K_B\le64Bd_B.
\]

Moreover, with

\[
\delta_B=\frac{15}{4B}+\frac{225}{4096B^3},
\]

\[
|R_B-K_B|\le\delta_B.                                          \tag{3}
\]

Indeed the summand difference is bounded by `16r+r^2`; summing (2) with
`n >= B` gives (3). These constants deliberately favor a short exact proof over
optimizing every finite endpoint.

## 4. LGT-R0-02: R0 as source-selected integer-current energy

Let `x=pi/16`, `Y_n=16^n x=U_n+T_n`, and

\[
\mathcal A_B=\frac1B\sum_{n=B}^{2B-1}(1-\cos(2\pi Y_n)),\qquad
\tau_B=\frac{\pi}{32B^2}.
\]

For every integer `B >= 1`,

\[
\boxed{
\frac8{289B}\left(K_B-\frac{17}4-\delta_B\right)-\tau_B
\ \le\ \mathcal A_B\ \le\
\frac{2\pi^2}{225B}\left(K_B+\frac{15}4+\delta_B\right)+\tau_B.}
                                                                    \tag{4}
\]

**Proof.** For `|t| <= 1/2`,
`8t^2 <= 1-cos(2 pi t) <= 2 pi^2 t^2`.
The original rational orbit's mean loss therefore lies between `8E_B/B`
and `2 pi^2 E_B/B`. Combining (1) and (3) bounds `E_B` above and below.
Finally the cosine is `2 pi`-Lipschitz and (2) gives
`|A_B - B^(-1) sum(1-cos(2 pi U_n))| <= 2 pi max T_n <= tau_B`.
No discontinuous nearest-integer operation is transported across the tail. ∎

Thus, with every limit over integer `B -> infinity`,

\[
\boxed{
\mathrm{R0}\ \Longleftrightarrow\ \liminf_B K_B/B>0
\ \Longleftrightarrow\ \liminf_B d_B>0.}                         \tag{5}
\]

The exact missing arithmetic assertion can now be stated without pi, a real
phase, a tail oracle, or an asymptotic reconstruction operator:

> There exist `c>0` and `B_0` such that for every integer `B>=B_0`, the original
> rational recurrence has `J_(n+1) != 16J_n` at at least `cB` clocks
> `B<=n<2B`.

**Novelty tax:** (5) is an equivalent reformulation, not a proof step toward its
truth. The useful new instrument is (4): explicit stable conditioning,
`O(1/B)` endpoint error, `O(1/B^2)` source error, and a carry-only certificate.
It improves the interface, not the known statistical order. Unlike a generic
positive Gram object, this particular positive energy has a proved two-sided
comparison with the target. Its lower bound is still unproved.

## 5. LGT-R0-03: sparse current forces a quantitative Green shadow

For every integer `1 <= L <= B`, all but at most

\[
L(1+K_B)
\]

clocks `n` in `[B,2B)` satisfy

\[
|\epsilon_n+T_n|
\le16^{-L}\left(\frac12+\frac1{64B^2}\right).                   \tag{6}
\]

At those same clocks,

\[
\boxed{
\left|n^2\epsilon_n+\frac1{64}\right|
\le (2B^2+\tfrac1{16})16^{-L}+\frac1{30B}.}                    \tag{7}
\]

**Proof.** Exclude the final `L` clocks and each `n` for which some
`a_(n+j) != 0`, `1<=j<=L`. A nonzero current excludes at most `L` values
of `n`, and their number is at most `K_B`. On the surviving clocks, the
recurrence telescopes to

\[
\epsilon_n+\sum_{j=1}^{L}16^{-j}r(n+j)=16^{-L}\epsilon_{n+L}.
\]

Add the exact omitted tail `16^(-L) T_(n+L)` to obtain (6).

For (7), first note `r(m)>15/(64m^2)` for every integer `m>=1`.
The numerator of the difference, expressed in `k=m-1>=0`, is
`9664k^3+19336k^2+12770k+2783`, over a positive denominator. Using
`(1+u)^(-2)>=1-2u` gives

\[
\frac1{64}-\frac1{30n}
\le \frac{15}{64}\sum_{j\ge1}16^{-j}\frac{n^2}{(n+j)^2}
<n^2T_n<\frac1{64},
\]

because `sum j16^(-j)=16/225`. Multiply (6) by `n^2<=4B^2` and use this
tail bound. ∎

**Rate-sensitive consequence.** If a sequence `B_i -> infinity` satisfies
`A_(B_i) log B_i -> 0`, then for every fixed `delta>0`, choosing
`L_i=ceil((2+delta)log_16 B_i)` shows

\[
n^2\epsilon_n\longrightarrow-\frac1{64}
\quad\text{in probability under uniform clocks }n\in[B_i,2B_i).
\]

Indeed (4) gives `K_B/B <= (289/8) A_B + O(1/B)`, so the exceptional
fraction is `O(L A_B+L/B) -> 0`, while the right side of (7) tends to zero.
The stronger assumption **must be retained**: mere failure of R0 only gives
`A_(B_i)->0` and does not imply `A_(B_i) log B_i ->0` along any subsequence.

This identifies the source-specific profile a rapidly coherent shell would
have to emulate: the actual bounded negative Green solution. Its coefficient
`-1/64` comes from the four-pole cancellation, `n^2 r(n)->15/64`, and the
reverse geometric sum `sum 16^(-j)=1/15`. It is not an independent Gamma
randomness assumption.

## 6. A weaker prospective arithmetic theorem

**OPEN, not proved:** there exist `eta,delta>0` and `B_0` such that for every
integer `B>=B_0`, at least `eta B` clocks in the shell satisfy

\[
|n^2\epsilon_n+1/64|\ge\delta.                                  \tag{H}
\]

Choosing `L=ceil(log_16(8B^2/delta))` in (7), for sufficiently large `B`,
would imply

\[
K_B\ge\eta B/L-1,\qquad
\mathcal A_B\ge\frac{8\eta}{289L}-O(1/B).
\]

This would be a source-selected `1/log B` shell saving, still weaker than R0
and stronger than the inherited logarithmic absolute loss on prefixes.
It isolates an independently formulable source-scale exclusion question; no
proof of (H) follows from source positivity, pole complexity, irrationality,
or the inequalities in this note. Finite exact rational intervals can test it,
but cannot establish its all-large-shell quantifier.

The direct R0 target (5) remains preferable if its integer-current density can
be bounded. A framework that only rewrites that density buys no arithmetic
advance.

## 7. Hostile receipts and boundary of the attempted contradiction

* **Same-forcing coherent seed `s=-x`:** `U_n=-T_n`, `|U_n|<1/2` for all
  `n>=0`, hence `J_n=a_n=0`. It saturates the Green-shadow profile, fails
  (H), and has `A_B=0`. Thus no source-blind positive-current theorem is
  possible. The exact zero seed must enter the missing density proof.
* **Rational alias `s=1/16`:** `J_n(s)=J_n(0)+16^(n-1)` for `n>=1`.
  Therefore `a_n(s)=a_n(0)` for `n>=2`; later currents do not authenticate
  the seed. Retain `U_0=0`, not just later current observations.
* **Finite coherent rational controls `s=-P_M`:** for `0<=n<=M`, the
  state is a negative finite Green tail of magnitude below `1/2`, so
  `J_n=a_n=0` through `M`. They refute finite-horizon source-only
  authentication claims; they do not refute the fixed original zero seed.
* **Periodic nonnormal completions:** the finite energy inequalities remain
  valid; positive current density can establish only R0, not normality.
  For instance the completed fixed point `1/15` has R0 but is nonnormal.
* **Slow coherent shells:** sparse digit constructions in LMF-03 already
  show that restricted exponent zero is compatible with failure of R0.
  Nothing here replaces the missing medium-scale arithmetic estimate.

The contradiction campaign stops at a demonstrated proof-pathway gap:
`a` is an exact source-preserving observable with stable inversion, but no
known argument forces its positive lower density for the literal zero
source. There is no pair of different fully authenticated exact trajectories:
the recurrence and seed determine one trajectory. Countermodels necessarily
relax the seed, source, or available observation contract.

## 8. Verification contract

The root's integrated probe should check (1), (3), (4), (6), and (7), with
original rational source and seeds `0`, `1/16`, `1/7`, and `-P_M`.
Use fresh shells `{37,73,149,293}` in addition to small calibrated shells.
Exact rational identities verify the current and endpoint algebra; certified
tail/cosine intervals are needed for certified phase-loss bounds. A floating
cosine check is only an observation.

Mutations to reject: drop the endpoint term; replace `a-r` by `a` as an
exact identity; infer (7) from `A_B->0` without its logarithmic rate; assert
that every positive source has positive current density; authenticate the
seed from currents after clock 1.

Same-model derivation and computation are method triangulation, not an
independent mathematical referee or a formal-kernel proof.
