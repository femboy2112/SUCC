# Validation and evidence scope

Research date: 2026-11-18, America/New_York. Base commit:
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`.

All commands below run from the SUCC repository root. The new research uses
exact integers and rational arithmetic; floating point is not used to certify
any phase interval, matrix order, source identity, or carry-word construction.
The universal results have paper proofs in the linked notes. Finite probes
calibrate their implementations and failure controls.

## Mandatory repository gates

| Command | Observed result | Receipt |
| --- | --- | --- |
| `python scripts/verify_provenance.py` | PASS: 72 items, including 17 byte-identical archives and 55 mechanical namespace migrations | `validation/provenance_final.log` |
| `python -m unittest discover -s tests -p 'test_*.py'` | 14,505 executed: 14,501 passed, 2 skipped, 2 environment errors; both errors resolved and affected modules rerun successfully | `validation/full_unittest.log`, `validation/environment_repair_rerun.log` |
| `python scripts/observer_foundations_probe.py` | PASS, exit 0 | `validation/observer_foundations.log` |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit 0 | `validation/ordinal_succ_report.log` |

The provenance gate verifies archival preservation. It does not certify the
truth of the research propositions. Existing foundation probes retain their
explicit unresolved/global-positivity flags; an exit-zero smoke probe does not
promote those flags.

### Full-run environment repair

The original full command completed in 1414.384 seconds with two errors. Its
unaltered log is preserved. `test_round2_registry` required three pinned Git
commits absent from the initial shallow clone; `git fetch --unshallow origin`
restored the history and all three objects were verified as commits.
`test_eodcs_meta_choice_descent` launched a script that could not import the
package from the scripts directory. The repository README's development setup
already specifies installation or `PYTHONPATH` pointing at the repository.

After those environment repairs:

```sh
PYTHONPATH=. python -m unittest tests.test_eodcs_meta_choice_descent tests.test_round2_registry -v
```

**All 17 tests passed in 0.591 seconds**, including both original errors and
the surrounding negative controls. No source code was changed for the repairs.
`validation/environment_repair.json` records the causes and restored identities.
Every non-skipped test now has a passing execution across the full run and this
targeted repair run. A second single clean run of the entire suite was not
performed; this receipt must not be described as one uninterrupted green run.
For reproduction, use full Git history and the README's package/import setup.

## New focused suite

```sh
python -m unittest discover -s tests -p 'test_causal_235*.py' -v
```

**29 methods passed** in the recorded focused run. The same methods are included
in full discovery through two root test modules.

| Area | Methods | Distinct checks and controls |
| --- | ---: | --- |
| Actual source clock factor | 8 | Literal four-pole Fraction states; inverse clock maps; complete CRT cycles and wraparound; compatible reduction; independently reconstructed Fibonacci pair; wrong cross-clock mutation; exact phase-distance intervals |
| Fibonacci construction | 9 | Polynomial intertwiners; integral operator-specific splitting and failed all-frame extrapolation; characteristic polynomial; matrix and seed orders; near-returns; source norm and source-mask mutation; divisible-by-5 singular case; observed filter latency |
| Mixed-place causal shadows | 4 | Arbitrary prescribed finite carry words; genuine rational 2-/3-adic state differences; adaptive local histories; exact-zero discriminator and bounded-height separation |
| Collatz and Euler controls | 8 | All 2,046 parity words of lengths 1–10 at two positive representatives; ordered offsets and cylinders; local error laws; expanding positive paths and signed fixed point; all-even quantifier counterexample; genuine versus fake Euler factor at 6 |

The exact output is in `validation/focused.log`. These are implementation
checks of scoped mathematical statements, not a computation of universal
Collatz termination or pi normality.

## Replayed prior artifacts and new receipts

The four files in `inputs/` are copied byte for byte from the earlier conversation
artifacts. Their original SHA256 hashes are recorded in
`validation/initial_artifact_hashes.json`; the final manifest records current
repository artifact bytes separately.

```sh
python research/2026-11-18/causal_235_local_dynamics/inputs/fibonacci_2x5x3_probe.py
python research/2026-11-18/causal_235_local_dynamics/inputs/test_causal_235.py
python research/2026-11-18/causal_235_local_dynamics/generate_receipt.py
python research/2026-11-18/causal_235_local_dynamics/probe_discriminant.py
```

- Prior Fibonacci probe: **711 exact checks passed**. Its existing finite
  denominator witnesses are preserved without upgrading their scope.
- Prior causal note: **6 test methods passed**. Its auxiliary group example is
  retained as provenance; the new Fibonacci construction supplies the requested
  operator and source map.
- Source energy: exact rational outer bounds for five shells with
  B=16,32,64,128,256, using the authentic source and the rigorous tail bound
  r(n+1)/15. See `validation/source_energy.json`. These indices lie in an
  already explored range; they are calibration, not an untouched holdout.
- Discriminant: exact base orders 3,2,5; ranks of powers of T-I modulo 5 are
  5,4,3,2,1,0; the fourth power's first column is (4,3,1,2,4). The separate
  Collatz fifth-prime discrete-log values are checked through 5^6. See
  `validation/discriminant_mechanism.json`.

## Provenance, independence, and limits

`validation/source_map.json` pins the base files and the exact reference-only
heads of recent PRs 657 and 665. Those open-branch notes were read for the source
filter and memory-conditional null correction; their code was not silently
merged into this branch. Preserved input notes retain their historical wording.

Parallel reviews used the same model family. Their different derivations and
implementations provide error checks, not independent external refereeing or
independent arithmetic data. No formal proof assistant certificate, universal
statistical result, or academic-priority claim is asserted.

The actual-zero phase-separation theorem is a composite extension of an existing
gap lemma; its universal conclusion follows from the displayed proof, not a
finite plot. It proves a limsup separation, without a positive lower density.
Mixed-place shadows change the seed and fail the exact U0=0 discriminator.
The observer factor recovers and compresses time; it creates no new real-phase
information. These boundaries are part of the result.

R0, pi normality, Collatz for every positive integer, and RH remain OPEN.
Hosted CI status is a separate observation from these local receipts and must
be checked at the published commit before it is described as passing.
