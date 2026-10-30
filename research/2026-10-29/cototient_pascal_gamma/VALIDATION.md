# Validation — SUCC cototient/Gamma research, 2026-10-29

Source parent: SUCC research PR #372 head `44912760eca39069ef5b980a492a1feabc9f6149`. No original forcing / seed / main changes.

## Executed locally (complete outputs and exact scope)

1. `python cototient_dual_probe.py -q`: **14/14 unittest methods PASS** in local stdlib. Includes exact signed four-pole Pascal source, Möbius totient/cototient, finite bivariate transforms, finite Mellin normalizers, exact mod-16/prime-power Fourier shells, rank-shift CRT/mass cells, and stable bounded-sequence source reconstruction. An initial test assertion mistakenly compared an odd event at t=0 to total mass 1; repaired the test after examining its own conditional-scope error; no mathematical identity was changed. This failed initial attempt is reported explicitly rather than suppressed.
2. `python independent_cototient_oracle.py`: PASS. Independent SymPy symbolic reductions of complementary PGFs, q16 conditional closed contrasts and covariance. Mpmath direct source-integral checks agree with the completely different signed-exponential finite source reduction to better than `1e-45` for n=2,4,7, both primitive and cototient. Four-cell q6 rank-selection factorial computed at precision 60 dps with derived absolute unnormalized tail `<1e-47` at j=170. Dirichlet finite-part quantities independently evaluated. Raw numerical values saved in `independent_receipt.json`.
3. External primary/reference math pages consulted: MathWorld Cototient; DLMF 27.10, 27.4 and 25.2.

## Verification boundaries

- Exact rational tests certify implementations on the tested inputs; universal claims rely on displayed paper derivations, not the test count.
- Independent quadrature uses arbitrary precision without independently certified interval enclosures. No numerical output proves a universal limit.
- The finite Gamma/log coefficient -γ cancellation is exact from Γ'(1) and normalization; it is not a computed coincidence.
- Global cototient Dirichlet `FP` uses the Laurent expansion at s=2; it is *not* the local conditional Oily differential.
- Cototient stable inverse / Cesàro comparison works for the coherent nonnormal same-forcing counterseed and therefore **does not** imply π normality.
- Original BBP forcing / U0=0, historical contracts, branches, CI remain unchanged. No full root native suite, hosted CI, Lean or external referee run is claimed.
