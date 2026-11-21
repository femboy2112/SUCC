# Validation receipt — 20 November 2026

Source: immutable Main XXVI's four-pole forcing, literal zero seed. Research parent: draft #680 `5085b558cbba28bfc347d12865baeb892379af17`. Files are additive only. Scope: exact integer/rational and finite 2-adic residue arithmetic, classical imported parity-conjugacy theorem, exact factorization; no native sensor tests, no analytic all-shell signed pi estimate.

## Reproducible commands executed locally

```bash
python -m unittest discover -v -p 'test_*.py'
python independent_audit.py
python -m compileall -q parity_dual.py test_parity_dual.py independent_audit.py
python parity_dual.py
```

**Results:** all **16/16 unit tests PASS** (`focused_unittest.log`). Independently written (does not import implementation module) exact/SymPy audit **7,825 checks PASS**, including finite parity-map bijectivity for moduli 2^1 through 2^12, two inversion routes, Omega commutation/period, source polynomial identities, 801 independent mod4 controls, and BBP 48-bit source-selected dual residue (`independent_audit_receipt.json`, `independent_audit.log`). `compileall PASS`. Finite tests support the code's advertised scope, not the universal conjugacy theorem (which is a credited classical result).

**Original source finite certificate:** rational BBP partial sum `P_12=sum_(j=1)^12 16^-j r(j)` and strict tail `0<x-P_12<16^-12 r(13)/15` agree on floor of `16^12 x`, giving `3243F6A8885A`; the parity address is `0xA5888A6F3423` and the inverse parity seed modulo `2^48` is `0x138D4B466283`. Replaying exact 48-step shortcut Collatz parities from the minimum positive representative matches the address, while not determining or constraining its infinite orbit.

**Mutation and obstruction controls:** root/quarter label alone fails source factor, raw-state reflection is not Omega, out-of-family BBP mutated source produces another legal conjugate parity path, all-zero stream is also perfectly encoded, pointwise finite source identification does not prove normality, positive integer termination or physical energy. The classical Bernstein--Lagarias/Monks--Yazinski theorems are credited, not claimed new.

**Not run or claimed:** full inherited SUCC root unit suite (>14k), `scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`, hosted CI, Lean, independent human referee, root-source conjugacy to π real digits beyond their universal coding map, π R0/normality, or general Collatz termination.
