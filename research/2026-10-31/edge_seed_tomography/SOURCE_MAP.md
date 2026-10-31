# Source / measurement / carrier adequacy map

**Types, not metaphors.** The distinctions below are required for lawful categorical transport. All equations are checked on their declared domains; no physical source or normality proof follows automatically.

| Layer | Object and operation | Concrete source map | What is lost | Authority |
|---|---|---|---|---|
| Original arithmetic | exact rational state `U_n(0)`, `U_0=0`, `r(n)` | `U_(n+1)=16U_n+r(n+1)` | nothing if all four poles, time index and initial seed retained | Exact rational original source |
| Real circle | `x_n=U_n mod 1` | quotient `Q/Z`; actual update `x_(n+1)=16x_n+r(n+1) mod 1` | unwrapped integers and denominators | Source map, but circle value alone not complete source |
| Path edge | `d_n=U_(n+1)-U_n` | `d_n=15U_n+r(n+1)` | static `×15` covering is 15-to-one | ESM-01/02: Haar **reflection** only after orbit-invariance closure |
| Dynamical weak limit | `μ=lim μ_(N_j)`, `T16_* μ=μ` | empirical telescoping + summable forcing | exact finite seed and realized journal not recoverable from limiting distribution | ESM-03, conditional on subsequential limit |
| Counterfactual seed | `U_n(s)=U_n(0)+16^n s` | change initial seed; not a realized event | nothing, but it is **not** a π-source observation | ESM-04/07 virtual response |
| Full seed intensity | `I_N(s)=|Σz_n e(h16^n s)|²` | full pair Gram `z_n conj(z_m)` | one global phase | Exact inverse-Fourier reconstruction ESM-04 |
| Averaged seed intensity | `∫I_N(s) ds=N` | discard off-diagonals | **all pair phases** | Gauge/positivity negative control |
| Prime sampling grid | `j/p` for a certified alias-free prime p | finite DFT, labels `h(16^n−16^m) mod p` | none of the N(N−1) pair phases, for this finite N/h | ESM-05/06 exact finite; **not** genuine p-adic place |
| Projective plane | translates of `D={16^n mod73:n=1..9}` | cyclic difference set / incidence lines | original source phase values unless separately attached | Exact finite combinatorics, not Spec Z |

## Genuinely commutative vs noncommutative squares

**Commutative dynamical cover:** On the *model* circle, `M15∘T16 = T16∘M15` exactly because `15·16=16·15`. It is not injective. Invariance is necessary for Haar reflection (ESM-02); plain diagram commutation is not sufficient.

**Source forcing defect:** `M15∘T_n` compared with `T_n∘M15` for the *affine original-source time step* `T_n(x)=16x+r(n+1)` differs by `14 r(n+1)`. This is a source-labelled affine-square displacement, not a holonomy around a declared closed physical path. The actual successor edge yields `U_(n+1)-U_n=15U_n+r(n+1)`. The signed error is bounded by ESM-01; one must retain it when making the model-square diagram about the actual orbit.

**Observation fibre failure:** `M15` sends 15 circle points to one. A static point law `1+cos(2πx)` is nonuniform but maps to Haar. Under `T16`-invariance the fibre loss does not prevent reflection **of this one target property**, because the only absolutely continuous invariant probability is Haar. This does not reconstruct all original source records, and it is not a general target-descent theorem for arbitrary properties.

**Seed-selection failure:** The genuine π orbit is precisely `s=0`, not the almost-everywhere `s` in ESM-07. The counterfactual `s*=-π/16` and rational `s_K=-c_K` defeat uniformizing-from-ensemble arguments. Any proposal that proves zero-seeded normality based solely on ESM-07 (or the 73-plane) has crossed the source-map boundary.

## Concrete reuse plan (without a parallel category)

Main SUCC uses `operational_yoneda_descent.ObservationPathCategory` and `yoneda.FiniteFunctor`; `prime_clock_yoneda` shows an authenticated arithmetic quotient. We do **not** implement or claim a second category in this research branch. The eventual adapter should use these existing interfaces and declare two separate certified maps: (a) actual finite source/edge readouts including the four poles and U0, and (b) virtual perturbation measurements with an explicit `counterfactual=True` provenance flag. Equating them without a source-preserving morphism is forbidden.

**Diagram pass/fail:** `M15 ∘ T16` commutes, `M15 ∘ T_n` differs from `T_n ∘ M15` by exactly `14 r(n+1)`, and a finite Fourier sampling map preserves the **full pair response** iff labels are distinct modulo p. **Failure receipt:** p=73 with h divisible by73 aliases every label, while p=17 with N=9 aliases many labels. The tool must fail closed on either. A projective design with no source phase data can measure neither the selected Weyl sum nor π normality.
