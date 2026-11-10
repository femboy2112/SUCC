# SUCC — C-monoid Carrier and Causally Generated Categorical Shadows

**Local, read-only mathematical dossier, 2026-11-09**  
**GitHub status:** No GitHub writes, commits, pushes, issues, or PR modifications.  
**Read baseline:** `femboy2112/SUCC`, `main` at `43a607818907120d4cdab73d240f5b4d7700b63f` (Main XXI). The research PRs discussed below are **not** treated as merged.  
**Methods:** Exact derivation, independent literature checking, and a standalone standard-library `Fraction`/finite-category prototype. Not a Lean proof and not a complete C-monoid implementation.

## Executive verdict

The promising design is **not** a one-object ordinary Cartesian closed category: such a category is necessarily trivial, since its only object is terminal. Instead, take a nontrivial *C-monoid* `M`, the one-object category `BM` underlying it, and Scott's idempotent-splitting construction `K(M)`, which **is** a Cartesian closed category. `BM -> K(M)` is fully faithful. A separate, source-generated tower of diagram/arrow categories gives literal squares and cubes induced by carrier equalities; 2- and higher cells with independent witness content require added proof/enrichment data.

Crucially, the SUCC/FUCC affine relation `V_p S = S^p V_p` is exactly a nontrivial arrow-category square. Coherence for two primes is an exact commuting cube. The frozen BBP source defines a strict functor from the causal time category to rational affine maps, including a source correction cocycle. The initial zero is then a *marked global section*, not an arbitrary orbit-independent property of the underlying monoid. This architecture makes source anchoring and observational loss first-class without proving any unproved asymptotic cancellation.

## 1. Precise categorical firewall

1. **One-object CCC collapse (DISCLOSED).** A CCC must have a terminal object. If its only object is `*`, terminality requires `Hom(*,*)` to be a singleton. The corresponding monoid has only its identity. This rules out the literal proposal but not the intended C-monoid replacement.
2. **C-monoid semantics (classical).** A C-monoid is a monoid supplied with chosen pairing/projections and abstraction/evaluation operations satisfying the algebraic laws for a Cartesian closed structure *except the ordinary one-object terminal requirement*. In established presentations, C-monoids correspond to suitable untyped lambda calculi with products and surjective pairing. Equivalently, `End(U)` is a C-monoid when `U` is a nonterminal object in a CCC with `U×U ≅ U` and `U^U ≅ U`, with the chosen structures appropriately matched.
3. **Karoubi construction (classical, exact).** For a C-monoid `M`:
   - objects of `K(M)` are `e∈M` with `e²=e`;
   - `Hom(e,f) = {a∈M | f a e=a}`;
   - `id_e=e`; composition is multiplication in `M`;
   - `K(M)` is Cartesian closed, and the embedding `BM -> K(M)`, `* ↦ 1_M`, is fully faithful.
4. **Smallest typed jump (classical, interesting).** Rodenburg and van der Linden (1989) proved that every C-monoid admits a CCC with exactly **two objects** `U,T` and `End(U)=M`. A nontrivial typed categorical universe need not first create a large menu of primitive carriers.
5. **What this does not give.** `K(M)` does not automatically provide all quotients, arbitrary subobjects, source-realization maps, an observable Haar theorem, or nontrivial 3-cells. Idempotents are categorical retracts, **not automatically physical subsystems**.

## 2. Causal shadow architecture (new design / conjectural integration)

The base is a designated carrier monoid `M` with a distinguished *admissible source-action submonoid* `A ⊂ M`, a provenance predicate, and initial marked state `z₀`.

```
CARRIER ALGEBRA:       M (one object; C-monoid operations; marked A)
      |                  |
      | BM --> K(M)      | faithful embedding of original endomorphisms
      v                  v
TYPED 1-LEVEL:      K(M) = retracts / typed carrier views
      |
      v
CUBICAL SHADOWS:    Arr(K(M)) = Fun([1], K(M))    (squares)
                    Arr²(K(M))                  (commuting cubes)
                    Fun([1]^n, K(M))             (n-dimensional diagrams)
      |
      v
2-CATEGORY:        a source-generated sub-2-category of Cat
                    (categories, functors, natural transformations)
      |
      v
GENUINE 3+ CELLS:  declared rewriting/proof polygraph with
                    source/target, whiskering, interchange, coherence
```

**Dimension warning.** `Arr^n(C)` is still an ordinary 1-category; it contains n-dimensional commutative *diagrams*. It is **not** by itself an n-category with nontrivial higher cells. The nerve `N(C)` similarly provides an all-dimensional simplicial shadow fully determined by the original 1-category. Genuinely new 2-cells can be (a) source-attested natural transformations/intertwiners, (b) compatible behavioral-order comparisons, or (c) directed rewrite proofs. 3-cells then compare parallel 2-dimensional witnesses; nontrivial n-cells require separately declared coherent generators. Polygraphs/computads are a standard way to generate such towers.

**Nontriviality firewall.** Do not put the noncommuting affine arrows `S,V_p` in the 2-endomorphism set of an *identity 1-arrow*. In a one-object, one-1-arrow strict 2-category, Eckmann–Hilton forces those 2-endomorphisms to commute. Keep the arithmetic arrows at 1-cell level, and put the commuting-square/rewrite witnesses one dimension above.

**Causal-shadow condition (proposal).** For every higher-dimensional cell `c`, require a declared source/target projection down to typed lower-level paths, compatible with all face, degeneracy, and composition operations, plus a provenance check. If a proposed higher cell changes the original source or erases a selected initial condition, it is an *abstract model cell*, not a source-realized causal cell. If a purported nontrivial higher layer follows only by repeated `Arr`/nerve construction, call it an *exact structural shadow*, not new dynamical information.

## 3. First exact SUCC/FUCC 2-dimensional square and 3-dimensional cube

Define the positive affine carrier monoid

`A = {(a,b): a∈N_{>0}, b∈N_0}` with `f_(a,b)(n)=a n+b`.

Composition is `f_(a,b) ◦ f_(c,d) = f_(ac, a d+b)`. Define `S(n)=n+1`, `V_p(n)=pn`. Then, **as actual carrier maps**, for all positive integers `p,k`,

`V_p ◦ S^k = S^(pk) ◦ V_p`.

In the arrow category `Arr(BA)`, an object is a carrier arrow `m∈A`; a morphism `m -> n` is a pair `(a,b)` satisfying `b◦m=n◦a`. Hence the preceding relation is the explicit **commutative square**:

```
     * -------- S^k --------> *
     |                        |
    V_p                      V_p
     |                        |
     v                        v
     * ------- S^(pk) ------> *
```

For primes `p,q`, the two compositions of these squares agree:

`alpha_q(pk) ◦ alpha_p(k) = alpha_p(qk) ◦ alpha_q(k) = alpha_(pq)(k)`.

Here `alpha_p(k) : S^k -> S^(pk)` has both boundary maps `V_p`. The equality gives a commuting 2×2 square **in the arrow category**, equivalently a 3-dimensional commuting **cube in the iterated arrow category `Arr²(BA)`**. It is causal in the precise sense of being built from actual, equal affine functions, and it has no independent cube generator. This identity is algebraic, not a prime-distribution theorem. The primality of p and q is not used in the coherence itself.

**Scope note:** `A` is an affine monoid, *not yet a C-monoid*. A faithful embedding `A -> End(U)` into a genuine C-monoid realization preserving the equality on a selected arithmetic retract remains a construction gate.

## 4. Exact original four-pole BBP source as a functor

Preserve the actual source without mutation:

`r(n)=4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)`, `n>=1`, `U_0=0`, `U_n=16 U_(n-1)+r(n)`.

Let `T` be the causal poset category of nonnegative integer times, with a unique arrow `n→m` for `n≤m`. Set

`R_(n,k) = sum_(j=1)^k 16^(k-j) r(n+j)` and
`F_(n,k)(u) = 16^k u + R_(n,k)` for `k≥0`.

The following is exact for every n,k,l (not only in a fitted range):

`R_(n,k+l)=16^l R_(n,k)+R_(n+k,l)`

and therefore

`F_(n+k,l) ◦ F_(n,k)=F_(n,k+l)`.

**Theorem (DISCLOSED by regrouping).** Sending `n` to `Q` and the time arrow `n→n+k` to `F_(n,k)` defines a functor `F:T→Set`. The source correction `R` is a coherent affine 1-cocycle for concatenated chronological blocks. It is a nonzero, measurable deformation of the homogeneous carrier map `u↦16^k u`, not an arbitrary phase fitted later.

**Pointed-section theorem (DISCLOSED).** A natural transformation `Δ{*}⇒F` is a compatible path `(u_n)` with `u_(n+k)=F_(n,k)(u_n)`. The evaluation map `Nat(Δ{*},F)→Q` at `n=0` is a bijection, with inverse given by the causal recursion. The literal original-zero source is the **marked section corresponding to `u_0=0`**.

This distinguishes three objects that can otherwise get conflated: the source functor, the initial-state selection, and the observed empirical measure on the circle.

## 5. A sharp origin-loss counterexample

Let two source-compatible seeds be `s=0` and `t=1/16`, with identical frozen forcing. Their difference after `n` steps is

`U_n(t)-U_n(s)=16^n (t-s)=16^(n-1)`.

Hence for **every** `n≥1` the two fractional circle observations coincide exactly:

`{U_n(t)}={U_n(0)}`.

But their initial states are distinct. Thus the observation functor "discard time 0, retain later mod-one observations" **cannot reconstruct the original seed**. A pointed history/section can, while an unpointed future circle-law observer cannot. This is a mathematically exact example of `φ`-level indistinguishability coexisting with incomplete `σ`-level source reconstruction.

**Limit:** This particular alias has the same ultimate digit-normality behavior, because the fractional futures actually coincide. It proves **source-identity loss**, not an obstacle to normality itself. Source-dependent nonnormal wrong-seed controls must still be tested separately.

## 6. The hidden coherence requirement for a 2-category of observers

Suppose a restricted observer checks whether two functions agree on a probe set `P`:

`f ~_P g  iff  f(x)=g(x) for all x∈P`.

This can *fail* to define a 2-cell-compatible congruence under carrier composition. Counterexample on carrier `{0,1,2}`:

```
f = (0,1,2)  [identity]
g = (0,0,2)
h = (1,1,1)
P = {0}

f ~_P g, BUT (f∘h)(0)=1 != 0=(g∘h)(0).
```

The failure arises because the carrier move `h` transports the sole probe at 0 to the unobserved site 1. To make this observation equivalence respect *both* composition directions, a sufficient condition is `h(P)⊆P` for every admissible source action `h` (alongside an appropriate common codomain observation convention). Equivalently, use the source-action saturation `P^dyn = ⋃_(h∈A)h(P)`, or a compatible stronger probe completion.

**This is load-bearing for higher categories:** if we use observation equivalences as 2-cells, they must survive whiskering and horizontal composition. Otherwise "equivalent observer models" cease to be coherent after a lawful source action. The source-driven pin-bed probe completion in #541/#543 is therefore a natural candidate for this closure requirement; a specific interoperation theorem still needs proof.

A preordered enrichment `f⇒g` based on a two-sided composition-stable simulation preorder yields a locally preordered 2-category (no nontrivial 3-cells). To obtain proof-sensitive 3-cells, store derivations of each comparison rather than quotienting them to a bare yes/no relation.

## 7. The existing SUCC Haar projector IS a split idempotent

PR #565 contains an especially direct, load-bearing categorical example. Let `T(x)={16x}` act on circle positions, and let `B_a(y)=(a+y)/16` for `a=0,...,15`. On probability measures set

`C nu = (1/16) sum_(a=0)^15 (B_a)_* nu`, `Q=C T_*`.

Then the exact identities are

`T_* C = id`, `Q²=Q`, `C T_*=Q`.

Thus `Q` is a **split idempotent on the probability-law carrier**: the tail law is a retract of the full law space under `T_*` (retraction) and `C` (section). This is precisely the kind of operator from which a Karoubi observer object could be formed *if the chosen C-monoid actually internalizes these law operators*. The retraction does not prove that the source law is `Q`-fixed. For example, `Q(delta_0)` is the uniform grid on `{a/16}`: its first digit is uniform, but its future tail is identically zero, so the law is far from circle Haar.

The open normality estimate is then transparently a **fixed-point defect bound**, such as `W1(mu_A,Q mu_A)->0` with the stationarity/endpoint condition from #565. Idempotent splitting exposes the right type of obstruction; it does not settle the signed arithmetic estimate.

A new exact Fraction probe checked `T_* C=id` and `Q²=Q` on three rational atomic laws and explicitly verified the non-Haar `Q(delta_0)` control.

## 8. The next REAL challenge for π, not a proof by category theory

Under a source-faithful C-monoid realization, write the selected BBP state as a pointed section `z₀`. Probe with the actual character `O_h(u)=exp(2πih{u})` and transport it through the source functor. The needed theorem is still, for each nonzero integer h,

`lim_(A→∞) A^(-1) sum_(n=A)^(2A-1) O_h(F_(0,n)(0)) = 0`.

Categorical internalization can enforce the original-zero section, composition, source signed poles, and observer naturality. It **does not itself imply** the preceding signed cancellation estimate. Current late research targets also include #565 conditional digit Haar, #571 oriented Haar currents, and #574 source-calibrated prime-sign contrast; these are distinct probes and must not be conflated with a source-specific all-epoch estimate.

A genuinely new bridge would be a theorem tying a *higher-cell coherence defect* (from **source-attested** BBP carry/prime transformations) to a signed harmonic cancellation bound. Its null controls must include coherent wrong seeds and periodic/de Bruijn nonnormal orbits. High-dimensional consistency, stable observations, and small regression error alone do not prove Haar.

## 9. Local exact-computation receipt

Run `python succ_cmonoid_local_probe.py`. Standard-library Python only. On this exact file, the test printed:

```
AFFINE: 4 independent (p,q) instances of source/target-square + cube interchange verified
BBP: 100 exact Fraction block-composition equalities verified
SEED: zero and 1/16 seeds have different initial states, identical fractional outputs for n >= 1
OBSERVER: point probe fails congruence; action-closed probe set has 3 states
KAROUBI FINITE PROXY: 27 base maps, 10 idempotent objects, 348 typed morphisms across 100 homsets
HAAR SPLIT: T_* C=id and Q²=Q on 3 exact atomic laws; Q(delta_0) is non-Haar
C-MONOID: NOT implemented; no claim of exponentials/CCC for these finite or affine proxies
```

The 3-state Karoubi proxy uses the **full transformation monoid** on 3 points. It exhaustively checks identity and composition closure for the idempotent-split category; it does **not** construct a C-monoid, because exponentials/pairing are not supplied. Finite enumeration is a validation of the explicitly scoped toy, not proof of the universal categorical theorems.

## 10. Proposed integration acceptance gates (NO repo modification yet)

1. Construct a genuine nontrivial C-monoid with cited axioms, explicit equational checker or formalization, and a certified `U^U ≅ U ≅ U×U` witness, rather than calling any endomorphism monoid a C-monoid.
2. Show a *conservative* faithful arithmetic source representation; distinguish equality on encoded `N` from extensional equality on all untyped carrier values.
3. Preserve the literal BBP four-pole `r`, the zero seed, exact history/carries and source provenance; no moving correction into a fictional seed-independent statement.
4. Implement `Kar(M)` objects/morphisms and test identities/composition/product/exponential laws where the chosen C-monoid model supports them.
5. Implement `Arr(K(M))` squares and iterated cubes, with source faces, interchange, provenance and failure controls. Report clearly which layers are ordinary functor categories and which are genuine higher categories.
6. Require dynamic saturation/congruence of observational 2-cells, and keep source-truth vs observer-indistinguishability typed separately.
7. Try to derive **and falsify** a source-specific higher-cell defect inequality that has an explicit original-zero Weyl/Haar consequence. No asymptotic status promotion without a proof.

## Claim ledger

| Statement | Classification | Boundary |
|---|---|---|
| One-object ordinary CCC is trivial | DISCLOSED | categorical definition of terminal object |
| C-monoid Karoubi envelope is CCC | CORROBORATED CLASSICAL | assumes full C-monoid axioms; literature below |
| Every C-monoid yields a 2-object CCC with matching End(U) | CORROBORATED CLASSICAL | Rodenburg–van der Linden theorem |
| Canonical square/cube from S/Vp affine laws | DISCLOSED | exact affine arithmetic |
| BBP chronological source functor and cocycle | DISCLOSED | original frozen four poles, all n,k,l |
| Seed section selected by u0=0 | DISCLOSED | indexed set-valued functor |
| Future fractional observations lose some seed identity | DISCLOSED | specific zero vs 1/16 example |
| Restricted probe equivalence may fail composition | REFUTED if assumed universally | explicit 3-point countermodel |
| Source-law Haar projection Q is a split idempotent | DISCLOSED | on probability-law carrier, not yet in candidate M |
| Affine monoid is already a C-monoid | UNVERIFIED / NOT CLAIMED | no exponential/pairing axiom provided |
| Full source-faithful C-monoid embedding | CONJECTURED CONSTRUCTION | need genuine model and injectivity proof |
| Genuine higher 3+ categorical source witnesses | CONJECTURED CONSTRUCTION | need coherent polygraph or enrichment |
| Selected π source signed cancellation, base-16 normality | OPEN | no all-epoch estimate derived |

## Sources and repo provenance

- Lambek and Scott, *Introduction to Higher Order Categorical Logic*, §§15–16: C-monoids, Scott's Karoubi theorem, U/T subcategory and reflexive objects. [PDF](https://raw.githubusercontent.com/Mzk-Levi/texts/master/Lambek%20J.%2C%20Scott%20P.J.%20Introduction%20to%20Higher%20Order%20Categorical%20Logic.pdf)
- Pieter Hofstra and Philip Scott, *Aspects of Categorical Recursion Theory*, §4.5, [author-hosted survey](https://www.site.uottawa.ca/~phil/papers/LambekAV.pdf).
- P. H. Rodenburg and F. J. van der Linden, *Manufacturing a Cartesian Closed Category with Exactly Two Objects out of a C-Monoid*, *Studia Logica* 48 (1989), 279–283. DOI [10.1007/BF00370825](https://doi.org/10.1007/BF00370825).
- Arnoud van der Leer, Kobe Wullaert, Benedikt Ahrens, *Scott's Representation Theorem and the Univalent Karoubi Envelope*, ITP 2025, [DOI 10.4230/LIPIcs.ITP.2025.33](https://doi.org/10.4230/LIPIcs.ITP.2025.33).
- Dimitri Ara et al., *Polygraphs: From Rewriting to Higher Categories*, Cambridge University Press (2025), [book chapter](https://doi.org/10.1017/9781009498968.020); [arXiv preprint](https://arxiv.org/abs/2312.00429).
- M. A. Batanin, *The Eckmann–Hilton argument and higher operads*, *Advances in Mathematics* 217 (2008), [DOI 10.1016/j.aim.2007.06.014](https://doi.org/10.1016/j.aim.2007.06.014).
- SUCC main [AGENTS.md](https://github.com/femboy2112/SUCC/blob/main/AGENTS.md), [FOUNDATIONS.md](https://github.com/femboy2112/SUCC/blob/main/docs/FOUNDATIONS.md), [PI_NORMALITY_FRONTIER.md](https://github.com/femboy2112/SUCC/blob/main/docs/PI_NORMALITY_FRONTIER.md). Related research: [#541](https://github.com/femboy2112/SUCC/pull/541), [#543](https://github.com/femboy2112/SUCC/pull/543), [#565](https://github.com/femboy2112/SUCC/pull/565), [#568](https://github.com/femboy2112/SUCC/pull/568), [#571](https://github.com/femboy2112/SUCC/pull/571), [#574](https://github.com/femboy2112/SUCC/pull/574).