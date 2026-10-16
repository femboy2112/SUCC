# Research Frontier — 2026-10-15

A living map of what is established, what is scoped-and-open, and what is RH-hard, after the
Academic Main consolidation (integration head `42f5485`). This separates **six tracks** so a reader
immediately sees why Poisson summation is settled while Weil positivity is not. Status vocabulary
follows [AGENTS.md](../AGENTS.md). **RH PROVED: NO. Signed-Weil global positivity: OPEN.**

## Track 1 — Core algebraic / topological carrier reconstruction

**Status: CLASSICAL, realized as exact finite source charts.** Group completion, localization,
quotient presentations, profinite/CRT inverse limits, metric completion, finite/full adèles.
Documented completely in [CARRIER_ATLAS.md](CARRIER_ATLAS.md) §1. No open obstruction at this layer
beyond the honest access boundary (uncountable carriers have only a finite computable subclass of
points). Nothing here bears on RH.

**Proof Teeth branch extension:** PH-01–08 now prove the normalized cyclic Haar
direct-limit completion `L²(Zhat)≅ell²(Q/Z)`, its bounded-cone universal property,
strong convergence and the exact norm obstruction. PT-C01–05 implement minimum
observations with explicit collisions/descent gates. Paired YEAN commit `bf49477d`
kernel-checks 62 finite algebra theorems; analytic completion and Fourier transport
are still paper proofs. See [the scoped supplement](CLAIM_SUPPLEMENT_PROOF_TEETH.md).

## Track 2 — Source-faithful categorical / observer / proof systems

**Status: PROVED LOCAL / CLASSICAL.** The four-class field taxonomy (Simple / IdealHard / Fucked /
Unresolved), compact-gluing and its noncompact-escape no-go, profinite aliasing, no-ghost Farkas
gluing, and the ordinal (Goodstein/ε₀, supermartingale) termination firewall. Documented in
[OBSERVER_PROOF_ACCESS.md](OBSERVER_PROOF_ACCESS.md). Key discipline: ordinal/almost-sure
termination is proved **distinct** from, and never promoted to, a signed Weil sign.

## Track 3 — Effective finite-to-global and Simple/IdealHard/Fucked analysis

**Status: PROVED where marked; RH classification Unresolved.** Kleene-tree IdealHard witnesses,
noncompact FuckedField, phantom source-maps, and the inverse-limit trilemma (global compatible
existence vs computable witness vs observable identity). RH is explicitly left **Unresolved** — not
IdealHard, not Fucked — pending a theorem.

## Track 4 — Tate / Pontryagin / Fourier / Poisson completed harmonic interfaces

**Status: CLASSICAL / PAPER PROVED (imports), exact finite receipts.** Local self-dual Fourier on
Q_p, the rational adelic solenoid and its Pontryagin dual Q, the Schwartz–Bruhat **adelic Poisson
theorem** (proved two dependency-distinct ways), idelic Mellin → `Gamma_R(s)ζ(s)`, and the single
`Gamma_R(s)=π^{-s/2}Γ(s/2)` archimedean factor. Documented in [CARRIER_ATLAS.md](CARRIER_ATLAS.md) §2.

**PR #131's corrections are canonical here:**
- Integer rational-coset scales with rational translates **suffice** to span finite-adèle tests
  (`1_{u+(a/b)Ẑ}=Σ_{j=0}^{b-1} 1_{u+(a/b)j+aẐ}`). The earlier "noninteger scales are necessary"
  claim is **REFUTED** (CTW-02). Restricting *both* scales and translates to integers does fail.
- Overall scalar normalization is lost under logarithmic differentiation, so a finite coefficient
  check cannot authenticate supplied root-number metadata (CTW-11) — but this is **not** a universal
  root-number impossibility: full global logarithmic data with self-duality give
  `w=(-1)^{ord_{1/2}F}` via central-order parity.

These corrections mark it an **analytically classical reconstruction** with explicitly stated
classical dependencies (real Poisson, LCA duality, character orthogonality, Stone–Weierstrass).

## Track 5 — Genuine signed Weil and Suzuki arithmetic proof research (RH-critical)

**Status: scoped PROVED ANALYTIC results; global sign OPEN.** Source is the SHA-pinned PR85
completed-zeta Suzuki blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`: conductor 1, parity even,
half-density 1/2, root number 1, both completed poles and one real `Gamma_R` retained; genuine von
Mangoldt half-density weights `w_n = log(p)/√(p^k)` (so Λ(4)=log 2); fake composite 6 and non-Euler
mutants refused; **no nontrivial zero ordinate is a construction input**.

| Object | Statement | Scope / metric | Status |
|---|---|---|---|
| Γ_ℝ Fourier multiplier | m_J(ω)=Σ_{j<J}(4/(4j+1))·ω²/(ω²+((4j+1)/2)²) = ω-part of Re ψ(1/4+iω/2) | truncation ≤ true multiplier (omitted modes PSD) | CLASSICAL / PROVED |
| 4-moment coercivity | Q_ζ(f) > ‖f‖²/50 | a=1/2, p=2 only, moments 0..3 = 0 | PROVED ANALYTIC |
| 7-moment coercivity | Q_ζ(f) > ‖f‖²/16 | a=1/2, moments 0..6 = 0 | PROVED ANALYTIC |
| 16 / 18 / 30-moment | Q_ζ(f) > ‖f‖²/20 (16), > ‖f‖²/16 (18,30) | a=1/2, Ω=12, J=32, moment-null codim 16/18/30 | PROVED ANALYTIC |
| K-relative transport | D_r = Q_r G Q_r ⪰ κ Q_r K Q_r, K=V*V=(−Δ_N)^{-1} | mean-zero carrier; **relative to K, NOT κI** | PROVED ANALYTIC |
| Zero-shift residual | 0 ⪯ R0 ⪯ (11/40)²/κ · I via Douglas range | NO D^{-1}/K^{-1} at λ=0; ‖g'‖₁<11/40 interval-proved | PROVED ANALYTIC |
| All-radii existence | ∀ a>0, target L ∃ finite moment rank r: Q_ζ(f)>L‖f‖² on r-moment-null f | symbolic enormous r; effective existence only | PROVED ANALYTIC |
| Small-window all-f | W_ζ(f*f̃) ≥ ‖f‖²/100, ∀ f∈C_c^∞(−a,a) | a≤1/12 (NO prime active); classical Yoshida/Suzuki | PROVED ANALYTIC |
| Rank-4 completion | G+(65/16)P4 ⪰ 0 with positive Hilbert sqrt | finite-rank auxiliary; Morse index ≤ 4 | PROVED ANALYTIC |
| Tate→Weil obstruction | source A^N G is SIGNED, not a positive Gaussian mixture | scoped NO-GO on a positive-transport shortcut | PROVED (refutation) |

This is a **scoped research result requiring continuing hostile review**, not a step toward a proof:
the remaining source Schur sign is unresolved.

### The named open obstructions (the firewall)

**Proof Teeth branch refinement:** the full cross/resolvent parity reduction and
compressed-K quotient residual are derived, eight authentic trial-certificate
failures are certified, and the inherited scalar response cap sharpens to
`75625/20699`. The explicit corrected operator may use `4P4`; it remains a modified
operator. The genuine `Ainf−R0` sign is still OPEN. See
[the analytic dossier](../research/2026-10-15/FOUR_LOW_SCHUR_CROSSPOLLINATION.md).

1. **Low Schur sign.** For every window the finite low block `S0 = A − R0` (the all-test sign at
   that radius) is **UNVERIFIED**. "Every high sector positive ⇒ full Weil positive" is **REFUTED
   generally** by signed low-block countermodels.
2. **Low/high resolvent coupling.** The K low/high cross-channel has rank exactly 2 (not zero); the
   cross-resolvent range is used only for the finite zero-shift bound, never to certify a sign.
3. **λ↓0.** Handled via the Douglas range/factorization theorem; **no spectral gap D ⪰ cI** is
   introduced and no D^{-1} exists at λ=0.
4. **Source → Weil-sign identification.** A source-faithful positive Hilbert Gram factorization
   `K_g(x,y)=⟨Φ(x),Φ(y)⟩` surviving fake-composite / wrong-Γ / wrong-pole / conductor-parity /
   non-Euler controls is the **missing typed morphism**. Assuming `K_g ⪰ 0` merely restates RH.
5. **All-a uniformity.** Short-interval positivity (a≤1/12) is classical and unconditional;
   prime-active and all-a windows remain the hard, RH-equivalent problem.

**Reviewer watch (load-bearing assumptions).** Every certificate clears its floor by a thin,
outward-rounded exact-rational margin and depends on the pinned `C_∞ = −ψ(1/4)+log π < 43/8`
(actual ≈ 5.3719 vs 5.375). Examples: 7-moment gap 0.0658>0.0625; 4-moment 0.0214>0.02; small-window
0.01265>0.01. Validity rests on the SHA-pinned source constants and conservative outward rounding —
both present and checked, with essentially no numerical headroom.

## Track 6 — Physical / quantum / chaos / ordinal experimental mathematics

**Status: TESTED MODEL / exploratory.** The logistic-source quotients, Misiurewicz phase, chaos
source-debt, and the physical-carrier motivation. These are motivation and instruments, never
proof certificates; near-zero sampled eigenvalues are TESTED MODEL, never rational positivity
certificates, and physical ontology is never a prerequisite for the established mathematics.

---

## Why Poisson is closed and RH positivity is not

Tracks 1–4 are **classical theorems** (existence, duality, summation) realized exactly; their truth
does not depend on any sign. Track 5's hard object is a **signed** completed Weil form whose global
positivity is equivalent to RH. The consolidation proves scoped high-subspace / short-window
positivity and sharpens the obstruction, but the low Schur sign, the low/high coupling, the `λ↓0`
behavior, and the source→Weil typed morphism remain open. **RH remains OPEN.**

See [CARRIER_ATLAS.md](CARRIER_ATLAS.md), [OBSERVER_PROOF_ACCESS.md](OBSERVER_PROOF_ACCESS.md),
[SUCC_RESEARCH_DEPENDENCY_DAG.md](SUCC_RESEARCH_DEPENDENCY_DAG.md),
[CLAIM_LEDGER.md](CLAIM_LEDGER.md), and
[ACADEMIC_CARRIER_INTEGRATION_AUDIT_2026-10-15.md](ACADEMIC_CARRIER_INTEGRATION_AUDIT_2026-10-15.md).
