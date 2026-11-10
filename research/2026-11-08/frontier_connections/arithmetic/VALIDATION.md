# Arithmetic-front validation

All commands run from the repository root using the existing environment
`/tmp/succ-learning-yoneda-venv/bin/python`; no package installation occurred.
New files are confined to this arithmetic namespace. No native source,
archived proof, frozen contract, shared roadmap or catalog was modified.

## Focused tests

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
/tmp/succ-learning-yoneda-venv/bin/python -m unittest discover \
  -s research/2026-11-08/frontier_connections/arithmetic -p 'test_*.py' -v
```

**10 tests PASS**, exit0, raw [tests.log](tests.log).

- 165 nonempty weighted supports: exact Fraction fourth-moment collision identity.
- 90 degree3/4 weighted collision fibers: exact Newton/multinomial identity.
- 606 off-diagonal pairs: exact tomography inverse equations.
- 3,000 exact affine exponent comparisons.
- 155 complete small-field coefficients enclosed by rational direct phases.
- The same155 integer centers independently matched Python arbitrary-precision
  scalar contractions, without NumPy's matrix multiplication.
- Characteristic2 failure, two-point tomography ambiguity, arbitrary phase
  rotations, wrong quadratic sign and wrong normalization are explicit controls.

## Complete source menu

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
/tmp/succ-learning-yoneda-venv/bin/python \
  research/2026-11-08/frontier_connections/arithmetic/mixed_quadratic.py \
  --source research/2026-11-08/complement_budget/results/source_1103.json \
  --output research/2026-11-08/frontier_connections/arithmetic/MIXED_QUADRATIC_1103.json
```

**Complete calculation PASS**, exit0. Per run38,878,562 coefficients are
covered (2frequencies×4409²), with uniform error<3.104e-7 and explicit
int64 bounds below4.963e18. The original exact source was already reconstructed
and audited in the preceding complement-budget round. Here its raw receipt
is hashed and reused, without fresh-source or independent-source claims.

The original experiment protocol was committed and pushed by root at
`3a1d9b63` before evaluation. The five fixed coefficient probes were selected
in the instrument before source-menu evaluation; extrema are selected by the
completed scan and labeled as such. These coefficient probes are not a fresh
source holdout.

After hostile review, two generic input guards were added (bounded modular
index products; quantized input-center range). The fixed p4409 calculation
already satisfied them. A complete replay was executed after the guards.
The initial receipt/log are retained, and [GUARD_CHANGE.patch](GUARD_CHANGE.patch)
reconstructs the exact initial instrument from the final code. No source,
precision, menu or selection criterion changed. Mathematical replay equality
is recorded in [REPLAY_COMPARISON.json](REPLAY_COMPARISON.json).

## Separate interval implementation

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
/tmp/succ-learning-yoneda-venv/bin/python \
  research/2026-11-08/frontier_connections/arithmetic/independent_review.py
```

**14 probes /7,714 direct terms PASS**, exit0. The independent implementation
uses70-digit `MPIntervalContext`, recomputes the coset via modular powers,
and uses neither the Taylor root table nor the matrix algorithm. It shares
the original source boxes. It verifies reported centers, not the entire
exhaustive maximum independently. The separate exact scalar contractions
on all small-field coefficients address matrix-algorithm fidelity.

[Independent receipt](INDEPENDENT_REVIEW.json) records exact rational intervals,
containment, input and code hashes. The root coordinates additional hostile
review and repository gates. This lane does not claim a newly rerun native
full suite, new Lean formalization, hosted CI success, external academic
refereeing, or an asymptotic original-zero theorem.

**Pi base-16 normality: OPEN. RH: OPEN.**
