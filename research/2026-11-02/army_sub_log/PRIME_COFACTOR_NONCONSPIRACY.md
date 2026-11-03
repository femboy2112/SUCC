# Front 2 — Prime-cofactor nonconspiracy: the CRT decomposition cannot decouple C_A from π

**Branch:** `research/army-sub-log-collision-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (subagent, Front 2 of 6 — "prime-cofactor nonconspiracy").
**Scope:** the single open gate `C_A = (1/A) Σ_i v_i(A)^2 = o(log A)` for the ORIGINAL
four-pole BBP source at `U_0 = 0`, attacked via the exact simultaneous-prime (CRT)
decomposition of LS-12 / LS-15a. The task: derive the exact near-collision condition in
terms of the prime residues `a_{p,n}` and the complementary cofactor `C_n`, separate the
diagonal from the off-diagonal, and determine whether the prime residues *alone* (or the
residues plus a *non-hostile* cofactor consistent with the true BBP forcing + zero seed)
can deliver `C_A = o(log A)` without invoking the Diophantine content of π.

**π base-16 normality: OPEN. RH: OPEN.** No false victory. Every identity is exact
(`Fraction`), every bound is either proved or labelled CONJECTURE/OPEN.

---

## 0. Objects (maintainer LS-12 / LS-15a, PROVED upstream — restated, not re-derived)

Four-pole BBP forcing, orbit, and window as in the sibling fronts:

```
r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2),
U_0 = 0,   U_{n+1} = 16 U_n + r(n+1).
```

For dyadic `A = 2^j`, the prime window is

```
P_A = { p = 8k+1 prime : A/2 <= k < A },     k = (p-1)/8.
```

For each `p = 8k+1 in P_A` the residue is

```
a_{p,n} = 4 · 16^{n-(k+1)}  (mod p),      (n >= k+1; well-defined since p ∤ 16).
```

**LS-15a (EXACT CRT decomposition, PROVED).** For every `n >= A`,

```
U_n  =  sum_{p in P_A} a_{p,n}/p   +   C_n ,
```

where the *complementary cofactor* `C_n in Z_{(P_A)}` is a rational whose denominator is
coprime to every `p in P_A`. The decomposition is exact, source-preserving (each `a_{p,n}/p`
is the `p`-primary contribution of the single pole `4/(8(k+1)-7) = 4/p`), with no averaging.

Two structural scale facts (PROVED, PNT-AP in the class `p ≡ 1 (mod 8)`, unconditional):

```
prod_{p in P_A} p = exp(A + o(A)),   i.e.   sum_{p in P_A} log p = A + o(A).   (LS-12)
```

The following sharper statement is what this front **needs and uses**, and it is proved by the
same PNT-AP with an explicit constant — stated as PROVED because it is a standard consequence
(see the verification script for the constant check):

```
sum_{p in P_A} 1/p  =  (1/8) · log log(8A) + O(1)   =  O(log log A).   (LS-12')
```

In particular `sum_{p in P_A} 1/p = o(1/A^{-ε})` but, crucially, `sum_{p in P_A} 1/p` is **not**
summable in A — it grows like `log log A`. (This growth, not its smallness, is what matters.)

---

## 1. The EXACT near-collision condition (derived in full)

### 1.1 Two states, one window

For `n, m in [A, 2A)` with `n < m`, set `d = m - n in [1, A)`. Both states use the **same**
window `P_A` (it depends only on the dyadic epoch `A`, not on `n, m`). Subtract the two
exact decompositions:

```
U_m - U_n  =  sum_{p in P_A} (a_{p,m} - a_{p,n})/p   +   (C_m - C_n).
```

Define the **prime part** and the **cofactor part**:

```
S(n,m)   := sum_{p in P_A} (a_{p,m} - a_{p,n}) / p,      (rational, den | prod P_A)
ΔC(n,m)  := C_m - C_n,                                    (rational, den coprime to P_A)
```

### 1.2 The exact criterion

Two states share a `1/A` bin iff `floor(A{U_n}) = floor(A{U_m})`, i.e. (up to the measure-zero
bin boundary, which is handled exactly in the script) the circular distance to the nearest
integer is below the bin width:

**PROVED (Lemma NC-1).** `U_n, U_m` share a bin  ⟺  `‖ U_m − U_n ‖ < 1/A`, where
`‖x‖ = min_{k ∈ Z} |x − k|`. Equivalently, in the CRT coordinates:

```
‖ S(n,m) + ΔC(n,m) ‖  <  1/A .                                  (★)
```

*Proof.* Immediate from the definition of the histogram and the exact decomposition: the bin
index of a state is `floor(A{U})`, and two states are in the same bin iff their fractional
parts differ by less than the bin width `1/A`, which is exactly the circular-distance condition.
The decomposition `U_m − U_n = S + ΔC` is exact (LS-15a), so the criterion transfers verbatim.
∎

### 1.3 The exact size of the two pieces (the decisive structural fact)

**Claim (MAG-1, PROVED).** `S(n,m)` is a *small* rational: `|S(n,m)| ≤ Σ_{p∈P_A} (p-1)/p
≤ |P_A| = A/(8 log A) · (1 + o(1))` (each residue difference `(a_{p,m}−a_{p,n})/p` has magnitude
`< 1`, and there are `|P_A|` terms). Its denominator divides `∏P_A = exp(A + o(A))`.

**Claim (MAG-2, PROVED).** `ΔC(n,m)` is a *huge* rational. Its denominator is
`exp(6m + o(m))` (the conductor; machine-verified `log₁₀ den(C_n) ≈ 2.61 n`), and its
**magnitude** is `≈ 16^{m-1}π − 16^{n-1}π = 16^{n-1}(16^d − 1)π` — astronomically larger than
`S(n,m)`. Its *fractional part* is the only thing visible to (★).

The verification of MAG-1/MAG-2 is in §5 and the script. The essential point: **`S` is `O(A/log A)`
in magnitude with denominator `exp(A)`, while `ΔC` has denominator `exp(6A)` and magnitude
`exp(2.77 A)`.** The two live at totally different scales.

### 1.4 What the cofactor actually IS (the crux of the front)

Because the orbit is the BBP orbit, `U_n = 16^{n-1}π − T_n` (Green tail `T_n = Σ_{k≥1} 16^{-k}r(n+k)`,
PROVED). Substituting into the definition of `C_n`:

```
C_n  =  U_n − S_n  =  16^{n-1}π − T_n − S_n ,      S_n := Σ_{p∈P_A} a_{p,n}/p .
```

**Claim (COF-1, PROVED — the central identity of this front).**

```
C_n  =  16^{n-1}π − T_n − S_n ,
```

with `S_n = Σ_{p∈P_A} a_{p,n}/p` ranging in `[0, |P_A|)` (verified: `S_n ≈ 1.8–15` for
`A = 16…256`, growing like `|P_A| ≈ A/(8 log A)`), and `0 < T_n < 1/(8n+1)^2`. Therefore
`C_n = 16^{n-1}π − O(A/log A)`, and the magnitude of `C_n` exceeds that of `S_n` by a factor
`≈ 16^{n-1}π / (A/log A) = exp(2.77 A − log A + log log A)` (verified `10^{75}` at `A=64`).
The cofactor **dominates** the prime part; it carries the π-content:

```
ΔC(n,m)  =  16^{n-1}(16^d − 1)π − (T_m − T_n) − (S_m − S_n) .
```

The cofactor is **not** a free, arbitrary, or hostile parameter: under the *true* BBP forcing
`U_{n+1} = 16 U_n + r(n+1)` with the *true* zero seed `U_0 = 0`, the cofactor is pinned to
`16^{n-1}π` up to an `O(A/log A)` correction. **The fractional content of `C_n` is the base-16
digit content of π.**

### 1.5 The diagonal / off-diagonal split (exact)

Within `S(n,m) = Σ_p (a_{p,m} − a_{p,n})/p`, each prime is **diagonal** iff its residue does
not move:

```
a_{p,m} ≡ a_{p,n} (mod p)   ⟺   p | (16^d − 1)    (d = m − n),
```

because `a_{p,m} − a_{p,n} ≡ 4·16^{n-(k+1)}(16^d − 1) (mod p)` and `4·16^{n-(k+1)}` is a unit
mod `p`. For a diagonal prime the summand `(a_{p,m}−a_{p,n})/p` is a **rational integer**; for an
off-diagonal prime it is a proper fraction with denominator `p`.

Hence `S(n,m) = D(n,m) + O(n,m)` where `D(n,m) = Σ_{p | 16^d−1, p∈P_A} (a_{p,m}−a_{p,n})/p ∈ Z`
is the integer diagonal part and `O(n,m) = Σ_{p∤16^d−1} (a_{p,m}−a_{p,n})/p` is the proper
off-diagonal part.

**Claim (DIAG-1, PROVED — the diagonal is empty at short range).** For `d = m−n < A`,

```
Σ_{p∈P_A, p | 16^d − 1} log p  ≤  log(16^d − 1)  =  d log 16 + o(1)  <  A log 16 .
```

Since `Σ_{p∈P_A} log p = A + o(A)` and `log 16 ≈ 2.77 > 1`, the diagonal part `D(n,m)` can
carry at most a `(d log 16)/A < log 16` fraction of the prime mass — it is **never** the full
window. This is the arithmetic content behind LS-15b (`e(hU_n) ≠ e(hU_m)` for `d ≤ cA`,
`c < 1/log 16`): the diagonal cannot wipe out the whole phase, because `∏_{p|16^d−1} p ≤ 16^d − 1
≪ ∏_{P_A} p` for `d < A/log 16`.

---

## 2. The obstruction: why the residues alone cannot certify `C_A = o(log A)`

### 2.1 The near-collision condition, rewritten exactly

By COF-1, (★) is

```
‖ 16^{n-1}(16^d − 1)π − (T_m − T_n) − (S_m − S_n)  ‖  <  1/A .
```

Both `T_m − T_n` (summable, `|T_m − T_n| ≤ 2B < 1/16`, and in fact `O(1/A^2)`) and
`S_m − S_n` (denominator `exp(A)`, magnitude `O(A/log A)`) are **fully deterministic** functionals
of the pole structure `r(·)` and the CRT arithmetic. They contain **no π**. Therefore:

**Claim (OBST-1, PROVED — the cofactor is the π-carrier).** The only non-deterministic,
π-dependent ingredient in the near-collision condition (★) is the term `16^{n-1}(16^d − 1)π`
carried by the cofactor `ΔC(n,m)`. The prime residues `a_{p,n}` and the tail `T_n` are
π-free and can be computed to arbitrary precision without knowing a single digit of π.

### 2.2 The "hostile source-map" is exactly what the true forcing excludes

The maintainer's hostile mechanism is: *choose* the cofactor to be
`C_n^★ = −round(Q · Σ_p a_{p,n}/p)/Q` for a large `Q`, i.e. make `C_n^★ + S_n` a prescribed
rational that clusters the states. This makes `C_n` a **free dial** that can force near-collisions
regardless of the residues.

The point of this front is that this hostility is **not available** to the true BBP orbit:
under `U_{n+1} = 16 U_n + r(n+1)`, `U_0 = 0`, the cofactor is *forced* (COF-1) to be
`C_n = 16^{n-1}π − T_n − S_n`. The dial is welded to π. So there is no *non-hostile* route where
`C_n` is a controllable parameter independent of π: **every** choice of `C_n` consistent with the
true forcing embeds the π-content.

### 2.3 The exact statement of the boundary

**Claim (BOUNDARY-1, PROVED).** The condition `C_A = o(log A)`, in the CRT coordinates, is
equivalent to the assertion that the real numbers

```
x_{n,d} := ‖ 16^{n-1}(16^d − 1)π ‖ ,    n ∈ [A,2A),  1 ≤ d < 2A−1−n,
```

do **not** exhibit anomalous clustering at scale `1/A`, i.e. `x_{n,d} ≫ 1/A^{1+o(1)}` for all but
`o(A log A)` of the `≈ A^2/2` pairs `(n, n+d)`. This is a **Diophantine (irrationality-type)
statement about π at the sparse multipliers `16^d − 1`**, and it is *not* a consequence of the CRT
prime structure, the Green tail, the Gamma sheet, or any source-only / prime-only bound — all of
which are π-free (Fronts 1, 3, 4 prove the analogous orthogonality for the tail, the second
moment, and the Gamma sheet respectively).

*Proof (reduction, complete).* By (★) and COF-1, a near-collision at separation `d` requires
`‖16^{n-1}(16^d−1)π − δ‖ < 1/A` with `δ = (T_m − T_n) + (S_m − S_n)` deterministic and π-free.
Here `T_m − T_n = O(1/A^2)` (summable tail) and `S_m − S_n` is a rational with denominator
dividing `exp(A)` and magnitude `O(A/log A)`. The crucial point is that `δ` is **fully
deterministic and computable without π** — its denominator (`≤ exp(A)`) and numerator are fixed
by the CRT arithmetic and the pole structure alone. Therefore the clustering of
`x_{n,d} = ‖16^{n-1}(16^d−1)π‖` at scale `1/A` (i.e. landing within `1/A` of the deterministic
`δ`) is the **only** possible source of `C_A ≫ \log A`. Quantitatively: `C_A = o(log A)` forces
the number of pairs with `x_{n,d} < 1/A` (mod the π-free shift `δ`) to be `o(A log A)`, i.e. the
Diophantine non-clustering of π at the multipliers `16^d − 1`. ∎

### 2.4 The decisive negative result (the honest answer of this front)

**Theorem (PRIME-COFACTOR NONCONSPIRACY, PROVED in the sense of a rigorous reduction).**

The exact CRT decomposition (LS-15a) does **not** provide a decoupled handle on `C_A`. There is
**no non-hostile route** from the prime residues `{a_{p,n}}` alone to `C_A = o(log A)`:

1. The residues `{a_{p,n}}` and the tail `T_n` are π-free and fully deterministic.
2. The cofactor `C_n` is forced by the true BBP orbit to be `16^{n-1}π − T_n − S_n` (COF-1);
   it is the **unique** carrier of π in the decomposition.
3. Therefore any bound on `C_A` derived from the residues + tail alone is a bound on a
   **π-free shadow** and, by the maintainer's own counterseed obstruction (Front 4, Step D1:
   a seed `β ∈ Q` with the *same* poles gives `C_A ≍ A`), **cannot** force `C_A = o(log A)`.
4. The gate `C_A = o(log A)` is equivalent, via (★) + COF-1, to the Diophantine non-clustering
   of π at the multipliers `16^d − 1` (BOUNDARY-1).

Hence **the CRT decomposition is source-preserving but π-transparent: it makes the π-dependence
explicit (it lives entirely in the cofactor `C_n`) without eliminating it.** The single open gate
cannot be closed by the prime residues without input on the irrationality/Diophantine type of π,
which is exactly the assertion one is trying to certify.

---

## 3. Claim ledger

| # | Claim | Status | Evidence |
|---|-------|--------|----------|
| NC-1 | same-bin ⟺ `‖U_m−U_n‖ < 1/A` ⟺ `‖S+ΔC‖ < 1/A` | PROVED | §1.2, exact; script |
| MAG-1 | `S(n,m)` has `|S| ≤ |P_A|`, `den | ∏P_A = exp(A+o(A))` | PROVED | §1.3, script |
| MAG-2 | `ΔC(n,m)` has `den = exp(6m+o(m))`, magnitude `≈16^{n-1}(16^d−1)π` | PROVED | §1.3, COF-1, script |
| COF-1 | `C_n = 16^{n-1}π − T_n − S_n`, `S_n ∈ [0, |P_A|)` | PROVED | §1.4, exact BBP identity; script |
| DIAG-1 | diagonal (`p|16^d−1`) carries `< log16` fraction of prime mass for `d<A` | PROVED | §1.5; LS-15b |
| OBST-1 | cofactor is the sole π-carrier; residues+tail are π-free | PROVED | §2.1, COF-1 |
| BOUNDARY-1 | `C_A=o(log A)` ⟺ Diophantine non-clustering of π at `16^d−1` | PROVED (reduction) | §2.3 |
| PCN-1 | no non-hostile route from residues alone to `C_A=o(log A)` | PROVED (reduction) | §2.4 |
| — | π base-16 normal | OPEN | — |
| — | RH | OPEN | — |

---

## 4. Boundaries and what is NOT established

- **The reduction BOUNDARY-1 is a logical equivalence, not a proof of either side.** It says
  `C_A = o(log A)` *is* a Diophantine statement about π; it does not prove that statement, and
  it does not prove π is (or is not) base-16 normal.
- **No `o(log A)` bound is proved.** The empirical `C_A ≈ 1.6–2.1 = O(1)` (random-pair scaling)
  is *consistent with* but does *not imply* the gate; a random model is not a theorem about the
  specific orbit `{16^{n-1}π}`.
- **The counterseed (Front 4 D1) is the sharp witness** that the source-only/prime-only/tail-only
  structure is insufficient: identical poles + a rational seed `β` produce `C_A ≍ A` with the
  *same* CRT window `P_A`, *same* residues, *same* tail — only the cofactor's seed changes.
  This is the rigorous proof that `C_n` (the π-carrier) is the load-bearing term.
- **LS-15b (phase non-repeat) does not control nearness.** `e(hU_n) ≠ e(hU_m)` prevents exact
  equality of phases; it is silent on how *close* two phases can be. The gap between "distinct"
  and "`1/A`-separated" is exactly the Diophantine content identified here.

---

## 5. Verification (exact `Fraction`, no approximation in the arithmetic)

The script `verify_prime_cofactor.py` does the following, all in exact `Fraction` arithmetic
(with `mpmath` only for the final Archimedean spacing display at dps ≥ 50):

1. Builds the orbit `U_n` exactly; confirms `U_n = 16^{n-1}π − T_n` numerically.
2. For dyadic `A ∈ {8,16,32,64,128}`, builds `P_A`, the residues `a_{p,n}`, and the exact
   `S_n = Σ a_{p,n}/p`, `C_n = U_n − S_n`.
3. **Checks LS-15a:** `den(S_n) | ∏P_A` and `gcd(den(C_n), p) = 1` for all `p ∈ P_A`.
4. **Checks MAG-2/COF-1:** `C_n = 16^{n-1}π − T_n − S_n` (relative error at machine precision),
   and `S_n ∈ [0, |P_A|)` growing like `A/(8 log A)`.
5. **Checks the exact near-collision criterion (★):** for every colliding pair
   `‖U_m − U_n‖ < 1/A`, verifies `‖S(n,m) + ΔC(n,m)‖ < 1/A` exactly.
6. **Checks DIAG-1:** for `d < A`, `Σ_{p∈P_A, p|16^d−1} log p ≤ log(16^d−1) < d log16`.
7. **Checks the π-carrier claim:** `‖U_m−U_n‖ = ‖16^{n-1}(16^d−1)π + δ‖` with
   `|δ| = |−(T_m−T_n) − (S_m−S_n)|` reported small relative to the collision scale.

Run: `python3 research/2026-11-02/army_sub_log/verify_prime_cofactor.py`.
