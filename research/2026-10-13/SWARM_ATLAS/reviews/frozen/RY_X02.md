# SWM-X02 — Holonomy-invariant laws do not supply individual global sections

## 1. Original question and exact hole

A04 identifies deterministic proof-transport obstructions through nonabelian
holonomy; C17 transports a joint law while retaining the original-source index;
F47 identifies the cycle obstruction to consistent clocks. What survives when
point-valued transport is replaced by probability laws? In particular, does a
lawful collection of local distributions certify any simultaneous original
point or phase assignment?

The exact bridge is an affine classification of probability-law sections,
including their possible lift to a random **global point section**. These two
objects are different. The classification and lift criterion are proved below.
The independent A04 audit found no defect in its fixed-point criterion.

## 2. Mathematical context and provenance

This assignment starts at integrated commit
`7913e101d6e83b697f4e13535cc3b1330b80f0c2` and reads A04, C17, and F47 directly.
The ingredients are classical finite permutation groups, invariant measures,
and finite conditional probabilities. Academic novelty is **UNVERIFIED**; no
new general invariant-measure principle is claimed. The derivation below is
self-contained and requires no external theorem to close a proof gap. It adds
an explicit law-to-individual-section obstruction and source-conditioned target
criterion to the repository's actual transport objects. For primary background,
Etingof et al., [Introduction to representation theory](https://math.mit.edu/~etingof/representationtheorybook.pdf),
§4.7 uses the finite-group average as projection onto invariant vectors. That
averaging mechanism is classical; this dossier derives the probability-simplex
and global-coupling statements explicitly rather than attributing them to that
representation-theory discussion.

Only new X02 files are added. A04's implementation is imported solely as the
system under audit; the independent section enumeration, permutation-group,
linear-constraint, and probability calculations do not call its algorithms.

## 3. Common ambient, objects, maps, and hypotheses

Let G be a finite connected graph with a chosen orientation for each declared
edge, a root r, and nonempty finite fiber F. Every edge e:u→v carries a
permutation g_e:F→F; traversal in reverse uses g_e⁻¹. Multiple edges and loops
are allowed but are not needed for the counterexample. The edge list is the
complete declared source contract. A graph assertion does not authenticate
that contract empirically.

Choose a spanning tree and write P_v:F→F for root-to-v transport. Define
`H_e = P_v⁻¹ g_e P_u` and let H≤Sym(F) be the subgroup they generate. Its orbits
are C₁,…,C_k. A point section is a family s_v satisfying s_v=g_e(s_u).
A law section is a family μ_v∈Δ(F) satisfying `μ_v=(g_e)_* μ_u`, where
`g_*μ(y)=μ(g⁻¹y)`. These are simultaneous equalities of laws, not a promise of
simultaneous pointwise outcomes.

For the original-source version, fix a finite set O and marginal π∈Δ(O).
The object at v is a joint law J_v∈Δ(O×F) with O-marginal π. Every transport
is `id_O×g_e`; it leaves the original index untouched. Both real probabilities
and their rational submodel are covered. Conditional claims apply only on
positive-mass events; originals with π(o)=0 are not silently certified.

## 4. Candidate theorem and quantified conclusions

**Law-section classification.** For every such connection, restriction to the
root is an affine bijection

`{law sections} ≅ {H-invariant μ∈Δ(F)} ≅ Δ({C₁,…,C_k})`.

The map sends orbit masses λ_j to `μ_r(x)=λ_j/|C_j|` for x∈C_j and then to
`μ_v=(P_v)_*μ_r`. The extreme law sections are precisely the transports of the
uniform laws on individual H-orbits. The polytope has dimension k−1 and is
always nonempty. Point sections correspond precisely to singleton H-orbits.

**Global coupling criterion.** A supplied law section is the family of
marginals of a probability law ρ on F^V supported on all edge equations
simultaneously iff μ_r is supported on `Fix(H)`. If such ρ exists, it is unique
for the supplied law section. Thus liftable law sections form the face generated
by singleton-orbit vertices; that face can be empty. Every law section lifts iff
all H-orbits are singletons, equivalently H acts trivially on F. Existence of
some point section is insufficient to lift every law section.

**Original-index classification.** Joint-law sections with marginal π are
parametrized by nonnegative orbit masses α_o,j satisfying

`Σ_j α_o,j = π(o)` and `J_r(o,x)=α_o,j/|C_j|` for x∈C_j.

This is a product of orbit simplexes, one for each o with π(o)>0, with dimension
`|supp(π)|(k−1)`. Its extreme points assign one orbit to each positive-mass
original and distribute that original's mass uniformly on its assigned orbit.
Transport to v is by `id_O×P_v`.

**Original-target criterion.** Given a fixed target T:O→Z, observing a
positive-mass local state x certifies a unique T-value within the declared
support iff all originals o with α_o,j>0 have the same T(o), where
`j` is the orbit of `P_v⁻¹x`. Consequently a deterministic decoder for T from
local state exists almost surely iff this constancy condition holds for every
positive-mass orbit. Conditional distributions of O are identical for any two
states within the same transported orbit. Changing vertices or tree coordinates
does not improve this source-relative identifiability.

## 5. Complete derivation and coherence checks

Tree equations uniquely force μ_v=(P_v)_*μ_r. The remaining edge equation
becomes `(P_v)_*μ_r=(g_eP_u)_*μ_r`, or `(H_e)_*μ_r=μ_r` after applying the inverse
tree transport. Invariance under each generator implies invariance under its
inverse and under products, hence under H. Conversely H-invariance supplies
every edge equation. Restriction to r and tree propagation are mutually inverse
affine maps.

For a finite permutation, `(h)_*μ=μ` means μ(hx)=μ(x). Thus H-invariance is
exactly constancy on H-orbits. The total mass λ_j of C_j forces each point in
that orbit to have mass λ_j/|C_j|; arbitrary nonnegative orbit masses summing to
one give an invariant law. Disjoint orbit supports give uniqueness. The standard
coordinate simplex has precisely its unit coordinate vectors as extreme points:
if two coordinates are positive, moving a sufficiently small mass between them
expresses the point as a nontrivial average; a unit vector cannot be so expressed
by nonnegative normalized vectors. This proves the claimed vertices and
dimension without importing a numerical optimization claim.

Independently rederiving A04, tree equations force a point section to be
`s_v=P_vx`. The arbitrary edge equation is then equivalent to H_ex=x. These
hold for all edges iff H fixes x. Therefore global sections are bijective with
Fix(H), and there is exactly one section for each such root value. If a joint
ρ is supported on global sections, its root marginal must consequently be
supported on Fix(H). Conversely, when μ_r has that support, push it forward by
`x↦(P_vx)_v` to obtain ρ. This has the desired marginals and is supported on
every edge equation. Any eligible ρ must be this pushforward because a section
is uniquely determined by its root. This proves necessity, sufficiency, and
uniqueness; mere compatibility of edge marginals is weaker.

For original indices, transport never mixes O-rows. Each row J_r(o,−), of total
mass π(o), must separately be H-invariant. Applying the orbit argument to each
positive row proves the α classification. A zero-marginal row is identically
zero. The product's extreme points choose an extreme orbit law independently
in every positive row: a nonextreme row permits a nontrivial convex split of the
whole joint law, while extremality of every row forces each coordinate of any
convex decomposition to coincide. This also gives the stated dimension.

For x∈C_j of positive total mass, Bayes' finite formula gives

`Pr(o | x) = α_o,j / Σ_b α_b,j`.

The factor |C_j| cancels. The support is therefore exactly {o:α_o,j>0}, independent
of x inside the orbit. A target decoder exists precisely when T is constant on
each such support; choose that constant to construct the decoder. Distinct
T-values in one support give a direct collision witness. Tree transport merely
renames the local states. The orbit-coordinate map
`q_v(x)=[P_v⁻¹x]_H` obeys `q_v g_e=q_u`, because their two root-coordinate values
differ by H_e. It is therefore an actual commuting quotient, not an analogy.

Finally a vertexwise gauge k_v changes g_e to k_v g_e k_u⁻¹, laws to
(k_v)_*μ_v, and joint laws to (id_O×k_v)_*J_v. Tree paths telescope to
`P'_v=k_vP_vk_r⁻¹`; holonomy conjugates by k_r, so its orbit simplexes and
fixed-point lift face are carried bijectively to the new coordinates. Neither
original-target constancy nor existence of a global coupling changes.

## 6. Crucible: source-complete counterexamples and exact receipts

**Nonabelian obstruction invisible to marginal consistency.** Use F={0,1,2}
and a simple graph on vertices0,1,2,3. Edges0→1,1→2,2→3 have identity transport;
edges0→2 and0→3 carry s=(01) and t=(012). The identity tree makes s,t the two
based holonomies. They generate the nonabelian group S₃, which acts transitively
with no common fixed point. The unique law section is uniform at every vertex,
but there is no point section and no joint distribution supported on all edge
constraints. The edge laws `(x,g_ex)` with uniform x are individually valid and
have compatible one-vertex marginals; they cannot be amalgamated into the
claimed global point assignment.

**A point section exists, yet a law can still fail to lift.** Extend both
permutations by fixing a fourth state3. The holonomy orbits are {0,1,2} and {3}.
There is one deterministic point section, rooted at3, while the law polytope
has two vertices: uniform on the first three states and δ₃. Only δ₃ lifts to a
random global point section. The existence test alone misses the obstruction
for a specified law.

**Original preparation cannot be averaged for free.** If a declared original
preparation is a deterministic map i:O→F, then
`J_r(o,x)=π(o)1_{x=i(o)}`. Joint-law invariance requires every i(o) with π(o)>0 to
lie in Fix(H), since its conditional row is a Dirac mass. Averaging this
preparation over a holonomy orbit produces a different declared joint law.
It does not manufacture a certificate about the unrandomized preparation.
For transitive H, every lawful joint law is π⊗uniform(F), so the local state
conveys no information about O beyond the prior support. A nonconstant original
target remains ambiguous.

**Clock bridge.** For additive clock fiber Z/m, the subgroup H is generated
by cycle-lag residues. Orbits are cosets of H and extreme law sections are
uniform on those cosets. A frustrated nonzero cycle therefore still admits
law sections, while no deterministic phase assignment exists. For one cycle
of residual c, the number of orbits is gcd(m,c). Uniform uncertainty about
phase does not prove synchronized actual phases or shared semantic truth.

**Retained coupling matters.** The probe uses two originals with marginal
(1/3,2/3) and holonomy orbits {0,1},{2},{3}, with row orbit masses
(1/6,1/6,0) and (1/3,0,1/3). States0 and1 have the same ambiguous original
posterior (1/3,2/3), while2 certifies original0 and3 certifies original1.
A separate diagonal-versus-independent control has identical original and
current marginals but different target identifiability.

`X02_RECEIPT.json` records **617** generator-pair classifications on degrees1–4
against independently enumerated active-constraint vertices and exact rational
ranks; **49,421** denominator-six laws checked against the orbit reconstruction;
**216** S₃ triangle connections compared with brute-force point sections and
A04; **396** gauge-transformed extreme law sections; and **1,295** clock-lag
triangles for moduli2–8 checked against direct phase enumeration. Six focused
unit tests cover the counterexamples, source coupling, null conditioning, and
invalid transport. A first local test caught a consumed-generator bug in the
new brute-force oracle; materializing its edge iterable corrected it, and all
reported runs are after that correction. These finite controls corroborate the
universal written derivations; they do not replace them.

## 7. Verdict and independent audit

**PROVED LOCAL / CLASSICAL:** orbit-simplex classification, fixed-original joint
version, global-coupling lift criterion, gauge invariance, and original-target
support criterion. **REFUTED:** compatible invariant law sections entail an
individual global point section; existence of one point section lifts every
law; stochastic clock coherence entails actual phase alignment. The A04
fixed-point theorem **SURVIVES** the independent proof reconstruction and all
216 exact triangle audits. Its distinction between arbitrary actions with fixed
points and regular torsors remains necessary.

There is no Lean kernel proof for X02. Academic novelty, empirical source
completeness, and any claimed physical preparation are **UNVERIFIED**.

## 8. Remaining obstruction and next falsifier

Invertibility and the finite common fiber are load-bearing. For general
stochastic loop transports K₀,K₁, a common invariant law need not exist: on
{0,1}, let K₀ reset every state to0 and K₁ reset every state to1. Their unique
stationary laws are δ₀ and δ₁, so there is no common law. Replacing permutations
by arbitrary stochastic instruments therefore requires a new compatibility
analysis, not reuse of the orbit theorem.

The next discriminating target is a graph of specified finite joint
report/current-state instruments, retaining the original index and recording
which histories can actually coexist. Derive the exact linear feasibility
problem for unconditioned laws and the additional global-coupling constraints;
then include incompatible resets, null outcomes, and shared latent noise as
mandatory controls. A feasible marginal system must not be promoted to an
actual-history amalgamation without the coupling proof.

## 9. Cross-domain payoff and dominance boundary

A04 supplies the actual connection and its based holonomy; C17 supplies the
functorial action `J↦(id_O×g)_*J`; F47 embeds clock lags as translation
permutations. X02 applies that action to the same graph, classifies its law
sections, and identifies exactly which lie in the image of probability laws
on A04's point-section set. The extra obstruction is the fixed-point-support
face, while the retained α rows control original-target claims. This strictly
separates coherent stochastic descriptions from a global individual witness.
It proves no source authentication, stochastic physical realization, or
RH-facing positivity statement.

## 10. Deliverables and reproducibility

Owned files are this dossier, `X02_RECEIPT.json`,
`scripts/swarm_x02_probe.py`, and `tests/test_swarm_x02.py`, on isolated branch
`research/swarm-x02-holonomy-laws-2026-10-13`.

Executed successfully:

```sh
python -m unittest discover -s tests -p test_swarm_x02.py -v
python scripts/swarm_x02_probe.py > research/2026-10-13/SWARM_ATLAS/X02_RECEIPT.json
```

The receipt binds the exact probe by SHA-256 and gives the frozen base. Six
owned tests passed. Repository-wide validation is left to the integration
owner; this assignment claims no full-suite run, CI success, remote push, or
kernel formalization.
