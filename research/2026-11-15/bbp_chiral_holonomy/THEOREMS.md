# BBP's 7±4 chiral loop: source-selected Clifford phase and four-time circle interferometer

**Research note, 2026-11-15.** This is an additive successor of SUCC draft #646 and of the local `bbp_loop_holonomy` dossier. All source identities retain the exact BBP four-pole rational forcing and the literal `U_0=0`. The results are classical arithmetic, finite-dimensional operator algebra and exact observer equalities. They **do not** establish π-normality, R0, a new source-specific all-shell cancellation estimate, physical energy production, Higgs dynamics, or quantum hardware. "Quantized" refers only to the explicitly constructed root-of-unity *phase*.

## Source contract and scope

Use the original (unreduced!) rational state

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Write \(x=\pi/16\), \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\), \(z_n=\{U_n+T_n\}=\{16^nx\}\), with the authentic classical BBP identity imported. Denominators of \(U_n\) are odd, so \(U_n\) belongs to \(\mathbb Z_2\). Let \(q=16^k\), \(k\ge1\), \(\omega=e^{2\pi i/16}\), and for \(n\ge k+1\), define the source return holonomy

\[
J_{n,k}=\frac{U_{n+q}-U_n}{q}\pmod{16}.
\]

Reduction of the rational quotient is in \(\mathbb Z_2\), not real fractional-part reduction. Direct original-source truncation gives \(J_{n,k}=11,11,3,3\pmod{16}\) according to \(n\pmod4\) (the fully written finite derivation is in the companion `bbp_loop_holonomy/THEOREMS.md`, LH-01). **No use of the unreviewed global 2-adic logarithm identity `F(0)=0` is necessary for the stable n range.**

## CH-01 — the exact 7±4 decomposition (PAPER-PROVED FINITE)

Put \(s_n=(-1)^{\lfloor n/2\rfloor}\), whose values on \(n\bmod4\) are `+,+,-,-`. Then

\[
\boxed{J_{n,k}=7+4s_n\pmod{16}}.
\]

Thus \(J_n\in\{3,11\}\), their difference is 8, and

\[
\boxed{\omega^{J_{n,k}}=i\omega^7s_n,\qquad
\omega^{J_{n+2,k}}=-\omega^{J_{n,k}}.}\tag{CH1}
\]

Also \(J_nJ_{n+2}=3\cdot11=33\equiv1\pmod{16}\), while \(J_n^2\equiv9\pmod{16}\) for both sectors. This contrasts **multiplicative inverse units** with **antipodal additive circle characters**. The symmetric center 7 = 2³−1 is a natural *integer-lift convention*, **not a unique center in the ring modulo 16** (one may choose 15 with reversed orientation). The invariant content is the pair {3,11}, the order-two coset and the source-selected two-time sign flip; never infer the actual 2-adic predecessor \(-1\) from the chosen center 7.

## CH-02 — a genuine central −1 in the four-state clock representation (PAPER-PROVED FINITE)

On \(\mathcal H_4=\mathbb C^{\mathbb Z/4\mathbb Z}\) define unitary operators

\[
T_2|j\rangle=|j+2\rangle,\qquad
M|j\rangle=\omega^{J_j}|j\rangle,
\]

where \(J_j\) uses the verified periodic source jet values. The return holonomy gives

\[
\boxed{T_2M=-MT_2,\qquad T_2MT_2^{-1}M^{-1}=-I.}\tag{CH2}
\]

Writing \(j=2b+a\) with \(a,b\in\{0,1\}\), the operators become

\[
T_2=X\otimes I_2,\qquad M=i\omega^7(Z\otimes I_2),
\]

so the anticommuting Pauli/Clifford *algebra* is exact. The central sign survives any **simultaneous** unitary basis conjugation of these two declared operators. This is a mathematical projective commutator, **not** a physical qubit, an energy eigenvalue or evidence that BBP generates Higgs bosons. The source origin enters through the specific rational derivative jet; the ring/basis alone does not force the anticommutator (see CH-07).

## CH-03 — the next refinement turns −1 into a parity-selected square root (PAPER-PROVED FINITE)

The same **exact unreduced** difference quotient at one finer register is

\[
J_{n,k}^{[32]}=(U_{n+q}-U_n)/q\pmod{32}.
\]

For \(n\ge k+2\), the original-source truncation and Taylor integrality give

\[
\boxed{J_{n,k}^{[32]}\equiv r'(n)+16\pmod{32}.}\tag{CH3}
\]

Proof details: \(U_n=\sum_{j=0}^{n-1}16^jr(n-j)\); divide the q-difference by q and retain j=0,1 modulo 32. All j≥2 vanish. The rational function has odd 2-adic denominator, and its second divided Taylor coefficient \(r''(t)/2\in2\mathbb Z_2\), as verified independently coefficientwise from the original numerator and denominator in `independent_audit.py`. Since q is divisible by 16, each difference quotient equals \(r'(t)\pmod{32}\). The j=1 term is 16\(r'(n-1)\equiv16\pmod{32}\), because the derivative is odd.

The independently certified polynomial table for \(r'(n)\pmod{32}\), with columns \(n\equiv0,\ldots,7\), is

`[11, 27, 3, 3, 27, 11, 19, 19]`.

Consequently the **actual q-loop** register-32 table is

`[27, 11, 19, 19, 11, 27, 3, 3]`, and

\[
\boxed{J_{n+2,k}^{[32]}-J_{n,k}^{[32]}
\equiv \begin{cases}24,&n\text{ even},\\8,&n\text{ odd}\end{cases}\pmod{32}.}\tag{CH4}
\]

The higher-phase commutator is therefore

\[
\boxed{\exp\left(\frac{2\pi i}{32}(J_{n+2}-J_n)\right)
=-i(-1)^n,\qquad
\left[-i(-1)^n\right]^2=-1.}\tag{CH5}
\]

This is the exact source-selected **binary refinement** of CH2: at level 16 the answer is fixed \(-1\); at level 32 it is one of its two complex square roots \(\pm i\), selected by the other time bit. At arbitrary levels \(2^m\), defining \(\Gamma_n^{(m)}=\exp(2\pi i(J_{n+2}-J_n)/2^m)\) for the same rational q-quotient yields the compatible formal law \((\Gamma_n^{(m+1)})^2=\Gamma_n^{(m)}\). No claim is made that every higher branch has been classified; the first two stages are explicitly determined.

## CH-04 — temporal Haar/Walsh factorization (CLASSICAL EXACT; original phase gives the selected filter)

The source sign has the four-tap mask `(+,+,-,-)`. For any observable \(f\) on the real circle, letting \(Kf(z)=f(16z)\), a four-step block gives the exact response

\[
\sum_{j=0}^{3}\omega^{J_{n+j}}f(z_{n+j})
=i\omega^7[(1+K)(1-K^2)f](z_n)
=i\omega^7[(1-K)(1+K)^2f](z_n)
\]

when \(n\equiv0\pmod4\). The filter has zero response to a constant signal, so a **source-chirality-only** detector would incorrectly declare the coherent wrong seed uninformative. Preserve the unweighted (DC) reference.

The previous original-source first-level mixer `w_n=ω^(F(n)-F(n+1))` distinguishes the parity bit \((-1)^n\). Together with \(s_n\) its two classical source registers furnish the four Walsh characters \(1,(-1)^n,s_n,(-1)^ns_n\), with exact Hadamard inversion. This is complete **four-sector readout**, not an independent physical quantum complementarity theorem. `four_walsh_channels` and its inverse implement the exact algebra.

## CH-05 — two-time and four-time source-labelled collision interferometers (PAPER-PROVED EXACT)

The minimal two-time version uses the source loop to synthesize a phase reference:

\[
Y_{n,k}(h)=\omega^{J_{n,k}}e(hz_n),\qquad e(t)=e^{2\pi it}.
\]

CH1 and \(z_{n+2}=\{16^2z_n\}\) imply

\[
\boxed{Y_{n+2,k}(h)\overline{Y_{n,k}(h)}=-e(255h z_n).}\tag{CH6}
\]

Thus the **signed complex interference** is an actual Weyl mode and the coherent two-path magnitude is

\[
\boxed{\tfrac12|Y_{n+2,k}(h)+Y_{n,k}(h)|^2
=1-\cos(2\pi255h z_n).}\tag{CH7}
\]

For a *genuine four-time carrier return*, use \(q=16^k\), \(\Phi_{n,q}=e(z_{n+q}-z_n)\), and

\[
V_{n,k}(h)=\omega^{J_{n,k}}\Phi_{n,q}^{h}.
\]

Then the original source and the same Euclidean-circle orbit give

\[
\boxed{V_{n+2,k}(h)\overline{V_{n,k}(h)}
=-e\bigl(h\,255(16^q-1) z_n\bigr),}\tag{CH8}
\]

\[
\boxed{\frac12|V_{n+2,k}(h)+V_{n,k}(h)|^2
=1-\cos\bigl(2\pi h\,255(16^q-1)z_n\bigr).}\tag{CH9}
\]

These use the chronological phase taps n, n+2, n+q, n+q+2 and the authentic unreduced q-loop source character. No independent random clock is inserted. They are *mathematical phase-coherent detectors*; positive energy is not postulated as physical Joules. Crucial accounting: the source phase **cancels after the calibrated two-path product**, leaving a real Weyl mode. This is exact target access, not by itself a new BBP arithmetic inequality or a physical field excitation.

## CH-06 — all-mode normality equivalence and one-mode R0 sufficient gate (CLASSICAL CONDITIONAL)

Fix k, so m=255(16^(16^k)-1) is a **fixed nonzero integer**. On shells B→∞, CH8–9 give

\[
\mathcal C_{B,k}(h)=B^{-1}\sum_{n=B}^{2B-1}V_{n+2,k}(h)\overline{V_{n,k}(h)}=-W_B(mh).
\]

By Weyl/Wall and preservation of base-16 normality under nonzero rational multiplication,

\[
\boxed{x\text{ is base-16 normal}\iff
\mathcal C_{B,k}(h)\longrightarrow0\quad\forall h\ne0.}\tag{CH10}
\]

A self-contained converse: if all \(W_B(mh)\to0\), then \(mx\) is normal. Any invariant subsequential empirical limit \(\mu\) for x pushes through the multiplication map \(L_m\) to Lebesgue measure. Since \(L_m\) is finite-to-one Lipschitz, every Lebesgue null set has a null image, so \(\mu\ll\mathrm{Leb}\). Invariance under \(z\mapsto16z\) forces \(\widehat\mu(h)=\widehat\mu(16^jh)\), and the Riemann–Lebesgue lemma sends all nonzero Fourier coefficients to zero. Hence \(\mu\) itself is Lebesgue. Source time labels are unchanged throughout. (This is a classical equivalent criterion, not a demonstrated decay.)

Define the four-time normalized energy \(D_{B,k}(1)=\tfrac1{2B}\sum|V_{n+2,k}(1)+V_{n,k}(1)|^2=1-\Re W_B(m)\). The deterministic elementary inequality \(|1-e(mt)|\le m|1-e(t)|\) yields

\[
\boxed{1-\Re W_B(1)\ge D_{B,k}(1)/m^2.}\tag{CH11}
\]

Therefore an independently established source-specific uniform bound \(\liminf_{B\to\infty}D_{B,k}(1)>0\) for one **fixed k** would imply the weakest open R0 statement for the authentic source. For the minimal two-time CH7, the same implication holds with \(m=255\), a much better conditioning factor. No such original-source lower bound is proved in this research. A finite isolated pulse, even at every clock precision, is not a positive-density shell margin.

## CH-07 — the hostile coboundary mutation keeps zero/isometry but kills source chirality (PROVED FINITE COUNTERMODEL)

Let \(g(t)=2t^2\) and modify the forcing by the exact telescoping coboundary

\[
\widetilde r(t)=r(t)+g(t)-16g(t-1).
\]

The new recurrence with \(\widetilde U_0=0\) has \(\widetilde U_n=U_n+g(n)\) for **every** integer n≥0. Since \(g(0)=0\), the zero seed is identical. In \(\mathbb Z_2\), \(\widetilde r\) is still an isometry: its difference quotient differs from the odd original one by \(2(t+s)-32(t+s-2)\), an even integer. If the separate BC-0 paper premise \(F(0)=0\) is accepted, the backward extension \(\widetilde F=F+g\) also preserves the exact 2-adic zero anchor and isometric clock.

Yet for the same q-loops

\[
\boxed{\widetilde J_{n,k}\equiv J_{n,k}+4n\pmod{16},
\quad (\widetilde J_{0},\widetilde J_1,\widetilde J_2,\widetilde J_3)\equiv(11,15,11,15).}\tag{CH12}
\]

Now \(\widetilde J_{n+2}=\widetilde J_n\), so the phase operator **commutes** with the two-step time shift; the central \(-I\) becomes \(+I\). The mutation changes the forcing presentation and destroys the original four-pole source passport, but **preserves the completed real π orbit**. Exact telescoping gives \(\widetilde T_n=T_n-g(n)\), hence \(\widetilde U_n+\widetilde T_n=U_n+T_n\). It is a different source presentation of the same completed target, not an authenticated original BBP forcing. This kills the claim that all source-isometric zero-pointed carriers automatically exhibit CH2. It does not by itself establish that original CH2 forces π-normality.

**Main XXVI correction, preserving the failed claim:** the original sentence “The mutation changes the real source/π target” is **REFUTED**, as already identified in #651 PS-07. For finite N the source-series correction is exactly \(16^{-N}g(N)\), which tends to zero for \(g(N)=2N^2\). For fixed n the finite J-step tail correction is \(-g(n)+16^{-J}g(n+J)\), so its limit is \(-g(n)\). The modified tail loses the original positive decaying Green-law specification; reusing the original positive \(T_n\) would be a different, incorrect completion. The commutator counterexample survives this minimum repair. Independent exact regression: `tests/test_main_xxvi_source_transport.py`.

## Verdict and proof debt

**Proved within explicitly stated algebraic/analytic hypotheses:** CH1–9, source operator anticommutation, first higher phase lift, finite four-clock Walsh factorization, exact temporal interference, mutation control and CH10/11 as *conditional* classical normality criteria. The original four-pole derivative polynomial congruences are independently machine-checked as finite arithmetic in `independent_audit.py`; the infinite normality theorem is not. A source-selected unconditional signed all-shell inequality remains **OPEN**.

**Next verdict-changing discriminating experiment:** compute the four-phase measurement jointly with the *full* exact odd-denominator/CRT winding, the real Green tail and the literal zero-seed passport; preselect fresh shells. Seek a bound on original source correlations that distinguishes the coherent wrong seed and **forces a fixed-frequency shell margin**, rather than only exact reconstruction or generic irrational escape. The coboundary mutation instead tests source-presentation dependence: preserve the completed-circle conclusion under its explicit gauge transport, or make an original-forcing hypothesis that is inapplicable to the mutant. Identical completed-circle orbits cannot be separated by a completed-phase-only detector. Use complex quadratures and full time labels. The chirality-only average has a deliberate false-negative for a coherent constant orbit; a single two-time energy channel is not a universal normality detector.

**Provenance:** original SUCC `observational_succ/duck_bbp.py` (immutable); Main XXV `docs/PI_NORMALITY_FRONTIER.md`; draft #646 (original zero and real/2-adic transport), its additive `TEMPORAL_JOINING.md`, and companion `bbp_loop_holonomy/THEOREMS.md` (LH-01 through LH-07). Wall's classical normality criteria are also restated in *Descriptive Complexity in Cantor Series*, JSL (https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/descriptive-complexity-in-cantor-series/19EAD3B2B426D3826A6DA9405DFB7D81). No academic priority, physics or full-suite verification claim.
