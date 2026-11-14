# Liber Secundus — De Causis et Propinquitate

## Scope and provenance

This book gives a finite-dimensional vertical slice of causal observation. It
preserves the proposal in [PR #618's nine-section note](../../research/2026-11-13/causal_relevance_proximity/RESEARCH_NOTE.md): relevance is to be obtained from declared interactions, not read off an independently chosen spatial chart. It does not identify relevance with correlation, require derivatives to exist, or infer a physical spacetime.

Results below are **CLASSICAL CONSEQUENCES / PROVED PAPER**, with their proofs
included. Their organization as a source-relative prediction/geometry interface
is new to this manuscript; academic priority is **UNVERIFIED and not claimed**.
Finite implementation checks are listed in the round validation record, not
substituted for these proofs. The linear layer uses a field, and the minimax and
derivative results additionally use real or complex Hilbert/normed spaces. These
are declared extensions of the set/action kernel, not axioms forced by it.

## 1. Finite contact contrasts precede derivatives

Fix a carrier law, a repeatable preparation/context \(c\), an admissible
intervention label \(u_x=a\), a horizon \(t\), and a real or vector readout. Let

\[
m_{y\leftarrow x}(a;t,c)
=\mathbb E[O_y(t)\mid\operatorname{do}(u_x=a),c].
\]

This is a response law, not an already performed experiment. Its finite contrast
is \(m(a;t,c)-m(b;t,c)\). For deterministic sources the expectation is unnecessary.
For a stochastic source it is an expectation under the intervention-modified
kernel. For a quantum source it can be
\(\operatorname{Tr}(O_y\Phi_{t,c,a}(\rho_c))\), with a specified family of
channels/instruments. These are different implementations of the response law;
they do not identify classical kernels with quantum operations.

**CG-01 (sensitivity transport).** If all finite-dimensional maps in
\(z_{k+1}=F_k(z_k,u_k)\), \(O=h(z_t)\), are differentiable along the declared
trajectory and the intervention changes only \(u_s\), then

\[
D_{u_s}O=Dh(z_t)D_zF_{t-1}\cdots D_zF_{s+1}D_uF_s.
\]

Every factor is evaluated on that trajectory, with the empty product equal to
the identity. **Proof.** The perturbed input first changes \(z_{s+1}\) by
\(D_uF_s\); successive applications of the chain rule multiply by the displayed
state derivatives, and the last application multiplies by \(Dh\). This proves
the formula for every finite \(t>s\). It does not justify interchanging a
derivative with an infinite horizon, expectation, or limit. For
\(z_{k+1}=Az_k+Bu_k\), \(O=Cz_t\), it is \(CA^{t-s-1}B\).

**Countermodels.** \(m(a)=|a|\) is not differentiable at zero. A threshold
\(m(a)=1_{a>0}\) is discontinuous. \(m(a)=a^2\) has derivative zero at zero yet
a nonzero contrast between zero and one. First derivatives at one context do not
reconstruct finite interventions. In the classical common-cause model
\(X=Z,Y=Z\), observing \(X\) predicts \(Y\), but replacing the equation for \(X\)
by \(X=a\) does not change \(Y\). Correlation is not the do-response.

## 2. The exact obstruction to an observed dynamics

Let \(V,W\) be vector spaces over a field, let the linear surjection \(P:V\twoheadrightarrow W\) be
the present readout, and let the linear map \(A:V\to V\) be a source action. Write \(N=\ker P\).
The comparison square asks for a linear \(B:W\to W\) satisfying

\[
PA=BP. \tag{2.1}
\]

**CG-02 (linear action descent).** The following are equivalent:

1. A map \(B\) satisfying (2.1) exists.
2. \(A(N)\subseteq N\).
3. The hidden-response map \(K_A=(PA)|_N:N\to W\) is zero.

When it exists, \(B\) is unique, and all words in descended actions commute with
\(P\). **Proof.** Equation (2.1) gives \(PAz=0\) for \(z\in N\). Conversely,
if this holds, define \(B(Px)=PAx\); replacing \(x\) by \(x+z\), \(z\in N\),
does not change the result. Surjectivity gives the whole domain and uniqueness;
linearity follows by choosing representatives. Applying the identity repeatedly
proves the word assertion. The equivalence of 2 and 3 is the definition of \(N\).

Thus the obstruction is a map, not a scalar mismatch. Its kernel consists of
presently hidden perturbations remaining hidden after one action. Its image is
the set of observable one-step differences produced by hidden perturbations.
Its rank counts independent escaping directions. This is the linear instance of
the existing [BPGS future-safe quotient criterion](../CLAIM_SUPPLEMENT_BOUNDARY_PORT_GEOMETRY.md)
and its [complete source proof, §7](../../research/2026-10-22/BOUNDARY_COMPLETE_GEOMETRY_SELECTION.md).
It is not a renamed new theorem.

**Smallest informative example.** With

\[
P=\begin{pmatrix}1&0\end{pmatrix},\qquad
A=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\]

states \((0,1)\) and \((0,-1)\) have the same present readout and next readouts
\(+1,-1\). Here \(K_A(0,z)=z\). No function of the present readout alone predicts
both next observations. In contrast, \(A=\operatorname{diag}(2,3)\) descends to
\(B=2\), despite completely unresolved second coordinates.

### 2.1 Exact quantitative prediction debt

**CG-03 (optimal hidden-fiber error).** Let \(V,W\) be finite-dimensional real or
complex Hilbert spaces, a linear surjection \(P:V\twoheadrightarrow W\), and let \(F:V\to Z\) be
linear, where \(Z\) is any finite-dimensional normed space. Let \(P^\dagger\)
be the inverse of \(P|_{N^\perp}\) onto \(W\), and let \(\Pi_N\) be the
orthogonal projection onto \(N\). Then

\[
\inf_{g:W\to Z}\ \sup_{\|x\|\le1}\|Fx-g(Px)\|
=\|F|_N\|=\|F\Pi_N\|. \tag{2.2}
\]

The infimum includes arbitrary nonlinear predictors. A linear optimum is
\(g_*(y)=FP^\dagger y\). For a real radius \(r\ge0\), on the fixed prior fiber

\[
\mathcal F(y,r)=\{P^\dagger y+z:z\in N,\ \|z\|\le r\},
\]

the exact minimax error is \(r\|F|_N\|\), attained at the center
\(FP^\dagger y\). If the prior is the unit ball and \(\|P^\dagger y\|\le1\),
its fiber has \(r=(1-\|P^\dagger y\|^2)^{1/2}\).

**Proof.** For any \(\|z\|\le1\) in \(N\), \(+z\) and \(-z\) give the same data.
The triangle inequality gives

\[
2\|Fz\|\le \|Fz-g(0)\|+\|-Fz-g(0)\|.
\]

At least one error is at least \(\|Fz\|\); taking the supremum proves the lower
bound for every \(g\). For the proposed optimum,
\(Fx-g_*(Px)=F\Pi_Nx\), whose norm is at most \(\|F|_N\|\|x\|\).
Projection has norm at most one, and restricting to \(N\) gives equality of the
two operator norms. Translate the same symmetric-pair argument by
\(P^\dagger y\) and scale by \(r\) for the fiber formula. Pythagoras gives the
unit-ball fiber radius. This also covers \(N=0\), \(r=0\), and the zero target.

For one-step prediction take \(F=PA\). In particular,

\[
\inf_{B\in\operatorname{Hom}(W,W)}\|PA-BP\|
=\|K_A\|,
\qquad B_*=PAP^\dagger. \tag{2.3}
\]

For a future target \(C A_wx\), take \(F=CA_w\): its error from the present
readout is exactly \(\|CA_w\Pi_N\|\) on the unit ball. With an unbounded hidden
fiber and \(F|_N\ne0\), every predictor has unbounded worst-case error, by
scaling the symmetric pair. A hidden horizon is therefore target-dependent:
the relevant radius can be zero at the present time and positive later.

This is an elementary optimal-recovery result, not an assertion that arbitrary
nonlinear or non-Hilbert source priors have linear optimal predictors. The
symmetry and norm prior are mathematical information supplied to the observer;
they are not inferred from a finite fit. [Foucart–Liao](https://foucart.github.io/publi/OR_L1Noise_v2.pdf),
§1 and Lemma 2, place the symmetric-pair lower bound in classical
information-based complexity. The proof here is self-contained.

## 3. The smallest linear predictive completion

Let \(V=\mathbb F^n\), with a finite nonempty action alphabet \(\mathcal A\),
linear actions \(A_a\), and a readout matrix \(P\) of rank \(r\). For a word
\(w=a_1\cdots a_k\), define \(A_w=A_{a_k}\cdots A_{a_1}\); the empty word has
identity action. Put

\[
\mathcal V_k=\operatorname{span}_{\mathbb F}
  \{\text{rows of } PA_w:|w|\le k\}\subseteq V^*.
\]

**CG-04 (minimal predictive refinement).** The sequence satisfies

\[
\mathcal V_{k+1}=\mathcal V_k+\sum_{a\in\mathcal A}\mathcal V_k A_a.
\]

It stabilizes by \(k=n-r\). Let \(Q\) be any row-basis matrix of the stable space
\(\mathcal V_\infty\), of dimension \(d\). Then:

1. \(P=LQ\) for a linear \(L\), and for each \(a\) a unique \(B_a\) satisfies
   \(QA_a=B_aQ\).
2. \(\ker Q=\bigcap_w\ker(PA_w)\), the largest subspace of \(\ker P\)
   invariant under every \(A_a\).
3. Every other linear refinement \(R\) satisfying \(P=L'R\) and
   \(RA_a=D_aR\) has \(\mathcal V_\infty\subseteq\operatorname{row}(R)\).
   Consequently \(d-r\) is the minimum number of added independent linear
   readout coordinates needed for exact closure.

**Proof.** Every nonempty word splits as its first letter followed by a shorter
word, giving the recursion. If equality holds at one stage, the row space is
right-invariant under every \(A_a\), so all later stages equal it. Otherwise the
dimension rises by at least one; starting at \(r\), at most \(n-r\) strict
increases are possible. At the stable space, each row of \(QA_a\) is a linear
combination of rows of \(Q\), giving \(B_a\); row independence gives uniqueness.
The formula for the kernel follows by annihilating all spanning rows. If
\(z\in\ker Q\), then \(PA_w A_a z=0\) for all words, so the kernel is invariant.
Any invariant subspace inside \(\ker P\) is annihilated by every \(PA_w\), hence
lies inside \(\ker Q\). Finally, for another refinement,
\(PA_w=L'D_wR\), so all generating rows lie in \(\operatorname{row}(R)\).
This proves both minimality and the dimension claim.

The additional coordinates are not automatically executable observer memory.
They may require unavailable state preparations, destructive interventions, or
future readouts from different copies of the same initial state. CG-04 proves
the smallest sufficient mathematical state representation. Acquiring that
representation is a separate policy/access obligation. For the two-state example
above, \(P\) needs one added coordinate and \(Q=I_2\) works, but that does not make
the hidden second coordinate presently measured.

The bound is sharp for every \(1\le r\le n\): let the rows of \(P\) be
\(e_1^T,\ldots,e_r^T\), and let \(A\) have ones on its superdiagonal and zeros
elsewhere. Then \(\mathcal V_k\) is spanned by the first
\(\min(n,r+k)\) coordinate rows, so exactly one dimension is added at each
step until \(n-r\). Zero readout
\((r=0)\) is already closed; the displayed upper bound remains valid but loose.
CG-04 is the action-family extension of classical observable-subspace/Kalman
constructions, not a claim to have originated them.

## 4. Defects compose with signs and calibrated transport

The precise comparison can change spaces at each stage. Let

\[
A_i:V_{i-1}\to V_i,\quad B_i:W_{i-1}\to W_i,\quad
P_i:V_i\to W_i,
\qquad E_i=P_iA_i-B_iP_{i-1}.
\]

**CG-05 (typed defect telescoping).** For every integer \(m\ge1\),

\[
P_mA_m\cdots A_1-B_m\cdots B_1P_0
=\sum_{i=1}^m B_m\cdots B_{i+1}E_i A_{i-1}\cdots A_1. \tag{4.1}
\]

Empty products are identity maps on the appropriate spaces. For subordinate
operator norms,

\[
\|E_{[1,m]}\|
\le\sum_{i=1}^m
 \left(\prod_{j=i+1}^m\|B_j\|\right)\|E_i\|
 \left(\prod_{j=1}^{i-1}\|A_j\|\right). \tag{4.2}
\]

**Proof.** Substitute \(E_i=P_iA_i-B_iP_{i-1}\) in the sum. Each interior
term cancels with the adjacent term; only its two endpoints remain. The norm
bound follows from the triangle inequality and submultiplicativity. No
commutativity is used. The two-stage form is
\(E_{21}=E_2A_1+B_2E_1\). It is a twisted derivation identity, not by itself a
curvature, phase, or cohomology class.

**Cancellation receipt.** In one-dimensional spaces take every \(P_i=1\),
\(A_1=A_2=1\), \(B_1=B_2=-1\). Then \(E_1=E_2=2\), but the two-stage defect
is zero. A perfect final readout does not certify faithful intermediate
computation. Conversely small step errors need not remain small when the
propagators amplify them; (4.2) keeps this cost explicit.

**CG-06 (coordinate covariance).** For invertible source charts \(S:V\to V'\)
and observed charts \(T:W\to W'\), set

\[
A'=SAS^{-1},\quad P'=TPS^{-1},\quad B'=TBT^{-1}.
\]

Then \(E'=TE S^{-1}\), \(\ker P'=S\ker P\), and
\(K'_{A'}=TK_A(S^{-1}|_{S\ker P})\). **Proof.** Substitute the three formulas
and cancel inverse pairs; restricting the resulting \(P'A'\) to \(S\ker P\)
gives the last formula. Vanishing, rank, and the dimensions of kernels/images
are invariant. Numerical norm sizes are invariant only if the norms/units are
transported with \(S,T\); fixed Euclidean coordinate norms do not have this
invariance. Under transported Hilbert structures, the pseudoinverse and
orthogonal projector in CG-03 transport accordingly.

### 4.1 Nonlinear descent requires whole fibers

For arbitrary maps \(q:X\to Y\), \(F:X\to X\), an observed action exists on
\(q(X)\) exactly when \(qF\) is constant on every \(q\)-fiber. The same
representative argument as CG-02 proves this set-level statement.

**CG-07 (differential criterion with a global hypothesis).** Suppose
\(U\subseteq\mathbb R^n\) is open, every nonempty fiber of a linear map \(P\)
intersected with \(U\) is convex, and \(F:U\to\mathbb R^n\) is \(C^1\).
Then \(PF\) factors as a map \(P(U)\to P(\mathbb R^n)\) through \(P|_U\) if and only if

\[
P\,DF_xz=0\quad\text{for every }x\in U,\ z\in\ker P.
\]

**Proof.** Descent makes \(PF\) constant along every sufficiently short vertical
segment; differentiate. Conversely, join two points in a fiber by its line
segment in \(U\). The derivative of \(PF\) along the segment is zero everywhere;
the fundamental theorem of calculus gives equal endpoints. For an effective selfmap of \(P(U)\), additionally require \(F(U)\subseteq U\).
Piecewise smooth path-connected fibers suffice with the analogous
vertical-tangent condition.

The condition at one baseline is insufficient: \(P(x,z)=x\),
\(F(x,z)=(z^2,0)\) passes the hidden derivative test at \(z=0\) yet does not
descend. Fiber connectedness also matters for a nonlinear readout: on
\(X=\mathbb R\setminus\{0\}\), \(q(x)=x^2\), \(F(x)=e^x\), every tangent kernel
of \(Dq\) is zero, but \(qF(1)=e^2\ne e^{-2}=qF(-1)\). Tangent tests cannot
compare disconnected representatives of one observation.

## 5. Three geometries with different meanings

### 5.1 Relative influence order

Given calibrated intervention contrasts or derivatives, a nonnegative score
\(R_y(x)\) produces a target-relative total preorder
\(x\succeq_y z\iff R_y(x)\ge R_y(z)\). Reflexivity and transitivity follow from
the order on real numbers. Ties need not identify source nodes. This is a valid
weak form of “closer means relatively more relevant,” but it is not a distance
between pairs of states, is generally not symmetric in source and target, and
does not force an embedding or a unique scale.

### 5.2 Geometry of distinguishable behavior

For a common admissible experiment family \(\mathcal E\), give each response
space a bounded metric \(\delta_e\le1\), and let \(f_e:X\to Y_e\) be its exact
response law (a distribution may be such a response). Define

\[
d_{\mathcal E}(x,x')=\sup_{e\in\mathcal E}
  \delta_e(f_e(x),f_e(x')).
\]

For an empty instrument family use the convention \(d_{\varnothing}=0\).

**CG-08 (behavior pseudometric).** This is a pseudometric; its zero relation is
equality of all declared response laws. It becomes a metric on that quotient.
Adding instruments can only increase \(d_{\mathcal E}\) and refine its zero
classes. **Proof.** Each pulled-back metric has symmetry, zero diagonal, and
the triangle inequality. Taking suprema preserves the latter because
\(\sup_e(a_e+b_e)\le\sup_ea_e+\sup_eb_e\). Zero distance forces every
nonnegative summand to vanish. The remaining assertions follow directly.

This measures experimental distinguishability, not causal influence between
nodes. If \(\mathcal E=(e_1,e_2,\ldots)\) is countable, the weighted sum
\(\sum_j2^{-j}\delta_{e_j}(f_{e_j}(x),f_{e_j}(x'))\) is another pseudometric
with the same zero relation and generates the initial topology of those maps.
To verify the topology claim, control a finite initial sum by finitely many
coordinate neighborhoods and the tail by \(\sum_{j>J}2^{-j}\); conversely every
single coordinate discrepancy is bounded by \(2^j\) times the sum. The supremum
topology can be strictly finer. No topology or metric is intrinsic until the
experiments and response metrics have been declared.

### 5.3 Geometry of composable cost

For a directed graph of lawful elementary transitions with declared
nonnegative edge costs, the infimum of summed path costs is an extended directed
pseudometric: empty paths give zero, and concatenation proves the triangle
inequality by approximating each infimum. In a finite graph with strictly
positive edge costs, distinct reachable vertices have positive distance;
unreachable pairs have distance \(+\infty\). Symmetric undirected positive
costs on a connected finite graph give a metric. This is the classical
Lawvere-enriched viewpoint ([Lawvere 1973, official reprint metadata](https://www.tac.mta.ca/tac/reprints/articles/1/tr1abs.html)).

The graph must encode composable transitions, not just endpoint sensitivities.
A decreasing transform of an influence score is an explicit cost convention.
Multiplying every cost by two preserves all shortest paths and relative orders,
while changing every nonzero distance. Hence relevance/order alone cannot fix
an absolute metric scale. The repository already proves stronger topological
nonuniqueness for \(p\)-adic metrics in
[OPIG-N4](../CLAIM_SUPPLEMENT_OBSERVATION_PINNED_GEOMETRY.md).

## 6. When causal latency really equals graph distance

Let \(A\in\mathbb R^{n\times n}\) and put an edge \(x\to y\) exactly when
\(A_{yx}\ne0\). A source perturbation at coordinate \(x\) has response
\((A^k)_{yx}\) at \(y\) after \(k\) ticks. This presumes coordinate intervention
and target readout access; it is not inferred from passive observations.

**CG-09 (structural locality and no-cancellation recovery).** For every \(k\ge0\),
the response \((A^k)_{yx}\) is the sum, over length-\(k\) walks from \(x\) to
\(y\), of products of their signed edge weights. Thus no such walk implies zero
response. If all entries of \(A\) are nonnegative, a response is positive if and
only if such a walk exists. Consequently the earliest nonzero response time,
including time zero, equals directed shortest-path length for nonnegative \(A\).

**Proof.** Expand the matrix product entry by entry. Each intermediate index
list is precisely a walk; absent edges have a zero product. In the nonnegative
case a nonzero walk product is positive, and a sum of positive terms cannot
cancel. Minimizing the permissible length gives the final conclusion.

**Signed counterexample.** In node order \((x,a,b,y)\), let the only nonzero edges
be \(x\to a=1\), \(x\to b=1\), \(a\to y=1\), \(b\to y=-1\). There are two
length-two structural paths but \((A^2)_{yx}=1-1=0\), and all later responses
also vanish. The earliest-response relation is not even transitive:
\(x\to a\) and \(a\to y\) respond in one tick, while \(x\to y\) never responds.
Treating these times as a directed metric would demand \(+\infty\le1+1\).

An intervention clamping the \(b\)-leg to zero reveals the other path, but that
is a new instrument and source context. First-order endpoint response cannot
reconstruct a signed internal graph without such extra access or a
no-cancellation hypothesis. With full state readout and lawful reset/basis
preparations, the \(n\) one-step contrasts from \(0\) to \(e_x\) recover every
column of \(A\). With only readout \(P\), those experiments recover \(PA\);
all matrices \(A+D\) with \(PD=0\) remain indistinguishable to this one-step
bank. Future probes can split that class, precisely as CG-04 specifies.

The implication “large influence means short graph distance” also fails with
nonnegative weights: a direct edge of weight \(1/100\) can be weaker than a
two-edge chain with weights \((1,1)\). CG-09 certifies support and earliest time,
not an unsupported monotone ordering of amplitudes by distance.

## 7. Acquiring predictive coordinates on one actual schedule

CG-04 constructs a sufficient representation from all mathematical action
words. The following criterion tests whether one actual schedule supplies it.
Readouts here are nondestructive; if an instrument updates the carrier, include
its known update in the composed source maps and specify whether the target is
before or after that update. Omitting disturbance invalidates the criterion.

Fix linear actions \(A_{a_1},\ldots,A_{a_t}\) to be performed, with arbitrary
initial state \(x_0\in V\). Put

\[
M_0=I,\qquad M_j=A_{a_j}\cdots A_{a_1},\qquad
H_t=\begin{pmatrix}P\\PM_1\\\vdots\\PM_t\end{pmatrix}.
\]

The exact realized record is \(H_tx_0\). Let \(Q\) be the predictive completion
from CG-04, and set \(F_t=QM_t\); this target is the complete predictive
coordinate of the **current** carrier, not of its initial state.

**CG-10 (actual-schedule acquisition).** The record determines \(F_tx_0\) for
every \(x_0\in V\) if and only if

\[
\ker H_t\subseteq\ker F_t,
\quad\text{equivalently}\quad
\operatorname{row}(F_t)\subseteq\operatorname{row}(H_t).
\tag{7.1}
\]

When (7.1) holds, a linear \(L_t\) exists with \(F_t=L_tH_t\), and every future
action-word response of the current carrier is obtained by evolving
\(L_tH_tx_0\) with the descended actions. If the initial target \(Qx_0\) is
requested instead, replace \(F_t\) by \(Q\); this is a different condition.

**Proof.** Two initial states yield the same record precisely when their
difference lies in \(\ker H_t\). All such differences leave the target unchanged
exactly under the kernel inclusion. In finite dimensions, the annihilator of
\(\ker H_t\) is \(\operatorname{row}(H_t)\), giving the equivalent row condition
and a factor \(L_t\). Alternatively, define \(L_t(H_tx)=F_tx\) on
\(\operatorname{im}H_t\) and extend linearly. The future prediction statement
uses \(P=LQ\) and \(QA_a=B_aQ\) from CG-04. No unseen experiment has been
inserted into the actual record.

**Quantitative form.** In calibrated Hilbert coordinates, let \(H_t^\dagger\)
be the ambient Moore–Penrose inverse: it inverts \(H_t|_{(\ker H_t)^\perp}\)
on \(\operatorname{im}H_t\) and is zero on
\((\operatorname{im}H_t)^\perp\). Thus it also accepts noisy records outside
the image. For the prior
\(\|x_0\|\le1\), CG-03 gives the exact noise-free minimax error

\[
r_t=\|F_t\Pi_{\ker H_t}\|.
\]

If the received record is \(y=H_tx_0+\eta\), with independently justified
\(\|\eta\|\le\epsilon\), the explicit predictor \(F_tH_t^\dagger y\) has error
at most

\[
r_t+\epsilon\|F_tH_t^\dagger\|.
\tag{7.2}
\]

Indeed its error is \(F_t\Pi_{\ker H_t}x_0-F_tH_t^\dagger\eta\), and the
triangle inequality proves (7.2). The true noisy minimax error is at least
\(r_t\), because zero noise is allowed. The sum in (7.2) is a conservative
bound, not an asserted sharp noisy radius.

**Two exact receipts.** Let \(P=[1,0]\), and give the source two available
actions: the coordinate swap \(S\) and \(D=\operatorname{diag}(1,0)\). The
all-action completion has \(Q=I_2\).

1. Perform \(S\). Then \(H_1=I_2\), \(F_1=S\), and the current state is
   \((y_1,y_0)\) from the two actual readouts. No reset is required.
2. Perform \(D\). Then both rows of \(H_1\) are \([1,0]\), while \(F_1=D\).
   The current predictive state \((x_{0,1},0)\) is determined, although the
   initial hidden coordinate \(x_{0,2}\) remains unknown. Erasing hidden
   information can make future prediction sufficient without recovering history.

This supplies a precise access bridge for a prescribed finite experiment. It
does not prove that a suitable schedule exists, is affordable, preserves an
initial target, or can be learned without authenticated action laws. Adaptive,
resource-bounded schedule synthesis remains a separate task.

## 8. When adaptive acquisition cannot beat a fixed schedule

The next result resolves a restricted policy-synthesis question without
enumerating adaptive decision trees. Its target concerns the **initial**
carrier. It does not equate initial-state recovery with prediction after an
intervention that erases hidden state.

Let \(V\) be a finite-dimensional real or complex Hilbert space. Let
\(\{A_a:a\in\mathcal A\}\) be a finite family of total homogeneous linear source
actions, let \(P:V\to W\) be a passive linear readout, and fix a linear initial
target \(F:V\to Z\) into a finite-dimensional normed space. The possible initial
states are the entire closed unit ball of \(V\). Read \(P\) before any action
and after each action. Known linear instrument updates may instead be included
in the action maps, with that readout convention preserved.

Give each action a state-independent positive cost \(c_a\), and fix a budget
\(B\ge0\). A deterministic adaptive policy chooses its next action or termination
from the exact readouts and action labels recorded so far. Require termination
on every allowed initial state, with total action cost at most \(B\).
Its terminal decoder may be any function of its finite record. This grants
exact real/complex readout and arbitrary mathematical decision maps; it does
not assume that finite-bit arithmetic or physical sensors implement them.
A finite action budget is not a finite information or bit-precision budget.
This is an idealized noiseless worst-case information theorem; rational
certificates verify its finite algebraic conditions, not physical executions
on every real initial state. No reset is assumed, and destructive linear
actions are included through their actual effect in \(H_w\).

For each fixed word \(w\), form \(H_w\) as in CG-10, and define
\[
r_F(w)=\|F\Pi_{\ker H_w}\|,\qquad
\mathcal W_B=\{w:\ \sum_{a\text{ in }w}c_a\le B\}.
\]
The empty word is included and has \(H_{\varnothing}=P\). Let
\(R(\pi)=\sup_{\|x_0\|\le1}\|Fx_0-\widehat F_\pi(x_0)\|\) be the
worst-case error of a policy and its terminal decoder.

**CG-11 (zero-record domination of adaptive acquisition).** Under these
hypotheses,
\[
\boxed{\inf_\pi R(\pi)=\min_{w\in\mathcal W_B}r_F(w).}
\tag{8.1}
\]
More strongly, every policy is weakly dominated in worst-case error by a fixed
schedule: use the action word \(w_0\) that the policy performs on \(x_0=0\),
with the minimum-norm decoder \(FH_{w_0}^\dagger\).

**Proof.** Homogeneous actions preserve zero, so the run on \(x_0=0\) has
only zero readouts and terminates after some feasible word \(w_0\). Let
\(z\in\ker H_{w_0}\) with \(\|z\|\le1\). Its initial readout is zero, so
determinism chooses the same first action as in the zero run, or the same
immediate termination. After the first chosen action its readout is again
zero, by the definition of \(H_{w_0}\). Induction repeats this argument at
every step. Thus both \(+z\) and \(-z\) follow exactly the zero-run word and
terminate with the same record and decoder output \(b_0\). The symmetric-pair
inequality gives
\[
R(\pi)\ge\max\{\|Fz-b_0\|,\|-Fz-b_0\|\}\ge\|Fz\|.
\]
Taking the supremum over the unit hidden ball gives
\(R(\pi)\ge r_F(w_0)\ge\min_{w\in\mathcal W_B}r_F(w)\).
Conversely, any fixed word is an allowed policy. CG-03 gives its exact error
\(r_F(w)\), attained by \(FH_w^\dagger\). Finally, for a nonempty finite
\(\mathcal A\), positive costs bound every feasible word's length by
\(\lfloor B/\min_a c_a\rfloor\), so \(\mathcal W_B\) is finite and the
minimum exists. This proves (8.1) and the stronger domination statement.
If the alphabet is empty, the only word is empty and CG-03 proves the result
directly.

**Exact identification corollary.** Some adaptive policy identifies \(Fx_0\)
for every initial state in the unit ball under budget \(B\) if and only if a
fixed feasible schedule has
\[
\ker H_w\subseteq\ker F.
\]
Its zero-run word is one such schedule. In particular, adaptivity does not
repair a missing initial-target distinction in this model class.

**Finite rational obstruction certificate.** In Euclidean source coordinates,
suppose the matrices, costs, and budget are rational, with positive costs.
Enumerate the finitely many feasible
words. For each word compute whether
\(\operatorname{rank}\binom{H_w}{F}=\operatorname{rank}H_w\) by exact Gaussian
elimination. If one passes, it supplies a lawful fixed schedule and a rational
linear target decoder. If none passes, Gaussian elimination supplies, for
every feasible \(w\), a rational vector \(z_w\in\ker H_w\) with \(Fz_w\ne0\).
Scale each by the rational factor
\(1/\max(1,\|z_w\|_1)\); then \(\|z_w\|_2\le1\) still holds and its target is
still nonzero. The finite table of words, costs, and these hidden-pair witnesses
certifies that **no** adaptive policy in the declared class achieves exact
identification. The proof is the zero-run argument above; enumeration may be
exponentially large and has no claimed efficiency advantage.

If zero costs or an infinite word set are allowed while each policy still
terminates on zero, the same proof gives equality of **infima** over policies
and feasible finite words. A minimum or finite enumeration certificate is then
not guaranteed. State-independent worst-case action cost, a fixed initial
linear target, and the declared prior are load-bearing; average cost, hidden
state-dependent admissibility, randomization, and nonlinear source laws are
different problems.

### 8.1 A small exact counterexample outside the ball hypothesis

Symmetry of a strict subset of the ball is insufficient. Use source state
\((r,a,b,c)\in\mathbb R^4\), passive readout \(P(r,a,b,c)=r\), and three
unit-cost actions that replace \(r\) by \(a,b,c\), respectively, leaving the
other three coordinates unchanged. These actions are total homogeneous linear
maps. Use the Euclidean target norm, fix \(F(r,a,b,c)=(a,b,c)\), budget \(B=2\),
and the finite symmetric prior
\[
K=\{(0,h):h\in\{0,\ \pm u,\ \pm v,\ \pm w\}\},\quad
u=(0,\tfrac12,0),\quad v=(\tfrac12,0,0),\quad
w=(\tfrac12,0,\tfrac12).
\]
Every state lies in the unit ball. Query \(a\); if its value is zero, query
\(b\), and otherwise query \(c\). This adaptive policy identifies all seven
initial states exactly.

Every fixed two-query schedule fails. Reading \((a,b)\) fails to distinguish
\(v\) from \(w\); reading \((a,c)\) fails to distinguish \(0,+u,-u\);
reading \((b,c)\) fails to distinguish \(0,+v,-v\). Query order does not
alter hidden coordinates, and repetitions cannot improve these distinctions.
The first collision has target distance \(1/2\), so every fixed schedule has
worst-case error at least \(1/4\). The fixed schedule \((a,b)\), using the
midpoint on each of its two ambiguous signed pairs, attains exactly \(1/4\).
Thus adaptive error is zero while best fixed error is \(1/4\).

This refutes replacing the full-ball hypothesis by “any symmetric subset of
the unit ball.” It does not refute CG-11. Its lower-bound argument still holds
on whichever hidden vectors belong to \(K\), but the linear fixed-schedule
optimal-recovery identity for the entire ball no longer applies.

The [standalone exact probe](../../research/2026-11-13/principia_observatoris/adaptive_linear_probe.py)
enumerates all 13 fixed words of lengths zero through two and checks this
seven-state result in rational arithmetic. It also preserves separate hostile
controls for nonlinear actions, state-dependent costs, and a randomized
expected-squared-loss objective. Those controls verify particular countermodels;
the universal statement (8.1) has the proof above.

The homogeneous zero-fixed assumption is a sufficient simplification, not an
asserted necessary condition: known affine offsets also admit a center-run
argument after subtracting the fixed-schedule offsets. No extension to unknown
offsets or state-dependent interventions is claimed.

CG-11 is a classical adaptive optimal-recovery consequence presented as a SUCC
acquisition certificate. [Novak's author survey, Theorem 0](https://users.fmi.uni-jena.de/~novak/novak2.pdf),
recalls the Bakhvalov–Smolyak nonadaptive optimality result for scalar integration
on convex balanced classes. [Krieg–Kritzer, Introduction](https://www.ricam.oeaw.ac.at/files/reports/23/rep23-30.pdf),
distinguish settings with optimal linear algorithms from more general
vector-valued approximation. Those broader classes are not silently imported
into (8.1). The actual source-action/cost statement here is proved above;
scholarly priority is not claimed. It reduces this exact finite linear problem
to fixed experiment design. More general embodied-policy questions remain
outside its hypotheses.

## 9. What this book establishes and leaves open

The weak kernel does not derive a single geometry. It supports three legitimate
constructions after different additional data: influence order, distinguishable
behavior, and composable cost. The special nonnegative linear model gives an
exact bridge from causal latency to source graph distance. Signed cancellation,
hidden fibers, and calibration show why a stronger universal bridge fails.

The constructive gain is CG-02–CG-05: a precise obstruction, the smallest
linear repair, an exact best-possible prediction-error certificate, and a
composition law. These instantiate the author's geometric/computational
misalignment without attributing a physical geometry to a fitted matrix. They
do not settle source adequacy, quantum/classical ontology, or the arithmetic
source-selected cancellation problem.

CG-10 closes the access gap for a prescribed actual schedule. CG-11 additionally
eliminates any adaptive advantage for a fixed initial linear target on the
complete Hilbert ball, and gives a finite rational decision/certificate method
under positive action costs. Outside that restricted class, the next useful
extension is a resource-aware version of CG-04: given an
authenticated intervention instrument family with disturbance and reset costs,
characterize which required predictive coordinates can be obtained on a single
carrier, and give a sharp cost or impossibility certificate. Merely finding a
basis of formal future readouts does not solve that access problem.

### Sources and internal antecedents

- PR #618, [research note](../../research/2026-11-13/causal_relevance_proximity/RESEARCH_NOTE.md), all nine sections: founding proposal, classical sensitivity formula, cancellation, and horizon adversaries.
- BPGS-08/09, [claim supplement](../CLAIM_SUPPLEMENT_BOUNDARY_PORT_GEOMETRY.md): failure of present-readout descent and largest future-safe action quotient.
- OPIG-N4, [claim supplement](../CLAIM_SUPPLEMENT_OBSERVATION_PINNED_GEOMETRY.md): source topology does not determine a unique physically calibrated metric.
- Boyd and Lall, [Observability and state estimation](https://ee263.stanford.edu/lectures/observ.pdf), slides 4–7: finite observability map, null-space ambiguity, Cayley–Hamilton closure. CG-04 includes multiple actions; its proof is given above.
- Boyd and Lall, [Autonomous linear dynamical systems](https://ee263.stanford.edu/lectures/lds.pdf), slides 16–20: conditional linearization and examples where identical linearizations conceal different dynamics.
- Foucart and Liao, [Radius of Information for Two Intersected Centered Hyperellipsoids](https://foucart.github.io/publi/OR_L1Noise_v2.pdf), §1 and Lemma 2: classical optimal-recovery setting and symmetric-pair lower bound; this book uses only the simpler ball case proved above.
- Novak, [Some Results on the Complexity of Numerical Integration](https://users.fmi.uni-jena.de/~novak/novak2.pdf), Theorem 0: classical scalar no-adaptivity antecedent. Krieg and Kritzer, [Homogeneous algorithms and solvable problems on cones](https://www.ricam.oeaw.ac.at/files/reports/23/rep23-30.pdf), Introduction: the vector-valued/general-convex-class distinction. Both PDFs inspected.
- Bakhvalov, [1971 original article metadata](https://www.mathnet.ru/eng/zvmmf6826): historical attribution checked against the journal record; its full Russian proof is not a premise used here.
- Lawvere, [Metric spaces, generalized logic and closed categories](https://www.tac.mta.ca/tac/reprints/articles/1/tr1abs.html), 1973, reprinted 2002: established directed metric/enriched-category antecedent. The reprint metadata was retrieved; the PDF endpoint returned a fetch error in this round. No uninspected theorem from that PDF is used as a proof premise.
