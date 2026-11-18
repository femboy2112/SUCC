# Borwein Autocorrelation Kernel: A Rational Squared Distance to Haar and Explicit Hex-Word Certificates

**Operation: SUCC π-Normality Competitive Crucible — 2026-11-17.**
**Source branch:** draft PR #657, original signed four-pole BBP, literal U₀=0; no original source or archival data changed.

**Originating question:** Can the impulse/Dirac-versus-Borwein convolution construction and the ordinal knowledge-volume give a *new, checkable all-mode convergence instrument* rather than repeating the open Weyl criterion? Can the observer compile a whole convolution history into one nonnegative rational energy and transmit a certified bound on every hex-digit word? The target is π normal to base 16, not finite coincidence with noise.

**Verdict:** QKB-01–07 are elementary/classical exact deductions, with independently executable rational implementations. They strengthen SUCC's finite **certificate interface**, introduce an origin-invariant **characteristic autocorrelation energy** with an explicit spectral condition number, and certify finite π-word counts from the original BBP future-tail bound. **The uniform asymptotic estimate Q_B→0 is NOT proved**; full π normality remains OPEN. These are source-typed applications of convolution/Parseval/Erdős–Turán, not claims of mathematical priority.

## 1. One source, one reference; no random seed

Keep precisely
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
The imported/independently rederived classical BBP identity gives \(x=\pi/16\), \(U_{2B}+T_{2B}=16^{2B}x\), \(0<T_{2B}<r(2B+1)/15\).

For a shell \(B\ge1\), the *one original rational terminal endpoint* gives \(B\) phase observations:
\[
\boxed{q_{B,k}=\frac{U_{2B}}{16^k}\pmod1,\quad 1\le k\le B.}\tag{QKB1}
\]
The genuine phases \(y_{B,k}=16^{2B-k}x\bmod1\) differ by \(16^{-k}T_{2B}\). All \(q_{B,k}\) are rational and retain the *literal original source*; any other seed or forcing is a hostile countermodel, not an alternate original history.

Use the proven two-rectangle Borwein leakage kernel from [BSI](BORWEIN_SWEPT_IMPULSE_BBP.md):
\[
\boxed{L(\theta)=c\left(\|\theta\|_{\mathbb T}-\delta\right)_+^2,\quad
c=\frac{162}{289},\ \delta=\frac1{18},\ \ell_0:=\int_{\mathbb T}L=\frac{256}{7803}.}\tag{QKB2}
\]
The two auxiliary uniforms/rectangular pulses define a test **observer filter**, not new randomness or information injected into BBP.

Define the source-rational swept signal and its centered version:
\[
\widehat J_B(\alpha)=\frac1B\sum_{k=1}^B L(q_{B,k}-\alpha),\quad
F_B(\alpha)=\widehat J_B(\alpha)-\ell_0.
\]

## 2. An exact rational source-to-Haar squared energy

**QKB-01 (EXACT, origin-independent positive energy):**
\[
\boxed{\mathcal V_B:=\int_{\mathbb T}|F_B(\alpha)|^2d\alpha
=\sum_{h\in\mathbb Z\setminus\{0\}}
|\widehat L(h)|^2
\left|\frac1B\sum_{k=1}^Be(hq_{B,k})\right|^2.}\tag{QKB3}
\]
Here \(e(t)=e^{2\pi it}\), and Parseval gives the equality. Every summand is **nonnegative**, with **strictly positive weight for each h≠0**, since BSI proved \(\widehat L(h)\ne0\) for every such h. The energy is invariant under a *common circle rotation* of all phase data, unlike a single anchored R0 phase-loss reading.

The energy is also a **finite exact rational number**, despite the infinite Fourier representation: each \(\widehat J_B\) is continuous, piecewise quadratic, with rational breakpoints at the rational phases translated by \(0,\pm\delta,1/2\). Squaring and integrating piecewise quartic rational polynomials produces an exact Fraction. See [the executable module](../../../observational_succ/borwein_quantitative_certificate.py).

Equivalently define the circle autocorrelation kernel
\[
K(\tau):=\int_{\mathbb T}L(a)L(a-\tau)da.
\]
Then
\[
\boxed{
\mathcal V_B=\frac1{B^2}\sum_{k,\ell=1}^BK(q_{B,k}-q_{B,\ell})-\ell_0^2.
}\tag{QKB4}
\]
Every K value at a rational shift is rational. Its Fourier coefficients are \(\widehat K(h)=|\widehat L(h)|^2>0\) for every integer h, including h=0. The kernel is strictly positive definite on finite sets of distinct circle points; its associated mean embedding is *characteristic*, and \(\mathcal V_B\) is its squared distance between the BBP shell empirical measure and Haar. This is a classical MMD/Parseval identity, not a new physical source energy or a probability assigned to π.

**Finite strictness:** for every finite B, \(\mathcal V_B>0\), since a finite atomic empirical measure cannot equal Haar and the kernel has all nonzero Fourier weights. Strict finite positivity does **not** forbid \(\mathcal V_B\to0\); equidistributed sequences have exactly that behavior.

## 3. Exact finite RATIONAL spectral gain lower bound

For integer \(h\ne0\), BSI established the nonvanishing coefficient
\[
\widehat L(h)=\frac{648}{289}
\left[
\frac{\frac49(-1)^h}{(2\pi h)^2}
+\frac{\sin(\pi h/9)}{(2\pi h)^3}
\right].
\]
By the reverse triangle inequality, \(\pi>3\), \(\pi<22/7\), and \(|h|\ge1\),
\[
\begin{aligned}
|\widehat L(h)|&\ge\frac{162}{289\pi^2h^2}
\left(\frac49-\frac1{2\pi|h|}\right)\\
&>\frac{162}{289\pi^2h^2}\left(\frac49-\frac16\right)
=\frac{45}{289\pi^2h^2}\\
&>\boxed{\frac{2205}{139876\,h^2}=:\frac{c_\star}{h^2}.}
\end{aligned}\tag{QKB5}
\]

**QKB-02 (PROVED explicit all-mode gain):** the same single filter sees EVERY nonzero Fourier character with a declared inverse condition-number growth at most \(h^2/c_\star\). A tiny filtered response does not by itself make the underlying characters small at arbitrary *unbounded* h without paying that growth.

## 4. Original BBP tail transfers the rational energy to the true orbit

Let
\[
J_B(\alpha)=B^{-1}\sum_{n=B}^{2B-1}L(16^nx-\alpha),\quad
\epsilon_B=\frac{16r(2B+1)}{7225B}=O(B^{-3}).
\]
The original authenticated BBP source/tail and \(\operatorname{Lip}L=144/289\) give
\[
\sup_\alpha|J_B(\alpha)-\widehat J_B(\alpha)|<\epsilon_B.
\]
Write \(V_B^{\rm true}=\int|J_B(\alpha)-\ell_0|^2d\alpha\).

**QKB-03 (EXACT quantitative source transport):**
\[
\boxed{
\left|\sqrt{V_B^{\rm true}}-\sqrt{\mathcal V_B}\right|\le\epsilon_B.
}\tag{QKB6}
\]
Proof: the reverse triangle inequality in \(L^2(\mathbb T)\), bounded by the known \(L^\infty\) phase-shadow error.

Hence every actual original-source Weyl sum at **every nonzero integer frequency** obeys
\[
\boxed{
|W_B(h)|\le
\min\left(1,\frac{139876}{2205}h^2
(\sqrt{\mathcal V_B}+\epsilon_B)\right).
}\tag{QKB7}
\]
Proof: the absolute value of the h-th Fourier coefficient of the centered true swept response is \(|\hat L(h) W_B(h)|\); Cauchy–Schwarz bounds it by \(\|J_B-\ell_0\|_2\); use QKB5–6.

No estimates from a stochastic π model, unknown RH zeros, randomized seeds or independence assumptions appear. **All finite source input is rational; the use of \(\sqrt{\mathcal V_B}\) is controlled by a certified rational upper root when implementing the bound.**

## 5. A fully quantitative HEX-WORD discrepancy transfer

Let \(\mathfrak D_B\) denote the supremum of interval-frequency errors for the **true completed BBP orbit** \(16^nx\), \(B\le n<2B\).

The explicit Erdős–Turán discrepancy inequality
\[
\mathfrak D_B\le\frac3{H+1}+3\sum_{h=1}^H\frac{|W_B(h)|}{h}
\]
holds for each integer \(H\ge1\) (see Androma theorem #9093 and the established Kuipers–Niederreiter/Montgomery family of estimates). Substituting QKB7 yields

**QKB-04 (PROVED, source-certifiable universal digit-frequency bound):**
\[
\boxed{
\mathfrak D_B\le
\frac3{H+1}+
\frac{69938}{735}H(H+1)
\left(\sqrt{\mathcal V_B}+\epsilon_B\right),
\quad H=1,2,\ldots.
}\tag{QKB8}
\]

For any hexadecimal word \(w\) of length \(k\), its digit-cylinder corresponds to an interval of length \(16^{-k}\). Therefore
\[
\boxed{
\left|\frac{\#\{\text{occurrences of }w\text{ starting at shell clocks}\}}B
-16^{-k}\right|\le\mathfrak D_B,
}\tag{QKB9}
\]
**simultaneously for every such word**. A rational certificate \(q\ge\sqrt{\mathcal V_B}\), verified by \(q\ge0,q^2\ge\mathcal V_B\), makes the right-hand side of QKB8 itself entirely rational and independently checkable.

Choosing \(H\asymp(\sqrt{\mathcal V_B}+\epsilon_B)^{-1/3}\) proves the *conditional* quantitative convergence rate
\[
\mathfrak D_B=O((\sqrt{\mathcal V_B}+\epsilon_B)^{1/3}),
\]
with absolute constants. **No rate or even convergence of \(\mathcal V_B\) is proven for original π.** For the finite shells currently tested, this general upper bound can exceed 1 and is not claimed to be a practically sharp certificate.

## 6. An exact one-scalar full-normality gate

**QKB-05 (PROVED EQUIVALENCE, OPEN source application):**
\[
\boxed{
\pi\text{ normal to base }16
\iff
\lim_{B\to\infty}\mathcal V_B=0.
}\tag{QKB10}
\]

Forward proof: normality means each dyadic-shell empirical circle measure converges weakly to Haar. The translated continuous test family \(L(\cdot-\alpha)\) is uniformly bounded and equi-Lipschitz, so \(J_B(\alpha)\to\ell_0\) uniformly in \(\alpha\). The original source shadow error \(\epsilon_B\to0\) then gives \(\mathcal V_B\to0\).

Reverse proof: if \(\mathcal V_B\to0\), QKB7 gives \(W_B(h)\to0\) for each fixed h≠0. Weyl's criterion yields base-16 normality. Equivalently QKB8 gives vanishing interval discrepancy by first choosing large H and then B.

This is a **new exact rational squared-kernel representation**, not an independent proof of its zero limit. The final required arithmetic claim is the \(\forall\varepsilon\exists B_0\forall B\ge B_0\) estimate \(\mathcal V_B<\varepsilon\).

## 7. Source-certified individual digits, rather than floating π samples

For original shell clock n and desired hexadecimal word length k, compute from **only the rational source**
\[
z_n=\frac{U_{2B}}{16^{2B-n}},\quad
0<16^n x-z_n<
b_n:=\frac{r(2B+1)}{15\cdot16^{2B-n}}.
\]
Let \(M=16^k\).

**QKB-06 (PROVED finite exact word-certificate test):** if
\[
\boxed{\lfloor M z_n\rfloor=\lfloor M(z_n+b_n)\rfloor,}
\tag{QKB11}
\]
then the actual \(k\)-hexadecimal-digit word beginning at this clock is certified exactly as \(\lfloor Mz_n\rfloor\bmod M\). If not, mark the position **ambiguous**, rather than guessing from floating precision.

The pure Fraction implementation returns lower counts for every word and the list of unresolved clocks. With u unresolved clocks, any actual word count is bounded between its known count and known count+u. This remains valid even if the test occasionally flags an unnecessary ambiguity.

**QKB-07 (OBSERVED exact in-sample source certificates):** for B=32,64,128, the genuine four-pole zero-seeded source certifies **every tested clock for every k=1,2,3,4**: zero ambiguities. These are direct source-validated finite blocks, not proof of limiting word frequencies.

## 8. Hostile controls and next proof instrument

- **True locked alternative:** an identically fixed circle phase has \(\mathcal V_B\equiv335872/304434045>0\) at every B. A nonunit fixed phase (e.g. x=1/15) gives the *same* positive energy: the full-normality detector correctly rejects it even though original R0 can hold.
- **Almost-uniform finite grids:** equally spaced rational points have \(\mathcal V_B>0\) at each finite sample but approach zero as grid size increases. This confirms the correct completion interpretation.
- **Source forgery:** a changed seed or a positive decreasing matched locked forcing must be handled with its *own* source passport; no random source is substituted for the original BBP r(n).
- **Periodized convolution:** L is an explicitly wrapped circle kernel derived from the two-pulse real Borwein leakage. It is NOT the positive source-Mellin mask Q(t) itself. The still-open intertwinement from **source impulses** to **radix carry/winding** is not paid by merely composing circle kernels.
- **Higher observer:** an inherited exact finite rational \(\mathcal V_B\) and the per-word tail proofs are reusable certificates. A sequence of increasingly precise finite certificates is **not** automatically a finite universal proof of \(\mathcal V_B\to0\).
- **New quantitative hole:** obtain an *independent source-derived upper bound* for \(\mathcal V_B\to0\) (ideally a rate), or a source-valid inequality between it and a different already-bounded arithmetic quantity, rejecting locked/sparse/near-seed controls. The bounded-Gamma Mellin tower is available as a proposed **source-generation instrument**, not an assumed normality theorem.

## Competitive proof acceptance contract

For a claimed π-normality proof from any agent (including Gemini Argon), ask for a finite manuscript that:
1. Retains the original four signed BBP poles, literal zero seed and integer winding, or proves an equivalent authentic source representation.
2. Establishes a uniform all-late-shell bound strong enough to make \(\mathcal V_B\to0\) or directly proves every nonzero Weyl coefficient tends to zero **without assuming normality/RH or an unverified oracle**.
3. Supplies the original-source transport, its quantifiers, a source-typed signed bound, and hostile controls against known locked, near-locked and matched alternative sources.
4. Distinguishes independently verified mathematical proof from finite numeric fits, source-dependent changes of seed, and same-model repeated audits.

A verified proof passing those conditions would win the friendly research bet. Claiming victory because a new rational energy *represents* normality does not.

## Exact reproducibility and provenance

Implementation: [observational_succ/borwein_quantitative_certificate.py](../../../observational_succ/borwein_quantitative_certificate.py); tests: [tests/test_borwein_quantitative_certificate.py](../../../tests/test_borwein_quantitative_certificate.py); [execution and hostile validation](BORWEIN_QUANTITATIVE_VALIDATION.md). The combined local Borwein test family (including prior PR #657's 9 tests) passed 23/23 in the exact local files, with per-file Git blob hashes retained in the receipt.

References: [Prior full-mode two-pulse kernel](BORWEIN_SWEPT_IMPULSE_BBP.md), [Source Mellin/Gamma knowledge-volume ascent](ORDINAL_MELLIN_GAMMA_OBSERVER_ASCENT.md), [Source-specific rational endpoint/phase tail](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), [Original SUCC Method](../../../docs/METHOD.md), [Erdős–Turán inequality](https://androma.org/theorems/9093), [Classical Borwein integral convolution](https://people.phy.cam.ac.uk/dag9/MathsMethods/l04-borwein.pdf). This is not an independent mathematical-physics realization of QM/GR, not a zeta spectral proof and not an all-mode normality theorem.
