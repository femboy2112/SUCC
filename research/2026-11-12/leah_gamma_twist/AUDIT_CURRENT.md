# Adversarial audit: centered-current rate control and target interpolation

Date: 2026-11-12. Scope: read-only review of `HOSTILE.md`,
`HOLOGRAPHIC.md`, `observational_succ/leah_gamma_twist.py`, and
`tests/test_leah_gamma_twist.py`. Only this audit file was written by this
review pass. The reviewing agent is from the same model family; this is
separate-method verification, not external refereeing or formal proof.

## Verdict

The centered-current implementation matches the definitions and finite
inequalities in `INVERSE_R0.md`. The sparse logarithmic impulse construction
in HOSTILE H10–H12 survives the off-by-one audit and an additional exact
integer check. Its seed is explicitly different from zero, and no proof of
R0 for the authentic source is supplied or implied.

The quadratic interpolation theorem and its continuous-seam estimate are
valid. One sentence in HBT-04 overstates the endpoint pair's gap as the
unqualified ambiguity supremum. The counterexample and minimal repair are
recorded below. The claimed asymptotic quadratic order survives that repair.

## 1. HOSTILE H10–H12: pulse locations and waiting times

The pulses begin at `t_1=16`, with
`t_(j+1)-t_j=ceil(log_16 t_j)`. They are strictly increasing because the
gap is at least one; the exceptional first gap is exactly one. For
`t_j<=n<t_(j+1)`, the next future pulse is `t_(j+1)`, including when `n`
is itself a pulse. Therefore

\[
1\le t_{j+1}-n\le\lceil\log_{16}t_j\rceil
\le\lceil\log_{16}n\rceil.
\]

There is no pulse-at-the-current-clock off-by-one in `S_n`: its definition
uses `t_j>n`, while `C_n` uses `t_j<=n`. The geometric sum bound
`S_n<=1/15` follows because future differences are distinct positive
integers. The original Green tail satisfies `0<T_n<x<1/2`, so
`S_n-T_n` is strictly between `-1/2` and `1/2`. Thus the nearest integer
of `U_n(s)` really is `C_n`, and its current is one precisely at pulse
times. This conclusion does not assume anything about the distribution of pi.

The single next pulse gives

\[
S_n\ge16^{-\lceil\log_{16}n\rceil}\ge(16n)^{-1},
\]

so H10 is valid at every `n>=16`. It is incompatible with the negative
Green profile even at an individual sequence of late clocks.

For the interior pulse count `K_B=# {B< t_j <2B}`, consecutive included
pulses are at least `log_16 B` apart. Hence
`K_B<=B/log_16 B+1`. Every gap intersecting the shell has its left pulse
at most `2B`, so its length is at most `ceil(log_16(2B))`.
The endpoint penalty of two in H11 is safe (one can obtain a slightly
stronger lower endpoint count). Thus both H11 bounds hold for every
integer `B>=16`.

H3 has a coefficient bounded below away from zero at late B, and H4
has only `O(1/B)` endpoint loss. Combining them with H11 correctly gives
`A_B=Theta(1/log B)`. This refutes replacement of the H7 premise by
`A_B=O(1/log B)` or merely `A_B->0`.

**Authentication audit.** The seed `beta-x` is nonzero because
`beta<1/16<x`. This is a single fixed same-forcing changed seed, not
a second trajectory obeying the exact original seed. The manuscript
preserves this distinction. H12 therefore kills a source-blind inference,
not R0 for pi.

## 2. Other HOSTILE endpoint checks

* H3 sums only interior edges `B<=n<=2B-2`; each residual vertex is
  used at most twice. The source monotonicity supplies
  `|a-r(n+1)|>=1-r(B+1)` at a nonzero integer impulse.
* H4 includes the possible impulse at `2B` through `K_B+1` and pays
  all future impulses. The latter convolution weight is exactly
  `(1-16^(-B))/225`, yielding its printed `3375=15*225` denominator.
* H6 discards the last L starting clocks. For every retained clock,
  its L-step future ends at most at `2B-1`, so all relevant pulses
  belong to the stated interior count. The bound `L(K_B+1)` is valid.
* H7 uses a fixed power p before taking the shell limit. Its
  `A_B log B->0` assumption is retained. No inference from bare
  failure of R0 to this stronger rate is made.
* H9 uses `T_(2B)<1/(256B^2)` and
  `sum_(n=B)^(2B-1) 16^(2(n-2B))=(1-16^(-2B))/255`.
  The resulting denominator `8355840=255*65536/2` is correct.

## 3. HOLOGRAPHIC interpolation and a localized counterexample

HBT-01 has the correct constant. The target function is
`f(y)=e(hy/16)`, so `sup|f''|=pi^2 h^2/64`; the linear interpolation
error over a cell of width `1/q` is at most that value divided by
`8q^2`. The complex-valued result follows from the integral remainder
and the triangle inequality. Each barycentric channel coefficient has
modulus one, giving the stated norm-one l1 reconstruction estimate.
The manuscript correctly warns that converting unscaled moments to
barycentric channels can amplify their errors by q.

HBT-02 is also valid: translation by an integer c on the interpolation
grid obeys `P(c+y)=e(hc/16)P(y)`. Thus its contracted kernel agrees with
the actual carry/arrival summand, including the seam. Its slope bound is
`16*(2q|sin(pi h/(16q))|)<=2pi|h|`. The source correction sign is correct.
HBT-03 pays the completed-tail error explicitly and labels the fixed-q
signed response estimate as OPEN.

**Finding AC-01 — false without a frequency/resolution restriction.**
HBT-04 originally said that the endpoint/midpoint gap
`1-cos(pi h/(16q))` is “the ambiguity supremum” for the half-open cell.
For `q=1,h=32`, take

\[
\mu=\tfrac12(\delta_{1/4}+\delta_{3/4}),\qquad
\nu=\delta_{1/2}.
\]

Both have mass one and first moment one half in the cell `[0,1)`.
But `f(y)=e(2y)` has integrals `-1` and `1`, a gap of **2**.
The printed endpoint/midpoint expression is `1-cos(2pi)=0`.
Symmetric pairs approaching the cell endpoints have gap tending to
zero; they do not maximize this high-frequency ambiguity.

**Minimal repair:** replace the supremum sentence by “the strictly
interior symmetric pairs approach this displayed endpoint gap.”
Alternatively state and prove a suitable small-cell/fixed-frequency
restriction. The existing `q->infinity` argument with fixed nonzero h
still gives an Omega(`q^-2`) ambiguity and refutes uniform error
`o(q^-2)`. Its asymptotic-order conclusion and HBT-01 do not depend
on the false global-supremum wording. No minimax constant is established.

## 4. Root implementation audit

`centered_path` updates the exact residual with
`raw=16*residual+forcing(n)` and then subtracts `floor(raw+1/2)`.
Since the unwrapped prior nearest integer is integral, this is exactly
`a_n=J_n-16J_(n-1)`, with no discarded winding. The stored seed and
the separately documented initial anchor retain source authentication.
`impulses[0]` is an anchor convention, not a dynamical pulse included
in shell statistics.

`shell_metrics` uses residual indices `[B,2B)` and pulse indices
`[B+1,2B]`, matching INVERSE_R0's energy convention. HOSTILE's K is
instead an **interior count** through `2B-1`; those two notes must
not silently substitute their K notation for each other. The current
implementation and tests use the INVERSE_R0 convention consistently.

The source-error budget uses `16r+r^2`, valid because every pulse in
these shells occurs at clock at least two and has absolute value at
most eight. The finite exact endpoint constants are 15/4 and 17/4.

`shell_antilock_interval` uses the existing rational Machin/Taylor
character enclosure. Its tail payment `8*source_tail_budget(n)` is
safe because `2pi<8`; clipping each loss interval to `[0,2]` is valid.
The result concerns the completion `x+seed`, as its docstring states.
It is a finite certificate, not an asymptotic test.

`silent_response` implements the exact finite recurrence, including
zero-length windows and the terminal residual. The unit tests include
a separately evaluated four-pole unwrapped recurrence, endpoint-term
mutations, source-correction mutation, rational aliases, coherent
rational terminal seeds, finite interval loss bounds, and domain guards.

No source-zero overclaim was found in the code or the eight tests.

## 5. Executed checks

Ran:

```
python -m unittest tests.test_leah_gamma_twist
```

Result: **8 tests PASS**, reported runtime 0.183 seconds.

An additional exact integer/Fraction check covered:

* every `n=16,...,16384`: correct next-pulse distance and
  `16^(-distance)>=1/(16n)`;
* every shell `B=16,...,2048`, plus `4096,8192,16384`: H11's exact
  lower count and sharp upper count. For `K_B>1`, the latter was
  tested without floating logarithms via the equivalent integer
  comparison `B^(K_B-1)<=16^B`.

Output: **36,810 exact checks PASS**, including **2,036 shell-count
cases**. These finite tests supplement the all-index proofs above.
The AC-01 counterexample uses only exact roots of unity and needs no
floating phase evaluation.

At the time of this audit the source module SHA-256 was
`adfa76505eb6c5e995012f94447db484c0925455ade6953101f6419df429f596`,
and the test module SHA-256 was
`c1a86679adc15a23815a9e7dc8d1bfc62d830d9cb259beeb525cdb35cf6aa07c`.
Subsequent revisions require their own exact-head checks.

## 6. Remaining proof debt

No all-large-shell lower bound on the authentic centered-current density
has been derived. The source profile can be followed by wrong-seed
controls, and its fixed-order jets do not rule out those controls.
The interpolation instrument preserves the desired signed contraction
but does not estimate it. R0 and normality remain OPEN.
