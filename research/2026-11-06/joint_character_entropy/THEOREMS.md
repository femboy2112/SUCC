# Source-authenticated joint action–observation characters: finite-state entropy, periodic gauge rigidity and a reversible BBP observer

**2026-11-06 | Research-only, additive child of SUCC PR #525.** The original four signed BBP poles and the literal zero initial state are **immutable**. These results are elementary proofs or classical information-theory consequences in a new SUCC organization; no worldwide priority or formal Lean proof is asserted. **π normality, selected signed Weyl cancellation and RH remain OPEN.**

## 0. The exact arithmetic carrier and its certified source stream

Let
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1),\quad T_n=\sum_{j\ge1}16^{-j}r(n+j).
\]
The established BBP identity gives \(T_0=\pi/16\). With \(z_n=\{U_n+T_n\}\), the exact Green completion is
\[
\boxed{z_n=\{16^n\pi/16\},\qquad z_{n+1}=\{16z_n\}.}\tag{J0}
\]
These are genuinely distinct from the uncompleted rational states \(x_n=\{U_n\}\): digit boundaries may be crossed by adding \(T_n\), and **normality of the first digits of \(x_n\) is not silently identified with normality of π**.

The source-only rational tail enclosure, for \(n\ge0,d\ge1\), is
\[
L_{n,d}=\sum_{j=1}^{d}16^{-j}r(n+j),\qquad
\boxed{T_n\in\big[L_{n,d},\ L_{n,d}+\tfrac{16^{-d}}{15(n+d+1)^2}\big]}.\tag{J1}
\]
Proof: the omitted tail is \(16^{-d}T_{n+d}\), and the authenticated rational inequality \(0<r(m)<1/m^2\) for every \(m\ge2\) gives \(0<T_{n+d}<1/[15(n+d+1)^2]\) since \(n+d\ge1\). The \(n=0\) step includes the exceptional \(r(1)=47/15\) **exactly** among the finite terms, never under the \(1/n^2\) bound.

For each \(n\), if the interval \(x_n+[L_{n,d},R_{n,d}]\) stays in a single base-16 one-digit cell on the *unwrapped* line, its cell label modulo 16 certifies \(d_n=\lfloor16z_n\rfloor\). The interval can be refined to resolve any actual \(n\): because \(z_n\) is irrational (π is irrational), it is never on a radix-cell boundary. This is a finite algorithm for each digit, not a uniform bound on its stopping time and not a proof of digit frequencies.

## 1. JC-01 — source-authenticated joint character and its symbolic slice (PROVED LOCAL)

Given realized circle phases \(z_n\), a causal action \(a_n\in\mathbb T\) and observations \(y_n=z_n+a_n\pmod1\), retain the **joint** record
\[
\Gamma_N=\frac1N\sum_{n<N}\delta_{(a_n,y_n)}.
\]
The exact gauge-decoded character is
\[
\boxed{\int e^{2\pi ih(y-a)}\,d\Gamma_N(a,y)=\frac1N\sum_{n<N}e^{2\pi ihz_n}}\tag{J2}
\]
for all integers \(h\), with no probabilistic assumptions. This is PR #525 RG9–RG12 and is a *faithful transport identity*, not cancellation.

A finite-memory observer may choose the special **digit-lattice gauge**
\[
a_n=\frac{q_n+\sigma_n}{16}\pmod1,\quad q_n\in\{0,\ldots,15\},\quad\sigma_n\in\{0,\ldots,6\}.
\]
Since \(d_n=\lfloor16z_n\rfloor\), its observed first digit is **exactly**
\[
\boxed{c_n=\lfloor16y_n\rfloor=(d_n+q_n+\sigma_n)\bmod16.}\tag{J3}
\]
This is valid even if the unobserved fractional part of \(z_n\) is arbitrarily close to 1. The action changes the *representation*, not π or the original source dynamics.

## 2. JC-02 — PERIODIC-CHART RIGIDITY, even with vanishing source forcing (PROVED LOCAL)

**Theorem.** Let \(b\ge2\), \(x_{n+1}=\{bx_n+\epsilon_{n+1}\}\) with \(\epsilon_n\to0\), and let \(a_n=a_{n\bmod p}\) be any fixed periodic sequence of circle rotations, \(p\ge1\). Then
\[
\boxed{\{x_n+a_n\}\text{ is Haar-equidistributed}\ \Longleftrightarrow\ \{x_n\}\text{ is Haar-equidistributed}.}\tag{J4}
\]
The same holds if the actual actions \(a'_n\) satisfy \(N^{-1}\sum_{n<N}d_{\mathbb T}(a'_n,a_{n\bmod p})\to0\), because the two observation streams have the same weak limits by the uniform continuity of circle test functions.

**Proof.** Choose any subsequence \(N_j\to\infty\) along which all \(p\) residue-class empirical measures of \(x_n\) converge weakly to \(\mu_r\) (compactness of probabilities on the circle). The residue-class measures satisfy
\[
(E_b)_*\mu_r=\mu_{r+1\bmod p},\quad (E_{b^p})_*\mu_r=\mu_r,\qquad E_b(x)=bx\bmod1,\tag{J5}
\]
because each shift by one time step preserves class counts up to \(O(1/N_j)\), and the source perturbation tends to zero (for fixed \(p\), compositions differ by \(o(1)\)).

If the observed marginal tends to Haar \(\lambda\), then
\[
\lambda=\frac1p\sum_{r=0}^{p-1}(\tau_{a_r})_*\mu_r.
\]
All summands are **positive measures**, hence each translated class measure is dominated by \(p\lambda\). Translation preserves Haar, so \(\mu_r\ll\lambda\) with an \(L^1\) density. From (J5),
\(\widehat\mu_r(h)=\widehat\mu_r(b^{pk}h)\) for all \(k\ge0\). By the Riemann–Lebesgue lemma all nonzero Fourier coefficients vanish; \(\mu_r=\lambda\). Thus all subsequential class limits are Haar and the raw empirical measures converge to Haar.

Conversely, if the raw empirical measures tend to Haar, the same domination and invariant-class argument applied to \(\lambda=p^{-1}\sum\mu_r\) forces every \(\mu_r=\lambda\); translating them preserves Haar. ∎

**Sharp scope.** This does NOT hold for arbitrary time-dependent observation charts. PR #525 RG-06 constructs an irrational staircase with only \(O(\sqrt N)\) chart switches making the constant zero orbit appear Haar. Such a chart is **not** Cesàro-asymptotic to any fixed periodic chart. Periodic marginal Haar is trustworthy; a general adaptive *unlogged* marginal is not.

## 3. JC-03 — rational-seed source-gauge equivalence (CLASSICAL, independent local proof)

For any rational seed \(s\in\mathbb Q\), the authentic same-source circular orbits satisfy
\[
x_n(s)=x_n(0)+a_n\pmod1,\qquad a_n=16^n s\pmod1.
\]
Write the denominator of \(s\) as \(2^eq\) with \(q\) odd. After at most \(\lceil e/4\rceil\) steps the 2-power part disappears. The remaining phase has period dividing \(\operatorname{ord}_q(16)\) (\(q=1\): eventually zero). By JC-02, and because the true source \(r(n)\to0\),
\[
\boxed{x_n(s)\text{ Haar-generic}\iff x_n(0)\text{ Haar-generic}\quad\forall s\in\mathbb Q.}\tag{J6}
\]
The corresponding completed numbers differ by the rational translation \(s\), so this is the classical rational-addition invariance of normality, attributed to Wall. It is not a new global normal-number theorem. Citation: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/descriptive-complexity-in-cantor-series/19EAD3B2B426D3826A6DA9405DFB7D81 (Theorem 1.3).

**Crucible consequence:** a rational initial seed such as \(s=1/5\) is *not* a known nonnormal completion; its normality verdict is exactly as unknown as the original. The coherent periodic ghost completion \(\beta=1/5\) instead uses \(s=1/5-\pi/16\), which is irrational. The zero-seed authentication is not by itself a source-selected signed normality theorem. Arbitrarily long finite behavior can still be approximated by rational seeds, so rationality does not resolve a finite-observer probe gap.

## 4. JC-04 — FINITE-STATE SOURCE-ENTROPY TRANSFER (CLASSICAL INFORMATION THEORY, PROVED LOCAL)

Take any infinite digit stream \(D=(d_n)_{n\ge0}\) over \(\{0,\ldots,b-1\}\), any *explicit* finite-alphabet auxiliary source stream \(\Sigma=(\sigma_n)_{n\ge0}\), and a deterministic **synchronous causal** Mealy machine with \(Q\) internal states:
\[
c_n=f(q_n,d_n,\sigma_n),\qquad q_{n+1}=g(q_n,d_n,\sigma_n).
\tag{J7}
\]
It emits exactly ONE symbol in the same \(b\)-digit alphabet per input digit. It has no unaccounted oracle tape, unbounded hidden state, random seed of growing information, or independent time-dependent output sequence. Let \(P_{W,N}^{(k)}\) denote the overlapping empirical length-\(k\) block distribution for a finite prefix \(W_0,\ldots,W_{N-1}\), with Shannon entropy in **nats** \(H(P)=-\sum P\log P\). Write
\[
\Delta_{W,N}(k)=k\log b-H(P_{W,N}^{(k)})\ge0.
\tag{J8}
\]

**Finite theorem (precise quantifiers):** for **every** \(N\ge L\ge k\ge1\) with \(k\mid L\), any input/source/output and any deterministic machine as above, set
\[
\varepsilon=\frac{L-k}{N-k+1},\quad h_2(\varepsilon)=-\varepsilon\log\varepsilon-(1-\varepsilon)\log(1-\varepsilon),\quad h_2(0)=h_2(1)=0.
\]
Then
\[
\boxed{\Delta_{D,N}(k)\le\frac{k}{L}\Big[\Delta_{C,N}(L)+H(P_{\Sigma,N}^{(L)})+\log Q\Big]
+h_2(\varepsilon)+\varepsilon k\log b.}\tag{J9}
\]

**Derivation.** Choose a uniformly random starting index \(I\in\{0,\ldots,N-L\}\). Since the machine is causal, the output word \(C_{I:I+L}\) is a deterministic function of the input word \(D_{I:I+L}\), the source word \(\Sigma_{I:I+L}\), and the observer state \(q_I\). Therefore
\[
H(P_{C,N}^{(L)})\le H(P_{D,N}^{(L)})+H(P_{\Sigma,N}^{(L)})+\log Q.
\tag{J10}
\]
Partition the length-\(L\) input word into \(m=L/k\) consecutive \(k\)-blocks. By entropy subadditivity its entropy is bounded by the sum of the chunk entropies. The start index of each chunk is uniform on a contiguous subinterval of \(\{0,\ldots,N-k\}\), of length \(N-L+1\); that differs in total variation by exactly \((L-k)/(N-k+1)=\varepsilon\) **at the index level** from uniform sampling of all \(k\)-block starts. Applying the deterministic block map cannot increase TV. For any alphabet size \(b^k\), the elementary entropy continuity bound gives
\[
H(\text{each chunk})\le H(P_{D,N}^{(k)})+h_2(\varepsilon)+\varepsilon k\log b.
\]
Combine with (J10), write the entropies as maximal entropy minus deficit, divide by \(m\), and obtain (J9). Every step is finite, elementary and independent of a probability model for π. ∎

**Asymptotic corollary.** Suppose the auxiliary source satisfies
\[
\lim_{L\to\infty}\frac{1}{L}\limsup_{N\to\infty}H(P_{\Sigma,N}^{(L)})=0,
\tag{J11}
\]
and the emitted digit word \(C\) is **normal in base \(b\)** (ALL fixed-length block frequencies tend to \(b^{-L}\), not just one-symbol frequencies). Fix \(k\), let \(N\to\infty\) in (J9) with each fixed multiple \(L\) of \(k\). Then \(\varepsilon\to0\), \(\Delta_{C,N}(L)\to0\), so \(\limsup_N\Delta_{D,N}(k)\le (k/L)(\limsup_N H(P_{\Sigma,N}^{(L)})+\log Q)\). Let \(L\to\infty\) along multiples of \(k\). This forces \(\Delta_{D,N}(k)\to0\), and finite-alphabet maximal entropy is attained **only** at the uniform length-\(k\) distribution. Hence every block has the correct frequency: \(D\) is normal.

For a periodic auxiliary source with period \(p\), \(H(P_{\Sigma,N}^{(L)})\le\log p\) for all \(N,L\). Therefore the readable, usable finite budget becomes
\[
\boxed{\Delta_{D,N}(k)\le\frac{k}{L}\big[\Delta_{C,N}(L)+\log(pQ)\big]
+h_2(\varepsilon)+\varepsilon k\log b.}\tag{J12}
\]

This is a quantitative **no-false-normality theorem for a declared finite-state observer with a zero-entropy source**. It does NOT say any algorithmically computable source is zero-entropy: a computable Champernowne digit stream is normal and has maximal empirical block entropy rate. If a machine receives such a stream and outputs it while ignoring a constant input, the conclusion fails unless the source term is retained. The condition (J11) is indispensable.

Classical provenance: Shannon's 1948 *A Mathematical Theory of Communication*, Theorem 7 (finite-state transducer entropy nonincrease for finite-state statistical sources), https://academicweb.nd.edu/~powers/ame.20231/shannon1948a.pdf; later finite-state normality studies e.g. https://www.sciencedirect.com/science/article/pii/S0022000019300169. JC-04 is an explicit finite **empirical block-entropy inequality** and its SUCC application, **not** a claim to have invented the underlying information principle.

## 5. JC-05 — a reversible, actual-BBP observer with a finite source clock (PROVED LOCAL)

To connect the entropy theorem to the *same joint character*, choose the source-derived pole clock
\[
\boxed{\sigma_n=(8(n+1)-7)\bmod7\in\{0,1,\ldots,6\}.}\tag{J13}
\]
This is the reduced first-pole denominator label, period 7; it is **not sufficient alone to authenticate the four-pole source**, which is independently checked when computing \(d_n\). Make the observer's action genuinely history-dependent via
\[
\boxed{\begin{aligned}
 c_n&=(d_n+q_n+\sigma_n)\bmod16,\\
 q_{n+1}&=(q_n+3d_n+2\sigma_n)\bmod16,\qquad q_0=0.
\end{aligned}}\tag{J14}
\]
The action is \(a_n=(q_n+\sigma_n)/16\bmod1\), as in (J3); \(q_n\) is the **realized internal memory** of this observer, not an independent arbitrary input. Source and observer states evolve together on the original carrier. This is a deterministic 16-state Mealy transducer; folding the 7-phase clock into the state gives a 112-state autonomous machine.

**Reversibility is explicit:** if \(c_n\) and \(\sigma_n\) and \(q_0\) are logged, then
\[
\boxed{d_n=(c_n-q_n-\sigma_n)\bmod16,\quad q_{n+1}=(-2q_n+3c_n-\sigma_n)\bmod16.}\tag{J15}
\]
Induction gives exact reconstruction of the entire original digit stream from the output and the finite source clock, and vice versa. Both the forward and inverse are synchronous finite-state machines with the same period-7 source.

Applying JC-04 in both directions proves
\[
\boxed{(c_n)\text{ is base-16 normal as a digit word}\iff(d_n)\text{ is base-16 normal}\iff\pi\text{ is base-16 normal}.}\tag{J16}
\]
The last equivalence uses the **completed** authenticated digits \(d_n=\lfloor16\{16^n\pi/16\}\rfloor\), not the uncompleted \(\lfloor16\{U_n\}\rfloor\).

**Scope of a real new proof opportunity.** A future source-specific argument could try to prove all-block equidistribution of the *transformed* \(c_n\). JC-04/05 guarantees that such a proof could not merely be a finite-memory encoding illusion: it would force normality of π. But no source-selected estimate for all \(c\)-blocks is supplied here. The Fourier character \(\mathcal J\) still contains the original open signed Weyl sum. The finite-state transformation may change the arithmetic expression of observables, not their logical difficulty.

## 6. JC-06 — discriminating failures and controls

1. **Unlogged arbitrary gauge:** the PR #525 irrational staircase fakes a Haar marginal from \(x_n\equiv0\); it needs an unbounded clock and violates the fixed-period hypothesis of JC-02. The joint decoder still exposes \(e(hx)=1\).
2. **Finite periodic chart can hide a single Fourier mode, not all modes:** \(x_n\equiv0\), \(a_n=(n\bmod7)/7\). The observed first Fourier coefficient is zero at exact multiples of 7 samples, but its 7th coefficient is one; Haar fails. This is a constructive warning against single-mode tests.
3. **Auxiliary-source loophole:** take input \(d_n=0\), external source \(\sigma_n\) equal to the base-\(b\) Champernowne word (normal), and machine \(c_n=\sigma_n\). Finite state alone does **not** prevent false normality; the source has maximal block entropy rate and J11 fails. A finite de Bruijn word of order 5 repeated gives a calibration where omitting the finite source entropy term already numerically breaks J9. A repeated de Bruijn word is periodic, **not** normal asymptotically.
4. **Too-weak output observation:** a single-digit histogram may be exactly uniform while the digit word is periodic (e.g. 0123456789abcdef repeated). Full block normality is essential for JC-04/05.
5. **Wrong seed:** the completed \(\beta=1/5\) has a periodic digit stream and therefore its reversible encoded stream cannot be normal. Its initial seed \(\beta-\pi/16\) is irrational; rational seeds are not independent nonnormal controls (JC-03).
6. **Known finite arithmetic:** exact BBP tail intervals and independent rigorous Machin arctangent intervals certify **128 matching hexadecimal digits** of \(\pi/16\), with no reliance on floating-point π. This is a finite source- and computation-integrity test, not a frequency theorem.
7. **Hostile prior computation:** the earlier unrefined mutation expecting the actual first digit to be unresolved at tail depth one **failed** because that original cell was already decidable. The corrected negative control deliberately chooses a synthetic rational state centered at an interval boundary; the source-interval algorithm then refuses to guess. Retain this failure as a calibration correction, not an arithmetic discovery.

## 7. JC-07 — a quantitative source-clock entropy-to-signed-Weyl bridge (PROVED LOCAL, CONDITIONAL)

The information budget can be transported to the **source-authenticated joint character**, not merely to a normality verdict. The following is a finite mathematical inequality. Its key premise is a bound on an **output block entropy deficit** that remains OPEN for the actual selected source.

Fix \(A,k\ge1\) and read \(N=A+k-1\) consecutive **completed** base-16 digits \(D_{[A,A+N)}=(d_A,\ldots,d_{A+N-1})\), where \(d_n=\lfloor16z_n\rfloor\). For each \(n\in[A,2A)\), the length-\(k\) block beginning at \(n\) determines the prefix cell containing \(z_n\). Put \(P_{D,A}^{(k)}\) for the empirical distribution of these blocks over precisely \(A\) starts, and \(\Delta_{D,A}(k)=k\log16-H(P_{D,A}^{(k)})\). If \(16^k>|h|\), the discrete Fourier sum on the uniform \(16^k\)-cell grid vanishes for every nonzero integer \(h\):
\[
\frac{1}{16^k}\sum_{j=0}^{16^k-1}e^{2\pi i h j/16^k}=0.
\]
For a point inside the \(j\)-th cell, \(|e^{2\pi i h z_n}-e^{2\pi i h j/16^k}|\le2\pi|h|/16^k\). Pinsker's inequality for the empirical block law and the uniform \(16^k\)-cell law gives
\[
\sum_j|P_{D,A}^{(k)}(j)-16^{-k}|\le
\sqrt{2\big(k\log16-H(P_{D,A}^{(k)})\big)}
=\sqrt{2\Delta_{D,A}(k)}.
\]
Thus for the genuine selected completed orbit, and indeed for any radix expansion:
\[
\boxed{
|\mathcal J_A(h)|
=\left|\frac1A\sum_{n=A}^{2A-1}e^{2\pi i h(y_n-a_n)}\right|
\le\sqrt{2\Delta_{D,A}(k)}+\frac{2\pi|h|}{16^k}.}
\tag{J18}
\]
This uses the full \(k\)-block distribution of the *genuinely completed* source-selected digits, not just a one-digit histogram or a virtual-seed ensemble.

Apply JC-04 to the contiguous input/output/source segment \([A,2A+k-1)\) of length \(N=A+k-1\). The observer starts in its **realized state** \(q_A\), which costs at most \(\log16\) entropy; the period-7 source clock costs at most \(\log7\). For \(k\mid L\le N\) the finite sampling-continuity parameter is \(\varepsilon=(L-k)/A\). Let \(\Delta_{C,A,N}(L)\) denote the empirical \(L\)-block entropy deficit of the observed source-clock digit stream on this segment. Inserting J12 into J18 gives
\[
\boxed{
|\mathcal J_A(h)|\le
\sqrt{2\left[\frac{k}{L}\big(\Delta_{C,A,N}(L)+\log112\big)
+h_2\!\left(\frac{L-k}{A}\right)+\frac{(L-k)k\log16}{A}\right]}
+\frac{2\pi|h|}{16^k}.}
\tag{J19}
\]
**Every term in J19 is an observer-output block statistic, a declared finite information budget, or a universal coefficient.** It is a source-authenticated, policy-budgeted, signed Fourier *upper bound* for every finite epoch and every nonzero \(h\) with \(16^k>|h|\). It does **not** imply the bound is small on the actual π stream.

**Single-growing-scale sufficient criterion.** Suppose we can establish for the original zero-seed source divisibility-compatible integer functions \(k(A)\mid L(A)\le A+k(A)-1\) with
\[
\begin{gathered}
k(A)\to\infty,\qquad \frac{k(A)}{L(A)}\to0,\qquad
\frac{k(A)L(A)}{A}\to0,\\
\boxed{\frac{k(A)}{L(A)}\Delta_{C,A,A+k(A)-1}(L(A))\to0.}
\end{gathered}
\tag{J20 OPEN PREMISE}
\]
Then J19 yields \(\mathcal J_A(h)\to0\) for every fixed \(h\ne0\); Weyl's criterion would prove π base-16 normal. Unlike all-fixed-length block normality, J20 is a **single growing-scale sufficient condition**, generally stronger and not known to be necessary. One possible *scale design*, **NOT a proved entropy estimate**, is \(k(A)\asymp\sqrt{\log_{16}A}\), \(L(A)\asymp\tfrac12\log_{16}A\), rounded so \(k\mid L\). Such scaling gives \(16^L\ll A\), avoiding the elementary finite-sample-count floor that makes near-maximal entropy impossible for blocks longer than \(\log_{16}A\). Indeed, for the finite source-clock output segment of length \(N=A+k-1\) there are at most \(N-L+1\) observed \(L\)-blocks, hence \(H(P_C^{(L)})\le\log(N-L+1)\) and
\[
\boxed{\Delta_{C,A,N}(L)\ge\max\{0,L\log16-\log(N-L+1)\}.}\tag{J21}
\]
If \(L\ge(1+\delta)\log_{16}A\) for fixed \(\delta>0\), then J21 makes the scaled debt in J20 diverge when \(k\to\infty\). Therefore *logarithmic observation depth is an actual, source-independent feasibility boundary* for this specific entropy gate, not an arbitrary numerical choice. The actual arithmetic assertion J20 remains **UNVERIFIED**.

For the coherent periodic completion \(\beta=1/5\), the input digit word is periodic; because the source clock and observer states have finite cardinality, the encoded output is eventually periodic. Its \(L\)-block entropy is bounded uniformly in \(L\), so \(\Delta_C(L)=L\log16-O(1)\), and J20 **fails** on that control. Proving J20 for the true selected zero seed would therefore be genuinely seed-discriminating.

**Interpretation.** J19 derives a concrete, finite, source-budgeted upper bound on the original *signed* joint character from a self-realized observer's transformed digit observations. It is not an unconditional arithmetic saving: the output entropy estimate is the unpaid proof debt. The constituent information inequalities are classical, here composed and quantified for the authenticated SUCC source.

## 8. The still-open arithmetic gate

For every fixed nonzero \(h\), the source-authenticated selected joint character is
\[
\boxed{\mathcal J_A(h)=A^{-1}\sum_{n=A}^{2A-1}e\big(h(y_n-a_n)\big)
=A^{-1}\sum_{n=A}^{2A-1}e\big(h\{16^n\pi/16\}\big).}\tag{J17 OPEN}
\]
Showing \(\mathcal J_A(h)\to0\) for all such \(h\) is **still open** and equivalent to π base-16 normality. The *newly certified alternate gate* (J16) is full-block normality of the reversible source-clock stream \(c_n\). That is a theorem-equivalent target, not a new unconditional signed inequality. Neither algebraic transfer nor 128 finite certified digits pays the outstanding infinite cancellation debt.

**Next verdict-changing probe:** Find a **source-specific, seed-selective estimate** for actual original-zero-seed \(c\)-block deficits at a growing family of block lengths \(L(N)\), with an asymptotic bound that beats the finite-sample entropy floor. Every candidate must survive the rational-seed equivalence, explicit periodic-completion ghost, finite-state source-budget controls, and independent BBP/Machin holdouts. Do not promote a finite histogram into an infinite theorem.

## 9. Provenance correction and genuinely fresh source-epoch controls

The signed values for `(A,h)=(223,1),(223,2),(457,1),(457,2)` had been seen in an exploratory calculation before the first preregistration, although the official runner was executed after it. **They are pre-seen calibration data, not blind holdouts.** The former file is preserved unchanged for provenance. A separate addendum was pinned on GitHub commit `6659899812abee3ae6625907212c8d991dfbf6ee` before calculating the new untouched cases. The original four-pole zero-seeded signed character at `(A,h)=(239,3)` lies in the rigorous interval `[0.062069108483,0.062069108492]`, while `(503,3)` lies in `[0.007157640762,0.007157640771]`. The exact 16-root grid at `h=3` is certified below `5·10^{-12}`, and the completed periodic `β=1/5` control is certified above `0.999999999995`. These are **OBSERVED-FINITE** bounds; they neither quantify nor imply an asymptotic Weyl saving.
