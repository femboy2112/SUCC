# OPERATION CAUSAL RESPONSE ROTATION — circle/line lifts, universal causal Haar, and exact selected-phase retrieval

**2026-11-02. Research-only; based exactly on SUCC draft #463 at 43adc90badfc6b8abc1631a4332c09cda007ccb7, stacked through #462/#460/#459 on Main XIX.** Original four signed BBP poles, literal U_0=0, all legacy contracts and main remain untouched. The mathematical ingredients (Fourier characters, Hadamard-lacunary integer powers, circle covering, basic phase retrieval) are classical; the new-to-SUCC contribution is the *declared causal-axis instrument*, its precise interfaces to source, zero-seed and selected signed phases, and the nonadequacy tests. No claim of scholarly priority, RH, pi normality or quantum evidence.

## 0. Hypothesis and precise interpretation

The conjectured rotation is NOT the Fourier transform of the chronological list of pi digits. It is the Fourier transform in a **counterfactual intervention parameter**: how much an initial perturbation at the carrier's causal boundary influences the orbit at each later time. An orbit can be maximally coherent in chronological circle phase but weakly uniform as a measure of causal-response interference. We must distinguish those two definitions of observation.

Let b>=2, integer h!=0, and a specified real or rational forcing r_1,r_2,... . On an affine source instance
\[
U_0(s)=s,\qquad U_{n+1}(s)=bU_n(s)+r_{n+1},
\]
write u_n=U_n(0). Then the exact causal response is
\[
\boxed{U_n(s)=u_n+b^n s,\quad
\partial_s U_n(s)=b^n.}\tag{CR-0}
\]
For the authentic BBP source b=16, u_0=0 and
\[
r_n=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]
The same family construction also applies to the **explicitly different** coherent zero-seeded shadow in #463; do not identify their sources.

Define e(x)=exp(2pi i x), C=R/Z, and the causal phase field
\[
\boxed{Z_{n,h}(s)=e(h(u_n+b^n s))
=z_n e(hb^n s),\quad z_n=e(hu_n),\quad s\in C.}\tag{CR-1}
\]

## 1. CR-01 — actual line→circle covering and causal winding (PROVED, classical)

The real line has a canonical lift Theta_(n,h)(s)=h(u_n+b^n s). Under s->s+1,
\[
\Theta_{n,h}(s+1)-\Theta_{n,h}(s)=hb^n\in Z.
\]
Thus Z_(n,h):C->C has winding/degree **exactly hb^n**, and
\[
(2pi i)^{-1}Z_{n,h}(s)^{-1}\partial_sZ_{n,h}(s)=hb^n.
\]
The circle is the quotient of this lifted line by integer deck translations. There is **no global single-valued real logarithm on the seed circle** for h!=0; forgetting winding/carry destroys information. This is a topological covering, not a homeomorphism rotating R into S1 or literal curvature of an intrinsic one-dimensional circle.

The cause-to-effect derivative b^n is source-independent. It records the causal amplification of the initial state; it does NOT itself determine the actual pi trajectory or which seed was selected.

## 1B. CR-01B — the correct invertible circle/line carrier is a solenoid (PROVED; solenoid idea inherited #452)

Define the inverse-limit solenoid
\[
\Sigma_b=\{(s_0,s_1,\ldots)\in(\mathbb R/\mathbb Z)^\mathbb N:
bs_{j+1}=s_j\bmod1\}.
\]
Multiplication by b on every coordinate is an **automorphism**
\[
\boxed{[b](s_0,s_1,\ldots)=(bs_0,s_0,s_1,\ldots),\quad
[b]^{-1}(s_0,s_1,\ldots)=(s_1,s_2,\ldots).}\tag{CR-1a}
\]
On the individual circle, the map s_0→bs_0 is b-to-1 and cannot be inverted without a choice of inverse-branch history. Its solenoidal lift IS invertible because the compatible whole history is retained. The exact mathematical idea of a solenoidal invertible cover was previously developed in SUCC #452; it is **not newly discovered** here.

The lifted real causal coordinate s has a canonical map
\[
\boxed{\iota(s)=(s\bmod1,s/b\bmod1,s/b^2\bmod1,\ldots)\in\Sigma_b,}\tag{CR-1b}
\]
and projection \(\pi_0:\Sigma_b\to\mathbb R/\mathbb Z\) obeys
\(\pi_0\iota(s)=s\bmod1\) and \([b]\iota(s)=\iota(bs)\).
There is NO canonical continuous circle→solenoid inverse without selecting infinitely many compatible roots. As an explicit counterexample, both towers
\[
(0,0,0,\ldots)\quad\text{and}\quad
(0,1/b,1/b^2,\ldots)
\]
project to the SAME initial circle value zero, but encode different inverse histories.

On any continuously differentiable circle function f(s), write \(C_bf(s)=f(bs)\) and \(D_h=(2\pi ih)^{-1}\partial_s\). The chain rule yields the **noncommutative unit–unit causal differential law**
\[
\boxed{D_h C_b=b\,C_b D_h,\qquad
[D_h,C_b]=(b-1)C_b D_h.}\tag{CR-1c}
\]
This is the explicit operator-level version of the user's proposed rotation along *causal effect* rather than along ordinary chronological Fourier frequencies. It is classical dilation/differentiation algebra; it does not create intrinsic Riemann curvature or a source-derived signed saving. A scalar phase field's open-path cocycle is not automatically nontrivial closed-loop holonomy.

The correct **typed factorization is real line→solenoid→circle**, not circle→line as an invertible homeomorphism. Causal-time dilation is invertible in the first two carriers (with all inverse history retained) and noninvertible on a single circle snapshot. Source identity and the literal U0=0 real-lift anchor remain separate additional data.

## 2. CR-02 — the causal-axis Fourier lift is isometric, not a chronological DFT (PROVED)

Let M=N+1 and consider arbitrary unit complex phases z_0,...,z_N. Define
\[
\Phi_{N,h}(s)=\sum_{n=0}^N z_n e(hb^n s).
\]
The linear map from the M time amplitudes to the L2 seed-circle function is an isometry, by Fourier orthogonality:
\[
\int_0^1|\Phi_{N,h}(s)|^2ds=\sum_{n=0}^N|z_n|^2=M.
\]
The causal-frequency spectrum has exactly M coefficient slots at hb^n, each with intensity |z_n|²=1. Therefore **coherent and nonnormal source orbits have the same perfectly flat causal power spectrum** on the declared M slots. This is an orthogonal Fourier embedding in the seed *intervention* coordinate, not a transform in chronological time.

Define the nonnegative causal interference probability measure
\[
\boxed{d\mu_{N,h}(s)=\rho_N(s)ds,\quad
\rho_N(s)=|\Phi_{N,h}(s)|^2/M.}\tag{CR-2}
\]

## 3. CR-03 — universal weak-Haar causal rotation, even for maximally coherent orbits (PROVED)

**Unique-differences lemma.** If n>m and a>b are nonnegative integers,
\[
b^n-b^m=b^a-b^b>0
\implies n=a,\ m=b.
\]
Proof: \(b^n-b^m=b^m(b^{n-m}-1)\), and the second factor is congruent to −1 mod b. Hence the highest power of b dividing the difference is precisely b^m, recovering the lower index m; then recover n. This holds for composite b too (the b-divisibility exponent, not a p-adic valuation).

For any integer k, use normalized Fourier coefficients
\(\widehat\mu_{N,h}(k)=\int_0^1e(-ks)\,d\mu_{N,h}(s)\).
Expansion and orthogonality give the EXACT finite identity
\[
\boxed{
\widehat\mu_{N,h}(k)
=\frac1M\sum_{\substack{0\le n,m\le N\\h(b^n-b^m)=k}}
z_n\overline z_m.}\tag{CR-3}
\]
The zero coefficient is 1. For every k!=0, at most ONE ordered pair contributes:
\[
\boxed{\sup_{k\in Z\setminus\{0\}}|\widehat\mu_{N,h}(k)|=1/M.}\tag{CR-4}
\]
Thus, for EVERY bounded unit-phase sequence (with no restriction on source and no assumption of normality),
\[
\boxed{\mu_{N,h}\xrightarrow[N\to\infty]{\mathrm{weak-*}}m_C,}\tag{CR-5}
\]
Haar probability on the causal seed circle. Proof: (CR-4) kills every fixed nonzero Fourier character; trig polynomials are dense in C(C), so all continuous test integrals converge.

**An essential distinction:** this is causal seed-observer weak convergence, NOT time normality of the selected pi digits. The same result holds for z_n≡1 and for the coherent changed-source shadow z_n=e(h U_tilde_n) -> e(2h/15). The causal observer appears uniform while the selected time trajectory remains coherent and nonnormal.

**No stronger convergence is implied.** Exact Parseval yields
\[
\boxed{\int_0^1(\rho_N(s)-1)^2ds=\frac{N}{N+1}
\longrightarrow1,}\tag{CR-6}
\]
and \(\int_0^1|\Phi_{N,h}|^4ds=M(2M-1)\).
This weak-Haar sequence does NOT converge to the constant density 1 in L2. Its moving frequency structure retains O(1) total L2 fluctuation even when every individual nonzero Fourier coefficient vanishes.

## 4. CR-04 — phase retrieval from causal INTENSITY alone (PROVED; anchor essential)

For EVERY n=1,...,N, the frequency \(k_n=h(b^n-1)\) occurs in CR-3 only for the pair (n,0). Hence
\[
\boxed{
M\,\widehat\mu_{N,h}(h(b^n-1))=z_n\overline z_0.}\tag{CR-7}
\]
With authentic literal zero initial condition u_0=0, z_0=1, so a **nonnegative real intensity function of causal displacement alone recovers EVERY selected complex phase z_n**, exactly and without phase ambiguity. In general it recovers the phase sequence up to one common global phase, repaired by a calibrated initial anchor.

This is a lossless observation map at each finite N when retaining the *full calibrated function* rho_N(s); its weak Haar limit throws away precisely the moving frequencies that store the phase sequence.

For the authentic source, \(\widehat\mu_{N,h}(h(16^n-1))=e(hu_n)/(N+1)\), so the missing signed normality gate becomes
\[
\boxed{
S_N(h)=\sum_{n=1}^Ne(hu_n)
=(N+1)\sum_{n=1}^N\widehat\mu_{N,h}(h(16^n-1)).}\tag{CR-8}
\]
This is an exact **representation equivalence**, not a newly proved o(N) estimate. The sum of moving coefficients, not their individual moduli, is the unpaid selected signed interaction.

**Seed translation/no-go:** changing the same forcing to initial seed s0 changes the causal response field by
\(\Phi^{s0}_{N,h}(s)=\Phi^{0}_{N,h}(s+s0)\).
Thus every Haar-averaged nonlinear statistic of intensity (all its integrated moments, distribution of values, etc.) is identical for the authentic seed and the coherent same-forcing counterseed \(s_*=-\pi/16\). An **uncalibrated** seed origin cannot select pi. Keeping the actual origin/anchor in CR-7 is essential.

## 4B. CR-04B — same authentic four-pole source has BOTH normal and coherent seeds, yet identical global causal invariants (PROVED, classical existence)

This makes the observer inadequacy decisive without assuming ANY currently open statement about pi.

For original signed four poles, the completed zero-seed point is alpha=pi/16. The exact source Green tail gives
\[
U_n(s)=16^n(\alpha+s)-T_n,\qquad \sum_{n\ge1}|T_n|<\infty.
\]
Choose **one proven base-16 normal real number** c, such as the base-16 Champernowne constant (or simply use Borel's theorem that almost every real c is base-16 normal). Define
\[
s_{\rm normal}=c-\alpha,\qquad s_{\rm coh}=-\alpha.
\]
Then the SAME unchanged forcing r(n) yields
\[
U_n(s_{\rm normal})=16^n c-T_n,
\qquad U_n(s_{\rm coh})=-T_n.
\]
The summable tail changes any fixed-h exponential Weyl sum by O_h(1), so the first orbit is rigorously base-16 equidistributed; the second has
\(\lim_N N^{-1}\sum_{n\le N}e(hU_n(s_{\rm coh}))=1\)
for every fixed h!=0 and is manifestly nonnormal.

Yet their causal interference profiles are translations of each other:
\[
\boxed{\rho_N^{s_{\rm normal}}(s)=
\rho_N^{0}(s+s_{\rm normal}),\quad
\rho_N^{s_{\rm coh}}(s)=\rho_N^{0}(s+s_{\rm coh}).}\tag{CR-7a}
\]
Consequently **EVERY** statistic invariant under translation of the causal-intervention circle is exactly identical for a genuinely normal and genuinely nonnormal member of the SAME FOUR-POLE SOURCE CLASS at each N: all seed-integrated moments, full distributions of intensity values, absolute magnitudes of all Fourier coefficients and global weak-Haar conclusions. The source itself has not changed; ONLY the selected real seed did.

This is an unconditional **source-matched obstruction**, stronger than a hypothetical "if pi is normal" comparison. It proves that global seed-translation invariant observations are insufficient to classify the normality of a marked initial condition. To prove pi normal one must supplement them with the authentic anchor U0=0 and a genuine seed-specific signed estimate. This does NOT refute the possibility that those additional data could establish normality.

External classical normal-number existence: Borel's almost-everywhere normality theorem; constructive base-b Champernowne normality. No new normal-number result is claimed here.

## 5. CR-05 — exact exponential resolution boundary of an intensity-only causal observer (PROVED)

For every latest time N>=1, the smallest absolute difference frequency involving z_N is
\[
\boxed{\min_{0\le m<N}|h(b^N-b^m)|=|h|(b-1)b^{N-1}.}\tag{CR-9}
\]
Consequently, an intensity observer retaining only Fourier modes |k|<=K with
\(K<|h|(b-1)b^{N-1}\)
receives **no coefficient involving the latest phase z_N**; the zero coefficient is the constant 1. It cannot recover that phase from this band-truncated observation without extra independently certified source assumptions. The anchored direct recovery mode in (CR-7) lies at |h|(b^N-1).

This is an **exponential Fourier-bandwidth requirement for THIS particular causal intensity readout**, not a general computational or information-theoretic lower bound for all ways to compute U_N. The original rational BBP source can compute any given finite U_N directly without performing a Fourier inversion at such high frequencies.

## 6. CR-06 — the causal unit/phase-power square exposes the selected differential (PROVED)

Write the time/seed field as \(Z_n(s)\) with fixed h. Compare two operations both sending its causal frequency hb^n to hb^(n+1):
- phase-power \(\mathcal P_b Z_n(s)=Z_n(s)^b\);
- causal-seed dilation \(\mathcal C_b Z_n(s)=Z_n(bs)\).

Their ratio is the **actual selected original circle phase**:
\[
\boxed{\frac{\mathcal P_b Z_n(s)}{\mathcal C_b Z_n(s)}
=e(h(b-1)u_n),}\tag{CR-10}
\]
independent of s. The real chronological successor has
\[
\boxed{\frac{Z_{n+1}(s)}{\mathcal P_b Z_n(s)}
=e(hr_{n+1}),}\tag{CR-11}
\]
a seed-blind exact forcing cocycle; the alternative alignment satisfies
\[
\boxed{\frac{Z_{n+1}(s)}{\mathcal C_b Z_n(s)}
=e(h(u_{n+1}-u_n)).}\tag{CR-12}
\]
This is an operational **causal structural differential**: two mathematically distinct alignments of the same causal frequency yield different phase factors. The pair (CR-10,CR-11) retains the selected state *and* the source, whereas forcing-only CR-11 does not identify the selected seed.

The ratios are scalar exact coboundaries on these response fields: they do NOT establish nontrivial physical gauge curvature, a Riemann-sphere rotation, or a new asymptotic signed estimate. Their role is to specify a legitimate source/seed-faithful common-basis transport in the causal parameter.

## 6B. CR-06B — a finite-order causal DIFFERENTIAL projector recovers any historical phase (PROVED)

The causal rotation has a second exact, source-faithful inverse that does NOT require integrating against exponentially large Fourier frequencies. Instead use the user's proposed *differential along the structural intervention axis*:
\[
\boxed{\mathcal D_h=(2\pi i h)^{-1}\partial_s,\quad
\mathcal D_h Z_{n,h}(s)=b^nZ_{n,h}(s).}\tag{CR-12a}
\]
This is **not** chronological differentiation \(\Delta_n\), and not the seed-blind source covariant difference \(E-b\) from #463. The operator is the infinitesimal generator of the initial-seed translation action on the response field.

At finite N, let the known distinct eigenvalues be \(\lambda_n=b^n\) for \(0\le n\le N\). Construct the rational Lagrange spectral projectors
\[
\boxed{L_{n,N}(X)=\prod_{\substack{0\le m\le N\\m\ne n}}
\frac{X-\lambda_m}{\lambda_n-\lambda_m}\in\mathbb Q[X].}\tag{CR-12b}
\]
Then \(L_{n,N}(\lambda_m)=\delta_{nm}\), and therefore
\[
\boxed{[L_{n,N}(\mathcal D_h)\Phi_{N,h}](0)=z_n=e(hu_n),\quad0\le n\le N.}\tag{CR-12c}
\]
This is an exact **unit–unit causal differential tomography theorem**, recovering any historical complex phase from the complete complex response function and its first N derivatives at the *calibrated* intervention origin.

Equivalently the measured causal derivatives define polynomial moments
\[
\boxed{M_k=(2\pi i h)^{-k}\Phi^{(k)}_{N,h}(0)
=\sum_{n=0}^N (b^n)^k z_n,\quad0\le k\le N.}\tag{CR-12d}
\]
The Vandermonde matrix has nonzero determinant
\(\prod_{0\le m<n\le N}(b^n-b^m)\), so all phase coefficients are uniquely recoverable by a rational linear inverse on their coefficient vector.

**Very important precision and authority firewall.** The theorem is a finite interpolation/reconstruction identity valid for ANY phases; it does not certify the actual source or bound their signed sum. Higher derivatives have magnitudes growing up to \(b^{N^2}\), so a finite-precision implementation may be badly conditioned. This is not a uniform-in-N stability theorem, computational speedup, or a normality proof. Unlike CR-04's *intensity-only* spectral readout, this instrument requires complex response values and high-order causal derivatives. The two are mathematically independent readout implementations of the same finite phase record, not blind independent mathematical provenance.

## 6C. CR-06C — the full structural-effect Jacobian across causal time (PROVED, elementary Green algebra)

The seed-intervention axis above varies U0 while retaining the exact forcing. A SECOND, separately typed causal experiment allows a small intervention at EACH forcing step. On a finite horizon 0<=n<=N, choose input changes \(\epsilon_0\) in the initial value and \(\epsilon_j\) in r_j, j>=1. The resulting state changes are EXACTLY
\[
\boxed{
\delta U_n=\sum_{j=0}^{n}J_{n,j}\epsilon_j,\qquad
J_{n,j}=b^{n-j}\mathbf1_{j\le n}.}\tag{CR-12e}
\]
This lower-triangular retarded Green matrix has every diagonal entry 1, hence \(\det J=1\). Its inverse is the *actual causal source differential*
\[
\boxed{
(D_bv)_0=v_0,\quad (D_bv)_n=v_n-bv_{n-1}\ (n\ge1),
\quad D_bJ=JD_b=I.}\tag{CR-12f}
\]
The first-order causal effect-birth law is
\[
\boxed{J_{n+1,j}-bJ_{n,j}=\delta_{j,n+1}.}\tag{CR-12g}
\]
This pinpoints the precise time at which a forcing intervention first enters the source path, rather than distributing it over a fictitious homogeneous time-frequency mode.

For the authentic forcing r and coherent changed forcing r_tilde, with both literal zero seeds,
\[
\boxed{U_n-\widetilde U_n=\sum_{j=1}^{n}b^{n-j}(r_j-\widetilde r_j).}\tag{CR-12h}
\]
The identity reproduces the exact source boundary-amplifier comparison already made in #462. It is a **unimodular causal source-to-state isomorphism on finite line histories**; passing to circle states modulo one discards integer carry unless it is separately retained. This is the finite algebra behind the user's intended "rotate along structural effect across time" language.

**Source-type firewall:** varying the source slots \(\epsilon_j\) changes the exact forcing, while varying only the initial seed \(\epsilon_0\) preserves it. A multi-intervention Fourier transform may be a richer observation instrument, but simply knowing J, its inverse or its δ birth law neither forces π digit equidistribution nor identifies the real selected seed. The source/carry/Archimedean phase must still enter a NEW signed estimate.

## 7. CR-07 — 34th-moment first resonance is source-only, not a selected-seed proof (INHERITED #404, independently exact-probed)

**Prior art inside SUCC:** PR #404 (already integrated into Main XVII and then Main XIX) proved Haar seed-averaged balanced moments up through order 32 are phase-blind and identified the first phase-dependent balanced moment at order 34 (17 factors per side). This round DOES NOT rediscover or claim that result.

The simplest exact local resonance is the homogeneous base-b arithmetic identity
\[
\boxed{b\,b^n+b^{n+2}=(b+1)b^{n+1}.}\tag{CR-13}
\]
Both sides have b+1 frequencies, so at b=16 the first local balanced collision is 17 against 17 factors. In the actual source phase it contributes
\[
\boxed{
e\big(h(16u_n+u_{n+2}-17u_{n+1})\big)
=e(h(r_{n+2}-r_{n+1})).}\tag{CR-14}
\]
The expanding selected seed cancels because the exponent polynomial \(16+E^2-17E=(E-1)(E-16)\) vanishes at the causal multiplier 16. Thus even this first high-order mixed source resonance is *seed blind*. The entire collection of integrated seed moments is shift invariant as shown above.

For a base b and a fixed balanced multiplicity q<=b, sums of q nonnegative powers of b have unique multiset representations. This follows from base-b carrying: if q<b no carry is possible; if q=b the only possible carry is b equal powers to one higher power, with no alternate equal-length representation. At q=b+1, CR-13 furnishes a collision. These are inherited in mathematical substance from #404, and separately tested only for small finite support.

## 8. CR-08 — correct selected causal microscope is an exponentially shrinking seed window (EQUIVALENCE, inherited #404)

The causal lift is uniformly Lipschitz in seed at finite N:
\[
|\Phi_N(s)-\Phi_N(0)|
\le2\pi|h|\,|s|\sum_{n=0}^Nb^n.
\]
Choose \(\delta_N=b^{-(N+1)}\). For all s in [0,delta_N],
\[
\boxed{|\Phi_N(s)-\Phi_N(0)|\le\frac{2\pi|h|}{b-1}.}\tag{CR-15}
\]
With \(A_N=\delta_N^{-1}\int_0^{\delta_N}\rho_N(s)ds\), one has
\[
\boxed{
|\Phi_N(0)|\le\sqrt{(N+1)A_N}+\frac{2\pi|h|}{b-1},
\quad
\sqrt{(N+1)A_N}\le|\Phi_N(0)|+\frac{2\pi|h|}{b-1}.}\tag{CR-16}
\]
Hence on the original zero-seeded BBP orbit, for every fixed nonzero h,
\[
\boxed{S_N(h)=o(N)\iff A_N=o(N).}\tag{CR-17}
\]
This is a *positive intensity* local criterion requiring exponentially fine causal resolution, but it is an EQUIVALENCE to the unpaid Weyl gate, not a proof. NWR-09 of prior PR #404 already established the shrinking-seed-cylinder principle for the linear response; this is its exact intensity analogue.

The coherent same-source counterseed has |Phi_N(0)|~N and A_N~N (up to O_h(1) terms), while both its mu_N and the original mu_N converge weakly to Haar over the ENTIRE seed circle. That is the operational difference between global averaging and selected observation.

## 9. An optional literal log-causal rotation (PROVED but completely source blind)

The causal susceptibility is b^n. Measuring its logarithm in an independent unit a>1 gives coordinates \(n\log_a b\) mod1. If \(\log_a b\notin\mathbb Q\), the classical geometric-series argument proves the corresponding rotation orbit is equidistributed mod1. For b=16,a=3 this is irrational by unique factorization (no 3^p=16^q with positive p,q). Therefore even a perfectly coherent *time* circle trajectory has a perfectly equidistributed **log-causal-susceptibility rotation**. This is a real mathematical realization of the metaphor, but it depends only on multiplier b and cannot discriminate pi from the coherent counterseed or shadow.

## 10. Verdict and next discriminating probe

**DISCLOSED paper (mostly classical mathematics, explicit scoped SUCC realization):** line/circle winding CR-01, causal Fourier isometry CR-02, universal weak-Haar and non-L2 theorem CR-03, calibrated intensity phase retrieval CR-04, Fourier-band resolution CR-05, exact unit/causal-dilation phase mismatch CR-06. The source-only 34th-moment threshold and shrinking-seed principle are INHERITED from #404. Finite pure-Fraction test methods corroborate exact algebra, not any unbounded normality claim.

**REFUTED:** any claim that weak-Haar causal response, flat causal spectral magnitudes, seed-integrated moments or log-causal equidistribution implies chronological base16 normality of pi. Same-four-pole coherent changed seed and zero-seeded positive shadow both satisfy universal causal Haar while having full real coherence.

**OPEN:** the source-derived ALL-HORIZON bound \(S_N(h)=o(N)\) for every fixed h!=0, and equivalently the genuinely selected sublinear intensity on the exponentially shrinking causal seed cylinder. Merely recovering all selected phases from intensity is not cancellation.

**Next falsifier:** derive a NEW source-specific signed bound on the shrinking causal aperture using the full four-pole BBP cofactor, zero seed, and actual real-phase moving Fourier bundles (CR-8). It must fail on the coherent same-source irrational seed and positive all-order-asymptotic changed source. Global weak-Haar, 34th-moment source resonance, exact phase retrieval and ordinary source-cocycle commutators are diagnostics, not proofs.
