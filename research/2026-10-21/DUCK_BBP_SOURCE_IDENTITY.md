# The BBP source identity, independently reconstructed and kernel checked

The BBP identity is classical, due to Bailey, Borwein and Plouffe,
*Mathematics of Computation* 66 (1997), 903–913,
[DOI 10.1090/S0025-5718-97-00856-9](https://doi.org/10.1090/S0025-5718-97-00856-9).
An [author-hosted primary manuscript](https://plouffe.fr/articles/ON%20THE%20RAPID%20COMPUTATION%20OF%20VARIOUS%20POLYLOGARITHMIC%20CONSTANTS%201997.pdf)
identifies the exact coefficients. This note supplies the independently derived
calculus reduction implemented in `formal/duck_pi/BBPIntegral.lean`.
It is not a novelty claim or a digit-distribution theorem.

Put P(x)=4−2x³−x⁴−x⁵ and F(x)=P(x)/(1−x⁸/16) for 0≤x≤1.
Exact rational simplification gives

\[
F(x)=\frac{4x}{x^2-2}-\frac{4(x-2)}{x^2-2x+2}.
\]

All denominators stay nonzero on this interval. A primitive is

\[
G(x)=2\log(2-x^2)-2\log(x^2-2x+2)+4\arctan(x-1).
\]

Direct differentiation proves G′=F. At the endpoints G(1)=0 and G(0)=−π,
using the standard arctangent value. The fundamental theorem of calculus
therefore gives ∫₀¹F(x)dx=π.

The geometric expansion F(x)=Σₙ≥0 P(x)(x⁸/16)ⁿ is justified pointwise and
by the summable uniform majorant |P(x)(x⁸/16)ⁿ|≤8·16⁻ⁿ.
Dominated termwise integration gives

\[
\pi=\sum_{n\ge0}16^{-n}
\left(\frac4{8n+1}-\frac2{8n+4}-\frac1{8n+5}-\frac1{8n+6}\right).
\]

The Lean proof uses actual `Real.pi`, interval integrals, geometric summability
and dominated convergence from pinned mathlib. Its final `HasSum` declaration
has no BBP identity hypothesis. It compiled in [run 39613723244](https://github.com/femboy2112/SUCC/actions/runs/39613723244)
at `6fbe9d29355aaccca5ebf2753d34eee2e2ece627`; that *combined* run failed in
the separate Weyl extension. See the [current exact-source receipt](DUCK_PI_KERNEL_RECEIPT.md)
for subsequent validation.

For r(m)=4/(8m−7)−2/(8m−4)−1/(8m−3)−1/(8m−2), let
T_n=Σₖ≥1 16⁻ᵏr(n+k), and x₀=0, xₙ=16xₙ₋₁+r(n) before passing to the circle.
The exact recurrence gives xₙ+Tₙ=16ⁿT₀. The proved source identity is π=16T₀.
Thus for every n≥0,

\[
16^n\pi=x_{n+1}+T_{n+1},\qquad
d_{\mathbb R/\mathbb Z}(x_{n+1},16^n\pi)
\le T_{n+1}\le\frac{r(n+2)}{15}\le\frac1{(8n+9)^2}.
\]

`PiSource.lean` composes these independently established statements without a
new source axiom. The source identification gap is closed here. The global
equidistribution gap is entirely different and remains open.
