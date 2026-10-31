# Operation Main XVII — carrier architecture overview

**Research-status only.** This document fixes the *typing discipline* for the integrated frontier and
points to where each layer is realized. It promotes no mathematical status. The author's Harmonic /
Golden / Euler–Mascheroni triangle and Oily–Macaroni terminology, provenance and physical intuition
are preserved and kept distinct from model interpretation and classical theorems.

## 1. The organizing structure

```
  ℕ/ℤ  →  finite Pascal/path carrier  →  embedded observer & extrusion
        →  Gamma/harmonic/golden analytic structure  →  source-specific realization
        →  selected trajectory  →  (open) selected global theorem
```

The **universal carrier is defined without reference to π**. The authentic four-pole BBP source
appears only as one *specialization* inside it, alongside hostile control sources that the carrier
admits without identifying.

## 2. Strict mathematical typing (do not conflate)

| # | type | definition | principal realization in this integration |
|---|---|---|---|
| 1 | **Carrier proper** | finite arithmetic objects + permitted operations | `universal_nz_carrier` (#417): labeled Pascal/Bratteli paths give ℕ; signed completion gives ℤ; degree-2 polarization `ab = C(a+b,2)−C(a,2)−C(b,2)` recovers multiplication (π-free) |
| 2 | **Embedded observer** | finite subsystem with causal access, retained state, external history | `observer_carrier_model` (#414): "observer ≠ carrier"; factorization iff constant-on-fibres (MA-01/02); `count_out` (#406) counting quotient lossless only if η + branch metadata retained |
| 3 | **Internal model** | representation built by that observer | `probability_operations` (#412) Haar branch law; `three_channel_spatial_h3` (#402) H³ observer family; `fibonacci_epicycle_demon` (#397) prequential-KL clock — all *declared* models, not the carrier |
| 4 | **Source realization** | exact specialization of the carrier to one arithmetic source | `universal_n_carrier` (#416) `F_{b,r}(n,u)=(n+1, bu+r(n+1))`; BBP = `R(a)=4/a−2/(a+3)−1/(a+4)−1/(a+5)`, `V(a)=a⁴/((a+3)²(a+4)(a+5))`, `R=∂_a log V`; multiplicative carrier `B_0=1, B_{n+1}=B_n^{16} V(8n+1+u)`, `U_n(0)=∂_u log B_n|_{u=0}`; `v_2(B_n(0))=−(16ⁿ−1)/3` |
| 5 | **Selected trajectory** | the actual initial/boundary condition + signed realization | `U_0 = 0`; `U_n = 16 U_{n−1} + r(n)` = `16^{n−1}π − T_n`, `0 < T_n < (8n+1)^{-2}`; the **initial jet of `B_0(u)`** (not merely `B_0(0)=1`) is load-bearing — `B_0(u)=1+su` preserves every pointwise `V` value and prime valuation but changes the selected derivative trajectory |
| 6 | **Global truth claim** | what is legitimately provable about the selected trajectory | the signed Weyl gate `T_N(h)=o(N)` ⇔ π base-16 normality — **OPEN**. A model theorem transfers to the carrier *only* via a proved abstraction / factorization / simulation / comparison map |

**Transfer rule.** A statement about a type-3 internal model (or a positive type-4 source statistic)
does not, by itself, bound the type-5 selected signed sum. Positive physical/semantic covariances are
not automatically source-derived positive Weil forms; the identification is never asserted silently.

## 3. The analytic spine (type-4 structure)

- **Gamma / Poisson / Pascal actualization**: `universal_n_carrier` Gamma→negative-binomial; the
  golden fixed-point locus `q_{r,θ}=λ^r ⇔ θ=λ/(1−λ^r)` (Main XVI) with the BBP point at `(r,θ)=(2,1)`,
  Oily–Macaroni `Ω_OM = λ − γ = (1−γ) − λ²`.
- **Basel / line-circle**: `basel_line_circle` (#420) finite-cycle Green operator, `Tr G_N² =
  (N²−1)(N²+11)/720`, six-Gamma determinant, digamma, negative-ζ identities. Local intrinsic circle
  curvature is zero; global closure/winding is measurable; weighted Green response is source-sensitive
  but **seed-blind**; a scalar phase gradient has trivial holonomy; an independently chosen magnetic
  flux is **not** an authenticated BBP interaction. The all-order `N^{-2k}Tr(G^k) → 2ζ(2k)/(2π)^{2k}`
  is PROVED for k=1 / unweighted and **CONJECTURED** for weighted k≥2.
- **Analytic continuation & prime arithmetic**: `dyadic_zeta_prime_exposure` (#422) keeps finite
  divergent sums, analytic continuation, regulator-dependent finite parts, real-convergent Euler
  products, p-adic limits, prime *exposure* vs prime *survival* strictly separate; the complete
  negative-odd-ζ denominator is the classical von Staudt–Clausen law.
- **Prime-frame representation** (type-5 probe): `carrier_first` (#424) ST3/ST4
  `A_n = Σ_p β_{p,n} log p`, `|U_n(0) − A_n| ≤ 1/(120 n³)`, signed coefficients, chronological
  weights `16^{n−k}`, CRT complement; a transport bound (`carrier_adelic_transport` #421 CAT-05) is an
  *equivalent cancellation criterion, not a saving*.

## 4. Pisot / Fibonacci / connection geometry (auxiliary, type-3)

`pisot_ramification` (#418): positive combinatorial decompositions, Pisot-unit coordinate changes,
number-field ramification (disc = −3·5·17). `pisot_lagrangian_geometry` (#419): a sixfold lattice
holonomy — but pure multiplication inside one commutative number field commutes, so the nontrivial
holonomy depends on an **additional, hand-chosen cross-field identification** (an explicit Z-module
pairing φ↔√3). It is a *declared gluing witness*, **not** native physical spacetime curvature, and
the order-6 property is not invariant under the choice.

## 5. Hostile sources the carrier admits without identifying

See the countermodel ledger (`MAIN_XVII_CLAIM_REGISTRY.md` §2): `s*=−π/16`, the AT-07 seven-pole
null, SC-05 block-coherent seeds, the `Q_mut`/J-involution source mutants, the #421/#424 entire-
remainder and Gaussian rational-boundary shadows, and the Stoneham c=2 / de Bruijn / Kempner /
Champernowne / biased-Bernoulli controls. The architecture is required to realize all of these inside
the same carrier while keeping them *distinct* from the authentic four-pole BBP source.
