# Validation — original-source Fekete and finite Fourier exclusion

**Source:** SUCC draft #512 exact parent \`effbd923578a160ddbb792265a6a5ed311ff342f\`. Add-only research branch. Original four signed BBP taps and literal U0=0 are unchanged; no input π digits, physical fermion assumptions, original-normality claims or new Lean theorem.

## Actually executed and exact-blob verified

- The independent [research source probe](source_exclusion_probe.py) was executed in a local Python process from exact saved bytes; it printed \`SOURCE_EXCLUSION_FRESH_HOLDOUTS_PASS\`. Test epochs A=9,17,33 were declared before execution in PREREGISTRATION.md. Its **Git blob SHA** \`712944efc5daf1e5b6684bccbf143d20fa4afec6\` and **SHA-256** \`a87e6acfd01d04b23c10a649317e444ea2ddf0ccc2212acce118d4a8867d1460\` were computed on those locally executed bytes. The GitHub connector independently returned the SAME exact Git blob SHA for the committed source.
- [The separate root test suite](../../../tests/test_pauli_fekete_exclusion.py) ran **8/8 unittest methods PASS**, zero failures/errors in approximately 0.300s. Source was mirrored in the intended research path in the local test directory, and the committed source bytes have the same Git blob SHA \`74a9dbfd44357cc0f3a2f0278ce3aab3f3792ea6\` as the locally executed root test file, verified by GitHub fetch. These are focused isolated tests, not the full native root suite.
- Independent exact Fraction original-source evaluator cross-checked the original four-pole taps against the collapsed \(r(n)=(120n^2-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]\). The original unwrapped U_n was kept as exact Fraction until reduced modulo1 for phase observation. The *same four-pole forcing* coherent control was generated as \(-T_n\) from source-only rational future-tail terms; its 40-term truncation has a rigorous neglected-tail cap.
- Each finite frame purity was computed independently from the full M×M complex empirical matrix and from the Fourier-structure formula. Each positive regularized log kernel was computed using the complete pairwise K_r sum, not an unbounded truncated Fourier series. All 3 fresh epochs ×4 distinct configurations passed the stated estimates.
- Root-of-unity Fekete maxima, half-circle hard-core/macro-overcrowding controls and duplicate-point determinant collapse passed. Values and exact limitations in [FINITE_DIAGNOSTICS.md](FINITE_DIAGNOSTICS.md).

## Mathematical authority separate from finite runs

PF1/PF6/PF13 are all-N algebraic/analytic identities with full source-independent proofs in [PROOFS.md](PROOFS.md). The exact source-specific wrong-seed asymptotic PF11 follows from the inherited all-n analytic future-tail bound. No infinite conclusion is inferred from the A=9,17,33 finite floating trig data.

**Outstanding:** independently refereed source-bound proof \(E_A^{\rm BBP}\ge-o(1)\), external novelty priority, full ~11k SUCC suite on exact head, new Lean formalization, and any physical Pauli principle in BBP. Hosted CI exact-head status is recorded separately on the PR; do not attribute ancestor workflows to the child.

**Reproduction** from actual repo checkout:
\`\`\`sh
python research/2026-11-05/pauli_fekete/source_exclusion_probe.py
python -m unittest discover -s tests -p 'test_pauli_fekete_exclusion.py' -v
\`\`\`

The expensive full native suite and provenance are integration gates, not prerequisites to developing an exploratory add-only mathematical source dossier.
