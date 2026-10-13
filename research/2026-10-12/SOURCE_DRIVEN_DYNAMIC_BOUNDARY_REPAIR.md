# Source-driven SUCC repair on an unresolved inverse electrical network

**Date:** 2026-10-12. **Scope:** exact rational, finite, passive RC graphs with a declared linear time-invariant carrier law. **Status:** classical Schur/Kron reduction, star-mesh, positive Stieltjes resolvents, Ho–Kalman minimal realization, and elementary exact-source certificates combined into a new-to-SUCC discovery workflow. **Academic novelty is NOT established.** The physical network is a declared mathematical simulator, NOT a laboratory observation. This dossier uses no Riemann-zeta zeros or unproved RH principles.

## Why this is a genuine SUCC hard test

The preceding Galilean-to-Lorentz reconstruction worked because the missing geometry had a known answer. Here E begins with an **unknown latent finite electrical-network geometry**. The simulator alone holds the generating graph. E receives only exact boundary voltage-to-current matrices at lawful Laplace parameters. Starting with **one source-derived static response**, E (i) constructs multiple independent geometries, (ii) discovers that static measurement cannot choose between them, (iii) attempts the smaller dynamic repair and falsifies it with a later observation, (iv) infers what structural capacity is missing, (v) reconstructs and independently audits a two-hidden-mode model from only four finite response matrices, and (vi) discovers a residual *all-frequency* ontological ambiguity that no future boundary experiment of the declared kind can resolve.

A new theorem of universal mathematical priority is **not claimed**. The novel-to-project deliverable is a reproducible source-typed obstruction-to-repair E operator with an honest irreducible observation quotient.

## DB1. Declared original carrier and observation law (CLASSICAL)

Let \(G=(V,E,g)\) be a finite undirected network with strictly positive rational conductances, nonempty labeled boundary \(B\subseteq V\), interior \(I=V\setminus B\), and a nonnegative rational diagonal interior capacitance matrix \(C\). Each interior connected component meets the boundary. Its graph Laplacian is

\[
L=\begin{pmatrix}L_{BB}&L_{BI}\\L_{IB}&A\end{pmatrix},\quad A=L_{II}>0.
\]

For a fixed real Laplace parameter \(s\ge0\), the zero-initial-condition interior field with a prescribed boundary voltage vector \(u\) obeys \((A+sC)z=-L_{IB}u\). The boundary current is

\[
\boxed{\Lambda_G(s)=L_{BB}-L_{BI}(A+sC)^{-1}L_{IB}.}\tag{DB1}
\]

This is the dynamic Dirichlet-to-Neumann (DtN) or Schur-boundary response. The graph and capacitors are the declared source; the observer receives only \(\Lambda_G(s)\), not \(G\). A full matrix is an ideal exact boundary experiment consisting of a spanning family of voltage excitations. No source label alone authenticates physical data.

## DB2. Exact STATIC Y–Δ obstruction: two geometries, one boundary law (CLASSICAL / PROVED LOCAL)

A 3-arm interior star with conductances \(g_1,g_2,g_3>0\), \(G=g_1+g_2+g_3\), has

\[
\Lambda_Y(0)=\operatorname{diag}(g_1,g_2,g_3)-\frac{gg^T}{G}.
\]

The all-boundary triangle with edges of conductance \(u_{ij}=g_i g_j/G\) has **exactly** the same boundary matrix. Thus no sequence of static boundary voltage-current experiments identifies which topology is physically present. This is the classical star-mesh equivalence; see Curtis–Ingerman–Morrow, *Circular planar graphs and resistor networks*, Linear Algebra Appl. 283 (1998): https://doi.org/10.1016/S0024-3795(98)10087-3.

Conversely, when the observed \(\Lambda(0)\) is a symmetric, zero-row-sum, positive complete-triangle response, put \(a=-\Lambda_{12}>0\), \(b=-\Lambda_{13}>0\), \(c=-\Lambda_{23}>0\). The unique **positive star-arm triple within that candidate class** is

\[
\boxed{g_1=a+b+ab/c,\quad g_2=a+c+ac/b,\quad g_3=b+c+bc/a.}\tag{DB2}
\]

*Proof:* since \(u_{12}=g_1g_2/G\), \(u_{13}=g_1g_3/G\) and \(u_{23}=g_2g_3/G\), \(ab/c=g_1^2/G\). Therefore \(a+b+ab/c=g_1(g_2+g_3+g_1)/G=g_1\); similarly for the other arms. The formula reconstructs arms from shadow data without reconstructing the true hidden topology.

**Actual source readout in the experiment:**

\[
\Lambda(0)=\begin{pmatrix}8/5&-3/5&-1\\-3/5&21/10&-3/2\\-1&-3/2&5/2\end{pmatrix},\quad g=(2,3,5),\;G=10.
\]

Both the triangle with edges \((3/5,1,3/2)\) and a star with arms \((2,3,5)\) are reconstructed. E cannot pick a true topology from those observations. The failed categorical square is **an exact nonfaithfulness witness for the static boundary observation functor**.

## DB3. The dynamic source law repairs static observational insufficiency (CLASSICAL)

For the star with one capacitive central node \(c>0\),

\[
\boxed{\Lambda_Y(s)=\operatorname{diag}(g)-\frac{gg^T}{G+cs}.}\tag{DB3}
\]

The pure resistor triangle has \(\Lambda_\Delta(s)=\Lambda_\Delta(0)\). They agree at \(s=0\) but differ for every \(s>0\). Their difference for a star is rank-one positive semidefinite. The *new physical structure* is a justified time-dependent storage response, **not** a historical necessity forced by static data alone. Adding an irrelevant or prohibited imaginary probe would not qualify as a repair.

## DB4. A stronger source model defeats the first dynamic repair (PROVED LOCAL)

The simulator's hidden network has three boundary vertices joined to a central hidden node \(h_0\) by \(g=(2,3,5)\), and one *pendant* hidden node \(h_1\) connected to \(h_0\) by \(h=4\). The two nodes have positive capacitors \(c_0=2\), \(c_1=3\). The interior matrices are

\[
A=\begin{pmatrix}14&-4\\-4&4\end{pmatrix},\quad C=\operatorname{diag}(2,3),
\qquad L_{IB}=\begin{pmatrix}-2&-3&-5\\0&0&0\end{pmatrix}.
\]

Eliminating the pendant analytically yields

\[
\boxed{\Lambda_\text{true}(s)=\operatorname{diag}(g)-gg^T h(s),\qquad
h(s)=\frac1{G+c_0s+\frac{hc_1s}{h+c_1s}}.}\tag{DB4}
\]

Notice that the pendant is invisible at \(s=0\) (its DC potential equilibrates with the center), but not dynamically invisible.

At \(s=0\) the triangle, one-mode star and serial graph coincide. At \(s=1\), E rejects the triangle but can calibrate a spurious one-mode star: \(c_{\mathrm{eff}}=26/7\) gives exactly the same response at \(s=0,1\). At \(s=2\) the responses diverge. Thus **one new kind of observation initially repairs insufficiency without fully repairing the model class**. This is a falsification, not a failing test.

## DB5. The finite-observation *reciprocal curvature* invariant (PROVED LOCAL; general classical Stieltjes)

Let \(h(s)=(g_i-\Lambda_{ii}(s))/g_i^2\), defined from the original source response and the DC-reconstructed arms. Define \(q(s)=1/h(s)\). For our serial network,

\[
q(s)=G+c_0s+\frac{hc_1s}{h+c_1s},\quad
q(0)=10,\;q(1)=96/7,\;q(2)=82/5.
\]

Consequently E can compute from **three finite shadows**

\[
\boxed{q(2)-2q(1)+q(0)=-36/35<0.}\tag{DB5}
\]

For every 1-mode capacitive star, \(q(s)=G+cs\) is affine, so the same defect is identically zero. The negative defect therefore falsifies **every** one-mode star sharing the source-derived arms, not just one hand-picked alternative.

This extends beyond a star. For any positive finite RC network with strictly positive interior \(C\), let \(K=L_{IB}\), \(D=C^{-1/2}AC^{-1/2}>0\), \(w=C^{-1/2}K e_i\). By the finite spectral theorem,

\[
h_i(s)=e_i^TK^T(A+sC)^{-1}Ke_i=\sum_j \frac{w_j^2}{s+\lambda_j},\quad\lambda_j>0.
\]

For a nonzero port coupling, \(q_i=1/h_i\) satisfies

\[
q_i''(s)=\frac{2(h_i')^2-h_i h_i''}{h_i^3}\le0
\]

by the weighted Cauchy–Schwarz inequality. Equality on an interval occurs precisely when all **visible** eigenvalues have one common value. Therefore **strictly negative three-point curvature proves at least two distinct observable relaxation rates** in the declared passive linear dynamic class. Note: for arbitrary graphs use \(h_i(s)=(L_{BB}-\Lambda(s))_{ii}\); the division by \(g_i^2\) above is merely a star-specific normalization.

Interval robustness: if each measured \(q(0),q(1),q(2)\) has a certified error interval of radius \(\epsilon\), then the defect lies in \([-36/35-4\epsilon,-36/35+4\epsilon]\). The sign remains certified for \(\epsilon<9/35\). A wider interval is `INCONCLUSIVE`, never a false theorem. Bounds on q are assumed; raw voltage/current noise would need propagated interval arithmetic.

## DB6. Four FINITE shadows uniquely reconstruct the serial model IN ITS CLASS (PROVED LOCAL)

Within the declared restricted topology: exactly three star arms reconstructed from DC, one central storage node with capacity \(c_0>0\), and one connected pendant with link \(h>0\) and capacity \(c_1>0\), **the four response matrices at \(s=0,1,2,3\) determine all three hidden parameters uniquely**. No infinite-moment oracle is needed.

Given \(q(s)\), set

\[
r_j=\frac{q(j)-G}{j}=c_0+\frac{c_1}{1+jt},\qquad t=\frac{c_1}{h}>0,\quad j=1,2,3.
\]

Define \(d_1=r_1-r_2\), \(d_2=r_2-r_3\), and \(R=d_1/d_2\). Then

\[
\boxed{R=\frac{1+3t}{1+t},\quad t=\frac{R-1}{3-R},\quad
c_1=d_1\frac{(1+t)(1+2t)}{t},\quad h=\frac{c_1}{t},\quad
c_0=r_1-\frac{c_1}{1+t}.}\tag{DB6}
\]

All divisions are legitimate for a true positive serial model: \(d_1,d_2>0\), \(1<R<3\), \(t,c_0,c_1,h>0\). This yields a deterministic rational inverse, followed by an **independent exact forward-response verification for all four matrices**. In the source experiment, \(R=13/7\), \(t=3/4\), and E reconstructs \((c_0,h,c_1)=(2,4,3)\). The graph reconstructed from the four matrices agrees with held-out \(s=4,11,17\), which were not part of parameter selection.

**Proof of uniqueness:** the algebra above is reversible and determines \((t,c_1,h,c_0)\) in this declared positive family. There are no additional free parameters. It DOES NOT show the true physical network is a serial network rather than an externally indistinguishable different circuit.

### Actual E-tower evidence protocol

- At E0, acquire source/basis/epoch-tagged \(\Lambda(0)\), synthesize the Y and Δ geometries from a linear circuit law.
- At E1, receive lawful \(\Lambda(1)\), eliminate the triangle, fit one-mode capacity \(26/7\).
- At E2, receive \(\Lambda(2)\), compute the strict inverse-curvature defect, eliminate the remaining 1-mode candidate.
- At E3, receive \(\Lambda(3)\); solve DB6 to **construct**, not retrieve, a serial graph.
- Independently check the forward equations and held-out \(s=4,11,17\), plus three high-frequency coefficients. The latter are NOT fed into the four-sample reconstruction.
- Mixed source IDs, epochs, measurement bases, impossible matrices, wrong capacitances or negative conductances fail rather than silently merge.

## DB7. A separate Hankel-rank source invariant (CLASSICAL / PROVED LOCAL)

When all interior capacities are strictly positive, the high-frequency expansion of \(L_{BB}-\Lambda(s)\) has rational Markov matrices

\[
M_k=K^TC^{-1}(AC^{-1})^kK = W^T D^k W,
\qquad W=C^{-1/2}K,
\quad D=C^{-1/2}AC^{-1/2}.
\]

The block-Hankel matrix \(\mathcal H_r=[M_{i+j}]_{0\le i,j<r}\) is a **Gram matrix**, because its blocks are \((D^i W)^T(D^j W)\). Hence it is PSD and

\[
\boxed{\operatorname{rank}\mathcal H_r\le\text{number of interior storage states},}
\]

with eventual rank equal to the **minimal observable/reachable linear realization dimension**. This is established Ho–Kalman realization theory, not a new spectral theorem: https://doi.org/10.1016/S0377-0427(00)00341-1.

For the serial graph and one normalized port,

\[
(m_0,m_1,m_2)=\left(\frac12,\frac72,\frac{155}{6}\right),\qquad
\boxed{m_0m_2-m_1^2=\frac23>0.}\tag{DB7}
\]

The general two-node serial formula is \(m_0m_2-m_1^2=h^2/(c_0^3c_1)>0\). That certifies two observable dynamic dimensions. The scalar moments are an independent mathematical audit of the **finite-sample** repair, not prerequisites fed to E's reconstruction.

## DB8. The hardest no-go: perfect ALL-FREQUENCY data may not determine ontology (PROVED LOCAL)

Take a 1-hidden-node star with arms \(g\) and capacity \(c\). Construct a different network with TWO nonadjacent hidden hubs, each connected to every boundary vertex with conductance \(g_i/2\), and capacity \(c/2\) per hub. Its Schur complement is

\[
\Lambda_{\text{twin}}(s)=\operatorname{diag}(g)
-2\frac{(g/2)(g/2)^T}{(G+sc)/2}
=\operatorname{diag}(g)-\frac{gg^T}{G+sc}
=\Lambda_{\text{star}}(s)
\]

**for every Laplace parameter \(s\ge0\)**. The twin has two physical interior vertices, yet the Hankel rank is only one. Its antisymmetric hidden mode is invisible to every boundary current readout in the declared experiment. No further data from the SAME observation interface can prove which topology is actual.

The right invariant is *minimal observable dynamical dimension*, not literal interior-node count. Repairing the remaining ontology claim requires a new instrument, a justified geometrical restriction, or intervention that breaks the equivalence. This is source-relative observational darkness, even after an ideal all-frequency record.

## DB9. Partial proof-support transport under SOURCE CHANGE (PROVED LOCAL)

Let an intervention change only interior capacitances \(C\to C'\), leaving conductance graph \(L\) fixed and both systems passive. Then

\[
\boxed{\Lambda_{C'}(0)=\Lambda_C(0),}\tag{DB9}
\]

since \(sC\) vanishes at static \(s=0\). But in general \(\Lambda_{C'}(s)\ne\Lambda_C(s)\) for \(s>0\). Thus all DC proofs transport through this source-changing intervention, while claims inferred from dynamic data must be revalidated on the new epoch. This is a **concrete selective commuting-square theorem**: one lawful environmental change preserves an observation subfunctor without preserving the complete observation functor.

## DB10. Dynamic passivity supplies universal inequality certificates (CLASSICAL)

For \(A>0,C\ge0\) and \(s\ge0\), write \(R_s=(A+sC)^{-1}\). Then

\[
\Lambda'(s)=K^TR_s C R_sK\succeq0,
\qquad
\Lambda''(s)=-2K^TR_s C R_s C R_s K\preceq0.
\]

The second term is negative semidefinite since \(R_s C R_s C R_s\) is PSD: it equals \(R_s^{1/2}(R_s^{1/2} C R_s^{1/2})^2 R_s^{1/2}\). Thus exact finite differences of \(\Lambda(s)\) across increasing equally spaced rates satisfy Loewner monotonicity/concavity. The implementation checks this on 100 separately generated positive rational networks and 4 independent boundary directions each, but tests are not the universal proof. Violations would falsify the declared passive source law or the measurement record; one must NOT infer the source geometry automatically.

## Obstruction-to-repair receipts and SUCC classification

| SUCC failure | Explicit measurement/witness | Exact repair or limitation |
|---|---|---|
| Static model nonfaithfulness | \(\Lambda_Y(0)=\Lambda_\Delta(0)\) | Add a lawful time-dependent boundary response |
| One-pole insufficient | \(q(2)-2q(1)+q(0)=-36/35\) | Admit \(\ge2\) visible relaxation rates |
| Source-compatible inverse construction | \(q(0),q(1),q(2),q(3)\) with \(R=13/7\) | Reconstruct \(c_0,h,c_1\) within serial topology |
| Proof closure under new causal evidence | Distinct observer reports at s=0,1,2,3 | Typed finite E reconstruction; no universal checkpoint |
| Literal hidden topology identification | Star vs twin equality at **all** s | Dark under same interface; require new intervention |
| Source-changing carrier | Capacitor mutation preserves DC but alters dynamic response | Transport only static proof support |
| Measurements with bounded noise | \(\Delta q\) interval excluding 0 | Robust sign proof; otherwise INCONCLUSIVE |

## Falsification and replication

Files: `observational_succ/dynamic_boundary_inverse.py`, `tests/test_dynamic_boundary_inverse.py`, `scripts/dynamic_boundary_inverse_probe.py`, `research/2026-10-12/DYNAMIC_BOUNDARY_INVERSE_RECEIPT.json`. All exact matrix arithmetic is implemented with Python `fractions.Fraction` and Gauss-Jordan elimination; the tests include **51 named cases** and 240+140+100+100+160=**740 seeded randomized rational instances** with additional independent comparisons, 3 frequency-family holdouts, and forged evidence/negative parameters/epoch controls. Command:

```sh
python -m unittest tests.test_dynamic_boundary_inverse -v
python scripts/dynamic_boundary_inverse_probe.py
```

Run with the full repository package installed; standalone testing uses `python -m unittest discover -s tests -p 'test_*.py'`. The full GitHub CI will run the existing source-provenance and overall test suite automatically, and the new probe independently checks the saved receipt exactly.

### New-to-project versus independent mathematical novelty

- **Known results:** star–mesh equivalence and inverse electrical networks (Curtis/Ingerman/Morrow), Schur complement/Kron reduction, Stieltjes resolvent curvature, Hankel minimal realizations (Kalman/Ho), and passive RC dynamics. No independent scholarly novelty is asserted for DB1–DB10.
- **Concrete SUCC advance:** one complete, source-type-checked pipeline **static nonidentification → dynamic partial repair → falsification → reconstruct new model from four finite observations → fresh predictions → residual all-frequency dark rival**. Unlike a hand-picked successful mapping, the first two repairs can fail while the structured E estimator adapts.
- **Deliberate hard boundary:** the unknown graph is unknown *to E*, not an outstanding open problem in all mathematics; precise passive linear circuit/source class and exact boundary law are declared. Honest observation source, continuous physics, measurement error, finite-time stimulus realization, noise and causal instrument cost require further work. This does **not** construct a universally faithful carrier epistemology.
- **Arithmetic firewall:** graph-Laplacian energy positivity, Stieltjes moment Hankel PSD and even complete passive-system identification have **no established morphism to the full completed Weil/Suzuki form**. Therefore none implies the Riemann hypothesis. The correct arithmetic analog would need authentic prime-power and Γ source laws plus a noncircular identification and positivity theorem.

## Next genuinely discriminating theorems

1. Prove a categorical **obstruction-to-repair theorem** for a functor of *source-law-preserving instrument extensions*, in which an observer category grows as countermodels demand. Classify when the extensions commute with prior proof transport, when they are executable under destructive backaction, and when they change the admissible source class.
2. Formalize the exact DB2, DB5, DB6, DB8 kernels in Lean or another proof assistant, especially the restriction that uniquely reconstructed *parameters* do not imply uniquely reconstructed **ontology**.
3. Replace ideal matrix probes by exact rational interval bounds on finite voltage/current excitations, with legal time windows, noise, resets, and source interventions. Distinguish (i) mathematical counterfactual simulations and (ii) independently attained empirical evidence.
4. Develop an automated **probe-design compiler** that proposes observables separating current candidate models subject to a cost model. Prove limits/complexity, including cases of identical all-frequency observables.
5. Try the exact same E procedure on an independently source-justified arithmetic test-function family. Require a new invariant that survives counterfeit Euler impulses, missing prime/Arch data, virtual-zero alternative completions and all tests in the ledger; avoid reading zeros. A proof about analytic observation *identifiability* is not yet the positive completed Weil theorem.

## Core insight

**A failed commuting loop can distinguish a law defect from an observer defect.** The static loop closes perfectly for two different networks; that *success* measures nonfaithfulness. A dynamic loop that fails measures a hidden relaxation mode, whose spectral moments predict a new observable invariant. Even after the reconstructed loop closes, the twin-hub countermodel proves that some underlying carrier distinctions lie outside its observational signature.

This is a strong case where our precise understanding of a failed representation *generates the next mathematical object to construct*, while also proving exactly what remains inaccessible.
