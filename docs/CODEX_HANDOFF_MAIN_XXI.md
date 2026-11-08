# Research-branch handoff after Main XXI (2026-11-07)

This note is for any agent or researcher who opens a research branch off `main` after Main
XXI, including the parallel Codex research line. Main integration and the canonical docs
are maintained separately. **New research belongs on its own branch and draft PR. It is
audited as a fresh submission, and nothing is promoted automatically.**

**π base-16 normality: OPEN. Selected signed Weyl gate `S_N(h)=o(N)`: OPEN. RH: OPEN.**

## 1. Rebase point

Start from the `main` merge commit of Main XXI, which is recorded in
[`SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07.md`](SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07.md).
All of #525–#543 are in that ancestry, so do not re-import them. The frozen source and its
provenance did not change in Main XXI:

- `provenance/IMPORT_MANIFEST.json` blob `a8805a8e…`;
- the `formal/`+`provenance/` tree hash `82c6cf9f…`;
- `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_{n-1}+r(n)`.

## 2. Import these instead of re-implementing

A Main XXI census executed the duplicates of each item below against the canonical API.
Every one was value-identical, with exact `Fraction` arithmetic and `U_0=0`.

| Need | Canonical API |
|---|---|
| Four-pole forcing, lifted/forced orbit (Lean-backed tail) | `observational_succ.duck_bbp`: `forcing`, `lifted_orbit`, `forced_orbit`, `tail_interval` |
| Integer engine with literal carries `(16·rem+c)//q` | `observational_succ.integer_bbp_carrier`: `forcing_pair`, `step`, `source_states` |
| Seeded, reduced selected orbit; `c_A(h)` at scoped precision; receipt writer with sha256 dependencies | `observational_succ.selected_orbit`: `SelectedOrbit`, `weyl_coefficient`, `write_receipt`, `sha256_file` |
| 2-adic zero boundary, isometry, odometer | `observational_succ.bbp_binwindow_conjugacy`, `observational_succ.bbp_two_adic` (since 2026-10-27; #527 rederived it) |
| Prime births (first-pole denominators) | `observational_succ.bbp_cyclotomic_birth.birth_index` |
| Exact cyclotomic DFT | `observational_succ.finite_fourier_carrier`: `CyclotomicElement`, `exact_dft` |
| Pin-bed surfaces (new in XXI) | `fourier_yoneda_pinbed` (#541), `driven_pinbed_observer` (#543), `learning_pinbed` and `pinbed_oscillator_bridge` (#542) |

These look alike but are **different objects**:

- `selected_orbit.carry_by_definition` is the #522 critical-carry bit, not the integer
  carry.
- `gamma_bbp_signed_coherence.green_tail_interval` is strictly tighter than
  `duck_bbp.tail_interval`.
- `pinbed_oscillator_bridge.four_pole` is a deliberately independent oracle. Do not "fix"
  it into an import.

## 3. Pin-bed conventions: they do not compose verbatim

| PR | Formalism | Convention |
|---|---|---|
| #541 | Bernoulli `B₂` continuous surfaces; inverse `μ=λ−½D²F` | surface multipliers `m_h/(2π²h²)` |
| #543 | driven forward-window observer; first-order inverse `𝒜_α` | **forward** windows. `C₁₆(½)=341/√205` for **real** laws only; the complex norm is `31`. "`h=2` wins" holds at `b=16` only. |
| #542 | finite two-tone windows `R_{L,k}` plus continuous surfaces | finite windows are forward. Continuous surfaces are **backward** convolutions `g*μ` with `G_a(r)=conj(a_r)`. |

#543's inverse and coherence relation `a_h f̂₁=a_{h−1}f̂₀` apply to #542's continuous
surfaces **only after complex conjugation**. Symbols also collide inside #543: `A_α`,
`C_b(α)` vs `C_α(d)`, and `a_h` as a scalar vs a vector.

## 4. Known hazards on main

- **Global mpmath precision.**
  - 15 library modules assign `mp.mp.dps` without restoring it. The largest offenders are
    `prime_form_heat` (23 sites), `completed_weil_transport` (11), and the `black_sun_*`
    family. Test files add 95 more assignments in 43 files.
  - Use `mp.workdps` in new code, and never trust ambient precision in a test.
  - `prime_form_heat` is **not** fixed. Its pinned receipt
    `research/2026-10-14/PRIME_FORM_HEAT_RECEIPT.json` and six tests depend on the leak, so
    the repair needs a dedicated round with receipt regeneration under provenance.
  - `gram_mobius` *was* fixed in Main XXI: it no longer sets precision at import, and its
    values are bit-identical.
- **`research/2026-11-06/holographic_triangle/independent_run.sh`.** Do not run it. It
  calls a `receipt.py` that never existed and, under `set -eu`, truncates the tracked
  `FINITE_RECEIPT.json`.
- **cwd-relative opens.** `joint_character_entropy/fresh_holdout_probe.py:17` must be run
  from its own directory.
- **Hand-edited result JSONs.** Several tracked `FINITE_RESULTS`-style JSONs carry
  hand-written keys that no script emits: `spectral_exorcism`, the Galois selector, and
  `critical_collision` `HOLDOUT_N4096`. The numbers agree on the shared keys. New receipts
  should be byte-reproducible from a documented command.

## 5. Test discipline that Main XXI enforced

- **A bound must be tested against an independently computed true quantity at its tightest
  point,** not against its own formula. In XXI, five wrong pin-bed implementations passed
  the original tests until `tests/test_main_xxi_pinbed_hardening.py` was added.
- **REFUTED needs a demonstrated countermodel.** A failed proof route goes under
  `UNVERIFIED` with its wall named. See `docs/METHOD.md` and Main XXI receipt R1.
- **A proposed proof of any open gate must fail on all three hostile controls:**
  - the coherent counterseed `s_*=−π/16`;
  - the CB-3 same-forcing seeds;
  - the GA-09 arc grid (`research/2026-11-07/main_xxi_receipts/`).

## 6. The open target

See [`PI_NORMALITY_FRONTIER.md`](PI_NORMALITY_FRONTIER.md) §3 and §6. The sufficient scalar
targets are equivalent or conditional routes to the same open gate:

- (LS) or (H2\*);
- `C^x_{A,A}=o(\log A)`;
- `E_a(μ_A^x)→0`.

Main XXI added **transport**, not decay: the zero-seed orbit and `\{16^{n-1}π\}` are
interchangeable at cost `O(A^{-1/2})` (√ critical Fejér) or `O(A^{-2})` (golden energy).
What is missing is one **source-selected decay estimate**.

## 7. Registering new claims

Add a `docs/CLAIM_SUPPLEMENT_<NAME>.md` table and register its namespace in
`docs/CLAIM_NAMESPACE_REGISTRY.json`. A bare prefix that merely *starts like* an existing
one is a separate namespace (`MXXI` vs `MXX`). Then regenerate the catalog **last** with
`python scripts/build_math_memory.py --write`, and check with `--check`.
