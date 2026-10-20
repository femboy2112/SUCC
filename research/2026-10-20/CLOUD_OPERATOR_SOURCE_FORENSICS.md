# Cloud lane D: primitive completion and a constrained signed-source inverse

Date: 2026-10-20. Parent: `main` at
`0e56e0ae26f3d52a2ea34c0a4288478139fcb634`. The detached PR201 head
`cbc4010458c00be995b8af3f229c9bba410301e2` was inspected without modification.
This lane adds independent files only. No original module, Claude branch,
shared claim registry or archived source is edited.

**Earned result:** a further exact positive-definite improvement of BOTH
parity blocks of the current first-window signed-source Schur lower at
J=8, M=80. The improvement retains polynomial constraints that the previous
ambient inverse discarded. Both improved lower blocks remain negative
definite: the true S4 sign is **OPEN/AMBIGUOUS**, not refuted. RH is OPEN.
The general inverse identity is classical. Its paid application to this
particular original-source enclosure is new to this project, with no claim
of academic priority. No infinite-dimensional Lean proof is asserted.

## 1. Hole contract and source reconstruction

The proposed implication is a typed one:

`q(u) >= kappa <Ku,u>` on derivative tests, `K=V*V`

`=>` a closed primitive form with an inverse bounded by `1/kappa`,

and then a source-faithful inverse bound on an actual continuum residual.
The implication requires kernel descent, primitive closability, a declared
completion and a genuine form core. A lower bound alone supplies none of
those missing identifications. The weakest useful target is a fixed finite
window and its four-low/high decomposition; it is much weaker than all-radius
Weil positivity. Cheapest falsifiers are a nonclosable transported form,
a dense non-core, and a source residual outside the high moment space.

The live source is more advanced than older ledger summaries suggest:
`full_prime_resolvent.py` and
`research/2026-10-18/ROUND2_SIGNED_PRIME_RESOLVENT.md` already contain an
all-high Bessel bound and an explicit primitive form-core argument. Older
`INHERITED_SOURCE_CONDITIONAL` labels must not erase those later proofs.
Conversely, their existence is not formal-kernel verification.

**Byte provenance correction.** The source module
`observational_succ/source_weil_hierarchy.py` has retained Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`. It is NOT an entry in
`provenance/IMPORT_MANIFEST.json`. Git introduces that path at SUCC commit
`b0cef75f47de29b1326b351df35b9e5423f2ed4f` on October 14, 2026. The sentence
in `ROUND2_SIGNED_PRIME_RESOLVENT.md` attributing this file's origin to the
October 10 FuckingRH import commit `ba075348...` is unsupported by the actual
file genealogy. The latter commit is the provenance anchor for the separately
listed 72 imported items, not for this later implementation. The retained-byte
pin remains valid. This distinction changes provenance, not the derived
operator's sign. Reproduce with:

```sh
git log --all --diff-filter=A --format='%H %ad %s' --date=iso -- observational_succ/source_weil_hierarchy.py
git ls-tree 0e56e0ae26f3d52a2ea34c0a4288478139fcb634 observational_succ/source_weil_hierarchy.py
```

Primary-paper check, retrieved October 20: Suzuki's latest displayed version
is v3, September 23, 2026. Theorem 1.1 identifies the primitive self-adjoint
realization as a Friedrichs extension; §§8.4–8.5 distinguish the derivative
norm quotient from the K-generalized quotient. Equation (1.3) supplies the
prime/Gamma/pole/contact normalization. These are source identifications and
classical operator statements, not a proof of all-radius positivity.

## 2. Exact completion-transport theorem

**COT-01 — CLASSICAL, complete proof below.** Let H and G be real or complex
Hilbert spaces, V:H→G bounded, K=V*V, and D0⊂H a linear space. Put
N=D0∩ker(V), E=closure(V D0) in G. Let q0 be a Hermitian sesquilinear form on
D0 with q0[u]≥κ||Vu||² for all u∈D0, where κ>0 is independent of u.
Assume:

1. q0(n,u)=0 for every n∈N and u∈D0 (descent through the actual kernel).
2. The descended form t0(Vu,Vv)=q0(u,v) is closable in E. Explicitly, whenever
   Fn∈VD0, Fn→0 in E and t0[Fn−Fm]→0, one has t0[Fn]→0.

Then D0/N with norm ||[u]||K=||Vu|| completes isometrically onto E.
The closure t of t0 is densely defined, closed and satisfies
t[F]≥κ||F||² on its form domain Q. There is a positive self-adjoint operator
T on E, with form domain Dom(T^(1/2))=Q, satisfying T≥κI and
||T^(-1)||≤1/κ. For each r∈E there is exactly one x∈Q such that
t(x,v)=<r,v> for all v∈Q; it is x=T^(-1)r. Moreover

`<r,T^(-1)r> = sup_{v in Q} (2 Re<r,v> - t[v]).`             (1)

If a separately specified closed source form t_source agrees with t0 on VD0,
its identification with t additionally requires VD0 to be a **form core**
for t_source. E-density alone is insufficient. No conclusion says that T is
bounded, that V has a bounded inverse in its original norms, or that the
derivative operator has an ordinary L² gap.

**Proof.** Kernel descent makes the quotient and form well-defined. V is an
isometry for the quotient norm and has dense image in E, so its extension is
unitary. Closability constructs the E-valued form closure. For a convergent
form-Cauchy sequence the lower bound passes to the limit. The norms t[F]^(1/2)
and (t[F]+||F||²)^(1/2) are equivalent by κ>0, so Q is complete for t.
The functional v↦<r,v> is bounded there by ||r||/sqrt(κ). Riesz representation
gives unique x and t[x]=<r,x>; hence ||x||≤||r||/κ. The solution map is bounded,
positive, self-adjoint, injective and has dense range on E. Its inverse is
the positive self-adjoint form operator (equivalently the first representation
theorem), with spectrum in [κ,∞). Completing the square in the t inner product
gives (1). Finally, equality of closed forms follows by form-norm closure
precisely under the core hypothesis. ∎

The theorem also covers a negative semibound by adding a multiple of the
primitive norm before closing. An inverse bound requires the stated positive
κ after that shift is removed; semiboundedness by itself is not coercivity.

### 2.1 Minimal failures and correct compact example

**COT-02 — REFUTED implication (kernel omitted).** In R² let V(x,y)=x and
q0(x,y)=x²+y². Then q0≥|V|² but q0(0,1)=1≠q0(0,0); no form descends through V.

**COT-03 — REFUTED implication (primitive closability omitted).** Take
H=G=ℓ²(N), Ve_n=e_n/n, and h=(1/n)_n∈ℓ². On ALL of H set

`q0[u] = ||Vu||² + |<u,h>|² >= ||Vu||².`

This is a bounded nonnegative form, hence closed on the original H; V is
injective, compact and dense-range. In primitive coordinates F=Vu its domain
is V(H)={F:Σn²|F_n|²<∞}, and

`t0[F] = ||F||² + |Σ F_n|².`

Let F^(m) have its first m entries 1/m and remaining entries zero. Then

`||F^(m)||²=1/m`, `t0[F^(m)]=1+1/m`,

`t0[F^(m)-F^(n)]=1/m+1/n-2/max(m,n) -> 0.`

The primitive form is NOT closable. Thus original closedness plus a K-relative
positive lower bound cannot replace condition 2. Countably infinite dimension
is essential for this obstruction; a densely defined finite-dimensional form
has full finite-dimensional domain and is continuous. The exact sequence
receipt is checked independently by direct finite coordinate sums.

**COT-04 — REFUTED implication (dense domain substituted for form core).** On
L²(0,1) let q_ext[f]=∫|f'|²−|f(0)|²−|f(1)|² with domain H¹(0,1).
Trace bounds give, for every ε>0,

`|f(0)|²+|f(1)|² <= ε||f'||² +(2+4/ε)||f||².`

Indeed integrate the fundamental theorem for |f|² from each endpoint and
apply Cauchy–Schwarz and Young. At ε=1/2, q_ext+11||·||² is an equivalent
H¹ norm, so q_ext is a closed semibounded form. Its restriction to H¹_0 has
q[f]=||f'||²≥2||f||²: use f(x)=∫_0^x f' and integrate |f(x)|²≤x||f'||².
H¹_0 is L²-dense, but it is not a core of q_ext. The constant f=1 has
q_ext[1]=−2. Positivity on a merely dense subspace does not transfer to a
different closed extension.

**COT-05 — classical positive control.** With the same compact V=diag(1/n),
q0[u]=||Vu||² transports to t[F]=||F||² on E=ℓ². The derivative operator is
K=diag(1/n²), with no positive absolute gap, while the primitive operator is
I, with gap one. Compactness in derivative coordinates and coercivity in
primitive coordinates coexist without contradiction. The stronger
q0[u]=||u||² instead transports to the closed unbounded primitive operator
diag(n²), showing why a lower bound does not give a bounded extension.

## 3. Source realization and quantitative gap actually audited

At I=(−1/2,1/2), V is integration from −1/2 on derivative L²_0(I).
Its primitive image is H¹_0(I). The derivative high space is orthogonal to
P0,...,P4. Integration by parts maps it to H¹_0(I)∩E, where

`E = {F in L²(I): <F,x^j>=0 for j=0,1,2,3}.`

Closure in primitive L² gives exactly E. Derivative odd corresponds to
primitive even, and derivative even to primitive odd. The original high
K-bound becomes an ordinary lower bound only on that primitive completion.

Directly differentiating the source screw channels with sign −g'' gives

`H_J = Γ_J − C I − w A_b + 2|cosh(x/2)><cosh(x/2)|`
`                         − 2|sinh(x/2)><sinh(x/2)|,`

`Γ_J = Σ_{j<J}(4/(4j+1) I − E_{(4j+1)/2}),`

where E_α has kernel exp(−α|x−y|), b=log2, w=log2/sqrt2 and
C=γ+π/2+3log2+logπ. Since log2<1<log3, this window has precisely the genuine
n=2 prime-power input. No zeros are inputs; the real Gamma factor, both
opposite pole signs, contact and half-density remain present.

The Gamma Fourier symbols are

`m_j(ξ)=16ξ²/[(4j+1)((4j+1)²+4ξ²)] >= 0.`

Their increasing sum defines a closed nonnegative form on zero-extended
L²(I); bounded contact, translation and rank-two pole terms preserve
closedness and semiboundedness. The finite-moment core is justified by
shrinking support, mollifying, and removing moments with four fixed smooth
interior functions. The controlling dilation inequality
m(λξ)≤max(1,λ²)m(ξ) follows termwise. It gives strong continuity in the
weighted Fourier norm, and the finite moment-correction matrix is positive
definite. This reproduces the relevant existing core argument, independently
of its finite sign computations. H¹_0 lies in the Gamma operator domain
because m(ξ)≤5|ξ|. The clamped trials used below lie in H²_0 and therefore
have legitimate complete-source L² action residuals.

The current all-high comparison uses the full Legendre tail via Bessel's
inequality, a 256-rung Gamma lower, rigorous spherical-Bessel tails and
signed contact/pole/prime subtraction. Its rational lower margins exceed
κ=63/500 (primitive even) and κ=153/500 (primitive odd). Retaining the true
prime mismatch gives, on the correct parity form domain,

`D >= B_E,   B=κI+w0(I−A_b),   w0=12/25 <= log2/sqrt2.`      (2)

The existing code computes the same all-high budgets by a distinct factorial
coefficient implementation. Our fresh replay reran that computation; this
is shared analytic provenance, not a new independent source. Equation (2)
is the inherited source inequality used in the new theorem below.

## 4. Constraint-aware inverse theorem

**COT-06 — CLASSICAL identity with complete proof.** Let B be a bounded
self-adjoint operator on a Hilbert space G, B≥κI for κ>0. Let
h1,...,hm∈G be linearly independent and L:C^m→G have these columns.
Put E0=ker L*, M=L*B^(-1)L and

`T0=B^(-1)−B^(-1)L M^(-1)L*B^(-1).`                         (3)

Then T0 is positive semidefinite, T0≤B^(-1)≤κ^(-1)I, and for every r∈E0,

`<r,(B|E0)^(-1)r> = <r,T0 r>`
`                   = <r,B^(-1)r> − z* M^(-1)z,`
`z=L*B^(-1)r.`                                             (4)

Here B|E0 means its orthogonal compression, not an invariance assumption.
If a closed positive form D on a smaller subspace E⊂E0 dominates B there,
then for r∈E, `<r,D^(-1)r> <= <r,T0 r>`.

**Proof.** M is positive definite. Maximizing
2Re<r,v>−<Bv,v> subject to L*v=0 gives the unique stationary point
v=B^(-1)(r−L M^(-1)L*B^(-1)r)=T0r. It lies in E0 and is the global
maximizer by strict positivity of B. This proves (4) and the compression
interpretation. Formula (3) also equals B^(-1/2)(I−P)B^(-1/2), with P the
orthogonal projection onto range(B^(-1/2)L), proving its order bounds.
The final statement follows from (1) by enlarging the maximization domain
and replacing the source form by its lower comparator. ∎

If the hj are orthogonal with dj=||hj||², then M≤κ^(-1)diag(dj), so

`z*M^(-1)z >= κ Σ_j |z_j|²/dj.`                             (5)

This weaker correction avoids inversion of an interval Gram matrix while
retaining a provable improvement. It works in infinite dimensions because
the only Gram inversion is finite and B has the stated genuine gap.

For residual columns ri=pi+ei∈E and bounds ||ei||≤δi, Young's inequality
in the positive SEMIDEFINITE T0 form gives, for any η>0 and coefficient z,

`<Σz_i r_i,D^(-1)Σz_i r_i>`
`<= (1+η)<Σz_i p_i,T0 Σz_i p_i>`
` + (1+1/η)κ^(-1)(Σδ_i²)||z||².`                           (6)

The previous source error charge is therefore unchanged. The new correction
is applied to the same nominal continuum residual, without charging its
action error again. T0 need not be strictly positive on the whole ambient
space for Young's inequality to hold.

### 4.1 Exact source evaluation with uncertain log2

Use h=(P0(2x),P2(2x)) for primitive even parity, and
h=(P1(2x),P3(2x)) for odd parity. Their squared norms are (1,1/5) and
(1/3,1/7). They are precisely low moment constraints in E.

For 1/2<b<1, define L_b=(−1/2,1/2−b), C_b=(1/2−b,b−1/2),
R_b=(b−1/2,1/2). Write a=(κ+w0)/(κ(κ+2w0)) and
c=w0/(κ(κ+2w0)). Direct edge-block inversion gives

`B_b^(-1)h = h/(κ+w0)` on C_b,

`B_b^(-1)h(x) = a h(x)+c h(x+b)` on L_b,

`B_b^(-1)h(x) = a h(x)+c h(x−b)` on R_b.                   (7)

For nominal b0 with |b−b0|≤δb and the complete known piecewise-polynomial p,
the independent polynomial integrator evaluates z0=<p,B_b0^(-1)h> exactly.
With Sp≥sup_I|p|, Sh≥sup_I|h| and Sh'≥sup_I|h'|, a valid error is

`|<p,B_b^(-1)h>−z0| <= δb Sp(4 Sh/κ+c Sh').`               (8)

**Proof.** The two moving partition boundaries change classification on
total measure at most 2δb. Each inverse value is bounded by Sh/κ, so the
jump contribution is at most 4δb Sp Sh/κ. Off those sets only the shifted
polynomial changes; the mean-value bound costs c δb Sp Sh' over length at
most one. All shifted arguments stay in I. ∎

The code avoids catastrophic polynomial coefficient estimates for p by
using `sup|p| <= |p(left)| + sqrt((right−left)∫|p'|²)` on each piece;
the square root is rounded outward with integer arithmetic. This is an
analytic uniform bound, not sampled values.

For exact nominal moment vectors zj and errors εji from (8), 0<θ<1 gives
the following all-coefficient Loewner lower for the correction (5):

`C_lower=(1−θ)κ Σ_j z_j z_j*/dj`
`        −(1/θ−1)κ Σ_{j,i} ε_ji²/dj I.`                    (9)

This follows from reverse Young and Cauchy–Schwarz across residual columns.
The newly improved Schur lower is the previous lower plus (1+η)C_lower.
The nominal residual is checked to have all four exact vanishing moments.
No source-dependent projection is inferred from a caller's parity string.

## 5. Fresh source outcome and actual boundary

Executed:

```sh
python scripts/cloud_operator_source_probe.py --output research/2026-10-20/CLOUD_OPERATOR_SOURCE_J8.json
python -m unittest discover -s tests -p test_cloud_operator_transport.py -v
```

Fresh source J8/M80 replay completed; nine focused tests passed. The JSON
records interpreter, source parameters, source/code SHA256 hashes, precise
rational matrices, and execution arguments. Display rounding is downward
in Loewner order: floor entries on a 10^-18 grid and subtract 2·10^-18 I
to cover row sums of rounding error. Sign tests use Fractions.

The additional gain matrices are EXACTLY:

Derivative odd / primitive even:

`10^-18 [[3463996955140, -167747527079],`
`        [-167747527079, 64529071408]].`

Derivative even / primitive odd:

`10^-18 [[21236511115671, 14290598047569],`
`        [14290598047569, 9616958211169]].`

Both have positive leading diagonal and strictly positive determinant.
The resulting sufficient lower diagonals are approximately
(-0.02729078,-0.02694652) and (-0.01237120,-0.01208095).
Both resulting LOWER matrices remain negative definite. This means the
certificate is insufficient, not that the true source has negative energy.
The source retained all original signed channels and no zero coordinates.

The next sharp probe is to replace (5) by the exact 2×2 moment Gram inverse
in each parity, enclosing its dependence on b rigorously, and then compare
at a held-out Gamma depth. This may improve the bound but cannot be promised
to settle its sign. A subsequent positive certificate would concern this
window only; arbitrary-radius positivity would still need a new theorem.

## 6. Independent checks, falsifiers and limits

The mathematical routes are genuinely different in the stated limited sense:

- COT-01 is an abstract quotient/Riesz theorem; COT-03 uses an explicit
  nonclosability sequence, not source numerics.
- COT-06 is constrained variational optimization. Exact finite holdout
  B=diag(2,3), h=(1,1), r=(1,−1) gives ambient 5/6, correction 1/30,
  and constrained 4/5, agreeing with direct restriction to (1,−1).
- The new polynomial integrator uses independent binomial coefficients and
  antiderivatives. Exact pointwise tests recover B_b B_b^(-1)h=h on rational
  edge/center holdouts. Exact shifted pairings test (8) at b0±δb.
- Nonhigh residuals and inexact floating parameters are rejected. Positive
  source gains are checked by exact 2×2 principal minors, not floating spectra.
- A separate cloud referee reviewed (3)–(9), including the moving-boundary
  estimate and correlated-column penalty, and found no flaw. This is same-model
  methodological review, not independent external provenance or a kernel proof.
  The referee did not independently recompute the whole Gamma source.

The inherited source integration, trial selection, all-high Bessel theorem,
parameter intervals and previous action-error budgets remain shared
dependencies. This lane independently derives the additional correction;
it does not independently reimplement every inherited interval primitive.

| Claim | Status | Boundary / next falsifier |
|---|---|---|
| COT-01 completion transport | CLASSICAL / PROVED PAPER | Kernel descent, primitive closability, source core required |
| COT-02 omitted kernel descent | REFUTED | R² exact witness |
| COT-03 original closedness implies primitive closability | REFUTED | Explicit ℓ² sequence |
| COT-04 L²-dense positivity identifies closed source extension | REFUTED | H¹ Robin boundary form, constant negative test |
| COT-05 compact derivative and primitive gap coexist | CLASSICAL / exact diagonal control | Does not prove a source gap |
| COT-06 constrained inverse and moment correction | CLASSICAL / PROVED PAPER | B bounded SA and genuinely coercive |
| COT-07 paid source gain at J8/M80 | PROVED PAPER + EXACT RATIONAL INSTANCE | Shared source dependencies; no S4 sign |
| Source module was one of 72 imported files | REFUTED provenance sentence | Git introduction and manifest absence |
| Full signed S4 positivity / RH | OPEN | Need positive actual signed-source lower; all-radius gap remains |

## 7. Literature, novelty and integration

Primary literature inspected:

1. [Suzuki, *Weil's quadratic form via the screw function*, v3](https://arxiv.org/html/2606.09096v3),
   Theorem 1.1, equation (1.3), §§8.4–8.5. Maps the source to the correct
   closed primitive realization and distinguishes two Rayleigh denominators.
2. [Douglas, *On majorization, factorization, and range inclusion of operators
   on Hilbert space* (1966), Theorem 1](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf).
   For bounded operators, range inclusion, positive majorization and bounded
   factorization are equivalent. Its unbounded theorem has additional domain
   hypotheses; it is not a license to ignore the completion above.
3. [Anderson–Trapp, *Shorted Operators. II* (1975)](https://doi.org/10.1137/0128007).
   The publisher's abstract verifies the classical Hilbert-space shorting
   context. The full paper was not used as an unchecked proof dependency;
   the exact constrained identity needed here was proved in §4.

The original source-specific Schur machinery, the new correction, and the
classical operator literature are three different provenance layers. This
package supplies a new-to-project quantitative correction and explicit
countermodels, not a claim to have invented Schur complements or Friedrichs
extensions. Merge independently from pinned main after review; it touches no
Claude-owned file. Its executable source probe depends on existing main's
source adapters, and its documentation should eventually be linked by the
coordinator rather than by simultaneous edits to common indices.
