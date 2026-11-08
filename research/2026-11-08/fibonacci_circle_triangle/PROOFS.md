# Golden integer-clock circle triangulation × SUCC Pascal source × signed π observability

**2026-11-08, research branch only.** Original SUCC source and literal `U_0=0` are unchanged. Result labels FCT-01…FCT-07 are **new-to-this-branch mathematical syntheses**; the two-gap/Fibonacci facts and classical interpolation/rotation obstruction are not claimed as globally novel. **π base-16 normality, original-zero signed Weyl decay, and RH remain OPEN.** Finite numeric experiments do not prove asymptotics. This dossier states complete proofs and explicit negative controls.

## Source passport and three distinct arrows

Let `alpha = (sqrt(5)-1)/2 = 1/phi`, `F_0=0,F_1=1`. Two systems must remain separate:

1. Golden sampling of the abstract circle: `v_n = exp(2 pi i n alpha)`. This is **not** the actual BBP orbit.
2. Original source-selected BBP: `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16 U_(n-1)+r(n)`. Real phases are `x_n={U_n}`. The completed phase is `16^n*pi/16`, with `0<T_n=sum_(j>=1)16^-j r(n+j)<1/[15(n+1)^2]`.
3. Conditional Pascal observation of the genuine *positive* four-pole source `R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5)` under `mu_a(dx)=exp(-ax)Q(x)dx/R(a)`, `Q(x)=4-2 exp(-3x)-exp(-4x)-exp(-5x)>0`. The binary sensor's bits are NOT pi digits.

Source references: `docs/OPERATIONAL_TRIANGLE.md`, `research/2026-10-29/operational_triangle_frontier/THEOREMS.md` (TG-01…TG-09), `research/2026-10-29/golden_gamma_farey_twist/README.md` (Farey triangles), `research/2026-10-26/OILY_LOG_CLOCK_HILBERT_TRANSPORT.md` (phase-bearing positive observation), `docs/PI_NORMALITY_FRONTIER.md`, and draft #544's actual-source covariance. Do not identify the three types by analogy.

## FCT-01 — exact Fibonacci gaps, source-independent, PROVED (classical arithmetic)

For every integer `k>=3`, let `P_k` be the convex polygon whose vertices in circular order are `{v_n: 0<=n<F_k}`. The circle partition has **exactly**:

- `F_(k-1)` long gaps `L_k=alpha^(k-2)` turns;
- `F_(k-2)` short gaps `S_k=alpha^(k-1)` turns.

Both sizes are in `Z[alpha]`, and the total is exactly one: `F_(k-1)*L_k+F_(k-2)*S_k=1`. The long gaps lie in the signed direction `sigma_k=(-1)^(k-1)` from old vertices with labels `j=0,...,F_(k-1)-1`; all other old vertices have a short gap in that direction.

**Full induction.** The Fibonacci identity `F_k alpha-F_(k-1)=(-1)^(k-1)alpha^k` follows from `alpha^2+alpha=1` and the Fibonacci recurrence; check k=1,2, then induct. Base k=3: `P_3` consists of `0,alpha`, with positive forward gaps `alpha` and `alpha^2`, and exactly the specified long start j=0. At step k→k+1 the new labels are `F_k+j`, `0<=j<F_(k-1)`. Their positions are the old positions `j alpha` shifted by `sigma_k alpha^k`; each lies strictly inside its *distinct* long gap, since `L_k=alpha^(k-1)+alpha^k`. Thus the long gap splits into `alpha^k` next to the old vertex and `alpha^(k-1)` beyond the new vertex. Old short gaps stay `alpha^(k-1)`. The new counts are `F_(k-1)` short and `F_(k-1)+F_(k-2)=F_k` long. In the opposite new direction every old vertex j<F_k has a long gap immediately adjacent (it was either an old short gap or the remaining part of a split long gap), whereas every new vertex has a short one. This establishes the stronger labeled induction invariant. **No three-gap theorem is required as an unproved import.** This is also a specialization of known golden rotation spacing/three-gap results, not a claim of novel priority.

There are exactly `F_(k-1)` new triangles in the planar annulus `P_(k+1)\P_k`, one for each former long arc. Each new point lies on the circular arc outside its old chord; convexity gives disjoint triangle interiors. Thus integer-clock circle accumulation **literally constructs a nested triangulation of the disk**.

## FCT-02 — exact curvature area, Fibonacci scaling and BBP tail-matching, PROVED

For a circle of radius `R>0`, the triangle added at each old long gap is congruent. Its area is

`tau_k=2 R^2 sin(pi alpha^(k-2)) sin(pi alpha^(k-1)) sin(pi alpha^k)>0`.

Proof: for three ordered circle vertices with successive arcs `a=alpha^k`, `b=alpha^(k-1)`, the Euclidean oriented triangle area is `R²/2[sin(2pi a)+sin(2pi b)-sin(2pi(a+b))]`; the displayed product is the sine-addition identity with `a+b=L_k`. Reversing orientation changes signed area but not absolute area. Consequently `Area(P_(k+1))-Area(P_k)=F_(k-1)tau_k` exactly.

The polygon's area and its missing circular area are

`Area(P_k)=R²/2[F_(k-1)sin(2pi L_k)+F_(k-2)sin(2pi S_k)]`,

`D_k=pi R²-Area(P_k)=R²/2[F_(k-1)(2pi L_k-sin(2pi L_k))+F_(k-2)(2pi S_k-sin(2pi S_k))]>0`.

The first equality is the shoelace formula in circular order; the second uses the total angular gap exactly `2pi`. Since `theta-sin(theta)=theta³/6+O(theta^5)` and `F_k=(phi^k-(-alpha)^k)/sqrt(5)`, we get

`lim_(k→infty) F_k² D_k/R²=C_gold`,

`C_gold = [2pi³/(15 sqrt(5))]*(phi^5+phi) = 23.495653453930634...`.

Indeed the two leading terms become respectively `phi^5/(5 sqrt(5))` and `phi/(5 sqrt(5))` after multiplying by `F_k²`, giving the constant. Individual new triangles have area `Theta(alpha^(3k))`; their number is `Theta(alpha^(-k))`, so each layer gains `Theta(alpha^(2k))`. Thus a sequence of **integer-clock inscribed polygons** recovers the circle's Euclidean area with quadratic error in its number of points.

For the original source Green tail, the existing exact four-pole expansion gives `T_n=1/(64n²)+O(n^-3)` (unconditional; no normality assumption). Therefore along **the independent index substitution** `n=F_k`, the two shrinking positive quantities have an exact comparative limit

`lim_(k→infty) D_k/T_(F_k)=64 R² C_gold`.

**Truth boundary:** The numerical exponent match does not identify the golden mesh as a dynamical factor of BBP, does not use the zero seed, and does not constrain signed Weyl correlations. It makes the geometric resolution scale compatible with the authentic tail *after an explicit normalization*, not an arithmetic explanation of normality.

## FCT-03 — Pascal grade→circle harmonic functor and non-Haar native limit, PROVED (TG + exact finite algebra)

At source clock `a>0`, take the authentic positive law `mu_a` and m conditionally independent binary observations with failure probability `f(X)=exp(-8X)`, success `g(X)=1-f(X)`. Grade `J` has exact rational probabilities

`q_(a,m)(j)=binom(m,j)/R(a)*sum_(t=0)^j (-1)^t binom(j,t)R(a+8(m-j+t)), 0<=j<=m.`

This is TG-01's measure-valued Pascal recursion after taking total masses, not the deterministic BBP digit law. Embed grade j as `z_j=exp(2pi i j alpha)` and retain the complex harmonic sensor:

`Phi_(a,m)(h)=sum_(j=0)^m q_(a,m)(j) z_j^h
 = R(a)^-1 sum_(t=0)^m binom(m,t) z_h^(m-t)(1-z_h)^t R(a+8t)`, `z_h=exp(2pi i h alpha)`.

Proof: conditional on X, the grade generating function is `[f(X)+z_h g(X)]^m`; expand the mth power and use the exact four-pole Laplace shifts. For m=2, the three points z0,z1,z2 are distinct on a circle; no line intersects the circle in three distinct points. Thus the probability q0,q1,q2 is determined uniquely by **one coherent complex reading** Phi plus known total mass 1. The latent source posterior is not recovered by those three masses.

More generally `Phi(h),h=0,...,m` form a Vandermonde system in nodes `z_j`; it is invertible because alpha is irrational. One explicit (very small) determinant lower bound follows from the quadratic norm:

`||q alpha||>=1/(sqrt(5)q+1/2)` for every positive integer q, hence

`|det V|=product_(0<=i<j<=m)|z_j-z_i|>=product_(q=1)^m[4/(sqrt(5)q+1/2)]^(m+1-q)>0`.

Proof: nearest integer p to q alpha gives nonzero integer norm `(p-q alpha)(p+q phi)=p²+pq-q²`; bound the second factor by `sqrt(5)q+1/2`. Use `2|sin(pi q alpha)|>=4||q alpha||`. Finite invertibility is not uniformly conditioned at growing m. This is *target-relative finite Yoneda-like reconstruction*, not full categorical Yoneda full faithfulness without actual Hom-objects.

At the **native source scale** `a_n=8n-7,m=n`, TG-04 already proves rescaled `a_n X ⇒ Gamma(2,1)` and conditional grade tends to `Poisson(Y)` given Y, so `J ⇒ NegativeBinomial(2,1/2)` with masses `(j+1)/2^(j+2)`. Hence for every fixed nonzero h,

`lim_(n→infty) Phi_(a_n,n)(h) = (2-z_h)^(-2)`.

It is never zero, and its modulus is at least `1/9`; because h alpha is dense mod1, this bound is sharp as an infimum across integer h. **The circle-embedded native Pascal triangle is NOT asymptotically Haar.** This is an exact negative control: geometric completeness and an auxiliary golden fixed point DO NOT make an actual π source orbit normal. If one first holds `a` fixed and sends m→∞, the circle modes instead tend to zero by dominated convergence because `0<f(X),g(X)<1` almost surely. These two regimes do not commute, which is exactly why observation scale and source chronology are load-bearing.

## FCT-04 — target-sufficient golden finite-element pin and O(A^-2) original-source transfer, PROVED

Use the sorted vertices `t_j={j alpha}` for `0<=j<F_k`, and circular gap lengths `ell_j in {L_k,S_k}`. On the jth circular interval `[t_j,t_(j+1)]` (unwrapped across 1 as needed), write `x=(1-u)t_j+u t_(j+1)` in the **arc-length coordinate** with `0<=u<=1` and define its complex linear interpolant

`I_(k,h)(x)=(1-u)e(ht_j)+u e(ht_(j+1))`, `e(t)=exp(2pi i t)`.

The second-derivative interpolation remainder is pointwise

`|e(hx)-I_(k,h)(x)| <= (2pi|h|)² ell_j²/8 <= (pi² h²/2) L_k² =: eta_(k,h)`.

Both the true character and its interpolant have modulus ≤1. Integrating the interpolant against the original epoch empirical measure and Haar uses **only the barycentric nodal masses** (for Haar, weight at vertex j is `(ell_(j-1)+ell_j)/2`). Define the signed nodal difference mode `P_(A,k)(h)=int I_(k,h) d(mu_A^U-Haar)`. For each integer A≥2 and h≠0,

`|c_A^U(h)-P_(A,k)(h)| <= 2 eta_(k,h) = pi² h² L_k²`.

The factor 2 pays for empirical and Haar interpolation separately (the latter has exact character mean 0). This is a *phase-sensitive* deterministic instrument; absolute nodal TV bounds are optional and unproved. Choose k=k(A) such that `F_k<=A<F_(k+1)`; Binet gives `F_k L_k<2`, while `F_(k+1)<=2F_k`, hence `L_k<4/A`. So

`|c_A^U(h)-P_(A,k(A))(h)| < 16 pi² h²/A²`.

By the **authentic original U0=0** Green-tail transport,

`|c_A^pi(h)-P_(A,k(A))(h)| < 16 pi² h²/A²+2pi|h|/[15(A+1)²]`.

This is an unconditional, **source-faithful O_h(A^-2) approximation of the signed Fourier target**. It is not a bound on P itself, and it does not prove c→0. A mesh of order A requires O(A) nodal features; applying an unsigned L1 occupancy bound to all of them would be stronger than normality and is NOT assumed.

## FCT-05 — retain history: second-order signed lag/Fejer energy transfer, PROVED

For an ordered epoch `x_0,...,x_(A-1)` (the authentic BBP choice is `{U_(A+j)}`), put `z_j=e(hx_j)` and `v_j=I_(k,h)(x_j)`. For any `1<=H<=A`, zero-extend the vectors and define the finite causal Gram energy

`E_H(z)=[1/(A H²)] sum_(t in Z) |sum_(s=0)^(H-1)z_(t+s)|²`.

Since `|z_j|=1`, `|v_j|<=1`, and `|z_j-v_j|<=eta_(k,h)`, every t-block sum has difference at most H eta; the l2 translate triangle inequality, or the exact signed lag expansion, gives

`|E_H(z)-E_H(v)|<=2 eta_(k,h)=pi² h² L_k²`.

A direct proof using the energy expression: H1's diagonal `(1/(AH))sum|z_j|²` differs by at most `2eta/H`, while each lag product `z_(j+ell)conj(z_j)` differs from its v counterpart by at most `2eta`. The weighted off-diagonal lag coefficients sum to `(H-1)/H`; total error ≤`2eta`. This preserves **all signed chronological cross terms**. The v_j are representable by two neighboring golden vertices and the time-label j. If those labels are discarded, permuting the same points leaves their static pin distribution unchanged while changing E_H. The instrument must be a *learning history*, not just a spatial snapshot.

At `k(A)`, the error is `O_h(A^-2)` **uniformly in the lag aperture H**, including H≈sqrt(A) and H=A. This gives a candidate observation interface for #544's exact-forcing signed-covariance gate but no arithmetic upper bound on the resulting energy. A coherent nonnormal control has energy `1-(H²-1)/(3AH)` (for H≤A) and the interpolation reproduces it exactly when all phases are 0: no false Haar claim.

## FCT-06 — no direct time-equivariant golden circle to radix-16 circle, PROVED NEGATIVE

Let `R_alpha(x)=x+alpha mod1` and `T_16(y)=16y mod1`. Every continuous `f:S^1→S^1` satisfying `f∘R_alpha=T_16∘f` is **constant** with value among the fifteen fixed points of T_16.

Proof: uniform continuity provides δ>0 so `d(x,y)<δ` implies `d(f(x+n alpha),f(y+n alpha))<1/32` for every n≥0, because the input rotation is an isometry. Equivariance gives `d(16^n f(x),16^n f(y))<1/32` for all n. **Forward expansivity:** if `d(16^n u,16^n v)<1/32` for all n≥0, choose the representative difference d0 with |d0|<1/32. Then |16d0|<1/2; no integer wrap can occur while the next difference stays below 1/32. Inductively |16^n d0|<1/32 for every n, forcing d0=0. Thus f(x)=f(y) for nearby x,y; continuity and connectedness make f globally constant. The constant must solve `16c=c mod1`, so c∈(1/15)Z/Z.

This exact **no-go** rules out silently identifying the golden rotation and ×16 circle carriers through a continuous factor that commutes with unit time. A source/history-augmented observer can carry both dynamics in a product, but source-sensitive signed mixing remains an independent theorem debt. An arbitrary set-theoretic correspondence is not a substitute for this transport check.

## FCT-07 — verdict, controls and next discriminating theorem

- **Classical/proved:** exact golden gaps and nested inscribed triangles; curvature-sensitive area constants; source-independent barycentric and signed lag transfers; finite Pascal complex Vandermonde reconstruction; exact passive native Pascal anti-Haar limit; no continuous direct golden→×16 factor.
- **New to this repo connection:** geometric polygon area error `Theta(F_k^-2)` and original source Green-tail `Theta(F_k^-2)` have a fully explicit ratio; time-labeled triangle interpolants preserve authentic signed lag energy at `O_h(A^-2)` sensor cost, with no changed pole or seed.
- **Source-specific phase bound not proved:** no new inequality shows `P_(A,k(A))(h)→0`, `E_H(v)→0`, or #544 `R_(A,h)(H_A)≤o(1)` for literal U0=0. These remain equivalent or sufficient open normality obligations.
- **Hostile witnesses:** coherent same-forcing seed `s*=-pi/16`, native Pascal negative-binomial circular mode (nonzero ≥1/9), seed-independent golden geometry, low-rank source mutants matching Γ(2), and sequences with identical circle point-multisets but different lag energy. The constant `lambda-gamma` comes from the *declared* rank-two log/Laplace contrast in `docs/OPERATIONAL_TRIANGLE.md`; it is not a curvature invariant of the naked circle or a selected signed arithmetic estimate.
- **Next verdict-changing probe:** couple `I_(k,h)(x_n)` and its time-labelled barycentric products to original zero-seed **odd-prime denominator births, literal carries and #544 exact forcing F_ell(n)**. Seek an all-epoch signed bound that beats the coherent wrong-seed and terminal-support shadows. Do not substitute positivity of the triangle areas or circular mesh completeness for that bound.

## Reproducibility

`observational_succ/golden_circle_triangle.py` uses exact integer arithmetic for `Z[alpha]` ordering, Fibonacci parent/child gaps and exact Fraction four-pole/grade values. Geometric sine values and complex Weyl tests are conventional floating diagnostics (NOT certified intervals); symbolic proofs above supply universal scope. `tests/test_golden_circle_triangle.py` includes exact gap/parent checks, the native source transform, original U0=0 finite epochs, coherent nonnormal controls, and history-permutation tests. Focused tests on Python 3.13.5: 21/21 PASS. Full native repository 12k+ tests, provenance, GitHub CI, external refereeing and Lean formalization of these new results are **NOT RUN** at this stage.

Prior-source bibliography for golden rotations/three-gap behavior: van Ravenstein, *Optimal Spacing of Points on a Circle*, Fibonacci Quarterly 27(1) (1989), available at https://www.fq.math.ca/Scanned/27-1/vanravenstein.pdf. Its spacing result is classical; this dossier supplies a self-contained inductive proof for the exact counts needed. Source-specific links are the SUCC paths in the opening passport.
