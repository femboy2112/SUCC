# Claim Index

Latest research: [Arithmetic Resonance claim supplement](CLAIM_SUPPLEMENT_ARITHMETIC_RESONANCE.md), with source-specific range and two-sided Schur bounds; original sign OPEN.

A concise entry point into the full claim record. Nothing here replaces or deletes a historical
entry; this index **points** into the ledger and the per-feature supplements, and records the few
visible current-status corrections. Status vocabulary follows [AGENTS.md](../AGENTS.md):
`CLASSICAL · PROVED LOCAL · TESTED MODEL · HYPOTHESIS · REFUTED · UNVERIFIED`. **RH PROVED: NO.**

## Master record

- **[CLAIM_LEDGER.md](CLAIM_LEDGER.md)** — the full ledger: **580 `O####` claims**, the adversarial
  suite (§ "Adversarial suite"), the outstanding highest-value claims (§ "Outstanding highest-value
  claims"), the Cambrian campaign section, and the **"Carrier → Tate → Weil (2026-10-15)"** section.
  Integrity: no duplicate `O####` rows (checked); link audit across new docs passed (0 genuine
  broken links, Dimension F).

## 2026-10-15 claim families (Academic Main)

| Prefix | Distinct IDs | Topic | Primary supplement(s) |
|---|---|---|---|
| EC | 10 | edge-category carrier reconstruction (N→Z→Q, Q(i)→C, Ẑ→A_f) | CLAIM_SUPPLEMENT_EDGE_CARRIER_RECONSTRUCTION.md |
| CTW | 14 | carrier → Tate → completed signed Weil; the #131 corrections | CLAIM_SUPPLEMENT_CARRIER_TATE_WEIL.md, CLAIM_SUPPLEMENT_TATE_CARRIER_WEIL.md |
| TSF | 13 | Tate×Suzuki Fourier high-moment coercivity, K-relative positivity | CLAIM_SUPPLEMENT_TATE_SUZUKI_FOURIER_HIGH.md |
| AS | 12 | adelic solenoid + Pontryagin duality + adelic Poisson | CLAIM_SUPPLEMENT_ADELIC_SOLENOID_POISSON.md, CLAIM_SUPPLEMENT_PONTRYAGIN_ADELES.md |
| HC | 11 | Hilbert-carrier 4-adic completion, Suzuki cell integrals | CLAIM_SUPPLEMENT_HILBERT_CARRIER.md, CLAIM_SUPPLEMENT_HILBERT_WEIL_ATLAS.md |
| SCF | 10 | source-field inverse-limit trilemma (Simple/IdealHard/Fucked) | CLAIM_SUPPLEMENT_SOURCE_FIELD_INVERSE_LIMIT.md, CLAIM_SUPPLEMENT_SUCC_FIELDS.md |
| TZ | 6 | idelic/Tate zeta Mellin, archimedean Γ_ℝ | CLAIM_SUPPLEMENT_ALL_PLACES_ZETA.md, CLAIM_SUPPLEMENT_TATE_SOURCE_CONDUCTOR.md |

Further 2026-10-15 supplements: bessel-seven (`TATE_BESSEL_SEVEN_SCHUR`), weighted-bessel-four
(`TATE_WEIGHTED_BESSEL_FOUR`), prime-clock UV (`TATE_PRIME_CLOCK_UV`), eta/Bernoulli
(`TATE_ETA_BERNOULLI`), 1−s reflection diode (`TATE_REFLECTION_DIODE`), one-object residual/shorting
(`ONE_OBJECT_RESIDUAL`, `ONE_OBJECT_SHORTING`), APOLLO prime-domain & source-first interference,
ordinal-ranked SUCC, observer-Tate ATOM, classical unit-origin / Haar clock, prime-completion
obstructions. The complete set is `docs/CLAIM_SUPPLEMENT_*.md` (77 files). The earlier research waves
(Phoenix II #57–99, many-worlds, swarm atlas, Black Sun, Zeno, wild-embedding) retain their own
supplements unchanged.

## Current-status corrections (originals preserved, pointers added)

- **Proof Teeth research update:** [new claim supplement](CLAIM_SUPPLEMENT_PROOF_TEETH.md)
  records PH-01–08 (profinite Hilbert/Fourier), PT-C01–05 (minimum observations),
  genuine Lean upgrades for YX-01/YX-02 and the rational part of YX-03, and
  source-specific Schur trial obstructions. Fourier/analytic Lean proof and the
  original signed Schur positivity remain unproved. The inherited synthesis P5
  phrase treating `sqrt(2)+i*r` (r rational) as noncomputable is corrected there:
  it is computable and witnesses proper inclusion only.

- **AS-04 (integer conjunct) → CTW-02.** `research/2026-10-15/ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md`
  AS-04 preserved the original "finite-adèle span must include *non-integer* scales" necessity. PR
  #131 / **CTW-02** proves integer scales with rational translates already span `S(A_f)` (exact
  disjoint refinement); only the "single prime" necessity stands. The AS-04 row now carries an inline
  **SUPERSEDED** pointer; the original statement is preserved.
- **CTW-11 (REFUTED, with caveat).** "overall scalar recoverable from the log-derivative" is refuted,
  but this is **not** universal root-number impossibility — full global logarithmic data + self-duality
  give `w=(-1)^{ord_{1/2}F}`.
- **CTW-12 / CTW-13 (REFUTED).** Weil-positivity shortcuts carry explicit negative certificates (ζ
  Weil distribution negative on a log2 bump, W<−19/75; self-duality + Euler factors + poles do not
  force positivity).
- **TSF-A (REFUTED GENERALLY).** "every high sector positive ⇒ full Weil positive" is refuted by
  signed low-block countermodels — the low Schur sign remains the open RH-hard object.

## How to navigate

The [Collective Observer supplement](CLAIM_SUPPLEMENT_COLLECTIVE_OBSERVER.md)
adds CO-01–17 on the #140 child branch: modular algebra and conductor interaction,
chronological cooperative policies, rational Gamma aliases, source-preserving
effects, finite formal proofs and the sharper conditional signed-source bounds.
Its dependency manifest explicitly pins sibling mathematics instead of implying
that the independent source branches were merged.

Carrier reconstructions → [CARRIER_ATLAS.md](CARRIER_ATLAS.md). Proof-access classification →
[OBSERVER_PROOF_ACCESS.md](OBSERVER_PROOF_ACCESS.md). What is open and why →
[RESEARCH_FRONTIER_2026-10-15.md](RESEARCH_FRONTIER_2026-10-15.md) and
[SUCC_RESEARCH_DEPENDENCY_DAG.md](SUCC_RESEARCH_DEPENDENCY_DAG.md). How #101–#131 were consolidated →
[ACADEMIC_CARRIER_INTEGRATION_AUDIT_2026-10-15.md](ACADEMIC_CARRIER_INTEGRATION_AUDIT_2026-10-15.md).
