# The missing diffusivity is exactly a retained-memory Schur term

**Date:** 2026-10-23. **Status:** complete paper proof for each fixed integer
radix, plus exact rational two-residue calibration. No Lean, physical-measurement,
or independently novel-theorem claim. This closes the next analytic target
identified in [the clock/heat manuscript](SOURCE_FAITHFUL_LIMITS_HEAT.md).

## RM-01: source-resolved Bloch fiber and quantitative resolvent theorem

Fix an integer `a>=2`. On the bilateral source write `n=am+r`, `0<=r<a`.
At coarse Bloch phase `z=exp(i theta)`, successor is the unitary a-by-a matrix

`T_a(z)e_r=e_(r+1)` for `r<a-1`, and `T_a(z)e_(a-1)=z e_0`.

For a>2 these are the usual cyclic entries; for a=2 both directions must be
retained when forming `T+T*`. Let

`L_h(theta)=h^-2(2I-T_a(z)-T_a(z)*)`,
`u=a^-1/2(1,...,1)`, `Q=I-uu*`,
`r_h(alpha,theta)=u*(alpha+L_h(theta))^-1 u`, `alpha>0`.

This is the finite-dimensional fiber of *bilateral* nearest-neighbor heat,
including the residue register. It is not a prime-FUCC fiber or a signed Weil
operator. The scalar r is the exact visible resolvent after eliminating the
hidden coordinates, not the reciprocal of the compressed visible generator.

For `theta=a h xi`, define `C_a=(a^2-1)/12`. For every real xi, h>0, alpha>0,

`|r_h(alpha,a h xi)-(alpha+xi^2)^-1|`
` <= h^2 [C_a xi^2/alpha + xi^4/(12 alpha^2)]`.                 (RM1)

Consequently on `|xi|<=R`, `alpha>=alpha_0>0`, convergence is uniform with
the explicit `O(h^2)` bound obtained by substituting R and alpha_0. This part
needs **no upper alpha bound** and no unverified high-frequency gap estimate.

### Proof

The eigenvalues of T are `exp(i phi_j)` with
`phi_j=(theta+2pi j)/a`, `0<=j<a`. Normalized eigenvectors have components
`a^-1/2 exp(-i r phi_j)`; the last-to-first equation uses
`exp(i a phi_j)=z`. Therefore

`lambda_j=4h^-2 sin^2(phi_j/2)`,
`w_j=|sum_(r=0)^(a-1) exp(i r phi_j)|^2/a^2`,
`r_h=sum_j w_j/(alpha+lambda_j)`, `w_j>=0`, `sum_j w_j=1`.        (RM2)

With theta=a h xi, `phi_0=h xi`. The finite double sum gives

`1-w_0 = a^-2 sum_(r,s) [1-cos((r-s)h xi)]`
`      <= (h^2 xi^2/(2a^2)) sum_(r,s) (r-s)^2`
`       = C_a h^2 xi^2`.                                      (RM3)

The last equality uses
`sum_(r,s)(r-s)^2=a^2(a^2-1)/6`, an elementary finite sum. Also

`0<=xi^2-lambda_0<=h^2 xi^4/12`.                               (RM4)

The first inequality is `|sin x|<=|x|`. The second follows from the same
quartic cosine bound used in the heat manuscript and is valid globally.

All reciprocals in (RM2) lie in `[0,1/alpha]`, hence

`|r_h-(alpha+lambda_0)^-1| <= (1-w_0)/alpha`.

The difference between `(alpha+lambda_0)^-1` and `(alpha+xi^2)^-1` is at most
`h^2 xi^4/(12alpha^2)` by (RM4). Combine with (RM3). QED.

The proof bounds the other branches by their *total overlap weight*. It does
not count correlated evaluations of spectral branches as independent evidence.
Fixed a is essential to the stated asymptotic: C_a grows quadratically.

## RM-02: quantitative recovery of the memory correction

Relative to `span(u) direct-sum Q C^a`, write

`L_h = [[A_h, B_h], [B_h*, D_h]]`.

Then

`A_h=(2-2cos(theta))/(a h^2)`,
`r_h^-1=alpha+A_h-B_h(alpha+D_h)^-1 B_h*`.                      (RM5)

The inverse exists because `L_h>=0` and alpha>0. Formula (RM5) follows by
solving the hidden row of the block system. No bounded-below estimate on D_h
is needed. Its correction

`C_h(alpha,theta)=B_h(alpha+D_h)^-1B_h* >=0`

has a nontrivial continuum limit. For every fixed `R>=0` and
`0<alpha_0<=alpha_1<infinity`, impose

`a h R <= pi`, `C_a h^2 R^2 <= 1/2`.                           (RM6)

Uniformly for `|xi|<=R` and `alpha in [alpha_0,alpha_1]`,

`|r_h^-1-(alpha+xi^2)|`
` <= h^2 [R^4/12 + 2 C_a R^2(alpha_1+R^2)]`,                  (RM7)

and

`|C_h(alpha,a h xi)-(a-1)xi^2|`
` <= h^2 [(a^3+1)R^4/12 + 2 C_a R^2(alpha_1+R^2)]`.           (RM8)

Thus the exact retained-memory term removes the excess diffusivity `a-1`
from the naive visible generator. This is an actual calculated correction,
not an analogy between hidden information and diffusion.

### Proof

When `|theta|<=pi`, the eigenangle `phi_0=theta/a` is a closest root angle to
zero modulo `2pi`. Accordingly `lambda_j>=lambda_0` for every j. Put
`delta=C_a h^2 R^2<=1/2`. Equations (RM2)--(RM3) imply

`(1-delta)/(alpha+lambda_0) <= r_h <= 1/(alpha+lambda_0)`.

Taking reciprocals,

`0 <= r_h^-1-(alpha+lambda_0)`
`   <= delta (alpha+lambda_0)/(1-delta)`
`   <= 2 C_a h^2 R^2 (alpha_1+R^2)`.

Combining with (RM4) proves (RM7). The exact visible coefficient in (RM5)
satisfies the coarse-mesh dispersion estimate

`|A_h-a xi^2| <= a^3 h^2 xi^4/12`.

Now rearrange `C_h=alpha+A_h-r_h^-1` and apply (RM7), obtaining (RM8). QED.

The lower alpha bound is needed for the resolvent estimate (RM1); the proof
of (RM7)--(RM8) only needs alpha>0 and a bounded upper alpha on this compact
frequency band. We keep the common closed alpha interval to state both
theorems together. The code checks the rational sufficient condition
`a h R<=3<pi`, rather than converting a floating value of pi to evidence.

## RM-03: complete two-residue formula and an order-of-limits counterexample

For a=2 let `c=cos(theta)`, `s=sin(theta)`. With hidden unit vector
`v=(1,-1)/sqrt(2)`, direct source-basis multiplication gives

`A_h=(1-c)/h^2`, `D_h=(3+c)/h^2`, `B_h=i s/h^2`,

up to the explicitly reversible choice of Fourier orientation for B. Thus

`C_h=(1-c^2)/(h^4[alpha+(3+c)/h^2])`,
`r_h^-1=alpha+(1-c)/h^2 * (alpha h^2+2)/(alpha h^2+3+c)`.        (RM9)

The raw B phase changes sign under conjugating the Fourier convention; its
norm-square does not. Cosine alone therefore identifies the scalar Schur
correction but does not authenticate that phase. At theta=0 the coupling is
zero and `r=1/alpha`. At theta=pi the coupling is again zero, but the visible
generator is `2/h^2`; this is not the zero-frequency branch.

**No uniform memory limit on all alpha>=alpha_0.** Take

`theta_h=2 arctan(h)`, `xi_h=arctan(h)/h ->1`, `alpha_h=h^-4`.

Then `c_h=(1-h^2)/(1+h^2)` and (RM9) yields

`0<=C_h(alpha_h,theta_h)<=4h^2 ->0`,

whereas `(a-1)xi_h^2 ->1`. Thus the bounded upper-alpha condition in (RM8)
is necessary for that uniform conclusion. This does **not** contradict the
uniform resolvent estimate (RM1), since both resolvents shrink as alpha grows.

## Exact executable calibration

`source_faithful_resolvent.py` evaluates (RM9) using Fractions and exposes
the visible generator, hidden generator, coupling magnitude, memory correction,
effective denominator, true visible resolvent, and false memory-deleted
resolvent separately. It also returns the general-a rational bounds.

The independent two-by-two check works in the original residue basis:
for `z=c+is`, the diagonal of `alpha+L_h` is `d=alpha+2/h^2`, its off-diagonal
squared magnitude is `[(1+c)^2+s^2]/h^4`, and the uniform matrix coefficient
of the inverse is

`[d+(1+c)/h^2]/[d^2-((1+c)^2+s^2)/h^4]`.

This is compared exactly against the Schur route for rational unit-circle
phases, including both endpoints. Further checks use rational
`z=(1+ih)/(1-ih)` and an independent alternating-series bracket for arctan(h)
to enclose the corresponding physical frequency. They check (RM1), (RM8),
the disappearing-memory high-alpha control, and the detected false mutation
that omits memory. These seven tests calibrate finite algebra and interval
budgets; RM-01 and RM-02 remain paper proofs over all declared parameters.

## What changed, and the remaining boundary

The earlier noncommuting-limit theorem said that removing the environment
before evolving changes H_t to H_(a t). We can now quantify the exact missing
term: in the low-frequency resolvent, retained memory contributes
`(a-1)xi^2+O(h^2)`, restoring the ordinary Laplacian. This closes a concrete
source-preserving renormalization calculation.

These are elementary consequences of the finite polyphase/Bloch decomposition
and Schur complement, written out rather than treated as a new fundamental
law. The scholarly novelty claim remains unverified. The classical provenance
for cyclic Fourier eigenvalues and projection-memory interpretation is the
same as in the accompanying heat manuscript; no additional external theorem
is assumed here.

The result does not identify a signed Weil source, remove its Gamma/pole/contact
obligations, certify named arithmetic spectral cyclicity, or authorize a
physical intervention. It is uniform for each **fixed** radix. A subsequent
precise question is whether useful error control survives a refinement regime
`a=a(h)->infinity` while retaining an explicitly stated finite observation
band. The existing estimates already give sufficient conditions such as
`a(h)^3 h^2 ->0` for the absolute memory error at bounded R and alpha; they
do not certify optimality. The source-scale condition `a(h)h->0` alone is
weaker and does not imply the current sufficient memory-error condition. The first test of a
stronger assertion is its exact Bloch fiber, including weights, without
discarding the growing environment.
