# Executed validation and exact scope

## Native gates

The actual full native run passed: **12,147 tests,1261.370 seconds, exit0**.
It used an explicit repository PYTHONPATH, fixing the prior round's invocation
failure without changing its frozen CLI or tests:

```sh
PYTHONPATH="$PWD" OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
/tmp/succ-learning-yoneda-venv/bin/python \
  -m unittest discover -s tests -p 'test_*.py'
```

All native inputs under tests/, scripts/, observational_succ/, formal/,
provenance/ and docs/ stayed unchanged from95d9860 throughout the run.
The new research namespace is tested separately. This successful new run
does not rewrite the previous round's genuine exit1 receipt.
The provenance, observer-foundations and ordinal gates each passed separately
and in the focused replay. `git diff --check` passed.

## Focused research validation

**31 focused tests passed:**25 new tests and6 inherited prime-resonance tests.
The focused runner completed14 commands with exit0 and5 matching mathematical
oracle payloads. Historical source/proof hash metadata remains in its original
receipts; the replayer compares that metadata separately where necessary.
Raw logs and command records are in [validation/focused](validation/focused/).

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
/tmp/succ-learning-yoneda-venv/bin/python \
  research/2026-11-08/complement_budget/validate.py \
  --output /tmp/succ-complement-focused
```

Add `--source` to reconstruct all four original source runs and complete
spectra. Add `--native` to repeat the native suite; the actual successful
native run above was executed separately, not silently inferred from this flag.

The source experiments check8 configurations over4 registered clocks, with
61,568 exact recurrence steps in aggregate and30,784 clean-interval
principal-part checks. Twelve independent modular power sums check source
checkpoints. The raw folded boxes, direct W enclosures, unwrapped/carry
hashes and exact final bounds are retained in results/.

Every one of738,840 complete DFT coefficients was evaluated by integer
outward arithmetic. Normalized error radii are below8e-12. This covers the
declared monomial menus only. A finite certificate is not an asymptotic proof.

## Separate algorithms and hostile checks

- Reduced-Fraction reconstruction checked3,290 original source states,
  3,290 folded values and4 direct Weyl means against the common-denominator
  implementation. Twelve full spectrum replays establish repeatability;
  78 direct interval sums bypass FFT and convolution.
- A separate MPIntervalContext at70 decimal digits evaluated66,000 direct
  terms at the6 held-out maximizing coefficients. All fit the root bounds
  and their stated radius gaps. See [HOLDOUT_REVIEW](HOLDOUT_REVIEW.json).
  This shares the source boxes and is not independent source provenance.
- Hostile FFT checks compare65 outputs with independent direct sums and
  reject125 sign/scaling mutations. There are240 exact dual-bound checks.
- Nonlinear model-law checks solve750,180 exact finite transport problems,
  producing6 nonvacuous large-coset certificates. Source-law checks include
  8 outward configurations with q=2,4,12,2162 exact cocycles,2166 principal
  parts and12 independent modular sums.
- A separate CBM5 review checks313 polynomial-family escapes,9 rotated
  discrepancies and6 distance cases, including a nonvacuous arithmetic bound.
- The unit-chirp front checks36 outward approximation bounds,3185 rational
  cocycles and rational coherent controls. The hostile folding front checks
  348 exact cyclotomic identities,161 split clocks and a complete p4409 source.

Agents used distinct assignments and implementations but share a model family
and workspace. No external refereeing is claimed. The new analytic theorems
are paper proofs using explicit classical inputs, not newly kernel-checked
Lean theorems. Existing formal/source files are untouched.

## Performance repair and receipts

The first large holdout run was stopped with exit130 before it emitted a
source receipt or phase output. Replacing repeated full-integer division by
the algebraically identical literal-carry recurrence made the run practical.
All three complete development source payloads replayed identically afterward.
The successful holdout records the new implementation hash. See
[STREAM_REVIEW](STREAM_REVIEW.md); the interrupted raw log is retained.

GitHub CI is separate from local validation. Its final-head state is reported
in the PR coordination comment; no local pass is called a hosted CI pass.
The exact source contract and live repository pins are in PROVENANCE.json.

Pi base-16 normality: OPEN. RH: OPEN.
