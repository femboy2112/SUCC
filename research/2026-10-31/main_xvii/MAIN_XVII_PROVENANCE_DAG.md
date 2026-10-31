# Operation Main XVII — cross-PR provenance and dependency graph

**Date:** 2026-10-31 (New York). **Baseline:** `main = e18ba565` (Operation Main XVI).
**Integration branch:** `integration/succ-main-xvii-carrier-selected-frontier-2026-10-31`.
This file records the exact commit ancestry used to plan the integration. Heads were refreshed
from GitHub at operation start; abbreviated SHAs below are the live PR heads at that time.

## 1. The 35 open research PRs (#390–#424)

All are additive draft PRs created 2026-10-30 on top of Main XVI. None modifies `main`'s
canonical files except **#396** (one additive `docs/CLAIM_INDEX.md` block + a regenerated
`docs/math_memory/CLAIM_CATALOG.json` + a new supplement + a new `tests/` test). No PR touches
`observational_succ/`, `formal/`, `scripts/`, `provenance/`, `.github/`, `ci.yml`, the frozen BBP
source, `U_0 = 0`, or the four signed poles.

## 2. The dependency DAG (by `git merge-base --is-ancestor`, verified)

Six root clusters off `main`; linear chains verified ancestor→descendant.

```
CLUSTER A  (time-extruded / Lorentz triangle)
  main → #390 → #392 → #393 → #394                         leaf: #394
  main → #391                                              leaf: #391  (independent root)

CLUSTER B  (frame reset / human observer)
  main → #395                                              leaf: #395
  main → #396                                              leaf: #396  (touches CLAIM_INDEX/CATALOG)

CLUSTER C  (Fibonacci → carrier spine → universal-N)
  main → #397 → #402 → #404 → #406 → #409 → #412 → #414 → #416
                                              ├── #418     leaf: #418  (+ non-Pisot/Pisot ramif.)
                                              └── #420     leaf: #420  (+ Basel/line-circle)

CLUSTER D  (BBP prime stroboscope → cylinder forges)
  main → #398 → #399 → #400 → #401 → #403 → #405
                                 ├── #407 ──┬── #410       leaf: #410  (DeepSeek V4 forge)
                                 │          └── #411 → #415 leaf: #415  (Codex Astra forge)
                                 └── #408 → #413           leaf: #413  (triangle fabric + Fib. extrusion)

CLUSTER E  (universal N/Z carrier)
  main → #417 ─┬── #421                                    leaf: #421  (adelic jet transport + all-order shadow)
               └── #424                                    leaf: #424  (carrier-first certified transport)

CLUSTER F  (Pisot-Lagrangian ; dyadic zeta)
  main → #419                                              leaf: #419  (Pisot-Lagrangian geometry)
  main → #422 → #423                                       leaf: #423  (dyadic zeta + summation arrows)
```

Notes.
- **#410 and #415 are genuine siblings** (both base on #407): DeepSeek-V4 and Codex-Astra-Ultra
  cylinder proof-forges. Neither is an ancestor of the other; both are integrated.
- **#418 and #420 are genuine siblings** (both base on #416); both integrated — #418 adds the
  non-Pisot/Pisot ramification dir, #420 adds the Basel/line-circle dir.
- **#421 and #424 are genuine siblings** (both base on #417); both integrated.
- Linear chains are subsumed by their leaf (verified: e.g. #416 is an ancestor of both #418 and
  #420; #407 of both #410 and #415; #405 of #413).

## 3. The 13 ancestry-minimal leaves integrated

`#391  #394  #395  #396  #410  #413  #415  #418  #419  #420  #421  #423  #424`

These 13 tips subsume all 35 open PRs by inclusion. Each was merged with an ancestry-preserving
`--no-ff` merge onto the integration branch (history preserved; branches retained). The 22 interior
PRs (#390, #392, #393, #397–#409, #411, #412, #414, #416, #417, #422) are integrated transitively
as ancestors of the leaves.

## 4. Merge result

13 `--no-ff` merges, **zero conflicts** (every PR is additive under its own
`research/2026-10-30/<dir>/`; shared spines share identical commits via their merge-base).
Overall diff vs `main`: **1312 files, +175843 / −3** (the 3 deletions are #396's catalog
regeneration). 34 new `research/2026-10-30/` dirs.

The near-absence of conflicts is structural: distinct dirs per package, and the only canonical-file
touch (#396) is unique. The math-memory `CLAIM_CATALOG.json` is regenerated **last**, after all doc
edits, per the standing lesson.
