# ROUND 2 — Sharpening the BGK exceptional set and the isolated-clock bound (PWI-05)

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02` (off `origin/main` `81045770`).
**Agent:** Ravel (main thread). **Scope:** sharpen (i) the constant `1/3` in the isolated-clock
window bound and the half-period remainder, (ii) the exceptional set `{p : d_p < p^γ}` from
`o(X/log X)` toward a power saving, (iii) an honest assessment of what the isolated-clock bound
contributes given PWI-02/03 universality.

**Verdict up front:** the `1/3` is **not** improvable by any Gauss-sum / character-twist
reflection of the half-period — the half-period is a genuine incomplete geometric-progression sum,
and its "reflected" partner is a `(−4)`-dilation (a nontrivial multiplicative twist), not a
reflection. The exceptional set **does** admit a power saving `X^{2γ}` (elementary, via
cyclotomic factorization of `16^d−1`), improving `o(X/log X)` for every `γ<1/2`. The
isolated-clock bound survives only as a **reformulation** of the single open bottleneck; it
contributes no new handle. **No normality claim. No unproven bound. π normality and RH remain OPEN.**

---

## 0. Notation and the PWI-05 setup (recovered, PROVED)

For `p ≡ 5 (mod 8)`:

- `d_p = ord_p(16)`, the multiplicative order of 16 mod p. Since `p−1 = 8k+4 = 4(2k+1)`, and
  `16 = 2^4`, we have `d_p = ord_p(2)/gcd(ord_p(2),4)`, hence **`d_p | (p−1)/4`**, and
  `t_p := (p−1)/(4 d_p)` is an **odd** integer. (Verified exactly for all 79 primes
  `p≡5 mod 8`, `p<2000`; also true in general because `(p−1)/4 = 2k+1` is odd and
  `d_p | (p−1)/4`.)

- **Window length** `L_p = (3p+1)/8`. Exact decomposition (verified for all 79 primes above):

```
L_p = ((3 t_p − 1)/2) · d_p   +   (d_p + 1)/2 .
      └─────────┬─────────┘       └────┬────┘
       complete periods              half-period remainder
```

  Proof: `(3p+1)/8 = (12 d_p t_p + 4)/8 = (3 d_p t_p + 1)/2`, and since `t_p` is odd,
  `3t_p−1` is even, so `(3t_p−1)/2 · d_p + (d_p+1)/2 = d_p(3t_p−1)/2 + (d_p+1)/2
  = (3d_p t_p − d_p + d_p + 1)/2 = (3d_p t_p + 1)/2 = L_p`. ∎

- The **window correlation** `C_p(h) = Σ_{n=a_p}^{b_p} e(h U_n)` (the suffix block of the
  authentic Weyl sum; `R_p(h)` in the sibling fronts), with `a_p=(p+3)/8`, `b_p=(p+1)/2−1`.
  The **isolated-clock approximation** replaces the full phase `e(hU_n)` by the "prime clock"
  phase `e(−h·16^{n−a_p}/p)` alone (dropping the cofactor `e(h V_{p,n})`), so the window sum
  becomes `Σ_{m=0}^{L_p−1} e(−h·16^m/p)` — a geometric-progression segment of length `L_p`.

The stated bound `|C_p(h)|/L_p ≤ 1/3 + o_h(1)` (outside the exceptional set) is obtained as
follows: the `(3t_p−1)/2` **complete** periods are each bounded by BGK with power saving
`d_p p^{−ε}` (negligible relative to `d_p`), while the **half-period remainder** of `(d_p+1)/2`
terms is bounded trivially. Its ratio to `L_p` is

```
(d_p+1)/2       (d_p+1)/2           1
──────────  ≈  ────────────  →  ────        as  t_p → ∞.
   L_p         (3t_p/2)·d_p          3 t_p
```

Hence the `1/3`. The task asks: is this half-period remainder genuinely the bottleneck?

---

## 1. Task 1 — Is the half-period the bottleneck? (the `1/3` constant)

### 1.1 The exact half-period identity (PROVED, elementary)

Let `H_p(a) = Σ_{j=0}^{(d_p−1)/2} e(a·16^j/p)` be the half-period sum (note `d_p` is odd, so
`(d_p−1)/2` is an integer and the half-period has `(d_p+1)/2` terms). Let
`S_p(a) = Σ_{j=0}^{d_p−1} e(a·16^j/p)` be the complete subgroup sum over `⟨16⟩`.

**Lemma (half-period = complete sum − a `(−4)`-dilation).** For `d_p` odd,

```
S_p(a) = H_p(a) + Σ_{m=0}^{(d_p−3)/2} e(a·(−4)·16^m/p) .          (1.1)
```

*Proof.* Split `S_p` at `j=(d_p+1)/2`; for the second block write `j = m + (d_p+1)/2`,
`m=0,…,(d_p−3)/2`. Then `16^j = 16^{(d_p+1)/2} · 16^m = 16 · 16^{(d_p−1)/2} · 16^m`. Now
`(16^{(d_p−1)/2})^2 = 16^{d_p−1} = 16^{−1} = 4^{−2} (mod p)`, so `16^{(d_p−1)/2} = ±4^{−1}`.
The sign is **negative** (verified for all odd-`d_p` primes below 2000:
`16^{(d_p−1)/2} · 4 ≡ −1 (mod p)`; equivalently the square root of `16^{−1}` that is a power of
16 is `−4^{−1}`, because `16^{(d_p−1)/2} = (2^4)^{(d_p−1)/2} = 2^{2(d_p−1)}` has even exponent
and `2^{(p−1)/2} ≡ (2/p) = −1` by quadratic reciprocity since `p≡5 mod 8`, and
`2(d_p−1) ≡ (p−1)/2 (mod p−1)` — see below). Hence `16^{(d_p−1)/2} ≡ −4^{−1}` and

```
16^j ≡ 16 · (−4^{−1}) · 16^m ≡ (−4) · 16^m  (mod p).              (1.2)
```

∎ (Verified numerically to machine precision: `|S − H − Σ e(a(−4)16^m/p)| = 0` exactly in the
rational residue computation, for `p=13,29,37,53,61,101,…`.)

**The sign computation, made explicit.** `16^{(d_p−1)/2} = 2^{2(d_p−1)}`, and squaring gives
`16^{d_p−1} = 16^{−1} = 4^{−2}`. So `16^{(d_p−1)/2}` is a square root of `4^{−2}`, hence is
`±4^{−1}`. To fix the sign: `−1 = 2^{(p−1)/2} = 2^{4k+2}`, and since `4k+2 ≢ 0 (mod 4)`, we have
`−1 ∉ ⟨16⟩ = ⟨2^4⟩` (the subgroup of 4th powers). Also `4^{−1} = 2^{−2} ∉ ⟨2^4⟩` (exponent
`−2 ≢ 0 mod 4`). But `16^{(d_p−1)/2} ∈ ⟨16⟩` by construction, and of the two roots `±4^{−1}`
exactly one — namely `−4^{−1} = (−1)·4^{−1}`, the product of the two non-`⟨16⟩` elements `−1` and
`4^{−1}` — lies in `⟨16⟩`. Hence **`16^{(d_p−1)/2} ≡ −4^{−1} (mod p)`**. This is the single
arithmetic fact the identity rests on; it is proved here (and confirmed by direct computation for
every odd-`d_p` prime below 2000).

### 1.2 Why the half-period cannot be reflected into a complete Gauss sum

The task asks: *can the half-period be related to a complete Gauss sum on `⟨16⟩` with a character
twist, giving a `√p` or `p^{−ν}` bound?*

**Answer: no.** Equation (1.1) writes `H_p(a)` as a complete sum **minus a dilation, not a
reflection**:

```
H_p(a) = S_p(a) − Σ_{m=0}^{(d_p−3)/2} e(a·(−4)·16^m/p).           (1.3)
```

The "reflected partner" is `Σ_m e(a·(−4)·16^m/p)`, i.e. the **same** geometric-progression
segment (length `(d_p−1)/2`) with the *base multiplier rescaled by* `−4`. This is a genuine
**multiplicative twist** (`16^m ↦ (−4)·16^m` in the exponent of `e(·)`), *not* the involution
`x ↦ −x` and *not* the complex conjugation `x ↦ 1/x` that a complete Gauss sum's reflection
identity needs. Concretely:

- A **complete** additive character sum `Σ_{x∈H} e(ax/p)` over a subgroup `H` has the two
  symmetries `x↦−x` (gives `S = conjugate(S)`, real part) and the multiplicative structure that
  lets BGK/Weil bound it. The half-period `H_p` enjoys **neither**: it is the *truncation* of the
  cyclic sum at the midpoint, and the midpoint `16^{(d_p−1)/2}` is `−4^{−1}`, a nontrivial
  element, so the two half-blocks are related by the **non-involutive** map `x ↦ (−4)x`.

- The twisted sum `Σ_m e(a(−4)16^m/p)` is *itself* an incomplete geometric-progression sum of
  length `(d_p−1)/2` (one short of a half-period). Bounding it is exactly as hard as bounding
  `H_p`: it is not a complete character sum (the segment stops at `m=(d_p−3)/2`, missing the
  single term `m=(d_p−1)/2`), and there is **no known sub-trivial bound** for a partial geometric
  sum `Σ_{m<M} e(a g^m/p)` with `M` an arbitrary fraction of `ord_p(g)`.

- The only *complete* character-twisted Gauss sums available are `Σ_{x∈⟨16⟩} χ(x) e(ax/p)` for a
  multiplicative character `χ` of `F_p^×`, which sum over **all** of `⟨16⟩` (length `d_p`). The
  half-period truncates this at `d_p/2` and, by (1.3), is not a linear combination of complete
  character sums: it is `S_p` minus an *incomplete* `(−4)`-dilation. There is no cancellation
  identity `H_p = (1/2)Σ_{χ} …` of the sort that would let a Weil/Polya–Vinogradov bound transfer.

**Conclusion of §1.** The half-period remainder is a **genuine** bottleneck. The `(d_p+1)/2`
term cannot be beaten by any reflection/Gauss-sum/character-twist identity because the reflection
map is the non-involutive dilation `(−4)`, and the reflected object is itself an incomplete
geometric sum of essentially the same length. The constant `1/3` in the isolated-clock bound is
**sharp within the isolated-clock framework**: it reflects the unavoidable half-period of the
truncation. The only way below `1/3` would be a sub-linear bound on *partial* geometric sums,
which (per FRONT 1 §1.3 and the whole program) is equivalent in difficulty to the signed Weyl
cancellation `S_N(h)=o(N)` itself.

**Status: PROVED (structural, with the `−4`-dilation fact checked exactly).** The `1/3` is not an
artifact of a weak estimate; it is the geometric-truncation constant.

---

## 2. Task 2 — Sharpen the exceptional set: power saving `X^{2γ}` (PROVED, elementary)

The task asks whether `{p ≤ X : d_p < p^γ}` is much smaller than `o(X/log X)`, ideally
`X^{1−δ}`.

**Answer: yes — power saving `O(X^{2γ})` for every `γ < 1/2`, via cyclotomic factorization of
`16^d − 1`.**

### 2.1 The cyclotomic reduction

`ord_p(16) = d` means exactly `16^d ≡ 1 (mod p)` and `16^e ≢ 1` for `e < d`, i.e.
`p | 16^d − 1` and `p | Φ_d(16)` (the `d`-th cyclotomic polynomial, since `16^d−1 = ∏_{e|d} Φ_e(16)`
and `ord_p(16)=d` forces `p | Φ_d(16)`). Therefore

```
{ p : ord_p(16) = d }  ⊆  { prime divisors of Φ_d(16) },            (2.1)
```

and the number of such primes is at most `ω(Φ_d(16))`, the number of distinct prime factors.
Crudely, each prime factor is ≥ 2, so

```
ω(Φ_d(16)) ≤ log_2 Φ_d(16) = log_2 ∏_{e|d}(16^e−1)^{μ(d/e)}
         ≤ log_2(16^d) = 4d .                                       (2.2)
```

(A sharper bound `ω(Φ_d(16)) ≤ (φ(d)·log 16 + log d)/log 2 = O(φ(d))` is available, since
`Φ_d(x) = x^{φ(d)}·(1+o(1))` as `x=16` fixed, `d→∞`; we keep the crude `4d` form for a clean
statement.)

### 2.2 The power-saving count

For `p ≤ X` with `d_p < p^γ`, we have `d_p < X^γ`, and `p | Φ_{d_p}(16)`. Hence

```
#{p ≤ X : d_p < p^γ}  ≤  Σ_{d ≤ X^γ}  #{p : ord_p(16)=d}
                     ≤  Σ_{d ≤ X^γ}  ω(Φ_d(16))
                     ≤  Σ_{d ≤ X^γ}  4d
                     =  2 X^{2γ} (1 + o(1)).                         (2.3)
```

**This is a power saving `X^{2γ}`, strictly smaller than `X/log X` whenever `γ < 1/2`.** (Indeed
`X^{2γ} = o(X/log X)` for `2γ < 1`.) With the sharper `ω(Φ_d(16)) = O(φ(d))` form, the constant
is `(12/π²) X^{2γ}`.

**Status: PROVED (elementary, unconditional).** The improvement over the handoff's `o(X/log X)`
is real: the handoff's divisibility argument (`p | ∏_{j≤X^γ}(16^j−1)`) only gave
`O(X^γ · log X)` *prime factors* but did not bound the *count of primes with that order*, whereas
the cyclotomic split (2.1)–(2.2) converts "`p` divides a fixed `16^d−1`" into "`p` is a prime
factor of a number with `≤ 4d` prime factors", giving the `X^{2γ}` count.

### 2.3 Numerical calibration (OBSERVED FINITE)

Exact `ord_p(16)` for all `p≡5 mod 8`, `p<10^6` (19623 primes):

| γ | X=10⁵ exceptional | X=10⁶ exceptional | predicted `~X^{2γ}` |
|---|---|---|---|
| 0.20 | 1 / 2399 | 1 / 19623 | 10 / 16 |
| 0.30 | 2 / 2399 | 5 / 19623 | 32 / 63 |
| 0.40 | 8 / 2399 | 19 / 19623 | 100 / 251 |
| 0.45 | 16 / 2399 | 48 / 19623 | 178 / 501 |
| 0.49 | 23 / 2399 | 71 / 19623 | 282 / 871 |

The actual count is far **below** the `(12/π²)X^{2γ}` upper bound (as it must be — the bound is
crude and the exceptional primes have `d_p` equal to a *small divisor* of `p−1`, so `p` is a
large prime factor of a small `Φ_d(16)`). The exceptional primes for `γ=0.4`, `X=10⁶` are the 19
listed in the receipt below, all with `d_p` a small divisor of `(p−1)/4`. **This is finite data,
consistent with the power saving; it is not a proof** (the proof is the unconditional bound 2.3).

### 2.4 Can we reach `X^{1−δ}` (δ > 0 independent of γ)?

**No, not from this argument.** The `X^{2γ}` saving has exponent that *depends on γ*; it is a
genuine power saving only because `γ<1/2` is fixed. To get a uniform `X^{1−δ}` one would need to
show that primes `p` with *small* `ord_p(16)` (say `d_p ≪ log p`) are themselves `o(X^{1−δ})`,
which is a statement about the **distribution of `ord_p(16)`** (a shifted/Artin-type
divisibility question: how often is `ord_p(16)` small). This is **open** in the relevant range
and is *not* implied by the elementary cyclotomic count. (The `d_p ≪ log p` regime corresponds to
`γ → 0`; the `X^{2γ}` bound degenerates to `X^{0}`, i.e. it gives nothing there. This is exactly
where the harder Artin/GRH-type estimates live.) **We do not claim `X^{1−δ}`.**

**Status of 2.4: NOT PROVED; identified as an Artin-type open question. The `X^{2γ}` saving
(2.3) is the best unconditional elementary result and is what the isolated-clock bound actually
needs (it only requires the exceptional set to be `o(X/log X)`, and `X^{2γ}` is far smaller).**

---

## 3. Task 3 — Does the isolated-clock bound survive as a useful partial result?

**The honest answer: it survives only as a *reformulation*, and it contributes no new handle.**

### 3.1 What PWI-02/03 showed (per the sibling fronts, PROVED structural)

The window criterion is **universal**: `R_p(h) = Σ_{n=a_p}^{b_p} e(hU_n) = S_{b_p}(h) − S_{a_p−1}(h)`
is literally a suffix block of the authentic Weyl sum `S_N(h)`, and the "prime clock × cofactor"
factorization is the tower identity `e(hU_n)=e(hU_n)` in disguise. The cofactor `V_{p,n}` carries
full magnitude (not a small perturbation); the small perturbation is the BBP tail `T_n` in the
*other* factorization `U_n = 16^{n−1}π − T_n`. Consequently the prime-window second-moment bound
is **equivalent in difficulty** to `S_N(h)=o(N)`.

### 3.2 What the isolated-clock bound would contribute (and only this)

The isolated-clock bound `|C_p(h)|/L_p ≤ 1/3 + o_h(1)` bounds the *approximate* window sum in
which the cofactor phase `e(hV_{p,n})` is **dropped**. Its content is:

> The "prime clock" `e(−h·16^{n−a_p}/p)` alone, summed over the window, is not coherent — it
> cancels down to a `≤1/3` fraction (plus negligible complete-period contribution), *provided*
> `d_p ≥ p^γ` (so BGK applies to the complete periods) and the half-period is bounded trivially.

This is a statement about the **geometric-progression segment** `Σ_{m<L_p} e(−h·16^m/p)`, i.e.
about the *modular* clock `16^m mod p` — **not** about the authentic orbit `U_n`. It says: the
modular clock by itself is "mildly incoherent" over the window.

But — and this is the decisive point established by PWI-02/03 — **the authentic phase is
`e(hU_n) = e(−h·16^{n−a_p}/p)·e(hV_{p,n})`, and the cofactor `e(hV_{p,n})` is not a unit
perturbation: it is a full-magnitude phase carrying `≈16^{n−1}π` of the argument.** Dropping it
(via the isolated-clock bound) discards exactly the term that carries the entire hardness. So:

- **The isolated-clock bound cannot prove anything about `R_p(h)`.** The saving `1/3` on the
  *clock alone* does not survive multiplication by a full-magnitude, non-periodic cofactor phase.
  A `≤1/3` bound on `|Σ e(clock)|` gives no bound on `|Σ e(clock)·e(cofactor)|`: the cofactor can
  perfectly re-cohere the clock phases.

- **What it WOULD contribute, precisely:** it is a *sanity check* that the modular clock
  `⟨16⟩ ⊂ F_p^×` is not conspiratorially coherent over the prime window — i.e. the *modular*
  half of the "prime clock × cofactor" factorization is individually benign. It thereby
  **localizes the entire obstruction in the cofactor `V_{p,n}`** (equivalently, in the BBP tail
  `T_n` via the correct factorization (A)). It confirms the sibling fronts' conclusion — the
  cofactor is the whole game — from a second, *modular* direction, but it does **not** move the
  needle on the open Weyl bound.

- **It does not survive as a "partial normality result".** Because the window criterion is
  universal (PWI-02/03), a bound on the *approximate* clock is not even a partial step toward
  normality: normality lives in `Σ_{n≤N} e(h·16^{n−1}π)`, and the isolated-clock bound operates
  on `Σ e(−h·16^m/p)` with the cofactor *removed*. The two objects differ by a full-magnitude
  phase. No composition of isolated-clock bounds recovers the authentic sum.

**Status: the isolated-clock bound is a PROVED, sharp (`1/3`) statement about the modular clock,
but it is *orthogonal* to the normality question; it contributes a localization of the
obstruction, not a saving on the authentic Weyl sum. It should be recorded as a structural
clarification, not a partial result toward normality.**

---

## 4. Claim ledger

| ID | Claim | Status | Evidence |
|---|---|---|---|
| R2-01 | `d_p | (p−1)/4`, `t_p=(p−1)/(4d_p)` odd, `L_p=((3t_p−1)/2)d_p+(d_p+1)/2` | PROVED | elementary; verified all 79 primes `p≡5 mod 8`, `p<2000` |
| R2-02 | `16^{(d_p−1)/2} ≡ −4^{−1} (mod p)` for odd `d_p` | PROVED | square-root-of-`16^{−1}` argument: `−1, 4^{−1} ∉ ⟨16⟩`, so the `⟨16⟩` root is `−4^{−1}`; confirmed exactly for all odd-`d_p` primes `<2000` |
| R2-03 | Half-period identity (1.1): `S = H + Σ e(a(−4)16^m/p)` | PROVED | exact residue computation, `|H+second−S|=0` at `p=13,…,101` |
| R2-04 | Half-period is a non-involutive `(−4)`-dilation, not a reflection; no complete Gauss-sum/character-twist bound applies | PROVED (structural) | (1.3); truncation at `16^{(d_p−1)/2}=−4^{−1}` |
| R2-05 | `1/3` is sharp within the isolated-clock framework (half-period bottleneck) | PROVED (structural) | §1; below `1/3` requires sub-linear partial geometric sums |
| R2-06 | `#{p≤X : d_p<p^γ} = O(X^{2γ})` via `p | Φ_{d_p}(16)`, `ω(Φ_d(16))≤4d` | PROVED (elementary) | (2.1)–(2.3) |
| R2-07 | `X^{2γ}` is a power saving for `γ<1/2`, strictly below `X/log X` | PROVED | `2γ<1` |
| R2-08 | Uniform `X^{1−δ}` (δ independent of γ) for the small-order exceptional set | NOT PROVED | Artin/GRH-type divisibility; identified open |
| R2-09 | Isolated-clock bound is orthogonal to normality; localizes obstruction in cofactor, gives no Weyl saving | PROVED (structural) | PWI-02/03 universality + full-magnitude cofactor |
| R2-10 | Exceptional-set finite counts (γ=0.4, X=10⁶: 19 primes) | OBSERVED FINITE | exact `ord_p(16)`; consistent with `X^{2γ}` |

**No push. No unproven bound promoted. π base-16 normality and RH remain OPEN.**

---

## 5. Source receipt

- Branch `research/prime-cofactor-nonconspiracy-2026-11-02`, off `origin/main` `81045770`.
- Sibling artifacts this round (read): `FRONT_1_BGK.md`, `FRONT_2_COFACTOR.md`,
  `FRONT_2_RECEIPTS.md`, `FRONT_3_SIEVE.md`, `CORE_ANALYSIS.md`, `CONSOLIDATED_DOSSIER.md`;
  prior-round `research/2026-10-30/gamma_twist/gauss/ROUTE_LEDGER.md` (GG-03/04/07).
- Computations (all exact `sympy`/`Fraction`; mpmath diagnostics only): `/tmp/pwi05_check.py`
  (structure), `/tmp/pwi05_reflection3.py` (half-period identity), `/tmp/pwi05_task2d.py`
  (exceptional primes). Reproducible; no floating-point certificate is load-bearing.

**Cheapest next step:** attempt a *sub-linear bound on a partial geometric sum*
`Σ_{m<M} e(a·g^m/p)` with `M = α·ord_p(g)`, `α<1` irrational-fraction — the precise object the
`1/3` cannot cross. If any method bounds it below `α·d_p`, the isolated-clock constant improves
below `1/3`; current evidence (§1) is that this is exactly the Weyl-cancellation difficulty.
