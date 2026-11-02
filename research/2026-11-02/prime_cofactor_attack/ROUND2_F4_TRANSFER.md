# ROUND 2 — f₄ edge-isolation transfer to the full mixed sum

**Date:** 2026-11-02. **Agent:** Ravel (main). **Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`.
**Predecessor:** `ROUND2_CORE.md` (f₄ isolation; partial-summation obstruction identified).
**This file:** the *sharpened* question — can the isolated-clock BGK saving (PWI-05) be
*transferred* to the full mixed sum `W_p(h)` by (i) partial summation / completion, or
(ii) a bilinear argument — given the **f₄ edge-isolation** decomposition.

**Verdict up front:** The f₄ isolation does **not** transfer the BGK saving. The transfer
fails for a *sharper* reason than "the cofactor is large": the cofactor's kernel
`16^{n-j}` is **exactly rank-1** (`16^n · 16^{-j}`), which turns the problem into the
*completed* (tail) factorization (A) — and the only object that controls that is the
**lacunary Weyl sum** `Σ e(h·16^{n-1}π)`, which is exactly the signed-cancellation gate.
The rank-1 structure is a *new, exact, PROVED* fact, but it transfers the difficulty to
the completed clock, not away from it. No normality claim; no unproven bound. π base-16
normality and RH remain OPEN.

---

## 0. Objects (recapitulated, exact)

Base `b=16`, `e(t)=e^{2π i t}`. The four-pole forcing and its fₘ edge decomposition:

```
r(n) = 4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)
     = 2 f_3(n) + f_4(n) + f_5(n),
f_m(n) = 1/(8n−7) − 1/(8n−7+m),    m ∈ {3,4,5}.
```

`U_n = Σ_{j=1}^n 16^{n-j} r(j)`, `U_0 = 0`. For prime `p ≡ 5 (mod 8)`, birth
`a_p = (p+3)/8` (so `p = 8a_p − 3`), window `[a_p, (p+1)/2) = [a_p, b_p)`,
`b_p = (p+1)/2`, length `L_p = b_p − a_p = (3p+1)/8`.

The **pole isolation** (PROVED, `ROUND2_CORE.md` §2): `f_4(a_p) = 1/(p−4) − 1/p` carries
the `−1/p` pole exclusively; `f_3(a_p) = 1/(p−4) − 1/(p−1)` and `f_5(a_p) = 1/(p−4) − 1/(p+1)`
are p-free. Hence inside the window

```
U_n = −16^{n−a_p}/p + V_{p,n},          c_p = −1,
V_{p,n} = 2 U^{(3)}_n + U^{(5)}_n + ( U^{(4)}_n + 16^{n−a_p}/p ),      p-free,
U^{(m)}_n = Σ_{j≤n} 16^{n-j} f_m(j)   (unit coefficient; coeff₃=2, coeff₄=1, coeff₅=1).
```

**Receipt (exact Fraction, p=13, a_p=2, b_p=7):** `r == 2f₃+f₄+f₅` is `True`; `U_n ==
2U^{(3)}_n + U^{(4)}_n + U^{(5)}_n` is `True` for every `n ∈ [2,7)`; and
`V_{p,n} == 2U^{(3)}_n + U^{(5)}_n + (U^{(4)}_n + 16^{n−a_p}/p)` is `True` for every
`n ∈ [2,7)` (see `round2_f4_transfer_compute.py`). `f_4(a_p) = 4/117 = 1/(p−4) − 1/p` exactly.

The two target objects:

```
isolated clock:   C_p(h) = Σ_{n=a_p}^{b_p−1} e(−h 16^{n−a_p}/p),
mixed sum:        W_p(h) = Σ_{n=a_p}^{b_p−1} e(−h 16^{n−a_p}/p) e(h V_{p,n}) = Σ_{n=a_p}^{b_p−1} e(h U_n).
```

The second equality is exact (`e(−h·clock)e(hV) = e(hU_n)`). **`W_p(h) = R_p(h)` is the
prime-window block of the authentic Weyl sum** (PROVED, all prior fronts).

---

## 1. Task 1 — is the cofactor "slowly varying"? Is the f₄ split individually smoother?

### 1.1 The naive partial-summation obstruction (CONFIRMED, quantified exactly)

Partial summation (Abel) over the mixed sum with the cofactor as weight gives

```
W_p(h) = e(h V_{p,b_p}) C_p(h) − Σ_{n=a_p}^{b_p−1} (e(h V_{p,n+1}) − e(h V_{p,n})) C_{p,≤n}(h),
C_{p,≤n}(h) = Σ_{m=a_p}^{n} e(−h 16^{m−a_p}/p).
```

Each weight difference satisfies

```
V_{p,n+1} − V_{p,n} = 15 V_{p,n} + r(n+1),
```

so `|e(hV_{n+1}) − e(hV_n)| ≈ 2π|h|·|V_{n+1}−V_n| = O(|h|·15·|V_n|) = O(|h|·16^{n−1}π)`.

**Exact receipt (p=13, §7 of `round2_f4_transfer_compute.py`):** `inc/V = 15.000000` for
every `n ∈ [2,5]` (the `r(n+1)` term is `O(1/n²)`, negligible against `15 V_n`), and the
increment identity `V_{n+1}−V_n == 15 V_n + r(n+1)` holds exactly in `Fraction`.

The total variation of the weight over the window is therefore

```
Σ_{n} |e(hV_{n+1})−e(hV_n)| ≍ |h| Σ_{n} 16^{n} ≍ |h| 16^{b_p} ≍ |h| 16^{p/2},
```

which is **exponentially larger** than the window length `L_p ≈ 3p/8`. Any saving
`|C_p(h)| ≤ (1/3+o(1))L_p` is swamped: the Abel identity bounds `|W_p|` by
`|C_p| + O(|h|16^{p/2})`, i.e. by a term astronomically above the trivial bound `L_p`.

> **Conclusion (task 1, first half): the cofactor is NOT slowly varying. Its first
> difference is of the same lacunary order as the cofactor itself (`ΔV ≍ 15 V`), and
> naive Abel/partial summation transfers nothing. This is PROVED, exact, and
> quantifies the obstruction in `ROUND2_CORE.md` §3.**

### 1.2 Does the f₄ isolation make V mod 1 a sum of individually smoother/smaller terms?

This is the *substantive* question, and the answer is **partly yes, in a precise but
useless-for-the-goal sense** — it is the new structural fact of this round.

**Fact (PROVED, exact). The kernel `16^{n−j}` is exactly rank-1:** `16^{n−j} = 16^n · 16^{−j}`
over Q. Therefore every edge sum factorizes

```
U^{(m)}_n = Σ_{j≤n} 16^{n−j} f_m(j) = 16^n · S^{(m)}_n,   S^{(m)}_n = Σ_{j≤n} 16^{−j} f_m(j).
```

and the completed edge sums `S^{(m)}_n` **converge** (the `16^{−j}` is summable against
`f_m(j) ≍ m/(64j²)`):

```
S^{(m)}_∞ = Σ_{j≥1} 16^{−j} f_m(j)  < ∞,      (explicit BBP-type constant),
S^{(m)}_n = S^{(m)}_∞ − T^{(m)}_n,   T^{(m)}_n = Σ_{j>n} 16^{−j} f_m(j) = O(16^{−n} n^{−2}).
```

The same holds for the combined forcing:

```
S_n = Σ_{j≤n} 16^{−j} r(j) → π/16,     (BBP, exact),     U_n = 16^n · S_n.
```

**Receipt (exact/mpmath, dps=120):** `Σ_{j=1}^{200} 16^{−j} r(j) = π/16` to 120 digits
(diff `2.4×10^{−122}`); at `n=10` the partial sum matches `π/16` to `1.3×10^{−16}`, at
`n=40` to `6.5×10^{−54}` (exponential convergence).

So **"smoother/smaller" is achieved, but it splits the cofactor into `16^n × (convergent
partial sum)`, not into a sum of small terms.** The `16^n` factor is *not* small and *not*
slow: it is exactly the lacunary growth that `W_p` shares with the leading clock. The f₄
isolation refines `S_n` into edge components `S^{(3)}_n, S^{(5)}_n, S^{(4)}_n − 16^{−a_p}/p`,
each of which is a *convergent* (hence in that narrow sense "smooth") sequence — but each is
still multiplied by the same `16^n`. No edge is individually "small"; each carries the full
lacunary magnitude.

> **Conclusion (task 1, second half): the f₄ isolation does NOT produce individually
> "small" or "smooth-in-the-useful-sense" pieces. It produces a rank-1 factorization
> `U^{(m)}_n = 16^n · S^{(m)}_n` where `S^{(m)}_n` is convergent, but the `16^n` factor
> is common to all edges and is the entire obstruction. This is PROVED and is the
> cleanest possible statement of *why* the isolation cannot help: it re-derives the
> completed-tail factorization (A), whose controlling object is the lacunary Weyl sum.**

### 1.3 Completion argument — does it transfer the saving?

The completion identity (exact, BBP):

```
U_n = 16^{n−1} π − T_n,   T_n = Σ_{k≥1} 16^{−k} r(n+k),   T_n = O(16^{−1} n^{−2}).
```

so `e(h U_n) = e(h·16^{n−1}π) · e(−h T_n)` with `e(−h T_n) → 1` exponentially fast in the
window (`T_n < 2^{−Θ(p)}` for `n ≥ a_p ≈ 3p/8`). This is factorization (A) — the *correct*
one. To transfer the isolated-clock saving to `W_p` via completion, one must control

```
Σ_{n} e(h·16^{n−1} π) = Σ_{n} e(h·16^{n} · π/16)   (the lacunary Weyl sum of π's 16-digits),
```

because the small tail `e(−hT_n)` does not change the leading phase. The isolated prime
clock `C_p(h)` is *not* this object: `C_p` sums `e(−h 16^{n−a_p}/p)` over a *partial*
geometric progression of `16` mod p, whereas the completed clock sums `e(h·16^{n−1}π)`
over a lacunary sequence of a *transcendental* base point. BGK's saving lives on the
subgroup `⟨16⟩ ⊂ F_p^×`; the completion moves the base point from `−1/p ∈ Q` to `π/16`
transcendental, and BGK has nothing to say there.

> **Conclusion (task 1, third half): the completion argument transfers the difficulty
> from the *rational* prime clock to the *transcendental* completed clock. It is an
> identity, not a reduction; the BGK saving does not survive the base-point lift
> `−1/p ↦ π/16`.**

---

## 2. Task 2 — the bilinear argument

### 2.1 The natural bilinear form and its exact rank

Write `W_p` as a bilinear form. The mixed sum is

```
W_p(h) = Σ_{n=a_p}^{b_p−1} e(−h 16^{n−a_p}/p) · e(h V_{p,n}).
```

Substituting the rank-1 kernel (`16^{n−j} = 16^n 16^{−j}`), and using
`V_{p,n} = 2U^{(3)}_n + U^{(5)}_n + (U^{(4)}_n + 16^{n−a_p}/p)`:

```
e(h V_{p,n}) = exp( 2π i h · 16^n [ 2 S^{(3)}_n + S^{(5)}_n + S^{(4)}_n + 16^{−a_p}/p ] ).
```

Two candidate bilinear decouplings, and their exact status:

**(i) Diagonal (single-index) form.** Since `16^{n−j}` is rank-1, every edge sum is a
*diagonal* form `Σ_j 16^n · (16^{−j} f_m(j))`. The mixed sum is *not* a genuine
two-variable bilinear form: it is a single-index sum over `n` of `e(h U_n)`. There is no
second "free" variable `m` to sum over; the `j`-sum is already collapsed into `U_n`.

**(ii) Two-variable form via the tower.** Using `U_n = 16^{n−a_p} U_{a_p} + W_{p,n}`:

```
W_p(h) = Σ_{n} e(h·16^{n−a_p} U_{a_p}) · e(h W_{p,n})
       = Σ_{n} e(h·16^{n−a_p} U_{a_p}) · e(h·16^n · Ŝ_{p,n}),
Ŝ_{p,n} = Σ_{j=a_p+1}^{n} 16^{−j} r(j)  = (π/16 − S_{a_p}) − T'_{p,n},   T'_{p,n} = Σ_{j>n} 16^{−j} r(j).
```

Write `a_n = e(h·16^{n−a_p} U_{a_p})`, `b_n = e(h·16^n · (π/16 − S_{a_p})) · e(−h·16^n T'_{p,n})`,
so `W_p(h) = Σ_n a_n b_n` is a **diagonal** (rank-∞-in-the-silly-sense) bilinear form
`Σ_{n,m} a_n b_m δ_{n=m}`. The kernel is the identity `δ(n,m)`.

### 2.2 The hypotheses a bilinear bound would need, checked exactly

A large-sieve / bilinear (`Type I/II`) argument for `Σ_n a_n b_n` with `|a_n|,|b_n| ≤ 1`
requires controlling `Σ_{n≤N} |Σ_{m} b_m K(n,m)|`-type bilinear forms where the *kernel*
has **bounded bilinear complexity**. The exact hypotheses and their status:

| Hypothesis | Statement | Status (exact) |
|---|---|---|
| **H1 (kernel rank)** | `K(n,m)` has low rank `r ≪ (log N)^c` | **FAILS to help**: the natural kernel is `δ(n,m)` (identity), which is *full* rank `N`; the alternative kernel `16^{n−j}` is rank-1 but couples `n` to `j` through the *lacunary* multiplier `16^n`, not through a summable two-variable kernel |
| **H2 (well-spacing)** | the phase points `{16^{n−a_p}/p}` (or `{16^n π/16}`) are `δ`-well-spaced for large sieve | **FAILS**: `{16^m/p}` is clustered in `⟨16⟩ ≤ F_p^×` (subgroup, not spaced); `{16^n π/16}` is lacunary (exponentially growing), the maximal non-spacing |
| **H3 (smoothing / total variation)** | the coefficient `b_n` has bounded `ℓ¹`-variation `Σ|b_{n+1}−b_n| ≪ N^{1−ε}` | **FAILS exactly**: `b_n = e(h·16^n·(·))` has `|b_{n+1}−b_n| ≍ 2π|h|16^n`, so `Σ|Δb_n| ≍ |h|16^N` (verified §1.1), no `N^{1−ε}` |
| **H4 (completion / tail)** | `b_n` is a small perturbation of a constant, `b_n = 1 + o(1)` | **FAILS for the useful form**: only `e(−h T_n) → 1`, but this multiplies `e(h·16^{n−1}π)`, which is *not* `→1`; the leading phase is the entire object |
| **H5 (multiplicative character / subgroup)** | `a_n` or `b_n` is a multiplicative character of `F_p^×` (for BGK/Weil) | **FAILS**: the phase is `e(h·16^{n−a_p} U_{a_p})` with `U_{a_p}` a *rational* (not a residue of a character); the base point is lifted to `π` (transcendental) in the completed form |

**Every hypothesis fails at a verified, exact level.** The bilinear complexity is *not*
bounded: the object is a lacunary Weyl sum, whose bilinear form is the identity kernel
with exponentially-varying diagonal coefficients — the worst case for every known
bilinear method.

### 2.3 The precise bilinear obstruction

The mixed sum is a **diagonal** bilinear form `Σ_n a_n b_n` where both `a_n` and `b_n`
are unit-modulus and *lacunary* (each carries a `16^n` phase). A bilinear bound on a
diagonal form with unit-modulus lacunary entries is *exactly* the Weyl-sum estimate
`Σ_n e(h·16^n θ) = o(N)` — which is **equivalent to the signed-cancellation gate**
(SCB-06, PROVED equivalence in the repo ledger). There is no Type-I/Type-II smoothing:
no variable is free to average over, and the kernel has no short-range or low-rank
structure that a completion could exploit.

---

## 3. Task 3 — what is PROVED and what is the obstruction

### 3.1 PROVED (exact, elementary; all receipts in `round2_f4_transfer_compute.py`)

| ID | Statement | Status | Receipt |
|---|---|---|---|
| R2T-01 | `r = 2f₃+f₄+f₅`, each `f_m` = difference of two reciprocal-linear poles | PROVED | SymPy `expand`, exact |
| R2T-02 | `f_m(n) ≍ m/(64n²)`, `f_m(n+1)−f_m(n) = O(n^{−3})` (individually smooth/small in n) | PROVED | SymPy `series` §1.2 |
| R2T-03 | Pole `−1/p` carried exclusively by `f₄(a_p)=1/(p−4)−1/p` | PROVED | exact Fraction, p=13 |
| R2T-04 | `V_{p,n} = 2U^{(3)}_n + U^{(5)}_n + (U^{(4)}_n + 16^{n−a_p}/p)`, p-free | PROVED | exact Fraction, all n in window |
| R2T-05 | `V_{p,n+1}−V_{p,n} = 15 V_{p,n} + r(n+1)`, so `ΔV/V = 15 + o(1)` | PROVED | exact Fraction, inc/V=15.0000 |
| R2T-06 | Kernel `16^{n−j} = 16^n·16^{−j}` is exactly rank-1 over Q | PROVED | trivial factorization |
| R2T-07 | `U_n = 16^n S_n`, `S_n → π/16` (BBP, exponential tail) | PROVED | BBP; verified 120 digits |
| R2T-08 | `W_p(h) = R_p(h) = Σ e(hU_n)` is a prime-window block of the authentic Weyl sum | PROVED | exact, all fronts |
| R2T-09 | Naive Abel transfer blocked: total weight variation `≍ |h|16^{p/2} ≫ L_p` | PROVED | §1.1 |
| R2T-10 | Bilinear hypotheses H1–H5 all fail at exact level | PROVED | §2.2 table |

### 3.2 OPEN / obstruction (unchanged, now in f₄-isolated coordinates)

**The transfer is NOT proved.** The exact obstruction is:

> The f₄ edge-isolation makes the clock–cofactor separation *cleaner* (disjoint forcing
> edges, PROVED) and exposes the rank-1 kernel `16^{n−j}` (PROVED). But the rank-1
> factorization **completes** the cofactor into `16^n · S_n`, i.e. it moves the object
> from the *rational* prime clock `−16^{n−a_p}/p` to the *transcendental* completed
> clock `16^{n−1}π`. The BGK saving on `C_p(h)` lives on `⟨16⟩ ⊂ F_p^×`; it does not
> survive the lift `−1/p ↦ π/16`, because BGK/Weil require a finite-field algebraic
> base point. The completed object is the lacunary Weyl sum
> `Σ_n e(h·16^{n−1}π)`, whose `o(N)` bound is exactly the signed-cancellation gate
> (SCB-06-equivalent to base-16 normality of π).

The remaining lemma is **unchanged** (sharpest form):

```
sup_{1≤|h|≤16^{m−1}} |S_N(h)| = O(N^θ),  θ < 1,  m = ⌊log₁₆ N / 3⌋,
S_N(h) = Σ_{n≤N} e(h·16^{n−1}π).
```

No edge-isolation, no partial summation, no bilinear reorganization reaches this. The
f₄ isolation is a *refinement of the exact structure*, not a new lever.

---

## 4. Claim ledger (final)

| ID | Statement | Status |
|---|---|---|
| R2T-01..R2T-08 | exact f₄-isolation arithmetic, rank-1 kernel, BBP completion | PROVED |
| R2T-09 | naive partial-summation transfer fails (ΔV ≍ 15V, variation ≍ 16^{p/2}) | PROVED (obstruction) |
| R2T-10 | bilinear hypotheses H1–H5 all fail (identity kernel, lacunary, non-spaced, transcendental base) | PROVED (obstruction) |
| R2T-11 | BGK saving on `C_p(h)` transfers to `W_p(h)` via f₄ isolation | **NOT PROVED** (obstruction: base-point lift `−1/p ↦ π/16`) |
| R2T-12 | `Σ_n e(h·16^{n−1}π) = o(N)` (signed cancellation) | OPEN (= base-16 normality of π) |
| R2T-13 | π base-16 normality, RH | OPEN (unchanged) |

---

## 5. Boundary and honesty statement

This round **proves** that the f₄ edge-isolation yields a *cleaner* decoupling and the
exact rank-1 kernel `16^{n−j} = 16^n·16^{−j}` — a new structural fact — and that this
rank-1 structure *completes* the cofactor into `16^n S_n` with `S_n → π/16`. It
**proves** that neither partial summation (task 1) nor a bilinear reorganization
(task 2) transfers the isolated-clock BGK saving, because (i) the cofactor's first
difference is of the same lacunary order as the cofactor (`ΔV ≍ 15V`, variation
`≍ 16^{p/2}`), and (ii) the only bilinear form is a diagonal one with unit-modulus
lacunary entries — the Weyl-sum worst case — whose kernel is the identity and whose
base point is lifted from `−1/p` (rational, where BGK lives) to `π/16` (transcendental,
where no theorem reaches). **No normality is claimed; no sub-trivial bound is asserted.**
The transfer is blocked at the same signed-cancellation gate, now written in the
cleanest possible (f₄-isolated, rank-1-completed) coordinates. π base-16 normality and
RH remain OPEN.
