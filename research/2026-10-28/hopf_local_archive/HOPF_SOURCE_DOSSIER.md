# OPERATION HAND-TO-HAND: SUCC × Quaternionic Hopf × Source-Faithful Chiral Transport

**Prepared locally:** 2026-10-27 (America/New_York).  
**Mutations:** NONE to GitHub. No branches, commits, PRs, labels, approvals, workflow changes, or main updates.  
**Status:** Self-contained mathematics, exact fraction implementation, focused replay and independent symbolic oracle. NOT an approved replacement for SUCC's original source or a proof of π normality or RH.

## 0. Pinned inputs and epistemic scope

- SUCC `main` observed at `6dd80730c3575d91f746546a25da5aedbd2e2737` (Main XI). The repository's proposed Main XII consolidation is draft [PR #342](https://github.com/femboy2112/SUCC/pull/342) with observed head `ce7df73431e85a4eb2a290445da8e09d4f924b3e`. DO NOT infer its merge status from this frozen note.
- Primary direct source: [PR #333](https://github.com/femboy2112/SUCC/pull/333) at `a0e4bfd9c218dfdc83ed9d5684ce8d8e4624cde5`, `observational_succ/rank_two_chiral_towers.py` and `research/2026-10-27/BBP_RANK_TWO_CHIRAL_E_TOWERS.md`. Original SUCC BBP numerator/denominator independently checked against `main/observational_succ/bbp_natural_carrier.py`.
- The category/seed firewall is [SUCC ↔ FUCC source labels](https://github.com/femboy2112/SUCC/blob/main/research/2026-10-22/SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md), [PR #310](https://github.com/femboy2112/SUCC/pull/310), and chiral [PR #333](https://github.com/femboy2112/SUCC/pull/333): equal source marginal data or positive Oily moments do NOT establish a joint law or signed Weyl cancellation.
- Standard mathematical reference: the ordinary quaternionic Hopf map, right Sp(1) quotient, and S4=HP1 are given explicitly in https://pure.hw.ac.uk/ws/files/15284396/paper_S_4_final.pdf (equations 213–215). See also https://ncatlab.org/nlab/show/quaternionic+Hopf+fibration . The new-to-SUCC content below is **the derived identification with PR333's specific matrix, gauge-parity obstruction, typed two-chart transport, source pole tomography and countermodels**. Novel academic priority not reviewed.

## 1. Exact original signed source and real rank-four chiral dynamics

The immutable original four-pole forcing is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad n\ge1.
\]

Equivalently

\[
r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.
\]

The genuine zero-seeded expanding source is `U_0=0`, `U_n=16U_(n-1)+r(n)`. π-normality remains the signed Weyl gate `\sum_{n\le N}e(hU_n)=o(N)` for each fixed nonzero integer h, **UNPROVEN**. It is not established by the decaying source impulse system below.

PR333 supplies an additive rational vector space `E=Q(i)⊕Q(i)` with **coordinatewise** multiplication. In rational coordinates `x=(Re z,Im z,Re w,Im w)`, its genuine source-selected successor is

\[
T=\frac12\begin{pmatrix}
1&0&0&1\\1&0&0&-1\\0&-1&1&0\\0&-1&-1&0
\end{pmatrix},
\quad J(a,b,c,d)=(c,-d,a,-b).
\]

For source seed `b=(2,0,0,0)` and readout `\ell(a,b,c,d)=2a-2b+2c-2d`, the first eight exact taps are `(4,0,0,-2,-1,-1,0,0)`; the first source shell Mellin moments reproduce precisely r(n). The even/odd chiral shell taps sum to masses +15/4 and −15/4, canceling the 1/n forcing leading terms. The additive source operators satisfy:

\[
T^4=-J/4,\qquad T^8=I/16,\qquad T^\mathsf{T}T=I/2,\qquad\det T=-1/4.
\]

**Crucial source typing:** the carrier `Q(i)⊕Q(i)` has nontrivial zero divisors. Quaternions `H_Q` are a division algebra (norm is sum of four rational squares). Therefore no *unital ring isomorphism* between them exists. The map `ι(z,w)=z+w j` is just a **Q-linear Euclidean isometry**, enabling a geometrically valid additional observable without replacing original ring multiplication.

## 2. Quaternionic Hopf geometry and signed interference

Let `H_Q=Q+Qi+Qj+Qk` with `i²=j²=k²=ijk=−1`. For a nonzero **pair** `q_1,q_2∈H_Q`, define

\[
D=|q_1|^2+|q_2|^2,\quad R=\frac{2q_1\bar q_2}{D},\quad B=\frac{|q_1|^2-|q_2|^2}{D}.
\]

Then `|R|²+B²=1`, so `H_R(q1,q2)=(R,B)` lies on `S4` in `H⊕R`. Every common right unit gauge `(q1,q2)→(q1u,q2u)` leaves it unchanged. Equivalently the normalized rank-one quaternionic Hermitian projector `P=(q_i\bar q_j)/D` has `P²=P`, and its coordinates are `P11=(1+B)/2`, `P12=R/2`, `P22=(1−B)/2`.

For `q_1=z_1+w_1j`, `q_2=z_2+w_2j` (complex `z_i,w_i`), the quaternionic relative value is

\[
q_1\bar q_2=(z_1\bar z_2+w_1\bar w_2)
              +(w_1z_2-z_1w_2)j.
\]

The second channel is **subtractive and order-sensitive**, not a product of independently invented Gaussian carriers. Whether this bilinear term matches any source-selected BBP cross-time Fourier saving remains a separate UNVERIFIED question.

## 3. THEOREM HOPF-CHIRAL-1 — source successor is quaternionically anti-oriented

The original rational source matrix, **not a chosen new dynamics**, has the exact Hamilton-factor decomposition

\[
\boxed{\iota(Tx)=L\,\overline{\iota(x)}\,r,
\quad L=i+k,\quad r=\frac{1-i-j-k}{4}.}
\]

**Proof.** Directly apply the right-hand side to `1,i,j,k` and compare with the four columns of the source-derived matrix T. Both are rational linear maps, so equality on the basis proves equality everywhere. Their squared norm scaling is `|L|²|r|²=2·(1/4)=1/2`, consistent with `TᵀT=I/2`; the conjugation reverses the real orientation, consistent with `det T=−1/4`.

### A decisive obstruction to treating T as a self-map of ONE Hopf S4

Take `(q1,q2)=(1,i)` and apply the common RIGHT gauge `u=j`, obtaining `(j,k)`. Their original right Hopf points are equal. Applying T independently to the two quaternionic blocks gives

\[
H_R(T1,Ti)=(k,0),\qquad H_R(Tj,Tk)=(-k,0).
\]

The images disagree. Hence **there exists no map** `F:S4_R→S4_R` satisfying `F(H_R(q1,q2))=H_R(Tq1,Tq2)` on all pairs—not even a discontinuous one. This refutes a naive global quaternionic one-step Hopf factor of PR333.

## 4. THEOREM HOPF-CHIRAL-2 — a pair of opposite handed Hopf charts REPAIRS the one-step map

Introduce a LEFT-gauge observer

\[
H_L(q_1,q_2)=\left(\frac{2\bar q_2q_1}{D}, B\right).
\]

It is unchanged by `(q1,q2)→(u q1,u q2)` for unit quaternion u. Both `H_R` and `H_L` are legitimate Hopf quotient spheres, but they use **different equivalence relations on the same pair**.

Because `T(qu)=L\overline{qu}r=(L\bar u L^{-1})T(q)`, common RIGHT gauge on the input becomes common LEFT gauge on the output. Similarly, `T(uq)=T(q)(r^{-1}\bar u r)`, mapping common LEFT gauge to common RIGHT gauge. Consequently, one genuine source step defines well-typed maps between **two** observational sphere charts:

\[
\boxed{
S^4_R\xrightarrow{\ \Phi_{R\to L}\ }S^4_L
\xrightarrow{\ \Phi_{L\to R}\ }S^4_R.
}
\]

With `r=(1-i-j-k)/4` and `L=i+k`, the exact coordinate formulas are

\[
\boxed{\Phi_{R\to L}(R,B)=(r^{-1}\bar Rr,B),
\qquad\Phi_{L\to R}(R,B)=(L\bar RL^{-1},B).}
\]

**Proof.** For example, after T, the left relative coordinate is

\[
\frac{2\overline{Tq_2}\,(Tq_1)}{D'}
=\frac{\bar r(2q_2\bar q_1)r}{|r|^2D}
=r^{-1}\bar Rr,
\]

because `D'=|L|²|r|²D`. The other direction is the same computation with left/right reversed. The result is a **handedness-indexed observer system**, not a claim that source J-parity and gauge handedness are literally the same grading. Both maps preserve the latitude B and conjugate its relative quaternion, so neither produces mixing by itself.

This is a precise categorical interpretation of the odd SUCC obstruction: it is a **pathway-gap for a single fixed Hopf chart**, repaired by supplying the missing orientation label. Do not use the words quantum collapse or physical handedness as if these algebraic results demonstrated them.

## 5. THEOREM HOPF-CHIRAL-3 — even steps descend to one sphere as a quarter-turn

The true two-step source map factors over rational Hamilton quaternions as

\[
\boxed{\iota(T^2x)=\frac14(1-k)\,\iota(x)\,(1+i).}
\]

This follows by composing the previous formula, or by exact basis calculation. Common right gauge is preserved at even steps. On the right Hopf sphere, its induced map is

\[
\boxed{\Phi_2(R,B)=\left(\frac{(1-k)R(1+k)}2,B\right).}
\]

In five real coordinates `R=r0+r1i+r2j+r3k`, this is simply

\[
(r_0,r_1,r_2,r_3,B)\mapsto(r_0,r_2,-r_1,r_3,B).
\]

Therefore `Φ₂⁴=I` on the WHOLE Hopf sphere. By composition, this is exactly `Φ_(L→R)∘Φ_(R→L)`. The 4-step source involution `T⁴=−J/4` projects to the half-turn `Φ₂²`; the 8-step source scalar return becomes the identity `Φ₂⁴` on the projective observation.

**New-to-SUCC mathematical result:** the signed chiral source really admits a quaternionic two-step Hopf transport. **Critical negative result:** this transport is a finite-order rotation, with no stand-alone route to Weyl cancellation or sphere equidistribution.

## 6. Source-grounded candidate Hopf observations and their tests

### C0. Consecutive decaying source states: a sharp NO-GO

`q_n=ι(T^n b)`, and define `H_R(q_n,q_(n+1))`. For any nonzero input x, `||Tx||²=||x||²/2`, hence

\[
B_n=\frac{1-1/2}{1+1/2}=\frac13.
\]

Thus **every** consecutive-pair state is trapped on a single latitude `S³⊂S⁴`. Since `T^8=I/16`, its projective observation obeys `H_(n+8)=H_n` exactly. The selected seed b visits only five distinct Hopf points in that eight-step cycle (computed by exact Fractions). This cannot be a dense or equidistributed S4 realization.

### C1. Chiral mirror: also confined to an equator

`H_R(ι(x),ι(Jx))`: J swaps/complex-conjugates carrier components and preserves norm, so `B=0` identically. An apparent second independent direction generated merely by the J mirror does not furnish the missing amplitude parameter.

### C2. Anchored carrier chart: genuinely lossless S4 compactification

Take `H_R(ι(x),1)` with a fixed quaternionic source gauge. It is the standard inverse-stereographic embedding of `R⁴` into `S⁴` minus the north pole. The **entire four-real-coordinate source state is recoverable**, not just the amplitude:

\[
\boxed{x=R/(1-B),\quad B\ne1.}
\]

Thus the original signed source readout is also recoverable. Pushing T through this chart and fixing the north pole at infinity yields a **global continuous sphere homeomorphism** (this is *not* the failed pairwise T Hopf quotient):

\[
F(\operatorname{Hopf}(x,1))=\operatorname{Hopf}(Tx,1),\quad F(\infty)=\infty.
\]

Since `det T<0`, the degree of this one-point-compactified real-linear homeomorphism is −1. Since `TᵀT=I/2`, its latitude satisfies the exact Möbius recurrence

\[
\boxed{B_{n+1}=\frac{3B_n-1}{3-B_n}.}
\]

For authentic b, `||T^n b||²=4/2^n`, giving `B_0=3/5`, `B_1=1/3`, `B_2=0`, `B_3=−1/3`, `B_4=−3/5`, `B_8=−63/65`. It converges to south pole `(R=0,B=−1)`; north is the second fixed pole. This is a source-faithful, autonomous S4 **compactification**, not a topologically dense source orbit.

### C3. The literal four signed poles: lossless but localized

Put `A_n=(4/(8n−7), −2/(8n−4), −1/(8n−3), −1/(8n−2))∈H_Q`, and observe `H_R(A_n,1)`. The decoder `A_n=R/(1−B)` recovers each of the four signed pole terms, hence the actual source r(n) by coordinate summation. The first pole declines as `O(1/n)`, so this sequence approaches the south pole; an elegant sphere representation alone gives no distribution of selected BBP phases. **Frame control:** permuting the four rational pole coefficients leaves the scalar r(n), Euclidean norm and Hopf latitude unchanged but changes the relative quaternion R. The assignment of labeled poles to i,j,k directions is a *declared geometric frame*, not canonically fixed by scalar BBP forcing. A genuine frame transport must be proved before treating a specific quaternionic component as source-invariant.

A signed-amplitude mutant `A_n→(|A_n^a|,|A_n^b|,|A_n^c|,|A_n^d|)` preserves `||A_n||²` and hence latitude B, **but changes R and the actual forcing**. The latitude by itself is sign-blind; the full relative quaternion is not.

### C4. Coupled pole/chiral mixed Hopf: nonconstant latitudes and source-labelled tomography

Choose the explicitly declared (NOT canonical) synchronous pairing

\[
q_1(n)=A_n,\qquad q_2(n)=\iota(T^{n-1}b),\quad n\ge1.
\]

Both components originate from the actual PR333 source, but pairing their clocks with this index relation is a **new modelling choice**, not a theorem of original BBP selection. A shifted pairing with `T^n b` uses the same source components yet produces a different Hopf latitude; this is an explicit **source-map adequacy** negative control.

The Hopf observable has variable latitude and generally four nonzero relative quaternion coordinates. For example,

\[
B_1=\frac{5543}{9143}>0,\qquad
B_2=-\frac{2366005}{3000083}<0,
\qquad B_{12}=\frac{31487968689047}{191601226426985}>0.
\]

**Exact tomography when source-companion q2(n) is retained:**

\[
\boxed{A_n=\frac{R_n\,q_2(n)}{1-B_n}.}
\]

This follows from `R=2q1\bar q2/D` and `1−B=2|q2|²/D` with nonzero q2, and preserves the original signed forcing. The Hopf observable alone does not identify the source-dependent gauge q2. Distinct pairs on its Hopf fiber can encode different signed four-pole records.

As `n→∞`, `||A_n||²=11/(32n²)+O(n^{-3})`, whereas `||q2(n)||²=4·2^{-(n-1)}`. Hence this mixed construction **approaches the north pole**, with `B_n→1`, `|R_n|→0`. It is algebraically nondegenerate in finite windows but still does NOT generate an equidistributed S4 path or establish π normality.

## 7. Hostile countermodels and closed claims

1. **Wrong algebra mutation**: multiplying source coordinates as Hamilton quaternions instead of `Q(i)×Q(i)` violates source ring structure: `(1,0)(0,1)=0` in the original ring, while `1·j=j≠0` in H. REFUTED as an algebra homomorphism.
2. **Wrong chiral successor**: replacing odd `v→g\bar v` by `v→gv` fails the exact source impulse taps and two-step factor. Tested.
3. **Same right gauge, different one-step images**: `(1,i)` and `(j,k)` represent one right Hopf point, but their T-images represent opposite quaternionic points `±k`. REFUTES the one-chart odd descent.
4. **Positive/equal amplitudes**: J-mirror B=0; consecutive T pair B=1/3. REFUTES the inference that four complex directions automatically fill S4 via the quaternionic Hopf observable.
5. **Signed-to-absolute pole mutation**: latitude unchanged, source readout altered. Refutes treating Hopf B as source-complete.
6. **Same forcing, different real seed**: For arbitrary seed c, `U_n(c)=U_n(0)+16^n c`. An exactly rational seed c=1/3 produces a persistent phase shift 1/3 modulo1; this proves a positive-source-only Hopf observer is insensitive to a genuine seed change, **not** by itself nonnormality. Stronger: by the pre-existing original BBP identity `Σ_{j>=1}16^{-j}r(j)=π/16`, choose the alternative (NONAUTHENTIC) real seed `c=−π/16`. Then

   \[
   U_n(-\pi/16)=-\sum_{k=1}^{\infty}16^{-k}r(n+k)\longrightarrow0.
   \]

   Indeed `0<r(j)≤8/j²` follows from the exact rational source passport (for j≥1, each denominator factor is bounded below by `j,3j,j,5j` and numerator bounded above by `120j²`); consequently `|U_n(-π/16)|≤8/[15(n+1)²]`. Its phases converge to 1: a genuinely nonnormal changed-seed orbit preserving **all four poles**. No Hopf observable depending only on the source decaying T and pole terms can distinguish it from the zero-seeded source unless actual U seed/carries are included.
7. **Frame/pairing controls**: Pole-basis permutation preserves scalar r(n) but changes quaternion R, and changing the source-partner time shifts mixed Hopf B despite using the same authenticated ingredients. Hence there is no unique source Hopf map without a declared frame and clock transport.
8. **No crossed-boundary promotion**: a source-faithful quaternionic observation is not a normality theorem. It lacks the selected signed estimate `Σ e(hU_n)=o(N)`.

## 8. Status / acceptance matrix

| Claim | Precise boundary | Status |
|---|---|---|
| T matrix, original taps, four source poles, T8, signed chiral split | PR333 source reconstructed in local exact rational code | DISCLOSED (source algebra; from PR333) |
| TᵀT=I/2, det T=−1/4, T=L conjugate(.) r | Exact 4×4 source-derived matrix | DISCLOSED (new-to-local bridge) |
| Odd T fails right-Hopf self-descendance | Explicit exact two-pair counterexample | REFUTED as a universal self-map |
| Odd T exchanges right/left Hopf gauges | Two exact relative-quaternion formulas | DISCLOSED |
| Even T² descends to an order-four Hopf base rotation | Exact Hamilton factor and exact composition | DISCLOSED |
| Consecutive source Hopf latitude 1/3, 8-cycle | Whole nonzero source E and selected seed | DISCLOSED |
| J mirror Hopf equator | Whole E | DISCLOSED |
| Lossless stereographic Hopf lift and Möbius latitude | One chosen source anchor, not intrinsic Hopf gauge | DISCLOSED |
| Four signed poles reconstructed from anchored/mixed Hopf | Given exact authenticated companion state | DISCLOSED |
| S4 dense/round-Haar normality from authentic BBP | Selected expanding zero-seeded U_n not coupled with any proved signed saving | UNVERIFIED |
| Quaternionic physics / quantum collapse / unique natural SUCC S4 | No source identification or physical test | UNVERIFIED; do not claim |
| Code tests | 34 exact standard-library unit tests + independent SymPy oracle | OBSERVED locally, scope-limited |

## 9. Next verdict-changing probe after Claude completes Main XII

**Minimum acceptable future research theorem:** Construct a typed, source-preserving joint map from **the actual** `n,U_+(n),U_-(n)`, four signed poles and real zero-seed/carry data into quaternionic blocks `(q1(n),q2(n))` with a measurable *nontrivial* source-specific covariance/character identity. Prove that its chosen left/right Hopf change of charts actually intertwines the declared source action. A candidate may succeed only if it exposes information unavailable to the matched-forcing changed-seed source and to normal finite-type countercontrols.

Predeclare controls: authentic source `U_0=0`; changed seed `U_0=−π/16`; exact rational finite alternative `U_0=1/3`; sign-mutated poles; wrong odd chirality; independent-partner/no-ghost mutant; mirrored equal-norm constant-latitude control; synthetic Pisot torus (good cancellation but not authentic source). Record output for **all** and seek a signed Weyl saving for the authentic expanding orbit, not the shrinking impulse or a synthetic torus rotation.

**Integration protocol:** Recheck current main head, branch ancestry and repo instructions when Claude finishes. Keep this note additive and branch-independent until the owner authorizes integration. Do not silently modify original-source definitions, PR333 lemma names, historical proof contracts, formal receipts, or main. If a future PR is opened at user's request, pin input SHAs and include fail-controls and full repo CI; this local dossier is a starting point, not an authority upgrade.

## Reproducibility

- `python -m unittest -v test_hopf_source.py` — 34 focused local tests (Fraction exact; 0 external runtime dependencies).
- `python oracle_sympy.py` — independent Gaussian sector derivation, matrix, determinant, source taps, T² factor and Hopf rotation (SymPy required).
- `python make_receipt.py` — JSON scope/claim summary and sample rational Hopf coordinates.
- SHA-256 byte manifest and raw logs are bundled in the local ZIP. Scripts did not access network or mutate the GitHub repository.
