# Codex finite-band launchpad validation

## Exact environment and replay

All new files are additive to research child of #407 (`5f05181339ea97a56999ca8b8ab10a2009c6c84d`). No old source, theorem contract, workflow or main branch changed.

Executed locally in the research directory:

```sh
python -m unittest -v test_finite_band.py > tests.log 2>&1
python independent_oracle.py > independent_receipt.json
```

**12/12 focused Python stdlib tests PASS.** Tests cover original rational source, truncated Green coboundary, two mathematically equivalent Fejér evaluations, all-zero and de Bruijn adversaries, exact hard cylinder floor, rational seam points, random discrete clouds, translated short-arc hot spot, source/pure smoothed transfer, and source-rational Stoneham c3/c5 residue stages.

**Independent implementation:** `independent_oracle.py` does not import the local implementation. It uses the single rational combined BBP numerator/denominator source, rational direct prefixes, a 75-decimal-place mpmath Dirichlet-square Fejér kernel, a separately coded weighted Fourier sum, and exact hard Q counts. All 3 separate `(N,H)` cases PASS with discrepancies smaller than `1e-65`. These finite tests check formulas and implementations; the exact bounds for all N/H are from the paper proof. No independent blind referee or Lean formalization has been run.

**Proof authority:** FB-01/02/04 are elementary paper proofs; FB-05 uses the already published Stoneham normality/weak hot-spot bound and the locally derived deterministic Fejér bound; FB-03 is a conditional implication that depends on the separately audited MS-02 entropy criterion. The **original selected π Fejér upper bound is NOT proved**. No original π-normality or RH promotion.

**Not executed/claimed on this new branch:** full SUCC `10,008` root tests, AGENTS provenance/observer/ordinal checks, exact-head hosted CI before new commit/push, or formal Lean. The parent/recent-sibling CI status must be checked separately. Codex should run these after adding actual research results and preserve failures; the existing mathematics catalog has a documented baseline stale-file issue in sibling branches.

Exact source SHA256 manifest is in `SOURCE_MANIFEST.json`; hash checks verify research bytes, not mathematical truth.
