# Operation Four-Point SUCC: Seinfeld zero → projective triangle → golden elliptic curve → Kronecker cusp

**2026-10-25. Research-stage steelman, crucible, and verdict.** Proposed stacked parent: draft [MRMW #301](https://github.com/femboy2112/SUCC/pull/301), which itself stacks on source-authenticated [Spectral Purity #298](https://github.com/femboy2112/SUCC/pull/298) and internal matrix [#296](https://github.com/femboy2112/SUCC/pull/296). Distinct sibling inputs were READ, NOT MERGED: Seinfeld zero [#294](https://github.com/femboy2112/SUCC/pull/294), Seinfeld relative-phase/Frobenius [#295](https://github.com/femboy2112/SUCC/pull/295), independently refined Möbius matrix [#299](https://github.com/femboy2112/SUCC/pull/299), carrier-relative target [#300](https://github.com/femboy2112/SUCC/pull/300), and Gamma reference/seam [#302](https://github.com/femboy2112/SUCC/pull/302). Main, imported archival sources, and original four-pole BBP forcing remain unchanged. **No π normality, RH, geometric uniqueness, source-selected signed saving or scholarly-priority claim.**

## 0. Exact user hypothesis and the crucial typing correction

The author proposes the triangle `0 ↔ 1 ↔ ∞ ↔ 0`, with finite/continuum/Archimedean viewpoints; an Euler–Mascheroni perturbation near φ^(-1); a fourth SUCC point; and Seinfeld null histories, Möbius incidence, and internal Fourier Gram walks on one diagram. Its strongest defensible formalization requires three DIFFERENT carriers, with explicit maps:

1. **Projective boundary**: the marked points `0,1,∞` on the real projective line `RP¹=R∪{∞}`, topologically a circle. They are three distinct projective points. This is **not** the additive circle `R/Z`, on which `0` and `1` are equal.
2. **Arithmetic dynamics**: genuine unwrapped `U_0=0, U_n=16U_(n−1)+r(n)`, with the original signed four-pole `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`. Its circle readout is `{U_n}`; its whole integer lift, carries and source clock cannot be erased.
3. **Archimedean analytic completion**: Gamma, harmonic/logarithmic finite parts, period lattices and analytically continued Epstein zeta values; these require a declared scale and subtraction prescription. Numeric equality between scalars alone is not an identification of these carriers.

Consequently `0 ↔ 1 ↔ ∞` can be modelled as a **diagram of charts and explicit transition maps**, not literal equalities of finite objects with continuum cardinalities or an automatic categorical equivalence. The projective line already has continuum-many points; the distinguished coordinates are labels.

## 1. Three marked points are rigid; a fourth gives a real invariant

On the upper half-plane with curvature −1, the ideal hyperbolic triangle with boundary vertices `0,1,∞` has three zero angles. Gauss–Bonnet yields **area π**. A four-vertex ideal quadrilateral has area **2π**, regardless of its cross-ratio; its area therefore cannot fingerprint its shape. Equilateral Euclidean triangles alone do not canonically select the golden ratio; a 36°/72° pentagonal or a separate self-similarity law is required.

`PGL₂` acts sharply triply transitively on three distinct projective points, hence an ordered triple has no free cross-ratio. For four ordered distinct projective points, the **exact** determinant expression

`CR(A,B;C,D) = [A,C][B,D] / ([A,D][B,C])`, where `[A,B]=a_A b_B−a_B b_A`,

is unchanged by invertible 2×2 projective transformations. With homogeneous coordinates `(∞,0;1,λ)`, the value is exactly `λ`. For the fourth marked point choose `λ∈(0,1)`. If an extra golden renormalization rule is DECLARED, `T(λ)=1/(1+λ)`, the unique positive fixed point is

$$
\boxed{\lambda=\frac{\sqrt5-1}{2}=\varphi^{-1},\qquad\lambda^2+\lambda-1=0.}
$$

This is a meaningful **selection mechanism** for φ that makes explicit the additional dynamical hypothesis. Projective geometry alone does not force that choice.

## 2. The four-point elliptic lift has exact j=2048

Take a branched double cover of `P¹` at the four labels `0,1,λ,∞`. Riemann–Hurwitz gives `2g−2=−4+4=0`, hence genus one. In Legendre coordinates its nonsingular model is

$$E_\lambda:\quad y^2=x(x-1)(x-\lambda),\quad \lambda\ne0,1.$$

The classical elliptic invariant is

$$j(E_\lambda)=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}.$$

At the declared golden fixed point `1−λ=λ²`, and therefore

$$\boxed{j(E_{\varphi^{-1}})=256\frac{(2\lambda^2)^3}{\lambda^2\lambda^4}=2048.}$$

The exact rational model `E:y²=x³−30x+25` has the **same j** by `j=1728(4a³)/(4a³+27b²)`, with `a=−30`, `b=25`, and is nonsingular because `4a³+27b²=−91125≠0`. Equality of j yields isomorphism **over an algebraic closure**, not a distinguished identification over Q, nor a source-specific isomorphism to BBP. The six anharmonic transforms `λ,1−λ,1/λ,1/(1−λ),λ/(λ−1),(λ−1)/λ` share j, so the j-observer forgets marked-label/orientation data. Classical reference: [j-invariant lecture](https://personalpages.manchester.ac.uk/staff/gabor.megyesi/teaching/math32062/j-inv.pdf); [NIST DLMF modular lambda/J relation](https://dlmf.nist.gov/23.19).

**Exact source probe:** Use the *actual* finite BBP rational orbit as a time-varying projective fourth point `λ_n={U_n}`, retaining the full unwrapped state as a separate authenticated field. At n=1 the original source has `U_1=47/15`, `λ_1=2/15`, and `j(λ_1)≠2048`. Thus no automatic theorem that the original BBP source selects the **constant** golden Legendre curve is possible from this simple mapping. A source-compatible fourth-point constraint or explicitly time-dependent elliptic family must still be proved.

## 3. Euler–Mascheroni as an ACTUAL degenerating-geometry finite part

Let `τ=x+iy` in the upper half-plane, `y>0`, and define the area-normalized Epstein series

$$
Z(\tau,s)=\sum_{(m,n)\in\mathbb Z^2\setminus\{(0,0)\}}\frac{y^s}{|m\tau+n|^{2s}},\quad\operatorname{Re}s>1.
$$

Use its analytic continuation and define `FP_(s=1)Z = lim_(s→1)(Z(τ,s)−π/(s−1))`. The **classical first Kronecker limit formula**, in precisely this normalization, is

$$\boxed{\operatorname{FP}_{s=1} Z(\tau,s)
=2\pi\big[\gamma-\log2-\log(\sqrt y|\eta(\tau)|^2)\big].}$$

Reference: [published Springer source with this normalization](https://link.springer.com/article/10.1007/s10955-021-02768-4); [Kronecker limit formula derivation](https://link.springer.com/article/10.1007/s11139-022-00586-0). This is not an original SUCC theorem. It is a **genuine existing analytic realization** of the user's proposed structure: one finite part contains both a universal Euler boundary term and a lattice-shape-dependent fingerprint.

At `τ=iy`, let `q=e^(−2πy)`, and write the Dedekind product as

$$\eta(iy)=e^{-\pi y/12}\prod_{n\ge1}(1-q^n).$$

Exact algebra in the Kronecker limit formula yields

$$
\operatorname{FP} Z(iy,1)=\frac{\pi^2 y}{3}-\pi\log y
+2\pi(\gamma-\log2)-4\pi\sum_{n\ge1}\log(1-q^n).
$$

The branch collision `λ→0` sends its Legendre period ratio `τ_λ=iK(1−λ)/K(λ)` toward `i∞`. Define the **declared cusp subtraction**

$$R(y)=\operatorname{FP}Z(iy,1)-\frac{\pi^2y}{3}+\pi\log y.$$

Then, without inserting γ into the **definition of R**, the theorem gives

$$\boxed{\gamma=\log2+\frac1{2\pi}\lim_{y\to\infty}R(y).}$$

Furthermore `−log(1−t)≤t/(1−t)` on `(0,1)` and `1−q^n≥1−q` imply the **explicit positive exponential error bound**

$$\boxed{0<R(y)-2\pi(\gamma-\log2)\le\frac{4\pi q}{(1-q)^2},\quad q=e^{-2\pi y}.}$$

Thus gamma is exactly recoverable as the finite boundary remainder of a **degenerating four-point/elliptic geometry with a chosen Archimedean lattice normalization**. Its value is not inferred from λ≈γ; it comes from the Epstein/eta analytic theorem. Another subtraction convention changes the reported finite constant and must carry its conversion term. This directly respects [#302](https://github.com/femboy2112/SUCC/pull/302)'s `γ_c=γ−c` reference transport.

For the declared golden interior point let `τ_φ=iK(1−φ^(-1))/K(φ^(-1))`. Define `Σ(τ)=log(√y|η(τ)|²)`. Directly subtracting two Kronecker finite parts gives a source-independent **shape fingerprint**

$$\boxed{\operatorname{FP}Z(\tau_\varphi,1)-\operatorname{FP}Z(i,1)
=-2\pi\log\frac{\sqrt{y_\varphi}|\eta(\tau_\varphi)|^2}{|\eta(i)|^2}.}$$

The **universal γ cancels** in this shape comparison. Numerically `y_φ≈0.896256112326`, the golden finite part is `≈2.609518640861`, and its difference from the square lattice is `≈0.024536881282`. Those digits are explicitly **uncertified mpmath diagnostics**, independently checked by a convergent Poisson/Bessel expansion with extrapolation; they are not finite mathematical certificates.

**A legitimate γ-vs-golden reference perturbation** is `F_λ(z)=e^{λz}Γ(1+z)` for `|z|<1`. The canonical Gamma series gives

$$\log F_\lambda(z)=(\lambda-\gamma)z+
\sum_{m\ge2}\frac{(-1)^m\zeta(m)}m z^m.$$

At the golden fixed λ, the first-jet mismatch is **exactly** `φ^(-1)−γ≈0.040818323848`. However this first jet changes under Γ_c from #302; `λ` was an explicitly selected reference. No special closeness law or determination of γ from φ alone is established. Reference: [NIST DLMF Gamma expansions](https://dlmf.nist.gov/5.7).

## 4. Adding the fourth point to Seinfeld chains creates two NEW cycles, not four independent constraints

For a labelled triangle `K₃`, the rational edge-chain cycle rank is `E−V+1=3−3+1=1`. For tetrahedral complete graph `K₄`, rank is `6−4+1=3`: a fourth vertex produces **two additional independent cycles**. Its four oriented triangular face boundaries satisfy the exact 2-chain syzygy

$$\boxed{\partial([123]-[023]+[013]-[012])=0.}$$

The four faces span only a three-dimensional edge-cycle space. This is a rigorous *Seinfeld zero with prior structure*: a nonzero labelled 2-chain whose boundary cancels. Counting all four face relations as independent would reproduce the known macro-zero rank error from #294. Möbius incidence over face subsets may diagnose signed higher interactions, but #299 already certifies authentic negative unordered Möbius contrasts. No general positivity is inherited from atomic Grams.

## 5. Sixteen inverse branches: a useful structural mismatch, not a hidden isomorphism

For the authentic circle affine SUCC map `x↦16x+r(n) mod1`, inverse fibers are torsors for `C₁₆`, which includes elements of order 16. On an elliptic curve over characteristic zero, the kernel of multiplication by four is `E[4]≈(Z/4Z)²`, also of order 16 but exponent 4. **Those groups are not isomorphic.** This invalidates a tempting identification from 16 matching labels alone.

Nevertheless multiplication-by-4 on E descends through `E/{±1}≈P¹` to a rational **Lattès map of degree 16**. In the rational model `y²=x³−30x+25`, the x-coordinate doubling map is

$$\boxed{D_2(x)=\frac{x^4+60x^2-200x+900}{4x^3-120x+100},\qquad D_4=D_2\circ D_2.}$$

Its reduced rational degree is **16** (exact SymPy polynomial computation, and independently the classical degree formula `deg[m]=m²`). The x-quotient has four branch values from the four 2-torsion points, while the SUCC circle dynamics after `z=e(x)` has form `z↦e(r(n))z^16` and only two critical values `{0,∞}`. Therefore these rational maps cannot be simply Möbius-conjugate at any step. A *different* semiconjugacy, correspondence, observer quotient or source-labelled interface is still allowed but must be constructed and tested.

The elliptic 4-torsion has the abstract alternating Weil pairing `e₄((a,b),(c,d))=i^(ad−bc)`. The sixteen labelled ququart Weyl operators `X^a Z^b` on C⁴ are Hilbert–Schmidt orthogonal, supplying a finite symplectic **candidate Fourier basis**. The focused tests verify this exact finite algebra (entries in `{0,±1,±i}`) and its orientation, without claiming the BBP character `e(hU_n)` is a Weil pairing. The base-16 four-bit Walsh highest-order even-parity counterfeit still defeats all 14 lower nontrivial masks. A 16-element operator basis supplies new coordinates, not the arithmetic distribution theorem.

## 6. A decisive NO-GO for any j-only attempt at π normality

Let α be any irrational number, `x_n={nα}`, and `y_n=min(x_n,1−x_n)`. Then x_n is equidistributed on the circle, whereas y_n is entirely contained in `[0,1/2]`, so it is NOT circle-equidistributed. But the elliptic invariant has exact anharmonic symmetry `j(t)=j(1−t)`, giving

$$\boxed{j(y_n)=j(x_n)\quad\text{for every }n.}$$

All observations of the scalar elliptic j along the histories agree **pointwise**, yet their circle equidistribution properties are opposite. This is a rigorous hostile counterexample showing that a `j`-only observer, however elegant, cannot establish source-selected Weyl cancellation. One must retain marked branch/orientation and genuine SUCC integer lifts, or prove a new source-specific descent condition that restores them. This precisely matches the target-access discipline of #300.

## 7. Test ledger, independent routes and the next verdict-changing instrument

Files: `observational_succ/seinfeld_four_point.py` (pure exact Q and Q(√5)); `observational_succ/four_point_kronecker.py` (explicitly numerical Gamma/eta/Epstein diagnostics); `tests/test_seinfeld_four_point.py` (11 adversarial test groups); `scripts/seinfeld_fourpoint_probe.py`; source-hashed `SEINFELD_FOURPOINT_RECEIPT.json`.

**Observed local scope:** Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0; 11/11 grouped unittest checks passed. Exact PGL₂ cross-ratio invariance under 250 seeded matrices, exact quadratic-field proof `j=2048`, all 6 anharmonic variants, actual first 19 authenticated rational four-point readouts, tetrahedral face matrix rank 3, C16-vs-C4² group exponents, 16 Hilbert–Schmidt Weyl operators, exact degree-16 Lattès composition, four-bit parity hostile histogram, and two separate mpmath routes for the Kronecker finite part were exercised. Initial JSON replay failed because tuples and JSON arrays differ; the serialization normalization was corrected and `--verify` then passed. `compileall` passed. **The local parent source was an expressly declared narrow API shim, not the authentic full GitHub checkout.** Native full-repo tests, provenance/observer/ordinal commands and hosted CI are separate pending gates; no Lean kernel declarations claimed.

**Next probe (OPEN):** Construct an explicit source-faithful map from the time-varying **marked** elliptic fourth-point lifts `(n,U_n,c_n,P,k)` into the signed Fejér innovation of #298/#301, retaining integer carries, exceptional p=3/p=5 numerator cancellations, moving n²/n³ frequency boundaries, and original zero initial state. Predeclare an all-N inequality for at least one fixed nonzero h with a bound smaller than N, and verify which precise selected four-pole term makes it fail on (i) #294 SS-08 positive nonnormal source, (ii) #297 changed-initial/exact-forcing controls, (iii) #298 full-conductor fake, (iv) #301 same-carry/tower fake and (v) the j-alias equidistribution counterexample above. If only j, symmetry, PSD, Kronecker constant or finite interaction plots survive, **that does not imply π normality**. The missing signed all-N estimate remains the frontier, not a solved theorem.

**Claim ledger:** projective cross-ratio + ideal area + 4-point Legendre j + cusp Kronecker = CLASSICAL PAPER-PROVED; source four-point exact readouts, tetra syzygy, C16 vs C4² and Weil/Weyl finite operator checks = EXACT FINITE (with classical proof where stated); numerical golden shape = OBSERVED, noncertifying; j-only normality route = REFUTED by counterexample; geometric SUCC source factor, signed Weyl cancellation, π normality and RH = OPEN/UNVERIFIED. No new result claims academic novelty.
