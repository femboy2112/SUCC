# Validation and execution boundaries — Operation RETURN SEAM

**Environment:** Python 3.13 standard library in isolated `/mnt/data/succ_crossplace_20261106`; parent source and immutable AGENTS.md audited via connected GitHub. No full local SUCC clone: container `git ls-remote https://github.com/femboy2112/SUCC.git` fails DNS. GitHub branch commits and readback are done via the connected GitHub tool, not via a credential-less git push.

**Preregistration:** `PREREGISTRATION.md` was frozen on GitHub at commit `c0a3bda86236486421a6ffd0502ee366f851e8f5` BEFORE the K=9/10/11 fixed sample and new K9/10 surrogate measurements. Prior k≤8 exploratory data and select denominator bits were explicitly disclosed. No parameter search or retuning happened after new measurements.

**Exact theorem authority:** Theorem RS1/RS2/RS3/RS5/RS9/RS10/RS11 arguments are written in THEOREMS.md with quantifiers. They derive from previously proved V isometry/zero in parent #527 and classical positive expansivity and entropy constraints, not from finite sample inference. A separate SymPy check verified parent DB6 rational derivative identity and DB7 logarithm derivative; this does not count as formal Lean verification or independent peer review.

**Finite reproducible commands:**

```sh
python -m compileall -q bridge.py test_bridge.py independent_oracle.py run_probes.py receipt.py symbolic_audit.py wrong_seam_probe.py
python -m unittest discover -v -s . -p 'test_*.py' >LOCAL_TEST_STDOUT.txt 2>LOCAL_TEST_STDERR.txt
python independent_oracle.py >INDEPENDENT_ORACLE_RAW.json
python run_probes.py >FINITE_RESULTS.json
python wrong_seam_probe.py >WRONG_SEAM_NEGATIVE_CONTROL.json
python symbolic_audit.py >SYMPY_AUDIT_LOG.txt
python receipt.py >FINITE_RECEIPT.json
python receipt.py --verify
```

A **preliminary red run** is archived as `INITIAL_FAILED_TEST_LOG.txt`. It assumed wrong-carry decoding necessarily threw an error. Correct arithmetic showed it can instead produce a *different plausible fraction*; the subsequent test insists on inequality of reconstructed values and passed. A still-earlier scratch probe initially compared fractional rather than unwrapped 2-adic residues and correctly found discrepancies. This is an input/typing defect, NOT a counterexample to original 2-adic Haar.

**Executed scoped result:** 16/16 focused research-local methods PASS, 0 errors/failures; independent arithmetic oracle and rational-return probe PASS; optional SymPy identities PASS; compileall PASS; SHA256 receipt replay PASS. All initial finite failures are retained rather than edited away.

**Independent source:** `independent_oracle.py` independently iterates the authentic original four partial fractions as full unwrapped rational U, then checks held-out p-adic returns and reconstructs fractions using bounded numerators, without importing `bridge.py`. These are two implementations of the SAME underlying mathematics, not blind outside witnesses.

**Fresh finite scope:** exact n=128 for k=9,10,11 real distances >=1/4 and same *unwrapped* residue; original U0=0 and all positive-time poles are retained. Source-return clone independently checked for k=1..10 at n=0,7,43,128. Denominator precision probes k bits at n=73,149,293,587 are exact finite but not an exponential growth theorem. Floating normalized-residue RMS is NOT a rigorous bound on π's infinite Weyl sums.

**NOT CLAIMED:** entire native SUCC 12k+ suite; root `scripts/verify_provenance.py`, observer/ordinal probes; Lean kernel; hosted GitHub Actions exact-head; external referee; π base16 normality; original-source infinite real signed savings; quantum/physical claims; academic priority.
