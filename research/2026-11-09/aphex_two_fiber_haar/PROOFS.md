# Aphex × two-fiber Haar: sharp source-calibrated parity descent

**2026-11-09. Additive research child of PR #573, exact parent c8763d74b0db0145f574db9bde67d922430080fa.** Original BBP four signed poles, literal U0=0, provenance, existing research, formal contracts, workflows and main untouched. **Pi base-16 normality, original-zero parity balance and RH remain OPEN.** Mathematical priority not asserted.

## TFH-01: fitted Aphex coefficient = exact conditional Haar wavelet (PROVED)

For any finite signed observations a_n,b_n in {-1,+1} with BOTH source sign classes nonempty, define p_plus=Pr(a=1), p_minus=Pr(a=-1), m=p_plus-p_minus, and the conditional complementary responses

\[
u_+=E[b\mid a=+1],\qquad u_-=E[b\mid a=-1].
\]

The binary signed Haar coordinates on the source-sign fiber are
\[
t=(u_++u_-)/2,\qquad \beta=(u_+-u_-)/2.
\]

Directly using p_plus=(1+m)/2 and p_minus=(1-m)/2 gives the **exact identities**

\[
E[b]=t+m\beta,\quad E[ab]=\beta+mt,\quad
\operatorname{Cov}(a,b)=(1-m^2)\beta.
\]

Var(a)=1-m^2>0, so the Aphex observer's least-squares optimal coefficient from #573 is EXACTLY \(\beta=\operatorname{Cov}(a,b)/\operatorname{Var}(a)=(u_+-u_-)/2\). This is a **binary source-sign conditional Haar detail**, NOT the full 16-child / entire-future-tail Haar projector of #565; they are not interchangeable.

## TFH-02: sharp finite source-relative real parity certificate (PROVED)

For the true original four-pole source, #572 gives real completed hexadecimal digit parity sign s_n=a_nb_n, with a the genuine balanced-prime p parity, and b the complete other-odd-CRT/global-winding/2-adic-clock/tail complement. Therefore

\[
P_A:=E_A[s]=\beta_A+m_A t_A,\qquad |t_A|\le1.
\]

Hence the **sharp finite bound**

\[
\boxed{|P_A-\beta_A|\le|m_A|},\quad
\boxed{|P_A|\le|\beta_A|+|m_A|}.
\]

Sharpness: choosing b identically +1 with any biased source-sign law gives beta=0 and P=m. The coefficient 1 cannot decrease. The existing #572/#554/BEC **conditional source-specific prime estimate** is
\[
|m_A|\le 1/p_A+(2+\log p_A)\,\mathcal E_A=o(1).
\]
Thus the observer-to-real-parity ERROR is source-bounded by that same prime estimate. The limit \(\beta_A\to0\) remains **OPEN**, and is equivalent to real hex parity balance given the imported local estimate. No new unconditional cancellation or normality proof is claimed.

**Data-leakage firewall:** fitting beta uses the observed complementary sign b, which already encodes real parity. A calibrated equality is not an independent original-source prediction. The new arithmetic theorem needed would derive bounds on the conditional responses u_plus,u_minus without assuming or fitting the real-digit answer.

## TFH-03: observer fit is not normality (PROVED)

The minimum mean half-square regression loss, with optimized intercept, is

\[
L_{\min}=\frac12\left[
p_+(1-u_+^2)+p_-(1-u_-^2)\right].
\]

This is the conditional variance of the complementary sign. Coherent source-preserving wrong seed b=a has u_plus=1,u_minus=-1, beta=1, real sign s identically +1 and ZERO prediction loss. Consequently perfect observer prediction can coexist with maximal nonnormality. An optimizer reducing its loss proves nothing about the needed original-zero beta_A->0.

## TFH-04: rigorous measurement-precision payment (PROVED, sharp)

Keep the prime-local a sign EXACT. Let the true complement b be replaced by rational approximate response b_tilde, with mean absolute error epsilon=E|b-b_tilde|. Define the two-fiber contrast beta_tilde from the approximate conditional means. Since the smaller source-sign fiber has mass p_min=(1-|m|)/2,

\[
\boxed{|\tilde\beta-\beta|\le\frac{\varepsilon}{1-|m|}}.
\]

Proof: split total absolute error between the two fibers, divide by their respective masses and by two. Equality is attained with all same-sign perturbation restricted to the minority fiber. When #554 makes m->0 conditionally, the instrument's precision condition number tends to 1. That validates observation stability, not arithmetic cancellation.

## TFH-05: original source A512 rational receipt (OBSERVED FINITE)

These 2×2 counts are reconstructed from the ALREADY RECORDED #572 original four-pole source window A=512, p=1217, not a new blind holdout:

| source a | complement b=+1 | complement b=-1 | total |
|---|---:|---:|---:|
| +1 | 133 | 121 | 254 |
| -1 | 125 | 133 | 258 |

Therefore p_plus=127/256, p_minus=129/256 and

\[
u_+=6/127,\quad u_-=-4/129,\quad
\beta=641/16383,\quad t=133/16383.
\]

The actual zero-origin real parity is P=5/128. The EXACT approximation error is

\[
|P-\beta|=133/2097024\approx0.00006342<1/128=|m|.
\]

The minimum conditional regression half-loss is 1046843/2097024. This is finite observational data, not an all-A estimate. The synthetic four-count oracle and canonical original-source SourceParity adapter are separate algorithmic implementations with shared mathematical provenance.

## TFH-06: hostile controls

1. Coherent same-forcing p-integral wrong seed b=a: beta=1, P=1, L_min=0. This kills low-loss=>Haar.
2. Constant complement b=+1: beta=0, P=m, equality in the sharp error bound.
3. Identical source a with b=a versus b=-a: beta=+1 versus -1, P=+1 versus -1. Source-only identification impossible without source-selected complement information.
4. Small beta of this SINGLE binary source-sign fiber does NOT certify any of the other 14 first-digit Fourier modes or any future-conditioned word law.
5. The detector is retrospective unless trained on a separate earlier epoch and tested on unseen source times; even held-out numeric agreement is not a universal proof.

## Verification and next verdict-changing probe

Two new additive files: observational_succ/aphex_two_fiber_haar.py and tests/test_aphex_two_fiber_haar.py. Original 2×2 table has independent Fraction calculation. **5,208 admissible small +/-1 sign-pair streams at N<=6** were exhaustively enumerated by an independent reference implementation and satisfied the conditional algebra, sharp error and loss formula; finite computation is not the proof (the above identities are). The original-source adapter replays #572's A512 receipt; exact-head native full suite and hosted CI must be inspected separately, not assumed. No Lean certification or independent scholarly referee claimed.

**OPEN TARGET:** from original U0=0, full signed prime/CRT winding/tail and #554 character bounds, prove u_plus(A)-u_minus(A)->0 for every integer epoch A. This would give only pi hex parity balance; not base-16 normality. The coherent wrong seed has difference exactly 2 and MUST fail the proposed proof.
