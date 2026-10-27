# Pointed-circle solenoid native-validation status

**Date:** October 27, 2026. **Research branch:** (to be committed as one atomic source addition, stacked over PR #319 at `6a187a61b19e389ed61e336a5d1c208bd21d773a`).

- Scoped standard-library exact tests: run in local isolated environment with a **temporary faithful `authentic_r` shim** copied from the inspected SUCC module. This shim is explicitly **excluded** from the GitHub commit; native SUCC `observational_succ.succ_internal_matrix_walk.authentic_r` is imported on GitHub.
- Independent checks: original source rational-cancellation and denominator parity; signed reference-cut cocycle and boundary; `2→16` cofinal inverse histories; torsion/winding memory mismatch; exact modular 2-adic isometry at negative/positive arguments; complete original residue permutations through modulus 16^3 (plus 16^4 in receipt); full-cycle character cancellation; repaired false candidate; positive isometric countermodel with matching leading real coefficient; odd-torsion grid harmonic countermodel; false normality status flags.
- Universal analytic and topological theorems are **paper proofs in the dossier**, not established by the finite tests.
- **No Lean kernel proof is asserted.** Native combined tree full-suite, provenance, observer, ordinal and hosted workflows must be inspected on the final pushed head. Historical archives and original theorem source are not modified.
- The local original source shim is a test environment fixture only and never part of committed blob manifest. No claim of new normality, RH or mathematical academic priority is made.

## Actual isolated local execution

- `PYTHONPATH=. python -m unittest discover -s tests -p 'test_solenoid_cut_source.py' -v`: **21/21 passed**, 0.168s, exit 0. The complete focused log is preserved at `research/2026-10-27/POINTED_CIRCLE_SOLENOID_FOCUSED_TEST.log`.
- `PYTHONPATH=. python scripts/solenoid_cut_source_probe.py --write` then `--verify`: deterministic source+test+probe SHA-256 receipt replayed successfully. The receipt enumerates all `16^4=65,536` BBP source-clock residues and `16^3=4096` hostile-control time residues.
- A deliberate `normality_proved=True` mutation in a temporary copy of the receipt was **rejected by recomputation**. The stored receipt and parent source are unchanged.
- The exact finite group is implemented with Fraction/integer modular inverses and does not use a π-digit oracle. The first source test independently equates the repository-native signed four poles to the fully canceled rational formula.
- These are **isolated** tests with a temporary source shim: native full SUCC CI, Lean, and adversarial external peer review remain separate obligations. The Python shim is **not committed**.
