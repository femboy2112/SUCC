# Coherent observer continuation and forced seams

All results have classical mathematical content. Their SUCC composition is developed here with explicit source, history, topology and target obligations. The arithmetic examples and application boundary are in [ARITHMETIC_PLACE_SEAM.md](ARITHMETIC_PLACE_SEAM.md), [BBP_MOMENT_SEAMS.md](BBP_MOMENT_SEAMS.md) and [RH_ORACLE.md](RH_ORACLE.md).

## 1. What must agree

Fix a carrier c and a comparison target q. At position t let E_t be the admissible observer states, including source evidence, retained causal history, frame and current report. Let J_t be a valid comparison map into a common target space. Define

\[
 F_t(c,q)=\{o\in E_t:\operatorname{src}(o)=c,\ J_t(o)=q,
                    \text{all declared constraints hold}\}.
\]

There are two distinct constructions:

- A family in these fibers agrees on c,q while other observer coordinates can vary.
- A parallel family additionally satisfies every transport equation o_v=T_{uv}o_u.

In either case source authentication is a mathematical premise requiring evidence. Equality of strings in the implementation is bookkeeping for that premise, not its proof. If a full causal history matters to an edge, the state must retain it or a proved sufficient quotient. Prefix expansion always works in a finite model, at potentially exponential cost.

**Invariant guard.** If D(o)=q is exactly the agreed transported invariant, D is constant and cannot have opposite nonzero endpoint signs. A crossing coordinate must therefore be a declared relative location, discrepancy, orientation-dependent coordinate or other permitted varying report. That guard prevents proving a contradiction from incompatible definitions of agreement.

## 2. PI-01: exact finite extension theorem

Let F_0,...,F_n be finite fibers, A subset F_0 and B subset F_n the allowed endpoints, and E_i subset F_i x F_{i+1} lawful edges. Every edge must preserve the source/comparison target and required memory. Write

\[
 L_0=A,\quad
 L_{i+1}=\{y:\exists x\in L_i,\ (x,y)\in E_i\},
\]
\[
 R_n=B,\quad
 R_i=\{x:\exists y\in R_{i+1},\ (x,y)\in E_i\}.
\]

The following are equivalent:

1. There is a lawful endpoint-to-endpoint observer chain.
2. L_n intersects B.
3. L_i intersects R_i for at least one i.
4. L_i intersects R_i for every i.

**Proof.** Any chain belongs to both cones at every cut. Conversely a state in both cones has an admissible prefix from A and suffix to B, by induction in the cone definitions. Concatenation at that same complete state gives the chain. This also constructs a witness by retaining predecessor pointers. If no chain exists, the two cones are disjoint at every layer. On a given explicitly represented graph this costs O(number of vertices + number of edges). QED.

**Why full state matters.** The source sets {0,1}, {1,2}, {0,2} are pairwise compatible but globally inconsistent. Allowing each edge to pick a different source creates a spurious path. A state can instead retain one common source witness or the entire cumulative feasible source fiber. Likewise a local transition relation cannot erase a history on which future legality depends.

## 3. PI-02: exact non-vacuous seam theorem

Let Z be any specified set of observer vertices, including a simultaneous-null set defined by many coordinates. Assume at least one A-to-B chain exists.

\[
 \boxed{\text{Every lawful chain meets }Z
 \quad\Longleftrightarrow\quad
 \text{no lawful chain survives deletion of }Z.}
\]

**Proof.** A chain avoiding Z is exactly a chain in the graph with Z removed. Apply PI-01. QED.

This is necessary and sufficient for finite crossing. It works for directed causal paths. The initial existence assumption prevents vacuous claims that a disconnected system has a forced seam. For continuous paths, the same equivalence holds with path components of E minus Z. This abstract equivalence is a characterization; the actual separator certificate remains to be supplied.

**Quantitative version.** Give each vertex the nonnegative cost a(v)=|D(v)|. For reachable vertices define

\[
 w_0(v)=a(v),\qquad
 w_{i+1}(v)=\min\{a(v),\max_{u\to v}w_i(u)\}.
\]

Unreachable values are minus infinity. Induction gives

\[
 \max_{v\in B}w_n(v)
 =\max_{\text{lawful chains }P}\min_{v\in P}|D(v)|.
\]

Thus every chain hits |D|<=tau exactly when this optimum is <=tau. This is a finite bottleneck formulation of the separator test.

## 4. PI-03: sharp carrier-granular intermediate value law

Let o_0,...,o_n be a lawful chain and d_i a real relative defect in one transported orientation. Suppose d_0<=0<=d_n and

\[
 |d_{i+1}-d_i|\le\delta.
\]

Then either a vertex is exactly null or a sign-changing edge has an endpoint satisfying

\[
 \boxed{|d_i|\le\delta/2.}
\]

**Proof.** If no zero occurs, take the first positive value. Its predecessor is negative; their absolute values add to their jump, at most delta. At least one is at most delta/2. The reverse endpoint orientation is identical. QED.

The constant is sharp: the two-vertex chain (-delta/2,+delta/2). Linear interpolation has a root inside the edge, but it represents an actual observer only if the carrier admits that edge interior.

If the values lie in hZ, h>0, and all jumps are **strictly less than 2h**, a genuine zero vertex is forced. Otherwise the first sign-changing edge would jump from at most -h to at least h. Equality is insufficient: (-h,+h) is the sharp countermodel.

With certified readout errors epsilon_i, endpoint signs must be certified with those errors included. A true near-zero of size delta/2 has measured magnitude at most delta/2+epsilon_i. Uncontrolled floating signs are not certificates.

## 5. PI-04: coherent transport is governed by holonomy

Let a connected graph have fibers F_v and bijections T_e on oriented edges, with inverse transport on the reversed edge. Choose a root r and anchor a in F_r. A parallel section with that anchor exists if and only if every based loop transport H fixes a:

\[
 \boxed{H(a)=a\quad\text{for every loop based at }r.}
\]

If it exists, it is unique; a second prescribed endpoint b is compatible exactly when transport of a along a root-to-endpoint path equals b.

**Proof.** A parallel section necessarily returns to its own anchor along every loop. Conversely choose root-to-v paths and transport a along them. Two choices differ by a based loop, hence give the same value. Comparing the chosen path to v with the path to u followed by u->v verifies each edge equation. Root transport also proves uniqueness. QED.

On a finite graph a spanning tree reduces verification to the fundamental non-tree loops. Requiring every holonomy to be the identity on the entire fiber is stronger than necessary: only the anchor must lie in their common fixed set.

For linear fibers the allowable anchors are the common holonomy-fixed subspace. A real one-dimensional loop with transport -1 forces a=0. For a **continuous**, potentially nonparallel scalar section with gluing f(1)=-f(0), ordinary IVT likewise forces a zero. A complex scalar has no such conclusion: exp(i*pi*t) avoids zero while joining opposite values. The real orientation hypothesis is substantive.

## 6. PI-05: constructive endpoint-preserving continuum selection

Suppose F(t) is a nonempty compact convex subset of R^d for each t in [0,1], varying continuously in Hausdorff distance. Let a in F(0), b in F(1). Define

\[
 y(t)=(1-t)a+tb,\qquad s(t)=P_{F(t)}y(t),
\]

where P is Euclidean nearest-point projection. Then s is a continuous section with s(0)=a and s(1)=b.

**Proof.** Compactness gives a minimizer; convexity and strict convexity of squared distance give uniqueness. If t_n->t, Hausdorff continuity bounds the corresponding sets locally. Every subsequential limit z of projections lies in F(t). For any w in F(t), choose w_n in F(t_n) tending to w. Passing to the limit in the minimizing inequality makes z the unique nearest point to y(t). All subsequential limits coincide, so the projections converge. Endpoint projection fixes a,b. QED.

This is a usable sufficient condition, not a necessary one and not a claim that all observer fibers are convex. Taking a convex hull can introduce fictitious observers unless mixtures are lawful in the carrier.

**A granularity modulus.** For p=P_K x, q=P_L y, h=d_H(K,L), projection inequalities imply

\[
 \|p-q\|^2\le \|x-y\|\|p-q\|
       +(\operatorname{dist}(x,K)+\operatorname{dist}(y,L))h.
\]

Indeed approximate q by a point of K and p by a point of L within h, apply the two projection variational inequalities and subtract. Solving this quadratic gives

\[
 \|p-q\|\le\|x-y\|
  +\sqrt{(\operatorname{dist}(x,K)+\operatorname{dist}(y,L))h}.
\]

If y is M-Lipschitz, F is H-Lipschitz in Hausdorff distance and dist(y(t),F(t))<=R, then

\[
 \|s(t)-s(u)\|\le M|t-u|+\sqrt{2RH|t-u|}.
\]

A continuous relative scalar defect on this feasible graph has a zero if its endpoint signs straddle zero. A Lipschitz defect additionally inherits explicit mesh jump bounds.

**Crucible.** Nonempty compact connected fibers alone fail: F(t)={sin(1/t)} for t>0, F(0)=[-1,1]. The feasible graph is compact but no continuous section exists at zero. Hausdorff continuity is not decorative.

## 7. PI-06: exact refinement criterion for continuous sections

Let X be compact metric, F subset [0,1]xX closed, and A subset [0,1]^2 x X^2 a closed optional pairwise compatibility relation. Fix endpoints a,b. Let omega:[0,1]->[0,infinity) be **continuous**, nondecreasing, with omega(0)=0.

For the dyadic mesh D_n={k/2^n:0<=k<=2^n}, let P_n consist of all assignments x:D_n->X satisfying the endpoints, F, every declared pair relation A, and

\[
 d(x(s),x(t))\le\omega(|s-t|)
 \quad(s,t\in D_n).
\]

Then

\[
 \boxed{\forall n,\ P_n\ne\varnothing
 \quad\Longleftrightarrow\quad
 \text{a continuous section with these constraints and this modulus exists}.}
\]

**Proof.** Each P_n is compact, because it is a closed subset of a finite power of X. Restriction P_{n+1}->P_n is continuous and total. In the product of all P_n, compatibility equations are closed. Any finite collection is realized by projecting from a sufficiently high nonempty level. Compactness gives compatible assignments at all levels; surjectivity of each restriction is unnecessary. They define a uniformly continuous function on the dyadic rationals, hence a unique continuous extension to [0,1]. Closedness passes F and A to the limit. Continuity of omega passes the same modulus. The reverse implication is restriction of an existing section. QED.

This is an existence theorem, not a computable-choice theorem. The finite assignments may themselves take values in an infinite compact space; nonempty P_n is an assumption, not an executed test.

An inverse limit of finite **discrete** state spaces is totally disconnected. A compatible sequence of finite path records is therefore not itself an ordinary continuous path in that product. PI-06 constructs its curve in the declared compact metric realization X, with a common modulus. A different carrier needs its own geometric realization or justified quotient of addresses.

**Why compactness and one modulus matter.** Nonempty discrete levels P_n=N with maps k->k+1 have no compatible sequence: p_0=p_n+n is impossible for all n. Bounded but increasingly oscillatory sections need not have a continuous limit. Adjacent-edge checks must either imply all needed comparisons by a proved cocycle law or be expanded to retain the relevant history.

## 8. PI-07: simultaneous null towers and a multidimensional repair

Let K be compact and D_j:K->R continuous. There is a common zero of all D_j if for every m the equations D_1=...=D_m=0 have a **simultaneous** solution.

**Proof.** Their finite common-zero sets are nonempty, closed and nested. Compactness gives an element of the intersection. QED.

For compact metric K it suffices to have x_m with

\[
 \max_{j\le m}|D_j(x_m)|\le\epsilon_m,\qquad\epsilon_m\to0.
\]

A convergent subsequence with indices tending to infinity makes each fixed D_j vanish at the same limit.

Equivalently define a_m=min_x max_{j<=m}|D_j(x)|. The a_m are nonnegative and nondecreasing. A common null exists iff every a_m=0, equivalently iff their limit is zero. One root per coordinate is insufficient: t-1/3 and t-2/3 have distinct roots. Even antipodal vector endpoints can avoid the origin, as (2t-1,4t(1-t)) does.

**Poincare–Miranda repair.** Let D:[0,1]^m->R^m be continuous with D_j<=0 on x_j=0 and D_j>=0 on x_j=1. Then D has a simultaneous zero. To see this from Brouwer's theorem, apply it to

\[
 T(x)=\operatorname{clip}_{[0,1]^m}(x-D(x)).
\]

At a fixed point, an interior coordinate forces D_j=0. At x_j=0 the fixed-point equation forces D_j>=0, while the face condition forces D_j<=0; at x_j=1 the inequalities reverse. Thus every coordinate is zero. This is the classical Poincare–Miranda theorem, not a new SUCC theorem.

An all-order version uses the compact Hilbert cube K=product_j[-1/j,1/j] in l^2. If every coordinate D_j is continuous and has the corresponding face signs, fix tail coordinates to zero and apply the finite theorem to the first m coordinates. Compactness then produces a common zero of all coordinates. This is the mechanism in Mawhin's Theorem 5.1 [1]. It requires a coherent multidimensional family of actual observers; arbitrary formal coordinates do not supply it.

## 9. PI-08: zero and infinity are typed boundary observers

The change u=t/(1+t) identifies [0,infinity] with [0,1]. The preceding theorems apply only if the state, source comparisons and relevant defects extend continuously at the added point. Reparameterizing sin(t) does not create a limit. A formal inverse-limit observer need not be a continuous real-parameter endpoint.

If f is continuous on [0,infinity), f(0)<0 and liminf f(t)>0, some finite T has f(T)>0 and IVT yields a finite zero. If f(t)=1/(1+t), the only zero after compactification is the new infinity point. Distance between endpoint locations supplies no sign condition: f identically 1 is a control.

## 10. Composed continuation/crossing law

The requested theorem is a **composition** with independently checkable premises:

1. Correct source/history constraints define the feasible observer space.
2. PI-01, PI-04, PI-05 or PI-06 supplies endpoint continuation in the intended sense.
3. PI-02, PI-03, an oriented-loop argument or PI-07 supplies the specified seam.
4. An application-specific identity or arithmetic bound assigns consequences to that seam.

For example a source-authenticated real scalar defect, a PI-05 section and opposite endpoint signs force an exact continuous zero. At discrete resolution PI-03 gives delta/2 or, under its lattice condition, an exact vertex zero. For a full null tower PI-07 replaces a scalar sign argument.

These hypotheses exclude explicit countermodels rather than dismissing the user's construction. They show precisely which kind of continuous observer family is sufficient, and which part of a mathematical application still has to be proved.

## 11. PI-09: an information-relevant rank seam

Let A(t) be a continuous family of real d-by-d observer Jacobians, and suppose det A(0) and det A(1) have opposite signs. The determinant is continuous, so some t_* has det A(t_*)=0. Thus a nonzero infinitesimal carrier direction belongs to the observation kernel at that point.

This is a precise first-order invisibility seam. It need not destroy global identification: x mapped to x^3 is injective although its derivative at zero vanishes. If all A(t) are required to be invertible, the opposite endpoint orientations instead certify that such a family does not exist. A rank-defect conclusion is distinct from a scalar display zero.

## References

1. Jean Mawhin, *Variations on Poincare–Miranda's theorem*, Advanced Nonlinear Studies 13 (2013), 209–217; Theorem 5.1, pp.215–216. [Paper](https://www.degruyterbrill.com/document/doi/10.1515/ans-2013-0112/pdf).
2. Allen Hatcher, *Algebraic Topology*, covering-space lifting, Propositions 1.30 and 1.33. [Author's chapter](https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf). General covering maps require their own hypotheses; the finite transport proof above is self-contained.
3. Ernest Michael, *Continuous selections I*, Annals of Mathematics 63 (1956), 361–382. The present dossier proves only its elementary compact-convex Hausdorff-continuous specialization directly; no unrestricted selection claim is imported.

The proof bodies above were independently reconstructed by the constructor and adversarial agents, then checked and synthesized by the root agent. They share model family and task provenance; this is not independent scholarly or formal-kernel verification.
