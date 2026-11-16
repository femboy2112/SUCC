# Validation and claim boundaries

Research branch is a draft child of SUCC PR #623 (exact ref determined at push). No archival source, mainline, claim ledger, π/RH source, or production defaults intentionally changed.

## Locally executed commands (Python 3.11+ or 3.12+, stdlib)

From a minimal worktree/package containing `observational_succ/observer_gr_bridge.py` and `tests/test_observer_gr_bridge.py`:

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_observer_gr_bridge.py' -v
```

**PASS:** 12 named exact-rational tests. Covers two conformal 2D metrics; massless scalar coordinate action, field response and covariant stress independence; 3+1 nine-null measurement rank and each one-row ablation; 50 seeded symmetric tensors; potential-invisible null energy; R² Einstein-background variation; finite boundary-entropy ambiguity; the Poisson volume/rate calibration gauge; normalization scaling; Jacobson coefficient arithmetic.

```sh
python research/2026-11-14/operational_gr_source_action/independent_symbolic_audit.py
```

**PASS:** independent SymPy 1.14.0 Einstein/Ricci calculation for the 2D and 4D conformal metrics, 2D scalar action/stress Weyl invariance, R² contribution vanishing on the 4D constant-curvature example, finite 2-jet stealth deformation.

**A transient symbolic-domain issue was retained and corrected:** `sqrt(Ω^4)` could not be simplified to `Ω²` automatically without declaring positivity. The independent symbolic audit now explicitly uses `Ω²` on its documented `t<1` patch. This was not a failed mathematical claim.

## Authority

- Exact algebraic scope: the nine-null rank and proof, conformal Weyl identities, boundary bit count, source-counting gauge, 4D Einstein-background R² variation.
- Classical conditional physics: Jacobson local Rindler equilibrium, Unruh heat, Clausius and Raychaudhuri; not deduced from finite observers. No new physical GR result claimed.
- Source-map adequacy: **UNVERIFIED**; no actual clock, heat or horizon entropy experiments.
- Novelty: not established; all fundamental geometric/dynamical ingredients are classical. The nine fixed rational null readout schedule is a new-to-SUCC elementary explicit specialization.
- Full SUCC suite, repo provenance checks and Lean on this combined worktree: **NOT RUN locally**, as the complete repository was not present in this container. GitHub CI must be read on the final pushed SHA; no future pass is inferred.

## Next falsifier

Construct a non-Einstein background with separately calibrated clock, horizon entropy and scalar matter flux. Require the Clausius/focusing relation for nine predeclared null directions, then vary the gravity-action coefficient β of R² and the source entropy coefficient α independently; reject the hypothesis if the same measured data predict distinct refutable outcomes. Do not fit parameters on the holdout.
