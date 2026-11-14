# Causal derivative and relevance-generated proximity

**Date:** 2026-11-13  
**Status:** RESEARCH PROPOSAL / mathematical definitions plus a scoped classical chain-rule identity; no empirical validation or novel theorem claimed.  
**Origin:** Leah's proposal: *“Closer” should mean “relatively more relevant”*, with geometry emerging from operationally accessible causal coupling rather than an assumed background metric.

## 1. Steelman: make closeness an output, not an input

A carrier-relative observer should not first declare two states “far apart” in a geometric coordinate system and then append a mechanism explaining why they are locally inseparable. It should identify the interventions and readouts that couple them and **derive** a notion of proximity from those relations.

> **Working principle.** For a specified carrier, observation horizon, instrument class and calibration, *closer* means *more causally relevant to the target observable*.

This is a proposal for **operational proximity**, not an assertion that spatial proper distance, signal speed, entanglement, or all quantum phenomena reduce to one scalar.

## 2. Primitive: finite causal contrast; derivative when it exists

Declare (i) a source/carrier model \(\mathcal C\), (ii) admissible controlled interventions \(\operatorname{do}(u_x=a)\), (iii) observable \(O_y\), (iv) a fixed context \(c\) including all other controls and initial-state preparation, and (v) a horizon \(\tau\). Write

\[
m_{y\leftarrow x}(a;\tau,c)
=\mathbb E_{\mathcal C}[O_y(t+\tau)\mid \operatorname{do}(u_x=a),c].
\]

The primitive causal contrast is

\[
\Delta_{x\to y}^{\tau,c}(a,b)
=m_{y\leftarrow x}(a;\tau,c)-m_{y\leftarrow x}(b;\tau,c).
\]

If the real-valued response is differentiable at the declared baseline \(a_0\), the **causal derivative** is

\[
\boxed{D_{x\to y}^{\tau,c}(a_0)
=\left.\frac{d}{da}m_{y\leftarrow x}(a;\tau,c)\right|_{a=a_0}.}
\]

For vector inputs and outputs use the Fréchet derivative/Jacobian in specified normed spaces. The do-notation means an *identified intervention*, not conditioning on \(u_x=a\) in observational data. With no intervention access or causal identification, this object may be mathematical but not measurable by the observer. If differentiability fails, retain finite contrasts rather than inventing an infinitesimal response.

**Important correction:** operational relevance *suggests a causal derivative to look for*; it **does not logically guarantee** one exists. Example: \(m(a)=|a|\) has a well-defined finite contrast but no derivative at \(a=0\).

## 3. “Relatively relevant” requires calibrated units

For scalar perturbation/output scales \(s_x,s_y>0\), define the dimensionless differential relevance

\[
R_{T,c}(x\to y)
=\sup_{0\le\tau\le T}
w(\tau)\,\frac{s_x}{s_y}
\left|D_{x\to y}^{\tau,c}(a_0)\right|,
\qquad 0\le w(\tau)\le1.
\]

For vector spaces use \(\|S_y^{-1}D S_x\|\) with declared input/output normalization operators. These scales are part of the measurement contract, not hidden universal constants. Under \(u'_x=au_x\), \(O'_y=bO_y\) with corresponding transported scales \(s'_x=|a|s_x\), \(s'_y=|b|s_y\), the normalized scalar relevance is unchanged; *without* transported calibration, numerical “distance” changes with units.

A **relative closeness preorder** for target \(y\) is immediately available:

\[
x\succeq_{y,T,c} z
\quad\Longleftrightarrow\quad
R_{T,c}(x\to y)\ge R_{T,c}(z\to y).
\]

This need not be symmetric: \(x\to y\) can matter without \(y\to x\) mattering. A unique Euclidean geometry does not follow.

For a finite declared set of admissibly coupled nodes, one *optional* directed path geometry is to give every \(R(x\to y)>0\) an edge length

\[
\ell(x,y)=\log(1+1/R(x\to y))>0,
\]

assign \(+\infty\) when \(R=0\), and let \(d(x,y)\) be the infimum of directed path-length sums (\(d(x,x)=0\)). Concatenation gives a directed triangle inequality. It is not automatically a symmetric metric, a physical proper distance, or even a faithful representation of **net** causal response (different paths may cancel). The edge-to-length transform is an explicit **choice**, not a derived law.

## 4. Exact check: a causal derivative is a propagated sensitivity

In a differentiable discrete-time system

\[
z_{n+1}=F(z_n,u_n),\qquad O_y(n)=h_y(z_n),
\]

a perturbation to one component \(u_x(s)\) has, for \(t>s\), derivative

\[
D_{x\to y}(t,s)
=Dh_y(z_t)
\Bigl[\prod_{k=s+1}^{t-1}D_zF(z_k,u_k)\Bigr]
D_{u_x}F(z_s,u_s),
\]

where the product is ordered in propagation order (later Jacobians on the left; the empty product is the identity). This follows directly from the multivariable chain rule (**CLASSICAL / PROVED BY THE DISPLAYED DERIVATION**, conditional on differentiability and the specified intervention).

For a linear time-invariant carrier \(z_{n+1}=Az_n+Bu_n\), \(O_y=C_y z\), this reduces exactly to

\[
\boxed{D_{x\to y}(t,s)=C_y A^{t-s-1}B_x.}
\]

Thus the proposed derivative is not merely poetic: in ordinary dynamical models it is a standard impulse-response/sensitivity object, whose support and magnitude can generate operational adjacency. Deriving an *intrinsic* geometry from it is the new interpretive target; the existence of impulse responses is classical.

## 5. Crucible: countermodels that any reconstruction must survive

1. **Correlation without causal influence.** Let \(X=Z\) and \(Y=Z\) for one hidden common cause \(Z\). The observational correlation is perfect; intervening on \(X\) alone leaves \(Y\) unchanged. So correlation-defined proximity and intervention-defined proximity disagree. **Receipt:** structural equations above.
2. **Different paths can cancel.** Set \(z_1=x\), \(z_2=x\), \(y=z_1-z_2\). Each leg has nonzero local sensitivity, but the total \(D_{x\to y}=0\). A shortest-path metric computed from *magnitudes* invents an apparent influence that the net readout does not have. **Receipt:** \(dy/dx=1-1=0\).
3. **Strong quantum correlation is not signaling.** For a bipartite entangled state, local trace-preserving operations on one subsystem cannot by themselves change the other's reduced-state statistics. Entanglement can be operationally relevant to *joint* measurements while one-way causal derivative of the remote *marginal* vanishes. Joint-observable and marginal-signal geometries must remain distinct.
4. **Nonlinearity and context.** Thresholds can make \(D\) undefined; saturation can make \(D=0\) near one operating point despite large finite interventions; dynamics can make \(R\) strongly dependent on \(T,c\). Geometry may be multiscale and state-dependent.

**Verdict:** The proposal **SURVIVES as a disciplined operational research program**. The stronger assertion “relative relevance uniquely fixes physical spacetime geometry” is **UNVERIFIED**, and a direct equivalence of causal proximity with quantum entanglement is blocked by the no-signaling example. No RH, π-normality, gravity, or ER=EPR implication has been established.

## 6. Boundary is a causal relevance threshold

Given an observed subsystem \(\Omega\), define its **incoming operational boundary** at threshold \(\theta>0\) by

\[
\partial^{\mathrm{in}}_{\theta,T,c}\Omega
=\{y\notin\Omega:\sup_{x\in\Omega}R_{T,c}(y\to x)\ge\theta\}.
\]

This formalizes the intuition that a “boundary is near” when outside interventions cannot be neglected in local predictions. Unlike a geometric boundary, this set may be disconnected or nonlocal relative to a pre-existing embedding; its dependence on probes, timescale and target must be kept explicit. It does **not** establish “classical = remote boundary, quantum = local boundary”: ordinary classical circuits can be strongly boundary-sensitive too.

## 7. Next discriminating probe (UNVERIFIED)

Implement a small exactly solvable carrier and recover its \(D\)-matrix by two independent routes: (1) symbolic/automatic differentiation of its transition dynamics and (2) calibrated finite interventions with a convergence/error check. Require these controls:

- **Positive:** a coupled edge whose derivative is known nonzero.
- **Negative:** an independent node with zero response.
- **Confounder:** common-cause correlation with zero do-response.
- **Hostile mutation:** two-path cancellation, threshold discontinuity and unit-rescaling.
- **Holdout:** change context/horizon or remove a carrier edge; predict how the proximity ordering changes *before* computing it.

The demanding future test is whether the resulting operational adjacency recovers an independently declared locality structure under suitable finite-propagation assumptions, while not misclassifying nonsignaling entanglement as causal communication.

## SUCC integration and claim accounting

- **Definitions:** finite causal contrast, conditional causal derivative, calibrated relevance preorder, optional directed path geometry and threshold boundary are *proposed constructs*.
- **Classical mathematics:** sensitivity transport by the chain rule; directed shortest-path triangle inequality (given nonnegative lengths).
- **Conjectured / UNVERIFIED:** these constructs give a useful source-faithful geometry for general SUCC carriers or yield new results in number theory or physics.
- **Provenance / compatibility:** complements [carrier-relative target descent](../../../docs/CARRIER_RELATIVE_TARGETS.md), [boundary-port geometry and intervention identifiability](../../../docs/CLAIM_SUPPLEMENT_BOUNDARY_PORT_GEOMETRY.md), and [observation-pinned geometry nonuniqueness](../../../docs/CLAIM_SUPPLEMENT_OBSERVATION_PINNED_GEOMETRY.md); it does not replace their source/probe contracts, change the claim ledger, or promote their evidence levels.

**Author intuition:** Leah. **Formalization:** research note prepared in conversation. **Physical measurements / new experiment runs:** none. **Claim of academic novelty:** none.


## 8. Addendum — classical appearance as geometric/computational agreement (Leah, 2026-11-13)

### Author's hypothesis, kept distinct from a physics theorem

> A system *appears* classical when the geometric notion of closeness lines up with the computational form. If its data can be observed freely, and those observations can verify more of the system than they falsify, the system is acting classically **relative to the observer's model**. That model may itself emerge from deeper dynamics.

This is a proposed **model-relative classical appearance criterion**, not the assertion that a physical system *is fundamentally classical*, or that classicality can be established by counting confirmations. It says that at the chosen observer scale, **what looks near, what computes locally, and what can be reliably checked agree**. Apparent autonomy and local predictability may be emergent from a finer carrier.

### Formal reconstruction and explicit typing

Fix an observer toolkit \(\mathcal T\), carrier \(C\), context class \(\mathcal K\), observation horizon \(T\), a candidate effective model \(M\), and a test distribution \(\mathcal H\) of *previously withheld* experiments. Keep three independently specified objects:

1. **Geometric proximity** \(d_G(x,y)\): a declared distance/preorder available to the effective observer (possibly reconstructed from separate instruments; not automatically Euclidean distance).
2. **Computational proximity** \(d_C^M(x,y)\): shortest legal dependency/cost path through the *model's* computational graph, using its actual local transformations; \(+\infty\) if unreachable.
3. **Measured causal relevance** \(R_{T,c}^{C,\mathcal T}(x\to y)\): calibrated do-response from Section 3, estimated or certified from the carrier, **not fitted and evaluated on the same observations without holdouts**.

A possible **alignment criterion** on a specified finite set \(P\) of admissible comparisons is

\[
\begin{aligned}
d_G(x,y)<d_G(x,z)&\ \Longrightarrow\
R_{T,c}(x\to y)\ge R_{T,c}(x\to z)-\epsilon_R,\\
d_C^M(x,y)<d_C^M(x,z)&\ \Longrightarrow\
R_{T,c}(x\to y)\ge R_{T,c}(x\to z)-\epsilon_R .
\end{aligned}
\]

The conditions are *hypotheses to test*, not automatic facts: propagation delays, attenuation, interference and heterogeneous edge strengths can invalidate them even in classical systems. A weaker usable version is a calibrated low-violation fraction of the specified comparisons. If \(d_G\) itself was built entirely from the same \(R\), geometry–response agreement is partly definitional; independent measurements, transport/gauge controls and a second graph are needed for a substantive test.

**Free observability** cannot literally mean zero physical interaction or complete hidden-state access. Make it *low-disturbance access for a declared target*: an admissible observation instrument \(\mathcal I\) has outcome/readout but modifies subsequent target-observable distributions by at most \(\epsilon_{\rm obs}\) under a specified operational norm and horizon, relative to a no-observation control. An instrument can be informative yet not low-disturbance. State dependence, destructive probes, and inaccessible variables remain explicit. This is a testable *relative* requirement, not an unrestricted observer power.

**“Verify more than falsify” — clarified in Section 9.** The author's emphasis is *not* a vote-counting rule for evidence. Rather, a finite observer can repeatedly find that a model is useful, predictive and locally verifiable while lacking any instrument that distinguishes (i) an eventual finite counterexample from (ii) persistent shrinking defects that disappear only in the analytic limit. Both can remain observationally indistinguishable in the available geometric/probe frame even when their source-level computational futures differ. Independent held-out agreement still matters, and one decisive counterexample still refutes a universal claim, but the primary proposed mechanism is **a mismatch between observable geometric locality and source-level computational causality**, not a preponderance of positive tests.

Thus a possible **operational diagnostic**, not a definition of classical physics, is:

\[
\boxed{\operatorname{ClassicalAppearance}(M;\mathcal T,C,T,\mathcal H)
\ \text{is supported when alignment, low-disturbance access,
and held-out predictive adequacy all pass declared thresholds.}}
\]

No scalar “classicality” is asserted. Keep the three diagnostics separate so a strong fit cannot conceal a probe-access gap or a geometric mismatch.

### Crucible: the hypothesis must survive these adversaries

- **Classical chaos:** a deterministic classical system may have excellent local equations and ordinary geometry, yet finite-resolution observations cannot reliably predict distant trajectories. Failure of long-horizon verification does not make the underlying dynamics non-classical. The horizon is essential.
- **Quantum nondemolition / commuting observables:** a quantum system can permit repeated low-disturbance measurement of a selected commuting observable algebra and yield an excellent effective classical model. Passing the diagnostic may certify an effective description, not underlying classical ontology.
- **Spurious verification:** a fitted computational graph and constructed geometry can agree perfectly with the very data used to build them; a held-out source intervention may refute both. Keep source map \(\sigma\), observation closure, and predictive adequacy independent.
- **Classical nonlocal-looking computation:** a classical network can have shortcuts or hidden wires, making geometric proximity and dependency-graph locality disagree. The system remains classical; it is the proposed effective geometry/model pairing that fails.
- **Coarse graining:** two distinct microscopic systems (one classically stochastic, one with quantum coherence invisible to the chosen toolkit) can have the same permitted observable transcripts. The diagnostic may classify both as classically appearing **relative to those observations**, without settling a fundamental distinction.

**Verdict:** **CONJECTURED / UNVERIFIED as a useful criterion of *classical appearance***. The unrestricted biconditional “a system is classical if and only if geometric and computational closeness align” is **not established**; the adversaries prohibit treating it as a universal necessary-and-sufficient definition. **Surviving insight:** classicality *as experienced by a finite observer* may be usefully studied as agreement between operational geometry, compositional computational prediction and nondestructive, independently checkable observations. Effective agreement is compatible with a deeper underlying theory.

### Next verdict-changing probe

Predeclare two models that are observationally equivalent on a training toolkit but disagree on an *unseen intervention*. Construct a small graph carrier with independently given coordinates, transitions and readouts. Train an effective \(M\) and \(d_C^M\) on one family; compute \(R\) from held-out interventions using independent finite contrasts. Compare (i) aligned local edges, (ii) a hidden shortcut, (iii) a canceling two-path mechanism, and (iv) a destructive probe. Record geometry–computation alignment, observation disturbance and prediction failures **separately**. The hypothesis earns empirical support only if it predicts *which* effective descriptions remain stable when the toolkit or scale changes—not merely which descriptions fit their construction data.

**Scope firewall:** This note asserts no physical collapse mechanism, no equivalence of correlation and signaling, no unique spacetime geometry, and no deduction of RH, π normality, or a Yang–Mills mass gap.


## 9. Addendum — delayed finite falsification versus limit-only defect; the unseen causal horizon (Leah, 2026-11-13)

### The sharpened author's hypothesis (not a majority-vote test)

> A finite observer can inhabit a model that seems true until a finite, constructible but prohibitively difficult counterexample arrives; or one that continually compensates for finer and finer defects, attaining exact agreement only in an analytic limit. The observer cannot tell the regimes apart by the available observations when the **computational structure of causal dependence is misaligned with the geometry of observation**. The causal event is like a quasar outside the available observational horizon: it matters before the observer has evidence that it matters.

Here "**seems true**" means *consistent with the declared finite evidence and useful as an effective model*, not a logical universal truth that later becomes false. "**Analytic place**" means a limit or completion with its own quantifiers and possible continuous extension, *not* an event that happens at a final finite step.

**Two rival regimes (not asserted exhaustive):**

- **Finite-surprise/hidden-witness regime:** there exists a finite source index \(N\) and a valid counterexample \(w_N\) whose construction or detection lies beyond the present observer's resource, intervention or geometric horizon. The first decisive failure is finite, although perhaps astronomically late.
- **Limit-only/asymptotic-defect regime:** a signed or unsigned correction \(e_n\) remains nonzero at every finite resolution \(n\) yet converges to zero: \(e_n\ne0\) for all finite \(n\), \(\lim_{n\to\infty}e_n=0\). The *limit object* may have an exact identity that no finite truncation realizes.

The second regime need not represent failure of the analytic theorem: a nonzero finite residual and an exact limiting equality are logically compatible. The first regime really refutes whichever universal statement the witness violates. Mere finite usefulness does not distinguish them.

### A small exact indistinguishability certificate (CLASSICAL, finite-access scope)

For any fixed finite observation horizon \(H\in\mathbb N\), consider the computable sequences

\[
a(n)=\frac{1}{n+1}\quad(n\ge0),\qquad
b_H(n)=
\begin{cases}
\frac{1}{n+1},&0\le n\le H,\\
1,&n>H.
\end{cases}
\]

These are **exactly identical for all finite observations at indices \(0,\ldots,H\)**, even with infinite numerical precision at those indices. Yet:

\[
a(n)>0\ \forall n<\infty,\qquad \lim_{n\to\infty}a(n)=0;
\]

while \(b_H\) **first breaks** the candidate finite law \(e(n)=1/(n+1)\) at the constructible finite witness \(n=H+1\) and has \(\lim b_H(n)=1\).

**Proof/receipt:** equality through \(H\) follows by substitution; at \(H+1\), \(1\ne1/(H+2)\); both limits follow immediately from their formulas. Both formulas are elementary computable objects. If a deterministic finite protocol reads an arbitrary finite list of indices rather than a prefix, choose \(H\) larger than its greatest queried index, and it receives the same entire transcript from both candidates. An adaptive protocol with finitely many terminating queries can be handled by running it on \(a\), then choosing \(H\) beyond its largest query. This proves **no uniformly guaranteed finite readout-only discriminator for this unrestricted pair family**, not the uncomputability of either sequence.

**What would defeat the ambiguity?** Access to the generating formulas, a source authentication constraint, a valid global proof of a uniform bound or convergence rate, or a probe allowed to reach an independently bounded witness can distinguish the particular cases. This is an **instrument- and model-class-relative** indistinguishability result, not a metaphysical assertion that nobody can ever know in advance. Finite computational accessibility and practical tractability must also be distinguished.

### The geometric–computational mismatch is the mechanism to test

Let \(G_{\mathrm{obs}}\) be the observer's effective geometry, equipped with an accessible region \(B^G_R(y)\) around a target readout \(y\). Let \(\operatorname{Anc}_C(y;\tau,c)\) be the **actual source-level causal ancestors** capable of influencing \(y\) within horizon \(\tau\) in context \(c\) (a structural dependence set, not necessarily the support of a derivative at one baseline). Define the unseen causal set

\[
\boxed{
U_{R,\tau,c}(y)
=\operatorname{Anc}_C(y;\tau,c)\setminus B^G_R(y).
}
\]

Here the notions of "within \(\tau\)" and "within \(R\)" must be declared and calibrated separately; the formula uses a common typed node map into the geometric chart. If that map is unavailable, the set is itself **undefined** and the lack of a bridge is the access gap. \(U\ne\varnothing\) says the observer's spatially nearby/probe-accessible region omits a computationally relevant cause. An ancestor can remain inactive for the observed context, only manifest at a later horizon, or be hidden below sensitivity.

For differentiable comparable carrier/model readouts with a common calibrated chart, propose the **causal derivative of the model defect**

\[
\boxed{
D^{\mathrm{defect}}_{x\to y}(\tau,c)
=D^C_{x\to y}(\tau,c)-D^M_{x\to y}(\tau,c).
}
\]

When accessible, a nonzero response difference is a potential *early discriminator* even if the unperturbed trajectories agree. When the source cannot be perturbed/read at \(x\), or the defect activates only outside the current horizon or operating context, it is **UNVERIFIED**, not zero. Nondifferentiable gates require finite causal contrasts instead.

This is the proposed "unseen quasar": **the observer's effective causal light cone and the true source dependency cone fail to coincide under the available projection**. The metaphor does not imply superluminal signaling or literal quantum measurement collapse; it describes limits of model locality, access, detection latency and possible hidden dependencies.

### Why the earlier "confirmation versus refutation" safeguard was insufficient

The fact that *one exact counterexample defeats a universal theorem* is correct, but was not the point at issue. The stronger concern is that many successful finite tests may leave **both** a latent finite-witness model and a genuine asymptotic-limit model alive in the same observational equivalence class. A rare falsifying witness is one route out; a justified source theorem or new counterfactual intervention is another. No quantity of repeated tests *inside the same blind horizon* necessarily discriminates them.

This also explains why merely increasing microscope resolution or taking more samples in the same chart need not repair the obstruction. The missing probe may require a different source map, a new intervention channel, a longer clock, a hostile counterseed, or an analytic bound that closes the tail.

### Steelman–crucible–verdict

- **DISLOSED / mathematical scope:** the finite indistinguishability pair above has a short exact proof. It certifies a no-uniform-discriminator result only for finite readout access without stronger promises. The limit example is standard analysis.
- **CONJECTURED:** experimentally meaningful classical appearance can be modeled as **operational stability of the alignment between geometric observation and source-level computational causality**, rather than as an intrinsic classical/quantum label.
- **UNVERIFIED:** the geometry–causality mismatch is the actual mechanism behind any specific unexplained physical phenomenon or arithmetic obstruction; no carrier-grounded intervention experiment was performed.
- **Counterweight:** some classically deterministic systems have unseen ancestors, and some quantum systems permit stable effective classical observations. Thus the mismatch is **not** a definition of fundamental quantum/classical ontology, nor is it a sufficient proof that the source is nonclassical.
- **Next verdict-changing probe:** hold an observer's geometric chart \(G_{\rm obs}\) and finite record fixed; construct two source-faithful candidate carriers matching all observed readouts but differing between a delayed finite gate and a shrinking analytic defect. Specify an out-of-chart intervention \(u_x\), predict \(D^{\rm defect}_{x\to y}\) or a finite contrast *before* probing, and test whether the intervention separates them. Include a negative control (no link), a positive control (known link), a mutation (hidden shortcut), and a holdout (later time/changed context). If no feasible intervention separates them, report a **probe gap** rather than interpreting matched observations as a proof of either regime.

**Connection to SUCC frontiers:** this framing highlights the difference between finitely computable counterexample search and a source-specific uniform analytic cancellation theorem. It does *not* establish either a counterexample or the missing \(\pi\)-normality estimate. Exact analytic completion cannot be inferred from arbitrarily persuasive finite prefixes without a valid tail theorem.
