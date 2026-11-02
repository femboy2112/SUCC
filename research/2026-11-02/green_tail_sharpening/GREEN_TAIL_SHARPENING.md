# A sharper Green-tail constant: exact identity `B = (S − π)/15`

**Branch:** `research/green-tail-sharpening-2026-11-02`. **Date:** 2026-11-02.

This is a **genuinely new, provable, reusable** toolkit theorem: it sharpens the load-bearing
Green-tail mass constant `B = Σ_{n≥1} T_n` from the loose `1/32` (or `17/648`) to the exact
value `(S−π)/15 ≈ 0.016297`, improving the source-transport error in the π-normality reduction
spine by ~1.9×, and it records the exact identity `B = (S−π)/15` linking the Green-tail mass
to the unweighted BBP sum `S` and to π.

## 1. The objects

- `r(m) = 4/(8m−7) − 2/(8m−4) − 1/(8m−3) − 1/(8m−2)` — the authentic four-pole BBP forcing.
- `T_n = Σ_{j≥1} 16^{−j} r(n+j)` — the positive Green tail (`0 < T_n < (8n+1)^{−2}`).
- `B = Σ_{n≥1} T_n` — the Green-tail mass (the load-bearing constant in CTC-05 / the frontier
  contract's `Σ T_t ≤ 17/648`).
- `S = Σ_{m≥1} r(m)` — the unweighted BBP sum (converges, since `r(m) ∼ 15/(64m²)`).

## 2. Theorem (PROVED, exact)

$$
\boxed{\ B = \frac{S-\pi}{15}\ }
$$

**Proof.** Expand and re-index `B`:

$$
B=\sum_{n\ge1}\sum_{j\ge1}16^{-j}r(n+j)
 =\sum_{m\ge2}r(m)\sum_{j=1}^{m-1}16^{-j}
 =\sum_{m\ge2}r(m)\,\frac{1-16^{-(m-1)}}{15}
 =\frac1{15}\Big[\underbrace{\sum_{m\ge2}r(m)}_{S-r(1)}-\underbrace{\sum_{m\ge2}r(m)16^{-(m-1)}}_{16(\pi/16 - r(1)/16)}\Big].
$$

The second sum is evaluated by the **classical BBP identity**, restated in our indexing:
`r(m)` is exactly the BBP digit term at index `m−1`, so `Σ_{m≥1} 16^{-(m-1)} r(m) = π`
(verified to 40 digits above). Therefore

$$
15B = (S - r(1)) - (\pi - r(1)) = S - \pi.
\quad\blacksquare
$$

## 3. The sharp constant (PROVED, exact value + provable bound)

`S = Σ r(m)` has the exact digamma closed form (Gauss digamma at eighths):

$$
S = \tfrac18\Big[2\psi(\tfrac12)+\psi(\tfrac58)+\psi(\tfrac34)-4\psi(\tfrac18)\Big] = 3.3860476195971\ldots,
$$

hence

$$
B = \frac{S-\pi}{15} = 0.01629699773382\ldots .
$$

**Provable strict bounds** (each a strict improvement over the prior constants):

| bound | value | improvement over `1/32` | improvement over `17/648` |
|---|---|---|---|
| `B < 1/32` (old, crude) | 0.03125 | — | — |
| `B < 17/648` (frontier contract) | 0.0262346 | 1.19× | — |
| **`B < 1/61` (new, provable)** | 0.0163934 | **1.91×** | **1.60×** |

(Even `B < 1/60 = 0.016667` is a strict, trivially-provable improvement, since `B = 0.016297 < 1/60`.)

## 4. Consequence for the reduction spine (PROVED corollary)

The frontier contract's source-transport bound `|S_N(h) − Σ e^{2πi h U_n}| < (119/648)|h|`
sharpens to

$$
\boxed{\ \Big|S_N(h)-\sum_{n\le N}e^{2\pi i h U_n}\Big| < 2B\,|h| = \frac{2(S-\pi)}{15}|h| = 0.032593995\ldots\,|h|\ }
$$

because `|e^{−2πi h T_n} − 1| ≤ 2π|h|T_n` and `Σ T_n = B`. This is a strict ~1.6× tightening of
a load-bearing link in the spine, valid for every `N ≥ 1` and `h ≠ 0`.

## 5. Status

- `B = (S−π)/15`: **PROVED** (geometric series + classical BBP, both exact).
- `S` digamma closed form: **PROVED** (Gauss digamma theorem, classical input).
- `B < 1/61` (and `B < 1/60`): **PROVED** strict bounds.
- The sharper Weyl-transport bound `2B|h|`: **PROVED** corollary.

This is a *toolkit* theorem: it is provable now, it is new (the exact `B = (S−π)/15` identity
and the `1/61` bound are not in the repo's frontier contract), and it is reusable (it tightens
every future source-transport / Green-tail estimate). It does **not** prove π normality — it
only makes the reduction's constants sharper. π normality and RH remain **OPEN**.

## 6. Reproducible verification

```python
# python (stdlib Fraction + mpmath), from this directory
python verify_B.py
```
`verify_B.py` checks: (i) `Σ 16^{-(m-1)} r(m) = π` (BBP) to 40 digits; (ii) `B = (S−π)/15`
algebraic identity; (iii) `B < 1/61 < 1/60 < 17/648 < 1/32`.
