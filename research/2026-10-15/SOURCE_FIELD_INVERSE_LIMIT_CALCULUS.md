# SimpleField / IdealHard / FuckedField — SOURCE-INDEXED INVERSE LIMITS, SELECTION AND PHANTOM OBSERVATION

**Date:** October 15, 2026. **Research origin:** maintainer's precise field classification, continuing the Tate–Weil–Suzuki source-positive program. **Base:** draft PR #116 (Tate/Suzuki high-sector) exact commit \`e7d1f1cee0357ae78db07545fc8e2571f3aedd47\`. Independent prior work imported conceptually: \`research/2026-10-14/ZENO_SUCC_GLOBAL_PROOF_SHAPES.md\`, \`ZENO_PROOF_DEBT_MACHINE.md\`, \`IDEALHARD_WEIL_SIGN_CONTRACT.md\`, classical König/WKL and computability. Non-main research branch, no historical-file changes or merge. **RH PROVED: NO.** Scholarly priority of the component classical mathematics NOT claimed.

## 0. Maintainer hypothesis, preserved, and the interpretation being tested

The author's operational field distinctions:

> **SimpleFields:** an infinite inverse limit is executable in finite time.
>
> **IdealHard:** an infinite inverse limit is not executable in finite time but is still provable relative to the carrier through a finite→global recursive SUCC process.
>
> **FuckedFields:** a global realization is impossible, or multiple lawful realizations remain nonuniquely indistinguishable from the observer (real versus phantom), without a currently available terminating discriminator.

We preserve this distinction as a **source-/toolkit-relative classification of an object plus an actual claimed output**, not three grades of numerical difficulty or permanent categories assigned to a mathematical equation.

A crucial interpretation repair: infinitely many separately materialized nontrivial output symbols CANNOT be printed in finitely many ordinary machine steps. In a SimpleField, "executable" must mean a **finite exact name/program/proof** that can answer an arbitrary finite coordinate request in finite time, or a finite symbolic operation with a proved global meaning. A finite *physical completion of infinitely many interactions* is not asserted.

Similarly, *resource infeasibility* (a finite algorithm with enormous runtime) is not *Turing noncomputability*. IdealHard may mean either a resource-bound obstruction in the declared toolkit or, more sharply, a mathematically provable absence of a computable selector. Our strongest control uses the latter.

## 1. Precise inverse system and THREE independent propositions (SCF-01)

Fix a declared source law \(\mathscr S\), a reference observer \(\mathsf E\), test/probe closure \(\mathrm{Cl}(\mathsf{Tools})\), and proof calculus \(\mathcal P\). Let

\[
X_0\xleftarrow{\pi_0}X_1\xleftarrow{\pi_1}X_2\xleftarrow{\pi_2}\cdots
\]

be a source-indexed inverse system. The global realization set is

\[
\boxed{X_\infty=\varprojlim_n X_n
=\{(x_n):x_n\in X_n,\;\pi_n(x_{n+1})=x_n\;\forall n\}.}\tag{SCF-01}
\]

At each level, an actual observer has a report map \(O_n:X_n\to Y_n\); these must commute with any declared report bonding maps. The observer has access to reports \(O_n(x_n)\), **not automatically all of x_n**, and finite report availability does not imply finite information content of the underlying mathematical stage.

Separate exactly:

- **Existence \(E\)**: \(\mathcal P\vdash X_\infty\ne\varnothing\), a mathematical proposition; does not extract a named member.
- **Selection/computability \(C\)**: does the declared source/toolkit produce a finite program/name for some **lawful individual global path** whose n-th coordinate is decidable on request, with a proof of uniform correctness? If not, is nonexistence of a computable selector PROVED or merely no method known?
- **Identity/observability \(I\)**: is \(O_\infty:X_\infty\to\varprojlim Y_n\) jointly injective on the actually lawful source histories? This is about distinguishing the **source**, not whether the observer's report is internally coherent.

A statement about property \(P\), such as "the ORIGINAL Weil form is nonnegative on ALL tests at ALL radii," is a FOURTH independent proposition. Even a complete proof of \(E\), an exact stage evaluator and observational faithfulness do not manufacture the property \(P\).

**No scalar truth score:** source/contact \(\kappa\), truth indistinguishability \(\phi\), source-map adequacy \(\sigma\), coupling \(\rho\), probe availability \(\mu\), proof-system strength, and executable complexity remain separate; high coherence does not certify positivity.

## 2. SCF-02 SimpleField: an infinite object has a finite exact executable name (PROVED ELEMENTARY)

For fixed source parameter \(c\in\mathbb N\), set \(X_n=\mathbb Z/2^n\mathbb Z\), with reduction bonding maps, and

\[
x_n=c\bmod2^n.
\]

A finite program with input n computes this coordinate exactly. The single modular identity

\[
(c\bmod2^{n+1})\bmod2^n=c\bmod2^n
\]

proves the entire infinite compatibility assertion, while the original named integer c fixes which point of the inverse limit we mean. Every query halts; no physically executed ω-sequence is claimed. This is a precise **SimpleField of source-specified computable global realization**. The same *carrier* \(\mathbb Z_2\) contains points not fixed by a known finite integer name; source and observer specification matter.

Executable: \`simple_residue_inverse_limit\`. Its finite stage samples are checks; the universal law is proved by modular arithmetic, not by stage sampling.

## 3. SCF-03 IDEALHARD: global existence provable with no computable path (CLASSICAL KLEENE TREE / WKL)

Choose a fixed acceptable effective numbering \((\varphi_e)_{e\in\mathbb N}\) of all partial binary-valued computable functions. Define a decidable prefix-closed binary tree T by

\[
\boxed{s\in T,\ |s|=n
\iff\forall e<n,\;[\varphi_e(e)\downarrow
\text{ within }n\text{ steps to }b\in\{0,1\}]
\Longrightarrow s(e)\ne b.}\tag{SCF-03}
\]

This source law is decidable for any finite s: simulate only finitely many programs for the bounded n steps. It is PREFIX CLOSED: a later admitted node cannot violate an earlier prefix check. For each n there is at least one valid binary string (simply choose the opposite bit for each of the finitely many halting self-programs detected by stage n).

The **classical finite→global theorem**, König's lemma / weak König's lemma for binary trees, therefore proves there is an infinite branch \(b\in[T]\).

But NO infinite branch can be total computable. If a path b were computable, choose an index e of the partial program computing its bits \(\varphi_e(k)=b(k)\). In particular \(\varphi_e(e)=b(e)\downarrow\) after a finite time t. At stage n>max(e,t), the condition of T forces \(b(e)\ne\varphi_e(e)\), contradiction.

\[
\boxed{
(\forall n\; T\cap2^n\ne\varnothing)
\;\wedge\;
[T]\ne\varnothing
\;\wedge\;
[T]\cap\{\text{computable paths}\}=\varnothing.
}\tag{SCF-03B}
\]

The existence proof is finite mathematics **relative to the classical compactness axiom WKL** (not derivable by blindly running all finite stages), while a computable witness does not exist. This is the sharp **IdealHard** scenario the maintainer described: source-consistent global existence, no finite computable realization of any individual admissible path. It is NOT a claim that an actual human/physical observer experiences this tree.

**Finite executable control:** \`finite_kleene_tree_calibration\` accepts a finite *synthetic* bounded self-halting transcript and checks exact prefix closure and nonempty enumerated levels. It does NOT implement the universal numbering, cannot prove the no-computable-path theorem from a finite synthetic trace, and explicitly says so. The mathematical all-level noncomputability follows from SCF-03's paper proof.

**Proof-system dependence:** Reverse mathematics distinguishes WKL from weaker effective systems (e.g. RCA_0). Calling existence "provable relative to carrier" must state the proof principles allowed; a finite proof in classical mathematics is not an executable selector.

## 4. SCF-04 compactness boundary: all finite levels viable DOES force global existence when stages are finite (CLASSICAL)

**Theorem:** For an inverse sequence of **nonempty finite sets** with total bonding maps, the inverse limit is nonempty.

Proof: each finite compatible prefix is realized by choosing a point at a sufficiently deep finite stage and projecting backward. These finitely satisfiable constraints define closed sets in \(\prod_nX_n\), compact because each finite discrete X_n is compact. The finite intersection property gives a point in their intersection; equivalently, apply König to the finitely branching tree of valid compatible prefixes.

**Therefore:** with genuine finite, compact source stages, the literal conjecture "every finite stage admits a compatible history yet there is mathematically NO global history" is REFUTED by compactness. This is a hard boundary, not a limitation of today's numerical probes. In that setting FuckedField must instead concern a different target predicate, nonidentifiable observations, source-inadequate maps, or a proof/effective-selection gap.

**Dropping compactness produces an exact FuckedField-IMPOSSIBLE model.** Let T be the tree of finite strictly decreasing sequences of NATURAL numbers. It has a node at EVERY finite depth n, e.g. \((n-1,n-2,\ldots,0)\); but no infinite descending natural path exists. The root has infinitely many successors, so König's finite-branching hypothesis does not apply. This is a rigorous source-specific proof of **no global realization** despite every finite depth passing. Executable: \`noncompact_descending_field\`.

**Critical application to Tate:** A finite list of prime places or finite truncation of gamma modes is not automatically a finite SET of possible mathematical states. Its test-function spaces can remain infinite-dimensional. One must build explicit compact/finite quotients and source-faithful bonding maps BEFORE invoking SCF-04. Source-infinite information inside each "finite" stage is exactly the type issue the maintainer flagged.

## 5. SCF-05 FuckedField-PHANTOM: the observation map fails to distinguish lawful global histories (PROVED)

Let \(X_n=\{0,1\}^{2n}\), with prefix bonding maps, and permit **all** binary global source histories. Compare the fixed lawful paths

\[
x=000000\cdots,\qquad y=010101\cdots.
\]

They are different: their FULL stage-1 prefixes \(00\) and \(01\) already differ. But suppose observer E sees ONLY the even-coordinate reports \(O_n(z)=z(0)z(2)\cdots z(2n-2)\). Then for all n

\[
\boxed{O_n(x|_{2n})=0^n=O_n(y|_{2n}),\qquad x\ne y.}\tag{SCF-05}
\]

No algorithm whose inputs consist solely of these reports can tell which lawful source is actual, even if it runs forever and sees *every* available report. This is **source-map/σ inadequacy**, not a proof that no global source exists. A newly justified odd-coordinate probe distinguishes them immediately and reclassifies the observer-source pair. The diagnosis is relative to \(\mathrm{Cl}(\mathsf{Tools})\), not eternal ontology.

More generally, \(O_\infty\) is jointly injective iff every pair of different lawful histories differs under some finite observed report. If it is noninjective, no computation over ONLY those reports can recover the hidden distinction. This is the exact lawful **real/phantom** obstruction requested by the user.

Executable: \`hidden_coordinate_phantom\`, with the odd-coordinate mutation serving as positive control.

## 6. SCF-06: moving impostors are NOT one permanent phantom (PROVED QUANTIFIER NO-GO)

Full-prefix observations on all binary global sequences are jointly separating. Nevertheless for the ACTUAL zero sequence x, every finite prefix length n is compatible with some DIFFERENT sequence \(y_n\) whose first n bits are zero and whose (n+1)st bit is one. Thus

\[
\boxed{
\forall n\;\exists y_n\ne x:
O_n(y_n)=O_n(x)
}
\]

holds, while

\[
\boxed{
\exists y\ne x\;\forall n:
O_n(y)=O_n(x)
}
\]

is FALSE. The existential and universal quantifiers cannot be swapped. A different apparent phantom at every finite depth does not prove a **single globally undetectable phantom**. Full projective coordinates always distinguish fixed distinct histories eventually, although no single finite depth identifies all points of the Cantor carrier simultaneously.

Executable: \`moving_impostor\`. This adversarial control is mandatory before claiming that "there could be a phantom somewhere beyond every finite stage" means permanent unidentifiability.

## 7. SCF-07: source property obstruction and genuine RH signs

Let H=ell²(N), P_k the first-k coordinate projection. Given any depth k, choose M≥k and bounded selfadjoint source operators

\[
A_+=I,\qquad A_-=I-2|e_M\rangle\langle e_M|.
\]

The first k×k compressions agree, yet \(A_-\) has the exact negative direction \(e_M\). For **each fixed M**, stage M+1 exposes this difference; no fixed bounded negative operator remains hidden from EVERY dense finite compression. But there is no uniform k excluding an adversarial M. Executable: \`remote_negative_sign_shadow\`. This matches existing SUCC IH-01 and is NOT claimed as a new theorem.

**General dense-exhaustion correction (CLASSICAL):** If bounded selfadjoint A on H and \(P_n\to I\) strongly with finite-dimensional ranges, then

\[
[\forall n,\;P_nAP_n\succeq0]\implies A\succeq0
\]

because \(\langle P_nu, A P_nu\rangle\to\langle u,Au\rangle\). Conversely every strictly negative vector direction eventually yields a strict negative finite compression. An unbounded/form-defined version needs a common dense FORM CORE, graph/topology and continuity assumptions; silently upgrading L² strong convergence to Weil H¹/coercive convergence is forbidden.

**Actual Weil/RH application:** Weil positivity asks for \(Q_\zeta(f)\ge0\) for all compact smooth admissible tests f. A strict violation, if it exists, is by its quantifier itself a mathematically FINITE compact-support counterexample \(f\) on a finite radius a. Proving its value negative by a terminating numerical machine further requires a computably named dense set of smooth test functions, source-typed evaluations with certified errors, and continuation of strict negative sign through approximation. There is no known uniform a, precision, or time bound. "Witness can hide beyond every *known* feasible bound" is compatible with eventual mathematical finite distinguishability.

Our SUCC/Tate/Suzuki imported branch proves \(D_{18}\succeq K/16\) at a=1/2 and a **source-positive high sector at each finite a** by a very expensive finite moment cutoff. This is all-test on the declared high-space, not mere sample-level positivity. The remaining low Schur signs \(S_{a,r}=A_{a,r}-R_{0,a,r}\) are UNVERIFIED, including first-prime \(S_{1/2,18}\).

**THE KEY TYPED CONSEQUENCE:** These facts do NOT classify RH as FuckedField, IdealHard, SimpleField, undecidable, or false. None of those labels follows from an unproved global low-sign implication. The right current claim is

\[
\boxed{
\text{RH source well defined}
\ \wedge\
\text{high sign for each a source-proved}
\ \wedge\
\text{all-a low Schur sign UNVERIFIED}.
}\tag{SCF-RH}
\]

The architecture must classify the **specific proof obligation + toolkit**, not collapse all mathematics into one permanent field label.

### SCF-RH-J2. REAL first-prime source example: a finite negative stage is NOT a global negative witness

An actual arithmetic discriminator is now in the executable module rather than just the synthetic moving negative operator.

Take the original completed zeta Suzuki signed kernel on \(a=1/2\), and the true low Legendre derivative basis mode \(u=L_1(x)=P_1(2x)\), with exactly \(\|u\|_{L^2(-1/2,1/2)}^2=1/3\).

The pinned original source evaluator \`authentic_full_low_entry(1,1,a=1/2,J=2)\` retains the true prime p=2 half-density, TWO signed polar modes, contact, and the first two native \(4j+1\) real Gamma rungs. Its rigorous outward-rational interval satisfies

\[
\boxed{q_2=\langle u,G_2u\rangle<0.}\tag{SCF-RH-J2a}
\]

This is a NEGATIVE result for the **actually sourced truncated operator**, not a counterfeit example. However the omitted Gamma tail is a POSITIVE-definite-kernel correction on mean-zero derivative-coordinate functions, because the OU modes \(e^{-\alpha_j|x-y|}\) are PSD and the associated constant terms vanish on \(\int u=0\). On the original interval of length one, the source-proved \(\sum_{j\ge2}4/(4j+1)^2\le \tau_2=13/81\) gives the rigorous operator inequality

\[
\boxed{
0\le \langle u,(G-G_2)u\rangle
\le \frac{13}{81}\|u\|_2^2=\frac{13}{243}.
}\tag{SCF-RH-J2b}
\]

Therefore the **FULL original-source** quadratic value is enclosed by

\[
\boxed{
q_{\infty}\in
\left[q_2^{\rm lo},\,q_2^{\rm hi}+\frac{13}{243}\right].
}\tag{SCF-RH-J2c}
\]

The actual rigorously obtained q2 interval is strictly negative, but this **full-source enclosure contains zero**. No negative witness to RH follows. The imported PR #116 complete 18×18 J=2 low-block scan independently observed all 18 truncated low diagonal intervals strictly negative; their sign cannot be transferred to the full operator without the omitted source-positive correction and real high/low cross-resolvent.

**Why this matters for the field taxonomy:** a finite model can be internally source-faithful while its property-of-interest changes after lawful completion. This is an **analytic/source-tail probe gap**, not source-map nonidentification or a proof of FuckedField global impossibility. The next instrument is stronger Gamma/J control and the genuine source-residual Schur \(A-L_U-\kappa^{-1}C_U\), NOT renaming the truncated negative mode a "phantom zero".

Executable: \`original_weil_finite_gamma_sign_gap(J=2)\` with source blob assertion through the original analytic low adapter, source Gamma tail, exact Fraction sign tests and a frozen proof receipt. No nontrivial zeta zero is read.

## 8. Effective construction versus enormous finite resources (SCF-08)

The existing all-radius source high theorem defines a finite \(J=2^M\) and Legendre cutoff r(a,L) for every finite rational input a,L, with an elementary closed-form proof. This is a total **computable mathematical construction**: even when M exceeds one million, the requested integers and individual finite stages exist in the ordinary Turing sense. It is not mathematically proven noncomputable just because actual hardware cannot enumerate them under an available budget.

Record two independent diagnostics:

- **Resource-IdealHard relative to budget B:** a finite algorithm/proof may exist, but the required stage exceeds the declared physical wall B.
- **Selection-IdealHard (Kleene):** no computable individual global witness exists at all, although a finite classical existence proof does.

These cases have different outcomes under a future increase of tools: raising B may repair the first, while a computable selector cannot repair the second in the same model. This is a better operational interpretation of the user's Simple/IdealHard boundary than turning "very large" into "infinite."

## 9. Discriminating probe and source-certificate contract (SCF-09)

**Predictions fixed before hostile controls:**

| Model | Every finite level viable? | Global point? | Computable point? | Observer can identify? |
|---|---|---|---|---|
| Fixed-seed 2-adic inverse system | Yes | Yes | Yes, source program | Yes given seed and full residues |
| Kleene effective binary tree | Yes | Yes (WKL) | **No** (diagonal) | Full prefixes separate paths, but no computable selector |
| Decreasing-natural tree | Yes | **No** | No such point | Not applicable |
| Even-bit observer on Cantor source | Yes | Yes, many | Yes (both shown) | **No** with even-bit closure |
| Moving impostors with FULL prefix probes | Yes | Yes, many | Yes for those witnesses | Fixed pairs always distinguish at some depth |

**Probe interpretation:** A "PASS" in a finite Kleene synthetic run validates only the bounded predicate, never WKL or uncomputability. A "PASS" on all n of a mathematical finite-level theorem licenses E only under finite branching/compactness. Genuine FuckedField permanent phantom requires **one fixed pair** of lawful histories with equal ALL available observations, not an adversarial pair changed as n changes. A failed finite positivity sample cannot settle the global all-test sign, and a finite negative witness must be sourced to the original \(Q_\zeta\), not to truncated Gamma or a fake Euler 6.

**Reproduction:** \`observational_succ/source_field_inverse_limits.py\`; \`tests/test_source_field_inverse_limits.py\`; \`scripts/source_field_inverse_limit_probe.py --verify\`; frozen original-source-safe receipt \`research/2026-10-15/SOURCE_FIELD_INVERSE_LIMIT_RECEIPT.json\`. Python 3.10/3.13 CI also runs original Tate/Suzuki high-sector and provenance checks. Tests preserve mathematically PROVED versus executable finite CALIBRATION boundaries.

## 10. Next truly RH-consequential transport

The proposed major theorem should be typed as

\[
\boxed{
\text{source-correct compact Weil hierarchy}
+\text{actual consistent test-domain limit}
+\text{provably transportable low-Schur sign}
\Rightarrow
\text{all-a Weil positivity}\Rightarrow\mathrm{RH}.
}
\]

It must supply ALL of:
1. **Source law / sigma:** original prime-power Euler, half-density, one Gamma_R, contact and both poles; no zeros as construction input and no fake composite 6.
2. **Existence / analytic closure:** a genuine coherent distribution/quadratic-form limit with explicit common test space, source/basis matching, continuity and legitimate quantifiers (not infinitely many separately executed steps).
3. **Uniform sign transport:** either prove each \(\mathcal S_{a,r(a)}\succeq0\) from an actual source-derived law, or a source-preserving gluing invariant propagating low signs for all radii; a high-sector theorem alone cannot discharge this.
4. **Observational identity:** specify what an observer actually reads, and prove the report maps separate **genuine** from modeled/phantom sources, or use an additional lawful conductor/Gamma/sign probe. If no discriminator is known, state \(\sigma\)-UNRESOLVED rather than assume identification.
5. **Hostile controls:** change prime 2, composite 6, conductor/parity, real Gamma/contact, source epoch, parity of low Schur, moved high negative rank, and a noncompact tree. A counterfeit route must fail without conflating an absent experimental certificate with an actual contradiction.

The most valuable new inference is NOT "RH is FuckedField". It is that **finite-to-global existence, finite executable selection, and operational global identifiability require different transducers and different proofs**. Source-indexed SUCC can now test them independently.

## Classical provenance

- John Stillwell, *Reverse Mathematics: Proofs from the Inside Out*, chapter 4, "Computability" (2019), https://doi.org/10.23943/princeton/9780691196411.003.0004 (computable infinite binary trees without computable paths).
- Reinhard Diestel and collaborators, "Profinite separation systems", finite-set inverse-limit compactness lemma, https://www.math.uni-hamburg.de/home/diestel/papers/ProfiniteASSlong.pdf.
- Standard König's lemma / weak König's lemma, finite-branching compactness and its distinction from computable path selection. See John Stillwell (above) and M. Ayala-Rincón et al., *Compactness and Applications* (formal theorem and discussion), https://mat.unb.br/~ayala/CompactnessAndApplications.pdf.
- Original Weil/Schur source: SUCC PR #116 and its immutable ancestors #109, #110, #114. No original academic-novelty claim.

**RH PROVED: NO.** No result in this dossier proves RH undecidable or mathematically inaccessible to any future mathematician or machine.
