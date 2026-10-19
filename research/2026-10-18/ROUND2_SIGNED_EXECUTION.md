# Signed-source Round II execution record

Base: `f309d9104ba480c1999c962af1df7c50f19e1bfe` (PR177).
Branch: `research/round2-signed-2026-10-18`.
Interpreter: `/tmp/succ-institute-venv/bin/python`, CPython 3.12.3,
mpmath 1.3.0. Exact mathematics uses `fractions.Fraction` and integer square
roots; no floating-point sign test supplies proof authority.

## Completed source replays

```sh
/tmp/succ-institute-venv/bin/python scripts/full_prime_resolvent_probe.py --source --J 8 --M 80 --output research/2026-10-18/ROUND2_FULL_PRIME_J8.json
/tmp/succ-institute-venv/bin/python scripts/full_prime_resolvent_probe.py --source --J 24 --M 192 --output research/2026-10-18/ROUND2_FULL_PRIME_J24.json
```

Both exited 0. J8: 18.6703s, 27,400KiB; J24: 177.0900s, 43,316KiB.
Each process had hard 240 CPU-second and 1 GiB address-space limits. Both
parity gains are exactly positive definite at both depths. Both new lower
blocks remain negative definite. The result is a strict sufficient-bound
improvement; the actual source energy and S4 sign remain unresolved.

The preceding inline J8 attempt completed its mathematics but failed while
serializing an audit Fraction with more than 50,000 decimal digits.
`receipts/round2-full-prime-first-attempt.log` preserves that failure.
The successful CLI exports those enormous audit quantities as outward
rational brackets plus hashes of their exact integer encodings. All Schur,
Gram and gain matrices remain full exact rational strings. No sign decision
uses a bracket display or hash as a substitute for the exact calculation.

## Local validation

```sh
/tmp/succ-institute-venv/bin/python -m unittest discover -s tests -p test_full_prime_resolvent.py -v
/tmp/succ-institute-venv/bin/python scripts/verify_provenance.py
/tmp/succ-institute-venv/bin/python scripts/observer_foundations_probe.py
/tmp/succ-institute-venv/bin/python scripts/ordinal_succ_report_probe.py
/tmp/succ-institute-venv/bin/python scripts/full_prime_resolvent_probe.py --audit-capsules
/usr/bin/time -v timeout 1200 /tmp/succ-institute-venv/bin/python -m unittest discover -s tests -p 'test_*.py'
```

Focused 8 tests: PASS, 7.713s. Provenance:PASS, 72 imported items, 17 byte-identical
research archives, 55 mechanical namespace migrations. Observer, ordinal and
existing-schema capsule probes: PASS. Raw outputs are retained in `receipts/`.
The capsule checker verifies structure and hashes and explicitly issues no
semantic proof authority.

Full suite: **PASS**, 5,302 tests in 555.695 test seconds; elapsed wall time
9:21.58, peak 319,076 KiB resident memory, exit 0. The 1200-second wall
timeout did not fire. No skips or failures were reported.

The full suite initially inherited 8 numerical-library threads. When this
was observed, all existing threads were pinned to one CPU for the rest of
the run; `receipts/round2-full-suite-affinity.json` records the action.
The scientific source probes used single-process exact arithmetic. No new
Lean theorem is supplied by this signed-analysis stream, and no Lean kernel
status is claimed for its paper proofs. Hosted CI status is reported by the
PR; local execution alone does not establish hosted success.

## Independent review and limits

Hostile review is recorded separately at commit
`da239e2370df7aafc1d8404b86e7213e3febeb46`,
`research/2026-10-18/ROUND2_HOSTILE.md`. Its exact J8/J24 receipt and
implementation hashes match this branch. It rederived the core, Bessel,
source-normalization, inverse and correlated-error arguments and reconstructed
the saved matrix algebra independently. It did not repeat the full source
replay or independently audit every inherited finite interval primitive.
The manuscript's explicit fixed-parity scope repair was verified. The later
paragraph making the variational shorting bridge explicit changes no code.

The independent factorial Bessel implementation exactly matches the inherited
recurrence implementation. Both share the same source and analytic facts.
These are implementation and paper checks by collaborators with shared
context, not blind external peer review or independent source provenance.

No PR178 or PR179 analytic result is imported. No archived source was edited.
No merge, release, license change, zero-ordinate input or all-radii positivity
claim is made. **RH PROVED: NO.**
