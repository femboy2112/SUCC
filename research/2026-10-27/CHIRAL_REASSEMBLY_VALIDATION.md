# Chiral target descent: executed validation and authority boundary

Pinned source parent: PR #333, `a0e4bfd9c218dfdc83ed9d5684ce8d8e4624cde5`.
This is a source-authenticated partial standalone tree, not a complete native SUCC checkout.
Original source module is copied byte-for-byte, not replaced by a shim.

## Executed checks

- New exact focused tests: **23 passed**.
- Unchanged parent rank-two tests: **17 passed**.
- Combined local discovery: **40 passed**, zero failures, in 3.366 seconds.
- Optional alternate SymPy algebra: all endpoint, pole, source, and two-clock identities pass.
- Exact receipt generation and replay: pass, including three deliberate false-authority/source mutations.
- Alternate mpmath 80-digit method: the direct original four-pole recurrence and the full all-pairs
  Poisson kernel agree with every rigorous Fraction enclosure at N=16,32,64,128,256.
  This floating-point corroboration is NOT the certificate authority and is not a blind witness.
- Positive control: coherent phases have full energy 2.
- Negative control: the explicitly different PR320 zero-seeded rational nonnormal source has energy near 2.
- Hidden-mode control: q=17 uniform roots have exact nonzero full energy 2/131071 even though modes1..16 vanish.
- Authentic hostile probe: the no-error pointwise drift J_N<=Q_N/2 fails at N=2 by a certified margin >0.648250722873.

## Reproduction

```sh
python -m unittest discover -s tests -p 'test_*chiral*.py' -v
python research/2026-10-27/chiral_target_independent_oracle.py
python scripts/chiral_target_descent_probe.py --verify research/2026-10-27/CHIRAL_REASSEMBLY_RECEIPT.json
python research/2026-10-27/chiral_target_pair_oracle.py
```

Only the two optional alternate oracles need SymPy or mpmath. The production module,
focused tests and exact receipt use only Python's standard library.

## Source hashes

Exact Git blobs checked locally before upload:

| File | Git blob |
|---|---|
| parent `rank_two_chiral_towers.py` | `8305e09892f19007e0ae0538a60d05954b2def9e` |
| `chiral_target_descent.py` | `6cdcb9133c93324eb0e6e604626f4238ef4a3e04` |
| `test_chiral_target_descent.py` | `317e76b211fc45441cdc6511961360338fe2a668` |
| `chiral_target_descent_probe.py` | `429d4f8879f81996df0e41b8d83edaa78c9cb93e` |
| main proof dossier | `b3d4a571dffa642cd9c1dd4a6daf6ec4e2f13778` |

The deterministic receipt binds SHA-256 of both production modules, the test file and the probe.
Raw test, symbolic, replay and pair-oracle outputs are included in the downloadable research archive.
The repository includes the receipt and executable alternate oracles; do not confuse receipt checking
with proof of an infinite-time limit.

## Failures and unrun gates

Direct `git clone` failed DNS resolution. A combined process timed out while generating the longer
receipt after its tests and symbolic checks had completed; receipt generation was rerun separately
and completed, followed by successful exact replay. No mathematical test failure is hidden.
Full native repository tests, `verify_provenance.py`, observer/ordinal probes, and pinned Lean
were NOT run in this environment. Hosted CI must be inspected at the final published SHA; it is
not preclaimed here. No normality, stronger selected Weyl order, external peer-review, or
scholarly-priority conclusion follows from this validation.
