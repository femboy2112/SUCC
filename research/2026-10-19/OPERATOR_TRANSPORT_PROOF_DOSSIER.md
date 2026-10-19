# Operator transport: proof dossier and adversarial boundary

Status: **PROVED LOCAL, PAPER** for the statements proved in the accompanying
[Paper B](PAPER_B_ATOMIC_HAAR_TRANSPORT.tex). Scholarly priority is
**UNVERIFIED**. Infinite theorems are not inferred from the finite tests.

## Contract, dependency cut, and source baseline

The target was a finite-to-global star-intertwiner theorem: for increasing
finite prime sets F_j with union P, a uniformly bounded family
T_j: ell²(N+) → L²(Zhat, additive Haar) intertwining the selected shifts and
their adjoints should converge WOT to zero if the selected prime reciprocals
diverge. The target also required fixed-basis support, bounded-test rates,
the summable complement, and a correctly typed distributional alternative.

The weakest sufficient form is stronger than that contract:
**forward intertwining alone suffices for WOT collapse**. Adjoints are
needed for the exact support theorem, not for weak collapse. The proposed
“remove adjoints” countermodel was therefore rejected for the limit claim
and retained only for the support claim.

The argument cuts the attempted promotion from finite-prime unitary
equivalences to nonzero bounded infinite transport. Its proof language is
Hilbert space and profinite measure theory. It uses no signed analytic
form, Gamma estimate, source reconstruction, unproved countable Wold
theorem, or nontrivial zero position.

This lane started at PR179, commit
81684b4b8956f9f5da56c376ba7e4339277eb665, on branch
research/forge-ii-operator-2026-10-19. It independently inspected sibling
PR178, e42096ec0186228dd0f748767599e470f2ca2e1d, using git show.
The reconstructed files were:

- research/2026-10-18/INSTITUTE_ATOMIC_HAAR.md, SHA256
  af274722e2e685c0960127073403da72f3a0e46cc3d0657f89c9dbfcdafcbcca;
- observational_succ/institute_atomic_haar.py;
- tests/test_institute_atomic_haar.py.

The exact PR178 extraction's ten focused tests passed before the new lane's
work. The PR179 provenance checker also passed: 72 items, 17 byte-identical
research archives, 55 mechanical namespace migrations. No imported theorem
or frozen archival file was edited. The new finite implementation is
independent of the sibling module.

## Claims and full derivations

The paper supplies complete proofs. The following map identifies every
load-bearing step, including the distinct forward-only route.

| Claim | Quantifiers and exact conclusion | Proof inputs and status |
|---|---|---|
| D1: calibrated actions | For every a≥1, V_a e_n=e_(an) and U_a f=√a 1_(a Zhat) f(x/a) are isometries; U_a* g=a^(-1/2)g(ax) | Restricted Haar scaling by 1/a; change of variables. PROVED LOCAL |
| D2: star support | For every finite prime set F, bounded selected star intertwiner T, and n≥1, T e_n is supported in K_(F,n)=d_F(n)E_F, of mass α_F/d_F(n) | Write n=d_F(n)r; selected lowering kills e_r; Haar joint kernel is L²(E_F); forward shifts move support. PROVED LOCAL |
| D3: sharp rate | For bounded g, the coefficient modulus is at most norm(T) norm(g,∞) √(α_F/d_F(n)); the localized L² bound also holds | Cauchy–Schwarz; equality from a rank-one wandering map and g=1. PROVED LOCAL |
| D4: forward cylinder rate | For g of period m and G excluding p dividing m, the coefficient modulus is at most norm(T) √(m α_G/d_G(n)) norm(g,2), assuming only TV_p=U_pT | Simultaneous diagonalization and exact backward-eigenvector norm identity. PROVED LOCAL |
| D5: WOT collapse | Every uniformly bounded forward-intertwining family along an increasing exhaustion of divergent P is WOT zero | D4, finite bad-prime removal, vanishing Euler products, two dense spans. PROVED LOCAL |
| D6: summable star complement | Restricted tuples are unitarily equivalent iff the selected reciprocal sum is finite; all star intertwiners are I tensor B on the wandering decompositions | Positive Euler product, disjoint shells covering measure one, equal infinite multiplicities. Reconstructed PR178, PROVED LOCAL |
| D7: unitary topology | Every finite-prime unitary family in D5 is WOT zero but has no strongly convergent subsequence | Fixed nonzero vectors retain their norm. PROVED LOCAL |
| D8: weak limits | Across all finite-star families of norm at most M, possible WOT cluster points are exactly global star intertwiners of norm at most M | Eventual prime equations pass through WOT; global maps are constant families. PROVED LOCAL |
| D9: algebraic distributions | All maps c00→D' preserving actions and lowering correspond to unit-supported vacua η, with J_η e_n=n^(-1/2)(m_n)_*η; nonzero maps are injective | Transposed cylinder actions and compact clopen separation. Reconstructed PR178, PROVED LOCAL |
| D10: typed completion | For δ_1 and its initial test topology τ_J, weak D' is the completion of c00; maps to complete Hausdorff locally convex spaces extend uniquely, including equivariance | Finite interpolation, weak-dual completeness, completion extension argument. PROVED LOCAL |
| D11: norm obstruction | J has no continuous extension from unweighted ell²; no continuous weak-D'→ell² map recovers every e_n; τ_J-continuous maps to normed spaces have finite rank | Harmonic evaluation; J e_n→0; finite-seminorm continuity. PROVED LOCAL |

### The distinct forward-only proof

For a finite prime set G, suppose V_p* h=λ_p h with |λ_p|²=1/p.
Atomic coordinates satisfy h_(kr)=λ_k h_r for k in M_G and r in C_G.
Unique selected factorization and nonnegative geometric summation give

    norm(h)² = α_G^(-1) sum_(r in C_G) |h_r|²,
    |h_n| ≤ norm(h) sqrt(α_G/d_G(n)).

For p not dividing m, R_p:g(x)→g(px) is a unitary permutation on the
m-dimensional cylinder space. These permutations commute. On each
normalized joint eigenvector g_l, U_p* g_l=p^(-1/2)ω_(p,l)g_l, with
|ω_(p,l)|=1. The adjoint of **the forward equation alone** gives
V_p*T*g_l=T*U_p*g_l; the previous calculation applies to h=T*g_l.
A general cylinder test has m eigencomponents; Cauchy–Schwarz on their
coefficients contributes at most √m.

For each fixed period, the excluded primes are finite. Reciprocal
divergence persists, and α_G→0 since −log(1−1/p)≥1/p.
Uniform boundedness permits the dense-span approximations in both Hilbert
spaces. This proves the infinite claim without support intersections and
without assuming any adjoint intertwining equation.

### The exact distribution category

D is the locally constant complex test space with the locally convex
inductive limit topology over finite-dimensional stages D_(j!).
Every algebraic functional on D is continuous. The target is D' with
σ(D',D), and pairings are bilinear. The two distributional actions are
transposes of U_p* and U_p; the lowered action is not a Hilbert adjoint.

Fixing J e_n=n^(-1/2)δ_n is extra origin data. Given a distribution and
finitely many tests, choose a common period m. Let b_r be its mass on the
residue class r mod m. The finite source vector
sum_(n=1)^m √n b_(n mod m) e_n has exactly those pairings. This proves
weak density constructively. A pointwise Cauchy net of linear functionals
has a linear pointwise limit, proving completeness. These facts yield the
completion property. Continuous action identities extend from the dense
image.

This category is restrictive and explicit. Any continuous linear map from
(c00,τ_J) into a normed space is controlled by finitely many test seminorms;
it therefore factors through one finite cylinder dual and has finite
rank. The completion does not retain the atomic Hilbert norm. The
classical completion property is not presented as a new universal principle.

## Adversarial receipts

| Alteration or overclaim | Exact receipt | Verdict |
|---|---|---|
| Drop uniform boundedness | R_F e_1=α_F^(-1)1_EF extends to a selected star map of norm α_F^(-1/2), while its pairing with 1 stays equal to 1 | REFUTED WOT collapse |
| Drop reciprocal divergence | For summable P, a fixed nonzero global unitary is a constant finite-intertwining family | REFUTED WOT collapse |
| Claim all summable-regime families converge | T_j=(−1)^j T for a fixed global unitary | REFUTED |
| Claim WOT-zero unitaries converge strongly | norm(T_j f)=norm(f) for every fixed nonzero f | REFUTED |
| Replace d_F(n) by n before all divisors are selected | F={2,3}, n=5: actual mass 1/3, proposed mass 1/15 | REFUTED |
| Drop adjoints from exact vacuum support | For F={2}, T=U_2S and S e_1=√2 1_odd give T e_1=2 1_(v_2=1), with U_2*T e_1≠0 | REFUTED |
| Say adjoints are necessary for WOT collapse | D4–D5 prove collapse with only forward equations | REFUTED necessity claim |
| Treat a prime dividing the test modulus as a unitary permutation | Period-six test (2,−1,3/7,4,−3,5) changes norm under pullback by 2 | REFUTED |
| Promote completion to Hilbert transport | Harmonic evaluation is unbounded on ell²; also J e_n→0 while norm(e_n)=1 | REFUTED |
| Infer the canonical vacuum from actions | Every unit-supported distribution is allowed, including δ_u for any profinite unit u | REFUTED |
| Infer the global theorem from finite residue checks | Finite code verifies no reciprocal divergence, completeness or density statement | Invalid inference |

## Primary-source comparison and novelty tax

Primary sources were checked on 2026-10-19. These are bounded comparisons,
not a completeness claim about the literature.

| Primary source | Exact location and comparison |
|---|---|
| [Sarkar, Wold decomposition for doubly commuting isometries](https://www.isibang.ac.in/~jay/papers/wold_n_var.pdf), [DOI](https://doi.org/10.1016/j.laa.2013.12.011) | Corollary 3.2 and Theorem 3.3, printed pp. 8–9, give the finite-tuple joint wandering decomposition and Hardy-space multiplicity model. This is a predecessor for finite shell multiplicity, not a countable promotion theorem. |
| [Dan–Guo, arXiv:1907.05815v2](https://arxiv.org/abs/1907.05815v2), [full text](https://arxiv.org/pdf/1907.05815), [DOI](https://doi.org/10.1007/s11425-020-1965-1) | Definition 1.1 and Corollary 1.4 specify infinite Beurling generation. Proposition 3.4 and Remark 3.5, printed pp. 29–30, exhibit zero joint defect outside that class. The broad infinite Wold obstruction is prior art. |
| [Bost–Connes, 1995](https://doi.org/10.1007/BF01589495) | Primary publisher record verified for arithmetic operator-algebra context. Author/preprint PDF retrieval was unavailable in this pass. No uninspected theorem is used as a premise or claimed exact predecessor. |

The new-to-project gains are the finite-to-global obstruction, sharp
selected-factor support rate, stronger forward-only proof, and explicit
test-topology completion costs. Their elementary mechanisms incur a large
classical-specialization tax. Scholarly priority for the arithmetic
formulations is **UNVERIFIED**; no new Wold or abstract completion theorem
is claimed.

## Reproduction and finite/infinite boundary

Commands run in the isolated lane:

    python scripts/verify_provenance.py
    python -m unittest discover -s tests -p 'test_forge_operator_transport.py' -v
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp research/2026-10-19/PAPER_B_ATOMIC_HAAR_TRANSPORT.tex
    git diff --check

The focused suite has seven passing tests with exact Fraction values.
It independently counts valuation shells over all subsets of {2,3,5,7}
and selected integers, then uses held-out primes 11,13 and unselected
factors 17,19. It checks sharp normalized-shell pairings, prime-exclusion
mutations, direct exponent-box sums, and interpolation of signed rational
cylinder data compatible with coarser moduli. Resource caps reject
unbounded residue enumeration; floats, composites and duplicate primes
are rejected.

The paper compiles to eight pages; a second pass resolves references.
The PDF is a derived build artifact. Whole-repository validation and final
integration belong to the root lane; these focused receipts do not claim
that the full suite has run here.

Independent adversarial review by the formal-audit agent found no
normalization, quantifier, or topology defect in the forward-only proof,
distribution classification, weak-dual completion, interpolation, or
Hilbert-interface counterexamples. The root independently reconstructed
the shell bound and forward-only eigenvector argument. This is human-style
proof review by separate agents, not a formal-kernel proof.

No missing mathematical lemma remains for D1–D11 as stated. The next
falsification opportunities are formal measure-theoretic verification and
a broader exact-priority search. Neither is a premise silently supplied by
the finite tests. No signed Weil identification or positivity follows.
**RH PROVED: NO.**
