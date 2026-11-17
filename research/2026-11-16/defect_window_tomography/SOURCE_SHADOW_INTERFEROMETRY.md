# Source-Shadow Interferometry — Exact Rational Phase-Variance Certificates on the Original BBP Orbit

**Research:** Principia Observatoris / Defect-Window Tomography / Gamma Ice-Climb  
**Date:** 2026-11-16  
**Author's proposal:** Leah — interrogate the connected causal patches beyond a coarse subjective observer's horizon using multiple observer windows and source-authenticated signed defects. Ask whether the literal zero-seeded four-pole BBP dynamics forces enough hidden phase disagreement, on *every late shell*, to establish the first escape rung R0.  
**Status:** IFS-01–07 are classical identities and exact finite rational source certificates; IFS-08 is a certified finite large-pair witness; IFS-09 is a proved no-go for unrestricted observer quantifiers; IFS-10 is an OPEN, precisely formulated original-source inequality. No π-normality, RH, physical causal-energy or quantum result is asserted.

## 1. Restore all types: source, time, observation, phase, and pair

Retain *exactly* the canonical BBP source and its zero seed:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Put \(x=\pi/16\) using the *imported classical BBP identity*; let

\[
P_n=\sum_{j=1}^n16^{-j}r(j),\quad U_n=16^nP_n,\quad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\quad
Y_n=U_n+T_n=16^nx.
\]

The source-derived future bound, retained in Main XXVI, is

\[
0<T_n<\beta_n:=r(n+1)/15,\quad n\ge1. \tag{IFS1}
\]

Let \(e(t)=e^{2\pi it}\), \(z_n=e(Y_n)\) and \(W_B=B^{-1}\sum_{B\le n<2B}z_n\). The *objects being grouped* are **time indices from one authenticated trajectory**, not alternate source worlds or independent Bernoulli digit draws.

A **finite subjective observer** is a specified shell-local partition \(\Pi_B\) of the integer indices \(I_B=\{B,\ldots,2B-1\}\) into nonempty cells \(C\). It remembers a label but discards distinctions between indices inside the same cell. Example: \(\Pi_B^{\mathrm{carry}}\) identifies times with the same literal \(C_n=\lfloor U_n\rfloor\bmod4\); \(\Pi_B^{\mathrm{clock}}\) identifies \(n\bmod4\). These are *different* readouts. If the observer also retains exact \(n\), its cells are singletons and the hidden-fiber energy below is identically zero. No assertion is made that a physical carrier erases its time coordinate.

Write \(p_C=|C|/B\), \(\mu_C=|C|^{-1}\sum_{n\in C}z_n\). All comparisons below use **the same chronological phase basis**, rather than separate means substituted inside nonlinear exponentials.

## 2. The exact three-observer Pythagorean interferometer

Define the within-cell hidden-phase variance

\[
\boxed{\mathcal V_{B,\Pi}
=\frac{1}{2B}\sum_{C\in\Pi}\frac1{|C|}
\sum_{n,m\in C}|z_n-z_m|^2
=\sum_Cp_C(1-|\mu_C|^2).}
\tag{IFS2}
\]

Define the subjective cell-centroid displacement from the distinguished reference phase \(1\) by

\[
\mathcal L_{B,\Pi}=\sum_Cp_C|\mu_C-1|^2.
\tag{IFS3}
\]

**IFS-01 (CLASSICAL / PROVED PAPER; exact anchored variance):**

\[
\boxed{
2(1-\Re W_B)=\mathcal V_{B,\Pi}+\mathcal L_{B,\Pi}.
}
\tag{IFS4}
\]

**Proof:** on each cell expand \(|z_n-1|^2=|(z_n-\mu_C)+(\mu_C-1)|^2\); the signed cross term vanishes because \(\sum_{n\in C}(z_n-\mu_C)=0\). Sum with \(1/B\). Since \(|z_n|=1\), \(B^{-1}\sum|z_n-1|^2=2(1-\Re W_B)\). The pair identity follows by expanding the double sum. \(\square\)

**IFS-02 (CLASSICAL / PROVED PAPER; global variance):**

\[
\boxed{1-|W_B|^2
=\mathcal V_{B,\Pi}
+\sum_Cp_C|\mu_C-W_B|^2.}
\tag{IFS5}
\]

Hence for every \(B,\Pi\):

\[
0\le\mathcal V_{B,\Pi}\le1-|W_B|^2
\quad\Longrightarrow\quad
\boxed{\mathcal V_{B,\Pi}\ge\delta>0
\implies\Re W_B\le\sqrt{1-\delta}<1.}
\tag{IFS6}
\]

Thus a *uniform positive within-fiber bound on every sufficiently late integer shell* would suffice for R0. It is **stronger than R0**, not equivalent: a constant nonunit phase can have R0 while every within-fiber variance is zero.

### Observer refinement is a measurable loss of hidden variance

For a refinement \(\Pi'\) of \(\Pi\) (every \(\Pi'\)-cell lies in a \(\Pi\)-cell), write \(\mu_{C'}\) for the finer means. Then

\[
\boxed{
\mathcal V_{B,\Pi}-\mathcal V_{B,\Pi'}
=\sum_{C\in\Pi}\sum_{\substack{C'\in\Pi'\\C'\subseteq C}}
\frac{|C'|}{B}|\mu_{C'}-\mu_C|^2\ge0.}
\tag{IFS7}
\]

**IFS-03 (CLASSICAL / PROVED PAPER):** this is exact conditional-expectation/variance decomposition. It is the mathematical information gained by a finer readout. It is not itself physical heat, entropy production, a causal-transport phase, or a theorem identifying the actual source of the lost directions.

**Important computational distinction:** IFS7 applies to **true** variance. A conservative rational lower-bound estimator built by replacing each chord with a separate pairwise lower bound need not be monotone under arbitrary partition refinement; finite instances can be tested but no invalid universal monotonicity is asserted for that estimator.

## 3. A completely rational BBP phase-interference certificate

For real \(a\), write \(\|a\|_{\mathbb T}=\min_{m\in\mathbb Z}|a-m|\). For any real \(t,s\),

\[
|e(t)-e(s)|=2\sin\big(\pi\|t-s\|_{\mathbb T}\big)
\ge4\|t-s\|_{\mathbb T},
\tag{IFS8}
\]

since \(\sin(\pi d)\ge2d\) for \(0\le d\le1/2\). Circular distance is 1-Lipschitz under additive perturbations.

Define **exact rational** pair and anchor depths on the original zero-seeded source:

\[
\boxed{
a_{n,m}:=\Big[\|U_n-U_m\|_{\mathbb T}-\beta_n-\beta_m\Big]_+,
\qquad
a_{n,0}:=\Big[\|U_n\|_{\mathbb T}-\beta_n\Big]_+,
}
\tag{IFS9}
\]

where \([v]_+=\max(0,v)\) and all \(U,\beta\) are generated from the four poles via finite Fraction arithmetic. Since \(Y_n-U_n=T_n\in(0,\beta_n)\),

\[
|z_n-z_m|\ge4a_{n,m},\qquad |z_n-1|\ge4a_{n,0}.
\tag{IFS10}
\]

**IFS-04 (PROVED PAPER; certified finite rational lower bounds):**

\[
\boxed{\mathcal V_{B,\Pi}\ge\mathcal Q_{B,\Pi}
:=\frac{16}{B}\sum_{C\in\Pi}\frac1{|C|}
\sum_{\substack{n<m\\n,m\in C}}a_{n,m}^2.}
\tag{IFS11}
\]

\[
\boxed{
1-\Re W_B\ge\mathcal A_B^{\rm rat}
:=\frac8B\sum_{n=B}^{2B-1}a_{n,0}^2.
}
\tag{IFS12}
\]

Both right-hand sides are **nonnegative rationals** calculated entirely from a *finite authenticated BBP prefix and rigorous source tail*. The inequalities are universal under the stated tail condition. They are not estimates of a statistical probability law.

**Proof:** substitute IFS10 into the unordered-pair form of IFS2 and the anchor identity \(1-\Re W_B=(2B)^{-1}\sum|z_n-1|^2\). Square the nonnegative chord lower bounds. \(\square\)

These formulas allow exact finite claims about the specific \(\pi/16\) orbit **without numerical evaluation of π, rounding complex exponentials, or assuming independent hexadecimal digits**.

## 4. Finite source-selected measurements (executed; not an asymptotic theorem)

The local exact-rational verifier computes \(U_n\) from the literal zero seed and \(r(n)\) for \(1\le n\le512\), uses \(\beta_n=r(n+1)/15\), and evaluates IFS11 as a Fraction. The displayed decimals below are only readable truncations of those exact lower bounds. Threshold comparisons use exact rational \(3/5\), not floating-point rounding.

| Shell start B | Carry-only \(\mathcal Q_{B,\Pi_{\rm carry}}\) | Clock-only \(\mathcal Q_{B,\Pi_{\rm clock}}\) | Joint carry×clock \(\mathcal Q\) |
|---:|---:|---:|---:|
| 32 | approximately 0.65287 | approximately 0.60693 | approximately 0.44269 |
| 64 | approximately 0.63805 | approximately 0.63190 | approximately 0.53490 |
| 128 | approximately 0.65959 | approximately 0.64348 | approximately 0.58102 |
| 256 | approximately 0.65325 | approximately 0.65020 | approximately 0.62533 |

**IFS-05 (OBSERVED EXACT FINITE CERTIFICATE):** for every \(B\in\{32,64,128,256\}\),

\[
\boxed{\mathcal V_{B,\Pi_{\rm carry}}>
\mathcal Q_{B,\Pi_{\rm carry}}>\frac35.}
\tag{IFS13}
\]

The strict rational lower inequality also holds for the separate clock-only observer on these four shells. Therefore the original π orbit satisfies the rigorous **finite-only** bounds

\[
\boxed{\Re W_B(\pi/16)<\sqrt{2/5}
\qquad(B=32,64,128,256).}
\tag{IFS14}
\]

These are specific finite signed shell consequences of authenticated rational arithmetic. The source has been studied previously to horizons far beyond these shells; **these are not a fresh held-out statistical prediction**. They do not imply anything for all sufficiently large \(B\), nor π normality.

The completed-orbit phase relation is used only through the classical BBP source identification and the rigorous tail. Comparing the same Fraction source by both the chronological recurrence and a direct weighted partial sum is a code-level cross-check, not an independent proof of the imported BBP identity.

### IFS-06: a one-sided anchored rational certificate

The independent rational anchor sum \(\mathcal A_B^{\rm rat}\) in IFS12 also exceeds \(1/2\) for \(B=4,8,16,32,64,128\) in exact finite tests. Because it measures distance to the reference phase \(1\), this already directly verifies nonlocking on those **specific** shells. It cannot be turned into R0 without its eventual all-integer-shell quantifier.

## 5. Turn a hidden causal patch into a *mass* criterion, not mere existence

Fix a rational separation threshold \(\epsilon>0\). Let \(N_{B,C}(\epsilon)\) be the number of **unordered** source pairs inside cell \(C\) with \(a_{n,m}\ge\epsilon\). The exact rational estimator obeys

\[
\boxed{
\mathcal Q_{B,\Pi}
\ge\frac{16\epsilon^2}{B}
\sum_C\frac{N_{B,C}(\epsilon)}{|C|}.
}
\tag{IFS15}
\]

**IFS-07 (PROVED PAPER; pair-mass gate).** If there exist \(\epsilon,\theta>0\), \(B_0\) and a source-authenticated admissible partition schedule \(\Pi_B\) such that

\[
\boxed{
\forall B\ge B_0:\quad
\sum_C\frac{N_{B,C}(\epsilon)}{|C|}
\ge\theta B,
}
\tag{IFS16}
\]

then \(\mathcal V_{B,\Pi_B}\ge16\epsilon^2\theta\) and consequently

\[
\boxed{
\Re W_B(\pi/16)\le\sqrt{1-16\epsilon^2\theta}<1
\quad\text{for all }B\ge B_0,
}
\tag{IFS17}
\]

with the parameters necessarily in the feasible range \(0<16\epsilon^2\theta\le1\). **This would prove R0.** It does not follow from the existence of a single hidden pair on every shell: a lone pair can have weight \(O(B^{-2})\) for a large cell. Positive density/weighted pair mass is the unpaid arithmetic content.

**IFS-08 (OBSERVED FINITE SOURCE-MASS CONTROL):** at threshold \(\epsilon=1/4\), the carry-only observer's exact rational weighted pair mass divided by \(B\), for \(B=32,64,128,256\), is approximately \(0.25208, 0.23688, 0.24661, 0.24712\). This is an *orientation-preserving source test* of the proposed pair budget, not a universal lower bound. The full \(\mathcal Q\) uses all pairwise distances, not only the thresholded ones.

No independence of pair outcomes is assumed. A source-specific future theorem must handle their deterministic chronological coupling.

## 6. Gamma translation and the A→B→C observer ladder

The [adaptive Gamma Ice-Climb](ADAPTIVE_GAMMA_ICE_CLIMB.md) constructs a **declared additional** forward microscope with an exactly transported nonlinear observation-order defect:

\[
\mathscr D_{n-1}(x)=c(x)z_n(x),\qquad
c(x)=q(x)-q(x/16)^{16},\quad
q(x)=(1-2\pi ix)^{-1}.
\tag{IFS18}
\]

Its source-independent composition uses the same real-lift family. The earlier paper proves \(|c(\pi/16)|>1/5\). The *Gamma-defect* version of within-fiber energy is therefore

\[
\boxed{
\mathcal V^\Gamma_{B,\Pi}
=\frac{1}{2B}\sum_C\frac1{|C|}
\sum_{n,m\in C}|\mathscr D_{n-1}-\mathscr D_{m-1}|^2
=|c(x)|^2\mathcal V_{B,\Pi}.
}
\tag{IFS19}
\]

**IFS-09 (PROVED PAPER; equivalent signed instrument):** the Gamma defect transports the full interference energy without loss of orientation when the fixed nonzero complex scalar is retained. In particular, the four finite carry-only shells in IFS13 satisfy

\[
\boxed{\mathcal V^\Gamma_{B,\Pi_{\rm carry}}>3/125.}\tag{IFS20}
\]

The value \(3/125\) combines two *previously proved* separate lower bounds, \(3/5\) and \(|c|^2>1/25\); it is **not** another independent source observation. If the phase is replaced with \(|\mathscr D_n|\), every time has the same magnitude \(|c(x)|\), so the resulting within-cell energy is zero. Carrying the complex phase is indispensable.

This is a successful algebraic **A→B, B→C → A→B→C versus A→C** comparison of raw and compressed windows, and a finite original-BBP witness. It still does not supply the missing eventual signed estimate.

## 7. Hostile division: universal observer claims fail

**IFS-10a — REFUTED: 'any chosen finite-resolution observer must see positive hidden variance'.** An observer retaining the exact index \(n\) has singleton cells; hence \(\mathcal V_{B,\Pi}=0\) identically for every source, including π. A source-aware sufficiently refined phase-digit partition can also make within-cell variance arbitrarily small: for cells of phase-arc width \(\Delta=16^{-k}\),

\[
\boxed{\mathcal V_{B,\Pi_{\rm phase},k}\le\pi^2\,16^{-2k}.}\tag{IFS21}
\]

Proof: for each arc choose the midpoint unit complex phase \(v_C\); every member is at complex distance at most \(\pi\Delta\) from it. The cell mean minimizes squared Euclidean distance, so conditional variance is at most \(\pi^2\Delta^2\). This bound is true for **every source**. Thus an arbitrary observer's hidden variance is neither an intrinsic source invariant nor a universal lower certificate. Specify the observer *passport* first.

**IFS-10b — REFUTED: 'within-fiber variance lower bound is necessary for R0'.** For \(x=1/15\), \(16x\equiv x\bmod1\), so \(z_n=e(1/15)\ne1\) is constant. It satisfies R0 with margin \(1-\cos(2\pi/15)>0\), yet \(\mathcal V_{B,\Pi}=0\) for every observer and shell. The anchor-centroid term in IFS4 carries the entire deviation.

**IFS-10c — REFUTED: 'one hidden patch beyond every finite horizon forces a uniform margin'.** The sparse irrational control \(x_\star=3/16+\sum_{j\ge1}16^{-4^j}\) from the [adaptive Gamma dossier](ADAPTIVE_GAMMA_ICE_CLIMB.md) has nontrivial source structure arbitrarily deep, but along \(B_j=2\cdot4^j\),
\[
1-\Re W_{B_j}(x_\star)<32\pi/(225B_j)\to0.
\]
By IFS5, \(\mathcal V_{B_j,\Pi}\le1-|W_{B_j}|^2\le2(1-\Re W_{B_j})\to0\), for **every** partition schedule. Mere connectedness at arbitrarily high indices has no quantitative mass obligation.

**IFS-10d — source-blind same-forcing mutant:** changing the BBP seed to \(s=-x\) gives the identically-one completed real circle and zero within-fiber variance for every observer, while forcing-only Gamma/Green windows are unchanged. The actual zero seed and integer history must be used in any source-selection argument.

**IFS-10e — source-resolution mixing:** the partitions \(\Pi_{\rm carry}, \Pi_{\rm clock}\), their joint refinement, and digit-prefix partitions are not interchangeable. A joint-cell gain is not evidence of a causal mixed derivative unless every declared source/intervention cell and covariance transport is supplied. Never claim curvature or physical quantum interference from the positive pair Gram alone.

## 8. Claim-status ledger and next verdict-changing theorem

| ID | Authority | Surviving theorem / remaining debt |
|---|---|---|
| IFS-01/02 | **CLASSICAL / PROVED PAPER** | Anchored and global Pythagorean variance identities; sufficient \(V\)-lower bound for R0. |
| IFS-03 | **CLASSICAL / PROVED PAPER** | Law of total variance under explicitly refinable observer partitions. |
| IFS-04 | **PROVED PAPER** | Exact BBP \(U_n,\beta_n\)-only rational chord/anchor lower certificates. |
| IFS-05/06 | **OBSERVED FINITE EXACT** | Four shell carry and clock lower bounds \(>3/5\); six finite anchor bounds \(>1/2\). No asymptotic quantifier. |
| IFS-07 | **PROVED CONDITIONAL IMPLICATION** | Positive weighted source-separated pair mass on every late shell implies R0. |
| IFS-08 | **OBSERVED FINITE EXACT** | Source-attached \(1/4\)-pair mass in four finite shells; no future density estimate. |
| IFS-09 | **PROVED EQUIVALENT INSTRUMENT** | Full complex Gamma-defect pair variance scales by \(|c(x)|^2\); no new statistical saving. |
| IFS-10 | **OPEN SOURCE-SPECIFIC ESTIMATE**, with multiple **REFUTED** overstrong readings | Need a zero-seed/four-pole-derived positive all-late-shell lower bound, not an observer-uniform tautology. |

**Executed finite checks:** [test_shadow_interferometry.py](../../../tests/test_shadow_interferometry.py) uses only standard-library Fraction arithmetic. It validates the chronological recurrence against the independently summed BBP prefix, exact pair metrics and sum weights, all four finite carry/clock thresholds, refinement identity on Gaussian-rational unit-circle controls, Gamma-scalar energy, source-tail mutations, and the fixed-phase/locked/singleton counterexamples. See [VALIDATION](SOURCE_SHADOW_INTERFEROMETRY_VALIDATION.md) for the exact run and the non-claims. The paper is a combination of elementary harmonic geometry and authenticated finite BBP data; independent source verification is not inferred from two algorithms sharing the same coefficients.

**Next offensive (OPEN; genuinely verdict-changing):** choose a *fixed source passport* such as the literal \(C_n\bmod4\) observer, predeclare \(\epsilon,\theta>0\), and try to prove the weighted source-pair count IFS16 for every large integer shell using the original odd-denominator, fractional-cofactor, integer-winding and zero-seed chronology. First attack any candidate bound with same-forcing wrong seeds, rational finite shadows and source-coboundary frames; then establish a genuinely independent arithmetic estimate. If this gate survives, IFS17 yields R0. The original full base-16 normality still requires every nonzero Fourier mode; a finite interferometer does not promote that conclusion.
