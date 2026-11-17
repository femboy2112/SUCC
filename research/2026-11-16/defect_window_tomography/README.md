# Defect-Window Tomography: when incompatible shadows encode a hidden carrier

**Operation:** Principia Observatoris / source-faithful observer reconstruction  
**Date:** 2026-11-16  
**Author's insight:** Leah — two apparently incompatible models may be projections of one larger structure; the signed, window-relative defect may encode the structure neither projection sees.  
**Scope:** elementary finite-dimensional linear algebra; prospective nonlinear/source-specific extension.  
**Research status:** DWT-01 and DWT-02 are paper-proved classical/local deductions; exact countermodels DWT-03–05 are testable finite examples; inverse source authentication and the π bridge are **CONJECTURED/UNVERIFIED**. No claim of academic priority.



**2026-11-16 moving-frame unattainability:** [A co-moving original-BBP observer and a source-rational relative-speed gate for R0](MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md) proves exact source/observer transport, (e(-U_n)z_n=e(T_n)\to1) without finite equality, and the objective circle's nonstationarity from π irrationality. It distinguishes a finite radix-16 horizon/Haar information cost from literal thermodynamic temperature and from the deterministic π orbit. Its 15th-mode step-speed has rigorous original-source rational lower certificates on B=16,32,64,128,256; [exact 11-test and high-precision validation](MOVING_FRAME_VALIDATION.md) are finite only. A uniform all-late-shell speed bound would imply R0 but remains **OPEN**. The adaptive Gamma defect transports the same motion energy without independent source evidence.

**2026-11-16 source-shadow interferometry:** [Exact rational BBP hidden-fiber phase certificates and the weighted pair-mass R0 gate](SOURCE_SHADOW_INTERFEROMETRY.md) derives the three-observer anchored-variance decomposition, source-tail lower bounds using only the original zero-seeded four-pole recurrence, and strictly certified finite carry-mod-4/clock-mod-4 thresholds (>3/5) on shells B=32,64,128,256. The [matching exact 13-test regression](../../../tests/test_shadow_interferometry.py) and [high-precision independent representation audit](SOURCE_SHADOW_INTERFEROMETRY_VALIDATION.md) preserve all finite evidence. Singleton, phase-refinement, wrong-seed, fixed-nonunit and sparse-irrational controls prevent claiming any universal observer lower bound, R0 or pi normality.

**2026-11-16 adaptive Gamma ice-climb:** [A→B→C microscopic Gamma transport and the R0 boundary](ADAPTIVE_GAMMA_ICE_CLIMB.md) constructs a forward-only scale-renormalized Gamma window with a stable seed, exact signed nonlinear compression defect, rigorous |c(π/16)|>1/5 decoder margin and source-prefix O(n^-2) calibration. [Exact tests and receipts](ADAPTIVE_GAMMA_VALIDATION.md) include a locked rational and sparse irrational nonnormal source that defeat any inference from path coherence alone to R0. No original source or main state is changed.

**2026-11-16 Gamma-dilation continuation:** [Gamma Dilation Bridge — A Causal Analytic Seed from a Boundary Zero](GAMMA_DILATION_ANALYTIC_SEED.md) identifies the separate Fourier character, radix generator and Gamma/Mellin weight; derives a forward-only conditioned-Gamma endpoint identity, a source-typed transported jet, exact mixed-term compensation, shape-two transport and an explicit inverse-resolution barrier. This is a conditional added observer; it does not promote the original BBP R0 or π normality.

**2026-11-16 analytic-seed continuation:** [Transported Germs and Observer Differentials — the A → B → C Coherence Contract](TRANSPORTED_GERMS_AND_JETS.md) gives an exact moving-chart differential/Duhamel identity, a first-jet continuation law for genuine-prime compensation, an independently checkable prime-inventory collision, and the BBP real-lift derivative that separates otherwise identical integer-time circle observations. Arbitrary analytic functions require full germs or additional governing equations; monodromy/path history stays explicit.

**2026-11-16 extension:** [Contextual Zero, the Third Observer, and Boundary Defect Bookkeeping](CONTEXTUAL_ZERO_THIRD_OBSERVER.md) adds the typed zero-fiber equivalence, active-probe defect decomposition, exact compensating-reservoir model, and adversarial resource/entropy controls (ZTO-01–08). This is an additive research interface, not a physical vacuum or arithmetic normality theorem.

## 1. Steelman: incompatibility is not a source verdict

An observed incompatibility can mean at least three different things:

1. **Model failure:** an assumed effective dynamics genuinely predicts the wrong observed response.
2. **Projection failure:** each effective model forgets latent directions needed to predict its own future; their signed residuals may become coherent once windows are jointly transported.
3. **Underdetermination:** several different source mechanisms produce the same accessible shadows *and the same recorded defects*. Even perfect internal coherence does not select an actual source.

The operative question is not whether a defect is nonzero but whether its *oriented dependence on source states, interventions, history and chart changes* predicts observations that an alternative explanation cannot.

A window is a declared readout, not an arbitrary metaphor. A measurable discrepancy only exists after specifying a common source, calibration, temporal orientation, transport to comparable codomains and a prediction target. Without those, a putative cross-window difference is not a typed number.

**Thesis (hypothesis):** In selected source-constrained families, the structure of signed window defects can identify latent couplings or missing coordinates, even when local models fail to close. This is an inverse problem, not an automatic consequence of measuring nonzero residuals.

## 2. Typed linear problem

Fix a field \(\mathbb F\) (use \(\mathbb R\) or \(\mathbb Q\) in the examples), a vector space \(V\), and source action \(K:V\to V\). For \(m\) observers choose

\[
 P_i:V\to W_i,\qquad B_i:W_i\to W_i,\qquad
 D_i=P_iK-B_iP_i.
\]

Write \(W=\bigoplus_i W_i\), \(P=(P_1,\ldots,P_m):V\to W\), \(B=\bigoplus_iB_i\) and \(D=PK-BP\).
The \(B_i\) are provisional autonomous local dynamics, *not* assumptions about independence in the source. A joint effective dynamics \(C\) may have off-diagonal blocks.

The raw signed defect \(D\), the norms \(\|D\|\), the observable kernel \(N=\ker P\), and whether the source is correctly authenticated are separate diagnostics. Numerical norms require declared and transported units. Replacing \(D\) with \(|D|\) generally destroys orientation information.

### DWT-01: joint correction / descent lemma — PROVED PAPER (classical)

There is a unique linear \(E:\operatorname{im}P\to W\) satisfying

\[
  D=EP
\]

if and only if \(D|_{\ker P}=0\). Because \(D=PK-BP\), this is equivalent to

\[
 \boxed{K(\ker P)\subseteq\ker P.}
\]

Under these conditions \(C:\operatorname{im}P\to\operatorname{im}P\) defined by \(C(Pv)=PKv\) is well-defined, linear, unique on \(\operatorname{im}P\), and satisfies \(CP=PK\). Moreover \(E=C-B|_{\operatorname{im}P}\), viewing both as maps into \(W\). If \(P\) is onto all of \(W\), then \(C\) is uniquely defined on \(W\). If \(P\) is not onto, the theorem makes no assertion about a unique extension of \(C\) outside \(\operatorname{im}P\).

**Proof.** If \(D=EP\), every \(v\in\ker P\) has \(Dv=0\). Conversely, if \(D\) kills \(\ker P\), define \(E(Pv)=Dv\). Any two representatives differ by an element of \(\ker P\), so this is well-defined and unique. On \(\ker P\), \(Dv=PKv-BPv=PKv\); hence \(D|_{\ker P}=0\) iff \(K\ker P\subseteq\ker P\). The same representative argument defines \(C(Pv)=PKv\) and gives the stated identity. \(\square\)

**Crucial negative interpretation:** failure of this criterion means no *autonomous dynamics on the current joint report* exists. It does **not** mean that no common source \(K\) exists: one has already been specified. A nonzero defect can be evidence of a lost source direction.

This is the direct multi-window specialization of [Principia CG-02](../../../docs/principia_observatoris/02_causality_geometry.md), not a claimed novel theorem. Its time-dependent, signed generalization belongs to [CG-05/06](../../../docs/principia_observatoris/02_causality_geometry.md) and [Main XXVI Gamma transport](../../../docs/MAIN_XXVI_OBSERVER_TRANSPORT.md).

## 3. Crucible: an exact latent coordinate inside the signed defect

Take \(V=\mathbb Q^3\) with state \(z=(x,y,h)^T\). The two shadows report \(x\) and \(y\), while \(h\) is unobserved. Set

\[
 P=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix},
 \qquad B=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad K_1=\begin{pmatrix}0&1&1\\-1&0&0\\0&0&1\end{pmatrix}.
\]

The true source law is \(x'=y+h,\ y'=-x,\ h'=h\). The apparent two-window rotation predicts \((y,-x)\). Its **signed**, state-dependent discrepancy is

\[
 \boxed{D_1=PK_1-BP=
   \begin{pmatrix}0&0&1\\0&0&0\end{pmatrix},\qquad
   D_1z=(h,0)^T.}
\]

- Each scalar shadow is non-autonomous. Even the combined present report \((x,y)\) is non-autonomous, because the hidden direction \((0,0,1)\) escapes into the next visible state.
- The first component of the defect *is* the latent coordinate \(h\), under the stated source family and signed calibration: \(h=x'-y\).
- Thus the mismatch can reconstruct a missing coordinate after a one-step observation, even though it obstructs prediction using the present report alone.
- If the source model is unknown, \(x'-y\) is only a residual. Calling it a persistent physical variable \(h\) requires the source-law and future-prediction checks below.

**DWT-02 (dynamic observability) — CLASSICAL / PROVED PAPER.** For any fixed *known* finite-dimensional \(K,P\), define

\[
 \mathcal O_L=
 \begin{pmatrix}P\\PK\\\vdots\\PK^L\end{pmatrix}.
\]

Two initial states have identical reports through time \(L\) exactly when their difference lies in \(\ker\mathcal O_L\). Consequently all initial coordinates are uniquely reconstructed from that finite history iff \(\operatorname{rank}\mathcal O_L=\dim V\). Proof: the recorded transcript is \(\mathcal O_Lz\), and linear injectivity is equivalently full column rank. For \(K_1,P\) above, \(\mathcal O_1\) has rank 3, although \(P\) has rank 2.

This **does not identify unknown \(K\)**, recover unrecorded history, or validate a proposed source family. It is the classical observability-matrix criterion in exact finite linear systems. The surviving state ambiguity is \(\ker\mathcal O_L\), a useful toolkit-relative \(\phi\) object; adequacy of the purported physical/arithmetic source is the separate \(\sigma\) question.

## 4. The hostile twin: the same entire one-step defect, a different source

Change *only* the hidden evolution:

\[
 K_2=\begin{pmatrix}0&1&1\\-1&0&0\\0&0&2\end{pmatrix}.
\]

Then **as complete linear operators**,

\[
 PK_2=PK_1,\qquad PK_2-BP=PK_1-BP=D_1.
\]

Thus even exact access to both raw one-step shadows and their full signed defect does not choose \(K_1\) over \(K_2\).

For the fixed initial state \(z_0=(1,2,3)^T\), both sources report

\[
 (x_0,y_0)=(1,2),\quad (x_1,y_1)=(5,-1),\quad D(z_0)=(3,0).
\]

But their **predeclared second-step forecasts** separate:

| Source hypothesis | Hidden value after first step | Visible report at step 2 |
|---|---:|---|
| \(K_1\): persistent \(h\) | 3 | \((2,-5)\) |
| \(K_2\): doubling \(h\) | 6 | \((5,-5)\) |

Alternatively, a genuinely new third instrument \(P_C=(1,2,1)\), with its units and source connection calibrated independently, predicts at step 1 the scalar \(6\) under \(K_1\), versus \(9\) under \(K_2\). The superficially new \(P_C^{\rm redundant}=(1,2,0)\) yields \(3\) under **both** hypotheses at step 1: merely renaming a linear combination of existing windows does not open a new direction.

**DWT-03 — REFUTED (with counterexample):** 'One-step shadow defects uniquely determine the latent source dynamics.' Receipt: the exact \(K_1,K_2\) pair above. The minimal repair is a declared source family plus a fresh, separating longer-horizon or independent-window probe. The pair is a toy linear source test, not an empirical demonstration.

## 5. Other required hostile controls

**DWT-04 — zero defect does not recover the source.** Let

\[
 K_0=\begin{pmatrix}0&1&0\\-1&0&0\\0&0&2\end{pmatrix}.
\]

Then \(PK_0=BP\), so the visible model is perfectly autonomous, while the hidden third coordinate evolves as \(2^nh_0\) and remains invisible to every \(PK_0^n\). A zero defect certifies observed descent, not full physical-source identification. Two states differing only in \(h_0\) have identical visible transcripts for *every* finite horizon.

**DWT-05 — signed and gauge controls.** In the \(K_1\) model the two initial states \((1,2,+3)\) and \((1,2,-3)\) have defects \((+3,0)\) and \((-3,0)\). Taking absolute values erases this necessary sign. Under invertible source/observer charts \(S,T\), with \(K'=SKS^{-1},P'=TPS^{-1},B'=TBT^{-1}\),

\[
 D'=TD S^{-1}.
\]

For example \(S=\operatorname{diag}(1,1,-1)\), \(T=\operatorname{diag}(2,1)\) yields the displayed defect coefficient \(-2\) instead of \(+1\). Its rank and vanishing properties remain invariant; numerical coefficients need transported units and orientation. A claimed *phase* requires a separately declared operational phase transport: no phasor is inferred just because a complex coordinate could be attached.

**Redundant latent extension.** Append a fourth, never-observed independent coordinate to either carrier. It changes the underlying source dimension without changing any \(P K^n\) on the observed block. Hence even arbitrary-long exact visible transcripts need not recover a unique unconstrained latent ontology. Identifiability is always relative to the source class and available probes.

**Source-compatibility firewall.** Two separately fitted effective laws are not made *physically* compatible simply by placing them in a formal direct-sum carrier. The proposed parent must respect authenticated source maps, joint chronology, allowed interventions, provenance and new predictions. Nor does a nonzero overlap difference certify a common parent. If overlap maps/units are unspecified, the comparison is an **access gap**, not a numerical obstruction. If local charts have lawful nontrivial transition functions, their nonidentity is not itself a failed gluing: distinguish transition data from an actual violated cocycle or descent condition.

## 6. What the defects can and cannot certify

| Object | What is established | What remains unpaid |
|---|---|---|
| Local operator \(D_i\) | Signed deviation from a specified \(B_i\) relative to \(K,P_i\) | Which model/source premise produced it |
| Joint \(D=PK-BP\) | Failure or success of closure on present joint report via DWT-01 | Unique reconstruction of \(K\) |
| \(\mathcal O_L\) | Initial state distinguishability when \(K\) is known | Source/model identification when \(K\) is unknown |
| New transported window / delayed response | Can discriminate predeclared rival sources | Validity of instrument, calibration and actual carrier |
| Global gluing/holonomy | May encode topology under lawful transition/cocycle contracts | A theorem identifying it with this defect or an arithmetic phase |

The useful information is **not** the defect's magnitude by itself. It is the *source-typed signed response across contexts, intervention directions, window overlaps, temporal lags and calibrated transports*. Absence of a possible discriminator is reported as contextual saturation/darkness, not proof that the parent is true.

## 7. Proposed Defect-Window Tomography protocol (CONJECTURED)

1. **Authenticate the source and two windows.** State carrier class, observation maps, clocks, calibrations, sign/orientation, admissible interventions, state priors and any nonlinear operations in their actual order.
2. **Compute raw signed defects before compression.** Preserve \(D_i\), their kernel restrictions, chart-transported versions and uncertainty/error bounds; also preserve absolute/norm summaries as different data, not replacements.
3. **Enumerate source-compatible rivals.** Include (a) shared latent parent, (b) incompatible local fits, (c) same-window counterfeit or extra hidden dimension, and (d) wrong-gauge/source mutation. Document whether alternatives are distinguishable within the available toolkit.
4. **Freeze a prospective third-window or time-lag prediction.** Choose a probe splitting the largest live equivalence class: in §4, step 2 or the \((1,2,1)\) readout, *not* the redundant \((1,2,0)\) readout. Record predicted outcomes, numerical/analytic budgets and pass/fail/ambiguous branches **before** collecting it.
5. **Use mutation, null and holdout controls.** Confirm the test can fail for the hidden-drift mutant and for sign-erasure; check that added observability actually increases rank. Do not validate a fit with its training windows.
6. **Certify scoped dominance.** Prefer the parent only if it survives new probes while rival predictions fail, without introducing unfalsifiable variables or worse source contradictions. Where rivals remain observationally identical, state the missing lamp.

If \(K,P\) are matrices and exact source states are available, this protocol has a finite executable component. General sheaf/gluing analogies require explicit overlap restrictions and cocycle laws; neither a cohomology class nor a probabilistic posterior exists without its own hypotheses.

## 8. SUCC interface: why the π arithmetic debt is untouched

Main XXVI's actual source remains

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
 \quad U_0=0,\quad U_n=16U_{n-1}+r(n),
 \quad U_n+T_n=16^n\pi/16.
\]

Its rational state, real-circle phase, literal integer carry, 2-adic address and source-conditioned Gamma window are different typed observers; one must **construct and certify actual transports** before interpreting their mismatch as a common-source diagnostic. [Main XXVI Atlas](../../../docs/MAIN_XXVI_CONSTRUCTIVE_INTERFERENCE_ATLAS.md) preserves exactly these interfaces. The [carry–Gamma decoder](../../../docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md) is a calibrated forward/equivalent instrument, **not** source selection. The [observer transport bound](../../../docs/MAIN_XXVI_OBSERVER_TRANSPORT.md) controls forward errors and explicitly lacks a converse.

An appropriate *future* attack would construct a source-faithful, zero-seed-sensitive defect observable on the exact growing-CRT/carry history, then predeclare a new signed prediction that changes under the coherent wrong seed, finite rational shadow seeds and forgotten winding. A successful holdout might corroborate the mechanism; to pay R0 it would still need a **uniform all-late-shell** source-derived estimate. No identity here supplies one.

The smallest open rung is unchanged:

\[
 \exists\eta>0,\ B_0\ \forall B\ge B_0:\qquad
 \operatorname{Re}\frac1B\sum_{n=B}^{2B-1} e(16^n\pi/16)\le1-\eta.
\]

No claim about π normality, RH, physical hidden channels or quantum speedup is made.

## 9. Claim ledger, source map and validation

| ID | Verdict / authority | Exact boundary / falsifier |
|---|---|---|
| DWT-01 | **PROVED PAPER / CLASSICAL** | Joint linear factorization iff \(D|_{\ker P}=0\); applies only to the declared \(K,P,B\). |
| DWT-02 | **PROVED PAPER / CLASSICAL** | Observability-matrix rank criterion when \(K\) is known; no unknown-source identification. |
| DWT-03 | **REFUTED with exact counterexample** | Same full one-step defects do **not** uniquely select \(K\): explicit \(K_1,K_2\). |
| DWT-04 | **PROVED EXACT MODEL** | Exact zero defect can coexist with permanently invisible hidden state. |
| DWT-05 | **PROVED EXACT MODEL** | Signed defect resolves the \(\pm h\) pair; gauge-transformed coefficient changes while rank persists. |
| DWT-06 | **CONJECTURED / UNVERIFIED** | Source-constrained multiscale defect tomography can identify nontrivial parent structure outside the toy family. Falsifier: held-out source-intervention or window disagreement. |
| DWT-07 | **UNVERIFIED** | A source-selected defect invariant can yield an eventual π carry/Weyl estimate. Needs authenticated arithmetic transport and an all-shell proof. |

**Provenance / dependencies:** author's 2026-11-16 observation; Principia [CG-02/03/05/06](../../../docs/principia_observatoris/02_causality_geometry.md), [D2 signed defects](../../2026-11-14/tenacious_d/DEFECT_AND_GAUGE.md), [Main XXVI observer transport](../../../docs/MAIN_XXVI_OBSERVER_TRANSPORT.md), [Main XXVI source/phase obstruction](../../../docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md), and [method](../../../docs/METHOD.md). These are overlapping provenance families, not independent physical verification. The joint-factorization and observability results are elementary/classical mathematics reused here; no academic novelty priority is asserted.

**Executable finite controls:** run

~~~sh
python -m unittest discover -s tests -p 'test_defect_window_tomography.py' -v
~~~

The new test module uses only Python's standard library and exact rational arithmetic. It checks DWT-03 rival equality, rank growth, delayed and third-window separation, sign/gauge mutations, and the zero-defect countermodel. Such finite checks do not prove general claims beyond the accompanying derivations. No existing SUCC source file, frozen import, claimed theorem, or main-branch status is changed by this research note.

**Next verdict-changing probe:** construct a *source-authenticated* third window or delayed action for a nontrivial SUCC carrier, pre-register rival signed predictions, then test a withheld source regime. If no lawful map into a common carrier can be written, classify the failure as a pathway/access gap rather than asserting incompatibility or latent unity.
