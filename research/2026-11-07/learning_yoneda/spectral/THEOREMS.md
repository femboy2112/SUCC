# Continuous pin audit and the cost of predicting through finite bandwidth

Status: **PROVED LOCAL paper mathematics**, with exact finite checks in
`independent_oracle.py`. No Lean certificate, external referee, worldwide
priority claim, or original-zero cancellation theorem. This work adds a
quantitative observer limitation to the read-only #541–#543 stack.

## SP-1. The claimed half-aperture constant survives independent derivation

Use the forward-window convention of #543. For a finite measure on T=R/Z,

`R_k mu(y)=2 int_{0 <= {x-y} < 1/2} exp(-2 pi i k {x-y}) dmu(x)`.

The h-th Fourier multiplier is `a_(h-k)`, with `a_0=1`, `a_r=0`
for nonzero even r, and `a_r=2i/(pi r)` for odd r. For a **real** zero-mass
measure eta, Parseval and conjugacy give

`D(eta)^2 = ||R_0 eta||_2^2+||R_1 eta||_2^2
           = sum_(h != 0) w_h |m_h(eta)|^2`,

where

* `w_(+/-1)=4/pi^2+1/2`;
* `w_h=4/(pi^2 h^2)` for odd `|h|>=3`;
* `w_h=4(h^2+1)/(pi^2(h^2-1)^2)` for nonzero even h.

These are the **symmetrized** weights. Using the unsymmetrized complex
weights `|a_h|^2+|a_(h-1)|^2` gives a different optimization problem.
For `T_(b,a)(x)=bx+a`, b a positive integer,

`sup_(mu != nu) D(T_*mu-T_*nu)/D(mu-nu)
 = sup_(h>=1) sqrt(w_h/w_(bh))`.

The upper bound follows by Fourier reindexing. Equality of each candidate
ratio is realized by the probabilities `1 +/- epsilon cos(2 pi b h x)`,
`0<epsilon<=1`. Thus no unrealizable Hilbert vector is needed.

For even b>=2, write t=b^2 and u=h^2. The even-h ratio is

`r_t(u) = (u+1)(tu-1)^2 / ((u-1)^2(tu+1))`.

Its logarithmic derivative has numerator

`-(t-1)(3tu^2+(t+1)u+3)`

over positive denominator `(u+1)(u-1)(tu-1)(tu+1)`. It decreases on
u>1. The odd h>=3 ratios are below b^2, whereas h=2 is above b^2.
The maximum is therefore at h=1 or h=2. At b=16,

`w_2/w_32 = (5/9) (1023^2/1025) = 116281/205`,

and `pi<22/7` already puts the h=1 candidate below this value. Consequently

**`C_16 = 341/sqrt(205)`**, attained by the input frequency 32 cosine laws.

This is an expansion bound, not contraction or arithmetic cancellation.
The universal frame bounds are also correct:

`4/pi^2 <= h^2 w_h <= 4/pi^2+1/2`.

The even maximum uses `h=2` and `pi^2>88/9`; the oracle certifies a
sufficient pi interval from the alternating Machin series, without a
floating pi value. The lower bound is attained at every odd |h|>=3.

## SP-2. Other load-bearing operator hypotheses

For every proper aperture 0<alpha<1, put omega=exp(-2 pi i alpha).
Distributional differentiation of the two moving endpoints gives

`alpha D R_0 mu = tau_(-alpha)*mu - mu`,
`alpha (D-2 pi i) R_1 mu = omega tau_(-alpha)*mu - mu`.

Subtracting omega times the first identity yields exactly the #543 inverse

`mu = alpha ((D-2 pi i)R_1 mu - omega D R_0 mu)/(omega-1)`.

The proof includes mass. It requires complete translated profiles, proper
aperture, known phase convention, and distributions rather than pointwise
derivatives at atom seams. The inverse is of order one, stable in H^-1;
it does not promise total-variation stability.

The cross-channel condition `W_0 f_1=W_1 f_0`, mass one, and positivity
of the inverse are jointly necessary and sufficient for realization. The
coherence condition cannot be omitted: adding `epsilon exp(2 pi i y)`
to f_1 keeps the inverse unchanged but leaves the compatible range.
The #542 positive-definite moment criterion and #543 positive inverse
criterion describe the same probability range. Their forward/backward
convolution signs must be conjugated consistently; they are not identical
arrays without that convention map.

The affine observer operators compose on the compatible range. On the
ambient pair space, the identity action is a projection. Reject transverse
channel defects before projection. This matters when interpreting a finite
implementation as a functor; it is not a new category class.

The #541 B2 inverse uses two derivatives, with sharp affine norm b^2.
The two-tone inverse uses one derivative and gives the above norm.
Both are law reconstruction results. Neither reconstructs unwrapped
integer carries or a history without the corresponding source fields.

## SP-3. A sharp rate for finite-band learning, uniform in memory depth

Fix integer b>=2, sensor bandwidth H>=1, memory depth N>=0, and future
horizon k>=1. Let a_1,a_2,... be **any prescribed known** circle translations.
The law evolves by `x_(n+1)=b x_n+a_(n+1) mod 1`. The source family here is
**all initial Borel probability laws**, with the same prescribed forcing.
Write `B=b^k` and `W=sum_(h!=0)w_h=3-4/pi^2`.

At every time 0<=n<=N, the observer receives all exact complex moments
`m_h(mu_n)` for |h|<=H, with phase references known and bound to the
source. This is equivalent to receiving those Fourier modes of both
two-tone profiles. An observer can retain the complete transcript and
compute any function of it; adaptive choices from this menu cannot provide
more information than the full transcript.

Let `R_(H,N,k)` be the infimum, over all deterministic estimators of the
future centered two-tone surface from this transcript, of the supremum
L2⊕L2 error over the stated initial laws. Estimators may output arbitrary
L2 pairs, so the lower bound also applies when they are required to output
realizable surfaces. The upper bound below permits arbitrary L2 outputs.

Then, with `q=ceil(2H/B)` and `L=floor(H/B)`,

**`1/(2 pi^2 q) <= R_(H,N,k)^2 <= sum_(|h|>L) w_h`.**

In particular, for H>=B,

**`B/(6 pi^2 H) <= R_(H,N,k)^2
  <= 4(4/pi^2+1/2) B/H`.**

For H<B the lower bound is at least `1/(4pi^2)` and the upper bound W.
Thus the sharp uniform order is

**`R_(H,N,k) = Theta(sqrt(min(b^k/H,1)))`, uniformly in N and forcing.**

The constants are explicit but are not claimed to be optimal.

### Constructive lower-bound proof using positive laws

For integer M>=1 define the Fejer probability density

`F_M(x)=M^-1 |sum_(j=0)^(M-1) exp(2 pi i jx)|^2`,
`m_h(F_M dx)=(1-|h|/M)_+`.

Set R=H b^N and choose the two **genuine probabilities**

`mu=(delta_0+F_R dx)/2`, `nu=F_(2R) dx`.

Their moment difference at frequency l is

`d_l=0                          if |l|<=R;`
`d_l=(|l|/R-1)/2               if R<|l|<2R;`
`d_l=1/2                       if |l|>=2R.`

Every sensor reading through time N accesses an initial frequency
`b^n h` of magnitude at most Hb^N=R, multiplied by the same known source
phase. Therefore the full transcripts of these two laws are identical,
including every adaptive transcript over the declared menu. At time N+k,
their moment difference has magnitude 1/2 whenever |h|>=q. Hence

`D(mu_(N+k)-nu_(N+k))^2 >= (1/4) sum_(|h|>=q) w_h
 >= (2/pi^2) sum_(h=q)^infinity h^-2 >= 2/(pi^2 q)`.

Any single estimate of these identical data errs on one target by at least
half their distance. This proves the lower bound. If H>=B then
`q<=2H/B+1<=3H/B`. If H<B then q<=2. If B>=2H, both Fejer densities
push exactly to Haar; the two target laws are `(delta_a+lambda)/2` and
lambda. Their distance squared is exactly W/4, giving the stronger
radius lower bound W/16 in this regime.

### Upper-bound proof

Use the final observed law at time N. To predict at N+k, its Fourier
coefficient at h is the known phase times `m_(Bh)(mu_N)`. Retain this
exactly for |h|<=L and set the other centered surface modes to zero.
Every missing probability moment has magnitude at most one. Parseval
therefore gives squared error at most `sum_(|h|>L)w_h`.
For L>=1, the frame upper bound and `sum_(h>L)h^-2<=1/L` yield
`2(4/pi^2+1/2)/L`; if H>=B then L>=H/(2B). This proves the displayed
bounds, and the finite-band predictor is explicitly specified.

### Consequence and scope

For worst-case error epsilon below the saturation constant, uniform
future prediction requires bandwidth of order at least `b^k/epsilon^2`.
Unlimited retained history does not remove that cost for this continuum
law family. This is a quantitative form of the learning/resource gap;
it does not deny an adaptive advantage on a restricted finite source family.
The adversarial pair depends on the finite depth N. This is a uniform
finite-resource theorem, not one fixed pair that survives every infinite
observation. Nor does it claim that every fixed initial law attains the
worst-case bound.

The theorem applies to the **same authentic four-pole BBP forcing** by
choosing b=16 and a_n=r(n) mod 1. Its hostile pair changes the initial law;
it is not in the singleton source family with literal U0=0. For that
singleton, source knowledge already determines the exact rational history,
and the minimax obstruction is inapplicable. It cannot refute normality,
nor prove cancellation from knowing the zero selector.

## SP-4. Full history × sensor energy bookkeeping

Let v_n be any common-gauge centered spatial response in a real or complex
Hilbert space, from golden, two-tone, B2, or finite Fejer probes. Let P be
any finite partition of the time indices, with cell masses p_C and cell
means v_C. Define global mean v. Direct expansion with conjugates gives

`sum_C p_C ||v_C||^2 = ||v||^2 + sum_C p_C ||v_C-v||^2`,

and refining P to P' gives exactly

`E(P')-E(P)=sum_C sum_(D subset C) p_D ||v_D-v_C||^2 >=0`.

For each cell one must retain the signed cross terms

`||v_C||^2 = |C|^-2 sum_(n,m in C) <v_n,v_m>`.

For a fixed realized transcript, adaptive memory only chooses a partition
and the same identity holds. No independence, random seed, or stochastic
martingale assumption is needed. #535 and #540 prove the special dyadic
versions; this extension to arbitrary history partitions is classical
conditional variance, not an original-source signed estimate.

**Exact sharp hostile control:** a constant-phase completed orbit makes
all v_n identical, so every refinement increment is zero and the global
energy stays at W for the two-tone bed. In authentic BBP forcing it is
realized by the changed seed s*=-pi/16 with U_n(s*)=-T_n; its empirical
two-tone energy tends to W. Periodic completions similarly retain non-Haar
energy. Conversely a zero-sum two-cell example v_1=-v_2 has global energy
zero and positive refined energy. This rules out either sign of global
signed interference being forced by local positive sensor energies.

## SP-5. Reconciliation with the critical Fejer and golden fronts

The #533 logarithmic frequency-ray rigidity is valid for expanding-orbit
limits; #536 transports critical **square-root** energy at O(1) on full
prefixes; #538 improves this to O(A^-1/2) on epochs. The latter estimate
does not automatically give an o(1) difference of unsquared critical
energies without an energy bound. #540's fixed golden kernel and #543's
two-tone kernel separately have Lipschitz pair kernels and O(A^-2)
unsquared energy transport. These statements concern different observables
and are compatible.

All such transport estimates survive the coherent same-forcing wrong seed.
All positive response/realization/frame identities survive it as well.
Therefore the combined operator stack supplies no new source-selected
signed-correlation inequality. The critical missing arithmetic statement
remains, for example, `C_(A,A)^U=o(log A)` at every sufficiently large
epoch, or a genuinely sufficient one-sided collision/return estimate.

**Next discriminator:** derive that estimate from the literal zero seed
and the chronological rational source, while demonstrating the step that
fails for s*. The finite-band theorem identifies a concrete observation
cost; it pays none of this arithmetic debt.
