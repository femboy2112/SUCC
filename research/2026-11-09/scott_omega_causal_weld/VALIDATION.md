# Local validation receipts, limits, and replay commands

## Actual execution on exported artifacts in this response

Four historical local scripts were re-executed from their previous files with `python`, with exit code 0:

- `succ_cmonoid_local_probe.py`: 4 affine prime-square/cube cases; 100 exact BBP block identities; finite Karoubi proxy (27 maps, 10 idempotents, 348 typed arrows); Haar split in three exact atomic cases; seed alias; no genuine C-monoid claim.
- `succ_omega_dimension_probe.py`: 140 Ω finite β growth reductions; 680 grid growth-rank states; CRT torus/12 Fourier modes; 340 currying readings; octahedral defect; synthetic holonomy on 64 plaquettes; no true source-derived flux.
- `succ_omega_gluing_probe.py`: 9 finite BBP horizon/seed models; 56 approximate fiber checks; 128 winding/carry; 13 domain/limit-order; 27 Fourier orthogonality; 205 polynomial checks.
- `succ_scott_omega_weld_probe.py`: 1,576 finite fraction checks of the opposite-arc seam and non-equal finite stages; *the infinite-limit equality is proved on paper*, not by the finite loop.

New standalone module `observational_succ/scott_omega_source_weld.py` and repo test `tests/test_scott_omega_source_weld.py` executed **locally together** as plain Python without the rest of the repository: **10 unittest methods PASS** in approx. 0.08 sec. These include 0/1 seed, exact `U_n+T_n^(L)=16^nP_L` for five horizons, nested strict compact enclosures for 12 times × 19 horizons, circle seams, origin alias, Ω growth and genuine four-pole hexadecimal digit enclosures (`3.243F6...`). Test uses rational calculations and no π oracle.

## Run on full repository

~~~bash
python -m unittest discover -s tests -p "test_scott_omega_source_weld.py" -v
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
~~~

Do not mark these five **full-repo** commands as PASS until actually executed on a materialized full checkout. A GitHub draft PR created through the connector is **not** a test run. Check hosted CI on the exact resulting head; absence of a run is not success. Lean is not executed for the new theorems.

**Provenance limitations:** Earlier codes and new tests derive from one assistant's mathematical definitions; different languages/implementations and genuinely independent theorem review are missing. The source algebra is explicit and exact, so another implementation has clear falsifiable outputs to compare.
