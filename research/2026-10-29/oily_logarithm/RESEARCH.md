# SUCC — Operation Oily Logarithm: source Lévy exponent, reciprocal base-16 twist, and seed-winding triangle

**Research-only, 2026-10-29.** Continue the authentic SUCC four-pole BBP source, its neutral `U_0=0`, recursive carrier/convolution PR #367, inertial preparation PR #373, Operation Kepler #379, and two-opposing-observer PR #381. The source and all historical files remain unchanged. This is a *new-to-SUCC synthesis* of classical integral/probabilistic identities with exact finite-source algebra; external academic novelty is not claimed. **Base-16 normality of π and RH remain OPEN.**

## Question and object types

The author proposes an "oily-logarithm" while varying the BBP seed from its neutral value, coupling two observers, and looking for a mathematical feature that distinguishes the **actual selected path** rather than merely providing another coordinate system. Three distinct logarithms are needed:

1. **Source cumulant logarithm:** a canonical analytic logarithm of an infinitely divisible *positive* original four-pole carrier. It contains authentic four-pole finite corrections but is seed-blind.
2. **Principal character logarithm:** a branch-sensitive lift of the selected BBP *circle phase*. It produces an **integer carry cocycle** that must be retained, not exponentiated away.
3. **Joint signed cumulant logarithm:** a uniformly root-free local logarithm whose first derivatives retain the genuine original selected phases, and whose mixed derivatives reproduce the two-observer signed covariance. It is a useful exact interface but supplies no new all-N cancellation estimate.

The word **oily** denotes the author's proposed unification, not an established mathematical operator. Logarithmic normalization and Mellin–Gamma derivative operations have classical predecessors; this dossier proves their exact specialized relations and deliberately tests a same-forcing nonnormal counterseed.

## 1. Original source passport and a canonical Lévy logarithm

Fix the original source, for all `a>0`,

\[
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}
=\frac{15(a+\alpha)(a+\beta)}{a(a+3)(a+4)(a+5)},
\]

\[
\alpha=\frac{121-\sqrt{241}}{30},\quad
\beta=\frac{121+\sqrt{241}}{30},\qquad
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}>0.
\]

The original source measure is `mu_a(dx)=e^(-ax) Q(x)dx/R(a)` on `x>0`, and native arithmetic time is `a_n=8n-7`, `r(n)=R(a_n)`, `U_n=16U_(n-1)+r(n)`, `U_0=0`. The source's positive convolution roots and logarithmic interactions were proved in PR #367; they are **inherited**, not newly discovered in this round.

Define

\[
B(x)=1+e^{-3x}+e^{-4x}+e^{-5x}-e^{-\alpha x}-e^{-\beta x}.
\]

Because `3<alpha<4<beta<5`, regroup
`B=1+e^(-5x)+(e^(-3x)-e^(-alpha x))+(e^(-4x)-e^(-beta x))>0` for all `x>0`.
Also `B(0)=2`, `B'(0)=-59/15` exactly. Define the **source oily logarithm** at real relative frequency `t`:

\[
\boxed{\mathfrak L_a(t)=\int_0^\infty
\frac{e^{-ax}B(x)}x\bigl(e^{iatx}-1\bigr)\,dx
=\log_0\frac{R(a(1-it))}{R(a)}.}\tag{OL-1}
\]

Here `log_0` is the continuous branch with value zero at `t=0`. The integral converges absolutely at zero because `e^(iatx)-1=O(x)`, and at infinity because `a>0`. Proof of equality: apply the elementary Frullani integral

\[
\int_0^\infty\frac{e^{-cx}(e^{iyx}-1)}x\,dx=\log\frac{c}{c-iy},\qquad c>0,
\]

to the six terms of `B`. They reproduce exactly the factorized rational `R`. Therefore the Fourier transform is 

\[
\mathbb E_{\mu_a}e^{iatX}=e^{\mathfrak L_a(t)}\ne0
\quad\text{for every real }t.
\]

Its attenuation obeys `Re L_a(t)=int (cos(atx)-1)e^(-ax)B(x)dx/x<0` for `t!=0`; the imaginary part is the signed (unwrapped) argument. At arbitrary positive subdivision rank `τ`, the inherited convolution law has Fourier log `τ*L_a(t)`. This is a **Lévy–Khintchine characteristic exponent** of the authentic scalar field, *not* a physical or signed-digit phase law.

### Exact original-source Gamma twist and its `59`

The expansion `B(x)=2-(59/15)x+O(x²)` and the change of variable `y=ax` give, for every fixed real `t`,

\[
\boxed{\mathfrak L_a(t)=-2\log(1-it)
-\frac{59}{15a}\left(\frac1{1-it}-1\right)+O_t(a^{-2}).}\tag{OL-2}
\]

A uniform compact-`t` remainder follows by Taylor's theorem for `B(y/a)` under the exponentially integrable kernel; no term is fitted numerically. The exact original *relative-frequency-one* specialization is

\[
\boxed{\mathfrak L_a(1)=-\log2+\frac{\pi i}{2}
+\frac{59}{30a}(1-i)+O(a^{-2}).}\tag{OL-3}
\]

Gamma(1,1) contributes `1/(1-i)=(1+i)/2` (45 degrees), and Gamma(2,1) contributes `(1-i)^(-2)=i/2` (90 degrees). Equation OL-3 gives a source-authenticated finite deviation from the rank-two phase **and** amplitude. The fake `Q_fake(x)=15x` has the same Gamma(2) endpoint but log exactly `-2 log(1-it)` for every finite `a`; it fails the `59` correction. No universality or selected π cancellation is inferred from this finite source fingerprint.

## 2. Exact base-16 reciprocal logarithmic source twist

Here is a source-specific algebraic consequence not requiring any probability approximation. The numerator shifts obey

\[
\boxed{\alpha\beta=16,\quad \alpha+\beta=121/15.}
\]

Thus `alpha=4 e^(-eta), beta=4 e^(eta)`, with

\[
\cosh\eta=121/120,\quad
\sinh\eta=\sqrt{241}/120,\quad
\eta=\log\frac{121+\sqrt{241}}{120}.
\]

The numerator is self-reciprocal under the map `a -> 16/a`:

\[
P(a)=(a+\alpha)(a+\beta),\qquad P(16/a)=\frac{16}{a^2}P(a).
\]

The full four-pole `R` is **not** exactly invariant because its denominator poles do not pair under this inversion. Define the dimensionless **oily inversion logarithm**

\[
\boxed{\mathfrak D(a)=\log\frac{R(16/a)}{R(a)}-3\log\frac a4
=\log\frac{16(a+3)(a+5)}{(3a+16)(5a+16)}.}\tag{OL-4}
\]

The second equality follows by cancelling the palindromic numerator, the fixed pole at 4, and the explicit cubic homogeneity. A direct rational witness is

\[
\boxed{e^{\mathfrak D(a)}-1=\frac{a^2-16}{(3a+16)(5a+16)}.}\tag{OL-5}
\]

Consequently `D(16/a)=-D(a)`, `D(4)=0`, it is strictly increasing on `a>0`, and

\[
\boxed{-\log(16/15)<\mathfrak D(a)<\log(16/15).}
\]

To see strict monotonicity differentiate OL-4:

\[
\mathfrak D'(a)=\frac{1/5}{(a+3)(a+16/5)}
+\frac{1/3}{(a+5)(a+16/3)}>0,\qquad
\mathfrak D'(4)=1/126.
\]

Set `a=4e^u`. Exact rational algebra gives

\[
\boxed{\mathfrak D(4e^u)=2\operatorname{artanh}
\frac{\sinh u}{31\cosh u+32},\qquad
\mathfrak D(4e^u)=\frac2{63}u+O(u^3).}\tag{OL-6}
\]

This is an exact **odd hyperbolic logarithmic twist**, with the source-determined numbers 16, 15, 31 and 32. It is different from a literal 45-degree Euclidean rotation. The `Q(sqrt(241))` root geometry and `Q(sqrt5)` Oily/golden marker remain different arithmetic fields; their positive powers have no nontrivial exact identity without additional structure.

**Native-clock obstruction:** no pair of integers `n,m>=1` satisfies `(8n-7)(8m-7)=16`: both factors would have to be positive divisors of 16 congruent to 1 mod 8, and the only such divisor is 1. In fact the original arithmetic clock jumps from `a_1=1` with `e^D=128/133<1` to `a_2=9` with `e^D=2688/2623>1`. Thus this inversion is an exact symmetry of the **continuous source extension**, but not a stepwise reversal of the discrete BBP clock. This is a critical scope guard.

## 3. Mellin + Gamma + golden + Euler are one coherent log chart

For `Re(s)>-1`, and real `t`, the original carrier has the exact transform

\[
\boxed{\mathcal M_a(s,t)
=\mathbb E_{\mu_a}[(aX)^s e^{iatX}]
=\frac{a^s\Gamma(s+1)}{R(a)}
\sum_{(d,c)=(0,4),(3,-2),(4,-1),(5,-1)}
\frac{c}{[a(1-it)+d]^{s+1}}.}\tag{OL-7}
\]

This follows by integrating the **original four signed exponentials** as a single positive density; it introduces no substitute stochastic π generator. The formula is continuous and nonzero in some neighborhood of `s=t=0`, so its local logarithm exists. At `s=0`, its Fourier log is the global canonical source exponent OL-1. The original near-zero source shape `Q(x)=15x-(59/2)x²+O(x³)` gives

\[
\mathcal M_a(s,t)=\frac{\Gamma(s+2)}{(1-it)^{s+2}}
\left[1-\frac{59}{30a}\left(\frac{s+2}{1-it}-2\right)
+O_{s,t}(a^{-2})\right].\tag{OL-8}
\]

This is uniform for `s,t` in sufficiently small compact real/complex neighborhoods of zero, with a specified analytic branch. In logarithmic form,

\[
\boxed{\log\mathcal M_a(s,t)=\log\Gamma(s+2)
-(s+2)\log(1-it)
-\frac{59}{30a}\left(\frac{s+2}{1-it}-2\right)+O(a^{-2}).}
\]

Therefore `d/ds log M_a(s,0)|s=0 = E log(aX) -> psi(2)=1-gamma`. Define `lambda=(sqrt5-1)/2`, the separately authenticated two-stage Oily PGF marker; evaluating at `t=i lambda` gives the **Laplace** observable `M_a(0,i lambda)=E exp(-lambda aX)->lambda²`, since `(1+lambda)^(-1)=lambda`. The *declared* two-readout contrast is

\[
\boxed{\Omega_a=\left.\partial_s\log\mathcal M_a(s,0)\right|_{s=0}
-\mathcal M_a(0,i\lambda)
=\lambda-\gamma-\frac{59}{30a}(1+2\lambda^4)+O(a^{-2}).}\tag{OL-9}
\]

This recovers and locally unifies the inherited Oily–Macaroni single-carrier result. `gamma` enters through the **Mellin derivative of Gamma**, not as a mysterious standalone source of Fourier cancellation. Neither `lambda` nor the geometric inversion root `eta` is selected by the other without an explicit source map.

## 4. Two opposed observers: an exact log-barycenter for source AND seed

Fix `a>t>=0`, any real *central seed* `c`, any offset `s`, integer `h`, `x>0`, and native `n>=1`. Define the normalized source amplitudes

\[
f_b(x)=\sqrt{\frac{e^{-bx}Q(x)}{R(b)}},\qquad
\Psi_{\pm}(x)=e^{2\pi i h U_n(c\pm s)}f_{a\pm t}(x),\quad
\Psi_0(x)=e^{2\pi i h U_n(c)}f_a(x).
\]

The original recurrence gives `U_n(c+s)+U_n(c-s)=2U_n(c)`. The opposing carrier source midpoint gives `f_(a+t) f_(a-t)=H_a(t) f_a²`, with `H_a(t)=R(a)/sqrt(R(a+t)R(a-t))`. Hence the **exact full common-mode identity**

\[
\boxed{\Psi_+(x)\Psi_-(x)=H_a(t)\Psi_0(x)^2,}\tag{OL-10}
\]

and **exact relative-mode identity**

\[
\boxed{\frac{\Psi_+(x)}{\Psi_-(x)}=
\exp(4\pi i h16^n s)\,e^{-tx}
\sqrt{\frac{R(a-t)}{R(a+t)}}.}\tag{OL-11}
\]

The second ratio cancels the entire actual central BBP phase; the product retains its **square**. Choose an unwrapped logarithm

\[
\ell_{n,h}(c,a,x)=2\pi ih U_n(c)-\frac{ax}{2}
+\frac12\log Q(x)-\frac12\log R(a).
\]

Then `ell_+ + ell_- - 2ell_0=log H_a(t)` **exactly**, while principal logs can differ by integer multiples of `2pi i`. The relative observer disagreement is orientational and source-normalized; the common mode still holds the unknown selected π phase. The identity is valid for **every** central seed, including the coherent `c=-pi/16`. It cannot by itself select the neutral arithmetic path or prove normality.

## 5. Integer winding is the information lost under phase exponentiation

Let `x_n(c)={U_n(c)}` in `[0,1)` and `z_n=e^(2pi i U_n(c))`. Use the `[0,2pi)` phase-log branch, so `log_+ z_n=2pi i x_n`. The exact integer **literal carry** is

\[
\boxed{\kappa_n(c)=16x_{n-1}(c)+r(n)-x_n(c)\in\mathbb Z.}\tag{OL-12}
\]

Multiplying the branch equation by `exp(2pi i·)` erases `kappa_n` completely. A source- and seed-sensitive theory must retain this integer before taking the circle quotient; its mod-`q` residue cannot be recovered from the character alone after the loss.

### A second Gamma/Euler logarithm, now from the seed line—**universal no-go**

For integer `h!=0` and any real central seed `c`, consider the logarithmically weighted response to a uniformly available seed displacement:

\[
\mathcal S_{n,h}(c)=\int_0^1\frac{1-e^{2\pi ih[U_n(c+u)-U_n(c)]}}u\,du
=\int_0^1\frac{1-e^{2\pi ih16^n u}}u\,du.
\]

With `b=2pi |h|16^n`, classical sine/cosine integrals give **exactly**

\[
\boxed{\mathcal S_{n,h}=\gamma+\log b-\mathrm{Ci}(b)
-i\operatorname{sgn}(h)\mathrm{Si}(b).}\tag{OL-13}
\]

Since `sin b=0` and `cos b=1` for these integer cycles, integration by parts gives

\[
\left|\mathcal S_{n,h}-n\log16-
\left(\gamma+\log(2\pi|h|)-i\operatorname{sgn}(h)\frac\pi2\right)\right|
\le\frac1b+\frac2{b^2}+\frac2{b^3}.
\]

Thus Euler–Mascheroni **and** an opposing 90-degree imaginary finite part arise from a logarithmic seed perturbation integral. However `S_(n,h)` is **independent of the source and the central seed**. It works equally well for every coherent, rational, or shifted arithmetic history. Hence this appearance of `gamma` and a quarter-turn is a strict **counterexample to treating those features alone as evidence of π normality**. See NIST DLMF §6.2 for the exact definitions and limits of Ci/Si.

## 6. A genuinely seed-sensitive triangular branch disagreement at modulus three

For any real central seed `c`, choose two *symmetrically coupled*, rather than independently sampled, counterfactual preparations `c±delta`. Let `x_n={U_n(c)}` and

\[
J_n(\delta;c)=\{U_n(c+\delta)\}+\{U_n(c-\delta)\}-2x_n
\in\{-1,0,1\}.
\]

Set `theta={16^n delta}`. Elementary modulo-one arithmetic proves the **exact pointwise law**

\[
\boxed{J_n(\delta;c)=\mathbf1_{\theta>x_n}-\mathbf1_{\theta\ge1-x_n}.}\tag{OL-14}
\]

The conventions at measure-zero boundaries match the `[0,1)` branch. If `delta` is uniform on `[0,1]`, `theta` is uniform, and the exact **ternary disagreement law** is

\[
P(J=+1)=\max(1-2x_n,0),\quad
P(J=-1)=\max(2x_n-1,0),\quad
P(J=0)=1-|1-2x_n|.
\]

Take the smallest root-of-unity character that distinguishes the signed `+1` and `-1` branches: `omega=e^(2pi i/3)`. Its expectation is

\[
\boxed{\mathcal B_{n,3}(c)=E_{\delta}\omega^{J_n(\delta;c)}
=1-\frac32|1-2x_n|+i\frac{\sqrt3}{2}(1-2x_n).}\tag{OL-15}
\]

As `x_n` increases from zero to one, this complex number traces **two sides of the exact equilateral triangle** with vertices `omega, 1, omega^(-1)`, at uniform speed `2sqrt3`. Its imaginary part yields the exact inverse

\[
\boxed{x_n=\frac12-\frac{\operatorname{Im}\mathcal B_{n,3}}{\sqrt3}.}\tag{OL-16}
\]

A mod-two character sees only `(-1)^J` and loses the orientation: its expectation is `1-2|1-2x_n|`, invariant under `x_n -> 1-x_n`. Mod three is the **smallest cyclic character** distinguishing the two signed branches. This gives a faithful reason for testing prime three in a carry/totient study, but it does not prove that three controls π's base-16 digits.

**Coherent counterseed is discriminated, not erased.** For the original *same-forcing* advanced seed `c*=-pi/16`, `U_n(c*)=-T_n`, so `x_n(c*)=1-T_n` for `n>=1` (since `0<T_n<1/2`). Consequently,

\[
\mathcal B_{n,3}(c*)=\bar\omega+2T_n(1-\bar\omega),\qquad
|\mathcal B_{n,3}(c*)-\bar\omega|=2\sqrt3\,T_n
\le\frac{2\sqrt3}{(8n+1)^2}.
\]

The authentic zero-seed begins with `U_1=47/15`, hence `x_1=2/15` and
`B_(1,3)=4/15+(11/15)omega=-1/10+i*11sqrt3/30`.

**Normality criterion, not proof:** by the exact inverse OL-16, the original zero-seeded `x_n` is uniformly distributed mod one **iff** its `B_(n,3)` images equidistribute in arclength on those two sides. This is a conjugate geometric description, not a new asymptotic estimate. Any claim of progress needs a source-dependent estimate on the time distribution of these branch labels that cannot be deduced merely from the invertibility.

## 7. A safe complex logarithm that retains genuine selected phases

For source time `a>0`, finite Pascal observation depth `n>=0`, integer `h!=0`, and real seed `c`, define for each positive source microstate `x`

\[
M_{n,h,c}(x)=\sum_{j=0}^n\binom nj
(1-e^{-8x})^j e^{-8x(n-j)}e^{2\pi ihU_{n+j}(c)},
\qquad |M_{n,h,c}(x)|\le1.
\]

Define an **independently normalized signed logarithm**

\[
\boxed{\mathfrak C_{n,a,h,c}(\eta)=
\log\mathbb E_{\mu_a}\exp(\eta M_{n,h,c}(X)),\quad |\eta|<\log2.}\tag{OL-17}
\]

The disk is **uniform in n,a,h,c**: `|E exp(eta M)-1|<= exp(|eta|)-1<1`, so the expectation is in the open disk centered at 1 of radius one, avoids zero and the principal branch cut, and admits a unique analytic log with value 0 at `eta=0`. Its derivatives satisfy

\[
\partial_\eta\mathfrak C(0)=\sum_jq_{n,a}(j)e^{2\pi ihU_{n+j}(c)}
=: \Theta_n(a,h,c),
\]

\[
\partial_\eta^2\mathfrak C(0)=E[M_{n,h,c}(X)^2]-\Theta_n^2,
\]

\[
\boxed{\partial_a\partial_\eta\mathfrak C(0)
=-\operatorname{Cov}_{\mu_a}(X,M_{n,h,c}(X)).}\tag{OL-18}
\]

The last formula is **exactly one half** of the signed derivative of the two opposing observers' difference: `d/dt[Theta(a+t)-Theta(a-t)]|_0=2partial_aTheta`. Because the source clock derivative acts only on `mu_a`, the selected seed and literal BBP phases remain genuinely present in these connected cumulants. The finite `q` and `q'` instruments use exact `Fraction` arithmetic; numerical evaluation of the transcendental cumulants is deliberately separate.

**Limitations:** constant phase sequences have nonzero `partial_eta C` but zero source score; the source-covariance score can vanish on the same-forcing coherent counterseed even while the Weyl average tends to one. An analytic logarithm avoids spurious zero denominators; it is not an all-N signed cancellation theorem.

## 8. The actual signed target, primary sources and next falsifier

The original BBP prefix/tail identity from #379 implies for any real seed `c`

\[
U_n(c)=16^{n-1}(\pi+16c)-T_n,\quad 0<T_n\le(8n+1)^{-2}.
\]

Therefore the integer-frequency normalized Weyl cancellation for `U_n(c)` is equivalent to base-16 normality of `pi+16c` (with the usual interpretation modulo integers). The original `c=0` case remains OPEN; `c=-pi/16` is coherent and not normal. An invariant of the source alone or of seed-differentials alone necessarily survives this counterseed and cannot prove the original claim.

**Highest-value next experiment:** retain the real original four-pole source, `c=0`, `q=3` branch orientation, the full 16-class literal carry, and source-connected log cumulants. Seek a *noncircular* bound on their joint **common-mode** signed character, not simply a bounded opposition difference or an invertible rewriting of the Weyl mean. Require independently tested predictions that fail for: (i) coherent same-forcing counterseed; (ii) fake positive source `Q=15x`; (iii) wrong original pole; (iv) omitted branch integer; (v) only `q=2` unsigned branch information; and (vi) uniformly randomized seed that is Haar but not the selected initial state. No claim that such a bound has yet been obtained.

**Primary classical context:** [DLMF Gamma Euler integral and ψ](https://dlmf.nist.gov/5.2), [DLMF Gamma special values](https://dlmf.nist.gov/5.4), [DLMF cosine/sine integral identities](https://dlmf.nist.gov/6.2); original BBP source: Bailey, Borwein and Plouffe, *On the rapid computation of various polylogarithmic constants*, 1997, https://www.davidhbailey.com/dhbpapers/digits.pdf. The exponential/log-moment integrals and Lévy–Khintchine framework are classical. This report does not claim new academic priority, a physical observer mechanism, or formal Lean verification.
