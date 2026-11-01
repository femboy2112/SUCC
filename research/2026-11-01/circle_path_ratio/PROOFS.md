# Unit-SUCC circumference/diameter path quotient: an exact geometric seam and an authenticated BBP bracket

**Status: classical geometry and probability + source-specialized paper derivations + 44 focused exact regression tests. Not a Lean/kernel proof; not a proof of base-16 normality of π or RH.** This dossier uses the original SUCC four signed BBP poles, literal zero initial condition and the actual radix-16 orbit. No geometric/quantum operation is invented as intrinsic to that deterministic source without declaring its domain.

## G1 — two *different* paths with the SAME endpoints produce π as a length quotient

Let C be the unit circle `x²+y²=1`, A=(1,0), B=(-1,0). Compare (a) the upper semicircle traversed from A to B in its induced Euclidean metric, with (b) the straight diameter A→B in R². The latter has length 2. In the rational projective parameter `t∈[0,∞]` put

    Γ(t)=((1−t²)/(1+t²), 2t/(1+t²)).

Direct differentiation proves `||Γ'(t)||=2/(1+t²)`; thus `L_arc=2∫_0^∞ dt/(1+t²)=π`, and the dimensionless **same-endpoint path quotient** is

    Π_geom = 2 L_arc / L_diameter = 2∫_0^∞ dt/(1+t²) = π.

The equality with the standard analytic π is classical (`arctan ∞=π/2`). π has NOT been inserted as a numerical input in the algebraic circle equation or the chord-refinement algorithm. The result is a geometrically exact representation of known π, not a new independence/irrationality/normality proof. The arc and diameter live on DIFFERENT path constraints, so an interferometer coupling the two is an extra control experiment.

The angular/arc-length one-form on the projective coordinate is `η=2dt/(1+t²)`. On its complexification it is meromorphic with poles `t=±i`; its real period gives one circle traversal. This source-neutral circle differential has **two punctures**, distinct from the authentic BBP's FOUR rational source poles `(7/8,1/2,3/8,1/4)` on a separate projective coordinate (PR #442). An identification of those two punctured spheres/complex connections requires an extra declared source map. Also, a circle's *extrinsic* curvature is 1/R and its *intrinsic* 1D Riemann curvature is zero; this angular one-form is not the Zak two-form curvature in PR #438.

## G2 — the unit successor constructs the curved path recursively, without knowing π

Bisect each upper unit-circle arc through its radial midpoint. At stage k the upper semicircle is approximated by `n_k=2^k` equal chords of length `c_k`; start `c_0=2` (just the straight diameter). The Pythagorean/half-chord identity is exactly

    c_(k+1)² = 2−2 sqrt(1−c_k²/4)
             = c_k²/[2(1+sqrt(1−c_k²/4))].

The second, rationalized form avoids cancellation near the limit. Define the full circle-to-diameter quotient represented by that finite curved polyline as

    Π_k = 2 L_polyline / L_diameter = 2^k c_k.

This is a **purely algebraic nested-radical recursion** requiring successor, multiplication and positive square-root selection. Pure integer addition does NOT generate √2; the required carrier extends through nested real algebraic fields and an ordered real completion. Its branch convention (positive roots, upper semicircle, forward orientation) is part of the observer's history.

Standard inscribed/circumscribed path comparison proves, for all k>=1,

    Π_k < π < Π_k/sqrt(1−c_k²/4).

π is literally the common limit. Using `c_k=2sin(π/(2*2^k))` *only in the proof of the error*, and `0<x−sin x<x³/6`, with `π<4` from a circumscribed square, yields

    0<π−Π_k<8/(3*4^k).

The iteration is self-referential as a path *construction*: each stage is the next admissible refinement of the same circle with a fixed diameter normalization. It is NOT a fixed scalar π satisfying a nontrivial polynomial equation. Viète's infinite nested square-root product follows by multiplying the successive ratios Π_k/Π_(k−1), with Π_0=2; it is classical.

## G3 — circle angle ×2 is a rational map on the projective line, ×16 is four copies

Let `C(t)=(1+i t)/(1−i t)` be the Cayley uniformization of the real projective circle. Define the projective rational doubling map

    D₂(t)=2t/(1−t²),

with its denominator-zero points handled homogeneously, NOT deleted. Exact algebra gives

    C(D₂(t))=C(t)²,
    (D₂)^*η=2η,
    C(D₂∘D₂∘D₂∘D₂(t))=C(t)^16,
    (D₂^∘4)^*η=16η.

Thus **four inverse refinements of the geometric circle correspond to one radix-16 coarsening**. In homogeneous coordinates t=a/b, the true update is

    [a:b] -> [2ab : b²−a²].

No artificial truncation of the t=∞ state is lawful. An independent complex-binomial oracle uses the real and imaginary parts of `(b+ia)^16`; its outputs exactly equal the fourfold homogeneous recurrence.

Real circle rotations by angle 2πr also become projective Möbius transformations:

    R_τ(t)=(t+τ)/(1−τt),  τ=tan(πr),
    R_τ^*η=η.

Therefore the **literal original** `U_(n+1)=16U_n+r(n+1)` becomes a typed nonautonomous projective circle path

    t_(n+1) = R_(τ_(n+1)) ◦ D₂^∘4 (t_n),
    t_0=0,

where `t_n=tan(πU_n)` is interpreted projectively and `τ_n=tan(πr(n))` is algebraic: its complex Cayley rotation is the root of unity `exp(2πi r(n))`, since r(n) is rational. The exact source boundary `U0=0` is retained. Circle rotations are isometries for η, so the full time-indexed map's pullback multiplies η by 16. That expansion is source-blind; the source resides in the ordered R_τ labels and the seed. The actual circle phase `exp(2πihU_n)` remains the proof target.

**Sphere/gluing no-go.** If one tries to analytically interpolate all time-indexed rotations by `z↦exp(2πi r(z))z` on the compact source Riemann sphere, the multiplier has an essential singularity at EACH actual pole of the nonconstant rational r(z). Therefore it does NOT extend as a globally meromorphic/rational one-parameter map on that compact sphere. The correct object is a punctured-base analytic cocycle, or the exact discrete, cyclotomic source-labelled maps. A single unpunctured rational source×circle map would be false without an explicit different construction.

## G4 — two rigorously defined path-space kernels can read the SAME ratio

Construct a declared 2-channel metric graph with the same endpoints A,B: a straight edge of length `2R`, and a designated upper semicircular edge (or its finite kth polyline approximation) of length `R Π_k`. Diffusion on each arclength line channel is a separately typed **Wick/heat** path integral; the standard free generator is `Δ`. For any t>0, its exact one-dimensional kernel at separation ℓ is

    H_t(ℓ)=(4πt)^(-1/2) exp(−ℓ²/(4t)).

The nontrivial path integral over intermediate positions is legitimate: convolution of m Gaussian steps yields exactly H_t for every m. Define its normalized log action

    A_t(ℓ) = −log(H_t(ℓ)/H_t(0)) = ℓ²/(4t).

The prefactor `sqrt(4πt)` CANCELS. So for the two routes,

    2 sqrt(A_t(R Π_k)/A_t(2R)) = Π_k.

The quotient is exact for EVERY t>0 and k, not only in a small-time limit. Taking k→∞ yields the geometric π. This construction has a genuine sum/integral over stochastic paths, but the line channels and their coupling were DECLARED. It is NOT a physical tunneling-through-a-barrier mechanism, nor an intrinsic BBP quantum probability measure.

On the complete circle instead of one designated upper arc, the heat kernel includes two equal short antipodal arcs and all windings. Varadhan's short-time log asymptotic still extracts their common shortest arc distance; the multiplicity contributes only a lower-order log factor. This is an independently established classical heat-kernel distance principle. The real-time Fresnel/Feynman kernel instead contains `exp(iℓ²/(4t))`, whose single phase is only known modulo 2π. Recovering an unwrapped ℓ from one complex phase is UNDEFINED without time variation, branch tracking or Wick continuation. SUCC PR #444's rigorous Feynman model does not itself make the two metric-channel lengths an original BBP source operation.

## G5 — a source-authenticated BBP/Wilson bracket contains the geometric path quotient

**Unchanged source** from SUCC Main XVIII and PR #446:

    r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2),
    U0=0, U_(n+1)=16 U_n+r(n+1).

Its known completed identity is

    π = 16∑_(j>=1)16^(−j) r(j).

Define the exact rational truncation and true source order defect

    B_N = 16∑_(j<=N)16^(−j)r(j),
    d_j = 15(r(j)−r(j+1))>0.

From PR #446 the Wilson-curvature upper approximation is

    W_N = (16/225)(47−∑_(j<=N)16^(−j)d_j).

An INDEPENDENT finite summation-by-parts derivation proves the crucial new simplification

    W_N = B_N + (16/(15*16^N)) r(N+1).

Since r(j)>0 is strictly decreasing, we obtain the strict source bracket B_N<π<W_N. In particular the Wilson upper bound is a **corrected source truncation**, not an independent third measurement from a separate source family.

The positive source density `(1−t)(t²+2)(t²+2t+2)` lies between `4(1−t)` and `15(1−t)` for t∈[0,1], so

    r(N+1) >= 4/[(8N+1)(8N+2)],
    r(N+1) < 15/(64N²).

Consequently

    π−B_N > 4/[16^N(8N+1)(8N+2)],
    π−B_N < 1/[4N²16^N].

For the geometry choose **k=4N subdivisions**: this is exactly 16^N line segments, matching the arithmetic radix resolution. Its known geometric error is

    0<π−Π_(4N)<8/(3*256^N).

For EVERY N>=2, the elementary inequality

    3*16^N > 2(8N+1)(8N+2)

implies `π−B_N > π−Π_(4N)` and hence B_N<Π_(4N). At N=2 this reduces to 768>612, and the ratio of successive exponential factors exceeds that of the quadratic denominator; induction establishes every N>=2. N=1 is separately certified by outward exact radical intervals: Π_4>392/125=3.136>47/15=B_1. Therefore for EVERY N>=1:

    **B_N < Π_(4N) < π < W_N.**             (G5)

This is a REAL all-horizon finite bracket stitching **an independent geometric path recursion** between two authentic rational BBP source approximations. In particular

    0<Π_(4N)−B_N<1/(4N²16^N),
    0<W_N−Π_(4N)<(16/(15*16^N))r(N+1).

The remaining common constant is π because both routes independently use the standard already-known circle/BBP identities. This bracket is NOT an independent derivation of the BBP formula from the circle refinement. It proves a source-coupled finite comparison, not equality of each refinement step.

**Rate mismatch (decisive boundary):** `π−Π_(4N)∼(π³/24)256^(−N)`, while `π−B_N∼(1/4)16^(−N)N^(−2)`. The geometric refinement step corrections are `Θ(256^(−N))`, while actual BBP increments are `Θ(16^(−N)N^(−2))`. Their ratio tends to ZERO exponentially. Thus there is NO termwise bounded-above/below scalar gauge identifying every 16-fold geometric refinement increment with one BBP source increment. The two histories converge to the same *limit* but cannot be declared the same local dynamics without a nontrivial source-dependent transport.

## G6 — finite field/clock triangulation: the geometric and BBP phase channels differ

The kth inscribed chord is in a real subfield of a 2-power cyclotomic extension because it is built from half-angle radicals / 2-power roots of unity. On the other hand the combined authentic BBP source is

    r(n)=(120n²−89n+16)/[(2n−1)(4n−1)(8n−7)(8n−3)].

Every denominator is ODD at integer n. Hence each zero-seeded exact U_n is rational with ODD denominator, and its finite complex circle character is an odd-order root of unity.

Let Q_N be the least common denominator of U_1,..,U_N (odd). At geometric level k, the natural half-angle root has order `2^(k+2)`. Since gcd(Q_N,2^(k+2))=1, the Chinese remainder theorem gives the **exact finite common carrier**

    Z/(2^(k+2) Q_N) ≅ Z/2^(k+2) × Z/Q_N.

The 2-primary geometric branch and odd-primary arithmetic BBP phase are independently representable inside this common root-of-unity register. It pays a growing conductor cost; the common carrier does not enforce signed cancellation, and the geometric line-length radicand is not being mislabeled as a primitive state of the discrete register. The corresponding cyclotomic field towers are coprime-conductor families, and their finite compositum is supported in Q(ζ_(2^(k+2)Q_N)).

## G7 — no false digit-normality inference

The universal circle ratio and the projective ×16 semiconjugacy are CLASSICAL and hold independently of BBP's special source. In the ORIGINAL SAME forcing, an altered seed s=1/5−π/16 yields the coherent nonnormal completed circle point q=1/5, even though the circle/diameter path ratio remains the same π and the ×16 angular form scales identically. Therefore:

- The geometric ratio π is not by itself an all-horizon signed Weyl estimate.
- The projective/heat/curvature carrier is not source-selected unless the four actual poles, U0=0 and the actual real-circle characters enter the statement.
- A BBP-source-to-rational-circle map is exact at integer times; it does not imply ergodicity of the actual selected orbit.
- The remaining verdict-changing target is a **source-attested signed** estimate `Σ_(n<=N)e(hU_n)=o(N)` for each fixed nonzero integer h, or an equivalent Main XVIII critical Fejér signed-lag upper bound.

This is a new, sharply testable carrier construction, not a proof of π normality or RH.

## Provenance and bibliography

- Classical circle rational parametrization: Norman Wildberger, UNSW mathematics geometry curriculum, https://www.maths.unsw.edu.au/sites/default/files/mathcurriculumgeometry.pdf
- Viète path refinement / infinite products: Moreno & García-Caballero, *On Viète-like formulas*, Journal of Approximation Theory 174 (2013), https://www.sciencedirect.com/science/article/pii/S0021904513001159 ; Imperial College *History of Mathematics* worked derivation https://www.ma.imperial.ac.uk/~bin06/HoM/HoM17/m3hsoln6.pdf
- Classical circle heat kernel/Varadhan: *The Heat Kernel on a Circle* https://mc.sbm.org.br/wp-content/uploads/sites/9/sites/2023/12/57-Article-3.pdf and https://www.cs.cmu.edu/~kmcrane/Projects/HeatMethod/paper.pdf
- Existing SUCC PR #438 Zak time-frequency torus constant connection, #440 source Hausdorff Newton–Gamma, #442 original source punctured sphere, #444 rigorous Feynman, #445 quantum phase echo, #446 exact Wilson order-curvature.
- The exact source-to-π BBP identity and all source-boundary normality obligations are PREEXISTING. The new finite bracket and explicitly unified projective/heat carrier construction are scoped specializations, not claimed external academic priority.
