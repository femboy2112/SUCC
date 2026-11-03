# The exact lag-L autocorrelation structure of K_j

**Branch:** `research/sherman-gs05-signed-cascade-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (subagent, Wave 2a). **Scope:** derive the exact lag-L autocorrelation
structure of the GS-05 signed cross-block reinforcement `K_j`, its Diophantine reduction, and an
explicit controlled tail-error bound. Companion: `verify_lagL_autocorrelation.py` (all identities
machine-verified; see the claim ledger below for which are PROVED vs machine-verified).

**Status line:** π base-16 normality and RH remain **OPEN**. Nothing here closes them.

---

## 0. Objects (all previously established, reproduced here for self-containment)

- Orbit `U_0=0`, `U_{n+1}=16U_n+r(n+1)`, `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`.
- Green tail: `U_n = 16^{n-1}π − T_n`, with the **convergent tail series**

  $$
  T_n = \sum_{j\ge 1} 16^{-j}\,r(n+j), \qquad 0 < T_n = O(n^{-2}).
  $$

  (Derivation: `U_n=\sum_{k=1}^n 16^{n-k}r(k)=16^{n-1}\sum_{k=1}^n 16^{-(k-1)}r(k)`, and
  `\sum_{k\ge1}16^{-(k-1)}r(k)=π` is exactly the BBP π formula at `m=k-1`; hence the residual is
  `T_n=16^{n-1}\sum_{k>n}16^{-(k-1)}r(k)=\sum_{j\ge1}16^{-j}r(n+j)`.)
- Cross-block vectors `A=\sum_{n=a+1}^{a+L}e(hU_n)`, `B=\sum_{m=a+1}^{a+L}e(hU_{m+L})`, and
  `K_j=\operatorname{Re}\sum_{\text{pairs}}A\overline B
  =\sum_{n,m=a+1}^{a+L}\cos\big(2πh(U_n-U_{m+L})\big)`
  (the pair sum is the ordered double sum; `K_j` is then aggregated over disjoint blocks
  `a=0,2L,4L,\dots`, linearly — see §5).

---

## 1. The exact lag-L decomposition (PROVED)

**Claim (GS05-LAG, PROVED — exact, no approximation).** With `k=m+L-n` (so that
`k\in\{1,\dots,2L-1\}` as `n,m` run over `\{a+1,\dots,a+L\}`),

$$
\boxed{\,U_{m+L}-U_n \;=\; 16^{\,n-1}(16^{k}-1)\,\pi \;-\;(T_{m+L}-T_n)\,}
$$

and therefore

$$
\boxed{\,K_j=\sum_{n,m=a+1}^{a+L}\cos\!\Big(2πh\Big[16^{\,n-1}(16^{k}-1)\pi-(T_{m+L}-T_n)\Big]\Big).\,}
$$

*Proof.* Substitute `U_\ell=16^{\ell-1}π-T_\ell` into `U_{m+L}-U_n`:
`16^{m+L-1}π-16^{n-1}π-(T_{m+L}-T_n)=16^{n-1}(16^{m+L-n}-1)π-(T_{m+L}-T_n)`, with
`k=m+L-n`. ∎

This is the same content as the telescoping identity GS05-TEL (which reads
`(16^L-1)U_n+F(n,L)=U_{n+L}-U_n` for `m=n`, the diagonal `k=L`), now carried to the **full
off-diagonal pair** `(n,m)`, i.e. the entire autocorrelation, not just the diagonal lag.

---

## 2. The exact role of the tail vs the π-term (PROVED decomposition)

The argument of each cosine splits **additively and exactly** into

$$
2πh\,(U_n-U_{m+L}) = 2πh\cdot 16^{\,n-1}(16^k-1)\pi \;-\; 2πh\,(T_{m+L}-T_n),
$$

with the two parts playing categorically different roles:

| part | size | nature | role in `K_j` |
|---|---|---|---|
| `16^{n-1}(16^k-1)π` | the orbit `{16^{n-1}π}` under the **sparse multiplier** `16^k-1`, `k=1..2L-1` | arithmetic / Diophantine (oscillatory in `n`) | **dominant**: sets the phase via `\|\cdot\|`; the *only* source of decorrelation |
| `T_{m+L}-T_n` | `O(1/n^2)`, **summable** (`\sum_n T_n = B = 0.0163\ldots < 1/61`) | smooth, deterministic, **non-oscillatory** (monotone in the index) | **sub-leading**: a Lipschitz phase perturbation `2πh(T_{m+L}-T_n)=O(h/n^2)` |

Precisely, the tail enters the cosine **only through a bounded phase shift**, not through the
multiplier. Writing `θ=16^{n-1}(16^k-1)π` and `τ=T_{m+L}-T_n`:

$$
\cos\!\big(2πh\,(θ-τ)\big)
=\cos(2πhθ)\cos(2πhτ)+\sin(2πhθ)\sin(2πhτ),
$$

so with `|\cos(2πhθ-2πhτ)-\cos(2πhθ)|\le 2π|h|\,|τ|` (Lipschitz constant of cos is 1):

$$
\Big|K_j-K_j^{(0)}\Big|\;\le\;2π|h|\sum_{n,m=a+1}^{a+L}|T_{m+L}-T_n|,
\qquad
K_j^{(0)}:=\sum_{n,m}\cos\!\big(2πh\,16^{n-1}(16^k-1)π\big).
$$

The tail's *summability* (`\sum T_n<\infty`) is a **coarser** fact than what is needed here: the
pairwise control needs the **pointwise** bound `T_n\le C/n^2`, which is strictly stronger (and is
what yields the `O(L^2/a^2)` error in §3).

---

## 3. The Diophantine reduction and the explicit tail-error bound (PROVED)

**Claim (GS05-DIO, PROVED).** The leading term reduces **exactly** to a distance-to-integer
(`\|\cdot\|`) sum over the orbit `{16^{n-1}π}`:

$$
K_j^{(0)}
=\sum_{n,m=a+1}^{a+L}\cos\!\big(2π\,\|\,h\,(16^k-1)\,16^{n-1}π\,\|\big),
\qquad k=m+L-n.
$$

*Proof.* `\cos(2π x)=\cos(2π\{x\})=\cos(2π\min(\{x\},1-\{x\}))=\cos(2π\|x\|)` for real `x`, applied
to `x=h(16^k-1)16^{n-1}π`. ∎ (Machine-verified exactly: `K_0 = K_0^{\text{dio}}` to `0` in mpmath,
see §6.)

**Claim (GS05-TAIL, PROVED — explicit controlled error).** Using the certified two-sided bound
`T_n\le 1/(64n^2)` (Green-tail sharpening round), and `n,m+L\ge a+1`:

$$
\sum_{n,m=a+1}^{a+L}|T_{m+L}-T_n|
\;\le\;\sum_{n,m}\big(T_{m+L}+T_n\big)
\;\le\;\frac{L^2}{32\,(a+1)^2},
$$

hence

$$
\boxed{\,\Big|K_j-K_j^{(0)}\Big|\;\le\;\frac{\pi|h|\,L^2}{16\,(a+1)^2}\,.}
$$

**Interpretation.** `K_j` is `O(L^2)` in scale (L² cosine terms). The tail error is
`O(|h|L^2/a^2)`, so the tail is **negligible relative to the leading term precisely when**
`a^2\gg|h|`, i.e. once the block start `a` exceeds `\sqrt{|h|}`. In the cascade `L=2^j` with
disjoint blocks `a=0,2L,4L,\dots`, the *positive*-`a` blocks are automatically in this regime; only
the very first block (`a=0`, where `T_1\approx0.0083` is `O(1)`) carries a non-negligible tail
mass, and it is a single fixed `O(|h|L^2)`-bounded term that does not affect the `j\to\infty`
divergence question.

---

## 4. What is therefore PROVED about the pair correlation (summary)

The full statement we can now assert *unconditionally*:

> `K_j` equals the **lag-L pair correlation of the orbit `{16^{n-1}π}` at the multipliers
> `16^k-1` (`k=1,\dots,2L-1`)**, up to an explicit error
> `|K_j-K_j^{(0)}|\le \pi|h|L^2/(16(a+1)^2)`, where the leading term is **exactly**
> `K_j^{(0)}=\sum_{n,m}\cos(2π\|h(16^k-1)16^{n-1}π\|)`.

Consequences for the GS-10 gate `D_J(h)\to\infty`:

- The signed anti-correlation requirement `K_j\le(1/2-\delta_h)E_j` is now, **exactly**, a
  statement that the Diophantine orbit `\{\|h(16^k-1)16^{n-1}π\|\}` has its `\cos(2π\,\cdot\,)`
  values summing below threshold — i.e. that the rotation by the **sparse, 15-divisible
  multipliers** `16^k-1=15(16^{k-1}+\cdots+1)` is **pair-wise decorrelated** at the block scale.
- The tail `T_n` contributes **only** the bounded `O(|h|L^2/a^2)` error; it cannot be the source of
  anti-correlation (it is smooth and non-oscillatory). **All** of the signed structure lives in
  `\{16^{n-1}π\}`.

**This is a reduction, not a proof:** we have *located* `K_j` exactly on the Diophantine orbit and
*quantified* the tail; proving `K_j\le(1/2-\delta_h)E_j` still requires a genuine Diophantine
decorrelation estimate for `\|h(16^k-1)16^{n-1}π\|` (equivalently the Weyl sum
`\sum e(h(16^k-1)16^{n-1}π)`), which is the same summit (RL) that the reduction spine already
located. **π normality and RH remain OPEN.**

---

## 5. Aggregation over blocks (PROVED, linearity)

`K_j` is defined as the aggregate over disjoint blocks `a\in\{0,2L,4L,\dots\}`. Since both the
leading term and the tail term are linear in the block, the aggregate decomposition is the block-sum
of the above, and the aggregate error bound is the block-sum of `\pi|h|L^2/(16(a+1)^2)`, which over
`a=2L,4L,\dots` is a convergent geometric-like tail `O(|h|L^2/a_0^2)`.

---

## 6. Claim ledger

| id | statement | status |
|---|---|---|
| GS05-TEL | `(16^L-1)U_n+F(n,L)=U_{n+L}-U_n` | **PROVED** (exact; diagonal of GS05-LAG) |
| GS05-LAG | `U_{m+L}-U_n=16^{n-1}(16^k-1)π-(T_{m+L}-T_n)`, `k=m+L-n` | **PROVED** (exact substitution) |
| GS05-DIO | `K_j^{(0)}=\sum\cos(2π\|h(16^k-1)16^{n-1}π\|)` | **PROVED** (cos mod-1 identity) |
| GS05-TAIL | `\|K_j-K_j^{(0)}\|\le π\|h\|L^2/(16(a+1)^2)` | **PROVED** (Lipschitz + `T_n\le1/(64n^2)`) |
| Tail series `T_n=\sum_{j\ge1}16^{-j}r(n+j)=16^{n-1}π-U_n` | **PROVED** (BBP residual) + **machine-verified** to `10^{-248}` |
| Lag decomposition (V2) | as GS05-LAG | **machine-verified** to `10^{-1095}` |
| GS-10 gate `D_J(h)\to\infty` | requires `K_j\le(1/2-\delta_h)E_j` on growing scales | **OPEN** (reduced to a Diophantine decorrelation estimate; = summit RL) |
| π base-16 normal / RH | — | **OPEN** (unchanged) |

---

## 7. Source receipt

- Definitions and GS05-TEL: `research/2026-11-02/sherman_gs05/GS05_TELESCOPING.md` (main thread,
  this branch).
- Green-tail sharpening (`T_n\le1/(64n^2)`, `B<1/61`): `research/green-tail-sharpening-2026-11-02`
  branch (per MEMORY.md 2026-11-02).
- Reduction spine (RL = unique summit): `research/pi-normality-framework-spine-2026-11-02`.
- Verification: `verify_lagL_autocorrelation.py` (this directory), all four verifications pass.

---

## 8. Cheapest next step

Prove (or computationally probe) the **pair-decorrelation** of `\{\|h(16^k-1)16^{n-1}π\|\}` for
`k=1..2L-1`: specifically, whether `\sum_{k}\cos(2π\|h(16^k-1)16^{n-1}π\|)` (the `k`-sum at fixed
`n`, which is the inner sum of `K_j^{(0)}`) exhibits signed cancellation. This is a purely
Diophantine, tail-free question now that GS05-TAIL has quarantined the tail.
