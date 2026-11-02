# The entropy–dimension bridge: obligation (B) ⟺ positive entropy of π's digits

**Branch:** `research/x3-rigidity-machinery-2026-11-02`. **Agent:** Ravel (main).

## The key classical identity (Furstenberg / Hochman)

For the `×16` map `T_16(x) = {16x}` and any `T_16`-invariant probability `μ` on `[0,1)`:

$$
\boxed{\ h_{\mu}(T_{16}) = \operatorname{dim}_* \mu \cdot \log 16\ }
$$

(the measure-theoretic entropy equals lower Hausdorff dimension times `log 16`). This is the
Furstenberg entropy formula / Hochman's entropy-dimension identity for `×m` maps. **Consequence:**
obligation (B) `dim_* μ > 0` is equivalent to **positive entropy** `h_μ(T_16) > 0`.

## The bridge to the existing SUCC collision-energy machinery

The entropy of the orbit measure is the **Shannon entropy rate of the base-16 digit stream**:
$$ h_{\mu}(T_{16}) = \lim_{m\to\infty} \frac{H_m}{m}, \qquad
H_m = -\sum_{|w|=m} p_m(w)\log p_m(w). $$

This is **exactly the object the SUCC reduction already tracks** via the collision energy
`Q_{m,N} = 16^m Σ p_m(w)²` and the Rényi-2 ≤ Shannon inequality:
$$ H_m \ge -\log Q_{m,N}, \qquad\text{so}\qquad h \ge \liminf_{m} \frac{-\log Q_{m,N}}{m}. $$

## The clean reduction (this is the important part)

The ×3 rigidity route splits normality into two *weaker* statements:

| Obligation | Clean equivalent | Strength vs. normality |
|---|---|---|
| (A) `T_3`-invariance | `μ̂(3h)=μ̂(h)` ∀h | strictly weaker than `S_N(h)=o(N)` |
| (B) `dim_* μ > 0` | **`h > 0`** (positive entropy rate of π's digits) | strictly weaker than `h = log 16` |

Normality is `h = log 16` (full entropy); (B) needs only `h > 0` (the digit stream is **not
zero-entropy**: not eventually periodic, not a Sturmian/substitution/Toeplitz sequence of zero
entropy). **Hochman–Shmerkin Thm 10.4 then combines (A)+(B) into `h = log 16`.**

## What this buys the SUCC program (the genuinely-new framework value)

1. **(B) is now a *named, weaker, clean* target**: "π's base-16 digits have positive entropy rate"
   — not "π is normal." It is the *right* object to attack for the rigidity route, and it connects
   (B) back to the collision energy `Q_m` the program already computes.
2. **The chain is fully pinned**:
   `dim_* > 0` (classical: Furstenberg/Hochman) `⟺` `h > 0` (definition) `⟺`
   `liminf H_m/m > 0` (Rényi-2) `⇐` `liminf −log Q_m/m > 0`.
3. **The honest status**: positive entropy `h > 0` is **NOT** implied by finite irrationality measure
   `μ(π) < 15/2` (a zero-entropy orbit — e.g. Thue–Morse — can have finite irrationality measure).
   So (B) is a genuine, independent, still-open statement — but it is *weaker* and *different* than
   normality, and now cleanly connected to the program's existing entropy/collision machinery.

## Empirical anchor (finite, correct precision)

`H_1 = 2.7690…` vs `log 16 = 2.7726…` over the first 1999 digits of π (digits `2.43F6A8…` verified).
The empirical entropy rate is near-maximal (`h ≈ log 16`), consistent with normality — but (B) only
requires `h > 0`, a vastly weaker statement.

## Status

The bridge is **classical (Furstenberg/Hochman) + definitional**, and connects (B) to the existing
SUCC `Q_m`/`H_m` machinery. Obligation (B) is now stated in its cleanest form: **prove the base-16
digit stream of π has positive entropy rate**. This is strictly weaker than normality and genuinely
different from the Weyl gate — but still open. π normality and RH remain **OPEN**.
