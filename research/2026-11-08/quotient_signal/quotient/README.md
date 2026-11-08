# A learned quotient that preserves the signed signal

[QS1--6](THEOREMS.md) give a precise affirmative interpretation of the user's
proposal. A transcript observer learns the complementary response `P_F b`;
restoring the declared carrier phase produces `a P_F b`, the optimal
mean-square approximation to `z=ab` in the allowed modulated observer space.

The new sharp finite instrument identity is

    ||P_F - M_a P_F M_conjugate(a)||op²
       = max_occupied_cell (1-|E[a|cell]|²).

For an M-cell local phase partition this is at most `pi² h²/M²`. Hence
learning the carrier makes demodulation and conditional source observation
commute to a controlled accuracy. The error can be small while the retained
signed correlation is large; that can represent successful recovery of a
coherent signal. The source-specific sign remains in the conditional product
and in an exact signed ledger of increments across memory refinements.

The paper includes all assumptions, proofs, source instantiation and gauge
scope. It reuses the existing finite transcript fibers without adding a
parallel category implementation. It does not prove that original-zero signed
covariance decays or identify an Euler--Mascheroni constant in this residual.

Reproduce the independent exact algebra checks with Python 3.12.3, standard
library only:

```sh
python3 -m unittest discover -s research/2026-11-08/quotient_signal/quotient -p 'test_*.py' -v
python3 research/2026-11-08/quotient_signal/quotient/oracle.py --output /tmp/quotient-exact.json
```

Executed: **7 tests PASS; 28 weighted finite families and 3,598 exact identity
or inequality checks PASS**, plus four explicit hostile controls. The oracle
uses Gaussian rationals and nonuniform rational weights, and imports none of
the source, prior projection, or interval engines. Its exact receipt is
[EXACT_RECEIPT.json](EXACT_RECEIPT.json). This is implementation diversity for
finite algebra; the paper and code still share the claimed identities, and
these checks are not an independent arithmetic theorem about the zero seed.

Controls retain arbitrary-gauge failure, equal magnitude/opposite signed
responses, opposing signed refinement increments `+1/3,-1/3`, and a zero mean
error with unit trajectory-reconstruction error. Source experiments and the
Gamma investigation belong to sibling directories and have separate status.

**Original-zero covariance: OPEN. Pi base-16 normality: OPEN. RH: OPEN.**
