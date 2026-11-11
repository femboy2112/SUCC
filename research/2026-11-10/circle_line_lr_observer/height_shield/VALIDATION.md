# Validation and provenance ledger: Farey height shields

**Date:** 2026-11-10 local / 2026-11-11 UTC. **Parent:** SUCC PR #595 at exact head `4e311d03e3ac9c3dbcbdc32477cd113f2ac0743b`; scope is strictly additive under `research/2026-11-10/circle_line_lr_observer/height_shield/`. No preexisting source, tests, historical claims, imports, workflow or main files changed.

## Actual local execution

Standalone Python 3.13 stdlib environment, no source checkout of SUCC (the matching canonical import is therefore intentionally skipped). Commands:

```sh
python -W error -m unittest -v test_height_shield.py
python -m compileall -q farey_height_shield.py test_height_shield.py
```

**Result:** 15 unittest methods discovered: **14 passed, 1 skipped** because `observational_succ.duck_bbp` was not installed in this standalone workspace. The optional cross-check runs automatically if the repo's canonical package is available. **compileall passed**. Native ~13k suite, Lean/formal kernel, parent CI and hosted checks were NOT run or inferred from these results. Raw focused output is preserved in `focused-tests.log`.

## Exact proof-carrying executions

Every run in `height_shield_receipt.json` was reconstructed by `verify_height_certificate`, including all rational source bounds, signed quotient comparisons, orientations, Farey determinants, height threshold, and final positive margins. Four-pole source terms were separately inspected against frozen `duck_bbp.py` via GitHub; this is not a same-environment canonical import test.

| Target source | H | Elementary arrows | Macro runs | Final rational Farey bracket | Source stages |
|---|---:|---:|---|---|---:|
| circle-beta (pi) | 100 | 20 | `L6,R14` | `311/99 < pi < 22/7` | 11 |
| circle-beta (pi) | 1,000 | 29 | `L6,R15,L1,R7` | `2818/897 < pi < 355/113` | 17 |
| original 4-pole (pi) | 1,000 | 29 | `L6,R15,L1,R7` | same | 3 |
| circle-beta (pi) | 66,317 | 316 | `L6,R15,L1,R292,L1,R1` | `208341/66317 < pi < 104348/33215` | 31 |
| original 4-pole (pi) | 66,317 | 316 | same | same | 7 |
| factorial-sparse nonnormal | 1,000 | 34 | `L14,R17,L3` | `785/256 < z < 2401/783` | 3 |
| original 4-pole (pi) | 1,000,000 | 322 | 10 runs | `3126535/995207 < pi < 1146408/364913` | 8 |

All seven entries have a positive exact `uniform_margin`; do not confuse the displayed source stage counts (different computational units) with wall-time or a universal modulus. The full raw fractions in the JSON are the rational certificates, not decimal approximations.

## Adversarial probes and independent algorithmic checks

- Every reduced rational with denominator up to 218 is excluded from the sample Farey interval `333/106 < pi < 355/113` by exact integer inequalities, without using a pi decimal oracle.
- The H=30 receipt enumerates every candidate rational in the tested range, verifying that the bounded-denominator cut functor is completely decided by its bracket.
- H-values 1,2,7,10,100,113,218,1000,33215,66317,1000000 produce nested certified brackets and output lengths at most `H-1`.
- Expanded 322-arrow macro path from the circle source matches **one-arrow-at-a-time BBP oracle replay** exactly. The two methods share an identification of pi but do not share computational source recurrences.
- Forged source intervals, broken Farey ancestry, wrong final brackets, and inflated margin values are rejected.
- A rational-mediator name approaching 7/2 produces `BudgetExhausted(UNKNOWN)` rather than a fabricated L/R answer; two equal real names also remain UNKNOWN.
- Two correct but separated real names, pi versus pi+16^-60, return UNKNOWN at depth 5 yet yield a rational disjointness witness at depth **57**.
- The factorial-sparse nonnormal irrational passes the same rational-height separation theorem. This deliberately refutes any normality conclusion from perfect finite-cut reconstruction.

**Retained local failure:** An initial test used `>` to compare *source enclosure endpoints* with the computed positive margin. At certain boundary candidates the sharp margin is attained by the source endpoint, so the correct finite arithmetic is `>=`; the true target inequality remains strict because x lies strictly inside its source interval. Test corrected and rerun; no production mathematics changed because of this false rejection. Prior near-miss source tests and budget UNKNOWN cases are preserved as non-success receipts.

## Claims and unexecuted gates

- **PROVED PAPER:** Farey denominator barrier; finite-height shield totality conditional on source enclosure and irrationality; at most H-1 *individual arrow* outputs; positive uniform separation modulus for every rational denominator<=H; coherence of finite cut presheaves; exact compressed run identities; effective separation of unequal correct real interval names.
- **TESTED FINITE:** 14 local tests passed, 1 optional canonical SUCC import skipped; exact certificates for selected H and three source constructions; independent simple-arrow replay for first 322 decisions.
- **CLASSICAL IMPORT:** geometric pi, pi irrationality/transcendence, original BBP identity, basic Farey/Stern–Brocot arithmetic. The circle-beta source and BBP source are *not* independent proofs of pi normality or of the central imported identity.
- **REFUTED shortcut:** all-height decidable cut/inequality observations imply normality (factorial-sparse irrational is a countermodel).
- **UNVERIFIED/OPEN:** full typed lambda compiler, original-zero signed Weyl/odd-eight decay, #591 overlap, #593 joining, pi base-16 normality, RH, full SUCC native CI on this branch, external blind mathematical review or Lean kernel verification.

Mandatory `AGENTS.md` gates are required at integration time, not falsely claimed from this additive draft branch. The intended main consolidation is separate and should pay heavy CI only when the integration candidate is frozen. **Do not merge this research draft to main on the basis of these local receipts.**

## Local hashes before publication

```text
farey_height_shield.py 7f54151d3acd95adb2fcf03e2f8ef8b9b74cbecda2c6d214b88b8a1b35d7a2b7
test_height_shield.py cfaf43bdab16b9f0377e39edca3197ee25bde820b8fb2ee53dc18d390623927a
README.md 78af68818309ec4b726619fec90f13ca66ff9af0cf8670ddb3a9a0ba4e7f520f
HEIGHT_SHIELD_THEOREMS.md 8b492e3a99091d4900a8e88f55856fc2698455449e5bd91d0b5417fd67ffc7e6
HOSTILE_GATES.md 5197aaf8aaafbbda1e867f159e88fe65cf308cebc6c0318d3ec380efe77354e7
focused-tests.log 4fb5e8867f4ebb37bee6a5dbe238e924dda6c49a83d0c5c54599a3f6f24859ca
height_shield_receipt.json 00d937e34b5b9f2c244120808ea6353499ce2cbf601525d7179f9aa632b1e61e
```

Remote Git blobs and commit ancestry must be verified independently **after** publication. These local hashes are reproducibility identifiers, not a proof that the semantic claims are true.
