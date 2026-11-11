# Validation and publication checkpoints

## Initial archive checkpoint

The checkout was created from SUCC main at
`43886e830cee5ff6d6b37719e18d809819673bd9` on the non-main branch
`aletheia/cursed-categories-dedekind-yoneda-2026-11-10`.
The first publication contains Rounds I and II, their fresh exact probe, local
claim ledger, provenance, and generated discovery-catalog update.

Fresh root execution on Python 3.12.14:

```sh
python -W error research/2026-11-10/cursed_categorical_computation/round_ii_probe.py --output round_ii_root_receipt.json
```

Result: PASS. The archived receipt names its source hash. The root rerun had the
same source hash and passed the declared finite domains. Counts and controls
are recorded in round_ii_receipt.json. These are implementation checks, not a
replacement for the proofs in the notes or independent external refereeing.

The three fast repository gates also ran successfully on the unchanged base:

```sh
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Provenance verified all 72 imported items, including 17 byte-identical research
archives and 55 documented namespace migrations, against original source commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`.

The full repository unittest gate and final-head hosted CI are not claimed at
this checkpoint. Their actual outcomes will be recorded at the end of the next
round. The repository workflows are unchanged. Both requested branch pushes
will precede one final draft PR so the PR gates review the completed result.

## Reproducibility and limits

The new probes use exact integers and fractions.Fraction for proof-relevant
arithmetic. No Lean/Rocq build, full PIGAME execution, universal positivity
inference from samples, or normality/RH proof is claimed. Cited donor branch
theorems retain their provenance and are not silently counted as fresh runs.
