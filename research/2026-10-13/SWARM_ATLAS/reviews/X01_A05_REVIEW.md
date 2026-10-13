# Independent A05 adversarial review of X01

**Subject:** `d9631e3008051628a45bd6373ef35e884d3a7384`, `SWARM_ATLAS/X01.md`. **Reviewer base:** `ad6db3cfeb4cd9426b622f31d3d5c2892c3d7d37`. I read the theorem, then reconstructed the proofs and wrote a separate enumeration. I neither read nor imported `X01_probe.py`. This is an independent reasoning/implementation pass, not independent physical evidence or academic priority review.

**Verdict: SURVIVES under its stated hypotheses.** No repair to T1/T2 is required. The repairs below apply to specific attempted relaxations. The principal retains final acceptance authority.

## Independent derivation

For a retained inverse family, its empty-stage coordinate contains an actual receipt e. Every larger coordinate restricts to that same e; its report is therefore the restriction of Ψ(e). This constructs both inverse maps between E and lim D. Empty E gives empty lim D because the empty stage is included. Omitting that stage when W=∅ would instead create a terminal singleton limit, a false witness.

For an image family, the empty stage fixes l. Singleton stages fix a profile z; union stages ensure each finite restriction `(z|F,l)` has a receipt. Conversely this finite matching property constructs the family. With O and L discrete, every neighborhood of `(z,l)` contains the cylinder requiring a finite set of report coordinates and that **exact** label. Thus lim B is closure J(E), while the image of lim D is J(E). Closedness is consequently precisely the image/limit exchange condition. Infinite discrete L poses no difficulty: Y is a disjoint union of label slices, and closedness is equivalent to closedness in every slice.

For cost, put T_F={e:Ψ(e)|F=z|F,λ(e)=l}. Coordinate/label continuity makes T_F closed. If M is finite, for every t>M and finite collection of probe sets, the union constraint has infimum ≤M and hence a witness inside K_t={c≤t}. The closed subsets T_F∩K_t have the finite intersection property, so their intersection is nonempty. Choose t=M+1 first, then include all sublevels K_(M+ε) inside that one compact set. Hausdorffness makes those compact sublevels closed. The resulting receipt satisfies every coordinate and has cost ≤M. Every global receipt has cost ≥M, proving equality and attainment. If M=∞, finite-valued c forbids a global receipt. No infinite experimental execution or computable receipt selector is supplied.

The refinement target consists of pairs `(r,e)` with r|F=Ψ(e)|F. The comparison image consists of the pairs with r=Ψ(e)|G. It is injective because e is retained. Therefore its **exact general criterion** is:

> For every receipt e and every large report r over its small report, r=Ψ(e)|G.

When every A_s is inhabited, every small report is supported, so this is equivalent to injectivity of X_G→X_F. Full inhabitation can be weakened to support of every small report; absent either hypothesis, unsupported noninjective fibers need not obstruct the comparison.

## Directed attacks and exact repairs

1. **Empty receipt fibers conceal report failures.** Let source reports be 00,10,11; only source 00 has a receipt. For F={first bit}, G={both bits}, the restriction 10,11→1 is noninjective, but the receipt comparison is bijective: its supported fiber contains only 00. This refutes the unrestricted T2 equivalence, not the stated inhabited version. Repair: require every small report supported, or use the receipt-relative criterion above. With all fibers empty, the comparison is likewise empty-to-empty and cannot establish coverage.

2. **Non-discrete label topology breaks the closure formula.** Let W=∅, E={e}, L={0,1} indiscrete, λ(e)=0. Then lim B has label 0 only, whereas closure J(E) contains both labels. E is compact and λ continuous. Repair: retain discrete L for the exact finite-cylinder formula; Hausdorffness alone would also be insufficient for that formula (labels 1/n in usual R have a new closure label 0, never admitted at the empty stage).

3. **Discontinuous labels defeat bounded-cost lifting.** Take the compact convergent sequence E=N∪{∞}, reports q_n(k)=1[k≤n], q_n(∞)=0, and c=0. Label finite k by a and ∞ by b in discrete L. Every finite all-zero report with label a has a cost-zero receipt, but no global such receipt exists. All report coordinates are continuous; λ is discontinuous at ∞. Repair: retain label continuity, or, for a fixed target cost theorem, separately prove the matching-label fiber is closed. Compact source labels cannot silently be retopologized as discrete identities: a continuous map from compact E to a discrete label set has finite image.

4. **Compact original S does not imply compact supported E.** Independent alternative: S={0,1}^N, Φ=id, with receipts only for finite-support sequences and constant labels. Supported E is dense and proper. Every finite all-ones report has a receipt supported exactly on those requested coordinates, but the all-ones original source has an empty receipt fiber. Thus lim B=S and image(lim D)=E differ. With cost c(e)=number of ones, each sublevel is compact: sequences with at most n ones form a closed subset of Cantor S and lie wholly in E. Finite all-ones constraints on F have minimum cost |F|, so M=∞ correctly rejects the missing receipt. Setting c=0 would give a uniform cap but noncompact sublevels. Repair: apply compactness/coercivity to **receipt support E**, not merely to S; do not delete empty A_s.

5. **Costs and quantifiers are material.** A singleton receipt of cost ∞ refutes `receipt exists iff M<∞` if extended-valued costs are permitted. Repair: keep finite-valued c, or restrict existence to finite-cost receipts. Caps are profile-specific: E=N discrete, one report coordinate Ψ(k)=k, constant label and c(k)=k have compact finite sublevels and receipts for all profiles, yet no common cap for all profiles. The valid order is `for each (z,l), exists finite cap`, not one cap for all `(z,l)`. Expensive arbitrarily chosen approximants do not refute cheap-witness existence.

6. **Hausdorffness protects attainment.** Take positive integers E with the indiscrete topology, constant reports/labels and c(k)=1/k. Every sublevel is compact in its indiscrete subspace topology, and every finite constraint has infimum 0, but no receipt attains cost 0. Repair: retain Hausdorff E, which makes compact sublevels closed, or explicitly require closed compact sublevels. Compactness alone cannot substitute for that closure step.

## Validation and claim boundary

Run `timeout 30s python research/2026-10-13/SWARM_ATLAS/reviews/X01_A05_probe.py`. Exit 0 is preserved in `X01_A05_receipt.json`, with program/review hashes. The separate probe passed 601 finite models, 5,409 refinement comparisons and 4,808 cost equalities, covering zero receipt multiplicities, labels and actual coherent inverse families. It also checks the three-source unsupported-fiber control, non-discrete finite label countermodel and finite-support cost controls. These checks corroborate finite cases; the infinite and topological claims above rest on the explicit derivations.

[Stacks 086J](https://stacks.math.columbia.edu/tag/086J) confirms the classical finite-nonempty inverse-limit theorem; [Stacks 0AKK](https://stacks.math.columbia.edu/tag/0AKK) supplies an independent warning against general surjective-set compactness. X01 does not misuse either. [Rockafellar–Wets, Theorem 1.9](https://sites.math.washington.edu/~rtr/papers/rtr169-VarAnalysis-RockWets.pdf) concerns Euclidean minimum attainment; the general Hausdorff cost argument here is the direct finite-intersection proof, not an attributed extension of that theorem.

The source-family audit remains mathematical: κ is supplied maps; φ is proof plus a separate finite implementation; σ does not authenticate any physical source, receipt accessibility, topology or resource cost; ρ grants no support. **PROVED LOCAL survives for the abstract theorem.** Physical execution, algorithmic synthesis of receipts, kernel certification and integration suites remain unestablished by this review.
