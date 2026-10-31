# SUCC — No-Discard Observer × Oily–Macaroni Normalization × Arithmetic Epicycle Bounds

Date: 2026-10-30. **DRAFT RESEARCH ONLY.** Continuation of #397 from Main XVI e18ba565ca540adb7edf3292f5593929e76d91c5. No changes to original signed BBP four poles, U_0=0, archived source, legacy proof contracts, workflows, or main. Read-only source passports: #390 (integer carry, periodic corridor), #392 (retained latent two-panel distribution and Mellin/Gamma tiles), #395 (Stoneham normal controls), #398 (prime stroboscope). Pi base-16 normality and RH remain OPEN.

**Author's hypothesis:** an observer cannot *knowingly discard* information; mistaken epicycle models can be kept coherent by appending corrections and retaining their provenance. Oily–Macaroni normalized paths might quantify the cost and permit arithmetic bounds. The analysis below separates losslessness, observer prior/surprise, conditional entropy, source divergence, and selected arithmetic. These are not the same quantity.

## ND-01: operational losslessness and retained history — EXACT DEFINITION, CLASSICAL IMPLICATIONS

At update t the observer has S_t, sees D_(t+1), and emits a new internal state S_(t+1) and a retained record R_(t+1). The no-discard contract is a left-invertible update on its declared admissible histories:
\[
(S_t,D_{t+1})\stackrel{F}{\longmapsto}(S_{t+1},R_{t+1}),\quad
G(F(S_t,D_{t+1}))=(S_t,D_{t+1}).
\]
If it truly *witnessed* full history W, a projection T(W) is not lossless unless a side record reconstructs W from (T(W),R). A statistic sufficient for an *inference about latent X* need not be sufficient for reconstructing the original observed events.

If an instrument only measures a coarse grade, the unmeasured chronological arrangement is not "knowingly discarded"; do not pretend it was observed. For a declared probability law, the minimal expected **lossless description uncertainty** for a side record is Shannon H(W|T(W)) bits (up to coding convention and finite overhead). For worst-case all distinct length-N b-ary histories, a lossless finite-memory encoding needs at least b^N distinct internal+record states. No such worst-case linear-bit claim applies to one computable π sequence with an unrestricted π algorithm.

This is an observer-information axiom, NOT a physical Landauer heat bound. See Bennett (2003), https://doi.org/10.1016/S1355-2198(03)00039-X.

## ND-02: an exact positive Oily–Macaroni probability law — PROVED IN DECLARED GAMMA(2) LIMIT

Use the same shared Y~Gamma(2,1) from #392, with J,K|Y independent Poisson(Y). Put s=j+k. Their exact joint distribution and harmonic/golden/Gamma contrast are
\[
p_{jk}={(s+1)\binom{s}{j}\over 3^{s+2}},\quad
D_s=H_{s+1}-\gamma-\lambda^{s+2},\qquad \lambda=\varphi^{-1}.
\]
The original Oily corner is D_0=λ−γ>0. Moreover
\[
D_{s+1}-D_s={1\over s+2}+(1-\lambda)\lambda^{s+2}>0.
\]
Thus every D_s is strictly positive and the tilt
\[
W_{jk}={p_{jk}D_s\over \mathcal Z_{\rm OM}},\quad
\mathcal Z_{\rm OM}=1-\gamma+\log3-(1+3\lambda)^{-2}>0
\]
is a well-defined probability law. The normalizer is exactly the (z,w)=(1,1) value of #392's authentic Gamma Mellin–Fourier surface; numerically 1.3986354504917860494... .

The prior-relative surprise / precommitted model-label cost is
\[
L_{\rm OM}(j,k)=-\log_2 W_{jk}
=(s+2)\log_2 3-\log_2(s+1)-\log_2\binom{s}{j}
-\log_2 D_s+\log_2\mathcal Z_{\rm OM}.
\]
Since binom(s,j)<=2^s and D_s<=H_(s+1)<=1+log(s+1), all j,k obey the explicit lower bound
\[
L_{\rm OM}(j,k)\ge s\log_2(3/2)+2\log_2 3
-\log_2(s+1)-\log_2(1+\log(s+1))
+\log_2\mathcal Z_{\rm OM}.
\]
This is a *reference-prior coding cost*, NOT a universal algorithmic Kolmogorov complexity lower bound. A high-grade path may have a short generative program. Exact change-of-measure information cost is KL(W||P)=E_W log(D_S/Z_OM)>0, approximately 0.17513723845 nats (0.25267 bits). This one-time auxiliary selection cost is not automatically a per-π-digit tax.

For any precommitted collection of full-support predictive experts P_(j,k) on actual digit prefixes, the mixture
\(P_{\rm mix}(x_{1:N})=\sum W_{jk}P_{jk}(x_{1:N})\) obeys the **pathwise** coding inequality
\[
-\log_2 P_{\rm mix}(x_{1:N})
\le-\log_2 P_{jk}(x_{1:N})+L_{\rm OM}(j,k).
\]
This is an exact no-hindsight model-label accounting identity, not evidence that the auxiliary Gamma grades sample the actual digits. A model chosen *after seeing* x_(1:N) must pay its predeclared selection/index/reset description.

## ND-03: the specific information that Oily weighting cannot erase — PROVED

In the **finite native** two-full-panel retained-source model, conditional on total grade S=J+K=s, the panel split is source-independent hypergeometric:
\[
P_n(J=j|S=s)=\frac{\binom nj\binom n{s-j}}{\binom {2n}s}.
\]
Multiplying the full joint law by the **same positive function D_s of total s** and renormalizing does not change this conditional split distribution. Therefore the Oily-normalized model retains a strictly positive side-record requirement for reconstructing observed panel labels (except at deterministic boundary grades).

In the Gamma boundary this reduces to \(P(J=j|S=s)=\binom{s}{j}2^{-s}\). Average split uncertainty:
\[
H_P(J|S)=1.70078039368\ldots\;\text{bits},\quad
H_W(J|S)=2.11701518093\ldots\;\text{bits}.
\]
Both numbers belong to the auxiliary source/observer law, NOT the selected π orbit.

Stronger: if the observer witnessed the actual **ordered** binary word of 2n conditional-i.i.d. trials and retained only total S, every word with s successes has the same likelihood even after mixing over X and after Oily tilting. Thus
\[
H_W(\mathrm{word}|S=s)=\log_2\binom{2n}s
\]
**exactly at every finite n**. This is source-independent conditional chronological information, and total grade is NOT a lossless encoding of witnessed word order. If the observer never measured word order, the axiom does not require inventing it retroactively.

Define a finite-n Oily grade tilt \(W_n(s)=P_n(S=s)D_s/\sum_t P_n(S=t)D_t\), with both panels of native depth n and the same original positive source μ_(8n−7). Its limit is \(W_\infty(s)=(s+1)2^sD_s/(3^{s+2} Z_{\rm OM})\). The authentic source has uniform exponential-grade moments for any fixed 1<z<3/2 by \(E[z^{S_n}]\le R(a_n-16n(z-1))/R(a_n)\) for all sufficiently large n. Oily weighting by D_s=O(log(s+2)) preserves such a bound at slightly smaller z. Together with source TV convergence (PR #392), it justifies dominated/summable asymptotics for the expected chronological entropy:
\[
\boxed{H_{W_n}(\mathrm{word}|S)=\bar s_{\rm OM}\log_2 n+O(1)}
\]
with **exact positive leading coefficient**
\[
\bar s_{\rm OM}=E_{W_\infty}S
=\frac{6-4\gamma+4\log3-4(1+3\lambda)^{-3}}
{1-\gamma+\log3-(1+3\lambda)^{-2}}
=5.6580417264381389589\ldots.
\]
The O(1) refinement follows from exponential tails and O(1/n) finite-source analytic PGF convergence away from the pole; at minimum, the displayed leading \(\sim\bar s_{\rm OM}\log_2 n\) law follows by uniform integrability. This is a **conditional Shannon information budget** for reconstructing deliberately *witnessed* words, not a statement about every algorithm or π's digit entropy. The normalization produces a derived numerical growth coefficient without fitting one.

## ND-04: exact ORIGINAL FOUR-POLE logarithmic source distinguishability — PROVED

Retain
\[
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x},\qquad
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5)>0.
\]
Let authentic μ_a(dx)=e^{-ax}Q(x)dx/R(a) and Gamma-matched fake ν_a(dx)=a²x e^{-ax}dx. Set pole coefficients c=(4,-2,-1,-1) and offsets t=(0,3,4,5), so \(\sum c_i=0\).
Put \(\mathscr L(a)=\int_0^\infty e^{-ax}Q(x)^2/x\,dx>0\).
The Frullani/logarithm identity and the vanishing total of the squared-pole coefficients give the exact nine-shift positive logarithmic expression:
\[
\begin{aligned}
\mathscr L(a)
&=-\sum_{i,j}c_i c_j\log(a+t_i+t_j)\\
&=-16\log a+16\log(a+3)+8\log(a+4)+8\log(a+5)\\
&\quad-4\log(a+6)-4\log(a+7)-5\log(a+8)-2\log(a+9)-\log(a+10).
\end{aligned}
\]
Define \(w(x)=Q(x)/(15x)\) with w(0)=1, and \(m_a=E_{\nu_a}w(X)=a²R(a)/15\). Then dμ_a/dν_a=w/m_a and the **exact chi-squared divergence** is
\[
\boxed{\chi^2(\mu_a\Vert\nu_a)
=\frac{\mathscr L(a)}{a^2R(a)^2}-1.}
\]
Derivation: Eν[w²]=(a²/225)\mathscr L(a), and \(m_a²=(a^4/225)R(a)^2\).

The source-local Taylor coefficient Q(x)=15x−(59/2)x²+O(x³) implies
\[
\boxed{\chi^2(\mu_a\Vert\nu_a)=\frac{3481}{450a²}+O(a^{-3}),\qquad
D_{\rm KL}(\mu_a\Vert\nu_a)=\frac{3481}{900a²}+O(a^{-3}).}
\]
These constants are 2*(59/30)² and (59/30)². The KL asymptotic follows by expanding the normalized density against the Gamma(2,1) tangent with its variance 2. Neither coefficient proves unique source recovery; high-jet-matched mutants are negative controls.

A global elementary *rational* bound follows from the positive decomposition \(Q=2(1-e^{-3x})+(1-e^{-4x})+(1-e^{-5x})\), and \(1-e^{-y}\in[y-y²/2,y]\) for y>=0. Thus
\[
0\le1-w(x)\le c\,x,\quad c=59/30.
\]
Since ν_a has EX=2/a and EX²=6/a², for \(a>2c=59/15\), \(m_a\ge1-2c/a>0\), and hence
\[
\boxed{D_{\rm KL}(\mu_a\Vert\nu_a)\le\chi²(\mu_a\Vert\nu_a)
\le\frac{6c²}{a²(1-2c/a)^2}.}
\]

## ND-05: Oily normalized source-vs-fake bound, and a **NO-GO** for source-only epicycles

At native n>=3 take a_n=8n−7, two panels of n Bernoulli observations each conditional on the *same retained X*; both authentic μ and fake ν use the identical conditional channel p(X)=1−e^{-8X}. For finite grades s<=2n, use common score h(s)=D_s>0 and normalize each law **separately** after multiplying by h(s). Write the resulting joint outcome laws \(P_n^{OM},Q_n^{OM}\).

Data processing bounds their unweighted chi-squared divergence by \(\chi²(\mu_{a_n}\Vert\nu_{a_n})\). For an arbitrary pair of laws P,Q with P<<Q and the same positive tilt h in [h_min,h_max], a direct density calculation gives
\[
\chi²(P_h\Vert Q_h)\le(h_{\max}/h_{\min})^3\chi²(P\Vert Q).
\]
(Use the variance of dP/dQ under Q_h and compare both tilted normalizers.) Since D_s is monotone, \(h_{\min}=\lambda-\gamma\) and \(h_{\max}\le H_{2n+1}\le 1+\log(2n+1)\). Thus for every n>=3:
\[
\boxed{D_{\rm KL}(P_n^{OM}\Vert Q_n^{OM})\le
\frac{6(59/30)^2}{(8n-7)^2[1-59/(15(8n-7))]^2}
\left(\frac{1+\log(2n+1)}{\lambda-\gamma}\right)^3.}
\]
The right side is O((log n)^3/n²) and is **summable** in n. This is a genuine universal original-source upper bound under the declared common observation/tilt protocol; it may be coarse for modest n.

**Crucible:** the sum of these **marginal single-clock** KL bounds is finite. This is not the KL divergence of one retained-latent multitime process, nor an unconditional statement about any physical observer's memory. It proves that merely adding Oily-weighted endpoint/source comparisons cannot yield a growing linear information gap that singles out π's selected Weyl phases. A novel source-selected intertime carry/phase coupling remains mandatory. Coherent same-forcing counterseed s*=−π/16 preserves the whole positive carrier and all bounds while remaining nonnormal.

## ND-06: unconditional π-specific finite-state epicycle capacity bound — NEW COROLLARY OF CLASSICAL IRRATIONALITY MEASURE

Let an **autonomous deterministic** q-state machine produce one hexadecimal digit at each transition, with a fixed start state and no external clock, index oracle, side tape, or source of digits. Its output is eventually periodic with preperiod m, period p, and m+p<=q. Let r∈[0,1] be the rational with those digits. The reduced denominator d of 3+r satisfies
\(d\le16^m(16^p-1)<16^{m+p}\le16^q.\)

If its first N digits match π after the radix point, then \(|\pi-(3+r)|\le16^{-N}\). Let \(\mu_* =7.103205334137\ldots\) be the *published* Zeilberger–Zudilin 2020 upper bound on the irrationality measure of π: https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html. For **every** \(\nu>\mu_*\), sufficiently large-denominator rationals obey \(|\pi-p/d|>d^{-\nu}\), and a finite exceptional denominator set is uniformly separated from π. Thus there exists N_0(ν) such that **for every N>=N_0** and every autonomous q-state model matching those N digits,
\[
\boxed{q\ge N/\nu.}
\]
In particular any limiting linear coefficient strictly below \(\mu_*^{-1}\approx0.140781513832\) works asymptotically. No computable N_0 is asserted from the quoted exponent bound. This converts #390's arithmetic periodic-corridor obstruction into a model *state-capacity* lower bound.

**Critical restrictions:** (a) q is the **number of states**, NOT description bits; (b) a program with an external counter and arbitrary-precision algorithm for π is not a q-state autonomous generator; (c) adaptive exceptions, input oracle, reset tape, or clock must be separately represented/charged; (d) the bound follows from irrationality alone, not normality and not the Oily tilting. Claiming q ≥ cN for every observer, or an unavoidable cN **bit** cost, is refuted by computability of π.

## ND-07: reset policy and prequential epicycle ledger (DECLARED, not a universal minimum)

A no-hindsight observer who chooses a finite expert family with a fixed prior W pays model selection surprise \(L_{\rm OM}\) in a Bayesian mixture; if it changes the model class, it must also record the changes of prior, timing, and chosen labels. For r arbitrary distinct reset positions among N-1 boundaries, **if the reset positions themselves must be losslessly reconstructed and all such schedules are admissible**, a worst-case fixed-length schedule index requires at least \(\lceil\log_2\binom{N-1}{r}\rceil\) bits. A particular algorithmic reset schedule (e.g. prescribed Fibonacci times) may have a short program; this is not a pathwise universal lower bound. The full score should be prequential, with predictions frozen *before* the next digit.

A fixed, full-support finite-order Markov predictor on a **hypothetically normal** π has an eventual negative log-evidence rate equal to the context-averaged KL penalty (PR #397, FEO-05). Normality is unproved, and even normality is compatible with computation-based digit prediction. Conditioning a fair i.i.d. ensemble on a selection record can change observed frequencies without violating an entropy ledger. A deterministic π sequence is not itself an i.i.d. ensemble; do not infer heat/erasure laws from its digit expansion.

## Claim ledger and next falsifier

| ID | Claim | Verdict |
|---|---|---|
| ND-01 | A left-invertible event update is formally lossless; latent sufficiency does not imply history retention | DISCLOSED under specified observer contract |
| ND-02 | Oily weights define a positive normalized joint distribution and explicit prior-relative path surprise | DISCLOSED, declared auxiliary model |
| ND-03 | Oily tilt preserves source-independent split, and full witnessed-word history has logarithmic expected conditional information \(\bar s_{\rm OM}\log_2 n+O(1)\) | DISCLOSED paper proof / local numerical controls, source-only |
| ND-04 | Exact nine-log four-pole chi-squared formula and asymptotic \(3481/(450a²)\) | DISCLOSED analytic derivation; independently integrated numerically |
| ND-05 | Same-channel Oily-normalized source/fake KL has a summable O((log n)^3/n²) upper bound | DISCLOSED under declared shared-X per-clock sensor, **NOT** joint-time KL |
| ND-06 | π prefix matching needs q>=N/ν autonomous states eventually, for any ν>published μ* | DISCLOSED corollary, with no effective threshold/bit bound |
| ND-07 | Fixed-prior model label and fully specified reset schedule have chargeable description costs | DECLARED design / classical coding identity |
| ND-08 | These results imply π normality or a physical Maxwell-demon heat law | REFUTED as implication; π normality and RH OPEN |

**Next genuinely verdict-changing task:** construct a precommitted **lossless signed two-time carry/phase observer** including actual U_0=0, literal radix-16 integer seam, intermediate grade split, the source's four signed poles, and full selection/reset records. Derive an all-horizon source-specific occupancy, finite-state gambling, or Weyl saving that (i) is not equivalent to a normality hypothesis, (ii) rejects coherent same-forcing s*=−π/16, (iii) survives a Gamma-matched and higher-jet-matched source mutant, (iv) is calibrated on Stoneham c=3/5 normal controls and de Bruijn nonnormal controls. Source-only, invertible weighted endpoint smoothing cannot supply that estimate.

**No integration/merge, release, source change or theorem-status promotion.** Full SUCC root suite, hosted CI, Lean, and blind external review NOT RUN for this addendum; inspect exact standalone tests and receipts before use.
