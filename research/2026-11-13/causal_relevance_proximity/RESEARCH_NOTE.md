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
