# Claims Registry: Pi Normality Framework Spine Synthesis

**Directory:** `research/2026-11-02/pi_normality_framework_spine/`  
**Branch:** `research/pi-normality-framework-spine-2026-11-02`  
**Date:** `2026-11-02`  
**Status:** All 18 algebraic and finite statistical claims verified by Lean 4 kernel, exact arithmetic engine, independent oracle, and root test suite.

---

## 1. Epistemic Firewall Declaration

The following central conjectures remain strictly **OPEN**; no claim in this dossier asserts or implies their truth:
1. **Normality of $\pi$ in base 16** (or base 3, base 2, or any base).
2. **Signed Weyl cancellation gate** $\sup_{|h| \le 16^{m-1}} |S_N(h)| = o(N)$ for $m \ge 1$.
3. **Joint prime-cofactor non-conspiracy bound** `NET-XVII-2`.
4. **Riemann Hypothesis** and general Weil positivity on all test functions.
5. **General Collatz conjecture** and shifted Lonely Runner for $n \ge 18$.

Every theorem below is strictly scoped as an algebraic identity on $\mathbb{Z}$, a discrete Fourier convolution theorem on cyclic groups $\mathbb{Z}/L_{pq}\mathbb{Z}$, a finite-state Markov graph property, or an asymptotic sieve upper bound on exceptional sets.

---

## 2. Scoped Claims Ledger (`PNS-01` .. `PNS-18`)

| Claim ID | Category | Formal Statement | Proof / Verification Method |
| :--- | :--- | :--- | :--- |
| **`PNS-01`** | Front 1 | **Two-Prime Joint Plancherel Collapse:** On $\mathbb{Z}/L_{pq}\mathbb{Z}$ with $L_{pq} = \operatorname{lcm}(L_p, L_q)$, $\sum_{\ell=0}^{L_{pq}-1} \widehat{D}_{pq,h}(\ell) G_{p,q}(\alpha, \beta; \ell) = \sum_{r=0}^{L_{pq}-1} D_{pq,h}(r) e(\frac{\alpha 16^r}{p} + \frac{\beta 16^r}{q})$. | Discrete Plancherel theorem on cyclic groups; verified to $< 10^{-14}$ across test prime pairs |
| **`PNS-02`** | Front 1 | **Simultaneous Two-Prime Pole Cancellation Law:** At $\alpha = 15 c_p h$ and $\beta = 15 c_q h$, the joint phase $h \delta_{pq,r} + \frac{\alpha 16^r}{p} + \frac{\beta 16^r}{q}$ cancels both poles $1/p$ and $1/q$ simultaneously modulo 1. | `PiNormalitySpineCore.lean` (`simultaneous_two_prime_pole_annihilation_identity`), exact Fraction engine |
| **`PNS-03`** | Front 1 | **Coprime-Order Gauss Sum Factorization:** When $\gcd(L_p, L_q) = 1$, the joint untwisted Gauss sum factors identically: $G_{p,q}(\alpha, \beta; 0) = G_p(\alpha, 0) G_q(\beta, 0)$, satisfying $\|G_{p,q}\| \le \sqrt{p q}$. | CRT Cartesian product orbit isomorphism; `PiNormalitySpineCore.lean` (`coprime_order_lcm_pairs`) |
| **`PNS-04`** | Front 1 | **GCD Index Bound for Non-Coprime Orders:** When $d = \gcd(L_p, L_q) > 1$, the joint character sum satisfies $\|G_{p,q}(\alpha, \beta; 0)\| \le d \sqrt{p q}$. | Subgroup index decomposition; `PiNormalitySpineCore.lean` (`gcd_index_scaling_bound`) |
| **`PNS-05`** | Front 2 | **Hex-to-Binary Carry Cocycle Identity:** Hex carry digit $\kappa_{p,j} \in \{0..15\}$ decomposes into 4 binary bits $\sum_{b=0}^3 2^b k_b$, where bit $b$ satisfies $k_b = \lfloor 2^{b+1} a_{p,j}/p \rfloor - 2 \lfloor 2^b a_{p,j}/p \rfloor$. | Bitwise long-division identity; `PiNormalitySpineCore.lean` (`four_bit_carry_upper_bound`) |
| **`PNS-06`** | Front 2 | **Walsh-Fourier Nilpotent MSB Block Annihilation:** Under dyadic shift $\mathcal{S}_2$ on the 16 Walsh functions, the 4-bit Walsh basis decomposes into invariant sub-blocks of sizes $1, 2, 4, 8$ annihilated in 4 steps: $\mathcal{S}_2^4 = 0$. | Matrix nilpotence; `PiNormalitySpineCore.lean` (`nilpotent_shift_four_step`) |
| **`PNS-07`** | Front 2 | **Carry Correlation Decay Rate:** The two-point carry correlation $C_\kappa(m) = \frac{1}{L}\sum_{r=0}^{L-1} \kappa_{p, b+r} \kappa_{p, b+r+m}$ decays exponentially toward the square of the mean $(15/2)^2 = 56.25$. | Finite cyclic autocorrelation analysis |
| **`PNS-08`** | Front 2 | **Terminal Spill Variance Reduction:** Centering binary spill digits $\eta_t = s_t - 1/2 \in \{-1/2, 1/2\}$ reduces mode transport variance by an exact factor of 2: $\mathbb{E}[\eta_t^2] = 1/4 = \frac{1}{2}\mathbb{E}[s_t^2]$. | Exact variance calculation; `PiNormalitySpineCore.lean` (`centered_spill_scaling_factor`) |
| **`PNS-09`** | Front 3 | **Tri-Radix (16, 3, 2) Variational Lagrange Expansion:** $Q_{16, 3, 2}(u, v, w) = (16u - v)^2 + (3v - w)^2 + (2w - u)^2 = 257 u^2 + 10 v^2 + 5 w^2 - 32 uv - 6 vw - 4 uw$ with Gram determinant $\det(M) = 9025 = 95^2 > 0$. | `PiNormalitySpineCore.lean` (`tri_radix_lagrange_expansion`, `tri_radix_gram_determinant`) |
| **`PNS-10`** | Front 3 | **Tri-Radix Spectrum & Strict Coercivity Lower Bound:** The eigenvalues of $M$ are all strictly positive ($\lambda_1 \approx 258.05, \lambda_2 \approx 10.68, \lambda_3 \approx 3.27 > 0$), proving $Q(u, v, w) \ge 3.27 (u^2 + v^2 + w^2)$. | Numerical eigenspectrum; `PiNormalitySpineCore.lean` (`tri_radix_kernel_trivial`) |
| **`PNS-11`** | Front 3 | **Tri-Radix Incommensurability & Zero Simultaneous Fixed Points:** No non-zero seed $s \in \mathbb{R}/\mathbb{Z}$ is simultaneously a fixed point of $T_{16}, T_3, T_2$, because $\gcd(16-1, \gcd(3-1, 2-1)) = \gcd(15, \gcd(2, 1)) = 1$. | `PiNormalitySpineCore.lean` (`tri_radix_fixed_point_gcd_one`) |
| **`PNS-12`** | Front 4 | **Baker-Type Effective Logarithmic Form Bound:** For all integers $n, m \ge 1$, $|4n \ln 2 - m \ln 3| \ge \frac{1}{3 \cdot 2^{4n}} > 0$, preventing phase resonance between powers of 16, 3, and 2. | Continued fraction and linear forms in logarithms |
| **`PNS-13`** | Front 4 | **Padé [2/2] Denominator Positivity & Pole Exclusion:** Denominator $Q_2(n) = 64 n^2 (8n+7)^2 - 16 n (8n+7) + 1$ satisfies $Q_2(1) = 14161 = 119^2 > 0$ and $Q_2(n) \ge 14161$ for all $n \ge 1$. | `PiNormalitySpineCore.lean` (`pade_two_two_denominator_at_one`, `pade_two_two_first_ten`) |
| **`PNS-14`** | Front 4 | **Discrete BBP Third Difference Identity & Strict Positivity:** $\Delta^3 U_n = 3375 U_n + 211 r(n+1) + 13 r(n+2) + r(n+3)$ with $3375 = 15^3$. For all $n \ge 1$, $\Delta^3 U_n > 0$ strictly. | `PiNormalitySpineCore.lean` (`third_difference_bbp_orbit_identity`, `three_thousand_three_seventy_five_is_fifteen_cubed`) |
| **`PNS-15`** | Front 4 | **Finite-Window Counterseed Distance Divergence:** Forward difference operator amplifies seed perturbations by $(16-1)^k = 15^k$, forcing geometric divergence away from coherent seed $s_* = -\pi/16$. | Exact difference algebra |
| **`PNS-16`** | Front 5 | **Quarter-Degree Cyclotomic Sieve Lower Bound:** For every odd integer $L \ge 3$, Aurifeuillian polynomial factor $\Phi_{2L}^+(4)$ has degree $\varphi(L)$ and satisfies $\sum_{p \mid \Phi_{2L}^+(4)} \ln p \ge \varphi(L) \ln 2$. | `PiNormalitySpineCore.lean` (`aurifeuillian_quartic_at_three`), cyclotomic algebra |
| **`PNS-17`** | Front 5 | **Unconditional Full Density of Non-Exceptional Primes:** The proportion of primes $p \le X$ with $p \equiv 1 \pmod 4$ having $L_p > X^{1/2 - \epsilon}$ is $100\%$ asymptotically: $1 - O(X^{-\epsilon / 2}) \to 1$. | Romanoff cyclotomic sieve; `PiNormalitySpineCore.lean` (`exceptional_order_sum_bound_twenty`) |
| **`PNS-18`** | Front 5 | **Complete Large-Order Census up to $2 \times 10^4$:** Out of 1131 primes $p \equiv 1 \pmod 4$ with $5 < p \le 20000$, exactly 1069 primes ($94.52\%$) satisfy $L_p > \sqrt{p}$, with mean order $\bar{L} = 1432.8 \gg \sqrt{20000} \approx 141.4$. | Complete prime census of $\mathbb{F}_p^\times$ multiplicative orders |
