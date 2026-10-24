# π Moonwalk — Report B: the sparse cyclotomic time-lag inequality (CYC-01)

**Honest headline.** This round produced a *proven* sharpened conditional-normality
inequality (CYC-01′) and an exhaustive calibrated validation of the plan's candidate form
(CYC-01), together with a decisive clarification of **where** the π problem actually lives.
It did **not** produce a π-source-specific theorem or a decisive obstruction. **π normality
in every base (16, 2, 10, absolute) remains OPEN.** RH remains OPEN. No Weil positivity is
claimed anywhere. Per the plan's own warning, a conditional criterion is not progress on the
missing source-specific cancellation; this report does not count it as such.

Carrier conventions: base `b≥2`, point `x∈[0,1)`, orbit `x_j=frac(b^j x)`, `e(t)=exp(2πi t)`.
`A_{h,N}(x)=(1/N)Σ_{j<N} e(h b^j x)`, `c_n(N)=Re A_{n,N}`, `η_N=max(0,2c_1(N))`,
`d_1=0`, `d_n=min_{p genuine prime|n}[d_{n/p}+|c_n−c_{n/p}|]`, `n_d=|h|(b^d−1)=|h|∏_{e|d}Φ_e(b)`.

## 1. CYC-01′ — proven (Demonstrated)

**Theorem (CYC-01′).** For every integer `b≥2`, every `x∈[0,1)`, every nonzero integer `h`,
every integer `R≥2` and every `N≥1`,
```
|A_{h,N}(x)|^2 ≤ (1 + (R-1)/N)·[ 1/R + (R-1)/(2R)·η_N + (2/R^2)·Σ_{d=1}^{R-1}(R-d)·d_{n_d}(N) ]
               + (N+R-1)(R^2-1)/(3 R N^2).
```
**Proof (three exact steps).**
1. *Exact van der Corput.* With `a_k=e(h b^k x)` (0≤k<N, else 0) and `β_j=Σ_{r=0}^{R-1}a_{j+r}`
   over `j=-(R-1),…,N-1`, every `a_k` occurs exactly `R` times, so `Σ_jβ_j=R·S` **exactly**
   (`S=Σa_k=N·A`). Cauchy–Schwarz over the `N+R-1` indices gives
   `R^2|S|^2 ≤ (N+R-1)[RN + 2Σ_{d=1}^{R-1}(R-d)Re C_d]`, `C_d=Σ_m a_m \bar a_{m+d}`.
2. *Cyclotomic autocorrelation.* `Re C_d = Σ_{m=0}^{N-1-d} cos(2π n_d b^m x)`, so
   `Re C_d ≤ N c_{n_d}(N) + d` (the ≤d dropped terms are cosines in [−1,1]). The lag-`d`
   correlation *is* the Weyl cosine sum at the cyclotomic frequency `n_d`.
3. *Prime-word telescoping.* `c_{n_d} ≤ c_1 + d_{n_d}` (triangle inequality on the min-cost
   prime-divisor path), and `2c_1 ≤ η_N`. With `Σ(R-d)=R(R-1)/2` and `Σ(R-d)d=R(R-1)(R+1)/6`
   (both verified symbolically), assembling and dividing by `R^2N^2` gives the statement. ∎

*Checked:* holds with margin on x=0 and on the tightest observed cell (x=1/2,b=2,h=2,R=2,
N=65536, margin ≈ 2.3e-5); correctly *false* on an incoherent synthetic triple
(|A|²,c₁,S not from any orbit) — i.e. the bound has content.

Classical content: van der Corput differencing and `b^d−1=∏Φ_e(b)` are classical. **New to
SUCC:** the assembly tying the lag-`d` correlation to the *prime-word telescoping cost*
`d_{n_d}` of the cyclotomic frequency. No academic-novelty claim.

## 2. CYC-01 (the plan's exact candidate form) — Observed, exhaustively

`|A| ≤ (R-1)/N + sqrt( 1/R + (R-1)/(2R)η_N + (2/R^2)Σ(R-d)d_{n_d} + 2(R-1)(R-2)/(3RN) )`.

Same three principal terms as CYC-01′ (Demonstrated); the boundary is regrouped (additive
`(R-1)/N` outside, inner `2(R-1)(R-2)/(3RN)`). Verified numerically by an independently-built,
**calibrated** instrument (Daniel), cross-checked by a second instrument sharing no code
(agreement ≤7e-20):

- **GAP = RHS−|A| ≥ 0 in >1.3M cells, 0 negatives:** 432,446 main-sweep (random + deterministic,
  N up to 16384/262144), 22,176 periodic, 852,040 rationals (all reduced p/q, q≤100, b∈{2,16},
  7 h, 5 R), plus adversarial annealing.
- **Global min GAP = 1/65536 exactly**, at a saturated cell (|A|=1, radicand=1 exactly), where
  GAP equals the leading `(R-1)/N` term. **The R=2 corner** (where the inner term vanishes) was
  specifically hammered: min non-saturated GAP there ≈ 0.0359 via annealing — still positive,
  because the outer `(R-1)/N` term compensates for the vanishing inner term.
- **Load-bearing:** dropping T1/T2/T3 yields 13462/2244/3295 violations respectively; the
  instrument can see a false bound. T4 and the leading term have slack in the sample (consistent
  with the plan's inner constant being ~2× the provable minimum of CYC-01′).
- Calibration: 17/17 checks pass; `d_n` matches brute-force prime-ordering; x=0, x=1/2, and
  periodic rationals match exact closed forms; π hex digits verified; an `np.cumsum` long-double
  rounding bug was caught and fixed before any data were trusted.

**Status:** CYC-01 (plan's exact constants) is **Observed** (overwhelming calibrated numerical
evidence, two instruments), with its spine **Demonstrated** via CYC-01′. A line-by-line proof
that the plan's exact grouping dominates CYC-01′ is a finite elementary inequality, not written
out here. Sampling is not proof; `h,R` beyond the grid, `b∉{2,16}`, and `N` between grid points
are untested.

## 3. π-specific vs generic — the decisive clarification (CYC-04)

CYC-01 holds for **every** x: it is a **generic conditional criterion**, not π-progress.
The numerics pin exactly how:

- **Non-normal periodic sources behave correctly.** x=1/3 (b=16 fixed point, |A|=1): RHS stays
  **bounded away from 0** at every R up to 12, even at N=10¹² (RHS ≈ 1.118 at R=2 → 1.208 at
  R=12; GAP ≈ 0.118–0.208). The bound **correctly refuses to prove normality** for a non-normal
  source — it is sound and non-vacuous. x=1/101 (b=2, period 100): at small R the bound does not
  see the long period (T3 ≈ 1e-52), RHS = R^(−1/2); detecting the period needs R ≳ period.
- **π empirically shrinks but the bound floors at R^(−1/2).** |A_{1,N}(π)|: 0.241 (N=16) →
  3.6e-4 (N=262144). At **fixed** R, RHS decreases monotonically to the hard floor **R^(−1/2)**
  (T1=1/R). With R growing like ⌈log₁₆N⌉, RHS keeps shrinking slowly (0.61 at N=1024 → 0.45 at
  N=262144), tracking R^(−1/2). **Consequence:** no single R can prove normality; one needs
  R=R_N→∞ **and** the carry-sum term controlled.

So the mechanism does not manufacture π cancellation; it transports the fundamental correlation
up the cyclotomic ladder. The open content is entirely in the carry-sum term for x=π.

## 4. The next smallest theorem that would change the verdict (OPEN)

**CYC-03 (open).** Prove that for x=π, base b=16, every fixed nonzero h, with a lag window
`R_N→∞` admissibly slow (e.g. `R_N < (1−δ)log₁₆N`, fixed δ>0),
```
(2/R_N^2) · Σ_{d=1}^{R_N-1} (R_N - d) · d_{|h|(16^d-1)}(N; π)  →  0   as N→∞,
```
together with `η_N→0` (controlled chord calibration). By CYC-01 this forces `|A_{h,N}(π)|→0`
for every fixed h — i.e. **hexadecimal normality of π, hence binary normality.** This
convergence is presently **OPEN**; it must come from π's authenticated source (nested-circle /
Wallis–Kummer / BBP), **not** from genericity. Daniel's π data is consistent with it but is not
proof.

**Lanes not attempted this round (OPEN):** CYC-02 (source-transfer error budget for the sparse
cyclotomic set, R_N growth), the BBP four-pole dynamical lane (BBP-01..05), and the
chord-moment / Hankel lane. Each remains a separate research target; none was advanced here.

## Reproducibility
Instruments (two independent): `research/2026-10-23/cyc01_instrument.py` (A),
`research/2026-10-23/cyc01_xcheck.py` (B), calibration `research/2026-10-23/cyc01_calibrate.py`.
The full per-row CSVs (>1.3M rows) are regenerable from these; they are not committed for size.
Precision: mpmath + 80-bit long double, cross-checked at dps 50/60/80/90/100.

## 5. Firewall
RH, π normality (all bases), abc, and signed-Weil positivity are **OPEN**. No positive
chord/Hilbert overlap is presented as Weil positivity. SUCC remains a Σ₁ verifier, not a Π₂
prover. RH_PROVED: NO.
