# Front C/F/G validation

On the isolated child of `c9dfcdf057c4870f113e898464e4821c2ff5fedf`:

```
python research/2026-11-04/critical_chirp_source/front_cfg/probe.py
Ran 7 tests in 0.429s
OK

python research/2026-11-04/critical_chirp_source/front_cfg/probe.py --receipt
python research/2026-11-04/critical_chirp_source/front_cfg/probe.py --verify
CFG_FINITE_RECEIPT_VERIFIED
```

All commands exited zero. `FINITE_RECEIPT.json` is the exact deterministic
output of `--receipt`. At the three fresh radix fixtures, 47/47, 123/123 and
203/203 good positions satisfied their exact rational phase-arc certificate.
The 0, 4 and 24 excluded switch positions fit the proved budget. Reversing
the digit orientation rejected all those good-position certificates, with
every rejected index retained in the receipt.

The independent forcing formulas, tail intervals, local half-turn Taylor
remainder and literal radix transport are exact arithmetic checks. A terminating
finite digit fixture is **not normal**; no test or receipt claims otherwise.
CFG-1/2's normality and their all-epoch asymptotic conclusions come from the
paper proofs, not finite extrapolation. These are finite component holdouts,
with surrogate frequencies and explicitly identified arbitrary radix depths.

No failed test occurred in this front's first execution. The inherited native
suite, hosted CI and external proof review are coordinator-owned and are not
claimed by this front. The primary literature and pinned #496 proof were
read live; the proof itself needs only the source completion, CC-01, elementary
radix arithmetic, calculus, and classical existence of a normal number.
