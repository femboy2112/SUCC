# Finite observer, infinite computation, finite universal certificate

**SUCC / Principia Observatoris / BBP source and endpoint norm — 2026-11-17**

**Originating distinction (Leah):** the subjective and objective observers *constructively access the same object*. An observation-only subjective observer can never finish an infinite path by literally enumerating it, whereas an objective observer with the authenticated source structure can prove a property of the entire path without completing that enumeration.

**Status:** FOIC-01–05 are elementary/classical conditional theorems with exact proofs. FOIC-06 is a counterexample to an overstrong R0 inference. FOIC-07 is a source-specific open theorem. No new irrationality proof, π-normality theorem, physical nonlocality or universal computational impossibility is claimed.

## 1. Source object and precise meanings of “lock”

Retain the **literal original zero-seeded** four-pole BBP source:
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
The imported exact identity identifies the completed orbit with \(x=\pi/16\) and
\[
Y_n=U_n+T_n=16^nx,\quad z_n=e(Y_n),\quad e(y)=\exp(2\pi iy).
\]

**Exact recurrence/lock:** \(\exists m>n\ge0:z_m=z_n\), which under the base-16 map entails an eventually periodic orbit. **Approximate shell locking relevant to R0:** a sequence \(B_j\to\infty\) for which
\[
A_{B_j}(x)=1-\Re\left[\frac1{B_j}\sum_{n=B_j}^{2B_j-1}e(16^nx)\right]\to0.
\]
These predicates are **not equivalent**. A trajectory can avoid *every exact repeat* yet approach the zero-phase reference on arbitrarily late shells.

### FOIC-01 (CLASSICAL / PROVED PAPER): an objective finite proof of no exact repeat

If \(x\notin\mathbb Q\), then for every pair of distinct nonnegative integers \(m>n\),
\[
z_m=z_n\ \Longrightarrow\ (16^m-16^n)x\in\mathbb Z
\ \Longrightarrow\ x\in\mathbb Q,
\]
a contradiction. Therefore
\[
\boxed{\forall m>n\ge0,\quad z_m\ne z_n.}
\tag{FOIC1}
\]
For \(x=\pi/16\), this uses the **existing classical theorem that π is irrational** and the imported BBP completion. It is a finite argument about an infinite quantified family; it does **not** require enumerating all digits and cannot be attributed to the bare premise \(U_0=0\) alone. Countermodel: the zero-seeded recurrence with \(r\equiv0\) is identically locked. The full source identity is load-bearing.

## 2. Any fixed finite-resolution trace has an exactly locking rival

Fix \(x\in[0,1)\), an observation horizon \(H\in\mathbb N\) and a tolerance \(\varepsilon>0\). Choose \(m>H\) large enough that \(2\pi16^{H-m}<\varepsilon\), and put
\[
q_m=\frac{\lfloor16^m x\rfloor}{16^m}\in\mathbb Q.
\]
Then \(0\le x-q_m<16^{-m}\), so for every \(0\le n\le H\),
\[
\boxed{
|e(16^nx)-e(16^nq_m)|
\le2\pi16^n|x-q_m|
<\varepsilon.
}
\tag{FOIC2}
\]
Yet
\[
\boxed{e(16^nq_m)=1\quad\forall n\ge m.}
\tag{FOIC3}
\]

**FOIC-02 (PROVED PAPER):** a finite-resolution, finite-horizon instrument observing only these phases cannot distinguish the original irrational trajectory from *some* eventually exactly locked terminating-rational endpoint. This is a statement about **that observation toolkit and competing endpoint class**, not a counterfeit with the original four-pole forcing and literal zero seed. If it receives an authenticated source proof, the observer's toolkit has enlarged and the indistinguishability premise no longer applies.

**FOIC-03 (CLASSICAL / SOURCE-AWARE ACCESS THEOREM):** the property “never returns to a previous state” does not factor through any one finite-horizon finite-precision phase observation on the unrestricted endpoint class. The proof consists of the irrational endpoint together with the rational terminating shadow of FOIC-02. However, it *does* follow from a finite verified source-level certificate of irrationality. Thus absence of an observation-only decision procedure is not absence of a finite mathematical proof.

This is the precise form of **shared-object observer agreement**: on all overlapping readouts the subjective and objective observers agree. Their difference is a **toolkit/proof-access gap**, not contradictory facts about a shared carrier.

## 3. The crucial R0 crucible

**FOIC-04 (REFUTED inference):** “a productive infinite computation with no finite repeats must escape zero-phase locking on all late shells.”

Counterexample, already authenticated in SUCC's [adaptive Gamma hostile dossier](../../2026-11-16/defect_window_tomography/ADAPTIVE_GAMMA_ICE_CLIMB.md):
\[
x_\star=\frac3{16}+\sum_{j=1}^{\infty}16^{-4^j},\qquad B_j=2\cdot4^j.
\]
Its base-16 expansion is not eventually periodic, so \(x_\star\) is irrational and its orbit has no two equal phases, by FOIC-01. Yet the proved sparse-tail bound gives
\[
\boxed{
0\le A_{B_j}(x_\star)<\frac{32\pi}{225B_j}\longrightarrow0.
}
\tag{FOIC4}
\]
So even an objective, globally valid, finite proof of **exact no-repetition** does not prove R0. This falsifier is the barrier between the user's constructively valid finite/infinite observer intuition and an as-yet-unproved π-normality consequence.

The original zero-seeded BBP endpoint is not replaced by \(x_\star\); the countermodel kills an invalid *general implication*, not the specific arithmetic conjecture for π.

## 4. Source-compressed certificates versus raw execution

There are two distinct proof technologies:

1. **Trace-enumerating observer:** checks every accessible computational step. Any finite trace has terminating-rational shadows, and no last stage exists where mere completion of all digit computations occurs.
2. **Invariant-bearing observer:** takes the *same authenticated mathematical object* with a source-level theorem and proves its all-time property without enumerating all times. For π, irrationality gives FOIC1. The observer may be given this theorem, derive it within a richer calculus, or be barred from it by its resource/toolkit restrictions.

Nothing prevents a subjective observer from learning or constructing a finite proof once its instruments include the relevant source mathematics. The stronger claim “a subjective observer can **never** prove no exact cycle” is therefore false without an explicit restriction to observation-only enumeration.

A finite proof of an all-time property is a compact deduction, **not** a physically completed infinity of computations. A productive/coinductive stream can still be periodic; infinitude of a computation graph by itself does not entail nonperiodicity.

### FOIC-05 (exact selected-source connection)

Our established terminal BBP rational norm is
\[
\boxed{
R_B(0)=\frac1B\sum_{k=1}^{B}\left\|\frac{U_{2B}(0)}{16^k}\right\|_{\mathbb T}^{2}.
}
\]
The existing [endpoint coercivity audit](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md) proves, with source-paid tail error \(\rho_B\to0\),
\[
8R_B-\rho_B\le A_B(\pi/16)\le2\pi^2R_B+\rho_B.
\]
Hence
\[
\boxed{\mathrm{R0\ for\ }\pi\iff\liminf_{B\to\infty}R_B(0)>0.}
\tag{FOIC5}
\]
This is the open **quantitative** invariant: a finite proof that the original source forces a uniform eventual lower shell energy. It is stronger than FOIC1 and is not produced by irrationality, a finite observation, a high-order seed resonance, or bare source-zero semantics.

### FOIC-06 (OPEN source-specific challenge)

Find a source-typed, finite, globally quantified argument that the literal four poles and \(U_0=0\) prevent \(R_B(0)\) from collapsing on arbitrarily late integer shells. The previous [tail-floor intermediate](../../2026-11-16/defect_window_tomography/TERMINAL_TAIL_BASELINE.md) asks first for the weaker eventual pointwise \(R_B(0)\ge(16\,711\,680 B^5)^{-1}\). Neither premise is yet proved.

**Falsifiers:** the locked counterseed \(s=-\pi/16\); shell-dependent dyadic winding erasure; rational terminating shadows \(q_m\); the irrational sparse \(x_\star\); and the delayed-impulse versus initial-seed provenance alias. The winning proof must retain the actual source-selected numerator/winding and must not infer a density bound from mere nonperiodicity.

## Claim ledger

| Claim | Status | Scope |
|---|---|---|
| FOIC-01 | CLASSICAL / PROVED PAPER | Irrational x ⇒ no exact repeated base-16 circle state; BBP source plus π irrationality licenses the application |
| FOIC-02 | PROVED PAPER | Every finite-precision phase trace has a terminating rational shadow whose orbit eventually locks |
| FOIC-03 | CLASSICAL / PROVED PAPER | Non-repetition is not identifiable from finite observation-only traces on unrestricted endpoint class; source-level proofs can identify it |
| FOIC-04 | REFUTED | No exact repeats does **not** imply R0 (sparse irrational countermodel) |
| FOIC-05 | INHERITED PROVED EQUIVALENCE | Original zero-seed terminal rational norm recodes R0 |
| FOIC-06 | OPEN | Positive all-late-shell R0 endpoint-norm floor or weaker arithmetic improvement |

**Provenance and boundaries:** SUCC [Principia causal observer geometry](../../../docs/principia_observatoris/02_causality_geometry.md); [Contextual Zero Backbone](../../../docs/CONTEXTUAL_ZERO_BACKBONE.md); [Seed-Resonance Interferometry](SEED_RESONANCE_AND_NULL_SUPPORT.md); [original frontier](../../../docs/PI_NORMALITY_FRONTIER.md); [endpoint report](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md). All proofs here use elementary classical facts and previously authenticated SUCC arithmetic; no independent confirmation of π's identification, finite-to-infinite inference, quantum theory, or original-source normality is claimed.

**Executable checks:** [tests/test_finite_observer_infinite_certificate.py](../../../tests/test_finite_observer_infinite_certificate.py) tests exact finite shadow bounds, terminal locking, seed/source compatibility and sparse-control structure. An executable test does not prove FOIC1's universal statement or FOIC6's missing arithmetic premise.
