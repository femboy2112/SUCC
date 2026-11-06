# SUCC: Observer bridge vs Busy Beaver coherence debt

Research-only, additive child of merged main `a673ec95dfac4ef6a61c60222be8b615fd08535d`. The true original BBP recurrence remains unchanged. This package addresses the user's counterexample-in-a-growing-haystack intuition and its consequences for observer-embedded proof construction. It does **not** attempt to prove π normality.

Read `PROOFS.md` first, then `SOURCE_MAP.md`, `CLAIM_LEDGER.md`, `NEXT.md`, and `VALIDATION.md`. `coherence.py` implements exact finite calibration cases; `tests/test_observer_bridge_coherence.py` contains preregistered probes. The Busy Beaver and compactness theorems are paper imports; finite code cannot prove nonhalting or evaluate a general Busy Beaver function.

The main mathematical result is the finite rational-bridge deception `b0(x)=x mod1`, `bM(x)=(M+1)x mod1`, agreeing on every supplied rational probe and both commuting with ×16, together with a **genuine future original four-pole new-prime probe** that refutes the rival. The related moving-switch, hidden-tag, and Busy Beaver examples separate late falsification, model-class noncompactness, and truly unobservable targets.
