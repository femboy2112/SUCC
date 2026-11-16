# Boundary-first reconstruction: filters, twists, and the observable quotient

**2026-11-12; Main XXV base db9fb4b84672050efa79b13377f1e73364598a14.** Research branch only. The authentic four-pole BBP source, literal U_0=0, provenance manifest and archived theorem contracts are unchanged. **R0, base-16 normality of π, Goldbach, completed Weil positivity and RH remain OPEN.**

## The proposed holographic direction

Instead of guessing an interior model and projecting it outward, prescribe a **boundary response functor** and determine what is logically reconstructible from its spectral/temporal filters. The phrase "radiates outward" means an explicitly defined transfer/observation law, **not** physical radiation or a claim of instantaneous access to an infinite boundary.

A finite-dimensional rational linear realization has internal state x_(n+1)=Ax_n, source/initial vector b=x_0, and boundary readout y_n=Cx_n. Declare every A,b,C, observation port and admissible mask. The boundary sequence is y_n=CA^n b. A family of masks D_h changes the boundary instrument to C D_h, giving y_(n,h)=C D_h A^n b. These are new *physical/semantic instruments* unless derived from the original accessible boundary; cannot add them free of charge.

### Theorem BF-01: Hankel boundary rank is the minimal observable-reachable order

For n-dimensional A and scalar C, let H_d(i,j)=CA^(i+j)b for 0<=i,j<d. Set O_d=[C;CA;...;CA^(d-1)] and R_d=[b,Ab,...,A^(d-1)b]. Then **H_d=O_d R_d**, exactly, by associativity. For d>=n, its rank is the dimension of the reachable space modulo the subspace of reachable states whose future boundary readouts all vanish. This is the classical minimal SISO realization order. Cayley-Hamilton implies all later responses are determined by a finite linear recurrence once a minimal realization is known. This does **not** reconstruct the original unobservable bulk.

**Proof of quotient:** R=span{A^j b} stabilizes by n-1; N={v in R: CA^k v=0 for every k>=0} stabilizes by n-1 using Cayley-Hamilton. N is A-invariant. The induced observable pair on R/N is reachable and observable; the corresponding finite Hankel rank equals dim(R/N). An independent hidden block changes the interior without changing *any* boundary moment.

**Hostile example:** A=diag(2,3,7), b=(1,1,0)^T, C=(1,1,0). All boundary moments are 2^n+3^n. Replace hidden eigenvalue 7 by 17: every moment and every finite or infinite scalar boundary filter on that original port agrees. The internal matrices differ. Thus complete boundary observation recovers only an equivalence class unless observability, source geometry or additional ports rule out hidden sectors.

### Theorem BF-02: a separating filter bank recovers a present state

For diagonal masks D_h=diag(f_h(1),...,f_h(n)), let B_h=C D_h. The instantaneous response is y_h=B_h x. Assemble the rational matrix B with rows B_h. Then x is uniquely reconstructible from all y_h **iff rank(B)=n**. If rank<n, any nonzero kernel vector is a genuinely invisible interior perturbation. The exact solver refuses rank-deficient and inconsistent measurements. The theorem is elementary linear algebra but its *operational* implication matters: a spectral filter only adds information if its boundary implementation and source map are justified.

Example: C=(1,2), masks (1,1) and (1,-1) yield y=(11,-5) for x=(3,4); the inverse is unique. But two proportional masks do not add information, and if C_j=0 every diagonal mask remains blind to coordinate j. Thus "more filters" is not equivalent to "complete filters."

**Nontrivial extension challenge:** Replace freely chosen diagonal masks by the **actual SUCC carrier's** prime-power/Γ phase, signed real carry and original zero-seed probes. Prove a uniform separating estimate or a nullspace obstruction in a stated completion. No such source-derived rank/coercivity theorem is supplied here.

### Theorem BF-03: signed future-conditioned spectral lines are exactly the missing digit defect

This is a **recovery/reuse of RHY-10**, not a novel claim. Let p(a,w) be the first-digit/future-word joint law and ζ=e(1/16). For h=1,...,15 set G_h(w)=Σ_a ζ^(ha)p(a,w). The inverse discrete Fourier transform gives

p(a,w)-p(w)/16 = (1/16) Σ_(h=1)^15 ζ^(-ha) G_h(w).

Thus the 15 signed spectral lines for **each future word w** recover every conditional defect. Averaging over future words before filtering destroys the very correlations we need. The exact new adapter retains finite rational exponent/weight dictionaries rather than floating complex values; it tests the same failure on a balanced alternating binary stream, whose one-digit marginal is uniform while the future-conditioned filter detects perfect predictability.

**Finite-window caveat:** The adapter uses noncyclic length-(depth+1) windows, whereas RHY-10 uses cyclic empirical counts; the DFT identity holds for either if one uses its own consistent normalization. Boundary endpoints cost O(depth/N), not zero. Do not claim the two conventions coincide.

### Theorem BF-04: source authentication is a separate, non-spectral port

Use the immutable original r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2) and U_n=16U_(n-1)+r(n). Exact finite unwrapped recurrence and U_0=0 are checked independently of the boundary rank. Same forcing with s=1/16 has valid transitions but the wrong pin. The coherent wrong seed s=-π/16 has the same forcing and a completed nonnormal orbit. All closed, source-corrected temporal holonomies remain seed-blind by APH-01. Therefore a filter theorem for generic rational matrices or conditional digit laws cannot imply π normality without a new source-selected signed estimate.

## Two genuinely different obstructions

1. **Pathway/observability gap (σ):** an internal sector lies in the kernel of all currently allowed boundary maps. No amount of repeating those filters can reveal it. Add a genuinely independent source-calibrated port or restrict the interior category.
2. **Quantitative/probe gap (μ):** a boundary filter is injective in principle, but no uniform bound controls inverse amplification or the signed all-epoch source response. A finite invertible matrix is not a dimension-independent stability theorem. This is where a true arithmetic estimate must enter.

## A source-locked proposed proof campaign

**π route:** authenticate U_0=0, preserve the true completed tail and carry, build the conditional spectral filters G_h(w) using the **actual** π orbit, and seek a source-derived upper bound on Σ_w Σ_(h≠0)|G_h(w)| or on the exact conditional Haar defect. Require a rate uniform over the prescribed growing observation depth J(A). Reject rational aliases, coherent counterseeds, periodic fake normality, independent prime marginals and fake forcing. The needed signed estimate is OPEN.

**RH route:** reuse the completed prime–Archimedean Weil form with genuine Λ(p^k), half-density p^(-k/2), Γ/pole/contact, test-function domain and correct sign. Investigate boundary response Hankel or Schur complements **without** identifying a generic positive Gram with the signed Weil form. A real positive source identification and an all-test inequality are missing. Test fake-6, wrong Γ, wrong half-density and finite-moment matched counterfeits. RH remains OPEN.

**Goldbach route:** take a boundary pair response at a prescribed even target E and keep its prime-label source. A complete two-point Fourier response may reconstruct the finite additive convolution, but positivity of a reconstructed scalar is not automatic. A uniform all-even nonempty-fiber bound remains OPEN.

## Relation to existing SUCC

- Existing exact finite Jacobi inverse boundary theorem: observational_succ/spectral_boundary_rigidity.py. It reconstructs a **restricted positive chain**, not every bulk.
- Fourier Yoneda pinbed: observational_succ/fourier_yoneda_pinbed.py; existing empirical law and boundary response tools.
- Recursive Haar: research/2026-11-09/recursive_haar_pinbed/THEOREMS.md (RHY-01/02/10).
- Authenticated source and actual frontier: docs/PI_NORMALITY_FRONTIER.md, docs/PI_FRONTIER_CONTRACT.md.
- Seed-blind closed paths: research/2026-11-07/pinbed_yoneda_oscillators/ANCHORED_PATHS_VS_HOLONOMY.md.
- Twin rendezvous and relational Bell boundary: draft PR #604. The present model is **classical rational linear dynamics**, not ER=EPR or a bulk spacetime geometry.

## Validation / authority

Implementation: observational_succ/boundary_filter_tomography.py and tests/test_boundary_filter_tomography.py. The derivations above prove universal finite-linear statements; no Lean formalization or external peer review. At the time of authoring, focused code had not been executed in a full checkout; the new branch must pass the four AGENTS.md commands and hosted checks before integration. No test count or CI success is claimed without actual tool receipts.
