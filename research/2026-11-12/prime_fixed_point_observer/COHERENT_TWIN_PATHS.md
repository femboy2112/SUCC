# Coherent twin paths: a working arithmetic construction

Continuation of published commit `e9639c0ddb07385c6000b670d26cf0f7b91dacaa`.
The user's present-only and frame-transport constraints remain mandatory.
The code and proofs construct a finite mathematical protocol, not a physical
experiment or an objective collapse law.

## The result

The new refinement has a positive realization: **the arithmetic carrier can
record accept/reject branches while preserving a deliberately encoded logical
state and all of its entanglement with a reference**. What must remain
unrevealed to the inaccessible carrier is the protected logical distinction.
The carrier need not stay untouched.

Three results make this precise:

1. A code-level criterion says exactly when a specified present twin survives,
   and separately when a present recovery can restore it.
2. The actual arithmetic returns admit explicit protected encodings, including
   one that coherently uses both accepted and rejected branches.
3. A phase-sensitive present comparison separates coherent relative mismatch
   from lost contrast, while retaining exact counterexamples to inference
   about the observers' entire past.

The user's next refinement, viewing the twins externally as the endpoints
of one carrier bond, also has an exact encoded-state dictionary. A bridge
that transmits freely chosen messages requires a communication operation
in addition to the shared state. Section 7 separates these statements and
constructs a coherent communication protocol with its resources declared.

The proofs and controls are in [COHERENT_CHANNELS.md](COHERENT_CHANNELS.md),
[ARITHMETIC_COHERENCE.md](ARITHMETIC_COHERENCE.md),
[COHERENT_PATH_TRANSPORT.md](COHERENT_PATH_TRANSPORT.md), and the
[adversarial audit](reviews/coherent_path_adversarial_audit.md).
The [registered contract](COHERENT_PATH_CONTRACT.md) records the hypothesis,
permissions, source state, acceptance criteria and cheapest falsifiers.

## 1. The right invariant is the protected logical information

Let C be a finite logical space, B the current accessible output of one
observer, and E the part of the carrier inaccessible at the meeting.
Assume a specified isometry W:C->B tensor E, and a fixed calibrated intended
transport V:C->B. Then the following are equivalent:

\[
 \text{every logical state is transported by }V;
 \qquad
 (\mathcal N\otimes\mathrm{id})(\Phi_d)=\Phi_V;
 \qquad
 \boxed{W\psi=V\psi\otimes\eta\quad\text{for every }\psi\in C,}
\]

where the middle expression uses the corresponding pure-state density
operators, N is the channel obtained by tracing E, and the same unit vector
eta works for every logical input. The reference is untouched or its known
transport has been removed. An unknown noisy second observer is not
automatically an inert reference.

The proof uses the full entangled reference as a test of every input matrix
unit. A pure reference-output reduction forces global factorization; reference
coefficient comparison then gives the same eta for every input. This is a
specialization of classical finite channel theory with a self-contained proof.

There is a broader condition if the observer can decode its current output:

\[
 \exists\mathcal R\text{ CPTP with }\mathcal R\mathcal N=\mathrm{id}
 \quad\Longleftrightarrow\quad
 E_a^*E_b=\lambda_{ab}I_C
 \quad\Longleftrightarrow\quad
 \mathcal N^c(X)=\operatorname{Tr}(X)\tau_E.
\]

Here E_a are the Kraus operators, and N^c is the inaccessible carrier's
channel. This is the classical Knill--Laflamme criterion. It allows an
independent syndrome: the raw accessible output may be mixed, yet the
logical twin is exactly recoverable. The current decoder and its access
requirements are part of the protocol. Merely embedding everything in a
larger universe supplies neither access nor a decoder.

## 2. An explicit arithmetic twin that survives a carrier interaction

Our centered arithmetic return is

\[
 T_{3,2}\varepsilon_k=
 \begin{cases}\varepsilon_{2k/3},&3\mid k,\\0,&3\nmid k.\end{cases}
\]

Its retained-record isometry keeps rejected inputs instead of deleting them:

\[
 W\varepsilon_k=
 \begin{cases}
 \varepsilon_{2k/3}\otimes|0\rangle,&3\mid k,\\
 \varepsilon_k\otimes|1\rangle,&3\nmid k.
 \end{cases}
\]

Now choose orthonormal logical vectors

\[
 c_1=(3\varepsilon_3+4\varepsilon_2)/5,
 \qquad c_2=(3\varepsilon_6+4\varepsilon_4)/5.
\]

The literal arithmetic branches give

\[
 Wc_1=\varepsilon_2\otimes(3|0\rangle+4|1\rangle)/5,
 \qquad
 Wc_2=\varepsilon_4\otimes(3|0\rangle+4|1\rangle)/5.
\]

Therefore, for arbitrary complex alpha,beta,

\[
 \boxed{W(\alpha c_1+\beta c_2)
   =(\alpha\varepsilon_2+\beta\varepsilon_4)
      \otimes(3|0\rangle+4|1\rangle)/5.}
\]

The environment changes and both arithmetic branches occur. Its complete
state is independent of alpha,beta. Tensoring this identity with a twin
reference proves preservation of the full encoded correlation. A present
decoder identifies epsilon_2,epsilon_4 with the two logical output labels.
No histories are exchanged or directly compared.

This construction requires a chosen superposition encoding. It is not an
assertion that unencoded integers 2 and 3 preserve their distinction:
indeed both have the same arithmetic output epsilon_2, while their
information is transferred to the record. That pure output is an exact
counterexample to using purity as a certificate of information preservation.

For a whole finite route, each record h has a partial isometry K_h with a
disjoint input sector. If L lies in the common output ranges of the chosen
branches and sum_h |c_h|^2=1, then

\[
 J_c\phi=\sum_h c_hK_h^*\phi,
 \qquad
 W_NJ_c\phi=\phi\otimes\sum_hc_h|h\rangle.
\]

This is a constructive classification of all directly isometric codes for
this finite arithmetic channel. Codes requiring further recovery are a
separate class. The common output-range condition and the full coefficient
vector carry the information missing from a claim that paths merely agree
at a root.

## 3. Every finite route has a protected success encoding, with a cost

For a prescribed sequence of proper coprime returns (q_j,r_j), reduce each
prefix ratio to a_j/b_j:

\[
 \alpha_j=\prod_{i=1}^j r_i/q_i=a_j/b_j,
 \quad L_N=\operatorname{lcm}(b_1,\ldots,b_N),
 \quad M_N=\alpha_NL_N.
\]

With D_d epsilon_k=epsilon_(dk), the exact identity is

\[
 \boxed{T_N\cdots T_1=D_{M_N}D_{L_N}^*,
 \qquad W_ND_{L_N}\psi=D_{M_N}\psi\otimes|0^N\rangle.}
\]

The proof checks the entire path domain: each intermediate label must be an
integer, so every reduced prefix denominator must divide the source label.
The final ratio alone misses that requirement.

For example, first apply T_(2,1), then T_(3,2). The final multiplier is
1/3, but L_2=6 and M_2=2. Input3 is rejected immediately, even though
the endpoint expression 3/3 is an integer. The correct route has domain
the multiples of6. Reversing those two returns has the same endpoint
multiplier but domain the multiples of3.

Thus two finite observers can select their source encodings from their own
route data, arrive in decoded copies of one logical space, and compare only
their present outputs. The encoded source scale depends on the route. On
logical labels0,...,d-1 it reaches L_N(d-1); preparation, computation and
decoding are actual resources.

For every infinite sequence of strict proper returns,

\[
 L_N\mid L_{N+1},\qquad L_N-M_N\ge N,
 \qquad L_N\ge N+1,
 \qquad\bigcap_ND_{L_N}H=\mathbb C\varepsilon_0.
\]

Each accepted step strictly decreases a positive integer, which proves
the bound. Every finite horizon admits the encoding, but one fixed
nontrivial all-success code cannot last indefinitely. Other coherent record
sectors can survive: repeated T_(3,2) leaves every nonmultiple of3 in the
same rejected branch forever. That preserves a state but does not execute
the desired successful arithmetic traversal.

For an unencoded uniform d-level twin, all-success selection has probability

\[
 p_N=\frac{1+\lfloor(d-1)/L_N\rfloor}{d}.
\]

Once only the root survives, the conditional state is pure but has Schmidt
rank1. Postselecting that clean event has discarded the original twin's
logical information. The retained failures and their probabilities must
remain part of the report.

## 4. A meeting needs both phase and contrast

In a calibrated two-qubit current output, consider

\[
 \rho_\gamma=\tfrac12\left(|00\rangle\langle00|+|11\rangle\langle11|
 +\gamma|00\rangle\langle11|+\overline\gamma|11\rangle\langle00|\right),
 \quad |\gamma|\le1.
\]

For a supplied exact density matrix, the expectations ZZ=1 and ZI=0
characterize this sector. Within it, the present quantities

\[
 x=\langle XX\rangle,\quad y=\langle XY\rangle,
 \qquad\boxed{\gamma=x-iy}
\]

reconstruct the state. Its purity is (1+|gamma|^2)/2 and its overlap with
the original Bell state is (1+Re gamma)/2. Those are different diagnostics.

| Current state | Original Bell overlap | Joint purity | XY | Individual outputs |
| --- | ---: | ---: | ---: | --- |
| gamma=i, a pure relative phase | 1/2 | 1 | -1 | Both I/2 |
| gamma=0, a dephased mixture | 1/2 | 1/2 | 0 | Both I/2 |

The rows also give identical computational-basis agreement. One additional
present quadrature separates them. This is a concrete repair of the
comparison interface; it does not reveal which past mechanism produced a
given current state. The audit also gives a quantitative robust bound when
the sector guards are only approximately satisfied.

These expectations are not all simultaneously available from one physical
copy. A physical protocol needs repeated preparations and calibration/error
bounds, or a supplied classical state description. If the permitted outputs
are only the two local reduced states, the table is an impossibility witness:
no comparator using only those states can distinguish the rows. A joint
current diagnostic is an explicitly richer present output, not access to
the observers' histories.

## 5. A clean final event does not certify a clean past

There are two exact controls:

* Recording the twin's label into a carrier qubit by CNOT makes the reduced
  twins separable. Applying the same CNOT again restores the entire original
  joint state. This record-and-reversal and an idle history have identical
  present data, even if the whole final carrier state is exposed.
* Projecting the dephased mixture onto the desired Bell state succeeds with
  probability1/2 and prepares that pure state conditionally. The final
  measurement can therefore create the very pure output being used as a
  supposed certificate of its pre-meeting history.

These are identifiability boundaries: no observation on equal final states
can distinguish their histories. They do not invalidate a theorem derived
from a specified dynamical model; they prevent the theorem from being
inferred solely from the successful meeting outcome.

Nor does a local state update imply a superluminal signal. A local
trace-preserving quantum operation leaves the other twin's unconditioned
marginal unchanged. Actual propagation follows the carrier's specified
interaction structure. CPT-05 proves a finite-circuit causal-support law;
there is no assumed physical light cone or collapse speed in the arithmetic
construction.

## 6. What the construction earns

The strongest surviving architecture is a **protected, frame-calibrated
logical transport with a declared present diagnostic**. It permits carrier
interaction, retained branch structure and explicit recovery. It separates
relative phase, information leakage, and source authentication.

For finite paths, verified edge errors epsilon_j accumulate to at most
sum epsilon_j in the stipulated isometric model. For two separate path
channels with independent auxiliary preparations, plus a calibrated ideal
mismatch delta, the current target-projection failure is
at most min(1,(E_A+E_B+delta)^2). These bounds supply a quantitative meaning
of a defect budget, with fresh-record and frame assumptions stated.

A genuinely shared carrier needs the actual joint isometry and its own
bound. The product-channel theorem does not silently assume away shared
environmental correlations. Conversely, preservation of one Bell state
under a joint operation does not certify the operation on every joint input.

### Coherence also needs a source-observable check

The [cross-audit](reviews/coherence_cross_audit.md) supplies a concrete
arithmetic warning. The centered basis epsilon_k refers to original source
label k+1. On the displayed code c_1, the source prime projector has
expectation16/25: its original labels are4 and3. The output epsilon_2
has original label3 and prime expectation1. On c_2 the source labels7
and5 are both prime, and its output epsilon_4 is also prime. Therefore
the input prime effect on the logical code is diag(16/25,1), whereas
applying the ordinary prime projector to both output labels gives I.

The logical information is perfectly preserved, but this unchanged output
observable is the wrong interpretation of that information. A correct
present effect O_out must satisfy

\[
 \boxed{V^*O_{\rm out}V=J^*O_{\rm source}J}
\]

on the logical space. Here the correct effect assigns weights16/25 and1
to epsilon_2 and epsilon_4. It is no longer the ordinary sharp prime
projector. Constructing this transported observable can itself require
the source data one hopes to learn; its cost and provenance must remain
explicit. The same issue applies to the additive relation used by a
prime-pair observable. This is a source-faithfulness obligation with an
exact counterexample, not a failure of the coherent encoding theorem.

This is a genuine construction and characterization step for the observer
program. It does not prove that objective physical collapse occurs only at
the meeting. It does not make agreement into independent source evidence.
Goldbach, pi normality and RH remain open: the missing source-specific
arithmetic estimate has not been obtained from coherence alone.

The next constructive question is whether the protected current output can
be chosen to retain a **particular additive arithmetic observable**, with
an independently proved computation/transport/error budget, while rejecting
the earlier source relabeling and relative-phase countermodels. Encoding
the desired answer as an unexplained input would merely move the obligation.

## 7. The outside carrier bond and the ER=EPR proposal

Let `C` be the logical space, `bar C` its conjugate, and let
`J_A:C->H_A` and `J_B:bar C->H_B` be isometric encodings into the two
carrier patches. The external state is

\[
 |\Psi_{\rm ext}\rangle
 =(J_A\otimes J_B)|\Phi_d\rangle,
 \qquad
 |\Phi_d\rangle=d^{-1/2}\sum_j |j\rangle|\bar j\rangle.
\]

The internal twin description and the external encoded-bond description
give exactly the same present probabilities when effects are transported
through the encodings. For example,

\[
 \langle\Psi_{\rm ext}|X\otimes Y|\Psi_{\rm ext}\rangle
 =\langle\Phi_d|
       J_A^*XJ_A\otimes J_B^*YJ_B
   |\Phi_d\rangle.
\]

Joint present effects obey the same pullback rule. Protected path
isometries transport this bond and leave fixed carrier records. This is
the precise positive equivalence proved in
[CARRIER_BOND_DUALITY.md](CARRIER_BOND_DUALITY.md). Calling its endpoints
carrier defects is an interpretation of the declared encoding; it does
not yet specify a metric defect or gravitational solution.

### A bond can support a protocol without being a free wire

The mathematical types are different: a shared state prepares two
outputs, while a communication channel accepts an independently chosen
input and makes it available at the other end. The normalized Bell
preparation and selected Bell effect satisfy

\[
 (\langle\Phi_d|\otimes I)(I\otimes|\Phi_d\rangle)
 =I/d.
\]

The successful branch is an identity map after normalization, with
probability `1/d^2`. Omitting this scalar conceals postselection.
[BRIDGE_COMMUNICATION.md](BRIDGE_COMMUNICATION.md) gives the complete
qubit protocol: all four Bell branches, one shared Bell pair, two
communicated classical bits, and conditioned corrections implement the
identity channel. Without the message, the receiver sees
`rho -> Tr(rho) I/2` for every chosen input.

A fully coherent implementation retains the syndrome `M` and supplies
the actual controlled coupling

\[
 T|\psi\rangle
 =\tfrac12\sum_{a,b}|a,b\rangle_M X^bZ^a|\psi\rangle_B,
 \qquad
 C=\sum_{a,b}|a,b\rangle\langle a,b|_M\otimes Z^aX^b,
\]

so `CT psi=|++>_M tensor psi_B`, including every reference correlation.
One implementation transports the coherent syndrome to the receiver;
another supplies the stated joint interaction. Thus the walkers can
communicate coherently in the larger carrier, with a declared channel.
The channel's capacity, access, timing and cost are additional data.
Preserving one shared Bell state under a joint interaction is also weaker
than preserving every possible logical input.

The teleportation pair is consumed by this particular implementation.
Preserving an existing observer/reference bond while transferring a further
message therefore requires the stated additional resource pair or channel,
or a separately proved joint encoding. Complete reference preservation
applies to the transmitted input; it does not make its communication
resource inexhaustible.

### The exact meeting distinction in the physics sources

Maldacena and Susskind's
[original proposal, Section 3.4 and Figure 10](https://arxiv.org/pdf/1306.0533),
already depicts two observers entering opposite black holes and meeting
inside. It does not permit a message through the original bridge to an
observer remaining in the other exterior. The generalized relation for
arbitrary entangled particles is presented there as a quantum-gravity
conjecture, with no general classical geometry promised.

Gao, Jafferis and Wall's
[traversable construction](https://arxiv.org/pdf/1608.05687) adds an
interaction coupling the boundaries in a specified gravitational model.
Maldacena, Stanford and Yang's
[Section 2.1.1](https://arxiv.org/pdf/1704.05333) then relates a controlled
coupling to a measurement, communicated result and conditioned operation.
Their equivalence concerns the **receiving side's current reduced
state**. The joint final states can differ. This is decisive for the
user's meeting rule: a comparator given both current quantum outputs
may distinguish the protocols even though the separated receiver cannot.

The exact control is a coherent CNOT producing a Bell state versus the
same controlled operation with its control dephased. Both receiver
marginals are `I/2`; at the joint meeting, `XX` has expectations 1 and 0.
No history comparison is needed. The
[ER=EPR audit](reviews/er_epr_equivalence_audit.md) states the permitted
output algebra and intervention resources for each equivalence.

### Shared information and inferred geometry each need a further contract

Two disjoint endpoint algebras cannot both implement the same full
noncommutative logical algebra on an entire preserved code. Their
physical operators commute, so exact code-preserving intertwining forces
the corresponding logical operators to commute too. State-specific
Bell mirror identities evade this statement because they are identities
on one vector, with transpose reversing multiplication; they do not
supply two independently accessible copies of a whole quantum memory.
The bond note proves this boundary and retains the compression-only
countercontrol.

The repository's October
[arithmetic holography obstruction](../../2026-10-22/ARITHMETIC_HOLOGRAPHY_OBSTRUCTIONS.md)
already realizes the same boundary copy encoder on two graphs with
different boundary distances. Consequently these present state data do
not uniquely determine an underlying geometry. A genuine geometric
equivalence would need a source-derived locality/metric dictionary,
admissible dynamics and causal access, not just the tensor contraction.

The earned statement is therefore exact: **encoded twins and an external
correlation bond are two descriptions of the same declared state and
present observations. Coherent communication is additionally realizable
when its actual channel is included on both sides of the dictionary.**
If the twins share messages while constructing their models, their
agreement also has shared provenance. It certifies the stated consistency
conditions, and still needs a separate source-authentication argument.

## Reproduction and evidence

Run from the repository root:

```sh
python research/2026-11-12/prime_fixed_point_observer/arithmetic_coherence_probe.py
python research/2026-11-12/prime_fixed_point_observer/coherent_channels_probe.py
python research/2026-11-12/prime_fixed_point_observer/coherent_path_transport_probe.py
python research/2026-11-12/prime_fixed_point_observer/reviews/coherent_path_adversary_probe.py
python research/2026-11-12/prime_fixed_point_observer/reviews/coherence_cross_probe.py
python research/2026-11-12/prime_fixed_point_observer/carrier_bond_probe.py
python research/2026-11-12/prime_fixed_point_observer/bridge_communication_probe.py
python research/2026-11-12/prime_fixed_point_observer/reviews/er_epr_intervention_probe.py
```

Exact results, original runs, source preservation, required repository gates
and artifact hashes are recorded in [VALIDATION.md](VALIDATION.md). The
universal statements have written proofs; their finite test counts are
implementation calibrations, not independent mathematical votes. No formal
kernel or external peer review is claimed for this continuation.
