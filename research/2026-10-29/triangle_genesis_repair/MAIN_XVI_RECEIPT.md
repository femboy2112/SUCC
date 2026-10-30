# Operation Main XVI — Triangle Genesis repair & advance: integration receipt

**Date:** 2026-10-29 (New York). **Status:** repair of three Main XV inconsistencies + one new
obstruction, integrated to `main` through a reviewed PR. No publish, tag, release, force-push,
archive rewrite, frozen-source change, or branch deletion. No mathematical status promoted.
**π base-16/base-3 normality and RH remain OPEN.**

## 1. Before / after

| | SHA |
|---|---|
| `main` before | `27d5ae78d52551bdf982e5f206d853d1b25624a8` (Operation Main XV) |
| Branch | `integration/succ-main-xvi-triangle-repair-2026-10-29` (from `origin/main`) |
| `main` after merge | _recorded on the PR after the authorized merge_ |

The push-to-main "Observational SUCC validation" run for Main XV completed **success** (confirmed),
so the Main XVI baseline is a fully-green `main`.

## 2. What changed and why (the four deliverables)

**P0 — Weyl normalization (correction).** The Main XV handoff/receipt and one CLAIM_LEDGER line
wrote the *normalized* average `Sbar_N(h)=(1/N)Σ e(hU_n(0))` with an `o(N)` gate. Since
`|Sbar_N|≤1`, `Sbar_N=o(N)` is vacuous (every orbit satisfies it). Corrected to the two equivalent
non-vacuous forms `T_N(h)=Σ e(hU_n(0))=o(N)` ⇔ `Sbar_N(h)=o(1)`, with a convention note
(`WEYL_NORMALIZATION_CONVENTION.md`). **The repo's dominant `S_N(h)=Σe(hU_n)=o(N)` usage is the
unnormalized sum and is correct; it was left untouched** (directive rule). Only three normalized
`(1/N)…=o(N)` sites were fixed: the Main XV handoff, the Main XV receipt §7, and
`docs/CLAIM_LEDGER.md` Main XV firewall paragraph. Regression witness: the coherent all-zero orbit
passes the vacuous `Sbar_N=o(N)` yet is nonnormal and fails `Sbar_N=o(1)`.

**P1 — golden locus (TG-11, PROVED).** Replaced the false global-uniqueness statement ("D_λ and
D_self agree only at `(2,1)`") with the proved locus
`q_{r,θ}=λ^r ⇔ θ=λ/(1−λ^r)` (`r>0`), supercritical on the whole curve, Laplace rate
`θ(1−q)=λ` constant, calibration `(1,φ,λ),(2,1,λ²),(3,φ/2,λ³)`, and the **restricted uniqueness**
`θ=1 ⇒ r=2` (so the authentic BBP point `(2,1)` stays distinguished as the unique intersection of
its clock slice with the locus). `GOLDEN_LOCUS_THEOREM.md`; symbolic + independent root-isolation
checks for `r=1..6`.

**P2 — seed-alias dichotomy (TG-12, PROVED).** From the affine law `U_n(s)=U_n(0)+16^n s`, a
seven-class classification of seed distinguishability (unwrapped / exact alias `s∈(1/16)ℤ` /
eventual alias `s∈ℤ[1/16]` / constant twist `q|15` magnitude-invariant / absolute-phase vs
magnitude / integer carry / coherent `s*=−π/16`). Corrected the Main XV control slate: a candidate
estimate is required to FAIL only on seeds its own observable can separate (`s*`, periodic twists
`q∤15`, source mutants), **not** on magnitude-/phase-aliased rational seeds — demanding the latter
would force a valid theorem to contradict itself. `SEED_ALIAS_CLASSIFICATION.md`.

**P3 — carry obstruction (TG-13, PROVED negative).** The literal carry `κ_n(s)` separates
circle-aliased seeds but carries no bound on `|T_N(h)|`; no noncentral/carry/absolute-phase
enrichment is simultaneously a magnitude bound and an alias separator. Explicit limitation:
this does **not** produce the missing signed cancellation. `SEED_ALIAS_CLASSIFICATION.md`.

## 3. Files

New (`research/2026-10-29/triangle_genesis_repair/`): `WEYL_NORMALIZATION_CONVENTION.md`,
`GOLDEN_LOCUS_THEOREM.md`, `SEED_ALIAS_CLASSIFICATION.md`, `golden_locus.py`, `seed_alias.py`,
`independent_oracle_xvi.py`, `MAIN_XVI_HANDOFF.md`, `MAIN_XVI_RECEIPT.md`; new top-level regression
`tests/test_triangle_genesis_repair.py`.

Surgical edits (additive / correction only): `docs/OPERATIONAL_TRIANGLE.md` (TG-09 locus fix + Weyl
convention + status rows + refs), `docs/CLAIM_LEDGER.md` (vacuity fix + TG-09/11 + Main XVI block),
`docs/ROADMAP.md`, `docs/math_memory/INDEX.md`, the two Main XV dossiers (P0 sites + control row),
and the three frontier dossiers (`THEOREMS.md`, `CLAIMS.md`, `ORIGINAL_TRIANGLE_PROVENANCE.md`,
locus). **No frozen BBP source, `provenance/IMPORT_MANIFEST.json`, `ci.yml`, or workflow changed;
`U_0=0` and the four signed poles unchanged.**

## 4. Validation (local, on the integration candidate)

| Gate | Result |
|---|---|
| `tests/test_triangle_genesis_repair.py` (new, P0–P3 + oracle cross-check) | **22 passed** (unittest discover) |
| Independent oracle `independent_oracle_xvi.py` (substitution/polyroots + modular + mpmath) | all agree: golden locus r=1..6, alias classes, counterseed collapse |
| Frontier `test_operational_triangle.py` (unchanged code) | **10 passed** (no regression) |
| `verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, source_commit `ba075348`, rc=0 |
| `observer_foundations_probe.py` / `ordinal_succ_report_probe.py` | rc=0 (firewall flags unchanged) |
| `verify_math_memory_graph.py` | PASS, 51 nodes / 60 edges, rc=0 |
| `build_math_memory.py --check` | _regenerated LAST; rc recorded below_ |
| Full root suite `unittest discover -s tests -p 'test_*.py'` (normal env) | **Ran 10008 tests; 1 error** = the pre-existing environment-only artifact `test_eodcs_meta_choice_descent` (subprocess `python scripts/meta_choice_descent_probe.py` puts `scripts/` on `sys.path[0]` → `ModuleNotFoundError: observational_succ`); both files **unchanged** by Main XVI, bare-subprocess failure reproduced, and `PYTHONPATH=<repo>` (CI's `pip install -e`) → probe rc=0. 10007 native pass. **Do NOT run the suite under `python -I`** — isolated mode excludes the user/editable `observational_succ` and spuriously fails ~168 import-only modules. |
| Independent adversarial audit (blind d'Alembert, exact sympy/mpmath/ℚ) | **all four claims SURVIVED; FIREWALL INTACT** — no refutation, no firewall overstep. Three low-severity tightenings applied below |
| Frozen BBP sources / `ci.yml` / workflows vs `main` | byte-identical; nothing changed |

**Audit tightenings applied (no defects; all SURVIVED).** A blind adversarial pass re-derived every
claim from scratch and confirmed P0/P1/P2/P3 with firewall intact. Three cosmetic/rigor
reinforcements it suggested were folded in: (1) P3 — scoped the universal "no observable is both a
magnitude bound and an alias separator" to functionals *determined by* `{|T_N(h)|}` (a trivial
`(magnitudes, carry)` bundle contains both but is not a `|T_N|` bound; its separating power lives in
the carry, which gives no saving); (2) P2 — stated the `n ≥ 1` summation convention explicitly (the
class-2/3 magnitude-invariance excludes the `U_0` seed term; an `n = 0`-inclusive sum would differ
and must not be mistaken for a separation); (3) P1 — made the `⇒` direction self-contained (strictly
convex PGF with `μ ≤ 1` has `G(z) > z` on `[0,1)`, so an interior fixed point forces `μ > 1`). The
audit explicitly did not re-audit the pinned #293/SGO-09 transport constant (out of scope).

_(The §4 "recorded below" rows and the final `main` SHA are filled from the actual suite run, the
catalog regeneration, and the hosted CI on the exact PR head.)_

## 5. Mathematical status (unchanged; no promotion)

TG-11 golden locus: PROVED (classical Galton–Watson/Gamma). TG-12 seed-alias dichotomy: PROVED
(exact ℚ + mpmath). TG-13 carry obstruction: PROVED negative. P0: notational correction. π
base-16/base-3 normality, RH, the signed gate `T_N(h)=o(N)` (`Sbar_N(h)=o(1)`), general Collatz,
and shifted Lonely Runner n=18..94 all remain **OPEN**. Main XVI promotes no mathematical status and
supplies no signed cancellation.
