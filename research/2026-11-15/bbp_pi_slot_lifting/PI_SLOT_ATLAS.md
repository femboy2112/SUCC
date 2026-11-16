# Audit of load-bearing π slots in the maintained SUCC BBP frontier

**Coverage:** Maintained Main XXV `docs/PI_NORMALITY_FRONTIER.md`, `docs/PI_FRONTIER_CONTRACT.md`, original `observational_succ/duck_bbp.py`, and working draft #646/#648/#649 theorem interfaces. This inventories **declared functional families**, not every historical or textual occurrence of the glyph π in the whole repository. Changes are algebraic type-preserving substitutions, not numerical fitting.

Let `C` be the exact #649 binary click, `τ` its shared original uniform threshold, `Y_n=Cτ^(8n)`, `T_n=E Y_n`, `U_n=E C(16^n-τ^(8n))`, and `x=E C=π/16` by the imported classical BBP identity. Let `e(t)` denote the unique standard unit-circle character of real turns (whose usual expression is `exp(2πit)`). **This use of geometric π in the circle character is a coordinate normalization, not a hidden input value of the arithmetic target.**

| ID | Previously π-bearing mathematical interface | Exact π-target-free lifted object | Preservation / source-truth debt |
|---|---|---|---|
| S0 | Euclidean geometric `π` | `4∫_0^1dt/(1+t²)`; BBP equality `16∫Q/(16-t⁸)` | The identity between geometric circle and BBP formula is classical/imported, **not** recovered from Poisson sampling |
| S1 | `x=π/16` | `E C = ∫g(t)dt` | Source coin uses only uniforms, threshold comparisons/maxima, rational expressions |
| S2 | `P_n` partial π source | `E[C(1-(τ⁸/16)^n)]` | This is `Σ_{j≤n}16^-j r(j)`; original literal zero |
| S3 | `U_n=16^n P_n` | `E[C(16^n-τ^(8n))]` | Finite polynomial integral is exactly rational, with *unreduced* integer winding |
| S4 | `T_n=16^n(x-P_n)` | `E[Cτ^(8n)]=∫g(t)t^(8n)dt` | Positive, decaying authentic future; `T_n~1/(64n²)` |
| S5 | `16^nπ/16` | `U_n+E[Cτ^(8n)]` | Every orbit time, including zero, exact identity |
| S6 | `z_n={16^nπ/16}` | `{U_n+E Y_n}` | Apply fractional part **after** expectation; sample-wise `{C}=0` is wrong |
| S7 | `W_B(h)=B^-1Σe(h16^nπ/16)` | `B^-1Σe(hU_n)e(h E Y_n)` | Nonlinearity: **not** `E[e(hY_n)]`; marked Poisson product gives an exact randomized lift |
| S8 | `Σ_h 2^-h|W_B(h)|²` / Oily all-mode | The same deterministic pair energy with each `e(hz_n)` replaced by its compensated Poisson mean; or exact pair `e(h(U_n-U_m+T_n-T_m))` | Generic positive norm never implies signed cancellation; all-mode decay OPEN |
| S9 | Basel `Σ_{n≥A} n^-2e(h16^nπ/16)` | `Σ_{n≥A} n^-2e(hU_n+ h E Y_n)` | Previous signed Tauberian equivalence, now source-complete; signed smallness OPEN |
| S10 | digits `⌊16^k {16^nπ/16}⌋` | `⌊16^k{U_n+E Y_n}⌋` | Noncommutation with E; at `16^kT_n<1`, exact source carry `1[{16^k{U_n}}+16^k E Y_n≥1]`; no sampled coin digit |
| S11 | Haar word counts/CDF/Wasserstein overlap | Cylinders evaluated on actual `z_n={U_n+E Y_n}` | **Do not** replace indicators, CDFs, absolute values, min, or floor by expectations of sampled indicators; exact edge case matters |
| S12 | 2-adic carrier `F(n)`, zero seed | Arithmetic `U_n=F(n)` in `Z₂` (paper premise in #646) | No π input; differentiate source-index/carry from real digit-reversal code |
| S13 | source return `J_(n,k)` and `7±4` | `J_(n,k)=(U_(n+16^k)-U_n)/16^k (mod 16)` | Already π-free, but SOURCE-presentation-dependent, as coboundary gauge demonstrates |
| S14 | two-time chiral phase `-e(255h z_n)` | `-e(h[U_(n+2)-U_n + E(Y_(n+2)-Y_n)])` | Original source phase `−1` calibrates, signed real Green difference is O(n^-3) |
| S15 | four-time chiral return `-e(h 255(16^q-1)z_n)` | `-e(hΔ_qΔ_2 U_n)exp(i2πh D_(n;q,2))`, `D=E[C τ^(8n)(1-τ^(8q))(1-τ^16)]` | The enormous time multiplier moved into rational lift; paid positive continuous correction O(n^-3) uniformly in q |
| S16 | original-chiral integral defect `π/16-\mathcal B_χ` | `E[C]-\mathcal B_χ` = exclusive-click probability from #649 | Strictly positive for this **chosen** source observer; not π-normality energy |
| S17 | *entire circle phase* from source coin | `e(hU_n) E_PPP∏(1+i2πh C_j τ_j^(8n)/λ)` | Exactly unbiased for each n, finite a.s., source variance `e^((2πh)²T_(2n)/λ)-1` |

### The exact coercivity gap

The source now supplies the **complete answer to target access**: no arithmetic π appears in the input to the random source program, finite polynomial part, Green moment, or real-time signed phase after Poisson-lifting. It does NOT supply a new **all-large-shell arithmetic estimate** bounding `Re W_B(1)` away from 1 or sending all `W_B(h)` to zero. The original zero-seeded phase and integer winding remain the hard objects. In particular, no finite randomized experiment can convert a still-open universal asymptotic statement into a proof simply by having an unbiased observable.

### A hostile demonstration of why the nonlinear slots are load-bearing

At n=0 the source coin C is an integer. For any integer h, `e(h C)=1` pathwise, so `E[e(h C)]=1`; but `e(h E C)=e(h π/16)` is nontrivial. Likewise `floor(16{C})=0` pathwise, but `floor(16π/16)=floor(π)=3`. Swapping the order of `E`, phase, and floor destroys the target even with a perfectly authenticated source. The marked Poisson product is an exact complex compensation, not permission to perform that illegal interchange.

### Deliberate exclusions

π also appears as a **geometric unit** in Fourier characters (`2π`), in arclength geometry, and in Archimedean normalization factors of the separate zeta/RH program. These are not additional unknown π arithmetic seeds. Substituting the BBP coin into the genuine zeta theta/Euler source would require an authenticated source morphism; no such morphism has been demonstrated. The atlas does not silently identify the BBP source with completed zeta or with a physical qubit field.

### S18 — Complete Oily all-harmonic π slot, without infinite deterministic harmonic enumeration

For each shell B, choose `H` with SUCC #644's `q_h=(h+1)/(3·2^h)`. Use **two independent entire-shell Poisson phase fields conditioned on H**, each generated from the same canonical π-free BBP coin (and internally shared across source times), with rate `λ_H=λ₀H²`. Their real complex cross product is an unbiased estimator of `Σ_(h≥1)q_h|W_B(h)|²`. Exact expected Poisson row count: `64λ₀/3`. Exact second moment ≤`(1+δ_B)²`, `δ_B=exp((2π)² T_(2B)/λ₀)-1`. This closes **finite expected-cost measurement access** to the complete existing normality detector, **not** its open decay estimate. See PS-09.
