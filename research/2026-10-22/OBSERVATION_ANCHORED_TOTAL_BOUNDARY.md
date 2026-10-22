# SUCC — Observation-anchored total boundary: realization selection, not constant derivation

**Research date:** 2026-10-22. **Stacked branch:** `research/total-boundary-adelic-impedance-2026-10-22`, based on Witt Carry Observer Limit PR #240 at `68c6d82aed31c8337826841c3bce023790c0e821`. **Research only**: main and historical frozen files untouched. Classical results plus new-to-SUCC source interfaces; academic originality not established. No actual physical measurements, derived fine-structure constant, gravitational ER=EPR, signed Weil positivity, or RH proof.

## 1. Corrected research target: select a model, not a universal number

Let M be the predeclared family of mathematically coherent source/geometry models satisfying SUCC/FUCC, boundary, arithmetic and analytic constraints, with gauge/source equivalence ~. Each model must, **before examining the observation**, define a physically meaningful boundary response Lambda_M(scale) and a dimensionless observable O_j(M).

An independently calibrated experiment returns data y_j with observation uncertainties eps_j and justified theoretical prediction uncertainties tau_j(M). The **surviving model fiber** consists of M such that |O_j(M)-y_j| <= eps_j + tau_j(M) for every j.

**ABR-04 (conditional finite identification).** If exactly one gauge-equivalence class intersects these predeclared measurement bands, the experiment selects that class **relative to the admissible family**. A sufficient robust condition is pairwise prediction separation greater than twice a common bound on total uncertainty, with a true prediction inside its claimed error budget. This is immediate interval geometry; it does not prove the source family exhaustive.

**ABR-05 (conditional compact limit).** If X=M/~ is compact Hausdorff and the full observation operator F:X->R^d is continuous and injective, F is a homeomorphism onto its image. Thus an indefinitely improving compatible stream of observations converging to F(M_actual) yields estimates approaching M_actual **within the declared family**. Actual physical sensor/source faithfulness, model-class coverage, and the existence of a separating F remain independent obligations. A single scalar is generally incapable of separating unrestricted high-dimensional moduli; if it separates a finite or sufficiently constrained family, one scalar may suffice.

A model that allows its free parameter to be set equal to the measured constant after observing it has **calibrated a parameter**, not predicted a geometry or supplied independent confirmation. Require a held-out consequence not used in the fit.

## 2. Literal boundary-only interaction, with no mystery field

For a finite positive resistor network with boundary B and interior I, its energy operator is block-decomposed:
\[
L=\begin{pmatrix}C&B^*\\B&A\end{pmatrix}
\]
with invertible interior block A. Eliminating interior states gives the standard Dirichlet-to-Neumann boundary response
\[
\boxed{\Lambda=C-B^*A^{-1}B.}
\]
For two disjoint interiors touching **only along a common interface**, identify their boundary potentials; their boundary fluxes add, hence
\[
\boxed{\Lambda_{\rm glued}=\Lambda_1+\Lambda_2}
\]
on that interface (under the stated common trace orientation). More exterior/interior blocks require further Schur elimination. This is an exact operational model for the user's boundary-only coupling intuition. It is **not** yet a SUCC-derived physical gravitational boundary operator.

## 3. ABR-02: exact geometry nonidentifiability even with the whole static response

Two genuinely different finite networks can have identical entire static boundary maps:

- Direct 2-terminal edge of resistance 2 (conductance 1/2).
- Two edges of resistance 1 joined in series through one hidden interior node.

For both, exact rational elimination gives
\[
\Lambda_{\rm edge}(0)=\Lambda_{\rm series}(0)
=\begin{pmatrix}1/2&-1/2\\-1/2&1/2\end{pmatrix}.
\]

This is stronger than a constant-fitting ambiguity. **Every** DC boundary voltage/current experiment has the same result, though the internal graphs are nonisomorphic. Repeating the static experiment indefinitely never distinguishes them.

### ABR-03: a predeclared dynamic probe breaks the tie

Place an independent shunt capacitor of value 1 at the hidden interior node **in the second candidate's stipulated physical realization**. Its Laplace-domain boundary response at real s>=0 is
\[
\Lambda_{\rm series}(s)=
\begin{pmatrix}
1-(2+s)^{-1}&-(2+s)^{-1}\\
-(2+s)^{-1}&1-(2+s)^{-1}
\end{pmatrix}.
\]
At s=0 the ambiguity persists. At s=1,
\[
\Lambda_{\rm series}(1)=
\begin{pmatrix}2/3&-1/3\\-1/3&2/3\end{pmatrix},
\]
while the frequency-independent edge remains at its DC matrix. A separately reserved dynamic boundary measurement of the off-diagonal admittance -1/3 +/- 1/100 therefore selects the series model over the direct edge **within this two-model prior**. The capacitor and its dynamic measurement must be independently justified, not fitted after seeing the result. All calculations and 16 hostile tests use exact Fractions.

A related real inverse-boundary precedent: Nachman, Annals of Mathematics 143 (1996), proves conditional full boundary uniqueness for 2D scalar conductivity; anisotropic coefficients retain a boundary-fixing-diffeomorphism equivalence. https://annals.math.princeton.edu/articles/13206 . This does NOT claim that arbitrary SUCC geometries inherit such a theorem.

## 4. Fine structure alpha and Euler-Mascheroni gamma: different epistemic roles

**Alpha:** The physical fine-structure constant is an excellent *candidate measured boundary calibration* only when one SUCC realization has **independently determined a dimensionless physical observable** whose predicted value depends on its branch and whose scale (e.g. low-energy) is specified. NIST's current published CODATA 2022 recommendation gives alpha inverse 137.035999177(21). Source: https://physics.nist.gov/cuu/pdf/JPCRD2022CODATA.pdf . SUCC currently predicts **no alpha value**; fitting it as a freely chosen parameter is not independent evidence for that realization. The familiar exact identity alpha = Z0/(2 R_K) also does not by itself provide two independent empirical measurements in the present SI because derived constants share sources and definitions.

**Gamma:** The Euler-Mascheroni constant gamma is fixed by its **mathematical definition** as lim(H_N-log N). We can literally compute it from arithmetic, but that calculation is not by itself an *independent empirical observation that physical spacetime realizes one model*. Gamma can become a reality anchor only if a specified physical observable is independently measured and a candidate model has predicted its value to equal gamma without inserting gamma by construction. Different models may also predict different constants, all mathematically admissible before the experiment.

**Correct use of either:** construct distinguishable candidate observable values and their physical source maps first; then measure independently and use the result to choose a surviving equivalence class. Do not require alpha or gamma to drop out of common axioms as a universal fixed number.

## 5. Boundary-pinning theorem agenda for SUCC

Build a genuine source-indexed functor Lambda from admissible SUCC arithmetic, analytic, quantum and geometric realizations to physical boundary-response objects, with actual glue/intertwining laws. Calibrate the functor against independent source experiments. Find a jointly separating family of boundary probes F_j on the surviving model class, then prove that observations select one gauge equivalence class or provide an explicit indistinguishable countermodel.

**Independent controls:** source-faithful versus fake prime input, postfit versus prior predictions, gauge-equivalent versus nonisomorphic graph interiors, whole DC DtN vs held-out dynamic DtN, model error vs measurement error, and a source-observer alias. No source-metadata string authenticates a physical instrument, and a synthetic measurement never establishes physical reality.

### Claim ledger

- ABR-01: classical finite Schur/DtN formula and conditional additive interface gluing — PAPER PROVED/EXACT.
- ABR-02: one direct resistor vs two series resistors share the entire static boundary map — EXACT FINITE PROVED, topology uniqueness REFUTED.
- ABR-03: an independent dynamic RC interface measurement can discriminate those static-equivalent candidates — EXACT FINITE PROVED, not actually measured.
- ABR-04: finite model fiber selection via certified intervals, gauge quotient and prediction separation — CLASSICAL CONDITIONAL.
- ABR-05: compact Hausdorff source plus jointly separating continuous response yields stable inverse-limit observer selection — CLASSICAL CONDITIONAL.
- ABR-N1: any measured scalar forces one underlying geometry — REFUTED by exact nonisomorphic static-equivalent models.
- ABR-N2: free-parameter postfit counts as a new independent physical prediction — REFUTED epistemic inference.
- ABR-06: SUCC predicts physical alpha or a gamma-anchored measured observable, an Einstein geometry or signed completed Weil positivity — UNVERIFIED.

**Executable artifacts:** `observational_succ/boundary_realization_selection.py`, `tests/test_boundary_realization_selection.py`, `scripts/boundary_realization_probe.py`, frozen source-Git-blob receipt. No original source archival files touched.

**Verdict-changing next probe:** construct two genuinely SUCC-compatible source realizations with distinct, predeclared dimensionless **physical** boundary predictions. Specify a physically feasible independent instrument, tolerance, and a second held-out response; demand exact glue/naturality and source-map passes. If boundary predictions coincide, classify equivalence rather than inventing uniqueness.
