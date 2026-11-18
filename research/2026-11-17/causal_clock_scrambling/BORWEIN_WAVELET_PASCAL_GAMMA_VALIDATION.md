# Borwein Wavelet–Pascal–Gamma validation and hostile receipts

**Date:** 2026-11-17. Companion to [the theorem manuscript](BORWEIN_WAVELET_PASCAL_GAMMA.md). **Research-only. Full base-16 π normality, R0, and RH remain OPEN.**

## Source and focused execution

Source: the original four signed BBP poles, actual initial seed U_0=0, and the previously authenticated rational source-tail identity. The branch is stacked on draft PR #657; no edits to original source, main, archived provenance, releases or tags.

Executed in a local Python environment with the exact branch-equivalent source files:

    PYTHONPATH=/mnt/data python -m unittest \
      test_borwein_bbp_sweep \
      test_borwein_quantitative_certificate \
      test_borwein_scale_renormalization \
      test_bbp_tail_impulse -q

**53/53 tests passed: 24 inherited + 29 newly authored.** The optional high-precision Gamma numerical test skips if mpmath is unavailable, so mandatory exact Fraction tests require only the standard library.

| Newly committed file | Byte-identical local and fetched Git blob SHA |
|---|---|
| [Source-scale exact module](../../../observational_succ/borwein_scale_renormalization.py) | a406f4877c1614f434194c43cb06e8956caf3de9 |
| [Chronological source-tail impulse module](../../../observational_succ/bbp_tail_impulse.py) | 54399f281f60ebb01c1d6e461e69242e65460c6a |
| [16 scale/wavelet tests](../../../tests/test_borwein_scale_renormalization.py) | 3ed7ef3a67f78d15de5ed89db0e784358fd5ac3d |
| [13 Pascal/Gamma tests](../../../tests/test_bbp_tail_impulse.py) | 3e1cf1e56301d4e9cf4f02ba2fe07c03c008625c |

## Exact original-source wavelet budget

Each observation uses one rational U_N; all listed values below were computed by Fraction arithmetic, not π digit approximations.

C_atom = 335872/304434045 ≈ 0.0011032668833080084.

| Prefix N | Nonnegative wavelet budget, decimal view | Remaining squared Haar distance, decimal view |
|---:|---:|---:|
| 2 | 0.0000488238439171 | 0.0010544430393909 |
| 4 | 0.0001354257209767 | 0.0009678411623313 |
| 8 | 0.0009585337837746 | 0.0001447330995334 |
| 16 | 0.0010401398190052 | 0.0000631270643028 |
| 32 | 0.0010324894776862 | 0.0000707774056218 |

Every row satisfies budget + residual = C_atom EXACTLY. **Budget decreases from N=16 to N=32**; this is a hostile counterexample to assuming per-stage monotonically improving Haar energy.

Fejér positivity proves for every finite N-point circle observer a strictly positive lower floor 4862025/(313044726016 N^4), with the exponent 4 sharp by matching equally spaced-grid upper examples. Tests verify both bounds exactly on finite rational examples; the universal result is the paper Fejér proof.

## Original chronological block interference

For consecutive length-N blocks starting at a, the exact source-rational identity is

    E_merged = (E_left + E_right)/2 - D_(a,N),

with D nonnegative and independently reconstructed by the finite Borwein autocorrelation-kernel double sum. The dilation h ↦ 16^N h of the actual radix circle is checked by **exact equality of rational character angles**, not only by complex floating approximations.

| a=N | Left energy | Right energy | Merged energy | Interference D |
|---:|---:|---:|---:|---:|
| 2 | 0.001097694 | 0.000120552 | 0.000338469 | 0.000270654 |
| 4 | 0.000183797 | 0.000661411 | 0.000366426 | 0.000056178 |
| 8 | 0.000100242 | 0.000142522 | 0.000055678 | 0.000065704 |
| 16 | 0.000133943 | 0.000070153 | 0.000096442 | 0.000005606 |

The a=N=4 merged energy is **larger** than the left energy: contraction is not automatic even for original BBP finite shadows. At a=N=16 the positive defect is small relative to mean energy; no uniform all-shell gap has been established.

The original source future-tail bound supplies explicit rational comparisons of every such finite shadow with the true π phase history.

## Pascal hierarchy, Gamma asymptotics and source-carrier convergence

Exact original source formula:

    S_(N,k) = integral_0^1 t^(8N) (1-t^8)^k K(t) dt > 0,
    S_(N,k) = S_(N+1,k) + S_(N,k+1).

Each finite M-term source truncation gives rational S_[M] values and exact rational mass conservation at every Pascal level m:

    sum_(n=0)^m binom(m,n) S_[M]_(n,m-n) = P_M.

All tested first and second Bernstein moments equal their independent source-moment expressions exactly. The paper proves two endpoint Gamma asymptotics and a joint proportional-order Laplace rate; no extrapolation from finite ratios is used as a proof.

A separate 70-digit direct mpmath quadrature for (N,k)=(0,0),(0,2),(1,1),(4,3),(8,5) lay strictly inside independently computed 20-term rational source-tail lower/upper bounds, with relative interval widths approximately 10^-28. The optional local high-order test compares selected k=100,300 values to the derived Gamma k-asymptotic; the exact symbolic asymptotics are proved in the manuscript.

For M source terms and Pascal level m the new rational observer's W1 distance to the normalized full original Mellin carrier satisfies

    W1 <= 1/(2 sqrt(m)) + 16^(-M) r(M+1)/(15 P_M).

Finite conservative upper certificates:

| Source cutoff M | Level m | W1 upper ceiling, decimal view |
|---:|---:|---:|
| 4 | 16 | 0.125000063796 |
| 8 | 64 | 0.062500000000265 |
| 16 | 256 | 0.03125 |
| 32 | 10000 | 0.005 |

**The convergent measure here is the Mellin source carrier in coordinate y=t^8, NOT π's circle-phase empirical measure.**

## No-go controls, open boundary, and unrun gates

The previous locked positive zero-seeded Mellin source has the same Pascal identity, complete monotonicity and first Gamma time-axis asymptotic, but its completed radix-16 orbit stays at one phase and spends **zero wavelet detail energy**. Its high-order Gamma-axis coefficient differs by a factor of ten, which discriminates source profiles without proving digit statistics.

Further, every radix-16 orbit—including a perfectly locked orbit—has one-step filtered empirical-measure transport defect at most 64/(289N). Thus approximate source-dynamical invariance alone does NOT select Haar among invariant measures.

**OPEN:** a source-specific, signed BBP four-pole/cofactor/carry-to-wavelet inequality that forces the accumulated wavelet budget to saturate C_atom at every large horizon. This is the missing step equivalent to proving actual π normality, not a consequence of positive Gamma moments or finite tests.

**Unexecuted on this exact head:** full root SUCC unittest/provenance/observer/ordinal gates, Lean formalization, final hosted CI completion and independent referee audit. Earlier full-suite receipts apply only to their own recorded commits.
