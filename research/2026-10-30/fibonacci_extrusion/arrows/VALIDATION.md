# Executed arrow validation

All work is additive under this folder, on isolated PR408 child branch
`research/fibonacci-triangle-extrusion-2026-10-30`. Parent head is
`7b5a2b4534aa5e71865046ca8d3f723d8002b9fe`.

- Focused final suite: **12 tests PASS**; exact Fraction and Q(lambda)
  arithmetic. The earlier10-test successful run is retained separately and
  is not counted again. No failed mathematical assertion occurred.
- Probe: two exact cycle witnesses, rank23 on dimensions24 and28; five
  positive native-source aliases; six exact finite residuals; five positive
  rational infinite-product lower certificates;301 fresh Zeckendorf cases.
- Separate oracle: six Mellin-residue reconstructions, three fresh residuals,
 330 native Beta joint entries,72 translated-Fibonacci cycle checks,23 joint
  entries recovered by Lagrange interpolation in SymPy's algebraic field.
- Complementary arithmetic review: seven moduli, five brute-force Hensel
  precision lifts,59 pre-birth states, four first-pole times and six finite
  surgery controls; exact reviewed sibling hash retained.
- Source density positivity has an exact coefficient-positive polynomial
  certificate in addition to the concavity proof. The finite quadratures of
  the parent are not used as a premise here.

The finite residual code has only finitely many zero moments. The **infinite**
alias rests on the proved nested-projection limit and strictly positive
infinite-product lower bound. Tests do not purport to evaluate an infinite
function or establish π normality.

Same-model reasoners and separate algorithms do not provide independent
external proof authority. Full repository checks and hosted CI belong to the
root delivery and are not duplicated here. No Lean proof was attempted for
the functional-analysis claims.

Read-only exploration encountered two guessed nonexistent paths (the parent
module filename and an old Lorentz directory). `rg --files`/`git ls-tree`
located the actual files and they were read. Several patch attempts failed
atomically on unused context lines; smaller intended patches then succeeded. None was
a mathematical failure. The large primary Borwein PDF exceeded the browser
size limit; its publisher metadata and a readable author-hosted exposition
were inspected, and the needed Gram argument is proved explicitly here.

Commands and output hashes are retained in `receipts/focused*.json` and
`receipts/oracle-run.json`. `probe.json` holds the first exact witness output;
the separately captured replay has the same mathematical contents.

Reproduce without overwriting historical receipts:

```sh
python3 -m unittest discover -s research/2026-10-30/fibonacci_extrusion/arrows -p 'test_*.py' -v
python3 research/2026-10-30/fibonacci_extrusion/arrows/run_probe.py fresh-probe.json
```

For the oracle, use a disposable folder or select a fresh output name in a
copy: it deliberately refuses to overwrite its saved `oracle.json`.
