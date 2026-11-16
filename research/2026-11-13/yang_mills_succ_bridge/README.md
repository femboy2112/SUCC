# OPERATION SUCC × YANG–MILLS 4D: gauge-complete carrier observers

**Research date:** 2026-11-13. **Parent:** SUCC Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`. **Mode:** additive draft research. **Targets:** reconstruct the released theorem claim accurately; reproduce a finite *mathematical core* with exact, hostile controls; identify source-dependent, non-tautological routes toward a continuum spectral gap.

**Verdict:** **OpenAI's October submission addresses 4D quantum Yang–Mills existence; the full Clay existence-and-mass-gap problem is NOT solved.** The proof group issued an assessment in favor of the October existence result, but its specified mass-gap, uniqueness, and confinement obligations remain open. This SUCC contribution is a finite model plus a research protocol. It does **not** rebuild the external Lean proof or establish any 4D compact-simple-group continuum result.

## A. Claim recovery: what was actually released

### Primary sources, pinned to accessible commits

1. OpenAI's [26 October 2026 announcement](https://openai.com/index/building-scientific-understanding-with-academic-communities/) reports a proof of certain 4D gauge-field and fermion QFT existence constructions, including pure YM as a subproblem, based on Balaban-style constructive methods. The natural-language manuscript for the physics results was initially withheld for academic shepherding.
2. **OpenAI October source:** [`yang-mills-group/OpenAI-YM-20261028` at `3456e5e75cf8d4cd558955a5c7638fba2d68f464`](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464). The principal target is [`YangMills.jointExistence : YangMills.JointExistence`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/ChallengeSpec.lean); [`Solution.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/Solution.lean) projects a much deeper theorem in [`Construction.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/Construction.lean). `Challenge.lean` contains the intentional **reference-only** `sorry`; the solution is separately checked against that reference.
3. **Independent group:** [`yang-mills-group/YM` at `55ba9fc36293b3f4d52c6b1f813169a0be76ee98`](https://github.com/yang-mills-group/YM/tree/55ba9fc36293b3f4d52c6b1f813169a0be76ee98). The 10 November assessment in `docs/assessment-1.pdf` concludes in the group's opinion that a Wightman QFT exists as a four-dimensional Wilson-lattice scaling limit for each compact simple group; *it does not conclude uniqueness of the infinite-volume limit, confinement, or a positive gap*. The [scope guide](https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/checks.md) lists A1–A8 checks, including one selected scalar OS field and the actual limitations of its additional OPE check.
4. [Reproduction contract](https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/rerun.md): Lean 4.32.0, pinned Mathlib/dependencies and comparator (different toolchain), roughly 52 GiB in the documented completed build, and careful axiom and source-input auditing. `python3 scripts/verify.py integrity` followed by `python3 scripts/verify.py all` runs the external check in a proper checkout. **No SUCC script executes or replaces these steps.** The documented review performs a selected axiom/Comparator check and retains its isolation limitations.
5. [Clay's canonical Yang–Mills problem](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) requires **both** a nontrivial quantum theory and **strictly positive physical mass gap**. As of this dossier it remains listed **UNSOLVED**.

### Actual logical targets, not social-media compression

| Property | External October source and group check | SUCC status |
|---|---|---|
| Four-dimensional Wilson lattice origin | Explicit single-source family and action/insertions | **EXTERNAL**; source description reviewed; not imported as local theorem |
| Wightman axioms and selected OS bridge | Formal theorem and review A1–A7; source to reconstruction claimed/assessed | **EXTERNAL**; no local Lean reproduction |
| OPE and leading stress-trace behavior | Submitted bounds; separately reviewed OPE adapter | **EXTERNAL**, assumptions and witness scope pinned |
| Uniqueness of thermodynamic limit | Excluded from submission scope | **OPEN** |
| Confined phase and physical continuum mass gap | Excluded from submission scope | **OPEN** |
| SUCC toy finite gauge observability | This dossier's explicit exact construction | **PAPER DERIVATION / 19 finite tests** |
| New Yang–Mills mass-gap theorem | Nothing proved here | **OPEN** |

The review itself warns that successful Lean compilation establishes the **formal proposition specified**, while independent physics/mathematics interpretation of the definitions remains necessary. The original Lean proof is enormous. We have not read every source file or rerun the external build; never label this a complete independent certification.

## B. Steelman: a physically sourced SUCC gauge-oracle

Treat the lattice field as a finite **carrier** with exact group action. The SUCC observer measures Wilson paths and plaquette fluxes; an oracle checks that the measurements transform correctly and jointly arise from one **source state**. Genuine gauge transformations are **identifications**, whereas loss of a noncontractible Wilson channel is an *instrument defect*, not a gauge identification. A refinement/renormalization arrow must transport the source law and specified gauge-invariant observables, with explicit distortion/scale budgets, before proposing a physical gap.

A candidate categorical diagram is

\[
\mathcal A_\Lambda \longrightarrow \mathcal A_\Lambda/\mathcal G_\Lambda
\xrightarrow{\;\mathrm{Wilson}\;} \mathrm{Obs}_\Lambda,
\quad (\Lambda,a)\longrightarrow(\Lambda',a').
\]

The first arrow quotients actual gauge symmetry. The second must be shown **separating** for the chosen observables on the declared object class. The scale arrow must preserve the selected Wilson measure and pay for limits, reflection positivity, fields, gauge covariance, topology, and physical distance. Neither its visual curvature nor an ordinary commuting square proves a gap. This is a research architecture, not an imported consequence of YangMills.jointExistence.

## C. Mathematical outputs and hostile controls

### YMS-01: exact abelian Wilson quotient (ELEMENTARY PAPER PROOF)

For **every** finite connected graph \(\Gamma=(V,E)\), every modulus \(q\ge2\), and oriented edges, a configuration is \(A\in(\mathbb Z/q)^E\). Gauge maps \(\phi\in(\mathbb Z/q)^V\) act via

\[
A_{u\to v}\mapsto A_{u\to v}+\phi(u)-\phi(v)\pmod q.
\]

Choose a spanning tree and a root. There exists a unique \(\phi\) with \(\phi(root)=0\) making **every tree edge zero**. The remaining \(b=|E|-|V|+1\) chord values are exactly the fundamental Wilson-cycle holonomies. Two link fields lie in the same gauge orbit **if and only if** their complete ordered chord tuples agree. Thus

\[
\boxed{\mathcal A_\Gamma/\mathcal G_\Gamma\cong(\mathbb Z/q)^b},\qquad
|\mathcal A_\Gamma/\mathcal G_\Gamma|=q^b,\quad |\mathrm{orbit}|=q^{|V|-1}.
\]

Proof: fix root potential, integrate signed links along the unique tree path to each vertex; this kills every tree edge. The gauge-fixed chord values are manifestly gauge invariant. Conversely equal tuples yield the same unique representative, so the two sources are gauge related. Constant gauge maps form the sole stabilizer on a connected graph. **This quotient is exact and complete in the finite abelian category, not a theorem for nonabelian compact simple groups.**

We can put a Fourier–Yoneda-type Haar energy on **probability laws on the quotient**, not on individual field states: for \(M=q^b\) classes, sample counts \(c_h\), and \(N=\sum_h c_h\),

\[
\boxed{E_\Gamma(\mu)=M\sum_h(c_h/N)^2-1
=\sum_{\chi\ne1}|\widehat\mu(\chi)|^2\ge0.}
\]

The last equality is finite-character orthogonality (Plancherel). Its zero set consists exactly of the uniform **orbit law**. Changing a representative by gauge transformations leaves this energy unchanged. **Do not confuse a Haar law on the gauge-orbit quotient with the interacting Yang–Mills vacuum**: the latter need not be Haar on its gauge-invariant observables, and spectral mass is an entirely different predicate.

Calibration: the connected 4-vertex, 5-edge, q=3 test has 3^5=243 fields, 3^(5-4+1)=9 gauge orbits, and 27 fields per orbit. All 243 fields and all 3^4 gauge maps are exactly enumerated, as opposed to sampling a few favored charts.

### YMS-02: local curvature cannot identify all global holonomy (CONSTRUCTIVE COUNTERMODEL)

On an **honest four-dimensional periodic** side-\(L\ge2\) \(\mathbb Z/q\) lattice, the links are \(A_\mu(x)\). Define gauge map and oriented plaquette

\[
A'_\mu(x)=A_\mu(x)+\phi(x)-\phi(x+e_\mu),
\quad F_{\mu\nu}(x)=A_\mu(x)+A_\nu(x+e_\mu)
-A_\mu(x+e_\nu)-A_\nu(x)\pmod q.
\]

Every plaquette is gauge invariant. The discrete Bianchi identity \(dF=d^2 A=0\) holds, with the full six-face alternating sum checked for every test cube.

Now compare \(A=0\) to the **flat but globally twisted connection**

\[
A_0(x)=\mathbf 1_{x_0=L-1},\qquad A_j(x)=0\quad(j=1,2,3).
\]

Both have **every** plaquette equal to zero and satisfy every local Bianchi check. Yet the noncontractible Wilson loop in direction zero is 0 for the vacuum and 1 for the twisted connection. They are *not gauge equivalent*. This is a topological obstruction: in this abelian torus model, local flatness does not remove classes in \(H^1(T^4;\mathbb Z/q)\). An oracle consisting only of local field-strength observations would incorrectly merge distinct gauge orbits. **This is exactly the gauge redundancy versus incomplete-observer distinction SUCC needs.**

The implementation tests 16 sites, 64 oriented links, 96 plaquettes on side 2 for q=2,3,5; random gauge transformations, global Wilson loops and all 64 three-face Bianchi cells are independently recomputed. No claim is made about nonabelian principal bundles, continuum manifolds, or quantum confinement.

### YMS-03: a PSD/reflection-like kernel can lose its continuum spectral gap (COUNTERMODEL)

For each rational physical lattice spacing \(0<a<1\), define a strictly positive finite transfer kernel

\[
K_a=\begin{pmatrix}1&\epsilon_a\\\epsilon_a&1\end{pmatrix},
\quad \lambda_\pm=1\pm\epsilon_a,
\quad r_a=\frac{\lambda_-}{\lambda_+}
=\frac{1-\epsilon_a}{1+\epsilon_a}.
\]

The matrix is positive definite for \(0<\epsilon_a<1\); the scalar kernel has a positive discrete spectrum and a finite-lattice spectral splitting. At physical distance \(t=na\), the two-state physical inverse correlation length is

\[
 m(a)=-\frac{\log r_a}{a}.
\]

Taking \(\epsilon_a=a^2\) yields an exact all-\(a\) inequality

\[
\boxed{0<m(a)=\frac1a\log\frac{1+a^2}{1-a^2}
\le \frac{2a}{1-a^4}\longrightarrow0.}
\]

The inequality follows from \(\operatorname{artanh}(x)=\int_0^x(1-t^2)^{-1}dt\le x/(1-x^2)\), with \(x=a^2\). Therefore **strictly positive finite transfer eigenvalues and positive finite mass at every cutoff do not imply a strictly positive physical continuum mass**. This is NOT an Osterwalder–Schrader result: it is the precise finite kernel warning against substituting positivity for a uniform physical gap.

For a contrasting family \(\epsilon_a=a/4\), the exact lower bound is

\[
 m(a)\ge\frac{1-r_a}{a}=\frac{1}{2(1+a/4)}\ge\frac25.
\]

For every fixed observed cutoff horizon \(K\), form two valid families on \(a_n=1/n\): both use \(\epsilon_{a_n}=a_n^2\) for all \(n\le K\); after \(K\), the first stays quadratic and loses the gap, while the second switches to linear and keeps a positive lower bound. They share **every** finite observation in that declared cutoff window. Only an authenticated **all-scale** assumption, an actually proved uniform estimate, or a stronger source law can discriminate. The QFT problem requires analogous estimates on the true reconstructed gauge-invariant Hilbert space, with the correct physical scale; no fixed 2×2 matrix supplies them.

### YMS-04: complete nonabelian finite-graph quotient; individual Wilson traces are incomplete (PAPER THEOREM + COUNTERMODEL)

The **spanning-tree quotient generalizes to every group** \(G\), including compact simple groups at the *finite graph kinematics* level. Gauge fields are assignments \(U_e\in G\); site maps act as \(U_{u\to v}\mapsto g(u)U_e g(v)^{-1}\). Fix a root and multiply oriented tree links along each unique root path. This makes every tree edge the identity. The remaining \(b=|E|-|V|+1\) chord holonomies are determined up to **one shared residual conjugation** of all chords. Conversely, simultaneous conjugacy of those chord tuples is sufficient for full gauge equivalence. Thus, as a quotient set (and in the standard compact-group topology for finite graphs),

\[
\boxed{G^E/G^V\cong G^b/G_{\mathrm{Ad}},}
\]

where the right action is **diagonal simultaneous conjugation**, not separate conjugation of each component. For a finite example, take a two-vertex, three-parallel-link graph and \(G=S_3\). There are \(6^3=216\) link configurations and, by Burnside's lemma, \((6^2+3\cdot2^2+2\cdot3^2)/6=11\) simultaneous-conjugacy classes of two chord holonomies. The isolated tests exhaustively enumerate all 216 configurations under all \(6^2=36\) site-gauge maps and recover exactly 11 orbits. This establishes a concrete nonabelian extension of SUCC's finite observer contract, **not** a construction of a 4D interacting quantum theory.

The failure of separate trace observables now has an explicit example.

For the finite nonabelian group \(S_3\), take two transpositions \(a\ne b\). The loop pairs \((a,a)\) and \((a,b)\) have the **same individual permutation-representation traces** \((1,1)\), yet their mixed Wilson-word traces differ:

\[
\operatorname{tr}(aa)=3,\qquad\operatorname{tr}(ab)=0.
\]

Consequently independent loop-trace marginals do not distinguish every simultaneous-conjugacy class. Mixed words retain relational source data. This is a finite counterexample to an over-strong observer-completeness claim; \(S_3\) is NOT the compact connected simple group in the OpenAI theorem. A nonabelian compact-simple extension requires a proved character/loop family that separates the correct quotient and remains stable under scaling.

### YMS-05: subdividing an edge gives a gauge-natural curved arrow (PAPER IDENTITY + EXHAUSTIVE S3 TEST)

For **any group** and an oriented coarse edge \(u\to v\), replace that edge by a two-step path \(u\to w\to v\) with link variables \(A,B\). The **source-preserving** coarse observable is their **ordered product** \(AB\). Under independently chosen site gauges \(g_u,g_w,g_v\),

\[
\boxed{(g_u A g_w^{-1})(g_w B g_v^{-1})
=g_u(AB)g_v^{-1}.}
\]

Thus taking the path product **then** applying the coarse gauge equals applying the refined gauge **then** taking the path product. The internal vertex gauge cancels exactly and the induced map descends to the gauge quotient. For noncommuting \(A,B\), reversing the order \(AB\to BA\) is a real source/path mutation, **not** a valid change of chart. The local test exhausts all \(6^5=7,776\) S3 choices of two link values and three gauge values, and includes a noncommutative reversed-path mutant.

This is the cleanest *actual morphism* resembling the proposed SUCC source-connected arrow: transport along an oriented path is lawfully compositional and coordinate covariant. It is a **finite graph subdivision**, **not** a Wilson renormalization transformation, a physical metric geodesic or a 4D continuum estimate. Real RG additionally integrates over many link variables and must transport the probability law and scale correctly.

## D. SUCC bridges with valid and invalid inferences

| SUCC instrument | Exact overlap | Missing mathematical obligation |
|---|---|---|
| Fourier–Yoneda pinbed (`observational_succ/fourier_yoneda_pinbed.py`) | Harmonic separation of finite **laws**; now a gauge-orbit law example | Source-derived Wilson operator completeness at compact simple G and all scales; YM vacuum is not generic Haar |
| Holonomy and categorical transport (`holonomy_proof_transport.py`) | Path dependence and admissible observations of quotient geometry | Do not interpret declared GF(2) curvature as physical SU(2)/SU(3) Yang–Mills |
| Source-coupled oracle (`bbp_coupled_oracle.py`, PR #609) | Checks that proposed observations share one authenticated source | Wilson action, gauge invariance, OS field limits and no invented alternative measure |
| Coherent observer/pinbed probe audit (PR #612) | Necessary/sufficient/equivalent versus stronger diagnostics | Preserve actual gauge symmetry and quantifier order; negative controls at fixed vs moving scales |
| Signed Schur/Weil RH archive | Quadratic-form authority, source provenance, contrast of positive/negative forms | A positive OS form is **not** the completed signed Weil form; no RH transfer without original primes, Gamma, contact, poles |
| π BBP selected orbit | Two-scale limit/observer discipline | No inference that an unrelated gauge-theory existence proof yields π signed Weyl cancellation |

**Goldbach and Collatz:** neither physical YM gauge symmetry nor the 4D lattice construction supplies their missing number-theoretic mechanisms. A categorical observer analogy alone is not a theorem for any of these problems.

## E. Next falsifiable work: don't reinvent the giant proof, target its open boundary

**Track YM-1 — Proof-contract adapter.** Treat the external Lean project as *external, pinned evidence*, never a theorem silently admitted to SUCC. Reconstruct the exact target `YangMills.JointExistence`, the scoped OS/OPE/trace structures, dependency roots and tool versions from the October source and the group's review. Compile a small **new** Lean wrapper only in an environment with the pinned toolchain, and check its proposition/axioms against their reference files. Do not copy the million-line source into SUCC, or relabel a model test as formal verification.

**Track YM-2 — Gauge-complete Wilson oracle.** Starting from the now-proved **general finite-graph nonabelian** quotient and exhaustive S3 implementation, identify explicit complete, numerically stable mixed-word/representation-character observations for **compact simple** groups; prove the completeness/stability claims, rather than assuming that individual Wilson traces suffice. Then make this observer compatible with actual plaquette-law probabilities, not arbitrary freely chosen masks. Check gauge-equivariance and the topology of periodic lattices against YMS-02.

**Track YM-3 — Scale-uniform gap certificate.** Recover a specific gauge-invariant two-point operator from the existence construction and show a uniform physical-distance bound or spectral inequality in the identified reconstructed Hilbert space. A candidate sufficient form is \(\sup_{a\le a_0}\sup_{t\ge t_0}e^{m t}|C_a(t)|\le C\) with **one** \(m>0\), after specifying the channel, volume limit, normalization and required OS assumptions. Such a bound is **not** an automatic mass-gap theorem for every channel; the exact set of states detected, spectral support and reflection positivity must be checked. Test two distinct continuum scaling families agreeing at all finite calibration cutoffs (YMS-03), low-frequency/zero-energy modes, topological sectors and wrong source laws. Strictly positive finite lattice eigenvalues are never enough.

**Track YM-4 — UV/IR transport anomaly probe.** Define true coarse-graining transport between *Wilson observables* with an operator/basis/source law. Examine a two-path square: gauge quotient before/after renormalization vs renormalization before/after quotient. Its commutator may diagnose source leakage; on exact gauge-equivariant maps it should vanish. If it is nonzero, isolate whether this is a legitimate holonomy/topological obstruction, an instrument approximation, a contact term, or an inconsistent transport map. No invented physics curvature from a diagram alone.

**Track YM-5 — Honest separation of domains.** Preserve source maps to (a) 4D YM, (b) BBP π, (c) completed Weil/RH, (d) Goldbach, (e) Collatz. New mathematics that can transfer between domains must specify a natural transformation/intertwiner **and prove** that it transports the target predicate, not just a visualization or positive energy.

## F. Claim ledger and validation authority

| Claim | Verdict | Proof/receipt | Boundary |
|---|---|---|---|
| YMS-00 external YM existence result | **EXTERNAL ASSESSED**, not locally reproduced | October Lean source; review A1–A8 and dated evidence | No positive gap, unique IR limit or complete all-field OS extension imported beyond its scope |
| YMS-01 exact connected abelian gauge orbit quotient | **PAPER DERIVED + FINITE TESTED** | Spanning-tree gauge-fixing proof; exhaustive 243-field/81-gauge example | Compact simple nonabelian generalization not supplied |
| YMS-01b finite quotient Plancherel pinbed energy | **CLASSICAL + EXACT TESTED** | Finite Fourier orthogonality; uniform/nonuniform controls | Haar on quotient ≠ interacting YM vacuum; energy ≠ mass gap |
| YMS-02 4-torus flat nontrivial connection | **PAPER DERIVED + FINITE TESTED** | Explicit hyperplane link assignment and gauge-invariant Wilson cycle | Nonabelian bundles and continuum unaddressed |
| YMS-03 positivity and gap counterfamilies | **PAPER DERIVED + FINITE TESTED** | Exact eigenvalues and integral upper/lower bounds | 2-state kernel only; NOT 4D YM or OS axioms |
| YMS-04 nonabelian gauge orbit quotient and trace blindness | **CLASSICAL FINITE-GRAPH THEOREM + EXACT FINITE S3 TEST** | Tree reduction yields G^b/G under simultaneous conjugation; 216 fields × 36 gauge maps, 11 orbits; mixed-word trace witness | Does not establish a complete *restricted Wilson character bank* for SU(2) or any 4D QFT |
| YMS-05 oriented subdivision naturality | **PAPER IDENTITY + EXHAUSTIVE FINITE TEST** | Internal gauge factor cancels; all 7,776 S3 inputs; noncommuting reversed-path mutant | Not renormalization or physical geodesic |
| YMS-06 external full Lean proof rerun | **UNVERIFIED HERE** | Requires pinned external build/comparator | Lean not installed; ≈52 GiB external project |
| YMS-07 4D pure YM mass gap | **OPEN** | No source-specific uniform physical gap estimate | Clay problem untouched |

**Validation completed locally:** `python -m unittest discover -s tests -p 'test_yang_mills_gauge_oracle.py'`: **19/19 PASS**, Python 3.13.5, `PYTHONPATH` pointing at the isolated new source mirror. Python `compileall`: PASS. Deterministic finite receipt: `FINITE_RECEIPT.json`. The local mirror contains **only** the new module and tests; it is *not* a complete SUCC checkout. No GPU/cloud simulations, no imported Lean kernel runs, no review of every external file, and no full `AGENTS.md` gates are claimed.

**Required verification in a real SUCC checkout:**

```sh
python -m unittest discover -s tests -p 'test_yang_mills_gauge_oracle.py' -v
python scripts/yang_mills_gauge_oracle_probe.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

**External independent replay, in a separate qualified environment:**

```sh
cd YM/submissions/openai-20261028
python3 scripts/verify.py integrity
python3 scripts/verify.py all
```

The external complete replay is expensive, uses a pinned different repository and compiler chain, and should record its own receipts. It must never be reported as completed by the SUCC toy tests.

## G. Final verdict

**Faithful hypothesis survives:** Gauge-complete source observers plus transport contracts are a mathematically legitimate new SUCC research interface to the published 4D Yang–Mills construction. The finite abelian and nonabelian graph quotients, oriented path naturality and 4-torus topological blind spot are exact. The two-state transfer family refutes any unconditional inference from finite positivity/gaps to a physical continuum gap. The actual source-selected nonabelian uniform spectral estimate, required for a mass-gap theorem, remains an access/probe/pathway gap, not a mathematical consequence of the existence statement. **No RH, π-normality, Goldbach or Collatz claim follows.**
