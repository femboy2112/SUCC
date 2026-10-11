# Foundations: a finite, physical observer constructing mathematical knowledge

**Version:** founding research frame, October 2026. **Status:** proposal plus cited/classified mathematics, not a complete theory of cognition or a proof of RH.

## 1. The initiating distinction

The originating claim is **not** “Hilbert space is logically greater than the integers.” It is: in our empirically modeled physical world, a mathematician and their measuring environment are already physical processes, generally represented using quantum Hilbert-space models, **before** they form mathematical concepts about the world.

A causal event changes what a particular observer has actually encountered. A semantic interpretation relates that event to a model, often revising relationships among previous events. The observer may formalize or prove claims about mathematical spaces without ever ceasing to be a physical observer.

Distinguish:

- **Physical carrier** — a specified system, dynamics and measurement instrument. Whether quantum mechanics is ultimate ontology is open.
- **Causal record** — ordered outcomes, contexts and provenance. It is not the same as the observer's reduced physical state.
- **Semantic representation** — revisable model of field dynamics or meaning. No established brain-to-math functor is assumed.
- **Mathematical structure** — formally defined objects and proofs. A theorem is not merely accumulated perceptual agreement.
- **Global report** — an invariant extracted from a completed history or mathematical object with explicit axioms and domains.

The theory asks which morphisms between these levels are *faithful, causal, regular, computable and justified*.

## 2. Finite observational SUCC

Write a finite recorded stage as

\[
O_n=(\text{events through }n,\text{source journal},\text{field context},\text{admissible probes}).
\]

An observation SUCC arrow \(O_n\to O_{n+1}\) appends a **realized** event, not an expected future event. Transformations of the representation can be invertible or lossy; erasure of a connected *residual* is not erasure of its original observed fact.

For normalized arithmetic source coefficients \(a(1)=1\), the finite causal Dirichlet logarithm \(b=\log_*a\) is reconstructible via \(a=\exp_*b\). At two independent primes \(p,q\),

\[
b(pq)=a(pq)-a(p)a(q).
\]

Genuine zeta data have \(b(6)=0\) but still \(a(6)=1\). The composite was explained by earlier primitive channels, not invalidated. Deliberate counterfeit \(a(6)=2\) gives \(b(6)=1\). This distinction remains vital even for applications completely unrelated to number theory.

## 3. Why the *second* derivative is relational

An observer who compares local observations with a model already uses an informal analogue of the first derivative: how has the model changed? Comparing *relations among* changing observations suggests a mixed second derivative of a two-input report.

With a continuously indexed two-time kernel \(K(t,u)\), the **finite** version is

\[
\Delta_t^h\Delta_u^k K =
K(t+h,u+k)-K(t+h,u)-K(t,u+k)+K(t,u).
\]

Both single-observer contributions cancel. Its normalized limit, where meaningful, is \(\partial_t\partial_uK\). This mathematical formalism is a proposed model of comparative cognition, **not** a measured neurophysiological mechanism.

The sharp classical RH connection is Suzuki's even screw function:

\[
K_\Psi(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u),\quad
\partial_t\partial_uK_\Psi=\Psi''(t-u)=W_{\rm Weil}(t-u)
\]

as a distribution. This is classical mathematics; global positive definiteness of the completed kernel is RH-equivalent, **not established**.

Do not confuse **pointwise positive curvature** with **positive-definite correlations**. A scalar function \(\Psi(t)=t^4\) has nonnegative values and second derivative but the two-time Gram at \(t=\pm1\) is \(\begin{pmatrix}2&-14\\-14&2\end{pmatrix}\), determinant \(-192\). Conversely \(\Psi(t)=1-\cos t\) yields a positive Hilbert Gram with sign-changing pointwise curvature.

## 4. The quantum carrier can preserve causal histories without proving Weil positivity

Finite quantum measurements can be modeled by instruments \(K_o\), with \(\sum_oK_o^\dagger K_o=I\). Conditional outcomes have probability \(p_o=\mathrm{tr}(K_o\rho K_o^\dagger)\) and posterior state \(K_o\rho K_o^\dagger/p_o\). Recording the outcome does not require the reduced system state to retain every previous coherence.

The module **quantum_records.py** supplies an exact rational, real two-state example, with causal order, positive density matrices and immutable replayable observation histories. It is a genuine finite quantum-instrument model, **not** a description of a human mathematician.

For a positive semantic evidence distribution, an exponential-family normalizer

\[
Z(\theta)=\sum_n a(n)e^{\theta\cdot v(n)}
\]

has Hessian \(\nabla^2\log Z=\mathrm{Cov}(v,v)\succeq0\). A square-root encoding of probabilities makes that covariance a Hilbert metric. **Fake arithmetic sources also produce positive semantic covariances**; the equality with a particular Weil form requires its own source-sensitive theorem.

On the critical half-density, naive normalized finite arithmetic Hilbert vectors can converge weakly to zero while retaining norm 1. Their positive phase correlations can converge to a discontinuous limit. These are representation/topology countermodels—not evidence that physical observers or RH are pathological.

## 5. Ordinals distinguish three different operations

\[
O_0\to O_1\to\cdots,\qquad
O_\omega=\operatorname{colim}_{n<\omega}O_n,\qquad
R_{\omega+1}=\mathsf{Report}(O_\omega).
\]

At successor stages, an observed finite fact is added. At the mathematical limit, compatible records form an **ideal** colimit; this is **not** physical infinite elapsed computation. The \(\omega+1\) report is a *new typed operation* and may require independently justified axioms, a topology, or a theorem. The name “report” supplies no positive sign and no theorem by itself.

A strong classical finitary result applies to increasing first-order theories \(T_n\):

\[
\left(\bigcup_{n<\omega}T_n\right)\vdash_{\mathrm{finite}}\varphi
\iff
\exists n<\omega:T_n\vdash_{\mathrm{finite}}\varphi.
\]

Any finite proof uses finitely many axioms, all included at a common finite stage. **A formal limit does not manufacture additional finitary proofs.** A finite proof of a universal mathematical theorem might nonetheless exist by structural reasoning.

The software verifies finite stage support for a *supplied finite proof*; the general theorem is a short classical compactness argument, not an executed infinity.

## 6. Gödel, Turing, self-reference and proof strength

**Gödel:** finite proof codes can be checked, and for suitable effectively axiomatized consistent arithmetic theories, every particular “n is not a contradiction proof” instance can be provable without the theory proving its universal consistency \(\mathrm{Con}(T)\). This uses Gödel's second incompleteness theorem with its standard representability/derivability hypotheses. It says nothing about RH independence.

**Diagonalization:** a computable substitution operation can produce a self-indexed formula. Our typed syntax and injective encoding implement its **meta-level syntax**, but **not** the representability theorem *within PA*, so no mechanized Gödel theorem is claimed.

**Turing:** “program has not halted in its first n steps” is decidable for any specified n; the uniform all-n claim across all Turing-complete programs is undecidable. The two-counter module tests a genuine loop, a delayed halt and an immediate halt. This is not a proof that a specific fixed problem such as RH is independent.

**Ordinal proof progressions:** adding a consistency or uniform-reflection axiom at a successor can strengthen a theory, but the new logical commitment requires justification. It is not another ordinary observed event. Constructive ordinal notations, reflection strength and formal soundness have independent proof obligations.

**A separate semantic countermodel:** in a weak unary first-order language, interpret every named numeral as an ordinary natural for which \(P(n)\) holds, while an additional unnamed element fails \(P\). Then every named ground instance is true but \(\forall x\,P(x)\) is false. This is a correct *weak-language* countermodel, **not** a PA model.

## 7. Falsifiability, computable analysis and the RH interface

The observer's finite probe family can be insufficient to distinguish broader global mathematical structures. For a continuous real kernel, a strictly negative finite Gram witness can be perturbed to rational times and coefficients; a **rigorously sound interval oracle** can certify a negative upper bound.

The software uses exact Fraction interval arithmetic and strictly refuses unauthenticated floating values as certificates. A separate module certifies the **prime-source component** of Suzuki's kernel using rational logarithm/square-root enclosures; it deliberately does **not** claim the complete Gamma/pole term has been enclosed.

With a certified **completed** source evaluation, a strict negative Gram would refute global positivity; finite failure to find one is still unresolved. The RH-equivalent sign remains an independent missing theorem.

## 8. What counts as advancing the general theory

A substantial result must establish a new preservation/failure theorem about actual observations, formal proof, semantics, quantum instruments, restricted Yoneda probes, ordinal limits or second-order correlations. It must not merely rename a Gödel or Weil equivalence.

Examples of next honest targets:

- A typed functor from finite instruments and outcome records to informational semantics, with a *proved* data-processing law.
- Exact characterization of which observer/semantic maps preserve relevant causal histories and correlation structure.
- A machine-checkable proof of Gödel substitution representability and carefully scoped reflection hierarchies.
- A topology-controlled theorem for the \(\omega+1\) report, with counterexamples where finite positive states fail to glue.
- A rigorous Gamma/pole interval oracle completing the already-certified arithmetic prime side; then a genuine source-exclusive Weil sign investigation.

## Sources and provenance

Master historical file (unaltered): [founding dossier](../provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md).

Foundational references: Gödel (incompleteness), Turing (1939 ordinal logics), Feferman (reflection progressions), Suzuki (2023 screw function), Schoenberg (negative-type kernels), GNS and quantum-instrument theory. See full bibliography and caveats in the original dossier.

The physical carrier and semantic framing are the user's research hypotheses. Existing theorems retain attribution to their original authors. RH remains open.
