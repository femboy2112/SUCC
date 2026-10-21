# π, polygon SUCC, and the normality/path-defect frontier

**Date:** 2026-10-20. **Parent `main`:** `b5f9591033db2022bda6a2f16a935c06466f9eff` (Academic Main VII). **Branch:** `research/pi-polygon-normality-path-defect-2026-10-20`. **Status:** classical mathematics with exact new-to-project interfaces and a falsified general inference. **π normal in any fixed base: OPEN. No normality of π is claimed.** Original archives unchanged; no RH/abc/Weil claim.

## 0. Faithful source hypothesis, with explicit quantifiers

**Author's proposal:** Start from the circle, without privileged vertex, origin, sampling clock, or digit labels. Apply successor steps to nested inscribed/circumscribed polygons; the circle, its tangent envelope and perimeter emerge as the limiting geometry. Perhaps its rigidity forces uniform base-`b` symbolic statistics for the uniquely selected circumference/diameter ratio, or any putative non-normal representation would have to hide the uniformity in a defect of the chosen path/observation map.

The *strongest testable version* is **source-derived π path rigidity**: exhibit a constraint obtained from the **specific nested perimeter construction** (not merely from symmetry of all polygons) which forces

`∀b≥2 ∀h∈ℤ\{0}: lim_{N→∞} N^{-1} Σ_{j<N} exp(2π i h b^j π)=0`,

or prove it for one specified `b` before generalizing. By Weyl's criterion this implies base-`b` normality. It is **UNVERIFIED**. Numerical prefix agreement, random-looking behavior, injectivity, or an invariant measure alone do not entail this conclusion.

The user's proposed *path-defect alternative* must be typed: a finite approximation's failure to preserve arbitrarily long orbit statistics can indeed be an independently demonstrable **limit-order/precision defect**. A truly exceptional orbit under the canonical base map need not be a defect of the geometric source or its coding. Defining `defect := non-normal` would make the statement vacuous; we do **not** adopt that definition.

## 1. Source, paths, and observation arrows

Let `C` be a Euclidean circle of radius one; `π := circumference(C)/2`. Normalize its phase circle to `𝕋=ℝ/ℤ` with Haar probability `λ`. The circle has no privileged angle-zero; a coordinate chart does. Its tangent envelope and uniform **spatial** angular measure are invariant under reparameterization when the measure is pushed forward with the chart.

For every integer `m≥3` let

- `G_m={j/m mod 1: 0≤j<m}` be regular polygon vertex directions;
- `μ_m=m^{-1}Σ_{j=0}^{m-1}δ_{j/m}` be uniform **spatial** vertex measure;
- `T_b(x)=b x mod 1` be **temporal/scale-digit dynamics** for `b≥2`;
- `ν_N(x)=N^{-1}Σ_{j=0}^{N-1}δ_{T_b^j x}` be an **empirical orbit** measure;
- `α={π}` be the source-selected phase under an *additional* choice of mapping the perimeter ratio modulo one (not a geometric tangent direction specified by the circle itself).

Two maps on successive `G_{m b}→G_m` have the same uniform pushforward but DIFFERENT semantics:

`P(j/(mb))=floor(j/b)/m` (coarse cell/retained prefix) and

`R(j/(mb))=(j mod m)/m=T_b(j/(mb))` (rotation/digit shift).

Both have exactly `b` children per parent, so `P_* μ_{mb}=R_* μ_{mb}=μ_m`. **They are not the same morphism and do not form the same path interface.** Example: `x=1/7`, `m=4`, `b=2`, coarse quantization `q_4(x)=0`, fine `q_8(x)=1/8`. Hence `P(q_8(x))=0` but `T_2(q_8(x))=1/4`. Balanced pushforward cannot certify commuting of these source paths. The symmetry of `G_m` concerns **space averages**; digit normality concerns **one orbit's time averages**.

The roots-of-unity identity is exact:

`∫ exp(2π i h x) dμ_m = 1` if `m|h`, otherwise `0`.

Consequently `μ_m ⇒ λ` as `m→∞` through increasing divisibility (e.g. `m=4·b^n`). This proves **spatial** Fourier cancellation for each fixed nonzero `h`; it says nothing by itself about the π-orbit sum above.

## 2. Archimedean π-generation independent of π digits (POL-01)

Write `m=4·2^r` for regular polygons inscribed in the unit circle. Their squared side length `x_m=4 sin²(π/m)` obeys the exact half-angle recursion

`x_4=2`, `x_{2m}=2−sqrt(4−x_m)`.

Their normalized inscribed and circumscribed half-perimeters satisfy

`L_m=(m/2)sqrt(x_m) < π < U_m=m sqrt(x_m/(4−x_m))`.

Both inequalities are strict for finite `m`. The gap is

`U_m−L_m=m(tan(π/m)−sin(π/m))`.

For `m≥4`, use `sin θ≤θ`, `1−cos θ≤θ²/2`, `cos θ≥1/√2` for `θ=π/m≤π/4`, and `π<4` to obtain

`0<U_m−L_m≤π³/(√2 m²)<64/m²`.

The code evaluates **rational outward enclosures** of every square root with exact integer `isqrt`, and intersects successive brackets. There are no input π digits or unbounded floating-point rounding assumptions. Arbitrary precision is a **declared finite parameter**, and insufficient precision fails closed. Independently, an exact alternating-series Machin formula bounds π in unit tests; that formula is a holdout, not a source input to the polygon algorithm. Every rational enclosure yields a finite number of *certified* digit-prefix positions, and an enclosure straddling a base-`b` boundary yields **no false digits**.

Source specificity: this construction singles out π rather than an arbitrary phase and gives a quantitative error budget. It does not yet yield a π-specific lower bound on Fourier cancellation.

## 3. The noncommuting-limits theorem (POL-02; genuine path defect)

For any `x∈[0,1)`, set `q_m(x)=floor(b^m x)/b^m` and use its canonical **terminating** expansion. Every `q_m(x)` has an eventually-zero base-`b` digit tail and therefore

`lim_{N→∞}ν_N(q_m(x))=δ_0` for every finite `m`.

For fixed `N`, continuity of the circle map `T_b` implies `lim_{m→∞}ν_N(q_m(x))=ν_N(x)`. Therefore, **if x is normal in base b**, the two iterated limits are distinct:

`lim_{m→∞}lim_{N→∞}ν_N(q_m(x))=δ_0`, but

`lim_{N→∞}lim_{m→∞}ν_N(q_m(x))=λ`.

This does not *assume π is normal*. It is an unconditional theorem for every already-known normal number (e.g. the base-`b` Champernowne construction) and diagnoses why an observer who lets orbit time grow at fixed finite spatial refinement will see the wrong limiting statistics. The approximation is exact on every predeclared finite prefix when `m≥N+k−1` for `N` observed starting positions of length-`k` digit blocks. This gives exact finite source faithfulness **without uniformity in N**.

For arbitrary rational `y`, the orbit `T_b^j(y)` is eventually periodic. The π-polygon rational midpoints are therefore also non-normal as standalone numbers. It would be a false inference to transport that fact through `y→π` without paying the limit-interchange cost.

## 4. Quantitative π-specific observation transport (POL-03)

Let `L_s<π<U_s` be any exact polygon bracket from §2, `y_s=(L_s+U_s)/2`, and `ε_s=(U_s−L_s)/2`. For **any** 1-periodic real or complex Lipschitz observable `F` with circle Lipschitz constant `Lip(F)`:

`|ν_N(π)(F)−ν_N(y_s)(F)| ≤ Lip(F) ε_s (b^N−1)/(N(b−1))`.

Proof: `T_b` is `b`-Lipschitz for the circle metric, hence the absolute error at step `j` is at most `Lip(F) b^j ε_s`; sum the geometric series. The same phase result holds with `{π}` replacing `π` throughout. Inserting the polygon gap bound gives

`|difference| < 32 Lip(F) (b^N−1)/(N(b−1)m_s²)`.

For a Fourier character `F_h(x)=exp(2π i h x)`, `Lip(F_h)=2π|h|<8|h|`. Thus the true π-orbit Fourier sum differs from its rational polygon-midpoint counterpart by at most

`4|h| (U_s−L_s) (b^N−1)/(N(b−1))`.

All constants in this bound are source-derived and explicit; the sum for the rational midpoint must still be bounded independently, with its numerical evaluation and analytic tail error properly certified. At **fixed `s`**, the error budget grows exponentially in `N`: no uniform infinite-horizon conclusion follows. Sufficient refinement for a fixed `N` has `m_s` significantly larger than `b^(N/2)` (up to factors), an observation-resource cost, **not** a π normality bound.

The Lipschitz bound cannot be applied unmodified to discontinuous cylinder indicator functions. For digits use *certified strict containment* of the π interval within one base-`b` cylinder, or an explicitly sourced boundary-separation estimate.

## 5. Source-defect trichotomy and no-go theorem (POL-04–06)

**Trichotomy of possible evidence:**

1. **Source defect:** the purported circle or π enclosure is unsound; calibrate against independent exact enclosures.
2. **Transport/observation defect:** noncommuting diagrams, inconsistent sampling weights, illegal interchange of limits, or insufficient digit precision; independent finite counterexamples can certify these.
3. **Exceptional arithmetic orbit:** the exact π phase under the genuine base map might be non-generic. This possibility is **OPEN**, not automatically a problem in geometry, semantics, or observation. A claim that every such path has an independently verifiable defect needs an additional theorem defining the defect without assuming the conclusion.

**No-go:** Symmetry, nested balanced polygon weights, and compatibility of all finite source grids alone cannot force every compatible infinite path to be normal. The path `000...` is compatible with all prefix projections, and is maximally non-normal. An irrational non-normal path exists too: base-2 digits `d_n=1` exactly when `n` is a positive perfect square, else zero. Its ones have density zero, so the one-block statistics are nonuniform; gaps between ones are unbounded, hence it is not eventually periodic and represents an irrational number. Nothing is malformed about its source polygon grids.

Thus the *universal* assertion "every non-normal path in a uniform polygon inverse limit must have a flawed source/transport map" is **REFUTED**. The narrower π-specific assertion remains **UNVERIFIED**, since the circumference/perimeter selection adds special information unavailable to the generic countermodels.

The exact finite block total-variation deficit is `TV_(N,k)=(1/2)Σ_w |p_(N,k)(w)−b^(−k)|`. Base-`b` normality is equivalent to `TV_(N,k)→0` **for every fixed k**, with overlapping block starts. Balanced one-digit frequencies alone are insufficient (alternating 0101... passes `k=1` but fails `k=2`). Full Shannon/KL entropy deficit yields an analogous equivalence, but finite deficits are not probabilities of normality.

## 6. A precise conditional route that would establish normality (POL-07)

A legitimate successful proof could produce, for each fixed base `b` and integer frequency `h≠0`, polygon stages `s(N)` and rational midpoint `y_(s(N))` satisfying:

(A) `|N^{-1} Σ_{j<N} exp(2π i h b^j y_(s(N)))|→0` by a **new source-derived, noncircular** argument, and

(B) `(U_(s(N))−L_(s(N))) (b^N−1)/N→0` by the certified polygon gap.

Then the Fourier bound in §4 and Weyl's criterion imply π is base-`b` normal. Condition (B) is attainable by refining polygons aggressively; **(A) is the entire outstanding hard problem** and cannot be inferred merely from balanced grid weights, the existence of the circle, or the ability to compute many digits. If using only a sparse sequence `N_j`, one additionally needs a justified all-N interpolation condition (e.g. `N_(j+1)/N_j→1` plus bounded test observables).

This is a discriminating proof contract, not an advance to a known theorem about π's digit distribution. A π-specific ingredient could include structural control of phase correlations derived from the nested perimeter recurrence, a certified BBP-type arithmetic shift relation, or genuinely new exponential-sum estimates. None has been supplied here.

## 7. Crucible and calibrated holdouts

| Probe | Predicted from sound theory | What it refutes / detects |
| --- | --- | --- |
| Exact polygon brackets vs independent alternating Machin bounds | Both strictly enclose the same π; polygon interval narrows | Bad radical signs, interval arithmetic, source drift |
| 4→8→16→... regular polygon source | Equal angular weights and exact root cancellation spatially | Unjustified claims of time cancellation |
| `P` vs `R` at `x=1/7` | Both push forward uniform grid weights; diagrams disagree | Equating prefix and shift maps |
| `000...` and perfect-square digit stream | Both compatible; non-normal (latter irrational) | "all paths generic" / mandatory structural source defect |
| `0101...` | TV at k=1 is zero; TV at k=2 is nonzero | One-digit uniformity implies normality |
| Known normal Champernowne + its finite truncations | Normal limit; every truncation eventually zero; order matters | Interchange of `N` and `m` limits |
| Certified finite π prefixes | Exact floor containment for finite `k`; stop at first ambiguous digit | Numerical prefix samples advertised as infinite proofs |
| Rational midpoint horizon `N` | Source-to-orbit error grows at worst as geometric-series budget | Claim of a uniform `N→∞` argument from fixed polygon stage |
| π-specific Fourier cancellation | **No established decay** | The decisive currently-missing theorem |

## 8. Status, provenance, next tasks

- **POL-01** classical exhaustion + exact dyadic outward certificates, **PROVED PAPER / TESTED MODEL**; π itself is not computed using input π digits.
- **POL-02** noncommuting limits, **PROVED PAPER** (conditional difference when `x` normal; unconditional rational limit).
- **POL-03** orbit-error inequality, **PROVED PAPER / EXACT BUDGET**; no cancellation claim.
- **POL-04** finite-grid Fourier and balanced morphisms, **CLASSICAL / EXACT MODEL**.
- **POL-05** universal genericity-from-grid-symmetry inference, **REFUTED** by `0∞` and sparse-squares paths.
- **POL-06** every non-normal π encoding is necessarily a defect of a lawful path, **UNVERIFIED**; canonical digit encoding of irrational π is unique in the usual positional convention.
- **POL-07** conditional Fourier transfer route to normality, **PROVED CONDITIONAL / OPEN HYPOTHESIS (A)**.
- **POL-08** any practical π digit-frequency sample or interval certificate proves π normal, **REFUTED** as a logical inference.

**Reproduction:** `python -m unittest discover -s tests -p 'test_pi_polygon_normality.py' -v` and `python scripts/pi_polygon_normality_probe.py`. The frozen exact JSON receipt is `research/2026-10-20/PI_POLYGON_NORMALITY_FINITE_RECEIPT.json`. Testable code lives in `observational_succ/pi_polygon_normality.py`. No Lean kernel check was run; paper proofs are not certified Lean theorems.

**Related SUCC interfaces:** `docs/OBSERVER_PROOF_ACCESS.md` (source/tool/target distinctions), `docs/CARRIER_ATLAS.md` (limit ≠ finite carrier), `research/2026-10-19/FACTORIAL_BORWEIN_HOLOGRAPHIC_CLOCK.md` (sampling on a restricted range), `research/2026-10-19/PRIMORIAL_FACTORIAL_PHASE_CLOCKS.md` (fixed-vs-moving-window quantifier firewall), `research/2026-10-19/SUCC_META_GENERATIVE_CHOICE_DESCENT.md` (lawful source maps), and `docs/METHOD.md` (steelman–crucible–verdict).

**External classical sources:** Archimedean polygon exhaustion, e.g. Heath's translation and notes in [*The Works of Archimedes*](https://archive.org/details/worksofarchimede029517mbp) and [Archimedean derivation](https://pages.uoregon.edu/ddugger/area_and_volume2.pdf); normality/dynamical systems: [Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions*](https://doi.org/10.1080/10586458.2001.10504441), [Bailey–Crandall, *Random Generators and Normal Numbers*](https://doi.org/10.1080/10586458.2002.10504704). The Bailey–Crandall hypothesis is **conditional**, not a resolution of π normality. For classical normal-number constructions, consult D. G. Champernowne (1933), *The construction of decimals normal in the scale of ten*, Journal of the London Mathematical Society 8, 254–260. Independent academic novelty of this SUCC framing is unverified.

**Next decisive actions:** (1) certified rational-phase Fourier sums + independently verified analytic interval envelopes; (2) source-derived recurrence identities yielding *nontrivial* cancellation beyond generic grid symmetry; (3) explicit false-transport mutants (uniform discrete weights but malformed time map); (4) an all-horizon bound or controlled dense-subsequence interpolation; (5) compare the strongest exact hypotheses with Bailey–Crandall's conditional map and seek an independent mathematical referee. Do not claim source rigidity without a countermodel-resistant π-specific inequality. Do not merge into `main` before review and required gates.

## 9. Categorical reconstruction: path space is not the circle (POL-09)

There is a clean formal answer to *"the circle exists before we place ticks"*. For a fixed polygon size `m₀≥3` and base `b≥2`, use the finite polygon phase grids `G_n={j/(m₀bⁿ):0≤j<m₀bⁿ}` with the **prefix** bonding maps `P_n(j)=floor(j/b)`. Their inverse-limit carrier is

`X_P=lim←(G_n,P_n) ≅ {0,...,m₀−1} × {0,...,b−1}^ℕ`, a compact, totally disconnected path space. The bijection uses the exact recurrence `j_(n+1)=b j_n+d_(n+1)` for the digit appended at level `n+1`. **This path space is not topologically the circle.** An explicitly defined, continuous, surjective quotient map recovers the circle:

`e((j_n)) = lim_(n→∞) j_n/(m₀ bⁿ) mod 1`.

Indeed its nested cell `[j_n/(m₀ bⁿ),(j_n+1)/(m₀ bⁿ)]` has width tending to zero; its points converge to a unique real in `[0,1]`, whose endpoints are identified modulo one. Usually `e` is one-to-one, but a base-grid endpoint has two symbolic expansions: with `m₀=4,b=2`, `initial j₀=1, 000…` and `initial j₀=0,111…` both converge to phase `1/4` (approaching from opposite sides). The phase `0` on the circle similarly identifies the real endpoints `0` and `1`. Since `{π}` is irrational, its canonical prefix lift under `e` is unique.

The uniform measure on each `G_n` is exactly compatible under `P_n`. Hence independent, uniformly chosen `j₀` and refinement digits determine a consistent product probability `μ_P` on `X_P`, and `e_* μ_P=λ`, the uniform angular measure: every level-`n` cylinder has mass *exactly* `1/(m₀ bⁿ)`, equal to the arclength of its image interval. This equality reconstructs **Haar as a pushed-forward ensemble measure**; it does not say that *every single path* is generic for it. The path `0∞` and the irrational sparse-squares path are perfectly lawful measure-zero exceptions.

**Theorem status:** elementary product topology/measure and nested intervals, **CLASSICAL / PROVED PAPER / EXACT FINITE TESTED**. **Crucial boundary:** one must not switch to the other balanced bonding system `R=T_b` and assume that the same compatible source path or quotient has been transported; its path semantics are different. The source-specific path selected by π is a **point** of `X_P`. Showing that its *forward base-b orbit* equidistributes remains the π-normality problem.

**Executable calibration:** `polygon_prefix_path()` and `polygon_cylinder()`; the unit tests check exact nested cells, uniform finite cylinder weights, and the explicit double-code endpoint witness. This is a lawful categorical carrier-to-circle quotient, not a novel proof of π normality or a physical continuity theorem.
