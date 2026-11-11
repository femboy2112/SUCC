# Dedekind–Yoneda: exact category definitions, theorems, and boundaries

**Status:** PROVED PAPER for the specified classical/categorical constructions, except clearly marked conjectural interfaces. `test_cut_graph.py` is independent finite calibration, not kernel-checked proof. No scholarly novelty or global arithmetic conclusions are claimed.

## CY-01. What counts as an irrational cut

Use classical set theory. Let `Q` be the linearly ordered set of rationals. Let `Q_<=` be its thin category: there is exactly one arrow `q -> r` if `q<=r`. Let `Irr_<=` be the thin full subcategory of `(R,<=)` on irrational objects. These are distinct categories: the irrational category has uncountably many objects and no terminal or initial object, and is **not a CCC**. It is not equivalent to the rational poset category.

A lower cut `L subset Q` is irrational precisely when:

1. `L` is nonempty and proper;
2. it is downward-closed (`q<=r in L => q in L`);
3. it has no greatest element (roundedness);
4. its complement `Q\\L` has no least element.

For each irrational `x` set `L_x={q in Q: q<x}`. Conversely, for a cut with these properties take `x=sup_R L`. Boundedness above and below follow from properness and nonemptiness; density of rationals shows `L=L_x`. If `x in Q`, its lower complement would have least element `x`, contradicting (4), so `x` is irrational. This gives a *bijection* of irrational cuts and irrational reals. Condition (4) is essential: `L={q:q<0}` satisfies (1–3) but represents rational zero.

A two-sided locatedness condition is redundant classically under these hypotheses; in constructive settings it must be stated and handled separately. We make **no constructive-equivalence claim**.

## CY-02. Restricted Yoneda via subterminal rational presheaves

Define a functor `F_x:Q_<=^op -> Set` by `F_x(q)={*}` if `q<x`, otherwise empty. The functor maps every rational arrow `q<=r` to the unique allowed restriction `F_x(r)->F_x(q)`; this is well-defined because the cut is lower.

There is a natural transformation `F_x => F_y` iff `L_x subset L_y`. For nonempty/empty singleton-valued functors, the transformation is unique wherever it exists. Rational density gives `L_x subset L_y iff x<=y`. Hence the assignment

`N: Irr_<= -> [Q_<=^op,Set], x |-> F_x`

is fully faithful. Its essential image is the full subcategory of subterminal presheaves whose support is an irrational cut as in CY-01. Restricting the codomain to that image is a category isomorphism up to the set-level identification of `x` and its support. This is **restricted Yoneda**, not the claim that irrational `x` is an object of `Q` or that `F_x` is representable *inside the rational category*.

**Proof of rational probe sufficiency:** if `x<y`, density gives a rational `q` strictly between them. Then `F_y(q)={*}` and `F_x(q)=empty`, so `F_x,F_y` are distinguishable. No finite subfamily of probes is sufficient for all irrationals (see HOSTILE_GATES).

## CY-03. The computation graph of a cut

The category of elements `El(F_x)` has objects rational witnesses `q<x`, with one arrow `q->r` when `q<=r<x`. It is nonempty and filtered: two witnesses admit the common upper bound `max(q,r)` still below `x`, and parallel arrows coincide in a poset. The forgetful diagram `El(F_x)->Q_<=->R_<=` has colimit `sup_{q<x} q=x` in `R_<=`. No finite object of that diagram need equal `x`. In `Q_<=` the colimit generally does not exist, so the completion matters.

This is the precise interpretation of a *number turning into a coherent category of rational computational forms*. The diagram is countable but may lack an effective enumeration of its **memberships** when `x` is noncomputable. Countability of rational nodes is not computability of the cut.

## CY-04. Rational affine arrows and order squares

Let `Aff_Q^+={(a,b):a in Q, a>0, b in Q}` under `(a,b) circ (c,d)=(ac,ad+b)` (right map applied first). The unit is `(1,0)` and inverse `(1/a,-b/a)`. It acts on irrationals by `A_(a,b)(x)=ax+b`; irrationality is preserved by positive rational scaling and rational translation. Every action map is an order automorphism.

On rational cut probes, define `A_(a,b)*F_x` by

`(A_(a,b)*F_x)(q) = F_x((q-b)/a)`.

For irrational `x`, this equals `F_(ax+b)(q)` exactly. Reindexing commutes with the order natural transformations: `x<=y` implies `ax+b<=ay+b`. This is a genuinely commuting square of functors, not a numerical phase equivalence.

The action groupoid `Aff_Q^+ ⋉ Irr` has objects irrational cuts and numerical arrows `(a,b):x->ax+b`. It is **not** equivalent to `Irr_<=` (one has invertible horizontal action arrows, the other noninvertible order arrows). Each action orbit is countable; its stabilizer is trivial: if `ax+b=x`, then `(a-1)x=-b`, forcing `a=1,b=0` since `x` is irrational. Thus the action groupoid is an equivalence-relation groupoid with one arrow between every two objects in one orbit, and is equivalent (noncanonically, after choosing representatives) to the discrete category of affine orbits. This **equivalence forgets numerical source/observer labels**, so it is unsuitable as a standalone authenticated SUCC carrier.

## CY-05. The branch-functor firewall for radix 16

Let `I_d={irrational x:d/16<x<(d+1)/16}`, for `d=0,...,15`. For every `d`, `T_d:I_d -> Irr(0,1)` defined by `T_d(x)=16x-d` is a strictly increasing order-isomorphism, inverse `y|->(d+y)/16`. Its cut reindexing law is

`F_(16x-d)(q)=F_x((q+d)/16)`.

On the disjoint union of these *branch charts*, the digit label is retained and all squares commute. The global fractional-part map `T(x)={16x}` is **not** monotone across digit boundaries; it is not an endofunctor of the global ordered irrational category. Suppressing `d` would erase the precise carry and violate the functor hypothesis. All branch endpoints are rational, so they are absent from `Irr`; extending the construction to rational cuts requires explicit boundary conventions.

## CY-06. Integer winding is an affine cocycle

For irrational `x in (0,1)` let `k_n=floor(16^n x)`, `theta_n=16^n x-k_n in (0,1)`, `d_n=floor(16 theta_n)`. Then

`k_0=0`, `k_(n+1)=16 k_n+d_n`, `k_n=sum_(j=0)^(n-1)16^(n-1-j)d_j`.

These follow from the elementary floor identity `floor(16(k_n+theta_n))=16 k_n+floor(16 theta_n)`. The numerical affine arrow `(16^n,-k_n)` carries `x` to `theta_n`; composition along digit branches yields the same arrow as the concatenated digit word. Under restricted Yoneda:

`F_(theta_n)(q)=F_x((q+k_n)/16^n)`.

This faithfully retains the rational cut and complete *integer winding*. It says nothing about the asymptotic distribution of `theta_n`.

## CY-07. Irrational-only is not closed under ordinary arithmetic

For irrational `x`, positive rational affine maps preserve irrationality, but `sqrt(2)*sqrt(2)=2` and `sqrt(2)+(-sqrt(2))=0`. Consequently no total field/ring structure lives inside the irrational-only full subcategory. Correct categorical arithmetic extends to the full real-cut category. The coherent BBP wrong seed `s=-pi/16` maps the completed value `pi/16+s` to rational zero; an irrational-only test suite would **miss the most important hostile control**.

## CY-08. Finite prefixes versus completed proof

If an oracle supplies correct rational open intervals `(l_N,u_N)` with `l_N<x<u_N`, `u_N-l_N->0`, then for each rational `q != x` a finite N separates q from the interval; thus the cut probe `q<x` is eventually decidable. For irrational x this handles *every rational q*. Each radix branch boundary is rational, so any fixed finite digit prefix eventually receives a strict cylinder certificate. This does not decide equality of arbitrary computable reals, compare two general cut oracles with equality, or bound the search depth uniformly across all irrational x.

A symbolic term `Fix(F)` producing approximations still needs a mathematically proved enclosure and boundary condition; ordinary beta-reduction alone does not certify its real value. Separate lambda semantics, source provenance, and asymptotic analysis.
