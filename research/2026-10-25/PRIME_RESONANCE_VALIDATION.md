# Prime resonance: validation and authority receipt

Date: 2026-10-25. Pinned parent PR #296:
`461942c0bf616518e668d236d1c6b1596665a7dd`.
Branch: `research/pi-prime-clock-resonance-killer-2026-10-25`.
All changes are additive; imported archives, main, the concurrent matrix
branch, and shared frontier/architecture files were not edited.

## Actual local checks

| Check | Observed result |
|---|---|
| Native parent source/projection/matrix integration baseline | 34 tests passed |
| New research tests, final modules | 40 tests passed |
| New research tests plus claim namespace guards | 55 tests passed |
| Full `unittest discover` sweep | 8,390 tests in 806.927 seconds; 8,389 passed, one subprocess import error |
| After correcting the local editable-package installation | All 11 tests in the affected inherited module and all 40 final research tests passed: 51/51 |
| `scripts/verify_provenance.py` | SOURCE_PROVENANCE_VERIFIED: 72 items, 17 byte-identical archives and 55 mechanical migrations |
| `scripts/observer_foundations_probe.py` | Exit 0; raw output preserved |
| `scripts/ordinal_succ_report_probe.py` | Exit 0; raw output preserved |
| New source-hashed receipt `--write` then independent `--verify` replay | Exact match; eight prime windows, source-only controls and certified intervals |
| Compileall for all four new modules and the replay script | Exit 0 |
| `formal/PrimeClockProjection.lean`, Lean 4.14.0 | Exit 0; three principal theorem axiom reports: propext, Quot.sound |
| Wrong-clock-index Lean mutation | Rejected, exit 1, explicit unproved equality; log preserved |

**Full-sweep qualification:** the inherited
`test_eodcs_meta_choice_descent.TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count`
launches `scripts/meta_choice_descent_probe.py` as a subprocess. The first
local environment had the numerical dependencies but not an editable install
of this checkout; that subprocess raised `ModuleNotFoundError: observational_succ`.
Running `pip install --no-deps --no-build-isolation -e .`, matching the package
installation already used by hosted CI, fixed it without changing repository
code. The affected module and all final new modules were rerun successfully.
The initial full discovery imported the earlier version of the new modules;
the later focused runs cover their added gcd/inverse/collision checks.
**There was no second clean one-shot full sweep.** The failed run and corrected
rerun remain separate evidence; the initial error is not silently relabelled.

Runtime: Python 3.12, mpmath 1.3.0, NumPy 2.3.5, SymPy 1.14.0,
SciPy 1.17.0. Only exact integer/Fraction computations and explicitly
certified rational character intervals are proof-critical in the new code.
No shim supplied the original BBP source or the natural/integer carriers.

Raw logs are under [prime_resonance_validation](prime_resonance_validation/).
The deterministic mathematical receipt is
[PRIME_RESONANCE_RECEIPT.json](PRIME_RESONANCE_RECEIPT.json).
Its replay hash is
`dc2a29b1006a9c8f3eae2646677a5326b2ac503d9067d64cf1d78acc02bb2714`.
The receipt contains SHA-256 hashes of nine construction/authority inputs;
replay fails if those sources or exact outputs change.

## Reproduce

From the repository root, install the repository and declared test extras,
then run the four required AGENTS checks. The new focused suite is:

```sh
python -m unittest tests.test_prime_clock_resonance tests.test_bbp_resonant_lags tests.test_bbp_resonance_controls tests.test_bbp_resonance_collision -v
python scripts/prime_clock_resonance_probe.py --verify
lean formal/PrimeClockProjection.lean
```

The normal Lean replay needs no custom build. This environment required a
path-discovery compatibility shim for Lean's own executable lookup; its exact
code and downloaded compiler provenance are in
[PRIME_CLOCK_FORMALIZATION.md](PRIME_CLOCK_FORMALIZATION.md). It does not
modify the proof kernel or supply theorem facts. The negative mutation
replaces the contraction target's `u j` by `u (j+1)` and must be rejected.

## Hosted status and mathematical scope

At the start and final pre-publication recheck, parent PR #296 still had its
pinned head. Its hosted checks were three successes and one **cancelled**
Observational SUCC validation run. None was promoted to a full success.
This branch's own hosted checks are separate from the local checks above;
inspect the draft PR at its actual head. Publication is batched as one new
branch update and one stacked draft PR; no workflow restart is requested.

The paper inequalities and asymptotics have explicit derivations and
adversarial audits. The Lean authority covers only the declared finite
algebraic kernel. The asymptotic signed decay, all-prime inverse-arc avoidance,
and prescribed-scale authentic collision saving are UNVERIFIED. This round
does not prove pi normality, RH, physical claims, or logical independence.
