# Zero-selected carry × signed arithmetic flux — continuation theorems (ZSC)

**Baseline:** Main XXIV `071ce1e0ee6ab8f8c07113e901131aa646d6b95d`; continuation of this dossier
from PR #599 head `bc8ab91402f18273cfd6fc107cb7e8e50a8a2430`. **π base-16 normality, every
source-selected signed estimate, the seam-density statement and RH remain OPEN.** No all-shell
signed estimate for the zero seed is proved here. What is proved: the exact Diophantine price of
any fixed saving (ZSC-01), the exact identity of the weakest statistical rung and its sufficiency
for a mode-1 saving (ZSC-02, ZSC-03), what existing irrationality input does and does not give
(ZSC-04), the logical independence of the seam target from both (ZSC-05), and a classification of
the source class that says precisely what the zero seed is (ZSC-06).

Status labels as in [THEOREMS](THEOREMS.md): `PROVED LOCAL` (complete elementary proof here;
same-model authorship, not external refereeing, not Lean), `CLASSICAL IMPORT` (cited theorem, with
its verification status in [SOURCE_MAP](SOURCE_MAP.md)), `OBSERVED FINITE`, `OPEN`.

## 0. Notation

Source contract of THEOREMS §0, unchanged: `r(n)`, `U_0 = 0`, `U_n = 16U_(n-1) + r(n)`, `T_n`,
`Y_n = U_n + T_n = 16^n x`, `x = π/16`, `C_n = ⌊U_n⌋`, `κ_n = C_n - 16C_(n-1)`,
`ε_n = ⌊Y_n⌋ - C_n`, `d_n = ⌊16{Y_n}⌋` (so `{Y_n} = 0.d_n d_(n+1) d_(n+2)…` in base 16).

For a real `ξ` write `y_n = 16^n ξ`, `d_n(ξ) = ⌊16{y_n}⌋`, and for integers `h ≠ 0`, `B ≥ 1`

```text
W_B(h; ξ) = (1/B) Σ_(n=B)^(2B-1) e(h y_n),        D_(B,h) = (1/B) Σ_(n=B)^(2B-1) e(h U_n).
```

`W_B(h) = W_B(h; x)`, and `|D_(B,h) - W_B(h)| ≤ 2π|h| max_(n≥B) T_n ≤ (π/32)|h| B^(-2)` (IAD-03).
A real `ξ` is the completed point of the **seeded carrier** with the same forcing and seed
`s = ξ - x`; all statements "for every real ξ" are statements about every seed.

- *Change set:* `Ch(ξ) = {n ≥ 0 : d_n(ξ) ≠ d_(n+1)(ξ)}`, shell density `c_B = #(Ch ∩ [B, 2B))/B`.
- *Carry-change set (zero seed):* `Ch^κ = {n ≥ 0 : κ_(n+1) ≠ κ_(n+2)}`, shell density `c^κ_B`.
- *Base-16 exponent* (Amou–Bugeaud normalization): `v_16(ξ) = limsup_m -log_16 ‖16^m ξ‖ / m`.
  Always `v_16 ≤ μ - 1`, and `μ ≥ 2` for every irrational (Dirichlet).

---

## ZSC-01 — the saving–exponent law (PROVED LOCAL; sharpens IAD-08)

**Lemma (coherent stretch).** Let `ξ` be real, `h ≠ 0`, and let integers `m ≥ 0`, `N ≥ 1`,
`B ≥ 1` satisfy `B ≤ m` and `m + N ≤ 2B`. Then

```text
Re W_B(h; ξ)  ≥  (2N - B)/B  -  2π|h| · ‖16^m ξ‖ · 16^N / (15 B).                 (1.1)
```

*Proof.* For `m ≤ n < m+N`: `‖h y_n‖ ≤ |h|·16^(n-m)·‖16^m ξ‖` and `Re e(t) ≥ 1 - 2π‖t‖`, so
these `N` terms sum to at least `N - 2π|h|‖16^m ξ‖(16^N - 1)/15`. The other `B - N` terms of the
shell have real part `≥ -1`. ∎

**Theorem.** Let `0 < η < 2` and suppose `Re W_B(h; ξ) ≤ 1 - η` for all `B ≥ B_0` (in
particular if `|W_B(h; ξ)| ≤ 1 - η`). Then for every `m ≥ max(2B_0, (2+η)/η)`:

```text
‖16^m ξ‖  ≥  (15η / (512π|h|)) · 16^( -((2-η)/(2+η)) · m ),      hence   v_16(ξ) ≤ (2-η)/(2+η) < 1.   (1.2)
```

Equivalently: `liminf_B (1 - Re W_B(h; ξ)) ≤ 2(1 - v)/(1 + v)` with `v = min(v_16(ξ), 1)`.

*Proof.* Put `N = ⌈m(2-η)/(2+η)⌉ + 1` and `B = ⌈(m+N)/2⌉`. Then `N ≤ m` (because
`m ≥ (2+η)/η`), so `m/2 ≤ B ≤ m`, `m + N ≤ 2B`, `B ≥ B_0`. By (1.1) and the hypothesis,
`2π|h|‖16^m ξ‖16^N/15 ≥ 2N - (2-η)B ≥ [N(2+η) - (2-η)(m+1)]/2 ≥ η`, using `B ≤ (m+N+1)/2` and
`N(2+η) ≥ m(2-η) + (2+η)`. Finally `N ≤ m(2-η)/(2+η) + 2`. ∎

**Remarks.**

1. *IAD-08(a) is the endpoint of this law.* IAD-08 used only the shell that begins at the
   approximation (`B = m`, `N = B`) and concluded `‖16^B x‖ ≥ cB·16^(-B)`. Choosing the best
   shell that *contains* the coherent stretch gives an exponential improvement: **a fixed saving
   `η` forces the restricted exponent strictly below 1**, namely `≤ (2-η)/(2+η) = 1 - η + O(η²)`.
2. *No theorem about `μ(π)` can pay it.* Every bound on the unrestricted irrationality exponent
   yields at best `v_16 ≤ μ - 1`, and `μ - 1 ≥ 1`. So neither the refereed record
   `μ(π) ≤ 7.1032`, nor `μ(π) = 2` if it is ever confirmed, implies the necessary condition for
   *any* fixed saving at *any* mode. This is not an artefact of the inequality `v_16 ≤ μ - 1`:
   Shallit's number `K = Σ_(k≥0) 16^(-2^k)` has bounded partial quotients (CLASSICAL IMPORT, seen),
   so `μ(K) = 2`, while `‖16^(2^k) K‖ ≤ 2·16^(-2^k)` and, by (1.1) with `m = B = 2^k`,
   `N = B - ⌈log_16 B⌉`, `Re W_(2^k)(h; K) → 1`. Best-possible unrestricted Diophantine type is
   compatible with no saving at all.
3. *Full decay at one mode needs exponent 0.* If `W_B(h; ξ) → 0` for one `h`, then
   `S(M) = Σ_(n<M) e(h y_n) = o(M)`, and a coherent stretch `[m, m+N)` has
   `|S(m+N) - S(m)| ≥ (N-k)(1 - 2π|h|16^(-k))` whenever `‖16^m ξ‖ ≤ 16^(-N)`; hence `N = o(m)` and
   `v_16(ξ) = 0`. The law (1.2) interpolates between `η → 0` (exponent 1) and this endpoint only
   down to `1/3` at `η = 1`; the difference is that (1.2) uses one shell, the remark two partial
   sums.
4. *Near-sharpness.* For `0 < λ < 1` let `ξ_λ` have digit `0` on `[2^k, 2^k + ⌊λ2^k⌋)` and digit
   `7` on the rest of `[2^k, 2^(k+1))`. Then `v_16(ξ_λ) = λ` and
   `liminf_B (1 - Re W_B(1; ξ_λ)) = (1 - cos(14π/15))·(1-λ)/(1+λ) = 1.978…·(1-λ)/(1+λ)`, against the
   bound `2(1-λ)/(1+λ)`. (The zero fraction of a shell is maximal, `2λ/(1+λ)`, at
   `B = (1+λ)2^(k-1)`.) The constant 2 in (1.2) cannot be lowered below `1.978`.
5. *Lag correlations.* (1.1)–(1.2) apply verbatim to `Θξ` for an integer multiplier `Θ`, hence to
   the lag-`ℓ` correlation (`Θ = 16^ℓ - 1`, IAD-08(b)) for fixed `ℓ`. For lags growing with `B`
   only the endpoint statement of IAD-08(b), with its `B - ℓ` factor, is claimed.

## ZSC-02 — the first statistical rung is the density of digit changes (PROVED LOCAL)

**Lemma (locality).** For real `ξ` and `n ≥ 0`:

1. if `d_n = d_(n+1) = … = d_(n+k-1)` (`k ≥ 1`), then `‖15 y_n‖ ≤ 15·16^(-k)`;
2. if `‖15 y_n‖ < 1/256`, then `d_n = d_(n+1)`.

*Proof.* (1) With common digit `j`, both `{y_n}` and `j/15 = 0.jjj…` lie in the closed cylinder
of length `16^(-k)` over `0.j…j`. (2) Write `{y_n} = j/15 + t`, `|t| < 1/(15·256)`, `0 ≤ j ≤ 15`.
The two leading digits are `jj` iff `{y_n} ∈ [17j/256, (17j+1)/256)`, and
`j/15 - 17j/256 = j/(15·256)`, `(17j+1)/256 - j/15 = (15-j)/(15·256)`. For `1 ≤ j ≤ 14` both
margins are `≥ 1/(15·256)`; `j = 0` occurs only with `t ≥ 0` and `j = 15` only with `t < 0`. ∎

**Theorem.** For every real `ξ` and every `B ≥ 1`, with `c_B` the change density of the shell:

```text
(a)  1 - Re W_B(15; ξ)  ≥  c_B / 3321;
(b)  1 - Re W_B(15; ξ)  ≤  2(k-1)(c_B + (k-1)/B) + 450π²·16^(-2k)      for every k ≥ 2;
(c)  |W_B(1; ξ)|  ≤  1 - (c_B - 1/B)/65793;
(d)  if c_B ≥ c > 0 for all B ≥ B_0, then every run of equal digits starting at a position
     m ≥ max(2B_0, 2/c) has length ≤ ((1-c)(m+1) + 2)/(1+c), and
     ‖15·16^m ξ‖ ≥ 16^( -((1-c)/(1+c))·m - 4 ).
```

*Proof.* (a) At a change, `‖15y_n‖ ≥ 1/256` by Lemma 2, so
`1 - cos 2π‖15y_n‖ ≥ 1 - cos(2π/256) > 1/3321`. (b) Call `n` good if `d_n = … = d_(n+k-1)`; then
`1 - cos 2π‖15y_n‖ ≤ (30π·16^(-k))²/2` by Lemma 1. A bad `n` has a change in `[n, n+k-2]`, so
there are at most `(k-1)(c_B B + k - 1)` bad `n` in the shell, each contributing at most 2.
(c) Let `|W_B(1)| = 1 - η'` and `W_B(1) = |W_B(1)| e(θ)`. The mean of `1 - cos 2π(y_n - θ)` is
`η'`, so the set `G^c` of shell times with `‖y_n - θ‖ > t` has at most `η'B/(8t²)` elements
(`1 - cos 2πt ≥ 8t²` for `t ≤ 1/2`). If `n, n+1 ∉ G^c` then
`‖15y_n‖ = ‖y_(n+1) - y_n‖ ≤ 2t`; with `t = 1/513`, `2t < 1/256` and Lemma 2 gives no change at
`n`. Hence `c_B B ≤ 2#G^c + 1 ≤ η'B·513²/4 + 1`. (d) Let `d_m = … = d_(m+L-1)`, `L ≤ m` (truncate
otherwise). The shell `B' = ⌈(m+L)/2⌉` contains `[m, m+L)` and has at most `B' - (L-1)` changes,
so `L - 1 ≤ (1-c)B' ≤ (1-c)(m+L+1)/2`, which is the run bound; it also excludes `L = m` once
`m > 3/(2c)`. If `‖15y_m‖ < 16^(-L-1)` then `16^i‖15y_m‖ < 1/256` for `i ≤ L-1` and Lemma 2 gives
a run of length `L+1`. ∎

**What this identifies.**

- *(a)+(b)*: `liminf_B c_B > 0  ⟺  limsup_B Re W_B(15; ξ) < 1`. A fixed real saving at the single
  mode `h = 15` **is** positive lower density of digit changes; nothing else.
- *(c)*: positive lower density of digit changes is **sufficient** for the primary target of the
  mission at mode `h = 1`: `limsup_B |W_B(1)| < 1`, and for the rational source
  `limsup_B |D_(B,1)| < 1`. Call this statement **(CH)**:

  > **(CH)** There are `c > 0` and `B_0` such that for every `B ≥ B_0` at least `cB` of the
  > positions `n ∈ [B, 2B)` have `d_n ≠ d_(n+1)` in the hexadecimal expansion of π.

  (CH) is implied by normality (then `c_B → 15/16`) and is far weaker: it is a one-parameter
  statement about escapes of the `×16` orbit from the sixteen fixed points `j/15`.
- *(d)*: (CH) forces the restricted exponent at the denominators `15·16^m` below
  `(1-c)/(1+c) < 1`, consistently with ZSC-01.
- The converse of (c) fails (two long constant runs of different digits give a saving at mode 1
  with no changes), and (CH) gives no saving at modes whose periodic points have digit changes
  (`ξ = 1/17`: `c_B = 1`, `W_B(17) = 1`).

## ZSC-03 — sixteen is sparse for every seed; (CH) is a statement about `⌊U_n⌋` (PROVED LOCAL)

**Renewal lemma (every real seed; sharpens RIO-10).** Let `n ≥ 1`,
`J(n) = ⌊log_16(15/(16 r(n+1)))⌋ ≥ ⌊log_4(2n)⌋`. If `κ_(n+1) = 16`, then

```text
κ_(n+2) = κ_(n+3) = … = κ_(n+1+J(n)) = 0,
```

and by RIO-09 the zero run after the 16 has length `b` with
`J(n) ≤ b < 1 + log_16((8n+9)(8n+14)/15)`: so `b = 2 log_16 n + O(1)` in an explicit window of
bounded width.

*Proof.* `κ_(n+1) = 16` gives `{U_(n+1)} = 16{U_n} + r(n+1) - 16 ∈ [0, r(n+1))`. While no carry
occurs, `{U_(n+1+j)} = 16^j{U_(n+1)} + Σ_(i=1)^j 16^(j-i) r(n+1+i) < (16/15)·16^j·r(n+1)` (`r`
decreasing), and this is `≤ 1` for `j ≤ J(n)`. `r(n+1) ≤ 15/((8n+1)(8n+2))` gives
`15/(16r(n+1)) ≥ 4n²`. ∎

**Corollary 1 (frequency of the letter 16).** For every seed and every `B ≥ 2`:
`#{B ≤ n < 2B : κ_n = 16} ≤ 1 + B/log_4 B`. Unconditionally the letter 16 has density zero in
the literal carry stream. (RIO-10 gave `16 → 0`, hence density `≤ 1/2`; SWT-04 had density 0
only under either normality hypothesis.)

**Corollary 2 (carry changes are digit changes).** For the zero seed and `B ≥ 2`:

```text
| c^κ_B - c_B |  ≤  3 (1 + (B+1)/log_4 B) / B   →  0.
```

*Proof.* By the cocycle `d_n = κ_(n+1) + ε_(n+1) - 16ε_n` (SWT-03), the change indicators of `d`
and of `κ^+` at `n` agree when `(ε_n, ε_(n+1), ε_(n+2)) ∈ {(0,0,0), (1,1,1), (0,1,1), (0,1,0)}`
(in the last two both change: `κ_(n+1) = d_n - 1 ≤ 14` against 15 or 16). `(1,0,1)` is impossible
for `n ≥ 2` (after a seam `d_(n+1) = 0`, but a seam starting at `n+2` needs `d_(n+1) ≥ 1`). The
remaining patterns `(0,0,1)`, `(1,1,0)`, `(1,0,0)` occur at most once each per seam run, seam runs
are in bijection with letters 16, and consecutive seam runs are separated as in Corollary 1. ∎

Therefore **(CH) ⟺ (CH_κ)**: *the literal carries of the zero-seeded rational source change at a
positive lower density of times in every large shell.* This is a statement about the integer
parts of exact rationals, with no π oracle, no tail and no seam hypothesis, and by ZSC-02(c) it
implies `limsup_B |D_(B,1)| < 1`.

## ZSC-04 — what existing irrationality input gives, for all `n` (PROVED LOCAL from one CLASSICAL IMPORT)

Import (Mahler 1953, Theorem 1; statement read in the source by the literature helper): *for all
positive integers `p` and `q ≥ 2`, `|π - p/q| > q^(-42)`.*

**Theorem.** For every `n ≥ 2`:

1. a run of equal hexadecimal digits `d_n = … = d_(n+L-1)` of `x` has `L ≤ 41n`; a run of zeros
   or of `F`'s, and hence every seam run and every run of literal carries 15, has `L < 41(n-1)`;
2. *(exact finite look-ahead)* for every `J ≥ 41(n-1)`: `⌊16^(n-1)π⌋ = ⌊ C_(n+J) / 16^J ⌋`. The
   first `n-1` hexadecimal digits of π are read off, with certainty, from the integer part of the
   rational `U_(42n-41)`;
3. `Ch ∩ [n, 42n) ≠ ∅`; consequently `#(Ch ∩ [0, N)) ≥ log_42 N - 2` for all `N ≥ 2`.

*Proof.* (1) By ZSC-02 Lemma 1, `|16^(n-1)π - M - j/15| ≤ 16^(-L)` for an integer `M ≥ 0`, i.e.
`|π - (15M+j)/(15·16^(n-1))| ≤ 16^(-L-n+1)`. Mahler with `q = 15·16^(n-1)` gives
`L + n - 1 < 42(n-1) + 42 log_16 15 < 42(n-1) + 41.03`. For `j ∈ {0, 15}` take `q = 16^(n-1)`.
(2) `C_(n+J) = ⌊Y_(n+J)⌋ - ε_(n+J) = 16^J⌊Y_n⌋ + D - ε_(n+J)` with `D` the integer of the digit
block `d_n … d_(n+J-1)`; the quotient by `16^J` has floor `⌊Y_n⌋` unless `D = 0`, a zero run of
length `J`, excluded by (1). (3) is (1); the count follows from the disjoint intervals
`[n_i, 42n_i)`, `n_0 = 2`, `n_(i+1) = 42n_i`. ∎

These are the **all-`n`, fully explicit** forms of RIO-11 and of the SWT-03 look-ahead. They are
consequences of an existing irrationality bound and are labelled as such: the rate is `log N`
changes, against the `cN` of (CH). Asymptotically `41` improves to `6.1033` (Zeilberger–Zudilin),
and would improve to `1 + ε` under `μ(π) = 2`.

**The ladder, with the exact position of each rung.**

| Rung | Statement about the hexadecimal digits of π (equivalently the carries, ZSC-03) | Status |
|---|---|---|
| L0 | infinitely many changes | known (irrationality) |
| L1 | `≥ log_42 N - 2` changes among the first `N` digits, every `N` | known (Mahler; this file) |
| L2 | at least one change in every shell `[B, 2B)`, `B` large | **OPEN**; needs the borderline `v ≤ 1` at denominators `15·16^m`; not implied by `μ(π) = 2`, which leaves an `ε` |
| L3 = (CH) | `≥ cB` changes in every large shell | **OPEN**; `⟺` a real saving at mode 15; `⟹` a saving at mode 1; needs exponent `≤ (1-c)/(1+c) < 1` |
| L4 | `W_B(h) → 0` for every `h ≠ 0` | **OPEN** (normality) |

For comparison (CLASSICAL IMPORT, seen): for irrational *algebraic* numbers the best known count
of digit changes is `≫ (log N)^(3/2)(log log N)^(-1/2)` (Bugeaud–Evertse 2008, Thm 3.1). L2 and
L3 are open there as well.

## ZSC-05 — the seam target is independent of the saving and of the wall (PROVED LOCAL)

All three examples are seeded carriers of the **unchanged** forcing (seed `ξ - x`); the seam is
`ε_n(ξ) = 1 ⟺ {y_n} < T_n` with the true tail `T_n`.

| Witness (hexadecimal digits of `ξ`) | `v_16` | change density | seam density | saving |
|---|---|---|---|---|
| **W1**: digit 1 at `a_0 = 16`, `a_(j+1) = a_j + ⌈√a_j⌉ + 1`; 0 elsewhere | 0 | `→ 0` | `→ 1` | none: `W_B(h) → 1` for all `h` |
| **W2**: digit `E` at `b_0 = 2`, `b_(j+1) = b_j²`; `F` elsewhere | `∞` | `→ 0` | `0` (seam-free) | none |
| **W3**: blocks `k = 1, 2, …` of length `2k`: `k` zeros, then `k` digits `1212…` | 0 | `→ 1/2` | `→ 1/2` | `limsup_B |W_B(1)| < 1` by ZSC-02(c) |

*Proofs.* W1: for `m ≥ 16` the next digit 1 is at distance `≤ √m + 1`, and no two 1's are
adjacent, so `16^(-√m-2) ≤ {y_m} < 1/2`: `v_16 = 0`. A shell contains at most `√B + 2` ones, hence
`≤ 2√B + 4` changes. `T_n ≥ r(n+1)/16 ≥ 1/(4(8n+2)²)`, so `ε_n = 1` as soon as `n` is followed by
`≥ log_4(16n+4)` zeros: all but `O(log n)` positions of each gap of length `≈ √n`. W2: no digit 0,
and `ε_n = 1` forces `d_n = 0`; `‖16^m ξ‖ ≤ 16^(-(b_(j+1)-m))`. W3: block `k` starts at
`k(k-1) ≈ n`, its zero run has length `k ≈ √n ≫ log n`, its second half changes at every
position. ∎

**Consequences.**

- `v_16 = 0` — the full Diophantine condition, necessary for decay at a single mode (ZSC-01,
  Remark 3) — implies **neither** a saving **nor** seam density zero (W1).
- Seam-freeness, the strongest form of Target A, implies **neither** a Diophantine bound **nor**
  a saving (W2).
- A fixed saving at mode 1, even (CH) with `c = 1/2`, does **not** imply seam density zero (W3).

So for seeded carriers of the authentic forcing, `ρ(N) = o(N)`, the wall, and (CH) are pairwise
independent; they meet only at normality. Any derivation of one from another must use the zero
seed in a way that fails for `W1`–`W3`, and by ZSC-06 the only such information is the identity of
the real number `x`.

## ZSC-06 — the moduli of sources: what the zero seed is (PROVED LOCAL; one CLASSICAL IMPORT)

**(a) The class.** A *source* is a pair `(g, s)`, `g ∈ Q[z]`, `s ∈ Q`, with forcing
`r_g(n) = ∫_0^1 z^(8n-8) g(z) dz = Σ_i g_i/(8n-7+i)`, state `U_0 = s`,
`U_n = 16U_(n-1) + r_g(n)`, and `G = g/(16 - z⁸)`. Then

```text
U_n = 16^n s + ∫_0^1 g(z) (16^n - z^(8n))/(16 - z⁸) dz,     T_n = ∫_0^1 z^(8n) G(z) dz,
Y_n = U_n + T_n = 16^n ξ,     ξ = s + ∫_0^1 G(z) dz.
```

The authentic source is `(g_π, 0)`, `g_π = 4 - 2z³ - z⁴ - z⁵ = K(z)(1-z)`,
`K = (z²+2)(z²+2z+2)`, `16 - z⁸ = K(z)·m(z)`, `m = (2-z²)(z²-2z+2)`, `ξ = π/16`.

**(b) Gauge.** For `h ∈ Q[z]` put `a(n) = ∫_0^1 z^(8n) h(z) dz`. The source
`(g - (16-z⁸)h, s + ∫_0^1 h)` has `G' = G - h` and

```text
U'_n = U_n + a(n),     T'_n = T_n - a(n),     ξ' = ξ,     |a(n)| ≤ ‖h‖_1/(8n+1).
```

Hence `|D'_(B,k) - D_(B,k)| ≤ 2π|k|·‖h‖_1/(8B+1)`: every limit statement about shell means, lag
correlations or block frequencies off a density-zero set is **gauge-invariant**. The seed and the
set of poles are **not**: `h ≡ c` moves the seed by `c` and adds the poles `-16c/(8n-7) + c/(8n+1)`
(this is RIO-01's static translation; the `H(n) - 16H(n-1)` control of RS is another instance).

**(c) Proper form.** Each gauge class has exactly one member with `deg g ≤ 7` (polynomial
division), i.e. forcing `Σ_(j=1)^8 A_j/(8n-8+j)`, the BBP normal form
`ξ - s = L(A) := Σ_j A_j v_j`, `v_j = ∫_0^1 z^(j-1)/(16-z⁸) dz = Σ_(k≥0) 16^(-k-1)/(8k+j)`.
**In the proper form the seed is an invariant of the class.** The authentic source is proper,
`A_π = (4,0,0,-2,-1,-1,0,0)`, seed 0.

**(d) The null relation, elementarily.**

```text
(z² - 4z + 2)/m(z) = z/(z²-2) - (z-1)/(z²-2z+2),
∫_0^1 (z²-4z+2)/m(z) dz = [ ½ log|z²-2| - ½ log(z²-2z+2) ]_0^1 = 0.
```

So `g_0 = K(z)(z²-4z+2) = 8 - 8z - 4z² - 8z³ - 2z⁴ - 2z⁵ + z⁶`, i.e.
`A_0 = (8,-8,-4,-8,-2,-2,1,0)`, has `L(A_0) = 0`. This is the seven-pole null source of AT-07 (with
the opposite sign) and Bailey's zero relation; the proof above needs no import. The authentic
`g_π` and the null `g_0` lie in the same four-dimensional family `{K·q : deg q ≤ 3}`, whose
periods `∫ q/m` span only `π`, `log 2` and `√2·log(1+√2)`.

**(e) Rigidity (uses Baker's theorem).** Import (Baker; quoted from the standard statement, *not*
re-read this round): *if the logarithms of nonzero algebraic numbers `α_1,…,α_k` are linearly
independent over `Q`, then `1, log α_1, …, log α_k` are linearly independent over the algebraic
numbers.*

> **Theorem.** `{A ∈ Q⁸ : L(A) ∈ Q} = Q·A_0`. Equivalently: the period space `V = L(Q⁸)` has
> dimension 7 over `Q`, `V ∩ Q = {0}`, and every nonzero element of `V` is transcendental.

*Proof.* Partial fractions at the eight roots `α` of `z⁸ = 16` give, with `P_A(z) = Σ_j A_j z^j`,
`L(A) = -(1/128) Σ_α P_A(α) Log(1 - 1/α)`. The eight logarithms are rational combinations of

```text
ℓ_1 = log 2, ℓ_2 = log 3, ℓ_3 = log 5, ℓ_4 = log(1+√2), ℓ_5 = iπ,
ℓ_6 = i·arctan(1/√2) = ½ log((1+2√2 i)/3),   ℓ_7 = i·arctan(1/3) = ½ log((4+3i)/5):
```

`Log(1 ∓ 1/√2) = ∓ℓ_4 - ℓ_1/2`, `Log(1 ± i/√2) = (ℓ_2-ℓ_1)/2 ± ℓ_6`,
`Log((1±i)/2) = -ℓ_1/2 ± ℓ_5/4`, `Log((3±i)/2) = (ℓ_3-ℓ_1)/2 ± ℓ_7`. The `ℓ_i` are linearly
independent over `Q`: an integer relation splits into real and imaginary parts; the real part
`2^a 3^b 5^c (1+√2)^d = 1` and its conjugate under `√2 ↦ -√2` give `d = 0`, then `a = b = c = 0`;
the imaginary part gives `u^e w^f = 1` with `u = (1+2√2i)/3 = -(1-√-2)/(1+√-2)` and
`w = (4+3i)/5 = i(2-i)/(2+i)`, which have nonzero valuation at primes above 3, respectively above
5, and zero valuation at the other; so `e = f = 0`, and then the coefficient of `ℓ_5` is 0. By
Baker, `L(A) ∈ Q` iff the seven coefficients vanish:

```text
P_A(√2) = P_A(-√2),   P_A(±i√2) = 0,   P_A(-1±i) = 0,   Im P_A(1+i) = 0,   P_A(√2) + P_A(1+i) = 0.
```

Over `Q` this is a linear system of rank 7 on `Q⁸` (exact computation in `Q(√2, i)`,
`zsc_core.baker_rank`); its kernel is spanned by `A_0`. ∎

**(f) Consequences.**

1. *What the zero seed is.* A proper source with zero seed is exactly a point `ξ ∈ V`; a proper
   source with rational seed `s` is a point of `V + s`. The zero seed excludes every nonzero
   rational completed point: `ξ ∈ Q` iff `A ∈ Q·A_0`, and then `ξ = s`. The hijack seeds of IAD-07
   are detected by this one invariant (`s ≠ 0` in proper form), but their completed points
   `x + s` are as transcendental as `x`.
2. *Uniqueness of the hostile null source.* Up to scaling, AT-07 is the **only** proper
   zero-seeded source whose completed point is rational. Either of two further source invariants
   excludes it: residue sum zero (`Σ A_j = 0`, i.e. `r = O(n^(-2))`; `Σ A_0 = -15`), or a
   nonnegative moment density `g ≥ 0, g ≢ 0` on `[0,1]` (then `ξ > 0`). The authentic source has
   both.
3. *Properness is essential.* The non-proper source `(g_H, 0)`,

   ```text
   g_H = (16 - z⁸)(3 - 2z) + g_0 = 2z⁹ - 3z⁸ + z⁶ - 2z⁵ - 2z⁴ - 8z³ - 4z² - 40z + 56,
   r_H(n) = 56/(8n-7) - 40/(8n-6) - 4/(8n-5) - 8/(8n-4) - 2/(8n-3) - 2/(8n-2) + 1/(8n-1) - 3/(8n+1) + 2/(8n+2),
   ```

   has literal zero seed, rational simple poles, residue sum 0 (`r_H = O(n^(-2))`), a moment
   density that is positive on `[0,1)` with a simple zero at 1 (the same shape as `g_π`, so the
   innovation calculus of IAD-03 and a Kusmin–Landau window as in IAD-04 hold with other
   constants), and the prime genealogy of the null source: its states are
   `U^H_n = U^0_n + 2·16^n - 3/(8n+1) + 1/(4n+1)` with `U^0_n` the state of `(g_0, 0)`.
   Its completed point is `ξ_H = 2`: `U^H_n = 2·16^n - T^H_n`,
   `0 < T^H_n → 0`, so `{U^H_n} → 1`, every late carry is 15, the seam density is 1 and
   `D_(B,h) → 1` for every `h`. *Positivity of `g_H`:* `(16-z⁸)(3-2z) ≥ 15` and `g_0 ≥ -15` on
   `[0,1]`, each with equality only at `z = 1`. In proper form it is `(A_0, s = 2)`.
4. *The census is not an invariant of π.* For every rational `ρ` the proper zero-seeded source
   `A_π + ρA_0` completes to `π/16`. For `ρ ≠ 0` it has seven poles per step instead of four,
   different denominators and a different prime genealogy; its states differ from the authentic
   ones by `ρ·U^0_n = O(ρ/n)`, and all its asymptotic statistics coincide with the authentic ones
   by (b). The four-pole source is the unique member of this line with `r = O(n^(-2))`.
5. *Asymptotic no-go (upgrades IAD-07).* IAD-07 used shell-dependent seeds and excluded only
   finite-horizon transfers. The sources in 2–3 are **fixed**, zero-seeded and census-complete, so:
   *no argument, finite-horizon or asymptotic, whose hypotheses are satisfied by every
   zero-seeded rational-pole source of a class containing `A_0` (proper) or `g_H` (non-proper,
   positive, `O(n^(-2))`) can prove a saving for any mode.* Scope: this says nothing about
   arguments that use properness together with `A ∉ Q·A_0`, i.e. that use `ξ ∈ V \ {0}`.

**Reading.** In proper form, *(rational forcing, zero seed, `A ∉ Q·A_0`)* is equivalent to
*`ξ` is a nonzero element of the seven-dimensional period space `V`*. That membership has a proved
non-statistical consequence — transcendence, and with it the finiteness of every seam run
(SWT-03) and the ceilings of ZSC-04. By (b), every statistical statement about the selected path
is a statement about the single real number `ξ`; by 4, the complete prime genealogy is not
determined by `ξ`; by ZSC-05, the base-16 Diophantine exponent of a completed point decides none
of the statistical targets. No hostile element of `V \ {0}` is known, and none is constructed here: "every nonzero
element of `V` is normal in base 16" is the Bailey–Crandall-type conjecture of which π is one
instance, and (CH) is open for every element of `V \ {0}`.

## ZSC-07 — Target A, instrument triage and the acceptance test

**Target A (seam density).** `ρ(N) ≤ H_N ≤ ρ(N) + 1 + b_N`, and `ε_n = 1 ⟺ {Y_n} < T_n`
(SWT-03): `ρ(N) = o(N)` says that positions followed by `≈ 2 log_16 n` zeros have density zero.
Unconditionally only `N - ρ(N) ≫ log N` is available (ZSC-04). No arithmetic input found in this
round improves it, and three facts say why none of the available kind can: the rare-carry
inequality `{U_n} ≥ 1 - r(n+1)/16` is an inequality for a rational of denominator
`exp((6+o(1))n)` at scale `n^(-2)` (no exclusion); `v_16 = 0` is compatible with seam density 1
(W1); and a zero-seeded positive `O(n^(-2))` rational source has seam density exactly 1
(ZSC-06(f)3). By ZSC-05 the target would in any case yield no saving. **Target A stays OPEN and
is demoted:** it is neither on the path to a signed estimate nor reachable from the Diophantine
side. What the source does give for every seed is ZSC-03: the letter 16 has density zero.

**Instrument triage (Phase 2).**

| Instrument | Discriminating fact | Verdict |
|---|---|---|
| Complete arithmetic genealogy | the census differs along the line `A_π + ρA_0` while every statistic agrees (ZSC-06(f)4); complete census with zero seed is coherent for `g_H` | not an invariant; closed for transfers, finite-horizon (IAD-07) and asymptotic (ZSC-06(f)5) |
| Carry-renewal dynamics | escapes from the fixed points `j/15` are exactly digit changes; their density is equivalent to a mode-15 saving and sufficient for a mode-1 saving (ZSC-02); 16-events renew with a rigid `15^a 16 0^b` shape (ZSC-03) | **selected**; yields the criterion (CH), not an estimate |
| Arithmetic cylinder refinement | the seeds sharing the first `N` carries of the zero seed form an interval of length `≤ 16^(-N)` around 0; which words are excluded for `ξ ∈ V\{0}` is a Diophantine question, answered to the extent known by ZSC-04 | reduces to L1; no discrepancy content |
| Two-index dispersion | every pair identity found is `U_(n+ℓ) - U_n = (16^ℓ-1)U_n + Δ_ℓ(n)`, the gauge of IAD-05 | no new partition found |

**Acceptance test for the statements of this file.**

| Question | ZSC-01 | ZSC-02/03 | ZSC-06 |
|---|---|---|---|
| Source-dependent input | none (holds for every real `ξ`) | forcing only (`r` decreasing, `T_n` brackets) | rational `g`, zero seed, Baker |
| Where the zero seed is used | not used | only in ZSC-03 Cor. 2 (cocycle with `ε`) | proper-form invariant `s = 0` |
| Old claim strengthened | IAD-08(a): endpoint → exponent `(2-η)/(2+η)` | RIO-10 (`16→0` → `16→0^J`), SWT-04 (letter 16 density 0 unconditionally) | AT-07 (uniqueness), IAD-07 (asymptotic scope) |
| Holds for the coherent wrong seed | yes (vacuously: no saving) | yes (`c_B = 0`, no saving) | it is the point `0 ∈ V` reached by `A_0` |
| New theorem or equivalent criterion | necessary condition (theorem) | criterion: (CH) `⟹` saving; (CH) itself OPEN | classification (theorem) |
| Falsifying control | any `ξ` with a saving and `v_16 > (2-η)/(2+η)` | any shell violating (a)–(c) | a second proper null vector; a rational `L(A)`, `A ∉ Q·A_0` |

**No estimate in this file passes the acceptance test as a source-selected signed estimate.**
The exact next missing inequality is (CH), in either of its equivalent forms (digits, or literal
carries of `⌊U_n⌋`).

## Summary

| | Statement | Status |
|---|---|---|
| ZSC-01 | A fixed saving `η` at one mode on all large shells forces `‖16^m ξ‖ ≥ c·16^(-((2-η)/(2+η))m)`; no bound on `μ` can supply it; constant 2 sharp to within `1.978/2` | PROVED LOCAL (Shallit witness: IMPORT, seen) |
| ZSC-02 | `c_B/3321 ≤ 1 - Re W_B(15) ≤ 2(k-1)(c_B+(k-1)/B) + 450π²16^(-2k)`; `|W_B(1)| ≤ 1 - (c_B - 1/B)/65793`; (CH) forces exponent `≤ (1-c)/(1+c)` | PROVED LOCAL |
| ZSC-03 | `16 → 0^(J(n))`, `J(n) ≥ ⌊log_4 2n⌋`, every seed; letter 16 has density 0 unconditionally; `|c^κ_B - c_B| → 0`; (CH) `⟺` (CH_κ) | PROVED LOCAL |
| ZSC-04 | For all `n ≥ 2`: equal-digit runs `≤ 41n`; exact look-ahead `J = 41(n-1)`; `≥ log_42 N - 2` changes | PROVED LOCAL from Mahler 1953 (IMPORT, seen) |
| ZSC-05 | Seam density, the wall and (CH) are pairwise independent for seeded carriers of the authentic forcing (W1–W3) | PROVED LOCAL |
| ZSC-06 | Gauge and proper form; elementary null relation; `{A : L(A) ∈ Q} = Q·A_0`; zero seed `⟺ ξ ∈ V`; hostile positive `O(n^(-2))` zero-seeded source `g_H`; census not an invariant of π | PROVED LOCAL; rigidity (e) uses Baker (IMPORT, not re-read) |
| (CH) | positive lower shell density of digit changes of π in base 16 | **OPEN** — the next missing inequality |
| SEAM-DENSITY | `ρ(N) = o(N)` | **OPEN**, demoted (ZSC-07) |
| — | any all-shell signed estimate for the zero seed; π base-16 normality | **OPEN** |
