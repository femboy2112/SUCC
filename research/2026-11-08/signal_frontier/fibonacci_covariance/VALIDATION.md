# Fibonacci observer validation and limits

The paper gives FC1–FC10; it does not claim source-selected cancellation.
The oracle implements a declared Fibonacci origin menu and tests its actual
original-source signed response. Source time and observer clock are separate.

Executed:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/succ-learning-yoneda-venv/bin/python \
  -m unittest discover -s research/2026-11-08/signal_frontier/fibonacci_covariance \
  -p 'test_*.py' -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/succ-learning-yoneda-venv/bin/python \
  research/2026-11-08/signal_frontier/fibonacci_covariance/observer.py \
  --output research/2026-11-08/signal_frontier/fibonacci_covariance/results --source
```

- Seven tests pass, including independently enclosed signs in Q(sqrt5),
  exact floor/cell boundaries, the source instrument's cell algebra and
  actual interval-enclosed Fourier polynomial energies.
- 57 exact Fibonacci return/discrepancy checks, k=2..20.
- 1,206 golden cell labels agree with a separate rational enclosure method.
- 32 actual band-limited signal energies lie rigorously inside the stated
  frame interval bounds. These use outward phase rectangles, not an ordinary
  floating-point eigenvalue assertion.
- 72 original/matched/synthetic source observer cases pass the finite
  calibration bound at A149,673; h1,3; M4,16; q13,55,233.
- Six source states are separately checked by modular power sums.
- All72 source Weyl rectangles match the independently executed parent
  origin-sweep instrument. The source and phase code is shared, so that
  agreement is a consistency check, not independent source authentication.
- The homometric directed difference histogram and its lack of
  translation/reflection equivalence are checked with exact integers.

`results/ORACLE.json`, `SOURCE_*.json` and `SUMMARY.json` are emitted by the
same documented command. Summary midpoints are descriptive only; the raw
files retain outward rectangles and certified comparisons. The protocol was
written before execution but was not separately committed by this worker.
The source epochs overlap the parent's already-observed epochs; the new
holdout is an observer/protocol holdout, not independent source data.

An initial fixture used `(-1)**m` with negative m, causing Python to produce
float before Fraction construction. The test rejected it with TypeError;
`INITIAL_FAILURE.log` retains that failure. Integer parity replaced it, and
the complete test and source/oracle commands were rerun. No theorem or bound
was changed to accommodate data. The final summary generator was integrated
into the producer and the complete producer was rerun after that change.

The sibling referee independently checked the paper proof and numerical
frame singular values. Those independent numerical checks remain numerical
corroboration; they are distinct from this worker's outward finite energy
certificates. No Lean proof, global native-suite pass, external referee or
worldwide novelty is claimed by this front. Root records repository gates.

For reproduction into a fresh output directory use the same producer command
with `--output /tmp/succ-fibonacci-clock-replay --source`. It compares source
Weyl rectangles to the pinned parent origin receipts in this repository.
