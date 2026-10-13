# Third moonshot swarm integration audit — 2026-10-12

Canonical record of the consolidation of the **third** 2026-10-12 swarm (claims
**O333–O471**, 139 new ledger entries) into `main`. Written so a new researcher or a
fresh session can understand what was merged, what survived adversarial audit, and
what remains conjectural **without reading any prior PR thread or agent transcript**.
It follows the first consolidation ([SUCC stack](./CLAIM_LEDGER.md), PRs #6–#22) and
the second ([`MOONSHOT_SWARM_AUDIT_2026-10-12.md`](./MOONSHOT_SWARM_AUDIT_2026-10-12.md),
O269–O332).

## What the swarm was

Nine remote branches surfaced in three wordless `git pull`s. They are **two stacked
research chains plus one trailing commit**, all rooted on commits already in `main`
(`dc10930` the dual-E tip, `2414c23` the logistic tip — both consolidated in swarm 2):

| Lineage | Superset tip | New claims (original numbering) | Content |
|---|---|---|---|
| **Field / adelic** (off `dc10930`) | `d1e6494` (`field-relative-closure-obstruction-calculus`) | O321–O418 (98) | diagonal-Q adelic/zeta, dynamic Fourier + virtual Mellin zeros, shadow-SUCC/FUCC, carrier/covariant/field-relative Meta-SUCC |
| **Logistic II** (off `2414c23`) | `b9d84bb` (`misiurewicz-chaotic-phase-e`) | O333–O360 (28) | source-admissible chaos quotients + the Misiurewicz positive-entropy phase quotient |
| **Historical** (off `d1e6494`) | `f44bb04` (`historical-maxwell-lorentz-obstruction-repair`) | O419–O431 (13) | Galilean→Lorentz / transverse-Maxwell exact 1+1 source-repair case study |

The six intermediate branch names (carrier, covariant, adelic-zeta, observer-fourier,
shadow, chaos-quotients) are nested snapshots of these same DAGs.

## The integrity defect: a three-way ledger-ID collision, and its fix

All three lineages forked **independently** and re-used the same ID block, because each
forked at a point whose ledger ended at O320 or O332 and none knew about the others:

- `main` already used **O321–O332** for the logistic CT series (swarm 2).
- the field lineage re-used **O321–O418** for adelic/Fourier/shadow/Meta-SUCC claims — colliding with main's O321–O332.
- the logistic-II lineage re-used **O333–O360** — colliding with the field lineage.
- the historical lineage re-used **O419–O431** — colliding with the logistic-II block once field was shifted.

Resolved by renumbering each lineage onto a disjoint contiguous block, leaving main's
O1–O332 untouched (single-pass, no-cascade shifts applied in each lineage's own tree,
where the shift is unambiguous):

| Lineage | Original | Consolidated | Shift |
|---|---|---|---|
| field / adelic | O321–O418 | **O333–O430** | +12 |
| logistic II | O333–O360 | **O431–O458** | +98 |
| historical | O419–O431 | **O459–O471** | +40 |

Final ledger is contiguous **O1–O471**, 471 distinct IDs, zero duplicates, zero gaps.
Consolidation is purely additive to pre-existing `main` files (no deletions). Only the
shared append-target files (ci.yml, README, ARCHITECTURE, ROADMAP, CLAIM_LEDGER)
required merge resolution; every resolution was a union, and the swarm-2 de-hype
correction of the dual-Riemann-sphere paragraph (which the field lineage, forked before
it, would otherwise have reverted) was explicitly preserved.

## The crucible: six independent adversarial bearings

Each cluster was re-derived **from scratch** by an independent read-only auditor in its
own exact-arithmetic code (not the repo's tests, not the ledger labels). All six passed;
collectively they found **zero wrong mathematical claims and zero firewall breaches**.
Load-bearing numbers independently reproduced:

- **A — adelic / zeta / Archimedean (O333–O346).** Diagonal-Q reciprocity (q=1/6: 1/2+2/3−1/6=1; global product 1; true-prime gate rejects fake p=6); CRT recovery bound M>2H²; the unobserved-prime escape q_n=M_n/(M_n²+1). **O345 (DZ8)** self-dual f_r with C_2(2)=C_2(−1)=3/2, C(0)=C(1)=1 — refutes "self-duality forces the standard Gamma" (its zeros stay **on** the line). **O346 (DZ9)** the off-critical falsifier: C(s)=[11/10+4^−s+4^(s−1)]/(47/20), zeros from t²+(11/5)t+1=0, exact discriminant 21/25, roots (−11±√21)/10, giving zeros at Re(s)≈0.180 and 0.820 — strictly inside 0<Re(s)<1 and **off** 1/2 — a correct counterexample to "completion ⇒ RH", with the actual ζ untouched and no zero positions used as inputs.
- **B — dynamic Fourier / virtual zeros (O347–O359).** Finite Fourier naturality Z/M→Z/N and tower composition; omitted-energy debt [1/2,1/4]→3/4; alias hidden energy 2; the C_ε family with off-line zeros exactly for 4/5<ε<1 (DZ9 is ε=10/11, C(2)=413/188) and C≡1 at canonical ε=0; the shear descent criterion U(ker A)⊆ker A with obstruction [1,0]; the 2/n² vs 2n unbounded-norm no-go.
- **C — shadow-SUCC/FUCC (O360–O375).** Genuine source underdetermination (1500 instances, 0 mismatches); SF7a global polynomial reconstruction [1,0,1] with its own Bézout; Gaussian-mixture variance rigidity vs the strictly-positive Hermite impostor (C(2)=1); SF8+ for primes [2,3,5,13] — pairwise coprime, joint amplitude infimum 0 by Kronecker density with an explicit height witness ⇒ no height-uniform decoder (scoped to THESE test vectors).
- **D — Meta-SUCC categorical stack (O376–O430).** Wigner rotation 40/41, 9/41 from v=3/5 boosts (40²+9²=41²), perpendicular boosts non-commuting; finite-set Beck–Chevalley holds iff full pullback (18,440-case enumeration), with the destructive-measurement commuting-but-undecodable countermodel; Horn confluence (18,000 runs), the 256 two-state/two-action machines {rank 1: 192, none: 64}; field trichotomy min-unsat-core 3, holonomy [3], min repair 2, NP-complete reduction (300 instances); **the Gaussian sieve 2304 survivors / 4356 edges / 243 components / max 580** reproduced by two independent survivor definitions; the analytic falsifier off-critical zero exactly 1/4+i/10 with ξ untouched. The one genuine categorical theorem is finite-set Beck–Chevalley; the rest is honest vocabulary over elementary set theory, and the docs admit the fibration/Yoneda framing is aspirational.
- **E — chaos II + Misiurewicz (O431–O458).** Terminal relative length r(1−r/4)=3/4 at r=3 (the "1/8" is the admissible preimage root of y=21/64, not the length); phantom root 7/8 vs source mean 1/8; r=4 window Markov chain rank one; Misiurewicz minimal polynomial r³−2r²−4r−8 (α=2·tribonacci), 3×3 adjacency [[0,0,1],[0,0,1],[1,1,0]] with spectral radius √2 and topological entropy **½ bit**, phase entropy 0; dual-E covariance (−1)^lag/4 → +1/4 under parity transport; 2/5 and 3/5 collapse after one logistic step; 14-step path count 128=2⁷.
- **F — historical Galilean→Lorentz / Maxwell (O459–O471).** Free-particle Galilean covariance (transformed velocity 11/15); the 1+1 vacuum wave operator's Galilean failure residual **−42/25** at v=3/5 and Lorentz residual **0** for all v (γ=5/4); flux S−vI not repairable by pointwise field mixing (trace invariant); two-null-ray+clock reconstruct Minkowski uniquely (λ₁=½ at v=3/5), cone-alone scale-ambiguous; velocity addition 15/17. O427 (failed square ⇒ unique ontology), O469 (metric resolves ether existence) are **REFUTED** (a coherent moving-medium alternative fits); O471 (physically attests 1887/1905, full Maxwell, GR, RH) is **UNVERIFIED**.

## Firewall status: intact

No claim identifies a source-to-Weil form, an Archimedean Γ-factor, RH, physical/ether
authentication, a physical/cognitive Lorentz law, quantum holonomy, or an all-D/all-K
existence theorem. Every such statement is stamped `REFUTED` or `UNVERIFIED` in the
ledger (O344, O345, O346, O356, O359, O365, O366, O367, O370–O372, O374, O394, O408,
O409, O427, O469, O471, …), echoed in README/ARCHITECTURE/ROADMAP, and asserted as
executable `is False` flags inside CI (`rh_proved`, `gamma_forced_by_finite_prime_data`,
`full_adelic_fourier_or_RH_proved`, `RH_or_Weil_positivity_proved`,
`physical_source_authenticated`, `RH_or_Weil_positivity_proved` (galilean),
`empirical_source_authentication`, `historical_simulation_not_historical_experiment`, …).

## Corrections applied during consolidation

The crucible found exactly one systemic quality nit — status flags **hard-coded `True`**
that assert a nontrivial fact instead of computing it — plus one actively-misleading
test. The genuinely computable / misleading cases were fixed (values unchanged; every
touched receipt stays byte-identical):

1. **`adelic_theta_completion.offcritical_self_dual_zero_witness`** — the off-line /
   in-strip / countermodel flags are now DERIVED by exact rational arithmetic
   (distinct real roots ⇒ R≠1 ⇒ off Re=1/2; `11>10` and `21<81` ⇒ 1<R<2 ⇒ zeros in the
   open strip), not literals.
2. **`field_relative_obstruction_probe`** — `lower_probe_count_1_impossible` now tests
   every singleton candidate against `factor().proved`; `reflection_symmetry` now reads
   the flag `field_analytic_shadow_countermodel` computes by exact s→1−s substitution.
3. **`relativistic_shadow_tower.finite_source_ontology_limit`** — the `report` lambda
   ignored its argument, making `report(a)==report(b)` vacuously true. It now extracts
   the observable law class (`model[0]`), so operational equivalence is a genuine
   computation (a Galilean-observation model would report differently).
4. **CLAIM_LEDGER** — removed 19 intra-table blank lines within the swarm-added block so
   it renders as a contiguous table (main's O1–O332 style left untouched); O421 (the
   Gaussian 580 holonomy) now states it is a **sieve OVERAPPROXIMATION**, not a
   prime-moat bound; O469's garbled claim text reworded (status/evidence unchanged).
5. **README** — the Galilean heading "SUCC **discovers** missing Lorentzian geometry" →
   "SUCC **reconstructs** Lorentzian geometry from null-ray shadows" (the metric is the
   simulator's declared source).

## Recorded nits (deliberately NOT changed)

- **Theorem-application flags** such as `shadow_zero_divisor`'s
  `infimum_joint_absolute_multiplier_amplitude: 0` and `prime_logarithms_rationally_independent: True`
  are explicitly-attributed conclusions of named classical theorems (unique
  factorization + continuous Kronecker density) that hold for any valid distinct-prime
  input. They are left as cited-theorem conclusions (`proof_source` is stated in the
  return, `test_vector_source_identity_must_be_verified: True`); faking a finite
  "computation" of an infinitary density result would be a worse rule-8 violation.
- **`unique_physical_model_selected: False`** (galilean) is a firewall disclaimer — no
  unique ontology is ever claimed — not a geometric quantity; constant False, like
  `RH_claimed`/`physical_source_authenticated`.
- **−42/25** is the Galilean wave-failure residual for the chosen witness, not an
  invariant; the invariant object is the defect matrix [[0,−v],[−v,v²]]. The ledger says
  "a true polynomial source solution", which is accurate.
- **O425** bundles a PROVED clause (□ commutes with L_v) and a REFUTED clause (metric
  invariance alone ⇒ time-orientation) under one label; both are correct, the row is
  just compound.
- README/ROADMAP phrases "Euclidean reconstruction" and the various Gaussian-sieve
  "escaping holonomy" descriptions are loose but accurate; the sieve-overapproximation
  caveat is now in the ledger row.

## Bottom line — what SUCC is after this swarm

The swarm adds a large body of **correctly-reproduced classical mathematics** — adelic
Tate/Poisson zeta completion, finite Fourier descent, harmonic Hermite/Gaussian shadow
inference, Kronecker-flow conditioning obstructions, voltage-graph holonomy, finite-set
Beck–Chevalley, logistic/tent symbolic dynamics, the Misiurewicz positive-entropy phase
quotient, and an exact 1+1 Galilean→Lorentz/Maxwell source-repair case study — each
dressed in the SUCC observer/record/proof recipe, with every grandiose SUCC/RH/physical
extrapolation **honestly guillotined** (REFUTED corpses and UNVERIFIED overreaches). Two
original analytic falsifiers are worth naming because they **actively kill** RH-adjacent
overreach: DZ8 (self-duality does not force the standard Gamma) and DZ9 (completion
symmetry does not force RH — explicit off-critical zeros of a noncanonical completed
multiplier). It proves **no new theorem of independent mathematical interest**; the
novelty is the framing/recipe and the disciplined firewall. SUCC remains a **Σ₁ verifier
/ certificate-audit layer, not a Π₂ theorem-prover** (O267).

Validation at the consolidation commit: provenance `SOURCE_PROVENANCE_VERIFIED`,
**1243 tests OK**, all standalone probes exit 0.
