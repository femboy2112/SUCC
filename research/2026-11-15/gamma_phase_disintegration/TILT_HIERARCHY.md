# Rate-tilt resonance hierarchy: independent derivation and hostile control

## Status and source scope

The root proposed the hierarchy. A second same-model agent independently
rederived the coefficients, checked the global remainder, and ran a separate
numerical implementation. The root reviewed the proof and reran the audit. These are paper derivations and finite diagnostics, not
external peer review or a claim of global novelty.

The original source rate law `mu` is inherited from the Oily bridge. Write
`B=K+V`, with integer `K>=0`, independent `V~Uniform[0,1]`. The authentic
law has `K>=1` with weights `16^(-j)(4,4,4,2,1)` on `8j-7+i`.
Let `mu1=E B`, `m_r=E B^r`, and use angular frequency `c=2*pi*k`,
nonzero integer `k`. All general statements below assume `B>=0`.

For `a>0` and `beta>=0`, define the **chosen observer tilt**

$$
D_{a,\beta}=\mathbb E(1+B/a)^{-\beta},\qquad
\Psi_{a,\beta}(t)=
\frac{\mathbb E[(1+B/a)^{-\beta}e^{-it\log(1+B/a)}]}
{D_{a,\beta}}.
$$

The authentic BBP tail uses `a=8n` and `beta=2`. Other beta values preserve
the base rate carrier but change the observer weighting. For `beta>0`,
they also admit the chosen Gamma(shape beta) scale-mixture interpretation;
this changes the positive time kernel from its authentic shape2. At
`beta=0` there is simply an untilted rate observer, **not a positive
Gamma(shape0) density**. No changed beta may be silently identified with
the original BBP tail.

## 1. First-order hierarchy

For fixed `beta>=0`, fixed nonzero integer k, and bounded real detuning d,
assuming `E B^4<infinity`,

$$
\boxed{
a\Psi_{a,\beta}(ac+d)
\longrightarrow\frac dc-\mu_1+\frac{i(1-\beta)}c.}
\tag{T1}
$$

The convergence is uniform for d in a fixed compact interval. Indeed,
put

$$
A=cB^2/2-dB,\qquad
M=|c|B^2/2+|d|B,\qquad
N=|c|B^3/3+|d|B^2/2.
$$

The integrand has first-order expansion

$$
(1+B/a)^{-\beta}e^{-i(ac+d)\log(1+B/a)}
=e^{-icB}\left[1+\frac{-\beta B+iA}{a}\right]
+\mathcal R,
$$

with the global bound

$$
|\mathcal R|\le\frac1{a^2}
\left[\frac{\beta(\beta+1)}2B^2+\beta BM+N+\frac{M^2}2\right].
$$

The weight inequalities follow from Taylor's theorem for
`(1+x)^(-beta)` on x>=0. For the phase, use
`|exp(iy)-1-iy|<=y^2/2` and the logarithm remainders.
At a lattice frequency,

$$
\mathbb E e^{-icB}=0,\quad
\mathbb E[B e^{-icB}]=i/c,\quad
\mathbb E[B^2e^{-icB}]=2\mu_1i/c+2/c^2.
$$

Thus the first coefficient is

$$
-\beta i/c+(ic/2)(2\mu_1i/c+2/c^2)-id(i/c)
=d/c-\mu_1+i(1-\beta)/c.
$$

Normalization is controlled by

$$
D_{a,\beta}\ge(1+\mu_1/a)^{-\beta},\qquad
|1-D_{a,\beta}|\le\beta\mu_1/a.
$$

If `L_beta` is the coefficient in (T1) and `C2` is the expectation of
its displayed remainder polynomial, then the explicit normalized bound is

$$
|a\Psi_{a,\beta}(ac+d)-L_\beta|
\le\frac{(1+\mu_1/a)^\beta}{a}
\left(C_2+\beta\mu_1|L_\beta|\right).
$$

In particular at `d=mu1*c`, beta2 gives `-i/c`, beta0 gives `+i/c`,
and beta1 makes the entire first-order coefficient zero. This explains
exactly which observer change defeats the native beta2 avoided-zero
coefficient; it does not alter that coefficient under its own hypotheses.

## 2. The beta1 second-order residual

Assume `E B^6<infinity`. Fix `beta=1` and the **constant** detuning
`d=mu1*c`. Then

$$
\boxed{
a^2\Psi_{a,1}(ac+\mu_1c)
\longrightarrow
\operatorname{Var}(B)-\frac{ic}{2}\kappa_3(B),}
\tag{T2}
$$

where `kappa3(B)=m3-3*mu1*m2+2*mu1^3` is the third central moment.

For the authentic law,

$$
\mu_1=7/2,\quad m_2=55/3,\quad m_3=595/4,
$$
$$
\operatorname{Var}(B)=73/12,\qquad\kappa_3(B)=42.
$$

Consequently

$$
\boxed{
a^2\Psi_{a,1}(ac+(7/2)c)\longrightarrow73/12-21ic.}
\tag{T3}
$$

The coefficient is nonzero. Canceling the first-order native residue by
changing the observer does not make every later residue vanish.

### Independent coefficient calculation

The logarithmic phase, after removing `exp(-icB)`, is

$$
y=\frac A a+\frac H{a^2}+O(a^{-3}),
\qquad A=cB^2/2-dB,\quad H=-cB^3/3+dB^2/2.
$$

Multiply the second-order expansions of `(1+B/a)^(-1)` and `exp(iy)`.
The coefficient of `a^(-2)` is

$$
B^2\left(1-\frac{d^2}2+\frac{3id}2\right)
+B^3\left(\frac{cd}2-\frac{5ic}6\right)
-\frac{c^2B^4}8.
\tag{T4}
$$

The unit-cell moment identities, independently obtained by integration
by parts, are

$$
\mathbb E[B^3e^{-icB}]
=3m_2i/c+6\mu_1/c^2-6i/c^3,
$$
$$
\mathbb E[B^4e^{-icB}]
=4m_3i/c+12m_2/c^2-24\mu_1i/c^3-24/c^4.
$$

Together with the first two identities above, substituting `d=mu1*c`
into (T4) gives exactly

$$m_2-\mu_1^2-\frac{ic}{2}(m_3-3\mu_1m_2+2\mu_1^3).$$

The denominator does not change the second coefficient: the numerator's
constant and first-order coefficients both vanish, while
`D_(a,1)=1+O(a^-1)`.

### Global cubic remainder and explicit normalized error

Let

$$M=|c|B^2/2+|d|B,\quad
N=|c|B^3/3+|d|B^2/2,\quad
R=|c|B^4/4+|d|B^3/3.$$

The absolute integrand remainder after (T4) is at most

$$
\frac1{a^3}
\left[B^3+MB^2+B(N+M^2/2)+R+MN+M^3/6\right].
\tag{T5}
$$

To check (T5), use the exact weight remainder
`|(1+x)^(-1)-(1-x+x^2)|<=x^3`, the phase estimates
`|y-A/a-H/a^2|<=R/a^3`, `|y-A/a|<=N/a^2`, and
`|y|,|A|/a<=M/a`. The cubic exponential remainder is at most
`M^3/(6a^3)`; replacing `y^2` by `A^2/a^2` costs at most `MN/a^3`.
The remaining three terms come from multiplying the weight expansion.
All are global for B>=0, so no large-B truncation is concealed.

Writing `C=|c|`, `D=|d|`, the expectation `C3` of the polynomial is

$$
\begin{aligned}
C_3={}&(1+11D/6+D^2+D^3/6)m_3\\
&+C(13/12+13D/12+D^2/4)m_4\\
&+C^2(7/24+D/8)m_5+C^3m_6/48.
\end{aligned}
$$

If `L2=Var(B)-ic*kappa3(B)/2`, the normalized error satisfies

$$
\boxed{|a^2\Psi_{a,1}(ac+\mu_1c)-L_2|
\le\frac{1+\mu_1/a}{a}(C_3+\mu_1|L_2|).}
\tag{T6}
$$

For the authentic law the additional exact moments are

$$m_4=8551/5,\qquad m_5=149467/6,\qquad m_6=3030175/7.$$

This explicit bound can be loose, particularly for large k, but it makes
the universal remainder auditable.

## 3. Exact hostile control matching both coefficients

The first-order result is a **general unit-cell theorem**. Any such law
with the same mean reproduces it. The second-order result depends only
on the first three moments and also fails to authenticate the original
four-pole source.

A concrete positive finite-cell control demonstrates this sharply. Take

$$
\Pr(K=2)=2/3,\qquad \Pr(K=3)=1/4,\qquad
\Pr(K=11)=1/12,
$$

with an independent uniform `V`, and put `B=K+V`. Exactly,

$$\mathbb EK=3,\quad\mathbb EK^2=15,\quad\mathbb EK^3=123,$$

so this control has the **same**

$$\mathbb EB=7/2,\quad\mathbb EB^2=55/3,\quad\mathbb EB^3=595/4.$$

It reproduces both (T1) for every beta and (T3). Yet its corresponding
Green endpoint is rational:

$$
T_0^{\rm control}=\mathbb E B^{-2}
=\frac{2/3}{2\cdot3}+\frac{1/4}{3\cdot4}
 +\frac{1/12}{11\cdot12}=\frac{35}{264}.
$$

Define its own forcing by `r_control(n)=16T_control(n-1)-T_control(n)`
and its zero-seeded recurrence accordingly. Its completed orbit is
`16^n*(35/264)` and is nonnormal. In fact the harmonic `h=33` is exactly
locked to one for every `n>=1`, because
`33*16^n*(35/264)=35*16^n/8` is an integer.

This control **changes the forcing** and does not refute an assertion
that explicitly retains all four original poles. It refutes promotion
from the two spectral coefficients, even with exact zero-seed control,
to unique source selection or π cancellation.

## 4. Actual independent audit

`audit_tilt_hierarchy.py` imports no SUCC modules. It checks the symbolic
coefficient calculation and derives the unit-cell moments via integration
by parts. It also computes the authentic rate moments from the exact
geometric recurrence, and verifies the finite-cell control and its
locked harmonic.

For numerical diagnostics, it directly integrates each piecewise-constant
rate interval by its endpoint antiderivative, with 90 decimal digits and
geometric depth64. The omitted base mass is exactly `16^-64`. This is a
numerical consistency probe, not an interval certificate.

Fresh grid: `k=-2,3,7`, `n=19,113,977,8191,131071,2097143,33554393`.
The beta1 second-order observations are checked against (T6). At the
largest n, beta0,1/2,3/2,2,3 are separately checked against (T1).

Executed: **17 exact/symbolic checks and 36 numerical diagnostics passed**.
At the largest n, the beta1 scaled responses included:

| k | Computed a²Psi | Predicted limit |
|---|---|---|
| -2 | 6.08380481465 + 263.893757282 i | 6.08333333333 + 263.893782902 i |
| 3 | 6.08439456016 - 395.840635920 i | 6.08333333333 - 395.840674352 i |
| 7 | 6.08911252429 - 923.628150433 i | 6.08333333333 - 923.628240155 i |

The finite calculations do not prove the asymptotic theorem. Its
mathematical authority is the displayed globally integrable remainder.
