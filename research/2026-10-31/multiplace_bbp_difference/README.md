# Operation BBP Three-Place Difference — Gamma resolvent and arithmetic prime exposure

**2026-10-31. Research-only, stacked on PR #429 head 33d53f576fe2c2e847e51c24ccf7a94aa6ec6f10.** Original four signed BBP poles, selected U_0=0, production, frozen archives and main unchanged. π normality and RH remain OPEN.

The user's hypothesis: represent BOTH r(x) and r(y) by infinite series in a common mathematical carrier, and see whether their difference produces new faithful arithmetic realizations. **This round succeeds on a precisely declared domain**, with a genuinely common rational resolvent expansion converging in the real, 2-adic and 3-adic metrics, including an exact finite remainder.

Highlights:

- **TD-01/02:** The ORIGINAL four-pole BBP source has a positive integral with factor \(P(t)=(1-t)(t^2+2)(t^2+2t+2)\). Rational coefficients \(C_j(y)\) are literal Archimedean Gamma moments. The expansion \(r(x)-r(y)=\sum_{j\ge1}(8(y-x))^jC_j(y)\) has an exact rational remainder at every depth.
- **TD-03:** Real/2-adic/3-adic convergence conditions are all stated and effective; same rational coefficient sequence, separate metric-specific remainder budgets.
- **TD-04:** Genuine original-source 3-adic exact sharp valuation \(v_3(r(y-6^m)-r(y))=m-2d(y)\) for m>d(y), with d(y) the MAXIMUM individual pole depth. This upgrades the loose combined-denominator estimate in PR #429 to an exact equality with a weaker onset. All four original signs survive a nontrivial colliding-pole cancellation test.
- **TD-05/07B:** Deep 3-adic poles have exact density 4/3^k for k≥2 and mean depth 5/3. Their depth statistic and original zero-seed 2-adic BBP residue factorize **exactly** on CRT time blocks. Removing deep poles changes ANY normalized selected real Weyl sum by ≤4/3^k+4/N; thus deep poles alone cannot carry persistent nonnormality.
- **TD-06:** Same rational Δ_m=r(1)−r(1+6^m) converges to 47/15 in the reals but to 0 at p=2 and p=3 with v₂=m, v₃=m−2. Reduced denominators ALWAYS have one factor5, no factors2 or3, and obey \(B_m>(5/141)6^m\). This is a rigorously quantified, source-specific complementary-prime exposure.
- **TD-07:** Positive Gamma-moment resolvent has genuinely NONCOMMUTING finite-observer depth and arithmetic horizon limits in the real metric: 47/15 versus 0. The first nonzero coefficient fully detects local p-adic valuations but is asymptotically negligible in the real metric. This is why declaring a completion protocol is load-bearing.

The results do NOT supply the selected four-pole/zero-seed signed phase cancellation needed for π normality, nor a Weil positivity/RH theorem. Existing SUCC DSI source isometry and earlier SUMMATION SNAPSHOT ARROWS are credited. No academic priority claimed for classical Gamma/geometric/CRT facts.

Read [full mathematics](PROOF.md), [claims](CLAIMS.md), [next proof gate](NEXT.md), [validation](VALIDATION.md), [exact Python probe](multiplace_difference.py), and [22 discoverable root regressions](../../../tests/test_multiplace_bbp_difference.py). No release or main merge authorized.
**TD-07C — source-specific limit obstruction:** The authenticated BBP r has actual 3-adic pole singularities. Although every fixed integer y has r(y−6^m)−r(y)→0 3-adically, its average p3 absolute norm over good classes is exactly 4/3−7/3^m→4/3. More sharply, for fixed m the normalized norm average over y mod3^K grows at least (2/3)(K−m−1). Thus the bounded real Weyl phase can disregard deep poles, but an unbounded p3 magnitude observer cannot: it fails uniform integrability. Two additional finite tests check this. Total 24 new tests.
