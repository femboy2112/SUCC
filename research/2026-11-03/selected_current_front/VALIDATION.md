# Original selected-current and integration audit validation

**Research branch parent:** SUCC #488 exact original source tip `f47e3768631cd1628c1390d529811c911e0f6443`. **Preregistration pushed to GitHub FIRST** as commit `d07f6d1487eb032de36935e66e7a81357aa71ebc` before evaluating the new selected source epochs A=40,80,160 and origin-integration holdouts A=12,24. These are same-assistant preregistrations, not blinded independent reasoners.

**Actually executed isolated local staged tests:**

- `python -m unittest discover -s /mnt/data/succ_selected_current_front/tests -p test_selected_current_front.py -v`: **15/15 PASS**, zero skipped; all declared original-source comparisons, 2 independent exact time/source implementations, both exact boundary integrals, Gamma synthetic Lipschitz control, forced-source boundary crossings, shifted-current branch squares, point-mass hostile controls.
- `python -m unittest discover -s /mnt/data/succ_circle_path_electric/tests -p test_circle_path_electric.py -v`: **12/12 inherited PR #488 focused PASS**, zero skipped. These are reuse of the same source lineage, not independent proof attestation.
- `python .../independent_oracle.py`: **PASS**, second original source formula uses collapsed polynomial A/D and common integer modulus, and an independent piecewise-origin integration without triangular pair kernels.
- `python .../probe.py --verify`: **PASS**, full deterministic exact `FINITE_RECEIPT.json` regeneration, no pi digits or floating thresholds.
- `python -m compileall -q ...`: **PASS**.

**First staged test calibration:** a first run produced THREE `ValueError` instances because the energy evaluator rejected the single-cell root level m=1. This was reproduced, corrected to the mathematically required `E_0=J_1=1` convention while keeping the triangular formula restricted to m>=2, and all 15/15 reran green. Raw final log is `TEST_LOG.txt`. This was an ordinary input/domain mismatch, not a result being discarded.

**Fresh, exact original source finite measurements (diagnostic, NO extrapolation):**

| A | E_(A,16)(canonical) | J_(A,8) | J_(A,16) |
|---:|---:|---:|---:|
| 40 | 1.32000000 | 1.16127635 | 1.32607188 |
| 80 | 1.17500000 | 1.08257846 | 1.16172807 |
| 160 | 1.05250000 | 1.02827059 | 1.06298393 |

Values above are rounded only for presentation; `FINITE_RECEIPT.json` retains exact rational fractions and source phase SHA256 commitments. No finite trend is promoted to a source asymptotic. The exact original-source one-step forced crossing means at m=16 were about 0.0011775, 0.00029367, 0.00007333 for these three epochs respectively; all satisfy the proved rational cap. The true Gamma energy comparison bounds come from source-analytic proof, NOT from fitting π digits.

**Source map and finite controls:** true original signed poles, literal `U_0=0`, no replaced forcing, exact real Fraction phases. `source_epoch(A)==independent_modular_epoch(A)` exactly at each preregistered A; no Galois/virtual path averaging. Point mass at 1/5 has canonical and origin-averaged energy m at every mesh and passes the `×16` fixed-point condition. This is an explicit false-positive firewall for source-invariant-current reasoning.

**Access boundary:** container Git clone of the public repository failed `Could not resolve host: github.com` (exit 128). Therefore these were isolated source-focused tests, not the full native SUCC suite. No native root provenance / observer foundations / ordinal report / whole-repo tests, no new compiled Lean, no external peer review and no child exact-head hosted CI success claimed. Integration and full suite belong to the requested Claude follow-up. Current GitHub branch/tree contents must be re-fetched and byte-verified after commit.

**Classical provenance:** the triangle/sinc² Fourier transform and martingale energy decomposition are standard. The source-specific exact Gamma transport and real time-boundary crossings are elementary consequences of inherited original SUCC BBP tail and forcing identities; they do not independently certify the inherited source's analytic tail proof. **The actual original selected `J=o(log m)` and π normality remain OPEN.**
