# A shared bridge: coherent communication needs an actual channel

Continuation parent: `e9639c0ddb07385c6000b670d26cf0f7b91dacaa`.
Status: **CLASSICAL** finite quantum-information protocols and
**PROVED LOCAL** exact normalization, branch and access calculations.
No spacetime geometry, traversable wormhole, objective collapse law or
unlimited communication resource is constructed here.

## 0. Faithful reading and resource types

The user proposes viewing the twins externally as correlated defects of a
larger carrier, joined by a shared bridge through which they cooperate
while retaining coherent evolution until their meeting. A precise positive
version is possible: retain the relevant branch registers coherently,
transmit a declared communication register or supply a declared controlled
coupling, and recover the logical information in the current output.

Three resources must be distinguished, even when a diagram relates them:

| Resource | Mathematical type | Operational role |
| --- | --- | --- |
| Entangled preparation | `eta: C -> A tensor B` | Produces a shared state |
| Communication channel | `N: L(S) -> L(B)` | Transmits an independently chosen input |
| Joint effect or controlled coupling | `A tensor S -> C`, or a joint unitary | Supplies an additional comparison, interaction or branch operation |

Here `C` in the first and third rows denotes the scalar field, the tensor
unit, not the logical-code notation of the preceding note. A physical
channel acts on density matrices and must be completely positive and
trace preserving. An individual selected measurement branch is only
trace nonincreasing. An entangled vector is not automatically either one.

All bases and Bell phases below are declared in a calibrated common
description. Actual frames must be transported as in
[TWIN_OBSERVERS.md](TWIN_OBSERVERS.md). Internal syndromes may be carried
or processed during the walk. The final comparator still sees only the
current outputs at one meeting event, not an untransported comparison of
the twins' raw histories. Classical messages below are present protocol
outputs, not access to an entire earlier observation history.

The classical precedent is Bennett et al.,
[*Teleporting an unknown quantum state via dual classical and
Einstein--Podolsky--Rosen channels*, 1993](https://research.ibm.com/publications/teleporting-an-unknown-quantum-state-via-dual-classical-and-einstein-podolsky-rosen-channels).
The category-theoretic formulation explicitly includes branching and
communication: Abramsky and Coecke,
[*A categorical semantics of quantum protocols*, Sections 3 and 9.1](https://arxiv.org/pdf/quant-ph/0402130).
The calculations below fix the normalization and conventions directly.

## 1. The normalized cup and cap do not give a free deterministic wire

For `H=C^d`, with `d>=1`, fix the normalized maximally entangled vector

\[
 |\Phi_d\rangle=d^{-1/2}\sum_{j=0}^{d-1}|j\rangle|j\rangle.
\]

Prepare it on `A,B`, and apply the selected Bell bra `<Phi_d|` to the
input `S` and `A`. The resulting map `K:S->B` is

\[
 \boxed{
 K=(\langle\Phi_d|_{SA}\otimes I_B)
       (I_S\otimes|\Phi_d\rangle_{AB})
   =\frac1d I_{S\to B}.}
\]

**BCOM-01 — PROVED LOCAL.** For every unit input, this selected branch has
probability `1/d^2`. The calculation also holds with any reference attached.

**Proof.** Apply the composition to `sum_k psi_k|k>`. The Bell bra
contributes `delta_kj/sqrt(d)` to the term with input `k` and pair label
`j`; the preparation contributes its own `1/sqrt(d)`. The output is
`sum_k psi_k|k>/d`. Its squared norm gives the probability. Tensoring
the same linear identity with a reference leaves it valid. QED.

The unnormalized categorical cup `sum_j|j,j>` and its matching cap obey
the exact snake identity `I`. Their norms are `sqrt(d)`. For `d>1`, they
are not respectively a unit state preparation and a physical
trace-nonincreasing selected effect. Normalizing both exposes the `1/d`
amplitude. Discarding that scalar would erase the selected branch's cost.

Postselection on this result does transmit the normalized input on the
successful branch. It supplies neither success on every attempt nor a
remotely known success flag without a declared way to communicate it.
That is a precise state/effect/channel distinction, not a prohibition on
using the construction inside a complete protocol.

## 2. All four branches produce a deterministic qubit channel

Let `S` be the input qubit. Alice holds `S,A`; Bob holds `B`. They initially
share `Phi_2` on `A,B`. Alice applies `CNOT_(S->A)`, then Hadamard on `S`.
In this note the syndrome bits are `a=S` and `b=A` after those operations.
Thus this bit order is the reverse of some textbook naming conventions.

Set

\[
 X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 U_{ab}=X^b Z^a.
\]

Expanding the three-qubit circuit gives the isometry

\[
 \boxed{
 T|\psi\rangle
 =\frac12\sum_{a,b\in\{0,1\}}|a,b\rangle_M
             \otimes U_{ab}|\psi\rangle_B,}
\]

where `M=(S,A)` contains the present syndrome registers. In particular,
the unnormalized Bob branch is `E_ab psi`, with `E_ab=U_ab/2`.

**BCOM-02 — CLASSICAL teleportation, explicit local proof.** Each syndrome
occurs with probability `1/4`, independently of the input. After receiving
`a,b`, Bob applies `C_ab=U_ab^*=Z^a X^b`. Then

\[
 C_{ab}E_{ab}=I/2,
 \qquad
 \sum_{a,b}C_{ab}E_{ab}\rho E_{ab}^*C_{ab}^*=\rho.
\]

**Proof.** Each `U_ab` is unitary, so `E_ab^*E_ab=I/4`. Its inverse
correction makes every branch `I/2`; summing its four density outputs
gives `rho`. The equality holds on all matrix units, so its extension
with the identity channel on any reference also holds. QED.

The standard implementation consumes **one shared Bell pair and two
classical bits from Alice to Bob per teleported qubit**, with its local
gates, measurements and corrections. This is the resource accounting of
the [Watrous/IBM Quantum teleportation lesson](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/entanglement-in-action/quantum-teleportation).
The classical bits select a correction; they are not a classical
description of the unknown qubit. The protocol transfers the input rather
than retaining two independent copies of it. Repeating this particular
one-qubit protocol requires fresh pairs and messages on each use.

If the observers already carry a protected twin relation and wish to
transmit a further independent message, this protocol needs a separate
communication resource pair, or another explicitly supplied channel.
Its reference-preservation theorem concerns the transmitted input and
its existing correlations; the consumed resource pair is not a reusable
shared memory. A different joint code or resource protocol would need
its own preservation and cost proof.

## 3. Without the message, the receiver gets an exact constant channel

**BCOM-03 — PROVED LOCAL Pauli-twirl control.** If the syndrome is not
available to Bob and no conditional correction is applied, his current
channel is

\[
 \boxed{
 \mathcal D(\rho)=\frac14\sum_{a,b}U_{ab}\rho U_{ab}^*
      =\frac{\operatorname{Tr}\rho}{2}I.}
\]

**Proof.** Conjugation by `Z` cancels the off-diagonal entries when
averaged with the identity. Averaging the remaining diagonal matrix with
its `X` conjugate makes both entries half the trace. This is the displayed
four-term average. QED.

For a density matrix, Bob sees `I/2` for every chosen input. With a
correlated input `rho_SR`, his reference/output density is
`I_B/2 tensor rho_R`, in the corresponding register order. The perfect
channel emerges only when the additional message/correction resource is
used. Retaining the global branch amplitudes does not make them locally
accessible to Bob.

One communicated syndrome bit is also insufficient for this protocol.
For example, correcting `X^b` but withholding `a` leaves
`(rho+Z rho Z)/2`. It transmits the diagonal populations but erases the
input coherence. This provides a control that can pass classical label
tests while failing the full quantum channel test.

### Arbitrary local chosen-message operations still cannot signal

**BCOM-04 — CLASSICAL no-signalling, explicit proof.** For any finite
bipartite state `rho_AB` and any chosen local CPTP map `L_m` on Alice,

\[
 \operatorname{Tr}_{A'}
    [ (\mathcal L_m\otimes\mathrm{id}_B)(\rho_{AB}) ]
 =\operatorname{Tr}_A\rho_{AB},
\]

independently of the chosen message label `m`.

**Proof.** Write `L_m(X)=sum_j L_(mj) X L_(mj)^*`, with
`sum_j L_(mj)^*L_(mj)=I_A`. For every Bob observable `O`, its expectation
after the map equals

\[
 \sum_j\operatorname{Tr}
    [\rho_{AB}(L_{mj}^*L_{mj}\otimes O)]
 =\operatorname{Tr}[\rho_{AB}(I_A\otimes O)].
\]

All Bob expectations agree, giving equality of the reduced matrices.
This covers all local choices and nonselective local measurements. A
chosen measurement **outcome** is not a freely selectable CPTP operation.
Conditioning on an outcome requires knowing that outcome; sending it is
precisely an extra communication operation. QED.

If the supposed bridge is an actual interaction connecting the sides,
the local-only premise has changed. That can legitimately transmit
information, but its channel, causal availability and control interface
must then be specified. The shared state alone has not supplied them.

## 4. A fully coherent positive version with deferred readout

Keep `M` coherent in the state `T psi`. Suppose the protocol supplies the
joint controlled unitary

\[
 C=\sum_{a,b}|a,b\rangle\langle a,b|_M\otimes U_{ab}^*.
\]

**BCOM-05 — PROVED LOCAL.** It obeys

\[
 \boxed{CT|\psi\rangle
 =|+,+\rangle_M\otimes|\psi\rangle_B.}
\]

**Proof.** Every `U_ab^*U_ab` is identity, leaving the coefficient `1/2`
on each syndrome vector. Their normalized sum is `|+,+>`. The result
holds as a linear map, so tensoring any reference proves complete
reference preservation. QED.

This is a constructive coherent protocol. The records carry no remaining
information about the logical input after correction, and the chosen
final readout can be deferred to the meeting. A further Hadamard on each
syndrome qubit maps its fixed state to `|00>` if desired.

There is an explicit resource cost: `C` couples Alice's coherent syndrome
register to Bob's output. One implementation physically transmits the
two-qubit syndrome to Bob and applies the controlled correction there.
Another provides an actual suitable nonlocal interaction or communication
primitive. These are sufficient implementations, not a claim of minimal
coherent communication cost. Local operations on a preshared Bell pair
alone do not implement `C`, as BCOM-03/04 demonstrate.

There is a literal realization that also preserves an existing observer
bond. Leave that bond `Phi_AB` untouched, place a further message in `M`,
and supply a separate resource pair `Phi_RS`. Applying the protocol on
`M,R,S` gives, by BCOM-05,

\[
(I_{AB}\otimes CT_{MRS})
 (\Phi_{AB}\otimes|\psi\rangle_M\otimes\Phi_{RS})
=\Phi_{AB}\otimes|++\rangle_{MR}\otimes|\psi\rangle_S.
\]

The original twins remain entangled, the message arrives coherently, and
the consumed ancillary pair and actual communication are visible in the
formula. Tensoring an external reference preserves the same identity.
This follows directly from the proved map identity; it does not claim a
separate physical experiment or an extra finite test count.

If the classical teleportation syndrome is measured earlier, the corrected
logical channel and its correlations with a reference are still exactly
preserved. Keeping every record coherent is the stricter full-state
version, not a prerequisite for preserving the recovered logical state.
Neither version determines when an objective physical collapse occurs.

The syndrome can be used as a present internal control during the walk.
That respects the final present-output comparison rule: no step assumes
the observers can equate raw observations from separated frames. An
unavailable past record is not made available by a change of coordinates.

## 5. What the external-carrier picture earns

An external observer may model both walkers, their records and the
communication mechanism as one larger isometric circuit. In that model,
the coherent protocol supplies an explicit bridge for logical information.
Its present decoded output is exactly the intended channel, and its
internal branching need not be irreversibly selected before the meeting.

The channel implementation established here is specific:

> One preshared Bell pair, the declared local Bell-processing circuit,
> a two-bit classical channel, and conditioned corrections implement
> one qubit identity channel. A coherent version uses an actual coherent
> syndrome channel or an equivalent supplied joint coupling.

This does not identify a shared state with unlimited communication. It
also does not identify these Hilbert-space operations with a spacetime
wormhole. No metric, gravitational constraints, locality structure,
traversability theorem or dictionary from arithmetic operators to gravity
has been supplied by this calculation. The geometric ER=EPR question
therefore needs separate hypotheses and evidence.

If sharing the bridge lets both observers reuse the same messages, their
eventual agreement also has shared provenance. A consistency theorem
can certify that the specified communication and decoding worked; it
cannot turn their agreement into an independent authentication of an
arithmetic source or an unknown model of the carrier.

`bridge_communication_probe.py` checks the literal three-qubit circuit,
every Bell branch, all qubit matrix units, exact reference preservation,
the normalized cup/cap scalar, no-message and one-bit controls, and
arbitrary-local-map no-signalling on a complete two-qubit operator basis.
All arithmetic is exact. These finite checks calibrate the implementation;
the general claims have the explicit proofs above. There is no new
priority claim for teleportation, no-signalling or compact duality.

The completed run passed **204 exact assertions, exit 0**, recorded in
[BRIDGE_COMMUNICATION_REPORT.json](receipts/BRIDGE_COMMUNICATION_REPORT.json).
This includes all four qubit matrix units for the corrected, uncorrected
and one-bit channels, and all 16 two-qubit matrix units for each of nine
local CPTP choices in the no-signalling control. Source hashes and the
explicit bit-order convention are retained in the receipt. Reproduce with:

```bash
python research/2026-11-12/prime_fixed_point_observer/bridge_communication_probe.py
```
