# Validation and authority

Baseline: db9fb4b84672050efa79b13377f1e73364598a14.
The final commit/tree and completed final-head required-gate output are recorded
in the associated draft PR. This file records the reproducible commands and
prepublication receipts without pretending a later full run had already finished
when the file was written. No merge is authorized.

## Executed before the final content freeze

- Canonical baseline: 33 native tests across duck_bbp, integer_bbp_carrier and
  selected_orbit passed.
- New native suite: 10 tests passed, including separately written unwrapped
  four-pole replay, exact endpoint-grid controls, source correction, alias,
  terminal rational seed, tail brackets, certified cosine bounds, barycentric
  response and the repaired h32/q1 ambiguity witness.
- Root replay of inverse_probe.py:5,644 exact checks.
- Root replay of holographic_probe.py: 438 exact recurrence checks, 146 aliases,
  192 exploratory 80-digit interpolation checks. The floating checks are not
  certificates; the written interpolation theorem supplies the universal bound.
- probe.py: eight prescribed source shells, including held-out 97,193,389,769,
  have rational anti-lock intervals satisfying the proved energy bounds;
  H=1600 terminal-root seed has zero impulses through 1538. RESULTS.json contains
  all finite outputs, with source and scope labels.
- gaussian_probe.py and independent pade_audit_probe.py have exact JSON receipts.
  gamma_prime_probe.py and gamma_independent_audit.py use different arithmetic
  decompositions and have exact JSON receipts. hostile_probe.py reproduces the
  pulse and terminal-root controls. Counts remain per instrument; they are not
  summed into evidence votes.
- The three short required gates passed precommit: provenance (72 imports,
  17 byte-identical archives), observer foundations, ordinal report.
- Proof review found and repaired the HBT-04 ambiguity-supremum overclaim.
  The Gaussian degree-three sign correction and the power-of-two-degree scope
  are retained. See AUDIT_CURRENT.md, PADE_AUDIT.md and GAMMA_AUDIT.md.

The later native expansion from 8 to 10 tests adds the barycentric filter and
h32/q1 mutation. The current audit's older count 8 describes the snapshot it read.
No old count is silently presented as a later execution.

## Required final-head commands

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The full native run must complete at the final published SHA; precommit focused
success and a previous branch's CI do not substitute. Its exact completed count,
exit status, source tree and log hash belong in the PR validation block.
Hosted CI and local execution are separate reports.

## Dossier replays

Run from the repository root, with PYTHONPATH=.

```sh
python -m unittest tests.test_leah_gamma_twist
PYTHONPATH=. python research/2026-11-12/leah_gamma_twist/probe.py /tmp/leah-shells.json
PYTHONPATH=. python research/2026-11-12/leah_gamma_twist/inverse_probe.py
PYTHONPATH=. python research/2026-11-12/leah_gamma_twist/holographic_probe.py
python research/2026-11-12/leah_gamma_twist/gaussian_probe.py
python research/2026-11-12/leah_gamma_twist/pade_audit_probe.py
python research/2026-11-12/leah_gamma_twist/gamma_prime_probe.py
python research/2026-11-12/leah_gamma_twist/gamma_independent_audit.py
python research/2026-11-12/leah_gamma_twist/hostile_probe.py
```

Some independent probes require PYTHONPATH=. as well if the checkout is not
installed. JSON-generating scripts default to verification or deterministic
regeneration as documented in their headers. No random sampling affects a receipt.
The retained precommit logs in receipts/ are actual outputs, not full-native
results. Library packages used in the root environment: numpy 2.3.5,
scipy 1.17.0, sympy 1.14.0, mpmath 1.3.0.

## Scope

No external peer review, new Lean proof, effective PNT onset, all-shell statistical
saving or normality theorem was established. Same-model parallel research and
separate implementations can reveal different errors; their agreement is not
independent mathematical provenance. The unchanged frozen imports retain their
original authority. Only additive new files enter this research branch.
