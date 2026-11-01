# Operation SIGNED LAG FORGE — the next selected π normality attack

**Draft research integration, 2026-10-31. π normality and RH OPEN.**

This branch combines the original carrier-relative superposition work of PR #431, the phase-path/alias and exact seed-selection guards of PR #433, and a BYTE-IDENTICAL import of all 11 research/test files of sibling PR #432's source-edge and finite 73-point phase tomography. The new work provides a **source-authenticated, critical-log-depth signed van der Corput lag reduction** and a rigorous finite signed measurement, not just another observational equivalence.

- [PROOFS.md](PROOFS.md): full quantified original four-pole source lag identity, summable source correction, VdC signed lag bridge and critical logarithmic error O_h(1/log N), 3/5 conductor filtration, hostile controls, OPEN normality gate.
- [CERTIFIED_LAG_RECEIPTS.md](CERTIFIED_LAG_RECEIPTS.md): exact rational source-selected finite intervals at N=512,1024,1536 versus the coherent same-forcing nonnormal seed, with reproducible error budgets.
- [CLAIMS.md](CLAIMS.md): scoped theorem/finite/conditional/open statuses and source attribution.
- [VALIDATION.md](VALIDATION.md): 28 actually executed exact standalone tests, independent algebraic oracle, source SHA and honest incomplete hosted/full-run status.
- [INTEGRATION.md](INTEGRATION.md): pinned parent/sibling commits and exact imported source/test paths.
- [NEXT.md](NEXT.md): mathematical route ranking and explicit acceptance gates.
- [ASTRA_ULTRA_HANDOFF.md](ASTRA_ULTRA_HANDOFF.md): detailed ready-to-run execution prompt for Astra Ultra.

Executable research: selected_lag.py (exact rational source/cosine enclosures), independent_oracle.py (independent window energy/source finite check), run_receipt.py (outward finite certificates), and root discoverable tests/test_selected_lag_tomography.py.

**Mathematical focus.** Let U be the authentic rational zero-seeded four-pole trajectory. For nonzero integer harmonic h, define D_(h,k)(N)=Σ_(n<=N-k)e(h(16^k-1)U_n) and signed L_(N,K)(h)=2/(KN) Σ_(1<=k<K)(1-k/K) Re D_(h,k)(N). The new exact theorem bounds selected |S_N(h)/N|² by (1+(K-1)/N)[1/K + L_(N,K)(h)+E] with E≤11|h|/(420K) at K=floor(log16 N). If we can prove limsup L≤0 for every fixed h, π is normal. **That last selected signed inequality remains open.**

**Not allowed:** imply selected π is typical of the auxiliary path superposition; confuse dyadic CRT characters with real-circle Fourier phases; call PR #432's finite phase recovery a signed bound; use fixed finite grids beyond their alias horizon; demand asymptotic failure for rational shifted seeds (Wall says otherwise); infer RH from positive path resistance; or convert finite exact cosines into a universal statement.

Everything is additive on a research branch; no parent, main, frozen history, formal theorem registry, workflow, release, or license is modified. Do not auto-merge.
**Combined CI hardening:** two inherited test files have child-branch-only unique importlib oracle loader repairs (no changes to their source algorithms or assertions); read [INTEGRATION_TEST_IMPORT_REPAIR.md](INTEGRATION_TEST_IMPORT_REPAIR.md). This is an explicitly documented exception to otherwise additive changes and direct blob import. Parent PRs remain untouched.
