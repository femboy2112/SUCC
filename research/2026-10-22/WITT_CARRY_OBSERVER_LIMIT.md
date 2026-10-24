# SUCC — Witt carry, dual shadows, and learning geometry in the inverse limit

**Research date:** 2026-10-22. **Stacked on** `research/observation-pinned-intrinsic-geometry-2026-10-22@adf663f1523b28b51789859e0cc24169bfb5e7e5` (PR #238; ancestors #236, #235, #234). **Research only:** no changes to main, frozen source, mathematical proof admission, RH/Weil pipelines or physical observations. **Novelty status:** classical results combined into new-to-SUCC typed interfaces; academic originality unverified.

## Abstract — the desired theorem and its real boundary

The observer's job is three different tasks:

1. **Causal observational learning:** inspect successively finer actual source reports, never silently substituting synthetic readings.
2. **Mathematical completion:** exhibit a lawful inverse system of *entire finite source carriers, operations and bonding maps*, and prove its projective limit gives a well-defined topological ring/geometry.
3. **Physical realization:** verify independently that a real system satisfies the source family, sensor fidelity and other assumptions, rather than inferring them from the first few observations.

This draft proves classical conditional versions of (1)–(2), calibrates an indefinitely extensible finite-cost-at-each-stage algorithm, and supplies decisive source-map/identifiability counterexamples for (3).

The main discovery is that **the same complete observable geometric tree can support two nonisomorphic arithmetic sources**. A special source-sensitive carry observation separates them, but only within a genuinely justified model family.

## LCW-01 — same infinitesimal graded shadow, different extension law

For every rational prime p, compare

\[
R_2=\mathbb Z/p^2\mathbb Z\cong W_2(\mathbb F_p),
\qquad
D_2=\mathbb F_p[\varepsilon]/(\varepsilon^2).
\]

Both rings have p² elements, unique nonzero maximal ideals of size p with square zero, residue \(\mathbb F_p\), and isomorphic associated graded rings

\[
\operatorname{gr}_{(p)} R_2
 \cong \mathbb F_p[\varepsilon]/(\varepsilon^2).
\]

The right side is the *dual-number ring*. The left side is the length-two (unramified) Witt-vector ring. **Neither is a field**, and neither is isomorphic to the ordinary complex numbers. Their contrast does, however, closely capture the proposed “similar form, different algebra” intuition.

Using **ordinary base-p digit representatives** \(a=a_0+pa_1\), not the generally different Teichmüller–Witt coordinates, addition in \(R_2\) has

\[
(a_0,a_1)+(b_0,b_1)
=
((a_0+b_0)\bmod p,\,
 (a_1+b_1+\kappa_p(a_0,b_0))\bmod p)
\]

where

\[
\boxed{\kappa_p(a,b)=\left\lfloor\frac{a+b}{p}\right\rfloor}.
\]

The dual ring adds componentwise with no carry. A direct integer calculation gives the normalized group-cocycle identity

\[
\kappa(a,b)+\kappa((a+b)\bmod p,c)
=\kappa(b,c)+\kappa(a,(b+c)\bmod p).
\]

The cocycle is **not a coboundary**: a splitting of the additive extension \(0\to C_p\to C_{p^2}\to C_p\to0\) would supply a lift of the residue class 1 having order p, whereas *every* lift of that class has order p². By contrast the dual ring has additive group \(C_p^2\). The unseen thing in the coarse/graded observations is exactly the **carry extension class**.

A one-step, independent discriminating source probe exists at stage two:

\[
\underbrace{p\cdot1}_{R_2}=p\neq0,
\qquad
\underbrace{p\cdot1}_{D_2}=0.
\]

Equivalently, the source-marked successor operation \(S:x\mapsto x+1\) satisfies \(S^p\neq I\) on the mixed stage-two ring and \(S^p=I\) in equal characteristic. At stage one both exhibit the same \(\mathbb F_p\)-cycle, so the stage-two test is a genuine **held-out discriminator** rather than a restatement of the first observation.

## LCW-02 — a strong geometry-only FuckedField countermodel

At *every* finite depth k, compare \(R_k=\mathbb Z/p^k\mathbb Z\) with \(D_k=\mathbb F_p[t]/(t^k)\). Their compatible full limits are

\[
R_\infty=\mathbb Z_p,\qquad D_\infty=\mathbb F_p[[t]].
\]

Every element of either completed ring has digits \(a_0,a_1,\ldots\in\{0,\ldots,p-1\}\). The **digitwise bijection**

\[
h:\sum_{j\ge0}a_jp^j\mapsto\sum_{j\ge0}a_jt^j
\]

is an isometry for the normalized ultrametric whose distance is \(p^{-r}\) when r is the first differing digit. It sends each depth-k cylinder onto the matching depth-k cylinder, preserving normalized Haar probabilities \(p^{-k}\).

Consequently both complete *unlabelled* rooted ball trees are isometric and measure-isomorphic. The underlying Bruhat–Tits trees of the discretely valued fields \(\mathbb Q_p\) and \(\mathbb F_p((t))\) are both (p+1)-regular infinite trees, hence isomorphic as **unlabelled graphs**. An observer whose available probes see only tree incidence, metric, cylinder cardinalities and Haar mass CANNOT distinguish source characteristic, even after an infinite, complete collection of those observations. This is a **proved probe-closure nonidentifiability**, not a mere delay.

But h is NOT an additive/ring map. The counterexample \((p-1)+1=p\) becomes \(h(p)=t\), whereas \(h(p-1)+h(1)=0\) in characteristic p. A source-sensitive SUCC carry or p-fold marked-unit probe repairs exactly this missing discriminator.

**Do not infer** geometric or topological identification of the underlying spaces automatically gives source ring identification. This is the mathematically sharp version of “same same field, but different.”

## LCW-03–04 — the observer may reason forever and converge to a completed object

Let \(R_k=\mathbb Z/p^k\mathbb Z\) with authentic, surjective source bonding maps \(\rho_k:R_{k+1}\to R_k\). Suppose a coherent observation history \(x_k\in R_k\) satisfies \(\rho_k(x_{k+1})=x_k\) at **every** stage. Then

\[
x_\infty=(x_1,x_2,\ldots)\in\varprojlim R_k=\mathbb Z_p
\]

exists uniquely in that completion. Let a_k be the canonical integer representative of \(x_k\). By construction,

\[
\boxed{d_p(x_\infty,a_k)\le p^{-k}.}
\]

Each step is a **finite** computation giving another digit and a finer error certificate; no individual observer physically executes all infinitely many steps. **One coherent chain is a point in the completed space, not the entire space.**

To learn the geometry, the observer needs the **whole finite source carrier at each level**: its elements, addition/multiplication operations, source map, and parent projection. Each finite ring has \(p^k\) elements. Complete addition/multiplication tables contain \(2p^{2k}\) entries and are finitely computable/observable under a declared effective, resettable source instrument. If every level is accurately supplied, the ring operations commute with the bonding maps. The inverse limit is the topological ring \(\mathbb Z_p\); its rooted coset tree has vertices \((k,r)\), parent \((k-1,r\bmod p^{k-1})\), and p children \((k+1,r+jp^k)\), \(j=0,\ldots,p-1\).

Let \(T_k\) be the finite rooted coset tree through depth k. Their coherent inclusions have a directed union \(T\), whose end space is \(\mathbb Z_p\). Every rooted-radius-R ball in \(T\) has already stabilized by stage R. The finite canonical representatives in \(\mathbb Z_p\) form a \(p^{-k}\)-net, providing an explicit approximation rate and valid source-completion topology.

Under the **additional** declaration of the rank-two free module and fraction-field construction, the resulting field \(\mathbb Q_p\) supplies the actual Bruhat–Tits tree of \(\mathrm{PGL}_2(\mathbb Q_p)\) and its affine SUCC/FUCC matrix action from the preceding OPIG PR #238. This projective lift is not forced by merely observing one scalar trajectory, and neither geometry forces physical Einstein equations, EPR state, or signed completed Weil positivity.

## LCW-05 — model identification depends on available probe closure

For a **finite** candidate family \(\mathcal M\), suppose the source model belongs to \(\mathcal M\), its observations are faithful, every pair of different candidates can be separated by a finite available probe, and the learner fairly exercises those probes. The monotone version spaces \(V_k\subseteq\mathcal M\) contain the source model and eliminate each rival eventually. Because \(\mathcal M\) is finite, some finite stage has \(V_k=\{\text{actual model}\}\). This is an elementary correct-in-the-limit identification theorem **relative to the declared family**.

For an **infinite** family the intersection \(\bigcap_kV_k\) may be a singleton without any finite V_k being a singleton, so *pointwise asymptotic convergence* does not automatically supply a stopping certificate or eventual stabilization of an exact program index. Gold-style grammatical identification in the limit is a distinct, more stringent learning framework.

For the particular two-model family {mixed, equal}, geometry-only probes fail to separate them **at any depth**, whereas one verified \(\mathrm{marked\ addition}\) probe of p·1 at stage two separates them. The latter does **not** establish the entire mixed-characteristic source ontology when unbounded additional model classes and sensor aliases are permitted.

## LCW-06 — indefinite learning can have a controlled empirical error budget

Physical observations need not be treated as perfect oracles. Let an independently calibrated/resettable binary classification of any finite ring-table cell have conditional error probability at most \(\epsilon<1/2\), with independent errors across m repetitions of *that cell*. An odd-size majority fails with binomial tail

\[
E_m(\epsilon)=
\sum_{j>m/2}\binom mj\epsilon^j(1-\epsilon)^{m-j}.
\]

At stage k, \(Q_k=2p^{2k}\) complete operation-cell measurements suffice for addition and multiplication tables (exclude extra sensor/calibration costs). For chosen total error budget \(\delta\in(0,1)\), choose finite odd \(m_k\) satisfying

\[
\boxed{E_{m_k}(\epsilon)\le \frac{\delta\,2^{-k}}{Q_k}.}
\]

Such m_k exist for every k by standard majority concentration inequalities. The countable union bound proves

\[
\Pr[\exists \text{ an inaccurate entry at any stage}]
 \le\sum_{k\ge1}Q_kE_{m_k}(\epsilon)\le\delta.
\]

Independence **across stages** is not needed. Summability also implies by Borel–Cantelli that only finitely many incorrect stage reports occur almost surely; a learner that repairs/replaces stale finite reports from later complete compatible observations can still converge. Every individual stage uses finite time/resources, although resource demands grow and total infinite execution is an ideal limit, not a physical supertask.

The software computes exact rational binomial tails, and its example budget for p=2, \(\epsilon=1/4,\delta=1/8\), stages k=1..4 needs **21, 33, 47, 61** repetitions per table cell respectively. These are synthetic calibration targets, NOT measured sensor error rates. No physical instrument was accessed.

## LCW-09 — the lifted SUCC loop measures carry holonomy at *every* new rung

The nontrivial extension class has a source-relative path interpretation. A complete base-level cycle of \(p\) successive SUCC actions closes in \(\mathbb Z/p\), but its lift closes **only at that coarse level** in \(\mathbb Z/p^2\): it lands at \(p\), one step into the new digit. This is an **algebraic loop holonomy**, not an electromagnetic field phase or physical curvature.

More generally the exact non-split extension
\[
0\longrightarrow \mathbb Z/p\mathbb Z
\longrightarrow \mathbb Z/p^k\mathbb Z
\longrightarrow \mathbb Z/p^{k-1}\mathbb Z
\longrightarrow0
\]
has the explicit source-labelled holonomy
\[
\boxed{S^{p^{k-1}}(0)=p^{k-1}\ne0\pmod{p^k},
\qquad S^{p^{k-1}}(0)=0\pmod{p^{k-1}}.}
\]

**Proof:** on mixed-characteristic ring \(R_k\), \(S(x)=x+1\), so iterating \(p^{k-1}\) times adds \(p^{k-1}\). Its lower-level reduction vanishes while its top digit is exactly one. The additive extension is non-split: any lift of a generator of the base group has order \(p^k\), so cannot provide an additive section with the base's order \(p^{k-1}\). In equal characteristic \(D_k=\mathbb F_p[t]/(t^k)\), the marked successor is translation by 1 and \(S^p=I\) **at every k**; hence the coarse loop has trivial lift. The higher-rung holonomy is fully predicted from a sourced transition rather than manufactured by decorating a geometric loop.

This supplies a **cofinal sequence of fresh source checks**: rank k tests how a previously closed \(p^{k-1}\)-step clock loop lifts into newly visible structure. Each finite test is feasible in principle (though resource cost grows); their indefinitely many correct, compatible outcomes reconstruct the mixed characteristic tower *provided the global source and instrument assumptions are independently justified*. For a hidden extra-prime or changed extension after finite horizon, the first affected rank falsifies the hypothesis. An observer lacking these SUCC-action probes can traverse the identical geometry forever and learn no ring-characteristic difference.

Independent exact tests calibrate 16 selected mixed/equal lifted loops and negative source/type controls. This is a new-to-SUCC representation of classical group-extension arithmetic, not an academic novelty or physical gauge-field result.

## LCW-07 — the completed source need not be an original realized integer

Define the p-adic point

\[
x=\sum_{j\ge2}p^{j!}\in\mathbb Z_p.
\]

Every finite prefix has a nonnegative integer representative. All prefixes commute with reduction, so x is a genuine element of the mathematical completion. But x is not an ordinary integer: each nonnegative integer has eventually zero p-adic digits and each negative integer has eventually digits p−1, while x has infinitely many isolated ones and infinitely many zero digits. Thus mathematical completion does not guarantee the observer's **original physical source carrier** realizes the limit point. This is an exact source-map adequacy distinction already fundamental to SUCC's FuckedField taxonomy.

Similarly, a delayed counterfeit inverse tower with moduli \(p^k\) through stage K and \(p^kq\) afterward, for q another prime, is a legal system of surjective cyclic quotient maps. It matches every finite observation through K and diverges at K+1. No fixed finite observation proves all later source axioms.

## LCW-10 — one factorial chain learns the *entire* profinite arithmetic carrier

A single source-faithful indefinitely extensible clock sequence is enough to cover **all finite integer congruence observations**, not just the place p. Let \(m_k=k!\), and require complete oriented ring-source stages \(C_k=\mathbb Z/k!\mathbb Z\) with the authentic reduction \(C_{k+1}\to C_k\). Every finite modulus \(n\ge1\) divides \(k!\) for all \(k\ge n\). Thus the factorial chain is **cofinal** in the directed system of all finite quotients \(\mathbb Z/n\mathbb Z\), so the standard cofinal inverse-limit and CRT theorems give

\[
\boxed{
\varprojlim_{k\ge1}\mathbb Z/k!\mathbb Z
\cong
\widehat{\mathbb Z}
\cong
\prod_{p\text{ prime}}\mathbb Z_p.
}
\]

**Proof:** For any coherent factorial residue sequence \((x_k)_k\) and any modulus n, choose any k with n|k! and set \(x\bmod n=x_k\bmod n\); compatibility makes this independent of k. This yields a coherent family over all moduli. Conversely any full congruence family restricts along k!, and the two maps are inverse. CRT identifies every finite \(\mathbb Z/k!\mathbb Z\) with the product of its prime-power quotients, compatibly; passing to limits gives the product over all p. QED.

At rung k, the certified p-adic precision is

\[
v_p(k!)=\sum_{j\ge1}\lfloor k/p^j\rfloor,\qquad
d_p(x_p,x_k)\le p^{-v_p(k!)}.
\]

Every fixed p gains unbounded precision as k→∞. The forgetting arrow from stage \((k+1)!\) onto \(k!\) has **exactly \(k+1\) lifts for each previously observed residue**. Therefore the rooted *factorial observation tree* naturally has level-dependent branching \(k+1\), and its boundary realizes the entire profinite ring, not a lone chosen p-ary component. Every finite radius of the rooted observation tree stabilizes after its corresponding finite rung, just as in LCW-04. The exact finite code checks all quotient refinements through stage 7, the factorial Legendre prime valuations through stage 15, and cofinal access to every modulus 1..200. No physical observer has run infinitely many stages.

### A global counterfeit with the same observation geometry at every rung

At rung k, replace every source local ring \(\mathbb Z/p^{v_p(k!)}\mathbb Z\) with its equal-characteristic digit lookalike \(\mathbb F_p[t]/(t^{v_p(k!)})\), and take their finite product over primes p≤k. The two candidate *finite total rings* have **exactly the same cardinality \(k!\)**, the same placewise digit cylinder geometry, and compatible parent maps. Under a product of digitwise isometries, their whole inverse-limit spaces and Haar-cylinder structures match. Their ring arithmetic nevertheless differs: the real cyclic ring has characteristic \(k!\), whereas the equal-characteristic product has characteristic \(\operatorname{rad}(k!)=\prod_{p\le k}p\). At k=4 the two source rings have cardinal 24 but characteristics **24 versus 6**, with \(v_2(4!)=3\) and \(v_3(4!)=1\). This is the requested **global** FuckedField source-map adversary.

Notice that their infinite products both have **global characteristic zero** (their factors range over all primes), so looking only at that coarse global invariant need not separate them. The characteristic and carry probes must remain **prime-place source-relative**. Geometry-only observation at every rung is still insufficient. This supplies an unusually sharp reason that the global SUCC observation system must preserve its local prime-source arithmetic, not merely the shape of its inverse-limit object.

The factorial completion \(\widehat{\mathbb Z}\) is **not** the full adele ring \(\mathbb A_{\mathbb Q}\) or an Archimedean physical metric. Adding the real place, quantum dynamical state, and genuine ER=EPR geometry is still an independent source-mapping and proof problem.

## 8. Verdict, scope and next probe

**Disclosed within assumptions (paper proofs, not Lean-certified):** source carry extension/associated graded identity; all-depth ultrametric geometry/Haar equivalence and source nonidentifiability; second-rung marked-SUCC discriminator; source-complete effective inverse-limit construction and error bounds; finite candidate version-space identification; conditional countably summable measurement-error schedule; original-integer realization counterexample.

**Refuted:** inference of arithmetic source from geometry-only probes even after arbitrarily many observations; inference of infinite source fidelity from one finite observation; inference of original-integer realization from mathematical completion. None of these counterexamples denies the *conditional* learner theorem.

**Unverified:** empirically calibrated faithful sensors, completeness of the true physical source family, the source map into physical reality, an intrinsic quantum-state selection, Einstein/ER=EPR dynamics, signed Weil positivity, RH and academic novelty.

**Next decisive experiment:** preregister a marked unit and repeatable SUCC action on a physical system whose stage-two carry is independently measured. Compare \(\mathrm{char}=p^2\) versus \(\mathrm{char}=p\) predictions **without fitting the second observation**. Then require an independent two-system correlation such as the relative-phase Fourier probe from OPIG, to determine a quantum state rather than only a classical ring and tree. Keep every source/probe/failure receipt and permit true negative verdicts.

### Provenance

Classical Witt-vector and p-differential literature (Dupuy, Katz, Rabinoff & Zureick-Brown, https://arxiv.org/abs/1712.09487), Gold's original learning-in-the-limit paper (1967, https://www.cs.famaf.unc.edu.ar/~gabriel/files/gold67limit.pdf), and standard pro-p inverse limits and Bruhat–Tits theory. Internal SUCC `docs/OBSERVER_PROOF_ACCESS.md`, `observational_succ/source_field_inverse_limits.py`, `observational_succ/field_limit_compactness.py`, and the source-pinned OPIG PR #238. The 42 finite tests and source-hash-pinned receipt are in this research branch. Independent scholarly novelty has not been investigated sufficiently to claim any.
