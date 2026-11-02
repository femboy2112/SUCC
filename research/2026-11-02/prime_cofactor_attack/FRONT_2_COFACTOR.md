# ATTACK FRONT 2 — Exact arithmetic structure of the cofactor V_{p,n}

**Date:** 2026-11-01 (session) / 2026-11-02 (branch). Research-only; paper proofs.
**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`.
**Base:** `81045770` (main, `81045770234a114247e43eb08ae5c6d446e9514a`).
**Status summary:** Everything that is *exact* here is PROVED. Everything that
would *control* `e(h V_{p,n})` or bound `|R_p(h)|` below the trivial length is
**OPEN**, and the cofactor framing is provably *equivalent* to the already-known
missing signed-cancellation gate. No normality claim is made; no unproven bound
is asserted. π base-16 normality and RH remain OPEN.

---

## 0. Source, notation, boundaries

Base `b=16`, `e(t)=exp(2π i t)`. The four-pole BBP forcing is

```
r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2),
U_0 = 0,   U_n = 16 U_{n-1} + r(n),   U_n = Σ_{j=1}^{n} 16^{n-j} r(j).
```

`p` prime, `p > 5`, `p ≡ 5 (mod 8)`, birth index `a_p = (p+3)/8`, window
`a_p ≤ n < (p+1)/2 =: b_p`. Inside the window

```
U_n = c_p · 16^{n-a_p}/p + V_{p,n},   c_p = -1 (p ≡ 5 mod 8),   V_{p,n} ∈ Z_(p),
V_{p,n+1} = 16 V_{p,n} + r(n+1),     V_{p,a_p} = r(a_p) - c_p/p + Σ_{j<a_p} 16^{a_p-j} r(j).
```

All finite `r(j)`, `U_n`, `V_{p,n}`, `W_{p,n}` are exact rationals.

---

## 1. EXACT structure of V_{p,n} and W_{p,n}

### 1.1 The single most important arithmetic fact: r(n) is quadratic-over-quartic

Reducing `r(n)` to a common denominator, the **numerator is a quadratic in n**:

```
r(n) = (960 n² − 712 n + 128) / D(n),   D(n) = lcm(8n−7, 8n−4, 8n−3, 8n−2).
```

**Receipt (exact Fractions).** The un-reduced numerator is
`4(8n−4)(8n−3)(8n−2) − 2(8n−7)(8n−3)(8n−2) − (8n−7)(8n−4)(8n−2) − (8n−7)(8n−4)(8n−3)`
`= 960n² − 712n + 128` (SymPy `expand`, exact). The reduction factor
`gcd(960n²−712n+128, D_unreduced)` varies with `n` (see table below), but the
*un-reduced* numerator is exactly the quadratic `960n²−712n+128` for every n.

Asymptotic (SymPy `series`, exact coefficients):

```
r(n) = 15/(64 n²) + 151/(512 n³) + 1209/(4096 n⁴) + O(n^{-5}),   n → ∞.
```

In particular `r(n) > 0` for all `n ≥ 1`, and `r(n) < 15/(64(n−1)²)`-type bounds
(positive regrouping) hold; the inherited sharp bound `0 < T_n < 1/(64 n²)` and
`Σ T_n < 1/32` are unchanged.

**Exact reduced-numerator receipt (p=13 path is representative; table is general):**

| j | reduced r(j) | denom factors | raw numerator 960j²−712j+128 | reduction factor |
|---|---|---|---|---|
| 1 | 47/15 | 3·5 | 376 | 8 |
| 2 | 106/819 | 3²·7·13 | 2544 | 24 |
| 3 | 829/19635 | 3·5·7·11·17 | 6632 | 8 |
| 4 | 316/15225 | 3·5²·7·29 | 12640 | 40 |
| 5 | 857/69597 | 3²·11·19·37 | 20568 | 24 |
| 6 | 3802/466785 | 3²·5·11·23·41 | 30416 | 8 |

### 1.2 The tower identity is an exact telescoping (no phase approximation)

```
W_{p,n} := Σ_{j=a_p+1}^{n} 16^{n-j} r(j),
U_n = 16^{n-a_p} U_{a_p} + W_{p,n}.                       (tower, exact in Q)
```

**Proof.** `U_n = Σ_{j=1}^n 16^{n-j} r(j) = 16^{n-a_p} Σ_{j=1}^{a_p} 16^{a_p-j} r(j)
+ Σ_{j=a_p+1}^n 16^{n-j} r(j) = 16^{n-a_p} U_{a_p} + W_{p,n}`. Pure regrouping of a
finite rational sum; verified symbolically for p=13, every n in window (below).

### 1.3 V_{p,n} is a shifted, p-cleaned copy of the clock term

Combining the cofactor definition `U_n = c_p 16^{n-a_p}/p + V_{p,n}` with the tower:

```
V_{p,n} = 16^{n-a_p}( U_{a_p} − c_p/p ) + W_{p,n}.        (exact in Q)
```

**Proof.** `V_{p,n} = U_n − c_p 16^{n-a_p}/p = 16^{n-a_p}U_{a_p} + W_{p,n} − c_p16^{n-a_p}/p`.
The `W` term is empty at `n = a_p`, giving the stated initial value
`V_{p,a_p} = U_{a_p} − c_p/p = r(a_p) − c_p/p + Σ_{j<a_p}16^{a_p-j}r(j)`.

**Receipt (exact Fractions, p=13, a_p=2, b_p=7, c_p=−1):**

| n | V_{p,n} (exact) | V denom factor of 13? | W_{p,n} denom factor of 13? |
|---|---|---|---|
| 2 | 15857/315 | **no** | (empty) |
| 3 | 47446631/58905 | no | no |
| 4 | 110076361196/8541225 | no | no |
| 5 | 1238138984670283/6004481175 | no | no |
| 6 | 6227013682274832478/1887408582675 | no | no |

Both identities hold `True` in exact `Fraction` arithmetic for every n in the
window (checked for all listed primes below).

### 1.4 Denominator growth: exponential in n, no periodicity

`D(j) = lcm(8j−7,8j−4,8j−3,8j−2)` is a product of four numbers each `Θ(j)`, so
`D(j) = Θ(j⁴)`. `W_{p,n}` has denominator the lcm of `D(j)` over `j = a_p+1..n`,
hence `Θ((n!)⁴)`-like growth — specifically `O(exp(Θ(n log n)))` in bit length.
**Receipt (p=149, a_p=19, b_p=75):** denom(W_{19})=1 bit; denom(W_{24})=101 bits;
denom(W_{39})=263 bits; denom(W_{74})=609 bits (i.e. 184 decimal digits).

**Conclusion (task 1, periodicity).** `V_{p,n} mod 1` and `W_{p,n} mod 1` have
**no useful periodic or arithmetic-progression structure within the window**:
the rational `W_{p,n}` has denominator of exponentially growing bit size, so
`e(h W_{p,n})` ranges over roots of unity of astronomically large and rapidly
varying order as n advances. There is no finite modulus M with `W_{p,n+M} ≡ W_{p,n}`
mod 1. The only "structure" is the 16-geometric recurrence itself, which is exactly
the structure of `U_{a_p}`.

### 1.5 p-integrality inside the window is a congruence fact

**Lemma (PROVED).** For every prime `p > 5, p ≡ 5 mod 8`, and every `j` with
`a_p < j < b_p` (i.e. `(p+3)/8 < j < (p+1)/2`), none of `8j−7, 8j−4, 8j−3, 8j−2`
is divisible by `p`. Hence `W_{p,n}` and `V_{p,n}` have denominator coprime to `p`
throughout the window (they are p-integral, in fact p-*free* in the denominator).

**Proof.** Any multiple of `p` among `8j−k` (k ∈ {2,3,4,7}) equals `mp`. Since
`8j−k` lies in `(8a_p+8−7, 8b_p−8−2) = (p+4, 4p−10)`, we need `m ∈ {2,3}`.
But `p ≡ 5 (mod 8)` gives `2p ≡ 2 (mod 8)`, `3p ≡ 7 (mod 8)`, so
`2p+k ∈ {4,5,6,9≡1}` and `3p+k ∈ {9≡1,10≡2,11≡3,14≡6}`, never `≡ 0 (mod 8)`.
Thus `8j = mp + k` is never divisible by 8, contradicting `j ∈ Z`. ∎

**Receipt:** checked exhaustively for p ∈ {13,29,37,53,61,101,149,197,229,269};
`max p-exponent in denom(W) = 0` and `= 0` in denom(V) for all of them.

The p-adic pole is therefore carried *entirely* by the clock term
`c_p 16^{n-a_p}/p` (valuation exactly −1, inherited from `U_{a_p}`), and the
cofactor `V_{p,n}` is p-adically unramified inside the window. This confirms the
`Z_(p)`-integrality claim in the setup, but it is **not** a source of phase
control: integrality is a valuation statement, orthogonal to the real-phase
distribution of `V_{p,n} mod 1`.

---

## 2. The coupling V ↔ clock, and whether e(hV)e(h·clock) simplifies

### 2.1 The exact factorization and its immediate consequence

```
e(h U_n) = e(h · 16^{n-a_p} U_{a_p}) · e(h W_{p,n})                    (tower)
         = e(h c_p 16^{n-a_p}/p) · e(h V_{p,n})                        (cofactor)
```

Both are exact (arguments equal in `Q`). Substituting `V_{p,n}`'s exact form:

```
e(h U_n) = e(h c_p 16^{n-a_p}/p) · e(h·16^{n-a_p}(U_{a_p}−c_p/p)) · e(h W_{p,n})
```

The two clock factors collapse by the tower identity:

```
e(h c_p 16^{n-a_p}/p) · e(h·16^{n-a_p}(U_{a_p} − c_p/p))
  = e(h·16^{n-a_p} U_{a_p})
  = e(h U_n) · e(−h W_{p,n}) .
```

So the "simplification" is **exactly** the tower identity restated. It is a
*re-packaging*, not a *reduction*: the phase `e(h U_n)` is still the product of a
16-geometric clock phase and a 16-geometric partial sum `W_{p,n}` of the *same*
forcing `r(j)`.

### 2.2 W_{p,n} is NOT simpler than U_{a_p} — it is strictly harder

`U_{a_p} = Σ_{j=1}^{a_p} 16^{a_p-j} r(j)` has `a_p = (p+3)/8 ≈ p/8` terms.
`W_{p,n} = Σ_{j=a_p+1}^{n} 16^{n-j} r(j)` has, at the window's right end,
`(b_p−1) − a_p = (3p+1)/8 − 1 ≈ 3p/8` terms — roughly **three times as many**,
over the *same* forcing `r(j)`, with the *same* multiplier 16. Therefore:

> **W_{p,n} is the same kind of 16-geometric sum as U_{a_p}, only longer and
> with a shifted (later, larger-denominator) index range.** It is not simpler in
> any arithmetic sense; it is the same object at a later time.

This refutes the implicit hope of the framing: moving the "prime birth" into a
cofactor does not replace the hard 16-geometric sum with anything tractable. The
hard part of `U_n` — a 16-weighted signed sum of `r(j) ∼ 15/(64 j²)` — reappears
verbatim as `W_{p,n}`.

### 2.3 The "shared multiplier 16" is not a conspiracy, it is a tautology

The observation that `V_{p,n}` and the clock `16^{n-a_p}` share the multiplier 16
is exactly the statement that **both are governed by the same linear recurrence
`x ↦ 16x + r`. There is no independent "clock" to conspire with the cofactor: the
clock *is* the homogeneous part of the same recurrence that defines `V`.** The
coupling is the definitional identity

```
V_{p,n+1} = 16 V_{p,n} + r(n+1),
16^{n+1-a_p} = 16 · 16^{n-a_p}.
```

So any "cancellation" between `e(hV)` and `e(h·clock)` is a statement about the
*single* sequence `U_n` and cannot be extracted by algebraic rearrangement. The
phase `e(h U_n)` is one number; decomposing it into two factors that share a
multiplier does not introduce a new degree of freedom.

---

## 3. Is there a source-derived sub-trivial bound on |R_p(h)| without normality?

Define

```
R_p(h) = Σ_{n=a_p}^{b_p-1} e(h U_n),   window length L_p = b_p − a_p = (3p+1)/8.
```

The question asks whether `|R_p(h)| ≤ L_p (log p)^{-η}` (η > 0) can be proven
from the *source* (the exact arithmetic of r, the tower, the p-integrality)
**without** assuming normality of the 16-digits.

**Answer: No such bound is currently proven, and the cofactor framing cannot
produce one, because it is provably equivalent to the already-documented missing
signed-cancellation gate.**

### 3.1 Reduction to the known equivalence

The exact identity of §2.1 gives

```
R_p(h) = Σ_{n=a_p}^{b_p-1} e(h c_p 16^{n-a_p}/p) · e(h V_{p,n})
       = Σ_{n=a_p}^{b_p-1} e(h·16^{n-a_p} U_{a_p}) · e(h W_{p,n}) .
```

Both factorizations are the *same* sum over the *same* terms; they differ only in
which factor is called "clock". A sub-trivial bound on `|R_p(h)|` is therefore a
statement about the **signed Weyl sum of the single sequence `U_n` restricted to
the window `[a_p, b_p)`** — precisely the object that the signed-cancellation
frontier has already localized as the gap.

From the repo's own ledger (`docs/CLAIM_SUPPLEMENT_SIGNED_CANCELLATION_BARRIER.md`
and `research/2026-10-27/PI_SIGNED_CANCELLATION_SYNTHESIS.md`):

* **SCB-06**: "Fixed-M or existential sufficiently slow growing energy gates for
  all fixed nonzero modes are **equivalent to normality**." A sub-trivial bound on
  the signed Weyl sum (which is a fixed-M energy gate with M = window length) is,
  up to the documented moving-frequency subtlety, *equivalent* to the very
  normality it is being asked to avoid assuming.
* **SCB-07 / E7**: for *every* prescribed `M(N) → ∞, M(N) = o(N)`, one can
  construct a **normal** base-16 carrier with `liminf` endpoint energy `≥ 1/4` at
  every fixed `h` (and irrationality exponent ≤ 4). Hence a bound valid "for every
  normal carrier" is **false**; a bound specific to π must use arithmetic of π that
  is *not* shared by these normal counterexamples. No such source-arithmetic
  lemma exists yet.

### 3.2 Why the cofactor's "arithmetic structure" (§1) does not help

The exact facts proven in §1 — quadratic numerator, p-integrality, exponential
denominator growth, absence of periodicity — are all **coarse, generic, or
negative**:

* The quadratic numerator `960n²−712n+128` is *shared by every carrier* with the
  same forcing; it is a property of `r`, not of the selected orbit. The E7 normal
  counterexample has the *same* `r` and a *changed seed*; it inherits the identical
  quadratic numerator, tower identity, and p-integrality. Therefore **none of these
  facts can distinguish π from a normal (or even non-normal) counterfeit**, and
  none can yield a π-specific sub-trivial bound.
* p-integrality (§1.5) is a *valuation* statement (denominator coprime to p). The
  real phase `V_{p,n} mod 1` is insensitive to p-adic valuation; integrality does
  not constrain the uniform distribution of `e(hV_{p,n})` on the unit circle.
* The absence of periodicity (§1.4) is a *negative* result: it removes the only
  easy route to control, leaving exactly the hard signed sum.

### 3.3 Verdict (task 3)

> **REFUTED as "derivable from the source alone without normality," in the precise
> sense that no such derivation exists in the current literature or the repo, and
> the framing is provably circular-with-respect-to-normality (SCB-06).** The
> sub-trivial bound is *equivalent to* the missing signed-cancellation estimate,
> which is the documented OPEN gap. No counterexample to π-normality is claimed
> (indeed SCB-07/E7 are changed-seed carriers, not π); the correct statement is
> that the cofactor reformulation **adds no new leverage** and its exact structure
> is **shared** with carriers for which the bound is false.

---

## 4. The EXACT remaining lemma

There is no missing lemma *unique to the cofactor framing*; the remaining gap is
the repository-wide one, now expressed in cofactor language:

**Remaining lemma (OPEN, exact statement).** For the *authentic* four-pole orbit
(seed 0, `r` as above, `U_{a_p}` with `v_p = −1` at `a_p = (p+3)/8`), prove

```
Σ_{n=a_p}^{b_p-1} e(h W_{p,n}) · e(h·16^{n-a_p} U_{a_p}) = o(L_p),
L_p = (3p+1)/8,
```

for every fixed integer `h ≠ 0` and all `p ≡ 5 (mod 8)`, i.e. control the
**signed** correlation between the (later) 16-geometric partial sum `W_{p,n}` and
the (earlier) clock `16^{n-a_p}U_{a_p}`, where the moving completed frequency is
`h(16^{n-a_p} − 1)` in the standard energy form. This is verbatim the "missing
signed cancellation" of the signed-cancellation barrier, restricted to the
prime-birth window. **Equivalently** (SCB-06): it is the window-restricted
normality assertion.

Everything short of this — the exact tower identity, the quadratic numerator, the
p-integrality lemma, the no-periodicity theorem — is **PROVED here and gives no
asymptotic saving**. The single cheapest next step, consistent with the existing
frontier, is the shrinking-window boundary problem

```
#{ a_p ≤ n < b_p : {16^{n-a_p} π} < T_n } = o(L_p),
```

which (per the signed-cancellation synthesis §6) would extend transport to every
bounded one-digit statistic and is the weakest statement that is still *not*
implied by the exact arithmetic facts proven above.

---

## 5. Claim ledger

Labels per repo discipline: `PROVED` = paper proof in stated domain (not Lean, not
external peer review); `VERIFIED_FINITE` = exact computation; `OPEN` = no proof;
`REFUTED` = countermodel receipt given. No status is promoted.

| ID | Statement and domain | Status | Receipt / next falsifier |
|---|---|---|---|
| F2C-01 | `r(n) = (960n²−712n+128)/D(n)`, `D(n)=lcm(8n−7,8n−4,8n−3,8n−2)`, numerator quadratic for all n ≥ 1 | PROVED | SymPy exact expand; table §1.1 |
| F2C-02 | `r(n) = 15/(64n²) + O(n^{-3}) > 0` for n ≥ 1 | PROVED | SymPy series; positive regrouping |
| F2C-03 | Tower identity `U_n = 16^{n-a}U_a + W_{p,n}` exact in Q | PROVED | symbolic `Fraction` check, all n in window |
| F2C-04 | `V_{p,n} = 16^{n-a}(U_a − c_p/p) + W_{p,n}` exact in Q | PROVED | symbolic `Fraction` check |
| F2C-05 | `V_{p,n}`, `W_{p,n}` p-integral (p-free denom) in window | PROVED | congruence lemma §1.5; exhaustive check p ∈ {13,…,269} |
| F2C-06 | `U_{a_p}` has `v_p = −1` at `a_p=(p+3)/8` | VERIFIED_FINITE (p=13) | denom(4095)=3²·5·7·13, numer coprime to 13 |
| F2C-07 | `V_{p,n} mod 1`, `W_{p,n} mod 1` have no finite periodicity in window | PROVED | denominator bit-length grows Θ(n log n), §1.4 |
| F2C-08 | `W_{p,n}` is same-kind 16-geometric sum as `U_{a_p}`, ~3× longer | PROVED | term count (3p+1)/8 vs (p+3)/8 |
| F2C-09 | Sub-trivial bound on `|R_p(h)|` derivable from source without normality | REFUTED (as source-only) | SCB-06 equivalence-to-normality; SCB-07/E7 normal counterexamples share all of §1 |
| F2C-10 | Signed cancellation `Σ_{n=a_p}^{b_p-1} e(hU_n)=o(L_p)` for authentic orbit | OPEN | remaining lemma §4; would be window-restricted normality |
| F2C-11 | π base-16 normality, RH | OPEN | unchanged; nothing here affects them |

---

## 6. Boundary and honesty statement

Nothing in this round establishes π-normality, a sub-trivial Weyl bound, or RH.
The exact arithmetic structure of the cofactor is fully characterized and is
*generic*: it is shared by every carrier with the same four-pole forcing (only the
seed and the p-adic birth differ), so it cannot by itself produce π-specific
cancellation. The framing "does the clock conspire with the cofactor?" is answered
in the negative as a *mechanism*: the clock and the cofactor are the homogeneous and
inhomogeneous parts of the *same* recurrence, and their product phase is exactly
the original `e(hU_n)` with a relabeling. The honest remaining object is the
single missing signed-cancellation estimate, now written in prime-window
coordinates.
