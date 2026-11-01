# Operation Main XVIII — architecture overview

**Research-status only.** This fixes the typing discipline for the signed-lag frontier and points to
where each layer is realized. It promotes no mathematical status and preserves the author's physical-
carrier and semantic intuition as distinct from model interpretation and classical theorems.

## 1. Continuity with Main XVII

Main XVIII keeps the Main XVII typing spine and adds a signed, time-correlated observable on top of
it. The spine is unchanged:

```
  ℕ/ℤ  →  finite Pascal/path carrier  →  embedded observer  →  analytic (Gamma/Pisot/adic) structure
        →  source-specific realization  →  selected trajectory  →  (open) selected global theorem
```

The authentic four-pole BBP source is one specialization inside a π-free carrier; hostile and
counterfactual sources live in the same carrier and are never identified with the authentic one.

## 2. The three clusters by type

### Cluster A — counterfactual carrier and localization (PR #426)
A **type-1/type-5 contrast instrument**: an exact 16-fold triangle Ward/refinement law and a Walsh
localization on the finite carrier, run against *counterfactual* π carriers and original zero-seed
controls, with a "nonnormality-radiation" diagnostic that *detects* departure from normality on
hostile seeds. The diagnostic is a detector on known-hostile inputs; it is not, and must not be read
as, a proof that the authentic orbit is normal. Its finite-to-global statements are **criteria /
conditional**, not π-normality proofs.

### Cluster B — joint 2-adic × 3-adic × Gamma/Pisot structure (PRs #427 → #430)
A **type-4 analytic-spine** cluster. It develops the joint ×2/×3 local Haar clock and selected
tripling (`#427`, with an explicit solenoid reconstruction **no-go**), the Pascal 2↔3 dynamical
conjugacy with its Haar information defect and a Pisot bridge (`#428`), a half-power horizon with
genuine 2-adic ramification, a 6-adic successor and a BBP pole budget (`#429`), and a three-place
Gamma difference resolvent with a sharp 3-adic pole-depth distribution and prime *exposure* (`#430`).

Typing guards carried here:
- **Circle vs solenoid** Pontryagin duality is kept correct; the solenoid no-go is a genuine
  reconstruction obstruction, not a disguised normality statement.
- **Bounded real Fourier observables** are kept distinct from **unbounded p-adic norms**; an unbounded
  p-adic quantity is never substituted for a bounded real observable to manufacture cancellation.
- **Prime exposure** (a pole/denominator becoming visible) is kept distinct from **prime survival**.

### Cluster C — carrier path measure, tomography, and the signed lag (PRs #431 → #435)
The **type-5 selected-trajectory** cluster, where the signed observable lives.
- `#431` carrier-relative path measure: Pascal interference and effective resistance on the carrier.
- `#432` edge-normality gate and an exact **73-point seed-phase tomography** detector — exact only at
  **nine time modes** under its stated frequency conditions, with explicit alias checks; not valid at
  arbitrary horizons.
- `#433` selected-seed superposition: the first sixteen balanced moment orders, finite-grid
  anti-aliasing, near-zero nonnormal shadows, and the **Wall's-theorem rational-seed erratum** (a
  rational changed seed preserves asymptotic normality status; the Main XVI "must fail" requirement is
  corrected additively, the frozen record untouched).
- `#434` signed-lag van der Corput reduction with a critical logarithmic lag window, plus the
  test-loader isolation fix for the shared `independent_oracle` module name.
- `#435` the signed lag "fireworks": a doubled logarithmic clock, a sharp hostile transport barrier,
  and exact `q = 3^a 5^b` conductor-shadow spectra.

## 3. The signed observable (type-5, selected)

The best current formulation of the attack is the authentic signed lag observable

```
  L_{N,K}(h) = (2 / (K N)) · Σ_{k=1}^{K-1} (1 − k/K) · Re Σ_{n=1}^{N-k} e^{2πi h (16^k − 1) U_n}
```

with `U_0 = 0`, `U_{n+1} = 16 U_n + r(n+1)`. PR #435 establishes a smaller source-transport error at
`K ∼ log_4 N` and proves a **gate equivalence** (the original and doubled-clock signed criteria are
necessary as well as sufficient within the BBP forcing family). A gate equivalence is a criterion, not
progress on its premise. The remaining open claim is the **selected zero-boundary signed asymptotic
estimate for every fixed nonzero integer harmonic `h`**, which is the signed Weyl gate and is
equivalent to π base-16 normality — **OPEN**.

## 4. Transfer rule (unchanged)

A statement about a type-1..4 structure (a Ward identity, a Haar/Pisot law, a tomographic readout, a
transport bound) does not by itself bound the type-5 selected signed sum. Positive physical or semantic
covariances are not automatically source-derived positive Weil forms; the identification is never
asserted silently. A barrier or a nonnormal counterexample family is a **negative** result that
constrains proof routes; it is not a normality proof and not its negation for the authentic orbit.

## 5. Hostile and counterfactual sources the carrier admits without identifying

Carried forward and extended from Main XVII: the irrational coherent counterseed `s* = −π/16`
(genuinely nonnormal, same four-pole forcing — the decisive required-failure holdout), the AT-07
seven-pole null, the SC-05 block-coherent seeds, horizon-dependent rational coherent seeds `s_K`
(finite-prefix spoofing, not a fixed asymptotic nonnormal rational orbit), the exact dyadic-rounding
near-zero irrational seeds, and the prime-smooth `q = 3^a 5^b` completed orbits with limiting signed
spectrum `1_{(q/15)|h}` (pass arbitrarily many low modes while remaining nonnormal). The architecture
must realize all of these inside the same carrier while keeping each distinct from the authentic
four-pole BBP source.
