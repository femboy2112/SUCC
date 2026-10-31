# Gamma transport: phase rigidity, higher source jets, and the remaining bridge

**Parent:** PR400 `2b0628f52e9d88993c2e3ffa30b9748adfb781f0`.
**Authority:** paper proofs plus exact finite and independent computational
checks. No new Lean proof, external referee, scholarly-priority claim, signed
saving, π normality or RH result. The original four poles and `U_0=0` are retained.

The strongest results here separate an actual new source fingerprint from an
obstruction to one proposed positive Gamma-to-selected-phase mechanism. They do
not identify every possible noncentral transport with that mechanism.

## 1. Positive posterior lifts cannot hide persistent phase dispersion (GEO-01)

For each arithmetic time n let `(Omega_n,mu_n)` be any probability space. It may
be the authentic Gamma/Beta source posterior with its complete path, endpoint,
literal carry, prime labels and Walsh marks retained. Let `Z_n:Omega_n→C` have
`|Z_n|=1`, and let `z_n=e(hU_n(0))` be the actual selected unit character. Put
`m_n=∫Z_n dmu_n`.

**Theorem.** For every n,

\[
\int|Z_n-z_n|^2d\mu_n=2[1-\Re(\overline{z_n}m_n)]. \tag{1}
\]

Consequently:

* Exact positive reconstruction `m_n=z_n` forces `Z_n=z_n` almost surely.
* If `|m_n-z_n|≤epsilon_n`, then
  `∫|Z_n-z_n|²dmu_n≤2epsilon_n` and
  `1-|m_n|²≤2epsilon_n`.
* For any N, total conditional dispersion is at most `2Σ_(n≤N)epsilon_n`.
  A proposed lower bound `Σ∫|Z_n-z_n|²≥eta N` therefore requires reconstruction
  error at least `eta N/2`; it is incompatible with an `O(1)` Green error budget.

**Proof.** Expand the square, use `|Z_n|=|z_n|=1`, and integrate. The right side
is `2 Re(overline(z_n)(z_n-m_n))≤2|z_n-m_n|`. Also
`∫|Z_n-z_n|²=(1-|m_n|²)+|m_n-z_n|²`. Nonnegative integrands of integral zero
vanish almost surely. Summation is finite, requiring no interchange of limits.

For the authentic tail `T_n>0`, the previously established comparison between
`z_n` and `w_n=e(h16^(n-1)π)` has `epsilon_n=2π|h|T_n` and
`Σepsilon_n=2π|h|B`, where `B=(S_R-π)/15`. Thus **if** a positive latent lift is
claimed to reconstruct the selected phase with this same pointwise error, its
total dispersion about that selected phase is at most `4π|h|B`. Persistent
posterior mixing cannot be inserted into that representation at no cost.
The premise is explicit: the known scalar identity does not itself construct
such a random lift.

The theorem also holds for unit vectors in any complex Hilbert space, replacing
`overline(z)m` by the inner product. A unitary matrix observable applied to a
fixed unit vector is therefore subject to the same restriction on that vector.
Other vectors, signed kernels, nonpositive measures, vector-valued amplitudes of
variable norm, nontrivial reconstruction operators and estimates not based on
pointwise closeness lie outside this theorem.

**Sharp controls.** Under two equal positive weights put
`Z_±=(1-t²±2it)/(1+t²)`, target 1. Then
`m=(1-t²)/(1+t²)` and `E|Z-1|²=4t²/(1+t²)=2|m-1|` exactly. The factor 2 is sharp.
At t=1 the mean is zero and dispersion is 2: full cancellation is possible, but
it fails exact reconstruction of the selected unit character by distance 1.
This explains precisely why an auxiliary average is not automatically the
selected endpoint. The same proof applies to the coherent changed seed, so the
obstruction is architectural, not a zero-seed cancellation theorem.

## 2. A second finite-source correction to the golden/Oily triangle (GEO-02)

This section preserves the author's **Harmonic Numbers / Golden Ratio /
Euler–Mascheroni triangle** and **Oily–Macaroni**, `Omega_OM=lambda-gamma`, with
Leah / `femboy2112` provenance. The finite endpoint PGF, finite golden branch,
and its first correction are inherited from PR370. Only the next coefficient
and its sharp higher-jet controls are derived here.

Let

\[
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x},\quad
R(a)=\int_0^\infty e^{-ax}Q(x)dx,\quad a_n=8n-7,
\]

and keep the already declared time-matched observation law

\[
G_n(z)=\frac1{R(a_n)}\int_0^\infty e^{-a_nx}Q(x)
       [z+(1-z)e^{-8x}]^n dx. \tag{2}
\]

This is a positive auxiliary source/observer law. It is not a distributional
law for π's selected digits. At integer n its coefficients are positive
rationals, computed independently either by finite Laplace differences or
Euler Beta products.

**Theorem.** Uniformly for z in `[0,1]`,

\[
G_n(z)=G_0(z)+\frac{G_1(z)}n+\frac{G_2(z)}{n^2}+O(n^{-3}), \tag{3}
\]

where `G_0(z)=(2-z)^(-2)`, the inherited first coefficient is

\[
G_1(z)=-\frac{(z-1)(511z-302)}{120(z-2)^4},
\]

and the second coefficient is

\[
\boxed{G_2(z)=
\frac{(z-1)(159826z^3-46581z^2-131748z+35212)}{14400(z-2)^6}.} \tag{4}
\]

The expansion holds with the derivatives needed below on a fixed neighborhood
of the interior limiting root. It is not asserted uniformly over a growing
source family, rank or observation clock.

**Derivation.** More generally assume a positive bounded finite exponential
kernel has `Q(x)=c_1x+c_2x²+c_3x³+O(x⁴)`, `c_1>0`. Set

\[
A=(7+c_2/c_1)/8,\quad
B=(49/2+7c_2/c_1+c_3/c_1)/64,
\quad d=2-z,
\]
\[
D=z(1-z)/2,\qquad E=-z(1-z)(2z-1)/6.
\]

With `y=8nx`, the unnormalized latent density, after removing its constant
factor, is `y e^-y[1+Ay/n+By²/n²+O(poly(y)/n³)]`. The conditional binomial
factor is

\[
e^{-(1-z)y}\left[1+\frac{Dy^2}n+
\frac{Ey^3+D^2y^4/2}{n^2}+O(\operatorname{poly}(y)/n^3)\right].
\]

The denominator is `1+2A/n+6B/n²+O(n^-3)`. Integrating each power using
`∫y^j e^-dy dy=j!/d^(j+1)` yields

\[
N_1=2A/d^3+6D/d^4,
\quad N_2=6B/d^4+24(AD+E)/d^5+60D^2/d^6,
\]
\[
G_1=N_1-2A/d^2,
\qquad G_2=N_2-2AN_1+(4A^2-6B)/d^2. \tag{5}
\]

Authentic `c_1=15,c_2=-59/2,c_3=81/2` give `A=151/240,B=403/1920`, and direct
simplification gives (4). To control remainders, split at `y=n^(1/6)`; on the
lower interval Taylor remainders are bounded by `n^-3` times a fixed polynomial
in y and `e^-y/2`. On the upper interval the original bounded exponential
kernel and `a_n/(8n)→1` give exponentially small integrals, while the binomial
factor is at most 1. Its first fixed number of z-derivatives are bounded by
powers of `n(1-e^-y/n)≤y`, giving the same domination. This proves the uniform
expansion, including local derivatives. These are analytic estimates, not an
extrapolation of finite samples.

Write `q=(3-sqrt(5))/2=lambda²`. The known authentic least fixed point q_n is
interior for n≥2. Its source-specific expansion is

\[
\boxed{q_n=q+\frac\alpha n+\frac\beta{n^2}+O(n^{-3}),}\tag{6}
\]
\[
\alpha=-\frac{1231}{240}+\frac{2671\sqrt5}{1200},
\qquad
\boxed{\beta=\frac{6031}{80}-\frac{12139211\sqrt5}{360000}.}
\]

Indeed `1-G_0'(q)=1-2lambda³>0`, so coefficient matching in `q_n=G_n(q_n)` gives

\[
\alpha=\frac{G_1(q)}{1-G_0'(q)},\quad
\beta=\frac{G_0''(q)\alpha^2/2+G_1'(q)\alpha+G_2(q)}{1-G_0'(q)}. \tag{7}
\]

Uniform convergence puts q_n in a neighborhood on which the derivative of
`G_n(z)-z` is bounded away from zero. Substitution of the proposed expansion
has residual `O(n^-3)`; the mean-value theorem transfers it to the root. This
justifies the error in (6), rather than using a formal implicit series alone.

The finite-source log observer obeys

\[
E\log((8n-7)X)=1-\gamma-\frac{59}{240n}-\frac{3601}{28800n^2}+O(n^{-3}). \tag{8}
\]

For the general kernel above its two coefficients are `A-7/8` and
`5B-2A²-49/128`. This follows by integrating `log y` in the same density:
`E_Gamma(2)[y log y]=2psi(2)+1` and
`E_Gamma(2)[y² log y]=6psi(2)+5`, then adding
`log(1-7/(8n))`. The logarithmic singularity is integrable under y dy; the
remainder argument remains valid. Therefore the authentic finite Oily contrast
`Omega_n=E log((8n-7)X)-q_n` has second coefficient

\[
\boxed{-\frac{2174761}{28800}+\frac{12139211\sqrt5}{360000}.} \tag{9}
\]

**A decisive higher-jet control.** For every fixed `epsilon≥0`, the distinct
positive source `Q_epsilon=Q+epsilon(1-e^-x)^3` has the same `Q'(0),Q''(0)` and
therefore the same Gamma rank and first golden correction. It changes c_3 by
exactly epsilon and B by `epsilon/960`. Equations (5)–(7) yield

\[
\Delta G_2(z)=\frac{\epsilon}{160}(d^{-4}-d^{-2}),\quad
\boxed{\Delta\beta=-\epsilon\sqrt5/800},\quad
\Delta[\Omega_n]_{n^{-2}}=\epsilon(1/192+\sqrt5/800). \tag{10}
\]

Thus the second golden/Oily jet detects a previous higher-jet fake. It still
fails source uniqueness: `Q+epsilon(1-e^-x)^4` is positive, distinct, and agrees
through c_3, so it matches all coefficients in (3), (6), (8), (9). For every
finite Taylor depth m, the positive addition `(1-e^-x)^(m+1)` evades that depth.
The full original four-pole passport is stronger information than finitely many
positive-source asymptotic jets. None of these readouts controls signed phase.

## 3. What fixes a continuous Gamma interpolation? (GEO-03)

Classically Gamma's recurrence gives, for real t≥0,

\[
\mathcal G(t)=\prod_{\delta=1,4,5,6}\Gamma(t+\delta/8)^{c_\delta},
\quad
\mathcal G(t+1)/\mathcal G(t)=H(t)=\prod_\delta(t+\delta/8)^{c_\delta}.
\]

The exact source is `(log H)'/8` at t=n−1. A Gamma multiplication formula
rearranges these factors; a Barnes primitive
`B(t)=Π G_Barnes(t+delta/8)^c` obeys `B(t+1)/B(t)=mathcal G(t)`.
These are classical recoveries, and the exponent signs remain essential.

**Periodic ambiguity.** For any positive C² solution F of `F(t+1)=H(t)F(t)`,
`P(t)=F(t)/mathcal G(t)` is positive and 1-periodic. The analytic choice

\[
F_{\epsilon,m}(t)=\mathcal G(t)
\exp[\epsilon\sin^{2m}(\pi t)],\qquad m\ge1,
\]

matches every integer value and the first `2m-1` derivatives there, and has
**exactly the same H(t), hence the same continuous one-step forcing at every
real t**. At half-integers its ratio to mathcal G is exp(epsilon). A positive
C-infinity perturbation using a periodic flat function
`exp(-1/sin²(pi t))`, set to zero at integers, even matches all integer jets.
The latter is smooth, not real analytic at the integers. The parent/source
Gamma formula remains the chosen classical function; the construction shows
which proposed uniqueness inference would be invalid.

**Repair specialized to this source.** Among positive C² solutions with the
same normalization at t=0, **eventual log-convexity uniquely selects**
mathcal G. Its logarithmic second derivative is

\[
4\psi_1(t+1/8)-2\psi_1(t+1/2)-\psi_1(t+5/8)-\psi_1(t+3/4)>0,
\]

because trigamma is strictly decreasing and the first argument is smaller
than all the others. It tends to zero. If `g=log P` is C² periodic and
`(log F)''≥0` eventually, fix any t and let integer k→infinity. Then
`g''(t)≥-log(mathcal G)''(t+k)→0`. A periodic g with g''≥0 must be constant;
normalization fixes it. This is an elementary source-specific version of the
classical log-convexity uniqueness principle, not a new normality result.

A weakly continuous positive convolution semigroup is a different object and
also has a uniqueness repair: its time-one Laplace transform L_1(s)>0 fixes
`L_t(s)=L_1(s)^t` by additivity of `-log L_t`, first at rational t and then by
continuity. Laplace uniqueness fixes every measure. SUCC already records this
argument in `PASCAL_ROTATED_GAMMA_BULK.md` PB15. It is recovered here, not newly
claimed, and requires the full semigroup law; integer vertices alone do not
supply it.

**Complex monodromy.** Authentic integer exponents make mathcal G a single
meromorphic function. Its pole orders are 4 at `-1/8-m`; its zero orders are
2,1,1 at `-1/2-m,-5/8-m,-3/4-m`, respectively, for integers m≥0. Around a closed
contour avoiding this divisor, the logarithmic derivative has integral
`2πi` times an integer, so its exponentiated multiplicative holonomy is 1.
Noninteger auxiliary powers may have branch monodromy, but that is additional
rank/observer data. It cannot be silently assigned to the authentic four-pole
arithmetic transport.

## 4. Genuine affine order defect, with the zero boundary still absent (GEO-04)

Let `F_i(x)=16x+r(i)` on the **real lift**. These are actual source increments,
though applying them in a permuted order changes the physical arithmetic clock.
Direct composition gives

\[
F_iF_j(x)-F_jF_i(x)=15[r(j)-r(i)],
\quad
F_iF_jF_i^{-1}F_j^{-1}(x)=x+15[r(j)-r(i)]. \tag{11}
\]

This is a nonzero source-derived order defect for i≠j, since the authentic
positive Laplace transform r is strictly decreasing. It is more than a scalar
function of endpoint grade with zero curl. However it is a translation,
**independent of x and of the selected seed**. At i=1,j=2 its exact displacement
is `-12301/273`; distinct positive source mutants change the displacement, while
all seeds leave it fixed. Iterating such commutators gives an affine algebra of
translations and dilations, not a preferred zero-seed worldline.

On the actual chronological path, the inherited Green tail satisfies
`T_(n+1)=16T_n-r(n+1)`. The translation `C_n(x)=x+T_n` obeys the exact square

\[
C_{n+1}\circ F_{n+1}=D_{16}\circ C_n,\qquad D_{16}(x)=16x. \tag{12}
\]

The square holds for every seed. On circle Haar L² the coordinate translations
are unitary; a formal conjugacy therefore supplies no contraction of the
selected orbit. The zero seed maps to the initial pure-radix phase π/16, whereas
the coherent seed `-π/16` maps to zero. Equation (12) exposes the indispensable
boundary coordinate rather than estimating its orbit.

For finite exact checks, retain `(x_n,kappa_n)` with
`16x_(n-1)+r(n)=x_n+kappa_n`, `x_n∈[0,1)`. The full Walsh mark is
`chi_m(kappa_n)=(-1)^popcount(m & (kappa_n mod16))`, for all 16 masks. The code
computes the complete 16×16 grade/carry tensor
`Σ_j q_n(j) chi_a(j) chi_b(kappa_(n+j))`. It has genuine mixed entries and is
not replaced with q=3 or q=6 orientation. Those smaller labels identify 0 and6,
while Walsh mask2 separates them. This finite observation is not an asymptotic
signed inequality. Integer and dyadic aliases are respected: seed 1 has the
same circle path; seed1/16 adds one to the first carry then coalesces.

**A finite source-selected distinction.** The exact tensor ranks at n=3,7,17
are respectively4,5,10. For the coherent same-forcing seed `-π/16`, all marked
future times are at least2 and all carries are15. Its tensor therefore factors
as `W_ab=chi_b(15) Σ_j q_n(j)chi_a(j)`, of rank1 for every n≥2. Walsh inversion
also gives the exact identity
`Σ_b[1-W_0b²]=16[1-Σ_d p_d²]`, where p_d is the positive source-weighted carry
residue law. The coherent tensor has zero carry dispersion; authentic finite
fixtures have positive dispersion. This is an executed diagnostic that uses
the selected carry, unlike the seed-blind affine commutator. No positive-density
or all-horizon lower bound has been proved. Carry dispersion alone also does
not control a fixed complex character: digits near the circle cut can differ
while their circle phases remain close.

## 5. Literature and source boundaries

Primary classical references checked 2026-10-30:
[NIST DLMF §5.5](https://dlmf.nist.gov/5.5) for Gamma recurrence/multiplication
and log-convex uniqueness, [§5.12](https://dlmf.nist.gov/5.12) for Euler's Beta
integral, [§5.17](https://dlmf.nist.gov/5.17) for Barnes recurrence, and
[§5.2](https://dlmf.nist.gov/5.2) for Gamma's meromorphic divisor. The exact
formulae above are derived here from those identities and the frozen source;
no scholarly-priority claim is made.

The scalar Green constant was already explicit in October27's
`PI_SELECTED_BOUNDARY_CRT_FRONTIER.md`; PR400's purported new constant is a
recovery. The finite golden first correction is already PR370. Semigroup
uniqueness and periodic Gamma gauges also have prior repository proofs.
The new-to-this-campaign items are the second finite golden/Oily coefficients,
their exact cubic/fourth-order discrimination hierarchy, the quantitative
positive-phase-lift obstruction applied to a summable Green budget, and the
explicit source-Gamma eventual-log-convexity repair. They remain separate from
the still-open source-selected signed interaction theorem.
