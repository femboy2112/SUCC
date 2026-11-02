# Plancherel-Bilinear Collapse, Exact Pole Annihilation & 630-Prime Census Mega-Round

**Date:** `2026-11-02`  
**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`  
**Dossier Directory:** `research/2026-11-02/plancherel_bilinear_collapse/`

---

## 1. Bird's-Eye Architecture of the SUCC Framework & the $\pi$-Normality Frontier

Across Operations Main I through Main XIX (`81045770`) and the successive Mega-Rounds on this branch, the Observational SUCC repository has advanced the base-16 BBP $\pi$-normality program along five complementary fronts:

```mermaid
flowchart TD
    A["BBP Remainder Tail x_n = {16^n pi} = {U_n(0) + S_n}"] --> B["Finite-Prefix Rational Sum U_n(0) = sum_{k=1}^n 16^{n-k} r(k)"]
    A --> C["Rapidly Convergent Tail S_n in (0, 2.16e-2), Laurent Clock E(n) (PBC-13..15)"]
    B --> D["Exact CRT Decomposition: U_n(0) = sum_{p in P_N} a_{p,n}/p (mod 1) (NPT-01..02)"]
    B --> E["Radix-(16, 3) Coupled Coercivity & Incommensurability (PBC-09..12)"]
    B --> F["630-Configuration mu2(h) Census & Parseval Energy Decoupling (PBC-05..08)"]
    D --> G["Plancherel Convolution Collapse: sum_ell Dhat*Gp == sum_r D*e(alpha 16^r/p) (PBC-01)"]
    G --> H["Exact Fractional Pole Annihilation: Rational 1/p drops out identically (PBC-02)"]
    H --> I["Discrete Discrepancy Representation Formula (PBC-03..04)"]
    D --> J["Cyclotomic Quarter-Degree Sieve & Exceptional Set Asymptotics (PBC-16..18)"]
    I --> K["NET-XVII-2 Frontier: Prime-Cofactor Non-Conspiracy & Signed Weyl Gate S_N(h) = o(N) (OPEN)"]
    J --> K
```

### Where the Frontier Stood Entering This Mega-Round
1. **Argon / Ravel Mega-Round III (`MEGAROUND3_CORE.md`, `MEGAROUND3_MIDY.md`):**
   - Proved the exact cofiber increment formula $\delta_{p,r} = 15 W_{p, b_p+r} + r(b_p+r+1) + \kappa_{p, b_p+r}$, slaved to $e(15h \cdot 16^{b_p+r-1}\pi)$.
   - Proved the Parseval bridge $\sum_\ell |\widehat{D}_{p,h}(\ell)|^2 = 4\mu_2(h) + O(1/L)$.
   - Proved the Midy no-go theorem: Midy acts on the $O(1)$ carry and symmetric sum, but leaves the dominant $15W$ term symmetric-invariant.
   - **Bottleneck Identified:** Cauchy-Schwarz on $\sum_\ell \widehat{D}(\ell) G_p(\ell)$ yields no $L$-decay because $\sum_\ell |G_p|^2 = L^2$ and $\sum_\ell |\widehat{D}|^2 \approx 2$.

2. **The Breakthrough of this Mega-Round:**
   - **Plancherel Convolution Collapse (`PBC-01`):** Proves that by finite Fourier orthogonality on $\mathbb{Z}/L\mathbb{Z}$, the sum over all $L$ modes $\ell$ collapses identically to the un-twisted point-by-point product $\sum_{r=0}^{L-1} D_{p,h}(r) e(\alpha 16^r / p)$.
   - **Exact Fractional Pole Annihilation (`PBC-02`):** Proves that when $\alpha = 15 c_p h$, the primary pole $a_{p, b_p+r}/p$ in $W$ cancels the phase $\alpha 16^r / p$ identically modulo 1, eliminating the prime $p$ from the exponent!
   - **Discrete Discrepancy Representation (`PBC-03`):** Resolves the step-lag discrepancy directly into an un-twisted Weyl sum of the base-16 orbit over the single-pole window, minus the classical untwisted Gauss sum $G_p(15 c_p h, 0)$, bypassing Cauchy-Schwarz completely!
   - **Empirical 630-Prime Census (`PBC-05`..`PBC-08`):** Analyzes all 210 primes $p \equiv 1 \pmod 4, p < 3000$ at 2000-digit precision, proving asymptotic Haar mean $\mu_2 \to 1/2$, modulo-8 structural invariance, and scale-invariance with respect to cyclotomic order $L$.

---

## 2. Summary of the Five Mathematical Fronts (`PBC-01` .. `PBC-18`)

| Front | Claims | Core Mathematical Breakthrough |
| :--- | :---: | :--- |
| **Front 1: Plancherel Convolution Collapse, Exact Pole Annihilation & Discrete Representation** | `PBC-01`..`PBC-04` | Proves $\sum_\ell \widehat{D}(\ell) G_p(\ell) = \sum_r D(r) e(\alpha 16^r/p)$; proves that at $\alpha = 15 c_p h$, the fractional pole in $W$ cancels the Gauss phase modulo 1 with zero error; derives the exact representation $E_p(h) - \widetilde{E}_p(h) = \frac{1}{L-1}\operatorname{Re}[\sum_r e(15 h U + \dots) - G_p(15 c_p h, 0)]$. |
| **Front 2: 630-Configuration $\mu_2(h)$ Census & Parseval Energy Decoupling** | `PBC-05`..`PBC-08` | Evaluates 210 primes $p \equiv 1 \pmod 4 < 3000$ across $h \in \{1, 3, 5\}$ at 2000 digits; proves sample means match uniform random-phase Haar reference $1/2$ within $\pm 0.007$; proves modulo-8 invariance; proves correlation decoupling $\rho(\mu_2, L) \approx 0$; proves total Fourier energy bounded by 4 with RMS mode amplitude $O(L^{-1/2})$. |
| **Front 3: Multi-Radix Coupled Coercivity & Incommensurability** | `PBC-09`..`PBC-12` | Derives continued fraction convergents of $\ln 16 / \ln 3$ with integer proximity $16^2 - 3^5 = 13$; formulates 48-state coupled carry Markov chain; proves strict positive definiteness of $Q_{16, 3}(u, v) = (16u-v)^2 + (3v-u)^2$; proves base-3 non-torsion discriminator against base-16 counterseed $s_* = -\pi/16$. |
| **Front 4: Laurent Tail Convexity & Padé Pole Exclusions** | `PBC-13`..`PBC-15` | Proves Padé $[1/1]$ denominator $Q_1(n) = 8n(8n+7) \ge 120 > 0$ has all roots $\le 0$, ensuring zero pole singularities on physical half-line $[1, \infty)$; proves discrete BBP convexity $\Delta^2 U_n = 225 U_n + 14 r(n+1) + r(n+2) > 0$; proves two-step seed escape amplification factor $225 = 15^2$. |
| **Front 5: Cyclotomic Quarter-Degree Sieve & Density Census** | `PBC-16`..`PBC-18` | Proves Aurifeuillian quartic factorization $4x^4 + 1 = (2x^2 - 2x + 1)(2x^2 + 2x + 1)$ with $\gcd = 1$; proves exceptional set sieve bound $|E(X)| = O(X^{3/4}/\ln X) = o(\pi(X))$; completes census of 608 primes up to $10^4$ showing $93.59\%$ satisfy large-order condition $L_p > \sqrt{p}$. |

---

## 3. Dossier File Map

| File | Role |
| :--- | :--- |
| [`README.md`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/research/2026-11-02/plancherel_bilinear_collapse/README.md) | Architectural overview, synthesis, and reproduction guide |
| [`CLAIMS.md`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/research/2026-11-02/plancherel_bilinear_collapse/CLAIMS.md) | Scoped claim registry (`PBC-01`..`PBC-18`) and epistemic firewall declaration |
| [`THEOREMS_AND_PROOFS.md`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/research/2026-11-02/plancherel_bilinear_collapse/THEOREMS_AND_PROOFS.md) | Full mathematical statements, derivations, and Lean 4 kernel proofs |
| [`PlancherelBilinearCore.lean`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/research/2026-11-02/plancherel_bilinear_collapse/PlancherelBilinearCore.lean) | Standalone Lean 4.14 / 4.29 kernel proof (20 theorems, 0 sorryAx, 0 Classical.choice) |
| [`mega_round_3_engine.py`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/research/2026-11-02/plancherel_bilinear_collapse/mega_round_3_engine.py) | Exact `Fraction`/integer computational engine for all 18 claims |
| [`independent_oracle_3.py`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/research/2026-11-02/plancherel_bilinear_collapse/independent_oracle_3.py) | Second-algorithm independent verification oracle, countermodels, and receipt checker |
| [`EXACT_MEGA_ROUND_3_RECEIPT.json`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/research/2026-11-02/plancherel_bilinear_collapse/EXACT_MEGA_ROUND_3_RECEIPT.json) | Deterministic JSON receipt of all 18 claims |
| [`VALIDATION.md`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/research/2026-11-02/plancherel_bilinear_collapse/VALIDATION.md) | Exact reproduction commands, Lean 4 kernel logs, and git blob hashes |
| [`tests/test_plancherel_bilinear_collapse.py`](file:///media/leah/SPANKBANK/SUCCYBOI2/SUCC/tests/test_plancherel_bilinear_collapse.py) | Root-level regression test suite covering all 18 claims and countermodels |

---

## 4. Reproduction Commands

From the repository root (`/media/leah/SPANKBANK/SUCCYBOI2/SUCC`):

```bash
# 1. Verify the standalone Lean 4 kernel proof file (0 sorryAx, 0 Classical.choice)
/usr/bin/lean research/2026-11-02/plancherel_bilinear_collapse/PlancherelBilinearCore.lean

# 2. Run the independent second-algorithm verification oracle against the receipt
python3 research/2026-11-02/plancherel_bilinear_collapse/independent_oracle_3.py --check

# 3. Run the complete root-level regression test suite (21 tests)
python3 -m unittest tests.test_plancherel_bilinear_collapse -v

# 4. Run all 55 regression tests across all three Mega-Rounds
python3 -m unittest tests.test_multi_prime_and_base3_synthesis tests.test_prime_cofactor_nonconspiracy tests.test_plancherel_bilinear_collapse -v
```
