# Exact structural identities: residue-clock Gram matrix and Möbius source

**Date:** 2026-10-13. **Branch:** `research/dsv4-periodic-tail-enclosure-2026-10-13`. **RH PROVED: no.**
Notation: `r_n(k) = (k mod n)/n`, weight `w_k = 1/(k(k+1))`, inner product `<f,g> = sum_k f(k)g(k) w_k`, `L_s(f) = int_0^1 f(x) x^{s-1} dx`. All identities are exact; no zero location, Gamma, pole or Weil kernel is used. The ingredients are classical and cited; the assembly is the contribution.

## T1 — the target vector is exactly the harmonic logarithm

**Theorem.** `<1, r_n> = log(n)/n` for every `n >= 2`.

**Proof.** On cell `I_k = (1/(k+1), 1/k)` the constant function has `dx`-measure `1/k - 1/(k+1) = w_k`, so `L_1(f) = int_0^1 f dx = <f, 1> = <1, f>`. The cell-Mellin identity (classical, = repo ZCR-02) gives `L_s(r_n) = (zeta(s)/s)(1/n - n^{-s})` for `Re(s) > 1`, analytically continued to `Re(s) > 0` with a removable singularity at `s = 1`. As `s -> 1`: `zeta(s)/s = 1/(s-1) + (gamma-1) + O(s-1)`, while `1/n - n^{-s} = (log n/n)(s-1) + O((s-1)^2)`. Hence `L_s(r_n) -> log(n)/n`. Since `L_1(r_n) = <1, r_n>`, done. (Verified to `~1/N` truncation at `N = 2e5`.)

## T2 — the optimal single-clock approximation is closed-form

**Theorem.** `<r_2, r_2> = log 2/4`, `<1, r_2> = log 2/2`, so the optimal one-clock error is `E_2* = 1 - log 2`, attained at `a_2 = 2`.

**Proof.** `r_2(k) = 1/2` on odd `k`, `0` on even `k`. So `<r_2,r_2> = (1/4) sum_{odd k} 1/(k(k+1)) = (1/4) sum_{j>=0} 1/((2j+1)(2j+2)) = (log 2)/4` (the alternating-harmonic tail `1/2 - 1/3 + 1/4 - ... = 1 - log 2`, so the odd part is `log 2`). And `<1,r_2> = log 2/2` by T1. The least-squares optimum of `||1 - a r_2||^2` is `a* = <1,r_2>/<r_2,r_2> = 2`, with residual `E_2* = <1,1> - <1,r_2>^2/<r_2,r_2> = 1 - (log2/2)^2/(log2/4) = 1 - log 2`. (This is the Schur complement of the `2x2` Gram block `{1, r_2}`.) Verified to 14 digits.

## T3 — Möbius cancellation: the formal source equals the constant 1 in Mellin data

**Theorem.** For `Re(s) > 1`, `sum_{n>=1} mu(n) L_s(r_n) = -1/s = -L_s(1)`. Equivalently the formal combination `-sum_{n>=1} mu(n) r_n` has the *same* Mellin transform as the constant `1`.

**Proof.** `L_s(r_n) = (zeta(s)/s)(1/n - n^{-s})`, so
`sum_n mu(n) L_s(r_n) = (zeta(s)/s) [ sum_n mu(n)/n - sum_n mu(n) n^{-s} ]`.
Möbius inversion gives `sum_{n>=1} mu(n) n^{-s} = 1/zeta(s)` for `Re(s) > 1` (absolute convergence), and `sum_{n>=1} mu(n)/n = 0` as an Abel/Dirichlet sum — this is **equivalent to the Prime Number Theorem** (Hadamard–de la Vallée Poussin 1896; `sum_{n<=x} mu(n)/n -> 0` iff `M(x) = o(x)`). Therefore the bracket is `-1/zeta(s)` and the whole thing is `-1/s = -L_s(1)`. The PNT dependence is intrinsic, not a defect: it is exactly the cancellation that makes the Báez-Duarte source family `-mu(n)/n` reproduce the constant term. (Verified: `sum_{n<=N} mu(n)(1/n - n^{-s}) -> -1/zeta(s)` to `~1/N` for `s = 2,3,4`.)

**Boundary (stated flat).** This is the *Mellin-domain* shadow of the Nyman–Beurling/Báez-Duarte density statement — the **easy, formal** direction. It says the source combination `-mu(n) r_n` reproduces the target's Mellin data on `Re(s) > 1`; it does **not** say the sum converges in `L^2(w)`. Promoting the formal identity to genuine `L^2` density is precisely RH (Burnol/BBLS/Báez-Duarte). So T3 is a structural lemma, not a step toward a zero, and it cannot be silently upgraded.

## T4 — the Gram matrix lives in the cyclotomic log space

**Theorem.** For `L = lcm(m,n)`, `<r_m, r_n> = (1/(mn)) sum_{r=1}^{L-1} (r mod m)(r mod n) S_r(L)`, where `S_r(L) = sum_{k = r mod L} 1/(k(k+1)) = (psi((r+1)/L) - psi(r/L))/L` (with `r=0` read as `k0 = L`). By Gauss's digamma theorem, `psi(r/L)` is an explicit element of the `Q`-span of `{log(2 sin(pi k/L)) : k}` plus `pi cot(pi r/L)`. Hence **every** Gram entry — and therefore every optimal error `E_N* = 1 - b^T G^{-1} b` (Schur complement) — is an explicit cyclotomic-log number.

**Proof.** `1/(k(k+1)) = 1/k - 1/(k+1)` telescopes, and summing over a residue class gives the digamma difference; this is the standard digamma-telescoping identity (verified: `sum_r S_r(L) = 1` exactly for `L in {3,4,5,6,12}`). Gauss's digamma theorem (classical, e.g. DLMF 5.4) supplies the closed form. ∎

**Why this is the interesting part.** The Gram matrix is not some opaque transcendental object. Gauss's digamma theorem splits it cleanly into two arithmetic pieces: `log(2 sin(pi k/L))` — the logarithms of **cyclotomic units** (the *regulator* side of Dirichlet's class-number formula) — and `pi cot(pi r/L)` — the *`L(1,chi)`* side of the same class-number formula (for odd Dirichlet characters, `L(1,chi) = -(pi/(m sqrt{d})) sum_r chi(r) cot(pi r/m)`). So the residue-clock Gram matrix is concretely a **cyclotomic-regulator plus class-number** matrix, and `E_N* = det H_{N+1} / det G_N` is a ratio of such determinants. These are the same arithmetic objects that appear in the completed Weil form and in Suzuki's de Branges picture.

## Status labels

- T1, T2: **PROVED LOCAL** (elementary exact; T1 = repo ZCR-02, re-derived; T2's closed form `1 - log 2` was stated in the zero-centered doc but not as the *Schur-complement optimum* with the exact `b_2, G_22`).
- T3: **PROVED LOCAL** assembly of CLASSICAL facts (`1/zeta(s) = sum mu(n) n^{-s}`, `sum mu(n)/n = 0`); the *content* is the clean statement, not a new priority theorem.
- T4: **CLASSICAL** (Gauss digamma theorem) applied; the observation that the Gram matrix is cyclotomic-log is the contribution.

No priority claim against Nyman–Beurling, Báez-Duarte, Burnol, BBLS, BCF, Gauss, or DLMF. The new artifact is the *exact, verified* structural identification of the residue-clock Gram matrix and its Möbius cancellation.

Reproduce: `python3 -m unittest tests.test_gram_mobius -v`.
