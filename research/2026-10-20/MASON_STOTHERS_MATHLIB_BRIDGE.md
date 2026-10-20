# Mason–Stothers formal transport bridge (Deliverable C, Part IV)

**Date:** 2026-10-20. **Status: CLASSICAL** (Stothers 1981; Mason 1984;
`Polynomial.abc` is mathlib's, authors Jineon Baek & Seewoo Lee, 2024). The
contribution is strictly the **transport bridge**, the convention reconciliation, and
the controls — no new mathematics. **RH / integer abc remain OPEN and untouched.**

**File:** `formal/mathlib_bridge/MasonStothersBridge.lean` (+ `lakefile.toml`,
`lean-toolchain`, `lake-manifest.json`, `.gitignore`). The existing mathlib-free
`formal/MasonStothersDegreeDescent.lean` core (axioms `{propext, Quot.sound}`) is
**left intact and unmodified**.

## What the bridge does
It does **not** re-prove Mason–Stothers. It imports mathlib4's already-formalized
`Polynomial.abc` and **discharges the SUCC Proof-Forge certificate's claim** with it,
reconciling the two conventions exactly. Four kernel-checked results:

1. `radical_neg_prod` — `radical(A·B·(−C)) = radical(A·B·C)` (the `−1` unit).
2. `succ_mason_stothers_core` — SUCC `A+B=C`, nonzero, pairwise coprime, with the
   char hypothesis entering as `hW` (not all three derivatives vanish), discharged by
   `Polynomial.abc` after the `c := −C` sign change and elimination of mathlib's
   derivative-zero disjunct via `hW`.
3. `succ_mason_stothers_charZero` — char-0 corollary: discharges `hW` from
   `[CharZero k]` + non-constancy via `natDegree_eq_zero_of_derivative_eq_zero`
   (faithfully SUCC §3's nonvanishing of `W`).
4. `polynomial_fermat` — classical polynomial Fermat (char 0, `n ≥ 3`) **derived**
   from the bridge (mathlib v4.14.0 has **no** polynomial FLT — only a `TODO` — so this
   is a genuine derivation, not a citation).

## Convention map (SUCC ⟶ mathlib), recovered exactly
mathlib `Polynomial.abc` (tag v4.14.0, verbatim `#check`):
`{a b c : k[X]}`, `[Field k] [DecidableEq k]`, `a≠0,b≠0,c≠0`, `IsCoprime a b`,
`IsCoprime b c`, `IsCoprime c a`, `a+b+c=0` ⟹
`(natDegree a + 1 ≤ (radical (a*b*c)).natDegree ∧ … ) ∨ (derivative a = 0 ∧ … )`.

| item | SUCC | mathlib | reconciliation |
|------|------|---------|----------------|
| field | field `K` | `[Field k] [DecidableEq k]` | identical |
| sum | `A + B = C` | `a + b + c = 0` | `c := −C`; `A+B+(−C)=0` proved |
| nonzero | `A,B,C ≠ 0` | `a,b,c ≠ 0` | `−C ≠ 0` via `neg_ne_zero` |
| coprimality | pairwise | three `IsCoprime` | `IsCoprime.neg_right/neg_left` |
| radical | distinct monic irreducibles | `UFM.radical` (associate-invariant) | `radical_neg_prod` |
| degree bound | `max deg ≤ deg rad − 1` | `natDegree + 1 ≤ (radical).natDegree` | identical over ℤ; `+1` form avoids ℕ truncation |
| char hypothesis | `char 0` / `char > deg` ⇒ `W ≠ 0` | **none**; emits derivative-zero disjunct | SUCC's hypothesis is *precisely* what rules out mathlib's right disjunct — the heart of the bridge |

**Key structural finding.** mathlib carries **no** characteristic hypothesis; it
instead emits the Wronskian-collapse (`derivative a = b = c = 0`) as a second
disjunct. So the SUCC `char 0 / char > deg / W ≠ 0` hypothesis is *exactly* the
condition that eliminates mathlib's right disjunct. The bridge makes that
correspondence explicit and proved.

## Controls (the contract is genuinely discharged, not asserted)
- `control_hW_is_load_bearing` — a **proven** counter-model over `𝔽₂`:
  `A=X², B=1, C=X²+1` satisfies every other hypothesis (nonzero, pairwise coprime via
  explicit Bézout, `A+B=C`) yet all derivatives vanish (char-2 freshman's dream), so it
  lands in mathlib's right disjunct and the degree bound (`3 ≤ 2`) is false. `hW` is
  therefore load-bearing (SUCC §6).
- `#guard_msgs` coprimality control — a **machine-checked typecheck failure**: feeding
  `Polynomial.abc` a sum hypothesis where coprimality is expected yields a captured
  `application type mismatch`. The file compiles **iff** that elaboration genuinely
  fails, so it is a real source-mismatch control, not a comment.

## Axiom audit (honest)
`#print axioms` on all four results: **`{propext, Classical.choice, Quot.sound}`**.
This is the mathlib-free core's `{propext, Quot.sound}` **plus `Classical.choice`** —
the disclosed, expected price of importing mathlib (whose radical theory opens
`Classical`). The firewall forbids *faking* choice-freedom, not *using* mathlib; the
contrast with the standalone core is the documented cost of the transport.

## Build / reproduce
Toolchain `leanprover/lean4:v4.14.0`; mathlib pinned to tag `v4.14.0`
(`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`). From `formal/mathlib_bridge/`:
`lake update` (pulls the prebuilt cache via mathlib's post-update hook, 4904 files)
then `lake build MasonStothersBridge`. `.lake` is gitignored; only the source +
manifest are committed. Network required for the one-time cache fetch.

**Agent build receipt:** cache "Completed successfully"; `lake build` →
`Built MasonStothersBridge`, exit 0; no `sorry`/`admit`/`axiom`/`native_decide`/`decide`
in the file. **Coordinator independent rebuild:** see `PART_XI_COORDINATOR_REPORT.md`
for the re-run exit status and axiom print.
