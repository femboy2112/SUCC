# Lawful Probe Budget Forge — Principia Observatoris

**Draft research continuation of #626**, rooted in the pre-activation source-difference / identity-observer investigations. Entry point: [THEOREMS.md](THEOREMS.md).

This research distinguishes an observer's cost to **learn a target** from its cost to **construct a T-compatible backward reconstruction**. It gives three exact finite procedures: weighted pair-cover, worst-case single-copy adaptive AND/OR policy synthesis with losing certificates, and minimum-cost passive refinement tested for a deterministic or stochastic T-equivariant section. No unregistered readout may be invented as a hidden-label oracle.

The mathematical surprise is that extra passive information may destroy backward section feasibility while improving target knowledge. A six-state exact model realizes `no lift → stochastic-only at cost 2 → point at cost 5`; a separate three-state model refutes monotonicity of lifting under observation refinement.

Run from repository root:

```sh
python -m unittest discover -s tests -p 'test_probe_budget.py' -v
python research/2026-11-14/probe_budget/independent_oracle.py
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

The first two commands were executed in a clean isolated Python scaffold; the four required root commands are **not claimed** from that environment. The new module is standard-library-only and deliberately capped for exact exponential search. Read [VALIDATION.md](VALIDATION.md) for raw receipts and source-hash scope.

This is a research-only input to Principia. Do not merge to main, change original arithmetic source contracts, or call probabilistic section feasibility a measured posterior.
