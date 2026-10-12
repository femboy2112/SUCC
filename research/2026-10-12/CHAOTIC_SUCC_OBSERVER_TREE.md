# Chaotic SUCC: an origin-rooted observer tree over the logistic map

**Research offshoot (2026-10-12).** Base: `femboy2112/SUCC`, commit `583ef6b605d6fc47654e571ea43caaa05c016a12`, the tip of the [dual E-boundary tower PR #29](https://github.com/femboy2112/SUCC/pull/29), itself stacked on [shared carrier #28](https://github.com/femboy2112/SUCC/pull/28), [independent gluing #27](https://github.com/femboy2112/SUCC/pull/27), and [diagonal E ladder #26](https://github.com/femboy2112/SUCC/pull/26). Original proposal: attach the SUCC rooted E/dual-observer ladders to a deterministic logistic bifurcation, replace a ladder with a branching tree, and ask whether E can understand a chaotic frontier through a non-chaotic quotient. **Classification:** classical ergodic/symbolic-dynamical facts with new-to-SUCC source-typed implementations, local exact proofs, adversarial tests and an obstruction. No academic priority, RH result, physical-transfinite realization or empirical measurement claim.

## 1. Steelman, source, types and decisive distinctions

A genuine version of the intuition keeps the **same underlying dynamical carrier** for every E node, keeps a lawful report provenance, and distinguishes four outputs:

* *Trajectory state* \(x_t\) and full symbolic source path, which exhibit deterministic chaos at \(r=4\) for typical sources.
* *Set of possible pasts* of a declared terminal state \(y\): a binary inverse-image tree. This is an **epistemic tree**, not 2^n physically realized parallel trajectories.
* *Model/aggregate* \(\mathcal L^n g(y)\), a conditional average over the complete inverse tree of an observable \(g\), with declared equal branch weights arising from a specific invariant measure.
* *Dual source join* of a chronological left/right branch receipt and a same-source terminal state. It reconstructs one source, provided both records are genuine. Identity strings alone are not physical attestation.

**Critical origin distinction:** E is rooted at the origin of the *observation/history diagram*, not at the physical phase point \(x_0=0\). The latter is a fixed point of the logistic map at \(r=4\) and would make the proposed chaos experiment trivial.

Let \(X=[0,1]\), \(f(x)=4x(1-x)\), \(\Theta=[0,1]\), and

\[
T(\theta)=\begin{cases}2\theta,&\theta\le\frac12,\\2-2\theta,&\theta\ge\frac12,\end{cases}\qquad
h(\theta)=\sin^2\frac{\pi\theta}{2}.
\]

The strictly increasing homeomorphism \(h:\Theta\to X\) satisfies \(f\circ h=h\circ T\), verified directly with \(4\sin^2a\cos^2a=\sin^2(2a)\), including the tent folding symmetry. Thus all exact rational *symbolic* checks run in \(\Theta\); exact polynomial transfer calculations run in \(X\). One must not treat these two coordinate frames as automatically identical without \(h\).

Under Lebesgue \(d\theta\), \(T\) is invariant and the two branches each have conditional mass 1/2. The induced invariant law on \(X\) is the **arcsine measure**

\[
  d\mu(x)=\frac{dx}{\pi\sqrt{x(1-x)}} \quad (0<x<1).
\]

It has moments \(\int_0^1 x^k\,d\mu=\binom{2k}{k}/4^k\). This is an *assumed/derived mathematical stationary ensemble*, not a universally justified prior for other logistic parameters or real sensors.

## 2. CT1 — exact binary symbolic observer tree (CLASSICAL / PROVED LOCAL)

The two inverse tent branches are \(b_0(y)=y/2\) and \(b_1(y)=1-y/2\). For a chronological history word \(w=(s_0,\dots,s_{n-1})\in\{0,1\}^n\), set

\[
  I_w=b_{s_0}\circ\cdots\circ b_{s_{n-1}}([0,1]).
\]

These \(2^n\) cylinders partition \([0,1]\) up to shared endpoints, each has length and Lebesgue mass \(2^{-n}\), and \(T^n\) maps each cylinder *affinely and surjectively* onto \([0,1]\). The itinerary bits are independent fair Bernoulli symbols with respect to Lebesgue; the map is deterministic for each fully specified state. Exclude the critical/binary boundary ties from unique symbolic decoding; they have measure zero.

The prior \(n\) history bits restrict \(\theta_0\) to \(I_w\), but at steps \(t\ge n\), the image of this entire cylinder again fills \([0,1]\). Conditional on the prefix and the declared stationary prior, \(\theta_t\) is uniform for \(t\ge n\). Exact tests enumerate every word through depth 9 and verify independent forward itinerary reconstruction. **At depth n there are 2^n possible histories and exactly n bits of joint history entropy.** Describing the law is not the same as recovering an individual path.

## 3. CT2 — exact inverse-tree annihilation of polynomial frontier dependence (CLASSICAL / PROVED LOCAL)

At the logistic stage write the inverse branches

\[
  a_\pm(y)=\frac{1\pm\sqrt{1-y}}2,
  \qquad \mathcal Lg(y)=\frac{g(a_-(y))+g(a_+(y))}{2}.
\]

Here \(\mathcal Lg(y)=\mathbb E_\mu[g(X_0)\mid X_1=y]\) for a stationary \(X_0\sim\mu\), and \(\mathcal L^n g(y)\) is the equal-weight depth-n inverse-tree average. The average is over **all mathematical predecessor branches**, not a selected physical history.

The roots have \(a_++a_-=1\), \(a_+a_-=y/4\). Therefore their power sums \(S_k=a_+^k+a_-^k\) obey the exact recurrence

\[
  S_0=2,\quad S_1=1,\quad S_k=S_{k-1}-\frac y4 S_{k-2}.
\]

It follows immediately that \(\mathcal L:\mathbb Q[x]_{\le d}\to\mathbb Q[y]_{\le\lfloor d/2\rfloor}\). Thus for every polynomial \(g\) of degree \(d\),

\[
 \boxed{\mathcal L^n g\equiv\int g\,d\mu\quad\text{whenever }2^n>d.}\tag{CT2}
\]

Constancy follows after repeated degree halving; the constant equals the invariant integral since \(\int\mathcal Lg\,d\mu=\int g\,d\mu\). The integer depth \(n=d.\mathrm{bit\_length}()\) is sufficient, though not necessarily minimal for every polynomial. Calibration:

\[
\mathcal Lx=\tfrac12,\quad
\mathcal Lx^2=\tfrac12-\tfrac14y,\quad
\mathcal L^2x^2=\tfrac38,\quad
\mathcal L^2x^3=\tfrac5{16},\quad
\mathcal L^3x^4=\tfrac{35}{128}.
\]

**Chebyshev diagonal/halving basis:** define \(C_k(x)=T_k(1-2x)\), with \(T_k\) the degree-k Chebyshev polynomial (not the tent map). Because the two predecessor values of \(1-2x\) are \(\pm\sqrt{1-y}\),

\[
 \boxed{\mathcal L C_{2k}=C_k,\qquad \mathcal L C_{2k+1}=0\quad(k\ge0),}\tag{CT2b}
\]

and \(\mathcal LC_0=C_0\). Every nonzero-frequency Chebyshev mode is killed after \(\nu_2(k)+1\) inverse layers. *This is an exact finite-degree filtration, not an elimination of the dynamical entropy of the carrier.*

## 4. CT3 — uniform stabilization for continuous observables (CLASSICAL / PROVED LOCAL)

Because polynomials are dense in \(C[0,1]\), and \(\mathcal L\) is a positive sup-norm contraction, CT2 implies

\[
  \boxed{\lim_{n\to\infty}\sup_{y\in[0,1]}
       |\mathcal L^ng(y)-\mu(g)|=0\quad \forall g\in C([0,1]).}\tag{CT3}
\]

**Proof:** given \(\varepsilon>0\), choose polynomial \(p\) with \(\lVert g-p\rVert_\infty<\varepsilon\). For \(n\) beyond its finite annihilation depth, \(\mathcal L^np=\mu(p)\). Hence \(\lVert\mathcal L^ng-\mu(g)\rVert_\infty<2\varepsilon\).

**Quantitative conditional bound.** If \(g\) is Lipschitz on \(X\) with verified constant \(L_x\), then \(G=g\circ h\) is Lipschitz on \(\Theta\) with \(L_\theta\le(\pi/2)L_x\). Couple every inverse cylinder sample \(b_w(\theta)\) with a uniform point \(b_w(U)\), \(U\sim\mathrm{Uniform}[0,1]\). The latter, mixed over all words, has exactly Lebesgue law. Each branch shrinks distances by \(2^{-n}\), so

\[
|\mathcal L^ng(h(\theta))-\mu(g)|
 \le L_\theta 2^{-n}\int_0^1|\theta-u|du
 \le \boxed{\pi L_x\,2^{-n-2}}.\tag{CT3b}
\]

The implementation records the **exact rational coefficient of \(\pi\)** in this analytic upper bound; it does not pretend a floating-point \(\pi\) calculation is a rigorous interval certificate. Rates are conditional on the source's declared regularity. CT3 is uniform over terminals, not over all observables or unknown source laws. For a discontinuous set-indicator supported on a single endpoint's entire countable backwards orbit, exceptional terminal behavior can persist and uniform convergence need not hold.

## 5. CT4 — the forward-changing target exactly defeats matched-depth completion (CLASSICAL / PROVED LOCAL)

Define the Koopman operator \(Ug=g\circ f\). Since both inverse branches map to the same endpoint, \(\mathcal L(Ug)=g\) for **every** bounded observable and, by iteration, \(\mathcal L^nU^ng=g\). In particular, choosing \(g(x)=x\) gives

\[
\boxed{\deg(U^nx)=2^n,\qquad
\mathcal L^n U^nx=x,\qquad
\mathcal L^{n+1}U^nx=\tfrac12.}\tag{CT4}
\]

For each *frozen* target \(U^nx\), an additional level yields exact constancy, but at every aligned stage \(n\) the advancing target retains a nonconstant dependence. Equivalent Chebyshev test: \(\mathcal L^n C_{2^n}=C_1\ne0\), yet \(\mathcal L^{n+1}C_{2^n}=0\). This is a precise *rate-matched observational debt* example for the SUCC proof-backaction/Zeno program—not a claim of an actual infinitely fast physical process, unprovability or any obstruction against deciding a fixed finite-degree target.

## 6. CT5 — source-typed dual E gluing preserves the forgotten branch (CLASSICAL / PROVED LOCAL)

Let the original-source object be identified by an explicit `(source_id,version)` contract. The earlier observer E supplies a chronological word \(w\) of length \(n\); the opposing observer E'' supplies \(\theta_n\in(0,1)\) as an exact rational terminal report at causal step \(n\). Requiring matching source/version and time yields the unique reconstructed

\[
  \boxed{\theta_0=b_{s_0}\circ\cdots\circ b_{s_{n-1}}(\theta_n).}\tag{CT5}
\]

The independently replayed tent orbit verifies the word and endpoint. Each side alone is insufficient: the terminal has \(2^n\) generic preimages, and the word alone only gives a \(2^{-n}\)-length cylinder. With an interval terminal report \(\theta_n\in[a,b]\subset(0,1)\), the reconstructed original-state interval is exactly \((b-a)/2^n\) wide, by affine inverse-branch composition.

**Epistemic/physical gate:** signed source **metadata** are mathematical contracts, not authentication. A forged alternative branch word with the *same source string* can also glue to the same terminal and reconstruct a different past. Genuine physical causal testimony and an independent early-state holdout are necessary to identify the actual past. This explicitly preserves SUCC DB1/DB3 and SC1/SC3 distinctions: information join is meaningful, agreement of declared IDs alone is not.

## 7. CT6 — a stable report is not a lossless chaotic factor (REFUTED AS INFERENCE)

At depth \(n\), a constant E report has one value and aliases all \(2^n\) equiprobable history words. It contains 0 bits *about that history*; the unresolved history entropy is exactly \(n\) bits. If a report preserves only the first \(k\) history bits, it has \(2^k\) labels with fibers of size \(2^{n-k}\); its exact bit budget is \(k\) reported versus \(n-k\) unresolved. This is a combinatorial history projection, **not** a time-equivariant deterministic state factor \(q\) with \(q\circ f=F\circ q\).

Indeed the one-bit phase partition fails to close deterministically: \(\theta=1/8\) and \(\theta=3/8\) have the same current half-label but tent successors \(1/4\) and \(3/4\) have different half-labels. Likewise the tree transfer \(\mathcal L\) is **not multiplicative**:

\[
 \mathcal L(x^2)-\bigl(\mathcal Lx\bigr)^2
       =\frac{1-y}{4}\ne0\quad(0\le y<1).\tag{CT6}
\]

The positive conditional variance proves branch identity was discarded. In ergodic-theoretic language, the stationary \(r=4\) logistic system is measurably a one-sided fair Bernoulli shift (outside null itinerary ambiguities), and nontrivial Bernoulli factors have positive Kolmogorov–Sinai entropy; there is no nontrivial **zero-entropy deterministic dynamical factor** of this system modulo \(\mu\). The constant statistical-law report is instead a **measure/observable-level quotient**, not such a source-state factor. See the references below; numerical tests alone do not prove complete positive entropy.

**Counterexample to an even cheaper shortcut:** Adjacent physical states have *zero covariance* under \(\mu\) although \(X_{t+1}=4X_t(1-X_t)\) is deterministic. Exact arcsine moments give \(\mathbb E X=1/2\), \(\mathbb E X^2=3/8\), \(\mathbb E X^3=5/16\), and \(\mathbb E[X_tX_{t+1}]=1/4\), hence \(\mathrm{Cov}(X_t,X_{t+1})=0\). **Zero covariance does not imply independence**, nor missing causal structure.

## 8. CT7 — bifurcation and source-mutation controls

The solved inverse branch and stationary law above are **special to r=4**. For general \(f_r(x)=rx(1-x)\), the maximum image is \(r/4\), so full two-branch preimages of *every* \(y\in[0,1]\) fail whenever \(r<4\). As a positive ordered control, for rational \(r=16/5=3.2\) the nontrivial period-two points are

\[
 x_\pm=\frac{21\pm\sqrt{21}}{32},\qquad
 (f_r^2)'(x_\pm)=-r^2+2r+4=\frac4{25}.
\]

The derivative magnitude is below 1: this cycle is attracting. At \(r=4\), the period-two multiplier is \(-4\), so that particular cycle is repelling, while the full tent conjugacy gives positive invariant-measure entropy \(\log2\). This comparison **does not** classify every parameter in between: period windows and kneading constraints matter. In particular, "all r beyond the period-doubling accumulation" is not a safe synonym for chaos. See [kneading theory](https://www.scholarpedia.org/article/Kneading_theory).

**Required mutation controls:** remove one child, assign unequal inverse-branch weights, conflate observer-history origin with \(x_0=0\), substitute a different \(r\), lie about original source/version, omit the causal path label, infer independence from zero covariance, silently collapse a future-changing target to a fixed target, or claim a physical measurement from a mathematical source identity. Each mutation has a direct algebraic counterexample or an explicitly UNVERIFIED access gate.

## 9. What is now answered—and the next verdict-changing probes

| Question | Verdict with scope |
| --- | --- |
| Can E have a stable non-chaotic view while frontier dynamics is chaotic? | **YES** for the stationary ensemble and complete inverse-tree polynomial/continuous aggregation, at \(r=4\), with specified weights and observable regularity. |
| Can a polynomial frontier observable become exactly independent of terminal state in finite tree depth? | **YES**, after \(2^n>\deg g\). |
| Can E and E'' reconstruct an actual path from complementary history/endpoint data? | **YES mathematically**, when source reports are genuine; source authenticity **UNVERIFIED**. |
| Does this remove the positive path entropy or predict the actual next symbol from a finite past? | **NO**. It discards branch identity; future symbols remain fair under the invariant ensemble. |
| Can fixed-tree depth always finish targets that get harder with the frontier? | **NO**, by the exact \(\mathcal L^nU^nx=x\) matched-debt family. |
| Can this be transported uniformly over the logistic bifurcation diagram or actual measurement systems? | **UNVERIFIED**; kneading/branch weights/continuity/access may change. |
| Do these claims identify an Archimedean arithmetic place, prove RH, or create physical exponential computation? | **NO**; no such interface constructed. |

**Next experiments, in falsification order:** (1) use genuine source-labelled finite partitions for \(r<4\), with kneading-admissible paths and calibrated conditional branch probabilities rather than silently assuming 2^n equal-weight leaves; (2) add sensor noise and limited physical source attestations, measure how dual-E gluing fails when the reported path and terminal come from different actual sources; (3) characterize a **nonconstant** observer report whose autonomous dynamics has lower entropy, paying for any lost predictive target classes explicitly; (4) mechanize the Chebyshev transfer identity and \(\mathcal L^n U^n=I\) in an independent proof assistant, not merely another same-language implementation; (5) compare exact certificate sizes and rate-matched moving-goal debt against the existing [SUCC backaction track](../2026-10-11/PROOF_BACKACTION_DEBT_ZENO.md).

## 10. Reproduction, provenance, and external mathematical precedents

Run `python -m unittest tests.test_logistic_observer_tree` (or unittest discovery), and `python scripts/logistic_observer_tree_probe.py`. Compare its JSON with `research/2026-10-12/LOGISTIC_TREE_RECEIPT.json`. The tests include full exact cylinder enumeration, 400 seeded rational polynomial holdouts, exact Chebyshev chain checks, independently derived numerical trigonometric branch-averaging diagnostics, exact moving-target controls, period-two algebra, missing-branch/weight controls and same-ID forged-path controls. Floating diagnostics are explicitly **not** used as formal certificates.

Primary constructions and classical background:

* Logistic at 4 and the exact tent conjugacy, Lyapunov exponent \(\log2\): [Lyapax exact analytic controls](https://lyapax.readthedocs.io/en/stable/auto_examples/02_chaotic_maps.html); the conjugacy is also derived directly above.
* Kneading admissibility and changing entropy of interval maps: [Scholarpedia, *Kneading theory*](https://www.scholarpedia.org/article/Kneading_theory), including semi-conjugacy to piecewise-linear maps.
* Bernoulli, K-property, and absence of nontrivial zero-entropy factors: [*Some Recent Developments in Structural Ergodic Theory*, SIAM/ICM 2026](https://epubs.siam.org/doi/10.1137/25M1805564); the local polynomial theorem does not require this external classification.
* SUCC inherited source/observer constraints: [shared-carrier SC1–SC7](SHARED_CARRIER_BOUNDARY_DESCENT.md), [dual observers DB1–DB7](DUAL_BOUNDARY_OBSERVER_CORRELATION.md), and [state-changing proof-support/Zeno](../2026-10-11/PROOF_BACKACTION_DEBT_ZENO.md).

**Claim ledger:** CT1–CT7 above map to new entries O321–O332 on this research branch. Proven local statements are derived from classical mathematics, not claimed as research-priority discoveries. The physical chaotic measurement protocol, nontrivial zero-entropy state-factor construction, full bifurcation-parameter transport and arithmetic/RH adapter remain genuinely unverified or obstructed as specified.