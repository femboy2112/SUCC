# CARRIER-FIRST SUCC — source-indexed lawful history unification

**Date:** 2026-10-13. **Starting point:** completed Mathematical Atlas PR #50 at
\`759c30c72a2927212cdbfa41365800da96e5d515\`.
**Research branch:** \`research/carrier-indexed-unification-2026-10-13\`, draft PR #53.
**Status:** conditional finite source theorem architecture, explicitly tested,
with a standalone Lean 4.14 deterministic naturality/core proof. Stochastic
all-history identity is derived by exact finite reindexing, tested independently;
the entire Python implementation is NOT mechanically refined to Lean.

## 0. What we noticed

The repository ALREADY HAS the physical-carrier vocabulary and mathematical
source contracts: \`Frame\`, \`Engine\`, \`ControlledCarrier\`,
\`LawfulSource/HistoryFiber\`, and
\`StochasticInstrument/StochasticHistory\`. Replacing these with a completely
new "universal sheaf" would add another disconnected representation.

The correct next object is an **original-source-indexed carrier**, with a
lawful collection of mathematical perspectives over it. A carrier is the base
of the mathematics, not merely a report projected out of some new category.

This is a bridge, not a rewrite. We retain the original math and provenance
and explicitly distinguish:
- S — original source/preparation labels, never overwritten by measurement;
- C_h — the currently altered carrier after ACTUAL history h;
- A_h — actions permitted by the current source/instrument contract;
- K_a(c;z,c') — a complete JOINT outcome/next-carrier probability law;
- J_h(s,c) — an UNNORMALIZED source-indexed joint law, conditioned only
  by retaining the actual event trace without erasing its likelihood;
- a history receipt h — ordered actual actions and observed outcomes;
- E — the observer's model and possible unperformed alternative histories.

The original mathematical carrier labels do not provide an observer with
a physical instrument for reading the hidden original or authenticating the
source. Source ID, \`basis\`, \`epoch\` and types are software declarations.

## 1. The carrier object

For finite original and current sets S and C_0, a declared preparation is
a nonnegative normalized joint law

\[
J_\varnothing:S\times C_0\longrightarrow \mathbf Q_{\ge0},
\qquad \sum_{s,c}J_\varnothing(s,c)=1.
\]

A lawful instrument on a given current stage is a normalized row-wise
joint kernel
\[
K_a(c;z,c')\ge0,\qquad \sum_{z,c'}K_a(c;z,c')=1,
\]
with an explicit enabledness predicate. It need not be deterministic,
reversible, nor preserve state cardinality. Basis/source/epoch contracts
prevent implicit crossing of carrier spaces.

For an actual receipt z of an authorized action a, define

\[
\boxed{
J_{h\cdot(a,z)}(s,c')
=\sum_{c\in C_h}J_h(s,c)K_a(c;z,c').
}
\tag{CAR1}
\]

The sum \(\sum_{s,c'}J_{h\cdot(a,z)}\) is the **joint probability of the
entire actual receipt history**, not necessarily 1. Normalization is
performed only on a positive-probability event. If receipt mass is zero,
the model declares the event impossible rather than inferring arbitrary
original truth ex falso. A named action is executable only if enabled
for every CURRENT state with positive probability; otherwise an action
menu itself would become an undeclared hidden-state sensor. Alternative
physical access models require a separate explicit contract.

This representation never edits s. Source-current correlation is load
bearing: the marginal distributions on S and C can be identical for two
different joint laws while their next original-source posteriors disagree.

## 2. All-prior carrier descent and naturality theorem

Let q:C→D and q':C'→D' be complete current-state quotients; the ORIGINAL
source index is preserved exactly. Then the coarse joint instrument exists
with the correct original/source-history semantics for **every admissible
original-indexed prior** iff these two gates hold:

1. **Access:** enabled_a(c) is constant on every q-fiber.
2. **Joint report/carry law:** whenever q(c)=q(d) and both actions are
   enabled, for every receipt z and every coarse next state v,
\[
\sum_{c':q'(c')=v}K_a(c;z,c')
=
\sum_{c':q'(c')=v}K_a(d;z,c').
\tag{CAR2}
\]

Define the common value as \(\bar K_a(q(c);z,v)\). Within a disabled
fiber, unused joint row values are unobservable and need not agree,
but the enabled flag must descend. No hidden action can be run there.

**Sufficiency (finite exact reindexing).** For each original s, receipt z,
and next coarse carrier v:

\[
\begin{aligned}
q'_*J_{h a z}(s,v)
&=\sum_{c':q'c'=v}\ \sum_c J_h(s,c)K_a(c;z,c')\\
&=\sum_{u\in D}
   \left(\sum_{c:q c=u}J_h(s,c)\right)
   \bar K_a(u;z,v)\\
&=\bar K_a^{\,z}(q_*J_h)(s,v).
\end{aligned}
\tag{CAR3}
\]

The first and last expressions are UNNORMALIZED and retain the same s;
hence the total receipt evidence and the posterior on ORIGINAL s
match exactly whenever evidence has positive mass. If a subsequent
action is selected only from common public history and each new square
is lawfully checked, induction gives equality of all finite actual
adaptive history laws (including path evidence) and original target
proof support. Only paths actually instantiated are called actual.

**Necessity for all priors:** take Dirac original/current preparations
concentrated separately on c and d in the same q-fiber. Any claimed
coarse instrument law must give identical enabledness and joint
(z,v)-report rows for both. A prior-specific weaker condition is not
universal descent.

The implementation is \`audit_descent\`, \`checked_descent\`,
\`CarrierQuotient.push\` and \`transport_actual_history\`; complete
finite source tables and exact Fractions are required. Theorems are
CLASSICAL labelled-kernel lumpability/base-change adapted to an
original-indexed history, not independent mathematical priority.

**Lean scope:** \`formal/EODCS_CarrierIndexed.lean\` kernel-checks the
deterministic total-action specialization: all finite report and
endpoint naturality, original index invariance, original predicate
support/claim preservation and composition of strict carrier
comparisons. It does NOT mechanize the finite rational sum identity
CAR3, the Python access planner, or any empirical source facts.

## 3. Canonical repair must be over THE CARRIER

Given an original current-state report q_0:C→D and one or more declared
future instruments indexed by a, relative to specified future quotients
q'_a, define the ONE-STEP report
\[
q^*(c)=\Big(q_0(c),\big(
  \mathrm{enabled}_a(c),
  [K_a(c;z,v)]_{z,v}\ \mathrm{if\ enabled}
\big)_a\Big).
\tag{CAR4}
\]

This report is the coarsest mathematical refinement of q_0 whose fibers
carry the same enabledness and all supplied future joint rows: its
equivalence is literally the intersection of the corresponding kernels.
Every other source-supported refinement sufficient for those same
comparisons factors CAR4. The new report is NOT necessarily measurable
by a currently authorized physical instrument.

Under a fixed finite complete stationary action menu A:C→C, repeatedly
split the seed partition by receipt/next-block joint-row signatures.
Every strict refinement adds ≥1 current-state class and preserves
previous classes, hence finite termination after at most \(|C|-b_0\)
strict steps. The terminal partition is the coarsest stable refinement:
every adequate congruence must separate each witnessed unequal action
row, hence refine every stage. This is classical strong lumpability /
probabilistic bisimulation on complete finite tables. Unlike the
one-step report, the fixed point is stable under all declared action words.

The code records the action causing each strict split and distinguishes
a grammar-relative repair from an actually available new sensor.

## 4. Three distinct levels of view (a forgetful tower)

1. **Deterministic:** every enabled row is a Dirac probability-one atom
   (receipt,next current state).
2. **Relational support:** retain ONLY the positive-weight atoms. This
   preserves possible action paths and enabledness, and existential
   path composition under nonnegative weights.
3. **Stochastic:** retain the FULL joint receipt/next-current law,
   exact rational weights, and their original-indexed history effect.

The forgetful map stochastic→support is generally NOT invertible.
Same support with likelihood 1/4 versus 3/4 gives different evidence.
Matching receipt marginal and current-state marginal separately also
does not identify their joint law. For true SUCC proof transport,
the source must supply the correct layer of structure.

\`forget_probabilities\`, \`possibility_descent\` and
\`compose_possibilities\` provide a typed implementation, with
independent positive-support composition oracles.

## 5. Bridge to the existing mathematics; not a replacement

- **F48 / \`swarm_lawful_history.py\`:** source labels, original/current
  configurations, actual event-prefix replay, and uniform-action
  check. The adapter takes an EXPLICIT source prior; it does not assume
  equal original-source probability or forge a reset. Prefix support
  agrees under the common safely-enabled subset.
- **C17 / \`swarm_probability.py\`:** exact source joint preparation and
  \`StochasticInstrument\` are adapted without changing original indices;
  event/evidence/posteriors are compared independently. Conversion
  from a history with recorded past events is deliberately rejected
  until a separate receipt-preserving checkpoint interface exists.
- **A06 / \`swarm_categories.py\`:** the action-stable equivalence
  coreflection is the deterministic special case of the dynamic
  partition refinement; our finite stochastic version must use full
  probabilistic row signatures.
- **VOYAGER / topology:** a completed profile is a mathematical ideal,
  not a carrier stage or an original preparation magically realized.
  The carrier history space needs its own compactness, continuity,
  source-class and resource hypotheses before any inverse-limit theorem.
- **Cambrian PR #51:** joint report/receipt stochastic source descent
  and a finitely branching changing-history realization theorem are
  complementary to this runtime adapter, and must be reviewed and
  selectively imported during later consolidation.
- **EOS PR #45:** a parallel Lean 4.19 grammar/evolutionary line that
  must not silently overwrite Lean 4.14 or the inherited claim ledger.
- **Ongoing PR #49:** an actively changing swarm, NOT the immutable
  completed PR #50 parent. Its unmerged original child commits and
  registry are live work and require deliberate freeze before promotion.

## 6. Hostile controls and falsification opportunities

Finite independent tests:
- 180 seeded 4→3-state joint kernels with an independently implemented
  atomwise source-original reindexing oracle, including impossible
  receipts and full correlation distinctions;
- 90 independent four-state complete partition enumerations validating
  uniqueness of the coarsest stationary stable repair;
- two-stage destructive source history showing matched exact path
  likelihood, supported original labels and original-source posterior;
- real adapter agreement with F48 deterministic actual original-support
  replay and C17's independent unnormalized stochastic derivation;
- availability mismatch must not silently become a source observation;
- equal positive support but unequal weights is a STRICT negative;
- equal separate report and next-state marginals can still conceal
  opposite correlations;
- malformed/stale source, basis, epoch, float/negative probabilities,
  forged history, duplicate action names, impossible event, forgotten
  receipt and unowned sensor attempts all fail closed.

The final count, explicit CI SHAs and frozen cross-version deterministic
receipt must be checked at the final branch head before claiming success.
Python simulation is not a general physical-source or analytic proof.

## 7. What still needs proof

**CAR-H1:** General kernel-checked stochastic CAR3 with the correct
source-indexed finite-sum law, not merely deterministic naturality.

**CAR-H2:** Source-changing stages whose available action menu itself
changes, preserving original-state proof support and the right
history-dependent conditional probability over all *legal* adaptive
policies, not only a selected path.

**CAR-H3:** A genuine sheaf/site theorem for lawfully concurrent and
reorderable event histories; destructive incompatible experiments
are the mandatory counterexample. Merely naming a fibration is
insufficient to prove gluing.

**CAR-H4:** A physically meaningful access/cost semantics: one
nonresettable carrier, declared preparation leases, empirical source
calibration, energy/time and counterfactual histories; exact finite
model cost is not real time.

**CAR-H5:** Source-changing relational/quantum/continuous/analytic
history integrations with actual measure-theoretic or CPTP channel
hypotheses. The current finite calculation cannot be promoted to a
Weil/Suzuki operator or RH sign identity.

**CAR-H6:** Consolidate completed #50 with independently proved
Cambrian #51 and the eventually frozen rolling swarm #49, deduplicate
F41 #52 and keep EOS #45's formal pin separate, without corrupting
the original research source/provenance.

**Verdict:** The carrier already is the common mathematical host;
the remaining unification problem is to certify which observation,
history, quotient, probability, topology and proof structures are
lawful **over the same source-indexed carrier**. The local theorem
and executable model close an important conditional composability
edge, not the entire flagship sheaf/physical theory.
