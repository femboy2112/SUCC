# abc ris-moment bound (#196): independent re-derivation + BBLT comparison

**Date:** 2026-10-20. **Re-checks** `observational_succ/abc_triple_moment.py` (ABC-TMB-01, PROVED LOCAL).
**Verdict:** the partial theorem is **CORRECT as stated**; the `t < 1/2` ceiling is a **limitation of the
Cauchy–Schwarz method, not a genuine growth threshold**; the bound is **rigorously valid but very loose**
and **strictly inferior to BBLT 2410.12234**, exactly as #196 already states. ABC remains **OPEN**.

## 1. The claim, re-derived independently

With `ris(n) = n / rad(n)` (the *radical index* / powerful-part; `ris(n)=1` iff `n` squarefree),

> **S_t(X) = Σ_{a+b=c≤X, (a,b)=1} ris(abc)^t ≤ M(t)·M(2t)·X²,  for every rational 0 ≤ t < 1/2.**

Re-derivation (independent of the module's prose):

1. For a primitive triple `(a,b,c)`, `(a,b)=1 ⟹ a,b,c` pairwise coprime ⟹ `rad(abc)=rad(a)rad(b)rad(c)`
   and `abc = a·b·c`, so `ris(abc) = ris(a)ris(b)ris(c)` (ris is multiplicative on coprimes). Hence
   `S_t(X) = Σ_{c≤X} ris(c)^t · I(c)`, `I(c) = Σ_{a+b=c,(a,b)=1} ris(a)^t ris(b)^t`.
2. Inner Cauchy–Schwarz: `I(c) ≤ (Σ_{a<c} ris(a)^{2t})^{1/2}(Σ_{a<c} ris(c−a)^{2t})^{1/2} ≤ Σ_{n<c} ris(n)^{2t}`.
3. Averaging input (ABC-CLK-02 / Euler product): `Σ_{n≤c} ris(n)^θ ≤ M(θ)·c` for `θ < 1`, where
   `M(θ) = ∏_p (1 + (p^θ−1)/(p−p^θ))`-type Euler product converges iff `θ < 1`. So `I(c) ≤ M(2t)·c`.
4. Outer: `S_t(X) ≤ M(2t) Σ_{c≤X} c·ris(c)^t ≤ M(2t)·X·Σ_{c≤X} ris(c)^t ≤ M(2t)·X·M(t)·X = M(t)M(2t)X²`.

**Binding constraint: `2t < 1`** (step 3 needs the inner exponent `2t < 1`). This is the exact ceiling of
*this* method; it is not a property of `S_t` itself.

## 2. Independent numerical confirmation

Recomputed the exact census (`S_t_enclosure`) and the certified constant (`S_t_constant_upper`):

- Anchor: `S_1(24)` enclosure `= 557`, matching the exact integer moment `557` (independent route). ✓
- `C_{2/5} = M(2/5)M(4/5) ≈ 171.376` (exact rational in the module).
- Domination at `t = 2/5`:

  | X | exact S_t(X) | C_t·X² | holds | ratio S_t/(C_t X²) |
  |---|------|------|------|------|
  | 32 | 579.7 | 175489 | ✓ | 0.0033 |
  | 64 | 2413.9 | 701956 | ✓ | 0.0034 |
  | 128 | 10803.4 | 2807825 | ✓ | 0.0038 |
  | 256 | 45412.8 | 11231300 | ✓ | 0.0040 |

- `S_t_constant_upper(1/2)` and `(3/5)` both correctly **raise** `ABCClockError`.

The bound holds at every census point but is ~**250–300× larger** than the actual `S_t(X)`: it is a valid
rigorous upper bound, far from tight. (A finite census is evidence, never a proof of the uniform bound —
the proof is the §1 argument.)

## 3. Is `t = 1/2` a method limit or a real threshold?

**A method limit.** Any Hölder split of the inner sum into exponents `(r, r')` with `1/r + 1/r' = 1`
needs both `rt < 1` and `r't < 1`; minimising `max(r, r')` gives `r = r' = 2` (Cauchy–Schwarz), forcing
`2t < 1`. A different arrangement (e.g. exploiting the additive constraint `a+b=c` with Fourier/divisor
cancellation, or a large-sieve input) could in principle reach larger `t`. At `t ≥ 1/2` the Euler factor
`1/(1 − p^{2t−1})` in `M(2t)` diverges, so the *constant* blows up — but that is this estimate's constant,
not a proof that `S_t(X)/X²` is unbounded. The regime `1/2 ≤ t < 1` is **OPEN to this method**;
the obstruction `ABC-TMB-03` (dyadic tower `(1, 2^k−1, 2^k)`, `ris ≥ c·2^k`) shows no *uniform pointwise*
bound exists, but the mass is `o(X²)`, consistent with an `X²` average bound persisting past `1/2`.

## 4. BBLT (arXiv 2410.12234) comparison — the honest ladder

Bernert–Browning–Lichtman–Teräväinen bound the **exceptional set** `{(a,b,c): c > rad(abc)^{3/5+ε}}` and,
in their strongest form, the count of abc triples up to `X` with large quality, with exponent `3/5+ε`.
This is a **different object** than `S_t(X)`:

- `S_t(X)` is a **second-moment average** of the powerful-part weight `ris = n/rad` over *all* primitive
  triples; it never isolates the exceptional (high-quality) triples.
- BBLT counts the **rare exceptional triples** with the sharpest known exponent, via large-sieve /
  determinant-method geometry (Browning) and multiplicative-function machinery (Lichtman–Teräväinen).

**#196 is strictly inferior and not directly comparable**: an `X²` average bound on `ris^t` does not imply
any exceptional-set count, and the elementary `X^{8/5}` baseline (ABC-CLK-03) is weaker than `X^{3/5+ε}`.
A reproducible proof-obligation ladder toward BBLT:

1. Replace the moment average by an **exceptional-set indicator** `1[c > rad^{1+δ}]` and bound its sum.
2. Supply a **large-sieve / dispersion** input (not available from `M(θ)` Euler products alone).
3. Import the **determinant-method** count for integer points on the relevant surfaces.
4. Only then compare exponents to `3/5+ε`.

Steps 2–3 are exactly the capabilities SUCC's moment method **does not** have. **A rigorous statement of
*why* the SUCC transfer cannot reach the BBLT exponent is itself the successful research result here**;
no academic-novelty or competitive-exponent claim is made. ABC stays OPEN.
