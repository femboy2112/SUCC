# Fresh exact-source finite diagnostics — orbit exclusion, NOT normality

**Test chronology:** A=9,17,33, original source, coherent same-four-pole wrong seed, full roots and half-arc controls were declared in [PREREGISTRATION.md](PREREGISTRATION.md) before the new source probes. The previously used A=8,16,32,64,128 for roots/half arcs were **development**, not blind holdouts.

**Exact executed probe:** [source_exclusion_probe.py](source_exclusion_probe.py) was run in the local container on precisely these three epochs and four controls. Its Git blob SHA computed from the exact local executed bytes, \`712944efc5daf1e5b6684bccbf143d20fa4afec6\`, is identical to the blob fetched from the committed GitHub branch; the SHA-256 of the local file was \`a87e6acfd01d04b23c10a649317e444ea2ddf0ccc2212acce118d4a8867d1460\`. Source state evolution uses fully unwrapped \`Fraction\`; independent collapsed original forcing
\((120n^2-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]\) is checked against the four original signed poles for every n. The coherent wrong seed uses the **source-only future-tail rational series** \(-T_n\), truncated after 40 geometric terms; the remaining theoretical series is rigorously positive and bounded by \((4/(8(n+41)-7))16^{-40}/15\). No numerical π digits are input.

Reported complex Fourier phases and log chords are computed **only after** exact rational reduction, using double-precision complex/trigonometric functions: they are finite diagnostics, NOT rigorous outward interval certificates. Exact mathematical bounds and the sufficient asymptotic condition are independently proved in PROOFS.md.

Define \(E_A=A^{-2}\log|\Delta_A|^2\), and \(F_M=\operatorname{Tr}S_{A,M}^2\).

| A | configuration | E_A (observed) | abs c_1 | F_3 | F_5 |
|---:|---|---:|---:|---:|---:|
| 9 | ORIGINAL U0=0 | +0.091197565 | 0.137135003 | 0.362958742 | 0.240062482 |
| 9 | SAME forcing, coherent wrong seed | -7.418871970 | 0.999999969 | 0.999999917 | 0.999999752 |
| 9 | N roots of unity | +0.244136064 | 0 | 1/3 | 1/5 |
| 9 | half-circle grid | -0.112804392 | 0.639863387 | 0.515300068 | 0.338917284 |
| 17 | ORIGINAL U0=0 | -0.013849227 | 0.275429964 | 0.386819349 | 0.250817284 |
| 17 | SAME forcing, coherent wrong seed | -9.166342958 | 0.999999998 | 0.999999994 | 0.999999981 |
| 17 | N roots of unity | +0.166659608 | 0 | 1/3 | 1/5 |
| 17 | half-circle grid | -0.221363863 | 0.637526556 | 0.513973382 | 0.337453312 |
| 33 | ORIGINAL U0=0 | +0.022703967 | 0.037974040 | 0.348669953 | 0.228580881 |
| 33 | SAME forcing, coherent wrong seed | -10.808866394 | ≈1 | ≈1 | ≈1 |
| 33 | N roots of unity | +0.105954775 | 0 | 1/3 | 1/5 |
| 33 | half-circle grid | -0.300088992 | 0.636860239 | 0.513595984 | 0.337043346 |

**All fresh source/control tests PASS.** The independently coded frame-purity matrix equals the independent Fourier identity within 1e-11; the exact all-h positive regularized kernel bound is verified numerically by direct pairwise K_r for each configuration. The regular roots realize exactly E_A=(log A)/A (up to double rounding), and their small-mode frame purities saturate 1/M. The original source **does not** display a monotonic E_A trend on these epochs, and no asymptotic claim is made from three samples.

For A=9,17,33, the wrong-seed E is dramatically negative because its source-tail phases cluster near zero. The ALL-A theorem PF11 rigorously bounds E by \((1-1/A)(\log(\pi/32)-2\log A)\to-\infty\); the finite diagnostic is merely a calibration.

The half-circle control's limit is **exactly** \(-7\zeta(3)/(2\pi^2)\approx-0.4262783988175\), while first harmonic tends \(2/\pi\approx0.6366197724\), despite every pair of points being distinct and separated by at least 1/(2N) in circle distance. This falsifies the claimed implication "minimal pair separation of order 1/N forces Haar."

**Not claimed:** a source-selected original Fekete energy lower bound, original π normality, source-specific mixed Weyl cancellation, full native suite, new Lean theorem, external scholarly referee, or physical Pauli fermions in SUCC.
