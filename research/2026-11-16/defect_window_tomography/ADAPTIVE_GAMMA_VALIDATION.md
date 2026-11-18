# Adaptive Gamma Ice-Climb — finite validation and hostile controls

**Date:** 2026-11-16. Companion to [the full manuscript](ADAPTIVE_GAMMA_ICE_CLIMB.md). Finite tests check their declared domains; proofs of the universal algebraic identities are in the manuscript. Nothing here proves π-normality, R0, or a physical observer.

## Executed local regression

The same 7,112-byte test script locally executed and committed as [test_zoom_gamma_transport.py](../../../tests/test_zoom_gamma_transport.py) has matching Git blob SHA-1:

~~~text
1a6db1dead59c56aa164dda891418dffd9baa9ad
~~~

The local command was Python unittest verbose on that exact file: **10 tests run, 10 PASS, no failures/errors**. Tests include Gaussian-rational exact nonlinear-moment identities, radix-step composition, nonzero/null Gamma controls, positive microscopic time, invariant deck gap, original four-pole Fraction partial sums and tail/error comparisons, locked rational source, all-harmonic lock and three finite sparse-irrational hostile prefixes.

The exact rational checks are computational receipts. Finite float phase comparisons have explicit tolerances and do not certify universal limits.

## Independent high-precision implementation diagnostic

A separately written mpmath 70-digit direct quadrature computed

\[
\int_0^\infty e^{-g}e^{2\pi i x 16^{n+\delta_n(g)}}\,dg
\]

and compared it with \(e^{2\pi i16^nx}/(1-2\pi ix)\), for \(x=\pi/16\).

| n | Absolute quadrature difference |
|---:|---:|
| 0 | printed zero at working precision |
| 1 | 4.61750843317713407e-71 |
| 5 | 3.27436816900889473e-66 |

The same independent implementation reported:

~~~text
c(pi/16)    = 0.0788872807289900173520645836667 - 0.410067234498355375601721764074 i
abs(c)      = 0.4175863262487693775611
lower gap   = 0.3239958340498020447018
~~~

The independently derived **exact** rigorous lower bound in the manuscript is stronger in authority than these decimals: \(|c(\pi/16)|>41/195>1/5\).

Independent high-precision literal four-pole source evaluations produced these ratios of actual finite errors to the claimed analytic upper bounds; all should be below 1:

| n | Gamma M-error / bound | Signed defect error / bound |
|---:|---:|---:|
| 1 | 0.60803961870307 | 0.21000644533834 |
| 2 | 0.62821394407237 | 0.20886508089397 |
| 4 | 0.62968237805927 | 0.20879324701797 |
| 6 | 0.62968866073376 | 0.2087931149282 |
| 10 | 0.629688810953 | 0.20879315602571 |

These are floating numerical diagnostics, **not** certified intervals, external scholarly reviews, or source-independent witnesses.

## The decisive hostile irrational

The infinite source \(x_\star=3/16+\sum_{j\ge1}16^{-4^j}\) has exact nonzero Gamma decoder margin \(|c(x_\star)|>1/5\). Nevertheless its selected shells \(B_j=2\cdot4^j\) satisfy

\[
0\le1-\Re W_{B_j}(x_\star)<32\pi/(225B_j)\to0.
\]

The proof uses the full geometric digit-tail bound, not an inference from the three finite tested shells. This is the exact reason the formal Gamma transport, and even a large positive compression magnitude, cannot by themselves prove R0.

## Unexecuted and scope boundary

The full repository tests, AGENTS.md root provenance/observer/ordinal gates, Main XXIV/XXV/XXVI integration gates, Lean, hosted CI on the final branch head, independent original-source physical observations and any all-late-shell theorem were **not executed/claimed** by this local test. Source-prefix approximations are computed from existing authenticated BBP data, not newly observed measurements.

**Next probe:** freeze a source-selected *signed* joint carry/CRT/Gamma prediction distinguishable from the already equivalent Weyl average. Hostile-test changed seeds, rational finite shadows and coboundary gauges first. A finite success is not a universal proof.
