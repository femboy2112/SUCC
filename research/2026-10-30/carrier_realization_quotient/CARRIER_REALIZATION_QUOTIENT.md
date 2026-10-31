# SUCC — Operation RAW STATE: Carrier-realization quotient, entropy rigidity, and selected BBP nonconcentration

**Date:** 2026-10-30. **Status:** DRAFT RESEARCH ONLY. Target parent: COUNT-OUT PR #406 at `ba66c2e4217d1d6eec407b142ed467c48e39ed1c`, ultimately descended from Main XVI `e18ba565ca540adb7edf3292f5593929e76d91c5`. Related independent source-selected arithmetic research #403/#405, positive observer #395, arithmetic conductor #399/#401, Noether/Radix #404. Original four signed BBP poles, fixed original zero seed, historical contracts, production code, workflows and main are unchanged. **π base-16/base-3 normality and RH OPEN.**

## 0. Author's objective, strongest faithful interpretation

> "the goal of the quotient [is] to be left with the set that is the carrier realized in the pi-normal respecting shape, but without any arithmetic connections between them, just raw state. if we can do that, then we know we have a good handle on how the space is threaded together arithmetically"

Define **raw realized state** as the EMPIRICAL OCCUPATION MEASURE, or more cautiously its compact **set of weak subsequential limits**; quotient away time arrows/causal-path accounting and internal carry labels *in the OUTPUT*, while preserving the source, selected seed, literal integer lifts and proof certificates separately. The bare support set does not suffice: full-support biased Bernoulli measures are invariant, non-atomic, non-Haar. An uncalibrated change of state coordinates can also uniformize a non-Haar nonatomic full-support measure by its cumulative distribution function. Retain the base-16 reference partition/Haar measure and its calibrated state coordinates even when forgetting arithmetic EDGES. A quotient cannot use Haar averaging over SEEDS: that manufactures a uniform reference unrelated to actual selected occupancy.

**Operational object:** original carrier + selected orbit, its state samples, its raw empirical measure, and a rigorously controlled map between forced and pure-radix observations. **Acceptance:** a theorem restricting every limiting selected measure to Haar, an independently sourced finite-scale counting/occupancy certificate or a rigorous blockage. Finite numerics and rephrasings of normality do not establish acceptance.

## RS-01. Exact carrier source passport and raw quotient

For n≥1, original four-pole forcing is
\[
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),\quad r_n=R(8n-7)>0,\quad U_0(s)=s,\quad U_n(s)=16U_{n-1}(s)+r_n.
\]
Define the positive Green tail and BBP selected boundary
\[
T_n=\sum_{j\ge1}16^{-j}r_{n+j},\quad
\alpha=s+\sum_{j\ge1}16^{-j}r_j=s+\pi/16,
\qquad U_n(s)=16^n\alpha-T_n.
\]
For the authentic selected seed s=0, use x_n={U_n(0)}∈R/Z and pure b=16 state y_n={16^nπ/16}∈R/Z, n≥1. The first hexadecimal digit of π/16 is 3; π itself begins `3.243f...` in hexadecimal. A finite one-digit shift does not affect base-16 normality, but finite sample tables below refer to π/16 (and are labeled accordingly). These are **not identical pointwise** but their signed distance is governed by T_n. The finite raw-state measures are
\[
\mu_N^U=N^{-1}\sum_{n=1}^N\delta_{x_n},\qquad
\mu_N^{\rm radix}=N^{-1}\sum_{n=1}^N\delta_{y_n}.
\]
The quotient at infinity is the cluster-set functional \(\mathscr Q=\bigcap_{N\ge1}\overline{\{\mu_M:M\ge N\}}\) in weak-* topology. This exists by compactness even if one assumes no limiting distribution. For π base-16 normality, the desired outcome is the SINGLETON \(\mathscr Q=\{\lambda_{\rm Haar}\}\).

**Circle symbolic-firewall:** actual hexadecimal words belong naturally to the full one-sided shift \(\Omega=\{0,...,15\}^{\mathbb N}\). For digit sequence a of π/16, \(\nu_N=N^{-1}\sum_{n=0}^{N-1}\delta_{\sigma^n a}\); every weak limit ν is σ-invariant. All symbolic cylinders are clopen, eliminating half-open circle-cell boundary ambiguities. The standard radix evaluation π_b pushes each ν to a circle raw-state measure. Conversely a Haar circle limit gives the uniform Bernoulli symbolic limit because b-adic boundary points have Haar mass zero. Thus π base-16 normality iff every symbolic cluster ν is the uniform Bernoulli measure \(u\), iff every circle cluster is Haar. **Do not infer equal exact cylinder counts from a small Green correction before controlling seam visits.**

## RS-02. Original-source *Wasserstein* quotient bridge — DISCLOSED

Source positivity and summability yield
\[
0<T_n\le[(8n+1)(8n+2)]^{-1},\qquad
\mathcal M_{\rm BBP}:=\sum_{n=1}^\infty T_n
=\frac{S_R-\pi}{15}=0.01629699773382656556...,
\]
where the source pole sum has exact digamma form
\[
S_R=\sum_{n\ge1}r_n=-\tfrac18[4\psi(1/8)-2\psi(1/2)-\psi(5/8)-\psi(3/4)].
\]
The last equality follows by reorganizing absolutely convergent partial fractions; the Green identity follows by swapping the convergent positive double sum. Independent conservative elementary bound: \(\mathcal M_{\rm BBP}<1/81+1/72<1/32\) (obtained from the Green upper bound and a decreasing integral test). This requires no transcendental numerical oracle.

Couple the n-th forced point x_n with the n-th pure point y_n. Since their circle distance is at most T_n,
\[
\boxed{W_1^{\mathbb T}(\mu_N^U,\mu_N^{\rm radix})\le\frac1N\sum_{n=1}^N T_n\le\frac{\mathcal M_{\rm BBP}}N.}\tag{RS-W1}
\]
This is an **UNCONDITIONAL selected-source metric bound** for all N≥1, stronger in scope than a single harmonic error: every circle 1-Lipschitz test transfers. It proves the two raw quotient cluster-sets are identical, without assuming normality. It does NOT say that either is Haar.

For a b-adic circle interval I_w of size 16^-k and arbitrary epsilon>0, define the epsilon outer/inner neighborhoods I^+ε and I^-ε. Every index with T_n≤ε respects the corresponding inclusion; the other indices number at most \(\sum T_n/ε\). Thus
\[
\boxed{\mu_N^{\rm radix}(I_w^{-ε})-\frac{\mathcal M_{\rm BBP}}{Nε}
\le\mu_N^U(I_w)\le
\mu_N^{\rm radix}(I_w^{+ε})+\frac{\mathcal M_{\rm BBP}}{Nε}.}\tag{RS-buffer}
\]
At epsilon=16^-k/8 the error is at most \(8\mathcal M_{\rm BBP}16^k/N\). This is a **buffered resolution bridge**, not equality of raw k-cylinder counts: near-boundary occupancy must be controlled separately. At moving k∼c log_16 N, the additive error tends to 0 for c<1, but making it *relative* to cell mass 16^-k also requires c<1/2 (or a refined epsilon) and an independent boundary-buffer estimate.

## RS-03. A strictly weaker *sufficient target*: subexponential maximum-cylinder concentration — DISCLOSED (normality-equivalent)

For the actual infinite base-16 digit word a define
\[
p_{N,k}(w)=N^{-1}\#\{0\le j<N:a_{j+1}\cdots a_{j+k}=w\},
\quad M_k=\limsup_{N\to\infty}\max_{|w|=k}p_{N,k}(w).
\]
Put \(E_k=\log(16^kM_k)\ge0\), with log natural. **THEOREM:**
\[
\boxed{a\text{ base-16 normal}\iff\liminf_{k\to\infty}E_k/k=0.}\tag{RS-MaxCyl}
\]
Equivalently, a source-derived upper bound \(M_{k_j}\le16^{-k_j}e^{o(k_j)}\) on **some unbounded sequence** k_j suffices. This can allow an arbitrary polynomial multiplier k^B, or subexponential exp(sqrt(k)), in place of one uniform constant C. The source arithmetic must independently prove the bound; proving the equivalence alone is not π normality.

**Proof (full shift, no ergodicity assumed):** The shift empirical measures ν_N have compact nonempty limit set \(\mathscr L\). Every ν∈\mathscr L is shift-invariant. If a is normal, p_N,k(w)→16^-k and E_k=0 for all k. Conversely assume a non-Haar ν∈\mathscr L. Then some q-digit block law ν_q differs from uniform u_q; let \(\Delta_q=D_{KL}(\nu_q\Vert u_q)=q\log16-H_q(\nu)>0\). For every ℓ=mq+r, 0≤r<q, stationary block subadditivity gives
\[
H_\ell(\nu)\le mH_q(\nu)+r\log16
=\ell\log16-m\Delta_q.
\]
For any finite probability law, H_ℓ≥−log(max_w ν[w]); therefore
\[
\max_{|w|=\ell}\nu[w]\ge16^{-\ell}e^{m\Delta_q}.
\]
Since \(M_\ell\ge\max_w\nu[w]\) for every fixed ℓ, we obtain
\[
\boxed{E_\ell\ge\lfloor\ell/q\rfloor\Delta_q,
\qquad\liminf_{\ell\to\infty}E_\ell/\ell\ge\Delta_q/q>0.}
\]
This contradicts the assumed liminf zero. Consequently all ν are uniform, so a is normal. ∎

**Quantitative discriminator:** If \(\delta_*:=\liminf_{k\to\infty}E_k/k\), then for EVERY ν∈\mathscr L and fixed q,
\[
\boxed{D_{KL}(\nu_q\Vert u_q)\le q\delta_*,\quad
TV(\nu_q,u_q)\le\sqrt{q\delta_*/2}.}\tag{RS-KL}
\]
The second inequality is Pinsker in natural-log units. At δ*=0 exact Haar; for δ*>0 it bounds the worst permitted q-block bias. This **quantitative entropy amplification lemma** is a classical entropy argument specialized as an operational SUCC proof interface, not a novel mathematical principle.

Equivalently all invariant limit measures must have maximal entropy log16. The unique maximal-entropy invariant measure of the full shift is the uniform Bernoulli measure (classical uniqueness-of-MME theorem). This criterion is logically equivalent to normality, but its count-concentration form may be more amenable to occupancy/conductor methods than explicitly computing each digit frequency.

## RS-04. Three strict no-gos that the quotient must survive

1. **Bare support / full state access is insufficient.** Strictly positive iid digit probabilities \((2/17,1/17,...,1/17)\) give an invariant, non-atomic, FULL SUPPORT measure on all radix states and every finite word. It is non-Haar since P(0)=2/17 ≠1/16; its entropy rate \(H=\log17-(2/17)\log2=\log16-0.020922105308...\), and its heaviest k-cylinder has ratio \((32/17)^k\) to uniform. Thus even almost-maximal entropy and dense state access do not suffice.
2. **Finite block calibration is insufficient.** A periodic base-16 de Bruijn word of order 2 has exactly uniform one- and two-digit cyclic block frequencies, but is periodic and nonnormal at longer lengths. The exact-test generator checks all 256 two-symbol cylinders.
3. **Invariance is load-bearing.** The NONINVARIANT measure with a forced first digit 0 and all later digits uniform has max k-cylinder 16^{-(k-1)}, so \(16^k M_k=16\) (subexponential overhead!), yet the first digit is biased. The entropy rigidity proof would FAIL without stationarity of every orbit-limit. SUCC gets that stationarity from the expanding radix evolution, not from a gratuitous entropy axiom.
4. **Coordinate gauge is load-bearing.** A nonatomic, full-support probability on the line can be mapped to uniform by its cumulative-distribution homeomorphism, even if its original radix-16 digit law was biased. A completely unmarked "bare raw set" has no intrinsic meaning of base-16 normal. Retain the calibrated circle/radix partition while quotienting arithmetic path arrows.
5. **Prime conductor or isolated phase slips are insufficient.** PR #405 proves logarithmic selected lag-energy saving and stronger moving-frequency windows, not positive-density fixed-frequency dispersion. Source conductor growth and rare forced dephasing do not force RS-MaxCyl. A coherent changed seed has identical source and delta_0 raw-state limit. No source-only, seed-blind claim may identify the selected empirical shape.

## RS-04a. The correct three-time **normal-respecting raw shape** is a graph measure, NOT 3D Haar — DISCLOSED

This is the crucial geometry calibration when relating the carrier-realization quotient to PR #402's proposed third observation direction. Define the actual forced three-state snapshot
\[
\Gamma_N^U=\frac1N\sum_{n=1}^N\delta_{(x_n,x_{n+1},x_{n+2})}\in\mathcal P(\mathbb T^3).
\]
For the pure radix orbit, write \(T=T_{16}:y\mapsto16y\pmod1\), and \(F(y)=(y,Ty,T^2y)\). The pure three-state empirical measure is exactly \(F_*\mu_N^{\rm radix}\). Coupling the original selected triples coordinatewise and using the \(\ell^1\)-product-circle distance yields for **every N**
\[
\boxed{W_1^{\mathbb T^3}(\Gamma_N^U,F_*\mu_N^{\rm radix})\le\frac1N\sum_{n=1}^N(T_n+T_{n+1}+T_{n+2})\le\frac{3\mathcal M_{\rm BBP}}N.}\tag{RS-3W1}
\]
Thus every weak three-time raw-state limit is the pushforward \(F_*\mu\) for a \(T\)-invariant circle limit \(\mu\). **If the authentic π orbit were normal**, the uniquely appropriate three-time shape would be
\[
\boxed{\Gamma_{\rm normal}=({\rm id},T,T^2)_*\lambda_{\rm Haar}.}\tag{RS-GraphHaar}
\]
This is NOT 3D Haar on \(\mathbb T^3\): it is supported on the one-dimensional deterministic graph \(\{(y,Ty,T^2y):y\in\mathbb T\}\), a set of 3D Haar measure zero (Fubini). It has Haar one-coordinate marginals but maximum deterministic **inter-coordinate arithmetic correlation**.

The exact Fourier signature for integer (h0,h1,h2) is
\[
\boxed{\widehat\Gamma_{\rm normal}(h_0,h_1,h_2)
=\mathbf1_{\{h_0+16h_1+256h_2=0\}}.}\tag{RS-3Res}
\]
For instance, (16,-1,0) and (0,16,-1) have coefficient **1**, whereas full 3D Haar gives zero for every nonzero frequency. These are universal **radix-16 Ward resonances**, not a failure of normality or new evidence of π normality. They occur for EVERY source-normal or source-nonnormal trajectory in the appropriate compatible limit: the arithmetic threading has moved into the *support geometry* even after edges and chronology are forgotten. To test normality we must establish the **conditional density ALONG this graph**, not its ambient uniformity.

For the finite forced orbit the corresponding exact relation is
\[
16x_n-x_{n+1}+r_{n+1}=0\pmod1,
\quad e(16x_n-x_{n+1})=e(-r_{n+1}),
\]
so its averaged resonant character tends to 1 for **every initial seed** as \(r_n\to0\). This source-resonance does NOT select the zero seed. Conversely the coherent same-forcing seed has raw three-time limit \(\delta_{(0,0,0)}\), whose Fourier coefficients equal 1 for ALL characters, not just resonant ones.

General fixed-lag m-state extension: for times n+\ell_i with nonnegative fixed \(\ell_i\), the raw-state limit equals \((T^{\ell_1},...,T^{\ell_m})_*\mu\), with the original-source coupling bound \(W_1\le m\mathcal M_{\rm BBP}/N\). A **different** type of three-dimensional observable uses disjoint finite digit blocks, whose product law under Bernoulli/Haar follows from normality; do not confuse three overlapping exact real-circle states with three independent spatial coordinates. The graph of state states is not the 3D Fisher information space of independently adjustable observation intensities in PR #402.

## RS-05. Original three-positive-atom marks become ASYMPTOTICALLY PRODUCT in the scalar raw quotient — DISCLOSED no-go

The original positive Laplace decomposition supplies source *prior mark weights*, for d=3,4,5 and coefficients c=(2,1,1):
\[
R_d(a)=\frac{c_dd}{a(a+d)},\quad p_d(a)=R_d(a)/R(a),
\qquad\beta=(6,4,5)/15.
\]
For each n use the native a_n=8n−7 and any selected circle trajectory x_n. Define the PRIOR-MARKED raw measure
\[
\widetilde\mu_N=\frac1N\sum_{n=1}^N\sum_{d\in\{3,4,5\}}p_d(a_n)\,\delta_{(d,x_n)}.
\]
The deterministic product reference is β⊗μ_N^U. Since p_d(a)=β_d[b_d(a)/\sum_eβ_eb_e(a)] with b_d=a/(a+d), for a≥9 we have \(\sum_d|p_d(a)-\beta_d|\le4/a\). (Use \(|b_d-b_e|\le2/a\) and the denominator ≥a/(a+5).) At n=1 the total L1 deviation is ≤2. Therefore for ALL N≥2,
\[
\boxed{\|\widetilde\mu_N-\beta\otimes\mu_N^U\|_{TV}
\le\frac{2+4\sum_{n=2}^N(8n-7)^{-1}}{2N}=O(\log N/N).}\tag{RS-Mark}
\]
Here TV denotes the usual one-half total variation for probability laws; both measures are supported at the same finite x_n. **Any subsequential marked raw-state limit factorizes as β⊗μ**, regardless of whether μ=Haar or δ_0! The first-order 59/164 angular source information is still present at finite n, but it washes out in the asymptotic *uncoupled prior-marked one-point quotient*. This is a new-to-program **negative implication**, not a proof that retained-source conditional/posterior-interaction marks also factorize. Native conditional three-panel history may be genuinely non-product and must be kept if used to prove a new theorem.

## RS-06. Fully source-rational finite π cylinders — OBSERVED, rigorously certified

The original positive forcing is decreasing, so for any prefix length M,
\[
A_M=\sum_{j=1}^M16^{-j}r_j < \pi/16 < A_M+\frac{16^{-M}r_{M+1}}{15}.
\]
If multiplying both interval endpoints by 16^K and taking floor gives the same integer, the first K hex digits are certified by **exact Fraction arithmetic**; no floating π oracle or assumed digit distribution. Selected finite cylinder occupancies for N=128,512,2048,4096 were computed from a rigorously certified 4099-digit original-source prefix; independent rational Machin bounds verify the first 80 digits. Illustrative selected maxima:

| N | k=1 max count and ratio 16·max/N | k=2 max and ratio 256·max/N | k=3 max and ratio 4096·max/N |
|---:|---|---|---|
| 128 | 13 ; 1.625 | 3 ; 6 | 2 ; 64 |
| 512 | 41 ; 1.28125 | 6 ; 3 | 3 ; 24 |
| 2048 | 142 ; 1.109375 | 17 ; 2.125 | 4 ; 8 |
| 4096 | 274 ; 1.0703125 | 30 ; 1.875 | 6 ; 6 |

These are finite calibrated measurements **ONLY**. At k=3, 4096 possible blocks and N≤4096 samples make large maximum ratios unsurprising. No infinite-digit prediction, normality proof, or high-resolution nonconcentration assertion follows. A de Bruijn negative control can mimic complete uniformity at a fixed finite k exactly.

## RS-07. Two candidate routes for an authentic proof, and what is NOT supplied

**Route A (maximum cylinder / maximum entropy):** From source-zero-seed arithmetic and the full integer carry/CRT transport derive for some unbounded k_j the genuine selected occupancy upper bound \(M_{k_j}\le16^{-k_j}e^{o(k_j)}\). Proving these counts from known π digits or merely restating normality is forbidden. Leverage Stoneham #395's source-grid certificate as a calibrated positive model; compare zero-seed against coherent seed and all source mutants. No such π bound currently known.

**Route B (two-clock arithmetic rigidity):** A probability invariant under both ×16 and an arithmetically independent ×3, jointly ergodic with positive entropy, is Haar by Rudolph–Johnson. This could lower the required entropy threshold at the cost of a MUCH stronger second invariance. The '3' and '5' appearing as original Laplace-pole shifts are **not** ×3 or ×5 endomorphisms of π's selected circle orbit; no such additional invariance follows. A mixture of Haar and a rational orbit shows joint ergodicity is an essential issue. This is a *conditional research route*, not an established SUCC operation.

**Route C (source-to-grid buffered Wasserstein):** Build selected original-four-pole rational surrogates and prove uniform nonconcentration of their counts in **buffered** b-adic intervals, with both seam/edge leak and fixed-precision arithmetic controlled using RS-buffer. PR #399 denominator growth and #405 selected slips alone are insufficient, but their exact CRT data are potential instruments. A proof must distinguish true selected s=0 from coherent same-forcing s*=−π/16.

**Status ledger:** RS-01 well-defined quotient and classical symbolic invariance DISCLOSED. RS-02 original-source W1 and buffered bridge DISCLOSED. RS-03 max-cylinder/entropy rigidity CLASSICAL theorem with SUCC-specific quantified application (not pi result). RS-04 bare support, finite k, noninvariance and coordinate gauge falsifiers DISCLOSED. RS-04a three-time graph-Haar and 3D W1 DISCLOSED. RS-05 prior-mark factorization DISCLOSED. RS-06 finite pi prefixes OBSERVED/certified. RS-07 source-specific max-cylinder bound, ×3 invariance, signed grid saving UNVERIFIED/OPEN. **No p-adic conductor → normality shortcut, no physical spacetime or Noether claim.**

## External mathematics / research provenance

- Original BBP dynamical map and Hypothesis A: Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10 (2001), DOI https://doi.org/10.1080/10586458.2001.10504441.
- Classical Stoneham controls: Bailey–Crandall, *Random Generators and Normal Numbers*, Experimental Mathematics 11 (2002), DOI https://doi.org/10.1080/10586458.2002.10504704.
- Unique full-shift maximal-entropy measure: Climenhaga–Thompson et al., *On intrinsic ergodicity and weakenings of the specification property*, Advances in Mathematics 2016, https://doi.org/10.1016/j.aim.2016.03.013, full-shift lemma; classical proof from entropy subadditivity is reproduced above.
- Rudolph, *×2 and ×3 invariant measures and entropy*, Ergodic Theory and Dynamical Systems 10 (1990), https://doi.org/10.1017/S0143385700005629; conditional joint-ergodic + positive-entropy rigidity. Source original pole shifts are not endomorphism symmetries.
- Related SUCC: PR #390/#395/#399/#400/#403/#405/#406. Do not import unfinished draft results as historical certified theorems without parent/source status.

## Next falsifier

Try to prove an all-horizon selected occupancy amplification reversal: if some k-block law remains ε-biased, prove from the original four signed poles and selected zero boundary that no exponentially concentrated family of mk-block cylinders can exist. Require finite-grid exact source surrogates, source/seed controls, coherent changed seed, source-mutant jet matches, full real-circle CRT and integer seams, normal Stoneham and nonnormal de Bruijn/bias. A merely large conductor, logarithmic slip, or an O(log N/N) prior-mark factorization will not distinguish the limit measures. Preserve every failure and the raw test receipts.

**Validation scope:** standalone exact stdlib tests, a separately implemented rational Machin/BBP interval and 80-dps Gamma/entropy oracle, and remote Git blob identity. Complete SUCC root provenance/unit/observer/ordinal, hosted exact-head CI, Lean and external blind referees NOT RUN on this additive research child. No merge or theorem-status promotion without authorization.
