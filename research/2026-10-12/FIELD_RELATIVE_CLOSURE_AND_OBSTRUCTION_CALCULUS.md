# Field-relative categorical closure: simple, ideal-hard, and obstruction-bearing fields

**Research checkpoint:** 2026-10-12. **Source:** user's request to treat SUCC's commuting loop as an *environmentally situated proof object*, rather than as a diagram imposed on a field. **Scope:** static and finite-source observation mathematics plus rigorous (separately proved) infinite examples; source-changing maps and exact finite integer-voltage graph descent. **Status:** classical/PROVED LOCAL mathematics organized into a new-to-project obstruction and repair calculus. No academic priority, physical ontology, quantum experiment, general carrier-construction theorem, all-step Gaussian moat result or RH positivity claim.

**Base:** `femboy2112/SUCC` research PR #37, commit `82f518cda67c9f80054a0b973a5c12bbd248a309`; `main` and `provenance/` unchanged. This dossier extends—not supersedes—the previously validated ideal-frame trichotomy, adaptive source policy, Yoneda proof-transport and Gaussian voltage research. Tests and receipts are exact finite programs; no finite test proves statements involving all infinite stages.

## 0. The actual proposed object

An *environmental field model* is a tuple

\[
(\mathcal C_e,X_e,\mathcal A_e,\{O_{e,n}\}_{n\in\mathbb N},T_e,\mathcal L_e),
\]

where \(X_e\) is the **declared admissible original source class**, \(\mathcal A_e\) the lawful instrument/context arrows, \(O_{e,n}\) the observation history through stage \(n\), \(T_e\) the specified original-source claim, and \(\mathcal L_e\) the separately justified physical/analytic/graphical source law. A *proof-realization* includes an interpreter/decoder for the claim, source provenance, and commuting representations of each physical source arrow and admissible proof transformation. It is **not** a circular argument: independently specified source, observation and claim routes are required to agree.

**Essential repair to language:** “strictly greater than the carrier” is **not** a rigorous claim that a cause is physically outside our universe. At most we can prove that a *given observation interface* or mathematical realization requires an extension: extra probes, retained path history, a covering space, a stronger model class, or a new rule. All classifications below are **relative to \((X,\mathcal A,O,T)\)**. Changing those inputs can change the classification.

## F1 — Claim closure is exactly an observation-fiber factorization

For fixed source class \(X\), observation \(O:X\to Y\), and original-target claim \(T:X\to Z\),

\[
\boxed{\exists d:O(X)\to Z\text{ with }T=d\circ O\iff
 [O(x)=O(y)\implies T(x)=T(y)]\quad(\forall x,y\in X).}\tag{F1}
\]

**Proof.** A decoder yields the implication. Conversely, define \(d(O(x)):=T(x)\); the implication guarantees independence of the representative. This decoder is canonical on the *reachable image*; extension outside that image is unlicensed. For finite \(X\), constructing it or returning the pair \((x,y)\) with the same observation and unequal targets is decidable by exact enumeration. This is the claim-specific form of restricted-observer Yoneda/source-fiber adequacy; it does **not** prove full carrier identity.

**Tests:** exact XOR from two genuinely read-only bit probes; a lone bit probe has an explicit conflicting-source pair; forged source version, missing decoder row and fake pair fail replay.

## F2 — The precise simple / ideal-hard / dark classification

Assume a **fixed original source class**, a compatible, monotone sequence of observation maps \(O_n\), and a limit report \(O_\omega=(O_0,O_1,\ldots)\). Let \(K_n=\ker O_n\) denote the equivalence relation “same observed report.” By F1:

* **Simple for target \(T\)** if \(K_n\subseteq\ker T\) at some finite stage; the closure rank \(\rho(T)\) is the first such stage.
* **Ideal-hard / ideal-analytic for \(T\)** if \(\bigcap_nK_n\subseteq\ker T\) but no finite stage suffices; \(\rho(T)=\omega\) is an *ideal set-theoretic identification*, not a physically executed \(\omega\)-step or an effectively computable decoder.
* **Dark / “fucked” relative to this interface** if \(\bigcap_nK_n\not\subseteq\ker T\). In this case a pair of sources with all observations equal and unequal target values is the decisive obstruction, if such a pair exists in the stated source class.

This exhausts the **static target-factorization** possibilities when the limit report is defined. It does not exhaust environmental realism: Section F7 explains why lawful experimental ordering can defeat a statically adequate probe family, and F6/F8 explain why local source sections or geometric charts may not glue.

### F2a. A finite carrier cannot require genuine omega-only identification

**Theorem (finite stabilization).** If \(X\) is finite and \(O_\omega\) distinguishes every pair with different \(T\)-value, some finite \(O_N\) already distinguishes all such pairs. **Proof:** there are finitely many target-different pairs. Choose a finite distinguishing stage for each and let \(N\) be their maximum. Further, any increasing equivalence-partition sequence on an \(m\)-element set has at most \(m-1\) *strict changes*, although the timestamps of those changes can be arbitrarily delayed.

This is nontrivial for SUCC semantics: **infinite-limit closure truly requires an infinite original source class, a changing source/model class, or additional analytic/continuity structure**. Unlimited finite-state search does not automatically have an omega-only result.

### F2b. Genuine omega, in two orthogonal infinite classes

1. Source \(X=\{\infty\}\cup\mathbb N_{\ge1}\), probes \(p_n(k)=\mathbf1_{k=n}\), \(p_n(\infty)=0\), target \(T(\infty)=0,T(k)=1\). Every finite prefix aliases \(\infty\) with a later \(k\), but the full prefix tower distinguishes it from all \(k\). **Ideal-hard for this claim** by a written \(\forall k\exists n\) proof. Executing 100 probes is not the proof of the infinite statement.
2. Compact Cantor source \(X=\{0,1\}^{\mathbb N}\), continuous real-valued target \(T(x)=\sum_{j\ge1}2^{-j}x_j\), and coordinate probes. No finite prefix determines \(T\) exactly for all \(x\); all prefixes together do, and the uniform tail bound is \(\le2^{-n}\). Thus **even compactness and continuity can permit genuine omega-exact closure for an infinite-valued target**.

### F2c. Infinitely many probes need not have a source-realized limit

Let \(X=\mathbb N_{\ge1}\) and \(p_n(k)=\mathbf1_{k\le n}\). The all-zero prefix through stage \(N\) has a realizing source \(k=N+1\), but the full infinite all-zero record has **no** realizing element of \(X\). This is the noncompact failure of the finite-intersection property. One must separately check **source realizability** rather than interpreting every compatible formal infinite report as an actual carrier state. Analytic germs vs divergent formal Taylor jets give an analogous regularity failure.

## F3 — Compactness turns suitable point separation into finite proof support

Let \(X\) be compact Hausdorff, \(T:X\to Z\) continuous with \(Z\) finite discrete, and \(\{p_j:X\to Y_j\}\) continuous to Hausdorff target spaces. Suppose for every \(x,y\) with \(T(x)\ne T(y)\), some \(p_j(x)\ne p_j(y)\). Then **a finite family of probes determines \(T\)**.

**Proof:** \(D=\{(x,y):T(x)\ne T(y)\}\) is closed in compact \(X^2\), hence compact. Sets \(D_j=\{(x,y)\in D:p_j(x)\ne p_j(y)\}\) are open in \(D\) and cover it. A finite subcover exists. F1 supplies a decoder for the resulting finite joint observation.

**Quantitative extension.** For metric target \(Z\), replace \(D\) by the compact set \(D_\epsilon=\{(x,y):d(T(x),T(y))\ge\epsilon\}\). Some finite probes ensure that two sources with equal probe reports have target distance strictly below \(\epsilon\); this proves **uniform approximate reconstruction**, not necessarily exact finite identification. Cantor-target example F2b explicitly shows the distinction. This is classical compactness, not an invented global observer.

## F4 — An entire family of admissible probes can still be undecidable to classify

**Halting reduction (in the fixed 2-state setting).** For a Turing machine index \(e\), define the computable probe family on \(X=\{0,1\}\):

\[
p_{e,n}(0)=0,\qquad p_{e,n}(1)=\mathbf1_{\{e\text{ halts within }n\text{ steps}\}},\qquad T(x)=x.
\]

Each finite \(p_{e,n}\) can be evaluated by running \(e\) for at most \(n\) steps. The target is finitely identifiable **iff** \(e\) eventually halts. Otherwise it is dark under every admitted probe. Thus no algorithm taking an arbitrary uniform program for the probe family can always decide “simple versus dark.” This is a many-one reduction from halting; it does **not** assert that RH is undecidable or that the source carrier itself is externally inaccessible. The finite executable test evaluates only **supplied bounded halting results**, not an oracle for halting.

This also distinguishes finite source cardinality from effective recognition of sufficient observations.

## F5 — Three distinct commuting-square gates under carrier transformation

Let \(h:X\to X'\) be the genuine **declared** carrier intervention, \(O:X\to Y\) and \(O':X'\to Y'\) the old/new public observations, \(T:X\to Z\) the ORIGINAL claim, and \(T':X'\to Z\) its proposed transported meaning. Three independent questions are:

1. **Representation covariance:** a report map \(R:O(X)\to Y'\) satisfying \(O' h=RO\) exists iff \(\ker O\subseteq\ker(O'h)\).
2. **Original-source truth preservation:** \(T=T'h\) pointwise on \(X\).
3. **Original-claim decodability after intervention:** a post-report decoder exists iff \(\ker(O'h)\subseteq\ker T\).

Each is checked independently by source-fiber enumeration and returns the first explicit rival when false. The first two can hold while the third fails (an inadequately observed or erased original target); conversely a new high-precision observer can prove the target even though its observations cannot be predicted from the former coarse view. **A commuting square alone does not certify a proof.** For invertible frame changes plus adequate readouts the gates naturally succeed, just as a Lorentz transformation preserves some scalars while changing coordinate reports. No actual spacetime or cognitive metric is inferred here.

## F6 — Pairwise-local evidence may be globally unrealizable

Take the even-parity three-bit source class \(X=\{000,011,101,110\}\). Suppose the three local observers each report their coordinate to be 1. Each *pair* of such reports is realized by a legitimate source, but the triple (111) is absent from \(X\). Therefore

\[
\forall i<j\quad K(\text{report}_i,\text{report}_j)\ne\varnothing,
\qquad K(\text{all three})=\varnothing.
\]

This is the elementary finite-global-section/contextual-compatibility problem. A minimal unsatisfiable evidence core of size three is an exact certificate; no “global truth” may be concluded by explosion from the empty fiber. The broader sheaf contextuality framework of Abramsky–Brandenburger (2011) already characterizes global-section obstructions. **Do not** mistake this declared classical parity-source table for a physical Bell/Kochen–Specker experiment.

## F7 — Environmentally situated loop: integer-voltage path groupoids

For a finite graph \(G\) with integer displacement \(w_e\in\mathbb Z^d\) on each directed dart (reverse contributes \(-w_e\)), a vertex potential \(g:V(G)\to\mathbb Z^d\) obeys

\[
g(v)-g(u)=w_e\qquad(u\xrightarrow{e}v).
\]

**Theorem (voltage descent / classical).** Such a potential exists iff every closed walk has zero signed total displacement. **Proof:** telescope the edge equations in the forward direction. Conversely choose a spanning forest, integrate along its trees, and check each non-tree edge. A bad edge creates a finite closed source walk consisting of the tree path to its tail, the offending edge and the reverse tree path from its head, with provably nonzero total displacement. Self-loops and parallel edges are indispensable. The proof is classical voltage-graph theory and the additive torsor case of a flat global section; our code constructs **both types of exact certificate**.

**Three-edge winding:** edges \(0\to1,1\to2,2\to0\) each have voltage +1. Each single-edge chart admits a local potential, yet the completed circle has holonomy +3 and no global potential. The defect is not observational darkness: even complete knowledge of all three edges establishes the **impossibility** of the proposed globally single-valued potential.

**Authentic arithmetic holdout:** In \(\mathbb Z[i]/(5)\), avoid norm divisibility by 5. There are 16 survivors. The genuine unit-step Gaussian norm-sieve graph admits an escaping nonzero source-voltage loop. For the simultaneous authentic norm-5 and norm-13 sieve modulo 65, there are 2,304 survivors and 4,356 directed unit-step darts. Every quotient component has an integrating potential; independent connected-component counting gives 243 components and largest component 580. This is a sieve-overapproximation result, NOT an independent theorem for all Gaussian-prime step lengths or a proof about prime-only escaping walks.

A groupoid diagram “commutes” here because all actual displacement paths integrate to a single potential. In a general nonabelian measurement scenario, ordered path holonomy and original-claim invariance must be checked instead. **Do not promote the additive H¹ equation to a necessary-and-sufficient obstruction for arbitrary Set-valued sheaves.** General cohomological contextuality tests can have false positives/incompleteness; see Abramsky–Mansfield–Barbosa (2011) and Carù (2017).

## F8 — Environmental holonomy is claim-relative

Let a finite group \(G\) of invertible frame transformations act on source class \(X\), generated by \(g_1,\ldots,g_k\), and \(T:X\to Z\) a target. Then

\[
\boxed{T\text{ is invariant under every generated frame path}\iff
 T(g_jx)=T(x)\quad\forall j,x.}\tag{F8}
\]

The proof follows by composition and inverses (for a bijective generator, invariance implies inverse invariance). Thus checking a finite generating set suffices for arbitrarily long frame histories. In \(\mathrm{GL}(2,\mathbb F_2)\), two noncommuting shears fix zero, and permute the three nonzero vectors. “Source is zero” descends to the frame orbit quotient, but original XOR/parity does not. **Claim closure can survive genuine source-state holonomy even when global state/frame alignment fails.** Full observation identity and original-source claim invariance remain distinct requirements.

## F9 — A mathematically provable new-probe repair is an exact hitting-set problem

Given a baseline observer \(O_0\), let \(D\) be the set of **target-disagreeing source pairs still aliased by \(O_0\)**. Each candidate new probe \(p_j\) separates a subset \(S_j\subseteq D\). A family of probes makes the target decidable iff \(\bigcup_jS_j=D\). Thus smallest cardinality probe repair is exactly minimum set cover on the conflict pair universe.

**Complexity theorem (classical reduction).** Every instance of SET COVER with universe \(U\) and subsets \(S_j\) reduces to target-relative probe repair with source class \(X=U\times\{0,1\}\), baseline observation \(O_0(u,b)=u\), target \(T(u,b)=b\), and probes \(p_j(u,b)=b\) for \(u\in S_j\), otherwise zero. Under the baseline, the **only** target-disagreeing aliased pairs are \(((u,0),(u,1))\), and probe \(j\) separates that pair iff \(u\in S_j\). Therefore an at-most-\(k\) repair exists iff an at-most-\(k\) set cover exists. Membership in NP follows by checking finitely many pairs. The explicit general minimum-repair decision problem is consequently NP-complete. This is a reduction to an old NP-complete problem, not a new complexity class.

**Greedy failure:** Universe \(\{0,1,2,3,4,5\}\) and subsets \(\{0,1,2,3\},\{0,1,4\},\{2,3,5\}\). Greedy largest-first chooses the first and then needs the other two (three probes), while the last two alone cover everything (two probes). The exact checker returns the two-probe optimum and an independently checked minimality certificate.

**Scope firewall:** these are **static** source probes. A winning static cover does NOT imply that those instruments can be executed sequentially on one mutable physical carrier. See F10.

## F10 — Probe sufficiency is not lawful policy sufficiency

The previously implemented SUCC destructive two-bit source supplies a decisive orthogonal control. The jointly evaluated static map \((p_a,p_b)\) determines original XOR. But in the declared destructive carrier, reading \(p_a\) first irreversibly erases original \(b\), and vice versa. Every adaptive one-carrier strategy must make some first choice; either choice makes two opposite-parity original sources permanently indistinguishable. The complete finite AND/OR winning-set computation already proves no uniform sound policy. Conversely, a lawful reversible source transformation with outcome-dependent follow-up can have a winning two-step **adaptive** policy although no fixed two-step word wins. Thus:

\[
\text{static coverage}\not\Longrightarrow\text{executable decision policy},
\]

and the dynamic problem is *not* solved by enumerating only fixed probe permutations. This is classical active automata planning, consistent with previous SUCC CT5 and Y5–Y11. Genuine parallel experiments require separately prepared equivalent source copies or a verified reset protocol, not copies of a simulation table.

## F11 — Realization lower bounds without metaphysical origin

For any scalar autonomous linear system \(y_n=c^{\mathsf T}A^n b\) with state dimension \(d\), the Hankel matrix of observed outputs factors as

\[
H_{ij}=y_{i+j}=(c^{\mathsf T}A^i)(A^jb),\qquad\operatorname{rank}H\le d.
\]

For \(y_n=1+(-1)^n\), the observed \(2\times2\) minor is \(\begin{psmallmatrix}2&0\\0&2\end{psmallmatrix}\) and forces \(d\ge2\). A two-state realization exists with \(A=\operatorname{diag}(1,-1),\ b=(1,1)^{\mathsf T},\ c=(1,1)^{\mathsf T}\). Thus the lower bound is sharp **within the specified realization class**, and proves no claim of external ontology. The repository already implements Hankel bounds in its carrier-relative research track; this checkpoint treats them as a separate source-class requirement, not a new proof.

## F12 — The complete *obstruction profile*, not a single scalar complexity score

A field-relative proof situation should report at least:

\[
\boxed{\mathfrak O=(\rho_T,\ R_{\mathrm{source}},\ H_{\mathrm{loop}},\
 D_{\mathrm{carrier}},\ N_{\mathrm{context}},\ P_{\mathrm{provenance}}).}
\]

Here \(\rho_T\) is the static closure depth; \(R_{\mathrm{source}}\) checks one actual global source realizes all reports; \(H_{\mathrm{loop}}\) is the path-integration obstruction; \(D_{\mathrm{carrier}}\) checks adaptive policy feasibility under actual carrier updates; \(N_{\mathrm{context}}\) checks source/observation/target commutation; and \(P_{\mathrm{provenance}}\) is external source authentication. **The first five admit mathematical checkers in their declared finite domains. The sixth cannot be produced merely by typing matching `source_id` strings.** Their counterexamples are independent in scope; they must not be collapsed into a numerically appealing but meaninglessly scalar "knowledge" score.

**Conditional construction/verification theorem.** If a finite candidate model comes with (i) a nonempty source fiber for actual received evidence, (ii) a target constant on that fiber, (iii) source-correct compatible context transports for any claimed interventions, (iv) a verified global potential for every required lattice chart, and (v) a lawful observation history or independently attested experiment, then its final target claim and associated graph integrability are certified **relative to the declared source laws**. This is a conjunction of independent proven gates, **not** a theorem that the physical universe is accurately described or that arbitrary RH positivity follows.

### A no-go on any universal fixed "proof geometry"

The five mathematical dimensions cannot be inferred from the closure rank alone. In the parity triple, each local report has a globally declared source but their intersection is empty. In the winding triangle, source edge data may be entirely known while the proposed global potential does not exist. In destructive parity, full hypothetical static observation is sufficient while the actual policy has no winning strategy. In a lossy carrier update, observation covariance may hold while the original target becomes undecodable. **Different obstructions require different repairs**: a separator, an additional source-restricting axiom, an overlap lift/path witness, an alternative experiment or fresh source preparation, and/or a stronger source-law identification.

## F13 — Failed moonshots: what was killed and why

1. **"Omega automatically closes every environmentally consistent diagram."** False twice: smooth flat functions remain invisible to all origin jets, and noncompact local evidence can have no realized global source. Formal inverse limits and physically traversed infinity are different.
2. **"Every local solution glues if each pair agrees."** False: three even-parity reports pairwise realize but jointly do not; and a graph cycle can carry nonzero holonomy despite every single-edge patch solving perfectly.
3. **"More observations always repair a global loop."** False for fixed insufficient probe families and for new loop classes appearing at finer sieve periods. The Gaussian all-step existence theorem needs arithmetic coverage beyond local functoriality.
4. **"All possible probes on paper imply a winning experiment."** False under destructive carrier backaction; CT5 complete AND/OR policies supply a separate and strictly stronger gate.
5. **"A common carrier source identifier verifies the real environment."** False. Exact tables and Git SHAs verify internal declarations/bytes, not genuine external origin. Original-source ontological identification remains relative to available physical probes and lawful instrument calibration.
6. **"If a categorical loop closes, RH follows."** False: the previous genuine-Euler/self-Fourier test-function counterexample has a fully symmetric completed functional equation and auxiliary off-critical zeros. The RH-hard missing theorem is source-identified completion plus **positive-semidefiniteness of the actual Weil/Suzuki form**, not a commuting functional equation.
7. **"A finite number of strict partition refinements bounds the time needed."** False: a two-state source may remain observationally aliased for an arbitrarily long computable delay before a single separating probe becomes available.

## F14 — Exact next research targets

1. **Source-changing proof-support fibration.** Prove a Beck–Chevalley/base-change theorem for *verified original-source claims* and actual instrument kernels, with composable receipt semantics. Identify exactly when proof evidence survives lost or noncommuting carrier state. Include a state-changing counterexample with original-target semantic disagreement.
2. **Adaptive minimal repairs.** Generalize F9 from static hitting set to executable AND/OR games, preserving source versions and accounting for destructive action/reset costs. Classify when a mathematically adequate cover has no physical policy and prove complexity or approximation bounds on the hybrid problem.
3. **Contextual sheaf of source laws.** Develop sheaf restrictions with realizability, coherence, and regularity separately from additive torsor cohomology. Never use H¹ vanishing as an iff for arbitrary nonlinear Set-valued constraint sheaves.
4. **Infinity/regularity theorem.** Extend the \(\rho\)-classification to represented spaces and computable claims: effective convergence moduli, compactness, and source realization. No finite sample table may be promoted to omega completeness.
5. **Independent formal proof.** Port F1,F2a,F5,F7,F9 to Lean with correct finite source/edge domains and construct proof-object verifiers. Compare with Abramsky/Brandenburger contextuality and standard query complexity/cover theory before any novelty claim.
6. **Arithmetic source-derived positivity.** Find a legitimate new invariant reading *true* prime powers, exact finite-/Archimedean test functions and the completed Gamma factor and prove it is the **full** Weil/Suzuki form, then prove nontrivial positive-semidefiniteness. Keep fake composite impulses, matched non-Euler models, unknown-zero reading and source-dependent test-function mutations as negative controls. No step in F1–F13 supplies this theorem by itself.

## Reproducibility and citations

Additive source: `observational_succ/field_relative_closure.py`, `field_probe_repair.py`, `field_context_descent.py`, `field_limit_countermodels.py`; exact tests in four matching `test_field_*.py` files, script `scripts/field_relative_obstruction_probe.py` and saved JSON receipt. The local 65 tests include **420 independently enumerated random source tables**, **280 independent random set-cover instances**, **450 independently propagated integer-voltage graph checks**, plus genuine prime 5/13 Gaussian sieve checks. Every finite probability/count/graph quantity is exact; no floating oracles. This is a finite proof engineering artifact—not a proof assistant kernel implementation.

Background: [Abramsky–Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality* (2011)](https://arxiv.org/abs/1102.0264), [Abramsky–Mansfield–Barbosa, *The Cohomology of Non-Locality and Contextuality* (2011)](https://arxiv.org/abs/1111.3620), [Carù, *On the Cohomology of Contextuality* (2017)](https://arxiv.org/abs/1701.00656), [Frohme, *Active Automata Learning with Adaptive Distinguishing Sequences* (2019)](https://arxiv.org/abs/1902.01139), [Bohr–Mollerup theorem (DLMF)](https://dlmf.nist.gov/5.5), and the project's own pinned historical research. The proofs here do not depend on the unrefereed OpenAI Gaussian all-D existence claim.

**Scientific boundary:** Claim IDs, the exact test count and CI validation must refer to the committed head and the repository's authoritative ledger; the source is intentionally not merged to `main`.

## F15 — RH moonshot falsifier: arbitrarily long symmetric finite analytic shadows hide off-line zeros

**Theorem (exact rational polynomial family, PROVED LOCAL):** Fix any integer \(n\ge0\), and choose \(z_0=1/4+i/10\) strictly inside the critical strip, off the critical line. There exists a polynomial \(F_n(s)\in\mathbb Q[s]\) satisfying simultaneously

\[
F_n(s)=F_n(1-s),\qquad F_n^{(k)}(0)=\frac{d^k}{ds^k}1=0\quad(1\le k\le n),\quad F_n(0)=1,\qquad F_n(z_0)=0.
\]

**Constructive proof without any input of zeta zeros.** Put \(g(s)=s(1-s)\), and \(g_0=g(z_0)=79/400+i/20\). The inverse power \(h=g_0^{-n-1}=u+iv\) has rational real and imaginary parts. Since \(\Im(g_0)=1/20\ne0\), set rational

\[
B=v/\Im(g_0),\qquad A=u-B\Re(g_0).
\]

Then \(A+Bg_0=h\). Define

\[
\boxed{F_n(s)=1-g(s)^{n+1}[A+Bg(s)].}
\]

It is a rational polynomial symmetric under \(s\mapsto1-s\), its difference from the constant 1 vanishes to order \(n+1\) at zero, and \(F_n(z_0)=1-g_0^{n+1}h=0\). Because coefficients are real, conjugation and reflection supply the corresponding quartet. The Python checker constructs the coefficients using exact \(\mathbb Q(i)\) operations, verifies the FULL polynomial identity \(F_n(s)=F_n(1-s)\) symbolically, and checks \(F_n(z_0)=0\) exactly for orders 0–12 and several other rational points in the strip.

This falsifies the implication “any finite analytic jet at a boundary point + exact functional-equation symmetry determines zero locations.” It is **only** an analytic test-family counterexample: \(F_n\) is not the completed zeta function, need not have any genuine Euler factors or Gamma source, and has no claimed positive Weil form. A source-correct finite/Archimedean construction and global positivity remain missing and cannot be supplied by this example.

**Additional elementary positivity firewall:** the pointwise nonnegative kernel \(K(s,t)=(s+t)^2\) on \(\{0,1\}\) gives matrix \(\begin{psmallmatrix}0&1\\1&4\end{psmallmatrix}\), determinant -1 and negative quadratic value \(\langle(3,-1),K(3,-1)\rangle=-2\). Thus nonnegative pointwise kernel entries do NOT imply positive-semidefiniteness, reproducing in a different simple model the project's earlier Weil-positivity warning. Mathematical positivity **must be of the exact completed form**, not a manufactured positivity of its reports.
