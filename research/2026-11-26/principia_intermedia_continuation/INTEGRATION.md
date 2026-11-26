# Integration with Principia Intermedia #691

The concurrent draft [#691](https://github.com/femboy2112/SUCC/pull/691), inspected at `863952de0eb4d7a039fea73f10606203308635ea`, was discovered while publishing this continuation. It is preserved in full and is the stacked parent. Its Book VII and source-specific arithmetic results are complementary to this supplement; shared classical premises do not make the two dossiers independent mathematical witnesses.

## 1. Three different meanings of a null

| Construction | What varies | Null statement | What it does not establish |
| --- | --- | --- | --- |
| PS-01 arithmetic observer path | The absolute value on a fixed rational carrier | At the trivial observer, log nu(q)=0 for every q!=0, so nu(q)=1 | q is zero; ordinary magnitude is zero; real and p-adic completions are identified |
| #691 B3/B6/B7 source-cut path | Rational cuts and their nonzero rational residual D, with normalized places fixed | Real completion can have D=0, while rational approximations have real absolute value tending to zero | Simultaneous smallness in the fixed p-adic observers |
| BM-02 source moment field | A polynomial readout P_N on the fixed positive source measure | Its first N integrated moment channels vanish | P_N is pointwise zero, is a chronological carry field, or identifies the canonical homogeneous seed |

At the PS-01 seam nonzero magnitudes equal one; in B7 the real magnitude tends to zero. Those are different relative-zero axes. PS-01 suppresses place exponents and has singular inverse conditioning; B7 keeps the place normalizations fixed and pays for small real magnitude through the product formula. The two statements reinforce the need to declare the readout and normalization before claiming a common null.

The source-retaining graph transport in PS-02 includes q itself. It is a coherent transport of marked observations; it is not an inverse reconstructed from magnitude alone. The trivial magnitude observer still distinguishes q=a by testing nu(q-a)=0. Even its information loss is relative to the allowed observation family.

## 2. L1 sign partitions and L2 polynomial fields

Both dossiers use the same unweighted forcing measure mu, obtained from Q(t)dt by u=t^8. The weighted measure lambda=mu/(16-u) in #691 is an additional, explicitly different readout.

| Feature | #691 Book VII I4–I7 | This supplement BM-02–BM-06 |
| --- | --- | --- |
| Extremizer | Monic polynomial P_N^(1) minimizing integral abs(P) dmu | Monic polynomial P_N^(2) minimizing integral P^2 dmu |
| Field with null moments | sign(P_N^(1)), taking values +/-1 | P_N^(2), taking variable real values |
| First N null equations | integral u^k sign(P_N^(1)) dmu=0 | integral u^k P_N^(2) dmu=0 |
| Forced complexity | Exactly N switches; unique minimal partition up to global sign | Exactly N simple interior roots; unique monic polynomial |
| Limit obstruction | Infinite binary simultaneous null is impossible; finite fields can converge weakly | Monic norms decay; unit normalization gives an orthonormal weak-null family with no strong convergent subsequence |
| Arithmetic application | Rational cuts, denominator depth and place-valuations of signed integrals | Coefficient lattice, inverse Gram matrix and a paid residual threshold |

Already at N=1 the seams differ. P_1^(2)=u-530/12831 is centered at the mu mean. The L1 sign seam is the mu median. In the original t-coordinate, A_0(1/2)=3763/1920>47/30, so the median has t<1/2 and hence u<1/256. Meanwhile 530/12831>1/256. This is an exact separation control, not a notation choice. A median in t, its image in u, a weighted-lambda median, and a centered-moment mean must not be substituted for one another.

## 3. The actual BBP arithmetic compensation law

The preserved [BBP place-completion supplement](../principia_intermedia/BBP_PLACE_COMPLETION.md) proves, for the same nonzero rational source residual,

\[
 |D(t)|_\infty\prod_p|D(t)|_p=1.
\]

Consequently a real-null approach forces growth in the product of finite-place magnitudes. An arbitrary sequence need not have a single fixed divergent prime. On a reduced p-power grid of denominator depth e, p!=5, its exact valuation is

\[
 v_p(D)=-6e-v_p(15).
\]

This is a genuine original-BBP specialization of the arithmetic capacity principle in PS-05. It is stronger than an untyped seam analogy, while remaining a source-cut result rather than a chronological R0 implication. The integration reran the inherited exact Fraction oracle successfully; the raw output is retained in validation/inherited_two_place_recheck.json.

## 4. Compact RH is the more structured oracle

The preserved [#691 compact oracle audit](../principia_intermedia/RH_ORACLE.md) is the canonical source-specific treatment of the compact external proof. This supplement's [RH_ORACLE.md](RH_ORACLE.md) records the broader theorem-guide comparison and basic countermodels.

In the compact development at `lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`, `HeightLe` is a condition on a **place-indexed family**, not an assertion that every local entry equals one rational scalar. The entries can differ. One nonzero global H per certificate, bounds at all required complex and p-adic embeddings, and a prime-sum budget provide the common normalization. `HeightLe.mul`, `HeightLe.pow` and `HeightLe.nonneg` make the accounting compositional. The endgame multiplies reciprocal volume families to a constant and uses nonnegative height after paying the rank and index terms.

Primary code: [Heights.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Heights/Heights.lean), [LongForms.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Endgame/LongForms.lean), [Main.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Main.lean).

The rational product formula in PS-05 and B7 is an elementary specialization of this accounting principle. It is not the full `HeightLe` contract or a replacement for the actual integral period maps, paired lifts and volume estimates. No external Lean build was performed here.

## 5. Combined verdict and next discriminator

We now have constructive compatibility tests, necessary crossings, exact source-null fields, minimal signed partitions, and two distinct arithmetic capacity mechanisms. The next application still must derive the null constraints from the actual zero-seeded chronological source/carry counterhypothesis on a provably nonzero object. Free observer choices do not supply that implication. The two dossiers give stronger instruments for testing a proposed implication, not permission to assume it.
