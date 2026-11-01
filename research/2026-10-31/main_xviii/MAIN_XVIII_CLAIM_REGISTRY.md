# Operation Main XVIII — claim registry and countermodel ledger

**Research-status.** Epistemic labels for the integrated frontier, the hostile/countermodel ledger,
and the documented scoping caveats. **No mathematical status is promoted.** π base-16/base-2/base-3
normality, the signed Weyl gate `T_N(h)=Σ_{n≤N} e(h·U_n)=o(N)` (`Sbar_N(h)=o(1)`), RH, Weil positivity
(≠ positive covariance), general Collatz, and shifted Lonely Runner `n=18..94` all remain **OPEN**.

## 0. Audit

Three independent read-only reviewers re-derived the load-bearing algebra, re-ran the committed
probes with a compliant interpreter, and checked the firewall wording, one per cluster:
Cluster A (counterfactual carrier), Cluster B (2/3-adic × Gamma/Pisot), Cluster C (carrier path
measure → signed-lag fireworks). The principal resolved the DAG, the byte-copy reconciliation, the
module-isolation reconciliation, the invariants, and the catalog mechanics.

**Verdict: firewall intact across all three clusters; every package INTEGRATE or INTEGRATE-SCOPED;
no DEFER.** Scoping caveats are documentation-hygiene only, confined to quarantined
`research/2026-10-30/` and `research/2026-10-31/` directories, and none changes repo-wide status.

## 1. Cluster A — counterfactual triangle carrier (PR #426)

Verdict **INTEGRATE-SCOPED**. Firewall intact; the "counterfactual" is the reductio hypothesis
"assume π nonnormal", the Ward identity is explicitly seed-blind (a Dirac at 0 and `s*=−π/16` both
satisfy it), and the one "π normal iff" line is the classical Weyl/Wall criterion. Zero-seed/four-pole
forcing genuine (`U_n + T_n = 16^{n-1}π` checked to 1e-20). 11 tests pass; all VALIDATION numbers
reproduced by an independent script.

| claim | label |
|---|---|
| CT-01 hat transport `< q/(16N)` (`ΣT_n < ζ(2)/64 < 1/32`) | PROVED (elementary) |
| CT-02 discrepancy bound; "normal iff fixed-hat occupations → 1/q" | PROVED (classical) / **CRITERION** |
| CT-03 refinement `φ_{q,j}(16x)=Σ_t φ_{16q,j+tq}(x)` | PROVED (exact rational) |
| CT-04 Ward coboundary | PROVED (exact Fraction equality) |
| CT-05 `L1 < (2+8q)/N` | PROVED |
| CT-06 Walsh localization, max bias `≤ (1−16^{-k})M` | PROVED |
| CT-07 / CT-08 / CT-09 | DERIVED, **conditional on nonnormality** (compose MS-01 / FB1 / K01); a necessary defect, not an impossibility |
| CT-10 | OPEN (labeled) |
| CT-11 | OBSERVED FINITE |
| CT-12 forcing-charge tail `< 15q/(32N)`, `Σ_j C=0` | PROVED (elementary); an absolutely summable series with explicit modulus — **not** a finite→global or Weyl-gate result (see caveat A-2) |

## 2. Cluster B — 2-adic × 3-adic × Gamma/Pisot (PRs #427 → #430)

Verdict **INTEGRATE-SCOPED**. Firewall intact. The circle/solenoid **Pontryagin duality is correct**
(`dual(ℝ/Nℤ) ≅ ℤ`; the archive's `ℤ/Nℤ` claim is genuinely wrong and the `SOLENOID_ERRATUM` quotes it
accurately; colimit `ℤ[1/6]`; the solenoid is distinguished from the profinite `ℤ₂×ℤ₃`). Bounded real
Fourier observables are kept distinct from unbounded p-adic norms (TD-07C proves non-uniform-
integrability; the docs forbid substituting a p-adic norm for the bounded phase). All four test files
pass (77 tests).

| claim group | label |
|---|---|
| TWTH-01/02 joint 2/3-adic Haar, isometry `v2(U_s−U_t)=v2(s−t)`, Γ-bijection | PROVED LOCAL (conditional on inherited DSI-4) |
| TWTH-03 / 03B continuous-decoder no-go (solenoid) | PROVED LOCAL — genuine reconstruction obstruction, **not** a normality statement |
| TWTH-04/05 tripling carry, hat refinement, transport | PROVED LOCAL (Δ→0 not established; docs say so) |
| TWTH-07 Vinogradov + sparse-α control | CLASSICAL |
| TWTH-08 Rudolph–Johnson contract | CONDITIONAL (OPEN premises, incl. Furstenberg) |
| TWTH-11 spectral action on `ℤ[1/6]` | PROVED LOCAL (trivial; honest hostile control) |
| CP-01..10 Pascal 2↔3 conjugacy `H` | PROVED / Verified (CP-02/07/08 CLASSICAL); `H` is a declared chosen map, not a source-derived morphism |
| HP-01..08 half-power horizon, 2-adic ramification, 6-adic successor | PROVED LOCAL / classical |
| TD-01..07 three-place Gamma difference resolvent, 3-adic pole depth, prime **exposure** | PROVED LOCAL (`P(t)=(1−t)(t²+2)(t²+2t+2)`; densities `4/3^k`; `E[d]=5/3`) |
| TWTH-09, TD-08, CP-09/11 | OPEN (labeled) |

## 3. Cluster C — carrier path measure → signed-lag fireworks (PRs #431 → #435)

Verdict **INTEGRATE**. Firewall intact; the open gate is spelled out as
`limsup L_{N,⌊log₁₆N⌋}(h;0) ≤ 0`. §7 of `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md` matches the dossier
body clause by clause. No Lean claims (`formal/` diff is empty; docs say "paper proof, NOT Lean
kernel"). 140 Cluster C tests pass; committed receipts reproduced exactly (`receipts/SHA256.json` 0
mismatches); an independent 40-digit recomputation of the signed scores falls inside the stored
intervals.

| claim | label |
|---|---|
| T1–T4 transport bound, `|C−D| ≤ √(11|h|(16^k−1)/14)`, weighted `≤ 8⌈√(11|h|/14)⌉4^K/(9K²N)`, usable clock `K=⌊log_4 N⌋` | PROVED (paper); finite check Verified |
| BND-01 two-scale Jensen inequality | PROVED (classical convexity) |
| BND-02 original ⇔ doubled-clock signed criterion, within the BBP forcing family | PROVED; it is a **CRITERION / gate equivalence**, not progress on the selected bound |
| S1 hostile barrier: at coherent seed, `K∼c·log₁₆N`, `2<c<3`, reduced score → `4/c−4/c²` vs actual → 1, gap `(1−2/c)²` | PROVED (paper); a **NEGATIVE** result (rules out seed-uniform vanishing transport at that scale) |
| BND-03/04 dyadic-rounding near-zero irrational seeds, `< 22|h|/(105M²)`, coherence `O(log M)` later | PROVED (paper); **COUNTEREXAMPLE** family (completed point is a dyadic rational, trivially nonnormal; does not touch the zero seed) |
| ARITHMETIC A1–A10 prime-smooth `q=3^a5^b`, limiting signed spectrum `1_{(q/15)|h}` | PROVED (paper); A3 numerically Verified; **COUNTEREXAMPLE** family (pass arbitrarily many low modes while nonnormal) |
| Phase-magnitude vs signed-real audit (clipped helper bounds `|D|`, not `Re D`) | Verified correct; counterexample `(N=2,k=1,h=4,s*=−π/16)` reproduced at 60 digits; no consumer uses the clip as a signed bound |
| Edge-normality gate; 73-point tomography exact at **9 modes**, `h` coprime to 73 | PROVED (paper) / CRITERION; alias checks preserved (`16^9≡1 mod 73`; `N=10,11,12` aliased) |
| Wall rational-seed erratum RM-01/02 | CLASSICAL; correct and **additive** (frozen Main XVI record untouched) |
| finite interval receipts | OBSERVED / reproduced exactly |
| selected `limsup L ≤ 0`, π normality, RH | **OPEN**, nowhere claimed |

## 4. Countermodel / hostile-source ledger

Every proposed proof of the selected signed estimate must EXCLUDE all of these; a seed-blind argument
that would certify any of them normal is refuted on arrival.

| countermodel | character | status |
|---|---|---|
| `s* = −π/16` (same four-pole forcing, `U_n(s*) = −T_n`) | genuinely **nonnormal** irrational seed | decisive required-failure holdout |
| AT-07 seven-pole null `z = w − 2r` | zero seed + all odd conductor depths + coherent phases coexist | source-level coherent control |
| SC-05 block-coherent seed | coherent on a window, uncoordinated authentic orbit is not | control |
| horizon-dependent rational coherent seeds `s_K` | finite-prefix spoofing (state K and N together) | control, not a fixed asymptotic nonnormal rational orbit |
| dyadic-rounding near-zero irrational seeds (NEW, BND-03) | `O(M^{-2})` spoof of the M-term Weyl sum, then coherent | completed point is a dyadic rational (trivially nonnormal) |
| prime-smooth `q=3^a5^b` completed orbits (NEW, ARITHMETIC) | limiting signed spectrum `1_{(q/15)|h}` | pass arbitrarily many low modes while nonnormal; FW-A3 refutes the modulus-only surrogate |
| counterfactual carriers (Cluster A controls): all-zero, period-2, de Bruijn, Dirac at 0 | detector targets | labeled controls only |

The two NEW families (dyadic, `3^a5^b`) together kill any **forcing-only** route to the estimate. The
dossier correctly concedes that a route using the exact `U_0=0` boundary and diagonal rationality is
**not** excluded — that is the real open frontier (see HANDOFF).

## 5. Documented scoping caveats (hygiene; none changes repo-wide status; research prose not rewritten)

**Reconciliation policy:** caveats are recorded here rather than by rewriting the PRs' additive
research prose — this preserves the historical research record and avoids introducing errors into
AI-authored derivations, consistent with the Main XVII integration. None of these touches a canonical
status file; the catalog keys unregistered rows by path, so there is **no machine-level claim-ID
collision** and the 15 namespace-collision tests stay green.

- **A-1 (CT-xx prefix overlap).** PR #426 uses `CT-01..CT-12`; the older
  `research/2026-10-30/zero_boundary_dispersion/crt/` uses `CT-01..CT-08` with unrelated meanings.
  `CT` is not a registered namespace (only `CTW` is). Semantic overlap for a human reader only; the
  one concrete cross-reference (`edge_seed_tomography/PROOFS.md:251` "adjacent to CT-05") predates
  #426 and refers to the older dossier. Left unregistered, consistent with prior rounds.
- **A-2 (CT-12 wording).** README/PROOF call CT-12 "finite↔global certified"; it is an absolutely
  summable forcing-charge series with an explicit modulus, carrying no equidistribution content. The
  text disclaims normality, so this is wording, not a breach.
- **A-3 presentation:** CT-12 ledger row detached from its table; "Rigidity" title over a doc that
  shows the Ward identity is non-rigid; "the reductio is now exact" slightly strong (hedged on the
  same line).
- **B-1 malformed ledger tables** (orphan rows below closing prose) in
  `two_three_joint_carrier/CLAIMS.md` (TWTH-03B, TWTH-11) and `multiplace_bbp_difference/CLAIMS.md`
  (TD-07C).
- **B-2 stale test counts:** TWTH-10 CLAIMS says 15 (file 18); TD-09 CLAIMS says 22 (file 24; README
  appends "Total 24"). HP (14) and CP (21) counts correct.
- **B-3** hat-refinement identity stated for `q=16^m` without the `m≥1 (q≥2)` domain note (the code
  guards `q≥2`; immaterial for `m≥1`). Two weak-but-not-vacuous illustrative tests
  (`test_24` count-derived break; `test_15` sparse-α). `TWTH/CP/HP/TD` prefixes unregistered but
  unique to this cluster (no overlap). Stale "stacked on PR #427/#428/#429" provenance language
  (history, not defect). An "exposure vs survival" glossary line would help.
- **C-1 (helper docstring).** `selected_lag.py` `coherent_lag_lower_bound` is preserved unmodified
  (correct — history not rewritten) and bounds `|D|`, not `Re D`; its key `normalized_lower` and
  docstring do not say "modulus". No current consumer misuses it, and
  `test_signed_lag_fireworks_audit.py` pins the behavior with the 60-digit counterexample. A docstring
  addendum or rename is left to a later PR (non-blocking).
- **C-2 disclosed vacuity:** the `K=17` Weyl upper bound exceeds 1 (vacuous) and fresh positive signed
  scores at several `h` are **disclosed** in `RESULTS.md`; the dossier correctly forbids any
  "universal nonpositive finite inequality" claim.
