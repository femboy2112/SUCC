# The signed CRT decomposition of the Weyl gate: is the π-carrier the sole obstruction?

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (subagent "Front D: p-adic/CRT signed phase").
**Scope:** attack `S_N(h) = Σ_{n≤N} e(hU_n)` through the exact simultaneous-prime (CRT)
decomposition of LS-12/15a, with the **selected** phase (not the Galois/Ramanujan average).
Determine rigorously whether the CRT structure gives a genuinely different handle on `S_N(h)`
than the raw Diophantine rotation, or whether the cofactor `e(hC_n)` remains the entire
obstruction.

π base-16 normality and RH remain **OPEN** throughout; nothing here claims either.

---

## 0. The exact objects (all proved upstream, restated for self-containment)

```
r(n)   = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)      (four-pole BBP, exact rational)
U_0    = 0,   U_{n+1} = 16 U_n + r(n+1)                    (zero seed)
U_n    = 16^{n-1} π - T_n,   T_n = Σ_{j≥1} 16^{-j} r(n+j)  (Green tail, 0 < T_n < 1/(8n+1)²)
```

The gate: `S_N(h) = Σ_{n≤N} e(hU_n) = o(N)` for each fixed `h≠0` ⟺ π base-16 normal.

**LS-12 (CRT decomposition).** For dyadic `A = 2^j`, let
`P_A = { p = 8k+1 prime : A/2 ≤ k < A }`. Every `p ∈ P_A` has an exact clean source interval
covering all `n ∈ [A, 2A)`. With `b_p = (p+7)/8 = k+1` and
`a_{p,n} = 4·16^{n-b_p} mod p ∈ {0,…,p-1}`,

```
U_n = Σ_{p∈P_A} a_{p,n}/p + C_n,   C_n ∈ Z_{(P_A)}          (LS-12)
```

where `Z_{(P_A)}` = rationals whose reduced denominator is coprime to every `p ∈ P_A`. Hence

```
e(hU_n) = e(hC_n) · Π_{p∈P_A} e(h a_{p,n}/p)                (selected phase)
```

**LS-15a (prime-product height).** `Σ_{p∈P_A} log p = A + o(A)`, so `Π_{p∈P_A} p = exp(A+o(A))`.

The maintainer's Galois **average** (LS-13/14) averages the `a_{p,n}` over the multiplicative
group `u_p ∈ F_p^×`, producing Ramanujan sums `c_p(16^d − 1)` and an *exponentially small*
short-lag coherence — but this averages away the selected real phase. **Our object is the
selected phase `e(h Σ_p a_{p,n}/p)`.**

---

## 1. The exact selected-prime-phase structure

### 1.1 The residue is a geometric progression mod p (exact, elementary)

For `p = 8k+1`, `b_p = k+1`. The selected residue is

```
a_{p,n} = 4 · 16^{n - k - 1} mod p   =   4 · 16^{n - b_p} mod p.
```

As `n` runs, `a_{p,n}` is (up to the constant factor 4) the **geometric progression**
`{16^{n-k-1} mod p}`, which is periodic with period `ord_p(16)` — the multiplicative order of
16 in `F_p^×`. Thus each prime clock contributes a phase

```
e(h a_{p,n}/p) = e(4h · 16^{n - k - 1} / p)   (a Gauss-type sum over the powers of 16)
```

and the **full selected prime phase is a genuine product over p of geometric-progression phases**:

```
Φ_A(n) := Π_{p∈P_A} e(h a_{p,n}/p) = e( Σ_{p∈P_A} 4h · 16^{n-k-1} / p ).
```

This is *exact* — no averaging, no randomness — but note it is a product of **periodic** phases:
each factor has period `ord_p(16)`, which is finite and can be small (`ord_257(16) = 4`).

### 1.2 The decisive structural fact: the prime phase is *rational*, the π is *only* in the cofactor

The sum `Σ_{p∈P_A} a_{p,n}/p` is a **rational number** with (reduced) denominator
dividing `Π_{p∈P_A} p`. Therefore, for fixed `h`,

```
Θ_n^{(A)} := h Σ_{p∈P_A} a_{p,n}/p   is a rational number, and the selected prime phase
            Φ_A(n) = e(Θ_n^{(A)}) is a root of unity of order dividing |h| · Π_{p∈P_A} p
```

i.e. `Φ_A(n) ∈ Q(ζ_D)` for `D | |h|·Π_{p∈P_A} p` — a **torsion** point on the unit circle.

### 1.3 The exact separation (PROVED)

Because the CRT decomposition (LS-12) is **exact** (it is an identity of rational numbers, not an
approximation), we have the *exact* factorization at the level of the phase:

```
S_N(h) = Σ_{n≤N} Φ_A(n) · e(hC_n),      (∗)
```

where
- `Φ_A(n) = Π_p e(h a_{p,n}/p)` is the **selected prime phase** — a product of periodic
  geometric-progression phases, a torsion point of order dividing `Π_{p∈P_A} p`;
- `e(hC_n)` is the **cofactor phase** — the sole carrier of π (proved upstream:
  `C_n = 16^{n-1}π − T_n − S_n` where `S_n = Σ_p a_{p,n}/p` is the rational prime part).

**The factorization (∗) is an exact multiplicative separation of the *torsion* (prime, periodic,
algebraic) part from the *real transcendental* part `e(hC_n)`.**

The key question (task item 3) is whether this exact separation is *useful* — i.e. whether the
torsion part `Φ_A(n)` can be summed or bounded in a way that separates cleanly from `e(hC_n)`.

---

## 2. Can `Σ_n Φ_A(n)` be evaluated or bounded exactly?

### 2.1 Each prime clock individually: a complete Gauss sum (exact)

Fix one `p ∈ P_A`. Over a full period `L_p = ord_p(16)`, the sum of one prime clock is

```
Σ_{n=0}^{L_p-1} e(4h · 16^n / p)  =  complete Gauss sum over the subgroup ⟨16⟩ ⊆ F_p^×.
```

Since `16 = 2^4` and `p ≡ 1 (mod 8)`, `16` is a **quartic power**; the subgroup `⟨16⟩ ⊆ F_p^×`
is nontrivial in general. The complete sum over the cyclic subgroup `H = ⟨16⟩` of the additive
character is

```
Σ_{x∈H} e(4h x / p)  =  0   if  4h ≢ 0 (mod p)   [orthogonality of additive characters on H],
```

i.e. the single-clock sum **vanishes** whenever `p ∤ 4h`, because the additive character
`x ↦ e(4hx/p)` restricted to the subgroup `H` is nontrivial. Hence each individual prime clock,
averaged over its full period, is **exactly 0**.

### 2.2 The full product: a tensor of independent torsion clocks — no clean decoupling

The full prime phase is the **product** `Φ_A(n) = Π_p e(h a_{p,n}/p)`. Because the periods
`L_p = ord_p(16)` for different `p` are **multiplicatively entangled** (the `a_{p,n}` share the
common `16^n` and the common shift `k+1 = (p+7)/8`), the product does **not** factor into
independent one-clock sums: `Σ_n Π_p e(4h 16^{n-k-1}/p)` is a sum of a product, not a product of
sums.

Concretely, with `k_p = (p-1)/8`:

```
Φ_A(n) = e( 4h · 16^{n} · Σ_{p∈P_A} 16^{-k_p-1} / p ).
```

Define the **prime-phase coefficient**

```
ρ_A := Σ_{p∈P_A} 16^{-k_p-1} / p   (an exact rational, independent of n),
```

so that `Φ_A(n) = e(4h · 16^n · ρ_A)` — the **entire selected prime phase collapses to a single
geometric rotation with rational multiplier** `4h ρ_A`.

This is the crux. Let me state it precisely:

**Lemma (exact collapse).** `Φ_A(n) = e(4h · 16^n · ρ_A)` where `ρ_A = Σ_{p∈P_A} 16^{-(p+7)/8}/p`
is a rational number (a finite sum of rationals `1/(p·16^{k_p+1})`), hence `ρ_A = u/v` in
lowest terms for some integers `u, v` with `v | lcm_{p∈P_A}( p · 16^{k_p+1} )`. Therefore the
selected prime phase is **a single rational-rotation phase**, not a genuine product of
independent clocks: the CRT "tensor of clocks" collapses to one clock with rational frequency
`4h ρ_A` (a finite-order/torsion rotation).

**Proof.** `a_{p,n} = 4·16^{n-k-1} mod p`, and `e(h a_{p,n}/p) = e(4h·16^{n-k-1}/p)` because
adding a multiple of `p` inside `e(·/p)` is exact (period 1). Summing the exponents:

```
Σ_p h a_{p,n}/p  ≡  Σ_p 4h·16^{n-k_p-1}/p  (mod 1)
              = 4h·16^n · Σ_p 16^{-k_p-1}/p  =  4h·16^n·ρ_A   (mod 1).
```

The congruence is mod 1 (the phase is `e(·)`), and each `a_{p,n}` is taken in `{0,…,p-1}`, so the
identity is exact up to integer parts that are irrelevant under `e(·)`. ∎

### 2.3 Consequence: the prime phase is a rational Diophantine rotation in disguise

`Φ_A(n) = e(4h·16^n·ρ_A)` with `ρ_A ∈ Q`. But this is **exactly the same type of object as the
raw orbit**: a rotation by a power of 16 times a (rational) multiplier. Summing:

```
Σ_{n≤N} Φ_A(n) = Σ_{n≤N} e(4h ρ_A · 16^n)   — a geometric-phase Weyl sum with rational multiplier.
```

Since `ρ_A ∈ Q`, write `ρ_A = u/v` in lowest terms. Then `e(4hρ_A·16^n)` is a **torsion** phase:
it is periodic in `n` with period dividing `ord_v(16)`. Therefore `Σ_{n≤N} Φ_A(n)` is a
**periodic sequence summed over a length-N window**, exactly computable, and it is `O(N)` —
i.e. the prime phase **does not by itself give `o(N)` cancellation**. It is a finite-order
rotation (a "stroboscope"), contributing `Θ(N)` oscillation, not decay.

(When `v | 16^d` for some `d`, the phase is constant or `d`-periodic; in all cases the sum is
`O(N)` with an explicit quasi-periodic main term — no `o(N)` saving from the prime part alone.)

---

## 3. The decisive answer: the cofactor remains the SOLE obstruction (PROVED)

Combine the exact collapse (Lemma) with the exact factorization (∗):

```
S_N(h) = Σ_{n≤N} e(4h ρ_A · 16^n) · e(h C_n).        (†)
```

Now the crucial observation is the **double-counting of the prime part**. The cofactor is

```
C_n = 16^{n-1} π − T_n − S_n,    S_n := Σ_{p∈P_A} a_{p,n}/p  (rational).
```

But `e(hC_n) = e(h(16^{n-1}π − T_n)) · e(−h S_n)`, and `e(−h S_n) = e(−4hρ_A·16^n)` is exactly the
**inverse** of the prime phase `Φ_A(n)`. Therefore:

**Theorem (cofactor is the sole obstruction — PROVED).** For the *original zero-seeded BBP orbit*
`U_n = 16^{n-1}π − T_n`, the exact CRT factorization reconstructs the raw orbit:

```
Φ_A(n) · e(hC_n) = e(4hρ_A·16^n) · e(h(16^{n-1}π − T_n)) · e(−4hρ_A·16^n)
                 = e(h(16^{n-1}π − T_n)) = e(hU_n).
```

The prime phase `Φ_A(n)` **exactly cancels** the rational prime part `S_n` inside the cofactor,
leaving precisely the raw Diophantine rotation `e(h(16^{n-1}π − T_n))`. Hence:

```
S_N(h) = Σ_{n≤N} Φ_A(n) · e(hC_n) = Σ_{n≤N} e(hU_n)   EXACTLY, for every N, A.
```

The CRT decomposition is an exact **re-encoding** of the same Weyl sum; the "tensor of prime
clocks" `Φ_A(n)` and the "π-carrying cofactor" `e(hC_n)` are **not independent** — they are
inverse conjugates whose product is identically the raw rotation. The CRT structure therefore
gives **no genuinely different handle**: the cofactor `e(hC_n)` (equivalently the raw
`e(h(16^{n-1}π − T_n))`) remains the entire obstruction.

**In other words:** the prime part is rational/torsion, and *whatever* torsion the CRT exposes is
*by construction* the negation of the rational part already hidden inside `C_n`. Splitting
`U_n` into "prime clocks + cofactor" and then hoping to bound the two legs separately is a
**telescoping identity**, not a decoupling: the two legs multiply back to the single object we
started with.

### 3.1 Why the Galois average looked like progress (and why it is not)

The maintainer's LS-13/14 Galois average is *not* the selected embedding: it replaces each
`a_{p,n}` by `u_p a_{p,n}` and averages `u_p` over `F_p^×`, producing Ramanujan sums
`c_p(16^d − 1)`. That average is **legitimate as an average** (its smallness is real: exponentially
small short-lag coherence), but it is a *different object* from `S_N(h)`. The average annihilates
exactly the selected rational-rotation phase `e(4hρ_A·16^n)` that — by the Theorem — is the
negation of the rational part inside the cofactor. So the Galois average "sees cancellation" only
because it has thrown away the very phase that must multiply the cofactor to reconstruct the
original sum. The hostile source-map obstruction (LS-04) is the same phenomenon: it shows that
any inference from prime clocks *alone* (or from `p`-free denominator types alone) to normality is
invalid, because the rational prime part can be re-absorbed into a counterfeit `C_n^*`.

### 3.2 Boundary (what is NOT established)

- We do **not** claim `S_N(h) = o(N)`. The Theorem only establishes the **negative** result that
  the CRT/prime-clock decomposition does *not* reduce the gate: it is an exact identity, so it
  cannot be "harder or easier" than the raw sum. The raw sum's `o(N)` status is exactly the open
  question.
- We do **not** claim the cofactor `e(hC_n)` is "hard" in any new sense; only that it is the *same*
  obstruction as the original, unchanged by CRT.
- The prime phase `Φ_A(n)` being `O(N)`-oscillatory (periodic) is **proved**, but it is *irrelevant*
  to the gate, because it cancels.
- `A` here is a free dyadic parameter; the Theorem holds for **every** dyadic `A` simultaneously
  (the CRT decomposition is valid for each `A`, and the collapse + cancellation is exact at each).

### 3.3 What this rules out (negative results, PROVED)

1. Any strategy that sums `Σ_n Φ_A(n)` first (claiming the prime part is "easy because it is
   torsion/periodic") and then multiplies by a separately-bounded `e(hC_n)` is **invalid**:
   the two parts do not decouple; their product is the raw sum by telescoping.
2. Any strategy that treats the "cofactor `C_n`" as a *different* (e.g. smoother, smaller, or more
   regular) object than `16^{n-1}π − T_n` is **mistaken**: `C_n = 16^{n-1}π − T_n − S_n` with
   `S_n` rational, so `C_n` differs from the raw rotation only by a rational `S_n` whose phase is
   exactly `Φ_A(n)`'s inverse. The *real (Archimedean) content of `C_n` is precisely
   `16^{n-1}π − T_n`.
3. The "multi-prime CRT tensor" is **not** a genuine tensor product of independent obstructions;
   it collapses to a single rational rotation (Lemma), which is the inverse of the cofactor's
   rational part (Theorem).

---

## 4. Claim ledger

| ID | Statement | Status |
|----|-----------|--------|
| ST-01 | `a_{p,n} = 4·16^{n-k-1} mod p` is a geometric progression mod p, period `ord_p(16)` | **PROVED** (elementary, definitional) |
| ST-02 | Single-clock sum `Σ_{x∈⟨16⟩} e(4hx/p) = 0` when `p∤4h` (additive orthogonality) | **PROVED** (Gauss sum) |
| ST-03 | Exact collapse `Φ_A(n) = e(4hρ_A·16^n)`, `ρ_A = Σ_p 16^{-k_p-1}/p ∈ Q` | **PROVED** (Lemma) |
| ST-04 | `Σ_{n≤N} Φ_A(n)` is a periodic/`O(N)`-oscillatory sum (no `o(N)` saving alone) | **PROVED** (torsion rotation) |
| ST-05 | Exact factorization `S_N(h) = Σ_n Φ_A(n) e(hC_n)` | **PROVED** (from LS-12, exact) |
| ST-06 | `Φ_A(n) e(hC_n) = e(hU_n)` identically (prime phase cancels rational part of cofactor) | **PROVED** (Theorem) |
| ST-07 | CRT decomposition gives **no genuinely different handle**; cofactor = raw rotation = sole obstruction | **PROVED** (Corollary of ST-06) |
| — | `S_N(h) = o(N)` (the gate) | **OPEN** (unchanged by this work) |
| — | π base-16 normality | **OPEN** |
| — | RH | **OPEN** |

---

## 5. Source receipt

- Upstream proved inputs: `research/2026-11-02/line_sheet_gamma/PROOFS.md`, LS-12 (CRT
  decomposition, `U_n = Σ_p a_{p,n}/p + C_n`, `C_n ∈ Z_{(P_A)}`), LS-13/14 (Galois average +
  short-lag firewall), LS-15a (`Π_{p∈P_A} p = exp(A+o(A))`), LS-15b (selected-phase nonrepeat),
  and the hostile source-map obstruction (LS-04). All read from branch
  `origin/research/line-sheet-gamma-sublog-multiprime-2026-11-02`.
- Zero-seed/BBP orbit identities: memory 2026-11-02 flush (stable structural findings), and
  `research/2026-11-02/pi_normality_spine/` (reduction chain).
- This file is new work under `research/2026-11-02/shen_tzu_weyl/` only; no existing file modified.

**π base-16 normality and RH remain OPEN.**
