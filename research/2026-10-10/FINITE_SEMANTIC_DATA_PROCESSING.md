# A finite physical observer's semantic data-processing theorem

**Date:** 2026-10-10/11. **Status:** CLASSICAL theorem, exact new-to-project implementation and causal/quantum test; no experimental neuroscience claim.

**Code:** observational_succ/operational_semantics.py; observational_succ/quantum_records.py.

**Tests:** tests/test_operational_semantics.py; tests/test_quantum_records.py.

**Reproduce:** python scripts/semantic_data_processing_probe.py

## 1. Physical carrier, observed data, semantic readout

Begin with a physical measurement instrument acting on a finite real-qubit quantum state. It produces an outcome in a finite alphabet \(X\), distributed according to a classical probability vector \(p=(p_i)\).

An observer can subsequently translate those outcomes into semantic symbols \(Y\) via a **declared stochastic channel** \(C_{ij}=\Pr(Y=j\mid X=i)\), with \(C_{ij}\ge0\) and \(\sum_j C_{ij}=1\).

The translated law is \((Cp)_j=\sum_i p_i C_{ij}\).

This represents an explicit, testable layer of **semantic postprocessing of already observed outcomes**, not an empirical model of all human understanding. In particular, one may keep the original immutable outcome record even if a compressed semantic representation is lossy.

## 2. Unconditional exact theorem

For any two possible finite evidence laws p and q on the same input labels, define the total-variation distance

\[
\operatorname{TV}(p,q)=\frac12\sum_i |p_i-q_i|.
\]

Then

\[
\boxed{\operatorname{TV}(Cp,Cq)\le\operatorname{TV}(p,q)}.
\]

**Proof:** Let \(\delta_i=p_i-q_i\). By positivity and row normalization,

\[
\begin{aligned}
2\operatorname{TV}(Cp,Cq)
&=\sum_j\left|\sum_i C_{ij}\delta_i\right|\\
&\le\sum_{j,i} C_{ij}|\delta_i|\\
&=\sum_i|\delta_i|\sum_j C_{ij}\\
&=\sum_i|\delta_i|=2\operatorname{TV}(p,q).
\end{aligned}
\]

This is an exact theorem for all finite stochastic readouts, not an inference from sampling or a conjectural quantum effect. The Fraction-based implementation checks its hypotheses and computes rational before/after distances and slack without floating-point approximations.

**Composition:** If a second readout D accepts the symbols of C, then the composite DC is again stochastic. Therefore

\[
\operatorname{TV}(DCp,DCq)
\le\operatorname{TV}(Cp,Cq)
\le\operatorname{TV}(p,q).
\]

## 3. Quantum-to-semantic example

Take the two physical states \(|0\rangle\) and \(|1\rangle\). Measuring in the Z basis yields outcome laws (1,0) and (0,1), with TV distance 1. Measuring in the X basis yields (1/2,1/2) for both, with TV distance 0.

Even the perfectly distinguishing Z outcomes may be pushed through a forgetful semantic channel \(C\) mapping both labels to the single word “observed”, yielding TV 0. This does not retroactively alter the physical source state or delete a separate actualized causal record.

**Interpretation:** The larger physical carrier may contain distinctions invisible to the chosen semantic probe family. That is a precise **restriction-of-observability** result consistent with the author's physical-carrier intuition.

The result does **not** show that observers cannot derive valid universal mathematical theorems, does **not** say that semantic understanding is necessarily lossy, and does **not** imply the Weil functional is positive.

## 4. Adversarial and positive controls

- Identity semantic channel: distance preserved exactly, slack 0.
- Complete erasure channel: positive source distance becomes 0, slack equals original distance.
- Binary noisy channel with probabilities 3/4 and 1/4: maximally distinct inputs have output TV 1/2.
- Stochastic composition: exact agreement between direct composite and two successive applications.
- Illegal inputs: negative weights, totals not one, repeated labels, floats, label mismatches, malformed/incomplete Kraus instruments, and invalid quantum density matrices are rejected.
- A real-qubit physical measurement is distinguished from subsequent classical postprocessing; quantum states are not interpreted as semantic probabilities without the measurement map.

## 5. How this improves general Observational SUCC

It is a **proved preservation inequality** for one previously hypothetical arrow:

\[
\mathsf{PhysicalMeasurementOutcomes}
\xrightarrow{C}
\mathsf{SemanticReadout}.
\]

The arrow is not an arbitrary semantic functor, but its exact source, codomain, and information-loss law are specified.

This suggests a next theorem target: characterize the families of probes whose semantic postprocessing is *sufficient* to reconstruct particular causal-history invariants, and connect that to restricted Yoneda representations. The counterexample in which distinct histories receive the same semantic word shows why a faithful functor cannot be assumed.

**RH thread:** A positive covariance formed AFTER a forgetful observer readout may be incapable of detecting a counterfeit arithmetic source. Any observer-based Weil proposal must therefore prove that its selected observable/report functor is sufficiently source-faithful before a positivity theorem can be meaningful. This is a necessary architectural constraint, not RH progress by itself.

## 6. Status summary

- **CLASSICAL:** total-variation data-processing inequality for finite stochastic channels.
- **PROVED LOCAL:** exact rational channel composition and non-erasing causal-record distinctions.
- **TESTED MODEL:** real two-state Kraus measurements of Z and X, as implemented.
- **HYPOTHESIS:** a physical human mathematician's complete semantic understanding is described by a particular channel or category.
- **UNVERIFIED:** arbitrary semantic inference is contractive in this metric; observer covariance equals the complete Weil form; RH.
