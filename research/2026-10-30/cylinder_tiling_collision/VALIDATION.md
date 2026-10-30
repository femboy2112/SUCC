# Executed finite validation

Work directory `/mnt/data/succ_cylinder_collision`; parent baseline read from live PR #405 and Main XVI, with PR #392 two-triangle research read as a separate auxiliary model. No historical source edited.

Command:

```
python -m unittest discover -v -p 'test_*.py'
```

**16/16 pass**, raw output `tests.log` preserved; standard-library `Fraction`, `Counter`, digit-word enumeration only. Main source tests: exact four-pole recurrence and positive monotonic forcing; exact finite tail conjugacy; certified original hexadecimal prefix `243F6A88`; 79 source-selected shifted-word overlaps for m=2,3,5; 256-position exact finite cylinder census; quadratic refinement and all 15 nontrivial Walsh characters; Haar overlapping-word equality enumeration; zero, biased and de Bruijn adversaries; source-to-tent finite Lipschitz comparison.

Reported exact source calibration for `N=256`:

```
m=1: Q=2117/2048, distinct=16
m=2: Q=31/16,   distinct=164
m=3: Q=17,      distinct=248
```

Haar expectations for N=256 are `1+15/256`, `1+255/256`, `1+4095/256` respectively. The last level has 4096 cells but only 256 time observations; its diagonal collision floor is 16, so it is non-diagnostic asymptotically.

**Proof boundaries:** the 16 unit tests check exact finite statements and independently known calibrations. The collision-entropy implication is a paper proof using classical entropy, not a numerical theorem or new Lean proof. The all-N source-to-kernel transfer is an elementary analytic proof using source tail positivity, not established by testing a finite 28-point sample. No claimed proof of selected subexponential collision concentration, fixed-h Weyl o(N), normality or RH.

Do NOT count this as a run of the main SUCC 10,008-test suite, hosted CI, provenance gate, core Lean, or independent external review. Those must be separately executed on the actual PR head if merged/integrated.
