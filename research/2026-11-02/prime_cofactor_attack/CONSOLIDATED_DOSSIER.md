# Selected Prime–Cofactor Non-Conspiracy Conjecture — Consolidated Attack Dossier

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02` (off `origin/main` `81045770`).
**Conjecture (PR #459 / selected_prime_phase):** for every fixed `h≠0` there is `η_h>0` with
$$ \sum_{5<p\le X,\ p\equiv5\,(8)}\Big|\sum_{n=a_p}^{b_p}e\!\big(-\tfrac{h16^{n-a_p}}p\big)e(hV_{p,n})\Big|^2 \ll_h \frac{X^3}{(\log X)^{1+\eta_h}}, $$
`a_p=(p+3)/8`, `b_p=(p+1)/2-1`, `V_{p,n}=U_n+16^{n-a_p}/p` the p-integral cofactor.

**Verdict in one line:** the conjecture is **exact, well-posed, and equivalent in hardness to base-16 normality of π**; three independent fronts converge on the conclusion that the "prime clock × cofactor" factorization is a *red herring* (the tower identity in disguise), the correct normalization is the small BBP tail `T_n`, and no known exponential-sum theorem reaches it. π normality and RH remain OPEN.

---

## 1. The single decisive identity (all three fronts, PROVED)

The factorization named in the conjecture is exact (SPP-01), but it is **not** a product of independent factors. The tower identity
$$ U_n = 16^{n-a_p}U_{a_p} + \underbrace{\sum_{j=a_p+1}^n 16^{n-j}r(j)}_{W_{p,n}} $$
shows the clock `16^{n-a_p}` and cofactor `V_{p,n}` share the same multiplier 16, and their product collapses:
$$ e\big(-\tfrac{h16^{n-a_p}}p\big)e(hV_{p,n})=e(hU_n)=e\big(h\,16^{n-a_p}U_{a_p}\big)e(hW_{p,n}). $$
Therefore
$$ \boxed{R_p(h)=\sum_{n=a_p}^{b_p}e(hU_n)=S_{b_p}(h)-S_{a_p-1}(h),}\qquad S_N(h)=\sum_{n\le N}e(hU_n). $$

**`R_p(h)` is literally a suffix (prime-window block) of the authentic Weyl sum.** The conjecture is a *large-sieve-over-prime-windows* second-moment bound on the original Weyl sum — a reorganization, not a new object. Proving it is exactly as hard as `S_N(h)=o(N)`.

## 2. The real factorization (Front 1's key reframing, PROVED)

There are *two* exact factorizations, and the conjecture names the wrong one:

- **(A) The correct one (small cofactor):** `U_n = 16^{n-1}π - T_n`, `T_n=Σ_{k≥1}16^{-k}r(n+k)`, with `T_n = O(n^{-2}·16^{-1})` **exponentially tiny** in the window. So `e(hU_n)=e(h·16^{n-1}π)·e(-hT_n)`, `e(-hT_n)→1`. The meaningful "cofactor" is `T_n` — the small BBP tail — multiplying the leading lacunary phase `e(h·16^{n-1}π)`.
- **(B) The conjecture's "prime clock × cofactor":** `U_n = c_p16^{n-a_p}/p + V_{p,n}`. Here `V_{p,n}` has **full magnitude** `≈16^{n-1}π`, not small (verified: at `p=13, n=20`, `V≈2.4×10²³` = `U_n` itself). The "clock" `c_p16^{n-a_p}/p` is astronomically large, not a unit phase. Factorization (B) is `e(hU_n)=e(hU_n)` restated, inverting the true roles of "clock" (small) and "cofactor" (large).

**The mathematically meaningful attack target is factorization (A), not (B).** Any genuinely new input must live in the small BBP tail `T_n`'s exact rational structure.

## 3. Why the standard theorems all miss (Front 1, PROVED structural)

| Method | Why it fails |
|---|---|
| **BGK** (subgroup sums) | bounds the *complete* subgroup `Σ_{x∈⟨16⟩}e(ax/p)`; the window is a *partial* geometric segment (`M_p≈3p/8≈6·ord_p(16)`, incomplete periods), and `ord_p(16)≤(p-1)/4` so `⟨16⟩` is below BGK's `p^δ` threshold |
| **van der Corput** | the phase `e(h·16^{n-1}π)` is *lacunary* (exponential growth), no stationary region; lacunarity = the Weyl-normality problem itself |
| **Weil/Deligne** | base point π is transcendental; no finite-field algebraic `f(x)/p` object exists |
| **large sieve** | phase nonlinear in `n`; point set `{16^m/p}` not well-spaced (clustered in `⟨16⟩`) |

These are the *same* obstruction in four guises: the object is the Weyl sum of the base-16 digits of π.

## 4. Corrected quantitative structure (Front 3, PROVED — fixes a handoff error)

The windows **overlap heavily** (each `n` lies in `~n/log n` windows `{p:2n+1≤p≤8n-3}`). Opening the square with cross-prime multiplicity `w_X(n,m)`:
$$ \sum_p|R_p|^2=\sum_{n,m}w_X(n,m)\,e(h(U_n-U_m)). $$

**Correction to the handoff's constants.** The handoff's trivial bound `3X³/(64 log X)` omits the `φ(8)=4` class-density factor (primes `p≡5 mod 8` are ¼ of all primes). The correct constants are:
$$ \sum_p|W_p|\sim\frac{3}{64}\frac{X^2}{\log X},\qquad \sum_p|W_p|^2\sim\frac{3}{256}\frac{X^3}{\log X}. $$
(Numerically verified to ratio `→1` at `X=10^5`; the handoff's own numbers are also internally inconsistent by a further factor 2.)

**The conjecture's `(log X)^{-η}` saving is exactly the off-diagonal signed two-time cancellation** `Σ_{n≠m}e(h(U_n-U_m))` — the single bottleneck, unchanged.

## 5. Hostile controls with correct precision (Front 3, OBSERVED FINITE)

A **false refutation was caught and corrected** this round: `mp.dps=200` (insufficient for `16^{X/2}`) produced a spurious `M/T→1` "coherence". With exact `Fraction` residues at `dps≥6N_max/ln10+60`, two independent methods agree to `~-dps` digits:

| control | M/T at X=256 / 512 / 1024 | interpretation |
|---|---|---|
| **authentic** (U₀=0) | 0.0199 / 0.0089 / 0.0035 | decays ≈ 1/X, matches Haar |
| coherent s=-π/16 | 1.000 / 1.000 / 1.000 | saturates — correctly fails |
| all-zero | 1.000 / 1.000 / 1.000 | saturates |
| Haar (random) | 0.0119 / 0.0041 / 0.0012 | decays ≈ 1/X |
| p=257 clock | 0.254 / 0.253 / 0.252 | pinned at |mean|²=0.25, non-decaying |

The authentic orbit's `M/T ~ 1/X` is **consistent with normality** (and far stronger than the conjecture's weak `(log X)^{-η}`), but it is **finite** (X≤1024, 44 primes) — it cannot distinguish `1/X` from any mild decay, and it is **not a proof**.

## 6. The cofactor's exact structure gives no leverage (Front 2, PROVED)

The cofactor is fully characterized and **generic**:
- `r(n)=(960n²-712n+128)/D(n)` (quadratic numerator, exact); `r(n)=15/(64n²)+O(n⁻³)>0`.
- `V_{p,n}=16^{n-a_p}(U_{a_p}-c_p/p)+W_{p,n}` (exact); p-integral throughout the window (congruence lemma, PROVED).
- `W_{p,n}` is the *same kind* of 16-geometric sum as `U_{a_p}`, ~3× longer — **strictly harder**, not simpler.
- `V_{p,n} mod 1`, `W_{p,n} mod 1` have **no finite periodicity** (denominator bit-length grows Θ(n log n)).

Crucially: the quadratic numerator, tower identity, p-integrality, and no-periodicity are **all shared by every carrier with the same forcing** (including the SCB-07/E7 normal and non-normal changed-seed counterexamples). So none can distinguish π. The sub-trivial bound is **provably equivalent to normality** (SCB-06), and the cofactor framing **adds no new leverage**.

## 7. Bottom line and remaining lemma

- **Proved:** `R_p(h)` is a prime-window block of the authentic Weyl sum; factorization (B) is a red herring; factorization (A) (small tail `T_n`) is the correct target; the handoff's constants are off by 4×/16×; the cofactor's arithmetic is generic and gives no π-specific saving; the finite data (correctly computed) is consistent with normality.
- **Not proved, and equivalent to the open problem:** the signed cancellation `S_N(h)=o(N)`, equivalently `Σ_{n≤N}e(h·16^{n-1}π)=o(N)`.

**Remaining lemma (unchanged, sharpest form):** `sup_{1≤|h|≤16^{m-1}}|S_N(h)|=O(N^θ)`, some `θ<1`, `m=⌊log₁₆N/3⌋` — equivalently `Σ_{n≤N}e(h·16^{n-1}π)=o(N)` for the authentic orbit.

**Cheapest next discriminator (Front 2):** the shrinking-window boundary count `#{a_p≤n<b_p : {16^{n-a_p}π}<T_n}=o(L_p)`, the weakest statement not implied by the exact arithmetic facts.

**π base-16 normality and RH remain OPEN. No proof claimed; no false victory.**
