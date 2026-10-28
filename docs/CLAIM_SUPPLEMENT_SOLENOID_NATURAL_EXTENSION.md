# Claim supplement — real/2-adic solenoid natural extension

**2026-10-27, research draft.** Proofs and source references: [real/adic solenoid proof dossier](../research/2026-10-27/REAL_ADIC_SOLENOID_NATURAL_EXTENSION.md); inherited PRs #320, #321, #323, #324 and #328. Original four signed poles, zero-seed proof obligations, frozen archives and main are preserved.

| Claim | Status | Receipt / proof boundary |
|---|---|---|
| SNE-0: R/Z is a topological group isomorphic to sqrt(Z₂) | **REFUTED** for literal 2-adic square-root interpretation | Circle connected/divisible; Z₂ totally disconnected/not 2-divisible; {x in Q₂:x² in Z₂}=Z₂ by valuation |
| SNE-1: solenoid carries invertible ×16 with forward digit-writing and backward digit-reading | **CLASSICAL, explicit derivation** | Mapping-torus quotient (t,z)~(t+1,z−1), forward (x,z)↦({16x},16z+floor16x); explicit inverse and finite tests |
| SNE-2: one coherent solenoid orbit Haar-generic iff its projected real radix orbit is base-16 normal | **PROVED LOCAL** | Character group Z[1/2]; fixed denominator modes become finite shifts of integer Fourier modes; *not true for arbitrary lift sequences* |
| SNE-3: original U_n winding lifts shadow π solenoid orbit | **PROVED from inherited #323/#324 tail** | Exact U_n=16^(n−1)π−T_n, sum T_n=B; fixed m/16^k character difference ≤2π abs(m)B/(16^k N) |
| SNE-4: arithmetic 2-adic phase requires odd-denominator complementary character | **PROVED EXACT** | For u=A/B and q=16^k: u/q=R/q−K/B; counterexample 32/3 vs 0, same mod16 but different integer winding |
| SNE-5: no measurable Haar-preserving equivariant factor from +1 on Z₂ to Haar ×16 solenoid | **PROVED LOCAL with both hypotheses essential** | Odometer rigidity at times 16^j contradicts vanishing Haar solenoid character autocorrelation |
| SNE-5b: no continuous 2-adic time function encoding all winding digits of an irrational α | **PROVED LOCAL** | Finite-valued continuous digit function factors through finite 2-power modulus, forcing periodic digits and rational α |
| SNE-6: moving mode 1/16^N has Cesàro mean tending 1, for every α | **PROVED LOCAL** | Explicit geometric sum bound ≤2π abs(α)(1−16^(-N))/(15N); blocks unsupported growing-character gate |
| Selected S_N(h)=o(N) for authentic zero-seeded BBP | **OPEN** | No signed new order from topology, source time Haar, or finite probes; original four-pole odd-denominator phase is load-bearing |

**Validation scope.** An isolated Python 3.13 local working copy executed 11 focused tests (10 passed, one source-native import skipped) and 30,704 exact hostile rational cross-checks. Three new Python files were staged as byte-for-byte identical Git blobs to those locally tested. Local tests are not a universal proof or hosted GitHub CI. The independent paper derivations support the mathematical claims within their stated domains. Full native SUCC provenance/tests and CI remain pending.

**Falsifiable next gate:** derive an actual source-specific signed estimate stronger than the inherited logarithmic absolute deficit for the fixed integer Fourier modes e(hU_n), using the complementary phase while preserving the original zero selector. Require hostile nonnormal source and changed-selector controls. No merge or proof announcement authorized.
