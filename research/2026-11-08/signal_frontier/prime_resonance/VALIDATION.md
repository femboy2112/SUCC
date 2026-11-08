# Finite checks and scope

Executed from the pinned worktree with the existing virtualenv:

```
/tmp/succ-learning-yoneda-venv/bin/python -m unittest discover \
  -s research/2026-11-08/signal_frontier/prime_resonance -p 'test_*.py'
/tmp/succ-learning-yoneda-venv/bin/python \
  research/2026-11-08/signal_frontier/prime_resonance/oracle.py \
  --output research/2026-11-08/signal_frontier/prime_resonance/RECEIPT.json
```

Six tests PASS. Oracle PASS:

- 100 independent monic polynomial divisions, 1580 quotient evaluations.
- 118 exact full-field/coset exponential histograms, before any floating phase.
- 60 hidden-alias controls and 10 exact signed mixture identities.
- 1254 independent prime/order candidate checks across seven selector epochs.
- 3188 exact authenticated source principal parts and six independent direct
  modular source sums. The inherited unwrapped builder and carry hashes remain
  explicit in the receipt; this is not an independent source contract.
- 118 numerical Weil corroborations at80digits, including18 source cases at
  p=4201,4217,4337 and degree2,3,5 with **every bound strictly below1**.
  These are numerical checks of an imported paper theorem, not interval proofs.

The selector first appears at A=1051,p=4201. Development includes explicit
absence at137 and1050. Holdouts1601,2203,3001 have exact weight distances
74/1601,58/2203,106/3001 respectively; no finite case is substituted for the
asymptotic prime-density theorem. Source development/control primes were
fixed in the protocol before oracle execution. The18 larger-coset numerical
checks were added before executing their measurements to ensure nonvacuous
inequalities, after the root requested that validation. No coefficient fitting
or empirical exponent selection occurred.

The first oracle invocation failed before source replay because the inherited
builder could not import `observational_succ` when run as a standalone script.
The script now inserts its own repository root into its process-local import
path. The complete rerun passed. No package installation or global state change
was used. Root coordinates the mandatory repository gates and manifest.

Classical inputs are declared and URL/PDF-hash pinned in SOURCE_IMPORTS.json.
The PDF downloads are local reading aids, not copied into the repository.
Ford/Weil/PNT proofs are not formalized by these tests; no new Lean claim.

The next discriminating arithmetic task is to certify a small-error model of
the **original folded complement** whose nonresonant weighted degree is below
the proved budget, then bound its retained resonant coefficient. No such model
or coefficient-decay theorem was established by this front.
