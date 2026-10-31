# Local exact validation and scope

**Base consulted:** Main XVII HEAD `e8598cfa5d32fd1de8e94a3e458a366a0850d59e`. **Branch changes:** research-only new files and one new discoverable root test. **Original source and zero seed:** unchanged. **Local checkout:** isolated research files mirrored in `/mnt/data/succ_carrier_path_work`; the sandbox cannot resolve github.com for `git clone` (attempt failed with `Could not resolve host: github.com`). GitHub connector is used for direct repository writes instead.

## Commands executed locally

```sh
python -m unittest discover -s /mnt/data/succ_carrier_path_work/tests -p 'test_carrier_path_measure.py' -v
# Ran 20 tests ... OK (actual final verification below) (2026-10-31)

python /mnt/data/succ_carrier_path_work/research/2026-10-31/carrier_path_measure/independent_oracle.py
# Outputs exact 2, 2/3, 1, 21/67 for four network cases; direct Pascal16 true.

python /mnt/data/succ_carrier_path_work/research/2026-10-31/carrier_path_measure/carrier_path_measure.py
# r(1)=47/15; affine square n=0,p=3 is -94/15;
# line R=2, triangle R=2/3; Pascal16 all interior vanish.
```

### Independent algorithms

- Grounded `Fraction` Laplacian solve vs a **different** algorithm that enumerates weighted spanning trees and separating two-forests; compared exact graph resistance in five network examples including nonuniform conductances.
- Gaussian-Pascal q-polynomial recurrence vs direct combinations at `n≤10`, and all **65,536** bitwords at `n=16`; exact primitive root reduction uses the canonical basis of `Z[q]/(q^8+1)` (no approximate complex exponentials).
- Main original four-pole recurrence `U_(n+1)=16U_n+r(n+1)` vs exact rational algebra of `T_n(p x)−p T_n(x)` for 300 rational index/prime/state combinations, and exact source-integral rational upper bounds.
- Finite translated complete `Z_2/2^a` residue windows for a≤4 and starts 0,1,5, plus first windows a≤6. These are finite tests, not an independent general DSI theorem.
- Discounted integer-walk Green kernel exact values through displacement 5 vs direct finite path sums with rigorous geometric remainder bounds, `L=20,35`.

### Numerically displayed finite source-pairing results (raw computation exact rational)

| a | N=2^a | Mean antipodal real-phase error | Certified upper bound / N |
|---:|---:|---:|---:|
| 2 | 4 | 0.3121010 | 0.9808888 |
| 3 | 8 | 0.2496503 | 0.7846153 |
| 4 | 16 | 0.2072656 | 0.6514062 |
| 5 | 32 | 0.2581159 | 0.8112213 |
| 6 | 64 | 0.2596148 | 0.8159322 |

These seven-digit numbers are explanatory roundings of exact rational measurements; the code returns exact fractions. No trend claim and no inference about the limit. Pairings are defined from exact *2-adic* residues, and certified bounds concern the *real-circle* `e(hU_n)` phases; their mismatch is the point of the probe.

### Not executed / not claimed

- No complete `python -m unittest discover -s tests` against the entire live repo; no full `scripts/verify_provenance.py`, observer foundation/ordinal scripts, Lean kernel compilation, hosted CI, peer review, external formal referee, or π-normality proof.
- No changes to `docs/CLAIM_LEDGER.md`, approved formal namespaces, imported archival originals, exact BBP source, production modules, CI workflows or main.
- The work's new code tests finite and precisely stated classical identities, **not** the open signed all-horizon gate.
