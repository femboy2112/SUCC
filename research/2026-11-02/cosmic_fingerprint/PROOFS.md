# Cosmic Fingerprint — Exact background subtraction and reference-locked causal interferometry

**2026-11-02 — RESEARCH ONLY.** Exact parent: SUCC draft #464 at 0a69fe3d7260170248e2ef3bf1f1eb5de1b0c0f6 (ancestor #463→#462→#460→#459; merged Main XIX). Original four signed BBP poles, literal U0=0, main, historical proofs and production remain unchanged. This is a new-to-SUCC synthesis of classical Fourier orthogonality and astronomical reference-observation methods, **NOT a proof of pi normality or RH**.

## 0. Source, causal field and astronomical meaning

For base b>=2, horizon M>=2, and arbitrary phases |z_n|=|w_n|=1, write e(t)=exp(2pi i t), q_n=b^n and
\[
\Phi_z(s)=\sum_{n=1}^{M}z_ne(q_ns),\quad
\rho_z(s)=|\Phi_z(s)|^2/M,\quad s\in\mathbb R/\mathbb Z.
\]
For authentic BBP choose b=16, h∈Z nonzero, z_n=e(hU_n), where
\[
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).
\]
This is the *selected* original source, not a random seed. A coherent reference field has w_n=1; changing w changes the declared measurement.

The constant background below is analogous to subtracting a nuisance monopole; the CMB itself is anisotropic and is NOT literally this background. Planck used Commander/NILC/SEVEM/SMICA across different frequency maps, and SDSS uses spectral template cross-correlation. Neither astronomical precedent is a proof of our arithmetic statements.

## CF-01 — universal diagonal background; auto-power is source blind (PROVED)

Every nonzero ordered difference b^n-b^m is unique: if n>m, then b^n-b^m=b^m(b^(n-m)-1), with the last factor prime to b in the sense that b does not divide it; the largest integral power b dividing the difference recovers m, then n. Negative frequencies reverse the pair.

Expanding intensity gives EXACTLY
\[
\boxed{\rho_z(s)=1+A_z(s),\
A_z(s)=\frac1M\sum_{n\ne m}z_n\bar z_m e((b^n-b^m)s).}\tag{CF1}
\]
The constant 1 is the universal phase-blind diagonal. Orthogonality and the difference uniqueness imply
\[
\boxed{\int A_z(s)ds=0,\quad
\|A_z\|_{L^2}^2=(M-1)/M.}\tag{CF2}
\]
These hold for every coherent, normal, nonnormal, authentic or changed-source phase sequence: auto-power alone cannot classify normality.

## CF-02 — calibrated causal-anisotropy matched filter (PROVED)

With a second **fixed and calibrated** reference field w, use the globally integrated *centered intensity* cross-correlation
\[
C_M(z,w)=\int_0^1 A_z(s)A_w(s)\,ds.
\]
Expand both off-diagonal sums. Only equal ordered causal differences survive Fourier integration. Therefore
\[
\boxed{
C_M(z,w)=\frac1{M^2}\sum_{n\ne m}z_n\bar z_m\bar w_n w_m
=\frac{\left|\sum_{n=1}^{M}z_n\bar w_n\right|^2-M}{M^2}.
}\tag{CF3}
\]
No independence, stationarity, Gaussian radiation or random-phase premise is required.

For independent coherent reference w_n=1 and the genuine BBP source,
\[
\boxed{C_M^{BBP}(h)=|S_M(h)|^2/M^2-1/M,\quad
S_M(h)=\sum_{n=1}^{M}e(hU_n).}\tag{CF4}
\]
For every fixed h!=0, C_M→0 iff S_M(h)=o(M). By the already established summable BBP Green-tail Weyl transport, vanishing for all fixed nonzero h is equivalent to pi being base-16 normal. **CF4 is a new phase-referenced observation, NOT a proof that its limit is zero.**

## CF-03 — TWO phase-stepped positive sky intensities reconstruct the entire COMPLEX Weyl sum (PROVED)

For any coherent reference w, put S_(z,w)=sum z_n conj(w_n). Measure an ideal phase-controlled reference field at angles θ=0,π/2:
\[
I_\theta(z,w)=\int_0^1|\Phi_z(s)+e^{i\theta}\Phi_w(s)|^2ds\ge0.
\]
By character orthogonality, \(\int\Phi_z\overline{\Phi_w}=S_{z,w}\), and therefore
\[
\boxed{I_\theta=2M+2\operatorname{Re}(e^{-i\theta}S_{z,w}).}\tag{CF5}
\]
It follows that
\[
\boxed{S_{z,w}=\tfrac12[(I_0-2M)+i(I_{\pi/2}-2M)].}\tag{CF6}
\]
With w_n=1, this is the *full actual complex* BBP Weyl sum from two globally integrated nonnegative intensities. An external phase-locked reference changes the observation algebra: this does NOT contradict SUCC #404's first sixteen *unreferenced* seed-averaged balanced moments being source blind and the first intrinsic source-sensitive moment at order 34. The extra reference supplies a marked origin.

**No free proof/speedup:** requiring both I0=2M+o(M) and Iπ/2=2M+o(M) is exactly the missing selected signed estimate. The reference field contains b^M causal frequency and phase-calibration/precision assumptions, even though the ideal observation uses no shrinking seed aperture.

## CF-04 — gauge and component separation (PROVED)

If the source is shifted by a real seed s0, the phase becomes z_n e(hb^n s0). Shifting source and reference together leaves S_(z,w) and C_M invariant; shifting only the source with reference held at the independently fixed origin can change both. Thus a source/template relative gauge calibration is necessary.

Two **linear complex field** observations Y1=a1F+c1B and Y2=a2F+c2B recover source F and nuisance B uniquely if and only if the known response determinant D=a1 c2-a2 c1 is nonzero:
\[
\boxed{F=(c_2Y_1-c_1Y_2)/D,\quad
B=(a_1Y_2-a_2Y_1)/D.}\tag{CF7}
\]
When D=0 even noiseless measurements have a nontrivial kernel. This is the elementary identifiability gate behind multi-channel component separation; intensities do NOT generally mix as those linear complex fields.

## CF-05 — EHT-style closure phase is a RANK-ONE NO-GO here (PROVED)

A naive visibility for a single pure SUCC causal field is V_nm=z_n conj(z_m). Every closed triangle has
\[
\boxed{V_{nm}V_{m\ell}V_{\ell n}=1.}\tag{CF8}
\]
So all triangle closure phases are exactly zero, whatever the true BBP phase sequence. Astronomy's genuinely informative EHT closure data are NOT of this pure rank-one form. This is an explicit obstruction to silently importing a closure-phase theorem.

A two-component mixture can have nonzero closure: choose z=(1,1,1), w=(1,i,(3+4i)/5), and V_nm=(1/5)z_n conj(z_m)+(4/5)w_n conj(w_m). Then **exactly**
\[
\boxed{V_{01}V_{12}V_{20}=93/125-(24/625)i.}\tag{CF9}
\]
This is a mathematical counterexample to an overgeneralized closure null, not a physical SUCC detector or proof of pi normality. A declared second independent component must really exist.

## CF-06 — foreground residual error bound and template adequacy (PROVED)

If the observed centered anisotropy is A_z+η for real η∈L²(circle), while A_w is calibrated, Cauchy–Schwarz and CF2 give
\[
\boxed{|C_M^{obs}(z,w)-C_M(z,w)|
\le\sqrt{(M-1)/M}\|\eta\|_2\le\|\eta\|_2.}\tag{CF10}
\]
The matched intensity is uniformly L²-stable to additive science-foreground residual error. This says nothing about measurement bandwidth or establishing signed cancellation.

Two global integrated phase-step errors δI0,δI90 change the recovered complex sum by (δI0+iδI90)/2.

If a reference phase has w_n=e(h f_n) and \(\sum_n|f_n|<∞\), the triangle inequality yields
\[
\boxed{|\sum_{n\le M}z_n\bar w_n-\sum_{n\le M}z_n|
\le2\pi|h|\sum_n|f_n|=O_h(1).}\tag{CF11}
\]
Thus a summable Green-tail correction template (such as the original source's T_n, where SUCC proves \(\sum T_n<1/32\)) cannot by itself create a new o(M) cancellation theorem. The coherent changed-source relative-phase template gives a rational-affine restatement of the unresolved pi problem, not a proof.

## CF-07 — certified finite original-vs-shadow fingerprint, robust to small L² contamination (PROVED FINITE, inherited source certificate)

At original BBP p=257, n=33..128, M=96, h=1, SUCC #459 SPP-10 has already rigorously certified \(|S|/96<1/16\) with exact rational interval arithmetic. CF4 gives
\[
\boxed{C_{96}^{original}(1)<(1/16)^2-1/96=-5/768<0.}\tag{CF12}
\]
For the explicitly DIFFERENT positive zero-seeded coherent source from #421/#462, every such n satisfies \(\widetilde U_n\bmod1=2/15-d_n\), \(0<d_n<1/265^2\). Using \(2\pi<44/7\):
\[
\boxed{C_{96}^{shadow}(1)>
(1-44/(7\cdot265^2))^2-1/96>989/1000.}\tag{CF13}
\]
This is an exact certified **finite** contrast. Under an additive residual with \(\|\eta\|_2\le1/512\) in the SCIENCE channel and a clean fixed coherent reference, CF10 preserves the sign gap:
\[
\boxed{C_{96}^{original,obs}<-7/1536,\quad
C_{96}^{shadow,obs}>987/1000.}\tag{CF14}
\]
The original finite signed upper bound is INHERITED, not newly generated or independently re-certified by this round. The coherent source is a changed forcing, not an alternate original pi value.

## CF-08 — actual remaining theorem and what the astronomical instrument buys (OPEN)

The original four-pole selected signed condition \(S_M(h)=o_h(M)\) for every fixed h!=0 remains OPEN. A new all-horizon estimate on the calibrated cross-intensity C_M, or on both phase-step baselines I_theta=2M+o_h(M), would prove pi normality; **none has been established**. The exact transformations above reduce observation loss and give explicit conditioning/foreground controls, but do not add the required arithmetic estimate.

The next proof must use a specific original source/zero-seed constraint on the joint p-primary × p-free cofactor in #459/#460, producing a genuinely new signed inequality. A closure-phase-only, auto-spectrum-only, Galois-averaged, uncalibrated or summable-template shortcut is refuted by the controls above.

### External and SUCC mathematical provenance

Planck Collaboration, *2018 results IV: Diffuse component separation*, A&A 641 A4 (2020), https://doi.org/10.1051/0004-6361/201833881 — conceptual multi-channel foreground precedent.
SDSS stellar template cross-correlation https://classic.sdss.org/dr3/algorithms/redshift_type.php and STScI/JWST spectral templates https://spacetelescope.github.io/jdat_notebooks/notebooks/NIRISS/NIRISS_WFSS_postpipeline/02_Cross_correlation_template.html .
EHT Collaboration, *First M87 Results III*, https://doi.org/10.3847/2041-8213/ab0c57 and *VI*, https://doi.org/10.3847/2041-8213/ab1141 — phase/closure observational precedent, not the same visibility matrix.
SUCC #404, #421, #459, #462, #463, #464 — prior source/countermodel, selected finite interval, and causal response results, explicitly inherited.
