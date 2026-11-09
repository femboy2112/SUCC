# Validation and provenance — prime-birth carry junction

**Research-only; no full analytic Lean proof.** New code is standard-library only, exact Fraction until complex-angle diagnostics. Source is imported unchanged from `observational_succ.duck_bbp.forcing` and explicitly cross-checked as the sum of three positive differences. The exact p residue of the full **unwrapped** original recurrence is checked independently against the channel recurrence at calibration epoch A=100.

The research began with exploratory source epochs A=100,128,256,512,1024 (balanced p=233,313,617,1217,2473). A *fresh* holdout protocol was committed to GitHub at `4bfcc9b0cb4162b3695f5898b06dbfb3112724a7`, **before** choosing p and inspecting source traces at A=2048. The heldout deterministic selector picks the valid p=4937, m=617. All tests at previous epochs and the new holdout retain exact source and literal carry values.

Reproduce with root repository PYTHONPATH:

```
python -m unittest discover -s tests -p 'test_prime_birth_carry.py' -v
python research/2026-11-08/prime_birth_carry/experiment.py --output /tmp/PBC_2048_replay.json
```

The second command's output can be compared byte-for-byte to `FINITE_RECEIPT_2048.json`. Tests include original-pole source algebra, first-shell event passports, direct unwrapped p-residue oracle, exact twin-clock/cofactor and 3-channel junction equations, rational interval junction distributions (two independent methods), sign-changing parity lines, 16^-n boundary telescope, complex temporal-line DFT, unit-circle resolvent nonzero multiplier, prime/full real carry difference, and two p-integral wrong-seed controls. Float comparisons verify implementation only and must not be promoted to interval-certified asymptotic signs.

**Initial holdout runner failure (preserved):** the exact A=2048 dyadic seed contains >4300 decimal digits. Attempting `str(Fraction)` tripped Python's integer-to-decimal safety limit before writing the receipt. The repaired implementation hashes the **hexadecimal numerator and denominator** without altering the frozen source horizon, selector, or metrics. The completed receipt still includes the dyadic sign certificate and real carries all 15.

**Epistemic scope:** BEC-03's prime selector, BEC-04's incomplete-period bound and Cochrane–Pinner are externally sourced paper inputs (not rerun numerical tests). The four rational junction laws and cochain identities are exact paper derivations backed by independent Fraction implementations. The finite sample does not prove an all-A rate on the real complementary phase or normality. Full project validation requires `python scripts/verify_provenance.py`, `python -m unittest discover -s tests -p 'test_*.py'`, `python scripts/observer_foundations_probe.py`, and `python scripts/ordinal_succ_report_probe.py`; do not claim these were run merely because focused checks pass. GitHub CI is a separate exact-head gate.
