# Moving-Frame Unattainability and Source-Selected Speed Interferometry

**Research continuation:** Principia Observatoris · Defect-Window Tomography · Main XXVI π frontier  
**Date:** 2026-11-16  
**Author's hypothesis:** The subjective observer is always moving relative to the full carrier while naturally resting in its own reference frame. A moving, finite-resource observation horizon cannot be made absolutely source-complete by a fixed finite record. This resembles absolute-zero unattainability in thermodynamics and may permit a source-derived lower bound on π's Fourier anti-locking.

**Verdict:** MF-01–07 are exact classical/source-typed deductions, with finite original-BBP rational observations. MF-08 is a conditional R0 implication whose **source-selected eventual premise remains OPEN**. The physical-third-law and π-normality identifications are **UNVERIFIED**. No claim of mathematical or physics priority.

## 1. Recover the actual carrier, not the metaphor

Retain the original BBP source *and literal zero seed*:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\tag{MF1}
\]

The imported classical BBP identity gives \(x=\pi/16\) and
\[
Y_n=16^nx=U_n+T_n,\quad
T_n=\sum_{j\ge1}16^{-j}r(n+j),
\quad 0<T_n<\beta_n:=r(n+1)/15=O(n^{-2})
\quad(n\ge1).
\tag{MF2}
\]

Define objective circle dynamics \(z_n=e(Y_n)\), \(e(u)=e^{2\pi iu}\). Then \(z_{n+1}=z_n^{16}\).

**MF-01 — no exact objective rest (CLASSICAL / EXACT):**
\[
\boxed{z_{n+1}\ne z_n\quad\text{for every integer }n\ge0.}\tag{MF3}
\]
Indeed equality would require \(15\cdot16^n x\in\mathbb Z\), contradicting the classical irrationality of π. This is a statement about exact stationary *ticks* on the circle, not a lower bound on the magnitude or asymptotic density of motion. For a rational fixed point such as \(x=1/15\), the general "every observer always moves" slogan is false.

## 2. A source-authenticated co-moving observer almost rests

Unlike a chart that secretly presupposes the unknown real number \(x\), use the **known rational original source state** to define
\[
g_n(z)=e(-U_n)z,\qquad w_n=g_n(z_n)=e(T_n).
\tag{MF4}
\]
Every \(g_n\) is a rotation, hence an isometry of the circle; the chart is nonautonomous because the original source clock moves.

**MF-02 — exact co-moving intertwiner (PROVED PAPER):** for *every* \(z\in S^1\),
\[
\boxed{g_{n+1}(z^{16})
=e(-r(n+1))\bigl(g_n(z)\bigr)^{16}.}\tag{MF5}
\]
Proof: substitute \(U_{n+1}=16U_n+r(n+1)\). This is a genuine commuting source/observer square, not a fitted relation between sampled phases. At the actual orbit,
\[
\boxed{w_{n+1}=e(-r(n+1))w_n^{16}
=e(16T_n-r(n+1))=e(T_{n+1}).}\tag{MF6}
\]

Since \(0<T_n<\beta_n<1\) for every \(n\ge1\),
\[
\boxed{w_n\ne1\ \text{at every finite }n\ge1,\qquad
|w_n-1|\le2\pi\beta_n\longrightarrow0.}\tag{MF7}
\]
The observer **approaches rest in a source-calibrated co-moving chart** while the objective phase never has two identical consecutive ticks. If one instead centers the chart at the unknown exact \(z_n\), its state is identically 1 by definition, but that is an oracle chart and not an operational observation.

The frame connection and residual transport compensate exactly:
\[
\underbrace{\frac{z_{n+1}}{z_n}}_{\text{objective movement}}
=\underbrace{e(U_{n+1}-U_n)}_{\text{moving-frame compensator}}
\underbrace{\frac{w_{n+1}}{w_n}}_{\text{residual}},
\quad
U_{n+1}-U_n=15U_n+r(n+1).
\tag{MF8}
\]
Here \(w_{n+1}/w_n=e(T_{n+1}-T_n)\). The original forcing and integer winding/phase are retained. Nonzero connection coefficients are not automatically intrinsic curvature, physical acceleration, heat, or a positive Weil form. This construction is closely related to Principia's signed defect and the [new source-valid BBP carry/fraction compensation in PCE-15](https://github.com/femboy2112/SUCC/pull/661).

### A precise "unattainable zero" analogy

The **finite-stage residual \(T_n\)** is always strictly positive yet tends to zero. Its mathematical infimum is zero, not achieved by any finite truncation. The *actual* thermodynamic third law concerns the resources required to cool material systems to zero temperature under thermodynamic assumptions, not this analytic BBP tail. Masanes–Oppenheim, "A general derivation and quantification of the third law of thermodynamics," *Nature Communications* 8 (2017), [DOI:10.1038/ncomms14538](https://doi.org/10.1038/ncomms14538), establishes resource-sensitive cooling bounds; its thermodynamic results **do not imply** MF1–MF8 or a digit theorem.

## 3. The finite information horizon and entropy are observer-relative

For the **unrestricted** radix-16 carrier \(X\in[0,1)\) with nonterminating canonical digit expansion, let \(D_m(X)\) reveal its first \(m\) hexadecimal digits. The future observation \(D_k(T^n X)\) reveals digits \(n+1,\ldots,n+k\). Given only \(D_m(X)\), the number of possible future \(k\)-digit outputs is
\[
\boxed{16^{\,u},\qquad u=\min\{k,\max(0,n+k-m)\}.}\tag{MF9}
\]
This is an elementary finite cylinder-count theorem; each previously unknown digit is freely chosen in the *full-shift source class*. It is exact and optimal for each declared \(m,n,k\). A fixed finite initial precision \(m\) cannot unambiguously determine *all* future \(k\)-digit reports for arbitrary large \(n\); a target at horizon \(n\) requires at least \(n+k\) initial hexadecimal digits in the worst case.

**MF-03 — conditional Shannon horizon (CLASSICAL, WITH AN EXPLICIT PRIOR):** if **the carrier \(X\) is Haar/Lebesgue uniform** on \([0,1)\), the unknown digits are independent uniform symbols, and
\[
\boxed{H(D_k(T^nX)\mid D_m(X))
=4\,\min\{k,\max(0,n+k-m)\}\ {\rm bits}.}\tag{MF10}
\]
This is *epistemic Shannon entropy relative to an explicitly random full-shift prior*, not thermodynamic entropy, an independent prime coin, or a law for the digits of deterministic \(x=\pi/16\). For a point-mass prior on the authenticated exact BBP source, Shannon entropy is zero. Finite mathematical extraction of any fixed set of π digits is possible by refining the convergent BBP interval; the unbounded-horizon information demand is not an absolute undecidability theorem.

A growing observation budget may keep up with the moving horizon. Thus the unrestricted claim "no observer can ever pin carrier-relevant data" is **REFUTED** unless source family, accessible instruments, precision and budget are all specified.

## 4. A relative-motion energy that *would* force R0

Define the objective squared step-speed on each integer shell \(B\ge1\):
\[
\boxed{\mathcal S_B(x)=\frac1B\sum_{n=B}^{2B-1}|z_{n+1}-z_n|^2
=\frac2B\sum_{n=B}^{2B-1}\bigl(1-\cos(2\pi\,15\cdot16^nx)\bigr).}\tag{MF11}
\]
This is a **nonnegative squared chord diagnostic**, not physical kinetic energy or an inference from individual instantaneous velocity. In terms of the radix map it is a signed Fourier mode \(h=15=16-1\) in disguise.

Set \(A_B(x)=1-\Re W_B(x)\), \(W_B(x)=B^{-1}\sum_{n=B}^{2B-1}z_n\).

**MF-04 — exact speed-to-R0 bridge (PROVED PAPER):**
\[
\boxed{A_B(x)\ge\frac18\,\mathcal S_B(x)-\frac1B.}\tag{MF12}
\]
Proof: \(|z_{n+1}-z_n|^2\le2|z_{n+1}-1|^2+2|z_n-1|^2\) and
\(\sum_{n=B}^{2B-1}|z_{n+1}-1|^2
=\sum_{n=B}^{2B-1}|z_n-1|^2+|z_{2B}-1|^2-|z_B-1|^2
\le2BA_B+4\). Use \(\sum|z_n-1|^2=2BA_B\) and divide by \(B\).

A weaker **zero-boundary-cost** inequality is also exact:
\[
\boxed{A_B(x)\ge\frac{\mathcal S_B(x)}{450}.}\tag{MF13}
\]
Indeed \(|z^{16}-z|=|z^{15}-1|\le15|z-1|\), so \(\mathcal S_B\le450 A_B\). Either formula shows that a source-selected all-late-shell lower bound \(\mathcal S_B(\pi/16)\ge\delta>0\) would imply R0. The reverse implication is false: \(x=1/15\) has a fixed nonunit phase, satisfies R0, and has \(\mathcal S_B=0\).

### Do not confuse permanent nonzero motion with positive speed density

For irrational \(x\), \(\mathcal S_B>0\) at every finite \(B\) because no individual objective step is exactly stationary. **It does not follow that** \(\inf_{B\ge B_0}\mathcal S_B>0\). The existing sparse irrational hostile control \(x_\star=3/16+\sum_{j\ge1}16^{-4^j}\) has \(\mathcal S_{B_j}\to0\) on the selected shells \(B_j=2\cdot4^j\) because MF12 bounds \(\mathcal S_{B_j}\le8 A_{B_j}+8/B_j\), and \(A_{B_j}\to0\). It is irrational and moves at every tick, yet no eventual uniform speed margin exists. This is a **decisive refutation** of "always moving ⇒ R0."

## 5. Certified relative-speed lower bounds from the four BBP poles

The full phase \(Y_n\) is not computed with floating π. Define the rational circular metric
\(\|a\|_{\mathbb T}=\min_{m\in\mathbb Z}|a-m|\), and the **exact rational certificate**
\[
\boxed{
d_n=\big[\|15U_n\|_{\mathbb T}-r(n+1)\big]_+,\qquad
\mathcal Q_B^{\mathrm{speed}}=
\frac{16}{B}\sum_{n=B}^{2B-1}d_n^2.}\tag{MF14}
\]

**MF-05 — source-selected speed certificate (PROVED PAPER):**
\[
\boxed{\mathcal S_B(\pi/16)\ge\mathcal Q_B^{\mathrm{speed}}\ge0.}\tag{MF15}
\]
**Proof:** \(z_{n+1}/z_n=e(15Y_n)\). The tail bound gives \(\|15Y_n\|_{\mathbb T}\ge[\|15U_n\|_{\mathbb T}-15T_n]_+ \ge d_n\), because \(15T_n<r(n+1)\). For any circular distance \(d\in[0,1/2]\), \(|e(d)-1|=2\sin(\pi d)\ge4d\). Square and average. \(\square\)

All quantities in \(\mathcal Q_B^{\mathrm{speed}}\) are rationals from the literal original zero-seeded four poles, with no random clock, π digits or fitted source parameter.

**MF-06 — OBSERVED FINITE EXACT:** an exact stdlib Fraction implementation certified:

| B | \(\mathcal Q_B^{\rm speed}\) (decimal view only) | Implication \(A_B\ge\mathcal Q_B/8-1/B\) |
|---:|---:|---:|
| 16 | 1.115511010778805585 | \(>0.0769\) |
| 32 | 1.419544018700511624 | \(>0.1461\) |
| 64 | 1.457849048509467970 | \(>0.1666\) |
| 128 | 1.335706813143392397 | \(>0.1591\) |
| 256 | 1.332030683976076938 | \(>0.1625\) |

Every strict comparison used the actual exact Fraction, not these decimal approximations; in particular \(\mathcal Q_B^{\rm speed}>6/5\) for \(B\in\{32,64,128,256\}\), giving **finite-only** \(A_B>1/10\) there. These clocks are previously explored training territory, **not independent prospective holdouts**. The condition for every large shell remains OPEN.

**MF-07 — independent numerical representation audit (OBSERVED):** a distinct 760-digit mpmath computation of the completed phase reported true \(\mathcal S_B\) values of approximately \(1.615,2.106,2.172,2.017,2.043\), respectively, each exceeding the rational certified \(\mathcal Q_B\). This is a diagnostic high-precision replay on the same classical source, not a rigorous interval oracle or an independent proof of the π identity. Full finite execution receipts and mutated controls belong to [VALIDATION](MOVING_FRAME_VALIDATION.md).

## 6. The next decisive source-selected theorem (MF-08, OPEN)

The proposed arithmetic gate is precisely
\[
\boxed{
\exists\delta>0,\ B_0\ \forall B\ge B_0:
\quad \frac1B\sum_{n=B}^{2B-1}
\big[\|15U_n\|_{\mathbb T}-r(n+1)\big]_+^2
\ge\delta.}\tag{MF16}
\]

Then \(\mathcal S_B\ge16\delta\), and MF12 or MF13 yields a **uniform positive** \(A_B\), so R0 follows. For example MF13 gives the explicit eventual margin \(A_B\ge (16/450)\delta\).

**This is not proved.** It is a sufficient condition, *stronger* than R0. Its strength is that it asks about a **one-step, source-anchored rational phase diagnostic** involving the actual chronological four-pole recurrence, rather than generic observer entropy, source-blind Gamma smoothing or an arbitrarily partitioned phase variance.

For the canonical coherent wrong seed \(s=-x\), the completed orbit is exactly zero phase and the analogous \(d_n\) on its changed-state carrier vanishes because \(U_n(s)=-T_n\) and \(15T_n<r(n+1)\). For the scalar-periodic \(x=1/15\) control, speed is also zero even though R0 holds. For the sparse irrational control, the average speed gate fails along infinitely many shells.

### Where interferometry could earn new source content

The mode \(15=3\cdot5\) is arithmetically factorable, and the previous source work supplies carry, fractional remainder, odd-denominator cofactor, CRT and source-conditioned Gamma windows. But **factorization of 15 is not itself a prime-source theorem**. A genuine new proof would derive a lower shell budget for the rational clock statistic MF16 using the true zero ancestry and one of these retained source interfaces. It must not average away sign, substitute an independent prime clock, or promote positive full-shift entropy to the actual π orbit.

A concrete prospective protocol:

1. Freeze the source passport \(r,U_0=0\) and the typed observer: objective phase, rational co-moving frame, and speed window MF14.
2. Seek a *source-derived* conditional arithmetic estimate forcing the MF16 rational mean to remain positive on every late integer shell; an available finite certificate or high source resolution is not the missing quantifier.
3. Test each claimed inequality against coherent wrong seed, rational finite-shadow seeds from Main XXVI, sparsely moving irrational controls, coboundary gauges with corrected tail, and the \(x=1/15\) nonunit fixed phase.
4. Declare whether the new speed gate truly splits an old survivor class before attempting fresh held-out clocks beyond 131072; verify a frozen numerical prediction separately from any analytic proof.
5. The correct victory condition is a proved all-shell bound for the **authentic** carrier, which yields R0. Full base-16 π normality still requires all nonzero Weyl modes.

## 7. Claim ledger and provenance firewall

| Claim | Status | Scope / next falsifier |
|---|---|---|
| MF-01 | CLASSICAL / PROVED PAPER | Irrational π ⇒ no exact two-tick circle rest; sparse irrational defeats a uniform speed inference |
| MF-02 | PROVED PAPER | Exact source-rational co-moving intertwiner; \(w_n=e(T_n)\to1\) yet \(w_n\ne1\) for all finite n |
| MF-03 | CLASSICAL / PROVED CONDITIONAL | Full-shift digit horizon, conditional entropy under a Haar prior; **not** digit entropy of π |
| MF-04 | CLASSICAL / PROVED PAPER | Speed-to-R0 sufficient inequalities, zero- and nonzero-boundary versions |
| MF-05 | PROVED PAPER | Exact positive rational \(U_n,r(n+1)\) speed lower envelope |
| MF-06 | OBSERVED EXACT FINITE | \(B=16,32,64,128,256\) rational source certificates, no all-shell conclusion |
| MF-07 | OBSERVED NUMERICAL | Independent high-precision phase replay, not a rigorous interval certificate |
| MF-08 | OPEN / UNVERIFIED | Uniform zero-seed rational speed-energy lower bound for every late shell; R0/full normality remain OPEN |
| Thermodynamic equivalence | UNVERIFIED | No measured temperature, heat, Hamiltonian, thermal bath or physical resource model |

**Dependencies:** Main XXVI [π frontier](../../../docs/PI_NORMALITY_FRONTIER.md), [source-phase interface](../../../docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md), [interferometry and pair-mass gate](SOURCE_SHADOW_INTERFEROMETRY.md), [adaptive Gamma microscope](ADAPTIVE_GAMMA_ICE_CLIMB.md), [source-valid carry/fraction compensation in PCE](https://github.com/femboy2112/SUCC/pull/661), and [Principia observer dynamics](../../../docs/principia_observatoris/02_causality_geometry.md). These are not independent sources of evidence just because several use the same four BBP coefficients. 

**Validation:** [the focused exact tests](../../../tests/test_moving_frame_horizon.py) and [source-replay evidence](MOVING_FRAME_VALIDATION.md) describe executed checks and unrun root gates. No claim of academic priority, physical third-law proof, π normality, RH, or completed Weil positivity.
