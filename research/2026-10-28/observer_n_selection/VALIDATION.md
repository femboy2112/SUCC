# Validation and evidence boundary — 2026-10-28

**Parent:** source-relative demon draft PR #355 head `6770de1d20400115031354ef1a797f3328ff892e`. The three Python blobs in this draft exactly match the local files by Git blob SHA (see manifest below). The research branch adds files only and does not alter inherited definitions, production imports, history or CI workflows.

**Exact local execution:**
- `python -m unittest -v test_observer_model.py`: **11/11 tests passed**; correct source and controlled histories, uniform source, exact snapshot acceptance, two-time disambiguation \(1/7\) versus \(1/5\), whole-path finite rejection, transported KL, coarse-grained KL, and changed arithmetic labels.
- `python independent_oracle.py`: **183 distinct SymPy checks passed**; separate combinatorial whole-history derivation \(P(\omega)=k!(j-k)!/(j+1)!\), marginal summation, Bayesian selection, two-time analytic subtraction, and transported KL. Oracle imports no primary implementation.
- `python -m compileall -q .`: passed. Local finite-history acceptance for \(a=1/4\): depth 1 \(5/8\); depth 2 \(7/16\); depth 3 \(85/256\); depth 4 \(341/1280\). Vanishing infinite-depth success follows the separate measure-theoretic proof, not finite extrapolation.
- First symbolic oracle run failed because structurally different algebraically equal expressions were directly compared; corrected to `sympy.cancel(lhs-rhs)==0`. No mathematical theorem or source coefficient was changed; final oracle re-ran successfully.

**Exact Python Git blobs**:
- `observer_model.py` = `b710e8ed198388f211756d4bb95fc91d16f64874`
- `test_observer_model.py` = `f9fdd8ed4b06fd314f95b45e7ea1b7c9b0c3fd41`
- `independent_oracle.py` = `ea91db39506f6bd2d387f1c5960afb5cc2936aa0`

**NOT RUN:** full repository clone/native root AGENTS provenance+unit+observer+ordinal gates, hosted exact-head CI, Lean, external peer review, randomized blind multi-agent checks. Observed finite tests are not universal theorems. Human cognitive “N-first” likelihood is a hypothesis, not measured. No thermodynamic or RH claim.
