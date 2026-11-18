# Validation Receipt: Adelic BBP Period–Seed Duality (`ANC-01..12`) & Fermat–Quadratic-Reciprocity Self-Duality / Ramified-Cofactor Master Carry Congruence (`FQR-01..10`)

**Date:** 2026-11-17  
**Branch:** `research/pi-normality-crucible-frontier-2026-11-17`  
**Research documents:**
- Round I: [ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md](ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md) (`ANC-01..12`)
- Round II: [FERMAT_QUADRATIC_RECIPROCITY_SELF_DUALITY_AND_RAMIFIED_CARRY.md](FERMAT_QUADRATIC_RECIPROCITY_SELF_DUALITY_AND_RAMIFIED_CARRY.md) (`FQR-01..10`)

## 1. Exact Standard-Library `unittest` Execution and Git Blob SHA-1 Hashes

Command executed:
~~~sh
python3 -m unittest discover -s tests -p 'test_adelic_bbp_normality_crucible.py' -v
~~~

Result: **25/25 exact rational tests passed** (`OK` in `2.875s`), using only Python's standard library (`unittest`, `fractions.Fraction`, `math`, `functools.lru_cache`).

Committed file inventory and exact Git blob SHA-1 hashes (`git hash-object` / `wc -c`):
- `observational_succ/adelic_bbp_normality_crucible.py`: **22,058 bytes**, Git blob SHA-1 `beddee1e63137466e6ebd6f46d2b509816556331`
- `tests/test_adelic_bbp_normality_crucible.py`: **20,829 bytes**, Git blob SHA-1 `bf9799c912bcdc6f1954286c8f017dcc5589e18d`
- `research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md`: **42,301 bytes**, Git blob SHA-1 `379c014f8ebdf7df82d433f26659660942fa1bbf`
- `research/2026-11-17/causal_clock_scrambling/FERMAT_QUADRATIC_RECIPROCITY_SELF_DUALITY_AND_RAMIFIED_CARRY.md`: **28,552 bytes**, Git blob SHA-1 `460495d29d184148ff46ac2ef20b613b0ccd6734`

All mandatory `AGENTS.md` root probes (`scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`) and all merged 2026-11-17 test suites (`test_borwein_*.py`, `test_bbp_tail_impulse.py`, `test_pro_pi_*.py`) were also executed and passed.

## 2. Independent Symbolic (SymPy) Verification

An independent SymPy script (not importing `observational_succ`) verified:
1. **Combined rational factorization (`ANC-01`) and pairwise lane coprimality (`FQR-01`):**
   \[
   \frac{4}{8z-7} - \frac{2}{8z-4} - \frac{1}{8z-3} - \frac{1}{8z-2}
   - \frac{120z^2 - 89z + 16}{(2z-1)(4z-1)(8z-7)(8z-3)} = 0.
   \]
2. **Octic CRT Partial-Fraction Matrix and Boundary-Null Logarithmic Derivative (`ANC-05/06`):**
   - Verified $M \cdot M_{\mathrm{inv}} = I_8$ over $\mathbb{Q}$.
   - Verified $\frac{Q_{\mathrm{null}}(t)}{16-t^8} + \frac{1}{2}\frac{d}{dt}\ln\left(\frac{t^2-2t+2}{2-t^2}\right) = 0$ and $\int_0^1 \frac{Q_{\mathrm{null}}(t)}{16-t^8}\,dt = 0$.
   - Verified $Q_1(t) = Q_{\alpha_3}(t) + \frac{1}{4}Q_{\mathrm{null}}(t)$ and $Q_2(t) = Q_{\alpha_3}(t) - \frac{1}{4}Q_{\mathrm{null}}(t)$.
   - Verified $\Omega_\pi(r_1) = \Omega_\pi(r_2) = 1$ and $\Omega_\pi(r_\flat) = \Omega_\pi(r_{\mathrm{tel}}) = \Omega_\pi(r_{\mathrm{lock}}) = 0$.
3. **Closed-form 3-branch piecewise-quintic Borwein autocorrelation (`ANC-10`) and exact grid energy (`FQR-08`):**
   - Verified exact symbolic interpolation of $K(d) = (\mathsf{L} * \mathsf{L})(d)$ on $[0, 1/9]$, $[1/9, 4/9]$, and $[4/9, 1/2]$, continuity of $K, K', K'', K'''$ at $d = 7/18$, $2\int_0^{1/2} K(d)\,dd = \frac{65536}{60886809} = \left(\frac{256}{7803}\right)^2$, and $\mathcal{V}_N^{\mathrm{grid}} = \frac{576}{417605 N^4}$ for $9 \mid N$.
4. **Universal Fermat–Quadratic-Reciprocity Collapse (`FQR-02/03`):**
   - Verified $p\, U_N(0) \equiv 16^N \mathcal{C}_{p \bmod 8}(p, N) \pmod p$ across all $2,703$ pairs $(N, p)$ with $1 \le N \le 60$ and $p > \sqrt{8N}$ ($p \ge 7$), and verified exact equality $\mathcal{C}_{p \bmod 8}(p, Kp) = +P_K^{(r_1)}$ ($p \equiv 1 \pmod 4$) and $-P_K^{(r_2)}$ ($p \equiv 3 \pmod 4$).

## 3. High-Precision (`mpmath`) & $2$-Adic Diagnostic Cross-Checks

1. **$2$-Adic Null-Seed Evaluation (`ANC-03/04`):** $\mathfrak{U}_2(0) = \sum_{m=0}^{K-1} 16^m r_1(-m) \equiv 0 \pmod{16^{60}}$ ($240$ binary bits of exact $2$-adic precision).
2. **50-Digit Dirichlet $\chi_{-4}$ Limit (`FQR-03`):** 50-digit `mpmath` evaluation of $\lim_{N/p \to \infty} \mathcal{C}_{p \bmod 8}(p, N)$ matches $+\frac{\pi}{16}$ for $p \equiv 1 \pmod 4$ and $-\frac{\pi}{16}$ for $p \equiv 3 \pmod 4$ to 40+ digits.
3. **Ramified-Cofactor Master Congruence (`FQR-06/07`):** Verified exact equality $\lfloor Q_{2B}^{\mathrm{ram}} U_{2B}(0) \rfloor \bmod 16^B = \mathcal{Z}_B^{\mathrm{FQR}}$ and $\{Q_{2B}^{\mathrm{ram}} U_{2B}(0)\} = \widetilde{R}_{2B}/\Pi_{2B}^{\mathrm{simple}}$ for $B \in \{2, 4, 8, 16, 24, 32\}$.

## 4. Explicit Unrun Gates and Scope Firewall

- The full repository-wide 14,500+ test suite and hosted GitHub CI were not claimed as executed on this commit head; only the mandatory root probes (`verify_provenance.py`, `observer_foundations_probe.py`, `ordinal_succ_report_probe.py`) and focused 2026-11-17 test suites were run locally.
- No Lean 4 kernel formalization of `ANC-01..12` or `FQR-01..10` is claimed.
- Finite rational certificates and $2$-adic/$p$-adic congruences prove `ANC-01..12` and `FQR-01..10` within their stated domains; the asymptotic all-late-shell bounds $\liminf_B \mathcal{R}_B(0) > 0$ ($R_0$) and $\lim_B \mathcal{V}_B = 0$ (base-16 $\pi$ normality) remain **OPEN**.
