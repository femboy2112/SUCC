# Oscillator constructor: continuum aperture, first-order inverse, and stable dynamics

**Scope:** local proofs constructed and audited against the shared frontier
contract and published PR541/PR542 notes. The constructor and root share a
model family; this is not an independent referee or priority claim.
All full-profile statements quantify over every translated position on the
circle; finite samples require an additional approximation certificate.

## 1. Convention and exact forward-window transform

Let T=R/Z carry Haar probability lambda. Fix 0<alpha<1. For a finite complex
Borel measure mu and integer k, define, as an L2 equivalence class in y,

\[
R_{\alpha,k}\mu(y)
=\frac1\alpha\int_{\{x-y\}\in[0,\alpha)}
e^{-2\pi i k\{x-y\}}\,d\mu(x).
\]

For a density f this is alpha^{-1} integral_0^alpha e^{-2 pi i k s} f(y+s) ds.
Endpoint conventions affect at most a null set of translated positions.
Write W_k for the same bounded averaging operator acting on L2 functions.
The observation has three real channels on real laws:
R_0, Re R_1, and Im R_1.

Use m_h(mu)=integral e^{-2 pi i h x} dmu(x), and set

\[
a_r=\frac1\alpha\int_0^\alpha e^{2\pi i r s}\,ds
=
\begin{cases}
1,&r=0,\\
(e^{2\pi i\alpha r}-1)/(2\pi i\alpha r),&r\ne0.
\end{cases}
\]

Then, by Fubini,

\[
\widehat{R_{\alpha,k}\mu}(h)=a_{h-k}m_h(\mu).
\]

This matches the forward-window sign convention of PR542. A convolution
using a backward window has conjugated multipliers and must change the
subsequent signs consistently.

## 2. Exact first-order inverse

Put omega=e^{-2 pi i alpha}, which differs from 1 on the stated domain.
In distributions on the circle,

\[
\alpha D R_0\mu=\tau_{-\alpha*}\mu-\mu,
\qquad
\alpha(D-2\pi i)R_1\mu=\omega\tau_{-\alpha*}\mu-\mu.
\]

The first identity differentiates the two moving endpoints. The second
also differentiates the local oscillator phase. Subtracting omega times
the first identity cancels the displaced endpoint:

\[
\boxed{
\mu=\mathcal A_\alpha(R_0\mu,R_1\mu),\qquad
\mathcal A_\alpha(f_0,f_1)
=\frac{\alpha}{\omega-1}
\left[(D-2\pi i)f_1-\omega Df_0\right].
}
\]

The calculation can first be performed for smooth densities and then
extended to measures by distributional convolution, or checked directly
on each Dirac measure. It includes the zero Fourier coefficient.

The equivalent coefficient identity, valid for every integer h including
h=0 and h=1, is

\[
2\pi i\left[(h-1)a_{h-1}-\omega h a_h\right]
=\frac{\omega-1}{\alpha}.
\]

Consequences:

- The two-tone full-profile map is injective for every proper aperture,
  rational or irrational.
- The inverse has one distributional derivative, compared with two
  derivatives for the B2 surface of PR541.
- The inverse is not a claim of bounded recovery in total variation.
  Its natural stable target space is H^{-1}.

## 3. Realization requires coherence as well as positivity

Let f=(f0,f1) be an arbitrary L2 pair. The image of probability laws consists
exactly of pairs satisfying:

1. integral f0=1;
2. W_0 f1=W_1 f0;
3. A_alpha(f) is a nonnegative Borel measure.

The coherence identity in item 2 is equivalent to

\[
a_h\widehat f_1(h)=a_{h-1}\widehat f_0(h)
\quad\hbox{for every }h.
\]

The vector v_h=(a_h,a_{h-1}) is nonzero for every h by the inverse identity.
Thus coherence says that (f0hat(h),f1hat(h)) is a scalar multiple c_h v_h.
The inverse identity then shows A_alpha(f)hat(h)=c_h, hence
f=(R0 A_alpha(f),R1 A_alpha(f)). At h=0, coherence and integral f0=1
force integral f1=a_{-1}; consequently A_alpha(f) has mass one.
This proves sufficiency. Necessity follows from the forward transform and
commutativity of the two averaging operators.

**Hostile realization control.** Positivity of the recovered measure alone
does not suffice. Let

\[
f_0=1,\qquad f_1=a_{-1}+\varepsilon e^{2\pi i y},\quad\varepsilon\ne0.
\]

Then A_alpha(f)=lambda because (D-2 pi i)e^{2 pi i y}=0.
But the added h=1 channel violates coherence: a_1 is nonzero for every
0<alpha<1. The pair is not a realizable two-channel surface.

This is an explicit operational role for probe relationships: a valid
inverse output does not excuse incompatible channels.

## 4. A uniform H^{-1} frame for every proper aperture

For real finite zero-mass eta define

\[
D_\alpha(\eta)^2
=\|R_0\eta\|_2^2+\|R_1\eta\|_2^2.
\]

Set S_h=|a_h|^2+|a_{h-1}|^2. Because eta is real,
|m_{-h}(eta)|=|m_h(eta)|, and the exact real-law weight is

\[
w_h=\frac{S_h+S_{-h}}2
=|a_h|^2+\frac{|a_{h-1}|^2+|a_{h+1}|^2}2.
\]

Therefore

\[
D_\alpha(\eta)^2=\sum_{h\ne0}w_h|m_h(\eta)|^2.
\]

The unsymmetrized S_h is appropriate for arbitrary complex coefficient
vectors, but it does not give the sharp real-law operator norm by simply
isolating one frequency.

The inverse coefficient identity and Cauchy-Schwarz imply

\[
S_h\ge
\frac{\sin^2(\pi\alpha)}
{\pi^2\alpha^2[h^2+(h-1)^2]}.
\]

Averaging this bound at h and -h, and using convexity of x -> 1/x, gives

\[
w_h\ge
\frac{\sin^2(\pi\alpha)}
{\pi^2\alpha^2(2h^2+1)}
\ge
\frac{\sin^2(\pi\alpha)}{3\pi^2\alpha^2h^2},
\quad h\ne0.
\]

An explicit upper bound is

\[
w_h\le\frac{B_\alpha}{h^2},\qquad
B_\alpha=
\max\left\{
\frac12+\frac{9}{8\pi^2\alpha^2},
\frac{29}{9\pi^2\alpha^2}
\right\}.
\]

For |h|=1 use a0=1 and |a_r|<=1/(pi alpha |r|) otherwise. For |h|>=2,
the expression
1+(1/2)[h^2/(h-1)^2+h^2/(h+1)^2]
decreases for h>=2 and is 29/9 at h=2.

With

\[
\|\eta\|_{\dot H^{-1}}^2
=\sum_{h\ne0}\frac{|m_h(\eta)|^2}{4\pi^2h^2},
\quad
A_\alpha=\frac{\sin^2(\pi\alpha)}{3\pi^2\alpha^2},
\]

we have the all-law frame

\[
4\pi^2 A_\alpha\|\eta\|_{\dot H^{-1}}^2
\le D_\alpha(\eta)^2
\le4\pi^2 B_\alpha\|\eta\|_{\dot H^{-1}}^2.
\]

In particular there is no Diophantine small-divisor defect left in this
two-tone geometry. Constants depend on the declared aperture. This is
a stronger continuum result than finite injectivity alone.

## 5. The half-aperture has sharp and simple constants

For alpha=1/2,

\[
a_0=1,\quad
a_r=0\ \ (r\ne0\hbox{ even}),\quad
a_r=\frac{2i}{\pi r}\ \ (r\hbox{ odd}).
\]

The exact symmetric weights are

\[
w_h=
\begin{cases}
\frac4{\pi^2}+\frac12,&|h|=1,\\[2pt]
\frac4{\pi^2h^2},&|h|\ge3\hbox{ odd},\\[2pt]
\frac{4(h^2+1)}{\pi^2(h^2-1)^2},&h\ne0\hbox{ even}.
\end{cases}
\]

Thus the sharp frequency bounds are

\[
\boxed{
\frac4{\pi^2}\le h^2 w_h
\le\frac4{\pi^2}+\frac12.
}
\]

For even h, h^2w_h=(4/pi^2) f(h^2), where
f(u)=u(u+1)/(u-1)^2 decreases on u>1. Its maximum for even h is
f(4)=20/9. This is below the |h|=1 upper value because pi^2>88/9.
The lower constant is attained at every odd |h|>=3; the upper one at |h|=1.
Both are witnessed by actual small cosine perturbations of Haar.

Equivalently,

\[
\boxed{
4\|\eta\|_{\dot H^{-1}}
\le D_{1/2}(\eta)
\le\sqrt{16+2\pi^2}\|\eta\|_{\dot H^{-1}}.
}
\]

This frame has condition ratio sqrt(1+pi^2/8), independent of frequency.

## 6. Explicit surface dynamics and naturality

For T_(b,a)(x)=bx+a, with integer b>=1, define on two-channel Fourier
profiles the explicit operator

\[
\widehat{\mathcal L_{b,a}f}(h)
=e^{-2\pi iha}\,
v_h\,\frac{v_{bh}^{*}\widehat f(bh)}{S_{bh}}.
\]

The denominators are nonzero. On compatible profiles,
fhat(bh)=v_bh m_bh; therefore

\[
\mathcal L_{b,a}(R_0\mu,R_1\mu)
=(R_0T_{b,a*}\mu,R_1T_{b,a*}\mu).
\]

Direct matrix multiplication gives

\[
\mathcal L_{c,d}\mathcal L_{b,a}
=\mathcal L_{cb,ca+d}.
\]

The identity operator is obtained on the compatible range:

\[
\mathcal L_{1,0}|_{\mathrm{compatible\ range}}=I.
\]

On arbitrary L2 pairs, L_(1,0) is the orthogonal projection with
frequency matrix v_h v_h^*/S_h, not the identity. This distinction
is mandatory in the categorical typing.

The explicitly specified realizable surface class from section 3 and the
affine law class carry naturally isomorphic affine-monoid actions.
The statement reuses PR541's precise category of dynamical representations.

For real law differences the exact optimal one-step constant is

\[
\boxed{
C_b(\alpha)=\sup_{h\ge1}\sqrt{\frac{w_h}{w_{bh}}}.
}
\]

The upper bound follows by Fourier reindexing. Necessity is witnessed by
the genuine probabilities with densities
1 +/- epsilon cos(2 pi b h x), 0<epsilon<=1. The translation a contributes
only a common unit phase. The general frame yields the finite bound

\[
C_b(\alpha)\le b\sqrt{B_\alpha/A_\alpha}.
\]

For alpha=1/2 this improves to

\[
C_b(1/2)\le b\sqrt{1+\pi^2/8}.
\]

### Exact half-aperture expansion at even b

For even b>=2,

\[
\boxed{
C_b(1/2)^2
=\max\left\{
\frac{\pi^2+8}{8}\frac{(b^2-1)^2}{b^2+1},
\frac59\frac{(4b^2-1)^2}{4b^2+1}
\right\}.
}
\]

The two candidates come from h=1 and h=2. For odd h>=3 the ratio is
(b^2 h^2-1)^2/[h^2(b^2h^2+1)]<b^2. For even h>=2 set u=h^2, t=b^2.
The squared ratio is

\[
r_t(u)=\frac{u+1}{(u-1)^2}\frac{(tu-1)^2}{tu+1}.
\]

Its logarithmic derivative has the sign of

\[
-(t-1)[3tu^2+(t+1)u+3]<0.
\]

Thus the even maximum is at h=2, and is larger than b^2.

At b=16 the h=2 term wins. The elementary pi<22/7 bound already proves
the h=1 term is smaller. Consequently

\[
\boxed{
C_{16}(1/2)^2=\frac{116281}{205},
\qquad C_{16}(1/2)=\frac{341}{\sqrt{205}}
\approx23.816473085742615.
}
\]

This is attained by cosine-law differences at input frequency 32, which
becomes output frequency 2. It is an exact worst-case dynamics bound,
not a contraction or a source-specific cancellation theorem.

## 7. Useful truth targets: H1 and interval occupancy

For a real periodic H1 function g, subtract its mean. Fourier duality,
or integration against a zero-mean primitive of eta, gives

\[
|\eta(g)|\le \|\eta\|_{\dot H^{-1}}\|g'\|_2.
\]

The half-aperture frame therefore proves

\[
\boxed{
|\mu(g)-\nu(g)|
\le\frac14\|g'\|_2D_{1/2}(\mu,\nu).
}
\]

This includes periodic Lipschitz targets. It improves the derivative
order required by the B2 target-error bound from H2 to H1. It is an
expectation-error certificate, not a probability assigned to truth.
A threshold margin larger than the displayed error certifies that target.

### Interval occupancy against Haar

For D=D_(1/2)(mu,lambda), every circle arc I, with any consistent endpoint
convention, satisfies

\[
\boxed{
|\mu(I)-\lambda(I)|
\le\min\left\{1,\frac{3}{2^{5/3}}D^{2/3}\right\}.
}
\]

Proof: choose a piecewise-linear upper envelope g+ equal to one on I and
decaying with slope magnitude 1/epsilon outside, clipped at zero.
Choose a lower envelope g- equal to zero on the complement and increasing
with slope 1/epsilon inward, clipped at one.
They obey g-<=1_I<=g+ pointwise, with the same inequalities at boundary
atoms by taking g-=0 and g+=1 there. Their Haar integral error is at most
epsilon and squared derivative norm at most 2/epsilon. These bounds
continue to hold when the two ramps overlap: the integral error for a
segment of length L<2epsilon is L-L^2/(4epsilon)<=epsilon.
The preceding H1 bound yields

\[
|\mu(I)-\lambda(I)|
\le\epsilon+\frac{D}{2\sqrt{2\epsilon}}.
\]

Choose epsilon=(D/(4 sqrt(2)))^(2/3); D=0 is immediate. The result follows.

**Sharp exponent control:** for 0<epsilon<1, the measure

\[
\mu_\epsilon
=\lambda-\mathbf1_{[0,\epsilon]}\lambda+\epsilon\delta_0
\]

is a probability. Its interval discrepancy supremum is epsilon.
For eta_epsilon=mu_epsilon-lambda a primitive before centering is
Q(x)=epsilon-x on (0,epsilon), zero elsewhere. It has mean epsilon^2/2.
Hence exactly

\[
\|\eta_\epsilon\|_{\dot H^{-1}}^2
=\epsilon^3/3-\epsilon^4/4.
\]

The sharp frame gives D_(1/2)(mu_epsilon,lambda)=Theta(epsilon^(3/2)).
Thus no uniform interval bound with exponent greater than 2/3 in D can
hold on all probability laws. In terms of energy E=D^2, the exponent is 1/3.

**Boundary:** the interval estimate requires the Haar reference (more
generally, a density bound M gives an extra M^(1/3) factor). It cannot be
extended to arbitrary atomic references. Nearby Dirac laws have D->0,
while an interval separating their locations has probability difference 1.

## 8. Exact point distance, covariance, and the authentic source bridge

For circle distance d in [0,1/2], let

\[
\ell_\alpha(d)=(\alpha-d)_++(\alpha+d-1)_+.
\]

This is the overlap length of two alpha windows whose centers differ by d.
For Dirac laws their real two-channel covariance is

\[
C_\alpha(d)=
\frac{2}{\alpha^2}\ell_\alpha(d)\cos^2(\pi d).
\]

The individual point-profile norm squared is 2/alpha. Directly integrating
the common and disjoint parts of the two windows gives

\[
\boxed{
D_\alpha(\delta_x,\delta_y)^2
=\frac4{\alpha^2}
\left[\alpha-\ell_\alpha(d)\cos^2(\pi d)\right].
}
\]

At alpha=1/2 this simplifies to

\[
\boxed{
D_{1/2}(\delta_x,\delta_y)^2
=16d+16(1/2-d)\sin^2(\pi d).
}
\]

The leading behavior is 16d, so the point-translation norm is only
Holder 1/2 in the worst case. A first-order density inverse does not
give a Lipschitz point-location modulus for discontinuous aperture kernels.

For probabilities, E_alpha(mu)=D_alpha(mu,lambda)^2 has the real pair form

\[
E_\alpha(\mu)
=\iint C_\alpha(d_T(x,y))\,d\mu(x)d\mu(y)
-\left(1+|a_{-1}|^2\right).
\]

In particular, at alpha=1/2 the Haar baseline is 1+4/pi^2 and
C(d)=8(1/2-d)cos^2(pi d).

The covariance C_(1/2) is Lipschitz on [0,1/2] with constant at most
8+4pi, by differentiating each smooth piece. Therefore every coupling
gamma of mu,nu gives

\[
|E_{1/2}(\mu)-E_{1/2}(\nu)|
\le2(8+4\pi)\int d_T(x,y)\,d\gamma(x,y).
\]

Apply the unchanged PR541 authenticated BBP tail:
0<T_n<1/[15(n+1)^2], and the epoch coupling from {U_n} to
{U_n+T_n}={16^n pi/16}, A<=n<2A. Then

\[
\frac1A\sum T_n\le\frac1{30A^2}.
\]

This yields the all-A unsquared-energy transport theorem

\[
\boxed{
|E_{1/2}(\mu_A^U)-E_{1/2}(\mu_A^\pi)|
\le\frac{8+4\pi}{15A^2}.
}
\]

The corresponding surface-norm transfer is weaker. From the point
formula, sqrt(a+b)<=sqrt(a)+sqrt(b), and sin(pi d)<=pi d,

\[
D_{1/2}(\delta_x,\delta_y)
\le4\sqrt d+2\sqrt2\,\pi d.
\]

Integrate the coupling and use sum_(n=A)^(2A-1) 1/(n+1)<=log 2:

\[
\boxed{
D_{1/2}(\mu_A^U,\mu_A^\pi)
\le\frac{4\log2}{\sqrt{15}\,A}
+\frac{\sqrt2\,\pi}{15A^2}.
}
\]

Both are source transport results, not decay of the authenticated source
energy. Since every w_h>0 and the weights are summable,
E_(1/2)(mu_A^U)->0 is equivalent to weak Haar convergence and thus to the
maintained base-16 normality criterion. That selected decay remains OPEN.

## 9. Discrete local inverse audit

Let zeta=e^(2 pi i/m), 1<=L<m, and let unnormalized profiles be

\[
R_0p(y)=\sum_{j=0}^{L-1}p(y+j),\qquad
R_1p(y)=\sum_{j=0}^{L-1}p(y+j)\zeta^{-j}.
\]

Put omega=zeta^{-L}. The exact inverse is

\[
\boxed{
p(y)=\frac{
\zeta^{-1}R_1p(y+1)-R_1p(y)
-\omega[R_0p(y+1)-R_0p(y)]
}{\omega-1}.
}
\]

Indeed the first difference is omega p(y+L)-p(y), while the static
difference is p(y+L)-p(y). This is a local constructive inverse,
not merely a Fourier nonvanishing argument. For profiles normalized
by 1/L, multiply the displayed right hand side by L.

If each complex channel reading has error at most epsilon, coordinate
recovery from the unnormalized profiles has error at most

\[
\frac{2\epsilon}{\sin(\pi L/m)}.
\]

Density recovery m p(y) incurs an additional m. Hence this bound is
not uniform resolution at fixed measurement precision as the grid grows.

## 10. Scope guards

- At alpha=1, R0 records mass and R1 records only m1 times e^(2 pi i y).
  Haar and the density 1+epsilon cos(4 pi x) have identical outputs.
  At alpha=0 the normalized aperture is undefined.
- At a single fixed translated position, two distinct Dirac laws supported
  outside the proper aperture have the same zero readings. Full translated
  profiles are load-bearing.
- Any finite number of fixed readings still aliases some circle laws:
  choose more atoms than real constraints plus mass and perturb an interior
  probability along a nonzero annihilated zero-mass vector.
- Do not assert that both quadratures are logically necessary under every
  other access model. With full translated profiles, baseline plus one
  calibrated cosine profile already removes the static blind modes.
  At a static blind h, alpha h is an integer. For h!=+/-1 its cosine
  multiplier is proportional to
  h(cos(2 pi alpha)-1)-i sin(2 pi alpha), which is nonzero since h!=0 and
  0<alpha<1. The h=+/-1 static multiplier never vanishes on this domain.
  Complex quadratures provide the clean first-order inverse proved here.
- A common additive source drive does not alter the difference equation of
  two states under fixed linear dynamics, as PR542 already proves.
- Modulating probe weights, scanning an observer, and intervening on the
  authentic BBP source are distinct operations. No access is manufactured
  by a Fourier identity.
- A globally unknown constant phase can sometimes be calibrated from a known
  nonzero channel mean. It should not automatically be declared an
  unrecoverable loss. Erasing phase or allowing uncontrolled varying phase
  is a different observation contract and needs its own witnesses.

## Verdict

The continuum two-tone hole is closed within the full translated-profile
model. The actual added dependency edges are the explicit first-order
inverse, compatibility-plus-positivity realization condition, uniform
H^{-1} conditioning, exact bounded affine dynamics, and quantitative H1
and interval truth certificates. The half-aperture has an exact sharp
times-16 norm and an all-epoch authenticated source transport estimate.

These are classical harmonic-analysis constructions proved locally, with
no worldwide novelty claim. They do not supply the selected source's
asymptotic cancellation, physical probe access, or finite-sample
reconstruction of every circle law.
