# Front 4 — Gamma-sheet positivity: quantitative Archimedean gap or provable orthogonality?

**Branch:** `research/army-sub-log-collision-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (subagent, Front 4). **Scope:** the single open gate
`C_A = (1/A) Σ_i v_i(A)^2 = o(log A)` for the ORIGINAL four-pole BBP source, attacked via
the maintainer's LS-01…LS-09 line→sheet positive-kernel machinery.
**No π-normality or RH claim.** Complete derivations; every quantitative statement is checked
by `verify_gamma_archimedean.py` (exact `Fraction` + `mpmath` at dps≥50).

---

## 0. Objects (verbatim from maintainer LS-01…LS-09, unmodified)

- `r(n) = 4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)`, `U_0 = 0`, `U_{n+1} = 16 U_n + r(n+1)`.
- `P(x) = (1−x)(x²+2)(x²+2x+2) = 4 − 2x³ − x⁴ − x⁵`.
- Digamma defect `D(s) = ψ(s+1) − log s = ∫₀^∞ e^{−st} κ(t) dt`, `κ(t) = 1/t − 1/(e^t−1) > 0`.
- Green tail `T_n = Σ_{k≥1} 16^{−k} r(n+k)`, with `U_n = 16^{n−1}π − T_n`, `0 < T_n < (8n+1)^{−2}`.
- Continuum continuation `T(s) = ∫₀¹ x^{8s} P(x)/(16−x⁸) dx = ∫₀^∞ e^{−st} Q_BBP(t) dt`,
  `Q_BBP(t) = e^{−t/8} P(e^{−t/8}) / (8(16−e^{−t}))`.
- Sheet kernel `Q_sheet(t) = (1/16) ∫₀^t κ(u)κ(t−u) du`, `D(s)²/16 = ∫₀^∞ e^{−st} Q_sheet(t) dt`.
- **LS-04 (PROVED):** `0 < Q_BBP(t) < Q_sheet(t)` for every `t>0`.
- **LS-07/08 (PROVED):** `W(s) := D(s)²/16 − T(s) > 0` for every real `s>0`, and `W` is
  STRICTLY COMPLETELY MONOTONE: `(−1)^m W^{(m)}(s) > 0` for all `m≥0, s>0`.
- **LS-09 (PROVED):** `lim_{s→∞} s³ W(s) = 13/1536`.

---

## 1. THE EXACT RELATIONSHIP — T(s)/W(s) and the discrete tail T_n

### Lemma 1.1 (continuation hits the tail exactly).  `T(n) = T_n` for every integer n≥1.

*Proof (complete).* Expand the geometric denominator and integrate term-by-term (the series
converges absolutely for `0<x<1`, so termwise integration is justified):

```
T(s) = ∫₀¹ x^{8s} P(x) / (16 − x⁸) dx
     = Σ_{k≥0} 16^{−(k+1)} ∫₀¹ x^{8s+8k} P(x) dx.
```

With `P(x) = 4 − 2x³ − x⁴ − x⁵`, the moment is
`∫₀¹ x^{8s+8k} P(x) dx = 4/(8s+8k+1) − 2/(8s+8k+4) − 1/(8s+8k+5) − 1/(8s+8k+6)`.
Substitute `s = n` and observe `4/(8n+8k+1) − 2/(8n+8k+4) − 1/(8n+8k+5) − 1/(8n+8k+6)
= r(n+k+1)` (since `r(m) = 4/(8m−7) − 2/(8m−4) − 1/(8m−3) − 1/(8m−2)` and `8(n+k+1)−7 = 8n+8k+1`).
Hence

```
T(n) = Σ_{k≥0} 16^{−(k+1)} r(n+k+1) = Σ_{j≥1} 16^{−j} r(n+j) = T_n.   ∎
```

**Consequence (the linchpin).** The completely-monotone defect `W` samples the tail exactly at
integers:

```
W(n) = D(n)²/16 − T_n = (H_n − log n − γ)²/16 − T_n > 0,   (all n≥1)
```

where the second equality uses `D(n) = ψ(n+1) − log n = H_n − log n − γ` (classical; DLMF
§5.9.13 + `ψ(n+1) = H_n − γ`). So **Gamma-sheet positivity, at the discrete level, is exactly
the statement `T_n < (H_n − log n − γ)²/16`.**

### Lemma 1.2 (the bound is *tight*, matching the known tail at leading order).

Euler–Maclaurin gives `D(n) = 1/(2n) − 1/(12n²) + 1/(120n⁴) + O(n⁻⁶)`, hence

```
D(n)²/16 = 1/(64n²) − 1/(192n³) + O(n⁻⁴).
```

The tail's own asymptotic series (independently PROVED in the campaign) is
`T_n = 1/(64n²) − 7/(512n³) + O(n⁻⁴)`. Therefore

```
W(n) = D(n)²/16 − T_n = 13/(1536 n³) + O(n⁻⁴),   (sharp: 7/512 > 1/192, so the gap is +)
```

which reproduces LS-09 at the discrete level (`n³ W(n) → 13/1536`). Both `D(n)²/16` and `T_n`
share the leading term `1/(64n²)`; the positivity of `W` is carried entirely by the cubic
difference `13/1536` — the SAME quantity as the maintainer's leading continuum gap
`Q_sheet − Q_BBP = 13t²/3072 − 479t³/221184 + O(t⁴)`.

---

## 2. DOES THE POSITIVE KERNEL GAP GIVE A "MASS LOWER BOUND" ON T_n?

**Answer: NO. It gives a (tight) UPPER bound, and it is not a lower bound of any kind.**

`W(s) = D(s)²/16 − T(s) > 0` is equivalent to `T(s) < D(s)²/16`, an **upper** bound on `T`,
hence (via Lemma 1.1) on `T_n`. The "mass" (the value of `T_n`, or its total `B = Σ_n T_n`) is
bounded from *above*, never from *below* beyond the trivial `T_n > 0` (which comes from
`Q_BBP > 0`, not from the gap). A "mass lower bound" of the form `T_n > c/n²` with a positive
`c` would be a *different* assertion that the Gamma sheet does **not** produce — and the actual
tail is fully known (it *is* `≈ 1/(64n²)`, matching the upper bound at leading order), so the
upper bound is a true but already-known fact, strictly implied by the sharper exact asymptotic
series and by `T_n < (8n+1)^{−2}`.

---

## 3. THE ARCHIMEDEAN NEUTRALITY THEOREM (the honest answer)

**Verdict: the Gamma-sheet positivity is PROVABLY ORTHOGONAL to `C_A = o(log A)`. It carries
no Archimedean (real-spacing) control.** This is proved in four exact steps.

### Step A — the tail is π-free; the defect lives entirely in the tail.

`T_n = Σ_{k≥1} 16^{−k} r(n+k)` is a **deterministic function of the rational pole structure
`r(·)` alone**. It does not contain π. `D(s)` is universal (digamma). Therefore
`W(s) = D(s)²/16 − T(s)` is a functional of the *tail sequence* only. The state decomposes as

```
U_n = 16^{n−1}π − T_n  ⟹  {U_n} = {16^{n−1}π − T_n}.
```

The collision count `C_A` depends on the fractional parts `{U_n}`, which split into a **π-term
`{16^{n−1}π}`** and a **tail term `T_n`**. The Gamma sheet constrains only the tail term.

### Step B — the tail is sub-bin, hence a second-order (non-spacing) correction.

For `n ∈ [A, 2A)` (the epoch), `0 < T_n < (8n+1)^{−2} ≤ (8A+1)^{−2} < 1/(64A²)`. The bin width
is `1/A`, so the shift is

```
A · T_n < A/(64A²) = 1/(64A) ≪ 1  ⟹  the tail moves floor(A{U_n}) by at most 1,
and only for points within 1/(64A²) of a bin boundary.
```

Concretely, `A·T_A ≈ 1/(64A)` (verified: `9.3e−4, 2.4e−4, 6.1e−5, 1.5e−5, 3.8e−6` at
`A = 16, 64, 256, 1024, 4096`). The tail is at scale `O(1/A²)` while collisions are resolved
at scale `1/A`: **the tail is one full order below the collision resolution**, so it cannot
*create* a spacing (lower) bound; it is a sub-leading deterministic shift.

### Step C — `W(s) > 0` imposes nothing on the π-term, which is the only non-deterministic ingredient.

By Step A, `W(s) > 0 ⟺ T_n < (H_n − log n − γ)²/16`, a condition on `{T_n}` **alone**, already
true (and already strictly implied by sharper known bounds — Lemma 1.2). It says **nothing**
about `{16^{n−1}π}`, which is the base-16 digit sequence of π — precisely the object whose
equidistribution `C_A = o(log A)` would certify. A bound that is silent on the only unknown
input cannot bound the output.

### Step D — explicit witnesses (two directions of orthogonality).

**D1 (not sufficient — maintainer's own counterseed).** Fix the SAME four poles but replace the
seed by the real counterseed `U'_0 = 1/5 − π/16` (equivalently `β = 1/5`). Then the continuation
`T(s)`, the kernels `Q_BBP, Q_sheet`, and hence `W(s)` are **unchanged** (they are functionals of
the poles/`r(·)`, not of the seed). But `U'_n = 16^{n−1}(1/5) − T_n`, whose fractional part is
`{U'_n} = {16^{n−1}/5 − T_n}`; since `16^{n−1} ≡ 1 (mod 5)` for `n≥1`, `{16^{n−1}/5} = 1/5`
is **constant**, so all `U'_n` cluster at `{1/5 − T_n} → 1/5`, giving `C_A ≍ A` (maximal
collision). Hence `W(s) > 0` with `C_A ≍ A` is possible: **Gamma positivity does NOT imply
`C_A = o(log A)`.**

**D2 (not necessary — altered normal sequence).** Begin with a known base-16 normal sequence and
zero out digits in disjoint blocks at `A_j = 2^{j²}` of length `⌊A_j^{3/4}⌋`. Normality is
unchanged (zero-density modification), yet `C_{A_j} ≫ A_j^{1/2}`, so `C_A = o(log A)` fails
(LS-03 "sharp firewall"). This sequence is not the BBP source, but it shows the collision gate
is an *extra* arithmetic regularity condition, not a shadow of the (always-true) Gamma sheet.

**Conclusion of Step D.** `W(s) > 0` holds identically for the original source, for the
counterseed (which has `C_A ≍ A`), and is consistent with both `C_A = o(log A)` and its
failure. It neither implies nor is implied by the gate. **Orthogonality is proved.**

---

## 4. WHAT IS PROVED (claim ledger)

| # | Claim | Status | Evidence |
|---|-------|--------|----------|
| G1 | `T(n) = T_n` (continuation hits the tail at integers) | **PROVED** | Lemma 1.1 (termwise-integral identity); `verify` §1 |
| G2 | `W(n) = (H_n−log n−γ)²/16 − T_n > 0`, i.e. discrete = `T_n < D(n)²/16` | **PROVED** (from LS-07/08 + G1) | Lemma 1.1 |
| G3 | `W(n) = 13/(1536n³) + O(n⁻⁴)`, matching LS-09 | **PROVED** | Lemma 1.2; `verify` §2 ratio→1 |
| G4 | The positive gap is an UPPER bound on `T_n`, never a lower bound | **PROVED** | §2 (sign analysis) |
| G5 | Tail is sub-bin: `A·T_n < 1/(64A) ≪ 1` on `[A,2A)` | **PROVED** | Step B; `verify` §4 |
| G6 | `W(s)` is a functional of the π-free tail only | **PROVED** | Step A (definitional) |
| G7 | **Gamma-sheet positivity is ORTHOGONAL to `C_A = o(log A)`** | **PROVED** (orthogonality, both directions) | Steps A–D; `verify` §5 (counterseed) |
| — | `C_A = o(log A)` for the original source | **OPEN** (unchanged) | — |
| — | π base-16 normality, RH | **OPEN** | — |

**Boundary / what is NOT established.** Nothing here bounds `C_A` for the original source; the
Gamma sheet is shown to be *irrelevant* to the gate, not to solve it. The sub-bin claim (Step B)
bounds the *shift* magnitude, not the number of near-boundary π-points (which is itself
collision-type). No all-A statement about `{16^{n−1}π}` is made. The counterseed (D1) uses a seed
the original program forbids (the "one bit" anchor `β = π ⟺ U_0 = 0`); it is cited only to prove
non-sufficiency, exactly as the maintainer intended.

## 5. Answer to the three specific questions

1. **Exact relationship T(s)/W(s) ↔ T_n.** `T(s)` is the real continuation with `T(n) = T_n`
   (Lemma 1.1). `W(s)` is completely monotone and samples to `W(n) = (H_n−log n−γ)²/16 − T_n`,
   a tight upper bound on the tail with sharp cubic gap `13/(1536n³)`.
2. **Mass lower bound on T_n?** No. The positivity gives an upper bound (tight but already
   strictly implied by sharper known asymptotics), never a lower bound; it is non-vacuous only
   as a correct but non-informative upper bound on the fully-known tail.
3. **Archimedean control or orthogonality?** **Provably orthogonal.** The defect constrains the
   deterministic π-free tail at scale `O(1/A²)`, one order below the `1/A` collision resolution,
   and is silent on the only unknown (the base-16 digits of π). Explicit witnesses (counterseed
   with `C_A ≍ A`, altered-normal with `C_A ≫ log A`) close both implication directions.

## 6. Cheapest next step

Pursue NEXT.md routes #1 and #2 (selected real cofactor anti-conspiracy / source-map
interferometry), which act on the **π-term** directly. The Gamma sheet is a proven dead end for
the Archimedean gate and should be archived as such, not re-probed.
