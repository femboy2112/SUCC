# Ideal frame SUCC: finite completion, omega reconstruction, and persistent observational darkness

**Date:** 2026-10-10. **Status:** new-to-project formal framing, classical reconstruction theorems, exact finite implementation, and explicit nonidentifiability counterexamples. **No claim of a new general theorem of physical cognition or of RH.**

**Code:** `observational_succ/ideal_frames.py`; **tests:** `tests/test_ideal_frames.py`.

## 0. Author's proposal and faithful steelman

**Originating insight (maintainer, 2026-10-10):** Idealize the elapsed time between receiving a local observation and incorporating it into the best justified model as zero. A frame consists of a working model and the admissible field probes accessible in that frame. SUCC advances to a new frame in which observations alter the model and thereby alter what can next be probed.

Classify targets according to how many ideal frames are required:

1. **Simple:** sufficiently many *finite* ideal frame updates complete the relevant model.
2. **Ideal analytic:** no fixed finite stage completely identifies the target, but the compatible ideal omega record uniquely determines it.
3. **FuckedSpace:** even the complete omega record fails to identify the target, or no valid limit report exists in the claimed class.

**Researcher's repair:** "complete" must be defined relative to (a) the admissible *source/model class*, (b) a *specified observer/probe policy*, (c) a *target invariant*, and (d) a limit topology and realization hypothesis. It is not a property of a space in isolation. The below results show a clean exact trichotomy for full-source identification; target-relative identification is more general.

"Instant assimilation" is an epistemic idealization. It does not mean that all potentially conceivable probes are physically available or that their outcomes are known in advance.

## 1. Typed ideal observational frames

Let \(\mathcal X\) be a nonempty declared class of possible sources, \(x_*\in\mathcal X\) an actual source, and \(\mathcal P\) a set of realizable deterministic probes, each \(p:\mathcal X\to Y_p\). Physical/noisy versions instead require instruments and outcome distributions; the current theorem is deterministic.

A stage \(n\) has:
- immutable source-history \(H_n=((p_i,p_i(x_*)))_{i\in I_n}\), where every claimed observation is actually supplied by an admissible source probe;
- a compatible-source *version space* \(K_n(x_*)=\{x\in\mathcal X:\forall i\in I_n,\ p_i(x)=p_i(x_*)\}\);
- an optional preferred semantic model \(\widehat x_n\in K_n(x_*)\), which is not equivalent to certification of \(K_n=\{x_*\}\);
- a probe access policy \(A(H_n,M_n,r_n)\subseteq\mathcal P\), possibly dependent on a resource/clock state \(r_n\).

One ideal frame update assimilates all observations *currently admissible*. The next SUCC step may unlock new instruments:

\[
H_{n+1}=H_n\mathbin{\|}\operatorname{Observe}_{x_*}(A(H_n,M_n,r_n)),\qquad
K_{n+1}=\{x\in K_n:\text{x matches each new observation}\}.
\]

A semantic model can be recomputed by an ideal closure \(\operatorname{Cl}(H_{n+1})\). The closure is required to be sound relative to its stated axioms. There is **no assertion that computing such a closure is effectively possible in zero physical time**.

**Source-faithfulness theorem (elementary):** if \(x_*\in\mathcal X\) and every actualized observation was really obtained from \(x_*\), then \(x_*\in K_{n+1}\subseteq K_n\) for every finite \(n\). This says nothing about whether \(K_n\) becomes a singleton. A preferred model can oscillate or be wrong even while the compatible-source sets are nested.

For a target report \(T:\mathcal X\to\mathcal Z\), define the still-possible target values \(V_n=T(K_n)\). The report is *identified by frame n* iff \(|V_n|=1\). Full-source identification is the special case \(T=\mathrm{id}_{\mathcal X}\). This separates deciding a property from reconstructing the entire source.

For the growing family of probes define \(K_\omega=\bigcap_{n<\omega}K_n\). Then:

- **Finite-identifiable:** \(\exists n<\omega,\ |V_n|=1\).
- **Omega-identifiable only:** \(\forall n<\omega,\ |V_n|>1\) and \(|T(K_\omega)|=1\).
- **Persistently probe-dark:** \(|T(K_\omega)|>1\).

The categories classify \((\mathcal X,\mathcal P,A,T,x_*)\), not \(\mathcal X\) alone. These definitions are operational *ideal reports*, not executed physical supertasks. A distinct issue arises when \(K_\omega\) is empty because finite observations were modeled in a class that contains no actual source.

## 2. One unchanged probe tower, three exact mathematical behaviors

Let the source be a germ of a real-valued function at \(0\). At stage \(n\), all currently accessible derivative probes are known exactly:

\[
J_0^n f=(f(0),f'(0),\ldots,f^{(n)}(0)).
\]

SUCC unlocks derivative order \(n+1\). All earlier observations remain fixed. The proposed observation functor at omega is the Taylor-jet morphism

\[
J_0^\infty f=\sum_{k\ge 0}\frac{f^{(k)}(0)}{k!}x^k\in\mathbb R[[x]].
\]

Here \(\mathbb R[[x]]\) means *formal* series; convergence has **not** been assumed.

### A. Simple: bounded-degree polynomial germs

Put \(\mathcal X=\mathbb R[x]_{\le d}\), where the degree bound \(d\) is a genuine source-class premise, not an inference from a small initial jet. Equality of \(J^d_0 f\) and \(J^d_0 g\) forces equality of all coefficients:

\[
f(x)=\sum_{k=0}^{d}\frac{f^{(k)}(0)}{k!}x^k.
\]

Thus \(K_d(f)=\{f\}\), for every \(f\in\mathcal X\). For every \(n<d\), adding \(x^{n+1}\) (when \(n+1\le d\)) gives a different polynomial with the same \(n\)-jet. Uniform completion time for this class is therefore precisely \(d\) (counting the order-0 initial frame as stage 0).

**Unexpected class-relative consequence:** If the permitted class is the *unbounded* polynomial ring \(\\mathbb R[x]\), **even the zero polynomial is not identifiable at any finite stage**. For every \(n\), the polynomial \(f+x^{n+1}\) has the same observed \(n\)-jet as \(f\). Yet the full infinite jet uniquely determines any polynomial. Thus an individually finite object may still require an ideal omega report to be *certifiably* identified when no upper complexity bound is supplied. Finite description and finite identification are different notions.

**Boundary:** no finite jet can *certify that the unknown source has degree at most d* absent independently justified restrictions. Claiming the bound can yield an attractive but false "completed" model; a later higher derivative exposes the mistake.

### B. Ideal analytic: real-analytic germs

Put \(\mathcal X=\mathcal A_0\), real-analytic germs at 0. Every finite \(n\)-jet leaves infinitely many possibilities because \(f\) and \(f+\varepsilon x^{n+1}\) agree to order \(n\) for nonzero \(\varepsilon\).

But if all derivatives at 0 agree, the Taylor series agree; by real analyticity the functions agree on some neighborhood of 0, so they define the same germ. Therefore \(J_0^\infty:\mathcal A_0\to\mathbb R[[x]]\) is **injective**, while every finite \(J_0^n\) is noninjective. For full-source identification this is an honest example of *omega-only ideal reconstruction*.

The image is the ring of **convergent** series \(\mathbb R\{x\}\), not all formal series. The omega report is uniquely identifiable *given the premise that the genuine source is analytic*, but has not been physically executed.

A quantitative version requires a separate uniform majorant: if Taylor coefficients obey \(|a_k|\le MR^{-k}\), then for any \(0\le r<R\),

\[
\sup_{|x|\le r}|f(x)-\sum_{k=0}^n a_kx^k|
 \le \frac{M(r/R)^{n+1}}{1-r/R}.
\]

This is an explicit convergence modulus. Uniqueness from the full jet **does not itself supply** usable uniform error bounds without analytic control. In fact, across *all* analytic germs without a shared growth bound, no finite jet can give a uniformly valid error bound for the value at a fixed nonzero \(r\): after observing through order \(n\), both \(f\) and \(f+A x^{n+1}\) remain possible, and the value difference \(A r^{n+1}\) can be arbitrarily large. This directly separates **infinite-data uniqueness** from **uniform effective reconstruction**. A single Taylor chart may not reconstruct a distant point beyond its convergence disk; global claims require continued analytic continuation and domains.

### C. FuckedSpace: smooth germs under precisely the same probes

Put \(\mathcal X=C^\infty_0\), the ring of smooth germs at 0. Let

\[
f(x)=0,\quad
g(x)=\begin{cases}e^{-1/x^2},&x\ne0,\\0,&x=0.\end{cases}
\]

It is standard (provable by repeated differentiation and exponential dominance) that \(g\) is smooth, \(g^{(k)}(0)=0\) for every \(k\), but \(g\) is nonzero on every punctured neighborhood of 0.

Thus \(f\ne g\) as germs, yet \(J_0^\infty f=J_0^\infty g=0\). No number of repeated SUCC stages restricted to the derivatives-at-0 probe family distinguishes them.

Let \(\mathcal F_0=\ker J_0^\infty\), the ideal of flat smooth germs. Classical Borel's theorem says that the smooth Taylor-jet morphism is surjective. There is an exact sequence

\[
0\longrightarrow\mathcal F_0\longrightarrow C^\infty_0
\xrightarrow{J_0^\infty}\mathbb R[[x]]\longrightarrow0.
\]

The observer sees the quotient \(C^\infty_0/\mathcal F_0\), not the full smooth germ. This is a rigorous example of a *nontrivial observational kernel* at infinity. The analytic germ functor has no such kernel.

**Important limitation:** evaluating \(g\) at a *nonzero* \(x\) is an admissible new kind of probe that separates \(g\) from zero immediately. Hence "Fucked" is **relative to the accessible probe closure**, not an intrinsic verdict that the smooth world is forever unknowable. "All conceivable probes with all exact outcomes available from stage 0" would trivialize this example and even identify arbitrary functions at once.

**Independent source:** M. Fassina and Y. Pan, *A local obstruction for elliptic operators with real analytic coefficients on flat germs*, Annales de la Faculté des Sciences de Toulouse 31 (2022), §2, especially Taylor-jet kernel, Borel Lemma 2.2, and analytic-germ definition; https://doi.org/10.5802/afst.1722. Our trichotomy terminology is new-to-project; the analytic, smooth and polynomial facts are classical.

## 3. A second omega failure: local realizability does not force analytic completion

Consider the compatible formal Taylor coefficients \(a_k=k!\). Every finite prefix \((a_0,\ldots,a_n)\) is realized by the *analytic polynomial*

\[
p_n(x)=\sum_{k=0}^n k!x^k.
\]

The polynomials have exactly compatible finite jets: \(J_0^n p_{n+1}=J_0^n p_n\). Nevertheless the infinite series \(\sum_{k\ge0}k!x^k\) has **radius of convergence zero** (because \(|a_{k+1}/a_k|=k+1\to\infty\)). It is no analytic germ at zero.

Consequently the inverse limit of the finite jet spaces is the whole formal series ring \(\mathbb R[[x]]\), not automatically the analytic germ ring \(\mathbb R\{x\}\).

**Verdict: productive failure of the naive limit proposal.** Every finite frame admitting an analytic realization does not imply the ideal omega history admits an analytic realization. The obstruction is **regularity and source-map adequacy**, independent of the noninjective flat-function obstruction.

If the actual source is already known to lie in \(\mathcal A_0\), this particular pathology is excluded by premise. If the observer only infers analyticity from finite polynomial fits, it is not excluded.

By Borel's theorem this formal jet is realizable as a *smooth* germ, illustrating that realizability depends on the source class.

## 4. Adaptive indistinguishability lemma (elementary, general)

**Hypotheses:** (i) an observer's next-probe selection and semantic closure depend only on the already recorded history and declared resource clock, not on secret access to the actual source; (ii) all selected probes belong to a declared family \(\mathcal P\); (iii) two candidate sources \(x,y\) return identical outcomes on every \(p\in\mathcal P\).

**Claim:** any deterministic ideal observer has identical finite histories and identical semantic reports on \(x\) and \(y\), for every finite number of SUCC steps. Its history-derived omega report also agrees, whenever that report is defined.

**Proof:** initially both histories agree. If histories agree through frame \(n\), the history-dependent policy selects the same next probes, and (iii) gives the same outcomes; closure produces the same reported model. Induction proves equality through all finite stages. An omega report defined only from the compatible history has equal input for both sources. This is **a no-go theorem within the specified observer interface**, not a global impossibility theorem.

**Counterfactual discriminator:** admit even one probe \(q\) for which \(q(x)\ne q(y)\). A SUCC policy that actually accesses \(q\) breaks the equivalence. Thus inaccessible *information*, inaccessible *probe pathways*, and invalid *model-class restrictions* must be diagnosed separately.

No observer can certify a distinction not represented by any admissible probe or logically valid prior assumption. But a stronger model class can sometimes reduce the ambiguity without introducing a new physical measurement—as analyticity does in §2.

## 5. Fixed points, topology and the difference between three "ends"

A semantic closure can reach a fixed point without identifying the real source: a probe-blind observer can stop learning because the current probe menu has no separating query. Likewise a selected preferred model \(\widehat x_n\) can appear stationary while the compatible set \(K_n\) remains large.

For a monotone \(\omega\)-continuous operator on a pointed \(\omega\)-complete partial order, Kleene's fixed-point theorem constructs a least fixed point as \(\sup_n F^n(\bot)\). This yields a *fixed point of a declared operator*, not necessarily a faithful source representation or a complete mathematical proof. If the update is non-\(\omega\)-continuous, that theorem does not license identification of the limit with a fixed point.

Classical reference: University of Pennsylvania, J. Gallier, *Introduction to the Theory of Computation*, §7.7 (least fixed points), https://www.cis.upenn.edu/~cis5110/notes/tcbook-lang.pdf.

A complete observational report therefore needs three separate certificates:

1. **Identification:** target \(T\) has a singleton image on the source-compatible fiber.
2. **Realization/regularity:** the ideal data correspond to an object of the claimed source class, with appropriate topology; additional stability or modulus if numerical approximation is claimed.
3. **Epistemic authority:** a concrete mathematical argument justifies the report, not merely finite agreement or an unlicensed \(\omega\)-rule.

An \(\omega+1\) postprocessing rule may prove something from an explicitly given mathematical omega object under separately justified axioms. It cannot recover a missing flat-direction distinction from exactly the same derivative history if the report depends only on that history.

## 6. Discriminating tests and exact finite executable controls

All outcomes below were declared prior to running the finite test implementation:

| Rival claim | Positive probe | Negative/control probe | Expected verdict |
| --- | --- | --- | --- |
| Degree-\(d\) polynomial is identified after \(d\)-jet, assuming true bound | Rational polynomial and exact derivatives | Try one fewer derivative; add \(x^d\) | Success at \(d\), failure before \(d\) |
| An arbitrary analytic germ is finitely identified by derivative jet | \(f\) and \(f+x^{n+1}\) | Test derivative \(n+1\) | Equal through \(n\), distinct at \(n+1\) |
| Infinite jet suffices for every smooth germ | Zero and \(e^{-1/x^2}\) | New off-origin evaluation | Refuted by all-order mathematical counterexample |
| Finite analytic realizability implies omega analytic realizability | Coefficients \(a_k=k!\) | Ratio/radius of convergence | Refuted: every prefix realized, radius zero |
| A good finite fit establishes its source class | Actual \(x^4\), assume degree 0 | Observe fourth derivative | False early completion exposed |
| Ideal history can be freely rewritten during update | Fixed actual polynomial | Attempt to change an earlier derivative | Reject conflicting history |

The executable tests are exact rational, finite only. The infinite flat germ conclusion is a **mathematical proof**, not a test that pretends to iterate infinitely. The negative-radius result is likewise a mathematical statement supported by finite coefficient/ratio regression checks.

Reproduce finite suite:

~~~sh
python -m unittest tests.test_ideal_frames -v
python -m unittest discover -s tests -p 'test_*.py'
~~~

## 7. Relation to existing ObsSUCC work, and the RH firewall

- **Causal records:** new observations never invalidate previously realized outcomes; a wrong model-class assumption must be revised without rewriting causal data.
- **Restricted Yoneda:** the accessible probes generate a restricted observation functor. Its failure of faithfulness is measured by the observational equivalence kernel (for smooth jets, the flat ideal); switching probe families changes what is representable.
- **Operational semantics:** total-variation data processing characterizes classical stochastic loss on finite labels; the jet example is different, *deterministic structural nonidentifiability*. Do not treat its fibers as stochastic loss without an explicit probabilistic model.
- **Gödel/Turing:** finite instances or finitely realizable prefixes do not generally authorize an infinitary assertion; nevertheless structural theorems can prove an all-orders fact with a *finite proof*. Our analytic and smooth reconstruction conclusions are examples.
- **RH:** one may investigate whether finite source probes fail to distinguish source families or the needed completed arithmetic functional, but NOTHING here establishes Weil positivity or RH independence. A new source-derived bridge must explicitly preserve Gamma/poles, Euler structure, topology and test-function domains.

## 8. Claim ledger and next verdict-changing research

Recommended ledger entries:

- **O39 — HYPOTHESIS / formal proposal:** instantaneous sound semantic closure with successive admissible probe expansion; no physical brain claim.
- **O40 — CLASSICAL / PROVED LOCAL:** finite \(d\)-jet polynomial reconstruction conditional on genuine degree bound.
- **O41 — CLASSICAL:** infinite analytic jet injective, finite analytic jets noninjective; only convergent formal series are analytic germs.
- **O42 — CLASSICAL / explicit counterexample:** smooth Taylor jet has nontrivial flat ideal kernel; Borel map surjective; relative FuckedSpace.
- **O43 — PROVED LOCAL / mathematical counterexample:** all finite analytic jet prefixes realizable does not imply a realizable analytic omega object, via \(\sum k!x^k\).
- **O44 — PROVED LOCAL:** history-only deterministic observer cannot discriminate two sources equivalent on all its admissible probes.
- **O45 — REFUTED (as unconditional claim):** being "Fucked" is a property of \(\mathcal X\) independent of probes; off-origin evaluation defeats the displayed obstruction.
- **O46 — UNVERIFIED:** there exists a physically grounded, general finite-to-infinite observer completion trichotomy with calibrated computational resources and the correct topology.

**Next main research question:** Define an observer category with causally typed histories, probe-access morphisms, semantic closure and reports. Characterize its **faithful** and **nonfaithful** observation functors, with target-relative identifiability and a computable stability modulus. Test a genuinely model-dependent probe menu and find a counterexample where a false semantic model permanently excludes an actually available separating probe. Then distinguish the failure of *discovery* from a true inaccessible-observable boundary.

**No global success claim.** These examples are an excellent sharp test bed and a useful theoretical research program, not a newly proved universal law of observer access.
