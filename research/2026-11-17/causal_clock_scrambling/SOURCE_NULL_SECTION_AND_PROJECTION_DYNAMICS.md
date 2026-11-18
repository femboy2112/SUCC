# The Source-Null Section: Classical Carrier, Restricted Observation, and the Null-Information Seed

**SUCC / Principia Observatoris / original zero-seeded BBP source**  
**Date:** 2026-11-17  
**Originating axiom (Leah, clarified):** reality exists in full fidelity regardless of incomplete probing; its mathematical carrier is one actual history, while subjective readouts are generally non-injective shadows of it. SUCC is being constructed as a **classical source/observer formalism for nonclassical-looking dynamics arising under restricted projection and differently transported bases**. Most importantly, the **seed invariant is the null-information seed**: the distinguished BBP source history injects no *additional homogeneous initial-state input* beyond the original forcing.

**Claims:** NS-01–04 are algebraically exact under stated hypotheses and classical source-relative consequences; NS-05 is a proved projection/memory possibility, not a claim about every BBP readout; NS-06 is a proved logical limitation; NS-07 is an OPEN original-source number-theoretic challenge. No quantum-mechanical contextuality, Bell violation, relativity, physical vacuum temperature, or π base-16 normality theorem is asserted. The original source, zero seed, integer winding, positive tail and frozen provenance are not modified.

## 1. Formalize the intended "null information" without treating zero as ignorance

The **actual source** is the literal original signed four-pole BBP recurrence:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\qquad U_n=16U_{n-1}+r(n).
\tag{NS1}
\]

Write its source-generated particular solution
\[
F_0=0,\qquad
F_n=\sum_{j=1}^n16^{n-j}r(j).
\]

The space of **all** solutions to the same forced recursion is an **affine torsor** for the homogeneous solution space:
\[
\boxed{U_n(s)=F_n+16^ns,\qquad s\in\mathbb R.}\tag{NS2}
\]

**NS-01 (EXACT source-null section and conserved seed invariant):**
\[
\boxed{\mathcal I_n(U)=16^{-n}\big(U_n-F_n\big)=U_0=s
\quad\forall n\ge0.}\tag{NS3}
\]
Proof: \(U_{n+1}-F_{n+1}=16(U_n-F_n)\). Divide by \(16^{n+1}\), or use NS2. Hence the distinguished *source-null section* is
\[
\boxed{\sigma_0(r)=(F_0,F_1,\ldots),\qquad\mathcal I_n(\sigma_0)=0.}\tag{NS4}
\]

**Interpretation precisely intended:** "null-information seed" means **no extra initial homogeneous degree has been selected or injected, relative to this declared source and reference section**. It does not mean that the total mathematical object is information-free: the four poles, their signed order, the radix, the time origin and the fact that the null section was selected are source information. It does not mean the value zero is an uncertain probability distribution, nor that no mathematical data specify the source.

This is the exact distinction between **a null-input dynamical program** and **an unknown initial state**. The program's source and chosen input together specify a unique real history; a restricted observer may still fail to recover it.

The initial value alone does not enforce a property of the resulting completed orbit. Any other source law \(r'\) also has a unique null section; \(r'\equiv0\) with \(U_0=0\) is perfectly locked. Therefore the source-null property **cannot by itself** force π digit normality. A theorem using the *literal* signed original \(r(n)\) might, but still owes the arithmetic inequality.

## 2. Coordinate-covariant "nothing added"

A crucial calibration: "numerically equals zero" is **not** chart-independent. Let \(b_n\in\mathbb R\) be a declared change of source/observer chart:
\[
U'_n=U_n+b_n,\quad
r'(n+1)=r(n+1)+b_{n+1}-16b_n,\quad
s'=s+b_0.
\tag{NS5}
\]
The transformed distinguished reference section is
\[
F'_n=F_n+b_n,\qquad F'_0=b_0,
\]
which is the trajectory of the transformed source with the **transported initial reference** \(s'_{\rm ref}=b_0\).

**NS-02 (EXACT gauge-covariant null-excess invariant):**
\[
\boxed{
\mathcal I'_n-s'_{\rm ref}
=16^{-n}\!\left[U'_n-F'_{\mathrm{zero-source},n}\right]-b_0
=s.
}\tag{NS6}
\]
Here \(F'_{\mathrm{zero-source},n}\) denotes the new forcing's *zero-numerical-seed* solution; since \(F'_n=F'_{\mathrm{zero-source},n}+16^n b_0\), the formula is equivalent to
\[
\boxed{U'_n-(F_n+b_n)=16^ns.}\tag{NS7}
\]
Proof: substitute NS2 and NS5, then cancel the transported chart offset. The null-excess condition \(s=0\) is **invariant when the source passport and its origin are transported**, not when one mistakes the new coordinate zero for the old origin.

This realizes the user's concern: an observer can call a source component "nonzero" merely because it changed its chart; source selection must be stated in the common transported basis before declaring an injected information payload.

## 3. Full-fidelity singleton carrier and epistemic fibers

Fix the single actual history \(\omega_\ast=\sigma_0(r)\) (together with its admitted completion \(U_n+T_n=16^n\pi/16\)) and admissible observers \(P_i\). Their actual reports are \(P_i(\omega_\ast)\).

A finite observer's **compatible-source fiber** \(P_i^{-1}(P_i(\omega_\ast))\) may contain many *counterfactual histories*. This does not imply multiple actual histories, and it does not mean an observer may combine incompatible reports without a transport. The arithmetic source identity is an additional admissibility constraint.

**NS-03 (EXACT phase-null example):** for original circle phases \(P_n(U)=e^{2\pi i U_n}\), the affine seed \(s=a/16^m\) satisfies
\[
\boxed{P_n(U(s))=P_n(U(0))\quad\forall n\ge m,}\tag{NS8}
\]
although \(\mathcal I_n(U(s))=s\ne0\). This observer cannot see the injected seed on its later circle window; an exact real-state/source-passport observer can. Thus **source nullity and observational nullity are different**.

The family of later-circle aliases and the separately proved dense-null group/nowhere-continuity result remain as in [Seed-Resonance Interferometry](SEED_RESONANCE_AND_NULL_SUPPORT.md). The stronger fractional-time Gamma microscope has different source access and can separate some of those aliases, but no new accessibility is inferred merely by naming it.

## 4. How a classical carrier generates nonclassical-looking projected dynamics

Take an exact deterministic source carrier \(X\) with transition \(A\) and a non-injective observer \(P:X\to Y\). An observed transition \(B:Y\to Y\) exists as a closed law with
\[
P\circ A=B\circ P
\]
if and only if any two full states with identical observation produce the same next observation. In a linear model, the condition is \(A(\ker P)\subseteq\ker P\), exactly SUCC's prior CG-02 quotient descent criterion.

**NS-04 (CLASSICAL / PROVED PAPER; hidden-response obstruction):** if there exist \(x,x'\) with \(P(x)=P(x')\) but \(P(Ax)\ne P(Ax')\), no single-valued closed evolution on \(Y\) reproduces both. Observers restricted to \(Y\) can need memory, additional state, or conditional distributions to model what is an ordinary deterministic transition on \(X\).

**Exact tiny calibration:** let \(X=\mathbb Q^2\), \(A(a,h)=(h,a)\), and \(P(a,h)=a\). Both \(x=(0,1)\), \(x'=(0,2)\) report present observation 0, but next observations are 1 and 2. Their full states are unambiguous, classical, and evolve deterministically. A source-conditioned observer may recover hidden history by a suitably permitted lag probe.

This is a rigorous way classical dynamics can **look** non-Markovian, context-sensitive, noisy or nonlocal in a reduced coordinate description. It does not establish actual quantum contextuality, a violation of Bell inequalities, quantum amplitudes or relativistic spacetime geometry. The classical Mori–Zwanzig formalism is a direct antecedent: projection of deterministic microscale dynamics yields exact reduced memory and noise terms; see Parish–Duraisamy in *Coarse-Graining Turbulence* (Cambridge 2025) and the Mori–Zwanzig teaching derivation at IMPA. Kochen–Specker, under its quantum measurement assumptions, rules out simplistic assignments of universally pre-existing noncontextual values; a common real history alone does not bypass that theorem.

**Specificity firewall:** BBP's full completed **circle** \(z_n=e(16^n\pi/16)\) obeys the closed radix law \(z_{n+1}=z_n^{16}\). BBP's rational phase \(e(U_n)\) also has a closed **time-dependent** update when the source \(r(n+1)\) and clock are retained. We are NOT claiming that these particular complete phase readouts are non-Markovian. The projection/memory phenomenon applies to coarser or source-blind observer channels that actually fail the descent test.

## 5. Null seed determines the true orbit, but not its asymptotic distribution

With the classical BBP completion \(x=\pi/16\), the selected null section gives the single completed phase orbit. The prior endpoint norm and R0 criterion are exact:
\[
\boxed{
R_B(0)=\frac1B\sum_{k=1}^B
\left\|\frac{U_{2B}(0)}{16^k}\right\|_{\mathbb T}^2,\qquad
\mathrm{R0}\iff\liminf_{B\to\infty}R_B(0)>0.
}\tag{NS9}
\]

**NS-05 (PROVED logical firewall):** NS3 identifies exactly which trajectory belongs to the null section. It is not a coercivity statement. Every solution family for a different forcing can have the same exact null-injection invariant, including the perfectly stationary \(r\equiv0\) example. Likewise *an arbitrary number of seed derivatives* of the affine source dynamics reveals only its universal homogeneous propagator:
\[
\boxed{\partial_s U_n(s)=16^n,\qquad\partial_s^kU_n(s)=0\quad(k\ge2).}\tag{NS10}
\]
For the nonlinear phase, \(\partial_s^k e(U_n(s))=(2\pi i16^n)^k e(U_n(s))\). These derivatives preserve the current phase but do not automatically provide a new **source-specific signed shell bound**. A differentiated zero-looking probe can expose hidden directions without deciding the locked-versus-escaping asymptotic predicate.

**NS-06 (OPEN and source-restricted):** prove that the *literal* signed forcing, null initial section, authenticated integer winding and original source history imply a noncollapsing average of the backward BBP torus distances:
\[
\boxed{
\exists\delta>0,B_0\ \forall B\ge B_0:\quad
\frac1B\sum_{k=1}^B\left\|\frac{U_{2B}(0)}{16^k}\right\|_{\mathbb T}^2\ge\delta.
}\tag{NS11}
\]
This would yield R0, not automatically full π normality. The preceding [Proof-Direction Oracle](PROOF_DIRECTION_ORACLE.md) supplies a verifier for finite source-authenticated backward witnesses and the exact density criterion; its **uniform source-derived witness generator** is the missing mathematical construction.

The next probe should require a genuine *source-selected positive density* of separated terminal directions, rather than another direct computation of invariant I_n=0. The proposed objective/subjective oracle can select a representation, but its proof certificate must not assume NS11 or borrow a nonzero seed's endpoint.

## 6. Steelman, crucible, verdict / claim ledger

| ID | Status | Certified content and remaining debt |
|---|---|---|
| NS-01 | **PROVED PAPER / elementary classical** | \(\mathcal I_n=s\), canonical null section for the authenticated forced recurrence |
| NS-02 | **PROVED PAPER / coordinate transport** | No extra homogeneous seed is covariant when source reference and chart are transported |
| NS-03 | **PROVED PAPER / observer alias** | Source-nonnull dyadic seeds can become observationally null at all later integer phases |
| NS-04 | **CLASSICAL / PROVED PAPER** | Non-invariant observation fibers prevent a closed reduced evolution; explicit classical hidden-memory control |
| NS-05 | **PROVED logical limitation** | Null seed relative to forcing is not an all-shell dynamical coercivity theorem; affine jet tower alone is not new arithmetic |
| NS-06 | **UNVERIFIED / OPEN** | Authentic four-pole zero-section forces positive terminal norm on every late shell |

**Adversaries:** nonzero dyadic seeds that alias circle phases; \(s=-\pi/16\) coherent locked seed; the changed source \(r\equiv0\) with null seed; the sparse irrational failing R0; the per-shell winding-erasure seed; a source/gauge chart with \(b_0\ne0\); the exact time-dependent phase map which IS closed and therefore defeats the universal "all observations are non-Markovian" claim.

**Priority/physics:** "One real carrier, multiple imperfect observation maps" is an explicit model assumption; many mathematical frameworks already use that structure. Its application in the SUCC source-typing language is a research synthesis, not academic priority. A hidden classical carrier does not by itself reproduce QM's operational contextuality or Bell-nonlocal correlations, nor GR curvature/dynamics. Any claimed equivalence needs independent operator, empirical and transformation laws.

**Dependencies:** [Contextual Zero Backbone](../../../docs/CONTEXTUAL_ZERO_BACKBONE.md), [Principia knowledge/target factorization](../../../docs/principia_observatoris/03_knowledge_proof.md), [Principia causal geometry CG-02](../../../docs/principia_observatoris/02_causality_geometry.md), [Seed Resonance](SEED_RESONANCE_AND_NULL_SUPPORT.md), [Proof Direction Oracle](PROOF_DIRECTION_ORACLE.md), [Terminal BBP R0 norm](../../2026-11-16/defect_window_tomography/VIRTUAL_FIELD_FORM_METRIC.md), [Method](../../../docs/METHOD.md).

**Validation scope:** [tests/test_null_seed_source_anchor.py](../../../tests/test_null_seed_source_anchor.py) exercises exact original source, all affine seeds, transported chart/zero reference, dyadic phase alias, an r≡0 perfectly locked null-input model, a classical memory counterexample and affine derivative closure. No full root tests or Lean run implied by focused checks.
