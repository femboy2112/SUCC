# Operation Echo–SUCC: causal delay, two boundary Green functions and a uniform Fourier transport theorem

**Date:** 2026-10-27. **Research draft, not main.** Parent: [first-prime / CRT draft PR #322](https://github.com/femboy2112/SUCC/pull/322), head `73a124637444c0e51cae1ace1e70d8c65dd28eb9`. Source: unchanged four signed BBP poles and zero initial state. **Status:** the elementary Green/filter/transport theorems below are PAPER-PROVED (with exact finite independent algebra checks); any novelty/academic priority is UNVERIFIED. The inherited 2-adic infinite-past zero is a claim of [PR #321](https://github.com/femboy2112/SUCC/pull/321), **not** re-proved here. **Base-16 normality of pi and RH remain OPEN.**

## 0. Steelman the hammer-echo proposal

An acoustic linear environment maps an impulse to a sum of delayed and filtered copies. The user proposed substituting `t-tau -> n-s`. With ordinary index n and lag s, the real zero-seed BBP recurrence **literally** has a causal Green convolution:

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
U_n=\sum_{s=0}^{n-1}16^s r(n-s).
$$

The source index `a=n-s` obeys `a+s=n`, precisely the Goldbach–Seinfeld bin-window reindexing of PR #321. The common mathematics is a delay operator, not a physical prediction of frequency-dependent sound velocity, independent stochastic paths, or a quantum collapse. Real acoustic energy decays along lossy paths, whereas `16^s` **grows** in the ordinary absolute value and **decays** in the 2-adic absolute value. Equal formulas do not identify the metrics or observer characters.

Use `E f(n)=f(n+1)`. The state equation is `(E-16)U_n=r(n+1)`, for n>=0.

## 1. Source-specific summability (PROVED)

The original signed poles combine **exactly** to

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.
$$

For n>=1, all denominator factors and the numerator are positive (`120n^2-89n+16 >=31n^2+16`). For n>=2, each denominator factor is respectively at least `3n/2, 7n/2, 9n/2, 13n/2`, so

$$
0<r(n)\le\frac{1920}{2457n^2}<\frac1{n^2},\qquad n\ge2,
\qquad r(1)=\frac{47}{15}.
$$

In particular `r` is in ordinary `ell^1`, and asymptotic rational expansion gives

$$r(n)=\frac{15}{64n^2}+O(n^{-3}).$$

**Important:** the four separate first-order poles each decay like `1/n`, but their signed leading coefficient vanishes. Replacing them with a generic positive `1/n` source destroys the strength of the following uniform bounds.

### Exact unweighted source sum, and what gamma does NOT establish

Let `R=sum_(n>=1) r(n)`. Absolute convergence and `sum_(k>=0)(1/(k+a)-1/(k+b))=psi(b)-psi(a)` give

$$
R=\frac{-4\psi(1/8)+2\psi(1/2)+\psi(5/8)+\psi(3/4)}8
=\frac\pi4+\frac{5\sqrt2\,\pi}{16}+\frac58\log2
+\frac{5\sqrt2}{8}\log(1+\sqrt2).
$$

Here `psi=Gamma'/Gamma` and the last step follows from Gauss's rational digamma formula, [NIST DLMF 5.4.19](https://dlmf.nist.gov/5.4#E19). Numerically `R=3.38604761959719...`. The `-gamma` term in each `psi` cancels, since `-4+2+1+1=0`. Thus Euler–Mascheroni enters intermediate harmonic regularizations but does **not** survive in `R`. This is an exact source coefficient cancellation, not a normality mechanism or a universal `gamma=0` renormalization.

## 2. Real future Green solution versus 2-adic past (PROVED algebra; imported 2-adic boundary)

Define the convergent *real* anticipatory tail

$$
T_n=\sum_{j=1}^{\infty}16^{-j}r(n+j),\qquad n\ge0.
$$

The bound from section 1 gives, for n>=1,

$$0<T_n<\frac{1}{15(n+1)^2},\qquad
\sum_{n=1}^{\infty}T_n=\frac{R-\pi}{15}=:B<\frac1{15}.$$

The **exact** value is `B=0.01629699773382656556...`. The equality uses absolute-convergence/Fubini and the original BBP identity `pi=sum_(m>=1)16^(1-m)r(m)`:

$$
\sum_{n\ge1}T_n
=\sum_{m\ge2}r(m)\sum_{j=1}^{m-1}16^{-j}
=\frac1{15}\sum_{m\ge2}r(m)(1-16^{-(m-1)})=\frac{R-\pi}{15}.
$$

Both the zero-initial causal state `U_n` and the real **future-selected** state `V_n=-T_n` solve `X_n=16X_(n-1)+r(n)` for n>=1. They select different boundary conditions: `U_0=0`; `V_n -> 0` as n -> infinity. Their difference satisfies the homogeneous equation; moreover `T_0=pi/16`, hence

$$\boxed{U_n-V_n=U_n+T_n=16^{n-1}\pi,\quad n\ge0.}$$

This is the exact *real* two-boundary Green/gluing identity; `pi` is its homogeneous matching amplitude, not a probability amplitude.

Meanwhile PR #321 claims and proves on paper that `Phi_2(x)=sum_(s>=0)16^s r(x-s)` converges in `Z_2`, has `Phi_2(0)=0` and restricts to `U_n` for ordinary n>=0. The real forward tail and the 2-adic backward infinite window live in **different completions**. We may compare their common rational finite state `U_n`, but **must not** subtract general real and 2-adic numbers as though they inhabited one normed field.

## 3. The delay-filter factorization (PROVED)

For any finite integer-coefficient delay polynomial

$$P(X)=\sum_{j=0}^d c_j X^j,\qquad K=P(16),$$

Euclidean division supplies an integer polynomial `Q` such that `P(X)=K+(X-16)Q(X)`. Because `(E-16)U_n=r(n+1)`, it follows **without limits** that

$$\boxed{P(E)U_n=K U_n+Q(E)r(n+1).}$$

Thus `K=0` is the exact *characteristic annihilator* of the homogeneous carrier. In this case `P(E)U` is a finite linear combination of shifts of an `ell^1` source, hence itself in `ell^1`. In particular

$$P(E)=E-16:\quad P(E)U_n=r(n+1)\to0,
\qquad
\frac1N\sum_{n=1}^N e^{2\pi i h P(E)U_n}\to1
$$

for every fixed integer h. **Demanding that these phases decorrelate to zero would be a false positive proof strategy**. Changing the filter to `E-15` gives `P(16)=1`; the cancellation disappears.

## 4. Stronger theorem: complete orbit transport with lag-independent O(1) error (PROVED)

Let a finite list of arbitrary nonnegative lags `l_j` and integer coefficients `c_j` be given, allowing both to depend on N. Put

$$F_n=\sum_j c_j U_{n+l_j},\quad K=\sum_jc_j16^{l_j},\quad V=\sum_j|c_j|.$$

The real Green identity implies **term by term**

$$\boxed{F_n=K16^{n-1}\pi-\sum_j c_jT_{n+l_j}.}$$

With `e(x)=exp(2 pi i x)`, any integer h!=0, any N>=1 and **any complex weights** `|w_n|<=1`,

$$
\boxed{
\left|\sum_{n=1}^N w_n e(hF_n)
-\sum_{n=1}^N w_n e(hK16^{n-1}\pi)\right|
\le2\pi|h|BV
<\frac{2\pi|h|}{15}V.}
$$

Proof: `|e(x)-e(y)|<=2 pi |x-y|`; then sum the tails absolutely:
`sum_(n=1)^N T_(n+l_j)<=B` for *every* lag `l_j>=0`. The universal constant `B=(R-pi)/15` uses the complete **authentic** four-pole source. No probabilistic independence, cancellation, spectral equidistribution, or finite-lag cutoff is required.

The estimate remains valid, with the **same** budget, after summing absolute discrepancies over any partition of the observation indices (including all residue classes mod an arbitrary p). It also works for sparse high lags or varying p, provided `V` is tracked.

**Concrete corollaries and quantifiers:**

- For `P(E)=sum c_j E^j` fixed, the Fourier sums of `P(E)U` and the single ordinary radix orbit at integer frequency `hP(16)` differ by a **uniform O_(h,P)(1)**, so their normalized limits coincide.
- When `K=0` and `V=o(N)`, even for moving filters, the unweighted phase average tends to **1**, not 0.
- For the van der Corput lag filter `E^l-1`, `K=16^l-1`, `V=2`: **every lag l>=1**, even growing with N, has a total comparison error at most `4 pi |h| B`; the lag itself does not appear.
- For `P(E)=product_i(E^(l_i)-1)`, `K=product_i(16^(l_i)-1)`. The coefficient norm is **at most** `2^m` for m factors (potential coefficient collisions). If m grows, the total error may grow; it is not always O(1).
- If the composite frequency `hK` varies with N, ordinary fixed-frequency Weyl equidistribution does **not** supply a uniform estimate. This is a major caveat for the moving-lag results of PR #319.

## 5. Crucible / hostile countermodel (REFUTED generic echo-normality implication)

Take `alpha=15/64` and define the explicitly **different** source

$$
r^*(n)=\alpha\left(\frac1{n^2}-\frac1{16(n+1)^2}\right)>0,
\quad T_n^*=\frac{\alpha}{16(n+1)^2},\quad
U_n^*=16^{n-1}\alpha-T_n^*,\quad n\ge0.
$$

Here `U_0^*=0` exactly, `U_n^*=16U_(n-1)^*+r^*(n)`, and `r^*(n)~15/(64n^2)`: **the positive summable source, zero seed, exact Green identity, characteristic factorization and sharp moving-lag transport all hold**. But `alpha` is rational: `16^(n-1)alpha` is an integer for n>=3, while `T_n^*->0`, so for all nonzero integers h,

$$\frac1N\sum_{n=1}^N e(hU_n^*)\longrightarrow1.$$

This kills the inference **echo decomposition + source positivity + exact quadratic leading coefficient => normality**. PR #320 contains a stronger *different* fake matching 2-adic isometry and full finite clock; retain it too. Only information distinguishing the *entire authentic source* can overcome these controls.

## 6. Relevant prior mathematics; what is and isn't new

- [Bailey–Crandall (2001), *On the Random Character of Fundamental Constant Expansions*](https://doi.org/10.1080/10586458.2001.10504441): BBP dynamics and conditional normality framework.
- [Lagarias (2001), *On the Normality of Arithmetical Constants*](https://doi.org/10.1080/10586458.2001.10504456): perturbed radix orbits are far more general than examples where normality follows. The carrier/tail decomposition belongs in this established landscape.
- [Anashin (2006), *Ergodic Transformations of the Space of p-adic Integers*](https://arxiv.org/abs/math/0602083): single-cycle criteria for compatible p-adic maps; does not equate 2-adic Haar and real-circle Haar.
- [NIST DLMF, rational digamma identity](https://dlmf.nist.gov/5.4#E19) and [reflection/multiplication](https://dlmf.nist.gov/5.5): supports the exact source sum.
- [Bailey–Rudolph (2002), *An Ergodic Proof that Rational Times Normal is Normal*](https://www.davidhbailey.com/dhbpapers/): transformations of *known* normal numbers; not a proof that pi is normal.
- Standard tools still available: Weyl's criterion, van der Corput differencing, finite Fourier characters. Here the exact source-specific value of B, uniform transport across *arbitrary lags*, and character-root no-go are assembled explicitly for this repo; independent novelty is not asserted.

## 7. Verdict and next falsification probe

**PAPER-PROVED within stated hypotheses:** sections 1–5 (ordinary rational/real arithmetic), all finite filters and all nonnegative lags. **Inherited from PR #321, not re-audited here:** 2-adic infinite-past zero. **EXACT LOCAL TESTED:** eight independent-focused unit tests, source adapter replaced *only locally* by the identical four-pole rational formula to permit execution outside the full native tree; native and hosted CI not asserted. **REFUTED:** generic delay structure forces real signed cancellation. **OPEN:** the selected condition `sum_(n<=N)e(hU_n)=o(N)` for every fixed h!=0.

The no-go has a practical research consequence: linear time-invariant, fixed-integer-coefficient delay combinations **cannot create an independent real-circle normality discriminator**; they reduce to ordinary radix frequencies, up to a summable error. Next seek **source-specific nonlinear/conditional coupling**, e.g. a carry-branch/real-phase conditional signed test, on the authentic four-pole source versus PR #320's strong 2-adic mutant. Specify the Haar conditional baseline (not automatically zero for every observable) before running. Calibrate against `P=E-16`, the `E-15` mutation, a rational-nonnormal tail control, and held-out carry windows. A successful new bound must beat PR #319's logarithmic absolute-loss order and force normalized signed cancellation. This paper alone does not do that.

Reproducibility: `observational_succ/bbp_echo_delay_transport.py` and `tests/test_bbp_echo_delay_transport.py`; build exact rational prefixes and never calculate phases by converting huge unwrapped states directly to float. No original code, frozen archives, historical claims, Lean declarations, or default branch changed.
