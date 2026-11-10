# Executed validation and exact scope

The three research fronts plus root produced24 focused tests: root6,
quotient7, gamma7, hostile4. All passed. The full fresh replay executed
15 commands successfully and compared10 retained mathematical payloads
successfully. Command wall time totaled117.814seconds. Actual commands,
return codes, hashes and logs are in [validation/replay.json](validation/replay.json).

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/quotient_signal/validate.py --output /tmp/succ-quotient-final-replay
```

After this full replay, a narrow gamma serialization cleanup replaced an
import-time decimal-string-limit change with hexadecimal source hashes.
Seven gamma tests and the entire gamma oracle were rerun successfully at
the final code. Every mathematical field matched the full replay; only the
declared source-hash encoding and code hashes changed. Receipts:
[final gamma tests](validation/gamma_final_tests.json) and
[final gamma oracle](validation/gamma_final_oracle.json).
The import also preserves the process integer-string limit4300.
This is not represented as another complete replay of unchanged fronts.

| Evidence | Executed result | Authority boundary |
|---|---|---|
|Focused tests|24uniquePASS;7 gamma tests repeated after cleanup|Finite implementation checks|
|Weighted quotient oracle|28families,3598 exact checksPASS|Gaussian rational finite algebra|
|Hostile finite oracle|327680 exact checksPASS|Separate fourth-root/Gaussian implementation|
|Continuum calibrations|24 rational interval rowsPASS|Independent Machin/Taylor implementation; all-M theorem is paper proof|
|Gamma calibration|5cutoffs,1031pointwise/source checks,185kernel checks,192seed checks,3mutated-source rejectionsPASS|Rational enclosures and exact identities; all-N proof separate|
|Source quotient probe|300 configurationsPASS interval consistency; outward W enclosures retained|5epochs, h1,3, d0..4, two origins, three source/control families|
|Independent source phase readout|120rows,2760 scalar containmentsPASS at100digits,6fresh modular checks|Numerical cross-check, tolerance1e-80; shared source engine, independent phases/direct complements/grouping|
|Root source checks|15 independent modular-power state samples and30 direct complementary-phase samplesPASS|Unwrapped/carry hashes retained for every epoch|
|Provenance gate|PASS|`scripts/verify_provenance.py`|
|Observer foundations gate|PASS|`scripts/observer_foundations_probe.py`|
|Ordinal report gate|PASS|`scripts/ordinal_succ_report_probe.py`|
|Native suite|NOT RERUN; prior12147PASS reused with unchanged-input check|No new native pass claimed|
|Lean|No new Lean/kernel claim|Analytic and quotient theorems are paper proofs|

The native reuse compares `observational_succ`, `tests`, `scripts`, `formal`,
`provenance`, `docs`, `AGENTS.md`, `pyproject.toml`, and requirements files
against the previously tested pinned main `d32342d375f44ddf62221ad6aff2f534abdc0a03`.
The earlier full-suite receipt is
`research/2026-11-07/learning_yoneda/validation/native_suite.json`.
This branch's native code remains on that baseline even though live main has
advanced; this receipt does not certify Main XXI integration or a future merge.

The source protocol was committed before execution at143fe29d. The gamma
subtask wrote its preregistration before its finite oracle, after its symbolic
derivation; it was not separately Git timestamped before that subtask ran.
Development and holdout cases are labeled in the raw results. Temporal ranges
overlap previous source experiments; they are not independent source datasets.
No asymptotic exponent or constant was selected by fitting these values.

Three independent assignments and cross-reviews share a model family and
repository source. They are not external scholarly refereeing. Exact model
identities, rigorous finite interval enclosures, high-precision numerical
containment, paper proof, and an open global theorem are kept separate.
Errors found during implementation are in the claim/attempt ledger.

Fresh main was fetched before publication and remains
`43a607818907120d4cdab73d240f5b4d7700b63f`; the canonical forcing and selected
orbit files are byte-identical to this branch. The Main XXI handoff was read.
No rebase, merge, force-push, source mutation or shared catalog edit occurred.
All additions are under this dedicated namespace. Hosted final-head CI is
reported separately through draft#544; local results do not certify it.

**Pi base-16 normality: OPEN. RH: OPEN.**
