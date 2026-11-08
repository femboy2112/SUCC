# Operation LAPLACE CRITICAL — authentic BBP source, finite-place phase overlap, and boundary resistance

2026-11-08. Additive research child of SUCC #558 (`46b96e61ea8a309546b399da328c9bfcc077ada2`), with #496 and #555 explicitly prior art. Original four signed poles and literal `U0=0` remain frozen. **Base-16 normality of π, fixed-h Weyl decay, and RH remain OPEN.** `PROVED PAPER` means a complete scoped argument, not Lean checking, external scholarly priority or a full repository test run.

## A. The object and the selected operator

Let `e(x)=exp(2πix)`, `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)` and `U0=0`, `U_(n+1)=16 U_n+r(n+1)` with **unwrapped** rational state retained. Its real phase is exactly the full finite-prime additive-character product from #558: `f_n(h)=e(hU_n)=prod_p e(h[U_n]_p)` (no prime-independence assumption). For `|z|<1`, set `G_h(z)=sum_(n>=0) f_n(h) z^n`. Earlier PR #496 already proved that for all fixed nonzero integer h the Abel boundary `(1−z)G_h(z)->0` as z increases to 1 is equivalent (with bounded-sequence Tauberian and source Green transport) to base-16 π normality. **We do not claim this equivalence as a new theorem.**

## LCS-01. Exact positive source Laplace/Stieltjes density (PROVED PAPER)

For `n>=1`, with `Q(u)=4−2u^3−u^4−u^5=2(1−u^3)+(1−u^4)+(1−u^5)>=0` on `[0,1]`,

`r(n)=integral_(0)^1 u^(8n−8) Q(u)du`

`=integral_(0)^infinity exp(-(8n−7)t)[4−2exp(-3t)−exp(-4t)−exp(-5t)]dt`.

Thus for `0<=z<1`, the exact source generating function is

`R(z)=sum_(n>=1) r(n)z^n = z integral_0^1 Q(u)/(1−z u^8) du`.

All interchanges are justified by nonnegative summands; for complex |z|<1, absolute convergence supplies the continuation. The nonvanishing linear zero `Q(e^-t)=15t+O(t²)` at t=0 gives the genuine source jet `a=15/64`: `r(n)=a/n²+(151/512)/n³+O(n^-4)` (as already established in #556).

Writing `Li_2(z)=sum z^n/n²`, the remainder `r(n)-a/n²=O(n^-3)` implies `sum_n n|r(n)-a/n²|<infinity`. Hence, as real `z↑1`, using the classical dilogarithm integral,

`R(1)-R(z)=a*(1−z)*log(1/(1−z)) + O(1−z)`.

This is a **source-side logarithmic branch**, not a pole of the selected real phase series `G_h` and not a normality estimate. Classical dilogarithm source: NIST DLMF §25.12.

## LCS-02. Exact Euler–Mascheroni normalization seam (PROVED PAPER)

Define `d_n=n r(n)−a/n` and `D=sum_(n>=1)d_n`. The #556 original second jet yields `d_n=(151/512)n^-2+O(n^-3)`, so D converges absolutely. In fact, from `r(n)=a/n²+(151/512)/n³+E(n)`, `|E(n)|<=n^-4` for n>=2 (the original four-pole bound), for N>=2:

`|D−sum_(n<=N)d_n| <= 151/(512N)+1/(2N²)`.

The two source-normalization procedures have different finite parts:

`lim_(N->infinity) [sum_(n<=N)n r(n)−a log N] = D+a gamma`,

`lim_(z↑1) [R'(z)+a log(1−z)] = D`,

where `gamma` is Euler–Mascheroni. Proof: split `n r(n)=a/n+d_n`, use `H_N−logN->gamma`, the absolutely convergent remainder, and `R'(z)=-(a/z) log(1−z)+sum_(n>=1)d_n z^(n−1)`. These give an exact, source-authentic continuous/discrete harmonic seam with coefficient 15/64. They **do not** impose selected Fourier cancellation.

## LCS-03. Original-source Fourier Ward identity and uniform critical-frequency obstruction (PROVED PAPER)

For every integer h, every seed s, and |z|<1, define

`E_(h,s)(z)=sum_(n>=0) z^n e(16h U_n(s)) [e(h r(n+1))−1]`.

The exact state recurrence implies

`G_(h,s)(z)=e(hs)+ z G_(16h,s)(z)+z E_(h,s)(z)`.

For n>=1, original positivity and the density bound `Q(e^-t)<15t` give

`0<r(n+1)<15/(64n²)`.

Using `|e(x)-1|<=min(2,2π|x|)`, set `K=15π|h|/32`. Separating the n=0 term and summing `min(2,K/n²)` after `M=ceil sqrt(K)` (for integer nonzero |h|, K>=1), gives for all t>0:

`|(1−e^-t)E_(h,s)(e^-t)| <= min(2,(1−e^-t)(4+3 sqrt(15π|h|/32)))`.

In particular, if t↓0 and integer h=h(t) satisfies `|h(t)| t²->0`, the source correction vanishes **uniformly over arbitrary seeds**. This uniform subcritical estimate does not bound the `G_(16h,s)` ladder. At the **critical** scaling `h t²->lambda !=0` this bound stops vanishing; the next theorem proves that the obstruction is real and not a loose estimate.

## LCS-04. Nontrivial critical Laplace source scattering, with a Gamma square-root cusp (PROVED PAPER)

Let `h(t)` be integers with `h(t)*t²->lambda` as `t↓0`, and define the **source-only** normalized phase driver

`D_(h,t)=t sum_(n>=0) exp(-tn)[e(h r(n+1))−1]`.

Then the authentic four-pole source satisfies

`lim_(t↓0) D_(h(t),t) = I(lambda)`, where

`I(lambda)=integral_0^infinity exp(-x)[exp(2πi*(15/64)*lambda/x²)−1] dx`.

Proof: the exact `r(n+1)=(15/64)n^-2+O(n^-3)` on each compact rescaled interval n*t in [delta,L] gives a Riemann sum. The summands have modulus ≤2, so [0,delta] and [L,infinity) tails are bounded uniformly by 2delta and O(e^-L), respectively. Then delta↓0 and L↑infinity. For lambda !=0, `Re I(lambda)<0`, because `cos(2π*(15/64)*lambda/x²)-1<0` on a positive-measure set. Thus the critical driver is genuinely nonzero.

More sharply, as real `lambda->0`, lambda!=0,

`I(lambda)= -(π sqrt(30)/8) exp[-i sgn(lambda)π/4] sqrt(|lambda|) + o(sqrt(|lambda|))`.

Proof: x=sqrt(|lambda|)y; dominated convergence against `min(2,C/y²)` reduces the coefficient to `int_0^infinity (exp(i c/y²)-1)dy` with c=2π*(15/64)*sgn(lambda). Set v=y^-2 and integrate by parts (Abel damping for the oscillatory gamma integral): the coefficient is `−sqrt(pi)*(-i c)^(1/2)`, giving the displayed constant. This is the standard Gamma(1/2) integral, not a quantum effect or an Euler–Mascheroni normality proof.

**Matched-leading hostile control:** any positive source `r'(n)=a/n²+O(n^-3)` has exactly the SAME critical limit I(lambda), even if its pole structure and 1/n³ coefficient are different. A specific four-pole mutation is `r'(n)=r(n)+(1/10)[1/(8n−7)−2/(8n−4)−1/(8n−3)+2/(8n−2)]`: its first coefficient 15/64 is unchanged but its third-order coefficient shifts by 1/320. This refutes using I(lambda) alone as a complete original-source fingerprint.

## LCS-05. Coherent wrong-seed critical scaling and no-free-dissipation (PROVED PAPER)

For `s*=-pi/16`, the original recurrence has `U_n(s*)=-T_n`, where the canonical future Green correction satisfies `T_n=(64 n²)^-1+O(n^-3)`. Thus fixed h has `lim_(z↑1)(1−z)G_(h,s*)(z)=1`, despite the same source generating function R(z), source forcing, and all-origin source cocycles as the zero seed. The irrational counterseed is **not** itself an unwrapped rational p-adic state; its source-history equality must not be mistaken for equality of all seeded finite-prime character histories.

At critical h(t)*t²->lambda, the (n>=1) coherent wrong-seed Laplace transform instead tends to

`integral_0^infinity exp(-x) exp(-2πi lambda/(64x²)) dx`.

The n=0 omitted term is bounded by t; proof again uses bounded rescaled Riemann sums and `T_n~1/(64n²)`. It need not be zero and does **not** imply any fixed-h normality. External heat smoothing or the source-only critical response therefore cannot convert a seed-blind theorem into one about π's zero-selected signed mean.

## LCS-06. Exact signed prime/complement Laplace overlap (PROVED finite algebra; conditional route OPEN)

On an authenticated actual BBP epoch [A,2A) choose any eligible p (in particular #554's balanced p_A). Define `a_j=e(h[U_(A+j)]_p)` and `b_j=prod_(q!=p)e(h[U_(A+j)]_q)` for j=0,...,A−1. The **entire real phase** is `a_j b_j` exactly by #558. For tau>=0 set `b_j^tau=exp(-tau*j/A)b_j`. Let DFT `ahat(k)=A^-1 sum_j a_j exp(-2πikj/A)`, `bhat_tau(k)=A^-1 sum_j b_j^tau exp(-2πikj/A)`. Orthogonality gives the signed identity

`L_(A,h)(tau)=A^-1 sum_j exp(-tau*j/A)e(hU_(A+j))`
`=sum_(k mod A) ahat(k)*bhat_tau(-k)`.

This is a finite contour/Hadamard-product identity in the Laplace-like domain. It does NOT factor `L` into the product of marginal Laplace transforms. If `b_j=conjugate(a_j)`, the unweighted mean is 1 even if each marginal mean vanishes.

**A source-informed but strong conditional gate:** Suppose the #554 four-stage p-local prefix estimate `max_{0<=m<=A}|sum_{j<m}a_j| <=A E_A` holds, where `E_A->0`. Summation by parts for the finite DFT gives for all representative k, `|ahat(k)|<=E_A(1+2π|k|)`. For integer `0<=K<(A-1)/2`, DFT Parseval and Cauchy–Schwarz imply

`|L_(A,h)(tau)| <= sqrt(2K+1) E_A (1+2πK) + [sum_(|k|>K)|bhat_tau(k)|²]^(1/2)`.

For fixed-h genuine zero source, if along every large A some K_A satisfies `K_A->infinity`, `E_A K_A^(3/2)->0`, and **original-zero** complementary high-frequency tail tends to zero, then `L_(A,h)(tau)->0`. For a sequence of fixed positive tau_j↓0, the generic signed-window comparison `|W_A(h)-L_(A,h)(tau)|<=tau/2` then implies W_A(h)->0. The resulting theorem would prove normality if satisfied for every fixed h!=0. The complementary high-frequency condition is **UNVERIFIED** and looks numerically implausible: at original A=192 and 320 the complementary high-mode power beyond K=8 was ~0.927 and ~0.938, respectively. These are PRESEEN exploratory float diagnostics, not a refutation of the all-A hypothesis.

The weaker and more promising target is **signed high-mode cross-overlap decay**, not high-mode energy decay. Exactly this unresolved overlap is the time-domain #544/#554 forcing-corrected real/prime covariance in a different basis; no new original-zero asymptotic saving is claimed.

## Claim and provenance firewall

LCS-01 source Stieltjes integral and LCS-02 Gamma seam: source-authentic paper derivations with original four-pole moments; no new π result. LCS-03 Ward: existing #496 identity plus newly quantified critical uniform source bound. LCS-04 critical limit and square-root cusp: new-to-SUCC paper derivation, universal matched-leading-source no-go. LCS-05 seed firewall: inherited coherent control extended to critical Laplace scaling. LCS-06 finite DFT algebra: classical; source-specific prefix inequality imported CONDITIONALLY from #554. All true derivative, analytical limit and Tauberian claims are paper-level, not Lean-certified here.

**π BASE-16 NORMALITY: OPEN. THE MISSING SOURCE-SELECTED SIGNED BOUND: OPEN.**
