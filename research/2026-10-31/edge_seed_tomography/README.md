# Operation EDGE / SEED — original-source normality observer and finite signed tomography

**Research only, 2026-10-31.** Additive development stacked on [SUCC CRPM PR #431](https://github.com/femboy2112/SUCC/pull/431), itself based on Main XVII `e8598cfa5d32fd1de8e94a3e458a366a0850d59e`.

The research question is whether a SUCC *carrier-relative measure of difference* can be source-faithful enough to help resolve the selected base-16 π-normality problem. The answer here is precise but bounded:

1. **An actual difference measure:** `d_n=U_(n+1)-U_n=15U_n+r(n+1)`. The **edge orbit is Haar-equidistributed iff the original zero-seeded orbit is Haar-equidistributed**, using source summability and a noninjective-Haar-reflection theorem for invariant measures. This is an equivalent normality gate, not a proof of its value. The factor 15=3×5 connects legitimately to SUCC's local-prime programs but does not replace real-circle signed estimates.
2. **A complete finite phase instrument:** the full virtual-seed intensity `|Σz_n e(h16^n s)|²` remembers every pair ratio `z_n conj(z_m)` in distinct Fourier frequencies. A collision-free finite-prime sampling grid recovers the full pair Gram with source-authenticated exact rational phase classes. For nine modes the **73-point cyclic (73,9,1) difference set**, a finite projective plane of order eight, gives a *minimum-sized alias-free DFT grid* for the 73 labels. These finite designs are classical; the SUCC measurement adapter is new-to-repo.
3. **Exact source-blindness firewall:** any unimodular phase twist has seed-averaged 2nd moment N and 4th moment `2N²−N`, even under fixed finite radix-cylinder conditioning (for the tail). Almost every seed is normal by Borel–Cantelli; the genuine selected seed is **not** justified by that theorem. A changing family of explicitly rational, same-four-pole counterfeit seeds `s_K=-c_K` remains nearly coherent for `N<=K` with rigorous all-N errors. The fixed exceptional seed `s*=-π/16` from PR #431 is nonnormal.

**Primary docs:** [full proofs](PROOFS.md) · [source maps](SOURCE_MAP.md) · [scoped claims](CLAIMS.md) · [next mathematical handoff](NEXT.md) · [validation](VALIDATION.md) · [finite diagnostic receipt](finite_receipt.json).

**Implementation:** `edge_seed_tomography.py` (exact `Fraction` / modular arithmetic), `independent_oracle.py` (different algorithms), `probe.py` (finite float diagnostics explicitly not proofs), `tests/test_edge_seed_tomography.py` (discoverable unit tests).

**Never claim:** `E_N(h)=o(N)`, π normality, RH, source-derived Weil positivity, a universal projective realization of `Spec(Z)`, or that a virtual altered-seed readout is an actualized observation. Those remain unproved or not applicable here.

**Repo rules:** No merge to main, auto-merge, tag, release, publish, change to source recurrence, archival proof contracts or workflow. Draft PR only. Local research labels ESM-xx are not globally registered proof authorities.
