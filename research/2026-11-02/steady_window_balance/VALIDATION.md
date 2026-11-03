# Execution, calibration, and claim status

**2026-11-02**, exact parent #477 66d85548755920603911f086c5d26addf91c797c. Isolated Python 3.13.5 stage with the parent mirror files/tests and new source tests: **46/46 PASS, no skips**, Python compileall PASS. Inherited 31 source/mirror tests and 15 new window tests. The new three independent modular-vs-Fraction tests were initially accidentally nested inside another method, discovered by test count and repaired BEFORE recording 46/46. Other early implementation issue: direct summation of thousands of enormous Fractions timed out and full decimal conversion hit the Python 4300-digit safety limit. The exact common odd-denominator modular oracle eliminated repeated gcd costs.

**Preregistered fresh holdouts**, A=2048 and 4096; h=1,2,16; phase bins M=16,64,256. All 6 finite chronological costs pass preregistered 0.18<cost<0.32; all 4 spatial h=1 M64/M256 thresholds pass. Temporal costs retained as strict exact integer rational intervals of width 10^-10 and SHA256 digests of full numerator/denominator. Spatial imbalances, collision energies and bin counts computed exactly. No pi digits or external digit tables. The short printed receipts are in HOLDOUTS_SUMMARY.json; running the COMMITTED source probe with --verify gave **2/2 fresh epoch REPLAY PASS**, and --raw regenerates exact hex numerator/denominator (large ~70K-bit modulus). This uses same-reasoner preregistration, NOT independent blinding.

**Git byte-identity of locally executed and remotely re-fetched exact source files:**
- steady_windows.py: 578e210989a8589ee6a1bf3ffd5d6eecf54cedcd
- tests/test_steady_windows.py: 1b61935d77bebc9e4c3c25492d99787a61da3cc3
- probe.py: 4dcc75fe83f7b6d54d630eea854ff307c051a04e
- HOLDOUTS_SUMMARY.json: 6d9a31224ff5584f2d27024b7a1e7571bd72e417

**Finite controls:** exact original odd-denominator source; original U₀=0 finite seam/lag recurrence; full modular vs Fraction oracle equality; half-circle h-even false positive; balanced synthetic phase windows; coherent same-original-forcing changed seed; pseudo-stationarity Ward budget. Complex phase comparisons are floats with slack and are NOT claimed rigorous numerical certificates of a signed universal inequality. The new window-pair arithmetic measurements and threshold comparisons ARE exact.

**NOT RUN/CLAIMED:** full native SUCC >11k suite, root provenance/observer/ordinal reports, new Lean kernel formalization, exact GitHub-child CI success (inspect after draft PR), independent external referee, unbounded source window-balance estimate, π base-16 normality or RH.

**Claim ledger:** residual→automatic dephasing REFUTED by exact controls; asymptotic stationarity but non-Haar possibility DISCLOSED; deterministic antiphase window cancellation identities PAPER PROVED, source-specific all-N premise UNVERIFIED; finite original measurements OBSERVED. Keep draft, don't merge/tag/release/publish without explicit authorization.
