# A circle-and-line observer that emits an infinite L/R name of pi

**Date:** 2026-11-11, UTC. **Status:** CLASSICAL / PROVED LOCAL for
the mathematical statements; TESTED MODEL for the finite checks below. This
is a finite symbolic observer specification. It makes no claim about human
consciousness, an infinite physical execution, radix normality, or RH.

## 1. Hole contract

**Proposed theorem.** There is one finite program, using only integers and
rational arithmetic at runtime, which starts from an explicit Euclidean unit
circle and affine-line construction, emits an infinite Stern–Brocot L/R word,
and supplies certified rational endpoints converging to the circle's
circumference/diameter ratio. Every requested finite prefix is produced after
finitely many arithmetic steps. No pi constant, pi-digit table, BBP partial
sum, trigonometric library call, or comparison oracle is a runtime input.

**Hypotheses.** Ordinary classical real analysis supplies Euclidean arclength
and its change-of-variable rule. The established irrationality of pi is used
to prove that each exact rational branch comparison eventually resolves.
It is not an instruction called by the program. The finite program may use
unbounded integers and unbounded running time/memory as its output grows.

**Weakest sufficient result.** A computable sequence of strict nested rational
enclosures of the geometric ratio, of width tending to zero, plus its
irrationality, suffices to generate the desired L/R word.

**Proof leverage.** The circle/line data determine the actual measure and the
branch decisions. This removes the previous externally supplied BBP pi oracle
from the construction. It provides a second, geometry-derived presentation
of the selected constant with exact comparison certificates.

**Novelty tax.** The arctangent series and the computability of pi are
classical. The local contribution is the explicit typed assembly from
circle–line intersection, pulled-back Euclidean length, rational arc splitting,
certified interval state, and the L/R arrow representation. Computing the
constant does not establish the source-selected signed cancellation theorem.

**Cheapest falsifiers.** Erase the metric factor; change the circle/diameter
scaling inconsistently; reverse an L/R inequality; accept a branch while the
mediant is still inside the enclosure; discard rational endpoint labels; or
claim bounded memory suffices for the exact infinite word.

## 2. What the observer internally means by circle and line

The semantic carrier contains:

- the oriented unit circle C defined by x^2+y^2=1;
- the Euclidean metric ds^2=dx^2+dy^2;
- the points (1,0), (0,1), (-1,0), (0,-1), and the quarter-turn isometry;
- the ordered affine parameter line t;
- the secant line ell_t through (-1,0) with equation y=t(x+1).

These are finite equations and incidence/metric contracts. In particular,
the observer does not treat an arbitrary topological loop as a circle of a
known circumference. The metric is part of the specified object.

Substitution of the line equation into the circle equation gives

$$
x^2+t^2(x+1)^2=1.
$$

One intersection is the fixed point (-1,0). Factoring out that root gives
the other intersection

$$
P(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right).
$$

Every rational t produces a rational point on C. Direct calculation verifies
P(t) lies on C. On 0<=t<=1 this map traverses the first-quadrant arc exactly
once, from (1,0) to (0,1); its inverse there is t=y/(1+x).

### Proposition G1: the metric produces the integration kernel

Differentiating these rational coordinate functions gives

$$
P'(t)=\left(\frac{-4t}{(1+t^2)^2},
\frac{2(1-t^2)}{(1+t^2)^2}\right),
\qquad
\|P'(t)\|^2=\frac4{(1+t^2)^2}.
$$

Hence the pulled-back Euclidean arclength is

$$
ds=\frac{2\,dt}{1+t^2}.
$$

Let gamma be circumference divided by diameter, defined geometrically.
The diameter is 2, and quarter-turn isometries make all four quarter arcs
equal in length. Therefore

$$
\boxed{\gamma=4\int_0^1\frac{dt}{1+t^2}.}
$$

By the usual geometric definition gamma is pi. The derivation does not
assume a numerical pi value or insert one into the observer. It derives the
integrand from the specified circle, line, and metric.

This is where the shapes do actual work. Replacing the integrand by 1 while
retaining the prefactor 4 gives 4 instead of pi. The same rational point graph
without its metric weight therefore fails to determine the intended length.

Scaling the circle to radius r>0 changes the speed to 2r/(1+t^2) and the
diameter to 2r, so the ratio remains gamma. A computation which scales the
circle while retaining diameter 2 violates the semantic contract.

## 3. The 3–4–5 triangle gives a fast rational arc decomposition

Define the positive integral

$$
A(x)=\int_0^x\frac{dt}{1+t^2},\qquad 0\le x\le1.
$$

For a fixed a, the rational fractional-linear change of coordinate

$$
t=\frac{a+u}{1-au}
$$

satisfies, wherever the indicated denominator is nonzero,

$$
\frac{dt}{1+t^2}=\frac{du}{1+u^2}.
$$

This is a direct derivative and denominator identity. For a=1/2, it maps
u=0 to t=1/2 and u=1/3 to t=1. Splitting the integral at t=1/2 gives

$$
A(1)=A(1/2)+A(1/3),
\qquad
\boxed{\gamma=4\bigl(A(1/2)+A(1/3)\bigr).}
$$

There is an equally small circle-group certificate. With complex
multiplication written as an operation on rational coordinate pairs,

$$
P(1/2)=(3/5,4/5),\qquad P(1/3)=(4/5,3/5),
$$

and

$$
P(1/2)P(1/3)=(0,1).
$$

The two rational 3–4–5 points compose to one quarter turn. The integral
change of variables above supplies the arclength statement with the branch
and orientation already fixed. Thus neither a numerical pi value nor
unexplained large Machin constants are required.

The circle-coordinate transformations in this section and the Stern–Brocot
L/R transformations below are different typed operations. The former preserve
the angular differential; the latter refine a rational name of its period.
They must not be silently identified as the same action.

## 4. An exact rational enclosure generator

For n>=1 define the finite rational polynomial

$$
S_n(x)=\sum_{j=0}^{n-1}\frac{(-1)^j x^{2j+1}}{2j+1}.
$$

The finite geometric-series identity, integrated on [0,x], gives

$$
A(x)=S_n(x)+(-1)^n
\int_0^x\frac{t^{2n}}{1+t^2}\,dt.
$$

For 0<x<1 the remainder integral is strictly positive and satisfies

$$
0<\int_0^x\frac{t^{2n}}{1+t^2}\,dt
<\frac{x^{2n+1}}{2n+1}.
$$

This proof gives exact signs and bounds, without evaluating A or gamma.

For m>=1 put

$$
\ell_m=4\bigl(S_{2m}(1/2)+S_{2m}(1/3)\bigr),
$$

$$
u_m=4\bigl(S_{2m-1}(1/2)+S_{2m-1}(1/3)\bigr).
$$

### Proposition G2: strict nested geometry intervals

For every m>=1,

$$
\ell_m<\gamma<u_m,
\qquad
\ell_m<\ell_{m+1}<u_{m+1}<u_m,
$$

and the width is exactly

$$
\boxed{u_m-\ell_m
=\frac4{4m-1}\left(2^{-(4m-1)}+3^{-(4m-1)}\right).}
$$

**Proof.** The remainder sign gives the lower/upper inequalities. Consecutive
even partial sums differ by a positive pair of alternating terms, and
consecutive odd partial sums decrease by a positive difference, since
0<x<1. The width is the single term removed between S_(2m-1) and S_(2m),
summed for x=1/2 and x=1/3. Every assertion is a rational identity or the
stated positive remainder integral. The width tends to zero exponentially.

The first interval is already

$$
\boxed{\frac{505}{162}<\gamma<\frac{10}{3}.}
$$

In particular 3<gamma<4 is derived rather than supplied as an oracle fact.

For a simple explicit accuracy schedule, m=k+1 suffices for width<2^(-k),
for every integer k>=0. Indeed the width is at most

$$
\frac8{4m-1}2^{-(4m-1)},
$$

which at m=k+1 is 2^(-4k)/(4k+3)<2^(-k).

### Finite state schema

The generator needs counters and rational partial sums. Incrementing n adds
the two terms for x=1/2 and x=1/3; powers can themselves be updated by
multiplication by 1/4 and 1/9. Thus a fixed finite instruction list produces
the enclosures. Numerators, denominators, and counters are unbounded in size.
No runtime integral or trigonometric primitive is needed.

## 5. Compose the geometry oracle with the L/R arrow machine

Use a Stern–Brocot interval with positive denominators,

$$
\frac ab<\gamma<\frac cd,
\qquad bc-ad=1.
$$

Initialize (a,b,c,d)=(3,1,4,1), justified by G2. The mediant is

$$
q=\frac{a+c}{b+d}.
$$

Keep a precision counter m, initially 1, and refine it until one of the
following exact rational tests succeeds:

- if u_m<q, output L and replace (c,d) by (a+c,b+d);
- if ell_m>q, output R and replace (a,b) by (a+c,b+d);
- otherwise increment m and try again, emitting no unsupported arrow.

Each emitted arrow retains a certificate: the rational source enclosure,
the mediant, the successful strict inequality, and the updated endpoints.
This is a semantically bound observer: an L/R letter is justified by the
geometry-generated measure, rather than a pi comparison primitive.

In the endpoint-matrix convention

$$
M=\begin{pmatrix}a&c\\b&d\end{pmatrix},
$$

the updates are M -> ML and M -> MR with

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
$$

The letters' matrices have determinant +1; M has determinant -1 under
this column convention.

### Theorem G3: every finite prefix is produced in finite time

**Proof.** At a fixed state, q is rational. The geometric ratio gamma is
pi, and the classical irrationality theorem gives q!=gamma. Since the
strict source intervals shrink to gamma, eventually the whole interval
lies strictly on one side of q. Thus the refinement loop terminates and
emits the next arrow. Induction gives finite termination for every finite
requested prefix. The program never calls the irrationality theorem; that
theorem proves its productivity. No explicit efficient global precision
bound in the prefix length is asserted here.

### Theorem G4: the infinite word recovers the geometric pi

The determinant and strict bracketing are invariant under both updates.
After k arrows the endpoint gap is

$$
\frac cd-\frac ab=\frac1{bd}.
$$

Initially b+d=2. Each update increases b+d by a positive integer, so after
k arrows b+d>=k+2. For positive integers b,d,

$$
bd\ge b+d-1\ge k+1.
$$

Therefore

$$
\boxed{0<\frac cd-\frac ab\le\frac1{k+1}.}
$$

Every interval contains gamma. Their widths tend to zero, so their
intersection is exactly {gamma}={pi}. The width bound is uniform in the
number of emitted arrows. It is not a bound on the arithmetic work needed
to emit those arrows. This proves the requested finite-program/infinite-run
recovery theorem within the stated classical semantics.

## 6. What the algorithm shape tells us, and what remains unpaid

The observer exposes a real structural chain:

1. A line intersecting a quadratic circle gives a rational parametrization.
2. The Euclidean metric pulls back to a rational differential.
3. Circle composition becomes rational fractional-linear coordinate change.
4. A 3–4–5 decomposition moves the integration arguments inside the unit disk.
5. A finite geometric-series identity gives signed rational error certificates.
6. Certified rational comparisons select the L/R arrows.
7. Unimodularity turns the emitted word into an exact limiting number.

Every step has explicit retained structure. The intermediate rational
differential is a concrete new place to compare the geometry presentation
with the authenticated four-pole source presentation. A useful next theorem
would transport a specified observer or signed statistic through that
comparison with a quantitative residual bound.

The universal L/R grammar itself does not single out pi: changing the
certified target changes the branch sequence while preserving both update
matrices and their determinant law. The load-bearing information resides
in the source-bound comparison program and its labels.

The run-length pattern is a continued-fraction presentation. Its existence
does not supply a base-16 digit-frequency estimate. A source-derived bound
on the relevant branch statistics, correlations, or their transported radix
observables remains a separate theorem. Rephrasing that estimate as an
unproved property of the infinite word does not pay the novelty tax.

### Finite program does not mean bounded memory

A deterministic, autonomous machine with only finitely many internal states
has eventually periodic output. An eventually periodic Stern–Brocot L/R word
with both letters in its repeating block has a quadratic irrational limit:
the period matrix fixes that limit by a quadratic fractional-linear equation.
An eventually constant letter gives a rational endpoint. A finite prefix
acts by a rational fractional-linear map and preserves the algebraic degree
bound. Thus such a bounded-state output cannot name transcendental pi.

Our program has finitely many instructions but growing exact integer state.
That distinction is part of the theorem, rather than a hidden infinite
constant inside the implementation.

## 7. Finite constructor checks actually performed

An inline Python 3.12 standard-library calculation was executed during this
constructor bearing. It used fractions.Fraction for all acceptance tests.
It did not write to the repository or modify its implementation.

| Check | Executed scope |
|---|---|
| Circle equation and squared-speed identity | 81 distinct reduced rational parameters in [0,1], denominator at most 16 |
| 3–4–5 circle composition | Exact P(1/2)P(1/3)=(0,1) |
| Geometry enclosure nesting and exact width | m=1,...,40 |
| Independent source comparison | All 40 geometry intervals contain the narrow BBP interval from 100 source terms |
| L/R determinant, bracketing and width | 400 emitted arrows |

The 400-arrow run required geometry level at most 18. Its initial maximal
runs were

```
L^6 R^15 L R^292 L R L R^2 L R^3 L R^14 ...
```

The initial interval is [3,4]; changing the root convention changes the
initial run count. The familiar 355/113 approximation and the long following
run arise from the certified comparisons, not from a stored continued-fraction
table. The final endpoint denominator bit lengths in this finite run were
33 and 39. These observations do not prove any infinite word statistic.

The imported BBP implementation was used only as an independent regression
comparison. It is absent from the observer specification and the proof of G1–G4.
Its source identity and this geometry identity each identify the same real
pi by their own mathematical provenance; interval overlap alone would not
establish equality of two otherwise unidentified limits.

## 8. Primary sources and verdict

- [NIST DLMF 4.24.3](https://dlmf.nist.gov/4.24.E3) records the arctangent power
  series. The signed finite remainder used here is derived directly from the
  finite geometric-series identity, so the runtime certificate is explicit.
- David H. Bailey, [An elementary, self-contained proof that pi is
  transcendental](https://www.davidhbailey.com/dhbpapers/dhb-pi-trans.pdf),
  inspected primary author text dated July 24, 2026. Its Theorem 1 supplies
  a proof of the irrationality used for branch productivity. The stronger
  classical transcendence theorem supports the bounded-state obstruction.
- The governing SUCC AGENTS.md, docs/METHOD.md, and the existing Round III
  computation-graph note were read at the clean checkout rooted at
  `964768cd1fa5116f521625abfaaad8d8fab0f222`. No existing core or source contract
  is modified by this constructor note.

**Steelman:** an observer carrying exact circle/line geometry can derive and
execute the branch rule which names pi, with no pi-value oracle hidden in
the L/R system.

**Crucible:** the metric, source labels, branch inequality, root convention,
and finite-program/unbounded-state boundary are made explicit. The finite
checks compare different arithmetic presentations and preserve their shared
classical dependencies.

**Verdict: SURVIVES, PROVED LOCAL within classical real analysis.** G1–G4
construct the requested observer and prove every finite output prefix is
computable and the infinite name recovers the geometric pi. The additional
statistical implication for the authenticated SUCC orbit remains OPEN.
