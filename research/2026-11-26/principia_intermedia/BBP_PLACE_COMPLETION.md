# BBP place-completion supplement: a real null forces arithmetic compensation

**Status: PROVED PAPER.** Same original unweighted BBP source as B3/B4, no seed/carry modification. This is a stronger exact source-specific sequel to Book VII's multiple-place boundary. These are rational source-cut observers, not digit or physical path observables.

## B6. Deepest-cut congruence and irrationality of every even moment median

Let t_i∈Q∩(0,1), ordered distinct, initial sign ε. Use the actual A_k and M_k of BBP_TWO_PLACE B3. If all t_i have odd denominators, B3 applies. Otherwise set e=max_i(−v_2(t_i))≥1, a_i=2^e t_i∈Z_(2), d=8k+6. Multiplying the signed primitive identity by 2^{ed} gives the exact congruence in Z_(2):

\[
2^{ed}M_k\equiv-\frac{\epsilon}{4k+3}\sum_i(-1)^{i-1}a_i^d\pmod{2^{e+1}}.
\]

Proof: in 2A_k the highest power has odd coefficient −1/(4k+3); the remaining degrees are d−1,d−2,d−5 with coefficients respectively −2/(8k+5), −1/(2k+1), 8/(8k+1). After scaling their valuations are at least e+1, 2e, 5e+3, each ≥e+1. The total source moment is 2-integral and its scaled term vanishes modulo 2^{e+1}. This proves the congruence, without assumptions on the number of cuts or their individual odd denominators.

The number of deepest cuts (those with v_2(t_i)=−e) must be even for a null; if odd, the right side is odd, so v_2(M_k)=−e(8k+6) for EVERY k≥0. An even count is only necessary, not sufficient; the higher congruence retains their signed powers. If all cuts are odd-denominator, even k has valuation zero (B3).

**Corollary:** for every rational single cut t and every even k≥0, the genuine signed moment cannot vanish:

\[
v_2(M_k)= (8k+6)\min(0,v_2(t)).
\]

For even-denominator t it has negative valuation even for odd k. Hence the unique real median of the unweighted k-th moment is algebraic irrational in the original t-coordinate for every even k: it solves the nonzero polynomial 2A_k(t)−r(k+1)=0, and no rational t solves it. This strengthens B4 from k=0 and rules out the attempted even-denominator single-cut repair. It does NOT assert irrationality of t^8 or of the weighted λ median, nor rule out arbitrary even-depth multi-cut partitions.

## B7. Archimedean approach to the seam forces non-Archimedean growth

Let D(t)=2A_0(t)−47/15. For rational t, B4/B6 give D≠0. The rational product formula gives the exact identity for this SAME source residual:

\[
|D(t)|_\infty\prod_{p}|D(t)|_p=1.
\]

Therefore along any rational sequence approaching the real median, the product of finite-place magnitudes diverges. There need not be any fixed divergent prime for unrestricted denominators. For odd-denominator approximations the 2-adic factor is identically 1, so the growth must occur at other places.

For a reduced t=a/B with p|B, p≠5, put e=v_p(B)>0. In the polynomial

\[
15D=120t-15t^4-6t^5-5t^6-47,
\]

the degree-six term has p-valuation −6e (since p≠5). Every other term has strictly larger valuation (all coefficients integral, lower degrees). Ultrametric dominance gives

\[
v_p(D)=-6e-v_p(15).
\]

In particular on a rational p-power grid p≠5, any sequence converging to the irrational real median has reduced denominator depth e→∞: otherwise a subsequence lies in a fixed finite grid, contradicting irrationality. Hence |D|∞→0 but |D|_p→∞. For odd p, |D|_2=1 throughout. This is a concrete zero/null vs infinity duality in the original BBP forcing, not a formal analogy.

On the 3^N grid choose an interior bracket endpoint nearest in signed residual to the median (for sufficiently large N). Q≤4 yields |D|∞≤8/3^N. Since the denominator divides 15·3^{6N}, |D|_5≤5 and |D|_p≤1 at all p≠3,5. Therefore product formula already forces

\[
|D|_3\ge \frac{1}{5|D|_\infty}\ge \frac{3^N}{40}.
\]

The exact valuation above is stronger: |D|_3=3^{6e+1} with reduced depth e. This is a genuine real/arithmetic capacity constraint on a common nonzero rational witness, directly illustrating the height-patching structure in RH_ORACLE O2. There is no free approach to null in every place.

**Crucible:** if the observer silently renormalizes D at each place by unrelated factors, the apparent obstruction vanishes; the shared rational source and product formula forbid doing this for free. A rational sequence may converge to an algebraic real number without specifying its p-adic embedding. A p-adic continuation of the polynomial's root is a different problem. We did not prove its local solubility for all places. For p=5 the leading coefficient is not a unit; at denominator depth one two terms may tie, so the exact generic formula is restricted to p≠5.

## B8. Implication for the source/observer contract

Maintain the signed residual and its full place-indexed valuation vector, not merely the real absolute residual. The stronger theorem is not "approach zero forces truth": here approaching one null forces a measurable blow-up elsewhere, and every rational single cut stays non-null. A genuine joint seam must be in a common source-preserving completion with transported normalizers and a paid height budget. This does not say all multi-place paths fail; it tells us exactly why this one-chart rational approach cannot supply them.

The compact RH proof's reciprocal height families use a shared normalizing H within each certificate, then product-formula cancellation. This BBP example recovers that principle on an actual SUCC source rather than a generic toy number; it does not reproduce RH's automorphic theta volumes or force any missing chronological R0 implication.

## Independent validation

[Independent Fraction oracle](independent_two_place.py), run in Python in the local container (not the JavaScript runtime), checks signed integration using the factored Q expansion cell by cell. Fixed seed 20261126; 360 mixed rational cut families, 2,520 moment checks, including 1,673 odd deepest-count exact valuations and 224 even deepest-count congruence checks (remaining cases odd denominator); 1,683 rational single-cut even moment checks; 24 median brackets on p=2,3,7,11 grids of depths 1–6. Tested exact polynomial equality, valuation and denominator support and the product-formula growth consequence at p=3, not full large integer factorization. Raw outputs [PYTHON_RECEIPT.json](PYTHON_RECEIPT.json). Executed Git blob expected 966409aef8f2efb3773dc39a618b170ec630f2de; raw JSON expected 2b95feb49e586d1b572a7ecdb93287f5db1c037b. This is a separate implementation/runtime and new deterministic regimes, sharing the source contract, not a blind mathematical referee. Universal authority is the algebra above.
