# Operation OILY → ħ: moving-carrier anti-alias, height-optimality firewall, and conditional real cofiber

**Date:** 2026-11-02. **Status:** research-only, paper derivations and finite exact certificates. This is a proof attempt toward original base-16 π normality, **NOT A PROOF OF NORMALITY**. Exact parent #469 head ef6f8894741cac8d952e9fd12d49e4aa7d13fa25; #469 stacked on #467/#466/#464/#463/#462/#460/#459 and merged Main XIX 81045770234a114247e43eb08ae5c6d446e9514a. Gamma-seam #468 is a separately read sibling, NOT merged into this branch. No original four signed poles, literal zero seed, historical contracts, production, CI, Lean or main modified.

## 0. Frozen authentic object and notation

Write \(b=16\), \(e(x)=\exp(2\pi ix)\) and
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\tag{0}
\]
The original completed real boundary \(\alpha=\sum_{n\ge1}16^{-n}r(n)=\pi/16\) has the positive future Green tail
\[
U_n=16^n\alpha-T_n,\quad
T_n=\sum_{j\ge1}16^{-j}r(n+j)>0,\qquad T_n\downarrow0,\quad\sum_{n\ge0}T_n<\infty.
\tag{1}
\]
All these identities, and the exact original positive source Hausdorff representation, are inherited from SUCC (including #440, #465, #468). The authentic dyadic isometry \(F:\mathbb Z_2\to\mathbb Z_2\), with analytically proved \(F(0)=0\) and \(F(n)=U_n\), is inherited from research/2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md. Thus for \(Q=16^r\),
\[
\boxed{U_n\equiv U_m\pmod Q\quad\Longleftrightarrow\quad n\equiv m\pmod Q.}
\tag{2}
\]
This is EXACT finite **local** carrier arithmetic, not a real-circle continuity theorem. The dimensionless carrier-Weyl phase mesh \(\theta_r=2\pi/16^r\) is inherited from #441 and is NOT physical Planck's constant.

## OMH-01. HEIGHT-ONLY decoder requires LINEAR carrier depth (PROVED and sharp in declared class)

For each n≥1 put \(L_n=\operatorname{lcm}(1,\dots,8n)\), \(H_n=16^nL_n\), and define the admissible rational height class
\[
\mathcal H_n=\left\{A/B\in\mathbb Q:\ 0<A/B<16^n,\quad
1\le B\le L_n\text{ odd},\quad 0<A<H_n\right\}.
\tag{3}
\]
The authentic original rational U_n belongs to this class, since its original pole denominators all divide L_n. A height-only observer receives a 16-adic residue \(\bmod Q=16^r\), n and these bounds, **but not the full exact four-pole formula as an additional computing oracle**.

**Elementary exact obstruction:** for EVERY n≥1 and 1≤r≤2n−1 put Q=16^r and
\[
\boxed{x=1,\qquad y=\frac{Q+1}{2Q+1}.}\tag{4}
\]
Both lie in \(\mathcal H_n\). Indeed, \(2Q+1\le2^{8n-3}+1\le2^{8n-1}\le L_n\) by the classical elementary lcm lower bound \(\operatorname{lcm}(1,\dots,m)\ge2^{m-1}\) for m≥8 (Chan–Norrish). Both reduced denominators are odd, the numerator heights pass and both are in (0,16^n). Since \(2Q+1\equiv Q+1\equiv1\pmod Q\),
\[
\boxed{x\equiv y\equiv1\pmod Q,\qquad
\|x-y\|_{\mathbb R/\mathbb Z}
=\frac Q{2Q+1}\ge\frac{16}{33}.}\tag{5}
\]
Their complex real-circle phases therefore differ by at least \(2\sin(16\pi/33)\), so any decoder that assigns ONE phase to that local residue commits error at least \(\sin(16\pi/33)\) on one of the two height-admissible rationals. This is an exact nonuniform-local-to-real obstruction, not an example of two legitimate authentic four-pole time states.

**Asymptotically sharper lower and upper depth.** By the classical prime number theorem, \(\log L_n=\psi(8n)=8n+o(n)\). Hence for every fixed ε>0, for all sufficiently large n, the collision (4) remains inside \(\mathcal H_n\) for
\[
\boxed{1\le r\le\left(\frac8{\log16}-\varepsilon\right)n
\quad(\text{about }(2.88539-\varepsilon)n).}\tag{6}
\]
Conversely the rational cross-product uniqueness theorem already in #469 says that \(Q>2H_nL_n=2\cdot16^nL_n^2\) suffices. Thus, via the SAME PNT input, a depth
\[
\boxed{r\ge\left(1+\frac{16}{\log16}+\varepsilon\right)n
\quad(\text{about }(6.77078+\varepsilon)n)}
\tag{7}
\]
suffices for all large n. The entirely elementary explicit bound r=10n from #469 remains valid at EVERY n. These are upper/lower information bounds ONLY for the *height-only* decoder class; they do not refute recovering U_n by evaluating the fully known original source at time n. The two guarantees prove an intrinsic **linear scale** for worst-case rational height decoding, while the local Haar theorem has useful power savings only at depth r≲log16N.

## OMH-02. Moving-\(\hbar\) ORIGINAL selected REAL nonlocking across ALL carrier levels Q≤M (PROVED PAPER)

Import ONLY the published Zeilberger–Zudilin result \(\mu(\pi)<15/2\). Thus there is C>0 such that for every rational p/q with integer p and positive integer q,
\[
\boxed{|\pi-p/q|\ge Cq^{-15/2}.}\tag{8}
\]
The constant C may be ineffective; the inequality holds for unreduced denominators too, since q only enlarges. We do not infer any unverified new claim about π's irrationality exponent.

**Theorem.** For every fixed nonzero integer h there exists \(M_0(h)\) such that for EVERY integer M≥M0 and EVERY integer r≥1 with Q=16^r≤M, there is at least one
\[
\boxed{M\le n<15M:\qquad
\|h(U_{n+Q}-U_n)\|_{\mathbb R/\mathbb Z}\ge1/32.}
\tag{9}
\]
Importantly M0 is INDEPENDENT of r. Both n and n+Q are inside the finite time interval [M,16M), and their original source-local carrier residues are IDENTICAL by (2).

**Proof.** Let \(K=h(16^Q-1)\), \(\beta=K\pi/16\). The true original phase difference is
\[
h(U_{n+Q}-U_n)=16^n\beta-h(T_{n+Q}-T_n).
\]
Because T_n is positive, decreasing and O(n^-2), choose M0(h) large enough that \(|h(T_{n+Q}-T_n)|<1/96\) for ALL n≥M0 and ALL Q≥1. If (9) failed for some M,r, then \(\|16^n\beta\|<1/24\) for ALL 14M consecutive indices n=M,...,15M−1. Let \(\epsilon_n=16^n\beta-m_n\) be the nearest-integer error. Since \(|16\epsilon_n-\epsilon_{n+1}|<17/24<1\) and \(16\epsilon_n-\epsilon_{n+1}=m_{n+1}-16m_n\in\mathbb Z\), it is ZERO. Iterating gives
\[
|\epsilon_M|<\frac1{24}16^{-(14M-1)}.
\]
But \(16^M\beta=K16^{M-1}\pi\). Set \(q=|K|16^{M-1}\), and let p be the corresponding nearest integer (adjusting sign of h). Then
\[
\boxed{|\pi-p/q|<\frac{16^{-(14M-1)}}{24q}.}\tag{10}
\]
Since Q≤M, \(q\le|h|16^{M+Q-1}\le|h|16^{2M-1}\). Combine (8) and (10):
\[
C < \frac1{24}16^{-(14M-1)}q^{13/2}
\le C_h\,16^{-14M+(13/2)(2M)}=C_h16^{-M},
\]
impossible for ALL sufficiently large M, with M0 depending only on h. QED.

**Shorter shell at moving smaller Q:** using n∈[M,8M), seven M successive indices, the same proof gives a uniform witness whenever \(Q\le M/16\), since \(7-(13/2)(1+1/16)=3/32>0\).

This is an original-source selected REAL phase mismatch theorem on **growing carrier levels**, not merely the fixed-Q HBR-05 theorem of #469. It still uses only irrationality-measure information about the completed \(\pi\) boundary and the summable Green tail. It proves no density or signed Weyl cancellation.

## OMH-03. Genuine \(\log^2 N\) selected real MULTISCALE anti-alias energy (PROVED PAPER)

Let \(z_n=e(hU_n)\) for fixed h!=0. For arbitrary integer N≥2 define
\[
\boxed{
E_N^{\rm multi}(h)=
\sum_{\substack{r\ge1\\16^r<N}}
\sum_{n=0}^{N-16^r-1}|z_{n+16^r}-z_n|^2.}
\tag{11}
\]
For every sufficiently large j, apply (9) with M=16^j and each r=1,...,j. It supplies at least one n in [16^j,15·16^j) with n+16^r<16^{j+1} and
\[
|z_{n+16^r}-z_n|^2\ge4\sin^2(\pi/32).
\]
Choose \(J=\lfloor\log_{16}N\rfloor\). Summing the witnesses over all j from the fixed source-dependent j0 to J−1 and all r=1,...,j yields
\[
\boxed{E_N^{\rm multi}(h)\ge
4\sin^2(\pi/32)\sum_{j=j_0}^{J-1}j.}
\tag{12}
\]
In particular,
\[
\boxed{\liminf_{N\to\infty}
\frac{E_N^{\rm multi}(h)}{(\log_{16}N)^2}
\ge2\sin^2(\pi/32)>0.}
\tag{13}
\]
The rate is a real all-horizon selected phase statement at O(logN) simultaneous carrier levels, proved analytically; finite exact tests in this PR are NOT extrapolated to support it.

**Important "Oily" collapse firewall:** for any unit phases \(z_n\), choose a unit common direction \(\xi=S_N/|S_N|\) (arbitrary if S_N=0). Then \(\sum_n|z_n-\xi|^2=2(N-|S_N|)\). For each fixed Q, pairwise triangle/Cauchy imply
\[
\sum_{n<N-Q}|z_{n+Q}-z_n|^2\le8(N-|S_N|).
\]
Summing over \(R=\lfloor\log_{16}N\rfloor\) lags gives
\[
\boxed{E_N^{\rm multi}(h)\le8R(N-|S_N(h)|).}\tag{14}
\]
Therefore (13) certifies only \(N-|S_N(h)|=\Omega_h(\log N)\), NOT \(o(N)\). SUCC's earlier 2026-10-26/OILY_DIRECT_ARITHMETIC.md ALREADY proved the stronger explicit logarithmic original-source deficit \(N-|S_N(h)|\ge(\log_8N)/29-O_h(1)\). No false novelty or asymptotic-order improvement is claimed here.

## OMH-04. Same-source nonnormal \(\mu=2\) adversary (PROVED from published classical theorem)

For k≥0 let t_k be the binary Thue–Morse sequence, t0=0, t_(2k)=t_k, t_(2k+1)=1−t_k, and define
\[
c_{\rm TM}=\sum_{k=0}^\infty t_k\,16^{-(k+1)}.
\]
All its base-16 digits are 0 or 1, so it is **not base-16 normal**. Bugeaud (Annales de l'Institut Fourier 61 (2011), 2065–2076) proves the Thue–Morse–Mahler number has irrationality exponent EXACTLY 2 for every integer base b≥2. Multiplication by 1/16 preserves that exponent, hence \(\mu(c_{\rm TM})=2\).

Run the SAME authentic exact four-pole forcing but change only its real initial seed to \(s_{\rm TM}=c_{\rm TM}-\pi/16\). Then
\[
U_n(s_{\rm TM})=16^nc_{\rm TM}-T_n.
\]
Because the T_n correction is summable, this orbit is nonnormal. Nonetheless the full OMH-02 moving-Q anti-alias theorem applies to it by replacing π/16 with c_TM and using its STRONGER finite irrationality exponent. Thus even uniform moving-\(\hbar\) real anti-alias energy plus the exact original forcing is insufficient without the authentic real/2-adic zero-seed identification. The altered irrational seed is NOT an admissible rational 2-adic state and does NOT satisfy the original U0=0 hypothesis; this is a precisely scoped nonnormal control, not a refutation of an original-source selected theorem.

A separate SAME-four-pole periodic seed \(s=1/7-\pi/16\) has \(|S_N(1;s)/N|^2\to2/9\) but linear fixed-Q lag energy; it also satisfies the moving-Q mismatch conclusion, without an irrationality exponent. Both show mismatch energy does not force normality.

## OMH-05. Exact **conditional carrier/cofiber signed energy** and an actual new unproved sufficient target

For every \(Q=16^r\mid N\), define \(a_{n,r}=U_n\bmod Q\). Since the original F is isometric, \(a_{n,r}\) permutes the time residue labels, and \(n\equiv m(Q)\) iff \(a_{n,r}=a_{m,r}\). Let
\[
A_a=\sum_{\substack{0\le n<N\\n\equiv a(Q)}}z_n,\qquad
\boxed{G_{N,Q}(h)=\frac Q{N^2}\sum_{a=0}^{Q-1}|A_a|^2
=\frac1Q\sum_a\left|\frac QN A_a\right|^2.}
\tag{15}
\]
This is the mean-squared **selected real character conditioned on a genuine source-local carrier cell**, not independent Haar averaging. Finite discrete Parseval yields the exact identities
\[
\boxed{
G_{N,Q}(h)=\sum_{k=0}^{Q-1}
\left|\frac1N\sum_{n=0}^{N-1}z_n e(-k a_{n,r}/Q)\right|^2
=\frac Q{N^2}\sum_{\substack{n,m<N\\n\equiv m(Q)}}z_n\overline{z_m}.}
\tag{16}
\]
Cauchy gives
\[
\boxed{|S_N(h)/N|^2\le G_{N,Q}(h)\le1.}\tag{17}
\]
The right bound uses exactly N/Q indices per class; Q must divide N. A coherent constant phase gives G=1 and FAILS the hoped-for o(1). The first bound is precisely the signed-sum/spectrum connection needed to transfer a genuinely SOURCE-DERIVED joint real/local inequality to π normality.

**Quantified conditional normality route (UNVERIFIED INPUT):** Fix any ε∈(0,1). Suppose for EVERY fixed h!=0 there exist A_h,C_h>0 and an all-prefix-dense choice of admissible \(Q_N=16^{r_N}\) with \(16\le Q_N\le N^{1-\varepsilon}\), and \(M_N=Q_N\lfloor N/Q_N\rfloor\) (so N−M_N<Q_N), for which the ACTUAL four-pole/zero-seed sources satisfy
\[
\boxed{G_{M_N,Q_N}(h)\le
C_h\,Q_N(\log N)^{A_h}/M_N}\tag{18}
\]
for all sufficiently large N. Then
\[
\frac{|S_N(h)|}{N}
\le\sqrt{\frac{C_h Q_N(\log N)^{A_h}}{M_N}}
+\frac{Q_N}N
=O_h\big(N^{-\varepsilon/2}(\log N)^{A_h/2}\big)\to0.
\]
Weyl and the exact Green tail imply base-16 π normality. This is a REAL, strong, SOURCE-SELECTED sufficient inequality, much stronger than normality and **NOT PROVED**. It is not an inference from finite local Haar or from positivity. It requires control of the genuinely signed time-pair cofactor in (16), and a proof that the fixed original forcing/zero seed satisfies it. If it fails, seek a weaker o(1) conditional bound; neither should be assumed.

**Original Gamma seam conditional-energy transport (PROVED but NOT cancellation).** Define \(\widehat z_n=e(h16^n\alpha)\) with the SAME authentic source and \(\alpha=\pi/16\), and let \(\widehat G\) use the same carrier partition. Reverse triangle/Minkowski and \(|z_n-\widehat z_n|\le2\pi|h|T_n\) give, for ALL Q|N,
\[
\boxed{|\sqrt{G_{N,Q}^U(h)}-\sqrt{G_{N,Q}^\pi(h)}|
\le \frac{2\pi|h|\sqrt Q}{N}\sum_{n\ge0}T_n.}
\tag{19}
\]
The right side tends zero uniformly when Q≤N. This correctly combines SUCC #465/#468 Gamma source-tail transport with a genuinely new conditional real/cofiber observer. It still supplies **no upper estimate on either G**.

**Source-selected but very weak conditional noncoherence:** For N=16M with M a power of16, every Q=16^r≤M divides N. OMH-02 finds an actual within-class n,n+Q≤N with \(|z_{n+Q}-z_n|^2\ge4\sin^2(\pi/32)\). The exact conditional variance identity
\[
1-G_{N,Q}(h)=\frac{Q}{2N^2}\sum_{\substack{n,m<N\\n\equiv m(Q)}}|z_n-z_m|^2
\]
therefore gives
\[
\boxed{1-G_{N,Q}(h)\ge
\frac{4Q}{N^2}\sin^2(\pi/32)>0.}
\tag{20}
\]
This is a genuine original-source upper \(G<1\), uniform at moving Q≤M, but vastly too small to imply (18), let alone normality.

## OMH-05B. An exact refinement monotonicity obstruction (PROVED, universal)

The conditional energy (15) is monotone **NONDECREASING** under carrier refinement at a fixed, divisible horizon. For divisors \(Q_1\mid Q_2\mid N\), group each \(Q_1\)-class as \(t=Q_2/Q_1\) finer classes. Cauchy–Schwarz gives \(|\sum_{j=1}^t A_j|^2\le t\sum_j|A_j|^2\), hence
\[
\boxed{G_{N,Q_1}(h)\le G_{N,Q_2}(h),\quad
G_{N,1}(h)=|S_N(h)/N|^2,\quad G_{N,N}(h)=1.}\tag{20a}
\]
This is a finite exact fact for ANY unit phases. It creates a nontrivial design constraint: increasing carrier precision while observing the same finite time span cannot *by itself* reduce the normalized conditional real-energy upper bound. In particular a good finite \(Q=16\) estimate cannot be extrapolated mechanically to growing Q, even though the original carrier source is exactly Haar at both levels. A proof of small \(G_{N,Q(N)}\) must derive a genuinely NEW signed cofiber estimate, not invoke refinement monotonicity in the wrong direction.

On the exact base-16 orbit, normality would also imply \(G_{N,Q}(h)\to0\) at any fixed Q by the classical theorem that b-normality implies b^Q-normality and shift invariance, but this is NOT an all-growing-Q bound and is not used as a proof input.

## OMH-06. PREDECLARED 18 original-source finite conditional-energy certificates (OBSERVED CALIBRATED)

The first committed file on this draft branch was PREREGISTRATION.md, created **before** inspecting selected amplitudes at these fresh choices:
\[
N\in\{768,1536,3072\},\quad h\in\{9,11,17\},\quad Q\in\{16,256\}.
\]
The strict finite target is **G_(N,Q)(h)<2Q/N on EVERY one of 18 pairs**. The source is the literal original four rational poles, exact seed U0=0, no digit oracle. The standalone oracle uses exact rational Machin bounds for π, a 2^19 fractional phase grid, degree-18 rational Taylor polynomials for sin/cos, the derivative/Lagrange bound \((22/7)^{19}/19!\) per component, explicit grid angle error \((44/7)2^{-19}+(\pi_{\rm hi}-\pi_{\rm lo})\), and outward rounding to 10^-9. Each Q-conditioned complex group has length L=N/Q, and its rigorous quadratic upper is the sum of \((|{\rm rounded\ real}|+L\epsilon)^2+(|{\rm rounded\ imaginary}|+L\epsilon)^2\). Every inequality is checked as an EXACT Fraction; float conversions are only display.

**Result:** all 18/18 source-selected finite constraints PASS. The largest rigorously rounded-up \(G/(Q/N)\) is **1.258542912** at N3072,h9,Q16, versus preregistered threshold 2. Independent raw source formula \(r(n)=(120n^2-89n+16)/D(n)\), completely separate direct double trig diagnostic, reproduces all finite energy values strictly below the rigorous upper bounds (FLOAT-only; not proof). See CONDITIONAL_HOLDOUTS.json and independent source receipt.

These 18 finite cases were selected by the SAME model that implemented the oracle; not externally blind. No all-N G estimate was inferred or proved.

## OMH-07. Oily/Gamma normalizations as a falsifiable source map, NOT free interference

The original Oily–Macaroni constant \(\Omega=\varphi^{-1}-\gamma\) is an exact FIRST-JET mismatch in a declared exponentially tilted Gamma reference family from SUCC 2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md. It is not an independent exact selected π phase term.

**Constant phase shift no-go:** For any real c, \(e(h(U_n+c))=e(hc)e(hU_n)\), so \(|S_N(h;c)|=|S_N(h)|\) EXACTLY. An Oily reference phase offset by \(\Omega\) cannot generate cancellation. More generally, for any time-dependent phase correction \(\epsilon_n\to0\),
\[
\boxed{\left|\frac1N\sum_{n<N}e(h(U_n+\epsilon_n))-\frac{S_N(h)}N\right|
\le\frac{2\pi|h|}{N}\sum_{n<N}|\epsilon_n|\longrightarrow0.}\tag{21}
\]
In particular the source's auxiliary Oily log drift \(\eta_n=O(1/n)\), with reference correction \(\Omega\eta_n\), gives total unnormalized effect only O_h(logN): **it cannot create a normality theorem** by being inserted as a negligible additive phase. A successful Oily-based method would need a NEW source-derived non-negligible **joint signed cross-time interaction**, not a scalar center adjustment.

Also, the authentic unrenormalized log-Gamma source ratio
\[
G(t)=\frac{\Gamma(t+1/8)^4}
{\Gamma(t+1/2)^2\Gamma(t+5/8)\Gamma(t+3/4)}
\]
has digamma coefficients 4,−2,−1,−1 summing to ZERO. The common −γ term cancels: this source alone does not select a new unbalanced Euler–Mascheroni phase. This fact was already recorded in SUCC #465 and the Oily source handoff.

The earlier OILY_DIRECT_ARITHMETIC.md proves a truly **source-selected** logarithmic signed modulus deficit \(N-|S_N(h)|\ge(\log_8N)/29-O_h(1)\); the present multiscale energy (13) does NOT improve its fundamental order, by (14). This is a precise non-overclaim.

## 8. What would actually close π normality

**PROVED new-to-this-round:** source-height-only linear depth lower bound, asymptotic lower/upper depth window, original moving-Q selected-real nonlocking uniform over growing r, logarithm-squared multi-carrier pair energy, exact original conditional cofiber observer and Gamma transport, weak selected \(1-G>0\). **OBSERVED FINITE:** 10/10 Fraction exact rational method tests; 18/18 selected Fourier conditional energy exact rational interval certificates, independent float-only combined-source numerical diagnostics. **INHERITED:** all local F isometry/Haar and Gamma source law; published π irrationality measure, LCM PNT, Thue–Morse irrationality exponent.

**OPEN:** actual original-source all-N conditional estimate (18), all-scale signed #460 mixed prime/cofactor saving or #468 aggregate dyadic Haar dissipation; any \(S_N(h)=o(N)\) proof and π base-16 normality. The same-original-source Thue–Morse completion and periodic/carry coherent seeds pass parts of the new anti-alias machinery while remaining nonnormal; the full exact original U0=0 boundary is essential. No physical ħ, source-independent quantum evidence, RH, or scholarly novelty claimed.

### Primary and classical sources

- Original SUCC local F and 2-adic zero: research/2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md; original finite carrier Weyl #441; HBR #469; selected Oily signed arithmetic 2026-10-26/OILY_DIRECT_ARITHMETIC.md.
- Zeilberger–Zudilin, *The irrationality measure of π is at most 7.103205334137...*, Moscow J. Comb. Number Th. 9 (2020), https://arxiv.org/abs/1912.06345v2.
- Chan–Norrish, *Proof Pearl: Bounding Least Common Multiples with Triangles*, Journal of Automated Reasoning 62 (2019), https://trustworthy.systems/publications/full_text/Chan_Norrish_19.pdf.
- Bugeaud, *On the rational approximation to the Thue–Morse–Mahler numbers*, Annales de l'Institut Fourier 61 (2011), https://aif.centre-mersenne.org/articles/10.5802/aif.2666/.
- Classical \(\log\operatorname{lcm}(1,\ldots,m)=\psi(m)=m+o(m)\) follows from the prime number theorem; classical discrete Fourier Parseval and rational reconstruction are used with elementary derivations rather than asserted novel.
