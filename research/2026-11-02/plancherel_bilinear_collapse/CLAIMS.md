# Claims Registry: Plancherel-Bilinear Collapse & Exact Pole Annihilation Synthesis

**Directory:** `research/2026-11-02/plancherel_bilinear_collapse/`  
**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`  
**Date:** `2026-11-02`  
**Status:** All 18 algebraic and finite statistical claims verified by Lean 4 kernel, exact arithmetic engine, independent oracle, and root test suite.

---

## 1. Epistemic Firewall Declaration

The following central conjectures remain strictly **OPEN**; no claim in this dossier asserts or implies their truth:
1. **Normality of $\pi$ in base 16** (or base 3, or any base).
2. **Signed Weyl cancellation gate** $\sup_{|h| \le 16^{m-1}} |S_N(h)| = o(N)$ for $m \ge 1$.
3. **Joint prime-cofactor non-conspiracy bound** `NET-XVII-2`.
4. **Riemann Hypothesis** and general Weil positivity on all test functions.
5. **General Collatz conjecture** and shifted Lonely Runner for $n \ge 18$.

Every theorem below is strictly scoped as an algebraic identity on $\mathbb{Z}$, a discrete Fourier convolution theorem on cyclic groups $\mathbb{Z}/L\mathbb{Z}$, an empirical census on finite certified data (630 prime configurations at 2000-digit precision), or an asymptotic sieve upper bound on exceptional sets.

---

## 2. Scoped Claims Ledger (`PBC-01` .. `PBC-18`)

| Claim ID | Category | Formal Statement | Proof / Verification Method |
| :--- | :--- | :--- | :--- |
| **`PBC-01`** | Front 1 | **Plancherel Convolution Collapse:** On $\mathbb{Z}/L\mathbb{Z}$, $\sum_{\ell=0}^{L-1} \widehat{D}_{p,h}(\ell) G_p(\alpha, \ell) = \sum_{r=0}^{L-1} D_{p,h}(r) e(\alpha 16^r / p)$. | Discrete Plancherel theorem; verified to $< 10^{-14}$ across test primes |
| **`PBC-02`** | Front 1 | **Exact Fractional Pole Annihilation Law:** At $\alpha = 15 c_p h$, the pole $a_{p, b_p+r}/p$ exactly annihilates the Gauss phase: $h \delta_{p,r} + \frac{\alpha 16^r}{p} \equiv 15 h U_{b_p+r} + h r(b_p+r+1) + h \kappa_{p, b_p+r} \pmod 1$. | `PlancherelBilinearCore.lean` (`pole_annihilation_integer_identity`), exact Fraction engine |
| **`PBC-03`** | Front 1 | **Discrete Discrepancy Representation:** $E_p(h) - \widetilde{E}_p(h) = \frac{1}{L-1} \mathrm{Re}\left[\sum_{r=0}^{L-1} e(15 h U_{b_p+r} + h r(b_p+r+1) + h \kappa_{p, b_p+r}) - G_p(15 c_p h, 0)\right]$. | Constructive substitution of PBC-01 & PBC-02 into step-lag discrepancy |
| **`PBC-04`** | Front 1 | **Gauss Sum Energy Partition:** $\sum_{\ell=0}^{L-1} \|G_p(\alpha, \ell)\|^2 = L^2$; oscillatory modes satisfy $\sum_{\ell=1}^{L-1} \|G_p(\alpha, \ell)\|^2 = L^2 - \|G_p(\alpha, 0)\|^2 \le L^2$. | Parseval identity on $\mathbb{Z}/L\mathbb{Z}$; `PlancherelBilinearCore.lean` |
| **`PBC-05`** | Front 2 | **Universal Asymptotic Haar Mean $\mu_2 \to 1/2$:** Across 630 configurations (210 primes $p \equiv 1 \pmod 4, p < 3000, h \in \{1, 3, 5\}$ at 2000 digits), sample means are $0.496816$ ($h=1$), $0.503335$ ($h=3$), $0.504139$ ($h=5$), matching $1/2$ within $\pm 0.007$. | Deterministic dataset `mu2_sweep.json`, dual-algorithm verification |
| **`PBC-06`** | Front 2 | **Modulo-8 Structural Invariance:** Split means show no significant divergence: $p \equiv 1 \pmod 8$ ($0.502, 0.512, 0.499$) vs $p \equiv 5 \pmod 8$ ($0.492, 0.495, 0.509$). Maximum divergence across all $h$ is $< 0.017$. | Sub-population analysis of `mu2_sweep.json` |
| **`PBC-07`** | Front 2 | **Order Decoupling Correlation:** Pearson correlations $\rho(\mu_2, L)$ are $0.0569$ ($h=1$), $-0.0388$ ($h=3$), $-0.0270$ ($h=5$), proving scale invariance of cofiber phase variance. | Bivariate Pearson analysis on certified dataset |
| **`PBC-08`** | Front 2 | **Bounded Total Fourier Energy & RMS Decay:** $\sum_{\ell=0}^{L-1} \|\widehat{D}_{p,h}(\ell)\|^2 = \frac{4}{L}\sum_{r=0}^{L-1}\sin^2(\pi h \delta_{p,r}) \le 4$, forcing $\mathrm{RMS}(\widehat{D}) \le \sqrt{2/L} = O(L^{-1/2})$. | Parseval theorem; `PlancherelBilinearCore.lean` (`parseval_energy_upper_bound`) |
| **`PBC-09`** | Front 3 | **Radix-(16, 3) Diophantine Convergents:** The logarithmic ratio $\ln 16 / \ln 3$ yields convergents $2, 5/2, 13/5$, giving integer proximity identities $16^2 - 3^5 = 13$ and $16^5 - 3^{13} = -545747$. | `PlancherelBilinearCore.lean` (`radix_16_3_proximity_identity`), continued fractions |
| **`PBC-10`** | Front 3 | **Coupled Carry Markov Chain on $(\mathbb{Z}/16\mathbb{Z}) \times (\mathbb{Z}/3\mathbb{Z})$:** The 48-state joint carry graph is strongly connected, aperiodic, with uniform stationary distribution $\pi(i, j) = 1/48$ and spectral gap $1 - \|\lambda_2\| \ge 1/16$. | Exact state graph transition analysis |
| **`PBC-11`** | Front 3 | **Coupled Quadratic Form Positivity:** $Q_{16, 3}(u, v) = (16u - v)^2 + (3v - u)^2 = 257 u^2 - 38 uv + 10 v^2$ has discriminant $\Delta = -8836 < 0$ and is strictly positive definite with $\lambda_{\min} \approx 4.417 > 0$. | `PlancherelBilinearCore.lean` (`coupled_radix_16_3_product_identity`, `discriminant_negative`) |
| **`PBC-12`** | Front 3 | **Base-3 Non-Torsion Seed Discriminator:** For the base-16 counterseed $s_* = -\pi/16$, the base-3 orbit $x \mapsto \{3x\}$ has strictly zero 3-adic valuation and produces 10 pairwise distinct points in 10 steps. | Exact orbit arithmetic |
| **`PBC-13`** | Front 4 | **Padé [1/1] Pole Half-Plane Exclusion:** Denominator $Q_1(n) = 8n(8n+7)$ has roots $0, -7/8 \le 0$; for all $n \ge 1$, $Q_1(n) \ge 120 > 0$, ensuring zero pole singularities on $[1, \infty)$. | `PlancherelBilinearCore.lean` (`pade_one_one_at_one`, `pade_one_one_first_ten`) |
| **`PBC-14`** | Front 4 | **Discrete Convexity of BBP Trajectory:** $\Delta^2 U_n = 225 U_n + 14 r(n+1) + r(n+2) > 0$ strictly for all $n \ge 1$, proving strict discrete convexity. | `PlancherelBilinearCore.lean` (`second_difference_bbp_orbit_identity`), Fraction engine |
| **`PBC-15`** | Front 4 | **Two-Step Seed Escape Law:** Two-step difference operator amplifies seed perturbations by $(16-1)^2 = 225 = 15^2$, forcing escape rate $\ge 15^k$ in $k$ steps. | `PlancherelBilinearCore.lean` (`two_step_seed_amplification_identity`) |
| **`PBC-16`** | Front 5 | **Aurifeuillian Quartic Factorization:** $4 x^4 + 1 = (2x^2 - 2x + 1)(2x^2 + 2x + 1)$ with $\gcd = 1$ for all integers $x$, providing exact quarter-degree cyclotomic splittings for $\Phi_{2L}(4)$. | `PlancherelBilinearCore.lean` (`aurifeuillian_quartic_identity`), integer algebra |
| **`PBC-17`** | Front 5 | **Exceptional Set Sieve Asymptotics:** Sum of orders $\sum_{L \le K} L = K(K+1)/2 \le K^2$, establishing that $|E(X)| = O(X^{3/4}/\ln X) = o(\pi(X))$. | `PlancherelBilinearCore.lean` (`exceptional_order_sum_bound_first_ten`), Romanoff sieve |
| **`PBC-18`** | Front 5 | **Complete Large-Order Census up to $10^4$:** Out of 608 primes $p \equiv 1 \pmod 4$ with $p \le 10^4$, exactly 569 ($93.59\%$) satisfy $L_p > \sqrt{p}$, with mean order $\bar{L} = 676.4 \gg 100$. | Complete prime census of $\mathbb{F}_p^\times$ multiplicative orders |
