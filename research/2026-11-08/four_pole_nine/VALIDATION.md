# Independent execution and authority ledger — FOUR-POLE NINE

**Exact new research files**, created 2026-11-08 in an isolated lightweight Python research tree. **No full SUCC checkout was available in this container; direct GitHub access was through the connector.** The source code keeps the original BBP four rational pole signs, weights, offsets and literal zero seed. Files were not used to modify main, archived sources, `formal/`, `provenance/`, workflows or any open sibling research branch.

## Executed, exact scope

Environment: Python **3.13.5**, SymPy **1.14.0**, mpmath installed but **not required by new tests**. New module and root-discoverable test use the stdlib; the independent algebraic oracle uses SymPy. Numerical finite signed diagnostics use `cmath` on `Fraction`-reduced phases and **are not rigorous enclosures**.

- `PYTHONPATH=<isolated root> python -m unittest discover -s tests -p 'test_four_pole_nine.py' -v`: **34/34 PASS**, zero skipped or failed. Log: `FOCUSED_TEST_LOG.txt`. Tests include 100 original/source identity cases, 24 zero-seeded component reconstructions, 180 two-adic forcing seams, 79 two-adic lifted histories, closed Cauchy determinant, 3–4–5 jet rigidity, exact time-order commutator entries/norm, full 1+3+5 algebra, Poisson two-pole mutant, root-of-unity pairwise blind control, source-positive fixed-point brackets and first-jet asymptotic. The counts describe loop cases, **not independent theorems**.
- `PYTHONPATH=<isolated root> python -m unittest discover -s tests -p 'test_*.py' -v` with the **unchanged 21 focused tests from draft PR #549** added to the same isolated test tree: **55/55 PASS**. Log: `COMBINED_53_TEST_LOG.txt`. This is **not** the full SUCC native suite and does not imply that #549 is in main.
- `python -m compileall -q` on new module, tests and two probes: **exit 0**.
- `python research/2026-11-08/four_pole_nine/independent_sympy_oracle.py --out research/2026-11-08/four_pole_nine/INDEPENDENT_EXACT_RECEIPT.json`: **exit 0**, exact symbolic proof-equation crosscheck; independently reconstructs original source, two jets, rigid `(3,4,5)` solution, 3×3 Cauchy inverse, all 16 chronological commutator entries, closed Vandermonde norm, all 16 leading asymptotic matrix entries, 2-adic odd-denominator pairing and golden fixed-point drift. Output: `INDEPENDENT_ORACLE_LOG.txt` and deterministic JSON. This is an independent **implementation**, not an independent external scholar or Lean certificate.
- `python research/2026-11-08/four_pole_nine/finite_signed_probe.py`: **exit 0**, finite exploratory signed moments, **8 declared cases** with `A=17,31,61,127`, `h=1,2`. Their exact rational source phases were converted to native float trigonometry; `FINITE_SIGNED_DIAGNOSTIC.json` is **OBSERVED FINITE ONLY**, not interval-certified. The parameters were written into the script before its local execution, but **no earlier timestamped public preregistration exists**; do not call it preregistered evidence.
- `ARTIFACT_MANIFEST.json`: SHA-256 content hashes of executable code and raw result/log files; does **not** certify GitHub exact-head CI until those files are read back and their Git blob identities compared.

## Not executed locally / authority exclusions

- `python scripts/verify_provenance.py`: **NOT RUN locally** (full checkout absent).
- `python scripts/observer_foundations_probe.py`: **NOT RUN locally**.
- `python scripts/ordinal_succ_report_probe.py`: **NOT RUN locally**.
- Full native `python -m unittest discover -s tests -p 'test_*.py'` from SUCC main: **NOT RUN locally** (the 55-test combined replay above is a partial isolated package).
- Hosted GitHub PR-head CI: **check after push**; do not infer from root historical receipts or from local tests.
- Lean kernel: **NOT RUN** for these new claims; no .lean file is changed.
- External peer review / scholarly novelty: **UNVERIFIED**.
- Original zero-seed π Weyl limit, source-selected signed third cumulant or signed #544 covariance: **OPEN / UNVERIFIED**. Finite tests and two-jet rigidity do not address their all-epoch quantifiers.

## Reproduction

Run commands from a checked-out repository root, keeping the original interpreter/environment and a stable exact SHA. Do not rewrite archival receipt inputs. Independent source comparison is essential: the local tests intentionally implement the original four-pole function directly rather than modifying SUCC's canonical `duck_bbp`.

```sh
PYTHONPATH="$PWD" python -m unittest discover -s tests -p test_four_pole_nine.py -v
python research/2026-11-08/four_pole_nine/independent_sympy_oracle.py --out /tmp/four_pole_nine_sympy.json
python research/2026-11-08/four_pole_nine/finite_signed_probe.py
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
PYTHONPATH="$PWD" python -m unittest discover -s tests -p 'test_*.py'
```

The finite program updates `FINITE_SIGNED_DIAGNOSTIC.json` when invoked; for an immutable research checkout copy it to a scratch directory first if you need a clean working tree. All open tests and exact algebraic controls must remain visible even if a new theorem route is later refuted.
