# Europa Weyl and the selected π orbit

Research-only child of [#499](https://github.com/femboy2112/SUCC/pull/499). The analytic and arithmetic results have paper proofs and scoped finite checks. Two algebraic lemmas also compiled in Lean. The real-circle energy, base-16 normality of π, beta-GRH, and zeta RH remain open. The enduring deliverables are the arithmetic loss estimate, the marked finite maps in both directions, and counterexamples to transferring positivity or cancellation through those maps.

## π moonshot

Let Y be the zero-seeded angular projection of the authentic signed BBP source. Write D_t=den(Y_t), G_nt=den(Y_t−Y_n), and
$$
  H(n,t)=\log\bigl(D_t/\gcd(D_t,G_{nt})\bigr).
$$
This counts the prime-power mass in the later state that disappears from the pair difference. In every large epoch [A,2A), summing H over the other time costs O(A³ᐟ²) for **each fixed earlier endpoint**. A separately derived estimate gives the same bound for each fixed later endpoint. The pulse-free runs are geometric mod p. For p above the square-root threshold, a matching nonzero residue occurs at most once per multiplicative order on each run. The bound Σ log(p)/ord_p(16)=O(√A), together with the number of genuine pole births, gives the result. Small primes including all powers contribute O(√A) per pair in the worst case used here. [Fixed earlier endpoint](energy/PAIR_SIEVE.md) · [fixed later endpoint and all-tap proof](primal/PRIME_LAYERS.md).

Consequently, for H(n,t)>√A(log A)² the number of unordered exceptional pairs is O(A²/log² A). At q=q_A their **total contribution** to the actual circle tent energy is O(q/log² A)=O(1/log A). Diagonals contribute q/A. For these statements the tent uses distance to the nearest integer, and both ordered copies of a pair are counted. The absolute logarithmic loss relative to the full forcing LCM has a separate O(A²ᐟ³) mean bound. One can also exclude all pairs with |log G_nt−8t|>δA, at cost O_δ(q/√A) for any fixed δ>0.

**Remaining count, equivalent at this mesh.** Write g_nt for the centered numerator of the reduced circle difference. On the surviving pairs H≤√A(log A)², show that the count with |g_nt|<G_nt/q is o(A² K_A/q) on all large dyadic epochs. This is equivalent to the surviving tent target up to absolute constants and an additive o(1) in energy units. To see the converse, partition the circle into 2q equal half-open cells, with counts c_i. Every ordered pair at distance <1/q lies in cells at most two cyclic steps apart. Cauchy–Schwarz bounds their count by 5Σc_i². Every same-cell pair has tent weight ≥1/2, hence 5Σc_i²≤10A²J/q. The direct bound is immediate from tent weight ≤1. Discarding the diagonal and the exceptional pairs costs at most O(q/A+q/log² A) for either observable. This comparison concerns physical pair counts; it gives no converse for the unweighted Fourier band. The 8N endpoint denominator growth makes the surviving denominators exponentially large; it leaves the ratio |g_nt|/G_nt unresolved. Restricting the sum pays a quantified error but does not establish a saving on its largest term. An unweighted Fourier truncation at q² gives only a sufficient condition; the exact Fourier weights are sinc²(πh/q).

**The strongest control occurs inside the original source.** Its zero-seeded radial projection Z=U−Y also has denominator exponent 8, both square-root pair-loss estimates and the same eventual nonzero density spectrum. Its phases converge to zero. In fact J(Z)=q−[(3 log 2−2)/16]q²/A+O(q²/A²) for q=o(A). The proof finds one strictly negative partial tap prefix per radial block; every other prefix is positive, and none vanish. The radial and angular characters differ at inert primes. This identifies a genuine signed distinction that a successful estimate could use. [Proof and endogenous falsifier](radial/RADIAL_CONTROL.md).

**Same-forcing falsifier.** For every large A there are same-forcing odd rational seeds with denominator dividing D_A, size below 3·16^(−A), which pass every eligible aligned self-shadow up to cA for 0<c<4−log 16. Their epoch concentrates near 1/5 and J/q→1. The seed may depend on A. All eligible primes distinguish zero from any one fixed nonzero rational seed in the limit. An unconditional centered-numerator estimate needs the specific chronological zero boundary. [Growing-prime controls, all-order Abel boundary corrections and seed qualifications](boundary/PROOFS.md).

The independent arithmetic derivation classifies every rational eight-tap source. For nonzero w, log den(T_N(w))/N has a positive rational limit computable from its finitely many vanished pulse windows in the sense of the explicit formula (no effective last-zero algorithm asserted). This gives 6 for the original signed poles and 8 for the projected source. For both, log(M_N/den(T_N))=O(N²ᐟ³) with M_N the forcing LCM. The full p-adic top-layer formula includes eligible 3 and 5, prime powers and genuinely vanishing mutant windows. The two rational-state rank of the angular transfer is exact. Fewer linear states do not improve the real energy bound by themselves.

## Europa Weyl

| Marked input | Output | What is gained |
|---|---|---|
| Zero-seeded rational primal, native odd conductor | Affine finite Heisenberg action; tr(ρ Zʰ)=μ̂(h) | At nonaliases the optimized signed Haar-reference defect is exactly twice the modulus of μ̂(h). Character and position refinements obey dual maps. |
| Prime survival in every actual pair | Distinct time kets, fixed finite density spectrum, cyclotomic linear independence | Even at frequencies up to exp((4−ε)A), exact rational cancellation is excluded on large epochs. The magnitude can still tend to zero. |
| First N marked angular blocks, reversed normalized coordinate | A polynomial Q_N and Dirichlet polynomial B_N with B_N(1)=16^(1−N)Y_N/4 | B_N matches beta at 0,−1,…,−(8N−1); first failure at −8N is (8N)!/(2·16ᴺ). |
| Coefficients of Q_N | Signed beta prime-power arithmetic tape | Nearest-integer recovery has first ambiguous/incorrect degree λN+log N/(2g)+O(1), λ≈0.880223. Raw, unrounded logarithmic derivatives converge in weighted total variation on a strictly larger window, with a sharp crossover. |
| Reflected infinite character sequence | Completed signed Weil distribution Wχ on smooth compactly supported logarithmic tests | The conductor is 4; parity is odd; root number is +1; both completed endpoints are 1. Prime powers retain their signs and half-density, including the zero weight at 2. |
| Complete signed linear functional queried with localized bumps, plus known archimedean and source marks | Actual finite rational primal orbit | Recursively invert its Euler tape and reflect back. Nine ordered rational circle readings also recover eight taps given the forcing lift rule. This is nonlinear marked reconstruction. |
| Finite conductor operator space alone | Equality of quadratic forms on the whole Weil test space | Refuted for **linear** factorization through a fixed finite space. The beta form is strictly positive on an infinite-dimensional small-support space, so every finite observation map has a nonzero kernel witness. |

[Weyl operators, Fourier/refinement obstruction and relative Mann argument](weyl/WEYL_CONDUCTOR.md) · [beta completion, signed explicit formula and finite-rank obstruction](beta/BETA_WEIL.md) · [sharp decoding](reflection/REFLECTED_WINDOW.md) · [unrounded total variation](reflection/REFEREE.md) · [reverse marked map and its conditioning](reflection/MARKED_TRANSPORT.md).

There is also a source-specific Euler–Mascheroni identity. For m=8N and R_N(s)=β(s)−B_N(s), the ratio R_N(2)/R_N(1) differs from H_(m+1) by a positive amount smaller than 3/((m+2)(m+3)−2), with leading term 3/m². Thus γ appears in an authentic transverse Mellin moment. It controls a ratio of lifted period remainders. The physical phase involves scaling the endpoint by 16ᴺ. [Proof and rational interval checks](beta/GAMMA_BOUNDARY.md).

## Academic novelty and limits

The BBP formulas, Bailey–Crandall dynamics, Dirichlet beta, the primitive functional equation, finite Weil representation and Weil explicit formula are classical. The finite special-value interpolation here is *exactly* a truncated complex Euler transformation, as can be checked on the monomial test xʲ. Earlier SUCC work already derived a logarithmic loss from perfect phase coherence in #403, prime-window obstructions, the 6N and 8N constants in #497/#499, and a conditional normality gate. Those results are not rediscoveries to claim as advances.

The candidate research contributions are the rational eight-tap denominator exponent, two-sided in time square-root pair loss, the reflected-prefix tape estimates, reversible marked construction and quantitative cofactor/finite-rank obstructions in this particular source. The literature search located prior work on denominators of ordinary harmonic sums, classical criteria for roots-of-unity relations, short-support Weil positivity and complex BBP acceleration. It did not establish global priority. Boyd’s 1994 §5 already proves macroscopic prime survival for ordinary harmonic denominators by excluding finitely many short-prefix numerators. Shiu’s Theorem 2 gives the corresponding prime-power cancellation windows. Van Doorn’s Lemma 8 uses a rational one-period difference to study generalized harmonic sums. These precedents narrow the candidate contribution here to the specific geometric eight-tap classification and its quantitative consequences. [Boyd](https://doi.org/10.1080/10586458.1994.10504298) · [Shiu](https://arxiv.org/abs/1607.02863) · [van Doorn](https://arxiv.org/abs/2411.03073).

Review was by same-model workers using different derivations and implementations. There was no independent scholarly referee.

### Verification, provenance and source map

The starting fork is main → #493 → #496 → #497 → #499. #491, #492 and #498 are separate main children. #495 starts at the earlier #494 commit ed195a1, before the live #494 head. The authenticated hashes and base comparisons are in [the snapshot](FRONTIER.json) and [the nine comparisons](DAG.json). No sibling branch is silently incorporated. The source kernel, signed-pushforward interface and WeylBridge.lean are inputs. The zeta source-Weil interface targets conductor one; this work constructs the conductor-four beta functional separately.

The [archive receipt](ARCHIVE_RECOVERY.json) authenticates 14 restored members, including all 13 manifest payload hashes, against the recovered ZIP and pinned parent. Its original logs are historical. For current validation use the PR's exact-head checks. In the native checkout run the following.

~~~sh
python -m unittest discover -s tests -p 'test_prime_character_primal.py'
python -m unittest discover -s tests -p 'test_europa_weyl_research.py'
python research/2026-11-04/europa_weyl/replay.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
~~~

The twelve JSON comparisons check the declared finite horizons and mutations. The unrounded referee receipt also includes labelled numerical scaling diagnostics; the all-horizon total-variation proof uses Stirling and divisor convolution. The archival 26 tests and the beta/Weyl unit suites are reachable from normal test discovery. The Lean file in the research folder is outside the historical Lean baselines. Finite computation, even on the exact tree, cannot certify the asymptotic energy target.
