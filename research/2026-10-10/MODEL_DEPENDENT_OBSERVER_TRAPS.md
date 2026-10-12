# Observer traps under model-dependent probe access

**Date:** 2026-10-10/11  
**Scope:** exact, finite, deterministic causal observation with instantaneous sound incorporation of selected outcomes. **Status:** PROVED LOCAL (elementary lemmas), TESTED MODEL (finite implementation and exhaustive controls), HYPOTHESIS (extension to physical/cognitive observers). RH and Gödel independence are **UNVERIFIED**.

**Author's initiating idea:** the local frame is the observer's current model plus every probe it can perform *given* that model. SUCC changes the model via all available observations; changes in the model alter the accessible probes. Even a perfect, instantaneous local reasoner may be trapped by feedback between model and probe access. This document formalizes the strongest defensible finite reading without claiming the physical theory has already been proved.

**Implementation:** observational_succ/observer_traps.py  
**Tests:** tests/test_observer_traps.py  
**Standalone probe:** scripts/observer_trap_probe.py

## 1. Types and observational dynamics

Fix a finite nonempty source set \(X\), a finite nonempty global probe set \(P\), and a **total deterministic source response** \(r_p:X\to Y_p\) for each \(p\in P\). Fix an unknown actual source \(x_*\in X\).

An observed history is a finite immutable ordered sequence \(H_n=((p_i,r_{p_i}(x_*)))_{i\in I_n}\). Every event must be an output of the declared source. The full **version space** is

\[
K_n=\{x\in X: r_{p_i}(x)=r_{p_i}(x_*)\ \text{for every actualized event }i\}.
\]

The **preferred semantic model** \(m_n\in K_n\) is deliberately kept distinct from a certificate that \(K_n\) is a singleton. The semantic policy retains \(m_n\) whenever compatible; when refuted, it selects the first surviving member by a fixed declared order (the tie-breaking prior). Neither the preferred model nor the tie-break is a truth oracle.

Define a model-dependent access map \(A:X\to 2^P\setminus\{\emptyset\}\). At each frame the default observer simultaneously evaluates **all** probes in \(A(m_n)\), with zero assimilation time, then forms \(K_{n+1}\) and \(m_{n+1}\). Two deliberately weaker scheduling controls select only the first local probe repeatedly or choose probes cyclically.

The program also distinguishes an **uncertainty-aware** access policy

\[
A_\cup(K_n)=\bigcup_{y\in K_n}A(y),
\]

with the explicit additional premise that every probe in this union really can be executed. The union is NOT silently assumed to be a physically available action.

Every step is causally recorded as either an ordinary policy-selected event or an externally imposed probe. Replay checks both the event outcome and its claimed selection origin relative to the declared world and policy. A recorded external experiment is not rewritten as something the endogenous policy discovered.

### Source-faithfulness invariant

At all finite frames, \(x_*\in K_{n+1}\subseteq K_n\).

**Proof:** true outcomes cannot exclude the true source. Each newly actualized constraint intersects the preceding version space; no earlier source event is removed. This is independent of preferred-model quality.

**Boundary:** exact replay validates a supplied finite toy world under an externally supplied source label; it is not cryptographic authentication or an empirical test that any human brain uses the given model.

## 2. Observer-trap theorem (exact stationary-policy iff)

Fix a frame with \(x_*,m\in K_n\), \(m\ne x_*\), and let the policy use only \(A(m)\) while \(m\) remains preferred. Let \(S(m)\subseteq A(m)\) be the probes that would **eventually be selected** on that stationary preferred-model path:

- exhaustive local observation: \(S(m)=A(m)\);
- cyclic finite scheduling: \(S(m)=A(m)\);
- permanently selecting the first probe: \(S(m)=\{\operatorname{first}(A(m))\}\).

Then

\[
\boxed{\ m \text{ survives every later SUCC frame }\iff
\forall p\in S(m),\ r_p(m)=r_p(x_*)\ .\ }
\]

**Proof, forward direction:** if some \(q\in S(m)\) distinguishes \(x_*\) and \(m\), then cyclic/exhaustive scheduling selects it at a finite successor stage *unless \(m\) was already eliminated*, in which case the proposition also fails. The genuine outcome excludes \(m\).

**Proof, backward direction:** if every eventually selected probe gives identical outputs for \(m\) and \(x_*\), the preferred model is never refuted at the next frame. The policy therefore continues to select from the same stationary menu; induction proves survival at every finite successor. Under the ideal \(\omega\) record it is also retained, because every recorded equation remains true of \(m\).

**Exact residual fiber when trapped:**

\[
K_\omega=
K_n\cap\bigcap_{p\in S(m)}\{y\in X:r_p(y)=r_p(x_*)\}.
\]

The finite support guarantees that this fiber is actually reached after a finite cycle of its selected probes, even though the observer may keep taking further frames. **Stasis of the preferred model is not source identification**. Its compatibility set still has at least \(x_*,m\).

The theorem's iff depends on finite deterministic probes and on a stationary menu so long as the preferred model survives. Arbitrary noisy, changing, nondeterministic or physically inaccessible probes need new hypotheses.

## 3. Three different causes of indefinite nonidentification

For a false preferred model \(m\), let \(D(x_*,m)=\{p\in P:r_p(x_*)\ne r_p(m)\}\).

| Classification | Exact condition | What would distinguish the rival? |
| --- | --- | --- |
| **Global-probe blind** | \(D=\emptyset\) | A new source-sensitive probe outside declared \(P\), or a justified source-class restriction |
| **Access trap** | \(D\ne\emptyset,\ D\cap A(m)=\emptyset\) | Change the model-dependent *access map*, using a genuinely executable counterfactual probe |
| **Scheduling trap** | \(D\cap A(m)\ne\emptyset,\ D\cap S(m)=\emptyset\) | Fairly schedule an already-accessible discriminator |
| **Eventually discriminating** | \(D\cap S(m)\ne\emptyset\) | No structural barrier: the preferred model is refuted in finitely many frames under the declared schedule |

The four diagnoses are mutually exclusive for an incorrect preferred model under the stated finite policy. **An internal observer cannot generally compute which one is true without knowing \(x_*\)**; the finite exact certificate is generated by an *external laboratory that is given the source*.

This is a sharp distinction among a model/source-map gap, an access/pathway gap, a probe-scheduling gap, and ordinary finite latency.

## 4. Stronger indistinguishability and no-uniform-certifier result

**History equivalence lemma:** Fix the same deterministic initial semantic state and policy in two different source worlds \(x,y\). If every probe chosen along the history in world \(x\) returns the same result in world \(y\), then the selected probes, histories, version spaces, preferred models and all deterministic semantic reports are identical in both worlds, at every finite stage and for any history-derived ideal \(\omega\) report.

**Proof:** induction. Identical histories produce identical next menus, schedules and preferred-model updates. Equal responses produce identical extended histories.

**No-go corollary:** If a target \(T\) satisfies \(T(x)\ne T(y)\), no deterministic report computed **only** from these identical histories can simultaneously be correct on both sources. In particular, a model's apparent self-consistency does not certify that it is the actual source.

This is an information-theoretic obstruction relative to the chosen interface, **not** a theorem that the underlying mathematical distinction is unknowable by all possible methods.

### Categorical reading: observational kernel pairs, not yet Yoneda full faithfulness

For a fixed finite probe family \(S\subseteq P\), define the joint response map

\[
E_S:X\longrightarrow \prod_{p\in S}Y_p,\qquad
E_S(x)=(r_p(x))_{p\in S}.
\]

Its **kernel pair** is the observational equivalence relation
\(x\sim_S y\iff E_S(x)=E_S(y)\). If \(S\subseteq S'\), then
\(\sim_{S'}\subseteq\sim_S\): adding source-faithful probes can refine
observational equivalence but cannot merge previously separated sources.
A source-relative access trap occurs when the current policy selects a
family \(S\) with a nontrivial kernel pair on the actual and preferred
sources, even though the declared global map \(E_P\) separates them.

This is a **set-level** statement of joint source separation. It does
**not** establish full faithfulness of a categorical Yoneda embedding:
fullness/faithfulness of a functor refers to morphisms, whereas injectivity
of the displayed response map concerns source objects. A genuine
categorical generalization must explicitly specify source morphisms,
probe presheaves, natural transformations and compatible access-change
maps. This is a precise next research obligation rather than a diagram
accepted because it resembles Yoneda.

The other failure mode in the earlier ideal-frame note—the formal
factorial Taylor jet with no analytic realization—is *not* a nontrivial
kernel pair. There the inverse-limit observation data have **no
preimage** in the declared analytic source class. Thus feedback blindness
(noninjectivity under selected probes) and omega nonrealizability
(failure of surjectivity onto the reported formal data) must stay separate.

## 5. Closed-loop counterexamples and repairs

### Access trap under maximally exhaustive local assimilation

Use \(X=\{A,B\}\), \(P=\{\text{echo},\text{separator}\}\).

| Probe | Response on A | Response on B |
| --- | --- | --- |
| echo | same | same |
| separator | A | B |

Let the actual source be B, the initial preferred model A, and the menus \(A(A)=\{\text{echo}\}\), \(A(B)=\{\text{echo},\text{separator}\}\).

The observer measures **every** locally available probe on every frame, but echo never refutes A. Its model stays A and its compatible version space stays \(\{A,B\}\) forever. Global separator exists and is decisive. Two different true sources, A and B, generate the *same entire endogenous trace* under this policy.

An explicitly exogenous separator observation produces the truthful label B, eliminates A, and is recorded as external rather than pretended local discovery.

### Scheduling trap

Change A's access menu to contain both probes, but schedule only its first element, echo, every frame. The same false model persists. A two-probe cyclic schedule selects separator at the **second** SUCC and eliminates A. This is a scheduler defect, not intrinsic inaccessibility.

### Dynamic trap *after* valid correction

Take \(X=\{A,B,C\}\), with probes broad and fine:

| Source | broad | fine |
| --- | --- | --- |
| A | 0 | 0 |
| B | 1 | 0 |
| C | 1 | 1 |

Actual source C; initial favorite A. A's menu contains broad, which correctly refutes A, leaving \(\{B,C\}\). The observer legitimately revises its favorite to B. But B's menu again contains only broad, which cannot distinguish B from C. **The observer completed a rational update and then entered a fresh false-model fixed point.**

Thus "rational revisions occur" is not a sufficient anti-trap property. A single history can contain genuine progress and subsequent permanent blindness.

### Compatible-class union repair (with explicit feasibility premise)

Define \(U(K)=\bigcup_{y\in K}A(y)\), and evaluate every probe in \(U(K)\) at one successor.

**One-step identification theorem:** For finite \(K\), this produces \(K'=\{x_*\}\) for **every** possible source \(x_*\in K\) iff \(U(K)\) separates every distinct pair of candidates in \(K\):

\[
\forall x\ne y\in K\quad\exists p\in U(K):r_p(x)\ne r_p(y).
\]

**Proof:** if all source pairs are separated by the common probe menu, every false candidate disagrees with the genuine source on at least one observed output. Conversely, an unseparated pair both remain if either is actual. This is a direct finite separation theorem, not an asymptotic heuristic.

The stronger pairwise condition \(\forall x\ne y,\exists p\in A(x)\cup A(y)\) separating \(x,y\) **suffices**, but is not necessary: a third candidate's menu can contain a probe that separates the first two. The test suite includes this non-necessity control.

**Critical caveat:** unioning model-generated probe menus may not be physically executable. If probe access depends on the *actual* substrate rather than merely on which experiments the observer can conceive, the policy needs a separate physical feasibility predicate and may fail its assumptions.

## 6. Finite worlds cannot be genuinely omega-only identifiable

**Finite-stabilization lemma:** If \(X\) is finite and the version spaces \(K_0\supseteq K_1\supseteq\cdots\) contain only source-faithful observations, then

\[
K_\omega=\bigcap_{n<\omega}K_n=K_N
\]

for some finite \(N\) (even if \(K_N\) is not a singleton).

**Proof:** for each candidate \(y\in K_0\setminus K_\omega\), choose a finite stage \(n_y\) at which it was eliminated. There are finitely many such candidates, so \(N=\max_y n_y\) is finite (or take \(N=0\) if none are eliminated). After \(N\) no additional exclusions can occur.

Consequently, **a finite candidate class cannot be omega-only identifiable with respect to an exact deterministic target**: if it is identified at omega, it was already identified at some finite stage. This does **not** imply a known, effectively computable stopping bound or a sound internal certificate that the stage has finished.

More generally, each preferred-model change permanently eliminates at least one former candidate, so there are at most \(|X|-1\) semantic preference changes under the compatible-retention rule. A final *false* favorite may then be stationary forever even though the observer continues to collect observations.

**Infinite class contrast:** take candidates \(\{\infty\}\cup\{0,1,2,\ldots\}\) and probes \(p_n\) with \(p_n(\infty)=0\) and \(p_n(k)=1\) iff \(k=n\). When \(\infty\) is actual and SUCC unlocks \(p_0,p_1,\ldots\), every finite history leaves infinitely many candidates, but the ideal omega record identifies \(\infty\). This is a rigorous omega-only example independent of analyticity, and no infinite physical computation is implied.

## 7. Controls, reproducibility, and claim status

**Predicted contrasts before test execution:**

| Experiment | Expected result |
| --- | --- |
| Two-source world, exhaustive model-relative probes | False favorite persists with two compatible sources |
| Same world, exogenous true separator | False model refuted, source identified; external provenance retained |
| Same world, compatible-union probes | Truth identified if union probes executable |
| Same menu, always first probe versus cyclic scheduler | Scheduling trap versus finite refutation at SUCC 2 |
| Globally equal probe responses | Genuine indistinguishability under declared P |
| Three-source feedback | Initial false model refuted, next false model becomes stationary |
| Two distinct truths with same policy history | All endogenous histories and semantic reports identical |
| Forge an outcome, policy source or semantic state | Replay rejects |
| Exhaustively mutate all binary two-source/two-probe tables | Stationary-pair certificate matches actual finite trajectories |
| Exhaustively mutate three-source/two-probe binary tables | Pairwise menu-cover sufficient condition never falsely certifies failure |
| Pairwise menu-cover negative control | Strong pairwise condition not necessary for union-probe completion |

The Python tests enumerate **864** two-source comparisons and **5,184** three-source/union initial conditions, besides named tests. The computations are *finite model checks*: the all-orders theorems are proven algebraically by induction and finite support, not by simulating infinitely many frames.

~~~sh
python -m unittest tests.test_observer_traps -v
python scripts/observer_trap_probe.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/verify_provenance.py
~~~

**Ledger targets:** O47–O54. The named exact lemmas are PROVED LOCAL under finite deterministic assumptions, their implementations TESTED MODEL, the postulated human/physical observer dynamics HYPOTHESIS, and quantum/noisy/infinitary/RH extrapolation UNVERIFIED.

## 8. Existing literature: what is and is not novel

This feedback pattern connects to the economics of **self-confirming equilibrium**: on-path observations can perpetually agree with false beliefs about unvisited situations. Reference: Drew Fudenberg & David Levine, *Self-Confirming Equilibrium*, Econometrica **61** (1993), 523–545, https://ideas.repec.org/a/ecm/emetrp/v61y1993i3p523-45.html.

In adaptive control and system identification, sufficient input excitation can determine whether a feedback loop identifies unknown parameters. A relevant primary source is L. Gerencsér, *Closed loop parameter identifiability and adaptive control of a linear stochastic system*, Systems & Control Letters **15** (1990), 411–416, https://doi.org/10.1016/0167-6911(90)90065-3.

Our exact finite observer formalism, access/scheduling distinction and source-faithful counterexample suite are **new-to-repository research synthesis**, not a claim of academic priority over these literatures. The mathematical results here are elementary finite facts.

## 9. Open questions that could change the verdict

1. **Physical versus epistemic accessibility:** Is \(A(m)\) a set of probes an observer *knows how to perform*, or probes the actual physical carrier *permits*? Can a union-of-compatible-menus observer legally instantiate them, or does it violate causal feasibility?
2. **What is the right semantic closure?** When observations tie between \(A\) and \(B\), must "most sane" mean a stable favored model, an entire version space, a distribution over models, or a categorical object containing all compatible interpretations?
3. **Can access evolve without falsification?** In the spherical-cow idealization, is the observer permitted to invent new probes through logical closure alone, even if every observed result agrees with its model? What axioms generate these new experiments?
4. **Which fairness rule is physically justified?** Can repeated observation eventually explore every *physically* admissible discriminator? What are the unavoidable resource and risk constraints?
5. **Target-relative completion:** Is the goal full source identification, a particular invariant \(T(x)\), a theorem, or a safe action? An observer might never identify the entire field yet decide the desired invariant correctly.
6. **What survives noise or quantum backaction?** In stochastic or noncommuting measurement settings, which distinguishability and repeated-measurement conditions yield identification almost surely, and which access traps survive?
7. **Can we obtain effective completion moduli?** Even when a mathematical omega limit identifies a source, can the observer compute how much accuracy finite SUCC frames guarantee from accessible data alone?
8. **How should categorical semantics encode the feedback?** Define a typed observation functor with access-changing morphisms, and characterize precisely when a probe-family extension repairs its failure of faithfulness. Can those conditions be established from internal data rather than an external source oracle?
9. **RH application boundary:** Is there an explicitly defined source-sensitive test-function probe that the existing prime-only model misses but the completed Gamma/pole model gains? This requires construction and rigorous intervals; it is not evidence for RH from finite trap models.
10. **Formal verification:** Can a small proof assistant establish the stationary-pair iff, finite stabilization, and compatible-union separation independent of the Python implementation? This is an appropriate first mechanization target.

**Next falsifier:** Introduce *truth-conditioned physical feasibility* and a fully endogenous mechanism that can expand the probe family without oracle assistance. Demonstrate both a trap that remains after epistemic-union exploration and a trap that escapes under lawful active experimentation. Preserve every causal event and every failed candidate.
