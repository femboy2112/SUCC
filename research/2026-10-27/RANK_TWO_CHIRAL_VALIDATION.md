# Operation E² — Exact validation and claim authority

**Date:** 2026-10-27. **Working branch:** research/rank-two-chiral-e-tower-source-gluing-2026-10-27, stacked as independent research child on #331 at exact parent d47ff32e47104cca73264d99c9ec1088f20e7c1f. Original four signed source poles, zero initial condition and all historical imports unchanged.

## Verified local execution (not a full native CI run)

From an isolated executable package containing the *exact same* production/test/probe Python bytes:

- PYTHONPATH=/mnt/data/rank2_research python -m unittest discover -s /mnt/data/rank2_research/tests -p test_rank_two_chiral_towers.py -v: **17/17 passed** in 0.434 seconds, after the initial locally fixed keyword-only test-call mistake. Full test log preserved in the separate downloadable research archive.
- PYTHONPATH=/mnt/data/rank2_research python scripts/rank_two_chiral_probe.py --write research/2026-10-27/RANK_TWO_CHIRAL_RECEIPT.json --verify: **RANK TWO SOURCE AND RECEIPT VERIFIED**.
- Separate **SymPy** implementation on independent 4×4 rational block matrices: exact T^4=−J/4, T^8=I/16, literal resolvent K(t), controllability determinant 1/8, observability determinant 32, Hankel determinant 4, individual signed chiral masses and three source asymptotics. Output: **INDEPENDENT RANK-TWO SYMPY CHECK PASSED**.

The following locally tested content has matching uploaded repository Git blob identities (SHA-1 in ordinary Git blob format):

| Source path | Exact blob SHA |
|---|---|
| observational_succ/rank_two_chiral_towers.py | 8305e09892f19007e0ae0538a60d05954b2def9e |
| tests/test_rank_two_chiral_towers.py | 563ddd76890e37af1aae94d1f7333390120047eb |
| scripts/rank_two_chiral_probe.py | cba88bb84e80e746a9b1536e30310cd7bf938dda |
| research/2026-10-27/RANK_TWO_CHIRAL_RECEIPT.json | eaaf143b24af9fa61757e7449347b448668b95ae |
| research/2026-10-27/rank_two_independent_sympy_oracle.py | e5326f1d2888fe2b877bf6750cc01f3d616b457b |

**The first local test invocation failed due to a positional argument in a keyword-only test method; this was repaired in the test, not the production mathematics.** This failure is retained in conversation/tool execution history; no invalid theorem was promoted.

## Independent falsifiers and scopes

- Wrong conjugate gain g versus bar g violates J L+ J=L−.
- Erasing the odd channel leaves c1=2 rather than zero; flipping odd readout signs loses the authentic four-pole source.
- Strict J-fixed diagonal constraints forbid individually actuating two coordinates while remaining in the constrained graph; the full K² algebra permits independent coordinate multiplication.
- The common-bit demonstration's covariance 1/16 uses a declared joint support and **does not** mean the original π source is random.
- The real Weyl phases of *contracting source impulses* average to one; applying them instead of expanding U_n is refuted by an explicit O_h(1) phase-error bound.
- Changing the real initial seed while retaining forcing is a separate untested selected-Weyl obstruction; previous #320, #327, #328 and #330 countermodels still apply.
- The Gaussian module has rank two but its coupled source successor is only Q-linear; claiming K-linearity would be false.
- These 17 finite tests are not an infinite proof by enumeration. Paper analytic identities come from finite exact matrix algebra and classical integration, with explicit hypotheses.

## Hosted/native authority not preclaimed

Do NOT call this a full native repository pass, original import provenance verification, observer/ordinal suite pass, or Lean theorem proof until those **exact head** checks have run. The separate SymPy audit is not independent experimental/physical evidence. External scholarly novelty/prior art for the assembled construction remains UNVERIFIED. **Neither base-16 nor base-3 π normality or RH is proved.**

Required future native gates:

~~~sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python scripts/rank_two_chiral_probe.py --verify
~~~

Research continuation: prove a signed real-circle cross-correlation estimate for actual source-selected U+ and U−; independent multiplicative module gains alone do not imply such cancellation.
