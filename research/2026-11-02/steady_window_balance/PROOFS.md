# OPERATION STEADY WINDOW BALANCE — original BBP residual, finite-state limit, and deterministic antiphase pairing

**2026-11-02. RESEARCH ONLY.** Research child of SUCC [#477](https://github.com/femboy2112/SUCC/pull/477) at exact parent SHA 66d85548755920603911f086c5d26addf91c797c; #477 itself stacks on #475/#474/#473/#471/#470/#468 and merged Main XIX. Sibling [#476](https://github.com/femboy2112/SUCC/pull/476) inspected READ-ONLY: it already proves original odd-denominator non-antiphase, arbitrary antiphase permutations, and a slow-mesh Fejér sufficient criterion. Do not claim those as original. Keep the ORIGINAL BBP four signed poles, literal U₀=0, full selected real embedding, finite source heights and historical claim contracts unchanged. **π normality remains OPEN.**

## SWB-01. Positive analytic residual ≠ accumulated dephasing (decisive counterexample)

Use the source-inherited finite/continuum defect \(D_n=H_n-\log n-\gamma\) and authentic BBP tail \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\). Prior #473/#474 established

\[
W_n=D_n^2/16-T_n>0,\qquad W_n\sim13/(1536n^3).
\]

Consequently \(\sum_{n\ge2}W_n<\infty\). Construct an auxiliary circle trajectory (NOT the actual BBP orbit) with phase increments \(\theta_{n+1}-\theta_n=W_n\). Then \(\theta_n\to\theta_\infty\), and by Cesàro summation its empirical character mean approaches \(e(h\theta_\infty)\), modulus 1 for every integer h. Positive nonzero residual is therefore INSUFFICIENT for dephasing. The function W_n is a discrepancy between two scalar analytic constructions, **not** a proved increment of the actual selected BBP phase, and must not be quietly substituted into it.

There is even an **original-four-pole, same-forcing** control. Put \(\alpha=\pi/16\); retain r(n) exactly but choose the distinct real seed \(s=1/5-\alpha\). Its phase orbit is

\[
U_n(s)=16^n/5-T_n\equiv1/5-T_n\pmod1\longrightarrow1/5
\]

because \(16\equiv1\pmod5\). The source and W_n are unchanged yet the empirical measure tends \(\delta_{1/5}\), with \(|N^{-1}\sum e(hU_n(s))|\to1\). This REFUTES a source- or residual-only rule “residual >0 + steady state ⇒ Haar”. It does NOT refute a theorem genuinely using the original marked zero seed.

## SWB-02. What steady state DOES imply: radix-16 invariance, not Haar

Let \(x_n=\{U_n\}\) on \(\mathbb T\), \(F_n(x)=16x+r(n+1)\), \(T(x)=16x\bmod1\), and \(\mu_N=N^{-1}\sum_{n=0}^{N-1}\delta_{x_n}\). For any continuous circle-Lipschitz test f, with Lipschitz constant L and sup norm M, telescoping gives

\[
\left|\int f\circ T\,d\mu_N-\int f\,d\mu_N\right|
\le \frac{2M+L\sum_{j=1}^Nr(j)}N=O_f(N^{-1}).
\tag{SWB-02}
\]

The authentic r(j)>0 is summable by the original positive Gamma source integral. Any weak-* subsequential limit of the selected empirical measures is therefore T-invariant (by compactness, a limit exists along some subsequence). But T has non-Haar invariant measures such as \(\delta_{1/5}\), and all its finite periodic cycles, so asymptotic invariance does NOT imply uniqueness, mixing, dephasing or normality. Exactly this distinction is the user's “leave a snapshot to steady state” missing hypothesis: one needs *selection of Haar among the invariant measures*.

## SWB-03. EXACT time-aligned in/out-window cancellation certificate

Let \(e(x)=\exp(2\pi ix)\) and \(h\in\mathbb Z\setminus\{0\}\). For any source time start a and adjacent equal-length time windows \([a,a+L)\), \([a+L,a+2L)\), define their exact mean HALF-TURN misalignment

\[
P_{a,L}(h)=\frac1L\sum_{n=a}^{a+L-1}
\left\|h(U_{n+L}-U_n)-\frac12\right\|_{\mathbb T}\in[0,1/2].
\]

Pair time n with n+L and apply \(|e(y)+e(x)|\le2\pi\|y-x-1/2\|_{\mathbb T}\). This yields

\[
\boxed{\frac1{2L}\left|\sum_{n=a}^{a+2L-1}e(hU_n)\right|\le\pi\,P_{a,L}(h).}
\tag{SWB-03}
\]

The full ORIGINAL four-pole forcing explicitly determines the gap:

\[
U_{n+L}-U_n=(16^L-1)U_n+
F(n,L),\quad
F(n,L)=\sum_{j=1}^L16^{L-j}r(n+j).
\]

So the exact *assumption* required for cancellation by this PARTICULAR chronological matching is that \(P_{a,L}(h)\to0\) on sufficiently many source-selected windows. The existence of W_n>0 does NOT establish it. Indeed the fresh exact original-source holdouts below show costs near 1/4, not near 0, for this preassigned same-offset time pairing.

## SWB-04. EXACT phase-SECTOR window pairing, with correct even-harmonic parity

A better interpretation of “in-phase/out-of-phase windows line up” pairs **phase sectors** rather than fixed time offsets. Take an arbitrary N-point circle list \(x_n\) (eventually the authentic \(\{U_n\}\)), choose a dyadic mesh \(M=2^q\), and let

\[
c_d=\#\{n<N:\lfloor M x_n\rfloor=d\},\qquad d=0,\ldots,M-1.
\]

Fix h≠0 and factor \(h=2^v g\), g odd. Assume \(M\ge2^{v+1}\). Put \(t=M/2^{v+1}\). The bins form disjoint antiphase pairs

\[
(d,d+t)=\bigl(a+2jt,\ a+(2j+1)t\bigr),
\quad 0\le a<t,\quad0\le j<2^v.
\]

For bin center \(\xi_d=(d+1/2)/M\),

\[
\boxed{e(h\xi_{d+t})=-e(h\xi_d)}
\]

**exactly**, since \(h\,t/M=g/2\) is a half-integer. Therefore define the precise **selected window occupancy imbalance**

\[
\boxed{\mathcal A_{N,M}(h)=\frac1N
\sum_{\mathrm{antiphase\ bins}(d,d+t)}|c_d-c_{d+t}|.}
\tag{SWB-04a}
\]

Replacing original points by bin centers costs at most \(\pi|h|/M\) in normalized complex amplitude. The paired center contributions cancel algebraically, yielding the rigorous, deterministic theorem

\[
\boxed{\left|\frac1N\sum_{n<N}e(hx_n)\right|
\le\mathcal A_{N,M}(h)+\frac{\pi|h|}{M}.}
\tag{SWB-04b}
\]

This is the user's desired “line up and cancel trivially” identity in exact form. It needs NO randomness, Galois averaging or probabilistic independence. But proving \(\mathcal A_{N,M_N}(h)\to0\) for an explicit diverging mesh and every fixed h, along ALL original BBP prefixes, is a new selected-source statement and remains OPEN. As with #476's earlier general antiphase-permutation criterion, this statement is *stronger* than normality for many rapidly growing prescribed mesh schedules, and is a conditional cancellation contract, not an original-source estimate.

**Critical even-harmonic trap:** a naïve global half-circle shift \(d\to d+M/2\) flips odd harmonics but does NOTHING for even harmonics. For h=2, the true antiphase shift is M/4; for h=16, it is M/32. A sequence can balance half-circle counts exactly yet have an h=2 Weyl coefficient equal to 1. The 2-adic exponent v selects the correct pairs.

## SWB-05. Connect the occupancy pair criterion to existing positive collision machinery

Let \(E_{N,M}=(M/N^2)\sum_d c_d^2\ge1\) be the exact integer histogram energy from earlier #473/#475. Put \(\delta_d=c_d-N/M\). Then

\[
\sum_{\mathrm{pairs}}(c_d-c_{d+t})^2
\le2\sum_d\delta_d^2,
\]

and Cauchy across M/2 pairs yields

\[
\boxed{\mathcal A_{N,M}(h)^2\le E_{N,M}-1.}\tag{SWB-05}
\]

Thus a **near-Haar** collision energy \(E_{N,M_N}\to1\) at a diverging mesh implies antiphase balance for every fixed h and consequently normality. But the newer #475/#476 SUCC sufficient hypotheses only require slower energy growth such as \(E=o(\log M)\), so they do NOT establish \(\mathcal A\to0\). The antiphase criterion is a useful alternative, not a newly proved strengthening of the actual arithmetic source estimate.

The BBP source odd-denominator fact was already proved in #476 WM-03: combining the two even poles gives

\[
r(n)=\frac4{8n-7}-\frac1{8n-3}
-\frac{3n-1}{(2n-1)(4n-1)}.
\]

Every denominator is odd, hence all original \(U_n\) have odd reduced denominator. Exact equal-weight two-term antiphase \(e(hU_n)=-e(hU_m)\) is therefore IMPOSSIBLE: it would require \(h(U_n-U_m)\equiv1/2\pmod1\). Approximate antiphase BIN matching remains permitted, and multiway root-of-unity polygons can cancel exactly. This rules out one overly strong “trivial exact pair” reading, not the source-conditioned approximate-window proposal.

## SWB-06. Fresh original-source holdouts: what actually lines up?

Preregistered before inspection in PREREGISTRATION.md: exact original rational source, A=2048 and 4096, temporal h=1,2,16 and spatial bins M=16,64,256. The first naïve Fraction summation exceeded practical large-gcd/string serialization resources. An EXACT independent common odd-denominator modular lift resolved the access bottleneck; it is independently cross-checked against direct Fraction states and costs for finite n. All temporal values are certified by a single exact rational \(S/(2DL)\) with a published SHA256 digest of full exact numerator and denominator and interval width 10^-10; executable probe.py --raw reproduces their full hex representation.

| A | chronological P_{A,A/2}(1) (rigorous decimal interval center) | phase-window A_{A,64}(1) (exact) | phase-window A_{A,256}(1) (exact) |
|---:|---:|---:|---:|
| 2048 | 0.2472390354 | 87/1024 ≈0.08496 | 3/16=0.1875 |
| 4096 | 0.2496578456 | 149/2048 ≈0.07275 | 151/1024 ≈0.14746 |

The corresponding chronological h=2,16 costs at both epochs also lie near 1/4. All preregistered **finite** diagnostic thresholds pass. The two types of window matching exhibit materially different behavior. This is NOT asymptotic evidence that the spatial imbalance tends to zero; no blind independent expert/CI review is inferred.

Hostile controls: same ORIGINAL forcing but completed coherent real seed q=1/5 has each large-epoch phase in a single fixed bin, spatial \(\mathcal A=1\), and chronologically preassigned half-turn cost tending 1/2. Synthetic exactly balanced phase-sector bins give \(\mathcal A=0\), while a half-circle-balanced h=2 adversary exposes the parity error.

## Next falsifiable proof-producing target

Try to prove, for the original source and every fixed nonzero h, an explicit diverging dyadic mesh M_N with \(\mathcal A_{N,M_N}(h)=o(1)\) along ALL N; or prove the weaker existing #476 logarithmic-mesh source collision \(E_{A,m_A}=o(\log m_A)\) on dyadic source epochs with its already paper-proved all-prefix transport.

Probe on genuine newborn-prime p clean epochs and full p-free real cofactor, preserving the original carry. Do not infer the balance from the sign of W_n, mere T-invariance, exact prime nonvanishing, geometric projection, Galois averaging, or finite probe fits. At least one NEW original zero-seed, all-horizon signed/cofactor inequality is still needed.

**Ledger:** SWB-01 analytic residual-only implication REFUTED by summable counterexample; SWB-02 asymptotic stationarity but nonunique invariant measures PROVED; SWB-03/04/05 universal pairing identities PROVED (same mathematical family as earlier #476); source-specific SWB-06 finite OBSERVED; selected all-prefix window-balancing premise UNVERIFIED; π base-16 normality and RH OPEN.
