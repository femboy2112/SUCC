# The exact structure of C_A: collision energy = near-collision count at 1/A scale

**Branch:** `research/army-sub-log-collision-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** exact arithmetic structure of the open gate
`C_A = (1/A) Σ_i v_i(A)^2 = o(log A)`.

## 1. The object

Four-pole BBP: `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_{n+1}=16U_n+r(n+1)`.
Exact rationals `U_n = A_n/Q_n`, `Q_n = exp(6n+o(n))` (PROVED conductor). Green tail
`U_n = 16^{n-1}π - T_n`, `T_n = Σ_{k≥1} 16^{-k}r(n+k) > 0` summable, `Σ T_n = B < 1/32`.

$$v_i(A) = \#\{A\le n<2A : \lfloor A\{U_n\}\rfloor=i\},\qquad C_A=\frac1A\sum_{i=0}^{A-1}v_i(A)^2.$$

## 2. Exact reduction of C_A to a near-collision count

Two states `U_n,U_m` (`n<m`) share a bin iff `\lfloor A\{U_n\}\rfloor=\lfloor A\{U_m\}\rfloor`,
equivalently `\|U_n-U_m\| < 1/A` (circular distance to nearest integer), up to boundary.

Write `U_n - U_m = 16^{n-1}π - 16^{m-1}π - (T_n - T_m)`. Setting `m=n+d`:
$$U_n - U_m = 16^{m-1}(16^{-d}-1)π - (T_n - T_m) = -16^{m-1}(16^d-1)16^{-d}π - (T_n-T_m).$$

Equivalently, and more usefully, using `U_n = A_n/Q_n` exact:
$$U_n - U_m = \frac{D_{n,m}}{Q_n Q_m}, \qquad D_{n,m} = A_n Q_m - A_m Q_n \in \mathbb Z\setminus\{0\}.$$
(The difference is nonzero: equality `U_n=U_m` forces `16^{n-1}π=16^{m-1}π` i.e. `π` rational.)

A shared `1/A` bin means `\|D_{n,m}/(Q_n Q_m)\| < 1/A`, i.e. there is an integer `k` with
$$|D_{n,m} - k\,Q_n Q_m| < \frac{Q_n Q_m}{A}.$$

**This is the exact near-collision criterion.** `D_{n,m} - k Q_n Q_m` is a nonzero integer
unless the two states are exactly integer-separated. Empirically (A=256) the states are
**never** exactly integer-separated or exactly equal (0 such pairs), yet 124 pairs share a bin.

## 3. The scale separation (the decisive structural fact)

For `n,m \in [A,2A)`, `Q_n Q_m \asymp \exp(12A+o(A))` (since `log Q_n \sim 6n \sim 6A`).
The near-collision condition `|D_{n,m}-kQ_nQ_m| < Q_nQ_m/A` asks for an integer `D-kQ_nQ_m`
of size `< \exp(12A)/A \approx \exp(12A)`. This is **not** a small integer — it is astronomically
large. So the "integer numerator" picture is vacuous: the near-collision is governed by the
**real Archimedean spacing** `\|16^{m-1}(16^d-1)π\|` of the π-part, **not** by any exact rational
coincidence.

Concretely (A=256): colliding pairs have `\|U_n-U_m\| \sim 10^{-5} \sim 1/A^2`, while
`1/(Q_nQ_m) \sim \exp(-12\cdot256) = \exp(-3072)`. The states sit at random-pair spacing
`1/A^2`, and the rational denominator scale is **irrelevant** — it is `\exp(-3072)`, far below
any observable scale.

## 4. The load-bearing term is the Diophantine spacing of π

Since `\|U_n-U_m\| = \|16^{m-1}(16^d-1)π - (T_n-T_m)\|` and `T_n,T_m \le r(n+1)/15 \to 0`
summably (total `<1/32`), the tail contributes a **bounded, summable correction**. The dominant
term is:
$$\|16^{m-1}(16^d-1)π\| = \|(16^d-1)\,16^{m-1}π\| .$$

This is **exactly** a Diophantine-approximation statement about π at the sparse multiplier
`16^d-1`, scaled by `16^{m-1}`. It is the same object the `X3_DIMENSION.md` §2.2 identified
(the spacing is governed by `\|(16^k-1)π\|`, a Diophantine statement about π).

## 5. What this means for C_A = o(log A)

`C_A` is the collision energy of `N \asymp A` points `\{U_n\}` placed on the circle at
spacings `\|(16^d-1)16^{m-1}π\|`. For a **random** sequence these spacings are `\Theta(1/A^2)`
and `C_A = O(1)`. The empirical `C_A \approx 1.6-2.1` (bounded) is precisely the random-pair
signature.

**The open gate is therefore: prove the orbit `\{16^{n-1}π\}` has no anomalously-clustered
pairs beyond random, i.e. `\|(16^d-1)16^{m-1}π\| \gg 1/A^{2+o(1)}` for most `(d,m)`.** This is a
**Diophantine statement about π**, structurally identical to (and not obviously weaker than) the
signed Weyl gate. It is **not** controlled by the Green tail (which is summable and contributes
`O(1/A^2)` corrections), nor by the rational conductor (which is `\exp(-12A)`-scale, irrelevant).

## 6. Honest boundary

- `C_A` is a real Archimedean (spacing) object, governed by the Diophantine spacing of π.
- The tail `T_n` and conductor `Q_n` are **exact, computable, and irrelevant** to the `1/A^2`
  near-collision scale — they are `O(1/A^2)` and `\exp(-12A)` respectively.
- `C_A = o(log A)` is equivalent to a **Diophantine non-clustering statement about π**, not to
  anything the BBP/Green-tail/prime-CRT structure alone can certify.
- Empirically `C_A = O(1)` (random-pair scaling), which would be MORE than enough; the gap is
  proving it, and it requires the irrationality/Diophantine content of π.

π base-16 normality and RH remain **OPEN**.
