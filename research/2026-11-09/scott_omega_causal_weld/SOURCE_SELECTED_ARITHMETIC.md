# Front F — Source-selected arithmetic offensive: three attacks on the signed gap

**Audit correction (Cayley follow-up, 2026-11-09):** the corrected statements below supersede the parent draft at `afabc458323ef2e3a20ce2bae77239c4190819c5`. F-1 needs a genuine finite-complement split; F-2 does not prove rare crossings. F-4/F-11 require paid boundary reconstruction. F-6/F-7 are nonsharp upper inequalities, with true lag constant 225/4096. F-9 universal necessity is withdrawn. F-10's integration sign is corrected. See [errata](../cayley_source_observer/ERRATA.md), [covariance audit](../cayley_source_observer/SIGNED_COVARIANCE_AUDIT.md), and [boundary proofs](../cayley_source_observer/BOUNDARY_PROOFS.md).

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
epoch; the second still depends on the future mask `1-eps`. To isolate the genuinely
finite CRT sign c, use instead

    Cov_A(a,b) = Cov_A(a,c) + 2 Cov_A(a,b eps).

This follows from `b-c=2b eps`. The absolute correction is at most
`4 E_A[eps]`; its smallness requires an occupation estimate. The repaired
`tail_boundary_coupling` returns this exact covariance difference.

**Theorem F-2 (boundary control, PROVED).**  `ε_n = 1` only if `{U_n} ≥ 1 - T_n`,
and `T_n ≤ r(n+1)/15 < 1/16` for all `n ≥ 2`.  This locates crossings in a narrow strip but does not prove they are rare.
The historical A=512 receipt reports crossing count zero; that finite observation
provides no all-epoch frequency bound. Synthetic repetition of its aggregate
counts with eps=0 is an algebra check, not a fresh source reconstruction.

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
continuous Weyl frequency `c_A(8)` alone does not establish parity balance.
Controlling the supported progression with justified boundary passage is one
sufficient route; it is not necessary to prove each individual mode small
in order to bound the signed combination.

**Corrected obligation (F-4, OPEN arithmetic premise).** For the degree-H
Fejer mean F_H, points y_n and 0<delta<=1/32,

    |mean f(y_n)-mean F_H(y_n)|
      <= 2 * boundary_count(delta)/A + 1/((H+1)*delta).

Finite source and numerical evaluation errors must also be paid. The exact
source-certified version is CBO-B03. The former unqualified O(1/H) bound is
withdrawn: distance to digit cuts cannot be omitted, and the 1/|m| coefficient
sequence is not absolutely summable. Taking absolute values of a finite
weighted spectral sum is a possible upper bound, not a proved arithmetic saving.

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

which tends to `16384/641 ≈ 25.6` as `m_A → 0`. This compares to the fixed
A=512 reference value; it is not an asymptotic ratio to the changing original
source covariance. Therefore **no seed-blind
mechanism** — none that depends only on the forcing, the local prime marginal, or
any covariance functional that cannot see the seed — can distinguish the true
zero seed from this coherent shadow, and hence cannot prove `Cov_A → 0`.

**What this means:** source selection is a necessary missing ingredient for a
seed-uniform argument. A proposed estimate must distinguish the original zero
seed from the relevant coherent wrong seed. It need not distinguish two wrong
seeds from one another. This obstruction does not identify a sufficient analytic
mechanism or prove that source selection is the only remaining difficulty.

**Receipt:** PPP-08's construction is reproduced in
`research/2026-11-09/pi_parity_pressure/PROOFS.md`; the frozen holdout
`HOLDOUT_512.json` records `wrong_seed_signed_covariance = 16383/16384` and
`original_zero_signed_covariance = 641/16384`.

---

## Verdict

| Attack | Deliverable | Status |
|---|---|---|
| 1 | Exact tail-boundary decomposition + boundary control | PROVED (structural) |
| 2 | h=8 type firewall + boundary-paid finite Fejer reconstruction | PROVED (conditional reduction); signed estimate OPEN |
| 3 | Quantified seed-blindness obstruction (ratio ~25.6) | PROVED (obstruction) |
| 4 | Lag-1 source autocorrelation bound r(n)r(n+1) < (15/4)²/(n(n+1))² | PROVED (new elementary inequality) |
| 5 | Uniform lag-k bound r(n)r(n+k) < (15/4)²/(n(n+k))² | PROVED (uniform two-time correlation) |
| 6 | Zero-seed/shadow separation gap: |s_A+π/16| ≤ r(N+1)/(15·16^N)+1/D | PROVED (quantified obstruction) |
| 7 | Parity Fourier support exactly on m ≡ 8 (mod 16), coeff 16/(π i m) | PROVED (exact structural) |
| 8 | Parity mean = Σ_{m≡8(16)} (16/πim)·c_A(m), verified finite reconstruction | PROVED (exact reduction, verified) |

---

## Attack 7 (verified reduction): the parity mean is a single Weyl progression

**Theorem F-11 (corrected fixed-finite-epoch identity).** On the actual
completed irrational source phases, symmetric partial Fourier sums recover
the circle-parity mean for each fixed finite epoch:

    mean f(y_n) = lim_(H->infinity)
      sum_(0<|m|<=H, m=8 mod16) (16/(pi i m)) mean e(m y_n).

This follows from pointwise convergence away from rational digit cuts and
the finite number of samples, not from applying an L2 bound to atomic masses.
The old weighted-l1/uniform O(1/H) tail assertion is withdrawn. Historical
finite floating reconstruction is a diagnostic. The follow-up uses rational
interval evaluation plus an explicit Fejer/boundary/source error budget.

Here `f(y_n)=s_(n+1)` in PPP/TFH notation; comparison with its same-epoch
integer-parity mean pays at most 2/A. No signed decay follows from the identity.

**Receipt:** `observational_succ/parity_fourier_reconstruction.py` +
`tests/test_parity_fourier_reconstruction.py` (3/3, exit 0).

---

## Attack 6 (exact structural): the parity character's Fourier support

**Theorem F-10 (PROVED, sharpening PPP-00).**  The hexadecimal parity character
`f(x) = (−1)^{⌊16x⌋}` on `[0,1)` has Fourier coefficients

    a_m = ∫₀¹ (−1)^{⌊16x⌋} e^{−2πimx} dx = 16/(πim)  if m ≡ 8 (mod 16),
                                          = 0        otherwise.

**Proof.**  Split `[0,1)` into the 16 digit intervals; the coefficient is
`(2πim)^{−1}·(1−z)·Σ_{a=0}^{15}(−1)^a z^a` with `z = e^{−2πim/16}`.  The
alternating geometric sum equals 16 iff `z = −1` iff `m ≡ 8 (mod 16)`, and 0
otherwise.  This is the **exact support**: parity balance is controlled by the
Weyl means `c_A(m)` at the arithmetic progression `m ≡ 8 (mod 16)` **only**,
with the symmetric or boundary-paid summation specified above. At m=0,
the coefficient is zero by equal positive and negative cell lengths.
`formal/scott_omega/ParityFourierSupport.lean` checks only support congruences
and the six residues in 1..96; it does not formalize Fourier integration.

**Boundary:** exact support and coefficient; does not bound the Weyl means, so
normality/parity remain OPEN.

**Receipt:** `observational_succ/parity_fourier_support.py` +
`tests/test_parity_fourier_support.py` (4/4, exit 0).

---

## Attack 5 (quantified obstruction): the exact separation gap and the Diophantine wall

**Theorem F-8 (PROVED).**  Both the zero-seed completed orbit `16^(n−1)π` and the
PPP-08 p-integral shadow orbit `16^n(s_A+π/16)` are **irrational** at every `n`
(the shadow does not rationalise the orbit: `s_A+π/16` is rational + irrational).
The shadow is an *astronomically close* approximation, with exact gap bound

    0 < |s_A + π/16| ≤ r(N+1)/(15·16^N) + 1/D,
    N = 2A+16,  D = p·16^(2A+48)+1,

and the scaled completed-digit gap obeys `16^n|s_A+π/16| < 1/16` on `[A,2A+8)`,
so every completed hexadecimal digit of the shadow vanishes on the epoch.

**F-9 (universal necessity WITHDRAWN).** For a known seed s, the exact
difference from the original zero-seed orbit is `16^n s`. An effective
irrationality measure is not universally necessary to distinguish these
marked source states. For each fixed original completed digit, nested exact
source enclosures plus irrationality guarantee eventual certification.
An a-priori uniform resource rate or a selected all-epoch signed bound is a
different question. Diophantine estimates may help particular quantitative
separation tasks, but their claimed universal necessity was not established.

**Receipt:** `observational_succ/zero_seed_selectivity_gap.py` +
`tests/test_zero_seed_selectivity_gap.py` (4/4, exit 0).  The gap bound is exact
rational algebra; no π oracle is used to compute it (only the classical
irrationality of π is cited).

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
all `n ≥ 1`. This bound is valid but nonsharp: `n²r(n)->15/64` and the
scaled lag-product limit is `225/4096`, not `225/16`. The exact positive
source envelope in the follow-up ERRATA.md proves the corrected asymptotic.
The Lean file checks leading arithmetic and constant-term positivity only;
it does not formalize the full polynomial identity or asymptotic squeeze.

**Boundary:** this is a two-time (lag-1) *second-moment* control of the source
forcing.  It is a clean elementary input, but it does **not** bound any signed
Weyl mean and does not advance normality or parity balance (both OPEN).

**Receipt:** `observational_succ/source_lag1_autocorrelation.py` + `tests/test_source_lag1_autocorrelation.py` (4/4, exit 0), bound verified for n=1..1999 and by the positive-coefficient certificate.

**Theorem F-7 (uniform lag-k generalization, PROVED).**  For all integers
`n ≥ 1` and `k ≥ 1`,

    r(n) r(n+k)  <  (15/4)² / (n(n+k))².

**Proof.**  The difference `D_k(n) = (15/4)² den(n)den(n+k) − num(n)num(n+k)n²(n+k)²`
shifted by `t = n−1 ≥ 0` is a degree-8 polynomial in `t` whose **coefficients are
polynomials in `k` with all-positive integer coefficients** (the nine t-coefficients
are listed in `source_lag1_autocorrelation.lagk_polynomial_coefficients()`).  Since
`k ≥ 1`, every coefficient is positive, so `D_k(n) > 0` for all `n,k ≥ 1`.  This is
a valid nonsharp product bound for the forcing. Its true scaled leading
constant is `225/4096`, uniformly for integer k>=1 as n tends to infinity.  Verified on the full `n,k ∈ 1..299` grid (89,401
checks) and by the all-positive coefficient certificate (6/6 tests).

**Boundary:** a clean two-time *second-moment* control, not a signed Weyl-mean
estimate.  Normality and parity balance remain OPEN.

The corrected structural identities and hostile controls survive within their
stated scopes. The target beta_A->0 and full normality remain OPEN. No attack
here supplies the source-selected signed estimate; the finite covariance
repairs and boundary certificates make that missing premise explicit.
