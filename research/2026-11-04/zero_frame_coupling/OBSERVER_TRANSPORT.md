# Observer inversion and the sharp boundary that remains

Four operations must be kept separate: a common gauge translation, changing
sampling weights, changing chronological labels, and changing the source.
The first preserves a properly transported character exactly. The second
needs a change-of-measure estimate. The third needs actual source values at
the declared times. The fourth is a countermodel or a different theorem.

For arbitrary complex samples v_n and reciprocal weights `w_n=8A^3/(3n^3)`,
the sharp maximal norms obey the **optimal finite operator bounds**

\[
M_w(v)\le\tfrac83M(v),\qquad
M(v)\le\tfrac38(2-1/A)^3 M_w(v)\le3M_w(v).
\]

These follow from exact discrete summation by parts; both endpoints and all
weight increments are paid. Endpoint-supported data show the constants are
optimal. Thus the reciprocal Jacobian can be inverted with constant cost
if a bound controls **every** subinterval. The parent sinc zero controls
only the full interval. This is the precise difference.

For any fixed nonzero complex C² weight w, put
`B_w=max_(1<=x<=2) x^3|w(x)|`. Uniform two-step integration by parts and a
local half-turn give

\[
\max_{1\le a<b\le2}\left|\int_a^b w(x)e(-c\Lambda/x^2)dx\right|
=\frac{B_w}{2\pi|c|\Lambda}+O_{w,c}(\Lambda^{-2})
\quad(c\ne0).
\]

For the unchanged four-pole forcing with coherent wrong seed, keeping the
genuine radial channel and any fixed integer lag ell,

\[
\Lambda_A M^{*,w}_{A,\ell}(H_A(h))
\longrightarrow\frac{32B_w}{\pi|2\ell+1|}>0
\quad\text{for every fixed }h\ne0.
\]

This includes nonzero smooth compact tapers: their full-epoch integral may
lose every endpoint term, but their maximal subinterval integral has the
displayed nonzero constant. For reciprocal weight the relative-radial maximum
has limit `128/(3 pi |ell|)` after multiplication by Lambda, even along the
tuned whole-window zeros. [All proofs and error regimes](front_be/PROOFS.md).

These are sharp counterexamples to a universal transfer from a scalar
retimed/tapered zero to the original maximal saving. They do not refute a
new source-selected correlation estimate. Fixed-h lag transport still costs
only O_(h,ell)(1) on full prefix sums, as #506 proves; the unknown fixed-h
Weyl limit is preserved, not computed.

Causality is explicit: a positive lag uses a later radial state. It is a
retrospective observation or a report with delay, not future access at the
earlier time. No metric or spacetime symmetry has been introduced.

## Sharp order of the phase-undoing loss

This additional operator statement makes the loss unavoidable for arbitrary
complex data, while leaving the original source-selected possibility open.
Put `B(n)=P_n(E)Z_n=-r_o(n)+epsilon_n(n)`,
`v_n=e(H_AB(n))`, and define the multiplier norm

\[
\mathcal N_A=\sup_{M(f)>0}\frac{M(vf)}{M(f)}.
\]

At the original critical schedule,

\[
\left(\frac{15\pi}{256}+o(1)\right)\Lambda_A
\le\mathcal N_A\le
1+\left(\frac{45\pi}{128}+o(1)\right)\Lambda_A.
\]

For the upper bound apply exact summation by parts and BE-04's total
variation. For the lower bound choose the explicitly declared data
`f_n=conjugate(v_n)`. Its product with v is identically one, so M(vf)=1.
The positive joint jet theorem and
`r_o(n)=15/(64n^2)+O(n^-3)` give uniformly on the epoch
`f_n=e(15 Lambda_A/(64(n/A)^2))+O(Lambda_A/A+H_A(4sigma)^-A)`.
BE-02, with w=1 and c=-15/64, then gives

`M(f)=256/(15 pi Lambda_A)+O(Lambda_A^-2+Lambda_A/A+H_A(4sigma)^-A)`.

Since `Lambda_A~log A`, the error is o(1/Lambda_A); inversion proves the
lower bound. This establishes the optimal **order** Theta(Lambda_A), not
an exact leading operator norm. The chosen f is adversarial observer data,
not a claim that the genuine angular stream equals this compensator. A better
bound restricted to the original stream would need new arithmetic information.
