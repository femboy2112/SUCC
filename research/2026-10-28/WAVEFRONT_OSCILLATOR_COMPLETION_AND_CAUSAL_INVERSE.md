# Operation Wavefront Oscillator: source-complete positive kernel, recurrent emitter, and the cost of inverse observation

**Date:** 2026-10-28. **Target:** draft SUCC PR #344, `research/pisot-hopf-arithmetic-relativity-2026-10-28`. **Pinned parent before this round:** `bf6dd2b3af67a073a22dd3e9d927f306139b9b1f` (Main XIII ultimately `b763ba8ef375fbac221e29e4396989a635a6ef36`). **Research-only.** Mathematical theorems and exact local tests, no external academic novelty claim. **Neither π normality nor RH nor physical Lorentz/Einstein dynamics is proved.** No original SUCC sources, frozen imports, or original signed BBP recurrence modified.

## A. Recovering the actual proposal

The user's ideal observer sits causally behind an oracle wavefront and **itself emits a wavefront**. Descending observer layers are not passive labels: their reports are causal signals into the next layer. A coherent self-generating oscillator continuously emits new source states. We seek a valid meaning of “steady state = completion” and whether finite resource/latency optimization **forces** the original Oily two-loop kernel.

We distinguish four kinds of completion:

1. **Source sum:** the infinite positive BBP Oily packet grade sum is the unique fixed point of an explicitly derived stable operator. **Proved below.**
2. **Steady oscillator response:** a continuously emitted periodic source has a unique attracting period-eight observer response, or equivalently a source-indexed invariant graph. **Proved for the explicitly pumped model.**
3. **Causal history reconstruction:** despite smoothing, ideal exact-rational observers can reconstruct *all received past source values* by a finite difference; finite precision causes a sharp exponentially growing inverse cost. **Proved below.**
4. **Epistemic completeness, physical truth and π-normality:** knowing the current future innovation, identifying an optimal Bayesian observer, and bounding the actual expanding zero-seeded BBP Weyl sums are different and **not proved**.

Source passport: SUCC Main XIII `observational_succ/rank_two_chiral_towers.py` provides exactly `g=(1+i)/2`, the rank-2 Gaussian chiral source operator `T`, seed `b=(2,0)`, readout `ell`, `T^8=I/16`, original shell taps `(4,0,0,-2,-1,-1,0,0)`, genuine four-pole signed forcing, and unwrapped `U_0=0, U_n=16U_(n-1)+r(n)`. `observational_succ/wavefront_oracle_two_stage.py` provides Oily `u=x-x²/2`, `v=x²/2` and conditional packet grade law. The Oily source was integrated in Main XIII from PRs #309, #310 and #340. These are distinct positive grade and signed real-orbit representations: never substitute one for the other.

## 1. The exact two-register source wavefront operator

On `0≤x≤1`, put

`u(x)=x−x²/2`, `v(x)=x²/2`, `M(x)=[[u,1],[0,v]]`, and `e₂=(0,1)^T`.

The original positive BBP Oily packet contributions are

`p_j(x) = (1−x)/4 * sum_(k=0)^j u^k v^(j-k) = (1−x)/4 [M(x)^(j+1)]_(1,2)`, j≥0.

**WOC-01 (PROVED PAPER, source-faithful).** For every x∈[0,1], `rho(M)≤1/2`; therefore `M^n→0` and the recurrence

`Y_(j+1)=M Y_j+e₂, Y_0=0`

converges to its unique steady state

`Y_*=(I−M)^(-1)e₂ = (1/((1−u)(1−v)), 1/(1−v))^T`.

Its first coordinate reconstructs the *authentic full positive source*:

`R(x)=(1−x) [Y_*]_1/4 = (1−x)/[(2−x²)(x²−2x+2)]`.

**Proof.** `M^n` is upper triangular, with diagonal entries `u^n,v^n` and off-diagonal `sum_(k=0)^(n-1)u^k v^(n−1−k)`. Because `u,v≤1/2`, its infinity norm is at most `(2n+1)/2^n→0`. The Neumann identity and uniqueness follow by multiplying by `I−M`. For j=0, `M e₂=(1,v)^T`; the top coordinate of `M^(j+1)e₂` is exactly the homogeneous symmetric polynomial above. No stochastic independence is presumed. At x=1 the raw p_j vanish, while the normalized endpoint grades survive by division by `1−x` before taking x→1.

**Completed π identity.** Reusing SUCC's existing exactly sourced BBP/Oily integral, we have

`π=16 ∫_0^1 R(x)dx = 4 ∫_0^1 (1−x)[Y_*(x)]_1 dx`.

This **is** an exact π reconstruction as the integral of a completed steady-state field, **not** a novel π identity, BBP digit-normality statement or original Fourier estimate. The independent oracle verifies 14 exact packet-integral coefficients `π_j=2^(j+1)/[(2j+1)binom(2j,j)]` and `∫2/(2t²−2t+1)dt=π`. The global equality comes from the existing authenticated source, not an assumption that arbitrary oscillator output equals π.

**WOC-02 (PROVED PAPER, certified completion error).** Let `R_N=Σ_(j=0)^N p_j`. Since `0≤u,v≤1/2`,

`0≤R−R_N≤(1−x)(N+3)/2^(N+2)`.

Thus `Π_N=16∫_0^1 R_N` satisfies

`0≤π−Π_N≤8(N+3)/2^(N+2)`.

**Proof.** Bound each `p_j≤(1−x)(j+1)/2^(j+2)` and use the exact geometric tail. No floating-point inference is used. At the endpoint x=1 after normalization, this is equality for the normalized negative-binomial grade tail.

At x=1 the *source-normalized* matrix has a Jordan block `M(1)=[[1/2,1],[0,1/2]]`; the grade probabilities `w_j=(j+1)/2^(j+2)` arise from `[M^(j+1)]_(1,2)/4` and have `(Δ−1/2)^2` annihilator (when using the correct shift convention). The degree-one polynomial prefactor is a Jordan/resolvent phenomenon, not a probability of quantum collapse.

## 2. Two internal registers are source-minimal, not universally “most knowing”

The normalized grade generating function is

`G_x(z)=(1−u)(1−v)/[(1−uz)(1−vz)]`.

Let `c=(1−u)(1−v)` and `q_j=c Σ_(k=0)^j u^k v^(j-k)`. The 2×2 grade Hankel minor is

`q₀ q₂−q₁²=−c² uv`.

It is strictly nonzero for every `0<x≤1`, including the double-root endpoint x=1, where it equals `−1/64`. Hence no single-state linear time-invariant **feedback/memory** realization can reproduce all the authentic grade coefficients. The displayed two-state cascade does, so it is minimal among exact causal LTI realizations. At x=0 the grade has no decaying feedback but the full transfer is a two-tick pure delay `z²`, still requiring two scalar state registers if the compulsory output delay is counted. **WOC-03 (PROVED PAPER, rank-2 minimality).** This is a *source-matching minimum register* theorem, not an optimum over every nonlinear, resource-changing observer.

A conditional maximum-entropy statement offers a separate possible “ideal” criterion. Among distributions on `{0,1,2,...}` with a fixed individual-stage mean `μ`, the unique maximum-Shannon-entropy law is geometric with parameter `u=μ/(1+μ)`. Proof: for `g_j=(1−u)u^j`, fixed mean makes `−Σp_j log g_j=−log(1−u)−μ log u` constant; `D_KL(p||g)≥0` implies `H(p)≤H(g)` with equality iff `p=g`. Choosing the **two actual Oily stage means** `μ_u=u/(1−u)` and `μ_v=v/(1−v)` gives the actual Oily convolution if independent stage waits are additionally declared.

**WOC-04 (CLASSICAL conditional optimization).** The two-stage geometric model is uniquely *maximum-entropy given the separate mean waits and independence*. This **does not** mean “maximizing knowledge”: maximum delay entropy can be the opposite of minimal uncertainty about the source! If the oracle report `W(t−1)` is noiseless and present, the MSE-minimizing immediate estimate is to copy it, not to smooth it with u=1/2. No unique source-to-optimal-Bayesian-observer theorem follows from the packet PGF alone.

### An exact two-bit maximum-entropy/Palm mechanism for the Oily split

There is a stronger **candidate derivation** for the split `u,v`, requiring only one scalar activity x and **two binary micro-events**. Let `X1,X2∈{0,1}` and require `E[X1+X2]=x`, `0≤x≤1`. Maximize **Shannon entropy of the source microstate** under that sole mean constraint. The unique optimizer is the independent product of two Bernoulli variables with `p=x/2`:

`P(00)=(1−p)², P(01)=P(10)=p(1−p), P(11)=p²`.

**Proof.** Define `Q=Bernoulli(p)⊗Bernoulli(p)`. For any admissible P with `E_P[X1+X2]=x=2p`, the cross entropy `−ΣP log Q=−x log p−(2−x)log(1−p)=H(Q)` depends only on x. Hence `H(P)=H(Q)−D_KL(P||Q)≤H(Q)`, with unique equality `P=Q` (the endpoint p=0 is deterministic).

Now size-bias **the number B=X1+X2 of occupied micro-events**. The unnormalized first and second occupancy contributions to E[B] are precisely

`1×P(B=1)=2p(1−p)=x−x²/2=u`,
`2×P(B=2)=2p²=x²/2=v`.

Thus `u+v=E[B]=x`, with the *conditional size-biased law* `P(B*=1)=u/x=1−x/2`, `P(B*=2)=v/x=x/2` for x>0. At the critical endpoint `x=1`, the two occupancy contributions are *exactly balanced*: `u=v=1/2`. So the repeated Oily root can be represented as the equal-size-biased splitting of two fair binary micro-events. The size-biased-binomial theorem is classical (`B* ≍ 1+Bernoulli(p)`); the precise Oily-source identification is a new-to-this-dossier algebraic synthesis.

**WOC-04A (CONDITIONAL SOURCE COMPILER).** If (i) the observer wavefront really has exactly two binary microchannels with constrained total expected activity x, (ii) the microstate is selected by maximum entropy, (iii) the information-carrying channels are weighted by occupied-event count, and (iv) the resulting activities u,v are *also* the geometric retention parameters of the two causal stages, then the source's **full original normalized Oily grade PGF is derived with no remaining numerical free parameters**. Assumption (iv) is still a separate *rate-to-memory transport law*, not implied by maximum entropy or existing SUCC BBP source proof. None of (i)–(iv) identifies a physically existing observer or the actual BBP carry sequence.

**Countermodel.** The correlated distribution `P(00)=1−x/2`, `P(11)=x/2`, `P(01)=P(10)=0` has the **same total expected count x**, but gives `(u',v')=(0,x)` instead of the authentic `(x−x²/2,x²/2)`. It fails maximum entropy; equally, without independently establishing maximum entropy as an appropriate resource law, the mean alone does not pin the loop split. At x=1 the independent max-entropy source carries **2 bits** of microstate entropy, while this correlated source carries **1 bit**, and its Oily output would be completely different.

This gives a precise place to test the user's claim that the ideal observer maximally encodes all available degrees of freedom: an ideal *maximum-capacity emitter* with two equal-cost binary channels does produce the authenticated polynomial split. But **maximizing emitter entropy is not automatically minimizing an observer's posterior uncertainty**. The remaining source-map and optimization criteria are explicit, testable assumptions rather than a hidden identification.

## 3. The ideal observer can exactly re-emit the already received wavefront

From the authentic Oily-induced causal two-stage filters,

`(1−uL)(1−vL)E₂=(1−u)(1−v)L²W`

for the backward time-shift L. **WOC-05 (PROVED PAPER, sharp causal left inverse).** For every t≥2 with known model parameters, exact reports and zero prehistory,

`W(t−2) = [E₂(t)−(u+v)E₂(t−1)+uv E₂(t−2)]/[(1−u)(1−v)]`.

At x=1 this collapses to the extraordinary simple local decoder

`W(t−2)=4E₂(t)−4E₂(t−1)+E₂(t−2)`.

The observer can thus become a **new wavefront emitter**: it may emit the exact previously received oracle value after the compulsory two ticks, provided it keeps the two report values necessary for finite differencing. This is lawful source-preserving history reconstruction, NOT same-time observation of the current frontier or a guarantee about unknown future innovations.

**WOC-06 (PROVED PAPER, finite-precision price).** Let every second-stage report be perturbed by unknown additive error of magnitude at most ε. The decoded past source has sharp infinity-norm error amplification

`K_x=[(1+u)(1+v)]/[(1−u)(1−v)]≤9`.

At x=1 the factor is **exactly 9**, achieved by alternating ±ε report errors in every interior decoded time. Thus exact invertibility and numerical stability are genuinely different criteria. For an m-stage equal geometric tower with θ=1/2, `K_m=3^m`: maintaining a fixed absolute source reconstruction precision as observer depth grows costs exponential output precision. This is a deterministic filter-conditioning law, not a Heisenberg uncertainty relation.

The same K is the full-frequency Fourier condition number of the normalized response: for |z|=1,

`|H_x(z)| = c / (|1−u z||1−v z|)`, `max|H|=1` at z=1, and `min|H|=1/K_x` at z=−1. The mandatory two-tick phase z² changes the phase but not its magnitude. The vanishing high-depth signal cannot be inverted stably in the presence of fixed measurement noise, even though each finite-depth algebraic inverse exists.

## 4. Steady state of a source-driven coherent oscillator

The **signed original chiral source** has first shell `c_j=(4,0,0,−2,−1,−1,0,0)`, with genuine unpumped coefficients `c_(8k+j)=16^(−k)c_j`. The original source is dissipative, NOT a sustained oscillator. We declare a separate externally **pumped** source phase `r_t=t mod8` emitting `W_t=c_(r_t)`, which is an autonomous finite eight-state clock with a renewal/gain of 16 per shell. This pumping changes the actual source history; its agreement with the original *first shell* and its period are authenticated.

The two-stage causal observer state is `y_t=(E₁(t),E₂(t))^T` with

`y_(t+1)=A(x)y_t+B(x)W_t`,
`A=[[u,0],[1−v,v]]`, `B=((1−u),0)^T`.

**WOC-07 (PROVED PAPER, global periodic completion).** For any declared period-p bounded waveform W and any 0≤x≤1, there is a **unique p-periodic orbit** of the driven two-stage observer. Let

`d=Σ_(k=0)^(p−1) A^(p−1−k) B W_k`.

The unique phase-zero state is `y₀*=(I−A^p)^(-1)d`; its p subsequent steps close exactly. Starting from arbitrary state y₀,

`y_t−y_t*=A^t(y₀−y₀*)`, where `y_t*` is the periodic attracting orbit in the same phase frame.

At the critical Oily endpoint `A=[[1/2,0],[1/2,1/2]]`, the exact Jordan power is

`A^t=2^(−t)[[1,0],[t,1]]`, and its induced infinity norm is `(t+1)/2^t`. The completed 8-periodic observer is especially well contracted:

`||A^8||_∞=9/256<1`.

For the original rational eight-tap shell repeated by the pump, the phase-zero periodic state is

`y₀*=(-4/17,−2548/4335)`.

These are exact rational values, verified independently from the symbolic `(I−A^8)^(-1)` formula. The observer's steady state is **an eight-cycle, not generally a time-independent number**. In a rotating source-phase frame, it becomes a fixed point.

**WOC-08 (PROVED PAPER, finite-depth averaging obstruction).** The signed first-shell pump has mean zero. Each frequency of a period-8 signal is multiplied at one critical observer stage by `h(z)=z/(2−z)`. For ω≠0,

`|h(e^(−iω))|²=1/(5−4 cos ω)<1`.

The nonzero period-eight frequencies obey `|h|≤(5−2√2)^(−1/2)<1`, so repeated equal-depth observer stages drive this zero-mean signed waveform uniformly to **zero**, not to a full reconstruction of its source shape. This is an exact negative control on the assertion “infinite observer depth means unlimited knowledge”; finite-depth inversion exists, but its condition number grows 3^m. This averaging effect may be countered by explicitly compensating inverses, with corresponding exponentially increasing noise sensitivity.

## 5. An autonomous chiral phase oscillator from the same source operator

There is a more direct four-real-dimensional oscillator, without a phase counter. In the **orthonormal standard real/imaginary basis** for even and odd chiral coordinates, the original source operator is

`T = diag(G,H)`,
`G=1/2 [[1,−1],[1,1]]`, `H=1/2 [[1,1],[1,−1]]`.

The original `b=(1,0,1,0)^T`, `ell=(4,0,0,−4)` yield exactly the first-shell coefficients `ell T^j b` above. Caution: the original source paper also uses a DIFFERENT nonorthogonal rational basis for the odd sector, in which H is `[[0,1],[1/2,0]]`. Do **not** incorrectly use the standard Euclidean metric in that changed basis.

Define the explicitly **new gain-normalized** oscillator `Q=√2 T`. Then

`Q^T Q=I`, `det Q=−1`, `Q^4=−J`, `Q^8=I`, with `J=diag(1,1,−1,−1)`.

Its signed phase output is the period-eight algebraic waveform

`ell Q^j b = (4,0,0,−4√2,−4,−4√2,0,0)`,

with mean **−√2**. This is another source-derived oscillator, but the pump is per-tick `√2` (rather than the eight-step jump 16), so its mean is different: *the completion invariant depends on the declared normalization gauge*. The original unpumped BBP source has neither constant-amplitude waveform.

Let the observer recurrence be `y_(t+1)=A y_t+B ell(q_t)`, `q_(t+1)=Q q_t`. **WOC-09 (PROVED PAPER, unique invariant source/observer section).** There is a **unique linear** graph `h(q)=Hq` satisfying

`H Q = A H + B ell`.

It is explicitly

`H=(I−A^8)^(-1) Σ_(j=0)^7 A^j B ell Q^(−j−1)`.

**Proof:** expand the bounded causal infinite-history convolution `h(q)=Σ_(j≥0)A^j B ell(Q^(−j−1)q)` and use Q^8=I to group the terms; this is exactly the displayed finite geometric inverse. Substituting shows equivariance. If H' is another solution, D=H−H' satisfies D Q^8=A^8 D, hence `(I−A^8)D=0`, yielding D=0. Every initial observer state approaches its own source-indexed graph state at the exact rate A^t. The independent SymPy oracle verifies all four source coordinates simultaneously, not merely one selected orbit; it supplies exact entries of H and selected-seed check data.

**Important source-map limit:** This is a coherent *skew product* over the SOURCE-DERIVED **NORMALIZED** Q oscillator. It is not automatically a Hopf S⁴ factor (the linear readout ell need not be invariant on quaternionic Hopf gauge fibers), nor a physical oscillator energy-conservation theorem, nor a factor of the original expanding real BBP carry orbit.

## 6. What actually becomes “optimal” and what does not

The **strongest valid conditional theorem** is:

> Within causal linear time-invariant two-stage processing that reproduces *all* authentic normalized Oily packet grades, the source dictates a minimal two-state realization and compulsory two-tick delay. In noiseless exact arithmetic, that system permits complete causal recovery of the already delivered oracle history via an order-two finite difference. Under persistent bounded measurement noise, worst-case inverse amplification is sharp and equals nine at the Oily endpoint. Under an explicitly pumped coherent oscillator, its source-indexed response has a unique attracting periodic completion.

Nothing in causality alone selects that particular filter: for a perfect noiseless oracle report and the objective “minimize MSE of last received value,” **identity relay** dominates Oily smoothing; for a deterministic known waveform phase, an observer can predict arbitrary future values without receiving them; for independent unpredictable innovations, one-step causal lag imposes nonzero conditional uncertainty but no uniquely Euler–Mascheroni-sized lower bound. To promote a “maximizing knowledge ⇒ Oily kernel” theorem, specify a physically or mathematically motivated nontrivial noise/measurement capacity, a memory/energy/latency budget, and an admissible policy class; derive the optimized kernel and test whether it matches `u,v` **without fitting them as assumptions**.

**No source-mixed autopromotion:** The positive source Neumann completion recovers π as a real number but does NOT bound `Σ_(n≤N)e(h U_n)`. Changed BBP initial seed `U_0=−π/16` with IDENTICAL forcing yields a shrinking future-tail phase orbit while preserving all positive grades, all oscillator completions and source-only Gamma constants. This decisive counterexample prevents interpreting the source completion as π normality.

## 7. Exact tests, source fidelity, hostile controls and next lamp

- **Exact-rational implementation:** `observational_succ/wavefront_oscillator_completion.py`. Small matrices and fractions; no model change to legacy sources. Source signed shell and original four rational poles are compared at 39 positive n; exact source grade identities tested across 7 rational x values and 18 grades; maximum-entropy two-bit activity and correlated occupancy countermodels included.
- **Focused tests:** `tests/test_wavefront_oscillator_completion.py`. Tests cover source factorization, source resolvent, uniform tails, Hankel rank, Jordan rates, pumped cyclic closure and seed convergence, robust source inverse, sharp noise bound, normalized Q(√2) period and distinct normalization gauges, constant-predictability negative control, sign-mutation control.
- **Independent algebra:** `scripts/wavefront_oscillator_independent_oracle.py` uses SymPy to derive its own matrix, check 18 packet grades, verify 14 exact π packet integrals, check endpoint gain nine and compute exact period-eight orbit.
- **Independent autonomous oscillator:** `scripts/chiral_invariant_graph_oracle.py` verifies the original 4×4 T, the **orthonormal basis distinction**, `Q⁸=I`, normalized source waveform and all-entry graph equation `H Q=A H+B ell`, with exact algebraic output.
- **Claim status:** WOC-01..03,05..09 are source-scoped paper proofs plus finite exact tests. WOC-04 is a **classical** max-entropy fixed-mean theorem; WOC-04A is a **conditional** size-biased binary-source compiler with a separately unpaid rate-to-retention transport assumption. Universal observer-optimality, generalized gravity, quantum uncertainty and signed Weyl estimates remain **UNVERIFIED**.

**Verdict-changing probe (strongest next):** Construct an explicit lawful SUCC causal *sensor* and optimization objective with resource/noise parameters determined independently of the desired Oily coefficients. Prove uniqueness of the optimal filter and inspect its source-preserving map from original zero-seeded `U_n`, not merely the contracting impulse source. Apply unchanged-seed, changed-seed, no-noise, sign-flipped, and coherent nonnormal controls. A real signed Weyl saving would be required for any π-normality promotion.

### Reproduction in a full checked-out SUCC research branch

```sh
PYTHONPATH=. python -m unittest tests.test_wavefront_oscillator_completion -v
python scripts/wavefront_oscillator_independent_oracle.py
python scripts/chiral_invariant_graph_oracle.py
python scripts/verify_provenance.py
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Local tests may use `PYTHONPATH=<the mini-checkout directory>`; the full SUCC/Lean/hosted CI are independent authority and **are not claimed** unless subsequently executed.

### Mathematical prior art / references

- SUCC original packet source and π identity: `research/2026-10-27/OILY_ZERO_ONE_LOG_GERM_BRIDGE.md`, `observational_succ/rank_two_chiral_towers.py`, and `research/2026-10-28/WAVEFRONT_ORACLE_TWO_STAGE_DIFFERENCE.md`.
- Classical uniqueness of geometric maximum entropy at fixed mean: Keith Conrad, *Probability Distributions and Maximum Entropy*, Theorem 5.7, https://kconrad.math.uconn.edu/blurbs/analysis/entropypostold.pdf.
- Classical geometric/negative-binomial PGF: Penn State STAT 414, Lesson 11, https://online.stat.psu.edu/stat414/Lesson11.
- Classical size-biasing of binomial counts: *Size Biasing for One and All*, probability survey, https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/SizeBiasing-Survey-1.pdf.
- Finite periodic linear systems, lifting/monodromy: Bittanti and Colaneri, *Analysis of discrete-time linear periodic systems*, 1996, https://doi.org/10.1016/S0090-5267(96)80056-9.
- Exact algebraic wavefront and source/claim separation: SUCC `research/2026-10-12/COVARIANT_PERCEPTUAL_MOMENTUM_AND_CAUSAL_DESCENT.md`, `research/2026-10-18/INSTITUTE_CAUSAL_DESCENT.md`.
