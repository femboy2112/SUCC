# Probe-coherence horizons, destructive carrier access and proof-induced graph contraction

**Research date:** 2026-10-11. **Author's originating concepts:** the inverted-dual/minimal-support shape of proofs, field question-rewiring under proof absorption, and *FuckedFields* in which constructing a local proof perturbs its carrier and destroys the coherence of the remaining proof-relevant probes. “Riemann sphere” and “black-hole horizon” were stated as **metaphors for a boundary of meaningful observation**, explicitly **not** an asserted literal Riemann-sphere, holographic, spacetime or RH geometry.

**Status:** exact finite model, explicit mathematical no-go for a **bounded class of destructive source-measurement protocols**, adversarial tests, positive repairs; all extrapolations to mathematical RH proofs, quantum geometry, physical singularities, full categorical sheaf descent and actual human observers are **UNVERIFIED**.

**Repository dependencies:** PR #11 twin observers and PRs #10→#6; do not alter pinned RH import/provenance or historical defaults. This is freestanding general Observational SUCC work.

## 1. What does it mean for a probe to stop making sense?

Fix an **initial source** \(s_0\) in a declared class \(X\). A carrier configuration \(c\in C\) supports a collection of *typed* observations \(p:C\supseteq D_p\to Y_p\) and updates under each admissible probe:
\[
c\xrightarrow{p/y}u_p(c),\qquad y=p(c).
\]

For a statement about the **initial** source \(s_0\), the proof requires more than a numeric observation \(y\). It requires justified provenance that \(y\) represents a specified property of **that same initial source**; write
\[
(c,h)\models\mathrm{SupportsInitial}(p,y).
\]

A probe may remain meaningful as a measurement of the **current modified carrier** even when it ceases to represent a property of the initial source. This is the crucial type distinction. “Probe meaning collapses” need not mean the sensor stops emitting data; it may mean that the data no longer inhabit the source-relevant evidence type needed for the proposed theorem.

A **coherence horizon relative to target \(T\), allowed interventions \(\Pi\), and evidence contract \(\mathcal E\)** occurs when, within every admissible protocol from the initial source, the transition required to obtain some crucial witness destroys the remaining support needed to certify \(T(s_0)\) before a valid complete certificate can be assembled.

This is *operational nonrealizability*, not logical unprovability. A mathematical proof using independent axioms might establish \(T\) without actualizing any of the problematic physical probes.

## 2. Exact finite single-carrier theorem

Let \(X=\{(a,b):a,b\in\{0,1\}\}\), with target
\[
T(a,b)=a\oplus b.
\]
The local observer has **one** source carrier, initially \((a,b)\). There are two physical probes:

- **A-probe:** return current \(a\), then overwrite \(b\gets0\).
- **B-probe:** return current \(b\), then overwrite \(a\gets0\).

A reading of \(a\) after B-probe may be truthful about **current** \(a=0\), but cannot certify **initial** \(a\). Similarly B after A-probe cannot certify initial b. No copy, reset-to-original, nondestructive joint measurement or independent mathematical law may be assumed.

**Theorem (PROVED LOCAL).** No finite deterministic adaptive protocol using only these two probe operations on one source carrier can correctly decide the initial parity for **every** \(s_0\in X\). This remains true if the protocol performs arbitrarily many repeats after the first probe.

**Proof by indistinguishability:**

- If the first action is A-probe, the initial worlds \((0,0)\) and \((0,1)\) both yield a=0 and transition to the *same carrier* \((0,0)\) with the same event history/semantic flags. They have opposite original parity. Every later adaptive action yields identical transcripts in both worlds, so no output can be correct for both.
- If the first action is B-probe, the worlds \((0,0)\) and \((1,0)\) both yield b=0 and transition to the same carrier \((0,0)\), again with opposite parity. Future transcripts are identical.
- A strategy that never probes cannot distinguish any of the four original worlds.

Since each deterministic adaptive strategy must either stop or choose A/B first, every such strategy fails on some true source.

**Individually meaningful knowledge persists:** after A-probe, the observer knows the initial value of a. It may thereby determine every global property that is a known function of a. But it cannot infer the initial parity uniformly over X, and the later modified-carrier b=0 reading may not be laundered into an observation of initial b.

**Interpretive verdict:** we have a clean proof of **one protocol class's finite source-dependent epistemic horizon**. We have NOT proved no mathematical derivation of a global proposition can exist, much less that RH is independent of any conventional axiom system.

## 3. A minimal-support graph and the physically missing joint witness

The maintainer describes proofs as an *inverted dual*, small relative to the model graph and exposing the relationships between previously separate questions. This has a precise **restricted** version.

Let \(P=\{p_a,p_b\}\). A subset \(S\subseteq P\) is *logically sufficient* for target T on source class X iff
\[
\big(\forall s,t\in X\big)\quad
\left[\forall p\in S,\ p(s)=p(t)\right]
\Rightarrow T(s)=T(t).
\]
This is exactly the statement that T factors through the joint observation map of S. Define the inclusion-minimal logical probe supports \(\mathrm{MinSupp}_X(T)\).

For unrestricted original parity,
\[
\boxed{\mathrm{MinSupp}_X(T)=\{\{p_a,p_b\}\}.}
\]
Neither a nor b alone can decide parity over all four sources, but together they can.

The destructive single-carrier protocol can, however, obtain at most **one** of these source-original readings coherently:
\[
\mathcal F_{\rm physically\ supported}
=\{\varnothing,\{p_a\},\{p_b\}\}.
\]
The logically minimal support \(\{p_a,p_b\}\) is **absent**. This exhibits the proposed gap between the smallest supporting proof/probe **graph** and a path through physically realizable carrier states.

**Not a literal graph duality theorem:** proof dependencies are more accurately represented by a directed hypergraph, since one conclusion may depend jointly on several premises. The minimal support depends on the target T, candidate source class X, allowed primitive probes and the basis language. It is not the universally shortest proof program or minimal encoding in bits.

## 4. A proof can rewire the graph—but its premise must itself be supported

A valid new theorem can change the available source basis. In the laboratory:

**Before any new source law:** X contains all four bit pairs and parity needs \(\{a,b\}\), unavailable jointly on one carrier.

**After independently proving \(a=0\) as a law of the source family:** we have \(T=a\oplus b=b\), so
\[
\mathrm{MinSupp}_{X\cap\{a=0\}}(T)=\{\{p_b\}\}.
\]
Measuring b first on the unchanged carrier is now sufficient. The dependency graph's two-input gate has been rewired into a one-input gate.

**After independently proving \(a=b\) as a universal source restriction:** we obtain T=0 without any empirical query:
\[
\mathrm{MinSupp}_{X\cap\{a=b\}}(T)=\{\varnothing\}.
\]

Thus a validated proof can both *eliminate* an infinite or finite family of subordinate questions and *redirect* surviving questions to new shorter experimental/inferential paths. Its effect is **proof-induced contraction of the question dependency graph**.

**Adversarial premise control:** “a=0” is NOT true on unrestricted X. If it is merely guessed, the one-probe inference fails on initial source (1,0), where the b-probe returns 0 but original parity is 1. Source-class reduction is only lawful when the premise has an independent certificate in the declared mathematical basis.

The actual cost of acquiring, storing and verifying the new theorem is not included in the minimal probe count. There is no claim that a proof's syntax is automatically the shortest possible encoding.

## 5. Positive controls crucify a universal no-proof story

Three changes outside the original single-carrier protocol eliminate its obstruction:

1. **Two independently re-prepared copies of the same source:** query a on one and b on the other, then combine the two original-source readings.
2. **A nondestructive/joint read-only probe:** sample both values from one unchanged carrier.
3. **Independently verified source law:** a=0 or a=b reduces the mathematical support required as above.

These are constructive witnesses that the toy **carrier horizon is protocol-relative**. Removing the single-copy assumption, changing admissible probe types or supplying a valid law may change the completion class from physically inaccessible to finite.

A separate **asymptotic horizon** is possible if infinitely many probe results remain meaningful yet no finite stage justifies a global certificate. That is NOT the same phenomenon as a destructive probe making a source-relative measurement ill-typed. The two cases should remain distinct in ObsSUCC.

## 6. Relation to RH: strict nonimplications and a meaningful missing theorem

RH is a fixed mathematical statement about the zeros of the completed Riemann zeta function. A correct deductive proof need not involve a literal destructive observation of a physical carrier. Therefore the above single-carrier no-go has **no deductive implication** that RH is false, unprovable, Gödel-independent or physically inaccessible.

The strongest defensible research conjecture is narrower:

> For a specified class \(\Pi\) of source-derived finite/Archimedean observational constructions, every attempt to produce a global positive Weil-form/prime-completion certificate leaves the jointly required support domain before a lawful, source-faithful and analytically completed witness can be formed.

To make this a theorem rather than a metaphor, specify and prove:

1. The **actual source-specific arithmetic carrier**, operators and precise domain for every required prime, Euler, Gamma/Archimedean and test-function observation;
2. A physically/mathematically justified **state-changing or partial semantic transition** caused by constructing the certificate, as opposed to a self-imposed proof technique;
3. The **specific positive form/certificate** that would imply RH, with a valid identification to the *full completed Weil form* and proper support/topology;
4. A universal quantifier over an explicitly stated, nontrivial class of all admissible proof-construction protocols and independent positive/negative controls (including matched non-Euler sources); and
5. A proof that no allowed transfer, separate witness or stable mathematical invariant can bridge the apparent support loss.

Without these steps, “the probe horizon arrives before proof” is an important **hypothesis about our investigative interface**, not a result about the logical status of RH.

In particular, the existence of finite zero evidence or a repeatedly unsuccessful proof route does not establish a formal no-go for all analytic or arithmetic proof strategies.

## 7. Falsification program and status

| Proposed implication | Exact control | Verdict |
| --- | --- | --- |
| Two original bits can be collected by destructive single-carrier probes in sequence | First reading makes the other original component unobservable | REFUTED for this declared model |
| Destruction of initial-source meaning implies no observation remains meaningful at all | Second reading is meaningful for modified carrier but not for original-source parity | REFUTED |
| One-carrier deterministic protocol always identifies original parity | Pair of opposite-parity initial states produces identical all-future transcripts for each first action | REFUTED / local mathematical no-go proved |
| Minimal logical probe support automatically has a physically realizable measurement path | Both bits logically needed; no single-copy history can certify both | REFUTED |
| Proof-induced source laws can reduce probe support only by re-encoding the original same question | a=0 changes support {a,b}→{b}; a=b changes support→empty | REFUTED for this exact finite example |
| An unsupported supposed source law is safe to use for pruning | Source (1,0) invalidates guessed a=0 shortcut | REFUTED |
| Carrier backaction implies universal logical unprovability | Two-source-copy, non-destructive and proven-law repair cases | REFUTED |
| The same obstruction proves RH unprovable or a source-specific arithmetic theorem | Requires actual arithmetic operators, valid Weil/Gamma bridge and quantification across protocols | UNVERIFIED |

**New claim ledger proposals:**
- **O102 PROVED LOCAL:** exact adaptive single-carrier source-parity nonidentifiability after first destructive probe.
- **O103 PROVED LOCAL:** an observation of a modified carrier can remain meaningful while no longer supporting an initial-source-dependent proof.
- **O104 PROVED LOCAL:** minimal logical probe support need not be jointly physically actualizable.
- **O105 PROVED LOCAL:** independently justified mathematical laws contract/rewire minimal source-probe dependency supports; minimal with respect to specified probe basis, not globally smallest proof.
- **O106 PROVED LOCAL / TESTED MODEL:** extra preparations, nondestructive instruments or independently established source axioms can resolve the finite obstruction.
- **O107 UNVERIFIED:** any universally necessary non-actualizable proof-coherence horizon for RH or for all physically embodied observers.
- **O108 UNVERIFIED:** general sheaf/duality or cohomological characterization of proof-support incompatibility (finite measurement contexts here are not yet a theorem of contextuality).

**Next decisive round:** formulate the category (or indexed presheaf) of source states, typed evidence and state-changing probe morphisms; define a stable proof-certificate transport/gluing condition; compute examples where jointly needed evidence is compatible in an abstract source model but cannot be jointly actualized along any physical causal path. Contrast measurement backaction from evidence insufficiency and from formal axiom independence. Only then assess whether an analog of that theorem survives in *source-derived* arithmetic/Archimedean systems.

**Bottom line:** There can be genuine mathematical knowledge before a probe-coherence horizon. A proof may reduce the model's query graph, but its minimal sufficient support may be unreachable by all paths through a given carrier. That is a rigorous **conditional local-observer obstruction**, not an RH impossibility theorem.
