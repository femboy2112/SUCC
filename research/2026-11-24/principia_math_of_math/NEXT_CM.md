# Next proof cuts — CM period and automorphic theta reconstruction

**Research state (2026-11-24):** current Principia Genesis draft #690 now contains a genuine Gaussian \(\mathbb Z[i]\) theta finite-shell two-place construction (CM_THETA_TWO_PLACE.md T9–T14), plus an exact local coordinate sign discriminator and a certified Gaussian analytic completion theorem. The **automorphic theta-lift/period object occurring in the published Alpöge–Claude RH proof is NOT YET reconstructed**.

## A. The actual missing object and acceptance criteria

Recover the source-exact *automorphic* CM theta-lift kernel from the original published theorem / exposition, not a Gaussian shadow, a simple Jacobi theta function, or the illustrative lemniscate. For each component, pin its definition, domain, normalization, and mathematical dependency:

1. **CM carrier and integral structure**: actual quadratic characters, CM field, model of the relevant elliptic/formal group(s), theta space, algebraic coordinate rings, coefficient integrality lattice, and bad-prime places. Prove the coordinate choices and the actual Frobenius unit and coefficient denominators.
2. **Source-labelled lift**: source/target modules, repeated theta/period lift maps, composition and coupling laws, and faithful realization into conventional automorphic arithmetic. Determine precisely which lifts survive into a nonzero joint map.
3. **Local arithmetic**: on the *actual* theta coefficients or minors, prove increasing \(p\)-adic valuation under a declared inert prime and chosen Hasse/divided differential. Include the total loss of all coordinate changes, denominators and exceptional places. An auxiliary Honda formal model does not suffice without a certified source map.
4. **Real side**: on the **same** map/minors, derive source-based Petersson/period norm, determinant/covolume, slope, and normalization bounds; pay the effect of analytic theta Gaussian/period factors, conductor, and product formula.
5. **Nonzero/rank**: prove that accumulated maps contribute enough independent image directions, rather than dependent zero paths; recover rank via the same trace/period geometry employed by the proof.
6. **Global mathematical consequence**: derive the fully quantified, weighted one-sided prime inequality (M) with correct character/prime weights and error terms; then reconstruct the usual analytic RH consequence. No zero ordinates as inputs, no \(RH\) as a hidden premise.

### Pass conditions for one native CM milestone

Construct a **nonzero actual period-map minor** \(\Delta\) whose source passport pins the published theta-lift kernel and whose independent local and real-side realizations satisfy
\[
0 < \prod_{p}p^{e_p} \le |\Delta|_{\mathrm{arith}} \le \operatorname{HeightBound}_{\mathrm{real}}
\]
with each real/p-adic comparison justified by an explicit basis, integral lattice, embedding/period and denominator budget. If \(\Delta\) is algebraic nonrational, replace the naive integer inequality by the *correct absolute norms/product-formula/covolume statement* for the field of definition; no untyped transfer from \(\mathbb Z\).

The first native reconstruction need only recover a *finite honest fragment* of an actual lift: one nonzero input and output coefficient, one genuine local valuation and the matching real period/norm. It is a useful theorem if verified; it is not RH without global estimates.

## B. Work in a source-first dependency order

**Cut 1: published definitions / provenance.** Pin primary theorem labels/Lean paths, distinguish the illustrative \(y^2=1-x^4\) from actual automorphic theta lifts, and write a typed source/target/period diagram. Read exact primary code and paper; source authors are not substitute proofs but identify targets.

**Cut 2: the local formal-coordinate sign.** T13's \(-7/24\) obstruction shows that the auxiliary \(+\) Honda series cannot silently represent the actual lemniscatic logarithm by an integral strict coordinate, whereas the first \(-\) sign coefficient \(3/8\) is integral. Extend this *particular* coordinate comparison with a theorem (not just degree-40 finite checks), preferably using the appropriate CM Frobenius trace/unit and \(p\)-typical formal-group isomorphism. Do not assert all-order integrality from finite data. Then determine whether this local comparison is actually the one needed by the *automorphic* kernel.

**Cut 3: theta normalization and denominator ledger.** Already T11 proves that a Gaussian-weighted determinant incurs exactly \(q^{\sum n_i}\). Repeat with the actual theta-period input and every algebraic/real normalization. Track under composition, including conductor and the source's exceptional primes.

**Cut 4: actual lift plus rank.** Build one genuine nonzero period pairing and then independent lifts, using source-compatible Yoneda/knowledge-volume maps to prevent double-counting. Rank counts are proof-dependent, not just object names.

**Cut 5: (M).** Recover every quantifier, character and window and the exact exponents \(X/m,Xm/k,m,k/n^2\) from the published sources. The equality/reconstruction must preserve actual positive and signed arithmetic terms, not merely a final square-root-shaped bound.

## C. Exact hostile controls to predeclare

- Simple theta negative control: \(v_3(r_{30})=14<45\). If native transport claims full multiplicity for it, the transport is false.
- Wrong Honda/Frobenius unit: the \(+\) candidate already has \([T^9]h=-7/24\), \(v_3=-1\); \(-\) candidate has \(3/8\), \(v_3=1\) only at the first test.
- Split and fake primes: \(p=5\) and composite \(15\) cannot be inert-source substitutes.
- Identical period columns yield determinant \(0\); count *actual* independent lifts.
- Dropping Gaussian period/heat normalization changes the determinant by a known factor; false “no-cost” transport must fail.
- Bad reduction \(p=2\); changed theta coefficient at composite \(n=6\); wrong conductor, character parity, or Gamma factor.
- A same-shaped Gaussian theta kernel can fail the CM arithmetic lift condition. Do not treat matching source labels or low-order Taylor coefficients as integrality certification.
- With \(F=0\) all divisibility conditions hold vacuously; any capacity contradiction requires *nonvanishing*.
- Finite-source truncation for the completed theta must carry a proved uniform analytic tail, and signed limit operations need valid Fubini/normality hypotheses.

## D. Research authority ladder

**DISCLOSED:** Principia T1–T14 elementary results and correct imported/classical prerequisites under their stated boundaries; genuine Gaussian theta source and nonzero *finite shell* CM matrix with both local valuations and real norms; explicit normalizer; analytic completion; finite Honda sign obstruction.

**OBSERVED:** exact computations and local focused tests; independent SymPy/80-digit checks with the latter strictly numerical.

**CONJECTURED:** that the full automorphic RH proof's mathematical content can be reconstructed through Principia's source/path/null/knowledge-volume semantics, giving the same mathematics under a faithful realization.

**UNVERIFIED:** an actual automorphic theta-lift CM integral source, independent period-map minors, Petersson norm and conductor budget, global trace-formula rank, the exact (M), and full native RH semantic reconstruction.

**Boundary:** the published external Lean theorem stands independently. No new independent RH proof is claimed, and this reconstruction does not change its authority. Do not merge main until AGENTS.md full gates are run and reviewed.

## D2. The new quantitative source-coupling obligation

COUPLING_MASS.md T21–T25 proves that a behavioral quotient preserving output and target labels is insufficient for arithmetic/analytic quantitative semantics unless the **source weights and complete target-relevant interaction tensors** descend. This is not an imported claim of Weil positivity; it is an exact finite pushforward theorem with hostile failures.

For an actual automorphic theta-period candidate:
- Pin original source paths and the full signed coefficient/kernel or appropriate higher multilinear source data; distinguish original inputs from fitted test values.
- Before discarding any null path, show its contribution to the *actual target functional and period norm* is source-redundant, or transport its pushforward coefficient and cross terms explicitly.
- Check nonzero determinant and rank under that same compression, with actual integral-coordinate maps, p-adic valuations and Archimedean normalization paid.
- Test whether two source histories can have the same observable and pairwise projections but different higher-order theta-lift relationships. If so the toolkit requires higher coupling order or source restrictions; the parity family in T23 is a precise adversarial template.
- Prove finite-to-infinite completion in the actual analytic topology; a finite tensor identity is not a global uniform estimate.

**Acceptance:** recover, from native SUCC source/path/coupling operations, a mathematically valid original-theta-lift period-map coefficient AND its integral and real pairing on the same source. The finite Gaussian shell proof is a prototype, not this acceptance.

## E. Priority for future research rounds

First work on source authenticity and **one actual automorphic period coefficient**, not arbitrary generalizations. If an advertised map fails at the first p-adic unit, retain that failed receipt and try the correct sourced unit. Only scale to global rank and inequalities after the same object passes local and real normalization tests. Preserve every prior PR/branch and exact source.
