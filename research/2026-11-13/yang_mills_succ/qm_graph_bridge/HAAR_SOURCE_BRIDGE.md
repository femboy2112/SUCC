# Existing SUCC Haar operators as an exact presentation of a Wilson state

**Date:** 2026-11-13. **Parent:** `3929e30930438881bebcb371646389d9e66bfbde`.
**Status:** classical Hilbert-space facts, source-specific adapter definitions,
paper proofs, and exact finite rational implementations. No priority claim is
made for wavelets, conditional expectation, GNS, or unitary basis transport.

The existing SUCC quantum bridge already contains literal finite quantum
linear algebra: unitary Haar transforms, Hermitian operators, coherent
registers and measurement instruments. The useful next step is to attach
these maps to the **specified Wilson state and its observable representation**.
This note supplies that attachment at fixed finite lattice cutoff. Its
finite-partition limit recovers bounded Wilson observables on that fixed
configuration space. The four-dimensional continuum construction retains its
separate analytic obligations.

Implementation:
[`ym_haar_bridge.py`](../../../../observational_succ/ym_haar_bridge.py).
Tests: [`test_ym_haar_bridge.py`](../../../../tests/test_ym_haar_bridge.py).

## 1. What the existing SUCC maps already prove

The following are inputs inspected at their actual definitions, not new
constructions invented in place of SUCC's existing ones.

| Existing object | Exact map and retained information | Role in this bridge |
|---|---|---|
| [`carry_safe_polyphase.py`](../../../../observational_succ/carry_safe_polyphase.py), `polyphase_coords`, `tensor_unitary` | \(n=q(m-1)+r+1\), with quotient, residue and finite-horizon unhit slots | A basis bijection / finite-prefix isometry, including the controlled carry |
| [Ω–Haar packet](../../../2026-11-10/omega_bbp_operational_completion/OMEGA_HAAR_WAVELET.md), §§2,4 | All 16 inverse-fiber channels, or complete chronological Haar details | An exact change of Hilbert coordinates before any detail is discarded |
| [`omega_quantum.py`](../../../2026-11-10/omega_bbp_operational_completion/quantum_bridge/omega_quantum.py), `haar_analyze`, `haar_synthesize`, `coarse_instrument_isometry` | Orthogonal multiscale Haar; reversible detail retention; a flagged projection instrument | Existing mathematical QM semantics, distinct from low-pass postselection |
| [Intrinsic carrier, T1–T2](../../../2026-11-10/omega_bbp_operational_completion/intrinsic_carrier/PROOFS.md) | Half-line isometries with an explicit initial boundary; chronological 2/3 block commutator | The boundary cannot disappear when those operators are re-presented |
| [`haar_successor_junction.py`](../../../../observational_succ/haar_successor_junction.py), `signed_junction` | Exact high/low digit currents on genuine consecutive starts, including finite stationarity seams | Probability-law diagnostics, not automatically an amplitude unitary or a Wilson law |
| [`zero_anchored_lambda_haar.py`](../../../../observational_succ/zero_anchored_lambda_haar.py) | Typed evaluation of the authentic rational BBP source and recovered seed | Classical constructive source evaluation; the graph/linear semantics adapter is a separate typed map |

### 1.1 Polyphase is a unitary coordinate map, with its boundary stated

On \(\ell^2(\mathbb N_{\ge1})\),

\[
 W_q e_{q(m-1)+r+1}=e_m\otimes e_r,
 \qquad m\ge1,\quad0\le r<q,
\]

is unitary because it maps one complete orthonormal basis bijectively to
another. The successor becomes the actual controlled carry

\[
 (m,r)\mapsto
 \begin{cases}(m,r+1),&r<q-1,\\(m+1,0),&r=q-1.\end{cases}
\]

For a prefix of length \(N\), it is an isometry into
\(\mathbb C^{\lceil N/q\rceil}\otimes\mathbb C^q\), onto only when
\(q\mid N\). The existing `unhit` slots describe its range exactly.
The new adapter uses those existing coordinates and rejects a reverse read
that gives nonzero amplitude to a slot outside the original range.

The intrinsic family \(T_{p,a}=S^aV_p\), with
\(T_{p,a}e_m=e_{pm+a}\), uses a different starting convention. Its
ranges omit \(e_1,\ldots,e_{p-1}\), so its lossless coordinate target is

\[
 \mathbb C^{p-1}\oplus
 (\ell^2(\mathbb N_{\ge1})\otimes\mathbb C^p).
\]

Retaining that boundary gives a unitary relabelling. Dropping it gives a
compression. These are the exact existing SUCC distinctions.

### 1.2 The 16-channel normalization is explicit

The existing inverse-fiber packet uses

\[
 H_m(v)=\frac1{16}\sum_{k=0}^{15}e^{-2\pi imk/16}v_k.
\]

It obeys
\(\sum_m|H_m(v)|^2=\frac1{16}\sum_k|v_k|^2\).
Thus it is isometric when the input fiber carries normalized counting
measure. In standard amplitude coordinates on both sides, the unitary
DFT has output \(4H_m(v)\). This is exactly the factor in the existing
`fiber_parity_overlap`. Multiscale Haar and Walsh–Hadamard are distinct
full transforms, even though a two-entry Haar butterfly is a Hadamard.

## 2. Specify the Wilson state before choosing the wavelet metric

Fix a **finite** lattice graph, compact gauge group \(G\), normalized Haar
measure on every edge, and the specified Wilson coupling \(\beta\). Its
configuration space and probability law are

\[
 X=G^E,\qquad
 d\mu_\beta(U)=Z_\beta^{-1}e^{-\beta S_W(U)}\prod_{e\in E}dU_e,
 \qquad
 S_W(U)=\sum_p\left(1-\frac{\operatorname{Re}\operatorname{Tr}U_p}{d}\right).
\]

The action, density and finite product moments are the actual definitions in
[`PublicWilson.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicWilson.lean).
At fixed finite cutoff, \(X\) is compact, the density is continuous and
strictly positive, and the finite partition function is positive. This is a
specified source, not a freely chosen positive auxiliary state.

The commutative observable algebra acts by multiplication on
\(L^2(X,\mu_\beta)\), with cyclic vector \(\Omega=1\) and

\[
 \omega_\beta(f_1\cdots f_k)
 =\langle1,M_{f_1}\cdots M_{f_k}1\rangle
 =\int_X f_1\cdots f_k\,d\mu_\beta.
\]

This is the GNS realization of the finite Euclidean probability state.
It is not yet the physical Hilbert space obtained by the Yang–Mills
time-reflection quotient. That later construction has its own reflection
form and positive-time test algebra.

For a finite measurable partition \(\mathcal P=\{C_i\}\), omit null
cells and write \(p_i=\mu_\beta(C_i)>0\). A cell-constant function has
values \(f_i\) and squared norm \(\sum_i p_i|f_i|^2\). Normalized indicator
basis vectors are \(1_{C_i}/\sqrt{p_i}\); its ordinary amplitude vector
is \((\sqrt{p_i}f_i)_i\). Therefore the source chooses the Hilbert
metric used by a cellwise Haar transform.

Here **Haar wavelet** names the coarse/detail basis construction. It does
not mean that the interacting Wilson probability law has been replaced by
the unweighted group Haar law. Shared plaquette edges and the Wilson density
generally create dependencies; their probabilities remain in the weights.

## 3. Exact weighted Haar theorem

**HS-01 — PROVED LOCAL specialization of classical weighted wavelets.**
For two positive cell masses \(p,q\), set \(s=p+q\) and

\[
 m=\frac{pf_0+qf_1}{s},\qquad d=f_0-f_1.
\]

Then

\[
 f_0=m+\frac qs d,\qquad f_1=m-\frac ps d,
\]

\[
 \boxed{p|f_0|^2+q|f_1|^2
 =s|m|^2+\frac{pq}{s}|d|^2.}
\]

*Proof.* Substitute the inverse formulas; the cross terms cancel because
\(p(q/s)=q(p/s)\). The coefficient of \(|d|^2\) is
\((pq^2+qp^2)/s^2=pq/s\). ∎

Equivalently, on normalized amplitude coordinates,

\[
 \begin{pmatrix}\sqrt s\,m\\\sqrt{pq/s}\,d\end{pmatrix}
 =\frac1{\sqrt s}
 \begin{pmatrix}\sqrt p&\sqrt q\\\sqrt q&-\sqrt p\end{pmatrix}
 \begin{pmatrix}\sqrt p\,f_0\\\sqrt q\,f_1\end{pmatrix}.
\]

The displayed real matrix is orthogonal and hence a complex unitary.
For equal masses it is the existing Hadamard butterfly. With rational masses
and rational real values, the unnormalized formulas and both diagonal
metrics use exact rational arithmetic; no approximate square roots are
needed to certify the identity.

Apply this split at every node of a finite binary partition tree. Induction
gives a full invertible transform, one root mean and every detail, with
exact Parseval identity. The new module stores coefficients in the existing
coarse-to-fine level order and stores the source leaf masses. Its positive
coefficient metric is derived from those masses. The input number of leaves
is dyadic in this implementation; the paper split also permits arbitrary
finite binary trees after explicitly specifying their shape.

## 4. Transport the observables as well as the state

**HS-02 — PROVED LOCAL, source-preserving operator identity.** For any
unitary Hilbert-coordinate map \(W\) and bounded operators \(A_j\), put

\[
 \Omega'=W\Omega,\qquad A'_j=WA_jW^{-1}.
\]

Then all word expectations are unchanged:

\[
 \langle\Omega',A'_1\cdots A'_k\Omega'\rangle
 =\langle\Omega,A_1\cdots A_k\Omega\rangle.
\]

The proof is cancellation of each consecutive \(W^{-1}W\), followed
by preservation of inner products. Finite coordinate graphs can implement
these exact composition identities; the source state and observable labels
are part of the interpretation, not optional metadata.
For unbounded operators, this statement requires that the displayed products
are defined on the cyclic vector and all relevant domains are transported.

For the rational weighted coordinates \((m,d)\), multiplication by the
two cell values \((x_0,x_1)\) becomes

\[
 \boxed{
 M'_x=
 \begin{pmatrix}
 (px_0+qx_1)/s & pq(x_0-x_1)/s^2\\
 x_0-x_1 & (qx_0+px_1)/s
 \end{pmatrix}.}
\]

This is \(T\operatorname{diag}(x_0,x_1)T^{-1}\), where
\(T(f_0,f_1)=(m,d)\). For real \(x_0,x_1\), it is self-adjoint in the metric
\(\operatorname{diag}(s,pq/s)\). It need not be symmetric in the
unweighted Euclidean metric, because these are not normalized coordinates.
The implementation verifies intertwining and the metric-adjoint identity.

### A source-sensitive finite Wilson control

For a single \(\mathbb Z/2\mathbb Z\) plaquette, write its holonomy as
\(u\in\{+1,-1\}\). The exact normalized Wilson law is

\[
 \mu_\beta(u)=\frac{e^{\beta u}}{2\cosh\beta}
             =\frac{1+tu}{2},\qquad t=\tanh\beta.
\]

For rational \(-1<t<1\), both source masses are rational. This is a
genuine finite compact-group Wilson analogue, not an instance of the
nonabelian simple Lie-group continuum theorem.

For **every** such source, the adapted cyclic vector \((1,1)\) maps
to \((1,0)\). Nevertheless its transformed holonomy multiplication
matrix has top-left entry \(t\), so its expectation remains \(t\).
In particular the \(t=0\) and \(t=3/5\) sources have identical
adapted cyclic-vector coordinates and different observable representations.

**HS-03 — REFUTED shortcut, exact receipt.** Keeping that common vector
while substituting uniform weights or the uniform-source observable matrix
changes the \(t=3/5\) expectation to zero. Equal coordinates after
source-dependent basis changes do not establish equal states on an
authenticated observable algebra. The exact test detects this mutation.

## 5. Retaining, projecting, dephasing and tracing are different maps

Let \(P\) be the orthogonal coarse projection and \(Q=I-P\).
Complete Haar analysis is unitary. The following subsequent operations
have different domains and outputs:

| Operation | Exact map | Consequence |
|---|---|---|
| Keep all Haar coefficients | \(\psi\mapsto W\psi\) | Invertible; full norm and all transported expectations preserved |
| Retain a coherent projection flag | \(V\psi=P\psi\otimes|0\rangle+Q\psi\otimes|1\rangle\) | Isometry; \(V^*V=I\), with recovery on its image |
| Forget that flag | \(\rho\mapsto P\rho P+Q\rho Q\) | Trace-preserving dephasing; off-diagonal coherences are removed |
| Select the coarse flag | \(\rho\mapsto P\rho P\) | Trace-decreasing outcome with probability \(\operatorname{Tr}(P\rho)\) |
| Condition on that outcome | \(P\rho P/\operatorname{Tr}(P\rho)\) | Normalized conditional state; undefined for zero probability and nonlinear in \(\rho\) |

The exact finite control \((f_0,f_1)=(1,-1)\), \(p=q=1\), has
coarse mean zero and detail 2. Its norm squared is 2. Deleting the detail
leaves zero norm and no inverse. This is the same distinction already made
by SUCC's `coarse_instrument_isometry` and postselection functions.

Conditional expectation also fails to preserve products in general:
for a fair two-point \(f=\pm1\) observed only at the single coarse cell,
\(E(f)=0\) but \(E(f^2)=1\). Treating \(E\) as a faithful
algebra homomorphism would erase a real moment. Complete unitary transport
does preserve products, because it transports the multiplication operators.

The existing chronological \(P_2,P_3\) commutator measures disagreement
between two such lossy projections. Its Hermitian \(i[P_2,P_3]\) is
an actual finite QM observable. The exact unprojected source folds still
commute at their common six-step clock. These are compatible statements.

## 6. Recover the full fixed-cutoff Wilson state by a declared partition limit

**HS-04 — CLASSICAL theorem, proof supplied in the present setting.**
Let \((\mathcal P_j)\) be increasing finite measurable partitions whose
generated sigma-algebra is the Borel sigma-algebra modulo \(\mu_\beta\)-null
sets. Let \(P_j f=E_{\mu_\beta}[f\mid\mathcal P_j]\).
For every \(f\in L^2(\mu_\beta)\),

\[
 P_jf\longrightarrow f\quad\text{in }L^2(\mu_\beta).
\]

*Proof.* Each \(P_j\) is the orthogonal projection onto the cell-constant
subspace. These subspaces are increasing, and their union is dense because
the partitions generate the measurable sets modulo null sets. For an
approximation \(g\) in one such subspace, \(P_jg=g\) for all later
\(j\); contractivity gives
\(\|f-P_jf\|\le2\|f-g\|\). Density proves convergence. ∎

The details \(D_j=P_{j+1}-P_j\) are orthogonal projections onto mutually
orthogonal refinement spaces. Thus

\[
 f=P_0f+\sum_{j\ge0}D_jf\quad\text{in }L^2,
 \qquad
 \|f\|_2^2=\|P_0f\|_2^2+\sum_{j\ge0}\|D_jf\|_2^2.
\]

This is a complete weighted wavelet reconstruction of that specified
probability Hilbert space. It is not a physical process performing an
infinite computation in finite time.

There is an explicit finite bound for continuous bounded observables on
the compact finite configuration space. If each partition cell has
diameter at most \(\delta_j\), and
\(\omega_f(\delta)=\sup_{d(x,y)\le\delta}|f(x)-f(y)|\), then

\[
 \|f-P_jf\|_\infty\le\omega_f(\delta_j).
\]

This follows by comparing a point value with its conditional average over
the same cell. For \(k\) observables with \(\|f_i\|_\infty\le M_i\),
telescoping their products, using \(\|P_jf_i\|_\infty\le M_i\), gives

\[
 \left|\int\prod_{i=1}^k f_i\,d\mu_\beta
       -\int\prod_{i=1}^kP_jf_i\,d\mu_\beta\right|
 \le\sum_{i=1}^k\omega_{f_i}(\delta_j)\prod_{\ell\ne i}M_\ell.
\]

For Lipschitz observables, \(\omega_{f_i}(\delta)\le L_i\delta\).
These are bounds on the joint moments of the **same** Wilson state; finite
cell probabilities must be known or separately enclosed. The code certifies
the rational finite-mass case. It does not compute exact arbitrary SU(2)
Wilson cell masses or assume those masses to be rational.

For gauge-invariant target observables, one may instead refine the
gauge-invariant observable sigma-algebra. That recovers the invariant
Hilbert subspace relevant to those observables. An arbitrary finite
partition is not automatically preserved by gauge transformations.

## 7. Transport symmetry and reflection with the Hilbert coordinates

**HS-05 — PROVED LOCAL representation fact.** A unitary coordinate change
preserves a source's symmetry and reflection identities when the operators
and domains are transported with it. If \(U(g)\) is its gauge action,
use \(WU(g)W^{-1}\). If the time-reflection form is
\(q(f,g)=\langle\Theta f,g\rangle\) on a declared positive-time
domain \(\mathcal D_+\), use

\[
 \Theta'=W\Theta W^{-1},\qquad\mathcal D'_+=W\mathcal D_+.
\]

Then \(q'(Wf,Wg)=q(f,g)\). Positivity on that domain is unchanged,
and its nullspace quotient is carried isometrically to the corresponding
transformed quotient. This permits Haar coordinates in a reconstruction
proof; it supplies no missing reflection-positivity hypothesis.

For a **truncated** wavelet space, the needed positive-time support,
reflection compatibility and limit-continuity conditions must still be
checked. An arbitrary spatial or chronological Haar projection need not
preserve them. The upstream committee's
[`ReflectionPositivity.lean`](https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/checks/ReflectionPositivity.lean)
uses exact source-matched reflected entries and support-preserving
approximation. Those are the appropriate interfaces to match.

Likewise \(H'=WHW^{-1}\), on the transported domain
\(D(H')=W D(H)\), has the same spectrum as \(H\). A complete
Haar change of coordinates neither creates nor destroys a mass gap. A
finite compression can change the spectrum, which is why the cutoff and
the omitted details cannot be ignored.

## 8. Verdict, remaining dependency and validation

The direct bridge is now explicit:

\[
 \text{specified Wilson probability state}
 \longrightarrow L^2(\mu_\beta)
 \longrightarrow\text{source-weighted full Haar coordinates}
 \longrightarrow\text{transported observable and reflection representation}.
\]

Every displayed arrow here has a stated map and proof. Existing SUCC
polyphase and quantum-Haar operators already implement the finite coordinate
side. The new work identifies the correct metric and retains the Wilson
state through transformed observables. HS-04 provides a complete
fixed-cutoff reconstruction from an increasing family of finite partitions.

The next Yang–Mills interface is precise: match the construction's regulated
observable algebra, reflection/test domains and common source witnesses to
these coordinates, then transport its proved analytic bounds with explicit
norm constants. Across lattice cutoffs, the moduli of continuity, observable
renormalizations and partition dimensions may change. The fixed-cutoff
moment bound does not assert uniform ultraviolet control, infinite-volume
uniqueness, or a mass gap. No source-selected BBP cancellation follows merely
from this faithful representation.

### Claim ledger

| ID | Statement and status | Receipt / boundary |
|---|---|---|
| HS-01 | **PROVED LOCAL / CLASSICAL:** full weighted Haar split and finite-tree Parseval | Exact inverse formulas, all retained details; rational finite implementation |
| HS-02 | **PROVED LOCAL / CLASSICAL:** transported state and observable words agree | Explicit conjugation; no equality from state coordinates alone |
| HS-03 | **REFUTED shortcut:** source-adapted vacuum vector identifies the source without its representation | Z2 Wilson \(t=0\) versus \(t=3/5\), same vector and different retained moments |
| HS-04 | **PROVED PAPER / CLASSICAL:** generating partitions reconstruct the fixed Wilson state; explicit bounded-observable moment error | Exact source masses and generating/diameter assumptions; no uniform continuum claim |
| HS-05 | **PROVED LOCAL / CLASSICAL:** full unitary transport preserves declared gauge/reflection form and spectrum | Transport operators and support domains; truncation needs separate control |
| HS-06 | **OBSERVED:** existing finite SUCC QM operators and new rational adapter replay successfully | Test counts below; no physical quantum execution or Lean extension claimed |

### Executed checks in this continuation

- New `test_ym_haar_bridge.py`: **10 tests passed**.
- Existing `test_omega_haar.py`: **12 tests passed**.
- Existing `quantum_bridge/test_omega_quantum.py`: **20 tests passed**.
- Existing `test_carry_safe_polyphase.py`: **18 tests passed**.
- Existing `test_haar_successor_junction.py`: **15 tests passed**.
- Existing `test_zero_anchored_lambda_haar.py`: **19 tests passed**.

The quantum test first failed under unconfigured root discovery because its
sibling `omega_haar` module was not on the import path. Its existing
documented command, run inside `quantum_bridge`, passed without code changes:

```sh
PYTHONPATH=.. python -W error -m unittest -v test_omega_quantum.py
```

The other focused root test commands use
`python -m unittest discover -s tests -p '<named test file>' -q`.
The Ω–Haar predecessor uses discovery at its own containing directory.
These are focused finite checks and paper proofs, not a new full upstream
Yang–Mills kernel replay or physical quantum execution.
