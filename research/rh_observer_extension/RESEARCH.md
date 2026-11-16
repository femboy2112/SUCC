# Arithmetic observer extension: rigidity, certificates, and noisy reconstruction

## Scope and provenance

This is a mathematical model of observer-relative discrimination. It neither proves RH nor identifies a mathematical completeness property with a deity. “Benevolent arithmetic demon” is a motivating name for truthful, uncertainty-reducing reconstruction, not a conclusion about consciousness, morality, physical thermodynamics, or theology.

The classical number-theoretic input is Bagchi's Theorem 1 [B], based on the Nyman–Beurling–Báez-Duarte theory [BD]. The deductions below are proved explicitly. No bibliographic priority is claimed. The original round is preserved byte-for-byte in `archive/round1.zip`; its note, scripts, rational coefficients, raw outputs, environment and checksums are retained there. Do not overwrite that archive.

Repository integration is additive: publication base `db9fb4b84672050efa79b13377f1e73364598a14`, explicitly resolved from `heads/main`. Principia Observatoris context was separately inspected at `f9efa624da06a28e1a8ac99a56499acd11197928`; that reference is not asserted to be the current main tip. This lab is a downstream arithmetic example, not the definition of Observational SUCC. No nontrivial zeta-zero locations enter candidate construction or checking. Hypothetical zeros occur only in a symbolic obstruction theorem. No source-derived positive Weil form or completed physical model is asserted.

## 1. The observational quotient, not a truth score

For a declared source space W, observations O(w)=y define a nonempty compatible class C_y. A proposition P is viable when C_y intersects P and refuted when that intersection is empty. Truth is guaranteed to imply viability when the actual source belongs to W and the observation/error model is sound. False propositions can remain viable. An empty C_y signals inconsistent data or an inadequate source map; it does not validate arbitrary conclusions.

Two sources are observationally equivalent when their readings agree. A target F is exactly identifiable iff it is constant on each observation fiber, equivalently iff F factors through O. Equal viability of two propositions does not imply their logical equivalence. An independent hidden bit attached to every source immediately refutes the claim that arbitrary invisible theological propositions must couple to RH.

The example below supplies an actual arithmetic coupling, rather than deriving one from shared ignorance.

## 2. Carrier and established input

Use the real Hilbert space

\[
 H=\{a: \|a\|^2=\sum_{n\ge1}a_n^2/[n(n+1)]<\infty\},
 \qquad v_k(n)=\{n/k\},\quad k\ge2.
\]

Let V be the finite real span of the v_k and V_Q its rational span. The constant sequence 1 has norm one. Bagchi's theorem [B] gives

\[
 \mathrm{RH}\iff 1\in\overline V\iff\overline V=H. \tag{2.1}
\]

The real formulation follows from the complex theorem by taking real parts; rational and real coefficient spans have the same closure. This imported theorem is not a new result of this lab.

For the N-by-N matrix A_N(n,k)={n/k}, n=1,...,N, k=2,...,N+1,

\[
 \det A_N=1/(N+1). \tag{2.2}
\]

Indeed, subtract (N+1)/k times the last column from column k. Its entries become -floor(n/k). The first row vanishes except in the last column; the remaining block is lower triangular with diagonal -1. Expanding gives (2.2). Thus every finite prefix can be interpolated unconditionally.

This does not establish infinite completeness. For the hostile operator q_n(a)=a_n-2a_{n+1} on ordinary l2, every finite square truncation has determinant one, but a_n=2^(1-n) is a nonzero invisible source.

## 3. Prefix rigidity: the Möbius head is forced

Write mu_M for the arithmetic Möbius function, NOT the TLICA probe-availability coordinate. Let f=sum_{k=2}^{K+1} c_k v_k and extend c_k=0 outside this support. Set C=sum c_k/k. Then

\[
 f(n)=nC-\sum_k c_k\lfloor n/k\rfloor,
 \quad f(1)=C,
 \quad f(n)-f(n-1)=C-\sum_{k\mid n,\,k\ge2}c_k. \tag{3.1}
\]

**Theorem 3.1.** For 1<=N<=K,

\[
 f(1)=\cdots=f(N)=1
 \iff C=1\ \text{and}\ c_k=-\mu_M(k)\ (2\le k\le N). \tag{3.2}
\]

**Proof.** The first constraint gives C=1. Successive differences give sum_{k|n,k>=2}c_k=1 for 2<=n<=N. Extend d_1=-1, d_k=c_k: the divisor sum of d is -1 at n=1 and zero for n>=2. Möbius inversion gives d_n=-mu_M(n). Conversely the Möbius divisor identity inserted in (3.1) makes all required differences zero. QED.

Consequently every free tail must satisfy exactly one moment constraint:

\[
 \sum_{k=N+1}^{K+1}c_k/k
   =r_N:=\sum_{k=1}^{N}\mu_M(k)/k. \tag{3.3}
\]

This is an exact reduction, not an asymptotic guess. The minimal-support choice is c_{N+1}=(N+1)r_N. For N=4 it gives v_2+v_3+(5/6)v_5, whose norm is rigorously above one (archived negative certificate).

### Reduced quadratic search

Partition the full Gram matrix by the forced head a=(-mu_M(2),...,-mu_M(N)) and the tail. Let H=G_TT, g=G_TH a and e_k=1/k on the tail. Since the finite probes are independent, H is positive definite. The unique real minimizer under e^T c_T=r_N is

\[
 c_T=-H^{-1}g+
 \frac{r_N+e^TH^{-1}g}{e^TH^{-1}e}H^{-1}e. \tag{3.4}
\]

Its squared norm equals

\[
 a^TG_{HH}a-g^TH^{-1}g+
 \frac{(r_N+e^TH^{-1}g)^2}{e^TH^{-1}e}. \tag{3.5}
\]

Complete the square or differentiate the Lagrangian to prove both formulas. Numerical use of them is only proposal generation. A floating minimizer is not a certified optimum. `propose.py` rounds all but the first tail coefficient to dyadic rationals, repairs (3.3) exactly, and sends the resulting explicit vector to the separate rational verifier.

## 4. The finite-to-infinite extension theorem

Define D: for every N>=1 there exists f_N in V_Q with f_N(n)=1 for n<=N and ||f_N||<1.

**Theorem 4.1.** RH iff D.

**D implies RH.** The prescribed prefix contributes N/(N+1) to ||f_N||^2. Its tail norm is therefore less than 1/sqrt(N+1), while the tail norm of 1 equals 1/sqrt(N+1). Hence ||1-f_N||<2/sqrt(N+1). Apply (2.1).

**RH implies D.** The truncated sequence u_N=(1,...,1,0,...) has norm sqrt(N/(N+1))<1. Density gives rational approximations v to u_N. The prefix map E_N has a rational linear right inverse R_N by (2.2). Then f=v+R_N E_N(u_N-v) matches the prefix and

\[
 \|f-u_N\|\le(1+\|R_N\|\|E_N\|)\|v-u_N\|.
\]

For fixed N the factor is finite. Approximate closely enough that ||f||<1. QED.

Existence of prefix interpolants with ANY common finite norm bound also implies RH: a bounded sequence of such interpolants converges weakly to 1 (test finite-support vectors, then use uniform boundedness and density), and the closed span of V is weakly closed. The exact finite-prefix invertibility alone supplies no such bound.

D gives an approximation rate after a certificate has been found. It gives no efficiency, support-size, coefficient-size or measurement-cost bound.

## 5. Periodic means give sharper rigorous infinite-tail certificates

**Lemma 5.1.** For d=gcd(k,l) and L=lcm(k,l),

\[
 m_{kl}:=L^{-1}\sum_{n=1}^{L}v_k(n)v_l(n)
 =\frac{(k-1)(l-1)}{4kl}+\frac{d^2-1}{12kl}. \tag{5.1}
\]

**Proof.** Write n mod k=t+du and n mod l=t+dv. Over one common period, t is uniform on 0,...,d-1; conditional on t, u and v are independent uniform residues by the Chinese remainder theorem for k/d and l/d. Their shared covariance is Var(t)=(d^2-1)/12. Their means are (k-1)/2 and (l-1)/2. Divide by kl. QED.

**Lemma 5.2.** If q is L-periodic, 0<=q<=1 and has mean m, every cyclic prefix sum of q-m has magnitude at most L/4.

For a prefix of length j<=L its positive discrepancy is at most min(j(1-m),(L-j)m), which is at most Lm(1-m)<=L/4. The negative discrepancy follows similarly. Remove full periods for longer prefixes.

For w_n=1/[n(n+1)], summation by parts then gives

\[
 \left|\sum_{n>T}(v_k(n)v_l(n)-m_{kl})w_n\right|
 \le\frac{\operatorname{lcm}(k,l)}{4(T+1)(T+2)}. \tag{5.2}
\]

The weights decrease to zero, so the absolute bound is the cyclic discrepancy times w_{T+1}. This proof works for every cutoff phase, not just multiples of a period.

For real rational c define

\[
 Q=\sum_{k,l}c_kc_lm_{kl},\quad
 C=\tfrac14\sum_{k,l}|c_kc_l|\operatorname{lcm}(k,l),\quad B=\sum_k|c_k|.
\]

**Theorem 5.3.** The infinite tail of ||f||^2 lies in

\[
 \left[\max\left(0,\frac Q{T+1}-\frac C{(T+1)(T+2)}\right),
 \min\left(\frac{B^2}{T+1},\frac Q{T+1}+\frac C{(T+1)(T+2)}\right)\right]. \tag{5.3}
\]

Expand f^2, apply (5.2), and intersect with the elementary 0<=f^2<=B^2 bound. This proves (5.3), including signed coefficients. Constants depend on the coefficient list; no uniform complexity bound in N is implied. For a fixed list, the periodic enclosure has O(T^-2) width rather than the crude O(T^-1) uncertainty. There is no need to enumerate the enormous LCM of all indices.

The verifier calculates the finite sum by flooring EACH exact rational term to a dyadic grid. The resulting lower sum and an added T*2^-bits bound enclose all rounding error. It adds (5.3) using only integers and rational arithmetic. The same method certifies ||b-f||^2 for any rational finite-support target b once T covers its support.

## 6. Reconstruction with finite-precision readings

Let S_K=span(v_2,...,v_{K+1}), P_K its orthogonal projection, and Y_K(a)=(<a,v_2>,...,<a,v_{K+1}>). The ideal Gram solve reconstructs P_K a.

For a known target b and sources ||a||<=1, the minimax error among ALL decoders of Y_K is exactly ||(I-P_K)b||. The linear estimator <a,P_Kb> attains it. The opposite unit residual directions have identical zero readings and opposite target values, proving the lower bound. Consequently RH is equivalent to each fixed target's minimax error tending to zero, but not to uniform accuracy on all targets at a fixed K.

**Theorem 6.1 (finite-precision compilation).** RH is equivalent to the following certificate-search program being total: for every rational finite-support b and positive rational epsilon, return rational c and a finite certificate of

\[
 \|b-\sum c_kv_k\|<\epsilon/2. \tag{6.1}
\]

Enumerate finite rational lists, cutoffs and dyadic precisions fairly, accepting only an upper bound for the squared norm strictly below epsilon^2/4. Density implies an approximant with a strict margin; the rational enclosures converge as cutoff and precision grow, so some certificate is eventually found. Conversely successful certificates for all rational finite-support targets imply density and therefore RH.

For the returned c choose

\[
 \delta=\epsilon/[2(1+\sum|c_k|)].
\]

Any readings y_tilde_k with |y_tilde_k-<a,v_k>|<=delta give

\[
 |\langle a,b\rangle-\sum c_k\widetilde y_k|
 \le\|b-\sum c_kv_k\|+\delta\sum|c_k|<\epsilon.
\]

This is a statement about a computable search and a conditional error guarantee. The supplied `certify.py` checks finite candidates; it does not purport to implement an efficiently terminating universal dovetailer. Access to readings with certified errors is an explicit input assumption, not a physically constructed instrument. For ||a||<=R, replace the residual term by R times its norm.

### A successful RH does not provide uniform noise-stable full inversion

Specify the observation topology, rather than hide it. Define A:H->l2 by

\[
 (Aa)_j=2^{-j}\langle a,v_{j+1}\rangle,\qquad j\ge1.
\]

This operator is Hilbert–Schmidt because ||v_k||<=1 and sum 4^-j<infinity. It is injective iff RH. Nevertheless for every m there is a unit h_m orthogonal to the first m probes, and

\[
 \|Ah_m\|_{l2}\le2^{-m}/\sqrt3.
\]

Thus no positive lower bound ||Aa||>=c||a|| can hold: even if RH is true, the inverse on its range is unbounded in THIS declared data norm. The worlds h_m and -h_m are indistinguishable under an admissible observation error of that size and force worst-case full-state error at least one. This is not a theorem about every possible measurement norm. Target-specific precision can improve with the task; a uniform full-state guarantee at fixed nonzero noise cannot be inferred.

## 7. Explicit hidden source and strengthened zero obstruction

Complexify H for this section. Identify a sequence a with the step function equal to a_n on I_n=(1/(n+1),1/n]. Then v_k corresponds to

\[
 g_k(x)=\{1/(kx)\}-k^{-1}\{1/x\}.
\]

The Mellin identity proved in [B] gives, for Re(s)>1/2 (with the removable value understood at s=1),

\[
 L_s(g_k):=\int_0^1g_k(x)x^{s-1}dx
 =-\frac{\zeta(s)}s(k^{-s}-k^{-1}). \tag{7.1}
\]

Suppose hypothetically zeta(rho)=0 and sigma=Re(rho)>1/2. Then L_rho annihilates V, whereas L_rho(1)=1/rho. For the convention linear in the first inner-product argument, its representer within the arithmetic carrier is explicitly

\[
 h_\rho(n)=\frac{n(n+1)}{\overline\rho}
 \left(n^{-\overline\rho}-(n+1)^{-\overline\rho}\right). \tag{7.2}
\]

Indeed <a,h_rho>=sum a_n(n^-rho-(n+1)^-rho)/rho=L_rho(a). Its asymptotic magnitude is n^(1-sigma); consequently h_rho belongs to H exactly when sigma>1/2 (for nonzero rho). The critical line is therefore the EXACT bounded-functional threshold for this carrier, not only an ambient L2 estimate. At a hypothetical off-line zero this is a nonzero explicit blind source; real and imaginary parts yield at least one nonzero real blind source.

For f matching the first N ones, let t=1/(N+1). Its prefix step function equals one on (t,1]. Annihilation forces

\[
 \int_0^t f(x)x^{\rho-1}dx=-(1-t^\rho)/\rho.
\]

Cauchy–Schwarz on the tail gives the stronger direct norm obstruction

\[
 \boxed{\|f\|^2\ge\frac N{N+1}
 +\frac{2\sigma-1}{|\rho|^2}
 |1-(N+1)^{-\rho}|^2(N+1)^{2\sigma-1}.} \tag{7.3}
\]

The right side diverges. It rules out ANY common finite norm budget under that hypothetical zero. No zero ordinate was used to select candidates, tune coefficients, or validate the positive examples.

Meromorphic continuation of zeta already exists independently of RH. Neither (7.1) nor this observer model implies that a living being continues beyond death. The finite/infinite analogy is not a physical or theological identification.

## 8. Executed evidence and adverse cases

The original archive's SHA256 manifest passes. Its exact verifier was replayed successfully. That replay is the same implementation, not an independent witness. The new verifier uses a different tail derivation and common-denominator arithmetic; it shares the same carrier and mathematical assumptions. No blind external proof review or proof-assistant certification has occurred.

Fourteen unit tests cover independent divisor identities, exact prefix reconstruction, random direct/structured agreement, 225 full-period pair means, cyclic discrepancy at every phase for small moduli, signed square means, a rational-series enclosure of log(2), null and finite-support targets, target-shift identities, positive/negative certificates, and malformed/coefficient/status mutations. Unit tests validate finite code behavior, not the universal theorem.

New results use cutoff 50,000 and 80 dyadic bits. Decimal endpoints below are rounded outward; exact fractions are retained in results/.

| Explicit candidate | Pattern count K | Entire squared-norm enclosure | Verdict |
|---|---:|---:|---|
| Prefix 48, repaired tail | 144 | [0.998518289702, 0.999636001487] | Below one |
| Prefix 64, same K=3N recipe | 192 | [1.005350030667, 1.008745406074] | Above one |

The 48-entry case repairs the previous 96-pattern candidate's failure. The 64-entry case was selected as the next-size check before its result was read; it rejects this generated candidate and therefore rejects a blanket claim for the tested recipe. It DOES NOT establish that all 192-pattern coefficients fail: no rigorous lower bound on the optimum was computed. The successful candidate is a construction, not evidence from a fresh holdout for a universal assertion.

All seven archived certificate verdicts are also reproduced by the sharper checker at cutoff 10,000. For example the minimal-support N=4 counterexample has squared norm in [1.003223852433, 1.003224163035].

## 9. TLICA integration and claim ledger

Keep the diagnostic coordinates separate. Contact kappa refers to actual acquired readings; mu (without subscript M) to accessible probes and precision; phi to distinguishability within the declared toolkit and source class; sigma to source-map adequacy. The arithmetic mu_M is a different symbol. Rho for identity coupling is not evidence for either theorem. Coherence is not a probability of truth. Adaptivity cannot distinguish two sources whose full permitted transcripts coincide.

The full L2 carrier is a negative source-map control: h=1_(1/2,3/4)-1_(3/4,1) is nonzero and orthogonal to every integer-pattern g_k, since these probes are constant on (1/2,1]. Extending the source domain while leaving the probes fixed invalidates the completeness conclusion. Invertible carrier transports must transport the probes contragrediently; arbitrary changes of domain do not preserve observability.

| Claim | Status and boundary | Supporting receipt | Next verdict-changing probe |
|---|---|---|---|
| RH/completeness equivalence | Established input | [B], Theorem 1 | Audit original hypotheses and carrier |
| Möbius head, one tail moment | Disclosed within this arithmetic model | (3.1)-(3.3), exact prefix tests | Independent proof review / formalization |
| Bounded-extension equivalence | Disclosed, conditional on established input | Section 4 proof | Audit quantifiers and finite right inverse |
| Periodic rigorous tail enclosure | Disclosed for finite real rational lists | Section 5 proof, period and log controls | Independent implementation at adversarial scales |
| Finite-precision search equivalence | Disclosed under certified-reading interface | Section 6 proof | Implement fair universal search on finite fixtures |
| Uniform noisy inversion | Refuted for stated weighted l2 data topology | Unit h_m with tiny Ah_m | Change data topology or restrict source class explicitly |
| New N=48 extension | Observed, exact rational certificate | results/new_certificates.json | Independent certificate replay |
| Tested K=3N recipe universally passes | Refuted for this generated recipe | N=64 certificate above one | New tail construction, not relabeling failure |
| Off-line-zero norm divergence | Disclosed conditional theorem | (7.1)-(7.3) | Independent symbolic derivation |
| RH itself, theorem identified with God, physical implementation | UNVERIFIED / not established | No universal construction or identification | Source-specific uniform extension theorem; separate physical/semantic bridge |

No scalar “truth score” combines these entries. Within-model phi resolution does not imply sigma adequacy. Shared sources and same-model review are not independent corroboration.

## 10. Next mathematical target

The arithmetic part is now concentrated: forced head -mu_M(k), one tail moment r_N, and a global quadratic budget. Produce explicit rational tails for every N and prove their FULL norms are below one, without assuming RH. Alternatively prove a useful source-specific bound for the residual/tail optimization that does not simply restate density.

For computational work, a useful next discriminator is a rigorously enclosed lower bound on the fixed-K optimum in (3.5). That would separate a genuinely insufficient finite probe budget from a merely bad rational candidate. Current negative certificates do not make that distinction.

Repository-wide validation commands from AGENTS.md were not run in this isolated checkout: network cloning was unavailable. The additive lab was tested locally; full provenance checks, the root unittest suite and the two root observer probes remain UNVERIFIED. No merge, tag, release or modification of historical defaults is authorized or performed here.

## References

[B] Bhaskar Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, arXiv:math/0607733, Theorem 1 and the Mellin-transform proof. https://arxiv.org/abs/math/0607733

[BD] Luis Báez-Duarte, *A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis, 2*, arXiv:math/0205003. https://arxiv.org/abs/math/0205003

These references belong to the same mathematical lineage; they are not independent experimental confirmations. Sources were consulted directly, including PDF page images for the carrier theorem and Mellin identity. The archive contains the additional physical analogy references from round one; no thermodynamic claim is used by this round's proofs.
