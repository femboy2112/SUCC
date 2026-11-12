# Prime recoherence — exact experiment and outstanding gates

**Date:** 2026-11-12. **Tested isolated overlay:** `/mnt/data/prime_recoherence_research` on Python 3.13.5, stdlib only, outside full SUCC checkout. Test command:

```sh
cd /mnt/data/prime_recoherence_research
python -m unittest discover -s tests -p 'test_prime_recoherence.py' -v
```

**Observed:** 19 tests, all passed; 0 errors / failures / skips. Every calculation uses `fractions.Fraction`. Exact partial-trace density matrices independently verify marker-overlap formulas and the conditional-unitary cycle. A 144-case control sweeps two observer controls, three exact 2×2 rotations, and 25 branch-amplitude pairs (excluding the zero ray) to compare system/environment reduced purities and norm conservation. Tests also cover an orthogonal record in 125 signed/zero independent-bucket combinations, q-rate boundaries, real-phase versus purity separation, genuine prime-power support, and the fake-6 mutation.

**Authority:** Pure finite quantum toy results are exact computations backed by elementary algebraic paper derivations. The finite tests do **not** establish quantum physical dynamics, source-observer semantic identity, actual entropy production in the RH trace formula, or global all-test Weil positivity. No numerical black-box eigenvalue computation, Lean, physical experiment, or new RH theorem. The file hashes and pushed commit SHA will be checked after pushing.

**Mandatory integrated repo replay (not executed in this isolated overlay):**

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

For next research campaign, preregister one authentic prime-power/Gamma source map, source-independent dummy/composite controls, two disjoint source test supports, phase conventions, exact central contact, a sign-sensitive target, and a falsification criterion. Refuse to promote generic density-matrix positivity to Weil positivity.
