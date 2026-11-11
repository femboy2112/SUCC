# H-01–H-08: finite-height Farey shields and effective Dedekind–Yoneda

**Status:** PROVED PAPER under explicit classical source and irrationality hypotheses; the code is a finite exact-rational calibration. This note extends SUCC draft #595, itself a continuation of #594; it does not alter existing source/provenance or advance hexadecimal normality/RH.

## H-01. The precise object and hypothesis firewall

Fix an irrational real `x` strictly within the rational Farey bracket `[3,4]`. An *authenticated interval name* is a finite program that, upon refinement stage `s`, returns rational numbers `l_s < x < u_s`, with widths tending to zero, and for which every stage terminates. (Monotone nesting is convenient but not needed for the central productivity argument.) The program must have a mathematical proof that its names enclose the intended **source-selected** real. The statement `x is irrational` is a separate prerequisite and not derived from finite computation traces.

SUCC currently has two names for `x=pi`:

* **Euclidean circle-beta name:** let `W_0=1`, `W_(k+1)=W_k*(k+1)/(2k+3)` and `S_k=2*sum_(n<k) W_n`. The strict rational enclosure is `[S_k+3W_k, S_k+4W_k]`. Its geometric source is `pi=4 integral_0^1 (1+t^2)^(-1) dt`, derived from the Euclidean arc-length metric of the circle; the accepted source proof is on PR #595. Width `W_k < 2^(-k)` for positive k.
* **Original BBP four-pole name:** for `j>=1`, `r(j)=4/(8j-7)-2/(8j-4)-1/(8j-3)-1/(8j-2)` and `P_k=sum_(j=1)^k 16^(1-j) r(j)`. The *literal zero-seed* completed identity is `pi=sum_(j>=1)16^(1-j)r(j)` (classical BBP identity). By the source's positive, decreasing moment sequence, for k>=1, `P_k<pi<P_k+16^(1-k)r(k+1)/15`.

Both names are exact rational algorithms. The common semantic identification with geometric pi and pi irrationality are mathematical imports; numerical agreement of finitely many stages cannot itself establish them. There is **no pi constant, float, or digit oracle** in the implementation.

## H-02. Farey denominator barrier (classical, proved)

Let `a/b < c/d` with positive integer denominators and `bc-ad=1`. Every reduced rational `p/q` strictly between these endpoints satisfies

`q = d(bp-aq)+b(cq-dp) >= d+b`,

because `bp-aq` and `cq-dp` are positive integers. In fact the mediant `(a+c)/(b+d)` uniquely attains equality `q=b+d`; every other internal reduced rational has strictly larger denominator. This classical lemma is the load-bearing **global finite inference**: one rational bracket can settle infinitely many individually possible questions, including a finite denominator-bounded family.

## H-03. Uniform finite-height separation theorem (PROVED PAPER)

Fix an integer H>=1 and the source-certified irrational x in (3,4). Starting at the adjacent Farey bracket `[3/1,4/1]`, run the Stern–Brocot comparison algorithm, replacing the upper endpoint on L and the lower on R. Stop as soon as `b+d>H`.

**Theorem.** (i) Every arrow decision terminates after a finite amount of source refinement. (ii) The algorithm stops after at most `max(0,H-1)` individual L/R arrows. (iii) The resulting bracket contains x strictly but no rational of reduced denominator <=H strictly inside. (iv) A further finite refinement obtains a rational source interval `(l,u)` strictly inside `(a/b,c/d)`. The rational number

`delta_H=min(l-a/b, c/d-u)>0`

therefore satisfies **simultaneously for every** rational p/q with q<=H:

`|x-p/q| > delta_H`.

**Proof.** Each candidate mediant is rational. Irrationality gives `x!=mediant`; shrinking source intervals eventually separate it from that mediant, so every selected arrow is well-defined and computable. Farey determinant remains 1. An L step increases `b+d` by b>=1, and an R step increases it by d>=1. Initially b+d=2, so at most H-1 arrows suffice. By H-02, no rational denominator q<=H occurs strictly between the final endpoints. Since the source interval shrinks to x lying strictly between fixed rational endpoints, eventually `a/b<l<x<u<c/d`. Every q<=H is <=a/b or >=c/d, so `|x-p/q|>delta_H`, using strict inequalities. All computations and comparisons are finite at that H. QED.

**Do not confuse complexities.** There is a universal <=H-1 bound on *output arrow count* from this starting bracket. It is **not** a bound on integer sizes, source refinement stages, or wall-clock time uniform over all possible irrational inputs. The algorithm determines its own per-H precision; no closed-form polynomial irrationality measure for pi has been established.

## H-04. The whole bounded-denominator cut at once

Let `Q_H` be the **finite** ordered set of reduced rationals `q in [3,4]` whose denominator is <=H, viewed as a thin category. The finite subterminal presheaf `Y_(x,H)(q)={*}` exactly when `q<x` is determined by the height-H Farey shield **without querying its elements individually**. For q<=a/b the answer is true; for q>=c/d false; the barrier proves there is no third case. The root `[3,4]` handles all probes outside.

For H<=K, the restrictions are natural and exactly coherent:

`Y_(x,K)|_(Q_H) = Y_(x,H)`.

The rational-probe categories exhaust all rationals in `[3,4]` as H grows. Their compatible inverse-limit family reconstructs the full Dedekind lower-cut presheaf (and hence x under rational density). Thus the *finite computations* and *the completed Yoneda observer* are linked by a literal comparison-preserving family of finite functors. One cannot infer from this that x is normal in any radix, or that a finite cut prefix contains an infinite theorem independent of the source and hypotheses.

## H-05. Accelerated Euclidean arrows (exact)

For a Farey bracket containing x, set `U(x)=bx-a>0` and `V(x)=c-dx>0`. One R arrow replaces `(U,V)` by `(U-V,V)`; one L arrow replaces it by `(U,V-U)`. A maximal R run has length `floor(U/V)` and a maximal L run has length `floor(V/U)`; irrationality excludes exact integral quotient ties, because `(U/V)=k` would force `x=(a+kc)/(b+kd) in Q`. A k-run acts by integer shears:

`R^k: (a,b,c,d)->(a+kc,b+kd,c,d)`;

`L^k: (a,b,c,d)->(a,b,c+ka,d+kb)`.

On a source interval `l<x<u` wholly inside the Farey bracket, the R quotient is strictly increasing and satisfies

`(bl-a)/(c-dl) < U(x)/V(x) < (bu-a)/(c-du)`.

The L quotient is strictly decreasing with bounds `(c-du)/(bu-a) < V(x)/U(x) < (c-dl)/(bl-a)`. Integer comparisons on these rational endpoint quotients certify a whole run in one finite check. To finish an H shield, the implementation may commit **only the number of steps needed to cross b+d>H**, without proving where that longer run eventually ends. A complete-run certificate also bounds the actual quotient from above by k+1. The witness has an exact source interval, clock, arrow orientation, count, prior/final Farey matrices, and quotient bounds. A separate replay checker rejects detached source stages, malformed arithmetic, and forged margins.

The numeric-arrow interpretation is an equality between *expanded one-arrow paths* and *one run macro arrow*, not an unproved equivalence of arbitrary lambda computation semantics.

## H-06. Nonuniform input separation of any two computably named reals

Given two provably shrinking exact rational interval names of values x,y with x!=y, running their stages in parallel eventually yields disjoint intervals. Their rational midpoint q in the gap witnesses a different Dedekind probe: q lies strictly between x and y. This is semidecision of disequality. If x=y, the procedure need never halt, and arbitrary computable-real equality is **not** generally decidable.

For rational comparison with pi, the separate classical irrationality theorem guarantees every fixed rational candidate eventually separates. For height H, H-03 strengthens the separate pointwise statement to a **single computed certificate for all denominator<=H candidates at once**.

## H-07. Hostile nonnormal irrational; normality firewall (PROVED CONTROL)

Take `z=3+sum_(j>=1)16^(-j!)`. It lies in (3,4). Its base-16 digits are 1 at factorial indices and 0 elsewhere. These positions grow with arbitrarily long gaps, so the digit sequence is not eventually periodic and z is irrational. The asymptotic frequency of digit 1 is zero; therefore z is **not normal** in base 16. Nevertheless z has a computable strict rational interval name: its k-th partial sum is a lower bound and the omitted tail is strictly below `(16/15)*16^(-(k+1)!)`. Consequently z satisfies the entire height-H shield theorem, including finite arrow-productivity, certified positive separation margin and coherent rational Yoneda reconstruction.

This falsifies any claim that total finite rational separation, categorical reconstruction, and infinite correct arrow production alone prove statistical equidistribution. The authentic original-zero signed estimate is still required, and #591/#593 hostile joined-orbit models remain further controls.

## H-08. Next verdict-changing research test

Transport the exact H-dependent cut/carry witnesses through SUCC's signed Fourier/Haar observer, preserving the original four-pole source, literal U_0=0, full integer winding, exact real tail and old prime powers. Seek an inequality that separates the genuine source from the sparse nonnormal source and the coherent zero-phase wrong seed. Do **not** declare signed decay on the basis of the existence or productivity of a cut/name compiler. The finite height shield is a **phi-resolved** reconstruction result; the sigma-/arithmetic cancellation front remains OPEN.

**Source notes:** classical Farey gap theorem appears in the 2025 Bulletin of Symbolic Logic article *On Representations of Irrational Numbers and the Computational Complexity of Converting Between Such Representations* (Theorem 2.2; https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/on-representations-of-irrational-numbers-and-the-computational-complexity-of-converting-between-such-representations/03C51E2D8F12D418A48E4B58B51FF91C). SUCC's original circle/line and BBP source references: PR #595 and #594; classical mathematical facts are not claimed as SUCC novelties.
