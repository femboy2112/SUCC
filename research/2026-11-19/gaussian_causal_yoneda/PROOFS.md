# Gaussian causal Yoneda: theorem dossier and hostile boundaries

**2026-11-19.** Paper proofs within declared domains. Classical Fourier, Hilbert,
Yoneda, heat-semigroup, and Hermite ingredients are credited, not claimed as
original mathematics. New-to-this-SUCC assembly is the source-anchored Gaussian
interface, explicit BBP rational transfer and original-four-pole obstruction.
No R0, pi normality, RH, or physical back-action theorem is claimed.

## Notation and source contract

Write `e(u)=exp(2*pi*i*u)`, `T=R/Z`, and use normalized Lebesgue measure on T.
Fix `lambda>0` and the **periodized Gaussian**

`K_lambda(u) = sum_(h in Z) exp(-lambda*h^2/2)*e(h*u)`.

It has mean one, is positive, and is the heat kernel at time
`t=lambda/(8*pi^2)`. Define `K_theta(u)=K_lambda(u-theta)`,
`Q_lambda=sum_(h != 0) exp(-lambda*h^2)`,
`S_lambda=sum_(h != 0) h^2 exp(-lambda*h^2)`,
`R_lambda=sum_(h != 0) |h| exp(-lambda*h^2)`.
All sums converge absolutely.

**Do not confuse three different objects:** a smoothed Dirac **representation**
`K_theta` of one actual phase; a Gaussian **random perturbation** of the
unknown source seed; and the **actual deterministic** phase `theta_n`.
Only the last is the arithmetic target. A smoothing ensemble must not be
silently interpreted as alternative physical histories.

The unique authenticated BBP source throughout is

```
r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)
U_0 = 0; U_n = 16 U_(n-1) + r(n)
x = pi/16; T_n = sum_(j>=1) 16^(-j)*r(n+j)
Y_n = U_n + T_n = 16^n*x
```

Let `theta_n=Y_n mod 1`, `A_B=(1/B)sum_(B<=n<2B)(1-cos(2*pi*theta_n))`,
`W_B(h)=(1/B)sum e(h*theta_n)`.
R0 means `liminf_(B->inf) A_B>0`; base-16 normality requires
`W_B(h)->0` for all `h!=0` (plus the standard shell-to-prefix argument).

## GYC-01 — characteristic Gaussian representation; inversion is unstable

For a finite signed Borel measure `mu` on T, put `Phi_lambda(mu)=K_lambda*mu`.
Fourier coefficients satisfy

`(Phi_lambda(mu))_hat(h) = exp(-lambda*h^2/2)*mu_hat(h)`.

Every multiplier is nonzero. If `Phi_lambda(mu)=Phi_lambda(nu)` in L2,
then all Fourier coefficients of `mu-nu` vanish. Trigonometric polynomials
are uniformly dense in continuous functions, hence `mu=nu`. Thus
`Phi_lambda` is injective on finite signed measures (a classical
characteristic/universal kernel fact on T).

But there is **no uniform inverse Lipschitz bound** from smoothed L2 to total
variation. For `0<a<1`, let

`dmu_N^+ = (1+a*cos(2*pi*N*u))du`,
`dmu_N^- = (1-a*cos(2*pi*N*u))du`.

Their total variation distance (probability convention, half the L1 norm)
is `2a/pi`, independent of N. Their smoothed L2 distance is exactly
`sqrt(2)*a*exp(-lambda*N^2/2) -> 0`. These are genuine positive probability
measures. Faithful encoding therefore does **not** supply finite-precision
recoverability. This is the crucial distinction between the abstract full
Fourier spectrum and lawful finite observer instruments.

## GYC-02 — Gaussian heat is a natural *scale-changing* causal observer

Let `T_b(u)=b*u mod 1` for an integer `b>=2` and let `(T_b)_*` be
pushforward of finite measures. Then for all `mu` and `lambda>0`,

`(T_b)_*(K_lambda*mu) = K_(b^2*lambda)*((T_b)_*mu)`.

Proof: the Fourier coefficient at h of the left side is the input coefficient
at `b*h`, namely `exp(-lambda*b^2*h^2/2)*mu_hat(b*h)`, equal to the right.
For BBP's radix `b=16`, the required factor is **256**. Rotations commute
with smoothing at unchanged lambda. A fixed-scale observer who forgets this
transport will measure a coordinate defect not intrinsic source mixing.

For the locked delta at zero, `K_lambda * (T_b)_*delta_0=K_lambda` while
`(T_b)_*(K_lambda*delta_0)=K_(b^2*lambda)`. The latter spreads toward Haar
under repeated application even though the authentic point remains locked.
This explicitly refutes any inference from Gaussian heat relaxation to
point-orbit mixing.

## GYC-03 — source-anchored Gaussian displacement ⇔ R0

Set `D_lambda(theta)=||K_theta-K_0||_L2^2`. Parseval gives

`D_lambda(theta) = sum_(h!=0) exp(-lambda*h^2)*|e(h*theta)-1|^2`.

For every integer h, the factorization of `z^h-1` yields
`|e(h*theta)-1| <= |h|*|e(theta)-1|`. The h=+1,-1 terms supply a lower bound.
Since `|e(theta)-1|^2=2*(1-cos(2*pi*theta))`,

`4*exp(-lambda)*(1-cos(2*pi*theta)) <= D_lambda(theta)`
`D_lambda(theta) <= 2*S_lambda*(1-cos(2*pi*theta))`.

Let `E_B=(1/B)sum_(B<=n<2B) D_lambda(theta_n)`. Averaging yields

`4*exp(-lambda)*A_B <= E_B <= 2*S_lambda*A_B`.

**Thus R0 iff `liminf E_B>0`**, for every fixed finite `lambda>0`.
This equivalence holds for any phase sequence, including locked countermodels.
It is not an independent arithmetic anti-lock inequality.

Frame covariance: under an arbitrary clock-dependent rotation `alpha_n`,
compare the moved observation `K_(theta_n-alpha_n)` with the **equally moved**
reference `K_(-alpha_n)`. Translation invariance gives exactly
`||K_(theta_n-alpha_n)-K_(-alpha_n)||^2=D_lambda(theta_n)`.
The observer can read zero in its moving chart while its compensated
source-reference distance remains nonzero. A truly locked zero phase has
zero compensated energy. Omitting the moving reference gives a false positive.

## GYC-04 — Gaussian distance to Haar ⇔ all-frequency normality

Let `M_B(u)=(1/B)sum_(B<=n<2B) K_(theta_n)(u)` and set
`V_B=||M_B-1||_L2^2`. Parseval gives

`V_B = sum_(h!=0) exp(-lambda*h^2)*|W_B(h)|^2`.

For each fixed nonzero h, `|W_B(h)|^2 <= exp(lambda*h^2)*V_B`.
Conversely, if every fixed `W_B(h)->0`, dominated convergence applies to
the summable series, since `|W_B(h)|<=1`, and gives `V_B->0`.
Thus `V_B->0` iff every nonzero shell Weyl mode vanishes, hence (by standard
bounded-shell-to-prefix subdivision) the orbit is base-16 normal when it
is a radix orbit. This is the classical kernel mean discrepancy to Haar,
recast on the authenticated source. It is *strictly stronger* than GYC-03.

For any finite cutoff H,
`0 <= V_B - sum_(0<|h|<=H) exp(-lambda*h^2)*|W_B(h)|^2`
`<= sum_(|h|>H) exp(-lambda*h^2)`.
Hence fixed finite Fourier measurements have explicit spectral tail budgets,
but a fixed nonzero tail bound alone does not prove a limit of zero.

## GYC-05 — mean-energy versus energy-of-mean split

The Hilbert variance identity gives

`E_B = ||M_B-K_0||_2^2 + (1/B)sum ||K_(theta_n)-M_B||_2^2`.

Expand the squares, use `sum(K_(theta_n)-M_B)=0`, and cancel the cross terms.
A fixed nonzero phase alpha has `E_B=D_lambda(alpha)>0` but
`V_B=Q_lambda>0`, for every B. A completely zero-locked orbit has
`E_B=0`, again `V_B=Q_lambda>0`. A normal orbit has `V_B->0` and
`E_B->2*Q_lambda`. These distinguish target-relative escape from anchor
from genuine Haar equidistribution. Positivity of E is not full mixing.

## GYC-06 — exact four-pole BBP tail and rational energy transport

Elementary reduction of the **unchanged** BBP source gives

`r(n)=(120n^2-89n+16)/((2n-1)(4n-1)(8n-7)(8n-3))`.

For n>=1, rational subtraction yields the exact positive expressions

```
r(n)-15/(64*n^2) =
 (9664*n^3-9656*n^2+3090*n-315) /
 (64*n^2*(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)) > 0

15/(64*n^2)-r(n+1) =
 (5696*n^3+7672*n^2+2910*n+225) /
 (64*n^2*(2*n+1)*(4*n+3)*(8*n+1)*(8*n+5)) > 0.
```

The first numerator is
`9664*n^2*(n-1)+8*n^2+3090*n-315 >0` for n>=1.
The inherited positive, decreasing tail identity gives
`0<T_n<r(n+1)/15<1/(64*n^2)`.

The derivative of D has Fourier bound
`|D_lambda'(theta)| <= L_lambda=4*pi*R_lambda`.
Define **rational-source**
`Ehat_B=(1/B)sum D_lambda(U_n mod 1)`.
The mean-value theorem and exact tail bound give, for every integer B>=1,

`|E_B-Ehat_B| <= L_lambda/(64*B^2)`.

Likewise define `Mhat_B=(1/B)sum K_(U_n mod 1)` and
`Vhat_B=||Mhat_B-1||_2^2`. Parseval gives
`||K'_lambda||_2=2*pi*sqrt(S_lambda)`. Thus

`|sqrt(V_B)-sqrt(Vhat_B)| <= 2*pi*sqrt(S_lambda)/(64*B^2)`.

The L2 norm is used only as a geometric instrument; **no source-selected
uniform lower bound on either rational energy has been proved.**
Finite Fourier cutoff H adds at most
`8*sum_(h>H) exp(-lambda*h^2)` to D and
`2*sum_(h>H) exp(-lambda*h^2)` to V; standard geometric tail estimates
make these effective. Numerical floating-point coefficients are not rigorous
outward-rounded error certificates until interval bounds are added.

## GYC-07 — original forcing creates positive but summable *local* energy

As n->infinity,
`r(n)=15/(64*n^2)+O(n^-3)`, from the original four signed poles.
Taylor expansion at theta=0 gives
`D_lambda(theta)=4*pi^2*S_lambda*theta^2+O(theta^4)`.
Consequently,

`D_lambda(r(n)) = (225*pi^2*S_lambda/1024)*n^-4 + O(n^-5)`.

At lambda=1 the coefficient is approximately 1.918158758866. The sum
`sum_(n=B)^(2B-1) D_lambda(r(n))=O(B^-3)`: every causal innovation can be
nonzero while its source-forcing energy becomes negligible on late shells.

**Fatal control:** keep this *identical* r(n) but choose seed `s=-x`.
Then `U_n(s)=-T_n`, `Y_n(s)=0` for every n, so `E_B=0` identically,
while `D_lambda(r(n))>0` for each n (for large n, 0<r(n)<1).
Thus raw forcing energy, even source-correct and positive at each step, does
not imply a uniform anti-lock lower bound.

## GYC-08 — exact seed alias of every late phase probe

The seeds `s` and `s+1/16` yield completed phases whose differences at
n>=1 are `16^n/16`, an integer. All circle observations, their complete
Gaussian images, all Fourier characters, and every phase-only path functor
at n>=1 therefore agree. Yet the unwrapped source seeds differ. The
source anchor, or an additional lawful early-time or lift probe, is
necessary to distinguish them. Even complete Gaussian phase tomography
identifies only the declared phase quotient, not the source-bearing model.

## GYC-09 — Gaussian seed microscope, Hermite no-go, precision bill

Let Z be standard Gaussian; perturb only the BBP seed counterfactually:
`F_(n,s)(Z)=exp(2*pi*i*h*16^n*(x+s+sigma*Z))`, h nonzero integer.
Writing `a=2*pi*h*16^n*sigma`, Gaussian integration gives

`E F_(n,s) = exp(2*pi*i*h*16^n*(x+s))*exp(-a^2/2)`.

The phase is preserved algebraically, but if sigma is fixed the coherent
amplitude decays as `exp(-2*pi^2*h^2*sigma^2*256^n)`. Keeping attenuation
at least delta in (0,1) requires

`|sigma_n| <= sqrt(-log(delta)/(2*pi^2*h^2))*16^(-n)`.

Thus a fixed-resolution Gaussian **source perturbation** rapidly loses
practical deconvolution stability; a co-moving microscope must pay about
`4n` binary digits of preparation scale. This is a resolution requirement
for this instrument, not a lower bound on all algorithms for pi digits.

Using probabilists' Hermite basis `H_k(Z)`, the exact chaos energies are
`exp(-a^2)*a^(2k)/k!`, independent of `s`. Hence the authentic zero seed
and locked counterseed have **identical** chaos-order energy ledgers.
A proof based only on their positive norms cannot distinguish them.
Retained complex coefficients do carry a common phase, which requires a
calibrated reference to interpret.

## GYC-10 — the forward one-sided near-lock window has logarithmic length

For n>=1, source positivity also yields the strict lower tail bound
`T_n >= r(n+1)/16 > 15/(1024*(n+1)^2)`.

Fix `0<epsilon<1/16`. Suppose at L consecutive chronological times
`j=N,...,N+L-1` the *completed* real-circle phase obeys
`T_j <= theta_j <= epsilon`, with theta chosen in `[0,1)`.
Then theta_j<1/16, so no radix wrap occurs and
`theta_(N+L-1)=16^(L-1)*theta_N`. Hence

`L <= 1 + log_16(1024*epsilon*(N+1)^2/15)`.

This is an original-source **finite-window polarity restriction**.
It does *not* apply when `theta_j<T_j`, precisely the near-upper-fringe
configuration of the locked counterseed, nor to phases near one.
It establishes an O(log N) bound on a particular orientation of a
near-zero streak, **not** a uniform signed shell anti-lock inequality.
The next question is whether prime cofactor and carry arithmetic can
control the excluded orientation with positive shell density.

## GYC-11 — a source-derived signed Gaussian witness would prove R0

Let `v_n=K_(theta_n)-K_0` in L2(T), and let `q_n` be an independently
specified, causally available source-derived L2 witness. Suppose there
exist constants c>0, M<infinity and B0 such that, for every B>=B0,

`| (1/B)sum_(B<=n<2B) <v_n,q_n> | >= c`, and
`(1/B)sum_(B<=n<2B) ||q_n||_2^2 <= M^2`.

Cauchy-Schwarz on the Hilbert direct sum indexed by shell times gives
`c <= sqrt(E_B)*M`; thus `E_B>=c^2/M^2`.
GYC-03 then yields

`A_B >= c^2/(2*S_lambda*M^2)` for every such B: **R0 follows**.

This is a precise conditional sufficient instrument, **not a new estimate**.
The missing arithmetic task is to authenticate `q_n` and prove its signed
nonzero cross-correlation for the **original zero seed**. A witness chosen
from the target `v_n`, an unbounded hidden partial sum, or a fit to already
used shells is circular. The same original forcing with seed `-x` has
`v_n=0`; any claimed source-blind positive c is refuted.

## GYC-12 — causal/Yoneda interface, strictly conditional

For carrier C, model M, legal action family A, and encoding E:C->M,
`E o T_a = T_hat_a o E` for all a implies the same equality for every
finite forward word by induction. If permitted output maps also factor
through E, all permitted finite predictions agree. The encoding recovers
only the reachable behavioral quotient unless the lawful observations
separate states and the model is precisely the represented image.

For a category of causal carriers, restricted Yoneda
`X |-> Hom_C(-,X)|_P` is fully faithful **when the chosen probe subcategory
P is dense in C**. This is a classical categorical theorem under its
hypotheses, not an assertion that the currently implemented BBP or Gaussian
probes are dense. For Gaussian observations, GYC-01 proves injectivity on
complete measure readouts, while its ill-conditioning and GYC-08 prove
that such faithfulness is narrower than full physical source identification.

A commuting square is correct *representation* of causality, not evidence
that the internal model *causes* the external system to change. A physical
back-action theorem would require an explicit controller/instrument and
counterfactual interventions showing model-dependent carrier transitions.

## Existing work, provenance, and literature

- SUCC Main XXVI: `81be6b897ae980b801a3b9de9e22ef81e8360bfb`;
  `docs/PI_NORMALITY_FRONTIER.md`, `docs/principia_observatoris/README.md`,
  `research/2026-11-10/cursed_categories_dedekind_yoneda/CUT_YONEDA_THEOREMS.md`.
- SUCC #668 five-channel observer; #670 Hensel/Jacobian locked-frame controls;
  #671 causal-generator reconstruction and signed completion;
  #663 Borwein/kernel discrepancy. These draft branches are cited only,
  **not silently imported**.
- Sriperumbudur, Gretton, Fukumizu, Schoelkopf, Lanckriet,
  *Hilbert Space Embeddings and Metrics on Probability Measures*,
  JMLR 11 (2010) 1517-1561:
  https://www.jmlr.org/papers/v11/sriperumbudur10a.html
  (characteristic kernels, nonuniform inverse geometry).
- Fourier uniqueness on finite measures, Parseval, Hermite chaos,
  Gaussian characteristic functions, Yoneda and restricted density:
  classical tools; no priority claims.
