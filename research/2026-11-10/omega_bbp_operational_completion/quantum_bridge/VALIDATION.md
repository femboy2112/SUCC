# Focused quantum bridge validation — 2026-11-10

- Python 3.12 stdlib implementation `omega_quantum.py` imports only the exact existing `../omega_haar.py`. Numerical numpy crosscheck is separate and is **not** a runtime dependency.
- Test command from the new folder: `PYTHONPATH=.. python -W error -m unittest -v test_omega_quantum.py`.
- Test scope: dyadic Haar orthonormality/inverse, non-equality to Walsh–Hadamard, exact 4-qubit parity state, 2×2 / 3×3 butterflies and detail restoration, six-step Ω₄/Ω₅ BBP grouping, skew unitary flow, 12×12 Hermitian chirality and its time reversal, two-route heralded defect, BBP source-prefix π/16 index, finite-L phase-oracle versus Weyl overlap, rational wrong-seed phase=1, monodromy controlled shift, no-cloning overlap, rigorous source-tail upper enclosures, signal and shot-variance asymptotics.
- Independent numpy/SymPy audit (if present in the final validation section): full basis Gram/Hermitian spectrum and exact rational source asymptotic checks. Same agent and same mathematical inputs: not blind independent referee.
- Repo-wide `python -m unittest discover` and GitHub CI are **NOT RUN OR WAITED FOR** in this round (long CI explicitly discouraged). No new Lean kernel theorem is claimed.
- Claim status: mathematical finite operators/proof identities DISCLOSED in stated domain, implementations OBSERVED on focused tests, physical quantum compilation/quantum speedup/π normality UNVERIFIED or OPEN.

- Additional circuit: `CIRCUIT.qasm` is an OpenQASM 3 controlled-branch-increment sketch, accompanied by a **32-case** exhaustive gate truth table check and the exact character-state monodromy identity. **No OpenQASM parser or quantum device execution was available.**

- **Actually executed:** `18 tests ... OK` in 0.031 s with `-W error` on the local focused suite; independent NumPy/SymPy oracle PASS: direct orthogonal projector derivation, unitary matrices, Hermitian spectra, symbolic coefficient `675/128`, normalized chirality `16`, heralded echo `11/18`.
- Artifact SHA256 manifests are generated and checked before publishing. Draft PR commits and hosted CI status are reported separately; CI is not assumed green.
