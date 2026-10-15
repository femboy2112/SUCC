# WILD EMBEDDING SUCC — intrinsic sphere, perfect exterior, nonuniform witness debt, and boundary model interaction

**2026-10-14 research offshoot.** Branch: \`research/wild-embedding-boundary-descent-2026-10-14\`. **Exact pinned parent:** \`femboy2112/SUCC@dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc\` (draft PR #85, authentic completed-Weil source hierarchy; ancestry #76/#73/#71). Read-only independent context: prime-sphere #68, recursive Meta-SUCC #80, analytic meta-contour #81, and real arithmetic prime/Gamma boundary PR #86 at \`205ffd020dd2a320eeac70a91a2a2700c969c048\`. **Nothing merged into main. RH PROVED: NO.**

**Author's original proposal:** Perhaps a globally spherical mathematical carrier has a wildly embedded, infinitely intertwined realization, whose local finite observations make ordinary global source interaction and positivity extremely hard to certify. The strongest repaired version distinguishes the intrinsic source, the embedding into an ambient carrier, the topology of its complement, finite observational probe languages, and the source-preserving operators on an analytic test domain. The same abstract sphere may admit inequivalent ambient realizations. This is a bona fide classical topology phenomenon. **No identification between arithmetic adeles/prime-sphere/Suzuki's \(G_a\) and a literal wild embedding is supplied.**

## A. Primary sources and prior art

- **J. W. Alexander (1924)**, *An Example of a Simply Connected Surface Bounding a Region which is not Simply Connected*, PNAS **10** (1), 8–10, DOI 10.1073/pnas.10.1.8. Original openly available text: https://www.jstor.org/stable/84202 and https://pmc.ncbi.nlm.nih.gov/articles/PMC1085500/ . Alexander explicitly constructs finite increasingly hooked surfaces approaching a genus-zero simple closed surface whose exterior loop fails to contract; exterior group requires infinitely many generators.
- **Alexander duality** (classical; convenient formal topological-manifold statement): for every compact \(S^2\) embedding into \(S^3\), \(\widetilde H_j(S^3\setminus\Sigma;\mathbb Z)\cong\widetilde H^{2-j}(S^2;\mathbb Z)\). See Alexander-duality lecture slides https://www.dtubbenhauer.com/slides/algebraic-topology/26-alexanderduality.pdf and standard algebraic topology references.
- **Classical generalized Schoenflies** for tame/locally flat finite sphere approximants, and Arzelà–Ascoli compactness of equicontinuous maps \(D^2\to S^3\); the finite-to-limit regularity theorem below is a direct consequence.
- **Classical Magnus expansion/free-group lower-central filtration**, Alexander duality/Hurewicz \(H_1\simeq\pi_1^{ab}\), solvable/perfect group theory, and Fourier positivity of genuine Ornstein–Uhlenbeck kernels. Our exact implementations are new-to-SUCC educational/calibration objects, not independently established scholarly priority.
- **SUCC sibling PR #86** builds an *authentic* full-line prime dilation/Gamma commutation and a nonzero compressed first-prime boundary commutator, with its own analytical source and tests. We compare the algebra, but DO NOT import its proof or treat the finite toy below as authentic completed Weil.

## 1. Intrinsic/extrinsic probe nonconservativity — WES-01 (CLASSICAL; PROVED AS A SCOPE-SENSITIVE COROLLARY)

An embedded sphere is a pair \((S^3,e(S^2))\), with \(e:S^2\hookrightarrow S^3\) a topological embedding. Intrinsic chart functors that forget e map *every* such surface to \(S^2\). Yet two standard embeddings have nonisomorphic exterior fundamental groups: the tame round sphere has trivial \(\pi_1(U)\), while Alexander's wild embedding has \(\pi_1(U)\neq1\) in the non-simply-connected exterior component.

Thus no invariant that factors **solely** through the intrinsic homeomorphism type of \(S^2\) can recover exterior \(\pi_1\) for all embeddings. Calling the actual embedding a "projection" is too weak: the mathematically relevant extra datum is the *ambient embedding and complementary inclusion maps*, not the surface's intrinsic cells alone.

A source-faithful exact abstract-sphere check uses the double cone on the four-cycle: V=6, E=12, F=8, \(\chi=2\), chain boundary ranks \(\operatorname{rk}\partial_1=5,\operatorname{rk}\partial_2=7\), Betti \((1,0,1)\) over \(\mathbb Q\). It computes **NO** 3D realization or exterior fundamental group. The fact this complex is abstractly \(S^2\) cannot distinguish its potential ambient embeddings. The abstract result overlaps SUCC PRIME-SPHERE #68; no new sphere topology is claimed.

## 2. The unexpectedly severe abelian-observer no-go — WES-02 (CLASSICAL + EXPLICIT DERIVATION)

Take **any** embedded topological \(\Sigma\cong S^2\subset S^3\), including the horned sphere. Since \(S^2\) is compact and locally contractible, Alexander duality applies *irrespective of ambient wildness*:

\[
 \widetilde H_1(S^3\setminus\Sigma;\mathbb Z)
 \simeq\widetilde H^1(\Sigma;\mathbb Z)=0.
\tag{W1}
\]

The complement has exactly two path-connected components \(U_{\rm in},U_{\rm out}\) by the \(j=0\) duality calculation, and
\(H_1(U_{\rm in};\mathbb Z)=H_1(U_{\rm out};\mathbb Z)=0\) because \(H_1\) of their disjoint union is their direct sum. The degree-one Hurewicz theorem gives
\[
 \boxed{\pi_1(U)^{ab}\cong H_1(U;\mathbb Z)=0.}\tag{W2}
\]
In particular the actual Alexander exterior group is **nontrivial perfect**, not merely nonabelian: \(\pi_1(U)=[\pi_1(U),\pi_1(U)]\neq1\) by the original 1924 theorem.

**Strong consequence.** For any group homomorphism \(\rho:\pi_1(U)\to H\) with **solvable** target H, its image is a perfect solvable group. The only perfect solvable group is trivial (its derived series would simultaneously stabilize and terminate). Therefore
\[
 \boxed{\rho=1\quad\text{for every solvable target }H.}\tag{W3}
\]
This includes all U(1), finite cyclic, \(\mathbb Z^d\), finite nilpotent groups and S3 representations *of the actual exterior pi1*. Even infinitely many probes of that type cannot reveal its nontriviality. A5 is a small nontrivial **perfect** group, computed exactly below, but **no homomorphism from the actual horned exterior onto A5 is known or claimed here**. A perfect group need not have useful finite quotients; do not infer their existence from (W2).

**RH firewall:** SUCC's prime phase, Fourier and character charts are *not* automatically representations of this exterior group. The no-go applies only to a proposed topological exterior-holonomy interface factoring through such a group homomorphism, **not** to the analytic power of Fourier methods in RH. This is a \(\sigma\)-source-map/observer-language obstruction, not a proof of a physical bound or Weil positivity.

## 3. A bounded nonabelian-resolution hierarchy — WES-03 (PROVED LOCAL; FINITE FREE-GROUP TOY)

Let \(F(a,b)\) be the **free group**, which is *not* the horned exterior group. Put \(w_0=b\) and recursively \(w_{k+1}=[a,w_k]=a w_k a^{-1}w_k^{-1}\). Give the finite observer a truncated noncommutative Magnus report
\[
 M(a)=1+X,\qquad M(b)=1+Y,\qquad
 M(a^{-1})=\sum_{r=0}^{D}(-X)^r \ \ (\bmod\deg>D),
\]
similarly for \(b^{-1}\), in \(\mathbb Z\langle X,Y\rangle\).

**Theorem.** At every \(k\ge1\), the finite observer reading all monomials of degree at most k sees exactly the identity even though \(w_k\neq1\). The first distinguishing degree is **k+1**:
\[
 M(w_k)=1+\operatorname{ad}_X^k(Y)
              +O(\deg\ge k+2),\quad
 \operatorname{ad}_X^k(Y)=
 \sum_{j=0}^k(-1)^j\binom{k}{j}X^{k-j}YX^j.
\tag{W4}
\]
The monomial \(X^kY\) has coefficient \(+1\), establishing nontriviality without assuming faithfulness of a finite truncation. Proof by induction from the commutator product, since each commutation increases the least nonconstant homogeneous degree by one. All k>=1 have trivial abelianization, and increasing a bounded observer's sophistication eventually separates each fixed \(w_k\). **It does not require infinitely many probes for a single finite word; it demonstrates arbitrarily delayed finite distinguishability.**

\`wild_embedding_probes.py\` implements free reduction, noncommutative truncated Magnus integer polynomial arithmetic and exact horizon witnesses to k=6, with source/typing guards. At k=1,…,5 the reduced lengths are exactly 4,10,20,38,72, while first visibility occurs only at degrees 2,3,4,5,6 respectively. No actual horned-sphere complement embedding/representation is claimed: \(F_2^{ab}=\mathbb Z^2\), whereas the true horned exterior is perfect. Confusing the toy with an authentic exterior \(\pi_1\) is a deliberate refuted shortcut.

Finite group calibration: S3 has 6 elements and its commutators range over only 3 elements; A5 has 60 elements and every one is a commutator (verified by enumerating its even permutations and all 3600 pairwise commutators). This proves A5 is a possible finite *perfect target*, NOT that the actual wild exterior has an A5 quotient.

## 4. The **wild finite-to-global nonuniformity theorem** — WES-04 (PROVED MATHEMATICALLY, CLASSICAL COMPACTNESS CONSEQUENCE)

This is the closest rigorous analogue of the proposed "FuckedSpace geometry" and is more consequential than merely depicting horns.

Let \(\Sigma_n\subset S^3\) be tame embedded spheres converging to a wild embedded \(\Sigma\) in the Hausdorff metric. Fix a continuous loop \(\gamma:S^1\to U\subset S^3\setminus\Sigma\) that is not nullhomotopic in the limiting exterior U, and suppose its image is disjoint from every \(\Sigma_n\) for large n (automatic by compactness and Hausdorff convergence). Each finite tame complement component is an open ball by the locally-flat generalized Schoenflies theorem, hence \(\gamma\) has a contraction \(H_n:D^2\to S^3\setminus\Sigma_n\) for all sufficiently large n.

**THEOREM — no uniformly regular, uniformly separated contraction family.** For every pair of constants \(L<\infty,\ \delta>0\), there is an N such that for **every** n>=N and **every** filling \(H_n\) of \(\gamma\) in the n-th complement,
\[
 \boxed{\quad
 \operatorname{Lip}(H_n)>L
 \quad\text{or}\quad
 \operatorname{dist}(H_n(D^2),\Sigma_n)<\delta.
 \quad}\tag{W5}
\]
If a candidate filling is only continuous, interpret its Lipschitz constant as infinity unless a finite Lipschitz bound is separately proved.

**Proof.** Suppose infinitely many n admit fillings with \(\operatorname{Lip}H_n\le L\) and clearance \(\ge\delta\). Equip compact \(S^3\) with its round metric and compact \(D^2\) with Euclidean metric. The maps are uniformly equicontinuous and take values in a compact metric space. Arzelà–Ascoli extracts a uniformly convergent subsequence \(H_{n_j}\to H:D^2\to S^3\). As \(d_H(\Sigma_{n_j},\Sigma)\to0\), for all sufficiently large j the image of \(H_{n_j}\) lies at least \(\delta/2\) from \(\Sigma\). The uniform limit H likewise avoids \(\Sigma\). All boundary values remain the same \(\gamma\), so H fills \(\gamma\) in \(S^3\setminus\Sigma\). Since D² is connected and its boundary lies in U, H lies in the exterior U, contradiction. QED.

**Logical import:** every finite-stage "YES, the loop contracts" can coexist with a final "NO." The missing assumption is **uniform witness compactness/clearance**: \(\forall n\,\exists H_n\) cannot be promoted into a compatible convergent witness. This is a sharp no-ghost causal-gluing counterexample and a legitimate *geometric resource dichotomy*. It gives **no effective numerical N(L,\delta)** for Alexander's original construction, no actual physical energy/entropy law, and no source-specific undecidability theorem. Claims that the original source's horns force a black hole, or that RH has identical homotopy data, are unsupported.

**Arzelà–Ascoli positive control:** if the finite witnesses DID have common Lipschitz and clearance bounds, the preceding proof would construct a limit nullhomotopy—so under its assumptions the negative conclusion would be contradicted. **Negative controls:** omit Hausdorff convergence, permit the loop to change with n, allow clearance to vanish, or allow unbounded Lipschitz complexity; the proof no longer applies.

## 5. Why clipping a lawful carrier can manufacture interactions — WES-05/06 (PROVED LOCAL, classical compression identity)

Let \(P\) project onto an observer's subspace. A global operator A is observed as \(\Phi_P(A)=PAP|_{PH}\). It is generally **not** multiplicative. The exact defect is
\[
 \boxed{\Delta_P(A,B)=\Phi_P(AB)-\Phi_P(A)\Phi_P(B)
       =PA(I-P)BP|_{PH}.}\tag{W6}
\]
This obeys \(\|\Delta_P(A,B)\|\le\|PA(I-P)\|\|(I-P)BP\|\). If A and B commute **globally**, their compressed commutator can be nonzero:
\[
 \boxed{[\Phi_P(A),\Phi_P(B)]
       =\Delta_P(B,A)-\Delta_P(A,B).}\tag{W7}
\]
This is not a nonabelian bulk holonomy; the source of noncommutation is **boundary leakage** through unobserved states.

For three global operators, associativity forces the exact coherence relation
\[
 \Phi(A)\Delta(B,C)-\Delta(AB,C)
       +\Delta(A,BC)-\Delta(A,B)\Phi(C)=0.
\tag{W8}
\]
This is an **associativity defect identity**, NOT an assumed Hochschild cohomology class (the nonhomomorphic \(\Phi\) does not automatically give a bimodule action). Every occurrence of the source projection P and its basis must be retained.

**Independent EXACT rational finite source.** On \(\ell^2(\mathbb Z/5\mathbb Z)\), take the true finite cyclic permutation T and *declared toy bath* \(C=3I+T+T^{-1}=I+(I+T)(I+T)^*\succeq I\). On the full five-state carrier \(TC=CT\). Let P be the first three sites. Direct rational arithmetic proves
\[
 \boxed{
 [PTP,PCP]_{P H}=
 \begin{pmatrix}-1&0&0\\0&0&0\\0&0&1\end{pmatrix}\ne0 .
 }\tag{W9}
\]
It satisfies (W6)–(W8) exactly; the full observer P=I or single-coordinate observer gives zero. Positive C and a unitary T have generated a noncommuting *observed pair*, yet that has **no implication for completed Weil positivity**. \`wild_boundary_compression.py\` implements the finite algebra, Gram/SOS positive C, its leakage, third-level coherence, basis-gauge covariance, and hostility to floats/stale source metadata.

**AUTHENTIC SUCC CONNECTION (read-only sibling #86):** the original full-line prime logarithmic translations \(T_{\log p}\) commute with the single real Gamma convolution, but the compressed source window \(P_a\) generates a nontrivial \([P_a T_{\log2}P_a,P_a C_\Gamma P_a]\), which sibling PR #86 reports with a genuine continuum lower bound. Our toy isolates the algebraic cause and tests coherence; it neither independently rechecks PR #86's \(>3/22\) numerical lower bound nor changes the authentic source.

## 6. A positivity shortcut that wild embeddings cannot fix — WES-07 (CLASSICAL UNITARY INVARIANCE)

If a lawful source and test-domain transport is **unitary**, \(G\mapsto UGU^*\), then
\[
 \boxed{d_-(UGU^*)=d_-(G),\qquad
 \langle (UGU^*)(Uu),Uu\rangle=\langle Gu,u\rangle .}\tag{W10}
\]
Thus a mere *re-embedding/relabeling of Hilbert coordinates* does not turn an indefinite Weil form into a positive one. An exact rational 3–4–5 orthogonal two-state witness transforms a \(-1\) Rayleigh direction to a new basis, retaining its exact \(-1\) value. No wild-to-Weil Hilbert intertwiner is given: topological ambient homeomorphisms need not preserve the analytic source, measure, Gamma, time parameter or compact test-function domain.

**Crucial boundary:** Neither perfect exterior \(\pi_1\) nor nontrivial compressed commutators supply \(G_a\succeq0\). A source-identified operator map with the original prime powers, half density, real Gamma/contact, poles, proper \(H_0^1\) and full test quantifiers remains necessary.

## 7. Claim classification and next falsifiers

| ID | Scoped result | Claim status |
|---|---|---|
| WES-01 | Intrinsic S² cannot determine ambient complement \(\pi_1\) for every embedding | CLASSICAL (Alexander counterexample); exact six-vertex sphere core PROVED LOCAL |
| WES-02 | Horned exterior nontrivial perfect; every solvable-target representation trivial | CLASSICAL Alexander + Alexander duality + Hurewicz; explicit deduction PROVED |
| WES-03 | Deep free-group commutators escape every fixed finite Magnus-degree observer | PROVED LOCAL exact integer algebra; **toy not actual horned \(\pi_1\)** |
| WES-04 | Stagewise nullhomotopies cannot have both uniform Lipschitz and clearance bounds | PROVED as a classical Arzelà–Ascoli consequence; no effective growth bound |
| WES-05 | \(\Delta_P(A,B)=PA(1-P)BP\) and three-model coherence | PROVED LOCAL exact rational linear algebra |
| WES-06 | Commuting bulk shifts and positive bath may become noncommuting after observer compression | PROVED LOCAL finite toy; genuine arithmetic PR #86 is read-only |
| WES-07 | Lawful unitary transport preserves negative spectral depth/sign | CLASSICAL; exact rational mutation test PROVED LOCAL |
| WES-08 | Actual wild 3D embedding construction/finite geometry source | UNVERIFIED / NOT IMPLEMENTED |
| WES-09 | A source-preserving \(\pi_1\)-to-authentic-Weil operator functor giving positivity | UNVERIFIED (RH-specific missing bridge) |

**Conspicuous falsifiers:** claiming the free-group/S3 toy IS Alexander's perfect exterior contradicts (W2) and the solvable no-go; using only S² homology to infer complement simple connectivity is explicitly refuted; declaring \([PAP,PBP]\ne0\Rightarrow Q_W\ge0\) fails on finite signed-G toy controls; treating arbitrary homeomorphism as a unitary Hilbert-space intertwiner is a type error; stagewise finite homotopy success cannot justify a uniform limiting homotopy without clearance/modulus assumptions.

**Next research instruments:** (i) build a *real* finite-stage PL Alexander model with measured ambient embeddings, protected exterior loops, and quantitative clearance/Lipschitz witness budgets (not a projected sphere image); (ii) develop original-source \(\pi_1\) and pro-\(\pi_1\) inclusion maps for **complement neighborhoods**, NOT the intrinsic sphere alone; (iii) use genuine Suzuki \(P_a\), full-line prime shifts and real Gamma convolution to prove a source-identified boundary defect inequality against the **signed** prime/pole/half-density contributions, preserving domain and all errors; (iv) hostile mutations: selfadjoint sign preserved by unitary, no source 6, wrong parity/conductor, no invented cross-place phase. A nontrivial commutator norm by itself is neither a positivity theorem nor a physical wild-embedding witness.

**Verification:** \`observational_succ/wild_embedding_probes.py\` and \`wild_boundary_compression.py\`; two focused exact suites, deterministic JSON receipt and versioned workflow on Python 3.10/3.13, inherited source provenance. No Lean kernel result, independently validated wild finite meshes, full-repo CI or academic priority claimed until specifically checked.


## 8. A robust **conditional** boundary detector for the genuine arithmetic next step — WES-10 (PROVED LOCAL with declared error)

For a unitary global T, any orthogonal projection P and a bounded self-adjoint source bath C, suppose a finite, **independently certified** C₀ satisfies \(\|C-C_0\|\le\epsilon\). Then
\[
 \left\|[PTP,PCP]-[PTP,PC_0P]\right\|
 \le 2\,\|PTP\|\,\|P(C-C_0)P\|\le2\epsilon.
\]
Thus if a finite stage constructs a unit test vector u and proves
\(\|[PTP,PC_0P]u\|\ge m>2\epsilon\), the authentic compressed commutator is nonzero with operator-norm lower bound \(\ge m-2\epsilon\). This is a **model-of-model quantitative error transport**, valid independently of topology. It does NOT infer any signed quadratic form is PSD.

In the exact five-cycle toy, m=1 is certified by the first coordinate basis vector and the compressed commutator \(\mathrm{diag}(-1,0,1)\). With a **declared** error bound \(\epsilon=1/10\), the rigorous conditional lower bound is \(4/5\). An independent exact rational C perturbation by the positive diagonal \(+\frac1{10}|e_0\rangle\langle e_0|\) satisfies the comparison and preserves a commutator of norm at least \(4/5\). \`conditional_commutator_stability\` preserves a conspicuous \`genuine_arithmetic_gamma_error_verified=False\` flag: this is NOT an actual certified approximation of the real Gamma convolution.

The genuine arithmetic route can use this only after (i) producing source-correct \(P_a,T_{\log 2},C_\Gamma\), including their Hilbert spaces, (ii) independently bounding the precise \(C_\Gamma-C_{\Gamma,J}\) operator error in the same norm, and (iii) proving a test witness m on that precise source. Sibling PR #86 investigates this authentic route already; its stated continuum lower bound is **not** replicated or independently proved here. Even a nonzero authentic commutator cannot by itself dominate the full negative prime/pole/contact/half-density terms in Suzuki's completed Weil form.


## 9. HOSTILE ABLATION: wild complement topology cannot become Weil-sign discontinuity — WES-11 (PROVED CLASSICAL NO-GO)

The user's analogy is strongest in **observer representational access and witness compactness**, but it has a sharp mathematical limit that must be preserved.

The map \(\Sigma\mapsto\pi_1(S^3\setminus\Sigma)\) is *not* invariantly continuous under Hausdorff approximation by tame spheres: Alexander's finite approximants can have simply connected exteriors while the wild limit has a nontrivial exterior group. However, the **positive operator cone** is closed even in the **strong operator topology** on bounded self-adjoint operators. If \(A_n\succeq0\) and \(A_nu\to Au\) for every fixed u, then
\[
 \langle Au,u\rangle=\lim_n\langle A_nu,u\rangle\ge0
 \qquad(\forall u).
\]
Under the **stronger operator-norm control** already proved for genuine Suzuki \(G_{a,J,N}\) in ancestor PR #85, negative depth is even quantitatively Lipschitz:
\[
 \boxed{|d_-(A_n)-d_-(A)|\le\|A_n-A\|.}\tag{W11}
\]
Therefore a **true negative** Weil direction cannot first appear only *after* an infinite norm-convergent chain of wholly positive exact operators. If \(d_-(G_a)=d>0\), then for every sufficiently large certified stage with \(\|G_a-G_{a,J,N}\|<d/2\), its negative depth is \(>d/2\). This is an existential finite witness theorem, not an *effective finite cutoff*: d is unknown, and stage resource requirements may be astronomically large.

The exact rational toy \(G_\infty=\operatorname{diag}(1,-1)\), \(G_n=\operatorname{diag}(1,-1+1/n)\) has \(\|G_n-G_\infty\|=1/n\) and \(d_-(G_n)=\max(0,1-1/n)\): at n=1 the observer sees a PSD stage, but by n=2 a negative direction must already be visible. The returned \`wild_limit_sign_pathology_possible=False\` is scope-labeled as **generic operator mathematics**, not an original Weil computation.

**Crucial verdict:** Wild embedding supplies a compelling model for **why finite ambient probe languages may omit source structure or why stagewise homotopy witnesses fail to glue without uniform geometry**. It does **NOT** supply a mathematical mechanism by which *all* exact PSD, norm-convergent arithmetic Weil approximants could develop negative spectrum only at their limit. Any proposal making that analogy is **REFUTED** within the correct operator topology. Remaining source-specific RH difficulty is proving a universal *quantified sign theorem*, not overcoming a discontinuity of the PSD cone. This is an important falsification of the preferred intuitive frame, retained as a result rather than silently repaired.
