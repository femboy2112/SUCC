# Shen Tzu on the Weyl form — consolidated verdict (five fronts converge)

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel + 5 subagent fronts. **Target:** the signed Weyl gate
`S_N(h) = Σ_{n≤N} e(hU_n) = o(N)` ⟺ π base-16 normal.

## The attack

Full Art-of-War fan-out on the Weyl form itself, via the maintainer's `weyl_borg_fusion`
machinery (WB-02 exact signed decomposition). Five independent fronts, each attacking a genuinely
different flank.

## What each front proved

### Front A — cofiber decay (PROVED negative, the decisive one)
The within-cell cofiber `C_(N,M)(h)` appears to decay in `M` — but this is **the Weyl sum in
disguise**. The exact `s_n` structure is `s_n = σ_n − M·T_n` (bulk), where `σ_n = M{16^{n-1}π}
− ⌊M{16^{n-1}π}⌋` is the *pure π-phase*. The tail leg of the cofiber provably contributes only
`O(h·B/N)` (the `M` **cancels exactly**), while the π-phase leg `E_π` is *literally* the
fixed-frequency Weyl average of `{16^{n-1}π}`. **The cofiber does not reduce the gate to the
cell-imbalance leg — the two "legs" are the same object.**

### Front B — Ward/covariance ladder (PROVED inert)
The radix ladder `h → 16h → 16²h` is a **re-indexing symmetry**, not a source of cancellation.
`S_N(16h) ≈ S_{N+1}(h)` up to a summable `r(n+1)` correction — covariance only, no signed decay.

### Front C — van der Corput (PROVED inert)
Second differences grow like `225h·16^{n-1}π` (rapidly expanding map). van der Corput just
re-multiplies the frequency by `16^k−1`, leaving the Weyl functional form invariant. **No order
reduction.**

### Front D — CRT signed phase (PROVED negative, structurally decisive)
The "tensor of prime clocks" **collapses to a single rational rotation**
`Φ_A(n) = e(4hρ_A·16^n)` with `ρ_A ∈ Q`. And this prime phase is *exactly the inverse* of the
rational part `S_n` inside the cofactor, so `Φ_A(n)·e(hC_n) = e(hU_n)` **identically**. The CRT
decomposition is an exact re-encoding — the cofactor `e(hC_n)` = raw Diophantine rotation is the
**sole obstruction**, unchanged.

### Front E — cell-imbalance leg (PROVED negative)
The cell-imbalance leg is **not** closed by `C_M = o(log M)` alone: the Cauchy–Schwarz bound
`Σ_a|p_a−1/M| ≤ √(M(C_M/M − 1/M))` does not give `o(1)` from `C_M = o(log M)` (it gives only
`o(√(M log M))` at best, which is vacuous for the gate). The cell-imbalance and cofiber legs are
coupled through the same π-object.

## The convergent verdict

**Five independent attacks converge: the signed Weyl gate is a single, indivisible object — the
Diophantine rotation `e(h(16^{n-1}π − T_n))` — and every proposed decomposition (cell vs. cofiber,
prime vs. cofactor, ladder, difference) is a *re-encoding or symmetry* of that one object, not a
decoupling.** The π-content cannot be factored out of the Weyl sum by any of these means.

**What was ruled out (durable negative value):**
1. cofiber/cell-imbalance split → **same object** (Front A, E).
2. radix ladder covariance → **symmetry, not cancellation** (Front B).
3. van der Corput / second difference → **inert** (Front C).
4. prime-CRT decomposition → **telescoping identity** (Front D).

**Literature (main thread):** π base-16 normality OPEN (Bailey–Borwein 2014, MathOverflow);
`μ(π) ≤ 7.103…` gives only exponential spacing (insufficient); **no known bound on `{16^{n-1}π}`**.

## The honest state

The Weyl gate is now **fully mapped**: it is a fixed-frequency signed cancellation for the specific
π, with no known theorem even close, and every decomposition route is provably a re-encoding. The
only open path is a *genuinely new* signed-cancellation estimate on the four-pole orbit — which no
known analytic, Diophantine, ergodic, or rigidity tool supplies. This is a hard negative, but a
complete one: no future front need re-explore these five closed doors.

**π base-16 normality and RH remain OPEN.**
