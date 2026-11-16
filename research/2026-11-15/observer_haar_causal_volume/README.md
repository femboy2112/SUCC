# When a learned connection opens a deeper probe

Continuation of [draft #639](https://github.com/femboy2112/SUCC/pull/639),
at parent `2c73e6388b24c7a66683d089733105d14acda08a`.

The author's proposal asks whether an observer can choose its overall frame
while selecting particular observations probabilistically, and whether repeated
correlated structure can promote probes into finer knowledge slices. It also
asks whether hidden entanglement would leave detectable effects in later
observations. This round constructs explicit models and discriminators for
both questions, retaining the original SUCC source and its classical controls.

## The earned connection

**A structural observation can have zero immediate information about a target
and still increase the value of the next observation.** In the explicit model,
a hidden bit S determines whether the deeper instrument is connected to a
still-unknown target theta. If p=Pr(S=1), the deeper response has Haar contrast
p, squared detail p^2, and expected information

\[
I(p)=\tfrac12[(1+p)\log(1+p)+(1-p)\log(1-p)],\qquad
\tfrac12p^2\le I(p)\le(\log2)p^2.
\]

A coarse structural probe C changes p to p_C without revealing theta. Its
weighted Haar energy is Var(p_C), and

\[
\mathbb E I(p_C)-I(p)\ge\tfrac12\operatorname{Var}(p_C).
\]

The full four-state belief is retained after deep observations. Favorable
fresh evidence can raise deeper-probe odds under the specified stochastic
policy; copied evidence, a missing instrument, and arbitrary overconfidence
cannot. A two-stage example has positive utility even though both one-step
choices have negative utility, with rational certificates for the inequalities.

## The original causal volume already contains Haar slices

For the authentic Oily kernel and source law

\[
R(x)=\frac{4-2x^3-x^4-x^5}{16-x^8},\qquad
\mu(dx)=16R(x)dx/\pi,
\]

the inherited retained-source Gamma-depth covariance decomposes exactly into
weighted dyadic Haar coefficient products. At native unit depth,

\[
\frac{7\pi-20}{5\pi^2}
=\sum_I |c_I(a)|^2,
\quad a=1-x+x^3/2-x^4/4.
\]

Every finite dyadic level contributes positive detail. After J levels, the
unresolved variance is positive and at most 4^(-J)/4. The code certifies cell
masses, detail energies and residuals with exact rational enclosures derived
from the original four-channel kernel, without a pi or quadrature oracle.

This Haar observer acts on the source coordinate x. The existing zero-anchored
BBP Haar instrument acts on the completed radix phase. An intertwiner between
those two reports is still required; the new decomposition does not prove
phase equidistribution.

For a declared reversible finite Markov source, Gamma averaging also gives the
operator identity

\[
PG_{2\alpha}P-(PG_\alpha P)^2
=\sum_j(D_jG_\alpha P)^*(D_jG_\alpha P).
\]

This is a precise hidden-slice response and is already present in entirely
classical models. Its norm is bounded; it need not increase with Gamma depth.

## What would distinguish hidden entanglement

The finite two-qubit controls preserve the difference between a coherent Bell
state and a dephased classical mixture with identical same-basis probabilities
and identical local marginals. A local Haar/Hadamard basis rotation exposes
complementary coherence under trusted qubit measurements.

Same-basis conditional updates occur in both models. All restricted X/Z
setting-pair statistics of the Bell example can even be copied by two shared
classical signs if no qubit-device model is trusted. An additional rational
rotated-setting experiment supplies a CHSH discriminator: the chosen partially
coherent state gives exactly 5/2, above the local bound 2. This is a mathematical
prediction, not a physical Bell experiment or an observation of BBP.

Local outcome-forgotten measurements leave the remote marginal unchanged.
Changes in later joint complementary-basis measurements can reveal destroyed
coherence; selected remote states must be averaged with their actual outcome
probabilities. The code rejects the unweighted-average mutation that would
manufacture a signal.

ER=EPR remains a separate, model-specific gravitational/holographic question.
The inherited arithmetic thermofield construction is credited, but neither a
Haar transform nor a simulated quantum instrument supplies a gravitational
dual or physical source authentication.

## Read and reproduce

- [Theorems AH-01 through AH-10](THEOREMS.md): definitions, proofs, exact domains.
- [Hole contract](HOLE_CONTRACT.md): preregistered target and failure controls.
- [Claim ledger](CLAIM_LEDGER.json): earned status and remaining hypotheses.
- [Provenance](PROVENANCE.md): original source pins and primary references.
- [Validation](VALIDATION.md): actual runs, counts and limitations.
- [Next probes and TLICA interface](NEXT.md): source and instrument obligations.
- [Constructor notes](CONSTRUCTOR_NOTES.md): full belief, Haar/MI bridge, option value.
- [Translator notes](TRANSLATION_NOTES.md): original-source Haar decomposition and Gamma proofs.
- [Adversary notes](ADVERSARY_NOTES.md): classical controls, no-signalling and Bell settings.
- [Adaptive observer code](../../../observational_succ/adaptive_haar_observer.py).
- [Haar/Gamma and source certificates](../../../observational_succ/haar_gamma_bridge.py).
- [Quantum instrument controls](../../../observational_succ/haar_quantum_instruments.py).

All changes are additive research work. Written proofs justify their universal
claims; finite tests validate implementations within their declared budgets.
