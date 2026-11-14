# Polyhedral interception from a finite record

[TD-W1 and W2](WARNING_AND_CLASSICALITY.md) decide interception for finite hidden states and terminal action sets. The following extension allows a continuum of hidden states and commands, a bounded clock, and a finite record at every decision epoch. It gives an exact rational winning policy or an obstruction.

## TD-W4. Exact finite policy synthesis

A joined state b=(s,x) retains the original source s and the current state x. The initial nonempty set B₀ is a finite union of compact rational polytopes in a common Euclidean space. The deadline D is a nonnegative integer. At each time t≤D there are finitely many preterminal operations a of known positive integer duration. Each has a finite output alphabet O and a rational polyhedral legality guard L (or a finite union of such guards). For each o∈O, a finite union of closed rational polyhedra

\[
 R_{t,a,o}\subseteq\{(s,x,x')\}
\]

specifies the successor. Every legal state has at least one available successor and output. All possible outputs and successors are adversarial for the guarantee. This includes closed sensor strips overlapping at a threshold. Dynamics may erase x while s remains fixed. Intermediate failure, pending actuators and observer access must have the same state-and-clock interpretation as in W2. Time of arrival must enter the report whenever observable. A delayed terminal action is available only when its stated safety test includes its intervened trajectory and arrival by D.

Assume projected successor sets of reachable compact components are bounded. A known compact operational state envelope, or finitely many affine updates with bounded polyhedral disturbances, suffices. This hypothesis prevents an unbounded hidden fiber from evading finite witness detection. It is additional to compactness of B₀.

The terminal command u lies in a common rational polyhedron U⊆ℝᵐ. For a finite union B=⋃Pᵢ of compact rational belief polytopes, the safe action set at b is

\[
 C_t(b)=\{u\in U:g_k(b,u)\le0,\quad 1\le k\le r_t\}.
\]

Here each rational function gₖ is **affine in b for fixed u and affine in u for fixed b** (bi-affine polynomials are allowed). Jointly affine safety inequalities suffice for the requested linear safety class. Equalities use both weak inequalities. A state-independent command domain U need not be bounded. Optional finite known safety regions with different inequalities can be handled by intersecting each Pᵢ with the closed rational regions on which those obligations apply, testing all applicable inequalities at overlaps. If an external command bus is disabled in a region, an inconsistent inequality gives C_t(b)=∅ there.

**Theorem (PROVED PAPER).** Whether a record-driven policy guarantees safety by D is decidable with exact rational arithmetic under these hypotheses. Every winning instance admits a finite policy tree with rational terminal commands.

**Proof.** Given the current record and its belief B, first evaluate the robust terminal test. If V is the finite union of the vertex sets of all nonempty Pᵢ, then

\[
 \bigcap_{b\in B} C_t(b)=\bigcap_{v\in V} C_t(v).
\tag{1}
\]

Indeed, for fixed u and each Pᵢ, every b in it is a convex combination of its vertices, and every gₖ(b,u) is the corresponding affine combination. For the opposite inclusion every tested vertex is a compatible joined case. Thus (1) is one system of rational linear inequalities in u. Linear feasibility over the reals for such a system yields a rational feasible solution if nonempty, including unbounded or lower-dimensional feasible regions (for example eliminate variables then back-substitute rational endpoints or any rational between them). If the rows are jointly affine \(g_k=H_k u+J_k b-d_k\), an alternative is to maximize \(J_k b\) separately on each Pᵢ by rational linear programming and use the largest result. These are exact finite reductions of universal safety, with no assumption of exact analog readings by the policy.

A preterminal operation is eligible only if its duration fits and B⊆L. For a convex guard this follows by checking the vertices of every Pᵢ against every guard row. For a guard that is a union, vertex testing against union membership is insufficient. Instead decide emptiness of B∖L by distributing the negated closed inequalities over the finite union and checking the resulting mixed weak/strict rational linear systems (exact elimination may track strictness). The data must ensure total successor availability on L, or certify coverage by projecting the R graphs and checking containment in their union in the same way.

For each reported o form the exact joined belief

\[
 B_{a,o}=\bigcup_{i,j}\mathrm{proj}_{s,x'}\{(s,x,x'):(s,x)\in P_i,\ (s,x,x')\in R_{t,a,o,j}\},
\tag{2}
\]

where j ranges over that output's graph pieces. Intersection and projection of rational polyhedra remain rational polyhedral. For projection, eliminate a coordinate by retaining its zero-coefficient rows and pairing each lower bound with each upper bound. The projected conditions are necessary and sufficient for some admissible value of the forgotten coordinate. Iteration gives precisely the existential image. By the bounded-successor hypothesis each nonempty component of (2) is compact. No step fills the gaps between components. In particular every preimage retaining (s,x) uses that same s on output (s,x′). This is a lawful destructive observation on one copy.

Proceed by backward induction as in W2. A winning immediate terminal test finishes the branch. Otherwise choose a common eligible action for which every nonempty B_{a,o} wins at the new clock. Conversely the first move of any successful policy must meet precisely one of these alternatives. The finite alphabets, finite available operations, finitely many discrete epochs and strictly positive preterminal durations bound the number of finite histories considered, even though there are infinitely many possible hidden values. This gives a terminating algorithm with a finite certificate tree. Replacing the exact measured outcome by a more informative one in (2) would compute the wrong tree. □

## TD-W5. Dimension controls the size of a terminal obstruction

**Theorem (finite Helly certificate, PROVED PAPER).** Fix nonempty B as in W4. If no common terminal command is safe at time t, at most m+1 compatible joined cases suffice to prove it. They can be chosen from V in (1). An infeasible command domain U alone needs no hidden-case witness. A single case with C_t(b)=∅ needs just that case. For nonempty U of affine dimension d one may replace m+1 by d+1. The bound concerns a single **terminal** decision. A losing sequential policy may require distinct obstructions at many decision nodes.

**Proof.** After (1) choose a minimal infeasible subfamily of the finitely many convex sets C_t(v) in ℝᵐ, each already incorporating U. For each i choose uᵢ in the intersection of all other sets of this family, allowing a singleton empty set as a separate case. If there were at least m+2 members, take an affine dependence among the corresponding uᵢ. Its coefficients sum to zero and have both signs. The positive and negative parts, normalized by their common total, give two convex combinations of disjoint groups of witnesses with the same value u. For every i, at least one combination excludes uᵢ; every other witness in that combination belongs to C_t(vᵢ). Convexity forces u into that set, hence into the entire family, a contradiction. This is the finite Helly argument. If U is nonempty, work in its affine hull for the dimension improvement. Enumeration of subsets up to that size and rational LP give an executable witness. □

**Sharp continuum example.** Let Ω=U=Δᵐ, the probability simplex on m+1 coordinates, of affine dimension m. Keep one common readout. The command must satisfy \(u_i\le1-s_i\) for each coordinate i. These are jointly affine inequalities. All m+1 vertex sources eⱼ together force every uⱼ≤0, incompatible with Σuᵢ=1. For any k≤m cases s¹,…,sᵏ the common capacities cᵢ=1−maxⱼ sᵢʲ are nonnegative and satisfy

\[
\sum_i c_i\ge m+1-\sum_{j=1}^k\sum_i s_i^j=m+1-k\ge1.
\]

Fill the capacities to total one to obtain a common simplex command. At m=2, each vertex removes one facet's opposing barycentric coordinate. Any two compatible cases leave a command while the three vertices jointly rule one out. Eliminating the last barycentric coordinate realizes the same triangle in ℝ².

**Bounds and controls.** If compact reachability is removed, the singleton original source can lead after one declared operation to every current state x′≥0. The terminal scalar command u must satisfy u≥x′. Every finite set of hidden pairs has a common command and the entire belief has none. Quantifier elimination can still decide this particular case, while W5's finite witness has failed. If convexity of the per-case command sets is removed, a one-dimensional command chosen from {0,1,2} can have safe sets {0,1}, {1,2}, {0,2}; no two cases witness failure. If a convex guard test is used on a nonconvex guard union, endpoints −1 and 1 can both be legal and midpoint 0 illegal. Each assumption changes a concrete part of the algorithm or certificate.

**Executed example.** Start from the full rational polytope $-1\le s=x\le 1$. A one-bit sensor reports one of the two closed half-intervals (either report at zero), then destroys the state by setting $x'=0$. Require $u\in[-1,1]$ and $|u-s|\le 1/2$ by the deadline. Before observing, the two endpoints force disjoint command intervals. After the report the joined fibers are exactly $[-1,0]\times\{0\}$ and $[0,1]\times\{0\}$, so the unique commands are $-1/2$ and $1/2$. A one-tick sensor and one-tick terminal action succeed at inclusive deadline two. Moving the pulse arrival to tick three makes the same information unusable. The exact probe recovered both joined projections and commands. It checked all 231 unordered pairs with repetition on the denominator-five triangle grid by rational feasibility, and 25 full/deletion feasibility problems for the simplex obstruction at affine dimensions one through five. These counts describe finite controls for the proved all-dimensional result.

**Source and verification.** Finite Helly and Fourier–Motzkin elimination are classical. The contribution is their exact interface to W1/W2, including original/current pairs, adversarial finite reports, deadline, and continuous commands. See [Ziegler's discrete geometry notes, §2.2](https://page.mi.fu-berlin.de/gmziegler/vorlesung/35discregeom_notes.pdf) for the projection step. The [exact finite probe](polyhedral_interception_probe.py) implements elimination and witness lifting for the displayed controls. W4/W5 are paper proofs. The checker covers rational cases, with no claim of scalable policy synthesis or physical calibration.
