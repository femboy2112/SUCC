# Validation Receipt: Adelic BBP Period–Seed Duality, Iwasawa $2$-Adic Null-Seed Coherence, Octic CRT Period Quotient, and Parseval–Cauchy–Schwarz Normality Crucible

**Date:** 2026-11-17  
**Branch:** `research/pi-normality-crucible-frontier-2026-11-17`  
**Research document:** [ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md](ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md)

## 1. Exact Standard-Library `unittest` Execution and Git Blob SHA-1 Hashes

Command executed:
~~~sh
python3 -m unittest discover -s tests -p 'test_adelic_bbp_normality_crucible.py' -v
~~~

Result: **15/15 exact rational tests passed** (`OK` in `2.833s`), using only Python's standard library (`unittest`, `fractions.Fraction`, `math`, `functools.lru_cache`).

Committed file inventory and exact Git blob SHA-1 hashes (`git hash-object` / `wc -c`):
- `observational_succ/adelic_bbp_normality_crucible.py`: **16,919 bytes**, Git blob SHA-1 `ad61a1fd4ac15820e81a0a8aef8fd6101434bb0b`
- `tests/test_adelic_bbp_normality_crucible.py`: **13,951 bytes**, Git blob SHA-1 `8072237302a3042a74b1ad29d994fdf229d90b22`
- `research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md`: **42,301 bytes**, Git blob SHA-1 `379c014f8ebdf7df82d433f26659660942fa1bbf`

All 24 prior Borwein tests (`test_borwein_bbp_sweep.py` and `test_borwein_quantitative_certificate.py`) and all mandatory `AGENTS.md` root probes (`scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`) were also executed and passed.

## 2. Independent Symbolic (SymPy) Verification

An independent SymPy script (not importing `observational_succ`) verified:
1. **Combined rational factorization (`ANC-01`):**
   \[
   \frac{4}{8z-7} - \frac{2}{8z-4} - \frac{1}{8z-3} - \frac{1}{8z-2}
   - \frac{120z^2 - 89z + 16}{(2z-1)(4z-1)(8z-7)(8z-3)} = 0.
   \]
2. **Octic CRT Partial-Fraction Matrix and Boundary-Null Logarithmic Derivative (`ANC-05/06`):**
   - Verified $M \cdot M_{\mathrm{inv}} = I_8$ over $\mathbb{Q}$.
   - Verified $\frac{Q_{\mathrm{null}}(t)}{16-t^8} + \frac{1}{2}\frac{d}{dt}\ln\left(\frac{t^2-2t+2}{2-t^2}\right) = 0$ and $\int_0^1 \frac{Q_{\mathrm{null}}(t)}{16-t^8}\,dt = 0$.
   - Verified $Q_1(t) = Q_{\alpha_3}(t) + \frac{1}{4}Q_{\mathrm{null}}(t)$ and $Q_2(t) = Q_{\alpha_3}(t) - \frac{1}{4}Q_{\mathrm{null}}(t)$.
   - Verified $\Omega_\pi(r_1) = \Omega_\pi(r_2) = 1$ and $\Omega_\pi(r_\flat) = \Omega_\pi(r_{\mathrm{tel}}) = \Omega_\pi(r_{\mathrm{lock}}) = 0$.
3. **Closed-form 3-branch piecewise-quintic Borwein autocorrelation (`ANC-10`):**
   - Verified exact symbolic interpolation of $K(d) = (\mathsf{L} * \mathsf{L})(d)$ on $[0, 1/9]$, $[1/9, 4/9]$, and $[4/9, 1/2]$, continuity of $K, K', K'', K'''$ at $d = 7/18$ (confirming $7/18$ is not a breakpoint), and $2\int_0^{1/2} K(d)\,dd = \frac{65536}{60886809} = \left(\frac{256}{7803}\right)^2$.

## 3. High-Precision (`mpmath`) & $2$-Adic Diagnostic Cross-Checks

1. **$2$-Adic Null-Seed Evaluation (`ANC-03/04`):** $\mathfrak{U}_2(0) = \sum_{m=0}^{K-1} 16^m r_1(-m) \equiv 0 \pmod{16^{60}}$ ($240$ binary bits of exact $2$-adic precision), while the five non-root-of-unity octic channels $\alpha_1, \alpha_2, \alpha_4, \beta_1+\beta_2, \beta_3+\beta_4$ all evaluate to nonzero $2$-adic units modulo $16^{13}$.
2. **Parseval Identity at $d = 0$ (`ANC-10`):** 50-digit `mpmath` summation of $\ell_0^2 + 2\sum_{h=1}^\infty |\widehat{\mathsf{L}}(h)|^2$ matches the exact rational $K(0) = \frac{8192}{3758445} \approx 0.00217962481824$.
3. **Asymptotic Denominator Growth (`ANC-07`):** Verified $\frac{\log Q_N}{N} \to 6$ and $\frac{\log \Pi_N^\star}{N} \to \frac{8}{3}$ through $N = 80$, and verified $16^B \Pi_{2B}^\star < Q_{2B}$ (so the Adelic CRT Shadow $V_{2B}^\sharp$ fits in a single unit interval with $D_B = J_B = 0$) for all $B \ge 2$.

## 4. Explicit Unrun Gates and Scope Firewall

- The full repository-wide 14,500+ test suite and hosted GitHub CI were not claimed as executed on this commit head; only the mandatory root probes (`verify_provenance.py`, `observer_foundations_probe.py`, `ordinal_succ_report_probe.py`) and focused 2026-11-17 test suites were run locally.
- No Lean 4 kernel formalization of `ANC-01..12` is claimed.
- Finite rational certificates and $2$-adic congruences prove `ANC-01..12` within their stated domains; the asymptotic all-late-shell bounds $\liminf_B \mathcal{R}_B(0) > 0$ ($R_0$) and $\lim_B \mathcal{V}_B = 0$ (base-16 $\pi$ normality) remain **OPEN**.
