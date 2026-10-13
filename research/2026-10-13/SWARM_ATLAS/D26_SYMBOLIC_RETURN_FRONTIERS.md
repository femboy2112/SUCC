# D26 — Realized symbolic frontiers and return-depth commutation

Date: 2026-10-13. Frozen parent: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.
Branch: `research/swm-d26-2026-10-13`. Independent first-generation investigation.

## 1. Original question

Can hierarchical observation commute with source evolution or renormalization, while retaining actual itinerary provenance? The faithful steelman permits a stable coarse observer without pretending it knows every microscopic future. The rival stronger reading makes each finite itinerary window autonomous. The discriminators are actual source collisions, boundary itineraries and return clocks. Here κ is mathematical source contact, φ is proof/probe survival, σ is the declared generating map, and ρ is commitment to an attractive hierarchy; none authenticates physical observations.

## 2. Existing mathematical context

[Milnor–Thurston, *On iterated maps of the interval*](https://websites.umich.edu/~kochsc/MilnorThurston.pdf), §§2–4, defines addresses, itineraries and critical kneading data from interval maps. This source dependence precedes SUCC. [Hedlund, 1969](https://link.springer.com/article/10.1007/BF01691062) supplies classical finite-alphabet shift/local-rule context; a block code on whole sequences does not make a finite prefix autonomous. [Procaccia–Thomae–Tresser, 1987](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.35.1884) studies first-return renormalization selected through symbolic dynamics.

Native bearings are `logistic_observer_tree.py`, `chaos_source_quotient.py`, and `misiurewicz_phase_quotient.py`, with their 2026-10-12 dossiers. They share repository lineage, so are not three independent sources. Imported foundations remain frozen: manifest origin `ba075348b7bcc66d938b3e0ca96c26e95bba340a`; native phase originating commit `b9d84bb39594a7b35d214288ca914e516f23660e`. No imported theorem or runtime changes.

## 3. Proposed SUCC objects

Let α be the root in `(3,4)` of `α³−2α²−4α−8=0` (derivative `(3r+2)(r−2)>0` there), and `f(x)=αx(1−x)`. Put `a=1/α`, `c=1/2`, `z=1−1/α`, `q=α/4`, `J=[a,q]`, `H=[a,z]`. Delete every preimage of `{a,c,z,q}` to obtain forward-invariant `J*`; set `R=H∩J*`. Cells are `A=(a,c)`, `B=(c,z)`, `C=(z,q)`.

Define `F=f²|R`, return itinerary `I_R(x)_j=A/B` according to `F^j(x)`, and `Q_m(x)=I_R(x)[0:m]`. Observation depth is the number `m` of retained return symbols; source depth counts actual applications of `f`. Define `Σ_R=I_R(R)`, explicitly the realized image, rather than an invented tape space. I_R is a model object, not infinitely elapsed evidence.

## 4. Candidate theorem

**CLASSICAL / PROVED LOCAL, conditional exact source theorem.** Every finite A/B word has an actual source in R. For every `x∈R`, `n≥0`, `m≥1`,

`I_R(F^n x)=shift^n I_R(x)`,

`Q_m(f^(2n)x)=drop_n Q_(m+n)(x)`.

Truncation from depth `m+n` to `m` is coherent with further truncations. Thus two source steps per return step commute with observation only through the required buffer. The complete original-cell report through source time `2(n+m−1)` suffices by reading its even positions. This is sufficiency, not a universal minimal sensor-cost bound.

There is no autonomous function `G_m` with `Q_m F=G_m Q_m` for every source in R. Whole-itinerary equivariance and finite-window autonomy are distinct claims.

## 5. Proof attempt

Exact cubic reduction gives `c→q→a→z→z`; ordering gives `a<c<z<q`. Monotonicity then yields complete images `f(A)=C`, `f(B)=C`, `f(C)=(a,z)`. Consequently F has two monotone full branches from A and B onto `(a,z)`.

Repeated branch inverses pull an interior terminal interval back to a nonempty open cylinder for each finite return word. Removing countably many boundary preimages still leaves sources in R. Appending either next letter proves the autonomy obstruction for every m: equal m-prefixes can have distinct successor windows. The two displayed identities follow directly by indexing actual iterates. Their coherence is associative deletion of prefixes, not a stochastic averaging claim.

Concrete source witnesses are `3/10` and `2/5`: exact replay gives `ACB` and `ACA`. They also belong to J* for all future times. The defining cubic has no root modulo 5. In `S=Z[α,1/2]`, α is a unit modulo 5 because `αa=1`. Writing either initial point as `N/5`, with N a unit modulo 5, iteration preserves numerator invertibility modulo 5 while doubling the denominator exponent. Every excluded boundary belongs to S, so no iterate equals one. This supplies the otherwise missing infinite-domain witness obligation.

## 6. Crucible

**Boundary mutation:** z is fixed, so an everywhere-defined phase flip would require `phase(z)=1−phase(z)`. Receipt: exact `f(z)=z`.

**Illegal kneading/support mutation:** `AA` is not an original-cell itinerary, since `f(A)=C`. At `r=2`, the post-image carrier `[0,1/2]` has no strict right-half sources. Abstract binary labels cannot repair either missing realization.

**Wrong-source mutation:** `ACA` is graph-legal but is not the three-event itinerary of declared source `3/10`; independent replay gives `ACB`.

**Infinite ghost:** all finite `B^N` words are realized, but `B^∞∉Σ_R`. Write

`F(x)−x=−αx(x−z)[α²x²−α(α+1)x+(α+1)]`.

The bracket is convex and negative at both c and z: its values are `1+α/2−α²/4<0` and `3−α<0`. Thus `F(x)<x` on B. An orbit staying in B would decrease to a fixed point in `[c,z)`, where this factorization excludes one. Its closed return cylinders intersect only at excluded z. Finite language agreement cannot establish realized infinite-image equality. Indeed Σ_R is forward shift-invariant and dense in the full binary shift but not closed, so it is not that shift of finite type.

**Clock mutation:** for full tent T and section `(0,1/2)`, sources `1/10` and `2/5` have first-return times 1 and 2. Replacing both with `T²` gives the wrong first return for `1/10`.

## 7. Verdict

**SURVIVES:** the source-indexed return square and full finite return language, **CLASSICAL / PROVED LOCAL**. **REFUTED:** universal finite-window autonomy, unrestricted phase flipping, abstract-language substitution for actual source itineraries, and fixed-clock induction without constant-return hypotheses. The independent probe is **TESTED MODEL** evidence for its bounded cases; the universal conclusions rest on the written proofs. There is no Lean-kernel certification, academic novelty claim, measured carrier, invariant-density identification, or RH consequence.

## 8. Remaining obstruction

The smallest unresolved generalization is a source-certified variable return-time cocycle with finite-resolution boundary errors. For first-return map `F(x)=f^{τ(x)}(x)`, the lawful accumulated source clock is `S_n(x)=Σ_(j<n)τ(F^j x)`, not `2n`. A general finite-state observer must preserve enough information to recover this clock and its future report. Test a pair with equal observer reports and unequal necessary return clocks before promoting that extension.

## 9. Cross-domain connection with actual maps

H is a period-two restrictive interval: its interior and `f(H)` are disjoint, `f²(H)=H`, and `f²(∂H)⊆∂H`. With affine `ℓ(x)=(x−a)/(z−a)`, the rescaled return map is exactly `g=ℓ∘f²∘ℓ⁻¹`; hence `g^nℓ=ℓf^(2n)`. Symbolic return coding transports along ℓ without changing realized-source fibers. This is an explicit renormalization square, not a claim that every parameter admits it.

The source-proof connection is equally literal: a predicate `t:R→V` is recoverable from Q_m iff it is constant on each Q_m-fiber. Buffering repairs one future window; it need not recover the original microscopic identity.

## 10. Deliverables

`D26_probe.py` uses only standard-library exact rationals and independent polynomial long division, with no native imports. `D26_RECEIPT.json` records the source parent, actual logistic witnesses, 254 realized tent words, 1538 depth-square checks and hostile mutations. Generation command: `python research/2026-10-13/SWARM_ATLAS/D26_probe.py > research/2026-10-13/SWARM_ATLAS/D26_RECEIPT.json` (**exit 0**). No full suite, compiler, shared edit, or push was run. Receipt SHA-256: `e038442e3f72dc981f268149fe38269bfc6a45159811d5eff31e6f4ce5f441ce`.
