# Source audit: Gemini's √2 / π / grid / circle intuition

**Reading rule:** distinguish the supplied geometric intuition from the statements proved by elementary mathematics, and from its proposed use in SUCC's *selected* BBP orbit.

| Supplied idea | Precise mathematical status |
| --- | --- |
| `Z²` disk count divided by `R²` approaches π | **Correct** for a prescribed Euclidean metric; unit-square tiling gives `N(R)=πR²+O(R)` and an explicit error. This is area normalization, not a proof of base-16 normality. |
| Bare `N×N` exhausts `R²` as a set | **Not literal:** the unscaled integer grid remains countable and discrete. A *rescaled* mesh `(1/R)Z²` becomes dense, and Riemann-sum convergence supplies the measure limit. Cardinality alone does not select π. |
| π is singled out by isotropic `L²` geometry | **Correct in the stated Euclidean/rotationally invariant metric choice.** In `ℓ^p`, the inner-product parallelogram identity is special to `p=2`; arbitrary other norms yield different unit-ball constants. L¹/L∞ perimeter-to-diameter formulas must use an explicitly chosen intrinsic metric; mixing Euclidean and intrinsic lengths changes the numbers. |
| The single local unit diagonal is √2 | **Correct:** chord from `(1,0)` to `(0,1)` has length √2, and the square-diagonal ratio is √2. The inscribed four-sided polygon's *perimeter-to-diameter* ratio is `2√2`, not √2. |
| Viète joins finite radicals to the global π limit | **Correct.** The dyadic inscribed/circumscribed polygon ladder supplies algebraic approximants with certified `O(N^{-2})` error and a classical nested radical product. This does not classify all transcendental numbers as a single canonical complexity level. |
| Ellipse with semimajor a has perimeter `4a E(e)` | **Correct**, but its perimeter divided by the **major diameter** `2a` is **`2E(e)`**, not `4E(e)`. At e=0, E(0)=π/2 and the ratio is π. |
| Every irrational follows from algebraic boundary perturbations | **Not correct.** There are countably many finite algebraic specifications, but uncountably many irrationals. Smooth paths can encode arbitrary irrational parameters only if those parameters are allowed in the perturbation data; that is not a constructive classification. |
| Gaussian integers, complex tori and modular forms | **Genuine connections** when the lattice, metric, automorphic forms and L-function are concretely specified; they do not imply that every named irrational such as ζ(3) comes from an arbitrary torus shear without additional mathematics. |
| The entire lattice disk has uniform angular directions | **Correct with an explicit error**, proved here for all arcs by unit-square sector tiling. The primitive directions have a Möbius `O(log R/R)` error. A chosen sparse *subpath* can still concentrate on an axis and fail completely. |
| `√2` is local, π is global | **Useful relative metaphor**, not a unique mathematical hierarchy. A local algebraic value can be an infinite limit and a period can have finite closed representations; classifications depend on permitted operations, metric and observation language. |

## Exact source-specific connection worth studying

The genuine BBP rational integral root from PR #579 reduces classically to

```math
K(x)=\frac{16(1-x)}{(2-x^2)((x-1)^2+1)}
```

with a primitive consisting of `4 arctan(x-1)` plus a logarithm whose endpoint values cancel. Its remaining denominators exhibit **real quadratic poles at ±sqrt(2)** and **Gaussian poles at `1±i`**. This makes the user's local-√2 / global-angular-π motif concrete **for this source**. It is not an independent cancellation estimate for the digits: the analytic integration coordinate x in `[0,1]` is not the chronological index n of `16^nπ`.

A normalized cumulative source coordinate `Θ(x)=π^{-1}∫_0^x K(t)dt` pushes the positive measure `K(x)dx/π` to Haar on `[0,1]`. This is the general probability-integral-transform identity, so by itself it cannot select the original-zero BBP orbit from a wrong-seed orbit. The interesting problem is a **source-labelled chronological map** from the arithmetic updates to this angular coordinate with a new rigidity/occupancy estimate.

## Mathematics provenance

- [Gauss circle count and classical lattice tiling](https://mathworld.wolfram.com/GausssCircleProblem.html)
- [Viète product and dyadic polygon limit](https://mathworld.wolfram.com/PiFormulas.html)
- [Jordan–von Neumann parallelogram identity](https://www.mathematik.uni-muenchen.de/~michel/jordan-von_neumann_-_parallelogram_identity.pdf)
- [SUCC authentic source-first inverse-beta / Mellin root](../omega_bbp_operational_completion/INVERSE_BETA_BBP_ROOT.md)
- [Main XXIII frontier](../../../docs/PI_NORMALITY_FRONTIER.md)
