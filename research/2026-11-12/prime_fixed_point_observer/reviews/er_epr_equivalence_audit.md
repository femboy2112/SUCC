# ER=EPR refinement: shared carrier, chosen messages, and exact output equivalence

**Status:** primary-source audit, elementary finite channel proofs and exact
countercontrols. Physical identification of the arithmetic carrier with a
gravitational spacetime remains UNVERIFIED. The earlier source files are
unchanged. This audit uses the same model family as the main construction;
it is not independent experimental confirmation.

**Operational scope:** the coherent-coupling/measurement-and-message
equivalence below holds for the receiver's current marginal. If the
meeting comparator receives both quantum outputs, a joint present
measurement can distinguish those implementations.

## 1. Faithful interpretation of the new proposal

The user proposes that what appears externally as carrier defects or
wormhole endpoints might be the same larger connected system that the
twins experience internally. On that reading, the twins' apparently
separated descriptions could be coordinated by one coherent underlying
carrier. This is a meaningful dual-description hypothesis. It should be
tested by an explicit dictionary between states, observables, operations,
and accessible outputs rather than rejected merely because its two
descriptions use different language.

The phrase "share information freely" has two operational readings:

- **Shared preparation/coherent coordination:** the joint state and allowed
  dynamics maintain correlations that become observable in the declared
  comparison. No independently chosen new message has yet been transferred.
- **Chosen-message transfer:** after preparation, the left observer can
  choose an input and thereby change a present distribution accessible
  to the right observer before their ordinary meeting.

They require different channels. The second can exist in a connected
carrier, but its interaction and causal resource must be included in both
descriptions. Calling it a wormhole does not remove that requirement.

The direct comparator still sees only present outputs. An eventual
meeting is an additional interaction event; it does not grant retrospective
access to incompatible historical coordinate records.

## 2. What the primary ER=EPR sources actually support

### Maldacena--Susskind: exterior separation and an interior meeting

[Maldacena and Susskind, arXiv:1306.0533v2](https://arxiv.org/pdf/1306.0533),
Introduction and Sections 3.1--3.4, distinguish the semiclassical
two-black-hole setting from the broader conjecture about general
entanglement. Section 3.1, printed page 16, preserves the absence of
signalling between exterior regions through the original bridge.
Crucially, Section 3.4 and Figure 10, printed pages 18--19, explicitly
allow suitably timed infalling observers from opposite sides to meet
in the interior. The timing can also prevent a meeting. This supports
the shape of the user's two-walker picture without making an exterior
communication wire available. The proposed bridge for an arbitrary
entangled particle pair is described there as a conjectural, highly
quantum object, not a supplied smooth classical metric.

### Gao--Jafferis--Wall: communication requires the specified coupling

[Gao, Jafferis and Wall, arXiv:1608.05687v3](https://arxiv.org/pdf/1608.05687),
Introduction, equation (1.2), and Section 5, study an explicit interaction
coupling the two boundaries. In their eternal BTZ/AdS setup it induces
negative averaged null energy; gravitational backreaction opens a
traversable window. The construction includes its scalar-field boundary
conditions, the coupling's turn-on and sign, and a perturbative gravity
calculation. It does not obtain traversability from an entangled state
alone. The interaction also matters to the causal accounting. Section 5,
printed pages 14--15, relates the construction to a dynamically resolved
teleportation protocol. These are conditions of that physical model, not
properties established for the SUCC arithmetic carrier.

### Maldacena--Stanford--Yang: an exact restricted output equivalence

[Maldacena, Stanford and Yang, arXiv:1704.05333v1](https://arxiv.org/pdf/1704.05333),
Section 2.1.1, equation (2.3), printed pages 4--5, shows that a coherent
two-sided coupling can be replaced, for the receiver's marginal, by
measurement of the control observable, transmission of the outcome, and
the corresponding unitary on the receiver. The authors explicitly
distinguish that equality from equality of the global final states.
Section 2.2, equations (2.4)--(2.5), tests response to an intervention by
a cross-boundary commutator. Section 2.5, printed pages 12--13, supplies
parametric information-transfer bounds within the stated approximation;
it does not claim an unlimited-capacity channel or exact universal constants.

The differing descriptions are therefore a real opportunity: in a
specified holographic model, a boundary protocol and a bulk transit can
describe corresponding physics. The published examples retain preparation,
interaction, timing, access, and information costs. The mathematical task
is to reproduce such a correspondence for the proposed carrier.

## 3. The smallest nontrivial output-equivalence theorem available here

Let `A,B` be finite-dimensional systems. Choose mutually orthogonal
projections `P_j` on `A` with `sum_j P_j=I`, and unitaries `V_j` on `B`.
Then

\[
U=\sum_jP_j\otimes V_j
\]

is unitary. Compare the coherent implementation `rho -> U rho U*` with
the outcome-forgotten measurement-and-control implementation

\[
\mathcal M(\rho)=\sum_j(P_j\otimes V_j)\rho(P_j\otimes V_j^*).
\]

The latter requires the outcome-dependent action on `B`; if the parties
are separated, the classical outcome must reach that controller.

**ERE-01 — CLASSICAL / PROVED LOCAL receiver-channel equivalence.**
For every input density matrix, including any entangled external reference,

\[
\boxed{\operatorname{Tr}_A(U\rho U^*)
=\operatorname{Tr}_A\mathcal M(\rho).}
\]

**Proof.** Expand the coherent output in `j,k`. For `j!=k`, a partial
trace over `A` kills `P_j rho P_k`, since cycling the `A` factors gives
`P_k P_j=0`. The surviving diagonal terms are exactly the second
expression. Tensoring all operations with identity on a reference does
not change that argument. Unitarity of `U` follows from the same
orthogonality and `V_j* V_j=I`.

This is the precise finite operational content underlying the restricted
equivalence in the cited teleportation construction. Its domain is an
entire input channel, not one fitted state. It does not supply gravity.

**Scope countercontrol.** Set `P_0=|0><0|`, `P_1=|1><1|`, `V_0=I`,
`V_1=X`, and start with `|+>_A|0>_B`. The coherent implementation is
CNOT and produces `Phi+`; the measurement-and-control implementation
produces

\[
\tfrac12|00\rangle\langle00|+\tfrac12|11\rangle\langle11|.
\]

The receiver has `I/2` in both. At a later meeting where **both current
quantum outputs** are available, their `XX` expectations are 1 and 0.
Thus they are equivalent for the receiver-only interface and distinguishable
for the joint interface. Keeping an entire measurement dilation coherent
and granting reversible access to its ancillary record can avoid that
discarded-record channel. Such record/access belongs in the resource
model; a classical outcome alone does not restore arbitrary erased input
coherences. Restricted present-output agreement is not full history or
whole-carrier equivalence.

## 4. A chosen-message intervention separates EPR from an added wire

Prepare a fixed Bell pair `Phi+_AB`. After this preparation choose a
message `m in {0,1}` independently of that preparation. Give `m` only
to the left-side controller.

**Entanglement-only experiment.** Permit any trace-preserving local
operation `N_m` on `A` and its private auxiliaries, with no communication
interaction to `B`. The local-channel identity proved in
[BRIDGE_COMMUNICATION.md, BCOM-04](../BRIDGE_COMMUNICATION.md) gives

\[
\rho_B^{(m)}=I/2\quad\text{for both messages}.
\]

Consequently every right-side POVM has identical distributions under
the two interventions. For the explicit encoding `X_A^m`, the joint Bell
state changes but the right marginal does not. The optimal probability
of guessing an equally likely message from that output alone is `1/2`.

**Message-wire experiment.** Add a message qubit `M` initially in `|m>`
on the left and a specified `SWAP_(M,B)` interaction. This unitary
produces

\[
\rho_B^{(m)}=|m\rangle\langle m|.
\]

The right-side `Z` readout now determines the bit exactly. The trace
distance between its two possible current states is one, compared with
zero in the first experiment. The extra wire can be fully coherent; the
distinction is the permitted interaction, not collapse or measurement.

**ERE-02 — PROVED LOCAL operational inequivalence.** No dictionary
preserving the stated preparation, left interventions, right readout and
communication restrictions can equate these two experiments. Their
observable distributions differ. This refutes an *additional free
chosen-message channel* being equivalent to entanglement alone. It does
not refute a duality in which that interaction is mapped to a corresponding
gravitational or boundary interaction.

The same fresh-message probe makes the user's "conspiring twins" precise.
Agreement generated by common preparation is compatible with the first
experiment. Adaptation to newly chosen remote inputs requires the second
kind of resource, or some other specified causal interaction.

### A differential response probe

There is also a local, falsifiable interaction test. Let a Hermitian left
operator `A` encode a small intervention `exp(-isA)` before a joint
unitary evolution `V`; let `B` be a present right observable. Then

\[
\left.\frac{d}{ds}\operatorname{Tr}
\bigl(BVe^{-isA}\rho e^{isA}V^*\bigr)\right|_{s=0}
=i\operatorname{Tr}\rho[A,V^*BV].
\]

The sign follows from the declared `exp(-isA)` convention. If `V` factors
across the two sides, the commutator is zero. A nonzero response proves
an influence for that input and observable; a zero first derivative
does not exclude higher-order signalling or another separating observable.
This is a test of an executed interaction, not of an uncalibrated historical
coordinate comparison. The finite probe includes an exact CNOT witness.

## 5. What an actual dual-description dictionary must preserve

An operational claim should specify the following data before calling
two presentations equivalent:

| Data | Required match |
| --- | --- |
| Preparation and source | Which common state, code subspace, logical inputs and external references are represented. |
| Present observables | A map between the allowed current readouts, with their frame, type and probabilities. |
| Dynamics and interventions | Corresponding channels or instruments for every allowed operation and branch, including coupling controls. |
| Causal access | Which party can actuate or read each register at each event, and which messages can reach it. |
| Composition | The dictionary respects the finite order of interactions, conditional branches and final comparison. |
| Resource budget | Communication, ancillary storage, energy/timing assumptions and computation are recorded; equal output laws alone do not equate their costs. |

A finite sufficient condition is an isometric state encoding
`rho -> J rho J*`, matching effects `E=J*E'J`, and channel/instrument
intertwiners on the code for every allowed finite step. Induction then
matches all permitted finite outcome probabilities. If the representation
is complete on the relevant code and the operational dictionary is
invertible there, this gives the requested operational equivalence within
that scope. A resource claim additionally requires resource bounds on
implementing the dictionary; algebraic equality does not provide them.

Locality need not look identical in both coordinate presentations: a
boundary operation may encode a bulk-local operation in a complicated way.
What must match is the actual permitted capability and its causal/resource
accounting. Requiring the same drawing on both sides would incorrectly
exclude possible dual descriptions; silently adding a capability on one
side would incorrectly assert one.

## 6. The arithmetic antecedent already fixes part of the dictionary

The October 22
[arithmetic thermofield foundations](../../../2026-10-22/ARITHMETIC_ER_EPR_FOUNDATIONS.md)
construct, for `beta>1`,

\[
|\Omega_\beta\rangle
=\zeta(\beta)^{-1/2}\sum_{n\ge1}n^{-\beta/2}|n\rangle|n\rangle,
\qquad H_0|n\rangle=(\log n)|n\rangle.
\]

This supplies an actual normalized arithmetic twin with its stated
infinite-dimensional domain. Its section A8 already proves the no-signalling
identity; its mirrored partial arithmetic inverse is a selected filter
with a success flag, not a deterministic remote message operation.
The [Prime Bridge claim supplement](../../../../docs/CLAIM_SUPPLEMENT_ARITHMETIC_ER_EPR.md)
and the [obstruction synthesis](../../../2026-10-22/ARITHMETIC_HOLOGRAPHY_OBSTRUCTIONS.md)
also retain finite geometric encodings, recovery conditions and the
explicit absence of a derived gravitational spacetime.

The earlier geometric counterexample is especially relevant: a four-output
copy isometry can be implemented on a star or on a binary tree. The
boundary quantum map agrees while selected graph distances differ. One
may regard the implementations as equivalent for that restricted boundary
interface. The boundary map alone does not select a unique physical
metric or complete dynamical spacetime. More observables or assumptions
are needed to make that stronger choice.

Thus the present arithmetic construction already realizes parts of a
state/operator/recovery dictionary. Calling its external algebraic defects
wormhole endpoints is currently an interpretation. To become a physical
identification it must additionally produce the relevant geometric
observables, dynamics, causal response and field-equation regime, with
the same source and access accounting. No arbitrary loop defect or shared
eigenvector establishes those structures by itself.

## 7. Verdict and next discriminating construction

The smallest surviving proposition is:

> Two presentations of the same declared carrier can be operationally
> equivalent on their specified current-output algebra when an explicit
> state, intervention and readout dictionary preserves all permitted finite
> probabilities. A connected interior presentation need not add any
> exterior signalling capability. When a coupling is added, both
> presentations must include its causal and information cost.

This is instantiated nontrivially by ERE-01's receiver-channel equivalence,
with its joint-output failure control. Existing holographic examples
motivate a richer version; the arithmetic gravitational version remains
UNVERIFIED, with a concrete path to test it.

The next useful construction should choose one carrier interaction and
one meeting/output algebra, give the two dictionaries, and test the same
fresh-message intervention in each. If their response or communication
access differs, they are different operational models. If they agree,
record the exact observation class and cost under which that equivalence
has been proved. The remaining gravitational and arithmetic conclusions
retain their separate proof obligations.

The lightweight exact implementation is
[er_epr_intervention_probe.py](er_epr_intervention_probe.py). It tests the
fresh-message distinction, coherent/message-controlled receiver equivalence
on all matrix units of its finite example, a joint-state counterexample,
and the signed response identity. The completed run passed **39 exact
checks, exit 0**; the result and group counts are preserved in
[ER_EPR_INTERVENTION_REPORT.json](../receipts/ER_EPR_INTERVENTION_REPORT.json).
It simulates no wormhole or gravity. Reproduce from the repository root:

```bash
python research/2026-11-12/prime_fixed_point_observer/reviews/er_epr_intervention_probe.py --output research/2026-11-12/prime_fixed_point_observer/receipts/ER_EPR_INTERVENTION_REPORT.json
```

The read-only cross-audit of [BRIDGE_COMMUNICATION.md](../BRIDGE_COMMUNICATION.md)
found its cup/cap normalization, teleportation branch order, inverse
corrections, reference preservation and no-signalling proofs consistent.
Its coherent protocol explicitly supplies the controlled coupling or
syndrome transmission; its classical protocol includes both message bits.
Those are demonstrated channel implementations with stated resources,
not a proof that an entangled state and a communication channel are
interchangeable under all other resource budgets.
