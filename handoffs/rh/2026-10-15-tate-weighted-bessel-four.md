# RH handoff — the original four-moment positive high source and an explicit low-rank positive host

**Date:** October 15, 2026. Research branch \`research/tate-weighted-bessel-four-low-2026-10-15\`, draft PR #130, parent 7-moment source PR #128 commit \`21a1d6854df56b99e9846b311a1035455a6d6d88\`. Original signed Suzuki source SHA \`0cc8510b71d178fc79e8d410a86d8b6014cf9178\`, no source rewrite or nontrivial-zero lookup. Main, releases and \`femboy2112/FuckingRH\` untouched. **RH OPEN.**

## The positive theorem (mathematical all-tests, not numerical finite Gram)

For every nonzero complex smooth test f supported in \((-1/2,1/2)\) whose power moments \(\mu_k=\int t^k f(t)\,dt\), \(k=0,1,2,3\), vanish, the **authentic original completed Weil form** satisfies
\[
\boxed{W_\zeta(f*\widetilde f)>\frac{20699}{1000000}\|f\|_2^2>\frac1{50}\|f\|_2^2.}
\]
Proof: the real original 128 Gamma OU Fourier modes have spectral multiplier \(m_{128}(13)>6097/1000\); genuine true-prime p=2 half-density impulse has sharp first-window shift norm 1 and \(w_2<1/2\); authentic \(C_\infty<43/8\); original negative sinh-polar is bounded by \(1/4718592<10^{-6}\) using the four moments; positive cosh polar and omitted Gamma remain PSD. Crucially, the actual Gamma-weighted Fourier/Legendre spherical-Bessel leakage is proven \(<2013/10000\) by **96 exact rational frequency-cell enclosures**, modes l=4..15, series order 12 and rigorous omitted-series/omitted-angular tails; not floating numerical sampling. The final inequality is direct rational subtraction.

## Unmodified original signed Suzuki: only FOUR unresolved low moments

On true derivative Hilbert carrier \(H=L^2_0((-1/2,1/2))\), \(f=Vu\), \(K=V^*V=(-\Delta_N)^{-1}\), the genuine Legendre modes P1..P4 span a low subspace of dimension 4. Their orthogonal complement obeys
\[
\boxed{D_4=Q_4GQ_4\succeq\frac1{50}Q_4KQ_4.}
\]
The original PR #109 source derivative bound \(\|g'\|_{L^1(-1,1)}<11/40\) gives legitimate zero-shift \(0\preceq R_0\prec121/32\,I_4\), but **the original 4×4 short \(S_0=A-R_0\) is unverified**.

No \(cI\) high-compact spectral gap, unbounded \(D_4^{-1}\), omitted polar/prime, or fake primitive composite Euler atom is asserted. Rank-six/seven and parity fifteen reductions are preserved as independent negative/control checkpoints.

## A concrete positive host, with its correction explicitly displayed

The authentic negative form is bounded below solely by four low dimensions, by zero-shift Schur and \(\|G\|<11/40\):
\[
\boxed{\langle u,Gu\rangle>-\frac{649}{160}\|P_4u\|_2^2.}
\]
Therefore the **modified** operator
\[
\boxed{\widetilde G=G+\frac{65}{16}P_4\succeq\frac1{160}P_4\succeq0}
\]
is unconditionally PSD for every original derivative input. This is a genuine finite-rank, visible, non-Euler positive compensation; **it is not the original RH-strength \(G\)**. The original negative Morse index and nullity are each \(\le4\).

The correction can be written entirely in terms of the first four original test moments. With \(\mu_k=\int_{-1/2}^{1/2}t^kf(t)dt\) and \(u=f'\), integration by parts against the genuine unnormalized Legendre P1..P4 gives
\[
\begin{aligned}
\langle u,P_1(2t)\rangle&=-2\mu_0,\\
\langle u,P_2(2t)\rangle&=-12\mu_1,\\
\langle u,P_3(2t)\rangle&=3\mu_0-60\mu_2,\\
\langle u,P_4(2t)\rangle&=30\mu_1-280\mu_3.
\end{aligned}
\]
Since \(\|P_j(2t)\|^2=1/(2j+1)\), the complete positive correction is
\[
\boxed{
\frac{65}{16}\bigl[
3|2\mu_0|^2+5|12\mu_1|^2+
7|3\mu_0-60\mu_2|^2+
9|30\mu_1-280\mu_3|^2
\bigr].
}
\]
These are **source-typed observables**, not independent Brownian freedoms or four fictitious prime jets. The formula is exact for complex smooth tests (Cauchy–Schwarz/Hermitian inner-product conventions checked).

## The true low-source scan / what it does NOT yet prove

At true Gamma J32, the 4×4 original signed low Galerkin source has positive diagonal intervals and 2+2 reflection blocks. One finite-source parity determinant lower bound is positive; another crosses or lies below zero, and omitted Gamma is PSD. That stage is neither proof nor refutation of the **full** low block, and even PSD of the full low \(A\) alone would not establish \(S_0=A-R_0\ge0\). The source atlas rechecks J32/J64 and records both determinant endpoints, retained polar signs, and omitted tail.

## Next genuine RH step

Use true original source low 4×4 \(A\), find a source-valid high trial \(U:P_4H\to Q_4H\), and produce the **continuum derivative residual Gram** \(C_U\) with outward intervals. Prove the sufficient *zero-shift* matrix \(A-L_U-50C_U\succeq0\), not merely a sampled finite Gram or positive auxiliary \(\widetilde G\). That would establish the complete Weil sign on a=1/2 only; an all-a source-compatible prime-birth/Archimedean-gluing theorem is still needed for RH. Any negative original-source witness needs independent hostile audit.

**Artifacts:** mathematical paper \`research/2026-10-15/TATE_WEIGHTED_BESSEL_FOUR_SCHUR.md\`; source exact spectral implementation \`observational_succ/tate_weighted_bessel_four_schur.py\`; source rank-four host and moment formula \`observational_succ/tate_four_low_compensator.py\`; tests \`tests/test_tate_weighted_bessel_four_schur.py\` and \`tests/test_tate_four_low_compensator.py\`; replay \`scripts/tate_weighted_bessel_four_probe.py --verify\`; frozen \`research/2026-10-15/TATE_WEIGHTED_BESSEL_FOUR_RECEIPT.json\`; true signed source atlas \`scripts/tate_weighted_bessel_original_low4_scan.py\`; workflows \`.github/workflows/tate-weighted-bessel-four.yml\` and \`.github/workflows/tate-weighted-bessel-original-low4.yml\`. Exact source test support, not independent journal peer review. **RH PROVED: NO.**
