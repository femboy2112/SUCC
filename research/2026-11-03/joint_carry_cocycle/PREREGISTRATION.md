# Original-source joint-carry holdout declaration (before executing fresh cases)

**Date:** 2026-11-03. **Parent:** draft #483 SHA `8383f69f5eb92eb037dde84f686cf3c77e043c2e`.
This commits BEFORE new holdout calculations; same assistant and shared derivations, NOT blinded independent review.

Source is unchanged `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)` with literal `U0=0`. H/G are canonical projectors from #481; do not recast them as physically independent. No pi digits as inputs.

## Exact outcomes we demand

1. At huge dyadic anchors `n=2^k` for **k=23,47,89,193**, evaluate source-specific principal2 via a NEW short-cone evaluator that does NOT construct full U_n. It must equal `-1/2^(k+5)` on H, `+1/2^(k+5)` on G.
2. At the same anchors and `d=0..min(8,floor((k-1)/5))`, verify exact depth `k+5-4d`, including both channels where feasible. This is *validation of a paper general theorem*, never proof by finite extrapolation.
3. Compute the authentic original zero-seeded H/G **real** fraction/carry/odd complement on fresh indices **n=521,877,1327** using an independent common-modulus modular-orbit oracle. Validate the exact real-vs-odd carry identity, original scalar recurrence and zero-source matching. Preserve exact rational carry flags, 2-adic principal parts, odd cofactor phase and original phase; big rational fractions may be recorded by SHA256 with exact 2^-40 bounds.
4. Validate the q2 principal recurrence from first 4096 original source injections (small/modular state only), and compare to independent harmonic/parity clock and short-cone evaluator at sparse indices.
5. New negative controls: source-changed coherent odd cofactor with every desired dyadic q2 anchor but fixed real phase 4/5 and **zero** real/odd carry discrepancy; rational odd-place channel gauge that changes the real carry without altering total phase or q2 principal parts; invalid pre-gluing p2 reduction; universal scaled-precision-tax counterexamples.

No all-scale real distribution threshold is preregistered. Only exact oracle agreement, paper-lemma falsification, source identity, reproducibility and openly separated hostile controls can PASS. All finite statistics are diagnostic. Real Weyl, logarithmic-mesh collision `E_A=o(log m_A)`, and pi base-16 normality remain **OPEN**.
