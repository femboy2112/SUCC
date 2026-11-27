# Execution and validation

## Actual runs

1. Executed the standalone exact probe function in the ChatGPT JavaScript connector runtime. The committed probe.mjs wraps the same function and prints its result. The first development attempt failed because its phase-grid equivalence assertion was malformed; the corrected version uses independent full-grid enumeration, and the entire function was rerun. Added a zero-sentinel guard to the finite selector. No other failing assertion in the final run. Raw result: RECEIPT.json. It records all finite graph survival checks, exact hazard products, tree harmonicity, coupon counts, GA-07 factorial cells and nulls, phase alias/refinement, finite matrix units, cocycle and hexagon controls. All counted comparisons are deterministic integer/BigInt checks, not simulations of infinite behavior.
2. Ran Python standard-library Fraction oracle in the local container independently of JS, using separate algorithms: absorption linear equations, rational coupon/hazard checks, exponent-signature aliases, divisibility root, finite cyclic geometric waiting law and every matrix-product input column at N=6. Raw result: INDEPENDENT_RECEIPT.json. The uploaded Python source and stdout Git blob SHA were checked against the locally executed files: da34780fa55208bd73de5ed1691b3b2c84d7c346 and 82a67809175f9c81243c3c4cb083ba6ab7162ea7. Both runs agree on 32 fully reachable / 17 other three-state graph models and the full list of nine q=4 aliases (zero at q=8) on 38 smooth integers. This is method-separated finite verification, not independent human proof review.
3. PRF-13/14/15 are paper proofs. The Python finite cyclic positive-time analogue is a calibration, not a proof by discretization. No neural training, physical measurements, real analytic numerical clock experiment, or new RH/BBP asymptotic computation ran.

## Reproduce

~~~sh
cd research/2026-11-26/principia_reflexiva
node probe.mjs
python independent_oracle.py
~~~

Node CLI was not executed locally; JS function ran directly. Python command executed locally on the source whose hash is above.

## Repository gates

The local container cannot resolve github.com (git ls-remote failed with DNS error). The repository is accessed and edited through the GitHub connector, so no complete local worktree or repository dependency installation exists in this run. The AGENTS.md full gates (verify_provenance.py, unittest discovery, observer_foundations_probe.py, ordinal_succ_report_probe.py), remote CI and Lean were NOT RUN/NOT CLAIMED. This is a draft PR on the #693 research line, with only an additive dossier and ledger navigation. Verify the actual Git compare and rerun the mandatory gates before integration. No main merge, release, tag or frozen source alteration.
