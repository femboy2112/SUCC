# Twin rendezvous exact finite validation and replication contract

**Scope:** added pure-stdlib module `observational_succ/twin_rendezvous.py`, and `tests/test_twin_rendezvous.py`. Isolated local staging contains only these two new files plus a minimal package `__init__.py`; it does not execute the entire SUCC repository.

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_twin_rendezvous.py' -v
```

**Observed before commit:** 22 unit tests passed, 0 failures, 0 skips, under the local Python interpreter. They include exact all-16 Pauli pairs, an independent four-pole versus polynomial source comparison at n=1..50, full quantum density and partial traces with rational coefficients, marker overlap `γ=3/5`, dephasing without measurement, shared-environment uncompute, distinct-environment residual, single-click false-positive, independent-reference restricted soundness, rational Lorentz boosts, common meeting target, timelike reachability, original-BBP algebraic zero pin, same-wrong-model and same-wrong-seed hostile cases, and invalid-input controls.

These are finite implementation receipts. The `U⊗conj U` and all-normalized-marker statements in the written dossier rely on algebraic paper derivations, not the finite test count. The code deliberately does not measure a quantum system, perform a physical Bell test, simulate relativity beyond flat special relativity, enforce cryptographic provenance, decide mathematical proof truth or establish a signed π estimate.

**Before any integration or claim promotion:** run `AGENTS.md` checks on exact branch head, not an older green SHA:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Independent audit targets: environment-overlap phase orientation; all 16 Pauli classes; uniform error-coupling assumption behind witness Bell pairs; source certificate authenticity and frame transports; physical separation/no-signaling; source-specific signed-R0 firewall.
