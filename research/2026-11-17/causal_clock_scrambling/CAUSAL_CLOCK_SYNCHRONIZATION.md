# Causal Clock Synchronization, Moving Observation Walls, and Source-Pinned BBP Scrambling Controls

**SUCC / Principia Observatoris / Endpoint-Coercivity continuation** — 2026-11-17  
**Originating proposal:** the finite-resolution observation boundary can behave like a moving wall: a low-order return may be noise-like while the observer–boundary coupling retains signed higher-order information. Local models have time as a function of causal events; comparisons produce *differential causal time*; an objective account can construct a coherent *proper causal time* by reconciling competing models through a costed causal graph.

**Verdict:** CCS-01–07 are exact, conditional constructions or no-go results in the stated mathematical models. The coupling mechanism is a classical information-hiding example, not evidence of physical chaos. CCS-08 is an **OPEN** source-selected arithmetic proposal; R0, π base-16 normality, an actual thermodynamic vacuum, literal Lorentzian proper time, and physical quantum scrambling remain **UNVERIFIED**. "Proper causal time" is a candidate *term for an operational consensus clock*, not the physical relativistic quantity.

## 1. Source passport and scope

Retain exactly the original zero-seeded BBP dynamics:
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
With the classical BBP identity \(x=\pi/16\), \(Y_n=16^n x=U_n+T_n\), and
\[
T_{n+1}=16T_n-r(n+1),\qquad 0<T_n<r(n+1)/15.
\]

**CCS-01 (EXACT source compensation):**
\[
\boxed{
(U_{n+1},T_{n+1})
=(16U_n+r_{n+1},\,16T_n-r_{n+1}),\qquad
Y_{n+1}=16Y_n.
}\tag{CCS1}
\]
The forcing is a **signed local connection coefficient**, not a physical force or a new stochastic degree of freedom. Both paths are time-labelled by the **same source clock** n.

For \(\ell\ge0\) put
\[
F(n,\ell)=\sum_{j=1}^{\ell}16^{\ell-j}r(n+j).
\]
Then
\[
U_{n+\ell}=16^\ell U_n+F(n,\ell),\quad
T_{n+\ell}=16^\ell T_n-F(n,\ell),
\]
with the exact cocycle
\[
\boxed{F(n,\ell+m)=16^mF(n,\ell)+F(n+\ell,m).}\tag{CCS2}
\]
The direct \(A\to C\) computation and composed \(A\to B\to C\) computation agree **with source transport and compensator retained**. Dropping the forcing before the composition manufactures a spurious discrepancy.

This interface connects the previously proved exact co-moving chart \(g_n(z)=e(-U_n)z\), its residual \(e(T_n)\to1\) without finite equality, and Principia's source-labelled signed defect transport. It does NOT entail any Weyl-energy saving.

## 2. Three operational clocks

A **causal carrier** is an event DAG or locally finite partial order \(C\) with explicit state-transition maps and a declared source passport. A *causal path* is a chain \(\gamma=(e_1,\ldots,e_k)\) through actual dependencies. Parallel chains may be compared even though the directed causal order contains no directed cycles.

**Model causal time.** For observer \(i\), define a nonnegative labelled path cost
\[
\boxed{\tau_i(\gamma)=\sum_{e\in\gamma} c_i(e).}\tag{CCS3}
\]
Different \(c_i\) can count computation steps, source updates, physical elapsed seconds, energy estimates, memory dependencies, or weighted interventions—but they cannot be compared numerically without calibrating their units. If the cost depends on history, extend the state first; do not quietly assume additivity. \(\tau_i\) is a local **costed ordering**, not an independently proven physical time metric.

**Differential causal time.** After declaring comparison events, matching observables, orientation, units and transports, let \(a_e\in\mathbb R\) be the measured inter-observer clock offset on comparison edge \(e=(i,j)\). The clock discrepancy relative to candidate global vertex labels \(\theta\) is
\[
\boxed{\delta_e=a_e-(\theta_j-\theta_i).}\tag{CCS4}
\]
This is a real-valued signed 1-cochain on the **observer-comparison graph**. It is different from the operator defect \(P_jK_e-L_eP_i\) unless a scalarization/calibrated clock response has been provided. Changing observer charts correctly transports labels and norms; a raw sign mismatch is not intrinsically curvature.

**Operational consensus / proposed 'proper causal time'.** Freeze a connected comparison graph, source-valid event matching, positive confidence weights \(w_e\), a cost/scale convention and a reference \(\theta_{i_0}=0\). Solve
\[
\boxed{\theta_*=\underset{\theta:\theta_{i_0}=0}{\operatorname{argmin}}
\sum_e w_e\big[a_e-(\theta_j-\theta_i)\big]^2.}\tag{CCS5}
\]

**CCS-02 (CLASSICAL, EXACT — graph Hodge/least-squares clock lemma):** the grounded weighted graph Laplacian is positive definite, so \(\theta_*\) is unique after the reference is fixed. Its residual obeys \(D^TW(a-D\theta_*)=0\) where \(D\) is the oriented edge-incidence matrix. Moreover the minimum is zero **if and only if the signed comparison offsets sum to zero around every undirected graph cycle**. Proof: zero residual is exactly the existence of a vertex potential; a spanning-tree integration gives such a potential when all cycle sums vanish.

On a tree every arbitrary comparison flow can be fitted with zero residual: **a genuine comparison loop is the smallest possible defect discriminator**. The cycle in the comparison graph is not a causal cycle in the event DAG. This is the ordinary discrete Hodge decomposition/least-squares alignment idea, not a novel proof of general-relativistic proper time.

**Concrete hostile calibration.** Three reports \(a_{AB}=2\), \(a_{BC}=3\), \(a_{AC}=6\) disagree by the oriented cycle sum \(2+3-6=-1\). With unit weights, the optimal anchored potentials are \(\theta_A=0,\theta_B=7/3,\theta_C=17/3\), giving residuals \((-1/3,-1/3,+1/3)\) on edges \(AB,BC,AC\) and irreducible squared error \(1/3\). This is **measured inconsistency**, not authentication of which model is correct: a calibration error, hidden state, or true latent transport defect could produce it.

**CCS-03 (NO-GO):** neither the bare causal order nor minimizing graph disagreement canonically determines physical proper time, Lorentzian signature, a unique cost per edge, a clock scale, or the fastest actual computation path. If a path is selected by minimizing computation cost, a separate constrained optimization must preserve declared source coverage and cannot drop inconvenient comparison observations. In causal-set theory, recovering Lorentzian geometry uses causal order **plus volume/number information and manifold-like hypotheses**. In Lorentzian spacetime the maximal timelike interval is a distinct physical concept; no identification with (CCS5) is claimed.

## 3. The moving boundary as an operational scrambling candidate

Let \(Z\in S^1\) be a source-labelled phase; let \(R,R'\) be independent Haar-uniform circle masks, and let \(J_p\sim\mathrm{Bernoulli}(p)\), chosen by the observer. Measure
\[
A=R,\qquad B=Z[J_pR+(1-J_p)R'].
\]
Each **entire marginal law** is source-independent Haar for every \(p\in[0,1]\), while
\[
\boxed{\mathbb E(\overline AB\mid Z,p)=pZ,\qquad
\frac{d}{dp}\mathbb E(\overline AB\mid Z,p)=Z.}\tag{CCS6}
\]

**CCS-04 (CLASSICAL EXACT):** information invisible in every individual readout is recoverable from a shared-coupling joint observable. Independent masks at \(p=0\) give the source-independent null pair law. The derivative at \(p=0\) is a **prediction for a calibrated intervention**, not an observation if no change in \(p\) is accessible. At \(p=1\) the pair-product reveals \(Z\) exactly; the construction is mathematically **one-time-pad-style masking**, not necessarily chaos or physical scrambling.

"Wall bounce" becomes a meaningful model only after declaring: input probe, boundary channel, source state, output instrument, what variables are averaged, response kernel and an independent-/shuffled-clock negative control. "The local output looks random" alone does not imply lossless transport or any hidden recoverable phase. A genuinely irreversible many-to-one channel can erase information; a reversible source-coupled channel can hide it in correlations. Physics uses more stringent tests such as operator spreading/OTOCs and decoding to diagnose quantum information scrambling (Xu–Swingle 2024), and even OTOC decay can be confused with decoherence (Landsman et al./experimental literature). No claimed BBP or physical OTOC measurement has been run.

The earlier finite-stage residual \(T_n>0\), and its \(O(n^{-2})\) resolution, are an **analytic unattainability** example. They are not an actual temperature, vacuum energy, heat flux or reflected force. The shell norm's \(B^{-5}\) baseline (prior endpoint-coercivity report) can arise solely from a nonzero unfinished tail even in a completed locked control. A legitimate BBP probe must exceed that calibrated source uncertainty before a "bounce" can be interpreted as objective phase disagreement.

## 4. Causal order alone is not enough to select π

**CCS-05 (EXACT no-go within a seed-blind source family).** For arbitrary real seed \(s\),
\[
U_n(s)=U_n(0)+16^n s,\qquad
U_n(s)+T_n=16^n(x+s).
\tag{CCS7}
\]
All members have **identical** forcing \(r(n)\), integer source-event order, chronological cocycle \(F(n,\ell)\) and causal graph. But the particular mathematical changed seed \(s=-x\) gives the **perfectly locked completed orbit** \(Y_n=0\), so R0 fails there. The original \(s=0\) is distinct and remains the sole target.

Therefore **no observable that depends only on \((r(n),\mathrm{causal\ order})\), while discarding seed and selected winding, can prove a positive anti-locking bound for every member of that family**. This is a counterexample to a *source-blind inference*, **not** a refutation of the authentic original source.

The simplest selected winding observable retains the exact carries:
\[
C_n=\lfloor U_n\rfloor,\quad f_n=U_n-C_n,\quad
k_{n+1}=\lfloor16 f_n+r(n+1)\rfloor,
\quad C_{n+1}=16C_n+k_{n+1}.
\tag{CCS8}
\]
The \(k_{n+1}\) may include a final 16-valued carry; they are not declared independent digits, statistical random noise or proper-time increments.

**CCS-06 (NO-GO to overfitting proper time):** for any phase sequence \(z_n\), a chart chosen as its *exact unknown value* \(g_n(z)=z_n^{-1}z\) makes its apparent local phase identically one. Thus unrestricted "maximal agreement" can make even highly moving orbits appear stationary. A clock/frame alignment that uses the to-be-proved answer, the completed π orbit, or future digits to choose gauges is not a source-authenticated observation. The lawful rational chart \(e(-U_n)\) instead gives \(w_n=e(T_n)\to1\), which is already true on both original and locked analogues and does not force R0.

## 5. What could turn causal-clock tomography into the missing arithmetic inequality?

The authenticated Main XXVI target is
\[
\boxed{\mathcal R_B
=\frac1B\sum_{k=1}^{B}
\left\|\frac{U_{2B}}{16^k}\right\|_{\mathbb T}^{2},
\qquad
\liminf_{B\to\infty}\mathcal R_B>0
\iff\mathrm{R0}.}\tag{CCS9}
\]
Prior work proves an exact comparison with \(1-\Re W_B\) and calibrates the analytic \(B^{-5}\) source-tail floor; it does not prove the eventual constant lower bound.

**CCS-07 (SOURCE-PRESERVING PROBE CONTRACT, CONDITIONAL):**
1. Preserve both source roots \(U_0=0\) and \(T_n\), the exact r(n), signed carries \(k_n\), and forward/backward transport to a single terminal rational endpoint \(U_{2B}\). No source-changing "clock optimization."
2. Pick two *different* finite observer decompositions of the same source chronology (e.g., direct vs staged transport, or disjoint carry/cofactor windows) and a predeclared scalar/phase comparison instrument. Calibrate the transport units and expose *signed*, lagged joint responses rather than moduli or untyped variances.
3. Freeze comparison loops and their expected source cochain; measure *residual* cycle/diamond defects after lawful reconciliation. Refit neither the source labels nor the units to the held-out residual. A large residual is a diagnostic, not automatically proof of a cause.
4. Require a source-derived inequality \(J_B\le C\mathcal R_B+\varepsilon_B\) with \(\varepsilon_B\to0\) **and** a genuinely independent arithmetical estimate \(J_B\ge\delta>0\) for every late B. Only the combination can yield the R0 lower bound. If \(J_B\) is merely a disguised Weyl sum, this gains no theorem.
5. Test the identical-forcing wrong seed \(s=-x\), the shell-dependent dyadic winding-erasure seed, a rational alias, the sparse irrational failure class, and shifted/shuffled comparison clocks. At least one control must split the preferred mechanism, otherwise the new observer simply renames the open obstruction.

**CCS-08 (CONJECTURED / UNVERIFIED):** a zero-seed-sensitive signed clock-comparison response involving chronological carries and their odd-denominator source ancestry might produce a residual whose source-selected density has an all-late-shell positive bound. The existence of such a source estimate is not shown. Mere clock reconciliation, full-shift entropy, Gamma transport, or information-masking identity cannot supply it.

### Provenance / literature

- [SUCC original source/phase interface](../../../docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md), [source-selected endpoint coercivity](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), [terminal winding-erasure hostile control](../../2026-11-16/defect_window_tomography/TERMINAL_WINDING_ERASURE.md), [moving-frame analytic unattainability](../../2026-11-16/defect_window_tomography/MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md), [movable order-lift boundary](../../2026-11-16/defect_window_tomography/MOVABLE_BOUNDARY_ORDER_LIFT.md), [Principia causal geometry CG-01–06](../../../docs/principia_observatoris/02_causality_geometry.md). Shared algebra and four-pole provenance are NOT independent source witnesses.
- Jiang, Lim, Yao, Ye, *Statistical ranking and combinatorial Hodge theory*, Mathematical Programming (2011), https://arxiv.org/abs/0811.1067 — gradient/cyclic edge-flow decomposition and global least-squares inference.
- Surya, *The causal set approach to quantum gravity*, Living Reviews in Relativity (2019), https://doi.org/10.1007/s41114-019-0023-1 — causal order and volume, manifold-like assumptions and causal-time geometry.
- Xu and Swingle, *Scrambling Dynamics and Out-of-Time-Ordered Correlators in Quantum Many-Body Systems*, PRX Quantum 5, 010201 (2024), https://doi.org/10.1103/PRXQuantum.5.010201 — operational scrambling, propagation, and OTOC limitations.

**Reproducibility:** [tests/test_causal_clock_scrambling.py](../../../tests/test_causal_clock_scrambling.py) uses exact Fractions and finite C4 null controls. It establishes scoped algebraic identities only. [Focused validation receipt](CAUSAL_CLOCK_VALIDATION.md) records the actual run and provenance. The full root AGENTS gates, formal Lean proof of this manuscript, independently calibrated physical instruments, and any new all-shell BBP result are **not claimed**.
