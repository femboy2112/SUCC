# Mason–Stothers (polynomial abc): a SUCC Proof-Forge certificate

**Date:** 2026-10-20. **Branch:** `research/proof-forge-mason-stothers-2026-10-20`.
**Status:** **CLASSICAL** (Stothers 1981; Mason 1984). The theorem is not original to SUCC; the
contribution is the proof-certificate *representation* (`observational_succ/mason_stothers.py`), the
exactly-verified counterexample corpus, the honest Lean arithmetic core, and the integer-transfer
obstruction account. **RH / integer abc: untouched and OPEN.** No float is used as a certificate.

---

## 1. Statement

Let `K` be a field and `A, B, C ∈ K[x]` nonzero, **pairwise coprime**, **not all constant**, with
`A + B = C`. Assume `char K = 0` (or `char K > max(deg A, deg B, deg C)`). Then

> **max(deg A, deg B, deg C) ≤ deg rad(ABC) − 1,**

where `rad(P)` is the product of the distinct monic irreducible factors of `P`, equivalently the
squarefree part `P / gcd(P, P')`.

The characteristic hypothesis is essential (§6).

## 2. The principal invariant: the Wronskian

Define `W = W(A, B) = A'B − AB'`. Because `A + B = C` (so `A' + B' = C'`):

- `W(A, B) = A'B − AB' = A'(C−A) − A(C'−A') = A'C − AC' = W(A, C)`,
- `W(B, C) = B'C − BC' = B'(A+B) − B(A'+B') = B'A − BA' = −(A'B − AB') = −W(A, B)`.

So the three pairwise Wronskians coincide up to sign:
`W(A,B) = W(A,C) = −W(B,C)`. (Verified exactly in code: `test_wronskian_forms_all_equal_up_to_sign`
and the certificate step `W(A,B)=W(A,C)=-W(B,C)`.)

## 3. Nonvanishing of W (needs char 0)

`(A/B)' = (A'B − AB') / B² = W / B²`. So `W = 0 ⟺ (A/B)' = 0`. In characteristic 0, `(A/B)' = 0`
forces `A/B` constant; with `gcd(A,B)=1` this makes `B` a unit (constant), then `A` and
`C = A + B` are constant too — contradicting "not all constant". Hence **`W ≠ 0`** in char 0.

(In char `p` the implication `(A/B)'=0 ⟹ A/B` constant FAILS — e.g. `(x^p)' = 0` — which is the whole
story of §6.)

## 4. Multiplicity bound and the divisibility `(ABC)/rad(ABC) | W`

Let `P` be irreducible with `m = v_P(A) ≥ 1`. Write `A = P^m a`, `P ∤ a`. Then
`A' = P^{m−1}(m P' a + P a')`, and in char 0 (with `deg P' < deg P`, `P ∤ m`, `P ∤ a`) one gets
`v_P(A') = m − 1` exactly. Since `P | A` and `A, B` coprime, `P ∤ B`, so

- `v_P(A'B) = m − 1`,
- `v_P(A B') = m + v_P(B') ≥ m`,

whence `v_P(W) = v_P(A'B − AB') = m − 1` (the two valuations differ, so the minimum is attained
strictly). The same holds for prime factors of `B` and `C` via the two other Wronskian forms. As
`A, B, C` are pairwise coprime, each irreducible `P` divides exactly one of them, with
`v_P(ABC) = v_P(\text{that one})`, and

> `P^{v_P(ABC) − 1} | W` for every `P | ABC`  ⟹  **`(ABC)/rad(ABC) = ∏_P P^{v_P(ABC)−1}` divides `W`.**

(Verified exactly as `W mod M == 0` with `M = ABC/rad(ABC)` — certificate step `(ABC)/rad(ABC) | W`.
A backwards divisibility direction in the first draft was caught by the independent adversarial oracle
in §5: first-draft tests were all *tight*, where `M` and `W` are scalar multiples and the error is
invisible.)

## 5. Degree comparison

`W ≠ 0` and `M := (ABC)/rad(ABC)` divides `W`, so `deg M ≤ deg W`. Also
`deg W = deg(A'B − AB') ≤ deg A + deg B − 1` (and the two cyclic forms). With
`deg M = deg(ABC) − deg rad(ABC) = deg A + deg B + deg C − deg rad(ABC)`:

```
deg A + deg B + deg C − deg rad(ABC) = deg M ≤ deg W ≤ deg A + deg B − 1
  ⟹  deg C ≤ deg rad(ABC) − 1.
```

The two cyclic Wronskian forms (`deg W ≤ deg B + deg C − 1`, `≤ deg A + deg C − 1`) give the same bound
for `deg A` and `deg B`. Hence `max(deg A, deg B, deg C) ≤ deg rad(ABC) − 1`. ∎

**This final step is the one formalized in Lean** (`formal/MasonStothersDegreeDescent.lean`,
`degree_descent` / `degree_descent_all`): a mathlib-free, `omega`-closed, kernel-checked integer
inequality with axioms `{propext, Quot.sound}` (no `Classical.choice`). The polynomial lemmas of
§3–§4 are **disclosed formalization debt** (they need a polynomial/UFD/derivation library); they are
verified exactly in sympy, not faked in Lean.

## 5′. Two independent verification routes

Per the Proof-Forge discipline, the certificate is checked by two methodologically distinct routes:

1. **Certificate oracle** (`mason_stothers_certificate`, sympy over an exact field): per-triple it checks
   hypotheses, the three-form Wronskian agreement, `W ≠ 0`, `M | W`, and the degree bound.
2. **Independent adversarial oracle** (`scratchpad/ms_oracle.py`): 380 random coprime triples over `ℚ`
   and `GF(11)` (char > deg), with the radical degree recomputed by `factor_list` (distinct irreducible
   factors) — a *different* route than the module's `gcd`-squarefree `poly_radical`. Result:
   **0 bound violations, 0 radical mismatches, 0 unverified valid triples.** The disagreement between the
   routes in the first draft (the backwards divisibility) is exactly what the second route is for.

## 6. Hostile controls (hypotheses are load-bearing)

| control | what breaks | certificate |
|---------|-------------|-------------|
| all constant (`A=B=1`) | "not all constant" | raises / `hypotheses_ok=False` |
| coprimality failure (`A=B=x`) | pairwise coprime | raises / `hypotheses_ok=False` |
| sum mismatch (`A+B≠C`) | `A+B=C` | raises |
| **char p: `A=x^p, B=1, C=(x+1)^p` over `GF(p)`** | `W ≠ 0` | `W_is_zero=True`, `verified=False`, bound violated (`deg = p > 1 = deg rad −1`) |

The **characteristic-`p` counterexample** is the sharp one. In `GF(p)`, `(x+1)^p = x^p + 1`
(freshman's dream), so `A + B = x^p + 1 = C`; the triple is coprime and nonconstant; `rad(ABC) =
x(x+1)` has degree 2. The bound would claim `p ≤ 1`. It fails because `W = (x^p)'·1 − x^p·0 = p·x^{p−1}
= 0` in `GF(p)` — **the invariant vanishes identically**. (Exactly reproduced: `test_char_p_collapse`.)

## 7. Why this does NOT transfer to the integers (abc stays OPEN)

`integer_transfer_obstruction()` records the honest account; no integer abc result is claimed.

1. **No nonzero derivation on ℤ.** Any ring derivation `D : ℤ → ℤ` is identically zero
   (`D(1)=D(1·1)=2D(1) ⟹ D(1)=0`, then additivity). So the Wronskian `W = a'b − ab'` is identically `0`
   over `ℤ` — the carrying invariant simply does not exist.
2. **No archimedean size-drop.** `deg` is the valuation at infinity, and the proof crucially uses
   `deg P' = deg P − 1`: differentiation drops size by exactly one while obeying Leibniz. `log|n|` is the
   integer analogue of `deg`, but there is **no** operation on `ℤ` reducing `log|n|` by a bounded amount
   subject to a product rule.
3. **p-derivations are local.** Buium's `δ_p` give an arithmetic differential calculus, but they are
   `p`-adic and see one prime at a time; there is no single global object playing the role of the
   Wronskian with controlled archimedean size. The arithmetic derivative `n'` (`p'=1`, Leibniz) has no
   deg-drop property and grows, so yields no Mason–Stothers analogue.

This is precisely why Mason–Stothers is a one-page theorem while integer abc is open.

## 8. Novelty assessment

The theorem and the Wronskian proof are **classical and standard** (Stothers 1981; Mason 1984; the
`W = A'B − AB'` presentation is textbook, cf. Lang, Snyder). There is **no mathematical novelty** here.
The SUCC contribution is strictly infrastructural: (a) a reusable, exact, independently-checkable
proof-certificate object; (b) an exact counterexample corpus including the char-`p` collapse; (c) a
mathlib-free kernel-checked Lean core with honestly-disclosed debt; (d) the integer-transfer obstruction
stated as a structured, falsifiable account. The Proof Forge's claim is only that it makes the theorem
easier to *express, verify, generalize, and interrogate* than ad-hoc scripts — demonstrated, not that it
discovered anything.

## 9. Next falsification opportunity

- Discharge formalization debt (1)–(3) against a pinned mathlib project and compare `#print axioms`.
- Push the certificate to multivariate / function-field analogues (the ABC theorem for `K[x,y]`,
  Mason's higher-genus version) and see whether the same certificate shape survives — or exposes a new
  obligation.
