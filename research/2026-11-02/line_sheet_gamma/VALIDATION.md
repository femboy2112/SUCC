# Validation / reproducibility / claim ledger

**Date:** 2026-11-02. **Scope:** pure additive research child of SUCC PR #473 head 80dc4d8b54574e03843f198ff833e2add469422a. New test source and source probes do not modify original poles, U₀, formal, workflows or main.

## Locally executed

- Python 3 stdlib stage: **16/16 new focused test cases PASS** and the full staged package including **27/27 inherited parent tests** gives **43/43 PASS**; syntax compileall PASS.
- Independent SymPy exact expansion checks (not an original-source independent mathematical referee): \(\kappa(t)=1/2-t/12+t^3/720+\cdots\); \(Q_{\rm BBP}=t/64-7t^2/1024+55t^3/24576+\cdots\); \(Q_{\rm sheet}=t/64-t^2/384+t^3/13824+\cdots\); exact difference \(13t^2/3072-479t^3/221184+\cdots\).
- Exact Fraction algebra and endpoint rational certificates including \(Q_{\rm BBP}(x=11/20)=4950/326599<1/64\), \(L(5)=305/13824>1/48\) and \(L(6)=1/64\). 2000 positive numerical convolution comparisons on a logarithmic t grid and independent high-precision Laplace checks for noninteger s; these are **numerical diagnostics**, not the pointwise theorem proof.
- Pure Fraction source/p-primary all-prime decomposition for epochs A=16,32,64; finite Galois product against explicit two-prime automorphism enumeration at p=17,41; selfscale exact originals A=8..256 and deterministic global Fejér/Minkowski upper bounds on finite samples.
- Three preregistered *fresh* source exact dyadic epochs A=512,1024,2048: **3/3 PASS** the stipulated finite threshold \(\mathscr C_A<7/2\), with exact collision integers 970,2026,4050 and normalized fractions 485/256,1013/512,2025/1024. All real-source fractions and cell counts exact; displayed joint Galois log10 magnitudes are floats. This is NOT an all-A proof.
- New source module and root-test Git blobs were compared against locally executed content (see hashes below); these are same-implementation byte-identity checks, not external peer review.

## Verified original-module Git blob hashes

- line_sheet.py: 25ca7ee07e54876e7b746f4ca7dda1138d86c92f
- tests/test_line_sheet_gamma.py: 4e25012eecb72da621d18e2214a9867c8c15b5c1

## Explicitly NOT DONE

Native full SUCC 11k+ unittest discovery, scripts/verify_provenance.py, observer_foundations_probe.py, ordinal_succ_report_probe.py, new Lean formal declarations, hosted workflow green for this exact new child (to be checked after PR), or independent external mathematical reconstruction. The native container cannot resolve github.com for a full clone; connected GitHub research writes have exact ref provenance. No merge, tag, release, publication or canonical theorem-status promotion has been requested.

**Verdicts:** pointwise kernel, all-real complete monotonicity and multigalois product are PAPER PROVED within formulas and classical antecedents; finite numerical checks only corroborate examples; the *selected original arithmetic* o(log A) bound is **UNVERIFIED/OPEN**; π normality and RH remain **OPEN**.
