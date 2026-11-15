# Principia Observatoris — Quantum Haar Steering through a Gamma Causal Volume

**2026-11-14 · research-only proposed child of SUCC [#638](https://github.com/femboy2112/SUCC/pull/638).** This round answers the author's hypothesis: a source with entanglement might yield measurable conditional knock-on effects of a probabilistically chosen probe across an enlarging observer volume. The rigorous versions are (a) standard Bayesian conditioning with selection bias, (b) quantum steering with no-signalling, (c) real local disturbance and joint-state change, and (d) source-calibrated cross-boundary interactions. These are **not interchangeable**. No physical realization, ER geometry, original BBP entanglement, π normality or RH theorem is claimed.

**Grounding and provenance.** The original 16-child Haar, signed CDF-overlap and source-zero projector are in `docs/PI_NORMALITY_FRONTIER.md` and `research/2026-11-10/zero_anchored_lambda_haar/CONSTRUCTION.md`. Its zero-seed microscope is `research/2026-11-10/zero_seed_microscope/MICROSCOPE_THEOREMS.md`. Exact Gamma-volume convolution and positive Oily BBP source are in SUCC [#634](https://github.com/femboy2112/SUCC/pull/634) and [#636](https://github.com/femboy2112/SUCC/pull/636). The suspension is [#638](https://github.com/femboy2112/SUCC/pull/638); it is chosen continuous geometry, not a derived physical wormhole. The dual-endpoint Bell sector, X/Y phase probe, full-code coherence criteria, teleportation and ER=EPR audit **already exist** in [#601](https://github.com/femboy2112/SUCC/pull/601), especially `COHERENT_TWIN_PATHS.md`, `CARRIER_BOND_DUALITY.md`, `reviews/er_epr_equivalence_audit.md`. We cite those antecedents rather than claim priority for steering or CHSH.

## HGE-01 — Native radix-16 Haar parity on a causal observation cylinder (CLASSICAL / EXACT)

Let a digit word `p` of length `d` label a source-selected observed cylinder. Define the localized signed child character

\[
\psi_{p,8}(x)=16^{d/2}\mathbf1_{x\in I_p}(-1)^{a(x)},
\]

where `a(x)` is the next radix-16 digit and `16^(d/2)=4^d`. Under uniform Haar measure, `∫ψ_{p,8}=0` and `∫|ψ_{p,8}|²=1`, since among the 16 children eight have sign + and eight have sign −. Two such wavelets in disjoint or nested cylinders have zero inner product when their selected levels differ. The h=8 child digit character is **one** of the 15 independent 16-child Fourier/Haar detail modes, not the whole bank. Its associated diagonal quantum two-digit-code observable on `span{|0>,|1>}` is Pauli Z.

A classical digit Haar contrast is a functional of a diagonal probability law. A new *physical measurement in a complementary X/Y basis* is not derivable by postprocessing the already measured Z samples. The old SUCC `Q=C T_*` uniformly replaces the leading digit and is idempotent, while the Gamma dephasing channel below is a separate non-idempotent quantum semigroup. Equating these operators by the word "Haar" would be invalid.

## HGE-02 — Probe attraction changes the measured Haar law unless propensity is accounted for (CLASSICAL / PROVED)

On a fixed source history `H`, each lawful child experiment `a=0,...,15` has binary potential outcome with source-conditioned success probability `q_a`. The uniform Haar target is `C=(1/16)Σ_a ψ(a)q_a`, with `ψ(a)=(-1)^a` at the root. Choose `A` with strictly positive, history-predictable `π(a|H)`, then receive only its lawful outcome `Y`:

\[
\mathbb E[\psi(A)Y\mid H]=\sum_a\pi(a|H)\psi(a)q_a,
\quad
\boxed{\mathbb E\left[\frac{\psi(A)Y}{16\pi(A|H)}\mid H\right]=C.}
\]

The second is the inverse-propensity Horvitz–Thompson identity (not a finite-sample certainty). The `π` rule may be a softmax of expected information gain minus cost; its randomness must be included in the observer's own history. In the exact hostile example `q_even=3/4`, `q_odd=1/4`, policy mass per even child `3/32`, per odd child `1/32`: target `C=1/4`, naive signed report mean `1/2`, corrected mean `1/4`. If a child has `π=0`, the uniform target is **not generally identifiable** from observations without additional model restrictions. An unbiased estimator may also have high variance if propensities are tiny; no concentration or causal identification is claimed here without more assumptions.

## HGE-03 — Entire classical Haar probability hierarchy can conceal a nonclassical joint coherence (CLASSICAL / PROVED)

In the two marked-digit Hilbert subspace `|00>,|11>`, declare

\[
\rho_\gamma=\frac12\bigl(|00\rangle\langle00|+|11\rangle\langle11|
+\gamma|00\rangle\langle11|+\bar\gamma|11\rangle\langle00|\bigr),\quad|\gamma|\le1.
\]

For any effect diagonal in the complete two-party computational basis, its probability is **independent of** `γ`. Thus no amount of original-basis digit-Haar sampling (even its complete hierarchy) can distinguish entangled Bell `ρ_1` from the separable classical mixture `ρ_0` if the allowed instruments remain diagonal. In that toolkit the **entanglement target does not descend through observed evidence**, even though the diagonal source correlation `⟨ZZ⟩=1` is perfect. This is a strict, all-observations within that toolkit no-go, not a finite-count limitation.

Complementary joint Pauli readouts detect phase and contrast:

\[
\boxed{\langle XX\rangle=\operatorname{Re}\gamma,\qquad
\langle XY\rangle=-\operatorname{Im}\gamma,\qquad \langle ZZ\rangle=1.}
\]

In the source's `ρ_γ` family, joint X/Y readouts reconstruct `γ`. Their measurements require repeated preparations/accessible joint records, and noncommuting observables are not jointly sharp on one copy. A mere positive Gram, digit Haar coefficient, or probabilistic observer tendency does not imply that the original integer carrier contains such a bipartite Hilbert state.

## HGE-04 — Gamma volume generates a quantum source-dephasing semigroup, or preserves a co-moving gauge (CLASSICAL / PROVED)

Take **an additionally declared physical quantum system** on subsystems A and B. A phase at Gamma waiting time `t` acts on A as `U_t=diag(1,e^{iωt})`. Let `g_α` be the authentic mathematical Gamma convolution semigroup from #634 (`g_0=δ_0`). The quantum channel

\[
\mathcal D_{\alpha,\omega}(\rho)=\int_0^\infty g_\alpha(t)
 (U_t\otimes I)\rho(U_t^\dagger\otimes I)\,dt
\]

is CPTP because it is a positive mixture of unitary channels and satisfies `D_αD_β=D_(α+β)` by `U_tU_s=U_(t+s)` and Gamma convolution. On the marked sector,

\[
\boxed{\rho_\gamma\mapsto \rho_{\gamma(1+i\omega)^{-\alpha}}.}
\]

**Gauge-calibrated alternative:** if the same source phase acts as `U_t` on A and `\bar U_t` on B, the two branches `|00>,|11>` are both unchanged; the entire marked bond `ρ_γ` is invariant. An actual co-moving *representation* change need not dephase. By contrast, averaging an **unrecorded one-sided physical phase** reduces coherence; these must not be identified. A common twirl that preserves the state is not automatically gauge in nature unless its representation transformation genuinely preserves the source and target.

At integer `α=2`, `ω=1`, the factor is `(1+i)^(-2)=-i/2`. The state has `⟨XX⟩=0`, `⟨XY⟩=1/2`, `⟨ZZ⟩=1`: a naive **fixed XX-only experiment** would misidentify it as the separable `ρ_0` even though the correct quadrature is nonzero. The optimal CHSH bound for this two-qubit family is `S_max²=4(1+|γ|²)` by the classical Horodecki two-qubit singular-value criterion. At `γ=-i/2`, `S_max=√5>2`; in the same family, the partial transpose has a two-dimensional minor `-|γ|²/4<0`, showing entanglement. This is a **mathematical quantum model**, not an observed Bell violation. An actual experimental test requires distinct random local settings, spacelike separation when claimed, raw trial counts and uncertainty accounting.

## HGE-05 — The hidden-information "knock-on" is a conditional assemblage, not remote signaling (CLASSICAL / PROVED)

Alice chooses a projective basis `x` and records outcome `a`. The unnormalized source-conditioned remote ensemble is

\[
\sigma^B_{a|x}=\operatorname{Tr}_A[(P^x_a\otimes I)\rho_{AB}(P^x_a\otimes I)],
\qquad \boxed{\sum_a\sigma^B_{a|x}=\rho_B\quad\forall x.}
\]

In our `ρ_γ` sector, the two X-basis outcomes occur with probability `1/2` and Bob's **conditional** states are

\[
\boxed{\rho_{B|a,X}=\frac12\begin{pmatrix}1&a\gamma\\a\bar\gamma&1\end{pmatrix}.}
\]

For `γ=1`, Bob's conditional states are distinct X eigenstates. For `γ=0`, Bob's conditional X states are both maximally mixed, although computational-basis Z correlations are identical in both models. For every `γ`, forgetting A's outcome returns `ρ_B=I/2`. Thus detecting a change in Bob's **unconditioned local statistics** merely from Alice's distant choice would contradict this declared local-quantum-mechanics model. To correlate conditional records, Alice's outcome must become available at a later common meeting or via an allowed classical channel. These predictions do **not** require or demonstrate a traversable ER bridge.

A local trace-preserving measurement can absolutely change the **joint** state: forgetting a Z outcome transforms `ρ_1` into `ρ_0` while Bob remains `I/2`. The "hidden connection" can change for the joint observer without any remote controllable signal. Distinguish *state of the joint source*, *conditioned Bob state*, and *unconditioned Bob state*. Actual physical backaction on an independently controlled distant B marginal requires a declared interaction/coupling and causal access, as in SUCC #601's fresh-message intervention countermodel.

## HGE-06 — Evidence-driven higher-slice probe: an exact success and false-confidence control (CLASSICAL / PROVED)

Predeclare candidate `H_1:γ=-i/2` (Gamma-depth-two entangled), versus `H_0:γ=0` (dephased separable). Under both, repeated **Z/Haar** agreement is certain and produces likelihood ratio exactly one: repeating it does not discriminate the two. The complementary XY product `+1` occurs with probability `3/4` under H_1 and `1/2` under H_0. For `n` independently prepared fresh copies with positive XY outcomes and equal initial odds, the exact posterior is

\[
\boxed{\Pr(H_1\mid +^n,XY)=\frac{3^n}{3^n+2^n}.}
\]

At n=4 it is `81/97`. This provides a model where a source-labelled, complementary high-slice probe can accumulate genuine discriminating evidence. Feeding four duplicates of one observation into the same product formula is **invalid**, as is treating the observer's predictable basis choice as an extra source likelihood. If the real carrier is classical common-cause, no Bell witness survives complete causal/measurement checks; matched classical correlations are an essential hostile model.

## HGE-07 — General observable transport through causal volume; limits of Haar commutation (CLASSICAL)

For any bounded effect `E` on the joint Hilbert space, the measured coefficient after Gamma propagation is

\[
\operatorname{Tr}[E\mathcal D_\alpha(\rho)]
=\int_0^\infty g_\alpha(t)\operatorname{Tr}[U_t^\dagger E U_t\rho]dt.
\]

If an observable is an eigenoperator of the adjoint phase action with frequency `ω`, the corresponding amplitude is multiplied by a Gamma character `(1\pm iω)^(-α)` with sign determined by the explicitly declared orientation. In our model, the **diagonal digit Haar sector** is invariant while two complementary quadratures mix and attenuate. No general statement that a 16-ary Haar transform diagonalizes every causal quantum instrument is licensed; gauge/source action and measurement effect must be transported together.

This is the most useful exact bridge between: a radix-16 Haar source code, the Gamma causal-volume semigroup and entangled joint instrument statistics. It is an operator/effect dictionary for a **declared** finite quantum carrier. Its existence does not prove the arithmetic BBP forcing is a qubit channel or identify a wormhole metric.

## HGE-08 — What the ER=EPR proposal needs next (CONJECTURED interface / UNVERIFIED physical identification)

The already-authored #601 coherent twin and bond correspondence proves a finite encoded-state/POVM dictionary and separate message-intervention no-go; it does not derive gravity. The original ER=EPR proposal of Maldacena–Susskind concerns entangled black-hole wormholes and conjecturally broader entanglement, not an observed mechanical force from generic mathematics. The present round supplies a plausible **source-probe program**, not a theory of physical wormholes: prepare a source-calibrated bipartite state; preregister local Z and complementary X/Y probes; randomize each lawful basis choice; record outcomes, timings, gauge/frame calibration and any physical coupling; test conditional steering, unconditioned no-signaling, Bell witness and the joint-source channel against a separable common-cause control. Compare only current transported observables at a declared rendezvous, not presumed remote histories.

**A useful source-term split:** a receiver-only local marginal response under Alice's chosen intervention is **zero** for every local CPTP Alice operation in the no-communication model. A nonzero response after an allowed coupling would be a new causal dynamical effect, not implied by entanglement. To test whether a proposed **ER** geometry describes the same experiments, provide an independent gravitational boundary dictionary, actual metric/field dynamics, communication resources and numerical/rigorous calibration. Boundary-state equivalence does not uniquely determine bulk geometry.

### Proof/claim ledger and falsification

| ID | Status | Falsifier/limitation |
| --- | --- | --- |
| HGE-01 | CLASSICAL / EXACT | Nonzero mean or wrong scale norm in genuine 16-child Haar under uniform measure |
| HGE-02 | CLASSICAL / EXACT | Biased policy yields the same claimed uniform estimate without propensity correction |
| HGE-03 | CLASSICAL / PROVED | Any diagonal digit-effect distinguishes `ρ_γ` from `ρ_0` |
| HGE-04 | CLASSICAL / PROVED, declared Gamma+unitary source | Gamma semigroup/composition or XY quadrature fails in exact two-qubit matrices |
| HGE-05 | CLASSICAL / PROVED | Receiver local marginal changes under trace-preserving A-only operation |
| HGE-06 | CLASSICAL / PROVED, independent fresh-copy model | Z test separates models; copied outcome licenses a multiplied likelihood |
| HGE-07 | CLASSICAL conditional transport | Non-equivariant measurement basis incorrectly compared without gauge rotation |
| HGE-08 | CONJECTURED mechanism / PHYSICAL UNVERIFIED | Real source lacks required quantum state, instrument or geometry |

**SUCC frontiers:** π base-16 normality, R0, source-selected signed temporal Haar/CDF overlap, completed Weil positivity and RH remain **OPEN**. The *existing* `Qν` of the π frontier is a **classical comparison operator**, not a Bell instrument. Positive Oily Gamma and coherent twin Hilbert channels have different source types; no morphism between them has yet been authenticated.

**Primary/general literature:** Maldacena & Susskind (2013), *Cool horizons for entangled black holes*, arXiv:1306.0533; Gao–Jafferis–Wall (2017), *Traversable Wormholes via a Double Trace Deformation*, arXiv:1608.05687; Maldacena–Stanford–Yang (2017), *Diving into traversable wormholes*, arXiv:1704.05333. Quantum steering: its assemblage/no-signaling definition as in peer-reviewed `npj Quantum Information` 8 (2022), DOI 10.1038/s41534-022-00633-0. Bell inequality: Hensen et al. (2015), Nature 526, 682–686, DOI 10.1038/nature15759; Horodecki et al. (1995), Phys Lett A 200, 340–344, DOI 10.1016/0375-9601(95)00214-N. Classical Haar/probability correction: inherited SUCC source; Horvitz–Thompson 1952. No academic novelty is claimed for these classical foundations.
