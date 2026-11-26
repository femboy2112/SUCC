# RH as an adversarial theorem oracle — continuation, height cancellation and carrier capacity

**Scope:** SUCC's mathematics of mathematics, not an RH proof. Use the verified external Alpöge–Claude argument as a semantic test of the proposed observer framework. The actual automorphic arithmetic realization is not implemented here.

## O0. Sources inspected and their authority

Original formal source: leanprover-community/riemann-hypothesis commit 40e56bab026552e089d7afcfeff08d2defb9c005, [Main.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean) and [CharacterBoxes/MainConclusion.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean) read directly. The original proof exports RH and four Dirichlet-L statements; the central original conclusion uses a row construction and window estimate. Do not confuse Dirichlet GRH with all automorphic L-functions.

New compact rewrite: lsernau/grh-lean commit 72fead102f663d5c7a407964a13dc0cf9d977207 (November 25 release line). [Rubinstein verification and status](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/) reports November 26 that the compact proof compiled all 794 modules, used only Lean's three standard axioms, and comparator matched the five target statements and was accepted by six kernels. These are **reported external verifications**, not a rebuild in this SUCC round. The linked November 22 human-readable exposition is explicitly a working conditional reduction of its main inequality, not a replacement full conventional proof. Prefer the compact primary source for this audit. The following files were fetched by commit and their theorem declarations inspected:

- [Main.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Main.lean): five exported statements, uses New.grh.
- [New/Main.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Main.lean): star_inequality, eventual one-sided primeError, GRH. Primary proof spine.
- [New/Heights/Heights.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Heights/Heights.lean): HeightLe; nonneg for constant family 1.
- [New/Heights/OneDeterminant.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Heights/OneDeterminant.lean): height for a Gram determinant ratio, after extending a linearly independent family to a basis.
- [New/Exchange/ExchangeTheorem.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Exchange/ExchangeTheorem.lean): exchange_theorem.
- [New/Exchange/RowsReached.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Exchange/RowsReached.lean): weighted lift chain / restriction adjoint pairing.
- [New/Curve/KatzDivisibility.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Curve/KatzDivisibility.lean): katz_divisibility_limit.
- [New/Rows/GluedFormTheta.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Rows/GluedFormTheta.lean): depth_indicator_jet.
- [New/Rows/SparseThetaSum.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Rows/SparseThetaSum.lean): isolation and size bounds.
- [New/Rows/RowVolume.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Rows/RowVolume.lean): volume_iota_eq_prod_liftVolume.
- [New/Rows/LiftVolumeHeight.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Rows/LiftVolumeHeight.lean): heightLe_liftVolume_ratio.
- [New/Endgame/ShortAndEnough.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Endgame/ShortAndEnough.lean): short_forms, enough_forms, IndexLe.
- [New/Endgame/LongForms.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Endgame/LongForms.lean): heightLe_volume_ratio_sq, heightLe_volume_rows, integral_forms_long, exists_family_covolumeSq_le.
- [New/Endgame/OneSidedCriterion.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Endgame/OneSidedCriterion.lean): IsPolar.exists_window_sub_mul_le, entireL_ne_zero_of_primeError_le.

The exact declarations provide a stronger falsification oracle than word association with zero, entropy, Gamma, primes or determinants. This audit is selective, not a full dependency closure or an independent referee report.

## O1. Steelman → crucible → refine against actual proof objects

**Coherent continuation.** The actual exchange theorem compares theta integrals on complementary rank unitary groups for matched partner data, with a nonzero factor c and squared norm tied to conductor/L-value data. The rank and signature hypotheses, matched ramified data, and constant are essential. RowsReached uses a weighted adjoint pairing along a lift chain. This is a typed bridge between observations, not equality of arbitrary reports. Refine: every SUCC transport edge should carry a genuine partner map, nonzero normalization, and cost; mere shared carrier does not give a path. The universal statement that all common-source observers are connected is refuted by I2's disconnected fibers.

**Null constraints and nonvanishing.** Katz sharpness is an existential *lower p-adic magnitude* for some invariant derivative, i.e. a ceiling on achievable divisibility for a live jet. GluedFormTheta depth_indicator_jet chooses a single nonzero algebraic normalizer t with a uniform conjugate bound, and for each prime/place finds a suitable indicator jet at the prescribed multidegrees. It does not assert every jet at each depth is maximally divisible, nor that the same jet works at all primes. This is decisive against an indiscriminate "higher null means greater truth" claim. Refine: lower divisibility bounds, upper valuation/live-witness bounds and common normalizer must be separate contracts. The actual CM datum is not the simple Gaussian shell of #690; the earlier negative control v_3(r_30)=14<45 remains pertinent but illustrative. Book VII I4/I6 provide a native analogue: each new independent null costs complexity and a next witness stays nonzero; they do not prove Katz's theorem.

**Knowledge volume and rank.** short_forms supplies small lifted forms spanning columns with an index cost; enough_forms supplies a quantitatively near-spanning family of translated column images in rows. It is not enough to count labels or paths. one_determinant requires independent vectors completed to a basis, nonzero comparison factors and integrality of pairings; it retains twice the index and completion costs. Refine: observer rank/knowledge volume must be attached to actual maps and a nonzero exterior/Gram object. A duplicated column kills the determinant while preserving labels, a direct hostile control.

**Global coupling and seam.** HeightLe bounds a family y indexed by finite places through ONE nonzero normalizing H, a bound on its conjugates, local bounds on H y_iota, and an eventual sum of these costs. Its nonneg theorem for the constant family 1 uses the product formula. LongForms combines squared reciprocal ratios of the *same* volumes; the product is 1, and the sum of certified bounds cannot be negative. This is the structural obstruction. It is not a real-continuous IVT argument and must not be re-described as one. Refine the theorem program: the role of a necessary seam can be played by a nonnegative global capacity after transported cancellation, even on a disconnected/multi-place carrier; existence of the actual comparison family and each budget must be proved.

## O2. Native rational height-patching lemma (CLASSICAL / PROVED)

Let a finite family y_p∈Q^× be indexed by primes p, extended by 1 outside finite support. For one nonzero rational H, let A≥|H|∞, B_p≥|Hy_p|_p, with B_p=1 outside finite support and all quantities positive. The usual normalized p-adic absolute value is |q|_p=p^{-v_p(q)}. The rational product formula |H|∞∏_p |H|_p=1 follows directly by prime factorization. Therefore

\[
C(y;H)=A\prod_p B_p\ \ge\ \prod_p |y_p|_p.
\]

The optimal C over such certificates equals the right side (take H=1 and exact bounds). If y_p z_p=1 for every p, any two certificates, even with DIFFERENT but individually globally shared H_y and H_z, obey C_y C_z≥1. More generally C_{yz}≤C_y C_z for the product certificate with H_y H_z; no uncoupled place-specific normalizers may be substituted without paying their cost.

**Crucible:** on the constant family y=1 choose fake local normalizer H_2=2 and real normalizer H∞=1, others 1. This reports apparent product bound 1/2. It is invalid: with one H=2 the real factor is at least 2, restoring 1. Similarly dropping an omitted denominator prime or using distinct untwisted/twisted source passports can fake a negative height. This finite model is exact, not an approximation to a completed zeta kernel. The actual HeightLe is over algebraic/p-adic embeddings and conjugates with eventual prime sums; importing its full theorem needs number-field norms and its precise field maps. No claim that the toy realizes its automorphic y_iota.

For a single nonzero integral determinant d, with v_p(d)≥e_p≥0 for a finite set, |d|≥∏p^{e_p}; if |d|≤U and U<∏p^{e_p}, the proposed certificate is impossible. For rational determinant d with known clearing denominator D, apply to Dd and include v_p(D) and |D|. Never mix an integral object and a smaller analytically normalized object without transporting its scale. This is the exact arithmetic obstruction in #689 and #690, now placed alongside the reciprocal-family form from the real proof.

## O3. Native coherent path volume theorem (CLASSICAL / PROVED)

Let V_0 be d-dimensional Euclidean/Hermitian, let T_i:V_{i−1}→V_i be linear maps injective on the transported image E_{i−1}=T_{i−1}...T_1 V_0, with E_0=V_0. Define J_i as the d-dimensional volume dilation of T_i restricted to E_{i−1}, using the induced metrics. Then

\[
J(T_m\cdots T_1)=\prod_{i=1}^m J_i>0.
\]

Proof choose orthonormal bases of each E_i; the restricted matrices are square d×d and multiply, so absolute determinants multiply. Equivalently for a transported full-rank frame B_i=T_i B_{i−1} let G_i=B_i^*B_i. Then J_i²=det(G_i)/det(G_{i−1}), and the ratios telescope. This version is valid in exact rational real matrices, with no square-root evaluation. A rank failure makes the full d-volume zero and prevents this ratio contract. For a rank-one line E_0 embedded along e_1, ambient diag(2,3) gives dilation 2, not ambient determinant 6. This refutes using ambient or summed local volumes instead of the retained subspace.

Actual RowVolume theorem factors a particular chain's nonzero volume into individual lift volumes times a controlled factor (CostSquares). It must also prove its relevant good-form spaces and lift normalization match. O3 supplies a native minimal mathematical interface for the algebra of transported volume, not those hard identifications. It suggests storing the entire transported wedge frame or sufficient Gram witness in the observer state, not just individual norms.

## O4. Recover the real endgame budget (CLASSICAL algebra, primary source application conditional on actual imported hypotheses)

In compact New/Main.lean, star_inequality states m·remainder ≤ (log b)^2 budget. Read d=rowDim>0, n=number of independent short rows, n≥(1−4/b²)d and n≤d, L=log b·budget, h=mainHeight, R=remainder. LongForms supplies same-family upper bound V≤n(h−mR+L) and lower bound d(h−3L)≤V+2δ, where δ is the logarithmic index bound. The proof also has −(h−mR+L)≤H=b² x^99 and δ≤5d log(1+b²) budget.

General lemma: if n≥(1−η)d, n≤d, −w≤H with H≥0, w=h−mR+L, d(h−3L)≤V+2δ, V≤n w, then

\[
mR\le4L+\eta H+2\delta/d.
\]

Indeed n w=d w−(d−n)w≤d w+ηdH. Combine the bounds and cancel dh, divide by d. This gives in the actual notation

\[
mR\le4L+4x^{99}+10\log(1+b^2)\operatorname{budget}.
\]

The remaining scale domination in New/Main.lean gives the displayed star_inequality. We have reconstructed this algebraic cancellation exactly and identified its actual theorem-bearing inputs, not independently proved Short/Enough/LongForms or the scale bounds. Do not replace the one-sided remainder inequality by an absolute-value estimate: a very negative R need not be excluded by these hypotheses. Do not drop the missing-rank term: n<d and w negative changes the direction of the comparison. No use of zero coordinates of zeta in this construction.

Finally the proof uses a good second scale within a long window and a Landau-type one-sided analytic criterion, then functional equation for zeros on the line. The actual prime-error definition and auxiliary-character conditions in New/Endgame/OneSidedCriterion.lean are essential. Neither a finite seam nor the product formula alone excludes a zero.

## O5. Refined SUCC architecture and concrete next gates

The author's intuition survives in a stronger typed form:

1. Passport σ and source-coupled memory → legal observer/partner relation → jointly compatible family. Separate existential path from robust all-world strategy.
2. Declared signed transport → scalar separating seam or independent-dimensional null forcing (I3–I5); or source-specific local algebraic jet constraints. Separate observed zeros from arithmetic multiplicities.
3. Nonzero retained witness with a quantified rank/capacity filtration, including a live witness bounding achievable divisibility (Katz direction). No label counting.
4. Same-source arithmetic and real realizations with explicit denominator/normalization/level/index costs, including all-place family coupling.
5. Global certificate after canceling the common main contribution; one-sided bound with uniform parameters; independent analytic exclusion. A mathematical source certificate is not automatically a physical execution.

Concrete next vertical slice for #690 M4–M10: reconstruct compact New/Curve/KatzDivisibility on its actual CMLattice d (prime d≡7 mod 8), phiSeriesRing and place hypotheses, including both forced divisibility and live-jet upper valuation. Then reconstruct GluedFormTheta depth_indicator_jet quantifiers and common t with conjugate bound. Connect to IndexLe and one_determinant through actual comparison forms, not a fitted Gaussian shell. Use exchanged theta partner and weighted adjoint identities to certify rank-preserving continuation; derive volume ratios on exactly the selected rows, and reproduce LongForms cancellation. The compact proof gives explicit node names and much smaller audit surface than original #687 M0–M11. Keep #690's Gaussian and Honda controls, source-map mutation, duplicate rank, wrong place/sign, missing conjugate, missing denominator, vanished determinant and one-sided-sign mutants. This is a pathway/probe design, not a declaration that any missing theorem is already native SUCC.

For π: the theorem to target is still the genuine zero-seed BBP chronological carry family under hypothetical R0 failure, with explicit source/phase and real/arithmetic transport. Hobby–Rice freely creates nulls for generic positive measures, so it cannot distinguish π's digits. Seek an unavoidable null of a specifically selected, provably nonzero bounded arithmetic object, or a genuine one-sided bound after paying all costs. B3 establishes a real arithmetic obstruction for one chart, but not the required forcing from R0. No normality claim.
