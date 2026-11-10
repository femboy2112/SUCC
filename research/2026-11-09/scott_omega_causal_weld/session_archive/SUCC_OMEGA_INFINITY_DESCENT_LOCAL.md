# SUCC Omega–Lambda: finite gluing defects, completion, and the Archimedean circle

**Local research note, 2026-11-09/10. READ-ONLY GitHub policy.** Companion to `SUCC_OMEGA_LAMBDA_DIMENSIONAL_CALCULUS_LOCAL.md`. This note was prepared solely in the local container; no repository files, branches, PRs or commits changed. The authentic BBP source is as recorded in SUCC Main XXI `docs/PI_NORMALITY_FRONTIER.md`. Its published arithmetic facts are cited as inherited, not claimed novel.

**Scope and labels:** The fiber-product/gluing calculations, rational BBP identities, and finite error bounds below are elementary **DERIVED** mathematics. Standalone exact probes were **OBSERVED** passing with `python succ_omega_gluing_probe.py`. The interpretation as a genuine C-monoid faithful SUCC calculus is **CONJECTURED/UNVERIFIED**, not proved. Base-16 normality of pi, and RH, remain **OPEN**.

## A. Dimensional bookkeeping for omega-indexed semantics

`omega_k := λx. x x ... x` (k copies); `Omega_k := omega_k omega_k`. In leftmost syntactic reduction, the omega_k copy count grows by k−2 per contraction. This is an arity/copy-growth *grading*, not intrinsic geometrical dimension, typing, or a terminating computation. All `Omega_k` (k≥2) are head-unsolvable; treating their Scott denotation as bottom erases this growth information. Attach explicitly indexed, instrumented **trace semantics** before constructing geometries.

Under the proposed, *not yet implemented* compiled meaning `Omega_{d+2}^{SUCC} ↦ d independent SUCC coordinates`, three descriptions of a 3D coordinate carrier are available:

- `3 Omega_3`: `X×Y×Z` (three independent one-dimensional indices);
- `Omega_3 + Omega_4`: `X×(Y×Z)` (one axis and one curried/indexed sheet);
- `2 Omega_4 with one shared Omega_3`: `(X×Y)×_Y(Y×Z) ≅ X×Y×Z` via the **fiber product**.

**Counterexample:** two independent copies `(X×Y)×(U×V)` have *four*, not three, independently accessible coordinates. Ordinary union of two embedded planes in R³ is not a volume. The fiber product reconstructs coordinate triples from mutually compatible *pairs of projections*. This difference matters for causal interpretation.

### A.1. A quantitative approximate pullback

With real shared coordinate y and two finite computations returning `y` and `y'` with `|y−y'|≤ε`, the midpoint y*=(y+y')/2 yields compatible coordinates changed by at most ε/2 in sup metric. The bound is sharp (take y'−y=ε). For ε_k=16^{-k}, finite-resolution gluing defect is bounded by `1/(2*16^k)`, provided the comparison chart and same-coordinate identification are specified.

If source/carry/phase traces differ, equality of geometric coordinate triples is NOT automatically equality of computations. Need source-labelled higher cells or a compatibility cocycle.

## B. What “simultaneously finished at infinity” can legitimately mean

### B.1. Metric-completion criterion

Let X be complete and `a_n,b_m∈X` be Cauchy approximations with limits `a,b`. Define `D_{n,m}=d(a_n,b_m)`. Then `a=b` iff `D_{n,m}→0` along the product-directed limit `(n,m)→(∞,∞)`.

For explicit finite certificates, if `d(a_n,a_{n+1})≤α_n`, `d(b_n,b_{n+1})≤β_n` with summable tails, then:

`d(a,b) ≤ d(a_N,b_M)+ sum_{j≥N}α_j + sum_{j≥M}β_j`.

This is a **paid finite-resolution equivalence certificate**. Both algorithms can be nonterminating; their finite approximations are checked now. The limit is a mathematical object, **not an actual terminal SUCC event**.

### B.2. Scott-domain compact-probe criterion

In an algebraic pointed omega-cpo D, suppose `a_n` and `b_n` are increasing chains with `sup a_n=sup b_n=x`. For any compact element `k≤x`, compactness implies `k≤a_N` and `k≤b_M` for some N,M. Hence *every finite compact observable piece of x is eventually recovered on both routes*. If the domain is algebraic, agreement on all compacts characterizes equality of suprema.

**Crucial control:** In conventional Scott D-infinity semantics, head-unsolvable raw generalized Omegas collapse to `bottom`; their equality there preserves **no nontrivial omega-indexed trace data**. The proposed calculus needs a richer observation functor/operational trace model before semantic comparison.

### B.3. The two limits need not commute

Set `d(N,k)=1 if N≥k else 0`. Then

`lim_{N→∞} lim_{k→∞} d(N,k) = 0`, whereas

`lim_{k→∞} lim_{N→∞} d(N,k) = 1`.

Thus **precision k→∞** and **sample/trajectory length N→∞** must not be exchanged without a uniform-in-N estimate. More precise probes cannot by themselves prove an asymptotic cancellation theorem.

## C. The exact line–circle gluing is a quotient with a retained winding cocycle

The Archimedean circle is `T=R/Z`, with quotient `q:R→T`, `q(x)=[x]`. For hexadecimal dynamics, define `T_16([x])=[16x]` and `\tilde T_16(x)=16x`. Then

`q ∘ \tilde T_16 = T_16 ∘ q` **exactly**.

Integer deck shifts do not disappear: `\tilde T_16(x+n)=\tilde T_16(x)+16n`. If a representative x∈[0,1) is chosen at each stage, the integer carry is `c(x)=floor(16x)`, and `T_16(x)=16x−c(x)`. The carrier's circle position is the quotient, while the carry is essential **path-lift information**.

A loop `x(t)=t` for t∈[0,1] closes on the circle (`q(x(0))=q(x(1))`) but its real lift has endpoint defect `x(1)−x(0)=1`. Refining the mesh cannot make this integer winding vanish. It is a topological, rather than finite numerical, defect.

Local real angle charts can be glued to a circle-valued object, but their integer transition functions constitute a Cech cocycle. The identity map on S¹ has winding one; it has no continuous global real-valued angle lift. This is the **critical distinction** between a global quotient and a global equivalence of line and circle. The line is not homeomorphic to the circle.

### C.1. Finite cyclic approximants, and the critical direction-of-limit warning

Set `C_k={exp(2πij/16^k):0≤j<16^k}⊂S¹`. These finite cyclic groups are nested as subsets; their union is dense in S¹. **Metric completion** under the ordinary circle metric gives S¹. Fixed nonzero Fourier modes of uniform C_k vanish exactly once `16^k` does not divide h.

In contrast, the **inverse limit** `lim← Z/(16^k)Z` under residue reductions is the profinite ring `Z_16` (equivalently the 2-adic integers as a topological ring); it is totally disconnected and NOT S¹. Conflating this inverse limit with the Archimedean completion is a categorical category error. To compare them, use a declared digit-expansion map plus endpoint identifications, or a common character-theoretic interface, not an invented canonical isomorphism.

Given a real phase x and its k-digit truncation x_k=floor(16^k x)/16^k,

`d_T([x],[x_k]) ≤ 16^{-k}` and `|e^{2πihx}−e^{2πihx_k}| ≤ 2π|h|16^{-k}`.

This estimate is **uniform in the number of samples** if applied pointwise and averaged. Nevertheless it only transfers a finite-precision approximation to the original Weyl sum; it does not show the original Weyl sum tends to zero as the sample length grows.

## D. A SOURCE-SPECIFIC finite-to-analytic bridge already in BBP

Freeze authentic SUCC forcing

`r(n)=4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)`, n≥1,

and `U_0=s`, `U_n=16U_{n−1}+r(n)`. Its BBP series gives `π/16 = Σ_{j≥1}16^{-j}r(j)`. With a finite horizon L, set

`P_L=Σ_{j=1}^L 16^{-j}r(j)`,

`T_n^(L)=Σ_{j=n+1}^L 16^{n-j}r(j)` for 0≤n≤L, with `T_L^(L)=0`.

The exact cocycle law (finite arithmetic, no real analytic assumption) is

`16 T_{n-1}^(L) = r(n)+T_n^(L)`.

Consequently, for **every** 0≤n≤L and every rational seed s,

`U_n(s)+T_n^(L)=16^n(s+P_L)`.

The inhomogeneous source recurrence is thus **finite-horizon conjugate** to homogeneous ×16 motion by a source-derived, time-dependent correction. For zero seed, this approaches the genuine lifted circle orbit `16^n π/16`. This is a naturality-square construction, not just fitted agreement at a terminal endpoint.

### D.1. Rigorous quantitative tail (stronger than a crude 1/L bound)

One can prove for every integer n≥1:

`0 < r(n)=(120n²−89n+16)/[(2n−1)(4n−1)(8n−7)(8n−3)] < 4/n²`.

For the upper inequality, multiply by the strictly positive denominator. The numerator of `4D(n)-n²A(n)`, written in `m=n−1≥0`, is

`1928m⁴+3705m³+2379m²+531m+13 > 0`.

Therefore the omitted future satisfies

`0 < E_L := π/16−P_L < [4/(15(L+1)²)]16^{-L}`.

For every 0≤n≤L, the original-zero completed orbit obeys the certified error estimate

`0 < 16^n π/16 − (U_n(0)+T_n^(L)) < [4/(15(L+1)²)]16^{n−L}`.   **(BBP-gluing)**

And for any integer frequency h,

`|e^{2πih16^nπ/16} − e^{2πih(U_n+T_n^(L))}| < [8π|h|/(15(L+1)²)]16^{n−L}`.

This proves a **source-specific, finite-resolution bridge from rational computations to the Archimedean circle**, with complete error accounting. It is not a new theorem asserting source-selected signed cancellation. To obtain π normality one must additionally show for each fixed h≠0:

`(1/A)Σ_{n=A}^{2A−1} e^{2πih(U_n+T_n)} → 0`, or an equivalent authentic source-selected gate, as A→∞.

Proving a high-precision approximation to that sum, even uniformly in A, does not prove that the sum itself decays. Coherent wrong seeds and periodic controls remain essential.

## E. Gluing is a higher-categorical structure, not automatically a theorem

Let a source-observer presheaf `F` assign finite observations to chart contexts, with restriction maps and retained source metadata. To reconstruct a global observation, compatible local data must satisfy the **sheaf equalizer**:

`F(U) → ∏ F(U_i) ⇉ ∏ F(U_i∩U_j)`.

For program objects/transformations, a stack or higher descent theory requires isomorphisms on overlaps plus cocycle/higher coherence; pointwise pin agreement alone is not enough. For nontrivial phase connections, compare transported paths around plaquettes and keep holonomy rather than quotienting it away. At the sphere's center, polar `R+×S²` must collapse the angular S² to a single apex to obtain the full 3-ball. These boundary and quotient rules are **additional carrier data**.

## F. Falsification checklist and integration target

1. **Omega compiler:** Can one tagged `Omega_5` execution recover all three independent successor directions and preserve causal provenance? Bare Omega_5 is a countermodel.
2. **Approximate pullback:** Does source-labelled shared coordinate disagreement shrink with certified resolution, and does the projected midpoint preserve lawful transformations? A numeric midpoint alone may fail source constraints.
3. **Nontrivial winding:** Ensure the glued line-circle observer retains integer carry cocycles; otherwise the compiler falsely identifies a circle with a line.
4. **Topology firewall:** Distinguish Archimedean circle completion from the 16-adic inverse-limit algebra; they encode different notions of nearness.
5. **Limit-order firewall:** Keep observation-depth k and time-sample A as independent parameters. State the precise uniform estimate needed for any exchange.
6. **Source-specificity:** Any theorem claiming actual π cancellation must distinguish literal U0=0 from source-compatible coherent wrong seeds; the exact BBP conjugacy itself is seed-independent.
7. **Strong norms:** Uniform C0 convergence of geometric pin positions does not ensure convergence of derivatives, curvature, causal generators, or phase transport. Stronger source-respecting regularity is required.

**Next discriminating mathematical instrument:** Build an exact `16×16` pinbed whose cells carry original BBP lift, time-directed source correction, integer carry, and circle-valued oscillator reading; compare (i) two-axis evaluation, (ii) curried compiler, (iii) single compressed clock. Require preservation of source-labelled winding and signed future-conditioned Fourier probes. The uniform approximation bound (BBP-gluing) should pass; selected all-epoch signed cancellation remains an independent OPEN test.

## Sources / provenance

- SUCC Main XXI `docs/PI_NORMALITY_FRONTIER.md`, `observational_succ/duck_bbp.py` (authentic forcing, selected seed, Green-tail gauge), and SUCC PRs #541, #543, #565, #568, #571 and #574. These represent independent *modules* but share the same research provenance.
- Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, available at `https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/LambdaCalculus/Barendregt1984TheLambdaCalculus.ItsSyntax%2BSemantics.RevisedEdition.pdf` (unsolvables and Scott interpretation).
- The Stacks Project, sheaf condition: `https://stacks.math.columbia.edu/tag/00VL`.
- Cambridge, Hindley & Seldin, *Lambda-Calculus and Combinators*, chapter on Scott's D-infinity: `https://www.cambridge.org/core/books/abs/lambdacalculus-and-combinators/scotts-d-and-other-models/843F623394908CC3BEF9D4C6D419206B`.
- Domain theory lecture notes: `https://www.cs.cmu.edu/~rwh/students/niu.pdf`.

## Local tests

Run `python /mnt/data/succ_omega_gluing_probe.py`. Fraction-backed original BBP finite conjugacies, fiber-product epsilon repair, circle winding/carry, compact-probe models, noncommuting limit controls, and finite-character orbit checks passed in the local runtime. The script does not certify the infinity tail by numeric exhaustion; the displayed rational-polynomial positivity proof does.