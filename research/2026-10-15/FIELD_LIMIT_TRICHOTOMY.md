# ATOM II — SimpleFields, IdealHardFields and FuckedFields as effective finite-to-global theorems

**Date:** 2026-10-15. **Working branch:** research/observer-tate-bijective-descent-2026-10-15 (on Phoenix-II main 03db4420, not merged). Parent mathematical work: ATOM profinite-model/finite-Tate chart, compact adelic solenoid, and pre-existing finite-source field_relative_closure, field_limit_countermodels, no_ghost, recursive_operator_gluing. No zero data, empirical source claims, or old source mutation. **RH PROVED: NO.**

## 0. Recover the user proposal precisely

The user's intent is NOT to define classes by whether a mathematical object is “infinite.” Every interesting field has an infinite mathematical definition. The desired distinction is whether an **observer can construct, prove, or distinguish the right global target using its source laws and its allowed causal toolkit.**

A correct field label must therefore be indexed by a **triple**:
\[
\boxed{\text{FieldClass}(\mathsf{Source},\mathsf{Target},\mathsf{Tools})}.
\]
Different targets—recover source identity, evaluate a finite observable, produce any global witness, prove a formula, or certify a signed quadratic form—can have different computational classifications on the SAME underlying carrier. Changing the toolkit may repair a Fucked observational gap without changing mathematics. Changing the intended global ambient source can turn a provable limit into a nonexistent *original-source* lift.

A useful uncoupled diagnostic vector is:
\[
(\text{finite stage decision},\text{compatibility},
\text{source adequacy},\text{global existence},\text{uniqueness},
\text{finite symbolic representation},\text{computable witness},
\text{mathematical proof},\text{positive source cross-growth}).
\]
These are NOT one probability or one total “difficulty score.”

### Accurate meanings

**SimpleField (relative to the target):** a verified finite symbolic program/normal form constructs or computes exactly the requested global observable or source object in the representation agreed upon. If the output is a nontrivial infinite sequence, “finite executable” means a finite program plus a proof of lawful source compatibility that computes its requested finite coordinates in finite time—not enumerating ALL infinitely many coordinates before returning.

**IdealHardField:** mathematical source laws supply a finite classical proof of existence/target truth, yet the declared effective toolkit cannot construct an exact global witness (or supply the demanded execution) in finite algorithmic work. A *mathematically proved* impossibility of a computable selector makes the distinction sharp; mere slowness or a missing algorithm does not.

**FuckedField:** separate at least three modes:
1. **EMPTY GLOBAL SOURCE:** the specified global source model provably does not exist, even though every finite observation horizon is satisfiable;
2. **NONFAITHFUL TOOLKIT:** the permitted future action/readout closure identifies distinct source states with different target values;
3. **PHANTOM ORIGINAL SOURCE:** every finite observation can be matched by some original source, but there is no ONE original source realizing the complete global model. This must be read with the quantifiers in the right order.

A claim “we cannot currently prove or disprove” is often a fourth **UNVERIFIED/DARK WITHIN TOOLKIT** status, not a theorem of mathematical impossibility. This memo will never infer an intrinsic “RH is Fucked” from failure to find a finite certificate.

## 1. SimpleField: a source-faithful finite executable law for an infinite limit

Consider \(X_n=\mathbb Z/2^n\mathbb Z\) with reduction. Define the source section \(x_n=1\bmod2^n\). The program
\[
\texttt{given n: return 1 \% (2**n)}
\]
and the algebraic identity \(1\bmod2^n=(1\bmod2^{n+1})\bmod2^n\) provide an exact uniform constructor for ONE global source element of \(\mathbb Z_2\).

Its infinite source LAW is finitely described and its every finite coordinate is executable with a finite amount of work. This does NOT imply all elements of \(\mathbb Z_2\) are computable or that any computer can physically output infinitely many digits at one instant. It is therefore correctly a **SimpleField for the specified constant source point**, not for arbitrary profinite unknown-state identification.

**Source model-of-model link:** the ATOM-I bijection Hom_Q-alg(colim Q^(Z/m),Q)≅Zhat is classical, but recovering the full evaluation character of a *particular unknown point* can still require unbounded observations. A finitely described categorical isomorphism is not an oracle giving every hidden point's source identity.

## 2. IdealHardField: a fully effective finite system whose global witness is uncomputable

There exists a DECIDABLE binary tree \(T\subseteq\{0,1\}^{<\omega}\), closed under prefixes and with a node at every depth, but with NO COMPUTABLE infinite path. This is the classical Kleene-tree phenomenon (see authoritative elementary computability notes by Andrew Marks, Chapter 23, https://math.berkeley.edu/~marks/notes/computability_notes_v1.pdf).

We instantiate it with an **explicit bounded universal binary Turing machine enumeration**, implemented in field_limit_trichotomy.py. A finite program table has n states, 2 symbols, two movement directions and two terminal output instructions; Cantor unpairing of natural e enumerates all such finite programs. Input e is unary 1^e, so all partial computable maps N→{0,1} occur in the enumeration \(\varphi_e\). The code checks only finite stage simulations, with an exact declared time budget.

Define
\[
\boxed{\sigma\in T\quad\Longleftrightarrow\quad
\forall e<|\sigma|\
[\varphi_e(e)\downarrow_{\le|\sigma|}=b
\Rightarrow \sigma(e)\ne b].}
\tag{IDL-KLEENE}
\]

**Finite membership decidable:** for each e<|\sigma|, simulate exactly |\sigma| steps, inspect any halted binary output and check the corresponding bit. This terminates.

**Prefix closure:** if a machine halts within |\tau| steps for a prefix \(\tau\preceq\sigma\), it also halts within |\sigma| steps, so valid \(\sigma\) implies valid \(\tau\).

**All finite levels inhabited:** for each depth n, choose \(\sigma_n(e)=1-\varphi_e(e)\) when the bounded computation halts, and \(\sigma_n(e)=0\) otherwise. This is a finite algorithm with \(\sigma_n\in T\). These independently produced strings need **NOT** be nested when n varies; treating them as one compatible infinite witness would be a serious logical error.

**Global existence PROVED:** finite binary branching plus a node at every depth gives an infinite path by classical König's lemma. Equivalently, define the complete infinite diagonal-complement bit sequence using excluded middle for each halting predicate, and verify every prefix. Neither proof computes that path.

**NO computable path PROVED:** if an infinite path f were a computable binary-valued function, choose e indexing precisely f in the effective universal TM enumeration. Since \(\varphi_e(e)=f(e)\) eventually halts, the tree's constraint at every sufficiently long prefix requires \(f(e)\ne\varphi_e(e)=f(e)\), contradiction.

Therefore
\[
\boxed{
\forall n\;\exists\,\sigma_n\in T\cap2^n,\qquad
\exists\,f\in[T],\qquad
\nexists\,\text{computable }f\in[T].
}
\tag{IDL-IDEALHARD}
\]
This is a genuine **IdealHard** witness for the *task of producing a computable global path*, relative to classical mathematics and standard finite Turing computation. Existence is PROVED by a finite proof, yet no algorithm can output a correct full path. It is NOT an undecidable RH theorem. The code verifies bounded simulation and finite prefixes, not infinitely many stages by execution.

### A useful consequence: uniqueness changes the computational story

For a DECIDABLE finitely branching binary tree with exactly ONE infinite path, that path IS computable (Andrew Marks' notes, Exercise 23.6). The algorithm for its first k bits searches increasing finite tree levels until all surviving level-n nodes share a length-k prefix. If the promised unique path exists, this search eventually terminates: otherwise finite branching compactness would yield a second infinite path through an incompatible branch. There may be no known uniform TIME bound on the search.

Thus:
\[
\boxed{\text{effective compactness + UNIQUE path}
\Longrightarrow \text{computable path (per finite query)}.}
\tag{IDL-UNIQUE}
\]
Consequently our effective Kleene tree, which has no computable path, necessarily has MORE THAN ONE infinite path. The loss of computable selection is not compatible with a uniquely determined path under ALL the preceding effective compact binary hypotheses. In more general spaces without effective compactness or decidable presentations, uniqueness does not give this same algorithm.

This is arguably the most consequential theorem for SUCC's ambition to make recursive modeling BIJECTIVE: SOURCE FAITHFULNESS, EFFECTIVE COMPACTNESS, and GENUINE GLOBAL UNIQUENESS are load-bearing separately.

## 3. FuckedField-A: local satisfiability with EMPTY global source

Let \(X_n=\{m\in\mathbb N:m\ge n\}\) and let every bonding map X_(n+1)→X_n be the inclusion (same integer value). All stages are nonempty. For every finite horizon N, a globally compatible choice through X_1,...,X_N is simply m=N. But a full inverse-limit point would require ONE fixed integer m≥n for every n, which is impossible.

\[
\boxed{
\forall N\;\exists m_N\in\bigcap_{n\le N}X_n,\qquad
\bigcap_{n\ge1}X_n=\varnothing.
}
\tag{F-NONCOMPACT}
\]
There is no mysterious infinite proof hidden here: the obstruction is fully proved by the Archimedean unboundedness of N. The stage sets are infinite discrete/noncompact, so compactness and finite-branching König hypotheses do not apply. This is genuinely a *no global source* example despite perfect finite-prefix execution.

## 4. FuckedField-B: the phantom-versus-original source map

The earlier ATOM source constructor proved \( \mathbb Z\hookrightarrow\widehat{\mathbb Z}\) is dense, not onto. Fix the explicit CRT profinite point h with h_2=1 and h_p=0 for each odd p. For any finite set of moduli—or a factorial prefix—CRT produces an integer z_N matching h under ALL those observations. At the growing factorial moduli 2,6,24,120, the canonical finite integer representatives are 1,3,9,105.

Nevertheless NO single integer matches all stages: all 3^k coordinates zero imply integer z=0, while its 2-coordinate would have to be 1. Thus the correct mathematics is
\[
\boxed{
\forall N\;\exists z_N\in\mathbb Z\
[O_{\le N}(z_N)=O_{\le N}(h)]
\quad\text{but}\quad
\neg\exists z\in\mathbb Z\;\forall N\
[O_{\le N}(z)=O_{\le N}(h)].
}
\tag{F-PHANTOM}
\]

**Critical quantifier correction:** this does NOT produce one fixed integer z observationally indistinguishable from h at EVERY modulus. The full separating profinite tower eventually distinguishes h from each *particular* integer; the distinguishing stage depends on that integer. It is the global property "is there any integer source?" that no SINGLE FINITE residue prefix can refute. A mathematician with the full CRT SOURCE DESCRIPTION CAN PROVE h is not an integer. The observer with only finite-prefix access cannot resolve that claim in the claimed observation language. Fucked is therefore SOURCE/TOOLKIT RELATIVE, not an intrinsic proof-impossibility about this fully described h.

## 5. FuckedField-C: truly nonfaithful observational closure

For exact source states S={(x,t):x,t∈{0,1}}, the allowed action toggles the visible x and preserves the private tag t; the only authorized observation reads x. Hence sources (0,0) and (0,1) give IDENTICAL action/report trees for every finite word, and indeed every infinite sequence of authorized actions if no new probe is introduced. The source quotient map (x,t)↦x is noninjective. If the requested target is t, the toolkit is not separating.

A new independently authorized tag-readout repairs the defect. It was not present in the original toolkit, so a source certificate from that original toolkit could not claim the repair occurred automatically.

This is operational nonfaithfulness, not an inconsistent global inverse limit. Fucked modes A/B/C must be separately recorded.

## 6. The general compact-source gluing theorem (the precise positive counterpart)

Let X be compact Hausdorff, and each source-indexed observation constraint be a CLOSED subset F_i⊂X. If every finite intersection is nonempty, then
\[
\boxed{\bigcap_iF_i\ne\varnothing.}\tag{COMPACT-LIFT}
\]
Proof: the complements X\F_i are open. If the total intersection were empty, the complements would cover X; compactness would supply a finite subcover, contradicting finite intersection consistency. If the observer family separates original points, the global fiber contains AT MOST ONE point. Existence plus separation gives exactly one original source.

This theorem is NOT constructivist executable by itself, as the Kleene countermodel shows. It guarantees mathematical existence under compactness, not a computable witness. For effective decidable finitely-branching source trees with uniqueness, the additional unique-path effectivity theorem supplies an algorithm.

These conditions correspond directly to SUCC's *source construction/certification* axis:
- **Compactness/source properness** guards against no-global-source ghosts.
- **Separating observer probe closure** guards against nonunique source identity.
- **Effective finite stage presentation + unique limit** can upgrade the outcome to Simple/constructible.
- **Classical compactness with no computable selector** can give IdealHard.
- **Noncompactness or nonseparation** yields precise Fucked subtypes or unresolved source-map claims.

## 7. How this actually changes the Tate → Weil → RH research program

**Tate-adeles:** ATOM's true arithmetic carrier \(\mathbb A_f=\mathbb Q+\widehat Z\), \(\mathbb Q\cap\widehat Z=\mathbb Z\), and \((\mathbb R\times\widehat Z)/\mathbb Z\cong\mathbb A_\mathbb Q/\mathbb Q\) are CLASSICAL and constructive from finite source fractional cells. Its global SOURCE is not a pure compact finite quotient tower (the real place requires another topology). Each Q_p Schwartz–Bruhat test has a finite SUPPORT×PRECISION chart; the full function space is an infinite filtered union. Source reconstruction alone is not analytic continuation or multiplicative zeta positivity.

**Tate-complete SUCC** needs an effective-enough presentation of the full restricted adelic Schwartz test space, global additive Fourier/diagonal Poisson, compatible Mellin/Hecke local factors, and source-valid convergence/continuity. Many exact *finite queries* might be computable even if the global proof requires sophisticated analytic theorems. Therefore calling "Tate itself IdealHard" without a target/output and toolkit is NOT justified.

**Weil/Suzuki RH:** Let \(Q_\zeta\) be the authentic completed signed Weil form on LF test \(\mathcal D=C_c^\infty(\mathbb R)\). A countable smooth finite source-test dictionary with LF-dense span gives the classical equivalence
\[
Q_\zeta\ge0\;\forall f\in\mathcal D
\quad\Longleftrightarrow\quad
G_N=(Q_\zeta(d_i,d_j))_{i,j\le N}\succeq0\;\forall N.
\tag{RH-DENSE}
\]
A strictly negative genuine source test, IF it exists, is witnessed by some finite dense dictionary combination. With effective rigorous source evaluation, the search for a negative witness is therefore **semidecidable in principle**: enumerate finite vectors and rational upper error bounds until an upper bound is negative. This does not supply the stage at which such a witness would appear or establish RH's truth. An indefinitely positive finite search is not a mathematical proof of universal positivity.

The positive case demands a uniform SOURCE theorem ensuring every enlargement's original interaction is lawful:
\[
G_{N+1}=\begin{pmatrix}G_N&B_N\\B_N^*&D_N\end{pmatrix},
\quad\operatorname{Ran}(B_N)\subseteq\operatorname{Ran}(G_N),
\quad D_N-B_N^*G_N^\dagger B_N\succeq0.
\tag{RH-GROWTH}
\]
This is an RH-STRENGTH obligation, still unproved. Finite Fourier isomorphism, compactness and complete Tate source identity DO NOT produce it automatically; rational \(\begin{psmallmatrix}1&2\\2&1\end{psmallmatrix}\) passes both local diagonal tests and fails the cross sign. The already source-authenticated Suzuki low 30/high Schur at a=1/2 (parallel PR #107/#109) is the sharpest current concrete target.

**Do not label RH intrinsically Fucked.** The relevant analytic/Weil positivity remains open with an insufficient current construction, not a proved absence of any possible proof or discriminator. A source/observer toolkit can be weak without the mathematical conjecture being impossible.

## 8. Executed finite probes, controls and proof status

Code:
- observational_succ/field_limit_trichotomy.py implements an explicit effective universal binary TM enumerator and bounded diagonal tree membership, exact simple 2-adic symbolic source, noncompact inverse-limit no-go, finite noninteger CRT ghost, observational hidden-tag invariance, and the relative status ledger.
- observational_succ/field_limit_compactness.py implements exact finite nested Cantor source-fiber controls and a bounded prefix recovery algorithm for unique/tree-rival/Kleene models.
- tests/test_field_limit_trichotomy.py and tests/test_field_limit_compactness.py preserve exact typed positive/negative controls. The *infinite* existence/noncomputability/compactness theorems are proved in this manuscript, not extrapolated from finite tests.
- Original Tate/Weil modules, SHA-pinned source source_weil_hierarchy.py and any other agents' draft branches have NOT been modified.
- Wrongly claiming a finite stage proves the whole tree, a noncomputable path is effectively produced, a finite CRT prefix excludes all original integers, or one scalar Q score captures all these facts is a forbidden inference.

**Claim ledger:**
- SIMPLE law: PROVED LOCAL effective stage, classical source compatibility.
- IDEALHARD Kleene tree: CLASSICAL/PROVED infinite existence and NO computable path; finite bounded emulator calibrated.
- UNIQUE TREE path computability: CLASSICAL/PROVED under explicit effective finite binary branching/unique-path promise; no uniform time bound.
- FUCKED noncompact empty limit: CLASSICAL/PROVED.
- FUCKED phantom source-map: CLASSICAL/PROVED exact quantifier boundary.
- FUCKED nonfaithful toolkit: PROVED exact finite-carrier invariance for all action words.
- COMPACT-LIFT: CLASSICAL conditional theorem; arbitrary physical source compactness remains a premise, not tested.
- TATE GLOBAL POISSON and authentic RH source cross-growth: **UNVERIFIED**, RH PROVED: NO.

## 9. Next verdict-changing probe

**Source-indexed effective compactification for actual Tate tests.** Construct and prove which of the source-relevant Tate diagrams are effectively compact (profinite integral characters), which require two-axis noncompact support and independent real Schwartz topology, and which form limits retain a proved uniform test-space continuity modulus. Then use the canonical same-source Fourier/CRT characters to construct genuine pairings between all 30 Suzuki low modes and genuinely prime-active test domains. An independently justified Schur/feature inequality on their union (not individual positive domains) is the missing new sign mechanism.

**Do not confuse a finite truth/proof at stage n with a finite certificate of all stages. Do not infer that RH is unprovable or mathematically indeterminate.**

References:
- Andrew Marks, *Computability Theory*, §23, Kleene trees / DNC classes and Exercise 23.6 on unique computable-tree paths: https://math.berkeley.edu/~marks/notes/computability_notes_v1.pdf
- Classical Weak König Lemma, compact Hausdorff finite-intersection property, Stone/profinite duality, finite-source CRT and Tate Fourier.
- Existing SUCC context: field_relative_closure.py, field_limit_countermodels.py, prime_clock_yoneda.py, operational_yoneda_descent.py, tate_observer_completion.py, tate_adele_quotient_descent.py, observer_global_sign_gate.py, and APOLLO/ONE OBJECT/TATE×SUZUKI draft dossiers (read only).

**RH remains open.**


## 10. One finite observation may contain noncomputable INFINITE information (effective input gate)

“Finite-place stage” and “finite effectively available information” must never be identified merely because one model has a finite number of typed input slots. A single EXACT real number may encode infinitely many uncomputable digits.

Enumerate all partial computable binary-output programs \(\varphi_e\) as in the explicit TM code above and define
\[
\boxed{
\Omega_4=\sum_{e=0}^\infty4^{-(e+1)}
       {\bf 1}_{\{\varphi_e(e)\ \mathrm{halts}\}}.
}\tag{F-REAL-ORACLE}
\]
The base-four expansion uses only digits 0 and 1. Once the first e digits are determined, the unexamined tail after the e-th digit is at most one-third of the next digit's weight. Thus a computable real approximation with sufficiently small error would decide each halting digit successively, deciding the halting set—a contradiction. Therefore \(\Omega_4\) is a noncomputable real. The construction is classical and distinct from Chaitin's specific halting probability (we make NO prefix-free probability claim).

The code evaluates ONLY the finite bounded halting predicates e<d, up to a declared step budget B. The rational lower is the sum of already observed terminating program weights. The rational upper is this lower PLUS weights of unresolved first-d programs and the exact infinite tail \(4^{-d}/3\). Increasing the bounded execution time can shrink the interval, but no finite B is promoted to an oracle deciding arbitrary nonhalting.

**Consequence:** one “finite observer” endowed with an EXACT \(\Omega_4\) register would possess unbounded halting information as an ASSUMED oracle. This is not finite executable construction under ordinary Turing operations. Applied to Tate, the Archimedean Schwartz factor may have noncomputable arbitrary real parameters unless a computable dense effective presentation, approximation/evaluation oracle policy and error modulus are explicitly declared. Rational p-adic finite test charts do not license arbitrary exact real inputs silently.

**Claim F-REAL-ORACLE: PROVED classical noncomputability plus exact rational bounded simulation enclosures.** No proof of global Tate, RH, or a physical model is asserted.

## 11. Operator-compactness theorem: the true finite-to-global Hilbert contraction gate

This is the strongest direct connection to APOLLO's source-positive Hilbert/Krein decomposition.

Fix two **COMMON source Hilbert spaces** \(H_+,H_-\) and an indexed family \(v_i\in H_+\), \(w_i\in H_-\). For each finite F of indices let
\[
C_F=\{T\in B(H_+,H_-):\|T\|\le1,\
Tv_i=w_i\ \forall i\in F\}.
\]
Then
\[
\boxed{\quad
\exists T:\|T\|\le1,\ Tv_i=w_i\ \forall i
\quad\Longleftrightarrow\quad
C_F\ne\varnothing\ \text{for EVERY finite }F.
\quad}\tag{HILBERT-COMPACT}
\]

**Proof by operator compactness:** the norm-unit ball of \(B(H_+,H_-)\) is compact in the weak operator topology (WOT), via Banach–Alaoglu/Tychonoff (bounded operator unit balls as products of weakly compact Hilbert balls, with linearity/norm bounds preserved by weak limits). Each equality \(Tv_i=w_i\) is WOT-closed, because it is equivalent to \(\langle Tv_i,z\rangle=\langle w_i,z\rangle\) for all \(z\in H_-\). The sets C_F are closed and have the finite-intersection property: the intersection of finitely many constraints is their union finite constraint. Compactness yields a T in their total intersection.

**Constructive algebraic alternative:** suppose for every finite vector family the norm inequality
\[
\left\|\sum_i c_i w_i\right\|^2
\le\left\|\sum_i c_i v_i\right\|^2
\]
holds. The map \(\sum_i c_i v_i\mapsto\sum_i c_i w_i\) is well-defined and contractive on the algebraic source span. It extends uniquely to the closure. Set T=0 on its orthogonal complement. This gives the canonical minimal extension. It is a mathematical existence construction, not necessarily an algorithm that outputs all infinite feature coordinates.

**Exact finite executable prototype:** for rational vectors \(v_i\in\mathbb Q^d\), \(w_i\in\mathbb Q^e\), the source Gram condition is \(G_+-G_-\succeq0\). If true, select an independent source v-basis B, build the rational matrix \(T=W_B(B^TB)^{-1}B^T\), verify every \(Tv_i=w_i\) and \(I-T^TT\succeq0\) by exact Fraction principal minors. If false, provide a true negative principal minor. Implemented in field_contractivity_compactness.py with separate synthetic controls, NOT yet original Suzuki feature entries.

### Why a UNIFORM boundedness law is essential

Let \(H_+=H_-=\ell^2(\mathbb N)\), with source constraints \(Te_n=(n+1)e_n\). Every finite prefix has a bounded solution with norm at most its largest n+1, but no single bounded T can satisfy ALL constraints, since \(\|T\|\ge n+1\) for all n. This is a rigorously empty bounded-global target with individually feasible finite source stages. It violates the UNIFORM contraction premise, so it is no contradiction to HILBERT-COMPACT. The exact finite algorithm records the growing required operator norm.

### Source identification: where APOLLO and RH actually sit

APOLLO #110 defines original arithmetic \(K_g=K_+-K_-\), with independent positive feature families \(\Phi_\pm(x)\). For a fixed interval a, choose the actual H_+^(a),H_-^(a). A fixed-source contraction satisfying \(T\Phi_+(x)=\Phi_-(x)\) for ALL points exists iff the ORIGINAL signed Gram K_g is PSD on every finite set. This is RH-strength when imposed at every interval. HILBERT-COMPACT proves that all finite constraints *would* glue, but **we have NOT proved all those constraints are feasible**.

Across different widths a, the two separate source Hilbert presentations can change by **paired neutral prime-feature births** (APOLLO K5). They are not automatically one fixed common Hilbert pair, so operator compactness cannot be used across a without coherent source-labeled embeddings and uniformly bounded transported maps.

**The missing ingredient is now typed exactly:** a SOURCE-DERIVED proof of uniform finite Gram dominance/cross-block Schur positivity for the TRUE Weil/Krein features, rather than another finite observation or finite Fourier equivalence. This cannot be supplied by merely invoking Banach–Alaoglu. In particular, arbitrary positive+negative Hilbert factorization without the contraction remains insufficient.

**Claims:** operator compactness CLASSICAL/PROVED; finite rational contraction constructor PROVED LOCAL; unbounded finite-prefix obstruction PROVED; actual Suzuki all-finite contractivity and RH **UNVERIFIED**.

Mathematical background on WOT unit-ball compactness: https://www.math.uni-leipzig.de/~wirth/notes_ot_25.pdf and https://www.math.ucdavis.edu/~hunter/book/ch8.pdf; no new functional-analysis priority claim.
