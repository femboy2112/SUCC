# BBP carrier-return holonomy × real-circle energy: research-only child of #646

**Central result:** A 2-adic BBP source loop that closes at modulus `q=16^k` lifts to a nonzero original-four-pole-specific phase `11,11,3,3 mod16` as source time ranges through `n mod4`, while a selected irrational circle orbit must produce a finite phase-separation pulse of at least `1/17` in circle distance at arbitrarily late times. Combining them yields a signed, time-coupled **source-labelled interferometer** with an amplitude excitation floor and a scale-diverging response gain, but **no mean-density, fixed-Weyl-mode saving, R0 or pi-normality theorem**.

- `THEOREMS.md`: full mathematical derivations; effect of zero seed, circle metric, finite 2-adic return cocycle, odd-prime CRT and future Green tail; all hypothesis/quantifier/status firewalls.
- `loop_probe.py`: standalone standard-library exact four-pole rational/finite carrier/circle certificate, with full integer winding and odd-prime phase passport.
- `test_loop_probe.py`: 26 exact finite/unit/mutation controls, including π-return pulses and intentionally separated real-vs-2-adic states.
- `audit_algebra.py`: **independent** SymPy verification of the rational forcing derivative's four modular polynomial certificates.
- `FINITE_REPORT.json`: exact rational finite certificates, no digit fixtures.
- `TEST_LOG.txt` and `ALGEBRA_AUDIT.txt`: actual local output.
- `VALIDATION.md`: receipts, failure/recovery chronology, remaining unrun gates.
- `CLAIM_LEDGER.json`, `NEXT.md`: provenance and falsification gates.
- `make_report.py`: standalone exact rational finite certificate writer.

## Minimal reproduction

From this directory:

```sh
python -m unittest discover -s . -p 'test_*.py' -v
python audit_algebra.py
python loop_probe.py
```

The core module `loop_probe.py` is import-only by design. To regenerate the rational report:

```sh
python make_report.py > FINITE_REPORT.json
```

**Research guard:** All additions are new paths on a draft stacked from #646. No main changes, no source pole mutations, no release, no merge, no physical particle claims.
