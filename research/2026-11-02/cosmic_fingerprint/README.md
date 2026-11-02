# Cosmic Fingerprint — source-labelled astronomical interferometry for SUCC

**DRAFT, November 2 2026.** Stacked on exact draft #464 head 0a69fe3d7260170248e2ef3bf1f1eb5de1b0c0f6. Original four signed BBP poles and U0=0 remain unchanged. This is a freestanding, original-source-compatible observational instrument **NOT a proof of pi normality, RH, or physical electromagnetic emission by SUCC**.

### The exact new instrument

Let z_n=e(hU_n), n=1..M, with the ORIGINAL zero-seeded four-pole rational BBP orbit. Its causal seed-response field is Φ_z(s)=sum z_n e(16^n s), and nonnegative intensity ρ_z=|Φ_z|²/M.

Its universal diagonal background is 1. The centered auto-intensity A_z=ρ_z−1 has exactly the same L² power (M−1)/M for every phase sequence: **phase blind**.

A FIXED coherent reference field w_n=1 repairs the loss. The centered cross-intensity is EXACTLY
\[
\boxed{\int_0^1(\rho_z-1)(\rho_1-1)\,ds
=|S_M(h)|^2/M^2-1/M,}
\]
where S_M(h)=sum e(hU_n). It recovers the selected Weyl modulus from two nonnegative global causal intensity profiles.

A coherent phase-controlled reference even recovers the FULL complex sum from TWO positive globally integrated exposures:
\[
I_0=\int|\Phi_z+R|^2=2M+2\operatorname{Re}S_M,\quad
I_{90}=\int|\Phi_z+iR|^2=2M+2\operatorname{Im}S_M,
\]
so \(S_M=((I_0-2M)+i(I_{90}-2M))/2\). This is a new-to-SUCC phase-referenced observation route, a *classical* Fourier identity, **not** a new signed estimate.

### A certified finite source fingerprint, with a foreground-noise budget

The independently pre-existing exact original p=257 signed certificate in SUCC #459 implies the calibrated 96-state cross-contrast is strictly less than −5/768. The coherent positive **changed source** from #421/#462 has contrast greater than 989/1000 on those same n=33..128 states. With an exactly calibrated reference and L² science-residual foreground error <=1/512, the signs remain separated: original contrast <−7/1536, shadow >987/1000. Those are exact finite inequalities and **not** all-p cancellation bounds.

### Astronomy borrowed — and the rejected shortcut

Planck CMB component separation inspires explicit foreground/reference rank, SDSS/JWST stellar spectroscopy inspires calibrated template correlation, and EHT visibility/closure phases inspire gauge tests. But **a pure SUCC rank-one visibility has identically zero triangle closure phase** regardless of its chronological digits. An explicit unequal two-component Gaussian-rational mixture exhibits nonzero closure, showing what additional data would be required. The physical CMB is itself anisotropic; the exact baseline 1 is only a mathematical analogue.

Read [PROOFS.md](PROOFS.md), [CLAIMS.md](CLAIMS.md), [VALIDATION.md](VALIDATION.md), [SOURCE_MAP.md](SOURCE_MAP.md), [NEXT.md](NEXT.md). Reproduce [cosmic_fingerprint_probe.py](cosmic_fingerprint_probe.py), the root-discoverable test and [independent_sky_oracle.py](independent_sky_oracle.py) (float-only source/orbit diagnostic).

**π normality remains OPEN.** Any proof must establish a genuinely new original four-pole, zero-seed signed all-horizon inequality; calibration, source fingerprinting and faithful recovery are not enough.
