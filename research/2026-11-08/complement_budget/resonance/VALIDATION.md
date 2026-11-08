# Executed validation

From the repository root, with no changes to native or frozen files:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
/tmp/succ-learning-yoneda-venv/bin/python -m unittest discover \
  -s research/2026-11-08/complement_budget/resonance -p 'test_*.py'

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
/tmp/succ-learning-yoneda-venv/bin/python \
  research/2026-11-08/complement_budget/resonance/oracle.py \
  --output research/2026-11-08/complement_budget/resonance/RECEIPT.json
```

Both commands exited0. Six tests passed. The oracle certifies:

- 3,188 exact source principal-part clock values;
- 3,185 exact rational complementary cocycles;
- six independent direct modular power sums;
- 36 outward nonlinear-model approximation-floor checks;
- 1,050 exact principal-part matches for a rational same-forcing control;
- two accurately fitting inverse affine controls, retained rather than rejected.

The source primes4201,4217,4337 were already used in the parent dossier.
These are reused source cases with a new fixed model menu, **not fresh holdouts**.
All36 actual error lower endpoints exceed the upper endpoint of the stated
floor. The floor is deliberately conservative. The two coherent controls
have interval error upper endpoints below10^-5 and must survive the theorem.

The source builder and 80-bit outward phase instrument are inherited;
independent modular sums test the recurrence, not independence of the phase
primitive. Square-root bounds are obtained by integer square roots with
outward endpoint corrections, and are separately tested against exact rational
squares. No ambient floating precision or external numerical library enters
the certificates. Script, source, proof and imported theorem hashes are in
the receipt. Classical PR3 and the infinite limiting proof are not certified
merely by these finite checks. No new Lean theorem is claimed.

Parent-wide validation is reported by the round's root handoff. This front
ran only its scoped tests and oracle.
