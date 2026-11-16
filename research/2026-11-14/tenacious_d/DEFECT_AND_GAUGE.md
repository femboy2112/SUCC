# D2. Structural and predictive defects under observation

A report can retain every possible next outcome while losing its probability. A signed response can vanish along a structurally live route. Two separate questions govern the bridge between the two forges. Which declared experiments retain their incidence after observation? How well can one distribution on the report fiber predict their values?

The first forge supplies target factorization, linear intertwiners and telescoping defects in CG-02–06. The Second Forge supplies the Boolean and weighted may/must closures QG-2–5, signed walk expansions RG-1, and diagonal switching RG-4–5. The proofs below specify their common maps and give restricted answers to its questions about hitting probabilities and cancellation at a prescribed lag. The results have paper proofs. The standalone probe checks finite rational examples. The existing Lean authority applies to its original quantale declarations. [First forge, Book II](../../../docs/principia_observatoris/02_causality_geometry.md) · [Second Forge geometry §§1–6](../principia_observatoris_second_forge/CAUSAL_GEOMETRY.md) · [Referee I](../principia_observatoris_second_forge/agents/OPUS_IV_HOSTILE_REFEREE.md) · [Referee II](../principia_observatoris_second_forge/agents/OPUS_IV_REFEREE_ROUND2.md)

## D2.1. Action words and their linear representations

Take finite nonempty sets of states \(X\) and reports \(Y=q(X)\). In this section probability distributions and basis vectors are **columns**. The pushforward \(P\colon\mathbb R^X\to\mathbb R^Y\) sends \(e_x\) to \(e_{q(x)}\). A deterministic action \(t_a\) induces \(T_ae_x=e_{t_a(x)}\). A stochastic action induces the column-stochastic matrix \(T_ae_x=p_a(\cdot\mid x)\). A fixed word \(w=a_1\cdots a_k\) acts by \(T_w=T_{a_k}\cdots T_{a_1}\).

**Proposition.** For total deterministic actions, the following are equivalent.

1. Each action preserves equality of present reports.
2. Each action admits a deterministic induced action \(b_a\) on \(Y\).
3. Each generator admits a linear intertwiner \(PT_a=B_aP\).

Whenever these conditions hold, \(PT_w=B_wP\) for every word. Conversely, the latter identity for all words includes every generator.

**Proof.** If \(q(x)=q(x')\), the intertwining identity forces \(e_{q(t_a(x))}=e_{q(t_a(x'))}\). Conversely, constancy on fibers defines \(b_a(q(x))=q(t_a(x))\). Its linear extension proves the identity on all basis vectors. Induction gives the word identity. Surjectivity of \(P\) gives uniqueness of \(B_a\). Equivalently \(\ker P\), spanned by \(e_x-e_{x'}\) on common fibers, is invariant. This specializes Astra CG-02 to source-indexed actions. Fable QG-3 permits matching an endpoint by a path of *different length* in its Boolean closure, so closure exactness alone cannot supply this generator identity.

For an action with an emitted label \(\ell\) and updated source state, use its **joint** law of label and successor. The nonnegative matrix \(T_{a,\ell}\) contains the corresponding subprobabilities, with \(\sum_\ell T_{a,\ell}\) stochastic. A refusal can be a separate outcome only when registered by the source contract. If \(PT_{a,\ell}=B_{a,\ell}P\) holds for each branch, successive multiplication preserves the subprobability for every label word and final report. Summing the final report gives its transcript probability. The converse for **joint one-step** laws follows on basis vectors. Marginal label laws or unlabelled reachable endpoints supply weaker data.

For deterministic transitions with weights, replace each basis column by \(s_{a,x}e_{t_a(x)}\). Then \(PT_a\) factors through \(P\) exactly when the full weighted columns agree on each fiber. A zero weight erases successor information. For nonnegative weights, the support of a specified product equals the Boolean composition of the corresponding supports by path expansion. For signed weights this retains the one-way support inclusion from Fable RG-1.

## D2.2. Censored incidence and optimal stochastic prediction

Fix an action and put \(p_x=PT_ae_x\in\Delta(Y)\). These conditional laws are the rows when kernels are displayed in the usual start-by-destination table. For a declared model incidence relation \(G\subseteq Y\times Y\), write \(G_y=\{z:(y,z)\in G\}\). Require \(G_y\ne\varnothing\) on each present fiber when asking for a stochastic model.

**Incidence criterion.** Every true one-step transition is covered by \(G\) iff the censored matrix
\[
C_{z,x}=\mathbf 1_{\{z\notin G_{q(x)}\}}(p_x)_z
\]
vanishes. The excluded mass \(\lambda_x=\sum_z C_{z,x}\) is exactly
\[
\min_{\nu\in\Delta(G_{q(x)})}d_{\rm TV}(p_x,\nu).
\]
Indeed the event \(Y\setminus G_{q(x)}\) gives the lower bound. Move all excluded mass to any one allowed coordinate. The total variation cost of this move is precisely \(\lambda_x\). Here \(d_{\rm TV}(p,\nu)=\tfrac12\sum_z|p_z-\nu_z|=\max_{S\subseteq Y}(p(S)-\nu(S))\). This criterion concerns a single step or a declared word treated as one experiment. QG-5 compares coverage by an entire model closure when path replacement is allowed.

**Optimal common prediction.** Fix a report \(y\) with source fiber \(I=q^{-1}(y)\). The best worst-case error of a single model row respecting \(G_y\) is
\[
r_G(y)=\min_{\nu\in\Delta(G_y)}\max_{x\in I}d_{\rm TV}(p_x,\nu).
\tag{D2.2}
\]
The global one-step optimum over all stochastic \(B_a\) respecting \(G\) is \(\max_y r_G(y)\), since each report has an independently selectable column. For fixed model \(B_a\), its worst-case error over all initial source distributions equals its maximum error on the basis states. Convexity gives the upper bound and a point mass attains it.

There is an exact finite certificate for (D2.2). The constraints are \(\nu_z\ge0,\ \sum_{z\in G_y}\nu_z=1,\ \nu_z=0\) outside \(G_y\), and
\[
r\ge p_x(S)-\nu(S)\qquad (x\in I,\ S\subseteq Y).
\]
Minimize \(r\). A dual witness is a probability \(\alpha\) on the pairs \((x,S)\), giving the lower bound
\[
L(\alpha)=\sum_{x,S}\alpha_{x,S}p_x(S)
 -\max_{z\in G_y}\sum_{x,S:z\in S}\alpha_{x,S}.
\]
**Proof of sharpness.** Use the finite game with payoff \(p_x(S)-\mathbf1_{z\in S}\), with the maximizing player choosing \((x,S)\) and the minimizing player choosing \(z\in G_y\). Its mixed minimizing strategies are precisely the admissible \(\nu\). Its two game values are respectively (D2.2) and \(\max_\alpha L(\alpha)\). Finite linear-programming duality gives equality and attainment. For rational data the finite feasible systems have rational optimal vertices. A proposed primal/dual pair with equal values is checkable by substitution.

Write \(D=\max_{x,x'\in I}d_{\rm TV}(p_x,p_{x'})\), \(m=|I|\). Then
\[
r_G(y)\ge\max\{\max_{x\in I}\lambda_x,\ D/2\}.
\]
The second bound follows from the triangle inequality. With unrestricted output support,
\[
D/2\le r_Y(y)\le (1-1/m)D.
\]
The average of the \(m\) source laws gives the upper bound by convexity. Both bounds are attained. Two rows have a midpoint at radius \(D/2\). For \(m\) distinct point masses, the uniform center has radius \(1-1/m\), and some point mass receives center probability at most \(1/m\). Thus radius cannot in general be inferred by halving the fiber diameter. For a declared **single event** \(S\), a scalar predictor has exact worst-case error \((\max_x p_x(S)-\min_x p_x(S))/2\), attained at the midpoint. Different eventwise midpoints need not form a probability measure.

**Controls.** The interior Bernoulli laws \((1/4,3/4)\) and \((3/4,1/4)\) have the same support and radius \(1/4\). With \(G_y=\{1,2\}\), rows \((3/4,0,1/4),(0,3/4,1/4)\) have excluded mass \(1/4\) and diameter \(3/4\). Their constrained radius is \(1/2\), strictly larger than either elementary lower bound. The center \((1/2,1/2,0)\) gives the upper bound. Give dual mass \(1/2\) to each of the events \((x_1,\{1,3\})\) and \((x_2,\{2,3\})\) to certify the lower bound. Zero common-row error gives ordinary strong Markov lumpability with the specified support constraint. [Buchholz, 1994](https://doi.org/10.2307/3215235)

A support mask allows a model edge to carry zero probability. If every listed edge must carry strictly positive probability, the feasible set is relatively open in its simplex. For \(p=\delta_0\), \(G_y=\{0,1\}\), the infimum is zero and every feasible model has positive error. The distinction matters for attainment.

**Cross-forge separation.** Realize the Bernoulli example on states \(u,v,h\), with \(q(u)=q(v)=0,\ q(h)=1\). Let \(u\) and \(v\) jump only to \(u,h\), with the two respective Bernoulli rows above, and let \(h\) absorb. The sets of one-step reports agree on the merged fiber, so the Boolean generator relation has exact report support from every representative. By induction its reachable report endpoints are also exact. Nevertheless the best one-step stochastic error is \(1/4\). Support completeness and quantitative prediction thus have different verdicts even on the same authenticated carrier.

## D2.3. Propagation and a hitting-probability sandwich

Let \(T_i\) be source stochastic actions, \(B_i\) report stochastic actions, \(p\) an initial source distribution and \(p_{i-1}=T_{i-1}\cdots T_1p\). Set \(E_i=PT_i-B_iP\), \(d_i=\max_x\tfrac12\|E_i e_x\|_1\), and \(\delta(B)=\max_{y,y'}d_{\rm TV}(Be_y,Be_{y'})\). Astra CG-05 gives a sharper endpoint bound in total variation,
\[
d_{\rm TV}(PT_k\cdots T_1p,\ B_k\cdots B_1Pp)
\le \sum_{i=1}^k \Big(\prod_{j=i+1}^k\delta(B_j)\Big)
                \sum_x p_{i-1}(x)\tfrac12\|E_i e_x\|_1.
\]
Each weighted local term is at most \(d_i\). **Proof.** Expand the signed telescoping identity. Each \(E_i p_{i-1}\) has total mass zero. Write any such vector as \(s(u-v)\) for probability vectors \(u,v\), where \(s=\tfrac12\|\cdot\|_1\). The difference of their outputs is the convex average of column differences with weights \(u_yv_{y'}\). Hence each suffix action contracts by its displayed coefficient. Use the triangle inequality on the local mixture and the signed sum. A common reset \(B_j\) has coefficient zero and erases all earlier endpoint defects, even if an intermediate record retained evidence of them. For transcript error use joint outcome/update kernels on a state augmented with the retained history.

For a fixed chronological action schedule of length \(k\), an observable hit set \(H\subseteq Y\), and true pushed-forward rows \(p_{i,x}=PT_i e_x\), define \(L_{k+1}=U_{k+1}=\mathbf1_H\). Recursively set \(L_i(y)=U_i(y)=1\) on \(H\). Elsewhere set
\[
 L_i(y)=\min_{q(x)=y}\sum_z p_{i,x}(z)L_{i+1}(z),\qquad
 U_i(y)=\max_{q(x)=y}\sum_z p_{i,x}(z)U_{i+1}(z).
\tag{D2.3}
\]
**Proposition.** From any \(x\), the probability of hitting \(H\), including the current report, by the end of the schedule lies between \(L_1(qx)\) and \(U_1(qx)\). These bounds are exact extrema for the abstract process permitted to select a fresh representative of each report at each remaining time.

**Proof.** The true backward hitting recursion takes expectation in the actual successor state. Apply the inductive lower and upper bounds to that successor, group by its report, and compare the current representative with the extrema. At a hit the value is one. For the abstract process, attaining representatives exist at each of its finitely many decision points. Backward induction realizes the extremal values. This is a stochastic answer to the Second Forge hitting-probability question at fixed finite horizon. The permitted changes of representative give the rectangular uncertainty familiar in robust dynamic programming. [Iyengar, 2005](https://doi.org/10.1287/moor.1040.0129) · [Kwiatkowska, Norman and Parker, 2006](https://www.cs.ox.ac.uk/david.parker/papers/qest06.pdf)

A four-state chain shows strictness. From \(s\), move to \(a\) with certainty. Let \(a\) remain at \(a\), \(b\) move to \(h\), and \(h\) remain at \(h\). Merge \(a,b\) into the same report, keeping \(s,h\) separate. The source hit probability from \(s\) at horizon two is zero, yet \(U_1(qs)=1\) by switching to \(b\) at the merged report. Two copies of this example with the transitions from \(a,b\) exchanged contain both a strict lower and a strict upper failure from a selected start in separate sources. Ordinary lumpability makes every min and max agree for all observable hitting sets. Fixed-target equality can occur without lumpability, for example for \(H=Y\).

**Sharp nonuniformity.** Let \(0<\epsilon\le1\). In the preceding three-state partition, make \(u\) absorbing and let \(v\) move to \(h\) with probability \(\epsilon\), otherwise remaining at \(v\). The optimal common report row has hazard \(\epsilon/2\) and error \(\epsilon/2\) by the two-row midpoint formula. The may-quotient claims \(h\) reachable from \(q(u)\), although \(u\) cannot reach \(h\). Starting at \(u\), the model's horizon-\(k\) hitting-probability error is exactly
\[
1-(1-\epsilon/2)^k.
\]
Indeed the true probability is zero and the model survives \(k\) ticks with probability \((1-\epsilon/2)^k\). Its contraction coefficient is \(1-\epsilon/2\), so the propagated local-error bound above attains equality at every horizon. Thus arbitrarily small one-step minimax error coexists with an incorrect Boolean endpoint and a hitting-probability error tending to one. Sources claiming uniform long-horizon prediction must supply a separate uniform bound.

## D2.4. Compatible gauges and projected signed responses

Let a declared signed network act on node coordinates. The readout of a node partition is the mass-pushforward matrix \(P\) above. For an invertible diagonal gauge \(D=\operatorname{diag}(d_x)\), a diagonal report gauge \(\bar D\) satisfies \(PD=\bar DP\) iff the \(d_x\) are constant on each fiber. In fact any report linear map satisfying this equality must have \(\bar D e_{q(x)}=d_x e_{q(x)}\). Thus retaining the original physical interpretation of a sum readout across a gauge change constrains the allowable gauge. When both source and readout coordinates are transported together, \(P'=P D^{-1}\) gives \(P'(D A D^{-1})D=PA\) without this restriction.

For an action family suppose **one common** diagonal sign matrix \(S\) and one sign \(\varepsilon_a\) per generator satisfy \(A_a=\varepsilon_a S|A_a|S\). Then
\[
A_w=\Big(\prod_{j=1}^k\varepsilon_{a_j}\Big) S
       (|A_{a_k}|\cdots|A_{a_1}|)S.
\]
If \(S\) is fiber-constant, then \(PS=\bar SP\), so every aggregate column response is the corresponding nonnegative aggregate, up to its input/output signs and word sign. **Proof.** Multiply the generator identities and cancel adjacent \(S^2=I\). Fiber-constant output signs factor out of each reported sum. Input perturbations with several nonzero entries additionally require alignment after switching, just as the corrected Fable HQ-2 does.

**Failure under incompatible aggregation.** Let a source node \(x\) have edges of weights \(+1,-1\) to \(u,v\) respectively and no other edges. The graph is balanced by \(S=\operatorname{diag}(1,1,-1)\), so both individual impulses are nonzero. Merge \(u,v\) into one output report. Their observed sum is zero. Consequently internal balance does not ensure faithful response support after an arbitrary projection. A missing hidden edge, an absent report, and cancellation at the report can have different intervention signatures. Raw unit-dependent magnitudes can also change under positive diagonal rescaling within a fiber. Transporting the readout preserves the experiment.

## D2.5. A sign-pattern decision on acyclic or independently timed networks

**Theorem.** Fix distinct nodes \(x,y\), a positive integer lag \(k\), and a finite directed acyclic graph whose edges carry fixed signs and independently adjustable strictly positive magnitudes. Suppose there is at least one length-\(k\) path from \(x\) to \(y\). There exist magnitudes with zero lag-\(k\) response iff two such paths have opposite signs. The same statement holds for a time-unrolled network whose edges have independently adjustable magnitudes at each stage.

**Proof.** Same-sign path products have a nonzero sum. To realize the opposite case, choose a positive path and set all of its edge magnitudes to one. Set every other edge magnitude to a common \(\delta>0\). Any different path must use a different edge. In a DAG, the chosen path's edges alone form an ordered simple chain, so no alternative path can consist solely of these edges. If \(M\) is the number of length-\(k\) paths, choosing \(0<\delta<1/M\) bounds the sum of absolute rival products by \((M-1)\delta<1\). The response is positive. Repeat with a negative path to obtain a negative response. Interpolate linearly between the two positive magnitude assignments. Continuity of the response polynomial gives a zero with all edges still present. The time-unrolled model is itself a DAG and its independent variables meet the same hypotheses.

One can choose a rational cancelling weighting in this case. Choose a rational \(\delta\) and change the first assignment to the second **one edge at a time**. Either an intermediate rational assignment is already a zero, or one such change crosses zero. A DAG walk uses each edge at most once, so the polynomial is affine in the varied edge. Its root between rational endpoints is rational and strictly positive. This provides a constructive sign-pattern certificate.

A stationary cyclic system refutes unrestricted use of the mixed-sign test. With independent positive magnitudes \(a,b,c\), take
\[
 A=\begin{pmatrix}a&0\\c&-b\end{pmatrix}.
\]
The three length-three walks from coordinate 1 to coordinate 2 have signs \(+,-,+\), while
\[
 (A^3)_{21}=c(a^2-ab+b^2)
 =c\big((a-b)^2+ab\big)>0
\]
for every allowed weighting. Unrolling time while tying the same edge's magnitude across stages retains this obstruction. This resolves the Fable possible-cancellation question on the acyclic and independently timed subfamilies and gives an exact failure of its simplest extension. The unrestricted stationary sign-pattern problem remains open in this dossier.

## Scope and replay

D2.1 uses inherited linear factorization. D2.2 applies ordinary lumpability, total variation and finite linear-programming duality to a common observation map with a declared support mask. D2.3 specializes established robust dynamic programming and the prior defect identity. D2.4 synchronizes the two forges' coordinate conventions. D2.5 is the present paper derivation for the indicated restricted sign-pattern question. Literature priority remains unverified. No claim here depends on fitting an unknown carrier or on an asymptotic arithmetic estimate.

Run the standalone rational checker from the repository root with the command below.

~~~sh
python research/2026-11-14/tenacious_d/defect_and_gauge_probe.py
~~~
