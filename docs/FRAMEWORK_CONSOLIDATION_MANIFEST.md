# Framework Consolidation Manifest

**Author:** Ravel (research instrument)
**Date:** 2026-10-28
**Branch:** `research/ravel-consolidation-manifest-2026-10-28` (analysis only; read-only on all existing files)
**Scope:** Observational SUCC accretion review — separate the reusable CORE/PRIMITIVE
machinery from single-branch RESEARCH scaffolding, identify duplication, and propose a
minimal shared-primitive layer. **Nothing is deleted, moved, or modified.** This document
is the only new artifact.

---

## 0. Firewall (unconditional, non-negotiable)

This manifest is a **code-structure audit**. It certifies **no mathematics**.

- **π base-16 normality: OPEN.**
- **π base-3 normality: OPEN.**
- **RH: OPEN (separate program).**

No tier assignment, no "authoritative variant" note, and no consolidation priority below
promotes any finite computation, formal-coherence argument, modulus bound, or Weyl/carry
estimate into a cancellation theorem, a normality theorem, or a zero-location theorem.
The exact source contract (BBP four-pole recurrence, `U_0 = 0`, unwrapped exact rationals)
and every status label in `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md` and
`docs/CLAIM_LEDGER.md` remain in force and are not altered by this audit.

---

## 1. Inventory and tier counts

Surveyed `observational_succ/` (646 `.py` modules, 178,353 LOC; all under a single flat
package with no subpackages). Tiers classify **code structure and reuse**, not mathematical
status, provenance value, or correctness. "RESEARCH" is not a value judgment: provenance
scaffolding is deliberately preserved.

| Tier | Definition | Count (of 646) |
| --- | --- | --- |
| **CORE** | Foundational, repeatedly imported, must-stay: exact scalar/field algebra, arithmetic shadows, the transactional engine, and the small canonical circle/Fourier primitives already exported from `__init__.py`. | **~8** |
| **PRIMITIVE** | Reusable building blocks re-implemented (near-identically) across many research modules — should be shared. (BBP recurrence, Weyl/phasor sum, carry transport, Schur/Gram computations, totient/Ramanujan, circle transport.) | **~12–20 canonical primitives; ~90+ modules** carry one or more local variants |
| **RESEARCH** | Single-branch scaffolding tied to one dossier/handoff (per `research/2026-10-*`, `handoffs/`, and one `CLAIM_SUPPLEMENT_*`). | **~640** (the remainder) |

**Tier counts (headline):** CORE ≈ 8 · PRIMITIVE ≈ 15 (canonical) · RESEARCH ≈ 640.

### 1.1 CORE (foundational, must-stay)

- `core.py` — exact `Q(i)` `Scalar`, `Frame`, `Operation`, `BasisLift`, `AffineChart`,
  `rational()` with 512-bit budget; the field-relative foundation. (326 lines.)
- `arithmetic.py` — `Limits`, `ShadowIndex`, `factorization`, `divisors`,
  `structure_birth`, `source_at` (zeta / chi5 fixtures), `connected_audit`. (290 lines.)
- `engine.py` — `Engine`, `Record`, `canonical`/`digest` (SHA-256 journal),
  `conjugate_data`; the transactional event-sourced state machine. (378 lines.)
- `circle_transport.py` — `FiniteClock`, `CyclicOneObjectCategory`, `FiniteDualRefinement`,
  `conductor_birth_2_to_6`. Already exported in `__init__.py`.
- `circle_translation.py` — `CirclePolynomial`, `GaussianRational`,
  `TrigFourierPolynomial`, winding/aliasing witnesses; cross-language exact circle ring.

(Plus a handful of canonical finite/exact primitives already re-exported from
`__init__.py` — e.g. `infinite_realization` enclosures, `gamma_succ_path` — which are
CORE/PRIMITIVE by import graph, not by line count.)

---

## 2. PRIMITIVE tier — highest-value shared primitives

Canonical name · exact one-line math object · existing variant module(s) · most-authoritative
variant (per `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md` and the claim ledger).

The **source contract** is fixed once (frontier §0) and must be the single authority:

> `r(n) = 4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)`, `U_0 = 0`, `U_{n+1} = 16 U_n + r(n+1)`.

### 2.1 BBP four-pole source recurrence `r(n)`

- **Math object:** the literal signed four-pole forcing `r(n)` (index `n ≥ 1`).
- **Variants (≥10 near-identical):** `succ_internal_matrix_walk.authentic_r`,
  `pi_rank_lattice.authentic_r`, `oily_macaroni_transfer.authentic_r`,
  `vacuum_parameter_bbp.forcing`, `bbp_source_memory.forcing` (pole-sum form),
  `duck_bbp.forcing` (single combined fraction `(120n²−89n+16)/((2n−1)(4n−1)(8n−7)(8n−3))`),
  `pi_rational_base_carry.bbp_forcing`, `bbp_natural_carrier.exact_forcing` (+ numerator/denominator),
  `pi_source_collision.bbp_forcing`, `seinfeld_succ.bbp_forcing`, `pi_joint_prime_carrier.forcing`,
  `pi_dyadic_prime_transfer._bbp_forcing`, `twisted_observer_probe.bbp_odd_forcing`.
- **Most authoritative:** `succ_internal_matrix_walk.authentic_r` — the docstring states the
  contract verbatim ("Literal original signed four-pole BBP forcing; first index n=1"), and
  `succ_internal_matrix_walk` is the module named as the exact-math authority for the internal
  matrix walk in `docs/ARCHITECTURE.md`'s header entry. `pi_rank_lattice.authentic_r` is
  byte-identical and carries an explicit `SOURCE_TAG`. **Note (honesty):** both the 4-term and
  the `duck_bbp` single-fraction forms are algebraically identical over the common domain; the
  "authority" distinction here is **not** mathematical (they agree), it is *which module the docs
  point to as the front door*.

### 2.2 Unwrapped exact orbit `U_n`

- **Math object:** `U_n` exact rational orbit, `U_{n+1} = 16 U_n + r(n+1)` (no modular wrap).
- **Variants:** `succ_internal_matrix_walk.original_state`, `signed_pushforward.authentic_states`,
  `bbp_source_memory` (pole-moment machinery), `pi_rational_base_carry.bbp_source_states`
  (returns fractional states **and** literal integer lifts `C_0..C_N`).
- **Most authoritative:** `succ_internal_matrix_walk.original_state` (the unwrapped-`U_n`
  definition paired with the authoritative `r`); the lift-bearing `pi_rational_base_carry.bbp_source_states`
  is the authoritative *carry/lift* variant (see 2.6).

### 2.3 Weyl / Fourier phasor sum `A_{h,N}(x) = (1/N) Σ e(h·x_j)`

- **Math object:** normalized Weyl sum `(1/N) Σ_{j<N} e(2πi·h·x_j)` over an orbit/phase list.
- **Variants:** `pi_normality_moonshot.weyl_sum` (+ `fejer_energy`),
  `signed_pushforward.weyl_gate_value` (Fejér gate statistic over `formal_character`),
  `gamma_bbp_signed_coherence.weyl_orbit_transport`,
  `vacuum_phase_transport.certified_weyl_phase_transport`,
  `lambda_source_duality.selected_weyl_upper_from_branch_defect`,
  `circle_origin_gauge.selected_orbit_weyl_deviation_bound`,
  `poisson_circle_minimal.energy_to_weyl_upper`.
- **Most authoritative:** the frontier names `\hat S_N(h) = Σ_{n≤N} e(h U_n)` (exact-rational
  orbit) as the central object and the equivalence `π base-16 normal ⇔ \hat S_N(h)=o(N)`. The
  most faithful **exact** implementation is `signed_pushforward.weyl_gate_value` (uses exact
  `formal_character` over `original_state`); `pi_normality_moonshot.weyl_sum` is a
  float/mpmath generic-`x` variant (useful for π sentinel but not the exact authority).

### 2.4 Fejér energy band `E(H,N)`

- **Math object:** `E(H,N) − 1 = 2 Σ_{h=1}^{H−1} (1−h/H) |A_{h,N}|²` (band `h < H`).
- **Variants:** `signed_pushforward.weyl_gate_value` (band over `d`), `pi_normality_moonshot.fejer_energy`
  (band `1..band`), `bbp_sparse_carry_transport` gate (frontier §2).
- **Most authoritative:** `signed_pushforward.weyl_gate_value` (exact, section-2 Fejér gate as
  specified in the frontier); `bbp_sparse_carry_transport` is the authority for the *derived
  flat-carry* gate (distinct object — see 2.6).

### 2.5 Literal integer carry / digit extraction

- **Math object:** `carry = floor(16·x)` on a fractional circle state; `digit = floor(16·x)`; the
  literal-integer carry sequence `C_n` and its cocycle.
- **Variants:** `prime_base_carry.circle_carry` + `carry_cocycle`,
  `circle_time_carry.prime_carry_product` / `first_time_carry_defect`,
  `pi_dyadic_prime_transfer.dyadic_carry_branch_certificate`,
  `integer_bbp_carrier.carry_residue16`, `minimal_circle_carry.first_carry_excess`,
  `cyclic_carry_extension.carry_cocycle`, `witt_carry_learning.carry_cocycle`,
  `carry_safe_polyphase.carry_successor_holds`, `bbp_two_adic.carry_memory_mod`.
- **Most authoritative:** no single unambiguous winner. `prime_base_carry.circle_carry` is the
  cleanest `(root, multiplier) → (carry, residue)` primitive; the *BBP-16-specific* literal
  carry is `integer_bbp_carrier.carry_residue16`. **Honesty: I do not name one canonical
  "carry transport" module** — the family splits into (a) generic base-`q` carry, (b) BBP-16
  literal carry, and (c) the *sparse-carry transport budget* (a distinct, load-bearing object —
  see next).

### 2.6 Sparse-carry transport budget (load-bearing, distinct)

- **Math object:** the conductor-birth carry transport budget of frontier §2
  (`carry_kernel_budget`, `birth_carry_budget`, `carry_tail_upper`) on the flat-carry signal
  `b_t = c_t·1_{Q_t=Q_{t−1}}`.
- **Variants:** `bbp_sparse_carry_transport.py` is the sole and authoritative implementation
  (frontier §2 confirms it matches the code). No other module re-implements this object.
- **Authority:** `bbp_sparse_carry_transport` (this is a *primitive-to-be-shared*, not a
  duplicate; the frontier explicitly says it is the gate's code.)

### 2.7 Schur complement / shorted complement

- **Math object:** `S = A − B D^{−1} Bᵀ` (invertible `D`), or generalized
  `A − B D⁺ Bᵀ` (Moore–Penrose) under the range-inclusion hypothesis `ran(Bᵀ) ⊆ ran(D)`.
- **Variants (≥15):** `quantitative_rigidity.schur_complement` + `shorted_complement` +
  `range_inclusion_holds` (sympy, most complete), `reality_pin_selection.schur`,
  `recursive_operator_gluing.certify_schur`, `recursive_proof_capsules.schur_capsule`,
  `source_field_gluing.exact_scalar_schur_gluing`, `observer_global_sign_gate.exact_scalar_schur_source_gate`,
  `suzuki_signed_tail_gate.schur_scalar`, `direct_quotient_schur.exact_finite_operator_schur`,
  `conservative_boundary_flux.schur_port`, `full_prime_resolvent.source_schur_improvement`,
  `one_object_contact_neumann.contact_generalized_schur_pencil`, `observer_schur.schur_envelope`,
  `observer_discovery.schur_envelope`, `source_jump_spectral.exact_polar_schur`.
- **Most authoritative:** `quantitative_rigidity.schur_complement` / `shorted_complement` /
  `range_inclusion_holds` — the only variant that implements the *hypothesis* (range inclusion),
  the Moore–Penrose generalization, and the singular-`D` failure mode; all others are the plain
  `D>0` scalar/2×2 case.

### 2.8 Exact PSD / positive-definiteness test

- **Math object:** decide `M ⪰ 0` (or `M ≻ 0`) for an exact rational/symbolic symmetric matrix.
- **Variants (≥15):** `bochner_kernels.is_psd_exact` + `is_positive_definite_exact` (most
  careful, distinguishes PD vs PSD), `zeno_certificate.psd_exact`,
  `zeno_proof_debt.exact_psd`, `hidden_memory_schur.is_psd`, `one_object_residual_schur.psd`,
  `cofinal_schur_telescope.psd`, `one_object_relative_residual.psd`,
  `finite_gamma_fucc_fredholm.psd`, `observable_redundancy_forms._psd`,
  `categorical_model_bridges._positive_semidefinite`, `directional_source_inverse.psd2`,
  `full_prime_resolvent.matrix_psd`, `nested_schur_envelopes._psd`,
  `categorical_repair_synthesis.positive_definite`, `four_schur_dual_quotient._is_psd`.
- **Most authoritative:** `bochner_kernels.is_psd_exact` / `is_positive_definite_exact`
  (explicit PD-vs-PSD semantics and exact arithmetic).

### 2.9 Gram matrix construction (Fourier/polynomial basis)

- **Math object:** `G_{ij} = ⟨φ_i, φ_j⟩` for a declared feature/polynomial basis (often
  Legendre/trig, often with a derivative or moment weighting).
- **Variants (many):** `gram_mobius.gram`, `four_schur_dual_quotient.polynomial_moment_gram` /
  `derivative_moment_projection_gram`, `prime_active_weil_splines.two_spline_prime_active_gram`,
  `source_four_edge_gram.phase_edge_Young_gram_lower`, `gamma_fredholm_completion.finite_feature_gram_model`,
  `empirical_carrier.gram_example` / `gram_positive_definite`, `directional_source_inverse._gram`.
- **Most authoritative:** no single winner — the "Gram" family is genuinely *many different
  inner products*, not one object re-typed. The reusable core is the **PSD test (2.8) applied
  to a Gram**, not a single Gram constructor. **Honesty: I do not consolidate this family into
  one primitive** beyond the shared PSD predicate.

### 2.10 Totient / Euler-φ and Ramanujan sum

- **Math object:** `φ(n)`; `c_q(n) = Σ_{1≤k≤q, gcd(k,q)=1} e^{2πi·kn/q}` (Ramanujan sum).
- **Variants:** `totient` re-implemented in `cloud_ramanujan_transport.totient`,
  `multiplicative_orientation_gram.totient`, `round2_operators.totient`,
  `all_places_zeta.totient`, `wtf_global_calibration.totient`, `carrier_realization.euler_phi`,
  `dirichlet_cumulants.euler_phi_source`. `ramanujan_sum` in `cloud_ramanujan_transport.ramanujan_sum`
  and `secondary_circle_rigidity.ramanujan_sum`.
- **Most authoritative:** `cloud_ramanujan_transport` (has both `totient` and `ramanujan_sum`
  in one module). This is the cheapest, highest-confidence consolidation target.

### 2.11 Circle / modular arithmetic primitive (`mod1`, `circle`, residue)

- **Math object:** `x mod 1`, `floor(16·x)`, and `circle(x)` fractional part over exact rationals.
- **Variants:** `circle_transport.mod1`, `core` (modular `Frame`), `selected_branch_transport`
  (inline `j = (16*x).__floor__()`), `lambda_source_duality` and `wtf_global_calibration`
  (inline `(16*x).numerator // (16*x).denominator`), `bbp_two_adic` (modular 16 carry).
- **Most authoritative:** `circle_transport.mod1` (already CORE-exported); the *inline*
  `(16*x).numerator // (16*x).denominator` floor-of-16 pattern is the concrete duplication to
  collapse into one helper.

### 2.12 Ramanujan / character sums and divisor sums (number-theoretic kernels)

- **Math object:** `σ(n) = Σ_{d|n} d`, primitive-character sums.
- **Variants:** `rh_arithmetic_carrier.divisor_sum`, `source_path_projector.character_sum`,
  `tate_finite_bruhat_observers.cyclic_character_sum`, `cloud_ramanujan_transport.modulus_partial_sum`.
- **Most authoritative:** `cloud_ramanujan_transport.modulus_partial_sum` (exact `Fraction`,
  clean). `rh_arithmetic_carrier.divisor_sum` is trivial but standalone.

### 2.13 Circle transport (already CORE-adjacent)

- **Math object:** finite clock refinement tower, cyclic one-object category, dual refinement,
  conductor-birth `2→6`.
- **Authority:** `circle_transport.py` (already in `__init__.py`). Keep as-is.

---

## 3. Concrete duplication clusters (near-identical math, ≥2 modules)

Each cluster names a **canonical winner** and leaves the losers untouched (provenance).

| # | Cluster (near-identical math) | Modules (losers) | Canonical winner |
| --- | --- | --- | --- |
| D1 | BBP four-pole `r(n)` / `forcing` | `pi_rank_lattice`, `oily_macaroni_transfer`, `vacuum_parameter_bbp`, `bbp_source_memory`, `duck_bbp`, `pi_rational_base_carry`, `bbp_natural_carrier`, `pi_source_collision`, `seinfeld_succ`, `pi_joint_prime_carrier`, `pi_dyadic_prime_transfer`, `twisted_observer_probe` | `succ_internal_matrix_walk.authentic_r` |
| D2 | Totient / Euler-φ | `multiplicative_orientation_gram`, `round2_operators`, `all_places_zeta`, `wtf_global_calibration`, `carrier_realization.euler_phi`, `dirichlet_cumulants.euler_phi_source` | `cloud_ramanujan_transport.totient` |
| D3 | Ramanujan sum `c_q(n)` | `secondary_circle_rigidity.ramanujan_sum` | `cloud_ramanujan_transport.ramanujan_sum` |
| D4 | Exact PSD / PD test | `zeno_certificate.psd_exact`, `zeno_proof_debt.exact_psd`, `hidden_memory_schur.is_psd`, `one_object_residual_schur.psd`, `cofinal_schur_telescope.psd`, `one_object_relative_residual.psd`, `finite_gamma_fucc_fredholm.psd`, `observable_redundancy_forms._psd`, `categorical_model_bridges._positive_semidefinite`, `directional_source_inverse.psd2`, `full_prime_resolvent.matrix_psd`, `nested_schur_envelopes._psd`, `categorical_repair_synthesis.positive_definite`, `four_schur_dual_quotient._is_psd` | `bochner_kernels.is_psd_exact` / `is_positive_definite_exact` |
| D5 | Schur / shorted complement (plain `D>0` case) | `reality_pin_selection.schur`, `recursive_operator_gluing.certify_schur`, `recursive_proof_capsules.schur_capsule`, `source_field_gluing.exact_scalar_schur_gluing`, `observer_global_sign_gate.exact_scalar_schur_source_gate`, `suzuki_signed_tail_gate.schur_scalar`, `conservative_boundary_flux.schur_port`, `observer_schur.schur_envelope`, `observer_discovery.schur_envelope`, `full_prime_resolvent.source_schur_improvement` | `quantitative_rigidity.schur_complement` / `shorted_complement` |
| D6 | Weyl / Fejér phasor sum | `pi_normality_moonshot.weyl_sum`, `gamma_bbp_signed_coherence.weyl_orbit_transport`, `vacuum_phase_transport.certified_weyl_phase_transport`, `lambda_source_duality.selected_weyl_upper_from_branch_defect`, `circle_origin_gauge.selected_orbit_weyl_deviation_bound`, `poisson_circle_minimal.energy_to_weyl_upper` | `signed_pushforward.weyl_gate_value` (exact orbit) |
| D7 | `floor(16·x)` / circle fractional part | inline in `selected_branch_transport`, `lambda_source_duality`, `wtf_global_calibration`, `twisted_pair_transport`, `path_field_feedback` | `circle_transport.mod1` (+ a new `floor16` helper) |
| D8 | Carry cocycle (`carry_cocycle`) | `prime_base_carry.carry_cocycle`, `cyclic_carry_extension.carry_cocycle`, `witt_carry_learning.carry_cocycle` | **no single winner** — three distinct moduli/contexts; leave separate (honest: cannot consolidate without changing semantics) |

**Duplication cluster count: 8** (D1–D8), of which D1–D7 have a confident canonical winner and
D8 is honestly left uncon solidated.

---

## 4. Minimal consolidation path (proposal, priority order)

Proposal only — **no files are moved.** Extraction into a new small shared layer
(e.g. `observational_succ/primitives/` with `bbp.py`, `weyl.py`, `schur.py`, `nt.py`,
`carry.py`) is suggested, not performed.

1. **BBP source recurrence + unwrapped orbit (`r(n)`, `U_n`)** — the single most-duplicated
   object (12+ copies), and it is the fixed source contract that *must not* drift across modules.
   Justification: one authority prevents silent divergence of the exact source.
2. **Exact PSD/PD predicate (`is_psd_exact`)** — 15 near-identical re-implementations; a single
   correct exact-arithmetic predicate removes the largest class of subtle indefinite-matrix bugs.
   Justification: highest bug-risk primitive with the most copies.
3. **Schur / shorted complement with range-inclusion hypothesis** — 10+ copies of the plain
   `D>0` case, but only one implements the full hypothesis. Justification: consolidate the
   *correct* generalized form so downstream code stops reinventing the singular-`D` case.
4. **Number-theoretic kernels (`totient`, `ramanujan_sum`, `divisor_sum`)** — trivial, exact,
   and re-implemented 7+ times. Justification: lowest cost, immediate de-duplication.
5. **Weyl/Fejér sum (`A_{h,N}`, `E(H,N)`)** — a single exact `formal_character`-based sum
   (from `signed_pushforward`) plus a float fast-path; central object of the frontier.
   Justification: one normalized Weyl definition reduces "is this the same sum?" confusion.
6. **Literal carry + `floor(16·x)` helper** — collapse the inline floor-of-16 pattern into one
   helper; keep the three distinct carry cocycles separate. Justification: removes the most
   error-prone inline arithmetic without touching carry-cocycle semantics.
7. **Gram construction** — *do not* consolidate beyond the PSD predicate; the Gram family is
   genuinely many inner products. Justification: over-consolidation here would erase meaning.

---

## 5. What this manifest does and does not do

- **Does:** classify 646 modules by reuse structure; name 13 canonical primitives; name 8
  duplication clusters with 7 confident winners; propose a 7-step consolidation priority list.
- **Does not:** delete, move, or edit any module; merge branches; assert any mathematical result;
  promote any claim status; change the source contract; or certify π normality or RH (both OPEN).
