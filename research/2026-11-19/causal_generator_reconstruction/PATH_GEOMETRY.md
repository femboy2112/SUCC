# Forward path comparisons, phase reconstruction, and Jacobian path sums

**Date:** 2026-11-19. **Authority:** self-contained paper proofs with exact finite
controls. All theorem labels below are local to this document. The matrix and
graph identities are classical; the contribution here is their explicit
forward-access, anchored-frame, reconstruction, and precision contract for the
proposed causal-generator program. No academic priority is claimed.

## 1. What is being reconstructed

A finite directed graph, its individual edge weights, a minimal input/output
realization, and a scalar closed-walk generating function are different objects.
The precise observations needed to identify one need not identify the others.

This note proves two complementary results. On a **known, individually
addressable graph**, a finite collection of forward path comparisons identifies
all edge phases up to vertex gauge. Given a **known sequence of Jacobians**,
matrix composition is exactly the sum of its tangent-response paths, with
explicit covariance under moving frames. Neither hypothesis certifies an
unobserved graph topology or an unrestricted nonlinear source law.

The inherited SUCC foundations already supply the following pieces:

| Ancestor | Established component retained here |
|---|---|
| [Graph quantum semantics](../../2026-11-13/yang_mills_succ/qm_graph_bridge/GRAPH_QM_SEMANTICS.md), GQ-1--3 | Finite layered complex path sums equal matrix composition; composition, tensor, dagger, and the semantics quotient are explicit. |
| [Operational triangle](../../../docs/OPERATIONAL_TRIANGLE.md), TG-01--03 | Linear observation commutes with retained-source path summation; nonlinear observation and forgetting the posterior can fail. |
| [Edge carrier reconstruction](../../../observational_succ/edge_carrier_reconstruction.py) | A directed ray and a one-vertex loop have different completions; formal arrow inversion does not authenticate reverse physical time. |
| [Spectral boundary rigidity](../../../docs/CLAIM_SUPPLEMENT_SPECTRAL_BOUNDARY_KRYLOV.md), SBK-02--04 | Boundary realization needs a declared degree/model bound; dark modes and delayed hidden structure obstruct full-carrier reconstruction. |
| [Signed pushforward obstruction](../../../docs/CLAIM_SUPPLEMENT_SIGNED_PUSHFORWARD_OBSTRUCTION.md), SK2-E | Forcing-universal BBP path-coherence identities add no new rank beyond the authenticated step equations; the anchor supplies a separate constraint. |
| [Main XXVI observer transport](../../../docs/MAIN_XXVI_OBSERVER_TRANSPORT.md) | Signed one-step defects telescope; contraction and a summable weighting give explicit completed-operator error bounds. |

The new phase theorem does not evade SK2-E by relabeling the BBP step equations
as independently observed holonomies. Its edge phases are independent unknowns
only in the declared graph experiment.

## 2. A cycle can be compared without walking backward

Let $G=(V,E)$ be a finite directed multigraph with a root $r$, and suppose
every vertex is reachable from $r$. Edges have distinct action labels;
parallel edges remain distinct instruments. Choose a directed spanning
out-arborescence $T$. For each vertex $v$, let $P_v$ be its unique
forward tree path from $r$. Write $d(v)=|P_v|$.

An unknown phase connection assigns $g_e\in U(1)$ to every edge. The
transport of a forward path $P=e_1\cdots e_k$ is
$g(P)=g_{e_k}\cdots g_{e_1}$; scalars commute but the path order and endpoints
are retained. Set $t_v=g(P_v)$, with $t_r=1$.

The experiment must supply coherent comparison of the two forward paths

$$
P_u e,\qquad P_v,\qquad e:u\longrightarrow v.
$$

Both end at $v$. Their relative phase is

$$
H_e=t_v^{-1}g_e t_u. \tag{PG-1}
$$

For a tree edge, $H_e=1$. For a chord, this is the phase associated with its
fundamental cycle. The inverse in (PG-1) is algebra on two acquired reports. It
does **not** ask the observer to execute $P_v$ backward.

This protocol requires either reproducible preparations and forward replay, or
retained reports with a calibrated phase reference and a valid source matching
rule. If path durations differ, the waiting/reference evolution must be included
in that rule. A single uncontrolled trajectory is not automatically such an
instrument. In a time-layered graph, two paths ending at the same spacetime
vertex need no additional timing correction once both coherently referenced
reports are available. A spatial compressed graph additionally needs the stated
time/reference calibration.

### PG-01: complete rooted phase reconstruction

**Statement.** Under that access contract, the $\beta=|E|-|V|+1$ complex
phases $H_e$ on the chords identify the entire connection up to vertex gauge.
Precisely, two connections have the same chord data if and only if there exist
$h_v\in U(1)$, with $h_r=1$, such that

$$
g'_e=h_v g_e h_u^{-1}\qquad(e:u\to v). \tag{PG-2}
$$

Every gauge class has a unique representative with all tree-edge phases equal
to one. Its chord phases are exactly the measured $H_e$. Therefore its
transport along every finite directed path, including repeated walks, is
determined in this gauge.

**Proof.** Gauge-transform by $h_v=t_v^{-1}$. The transformed phase is
$t_v^{-1}g_e t_u=H_e$. It equals one on every tree edge by the definition of
$t_v$. Conversely, assign arbitrary phases to the chords and one to the
tree; this is a connection having exactly those chord data. If a rooted gauge
preserves every tree phase, then its value at a child equals its value at the
parent. Induction from $h_r=1$ forces every $h_v=1$. This proves uniqueness.
Applying these normal forms to two connections proves the equivalence. For a
path from $a$ to $b$, factors telescope to

$$
g(P)=t_b\left(\prod_{e\text{ along }P}H_e\right)t_a^{-1}. \tag{PG-3}
$$

The middle factor is completely determined by the chord data. Absolute endpoint
frames require the corresponding $t_a,t_b$ or their declared gauge choice.
No summation over unobserved alternatives has been used. $\square$

**Causal diamond example.** Edges $r\to a,r\to b,a\to v,b\to v$ form a
directed acyclic graph. Select the first three as the tree. The single chord
datum is $g(r\to b\to v)/g(r\to a\to v)$. The underlying graph has one
cycle even though no directed cycle, and no reverse-time traversal, exists.
This is the elementary model of two causal histories agreeing at a present
rendezvous event.

### PG-02: exact scope of the word “minimal”

The quotient of the connections in PG-01 by rooted vertex gauge is exactly
$U(1)^\beta$, by the explicit normal form. Each chord coordinate can vary
while every other chord coordinate remains fixed. Thus omitting any one of
these $\beta$ comparisons destroys injectivity within this experiment.

More generally, any differentiable, locally differentiably invertible
reconstruction from $k$ scalar phase measurements to an open part of this
quotient requires $k\ge\beta$: in local angular coordinates, the derivative
of a left inverse times the measurement derivative is the $\beta$-dimensional
identity, so the measurement derivative has rank $\beta\le k$. This lower
bound counts real phase coordinates, not arbitrary real-valued encodings with
discontinuous decoders, arbitrary vector instruments, or arbitrary quantum
queries. A pair of real quadratures implements one unit complex phase datum.

The count $\beta$ is the number of independent comparisons, **not** the
number of physical edge traversals. Fresh execution of both paths for each chord
uses

$$
C_T=\sum_{e:u\to v,\ e\notin T}\bigl(d(u)+1+d(v)\bigr) \tag{PG-4}
$$

edge traversals, in addition to preparation and phase-reference costs. Retained
tree reports may lower this cost under an explicit memory/replay contract.
Choosing a different tree changes latency and measurement error while preserving
$\beta$. Minimal probe count therefore does not settle optimal experiment cost.

**Failure receipts.** If the root cannot reach a vertex, a phase on an incoming
edge from that vertex need not occur in any available root path. If only one
unrepeatable route is available, a chord not traversed can be changed without
changing any acquired record. If a connection is supplied only through its
matrix entry sums, two labelled parallel edges with phases $(1,i)$ cannot
be separated from $(i,1)$: both sums are $1+i$. These connections are not
vertex-gauge equivalent, because a common endpoint gauge ratio would have to
equal both $i$ and $-i$. Edge-labelled access is essential.

**Classical provenance.** Gauge classes of graph connections are characterized
by holonomy; see Golénia--Truc, Proposition 2.1 [P1]. PG-01 gives the elementary
finite proof and spells out the forward-path instrument needed for this project.

## 3. Precision is paid as paths become long

### PG-03: phase error and path-length cost

Suppose the true and reconstructed normal forms have unit chord phases
$H_e,\widehat H_e$, with
$|\widehat H_e-H_e|\le\epsilon_e$. For every forward path $P$, let
$m_e(P)$ count its traversals of chord $e$. Then

$$
\left|\prod_{e\in P}\widehat H_e-\prod_{e\in P}H_e\right|
\le\sum_{e\notin T}m_e(P)\epsilon_e. \tag{PG-5}
$$

**Proof.** Replace the factors one at a time. Every remaining factor has modulus
one, so the modulus of each replacement term is exactly the error of that
factor. The triangle inequality gives (PG-5). $\square$

If each edge additionally has a known positive modulus $a_e$, the path weight
error is bounded by the right side times $\prod_{e\in P}a_e$. Summing over
all paths then charges their absolute weights. Relative phase information does
not reconstruct unknown moduli for free.

For a stationary weighted adjacency matrix with
$A_{vu}=\sum_{e:u\to v}a_eH_e$, put
$M=\max_v\sum_{e:u\to v}a_e$. If all chord errors are at most $\epsilon$,
then in the matrix infinity norm

$$
\|A-\widehat A\|_\infty\le M\epsilon,\qquad
\|A\|_\infty,\|\widehat A\|_\infty\le M.
$$

For $|z|M<1$, the resolvent identity and the geometric-series bound give

$$
\|(I-z\widehat A)^{-1}-(I-zA)^{-1}\|_\infty
\le\frac{|z|M\epsilon}{(1-|z|M)^2}. \tag{PG-6}
$$

Indeed the difference is
$(I-z\widehat A)^{-1}z(\widehat A-A)(I-zA)^{-1}$, and both resolvent
norms are at most $(1-|z|M)^{-1}$. This bound controls a damped path sum.
It does not establish a uniform estimate on an undamped boundary.

**Sharp conditioning failure in scale.** For scalars
$A=1-\epsilon$, $\widehat A=1-2\epsilon$, $z=1$, and
$0<\epsilon<1/2$, the operator error is $\epsilon$ while the resolvent
error is $1/(2\epsilon)$. A fixed noisy phase/weight measurement cannot be
advertised as a uniformly stable reconstruction arbitrarily close to a pole.
Likewise a small error on a repeated loop accumulates with its winding count.

## 4. Jacobians compile paths of first variations

Let $F_t$ be differentiable maps between open subsets of finite-dimensional
real spaces, or complex-differentiable maps between complex spaces. A merely
real-differentiable complex map is instead represented in doubled real
coordinates. Fix an actual trajectory
$x_{t+1}=F_t(x_t)$, and write $J_t=DF_t(x_t)$. For a fixed finite horizon
$N$, chain-rule composition gives

$$
D(F_{N-1}\circ\cdots\circ F_0)(x_0)=J_{N-1}\cdots J_0.
$$

### PG-04: exact tangent path sum and moving-frame covariance

For component indices $i_0=a,i_N=b$,

$$
(J_{N-1}\cdots J_0)_{ba}
=\sum_{i_1,\ldots,i_{N-1}}
\prod_{t=0}^{N-1}(J_t)_{i_{t+1},i_t}. \tag{PG-7}
$$

For invertible local chart derivatives $B_t$, define
$K_t=B_{t+1}J_tB_t^{-1}$. Then

$$
K_{N-1}\cdots K_0=B_N(J_{N-1}\cdots J_0)B_0^{-1}. \tag{PG-8}
$$

If an initial perturbation transforms by $v'_0=B_0v_0$ and a final covector
by $\ell'_N=\ell_NB_N^{-1}$, the observed response is invariant:

$$
\ell'_N K_{N-1}\cdots K_0v'_0
=\ell_NJ_{N-1}\cdots J_0v_0. \tag{PG-9}
$$

**Proof.** (PG-7) is the distributive expansion of matrix multiplication; every
term is a forward path through the time-layered component graph. This is the
inherited GQ-1 identity specialized to a derivative. In (PG-8), every adjacent
$B_t^{-1}B_t$ cancels, with the displayed order retained. Substitution of the
two endpoint transformations proves (PG-9). $\square$

The internal graph need not be invariant under a general change of basis:
matrix sparsity and individual path contributions can change. The total
anchored response is the invariant. Vertex phase gauge in PG-01 is a narrower
diagonal transformation than the general similarity ambiguity of realization
theory; they must not be conflated.

**Scope and failure receipts.** A Jacobian describes first variations along the
specified trajectory. It determines full finite displacements for affine maps
when their offsets and anchors are also retained. It does not identify a
general nonlinear map: $F(x)=x$ and $G(x)=x+x^2$ agree in value and first
derivative at zero, but disagree at one. Nor does a finite list of
$J_t$ determine all later matrices without an authenticated evolution law.
Observing a passive trajectory does not automatically provide the interventions
needed to measure every Jacobian entry.

A locally stationary display is consistent with (PG-8). Moving chart origins
can absorb motion; the transformation and its affine compensation must remain
in the record. Dropping endpoint frames or the compensation creates a different
observable. The five-channel frame-agreement work in PR #668 is the source-specific
BBP instance, with its original tail and integer lift retained.

## 5. From a stationary diagram to all finite walks and a resolvent

Let $A$ be a fixed finite complex matrix. Its weighted graph uses
$A_{vu}$ for transport from $u$ to $v$. Applying (PG-7) with every
$J_t=A$ proves that $(A^n)_{vu}$ is the sum of all length-$n$ weighted
walks from $u$ to $v$, for every integer $n\ge0$.

### PG-05: the completed path sum

As a formal matrix power series,

$$
\sum_{n\ge0}z^nA^n=(I-zA)^{-1}. \tag{PG-10}
$$

For any submultiplicative matrix norm, such as the induced infinity norm, and
$|z|\|A\|<1$, the equality is also an absolutely norm-convergent analytic
identity. The remainder after degree $L$ has norm at most
$(|z|\|A\|)^{L+1}/(1-|z|\|A\|)$. Multiplication by $I-zA$ gives
identity formally; analytically the same telescoping identity leaves a remainder
$(zA)^{L+1}\to0$. Matrix inversion gives a rational continuation wherever
$\det(I-zA)\ne0$. Continuation outside the original convergence disk is not
an assertion that the original infinite sum converges there. $\square$

This is a rigorous discrete path-sum model of the proposed reconstruction
pipeline. Giscard--Thwaite--Jaksch [P2] develop substantially more general
closed-form matrix-function path resummations. This note uses only the proved
finite-product and resolvent identities.

### PG-06: the closed-walk determinant identity

Over characteristic zero,

$$
Z_A(z):=\exp\left(\sum_{n\ge1}\frac{z^n}{n}\operatorname{tr}(A^n)\right)
=\det(I-zA)^{-1}. \tag{PG-11}
$$

It holds as formal power series and analytically near zero. To prove it, write
the eigenvalues with algebraic multiplicity as $\lambda_1,\ldots,\lambda_d$.
Triangularizing $A$ gives $\operatorname{tr}(A^n)=\sum_j\lambda_j^n$,
including nondiagonalizable matrices. Substitute into the formal series,
use $\sum_{n\ge1}u^n/n=-\log(1-u)$, exponentiate, and multiply the finite
factors. The result is $\prod_j(1-z\lambda_j)^{-1}$. $\square$

For an ordinary directed adjacency matrix, this is the Bowen--Lanford
closed-walk zeta identity; see [P3]. It is not automatically the Ihara
nonbacktracking zeta of an undirected graph, and it is not the Riemann zeta
function. Identifying either would require a separate source map.

For the Fibonacci matrix $A=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)$,
$\det(I-zA)=1-z-z^2$, and the particular boundary response
$e_1^T(I-zA)^{-1}e_1$ also equals $(1-z-z^2)^{-1}$. This equality of a
boundary response and a closed-walk zeta is specific to that example.

### PG-07: a scalar path integral can lose global distinctions

**Equal zeta, unequal anchored response.** For any complex $\lambda$, let

$$
A=\begin{pmatrix}\lambda&0\\0&\lambda\end{pmatrix},\qquad
B=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}.
$$

Both have trace $2\lambda^n$ at every positive power and zeta
$(1-\lambda z)^{-2}$. Yet

$$
e_1^T(I-zA)^{-1}e_2=0,\qquad
e_1^T(I-zB)^{-1}e_2=\frac{z}{(1-\lambda z)^2}.
$$

Thus all scalar closed-walk traces do not recover the anchored operator.

**Equal boundary response, different hidden zeta.** The one-state system
$A_1=(1/2)$ and the two-state system $A_2=\operatorname{diag}(1/2,1/3)$,
observed only from and to the first state, have exactly the same response
$(1-z/2)^{-1}$. Their full zetas differ by $(1-z/3)^{-1}$. The second
mode is invisible at the chosen boundary. This is the elementary direct-sum
instance of the inherited SBK dark-mode obstruction.

**Equal path intensities, different interference.** Two paths of amplitudes
$(1,1)$ and $(1,-1)$ have the same individual intensities, but coherent
sums two and zero. Intensities cannot replace the shared phase reference.

The correct reconstruction object is therefore the **declared target-preserving
response algebra**, with sufficient anchors and source constraints. A single
aggregate need not preserve every global question.

## 6. What is—and is not—Feynman-shaped here

Feynman's 1948 formulation [P4] assigns a complex contribution to a history
using its action and sums the contributions before taking the event probability.
Our finite graph uses a declared algebra of edge amplitudes and exact finite
composition. Its resemblance is operationally precise at that level. A continuum
quantum path integral additionally needs its specified action, measure or
regularization, boundary/state data, and a justified limiting construction.
Feynman diagrams conventionally organize perturbative terms; they are not
individual observed trajectories and are not identified with our graph edges.

PG-01 reconstructs a connection in a known-support model. PG-04 reconstructs
tangent responses from supplied Jacobians. PG-05 completes a stationary finite
operator under its analytic contract. PG-07 shows why each intermediate
compression must be tested against the target. None of these results proves
selected BBP phase cancellation, R0, pi normality, or RH. They provide exact
interfaces and falsifiers for the causal-generator theorem.

## 7. Reproduction and next discriminator

`path_geometry.py` implements rational-turn forward comparisons and reuses
`observational_succ.ym_graph_semantics` for exact matrix/path semantics.
`test_path_geometry.py` includes gauge changes, the forward diamond, growing
loop counts, missing-chord and inaccessible-root controls, noncommuting moving
frames, nonlinear-jet failure, intensity failure, hidden modes, trace/zeta
failure, and the resolvent conditioning family.

Run from the repository root:

```sh
python research/2026-11-19/causal_generator_reconstruction/test_path_geometry.py -v
```

Finite passes check the implementation on the stated cases. The universal
claims rest on the preceding proofs. These controls share the inherited exact
scalar and matrix code; their agreement is not independent physical evidence.
Observed on 2026-11-19: the command above passed all 12 tests.

The next discriminator for a proposed source application is to exhibit the
actual accessible path-comparison family, state its phase-reference and replay
costs, and mutate one claimed independent generator. If the mutation changes
the target while preserving every admitted report, the family is insufficient.
For BBP, a new useful generator must carry information or an inequality beyond
the forcing-universal path syzygies already bounded by SK2-E.

## Primary sources checked

- **[P1]** S. Golénia and F. Truc, *The Magnetic Laplacian Acting on Discrete
  Cusps*, Documenta Mathematica 22 (2017), 1709--1727, Proposition 2.1.
  [Publisher](https://ems.press/journals/dm/articles/8965539),
  [paper](https://emis.de/ft/32551), DOI 10.4171/DM/608.
  Used for classical holonomy/gauge attribution. The forward-access protocol is
  specified and proved here; no arbitrary-unitary equivalence is inferred.
- **[P2]** P.-L. Giscard, S. J. Thwaite and D. Jaksch, *Evaluating Matrix
  Functions by Resummations on Graphs: The Method of Path-Sums*, SIAM Journal on
  Matrix Analysis and Applications 34(2) (2013), 445--469.
  [Publisher](https://epubs.siam.org/doi/abs/10.1137/120862880).
  Used for path-sum literature context, not as a missing source-reconstruction
  premise; the required identities are proved above.
- **[P3]** M. Pollicott, *Dynamical zeta functions and the distribution of
  orbits*, author-hosted research survey, §3.1, Theorem 3.6 and its proof.
  [Author's notes](https://warwick.ac.uk/fac/sci/maths/people/staff/mark_pollicott/p3/zeta-function-survey-final.pdf).
  Used for Bowen--Lanford terminology; (PG-11) is proved for the stated general
  finite weighted-matrix setting without irreducibility assumptions.
- **[P4]** R. P. Feynman, *Space-Time Approach to Non-Relativistic Quantum
  Mechanics*, Reviews of Modern Physics 20 (1948), 367--387.
  [Author archive](https://authors.library.caltech.edu/records/9h858-5hv71),
  DOI 10.1103/RevModPhys.20.367. Used to delimit the physical analogy.
