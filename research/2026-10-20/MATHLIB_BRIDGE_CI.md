# Mason–Stothers mathlib bridge: pinned CI + axiom-audit receipt (Proof Forge III, Part VII)

**Date:** 2026-10-20. **Lane B (formal-methods / Lean).** **Status: CLASSICAL**
(Stothers 1981; Mason 1984; `Polynomial.abc` is mathlib's, authors Jineon Baek &
Seewoo Lee, 2024). This part adds **no mathematics** — it consolidates the existing
bridge with a *pinned CI gate*, an *axiom-audit receipt* consumed by the Python
proof-authority kernel, and a *separate machine-checked source-mismatch control*.
The bridge's theorems and the derived polynomial Fermat are preserved byte-for-byte.
**RH / integer abc remain OPEN and untouched.**

See `MASON_STOTHERS_MATHLIB_BRIDGE.md` (Part IV) for the mathematics of the bridge
itself (the convention map, the `hW` disjunct-elimination, the `𝔽₂` counter-model).
This document covers only the *consolidation surface*: pinning, the receipt, its
consumer, and the controls.

## 1. The pin (what makes the build reproducible)

Both pins are checked-in files under `formal/mathlib_bridge/`; nothing floats:

| pin | file | value |
|-----|------|-------|
| Lean compiler | `lean-toolchain` | `leanprover/lean4:v4.14.0` |
| mathlib4 revision | `lake-manifest.json` (package `mathlib`) | tag `v4.14.0`, commit `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84` |

`lakefile.toml` requires `mathlib` at `rev = "v4.14.0"`; the manifest freezes the
resolved commit above (and the transitive deps: `batteries`, `aesop`, `Qq`,
`proofwidgets`, `importGraph`, `LeanSearchClient`, `plausible`, `Cli`). `.lake` is
gitignored — only source + manifest are committed. The warm 5.2G olean cache used
for local verification is **not** committed and is reproduced in CI by
`lake exe cache get`.

## 2. The axiom audit (actual `#print axioms`, verbatim)

Captured by a fresh elaboration `lake env lean MasonStothersBridge.lean` (exit 0)
against the pinned toolchain + warm mathlib cache. The four `#print axioms`
commands live at the bottom of the bridge file and print:

```
'SUCC.MasonStothersBridge.succ_mason_stothers_core'    depends on axioms: [propext, Classical.choice, Quot.sound]
'SUCC.MasonStothersBridge.succ_mason_stothers_charZero' depends on axioms: [propext, Classical.choice, Quot.sound]
'SUCC.MasonStothersBridge.control_hW_is_load_bearing'   depends on axioms: [propext, Classical.choice, Quot.sound]
'SUCC.MasonStothersBridge.polynomial_fermat'            depends on axioms: [propext, Classical.choice, Quot.sound]
```

Every result sits inside the envelope **`{propext, Classical.choice, Quot.sound}`** —
the standard mathlib axiom set. This is the mathlib-free core's `{propext,
Quot.sound}` **plus `Classical.choice`**, the disclosed, expected price of importing
mathlib's radical theory (which opens `Classical`). No `sorryAx`. The source file
contains **no** `sorry` / `admit` / `axiom` / `native_decide` / `decide` (grep-clean).
The firewall forbids *faking* choice-freedom, not *using* mathlib.

## 3. The receipt and how Level C consumes it

The receipt is `formal/mathlib_bridge/axiom_audit.json`, written to the exact schema
consumed by `observational_succ/proof_authority.py :: FormalTheorem.validate_against_receipt`
(the trusted-kernel Level C, Part II):

```json
{
  "build_succeeded": true,
  "toolchain": "leanprover/lean4:v4.14.0",
  "manifest_rev": "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84",
  "theorems": {
    "succ_mason_stothers_core":     {"axioms": ["propext", "Classical.choice", "Quot.sound"]},
    "succ_mason_stothers_charZero": {"axioms": ["propext", "Classical.choice", "Quot.sound"]},
    "control_hW_is_load_bearing":   {"axioms": ["propext", "Classical.choice", "Quot.sound"]},
    "polynomial_fermat":            {"axioms": ["propext", "Classical.choice", "Quot.sound"]}
  }
}
```

(The `theorems` keys use the local short names — the namespace `SUCC.MasonStothersBridge.`
stripped — to match the consumer and the `tests/test_proof_authority.py` fixtures.)

`FormalTheorem.validate_against_receipt(receipt)` authenticates a Level C theorem by,
in order:

1. `receipt["build_succeeded"]` must be `True` (a name is not a theorem without a
   successful build);
2. `receipt["toolchain"]` must equal the theorem's pinned toolchain;
3. `receipt["manifest_rev"]` must equal the theorem's pinned mathlib rev;
4. the theorem **name must be present** in `receipt["theorems"]` — a fabricated
   name (e.g. `succ_proves_riemann_hypothesis`) is simply absent and is rejected;
5. every recorded axiom for that theorem must lie within the caller's
   `allowed_axioms` envelope — a `sorryAx` in the receipt fails this.

Thus **authority flows from the recorded build receipt, never from the dataclass
metadata**: a `FormalTheorem` with a made-up name, a wrong toolchain/rev, or an
out-of-envelope axiom cannot discharge a `Claim`. This is the "metadata cannot
elevate itself into mathematical authority" acceptance criterion.

**Integration check (reproduced):**

```
$ cd /home/leah/SUCC-pf3-lean && PYTHONPATH=$PWD python -c "..."
theorems: ['succ_mason_stothers_core', 'succ_mason_stothers_charZero', 'control_hW_is_load_bearing', 'polynomial_fermat']
validates: True
```

All 19 tests in `tests/test_proof_authority.py` pass unchanged.

## 4. The source-mismatch controls

Two independent negative controls guard against a vacuously-passing bridge:

- **In-file `#guard_msgs` coprimality control** (inside `MasonStothersBridge.lean`):
  feeding `Polynomial.abc` a sum hypothesis where an `IsCoprime` argument is expected
  produces a captured `application type mismatch`. The bridge file compiles **iff**
  that elaboration genuinely fails, so dropping a required hypothesis is caught at
  build time. Confirmed by `lake env lean MasonStothersBridge.lean` exiting 0 (the
  expected-error text matched).

- **Standalone `controls/WrongSource.lean`** (new, this part): imports the sound
  bridge and demands a strictly *stronger* (false) degree bound —
  `natDegree A + 2 ≤ deg rad(A*B*C)` instead of the proved
  `natDegree A + 1 ≤ deg rad(A*B*C)`. The kernel refuses the term. This file is
  **not** a `lean_lib` target (the lib glob is the single root module
  `MasonStothersBridge`), so `lake build` never compiles it; it is elaborated on its
  own and a **nonzero exit is the receipt**.

  Observed (verbatim), exit code **1**:

  ```
  $ cd formal/mathlib_bridge && lake env lean controls/WrongSource.lean
  controls/WrongSource.lean:44:2: error: type mismatch
    (succ_mason_stothers_charZero hA hB hC hAB hBC hCA hsum hnc).left
  has type
    A.natDegree + 1 ≤ (radical (A * B * C)).natDegree : Prop
  but is expected to have type
    A.natDegree + 2 ≤ (radical (A * B * C)).natDegree : Prop
  ```

  Were the bridge able to produce the `+2` bound this file would compile, and CI
  would (correctly) flag the control as broken.

## 5. The pinned CI gate

`.github/workflows/mathlib_bridge.yml` is a **single serialized job** (no matrix of
concurrent mathlib builds; a `concurrency` group serializes refs). It:

1. checks out the repo and sets up Python 3.13;
2. installs elan via the official `elan-init.sh`, pinning the compiler from
   `formal/mathlib_bridge/lean-toolchain` (same bootstrap as `eodcs-lean.yml`);
3. runs `lake exe cache get || true` then `lake build` in `formal/mathlib_bridge`;
4. greps the bridge `.lean` and **fails** on any `sorry` / `admit` / `native_decide`;
5. re-derives the `#print axioms` output (`lake env lean MasonStothersBridge.lean`)
   and **fails** if any axiom escapes `{propext, Classical.choice, Quot.sound}`;
6. runs `controls/WrongSource.lean` and **fails if it elaborates** (the control must
   fail);
7. cross-checks the committed `axiom_audit.json` against the live `lean-toolchain` +
   `lake-manifest.json` and then Python-validates it via
   `FormalTheorem.validate_against_receipt`;
8. prints and uploads `axiom_audit.json`.

The workflow is designed to be correct and pinned; it is not required to run in this
lane.

## 6. Two-theorem reuse (realized in Python, not duplicated in Lean)

The Proof-Forge contract is that the trusted kernel discharges **two** independent
theorem families through the *same* `proof_authority` machinery — this is the reuse,
and it lives in `observational_succ/proof_authority.py` + `tests/test_proof_authority.py`:

1. **Mason–Stothers ⟶ polynomial Fermat (Level C / D).** The Lean theorems above are
   consumed as `FormalTheorem`s against this receipt (Level C), and
   `SourceRealization` adds a proved object-identification on top (Level D) via the
   `polynomial_identity` source-map checker. `test_valid_theorem_verified_against_receipt`,
   `test_fake_theorem_name_rejected`, `test_axiom_envelope_enforced`, and the Level D
   tests exercise this family.

2. **Exact Schur-complement theorem ⟶ finite negative-witness / positivity (Level B).**
   The `negative_vector` and `finite_schur_positivity` trusted checkers reuse the
   exact `quantitative_rigidity` Schur kernel on witness-as-DATA: an exact rational
   `v` with `vᵀ M v < 0` certifies non-PSD, and the block diagnostics certify finite
   block positivity `M ⪰ 0` (MATH only — source identification is Level D's job, not
   a caller boolean). `test_negative_vector_certificate_verified` and
   `test_finite_schur_positivity_genuine_vs_trap` (incl. the `diag(1,−1)` trap)
   exercise this family. A finite certificate carries `scope='finite'` and therefore
   **cannot** discharge a `scope='global'` claim (the finite-Gram → global-kernel
   failure control).

Both families route through one `Claim.discharge` discipline (level sufficiency,
scope compatibility, normalization match, then exact re-verification), so the Level C
mathlib bridge and the Level B exact Schur witness share a single authority kernel
rather than two bespoke paths.
