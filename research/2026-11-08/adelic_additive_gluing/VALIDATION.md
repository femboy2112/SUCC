# Validation, independent checks, exact receipts, and honest limits

**Source:** exact four signed BBP poles and literal U0=0. **Parent:** #556 commit `f999bdd8ebd90c80e06a1484e128d1dda31d2fb6`; **pre-registration:** source-only protocol uploaded before held-out computation at commit `b71d766d464a4c45a53e2748db38f874a639faac`.

## Actual local tests (2026-11-08)

- Runtime Python 3.13.5. Local isolation: minimal API-compatible `duck_bbp.forcing` and `lifted_orbit` test fixture with the exact original polynomial, separately checked against the four signed fractions. **This fixture is NOT uploaded** to GitHub. On the target repository, the new module instead imports the existing canonical `observational_succ.duck_bbp` without modifications.
- New `tests/test_adelic_additive_gluing.py`: **19/19 exact methods PASS**. Source comparisons at n1..169; additive CRT at n1..96 and random signed rational controls; all-prime phase cocycle; odd denominator support ≤8n−3 through n145; critical holonomy for A2..256 and k1..5; same-π source coboundary; genuine balanced source p-primary birth histories for (A,p)=(32,73),(80,193),(100,233),(192,457), including every n through 2A; source complement = all other-prime product; full CRT Parseval and TV at A4,8,16,32,64; rejected composite-p and insufficient-cutoff mutants.
- Parent #556 suite `tests/test_adelic_scale_gluing.py` replayed in the same isolated environment after restoring the local test fixture's `lifted_orbit`: **14/14 PASS**. Combined `unittest` run: **33/33 PASS** and exit 0, complete raw output in `LOCAL_TEST_LOG.txt`.
- `python -m compileall -q observational_succ/adelic_additive_gluing.py tests/test_adelic_additive_gluing.py research/2026-11-08/adelic_additive_gluing`: exit 0.
- The first combined run failed 3 parent tests because the **local fixture** had omitted the canonical `lifted_orbit` API; this was corrected in the local test-only stub without touching any repository source. It was not a mathematical regression. The final 33-test run passed.
- Deterministic exact `Fraction` receipt: `PYTHONPATH=. python research/2026-11-08/adelic_additive_gluing/exact_receipt.py --write` then `--verify` both PASS. The JSON `EXACT_RECEIPT.json` contains source and new test SHA256, all finite original state/prime parts and exact holonomy/coboundary inequalities. **No floating input** to the exact receipt.

## Pre-registered genuinely later prime-real clocks

The pre-registered protocol is the *first commit* on this branch and predates the later-source numerical evaluation. The earlier calibration cases (32,73),(80,193),(100,233) were already seen in #556; they are NOT blind data.

For `A=192, p=457` the four real source births are `58,229,286,343`; for `A=320,p=769`, they are `97,385,481,577`. These are exact and independently checked against `p*r(n) modp`, `pU_n modp` and the all-prime additive character reconstruction at **every** point of each held-out epoch. h=1 and h=3 are separately recorded in `FINITE_DIAGNOSTICS.json`, using mpmath at 70 decimal digits with every phase first reduced as an exact rational mod1. **The displayed complex means are finite numerical diagnostics, not interval-certified values or proofs of an all-A limit.**

At A192, h1, the authentic mean is approximately `-0.05560071842055648 + 0.04131505238873005 i`, while the rational epoch-dependent coherent counterseed mean is approximately `0.9999999999989646 − 0.0000013322316906411 i`. At A320, h1, the authentic mean is approximately `-0.05453497325871211 + 0.02167546869283636 i`, and the coherent control is approximately `0.9999999999998659 − 0.00000047950956217995 i`. Both #554 prime-local marginals and complement temporal variation are displayed in the JSON. Actual complement TV/A for h1 is approximately 1.27539 and 1.30874 respectively, so the parent #556 Abel-variation bound remains vacuous.

An independently assembled original four-fraction source implementation in `independent_oracle.py` recomputed the four registered h1/h3 authentic and coherent-control complex readings at **110 decimal digits**. The printed 70-digit-derived double displays were reproduced within 2e-15; full numerical comparison log retained in `INDEPENDENT_ORACLE_LOG.txt`. This is a different arithmetic implementation, not independent scholarly review and not a universal/interval proof.

## Mathematical proof validation and no-go controls

- Elementary classical additive adèle formula AAG1: given a complete rational denominator factorization, reconstruct by exact modular inverse and CRT; tests include negative rationals, denominators 2/3/5/7/11 and huge original source conductors.
- Finite-time transport AAG3: exact rational modulo-1 equality at every sampled step for all small primes, even when p divides no current denominator.
- Four-birth source AAG5/AAG6: p=73/193/233/457, no p² pole in selected horizon, direct pU_n residue oracle and exact real complement recurrence check all stages.
- Full-conductor Haar and Parseval AAG7/8: exact integer counts, no probabilistic or numerical assumptions; Q is exponentially large from already audited PF7 on Main XXI.
- Critical holonomy AAG9/10 and same-π coboundary AAG12: paper bounds are universally quantified and independently tested at finite representative A,k, **not** inferred from tests. No claim of Lean certification for the analytic universal inequalities.
- **Hostile controls:** coherent wrong seed and fully original-source no-π-oracle dyadic epoch-dependent rational seeds have same p-primary source passport while radically different selected real mean; four-point full-conductor sample has exactly zero h1 coefficient yet TV=999/1000; same-π source coboundary changes critical holonomy; scalar holonomies never become Haar at the first natural critical scale. These refute only unearned universal shortcuts.

## Unrun / remaining gates

**NOT RUN HERE:** full 12k+ native SUCC test suite, `scripts/verify_provenance.py`, observer/ordinal foundations probes, full external codemods or branch ancestry integration, new Lean proof kernel, scholarly independent proof review, and exact-head GitHub CI before upload. These must be inspected after publication. The #544/#554 selected real signed covariance and π base-16 normality remain OPEN. A passed finite diagnostic does not promote either status.
