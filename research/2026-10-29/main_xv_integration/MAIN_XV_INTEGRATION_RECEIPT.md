# Operation Main XV — Triangle Genesis integration receipt

**Date:** 2026-10-29 (New York). **Status:** research-status integration of the live Triangle
Genesis frontier, the corrective prime-ladder firewall, and the order-statistic bridge onto a
fresh branch from live `main`. No mathematical status promotion. No publish, tag, release,
force-push, archive rewrite, or branch deletion performed. **π base-16/base-3 normality and RH
remain OPEN.**

## 1. Before / after

| | SHA |
| --- | --- |
| `main` before integration | `ac7303b2e0e2ec16e3b1d88d186324e1fae65ea5` (Main XIV + merged Oily name provenance #365) |
| Integration branch | `integration/succ-main-xv-triangle-genesis-2026-10-29` (from `origin/main`) |
| `main` after merge | _recorded after the authorized merge; see the post-integration handoff_ |

Tree delta vs `main`: **310 files changed, +35112 / −1** (the single deletion is a research-local
receipt line inside the recursive-carrier dir, carried by the #367 spine). All top-level docs are
additive; the one edit to an existing research doc is the R4/R5 correction banner (see §4).

## 2. Branch inclusion matrix (ancestry verified by `git merge-base`, not PR titles)

All 22 Triangle branches (#366–#387) share merge-base `ec2fbe32` with `main` (i.e. they forked
before the #365 naming-provenance commit; building from current `main` preserves that ledger).
Six ancestry-minimal leaves cover all 22:

| Leaf | Head | Subsumes (confirmed git ancestors) | Decision |
| --- | --- | --- | --- |
| **#378** inertial-relative-observer-gamma-memory | `3c3bda31` | #367, #369, #370, #371, #375 | INTEGRATED (`--no-ff`) |
| **#384** kepler-iii-selected-phase-shrinking-target | `85797027` | #367, #369, #370, #372, #374, #376, #377, #380, #382 | INTEGRATED (`--no-ff`) |
| **#385** minimal-pole-fermat-gamma-bridge | `5092dc70` | #367, #373, #379, #381, #383 | INTEGRATED (`--no-ff`) |
| **#387** operational-triangle-kernel-tomography | `9c245420` | #367, #373, #379, #381, #383, #386 | INTEGRATED (`--no-ff`); flagship |
| **#366** oily-stoneham-pathsheet | `b51e6a89` | (independent, main-based) | INTEGRATED (`--no-ff`) |
| **#368** oily-order-statistic-golden-sheet | `ee2ccc87` | (independent, main-based) | INTEGRATED (`--no-ff`) |

`#387` is **not** an ancestor of `#385` and vice versa (siblings off #383): both integrated.
The intermediate PRs #367/#369/#370/#371/#372/#373/#374/#375/#376/#377/#379/#380/#381/#382/#383/#386
are **integrated by inclusion** (their commits are reconstructed by the `--no-ff` merges of the
leaves above; no parent was re-applied as a fresh patch).

Corrective prime-ladder line (forked ~231 commits back; all changes purely additive, no path
collisions with `main`):

| Leaf | Head | Content | Decision |
| --- | --- | --- | --- |
| **#337** furstenberg-kempner-firewall | `0e36f9c5` | prime-ladder base (reduction theorem, all-prime rigidity, universal ×3 defect, anti-normal conjecture) **+ Kempner refutation + transverse-invariance disproof + top-level test** | INTEGRATED (`--no-ff`) |
| **#334** prime-ladder-ravel-audit | `809504e1` | Z2 / dyadic / {2,3} solenoid finite↔global atoms (+ standalone Lean `formal/Z2FiniteCharacterAtom.lean`), infinite-dimensionality theorem, 3-adic memory theorem, Weyl-route toolkit, indistinguishable-criterion note, Oily constant-registry research notes | INTEGRATED (`--no-ff`); **R4/R5 corrected** (§4) |

Order-statistic bridge:

| PR | Head | Content | Decision |
| --- | --- | --- | --- |
| **#359** max-root-polya-observer-bridge | `3a4f7e13` | MAX/ROOT order-statistic observer transport, bounded selection, off-axis controls (1 unique commit over the Main-XIV-integrated #356 base) | INTEGRATED (single `cherry-pick -x`; fully additive, no collisions) |

**Lean honesty note.** `formal/Z2FiniteCharacterAtom.lean` (from #334) is a standalone,
Mathlib-free Lean file with **no CI target and no `scripts/check_*_lean.py` binding**: the hosted
Lean workflows are each path-triggered on their own named files (`duck-pi-proof.yml`,
`duck-principle-lean.yml`, `no-ghost.yml`, `institute.yml`, …) and none globs `formal/*.lean` or
references this file. It therefore does **not** break CI and is **not** claimed kernel-checked
here; it is retained as additive research. A reader who wants it verified must add a check binding
and build it.

### Excluded / not resurrected

- No closed-without-merge experimental branch was resurrected merely to satisfy "all branches".
- The DeepSeek effective-density branch quarantined in Main XIV stays excluded; its REFUTED record
  is unchanged.
- No historical theorem ID, frozen BBP source (`formal/duck_pi/BBPSourceGenesis.lean`,
  `BBPIntegral.lean`, `observational_succ/bbp_minimal_path.py`, `integer_bbp_carrier.py`),
  `provenance/IMPORT_MANIFEST.json`, or `U_0=0` seed was touched.

## 3. Conflict surface

The six Triangle leaves conflicted on **nothing** that required manual resolution except the
math-memory catalog, which is regenerated from the final tree (`build_math_memory.py --write`,
the Main XIV discipline), not resolved ours/theirs. No leaf touches `ci.yml`, workflows,
`IMPORT_MANIFEST`, the frozen BBP Lean/Python sources, or the top-level
`FOUNDATIONS/ARCHITECTURE/ROADMAP/CLAIM_LEDGER` (those receive only the additive pointers in §4).
The ancient #334/#337/#359 branches are purely additive new files with **zero** path collisions
against current `main`.

## 4. Editorial changes made during integration (additive, honest-record)

- **R4/R5 correction banner** added to
  `research/2026-10-27-ravel-prime-ladder/PRIME_LADDER_REDUCTION_THEOREM.md`: the "π transcendental
  ⟹ positive topological entropy ⟹ normality bridge" (R4, previously labelled *PROVED classical*)
  is marked **REFUTED as a general bridge / UNVERIFIED for π**, cross-linked to the Kempner firewall
  (`research/2026-10-27-furstenberg-kempner/KEMPNER_FURSTENBERG_FIREWALL.md`, FK-1/FK-2/FK-5). This
  satisfies the known-conflict requirement to reword the inherited affirmative theorem while
  preserving the refuted-claim record.
- New apparatus interface `docs/OPERATIONAL_TRIANGLE.md` (Mission II/III).
- Additive pointers into `docs/ARCHITECTURE.md`, `docs/FOUNDATIONS.md`, `docs/ROADMAP.md`,
  `docs/CLAIM_LEDGER.md` (TG-01–TG-10 + REFUTED entries), `docs/math_memory/INDEX.md`.
- The author's original triangle and Oily–Macaroni provenance (PR #365 ledger) are preserved
  verbatim and characterized as the rank-two specialization; nothing deleted or renamed away.
- Two faithful tightenings to `operational_triangle_frontier/THEOREMS.md` TG-05, prompted by the
  independent audit (not defects): the `-59/(320n)` sentence now states the `(1-F)` sign flip
  explicitly (the bare integral is `+59/320`), and the uniform-remainder paragraph now states
  `d=2+t-z>=1` on the rectangle (minimum at `z=1,t=0`, so no small-`d` blow-up), names `P(y)` as a
  fixed polynomial with `P(y)e^{-y}` integrable, and notes `C_T` depends on `T` only through
  `e^{-ty}`. No claim changed.

## 5. Validation (local, on the integration candidate)

| Gate | Result |
| --- | --- |
| Frontier `test_operational_triangle.py` (#387) | **10 passed** |
| Frontier `independent_oracle.py` (#387 symbolic/numeric) | runs; `scaled_error → 0` (O(1/n²) after the 1/n jet), `source_defect_inferred → predicted` |
| 10 new top-level integration tests | **203 passed, 37 subtests passed** |
| `verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, 72 items, `establishes_mathematical_truth: false`, rc=0 |
| `observer_foundations_probe.py` / `ordinal_succ_report_probe.py` | exit 0 (firewall flags `false`) |
| `verify_math_memory_graph.py` | PASS: 51 typed nodes, 60 typed edges |
| `build_math_memory.py --check` | exit 0 (regenerated last; retained research-supplement warnings by design) |
| Frozen BBP sources / `ci.yml` / workflows vs `main` | byte-identical; no workflow changed |
| Independent re-derivation of TG-05 59-jet (my own exact R-sum + Richardson) | matches `J_BBP` at 7 generic `(z,t)` + exact `J(0,0)=-151/960` and `z=1` reduction |
| Independent adversarial audit (blind, exact symbolic/bit computation) | **FIREWALL INTACT — SURVIVED**; no defect, no status breach; one cosmetic sign nit (fixed above) + remainder-paragraph reinforcement (applied) |
| Full root suite (`unittest discover -s tests -p 'test_*.py'`) | **Ran 9986 tests**, 1 error — the pre-existing environment-only artifact `test_eodcs_meta_choice_descent.test_exact_probe_receipt_and_independent_count` (see §6). 9985 native pass. |

## 6. Root gates and catalog — recorded after the final doc commit

The mathematical memory catalog is regenerated **after** every doc (including this receipt and the
handoff) per the Main XIV lesson; `build_math_memory.py --check` exits 0.

**The single root-suite error is a pre-existing environment artifact, not an integration
regression — reproduced on pristine `origin/main`.** `tests/test_eodcs_meta_choice_descent.py`
(and `scripts/meta_choice_descent_probe.py`) are **unchanged** by this integration. The test
spawns `python scripts/meta_choice_descent_probe.py`; run that way, `sys.path[0]` is `scripts/`,
not the repo root, so the subprocess raises `ModuleNotFoundError: No module named
'observational_succ'`. It fails identically in a throwaway worktree checked out at pristine
`origin/main` (`ac7303b2`), and with the repo root importable (`PYTHONPATH=<repo>`, exactly what
CI's `pip install -e '.[test]'` provides) the probe exits 0 with its expected receipt
(`EXACT_FINITE_SOURCE_CONTRACT_NOT_GLOBAL_THEOREM`, `source_provenance_authenticated: false`) and
the module passes 11/11. The hosted CI matrix on the exact merged HEAD is the authoritative
full-suite gate.

Hosted-CI status at the exact proposed integration commit is recorded on the draft PR after push.

## 7. Mathematical status (unchanged; no promotion)

- Operational-triangle finite laws (TG-01/03): PROVED LOCAL. Sufficiency (TG-02): CLASSICAL,
  non-universal. Gamma–Poisson emergence (TG-04): CLASSICAL under regularity. Oily–Macaroni
  `Omega_OM = lambda - gamma` at `(r,theta)=(2,1)` (TG-05/09): CLASSICAL analysis + declared
  observers, original-triangle SPECIALIZATION. Two-variable 59-jet (TG-05): PROVED LOCAL,
  independently re-derived. Seed-resolved tomography + universal seed-smearing zero
  (TG-06/07/08): PROVED LOCAL representation, NOT a Weyl estimate.
- "Operational triangle certifies π normality / RH" (TG-10): **REFUTED as an implication**.
- Prime-ladder R4/R5 transcendence→entropy bridge (#334): **REFUTED as a general bridge /
  UNVERIFIED for π** (#337 Kempner firewall).
- π base-16/base-3 normality, RH, general Collatz, shifted Lonely Runner n=18..94: **OPEN**.
- Signed gate `∀ h≠0: (1/N) Σ e(h·U_n(0)) = o(N)`: **OPEN** — an unproven required cancellation.
