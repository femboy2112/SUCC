# Accelerating Frame / Oily clock: exact test and provenance receipt
2026-10-30. Additive child of SUCC draft PR #397. Main XVI base SHA e18ba565ca540adb7edf3292f5593929e76d91c5. All new files confined to research/2026-10-30/fibonacci_epicycle_demon/. No edits to the original four signed BBP poles, U_0=0, historical contracts, root CI, production, or main.

## Local executed checks

Command:

    python /mnt/data/succ_acceleration/accelerating_frame_probe.py

Actual result from the **final corrected** locally executed source:

    test_acceleration_sensitive_linear_response ... ok
    test_event_order_evidence_ninefold ... ok
    test_first_four_pole_59_jet_of_variance ... ok
    test_oily_clock_rapidity_response ... ok
    test_positive_source_posterior_cannot_detect_source_blind_boost ... ok
    test_source_ratios ... ok
    test_source_sensitive_order_response ... ok
    test_total_grade_invariant_under_clock_split ... ok

    Ran 8 tests in 0.104s
    OK

**Remote byte identity:** the corrected locally executed source has Git blob SHA-1 ca9c7cf3f4e25ef0adddc53a4ec5666d645c09d5. The actual committed branch file accelerating_frame_probe.py was fetched through GitHub and returned **exactly the same SHA** (4837 bytes).

## Disclosed initial defect and repair

The FIRST local run failed 1/8, because the probe incorrectly compared the Oily mean from the **two-full-panel total clock=2** source (5.6580417264...) with the **single conserved total clock=1** source (3.33319417546...). Both quantities are valid for their explicitly different clock protocols; silently importing one into the other is invalid. The test was corrected to require the clock=1 mean and its independent exact normalizer (4/5+log2−γ) before commit. The final committed code passed 8/8. This is an example of a source/passport mismatch caught by a falsifying test, not a claim of new uncertainty in the classical Gamma mixture.

## Controls and exact source calculations

- Rational original R(a)=4/a−2/(a+3)−1/(a+4)−1/(a+5), and Gamma-matched fake 15/a², with all b-moments exactly expressed through finite source shifts R(a+8(k+j)).
- Exact finite model tested at original-source a=1,9,17,73,257; both opposite-acceleration history posterior contrasts are strictly positive. Original and counterfeit contrast differ but the sign of their difference can change at small a (e.g. a=1), so no global sign claim.
- The first source-specific variance difference is −128·59/(15a³)+O(a^-4); exact rational finite a=65536 calculation approaches this coefficient within 2 absolute units after multiplying by a³. Numerical convergence is a holdout check, not a universal proof.
- Fixed-total budget Gamma negative-binomial total-grade invariance, Oily tilt KL identity and golden rapidity probe passed.
- Exact time-order protocol (+,−) likelihood ratio 9 vs reversed schedule, while pooled grade distribution is unchanged.
- The source-blind boost no-go is a direct symbolic conditional-likelihood factorization; finite test cases are illustrations only. The declared source-sensitive detector is extra structure, **not** a physical consequence of acceleration alone.
- External reference for Rindler/Unruh distinction (theory, not physically realized for SUCC): https://doi.org/10.1088/0264-9381/23/22/026 and https://journals.aps.org/prd/abstract/10.1103/PhysRevD.76.064008 .

## Unrun and prohibited inferences

NOT RUN: complete SUCC Python unittest suite, root provenance verifier, observer foundations, ordinal report, hosted current-head CI, Lean, mathematical catalog rebuild, external review. Do not claim actual original-zero-seed signed π normality; no Weyl saving is provided. Positive-carrier observer distributions alone cannot distinguish the coherent same-forcing nonnormal seed s*=-π/16. No physical horizon, Unruh heat, GR curvature or real detector mechanism has been inferred.

Next: derive an authentic source-zero-seed-sensitive **signed carry/phase** current under two time-dependent observation protocols, with explicit history records, q=6 residue controls, four-bit radix16 Walsh modes, higher-jet-matched mutants, and normalized versus unnormalized clock ablation.
