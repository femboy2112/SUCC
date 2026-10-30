# MAX / ROOT — SUCC order-statistic observer bridge

The exact distributional identity \(\max(U_1,\ldots,U_m)\overset{d}=U^{1/m}\) (independent uniforms) induces \(\operatorname{Beta}(m,1)\). Under SUCC's real source-marked Pólya prime-power process, this is an **observer selection** that induces a bounded Doob h-transform, not a secretly modified arithmetic field. Original source probabilities are recovered when the selected/rejected observer outcomes are retained.

A key hostile control is now proved: **the selected local phase-character has off-real zeros even though its complete infinite path law is mutually absolutely continuous with SUCC's unmodified source, with finite relative entropy**. Thus generic off-axis local zeros do not imply an energetic Maxwell demon. These are **not zeta zeros**, and RH/pi normality remain OPEN.

Read RESEARCH.md for definitions, proofs and explicit rejection controls. Run standard-library exact suite with `python -m unittest -v test_order_stat_bridge.py`, independent symbolic oracle with `python independent_oracle.py`, and countermodel mutations with `python mutation_probe.py` from this folder.

Draft-only, stacked on SUCC PR #356. No original source/BBP/zero selector, historical claim catalog, production code or CI workflow changes.
