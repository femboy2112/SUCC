# Validation — infinite cluster/BBP source gluing

**Pinned starting repository state:** draft #511 at SHA \`378a77eefa084225f30a209c27a2b4bc54897e72\`. Original four signed poles and U0=0 are unchanged. These are finite observations, not an infinite-volume theorem or π-normality certificate; exact mathematical infinity results are paper proofs in THEOREMS.md.

## Independently executed source and matrix tests — actual, not proposed

A separate **numpy + exact fractions** script was executed locally with \`OPENBLAS_NUM_THREADS=1\`. The exact source bytes executed are committed as [independent_numpy_probe.py](independent_numpy_probe.py). Git blob SHA of the actual executed local file \`3d90321a8af44792d6abad394567e64b224506da\` matched the blob SHA fetched from this GitHub branch. Its SHA-256 was \`74fb2cdcba2b2997f44c75c8e7626a77039bb2b9112ec6885b3d03e14aff1982\`. The raw output log SHA-256 was \`368f44892b5f591eec5cb0390e043dbcb9000925431c98dac4e4888422dea554\`.

Observed **new, prospectively selected** holdouts:

- N=7,8,9 cluster graph state pure finite preparations, all 24 graph stabilizers equal to +1 within 2e-11.
- Every one of the 21 contiguous cuts has reduced purity **1/2**, consistent with one ebit across the cut (proof of all-N uses single crossing CZ).
- Original zero-seeded source times n=2,5,11, harmonics h=1,3,-2, all N=7,8,9: \(Y_n+Z_n=U_n\) exactly as unwrapped Fractions; all 81 grouped character evaluations m=1,2,3 match \(e(hY_n)\) and \(e(hU_n)\) within 2e-11 after rational circle reduction.
- Prefix marginal consistency m=1..4 for every N=7,8,9: the reduced density matrix agrees with the buffered finite reference state C_(m+1) (including source rotations) within 1e-11 in every matrix entry. This is finite calibration for the quasilocal construction.
- GHZ_N phase coherence vs \(\operatorname{Tr}_{N+1}\mathrm{GHZ}_{N+1}\) for N=7,8,9: the N-level off-diagonal has magnitude 1/2 in the pure state and zero after tracing from N+1. All three new negative controls passed.

The exact observable source phases included (independent Fraction calculation):
- n=2: U mod1 \`1076/4095\`, Y mod1 \`2260/9009\`, Z mod1 \`536/45045\`.
- n=5: U mod1 \`32442016954/78058255275\`.
- n=11: U mod1 \`48891577015658186678698/76784965817741472215925\`.

Separate local checks of the additional pure-Bell-extension obstruction showed: C_2 two-site purity = 1, while the first two-site restriction of C_3 and C_7 has purity = 1/2. This independently calibrates the required mixed finite margins in the infinite cluster.

Raw script output:
\`\`\`text
N 7 source group correlations, stabilizers, cuts, compatible prefix density: PASS
N 8 source group correlations, stabilizers, cuts, compatible prefix density: PASS
N 9 source group correlations, stabilizers, cuts, compatible prefix density: PASS
GHZ_N coherence fails finite partial trace of GHZ_(N+1): PASS 7
GHZ_N coherence fails finite partial trace of GHZ_(N+1): PASS 8
GHZ_N coherence fails finite partial trace of GHZ_(N+1): PASS 9
\`\`\`

The new [stdlib rooted test suite](../../../tests/test_infinite_qubit_source_cluster.py) now has **16 test methods**, including the pure-pair-extension control. **Its exact committed blob has NOT been executed by this session's local container.** We only claim that the independent executed numpy script matches its exact committed Git blob, plus the additional explicitly documented checks. Do not report "16/16 passed" or full native 11k+ SUCC tests.

## Review and correctness authority

- GHZ incompatibility is exact finite partial-trace algebra; numerical N=7..9 checks do not prove the general statement.
- Infinite cluster existence/purity is a classical quasilocal *-automorphism and positive-functional argument; not supported merely by finite diagonals.
- Every contiguous cut one-ebit is a finite Schmidt decomposition across the one crossing CZ edge; numerical purities are calibration.
- Multiparty source character phase identity is the graph-stabilizer/local-rotation algebra; numerical source phases are exact Fraction inputs and floating complex *final output only*.
- No blind external scholarly review, new Lean theorem, full native SUCC run, hosted exact-head CI result or worldwide novelty claim.
- Original fixed-h Weyl, original critical sharp-subinterval rate, base-16 π normality and RH are OPEN.

## Reproduction

From a checkout with numpy available (the independent script uses numpy) and stdlib for the root tests:

\`\`\`sh
OPENBLAS_NUM_THREADS=1 python research/2026-11-05/infinite_qubit_field/independent_numpy_probe.py
python -m unittest discover -s tests -p 'test_infinite_qubit_source_cluster.py' -v
\`\`\`

At a coherent integration gate, separately run provenance, observer/ordinal reports and the full native suite once; do not block further mathematical work on the long CI.
