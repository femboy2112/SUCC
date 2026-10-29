# Finite resonance tests and bounded searches for local shifted-runner replacements

**Research draft, 28 October 2026. Not submitted. Authorship and submission are reserved for the maintainer.**

## Abstract

Poliakova introduced local uniform replacement rules for shifted Lonely Runner covers. We characterize locality of any finite rule with phases affine in the covering radius by finitely many interval-cover conditions, rational for rational phase coefficients. Failure of a condition produces an actual responsible time at an admissible scale. For a fixed affected even support and a fixed number of odd additions, the added velocities can be compressed into a bounded set without losing locality. Consequently existence of a local rule with prescribed largest affected velocity and prescribed positive gain is decidable by a finite collection of rational linear feasibility problems; real phase coefficients offer no advantage over rational ones. We also classify the rules in the binary/3 ladder with Poliakova's specified phases: its smallest gain-positive rule has largest affected velocity 192 and is her original construction. A compactness argument further shows that arbitrary phase schedules local along unbounded sizes admit rational affine replacements on identical supports. If all affected velocities share one odd part, any such rule requires at least two odd additions per removed speed; this bound is sharp. These results do not produce a new shifted-runner counterexample below 95.

## 1. Definitions and comparison with prior work

For distinct positive integer velocities $v_1,\ldots,v_n$ and real phases $s_i$ modulo one, write
\[
 \gamma(v;s)=\max_{t\in\mathbb R/\mathbb Z}\min_i\|s_i+v_it\|,
 \qquad \|x\|=\min_{k\in\mathbb Z}|x-k|.
\]
A $\delta$-cover has $\gamma(v;s)\le\delta$. A strict shifted counterexample has $\delta<1/(n+1)$. Blanco, Criado and Santos give examples for $5\le n\le17$ [1]; Poliakova proves existence for every $n\ge95$ [2]. Zhang v3 records $18\le n\le94$ as the remaining finite range [3]. These are statements in the inspected primary sources, not a claim of exhaustive bibliographic priority.

We use Poliakova's definitions [2, Definitions 3 and 5]. A rule consists of disjoint finite sets $R,S$ of positive even velocities, a finite set $A$ of distinct positive odd velocities, and phases
\[
 \alpha_v+\beta_v\delta \quad(v\in S\cup A).
\]
Let $Q=R\cup S\ne\varnothing$, $H=S\cup A$, $L=\max Q$, and $g=|R|-|A|$. Initially the velocities are $2,4,\ldots,2N$, all at phase zero, with $\delta=1/(N+1)$. At an admissible odd positive scale $b$, every $qb$ with $q\in Q$ is initially present. Remove $Rb$, rephase $Sb$, and add $Ab$ with the declared phases. Distinctness is preserved because the new velocities are odd.

The runner *responsible* for $t$ is the smallest original even velocity $p\le2N$ with $\|pt\|\le\delta$. Such a runner exists by the circle pigeonhole principle applied to $2t$. A rule is **local** if, whenever an affected runner is responsible, a runner from the same application's $H$ covers $t$. Locality implies cover preservation. Its converse is not assumed: an unaffected larger runner might rescue a failure of locality.

Poliakova's Table 1 already gives the asymptotic coefficient $1/224$ from a gain-two rule with $L=240$ and $P=30$; we do not improve that published coefficient. Her Theorem 7 proves a particular local rule by substituting $qt=k+\delta z$ and checking intervals in $z$. The sufficiency argument below generalizes that proof. The additional assertions are the exact converse, the complete responsible-residue set, bounded compression of odd additions, and a sharp classification within the specified ladder. Ordinary interval-union algorithms are classical; their reimplementation is not a novelty claim. Priority of these additional statements beyond the reviewed primary sources remains open to external review.

## 2. An exact finite characterization

For each $q\in Q$ define
\[
 K_q=\{0\le k<q:\gcd(k,q/2)=1\}.
\]
For $v\in H$ and $k\in K_q$ retain the runner only when
\[
 vk/q+\alpha_v\in\mathbb Z.
\tag{1}
\]
For a retained runner put
\[
 I_{q,k,v}=\{z\in[-1,1]: |(v/q)z+\beta_v|\le1\}.
\tag{2}
\]
These are closed intervals, possibly empty.

**Theorem 1 (finite locality test).** A rule with real coefficients $\alpha_v,\beta_v$ is local for every admissible $N,b$ and every real time if and only if
\[
 [-1,1]=\bigcup_{v\in H:\,(1)}I_{q,k,v}
 \quad\text{for every }q\in Q,\ k\in K_q.
\tag{3}
\]
For rational phase coefficients this is an exact finite rational test with $2\sum_{q\in Q}\varphi(q/2)$ cells. A failing cell yields a rational counterexample to locality at scale $b=1$.

*Proof, sufficiency.* Suppose $qb$ is responsible and write $qbt=k+\delta z$ with $k\in\mathbb Z$ and $|z|\le1$. If $d=\gcd(k,qb/2)>1$, the original even velocity $qb/d<qb$ has distance at most $\delta/d$, contradicting responsibility. Thus $\gcd(k,q/2)=1$. Reducing $k$ modulo $q$ preserves (1). Choose a rescuer supplied by (3). Its position is
\[
 vbt+\alpha_v+\beta_v\delta
 =vk/q+\alpha_v+\delta((v/q)z+\beta_v),
\]
whose distance to an integer is at most $\delta$ by (1) and (2).

*Proof, necessity and effective failure.* Suppose (3) fails at $q,k$. The complement of the finite union of closed intervals is relatively open; for rational coefficients choose a rational $z\in[-1,1]$ in that complement. Set $c_v=(v/q)z+\beta_v$ and $d_v=\|vk/q+\alpha_v\|$. For each earlier even velocity $p<q$, the number $d_p=\|pk/q\|$ is positive: otherwise $q/2$ divides $(p/2)k$, contrary to coprimality. Choose $N\ge L/2$ sufficiently large that $\delta=1/(N+1)$ is smaller than each of the following finitely many positive quantities:
\[
 \frac{d_p}{1+|(p/q)z|},\qquad
 \frac{d_v}{1+|c_v|}\ (d_v>0),\qquad
 \frac1{1+|c_v|}\ (d_v=0).
\tag{4}
\]
For resonant $v$, failure of (2) means $|c_v|>1$. Take $t=(k+\delta z)/q$ modulo one. Then $q$ covers $t$. The distance-to-integer function is 1-Lipschitz, so (4) excludes every earlier even velocity and every nonresonant rescuer. For a resonant rescuer, $\delta<|\delta c_v|<1-\delta$, so it also fails to cover. Therefore $q$ is responsible and no local rescuer covers. All choices are rational when the input coefficients are rational. For real coefficients the same finite-margin argument proves necessity. Finally, the residue count is $|K_q|=2\varphi(q/2)$, including $q=2$. ∎

The gcd is deliberately $\gcd(k,q/2)$, not $\gcd(k,q)$. For example $q=6,k=2$ is a possible responsible residue and must be checked.

## 3. Bounding added velocities and phase coefficients

**Theorem 2 (odd-velocity compression).** Fix $Q$ and suppose a local rule has $m\ge1$ odd additions. Let $M=\operatorname{lcm}(Q)$. There is a local rule with the same even roles and the same gain whose added velocities are distinct positive odd integers strictly below $mM$.

*Proof.* Since $M$ is even, each odd residue class has a representative $r\in\{1,3,\ldots,M-1\}$. Within one such class list the old added velocities increasingly as $v_i=r+q_iM$. Distinctness and positivity imply $q_i\ge i-1$. Replace them by $v'_i=r+(i-1)M\le v_i$, preserving distinctness within and between classes. Their maximum is less than $mM$. Keep $\alpha_i$ and replace $\beta_i$ by $\beta'_i=(v'_i/v_i)\beta_i$. For every affected $q$, $q\mid M$, so the resonance condition (1) is unchanged. Moreover
\[
 (v'_i/q)z+\beta'_i=(v'_i/v_i)((v_i/q)z+\beta_i).
\]
The multiplier lies in $(0,1]$. Every formerly covered tangent point is still covered. Theorem 1 now proves locality at every admissible scale. This argument need not preserve accidental nonresonant coverage at a particular finite $N$; that is unnecessary for locality. ∎

For $m=0$ no compression is needed.

**Theorem 3 (finite rational feasibility).** Fix a positive integer cap $L$ and a positive integer target gain $g$. Existence of a local affine-phase rule with largest affected velocity at most $L$ and gain at least $g$ is decidable by finitely many rational linear feasibility problems. Existence with real phase coefficients is equivalent to existence with rational phase coefficients.

*Proof.* Enumerate the finitely many disjoint roles $R,S$ among the positive even integers at most $L$, excluding empty $Q$. The number $m$ of odd additions satisfies $0\le m\le|R|-g$. Theorem 2 bounds their distinct velocities by $m\operatorname{lcm}(Q)$ when $m>0$, leaving finitely many supports.

For a fixed support, a useful $\alpha_v$ modulo one belongs to the finite rational set
\[
 \{-vk/q\pmod1:q\in Q,\ k\in K_q\}.
\]
If it belongs to no such set, that runner rescues no tangent cell and can be retuned without losing any coverage. Similarly it suffices to impose
\[
 |\beta_v|\le1+v/q_{\min},\qquad q_{\min}=\min Q.
\]
A coefficient outside this range has no interval meeting $[-1,1]$ in any cell and may be reset to zero without losing credited coverage.

Fix the finitely many $\alpha$ choices. Use each untruncated rescue interval with endpoints $a_v=(-1-\beta_v)q/v$ and $b_v=(1-\beta_v)q/v$, which are rational affine functions of $\beta_v$. Intersecting their union with $[-1,1]$ recovers (3). A finite interval family covers $[-1,1]$ exactly when some simple chain has its first interval containing $-1$, its last containing $1$, and consecutive intervals intersecting. Enumerate all such chains. Their conditions are non-strict rational linear inequalities; both directions of each overlap inequality are imposed. Thus (3), over finitely many cells, is a finite union of bounded rational polyhedra. Rational linear feasibility is decidable, and every nonempty rational polyhedron contains a rational point. This proves both assertions. ∎

**Explicit height bound.** For a fixed nonempty rescuer support of size $d$, put $B=\max(L,\max_{v\in H}v)$. If this support admits a local rule, there is a feasible rational phase vector whose $\beta$ coefficients share a denominator $D\le d!B^d$. Each $\alpha$ denominator divides $M=\operatorname{lcm}(Q)$. Indeed, after clearing denominators every chain/polytope constraint has integer coefficient magnitude at most $B$: overlap gives $v_i\beta_j-v_j\beta_i\le v_i+v_j$, and endpoint/box constraints have coefficient at most $L$. A nonempty bounded polyhedron has a vertex with $d$ independent active constraints. Cramer's rule gives a common denominator dividing their nonzero integer determinant, whose absolute value is at most $d!B^d$ by the determinant expansion. This bound is extremely large; no enumeration up to it was performed.

This is an in-principle completeness bound, not an efficient exhaustive search or a claim that the optimum cap has been determined. At this stage it concerns **local** affine-phase rules, not all cover-preserving replacements. Section 5 extends existence to arbitrary phase schedules on fixed finite supports.

## 4. Sharpness within the binary/3 ladder

Fix $J\ge2$. Rephase $3\cdot2^j$ for $2\le j\le J$ by $(1+\delta)/2$, remove $3\cdot2^{J+1}$, and add velocities $3,9$ at phase $1/4$. Each binary velocity $2^h$, $3\le h\le J+1$, is either removed or retained with phase $-\delta$; all remaining original velocities are unchanged. Here $L=3\cdot2^{J+1}$.

**Theorem 4 (complete fixed-phase ladder classification).** Such a rule is local exactly when each removed binary velocity has its immediate doubled successor retained. Equivalently, the binary removal word has no adjacent removals and ends with a retained velocity. Its largest possible gain is
\[
 \left\lfloor\frac{J-1}{2}\right\rfloor-1.
\]
Positive gain first occurs at $J=5$, $L=192$, and that first rule is uniquely Poliakova's Section 3 construction within this family.

*Proof.* For a triple velocity $q=3\cdot2^j$ with $j\ge3$, the half-phase rescuer $q/2$ covers all $z\in[-1,1]$. For $j=2$, the two added odd velocities rescue the two odd residue classes modulo four, exactly as in [2].

For a binary $q=2^h$, every responsible $k$ is odd. The only resonant half-phase triple rescuer is $3q/2$; it covers $z\in[-1,1/3]$. The odd additions do not resonate. A retained binary $2^\ell$ resonates only for $\ell\ge h$, and its $-\delta$ phase covers $[0,2^{1-(\ell-h)}]\cap[-1,1]$. If $q$ is retained, its own interval covers $[0,1]$. If it is removed, covering $z=1$ requires precisely its doubled successor to be retained; larger binaries end before one. These conditions are also sufficient to cover all $[-1,1]$. Theorem 1 gives locality.

Each removal is paired with its distinct immediately following retained position. There are $J-1$ binary positions, so at most $\lfloor(J-1)/2\rfloor$ removals. Alternating removed/retained pairs attain this number. One additional terminal removal and two additions make the gain the number of binary removals minus one. At $J=5$, four binary positions require the unique word removed, retained, removed, retained, giving removals $8,32,192$. ∎

This theorem does not claim that every local rule has $L\ge192$. Other phases, velocity families, or greater gain remain possible.

## 5. Arbitrary phase schedules and a sharp arithmetic obstruction

The affine restriction loses no existence possibilities on fixed finite supports.
The following statement concerns existence of a replacement, not identity with
the input schedule.

**Theorem 5 (affinization on fixed supports).** Fix finite R,S,A as in Section 1.
Suppose arbitrary circle-valued phases are local at scale one along a sequence
of admissible sizes tending to infinity. Then rational affine phases on the
same R,S,A are local at every admissible size and odd scale.

*Proof.* Let the radii be delta_j tending to zero. By compactness of the finite
phase torus, choose one joint subsequence converging to alpha. Signed local
lifts epsilon_vj of the phase errors tend to zero. By compactness of a finite
product of extended real lines, pass to a further joint subsequence for which
epsilon_vj/delta_j tends to beta_v, finite or infinite, for every label v.

Fix any responsible residue cell (q,k,z), with gcd(k,q/2)=1 and z in [-1,1].
At t_j=(k+delta_j*z)/q modulo one, q is actually responsible eventually:
every earlier even p has pk/q nonintegral and stays outside the shrinking
bad neighborhood. A nonresonant limiting phase cannot rescue these times.
For a resonant label with infinite beta_v, its residual tends to zero while
its absolute value divided by delta_j tends to infinity; it eventually lies
strictly between delta_j and 1/2. A finite beta_v with
abs((v/q)*z+beta_v)>1 likewise fails eventually. If no finite beta_v covered
this cell, all finitely many labels would fail, a contradiction. This uses
one fixed limiting vector for every cell, without an uncountable diagonal
selection. Reset unused infinite beta entries to zero. Theorem 1 supplies
all-size, all-scale locality for the resulting real affine rule. The
fixed-support rationalization in Theorem 3 makes its coefficients rational
without changing velocities or roles. ∎

Thus Theorem 3 also decides existence of local rules with arbitrary phase
schedules. This does not yield an effective limit-extraction algorithm for a
given schedule. Alternating phases 3/4+delta/8 and 1/4-delta/8 on additions
d,3d, with removal 4d and odd d, give a local schedule with two distinct
circle limits. No fixed affine schedule agrees with it eventually.

**Theorem 6 (one odd part cannot save runners).** Suppose all affected
velocities belong to {d*2^a:a>=1}, for one fixed positive odd integer d.
Any local rule, even with arbitrary phase schedules along unbounded sizes,
satisfies |A|>=2|R|. The coefficient 2 is sharp for every d.

*Proof.* Apply Theorem 5 to reduce to affine phases. Give each endpoint of
each responsible residue cell (q,k,z=+-1) weight 1/(2*|K_q|). The total
required endpoint mass is |Q|. Let E(v) be the total mass covered by an
exactly resonant rescuer v. Locality implies |Q|<=sum_v E(v).

For a rephased v=d*2^b with alpha_v=0 modulo one, resonance occurs exactly
at affected q<=v. Its capacity is half the number of distinct signed powers
of two lying in one interval of length 2 centered at -beta_v. That interval
contains at most two such numbers, so E(v)<=1. If alpha_v is nonzero,
resonance can occur only at q=d*2^a with a>b, and forces its reduced
denominator to be exactly 2^(a-b). This singles out at most one q, again
giving E(v)<=1.

For any odd added v, resonance at q=d*2^a with a>=2 forces alpha_v's reduced
denominator to have exact 2-adic order a; at a=1 that order is 0 or 1.
Thus an odd v resonates at at most one q. The fixed-point-free involution
k -> k+q/2 modulo q preserves K_q and changes vk/q by a half-integer.
At most half the residues resonate, so E(v)<=1/2. This includes q=2d;
discarding its even responsible residues would invalidate the argument.
Consequently |R|+|S|<=|S|+|A|/2, proving the inequality.

For sharpness remove 4d, add d and 3d, and give both phase 3/4. The two
added runners rescue the two odd residue classes modulo four, with tangent
slopes 1/4 and 3/4. Theorem 1 gives locality, with |A|=2|R|. ∎

The same-odd-part hypothesis is necessary for this conclusion: Poliakova's
rule uses odd parts 1 and 3 and has positive gain. Its rescuer v=12 has
endpoint capacity 3/2, pinpointing the failure of the even-rescuer bound.
Full quantifiers, limit details, exact controls and priority boundaries are
recorded in AFFINIZATION.md and OBSTRUCTION.md. These remain paper proofs;
compactness and elementary counting are standard tools, and academic priority
of this application is not certified by the present search.

## 6. Exact and formal verification

The rule checker enumerates every responsible residue and performs rational interval unions. For Poliakova's rule it checks 184 cells, independent of $N$ and scale. A separate source-labelled circle-cover generator and integer-only checker reproduce known examples with 5, 13, and 95 runners; the 95-runner concrete certificate has 5,225 intervals. This distinction is the mathematical advantage of the local characterization: one finite proof covers every admissible scale, rather than certifying a sampled collection of times.

The independent circle checker recomputes each endpoint from its original velocity, phase, radius, and integer winding before accepting a chain from zero to one. Its soundness and finite-breakpoint completeness proofs are in `CERTIFICATE_THEOREM.md`. A SHA-256 digest binds data but proves no mathematical statement on its own. Independent exact lower-envelope evaluation reproduces the published five-runner optimum $15/94$.

Lean 4.14 checks the universal deleted-speed lower-bound witness from the companion Alpha note, the full upper-half one-insertion hole theorem from Gamma, full real-time interval-chain soundness, and the all-length combinatorial packing inequality used in Theorem 4. Theorems 1–3, 5–6 and the analytic identification of the ladder pattern remain paper proofs. The Python parser and concrete JSON fixtures are not certified by Lean. Kernel exports and deliberately false controls delimit the formal authority precisely. Same-model agent reviews are correlated review, not independent external peer review.

## 7. Limits and next experiments

No new strict shifted counterexample for $18\le n\le94$ is asserted here. Restricted-menu solver timeouts or UNSAT reports do not prove the complete finite problem in Theorem 3 infeasible. The fixed-phase ladder obstruction indicates a precise next experiment: change phase families or arithmetic velocity support, rather than merely shortening the same ladder. An independently checked rule with $L/2-g\le94$ would extend the established shifted range.

## References

[1] M. Blanco, F. Criado, F. Santos, *Coloopless zonotopes and counterexamples to the Shifted Lonely Runner Conjecture*, [arXiv:2603.24784v4](https://arxiv.org/abs/2603.24784v4), 24 October 2026. Published-control data also appear in the authors' companion repository; no implementation was copied.

[2] D. Poliakova, *More (shifted) runners, less loneliness*, [arXiv:2609.23952v1](https://arxiv.org/html/2609.23952v1), September 2026, Definitions 3 and 5, Proposition 4, Theorems 6 and 7, and Table 1.

[3] Y. Zhang, *Tight instances of the Lonely Runner Conjecture: one-entry modifications and the growth of speeds*, [arXiv:2608.13599v3](https://arxiv.org/html/2608.13599v3), 18 October 2026, Section 8 and Appendix A.

[4] D. D.-F. Liu, *From rainbow to the lonely runner: a survey on coloring parameters of distance graphs*, Taiwanese Journal of Mathematics 12 (2008), 851–871, [doi:10.11650/twjm/1500404981](https://doi.org/10.11650/twjm/1500404981). Used for the separate deleted-speed priority audit, not for the new local-rule converse.

## Reproducibility appendix

From the repository root run `python -m unittest discover -s tests -p 'test_lonely_runner_*.py'`, `python scripts/lonely_runner_certificates.py --output /tmp/lonely-controls`, and the independent `scripts/verify_lonely_runner.py` on each generated cover. The pinned kernel runner is `scripts/check_lonely_runner_lean.py`; its explicit dependency-project option permits a read-only compatible mathlib cache. Raw tests, search scopes, failed controls, kernel receipts, source pins, and final hosted runs are recorded separately in the campaign validation files. No external submission or author contact has taken place.
