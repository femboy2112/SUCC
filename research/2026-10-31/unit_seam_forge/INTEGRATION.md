# Source and branch integration protocol — UNIT-TO-UNIT

**Intended parent:** draft PR #439 exact head `ca156a69cae170b18c5e3c000274525e5d094a4a`, itself stacked over PR #438. **Canonical main:** Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`. Main and all original historical source contracts remain untouched.

Before integration rerun:

1. Compare actual new branch head to commit and tree receipt in the new PR; verify parent ancestry and no unexpected modifications.
2. Confirm only these additive research files and root test are introduced. Do not duplicate `operational_yoneda_descent` or create a new global category framework.
3. Check canonical claim-ID namespace; local `U2U-xx` labels are provisional and must be allocated or mapped to existing IDs by the coordinator without overwriting originals.
4. Confirm test imports use **unique** `importlib.util.spec_from_file_location` module names so they don't collide with previous `independent_oracle` modules in 10k+ discoverable tests.
5. Exact source equalities: original `r(n)` and `U0=0`; original four signed poles, not finite moments only; `pi/16=T(0)` inherited and not guessed; no fake Pisot/Golden dependence.
6. Full gated CI: `python scripts/verify_provenance.py`, `python -m unittest discover -s tests -p 'test_*.py'`, `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py`. Review per-check raw logs and handle failures, no silent environment repair or invented run.
7. On new paper theorems, review the convergence boundary (`Re z>-1/8`), unique bounded tau recurrence, quantum/semigroup history distinctions, jet-depth counterexample and all-horizon U6 transport bound. Finite testing does not certify analytic estimates.
8. Preserve PRs #437–#439 prior hostile controls (changed seed q=1/5, pairwise-Haar triple lock, positive mutated source, signed Zak-band counterexamples), plus U7N positive finite-jet alias. Run fresh holdouts before any new claim promotion.

**No automatic merge, tag, release or publication.** If baseline changes, compare ancestry and re-run exact-head checks before retargeting; never force-update a moving branch.
