# Integration instructions — additive research only

Start from a clean non-main branch at the recorded #447 head, or first audit any
newer integration and update the source map. Do not overwrite existing production,
archive, proof authority, Lean, workflow, license or historical claims.

The provided patch adds this research directory and
`tests/test_categorical_source_gluing.py` only. Inspect paths with
`git apply --stat`, then `git apply --check`. Apply on a research branch, not main.
No commit or publication authorization beyond research is inferred.

## Required local checks

```sh
python research/2026-11-01/categorical_source_gluing/cover_certificate.py
python research/2026-11-01/categorical_source_gluing/independent_polynomial_oracle.py
python research/2026-11-01/categorical_source_gluing/frame_and_monodromy_audit.py
python -m unittest discover -s tests -p 'test_categorical_source_gluing.py' -v
```

Then run the actual existing category adapter test (it is skipped only where the
full `observational_succ` package is absent), and the repository-mandated checks:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Record interpreter/dependency versions and exact commit. Passing existing Lean CI
would not formalize the new paper proofs. Do not change canonical theorem status.

## Reuse the existing categorical machinery

`repo_adapter.py` imports FiniteCarrier, Instrument, BeliefGame and
ObservationPathCategory from the existing spine. The local SourcePath dataclass is
only an exact source-domain witness validator; it is not a competing general
category kernel. Any full integration should use the existing FiniteFunctor and
CertifiedSourceMorphism checks, including public outputs and enabledness.

## Next verdict-changing work

1. Formalize the stdlib-checkable polynomial certificate and all-horizon positive
   coefficient argument, with exact theorem-name/type binding.
2. Construct the actual source-differential/metric-channel amplitude intertwiner,
   or a source-specific signed trace estimate on the completed Fourier object.
   Neither one follows merely from calling the diagram a colimit or a stack.
3. Test against the correctly typed countermodels: false sheet glue, phase-sign
   mutation, wrong dual embedding, discarded radix branches, original real-model
   coherent irrational seed, and finite-source mutants. Do not pretend an
   out-of-domain counterseed satisfies the finite-register contract.

A successful analytic upgrade must exploit the original source AND the admitted
zero-seeded arithmetic state to bound the distinguished harmonic point, not replace
it by an average over the compact dual.
