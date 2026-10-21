# Exact logistic factor and canonical normality language

Date: 2026-10-21. Parent research head:
`9894d39250021bbbc2615c33dee0d286ddf0950f` (PR #232).
This lane owns `formal/duck_pi/LogisticFactor.lean` and `Normality.lean`.
The mathematics below is classical or an elementary new-to-project
formalization. Academic novelty is not claimed. No normality theorem for pi
is asserted.

**Compiler status at initial commit:** proof candidates await the actual
coordinator-run pinned kernel. Source inspection and a written proof are not
a substitute for compilation. The final campaign receipt must identify the
exact tested source hashes, declarations, axioms and mutation results before
assigning `LEAN_KERNEL_PROVED`. This dossier never installs Python proof
authority by declaration or by a successful receipt supplied by a caller.

## 1. Objects and source identity

The period-one circle is mathlib's `AddCircle (1 : ℝ)`, namely the quotient
of the additive real group by the integer multiples of one. Its `volume`
is the existing Haar measure of total mass one. `circleHaar_total_mass`
checks this normalization against `AddCircle.measure_univ`; no new ad hoc
probability measure or source path is introduced.

Every pi target is explicitly built from **mathlib `Real.pi`**. In the pinned
mathlib revision `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, the definition
is twice a chosen zero of cosine in `[1,2]`. Cosine and sine are the actual
analytic functions, not placeholders. This is the same constant used in
`Real.sin_add_pi`, `Real.sin_two_mul`, the irrationality proof and the Wallis
product. SUCC's rational polygon implementation is not imported as an
alternative definition of pi. A complete formal refinement theorem between
that Python implementation and `Real.pi` remains separate work.

Primary code sources inspected at that exact revision:

- [Trigonometric Basic](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/Analysis/SpecialFunctions/Trigonometric/Basic.lean):
  `Real.pi`, periodicity and trigonometric identities.
- [Inverse trigonometric functions](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/Analysis/SpecialFunctions/Trigonometric/Inverse.lean):
  `Real.sin_arcsin` with both domain inequalities.
- [Additive circle](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/Topology/Instances/AddCircle.lean)
  and [periodic integration](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/MeasureTheory/Integral/Periodic.lean):
  actual quotient, injectivity on a half-open fundamental interval and Haar
  mass, respectively.
- [Pi irrationality](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/Data/Real/Pi/Irrational.lean):
  `irrational_pi` is present. Irrationality is not used as a normality input.
- [Wallis](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/Data/Real/Pi/Wallis.lean):
  `Real.tendsto_prod_pi_div_two` is present. This is a product limit, not a
  digit-distribution theorem.

A search of this pinned tree found no existing normal-number or uniformly
distributed-sequence predicate to reuse. The definitions below are therefore
explicitly local to `ObservationalSUCC.DuckPi`, and no imported Weyl theorem
is invented.

## 2. The circle really has a logistic factor

Define

\[
q_0(t)=\sin^2(\pi t),\qquad D([t])=[2t],\qquad L(x)=4x(1-x).
\]

`logisticLift_periodic` proves `q_0(t+1)=q_0(t)` using
`sin(πt+π)=-sin(πt)`. `Function.Periodic.lift` then constructs the actual
well-defined map `q:ℝ/ℤ→ℝ`. No representative is selected by an unproved
formula. The quotient topology gives continuity.

The double-angle identity and `sin²+cos²=1` yield, for every real t,

\[
q_0(2t)=4\sin^2(\pi t)\cos^2(\pi t)
       =4q_0(t)(1-q_0(t)).
\]

Quotient induction transports this identity to every circle point. Every
value is in `[0,1]`. Conversely, for each `x∈[0,1]`, the actual circle point
represented by `arcsin(sqrt(x))/π` maps to x. The formal proof pays for
`π≠0`, `-1≤sqrt(x)≤1`, and `sqrt(x)^2=x`.

`logisticHatUnit` and `logisticUnit` have the typed codomain
`Set.Icc (0 : ℝ) 1`. The final semiconjugacy is

```lean
Function.Semiconj logisticHatUnit (fun t => t + t) logisticUnit
```

The projection is surjective but not injective: `[1/4]` and `[3/4]` are
distinct in `ℝ/ℤ`, yet `sin(π-π/4)=sin(π/4)`. The quotient inequality is
proved using injectivity of its representatives in `[0,1)`, rather than
silently comparing real representatives.

This produces a genuine continuous onto factor. It does not produce a
conjugacy, a selected orbit's genericity, pi-normality or source ontology.
The orbit `[0]` is exceptional and fixed even though the ambient expanding
system has its classical ergodic properties.

## 3. Digit normality is not defined as the desired Fourier theorem

For a natural base `b≥2`, real x and natural starting index n, the source
orbit is `b^n*x`. For every positive block length k, define its canonical
block code by

\[
B_{b,k,n}(x)=\left\lfloor b^k\{b^n x\}\right\rfloor.
\]

The code is an integer in `[0,b^k)`. Such codes are in bijection with all
length-k base-b words, including leading zeroes. Counting all `0≤n<N`
counts overlapping occurrences; it does not restrict n to multiples of k.
The canonical convention uses half-open cylinders, hence a terminating
expansion at rational endpoints. For example, the zero source has every
block zero. No choice of a second expansion enters the definition.

`NormalTo b x` includes `2≤b` and the exact quantifiers

```text
for every k>0 and every a<b^k,
  blockFrequency(b,k,a,N,x) → (b^k)^(-1) as N→∞.
```

`AbsolutelyNormal x` quantifies independently over every natural `b≥2`.
`PiNormal16`, `PiNormal2`, `PiNormal10` and `PiAbsolutelyNormal` are separate
propositions, all at `Real.pi`; none is asserted as a theorem.

The predicate `UniformDistributionModOne u` independently requests, for
every `0≤a≤c≤1`, convergence of the frequency of `fract(u_n)∈[a,c)` to
`c-a`. `HaarUniformDistribution u` instead uses every continuous real test
function on the actual additive circle and its Haar integral.
`FourierCancellation u` requires convergence of its complex exponential
averages to zero for **every nonzero integer frequency** h. All three
predicates have their own definitions. Their classical equivalences are
not disguised as definitions and are not claimed kernel-proved here.

## 4. A checked-form conditional bridge with a real proof obligation

The load-bearing elementary identity is

\[
B_{b,k,n}(x)=a\quad\Longleftrightarrow\quad
\{b^n x\}\in[a/b^k,(a+1)/b^k).
\]

It follows from the exact floor characterization, positivity of `b^k`, and
ordered division. This is `canonicalBlock_eq_iff`, not an assumption. It
identifies both finite counts, before any limit is taken.

For `a<b^k`, these cylinder endpoints lie in `[0,1]`, and their difference
is exactly `b^(-k)`. Therefore interval equidistribution of `b^n*x` implies
`NormalTo b x`. The instance at x=`Real.pi`, b=16 is a **conditional**
normality theorem. Its unproved equidistribution input remains visibly in
the theorem type.

The opposite claim that every source is normal is contradicted by
`zero_not_normal`: the frequency of the one-digit word 1 in the zero source
is zero, whereas normality would require `1/b>0`. `zero_orbit_not_uniform`
then refutes equidistribution of that orbit. Thus this vocabulary admits
an actual negative theorem and does not make normality vacuous.

## 5. Base-power descent: complete paper proof, formal debt preserved

Here is the precise reason base-16 normality implies base-2 normality. More
generally, let `B=b^r` with integers `b≥2,r≥1`, and suppose x is B-normal in
the canonical digit sense. Fix a base-b word w of length k. Split starting
positions into residue classes `n=rj+s`, `0≤s<r`.

For each fixed s choose `ell=ceil((s+k)/r)`, so the desired k digits are
contained in the first ell base-B digits starting at j. Among the
`B^ell=b^(r*ell)` possible B-word codes, exactly `b^(r*ell-k)` have the
specified k digits in positions s through s+k-1. These codes are disjoint.
B-normality gives every such code limiting frequency `B^(-ell)` along j;
their finite union therefore has frequency `b^(-k)` along that residue
class. This argument respects the terminating convention at rational
endpoints, because grouping canonical base-b digits into r-digit chunks
is the canonical base-B expansion.

There are at most r incomplete positions when the first N base-b starts
are split by residue class. Each class has asymptotic proportion `1/r`.
Adding the r limiting frequencies gives the required overall frequency
`b^(-k)`. Thus B-normality implies b-normality. Put b=2,r=4.

**Status: PAPER_PROVED / CLASSICAL.** The finite chunk-code identity, finite
disjoint union of limits, and interleaving limit are not formalized in
these two Lean files. No theorem declaration falsely asserts this bridge
is already checked. Base 10 is not a power of 2, so this argument supplies
no base-10 implication.

## 6. Hostile controls and the next formal debt

The coordinator should compile the exact files, export their full theorem
types and `#print axioms`, then run the following mutation controls:

1. Change the logistic coefficient from 4 to 3. At `[1/4]`, the commuting
   square would equate 1 with 3/4. The original proof must fail.
2. Replace the canonical half-open upper endpoint by a closed endpoint.
   At a block boundary `y=(a+1)/b^k`, the floor is `a+1`, not a. The exact
   cylinder theorem must fail.
3. Replace every required word frequency `b^(-k)` by 1. The elementary
   interval-width proof must fail for b≥2,k≥1.
4. Try to prove zero-source normality or injectivity of the logistic hat
   from the surviving theorems. The checked negative theorems contradict
   those false targets.

The formal gap to the full requested normality infrastructure consists of
the Haar/interval equivalence, Weyl's criterion, and base-power descent.
These are classical proof imports/formalization tasks. Even after those
are completed, the source-selected global Fourier or interval cancellation
for `Real.pi` remains a separate mathematical pathway gap. The logistic
factor neither closes nor hides it.

## 7. Observed kernel checkpoint and subsequent candidates

The preceding initial-status paragraphs describe the first lane commit.
Hosted [run 39613723244](https://github.com/femboy2112/SUCC/actions/runs/39613723244)
at commit `6fbe9d29355aaccca5ebf2753d34eee2e2ece627` subsequently compiled
both complete files and exported their actual theorem types and axiom lists:
12 declarations from `LogisticFactor.lean` and nine from `Normality.lean`.
Their exact SHA256 hashes were respectively
`f62200a0c866eb8e04aaf990186e927cfa43e349234a2525774d01123d623cf7`
and `240d7503ad05e8346d97c19129be52e3584f91622db540e9fdf44ea402840b62`.
The exported dependencies were confined to `propext`, `Classical.choice`
and `Quot.sound`. The logistic coefficient, canonical endpoint, word-frequency
and exceptional-zero mutations failed with compiling positive controls.

That combined run **failed overall** because the subsequent `WeylBridge.lean`
candidate had elaboration errors. It is evidence for the two successful
modules, not a successful whole-campaign receipt. The coordinator's final
receipt must determine the status of the repaired bridge and later modules.

The subsequent candidates use actual established mathematics, rather than
assuming equivalences:

* `WeylBridge.lean` proves convergence first for genuine circle characters,
  extends it through their dense complex linear span using uniformly bounded
  empirical and Haar functionals, then takes real parts. The density theorem
  is pinned mathlib's `span_fourier_closure_eq_top`.
* `HaarBoundary.lean` constructs empirical probability measures, identifies
  their integrals and finite counts, and invokes the pinned Portmanteau
  theorem for measurable observations with Haar-null frontier.
* `HaarIntervals.lean` constructs the canonical half-open cylinder from
  `AddCircle.equivIco`. Its frontier lies among the cut and two endpoints,
  each of Haar measure zero; quotient integration gives its actual length.
  This supplies the Haar-to-interval implication and, composed with the
  already checked cylinder theorem, a conditional Fourier-to-normality claim.

These three modules are **UNVERIFIED until their exact successful kernel
receipt**. The source-specific Fourier cancellation premise for pi is not
proved by any of them. The base-power descent in section 5 remains a paper
proof rather than a Lean declaration.
