# Operation FEJER–GAMMA: coherent infinite-series splitting of the selected BBP return energy

**Date 2026-11-06. Status: research-only; all new statements are locally derived, not Lean-certified or academically refereed.** This work starts at PR #534's exact head `ff99fa2861b370d1aac0a76f01e2d8505c5a8740` and retains the original four signed poles and literal `U_0=0`. In every displayed formula a complex conjugate is retained; no independence of source places, observer actions, or time fibers is assumed. **Base-16 normality of π, a new original-source signed Weyl estimate, and RH are OPEN.**

## 0. The exact target and the correct object to split

Let `Q=2^k`, `k>=0`, `M>=1`, `N=QM`, and `h` be a fixed nonzero integer. The authentic source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\ U_n=16U_{n-1}+r(n).
\]

Put `z_n=e(hU_n)` with `e(x)=exp(2πix)` and `|z_n|=1`. The return-fiber amplitude and positive energy from PR #528 are

\[
A_a=\frac1M\sum_{t=0}^{M-1}z_{a+tQ},\qquad
R_{Q,M}(h)=\frac1Q\sum_{a=0}^{Q-1}|A_a|^2,\qquad
W_N(h)=\frac1N\sum_{n=0}^{N-1}z_n.
\tag{FG0}
\]

**We split the scalar `1/Q` in this expression, rather than replacing Q by a formal infinity.** The distinction is essential to maintain the correct normalization and positivity.

## FG-01: the proposed two Gamma-half-density series and two harmonic time series — PROVED LOCAL

For integers `Q,M>=1`, let

\[
\alpha_j(Q)=(Q+j)^{-1/2}-(Q+j+1)^{-1/2}>0,\quad
\beta_r(M)=(M+r)^{-1}-(M+r+1)^{-1}>0.
\tag{FG1}
\]

Both series are absolutely convergent, with finite telescope and full values

\[
\sum_{j=0}^{J-1}\alpha_j(Q)=Q^{-1/2}-(Q+J)^{-1/2},\quad
\sum_{r=0}^{L-1}\beta_r(M)=M^{-1}-(M+L)^{-1},
\]

\[
\boxed{\frac1Q=\left(\sum_{j=0}^\infty\alpha_j(Q)\right)
\left(\sum_{\ell=0}^\infty\alpha_\ell(Q)\right),\qquad
\frac1M=\sum_{r=0}^\infty\beta_r(M).}\tag{FG2}
\]

The Gamma name is operational, not an assertion that Γ causes normality: the Laplace–Gamma formula gives

\[
\alpha_j(Q)=\frac1{\sqrt\pi}\int_0^\infty
s^{-1/2}e^{-(Q+j)s}(1-e^{-s})\,ds,
\qquad
\beta_r(M)=\int_0^1 u^{M+r-1}(1-u)\,du.
\tag{FG3}
\]

Move **one** `alpha` series and **one** `beta` series into each of the two conjugate M-sums, without changing the same residue label a:

\[
\Phi_a=\sum_{j,r\ge0}\sum_{t=0}^{M-1}
\alpha_j(Q)\beta_r(M)z_{a+tQ}.
\]

Since `sum alpha=1/sqrt(Q)` and `sum beta=1/M`, all interchanges are absolutely valid, `Phi_a=A_a/sqrt(Q)`, and

\[
\boxed{R_{Q,M}(h)=\sum_{a=0}^{Q-1}\Phi_a\overline{\Phi_a}.}\tag{FG4}
\]

Equivalently, fully expanding produces *two independent Gamma indices j,l, two harmonic indices r,s, and two time indices t,u*, but **the common residue label a remains shared**. This is exactly the requested coherent square. A constant-phase sequence has `Phi_a=1/sqrt(Q)` and R=1: the series alone add no signed saving.

## FG-02: exact nonuniform-truncation trap — PROVED LOCAL, HOSTILE NO-GO

Truncate each `alpha` series to J terms and each `beta` series to L terms (same J,L in the two conjugate amplitudes) and call the resulting energy `R^{(J,L)}`. Direct telescoping yields, for *every* unit-phase array,

\[
\boxed{R^{(J,L)}_{Q,M}(h)=R_{Q,M}(h)\,
\left(1-\sqrt{\frac Q{Q+J}}\right)^2
\left(\frac{L}{M+L}\right)^2.}\tag{FG5}
\]

At fixed J,L and Q,M→∞, the multiplier tends to ZERO even when `z_n=1` identically and the true R is exactly ONE. This is **spurious contraction from exchanging the arithmetic-scale limit with the infinite-series limit**. To recover R uniformly in growing Q,M, one must pay the respective tail budgets J/Q→∞ and L/M→∞, or choose an alternative uniform geometric representation. The fake saving is source-blind and cannot imply normality.

The exploratory test initially chose `J=L=10^10` and incorrectly asserted 4-place proximity to 1. The exact bound gives 0.9999434304576296, just outside the tolerance. The correction `10^12` passes; the original failed log is preserved. This is a test precision/series convergence error, not a refutation of FG5.

## FG-03: genuine coherent gluing and exact finite Fourier spectrum — PROVED LOCAL

One cannot replace the shared fiber label a by independently chosen labels without inserting the diagonal gluing kernel. Let

\[
K_Q(a,b)=\sum_{r=0}^{Q-1}e\!\left(\frac{r(a-b)}Q\right)=Q\,\mathbf 1_{a=b}.
\tag{FG6}
\]

Then

\[
R=\frac1{Q^2}\sum_{a,b=0}^{Q-1}A_a\overline{A_b}\,K_Q(a,b)
=\sum_{r=0}^{Q-1}\left|\frac1N\sum_{n=0}^{N-1}
 z_n e\!\left(-\frac{rn}{Q}\right)\right|^2.
\tag{FG7}
\]

The r=0 term is EXACTLY `|W_N(h)|²`. Therefore

\[
\boxed{R_{Q,M}(h)-|W_N(h)|^2
=\sum_{r=1}^{Q-1}\left|\frac1N\sum_{n<N}z_n e(-rn/Q)\right|^2\ge0.}\tag{FG8}
\]

Independent residue labels, with `K_Q` omitted, yield `|W_N|²` instead of R. A calibrated alternating ghost `z_n=(-1)^n` at even Q has `W_N=0` and R=1: **every bit of coherence is in the missing nonzero Fourier channel**. This kills any split that silently treats the conjugate fiber labels as independent.

## FG-04: exact dyadic martingale / holographic energy triangle — PROVED LOCAL

Fix **one** sample size `N=2^K M_0` and consider levels `0≤j≤K` with `q_j=2^j`. Define

\[
F_j(a)=\frac{q_j}{N}\sum_{\substack{0\le n<N\\n\equiv a\pmod{q_j}}}z_n,
\quad E_j=\frac1{q_j}\sum_{a<q_j}|F_j(a)|^2,
\quad F_0(0)=W_N.
\]

The fibers at each level split into two children whose means average to the parent. By the elementary parallelogram identity,

\[
\boxed{E_{j+1}-E_j=\frac1{2^{j+2}}
\sum_{a=0}^{2^j-1}|F_{j+1}(a)-F_{j+1}(a+2^j)|^2\ge0.}\tag{FG9}
\]

In particular,

\[
\boxed{R_{2^k,N/2^k}(h)=|W_N(h)|^2+\sum_{j=0}^{k-1}(E_{j+1}-E_j).}\tag{FG10}
\]

**This is a strong limit-order warning:** for fixed N, refining Q from 1 to N makes R MONOTONE NONDECREASING, from `|W_N|²` to `1`. A purported universal *contraction* under refinement is refuted. The dropped distinguishing information has been reallocated to nonnegative dyadic channels; it has not disappeared from the joint object.

For arbitrary unit phases let `A_a` be the original Q-fiber means. A second exact three-part balance is

\[
\boxed{1=\underbrace{|W_N|^2}_{\text{global coherent mode}}
+\underbrace{\frac1{2Q^2}\sum_{a,b}|A_a-A_b|^2}_{\text{between-fiber distinction}}
+\underbrace{\frac1{2QM^2}\sum_{a=0}^{Q-1}\sum_{t,s=0}^{M-1}
|z_{a+tQ}-z_{a+sQ}|^2}_{\text{within-fiber dephasing}}.}\tag{FG11}
\]

The last term equals `1-R`; the middle term equals `R-|W_N|²`. This is an **operational coherence triangle**. It does not identify the golden/harmonic/Euler–Mascheroni physical/categorical triangle with the three terms; such a source-specific natural transformation is UNVERIFIED.

## FG-05: the full time-square collapses into the triangular Fejér lag series — PROVED LOCAL

For `1≤d<M`, define the genuine source-selected lag character

\[
C_{Q,d,M}(h)=\frac1{Q(M-d)}\sum_{n=0}^{Q(M-d)-1}
 e\bigl(h(U_{n+dQ}-U_n)\bigr).
\]

Every ordered pair of time indices has separation d and multiplicity M−|d|. The diagonal has magnitude `|z_n|²=1`. Thus

\[
\boxed{R_{Q,M}(h)=\frac1M+
\frac{2}{M^2}\sum_{d=1}^{M-1}(M-d)\operatorname{Re}C_{Q,d,M}(h).}\tag{FG12}
\]

This is the exact Fejér triangle, and can also be viewed as the finite convolution of the two independent uniform M-windows. The diagonal `1/M` is **not** a lower bound for R: signed off-diagonal correlations can be negative.

For the ORIGINAL source the return displacement has the exact forced formula

\[
U_{n+dQ}-U_n=(16^{dQ}-1)U_n+S_{dQ}(n),
\qquad S_L(n)=\sum_{j=1}^L16^{L-j}r(n+j).
\tag{FG13}
\]

For the real source completion `Z_n={U_n+T_n}={16^nπ/16}`, define `C^Z` using Z rather than U. Then the full sum over `a` and time t **collapses to a single contiguous Weyl mean** at a high selected frequency:

\[
\boxed{C^Z_{Q,d,M}(h)=
\frac{1}{Q(M-d)}\sum_{n=0}^{Q(M-d)-1}
 e\!\left(h(16^{dQ}-1)16^n\frac\pi{16}\right).}\tag{FG14}
\]

The inherited tail bound implies `|R^U-R^Z|=O_h(1/N)` (see parent #528 RS11a). Thus the Fejér-lag representation is a valid, source-faithful reorganization, but **it regenerates very high-frequency original selected Weyl sums; it does not bound them**. A genuine improvement requires a new signed estimate on the weighted lag correlations that survives the hostile controls.

## FG-06: a source-specific prime-local resonant return is not a real return — PROVED LOCAL instance

The authentic original pole `8·33−7=257` first introduces `p=257` at time 33. One has `ord_257(16)=4`, as `16²≡−1 (mod257)` and `16^4≡1`. No original source denominator in times 34,35,36,37 is divisible by257. By the exact recurrence,

\[
U_{37}-U_{33}=(16^4-1)U_{33}+S_4(33)\in\mathbb Z_{257}.
\tag{FG15}
\]

Thus **the p-local additive character of the lag difference equals 1 exactly**; the newly born p-local character has returned to its previous value. But separate exact Fraction arithmetic yields

\[
\boxed{\frac{42}{100}<\|U_{37}-U_{33}\|_{\mathbb T}<\frac{43}{100}.}\tag{FG16}
\]

The real phases are nearly opposite despite the p-local perfect return. The same phenomenon occurs at p=149, birth time19, local order37, with real distance strictly between 45/100 and46/100. These are **finite exact original-source calibrations**, not newly preregistered holdouts (the p-specific witnesses were found after the preregistration). The remaining odd-prime complement carries the real separation. A local Gauss sum cannot be promoted to a global Fejér-lag cancellation without that coupling.

## FG-07: honest infinite realization of the M time stream — PROVED LOCAL

For each fixed a, the bounded sequence `z_(a+tQ)` defines an analytic generating series

\[
F_a(s)=\sum_{t=0}^\infty z_{a+tQ}s^t\qquad(|s|<1).
\]

Then an EXACT finite coefficient identity holds:

\[
\boxed{A_a=\frac1M[s^{M-1}]\frac{F_a(s)}{1-s}.}\tag{FG17}
\]

The extraction depends only on the first M terms, so it is not secretly using infinite-time distribution. An Abel mean `(1-ρ)F_a(ρ)` is a **different observable**; any asymptotic transfer back to finite Cesàro means needs a separately valid limit argument. Neither formal sums nor guessed regularization are source-selected Weyl estimates.

## Frontier and precise verdict

- **Disclosed locally:** the two absolutely convergent Γ-half-density factors, harmonic M-expansions, truncation bias, coherent Fourier gluing, dyadic martingale and variance triangle, Fejér lag identity, exact original-source p257 rephase/real-separation witness, and exact generating-function coefficient extraction.
- **REFUTED:** 'infinite normalization automatically creates cancellation'; 'independent residue labels preserve original R'; 'deeper dyadic conditioning contracts R at fixed N'; 'p-local rephase implies real rephase'. Each has an explicit witness above.
- **OPEN:** prove an unconditional nontrivial bound for the authenticated original source's weighted real lag sum in FG12, or the real return-fiber energy R, for every fixed nonzero h at a dense sequence of horizons, without assuming π normality. The reciprocal-series split itself pays none of this signed truth debt.

**Provenance:** source, selected zero boundary, exact Z₂ 2-adic returns and original R are inherited read-only from SUCC PRs #521, #527, #528, #529 and #534; all new work is in one additive research directory. Γ/Laplace, Parseval, finite Haar characters, martingale identity and Fejér kernels are classical math, locally rederived rather than claimed as worldwide novelties. No physical quantum interpretation follows from the series factorization.
