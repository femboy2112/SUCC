# Chiral target descent: reassembling SUCC without strengthening the normality target

Research child of PR #333, pinned parent `a0e4bfd9c218dfdc83ed9d5684ce8d8e4624cde5`.
Original four signed BBP poles, zero seed, inherited files, archives and main are unchanged.
**Pi normality remains OPEN. No stronger asymptotic order for its selected Weyl sums is proved.**
The algebraic/analytic results below have explicit proofs; finite certificates are a separate authority.
No external novelty priority or Lean-kernel authority is asserted.

## 1. Earlier work that is actually load-bearing

| Prior SUCC work | What is reused | What is not inferred |
|---|---|---|
| #26-#29, shared-carrier / dual E descent | A target descends precisely through its actual observation fibers; keep joint source information | Marginal uniformity or matching reports do not supply the joint law |
| #61, NO-GHOST miniature carriers | Declared independent operations need an actual joint carrier | Two projections do not manufacture missing states |
| #293/#323, original BBP Green bridge | Exact real source completion with a summable scalar tail | Shadowing does not supply equidistribution |
| #296, internal Fourier matrix | Keep evaluated signed pair terms; use a spectral observable rather than phase-blind occupancy | Positivity of a Gram matrix is not a decay estimate |
| #300 and the categorical observer atlas | Solve the target quotient rather than reconstruct every hidden variable | No new incompatible category class is needed |
| #308, two quadratic atoms | Explicit real endpoint kernels and the exact signed source | Coefficient-space rank is not dynamical multiplicative rank |
| #327/#328, growing-energy obstructions | Avoid unnecessarily prescribed growing clocks and conditional norms | Even normal finite-type carriers can fail those stronger gates |
| #330/#332/#334, solenoid/rank audit | Preserve the observed rank-one slice and transverse defect | Higher-rank bulk Haar does not imply the selected slice is Haar |
| #333, chiral source | Two rational zero-seeded streams sum to the authentic BBP state | The streams are not independent random samples |

Read `docs/CATEGORICAL_OBSERVER_ATLAS.md`, `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`,
and `research/2026-10-25/SUCC_INTERNAL_MATRIX_WALK.md` for the inherited constraints.
The last frontier document contains historical coefficients; the later #319 bound is
`N-(log_8 N)/14+O_h(1)`, still not `o(N)`.

## 2. Source contract and the exact positive gauge decomposition

Write `e(x)=exp(2*pi*i*x)`. Preserve

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
$$

The inherited chiral states satisfy `U_n=U_n^+ + U_n^-`, with both initial values zero.
Their completed constants are `C_+=pi+2 log 2`, `C_-=-2 log 2` and

$$U_n^\pm+T_n^\pm=16^{n-1}C_\pm.$$

The source-specific real Green integrals are

$$
T_n^+=\int_0^1t^{8n}\frac{2-t}{4(t^2-2t+2)}\,dt,\qquad
T_n^-=-\int_0^1t^{8n}\frac{t}{4(2-t^2)}\,dt.
$$

**Theorem: explicit anti-diagonal regularization.** For every integer `n>=0`, put

$$a_n=\frac1{4(8n+1)}.$$

Then exactly

$$\boxed{T_n^+=a_n+R_n^+,\quad T_n^-=-a_n+R_n^-,\quad R_n^++R_n^-=T_n,}$$

where

$$
R_n^+=\frac14\int_0^1\frac{t^{8n+1}(1-t)}{t^2-2t+2}\,dt,\qquad
R_n^-=\frac14\int_0^1\frac{t^{8n}(1-t)(t+2)}{2-t^2}\,dt.
$$

Both residuals are strictly positive. For `n>=1`,

$$
0<R_n^+\le\frac1{4(8n+2)(8n+3)},\qquad
0<R_n^-\le\frac3{4(8n+1)(8n+2)}.
$$

**Proof.** Subtract `1/4` from the first kernel and add `1/4` to the second.
The resulting numerators are exactly `t(1-t)` and `(1-t)(t+2)`.
Both quadratic denominators are at least one on `[0,1]`. Integrating the beta
monomials gives the displayed bounds. Adding the two residual kernels gives
`(1-t)/[(2-t^2)(t^2-2t+2)]`, the original BBP Green kernel. No limiting cancellation
or numerical approximation is used. QED.

In particular,

$$\sum_{n\ge1}(R_n^++R_n^-)=B=\frac{\sum_{n\ge1}r(n)-\pi}{15}<\frac1{15}.$$

The individually nonsummable `+/-1/(32n)` components are one explicitly known
anti-diagonal direction. Define **observation corrections**, not changed source histories,

$$\widetilde U_n^+=U_n^++a_n,\qquad \widetilde U_n^-=U_n^--a_n.$$

Their sum is exactly `U_n`. Their initial observations are `+/-1/4`, **not zero**;
the original underlying source states remain zero-seeded. The corrected recurrences
would have sources `r_+(n)+a_n-16a_{n-1}` and `r_-(n)-a_n+16a_{n-1}`; these must not
be relabelled as the original separate source laws.

**Uniform joint-character transport.** For any integers `a,b`, any `N>=1`, and any
complex weights `|w_n|<=1`,

$$
\boxed{
\left|\sum_{n=1}^N w_n\left[e(a\widetilde U_n^++b\widetilde U_n^-)
-e\left(16^{n-1}[a\pi+2(a-b)\log2]\right)\right]\right|
\le2\pi B\max(|a|,|b|).
}
$$

Indeed the real phase error is `a R_n^+ + b R_n^-`, bounded in absolute value by
`max(|a|,|b|)T_n`. Apply `|e(x)-e(y)|<=2*pi*|x-y|` and sum. This improves the
separate *transport error* from logarithmic to bounded after an explicit gauge;
it proves **no decay of either Fourier sum**.

The gauge is Archimedean, not a blanket p-adic regularization. The rational chiral
forcings have genuine poles at zero with residues `+1/32,-1/32`; only the sum removes
those poles. One cannot apply the original all-time Z_2 source extension independently
to both unregularized chiral sources.

### Moving transverse gains: reuse of #332 with the corrected joint observable

For a positive integer gain `Q` and `H=max(|a|,|b|)>0`, the complete sum of absolute
phase errors is at most

$$\sum_{n\ge1}\min\left(2,\frac{2\pi H Q}{15(n+1)^2}\right)
\le4\sqrt{\pi H Q/15}.$$

The last bound follows by integrating the decreasing majorant on `(0,infinity)`.
For `Q=product q_j^{m_j}` and `0<=m_j<M_j`, the normalized rectangular transport
error is at most

$$
\frac{4\sqrt{\pi H/15}}{N\prod_jM_j}
\prod_j\frac{q_j^{M_j/2}-1}{\sqrt{q_j}-1}.
$$

This is #332's summable-tail corridor now available for **every corrected joint
chiral character**, not only the sum character. In particular a single transverse
width `M=floor(2 log_q N)` gives `O_H(1/log N)`. It does not remove the rank-one trace
obstruction audited in #334.

## 3. Two distinct clocks: the exact filter ideal

Let `E f(n)=f(n+1)`. Take fixed integer polynomials `P_+,P_-`, set `D=P_+-P_-`, and form

$$F_n=P_+(E)U_n^+ +P_-(E)U_n^-.$$

The exact completed carrier is

$$
16^{n-1}\left[P_+(16)\pi+2D(16)\log2\right].
$$

Its raw Green defect is `P_+(E)T_n^+ +P_-(E)T_n^-`. By the preceding decomposition,

$$P_+(E)T_n^+ +P_-(E)T_n^-=D(1)/(32n)+O_P(n^{-2}).$$

**Theorem.** The raw defect is absolutely summable if and only if `D(1)=0`.
The explicitly retained logarithmic carrier cancels if and only if `D(16)=0`.
Thus simultaneous endpoint neutrality and logarithmic-channel cancellation mean

$$\boxed{D(X)=(X-1)(X-16)Q(X),\qquad Q\in\mathbb Z[X].}$$

These are different evaluation conditions, not two names for the same clock.
Division by the two distinct monic linear factors proves the integral factorization.
A nonzero difference polynomial satisfying both needs degree at least two.

For a constructive uniform bound, write `P_+=sum a_j X^j`, `P_-=sum b_j X^j` and assume
`sum(a_j-b_j)=0`. Then

$$
\sum_{n\ge1}|\text{raw defect}_n|
\le B\sum_j\max(|a_j|,|b_j|)
+\sum_j|a_j-b_j|\sum_{r=1}^j a_r^{\rm gauge},
\quad a_r^{\rm gauge}=\frac1{4(8r+1)}.
$$

Proof: use `sum_j(a_j-b_j)a_{n+j}=sum_j(a_j-b_j)(a_{n+j}-a_n)` and the exact telescoping
`sum_{n>=1}(a_n-a_{n+j})=sum_{r=1}^j a_r`. The lag cost is logarithmic, not exponential.
The formula applies to every finite filter, including an N-dependent one when its entire
right-hand side is tracked. The iff asymptotic above is for a fixed filter.

**Sharp saturation statement.** If `D=(X-1)(X-16)Q`, the original source recurrence gives

$$
\boxed{F_n=P_-(E)U_n+Q(E)[r_+(n+2)-r_+(n+1)].}
$$

The chiral source `r_+(n)` is a positive decreasing moment sequence tending to zero.
Consequently `sum_{n>=1}|r_+(n+2)-r_+(n+1)|=r_+(2)=121631/262080`.
The extra channel is explicitly summable. Thus these fixed linear chiral filters cannot
supply a *new* normality discriminator: they reduce to the original filtered orbit plus a
paid summable correction. This is an operational negative theorem, not a claim that nonlinear
or source-dependent couplings cannot help.

Example: `P_+=17-17X+X^2`, `P_-=1` gives `F_n=U_n+r_+(n+2)-r_+(n+1)`.
The mutation `D=X-16` cancels the completed logarithmic component but leaves a nonsummable
raw tail. The mutation `D=X-1` removes the harmonic residue but leaves a log-2 carrier.
If the completed pi coefficient also vanishes, the filtered phase mean tends to one,
not zero.

## 4. The weakest faithful categorical zoom-out

Let `mu_N` be the empirical measure of `({U_n^+},{U_n^-})` on `T^2`. Addition
`m(x,y)=x+y` has kernel `H={(t,-t):t in T}` and gives the quotient `T^2/H ~= T`.
This is the earlier source-fiber target-descent theorem instantiated on the actual
combined character, not an additional independent coordinate system.

For an auxiliary analysis measure `nu_N=mu_N * Haar_H`,

$$
\widehat\nu_N(a,b)=
\begin{cases}\widehat\mu_N(h,h),&(a,b)=(h,h),\\0,&a\ne b.\end{cases}
$$

The equality follows by integrating `e((a-b)t)`. Therefore

$$\boxed{\nu_N\longrightarrow\mathrm{Haar}_{T^2}
\iff m_*\mu_N\longrightarrow\mathrm{Haar}_{T}
\iff \pi\text{ is base-16 normal}.}$$

The auxiliary convolution does not assert physical randomization or a product law for the
actual chiral orbit. It removes only modes invisible to the specified target.
Every pointwise anti-diagonal gauge leaves `nu_N` **exactly** unchanged, so the correction
in section 2 preserves this quotient at every finite N.

Finite averaging over `t=j/q` retains aliases when `q | a-b`; it is not full Haar unless the
observed frequency set excludes such off-diagonal differences. These aliases are tested.
Uniform individual marginals still do not suffice: `(X,-X)` has a constant sum.

## 5. A finite-certifiable spectral target that is exactly equivalent to Weyl

Set `M_N(h)=N^{-1}sum_{n=1}^N e(hU_n)` and use **fixed summable weights**:

$$\boxed{\mathcal Q_N=2\sum_{h=1}^{\infty}2^{-h}|M_N(h)|^2.}$$

Then `0<=Q_N<=2`, and

$$\boxed{\mathcal Q_N\to0\iff M_N(h)\to0\ \forall h\ne0
\iff\pi\text{ is base-16 normal}.}$$

Proof: a fixed term is bounded by the nonnegative full sum. Conversely, choose a fixed
large cutoff H so the tail is small, and then use the finitely many fixed-mode limits.
No prescribed growing CRT schedule, full joint Haar law, or uniformity over moving modes
is added. This is a calibrated equivalent target, **not an achieved limit theorem**.

For finite computation,

$$\mathcal Q_{N,H}\le\mathcal Q_N\le\mathcal Q_{N,H}+2^{1-H}.$$

The kernel resummation makes the retained signed interactions explicit:

$$
\mathcal Q_N=\frac1{N^2}\sum_{n,m\le N}K(U_n-U_m),\qquad
K(t)=\frac3{5-4\cos(2\pi t)}-1.
$$

Here `-2/3<=K<=2`: individual cross terms can be negative even though the final spectral
sum is nonnegative. This is the earlier Fourier-Gram instrument with a summable observer
spectrum; the phase-blind occupancy baseline is not substituted for it.
The original Green bridge gives the explicit stability bound

$$|\mathcal Q_N(U)-\mathcal Q_N(16^{n-1}\pi)|\le16\pi B/N.$$

Indeed `|M_U(h)-M_pi(h)|<=2*pi*h*B/N` and the difference of squared moduli is at most
twice that; sum `sum h/2^h=2`.

A uniform q-point circle grid has **exact** full energy `2/(2^q-1)`.
For q=17 the first sixteen modes vanish, but the positive tail remains. The finite verifier
explicitly retains that tail instead of declaring normality from the observed band.

### Signed SUCC innovation, and a tested failed shortcut

Define `J_N=N^{-1}sum_{m<=N}K(U_{N+1}-U_m)`. Exact pair counting gives

$$\boxed{(N+1)^2\mathcal Q_{N+1}=N^2\mathcal Q_N+2N J_N+2.}$$

Thus the still-unproved source estimate is a cumulative **signed** innovation bound;
positivity or local source cancellation does not establish it.
A hypothetical eventually valid bound `J_N<=Q_N/2+epsilon_N`, with nonnegative
`epsilon_N->0`, would imply `Q_N->0`: multiplying the recursion bound by `1/(N+1)`
and telescoping gives `N Q_N<=O(1)+2 sum epsilon_n+2 log N`.
The special no-error assertion already fails for the actual zero-seeded source at `N=2`:
certified `J_2-Q_2/2>0.6482`. Any successful drift argument must accommodate temporary
reinforcement. An all-N contraction has been decisively refuted, not silently assumed.

## 6. Reproducible finite evidence and limits

The Python instrument reduces rational phases modulo one **before** any evaluation,
uses exact Machin arctangent brackets for pi, rational Taylor remainders, and outward dyadic
rounding. It outputs rigorous finite intervals and a separate exact spectral-tail budget.
No binary floating-point value is accepted as a phase witness.

Commands from the repository root:

```sh
python -m unittest discover -s tests -p 'test_chiral_target_descent.py' -v
python scripts/chiral_target_descent_probe.py --write receipt.json
python scripts/chiral_target_descent_probe.py --verify receipt.json
python research/2026-10-27/chiral_target_independent_oracle.py
```

The optional last command uses SymPy only as a second algebraic implementation.
The production module and focused suite use the standard library.

In the local source-authenticated partial tree: **23 new + 17 unchanged parent tests pass**;
independent symbolic oracle passes; the exact receipt and three false-authority/source
mutations pass. The parent's production Git blob is verified as
`8305e09892f19007e0ae0538a60d05954b2def9e`, matching live #333.
A combined validation command exceeded its process timeout during the longer receipt run;
the completed test and symbolic logs were retained, and the probe was rerun separately.
Direct Git clone failed DNS resolution. Thus this is **not** a full native checkout,
repository-wide test/provenance run, hosted CI pass, or Lean proof. No source shim replaces
an imported implementation. The production dependency is the byte-matched original module.

The receipt contains finite horizons 16,32,64,128,256 and the PR320 explicitly different
zero-seeded rational nonnormal source as a negative control. These observations do not
validate a fitted rate or establish any infinite limit.

## 7. Next verdict-changing research, without rebuilding old machinery

The strongest positive result here is the source-specific positive gauge decomposition
and its bounded-error joint Fourier transport. The strongest strategic result is removing
irrelevant anti-diagonal requirements and exposing the exact two-clock filter saturation.

Now prove an **authentic zero-selected arithmetic bound** on signed quotient innovations
or their cumulative sum. Retain original carries, the complete odd-denominator character,
source labels and zero seed. The kernel-pair formula and the gauge let each discarded term
carry an explicit error budget. Compare the actual source with the same-forcing changed
seed, PR320 nonnormal forcing, the q=17 hidden-mode control, and #327/#328's normal finite-type
growing-energy countermodels. A new criterion alone is not a proof advance in the selected
Weyl order; a new signed arithmetic estimate is still owed.

Classical context: Bailey-Crandall (2001), *On the Random Character of Fundamental Constant
Expansions*, DOI 10.1080/10586458.2001.10504441; Lagarias (2001), *On the Normality of
Arithmetical Constants*, arXiv:math/0101055. Their source-shadowing warnings are retained.
