# From the geometric source clock to the expanding Fourier observer

**Status: PROVED PAPER.** This is a quantitative comparison theorem. It does
not prove signed cancellation. It is independently checked in
`IMPLEMENTATION_CONFORMANCE.md`; `observer_probe.py` checks 18 rational
majorants as finite regression controls.

## 1. Named source and observable

Let `I_k=A_k([3,4])` be the circle-derived beta interval from
`LR_TRANSLATION.md`, with width

$$
W_k=\prod_{j=1}^k\frac{j}{2j+1}<2^{-k}\quad(k\ge1).
$$

Its rational midpoint is

$$
x_k=A_k(7/2)=2\sum_{n=0}^{k-1}W_n+\frac72W_k.
$$

The strict enclosure gives

$$
|\pi-x_k|<\delta_k:=W_k/2<2^{-k-1}.
$$

Keep the precise epoch and clock convention

$$
E_{A,h}(x)=\frac1A\sum_{n=A}^{2A-1}e(h16^{n-1}x),\qquad
e(y)=\exp(2\pi i y),
$$

for integers `A>=1` and `h`. The argument of `e` is in turns. It is not a
geometric radian coordinate on the original unit circle.

## 2. Quantitative theorem

For integers `A>=1`, `s>=0`, and nonzero integer `h`, set `k=8A+s`. Then

$$
\boxed{|E_{A,h}(\pi)-E_{A,h}(x_{8A+s})|
<\frac{|h|}{60A\,2^s}.}
$$

For `h=0`, the difference is exactly zero.

**Proof.** The derivative bound for a circle character gives

$$
|e(u)-e(v)|\le2\pi|u-v|.
$$

Apply it term by term and sum the geometric progression:

$$
|E_{A,h}(\pi)-E_{A,h}(x_k)|
\le\frac{2\pi|h|\delta_k}{15A}
       (16^{2A-1}-16^{A-1}).
$$

The geometry-derived bound `pi<4` and the strict interval width imply

$$
|E_{A,h}(\pi)-E_{A,h}(x_k)|
<\frac{4|h|}{15A}\,2^{-k}\,2^{8A-4}
=\frac{|h|}{60A}\,2^{8A-k}.
$$

Substitute `k=8A+s`. No pi digits, phase samples, normality assumption or
statistical fitting appears in this derivation. Using the different clock
`16^n` instead of `16^(n-1)` multiplies the displayed budget by 16.

The count `8A+s` is a sufficient number of source factors. It is not a claim
of linear bit complexity, linear memory, or an optimal runtime: the exact
integer registers grow, and arithmetic on them costs time.

## 3. Preserve the original zero seed and future tail

The pinned repository source is

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

Its established Green completion is

$$
U_n+T_n=16^{n-1}\pi,\qquad
0<T_n<\frac1{(8n+1)(8n+2)}.
$$

For `c_A(h)=A^(-1) sum_(n=A)^(2A-1) e(h U_n)`, the same Lipschitz bound,
`n>=A`, and `pi<4` give

$$
|c_A(h)-E_{A,h}(\pi)|
<\frac{8|h|}{(8A+1)(8A+2)}\quad(h\ne0).
$$

Consequently

$$
\boxed{|c_A(h)-E_{A,h}(x_{8A+s})|
<\frac{|h|}{60A\,2^s}
 +\frac{8|h|}{(8A+1)(8A+2)}.}
$$

The source and tail identity are imported from the
[pinned frontier](https://github.com/femboy2112/SUCC/blob/964768cd1fa5116f521625abfaaad8d8fab0f222/docs/PI_NORMALITY_FRONTIER.md)
and the preceding round's
[exact source bound](../cursed_categorical_computation/round_iii_dedekind/COMPUTATION_GRAPH.md).
They retain the original zero seed. For another seed `z`, the completed value
is `16^n(z+pi/16)`; silently retaining this theorem's midpoint target would be
wrong. In particular `z=-pi/16` yields the constant completed orbit zero.

## 4. What this makes available, and what it leaves unpaid

For each fixed `h` and fixed `s`, the transport error tends to zero. Thus a
separately proved cancellation estimate for the specific moving rational
averages `E_(A,h)(x_(8A+s))` would transfer to the original source.

This is a computable rational family with an explicit factorial/matrix
description, rather than an unspecified real approximation. That structure
may permit arithmetic arguments about the moving denominators and the
selected phases. No such cancellation estimate is derived here. Stating its
vanishing as an assumption is an equivalent reformulation of the existing
fixed-character problem after this error payment, not a proof advance on the
vanishing itself.

Digit parity is discontinuous. The displayed continuous-character estimate
cannot simply be substituted for the two-fiber parity contrast: digit
boundaries require certified margins or an additional boundary-frequency
estimate, and the authentic complement retains all prime powers, winding,
clock and future-tail data. The inherited prime-marginal hypotheses also
remain unchanged.

The next verdict-changing result would bound that selected signed quantity
uniformly for all sufficiently large integer epochs, while rejecting the
existing coherent wrong-seed controls. Finite accurate reconstruction and
an exact commuting diagram alone do not provide that bound.
