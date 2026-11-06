# Finite exact controls and authority

Local calibration, 2026-11-04: \`python -m unittest -v test_operational_probe\` -> **8/8 PASS**, 0 skips/failures. Tests use deterministic synthetic finite sources, not externally measured physical systems.

Controls include:
- Two same-appearance synthetic states that become distinguishable only when a paid tagging probe is available.
- Append-only journal provenance; missing labels rejected.
- Exhaustively composed state-changing finite probe words with identical trace and final state under reassociation.
- Every designated finite induction horizon shares two distinct computable compatible laws.
- Deterministic classical write operations with noncommuting order.
- A zero-seed nonmixing classical process.
- Rejection of invalid source-state IDs, probe names and malformed readouts.
- Distinct hidden states with identical visible appearance.

The exact instrument script is standalone and does not claim a real-world source signature, quantum probability, new Lean formal proof, proof of ZFC-equivalence, or π/RH results. Hosted whole-SUCC CI at the exact branch head is a separate check.
