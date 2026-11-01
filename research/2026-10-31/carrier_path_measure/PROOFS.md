# Carrier-relative path measures: theorem dossier and source obligations

**Research date:** 2026-10-31. **Authority:** classical mathematical derivations and locally tested finite exact models, NOT Lean-kernel or peer-referee authority. **Main baseline:** `e8598cfa5d32fd1de8e94a3e458a366a0850d59e` (Main XVII). **π base-16 normality / RH:** OPEN.

## 0. Proposal, steelman, types

Original conjectural intuition: `||a-b|| = superpos(abs(a-b), carrier)` where superpos is the family of carrier paths with the declared displacement/valuation. We retain its *path-dependent carrier* content without silently declaring a path state to be a real norm. Separate the data:

* A **carrier** `C=(V,E,oriented incidence,c)` with strictly positive conductances `c_e`; optional action labels, a source law, and an observer's admissible readouts.
* A **boundary constraint** `b=δ_target-δ_source ∈ C_0(V)` with zero total mass, and the affine family of unit flows `F_C(b)={j∈R^E : ∂j=b}`. The source and target must be connected.
* A **path state** `S_C(s,t)=Σ_{γ:s→t} w(γ) exp(2πi Φ(γ)) |γ⟩` on a FINITE path set, or on a countable set only after proving summability. `w(γ)≥0`; `Φ(γ)∈R/Z`. No quantum interpretation without a separately specified instrument.
* An **observer map**, e.g. energy minimum, amplitude sum, phase histogram, bounded finite Fourier functional. An observer's scalar result is not automatically a metric or source theorem.

Using *endpoint displacement* to select a family differs from requiring every path to have *length* `|a-b|`; the latter excludes detours and cycle degrees of freedom. If `|a-b|` enters as a primitive, this is a derived construction rather than a foundational derivation of the absolute value. The incidence boundary avoids circularity.

## CRPM-01 — Affine path/flow fiber and cycles (CLASSICAL)

For a connected finite graph with incidence map `∂:R^E→R^V`, and `b=δ_t−δ_s`, choose any `j_0` with `∂j_0=b`. Then

`F_C(b) = j_0 + ker(∂)` and `dim ker(∂)=|E|−|V|+1`.

**Proof.** Subtracting any two elements of `F_C(b)` gives a divergence-free cycle flow; adding any element of `ker ∂` preserves the boundary. For a connected graph, `rank ∂=|V|−1`; rank-nullity proves the dimension. A triangle has one cycle degree of freedom. A line/tree has none. Source and sink are signed boundary loads, not scalar distance.

**Boundary:** A count of virtual paths alone does not identify the source's actualized path or its phase.

## CRPM-02 — Carrier-relative norm and resistance (CLASSICAL, exact finite oracle)

Let `C=diag(c_e)`, `L=∂ C ∂^T`, and `b=δ_t−δ_s`. Set

`R_C(s,t) = min_{∂j=b} Σ_e j_e² / c_e = b^T L^+ b`.

**Proof.** Solve `L φ=b` modulo constants (connectedness). The electrical flow `j*=C∂^Tφ` obeys `∂j*=b`. Any feasible flow `j=j*+k`, `∂k=0`, has

`Σ j_e²/c_e = Σ j*_e²/c_e + Σ k_e²/c_e + 2 <φ,∂k> = R_C(s,t) + Σ k_e²/c_e`.

Thus `j*` uniquely minimizes energy, and `R_C=b^T L^+ b`. Define `d_C(s,t)=sqrt(R_C(s,t))`; it is a genuine metric since `d_C(s,t)=||L^{+1/2}(δ_s−δ_t)||_2`, with distinct vertices distinct in the zero-sum space. Adding an edge with positive conductance cannot increase `R_C`: extend the former minimizing flow by zero on the new edge. **Rayleigh monotonicity.** Unit edges line `0–1–2`: `R(0,2)=2`. Complete triangle: `R(0,2)=2/3`. Exact grounded-Laplacian solver crosschecked against an independently implemented Kirchhoff spanning-tree / separating-two-forest formula.

**Boundary:** Positive energy/Gram data cannot decide the sign of the authentic BBP real-circle Weyl sums. This is classical electrical network theory, reused in a SUCC carrier adapter, NOT a novel resistance theorem.

**Primary/academic provenance:** Lyons–Peres, *Probability on Trees and Networks*, available https://pages.iu.edu/~rdlyons/prbtree/prbtree.html ; Aldous–Fill, *Reversible Markov Chains and Random Walks on Graphs*, https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S7.html ; U. Washington 2025 notes https://courses.cs.washington.edu/courses/cse525/25sp/525-lecture-13.pdf .

## CRPM-03 — Gauge obstruction, phase holonomy and scalar coherence (CLASSICAL; SUCC negative theorem)

On a directed edge `u→v` choose `θ(u,v)∈R/Z`, with reverse orientation `θ(v,u)=−θ(u,v)` when reverses are admitted. For a path `γ`, `Φ(γ)=Σ_{e∈γ} θ(e)`. A gauge transformation `θ'(u,v)=θ(u,v)+g(v)−g(u)` gives

`Φ'(γ)=Φ(γ)+g(t)−g(s)` and `A'_C(s,t)=exp(2πi(g(t)−g(s))) A_C(s,t)`.

In particular `|A_C(s,t)|` is gauge invariant if path weights are gauge invariant. If `θ=dg`, *all* source-to-target paths have the SAME phase and therefore `|A_C(s,t)|=Σ_γ w(γ)`: **no inter-path cancellation can arise from an endpoint-only phase potential.** Conversely, on a connected undirected graph with unrestricted reverse paths, the edge connection is gauge-trivial iff its holonomy around every cycle is trivial (spanning-tree gauge and fundamental cycles). In the Pascal DAG, adjacent transpositions `01↔10` connect all bitpaths with the same `(n,k)`, so flatness of all elementary diamonds is sufficient for directed path independence.

For any finite family of positive weights and phases `z_γ=w_γ e^{iθ_γ}`,

`(Σw_γ)²−|Σz_γ|² = 2 Σ_{γ<η}w_γ w_η(1−cos(θ_γ−θ_η)) ≥ 0`.

This exact **coherence-loss identity** is phase-sensitive and nonnegative, but it does **not** imply a specific selected arithmetic Weyl estimate. It is easy to manufacture nontrivial holonomy by *choosing* phases; the source must authenticate the phases before any π claim.

**Receipt / REFUTED variant:** `θ(u,v)=F(v)−F(u)` can never generate phase cancellation between different paths with fixed endpoints, regardless of how many Pascal paths are summed.

## CRPM-04 — Gaussian-Pascal path interference and exact 16th-root cancellation (CLASSICAL; independently tested)

A path from `(0,0)` to `(n,k)` is a bitword with exactly `k` ones. Let `A(γ)` be the number of zero-before-one pairs in that word. The path polynomial is

`Q_(n,k)(q)=Σ_{γ}q^{A(γ)}`.

Partition by the last bit. Appending `0` changes no `A`; appending `1` creates exactly `n−k` additional zero-before-one pairs. Therefore

`Q_(n,k)=Q_(n−1,k)+q^(n−k) Q_(n−1,k−1)`, `Q_(n,0)=Q_(n,n)=1`.

These are the Gaussian binomial coefficients

`Q_(n,k)(q) = ∏_{j=1}^{k}(1−q^(n−k+j))/(1−q^j)` (as a polynomial identity).

Let `m≥2`, `q` a *primitive m-th root* and `0<k<m`. Every denominator factor is nonzero (`1≤j<m`) and the numerator contains `1−q^m=0`. Hence

`Q_(m,k)(q)=0` for every `1≤k≤m−1`.

In particular at `m=16` all 15 interior path amplitudes vanish identically. For `m=2^a`, the exact minimal polynomial is `Φ_m(q)=q^(m/2)+1`; the `cyclotomic_two_power` implementation reduces integer path coefficients in this quotient, with zero iff the evaluated amplitude at a primitive m-th root is zero. **Independent hostile check:** a second module enumerates all 65,536 length-16 bitwords, groups by `(k,A mod 16)`, and checks equality of antipodal residue counts; no recurrence is shared. The result is true.

**Source-matching firewall:** `q=exp(2πi/16)` and this path-area law are chosen by the mathematical model. Neither is shown to be the phase transport of the authentic BBP zero-seeded orbit. An entirely nonnormal orbit can be paired with the same independent Pascal model, so root-of-unity cancellation alone is **not a π-normality result**. The groups `C_16` and `(C_2)^4` must not be identified without a source-faithful map.

**External mathematical provenance:** Gaussian-binomial/q-binomial root-of-unity arithmetic is classical; see e.g. https://link.springer.com/article/10.1007/s00026-019-00461-8 . The role in this research package is a constructive adversarial comparison with a source-derived phase, not a claim to have discovered q-binomial coefficients.

## CRPM-05 — Original BBP noncommuting square, summable but seed-blind (PROVED LOCAL from exact original source)

Preserve the *exact* authentic recurrence:

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, `U_0=0`, `U_(n+1)=16 U_n+r(n+1)`.

For any positive integer `p≥2` (primality is not needed for this algebraic identity) let `V_p(x)=p x` and `T_n(x)=16x+r(n+1)`. Then for all `x∈Q` and `n≥0`,

`T_n(V_p(x))−V_p(T_n(x))=(1−p)r(n+1)`.

**Proof.** The `16 p x` terms cancel; the forcing terms leave `(1−p)r(n+1)`. This is an **action-square displacement defect**, not a gauge-invariant holonomy around a closed loop unless a genuine closing morphism has been constructed. Every tested exact rational x has the same defect.

**Original-source integral identity:** writing `P(t)=4−2t³−t⁴−t⁵=(1−t)(t²+2)(t²+2t+2)`,

`r(n)=∫_0^1 t^(8n−8)P(t) dt`, so `0<r(n)≤15/[(8n−7)(8n−6)]` for all `n≥1`.

As a result, `|(1−p)r(n+1)|≤15(p−1)/[(8n+1)(8n+2)]`, and the squared-action defect is absolutely summable in n. The defect is INDEPENDENT of the initial seed, so curvature/summability of this square alone cannot establish selected-orbit normality.

**Cross-check:** main `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md` preserves the same four poles and zero boundary. This square does not replace the selected Fourier gate.

## CRPM-06 — Exact changed-seed π counterexample with *uniform-in-N* bound (PROVED LOCAL)

The classical BBP series says `π=Σ_(k≥1)16^(1−k)r(k)`. Let

`T_n=Σ_(k>n)16^(n−k)r(k)`, `n≥0`.

Then `16^(n−1)π = U_n(0)+T_n`. By the previous integral estimate and `Σ_(j≥1)16^(−j)=1/15`,

`0<T_n≤1/[(8n+1)(8n+2)]`.

For *any real initial seed* s, `U_n(s)=U_n(0)+16^n s`. Choosing `s* = −π/16`, we get the exact identity

`U_n(s*) = U_n(0)−16^(n−1)π = −T_n`.

For `n≥1`, `T_n < 1/(64n²)`, and `Σ_(n≥1)1/n²<2` (e.g. the integral comparison). Thus `Σ_(n≥1)T_n < 1/32`. For every integer `h≠0` and EVERY integer `N≥1`, using `|e^{2πit}−1|≤2π|t|` and classical `π<22/7`,

`| Σ_(n=1)^N e^{2πi h U_n(s*)} − N | ≤ 2π |h| Σ T_n < π |h|/16 < 11 |h|/56`.

Therefore `N^(−1) Σ_(n=1)^N exp(2πih U_n(s*))→1` for every fixed integer h. The same authentic forcing, the same action-square defect, and the same Pascal model can coexist with an **explicit NONNORMAL seed**. This is a genuine counterexample to *seed-blind* normality arguments, not a refutation of normality of the authentic seed `U_0=0`.

**Provenance:** source-series identity classical Bailey–Crandall, https://doi.org/10.1080/10586458.2001.10504441 ; source-selected zero-boundary already required in main frontier and PR #424. The exact elementary uniform bound above is supplied as the research package's paper derivation, not independently Lean verified.

## CRPM-07 — 2-adic local opposition does not ensure real-circle opposition (FINITE EXACT + SUFFICIENT ANALYTIC LEMMA)

For rational `u=A/B` with odd B, define `u mod2^a = A B^(−1) mod 2^a`. Main SUCC's existing source-integrality / permutation work (see PRs #427–#428) provides the relevant general arithmetic context; our new tests independently verify that original `U_n mod2^a` is a complete residue system on several translated finite windows, `a≤6`. This is NOT an independent all-a proof.

In any certified complete window of `m=2^a` source states, pair the unique indices whose residues differ by `m/2`. This produces an exact fixed-point-free involution on the finite window. It gives *perfect opposition of the top 2-adic residue bit*, but NOT in the ordinary real-circle character `exp(2πihU_n)`.

For an arbitrary disjoint pairing `P` of indices, define exact rational errors

`ε_(i,j;h) = dist(h(U_j−U_i)−1/2, Z) ∈ [0,1/2]`.

Pairwise triangle inequality plus `|e^{2πit}−1|≤2π dist(t,Z)` gives the **certified finite inequality**

`|S_N(h)| ≤ N−2|P| + 2π Σ_(i,j)∈P ε_(i,j;h) < N−2|P| + (44/7)Σ ε` (if Σ ε>0; ≤ valid always).

This can serve as a source-specific signed certificate IF a separate all-horizon arithmetic bound proves the mean real-phase error tends to zero and the unmatched fraction tends to zero. It is **stronger than Weyl cancellation and not necessary for it**: for phases `{0,1/4,1/2,3/4}` arranged as `(0,1/2,1/4,3/4)`, the Fourier sum is exactly 0, yet prescribed pairs `(0,2),(1,3)` each have error 1/4. An independent clock cannot be declared a π-phase map merely by matching its cardinalities. **Stronger outright local-to-real counterexample:** the rational states `(0,1)` are complete modulo 2, so their nontrivial 2-adic parity character sums to `1+(−1)=0`, while the real character at h=1 has `exp(2πi·0)+exp(2πi·1)=2`. This disproves a generic transfer of local Fourier cancellation to real-circle cancellation.

**Exact data (finite only):** for original first `2^a` states, a=2,3,4,5,6, mean real opposition errors are approximately `0.3121010, 0.2496503, 0.2072656, 0.2581159, 0.2596148`. Raw values and bounds are rational, as produced by `carrier_path_measure.py`. No decay trend or all-horizon result has been established.

## CRPM-08 — Exact path-sum realization of absolute distance on Z (CLASSICAL, exact finite)

Give `Z` the two successor steps `x→x+1` and `x→x−1`, each chosen with probability 1/2, and discount every step by `λ=3/5`. This creates the countable path-space positive Green measure

`G(a,b)=Σ_(ℓ≥0)(3/5)^ℓ P_a(S_ℓ=b)`.

The sum converges absolutely since `Σ λ^ℓ<∞`. The Markov resolvent equation is

`G(0,d)=1_(d=0)+(3/10)(G(0,d−1)+G(0,d+1))`.

Check that `g(d)=(5/4)3^(−|d|)` satisfies it: at `d=0`, `5/4=1+(3/5)(5/12)`; at positive d the ratio equation is `1=(3/10)(3+1/3)`. The operator `f→δ_0+(3/5)Pf` is a contraction on bounded functions, so the bounded solution is unique. Therefore

`G(a,b)=(5/4)3^(−|a−b|)` and `|a−b|=log_3(G(a,a)/G(a,b))`.

**This is an exact recovery of ordinary absolute value from a carrier-defined all-path superposition.** It is not a new absolute value axiom, and is not a BBP normality result. Finite path truncations are computed directly by exact binomial walk counts:

`G_L(0,d)=Σ_(0≤ℓ≤L, ℓ≡d mod2, ℓ≥|d|) binom(ℓ,(ℓ+|d|)/2)(3/10)^ℓ`.

Since each transition probability is at most one, `0<G(0,d)−G_L(0,d)≤(5/2)(3/5)^(L+1)` once L is finite. The local tests validate the exact formula inside this independent rational tail bound for d=0..5 and L=20,35. This supplies a calibratable positive-path instrument to compare against the phase-sensitive SUCC lift.

The fair Pascal carrier similarly yields the exact normalized positive endpoint measure `P(K=k)=binom(n,k)/2^n`, even though its separately chosen q-phase extension can cancel at roots of unity. Positive probability and signed interference are different observer maps.

## CRPM-09 — Research gate and contamination-proof falsifiers (OPEN)

SUCC already certifies equivalence of base-16 normality and `S_N(h)=o(N)` for every fixed `h≠0` on the ORIGINAL zero-seeded BBP orbit. The question raised by the user's measure proposal is **not** whether a positive carrier can be equipped with a metric or an arbitrary phase that cancels (both are true). It is whether a **source-faithful, seed-sensitive, Archimedean** phase map `Φ_π(γ)` can be derived from the actual carry/prime source in a way that proves a nontrivial selected signed saving not derivable from formal gauge/path identities alone.

One sufficient, falsifiable target is a family of **predeclared** source-derived pairings (or signed cycles) of growing, concatenated observation windows, with exceptional indices `o(N)` and total certified real-phase mismatch `o(N)`. The pairing rule must be defined without inspecting the target Fourier phases, and it must fail on the seed `s*=-π/16`, phase-mutated counterfeits, and a source that merely copies the q-Pascal path statistics. This is a *research strategy*, not an existing theorem. Uniform random-normal streams need not exhibit alignment under a prescribed prime-residue matching, so that specific matching may be too strong: do not assume it is achievable.

A different route is to use a source-authenticated **nonflat** diamond phase connection with a quantified, source-boundary-specific interference estimate. First prove actual map/square commutation (or its defect), the scalar observation map, then a SIGNED inequality with a nontrivial all-horizon rate; only then connect to the selected Weyl gate. Gauge-trivial edge phases, positivity, finite moment matching and one-sided low-pole bounds are insufficient.

### Ledger verdicts

* **SURVIVES, CLASSICAL:** affine path-flow fiber, effective-resistance norm, gauge obstruction and Gaussian-Pascal root-of-unity cancellation and Z Green absolute-distance recovery (CRPM-01..04 and CRPM-08).
* **SURVIVES, PROVED LOCAL / exact tests:** original four-pole affine square, summable source forcing and changed-seed counterexample (CRPM-05..06).
* **SURVIVES, finite exact / conditional only:** 2-adic pairing and finite signed matching inequality (CRPM-07).
* **REFUTED with explicit receipt:** (i) endpoint-gradient phases yield nontrivial path interference; (ii) 2-adic character cancellation automatically yields Archimedean circle cancellation; (iii) carrier-only curvature implies normality regardless of seed.
* **OPEN (CRPM-09):** selected original `U_0=0` Fourier cancellation, π normality, RH and any comparison of these new measures with completed-Weil positivity.
