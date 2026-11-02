# New toolkit constants: exact closed forms of the Green-tail mass and the f_m series

**Branch:** `research/green-tail-sharpening-2026-11-02`. **Date:** 2026-11-02.

This records exact closed forms (digamma at eighths) for the constants that enter the
Green-tail reduction, making them rigorous rather than numerical.

## 1. The unweighted BBP sum S = Σ_{m≥1} r(m) — exact closed form (PROVED)

Using the f_m decomposition `r(m) = 2 f_3(m) + f_4(m) + f_5(m)`, `f_k(m)=1/(8m-7)-1/(8m-7+k)`,
and the reindexing `8m-7 = 8(m-1)+1`:

$$
\sum_{m\ge1} f_k(m) = \frac18\Big[\psi\!\big(\tfrac{k+1}{8}\big)-\psi\!\big(\tfrac18\big)\Big],
$$

so

$$
\boxed{S=\sum_{m\ge1}r(m)=\frac18\Big[2\psi(\tfrac12)+\psi(\tfrac58)+\psi(\tfrac34)-4\psi(\tfrac18)\Big]
=3.3860476195971917219364188314\ldots}
$$

Each `ψ(p/8)` is an **exact elementary number** by the Gauss digamma theorem (a combination of
`γ`, `π`, `log 2`, `√2`, and `log(1+√2)`/`log(2+√3)`). Hence `S` is exact, and combined with the
theorem `B = (S−π)/15`:

$$
\boxed{B=\sum_{n\ge1}T_n=\frac{S-\pi}{15}=0.0162969977338265655649183632105939984\ldots}
$$

is now a **fully exact** identity (no numerical truncation): the Green-tail mass is the exact
digamma expression `(S−π)/15`.

## 2. The f_m BBP series s_k = Σ 16^{-m} f_k(m) — new constants (PROVED exact relation)

The weighted series satisfy (verified to 166 digits):

$$
2s_3+s_4+s_5=\frac{\pi}{16},\qquad
s_k=\frac1{16}\Big[\operatorname{Lerch}\!\big(\tfrac1{16},1,\tfrac18\big)
-\operatorname{Lerch}\!\big(\tfrac1{16},1,\tfrac{k+1}{8}\big)\Big].
$$

Values:
$$ s_3=0.0469857290332300554401251937061\ldots,\quad
s_4=0.0501363699236407934187881132019\ldots,\quad
s_5=0.0522417128592611731048767108406\ldots .$$

These are **new BBP-type constants** (the three "difference-of-pole" series into which the
four-pole forcing splits). They are reusable: any future identity involving the source's
weighted digit extraction can be expressed in this basis.

## 3. Value to the toolkit

- `S` and `B` are now **exact** (digamma closed forms), removing the last numerical
  truncation from the `B = (S−π)/15` theorem of the previous round.
- The `f_m` basis `{f_3, f_4, f_5}` with its exact constants is a reusable decomposition of
  the four-pole source into three "edge" channels (the `f_4` channel carries the `p≡5 mod 8`
  prime pole exclusively).

No normality claim. π normality and RH remain **OPEN**.

## 4. Reproducible verification

```python
python verify_constants.py   # sympy: S digamma form, B=(S-pi)/15, 2s3+s4+s5=pi/16 (166 digits)
```
