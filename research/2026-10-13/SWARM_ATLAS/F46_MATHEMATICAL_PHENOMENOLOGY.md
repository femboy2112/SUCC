# F46 — Target-relative reconstruction, self-boundaries, and tolerant repair

First-generation independent dossier, 2026-10-13. Immutable source parent:
`5eb09e7cba36ec01b8f9d6834b78b5766fd93935`; investigator branch
`research/swm-f46-2026-10-13`. This is mathematical phenomenology in a declared
finite model. No psychology, neuroscience, physical ontology, RH, academic
novelty, or proof-assistant certification is asserted. Independent non-deriver
review remains the acceptance gate. Only this dossier, its standalone probe,
and its receipt are contributed.

## 1. Original question

When is a representation feature load-bearing for an observer's selected
field reconstruction or prediction, and what precisely obstructs repairing
that representation? Can a declared self/outside boundary be recovered from
the available representation without treating a semantic commitment as a
source fact?

The faithful reading is a preservation problem: a finite observer uses a
representation to make selected claims about a source; removing features
may erase distinctions needed for those claims. The word *self* supplies a
selected target, not a privileged physical partition. The contribution is
an exact quantitative refinement of the existing zero-error fiber criterion,
plus a minimal obstruction to a canonical repair at positive tolerance.

The initial gap is a pathway-gap: translate the informal terms into exact
maps. The resulting probe-gap compares exact sufficient representations,
tolerant approximations, and source-realizing reconstructions. The proofs
below distinguish them. External source authentication is an access-gap;
none of the finite tables or hashes supplies that contact.

## 2. Existing mathematical context

**Primary prior art, browsed on 2026-10-13:** optimal recovery studies what
can be reconstructed from limited information on a specified function class.
Micchelli and Rivlin's [1977 survey](https://link.springer.com/chapter/10.1007/978-1-4684-2388-4_1)
supplies this historical context; the publisher abstract was accessible,
the chapter body was not. Paruchuri and Chatterjee's [optimal-recovery paper](https://arxiv.org/abs/2307.01304)
relates reconstruction to Chebyshev centers and radii. Basu, Seo, and
Varshney's [maximal-distortion functional-coding paper](https://arxiv.org/html/2204.02586)
uses geometric feasible sets and hypergraphs for approximate function
computation. F46 treats a deterministic one-shot finite source, not their
asymptotic probabilistic coding problems. The elementary statements below
are proved here and no scholarly priority is claimed.

**Existing SUCC authority:** `field_relative_closure.py::FiniteField.factor`
already checks exact target constancy on observation fibers.
`phenomenology.py::Phenomenology` distinguishes restricted thin signatures,
ordered path signatures, and caller-supplied shadow targets. Current
architecture/roadmap/ledger already contain zero-error side-information
coloring (O65), behavioral quotient/action closure (O580–O587), causal
descent and minimal exact pair repair (O572, O574–O575), and source-realization
limits (O615, O629). F46 does not rebrand those as new discoveries.

**Import boundary:** `provenance/IMPORT_MANIFEST.json` names source repository
`femboy2112/FuckingRH`, commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`, original
`actualization/phenomenology.py`, blob
`b207b7590bd601c72dc239b0c89726517b5b20e6`, destination blob
`69d44bef4de5bff4ffb193e2a229a26105b7c93a`, and literal namespace translation.
The exact original was inspected with `git show` in the local source repo;
the frozen founding dossier and Yoneda guide were also inspected. Its SUCC
import commit is `ddefcaefd85a0469bae5f2678e97e6fd0e1f0b39`.
`field_relative_closure.py` is native: originating SUCC commit
`d1e64948f60662601074c1738d355b3456a17dcf`, current blob
`8110b6a0b20de56d495602fe9b288875e44b25e6`. No imported or runtime file is
modified. SHA-256 bindings to the inspected sources and governing files
are in the receipt.

## 3. Proposed SUCC objects

Fix a nonempty finite declared source `X`, a representation `q:X→Y`, a
positive integer `m`, and a selected rational target field `F:X→ℚ^m`.
Thus the target is a bounded real vector-valued field, with rational
coordinates for exact computation. Every source state has a table entry.
Decode only on `im(q)`.

A decoder is any map `d:im(q)→ℚ^m`. Its loss and optimal radius are

\[
 L(d;q,F)=\max_{x\in X}\|F(x)-d(q(x))\|_\infty,
 \qquad R(q,F)=\min_d L(d;q,F).
\]

All target coordinates have declared units. A vector of unrelated quantities
must be normalized or weighted before this norm has an interpretation.
Decoders may return coordinatewise estimates outside `F(X)`; they need not
describe a source-realizing field. Midpoints are estimates, not probabilities.
The source and loss contract, not the name *phenomenology*, justify the model.

An extra mathematical feature is `h:X→{0,…,k−1}` with joint report `(q,h)`.
It is not automatically a physically available probe. A feature is
**load-bearing at tolerance ε for F** when deleting it changes
`R≤ε` to `R>ε`. The stronger numerical notion is a strict radius increase.
Neither notion means that the feature is necessary for every other target.

A **self-boundary** is an independently declared Boolean target
`b:X→{0,1}`; the inside region is `b⁻¹(1)`. Recovery of this boundary is
the factorization question `b=\bar b∘q`. A prediction of `1/2` has absolute
error `1/2` at either label and decides neither membership nor its probability.

For stationary deterministic actions `U_a:X→X`, a finite word `w=a₁…a_j`
has `U_w=U_{a_j}∘…∘U_{a₁}`. A finite horizon `H` and output family `t_i`
give the target coordinates `F_H(x)=(t_i(U_w(x)))_{|w|≤H,i}`. These are
model-predicted counterfactual branches, not one observer's recorded history.
Our theorems apply to any such finite target family. They do not license
source resets or physical execution of all branches.

**Types kept distinct:** original source `x₀`; current carrier `U_w(x₀)`;
actual recorded toy event `(owner,word,report)`; ordered history; selected
model maps; possible source alternatives in a report fiber; and unexecuted
counterfactual words. A source label binds a declaration, not external origin.

## 4. Candidate theorem

The following statements quantify over every finite nonempty `X`, every
total report `q`, every total rational `m`-coordinate target `F` with `m≥1`,
and every rational `ε≥0`. They assume the unrestricted rational decoder and
sup norm defined above.

**F46-T1 — exact target radius (CLASSICAL / PROVED LOCAL derivation):**

\[
 R(q,F)=\tfrac12\max_{q(x)=q(y)}\|F(x)-F(y)\|_\infty.
\]

Each fiber's coordinatewise midrange is a minimizing decoder. A maximizing
same-report pair and one coordinate give a two-source obstruction to any
error bound smaller than this radius. `R=0` iff every coordinate factors
through `q`, recovering the existing finite exact factorization criterion.

**F46-T2 — representation invariant and feature monotonicity (PROVED LOCAL):**
bijections relabeling `im(q)` preserve `R`. If `q'=g∘q`, then
`R(q',F)≥R(q,F)`. Adding any feature gives `R((q,h),F)≤R(q,F)`.
Larger finite target horizons cannot reduce the radius. These statements
do not imply action descent of the current representation.

**F46-T3 — minimum tolerance-repair alphabet (CLASSICAL / PROVED LOCAL):**
form the graph on `X` with an edge `{x,y}` exactly when

\[
 q(x)=q(y)\quad\hbox{and}\quad\|F(x)-F(y)\|_\infty>2ε.
\]

Then `R((q,h),F)≤ε` iff `h` properly colors this graph. The minimum extra
alphabet size is exactly its chromatic number. If a fixed-width digital
feature is freely available, its minimum payload length is
`ceil(log₂ χ)` bits; this excludes source/basis/provenance/physical costs.
The encoder is a full-state mathematical feature, not a transmitter with
less information. Sup-norm interval geometry is a load-bearing hypothesis.

**F46-T4 — exact canonical repair and minimal tolerant obstruction (PROVED LOCAL):**
at `ε=0`, `(q,F)` is the coarsest refinement of `q` admitting exact target
decoding, up to relabeling. At positive tolerance no such coarsest
refinement need exist. With three states, constant `q`, scalar target
`F=(0,1,2)`, and `ε=1/2`, partitions `{{0,1},{2}}` and `{{0},{1,2}}`
are both optimal two-symbol repairs and incomparable. No repair is coarser
than both. Three is the minimum source cardinality for this phenomenon.

**F46-T5 — self-boundary identifiability (CLASSICAL / PROVED LOCAL):**
`b=\bar b∘q` iff `R(q,b)=0`. If a report fiber contains both labels,
`R(q,b)=1/2`, so no real-valued estimate can attain an error strictly below
`1/2` on that fiber. If all legal future reports alias such an opposite-label
pair, no deterministic finite transcript policy in that grammar decides
`b` on all sources. This is source/target/toolkit-relative, not a theorem
that an actual person lacks a self or that mathematical truth is relative.

**F46-C1 (REFUTED):** tolerance repairs always have a unique coarsest
partition. Receipt: the three-state T4 witness.

**F46-C2 (REFUTED):** the pair-conflict graph suffices for every target norm.
Receipt: the rational Euclidean triangle in §6.

**F46-C3 (REFUTED):** the midpoint radius also certifies a source-realizing
reconstruction. Receipt: a two-source scalar field with image `{0,2}`.

## 5. Proof attempt

**T1.** For any same-report pair and any decoder, the triangle inequality
gives `||F(x)−F(y)||∞≤2L`. Thus the stated right side is a lower bound.
In a fiber `C`, let `l_i=min_C F_i` and `u_i=max_C F_i`. The rational
midpoint decoder `d_i(C)=(l_i+u_i)/2` has coordinate error at most
`(u_i−l_i)/2`. The largest coordinate range over all fibers equals the
largest same-fiber sup-norm pair distance. This attains the lower bound.
The finite extrema exist, including zero-width fibers. Zero radius is
coordinatewise constancy; the decoder then has exactly the target values.

**T2.** Relabeling changes no fiber. Coarsening unions fibers, so the maximum
same-fiber distance cannot decrease. Refinement splits fibers, so it cannot
increase. Appending target coordinates cannot decrease a sup norm. These
are order statements on information and the specified target family;
arbitrary target changes or nonlinear unit changes are not invariances.

**T3.** Same `(q,h)` fibers must have all pair distances `≤2ε` by T1. This
is equivalent to giving different colors to every graph edge. Conversely,
a proper coloring leaves only such bounded-diameter fibers, and their
midrange decoder attains `≤ε`. Minimization over all colorings gives `χ`.
Colors can be reused in different old-report fibers because `q` is already
known. This counts side symbols, not total joint-report classes.

**T4.** For exact decoding, any sufficient refinement `r` has maps
`q=α∘r` and `F=β∘r`, hence `(q,F)=(α,β)∘r`; this proves its universal
coarseness. In the tolerant example each adjacent pair has range one,
radius `1/2`; the full triple has range two, radius one. Any partition
coarser than both repairs identifies `0~1~2` and is the invalid full
triple. The sole graph edge is `{0,2}`, so two colors are necessary and
sufficient. With one source there is one partition. With two sources,
either `q` already separates them, or the merged block has radius `≤ε`
and is coarsest, or it fails and only the separated partition works. This
proves minimal cardinality without extrapolating a finite search.

**T5.** Boolean fiber ranges are zero or one. T1 gives the zero/half split.
For the transcript claim, take opposite-label states with identical reports
for every legal word. A deterministic nonanticipatory policy chooses the
same first action on both; induction on the shared transcript gives the
same next action, outcome, and stopping decision at every finite step.
Its terminal label is therefore wrong on at least one source. Choosing a
new grammar, a source promise, or another target invalidates the hypothesis
and may repair the obstruction. No physical supertask is involved.

These are paper proofs plus exact checks, not Lean proofs. The derivations
and the probe share this investigator and model definitions, so they are
not independent reasoner bearings. The exhaustive search uses independent
optimization routes (midranges, pair bounds, decoder enumeration, and
feature-partition enumeration) but not an independent external source.

## 6. Crucible

Preregistered pass conditions: midpoint loss equals the pair lower bound;
enumerated scalar decoders attain that bound; feature-repair optimization
equals independent proper-coloring optimization; zero-radius answers match
the existing `FiniteField.factor` checker. A disagreement fails the probe
with its assertion and exit code. Negative candidates below must fail their
specified inference, rather than being erased from the success summary.

The probe exhausts every 1–4-state binary report and scalar target table
with values in `{0,1,2}`, at `ε∈{0,1/2,1,3/2}`. Separate fixed-seed rational
two-coordinate cases rotate target dimension, units and source size. These
bounded checks support implementation, while §5 supplies the universal proofs.

* **Dynamic hidden feature:** `X={0,1}²`, `q(a,b)=a`, `U(a,b)=(b,a)`.
  Current target `a` has radius zero; target `(a,b)` representing the
  current and next report has radius `1/2`. Extra feature `b` repairs it.
  Current perfect prediction does not imply future report descent.
* **Complete feature factorial:** for target `a XOR b`, radii under no
  features, `a`, `b`, and both are respectively `1/2,1/2,1/2,0`. The mixed
  risk difference is `−1/2`; joint gain is non-additive. Target `a+b` gives
  `1,1/2,1/2,0` and mixed difference zero. Duplicating feature `a` for target
  `a` gives `1/2,0,0,0` and mixed difference `+1/2`; this is redundancy.
  All four cells are computed from one model table. They are not four
  independent observations, and no mixed difference proves a mechanism.
* **Boundary alias:** constant report and identity dynamics on two sources
  with `b=(0,1)` leave boundary radius `1/2` at every modeled horizon.
  A constant target has radius zero under the same report. Toolkit survival
  therefore does not choose the semantic boundary or authenticate its origin.
* **Noncanonical repair:** the three-state T4 witness keeps both optimal
  partitions and the invalid common coarsening in the receipt.
* **Euclidean geometry mutant:** points `p₀=(0,0)`, `p₁=(2,0)`, `p₂=(1,2)`
  at `ε=6/5` have all pair distances `≤2ε`: their squared distances are
  `4,5,5≤144/25`. Yet no Euclidean decoder attains `ε`. Weights
  `(5/16,5/16,6/16)` have barycenter `c=(1,3/4)` and
  `Σ λ_i||p_i−z||²=25/16+||z−c||²>36/25=ε²` for every `z`.
  Thus pair compatibility is insufficient. General norms/allowed centers
  require feasible subsets or hypergraphs, as the primary coding paper
  motivates. The sup-norm decoder on these points instead attains radius one.
* **Decoder-range mutant:** constant report, scalar source values `0,2`.
  Free rational estimates attain one at the midpoint `1`; a decoder
  restricted to the source image `{0,2}` has minimum loss two. The theorem
  is an estimation bound, not a source-realization theorem.
* **Actual source adapter smoke:** the existing bounded phenomenology
  example integrates arithmetic through horizon three. Thin reports alias
  shadow targets `6,12`, giving laboratory numeric-target radius three;
  its distinct path signatures give radius zero on this two-target model.
  Both targets remain shadows. This is executed current code on a synthetic
  model, not actual observation of either target by that arithmetic observer.

## 7. Verdict

| Subclaim | Verdict / status | Receipt or derivation | Boundary / next falsifier |
| --- | --- | --- | --- |
| T1 target-relative exact radius | SURVIVES / CLASSICAL, PROVED LOCAL derivation | §5 pair lower bound + attaining midpoint; exhaustive decoder oracle | Change the allowed decoder set or norm; counterexamples already retained |
| T2 information order and relabeling | SURVIVES / PROVED LOCAL | Fibers and §5; seeded rational invariance checks | Unsourced target-coordinate or unit changes are not covered |
| T3 minimum extra alphabet | SURVIVES / CLASSICAL, PROVED LOCAL specialization | §5; exhaustive independent color and repair oracles | Physically unavailable feature; general norm; partial encoder knowledge |
| T4 exact/tolerant distinction | SURVIVES / PROVED LOCAL | Three-state witness and all ≤2-state proof | Identify another tolerance geometry admitting a canonical repair |
| T5 selected boundary recovery | SURVIVES / CLASSICAL, PROVED LOCAL | Boolean radius and shared-transcript induction | New genuinely accessible boundary discriminator or source promise |
| C1 unique tolerant repair | FAILS / REFUTED | Two incomparable optimal repairs | Restrict to exact decoding or add a justified choice criterion |
| C2 every norm has graph repair | FAILS / REFUTED | Rational triangle squared-distance certificate | Hypergraph of subsets admitting an allowed center |
| C3 radius certifies actual source field | FAILS / REFUTED | `{0,2}` constrained decoder | Source-realizing decoder class and its own optimal-recovery proof |
| Psychological self/brain mechanism; source authentication | BLOCKED / not established | No empirical instrument, population data, or authenticated source | Independent empirical contact and a falsifiable measurement contract |

The local statements are ready for independent crucible, not automatically
promoted into the shared claim ledger. Scientific priority remains unassessed.

## 8. Remaining obstruction

The smallest obstruction to an error cap is two source states with the same
report and target gap exceeding `2ε`. That pair is a mathematical witness
within the complete declared source class. It is not an observer's freely
available empirical measurement of the hidden states. F46-T4 additionally
isolates the smallest obstruction to *canonical tolerant repair*: three
states with a nontransitive tolerance relation. A search can choose a
minimum repair, but cannot infer that its arbitrary tie-break is a unique
semantic boundary.

For dynamical claims, all-word exact sufficiency is already treated by the
repository's action congruence results. A bounded-horizon radius does not
by itself prove infinite-horizon sufficiency; genuine completeness or the
existing stationary finite-source closure theorem is needed. Multiple
source-changing experiments cannot be freely joined without actual lawful
history/source transport. Noise, source incompleteness, source-realizing
decoders, adaptive feature costs and empirical self-boundary identification
remain outside the proved contract.

**TLICA coordinates, without a merged score:** κ/contact is actual recorded
causal acquisition and is absent for unexecuted feature maps; φ is the
specified report/action toolkit's inability to discriminate source pairs;
σ is the declared source/target/action map and its independent correctness
obligation; ρ is commitment to a selected semantic boundary or favored
repair, not numerical radius or evidence; μ is which discriminating actions
are feasible and actually scheduled. `R` quantifies reconstruction under
the fixed mathematical model only. Neither `R=0` nor small factorial
residuals establish κ, σ, or low ρ. No phase transport is declared or used.

The next strongest probe changes a load-bearing assumption: require an
actual realizable field decoder, or require the new feature to be obtained
by a legal one-carrier action. The retained scalar and dynamic witnesses
already separate the unrestricted mathematical repair from those stronger
contracts. This round stops at the proved radius and the minimal countermodel.

## 9. Cross-domain connection with actual maps

**Finite field → reconstruction:** map each existing `FiniteField` source
state `x` to its selected probe tuple `q(x)` and to its rational target
tuple `F(x)`. At `R=0`, the midpoint decoder is a true factorization
`F=d∘q`; the probe checks each scalar factor with the existing verifier.
At `R>0`, that square does not commute: a maximizing pair supplies the
explicit defect. Renaming targets does not hide it.

**Controlled dynamics → future field:** with the two-bit swap above,
`F₁=(q,q∘U)=(a,b)`. The coarse square would need
`q∘U=V∘q`. States `(0,0),(0,1)` have equal `q` but different `q∘U`, so
no such `V` exists. Repaired report `r=(a,b)` has the actual transition
`V_r(a,b)=(b,a)` and `r∘U=V_r∘r` on every source. This is an exact
dynamical map, not a metaphor for psychological change.

**Two observers → joint semantics:** maps `q_A(a,b)=a`, `q_B(a,b)=b` give
the common-source joint map `j=(q_A,q_B)`. For `t=a XOR b`, the decoder
`d_j(a,b)=a XOR b` gives `t=d_j∘j`; neither `q_A` nor `q_B` admits a
target decoder. When the two reads are actual nondestructive same-source
events, their lawful joint receipt can support this factor. Opposite
counterfactual branches or merely identical source labels cannot substitute
for that joint receipt. This is deterministic target synergy, not mutual
information, quantum entanglement, or source authentication.

**Identity commitment → target, not carrier equivalence:** a declared
boundary `b` pulls back through a genuine source bijection `h:X→X'` as
`b'=b∘h⁻¹`; with `q'=q∘h⁻¹`, radii and exact boundary membership agree.
Without the source map, matching report strings admits both equal-boundary
and opposite-boundary source interpretations. The constant-report two-source
witness checks this failure of untyped identity transfer.

## 10. Deliverables

* `F46_MATHEMATICAL_PHENOMENOLOGY.md`: definitions, complete elementary
  proofs, source provenance, prior art, negative controls, and verdicts.
* `F46_PROBE.py`: standard-library-only exact `Fraction` instrument;
  enumerated decoder/color/partition controls, bounded current-code smoke,
  fixed-seed separate rational cases, and receipt replay.
* `F46_RECEIPT.json`: raw source bindings, computational scope, exact
  witnesses, per-control statuses, run command/exit evidence, and resource
  usage. A REFUTED candidate is preserved even when the instrument passes.

Run from repository root:

```sh
timeout 25s python research/2026-10-13/SWARM_ATLAS/F46_PROBE.py --write research/2026-10-13/SWARM_ATLAS/F46_RECEIPT.json
timeout 25s python research/2026-10-13/SWARM_ATLAS/F46_PROBE.py --verify research/2026-10-13/SWARM_ATLAS/F46_RECEIPT.json
git diff --check
```

The probe enforces a 256 MiB address-space cap and a 20-second CPU cap.
No full test suite, compiler, CI, external empirical experiment, push,
release, default change or historical rewrite was performed in F46.
The repository's required integration validations remain the principal's
separate gate; this bounded contribution does not claim them passed.
