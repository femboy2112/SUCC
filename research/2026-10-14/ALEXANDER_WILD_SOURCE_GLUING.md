# Operation WILD-SUCC — Alexander's horned sphere, source-indexed nonabelian limits, and the Weil boundary

**Date:** 2026-10-14 (New York). **Pinned parent:** `femboy2112/SUCC` `research/signed-weil-h1-spectral-tail-2026-10-14@526bad9e55ec2506c52b0dc2ac2cf2b4252a2473` (draft PR #84), itself descended from genuine theta/Weil PRs #82/#78/#74/#73/#71. **Read-only siblings:** #85 finite source hierarchy; #86 authentic arithmetic meta-Weil boundary; #68 prime-chart sphere, #80 meta-holonomy. No merge into main, other branches, or the RH repository. **RH PROVED: NO.** No nontrivial zeta zeros are construction inputs, and no physical world is claimed to be a wild embedding.

## 0. Steelman: the finite-source sphere has two very different geometries

The maintainer's hypothesis is not that a sphere is literally knotted. It is that a globally simple object could admit observer- or carrier-relative realizations whose **ambient coupling across infinitely many resolutions** remains unseen when only the local intrinsic charts are read. The mathematical repair is to distinguish:

1. Intrinsic geometry: the source-manifold, e.g. `S²`, its singular/Čech homology and intrinsic SUCC paths.
2. **Embedded** geometry: a declared map `e:S²↪S³`, its complement, port/causal access and holonomy / fundamental group.
3. Bonding/source diagram: arrows linking actual chart versions `E_n→E_(n+1)`, including orientations, domain losses and resource cost.
4. Analytic/operator shadow: `H¹` forms with their correct signed prime/Gamma/pole couplings and chosen operator topology.

Do not silently identify these four. The bold candidate is a **source-indexed pro-/ind-diagram with ambient interaction diagnostics**, not a claim that `ξ` is a physical sphere or that wildness itself implies RH.

## W1 — Alexander's genuine horned-sphere source: the complement sees what the sphere cannot (CLASSICAL IMPORT)

J. W. Alexander, *An Example of a Simply Connected Surface Bounding a Region which is not Simply Connected*, PNAS **10** (1924), 8–10, DOI 10.1073/pnas.10.1.8, constructs an embedding `e:S²→S³` whose unbounded exterior component has nontrivial fundamental group although `e(S²)` is homeomorphic to the standard 2-sphere. Allen Hatcher, *Algebraic Topology*, Example 2B.2 (book pp. 170–172), explicitly constructs the exterior group by free-group injections:

```
F_1 --iota_0--> F_2 --iota_1--> F_4 --iota_2--> F_8 ...
iota_n(g_i) = [g_(2i-1),g_(2i)]
[x,y] = x y x^-1 y^-1
```

Here `F_(2^n)` has `2^n` genuinely distinct free generators. These are **actual exterior loop groups for Hatcher's nested X_n approximants**, not the fundamental groups of individual finite tame boundaries `∂B_n`; those two finite geometries must not be conflated. The exterior is the increasing union of `Y_n=R³\X_n`. Hatcher proves injections by free-product normal forms and uses compactness of loops/homotopies to identify the direct limit with the exterior group.

**W1 theorem (reproduced algebraically).** Every `iota_n` is injective. Indeed each pair of new letters generates a free factor `F(a_i,b_i)`, `[a_i,b_i]` has infinite order, and their cyclic subgroups lie in distinct free factors of `F_(2^(n+1)) = *_i F(a_i,b_i)`. The normal-form theorem for free products makes the free product of these infinite cyclic groups an embedded free subgroup. Hence the meridian `g_1` survives in the direct limit `G`, so `G≠1`.

However, each image generator is a **commutator**, so the induced map on first homology/abelianization is zero:

`H_1(F_(2^n);Z)=Z^(2^n) --0--> Z^(2^(n+1))`.

Abelianization DOES commute with this filtered colimit (it is a left adjoint):

`G_ab = colim (Z^(2^n),0) = 0`.

Thus `G=[G,G]` is perfect and nontrivial. Equivalently, every `G→U(1)` one-dimensional character is trivial. Every map from `G` into a **solvable group** (in particular a nilpotent group) is trivial: the image of a perfect group is perfect and a perfect solvable group must be trivial.

Alexander duality yields the same H₁ blindness for the actual exterior of the embedded S². It is **not** a theorem that every nonabelian representation of this group exists in a convenient finite matrix algebra; importing one without construction would create a ghost observer. Intrinsic homology of the source sphere and even exterior first homology do not detect wildness. **The ambient complement group does.**

**Scientific status:** Alexander/Hatcher geometric realization IMPORTED; elementary injection, abelianization and explicit group tower PROVED LOCAL (paper proof); exact finite computations TESTED. No original scholarly priority.

## W2 — quantified SUCC commutator-depth blindness (PROVED LOCAL + CLASSICAL Magnus import)

Write `w_k` for `g_1` transported through `k` stage arrows. Then `|w_k|=4^k` as a **freely reduced explicit word** (disjoint source labels prevent cancellation) and `w_k` contains `2^k` independently named free generators. Recursive commutator calculus gives

`w_k ∈ γ_(2^k)(F_(2^k))`, where `γ_1(F)=F`, `γ_(m+1)(F)=[γ_m(F),F]`.

By the standard Magnus-expansion theorem, the **first nonzero homogeneous term** of the Magnus expansion has degree exactly `2^k`, because it is the nonzero Lie word recursively obtained by bracketing two disjoint supports. Its explicit leading polynomial has `2^(2^k−1)` distinct monomials with coefficients ±1; no cancellation occurs because the left and right supports are disjoint. **Sharpness by lawful finite-stage operator probe:** map stage-k generator `g_i` to `I+E_(i,i+1)` in the integer unitriangular matrix group `UT_(2^k+1)(Z)`, whose nilpotency class is exactly `2^k`. A direct nested-matrix commutator calculation gives the meridian `I+E_(1,2^k+1)≠I`. These probes are stage-specific and explicitly **fail** to form a representation of the full perfect direct limit; otherwise W1 would be contradicted. Consequently

`w_k ∈ γ_(2^k) \ γ_(2^k+1)`.

**Observer consequence (exact finite theorem):** every source-compatible probe which factors through a nilpotent quotient of class `c<2^k` must report **identity** on the transported `w_k`, although the exact free-group state is nonidentity. A naive explicit-word carrier pays `4^k` letters; this is **not** a universal computation-complexity lower bound, because a DAG/grammar can compress the symbolic process.

For the full direct-limit group, even arbitrarily high but fixed nilpotency class detects no nontrivial global meridian (W1's perfect-solvable no-go). A nonabelian observer must therefore be more expressive than a scalar/abelian/nilpotent-compressed history; this does not assert that the completed Weil form has a hidden free-group presentation.

`observational_succ/wild_embedding_succ.py` performs exact word reduction, transports up to source budget, computes Magnus leading Lie polynomials, independently checks truncated Magnus series at initial depths, and executes sharp integral unitriangular group detectors through stage three. Source labels and operator domains remain typed.

## W3 — two different "spherical" limits must not be conflated (CLASSICAL + PROVED FINITE INTERFACE)

A separate, deliberate **negative control** is the sphere inverse tower

`S² <-^(degree p_0) S² <-^(degree p_1) S² <- ...`

where each map is the suspension of `z↦z^p` on `S¹` and `p_n` is a source-certified genuine prime. Every stage has **intrinsic** `H²=Z` and looks exactly like `S²`. Čech cohomology is continuous under inverse limits of these compact CW objects, so

`Čech H²(X) = colim[ Z --×p_0→ Z --×p_1→ Z ... ]`.

For an infinitely repeated prime cycle `P`, this group is `Z[P^-1]`, e.g. `Z[1/2]` or `Z[1/2,1/3]`, not `Z`. Thus the inverse-limit space is **not** a standard S² despite all its finite stages being standard spheres. A twist postponed beyond any chosen observation horizon creates the same bounded prefix as the identity tower but a different global invariant. This is a classical inverse-limit/cohomology calculation, newly source-typed to the SUCC prime clock. A composite degree-6 map is perfectly lawful topology, but **not** an independently authenticated primitive Euler-place SUCC.

**CRITICAL:** this construction is NOT Alexander's horned sphere. Its bonding maps are noninjective degree-p maps; the horned sphere is instead an intrinsic S² **embedded wildly** in S³. The two examples show *different failure modes*: (a) ambient complement data forgotten, (b) bonding data forgotten. They cannot be combined into one alleged topological model of ζ without an actual source functor.

## W4 — no-free-wildness via ambient bidirectional metric coherence (PROVED LOCAL, classical Arzelà–Ascoli)

Let `M=S³` with a fixed compact metric, `S=S²⊂M` the standard equator, and `h_n:M→M` homeomorphisms such that `h_n|_S` converges **uniformly** to an embedding `e:S→M`. Suppose the ambient `h_n` and their inverses are uniformly `L`-Lipschitz, with the same finite L independent of n. Then **e is tame**.

**Proof.** The two families are uniformly equicontinuous and have ranges in compact M. Apply Arzelà–Ascoli to select a common subsequence `h_(n_j)→h` and `h_(n_j)^(-1)→g` uniformly. Passing to limits in both identities `h_n∘h_n^-1=id` and `h_n^-1∘h_n=id` yields `h∘g=g∘h=id`, because the maps and inverses are uniformly equicontinuous. Thus h is an ambient homeomorphism and its restriction to S equals e. This makes e tame.

**Contrapositive:** approximating a genuine wild sphere through ambient homeomorphisms necessarily loses **uniform bi-Lipschitz conditioning** (or the convergence/ambient realization hypothesis). We can call this a rigorous *geometric resource/conditioning debt*, but not measured physical energy. Diverging distortion is NOT sufficient for wildness: `h_eps(x)=(x³+eps x)/(1+eps)` are homeomorphisms with inverse Lipschitz `~1/eps` but converge to the tame homeomorphism `x³`.

Finite rational controls also exhibit `h_eps:[0,1]→[0,1]` with slopes `eps,2-eps` on its two halves: forward error O(eps), inverse conditioning `1/eps`, and a noninjective limit collapsing an interval. This is a metric model, not Alexander's actual geometry.

## W5 — the REAL Weil source already exhibits an analytic "wild boundary" symptom (PARENT IMPORT + PROVED CONTROLS)

The original SUCC Suzuki wavefront work (PR #64; subsequently #70) proved for genuine prime-power `n=p^k`, `ell=log(n)`, `c=Lambda(n)/sqrt(n)`, first-activation `delta=2a-ell↓0`, that the source-correct **continuous hinge** operator has

`||G_(n,a)^raw||_HS² = c² delta⁴/6 →0`,

while the **correct differentiated** bounded operator on the v-variable has

`||B_(n,a)||_op = c` for **every** small positive delta **in bare L² on the v-variable**.

Normalized paired endpoint tents realize L² Rayleigh values `±c`, while their derivative energy divided by L² mass equals `12/delta²`, diverging at the onset. **Crucial metric repair:** on the correctly declared `H_0¹` carrier, `Q_n(v)=<G_n (i v'),i v'>` and the SAME genuine HS bound proves the **squared H¹ Riesz operator-norm bound** `||A_n^(H¹)||² <= c² delta⁴/6 ->0`. On a paired normalized tent, the H¹ Rayleigh value is `∓c/(1+12/delta²) ->0`. This uses the parent's exact original source identity and is a real analytical stabilization—not a claim that the first-prime coupling has vanished in L². Under zero extension to a common L²(R) source carrier, `B_(n,a)→0` **strongly but not in operator norm**. These identities are already genuine prime/Gamma-source mathematics on the original first-wavefront object, not novel topological inference.

This is an *analytic analogue of concentrating ambient complexity*: negligible continuous-kernel size does NOT license dropping the nontrivial differentiated boundary interaction. The exact rational tool checks the `delta⁴` and `delta^-2` scaling on a bounded surrogate rational coefficient. **That surrogate does NOT replace the authentic irrational `log 2/sqrt2` when assessing the true Weil form.** Wild embedding does not prove that analytic wavefronts are homeomorphic to horned-sphere complements.

## W6 — a quantitative source-topology criterion that could matter for Suzuki (PROVED GENERAL, RH APPLICATION OPEN)

**Classical collective-compactness upgrade.** If self-adjoint bounded `A_n` on a Hilbert space converge strongly to `A` and the set `∪_n A_n(B_1)` is relatively compact (collective compactness), then `||A_n−A||→0`. Sketch: A is compact by pointwise convergence into the compact closure. For any unit vectors `x_n`, pass to a weakly convergent subsequence. Collective compactness gives strong convergence of `A_n x_n`; self-adjointness plus strong convergence on fixed test vectors identifies its limit as `A x`; compactness of A gives `A x_n→A x`. Contradiction if the operator error stays above epsilon. Self-adjointness (or adjoint-strong convergence) is essential to this argument.

**Hostile control:** on `ell²`, `A_n=−|e_n><e_n|` are compact, negative, and converge strongly to zero while `||A_n||=1`; their union of unit-ball images contains `e_n` and is NOT relatively compact. Each fixed finite coordinate observer eventually sees only zero. This is a generic model, NOT an original-source zeta counterexample.

The PR #84 **authentic** signed Weil `H_0¹(-a,a)` Riesz operator is compact for EACH FIXED a by a source-spectral approximation theorem. Consequently, for any fixed source-compatible nested orthogonal projections `P_N↑I` in that Hilbert norm,

`||A_a−P_N A_a P_N||→0`.

But **no uniform rate in a, and no nonnegative sign, follows**. The first-prime family shows why merely having compact operators separately does not supply collective compactness as the parameter crosses a boundary. The source-certified signed spectral tail from PR #84 gives one genuine rate in the spectral-height direction; its low-height signed middle remains unclassified. PR #85 supplies a separate **source-continuous** compact Gamma hierarchy and one-sided positive Gamma tail; PR #86 supplies genuine first-window source forms positive on a 30-moment-null subspace but does not prove the remaining finite-dimensional Schur inequality. These are the relevant, still open concrete interfaces.

**Proposed next sign gate (not proved):** retain all original prime-power, Gamma/contact, rank-two pole and half-density terms and construct a wavefront-aligned low/high decomposition with a **certified source-relative Schur complement**. Find `A>0`, `B` and signed source cross term `C` with `B−C* A^-1 C >=0` on the entire unresolved low carrier, with genuine operator-domain and error certificates. In parallel require uniform inter-window boundary conditioning or explicitly account for its divergence. The wild homology-blind analogy becomes load-bearing only if a real source map identifies its nonabelian holonomy/inverse structure with those original Weil couplings. The arithmetic full-line multiplicative prime dilations and Gamma convolution already commute; do not import a nonabelian "horned" group by fiat. Actual noncommutation can arise upon additive SUCC or finite-interval compression, as separately demonstrated in #86.

## W7 — a precise source-Gaussian repair of the solenoid-to-Weil spectral mismatch (PROVED LOCAL / SIBLING IMPORT)

**Read-only sibling update:** `research/wild-adelic-embedding-solenoid-2026-10-14@721778bf7df28ab52a57346c8d8f4f31bf2b2c13` (separately descended from genuine arithmetic meta-Weil #86) proves that the compact additive prime-solenoid's real translation-flow Haar-L² has **pure point** characters, whereas Lebesgue `L²(R)` translations have **no nonzero eigenvectors**. Consequently **every bounded exact full-flow-equivariant operator in either direction is zero**. This is a classical Fourier/Plancherel spectral-type argument, not established by this branch's finite source tests. The sibling further distinguishes the additive solenoid and multiplicative idele class, preventing a fake Weil identification.

**The character frequencies `r` belong to the inverse-limit CIRCLE solenoid (or its Pontryagin dual), not to the suspended-sphere inverse-limit object of W3.** They share genuine-prime degree labels and the same localized integer group, but the topological carriers are different.

**Repair the representation TYPE, not the theorem.** For `tau>0` and an authenticated additive prime-solenoid character frequency `r` in the rational localization `Z[P^-1]`, take the **normalized Gaussian packet**

`h_(tau,r)(x)=(2tau)^(1/4) exp(-pi tau x²) exp(2pi i r x)`,  `x∈R`.

This is an ordinary **L²(R)** state with exactly norm one. It is not a genuine joint translation eigenfunction. Direct Gaussian integration proves the exact identities, where `(T_t f)(x)=f(x+t)`:

`||T_t h_(tau,r)-exp(2pi i r t)h_(tau,r)||² = 2(1-exp(-pi tau t²/2))`  (W8a),

`<h_(tau,r), h_(tau,s)> = exp(-pi (r-s)²/(2tau))`  (W8b).

This is **a finite-family approximate source intertwiner**, not a bounded exact map of the whole solenoid Hilbert space. For the budgeted unit `tau=N^-2`, for all rational `|t|≤T` and each fixed finite list of pairwise distinct source-local characters with squared separation `d²`:

`translation residual² ≤(22/7)T²/N²`,

`||Gram−I||_op ≤ (m−1)/[1+(3/2)d²N²]`   (W8c).

Proof: `3<pi<22/7`, `1−e^(-x)≤x`, `e^x≥1+x`, and the Gershgorin/row-sum estimate. Define the actual **finite-dimensional source-to-analytic operator** `B_(N,R):ell²(R)→L²(R)` on a chosen finite set of distinct authenticated characters by `B e_r=h_(N^-2,r)`, and let `D_t e_r=exp(2pi i r t)e_r`. Then for the m basis elements, Cauchy–Schwarz and the per-packet estimate give the true **finite-family almost-intertwining operator inequality** `||T_t B−B D_t||²_op <= m*(22/7)*T²/N²`. The Gram bound above is equivalently `||B*B−I||_op <= (m−1)/[1+(3/2)d²N²]`. These operator inequalities are sharp enough to distinguish a genuine finite-dimensional construction from a collection of unconnected scalar observations; they do **not** extend uniformly over the infinitely dense source frequency set. The probability mass in any fixed spatial window `[-R,R]` satisfies `∫|h|²≤(2R sqrt 2)/N <3R/N`. Thus for fixed finite source probes the packets become approximately translation-equivariant and orthogonal while **spreading out of every fixed spatial window**. There is no strong L² limit as N→∞; they converge weakly to zero. This is a mathematically exact **information/conditioning debt** appropriate to the user's IdealHard field language, *not* actual physical energy or quantum scattering.

**Sharp source nonuniformity:** the additive prime character group `Z[P^-1]⊂R` is dense for any prime p repeated indefinitely. For any fixed finite N choose authenticated character gap `delta=1/p^k <1/(8N)`. By `e^(-x)≥1−x` and `pi<22/7`, the Gaussian Gram overlap obeys

`<h_(N^-2,0),h_(N^-2,delta)> ≥ 1−(11/7)N²delta² >9/10`  (W8d).

So **no one Gaussian packet width** yields a near-orthogonal isometry of all source characters. The actual original solenoid has no bounded nonzero flow intertwiner at all; this finite packet construction does not contradict that theorem because its frequency set and N are restricted and its covariance error is nonzero.

**Even stronger Alexander obstruction:** Hatcher's original horned exterior group G is perfect, whereas every additive solenoid is abelian. Thus *any* abstract homomorphism G→Sigma is trivial. One must not identify the nonabelian embedded exterior loop group with the additive solenoid character group via a spurious 'sphere = arithmetic' arrow. The two source families are deliberately independent; combining them in a genuine Weil object requires a different, typed, nonabelian-to-analytic correspondence with verified arithmetic prime/Gamma/pole normalization.

**Status:** Gaussian integrals, finite signed/Gram bounds and rational source authentication PROVED LOCAL; the pure-point/continuous-spectrum NO-GO belongs to separately reviewed sibling WA-20 CLASSICAL + IMPORT; exact sub-source implementations and hostile fixed-N collision tests TESTED. Full signed completed Weil sign / RH still UNVERIFIED.

## W9 — adversarial controls / limits / citations

- **Intrinsic =/= embedded:** Abstract `S²` homology and even H₁ of exterior miss Alexander wildness, which lives in nonabelian π₁ and ambient isotopy class.
- **Finite-stage approximation ≠ completed infinity:** Exact subgroup injections preserve π₁ while nilpotent or abelian readouts eventually kill transported generators; no finite uniform observation horizon for unknown nested programs.
- **Colimit vs scalar report:** Abelianization DOES commute with group colimits. The failure is *loss of nonabelian information*, not a false mathematical claim of nonfunctorial abelianization.
- **Solenoid-sphere != horned sphere:** Stagewise S² with degree-p bonding changes the intrinsic inverse limit; Alexander retains intrinsic S² but changes exterior.
- **Finite group probe control:** A perfect nontrivial group need not have a convenient verified nonabelian matrix representation; no such representation is manufactured by this implementation.
- **No-free-warp converse fails:** large inverse distortion may converge to a benign homeomorphism; physical energy is not mathematically specified.
- **No-free-positivity:** positive finite models, Gram matrices, Gaussian moment kernels, or π₁ obstructions do not imply the sign of the authentic completed Weil form.
- **Source authenticity:** composite 6 can be a perfectly valid topological degree or affine dilation but is never an independent Euler prime; genuine contact/half-density/parity/character conditions remain separate.
- **Independent control:** wrong group stage, generator outside carrier, float leakage, lost source prime, missing inverse map and sign-blind Schwartz source are rejected or scope-labeled.

### Sources

1. J. W. Alexander (1924), *An Example of a Simply Connected Surface Bounding a Region which is not Simply Connected*, PNAS 10(1), 8–10. DOI: https://doi.org/10.1073/pnas.10.1.8 . **Original historical construction**.
2. Allen Hatcher, *Algebraic Topology*, §2.B Example 2B.2, book pp. 170–172: https://pi.math.cornell.edu/~hatcher/AT/AT.pdf . **Group-system free injections, commutator source and perfect exterior group**.
3. Standard free group / Magnus theory: lower-central series and Magnus leading homogeneous term, e.g. Magnus–Karrass–Solitar, *Combinatorial Group Theory* (classical import; exact finite expansions supplied).
4. Čech cohomology continuity and dyadic-solenoid example, e.g. https://www.math.uni-bielefeld.de/~drust/papers/thesis_corrections.pdf §1.2.21–22. Suspended degree-p S² tower follows by the suspension isomorphism.
5. Classical Arzelà–Ascoli + topology of wild embeddings; contextual modern article https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/topo.12309 .
6. Exact Gaussian Weyl-sequence / continuous-vs-pure-point spectral analysis, and independent sibling SUCC `research/wild-adelic-embedding-solenoid-2026-10-14@721778bf7d` (WA-20); separate ancestry and no shared numerical independence claim.
7. Source-correct original Suzuki/Gamma/Weil work: SUCC draft PRs #64, #70, #71, #84, #85, #86. The numerical and source obligations differ; sibling PRs are **not ancestry**.

### Reproduction / epistemic scope

`PYTHONPATH=. python -m unittest tests.test_wild_embedding_succ -v` is the exact focused suite, and `python scripts/wild_embedding_succ_probe.py --verify research/2026-10-14/WILD_EMBEDDING_SUCC_RECEIPT.json` is the byte-independent JSON receipt. Both include genuine-prime authentication, free-word and Magnus checks, group transition/cancellation, delayed sphere bonds, inverse-conditioning control, concentrated Weil proxy and the signed finite Schur control.

**Statuses:** W1 geom = CLASSICAL IMPORT; W1/W2 algebra = PROVED LOCAL, TESTED finite; W3 = CLASSICAL Čech + TESTED source type; W4/W6 = PROVED general analysis, finite rational controls; W5 = PARENT genuine-source theorem + TESTED exact surrogate; W7/W8 Gaussian finite packet = CLASSICAL GAUSSIAN INTEGRALS/PROVED LOCAL with independent sibling spectral no-go; any identification of an Alexander horned-sphere complement with Suzuki's completed Weil carrier or RH proof = UNVERIFIED. Academic novelty not claimed; no Lean kernel proof or empirical physical observation is asserted.
