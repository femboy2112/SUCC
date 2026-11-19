# Validation receipt

## Authority and scope

The universal results are paper proofs in the four theorem documents.
Exact computations corroborate them on declared finite domains; the tests
are not the infinite lift. Constructor, translator, adversary and root share
model/source provenance. No independent human referee or new formal-kernel
proof is claimed.

This is additive to main commit
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`. Existing source, production
code, historical theorem files, frozen imports and existing tests are not
changed. The new discoverable test imports only the new research probe.

## Final focused and differential checks

**PASS: 16 focused unittest cases.** The exact command and full output are in
[focused_tests.log](evidence/focused_tests.log):

```sh
PYTHONPATH=. python -m unittest tests.test_bbp_two_three_causal_transport -v
```

They cover original rational source moments, cyclic versus causal integer
products, all-block unit-minor/Smith certificates, literal-Q constant mode
and cofactors, sharp local inverse norms, compact ternary-height strata,
causal incoming-state error, actual Collatz cylinders and memory, the recovered Fibonacci module, 625 quartic-lift identities, and
negative controls for source mutation, discarded closure, lost chronology,
short histories, and local seed aliases.

The [finite probe](evidence/probe.json) records 768 authentic source indices,
48 window pairs, 5,460 positive valuation words, 30,948 terminal-memory
identities, and 30 sharp-depth counterexamples. Additional focused tests
check all 1,536 initial source indices and block dimensions through 32.

**PASS: independent local implementation, rerun by root.**
[independent_local_audit.py](independent_local_audit.py) imports no SUCC
arithmetic module. It checks the literal Fraction recurrence through 6,144
and a separately implemented modulus-81 recurrence through 1,000,003,
including fresh holdouts 4,096--6,144 and 180,002--1,000,003. It checks 28
boundary/window pairs, all eight entries of the exceptional mod9 certificate,
the full-history null, and a sign mutation whose height-only test fails to
detect the change. The leading-unit witness detects it. Root's rerun exactly
matches the [committed receipt](evidence/independent_local_audit.json), including
the script SHA-256.

**PASS: separately entered matrix and source audits.** The
[hostile review](HOSTILE_REVIEW.md) records a distinct scaled source recurrence
on indices 769--100000, triangular-recursion inverse coefficients through
dimension160, nilpotent determinants/ranks, and paired-clock Smith checks.
The late all-block theorem additionally has two paper derivations: monic
polynomial cokernels and an integer unit minor plus inverse denominator.
Literal-Q Smith forms and cofactor values were independently checked at
dimensions8,16,24. These latter finite calculations are separate from the
universal module proof.

**PASS: rational snapshot periods.** [Snapshot receipt](evidence/snapshot_periods.json)
checks the first32 exact orders using literal source fractions, an order
routine, and separate prime-divisor minimality tests. The general lower
bound is proved from the source height and elementary lifting, not inferred
from those32 examples.

## Required repository gates

The three non-suite commands completed successfully:

```sh
PYTHONPATH=. python scripts/verify_provenance.py
PYTHONPATH=. python scripts/observer_foundations_probe.py
PYTHONPATH=. python scripts/ordinal_succ_report_probe.py
```

All 72 preserved provenance entries were verified. Exact return codes and
outputs are recorded in [required_probes.json](evidence/required_probes.json)
and the corresponding committed logs.

**PASS: full inherited repository suite plus the initial 8 new cases.**
The discovery process ran **14,484 tests in 1295.032 seconds**, with
2 skips and no failures or errors. The process returned 0 and did not
time out. See [full_suite.json](evidence/full_suite.json) and the
[complete suite log](evidence/full_suite.log).

```sh
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  python -m unittest discover -s tests -p 'test_*.py'
```

The broad suite began with the first 8 new test methods loaded. Eight additional
focused methods were added while it ran, without changing existing production
or test files. The final 16-case focused run above covers the completed new
code. Accordingly, a successful broad run is reported as the full inherited
suite plus the initial focused cases, and is not mislabeled an execution of
all final new test methods in that same process. Final-source hosted CI is a
separate check and is not presumed successful.

## Reproducibility and limitations

The environment uses Python 3.12.14, numpy 2.3.5, scipy 1.17.0, sympy 1.14.0,
and mpmath 1.3.0, satisfying the repository's declared test dependency ranges.
The full suite is run with `PYTHONPATH=.` propagated to subprocesses and
`OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`.

The source snapshot pins actual read files and donor heads. The implementation
manifest hashes the final research Python and new test bytes. Paper proofs
were checked for quantifier, domain and source-type distinctions. No CI pass,
merge, release, normality theorem, universal Collatz result, or RH proof is
inferred from these receipts.
