# Round 2 — Consolidated Dossier (f₄ edge-isolation, BGK sharpening, joint equidistribution)

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02` (off `origin/main` `81045770`).
**Sibling consumed:** `research/selected-prime-window-energy-2026-11-01` (PWI-01..07).

**Verdict in one line:** the f₄ edge-isolation yields a *cleaner* decoupling and a new exact structure (rank-1 kernel), but — as three fronts prove — it does **not** transfer the isolated-clock BGK saving to the full sum; the mixed cross-term remains blocked at the single signed-cancellation gate. One genuine quantitative improvement this round: the BGK exceptional set is sharpened from `o(X/log X)` to a power saving `O(X^{2γ})`. π normality and RH remain OPEN.

---

## 1. New exact structure (PROVED, all exact Fraction)

**fₘ decomposition.** The four-pole forcing splits exactly:
$$ r(n)=2f_3(n)+f_4(n)+f_5(n),\quad f_m(n)=\frac1{8n-7}-\frac1{8n-7+m}. $$

**f₄ pole-isolation.** For `p≡5 mod 8`, `p=8a_p-3`, the `-1/p` pole is carried *exclusively* by `f_4(a_p)=1/(p-4)-1/p`. Hence within the window:
$$ U_n=-\frac{16^{n-a_p}}p+V_{p,n},\qquad V_{p,n}=2\sum_{j\le n}16^{n-j}f_3(j)+\sum_{j\le n}16^{n-j}f_5(j)+\Big[\sum_{j\le n}16^{n-j}f_4(j)+\frac{16^{n-a_p}}p\Big], $$
the bracket p-free. **Clock and cofactor now arise from disjoint forcing edges** (a *cleaner* separation than SPP-01).

**Rank-1 kernel.** `16^{n-j}=16^n\cdot16^{-j}` is exactly rank-1; consequently `U_n=16^n S_n` with `S_n\to\pi/16` (BBP, exponential tail). The cofactor therefore *completes* to the transcendental clock `16^{n-1}\pi`.

## 2. The transfer is blocked (PROVED obstruction, three independent reasons)

1. **Partial summation (Abel) fails** — `V_{p,n+1}-V_{p,n}=15V_{p,n}+r(n+1)`, so the cofactor's total variation over the window is `≍ |h|16^{p/2} ≫ L_p`. No slow variation.
2. **Bilinear reorganization fails** — the only bilinear form is diagonal with unit-modulus lacunary entries (the Weyl-sum worst case); kernel = identity; hypotheses (smoothing, spacing, regularity) all fail at the exact level.
3. **Base-point lift** — BGK lives on `⟨16⟩⊂F_p^×` (rational base `-1/p`); the rank-1 completion lifts it to `\pi/16` (transcendental), where no exponential-sum theorem reaches. The object is the lacunary Weyl sum `Σ_n e(h·16^{n-1}\pi)`.

**The f₄ isolation is a refinement of the exact structure, not a new lever.**

## 3. Genuine quantitative improvement (PROVED, elementary, unconditional)

**Exceptional-set power saving.** The BGK isolated-clock bound `|C_p(h)|/L_p\le 1/3+o(1)` holds outside `{p: d_p<p^\gamma}`. This round sharpens that exceptional set via cyclotomic factorization `p|\Phi_d(16)`:
$$ \#\{p\le X:d_p<p^\gamma\}\ \le\ \sum_{d\le X^\gamma}\omega(\Phi_d(16))\ \le\ 2X^{2\gamma}(1+o(1)), $$
a power saving `O(X^{2\gamma})`, strictly smaller than the handoff's `o(X/log X)` for every `\gamma<1/2`. (With the sharper `\omega(\Phi_d(16))=O(\varphi(d))`, the constant is `(12/\pi^2)X^{2\gamma}`.) Verified numerically to `X=10^6` (actual exceptional counts far below the bound).

**The `1/3` constant is sharp** (PROVED): the half-period remainder cannot be reflected into a complete Gauss sum, because `16^{(d_p-1)/2}\equiv -4^{-1}`, i.e. the "reflected partner" is a **non-involutive `(-4)`-dilation**, itself an incomplete geometric sum of the same length. Below `1/3` would require a sub-linear bound on partial geometric sums — equivalent to the open signed-cancellation gate.

**Reaching `X^{1-\delta}`** (uniform, δ independent of γ) is an **Artin-type open question** (distribution of small `ord_p(16)`); NOT claimed.

## 4. Joint equidistribution: the correct hypothesis (PROVED reframing)

The *literal* joint-equidistribution H0 is **provably false**: the clock `16^{n-a_p} mod p` lives in the subgroup `⟨16⟩` of size `≤(p-1)/4`, so it never equidistributes on `Z/p`. The correct statement is **conditional independence H1**: *conditioned on the clock class, the cofactor phase `hV_{p,n} mod 1` is uniform on the circle*. This is exactly equivalent to normality (the cofactor phase is slaved to `e(h·16^{n-1}\pi)`, the π-digit phase in disguise).

**p-integrality gives no handle** (PROVED category error): it is a p-adic valuation fact, orthogonal to the real-circle phase, and shared by every same-forcing carrier.

**Finite test** (exact Fraction, two methods agreeing to ~40 digits, `dps≥6N_max/ln10+60`): over the first 44 primes, the cofactor phase *conditioned on clock class* has χ²/dof ≈ 0.97/1.02/1.04 ≈ 1 (consistent with uniform), `cov_stat` tiny and sign-alternating. Consistent with H1; finite; no proof.

## 5. Bottom line

- **PROVED (new):** fₘ decomposition, f₄ pole-isolation, rank-1 kernel, exceptional-set power saving `O(X^{2γ})`, sharpness of the `1/3` constant, and the exact correction H0→H1.
- **PROVED (obstructions):** partial summation, bilinear reorganization, and base-point lift all block the transfer of the isolated-clock saving to the full mixed sum.
- **OPEN (unchanged):** `sup_{|h|≤16^{m-1}}|S_N(h)|=O(N^\theta)`, `\theta<1` — equivalently `Σ_{n≤N}e(h·16^{n-1}\pi)=o(N)`.

**π base-16 normality and RH remain OPEN. No proof claimed; no false victory.**
