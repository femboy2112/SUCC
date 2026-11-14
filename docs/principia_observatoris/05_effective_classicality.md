# Liber Quintus — De Geometria Emergente

## Restricted classical appearance and its operational boundary

This book proves a sufficient, and for a specified compression exact, criterion for a finite quantum carrier to admit a classical effective description. It does not characterize fundamental classicality. Geometric locality is a separate obligation from the state-reduction theorem below; the locality results of Book II must be supplied if locality is desired.

**Status.** PO-C1–C4 are complete finite-dimensional paper derivations using classical instrument and Markov-kernel mathematics. The integration and adversarial examples are new additions to this manuscript, with no scholarly priority claim. The universal intuition that geometric/computational alignment characterizes classical physics remains unestablished. Executable authority is reported separately in the round's validation record.

## 1. States, instruments and a declared observable algebra

Fix a nonzero finite-dimensional complex Hilbert space H. A state is a positive semidefinite operator ρ with tr(ρ)=1. Unnormalized states σ≥0 represent a branch together with its probability tr(σ); they are not a claim that the branch occurred.

An admissible action a has a finite outcome set O_a and completely positive maps

\[
\Phi_{a,o}:B(H)\longrightarrow B(H),\qquad o\in O_a,
\]

whose sum is trace preserving. H must include the memory needed for these composable state updates, or the stated instrument law must already be justified for the reduced system. An unmodeled environment cannot silently be reset between steps. The probability of outcome o in state ρ is tr(Φ_{a,o}(ρ)); a positive-probability outcome has posterior Φ_{a,o}(ρ)/tr(Φ_{a,o}(ρ)). The Heisenberg dual is defined by

\[
\operatorname{tr}(\Phi_{a,o}(\sigma)F)
 =\operatorname{tr}(\sigma\Phi^*_{a,o}(F)).
\]

Thus Φ* is completely positive and \(\sum_o\Phi^*_{a,o}(I)=I\). These are **quantum specialization assumptions**, not axioms imposed on every observer in Book I.

Choose a finite-dimensional unital commutative *-subalgebra

\[
D=\operatorname{span}_{\mathbb C}\{e_1,\ldots,e_m\}\subseteq B(H),
\quad e_ie_j=\delta_{ij}e_i,\quad e_i\ne0,\quad\sum_i e_i=I.
\]

The e_i are its minimal projections; their ranks in B(H) may exceed one. Define the linear coarse-state map

\[
q(\sigma)_i=\operatorname{tr}(\sigma e_i).
\tag{C0}
\]

For a state, q(ρ) is a probability vector. Every probability vector occurs: if r_i=tr(e_i), then \(\rho=\sum_i p_i e_i/r_i\) realizes p. The restriction retains expectations of D and can erase coherences and within-block state information. It does not assert that a microscopic state occupies one of the e_i before measurement.

A finite adaptive policy chooses its next action using the previous recorded outcomes and its own supplied randomness. Randomness is a supplied private seed independent of the initial carrier, with the same distribution in both comparisons; conditional on that entire seed, the policy is deterministic. It may have a bounded stopping rule. The same policy is used on both carriers. Its existence is a mathematical specification; executable memory, action availability and source authentication remain Book I obligations.

## 2. PO-C1: exact classical instrument descent

**Theorem PO-C1 (finite commutative instrument quotient).** For the fixed H, D and instrument family above, the following are equivalent.

1. For every a,o, \(\Phi^*_{a,o}(D)\subseteq D\).
2. For every a,o there is a matrix \(K_{a,o}\in\mathbb R_{\ge0}^{m\times m}\) such that, for every σ≥0,
   \[
   q(\Phi_{a,o}(\sigma))=K_{a,o}^{\mathsf T}q(\sigma),
   \qquad \sum_{o,j}K_{a,o}(i,j)=1\quad\text{for every }i.
   \tag{C1}
   \]

The matrices are unique, and

\[
\Phi^*_{a,o}(e_j)=\sum_i K_{a,o}(i,j)e_i,
\qquad
K_{a,o}(i,j)=\operatorname{tr}\!\left(\Phi_{a,o}(e_i/r_i)e_j\right).
\tag{C2}
\]

The classical carrier has hidden state i and action-dependent joint kernel
\(\mathbb P(o,j\mid i,a)=K_{a,o}(i,j)\). Initialized by q(ρ), it reproduces the quantum carrier's complete transcript distribution for **every finite adaptive policy** over the declared actions. It also reproduces the final expectation of every F∈D, jointly with each transcript.

**Proof.** Under (1), expand Φ*_{a,o}(e_j) uniquely in the e_i. It is positive, so every coefficient is real and nonnegative: test on a unit vector in e_iH. Summing the expansions over o,j and using unitality of the summed dual gives the row-total identity. Trace duality gives (C1), and evaluating on e_i/r_i gives (C2).

Conversely, (C1) gives, for every state ρ,

\[
\operatorname{tr}\left[\rho\left(\Phi^*_{a,o}(e_j)-\sum_iK_{a,o}(i,j)e_i\right)\right]=0.
\]

The bracket is Hermitian. Its expectation in every pure state is zero, hence the operator itself is zero. This proves (1) and uniqueness.

For a fixed transcript h=(o_1,…,o_n), let a_t be the action selected by the policy along that transcript. The unnormalized quantum branch is
\(\sigma_h=\Phi_{a_n,o_n}\cdots\Phi_{a_1,o_1}(\rho)\).
Repeated application of (C1) gives

\[
q(\sigma_h)=K_{a_n,o_n}^{\mathsf T}\cdots K_{a_1,o_1}^{\mathsf T}q(\rho).
\tag{C3}
\]

Taking the sum of components gives the same transcript probability. For a randomized policy, first condition on its entire private seed, independent of the initial carrier. The conditional policy is deterministic, so the preceding equality holds for each seed; average over the common seed distribution. This avoids treating a posterior distribution of controller randomness as independent of the observed history. Bounded stopping is implemented by absorbing stopped branches. Finally tr(σ_hF) is the pairing of q(σ_h) with F's coefficient vector. This proves the claims. □

**What the theorem establishes.** Coarse state is sufficient for all allowed future compositions, including feedback. Merely matching current expectations is weaker. This is an explicit realization of source-relative predictive closure, not an inference from repeated successful tests.

**What it does not establish.** No necessity is claimed for *every possible* classical realization with a different state space. The equivalence concerns the specified q, all source density states, and a Markov instrument acting on its m coordinates. Restricting allowed preparations can weaken the closure condition; adding actions can destroy it. The theorem does not derive physical access to D, an interpretation of hidden i as ontology, or a spatial metric.

## 3. PO-C2: quantitative finite-horizon robustness

Exact closure can be relaxed without normalizing rare branches. Let nonnegative K_{a,o} obey the row-total identity, and suppose a certified uniform calibration gives, for every action a and state ρ,

\[
\frac12\sum_o
 \left\|q(\Phi_{a,o}(\rho))-K_{a,o}^{\mathsf T}q(\rho)\right\|_1
\le\epsilon.
\tag{C4}
\]

**Theorem PO-C2.** For every common adaptive policy of at most N steps, the total variation distance between the quantum and classical transcript laws is at most \(\min(1,N\epsilon)\). The same bound holds for the joint law of the transcript and a final projective D-readout. If the initial coarse laws differ by total variation δ, replace Nε by δ+Nε.

**Proof.** At stage n, let σ_h be the unnormalized quantum branch and let v_h be the classical unnormalized coarse vector for the same history, including any action-choice probability. Set
\(E_n=\tfrac12\sum_h\|q(\sigma_h)-v_h\|_1\).
Homogeneity extends (C4) to σ_h with error at most ε tr(σ_h). For each history, the map \(v\mapsto(K_{a,o}^{\mathsf T}v)_o\) contracts the l1 norm: its columns are nonnegative and sum to one. The triangle inequality, summation over h, and \(\sum_h\operatorname{tr}(\sigma_h)=1\) give \(E_{n+1}\le E_n+\epsilon\). For randomized policies, first fix the full independent private seed and apply this bound, then average; total variation is convex. Thus E_N≤δ+Nε. Summing over final coordinates cannot increase l1 distance. Stopped branches can use an exact identity action. □

**Corollary PO-C2a (finite certificate for the uniform premise).** For a fixed action a, put

\[
D_{o,j}=\Phi^*_{a,o}(e_j)-\sum_iK_{a,o}(i,j)e_i.
\]

These are Hermitian. The bound (C4) for **every** density state is equivalent to the finite family of semidefinite inequalities

\[
\sum_{o,j}s_{o,j}D_{o,j}\preceq2\epsilon I
\qquad\text{for every }s\in\{-1,1\}^{|O_a|m}.
\tag{C4a}
\]

**Proof.** For each state, the sum of absolute values is the maximum over these sign vectors of \(\operatorname{tr}(\rho\sum s_{o,j}D_{o,j})\). A Hermitian operator has expectation at most 2ε in every state exactly when it is at most 2εI in the positive-semidefinite order. There are finitely many signs, so the quantifiers interchange without a limit. □

Thus finite-dimensional authenticated channel matrices can supply an all-state proof, rather than a sample of states. For rational Hermitian matrices and rational ε, each inequality has an exact principal-minor verification. The number of signs is exponential; no efficient tomography, experimental channel authentication or polynomial-time algorithm is asserted.

The uniform quantifier over states and actions in (C4) is essential. A bound fitted only on training preparations is not a certificate for untested interventions or conditionally reached states. This elementary telescoping result supplies a horizon **after** a source-derived error bound has been proved; it does not produce that error bound from data alone.

## 4. Outcome information cannot be replaced by an averaged channel

**Countermodel C-X1 (averaging hides failure of closure).** On a qubit write

\[
P_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
P_1=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
Q_\pm=\tfrac12\begin{pmatrix}1&\pm1\\\pm1&1\end{pmatrix}.
\]

Take D=span{P_0,P_1}. Define a measurement followed by reset:

\[
\Phi_\pm(\rho)=\operatorname{tr}(Q_\pm\rho)P_0.
\]

These maps are completely positive: they are measure-and-prepare maps, or have Kraus operators \(|0\rangle\langle\pm|\). Their sum is the trace-preserving reset channel \(\Lambda(\rho)=\operatorname{tr}(\rho)P_0\). For \(F=f_0P_0+f_1P_1\), \(\Lambda^*(F)=f_0 I\in D\), so the **averaged** Heisenberg channel preserves D.

But \(\Phi_\pm^*(I)=Q_\pm\notin D\). The states ρ_+=Q_+ and ρ_−=Q_− share q=(1/2,1/2), yet their outcome distributions are (1,0) and (0,1). No matrix K acting only on q can reproduce both. This is a two-dimensional exact counterexample to replacing individual-outcome closure by nonselective closure. All density and effect matrices displayed have rational entries.

A second insufficiency is mere **effect closure** \(\Phi_o^*(I)\in D\). It protects immediate outcome probabilities but need not protect future predictions. For example, take the one-outcome Hadamard unitary H; its effect is I, but \(H^*P_0H=Q_+\notin D\). A subsequent Z measurement distinguishes Q_+ from Q_− even though their initial q values coincide. Closure must include future target effects under the actual action maps.

## 5. PO-C3: target-relative nondisturbance

Let a measurement instrument have nonselective channel Λ=Σ_oΦ_o.

**Theorem PO-C3.** The following are equivalent:

\[
q\Lambda=q\text{ on all states}
\quad\Longleftrightarrow\quad
\Lambda^*(F)=F\text{ for every }F\in D.
\tag{C5}
\]

If the subsequent instrument family satisfies PO-C1, an inserted measurement satisfying (C5), **with its new outcome ignored and with the same subsequent policy**, changes no future transcript law or final D-expectation. More generally, if \(\sup_\rho \operatorname{TV}(q\Lambda(\rho),q(\rho))\le\eta\), every such subsequent transcript law changes by at most η, at every finite horizon.

**Proof.** The equivalence follows by testing e_j and using separation by states, as in PO-C1. The full subsequent experiment is a stochastic kernel from the initial q vector to its transcript and final D-readout, by PO-C1. Equality, or total-variation contraction by this kernel, proves the remaining claims. □

This is **nonselective target nondisturbance**. It neither says that the microscopic state is unchanged nor that conditioning on the outcome leaves the target distribution unchanged. Allowing a different feedback action because of the inserted outcome also changes the experiment being compared.

**Exact example.** The Z Lüders instrument \(\Phi_i(\rho)=P_i\rho P_i\) has \(K_i(j,k)=\delta_{j,i}\delta_{k,i}\). It obeys PO-C1 and (C5). Starting from Q_+, its ignored outcome changes the state to I/2, while q remains (1/2,1/2). Future Z/bit-flip/diagonal-phase experiments cannot detect that erased coherence. A subsequent X measurement, outside this invariant toolkit, distinguishes Q_+ and I/2 with plus probabilities 1 and 1/2.

For an explicitly stochastic effective dynamics, the qubit channel

\[
\Lambda_p(\rho)=(1-p)\rho+pX\rho X,\qquad0\le p\le1,
\]

induces the classical transition matrix
\(\begin{pmatrix}1-p&p\\p&1-p\end{pmatrix}\).
For p=1/3 this has rational coefficients. Composing it with Z readout retains exact classical transcript predictions. Inserting dephasing \(\rho\mapsto\sum_iP_i\rho P_i\) anywhere leaves those predictions unchanged. This is a finite coarse-graining example, not a derivation of macroscopic environmental decoherence.

## 6. PO-C4: entanglement is not a remote intervention signal

**Theorem PO-C4 (local-channel no-signaling law).** For any finite bipartite state ρ_AB and any trace-preserving completely positive map Λ_A on A,

\[
\operatorname{tr}_A[(\Lambda_A\otimes\mathrm{id}_B)(\rho_{AB})]
 =\operatorname{tr}_A\rho_{AB}.
\tag{C6}
\]

**Proof.** Pair the left side with any B-observable F. Trace duality gives
\(\operatorname{tr}[\rho_{AB}(\Lambda_A^*(I_A)\otimes F)]\), which equals \(\operatorname{tr}[\rho_{AB}(I_A\otimes F)]\) because Λ_A is trace preserving. All F separate the reduced states. □

Consequently every finite causal contrast in the *remote marginal*, between two such local actions, is zero, even for entangled input. A locally selected outcome can change a remote **conditional** state; identifying that subensemble requires the outcome record or a jointly available comparison. The statement assumes no intervening coupling or communicated signal.

For \(\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2\), remote Z outcomes have probabilities (1/2,1/2) before and after local Z measurement with its outcome forgotten. They become deterministic conditioned on the corresponding local outcome. The Bell-state density matrix and all these probabilities are rational; the square root in the vector representation is unnecessary for an exact check.

This law is already present in SUCC as PBR-05 in [the arithmetic ER=EPR supplement](../CLAIM_SUPPLEMENT_ARITHMETIC_ER_EPR.md). PO-C4 restates its finite-dimensional operational interface; it is not a new no-signaling theorem.

## 7. What survives of the founding classical-appearance hypothesis?

The faithful restricted interpretation is: **a model appears classical for an observer when its declared coarse states support an ordinary stochastic instrument calculus that predicts the allowed compositions, with a controlled target disturbance and a verified source map.** PO-C1 is a sufficient structural certificate; PO-C2 and C3 give explicit finite-horizon/error versions. When geometric locality is desired, the intervention-support and graph assumptions of Book II are additional hypotheses.

Keep at least three questions separate:

| Question | Certificate or diagnostic | Failure does not imply |
|---|---|---|
| Is the effective model compositionally predictive? | Exact quotient identities, or a proved uniform error bound | Fundamental nonclassicality |
| Is measurement gentle for the target? | (C5), or the operational bound in C3 | Inaccessibility of every other target |
| Does the declared geometry track causal dependencies? | Separate support/transport theorem and held-out interventions | Failure of classical mechanics |

**Classical chaos control.** For the entirely classical doubling map T(x)=2x mod 1, states x=0 and y=2^−(N+1) differ by an arbitrarily small amount. Their threshold readouts \(1_{[1/2,1)}(T^n x)\) agree for n<N and differ at n=N. Finite-resolution loss of long-horizon prediction is compatible with deterministic classical equations. Neither error growth nor a hidden horizon alone diagnoses quantum behavior.

**Classical shortcut control.** Two classical bits may be assigned arbitrary geometric separation L while the legal update is \((x,y)\mapsto(x,y\oplus x)\). The remote coordinate depends on x in one step for every L. Classical probabilistic semantics imposes no spatial speed limit; a faithful local chart needs a source-level finite-propagation premise.

**Training-only closure control.** Z-only transcripts match for Q_+ and Q_−, at every length. Admit a Hadamard action followed by Z measurement and they yield deterministic opposite readouts. The old quotient remains valid for its old toolkit, but fails under this explicitly enlarged toolkit. More training in the old family cannot replace the new intervention.

These examples refute an unrestricted equivalence between classical ontology, stable prediction, gentle measurement and geometric alignment. They preserve the proposed program as a target- and toolkit-relative theory of effective description.

## 8. SUCC specialization, provenance and remaining obligations

The existing [quantum_records.py](../../observational_succ/quantum_records.py) supplies exact rational real-qubit Kraus instruments and ordered branch records. Its `measure_z()` implements the Z specialization above. Its `measure_x()` supplies the enlargement that invalidates the Z-only quotient. O03 in [the existing ledger](../CLAIM_LEDGER.md) records order-sensitive probabilities, including the Z/X example with joint probabilities 1/2 versus 1/4. Those observations are exact calculations in a declared finite quantum model, not laboratory data.

The specialization map is explicit: source state = density matrix; action = validated `Instrument`; outcome component = \(\rho\mapsto K_o\rho K_o^{\mathsf T}\); readout = tr; record update = the existing positive-probability branch update. The q map is diag(ρ). Z instrument descent follows from \(P_iP_jP_i=\delta_{ij}P_i\). No change to existing record semantics is required. A valid branch calculation never certifies that a physical event occurred.

Primary antecedents checked for this round:

- E. B. Davies and J. T. Lewis, [*An operational approach to quantum probability*](https://doi.org/10.1007/BF01647093), Communications in Mathematical Physics 17 (1970), 239–260. The publisher abstract explicitly introduces instruments for sequential measurement. Full subscription text was not used as a proof dependency.
- E. A. Carlen and J. Maas, [*Gradient flow and entropy inequalities for quantum Markov semigroups with detailed balance*](https://www.janmaas.org/wp-content/uploads/2016/09/2016-Carlen-Maas.pdf), §4, especially Theorem 4.2, gives the established commutative invariant-algebra/classical Markov-chain bridge in its continuous-time detailed-balance setting. Our finite instrument proof above does not import its stronger semigroup assumptions.
- J. Watrous, [*The Theory of Quantum Information*, Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), provides standard state, channel and measurement definitions. No textbook content is redistributed.

The durable [quantum certificate probe](../../research/2026-11-13/principia_observatoris/quantum_certificate_probe.py) implements PO-C2a for real rational qubits by checking every sign and every required principal minor. Its [exact receipt](../../research/2026-11-13/principia_observatoris/receipts/quantum_certificate.json) covers 64 sign matrices: Z and bit-flip-then-Z at ε=0, reset-X at ε=1/2, and the rejected reset-X claim ε=1/3 (determinant −5/9). The reset-X states Q± attain error 1/2, proving sharpness for the stated comparison kernel. Three invalid instrument/kernel controls are rejected. The matrices are declared mathematical sources; no physical channel is authenticated by this certificate.

**Next verdict-changing obligation.** Given an authenticated carrier/instrument family and a proposed D, derive a uniform quantitative bound (C4) with a nontrivial horizon, including states reached after rare outcomes and withheld interventions. State-specific fitting does not pay this obligation. For a concrete physical interpretation, source adequacy and calibration must also be supplied. No physical collapse mechanism, spacetime metric, quantum-gravity conclusion, π-normality estimate or RH implication follows from this chapter.
