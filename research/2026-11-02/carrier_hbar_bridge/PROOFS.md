# Carrier-relative ħ: the original BBP 16-adic Haar theorem, selected-real anti-alias and source passports

**Research-only paper derivations, 2026-11-02.** Exact ancestor #467 at 1bbc2b69d79a5c85df10459c13173563ca44bcd3, itself stacked on #466→#464→#463→#462→#460→#459, rooted in merged Main XIX 81045770234a114247e43eb08ae5c6d446e9514a. Original four signed poles, U_0=0, frozen proofs, formal/Lean and production are unchanged. **NO π-normality or RH claim.**

## 0. What "carrier-relative ħ" actually means

SUCC #441 AQC-01/02 defines on the finite cyclic carrier \(A_r=\mathbb Z/16^r\mathbb Z\) the unit shift \(S_a\) and finite clock \(C_k\), with the *exact exponentiated Weyl relation*
\[
C_kS_a=e(ka/16^r)S_aC_k,\quad e(x)=\exp(2\pi ix).
\]
For the primitive pair the dimensionless carrier phase mesh is
\[
\boxed{\theta_r=2\pi/16^r.}
\]
This is NOT physical Planck's constant. Its associated real seed aperture \(\delta_r=16^{-r}\) has the same numerical scale, but lies in a DIFFERENT carrier; a real↔2-adic identification requires explicit source, carry and orientation transport.

Keep the single authentic four-pole source
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
The completed Archimedean point is \(\alpha=\pi/16\); the positive summable Green tail satisfies
\[
\boxed{U_n=16^n\alpha-T_n,\quad T_n=\sum_{j\ge1}16^{-j}r(n+j)>0,\quad \sum_nT_n<\infty.}
\]
These are the inherited source/BPP identities.

## 1. HBR-01 — exact all-resolution source-local Haar and moving-carrier power saving (INHERITED proof, NEW synthesis)

SUCC research/2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md, DSI-1..4, already proves that the ORIGINAL source has a bijective 2-adic isometry
\[
F(t)=\sum_{j\ge0}16^jr(t-j),\qquad F(0)=0,\quad F(n)=U_n\in\mathbb Q_2.
\]
The analytic proof of the nontrivial backwards-source identity \(F(0)=0\) is in that earlier paper. This round separately recalibrated it to 400 bits; that computation is not the proof.

For \(Q=16^r\), define \(a_{n,r}=F(n)\pmod Q\in A_r\). Isometry implies \(a_{n+Q,r}=a_{n,r}\) for all n, and \(a_{0,r},\ldots,a_{Q-1,r}\) permute all Q residues. Therefore, for EVERY integer k not divisible by Q,
\[
\boxed{\sum_{n=0}^{Q-1}e(k a_{n,r}/Q)=0,\qquad
\left|\frac1N\sum_{n=0}^{N-1}e(k a_{n,r}/Q)\right|\le\frac QN.}
\]
Proof: the complete period is a character sum over A_r, hence zero; split an arbitrary prefix into complete periods and fewer than Q leftover terms. In particular if \(r(N)\le(1-\varepsilon)\log_{16}N\), the original-source finite-carrier character sum has uniform \(N^{-\varepsilon}\) cancellation over ALL nontrivial local k, at a resolution refining with N. This genuinely solves a **2-adic carrier-relative Haar problem**, NOT π's real-circle normality.

## 2. HBR-02 — exact causal seed-aperture resolution phase transition (PROVED, mostly universal)

For any unit-phase sequence \(z_n=e(hU_n)\), nonzero integer h, and finite N, let
\[
W_N(s)=\sum_{n=0}^{N-1}z_n e(h16^n s),\quad
B_{N,r}=\delta_r^{-1}\int_0^{\delta_r}W_N(s)\,ds,\quad \delta_r=16^{-r}.
\]
Term-by-term integration gives \(B_{N,r}=\sum_{n<N}z_nK_{n,r,h}\), with
\[
K_{n,r,h}=\int_0^1e(h16^{n-r}t)\,dt.
\]
For every n>=r the exponent has nonzero integer winding, so \(K_{n,r,h}=0\) EXACTLY; for n<r,
\(|K_{n,r,h}-1|\le\pi|h|16^{n-r}\) by integrating \(|e(x)-1|\le2\pi|x|\). Hence
\[
\boxed{|B_{N,r}|\le\min(N,r).}
\]
Moreover (these are UNNORMALIZED errors):
\[
\boxed{|W_N(0)-B_{N,r}|\le(N-r)+\pi|h|/15\quad(r\le N),}
\]
\[
\boxed{|W_N(0)-B_{N,r}|\le(\pi|h|/15)16^{N-r}\quad(r\ge N).}
\]
Thus for ANY phase sequence \(B_{N,r(N)}/N\to0\) if \(r(N)=o(N)\); this apparent causal uniformity is source BLIND and even holds on coherent nonnormal orbits. Conversely if \(r(N)=N-o(N)\), normalized \(B_{N,r}\) agrees with the true selected signed Weyl mean up to o(1), so proving its vanishing is the original unresolved normality condition.

The threshold is sharp on the SAME-four-pole coherent real counterseed \(s_*=-\alpha\): here \(U_n(s_*)=-T_n\), so \(z_n^*\to1\) with summable errors. If \(r(N)/N\to\lambda\in[0,1]\), then \(B^*_{N,r}/N\to\lambda\), whereas \(W_N^*(0)/N\to1\). This is an exact source-calibrated version of the shrinking-seed aperture warning inherited from #404, not a new signed estimate.

## 3. HBR-03 — the real phase lives in the odd-denominator cofiber (PROVED, exact source-passport)

For the authentic U_n, choose the unique 2-adic residue \(a_{n,r}\in[0,Q)\) and write
\[
U_n=a_{n,r}+Qv_{n,r},\qquad v_{n,r}\in\mathbb Z_{(2)}.
\]
This is an EXACT rational identity at the real embedding, and \(Qv_{n,r}\) holds all the retained integer/carry/odd-prime information. The two correctly typed character equations are
\[
\boxed{e(hU_n/Q)=e(h a_{n,r}/Q)\,e(hv_{n,r})},
\quad
\boxed{e(hU_n)=e(hQv_{n,r}).}
\]
At the target integral real harmonic h, the local factor \(e(ha_{n,r})=1\) and its finite clock is precisely a HIGH ALIAS. Local Haar cancellation cannot simply be transported through this quotient; the entire selected Archimedean phase resides in the cofiber. This gives a source-attested algebraic form of #441/#461's no-direct-real-character rule.

## 4. HBR-04 — NEW all-r *selected original* real-circle phase separation (PROVED, not normality)

**Classical expanding-circle gap lemma.** For b>=2 and irrational β,
\[
\limsup_{n\to\infty}\|b^n\beta\|_{\mathbb R/\mathbb Z}\ge1/(b+1).
\]
Proof: if the limsup were below 1/(b+1), choose c between them. Center the nearest-integer errors \(\epsilon_n=b^n\beta-m_n\). Eventually \(|\epsilon_n|,|\epsilon_{n+1}|<c\), hence the integer \(m_{n+1}-bm_n=b\epsilon_n-\epsilon_{n+1}\) has absolute value <(b+1)c<1, so vanishes. Then \(\epsilon_{n+1}=b\epsilon_n\) indefinitely; boundedness forces \(\epsilon_n=0\), contradicting irrationality. The rational β=1/17 has exactly 1/17 error under b=16, so do not claim an improved bound uniformly over ALL reals.

Fix ANY carrier r>=1, \(Q=16^r\), integer h!=0, and
\(\beta=h(16^Q-1)\pi/16\), irrational. The exact original source-tail bridge gives
\[
U_{n+Q}-U_n=16^n(16^Q-1)\pi/16-(T_{n+Q}-T_n)
\]
with tail error tending zero. The gap lemma and phase continuity therefore yield the genuinely original-source selected-real theorem
\[
\boxed{\limsup_{n\to\infty}|e(hU_{n+Q})-e(hU_n)|\ge2\sin(\pi/17).}
\]
Yet \(a_{n+Q,r}=a_{n,r}\) EXACTLY for all n. Thus for ANY fixed observation \(f_r:A_r\to\mathbb C\), no matter how nonlinear or calibrated,
\[
\boxed{\limsup_{n\to\infty}|e(hU_n)-f_r(a_{n,r})|\ge\sin(\pi/17).}
\]
Apply the triangle inequality to the two equal carrier labels and the two separated real target phases. This is a quantitative **all-level original-source real nonfactor theorem**, extending earlier finite nofactor examples. It FAILS, correctly, for the same-exact-source changed real seed \(s_*=-\pi/16\), because \(U_n(s_*)=-T_n\to0\).

This proves infinitely repeated real phase noncoherence across each fixed carrier-alias lag. It supplies NO positive-density cancellation, no Weyl decay and no claim of π normality.

## 5. HBR-05 — NEW selected REAL lag-energy logarithmic lower bound (PROVED using published irrationality measure)

Import the PUBLISHED Zeilberger–Zudilin theorem \(\mu(\pi)\le7.103205334137\ldots<15/2\); we use only the conservative exponent \(15/2\). There is an unspecified C>0 such that for all sufficiently large rational denominators q (unreduced also allowed),
\[
|\pi-p/q|\ge Cq^{-15/2}.
\]
For fixed \(Q=16^r,h\ne0\), the source tail obeys \(h|T_{n+Q}-T_n|\to0\). Choose late time M so that it is <1/96 for n>=M.

**No-long-lock theorem.** For every sufficiently large integer M, at least one n in the half-open interval \([M,8M)\) has
\[
\boxed{\|h(U_{n+Q}-U_n)\|_{\mathbb T}\ge1/32.}
\]

Proof: if none did, every \(\|16^n\beta\|<1/32+1/96=1/24<1/17\) on all 7M consecutive integer indices. The same nearest-integer argument as §4 shows exactly \(\epsilon_{j+1}=16\epsilon_j\) across the entire interval, with NO integer carry. Thus \(|16^M\beta-m|<(1/24)16^{-(7M-1)}\). Put \(K=h(16^Q-1)\) and \(q=|K|16^{M-1}\); then
\[
|\pi-p/q|<(1/24)16^{-(7M-1)}/q
\]
for an integer p (adjusting sign if needed). This contradicts the imported \(Cq^{-15/2}\), since q is a fixed-K multiple of \(16^M\), and the upper/lower exponents are respectively approximately \(-8M\) and \(-7.5M\). QED.

The disjoint intervals \([8^jM_0,8^{j+1}M_0)\) thus each contain an original selected real-phase mismatch at least 1/32 turn. Define the *genuinely source-selected* fixed-carrier-lag energy
\[
\mathcal E_{N,Q,h}=\sum_{n=0}^{N-Q-1}|e(hU_{n+Q})-e(hU_n)|^2.
\]
Then the all-N quantitative conclusion is
\[
\boxed{\mathcal E_{N,Q,h}\ge
\frac{4\sin^2(\pi/32)}{\log8}\log N-O_{r,h}(1).}
\]
The onset M_0 is not effective here because an explicit Diophantine constant C is not extracted. This is a genuine original-source ALL-HORIZON real signed-phase nonlocking inequality, but **logarithmic energy is much weaker than the extensive/multiscale bound needed for Weyl cancellation**. It does not dominate SUCC's existing DC logarithmic absolute-loss result because that result controls a different stronger total-correlation observable.

**Decisive hostile control (linear lag energy still insufficient):** keep the SAME authentic four poles but change the real initial seed to \(s=1/7-\pi/16\). Then \(U_n(s)=16^n/7-T_n\). Because 16 mod7=2 has order 3 and Q=16^r≡1 mod3, \(16^Q≡2\pmod7\). Thus for h=1 every fixed-Q lag circle separation is eventually at least 1/7 turn, so \(\mathcal E_{N,Q,1}\gg N\), MUCH stronger than the original bound. Yet its h=1 Weyl mean is NONZERO:
\[
\lim_{N\to\infty}\frac{S_N(1;s)}N=
\frac{e(1/7)+e(2/7)+e(4/7)}3,\qquad
\left|\lim\frac{S_N}N\right|^2=\frac29.
\]
The last identity follows because the six ordered nonzero differences between 1,2,4 exhaust residues 1,...,6 mod7, giving \(|\zeta_7+\zeta_7^2+\zeta_7^4|^2=3+\sum_{k=1}^6\zeta_7^k=2\). Even LINEAR one-lag dissipation alone cannot prove normality. This source-matched changed-seed control is not the authentic zero-selected path.

## 6. HBR-06 — cross-completion source passport rejects recent rational-atom and entire echoes (PROVED)

The inherited genuine 2-adic source passport is the **nontrivial analytically proved** value
\[
\boxed{F_{\mathrm{BBP}}(0)=\sum_{j\ge0}16^jr(-j)=0\in\mathbb Q_2.}
\]
The CE-03 positive rational-atomic counterfeit reproduces r(1)..r(4), but has
\(r_a(n)=\sum_iw_ix_i^{n-1}\), positive rational nodes \(x_i\in(0,1)\) with \(v_2(x_i)<4\) and rational positive weights. The atomwise p-adic series converges, since \(v_2(16/x_i)>0\). Therefore
\[
\boxed{F_a(0)=\sum_{j\ge0}16^j r_a(-j)
=\sum_i\frac{w_i}{x_i-16}=-\alpha_a.}
\]
For the explicit CE-03 quadrature,
\(\alpha_a=4062342947075618/20689342837729335\), with \(v_2(\alpha_a)=1\). Consequently \(F_a(0)\ne0\pmod{16}\), whereas the ORIGINAL F(0) vanishes modulo 16^r for EVERY r. This is a precise **finite source-class distinction**, even though four original positive time moments agree. The rational completed number and the p-adic backward boundary belong to different completions but are canonically comparable HERE because the atomic model's both sums are the SAME well-defined rational \(\alpha_a\); no "2-adic value of π" is invented.

The separate CE-01 M=4 smooth positive rational-epsilon entire echo also fails the 2-adic source domain as soon as its forcing differs: the exact first nonzero correction satisfies \(v_2(\delta r(5))=-16\), so the altered r(5) is not even 2-integral. This does not show that EVERY source echo lacks a lawful 2-adic interpolation; it certifies a concrete one. Both controls changed the original source and must not be used to refute a genuine complete-four-pole theorem.

## 7. HBR-07 — fully source-certified real \(\hbar\) snapshots, but finite-horizon only (PROVED algorithmically)

The original finite BBP rational completion \(\alpha_B=\sum_{j=1}^B16^{-j}r(j)\) obeys SUCC #465's proved Gamma/Beta bound
\[
0<\alpha-\alpha_B\le16^{-B}/[(8B+1)(8B+2)].
\]
At an arbitrary finite real phase horizon n<=N and arbitrary carrier resolution r>=1, choose B=N+r. Then
\[
0<16^n(\alpha-\alpha_B)\le
16^{-r}/[(8B+1)(8B+2)]<16^{-r}.
\]
So one RATIONAL source completion certifies all original π-orbit phase positions to better than ONE real \(\hbar\)-cell at once. If a rational interval straddles a real bin boundary, increase B; this halts for each finite n,r because π is irrational and no \(\{16^n\alpha\}\) equals a rational bin boundary. **All finite real \(\hbar\)-histograms are constructibly certifiable**, though no uniform-in-N histogram convergence is proved.

Finite all-exact source witness: the first 256 original states give exactly 16 observations in every LOCAL 16-adic mod16 residue, whereas the REAL circle's 16 equal bins have counts ranging from 12 to 23. At local mod256 all 256 residues occur once; the REAL circle visits only 163 of its 256 bins. These are exact Fraction counts with no trigonometric rounding and demonstrate finite non-descent—not asymptotic nonnormality.

## 8. Honest verdict and next falsifier

**Earned:** exact source-local 16-adic signed Haar with moving-resolution power rate (inherited DSI, newly organized with AQC θ_r), quantitative selected-original all-level REAL alias separation, original source fixed-carrier-lag logarithmic REAL anti-locking energy (with published μ(π) input), sharp carrier seed-blur calibration, typed source-local/real cofiber, and finite 2-adic rejection of two prior positive changed-source countermodels.

**Still OPEN:** original \(S_N(h)=o_h(N)\) for all fixed h!=0, the all-prime mixed original 5-mod8 clock/cofactor signed saving of #460, the growing signed Haar loss hypothesis D_J→∞ of #468, π normality, RH. Neither a finite Weyl uncertainty support bound, a universal seed blur, an exact local Haar permutation nor a sparse real anti-lock result supplies the needed phase cancellation. The SAME-source coherent seed and periodic 1/7 seed prove why these distinctions are essential.

### Provenance
- SUCC original dyadic isometry and analytic backwards boundary: https://github.com/femboy2112/SUCC/blob/main/research/2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md (DSI-1..8, INHERITED).
- SUCC finite carrier Weyl pairing θ_r: https://github.com/femboy2112/SUCC/pull/441 (AQC-01/02, INHERITED).
- SUCC #467 positive entire/rational atoms, #465/#468 Gamma tail and signed Haar cascade, #459/#460 prime windows: explicitly INHERITED.
- Zeilberger–Zudilin, 2020 published μ(π)<7.103205334137..., https://doi.org/10.2140/moscow.2020.9.407 ; only the weaker 15/2 is used.
- Bailey/Borwein/Plouffe, Math. Comput. 66 (1997), 903–913, https://doi.org/10.1090/S0025-5718-97-00856-9 .

The test suite checks exact finite statements; the all-horizon claims come from the displayed derivations and classical irrationality input, NOT finite computation or Lean kernel checking.
