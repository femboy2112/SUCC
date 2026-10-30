# Operation Directional Inertia — validation and boundary

**2026-10-29 · research-only supplement, proposed child of SUCC PR #377** at exact parent `89bb5edf53b3c421a931a3492e5e59da30728dc7`. No original signed four-pole source, U0, archived files, historical claims, root code, GitHub workflows, or main branch touched.

## Exact execution

- `python directional_entropy_probe.py -v`: **19/19 passing** standalone stdlib `Fraction` test methods in 0.185 seconds. Exact original source R(a), variance/third-cumulant strict interlacing checks at rational parameters, rational Jeffreys bounds, all-step telescoping identity, four q6 source endpoints and first derivatives, genuine Oily two-geometric normalizations, exact 16 inverse branches, integer-seed alias, and adversarial rational-seed constructed carry-16 events with their entire predicted following zero runs.
- `python independent_oracle.py`: **PASS**, independently computed 58-digit direct source-pole/density integrations for exact forward/reverse source KL, 3rd-cumulant positivity, total information asymmetry via digamma, and the four-cell q6 marginal KL at a=80,160,320,640,1280. The ratio `a^4 KL(P_(a+8)||P_a)` approaches the predicted exact rational `111563264/1042965` from below (70.22, 85.87, 95.60, 101.06, 103.95); these numbers are diagnostics, not analytic proofs.
- The `q6` limiting cell masses and first responses were derived from closed rational residue generating functions, independently of observed numerical fits. The all-a information inequalities and all-time carry-frequency theorem are supported by explicit paper derivations in the dossier. The numerical oracle does not replace those proofs.
- The first standalone attempt intentionally exposed an incorrect test comparison: the unwrapped index-zero seeds `0,-1,-16` differ, even though the circle phases agree **from time one**. The test was corrected to retain that distinction. Two subsequent transient Python syntax mistakes in an added test were fixed before the final 19/19 pass. No failed result was silently promoted.

## Status firewall

All claims are scoped mathematical identities, old classical facts, original-source paper derivations, and exact finite checks. **No full native SUCC test suite, parent branch integration, Lean kernel proof, hosted CI or external peer review was executed for this new supplement**. Ptolemy/Kepler is methodological context, not a proof input. Mathematical KL distinguishability is not physical heat without an intervention protocol. Source-Haar inverse probabilities are *not* a law for actual pi digits. The zero-selected signed `o(N)` Weyl estimate, base-16 normality, RH, and physical entropy-production dynamics remain **OPEN**.

## Reproduction

`directional_entropy_probe.py` uses Python stdlib exclusively; `independent_oracle.py` requires `mpmath`. The files `focused.log`, `oracle.log`, and `independent_oracle_receipt.json` preserve exact execution/output. Root repository integration and third-party review should precede merging.
