# The Weyl normalization convention (Operation Main XVI, P0 repair)

**Status:** notational/mathematical correction. Fixes a vacuous statement introduced in the
Operation Main XV post-integration handoff. **π base-16/base-3 normality and RH remain OPEN.**

## The error being corrected

The Main XV post-integration handoff defined the *normalized* character average

```
Sbar_N(h) = (1/N) Σ_{n≤N} e(h·U_n(0)),   e(x) = exp(2πi x),
```

and then called `Sbar_N(h) = o(N)` the Weyl/normality condition. **This is mathematically
vacuous.** Every character has modulus 1, so for every orbit whatsoever

```
|Sbar_N(h)| ≤ (1/N) Σ_{n≤N} |e(h·U_n(0))| = 1 = o(N).
```

The bound `|Sbar_N(h)| ≤ 1` holds regardless of normality, so `Sbar_N(h) = o(N)` is satisfied by
**every** sequence, normal or not, and carries no content. The same remark already appears
correctly elsewhere in the tree — e.g. `docs/CLAIM_SUPPLEMENT_SIGNED_PUSHFORWARD_OBSTRUCTION.md`:
*"a modulus bound; normalized it tends to 1; not o(N)"* — so this is a local wording slip, not a
systemic belief.

## The two correct, equivalent statements

Fix the two objects and never again write `o(N)` against the normalized one.

- **Unnormalized Weyl sum** (this is the object the SUCC tree has long written `S_N(h)`):

  ```
  T_N(h) := Σ_{n≤N} e(h·U_n(0)),        |T_N(h)| ≤ N.
  ```

- **Normalized character average:**

  ```
  Sbar_N(h) := T_N(h)/N,                 |Sbar_N(h)| ≤ 1.
  ```

The Weyl equidistribution criterion for base-16 normality of π (via the pinned #293/SGO-09
transport `|T_N(h) − Σ e(h·16^{n-1}π)| < (119/648)|h|`) is, for every fixed integer `h ≠ 0`,

```
┌─────────────────────────────────────────────────────────────┐
│  T_N(h) = o(N)      ⇔      Sbar_N(h) = o(1)      (OPEN)       │
└─────────────────────────────────────────────────────────────┘
```

Both are the *same* open statement. The vacuous one is `Sbar_N(h) = o(N)` (equivalently
`T_N(h) = o(N²)`); it must never be used as the gate.

## Notation reconciliation with the existing tree (do NOT mass-rewrite)

The SUCC tree overwhelmingly writes `S_N(h)` for the **unnormalized** sum `Σ_{n≤N} e(hU_n)`, and
in that convention `S_N(h) = o(N)` is the correct, still-open gate (see
`docs/CLAIM_LEDGER.md:1117`, `CLAIM_SUPPLEMENT_SIGNED_PUSHFORWARD_OBSTRUCTION.md`,
`CLAIM_SUPPLEMENT_SIGNED_GAMMA_BBP.md` SGO-09, DC-1/#304, and the per-supplement `o(N)` rows).
**Those occurrences are valid and are left untouched.** Here `T_N` is that same object under an
unambiguous name, and `Sbar_N` is the normalized average, introduced only so that the normalized
gate reads `o(1)` rather than the vacuous `o(N)`.

Only three sites used the *normalized* average with an `o(N)` gate and are corrected by Main XVI:

| Site | Was | Now |
|---|---|---|
| `research/2026-10-29/main_xv_integration/MAIN_XV_POST_INTEGRATION_HANDOFF.md` | `S_N=(1/N)Σ…`, gate `S_N=o(N)` | `Sbar_N=(1/N)Σ…`, gate `Sbar_N=o(1) ⇔ T_N=o(N)` |
| `research/2026-10-29/main_xv_integration/MAIN_XV_INTEGRATION_RECEIPT.md` (§7) | `(1/N)Σ…=o(N)` | `T_N=o(N)` / `Sbar_N=o(1)` |
| `docs/CLAIM_LEDGER.md` (Main XV firewall paragraph) | `(1/N)Σ…=o(N)` | `T_N=o(N)` / `Sbar_N=o(1)` |

## Regression witness (exact)

`tests/test_triangle_genesis_repair.py::P0NormalizationVacuity`. Take the fully coherent, maximally
**nonnormal** all-zero orbit `U_n ≡ 0` (digit string `0000…`). Then `e(h·U_n) = 1`, so

```
T_N(h) = N,     Sbar_N(h) = 1     for every N and every integer h.
```

- The **vacuous** criterion `Sbar_N(h) = o(N)` is satisfied (`|Sbar_N|/N = 1/N → 0`): it **accepts**
  this nonnormal orbit.
- The **correct** criterion `Sbar_N(h) = o(1)` fails (`|Sbar_N| = 1 ↛ 0`): it **rejects** it, as it
  must.
- The unnormalized form `T_N(h) = N` is not `o(N)`: the canonical repo gate `T_N = o(N)` likewise
  rejects it.

The source-authentic coherent counterexample is the counterseed `s* = −π/16` of TG-08
(`U_n(s*) = −T_n → 0`, selected phase `→ 1`, nonnormal): it too satisfies the vacuous `o(N)` and
violates the correct `o(1)`. See `SEED_ALIAS_CLASSIFICATION.md`.

## Scope

This is purely a correction of the equidistribution *normalization*. It does not prove, weaken, or
strengthen any cancellation claim. `T_N(h) = o(N)` (equivalently `Sbar_N(h) = o(1)`) for every
fixed `h ≠ 0` is base-16 normality of π and remains **OPEN**.
