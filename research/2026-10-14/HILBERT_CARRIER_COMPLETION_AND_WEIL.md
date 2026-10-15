# HILBERT-CARRIER SUCC — finite addresses, complete square, source martingales and signed Weil wavefronts

**Research checkpoint:** 2026-10-14, after Phoenix II. **Exact parent:** \`main@03db44203147a7b28d445bb9f970fa71360e78c4\`. **Research branch:** \`research/hilbert-carrier-completion-2026-10-14\`. **No main edit, merge or release. RH PROVED: NO.**

## 0. Main reorientation: source facts, model proposal, formal obligation

The newly integrated \`main\` contains all 43 research PRs #57–99. Its integration audit reports **3,350 full-suite Python tests passing locally**; GitHub Actions on the exact consolidated main \`03db4420\` is also **green**. Importantly, the research frontier is no longer "does a completed arithmetic source exist?" but (1) actual source **30-moment Legendre low/high Suzuki sign**, (2) rigorous low/high **zero-shift** Douglas/Feshbach coupling as \(\lambda\downarrow0\), and (3) all compact test radii with one true Euler/Gamma/pole/half-density source, without reading nontrivial zero coordinates. In particular \`docs/RESEARCH_FRONTIER_2026-10-14.md\` warns that high-mode positivity is relative to the inverse-Neumann K metric **not \(\kappa I\)** and the legitimate shifted Schur is still RH-hard.

The author's new insight: "the Hilbert fractal" can connect an O-origin finite successor curve with a whole global square in the limit and give useful locality/integration machinery. The mathematically relevant object is **David Hilbert's space-filling curve**, NOT an abstract Hilbert-space vector, and NOT a Zeno clock that physically visits infinitely many cells. Its two essential properties are **nested 4-adic parameter intervals ↔ dyadic spatial squares** and **continuity/measure preservation after classical completion**. There are two distinct questions:

1. **TRUE / CLASSICAL, made source-operational here:** Can a finite-description, nested SUCC grammar certify *arbitrarily good spatial coverage* and *the mathematical limiting surjection*? Yes, with an explicit dyadic error and classical compactness.
2. **FALSE shortcut:** Does the curve's dense/complete image supply a one-to-one smooth parametrization, an isomorphism of \(H^1\) derivative forms, an operator sign theorem, or a physical proof of every unobserved original state? No. Those require additional source/domain/topology hypotheses, and several are mathematically impossible.

References: Hilbert 1891 classical construction, A. R. Butz, *Convergence with Hilbert's space-filling curve*, JCSS 3 (1969), 128–146 (DOI 10.1016/S0022-0000(69)80010-3); John Skilling, *Programming the Hilbert Curve*, AIP Conf. Proc. 707 (2004), 381–387; Alan Schoenfeld, *Continuous Measure-Preserving Maps onto Peano Spaces*, Pacific J. Math. 58 (1975), 627–642, https://msp.org/pjm/1975/58-2/pjm-v58-n2-p34-s.pdf ; Andrej Bauer, *Space-filling curves, constructively*, 2024, https://math.andrej.com/2024/01/30/space-filling-curves-constructively/ . Academic mathematical novelty UNVERIFIED; the assembly is new to SUCC.

## 1. A precise source-indexed 4-adic successor tower — HC-01 (CLASSICAL CONSTRUCTION + TESTED EXACT ALGORITHM)

At finite resolution k>=1, let \(\mathcal T_k=\{I_{k,d}=[d/4^k,(d+1)/4^k]\}_{d=0}^{4^k-1}\) and \(\mathcal Q_k\) be the \(2^k\times2^k\) dyadic square tiling of \([0,1]^2\). The standard Hilbert recurrence produces a bijection
\[
 \boxed{h_k:\{0,\ldots,4^k-1\}\overset{\sim}{\longrightarrow}
 \{0,\ldots,2^k-1\}^2.}\tag{HC1}
\]
For every adjacent time index, \(h_k(d)\) and \(h_k(d+1)\) share a square side (taxicab distance exactly 1). For every parent prefix \(p\) at depth j<=k, all indices \(d\in[p4^{k-j},(p+1)4^{k-j})\) map to the ONE dyadic square \(h_j(p)\), subdivided into \(4^{k-j}\) child squares. These source-aware commuting refinement squares are the main data. \`hilbert_carrier.point\`, \`index\`, \`prefix_square\`, \`coverage\` are pure integer and rational implementations, exhaustively checked through practical finite levels and independently invert each other's directions.

At finite k, the set of tile **centers is finite, never the whole continuum**. The \(\mathcal T_k\) intervals and \(\mathcal Q_k\) tiles have equal measure \(4^{-k}\) but finite equality of their sizes is not yet a global Lebesgue-measure theorem.

### CLASSICAL completion construction and certified finite tubes — HC-02

For an exact rational t∈[0,1], choose the index \(d_k=\min(4^k-1,\lfloor4^k t\rfloor)\) and its corresponding dyadic spatial tile \(Q_k(t)\). Prefix coherence gives a nested sequence of closed squares with diameter \(\sqrt2\,2^{-k}\). Cantor's nested compact intersection theorem yields one point \(H(t)\) in the intersection. At 4-adic endpoints, left/right choices agree because the respective adjacent Hilbert cells always share an edge and their diameter tends to zero. The resulting **classical continuous limit**
\[
\boxed{H:[0,1]\twoheadrightarrow[0,1]^2}
\]
is surjective: given any target q in the square, choose a nested sequence of dyadic cells containing q. Their inverse Hilbert intervals are nested and compact; their intersection contains a parameter t with H(t)=q. This is an ordinary mathematical proof about an infinity of cells described by a finite rule, **not** a physical \(\omega\)-step execution. The code \`parameter_tube\` returns the finite spatial enclosure and exact squared center-to-limit bound
\[
 \boxed{\|H(t)-c_k(t)\|_2^2\le\frac{1}{2\cdot4^k}.}\tag{HC2}
\]
Conversely \`target_preimage_tube\` returns an exact interval of length \(4^{-k}\) containing **at least one possible** source parameter for any rational target (including dyadic boundaries); it does not compute an infinite-precision inverse, a unique inverse, or a globally continuous section.

**Quantitative continuity:** if \(|s-t|\le4^{-k}\), their level-k Hilbert cells coincide or are neighboring time cells, whose spatial union has diameter at most \(\sqrt5\,2^{-k}\). Choose k with \(4^{-(k+1)}<|s-t|\le4^{-k}\). Then
\[
 \boxed{\|H(s)-H(t)\|_2^2\le20|s-t|.}\tag{HC3}
\]
Thus the familiar \(1/2\)-Hölder regularity is *derived from finite adjacency + nested source*, with explicit constants. More-than-half Hölder regularity is impossible for any surjection from interval to square: split time into m intervals; their images have diameter O(m^{-alpha}), yielding planar area O(m^{1-2alpha}), which tends to zero if alpha>1/2. A particularly simple exact **finite area witness** for hypothetical Lipschitz constant L uses m=floor(4L²)+1 intervals: images lie in m axis-aligned squares of total area at most \(4L²/m<1\). The code emits this exact rational bound and refuses to label H Lipschitz. Hence there can be no bi-Lipschitz parametrization, and inverse locality cannot be inferred from the forward Hölder modulus.

**Exact inverse-locality countercontrol:** at k=3, two GRID-ADJACENT cells have Hilbert indices 5 and 58 (separation 53) and coordinates (3,0),(4,0). At k=4 their analogous index gap reaches 213. Space-near need NOT mean parameter-near. By contrast consecutive Hilbert parameter cells are spatial-near, while a row-major ordering has occasional jumps of length \(2^k\).

### Constructive-logic caveat — HC-02a (CLASSICAL SEMANTIC COUNTERCONTROL)

Andrej Bauer (2024) explicitly distinguishes "every square point has distance zero to the curve" from the *internal* assertion "every point has a local continuous parameter section." The ordinary Hilbert curve is classically surjective, but such an internal surjectivity assertion fails in the sheaf topos \(\mathrm{Sh}([0,1]^2)\); the internal quantifier requires locally continuously chosen preimages. This is a genuinely important SUCC language/source warning: **the same diagram can carry different existence/choice requirements in different mathematical logics**. The code implements the classical rational finite tubes, not a topos semantics or a constructive universal section.

## 2. Measure-preserving traversal and \(L^2\) isometry — HC-03 (CLASSICAL SCHOENFELD + EXACT FINITE CALIBRATION)

For the standard Hilbert limit, each 4-adic parameter interval of length \(4^{-k}\) maps onto its corresponding dyadic square of area \(4^{-k}\). Distinct square interiors are disjoint, and the exceptional dyadic grid boundary set has planar measure zero. Matching measures on the generating dyadic-square algebra gives
\[
\boxed{H_*\lambda_{[0,1]}=\lambda_{[0,1]^2}.}\tag{HC4}
\]
Schoenfeld (1975) specifically discusses the Hilbert map's measure-preserving symmetry and proves the broader theorem for Peano spaces with full-support probability measures. The map is one-to-one away from a measure-zero set of dyadic grid boundaries (uniqueness of the nested tile address), so its **measurable** inverse exists almost everywhere. Thus
\[
 U:L^2([0,1]^2)\to L^2([0,1]),\qquad (Uf)(t)=f(H(t))
\]
is a **unitary isomorphism of measure Hilbert spaces**, with
\[
\langle Uf,Ug\rangle_{L^2[0,1]}=\langle f,g\rangle_{L^2([0,1]^2)}.
\]
Here "Hilbert" refers *both* to a space-filling curve and to the modern \(L^2\) Hilbert space, but the two notions are not synonyms.

**No H¹ transport (critical).** A continuous globally Lipschitz 1D parametrization cannot fill positive planar area. If BOTH coordinate functions of H lay in the 1D Sobolev \(H^1[0,1]\), they would be absolutely continuous and H would be rectifiable, again unable to fill planar area. Therefore at least one smooth coordinate function on the square pulls back to a function **not belonging to \(H^1[0,1]\)**. A legitimate *source* \(L^2\) isometry does **not** automatically preserve SUCC's completed-Weil \(H_0^1\) derivative form or compact domain. Nor does a continuous surjection admit a continuous inverse/section.

**Finite exact implementation:** \`exact_cell_inner_product\` encodes any complete rational dyadic square cell arrays by Hilbert order and verifies the full bilinear form exactly:
\[
4^{-k}\sum_d u(h_k(d))v(h_k(d))
=4^{-k}\sum_{x,y}u(x,y)v(x,y).
\]
This is a **basis permutation/measure correspondence**, not a new source covariance, physical observer, or whole-form Weil sign.

## 3. Hilbert martingale / conditional expectation and source-derived rate — HC-04 (CLASSICAL L² + PROVED LOCAL POLYNOMIAL INSTANCES)

On the square, let \(E_k\) be orthogonal conditional expectation onto the finite sigma algebra generated by the depth-k dyadic squares. Under U, the corresponding 4-adic time intervals carry **the same** finite stage:
\[
 U E_k f=\mathbf E[Uf\mid\mathcal F_k^{4\text{-adic}}].
\]
The finite source code evaluates exact rational square-polynomial cell means and norms, including
\[
 \|E_k f\|_2^2=4^{-k}\sum_d |\operatorname{avg}_{Q_{k,d}} f|^2,
 \qquad
 \|f-E_k f\|_2^2=\|f\|_2^2-\|E_k f\|_2^2.
\]
Dyadic simple functions are dense in L², so \(E_kf\to f\) **strongly** in L² for every fixed f, by classical martingale/conditional-expectation or density theory.

**Source-regularity rate:** if original source f is a rational polynomial, its explicitly bounded coordinate gradients \(L_x,L_y\) supply
\[
 \boxed{\|f-E_kf\|_2^2\le(L_x+L_y)^2\,4^{-k}.}\tag{HC5}
\]
For f(x,y)=x the exact error is **\(1/(12\cdot4^k)\)**, verified by independent polynomial integral and cell average arithmetic.

**Sharp no-go to uniform all-source completion:** for *each* finite k, choose a source-normalized Haar oscillation within one dyadic tile, equal \(+2^k\) on its left half, \(-2^k\) on its right half, and 0 elsewhere. This exact piecewise-constant function has L² norm one but \(E_k f=0\). Therefore
\[
 \boxed{\|I-E_k\|_{L^2\to L^2}=1\quad\text{for every }k.}\tag{HC6}
\]
So source-specific strong convergence does NOT imply operator-norm convergence on the entire L² unit ball. Uniform rates need a source regularity/compactness class. The Haar example is a declared nonarithmetic negative control, **not** an alternative original Weil Euler source.

## 4. Certified source integration by one successor curve — HC-05 (PROVED LOCAL EXACT, CLASSICAL MIDPOINT)

The measure-preserving correspondence suggests an exact finite approximation to 2D Lebesgue integration using the single one-dimensional Hilbert visit order:
\[
 Q_k(f)=4^{-k}\sum_{d=0}^{4^k-1} f(c_{k,d}).
\]
For a source-polynomial f on the square with independently computed bounds
\(M_{xx}\ge\|\partial_{xx}f\|_\infty\), \(M_{xy}\ge\|\partial_{xy}f\|_\infty\), \(M_{yy}\ge\|\partial_{yy}f\|_\infty\), midpoint Taylor cancellation on **each actual cell** yields
\[
\boxed{
\big|Q_k(f)-\int_{[0,1]^2}f\big|
\le
4^{-k}\left(\frac{M_{xx}+M_{yy}}{24}
+\frac{M_{xy}}{16}\right).}\tag{HC7}
\]
The \(\partial_{xy}\) term uses \(\operatorname{avg}|\delta x\delta y|=h^2/16\); for the pure x²/y² second terms use \(\operatorname{avg}\delta x²=h²/12\). For f=x²+y² the exact quadrature error is
\[
\boxed{|Q_k(f)-2/3|=1/(6\cdot4^k),}
\]
**attaining the Hessian upper bound exactly** at every k. Affine source polynomials integrate exactly already at k=1; mixed terms can have favorable cancellation. \`RationalPolynomial\` refuses float terms, duplicate monomials, invalid basis/epochs; \`exact_quadrature\` verifies true analytic polynomial integrals independently from Hilbert summation.

**Important distinction:** \(\int_0^1 f(H(t))\,dt=\int_{[0,1]^2}f\,dA\) is a measure-pushforward / area-integral statement; it is **NOT** integration with respect to arc length \(ds\) along a rectifiable physical path. Hilbert's curve has infinite length and no globally ordinary 1D line-integral reparametrization supplying area measure.

## 5. The **actual signed Suzuki** source uses Hilbert order — HC-06 (PROVED LOCAL FINITE, CLASSICAL OPERATOR BOUNDS)

Original main contains \`observational_succ/source_weil_hierarchy.py\`, an exact outward Fraction interval source for the **signed** Suzuki screw potential \(g_J\) with authentic \(\Lambda(p^k)/\sqrt{p^k}\), its only real Gamma ladder, poles/contact and half density. On mean-zero \(L_0^2(-a,a)\), its N-cell normalized matrix is
\[
 M_{ij}=h\,\widetilde g_J\big(h|i-j|\big),\quad
 N=2^k,\;h=2a/N.
\]
We now generate its full **N×N original-source cell entries** in canonical 2D Hilbert order of (i,j), for 1<=k<=4 and valid parent J,a. \`hilbert_suzuki_stream.source_stream\` replays the original parent \`stage(a,J,N)\`, visits each entry once, reconstructs the **exact identical** full signed matrix and refuses forged field values/source epochs or float-equivalent proof data. \`source_matrix_pair_witness\` independently evaluates any exact mean-zero Rayleigh quotient in BOTH original row-major and Hilbert stream, and requires literal equality. Thus no Gram sign, spectrum, or RH claim can change by ordering.

**Locality gives a true analytic read-order bound, not a new eigenvalue bound.** Since adjacent Hilbert matrix cells change exactly one coordinate by ±1, their original scalar difference arguments differ by at most h. With inherited authentic source-certified \(\mathrm{Lip}(g_J)\le L_J(a)\) and per-node original interval radius \(\eta\), successive rational normalized matrix entries obey
\[
\boxed{|M_d-M_{d+1}|\le h^2 L_J(a)+2h\eta.}\tag{HC8}
\]
A raster sweep instead has jumps of \(N\) cells across row boundaries. This may improve streaming locality or adaptive source evaluation ordering, but it does NOT improve the original operator-norm error \(\|G_a-\widetilde G\|\) or establish any negative spectral gap. The inherited mean-zero **positive omitted Gamma tail** and one-sided Loewner bounds remain intact but unchanged by the permutation.

**Type firewall:** the Hilbert curve parametrizes the 2D **kernel data coordinates (x,y)**, not a new 1D unitary coordinate change on the original Suzuki state space \(H_a=L_0^2(-a,a)\). Even a unitary L² reparametrization would preserve, not create, signed spectral positivity; \(H^1\) derivative transport is NOT supplied. Original low/high 30-moment Legendre/Schur and \(\lambda\downarrow0\) remain unresolved.

## 6. A source-specific computational avenue: adaptive nonsmooth wavefront geometry — HC-07/08 (EXACT FINITE SOURCE, CLASSICAL CODIMENSION)

The original signed \(g_J(|x-y|)\) contains source-specific **hinges** at
\[
 \boxed{x-y=\pm\log(p^r)\qquad(p^r\le e^{2a})}
\]
because the authentic prime term is \((|x-y|-r\log p)_+\). In the first prime window \(a=1/2\), only the primitive n=2 hinge is active; the fake composite 6 **must not** be allowed as an independent Euler place.

**Necessary correction:** the OTHER nonsmooth carrier locus \(x=y\) ALSO matters: the original \(r=|x-y|\) contact and finite positive Gamma OU resolvents depend on |r| and need not be C² across the diagonal, even before ANY prime-power hinge becomes active. Therefore this project has two clearly typed profilers:
- \`adaptive_profile\`: prime-power hinge lines ONLY, not a full source smoothness oracle.
- \`operator_singularity_profile\`: the origin diagonal **AND every original prime-power hinge**, certified with exact \(\log n\) rational outward intervals from the original source. Regions marked "smooth" are separated from every detected nonsmooth locus of the fixed finite-J source; **no high-order quadrature estimate is asserted unless derivative bounds are separately proved**.

Each line \(x-y=c\) meets at most O(N) cells on an N×N uniform square grid, since within any fixed x-column a strip of thickness ≤2h intersects only a bounded number of y-cells. The classifier conservatively uses at most \(8N\) finest transition tiles for each true n=p^r pair of ± diagonals, plus \(4N\) for the central x=y diagonal. Hence for fixed a and finitely many prime powers,
\[
 \boxed{\#\{\text{finest nonsmooth tiles}\}
 \le(4+8P_a)\,2^k,\quad
 P_a:=\#\{p^r\le e^{2a}\}.}\tag{HC9}
\]
All source-visible hinge intervals are rigorously classified as **ACTIVE, INACTIVE or TRANSITION**; fake 6 and float radius are rejected. A Hilbert-prefix quadtree refines only TRANSITION blocks. Since each depth contributes O(2^j) transitions, the number of adaptive leaves through depth k is O(2^k) for fixed \(P_a\), rather than O(4^k) on the naive uniform grid.

**What this DOES and DOES NOT accelerate:** it provides an exact, contiguous finite observation schedule for **identifying wavefront geometry**, so future certified piecewise smooth quadrature may spend expensive source-interval probes near kinks. It does not yet calculate full high-accuracy \(g_J\) integrals, improve the difficult 30-dimensional genuine Schur resolvent, control the entire signed operator's tail, or show a smaller computation than the main branch's direct analytic low-Legendre polynomial integrals. Existing main \`suzuki_moment_schur.py\` already avoids N² spatial sampling for direct low matrix entries; its zero-shift **high cross/resolvent coupling** is the real blocker.

## 7. Best next steps — concrete dependency graph, after Phoenix II

**P0 (done in this draft, gate by CI):** exact 4-adic↔2D Hilbert tower and inverse, rational forward/target tubes, finite 1/2-Hölder and no Lipschitz controls, source-polynomial Hessian quadrature, strong-not-uniform Haar obstruction, genuine Suzuki signed matrix read-only streaming, full nonsmooth diagonal+true-prime wavefront atlas, typed source/epoch/basis and immutable main provenance, exact replay. New-to-project assembly of mature classical proofs.

**P1 (immediate implementation):** use the authenticated **finite-J g_J operator atlas** to derive *actual piecewise second-derivative enclosures*, including the Gamma/contact diagonal strip, true \(\log2\) first hinge, and exact arithmetic source interval errors; certify a multilevel **operator norm** bound that is strictly sharper than parent global Lipschitz \(\sim11/N\) at \(a=1/2\). Test against the existing main source \`stage\` and independent direct Legendre integrals. A pretty Hilbert traversal without a strictly justified error or resource gain is **not** a research advance on RH.

**P2 (RH frontier, deeper):** build a source-authenticated original \(\lambda\)-regularized 30-dimensional **15+15 parity Schur cross-resolvent**. Main PR #96 derives finite exact low Legendre Gamma and true first-prime source entries; PR #99 identifies Douglas range/shorted-operator \(\lambda\downarrow0\) as the RH-hard gate. The needed deliverable is **an actual norm-controlled evaluation of \(B(D+\lambda I)^{-1}B^*\)** and a source-correct finite sign certificate, not a Hilbert-geometric PSD analogy. Hilbert quadtree ordering is an optional certified 2D kernel quadrature backend; its a.e. L² isometry does **not** justify \(H_0^1\) derivative transport.

**P3 (formal, orthogonal):** Lean4.14/mathlib source-indexed dyadic cylinders, covers and Cauchy/completion; obtain theorem-checked Hilbert continuity/Hölder and measure-preserving pullback by reusing established measure/compactness libraries. Test constructive/classical distinction as in Bauer 2024. No new Lean proof is asserted until kernel compilation.

**P4 (cross-framework application):** benchmark locality for sparse graph edges, causal-grid histories, field tensor discretization and adaptive scientific visualization, with independently measured wall clock and memory. Do not claim Hilbert strictly improves cache efficiency over source's existing Toeplitz/analytic compression without controlled benchmarks.

### Source and sign checklist

Preserve original \(\Lambda(p^r)=\log p\), \(\sqrt{p^r}\) half-density, complete real Gamma/contact, both polar signs, mean-zero \(u=iv'\), compact test domains and numerical/transcendental interval enclosures. A source-positive auxiliary covariance or a discrete Hilbert permutation is **not** the authentic completed Weil form. A fixed finite Hilbert curve is not the infinite limit; the infinite limit is not a physical observation or Hilbert-space \(H^1\) isomorphism; strong L² convergence is not uniform L²/operator-norm convergence. **RH remains open.**

## 8. Reproduction and exact evidence

Files:
- \`observational_succ/hilbert_carrier.py\`: exact integer d↔xy maps, prefix-compatible tubes, polynomial quadrature, finite L² cylinder isometry, Haar no-go, finite Lipschitz area impossibility.
- \`observational_succ/hilbert_prime_wavefront.py\`: source-true interval hinge classification plus diagonal-aware adaptive quadtree, Hilbert ordered with no missing/overlapping dyadic source squares.
- \`observational_succ/hilbert_suzuki_stream.py\`: authentic main source \`source_weil_hierarchy.stage\` replay, exact signed matrix permutation and per-successor genuine analytic bound; never promotes a Gram sign.
- \`tests/test_hilbert_carrier.py\`, \`test_hilbert_prime_wavefront.py\`, \`test_hilbert_suzuki_stream.py\`: independent exact finite proofs and adversarial signs/source mutations.
- \`scripts/hilbert_carrier_probe.py\`, \`research/2026-10-14/HILBERT_SOURCE_COMPLETION_RECEIPT.json\`: frozen original-source receipt, no nontrivial zero inputs.
- \`docs/CLAIM_SUPPLEMENT_HILBERT_CARRIER.md\` and dedicated Python 3.10/3.13 CI + inherited genuine Weil focused regressions + original immutable provenance.

This project **does not claim** construction of a physical sensor, scholarly priority, a globally smooth inverse, constructive sheaf-local global section, precise physical resource law or proof of RH. Full main suite and Lean kernel CI are separate from the dedicated feature workflow.


## 6a. Full genuine finite-J signed Suzuki *cell integrals* with NO midpoint interpolation — HC-09 (PROVED LOCAL using classical elementary antiderivatives)

A consequential mathematical extension of the source-first Hilbert traversal is that **the actual finite-J signed Suzuki kernel can be integrated over any rational rectangular cell exactly up to certified transcendental-constant enclosures**, without sampling \(g_J\) at a center and extrapolating across its kinks. The finite compressed matrix is an exact Galerkin object, not a midpoint surrogate.

Let \(x\in[x_0,x_1]\), \(y\in[y_0,y_1]\). Define
\[
 F_b(x_0,x_1;y_0,y_1)=
 \frac{(x_1-y_0-b)_+^3-(x_0-y_0-b)_+^3
       -(x_1-y_1-b)_+^3+(x_0-y_1-b)_+^3}{6}.
\tag{HC10}
\]
By two elementary integrations,
\(\iint(x-y-b)_+\,dx\,dy=F_b\), hence
\[
\boxed{\iint(|x-y|-b)_+\,dx\,dy
       =F_b(x_0,x_1;y_0,y_1)+F_b(y_0,y_1;x_0,x_1).}\tag{HC11}
\]
No smoothness restriction or "do not cross a prime-wavefront" assumption is needed. The formula **already handles the hinge exactly**. For genuine \(n=p^r\), substitute \(b=\log n\) and multiply by **exact source weight** \(w_n=\log p/\sqrt n\). Original SUCC \`source_weil_hierarchy.log_iv\` and \`sqrt_inverse\` provide rigorous outward rational intervals; because the entire hinge integral decreases monotonically in b, \([\log n]^-,[\log n]^+\) give source-certified rational lower/upper integrals with **zero spatial quadrature error**. Fake composite 6 is rejected, as are inactivated prime powers outside the window. This is the classical truncated-power/B-spline antiderivative mechanism, not novel calculus.

**The original Gamma integral ALSO has a closed source form, including the diagonal.** For \(\alpha>0\) define
\[
 A_\alpha(t)=
 \begin{cases}
  [e^{-\alpha t}-1+\alpha t]/\alpha^2,&t>0,\\
  0,&t\le0.
 \end{cases}
\]
Then \(A_\alpha''(t)=e^{-\alpha t}\mathbf1_{t>0}\) as a locally integrable distribution, with no delta artifact because \(A_\alpha(0)=A_\alpha'(0)=0\). Thus the same four-corner difference as HC10, with \(A_\alpha\) in place of \((t)_+^3/6\), plus its exchanged x/y rectangle, gives
\[
\boxed{\iint e^{-\alpha|x-y|}\,dx\,dy}
\tag{HC12}
\]
on every genuine rational cell (even a cell crossing \(x=y\)). Each finite original Suzuki Gamma rung
\(-4(1-e^{-(4j+1)|x-y|/2})/(4j+1)^2\)
therefore has an **exact cell integral**, enclosed by outward \(\exp\)-intervals. The authentic original pole
\(-4(e^{(x-y)/2}+e^{-(x-y)/2}-2)\)
integrates by separable exponentials; the original contact \(C_G|x-y|/2\) integrates via HC11 at b=0. Every term of \`source_weil_hierarchy.screw_interval\` is retained, with correct signs and one original real Gamma ladder. This construction is implemented by
\`observational_succ/hilbert_suzuki_cell_integrals.py\`.

For equal-width interval cells \(I_i,I_j\) with h=2a/N, the original \(\ell^2\)-normalized **finite projection** entry is
\[
 \boxed{\langle e_i,G_{a,J}e_j\rangle
       =h^{-1}\int_{I_i}\int_{I_j}g_J(x-y)\,dx\,dy.}\tag{HC13}
\]
The source engine returns a rigorous exact-rational **interval enclosure** for every such matrix entry and visits the complete N² array in Hilbert order without changing any signs or sources. The **spatial quadrature error of the finite projected block is identically zero**; only outward transcendental interval uncertainty remains. A separate independent original \`stage(a,J,N)\` midpoint matrix must agree *within its established \(h^2 L_J+h\eta\) bound*. An independent high-precision **numerical holdout**, not used as proof authority, checks the actual original \`signed_suzuki_g\` integrated against a triangular cell-pair geometry.

**Load-bearing distinction:** \(P_NG_{a,J}P_N\) still differs from the full compact operator \(G_{a,J}\) on all mean-zero L² directions. **No claim that \(\|G_{a,J}-P_NG_{a,J}P_N\|=0\)** follows from eliminating *midpoint quadrature error*. The original globally sourced projection and positive Gamma-tail bounds remain necessary. Nor does the finite compressed operator's sign prove the all-test signed Weil form.

**Actual next computational experiment:** Couple these interval-exact original Galerkin entries with the proper mean-zero contrast basis and parity modes; certify finite Schur blocks with **validated original** high cross/resolvent enclosures. Compare their widths and resulting \(\lambda\)-gates with main \`suzuki_moment_schur.py\`'s already superior direct analytic 30-mode low Legendre formulas. Any improvement must be demonstrated, not presumed from Hilbert ordering. The source engine is deliberately budgeted to small N and finite J; it has **not** constructed the authentic complete zero-shift Schur matrix.

**Adversarial findings retained:** a prime-only spatial quadtree misses the ORIGINAL \(x=y\) Gamma/contact singular locus; HC-08 includes it. At coarse k=2, a fully source-aware adaptive atlas can have **all 16** cells, so "adaptive beats uniform at every finite resolution" is **REFUTED**; only the asymptotic O(N) transition-cell theorem and measured high-k reductions are asserted. Exact antiderivative integration avoids the prime/Gamma kink crossing issue without needing adaptive refinement at all. This means adaptive Hilbert ordering's incremental value is **visit scheduling and possible efficient hierarchical compression**, not a source-sign or integration-accuracy shortcut when full analytic primitives already exist.
