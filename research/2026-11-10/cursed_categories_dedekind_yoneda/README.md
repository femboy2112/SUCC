# SUCC Cursed Categories III — the Dedekind–Yoneda irrational computation graph

**2026-11-10. Research-only additive dossier.** Earlier cursed rounds reconstructed and corrected in `ROUNDS_I_II.md`. This round: `CUT_YONEDA_THEOREMS.md`, `COMPUTATION_GRAPH.md`, `HOSTILE_GATES.md`, `cut_graph.py`, `test_cut_graph.py`, `test_cursed_rounds.py`, `VALIDATION.md`.

## The obnoxiously small object

Let `Q_<=` be the poset category of rational numbers, and let `Irr_<=` be the full subcategory of real numbers with **irrational objects only**. To each irrational `x` assign the contravariant rational-probe functor

`F_x(q) = {*} if q<x, and empty otherwise`.

These are subterminal presheaves. Natural transformations are exactly inclusions of lower cuts:

`Nat(F_x,F_y) ~= Hom_Irr(x,y)` (one element precisely when `x<=y`).

The image is the full subcategory of **nonempty proper lower presheaves** with no greatest lower element and whose rational complement has no least element. It is **isomorphic as a poset category** to `Irr_<=`. The category of elements of each `F_x` is the directed rational computation graph `{q in Q : q<x}`. Its supremum in the completed real order is `x`.

The one-object category with rational-positive affine arrows `(a,b)` acts on those cuts via `x -> ax+b`. An irrational `x` has trivial stabilizer; hence its action groupoid has unique arrows between two objects in one rational-affine orbit. This is **not** the order category, and the whole action groupoid does not encode order automatically. The two structures assemble into coherent order/affine squares (details in the theorem dossier).

For `x=pi/16` the original signed four-pole BBP forcing provides exact, nested rational intervals. A finite certificate can decide any rational comparison `q<x` (because `x` is irrational), compute any fixed radix-16 prefix, and traverse the unimodular Stern–Brocot tree. These are *finite computability/representation* theorems, **not** statistics or normality results.

## New computation pathways

1. **Rational Yoneda necromancy:** one irrational is an entire filtered category of rational arrows; recovering the cut recovers the irrational exactly.
2. **Two-arrow irrational compiler:** finite words in `L,R` give Farey-neighbor rational brackets; infinite, non-eventually-constant Stern–Brocot paths recover all positive irrationals (classical); 2x2 unimodular matrices carry exact denominators.
3. **Numeric affine groupoid:** rational pairs `(a>0,b)` are arrows `x -> ax+b`; composition is `(a,b)(c,d)=(ac,ad+b)`; inverse reindexes every rational cut probe.
4. **Radix as a labeled partial functor:** the global `x -> {16x}` is not order-preserving, so it is NOT a functor on `Irr_<=`; on each open digit branch `d/16<x<(d+1)/16`, the map `x->16x-d` is an order-isomorphism onto irrational `(0,1)`.
5. **Integer carry as a cocycle:** `k_n=floor(16^n x)`, `k_(n+1)=16 k_n+d_n`; the rational-query representation of the new phase is `q<theta_n iff (q+k_n)/16^n < x`.
6. **Finite-pinbed impossibility:** for every finite family of rational membership probes, distinct irrationals share the complete answer vector. Even normal and nonnormal irrationals can inhabit a common finite-probe cell. Thus finite cut evidence does not prove a distribution theorem.
7. **The arithmetic hydra:** the divisor-category/Yoneda/prime-valuation machinery from the prior round becomes the rational/natural semantic substrate for number-valued arrows and sound interval witnesses.

## Scope, CI, and source safety

- All files are additive. No frozen BBP code, provenance import, Lean, workflow, default branch, historical dossier, or existing research file is changed.
- Pure Python `Fraction` + `math.isqrt`; no dependency changes or numerical `pi` oracle.
- Local focused exact-rational tests: **14 passed**; see `VALIDATION.md` for exact scope and retained initial test errors. Do not infer full SUCC suite/CI/Lean passes.
- `pi` normality, selected parity balance, signed original-zero contraction, and RH: **OPEN**.
- A hostile `s=-pi/16` completed-zero seed is rational, and therefore **leaves the irrational-only subcategory**. Sound adversarial comparisons must take place in the full real-cut category as well.

## Related SUCC drafts

- [Main XXIII #584](https://github.com/femboy2112/SUCC/pull/584): source/seed/prime/Archimedean boundary.
- [Lambda–Haar #591](https://github.com/femboy2112/SUCC/pull/591): compiler and signed-overlap obstruction.
- [Seed microscope #592](https://github.com/femboy2112/SUCC/pull/592): coarse cylinder averaging versus zero-selected phase.
- [2→3 joining #593](https://github.com/femboy2112/SUCC/pull/593): normal margins can hide locked joint correlations.

Read `HOSTILE_GATES.md` before using any of this for normality.
