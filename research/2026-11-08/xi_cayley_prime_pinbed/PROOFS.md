# Critical circle, Euler horodisks, prime roots of unity, and the zero-detecting learning pin-bed

**Research round: 2026-11-08.** Intended SUCC base `main@43a607818907120d4cdab73d240f5b4d7700b63f` (reverify live head). The original zeta Euler factors, completed Gamma/pole factor and source normalization are **not** modified. The shifted half-density product below is an **explicit changed-source control**, not an alternate definition of Riemann's zeta. Classical material is credited; no novelty or proof of the Riemann Hypothesis is asserted.

## Steelman of the user's geometric intuition

An integer-clock observer sees local prime frequencies `log p` and wishes to transport their circular phases into the geometry of Riemann's critical line. A root-of-unity equation under a source-normalized Mellin oscillator lives on a vertical line; a Möbius transformation turns that line into a unit-circle boundary. A source-authenticated observer then tries to transport the **original prime plus Gamma completion**, including the missing analytic continuation, while retaining phase and all holonomy. The obstruction is an off-critical zero, which appears as an interior logarithmic-potential charge or nontrivial log-phase winding. This is a coherent program, but it is not automatically established by constructing circular prime-factor zeros.

## CXP-01 — precise Cayley disk and Euler horodisk (CLASSICAL; complete algebraic proof)

Take the complex projective coordinate `w=(s-1)/s=1-1/s`, with inverse `s=(1-w)^(-1)` except at `w=1` (the infinity-end of the s-plane), and `s=0` mapping to w=∞. For `s=σ+it`, direct multiplication gives

`|w|^2 = ((σ-1)^2+t^2)/(σ^2+t^2)`.

Therefore `|w|<1` iff `σ>1/2`; the critical line `σ=1/2` maps to `|w|=1`, and `s=1/2` maps to `w=-1`. Along the critical line parameter `t`,

`w=((4t²-1)+4it)/(4t²+1)`, with `|w|²=1` identically.

For any real threshold `σ_0>0` the inequality `Re(1/(1-w))>σ_0` is equivalent to

`|w-(1-1/(2σ_0))| < 1/(2σ_0)`.

Consequently the **unshifted original zeta Euler product** (`Re s>1`) is source-certified on exactly the *tangent horodisk* `D(1/2,1/2)` within the critical disk. The **half-density-shifted** product (`Re s>3/2`) converges on the smaller `D(2/3,1/3)`. The two disks are tangent to the unit circle at w=1. They are NOT the same domain. The original Euler-product nonvanishing region does not cover `|w|<1`.

## CXP-02 — complete xi-function, exact source logarithm and the missing extension (CLASSICAL / PROVED EQUIVALENCE, premise OPEN)

Define

`ξ(s)=(1/2)s(s-1)π^(-s/2)Γ(s/2)ζ(s),   F(w)=2 ξ((1-w)^(-1)).`

Because ξ is entire with `ξ(0)=ξ(1)=1/2`, `F` is holomorphic on the full open disk and `F(0)=1`. The functional equation `ξ(s)=ξ(1-s)` becomes `F(w)=F(1/w)` where both are defined; zeros off the unit circle are paired by inversion. The original Euler product gives the source-authenticated logarithm **only** on `H_1=D(1/2,1/2)`:

`L_E(w)= log[s(s-1)π^(-s/2)Γ(s/2)] + sum_p sum_(k>=1) p^(-ks)/k`,  `s=1/(1-w), Re s>1`.

The expression is interpreted with analytic logarithm branches anchored to the positive real value at the reference point `w_*=1/2`, `s=2`. Since all terms are holomorphic and the Euler double sum converges locally uniformly, `exp L_E=F` and the source log is holomorphic on H_1.

**Source-log extension theorem:** RH iff there exists a *single-valued holomorphic* `L` on the entire open unit disk, restricting to `L_E` on H_1, such that `exp L=F` (the exponential equality is in fact forced by the identity theorem). Proof: if L exists, F has no zero in the disk. Conversely, if RH holds, ξ has no zeros in `Re s>1/2`, so F is zero-free on simply connected D; its holomorphic log exists and can be phase-matched at w_* to L_E. The zero-free condition and Li criterion are RH-equivalent, not additional proved sign input. `F(w)` is not assumed to be holomorphic at the boundary w=1, where s→∞.

The connection to a *learning observer* is path-memory: `d log F=(F'/F) dw` is already source-known in H_1; continuation around a closed curve in the punctured disk has **integer winding**

`(1/(2πi))∮_Γ F'(w)/F(w) dw = number of enclosed F-zeros (multiplicity)`

for a simple positively oriented contour avoiding zeros. All such windings vanish iff RH. Transporting the prime log outside the Euler horodisk without supplying this missing property is the exact obstruction: no new Weil sign is proved by its existence inside H_1.

## CXP-03 — Jensen radial pin-bed with conditional finite zero exclusion (CLASSICAL / PROVED CONDITIONAL CERTIFICATE)

For `0<r<1` and a zero-free evaluation circle `|w|=r`, define

`J_ξ(r)=(1/(2π))∫_0^(2π) log |F(re^(iθ))| dθ`, `F(0)=1`.

Jensen's theorem gives

`J_ξ(r)=sum_(|w_ρ|<r) log(r/|w_ρ|)>=0`.

Thus **RH iff `J_ξ(r)=0` at every r∈(0,1)** (restrict to zero-free radii; continuity supplies the general statement). Positivity of J is UNCONDITIONAL; **zero**, not positivity, is the missing RH theorem.

For any `0<r_0<r<1`, the number of zeros in `|w|<=r_0` satisfies

`N_ξ(r_0) log(r/r_0) <= J_ξ(r)`.

Hence a *rigorously established* upper bound `exp(J_ξ(r))<r/r_0` certifies no zeros in `|w|<=r_0`. This is an authentic finite-radius proof instrument **only if** the log-mean upper bound is independently validated with all analytic/interval errors. Finite point sampling of phases or log moduli is not such a bound and can miss zeros. The exact Fraction code only converts a supplied certified bound into an integer zero-count cap; it cannot certify one for ξ.

## CXP-04 — finite prime roots of unity become critical-circle zeros (EXACT ALGEBRA; changed-source control)

The true zeta Euler factor is `(1-p^(-s))^(-1)`. Its local *poles*, where `1-p^(-s)=0`, lie at `s=2πik/log p`, `k∈Z` (at `k=0`, s=0 maps to w=∞); for `k≠0`, their finite Cayley points have `Re w=1` and `|w|>1`. These local poles are not the nontrivial ξ zeros.

Introduce the **deliberate half-density** oscillator `u_p(s)=p^(1/2-s)`. Then `u_p(1/2+it)=e^(-it log p)` is unit-modulus. For any integer m≥1 the polynomial `1-u_p(s)^m` vanishes exactly when `u_p(s)` is an mth root of unity, i.e.

`s=1/2+2πik/(m log p)`, `k∈Z`.

Under CXP-01, every such zero maps to the critical **unit circle**. This is a direct exact implementation of the user's root-of-unity picture in a Mellin prime clock. **It does NOT represent ξ**, and it is not a source-preserving transfer of the original Euler product: the half-density has moved the local factor from exponent `s` to exponent `s-1/2`.

## CXP-05 — decisive infinite-prime limit counterexample, with Euler–Mascheroni (CLASSICAL / PROVED)

Take the product of the half-density factors at finite prime cutoff P:

`E_P(s)=prod_(p<=P)(1-p^(1/2-s)).`

Each E_P is an entire finite exponential product, with **every zero on `Re s=1/2`**. However for `Re s>3/2` the sequence converges locally uniformly to `1/ζ(s-1/2)`. The right-hand side extends holomorphically across s=3/2, with a **simple zero** there because ζ has a simple pole at 1. In disk coordinates this new zero is

`w=(3/2-1)/(3/2)=1/3`, strictly **inside** the unit disk, on the *boundary* of the smaller convergence horodisk `D(2/3,1/3)`.

There is no contradiction with Hurwitz's theorem: zero-freeness of a locally uniformly convergent sequence is inherited only in the **open domain of convergence**, not across its boundary. At s=3/2 every finite E_P is positive and nonzero, but its limit vanishes:

`E_P(3/2)=prod_(p<=P)(1-1/p) -> 0`.

Moreover classical **Mertens' product theorem** shows exactly

`lim_(P→∞) (log P) E_P(3/2)=e^(-γ)`.

So an explicitly shifted prime-root-of-unity model has a **Gamma/Euler–Mascheroni-renormalized disappearance of mass**, and an analytic-continuation zero emerges away from every finite factor's circle-zero locus. The conclusion is a *counterexample to the naive finite-zero-geometry-to-infinite-zero-geometry argument*, not a proof or disproof of RH. It is particularly load-bearing for SUCC's prior Γ-prime/finite-to-infinite source-map research: model the topology and normalization before claiming zero confinement survives limits.

## CXP-06 — Euler-region authenticated approximation and explicit source error (PROVED bound, incomplete extension)

For `Re s=σ>1` and cutoff P≥2, let

`ζ_P(s)=prod_(p<=P)(1-p^(-s))^(-1)`.

The source difference of the analytic logs satisfies the absolute bound

`|log ζ(s)-log ζ_P(s)| <= P^(1-σ) / ((σ-1)(1-2^(-σ)))`.

Proof: the omitted prime log terms obey `sum_(p>P)sum_(k>=1)|p^(-ks)|/k <= sum_(n>P)n^(-σ)/(1-2^(-σ))`; dominate the integer tail by the integral `P^(1-σ)/(σ-1)`. Here the logs mean the consistent analytic Euler branches, not arbitrary principal values after crossing winding cuts.

Using the **unchanged** completion `ξ_P(s)=(1/2)s(s-1)π^(-s/2)Γ(s/2)ζ_P(s)`, the same bound is `|log(ξ/ξ_P)|<=B` and implies `|ξ-ξ_P|<=|ξ_P|(e^B-1)`. This is a genuine finite source-Gamma approximation **only in σ>1**. In particular it is not uniform as σ↓1 and supplies no zero-free bridge through the critical strip. The function ξ_P has an artificial zero at s=1 because a finite ζ_P does not cancel the completion's `(s-1)` factor; it must never be substituted for ξ there.

## CXP-07 — explicit fake reflection-symmetric Xi and Li/winding controls (PROVED EXACT FINITE)

For rational `0<a<1/2`, define the normalized polynomial

`Q_a(s)=1+s(s-1)/(1/4-a²)`.

It obeys `Q_a(0)=Q_a(1)=1` and `Q_a(1-s)=Q_a(s)`, is zero-free for `Re s>1`, and has **off-critical zeros** `s=1/2±a`. Its Cayley transform is

`Q_a(1/(1-w))=1+w/[(1/4-a²)(1-w)²]`.

The zeros occur at `w=-r_a,-r_a^(-1)` with `r_a=(1/2-a)/(1/2+a)∈(0,1)`. For a=1/4 these are `w=-1/3,-3`. Its log Taylor coefficients are exactly

`λ_n[Q_a]=2+(-1)^(n+1)(r_a^n+r_a^(-n))`.

In particular at a=1/4, `λ_1=16/3>0`, `λ_2=-64/9<0`. Jensen gives `exp J_Qa(r)=1` for r<r_a and `r/r_a` for r>r_a, away from the zero-radius circle. Independent Fraction formal-series, rational reflection, exact-count and numerical angular-average tests agree.

The **on-line comparator** `Q_line(s)=1+2s(s-1)` has zeros `s=1/2±i/2`, mapping to `w=±i`; its Cayley form is `(1+w²)/(1-w)²`, with no interior zeros and nonnegative coefficients `λ_n=2` for odd n, `λ_(2m)=2+2(-1)^(m+1)`. These are **fake** entire functions, not the Riemann xi-function and not even asserted to possess its original prime Euler product or Gamma completion. They prove only that *functional equation + right-half-plane zero-freeness + endpoint normalization + finite positive Li data* do not, by themselves, force critical-line zeros. SUCC's prior `euler_gamma_li_bridge.py` has a stronger original-completion finite-jet mutation test; it is linked, not rewritten.

## CXP-08 — exact Li circle-reading identification (CLASSICAL, no new sign)

Near w=0, because F(0)=1,

`d/dw log F(w) = sum_(n>=1) λ_n w^(n-1)` and `log F(w)=sum_(n>=1)(λ_n/n)w^n`.

The coefficients are those of the original completed xi-function and are already sourced/calibrated in SUCC `observational_succ/euler_gamma_li_bridge.py`; the symmetry `λ_-n=λ_n` makes this choice equivalent to the standard expansion at s=1 (Lagarias, 2007). Li's criterion states RH iff `λ_n>=0` for all n≥1. A finite positive prefix is not a proof. In the pin-bed language, finite Fourier/Taylor response data are **true finite observation outputs** but do not decide an arbitrary infinite source property unless the corresponding target descends through the observation fibers. The exact source-normalized log continuation/zero holonomy remains the missing global theorem.

## Cross-program claim verdict and next decisive test

**DISCL0SED/CLASSICAL WITH PROOF:** CXP-01, CXP-02 equivalence, CXP-03 Jensen and conditional zero count, CXP-04 finite shifted-root geometry, CXP-05 Mertens/Hurwitz countermodel, CXP-06 convergent Euler tail, CXP-07 fake finite calibrations, CXP-08 Li coefficient identification. These results belong to classical complex analysis, prime number theory and basic exact algebra; the combination is an original *SUCC research instrument*, not a new standalone global theorem.

**OBSERVED-FINITE:** exact Fraction algebra, sieve cutoff products and numeric original-completion comparisons; all tests have scoped source data and fake controls. Numerical contour winding without analytic enclosure is explicitly NONCERTIFYING.

**REFUTED:** 'every finite factor has unit-circle roots, so a global analytic continuation must'; 'the Euler-product zero-free horodisk already covers the critical disk'; 'Gamma/Mertens normalization alone enforces RH'; 'reflection symmetry and finite positive Li data are enough'; 'Euler factor local poles are nontrivial ξ zeros'.

**OPEN (RH):** derive from the **actual** unshifted prime/Archimedean source a signed/positive arithmetic inequality proving the global source log extends holomorphically (or all zero-count Jensen defects vanish, or the completed Suzuki/Weil form is positive). The half-density-shifted product is a wrong-source counterexample, not a candidate substitute. Compare original primes vs fake composite six, wrong shift, wrong Gamma completion, critical boundary, and arbitrary finite-step path sampling. Any proposed certificate must supply rigorous contour/log-mean enclosures uniform in the required radius and cannot constructively insert nontrivial zero locations.

**Specific cross-program route:** The source-conditioned quantity is the **logarithmic connection** `ω_E=d log[2ξ(s(w))]` on the Euler horodisk. Attempt a prime–Archimedean source-preserving extension plus a coercive obstruction estimate on the unit-disk complement. This identifies the same global cancellation/positivity seam already isolated in `FuckingRH` and SUCC's `RH_HANDOFF.md`, but presently does **not** pay that debt. A successful next result would be an independently certified nonzero lower bound for the distance from all source-admissible zero-bearing fake completions, or a Jensen upper bound strictly below `log(r/r0)` at radii approaching one, from prime/Gamma data alone.

### Original-source and literature passports

- SUCC `AGENTS.md`, `docs/RH_HANDOFF.md`, `docs/CATEGORICAL_OBSERVER_ATLAS.md`, `observational_succ/euler_gamma_li_bridge.py` and `handoffs/rh/2026-10-24-euler-mascheroni-completed-li.md`. This research does not modify any of these.
- DLMF §25.10 https://dlmf.nist.gov/25.10 — critical strip/zero-free Euler region.
- Lagarias, *Li Coefficients for Automorphic L-functions*, Annales de l'Institut Fourier 57 (2007), https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf — derivative generating function, gamma/prime split, Li criterion.
- Lagarias, *Euler's Constant: Euler's Work and Modern Developments*, arXiv:1303.1856, §3.3 — Mertens product with e^-γ, https://arxiv.org/abs/1303.1856 .
- Standard Jensen formula / argument principle / Hurwitz theorem. Prior classical results retain original credit.
