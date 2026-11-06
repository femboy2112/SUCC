# Validation and exact scope

**Current-work execution:** The research was derived from the original GitHub source contracts and tested in isolated local Python staging because a direct git clone from this container could not resolve github.com. The GitHub branch is written through the connected GitHub tool. Hosted CI for its exact head is a separate result and must not be inferred from the local scratch runs.

**Actual local execution:** 9/9 exact-rational focused tests passed in 0.612 seconds (Python unittest). These covered the four-term versus collapsed-polynomial source (n=1..159); independent common-odd-denominator modular orbit; strict source shear inequality; all 16 tent alias branches and leak positivity; original epoch flux identities; actual signed source flux of both signs; finite escape and exact-duplicate residual; source-correct coherent odd-denominator wrong seed; and the point-mass failure control.

**Receipt:** On the scratch implementation, receipt_probe.py --write FINITE_RECEIPT.json followed by receipt_probe.py --verify FINITE_RECEIPT.json returned EXACT_FRACTION_VALVE_RECEIPT_VERIFIED. Each compact row records a SHA256 of the **complete exact Fraction output tuple**, with rounded decimal values displayed only for quick inspection. A root test test_alias_valve_receipt.py replays this receipt against GitHub branch code. If CI fails, diagnose the uploaded code or receipt; do not claim byte-identical equivalence from similar local implementations.

**Independent implementation scope:** Fraction four-pole source and independently written quadratic-numerator/four-odd-factor source, with a common-odd-denominator modular recurrence. These are different computation paths using the same formula, not independent human referees. No π digits or random assumptions are used.

**Development vs holdouts:** Epochs (A,q)=(8,2),(12,4),(16,4),(24,8) were selected during exploratory development; in particular the pair with negative source flux is NOT a blind preregistered holdout. Exact opposite signs refute a universal sign claim regardless of the discovery procedure, but they cannot establish a frequency distribution or an all-A asymptotic. Fresh independent holdouts remain future work.

**Claims not made:** No native full-checkout local suite, new Lean theorem, independent academic review, source-selected J=o(K), signed Weyl decay, π normality, or RH. All paper proofs retain their domain and quantifier labels. The updated GitHub workflow status should be checked at the exact posted commit SHA.
