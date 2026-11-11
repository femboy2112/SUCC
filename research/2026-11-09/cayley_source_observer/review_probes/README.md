# Reproducible independent review probes

`parity_boundary_review_probe.py` is a **new reconstruction and current rerun**,
not the original temporary script behind `PARITY_INDEPENDENT_REVIEW.md`. The
original script and stdout were not persisted; only the written review survived.
No historical output has been recreated or backdated.

The review recorded the sine denominator family, Taylor terms, 16-bit setting,
100-digit diagnostic precision and 3,230 parameter cases. This script explicitly
uses numerators `-d,...,d` for each documented denominator `d`, consistent with
that record; identity with the lost source cannot be attested. It also reruns
the recorded 2,145 exact orbit cases: numerators `0,...,d-1`, denominators 1
through 65, seven sampled steps plus the final endpoint, and recursion depth
four. Counts include repeated rational values under different numerator and
denominator parameterizations.

The sine comparison is an independent high-precision **diagnostic**, allowing
`1e-90` for mpmath arithmetic at 100 decimal digits. It is not a rigorous oracle
or a replacement for the Taylor/rounding proof. The orbit probe uses exact
rationals and explicitly enumerates all sixteen inverse fibers, retaining the
fourteen other fibers and both endpoint effects. Its results certify only the
declared finite cases.

The review's original 1,750-case Fejer grid and stdout are unavailable. They are
**not reconstructed or rerun here**. The committed hostile unit tests and the
separate analytic proof retain their own authority.

Run from the repository root:

```sh
python research/2026-11-09/cayley_source_observer/review_probes/parity_boundary_review_probe.py
```

`CURRENT_RERUN_OUTPUT.json` is the actual stdout captured from the current run.
Its UTC timestamps, environment versions and source hashes identify that run;
they do not convert the earlier narrative review into an archived execution log.
