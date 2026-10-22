# HISTORY-DTN: growing Dirichlet networks, material memory, and two-direction SUCC/FUCC

**Research date:** 2026-10-22. **Status:** independent draft research. **Pinned source:** femboy2112/SUCC main@b116841f12b41aaf7600da39bbb40577f25b6295 (reviewed Academic Main VIII). **Executable:** observational_succ/growing_dtn_history.py. **Focused hostile tests:** tests/test_growing_dtn_history.py. **Deterministic probe:** scripts/growing_dtn_history_probe.py. **Claim status crosswalk:** docs/CLAIM_SUPPLEMENT_HISTORY_DTN.md. **Verbatim motivation and provenance:** HISTORY_DTN_PROVENANCE.md. **Independent active research:** PRs #233/#234/#235; the present work is a separate sibling off reviewed main, not their merge or replacement.

## Abstract and source-typed research object

The motivating phenomenon is lightning and Lichtenberg-style dielectric damage: a globally constrained electric field guides local material change; each local modification changes the field for future steps; the completed conductive and damaged structures are persistent records of previous interactions. This research constructs the **finite mathematical core** of that proposal in linear passive resistor networks, then supplies a **separate stochastic history layer** and a **source-authentic arithmetic SUCC/FUCC clock layer**. Their compositional laws are exact, but identifying them as intrinsic physics is UNVERIFIED. A quasistatic DtN solve has no wavefront or optical Cherenkov threshold; the blue glow discussed in the originating conversation must be treated as a separate retarded-field hypothesis.

The author's stronger compatibility proposal is: "What it SUCC looking backward while advancing forward has to agree with FUCC looking foward while advancing backward, within the same system?" This is deliberately **not** weakened to naive SUCC/FUCC commutativity. We test (a) forward evolution and backward conditional reconstruction on a single graph-state path space; (b) genuine additive and prime-multiplicative arithmetic actions on a source-labeled observation clock and their adjoints; and (c) whether their coincidence has a **source-certified** physical naturality map. (a) and (b) survive as separate exact constructions; (c) is open.

## 1. Boundary-value definition and theorem HDTN-01

Let \(G=(V,E,c)\) be a finite undirected graph with strictly positive edge conductances \(c_e>0\). Fix a nonempty electrode boundary \(B\subseteq V\); the interior is \(I=V\setminus B\). Assume each connected component meets \(B\), equivalently the grounded interior Dirichlet block \(A=L_{II}\) is positive definite. \(L\) is the weighted graph Laplacian. For a boundary voltage \(f\in\mathbb R^B\), the unique harmonic extension is

\[
Hf=(f,-A^{-1}L_{IB}f).
\]

The Dirichlet-to-Neumann response, or Kron-reduced boundary Laplacian, is

\[
\boxed{\Lambda_G=L_{BB}-L_{BI}A^{-1}L_{IB}.}
\]

The energy minimizes over interior voltages:

\[
f^\top\Lambda_G f
=\min_{u|_B=f}\sum_{\{x,y\}\in E}c_{xy}(u_x-u_y)^2.
\]

Hence \(\Lambda_G\succeq0\) and \(\Lambda_G\mathbf 1=0\). This is classical finite network theory, already connected to observational SUCC in dynamic_boundary_inverse.py, which additionally explores dynamic RC probes and inverse nonuniqueness.

**Exact rank-one insertion theorem (CLASSICAL; new-to-project implementation).** Add a fixed conductance increment \(g>0\) on oriented vertices \(e=(x,y)\), with incidence \(b=\delta_x-\delta_y\). Define \(b_I\) as its grounded interior projection,

\[
r=b_I^\top A^{-1}b_I\ge0,\qquad w=H^\top b\in\mathbb R^B.
\]

Then, with \(G'=G+ge\),

\[
\boxed{\Lambda_{G'}-\Lambda_G=\frac{g}{1+gr}\,ww^\top.}
\]

**Proof.** The new Laplacian is \(L'=L+gbb^\top\). Under a fixed electrode drive \(f\), the new interior minimizer is
\(u'_I=u_I-\frac{g}{1+gr}A^{-1}b_I(w^\top f)\).
Insert it into the quadratic Dirichlet energy and complete the square. The total increase is
\(\frac{g}{1+gr}(w^\top f)^2\).
Equality for all \(f\), followed by polarization, gives the exact matrix formula. Equivalently Sherman–Morrison expands the grounded inverse. This proof requires a fixed linear conductance increment in the solve; a nonlinear plasma front cannot be assumed to satisfy the same constitutive equations. QED.

**Consequences.** Every edge insertion increases the measured DtN form in Loewner order; the difference has rank at most one; it vanishes precisely when \(w=0\), meaning the endpoints have zero harmonic voltage difference under **all** boundary drives. Here \(r\) is the **grounded interior Green-function quadratic**, not generally the unrestricted two-terminal effective resistance between x and y. Boundary-boundary insertion has \(r=0\). Energy under an electrode drive \(f\) changes by \(\frac{g}{1+gr}(w^\top f)^2\).

## 2. Hidden material / future probe: exact nonidentification counterexample

Construct the four-node diamond with electrodes \(L,R\), internal vertices \(u,v\), and unit conductances on four arms \(L-u,u-R,L-v,v-R\). The two internal voltages both equal \((f_L+f_R)/2\) for **every** boundary voltage. Thus \(\Lambda_G=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\).

Adding interior edge \(u-v\) of conductance \(7\) produces **zero boundary change**, since \(w=0\), despite changing the full material graph. This refutes the unrestricted inference that a complete static boundary response identifies every internal edge. Such uniqueness may hold under special circular-planar or criticality assumptions; we do not negate those classical results.

Now apply the **same** new intervention \(L-u\) conductance increment \(1\) to each network. Electrode drive \(f=(0,1)\) gives

\[
C_{\mathrm{eff}}(G+(L,u))=\frac76,
\qquad
C_{\mathrm{eff}}(G+(u,v;7)+(L,u))=\frac{49}{41}.
\]

All rational results are regenerated by the independent grounded Schur/Kirchhoff implementation. Therefore present observation equivalence need not be **future-safe**: the material can hold a response-invisible degree of freedom that changes the outcome of future contact. This is a mathematically exact, very restricted sense of *imprinting*, not evidence of retrocausation or hidden quantum measurement.

## 3. Flatness under fixed increments versus actual material path-dependence

If the allowed edge increments have fixed conductances \(g_i\), then for any order \(\pi\),

\[
L_{\mathrm{final}}=L_0+\sum_i g_i b_i b_i^\top.
\]

Hence the terminal DtN matrix is independent of insertion order, even though the intermediate \(H_t,w_t,r_t\) and each individual gain depend on the order. Telescoping gives the exact identity \(\sum_t(\Lambda_{t+1}-\Lambda_t)=\Lambda_T-\Lambda_0\). On the fixed-conductance inclusion cube, this is an exact response potential, **not a nonzero terminal holonomy**. The implementation tests all \(3!=6\) orderings for a three-edge set and independently recomputes every Schur difference.

To introduce genuinely path-sensitive terminal geometry, declare a toy material-response law evaluated at insertion:

\[
g_e(G;f)=g_{\mathrm{base}}\left[1+\kappa(H_Gf(x)-H_Gf(y))^2\right],
\qquad \kappa\ge0.
\]

On the same diamond, apply \(f=(0,1)\), \(\kappa=1\), adaptive interior edge \(u-v\) with base 1, and a fixed \(L-u\) increment 1. Adaptive first: \(g_{uv}=1\) and final \(C=13/11\). Fixed first: internal voltages \(u=1/3,v=1/2\) give \(g_{uv}=37/36\) and final \(C=474/401\). The exact commutator-like **order defect** is

\[
\boxed{\frac{474}{401}-\frac{13}{11}=\frac{1}{4411}>0.}
\]

These laws are *toy, explicitly declared* constitutive rules. No experimental parameter or wood/carbonization prediction is asserted. The result demonstrates what additional modeling is needed before a history-dependent DtN description has genuine terminal path dependence.

## 4. A further general theorem: future-safe response equivalence

For any deterministic finite state space \(X\) (states must include all constitutive material memory), authorized interventions \(T_a:X\to X\) for letters \(a\) in alphabet \(A\), and observable \(O:X\to Y\) such as \(O(G)=\Lambda_G\), define

\[
x\equiv_\infty y
\iff
\forall w\in A^*,\quad O(T_w x)=O(T_w y).
\]

**Future-safe quotient theorem (CLASSICAL automata/Moore equivalence specialized here).** This is the **largest transition-compatible equivalence** refining current-response equality. Moreover for finite \(X\), the partition-refinement process starting from equality of \(O\) and repeatedly separating states by their successors reaches its fixed point after at most \(|X|-1\) strict refinement rounds.

**Proof.** Equality of every continuation trace is an equivalence relation, contains the empty word, and is stable under adding any authorized intervention in front of the continuation word. Conversely let \(R\) be any equivalence contained in current \(O\)-equality such that \(xRy\Rightarrow T_a x\,R\,T_a y\) for all \(a\). Induct on word length to obtain \(T_w x\,R\,T_w y\); since \(R\) refines \(O\)-equality, \(O(T_w x)=O(T_w y)\). Hence \(R\subseteq\equiv_\infty\). On a finite set every nontrivial strict partition refinement increases the number of equivalence classes by at least 1 and at most \(|X|-1\) strict increases exist starting from the one-class bound. Fixed points are transition-compatible and therefore realize \(\equiv_\infty\). QED.

**Interpretation.** Current \(\Lambda\) equality is not a congruence for authorized interventions, as the hidden-edge diamond witnesses. A source-relative, future-safe quotient needs the intervention alphabet and actual material-state dynamics, not just the present measurement. Infinite/unbounded, stochastic and physically uncertain interventions require separately stated notions; the finite proof does not establish uniform physical decidability. This is a classical theorem, not novel automata mathematics.

## 5. Exact backward/forward compatibility on the SAME growth system

Fix a finite configuration space \(X_t\) at discrete growth stage \(t\), and a declared Markov kernel \(K_t(x,y)\) for transitions. In the exact executable toy, \(X_t\) is a rung of the Boolean subset lattice of candidate edge labels; each candidate has strictly positive field-guided weight \(\epsilon+(\phi(x)-\phi(y))^2\), the field being recomputed after each actualized edge. This is a stochastic *model*, not a calibrated dielectric breakdown rate.

Given normalized initial law \(\alpha_0=\mu\) and target indicator \(\beta_T=1_A\), define

\[
\alpha_{t+1}(y)=\sum_x\alpha_t(x)K_t(x,y),
\qquad
\beta_t(x)=\sum_y K_t(x,y)\beta_{t+1}(y).
\]

**Exact dual overlap and conditioning theorem (CLASSICAL).**

\[
\boxed{\sum_x\alpha_t(x)\beta_t(x)=Z=\Pr(X_T\in A)
\quad\text{for every }t.}
\]

Proof: expand beta, interchange two finite sums and recognize the alpha recurrence. This is the rigorous, non-retrocausal sense in which a forward actualized process and its backward-looking future constraint must agree: they represent the SAME probability measure on histories, observed across different cuts. In the deterministic rational toy, the exact common overlap is \(Z=4655/6831\) on all three levels.

If \(Z>0\), the selected path marginal is \(\Pr(X_t=x\mid A)=\alpha_t(x)\beta_t(x)/Z\). Where \(\alpha_{t+1}(y)>0\), the exact Bayes backward kernel is

\[
R_{t+1}(y,x)=\frac{\alpha_t(x)K_t(x,y)}{\alpha_{t+1}(y)},
\]

so \(\alpha_t(x)K_t(x,y)=\alpha_{t+1}(y)R_{t+1}(y,x)\) is an exact shared edge flux from opposing temporal descriptions. Where \(\beta_t(x)>0\), the **forward success-conditioned Doob kernel** is

\[
K^A_t(x,y)=K_t(x,y)\frac{\beta_{t+1}(y)}{\beta_t(x)}.
\]

**Hostile conditional-reversal result.** The backward Bayes kernel conditioned on success **and the current state** is the same \(R\) on supported states: substituting \(\alpha^A_t=\alpha_t\beta_t/Z\) and \(K^A_t\) cancels beta factors. Thus do *not* claim that the future changed local physical causes or that every future-conditioned reverse transition is a new kernel. Stochastic reverse-time inference is generally not an inverse dynamical map; many histories lead to the same later state.

The tests retain a zero-success target, wrong row-sum mutation, supported-state flux equality, and the exact \(\alpha\beta\) invariant. This whole compatibility structure uses just stochastic finite histories, not prime number theory.

## 6. Genuine arithmetic SUCC/FUCC square and its limitations

Use the actual arithmetic source on \(H=\ell^2(\mathbb N_{\ge1})\):

\[
S|n\rangle=|n+1\rangle,\qquad V_p|n\rangle=|pn\rangle,
\]

for genuine primes \(p\). The **affine relation** is

\[
\boxed{V_p S=S^p V_p,\quad S^*V_p^*=V_p^*(S^*)^p.}
\]

They do **not** naively commute. \(V_p^*|m\rangle=|m/p\rangle\) when \(p\mid m\), otherwise \(0\); \(S^*|1\rangle=0\). These adjoints are **partial backwards shift operators**, not an invertible time machine and not the Bayes kernel \(R\).

On a single **source-recorded graph history** \(G_0,\ldots,G_T\), define the declared observation clock \(O(\omega,n)=\Lambda_{G_{n-1}}\) for \(1\le n\le T+1\). Both index routes \(n\xrightarrow S n+1\xrightarrow{V_p}p(n+1)\) and \(n\xrightarrow{V_p}pn\xrightarrow{S^p}pn+p\) land on the **same source-recorded terminal snapshot**, provided the endpoint is in the observed horizon. The intermediate snapshots can differ. This is a valid synthetic arithmetic chart using a shared material-history fiber, **not a genuine physical operation of multiplying the discharge time index by a prime**. Compare independent existing PR #235 for the full affine positive-monoid tower and its cutoff-exit defects.

**Faithfulness no-go.** A source graph with two distinct edges \(e\ne f\) available as one-step growth actions has distinct successors \(G+e\), \(G+f\). A scalar additive clock mapping both steps to \(n\mapsto n+1\) sends these distinct children to the same integer. Hence a time counter cannot be a faithful representation of a branching event category unless augmented with source-labeled path/branch fibers or quotient-authorizing observational equivalence. This is an exact graph-level obstruction, consonant with existing field_history_lift.py.

**What remains OPEN:** a natural, source-certified functor or factor action from physical/electrical material dynamics to the genuine prime multiplicative semigroup that also transports the response/operator observables. Mere endpoint equality is insufficient. The physical process's stochastic backward inference, its future-conditioned forward process, and arithmetic prime adjoints are THREE distinct notions with THREE different domains.

## 7. Wave, Lorentz, Mach and Cherenkov firewall

The static DtN model uses an elliptic boundary-value solve and a (possibly history-dependent) graph update. It does not define a finite propagation speed for the electromagnetic field; interpreting it as literal instantaneous causation is wrong. For a physical wave analogue, declare independent response field \(q\) with damped wave/Maxwell/telegrapher operator, retarded Green function, constitutive dispersion, coupling \(J(G_t)\), and measure its propagation speed \(u(\omega)\). A schematic linear toy equation is

\[
(\partial_t^2+2\gamma\partial_t-u^2\nabla^2)q=J_{G_t}.
\]

An ideal steadily moving source has Fourier support \(\omega=\mathbf{k}\cdot\mathbf v\); Cherenkov-like phase matching requires \(\omega(\mathbf k)=\mathbf k\cdot\mathbf v\), and an appropriate mode-phase-speed threshold. The phase velocity, group velocity and causal front velocity are not interchangeable. Such modes can be slower than vacuum \(c\), allowing a mode-relative Mach number \(v/u>1\) while respecting real special-relativistic causality. **No modeled blue spectrum, physical Cherenkov radiation, or experimentally determined wood-discharge wavefront follows from the present project.** Plasma fluorescence and damage tracks can occur without a Cherenkov cone. A luminous material wake may visualize relaxation/damage but not uniquely identify a supermode front.

## 8. Adversarial verdict table and certification boundary

| Proposed inference | Discriminator | Verdict |
| --- | --- | --- |
| Every changed edge is visible from present electrodes | Symmetric hidden u-v edge yields w=0 | REFUTED in unrestricted graphs |
| Invisible now means irrelevant to all future responses | identical L-u intervention yields 7/6 vs 49/41 | REFUTED (future-safe quotient needed) |
| Local fixed edge changes necessarily create terminal order dependence | all 3! insertion orders have same final L | REFUTED for fixed additive increments |
| Constitutive feedback can create terminal order dependence | rational 1/4411 defect | PROVED LOCAL under toy law |
| DtN edge gain formula holds for positive finite resistor graphs | Sherman-Morrison + grounded Schur and flux | CLASSICAL; exact executable model |
| SUCC forward / endpoint-backward messages can agree | overlap invariant and Bayes flux | CLASSICAL; exact model |
| Bayes reversal IS FUCC prime backward shift | division annihilates nonmultiples; different domains | REFUTED as conflation |
| V_p and S commute | actual affine braid, adjoint braid | REFUTED naive; CLASSICAL corrected |
| One counter counts all source histories faithfully | branching collision of distinct one-edge events | REFUTED |
| Similar discharge patterns prove SUCC fundamental, or blue means Cherenkov | no physical calibration or transporting functor | UNVERIFIED |

## 9. Reproduction, provenance, and next verdict-changing probe

Reproduce with: python -m unittest discover -s tests -p 'test_growing_dtn_history.py' -v; python scripts/growing_dtn_history_probe.py; python scripts/verify_provenance.py. The deterministic JSON receipt includes SHA256 for source, test and probe plus exact fractions; the separate GitHub Actions workflow requests Python 3.10 and 3.13. Our initial 18/18 local test receipt used a source-consistent minimal adapter of RCNetwork because the full repository checkout was inaccessible from that execution container; these are not **GitHub CI** or full-repo proof. This branch does not modify original provenance or other theories, and carries no Lean proof or full-universe physics claim.

**Next theory probe:** implement finite deterministic future-safe quotient partition refinement for interventions, independent matrix-tree/Kirchhoff oracle, and source-labeled stochastic bisimulation for material-memory states. Seek an honest transported arrow from genuine arithmetic prime source into physical response paths, and demand an explicit adversarial witness if it cannot exist. Only then introduce independently calibrated delayed wave physics and test A/B/C/D: frozen field, growing quasistatic field, material memory, wave-coupled dynamics. D must predict an *extra* angular, time-delay or spectral observable rather than simply reproduce branches that C already generates.

**Project provenance:** AGENTS.md and docs/METHOD.md (steelman/crucible/verdict), existing dynamic_boundary_inverse.py (static/dynamic source inverse), field_history_lift.py (history/point distinction), independent [PR #235](https://github.com/femboy2112/SUCC/pull/235). **Classical source attribution:** E. Curtis & J. Morrow, *The Dirichlet-to-Neumann Map for a Resistor Network* (SIAM J. Appl. Math. 51, 1991), DOI 10.1137/0151051; E. Curtis, D. Ingerman & J. Morrow, *Circular Planar Graphs and Resistor Networks* (Linear Algebra Appl. 283, 1998), DOI 10.1016/S0024-3795(98)10087-3; L. Niemeyer, L. Pietronero & H. Wiesmann, *Fractal Dimension of Dielectric Breakdown* (PRL 52, 1984), DOI 10.1103/PhysRevLett.52.1033; classical Kirchhoff, Kron/Schur, Sherman-Morrison, Doob h-transform, Moore/Myhill-Nerode finite observational congruence, and Markov forward/backward recursions. **No academic priority claim. No completed-Weil positivity, RH, real ER=EPR or intrinsic gravitational discovery.**
