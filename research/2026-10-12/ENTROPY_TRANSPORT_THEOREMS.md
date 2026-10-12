# Source-relative entropy transport and nested observer budgets

**Date:** 2026-10-12.

**Status:** CLASSICAL / PROVED LOCAL; new to this project's implementation.

**Scope:** finite probability laws, shared information, conditional frame changes, and a local simplification of the Gaussian-prime manuscript's entropy telescope. This note does not prove a new all-step-bound arithmetic theorem.

## 1. Conventions, source boundary, and provenance

All random variables in this note have finite alphabets. Except where two probability laws are explicitly compared in T4 or in the shift hypothesis of T5, every quantity in an identity is computed under **one declared joint law**. Every logarithm is base 2, so entropies and mutual informations are in bits. A consistent change of logarithm base rescales every term and preserves the inequalities.

Write

\[
H(X)=-\sum_x p(x)\log_2 p(x),\qquad
I(X;Y\mid Z)=H(X\mid Z)-H(X\mid Y,Z),
\]

with \(0\log 0=0\). Let

\[
h(t)=-t\log_2t-(1-t)\log_2(1-t)
\]

with its continuous endpoint values. Total variation is

\[
\operatorname{TV}(P,Q)=\frac12\sum_z|P(z)-Q(z)|.
\]

An assertion that one variable is determined by others means that an actual deterministic function gives that variable on every positive-probability atom. Such a function is a property of the declared source law. It does not authenticate a physical source or prove a proposition on omitted or zero-probability possibilities. Logical proof transport on a broader source class requires its own complete source-domain check.

The source manuscript is the pinned official OpenAI repository at commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`:

- [Coverage from shared continuation data: `coverage-transfer.tex`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex), especially `lem:conditioning` and `thm:transfer`.
- [Zero avoidance and the common-law budget: `information.tex`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/information.tex), especially `eq:translate-information` and `lem:telescope`.
- [Entropy conventions and continuity: `preliminaries.tex`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/preliminaries.tex).

This note builds on SUCC's [finite semantic data-processing theorem](../2026-10-10/FINITE_SEMANTIC_DATA_PROCESSING.md), [source-relative precision transport](../2026-10-11/SOURCE_RELATIVE_PRECISION_TRANSPORT.md), and [retained-history distinction in proof-backaction debt](../2026-10-11/PROOF_BACKACTION_DEBT_ZENO.md), inspected at main commit `68b33157df2086355c00300fc7b534251f6b09c0`. The original manuscript and preserved imports are not modified.

## 2. T1 — Exact shared-conditioning account

### Statement

Let \(X=(X_1,\ldots,X_d)\), with \(X_i\) taking values in a declared alphabet of size \(N_i\ge1\). Let \(R\) be receiver context and \(U\) one shared update or data transcript. Define the joint entropy deficit

\[
D_R(X)=\sum_{i=1}^d\log_2N_i-H(X\mid R)
\]

and conditional total correlation

\[
\operatorname{TC}(X\mid R,U)
=\sum_{i=1}^d H(X_i\mid R,U)-H(X\mid R,U).
\]

Then

\[
\boxed{
\sum_{i=1}^d[\log_2N_i-H(X_i\mid R,U)]
=D_R(X)+I(X;U\mid R)-\operatorname{TC}(X\mid R,U)
\le D_R(X)+H(U\mid R).
}\tag{T1}
\]

No independence of coordinates, source and update, or source and receiver is assumed.

### Proof

Substitution of the definitions gives

\[
\begin{aligned}
\sum_i[\log_2N_i-H(X_i\mid R,U)]
&=\sum_i\log_2N_i-H(X\mid R,U)
  -\operatorname{TC}(X\mid R,U)\\
&=D_R(X)+I(X;U\mid R)-\operatorname{TC}(X\mid R,U).
\end{aligned}
\]

Conditional subadditivity gives \(\operatorname{TC}\ge0\), while \(I(X;U\mid R)\le H(U\mid R)\). This proves the identity and inequality. The cost is attached to the **one joint transcript \(U\)**. ∎

### Weighted independently selected subsets

Let \(J\) be an auxiliary random subset of \(\{1,\ldots,d\}\), independent of \((X,R,U)\), and let \(\pi_i=\Pr(i\in J)\). For each fixed subset \(j\), let \(X_j=(X_i)_{i\in j}\), with its fixed product alphabet. An expectation such as \(\mathbb E_J H(X_J\mid R)\) averages these fixed-map entropies; it is not the entropy of a source-selected coordinate after forgetting the selector.

Applying T1 for each fixed subset and averaging gives

\[
\begin{aligned}
\sum_i\pi_i[\log_2N_i-H(X_i\mid R,U)]
&=\mathbb E_J D_R(X_J)
 +\mathbb E_J I(X_J;U\mid R)
 -\mathbb E_J\operatorname{TC}(X_J\mid R,U)\\
&\le\mathbb E_J D_R(X_J)+H(U\mid R).
\end{aligned}\tag{T1a}
\]

Here the left equality uses that a fixed coordinate is included with probability \(\pi_i\), and the final inequality applies \(I(X_j;U\mid R)\le H(U\mid R)\) to every subset. Independence of \(J\) ensures that conditioning on an actual auxiliary choice does not silently alter the source law used by these entropies.

For the manuscript's signed-coordinate setup, fix integers \(k\ge1\) and \(1\le r\le k\). There are \(k\) pairs with equal alphabet sizes \(p_j\) within each pair. Choose \(r\) distinct pair indices uniformly, then choose one independent fair sign for each. Every signed coordinate has inclusion probability \(r/(2k)\). The nonempty-selection hypothesis is needed when dividing by \(r\) below. Put

\[
\overline L=\frac1k\sum_{j=1}^k\log_2 p_j.
\]

If

\[
\mathbb E_J H(X_J\mid R)\ge(1-\epsilon)r\overline L,
\qquad H(U\mid R)\le\kappa r\overline L,
\]

then the expected alphabet capacity of \(X_J\) is \(r\overline L\), and T1a yields

\[
\frac1{2k}\sum_c[\log_2p_c-H(X_c\mid R,U)]
\le(\epsilon+\kappa)\overline L.\tag{T1b}
\]

With constant \(R\), this recovers the manuscript's one-shared-conditioning-cost lemma. Its source entropy premise is joint; a collection of large marginal entropies does not suffice.

### Controls and interpretation

**Repeated facts.** Let all eight coordinates equal one fair bit \(B\), and set \(U=B\). Each marginal entropy is one bit, but \(H(X)=1\). Hence \(D(X)=7\), \(H(U)=1\), and the sum of the eight conditional deficits is \(8=7+1\). Repetition does not create eight independent facts. The theorem remains valid because it retains the joint deficit.

**Information can create dependence.** For independent fair bits \(X,Y\) and \(U=X\oplus Y\), each individual conditional marginal remains uniform. Nevertheless \(I((X,Y);U)=1\) and \(\operatorname{TC}(X,Y\mid U)=1\). T1 accounts for their cancellation.

**Receiver context changes both sides.** If \(R=X=U\) is a fair bit, then \(H(U\mid R)=0\), but \(H(X\mid R)=0\) also. Retaining unconditional \(H(X)=1\) while charging only \(H(U\mid R)=0\) mixes two different information states. In the walk application, conditioning on an exact checkpoint time likewise determines its position; that conditioning cannot make the displacement cost free while retaining the original unconditioned position entropy.

**Adaptive selection.** Let \(X_1=B\), \(X_2=1-B\), with \(B\) fair, and select the index whose coordinate is zero. Each fixed coordinate is uniform, and each index is selected with probability one half, but the selected value is always zero. Uniform inclusion probabilities do not establish selector independence. An adaptive selector must be included in the data/context and the corresponding source entropies recomputed.

**Status:** CLASSICAL / PROVED LOCAL, by entropy identities. This is a generalization of the project's information accounting, without a claim of literature priority.

## 3. T2 — Conditional frame transport and the sharp two-entropy loss

### Statement

Let \((O,X)\) be an old context/target frame and \((O',X')\) a new frame. Let \(U\) be the update, \(W\) an observation, and \(R\) retained receiver context. Assume deterministic functions satisfying, almost surely,

\[
\begin{aligned}
O&=f_0(O',U,R),& O'&=g_0(O,U,R),\\
X&=f_1(X',O',U,R),& X'&=g_1(X,O,U,R).
\end{aligned}\tag{F}
\]

Thus old and new contexts determine each other given \((U,R)\), and the full frames do also. Coordinate-wise translation in finite groups satisfies these conditions when the common displacement is retained.

The exact signed loss is

\[
\boxed{
\begin{aligned}
&I(X;U,W\mid O,R)-I(X';W\mid O',R)\\
&\quad=I(X;U\mid O,R)
 +I(X';U\mid O',W,R)
 -I(X';U\mid O',R).
\end{aligned}
}\tag{T2}
\]

Consequently

\[
\begin{aligned}
I(X;U,W\mid O,R)-I(X';W\mid O',R)
&\le I(X;U\mid O,R)+H(U\mid O',W,R)\\
&\le2H(U\mid R).
\end{aligned}\tag{T2a}
\]

The difference in T2 can be negative; T2a is an upper bound on loss, not an assertion that every update loses information.

### Proof

For fixed values of \((U,R)\), conditions F make the context map bijective on its support. Within each corresponding context fiber, the target map is bijective on its conditional support. These bijections preserve the conditional target entropy, both before and after conditioning on \(W\). Hence

\[
I(X;W\mid O,U,R)=I(X';W\mid O',U,R).
\]

Split the original package by the chain rule:

\[
I(X;U,W\mid O,R)
=I(X;U\mid O,R)+I(X';W\mid O',U,R).
\]

For arbitrary finite variables,

\[
I(A;B\mid C,U)-I(A;B\mid C)
=I(A;U\mid B,C)-I(A;U\mid C),
\]

as follows by expanding all four terms into conditional entropies. Apply this with \(A=X'\), \(B=W\), and \(C=(O',R)\). This proves T2. Nonnegativity of the subtracted mutual information and the bounds

\[
I(X;U\mid O,R)\le H(U\mid O,R)\le H(U\mid R),
\]

\[
I(X';U\mid O',W,R)\le H(U\mid O',W,R)\le H(U\mid R)
\]

give T2a. ∎

The first cost is information the update reveals about the old target. The second can arise when knowledge of the update unlocks information in the observation. The subtracted term accounts for update information already present in the new frame.

### Exact sharp example in the prime residue group modulo 5

Let \(B,V\) be independent fair bits. Set

\[
X=2V+1+B,\qquad U=-B,\qquad
X'=X+U\pmod5=2V+1,\qquad W=V\oplus B,
\]

and let \(O,O',R\) be constant. The law has these four atoms, each of probability \(1/4\):

| \(X\) | \(U\) | \(X'\) | \(W\) |
|---:|---:|---:|---:|
| 1 | 0 | 1 | 0 |
| 2 | -1 | 1 | 1 |
| 3 | 0 | 3 | 1 |
| 4 | -1 | 3 | 0 |

Every fixed-\(U\) translation is a bijection of \(\mathbb Z/5\mathbb Z\). Both old and new residues avoid zero. The update is deterministic from \(X\): it is zero for odd \(X\) and \(-1\) for even \(X\).

The pair \((U,W)\) determines \(B\), then \(V\), then \(X\). Thus \(I(X;U,W)=H(X)=2\) bits. The table gives each combination of \(X'\in\{1,3\}\) and \(W\in\{0,1\}\) probability \(1/4\), so \(X'\) and \(W\) are independent. Finally \(H(U)=1\). Therefore

\[
\boxed{I(X;U,W)-I(X';W)=2=2H(U).}\tag{T2b}
\]

This exact probability-table argument refutes replacing \(2H(U)\) by \(H(U)\) solely because coordinate updates are bijective translations or are deterministic from the unknown source. It does not construct an entire infinite avoiding walk or realize all the other hypotheses of the Gaussian-prime manuscript.

The phenomenon persists with almost maximal initial marginal entropy. For any prime \(p\equiv1\pmod4\), choose independent \(B\) uniform on \(\{0,1\}\) and \(V\) uniform on \(\{0,\ldots,(p-3)/2\}\). Use \(X=2V+1+B\), \(U=-B\), \(X'=2V+1\), and \(W=(V\bmod2)\oplus B\). Since \((p-1)/2\) is even, \((U,W)\) consists of two independent fair bits determined by \(X\), while \(W\) is independent of \(X'\). The same two-bit loss occurs, with

\[
H(X)=\log_2(p-1),\qquad
\log_2p-H(X)=\log_2\frac{p}{p-1}\longrightarrow0.
\]

### Valid improvements under additional hypotheses

If \(I(X;U\mid O,R)=0\), then T2a improves to \(H(U\mid O',W,R)\le H(U\mid R)\). This one-cost bound is sharp: take \(X,U\) independent fair bits, \(X'=X\oplus U\), and \(W=X\).

If \(U\) is already determined by receiver context \(R\), all the update-information terms in T2 vanish. A deterministic constant update is a special case. An update determined by the **unknown target** need not be known to the receiver, as T2b demonstrates.

**Source-proof consequence:** T2 specializes to `eq:translate-information` in the pinned `information.tex`. It exposes potentially smaller conditional costs, but no extra estimate reducing those costs in the actual walk experiment has been established here. The generic coefficient 2 survives the audit.

**Status:** CLASSICAL / PROVED LOCAL identities and explicit sharp counterexample. No claim of a new all-\(D\) arithmetic result.

## 4. T3 — One shared update for a whole moving-state block decomposition

### Statement

Let \(V=(B_1,\ldots,B_m)\) be a finite observation word divided into \(m\ge1\) blocks. Let \(C\) be initial observer state, \(R\) retained receiver context, and \(U\) one joint transcript of additional updates. Suppose the state \(S_a\) at the start of block \(a\) satisfies

\[
S_a=f_a(C,R,U,B_1,\ldots,B_{a-1})
\quad\text{almost surely}\qquad(1\le a\le m).
\]

Then

\[
\boxed{
H(V\mid C,R)
\le I(V;U\mid C,R)+\sum_{a=1}^m H(B_a\mid S_a,R)
\le H(U\mid C,R)+\sum_{a=1}^m H(B_a\mid S_a,R).
}\tag{T3}
\]

No block independence is required.

### Proof

Condition once on the whole transcript:

\[
\begin{aligned}
H(V\mid C,R)
&=I(V;U\mid C,R)+H(V\mid C,R,U)\\
&=I(V;U\mid C,R)
 +\sum_{a=1}^m H(B_a\mid C,R,U,B_1,\ldots,B_{a-1}).
\end{aligned}
\]

The declared state function makes \((S_a,R)\) a function of the conditioning variables in its summand. Removal of conditioning therefore gives

\[
H(B_a\mid C,R,U,B_1,\ldots,B_{a-1})\le H(B_a\mid S_a,R).
\]

Sum these inequalities and use \(I(V;U\mid C,R)\le H(U\mid C,R)\). ∎

The update transcript is paid for once across the entire decomposition. If the state is computed from initial state and retained preceding observations, \(U\) may be constant and the overhead is zero. If additional stochastic updates are required, their joint transcript must be included in the reconstruction hypothesis and the information account. These are statements about conditional information; they do not measure physical computation work.

### Uncharged-update counterexample

Let \(B_1=B_2=U\) be one fair bit, put \(S_1=S_2=U\), and take \(C,R\) constant. Then

\[
H(V)=1,\qquad H(B_1\mid S_1)+H(B_2\mid S_2)=0.
\]

Suppressing \(U\) would falsely assert \(1\le0\): the first state is not determined by the claimed empty past. Charging the one-bit transcript once restores equality \(1\le1\). The finite implementation rejects the uncharged reconstruction using an exact functional-dependency collision, rather than treating a numerical inequality as evidence for a valid update map.

**Status:** CLASSICAL / PROVED LOCAL chain-rule generalization, newly implemented for moving SUCC observer states.

## 5. T4 — Conditional entropy continuity independent of receiver alphabet size

### Statement

Let \(P,Q\) be two laws on the same finite product alphabet \(\mathcal A\times\mathcal B\), with \(|\mathcal A|=M\ge1\), and put \(\delta=\operatorname{TV}(P,Q)\). For every \(\delta\in[0,1]\),

\[
\boxed{
|H_P(A\mid B)-H_Q(A\mid B)|
\le\delta\log_2 M+h(\delta).
}\tag{T4}
\]

There is no factor depending on \(|\mathcal B|\).

### Proof

First suppose \(0<\delta<1\). The pointwise common mass sums to \(1-\delta\). Define probability laws \(P_\cap,P_1,Q_1\) by

\[
(1-\delta)P_\cap(a,b)=\min(P(a,b),Q(a,b)),
\]

\[
P=(1-\delta)P_\cap+\delta P_1,
\qquad Q=(1-\delta)P_\cap+\delta Q_1.
\]

Realize each mixture with a Bernoulli indicator \(E\), where \(\Pr(E=1)=\delta\). The entropy chain rule in the \(P\)-mixture gives

\[
H_P(A\mid B)
=(1-\delta)H_{P_\cap}(A\mid B)
 +\delta H_{P_1}(A\mid B)+I_P(A;E\mid B).
\]

The analogous formula holds for \(Q\). Subtracting cancels the common-part term. Each residual conditional entropy is in \([0,\log_2M]\), so their difference in absolute value is at most \(\log_2M\). Each mixture-information term is in \([0,h(\delta)]\), because

\[
0\le I(A;E\mid B)\le H(E\mid B)\le H(E)=h(\delta).
\]

Their difference in absolute value is therefore at most \(h(\delta)\), not twice that amount. This proves T4. If \(\delta=0\), the laws coincide. If \(\delta=1\), use \(0\le H(A\mid B)\le\log_2M\). ∎

If the actual distance is only known to be at most \(\bar\delta\le1/2\), the right side may be evaluated at \(\bar\delta\), since both \(t\log_2M\) and \(h(t)\) are nondecreasing on \([0,1/2]\). This qualification matters when a uniform error bound is substituted for an actual distance.

### Classical source and priority boundary

T4 is an elementary, nonoptimal classical bound. Mohammad A. Alhejji and Graeme Smith prove the sharper bound

\[
|H_P(A\mid B)-H_Q(A\mid B)|
\le\epsilon\log_2(M-1)+h(\epsilon)
\]

for \(M\ge2\), \(\operatorname{TV}(P,Q)\le\epsilon\le1-1/M\), and show its sharpness. See their primary paper [*A Tight Uniform Continuity Bound for Equivocation*, arXiv:1909.00787v3, Main Result, equation (7)](https://arxiv.org/html/1909.00787v3), also [ISIT 2020, DOI 10.1109/ISIT44484.2020.9174350](https://doi.org/10.1109/ISIT44484.2020.9174350). The elementary common-part proof above is supplied to make this note self-contained; no new continuity theorem is claimed.

### Exact local simplification in the Gaussian-prime manuscript

In the pinned `information.tex`, `lem:telescope`, the target is an increment block of length \(L_j\), and the conditioning variable is the accumulated residue state \(Q_j\). The manuscript bounds the full residue alphabet and applies continuity separately to a joint entropy and a conditioning entropy.

Apply T4 directly with

\[
A=W_{L_j},\qquad B=Q_j,\qquad
|\mathcal A|\le K_D^{L_j}.
\]

Its existing joint-law shift estimate \(\operatorname{TV}\le\delta\le1/2\) then gives

\[
\begin{aligned}
H(W_{L_j}(t_*+a)\mid Q_j(t_*+a))
&\le H(W_{L_j}(t_*)\mid Q_j(t_*))\\
&\quad+\delta L_j\log_2K_D+h(\delta).
\end{aligned}\tag{T4a}
\]

Thus the paragraph estimating

\[
\sum_T k_T\log(2T)=O(T_+)
\]

and the following separate joint-plus-conditioning entropy continuity calculation are unnecessary **in this telescope step**. T4a supplies the required comparison without any bound on the size of the residue-state alphabet. When \(L_j\mid L_{j+1}\), its normalized error is

\[
\delta\log_2K_D+\frac{h(\delta)}{L_j}.
\]

The existing residue-update map, block chain rule, and telescoping argument remain. The source-derived geometry, joint-entropy estimates, coverage transfer, multiscale schedule, lower information rates, and final arithmetic existence/periodicity arguments retain their original proof obligations. This is a local proof simplification by a classical inequality, not a replacement of the all-\(D\) argument.

## 6. T5 — Finite nested receiver-rate budget with update and law-drift costs

### Statement

Fix integers \(n\ge1\), \(K\ge1\), and \(L_1,\ldots,L_n\ge1\) with

\[
L_1\mid L_2\mid\cdots\mid L_n.
\]

On one finite probability space, let \(V_1,\ldots,V_{L_n}\) be observations in one alphabet of size at most \(K\). For each needed offset define

\[
W_\ell(a)=(V_{a+1},\ldots,V_{a+\ell}),
\qquad W_0(0)=\varnothing.
\]

Let \(R\) be retained receiver context. Let \(Q_0(0),\ldots,Q_n(0)\) be nested states, meaning that for each \(j\ge1\), \(Q_{j-1}(0)\) is determined by \((Q_j(0),R)\). For each \(j<n\), put \(m_j=L_{j+1}/L_j\), and assume one finite update transcript \(U_j\) and starting states \(Q_j(a)\) at the offsets \(a=bL_j\), \(0\le b<m_j\), with the following properties.

1. **State reconstruction:** for every such offset,

   \[
   Q_j(a)=f_{j,a}(Q_j(0),R,U_j,W_a(0))
   \quad\text{almost surely}.
   \]

2. **Joint-law comparison:** for a number \(0\le\delta_j\le1/2\),

   \[
   \operatorname{TV}\!\left(
   \mathcal L(W_{L_j}(a),Q_j(a),R),
   \mathcal L(W_{L_j}(0),Q_j(0),R)
   \right)\le\delta_j.
   \]

All states compared in this formula use the same named state alphabet for a given \(j\). Neither stationarity of the process nor independence of observations is assumed. The triple-law comparison includes receiver context; matching only the unconditioned block marginal would not suffice.

Define the actual cost of the one joint update transcript by

\[
c_j=I(W_{L_{j+1}}(0);U_j\mid Q_j(0),R).
\]

Then the finite bound is

\[
\boxed{
\begin{aligned}
\sum_{j=1}^{n}
\frac{I(Q_j(0);W_{L_j}(0)\mid Q_{j-1}(0),R)}{L_j}
\le\log_2K
+\sum_{j=1}^{n-1}\left[
\frac{c_j}{L_{j+1}}
+\delta_j\log_2K
+\frac{h(\delta_j)}{L_j}
\right].
\end{aligned}
}\tag{T5}
\]

One may replace \(c_j\) by its upper bound \(H(U_j\mid Q_j(0),R)\). There is no factor for the number of blocks or residue coordinates multiplying that transcript cost. There is also no bound on the alphabet sizes of \(Q_j\) or \(R\) in T5.

### Proof

Define the entropy rates before and after adding state \(Q_j(0)\):

\[
a_j=\frac{H(W_{L_j}(0)\mid Q_{j-1}(0),R)}{L_j},
\qquad
b_j=\frac{H(W_{L_j}(0)\mid Q_j(0),R)}{L_j}.
\]

Nestedness implies that the \(j\)-th information charge in T5 is exactly \(a_j-b_j\).

For \(j<n\), partition \(W_{L_{j+1}}(0)\) into the \(m_j\) blocks of length \(L_j\). Apply T3 with initial state \(Q_j(0)\), receiver context \(R\), shared update \(U_j\), and block states \(Q_j(bL_j)\). This gives

\[
H(W_{L_{j+1}}(0)\mid Q_j(0),R)
\le c_j+\sum_{b=0}^{m_j-1}
H(W_{L_j}(bL_j)\mid Q_j(bL_j),R).
\]

For each summand, T4 applies with target alphabet size at most \(K^{L_j}\) and conditioning variable \((Q_j,R)\). The joint-law comparison, with the monotonicity qualification following T4, gives

\[
\begin{aligned}
H(W_{L_j}(bL_j)\mid Q_j(bL_j),R)
&\le H(W_{L_j}(0)\mid Q_j(0),R)\\
&\quad+\delta_j L_j\log_2K+h(\delta_j).
\end{aligned}
\]

Summing and dividing by \(L_{j+1}=m_jL_j\) yields

\[
a_{j+1}\le b_j+
\underbrace{\frac{c_j}{L_{j+1}}
+\delta_j\log_2K+\frac{h(\delta_j)}{L_j}}_{e_j}.
\]

Now telescope:

\[
\begin{aligned}
\sum_{j=1}^n(a_j-b_j)
&=a_1-b_n+\sum_{j=1}^{n-1}(a_{j+1}-b_j)\\
&\le a_1-b_n+\sum_{j=1}^{n-1}e_j\\
&\le\log_2K+\sum_{j=1}^{n-1}e_j.
\end{aligned}
\]

The last step uses \(a_1\le\log_2K\) and \(b_n\ge0\). This proves T5, including \(n=1\), when the error sum is empty. ∎

### Exact and approximate cases

If each update is determined by \((Q_j(0),R)\) and every compared joint law agrees exactly, then \(c_j=\delta_j=0\), and the total charge is at most \(\log_2K\).

For constant updates and a uniform law-drift bound \(\delta\le1/2\), the finite error in T5 is

\[
\boxed{
(n-1)\delta\log_2K
+h(\delta)\sum_{j=1}^{n-1}\frac1{L_j}.
}\tag{T5a}
\]

In particular it is at most \((n-1)[\delta\log_2K+h(\delta)]\). This is a finite inequality before any limiting argument.

For the manuscript's telescope, take constant receiver context, constant \(U_j\), \(K=K_D\), and its existing smoothing bound \(\delta=T_+^{-9}\). Together with its existing \(n=O(\log T_+)\) bound, T5a tends to zero: \(h(T_+^{-9})=O(T_+^{-9}\log T_+)\), so even the coarse total error is \(O_D(T_+^{-9}(\log T_+)^2)\). This conclusion uses no estimate for the size of the residue-state alphabet.

### Law-drift counterexample

Take independent fair bits \(A,B\), set \(V_1=A\), \(V_2=B\), let receiver context and \(Q_0(0)\) be constant, and put

\[
Q_1(0)=A,\qquad Q_2(0)=(A,B),\qquad L_1=1,\quad L_2=2.
\]

The information charges are

\[
I(Q_1(0);A)=1,\qquad
\frac12 I(Q_2(0);(A,B)\mid Q_1(0))=\frac12.
\]

Their sum is \(3/2\), exceeding the one-bit letter capacity. Nevertheless the intermediate state can update by the lawful deterministic additive rule

\[
Q_1(1)=Q_1(0)\oplus A=0.
\]

The missing condition is equality of the compared laws: at offset zero the block/state pair is \((A,A)\), while at offset one it is \((B,0)\). Their total variation distance is \(1/2\). Thus deterministic state transport alone does not permit an error-free nested telescope; the law-drift term is necessary.

Likewise, changing the physical source or its admissible law between terms does not preserve an entropy identity merely because variables retain the same names. Such an intervention needs its own declared source transition and joint-law comparison. Retained context must condition every relevant term consistently.

**Status:** CLASSICAL / PROVED LOCAL, assembled here as a finite receiver-aware theorem from T3 and T4. Its generality is useful for ObsSUCC; no literature priority or new all-\(D\) arithmetic theorem is claimed.

## 7. Operational boundary: conditional replay and state-changing probes

In `information.tex`, repeated packages are sampled independently **conditional on the old residue data** using a specified finite conditional kernel. They need not be consecutive observations along one evolving physical carrier. In `coverage-transfer.tex`, repeated continuations are independent after the exact mixing state is fixed, and can be dependent before that conditioning.

These distinctions are preserved by the theorems above. A SUCC application that substitutes state-changing physical probes for those synthetic replay laws must verify the new conditional kernels, the relevant independence, and the maps relating source epochs. Reusing a recorded outcome under several coordinate names cannot supply independent entropy. Forgetting an update annotation can make conditionally invertible frames lossy when viewed without that annotation, as T2b demonstrates.

The present results concern conditional uncertainty and lawful transport of finite distributions. They do not identify entropy with mathematical truth, prove a physical thermodynamic law for observers, or equate observation cost with proof complexity.

## 8. Implementation, validation, and claim ledger

The finite laboratory is implemented in [entropy_transport.py](../../observational_succ/entropy_transport.py), with [targeted tests](../../tests/test_entropy_transport.py) and the [reproduction probe](../../scripts/entropy_transport_probe.py). The integration receipt is [ENTROPY_TRANSPORT_RECEIPT.json](ENTROPY_TRANSPORT_RECEIPT.json).

The following checks are exact on the supplied finite tables:

- Nonnegative rational probability masses and normalization.
- Functional reconstruction and conditional frame bijections, with an explicit collision on failure.
- Conditional product-law identities, used to reject repeated coordinates presented as independent facts.
- Total variation between declared comparable finite laws.
- Equality of supplied source and basis metadata; these labels are declarations, not source authentication.

Computed entropy, mutual-information, total-correlation, continuity-bound, and slack values are **floating-point diagnostics**. They are not interval enclosures, formal proofs, or exact certificates for inequalities involving irrational logarithms. The exact mod-5 refutation is established by the probability-table argument in T2b; its numerical reproduction is a calibration of that argument.

At the targeted validation checkpoint, the following commands completed successfully:

```sh
python -m unittest discover -s tests -p 'test_entropy_transport.py' -v
python scripts/entropy_transport_probe.py
```

The targeted suite contained 12 passing tests. It includes the sharp two-cost example, exogenous and receiver-known updates, noninvertible frame rejection, repeated-coordinate and parity controls, consistent receiver conditioning, observer-alphabet-independent continuity, rational endpoint handling, deterministic moving states, an uncharged update, and a non-common-law nested-rate counterexample. These runs validate finite implementations and controls; the universal statements are established by their written proofs.

| Claim | Status | Boundary / next discriminator |
|---|---|---|
| T1 shared-cost identity and independent weighted-subset account | CLASSICAL / PROVED LOCAL | Actual source-dependent selection requires its own conditioning account. |
| T2 conditional frame identity | CLASSICAL / PROVED LOCAL | Conditional bijections must be checked on the declared support. |
| Generic replacement of \(2H(U)\) by \(H(U)\) under bijective, source-dependent translation | REFUTED | Exact mod-5 four-atom receipt T2b. |
| T3 one transcript per moving-state decomposition | CLASSICAL / PROVED LOCAL | Uncharged state innovations fail the exact reconstruction gate. |
| T4 receiver-alphabet-independent continuity | CLASSICAL / PROVED LOCAL | Nonoptimal; the sharper Alhejji–Smith theorem is prior work. |
| T5 finite nested receiver-rate budget | CLASSICAL / PROVED LOCAL; new to project | Requires joint block/state/context law comparisons and paid updates. |
| Removal of the full residue-alphabet estimate from the manuscript telescope | PROVED LOCAL simplification | Other geometry, coverage, schedule, and existence obligations remain. |
| A new all-\(D\) arithmetic theorem, a replacement of the full moat proof, or an RH consequence | UNVERIFIED / NOT ESTABLISHED | Would require the corresponding source-derived arithmetic construction and all missing global proof steps. |

There is no unresolved step in the finite proofs T1–T5 as stated after the local audit. The remaining uncertainty concerns applications: whether a proposed observation process actually has the declared source law, executable update maps, replay kernels, entropy inputs, and sufficiently small joint-law drift. A strict improvement of the manuscript's displacement cost would require an additional estimate on the conditional terms in T2, rather than a change of notation.
