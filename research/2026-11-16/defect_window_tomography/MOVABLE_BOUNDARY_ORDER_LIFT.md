# Movable Observation Boundaries — Null Marginals, Higher-Order Coherence, and Source-Typed BBP Pair Probes

**Research continuation:** Principia Observatoris / SUCC Knowledge Volume / Defect-Window Tomography / Main XXVI π frontier  
**Date:** 2026-11-16  
**Author's insight (Leah):** the observation boundary can be pushed. An apparently noisy readout may have null first-order information while a probe of the **observer's coupling to that noise** reveals structured second-order information. In the proposed stacked knowledge volume, this is one upward representational step, metaphorically "one Dirac delta above" the existing observation plane.

**Authority:** MBO-01–07 are classical exact conditional models and BBP source-typed inequalities. MBO-08 is a finite exact arithmetic calibration. MBO-09 is a conditional sufficient R0 gate with **OPEN** all-late-shell premise. No quantum effect, actual physical observer, true vacuum/absolute-zero thermodynamics, RH, π normality or academic priority is established.

## 1. Steelman: zero first moment is weaker than zero source information

A mean-zero observation need not be uninformative: a conditional distribution can depend on the source even when its first moment is zero. The strongest correct steelman is therefore:

> Every **individual marginal law** available to a coarse observer is exactly the same under competing source states. Yet the **joint law of two calibrated source-linked instruments** may contain a nonzero correlation. A lawful change of the coupling parameter can move that source distinction across the observation boundary.

This is distinguishability relative to an instrument and source class. No inference from a random-looking time series to actual stochastic dynamics is licensed.

### MBO-01 — a completely explicit movable boundary (CLASSICAL/EXACT)

Let the hidden source target be a unit complex phase \(Z\in\mathbb T\), and let \(R,R'\) be independent **Haar-uniform** circle phases. Let the experimenter choose \(p\in[0,1]\) and an independent Bernoulli variable \(J_p\) with \(\Pr(J_p=1)=p\). Define

\[
A=R,\qquad B=Z(J_pR+(1-J_p)R').
\tag{MBO1}
\]

Each *individual* marginal distribution is Haar on \(\mathbb T\), independently of \(Z,p\). In particular, \(\mathbb EA=\mathbb EB=0\), and \(\mathbb E|A|^2=\mathbb E|B|^2=1\). Those last two variances are the same for genuinely independent noise and for coupled noise; **single-channel positive energy is not a source witness**.

But

\[
\boxed{\mathbb E[\overline A B\mid Z,p]=pZ,\qquad
\frac{\partial}{\partial p}\mathbb E[\overline A B\mid Z,p]=Z.}
\tag{MBO2}
\]

**Proof.** On \(J_p=1\), \(\overline AB=\overline RRZ=Z\); on \(J_p=0\), \(\mathbb E(\overline R R')=0\) by Haar orthogonality. Take the Bernoulli mixture. Independent Haar multiplication/rotation proves the full-marginal claims. \(\square\)

For \(p=0\), the entire pair \((A,B)\) is a product Haar law, independent of \(Z\): **zero source accessibility even with all pair measurements**. At \(p>0\), the pair's correlation and joint law depend on \(Z\). The observer has **pushed** the boundary by changing a *declared intervention*, not by wishing an inaccessible observation into existence.

The derivative at \(p=0\) is a **prediction of this calibrated model**; it is not data acquired by a detector permanently stuck at \(p=0\). If actual \(p\)-interventions cannot be realized, this is an access/pathway gap.

### MBO-02 — precision/resource cost and the null control (CLASSICAL/EXACT)

From \(N\) independently repeated, freshly prepared pairs \((A_j,B_j)\) at the *same fixed* source phase \(Z\) and \(p>0\), define

\[
\widehat Z_N=\frac1{Np}\sum_{j=1}^N\overline{A_j}B_j.
\]

Because each product has modulus one and mean \(pZ\),

\[
\boxed{\mathbb E\widehat Z_N=Z,\qquad
\mathbb E|\widehat Z_N-Z|^2=\frac{1-p^2}{Np^2}.}
\tag{MBO3}
\]

This quantifies an observation horizon without asserting physical thermodynamic work. At \(p\downarrow0\), the inverse noise cost diverges for fixed \(N\); at \(p=0\), the source cannot be identified from these readouts. At \(p=1\), the idealized pair product is exactly \(Z\), so the model has zero sampling variance.

If \(Z\) has a **declared uniform prior** on the four 4th roots of unity and the masks are chosen Haar-uniform on this finite group \(C_4\), then the one-channel observations are source-independent, while \(V=\overline AB\) has conditional distribution

\[
\Pr(V=v\mid Z=z)=p\,\mathbf1_{v=z}+\frac{1-p}{4}.
\]

Its exact Shannon information is

\[
\boxed{
I(Z;A,B)=2+a\log_2a+3b\log_2b,\quad
a=\frac{1+3p}{4},\ b=\frac{1-p}{4},
}
\tag{MBO4}
\]
taking \(0\log0=0\). In particular \(I(0)=0\), \(I(1)=2\) bits, and
\(I(p)=3p^2/(2\ln2)+O(p^3)\) as \(p\downarrow0\). This is epistemic information about the declared finite random source, **not entropy of π**, thermodynamic entropy, or a statement that the BBP source is Haar-distributed.

The **genuine null** is independent masks at every setting: source-specific cross-correlation then vanishes. Conditional positive \(|A|^2\) or \(|B|^2\) cannot distinguish this null from the coupling model.

## 2. One upward knowledge-volume step, operationally—not literally a Dirac distribution

In the user's proposed knowledge volume, a base plane contains forms and observations; recurrent coherent relations may warrant a representation on the plane above. The mathematically sound *operational* realization here is an observable-degree lift:

\[
\mathscr L_1=\operatorname{span}\{1,A,B,\overline A,\overline B\},\qquad
\mathscr L_2=\mathscr L_1+
\operatorname{span}\{\overline A B,A\overline B\}.
\tag{MBO5}
\]

The first-moment restriction can be identically zero as a source discriminator while \(\overline AB\) belongs to the next degree and has source-dependent expectation. This is a **tensor/product lift** of a measurement algebra, not a proof that a literal Dirac delta metrically separates two planes. A Dirac distribution \(\delta_x\) localizes a point/source evaluation; it does not itself specify the distance between knowledge layers. If a metric on layers is wanted, define probe costs, Hilbert norms or discrimination radii separately.

Existing [Contextual Zero Backbone](../../../docs/CONTEXTUAL_ZERO_BACKBONE.md) interprets a zero as equality relative to a source-contextual quotient, not equality of all forms. [Principia knowledge/identification](../../../docs/principia_observatoris/03_knowledge_proof.md) requires a target to factor through actual accessible evidence. Prior [Adaptive Haar observer AH-03/04/05](https://github.com/femboy2112/SUCC/pull/641) explicitly constructs structural probes having zero immediate target information but positive future option value. The new "push \(p\)" model is a minimal clean algebraic instance of that **type of mechanism**, not independent source evidence for the earlier result.

### MBO-03 — the next level can be third order (CLASSICAL/EXACT)

Take independent uniform \(R_1,R_2\in\mathbb T\), and define
\[
A=R_1,\quad B=R_2,\quad C=ZR_1R_2.
\tag{MBO6}
\]
Every individual **and every two-channel** marginal law is independent of \(Z\), but

\[
\boxed{\mathbb E[\overline A\,\overline B\,C\mid Z]=Z.}
\tag{MBO7}
\]

Proof: each pair has a missing Haar factor and is uniformly distributed independently of \(Z\); the full product cancels both masks. \(\square\)

More generally, using \(d-1\) independent masks and one \(Z\)-times-their-product channel can conceal the source from all proper marginal subsets while revealing it at degree \(d\). Thus what constitutes "one step up" depends on the **declared observable algebra and accessible joint experiments**; first-order invisibility does not guarantee second-order recovery, and independent noise can remain opaque at every accessible order.

## 3. Gamma/Haar's actual source-memory mechanism

Earlier SUCC [Gamma-volume GV-06](../../2026-11-14/gamma_volume/THEOREMS.md) already proved an exact compression law for a source-retaining semigroup \(S_\alpha\), projection \(\Pi\), and source-independent reinjection \(J\) with \(\Pi J=I\):

\[
\boxed{
\overline S_{\alpha+\beta}-\overline S_\alpha\overline S_\beta
=\Pi S_\alpha(I-J\Pi)S_\beta J.
}
\tag{MBO8}
\]

The middle factor \(I-J\Pi\) retains the contrasts that have **zero source-average** and are lost at the first reduction. A subsequent source-dependent layer can couple those contrasts back into an observable report. This is precisely an instance where apparent first-order nullity and higher-order joint structure coexist. Its positivity is conditional: arbitrary nonreversible operators need not yield a positive scalar defect, and the source law must be retained through both stages.

The new mask model has the same **dependency architecture**: independent redraw erases the source in the cross-channel law; reusing an *actual shared mask* gives a phase-bearing covariance. It does **not** identify Gamma source, Haar randomness, a physical measurement apparatus or quantum entanglement with the original arithmetic BBP trajectory.

## 4. The honest BBP source-to-pair instrument

Retain literal
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1),
\quad Y_n=U_n+T_n=16^n\pi/16.
\tag{MBO9}
\]

For **one source clock \(n\)**, declare the controlled mask experiment from MBO1 with source phases inserted into the two channels:
\[
A_n=R_n\,e(U_n),\qquad
B_n=e(U_{n+1})(J_pR_n+(1-J_p)R'_n),
\quad e(t)=e^{2\pi it}.
\tag{MBO10}
\]

Each single-channel law is Haar, therefore **source-blind as a marginal**. Yet the signed joint moment is the exactly authenticated rational-source chronological phase difference:

\[
\boxed{
\mathbb E[\overline{A_n}B_n\mid U_n,U_{n+1},p]
=p\,e(U_{n+1}-U_n)
=p\,e(15U_n+r(n+1)).
}
\tag{MBO11}
\]

This is a *mathematical probe contract*. The masks are **added external tools** and do not randomize \(\pi\)'s digits. The phase \(e(U_{n+1}-U_n)\) is already constructible from the rational source; its recovery from a separately randomized instrument supplies no independent arithmetic evidence.

### MBO-04 — source-pinned corrected objective motion (EXACT)

Let \(\zeta_n=e(U_{n+1}-U_n)\) be the phase decoded by the second-order readout, while the actual completed objective step has \(\rho_n=\overline{z_n}z_{n+1}=e(Y_{n+1}-Y_n)=e(15Y_n)\). Then

\[
\boxed{\rho_n=\zeta_n\,e(T_{n+1}-T_n).}
\tag{MBO12}
\]

The original forcing has a positive integral density \(r(n+1)=\int_0^1 t^{8n}Q(t)\,dt\) with \(Q(t)=(1-t)(t^2+2)(t^2+2t+2)>0\) for \(0<t<1\), so \(r(n)\) is strictly decreasing. Consequently the authentic future tail \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\) strictly decreases. Thus
\[
0<T_{n+1}<T_n<\beta_n:=r(n+1)/15,
\]
and
\[
\boxed{|\rho_n-\zeta_n|\le 2\pi\beta_n.}
\tag{MBO13}
\]

**Proof:** the ratio in (MBO12) is exact. The phase chord satisfies \(|e(a)-e(b)|\le2\pi|a-b|\), and \(|T_{n+1}-T_n|<T_n<\beta_n\). \(\square\)

This is a source-coupled **signed second-order** relation and a rigorous first-order-to-second-order calibration error. It requires no stochastic assumption about the deterministic sequence \(U_n\).

## 5. A slightly sharper finite speed certificate, and the open R0 gate

Define
\[
\boxed{
d_n^{(2)}=\Big[\|U_{n+1}-U_n\|_{\mathbb T}-\beta_n\Big]_+,
\quad
\mathcal Q_B^{(2)}=\frac{16}{B}\sum_{n=B}^{2B-1}(d_n^{(2)})^2.
}
\tag{MBO14}
\]

Since \(\|\Delta Y_n\|_{\mathbb T}\ge d_n^{(2)}\) and \(|e(u)-1|\ge4\|u\|_{\mathbb T}\),
\[
\boxed{
\mathcal S_B(\pi/16)=\frac1B\sum|z_{n+1}-z_n|^2
\ge\mathcal Q_B^{(2)}.
}
\tag{MBO15}
\]

The earlier [moving-frame source certificate](MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md) used
\(d_n^{(1)}=[\|15U_n\|_{\mathbb T}-r(n+1)]_+\). The sharpened formula keeps the **exact added forcing inside the phase** and bounds only the genuinely hidden tail *change*, \(|T_{n+1}-T_n|<\beta_n\). It is not claimed that \(\mathcal Q^{(2)}\ge\mathcal Q^{(1)}\) for every conceivable source, but it improves every one of the inspected original-BBP shells.

**MBO-05 (OBSERVED FINITE EXACT):** original zero-seeded Fraction arithmetic gives:

| \(B\) | old \(\mathcal Q_B^{(1)}\) | new \(\mathcal Q_B^{(2)}\) |
|---:|---:|---:|
| 16 | 1.115511010778806 | 1.118497925016514 |
| 32 | 1.419544018700512 | 1.420255787319224 |
| 64 | 1.457849048509468 | 1.458084570487634 |
| 128 | 1.335706813143393 | 1.335759884755608 |
| 256 | 1.332030683976077 | 1.332044339267756 |

All strict improvements and all comparisons for \(B\in\{32,64,128,256\}\) to \(6/5\) were verified by **exact Fractions**, not decimal rounding. These are **in-sample finite checks**, not a held-out new asymptotic estimate.

### MBO-06 — the remaining source-selected criterion (CONDITIONAL / OPEN)

Previous [MF-04](MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md) proved
\[
1-\Re W_B(\pi/16)\ge\frac{\mathcal S_B}{8}-\frac1B
\quad\text{and}\quad
1-\Re W_B(\pi/16)\ge\frac{\mathcal S_B}{450}.
\]
Thus if
\[
\boxed{
\exists\delta>0,B_0:\ \forall B\ge B_0:\quad
\frac1B\sum_{n=B}^{2B-1}(d_n^{(2)})^2\ge\delta,
}
\tag{MBO16}
\]
then \(\mathcal S_B\ge16\delta\) and \(1-\Re W_B\ge(16/450)\delta>0\) for every late shell. **This would establish R0.** The eventual lower bound MBO16 is **OPEN**. Full π base-16 normality requires all nonzero integer Fourier modes, not just R0.

The correlation \(\mathbb E[\overline A B]=p\zeta_n\) is a *source-preserving readout*, **not an independent proof that \(\zeta_n\) has a nonzero signed all-shell mean or a positive distance from \(1\)**. Adding source-blind noise or arbitrary p-independent masks cannot create the missing arithmetic estimate.

## 6. Hostile controls and claim ledger

**MBO-07 (REFUTED overstrong inferences, with explicit receipts):**

- **Null first moments imply no information at any order:** refuted by MBO1–MBO2.
- **Nonzero single-channel variance implies source coupling:** refuted by \(p=0\), where \(\mathbb E|A|^2=\mathbb E|B|^2=1\) but the full joint distribution is independent of \(Z\).
- **Second-order always suffices:** refuted by the three-channel MBO6, whose every pair is source-blind while the third-order product is \(Z\).
- **Zero-mean noise proves the physical source is random:** refuted by entirely deterministic \(Z\) hidden behind independently randomized probe masks.
- **A fitted second-order correlation forces π normality:** refuted by locked \(x=1\) and the earlier sparse irrational countermodel (both admit the coupling construction, while R0 fails for them).
- **An inaccessible \(p\)-variation is an actual observation:** refuted as an evidence claim by the \(p=0\) joint law, which contains no \(Z\)-information; the derivative formula remains a prediction awaiting a lawful intervention.
- **One Dirac delta is a canonical distance between knowledge planes:** no mathematical distance has been declared. The degree lift is proved; the Dirac-metric identification is **UNVERIFIED**.

**Statuses:**

| ID | Status | Result / next obligation |
|---|---|---|
| MBO-01 | CLASSICAL/PROVED PAPER | Identical source-blind Haar single-channel laws with \(pZ\) second-order cross-response. |
| MBO-02 | CLASSICAL/PROVED PAPER | Exact \(1/(Np^2)\) mean-square source-estimation budget; finite-prior Shannon information formula. |
| MBO-03 | CLASSICAL/PROVED PAPER | Third-order source syndrome with all first/pair marginals source-blind. |
| MBO-04 | PROVED PAPER; SOURCE-TYPED | Original four-pole BBP signed pair phase and monotone-tail correction. |
| MBO-05 | OBSERVED EXACT FINITE | Sharper \(\mathcal Q_B^{(2)}\) at five specified shells. |
| MBO-06 | OPEN arithmetic premise / PROVED conditional implication | Uniform source-selected second-order rational speed mean implies R0, but is not known. |
| MBO-07 | REFUTED overstatements | Ordinary variance, uncorrelated noise and unmeasured couplings cannot authenticate the carrier. |
| MBO-08 | CONJECTURED / UNVERIFIED | A genuinely *new* attainable observer coupling to original BBP carry/cofactor history produces a source-specific late-shell lower bound, rather than merely re-encoding the same Weyl mode. |

**Provenance:** author insight in this conversation; [Contextual Zero](../../../docs/CONTEXTUAL_ZERO_BACKBONE.md), [Principia observer and knowledge](../../../docs/principia_observatoris/03_knowledge_proof.md), [Adaptive Haar #641](https://github.com/femboy2112/SUCC/pull/641), [Gamma source memory GV-06](../../2026-11-14/gamma_volume/THEOREMS.md), [source-shadow interferometry](SOURCE_SHADOW_INTERFEROMETRY.md), [moving-frame speed](MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md), and [Main XXVI frontier](../../../docs/PI_NORMALITY_FRONTIER.md). These are overlapping derivation families. The optional Haar masks are added to an already determinate source and do not authenticate BBP statistics.

**Validation:** [tests/test_boundary_order_lift.py](../../../tests/test_boundary_order_lift.py) runs exact \(C_4\) joint distributions, interventions, higher-order masks, and original-source Fraction steps and the enhanced speed certificate. A separate proof establishes the full continuous Haar formula. The executable model's finite \(C_4\) marginal uniformity applies only for \(Z\in C_4\); for arbitrary \(Z\in\mathbb T\), the main theorem uses continuous Haar. [Validation receipt](MOVABLE_BOUNDARY_VALIDATION.md) reports the actual test run and its limitations.

**Next verdict-changing probe:** Build a **source-derived** tunable coupling that uses the original four-pole \(r(n)\), literal zero seed, fractional fiber, integer carry/winding, and source-authenticated CRT cofactor history to produce a *conditional signed cross-response* not fixed in advance to \(e(U_{n+1}-U_n)\). Predeclare the new readout, covariance contrast, coupling budget and source-mutant outcomes. Demand a nontrivial all-late-shell inequality resistant to wrong seed, rational-shadow and sparse controls before promoting R0. That would turn a higher-order observer into an arithmetic argument rather than a new representation of the desired answer.
