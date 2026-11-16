# Main XXVI — signed observer error through a retained Gamma source

**Status:** PROVED PAPER, a composite deduction from the existing signed action-defect telescoping law and the declared Gamma/negative-binomial source law. This is a quantitative interface theorem, not an estimate on the original π winding. It claims no academic priority. Same-model review and exact finite controls are recorded separately from the proof.

## Contract and provenance

Let V,W be complex Banach spaces, K:V→V and B:W→W bounded linear contractions in the **declared norms**, and P:V→W bounded linear. Declare the one-step signed defect D=PK−BP. P need not be surjective or a contraction. The products below have their displayed order; K and B need not commute with P or D. For real α≥0 use the norm-convergent Gamma operator

\[
F_\alpha(A)=(2I-A)^{-\alpha}
=\sum_{n\ge0}w_n^{(\alpha)}A^n,\qquad
w_n^{(\alpha)}=\frac{\Gamma(n+\alpha)}{\Gamma(\alpha)n!2^{n+\alpha}}
\quad(\alpha>0),\qquad F_0=I.
\]

The source law and its normalization are [GV-04](../research/2026-11-14/gamma_volume/THEOREMS.md); its two-loop retained source is GV-05. The signed finite-word defect identity is [TD2.2](../research/2026-11-14/tenacious_d/UNIFIED_THEOREMS.md), proved in [DEFECT_AND_GAUGE](../research/2026-11-14/tenacious_d/DEFECT_AND_GAUGE.md). Exact versus approximate descent and hidden-fiber minimax error remain different contracts; see [Principia CG-02/03](principia_observatoris/02_causality_geometry.md). These are common mathematical inputs, not independent evidence for π normality.

## OGT-01 — Sharp Gamma transport of a one-step signed defect

For every real α≥0,

\[
\boxed{\|PF_\alpha(K)-F_\alpha(B)P\|\le\alpha\|PK-BP\|.}
\]

**Proof.** At α=0 both sides vanish. At each integer n≥1 direct telescoping gives

\[
PK^n-B^nP=\sum_{j=0}^{n-1}B^{n-1-j}DK^j.
\]

Contraction gives norm at most n‖D‖. GV-04's nonnegative coefficients have total mass one and generating function `(2−z)^−α`. Differentiating the convergent scalar power series at z=1 gives `Σ n w_n^(α)=α`. The series of signed operator differences is absolutely norm-convergent, dominated by `Σ n w_n^(α)‖D‖`. Summing the exact identity and taking its norm proves the assertion. No expectation has been inserted inside a nonlinear phase observable. ∎

The constant α is optimal uniformly over these contracts. In one dimension put K=1, B=1−ε, P=1 for 0<ε<1. Then ‖D‖=ε and

\[
\frac{\lvert PF_\alpha(K)-F_\alpha(B)P\rvert}{\|D\|}
=\frac{1-(1+\epsilon)^{-\alpha}}{\epsilon}\longrightarrow\alpha.
\]

This uses elementary differentiation at zero. It is not a numerical sharpness inference. For α=0 the optimal constant is zero.

At order one there is also an exact independent algebraic route:

\[
PF_1(K)-F_1(B)P=F_1(B)D F_1(K).
\]

Multiplication by `(2I−B)` on the left and `(2I−K)` on the right reduces both sides to D. For contractions each resolvent norm is at most one, recovering the bound. This independent algebraic check shares the same source/operator definitions.

## OGT-02 — The authentic two-loop factor is retained

For x∈[0,1], set

\[
u=x-x^2/2,\quad v=x^2/2,\quad a=(1-u)(1-v),\qquad
G_x(z)=\frac{a}{(1-uz)(1-vz)}.
\]

Let `Qx,α(A)=Gx(A)^α`, defined by GV-05's nonnegative, norm-convergent coefficient law, including the continuous conditional endpoint at x=1. Then

\[
\boxed{\|P Q_{x,\alpha}(K)-Q_{x,\alpha}(B)P\|
\le\alpha\left(\frac{u}{1-u}+\frac{v}{1-v}\right)\|D\|
\le2\alpha\|D\|.}
\]

**Proof.** The generating function `Gx(z)^α` has mass one. Its derivative at one is `α[u/(1−u)+v/(1−v)]`. Apply the same signed telescoping identity and sum with those coefficients. Since u,v∈[0,1/2], each ratio is at most one. At x=0 the law is the identity and the error is zero. At x=1, u=v=1/2 and `Q1,α=F2α`. The scalar sharpness family in OGT-01 with shape 2α shows the uniform factor 2α is optimal. ∎

For strongly measurable retained-source fields with an authenticated probability measure μ, pointwise contracts and integrable bounds permit the further estimate

\[
\left\|\int\left(P_xQ_{x,\alpha}(K_x)-Q_{x,\alpha}(B_x)P_x\right)d\mu(x)\right\|
\le\alpha\int\left(\frac{u}{1-u}+\frac{v}{1-v}\right)\|D_x\|d\mu(x).
\]

The integral exists whenever the operator-valued integrand is Bochner integrable; finite-dimensional bounded measurable matrix fields suffice. This is **one average of a retained-source comparison**, not composition of separately averaged layers. GV-06's exact compression defect `ΠSα(I−JΠ)SβJ` still applies if the shared coordinate is forgotten between layers.

## Crucible and boundary

The theorem steelmans coherent transport of approximate observer models. The contraction hypothesis is essential: at α=1, scalar K=19/10, B=9/5, P=1 gives left side 5 while ‖D‖=1/10. The minimum repair is the declared contraction domain (or a separately proved resolvent-growth budget), not a claim that every nonsingular resolvent has the stated bound.

These are upper bounds on forward transport error. They give no converse from a small Gamma-averaged defect to small D: GV-10's order-six alias is a retained countermodel. They establish no lower bound for actual carry escape, no original-source signed temporal cancellation, no physical source map and no new R0 or normality theorem. Source authentication, actual integer winding, real-circle phases and stochastic observer laws remain distinct objects.

Finite controls are implemented by [the exact rational probe](../scripts/main_xxvi_observer_transport_probe.py). It checks the signed noncommuting resolvent identity, integer-shape contraction instances, original two-loop coordinates, sharpness ratios and the noncontraction mutant. Its successful run is evidence for those finite cases only. The universal authority is the norm-convergent derivation above.
