# Validation — 2026-11-12

Exact standalone run, Python standard library only:

```text
$ python -m unittest -q test_carrier.py
----------------------------------------------------------------------
Ran 11 tests in 0.111s

OK
$ python carrier_probe.py > RECEIPT.json
```

All claims concern finite computational checks and elementary paper derivations. Test scope: n <= 84 for two coproduct associativity, trial division versus sieve through 512, exact convolution check through N=256, and all 256 binary masks of dimension 8. Additional exact fake-source, oracle lower-bound, rank, and Schmidt controls. These are same-session local tests, not independent external validation.

**No native full SUCC test suite, CI, Lean kernel, external mathematical review, or merge was performed in this addendum. Binary Goldbach remains OPEN.**