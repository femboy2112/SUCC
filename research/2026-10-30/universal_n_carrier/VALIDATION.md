# Validation receipt — universal N / Pascal / Gamma / Pisot / zeta(-1) / primes

2026-10-30. DRAFT source-constrained research. Original four signed poles, U0=0, archived contracts, production and main unchanged.

**Local exact runs:**
- Expanded local SymPy/mpmath/Fraction bridge_probe.py: **17/17 PASS**, including independent finite N zeta spine, Kummer carries and all-place product formula, Paschal Fibonacci/Pisot hostile recurrences, source positivity and 15/59/243 jets, original unweighted Gamma ratio, positive rank-two mutant, v2 slopes, heat regulator, zeta functional equation, original radix-16 weighted B_N, Abel decomposition and seed-twist counterexample.
- Source-independent natural_triangle_probe.py: **6/6 PASS** with exact Fraction source mixtures and order-sensitive countermodel.
- Compact locally executed stdlib universal_n_probe.py: **13/13 PASS** (source-algebra and successor/prime checks). A readable corresponding 13-method test module is included on the GitHub branch. Do not assume byte-identical execution until exact remote file bytes are independently replayed.
- Separate independent_oracle.py: **PASS** exact SymPy rational original R/Q, 85-digit mpmath Laplace integrals for a=1,9,17,73,257, direct original finite rational-versus-Gamma quotients N=1,7,25,90, all-prime factorizations and prime2 slope, asymptotic N^15/8 Gamma ratio at N=100,1000,10000, C constant derivative and Gamma–Green sum, Hurwitz/Lerch, zeta(-1) functional equation, convergent Euler product at s=2, Gamma–Poisson/Pascal and mutant. Local 4-stage integer B_N valuations, real logarithmic derivative and Abel multiplication separately checked exactly.

**Representative oracle values:**
- C_BBP = 0.00171415831468372017104209953889435619798938648...
- S_R = 3.38604761959719172193641883143841286022691835...
- M_BBP = 0.0162969977338265655649183632105939984019832635...
- N^(15/8) P_N/C_BBP: N=100 ->1.00242078258865, N=1000 ->1.00024217676707, N=10000 ->1.00002421864286.

**Explicit repaired finite-test defects:** initial infinite symbolic binomial generating series had a piecewise convergence guard and was replaced by exact coefficient tests; unevaluated log prime factors required symbolic simplification; symbolic Boolean root predicates were changed to numerical predicates; an order-sensitive history countermodel originally had accidentally equal path weights and was corrected. The independent Hurwitz zeta numerical derivative showed about 1e-10 loss of precision at rational shifts, and a contour derivative attempted at 85 digits timed out; the repaired oracle uses the official Lerch/Gamma identity plus a looser 1e-8 **numerical-only** calibration. No 85-digit direct Hurwitz derivative accuracy is claimed.

Full root SUCC AGENTS provenance, 10k+ unit suite, hosted exact-head CI, Lean and external blind referee **NOT RUN**. These local checks support finite formulas and holdouts, not an unproved universal source-selected pi normality/RH claim.
