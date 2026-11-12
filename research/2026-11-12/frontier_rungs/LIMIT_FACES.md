# Limit faces — the rungs of the signed ladder as excluded faces, with thresholds

Round 3 (2026-11-12), parent `9b4b71b2` (preregistration of this round), itself above draft PR #599
head `8de33430` and Main XXIV `071ce1e0`.

**π base-16 normality, the source-selected signed estimate and (CH) are OPEN and stay OPEN.**
Nothing below estimates anything about π. Every statement is about an arbitrary real `ξ` (so about
every seed), or about an arbitrary probability measure on `[0,1]`; the statements say what the
rungs of the ladder *are*, and how far from Lebesgue a shell must stay for a rung to fail.

Status labels: **PROVED LOCAL** = paper proof in this file by the same model that wrote the
statement, with exact or tolerance-checked instances in `test_faces.py` / `probe_rungs.py`; not
externally reviewed, not kernel-checked, and at the time of writing not yet audited by an
independent reader. **IMPORT** = classical theorem quoted, not reproved. **OBSERVED** = finite
numerics, an instance and not evidence for an asymptotic claim. **OPEN** = not known.

## 0. Notation

- `T = R/Z` is the circle, `T(y) = 16y` the continuous map on it, `y_n = {16^n ξ} ∈ [0,1)`,
  `d_n = ⌊16 y_n⌋` (so `y_n = 0.d_n d_(n+1) …` in base 16), `b_m = ⌊2{2^m ξ}⌋` the binary digits
  (`d_n = b_(4n) b_(4n+1) b_(4n+2) b_(4n+3)`).
- Shell measure `ν_B = B^(-1) Σ_(n=B)^(2B-1) δ_(y_n)`; prefix measure `μ_N = N^(-1) Σ_(n<N) δ_(y_n)`;
  `μ_(2B) = (μ_B + ν_B)/2`.
- `μ̂(h) = ∫ e(hy) dμ(y)`, `e(t) = exp(2πit)`; `W_B(h; ξ) = ν̂_B(h)` (as in CARRY_FLUX §0).
- **`M(ξ)`** = the set of weak-* limit points, in the probability measures on the circle `T`, of
  the sequence `(ν_B)_(B≥1)`.
- `Fix = {j/15 : 0 ≤ j ≤ 14} ⊂ T` (fixed points of `T`); `Per_k = {y ∈ T : N_k y = 0}`,
  `N_k = 16^k - 1` (points of period dividing `k`); a point of `T` is periodic iff it is a rational
  with odd denominator. For a finite `T`-invariant set `K` of periodic points, `Δ(K)` is the convex
  hull of the uniform measures on the orbits contained in `K`.
- **Interval quantities** (the convention of `docs/PI_NORMALITY_FRONTIER.md` §5): on `[0,1]` with
  cost `|u-v|`, `F_ν(t) = ν([0,t])`, `W_1(ν,ρ) = ∫_0^1 |F_ν - F_ρ| dt`, `λ` = Lebesgue,
  `Cν = (1/16) Σ_(a=0)^(15) (B_a)_* ν` with `B_a(y) = (a+y)/16`, `Q = C T_*`,
  `G(ν) = W_1(ν, Cν)`, `D(ν) = W_1(ν, Qν)`. For a shell, `T_* ν_B` is the shifted segment
  `B^(-1) Σ_(n=B+1)^(2B) δ_(y_n)`.
- `Fix16 = {j/15 : 0 ≤ j ≤ 15} ⊂ [0,1]`: the *sixteen* points that shell measures can approach on
  the interval. The circle point `0` has two lifts, `0` (digits `000…`) and `1` (digits `FFF…`).
  Forgetting the lift `1` is exactly the error in the provisional threshold `4/225` (LMF-04 (e)).
- Change densities on the shell `[B, 2B)`: `c_B = #{n : d_n ≠ d_(n+1)}/B` (ZSC-02),
  `c^(k)_B = #{n : d_n ≠ d_(n+k)}/B`, and the binary density
  `c^bin_B = #{m ∈ [4B, 8B) : b_m ≠ b_(m+1)}/(4B)`.
- `‖t‖` = distance from `t` to the nearest integer.

Two elementary inequalities are used throughout: `8s² ≤ 1 - cos 2πs ≤ 2π²s²` for `|s| ≤ 1/2`.

---

## LMF-01 — the limit set of shell measures (PROVED LOCAL; (e) uses one IMPORT)

**Theorem.** For every real `ξ`:

```text
(a)  M(ξ) is nonempty and compact;
(b)  every μ ∈ M(ξ) is T-invariant;
(c)  M(ξ) is connected;
(d)  if (u_n) is any real sequence with ‖u_n - 16^n ξ‖ → 0, the shell measures of ({u_n}) have the
     same limit set M(ξ).  In particular M(ξ) = M(ξ + q) for every dyadic rational q,
     M(16ξ) = M(ξ), and M is the same whether it is computed from the completed orbit or from the
     literal rational states U_n of any source gauge-equivalent to one completing to ξ;
(e)  ξ is normal in base 16  ⟺  M(ξ) = {λ}.
```

*Proof.* (a) The probability measures on the compact metric space `T` form a compact metrizable
space. (b) `T_* ν_B - ν_B = (δ_(y_2B) - δ_(y_B))/B` has total variation `≤ 2/B`, and `T` is
continuous on the circle, so `∫ f∘T dμ = ∫ f dμ` for continuous `f` and every limit point `μ`.
(c) `ν_(B+1) - ν_B` has total variation `≤ (B-1)/(B(B+1)) + 1/B + 2/(B+1) ≤ 4/B`. Fix a metric `d`
for the weak-* topology dominated by total variation. A sequence in a compact metric space with
`d(x_B, x_(B+1)) → 0` has a connected limit set: if the limit set were `A ⊔ A'` with `A, A'`
closed, nonempty and `d(A, A') = 3δ`, the sequence would visit the `δ`-neighbourhoods of both
infinitely often with steps eventually `< δ`, hence would lie infinitely often in the compact set
of points at distance `≥ δ` from both, producing a limit point outside `A ∪ A'`.
(d) For Lipschitz `f` on `T` the two shell integrals differ by at most
`Lip(f)·max_(n≥B) ‖u_n - 16^n ξ‖ → 0`, and Lipschitz functions are dense. Dyadic `q`:
`16^n q ∈ Z` for large `n`. `16ξ`: its shell measure is `ν_B` shifted by one step, at total
variation distance `≤ 2/B`. Sources: `U_n + T_n = 16^n ξ` with `T_n → 0` for the zero-seeded
proper source, and a gauge transformation adds `a(n) = ∫_0^1 z^(8n) h(z) dz → 0` (ZSC-06 (a)).
(e) By Weyl's criterion together with Wall's theorem (IMPORT, classical), normality is
`N^(-1) Σ_(n<N) e(h y_n) → 0` for every `h ≠ 0`. Prefix ⟹ shell: `B W_B(h) = 2B μ̂_(2B)(h) - B μ̂_B(h)`.
Shell ⟹ prefix: with `N_0 = N`, `N_(i+1) = ⌊N_i/2⌋`, the interval `[1, N)` is the disjoint union
of the shells `[N_(i+1), 2N_(i+1))` and at most one extra point per level, so if
`|W_B(h)| ≤ ε` for `B ≥ B_0` then `|Σ_(n<N) e(h y_n)| ≤ εN + 2B_0 + log_2 N + 2`. Finally
`W_B(h) → 0` for all `h ≠ 0` iff every `μ ∈ M` has `μ̂(h) = 0` for all `h ≠ 0`, iff `M = {λ}`. ∎

*Falsifier.* A real `ξ` and two shell limits separated by an open gap in `M(ξ)`; a limit point with
`μ̂(16h) ≠ μ̂(h)`.

**Boundary.** `M` is defined on the circle. The interval quantities `W_1`, `G`, `D` are *not*
functions of circle measures (they separate the lifts `0` and `1`), so limits of `W_1(ν_B, λ)` or
`D(ν_B)` are not determined by `M` alone; LMF-04 works on `[0,1]` for that reason.

---

## LMF-02 — the face dictionary (PROVED LOCAL)

**Lemma A (unimodular coefficient).** Let `μ` be a probability measure on `T` and `h ≠ 0`.
`|μ̂(h)| = 1` iff there is `θ` with `μ({y : hy = θ in T}) = 1`; then `μ̂(h) = e(θ)`.
`Re μ̂(h) = 1` iff `μ({y : hy = 0}) = 1`.

*Proof.* If `μ̂(h) = e(θ)` then `∫ (1 - cos 2π(hy - θ)) dμ = 0` with a nonnegative continuous
integrand. The converse is immediate. ∎

**Lemma B (finite support).** (1) A `T`-invariant probability measure gives mass zero to every
point that is not periodic. (2) A `T`-invariant probability measure supported on a finite set `S`
is a convex combination of uniform measures on periodic orbits contained in `S`.

*Proof.* (1) If `p` is not periodic, the sets `T^(-n){p}`, `n ≥ 0`, are pairwise disjoint (a common
point of `T^(-n){p}` and `T^(-m){p}`, `n < m`, gives `T^(m-n) p = p`) and have the same mass.
(2) By (1) the atoms are periodic points. For a periodic `p`, the other fifteen preimages of `Tp`
are not periodic (a periodic preimage lies on the cycle of `Tp`, on which `T` is injective), so
`μ({Tp}) = μ(T^(-1){Tp}) = μ({p})`: the mass is constant along each periodic orbit. ∎

**Theorem.** For `h ≠ 0` and `j ∈ Z/15` put `K_(h,j) = {p ∈ T periodic : hp = j/15 in T}`; it is a
finite `T`-invariant set. For a `T`-invariant probability measure `μ`:

```text
(a)  |μ̂(h)| = 1   ⟺   μ ∈ Δ(K_(h,j)) for some j;   then μ̂(h) = e(j/15), a 15th root of unity;
(b)  Re μ̂(h) = 1  ⟺   μ ∈ Δ(K_(h,0));
(c)  K_(1,j) = {j/15};     K_(15,0) = Fix;     K_(N_k,0) = Per_k;
(d)  each Δ(K) is a closed face of the simplex of T-invariant probability measures.
```

and for every real `ξ`, every `h ≠ 0`:

```text
(e)  limsup_B |W_B(h; ξ)| = max_(μ ∈ M(ξ)) |μ̂(h)|,    limsup_B Re W_B(h; ξ) = max_(μ ∈ M(ξ)) Re μ̂(h);
(f)  uniform modulus saving at h  (∃ η > 0, B_0 : |W_B(h)| ≤ 1 - η for all B ≥ B_0)
          ⟺   M(ξ) ∩ ⋃_j Δ(K_(h,j)) = ∅;
     uniform real saving at h     (∃ η > 0, B_0 : Re W_B(h) ≤ 1 - η for all B ≥ B_0)
          ⟺   M(ξ) ∩ Δ(K_(h,0)) = ∅.
```

*Proof.* (a) By Lemma A, `μ` lives on a coset `{hy = θ}`, which has `|h|` points; by Lemma B it is
a combination of orbit measures of periodic orbits inside the coset. If `p` and `Tp` both lie in
the coset then `15hp = h·16p - hp = 0` in `T`, so `θ = hp ∈ (1/15)Z/Z`. Conversely, if `p` is
periodic and `hp = j/15` then `h·16p = hp + 15hp = hp`, so `K_(h,j)` is invariant and every
`μ ∈ Δ(K_(h,j))` has `μ̂(h) = e(j/15)`. (b) is the case `θ = 0`. (c) Direct: `hp = j/15` with
`h = 1`; `15p = 0`; `N_k p = 0`. (d) If `μ = tμ_1 + (1-t)μ_2` is supported on the closed set `K`,
so are `μ_1, μ_2`. (e) `μ ↦ |μ̂(h)|` and `μ ↦ Re μ̂(h)` are weak-* continuous: a subsequence
realising the limsup has a convergent subsequence, whose limit is in `M`; and every `μ ∈ M` is a
limit along a subsequence. (f) is (e) with (a), (b). ∎

*Falsifier.* An invariant measure with `|μ̂(h)| = 1` and `μ̂(h)^15 ≠ 1`; a real `ξ` with a uniform
saving at mode 1 and `δ_(j/15) ∈ M(ξ)`.

**Corollary (the Basel shell quantity).** For `A ≥ 1` let `ω_A = Σ_(n=A)^(2A-1) n^(-2)`,
`p_n = n^(-2)/ω_A`, `B_A(h; ξ) = Σ_(n=A)^(2A-1) p_n e(h y_n)` (for `ξ = π/16` this is `B_A(h)` of
the frontier §4). Then `1/(2A) ≤ p_n ≤ 2/A`, and for every `ξ`, `h ≠ 0`, `A ≥ 1`:

```text
(g)  (1/2)(1 - Re W_A(h)) ≤ 1 - Re B_A(h) ≤ 2 (1 - Re W_A(h)),
     (1/2)(1 - |W_A(h)|)  ≤ 1 - |B_A(h)|  ≤ 2 (1 - |W_A(h)|).
```

So every rung of LMF-03 that is a uniform real or modulus saving of `W_B(h)` is the same rung for
`B_A(h)`. For `F_h(A; ξ) = Σ_(n≥A) e(h y_n)/n²` and `Ω_A = Σ_(n≥A) n^(-2) ∈ [1/A, 1/(A - 1/2)]`:

```text
(h)  if 1 - Re W_B(h) ≥ η for all B ≥ B_0, then Re(A·F_h(A)) ≤ A Ω_A (1 - η/2) for all A ≥ B_0,
     hence limsup_A Re(A·F_h(A)) ≤ 1 - η/2.   The converse is false.
```

*Proof.* `1/(2A) ≤ ω_A ≤ 4A/((2A-1)(4A-1))` (integral comparison; midpoint convexity of `t^(-2)`),
so `p_n ≥ (2A-1)^(-2)/ω_A ≥ 1/(2A)` and `p_n ≤ A^(-2)/ω_A ≤ 2/A`. (g) Real parts: both sides are
means of the nonnegative numbers `1 - cos 2πh y_n` with weights within a factor 2 of `1/A`.
Moduli: with `B_A = |B_A| e(θ)`, `1 - |B_A| = Σ p_n (1 - cos 2π(h y_n - θ)) ≥ (1/2)(1 - Re e(-θ)W_A)
≥ (1/2)(1 - |W_A|)`, and symmetrically. (h) `Ω_A - Re F_h(A) = Σ_(i≥0) ω_(2^i A)(1 - Re B_(2^i A)(h))
≥ (η/2) Ω_A`. Converse: let `d_n = n mod 2`, except `d_n = 0` for `n ∈ [16^i, 2·16^i]`, `i ≥ 1`.
The non-changes are exactly the positions of the shells `[16^i, 2·16^i)`, so `c_B = 0` at
`B = 16^i`: no uniform real saving at `h = 15` (ZSC-02 (b)). For `A ≥ 16` the weight
`Σ n^(-2)` of the non-changes `n ≥ A` is at most `(0.5243 + 0.0699)/A < (2/3) Ω_A` (first
relevant shell: `≤ L²/((L - 1/2)(2L - 1/2)A)` with `L = 16^i ≥ 16`; later shells: geometric), and
each change has `1 - cos 2π‖15 y_n‖ > 1/3321` (ZSC-02, locality lemma). Hence
`Ω_A - Re F_15(A) ≥ Ω_A/9963` and `limsup_A Re(A·F_15(A)) ≤ 1 - 1/9963`. ∎

---

## LMF-03 — the ladder: rungs are excluded faces (PROVED LOCAL; strictness of two steps uses IMPORTs)

### (a) The lowest rung R0 is the density of binary digit changes

**Lemma (binary locality).** For real `ξ` and `m ≥ 0`: (1) if `b_m = … = b_(m+k-1)` then
`‖2^m ξ‖ ≤ 2^(-k)`; (2) if `‖2^m ξ‖ < 1/4` then `b_m = b_(m+1)`. *Proof.* (1) `{2^m ξ}` and `0` or
`1` lie in a closed binary cylinder of length `2^(-k)`. (2) `[0,1/4)` has bits `00`, `(3/4,1)` has
bits `11`. ∎

**Theorem R0.** For every real `ξ` and `B ≥ 1`, let `q_B` be the fraction of `n ∈ [B, 2B)` for
which one of `b_(4n+i) ≠ b_(4n+i+1)`, `0 ≤ i ≤ 3`, holds. Then `c^bin_B ≤ q_B ≤ 4 c^bin_B` and

```text
(i)    1 - Re W_B(1; ξ)  ≥  q_B / 53  ≥  c^bin_B / 53;
(ii)   1 - Re W_B(1; ξ)  ≤  (k+2)(2 c^bin_B + (k-2)/(2B)) + 2π²·4^(-k)        for every k ≥ 2;
(iii)  if every binary shell [M, 2M), M ≥ M_0, contains at least cM positions m with
       b_m ≠ b_(m+1) (c > 0), then every run of equal binary digits starting at
       m ≥ max(2M_0, 2/c) has length ≤ ((1-c)(m+1) + 2)/(1+c), and
       ‖2^m ξ‖ ≥ 2^( -((1-c)/(1+c))·m - 4 );   in particular v_16(ξ) ≤ (1-c)/(1+c) < 1;
(iv)   ξ - b_0 = Σ_(m≥0) δ_m 2^(-(m+1)),  δ_m = b_(m+1) - b_m ∈ {-1, 0, 1} for ξ ∈ [0,1): the
       nonzero δ_m are exactly the binary changes and alternate in sign.
```

*Proof.* (i) A change at `m = 4n + i` gives `‖2^m ξ‖ ≥ 1/4` by Lemma (2), and
`‖2^m ξ‖ ≤ 2^i ‖y_n‖ ≤ 8‖y_n‖`, so `‖y_n‖ ≥ 1/32` and `1 - cos 2π‖y_n‖ ≥ 1 - cos(π/16) > 1/53`.
(ii) If `b_(4n) = … = b_(4n+k-1)` then `‖y_n‖ ≤ 2^(-k)` and `1 - cos 2π‖y_n‖ ≤ 2π²4^(-k)`.
Otherwise there is a change in `[4n, 4n+k-2]`; a change at `m` spoils at most `(k+2)/4` values of
`n`, and the changes concerned lie in `[4B, 8B)` or among at most `k-2` positions beyond. So there
are at most `((k+2)/4)(4B c^bin_B + k - 2)` spoiled `n`, each contributing at most 2. (iii) As in
ZSC-02 (d): a run `b_m = … = b_(m+L-1)` with `L ≤ m` lies in the shell `M' = ⌈(m+L)/2⌉`, which has
at most `M' - (L-1)` changes, so `L - 1 ≤ (1-c)(m+L+1)/2`; this excludes `L = m` once
`m > 3/(2c)`. If the maximal run at `m` has length `L` and `‖2^m ξ‖ < 2^(-(L+1))`, Lemma (2)
applied to `2^(m+i) ξ`, `i ≤ L-1`, gives `b_(m+L) = b_m`. (iv) `ξ = 2ξ - ξ` digit by digit. ∎

Therefore, with `R0 :⟺ limsup_B Re W_B(1; ξ) < 1`:

```text
R0   ⟺   δ_0 ∉ M(ξ)   ⟺   liminf_B c^bin_B > 0
     ⟺   ξ has no sparse alternating signed-binary expansion along any sequence of shells.
```

(The windows `[4B, 8B)` and the general binary shells `[M, 2M)` differ by at most 3 changes, so
"positive lower shell density of binary digit changes" may be read either way.) R0 is the real part
of the canonical Main XXIV target at `h = 1`; by (g), `R0 ⟺ limsup_A Re B_A(1) < 1`.

### (b) R1 and R2

```text
R1 :⟺  limsup_B |W_B(1; ξ)| < 1    ⟺   M(ξ) contains no δ_(j/15), 0 ≤ j ≤ 14     (LMF-02 (f), (c));
R2 :⟺  (CH): liminf_B c_B > 0      ⟺   limsup_B Re W_B(15; ξ) < 1   (ZSC-02 (a), (b))
                                    ⟺   M(ξ) ∩ Δ(Fix) = ∅                (LMF-02 (f), (c)).
```

`{δ_0} ⊂ {δ_(j/15)} ⊂ Δ(Fix)`, hence **R2 ⟹ R1 ⟹ R0**; quantitatively ZSC-02 (c) for the first
implication and `Re W ≤ |W|` for the second.

### (c) The period-`k` rungs

**Lemma (`k`-locality).** Let `k ≥ 1`, `n ≥ 0`. (1) If `d_(n+i) = d_(n+i+k)` for `0 ≤ i < L`
(`L ≥ 1`), then `‖N_k y_n‖ ≤ N_k·16^(-(L+k)) < 16^(-L)`. (2) If `‖N_k y_n‖ < 16^(-(k+1))`, then
`d_n = d_(n+k)`.

*Proof.* (1) `y_n` and the `k`-periodic point `p` with the same first `k` digits (`p = 1` if they
are all `F`) share `L + k` digits, so `|y_n - p| ≤ 16^(-(L+k))` and `N_k p ∈ Z`. (2) Write
`y_n = a/N_k + t`, `0 ≤ a ≤ N_k`, `|t| < 16^(-(k+1))/N_k`. If `1 ≤ a ≤ N_k - 1`, `p = a/N_k =
0.(w)^∞` with `w` the `k`-digit word of `a`, and the cylinder of the `(k+1)`-digit word `w w_1`
is `[c, c + 16^(-(k+1)))` with `p - c = 16^(-(k+1)) a'/N_k`, `a' = 16a mod N_k ∈ [1, N_k - 1]`;
both margins are `≥ 16^(-(k+1))/N_k`, so `y_n` has the digits `w w_1` and `d_(n+k) = d_n`. If
`a = 0` then `t ≥ 0` and the first `k+1` digits are `0`; if `a = N_k`, they are `F`. ∎

**Theorem (CH_k).** For every real `ξ`, `B ≥ 1`, `k ≥ 1`, `L ≥ 1`:

```text
(a_k)  1 - Re W_B(N_k; ξ)  ≥  8·16^(-2k-2) · c^(k)_B;
(b_k)  1 - Re W_B(N_k; ξ)  ≤  2L (c^(k)_B + (L-1)/B) + 2π²·16^(-2L).
```

Hence, with `(CH_k) :⟺ liminf_B c^(k)_B > 0`:

```text
(CH_k)   ⟺   limsup_B Re W_B(16^k - 1; ξ) < 1   ⟺   M(ξ) ∩ Δ(Per_k) = ∅,
```

`(CH_1) = (CH)` (ZSC-02 has the better constant `1/3321` for `k = 1`), and `(CH_k) ⟹ (CH_j)`
whenever `j | k`.

*Proof.* (a_k) Lemma (2) and `1 - cos 2πs ≥ 8s²`. (b_k) If `d_(n+i) = d_(n+i+k)` for `i < L`,
Lemma (1) and `1 - cos 2πs ≤ 2π²s²`; otherwise there is a `k`-change in `[n, n+L-1]`, which
happens for at most `L(c^(k)_B B + L - 1)` values of `n`. Faces: LMF-02 (f), (c). `j | k`:
`Per_j ⊂ Per_k`. ∎

*Where a naive portmanteau argument fails.* `c^(k)_B = 1 - ν_B(E_k)` with
`E_k = {y : d_0(y) = d_k(y)}`, a union of hexadecimal cylinders, neither open nor closed. Three
things must be checked before writing `ν_B(E_k) → μ(E_k)`: (1) one must work on the **circle**; on
`[0,1)` the map `T` is discontinuous and limits can charge the missing endpoint `1` (digits
`FFF…`), and on `[0,1]` the point `0 ≡ 1` is a boundary point of `E_k` carrying the atom of
`δ_0`, the most important measure in the question; on the circle `0` is interior to `E_k`.
(2) The remaining boundary points are nonzero `16^(k+1)`-adic rationals; a general limit of
measures may charge them, and only **invariance** (Lemma B (1): they are not periodic) gives
`μ(∂E_k) = 0`. (3) `μ(E_k) = 1` is not "support in `Per_k`" without invariance again
(`μ(⋂_n T^(-n) E_k) = 1`). The Fourier route above uses none of this; with (1)–(3) the portmanteau
route gives the same equivalence, and in addition `liminf_B c^(k)_B = 1 - max_(μ∈M) μ(E_k)`.

### (d) All modes, entropy, normality

```text
(AM)   for every h ≠ 0:  limsup_B |W_B(h; ξ)| < 1
         ⟺   M(ξ) contains no finitely supported measure   ⟺   (CH_k) for every k ≥ 1;
(E)    every μ ∈ M(ξ) has positive entropy       ⟹   (AM);
(N)    ξ normal in base 16   ⟺   M(ξ) = {λ}   ⟺   every μ ∈ M(ξ) has entropy log 16.
```

*Proof.* (AM): if `|μ̂(h)| = 1` then `μ` is finitely supported (Lemma A); a finitely supported
invariant `μ` lives on periodic points with a common odd denominator `q`, so `μ̂(q) = 1`, and on
`Per_k` for `k` the least common multiple of the periods. (E): finitely supported invariant
measures have entropy zero. (N): LMF-01 (e), and Lebesgue measure is the unique measure of maximal
entropy `log 16` of `T` (IMPORT, classical). ∎

### (e) The chain and its strictness

```text
(N) ⟹ (E) ⟹ (AM) ⟹ (CH_k) ⟹ (CH_j) (j | k) ⟹ (CH) = R2 ⟹ R1 ⟹ R0.
```

| Step that does not reverse | Witness (digits of `ξ`) | Why |
|---|---|---|
| R0 ⇏ R1 | all digits `1` (`ξ = 1/15`); irrational variant: digit `1` with digit `2` at the squares | `W_B(1) = e(1/15)` exactly: modulus 1, real part `cos(2π/15)`; the variant has `O(√B)` exceptional points per shell |
| R1 ⇏ R2 | runs `1^k 2^k`, `k = 1, 2, …` | `O(√B)` changes per shell, so `c_B → 0`; the shell splits into points within `16^(-3)` of `1/15` and of `2/15` in proportions `1/2 + O(B^(-1/2))` up to `O(√B)` points, so `|W_B(1)| → cos(π/15) < 1` |
| (CH) ⇏ (CH_2) | `0F0F0F…` (`ξ = 1/17`) | `c_B = 1`, `c^(2)_B = 0` |
| (CH_k) ⇏ (CH_k') for `k' ∤ k` | a point of exact period `k'` | `c^(k')_B = 0`; `c^(k)_B > 0` because `k' ∤ k` |
| (AM) ⇏ (E) | superblock `s`: for `k = 1 … ⌊log_2 s⌋ + 1` the word `0^(k-1)1` repeated `⌈s/2^k⌉` times | each `(CH_k)` holds with `liminf c^(k)_B ≥ 1/(3·2^(k+1))`; every `μ ∈ M` is purely atomic on periodic points, hence of entropy zero (IMPORT: entropy is affine under ergodic decomposition) |
| (E) ⇏ (N) | hexadecimal digits `d_n ∈ {0,1}` equal to the bits of the binary Champernowne number | the only shell limit is the Bernoulli(1/2,1/2) measure on digits `{0,1}`, entropy `log 2` (IMPORT: Champernowne) |

*Proofs of the two rows that need one.* Runs `1^k 2^k`: superblock `k` has length `2k` and starts
at `k(k-1)`, so a shell meets `O(√B)` runs and contains whole superblocks except `O(√B)`
positions; a position with `d_n = d_(n+1) = d_(n+2)` has `|y_n - d_n/15| ≤ 16^(-3)`. Period mix:
superblock `s` has length `ℓ_s ∈ [s, 3s]` for `s ≥ 16` and starts at a position `≍ s²`. For
`s ≥ 2^(k+1)` it contains the word `0^k 1` repeated `r = ⌈s/2^(k+1)⌉` times, and each `1` except
the last has `d_(n+k) = 0`: at least `r - 1` `k`-changes among `≤ 3s` positions. For atomicity: the
fraction of positions in stretches of period `> J` is at most `(J+2)/2^J + o(1)`, and positions
at distance `≥ L` from the end of a stretch of period `j ≤ J` are within `16^(-L)` of the orbit of
`0.(0^(j-1)1)^∞`; so every `μ ∈ M` gives mass `≥ 1 - (J+2)/2^J` to a finite set of periodic
points, for every `J`. ∎

Where the earlier witnesses sit: the coherent seed (`ξ = 0`), W1, W2 and the Shallit point
`Σ 16^(-2^k)` have `M = {δ_0}` and fail R0; W3 has `c_B → 1/2`, so it satisfies (CH), and fails
`(CH_2)`.

*Falsifier.* A real `ξ` satisfying a rung and failing a lower one; an explicit shell violating
(i), (ii), (a_k) or (b_k).

---

## LMF-04 — threshold theorems in the canonical units (PROVED LOCAL)

**Theorem (Kantorovich floor).** Let `ν` be a Borel probability measure on `[0,1]`, `h ≥ 1` an
integer, `θ` real. Then

```text
(a)  W_1(ν, λ)  ≥  (1/h) ( 1/4 - ∫ ‖hy - θ‖ dν(y) );
(b)  if 16 ∤ h:    G(ν) = W_1(ν, Cν)  ≥  (1/h) ( 1/4 - ∫ ‖hy - θ‖ dν(y) );
(c)  ∫ ‖hy - θ‖ dν  ≤  sqrt( (1 - Re e(-θ) ν̂(h)) / 8 ),   so with the best θ
     W_1(ν, λ)  and (16 ∤ h)  G(ν)   are   ≥  (1/h) ( 1/4 - sqrt( (1 - |ν̂(h)|)/8 ) ).
```

Consequently `W_1(ν, λ) ≤ 1/(4h) - ε` (or, for `16 ∤ h`, `G(ν) ≤ 1/(4h) - ε`) forces
`|ν̂(h)| ≤ 1 - 8h²ε²`. The constant `1/(4h)` in (a) cannot be increased: the uniform measure on the
`h` points `(i + 1/2)/h` has `|ν̂(h)| = 1` and `W_1 = 1/(4h)`.

*Proof.* `φ(y) = ‖hy - θ‖/h` is 1-Lipschitz on `[0,1]` with `∫_0^1 φ dλ = 1/(4h)`. For
probability measures `ν, ρ` on `[0,1]`, integration by parts gives
`∫ φ d(ρ - ν) = ∫_0^1 φ'(t)(F_ν(t) - F_ρ(t)) dt ≤ W_1(ν, ρ)`. (a) is `ρ = λ`. (b) is `ρ = Cν`:
`∫ φ dCν = ∫ ψ dν` with `ψ(y) = (1/16) Σ_a φ((a+y)/16) = (16h)^(-1) Σ_a ‖hy/16 - θ + ha/16‖`. With
`g = gcd(h, 16) < 16`, the numbers `ha/16 mod 1` run `g` times through the `N = 16/g` points of
`(1/N)Z/Z`, `N` even, and `Σ_(r<N) ‖s + r/N‖ = N/4` for every `s` because
`‖u‖ + ‖u + 1/2‖ = 1/2`. So `ψ ≡ 1/(4h)`. (c) Cauchy–Schwarz and `8s² ≤ 1 - cos 2πs`. ∎

**Shell form.** For every real `ξ` and `B ≥ 1` (re-derivation of the Main XXIV reconstruction of
`zero_anchored_lambda_haar/CONSTRUCTION.md` §2 for a shell segment — the proof there uses only
that the segment is consecutive):

```text
(d)  | D(ν_B) - G(ν_B) |  ≤  |y_2B - y_B| / (16B)  ≤  1/(16B);
     (15/16) W_1(ν_B, λ) - 1/(16B)  ≤  D(ν_B)  ≤  (17/16) W_1(ν_B, λ) + 1/(16B).
```

*Proof.* `T_* ν_B - ν_B = (δ_(y_2B) - δ_(y_B))/B`, `C` multiplies interval `W_1` distances by
`1/16`, `Cλ = λ`, and `ν - λ = (ν - Qν) + C(T_*ν - ν) + C(ν - λ)`. ∎

**Corollary (rung thresholds).** For every real `ξ` and every `B ≥ 1`:

```text
(R1)   W_1(ν_B, λ) ≤ 1/4 - ε   or   D(ν_B) ≤ 1/4 - ε - 1/(16B)      ⟹   |W_B(1)| ≤ 1 - 8ε²;
(h)    W_1(ν_B, λ) ≤ 1/(4h) - ε   or (16 ∤ h)   D(ν_B) ≤ 1/(4h) - ε - 1/(16B)
                                                                    ⟹   |W_B(h)| ≤ 1 - 8h²ε²;
(CH)   for every k ≥ 2:
       W_1(ν_B, λ)  and  D(ν_B) + 1/(16B)   are   ≥  1/60 - (k-1)(c_B + (k-1)/B)/30 - 16^(-k);
       so  W_1(ν_B, λ) ≤ 1/60 - ε   or   D(ν_B) ≤ 1/60 - ε - 1/(16B)   forces
       c_B  ≥  15ε/(k_ε - 1) - (k_ε - 1)/B,      k_ε = max(2, ⌈log_16(2/ε)⌉).
```

In particular

```text
limsup_B W_1(ν_B, λ) < 1/4    or  limsup_B D(ν_B) < 1/4     ⟹   R1 (hence R0);
limsup_B W_1(ν_B, λ) < 1/60   or  limsup_B D(ν_B) < 1/60    ⟹   (CH);
limsup_B W_1(ν_B, λ) < 1/(4N_k)  or  limsup_B D(ν_B) < 1/(4N_k)   ⟹   (CH_k)  (and a modulus saving
                                                                          at mode N_k);
normality                                                    ⟺   W_1(ν_B, λ) → 0  ⟺  D(ν_B) → 0.
```

Example: a shell with `W_1(ν_B, λ) ≤ 1/120` has `c_B ≥ 1/8 - 1/B`.

*Proof.* (R1), (h): (c) and (d). (CH): take `h = 15`, `θ = 0` in (a), (b). A position with
`d_n = … = d_(n+k-1)` has `‖15 y_n‖ ≤ 15·16^(-k)` (ZSC-02, locality lemma (1)); the other positions
of the shell number at most `(k-1)(c_B B + k - 1)` (ZSC-02 (b), proof) and have `‖15 y_n‖ ≤ 1/2`.
So `(1/15)·mean ‖15 y_n‖ ≤ (k-1)(c_B + (k-1)/B)/30 + 16^(-k)`. With `16^(-k) ≤ ε/2` the displayed
bound on `c_B` follows. Normality: LMF-01 (e), (d), and `W_1`-convergence to `λ` is weak
convergence. ∎

**(e) Sharpness, and the two provisional constants.**

1. *The minimum over the sixteen fixed points is `1/60`, for both functionals.*
   `min {W_1(ν, λ) : ν on Fix16} = min {G(ν) : ν on Fix16} = 1/60`, attained at
   `ν* = (1/30)δ_0 + (1/15) Σ_(j=1)^(14) δ_(j/15) + (1/30)δ_1`. Lower bound: (a), (b) with
   `h = 15`, `θ = 0` (the integral vanishes on Fix16). Exact LP-duality certificate:
   `faces_core.fix16_dual_certificate` (the dual witness is `φ'`, the sign pattern of period
   `1/15`; all sixteen vertex values equal `1/60`; the primal point `ν*` attains `1/60`).
2. *The thresholds `1/60` cannot be increased.* For the point `S*` with superblocks
   `0^k 1^(2k) 2^(2k) … E^(2k) F^k` (`k = 1, 2, …`): `c_B → 0`, `W_1(ν_B, λ) → 1/60`,
   `D(ν_B) → 1/60`. (A shell contains whole superblocks, which have the proportions of `ν*`,
   except `O(√B)` positions; within a run of digit `j` the distances `|y_n - j/15|` sum to less
   than `1/15`; so `W_1(ν_B, ν*) = O(B^(-1/2))`, and `W_1(·, λ)` is 1-Lipschitz, `G` is
   `17/16`-Lipschitz for `W_1`.)
3. *The provisional threshold `4/225` for `W_1` is false.* `4/225` is
   `min {W_1(ν, λ) : ν on the fifteen points j/15 < 1}` (exact, `faces_core.min_w1_fix15`); it is
   the wrong set, because shell measures on `[0,1)` approach the lift `1`. Explicit receipt: the
   shell `B = 30k` consisting of the single superblock `0^k 1^(2k) … E^(2k) F^k` followed by
   `F`'s has `c_B = 1/(2k)` and `W_1(ν_B, λ) ≤ 1/60 + 16/(450k) < 4/225` for every `k ≥ 33`
   (`k = 40`: `c_B = 1/80`, `W_1 = 0.016611…`). The provisional `D`-threshold `1/60` is correct,
   by coincidence of two different constants (`(15/16)(4/225) = 1/60` was the provisional
   derivation; the true reason is item 1).
4. *The thresholds `1/4` cannot be increased.* Runs `0^k F^k`: `M = {δ_0}`, so R0 fails, and
   `W_1(ν_B, λ) → 1/4`, `D(ν_B) → 1/4` (limit `(δ_0 + δ_1)/2` on the interval). For R0 and for R1
   the threshold is the same: `inf W_1(·, λ)` over `{aδ_0 + (1-a)δ_1}` is `1/4` (at `a = 1/2`),
   over single fixed-point masses it is `113/450 > 1/4` (at `7/15`, `8/15`), and `G ≥ 1/4` on
   both families with equality at `(δ_0 + δ_1)/2`, `δ_(7/15)`, `δ_(8/15)`.
5. *The elementary bound.* `|ν̂(h)| ≤ 2πh·W_1(ν, λ)` (the function `e(h·)` is `2πh`-Lipschitz) is
   stronger than (c) when `W_1` is small and gives a saving only below `1/(2πh) < 1/(4h)`. The
   content of this theorem is the sharp constant, not a new mechanism.

*Falsifier.* A probability measure on `[0,1]` violating (a) or (b); a real `ξ` with
`limsup W_1(ν_B, λ) < 1/60` and `liminf c_B = 0`.

---

## LMF-05 — mass on the fixed points: the prefix thresholds (PROVED LOCAL)

The linear bound of LMF-04 is useless for prefix measures (the first half of a prefix may be
anything). The following quadratic bound is not.

**Lemma (Fix-mass).** Let `ρ` be a probability measure on `[0,1]` with `ρ({j/15}) ≥ J_j ≥ 0` for
`0 ≤ j ≤ 15`, and `a = Σ_j J_j`. With `ψ(v) = ∫_0^(1/30) (v - s)^+ ds`:

```text
(a)  W_1(ρ, λ)  ≥  ψ(J_0) + ψ(J_15) + Σ_(j=1)^(14) 2ψ(J_j/2)  ≥  a²/60,
```

with equality in the second inequality iff `J = a·(1/30, 1/15, …, 1/15, 1/30)`. For every
`a ∈ [0,1]` the value `a²/60` is attained by some `ρ`.

*Proof.* On the window `(p - 1/30, p + 1/30)` around an interior `p = j/15`, with `f = F_ρ(p^-)`:
`F_ρ ≤ f` to the left and `F_ρ ≥ f + J_j` to the right, so the window contributes at least
`ψ(u) + ψ(J_j - u) ≥ 2ψ(J_j/2)` (`u = p - f`; `ψ` is convex). The windows `[0, 1/30)` and
`(29/30, 1]` contribute `ψ(J_0)` and `ψ(J_15)`. The sixteen windows are disjoint. Second
inequality: the tangent of `ψ` at `v_0 = a/30` gives `ψ(v) ≥ (a/30)v - a²/1800`; summing,
`(a/30)a - 15a²/900 = a²/60`. Attained by `F_ρ(t) = t` off the windows of half-width `a/30`
(interior) and width `a/30` (endpoints), flat inside them apart from the jumps. ∎

**Lemma (jump).** If a probability measure `ρ` on `[0,1]` gives mass `≥ J` to an arc of the circle
of length `ℓ ≤ J` (an interval, or `[0,t] ∪ [1-t,1]` with `ℓ = 2t`), then
`W_1(ρ, λ) ≥ (J - ℓ)²/4`.

*Proof.* Interval `[p, p+ℓ]`, `f = F_ρ(p^-)`: the cost is at least
`((p - f)^+)²/2 + ((f + J - p - ℓ)^+)²/2 ≥ (J - ℓ)²/4`. Wrapped arc with masses `a, b`, `a + b ≥ J`:
on `(t, 1-t)`, `F_ρ ∈ [a, 1-b]`, an interval of length `≤ 1 - J`. ∎

**Theorem (prefix thresholds).** For every real `ξ`, `B ≥ 1`, `k ≥ 2`, `N ≥ 2B`, with `β` the
fraction of `n ∈ [B, 2B)` for which `d_n, …, d_(n+k-1)` are not all equal
(`β ≤ (k-1)(c_B + (k-1)/B)`) and `a = (1-β)B/N`:

```text
(b)  W_1(μ_N, λ)  ≥  a²/60 - a·16^(-k);
(c)  if W_1(μ_(2B), λ) ≤ 1/240 - ε and 16^(-k) ≤ ε, then β ≥ 60ε, hence
     c_B ≥ 60ε/(k-1) - (k-1)/B;
(d)  if W_1(μ_(2B), λ) ≤ 1/16 - ε  (0 < ε ≤ 1/16),  then |W_B(1)| ≤ 1 - 32ε³.
```

So `limsup_N W_1(μ_N, λ) < 1/240` implies (CH), and `limsup_N W_1(μ_N, λ) < 1/16` implies R1; by
the Main XXIV inequality `W_1(μ_N, λ) ≤ (16/15) D_N + 1/(15N)`, so do `limsup_N D_N < 1/256` and
`limsup_N D_N < 15/256` respectively.

*Proof.* (b) Move the `(1-β)B` good points to their fixed points, at cost `≤ a·16^(-k)`, and apply
the Fix-mass lemma. (c) `(1-β)²/240 - 16^(-k)/2 ≤ 1/240 - ε` gives
`1 - (1-β)² ≥ 240(ε - 16^(-k)/2) ≥ 120ε`. (d) If `|W_B(1)| = 1 - η`, at most `ηB/(8t²)` points of
the shell are farther than `t` (on the circle) from the argument of `W_B(1)`; the jump lemma with
`J = (1 - η/(8t²))/2`, `ℓ = 2t`, `t = ε` gives `η ≥ 32ε³`. ∎

**Status of the provisional prefix constants.** The provisional value
`min W_1((μ' + ν)/2, λ) = 1/120` (`ν` on the fixed points, `μ'` arbitrary) is **false**: the
minimum is `1/240` (lemma with `a = 1/2`; an explicit rational measure within `1/7200` of it is
`faces_core.half_prefix_extremal`). The proved sufficient thresholds are therefore `1/240` for
`W_1(μ_N, λ)` and `1/256` for `D_N`, not `1/120` and `1/128`. Whether `1/240` is sharp *for
orbits* (a point with (CH) false and all large prefixes below a larger constant) is **not
determined**: the extremal measure is not shown to be a limit of prefixes.

*Falsifier.* A probability measure with `ρ({j/15}) ≥ J_j` and `W_1(ρ, λ) < a²/60`.

---

## LMF-06 — hostile controls and instances

A threshold theorem that a coherent control passes is wrong. Exact values and the largest witness
shell `B = 1500` of `RESULTS_rungs.json` (decimals truncated):

| Point | `c_B` | `W_1(ν_B, λ)` | `D(ν_B)` | rungs |
|---|---|---|---|---|
| coherent seed `s = -x` (completed orbit `0`) | 0 | `1/2` exactly | `15/32` exactly | fails R0; above every threshold |
| constant digit 7 (`ξ = 7/15`) | 0 | `113/450` | `1/4` | R0 holds, R1 fails; not below `1/4` |
| W1 (ZSC-05) | 0.041 | 0.4986 | 0.4674 | fails R0 |
| W2 (ZSC-05) | 0.000 | 0.4999 | 0.4687 | fails R0 |
| Shallit point | 0.001 | 0.4999 | 0.4687 | fails R0 |
| runs `0^k F^k` | 0.021 | 0.2485 | 0.2485 | fails R0; `W_1, D → 1/4` |
| runs `1^k 2^k` | 0.021 | 0.4047 | 0.3828 | R1 holds, (CH) fails |
| `S*` (LMF-04 (e) 2) | 0.044 | 0.0185 | 0.0185 | (CH) fails; `W_1, D → 1/60` |
| W3 (ZSC-05) | 0.506 | 0.4505 | 0.4224 | (CH) holds far above the threshold: the thresholds are sufficient, not necessary |

The threshold inequalities of LMF-04 and LMF-05 were checked on every shell of every string of
the probe (exact arithmetic where no cosine is involved).

**OBSERVED (instances, not evidence).** For `ξ = π/16`, on the preregistered fresh holdout shells
(data path authenticated first: the high-precision path, the integer series of the frozen source
with a rigorous enclosure, and the exact zero-seed carrier on `1 ≤ n ≤ 2600` give identical
digits):

| `B` | `W_1(ν_B, λ)` | `D(ν_B)` | `c_B` | `c^bin_B` | `Re W_B(1)` | `Re W_B(15)` |
|---|---|---|---|---|---|---|
| 3301 | 0.002927 | 0.002921 | 0.932444 | 0.495986 | 0.010340 | 0.020879 |
| 4099 | 0.003565 | 0.003568 | 0.934618 | 0.497072 | 0.016044 | 0.009595 |
| 5003 | 0.006074 | 0.005820 | 0.933839 | 0.500399 | 0.011836 | 0.002434 |
| 6007 | 0.003690 | 0.003614 | 0.934243 | 0.499750 | 0.007252 | 0.002199 |

All four shells are below `1/60` in both units (on the calibration shells `B = 64, 128` they are
not: `W_1 ≈ 0.026, 0.025`, the size expected of any 64- or 128-point sample). These are the
values a generic point shows; a finite set of shells says nothing about `limsup`, and the same
holds for the two pseudo-random control strings. Predictions RP-1…RP-4 of the preregistration
were met; mutation controls RM-1…RM-3 behaved as preregistered.

---

## Reading

1. **What the rungs are.** A rung of the signed ladder is the statement that the limit set
   `M(ξ)` of shell measures avoids a closed face of the simplex of `×16`-invariant measures:
   `{δ_0}` for R0, the fifteen vertices `δ_(j/15)` for R1, the simplex `Δ(Fix)` for R2 = (CH),
   `Δ(Per_k)` for `(CH_k)`, all finitely supported invariant measures for savings at every mode;
   normality is `M = {λ}` (LMF-02, LMF-03). The lowest rung R0 — the real part of the canonical
   target at `h = 1` — is equivalent to a positive lower shell density of binary digit changes
   (LMF-03 (a)), and it already costs a restricted exponent `< 1` at the denominators `2^m`
   (LMF-03 (a)(iii), consistent with ZSC-01). R0 for π is OPEN, as are all higher rungs.
2. **What the thresholds say.** In the units of Main XXIV, R1 follows from
   `limsup_B D(ν_B) < 1/4` and (CH) from `limsup_B D(ν_B) < 1/60`, whereas normality is
   `D(ν_B) → 0`; the coherent control sits at `15/32` (LMF-04). The constants are sharp for shell
   measures. This is Kantorovich duality with a triangle wave; it converts a fixed quantitative
   defect bound into a rung, and it provides **no** such bound. Proving `limsup D(ν_B) < 1/4` for
   the zero-seeded source would be a source-selected signed estimate, and none is known.
3. **What changed in the provisional constants.** `4/225` (fifteen points) is replaced by `1/60`
   (sixteen points: the lift `1`); the prefix constants `1/120`, `1/128` are replaced by `1/240`,
   `1/256` (LMF-04 (e) 3, LMF-05).
4. **What is not claimed.** No statement here distinguishes π from a generic point or from a
   hostile point; `M(π/16)` is not known to avoid any face, including `{δ_0}`. The observed values
   are instances. The entropy rung is defined and placed in the chain; no tool for proving it is
   offered. Sharpness of the prefix thresholds for orbits is not determined. The proofs are
   same-model and unaudited at the time of writing.

## Summary of statements

| ID | Statement | Status |
|---|---|---|
| LMF-01 | `M(ξ)` nonempty, compact, connected, invariant; depends only on `ξ` mod dyadic rationals and is gauge-invariant; normal ⟺ `M = {λ}` | PROVED LOCAL (Weyl–Wall IMPORT in (e)) |
| LMF-02 | invariant `μ` with `\|μ̂(h)\| = 1` ⟺ `μ ∈ Δ(K_(h,j))`, value `e(j/15)`; savings ⟺ excluded faces; Basel sandwich with constants `1/2, 2`; `A·F_h` one-directional, converse false | PROVED LOCAL |
| LMF-03 | R0 ⟺ binary change density, constants `1/53` and (ii), cost `(1-c)/(1+c)` at `2^m`; R1; `(CH_k)` ⟺ real saving at `16^k - 1`, constants `8·16^(-2k-2)` and `(b_k)`; (AM), (E), (N); chain with strictness witnesses | PROVED LOCAL (three IMPORTs in (d), (e)) |
| LMF-04 | `W_1(ν, λ)`, `G(ν)` `≥ (1/h)(1/4 - ∫‖hy - θ‖dν)`; shell thresholds `1/4` (R1), `1/60` ((CH)), `1/(4N_k)` (`(CH_k)`), all sharp for shells; `4/225` refuted | PROVED LOCAL |
| LMF-05 | Fix-mass lemma `a²/60`; jump lemma; prefix thresholds `1/240`, `1/16` for `W_1` and `1/256`, `15/256` for `D_N`; `1/120` refuted; orbit sharpness not determined | PROVED LOCAL |
| LMF-06 | controls on the correct side; π holdout values | exact checks / OBSERVED |
| — | R0, R1, (CH), `(CH_k)`, (AM), (E), normality for π | **OPEN** |
