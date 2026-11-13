# Target-relative signed boundary response: a continuous carry seam

Date: 2026-11-12. Base: Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`.

**Verdict.** The archive already contains the correct signed boundary object: the joint carry/arrival response, before either factor is averaged. A full bulk reconstruction, a full Gram gap, and a growing-depth inverse are unnecessary for R0. This note adds an elementary, source-realized piecewise-linear response with **quadratic resolution error and a continuous carry seam**. It improves an observation/transport instrument. It supplies **no new all-shell arithmetic saving**, and R0 and normality remain OPEN.

Authority: complete elementary paper derivations below; finite exact-rational structural checks and separately labelled high-precision numerical checks. Same-model analysis, no external review or Lean authority. No worldwide novelty claim.

## 1. Inspected sources and what is inherited

| Source | Pinned head / location | Mathematical contribution | First unpaid edge |
|---|---|---|---|
| Selected inverse branch, #312 lineage | Main: `research/2026-10-26/SELECTED_BRANCH_SYNTHESIS.md`, §6 | Signed midpoint carry/arrival approximation to the actual Weyl coefficient, with source payment | Selected signed mean tends to zero |
| Source-corrected closed paths | Main: `research/2026-11-07/pinbed_yoneda_oscillators/ANCHORED_PATHS_VS_HOLONOMY.md` | All corrected temporal holonomies are seed-blind; periodic seeds imitate finite observations | Open source-anchored statistical estimate |
| #605 target ambiguity and R0 certificates | `8fa0fe392f8c59f168a5d59a1f9c998c9e0de814`; `research/2026-11-12/holographic_boundary_filters/PHASE_AND_TARGET.md`, `PI_FILTERS.md` | Target row-span duality, minimax ambiguity, noise payment, fixed-resolution R0 minorants | Uniform positive selected certificate |
| #606 boundary tomography | `f133e37b2dc736a1200a6cb15184291b4557e0fd`; `research/2026-11-12/holographic_boundary_filters/THEOREMS.md` | Reachable-observable quotient; conditional digit Fourier lines; source port separate | Uniform signed original-source response |
| #607 filter complexity | `18a32aa23e1861a67b9f8d904f625b41aac00c1a`; `research/2026-11-12/boundary_filter_complexity/README.md`, `FILTER_TRANSPORT.md`, `DUAL_CERTIFICATE_BARRIER.md` | Finite-rank obstruction, source-grid resolution costs, full Gram-to-escape bridge | Uniform full Gram gap, stronger than CH/R0 |
| #604 two-root selection | `220df67b4ee3f558de63f08cc76ed52b34138302` | Finite seed-grid/infinite-time order-of-limits distinction | Selected signed residual at intermediate scales |

The four unmerged heads were inspected as donor sources, not merged. #605 and #606 contain distinct material under the same dossier path; a path alone does not establish provenance.

In particular, the following is **inherited**, not a new theorem: future-cell midpoint phases reconstruct the signed Weyl mean with error of order `|h|/q`, and complete finite digit Fourier lines reconstruct conditional defect. The new result below uses first moments to make the contracted response continuous and improve the error to order `h²/q²`.

## 2. The actual finite source packet

Let `r(n)` be the authentic four-pole forcing, `U_0=0`, `U_(n+1)=16U_n+r(n+1)`, and

\[
u_n=\{U_n\},\quad C_n=\lfloor U_n\rfloor,\quad
c_{n+1}=C_{n+1}-16C_n=\lfloor16u_n+r(n+1)\rfloor.
\]

Retain the literal integer carry, including carry 16 if it occurs. Then

\[
16u_n=c_{n+1}+u_{n+1}-r(n+1).
\tag{H1}
\]

Thus for every integer `h`,

\[
e(hu_n)=e\!\left(\frac{h(c_{n+1}-r(n+1))}{16}\right)
           e\!\left(\frac{h u_{n+1}}{16}\right).
\tag{H2}
\]

The source correction sign and the association of carry with its actual arrival are essential. No prime marginal, cofactor, winding or temporal order has been independently averaged.

For a shell `B<=n<2B`, the exact signed boundary measure is

\[
\nu_{B,h}=\frac1B\sum_{n=B}^{2B-1}
 e\!\left(\frac{h(c_{n+1}-r(n+1))}{16}\right)\delta_{u_{n+1}}.
\]

It obeys `||nu_(B,h)||_TV<=1` and

\[
W^U_B(h)=\int_0^1e(hy/16)\,d\nu_{B,h}(y).
\tag{H3}
\]

This is the old selected carry/arrival response, with the forcing correction kept exactly. It is a boundary response retaining the joint phase; its existence does not control its value.

## 3. HBT-01: quadratic, norm-stable target reconstruction

**PROVED LOCAL.** Fix integers `q>=1`, `h`, and `B>=1`. For each actual arrival put

\[
w_n=\lfloor q u_{n+1}\rfloor,\qquad
\lambda_n=q u_{n+1}-w_n,\qquad
\alpha_n=e\!\left(\frac{h(c_{n+1}-r(n+1))}{16}\right).
\]

For `0<=w<q`, define the directly weighted signed response channels

\[
L_w=\frac1B\sum_{w_n=w}(1-\lambda_n)\alpha_n,\qquad
R_w=\frac1B\sum_{w_n=w}\lambda_n\alpha_n.
\]

These are cell masses and first moments in barycentric coordinates. Every exponent and every barycentric weight is rational on the original rational orbit, so they are implementable as exact finite rational-phase dictionaries; no new measurement port is being assumed. Define

\[
\mathcal C_{B,q}(h)=\sum_{w=0}^{q-1}
\left[e\!\left(\frac{hw}{16q}\right)L_w+
 e\!\left(\frac{h(w+1)}{16q}\right)R_w\right].
\tag{H4}
\]

Then

\[
\boxed{|W^U_B(h)-\mathcal C_{B,q}(h)|
       \le\frac{\pi^2h^2}{512q^2},\qquad
       \sum_w(|L_w|+|R_w|)\le1.}
\tag{H5}
\]

If measured channels have total complex absolute error at most `epsilon`, the reconstructed target changes by at most `epsilon`. This is an operator norm-one estimate in the **barycentric channel l1 norm**, independent of the number of bins.

**Proof.** On `[a,b]`, linear interpolation `I f` of a twice continuously differentiable complex function satisfies

\[
|f(t)-If(t)|\le\frac12\sup_{[a,b]}|f''|\,(t-a)(b-t)
\le\frac18\sup|f''|\,(b-a)^2.
\]

The integral interpolation remainder has a nonnegative scalar Peano kernel, so the same bound holds for complex values using the triangle inequality. For `f(y)=e(hy/16)`, `sup|f''|=(pi h/8)^2` and cell length is `1/q`; this gives `pi²h²/(512q²)`. Multiply each error by the unit-modulus `alpha_n`, average, and use H2. Since `0<=lambda_n<1`, summing absolute channel values is at most the total original mass, one. Finally all coefficients in H4 have modulus one, proving the noise bound. QED.

**Noise accounting caveat.** If one instead measures unscaled first moments `H_w=integral_(cell) y dnu` and masses `M_w`, conversion gives `R_w=qH_w-wM_w`, `L_w=(w+1)M_w-qH_w`. Errors in `H_w` are multiplied by `q`. The norm-one statement is not a free guarantee for those different measurement coordinates. Exact rational barycentric weights are available here because the original recurrence computes each arrival.

## 4. HBT-02: the contracted carry seam is continuous

**PROVED LOCAL.** Let `P_(q,h)(t)` be the piecewise-linear interpolation, on the entire grid `(1/q)Z`, of `e(ht/16)`. For a real forcing value `r`, define

\[
K_{q,h,r}(u)=e(-hr/16)P_{q,h}(16u+r).
\tag{H6}
\]

It is continuous, 1-periodic in `u`, and

\[
\boxed{\operatorname{Lip}(K_{q,h,r})
 \le32q\left|\sin\frac{\pi h}{16q}\right|
 \le2\pi|h|.}
\tag{H7}
\]

The summand in H4 is exactly `K_(q,h,r(n+1))(u_n)`. Therefore replacing each source-state input `u_n` by any approximation at circle distance at most `epsilon_n` changes the contracted response by at most

\[
\frac{2\pi|h|}{B}\sum_{n=B}^{2B-1}\epsilon_n.
\tag{H8}
\]

No common digit chart or cell label is needed for this final scalar estimate.

**Proof.** Neighboring grid values of `P` differ by modulus `2|sin(pi h/(16q))|`. Its slope has modulus at most `2q|sin(pi h/(16q))|`. Composition with `16u+r` gives H7. Grid values satisfy `P(t+16)=P(t)` for integer `h`; interpolation retains that periodicity. At an arrival seam, `(c,y)=(c,1)` and `(c+1,0)` give the same product `e(h(c+1-r)/16)`. Hence the separately labelled channels may change, but their contraction has no jump. QED.

This continuity is the useful improvement over a stepwise midpoint readout. It does **not** make the interval Wasserstein/CDF defect globally branch-free; H7 is specifically a scalar smooth-character approximation with paid interpolation error.

## 5. HBT-03: completed-phase payment and the exact R0 threshold

The original source has `0<T_n<=r(n+1)/15`, and `Y_n=U_n+T_n=16^n*pi/16`. Thus H5 gives

\[
\boxed{|W_B(h)-\mathcal C_{B,q}(h)|\le
\frac{\pi^2h^2}{512q^2}
+\frac{2\pi|h|}{15B}\sum_{n=B}^{2B-1}r(n+1).}
\tag{H9}
\]

One can add H8 and the declared channel error to H9. Using the inherited bound `r(m)<=47/(15m²)`, the second term is at most `94*pi*|h|/[225(B+1)²]`.

Consequently the explicit candidate

\[
\exists q\ge1,\eta>0,B_0\quad\forall B\ge B_0:
\quad \Re\mathcal C_{B,q}(1)
\le1-\eta-\frac{\pi^2}{512q^2}
\tag{H10}
\]

would give R0 after a sufficiently large increase in `B_0` (with saving, for example, `eta/2`). The **new arithmetic ingredient would have to be a proof of H10 from the original-zero source**. None is supplied here. With free choice of fixed `q`, this is another R0 interface, not an independently weaker theorem. It must not be ranked as a solved dependency edge.

For R0, any proved margin larger than the fixed interpolation budget suffices; there is no requirement that the number of channels tend to infinity. For normality, every fixed nonzero `h` requires a vanishing signed mean, then the resolution can be sent to infinity in a separate explicitly controlled limit. Full state reconstruction remains unnecessary.

## 6. HBT-04: the quadratic order is sharp for mass/first-moment data

**PROVED LOCAL; universal response-contract statement, not a counterexample to the authenticated BBP orbit.** Within a future cell of width `1/q`, consider a symmetric two-point probability and the midpoint point mass. They have identical cell mass and first moment. With points at the endpoints and midpoint, their `e(hy/16)` integrals differ in modulus by

\[
1-\cos\left(\frac{\pi h}{16q}\right)
\sim\frac{\pi^2h^2}{512q^2}\qquad(q\to\infty,\ h\ne0\text{ fixed}).
\tag{H11}
\]

For a half-open partition, take the symmetric points strictly inside and let them approach the endpoints; these interior pairs approach the displayed endpoint gap. This is a lower bound on possible ambiguity, not its exact supremum for arbitrary h and q. The elementary identity is

`(e(ha/16)+e(hb/16))/2 = e(h(a+b)/32) cos(pi h(b-a)/16)`.

No target-recovery method using only those mass/first-moment data has uniform error `o(q^-2)` over the full declared class: an identical observation cannot approximate both target values to less than half their difference. H5's error bound has the same asymptotic **order**; this argument does not claim its constant is minimax-optimal (the two-target ambiguity yields half the gap).

## 7. HBT-05: full source compatibility is a singleton, not a hidden-sector pair

**PROVED LOCAL; elementary uniqueness.** If two systems both obey the exact original recurrence for every `n` and both have literal `U_0=0`, they have the same `U_n` for every `n`, by induction. With the same authenticated completion they have the same phases and the same R0 truth value.

Therefore an explicit pair of **fully** source-compatible systems with different R0 behavior cannot be constructed. A proposed indistinguishable pair must state the relaxed contract: a finite prefix, a phase-only port, a denominator grid, finite tolerance, free seed, or a mutant forcing. Hidden sectors elsewhere in a realization cannot change an observable already fixed by that recurrence.

This does not prove R0. A singleton mathematical object can still have an unproved asymptotic property. It distinguishes lack of target identifiability on a relaxed model class from the present lack of an all-scale arithmetic inequality for the identified source.

## 8. Hostile controls and actual validation

The test grid was fixed before the run: original-source rational seeds `0,1/16,1/3`; shells `B=7,13` and fresh larger shells `B=37,73`; resolutions `q=1,2,7,16`; modes `h=1,-1,3,17`. It was a diagnostic grid, not externally blinded and not an infinite certificate.

Executed in this session:

- **438 exact rational checks** of H1 (three seeds, `0<=n<146`).
- **192 high-precision interpolation checks** of H5, evaluated at 80 decimal digits. Maximum observed error/bound was `0.4789775904106247990002068661994432211035`.
- **146 exact alias checks:** seed `1/16` and seed zero have identical later rational fractional states. The separate unwrapped seed port distinguishes them.
- A mutation omitting `e(-hr/16)` failed the claimed bound already at the initial source step with `q=16,h=1`.
- Symmetric interior-pair controls at `q=16,64,256`, with endpoint inset `1/(10000q)`, gave ambiguity/bound ratios `0.9995875002488191`, `0.9995992562618643`, `0.9995999910163521`.

The numerical checks are not interval certificates. The universal error authority is the interpolation proof. Exact rational recurrence checks test source wiring only. The probe used the existing `SelectedOrbit` and `original_forcing` functions without edits. The root validation record should preserve its executed probe and receipt if this note is included in a PR.

Further decisive controls:

- Same forcing and seed `-pi/16` has completed `W_B=1`; H9 forces the response toward 1. Thus the transform cannot manufacture cancellation.
- A completed fixed point `1/15` has positive R0 saving but `|W_B|=1` and rank-one consecutive-phase Gram. A full Gram gap is unnecessarily strong for the target.
- Replacing signed `L_w,R_w` by magnitudes loses the original phase and invalidates H4.
- Pairwise factor marginals do not determine their joint response; no independence is imported.
- Higher powers, more bins, and exact source authentication improve access or approximation, not the unknown all-shell response estimate.

## 9. Next decisive arithmetic probe

Try to derive H10 at a **fixed small q** using the exact source-weighted barycentric channels, while retaining the cofactor and original-zero history. The quantitative debt is now explicit and does not worsen with temporal horizon. A proof must bound their signed contraction, not merely their separate norms.

Pass: an all-large-B inequality with a margin exceeding the fixed interpolation budget, derived from a property that the coherent counterseed fails. This proves R0 through H9.

Fail: the purported proof also applies to `s=-pi/16`, replaces joint channels by independent marginals, or derives its bound by assuming a Fourier saving. Retain the resulting counterexample or circular dependency.

Ambiguous: finitely many original-source certificates are positive but no all-scale induction, arithmetic estimate, or admissible limiting argument follows. This is the current status.

## Retained adversarial repair

The initial wording called H11 the ambiguity supremum for every h,q. That was false: at h=32,q=1, the endpoint pair and midpoint have equal response, but the interior pair {1/4,3/4} and midpoint 1/2 have identical mass/first moment and response gap 2. The root repaired the wording after the read-only current audit. The proved fixed-h, q-to-infinity quadratic-order lower bound is unaffected.
