# Restricted denominators — transference, the 2-adic tilt, and what the π-line lacks (RDT)

**Baseline:** branch `research/frontier-rungs-restricted-exponent-2026-11-12`, parent
`9b4b71b2`, descendant of Main XXIV `071ce1e0`. **π base-16 normality, (CH), L2 for π and every
source-selected signed estimate remain OPEN.** Nothing in this file is a statement about digit
statistics beyond run lengths, and no statement here is claimed to be new: the literature on
restricted denominators (Rivoal 2007, below) was found only after RDT-01…05 were derived, and no
systematic search for RDT-05 was made.

This file answers the "next verdict-changing probe" of
[NEXT](../../2026-11-11/innovation_arithmetic_decoupling/NEXT.md): *what does it take to prove
`‖b^m ξ‖ ≥ b^(-vm)` at restricted denominators with `v` below the unrestricted `μ - 1`, and do the
natural constructions for `log 2` and `π` supply it?*

Status labels: `PROVED LOCAL` (complete proof here; same-model authorship, **not audited at the
time of writing**, not external review, not Lean), `CLASSICAL IMPORT` (cited theorem; where it was
read is stated), `COMPUTED FROM IMPORT` (numerical evaluation of an imported closed formula),
`OBSERVED` (exact finite computation, no asymptotic authority), `CONDITIONAL`, `OPEN`.
Code: [`rde_core.py`](rde_core.py), tests [`test_rde.py`](test_rde.py) (24 tests, about 2 s),
exploration record [`RESULTS_rde.json`](RESULTS_rde.json).

## 0. Notation

`b ≥ 2` an integer base, `S` the set of primes dividing `b`. For a nonzero rational `x`,
`(x)_S = ∏_(p∈S) p^(v_p(x))` is its **S-part** (a positive unit of `Z[1/b]`), and `|x|/(x)_S` its
**S-free part**. `‖t‖` is the distance to the nearest integer. For real `ξ`,

```text
v_b(ξ) = limsup_m  -log ‖b^m ξ‖ / (m log b)          (so v_16 ≤ v_2, and v_b ≤ μ(ξ) - 1).
```

Rivoal's exponent is `λ = v + 1` (he bounds `|ξ - u/b^m|`). A *form* for `ξ` is a triple
`(A, B, I)` with `A, B ∈ Q`, `A ≠ 0`, `I = Aξ - B`.

---

## RDT-01 — the restricted transference lemma (PROVED LOCAL)

**Lemma.** Let `ξ` be real, `(A, B, I)` a form, `g ≥ 1` and `m ≥ 0` integers. Let `E > 0` be a
rational and `u` a positive unit of `Z[1/b]` such that

```text
H := E·|A| / u  ∈ Z        and        g·b^m·E·B / u  ∈ Z.                                   (1.1)
```

Put `Q := E·|I| / u`. Then for every integer `p`:

```text
(i)   if  p ≠ g b^m B / A :      | g b^m ξ - p |  ≥  (1 - g b^m Q) / H ;
(ii)  if  p = g b^m B / A :      | g b^m ξ - p |  =  g b^m Q / H .
```

Consequently `‖g b^m ξ‖ ≥ min(g b^m Q, 1 - g b^m Q)/H`, and `‖g b^m ξ‖ ≥ (1 - g b^m Q)/H` whenever
`g b^m B/A` is not an integer. (The statement is empty unless `g b^m Q < 1`.)

*Proof.* `A(g b^m ξ - p) = g b^m I + (g b^m B - A p)`. Multiplying by `E/u`,
`(EA/u)(g b^m ξ - p) = g b^m (EI/u) + Δ` with `Δ := g b^m E B/u - (E A/u) p ∈ Z` by (1.1), and
`|EA/u| = H`, `|EI/u| = Q`. If `Δ ≠ 0` then `|Δ| ≥ 1` and `H|g b^m ξ - p| ≥ 1 - g b^m Q`, which is
(i); `Δ = 0` iff `p = g b^m B/A`, and then `H|g b^m ξ - p| = g b^m Q`. ∎

**The admissible unit.** If `E·A, E·B ∈ Z[1/b]` (e.g. `E` the least common multiple of the S-free
denominators of `A` and `B`, possibly divided by a common factor of the S-free numerators), the
largest admissible unit is

```text
u_m = ∏_(p∈S) p^( min( v_p(EA), v_p(gEB) + m·v_p(b) ) ),                                    (1.2)
```

and `u_m = (EA)_S` as soon as `m ≥ m_0 := max_p ⌈(v_p(EA) - v_p(gEB))/v_p(b)⌉`. Then `H` is the
**S-free part of `EA`**: the lemma sees the height of the approximant *with the primes of the base
removed*, and powers of `b` in the denominator of `B` cost nothing.

No non-vanishing hypothesis is needed: case (ii) is an exact evaluation. In applications it is
handled either by a lower bound for `|I|` (RDT-05) or by a second form (Rivoal's device).

*Checks.* `test_random_forms_never_violate_the_lemma` (600 random forms, five constants, five
bases, multipliers `g ∈ {1, 3, 15}`; `> 1500` instances with a non-empty bound, none violated);
mutation `test_mutation_overclaimed_unit_is_rejected` (replacing `u_m` by `b·u_m` is refuted by
`ξ_6` below at `m = 4`, where the lemma is sharp to 1 %).

## RDT-02 — what the lemma can and cannot gain (PROVED LOCAL)

Fix a form and `E` with `EA, EB ∈ Z[1/b]`, `g = 1`.

**(a) Invariance.** Replacing `(A, B, I)` by `(wA, wB, wI)` with `w` a unit of `Z[1/b]` changes
neither `H` nor `g b^m Q` in (1.2). (The S-parts of `EA` and `EB` are both multiplied by `w`.)

**(b) The gain is the S-adic imbalance.** The classical argument for an *arbitrary* denominator
clears denominators to the integer form `(λEA)ξ - λEB`, `λ = ∏_p p^(-min(v_p(EA), v_p(EB)))`, of
height `q_0 = λE|A|` and error `e_0 = λE|I|`. For `m ≥ m_0`,

```text
H = q_0 / G,     Q = e_0 / G,      G := ∏_(p∈S) p^( (v_p(A) - v_p(B))^+ )  ≥ 1.              (2.1)
```

So a restricted bound improves on the unrestricted one from the same form **iff `A` is more
divisible than `B` at a prime of the base**, and by exactly that factor in both the height and
the error. If `v_p(A) ≤ v_p(B)` for all `p ∈ S`, the two coincide for every `m`.
(`test_gain_is_exactly_the_S_adic_imbalance`.)

**(c) No rescue.** For every `m ≥ 0`: `b^m Q_m ≥ E|I| / (EB)_S`, where `Q_m = E|I|/u_m`. Hence a
form is silent at every `m` unless `E|I| < (EB)_S`. For a prime-power base, normalise by (a) so
that `v_p(EB) = 0`; then the condition is `E|I| < 1`, i.e. *the gcd-normalised integer form must
already have error below 1*. Asymptotically: **a family of forms that does not prove
irrationality by the classical criterion (integer-normalised errors `→ 0`) proves nothing at
restricted denominators either**, however large its imbalance `G`.

*Proof.* By (1.2), `u_m ≤ ∏_p p^(v_p(EB) + m v_p(b)) = b^m (EB)_S`. ∎
(`test_no_rescue_inequality`.) This corrects the provisional criterion "`α + σ - δ > 0`" of the
round brief, which omitted the constraint `m ≥ m_0`; the correct pair of conditions is (2.2).

**(d) Asymptotic form.** Let `(A_n, B_n, I_n)` be forms with `E_n`, and units `u_n` admissible for
all `m ≥ m_0(n)`. Suppose, as `n → ∞`,

```text
limsup (1/n) log(E_n|I_n|/u_n) ≤ -θ < 0,     limsup (1/n) log(E_n|A_n|/u_n) ≤ χ,
limsup m_0(n) log b / n < θ,                 liminf (1/n) log|I_n| ≥ -α > -∞,                (2.2)
limsup (1/n) log|A_n| ≤ β.
```

Then `v_b(ξ) ≤ max( χ/θ , (α + β - θ)/θ )`. In all applications below `E_n ≥ 1` grows like
`e^(δn)`, `u_n = e^(γn)`, `θ = α + γ - δ`, `χ = β + δ - γ`, and the two terms coincide:

```text
v_b(ξ)  ≤  (β + δ - γ) / (α - δ + γ)     provided   α > δ   (the classical criterion).        (2.3)
```

*Proof.* Fix small `ε > 0` and, for large `m`, let `n = ⌈m log b/(θ - ε)⌉ + n_1` with `n_1` so
large that `b^m E_n|I_n|/u_n ≤ 1/2`; then `m ≥ m_0(n)` for large `m` by the third condition. In
case (i) of RDT-01, `‖b^m ξ‖ ≥ 1/(2H_n) ≥ e^(-(χ+ε)n)`. In case (ii),
`‖b^m ξ‖ = b^m|I_n|/|A_n| ≥ e^((n - n_1 - 1)(θ-ε) - (α+β+2ε)n)`. Divide by `m log b ≥ (n - n_1 - 1)(θ - ε)`
and let `ε → 0`. ∎

**Example with a provable gain (`μ = ∞`, `v_2 < 1`).** Let `ξ_6 = Σ_(k≥1) 6^(-k!)`. Then
`μ(ξ_6) = ∞` (Liouville), the unrestricted lemma applied to the partial sums gives nothing, and

```text
v_2(ξ_6)  ≤  log 3 / log 6  =  0.6131… < 1.
```

*Proof.* `A_k = 6^(k!)`, `B_k = Σ_(j≤k) 6^(k!-j!) ≡ 1 (mod 6)`,
`6^(k!-(k+1)!) < I_k < 2·6^(k!-(k+1)!)`. With `b = 2`, `E = 1`: `v_2(A_k) = k!`, `v_2(B_k) = 0`,
so for `m ≥ k!`: `u = 2^(k!)`, `H = 3^(k!)`, and `2^m B_k/A_k = 2^(m-k!) B_k/3^(k!)` is not an
integer. RDT-01 gives `‖2^m ξ_6‖ ≥ 1/(2·3^(k!))` for
`k! ≤ m ≤ M_k := ⌊(k+1)! log_2 6 - k! log_2 3 - 2⌋`. Every `m ≥ 2` lies in such a window with
`m > M_(k-1)`, whence `3^(k!) ≤ 2^((log 3/log 6 + o(1)) m)`. ∎ (`LiouvilleExample`.)
Together with Shallit's number (`μ = 2`, `v_16 = 1`; ZSC-01, Remark 2) this shows that `μ - 1` and
the restricted exponent are independent in both directions.

**Example with no possible gain.** For Shallit's `K = Σ 16^(-2^k)`, `v_16(K) = 1 = μ(K) - 1`: no
family of forms can give a restricted exponent below the unrestricted one.

## RDT-03 — the continued-fraction dictionary (PROVED LOCAL; one CLASSICAL IMPORT for the sharp constant)

Conventions of [CARRY_FLUX](../../2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md) §0:
`y_n = 16^n ξ`, `{y_n} = 0.d_n d_(n+1)…`; a *run of length `L` at `n`* is
`d_n = … = d_(n+L-1)`.

**(a) Runs are restricted approximations, with exact constants.** For real `ξ`, `n ≥ 0`, `L ≥ 1`:

```text
run of length L at n, common digit j   ⟹   ‖15·16^n ξ‖ ≤ max(j, 15-j)·16^(-L) ≤ 15·16^(-L);
‖15·16^n ξ‖ < 16^(-L)                  ⟹   run of length L at n.
```

*Proof.* `{y_n} = j/15 + η` has leading digits `j…j` (`L` times) iff
`-j·16^(-L)/15 ≤ η < (15-j)·16^(-L)/15`; for `j ∈ {0, 15}` the two ends of the circle are the
digits `0…0` and `F…F`. ∎ In particular, with `q = 15·16^B`:

```text
L2 fails at B (no change in [B, 2B))   ⟹   q·‖qξ‖ ≤ 225/16;        q·‖qξ‖ < 15/16   ⟹   L2 fails at B.
```

So L2 is, up to the factor 15 between the two constants, the statement that `ξ` has only finitely
many approximations `p/q` of quality `C/q²` with `q = 15·16^B`.

**(b) Legendre regime (runs longer than their starting position).** If a run at `n` has length
`L ≥ n + 3`, then `q‖qξ‖ ≤ 225·16^(n-L) < 1/2` for `q = 15·16^n`, so (Legendre) the reduced form
of the nearest fraction `p/q` is a convergent `p_k/q_k` of `ξ`, `q = G q_k`, and

```text
a_(k+1)  >  G²·16^(L-n)/225  -  2.
```

Conversely, if a convergent has `q_k | 15·16^n` then `‖15·16^n ξ‖ < 15·16^n/(a_(k+1) q_k²)`, and a
run of length `⌊log_16(a_(k+1) q_k² /(15·16^n))⌋` starts at `n`. *Proof.*
`1/((a_(k+1)+2) q_k²) < |ξ - p_k/q_k| < 1/(a_(k+1) q_k²)`, and (a). ∎ Thus **runs with `L > n + 2`
are exactly large partial quotients at convergent denominators dividing `15·16^n`**, and the
ZSC-04 run bound (`L ≤ 41n` for `x = π/16`, `n ≥ 2`, from Mahler) reads: if a convergent
denominator `q_k` of `π/16` divides `15·16^n`, then `a_(k+1) q_k² < 15·16^(42n+1)`.

**(c) The L2 regime: near-convergents.** Let `ξ ∈ (0, 1)` be irrational with convergents
`p_j/q_j` (`j ≥ -1`, `(p_(-1), q_(-1)) = (1, 0)`), and let `p ≥ 0`, `q ≥ 1` be integers with
`p/q ≠ ξ` and `q|qξ - p| < c`. Then there are `m ≥ -1` and integers `r ≥ 0`, `s ≥ 1`, `t ≥ 1` with

```text
(p, q) = r·(p_(m+1), q_(m+1)) + s·(p_m, q_m) = s·(p_(m+2), q_(m+2)) - t·(p_(m+1), q_(m+1)),
r + t = s·a_(m+2),        min(r, t)·s  <  2c·(1 + 1/a_(m+2))  ≤  4c.
```

*Proof.* Take `p/q > ξ` (the other side is symmetric with even `m ≥ 0`). Let `m ≥ -1` be the
largest odd index with `p/q ≤ p_m/q_m`. Since `p_(m+1) q_m - p_m q_(m+1) = -1`, the integers
`r = q p_m - p q_m ≥ 0`, `s = p q_(m+1) - q p_(m+1) > 0`, `t = p q_(m+2) - q p_(m+2) > 0` satisfy
the two displayed identities and `r + t = s a_(m+2)`. With `δ_j = q_j ξ - p_j`,
`p - qξ = s|δ_(m+2)| + t|δ_(m+1)| ≥ t|δ_(m+1)| > t/(q_(m+1) + q_(m+2))`. If `r ≥ 1`,
`q = r q_(m+1) + s q_m ≥ (r/(a_(m+2)+1))(q_(m+1) + q_(m+2))`, so `c > rt/(a_(m+2)+1)`; as
`max(r, t) ≥ s a_(m+2)/2`, `min(r,t)·s < 2c(a_(m+2)+1)/a_(m+2)`. If `r = 0` there is nothing to
prove. ∎

*Import (Dujella 2004, Theorem 1, arXiv cs/0402052; read at source by the literature helper):
for coprime `a, b` with `|α - a/b| < c/b²`, `(a, b) = (r p_(m+1) ± s p_m, r q_(m+1) ± s q_m)` with
nonnegative `r, s`, `rs < 2c`.* The local statement has `4c` instead of `2c` and is not used with
the sharper constant anywhere.

**Consequence.** If L2 fails at `B`, then `15·16^B = r q_(m+1) + s q_m` for consecutive
convergent denominators with `min(r,t)·s < 57` (`c = 225/16`; the local statement does not need
`p, q` coprime. With the import, applied to the reduced fraction: `15·16^B/G = r q_(m+1) ± s q_m`,
`rs < 29`). **L2 for `ξ` ⟺ a bounded family of binary forms in consecutive convergent
denominators takes values of the shape `15·16^B/G` only finitely often.** For π nothing is known
about this; for runs of medium length (`1 ≪ L < n`) the approximation quality `16^(-L)/q` is
weaker than `1/q²` and carries no continued-fraction information at all — that is the range in
which (CH) lives.

*Checks.* `ContinuedFractionDictionary` (locality in both directions on 4000 exact rationals;
the decomposition on `> 1000` random near-convergents of `π/16`, with the imported `2c` form never
violated; the partial-quotient inequality on 29 convergents; longest run among the first 3050
hexadecimal digits of `π/16` is `≤ 5` — observational).

## RDT-04 — series do not certify their own digits; the effective base (PROVED LOCAL, elementary)

**(a) Partial sums are silent.** Let `b` be a prime power, `ξ = Σ_(j≥1) b^(-j) ρ(j)` with
rational `ρ(j)`, `P_n` the `n`-th partial sum, `I_n = ξ - P_n`, and `D_n` the least positive
integer prime to `b` with `D_n P_n ∈ Z[1/b]`. For the form `(1, P_n, I_n)` and `E = D_n`:
`u_m ≤ 1` for every `m`, so `b^m Q_m ≥ b^m D_n|I_n|`; and if `v_p(D_n P_n) ≤ -n·v_p(b)` (the last
term is present to full depth), then `u_m ≤ b^(m-n)` for `m ≤ n`. In that case
`b^m Q_m ≥ D_n·b^n|I_n|` **for every `m`**, and `b^n I_n = ρ(n+1)/b + O(|ρ(n+2)|/b²)`: the lemma
is silent as soon as `D_n|ρ(n+1)| ≥ 2b`. For rational-function forcing, `D_n` grows exponentially
(for the frozen four-pole source it is divisible by every odd number below `2n`) while
`ρ(n+1)` decays polynomially. **A BBP-type series does not certify a restricted bound through its
own partial sums, whatever the base.** (The Dalzell-type integrals in (c) fail for the same
reason, RDT-02(c).)

**(b) The effective base.** What a series offers per unit of denominator growth is its *effective
base* `b_eff = b^(1/d)`, where the `j`-th term introduces denominators of size `≈ d·j`. In the
variable in which the source is a logarithm series `-log(1 - x) = Σ x^k/k`, `b_eff = 1/|x|`:

| Source | Series variable | `b_eff` | `log b_eff` |
|---|---|---|---|
| frozen four-pole BBP (`π/16`) | `x = (1 ± i)/2`, `x⁸ = 1/16` | `√2` | `0.347` |
| Bellard-type (`2^10`, denominators `≈ 10j`) | — | `2` | `0.693` |
| `log 2 = Σ 1/(k 2^k)` | `x = 1/2` | `2` | `0.693` |
| `log(16/15) = Σ 1/(k 16^k)` (pole vector `8·e_8`) | `x = 1/16` | `16` | `2.773` |

Padé acceleration (RDT-07, import) turns a large effective base into a restricted exponent below
1; the threshold in Rivoal's theorem at numerator 1 is `b_eff ≥ 12` (`log 12 = 2.485`).
(`test_series_self_certification_table`.)

**(c) The Dalzell family.** For integers `a, b ≥ 1`,
`∫_0^1 x^(4an)(1-x)^(4bn)/(1+x²) dx = A_n π + B_n` with

```text
A_n = (-1)^(bn)·4^(bn-1)       (a pure power of 2: the best possible 2-free height, H = E_n),
```

because `x^(4an)(1-x)^(4bn)` takes the real value `(1 ∓ i)^(4bn) = (-4)^(bn)` at `x = ±i`, so the
remainder on division by `1 + x²` is that constant. Let `E_n` be the odd denominator of `B_n`.
Since every admissible unit divides `(E_n A_n)_S = 4^(bn-1)`, RDT-01 can speak at some `m` only if
`E_n < 4^(bn-1)/|I_n|`, and (sharper, RDT-02(c)) only if `E_n|I_n| < 2^(v_2(E_n B_n))`. In the
normalisation `a + b = 1` (degree `4n`), `4^(bn)/|I_n| = e^((φ(a)+o(1))n)` with
`φ(a) = 4H(a) + (1-a) log 4`, `H` the entropy, and

```text
max_(0<a<1) φ(a) = φ(√2 - 1) = 4 log(1 + √2) = 3.5255… < 4 = lim (1/n) log lcm(1, …, 4n),
```

so the first condition already requires that more than 11.8 % of the logarithm of the generic
denominator cancel. OBSERVED
(`RESULTS_rde.json`, `a = b = 1`, `n ≤ 8`): `v_2(B_n) ≤ 4` while `v_2(A_n) = 2n - 2`, and
`log(E_n|I_n|)/n` increases through `0` at `n = 4`. So these forms carry a **large 2-adic
imbalance on the coefficient of π** — the kind RDT-02(b) wants — and are useless by RDT-02(c):
they do not converge. (`DalzellAndSeries`.)

## RDT-05 — `log 2` at powers of two: a restricted exponent below the unrestricted record (PROVED LOCAL; imports: prime number theorem)

For positive integers `a, b, c` with `b ≥ c` and `a + b > c` put

```text
F(x) = x^a (1-x)^b / (1+x)^c,            M_0 = max_[0,1] F = e^(-α),
R(ρ) = (1+ρ)^a (2+ρ)^b / ρ^c,            R_* = min_(ρ>0) R,
N_* = max(a+b-c, c),     γ = (b-c) log 2,
Ω = { ω ≥ 1/N_* : {aω} + {bω} < {cω} },   s = ∫_Ω dω/ω²,     δ' = N_* - s.
```

(`x_0`, the maximiser, is the root in `(0,1)` of `(c-a-b)x² - (b+c)x + a = 0`; the minimiser of
`R` is the positive root of `(a+b-c)ρ² + (2a+b-3c)ρ - 2c = 0`; `Ω` is a union of intervals with
rational endpoints, `1`-periodic above `1/N_*`, so `s` is a convergent series of positive
rationals and every partial sum `s_J` is a rigorous lower bound.)

**Theorem.** If `α > δ'`, then

```text
v_2(log 2)  ≤  ( log R_* + δ' - γ ) / ( α - δ' + γ ).                                       (5.1)
```

The same forms give, for unrestricted denominators, only `μ(log 2) - 1 ≤ (log R_* + δ')/(α - δ')`.

| `(a, b, c)` | `α` | `log R_*` | `N_*` | `s` | restricted (5.1) | unrestricted, same forms |
|---|---|---|---|---|---|---|
| `(1, 1, 1)` (Legendre) | 1.762747 | 1.762747 | 1 | 0 | 3.6221 | 3.6221 |
| `(6, 8, 7)` | 11.844978 | 12.681472 | 7 | 1.457754 | 2.5058 | **2.891400** |
| `(4, 6, 5)` | 8.259745 | 9.154247 | 5 | 1.157480 | 2.4076 | 2.9423 |
| **`(2, 4, 3)`** | 4.591777 | 5.624722 | 3 | 0.740695 | **2.3767** | 3.3801 |

With the rational truncation `s_60 = 0.73652…` the theorem gives, for `(2, 4, 3)`:

```text
v_2(log 2) ≤ 2.3814,     i.e.  ‖2^m log 2‖ ≥ 2^(-2.3814 m)  for all m ≥ m_0   (m_0 not computed).
```

The same exponent holds for `‖g·2^m log 2‖` with any fixed integer `g ≥ 1` (in particular at the
denominators `15·16^m`), by the multiplier `g` of RDT-01.

*Calibration against the literature.* The unrestricted column for `(6, 8, 7)` is
`2.89139977`, i.e. `μ(log 2) ≤ 3.89139977`; the fetched text of Marcovecchio (2009) quotes
Rukhadze's bound as `3.89139978` and proves `μ(log 2) ≤ 3.57455391`. The agreement to eight digits
is a consistency check of the rate and saving formulas, not a verification of either paper.
Against the best unrestricted bound, `μ - 1 ≤ 2.57455391`, the restricted bound (5.1) is smaller
for `(2,4,3)`, `(4,6,5)` and `(6,8,7)`. **It is still far above 1**, so by ZSC-01 it has no
bearing on any saving. Rivoal's tabulated restricted bound for `log 2` at powers of two is
`Λ(1,2,1) - 1 = 3.6221` (the Legendre value); his §7 suggests applying Rukhadze's method to
restricted denominators, which is what this theorem does at the point `x = -1`. No claim of
novelty is made.

*Proof.* Let `n ≥ 1` and substitute `t = 1 + x`:
`I_n := ∫_0^1 F^n dx/(1+x) = ∫_1^2 P(t) t^(-cn-1) dt`, `P(t) = (t-1)^(an)(2-t)^(bn) = Σ_i p_i t^i ∈ Z[t]`. Hence

```text
I_n = A_n log 2 - B_n,      A_n = p_(cn),      B_n = - Σ_(i≠cn) p_i (2^(i-cn) - 1)/(i - cn).
```

1. *Sizes.* `0 < I_n ≤ M_0^n log 2` and `I_n^(1/n) → M_0` (`L^n → L^∞` for a continuous positive
   function). By Cauchy's formula on `|t| = ρ`, `|A_n| ≤ ((1+ρ)^a (2+ρ)^b ρ^(-c))^n`, so
   `|A_n| ≤ R_*^n`.
2. *2-adic tilt.* The coefficient of `t^j` in `(2-t)^(bn)` is divisible by `2^(bn-j)`, so
   `v_2(p_i) ≥ (bn - i)^+`; hence `2^((b-c)n) | A_n`. In `B_n`, a term with `i < cn` has valuation
   `≥ (bn - i) - (cn - i) - v_2(cn - i) ≥ (b-c)n - v_2(cn-i)` and a term with `i > cn` has valuation
   `≥ -v_2(i - cn)`; so `v_2(B_n) ≥ -λ_n`, `λ_n := ⌊log_2(N_* n)⌋`. The tilt is real: `A_n` carries
   `2^((b-c)n)` and `B_n` does not (OBSERVED: `-4 ≤ v_2(B_n) ≤ 0` in every case of
   `RESULTS_rde.json`; only the lower bound is used).
3. *Odd denominators and saved primes.* The odd part of the denominator of `B_n` divides the odd
   part `D_n` of `lcm(1, …, N_* n)`. Let `p` be an odd prime with `p² > N_* n` and
   `(an mod p) + (bn mod p) < (cn mod p)`. Writing `an = a_0 + a_1 p`, `bn = b_0 + b_1 p`,
   `P(t) ≡ (t-1)^(a_0)(2-t)^(b_0)·(t^p - 1)^(a_1)(2 - t^p)^(b_1) (mod p)`; a monomial `t^i` with
   `i ≡ cn (mod p)` would need an exponent `e ≡ cn (mod p)` with `0 ≤ e ≤ a_0 + b_0 < (cn mod p)`
   from the first two factors — impossible. So `p | p_i` for every `i ≡ cn (mod p)`: `p | A_n`, and
   every term of `B_n` whose denominator `i - cn` is divisible by `p` (exactly once, since
   `p² > N_* n`) is `p`-integral. With `Δ_n := D_n / ∏ p` over these primes, `Δ_n B_n ∈ Z[1/2]`.
   By the prime number theorem, `log Δ_n ≤ (δ' + o(1)) n`: the primes concerned are those with
   `n/p ∈ Ω`, and `Σ_(n/v < p ≤ n/u) log p = n(1/u - 1/v) + o(n)`; primes below `n/W` contribute
   at most `(1+o(1)) n/W`, so truncating `Ω` at `ω ≤ W` and letting `W → ∞` loses nothing.
4. *Transference.* Apply RDT-01 with `b = 2`, `E = Δ_n`, `u = 2^((b-c)n)`: `H_n = Δ_n|A_n|/u ∈ Z`
   by step 2, and `2^m Δ_n B_n/u ∈ Z` for `m ≥ (b-c)n + λ_n`. In the notation of RDT-02(d):
   `θ = α + γ - δ'`, `χ = log R_* + δ' - γ`, `m_0(n) log 2/n → γ < θ` (this is `α > δ'`),
   `liminf (1/n) log I_n = -α`, `β = log R_*`. Both terms of RDT-02(d) equal the right side of
   (5.1). ∎

*Remarks.* (1) The triples `(a,b,c)`, `(b, a, a+b-c)` and `(c, a+b-c, a)` give proportional forms
(the substitution `x ↦ (1-x)/(1+x)`, and the symmetry of the hypergeometric function in its two
upper parameters); e.g. `(7,7,8)` — the weights for which the classical formula gives
`3.8914` — is `(6,8,7)`, where the tilt `b - c = 1` is visible. Proportionality is checked
exactly in `test_symmetries_give_proportional_forms`; it is used only to explain the table. (2) *Why `log 2` has a
tilt at 2:* the pole `x = -1` and the endpoint `x = 1` are congruent modulo 2, because the
argument of the logarithm — the ratio `(1 - (-1))/(0 - (-1)) = 2` of the two endpoint distances
to the pole — is itself divisible by the base. (3) A bounded scan (`c ≤ 21`, `a, b ≤ 33`) found
no triple below `2.3767`; nothing is claimed about optimality, and the refined constructions
behind `3.5746` were not examined for their own tilt.

*Checks.* `TiltedLegendreLog2`: for seven triples and `n ∈ {1,2,3,5}` every ingredient of steps
1–3 (integrality, both valuations, `Δ_n B_n ∈ Z[1/2]`, `p | A_n` for each saved prime, the Cauchy
bound, `0 < I_n ≤ M_0^n log 2`); a mutation (the unsaved prime 29 cannot be removed at
`(4,6,5)`, `n = 12`); the certified inequality of step 4 for `(4,6,5)`, `n ≤ 8`, against the true
`‖2^m log 2‖` on every admissible `m`.

## RDT-06 — π: where the 2-adic imbalance sits (one lemma PROVED LOCAL; the rest OBSERVED / CONDITIONAL)

**Family.** `N(z) = (z² - 2z + 2)^a M(z)`, `M ∈ Z[z]`, `D = deg N`, pole order `c`, endpoints
`p = 1 + i` and `p̄`:

```text
J_n := (1/i) ∫_(p̄)^(p) N(z)^n z^(-cn-1) dz  =  A_n·(π/2) + B_n,      A_n = [z^(cn)] N^n ∈ Z,
B_n = Σ_(k≠0) [z^(cn+k)]N^n · 2 Im((1+i)^k)/k ∈ Q
```

(path through the positive real axis). With `M = (z-1)^2`, `a = 2`, `c = 3` this is a Hata-type
family (conjugate endpoints, real pole) — the configuration of the constructions that prove
irrationality measures of π.

**(a) Lemma (2-adic shadow; PROVED LOCAL, using the standard fact that the 2-adic logarithm
vanishes on roots of unity).**

```text
v_2(B_n)  ≥  (2a - c/2)·n  -  log_2(Dn + 1)  -  1/2,          v_2(A_n) ≥ (a - c/2) n   (c ≤ 2a).
```

*Proof.* Work in `K = Q_2(i)`, `v(2) = 1`, `v(1+i) = 1/2`. Put `z = p̄(1 - θs)`, `θ = 1 - i`
(`z(0) = p̄`, `z(1) = p`). For `k ≠ 0`, `z(s)^k` is a power series in `s` convergent on `|s| ≤ 1`,
and `ℓ(s) = log(1 - θs) = -Σ θ^j s^j/j` converges at `s = 1` with `ℓ(1) = log_2(i) = 0`
(`i` is a principal unit and `4 log_2 i = log_2 1 = 0`). Termwise,
`d/ds [Σ_(k≠0) P_(cn+k) z^k/k + A_n ℓ(s)] = N(z)^n z^(-cn-1) z' =: G(s) = Σ g_j s^j`, so, both
sides vanishing at `s = 0` and converging at `s = 1`, `i·B_n = Σ_j g_j/(j+1)`. Now
`z - p̄ = 2is`, `z - p = 2i(s-1)`, so
`G = -θ p̄^(-cn)·(2i)^(2an)·(s(s-1))^(an) M(z(s))^n·Σ_j C(cn+j, j) θ^j s^j`, a prefactor of valuation
`2an - cn/2 + 1/2` times a series whose `j`-th coefficient has valuation `≥ (j - Dn)^+/2`. Since
`r/2 - log_2(1+r) ≥ -1` for integers `r ≥ 0`, `v(g_j/(j+1)) ≥ 2an - cn/2 + 1/2 - log_2(Dn+1) - 1`.
For `A_n`: the coefficient of `z^j` in `(z²-2z+2)^(an)` is divisible by `2^(an - ⌊j/2⌋)`. ∎

So **in every such family the rational part `B_n` is 2-adically small**: the 2-adic counterpart
of the form `A_n·log(p/p̄) + i B_n` is a convergent 2-adic integral, and its "period" `log_2(i)`
is zero. By RDT-02(b) the imbalance `v_2(A_n) < v_2(B_n)` is on the wrong side for π:

**(b) OBSERVED.** For the seven families `(a, deg-1 factor, (z-2)-factor, c)` of
`RESULTS_rde.json` and `n ∈ {12, 18}`: `v_2(A_n/2) < v_2(B_n)` in every case (e.g. Hata type:
`13` against `43` at `n = 18`), and the restricted and unrestricted quotients of RDT-01 for π are
**equal** at every tested `n`. The even real family of the round's scout,
`∫_(-1)^1 t^(2bn)(1-t²)^(an)(1+t²)^(-cn-1) dt` (two real poles, conjugate endpoints in the same
coordinates), shows the same equality for almost all weights tried and never converges. Numerator roots 2-adically closer to the pole than the
endpoints (`(z-2)^b`, `b > c`) do raise `v_2(A_n)` but cost at least as much at the Archimedean
place (product formula) and by RDT-02(c) cannot rescue a family.

**(c) Where a π-side imbalance does occur.** With *real endpoints and conjugate poles* (Dalzell,
RDT-04(c)) the coefficient of π is highly 2-divisible and `B_n` is not — the `log 2` mechanism,
the endpoint `1` being congruent to the poles `±i` modulo `1 + i`. But a pure π-form of this type
needs pole order 1 (higher order brings `log 2` in), and then the family does not converge.
**OBSERVED dichotomy:** the forms that converge have the imbalance on the constant term; the
forms with the imbalance on π do not converge. No family with both properties was found; none is
proved not to exist.

**(d) CONDITIONAL by-product: restricted numerators, i.e. `1/π`.** Reading the same forms as
`B_n·(1/π) + A_n/2 = J_n/π` reverses the roles, and (a) gives `u = 2^(⌈(2a-c/2)n - log_2(Dn+1) - 1/2⌉)`,
admissible for `m ≥ an + 1`. For `N = (z²-2z+2)²(z-1)²`, `c = 3`: on the segment `z = 1 + it`,
`|J_n| ≤ 2 e^(-αn)` with `α = 2.29589` (elementary), `|A_n| ≤ e^(4.55634 n)` (Cauchy on
`|z| = ρ`, the maximum being at `z = -ρ`), odd denominators `≤ e^((3 - s + o(1)) n)` with
`s ≥ s_60 = 0.6425` (the Frobenius argument of RDT-05 step 3 with the condition
`3·(2n mod p) < (3n mod p)`; checked exactly for `n ≤ 25`). RDT-01 then yields: *for every large
`m` and every integer `p` other than the single value `p_*(m) = -2^(m-1) A_n/B_n`,*

```text
| 2^m/π - p |  ≥  2^(-3.11 m).
```

The exceptional integer is not excluded (no lower bound for the oscillating `|J_n|` and no
determinant identity is proved here), so **`v_2(1/π) ≤ 3.11` is CONDITIONAL** on a non-vanishing
statement; unconditionally the exceptional case only has the unrestricted bound. Finite
certified exponents from the exact forms (`n ≤ 24`): `1.6–2.0` for `1/π` against `3.7–4.7`
unrestricted, and no gain for π (`RESULTS_rde.json`; `test_lemma_on_pi_and_reciprocal_pi`). This
concerns approximations `π ≈ 2^m/p` (numerators powers of two), not the hexadecimal digits of π.

## RDT-07 — a restricted exponent below 1 inside the period class `V` (CLASSICAL IMPORT + PROVED LOCAL extension)

**Import (Rivoal 2007, *Convergents and irrationality measures of logarithms*, Rev. Mat.
Iberoam. 23, 931–952, Theorem 1; statement and §§2–3 read in the fetched text).** For integers
`a, b, c` with `0 < |a/b| < 1`, `b ≥ 2`, `c ≥ 1` and a non-empty admissible set, every `ε > 0`,
every `u ∈ Z` and all large `m`: `|log(1 - a/b) - u/(bc)^m| ≥ (bc)^(-(Λ(a,b,c)+ε)m)`, with the
explicit `Λ` of his (1.3)–(1.6). He states `Λ(1, b, 1) < 2` for `|b| ≥ 12`.

**COMPUTED FROM IMPORT** (`rde_core.rivoal_Lambda`, which reproduces ten entries of his table to
`3·10^(-6)`): `Λ(1, 16, 1) = 1.881272` at `κ = 5.5106`. Hence, for

```text
ξ_* := log(16/15) = Σ_(n≥1) 16^(-n)/n = L(8·e_8)      (ZSC-06 convention; a proper zero-seeded
                                                        source with the single pole 8n; ξ_* ∈ V∖{0}),
v_16(ξ_*)  ≤  0.881272  <  1.
```

**Extension to the denominators `g·16^m` (PROVED LOCAL from his Lemmas 1 and 2).** The statement
of Theorem 1 does not cover `15·16^m`, nor `2^M` with `4 ∤ M`. Both follow from RDT-01 applied
to his forms: with `x = 1/16` and `p/q = κ`, his Lemma 1 gives `16^(qn) B_(pn,qn)(x) ∈ Z`,
`d_(pn) 16^(pn) A_(pn,qn)(x) ∈ Z`, and Lemma 2 gives `|R_(pn,qn)(x)|^(1/qn) → ρ` (a limit, so it
also serves as the lower bound needed in case (ii)) and `limsup |B|^(1/qn) ≤ β`. Take `E` the odd
part of `d_(pn)` and `u = 16^(-qn)`: then `H = E·|16^(qn)B|`, `Q = E·16^(qn)|R|`, and (1.1) holds
for `m ≥ (p-q)n + log_16(pn)` **for every fixed `g`**. RDT-02(d) gives the exponent
`log(16 e^κ β)/(-log(16 e^κ ρ)) = L(κ) - 1`, and its third condition is his hypothesis
`16^κ e^κ ρ < 1`. In his own proof the same constant is absorbed in two places: the trivial lower
bound for the distance between two distinct rationals (first display of each case of §3) and the
conditions (3.3)/(3.7), where it shifts the admissible `n` by `O_g(1)`. So for every integer
`g ≥ 1` and `ε > 0`:

```text
‖ g·16^m ξ_* ‖  ≥  16^(-(0.881272 + ε) m)        (m ≥ m_0(g, ε)),      and   v_2(ξ_*) ≤ 0.881272.
```

(`RivoalImport`: his Padé forms are rebuilt exactly, their integrality and remainder checked,
and RDT-01 is verified against the true `‖g·16^m ξ_*‖` for `g ∈ {1, 2, 4, 8, 15}`.)

**Consequences for the rungs of ZSC-04, for `ξ_*` (PROVED LOCAL given the above).**

1. Every run of equal hexadecimal digits of `ξ_*` starting at position `n` has length
   `≤ (0.8813 + ε) n + 1` for `n ≥ n_0(ε)` (RDT-03(a) with `g = 15`).
2. **L2 holds for `ξ_*`:** every shell `[B, 2B)` with `B` large contains a digit change — indeed
   every window `[n, n + ⌈0.89 n⌉]` does. This is the first rung above L1 for a nonzero element
   of `V`, and it uses the multiplier 15 (for runs of `0` or `F` the import alone suffices).
3. The number of changes among the first `N` digits is `≥ log N/log 1.89 - O(1)`: still
   logarithmic. **(CH) for `ξ_*` is OPEN.**
4. The necessary Diophantine cost of a saving (ZSC-01) is **paid** for `ξ_*`: the law no longer
   forbids a saving `η ≤ 2(1-v)/(1+v) = 0.126` at any mode. It gives no saving.

**Which elements of `span_Q{log 2, log 3, log 5} ⊂ V` this reaches (COMPUTED FROM IMPORT).** The
candidates are `log(N/2^i)` with `N` odd and `{3,5}`-smooth, `0 < N < 2^(i+1)`. For `i ≤ 12`:

| value | `(a, b)` | `Λ` | | value | `(a, b)` | `Λ` |
|---|---|---|---|---|---|---|
| `log(15/16)` | `(1, 16)` | **1.881272** | | `log(3/2)` | `(-1, 2)` | 3.547471 |
| `log(125/128)` | `(3, 128)` | 2.111892 | | `log(2025/2048)` | `(23, 2048)` | 3.889991 |
| `log(9/8)` | `(-1, 8)` | 2.211331 | | `log(1/2)` | `(1, 2)` | 4.622101 |
| `log(5/4)` | `(-1, 4)` | 2.901691 | | `log(243/256)` | `(13, 256)` | 6.699298 |
| `log(3/4)` | `(1, 4)` | 3.004521 | | `log(9/16)`, `log(25/32)`, `log(81/64)`, … | | admissible set empty |

Only `log(15/16)` is below 2. For numerator `±1` this is the complete list: `2^i ∓ 1` is
`{3,5}`-smooth only for `i ≤ 4` (a primitive prime divisor `≥ 7` exists otherwise). The three
values `log(15/16)`, `log(125/128)`, `log(243/256)` form a `Z`-basis of
`Z log 2 + Z log 3 + Z log 5`, but restricted exponents are not linear, so nothing follows for
`log 2`, `log 3` or `log 5` themselves (for `log 2`, RDT-05 gives `2.3767`).

## RDT-08 — the missing invariant of the π-line (PROVED LOCAL lemma; verdict)

**Lemma (no small argument for π).** Let `x ∈ C` with `1 - x = r e^(iθ)`, `r > 0`,
`θ ∈ (π/4)Z ∖ 2πZ`. Then `|x| ≥ 2^(-1/2)`, with equality exactly for `x = (1 ± i)/2`.

*Proof.* `|x|² = 1 - 2r cos θ + r² ≥ sin²θ` if `cos θ > 0` (minimum at `r = cos θ`) and `≥ 1`
otherwise; among the admissible `θ` only `θ ≡ ±π/4` has `cos θ > 0`. ∎

So a single logarithm `log(1 - x)` whose imaginary part is a nonzero multiple of `π/4` has
effective base `1/|x| ≤ √2`, and the extremal point `x = (1 ± i)/2` is **exactly the BBP point**:
`π = 4 Im Σ_k ((1+i)/2)^k/k`, `((1+i)/2)^8 = 1/16`, the frozen four-pole source being this series
grouped modulo 8. More generally all eight natural generators `log(1 - ζ_8^k/√2)` of `V` have
`|x| = 2^(-1/2)`; the large effective base of `ξ_* = log(1 - 1/16)` arises from a rational
combination that collapses to one real logarithm of a `{2,3,5}`-unit close to 1, and no such
collapse can carry an argument.

**Verdict on the probe of NEXT.md: Outcome B, in a precise form.**

- A restricted exponent below 1 **exists** in `V`: `v_16(log(16/15)) ≤ 0.8813` (IMPORT, Rivoal),
  with L2 as a consequence at the denominators `15·16^m` (PROVED LOCAL extension).
- A restricted exponent below the best known unrestricted one exists for `log 2`:
  `v_2(log 2) ≤ 2.3814 < 2.5746` (PROVED LOCAL, unaudited; still above 1).
- Both use one structure: **a non-unit, at a prime of the base, in the argument of the
  logarithm** (`16/15` against base 16; the ratio 2 of endpoint distances for `log 2`), which
  makes the coefficient `A_n` of the number more divisible than the constant term `B_n`
  (RDT-02(b)), and — to get below 1 — a large effective base (`≥ 12` in the import).
- The π-line lacks both. Its argument is a root of unity, congruent to 1 at the prime above 2:
  the single-logarithm effective base is at most `√2` (Lemma), and in the convergent Gaussian
  families the 2-adic imbalance falls on `B_n` (RDT-06(a)), so the forms bound restricted
  *numerators* (`‖2^m/π‖`) and give for π exactly the unrestricted exponent (OBSERVED).
- **Not claimed:** that `v_16(π) < 1`, or even `v_2(π) < μ(π) - 1`, is false or unprovable. Only
  that the Padé table of one logarithm and the one-pole Gaussian families examined here do not
  reach it. Machin-type representations (several logarithms with small arguments, e.g.
  `4 arctan(1/5) - arctan(1/239)`) have large individual effective bases but require simultaneous
  approximation with a common denominator; they were not examined.

**Exact remaining statements.**

1. (π, OPEN) Exhibit a family of forms `A_n π - B_n` with integer-normalised errors `→ 0` and
   `v_2(A_n) - v_2(B_n) ≥ cn`, `c > 0`; or prove that the 2-adic shadow argument of RDT-06(a)
   extends to every family built from logarithms of Gaussian (or cyclotomic) numbers with a
   convergent 2-adic counterpart, which would make the wrong-side imbalance a theorem.
2. (`log 2`, OPEN) `v_2(log 2) < 1`. The tilt of RDT-05 is one factor of 2 per step against
   denominators `e^(δ')`; reaching 1 needs an effective base of Rivoal's size, which `log 2`
   does not have at `x = 1/2` or `x = -1`.
3. (`ξ_* = log(16/15)`, OPEN) (CH). It is now the natural test object of the programme: a proper
   zero-seeded element of `V` for which L2 is proved and the Diophantine obstruction of ZSC-01 is
   absent, so that any failure of (CH) there would have to come from the medium scale alone.
4. (`1/π`, CONDITIONAL) the non-vanishing statement of RDT-06(d).

## Falsifiers and what was not verified

- RDT-01/02: one form, base, multiplier and `m` with `‖g b^m ξ‖` below the stated bound refutes
  the lemma. None in `> 1500` random instances and in every structured instance of the tests.
- RDT-05: any `n` with `Δ_n B_n ∉ Z[1/2]`, `2^((b-c)n) ∤ A_n`, `|A_n| > R_*^n` or
  `I_n > M_0^n log 2` refutes a step; a value `‖2^m log 2‖ < 2^(-2.39 m)` for arbitrarily large
  `m` refutes the theorem. The asymptotic steps (prime number theorem in the interval form;
  `I_n^(1/n) → M_0`) are standard and were **not** independently audited; `m_0` is not explicit.
- RDT-06(a): one `n` with `v_2(B_n)` below the bound. (b)–(d) are observations and a conditional
  statement; the saddle-point rate `2.4549` (which would give `2.84` in (d)) is heuristic and not
  used.
- RDT-07: rests on Rivoal's Theorem 1 and Lemmas 1–2 as read in a fetched text copy (scratch,
  not in the repository); `Λ(1,16,1)` is a numerical evaluation of his formula, not an interval
  enclosure. The table of smooth numerators was searched for `i ≤ 12` only.
- Literature values `3.57455391`, `3.89139978` are as printed in the fetched Marcovecchio text;
  Dujella's theorem as printed in arXiv cs/0402052. Legendre's theorem and the 2-adic logarithm
  are used from their standard statements.
- No part of this file was reviewed by a second reader at the time of writing.
