# Exact execution, source provenance and limitation receipts

**Repository parent verified live via GitHub connector:** SUCC draft #483, `research/causal-lorentz-dual-gluing-2026-11-03` pinned SHA `8383f69f5eb92eb037dde84f686cf3c77e043c2e`. New branch `research/joint-carry-odd-cofiber-2026-11-03`; preregistration was committed *separately before fresh holdouts* at SHA `2dc96f2116d3a6079a680300f7037a19456ca69c`. This round adds research/tests only. No source/Lean/provenance/production/workflow/main/LICENSE/history changes.

## Exact staging environment

A full local public git clone failed DNS `Could not resolve host: github.com` (rc 128). The code was executed in a STRICTLY ISOLATED staging directory under `/mnt/data`, using the prior exact published parent research ZIPs from PR #481 and #483 as identical source dependencies. Never describe this as native checkout/root CI. The parent code in the ZIPs was NOT modified; tests are importable by standalone source path. The new implementation was independently crosschecked against the parent's explicit Mellin `gaussian_unit_gluing.py` and both original exact integer-modulus and rational Fraction source evaluators.

### Reproducible commands and outcomes (ACTUALLY RUN)

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
# 62/62 tests PASS (37 earlier source/dual tests + 25 new joint-carry tests), 0 failures

python -m compileall -q research/2026-11-03/joint_carry_cocycle tests
# rc 0

python research/2026-11-03/joint_carry_cocycle/probe.py --verify
# EXACT original-source new finite receipt replay: PASS

python research/2026-11-03/joint_carry_cocycle/symbolic_oracle.py --verify
# Independent SymPy exact symbolic receipt: PASS
```

`TEST_LOG.txt`, `EXACT_RECEIPT.json`, `SYMBOLIC_RECEIPT.json`, and `TESTED_FILES.json` preserve the raw result and hashes. The new 25 tests include every source parity class, inverse-denominator p2 principal extraction, long all-k anchor formula, exact source-controlled depth bursts, fresh real binary carry, general random rational crosschecks, exact n=1 carry falsifier, zero-crossing coherent odd counterfeit, odd-sector gauge, and worst-case precision tax.

**Independent paths, not blind witnesses:** the original #481 source was independently computed through a different Fraction/Mellin module; a new integer LCM real-phase oracle validates source fractional states against a separate slow direct Fraction recurrence; a second principal-unit oracle uses Euler-inverse exponentiation rather than `pow(q,-1,2^k)`; independent SymPy recovers source polynomial and symbolic carry coboundary. All are within one model/reasoning session and shared-source provenance. Paper proof controls the unbounded quantifiers.

### Source-scoped finite holdouts preregistered beforehand

- k=23,47,89,193 for **huge** integer source indices n=2^k, plus post-anchor windows d<=min(8,floor((k-1)/5)). All exact q2 anchor principal values and depth equality PASS using only O(log n) source terms, not full astronomical history.
- Exact original source real fractional/carry/odd complement at new indices n=521,877,1327. All original zero-seeded modular source phases, local p2 principal parts, odd cofactor, and boundary formulas PASS. Source numbers themselves have SHA256 and exact outward 2^-40 rational enclosures; no low-precision floating claims.
- Original source 4096-step q2 current stream agrees with separately evaluated harmonic/parity source recurrence. Hash and end-state receipt preserved.
- Rational changed-source coherent odd cofactor with matching dyadic local principal phase but a fixed real phase 4/5 and zero odd-boundary indicators PASS as a **negative control**, not as original-source evidence. Universal precision-tax pairs checked exactly.

### Failures found and resolved before final staging

The initial testing round exposed an ordinary malformed expectation (n=3 is a valid source-memory index) and a **mathematical type mismatch**: a modular real fractional source state is NOT an unwrapped 2-adic original source state. In the actual n=1 case, the original U1=47/15 has odd p2 residue, whereas its real fractional phase 2/15 is even; the omitted integer carry is 3. A naive scaled-sum reconstruction from fractional H/G states was initially tested against the unwrapped U without reinstating this carry. The implementation was repaired to test the sharp gluing-precision formula on *unwrapped* source states, and the n=1 failure became a permanent hostile regression. No stale failing result was silently promoted. An exploratory unwrapped Fraction test to n=512 was too slow, so an independently evaluated exact common-denominator modular evaluator replaced it; no numeric approximation was introduced.

### Not claimed

- No full native SUCC >11k checkout tests, root provenance/observer/ordinal scripts, hosted exact-head CI success, independent external mathematician/referee, or new compiled Lean proof.
- No all-horizon selected real odd-cofactor cancellation, no infinite real histogram/near-pair rate, no π base-16 normality theorem, no RH result, no physical GR/quantum mechanism.
- No proof derived from finite observed values. All unbounded status labels require the separately provided paper derivations.
