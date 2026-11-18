# The Circle Has a Moving Zero — Gauge-Covariant Origins, Fifteen Fixed Frames, and a Rational Pair-Phase Norm

**SUCC / Principia Observer Geometry / original BBP null seed — 2026-11-17**

**Originating insight (Leah):** locating the "0" of the circle depends on where observer J pins the coordinate origin. Distinguish "0 in frame J" from an absolute assertion about the carrier, and use the same source/observer transport discipline that protects the BBP null-information seed. The BBP impulse filter has \(Q(z)=(1-z)H(z)\), with its only unit-circle zero \(z=1\); can a changed frame remove this apparent null wall?

**Verdict:** CZF-01–07 are classical/exact deductions with finite source-rational checks. **The resulting origin-independent anti-coherence condition is strictly stronger than original R0 and remains OPEN** for the authentic π orbit at all late shells. No normality, physical gauge theory, QM or GR result is claimed. The auxiliary impulse lag circle and the chronological radix circle are NOT silently identified.

## 1. A tagged zero [0,J], not literal \(0\cdot J\)

On the physical circle \(S^1=\mathbb R/\mathbb Z\), the standard group identity is \(0\pmod1\) (phase \(z=1\)), once the group law and original source chart are chosen. An *arbitrary marked point* on the circumference can instead be used as the observer's **coordinate origin**. These are different notions of zero.

Let the completed original circle angle be \(\theta_n=16^n x\pmod1\), \(x=\pi/16\). An observer J with origin angle \(\alpha_n\) reports
\[
\boxed{\phi_n^J=\theta_n-\alpha_n\pmod1.}\tag{CZF1}
\]
The notation "\(0*J\)" is interpreted as a **tagged origin** \([0,J]\), not a nonzero value of literal multiplication \(0\cdot J\).

### CZF-01 — the moving-circle-origin connection (CLASSICAL / PROVED PAPER)

The unmodified physical dynamics obeys \(\theta_{n+1}=16\theta_n\pmod1\). The moving-frame readout obeys the exact *affine* law
\[
\boxed{\phi_{n+1}^J=16\phi_n^J+c_n^J\pmod1,\qquad
 c_n^J=16\alpha_n-\alpha_{n+1}\pmod1.}\tag{CZF2}
\]
For h≥0 define \(c_{n,h}=16^h\alpha_n-\alpha_{n+h}\pmod1\). The diagram from A→B→C commutes when the signed connection is retained:
\[
\boxed{c_{n,h+k}=16^k c_{n,h}+c_{n+h,k}\pmod1.}\tag{CZF3}
\]
These are direct substitutions, not new curvature, physical time, entropy or a unique connection independent of source/observer charts.

**The exactly tracking-frame hostile control:** an oracle can select \(\alpha_n=\theta_n\), making \(\phi_n=0\) at every clock **and** \(c_n=0\). The original endpoint information then resides in the *choice of initial origin* \(\alpha_0=x\), and is NOT freely recovered from the apparently zero connection. Hence arbitrary per-clock recentering without an authenticated reference can erase all evidence by construction.

### CZF-02 — exactly fifteen constant zero pins preserve the source map (PROVED PAPER)

If the origin is constant, \(\alpha_n=\alpha\), its connection is \(15\alpha\). Therefore the new circle chart still obeys the **identical** unforced formula \(\phi_{n+1}=16\phi_n\) iff \(15\alpha\in\mathbb Z\). The admissible constant origin positions are exactly the 15 fixed points
\[
\boxed{\alpha\in\{0,1/15,2/15,\ldots,14/15\}\pmod1.}\tag{CZF4}
\]
Other constant reference points remain legitimate, but a correct observer must retain the nonzero affine connection \(15\alpha\). This is a conjugacy of circle dynamics under a coordinate translation; a translation does NOT preserve the group identity as a group automorphism.

The factor 15=16−1 also equals the magnitude of the BBP impulse mask's first nonvanishing signed lag moment, \(Q'(1)=-15\). **These facts are exact but occupy different operational bases**: one concerns chronological circle map equivariance, the other a finite source-Mellin-exponent convolution. No source-valid intertwiner between them has been proved by this numerical coincidence.

## 2. The source-null seed survives a change of zero

The original BBP rational source satisfies \(U_0=0,\ U_{n+1}=16U_n+r(n+1)\). Let \(F_n\) be its particular zero-seeded solution (so in the authentic case \(U_n=F_n\)). Transform to the observer's real-lift coordinate
\[
U'_n=U_n-\alpha_n,\qquad
F'_n=F_n-\alpha_n,\quad
r'(n+1)=r(n+1)+16\alpha_n-\alpha_{n+1}.
\tag{CZF5}
\]

### CZF-03 — source-relative zero, not displayed numerical zero (PROVED PAPER)

\[
\boxed{\mathcal I'_n=16^{-n}(U'_n-F'_n)=16^{-n}(U_n-F_n)=s.}\tag{CZF6}
\]
For the literal original null-information seed \(s=0\), this stays zero in **every correctly transported chart**, despite \(U'_0=-\alpha_0\) being numerically nonzero. An origin change without moving the source passport and reference is a different mathematical model, not an observation of the same carrier.

## 3. The null of the *impulse filter* is not the pin on the physical circle

The previous [BBP Impulse/Mellin Filter](BBP_IMPULSE_MELLIN_FILTER.md) uses the auxiliary lag-shift operator S on finite signed source impulse forms:
\[
Q(S)=(I-S)H(S),\quad Q(z)=4-2z^3-z^4-z^5.
\]
Its zero at \(z=1\) is the **trivial Fourier character of that auxiliary shift representation**. It is *not* the arbitrary point chosen as the zero of the physical \(z_n=e(16^n x)\) orbit.

### CZF-04 — spectrum and kernel survive lawful operator transport (CLASSICAL / PROVED PAPER)

For any unitary basis change G and \(S'=G^{-1}SG\),
\[
\boxed{Q(S')=G^{-1}Q(S)G,\qquad
\ker Q(S')=G^{-1}(\ker Q(S)).}\tag{CZF7}
\]
All singular values and multiplicities, including the zero singular value, are preserved. Thus **re-pinning an origin cannot delete a genuine filter null**. It may move which vector *represents* the null in the new basis. If one rotates displayed frequency coordinates without transporting S and Q together, any apparent migration of the zero is a gauge artifact.

The filter's nonzero cyclic gain still scales as \(\Theta(N^{-1})\) on an \(N\)-point auxiliary circle; choosing another circle marker does not turn it into a source-derived uniform infinite-horizon BBP winding inequality.

## 4. Remove the arbitrary pin from the phase comparison

For the true shell \(I_B=\{B,\ldots,2B-1\}\), put \(z_n=e(16^n x)\) and
\[
W_B(x)=\frac1B\sum_{n=B}^{2B-1}z_n.
\]
The original source-selected, *anchored* R0 defect is \(A_B(0)=1-\Re W_B(x)\). If the observation-zero pin is instead a constant angle \(\alpha\), the analogous reference-relative defect becomes
\[
A_B(\alpha)=1-\Re[e(-\alpha)W_B(x)],\qquad e(t)=e^{2\pi i t}.
\tag{CZF8}
\]
Without a transported source passport, \(A_B(\alpha)\) depends on the chosen pin.

### CZF-05 — a canonical origin-independent shell anti-coherence (PROVED PAPER)

Minimize over *all* fixed circle reference choices:
\[
\boxed{\inf_{\alpha\in S^1}A_B(\alpha)=1-|W_B(x)|.}\tag{CZF9}
\]
The equality is the elementary fact \(\max_\alpha\Re(e(-\alpha)W)=|W|\). Define the intrinsic pair-phase variance
\[
\boxed{
V_B=1-|W_B|^2
=\frac1{B^2}\sum_{B\le n<m<2B}|z_n-z_m|^2.}\tag{CZF10}
\]
Both \(V_B\) and \(1-|W_B|\) are invariant under a **common constant rotation** of all reports.

For clock-dependent frames \(\alpha_n\), the raw readouts \(\zeta_n=e(-\alpha_n)z_n\) must be **transported into one comparison basis first**. Their lawful relative phase is
\[
\boxed{\overline z_m z_n
=\overline\zeta_m\,\zeta_n\,e(\alpha_n-\alpha_m).}\tag{CZF11}
\]
If the observer drops \(\alpha_n-\alpha_m\), a time-varying chart can generate or erase apparent variance. A full closed-form circle law plus its transported reference is therefore part of the witness.

**Strong-versus-weak gap:** a uniform eventual bound \(V_B\ge\delta>0\), equivalently \(1-|W_B|\ge\eta>0\), implies original R0, but is **strictly stronger**. The rational nonunit fixed point \(x=1/15\) has constant \(z_n=e(1/15)\ne1\), so R0 holds while \(V_B=0\) for every B. Thus the source-anchored zero is meaningful even though pairwise comparisons can avoid choosing an arbitrary zero.

The exact two-channel decomposition is
\[
\boxed{
1-\Re W_B=(1-|W_B|)+(|W_B|-\Re W_B),
}\tag{CZF12}
\]
where the first term is **frame-independent phase dispersion** and the second is **alignment relative to the original source's chosen phase identity**. Both terms are nonnegative. This separates what a moving-zero-free interferometer can certify from what needs a source-passported anchor.

## 5. One original rational endpoint produces an origin-free certificate

Retain the literal original source:
\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad x=\pi/16.
\]
Choose the *one* canonical finite rational endpoint \(q_B=P_{2B}=U_{2B}/16^{2B}\). Its shell phases are backward projections \(e(U_{2B}/16^k)\) for \(1\le k\le B\).

Define the fully **rational, source-pinned but phase-origin-independent pair norm**
\[
\boxed{
\mathcal C_B=
\frac1{B^2}\sum_{1\le k<\ell\le B}
\left\|\frac{U_{2B}}{16^k}-\frac{U_{2B}}{16^\ell}\right\|_{\mathbb T}^2.
}\tag{CZF13}
\]
The value \(\mathcal C_B\) is unchanged under adding the *same* circle reference angle to each backward projection. It is not invariant under arbitrary source-changing seeds/gauges unless those changes are accounted for in the original source comparison.

Let
\[
\rho_B=\frac{8r(2B+1)}{225B}.
\]
The inherited BBP tail, \(0<T_{2B}<r(2B+1)/15\), proves
\[
\boxed{|W_B(x)-W_B(q_B)|<\rho_B\to0.}\tag{CZF14}
\]
Indeed each source phase error is bounded by \(2\pi16^{n-2B}T_{2B}\); summing the geometric progression over the B clocks and using \(\pi<4\) gives the displayed rational ceiling.

### CZF-06 — original-source rational pair sandwich (PROVED PAPER)

For arbitrary unit phases \(w_k=e(U_{2B}/16^k)\) with mean \(\overline w\),
\[
1-|\overline w|^2
=\frac1{B^2}\sum_{k<\ell}|w_k-w_\ell|^2.
\]
Since \(4\|a-b\|_{\mathbb T}\le|e(a)-e(b)|\le2\pi\|a-b\|_{\mathbb T}\) and \(1\le1+|\overline w|\le2\),
\[
\boxed{
8\mathcal C_B\le1-|W_B(q_B)|
\le4\pi^2\mathcal C_B.}\tag{CZF15}
\]
Combine with CZF14 and the 1-Lipschitz property of complex modulus:
\[
\boxed{
8\mathcal C_B-\rho_B
\le1-|W_B(\pi/16)|
\le4\pi^2\mathcal C_B+\rho_B.
}\tag{CZF16}
\]

Thus
\[
\boxed{
\liminf_{B\to\infty}\mathcal C_B>0
\iff
\liminf_{B\to\infty}(1-|W_B(\pi/16)|)>0.
}\tag{CZF17}
\]
A positive all-late-shell lower bound in CZF17 would imply R0 for **every choice of constant circle reference**. It is a **stronger theorem target**, not known and not equivalent to the original weaker R0. Full base-16 π normality would require analogues for every nonzero Fourier mode with actual limits tending to zero, not just this positive first-mode dispersion.

### CZF-07 — finite exact original BBP observations (OBSERVED FINITE)

An independent standard-library Fraction implementation computed the exact \(\mathcal C_B\) from the original zero-seeded four poles with no numerical π digits. The lower \(\mathcal L_B=8\mathcal C_B-\rho_B\) is an exact rational certificate of \(1-|W_B|\).

| B | \(\mathcal C_B\) (decimal view only) | Lower bound \(\mathcal L_B\) (decimal view only) |
|---:|---:|---:|
| 4 | 0.03569540244463 | 0.28553345752217 |
| 8 | 0.03889454710512 | 0.31115248904882 |
| 16 | 0.03608117299376 | 0.28864888687649 |
| 32 | 0.04180327048582 | 0.33442610103759 |
| 64 | 0.04169064021998 | 0.33352511385836 |
| 128 | 0.04174617626939 | 0.33396940916455 |

All six source Fraction certificates are strictly \(>1/5\), certified as exact comparisons rather than by rounded decimals. A separately coded 370-digit completed-π circle-phase calculation verified every finite inequality and numerical value (not interval certified). These are **in-sample finite clocks** and do not imply any eventual lower bound.

## 6. Hostile division, epistemic boundary, and next probe

1. **Trivial filter zero versus arbitrary physical circle pin:** the first is the trivial character of a declared lag-shift group representation, not a location chosen on the physical circle. Only a simultaneous operator conjugacy preserves that source.
2. **Source-dependent moving gauge:** selecting \(\alpha_n=\theta_n\) makes every observed phase zero, often with zero frame connection; the apparent disappearance is paid by the oracle's initial source-dependent origin \(\alpha_0=x\).
3. **Fixed nonunit point:** \(x=1/15\) has R0 but no phase dispersion; demanding the gauge-independent pair norm is strictly stronger than necessary.
4. **Locked source:** \(x=0\) has zero pair norm and fails R0. Other changed seeds/forcings require their own passports; the original authenticated source remains fixed.
5. **Sparse irrational cold shells:** the existing \(x_\star\) and Kempner source show that an irrational orbit can have \(|W_{B_j}|\to1\) along infinitely many shells; moving the circle pin cannot manufacture their missing density.
6. **Filter-origin swap without transporting Q(S):** invalid—an apparent moved spectral null is a coordinate artifact, and the actual kernel remains.
7. **Endpoint-only tomography:** pairwise probes of the same single \(U_{2B}\) remain functions of that single scalar. They are gauge-robust observation features, not extra source-history degrees of freedom. Previous history-rank no-go remains active.

**Next decisive arithmetic step (OPEN):** find a source-authenticated original-zero, four-pole/carry/cofactor law implying \(\mathcal C_B\ge\delta>0\) for every late integer B, *or* the weaker two-channel alternative of establishing either intrinsic dispersion \(1-|W_B|\) **or** source-pinned displacement \(|W_B|-\Re W_B\) on every shell without presupposing the desired result. Distinguish all locked and sparse controls with a predeclared signed prediction. Do not identify the Mellin impulse lag operator S with the chronological radix-16 map T without a proved intertwiner.

**Claim status:** CZF-01–06 CLASSICAL/PROVED PAPER; CZF-07 OBSERVED EXACT FINITE; original R0/normality **OPEN**. The source/circle group identity is specified by the authenticated model; its *coordinate presentation* can move. The newly defined pair norm does not solve the missing all-shell quantifier.

**Provenance:** [Source-null section](SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md), [BBP impulse/Mellin filter](BBP_IMPULSE_MELLIN_FILTER.md), [source-shadow variance](../../2026-11-16/defect_window_tomography/SOURCE_SHADOW_INTERFEROMETRY.md), [terminal form norm](../../2026-11-16/defect_window_tomography/VIRTUAL_FIELD_FORM_METRIC.md), [endpoint coercivity audit](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), and [SUCC METHOD](../../../docs/METHOD.md).

**Executable scoped controls:** [tests/test_circle_origin_gauge.py](../../../tests/test_circle_origin_gauge.py); [validation receipt](CIRCLE_ZERO_FRAME_VALIDATION.md). The original source and archived foundations are unchanged.
