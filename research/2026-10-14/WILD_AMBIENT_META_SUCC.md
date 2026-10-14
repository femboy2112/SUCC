# WILD-AMBIENT SUCC — Alexander complement, perfect commutator towers and finite nonabelian observers

**Research date:** 2026-10-14. **Intended parent:** `femboy2112/SUCC`, Arithmetic Meta-Weil PR #86 @ `205ffd020dd2a320eeac70a91a2a2700c969c048` (descends from Recursive Meta-SUCC PR #80). **Sibling, not merged:** original-source contour PR #83 and signed Weil H¹ tail PR #84; newest negative-depth PR #85. The pre-existing branch `research/wild-adelic-embedding-solenoid-2026-10-14` was discovered at PR #86's *unmodified* head; this research uses its own independent child branch. **RH PROVED: NO.** No zero positions, fake prime sources, physical probes, auxiliary Gamma factors or assumed Weil-positive Hilbert objects enter the construction.

## 0. The user conjecture and strongest precise interpretation

The conjecture is that a mathematically simple global object can appear, to a finite embedded observer, as the projection of an unboundedly entwined embedding. Two logically separate issues must be typed:

- **Intrinsic structure:** `e(S²) ≅ S²`. It determines intrinsic topological invariants of the surface, but not how its exterior is wired.
- **Ambient interaction:** the complementary space `R³ \ e(B³)` and its loops, attaching/branch relations and actual carrier source maps. The forgetful mapping `(R³,e(S²)) ↦ S²` need not reflect isomorphisms/equivalences of *pairs*. A source-dependent exterior-path probe can distinguish embeddings that all pure intrinsic topological models conflate.

Alexander's original 1924 horned sphere is the decisive classical control. Its bounded side is the image of a topological 3-ball, yet its exterior is not simply connected. Hatcher's *Algebraic Topology*, §2.B, pp. 169–172, explicitly constructs the classical exterior group through injected commutator towers. The topological realization is **IMPORTED MATHEMATICS**, not a claim that this Python module constructed the infinite PL embedding or physically measured its complement.

**New-to-SUCC objective:** derive and separately verify an exact finite-model observer of that perfect nonabelian group, plus a contrasting ambient Hopf/unlink measurement, one independent inverse-limit/cohomology obstruction, and a proved firewall against interpreting the new group energy as a source-positive Weil form.

### Relevant frozen project context

- SUCC PR #86 reconstructs the **true** source-signed completed Weil form from the genuine prime/Gamma/operator side. It proved that prime dilations and full-line Gamma convolution commute, but compression to a Weil window creates a *boundary-leakage commutator*. This is not naturally the nonabelian holonomy of Alexander's complement.
- SUCC PR #83 constructs source-certified complex contour windings, but a winding number lives in an **abelian** `Z` target. A scalar phase winding cannot read an arbitrary perfect-group obstruction through a source map.
- SUCC NO-GHOST and VOYAGER independently separate hypothetical mathematical possibilities from lawful source histories, and inverse-system completions from original-source realizations. Their methods are *architectural prerequisites*, not automatically an Alexander complement theorem.

## WA-01 — the intrinsic sphere does NOT identify the embedding (EXTERNAL CLASSICAL)

Let `e_0:S²→S³` be the standard tame sphere and `e_A:S²→S³` Alexander's horned sphere. Both are homeomorphisms onto a 2-sphere, and therefore possess the same intrinsic topology. However:

`π_1(S³ \ e_0(B³)) = 1`, while `π_1(S³ \ e_A(B³)) ≠ 1`.

Any ambient homeomorphism of `S³` mapping one embedded ball to the other would induce an isomorphism between these exterior groups. Such a map cannot exist. Therefore **an intrinsic equivalence does not necessarily lift to an ambient equivalence**. An octahedral finite PL sphere `(V,E,F)=(6,12,8)`, Euler characteristic 2, is a canonical exact intrinsic positive control; it is NOT a stage of the actual infinite Alexander embedding.

**Sharper homology blindness:** Hatcher shows the horned exterior group has trivial abelianization. Thus `H_1(exterior;Z)=0` despite the nontrivial `π_1`. This is not contradicted by Alexander duality, which sees the embedded `S²` cohomology and gives the same first-homology data for the tame and horned complements. Every **global** homomorphism to an abelian target is trivial, even though individual generators in a finite approximation may have nonzero first homology. This distinguishes stage-local characters from a character coherent under **all** source transitions.

Citations: Alexander, *An Example of a Simply Connected Surface Bounding a Region Which Is Not Simply Connected*, PNAS 10 (1924), 8–10: https://www.jstor.org/stable/84202 . Hatcher, *Algebraic Topology*, §2.B, pp. 169–172: https://pi.math.cornell.edu/~hatcher/AT/AT.pdf . Hatcher's pp. 171–172 state the generator-to-commutator injections, their direct-union identification with the exterior group and vanishing abelianization explicitly.

## WA-02 — exact finite ambient link certificates (PROVED LOCAL / CLASSICAL LINKING)

For one oriented rational square disk `D_r=[-r,r]² ×{0}` and a disjoint oriented embedded rectangle `B` in the plane `x=0` with vertical crossings at distinct `y_0<y_1`, both away from the square boundary, the linking number of their boundary curves is the oriented transverse intersection count:

`lk(∂D_r,B) = orientation(D) * orientation(B) * (1_(|y_1|<r) − 1_(|y_0|<r))`.

Proof: the only intersections of B with the spanning surface occur on the two vertical edges at z=0; the upward and downward edges have intersection signs + and −. Signed intersection with a spanning surface equals classical linking number for the two disjoint PL loops. The code checks all intersection coordinates using `Fraction`, not an unspecified drawing projection.

**Positive/negative controls:** square `r=2`, rectangle `(y_0,y_1)=(1,3)` has `lk=-1` (Hopf); `(3,5)` is unlinked with `lk=0`. Reversing either orientation flips the sign while preserving `|lk|`; positive homothetic rescaling preserves linking; boundary contact and mismatched source/epoch/basis/orientation are rejected. Exhaustive small rational-location comparisons are separate from the actual segment evaluator.

**Crucial limitation:** This is an *abelian* two-component link measurement. It is NOT a construction of Alexander's horns and cannot, on its own, detect the nontrivial **perfect** group of their exterior. It is a calibration of actual ambient sensing, not the final wildness lamp.

## WA-03 — source-indexed binary commutator tower (PROVED LOCAL; HATCHER IDENTIFICATION IMPORT)

For `n≥0`, let `F_n` denote a free group on `2^n` generators `x_v` indexed by binary words `v` of length n. Define the transition homomorphism

`φ_n : F_n → F_(n+1),  x_v ↦ [x_(v0), x_(v1)]`,

where `[a,b]=aba^{-1}b^{-1}`. Its algebraic normal form is exact; at finite depth n the root expands to a free reduced word of length `4^n` in `2^n` leaf generators, and its total exponent of every leaf is zero for n≥1.

**Injection proof (all n, not a bounded experiment).** Each target stage splits as a free product over old generator indices of independent rank-two free groups: `F_(n+1)=*_(|v|=n) F(x_(v0),x_(v1))`. In each rank-two factor, `[x_(v0),x_(v1)]` is a nontrivial freely reduced word and thus induces an injective map `Z→F_2`. The normal-form theorem for free products says the free product of these injections remains injective. Therefore every stage map `φ_n` is injective.

Form the directed colimit `G=colim(F_n,φ_n)`. Every generator at any stage is literally a commutator at the next stage, so `G=[G,G]`, hence its abelianization vanishes and every scalar/abelian character is trivial. Nontriviality follows either from the injected root or from the independent `A_5` homomorphism below.

**Exact relation to the real Alexander complement:** Hatcher's p. 172 states that `π_1(R³\B)` is the *union of the corresponding increasing groups* with precisely these generator-to-commutator transitions, after choosing the geometric generator system. Thus the abstract colimit is identified with the **actual horned-ball exterior fundamental group BY THIS EXTERNAL THEOREM**, not via the local free-word experiments. Basepoint changes conjugate group elements, so unqualified root-word labels are not ambient-gauge invariants.

**Finite causal cost:** explicitly expanding the root at depth n requires `4^n` signed letters, with `2^n` leaf generators; a finite lookup-circuit presentation remains compact. The reference evaluator refuses expansions exceeding a declared bound. A finite mathematical recursive description is not permission to perform infinitely many carrier experiments.

## WA-04 — the finite nonabelian `A_5` observer (PROVED LOCAL + GROUP-THEORETIC UNIVERSAL CONSTRUCTION)

Enumerate the 60 even permutations of five points. For every ordered pair `(a,b)` among the 60, evaluate `[a,b]` exactly. The 3,600-pair table maps *onto all 60 elements*, and stores a two-element commutator witness for each `g∈A_5`. This is independently valid mathematical finite exhaustive evidence; no probabilistic heuristic or Euler source occurs.

Fix any nonidentity target `g_root∈A_5`, for example `(1 2 3)`. At every vertex v with assigned `g_v`, choose **once from the fixed 60-entry table** `g_(v0),g_(v1)` such that `[g_(v0),g_(v1)]=g_v`. Then the maps `ρ_n:F_n→A_5` determined on leaf generators are compatible: `ρ_(n+1) φ_n=ρ_n`. The universal property of the directed colimit therefore produces ONE bona fide homomorphism

`ρ : G → A_5` with `ρ(x_root)=g_root≠1`.

This is a **finite construction rule characterizing an infinite recursively presented source**, not a finite empirical table from which infinity is guessed. An independent free-word evaluator at depth n checks that the expanded root word maps to `g_root` for every tested n. Source representation remains a theorem for all n because the finite table is complete and the recursion preserves the defining relations.

**Gauge-invariant readout:** a five-dimensional permutation representation `P_g` has trace equal to the number of fixed points of g. The root 3-cycle has `tr(P_g)=2`, versus `tr(P_1)=5`. Every A5 conjugation preserves trace (checked for all 60 gauges), giving a mathematically legitimate common-basis invariant rather than an arbitrary orientation sign.

**Actual source boundary:** Combined with the independently imported Hatcher exterior-group identification, this defines a nontrivial finite-group representation of Alexander's actual horned exterior. It does **not** construct an observer physically able to enact these loop probes, nor does it prove a homomorphism from SUCC's genuine prime/Archimedean operators to this group. Riebe (1968), *The Fundamental Groups of the Complements of Some Solid Horned Spheres*, independently reports A5 representations for classical/higher-order horned-sphere groups: https://digitalcommons.usu.edu/etd/6821/ . No academic-priority claim is made for A5 commutator surjectivity or the exterior group.

## WA-05 — a sharp SCALAR CONTOUR NO-GO for perfect ambient groups (PROVED / CLASSICAL)

For any connected space X whose fundamental group is perfect, any continuous nonvanishing scalar complex observable `f:X→C^×` induces

`f_* : π_1(X) → π_1(C^×) ≅ Z`.

Since `Z` is abelian, `f_*` must be zero. Therefore **every loop in X has zero scalar winding under f**, even when X contains a noncontractible loop. This is a definitive toolkit-relative blind spot for attempts to detect the Alexander exterior group by only scalar winding numbers. It does NOT say that a certified Xi contour observer cannot count zeros in a complex domain: its loops live in a different space and the genuine holomorphic source is essential. A source-justified intertwiner would be needed to transport the claim between the domains. The finite A5 representation is a nonabelian mathematical discriminator that survives this no-go.

**Mutation:** finite-stage `F_n` may admit nonzero abelian characters on individual *leaf* generators; only compatibility through all stages kills the root and every globally descending scalar character. Confusing stage coordinates with global characters violates the declared source-indexed transport.

## WA-06 — an independent solenoid and nontrivial global-cover obstruction (CLASSICAL / PROVED ALGEBRA)

Consider the inverse system of circles `S¹ ←^(z↦z^d) S¹ ←⋯` for integer d≥2. Each finite observed object is a smooth ordinary circle. On H¹ the induced maps multiply by d, so continuity of Čech cohomology for inverse limits of compact polyhedra gives

`Čech H¹(solenoid_d;Z) = colim(Z --×d--> Z --×d-->⋯) = Z[1/d]`.

The code realizes finite-stage classes `(n,j)→n/d^j∈Q`, and checks `(n,j)~(dn,j+1)` exactly. This is a fully specified inverse-limit object and a classical imported cohomology-continuity theorem, **not** Alexander's horned sphere (their intrinsic topologies differ!).

Even a single finite covering `z↦z^d` has no continuous global section: an alleged section on π₁ would satisfy `d·deg(section)=1`, impossible for d>1. Every finite set of rational phases has individually valid lifts; transporting around an oriented loop permutes the sheets by `i↦i+winding (mod d)`. This supplies a clean abelian/lower-order gluing obstruction *in contrast* to WA-05's perfect-group, abelian-blind obstruction.

A standard reference proving the solenoid's Čech H¹ calculation from circle-bonding maps is the topology literature on continuity of Čech cohomology for inverse limits, e.g. T. Gähler / D. Rust tiling-space notes: https://www.math.uni-bielefeld.de/~drust/papers/thesis_corrections.pdf §1.2.21–22.

## WA-07 — projection curvature is NOT proof of ambient wildness (PROVED LOCAL)

PR #86's genuine original-Gamma source already showed that full translations commute but their bounded-window compressions can fail to commute. An independent exact rational three-state control in this contribution has commuting matrices `A` and `K=A²` yet 

`[PAP,PKP] = [[0,-1,0],[1,0,0],[0,0,0]]≠0`

for `P=diag(1,1,0)`. The commutator equals its explicit outside-window leakage term. Thus **a nonzero observed compressed commutator is insufficient to infer a nontrivial uncompressed holonomy group, let alone a wild embedding**. It is consistent with purely lawful projection/endpoint effects; to make an ambient claim SUCC must retain the original space, actual embeddings and compatible continuation laws.

## WA-08 — finite nonabelian POSITIVE ENERGY does not imply Weil positivity (REFUTED SHORTCUT)

For any finite unitary group representation, the connection energy `E(v)=Σ_g||U_gv−v||²` is positive semidefinite. In the 5D permutation representation of A5, the constant vector is fixed by **every** element, so its energy vanishes. A signed source-style toy `E(v)−||v||²` is strictly negative on that vector (exact value `−5`). Thus the existence of nontrivial finite nonabelian holonomy and a true positive Dirichlet energy does not force a signed form to be nonnegative.

The genuine completed zeta/Weil form from PR #86 has the exact source-signed structure

`Q_W = E_Gamma + Σ_(n=p^k) w_n ||T_(log n)v−v||² − D_a ||v||² + 2|<v,cosh>|² − 2|<v,sinh>|²`.

`D_a` is a negative scalar correction and the two pole channels have opposite signs. **No SUCC/source functor from the exterior A5 group to these actual prime/Gamma operators has been constructed.** Authentic prime dilations and the full Gamma convolution are commuting (PR #86); importing a disconnected A5 gap or wildness argument would be wrong. Reflection symmetry also commutes with the indefinite toy form diag(1,−1): symmetry is not a positivity theorem.

## 1. Auditable claim ledger and provenance

| ID | Status | Claim | Evidence and boundary |
| --- | --- | --- | --- |
| WA-01 | EXTERNAL CLASSICAL | Standard vs Alexander intrinsic S² but ambient non-equivalent; nontrivial perfect exterior group | Alexander (1924), Hatcher §2.B; no geometric horn software construction |
| WA-02 | PROVED LOCAL / CLASSICAL | Oriented PL Hopf/unlink intersection equals linking number | Fraction geometry + complete restricted source contract; cannot certify horn wildness |
| WA-03 | PROVED LOCAL / CLASSICAL | Injective free commutator tower; perfect nontrivial colimit; scalar characters zero | Universal free-product normal form and compatible finite A5 representation; full Alexander identification EXTERNAL |
| WA-04 | PROVED LOCAL | Complete 60-element A5 commutator witnesses and finite invariant trace | 3600 exact products, exhaustive gauge conjugation, independent free-word oracle; no physical group probe |
| WA-05 | PROVED / CLASSICAL | Scalar complex winding is blind on a perfect π₁ source | Functor π₁→Z factors through abelianization; not a statement about zero-counting in the xi plane |
| WA-06 | CLASSICAL/PROVED ALGEBRA | Dyadic solenoid Čech H¹=Z[1/2], no continuous circle section | Classical cohomology-continuity theorem, finite rational stage checks; not an Alexander embedding |
| WA-07 | PROVED LOCAL | Projection can introduce commutators from commuting operators | Independent exact 3x3 matrix/cross-leakage certificate; source holonomy not inferred |
| WA-08 | REFUTED SHORTCUT | Nonabelian positive connection Gram ⇒ genuine signed Weil positive | Explicit -5 toy value, missing source functor, PR #86 original signed identity |
| WA-09 | UNVERIFIED | Physically realizable ambient/topological probe and verified arithmetic-to-embedding source functor | No device, no authenticated Euler/Weil-to-A5 morphism |
| WA-10 | UNVERIFIED | Original Weil positivity / RH proof from topology | No all-test lower bound or Suzuki global limit |

## 2. What would change the RH verdict?

1. Construct a **source-preserving representation** of the full arithmetic action graph `(S,V_p, Gamma, pole, half density, support projection)` in a mathematically justified *ambient* host with nontrivial source-tested higher holonomy, rather than borrowing A5 from Alexander.
2. Derive the **exact form identity** between its associated positive connection/Dirichlet energy and the *complete original signed* Suzuki/Weil form on the correct `H₀¹(-a,a)` test domain. Retain original Gamma contact, conductor, pole, negative scalar and all true prime-power atoms. The map must not assume sign as a premise.
3. Prove all-test lower bounds `Q_(a,J)(v,v)≥−η_(a,J)||v||²_(H¹)` with `η→0` using the full authentic source, or exhibit a strict certified negative witness for a candidate surrogate. Neither finite A5 representation nor finite contour samples satisfies this obligation.
4. Test abelian characters, nonabelian representations, inverse limits, false global sections and projection-only commutators in hostile matched sources. If the real arithmetic group remains flat under every lawful probe, classify that attempted nonabelian mechanism as **REFUTED FOR THAT SOURCE**, not an IdealHard proof.

**Verdict:** Genuine mathematical progress on identifying which models/observers lose global information under abelianization and finite projection. The Alexander complement supplies an actual classic physical-space topology example; SUCC now has a constructive finite nonabelian group observer of its Hatcher model. It remains a source-model diagnostic, not a source-derived proof of Weil positivity. Scholarly priority not established; mathematical ingredients are classical.

## 3. Reproduction

- `observational_succ/wild_ambient_succ.py` — pure standard library, exact rational PL intersection, free word source laws, A5 finite commutator table, solenoid phase and source/firewall API.
- `tests/test_wild_ambient_succ.py` — independent group-word evaluation and linking controls, source ID/epoch/frame mutations, projective-cover and Weil-sign mutations.
- `scripts/wild_ambient_succ_probe.py --verify research/2026-10-14/WILD_AMBIENT_SUCC_RECEIPT.json` — deterministic exact JSON receipt, each field scoped.
- Dedicated Python 3.10 / 3.13 GitHub workflow plus `scripts/verify_provenance.py`; no requirement for external pip packages in focused tests.
- Review against true parent `205ffd020dd2a320eeac70a91a2a2700c969c048`, and explicit unmerged sibling PR #83/#84. Exact remote CI result needs verification on the *published new head*; local tests are an independent but smaller suite.
