# Operation No-Discard × Oily Log — Validation and authority receipt
Date 2026-10-30. Research branch research/fibonacci-epicycle-demon-normality-2026-10-30. Parent: draft PR #397; original merge base Main XVI e18ba565ca540adb7edf3292f5593929e76d91c5.

## Executed: exact committed source bytes

Command (standalone Python 3, stdlib only):

    python no_discard_oily_probe.py

Final **locally executed** output:

    test_chi2_global_bound_and_jet ... ok
    test_exact_pole_logarithm ... ok
    test_high_grade_code_length ... ok
    test_history_split_unchanged ... ok
    test_oily_kl_under_global_bound ... ok
    test_oily_mean_grade_and_history_cost ... ok
    test_oily_normalizer ... ok
    test_rational_four_pole ... ok

    ----------------------------------------------------------------------
    Ran 8 tests in 0.258s

    OK

**Reproducible Git blob identity:** locally tested source, via git hash-object, has SHA-1 aabd1b395ec3442102c264492fd06056c6a26490; independent fetch of exact GitHub branch file research/2026-10-30/fibonacci_epicycle_demon/no_discard_oily_probe.py returned the same SHA-1 after correction. Initial upload had log_pole_square incorrectly casting Fraction directly into Decimal; first local test run caught TypeError, and a single-line rational-to-Decimal fix was committed. No false PASS claimed for the earlier code.

## Independent calculation / direct integral controls

A separate **locally authored, separately implemented mpmath** integration and 11-test oracle (not byte-identical to the committed stdlib script) checked the same finite-four-pole identity, including independently integrated e^(-ax) Q(x)^2/x against its nine-log expression and original chi-squared.

Independent direct quadrature vs exact log formula, at 65-digit working precision:

    a=17: chi2=0.017581292220609857046...
    a=49: chi2=0.002735985534465368993...
    a=129: chi2=0.00043566075894323273994...

For each, integrated chi2 and algebraic chi2 agreed to absolute error below 4e-42. Additional a=9 tests also passed. Source expression and first-order jets were separately checked with symbolic polynomial expansion (R(a)=(15a²+121a+240)/(a(a+3)(a+4)(a+5)), Q''(0)=-59). The separate mpmath 11-test suite passed 11/11 locally. These checks share mathematical hypotheses, so they are NOT independent mathematical referees or proof of universality.

Limiting OM normalizer: 1.398635450491786049428288845... .
OM prior KL(W||P): 0.1751372384536071698315868... nats.
OM mean total grade: 5.658041726438138958927509... .
Original split entropy: 1.700780393681594031045279... bits.
OM split entropy: 2.117015180927691170188122... bits.

## What tests do NOT prove

- No hosted exact-head CI has been run; complete root SUCC scripts/verify_provenance.py, full unittest discovery, observer_foundations_probe.py, ordinal report probe, Lean, and full mathematical memory rebuild NOT RUN.
- Source-native finite-n grade checks at n=3,5,8,12 do not establish the asymptotic entropy theorem; that relies on the paper proof and exponential-moment/TV controls.
- The paper's published irrationality exponent input is an **external classical theorem**, not derived or numerically checked by these tests. Any N_0 for the derived q>=N/nu corollary is non-effective here.
- The original four-pole source-normalized posterior is NOT a proven stochastic law of π's selected radix-16 digits. No signed zero-seed Weyl saving, RH proof, physical Landauer heat-cost statement, or π normality promotion is claimed.
- Summable marginal KL bounds are not automatically an intertime information budget for a retained latent or a deterministic arithmetic stream.

## Follow-up

For a new selected arithmetic result, build an exact-lossless **intermediate literal carry + grade split + seed-sensitive signed phase** channel and compare original U_0=0 with same-source s_*=-π/16, wrong seed/clock, Gamma-matched and high-jet-matched positive source, and classical normal/nonnormal benchmark streams. Predeclare a nontrivial source-specific all-horizon estimate and independent verification. Retain the original four signed BBP poles and integer branch; no prior reset without accounting.

Status: RESEARCH ONLY. Additive files. Do not merge blindly.
