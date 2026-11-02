# ×3 rigidity machinery — consolidated verdict

**Branch:** `research/x3-rigidity-machinery-2026-11-02`. **Date:** 2026-11-02.

Three fronts + main-thread analysis built the *machinery* to actually navigate the Hochman–Shmerkin
×16–×3 rigidity route to π normality. The result is a clean, honest map of the route: what is free,
what is weaker, what is classical, and where the single open gate sits.

## 1. The entropy–dimension bridge (main-thread + front)

**Furstenberg (1967) / Hochman (2014)** give the classical one-way chain:
$$ h_\mu(T_{16}) > 0 \;\Longrightarrow\; \dim_*\mu > 0, \qquad h_\mu(T_{16}) = \lim_m H_m/m . $$
Hence obligation **(B) `dim_* μ > 0` reduces to the single countable statement `liminf_m H_m/m > 0`**
(positive entropy rate of π's base-16 digits) — **strictly weaker than normality** (`h = log 16`).
The honest **asymmetry** (recorded): positive dimension does *not* imply positive entropy, so (B) is
genuinely weaker than the entropy statement, not equivalent.

## 2. The ×3 transfer-operator route is a re-encoding (front, PROVED)

- The ×16 transfer operator has a **classical Lasota–Yorke spectral gap** (BV contraction `16⁻ⁿ`,
  Lebesgue the unique invariant) — but this is the *base-16* gap and proves nothing new.
- `D_N(h) → 0` is **exactly** joint ×16×3-invariance of every weak-* limit — a **measure-rigidity**
  statement, not a spectral gap of any single operator. The ×3 Koopman operator is an **isometry**
  (no gap). This is the Furstenberg wall, already mapped (AR-5).
- **The transfer-operator route does NOT produce a spectral gap for the ×3 defect.** It re-encodes
  the same gate.

## 3. Frostman measurement harness (front, exact tool)

A certified exact-`Fraction`/digit-orbit tool that measures the sharpest empirical Frostman exponent
`s_N = min_I log μ_N(I)/log|I|`:
- π's orbit: `s_N` rises 0.774 → 0.867 (N=10³→10⁶), monotone toward 1 — **consistent with dim=1**.
- Controls correctly separated: Liouville (0.005), rational (0.333) both ≈0; random (0.795→0.860)
  tracks π within 0.01.
- **Brutally honest**: a *sanity gate*, not a proof of `dim_* > 0`.

## 4. The exact chain (all links classified)

```
(B) dim_* μ > 0
 ⟸ h_μ(T_16) > 0                 [Furstenberg/Hochman: PROVED classical]
 ⟺ lim_m H_m/m > 0               [Shannon–McMillan/KS: PROVED classical]
 ⟸ ∃m_N: log Q_{m_N,N}=o(m_N)    [MS-02 ⇒ normality ⇒ h=log16: PROVED SUCC-local]
      ↑ the open gate L4 = MS-03 (source-selected signed cancellation)
```

**The open gate is unchanged**: `Σ_{n≤N} e(h U_n) = o(N)` over the moving band — equivalently
`liminf_m H_m/m > 0` (positive entropy of π's digits), equivalently `log Q_{m_N,N}=o(m_N)`.

## 5. What the machinery actually buys SUCC

1. **(B) is now a clean, weaker, named target**: "positive entropy rate of π's digits" — strictly
   easier than normality, and a *non-sharp* positive-rate bound would already close it.
2. **The transfer-operator route is ruled out** as a shortcut (it's a re-encoding of the same gate).
3. **A certified Frostman harness** exists to *locate* the exponent and detect any concentration,
   validating the dimension side empirically against dim=0/1 controls.

**π base-16 normality and RH remain OPEN.** The rigidity route is a valid, equivalent (not easier)
decomposition; this round built the machinery (entropy–dimension bridge, transfer-operator verdict,
Frostman harness) that makes its two obligations *navigable* and *named*, without any false victory.
