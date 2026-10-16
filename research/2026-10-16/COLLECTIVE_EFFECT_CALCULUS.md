# Collective observer effects and the provenance/permission distinction

Status: **PAPER PROVED within the finite declared model; exact implementation
tests; not a Lean metatheorem or physical realization certificate.** This is an
additive interpreter over `source_lambda.py`, pinned by the integration manifest.
The original simply typed language and its public interfaces are preserved.

## Judgment and the work performed by the indices

Write `Gamma; C |- e : tau ! (k, O, g, U)`. Here C contains a source passport
`(identity, epoch, basis)`, a declared realized action path and an immutable
recording registry. `k` distinguishes recorded replay, mathematical derivation,
latent program, prediction, testimony, analytic import and exact finite check.
O is the set of recording origins, g is a vector of effect-execution counts and
U is the set of undischarged obligations. Composition takes union of O and U
and componentwise addition of g. These operations are associative with empty
units. Counts of replays and cardinality of O are different quantities; neither
is a count of independent experiments. The interpreter performs zero physical
measurements.

Every output also contains its immediate earlier dataflow references and a
separate set of **read capabilities**. Only replay of an admitted event gives
that capability; testimony can transfer it. Derived outputs retain provenance
without retaining raw-read capabilities. This conservative language can reuse
raw reports and compose all computations in one lambda term; it does not yet
have a general, capability-safe binder for arbitrary compressed derived values.
That is an explicit expressiveness restriction, not an impossibility theorem.

The pure lambda fragment retains de Bruijn binding, lexical closures, latent
read sets in function types and lazy branch selection. `Derive` executes the
actual checked term against only the permitted recording rows. A function or a
pair containing a function is a latent program, never a completed measurement.
Applying a function pays for its body reads. Static potential effects can
include unexecuted branches; actual recording origins are computed from the
executed reads.

`Predict` executes against an explicitly hypothetical atlas, carries
`COUNTERFACTUAL_NOT_RECORDED`, and cannot be coerced into testimony or readings.
`AnalyticImport` preserves all named premises, adds proof-replay and
source-identification debts, and never issues a theorem certificate.
`ExactQuadratic` reuses the actual rational signed-witness checker; the fact
that a finite matrix has a negative direction does not identify it with Suzuki.
Imported debts survive even through subsequent exact finite calculations.

## Finite preservation theorem

Assume the supplied finite registry faithfully describes the declared source,
and its path is an actual path of the separately supplied apparatus model.
These are premises, not consequences of a matching source string. Every
successful closed program has the following properties:

1. Every artifact passport is exactly C's passport. Every primitive origin is
   an existing event with that passport whose history is a prefix of C's path.
2. Every recipient obtains an event's raw reading only through replay by its
   declared origin or an explicit chain of transmissions from a holder.
3. Derivation creates no recording origin; prediction and latent code create
   none; transmission preserves origins and causal parent edges.
4. Every unresolved assumption on a dependency path remains in the resulting
   analytic or exact-check artifact. No constructor promotes an imported
   statement to a replayed Lean theorem or a global analytic conclusion.
5. A frozen-source registry rejects conflicting values at one modulus and
   rejects incompatible congruences. Unperformed reads, foreign epochs,
   non-prefix histories and references to future outputs fail.

Proof: induction on the finite command sequence. Replay checks the registry,
passport, history and origin. Relay checks an already constructed artifact and
sender membership; it copies origins, debts and capabilities without creating
any. Derive builds an atlas only from the input read capabilities, checks
sender membership and calls the finite lambda evaluator. Its report operations
preserve passport; its numerical operations return mathematical values, not
new source recordings. The remaining cases have the explicit debt unions
above. Every dataflow reference decreases the command index, so induction
also proves transitive preservation, not merely immediate-edge preservation.

For the higher-order lambda sublemma, use the standard logical relation:
ground values agree at their checked type; paired values agree componentwise;
related closures send related arguments to related results when the recorded
atlases agree on their latent reads and both executions terminate within fuel.
The variable case uses related environments, abstraction extends them,
application uses the closure relation, and each finite primitive is a
deterministic typed operation. Select takes the same branch on related Boolean
conditions. This proves preservation and observation equivalence for the
admitted evaluator. Fuel exhaustion is unresolved execution, not falsehood.
The Python implementation has tests, not a formal verification of this proof.

## Source change and miniature actions

`miniature_action` invokes the real `MiniPort.validate` / MATRYOSHKA factor
checker. Its expanded parent word must be defined for **all** surviving states.
It consumes a named capability in the successor model state and conservatively
increments the current epoch; the original passport is retained separately.
Old-epoch readings cannot become readings of the new source. Output is a
possibility set and a finite transition receipt, not a measured hidden state.

The model state is immutable and may be reused to explore counterfactual
branches. This is not a linear physical resource manager. To combine branches
into an actual claim requires the chronological planner's single policy tree
and replay proof. Two calls from the same old state do not establish joint
execution. Action identity, legality and observation must be specified in the
apparatus model; source labels do not establish calibration or causality.

## Counterexamples that determine the contract

**Provenance is not decoder authority.** B reads x modulo 3 and sends only the
Boolean `[x=0 mod 3]` to A. At x=1 and x=2 the message is identical. If A may
follow the message's origin identifier into B's raw tape, it distinguishes
these sources without performing or receiving the required read. The first
design that reconstructed tapes from origin sets had this flaw; the separate
`readable_events` field repairs it. The regression explicitly retains the
origin in the Boolean message while refusing A's attempted read(3).

**Replay is not independence.** Eight replays and arbitrarily many relays of
one event leave one origin. They do not generate eight physical experiments.

**Closures are not results.** `lambda _:Bool. read(7)` compiles and produces no
read. Applying it without the event fails. Transmitting the closure as a
measurement is rejected.

**Derived CRT is not a new primitive event.** From lawful mod-2 and mod-3 rows
one can compute a mod-6 report. This does not authorize an unrecorded primitive
`read(6)` or introduce an Euler impulse at 6.

**Mutually exclusive histories.** Events at paths `(left)` and `(right)` cannot
both be admitted under either realized path. Prefix histories `(first)` and
`(first,second)` can be combined under the latter, subject to frozen-source
consistency. The effect registry alone does not prove those paths physically
realizable; the action-table contract and planner supply the finite-model gate.

**Imported sign debt persists.** An open spectral-tail lemma, followed by an
imported consequence and an exact negative two-dimensional matrix witness,
still carries the original open lemma and source-identification debts. It is
not a negative original-Weil witness.

## No-new-distinction theorem

If two source histories give identical admitted primitive reports, identical
public capability/legality information, and identical lawful transitions at
every reachable prefix, every deterministic finite admitted program has the
same output signature on them. Apply the logical relation above at each
command. Data processing, testimony, miniature factor maps and analytic
consequences of common premises cannot refine that equivalence. A new joint
probe can refine it only if its actual source table does. A causal access
change can refine it only through a newly reachable lawful experiment.

The legality hypothesis matters: a source-dependent action menu is itself an
observation if its availability is publicly detectable. Ignoring that side
channel invalidates the no-go theorem. Randomness independent of the source
does not repair indistinguishability: couple equal random tapes and apply the
same induction, then average.

These are classical information-flow and logical-relation ideas integrated
into SUCC's source/event contracts. No academic originality is claimed.
