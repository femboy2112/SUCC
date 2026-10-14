# RH candidate handoff — all-place source and analytic model-model gluing

**Origin:** `femboy2112/SUCC`, research branch `research/source-interaction-adelic-analytic-gluing-2026-10-14`, rooted at pinned completed-Weil source commit `55307fec354be0c671562233ca744907cf716ca5`, PR #71. **RH PROVED: no.** This is a review candidate only; no changes to the separate RH repository.

## Mathematical object

Standard Schwartz–Bruhat source on `A_Q`: real Gaussian `f_∞(x)=e^{-πx²}`, finite place filters `f_p=1_{Z_p}`, normalized unit multiplicative Haar, and standard self-dual additive Fourier/Haar. The diagonal rational source is globally filtered to `Z` because `q∈Z_p for every p iff q∈Z`. This validates use of one actual theta lattice, not an arbitrary Gaussian fit. For Re(s)>1, local Mellin data multiply to `Γ_R(s)ζ(s)`; outside, the Poisson theta interaction uniquely provides

    ξ(s)=1/2 + s(s-1)/2 ∫_1∞ ψ(t)[t^{s/2-1}+t^{(1-s)/2-1}]dt,
    ψ(t)=sum_(n>=1)e^{-πn²t}.

The integral is absolutely convergent and entire after the polynomial normalization. Source theorem import: adelic Poisson/Jacobi identity. No list of zeta zeros is read or needed.

## Consequential new-to-project results (none is an RH proof)

1. For each FIXED finite set of primes P, its P-smooth theta has modular defect normalized by `2^h` tending to `−1` as `t=4^{-h}->0`, while the full source has defect exactly zero. A finite rational bound on the threshold is implemented. Finite-place and small-scale limits DO NOT commute; a physical finite model cannot inherit the full modular Poisson 2-cell for free.
2. Uniform exact rational bounds for missing theta modes, t-tail and 1st/2nd s-derivative over an **entire vertical real strip**. Only the theta integral J has a y-uniform bound; ξ derivatives have an additional |s|≤R gate. The finite `[1,T]` integral is also rigorously bracketed at the supported real values `s=1/2,-2,3`, via π/exp/root interval arithmetic and monotone Riemann sums. Those are true FINITE analytic certificates outside Euler convergence, not floating point extrapolations.
3. Exact classical source consequences: `ξ(s)>59/120` on real `[0,1]` (NOT the entire vertical critical strip); ζ real negative for 0<s<1; ζ(0)=-1/2; trivial negative even zeros simple; `ζ'(-2m)=(-1)^m (2m)!/[2(2π)^(2m)]ζ(2m+1)`.
4. Meromorphic continuation of original prime logarithmic current by `-ζ'/ζ=−ξ'/ξ+1/s+1/(s−1)+[digamma(s/2)−logπ]/2`; agrees with convergent `ΣΛ(n)n^{-s}` only for Re(s)>1, and poles require independent nonzero guard.
5. At real symmetry point `2ζ'(1/2)/ζ(1/2)=γ+π/2+3log2+logπ`, exactly the C_G contact constant in Suzuki's independently constructed source-Gamma operator. This is CLASSICAL functional equation content, not a new positivity theorem.

## Source mutants and falsification

- Finite P: modular defect limit -1.
- Finite p-adic probes: unseen denominator `1/ℓ` passes observed integrality but not full diagonal source.
- Even integer lattice at p=2: altered conductor and Fourier Haar factor; cannot claim unchanged theta self-duality.
- Composite `6` is valid as integer dilation but not as primitive prime Euler place.
- Functional-equation-only completion `ξ_fake=(1+10s(s−1))ξ` has spurious off-critical real zeros at `(1±sqrt(3/5))/2` while retaining reflection and endpoint constants; its Euler overlap differs at s=2.
- Correct theta tail bound plus uncertified arbitrary complex quadrature is NOT full numerical rigor; separate bounded-integral interval implementation remains the next engineering task.

## What RH would still require

This work constructs **the canonical analytic completed zeta** from one original arithmetic source, not a source-identified positive Weil quadratic form. Inherited PR #71 constructs its signed distribution. The next theorem must prove a domain-correct nonnegative form for the authentic completed Weil distribution on every admissible test, or Suzuki's authenticated compact-uniform global spectral limit with its correct normalization and boundary conditions. Neither source synchronization nor analytic continuation supplies the sign. Preserve fake-6, wrong Gamma, conductor, half-density, phase and a properly completed non-Euler Davenport–Heilbronn control in that proof program.

## Proofs, testing, authorship boundary

- Dossier: `research/2026-10-14/SOURCE_MODEL_ANALYTIC_GLUING.md`.
- Pure exact code: `observational_succ/source_model_interaction.py`, `source_model_interval_quadrature.py`.
- Tests: `tests/test_source_model_interaction.py`, `test_source_model_interval_quadrature.py`.
- Deterministic receipt: `scripts/source_model_interaction_probe.py` and frozen JSON in the same research folder.
- Independent 65-digit oracle: `scripts/source_model_analytic_oracle.py` and frozen numerical JSON; not an interval-accurate complex quadrature.
- Core mathematics is classical Euler/Tate/Jacobi/Mellin/Gamma. New-to-project exact finite source certification and obstruction packaging; independent scholarly novelty review absent.

No physical source was authenticated. Draft-only result; do not merge to main or forward to `femboy2112/FuckingRH` without explicit maintainer review.

## Additional source-independent character validation (SI-13–SI-16)

To test that the gluing framework is not simply hardcoding the ζ real-place Gamma factor, it was applied to the primitive odd Dirichlet character χ₄ of conductor 4. The ramified p=2 local factor and parity ε=1 require 

    Λ_χ₄(s)=(4/π)^((s+1)/2) Γ((s+1)/2) β(s).

Its actual signed theta 

    Θ_χ₄(t)=∑_(n∈Z)nχ₄(n)e^{-πn²t/4}

has the classical correct transport `Θ_χ₄(t)=t^-3/2 Θ_χ₄(1/t)` (finite Gauss sum `τ=2i`, root 1), yielding an entire reflection-symmetric completion through a convergent t≥1 integral without zero inputs. A signed-tail / derivative-tail certificate was derived in exact rational arithmetic; wrong parity cancels the input source exactly.

The previous SUCC PRIME-SPHERE sibling's auxiliary chiral Gamma kernel has `k_C(0)=4β(2)`. The χ₄ source FE independently implies `β'(-1)=2β(2)/π`; hence `k_C(0)=2π β'(-1)` exactly. This is a source-sensitive classical **cross-model consistency check**, not a derivation of RH or identification of the true Suzuki completed Weil form with the auxiliary chiral operator.

Artifacts: `observational_succ/source_character_interaction.py`, tests, exact character receipt/replay, optional independent 60-digit numerical oracle and frozen output. Total isolated exact tests: **54 passing** (42 earlier +12 primitive-character cases). No new Lean proof or full source checkout claimed.
