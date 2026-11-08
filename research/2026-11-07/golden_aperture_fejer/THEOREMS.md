# SUCC GOLDEN APERTURE × SPATIAL FEJÉR TRIANGLE × DYADIC SOURCE FIBERS

**Research-only, 2026-11-07.** Exact parent SUCC PR #538 `eda162b5610d4a9d66bb3c3acbcdc728cbc0eccd`; sister PR #539 `c8c5cf0488b3667b0f603983e9ad3766ba78e546` read-only. Original four signed BBP terms and `U_0=0` are immutable. `PROVED LOCAL` below denotes the written elementary derivations, not a Lean certificate, independent referee, or π-normality.

## 0. Correctly typed setup and conventions

Use the circle `T=R/Z`, normalized Haar measure `m(dt)=dt`, and `e_h(x)=exp(2πihx)`. For arc **fractional circumference** `c in (0,1)`, let `ν_c` be uniform measure on an arc of length `c` centered at zero, and define the *observed normalized arc density* `f_{c,μ}=d(μ*ν_c)/dm` and squared discrepancy

`E_c(μ)=||f_{c,μ}-1||²_(L²(m))`.

Select the golden number `a=φ^-1=(sqrt5-1)/2`, with `b=1-a=a²=(3-sqrt5)/2 <1/2`. This is exactly the fixed golden aperture of sister #539: its angular half-width is `δ=πa`. This source-independent *observer width* is not the authentic source's silver Pisot unit `1+sqrt2` and not a physical law.

For the authentic BBP forcing, retain the full FOUR signed terms

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`;
`U_0=0`, `U_(n+1)=16 U_n+r(n+1)`, `x_n={U_n}`;
`T_n=sum_(j>=1)16^-j r(n+j)`, `z_n={U_n+T_n}={16^n π/16}`.

The previously established source bound `0<T_n<1/[15(n+1)²]` holds for n≥1. Let `I_A=[A,2A)` (A≥1 integer), and write `μ_A^x=A^-1 Σ_(n in I_A)δ_(x_n)`, `μ_A^z` analogously. Put `d_T(x,y)=min_{m in Z}|x-y-m|`. **All finite original x_n are rational; no π digits are used in the exact certificates.**

## GA-01: golden complementary aperture law — PROVED LOCAL

For every circle probability measure μ and every c∈(0,1), the complementary arc of length `1-c` is a half-turn translate of the complement of an arc of length c. Consequently

`f_(c,μ)-1= -((1-c)/c) [f_(1-c,μ)(·+1/2)-1]`

(up to a harmless orientation convention). Taking L² norms yields

`E_c(μ)=((1-c)/c)² E_(1-c)(μ)`.

With `a=φ^-1`, `b=1-a=a²`, therefore

**`E_a(μ)=a² E_b(μ)=b E_b(μ)`**.   (GA1)

This is exact for *any* μ. The special feature is the **self-similarity of the two aperture lengths** `b=a²`, not an arithmetic result about π. It is consistent with #539 HPB-C5's optional design equality of geometric aperture a and locked-point discrepancy `1/a−1=a`.

## GA-02: the spatial Fejér triangle and exact signed integrated collision excess — PROVED LOCAL

For b<1/2, two equal arcs of length b, centered at x and y, overlap in normalized Haar length

`(b-d_T(x,y))_+`, where `(u)_+=max(u,0)`.

Thus for any empirical measure `μ_N=N^-1 Σ_(i=1)^N δ_(x_i)`:

`E_b(μ_N)= (1/(b²N²)) Σ_(i,j)(b-d_T(x_i,x_j))_+ −1`.

Using GA1 and b=a² gives the exact **golden spatial triangle**

**`E_a(μ_N)= (1/(bN²)) Σ_(i,j)(b-d_T(x_i,x_j))_+ − b`.**    (GA2)

Equivalently, define the ordered near-pair count `B_N(t)=#{(i,j):d_T(x_i,x_j)≤t}` (including the N diagonals). Since `(b-d)_+=∫_0^b 1[d≤t]dt`, the same expression is

**`E_a(μ_N)= (1/(bN²)) ∫_0^b [B_N(t)−2N²t]dt`.**  (GA3)

The integral on the right is **nonnegative for every point configuration**; individual integrand values can have either sign. This positivity is genuinely a whole-coupling theorem, not pointwise positivity. Its proof is the L²-square construction. With the original rational states, every summand is in `Q(sqrt5)`, and comparisons `d<b` are exact: since `0≤d≤1/2`, `d<b` iff `(3−2d)²>5`.

Define the continuous, symmetric **golden characteristic kernel**

`k_gold(t)=(b-||t||_T)_+/b −b`.

Then `E_a(μ_N)=N^-2 Σ_(i,j)k_gold(x_i−x_j)`. Its circle Fourier coefficients are `khat(0)=0` and

`khat(h)=sin²(πhb)/(π²h²b)=sinc²(πha)>0` for h≠0,

since b is irrational. Hence the kernel is positive definite on zero-mass measures and **characteristic**: `E_a(μ)=0 iff μ=Haar`. It is `1/b`-Lipschitz because `t→||t||_T` and the positive-part map are 1-Lipschitz.

At a locked point `δ_x`, `E_a(δ_x)=k_gold(0)=1-b=a`. By contrast E=0 for Haar. These are exact calibrations, not assumptions about BBP.

## GA-03: a ONE-SCALAR, one-fixed-radius normality criterion — PROVED CONDITIONAL, premise OPEN

Sister #539 gives the Fourier representation

`E_a(μ)=Σ_(h≠0) sinc²(πha)|μhat(h)|²`.

Every multiplier is strictly positive because a is irrational. Therefore for **any** sequence of probability measures on T, `E_a(μ_j)→0` iff `μ_j⇒Haar`: one direction tests each fixed h, the reverse uses dominated convergence under `Σ 1/(h²π²a²)<∞`.

Applying this to original BBP epochs, the source tail `T_n→0` ensures the same limiting empirical distribution for `μ_A^x` and `μ_A^z`; epoch-to-prefix dyadic decomposition (or previous ET3) identifies all-epoch Haar with base16 normality of π. Consequently the following single scalar is a **precise equivalence, not an achieved estimate**:

**`π normal base16 ⇔ E_a(μ_A^x)→0 ⇔ (1/A²)∫_0^b [B_A^x(t)−2A²t]dt→0`.**  (GA4 OPEN LIMIT)

The integrated excess is always nonnegative, so one needs only a source-selected *upper* bound `o(A²)` for its numerator. This does not prove the upper bound. A one-sided upper bound `B_A(t)≤A+KA²t` on all `0≤t≤b` only yields

`E_a(μ_A)≤1/A+(K−2)b/2`.

In particular the finite K=3 estimates from #536/#538 **do not, by this direct integration alone, establish decay**. Their normality consequence requires the separate ×16 frequency-ray rigidity.

## GA-04: new UNSQUARED source-to-π golden energy transport — PROVED LOCAL

For the authentic original source and any A≥1, source tail bounds give

`d_T(z_n,x_n)≤T_n<1/[15(n+1)²]` for n in I_A.

Because `t→(b−t)_+` is 1-Lipschitz and circular distances change by at most the sum of point displacements,

`|E_a(μ_A^z)−E_a(μ_A^x)| ≤ (1/(bA²)) Σ_(n,m in I_A)(T_n+T_m)`
`=(2/(bA))Σ_(n in I_A)T_n`.

Bound the epoch tail average by

`(1/A)Σ_(n=A)^(2A−1)T_n <(1/(15A))Σ (n+1)^(-2) ≤1/(30A²)`, using the integral of x^-2 from A to 2A. Therefore

**`|E_a(μ_A^π)−E_a(μ_A^U)| ≤1/(15b A²)`.**   (GA5)

The source-specific error tends to zero as **O(A^-2) in the energy itself**. This is a different, fixed-aperture observable from #538 ET1's critical H=A Fejér norm, which has O(A^-1/2) *square-root* transfer. No source-selected real Haar conclusion follows from GA5 alone.

For comparison, the direct L² translated-arc argument also gives the weaker but useful norm estimate

`|sqrt(E_a(μ_A^π))−sqrt(E_a(μ_A^U))| ≤ sqrt(2/15)/(aA) (H_(2A)−H_A) ≤sqrt(2/15) log2/(aA)`.

## GA-05: the TWO-AXIS source-clock × spatial-triangle hologram — PROVED LOCAL identity, OPEN saving

Let N=QM, Q=2^k, and use any contiguous original BBP epoch of length N (e.g. [N,2N)). For each j mod Q let `μ_j=M^-1 Σ_(t=0)^(M−1)δ_(x_{start+j+tQ})`. The original 2-adic source graph V is an isometry on Z₂; thus `V(n) modQ` is a permutation of the time labels `n modQ`, so these are **exactly the original source-state residue fibers, relabeled**. They do not create a new source distribution.

Define `g_j=f_(a,μ_j)−1`, `g=Q^-1Σ_j g_j=f_(a,μ)−1` and

`G_(Q,M)^gold := Q^-1Σ_j ||g_j||²_(L²(m))`.

The Hilbert variance decomposition is EXACT:

**`G_(Q,M)^gold = E_a(μ) + Q^-1Σ_j||g_j−g||²`.**  (GA6)

By the spectral form and FG-03/FG-04 of parent #535,

**`G_(Q,M)^gold = Σ_(h≠0) sinc²(πha) R_(Q,M)(h)`.**  (GA7)

Here `R_(Q,M)(h)=Q^-1Σ_j|M^-1Σ_t e(hx_(start+j+tQ))|²` is exactly SUCC's real return-fiber energy. Because the weights are summable and nonnegative, no questionable infinite interchange is needed. There is also a purely *arithmetic spatial* evaluation:

**`G_(Q,M)^gold = [1/(bQM²)]Σ_(j=0)^(Q−1)Σ_(s,t=0)^(M−1)(b−d_T(x_(j+sQ),x_(j+tQ)))_+−b`.**  (GA8)

At fixed N, splitting every Q fiber into its two children at 2Q gives

**`G_(2Q,M/2)^gold−G_(Q,M)^gold = (1/(4Q))Σ_(j=0)^(Q−1)||g_(j,0)−g_(j,1)||²≥0`.**   (GA9)

Therefore, for the dyadic partition, `E_a(μ)=G_1≤G_2≤...≤G_N=a`. This is a genuine 2D (dyadic-time × golden-space) energy bookkeeping identity. **Refinement reveals conditional distinctions; it does not automatically lower real coherence.** Constant phase controls give `G_Q=a` for all Q; uniform grids have small global E but need not small G_N.

If the original zero-seeded source admits a sequence of sufficiently dense horizons/epochs with `G_(Q,M)^gold→0`, then `E_a(μ)≤G→0` and π normality follows. For Q growing, this is generally STRONGER than normality; no signed source estimate on G is proved. Its value is a single real positive, fixed-width, carry-/source-typed target subsuming all frequencies of the earlier R(h).

## GA-06: uniform-in-Q completion transport for the TWO-AXIS energy — PROVED LOCAL

Apply the same 1/b-Lipschitz kernel argument separately on each residue fiber. Each fiber contains M points, so its energy difference after adding the authentic T_n has magnitude at most `(2/(bM))Σ_(n in fiber)T_n`. Averaging all Q fibers yields exactly

`|G_(Q,M)^gold(z)−G_(Q,M)^gold(x)| ≤(2/(bN))Σ_(n in epoch)T_n`.

For an epoch `[A,2A)` with N=A=QM, deduce the **UNIFORM-IN-RESOLUTION** bound

**`|G_(Q,M)^gold(π)−G_(Q,M)^gold(BBP)| ≤ 1/(15b A²)`** for every power-of-two Q dividing A.  (GA10)

This adds a genuine all-horizon source-gauge stability estimate to the return-fiber construction. It is not source-selected signed cancellation or a π normality proof.

## GA-07: quantitative connection to PR #538 critical Fejér rays — PROVED CONDITIONAL

For completed ×16 phases `z_n`, write `C_(A,A)^z` for the exact positive critical Fejér collision energy of parent #538. Fix `1≤H≤(A+1)/2`, `J=floor(log_16((A+1)/(2H)))≥0`. By the endpoint shift `|W_A^z(16^j h)−W_A^z(h)|≤2j/A`, the Fejér weight at h16^j is at least 1/2 for 0≤j≤J and 1≤|h|≤H. Hence

`|W_A^z(h)| ≤ sqrt[(C_(A,A)^z−1)/(J+1)]+2J/A` for 1≤|h|≤H.

The golden Fourier weights sum to `Σ_(h≠0)sinc²(πha)=1/a−1=a`. The high-frequency tail obeys `2Σ_(h>H) sinc²(πha)≤ 2/(π² a² H)`. Thus

**`E_a(μ_A^z)≤a( sqrt[(C_(A,A)^z−1)/(J+1)] + 2J/A)^2 + 2/(π² a² H)`.** (GA11)

With H≈sqrt(A), this proves `E_a=O(1/log A)+O(A^-1/2)` if the authentic critical Fejér energies are uniformly bounded. Parent #538 ET1 transfers bounded `C^x_(A,A)` to bounded `C^z_(A,A)`. **The needed all-A bound on C is OPEN.** This is quantitative output of an assumed source bound, not a new arithmetic saving.

## GA-08: exact computational method, certified finite receipts — PROVED ALGORITHM / OBSERVED FINITE

For original rational x_n, exact threshold `d<b` iff `(3−2d)^2>5` (0≤d≤1/2). Sort the rational points on the circle and sweep the clockwise gaps; since b<1/2, each unordered near pair appears in exactly one short oriented arc. This uses O(A log A) *order comparisons* plus O(A) sliding-window updates, rather than Θ(A²) pair comparisons (bit complexity depends on growing rational denominators).

For large A, avoid forming the enormous common denominator of the sum of all distances: compute each exact input rational x_n's integer floor at fixed scale P=10^digits; use rational bands of width 1/P on clockwise gaps, check b against certified rational bounds from integer-isqrt(5P²), and fall back to exact Fraction comparisons when a threshold is ambiguous. Count near pairs exactly, bound each selected gap by ±1/P, and propagate outward rational intervals through GA2. This is a **rigorous interval algorithm, not floating-point estimation**. Tests compare it against full Fraction brute force and direct high-precision arc-sweep oracle.

**Predeclared source-exact energy certificates:** A=79: [0.01035985538469, 0.01035985538470]; A=157: [0.00216407887510,0.00216407887511]; A=281: [0.00211303656019,0.00211303656020]; A=389: [0.00284911123664,0.00284911123665]. These are mathematically finite, **not asymptotic decay evidence**. A=512 was measured as performance calibration after the first results, not a blind holdout.

**Fresh preregistered large epochs:** A=1024: [0.00116171098489,0.00116171098490]; A=2048: [0.00024354735393,0.00024354735394]. The A=4096 computation timed out and is **NOT VERIFIED**. Earlier attempted exact denominator-sum engine also timed out, preserved as a performance failure; the fixed-point interval engine passed the held-out A1024/2048 cases without changing source or width. These finite values alone prove nothing about π normality.

Separate exploratory Q-fiber data are stored in FIBER_PROBE.json, not preregistered blind holdouts. Different-formula combined rational BBP source plus direct moving-arc interval sweep in independent_oracle.py agrees with exact pair evaluations on five small epochs; same mathematical premise, **not independent academic peer review**.

## Hostile boundaries and next theorem

- A completed periodic β=1/5 ghost is locked at one phase, so `E_a=G_Q=a`, not zero. Its real initial seed for the authentic forcing is irrational, outside the 2-adic rational-seed completion model.
- A zero-seeded alternative rational source H(n)=n/(2n−1)^4 has 2-adic Haar residues, but real phases→0, so `E_a→a` and `G_Q` need not tend to 0. Universal 2-adic-Haar ⇒ golden-real-Haar is refuted.
- The golden Pisot-power trajectory likewise locks and has E→a; stable conjugate Gamma/harmonic threshold of #539 is an **anti-normality** control, not a source-selected π proof.
- Rational aperture fractions may erase Fourier modes completely; golden irrational width does not. But any irrational fixed aperture has this property; golden is selected by the additional optional complement-self-similarity criterion.
- The new kernel is a faithful, stable *test instrument*, not a mechanism proving its own energy decays. Exact observation and source tail only transport an arithmetic theorem if it is first proved for the selected zero-seeded orbit.

**Next OPEN source-specific theorem:** prove for original `r(n)` and U0=0 the one-sided all-epoch integrated bound

`∫_0^b (B_A^U(t)−2A²t)dt=o(A²)`,

or a stronger/alternative source-selected golden dyadic-fiber bound `G_(Q_A,M_A)^gold→0` over sufficiently dense horizons with appropriate Q_A. Either would imply real Haar/π normality. No such bound is obtained here. The exact source carries, odd-prime correlations and original zero boundary must pay for its signed fluctuations. The K3 all-radius finite results and these golden finite certificates cannot substitute for an infinite proof.

## Source/provenance

Primary inputs: original BBP Bailey–Borwein–Plouffe source as pinned in SUCC main and #538; mathematical input #538 epoch-critical Fejér transport and #535 dyadic return-energy. Golden aperture, self-calibration and irrational Fourier multipliers: sibling #539 CIRCLE_WINDOW.md. Original 2-adic source-clock isometry: #527. Historic silver/Gamma/Pisot structures from #529/#534 are **separate typed coordinates**; no γ, φ or quantum identification at the source is asserted. Frozen source/Lean/provenance/workflows/license/main untouched.

## GA-09: rigorous distinction between the new circular-aperture model's *locking* and real Haar — PROVED LOCAL synthesis

The new sister #539 harmonic–Pisot boundary assumes a phase history `z_n=e(t_n)` and a finite weighted defect budget `Q_∞=Σ_(n≥1)[1−Re(z_n)]/n<∞`. Its HPB-04 result shows `(1/N)Σ_(n≤N)|z_n−1|²→0`, hence its empirical circle measures converge weakly to `δ_0`. Because `E_a` is continuous under weak convergence (its Fourier weights are summable), the exact golden window yields

**`Q_∞<∞ ⇒ E_a(μ_N)→E_a(δ_0)=a=φ^-1`, NOT zero.** (GA12)

The normality regime instead requires `E_a→0`. Thus the *same fixed observer* cleanly distinguishes harmonic phase-locking from Haar, without confusing its persistent **geometric** aperture with the realized temporal distribution. This is a source-independent discriminator and must not be applied to π without independently verifying the required hypothesis. In particular, proving a finite harmonic defect budget for authentic π would contradict its proposed normality rather than support it.
