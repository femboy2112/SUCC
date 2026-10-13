# Covariant Meta-SUCC: perceptual frame momentum, causal receipt nets and claim-preserving descent

**2026-10-12 | draft research checkpoint | source:** `femboy2112/SUCC`, stacked on Meta-SUCC PR #36 at `3751caee7a1e2eb12ffa38dba2181a80ba701ea6`. **Status:** classical Lorentz geometry, deterministic automata theory, finite-set categorical Beck--Chevalley and partial-order distributed information, with exact Fraction verifiers and positive/negative source models. **No research-priority claim, physical cognitive Lorentz law, empirical carrier attestation, actual quantum experiment, source-free RH statement or proof of Weil positivity.**

## 0. The user's interpretive proposal, steelmanned

Many E towers discover evidence and concepts at different depths. To a branch with substantial acquired context and a different causal history, its mathematical field is naturally organized differently than it appears to the original E at the base. The user proposes a *perceptual momentum*, analogous to relative motion in relativity: coordinate descriptions can tilt or rotate and the observer may report different simultaneity, yet genuine source truths should be covariantly transportable. The challenge is to allow **noncommuting transformations and physical carrier backaction**, not to demand that all different frame arrows literally commute.

We need three separately typed layers:

1. **Physical spacetime:** a Lorentzian carrier and causal event poset. An actual Lorentz boost is a coordinate transformation of spacetime, not an epistemic update. It cannot reverse causal ancestry or support faster-than-light evidence delivery.
2. **Epistemic frame:** the observer's source-relative coordinates, available probes, basis and full causal evidence ledger. A semantic frame change may be noncommuting and lack any literal physical velocity.
3. **Proof-support fiber:** a carrier-relative claim, its source-domain/meaning, admissible observation laws, trusted causal receipts and proof. Only a verified square or claim-fiber condition licenses its transport.

A useful operational proxy for the metaphor is the pair `(local horizon tilt, information/receipt lag)`, together with a rate per declared proper-time or observer-clock parameter. It is not established physical momentum; no unproved relationship to cognition or mass is assumed.

## CV1. Rational Lorentz frames and causal-order covariance (CLASSICAL / EXACT)

Take \(\mathbb Q^{1+2}\subset\mathbb R^{1+2}\) with Minkowski metric \(\eta=\mathrm{diag}(1,-1,-1)\), setting \(c=1\). For an exact rational boost \(L\in SO^+(1,2;\mathbb Q)\), \(L^T\eta L=\eta\), \(\det L=1\), and \(L_{00}\ge1\). Thus
\[
  \langle Lz-Lw,Lz-Lw\rangle_\eta=\langle z-w,z-w\rangle_\eta.
\]
A future causal vector is still future causal, because the proper orthochronous Lorentz group preserves the connected future light cone. This verifies **all causal dependency arrows** in any finite observation ledger after an honest frame change; it does not make a made-up arrow causal.

The exact boost at rapidity-half parameter \(r=1/3\) in the x direction is
\[
 B_x=\begin{pmatrix}5/4&-3/4&0\\-3/4&5/4&0\\0&0&1\end{pmatrix},
\quad v=3/5.
\]
E assigns the events \(a=(0,-1,0),b=(0,1,0)\) equal coordinate time. The moving frame assigns \(t'_a=3/4,t'_b=-3/4\). Their chronological order can reverse, but both are spacelike relative to E's origin event \(o=(0,0,0)\). Neither is in the causal past of \(o\). Actual physical delivery to E at the origin requires coordinate time at least 1. Arbitrary E *knowledge snapshots* must use actual causal ancestry, **not the entire coordinate time slice**.

## CV2. Frame-slice disagreement theorem (CLASSICAL / PROVED LOCAL)

Fix an anchor event \(o\) and two proper orthochronous inertial frames \(F,G\). Let \(D_F(o)=\{e:t_F(e)\le t_F(o)\}\), and similarly for \(G\). Then
\[
\boxed{D_F(o)\triangle D_G(o)\subseteq\{e:(e-o)^2_\eta<0\}.}\tag{CV2}
\]
**Proof.** Future or past causal events have the same signed temporal relation to \(o\) in every proper orthochronous frame. Therefore any event whose inclusion in the two coordinate cuts differs must be causally incomparable (spacelike) to \(o\). This holds for all events; it is not an assertion about which events have actually delivered their messages. The proof has exact finite Fraction examples and forged causal-parent tests.

## CV3. A genuine Wigner-rotation control: noncommuting physical frames (CLASSICAL / EXACT)

Let \(B_x,B_y\) be the same rational boosts along perpendicular axes. They DO NOT commute. In the indicated order, the product has a polar-like decomposition
\[
 B_yB_x=B_{\mathrm{net}}R,\qquad
 \boxed{R=\begin{pmatrix}1&0&0\\0&40/41&-9/41\\0&9/41&40/41\end{pmatrix}.}\tag{CV3}
\]
\(R\) is a nontrivial proper spatial rotation. The exact net boost velocity is \((12/25,3/5)\), with \(\gamma=25/16\). **Proof:** compute the product, determine the unique pure boost with the product's first column, and set \(R=B_{\mathrm{net}}^{-1}B_yB_x\). Its displayed entries are rational and verify \(R_{00}=1,R_{0i}=R_{i0}=0,R_{\mathrm{space}}^TR_{\mathrm{space}}=I,\det R=1\). Distinct orders give distinct frame paths; all preserve \(\eta\). Collinear 1+1 boosts commute, so this example deliberately uses two spatial dimensions.

**Perceptual analogy, not physical identification:** even after the source spacetime itself has been faithfully transported, its two-dimensional spatial axes may acquire a path-dependent rotation. SUCC's epistemic basis transports can have analogous noncommuting holonomy; they need not be Lorentzian or physical.

## CV4. Original-source claim transport (CLASSICAL FINITE FIBER THEOREM)

Let \(U:C\to C'\) be a lawful (possibly destructive) carrier action, \(O:C\to Y\), \(O':C'\to Y'\) two observation maps, and \(R:Y\to Y'\) a proposed report transport. Observation covariance is the **independent premise**
\[
\boxed{O'U=RO.}\tag{CV4a}
\]
For an original-source target \(t:C\to T\), a decoder from the post-action observation exists exactly if
\[
\boxed{\ker(O'U)\subseteq\ker t}\tag{CV4b}
\]
where kernels denote equivalence relations on the domain. **Proof:** if a decoder exists, equal reports imply equal target. Conversely define \(d(O'U(x))=t(x)\); kernel containment makes it single-valued. A required claim meaning after the action \(t':C'\to T\) additionally needs \(t=t'U\), but this condition is independent of observation covariance. If \(U\) is invertible and \(R\) invertible on the observed image, transport an old decoder \(d\) by \(d'=dR^{-1}\). A destructive map can make (CV4a) commute while violating (CV4b); no frame analogy repairs an actually erased original bit. Prior authentic *immutable receipts* may still preserve an original-source claim, but the poststate alone does not.

The checker supplies a constructive decoder or two original sources with identical post-action reports but different target values, plus independent yes/no observation- and claim-square audits.

## CV5. Path-independent claims under noncommuting frame holonomy (CLASSICAL GROUP ACTION)

Let a group \(G\) of admissible reversible frame transformations act on source states \(C\), with a target \(t:C\to T\). Then
\[
\boxed{t\text{ is path-independent under all finite frame words}\iff t(g_i x)=t(x)\ \forall i,x,}\tag{CV5}
\]
where the \(g_i\) generate \(G\) and inverses are permitted. **Proof:** invariance under generators implies invariance under their inverses and then any finite word; the reverse follows trivially. This is equivalently constancy of \(t\) on all \(G\)-orbits: \(t\) factors through \(C/G\). A certified action of the two noncommuting \(GL(2,\mathbb F_2)\) shears has orbits \(\{0\},\{1,2,3\}\): the *zero-vs-nonzero* target survives every frame, while original parity fails, with explicit generator/source witness. **Nonzero holonomy does not invalidate every mathematical claim.**

If a program forgets the full intervention path, it must test the claim's stabilizer. For a path-dependent noninvariant claim, preserving the ordered path receipt is part of the proof support.

## CV6. Beck--Chevalley is not implied by a merely commuting square (CLASSICAL FINITE-SET THEOREM)

For maps \(f:X\to Z\), \(g:Y\to Z\), let \(W\subseteq X\times_ZY\) be an alleged set of source-compatible comparisons. With projections \(p:W\to X\), \(q:W\to Y\), the existential/base-change identity is
\[
\boxed{q_!p^*(S)=g^*f_!(S)\quad\forall S\subseteq X.}\tag{CV6}
\]
It holds **if and only if** \(W=X\times_ZY\). **Proof:** for the full pullback, membership on both sides says that some \(x\in S\) has \(f(x)=g(y)\). Conversely, if \((x,y)\) is a compatible pair omitted from \(W\), take \(S=\{x\}\); then \(y\) appears on the right but not the left. The counterexample is a commuting but INCOMPLETE relation over two elements; all four singleton/empty/full predicates are independently checked. This is the precise categorical warning: **a commuting carrier/observer diagram is not automatically a valid quantification or proof-transport square**.

## CV7. Causal E-tower evidence is a downset, not a simultaneity slice (CLASSICAL / EXACT FINITE MODEL)

Let \(\mathcal E\) be a finite poset of source-tagged physical events, with arrow \(e\prec f\) only if an actual causal influence was declared and the two spacetime positions permit it. A knowledge state at checkpoint \(c\) is the set of probe receipts in the actual causal downclosure \(\downarrow c\); source-fiber inference intersects their preimages. Its proof of \(t\) is legitimate exactly if \(t\) is constant on the nonempty compatible-source fiber. The program never infers that a spacetime event was received merely because its coordinate time is earlier than \(c\).

**Exact example.** At \((0,-1)\), A reads the original first bit 1. At \((0,1)\), B reads the second bit 0. They are spacelike. E at \((1,0)\) has received only A's declared path and cannot yet determine original XOR; E at \((2,0)\) has recorded both lawful paths and determines XOR=1. This is an **epistemic** single macro-update at E after physical receipt, not a physically instantaneous or source-unauthenticated miracle. A forged superluminal parent arrow, wrong source/basis or incomplete receipt is rejected.

## CV8. Two E-tower observer clocks can converge without synchronizing (CLASSICAL FINITARY SUPPORT)

Let \(D^A_n,D^B_m\) be increasing causal downsets of authenticated evidence, each covering the same eventually delivered observation set \(D_\infty\). Suppose a target \(t\) is supported by a **finite** set of actual observations in \(D_\infty\). Then there are finite \(N,M\) at which both towers possess the entire support and independently certify the same \(t\), *even if their checkpoint times, spatial positions and local coordinate orders differ.*

**Proof:** list the finitely many events supporting a proof. Cofinality/fair delivery guarantees a finite receipt index in each tower for each event. Take the maximum for each tower and replay the same sound target proof from original-source receipts. This uses no universal simultaneous slice. If the model source class \(X\) is FINITE and the limiting compatible source set forces \(t\), finite support follows by choosing one separating event for each counter-source \(x\in X\) with \(t(x)\ne t(x_*)\). For compact \(X\), continuous finite-valued target and closed observation fibers, a related compactness argument may provide finite support. If fair delivery, source compatibility, finitary proof or eventual target identifiability fails, no conclusion follows.

The finite lab constructs two physical receipt paths A1→A2 and B1→B2 with different checkpoint positions/times and the same original XOR conclusion; it rejects a 'checkpoint sequence' that simply skips its required causal parent, no matter how plausible its wall-clock order looks.

## CV9. Perceptual momentum as a deliberately qualified operational observable (PROPOSED INTERPRETATION)

A tower's report has three distinct coordinates:

- **Physical velocity/frame tilt:** for an actual timelike worldline, proper time \(\tau\) and Lorentz frame are defined geometrically. Example: from \((0,0)\) to \((5,3)\), the climber experiences four proper-time units while base E assigns five coordinate-time units. Eight **declared** source events give rates 2 per proper time and 8/5 per E coordinate time.
- **Epistemic lag:** the set of source- and claim-relevant evidence event IDs known at A but not yet causally delivered to E, with immutable owner and basis. No physical transformation creates a new event ID or makes a missing report available.
- **Semantic momentum:** path-dependent change of model frame/probe basis, quantified by verified representation arrows and their holonomy. This need not have any literal Minkowski metric, proper time or conserved mechanical momentum.

The natural law for a high observer may be expressed in locally convenient coordinates while E expresses the same source invariant differently; **equivariance and original-target invariance, not equality of reports, is the criterion of agreement**. The proposed unification into one empirical physical 'cognitive Lorentz' metric is UNVERIFIED.

## CV10. Finite closure and counterexamples: exact gates (CLASSICAL / PROVED MODEL)

Full source/input provenance is an independent obligation. Passing a synthetic frame square, observing a test table and comparing identical causal receipts do **not** authenticate an external physical device or underlying ontology. Source IDs bind a formal context, not the universe.

Negative controls explicitly tested:

1. Coordinate simultaneity flips for spacelike A/B discoveries, while lightlike A→E receipt remains future-directed.
2. A physically available event that was never wired into E's ancestry supplies **no** knowledge.
3. A noninvertible carrier map can satisfy the observation square but erase a target about the original carrier.
4. A reversible carrier map can preserve truth but forget a target through a coarse report.
5. Two noncommuting semantic shears preserve zero-vs-nonzero but not parity.
6. A commuting square whose relation omits a compatible source pair fails Beck--Chevalley.
7. Incorrect source/basis, unlicensed original-source probe, forged superluminal parent, non-nested checkpoint history and inconsistent empirical reports are rejected.
8. A source/observer rate ratio does not establish physical psychology, future prediction, carrier-independent source authentication, Euler/Gamma identity or RH.

## Independent academic setting, novelty and continuation

- Lorentz boosts, Wigner/Thomas rotation and relativity of simultaneity are classical relativity. Rational coordinates provide **exact computational calibrations** only.
- Causal event DAGs and consistent distributed snapshots are the setting of Leslie Lamport, *Time, Clocks, and the Ordering of Events in a Distributed System* (Communications ACM 21, 1978), DOI 10.1145/359545.359563. https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15712-s12/www/papers/lamport78.pdf
- Group actions/holonomy-invariant predicates, finite fiber factorization and set-theoretic Beck--Chevalley are classical category/logic mathematics. A general Beck--Chevalley condition needs actual pullback and relevant adjoints; see https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/general-framework-for-the-semantics-of-type-theory/C6F4C4A0302E5F9E9F2B41BCABCA1E06 . No claim that we created the theory of relativity or the Beck--Chevalley condition.
- Existing SUCC source: `operational_yoneda_descent`, `adaptive_proof_policy`, `noncommuting_proof_transport`, `checkpoint_meta_tower`, `local_global_descent`, `shared_carrier_descent` and associated source ledger. This round adds the missing explicit **causal/Lorentz separation** and finite **simultaneity-independent proof receipt** interface without mutating those modules.

### What is still missing—ranked

1. **Authentic physical sourcing and interventions.** A device/action semantics that is independently certified to operate on the same original physical carrier. Formal coordinate transformations do not establish the metaphysical/empirical source.
2. **Indexed, compositional proof fibration.** Construct and verify a general source-indexed instrument category whose pullbacks, state-changing interventions, dependent proof objects and quantifiers satisfy Beck--Chevalley where justified, rather than isolated finite-set squares. Retain causally indexed original-source claims and gauge holonomy.
3. **Quantitative asynchronous resources.** A verified memory/bandwidth/noise/error/propagation model. Include physical reset/no-cloning constraints where relevant; a high E tower's epistemic macro-step is not a zero-time physical supertask.
4. **Actual empirical perceptual momentum model.** A measurable operational metric/connection on observer model states and communication latency. Classical Lorentz geometry alone does not prove brains, knowledge models or mathematical fields obey Lorentz laws.
5. **New arithmetic transport and global positivity.** Real adelic/Gamma/test-function domain maps and an original-prime-derived positive completed Weil/Suzuki form. Lorentz covariance/holonomy invariance do NOT generate RH-hard sign.
6. **Independent mechanization/priority.** Lean/formal proofs for CV4--CV8 plus systematic comparison with causal sheaves, distributed systems and categorical quantum measurement. Current exact rational code and written arguments are finite mathematical receipts, not full formal verification of relativity or an original discovery.

**Verdict:** Covariant proof-support descent is mathematically coherent under explicit source, frame, history and claim hypotheses. Locally lawful, noncommuting frames may contain incomparable but simultaneously valid epistemic views. An E-tower can become globally correct by receiving causally certified, source-compatible evidence without requiring globally synchronized time. The Lorentz analogy is a useful exact geometric test, NOT yet a physical identification of 'perceptual momentum'.
