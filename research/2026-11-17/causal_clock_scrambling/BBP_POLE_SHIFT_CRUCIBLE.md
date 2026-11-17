# BBP Pole-Shift Crucible — A Source-Specific Obstruction, Two Locked Rivals, and the Causal-Oracle Rank Barrier

**SUCC / Operation Aletheia, original zero-seeded π frontier** — 2026-11-17

**Research demand:** combine the literal BBP null-section, causal/history interferometry, backward rational endpoint norm, and observer-direction oracle to prove π base-16 normality if possible. Strongly challenge any purported source-derived all-shell inequality and retain only verified mathematical consequences.

**Verdict:** BPC-01–07 are proved algebraic or analytic claims under their stated hypotheses, with focused exact regressions. BPC-08 is a *conditional* external research input. The fundamental universal estimate \(\liminf_B R_B(\pi/16)>0\), R0, and full base-16 π normality remain **OPEN**. These are source-typed applications of established rational-summation, dynamical and continued-fraction facts, not claims of academic priority.

## 1. The authenticated source and the actual target

Fix exactly
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
The imported BBP identity gives \(x=\pi/16\) and \(U_n+T_n=16^nx\), where \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\). The **source-null section** is the homogeneous-input invariant
\[
I_n=16^{-n}\big(U_n-\sum_{j=1}^{n}16^{n-j}r(j)\big)=0.
\]
This selects the actual history relative to the full source passport, but is not a digit-distribution theorem.

The exact terminal source-norm gate is inherited:
\[
\boxed{R_B=\frac1B\sum_{k=1}^{B}\|U_{2B}/16^k\|_{\mathbb T}^{\,2},
\quad \mathrm{R0}\iff\liminf_{B\to\infty}R_B>0.}\tag{BPC0}
\]
Full base-16 normality demands *all nonzero Fourier modes*, not just R0.

## 2. A locked null-seeded four-pole rival matching BBP's leading asymptotics

Define the rational profile
\[
a(n)=\frac1{(8n-7)(8n-6)}
=\frac1{8n-7}-\frac1{8n-6},
\]
and a different forcing
\[
\boxed{r_{\rm tel}(n)=16a(n)-a(n+1).}\tag{BPC1}
\]
This has exactly four simple-pole terms,
\[
r_{\rm tel}(n)=\frac{16}{8n-7}-\frac{16}{8n-6}
-\frac1{8n+1}+\frac1{8n+2}.
\]

**BPC-01 (PROVED; exact locked zero-input control).** Its zero-seeded completed endpoint is *rational*:
\[
\boxed{\sum_{n\ge1}16^{-n}r_{\rm tel}(n)
=a(1)=\frac12.}\tag{BPC2}
\]
Proof: the partial sum telescopes to \(a(1)-16^{-N}a(N+1)\) and the remainder vanishes. Its completed radix-16 circle orbit is therefore exactly phase 1 for every \(n\ge1\).

**BPC-02 (PROVED; source-class matching).** This forcing is positive and strictly decreasing, because
\[
r_{\rm tel}(n)=\int_0^1 t^{8n-8}(1-t)(16-t^8)\,dt>0,
\]
and the integrand strictly decreases with \(n\) for every \(t\in(0,1)\). It has the **same leading asymptotic** as the actual BBP forcing:
\[
\boxed{r(n)=\frac{15}{64n^2}+O(n^{-3}),\quad
r_{\rm tel}(n)=\frac{15}{64n^2}+O(n^{-3}).}\tag{BPC3}
\]

Thus **null seed + four rational simple poles + strictly positive monotone forcing + the exact BBP leading \(15/(64n^2)\) profile** do not imply R0. This rival changes the actual pole positions and coefficients and is **not** a counterfeit with identical original forcing.

## 3. The genuine BBP poles carry an uncancelled shift-orbit invariant

The actual \(r(z)\in\mathbb Q(z)\) has simple poles and residues
\[
\begin{array}{c|cccc}
\text{pole } \alpha &7/8&1/2&3/8&1/4\\ \hline
\operatorname{Res}_{z=\alpha}r(z)&1/2&-1/4&-1/8&-1/8
\end{array}
\tag{BPC4}
\]
**An exact projected-zero/interferometry witness.** The *coarse* observer that remembers only the total residue sees
\[
\boxed{\tfrac12-\tfrac14-\tfrac18-\tfrac18=0.}
\]
But the four-component **integer-shift-orbit-resolved** residue is the nonzero vector \((1/2,-1/4,-1/8,-1/8)\). The global zero is cancellation, **not absence of four independent source-supported pole directions**. The shift-orbit weighted residues below are unchanged by adding any rational coboundary \((16-E)h\): this is a genuine source-class invariant relative to rational clock-gauge corrections, not an absolute invariant under arbitrary analytic completion or changes of forcing. The locked alternative also has total residue zero, but its **weighted residues vanish separately in each paired shift orbit**. This is an operational instance of a null coarse readout acquiring a nonzero source signature after a *lawful refinement of the observer algebra*. It does not yet impose a signed positive density on BBP integer carries.

All four poles lie in **different** equivalence classes \(\alpha+\mathbb Z\) of integer shifts.

Suppose a rational function \(h(z)\in\mathbb C(z)\) obeys
\[
r(z)=16h(z)-h(z+1).\tag{BPC5}
\]
On any pole orbit \(\alpha+\mathbb Z\), let \(c_j^{(k)}\) be the coefficient of \((z-\alpha-j)^{-k}\) in the partial fraction of \(h\). These coefficients have finite support. The corresponding coefficients of \(r\) would be
\[
b_j^{(k)}=16c_j^{(k)}-c_{j+1}^{(k)}.
\]
Therefore the **weighted shift-orbit residue** must vanish:
\[
\boxed{
\sum_{j\in\mathbb Z}16^{-j}b_j^{(k)}
=\sum_j16^{-j}(16c_j^{(k)}-c_{j+1}^{(k)})=0.
}\tag{BPC6}
\]

**BPC-03 (PROVED; source-specific rational-coboundary obstruction).** For each original simple-pole orbit, the sum (BPC6) equals exactly the one nonzero residue in (BPC4), contradiction. Thus
\[
\boxed{\nexists h\in\mathbb C(z):\ r(z)=16h(z)-h(z+1).}\tag{BPC7}
\]
In particular the actual source's future tail \(T_n\) is **not an everywhere-equal rational function of the clock**: if \(T_{n-1}=h(n)\) for all sufficiently large \(n\), the tail recurrence would give the rational identity (BPC5) at infinitely many positive integers, hence identically, contradicting BPC7.

For the locked rival (BPC1), the source poles occur in **shifted pairs**; the orbit residues of \(a\) are \(\pm1/8\), and the forcing coefficients at shifts \(j=0\) and \(j=-1\) are \(16c,-c\). Their weighted sums vanish exactly. The difference between the pole patterns is source-specific and falsifiable.

**Boundary:** the actual *nonrational infinite* \(h(n)=T_{n-1}\) DOES solve (BPC5) as a sequence. Excluding a rational closed form is not excluding all analytic/nonrational completions, and **does not by itself prove any uniform shell phase separation**. This is an instance of classical rational difference-equation pole-orbit obstruction, related to Abramov's rational summation theory and later discrete-residue work; it is not a newly discovered general criterion.

## 4. Higher-order terminal interferometry has an exact rank-one history collapse

Let \(N=2B\) and perturb each forcing event by a hypothetical impulse vector \(a=(a_1,\ldots,a_N)\), keeping \(U_0=0\). The terminal state is
\[
\boxed{U_N(a)=U_N(0)+\sum_{j=1}^{N}16^{N-j}a_j.}\tag{BPC8}
\]
Thus the linear map from an \(N\)-coordinate source-history perturbation to the terminal scalar has rank **one** and an \((N-1)\)-dimensional kernel.

**BPC-04 (PROVED; endpoint-probe no-go).** No family of readouts that *all factor through \(U_N(a)\)*—including every \(k\)-th backward phase, its modulus, analytic derivative, Gram tensor, and any finite statistical order—can distinguish two impulse histories with the same weighted sum in (BPC8). Its full Jacobian has rank at most one wherever derivatives exist; even higher-order nonlinear moments cannot repair an exactly identical endpoint.

For example, an impulse \(16^{-(j_2-j_1)}\) at clock \(j_1\) and an impulse 1 at \(j_2>j_1\) yield **the same full real states at every clock \(\ge j_2\)**, yet distinct earlier histories. These are adversarial changed-forcing models, not claims of extra impulses in the authentic source.

**BPC-05 (PROVED; history-lift contrast).** If the observer retains the entire chronological vector \((U_1,\ldots,U_N)\), its impulse Jacobian is lower-triangular:
\[
J_{nj}=\mathbf1_{j\le n}16^{n-j},
\]
with diagonal 1 and determinant 1. It reconstructs every hypothetical impulse:
\[
\boxed{a_n=U_n(a)-16U_{n-1}(a)-r(n).}\tag{BPC9}
\]
Thus a *new historical observation layer* can resolve distinctions a single terminal endpoint provably cannot. This is a concrete SUCC source-anchored reading of the user's "holographic information" and proof-direction oracle, not a mechanism proving digit randomness.

**Probe lesson:** the terminal norm remains the correct scalar R0 target; source-history access is what could supply *new arithmetic constraints* on its selected integer winding. Endpoint-only higher statistical order is structurally incapable of recovering the lost history in the adversarial model.

## 5. The sharp cold-neighborhood wall is \(1/17\), not an all-shell theorem

For any \(y\in\mathbb R/\mathbb Z\), let \(d_n(y)=\|16^ny\|_{\mathbb T}\).

**BPC-06 (PROVED; sharp forward cold-run lemma).** If
\[
d_n(y),d_{n+1}(y),\ldots,d_{n+L-1}(y)<1/17,
\]
then
\[
\boxed{d_n(y)<\frac{16^{-(L-1)}}{17}.}\tag{BPC10}
\]
Proof: choose the unique signed representatives \(v_j\in(-1/17,1/17)\). Since \(|16v_j|<16/17=1-1/17\), an integer wrap by \(\pm1\) cannot land back in the strict inner interval. Hence \(v_{j+1}=16v_j\) at each of the \(L-1\) steps. An infinite such run forces \(v_0=0\). Consequently every irrational orbit has **infinitely many** \(n\) with \(d_n\ge1/17\). The threshold is sharp: \(y=1/17\) yields the period-two orbit \(1/17,16/17,\ldots\), with every distance equal to \(1/17\).

This yields recurring *individual* escape events, but no lower bound on their **density**. R0 demands average phase energy on every sufficiently late B..2B shell.

## 6. Even badly approximable numbers can fail R0: critical Kempner control

Let
\[
\boxed{\kappa_{16}=\sum_{j=0}^{\infty}16^{-2^j}.}\tag{BPC11}
\]
Classical work by Jeffrey Shallit and later continued-fraction accounts establishes that this base-\(u\) Kempner family has **bounded partial quotients** for integer \(u\ge2\). Hence \(\kappa_{16}\) is badly approximable, and in particular its irrationality exponent is exactly 2.

For \(B_j=2^j\), all earlier sparse digits contribute integers to \(16^n\kappa_{16}\) on \(B_j\le n<2B_j\). The fractional part is exactly
\[
f_n=\sum_{\ell\ge j+1}16^{n-2^\ell}.
\]
The sum is below one, and
\[
\begin{aligned}
\sum_{n=B_j}^{2B_j-1}f_n
&=\frac{16^{2B_j}-16^{B_j}}{15}
\sum_{\ell\ge j+1}16^{-2^\ell}\\
&<\frac{16}{225},
\end{aligned}
\]
using the elementary bound on the subsequent lacunary tail. Because \(1-\cos(2\pi t)\le2\pi t\) for \(0\le t\le1\),
\[
\boxed{
0\le1-\Re W_{B_j}(\kappa_{16})
<\frac{32\pi}{225B_j}\longrightarrow0.
}\tag{BPC12}
\]

**BPC-07 (PROVED mathematical combination / hostile control).** Even *bad approximability* (and therefore optimal irrationality exponent 2), exact nonperiodicity, and a **zero-seeded** source representation do **not** force R0. The zero-seeded alternative recurrence here has rational forcing \(\widetilde r(n)=1\) when n is a power of 2 and zero otherwise, so it is **not** the four-pole BBP forcing. It nearly saturates the cold-run threshold: on its critical shell, the first \(B_j-1\) positions lie strictly below \(1/17\), but the final position crosses the threshold. This illustrates exactly why sporadic escape events are too weak.

The standard badly-approximable classification is inherited from published continued-fraction mathematics, not proven by the finite tests. Bibliography: Shallit, *Simple Continued Fractions for Some Irrational Numbers*, J. Number Theory 11 (1979), https://doi.org/10.1016/0022-314X(79)90040-4; Shallit's 2022 ECA interview https://ecajournal.haifa.ac.il/Volume2022/ECA2022_S3I5.pdf ; Hone–Varona, *Continued fractions and irrationality exponents for modified Engel and Pierce series*, Monatshefte für Mathematik 2019, https://doi.org/10.1007/s00605-018-1244-1 .

## 7. New external result under review: \(\mu(\pi)=2\) would not settle R0

An OpenAI September 24, 2026 [preprint](https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026) **claims** the irrationality exponent of π is 2, and its [formalization scope note](https://github.com/openai/math/blob/main/lean/docs/017.md) reports a Lean proof of the eventual \(q^{-2-\epsilon}\) lower bound. A [third-party status review](https://fcmo-ai.github.io/FCMO-AI-Newsletter/2026/10/08/openai-manuscript-claims-the-irrationality-exponent-of-is-exactly-2/) reports successful independent machine-checking of the encoded statement, while emphasizing **lack of independent mathematical referee review and unverified paper-to-code semantic equivalence**. Treat the research claim as *promising, externally reported/formalized, not independently reproved here*.

**BPC-08 (CONDITIONAL on the external theorem).** If \(\mu(\pi)=2\) is accepted as stated, then for every \(\epsilon>0\), for sufficiently large n,
\[
\boxed{\|16^{n}\pi/16\|_{\mathbb T}
=\|16^{n-1}\pi\|_{\mathbb T}
\ge 16^{-(1+\epsilon)(n-1)}.}\tag{BPC13}
\]
This gives the restricted exponent \(v_{16}(\pi)\le1\), matching the *consequence* of the previously studied critical-quintic floor, **without proving that floor or R0**. The Kempner control (BPC12) establishes that even the stronger badly-approximable hypothesis is insufficient for any positive dyadic-shell average.

**Further conditional critical-horizon implication.** Combining BPC-10's cold-run lemma with the claimed \(\mu(\pi)=2\), for any fixed \(\eta>0\) and all sufficiently large start clocks \(n\), the authentic π orbit cannot remain *strictly inside* the \(1/17\) neighborhood for \(L\ge(1+\eta)n\) consecutive ticks. Indeed a cold run would imply
\[
\left|x-\frac{p}{16^n}\right|
<\frac{16^{-(n+L-1)}}{17},
\]
which is eventually a \(q^{-(2+\eta/2)}\)-type approximation with \(q=16^n\), in contradiction with \(\mu(x)=2\). **This controls exceptionally long contiguous cold runs, not their aggregate density.** Kempner's failing shells contain cold runs of length \(B-1\) starting at \(n=B\), showing why the critical length ratio 1 remains compatible with badly approximable sources and failure of R0.

If the external theorem is independently accepted, its consequences should be integrated into the restricted-exponent claim ledger with source provenance; it must not be silently promoted to π normality or a proof of Main XXVI R0.

## 8. Source-faithful next offensive, with verdict-changing tests

**THE MISSING THEOREM** remains
\[
\boxed{\exists\delta>0,B_0\ \forall B\ge B_0:
R_B(0)=\frac1B\sum_{k=1}^B\left\|\frac{U_{2B}(0)}{16^k}\right\|_{\mathbb T}^2\ge\delta.}\tag{BPC14 — OPEN}
\]
The oracle's equivalently strong positive-density certificate asks for fixed \(\epsilon,\theta>0\) and at least \(\theta B\) source-separated terminal backward positions on **every** late shell. Full base-16 normality still requires the other Fourier modes even if BPC14 is proved.

This round finds a **genuine source-specific algebraic signature**—the uncancelled four shift-orbit residues in BPC4–BPC7—but has not transported it into a quantitative shell-winding density bound. It also shows why the proposed transport must be new: endpoint-only probes have a rank-one causal-history map, and badly approximable zero-input rivals can remain cold.

**Prospective falsifier:** propose a *source-selected pole/cofactor/carry-to-terminal-density inequality* that distinguishes the original four shift-separated residues from the locked shift-paired telescope; predeclare the period/height and source-passport information admitted to its proof. Demand that it reject all four hostile families: (i) tel source with identical leading \(n^{-2}\) coefficient but rational locked endpoint; (ii) sparse badly-approximable Kempner source with cold dyadic shells; (iii) coherent original-forcing wrong seed \(s=-\pi/16\); (iv) identical-terminal but different-impulse causal histories. Then seek a uniform bound on **all B**, not a finite fit or a disguised Weyl sum.

### Claim ledger

| Claim | Status | Exact scope |
|---|---|---|
| BPC-01/02 | **PROVED PAPER + FINITE CHECKED** | Alternative four-pole positive decreasing forcing with original leading asymptotic, zero seed and locked rational completed endpoint |
| BPC-03 | **PROVED PAPER + SYMBOLIC CHECK** | Original BBP forcing has a nonzero weighted residue in each of four integer-shift pole orbits; no rational source telescope or rational clock-tail |
| BPC-04/05 | **PROVED PAPER + EXACT CHECK** | One terminal source map has rank-one impulse sensitivity; full clock history has invertible lower-triangular source map |
| BPC-06 | **PROVED PAPER + EXACT CHECK** | Sharp cold-run threshold 1/17 and only pointwise, not positive-density, escape |
| BPC-07 | **PROVED using established CF result / finite checked** | Badly approximable \(\kappa_{16}\) fails R0; it is not authenticated BBP forcing |
| BPC-08 | **CONDITIONAL EXTERNAL CLAIM** | Recent \(\mu(\pi)=2\) claim would imply restricted exponent ≤1 but not R0; independent semantic review outstanding |
| BPC-09 | **OPEN** | Original zero-selected four-pole arithmetic forces terminal backward-winding positive density and hence R0/normality |

**Dependencies:** [source-null invariant](SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md), [source proof-direction oracle](PROOF_DIRECTION_ORACLE.md), [terminal endpoint coercivity](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), [original π frontier](../../../docs/PI_NORMALITY_FRONTIER.md), [integer-winding erasure](../../2026-11-16/defect_window_tomography/TERMINAL_WINDING_ERASURE.md), [SUCC Method](../../../docs/METHOD.md). Related classical machinery: Abramov (1971) and Arreche–Sitaula (2026), *A computational approach to rational summability and its applications via discrete residues*, J. Symbolic Computation 135, https://doi.org/10.1016/j.jsc.2025.102552.

**Execution receipts:** [pole/source/tomography exact tests](../../../tests/test_bbp_pole_telescope_oracle.py), [cold-run/Kempner tests](../../../tests/test_cold_run_horizon.py), [validation record](BBP_POLE_SHIFT_VALIDATION.md). Tests check finite arithmetic and explicit finite witnesses; they do not replace the universal residue proof, Shallit's infinite continued-fraction theorem, or the unproved BBP shell inequality.
