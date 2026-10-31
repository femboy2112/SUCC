# Complete Gauss units: exact blindness and selected-conductor obstructions

The strongest result is **GG-01/GG-05** in
[GAUSS_UNIT_BLINDNESS.md](GAUSS_UNIT_BLINDNESS.md): the entire collection of
complete order-eight weighted Gauss products at every odd prime has exact
integer coefficient fiber `c + 2 Z (1,-3,1,1)`. One complete algebraic
product at p=17 already determines this fiber. Intersecting with all-time
modulo-2^k source/orbit equality leaves precisely
`c + 2^(k+2) Z (1,-3,1,1)`. Thus recovering every GK unit does not repair
the positive mutant obstruction.

The dossier also proves that the selected complementary character cannot
be reconstructed by field operations in a fixed-p Gauss field, and that
authentic prime-power birth times escape even the union of all finite
composita of these prime Gauss fields. These are exact reconstruction
obstructions, not no-go theorems for analytic estimates.

Executed evidence:

- [15 focused tests](focused_tests-final.log), including all four prime
  classes, exact norms, Frobenius, both multiplication identities, large
  positive mutants, p19/p73 cancellations, and source discriminators.
- [17 complete exact Gauss/GK rows](probe_receipt.json), containing all
  119 Gauss sums as full cyclotomic coefficient arrays, normalized units
  modulo p^3, and independent cyclotomic unit-power checks.
- [Separate oracle](independent_receipt.json): Cartesian enumeration and
  univariate cyclotomic reduction match all 119 sums; an alternate product
  order matches every unit; 13 rational cofibers are reconstructed from
  direct weighted prefixes. Shared model/source, not independent proof authority.
- [Extra exact probes](extra_receiptcorrected.json): rank-three matrix and
  coefficient fiber, 10 authentic prime-power births, and coherent-null
  controls with zero Galois average.
- Raw execution metadata: [initial suite/probe/oracle](command_receipts.json),
  [final suite](tests_command_receipts-final.json), and
  [corrected extra probe](extra_command_receiptscorrected.json).
  A serialization-only failure is [preserved](INITIAL_FAILURE.md).

Reproduce from this directory:

```sh
python3 -m unittest -v test_gauss_exact.py
python3 run_probe.py > /tmp/gamma-gauss-probe.json
python3 independent_oracle.py /tmp/gamma-gauss-probe.json
python3 extra_probe.py
```

The tests and Gauss computation need only Python's standard library;
the independent and extra oracles additionally use SymPy. `run_validation.py`
captures bounded commands without a shell and refuses receipt overwrites.
The package does not run repository-wide gates or assert new Lean checks;
the integrating campaign owns those validations.

The next signed obligation remains source-selected: prove a quantitative
bound on the actual changing cofiber after retaining the original poles,
zero boundary and complete phase. A static GK invariant cannot supply
source authentication by itself. A larger ramified representation would
still need a signed saving, not merely exact reconstruction.
