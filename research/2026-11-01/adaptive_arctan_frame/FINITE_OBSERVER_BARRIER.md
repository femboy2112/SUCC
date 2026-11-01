# AAF-08: A strictly positive counterfeit defeats every finite mirror observer

This negative theorem constrains the interpretation of AAF-03–05; it does NOT refute them on the unchanged original source.

For **arbitrary finite** state horizon N and harmonic band H choose an integer

`L >= max(N, max_{1<=h<=H} k(16h), max_{1<=h<=H} k(h))`.

Define another source, with the same seed U0=0,

`r_L(n) = r(n)` for `n<=L`, and `r_L(n)=r(L)/2^(n-L)` for `n>L`.

This is **strictly positive and strictly decreasing for every n>=1**. It matches the authentic original source through L, so it has EXACTLY the same first N arithmetic states and every adaptive mirror label needed for the whole requested band. Nonetheless its completed point is

\[
\alpha_L=\sum_{j=1}^L16^{-j}r(j)+\frac{r(L)}{31\,16^L}\in\mathbb Q.
\]

The rational tail follows from the exact geometric identity `sum_{j>=1}(1/32)^j=1/31`. A rational completed point has eventually periodic base-16 expansion, hence is **not base-16 normal**. Its zero-seeded affine orbit is correspondingly not equidistributed: the positive Green-tail difference between its forced orbit and the pure `16^n α_L` orbit tends zero. Therefore:

> No predicate depending only on finitely many observed source values, arithmetic states, and mirror labels can by itself certify all-horizon normality even within strictly positive monotonically decreasing source sequences.

This fake changes the exact original *four-pole rational law after L*. It is not a counterfeit **within** the fully authenticated original four-pole source class, and it is not a refutation of the all-harmonic analytic gate using that full source. Exact tests construct these fake histories, verify positivity/decrease, equality of all finite probes and the rational completed value.

The original selected signed cancellation problem remains open. This certificate explicitly prevents finite-prefix fitted evidence from being promoted into an infinite conclusion.
