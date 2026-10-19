# Operation SUCC Academic Main V — Integration Audit (2026-10-19)

**The Source Coherence Forge.** Consolidation of the seven stacked draft PRs **#184–#190** onto the
Academic Main IV base, with an independent hostile mathematical audit and a coherence map of how the new
families relate. This record is authoritative for the Academic Main V integration.

**RH PROVED: NO. ABC: OPEN. Signed Suzuki `S₄ = A₄ − R₄`: OPEN (AMBIGUOUS).**

---

## 0. Verified base and intake

- **Verified base `main` = `4de865766d53ea448555386d98f3e88e3ec605b6`** (Academic Main IV merge, PR #183).
  Confirmed against live `origin/main` by fresh fetch — no other session had advanced main; PR #183 is
  still the last merge, 0 PRs merged since.
- **Integration branch:** `integration/succ-academic-main-v-2026-10-19`, head
  **`37bec225ed0cd8ea55e20bc24480c7462a2e5ed5`**.
- **The seven incoming PRs (live head SHAs, matched byte-for-byte to the intake snapshot):**

| PR | Family | Head SHA | +commits/main |
|----|--------|----------|---------------|
| #184 | RRT (RAD/RIS) | `eeadf00729dafff3c784251c969ec2afd331818f` | 14 |
| #185 | PPC (primorial/factorial clocks) | `74436bcfb346781eba5796c52baea59accb6734e` | 31 |
| #186 | GTC (Green–Tao clock APs) | `7e8984e0cb5d138760719018e5ac6ec2ab511b26` | 59 |
| #187 | ABC-CLK (ABC clock energy) | `b6c9f5003648a3bf688f76d9c6aa84f643bc3bda` | 19 |
| #188 | MCD (meta-choice descent) | `9dbf9402103b24234cb701530179545b28467ffa` | 19 |
| #189 | BDW (Borwein delta) | `414efb07f396af4a8d15ffed9fe36d6567fda95a` | 68 |
| #190 | FBH (factorial Borwein hologram) | `329c71c7deeae13f292a291b58d40820a2f3f23f` | 77 |

- **Out-of-scope sibling (preserved, not merged):** `research/borwein-abc-height-contact-2026-10-19`
  (`b073a3dfce62cd1e2e48fcf65838349c085d9ac3`), a divergent variant off #189 (merge-base = #189 head),
  **no open PR**, carrying unique `borwein_abc_bridge/contacts/height` modules. Left untouched on origin and
  flagged to the maintainer; NOT folded in (unreviewed, outside the authorized 7-PR scope).

## 1. True ancestry (git rev-list, not PR labels)

```
main → #184 → #185 → #186 → #189 → #190      (strict linear chain)
main → #187                                   (independent root)
main → #188                                   (independent root)
```

Verified by pairwise `git merge-base --is-ancestor`: `#184 ⊂ #185 ⊂ #186 ⊂ #189 ⊂ #190`; `#187`, `#188`
independent; all seven merge-base with `main` **is** `main`. The PR base labels happened to match this
time, but the DAG was taken from ancestry regardless. Terminal tips `{#190, #187, #188}` cover all seven;
machine-readable graph in `SUCC_ACADEMIC_MAIN_V_DEPENDENCY_GRAPH.json`.

## 2. Merge execution and conflict resolution

Seven history-preserving `--no-ff` merges in the preferred ancestry order **#188, #184, #185, #186, #189,
#190, #187** (development stages kept visible rather than squashed), followed by one navigation-reconcile
commit. Merge commits, coverage, and per-merge conflict status in
`SUCC_ACADEMIC_MAIN_V_MERGE_COVERAGE.json`.

- **Entire conflict surface = `README.md`** (touched by both #188 and the #184 chain). The two front-door
  edits are additive on different hunks; `git ort` auto-merged with no manual intervention. Every
  claim-supplement, the registry, CLAIM_INDEX, and all three workflow files were each touched by exactly
  one independent line → taken clean. **No manual conflict resolution was required; zero conflict markers
  in code/docs.**
- **Diffstat vs main: 42 files changed, +6611 insertions, 0 deletions** (plus the Academic Main V doc set).
  Purely additive — no archival file removed.

### Claim-navigation reconciliation (completeness repair)

The #184–#190 chain registered and indexed only **RRT, PPC, GTC, BDW**. The supplements for **#190 (FBH),
#187 (ABC-CLK), #188 (MCD)** existed as files but were never wired into the registry, `CLAIM_INDEX.md`, or
the README front door. Added all three **additively** (commit `37bec225`):

- `CLAIM_NAMESPACE_REGISTRY.json`: +3 namespaces → **23 namespaces, 23 unique `fq_prefix`, no collision**;
  all 15 `test_claim_namespace_collisions` tests pass, including the live `unregistered_prefix_collisions()`
  guard. No historical bare ID renamed.
- **`ABC-CLK` note:** its hyphenated bare tag is NOT parsed by the `claim_namespaces` regex
  (`[A-Z]{2,6}[0-9]*`), so ABC-CLK IDs are absent from the automated census and the `fqid()` mapper.
  Registered additively for navigation with an explicit `note`; a SUCC→YEAN FQID extractor keying off it
  would need a regex extension. Preserving #187's historical IDs outranks tooling tidiness.
- `CLAIM_INDEX.md` + `README.md`: front-door entries added for FBH, ABC-CLK, MCD with their firewalls.

### Frozen source preserved

`formal/EODCS_RelationalChoice.lean` is **byte-identical** to the frozen blob
`3d5601391dccda0c2c89f695b7c699bb08de6131` on base, #188, #190, #187 and the integration head. #188's new
theorems live in `formal/MetaChoiceRelationalDescent.lean` (importing the original); the Cambrian-rejected
in-place modification did **not** return. `scripts/verify_provenance.py` → `SOURCE_PROVENANCE_VERIFIED`,
72 items, 17 byte-identical archives, source commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`,
`establishes_mathematical_truth: false`.

## 3. Coherence map — how the new families relate

**Layer A — original-source arithmetic (#184–186, parts of #187).** SUCC/FUCC dynamics; genuine prime /
prime-power clocks (`Λ(p^k)=log p`); radical/excess multiplicity `rad`/`ris` (exact integer/Fraction); CRT
compatibility and the **successor non-identification no-go** (a fixed finite-instrument read of the
valuation vector cannot pin a successor — NOT a computability claim); primorial (→ `∏_q F_q`, squarefree)
vs factorial (→ `Ẑ = ∏_q Z_q`, all depths) completion, a *real* distinction; source-labelled p-adic
precision; additive `a+b=c` constraint. Mathematical source identity is kept distinct from numerically
matching residues (clocks decide **residues/phases**, never primality — primality is always independent
trial division).

**Layer B — categorical & logical transport (#188).** "Construct categorically; verify relationally;
certify globally through lawful source interfaces." Four **independent** gates: local witness availability,
transport/descent compatibility, original-source realization, proof authority. Witnessed dependent-type
choice is kept distinct from unrestricted categorical AC; the Diaconescu firewall (full internal AC ⇒
Boolean internal logic) blocks simultaneously asserting full internal AC and non-Boolean global logic. The
constructive `MayReport` left adjunction, image-relative descent theorem, and the F₂ odd-loop
counterexamples are new-to-project formal organization — **not** an original topos theory.

**Layer C — harmonic & analytic representations (#186, #189, #190).** Green–Tao/W-trick AP gates (external
theorem, cited); exact finite Fourier residue projectors; Borwein sinc/uniform-convolution lifts; prime-power
factorial windows; **stable source-to-continuous sampling embeddings** (the factorial Borwein hologram's
bounded injective `ℓ²(ℤ)→L²(ℝ)` lift, reversible **only on its range** — point evaluation is not bounded on
arbitrary L²); source-indexed operator transport; spectral mixing obstructions for growing CRT wheels. The
three "factorials" — Borwein simplex-volume, Poisson jump-time, arithmetic `v_p(N!)` — are kept **distinct**.

**Layer D — global certificates (status ledger).**
- *Exact source constructions:* rad/ris arithmetic, CRT local laws, Legendre windows, F₂ cochain certificates.
- *Constructive / classically proved preservation:* FBH-01..07 (PROVED LOCAL), MCD-01/03/06/10 (Lean-kernel,
  choice-free), the composition/partition identities.
- *Source-conditional implications:* ABC-CLK-05 (convex envelope piecewise-linear **assuming ABC**).
- *Finite verified computational statements:* 5×5 prime grids, held-out ABC census, 729-graph obstruction sweep.
- *Imported classical analytic theorems:* Green–Tao (2008), PNT-AP, Maynard–Tao, Diaconescu 1975, Borwein 2001.
- *Unverified global claims:* ABC-CLK-07, MCD-08/09 (explicitly UNVERIFIED).
- *Refuted implications:* FBH-09 (first-prime-width mutation), MCD-04/05/07, ABC-CLK-08/12.

A proof of a completion does not prove the completed point came from the original source; a positive
analytic/Hilbert Gram does not produce the signed completed Weil form. These boundaries are explicit in
every supplement.

## 4. Validation gates (the merged tree, run as one)

| Gate | Result |
|------|--------|
| `scripts/verify_provenance.py` | **SOURCE_PROVENANCE_VERIFIED**, 72 items, 17 byte-identical, source `ba075348…`, `establishes_mathematical_truth:false` |
| `compileall` (observational_succ, tests, scripts, formal) | **exit 0** (pre-existing `\p`/`\|`/`\h` docstring SyntaxWarnings in untouched old files only) |
| `observer_foundations_probe.py` / `ordinal_succ_report_probe.py` | exit 0 / exit 0 |
| `scripts.factorial_borwein_hologram_probe` (module invocation) | exit 0 — emits Weil/source firewall |
| `abc_clock_green_tao_probe.py --limit 1200` | exit 0 — "FINITE ENUMERATION, not a universal bound or ABC/RH proof" |
| `test_claim_namespace_collisions` | **15/15 OK**, unregistered-collision guard empty |
| **Lean 4.14.0 gate** | frozen + imported + standalone **all compile**; `#print axioms`: 8/9 declarations axiom-free, 1 only `propext`; **NO `Classical.choice`**; **no `sorry`/`admit`/`axiom`/`unsafe`/`native_decide`** |
| **Full `unittest discover`** | **`Ran 6001 tests — OK`** (0 failures, 0 errors; py3.12 local, package on path). The merged tree passes as one tree. Note: one test (`test_exact_probe_receipt_and_independent_count`) shells out to `scripts/meta_choice_descent_probe.py` as a subprocess; it requires the package importable (editable install / `PYTHONPATH`), which CI and the documented `pip install -e .[test]` provide — a bare `unittest discover` with no install errors on that one probe only. No test assertion was weakened. |
| Python 3.10 / 3.13 hosted CI | **[integration-head CI — pending push; filled in §8 of the operation report]** |

New-feature test files present and discovered: `test_rad_ris_transport.py`, `test_prime_phase_clocks.py`,
`test_green_tao_clock_ap.py`, `test_abc_clock_families.py`, `test_eodcs_meta_choice_descent.py`,
`test_borwein_prime_clock.py`, `test_factorial_borwein_hologram.py`.

## 5. Independent hostile mathematical audit (§3, read-only, methodologically distinct)

Three independent read-only reviewers, each briefed on the firewall and barred from running the heavy suite:

- **Audit A — number theory (#184–187):** **CLEAN.** All 10 points backed by a displayed proof or an exact
  finite enumeration the reviewer reproduced (CRT no-go quantifiers correct; rad/ris exact; primorial-vs-
  factorial completion real; clocks never claim primality; all-prior/√p-window no-go **proved** via
  Bertrand/primorial-growth, not merely swept; fixed-vs-growing modulus never slipped; Green–Tao/Maynard–Tao
  external-only with correct "≥ m of K, not consecutive" caveat; 1+jR ladders kept distinct from APs;
  `X^(8/5−…)` labeled strictly inferior to the 2026 `X^(3/5+ε)` benchmark; local independence never promoted
  to global; firewall intact). *Boundary:* the distinct-slope Maynard–Tao generalization is cited (labeled
  EXTERNAL), not independently recertified.
- **Audit B — operator/sampling (#189–190):** **CLEAN.** All 12 points exact: Irwin–Hall/simplex formulas and
  the "first crossing at 29" reproduced; sinc normalization consistent; **the bounded lift is well-posed on
  its range with topology stated (`ℓ²→L²`), never globalized to point evaluation on arbitrary L²**;
  width-budget `S_N<11/12` exact; Newton width-reconstruction proved; infinite-N limit converges in **L^∞**
  with explicit summable remainder `E_N→0`; the three factorials kept distinct; fixed-W no-mixing stated as a
  non-result; FBH-09 **exactly REFUTED**; firewall intact. *Routing suggestions (not defects):* the FBH-06
  4-Lipschitz coupling constant deserves a demonstration-grade proof; the off-grid label-collision probe (1/10
  collides N=4,6) is worth adversarial pushing.
- **Audit C — logic / source / provenance (#188):** **CLEAN / APPROVE.** All 10 points earned their label,
  most by two blind methods, independently reproducing the coordinator's gates: frozen blob = `3d5601391…`
  by `git ls-tree` **and** sha256 = the CI's recorded Cambrian anchor; the `#print axioms` trace (8/9
  axiom-free, 1 `propext`, **zero `Classical.choice`**) reproduced exactly; `witnessed_dependent_choice` is
  Σ/subtype DATA projection (not Prop extraction); MCD-04 off-image envelope separation proved in Lean
  (`empty_observation_fiber_separates_envelopes`); the 729-graph F₂ obstruction cross-checked by two
  algorithms (336 obstructed + 393 flat, odd-triangle sections = 0); MCD-07 REFUTED / MCD-08/09 UNVERIFIED;
  provenance 72 items confirmed; #188 introduces no summed Schur bound and leaves `S₄` OPEN. *Wording note
  (not a defect):* the May/CommonPossible refutation lives in the Lean, not the Python (which models the F₂
  graph sections); the Lean evidence fully carries it.

**Audit synthesis: all three independent reviewers returned CLEAN; zero confirmed defects.** Two
non-blocking routing suggestions (demonstration-grade proof of the FBH-06 4-Lipschitz coupling constant;
adversarial push on the off-grid label-collision probe) are logged for the Thinker-Dome, not gate failures.

**Retained Academic Main IV rule:** the #181 and #182 prime-two inverse estimates are **alternatives** for
the same Schur residual — **never summed** without a new common operator inequality. Nothing in Main V
resurrects a summed bound; signed `S₄` stays OPEN.

## 6. Mathematical novelty boundaries & open frontiers

- **Classical, imported:** Green–Tao, PNT-AP, Maynard–Tao, Dirichlet/Bertrand, Diaconescu 1975, Borwein 2001,
  Irwin–Hall, Newton identities, Legendre valuation, Max-2-LIN/MaxCut correspondence.
- **New-to-SUCC (source-sensitive synthesis, no priority claimed):** the registered RRT/PPC/GTC/BDW/FBH/
  ABC-CLK/MCD organizations; the choice-free relational-descent + existential-support adjunction
  (Lean-kernel verified); the factorial-Borwein range-only cardinal lift; the exact F₂ odd-loop obstruction
  certificates.
- **Proved genuinely new mathematical statements:** none that resolve ABC/RH/`S₄`. The results are exact
  realizations/organizations of classical mathematics plus finite certificates.
- **Refuted implications:** FBH-09, MCD-04/05/07, ABC-CLK-08/12.
- **Unverified / open:** ABC-CLK-07 (uniform ABC from clock weights), MCD-08 (concrete Grothendieck site),
  MCD-09 (novel arithmetic/Weil/RH), and the standing **ABC / signed-Weil / RH** frontier. The forward
  research program is in `SUCC_ACADEMIC_MAIN_V_RESEARCH_FRONTIER.md` (Moonshots A–E).

## 7. Verdict

Integration is coherent, additive, history-preserving, firewall-clean, and (Lean + provenance + probes +
namespace + two of three audits) green. Pending the full-suite count and integration-head CI, the
disposition is **GO** for the authorized main merge. [Final verdict + merged `main` SHA recorded in §8 of the
operation report once CI is green.]
