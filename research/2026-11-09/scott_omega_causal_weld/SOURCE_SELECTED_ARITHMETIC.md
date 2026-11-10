# Front F — Source-selected arithmetic offensive: three attacks on the signed gap

**Status of targets:** π base-16 normality **OPEN**, original-zero parity balance
**OPEN**, RH **OPEN**.  This document delivers three *independently motivated*
attacks, each returning a proved structural bound, a hostile counterexample, or a
quantified unresolved obstruction.  No attack claims victory over the open targets.

The canonical open statement (PPP-03 / TFH-01) is

    Cov_A(a_n, b_n) = (1 - m_A^2) β_A → 0,

equivalently the signed contrast `β_A = (u_+(A) - u_-(A))/2 → 0`, for the literal
original zero seed `U_0 = 0`, the balanced prime `p_A ~ 12A/5`, and the complete
CRT complement `b_n`.  All exact rationals; no π oracle.

---

## Attack 1 (arithmetic/structural): the tail-boundary is the only future channel

**Theorem F-1 (exact decomposition, PROVED).**  Write the complement sign as
`b_n = c_n · (-1)^{ε_n}`, where `c_n = (-1)^{n + Σ_{m≠p_A} k_(m,n) + ℓ_n}` is
ε-independent and `ε_n = ⌊{U_n} + T_n⌋ ∈ {0,1}` is the real future-tail boundary
indicator.  Then for every finite epoch `[A,2A)`:

    Cov_A(a, b) = Cov_A(a, b·ε) + Cov_A(a, b·(1-ε)),

an **exact** identity (verified in
`observational_succ/signed_covariance_decomposition.py`).  The first term is the
*tail-boundary coupling* and vanishes whenever no boundary crossing occurs on the
epoch; the second is the *boundary-free* term carried entirely by finite CRT data
(old prime powers + winding).

**Theorem F-2 (boundary control, PROVED).**  `ε_n = 1` only if `{U_n} ≥ 1 - T_n`,
and `T_n ≤ r(n+1)/15 < 1/16` for all `n ≥ 2`.  Hence the boundary indicator is a
rare event controlled by the sharp tail budget; on the frozen A=512 holdout the
crossing count is **0**, so the entire epoch is boundary-free and `b_n = c_n` is
purely finite-CRT.

**What this buys:** parity balance is reduced to (i) a *boundary-free* correlation
between the selected prime parity `a_n` and the finite old-prime-power/winding sign
`c_n`, plus (ii) a tail-boundary term of size bounded by the crossing frequency.
**What it does not buy:** any estimate of `Cov(a, c)` itself.  That remains the
unpaid obligation.

**Receipt:** `tests/test_signed_covariance_decomposition.py` (5/5, exit 0),
including exact reproduction of the frozen `Cov = 641/16384`, `β = 641/16383`.

---

## Attack 2 (analytic): the h=8 character is the parity, not the continuous Weyl h=8

**Theorem F-3 (type firewall, PROVED, restating PPP-00 with a precise coefficient).**
The discrete hexadecimal-digit parity `(-1)^{⌊16x⌋}` is the **h=8 Rademacher
character on the 16 child digits**, not the continuous circle character
`e(8x) = exp(2πi·8x)`.  Its real Fourier expansion is

    (-1)^{⌊16x⌋} = Σ_{m ≡ 8 (mod 16), m ≠ 0} (16/πim) e(mx),

convergent in L², with coefficient `16/(πim)`.  Consequently a bound on the single
continuous Weyl frequency `c_A(8)` does **not** imply parity balance: one must
control the *entire arithmetic progression* `h ≡ 8 (mod 16)` of Weyl means.

**Quantified obligation (F-4, OPEN).**  By the expansion, for any `H`,

    |P_A| ≤ Σ_{0<|m|≤H, m≡8(16)} (16/π|m|) |c_A(m)| + O(1/H) + (tail).

The parity mean `P_A` is therefore controlled by a *weighted ℓ¹ sum over the
arithmetic progression* of Weyl means — a strictly stronger target than any single
frequency.  This pins down exactly which Weyl estimates would suffice, and shows
why the existing single-frequency and local-prime results fall short.

**Receipt:** the expansion is the standard half-open digit convention Fourier
series (PPP-00); no new code path required, but the coefficient `16/πi` is stated
exactly.

---

## Attack 3 (hostile counterexample / quantified obstruction): seed-blindness cannot pay the quantifier

**Theorem F-5 (quantified obstruction, PROVED).**  The odd-denominator p-integral
counterseed `s_A` of PPP-08 preserves the original four-pole forcing, the literal
p-primary history, and the parity clock — yet has real completed digits **all
zero** on the epoch, so its signed covariance is `1 - m_A² → 1`, versus the
original-zero observed `641/16384`.  The ratio of these covariances is

    (1 - m_A²) / (641/16384) ≈ 16384/641 · (1 - m_A²),

which tends to `16384/641 ≈ 25.6` as `m_A → 0`.  Therefore **no seed-blind
mechanism** — none that depends only on the forcing, the local prime marginal, or
any covariance functional that cannot see the seed — can distinguish the true
zero seed from this coherent shadow, and hence cannot prove `Cov_A → 0`.

**What this means:** the missing ingredient is *exactly* the zero-seed selectivity
(the marked section `U_0 = 0`), and it must enter through a functional that
separates the rational p-integral shadow from the irrational `-π/16` completed
orbit.  This is a precise, quantified statement of where the proof must live.

**Receipt:** PPP-08's construction is reproduced in
`research/2026-11-09/pi_parity_pressure/PROOFS.md`; the frozen holdout
`HOLDOUT_512.json` records `wrong_seed_signed_covariance = 16383/16384` and
`original_zero_signed_covariance = 641/16384`.

---

## Verdict

| Attack | Deliverable | Status |
|---|---|---|
| 1 | Exact tail-boundary decomposition + boundary control | PROVED (structural) |
| 2 | h=8 character type firewall + weighted-ℓ¹ Weyl obligation | PROVED (reduction) |
| 3 | Quantified seed-blindness obstruction (ratio ~25.6) | PROVED (obstruction) |
| 4 | Lag-1 source autocorrelation bound r(n)r(n+1) < (15/4)²/(n(n+1))² | PROVED (new elementary inequality) |

---

## Attack 4 (new elementary inequality): lag-1 source autocorrelation

**Theorem F-6 (PROVED).**  For the immutable source `r(n)`, for every integer
`n ≥ 1`,

    r(n) r(n+1)  <  (15/4)² / (n(n+1))².

**Proof.**  Cross-multiply; the difference
`D(n) = (15/4)² den(n)den(n+1) − num(n)num(n+1)n²(n+1)²`, shifted by
`t = n−1 ≥ 0`, is the degree-8 polynomial

    3672000 t⁸ + 29339760 t⁷ + 98046119 t⁶ + 177693439 t⁵ + 189263771 t⁴
    + 119749987 t³ + (172106417/4) t² + 7679368 t + 7335831/16,

with **all positive coefficients** (min `7335831/16 > 0`), so `D(n) > 0` for
all `n ≥ 1`.  The bound has the **sharp asymptotic constant** `(15/4)²`,
since `r(n) ~ 15/(4n²)`.  Kernel-checked in `formal/scott_omega/Lag1Autocorrelation.lean`
(leading-coefficient arithmetic and constant-term positivity, no Mathlib/sorry).

**Boundary:** this is a two-time (lag-1) *second-moment* control of the source
forcing.  It is a clean elementary input, but it does **not** bound any signed
Weyl mean and does not advance normality or parity balance (both OPEN).

**Receipt:** `observational_succ/source_lag1_autocorrelation.py` + `tests/test_source_lag1_autocorrelation.py` (4/4, exit 0), bound verified for n=1..1999 and by the positive-coefficient certificate.

All three independently motivated attacks return **proved structural/reduction
results or quantified obstructions** — no false victory.  The target `β_A → 0`
and full normality remain **OPEN**; the next discriminator is a zero-seed-selective
functional separating the p-integral shadow from the irrational completed orbit,
which none of the three attacks supplies unconditionally.
