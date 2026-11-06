# Validation and limits

Research interpreter and exact LCM carrier derived from GitHub main and existing observer draft. Local scratch tree contains a byte-copy of `operational_probe.py` from the parent observer draft for testing **only**; the new GitHub branch must reuse the ancestor file instead of committing a competing copy.

**Actually executed in local isolated staging (Python 3.13):**

```text
python -m unittest test_source_sound_calculus test_source_sound_receipt -v
18 tests PASS; zero errors, failures or skips.
python receipt_probe.py --write FINITE_RECEIPT.json
python receipt_probe.py --verify FINITE_RECEIPT.json
SOURCE_SOUND_LCM_EXACT_RECEIPT_VERIFIED
python -m py_compile source_sound.py lcm_carrier.py receipt_probe.py
```

Detailed finite positive and hostile probes: (a) LCM least upper bound and associativity on finite ranges, (b) cyclic `C_m⊕C_n→C_lcm` kernel and image for 400 pairs, (c) exact fraction phase inclusion and CRT reconstruction, (d) original BBP four-term vs collapsed forcing, odd conductor and literal carry on an 80-step prefix, (e) one C6 clock with independent, zero-Dirac and correlated distributions, (f) model traces, observation fibers and source-labelled journals, (g) budget-sensitive observational refinement, (h) *sound model-relative induction* with a mutated transition step rejected, (i) introduction/elimination of ∧ and → under source-typed assumptions, (j) rejection of unsupported empirical attestation, wrong-source transport, forged outcomes, false lcm/group claims, bad initial seed, false carries and proof budget overflows, (k) deterministic exact BBP prefix SHA256 receipt.

**Separate native-integration test:** `tests/test_source_sound_repo_bridge.py` imports the *actual repository* `integer_bbp_carrier`, `bbp_natural_carrier`, checks force, conductor, integer lift and literal carry. This test **cannot run in isolated local staging**: public GitHub host resolution fails and production package is not installed. It must pass on the **hosted exact PR head**. The local `unittest discover` including this bridge raises `ModuleNotFoundError`; this is an environment access gap, not a successful full local suite. It is explicitly recorded, not hidden by skipped assertions. Native full SUCC tests and provenance/observer/ordinal probes are likewise hosted gates, not local claims.

**Authority:** Exact finite math tests and paper algebra. No new Lean contracts were submitted; same-model code paths are not independent external referees. Fixed comparison data does not prove π normality or quantum/state entropy. Claims in `CLAIM_LEDGER.md` preserve these boundaries.
