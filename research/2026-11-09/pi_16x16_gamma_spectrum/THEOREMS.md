# Source-authenticated 16×16 π spectral tomography and the Euler–Mascheroni firewall

**2026-11-09 · Research only · π one-digit normality OPEN · π two-digit normality OPEN · π full normality OPEN.** Parent #566 (head `4caae7652b430974448437bc716da9a3edba5fd9`), stacked over #562. Original BBP four signed poles, literal U₀=0, imported source, prime/carry interfaces, provenance and main remain unchanged. `PROVED PAPER` is elementary argument plus scoped tests, not new Lean or independent journal review. The fresh 131,072-digit holdout was preregistered at `a07f3646d139be55a565b65fb7318e5709643509` before inspecting additional digits.

## 1. Exactly WHICH 16×16 matrix is being studied? (SETUP)

Let `d_n` denote consecutive **real hexadecimal digits of π** certified from the original BBP source. For N genuine adjacent pairs from N+1 digits, `C_ab= #{0≤n<N : d_n=a,d_(n+1)=b}`, `r_a=Σ_b C_ab`, `c_b=Σ_a C_ab` and `p_ab=C_ab/N`. When each row is observed, the *empirical one-step Markov surrogate* is `P_ab=C_ab/r_a`; this DOES NOT imply the actual infinite deterministic π sequence follows a one-step Markov process. The exactly Haar 16-state transition is `H_ab=1/16`. For a linear prefix, `r_a-c_a=1_{d_initial=a}−1_{d_final=a}`; a synthetic wrap would make the flow exactly stationary but invent one π pair, so **linear is primary**. This is distinct from two further exact operators:

- Original-source **2-adic spatial precision** Haar `H`: sample n uniformly mod256, use `V(n) mod16` as first spatial nibble and `floor((V(n) mod256)/16)` as second. PR #566 proved all 256 pairs occur once.
- Original-source **2-adic temporal first nibble** deterministic permutation `G_ab=1_{b=g(a)}` with `g(a)=a+1 (a even), a−3 (a odd) (mod16)`. It has ONE digit uniformity but not pair uniformity.

The latter two are authentically source-derived yet cannot substitute for real digits.

## 2. Full exact source-odometer eigenbasis (PROVED PAPER, inherits #566)

The source 2-adic first digit is `f(n)=2(n mod2)−n (mod16)` and `f(f(n))=n`. Its time advance obeys `g=f∘(n↦n+1)∘f⁻¹`, hence is exactly one 16-cycle. For `j=0,...,15`, define `v_j(a)=exp(2π i j f(a)/16)`; the Koopman operator `Kv(a)=v(g(a))` satisfies `K v_j=exp(2πi j/16)v_j`. These are an orthogonal complete basis and give **all 16th roots of unity**. In particular the parity vector `(-1)^a` has eigenvalue `−1`, while the constant vector has eigenvalue `1`.

By contrast the 16×16 spatial 1→2 conditional Haar operator `H=J/16` has spectrum `{1,0×15}`; these are **two distinct source-induced matrices**. For the full p-adic odometer at precision 16^k, translation mod16^k is a single 16^k-cycle, giving all 16^k-th roots, and

`det(I-zG_k)=1-z^(16^k)`, normalized trace `(1/16^k)Tr(I-zG_k)^(-1)=1/(1-z^(16^k))` for |z|<1.

This inverse-limit spectral **pure-point** phenomenon is topological; it does not prove temporal real-digit mixing. The π real-digit empirical transition matrix is a separate object below.

## 3. The 225-dimensional invariant-measure/Lagrange space (PROVED PAPER / inherited #566)

Write `r_a/N`, `c_b/N` for row/column empirical marginals. Define the centered joint tensor

`J_ab = p_ab − r_a/(16N) − c_b/(16N) + 1/256`.

Then `Σ_a J_ab=Σ_b J_ab=0`. For exact finite energies `E_row=16 Σ_a(r_a/N−1/16)^2`, `E_col=16 Σ_b(c_b/N−1/16)^2`, `E_2=256 Σ_ab(p_ab−1/256)^2`, orthogonal projection yields

`E_2=E_row+E_col+256 Σ_ab J_ab²`.

The mixed term equals `Σ_(u,v=1)^15 |Σ_ab p_ab exp(2πi(ua+vb)/16)|²`. Thus **225 real dimensions** of signed mixed Fourier imbalance survive after fixing both one-digit marginals. Exactly stationary two-digit laws with one-digit Haar form the 225-dimensional Birkhoff polytope of doubly stochastic 16×16 transition matrices, not a single state. `H=J/16` is the center, deterministic permutation matrices are vertices. One-digit Haar alone leaves an enormous family of non-Haar joint laws, including full-support mixing alternatives.

## 4. New-to-SUCC decisive eigenspectrum firewall (PROVED PAPER, exact SymPy independent check)

Let `u=(1,-1,0,...,0)ᵀ`, `v=(1,1,-2,0,...,0)ᵀ`. Define an **entirely explicit positive doubly stochastic** matrix

`P*=H+(1/64)uvᵀ`.

Both u and v have zero sum, and `vᵀu=0`. Therefore `HN=NH=0`, `N²=0` for `N=uvᵀ/64`, so

`(P*)²=H`, exactly; `det(t I−P*)=(t−1)t^15`.

All 256 entries lie between `1/32` and `3/32`, and the row/column sums are each 1. **The nontrivial eigenvalues are ALL ZERO, IDENTICAL to Haar**, yet `P*≠H`. Its 2-digit stationary pair law is `q_ab=P*_ab/16` and has positive mixed energy

`E_2=Σ_ab(P*_ab−1/16)²=||N||_F²=12/4096=3/1024>0`.

Indeed N has a nontrivial length-two Jordan block at eigenvalue zero (rank(P*)=2, whereas rank(H)=1); the non-Haar singular value is `sqrt(3)/32`. This proves: **the full eigenvalue multiset, a maximal gap, full support, double stochasticity, and even exact two-step Markov forgetting do NOT identify the two-digit distribution**. Singular values / generalized eigenvectors / the 225 Fourier cross-modes do. This is a mathematical no-go, not a statement that π is nonnormal. (An exact separate SymPy calculation verified P²=H, rank2, eigen mults {1:1,0:15}.)

## 5. Rigorous Dobrushin spectral bound on the observed matrices (PROVED PAPER + EXACT finite arithmetic)

For any stochastic P, define the row-contraction coefficient

`δ(P)=(1/2) max_(a,b) Σ_c |P_ac−P_bc|`.

The classical Dobrushin–Deutsch–Zenger inequality bounds every nontrivial eigenvalue by `|λ|≤δ(P)` (no numerical eigensolver needed). For the source-certified real π 65,535 genuine adjacent-pair matrices:

- Original prior block 0..65535: `δ=497311/8555180≈0.05812981141`.
- **FRESH** block 65536..131071: `δ=123803/2292261≈0.05400912025`.
- Full 131,072-digit prefix (131,071 genuine pairs, not the sum of the two disjoint samples): `δ=481818/13186475≈0.03653880207`.

Each is **strictly below 1/2**, so none of these empirical P has a nontrivial eigenvalue equal to Euler–Mascheroni `γ≈0.57721` (or with absolute value that large). Numerical eigenvalue magnitudes agree: prior max ≈0.01647115, fresh max ≈0.01394413, full ≈0.01489851. The mathematical eigen bound is exact rational; these eigendecompositions are floating diagnostics. This does **not** imply convergence of δ(P_A), real digit Haar, or validity of a genuine Markov source model.

## 6. Exact inverse-frequency character projection + negative cold holdout (PROVED identity / OBSERVED nonreplication)

The user-highlighted paired frequencies `u` and `v≡−u mod16` measure digit **difference**, `D_k=#{n: (d_n−d_(n+1)) mod16=k}`. Define

`M(u,v)=N⁻¹ Σ_n exp(2π i (u d_n+v d_(n+1))/16)`, `E_−=Σ_(u=1)^15 |M(u,−u)|²`.

By EXACT finite Fourier Parseval,

`E_− = 16 Σ_(k=0)^15 (D_k/N−1/16)² =16 Σ_k (D_k/N)²−1`.

This is an exact statistic with a geometric and arithmetic interpretation, not a heuristic from individual eigenvalues. But empirical calibration and **new genuinely disjoint source holdout** separate sharply:

| Input | N genuine within-block pairs | E_− | E_−/(15/N) | Percentile vs 1,200 fixed-digit-count shuffles |
|---|---:|---:|---:|---:|
| Previously inspected π digits 1–65536 | 65535 | 0.0004636896253 | 2.02586 | 99.2% |
| Fresh π digits 65537–131072 | 65535 | 0.0001622522870 | 0.70888 | 22.3% |

**Frozen preregistration criterion FAILED:** the fresh result neither exceeded its shuffle 95th percentile 0.00038247507 nor achieved E_−/(15/N)>1.5. Explicit verdict **NONREPLICATION**. The fresh 225-mode mixed energy is 0.00329143191 versus its shuffle mean 0.00343681023; the finite first block was 0.00395272092. The fixed-histogram null is a sampling reference only, not a theorem of independent π digits. Selecting a striking pattern after seeing many modes is not blind validation. The fresh test was committed before 131072-digit calculation.

The opposite-mode top complex character in the old block was `(u,v)=(11,5)` with modulus 0.0097542; the fresh same character is approximately `0.00042646−0.00219625i`, much smaller and differently oriented. The top centered left/right singular-vector directions overlap between the two disjoint blocks in absolute cosine ≈0.0756/0.1373, respectively; these are **exploratory** and not calibrated all-epoch claims.

## 7. Where Euler–Mascheroni truly appears: source finite part, NOT a finite 16-state eigenmode (CLASSICAL + inherited #560)

For the original rational forcing `r(n)=15/(64n²)+(151/512)n⁻³+O(n⁻⁴)`, the source Laplace function `R(z)=Σ r(n)z^n` has

`R(1)−R(z) = (15/64)(1−z)log(1/(1−z))+O(1−z)`.

Writing `D=Σ_(n≥1)[n r(n)−15/(64n)]`, the two regularizations give (SUCC #560)

`lim_N (Σ_(n≤N)n r(n)−(15/64)log N)=D+(15/64)γ`,

`lim_(z↑1) [R'(z)+(15/64)log(1−z)]=D`.

This is the authentic **harmonic discreteness/continuous-Laplace seam**. `H_N−log N→γ` holds for ANY integer N, independent of π's digit dynamics: at N=16,256,65536,131072 the plain values are ≈0.60814027, 0.57916752, 0.57722329, 0.57721948, respectively. Selecting a number of digits to make this expression numerically approach γ is NOT evidence that the 16×16 matrix has γ eigenvalues.

**Finite-state analytic boundary firewall:** every fixed 16×16 matrix P has rational resolvent `(I−zP)⁻¹`; equivalently `det(I−zP)` is a polynomial. Its local singularities can be poles, **not** the logarithmic branch of R(z). The source `log(1−z)` phenomenon requires its actual infinite chronological/source scaling (or an explicitly constructed growing family of transfer operators). A genuine future link must derive a canonical source-weighted infinite-depth spectral determinant/limit whose regularization produces γ **and** distinguishes the zero-seed from coherent wrong seeds. Simply matching finite eigenvalues to γ is mathematically inadequate.

## 8. Frozen evidence, dependencies and scope

- Source-certified 131072 HEX digits from authenticated original numerator/denominator; two full outward integer enclosures at guards 24 and 32 have identical full strings, SHA256 incl newline `4e349f3af293f07c42135caabffe0ce262c7ff282847d71e158f05551cd89a73`. Fresh last-65536 block SHA256 incl newline `344972a0bd1028032907c0e2c9495ad7943265bde1fdd98d4be1c7de38520d03`. First 65536 match PR #566 hash, which matches PR #561 40960-digit precursor.
- Exact source computation is rigorous *conditional on the classical BBP identity for π*. The two guards are separately computed error budgets of the same algorithm, not truly independent BBP sources or referees.
- `FINITE_SPECTRAL_HOLDOUT.json` contains complete 16×16 matrices, eigenvectors/singular-value diagnostics, source hashes, modes, 1200 fixed-count shuffled reference and preregistered test verdict. The numerical spectra/shuffle ranks are not interval-certified mathematical theorems.
- #566 original 2-adic analytic isometry is inherited; #562 full prime CRT carry boundary and #565 conditional Haar and source grouping were inspected read-only; #560 gamma source-side result has explicit prior credit. Source-only/2-adic Haar, empirical real Markov surrogates, and real π normality are different objects.

**Status: π real hexadecimal 1-digit, 2-digit and full normality OPEN.** This round proves the eigenvalue-only obstruction and source-specific finite spectral bounds, and refutes its own exploratory opposite-mode persistence hypothesis on new data. The load-bearing original zero-seed conditional carry-current/spectral saving is still UNVERIFIED.
