# Independent-source audit receipt — TMF operation, 2026-10-16

**Scope:** branch `research/tate-mellin-prime-fucc-escape-2026-10-16`, parent `b8e147d8d53d4c3bd2e48d1f0ad06f3e59bf1b21` (draft PR #145). New files only; no archive rewriting, main mutation, merge or release. **RH PROVED: NO.** This work operates on the absolutely convergent normalized `Gamma_R(s) zeta(s)` half-plane and on *finite* compact half-density prime jets; it does not supply a signed Weil positivity proof.

## Reproduced parent baseline

Before new code, the parent FGF focused suite passed **36/36**, and `scripts/factorial_gamma_fucc_probe.py --verify` checked its frozen exact receipt plus its independent numeric calibration. Existing parent claims were inspected on GitHub. This is not a full cloned repository due to the current execution environment's lack of GitHub network resolution; local tests executed with `PYTHONPATH` on the existing parent FGF module, plus new modules. The parent commit, branch and instructions were verified through the connected GitHub API. Tests not present in this local partial checkout are **not** reported as executed.

## Local targeted execution

`Python 3.13.5`:

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python scripts/factorial_gamma_fucc_probe.py --verify
PYTHONPATH=. python scripts/tate_mellin_prime_transport_probe.py --verify
```

At the final local source state: **70/70 tests passed**, no failures or skips, and both deterministic exact source receipts validated. The fresh independent Gamma direct integral at `s=2+1.25i` differed from the Gamma_R special function by approximately `3.45e-77` (numerical, not rigorous interval). The independently implemented SUCC natural prefix and prime-rectangle FUCC source differed by ~`0.0018322771` at a fresh holdout, inside their **a priori rational** discrepancy budget. Beta and Dirac approximation errors at `t=0.375,1.25,1.875` are preserved in the exact raw test log; comparisons were only performed *after* deriving the uniform error inequalities.

**Raw test stdout+stderr:** [TATE_MELLIN_PRIME_TARGETED_TEST_LOG.txt](TATE_MELLIN_PRIME_TARGETED_TEST_LOG.txt). **Exact source receipt:** [TATE_MELLIN_PRIME_TRANSPORT_RECEIPT.json](TATE_MELLIN_PRIME_TRANSPORT_RECEIPT.json).

## Controls and independent routes

* **Distinct decompositions:** Gamma integral vs finite Beta/Exp vs finite positive log-Dirac; natural-number Dirichlet prefix vs prime-valuation Euler box. Beta and Exp are NOT independent laws; the prime-box and natural prefix are NOT equal finite carriers. Exact hyperbolic valuation cutoff is separately checked as a finite source bijection.
* **Exact arithmetic:** no Gamma/zeta oracle is used for positive prime-source coefficients or the Fraction-valued analytic truncation bounds. Fake base 6 and a changed 2-prime coefficient are detected by the first mismatching Dirichlet coefficient at 6 and 2 respectively, even while their finite positive-source Gram remains PSD.
* **Boundary:** at `0<sigma<=1`, the positive Euler probability family is certified to escape any fixed finite integer/log region; finite compact prime-half-density impulses remain available. This only refutes a naive *positive-probability limit*, not analytic continuation or RH.
* **Wrong completed factor:** odd real Tate parity, `2pi` scale, and the standalone pole-removal scalar have independent exact signatures; no claim that multiplying an arbitrary entire completion destroys all positivity.
* **Finite induced dependence:** hyperbolic H=6, p=2, p=3 prime activation covariance is exactly `-10800/4118023`, recovering 0 only in the full sigma>1 law with controlled tail.

## Repaired adverse test / provenance

An initial test at finite natural horizon `H=5` revealed that the optional diagnostic `natural_address_6` accessed a source point outside the declared cutoff (`KeyError: 6`). The implementation was corrected to use `address_to_vector.get(6)`; the `H=5` negative cross-prime covariance test then passed. This is a **finite source-domain repair**, not an analytic theorem change. A separate OOM-mutation control rejects rectangular Dirichlet coefficient grids whose estimated size exceeds 200,000 source states before allocating them. The full multi-thousand-test GitHub suite was deliberately **not** awaited or represented as passing.

## Exact Git blob identities of final local files

```text
660a3a81438c7569ea7cf835e0eaf8df4950ff15  observational_succ/tate_mellin_prime_transport.py
6b9344618a2171c8712dd8e91eb782ad2b653e38  tests/test_tate_mellin_prime_transport.py
dc2267bea9499ee7ed0a4762ffacc48932b1a5b4  scripts/tate_mellin_prime_transport_probe.py
e9838267fdd462e6f28ac0dfb1e6fb867a51afdf  research/2026-10-16/SUCC_FUCC_TATE_MELLIN_SOURCE_TRIANGLE.md
dcf9e546ea26036c87d2922f0fd00d9ad2a7e7ca  research/2026-10-16/TATE_MELLIN_PRIME_TRANSPORT_RECEIPT.json
55286d8d348c0d743ff1e11d07bfbfc6bf8fc131  research/2026-10-16/TATE_MELLIN_PRIME_TARGETED_TEST_LOG.txt
7df033acdb5d39570ba004703dd4f5a73d1333c3  docs/CLAIM_SUPPLEMENT_TATE_MELLIN_PRIME_TRANSPORT.md
```

These are SHA-1 Git blob values computed from **exact** local bytes with `git hash-object`. After writing via the GitHub connector, compare each remote blob SHA against the corresponding local hash; do not claim a byte-exact repository transfer before comparing them.

## Truth ledger

**Disclosed within specified domains:** rational quadrature, prime-probability and natural-prefix error bounds, coefficient controls, and finite covariance by exact rational arithmetic plus explicit algebraic proofs. **Corroborated as finite numerical diagnostics:** independent integral and special-function calibrations at specified test points. **UNVERIFIED:** source identification with the full signed completed Weil quadratic form, all-support low Schur positivity, comprehensive third-party mathematical review, and the repository's long full-suite hosted workflows. **Refuted shortcut:** positive completed Gamma×Euler probability Gram alone would imply RH. The missing signed-form identification remains.
