# VPB — Vacuum/parameter matrix elements and authentic BBP positive resolvent

**Date:** 2026-10-25. **Pinned base:** Coherent Main X at 1e3a453e869992961bc2d7f3bb6f2f1ddab38854. **Branch:** research/vacuum-parameter-bbp-krylov-2026-10-25. [Full proof dossier](../research/2026-10-25/VACUUM_PARAMETER_BBP_KRYLOV.md). No frozen source files modified.

**Claim discipline:** CLASSICAL means attributed paper mathematics, EXACT FINITE means an exact rational check within a stated scope, and UNVERIFIED means its needed discriminator has not been proved. Original academic priority is not claimed. π normality and RH remain OPEN.

| ID | Source-bounded result and status | Falsifier / outstanding obligation |
| --- | --- | --- |
| VPB-01 | **CLASSICAL / PAPER:** principal log(1)=0; log I=0 for positive operators; for each rational nonzero diagonal q, standard adeles satisfy product of all local norms =1 and sum of their logs =0. | Additive 0 differs from multiplicative 1; single-place ideles need not be norm-one; finite prime omissions leave exact signed residual. |
| VPB-02 | **CLASSICAL / PAPER:** for a>-1, integral from 0 to 1 of (t^a−1)/log(t) dt = log(1+a), anchored at a=0. Finite-dimensional self-adjoint matrices with spectrum >−1 have a spectral-calculus extension. | Noncommuting D log A[H] is NOT generally A^−1 H; use double resolvent or trace derivative with cyclicity. |
| VPB-03 | **CLASSICAL / SOURCE-EXACT:** original four-pole r(n) equals integral of t^(8n−8) P(t), P=(1−t)(t²+2)(t²+2t+2), positive for t<1 and P(1)=0. | All four signs, index and initial state must match main BBP source; coefficient mutations remove the endpoint cancellation. |
| VPB-04 | **CLASSICAL / PAPER + EXACT FINITE:** all alternating forward differences of r are strictly positive, all finite moment Hankel matrices are PD, continuous parameter derivatives alternate. | Unsigned scalar Hausdorff positivity is not completed signed Weil positivity or signed BBP carry cancellation. |
| VPB-05 | **PAPER DERIVED FROM AUTHENTIC BBP:** positive contraction M multiplication by t^8 on L²(Pdt) gives r(n)=<1,M^(n−1)1> and π=<1,(I−M/16)^−1 1>. | Depends on classical authentic BBP equality; a free positive operator with changed source is not π. |
| VPB-06 | **PAPER / EXACT FINITE:** for N>=1, 16^(N−1)π=U_N+T_N and r(N+1)/16<=T_N<=r(N+1)/15. | Digits are certified only when this entire interval stays inside one integer carry cell; no all-time frequency bound. |
| VPB-07 | **CLASSICAL VARIATIONAL / PAPER:** Krylov Galerkin G_ij=m_(i+j)−z m_(i+j+1) yields exact R(z)=L_d+<e,A^−1e> with L_d+||e||²<=R<=L_d+||e||²/(1−z). | Requires real 0<=z<1, positive operator and the correct Hilbert metric; not automatic for signed/complex sources. |
| VPB-08 | **PAPER PROVED ALL DEPTHS:** 0<=R(z)−L_d<=z^(2d)m_(2d)/(1−z). For π, <=(16/15)16^(−2d)r(2d+1). | The gap degenerates as z↑1; no arbitrary limit exchange. |
| VPB-09 | **EXACT FINITE + INDEPENDENT HOLDOUT:** eight Krylov basis elements and 17 rational authentic moments certify 23 fractional hexadecimal digits, 3.243F6A8885A308D313198A2. | Independent Machin alternating-series rational enclosure checks interval; this is value computation, not normality. |
| VPB-10 | **CLASSICAL / PAPER:** at z=1 the scalar R(1^−) remains finite though the full inverse is unbounded, inverse vector is not Hilbert, and R'(z)=(15/64)log(1/(1−z))+O(1). | Quadratic-form vs operator-domain distinction is load-bearing. No RH inference. |
| VPB-11 | **CLASSICAL / EXACT FINITE:** rank-one determinant lemma yields a normalized log-potential/resolvent parameter identity; one-port graph's static response is zero while a grounded 3-node path retains hidden determinant ab. | Gaussian free-energy interpretation requires a declared physical/statistical model and normalization. |
| VPB-12 | **EXACT FINITE COUNTERMODEL:** positive single-atom measure matching first two authentic moments yields rational π-like value 1608152/511915, hence base-16 nonnormal. | Mutant does NOT match all authentic moments; it kills the inference from positivity and finite jets alone. |
| VPB-13 | **OPEN / UNVERIFIED:** scalar moment/Krylov positivity or global vacuum norm identity yields π-selected Weyl cancellation S_N(h)=o(N), or original completed signed Weil positivity. | Requires selected signed carry/character correlations or an authentic Weil source identification, not numerical digits or generic Gram PSD. |

**Implementation/replay:** Python Fraction exact module observational_succ/vacuum_parameter_bbp.py; local 24 passing tests in tests/test_vacuum_parameter_bbp.py; source-carrier integration tests in tests/test_vacuum_parameter_bbp_integration.py; JSON probe scripts/vacuum_parameter_bbp_probe.py --verify. Test hosted exact head and AGENTS.md whole-repo checks independently. Keep archived originals and existing claim IDs untouched. **RH PROVED: NO. π NORMALITY PROVED: NO.**


### New two-ended finite transfer claim

**VPB-14 — PAPER PROVED / EXACT FINITE:** For each fixed nonzero integer \(h\), horizon \(N\ge1\), and positive Krylov depth \(d\), take the exact-rational interval \([l_d,u_d]\), midpoint \(a_d=(l_d+u_d)/2\), and radius \(\rho_d=(u_d-l_d)/2\). The genuine selected orbit and its rational midpoint obey

\[
\frac{|S_N(h,\pi)-S_N(h,a_d)|}{N}
\le \frac{8|h|}{15N}(16^N-1)\rho_d,
\]

by source-authentic π bracketing and the unit-circle Lipschitz bound using \(\pi<4\). The bound is wholly rational; checked for horizons 8,16,24,32 and exact scaling mutants. **Boundary:** the approximant's own signed sum remains uncontrolled; each fixed rational \(a_d\) has an eventually periodic base-16 orbit, so no π normality follows. No polynomial bit-complexity claim is made. New tests: tests/test_vacuum_phase_transport.py; executable instrument: observational_succ/vacuum_phase_transport.py. The proof is in dossier §10.
