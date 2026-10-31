# Signed CRT and moving-conductor front

Read [CRT_DOSSIER.md](CRT_DOSSIER.md) for proofs and their limits, and [ROUTE_LEDGER.md](ROUTE_LEDGER.md) for survived/refuted/dark routes. The primary SC-06 estimate remains open.

The new arithmetic content is a uniform sublinear-moving-filter conductor theorem and an exact extension-degree obstruction for the full ordinary finite-field character-value family, with a secondary exact polynomial denominator degree. Exact coherence cylinders and finite dyadic shadows isolate why local arithmetic snapshots cannot set a boundary-independent finite-window threshold.

Reproduce from repository root with fresh receipt names:

```sh
python3 research/2026-10-30/zero_boundary_dispersion/crt/run_receipt.py --name reproduce-tests -- python3 -m unittest discover -s research/2026-10-30/zero_boundary_dispersion/crt -p 'test_*.py' -v
python3 research/2026-10-30/zero_boundary_dispersion/crt/run_receipt.py --name reproduce-probe -- python3 research/2026-10-30/zero_boundary_dispersion/crt/crt_probe.py
python3 research/2026-10-30/zero_boundary_dispersion/crt/run_receipt.py --name reproduce-oracle -- python3 research/2026-10-30/zero_boundary_dispersion/crt/independent_oracle.py
python3 research/2026-10-30/zero_boundary_dispersion/crt/run_receipt.py --name reproduce-field -- python3 research/2026-10-30/zero_boundary_dispersion/crt/character_field_probe.py
```

The oracle reads the retained `receipts/probe.log` as a cross-implementation comparison target. `character_field_probe.py` additionally needs SymPy; every other program uses the standard library. Recorded runs used Python3.12.3, one thread, and a1024MiB limit. Nothing here claims a new Lean proof, hosted CI pass, external referee, π normality or RH.
