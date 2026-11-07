# Local research validation — 2026-11-06

**Source:** parent SUCC #536 at e463a191d82355c707662bdbfb4bf2150fdd4eb7; original four signed BBP poles + literal U0=0. PR #536 notes exact finite K3 prefix windows; this branch tests independent later epochs, not the same prefix count. No imported source modifications.

**Preregistration:** PREREGISTRATION.md committed at fd4f118a8a44cce1d15e9c42b14e57876cfc2844 before fresh experiments; it fixed A16..256 source/Fejér diagnostics but did not preregister all-real-radius tests beyond the threshold. Initial exploratory all-radius A16,32,64,128,256 are accordingly NOT blind holdouts. Separate PREREG_ALL_RADIUS.md committed at c0c36518ea83a003c0892b312fb3536202e3f1f6 BEFORE new exact all-radius tests at A191 and A319.

**Source math:** ET1–ET4 derivations are explicit in THEOREMS.md. Finite standard-library Fraction code verifies the source identity, averaged real tail bound, weighted frequency sum, and exact all-radius jump-point comparisons. Each odd-epoch holdout compares all distinct rational pair-distance jumps in [1/(A+1),1/2], not just a finite radius grid. Thus these finite K3 claims ARE exact despite no numerical sine/cosine interval proof. Local suite source/phase checks also involve floating Fourier evaluations which are explicitly OBSERVED-FINITE and NOT rigorous energy certificates.

**Executed local commands:**

```
python -m compileall -q epoch_fejer.py all_radius.py test_epoch_fejer.py independent_oracle.py
python -m unittest discover -v -s . -p 'test_*.py'
python independent_oracle.py
python -c 'from all_radius import max_all_radius_ratio; print(max_all_radius_ratio(191)); print(max_all_radius_ratio(319))'
```

**Results:** compileall PASS; final **14/14 focused unittest methods PASS**, zero failures/errors; separately assembled combined-rational `independent_oracle.py` **11 exact state and 4 averaged-source checks PASS**. Exact all-radius A191 and A319 satisfy K3; raw results in ALL_RADIUS_HOLDOUT.json. Floating epoch diagnostics in FINITE_RESULTS.json and NEW_EPOCH_FOURIER_DIAGNOSTICS.json and are explicitly NOT used for theorem proofs. Exploratory all-radius A16..256 completed but their entire giant rational witnesses are not embedded; script regenerates them.

**Honest failure history:** first run 8/10 passing with one flawed `%1` phase-to-float strict comparison and one `circle_states(2A)` instead of `circle_states(2A+1)` indexing mistake; original raw INITIAL_RED_TEST_LOG.txt preserved, tests repaired to exact Fraction modulo equality and correct array horizon, no source model changes. Complete re-run 14/14 passes.

**Not run in this isolated environment:** native SUCC 12k+ test suite at current child head, `scripts/verify_provenance.py`, root observer/ordinal probes, actual Lean kernel, hosted exact-head Actions, independent external peer review. No academic novelty or normality claim. The GitHub read-back of the full child commit, including exact blobs and parent comparison, must be verified after pushing.
