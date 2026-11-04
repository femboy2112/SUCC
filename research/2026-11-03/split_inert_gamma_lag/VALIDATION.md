# Validation receipts and authority boundaries

Pinned parent PR #484 at `057a68c4b4e01439e76c2050c28309a4858b9dc2`.
Preregistration **committed to GitHub before held-out runs** at `2235c5e00dcdfcbb96d5a9eee7709cd25f67848c`; exact branch `research/split-inert-gamma-lag-2026-11-03`.

**Actually executed in isolated local staging:**
- `python -m unittest discover -s /mnt/data/succ_round/tests -p 'test_odd_gamma*.py' -v`: 19/19 new methods PASS, no skips.
- Combined inherited attached Euler-Gamma odd-source tests plus new tests: 36/36 PASS. The 17 inherited tests are from the attached previous conversation's EGO package, which is NOT a committed ancestor. They are shared code-lineage validation, not an independent proof witness.
- `python research/2026-11-03/split_inert_gamma_lag/symbolic_oracle.py --verify`: exact polynomial/kernel derivative checks PASS. Independent SymPy implementation compared against hand rational/source derivations; same reasoner, not blind referee.
- `python research/2026-11-03/split_inert_gamma_lag/probe.py --verify`: exact finite receipts PASS. Predeclared windows A=96,192,384,768; 2,720 actual original source p-residues checked against Fraction through the first two windows. Larger windows check modular prime nonalias and integer product inequalities; no π digits. Gamma holdout s=17,49,113,257 has rational enclosing endpoints. Exact prime source residue checks include both 3mod8 and 7mod8 second inert pole mutations.
- `python -m compileall` on newly staged code/tests: PASS.
- Git working tree/public git clone **unavailable due container DNS** (`Could not resolve host: github.com`, exit 128). This is an access/environment limitation, not a test failure. GitHub connector read parent immutable contracts. Full suite, native root provenance, ordinal/observer probes, new compiled Lean, external referee and hosted CI are NOT claimed.

**Mathematical status:** GL-01..07 paper proofs within their types; GL-05..06 use the CLASSICAL fixed-modulus prime number theorem in arithmetic progressions, not finite extrapolation. GL-06 is a **GALOIS AVERAGE**, not selected real. The original chosen odd cofactor real nearpair/signed Weyl saving remains UNVERIFIED. No RH, π normality or physical Lorentz implication.

**Falsified attempt, preserved:** the initially considered inert p=4k-1 clean window [k,2k) fails at p=47,n=18 (and p=43,n=17). Its first secondary p injection comes from original 8n-3 or 8n-7=3p. Corrected all-n clean interval is [k,ceil(3k/2)). The source-specific prime family is clipped accordingly.

**Independent-provenance boundary:** external PNT-AP, digamma/Gamma, classical Ramanujan and large sieve are established imported mathematical theorems. A new source-specific arithmetic composition does NOT establish a new published theorem or the original π normality conjecture. Alternate computational routes share one source and same human/AI reasoner.
