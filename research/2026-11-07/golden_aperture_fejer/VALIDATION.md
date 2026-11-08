# Execution and provenance — golden aperture BBP, 2026-11-07

## Exact repository and hypotheses

- Base: source-specific critical Fejér PR #538 exact head `eda162b5610d4a9d66bb3c3acbcdc728cbc0eccd`. Sister HPB aperture PR #539 at head `c8c5cf0488b3667b0f603983e9ad3766ba78e546` read-only. Frozen original SUCC four signed source and literal U0=0, inherited AGENTS.md, archive, provenance, formal/Lean, workflows, license and main unchanged.
- `PREREGISTRATION.md` committed on GitHub at `44a099cc5b9903039e1b305ce989bdf4370839bc`, BEFORE measuring A79/157/281/389 golden values. Old #538 critical Fejér sample values were already known, but these fixed-golden spatial energies were not.
- `PREREG_LARGE_EPOCHS.md` committed at `31ab4a1d123ca48c394cf88b6a4ea74cbe6b7489` BEFORE measuring A1024/2048/4096 golden energies; A512 was separately pre-seen as an algorithm speed calibration, never a blinded holdout.
- All reported source values are **original zero-seeded BBP**, with the real completed π orbit entering only through the proven `T_n` inequality. No irrational seed was injected in selected observations.

## Actual executable local commands

```sh
python -m compileall -q golden_aperture.py test_golden.py finite_probe.py large_probe.py fiber_probe.py independent_oracle.py independent_check.py
python -m unittest discover -v -p 'test_*.py' >TEST_STDOUT.txt 2>TEST_STDERR.txt
python finite_probe.py >FINISHED_PROBE_LOG.txt
python large_probe.py >LARGE_PROBE_REPLAY_LOG.txt  # replays 1024,2048 only
python fiber_probe.py >FIBER_PROBE_LOG.txt  # exploratory, not preregistered
python independent_oracle.py >INDEPENDENT_ORACLE_LOG.json
python independent_check.py >INDEPENDENT_CHECK.json
python receipt.py
python receipt.py --verify
```

**Executed:** stdlib compileall PASS. **16/16 focused unittest methods PASS**, 0 errors and 0 current failures. Independent combined-rational source and direct moving-arc sweep `independent_check.py` PASS on 5 epochs A8/16/32/64/128, using mpmath 80-digit computational diagnostics compared to rigorous rational exact intervals. These are independent implementations of the same analytic formulas, NOT external mathematical referees or fully independent source provenance. Rational input pair-census exact threshold `d<b` is established by integer algebra; interval bounds use `isqrt` and exact integer division, not floating phase tests.

### Original selected finite results — CERTIFIED FINITE ONLY

The raw exact/oriented outputs are `FINITE_RESULTS.json` and `LARGE_RESULTS.json`; energy decimals are outward rounded rational bounds, not approximate interval half-width claims.

| Original epoch A | Golden source E_a interval (14 decimals) | Completed π interval using GA5 |
|---:|---|---|
| 79 | [0.01035985538469, 0.01035985538470] | [0.01033188941781, 0.01038782135157] |
| 157 | [0.00216407887510, 0.00216407887511] | [0.00215699803615, 0.00217115971406] |
| 281 | [0.00211303656019, 0.00211303656020] | [0.00211082615760, 0.00211524696280] |
| 389 | [0.00284911123664, 0.00284911123665] | [0.00284795782371, 0.00285026464959] |
| 1024 | [0.00116171098489, 0.00116171098490] | [0.00116154453477, 0.00116187743501] |
| 2048 | [0.00024354735393, 0.00024354735394] | [0.00024350574140, 0.00024358896647] |
| 4096 | **NOT COMPUTED** (time-limit) | **NOT COMPUTED** |

For the two larger epochs, the all-pair cutoff count and the distance sum **interval** (not exact huge common denominator) were certified from exact input rationals via a validated fixedpoint sweep. Crosschecked the new algorithm against the all-Fraction exact computation on small samples and the previously completed all-Fraction A1024 result; verified no source change or aperture retuning. The first exact large-window accumulation was too expensive, and the initial all-three large probe timed out at A4096. Both failures remain disclosed in `LARGE_TIMEOUT_NOTE.md` and logs. The default replay intentionally excludes the unverified case; `large_probe.py --include-4096` attempts it with no promised result.

### Two-axis exploratory source return fibers

A64/128 exact all-Fraction fiber Q=1,2,4,8,16, and A1024/2048 certified fixedpoint Q-depth data are in `FINITE_RESULTS.json`/`FIBER_PROBE.json`. At A1024, G_gold(Q32) is in [0.02134068882798,0.02134068882799]; A2048, G_gold(Q64) in [0.01869222836734,0.01869222836735]. Q refinement monotone within each selected finite epoch as proved. These were not new blind mathematical holds and do **not** imply G_gold→0.

## Failures deliberately preserved

- `INITIAL_TEST_LOG.txt`: strict comparison of a rigorous rational interval to a float-rounded golden constant incorrectly treated equality after float rounding as a failure. Corrected test compares exact rational interval endpoints; no source or data changed.
- Previous exact all-Fraction cumulative distance sum timed out beyond moderate sample size even after O(AlogA) pair search. Fixedpoint interval algorithm avoids constructing the enormous common denominator and was exact-rational validated.
- `LARGE_PROBE_LOG.txt`: preregistered A1024/2048 pass, A4096 runtime limit reached without a certificate. No status promoted for A4096.

## Mathematical status and integration boundary

GA-01..GA-07 and the exact interval algorithm have written local derivations. The source-specific original-to-π `O(A^-2)` estimate is an unconditional comparison theorem, not the unproved source-selected spectral/near-pair saving. The golden/source identification is **observer-design** and not the native BBP silver field. No claim of external academic priority, full 12k+ SUCC root tests, provenance/foundations/ordinal root probes, new Lean/kernel theorem or exact-head hosted CI success. Review and keep DRAFT. No merge/tag/release/publication.
