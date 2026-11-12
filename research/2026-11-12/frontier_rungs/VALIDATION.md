# Validation record — frontier rungs round (2026-11-12)

Nothing below is external peer review. Kernel verification covers only the exact lemmas listed in
`lean/README.md`. No outcome promotes an OPEN claim: π base-16 normality, R0, R1, (CH) and the
source-selected signed estimate are OPEN.

## Starting point and commit order

Branch `research/frontier-rungs-restricted-exponent-2026-11-12`, created from draft PR #599 head
`8de33430fb35dc0360dacff92c4ee1e4364ad458` (verified equal to the remote head and a descendant of
Main XXIV `071ce1e0`).

| Commit | Content |
|---|---|
| `1dd676ed`, `9b4b71b2` | preregistration, then its correction (shell history, data-fresh holdout) — before any code of the round existed |
| `bad403f1` | repairs to the 2026-11-11 dossier after the re-audit of its repaired passages |
| `18bab4a1` | LIMIT_FACES, `faces_core.py`, tests, probe and results, as written (pre-audit) |
| `b1457dd7` | RESTRICTED_EXPONENT, `rde_core.py`, tests, exploration record, as written (pre-audit) |
| `4c46a5db` | repairs to LIMIT_FACES after its audit |
| `9d6f2e56` | repairs to RESTRICTED_EXPONENT after its audit |
| later | Lean check, analysis, ledger, source map, this record; integration documents |

Theorem files were committed before their audits so that every repair is a visible diff.

## Independent audits (separate read-only instances of the same model family; own code; no dossier modules)

### 1. Re-audit of the repaired 2026-11-11 passages (CARRY_FLUX, THEOREMS IAD-02/04/05/07/08/09, SCOTT_TRANSPORT SWT-01/03)

No displayed theorem blocked. Three **false prose sentences** found and fixed in `bad403f1`:
"L2 and L3 are open [for algebraic numbers] as well" (L2 holds by Ridout); the hostile-control list
of NEXT.md (W3 is a positive control, not a hostile one); a stale pre-repair copy of the IAD-04
corollary in OBSTRUCTIONS O-2. Further overclaims and wording repaired: `v_16 ≤ μ − 1` for
irrationals only; fifteen fixed points; lag-correlation transfer; explicit bracket for `g_H`
(IAD-04 itself not re-run for it); two four-pole members on the π-line; "finite places `p ≠ q`";
the IAD-08 box now states the normalised lag form (as written before, the hypothesis held for every
real number at `ℓ = ⌊B/2⌋`); "(CH) is the weakest signed statement" withdrawn. The auditor's own
computations (1 365 847 checks of ZSC-01/02 on synthetic families; exact carries to `n = 2600`;
rank of the Baker system; witnesses) are its testimony.

### 2. Audit of LIMIT_FACES.md

Every displayed statement LMF-01…06 approved after line-by-line reading and independent
recomputation of every constant. Found and fixed in `4c46a5db`:

| Finding | Disposition |
|---|---|
| FALSE (summary table): the bound for `G(ν)` summarised without `16 ∤ h`; exact counterexample at `h = 16` (`G = 47/4096 < 48/4096`) | condition restored |
| FALSE (Reading 1): "closed face" for R1 (a union of faces) and for all-mode savings (a face that is not closed) | reworded |
| GAP (LMF-05 jump lemma): asymmetric wrapped arc untreated, proof incomplete | proved in full |
| OVERCLAIM: "all sharp for shells" (proved for `1/4`, `1/60` only); "`1/120` refuted" (as extremal value, not as threshold); "values a generic point shows" | reworded |
| nine cosmetic points (lifts, window/shell comparison, equality set, citations, probe docstring) | fixed |

### 3. Audit of RESTRICTED_EXPONENT.md

Nothing blocked. Headline numbers reproduced independently: the forms of the tilted family
`(2,4,3)` exactly to `n = 40` (divisibility, saved primes, sizes), `α = 4.59177713`,
`log R_* = 5.62472238`, `s = 0.74069536`, bound `2.3766635` (`2.3813210` with `s_60`); Rivoal's
table reproduced to `7·10^(−7)` on 18 of 19 entries, `Λ(1,16,1) = 1.8812718`; the extension to
`g·16^m` judged derivable from his Lemmas 1–2 with RDT-01/02(d); L2 for `log(16/15)` holds for every
large shell. Found and fixed in `9d6f2e56`:

| Finding | Disposition |
|---|---|
| FALSE (RDT-02(c)): "a family failing the classical criterion proves nothing at restricted denominators" — counterexample `ξ = 1/3`, forms `(2^k, (2^k−1)/3)` | replaced by the per-form statement |
| FALSE (RDT-04(a)): "`D_n` divisible by every odd number below `2n`" (`9 ∤ D_6`) | replaced by primes `p ≡ 1 (4)` in `(4n, 8n)`; full-depth hypothesis weakened |
| GAP / wrong condition (RDT-06(d)): non-vanishing of `J_n` is not sufficient; the displayed inequality was trivially true | condition restated (existence of `lim (1/n) log|J_n|`) |
| OVERCLAIM ("the ZSC-01 obstruction is absent" for `log(16/15)`) | exact range stated (`η ≤ 0.126`, `c ≤ 0.063`) |
| OVERCLAIMS: `L2 ⟺` (only `⟸`); wrong-side imbalance attributed to the shadow lemma (it is OBSERVED); effective base `√2` without the `Q(i)` qualification; a priority phrase | reworded |

**Not audited again:** the repairs listed in 1–3. FRONTIER_ANALYSIS, README and CLAIM_LEDGER were
written after the audits and aligned with them by the author; they were not audited.

## Lean kernel check (`lean/`)

`check_zsc_carry_flux_lean.py` against the pinned toolchain (Lean 4.14.0) and mathlib
(`4bbdccd9…`): `KERNEL_CHECKED`, 33 theorems, axioms exactly `propext`, `Classical.choice`,
`Quot.sound`; 9 paired controls (true statement compiles, mutated statement fails to compile, and
the negation of the mutant is proved). Written by a helper instance and re-run by the integrator
with the same outcome. Scope: ZSC-06 null relation (algebra and the vanishing integral), ZSC-02
locality lemma (both parts, every real), ZSC-03 renewal lemma (four-pole forcing, every real seed).
Not formalised: the BBP series itself, Baker rigidity, ZSC-01, ZSC-02 (a)–(d), ZSC-04/05, anything
statistical.

## Literature (citation check by a helper, not refereeing)

See SOURCE_MAP. The recollection "Rhin: `‖2^k log 2‖ ≥ 2^(−0.79k)`" was false (the constant belongs
to `‖(3/2)^k‖`). Rivoal 2007 was read at source and is the import of RDT-07. Three unrefereed 2026
claims (`μ(π) = 2`; `μ(log α) = 2`; `μ(π) ≤ 7.1019`) are recorded as CLAIMED / UNVERIFIED and are
not used. Baker's theorem is still quoted from secondary sources.

## Preregistered probe (`probe_rungs.py`, full run)

- Authentication first: three routes to the hexadecimal digits of `π/16` (exact zero-seed carrier
  on `1 ≤ n ≤ 2600`; integer series of the frozen source with a rigorous enclosure; high-precision
  π) agree on every digit compared (12 074 digits between the last two).
- 223 614 theorem-grade checks, 0 failures; `RESULTS_rungs.json` byte-identical across two Python
  environments and across re-runs after the audit repairs.
- Holdout shells `B = 3301, 4099, 5003, 6007`: `W_1 = 0.002927, 0.003565, 0.006074, 0.003690`;
  `D = 0.002921, 0.003568, 0.005820, 0.003614`; `c_B = 0.932444, 0.934618, 0.933839, 0.934243`.
- RP-1 (`W_1 < 0.009`), RP-2 (`D < 0.008`), RP-3 (`0.90 < c_B < 0.97`), RP-4: **met**.
  RM-1, RM-2, RM-3: rejected / flagged as registered.
- These values are of the size `B` independent uniform points would give; single shells below
  `1/60` also occur for points failing (CH). **Not evidence for any rung.**

**Deviations from the preregistration, all recorded as misses of the preregistration, not of the
data.** (1) The provisional threshold `w* = 4/225` for `W_1` was false: shell measures also approach
the lift `1` of the fixed point `0`; the proved threshold is `1/60`. RP-1's bound `0.009` was
stated as "about half of `w*`"; it is `0.54` of the proved threshold and was not changed. (2) The
provisional `D`-threshold `1/60` is the proved one, for a different reason than the one written.
(3) RM-1 was registered as "`W_1 ≥ 4/225`"; the constant-digit control gives `W_1 ≥ 1/4`. (4) The
first preregistration commit misquoted earlier shells and chose a holdout inside the already-read
range; it was corrected in a second commit before any probe code existed. (5) The probe covers
LIMIT_FACES only; RESTRICTED_EXPONENT has tests and an exploration record, not a preregistered
probe (its numerics are symbolic computations declared exploratory in the preregistration).

## Dossier-level runs (repository root, `PYTHONPATH=$PWD`, `-W error`)

- `unittest discover -s research/2026-11-12/frontier_rungs`: 50 tests OK (26 LMF, 24 RDT).
- `unittest discover -s research/2026-11-11/innovation_arithmetic_decoupling`: 72 tests OK after the
  re-audit repairs.

## What was not done

- No external review. No second audit of any repair. No Lean beyond the listed lemmas.
- No interval enclosure of `Λ(1,16,1)` or of the rates of RDT-05; `m_0` not explicit in RDT-05 and
  RDT-07.
- Rivoal's Lemmas 1–2 were read as stated, not re-proved. Baker, Ridout, Worley at source: not read.
- The Salikhov and Zeilberger–Zudilin forms were not examined for a 2-adic imbalance; Machin-type
  simultaneous constructions were not examined.
- Nothing here bears on R0, R1 or (CH) for π.

## Repository gates

Receipts of the repository-wide gates for the integration candidate are recorded in the Main XXV
integration audit and in the pull request description, keyed to the tested commit and tree, because
the mathematics catalog pins the hash of this file.
