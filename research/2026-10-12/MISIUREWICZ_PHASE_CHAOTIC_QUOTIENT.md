# Chaotic SUCC III: an exact nonconstant deterministic E phase over a positive-entropy logistic carrier

**Date:** 2026-10-12  
**Source and branch:** stacked onto Chaotic SUCC II PR #32, exact parent commit `8d32b2302f97f5e3a04e3a4b1a6d6419e634190e`; predecessor chaotic tree PR #30 and dual E/common-carrier PRs #26–#29. All code additive; no imported archival rewrite.  
**Verdict:** **SURVIVES**, classical conditional theorem, locally proved by exact cubic algebra and independently calibrated finite controls. No mathematical-priority, physical source-authentication, naturally selected probability law, all-parameter-chaos elimination, quantum, or RH claim.

## 0. What the maintainer proposed (and what is new relative to the preceding rounds)

The user asked whether a rooted E observer tree could accumulate enough knowledge that **a chaotic physical/dynamical observation front appears non-chaotic to E**, ideally without ignoring its shared-carrier identity and dual observer interface. CT1–CT7 established exact asymptotic and finite polynomial inverse-tree averages at logistic parameter 4, but a **constant aggregate** discarded original trajectories. CQ1–CQ4 demonstrated that blindly keeping both inverse roots for a logistic parameter below 4 invents unrealizable sources, whereas legitimate finite symbolic window observables at parameter 4 remain *stochastically* predictive. Neither construction supplied a **nonconstant deterministic** quotient genuinely arising from a positive-entropy logistic map.

This dossier supplies exactly such an example, with an important qualification: a **source-relative two-phase quotient on a forward-invariant dense subset**, not a globally continuous factor on the entire invariant interval. The observer *really does have a period-two law*, while the original source has exponentially many legal histories. This is familiar symbolic and interval dynamics, made into a falsifiable SUCC/E-tower construction rather than claimed as newly discovered logistic-map mathematics.

## 1. Provenance and classical source

J. C. Sprott, *Misiurewicz Point of the Logistic Map*, Department of Physics, University of Wisconsin (2005; revised 2006), https://sprott.physics.wisc.edu/chaos/mispoint.htm, reports the first band-merging logistic parameter near `3.67857351042832226`, its defining exact cubic, and the fixed postcritical endpoint (attributed there to Daniel Stoffer). That page cites M. Misiurewicz, *Absolutely continuous measures for certain maps of an interval*, Publ. Math. IHÉS **53** (1981), 17–51. Independently, Jim Crutchfield's UC Davis *Natural Computation and Self-Organization* homework specifically asks students to construct a three-element Markov partition for this two-band merger: https://csc.ucdavis.edu/~chaos/courses/poci/Homework/Week7.html. Thus this is **not** an academic novelty claim. The source checked here is the algebraic logistic map, not the decimal approximation of its parameter. General Markov interval map entropy equals the log spectral radius of its certified full Markov partition (classical interval dynamics; e.g. Drexel university lecture chapter `https://physics.drexel.edu/~bob/PHYS750_NLD/ch4.pdf`).

## 2. Exact source algebra and full invariant carrier

Let \(\alpha\) be the **unique real root in \((3,4)\)** of

\[
 p(r)=r^3-2r^2-4r-8.
\]

Here \(p'(r)=3r^2-4r-4=(3r+2)(r-2)>0\) for \(r>2\), while \(p(3)<0<p(4)\). The implementation keeps values as exact triples in \(\mathbb Q[\alpha]\), reducing \(\alpha^3=2\alpha^2+4\alpha+8\). The original source map is

\[
 f(x)=\alpha x(1-x), \quad c=\tfrac12,\quad
 q=\tfrac\alpha4,\quad a=\frac1\alpha,
 \quad z=1-\frac1\alpha .
\]

Its exact postcritical orbit follows by quotient-algebra multiplication (not by rounding):

\[
 \boxed{c\xrightarrow f q\xrightarrow f a\xrightarrow f z\xrightarrow f z.}
\]

The algebraic field records \(a=(\alpha^2-2\alpha-4)/8\) and \(\alpha a=1\). The strictly ordered endpoints are

\[
 0<a<c<z<q<1.
\]

The exact rational root bracket stored in the receipt, and monotonicity of the cubic on \(r>2\), certify every non-symbolic inequality without floating-point sign guesses. For example \(q-z=(\alpha-2)^2/(4\alpha)>0\). The **forward-invariant postcritical carrier** is

\[
 J=[a,q],\qquad f(J)=J.
\]

No claim about an arbitrary initial point outside J is inferred from this invariant-core analysis. Let the three closed Markov intervals be

\[
 A=[a,c],\qquad B=[c,z],\qquad C=[z,q].
\]

Using the critical monotonicity (increasing to \(c\), decreasing thereafter) and exact endpoint orbit, obtain **complete interval images**, not merely the endpoint pairs:

\[
 f(A)=C,\qquad f(B)=C,\qquad f(C)=A\cup B.
\]

The *derived* graph has adjacency, with rows/columns A,B,C:

\[
 M=\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix}, \qquad
 \det(\lambda I-M)=\lambda(\lambda^2-2).
\]

The PF spectral radius is \(\sqrt2\). By the standard Markov-interval entropy theorem (finite monotone Markov partition, full exact image unions),

\[
 \boxed{h_{\mathrm{top}}(f|_J)=\log\sqrt2=\frac12\log 2>0.}\tag{MC1}
\]

An elementary check underlying this theorem: both \(f^2|_A\) and \(f^2|_B\) are monotone onto \(A\cup B=[a,z]\). Thus each complete **two-step** return to the left phase provides two genuine source branches. The number of admissible finite symbolic paths from a fixed initial cell grows as \(2^{\lfloor n/2\rfloor}\) from A/B or \(2^{\lceil n/2\rceil}\) from C. At least this much exponential separation is present even though the precise numerical source outcome remains deterministic. The clean Markov partition controls the matching upper entropy bound. The characteristic polynomial and all endpoint images are checked independently in the test suite.

**Status MC1:** CLASSICAL / PROVED LOCAL, under this exact algebraic source. Not proof of a universal chaotic-parameter theorem.

## 3. The root-E quotient exists, is nonconstant, and is deterministic

Define a **source law for the observation**, not a new physical carrier:

\[
 \phi(x)=\begin{cases}
 0,&x\in A\cup B,\\
 1,&x\in C.
 \end{cases}
\]

At shared endpoints there can be conflicting obligations. Explicitly declare

\[
 D=\{a,c,z,q\},\qquad
 J^*=J\setminus\bigcup_{n\ge0}f^{-n}(D).
\]

Every inverse image set is finite because the source map is quadratic; consequently \(J\setminus J^*\) is at most countable. \(J^*\) is forward invariant and contains uncountably many genuine initial conditions. On \(J^*\), every \(f\)-transition crosses the source-certified bipartition \(A\cup B \leftrightarrow C\), so the following identity is **pointwise exact**:

\[
 \boxed{\phi(f^n(x))=\phi(x)\oplus(n\bmod2)
 \qquad\forall x\in J^*,\ \forall n\ge0.}\tag{MC2}
\]

Thus the deterministic induced two-state dynamics is

\[
 E_L\longmapsto E_R\longmapsto E_L\longmapsto E_R\cdots.
\]

This is a **nonconstant zero-topological/measure-entropy phase system**, while its full source retains positive topological entropy (MC1). The phase map is discontinuous at its boundary; no claims of a global continuous factor on connected J. Indeed \(z\) is fixed: any everywhere-defined binary flip law would require \(\phi(z)=1-\phi(z)\), impossible. The fixed point is a precise, unavoidable receipt **refuting** that stronger assertion. The countable exclusion is also the source of a noncompact-domain caveat: the topological entropy above is asserted on compact J, not computed by the noncompact-subspace definition of entropy on J*.

**Status MC2:** CLASSICAL / PROVED LOCAL. The globally-defined continuous/everywhere-pointwise stronger factor is **REFUTED** by the fixed point.

## 4. Nontrivial observable stochastic law under a *chosen* exact symbolic source

The transition-support graph M is **not** a probability matrix; edge existence does not determine physical branch weights. Instead we explicitly select the canonical **Parry (maximum entropy) symbolic Markov law**, derivable from \(M\) and its PF right eigenvector \(v=(1,1,\sqrt2)\):

\[
 P_{ij}=\frac{M_{ij}v_j}{\sqrt2\,v_i},\qquad
 P=\begin{pmatrix}0&0&1\\0&0&1\\1/2&1/2&0\end{pmatrix},\qquad
 \pi=(1/4,1/4,1/2).
\]

Both \(P\mathbf1=\mathbf1\) and \(\pi P=\pi\) hold **exactly over rational numbers**. The source phase is balanced: \(\Pr(E_L)=\pi_A+\pi_B=1/2\), \(\Pr(E_R)=\pi_C=1/2\). The conditional entropy rate is

\[
 \boxed{h_{\mathrm{Parry}}=-\sum_i\pi_i\sum_jP_{ij}\log_2 P_{ij}
 =\pi_C\cdot1=\tfrac12\ \mathrm{bit/step}.}\tag{MC3}
\]

The phase itself has **zero conditional entropy rate**: once E knows its current phase and time-step parity, its entire future phase sequence is fixed. For a fixed C start, the full n-step source itinerary carries exactly \(\lceil n/2\rceil\) fresh fair Parry branch bits; for a fixed A/B start, exactly \(\lfloor n/2\rfloor\). Therefore source-history loss is explicitly priced rather than erased:

\[
 \underbrace{\text{phase}}_{1\ \mathrm{bit\ current\ identity}}
 \quad\hbox{versus}\quad
 \underbrace{\text{microscopic n-path}}_{\sim n/2\ \mathrm{bits\ of\ history}}.
\]

### MC3b. Rigorous prior-family ablation: phase order is not an artifact of fair coin weights

Replace the special Parry C→A/B half-half row with **any exact** `p in [0,1]`:

\[
 P^{(p)}=\begin{pmatrix}0&0&1\\0&0&1\\p&1-p&0\end{pmatrix},\qquad
 \pi^{(p)}=(p/2,(1-p)/2,1/2).
\]

Direct rational multiplication proves `π(p) P(p)=π(p)` **for every p**, even endpoints. The coarse E phase has the same balanced distribution `(1/2,1/2)` and the same period-two prediction law. For `0<p<1`, the microscopic **symbolic metric entropy** is `H_binary(p)/2 > 0` bits/step, whereas for `p=0` or `p=1` it vanishes: those endpoint priors concentrate on a deterministic two-cycle even though the **topological entropy of the whole real source J** remains positive. The Parry `p=1/2` is the maximum-entropy member of the declared family. Tests compare `p in {0,1/5,1/3,2/5,1/2,3/4,1}`, verify normalization and stationarity exactly, and check that the phase predictions and raw parity covariance remain unchanged. A **source-law-independent pointwise quotient** survives the prior ablation; source-measure-dependent micro entropy does not. None of these arbitrary symbolic Markov laws is automatically the physical natural acim.

**Status MC3b:** CLASSICAL / PROVED LOCAL for explicitly chosen symbolic sources, not an acim identification.

**Critical epistemic distinction:** The Parry measure is a chosen invariant **symbolic** source measure, not a measurement or theorem that it equals the naturally occurring absolutely continuous invariant measure (acim) of the physical logistic map. It is also not the same as the stationarity assumption at r=4 (where the arcsine source law is available explicitly). A different legitimate invariant probability distribution on J can give different microscopic entropy while retaining the **pointwise** phase law whenever boundary preorbits have zero mass. More natural measure identification is an outstanding probe, not a fact inferred from this graph.

**Status MC3:** CLASSICAL / PROVED LOCAL, conditional on Parry-law choice.

## 5. Dual E/E″ correlation: positive transported common information persists at arbitrarily long lags

Place E and E″ at two chronological slices of **the same** source law, observing only phase. Write \(X=\phi(x_0)\), \(Y=\phi(x_n)\). The periodic quotient means \(Y=X\oplus(n\bmod2)\) under the stationary Parry law, \(X\sim\operatorname{Bernoulli}(1/2)\). Thus:

\[
 \boxed{\operatorname{Cov}(X,Y)=\frac{(-1)^n}{4};\quad
 I(X;Y)=1\text{ bit}\quad\text{for every }n.}\tag{MC4}
\]

A common-reference transport is declared operationally: **the orientation/lag parity is known and authenticated by hypothesis**. Define \(Y^\sharp=Y\oplus(n\bmod2)\). Then

\[
 \boxed{Y^\sharp=X,\qquad \operatorname{Cov}(X,Y^\sharp)=\frac14\text{ for every }n.}\tag{MC5}
\]

These two covariances are distinct raw and path-adjusted views, as required by an honest phasor/transport diagnostic. The phase sign flip is simply a **real Boolean parity transport**. It is neither evidence for quantum interference nor a physical faster-than-light communication channel. The dual receipts require source name, version, chronology, and a legal phase rule. Correct phase reports do not prove the unseen microscopic path, and string identifiers do not authenticate real measuring devices.

Compare Chaotic SUCC II at **r=4**: two length-m Bernoulli trajectory windows separated by \(n\ge m\) have **no** shared deterministic source-window information (CQ3). Here at the explicitly different r* parameter, the stationary source has a persistent **one-bit period-two factor** and is not strongly mixing: for every k,

\[
 \Pr(E_L\text{ at times }0,2k)=\frac12\ne\frac14
 =\Pr(E_L)^2.
\]

That is exactly why this does **not** contradict the r=4 Bernoulli/Kolmogorov mixing obstruction to a nontrivial periodic factor. Comparing *different sources and different invariant laws* is a critical dependency, not a paradox.

**Status MC4–MC5:** CLASSICAL / PROVED LOCAL for stationary Parry symbolic law and correctly transported lag. Not source-independent correlation.

## 6. Concrete actual-source counterexample: period-two phase does not identify a real trajectory

Take the **real, exact** source points \(x=2/5\in A\) and \(x'=3/5\in B\), both belonging to J*. (The tests certify their finite windows avoid boundaries; inclusion in J* for all future steps has not been independently established for these exact points, so only the tested *finite* trajectory statements use these witnesses.) Their first forward images are **algebraically identical**:

\[
 \boxed{f(2/5)=f(3/5)=6\alpha/25\in C.}\tag{MC6}
\]

For every subsequent time their **actual continuous source states** coincide. Their initial original-source identity is not recoverable from later states or from E's two-valued phase, even though both are legitimate logistic trajectories. The time-zero original-source distinction is recovered only by attaching an independently sourced initial branch identifier (A vs B) or other sufficient original-source evidence. This aligns with PR28's SC1 target-fiber factorization test, PR29's DB3 joint-report requirement, and PR30's source+history dual reconstruction. Neither legal phase predictability nor abstract history capacity authenticates an external observation.

**Status MC6:** PROVED LOCAL for exact indicated finite orbit windows, with original-source information no-go from the equality.

## 7. Steelman → crucible → verdict table

| Hypothesis | Prediction | Discriminator and outcome | Verdict |
|---|---|---|---|
| An E observer can have a nonconstant **deterministic** quotient while its logistic carrier has positive entropy | A valid two-state factor with law independent of which A/B branch occurred | Exact postcritical equality, original interval images, Markov characteristic polynomial and source phase-flip square | **SURVIVES / CLASSICAL under boundary exclusion**, MC1–MC2 |
| Any globally continuous binary phase can flip at every point of J | In particular at fixed point z | f(z)=z forces phi(z)=1-phi(z) | **REFUTED / explicit fixed-point counterexample** |
| Correct E phase must recover every original microscopic state | x and x' with same E record must coincide | x=2/5 and x'=3/5 merge at f(x)=6alpha/25 | **REFUTED / actual source alias** |
| E and E″ will always have same-signed raw correlation | Raw covariance positive for every lag | Cov at odd lag = -1/4, at even lag = +1/4 | **REFUTED / exact signed counterexample** |
| A declared parity common basis can restore their shared information | Transported covariance positive and stable | Correct lag XOR gives exactly +1/4, while incorrect/unsigned raw readings do not | **SURVIVES / CLASSICAL conditional on transport law** |
| An adjacency graph determines the physical invariant density | Parry branch weights physically selected without source law | Parry measure is mathematical construction with no measured/natural-acim identification | **UNVERIFIED / source-map gap** |
| Every chaotic logistic parameter has an equally simple phase quotient | Generic chaotic r supports exact period-two quotient | r=4 Bernoulli/mixing negative control; r* has special PCF source equation | **REFUTED as universal inference** |
| The root phase costs no information/observation resources | n-trajectory path recoverable from one phase bit | 2^ceil(n/2) legal path alternatives from C, 1 phase bit only | **REFUTED / exact cardinality** |

## 8. Calibration and reproducibility

- Implementation: `observational_succ/misiurewicz_phase_quotient.py`, 3D exact rational coefficient field operations for \(\mathbb Q[\alpha]\), verified integer polynomial long division, exact rational root bracket, sign certified via rational intervals and bisection, actual source replay, source-derived 3-cell adjacency, two-state phase quotient, exact Parry chain and dual-source parity receipts.
- Dedicated tests: `tests/test_misiurewicz_phase_quotient.py`, **37** named cases. External-to-implementation arithmetic controls independently divide sampled products by the cubic (240 seeded multiplications, 80 associativity cases); exact 3x3 determinant independently obtains \(\lambda(\lambda^2-2)\); independent graph path enumerator verifies all short paths; actually evaluated fractional initial states verify the source graph; covariance independently enumerates two equally weighted source phases for 32 lags; mutations include irrational/float input, stale source versions, wrong chronology, illegal phase and fixed-point exception.
- Full **offshoot-local** test assembly: 34 preceding PR30 tests + 41 preceding PR32 tests + 37 MC tests = **112 named tests**; validate with `python -m unittest discover -s tests -p 'test_*.py'` in the assembled research workspace. Full GitHub repo CI is a *separate* gate on the exact pushed commit, and will run the preexisting repository tests as well.
- Deterministic probe: `scripts/misiurewicz_phase_quotient_probe.py`, compared bytewise as parsed JSON with frozen `research/2026-10-12/MISIUREWICZ_PHASE_RECEIPT.json`. The receipt explicitly records parameter isolator, original-source collision, graph, Parry law and entropy, raw versus transported lagged covariance, and required rejection flags. No floating-point result is used as a certificate.
- Source provenance: J. C. Sprott (U Wisconsin), original source polynomial, exact SHA of source/test artifacts at GitHub branch; no history or imported archives touched. Scholarship novelty *UNVERIFIED*; earlier teaching materials already study this partition.

## 9. Highest-value next probe: physically meaningful E statistics without assuming Parry source law

**Missing lamp:** identify and validate (analytically or by a rigorously bounded transfer-operator interval scheme) the *natural absolutely continuous invariant measure* \(\mu_{\mathrm{acim}}\) for the same exact \(\alpha\). Under \(\mu_{\mathrm{acim}}\), compute actual branch weights, micro-observable conditional expectations, entropy and recovery debt. The period-two **pointwise** phase law should survive wherever the acim assigns zero mass to exceptional preorbits, but the conditional C→A/B probabilities need not be \((1/2,1/2)\). A decisive probe compares the source-derived \(\mu\) transfer action against uniform/Parry mutants on held-out source intervals. Next build robust finite-resolution/noisy phase instruments: show at what noise rate the raw periodic correlation decays and how much additional communication buys accurate E/E″ alignment.

This is a clean separation of **(i)** operational deterministic phase knowledge, **(ii)** genuine positive-entropy internal dynamics, **(iii)** source-labeled but non-attested measured histories, and **(iv)** a specific yet unpaid physical-prior identification. The project does not obtain a new Archimedean arithmetic interface, Gamma completion, positive Weil form, or RH proof.
