# OPERATION ALETHEIA — The Source-Attached Interferometer Atlas

**Date:** 2026-11-15. **Proposed stacked base:** [#642](https://github.com/femboy2112/SUCC/pull/642) (`89c6f645938c3f1e4f002f5e81411f458db1689c`). **Status:** exact classical finite laws, two new-to-project complete *instruments* and source-specific transport, explicit hostile countermodels; **R0, all-mode signed cancellation, π base-16 normality, completed Weil positivity, and RH remain OPEN**. This is not an announcement of a new proof. No original source, seed, historical archive, Lean, manifest, production default, main branch or release changed.

## 0. What “find them all” can mean rigorously

There are infinitely many equivalent ways to encode a proof obligation; no one can enumerate **all conceivable detectors**. We instead audit the finite *declared* SUCC research frontier: Main XXV `PI_NORMALITY_FRONTIER.md`, its governing claim supplement and handoff, spectral purity, zero-anchored Haar, source-sensitive innovation, Lagarias/Weil/Li/Newman zeta criteria, and the recent resonance [#642]. The accompanying JSON ledger has 30 individually typed instrument **families**: 23 π/source families and 7 RH/zeta families. These are families, not independent evidential votes. Some are equivalent formulations of the same open statement, some are merely necessary/sufficient, and some measure only a distinct property.

The original, fixed four-pole source and zero seed are always

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\qquad U_{n+1}=16U_n+r(n+1).
\]

With \(x=\pi/16\), \(T_n=\sum_{j\ge1}16^{-j}r(n+j)>0\), the completed phases are
\(z_n=\{U_n+T_n\}=\{16^n x\}\). The original source has the established **strict** tail bound \(T_n<1/(64n^2)\) for \(n\ge1\). For each positive integer shell \(B\), put

\[
W_B(h)=\frac1B\sum_{n=B}^{2B-1}e^{2\pi i h z_n},\qquad h\in\mathbb Z\setminus\{0\}.
\]

`source_shell_words` certifies every requested finite hexadecimal observation directly from **rational BBP bounds**, rather than reading π digits from a fixture or inventing a changed initial seed. Four source types remain independent: arithmetic orbit, freely chosen index/phase *observer* distribution, exact available source readouts, and any additional physical quantum carrier. The latter is NOT inferred by the first three.

## ATLAS-01 — A single authentic-source all-harmonic detector (CLASSICAL; exact new-to-SUCC instrument)

The actual critical *positive Oily* two-stage law (Main XIII; [#344], [#634]) has

\[
w_h=\frac{h+1}{2^{h+2}},\quad h\ge0;\qquad w_0=\tfrac14.
\]

**Declare, do not assert as the BBP source's physical likelihood**, a new frequency-sampling instrument: sample the sum of two independent geometric\((1/2)\) delays conditioned to be nonzero. Thus

\[
q_h=\Pr(H=h\mid H\ge1)=\frac{h+1}{3\,2^h},\quad h\ge1,
\quad\sum_{h\ge1}q_h=1,
\quad\mathbb E_q H=\frac83.
\tag{A1}
\]

The exclusion of the `h=0` DC grade is **essential**: including that grade leaves an unavoidable \(1/4\) energy floor even for a normal orbit. Choose independent uniform time indices \(I,J\) from \([B,2B)\), independently of \(H\). Define their signed phase-collision response

\[
Y_B=\cos(2\pi H(z_I-z_J)).
\]

By the finite-pair identity and Tonelli (\(\sum q_h=1\)), its expectation is

\[
\boxed{\mathcal C_B=\mathbb E Y_B
=\sum_{h\ge1}q_h|W_B(h)|^2\in[0,1].}\tag{A2}
\]

**Theorem.** For *any* real \(x\), with its actual base-16 multiplicative orbit, \(x\) is base-16 normal **if and only if** \(\mathcal C_B(x)\to0\) as integer \(B\to\infty\).

*Proof.* If \(\mathcal C_B\to0\), then for every fixed \(h\ge1\), \(0\le q_h|W_B(h)|^2\le\mathcal C_B\) and \(q_h>0\). Hence \(W_B(h)\to0\). Negative modes are complex conjugates; Weyl's criterion plus shell/prefix equivalence yields normality. Conversely, normality gives every fixed \(W_B(h)\to0\); domination \(|W_B(h)|^2\le1\) by the summable \(q_h\) gives \(\mathcal C_B\to0\). The qualitative theorem holds for *any* positive summable full-support harmonic weights; the Oily weights are a source-motivated economical instrument, **not** necessary or unique for the equivalence. QED.

**Closed causal-transfer kernel.** For \(|z|\le1\),

\[
\sum_{h\ge1}q_hz^h
=\frac{\frac4{(2-z)^2}-1}{3}=:\mathcal K_2(z).
\tag{A3}
\]

Thus an entirely equivalent, finite-pair *closed-form* detector is

\[
\mathcal C_B=\frac1{B^2}\sum_{i,j=B}^{2B-1}
\operatorname{Re}\mathcal K_2(e^{2\pi i(z_i-z_j)}).
\tag{A4}
\]

It is possible for the kernel value of an individual pair to be negative, yet the aggregate is nonnegative because (A2) is a sum of squared Fourier amplitudes. On quarter-circle grid \(z\in\{1,i,-1,-i\}\), the **exact** real kernel values are respectively \(1,-13/75,-5/27,-13/75\). A second independent oracle recovers (A4) on exhaustive finite grids without importing the primary Fourier-energy implementation.

**Exact finite-frequency truncation:** for any \(H\ge0\),

\[
\boxed{0\le\mathcal C_B-\sum_{h=1}^{H}q_h|W_B(h)|^2
\le\sum_{h>H}q_h=\frac{H+3}{3\cdot2^H}.}\tag{A5}
\]

This is a uniform, original-source-independent tail budget. For the actual π source one must additionally pay the arithmetic phase-completion error in ATLAS-02. The detector remains an **equivalent open gate**, not a proof that the response decays.

**Statistical readout:** applying the declared two-outcome transducer \(P(\mathrm{click}\mid I,J,H)=(1-Y_B)/2\) yields \(P_B(\mathrm{click})=(1-\mathcal C_B)/2\). This probability approaches \(1/2\) under normality, **not one**. Repeating detector trials to get "at least one click" probability near one proves nothing about normality; even many nonnormal sources click.

## ATLAS-02 — Uniform all-frequency transport from original rational source to completed π (NEW-TO-SUCC source estimate; PROVED PAPER)

For any fixed \(h\ge1\), \(2\pi<7\), and original \(B\ge1\),

\[
\left|W_B^{\pi}(h)-W_B^{U}(h)\right|
\le\frac1B\sum_{n=B}^{2B-1} 2\pi hT_n
<\frac{7h}{64B^2}.
\]

Since both Fourier means have modulus at most 1,
\[
\left| |W_B^{\pi}(h)|^2-|W_B^{U}(h)|^2\right|
\le 2|W_B^{\pi}(h)-W_B^{U}(h)|<\frac{7h}{32B^2}.
\]

**Sum over *all* harmonics, not just fixed h.** Using \(\mathbb E_q h=8/3\), we obtain the all-mode estimate

\[
\boxed{\left|\mathcal C_B^\pi-\mathcal C_B^U\right|
\le\frac7{12B^2}.}\tag{A6}
\]

The prime/real arithmetic source is still the **same zero-seeded four-pole BBP**. Thus \(\mathcal C_B^U\to0\) iff π is normal in base 16, and one can evaluate its finite-harmonic truncations with exact rational phases \(U_n\) and rigorous trigonometric enclosures. The bound uniformly pays the entire unbounded harmonic mixture because its first moment is finite. No source-specific decay of either energy has been established.

**Independent second proof of (A6):** on the closed unit disk, \(\mathcal K_2'(z)=8/[3(2-z)^3]\) and \(|\mathcal K_2'(z)|\le8/3\). Hence the pairwise kernel is \(8/3\)-Lipschitz under chord displacement along a straight segment in that disk. Original completion changes each pair phase by at most \(7(T_i+T_j)\). Averaging gives \((8/3)\cdot7\cdot2(64B^2)^{-1}=7/(12B^2)\). The two proofs use the same arithmetic tail lemma, so they are **mathematically dependent corroborations**, not independent witnesses that π is normal.

## ATLAS-03 — One all-depth Haar detector, exactly inside the source-generated digit volume (CLASSICAL; exact new-to-SUCC instrument)

For \(v\in\{0,1,\ldots,15\}^k\), let \(p_B(v)\) be the empirical proportion of shell start positions whose actual *future* hexadecimal digits begin with \(v\). Here \(p_B(\varnothing)=1\). Define

\[
\boxed{H_{B,k}=\frac{16\sum_{|w|=k+1}p_B(w)^2-\sum_{|v|=k}p_B(v)^2}{15}
=\frac{16}{15}\sum_{|v|=k}\sum_{a=0}^{15}\left(p_B(va)-\frac{p_B(v)}{16}\right)^2.}\tag{A7}
\]

Then \(0\le H_{B,k}\le1\). More specifically, if \(C_{v,h}=\sum_a p_B(va)e^{2\pi iha/16}\), Parseval on the finite child group \(\mathbb Z/16\mathbb Z\) gives

\[
15H_{B,k}=\sum_{|v|=k}\sum_{h=1}^{15}|C_{v,h}|^2.
\tag{A8}
\]

**One real pair detector:** sample independent indices \(I,J\) from the same shell and choose \(K\ge0\) with probability \(2^{-(K+1)}\). At depth k output

\[
Y_{B,k}=
\mathbf1_{\text{first k digits of I,J agree}}
\begin{cases}
1&\text{if next digits agree},\\
-1/15&\text{otherwise}.
\end{cases}
\tag{A9}
\]

Finite probability expansion gives \(\mathbb E Y_{B,k}=H_{B,k}\). The full source Haar-volume response is

\[
\boxed{\mathcal H_B=\mathbb E_{K,I,J}Y_{B,K}
=\sum_{k\ge0}2^{-(k+1)}H_{B,k}\in[0,1].}\tag{A10}
\]

**Theorem.** For *any* real source point with definite base-16 digit expansion not ambiguous at a terminating boundary, \(\mathcal H_B\to0\) iff that real is normal in base 16.

*Proof.* If \(\mathcal H_B\to0\), positivity and positive depth weight imply \(H_{B,k}\to0\) for every fixed k. The second formula in (A7) forces \(p_B(va)-p_B(v)/16\to0\). Induction from \(p_B(\varnothing)=1\) yields \(p_B(v)\to16^{-|v|}\) for every fixed word. Conversely, normality gives these limits and hence each \(H_{B,k}\to0\); dominated convergence through \(H_{B,k}\le1\) gives \(\mathcal H_B\to0\). QED.

**Finite observer depth:** for K positive integer,
\[
\boxed{0\le\mathcal H_B-\sum_{k=0}^{K-1}2^{-(k+1)}H_{B,k}\le2^{-K}.}\tag{A11}
\]

For π, a fixed B,K requires only the first \(2B+K\) hexadecimal digits of the **authentic pointed BBP source**, which have an exact finite rational certification algorithm by SUCC's positivity/irrationality bounds. No imaginary uniformly random seed or changed source polynomial is used.

**Explicit wrong inference killed:** the periodic 16-digit sequence `0123456789abcdef` has \(H_{B,0}=0\) on aligned 16-position shells (each first digit equally frequent), but \(H_{B,1}=1/16>0\): distinct first digits have deterministic next digits. Likewise the source with equal mass on only digits 0 and 1 has a zero h=8 parity contrast but \(H_{B,0}=7/15\), hence is far from uniform in the complete 15-mode bank. These are calibration controls for a **generic target**, not alternate source-realizations of the exact BBP equation.

**Do not confuse Haar objects:** (A7) is the new nonnegative *spatial/future-cylinder* squared-detail energy. It is NOT the original source-selected, two-epoch **signed** chronological CDF overlap \(\Omega_M\) of SUCC #591, nor the seed-cylinder microscope of #601/#604. They inhabit different observer charts, even though the wavelet/Fourier algebra is related.

## ATLAS-04 — Exact iid calibration and diagonal contribution (CLASSICAL)

For \(B\) *independent uniform circle points*, a pair of sampled indices \(I,J\), selected independently with replacement, satisfies \(\Pr(I=J)=1/B\). If \(I\ne J\), the relative phase of any nonzero harmonic has mean zero. Hence
\[
\boxed{\mathbb E_{\rm iid\ Haar}\mathcal C_B=1/B.}\tag{A12}
\]

Likewise, for independent full uniform hexadecimal strings, the probability that two independently selected samples match in their first k digits is
\(1/B+(1-1/B)16^{-k}\). Substituting into (A7) gives \(\mathbb E H_{B,k}=1/B\) **for each k**, hence
\[
\boxed{\mathbb E_{\rm iid\ Haar}\mathcal H_B=1/B.}\tag{A13}
\]

The two formulas share the same **expected diagonal finite-sample contribution** under the stipulated iid null. This is **not a universal lower bound**: off-diagonal signed correlations can cancel the diagonal, and a deterministic evenly spaced sample can have energy smaller than `1/B`. They do not mean π's deterministic orbit has iid law. Deleting the same-index diagonal removes this null expectation but also destroys the guaranteed nonnegative squared-energy representation for arbitrary empirical measures. The tradeoff is explicit.

**Adaptation and calibration.** An observer who selects an index with history-dependent known propensity \(\pi_t(n)>0\) must not use the raw nonuniform sample as a uniform-shell mean. For a bounded observable \(f\), the Horvitz–Thompson single-observation response \(f(z_A)/(B\pi_t(A))\) is conditionally unbiased for \(B^{-1}\sum f(z_n)\). The correction does not imply small variance; if some required propensity is zero the full shell target becomes unidentifiable without additional premises. The random harmonic \(H\) in ATLAS-01 is part of the *target weighting* itself, so no inverse weighting is needed when it follows its declared \(q_h\) law.

**New fully rational finite π certificates.** For each finite shell, the implementation obtains rational `U_n`, bounds the completed discrepancy using `T_n`, and approximates every required `cos/sin(2πh U_n)` with rational Machin `π` brackets and alternating Taylor remainders. The weighted squared energies have explicit rational errors, followed by the exact Oily harmonic tail and the all-frequency source-transport bound of ATLAS-02. A separate rational source-digit algorithm certifies the finite-depth Haar word energy exactly. Example strictly outward-rounded intervals, each an observation of **the original** zero-seeded source and **not** an all-B claim:

| B | Oily all-harmonic energy (H=16) | Haar all-depth energy (K=8) |
|---:|---:|---:|
| 4 | [0.1265643593, 0.1996743040] | [0.2240234375, 0.2279296875] |
| 8 | [0.0995382771, 0.1179607219] | [0.1437825520, 0.1476888021] |
| 16 | [0.0957956977, 0.1005462675] | [0.0693522135, 0.0732584636] |
| 32 | [0.0279846476, 0.0293172486] | [0.0311279296, 0.0350341797] |

The Oily bounds are broader at small B primarily because the all-frequency rational-to-completed Green budget `7/(12B²)` is conservative. Full unrounded calculation inputs and re-execution are in `probe.py`; the stored decimal endpoints are outward-rounded rational consequences. No claim of independent real-world measurement.

A finite randomized click can make repeated detection of a nonzero signal highly likely; no finite number of clicks licenses the all-large-B limit. For a false model, propensity corrections and source-independent fresh holdouts are required to avoid self-confirming probe attraction.

## ATLAS-05 — All established π rung detectors, one normalized interface (CLASSICAL with imported exact rungs)

These are **source-selected responses** on the original orbit; the following equivalences, except the two new combined instruments above, are inherited from Main XXV and [#642].

| Rung | Actual detector response on shell B | Exact all-B gate | Class |
|---|---|---|---|
| R0 | phase click \(p_{B,1}=\frac12(1-\Re W_B(1))\) | \(\liminf_Bp_{B,1}>0\) | Equivalent (open) |
| R1 | independent pair \(c_B=|W_B(1)|^2\) | \(\limsup_Bc_B<1\) | Equivalent (open) |
| CH | hexadecimal next-digit mismatch rate, or click h=15 | \(\liminf_Bc_B^{(1)}>0\) | Equivalent (open) |
| CH_k | k-distant digit mismatch rate, or click h=16^k-1 | \(\liminf_Bc_B^{(k)}>0\) | Equivalent (open) |
| All CH_k | family of all period-escape probes | excludes finitely supported invariant shell limits | Equivalent to AM, **not** normality |
| Hex parity | original-signed digit parity; prime-side complement \(\beta_A\) | mean parity 0 (with full CRT and real tails) | Necessary for normality, not sufficient |
| Words | all finite word frequencies | each \(p_B(v)\to16^{-|v|}\) | Equivalent |
| Individual Weyl | two phase-click quadratures for every h | all real and imaginary \(W_B(h)\to0\) | Equivalent |
| Gram/Fejer | \(D_{N,H}/H=2\sum_{j=1}^{H-1}(1-j/H)|W_N(j)|^2\) | prescribed \(H_N\to\infty\) and energy \(\to0\) | Sufficient; prescribed rate may be stronger |
| Basel six-frame | signed \(A F_h(A)\), with \(n^{-2}\) height and complete real phase | \(A F_h(A)\to0\) every nonzero h | Equivalent |
| Haar CDF | \(D_N=W_1(\mu_N,Q\mu_N)\) with source and future preserved | \(D_N\to0\) | Equivalent; no unconditional contraction |
| Chronological overlap | actual \(\Omega_M\) of signed opposite CDFs | a *source-derived positive uniform* overlap + late-block control | Conditional sufficient; OPEN |
| Conductor-flat purity | original flat-step \(J_N^{\rm flat}\), exceptional births removed | \(\limsup J_N^{\rm flat}\le0\) at specified \(H_N\) | Sufficient; OPEN |
| Mesoscopic lag | \(\chi_h((16^\ell-1)U_n+\Delta_\ell(n))\) | joint signed lag cancellation | Candidate; single lag insufficient |
| Source Mellin/Gamma | \(\mathcal M(m(1+i\lambda))/\mathcal M(m)\), \(k\)-faces | its original-positive-source Gamma limit | **Proved but different target** |
| Deep source-zero microscope | zero-child cumulative signed Haar details at \(K=N-o(N)\) | deep energy tends to zero all h | Equivalent, OPEN |
| Restricted exponent | source \(\|16^m\pi/16\|\) | exponent <1 | Necessary for R0, not sufficient |
| Mixed joining | 2→3 Fourier selected ratio-fiber observable | joint nonproduct/phase contrast | Different target, no implication to ordinary normality |

**The sharp hierarchy matters.** Generic positivity, Gamma decay, seed-blind innovation cancellation, a single parity mode, a single moving-lag correlation and a finite epoch below the Haar threshold are not proof of R0 or normality. The original zero-seeded source need not satisfy the same theorem as a *different* seed; a source-blind theorem claiming to do so must still face the known coherent controls. An alternative nonnormal **zero-seeded polynomial source** that drops the exact four-pole identity is a hostile control against insufficient source hypotheses, not a counterexample to a theorem that specifically uses the authentic source.

## ATLAS-06 — RH family: signed witness detectors, not positive BBP analogues (CLASSICAL; conditional access)

RH is a **separate arithmetic source**, the genuine completed \(\xi(s)\) with all prime powers, real Gamma, conductor, poles, proper Schwartz test domain and original functional equation. No claim of automatic BBP→Weil transport is made.

**Completed Weil sign.** Let \(Q_W(v)\) be the authentic completed signed Weil form (as in [SUZUKI_FIRST_PRIME_WAVEFRONT.md](../../../2026-10-13/SUZUKI_FIRST_PRIME_WAVEFRONT.md)). The classical Weil positivity criterion is \(\mathrm{RH}\iff Q_W(v)\ge0\) for every valid test \(v\). The compact-support test space is separable in its usual test-function topology on each support chart, and the distributional quadratic form is continuous there. Therefore choose a countable dense collection \((v_j)\) over the **full valid domain** with strictly positive normalized probabilities \(q_j\). Then
\[
p_{\rm bad}=\sum_jq_j\,\mathbf1_{\{Q_W(v_j)<0\}}>0
\quad\iff\quad\neg\mathrm{RH}.
\tag{A14}
\]

**Proof:** a negative sign at a sampled test refutes positivity, so implies \(\neg\mathrm{RH}\). Conversely under \(\neg\mathrm{RH}\), Weil gives some \(v\) with negative form; continuity provides a neighborhood on which the form remains negative. Density supplies at least one \(v_j\), and its positive sampling weight gives \(p_{\rm bad}>0\). QED under the stated test-space/correct-source criterion. If each sampled negative is rigorously evaluable and independent samples are drawn, eventual discovery under \(\neg\mathrm{RH}\) has probability \(1-(1-p_{\rm bad})^m\to1\). This is an **abstract** witness instrument: no complete, always-terminating exact sign evaluator for arbitrary \(v_j\) is provided, particularly at form-zero cases. NO detection at finite m never proves RH. Sampling must never be presented as a truth probability.

**Other distinct RH families:** Lagarias's actual divisor-sum inequality for all n≥2, Li positivity for all coefficients, complete finite-height zero certification, and the original de Bruijn–Newman heat boundary \(\Lambda=0\) (since the Rodgers–Tao theorem proves \(\Lambda\ge0\)). Countable full-support random selection of indices in the Lagarias/Li lists can again make counterexample discovery almost sure **if** a violating index exists, but finite nonviolation cannot prove the universal criterion. The heat detector at any **negative** deformation parameter necessarily sees non-real zeros because \(\Lambda\ge0\), *whether or not RH is true*: treating that as an RH falsifier is categorically wrong.

The original first-prime Suzuki wavefront is a locally exact source-observable interaction with the full Gamma and pole terms. Its verified narrow-support positivity does not imply whole-space completed Weil positivity. For any test support allowing prime powers \(q\le e^{2a}\), all such terms must be included, fake composite 6 must not be admitted as a prime-power source, and the signed first/rank-two term cannot be replaced by a positive generic Gram.

**Original external references:** Jeffrey C. Lagarias, *An Elementary Problem Equivalent to the Riemann Hypothesis*, Ann. Math. Monthly 109 (2002), [arXiv:math/0008177](https://arxiv.org/abs/math/0008177); Li's criterion with Bombieri–Lagarias [DOI:10.1006/jnth.1999.2392](https://doi.org/10.1006/jnth.1999.2392); Weil positivity summarized in [Lagarias, *The Riemann Hypothesis: Arithmetic and Geometry*](https://www.math.lsa.umich.edu/~lagarias/doc/mt-holyoke-rev.pdf); Rodgers–Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020) e6 [DOI](https://doi.org/10.1017/fmp.2020.6). Mathematical normality of π and RH are not inferred from the existence of these detectors.

## ATLAS-07 — A calibrated adversarial program and what would actually change the frontier

**Controls retained:** (a) original zero source's exact identity; (b) h=0 DC-leak mutation that leaves a 1/4 Oily floor; (c) irrational normal versus a rational period-1 orbit; (d) \(1/15\) passes R0 but fails R1; (e) uniform first digit but deterministic next-digit cycle; (f) parity=0 but 14 missing Haar children; (g) spatial seed averaging that erases nonnormality; (h) full gamma smoothing that can erase a fixed source through observer-induced attenuation; (i) original zero source's rational-to-completed tail; (j) alternate zero-source polynomial satisfying finite positivity but not four original poles; (k) incomplete conductor/carry source; (l) invented Weil positive Gram; (m) negative heat parameter as fake RH falsifier; (n) biased adaptive policy with zero propensity; (o) duplicate evidence treated as independent probes; (p) all modes truncated without a certified tail budget.

**Executable validation:** The Python standard-library module uses only exact `Fraction` arithmetic for source poles, rational source digit certificates, signed quarter-grid Fourier energies, Gram/Fejer pair sums, original conductor births, Haar word energies, and selection-bias controls. It rejects unnormalized/nonpositive probe laws and malformed digit inputs. Its independent oracle uses **a different algorithm** for full quarter-circle Oily kernel energy and for original zero-seeded BBP digits. A small high-precision completed-π comparison is explicitly labelled **SMOKE, NOT CERTIFICATE**. Exact universal theorems are written proofs above; finite tests are falsifiers, not proofs of asymptotic convergence.

**Decisive next proof, ordered by actual frontier leverage:**

1. Prove \(\mathcal C_B^U\to0\) directly from the original four-pole zero-seeded recurrence and the *closed Oily resolvent kernel* \(\mathcal K_2\), with a source-derived signed off-diagonal bound. If successful, ATLAS-02 immediately transports it to π, proving full base-16 normality. Merely expanding \(\mathcal C_B\) as a positive energy and assuming its limit is zero is circular.
2. Alternatively, prove an all-large-shell lower margin for the one-mode R0 click detector using the actual source's carry/history-resonant interactions; no broad seed-blind conclusion required. The source-specific necessary restricted-exponent cost \(v_{16}(\pi/16)<1\) remains unpaid.
3. In the Haar volume, derive a **source-selected deep-scale upper bound** on \(\mathcal H_B\), not just early scales. The exact branch splitting from source generation could be a different arithmetic handle from the closed phase kernel; no current identity bounds them against each other quantitatively at all B.
4. RH: source-authenticate the whole signed Weil form and establish a universal lower bound on its valid test domain, or construct a certified negative source witness. A randomized negative search is a diagnostic, not a positivity proof.

### Claim ledger

- **DISCLOSED / CLASSICAL:** ATLAS-01 full-support energy equivalence, closed Oily kernel, ATLAS-03 digit-Haar Parseval and all-depth equivalence, ATLAS-04 iid null calibration, ATLAS-05 imported normality/rung equivalences, Weil dense negative-witness reduction under the stated source and test-space hypotheses.
- **PROVED PAPER / SOURCE-SPECIFIC:** ATLAS-02 uniform \(7/(12B^2)\) completed-to-rational BBP energy transport, using the inherited original \(T_n<1/(64n^2)\).
- **OBSERVED:** exact finite source programs and independent finite oracles; high-precision π smoke values (not certified estimates of new asymptotic behavior).
- **CONJECTURED:** that a genuine source-selected arithmetic bound can be derived using the Oily closed kernel, the Haar all-depth construction, or a resonant-lag signed interaction.
- **UNVERIFIED:** source-specific all-shell energy decay, original R0, π normality, universal Weil positivity, RH, a physical Gamma/Haar/quantum interferometer for π, and an independently derived BBP→Euler/theta morphism.
- **REFUTED by explicit controls:** single-mode evidence implies normality; uniform first-digit distribution implies all-word normality; h=8 parity balance implies complete child Haar; source-free positive kernels imply original Weil sign; probabilistic measurement makes a deterministic theorem true.

This is a **complete instrument inventory relative to the explicitly named active frontier documents**, not a proof or guarantee that no other mathematical detector exists.
