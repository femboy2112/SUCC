# The authentic BBP field: atomic convolution, coherent subdivision and all-order interactions

**Date:** 2026-10-29. **Pinned source:** Main XIV,
`ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc`.
**Research branch:** `research/recursive-carrier-triangle-2026-10-29`.
**Authority:** complete paper derivations below; exact executable checks are
corroboration with their own recorded scope. No Lean kernel authority or academic
priority is asserted. The original four signed BBP poles and selected condition
`U_0=0` are retained. Base-16 normality of pi and RH remain **OPEN**.

## 1. Target and relation to the author's proposed sheet

The proposed object has an actualized path, a field of remaining possibilities,
and a composition law that must update the field between path segments. A useful
faithful reading has three obligations:

1. A second segment must use the field left by the first segment.
2. Subdividing a segment and recomposing it must preserve the complete result.
3. A field interaction must be distinguished from order dependence and from an
   unproved claim about physical self-interaction.

This dossier supplies a source-derived positive model satisfying the first two
obligations, proves an exact convolution dual, and identifies interactions of
every order. It does **not** derive a random sampler whose realized output is
the selected BBP orbit. The source parameter below is the known arithmetic
source clock; the additional convolution parameter is a mathematical
subdivision parameter, not elapsed physical time or the number of BBP steps.

The prior result
[Oily positive field and Gamma cocycle](../../2026-10-26/OILY_POSITIVE_FIELD_GAMMA_COCYCLE.md)
already established the positive source density, its normalized source-time
update, the first logarithmic differential, and its Euler--Mascheroni finite
part. The new result here is the explicit factorization of that *same* density
into independent elementary summands, its convolution roots, and a strictly
nonzero connected interaction at every finite order. General normalization
cocycles and history dependence also have predecessors in
[Realized paths and field feedback](../../2026-10-26/REALIZED_PATHS_AND_FIELD_FEEDBACK.md).
Those predecessors are preserved rather than reclassified as new theorems.

## 2. The exact original source and its positive field

For integer `n>=1`, the source is

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\tag{2.1}
$$

These are precisely the four coefficients and denominators in the original
Bailey--Borwein--Plouffe identity after replacing its index `i` by `n-1`.
See Bailey, Borwein and Plouffe, *On the rapid computation of various
polylogarithmic constants*, Theorem 1, equation (1.2),
[author-hosted primary paper](https://www.davidhbailey.com/dhbpapers/digits.pdf),
*Mathematics of Computation* 66 (1997), 903--913,
[DOI](https://doi.org/10.1090/S0025-5718-97-00856-9).

For real `a>0`, define the continuous source extension

$$
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x},\qquad
R(a)=\int_0^\infty e^{-ax}Q(x)\,dx.
\tag{2.2}
$$

Since

$$
Q(x)=2(1-e^{-3x})+(1-e^{-4x})+(1-e^{-5x})>0
\quad(x>0),
$$

this gives a probability measure

$$
\mu_a(dx)=\frac{e^{-ax}Q(x)}{R(a)}\,dx,
\qquad x>0.
\tag{2.3}
$$

Termwise elementary integration of the finite sum gives

$$
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)}.
\tag{2.4}
$$

In particular, `R(8n-7)=r(n)`. All four signs in (2.1) remain in (2.4);
positivity is a derived regrouping of the exact source, not a replacement by
absolute values.

Put `L_a(s)=E_{mu_a}[exp(-sX)]` for `s>=0`. Directly from (2.3),

$$
L_a(s)=\frac{R(a+s)}{R(a)},\qquad
\frac{e^{-sx}\mu_a(dx)}{L_a(s)}=\mu_{a+s}(dx).
\tag{2.5}
$$

The authentic one-step source update is `s=8`. The unnormalized operation is
multiplication by `exp(-8x)`. Its projectivization to a probability density
requires the current-field normalizer `R(a+8)/R(a)`.

## 3. Source factorization and elementary independent atoms

### Theorem A: exact four-summand convolution representation

Define

$$
\alpha=\frac{121-\sqrt{241}}{30},\qquad
\beta=\frac{121+\sqrt{241}}{30}.
\tag{3.1}
$$

Then `3<alpha<4<beta<5`. For every real `a>0`, let the following six random
variables be mutually independent:

- `E_0 ~ Exp(a)` and `E_5 ~ Exp(a+5)`;
- `E_3 ~ Exp(a+3)` and `E_4 ~ Exp(a+4)`;
- `B_alpha ~ Bernoulli(p_alpha)` and `B_beta ~ Bernoulli(p_beta)`, where

$$
p_\alpha=\frac{\alpha-3}{a+\alpha},\qquad
p_\beta=\frac{\beta-4}{a+\beta}.
\tag{3.2}
$$

Here `Exp(c)` means rate `c`, with density `c exp(-cx)` on `x>0`.
Then

$$
\boxed{\mu_a=\mathcal L(E_0+E_5+B_\alpha E_3+B_\beta E_4).}
\tag{3.3}
$$

**Proof.** Since `1<sqrt(241)<31` and `sqrt(241)<29`, formula (3.1) gives
the claimed strict interlacing. More explicitly,

$$
\alpha-3=\frac{31-\sqrt{241}}{30}>0,
\quad4-\alpha=\frac{\sqrt{241}-1}{30}>0,
$$

$$
\beta-4=\frac{1+\sqrt{241}}{30}>0,
\quad5-\beta=\frac{29-\sqrt{241}}{30}>0.
$$

Also `alpha+beta=121/15` and `alpha beta=16`; hence

$$
15a^2+121a+240=15(a+\alpha)(a+\beta).
\tag{3.4}
$$

Both probabilities in (3.2) lie strictly between zero and one. The Laplace
transform of `B_alpha E_3` is

$$
1-p_\alpha+p_\alpha\frac{a+3}{a+3+s}
=\frac{a+3}{a+\alpha}\frac{a+\alpha+s}{a+3+s}.
\tag{3.5}
$$

The beta factor has the same formula with `(3,alpha)` replaced by `(4,beta)`.
Independence makes the transform of the sum in (3.3)

$$
\frac a{a+s}\frac{a+5}{a+5+s}
\frac{(a+3)(a+\alpha+s)}{(a+\alpha)(a+3+s)}
\frac{(a+4)(a+\beta+s)}{(a+\beta)(a+4+s)}
=\frac{R(a+s)}{R(a)}.
\tag{3.6}
$$

Uniqueness of Laplace transforms of probability measures on `[0,infinity)`
proves (3.3). The elementary transform uniqueness and convolution product
theorems are stated with proofs in Sato, *Lévy Processes and Infinitely
Divisible Distributions*, Proposition 2.6, p. 10,
[publisher's primary excerpt](https://assets.cambridge.org/97811076/56499/excerpt/9781107656499_excerpt.pdf).
All source-specific algebra used here is displayed above. QED.

**Scope.** The four summands are independent in this explicit realization of
the one-dimensional positive density. Their existence is not a claim that the
four signed BBP summands were already independent random variables. The
factorization introduces two source-determined algebraic rates; it does not
replace the signed source by a stochastic arithmetic path.

## 4. An explicit positive Lévy density

Define

$$
\begin{aligned}
B(x)&=1+e^{-3x}+e^{-4x}+e^{-5x}-e^{-\alpha x}-e^{-\beta x}\\
&=1+e^{-5x}+(e^{-3x}-e^{-\alpha x})
 +(e^{-4x}-e^{-\beta x}).
\end{aligned}
\tag{4.1}
$$

Strict interlacing proves `B(x)>0` for every `x>0`. Also `B(0)=2` and
`B` is bounded on `[0,infinity)`.

### Theorem B: elementary Laplace exponent formula

For every `a>0` and `s>=0`,

$$
\boxed{-\log L_a(s)=
\int_0^\infty(1-e^{-sx})\frac{e^{-ax}B(x)}x\,dx.}
\tag{4.2}
$$

Thus

$$
\nu_a(dx)=\frac{e^{-ax}B(x)}x\,dx
\tag{4.3}
$$

is a positive Lévy measure on `(0,infinity)`: its weighted integral
`integral min(1,x) nu_a(dx)` is finite. No drift or killing term is needed
in (4.2).

**Proof.** The elementary Frullani identity used here is

$$
\log\frac{c+s}{c}
=\int_0^\infty e^{-cx}\frac{1-e^{-sx}}x\,dx
\quad(c>0,\ s\ge0).
\tag{4.4}
$$

One may prove it without a conditional interchange: write
`(1-exp(-sx))/x = integral_0^s exp(-ux) du`, apply Tonelli to the
nonnegative integrand, and integrate `1/(c+u)` over `[0,s]`.
Take logarithms of (3.6) and apply (4.4) to its six log terms. This gives
(4.2). Each term is absolutely integrable, so their finite signed combination
is legitimate. Near zero, `B(x)=2+O(x)` and the factor `1-exp(-sx)` is
`O(x)`; at infinity, `a>0` gives exponential integrability. The same bounds
prove the Lévy-measure integrability assertion. QED.

This is the classical positive-jump Lévy--Khintchine form. Infinite
divisibility need not be inferred by an uninspected application of the general
theorem: the next section constructs every convolution root directly.

## 5. Arbitrarily fine subdivision: a constructive convolution semigroup

For positive `d<c`, define

$$
\lambda(d,c)=\log(c/d)>0,\qquad
J_{d,c}(dx)=\frac{e^{-dx}-e^{-cx}}{\lambda(d,c)x}\,dx.
\tag{5.1}
$$

Formula (4.4), or its difference form, proves that `J_{d,c}` is a
probability measure on `(0,infinity)`. For `t>=0`, let
`P_{d,c,t}` be a compound-Poisson sum: draw a Poisson variable with mean
`t lambda(d,c)`, independently draw jumps with law `J_{d,c}`, and sum the
jumps, with the empty sum zero.

For `t>0`, `Gamma(t,d)` means the shape-rate density

$$
\frac{d^t}{\Gamma(t)}x^{t-1}e^{-dx}\,dx,
\quad x>0.
\tag{5.2}
$$

Its Laplace transform is `(d/(d+s))^t`, by the substitution
`y=(d+s)x` in the defining Gamma integral. At `t=0`, use the point mass at
zero instead.

### Theorem C: exact two-parameter sheet

For every `a>0` and `t>=0`, define the law `mu_{a,t}` of the sum of four
independent variables

$$
\begin{aligned}
G_{0,t}&\sim\operatorname{Gamma}(t,a),\\
G_{5,t}&\sim\operatorname{Gamma}(t,a+5),\\
P_{\alpha,t}&=P_{a+3,a+\alpha,t},\\
P_{\beta,t}&=P_{a+4,a+\beta,t}.
\end{aligned}
\tag{5.3}
$$

Then, for all `s>=0`,

$$
\int e^{-sx}\mu_{a,t}(dx)=L_a(s)^t.
\tag{5.4}
$$

Consequently

$$
\boxed{\mu_{a,1}=\mu_a,\quad
\mu_{a,t}*\mu_{a,u}=\mu_{a,t+u},\quad
\operatorname{Tilt}_s(\mu_{a,t})=\mu_{a+s,t}}
\tag{5.5}
$$

for `t,u>=0` and `s>=0`, where

$$
\operatorname{Tilt}_s(\eta)(dx)
=\frac{e^{-sx}\eta(dx)}{\int e^{-sy}\eta(dy)}.
\tag{5.6}
$$

**Proof.** For a compound-Poisson sum with rate `t lambda` and jump
Laplace transform `Jhat(s)`, summing the absolutely convergent Poisson series
gives transform `exp(t lambda (Jhat(s)-1))`. Using (5.1), this is

$$
\exp\left[-t\int_0^\infty(1-e^{-sx})
\frac{e^{-dx}-e^{-cx}}x\,dx\right]
=\left[\frac{d(c+s)}{c(d+s)}\right]^t.
\tag{5.7}
$$

Multiply the four transforms in (5.3) and apply (3.6), obtaining (5.4).
At `t=1`, Theorem A and uniqueness identify the law with the authentic
source field. Products of transforms prove the convolution identity in
(5.5). Finally the transform at `z>=0` of the tilted law is

$$
\frac{L_a(s+z)^t}{L_a(s)^t}
=\left[\frac{R(a+s+z)}{R(a+s)}\right]^t
=L_{a+s}(z)^t,
\tag{5.8}
$$

which proves the last identity. QED.

In particular, for every integer `k>=1`, `mu_a` is the convolution of `k`
independent variables with common law `mu_{a,1/k}`. This proves infinite
divisibility with an explicit construction. It also supplies a genuine
compatibility law for the proposed sheet: moving forward in source parameter
and subdividing into convolution pieces commute exactly.

For any `t=t_1+...+t_k` with nonnegative `t_j`,

$$
\operatorname{Tilt}_s
 (\mu_{a,t_1}*\cdots*\mu_{a,t_k})
=\mu_{a+s,t_1}*\cdots*\mu_{a+s,t_k}.
\tag{5.9}
$$

The overall tilt normalization is `L_a(s)^t`; on the subdivided side it is
the product of `L_a(s)^{t_j}`. Recomposition therefore preserves both the
normalized field and its total weight.

**Existence boundary.** These formulas construct probability measures and
their convolution semigroup. They do not assert that one jointly coupled
two-parameter random surface has been physically realized. They also do not
identify convolution parameter `t` with the authentic source time `n`.
The source sequence is the slice `a=8n-7, t=1`.

## 6. The triangular composition law and its nonadditive term

Put `F(a)=log R(a)` and let

$$
A_a(s)=-\log L_a(s)=F(a)-F(a+s).
\tag{6.1}
$$

This is the positive cost of one exponential tilt. The exact composition law is

$$
\boxed{A_a(s+t)=A_a(s)+A_{a+s}(t).}
\tag{6.2}
$$

The second segment uses the updated field. Using `A_a(t)` for that segment
instead produces the nonzero interaction

$$
\begin{aligned}
I_a(s,t)
&=\log\frac{L_a(s+t)}{L_a(s)L_a(t)}\\
&=F(a+s+t)-F(a+s)-F(a+t)+F(a).
\end{aligned}
\tag{6.3}
$$

For `s,t>0`, Theorem B implies

$$
\boxed{I_a(s,t)=\int_0^\infty
\frac{e^{-ax}B(x)}x(1-e^{-sx})(1-e^{-tx})\,dx>0.}
\tag{6.4}
$$

Thus `A_a(s+t)=A_a(s)+A_a(t)-I_a(s,t)`.
Equivalently, if

$$
C_a(s,t)=e^{I_a(s,t)}
=\frac{R(a+s+t)R(a)}{R(a+s)R(a+t)},
\tag{6.5}
$$

then `C_a(s,t)>1`. This factor is not fitted: it is a rational number for
rational `a,s,t`, computed from the original four signed poles.

### Theorem D: exact cocycle compatibility

For fixed `a>0` and any `s,t,u>=0`,

$$
\boxed{C_a(s,t)C_a(s+t,u)=C_a(t,u)C_a(s,t+u).}
\tag{6.6}
$$

**Proof.** Substitute (6.5). Both sides equal

$$
\frac{R(a+s+t+u)R(a)^2}{R(a+s)R(a+t)R(a+u)}.
$$

This proves that the nonadditive correction respects both bracketings of a
three-part subdivision. QED.

Here `C_a` is a multiplicative two-coboundary of the scalar function `L_a`;
its cocycle equation is a compatibility law, not a nontrivial cohomology
class. The fixed-base interaction and the transported cost (6.2) are two
views of the same normalization.

There is also a differential form of the sheet constraint. Differentiation
under the exponentially dominated integrals gives

$$
-F'(a)=\mathbb E_{\mu_a}X,\qquad
F''(a)=\operatorname{Var}_{\mu_a}X>0,
$$

and hence

$$
I_a(s,t)=\int_0^s\int_0^t
\operatorname{Var}_{\mu_{a+v+w}}X\,dw\,dv.
\tag{6.7}
$$

The field differential is source-derived variance. It is not a freely chosen
Euler--Mascheroni weight and does not by itself generate a signed Fourier
phase.

## 7. Interactions at every order, including a decisive cubic control

For `s>=0`, define the forward difference
`Delta_s F(a)=F(a+s)-F(a)`.

### Theorem E: strict alternating connected interactions

For every integer `m>=1`, every real `a>0`, and every `s_1,...,s_m>0`,

$$
\boxed{(-1)^m\Delta_{s_1}\cdots\Delta_{s_m}F(a)
=\int_0^\infty\frac{e^{-ax}B(x)}x
\prod_{j=1}^m(1-e^{-s_jx})\,dx>0.}
\tag{7.1}
$$

**Proof.** For `m=1`, the claim is (4.2). Taking a further difference in
`a` multiplies the integral's integrand by `exp(-s_{m+1}x)-1`.
All finite differences are finite sums of absolutely convergent integrals,
so induction is valid. At zero the integrand is `O(x^{m-1})`; at infinity
it is exponentially integrable. Every factor is strictly positive for
`x>0`, proving strictness. QED.

For any finite labelled collection of shifts, the connected subset
interaction is the corresponding finite difference of `F`. The full value
is recovered exactly by the finite inclusion-exclusion identity

$$
F\left(a+\sum_{j=1}^m s_j\right)
=\sum_{S\subseteq\{1,\ldots,m\}}
\left(\prod_{j\in S}\Delta_{s_j}\right)F(a),
\tag{7.2}
$$

where the empty subset contributes `F(a)`. This is just expansion of the
commuting shift operators `E_s=1+Delta_s`; it has no convergence issue.
Equation (7.1) proves that no finite interaction-order truncation is exact
for arbitrary positive subdivisions.

The cubic connected ratio is

$$
D_a(s,t,u)=
\frac{R(a+s+t+u)R(a+s)R(a+t)R(a+u)}
 {R(a+s+t)R(a+s+u)R(a+t+u)R(a)}.
\tag{7.3}
$$

Its logarithm is `Delta_s Delta_t Delta_u F(a)`, so `0<D_a(s,t,u)<1`
for positive shifts. A pairwise-only log model predicts `D=1`; this is an
exact falsifier of that truncation.

For the source extension at `a=s=t=u=1`,

$$
R(1)=\frac{47}{15},\quad R(2)=\frac{271}{210},\quad
R(3)=\frac{41}{56},\quad R(4)=\frac{241}{504},
$$

$$
C_1(1,1)=\frac{202335}{146882}>1,\qquad
D_1(1,1,1)=\frac{38372041208}{45916893225}<1.
\tag{7.4}
$$

An equally exact control lies on the authentic source clock, using
`a=1` and `s=t=u=8`:

$$
R(1)=\frac{47}{15},\quad R(9)=\frac{106}{819},\quad
R(17)=\frac{829}{19635},\quad R(25)=\frac{316}{15225},
$$

$$
C_1(8,8)=\frac{414839061}{52528300}>1,\qquad
D_1(8,8,8)=\frac{61527533661959200}{322441778977512831}<1.
\tag{7.5}
$$

### Corollary: every ordinary cumulant of the positive field is positive

For `m>=1`, differentiating the finite log factorization gives

$$
\begin{aligned}
\kappa_m(\mu_a)
&=(-1)^mF^{(m)}(a)\\
&=(m-1)!\left[
\frac1{a^m}+\frac1{(a+3)^m}+\frac1{(a+4)^m}+\frac1{(a+5)^m}
-\frac1{(a+\alpha)^m}-\frac1{(a+\beta)^m}
\right]>0.
\end{aligned}
\tag{7.6}
$$

Positivity also follows from integrating `x^m nu_a(dx)`. In the rational
four-pole coordinates these cumulants are rational for rational `a`:
the two algebraic terms are conjugates. In particular the strict sign is
not an artifact of floating-point root evaluation.

For fixed `m`, `kappa_m(mu_a)~2(m-1)!/a^m` as `a` tends to infinity.
The exact convolution representation makes the familiar Gamma(2) boundary
transparent: `aE_0` and `aE_5` approach independent rate-one exponentials,
while the Bernoulli activation probabilities tend to zero. This recovers
the inherited source boundary law rather than establishing a new selection
law for pi.

## 8. What the nonlinearity does and does not say

The source tilts commute:

$$
\operatorname{Tilt}_s\operatorname{Tilt}_t(\mu_a)
=\mu_{a+s+t}
=\operatorname{Tilt}_t\operatorname{Tilt}_s(\mu_a).
\tag{8.1}
$$

Their nonzero connected interactions therefore **do not imply a
noncommutative update law**, non-Abelian gauge curvature, gluon dynamics, or
physical backreaction. They quantify the failure of multiplying separate
same-field expectations when the factors share the same latent source
variable. They also quantify exactly how the later normalizer changes after
the first update.

For comparison, genuine order memory can be demonstrated with two
nonnegative observed-event kernels. Take probability row `p=(1/2,1/2)` and

$$
K=\frac12\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
L=\frac12\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\tag{8.2}
$$

Both are substochastic. At their respective action settings, missing row
mass can be assigned to a failure outcome. Define `Z_M(p)=pM1` and `Phi_M(p)=pM/Z_M(p)` when
`Z_M(p)>0`. Direct multiplication gives

$$
Z_{KL}(p)=Z_{LK}(p)=\frac58,
\quad\Phi_{KL}(p)=(3/5,2/5),\quad
\Phi_{LK}(p)=(2/5,3/5).
\tag{8.3}
$$

Thus an identical scalar path weight can coexist with distinct updated
fields. Retaining only a scalar free energy would erase this order effect.
The general exact law is

$$
\Phi_{KL}=\Phi_L\circ\Phi_K,\qquad
Z_{KL}(p)=Z_K(p)\,Z_L(\Phi_K(p)).
\tag{8.4}
$$

This finite declared countermodel is separate from the original BBP source.
It identifies what a future noncommutative arithmetic construction would
need to preserve; it does not provide such a construction.

## 9. Euler--Mascheroni and the selected arithmetic boundary

At authentic source times `a_n=8n-7`, the inherited free-energy identity is

$$
\sum_{n=1}^{N-1}A_{a_n}(8)
=\log\frac{r(1)}{r(N)}.
\tag{9.1}
$$

Since `r(N)~15/(64N^2)` and `r(1)=47/15`, harmonic subtraction gives the
already established finite part

$$
\log\frac{r(1)}{r(N)}-2H_{N-1}
\longrightarrow\log\frac{3008}{225}-2\gamma.
\tag{9.2}
$$

The convolution exponent `t` simply multiplies these log quantities. It
does not select a preferred Oily--Macaroni centering, and no factor involving
`phi^{-1}-gamma` has been inserted into the source density or its triangle
interaction. Any such extra relative weight needs an independently derived
arithmetic observation law.

The selected arithmetic recurrence remains

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n).
\tag{9.3}
$$

The positive field determines `r(n)` but does not contain the selected
expanding Fourier phase by itself. A complete original-source pi-normality
route still needs

$$
\forall h\in\mathbb Z\setminus\{0\},\qquad
\sum_{n=1}^{N}e^{2\pi i hU_n}=o(N).
\tag{9.4}
$$

There is a sharp control on any claim that the source field alone forces
(9.4). Write the original BBP tail as

$$
T_n=\sum_{k=1}^\infty16^{-k}r(n+k)>0.
\tag{9.5}
$$

Then `T_n->0`, `16T_{n-1}=r(n)+T_n`, and the original BBP identity gives
`T_0=pi/16`. Consequently `V_n=-T_n` solves the **same** forcing law

$$
V_n=16V_{n-1}+r(n),\qquad V_0=-\pi/16,
$$

but `exp(2pi i h V_n)->1` for every fixed integer `h`, so its normalized
Fourier mean tends to one. Every positive field, atom, convolution root,
triangle and connected interaction in this dossier is unchanged under that
seed change. The boundary `U_0=0` must therefore enter any eventual signed
argument essentially.

The changed-seed control does not refute a proof that actually uses `U_0=0`.
It refutes only the inference from these forcing-only identities to
selected-path cancellation without using that boundary. It also prevents an
auxiliary infinitely divisible law from being silently identified with an
arithmetic path sampler.

## 10. Executable formulas, mutation controls and truth states

Exact finite corroboration should use `Fraction` arithmetic for (2.4),
(6.5), (6.6), and (7.3). No transcendental evaluation is needed for those
identities and inequalities. For the atom factorization, work over the
quadratic field `Q(sqrt(241))`, representing a value by rational pair
`(p,q)` for `p+q sqrt(241)`. Multiplication is

$$
(p,q)(r,s)=(pr+241qs,ps+qr),
$$

and inversion is `(p,-q)/(p^2-241q^2)` when the denominator is nonzero.
The product in (3.6) must reduce exactly to a rational with zero radical
coefficient and equal `R(a+s)/R(a)`.

Useful independent checks and calibrated falsifiers are:

- Expand the four original partial fractions independently and recover
  `15a^2+121a+240`, `alpha+beta=121/15`, and `alpha beta=16`.
- Compare the exact atom-transform product with the direct rational source,
  including rational `a<1`, nonintegral shifts and fresh large source times.
- Test the two bracketings in (6.6) and the sequential normalizer identity
  `L_a(s+t)=L_a(s)L_{a+s}(t)`.
- Replace the updated second normalizer by `L_a(t)`: strict (6.4) must
  reject the result for positive shifts.
- Replace the cubic connected ratio by one: either exact receipt (7.4)
  or (7.5) must reject it.
- Change a source coefficient or a factor's Bernoulli probability while
  retaining the claimed source factorization: exact transform equality
  must fail on a declared nonzero shift.
- Use the substochastic matrices in (8.2) to show that agreement of scalar
  path weights does not certify agreement of the complete updated field.
- Retain the original-forcing changed-seed control in section 9 whenever
  an arithmetic cancellation consequence is proposed.

No finite execution count in this dossier substitutes for the proofs.
Execution receipts, source hashes, actual test counts and environment
limitations belong in the round's validation record.

| Statement | Truth state and boundary |
|---|---|
| Positive original-BBP field and source tilt | PROVED LOCAL (paper), inherited source identity |
| Four independent elementary summands, Theorem A | PROVED LOCAL (paper) by exact factorization and transform uniqueness |
| Explicit positive Lévy density, Theorem B | PROVED LOCAL (paper) by elementary absolutely convergent integrals |
| All convolution roots and tilt/subdivision compatibility, Theorem C | PROVED LOCAL (paper) by explicit Gamma and compound-Poisson construction |
| Triangle cocycle and strict pair interaction, Theorem D | PROVED LOCAL (paper); scalar normalization compatibility |
| Nonzero connected interactions at every finite order, Theorem E | PROVED LOCAL (paper); no finite-order truncation is exact |
| Nonzero interaction forces noncommutative dynamics | REFUTED by commuting source tilts with strict interaction |
| Scalar path weight determines the updated field | REFUTED by (8.2)--(8.3) |
| These forcing-only identities alone establish selected Weyl cancellation | REFUTED as a boundary-free implication by section 9 |
| Original zero-seeded signed Weyl cancellation | OPEN |
| Physical gluon dynamics or material backreaction authenticated by this construction | UNVERIFIED; no physical source map or measurement supplied |
| Academic novelty or priority of the explicit factorization | UNVERIFIED; no exhaustive literature claim |

The next arithmetic test is to derive a source- and zero-boundary-dependent
signed observable on this exact field whose transport to (9.4) has a proved
error bound, then establish a temporal cancellation estimate that fails on
the changed-seed control for an explicitly identified reason. Another
positive field identity alone does not close that obligation.

## 11. Reusable sufficient criterion: an admissible pole-zero pairing

The mechanism is not peculiar to the first successful coefficients. Let
`m,k>=0` be integers, `C>0`, `b_l,c_j>=0`, and `d_j>c_j`, with repeated
parameters permitted. Suppose

$$
R(a)=C\frac{\prod_{j=1}^m(a+d_j)}
 {\prod_{j=1}^m(a+c_j)\prod_{\ell=1}^k(a+b_\ell)}\quad(a>0).
$$

This is a **sufficient** criterion, not a characterization of every rational
infinitely divisible field. The positive source measure is explicitly

$$
\sigma=C\left(*_{j=1}^m[\delta_0+(d_j-c_j)e^{-c_jx}dx]\right)
 *\left(*_{\ell=1}^k[e^{-b_\ell x}dx]\right).
$$

Empty convolution means `delta_0`. These are nonnegative locally finite
measures, and their Laplace transforms multiply by Tonelli. Consequently
`int e^(-ax) sigma(dx)=R(a)<infinity` for every `a>0`, even when a zero
denominator rate makes the unweighted measure have infinite mass.
Normalizing this tilt gives the independent-sum representation

$$
\mu_a=\mathcal L\left(\sum_{\ell=1}^k E_{a+b_\ell}
 +\sum_{j=1}^m B_j E_{a+c_j}\right),\qquad
P(B_j=1)=\frac{d_j-c_j}{a+d_j}.
$$

**Proof.** The Laplace transform of each normalized unpaired factor is
`(a+b_l)/(a+b_l+s)`. For each paired factor it is

$$
\frac{(a+c_j)(a+d_j+s)}{(a+d_j)(a+c_j+s)}
=1-P(B_j=1)+P(B_j=1)\frac{a+c_j}{a+c_j+s}.
$$

Multiplication gives `R(a+s)/R(a)`, and transform uniqueness proves the
claim. The logarithmic integral then gives the positive Levy measure

$$
\nu_a(dx)=\frac{e^{-ax}}x\left[
\sum_{\ell=1}^k e^{-b_\ell x}
 +\sum_{j=1}^m(e^{-c_jx}-e^{-d_jx})\right]dx.
$$

The bracket is `k+O(x)` at zero and bounded at infinity. Thus its required
weighted integral is finite. Replacing every unpaired exponential by
`Gamma(t,a+b_l)` and every pair by the compound-Poisson construction with
rate `t log((a+d_j)/(a+c_j))` proves the convolution semigroup and tilt
compatibility exactly as in Theorem C. No new existence assumption enters.

All finite mixed logarithmic differences have the strict alternating signs
of Theorem E when every increment is positive and at least one factor
exists. A zero increment makes the interaction zero. If `k=0`, the source
law has an atom at zero of mass `product_j (a+c_j)/(a+d_j)`; it is purely
compound Poisson under subdivision. If `k>0`, there is no atom at zero and
the Gamma components account for the infinite Levy mass. If `m=k=0`,
every normalized field is `delta_0` and all interactions vanish. These
cases cover degeneracy and repeated factors explicitly. QED.

The original BBP field is the instance `C=15`, unpaired shifts `(0,5)`
and paired shifts `(3,alpha),(4,beta)`. This general sufficient class is a
reusable construction tool. Its breadth is also a control: infinite
divisibility and all-order interaction signs alone do not authenticate the
BBP source or select its arithmetic boundary.
