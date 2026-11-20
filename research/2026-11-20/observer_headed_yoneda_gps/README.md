# Observer-headed causal Yoneda pinbed (OHY)

**Operation:** GPS geometry + source-labeled observer cooperation + algebraic error correction. **Date:** 2026-11-20. **Scope:** additive research, stacked after SUCC constructive Fourier atoms #675. The original BBP source, seed, history, provenance and main branch are unchanged. All mathematics and tests are explicit; no pi-normality proof or physical GPS observation is claimed.

## The idea

Put **observer heads** on the old Fourier–Yoneda pinbed. Each head has an actual source/path passport, calibrated local reference, prospective causal action, memory and resource budget. The shafts are verified causal transports. The bed asks whether all reports have a common generating carrier—and whether their **joint** information determines the particular target under study.

The GPS analogy is exact in the relevant mathematical scope: *number* of sensors is a rank/parameter count; *geometric arrangement* determines local accuracy; *redundancy* yields error-detection/correction only when the observation code has enough distance. A second observer can genuinely unlock a distinction that neither observer can access alone, as in the XOR example; multiple duplicate or uncalibrated heads cannot.

## Result worth starting with

**OHY-06 — BBP seven-head error-correcting theorem:** In the declared five-parameter four-pole coefficient-and-seed family, any five distinct exact unwrapped clock readings determine the source (inherited rigorous arbitrary-clock theorem #671). Therefore any `m>=5` distinct heads form a full-spark observation code with **minimum distance `m−4`**. Seven readings give a **[7,5,3]** code: one entirely corrupted scalar report can be identified and repaired; two known erasures can be survived. This is exact rational/source-class fault tolerance, *not* a theorem about pi's statistical phase or real-world noisy probes.

**OHY-05 — Old pinbed syzygy becomes a syndrome:** the original two-tone channel equation `G_1 y_0 − G_0 y_1=0` is already a parity-check identity. With a third nonzero coherently calibrated gain, one complex harmonic admits an exact [3,1,3] code correcting one bad channel. The full probability-measure realization still needs positivity and cross-frequency consistency.

**OHY-01–04 — Carrier gluing / GPS / information synergy:** joint head rank determines source/target recoverability; the left-nullspace gives exact inconsistency checks; full-spark geometry gives error correction; singular values and bounded noise determine actual accuracy; two parity-type heads can each contain zero information about the target and jointly recover one full bit.

**OHY-08 — a shared blind spot cannot be cured by voting:** all heads restricted to late BBP circle readings are blind to the source-seed shift `1/16` from clock one onward. This is a true access-gap, not a need for more redundant heads. An authenticated seed/open-path memory head repairs it. Neither source recovery nor perfect parity-check agreement forces pi normality.

## Architecture

```text
                 Authenticated source + initial condition
                                 |
                 lawful chronological source paths
                     /         |        |       \
              Head A        Head B     Head C    Head D ...
              clock /        clock /    clock /  clock /
              memory         memory     frame    Fourier
                     \         |        |       /
                 calibrated, source-typed reports
                                 |
          joint realization (syndromes Λy = 0), rank / target descent
                                 |
          precision bound σ_min / target inverse; fault budget d_F
                                 |
                  qualified carrier-relative verdict
```

Joint observation is a **behavioral quotient** until lawful Hom-probes are shown dense: do not relabel scalar outputs as full Yoneda. The observer's own physical computation is a potential feedback subsystem only if real interventions and source response maps are supplied.

## Paper theorems and executable controls

| File | Purpose |
|---|---|
| [THEOREMS.md](THEOREMS.md) | Full definitions, quantified claims OHY-01–10, proofs, GPS/ECC/source boundaries |
| [observer_pinbed.py](observer_pinbed.py) | Standard-library exact rational head matrices, syndromes, rank, error correction, BBP source and forward holonomies |
| [test_observer_pinbed.py](test_observer_pinbed.py) | 33 exact focused regressions, including 7-head and 5-head fault cases |
| [independent_audit.py](independent_audit.py) | Separate SymPy formulas/inversions and NumPy singular-value stress cases; **does not import the implementation** |
| [independent_audit_receipt.json](independent_audit_receipt.json) | Raw scoped independent-audit output |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Truth statuses, dependencies, hostile controls, exact source-map boundary |
| [NEXT.md](NEXT.md) | Preregistered source-anchored observer cooperation experiment toward R0 |
| [PROVENANCE.md](PROVENANCE.md) | Main and donor provenance; classical antecedents; no novelty claim |
| [VALIDATION.md](VALIDATION.md) | Executed commands, counts, hash scope and known unrun suites |

Run from this directory: `python -m unittest -v test_observer_pinbed.py` and `python independent_audit.py` (the latter requires optional SymPy and NumPy). The exact implementation uses only Python stdlib.

## Boundaries

The joint source bank can **correct observer transcript corruption** but cannot certify an unrestricted unseen source continuation. The GPS comparison is a synthetic *local linearization*, not a physical receiver experiment. The unlocked 5-parameter BBP source still requires an independently proved source-selected signed all-shell Fourier/hexadecimal-domain-wall bound for R0; full pi normality and RH remain OPEN. Source-syndrome zero means compatibility within a declared class, not actual provenance, successful physical observation, or global phase mixing.
