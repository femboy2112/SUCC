# Null-Information Operations Must Conserve Observer Memory — a Strict Control for Source-Phase Interferometry

**Operation:** Source-Null / Adaptive Haar / Knowledge Volume / BBP relative-phase continuation  
**Date:** 2026-11-18  
**Originating observation (Leah):** A legitimate null-information operation should **neither strengthen nor weaken an observer's current model or the probability of its selecting the next key discriminating probe**. Otherwise a purported boundary observation contaminates the observer rather than measuring the carrier.

**Status:** NMC-01–04 are classical conditional-independence, decision-theoretic, and finite counterexample statements under declared hypotheses. NMC-05 is a proposed mandatory methodological contract for SUCC, not a physical theorem. No π normality, R0, physical vacuum-energy, or independent mathematical-priority claim.

## 1. Why a numerical zero or mean-zero marginal is not an epistemic null

Fix a finite source/hypothesis class \(\Theta\), a fully retained observer record \(M\), an optional randomized observation \(Z\), and a declared joint law \(P\). Do not confuse:

- **Value null:** \(Z=0\) for an event. This may be highly informative if \(P(Z=0\mid\Theta,M)\) varies by source.
- **Marginal mean null:** \(\mathbb E Z=0\). This does not even imply \(I(\Theta;Z)=0\).
- **Marginal information null:** \(I(\Theta;Z)=0\). This need not imply that \(Z\) is uninformative to an observer remembering \(M\).
- **Memory-conditioned information null:** \(I(\Theta;Z\mid M)=0\). This is the correct **current-knowledge** criterion relative to a fixed \(\Theta,M,P\).
- **Operational strong null:** memory-conditioned information null **plus** recoverable old memory, unchanged admissible future experiment laws/costs, and unchanged next-probe selection policy under the designated sham. This is stronger than mere conditional information neutrality.

For positive-probability conditioning events, \(I(\Theta;Z\mid M)=0\) iff
\[
\boxed{P(\Theta=\theta\mid M=m,Z=z)=P(\Theta=\theta\mid M=m)}
\tag{NMC1}
\]
for almost all \((m,z)\). Source-uniform neutrality for **all** admitted priors is ensured by the stronger family statement
\[
\boxed{P_\theta(Z\in dz\mid M=m)=K(dz\mid m)\quad\text{for every }\theta}
\tag{NMC2}
\]
on the support of each source model. This is a conditional Blackwell-null experiment, not a claim that \(\Theta\) is metaphysically random.

The original π source is deterministic. The probability model, when used, describes an observer's declared candidate source class, randomized instruments and policies. Do not infer a probability of π normality or random digits from it.

### NMC-01 — "null alone" can hide a complete bit from the remembered observer (PROVED CLASSICAL)

Take \(\Theta,R\) independent uniform signs in \(\{\pm1\}\). Let the **existing memory** be \(M=R\) and the proposed new readout \(Z=\Theta R\). Then:
\[
\boxed{I(\Theta;Z)=0,\quad I(\Theta;Z\mid M)=1\text{ bit},\quad \Theta=MZ.}
\tag{NMC3}
\]
Every standalone law of \(Z\) is a uniform random sign; nevertheless, the observer *already remembers the reference mask* and can decode the entire source bit. A probe classified "null" without conditioning on retained memory is a **false negative** for information gain.

This is exactly the logic of the shared-origin BBP phase probe \(A_n=M z_n,\ B_n=M z_{n+1}\). Individually each is Haar-uniform, yet once \(A_n\) is stored, \(B_n\) reveals \(z_{n+1}\bar z_n\) through their product. The relative phase remains a deterministic circle statistic; randomness belongs to the chosen mask, not the π digits.

### NMC-02 — a presently null observation may be an *option-value intervention* (PROVED CLASSICAL)

Let \(\Theta,R\) again be independent uniform signs and initial memory \(M\) empty. A structural step reports/stores \(R\). Then
\[
I(\Theta;R)=0.
\]
However if the next available sensor is **coupled to that same stored** \(R\) and yields \(Y=\Theta R\),
\[
\boxed{I(\Theta;Y\mid R)=1\text{ bit},\qquad I(\Theta;Y)=0.}
\tag{NMC4}
\]
Replacing that sensor's mask with a fresh independent \(R'\) eliminates recoverability from \((R,Y')\), with \(Y'=\Theta R'\).

The first step leaves the *current posterior* unchanged but can create a new **future instrument capability**. It is not a strong operational null relative to the entire future probe system. This is the exact class of phenomenon studied in Main XXVI [Adaptive Haar AH-03/04](https://github.com/femboy2112/SUCC/blob/main/research/2026-11-15/observer_haar_causal_volume/THEOREMS.md). It is legitimate **knowledge-sheet ascent**, but it must not be counted as a neutral sham.

### NMC-03 — preserving beliefs alone does not preserve discovery probabilities (PROVED DECISION CONTROL)

Take a trivial memory and a designated next discriminating probe \(q_\star\). Before intervention the observer's policy selects \(q_\star\) with probability 1. A new **source-independent fair coin** \(R\) has \(I(\Theta;R)=0\), yet a policy mutation "use \(q_\star\) iff \(R=1\)" reduces the probability of choosing \(q_\star\) to \(1/2\).

Thus posterior neutrality cannot establish the probability of the next key probe is unchanged. To call a control *fully neutral* also require equality of the next-action kernel:
\[
\boxed{\pi_{\mathrm{sham}}(q\mid M=m,z)=\pi_{\mathrm{baseline}}(q\mid M=m)}
\tag{NMC5}
\]
for every actual positive-probability sham outcome (or an explicitly coarser equality in distribution when that is the preregistered operational target), and matching action availability, computational costs, time budgets and source passport. Otherwise selection effects contaminate the comparison.

## 2. A typed strong-null operation, and the intended lift

Represent the observer as \(S=(M,\Pi,\mathcal A,C,\tau)\), where \(M\) is the retained record, \(\Pi\) the posterior/model and inferential closure, \(\mathcal A\) the set of legal next probes, \(C\) the cost/resource model, and \(\tau\) the source/time passport.

A proposed null operation maps \(N_0:S\mapsto S'\). To be **memory-faithful**, require a lawful retraction \(r\) satisfying
\[
\boxed{r\circ N_0=\operatorname{id}_S.}\tag{NMC6}
\]
This is an idealized information-preservation condition; a physical measurement that consumes irreversible resources must disclose its actual cost and generally cannot satisfy perfect cost neutrality.

To be **epistemically neutral**, require NMC1 (or the source-family form NMC2); for a deductive model with no probabilities, a suitable analogue is a conservative extension:
\[
\boxed{\mathrm{Cl}(S')\cap\mathcal L_{\rm old}=\mathrm{Cl}(S)}
\tag{NMC7}
\]
under the same inference rules and old-language claims, with old evidence preserved through \(r\). This statement is a *declared gate*, not a theorem about all arbitrary representation maps.

To be **continuation neutral**, require an experiment- and policy-preserving comparison under an explicitly matched baseline:
\[
\boxed{
\mathcal A_{\rm sham}=\mathcal A_{\rm baseline},\quad
C_{\rm sham}=C_{\rm baseline},\quad
\mathcal L(Q_{\rm next}\mid S,\operatorname{do}N_0)
=\mathcal L(Q_{\rm next}\mid S,\operatorname{do}\operatorname{id}).
}
\tag{NMC8}
\]
To preserve the **probability of a future discovery**, not merely the next chosen probe, also require the conditional *future probe outcome* law to match under the same source and action:
\[
\boxed{\mathcal L(Y_{\rm next}\mid\Theta,M,Q_{\rm next}=q,\operatorname{do}N_0)
=\mathcal L(Y_{\rm next}\mid\Theta,M,Q_{\rm next}=q,\operatorname{do}\operatorname{id})}
\tag{NMC8b}
\]
for every admissible \(q,\Theta,M\), with budgets/time and admissible interventions held fixed. For a multi-step discovery event, require a declared continuation-kernel equivalence under each allowed fixed policy, or prove a finite-horizon induction from matched controlled kernels. Equality of the query distribution *alone* cannot establish equality of eventual discovery chances.

If the null step prepares a shared mask used by later sensors, NMC8b may fail even while NMC1 is satisfied; classify the step as **option-value instrument preparation**, not a neutral control.

Under a fixed action set and equal costs, the classical posterior-neutral experiment does not change **optimal one-step Bayes decision value**, because the posterior is unchanged at each sham outcome. This statement does not ensure an actual, potentially randomized or suboptimal policy will choose the same next probe.

### NMC-04 — strong-null control versus deliberate second-order lift

To test a source phase \(Z_\theta\), precommit the observer to a particular future experiment and an immutable memory snapshot \(M_0\).

- **Matched sham** \(N_0\): leave old memory and future action law intact; add only a source-independent readout that is never reused as a hidden shared reference. If budgets/time are used, pay the same cost on both arms. Compare with the declared baseline without conditioning on an unblinded future probe choice.
- **Active lift** \(L_p\): permit shared reference masks. For unit-circle source phase \(Z\), independent Haar masks \(R,R'\), and \(J_p\sim\operatorname{Bernoulli}(p)\),
  \(A=R,\ B=Z(J_pR+(1-J_p)R')\).
  Each one-channel marginal is Haar, but
  \[
  \boxed{\mathbb E[\bar A B\mid Z,p]=pZ.}
  \tag{NMC9}
  \]
  Conditional on **remembering A**, B is informative. The lift is **intended to change the available joint information**, and therefore must not be called globally neutral.

A measured improvement in next-probe discovery is attributable to the chosen joint instrument only if the sham kept the prior information, policy, resources, action set, time schedule, and source passport matched. A null-looking marginal is insufficient.

## 3. Source-specific acceptance for the BBP normality offensive

The authentic source is the original signed four-pole \(r(n)\), exact \(U_0=0\), \(U_{n+1}=16U_n+r(n+1)\), and the selected completion \(U_n+T_n=16^n\pi/16\). A proposed BBP null operator or line-to-circle spectral measurement must preserve:

1. The **entire prior source and observation record** (zero-seed as null *homogeneous input*, not an unknown value; four poles, clock, carries, positive tail, phase, original source map).
2. All existing arithmetically justified finite certificates and their original reference frames, not merely numerically equal summary outputs.
3. The predetermined next-probe decision rule and compute budget under sham comparison; do not let irrelevant random masks push the reasoner toward/away from a favorable probe.
4. Explicit **phase/lag reference reuse only in the active lift**; never present source-blind new noise as actual π phase cancellation.
5. A frozen, source-valid signed prediction for the active second-order response, measured against the original locked, changed-seed, source-matched and independently randomized controls.

No memory-neutrality principle itself supplies an all-shell source-selected bound for \(W_B(h)\) or the rational Gram observer. It is an **identifiability/experimental-design firewall**, not a proof that the actual original π orbit is normal.

## 4. Claim ledger / next falsifier

| Claim | Status | Exact scope |
|---|---|---|
| NMC-01 | CLASSICAL / PROVED PAPER | Unconditionally source-blind Z can be fully informative given retained M; explicit XOR/sign calibration |
| NMC-02 | CLASSICAL / PROVED PAPER | Source-independent first probe can prepare a future coupling, giving positive option value while current posterior remains fixed |
| NMC-03 | CLASSICAL / PROVED PAPER | Source-independent randomized intervention can change next-probe selection; action invariance needs an independent contract |
| NMC-04 | MODEL CONTRACT | Reversible record, conditional posterior invariance, conservative old inference, same action/cost/time law under sham |
| NMC-05 | PROPOSED SUCC METHODOLOGY | Sham/lift separation for signed BBP boundary and relativized null-information operations |
| π R0 and full normality | OPEN | Requires original-source all-late-shell signed phase estimate, not a null information calibration |

**Provenance:** [Main Adaptive Haar AH-03/04](https://github.com/femboy2112/SUCC/blob/main/research/2026-11-15/observer_haar_causal_volume/THEOREMS.md), [Main Principia knowledge/proof](https://github.com/femboy2112/SUCC/blob/main/docs/principia_observatoris/03_knowledge_proof.md), [research source-null section #657](https://github.com/femboy2112/SUCC/blob/research/defect-window-tomography-2026-11-16/research/2026-11-17/causal_clock_scrambling/SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md), [movable-boundary order-lift](https://github.com/femboy2112/SUCC/blob/research/defect-window-tomography-2026-11-16/research/2026-11-16/defect_window_tomography/MOVABLE_BOUNDARY_ORDER_LIFT.md), and current signed BBP Gram-observer work in this conversation. Exact source/policy comparison is required before claiming an agent's next-probe probability improved.
