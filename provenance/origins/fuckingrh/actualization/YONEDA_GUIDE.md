# Finite categorical phenomenology — operational Yoneda prototype

The SUCC actualization engine now contains a **bounded category-theoretic observer**.
This is an implementable, source-auditable interpretation of *what a finite
mathematical observer can distinguish*, not a claim that mathematical truths
come into existence when observed or that RH has been decided.

## CLI

From the repository root (Python 3.10+, standard library only):

```bash
python -m actualization yoneda-demo
python -m actualization local-global-demo
python -m actualization probe-budget --a 6 --b 12 --budget 3
python -m actualization probe-budget --a 6 --b 12 --budget 4
python -m actualization probe-budget --lcm-horizon 10000 --budget 10000
python scripts/audit_actualization.py --output /tmp/yoneda-audit
python scripts/mutate_actualization.py --output /tmp/yoneda-mutations
```

The demos never read zeta-zero data and never produce RH certificates.

## Two genuinely different finite probe categories

**Thin/extensional category:** objects are selected positive integer labels;
there is one arrow `a -> b` precisely when `a | b`. A thin arrow's
observable content is only existence, **not** a leaked codomain ratio. This
restriction was enforced after the first CI run discovered an accidental
information leak. At wavefront 3 the observer contexts are `{1,2,3}`.
The restricted representables of targets 6 and 12 agree at those contexts.
Their first dividing probe that separates them is 4.

**Free path/intensional category:** the observer may construct paths by
multiplying by *integrated* source labels, retaining the entire ordered word.
At wavefront 3, `2` and `3` are integrated. Then

- `Hom_path(1,6)` contains (2,3) and (3,2);
- `Hom_path(1,12)` contains (2,2,3), (2,3,2), (3,2,2).

These targets remain **shadows** until direct SUCC reaches their labels.
Their path structures, however, can already be probed. The path category is
finite because all intermediate labels are within a declared bound and every
generator increases the label. Exceeding the expansion or depth budget raises,
rather than silently certifying absence.

The functor `forget_path_bridge` sends every path to its unique divisibility
arrow. It preserves composition and identities but is **not faithful**.
In particular, the two arrows `1 -> 6` are collapsed.

## Full Yoneda versus restricted Yoneda

For a category C, the full covariant Yoneda embedding is

`a -> Hom_C(-,a)`, with
`Hom_C(a,b) ~= Nat(Hom_C(-,a), Hom_C(-,b))`.

We implement explicit finite natural-transformation enumeration and verify
the identity, not just the number of matches.

But if the observer has only contexts J, the restricted representables
`Hom_C(J(-),a)` need not distinguish objects or morphisms.

**False-arrow test:** in the divisibility category `{1,2,3,6}`,
`Hom(2,3)=empty`, but when the only observer context is `J={1}`, both
restricted representables are singleton and there is ONE natural
transformation between them. That is an *apparent observer morphism*, not a
true global arrow. The full Yoneda test correctly yields ZERO.

The full Yoneda statement is classical; the restricted counterexample is an
explicit demonstration of why probe-budget claims require a declared context.

## Source-derived categorical transport — and its limits

Unique factorization builds a finite checked functor from the divisibility
poset to the formal logarithmic valuation category:

`n -> ((p, v_p(n)))`.

An arrow `a -> b` carries the prime-exponent difference
`v_p(b)-v_p(a)`, satisfying the additive degree law under composition.
The functor is FULL AND FAITHFUL on its finite image. Replacing the formal
`log(2)` label by an unrelated prime label fails the graded-arrow check.

This is a source-defined transport from multiplicative coordinates to formal
additive `sum v_p(n) log p` coordinates. **It is NOT an equivalence of Q_p
and R**, does not build Gamma, and does not supply Weil positivity.

A bridge is not free data. Given an actual checked functor F:C->D, we build
the companion profunctor

`B(c,d)=Hom_D(F(c),d)`.

Its source and target actions are checked for identities, composition and
interchange. The finite co-Yoneda calculation

`int^c Hom_C(a,c) x B(c,d) ~= B(a,d)`

is implemented as an explicit **quotient of composable witness pairs**.
The quotient identifies `(k∘f,h)` with `(f,h∘F(k))`.
For the two-prime path-category/forgetful bridge from object 1 to 6, five
raw witness pairs reduce to one target arrow. The four lost distinctions
are *measured information loss*, not spurious primality or global geometry.

A bridge that has the wrong naturality or discards the quotient identifications
fails the finite tests. A bridge may satisfy all these axioms and remain
arithmetically/RH-inert; companion coherence is automatic from an honest F.

## Budget certificates, not unbounded oracles

`ValuationWord` stores genuine finite prime exponents without computing the
possibly enormous integer they denote. A `ProbeBudget(B)` declares that the
observer may ask the typed divisibility queries `j|n` for `1<=j<=B`.

**Sharp theorem:**

`first_sep(a,b) = min_{p:v_p(a)!=v_p(b)} p^(min(v_p(a),v_p(b))+1)`.

Thus an exact proof can certify that ALL permitted probes fail to distinguish
two targets without literally executing B queries. This is a **deductive
finite proof**, not a claim that all physical observers could execute it.

Examples:

- 6 and 12 are indistinguishable at B=3, distinguished by 4 at B=4.
- 6 and 30 are first distinguished by 5.
- `a=LCM(1..10000)`, `b=2a` are distinct symbolic targets but share
  every divisibility probe at B=10000. Their first witness is 16384.
- `a=2^2048`, `b=2^2047` have the first distinguishing divisor 2^2048,
  although the descriptions and the proof of non-detection at smaller B are
  compact. Neither integer must be constructed as a fully realized worldline.

The operator returns **indistinguishable WITHIN B**, not "equal", "RH true",
"unprovable", or "physically impossible". A resource bound is a declared
operational model, not a universal bound on future mathematics.

## Local observer versus looking-down global model

`compare_local_global(local,global_model,horizon=N)` compares only
integrated source events at labels <=N. It stops before reading any future
source value from the global journal, reconstructs both shadow histories from
the truncated prefix, and reports observation agreement.

Example: local genuine zeta at N=3 and a global source with a future fake
coefficient at n=6 are identical on the declared observation class at N=3.
At N=6 the first differing coefficient becomes observable, while earlier
combinatorial shadow paths can remain unchanged.

This does **not** assert the internal prediction models are equal. The same
observations can coexist with different untested predictions, and the
comparator explicitly reports `internal_model_equality_claimed=False`.
Contexts and probe labels are part of a strict observation unless the caller
explicitly chooses value-only comparison. Arbitrary reversed journals or
mismatched conductor laws are rejected rather than guessed.

## API

```python
from actualization import (run_arithmetic, Phenomenology,
                           ValuationWord, ProbeBudget, compare_observers,
                           DivisibilityCategory, PathCategory,
                           forget_path_bridge, CompanionBridge,
                           co_yoneda_companion)

observer = Phenomenology(run_arithmetic(3), max_shadow_target=36)
report = observer.compare(6, 12)
assert report["thin_indistinguishable"]
assert not report["path_indistinguishable"]

cat = PathCategory(range(1, 7), (2, 3))
bridge = CompanionBridge(forget_path_bridge(cat))
transport = co_yoneda_companion(bridge, 1, 6)
assert transport["equivalence_classes"] == 1

a, b = ValuationWord.from_integer(6), ValuationWord.from_integer(12)
assert compare_observers(a, b, ProbeBudget(3)).verdict == "indistinguishable_within_budget"
```

## Mathematical and RH boundary

The RH-bearing target remains the **full completed** Weil pairing
`Q_L=P_L-K_L`. None of these categorical observer constructions has supplied
an arithmetic-to-Archimedean functor into its logarithmic *form domain*, an
exact equality with the Gamma/pole/prime trace, or an independently proved
positive Hodge polarization.

The path and thin probes ignore the true source coefficients: both accept a
fake primitive impulse at 6 unless the separate connected-Euler source audit
is invoked. The characters mod 5 and the Davenport-Heilbronn mixture likewise
require the actual Hecke/source test. A *finite source-faithful Yoneda bridge*
would have to carry this extra data through a genuinely completed pairing,
including forbidden log(6) and log(3/2) mutation controls.

Recommended further experiment: construct a typed, source-derived profunctor
linking a finite Hecke/CRT probe category and an explicitly declared
Archimedean Schwartz/Mellin test category. Prove naturality, preservation of
historical information, and **continuity in the log-Weil form norm**. Falsify
its primitive composite support before testing the completed sign. Do not
choose its fibers or metrics to make the Weil form positive.

## Literature / mathematical provenance

- Tom Leinster, *Basic Category Theory*, §4.3, Yoneda and full faithfulness:
  https://arxiv.org/abs/1612.09375
- Suzuki, *Aspects of the screw function corresponding to the Riemann
  zeta-function*, JLMS 2023, DOI 10.1112/jlms.12785, Theorem 1.7:
  https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12785
- Current project's `wiki/07-methodology-and-discipline.md`,
  `FINITE_ACTUALIZATION_AND_PROBEABILITY.md` and
  `OPERATIONAL_PROBE_MELLIN_FORM_INTERFACE.md`.

All code and tests use the Python standard library. GitHub Actions tests
the committed bytes on two Python versions; see the run/manifest in the
research handoff. External proof of RH remains OPEN.


## A genuine finite/real-circle interface: contravariant clocks

The module actualization/circle_transport.py gives an independent, exact
example of the kind of finite/Archimedean comparison this program needs.

The finite state is Z/mZ with its additive successor. Its dual character
indexed by j has circle phase angle j*k/m modulo 1 for state k. Thus the
finite dual character group embeds as the m-torsion subgroup of the genuine
real Lie circle R/Z, with no floating-point roots of unity.

For m dividing n, define finite projection and dual inclusion

    pi_(n,m)(k mod n) = k mod m
    iota_(m,n)(j mod m) = (n/m) j mod n.

Then the character-pairing identity holds exactly:

    j*pi(k)/m mod 1 = iota(j)*k/n mod 1.

The primal groupoid functor points from the n-clock to the m-clock; the
dual functor points in the OPPOSITE direction. Direct/inverse refinement
towers and the pairing are checked with rational arithmetic. This is an
actual source-defined bridge, not an artificially chosen comparison of
numbers.

At the 2 -> 6 LCM refinement, old dual indices {0,3} embed into
Z/6; the newly accessible indices are {1,2,4,5}, with exact conductor
3 modes {2,4} and conductor 6 modes {1,5}. Their total new dimension 4
agrees with the Haar-conductor innovation rank from the original system.

    python -m actualization circle-demo

In the directed limit this is the classical Pontryagin dual picture:
the dual of profinite Z-hat is discrete Q/Z, realized as torsion points
of the circle. Finite Haar state refinement and dual-character refinement
have reversed arrow directions. The literal continuous circle contains
many more nontorsion points, and the full Archimedean field R has additional
analytic structure. This module supplies neither the real Gamma local
factor nor a canonical positive arithmetic Hodge class. The character
pairing is automatically valid for fake Euler coefficients too, so the
source-connected mutation gate remains separate.

Primary reference: Jordan Bell, The Pontryagin duals of Q/Z and Q and
the adeles, https://jordanbell.info/LaTeX/mathematics/Qdual/Qdual.pdf .


## Endless finite realization and a non-finite representable

The distinction between infinitely many *finite observations* and a mere
large finite aggregate is formalized in
[the Ind-Yoneda construction](../research/2026-10-10/INFINITE_REALIZATION_LIMITS.md).
For C the positive-integer divisibility category, the diagram
L_N=lcm(1,...,N) has each term inside C, but the filtered colimit of
its Yoneda representables is the terminal presheaf, which is NOT h_m for
any finite m (query m+1 is an immediate counterexample).
This is the first exact prototype in which the infinite realization
is meaningful and no finite stage is the global object.

**A direction correction:** Yoneda restrictions across finite observer
categories form an inverse compatibility problem for fixed X,Y.
The L_N objects themselves form a *directed diagram*, so their limit
in the ind-completion is a filtered COLIMIT of representables, not an
inverse limit of the changing objects.

Executable bounded witness:
python scripts/infinite_realization_demo.py --stage 12 --terms 12

The bridge into real-valued analysis is demonstrated separately by
certified rational intervals for pi, e and the Euler-region zeta function.
Neither the ind-object nor finite restricted Yoneda yet constructs an
arithmetic-to-Gamma/Weil polarization. A valid RH transfer needs that
additional source-sensitive, form-topological theorem.


## The scalar quotient is not a path functor

The positive-half-plane finite Euler paths Z_P(2u) and Z_P(2)^u
have equal evaluated values at u=1, but their analytic first jets
differ. Identifying them after point-evaluation is a deliberately
NONFAITHFUL observation: it erases a source- and displacement-sensitive
piece of data. This is NOT a claim that ordinary scalar cancellation
is invalid or that prime multiplication itself is noncommutative.

The finite Gamma successor approximants G_N(z) obey
G_N(z+1)/G_N(z)=Nz/(N+z+1), not z, at each finite horizon,
although the canonical Gamma recurrence is recovered in the limit.
The exact factorial SUCC word, prime valuation ledger, and boundary
defect are retained separately.

Detailed theorem and controls:
[SUCC/Gamma prime-path germs](../research/2026-10-10/SUCC_GAMMA_PRIME_PATH_GERMS.md).
This is a scalar analytic-germ bridge inside Re(u)>1/2, **not**
a functor into the complete Weil form domain and not an RH proof.


## Complete SUCC-shadow probes select, incomplete windows can remain blind

The new [shadow-window theorem](../research/2026-10-10/SUCC_SHADOW_WINDOW_CANONICAL_SELECTION.md)
realizes the canonical Gamma solution via the infinite family of
finite curvature probes W_(n,θ,h). A finite integer orbit by itself
cannot distinguish periodic gauge deformations, but fractional
window measurements can. Their SUCC limit leaves only the periodic
defect as the Gamma curvature vanishes.

**Hostile example:** a continuous periodic function with strictly
positive curvature inside each integer cell can have downward
derivative jumps at every integer boundary. No number of
inside-cell-only probes detects the failure of global convexity;
boundary-crossing shadow probes do. Thus probe-category completeness
is essential, and no claim that "infinity automatically solves
normalization" survives the control.

Multivalued complex log is distinct: the obstruction is winding
monodromy around 0, not a 1-periodic positive Gamma gauge.
Gluing- and reversal-preserving scalar weights on integer winding
classes cannot suppress nonzero winding while remaining positive,
symmetric, and multiplicative. None of this proves the completed
Weil-form sign required for RH.


## Lambert-W inverse charts versus categorical shadow paths

The [Lambert-SUCC construction](../research/2026-10-10/LAMBERT_SUCC_INVERSE_TREE.md)
exhibits two different ways SUCC, Gamma, and an infinite analytic
completion meet. Inverting x(log x-1) with W recovers a useful
**continuous rank guess**; independent exact factorial SUCC replay
supplies the integer certificate and its prime valuation provenance.
Neither W's value nor the scalar mass contains all possible ordered
multiplication histories.

In a separate FULL path category, rooted labeled trees are
\`X * SET(T)\`, so finite combinatorial coefficients
\`t_n=n^(n-1)/n!\` reconstruct the analytic series
\`T=-W_0(-z)\`. The alternative W_-1 branch solves the same
implicit scalar equation but cannot arise from the power series
at z=0. An incomplete "new vertex is always a leaf" successor
functor misses genuine trees at every stage.

This genuine SUCC/shadow branch-selection principle is classical
species combinatorics, NOT a proof that prime-power source dynamics
select the global Weil-positive form. A fake primitive coefficient
at n=6 is not detected by the factorial-W seed, so the construction
does not pass the RH source-mutation criterion.


## Lambert W inside the multiplicative source algebra

Using W on scalar factorial mass was blind to a fake composite impulse,
but the blindness occurs during scalar compression, NOT in W's inverse
formula. The [Dirichlet-star lift](../research/2026-10-10/DIRICHLET_LAMBERT_SOURCE_LIFT.md)
uses the entire labelled multiplicative path space: a normalized
arithmetic source h belongs to the convolution augmentation ideal,
and W_*(h) is the coefficientwise finite solution of
\`w*exp_*(w)=h\`. Its ordered factor-path witnesses recover the
contribution from (2,3) and (3,2) at integer 6.

Under sufficiently strong absolute Dirichlet convergence, the
arithmetic Mellin transform intertwines W_* with scalar W_0.
**This is a genuine finite-to-analytic source-preserving coordinate
transport**, but NOT a preserved Euler product or a Weil positivity
theorem: W_*(zeta-1)(6)=-1, while a fake a(6)=2 makes W_*(h)(6)=0.
The prior connected logarithm b=log_*a must still be used to test
primitive multiplicativity.

This is a positive existence example for source-enriched paths, but
does not close the Gamma/Weil source-to-sign gate required for RH.


## Finite Euler-to-archimedean completion has two distinct seams

The [Hasse/SUCC vs Poisson/Gamma memo]
(../research/2026-10-10/FINITE_SUCC_HASSE_THETA_SEAM.md)
isolates two analytically valid continuations of the true integer
source. One route uses finite integer forward differences to build
eta and zeta; the other uses Gaussian heat sampling, Poisson duality,
and the archimedean Gamma factor to build xi. They match for zeta,
but fake source coefficients need not respect EITHER induced
source-to-target identification. Mirror symmetry alone can be
manufactured for incorrect sources.

At each negative-even trivial zero, the SCALAR SUCC-difference
realization terminates and equals zero, but its first/second
spectral derivatives do not terminate. Gamma's pole extracts the
first jet, and the Gamma-subtracted second-to-first jet quotient
equals a strictly positive Euler prime-power current. This is an
exact *classical* transport, not an RH or Weil sign proof.

The genuine Riemann–Siegel formula already has a square-root
integer observation window and archimedean phase; the essential
remainder and source-identity gate are not optional. New
real-even/reflective polynomial controls have off-line zeros
despite on-critical-line strict positivity.

The next proof-bearing object is a source-derived polarization
on the completed Weil test-function domain, or equivalently a
uniform Jensen-hyperbolicity mechanism. Both are open.


## Coupled arithmetic–archimedean exhaustion and Li coefficients

In the [balanced theta / Li proof memo]
(../research/2026-10-10/BALANCED_THETA_LI_WINDOW.md),
the two infinite limits \`N->infinity\` and \`|u|->infinity\` are
shown to be NON-INTERCHANGEABLE at fixed N. A zero-blind
\`N(u,epsilon)\` from Gaussian erfc tails lets the finite
arithmetic window track archimedean displacement with a
rigorous absolute reflection-defect budget. The half-density
1/2 is the unique exponent supporting the full Poisson
reflection, and fake a(6)=2 survives as a measurable duality
seam in an appropriately displaced window.

The same theta integrals produce finite Li coefficients
through formal logarithmic SUCC reexpansion in
\`w=(s-1)/s\`. A uniform Gaussian bound gives a genuine
zero-free disk near s=1 and a Cauchy error estimate for
every **fixed Li index**. The bound scales like \`r^(-index)\`,
so it offers NO theorem of positivity for all indices.
Finite off-line theta zero collisions coexist with positive
low-order Li-like coefficients; tracking zero motion cannot
replace an independent source-derived Weil/Li sign argument.


### Li-indexed double-limit diagonal: accuracy is not positivity

A constructive \`N(k),T(k)\` finite arithmetic–archimedean
observation schedule now gives **both** an exponentially shrinking
analytic error for the kth true Li coefficient and an
exponentially shrinking Poisson theta reflection error at
the moving window endpoint. The source horizon is linear in k
for simultaneous modular accuracy; it can be square-root in k
for coefficient approximation alone. This quantifier-correct
diagonal realizes infinitely many finite measurements, but
does not prove the coefficients' sign. See §8 of
[BALANCED_THETA_LI_WINDOW.md](../research/2026-10-10/BALANCED_THETA_LI_WINDOW.md).


## General observational SUCC, formal proof-checking and Gödel/Turing

The work has expanded beyond the specific RH source. The
[master dossier](../research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md)
and [wiki 9](../wiki/09-observational-succ-and-computability.md)
give an explicit typed account of the physical Hilbert observer,
the causal history of actual field events, the semantic maps,
finite mathematical proof authority, ordinal omega completion,
and an omega+1 correlation REPORT.

The new observer_logic.py provides a genuine validated and
reversible Gödel syntax codec, alpha-avoiding substitution,
a mathematically correct syntactic diagonal construction and
a fail-closed finite proof checker. It does NOT yet represent the
Gödel substitution graph inside PA. The new observer_reflection.py
makes a substantive ordinal distinction concrete: all finitary
proofs of the omega-union have a computable earliest finite
axiom-support stage. External consistency/reflection is
explicitly typed as an assumption, NEVER inferred from
the mere accumulation of observations.

An exact first-order unary outsider model separates truth
of ALL named finite instances from the universal formula
(no arithmetic/PA structure claimed). A rational-interval
Gram witness API provides negative certificates conditional
on a sound oracle; the certified Suzuki Gamma interval
oracle remains unbuilt. This is genuinely useful
foundational work even if RH stays open.
