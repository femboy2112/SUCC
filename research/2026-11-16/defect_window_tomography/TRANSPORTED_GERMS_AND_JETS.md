# Transported Germs and Observer Differentials — the A → B → C Coherence Contract

**Operation:** Defect-Window Tomography / Principia Observatoris / Main XXVI interface  
**Date:** 2026-11-16  
**Originating hypothesis (Leah):** construct a path A→B, realize a lawful analytic continuation along that path, and place a new observer at B with the endpoint, original anchor, and a transported *analytic seed*. Then that observer should be able to continue B→C so that the result agrees with continuing A→C along the concatenated path. The desired seed is a transferable differential from which a new observer can predict previously unmeasured defects.  
**Status:** OGTJ-01–05 are exact classical/paper identities or source-typed exact examples; OGTJ-06–07 are conjectural or open. No new external mathematical priority, quantum/physical inference, RH or π-normality claim.

## 1. Steelman and correction: a value is not a germ

The correct typed identity is a **composition of arrows**, not an equality of incomparable arrows:

\[
\boxed{T_{\delta*\gamma}=T_\delta\circ T_\gamma,\qquad
s_C=T_\delta(s_B)=T_\delta T_\gamma(s_A),}
\]
for a declared path \(\gamma:A\to B\) followed by \(\delta:B\to C\) on which both transports exist.

The symbol \(T_{A\to C}\) denotes the transport along **that same concatenated path**. There is no general claim that every independently selected direct path \(\eta:A\to C\) gives the same result. That stronger conclusion needs flatness plus appropriate topology/trivial holonomy and actual source transport; even a flat connection can exhibit monodromy on a non-simply-connected domain.

For an unrestricted holomorphic function, the transferable *analytic seed* is a **germ** \(g_A\) (a compatible analytic function near A), not merely its scalar value \(g_A(A)\) nor an arbitrary fixed finite jet. Analytic continuation, when it exists along \(\gamma\), transports \(g_A\) to a germ \(g_B\). Continuing \(g_B\) along \(\delta\) agrees with continuing the original germ along \(\delta*\gamma\). This is the classical pathwise continuation rule, not existence of a global continuation.

**OGTJ-01 — pathwise germ composition (CLASSICAL):** If the initial germ admits continuation along \(\gamma\) and its resulting endpoint germ admits continuation along \(\delta\), concatenating their locally compatible analytic representatives is a continuation along \(\delta*\gamma\); uniqueness along a fixed path makes the two constructions equal. The endpoint germ, *not just its value*, is the complete continuation datum in this unrestricted class.

**Finite-jet obstruction:** For any fixed \(m\), the distinct entire functions \(f(t)=0\) and \(g(t)=(t-a)^{m+1}\) have identical derivatives through order \(m\) at \(a\) but different values at \(a+1\). Thus a first differential is never universally sufficient for arbitrary analytic functions. Under a specified finite-order ODE with uniqueness, a finite jet may instead be exactly sufficient.

**Monodromy obstruction:** The germ of \(\log z\) at \(z=1\) has value zero. Continuing it once anticlockwise around the excluded point 0 returns to the same basepoint with endpoint value \(2\pi i\); the contractible path returns with zero. A path/winding label, or a globally single-valued continuation domain, is required. See [University of Tübingen Riemann surfaces notes §3.9](https://www.math.uni-tuebingen.de/user/deitmar/LEHRE/Skripten/RS.pdf) and [Berkeley analytic continuation lecture](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_18.html). This does not say zeta itself is multivalued; its meromorphic continuation is single-valued. The branch-sensitive object is the chosen germ/path.

## 2. Exact transported *observer differential*: a time-varying intertwiner

Let \(X,Y\) be finite-dimensional real or complex vector spaces, \(a\le t\le c\), and \(K(t):X\to X\), \(H(t):Y\to Y\) continuous. Let \(U(t,s)\) and \(L(t,s)\) be their unique forward propagators:

\[
\partial_t U(t,s)=K(t)U(t,s),\quad U(s,s)=I,
\qquad
\partial_t L(t,s)=H(t)L(t,s),\quad L(s,s)=I.
\]

Let the observer chart \(P(t):X\to Y\) be continuously differentiable. Set

\[
\boxed{\mathcal E(t):=\dot P(t)+P(t)K(t)-H(t)P(t)}
\tag{OGTJ2}
\]
and define the signed finite-interval source-to-observer transport defect
\[
D(t,s):=P(t)U(t,s)-L(t,s)P(s).
\tag{OGTJ3}
\]

**OGTJ-02 — continuous signed defect transport (PROVED PAPER; classical Duhamel/variation of constants):**

\[
\boxed{
D(c,a)=\int_a^c L(c,t)\,\mathcal E(t)\,U(t,a)\,dt
}
\tag{OGTJ4}
\]

and for every \(a\le b\le c\),

\[
\boxed{
D(c,a)=D(c,b)U(b,a)+L(c,b)D(b,a).
}
\tag{OGTJ5}
\]

**Proof.** Differentiate \(D(t,a)\): using the two evolution equations,
\[
\partial_t D(t,a)=H(t)D(t,a)+[\dot P(t)+P(t)K(t)-H(t)P(t)]U(t,a),
\quad D(a,a)=0.
\]
Variation of constants gives (OGTJ4). For (OGTJ5), substitute the definitions and the composition laws of \(U,L\); the intermediate terms \(L(c,b)P(b)U(b,a)\) cancel with opposite signs. No commutation, positivity, or scalar approximation is assumed. \(\square\)

**Meaning:** \(\mathcal E(t)\) is the source-typed *infinitesimal observer defect*. It tracks moving readouts as well as source/model dynamics. If the authenticated path law, \(P\), and \(H\) are given along B→C, B can compute its future interval defect from this differential and the transported source state. If \(\mathcal E\equiv0\), all such transport squares commute. A single observed value of \(\mathcal E(B)\) alone does **not** determine the entire future defect without further dynamics/regularity.

The formula is the continuous-time counterpart of inherited [Principia CG-05/06](../../../docs/principia_observatoris/02_causality_geometry.md). It is not a new physical force, curvature form, or causal entropy. A nonlinear readout requires a separate nonlinear comparison and, when appropriate, its linearization along an explicitly selected trajectory.

### Exact mutation control

Take \(X=\mathbb Q^2\) at rational timestamps, \(K=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\), \(H=0\), and the moving row \(P(t)=(t,1)\). The polynomial propagator is
\[
U(t,s)=I+(t-s)K,\qquad
\mathcal E(t)=(1,t)+(0,t)=(1,t)
\]
**with a correction:** \(\dot P=(1,0)\), \(PK=(0,t)\), so \(\mathcal E(t)=(1,t)\) as displayed.

Then
\[
\boxed{D(t,s)=(t-s,\ t(t-s)).}\tag{OGTJ6}
\]
Indeed \((1,r)U(r,s)=(1,2r-s)\), whose integral from \(s\) to \(t\) is exactly (OGTJ6). Omitting the chart differential \(\dot P\) incorrectly predicts the first coordinate of the defect to vanish. The interval composition equation holds identically in rational arithmetic. This verifies the *mechanism* of a moving observer's defect without requiring a physical energy interpretation.

## 3. Exact source-valid arithmetic calibration: prime observer jets

From [PCE #661](https://github.com/femboy2112/SUCC/pull/661), at \(s=-1\) a finite genuine-prime inventory \(Q\) has
\[
E_Q=\prod_{p\mid Q}(1-p)^{-1},\quad R_Q=(-1/12)/E_Q,\quad
u_Q=(E_Q+R_Q)/2,\quad v_Q=(E_Q-R_Q)/2,
\quad u_Q^2-v_Q^2=-1/12.
\]

The *actual discrete* insertion of a new genuine prime \(p\) has
\[
T_p=-\begin{pmatrix}\cosh t_p&-\sinh t_p\\-\sinh t_p&\cosh t_p\end{pmatrix},
\quad t_p=\log(p-1).
\]

Introduce an auxiliary boost chart **between** prime insertions, where \(\partial_tu=-v\), \(\partial_tv=-u\), and \(\partial_t^2u=u\). The source-typed first-order jet is
\[
\boxed{j_Q=(u_Q,q_Q),\qquad q_Q:=\partial_tu=-v_Q.}\tag{OGTJ7}
\]
It gives the exact one-prime update
\[
\boxed{
j_{Qp}=-
\begin{pmatrix}\cosh t_p&\sinh t_p\\
\sinh t_p&\cosh t_p\end{pmatrix}j_Q.
}\tag{OGTJ8}
\]

**OGTJ-03 — prime-seed transfer (EXACT SOURCE-LABELLED MODEL):** Under the *specified auxiliary boost law*, two numbers \((u,q)\) determine the full two-channel state \((E,R)=(u-q,u+q)\), and every prescribed next genuine-prime insertion. The update is coherent under concatenation because the boost matrices commute, while the \((-1)\) parity is retained at every actual prime insertion. The boost is a chosen analytic interpolation of the genuine finite source steps, not a physically or arithmetically observed fractional prime clock. The derivative \(\partial_t\) is **not** \(\partial_s\) of zeta.

**Sharp authentic-source witness:** Two different genuinely reachable finite inventories, \(Q_1=3\) and \(Q_2=2\cdot7=14\), have precisely the *same* projected value but different jets:
\[
\begin{array}{c|ccccc}
Q&E_Q&R_Q&u_Q&v_Q&q_Q\\\hline
3&-1/2&1/6&-1/6&-1/3&+1/3\\
14&+1/6&-1/2&-1/6&+1/3&-1/3
\end{array}
\]

For next prime \(p=5\), \(\cosh(\log4)=17/8,\ \sinh(\log4)=15/8\), so
\[
u_{3\cdot5}=-13/48,\qquad u_{14\cdot5}=47/48,\qquad
|u_{14\cdot5}-u_{3\cdot5}|=5/4.
\]
Given only \(u=-1/6\) and the two candidate source states, optimal minimax absolute prediction radius is \(5/8\). Giving B the **correct transported signed derivative** resolves it to zero within this restricted finite source family. Giving the wrong-sign derivative swaps forecasts and is decisively rejected.

For a fixed known invariant \(u^2-v^2=-1/12\), the magnitude \(|q|=\sqrt{u^2+1/12}\) is already fixed; at this source collision the missing information is just its **orientation sign**. This is a relative minimum, not a universal statement about full prime provenance. Two different prime inventories may produce the same \((E,R)\); the actual labels and allowed future prime set remain a separate authenticated source passport.

## 4. An actual BBP real-lift differential that distinguishes invisible integer shifts

The [computational continuum source history #659](https://github.com/femboy2112/SUCC/pull/659) declares an additional analytic real-lift path
\[
\gamma_x(t)=\exp(2\pi i16^t x),\qquad
x=\pi/16\ \text{for the authentic zero-seeded BBP source}.
\]

For any real \(x\), this is entire as a function of complex \(t\) (with positive real \(\log16\)). Its derivative is
\[
\boxed{
\dot\gamma_x(t)=2\pi i(\log16)\,16^t x\,\gamma_x(t).
}\tag{OGTJ9}
\]

At every nonnegative integer time \(n\), the distinct real lifts \(x\) and \(x+k\) (\(k\in\mathbb Z\)) produce the same circle observation, because \(k16^n\) is an integer. Yet
\[
\boxed{
\left.\frac{\dot\gamma_{x+k}}{\gamma_{x+k}}\right|_{t=n}
-
\left.\frac{\dot\gamma_x}{\gamma_x}\right|_{t=n}
=2\pi i(\log16)\,16^n k.
}\tag{OGTJ10}
\]

**OGTJ-04 — a source-law-dependent one-jet lift discriminator (EXACT ANALYTIC IDENTITY):** Once this entire interpolation and its time coordinate have been *explicitly chosen and source-authenticated*, the pair \((\gamma_x(t),\dot\gamma_x(t))\) determines \(x\), by
\[
x=\frac{\dot\gamma_x(t)}{2\pi i(\log16)16^t\,\gamma_x(t)}.
\]
Consequently the transported jet predicts the entire declared path even though its integer-time scalar observations alone cannot distinguish integer deck shifts. The derivative is a **new, stronger instrument**. It is not automatically measurable from the integer BBP orbit or inferred from any finite set of discrete samples, and arbitrary reinterpolations can change it. If a changing integer deck seed is given but the exact zero seed is *not* authenticated, the extra derivative separates that restricted family; it does not by itself prove the actual original-zero orbit escapes locking.

**OGTJ-05 — finite witness versus open asymptotic goal:** the signed winding across one tick remains \(15k16^n\) as proved in #659. Differentiation at the boundary and relative winding are compatible diagnostics of the same **declared** real lift, but neither provides the source-selected signed Weyl saving on every sufficiently late integer shell. The main BBP recurrence, future tail and physical/arithmetic meaning of the seed remain as in Main XXVI.

## 5. What B must inherit: a source passport, not an invented omniscient state

Under a known finite-order analytic ODE and calibrated observer maps, an operational handoff can be packaged as
\[
\mathsf{Seed}_B=
(\text{source passport }\tau,\ B,\ j_B,\
\text{orientation/path/history class},\
\text{analytic transport law},\
\text{readout chart and error budget}).
\tag{OGTJ11}
\]

- \(B\) is the destination **position**, not the observed value; do not conflate them.
- \(j_B\) is the *sufficient jet for the specified differential equation*, not always the whole germ. For unrestricted analytic continuation replace it with the full endpoint germ.
- The transport law, source label, and allowed path must be jointly valid. A stored numerical endpoint and its derivative without a lawful continuation rule cannot predict all future functions.
- Any physical/causal intervention required to measure a derivative has a distinct cost and disturbance budget. Mathematically transporting a known jet is not the same as physically acquiring it.
- Inverse reconstruction from a compressed report may fail or have nonzero minimax radius. **Handoff is a conditional construction**, not a proof that all reduced observers have enough information.

### Exact "minimal" conditions

Within the prime auxiliary boost class, \(j=(u,\dot u)\) is sufficient for all future boosts and sign-labelled insertions. Within the fixed negative zeta hyperbola and a *specified pair* of possible histories, \(u\) plus one orientation bit suffices for choosing the right continuation. Within the unrestricted class of analytic functions, **no fixed finite jet** suffices. In the continuous linear \(K,H,P\) class, an exact future defect generally needs the source propagators and the field \(\mathcal E(t)\) along the path, not only \(\mathcal E(B)\).

## 6. Crucible: where A→B→C must fail

1. **Unspecified path:** \(\log z\) has nonzero monodromy; equality of endpoints without an oriented path is insufficient.
2. **Unknown governing law:** \(f=0\) and \(g=(t-a)^{m+1}\) defeat any claimed universal finite-jet sufficiency.
3. **Wrong coarse readout:** \(u=-1/6\) aliases two genuine prime inventories; omitting \(q\) cannot predict next \(u\).
4. **Wrong gauge/sign:** the actual prime step is \(-B(t_p)\), not \(B(t_p)\); \(p=2\) has \(t_p=0\) but still flips sign.
5. **Missing moving-chart derivative:** \(P(t)=(t,1)\) forces the \(\dot P\) term in OGTJ2; omitting it breaks exact rational Duhamel comparison.
6. **Unmeasured BBP derivative:** integer-time circle data cannot determine an arbitrary chosen interpolation; a \(\dot\gamma\) expression is only a source-law prediction until a lawful path observer is supplied.
7. **Analytic endpoint versus arithmetic time:** \(\xi(-1)=\xi(2)=\pi/6\) and finite prime compensation do not alone yield an intertwiner from prime-analytic \(s\) variation to the actual zero-seeded BBP time/CRT carry process.
8. **Lossy averaging:** a Gamma-smoothed scalar can tend to zero for the perfectly locked \(x=1\) countermodel of #659; do not treat smoothing as a substitute for chronological real-phase control.

## 7. Claim ledger, provenance, and next verdict-changing probe

| ID | Status | Exact scope / debt |
|---|---|---|
| OGTJ-01 | **CLASSICAL / PROVED PAPER** | Pathwise analytic germ continuation composes when both segments exist; no endpoint-only path independence. |
| OGTJ-02 | **CLASSICAL / PROVED PAPER** | Continuous moving-observer defect differential, Duhamel integral, and signed composition under finite-dimensional C¹/continuous hypotheses. |
| OGTJ-03 | **EXACT SOURCE-LABELLED MODEL** | Prime \((u,q)\) boost jet reconstructs the two coordinate channels and predicts source-prime steps; auxiliary continuous clock only. |
| OGTJ-04 | **EXACT ANALYTIC IDENTITY** | Declared BBP real-lift one-jet distinguishes integer deck aliases and reconstructs chosen lift; new instrument not automatically observable. |
| OGTJ-05 | **EXACT / BOUNDARY** | Integer deck winding and derivative are compatible but not statistical cancellation. |
| OGTJ-06 | **CONJECTURED / UNVERIFIED** | A finite, source-authenticated analytic-jet handoff predicts genuinely withheld source-coupled defects across distinct SUCC observer types. |
| OGTJ-07 | **UNVERIFIED / OPEN** | The handoff yields an original-zero all-shell carry/Weyl saving or completed Weil positivity. No such estimate has been derived. |

**Source-map dependencies:** [Defect-Window Tomography](README.md), [Contextual Zero/Third Observer](CONTEXTUAL_ZERO_THIRD_OBSERVER.md), [CG-05/06](../../../docs/principia_observatoris/02_causality_geometry.md), [Computational Continuum #659](https://github.com/femboy2112/SUCC/pull/659), [Prime Compensation #661](https://github.com/femboy2112/SUCC/pull/661), [Main XXVI Frontier](../../../docs/PI_NORMALITY_FRONTIER.md), and [METHOD.md](../../../docs/METHOD.md). The constructions share classical and SUCC provenance. Independent finite implementations are regression evidence, not external source witnesses.

**Focused exact controls:** [tests/test_transport_germ_defect.py](../../../tests/test_transport_germ_defect.py) exercises rational prime-jet updates, two genuine-prime source collisions, zero-depth sign mutation, composition in two orders, a moving-readout Duhamel calculation, finite-jet insufficiency and integer-deck derivative coefficient. The universal derivations are on paper.

**Next decisive experiment:** On a single authenticated source, freeze A and B, their available readout toolkit, a *minimal candidate sufficient jet*, and a new C-window with a **predeclared signed prediction**. Compare with a matched counterfeit that preserves scalar endpoints but changes hidden derivative/holonomy. Show the predicted C defect distinguishes them under calibrated error bounds and preserves its source identity through the required transport. Only then seek a zero-seed, all-late-shell arithmetic inequality. No A→B→C slogan substitutes for that proof.
