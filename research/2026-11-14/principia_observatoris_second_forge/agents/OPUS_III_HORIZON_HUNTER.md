# OPUS III — The Horizon Hunter: finite-horizon completeness and its barriers

**Operation Principia Observatoris — Second Forge, Question B.** Date 2026-11-14. Agent report to the integrating principal investigator; nothing here is merged or ledger-promoted.

**Owned artefacts**

- this report;
- `observational_succ/observatoris_finite_horizons.py`, an exact lab module (stdlib only: `Fraction` and prime-field integers; floats are refused);
- `tests/test_observatoris_finite_horizons.py`, with 45 tests in 12 classes: positive, negative, mutation, holdout and exhaustive small-model tests.

Command: `python -m unittest tests.test_observatoris_finite_horizons -v`. Result on this machine: **45 tests, OK, about 1.6 s**.

**Shared input, not a validation witness.** Section 9 of `research/2026-11-13/causal_relevance_proximity/RESEARCH_NOTE.md`, read from branch `origin/research/causal-relevance-proximity-2026-11-13`, defines the founding pair a(n)=1/(n+1) and b_H. Nothing from the parallel "Astra" campaign was sought or used.

**Project machinery reused or attributed (not rediscovered)**

- `docs/CARRIER_RELATIVE_TARGETS.md`:
  - §1: target factorisation P = P̄∘E;
  - §4: target oscillation ω and the minimax error radius ω/2;
  - §5: compact target completion, the finite-stage clopen phenomenon, and the statement that "normality is not a continuous Boolean function of the prefix topology".
- `observational_succ/carrier_hankel_bounds.py`: Hankel-minor dimension lower bounds, and the delayed impulse δ_h with minimal LTI dimension h+1.
- `observational_succ/nerode_probe_growth.py`: `delayed_signal_chain`, which is the chain machine used in FH-7.
- `observational_succ/future_safe_quotient.py`: classical Moore/Mealy minimisation.
- `observational_succ/carrier_realization.py`: minimal linear realisation = Hankel rank.
- `observational_succ/infinite_realization.py`: Ind-object and colimit typing. A limit is not a finite elapsed step.

The present report sharpens these into exact horizon constants. It does not supersede them.

**Status vocabulary**

| Label | Meaning |
|---|---|
| CLASSICAL [source] | A known theorem. I re-prove it here when the proof is short. |
| PROVED | A paper proof given here, for a project-local deduction. |
| OBSERVED | Seen in exact finite models (an exhaustive or sampled search). |
| CONJECTURED | Not proved. |
| REFUTED | Comes with a receipt. |

I claim **no scholarly novelty**. Every "PROVED" item is an elementary deduction that is very likely in the literature.

**Global boundary.** Nothing here says anything about physics, RH, π-normality, actual brains, or any physical carrier. Each theorem is relative to a *declared* model class. Whether a real source belongs to that class is a separate obligation that no theorem here discharges (CARRIER_RELATIVE_TARGETS §3, obligation 3).

---

## 0. Common setting and conventions

The following conventions are used throughout:

- **Index convention.** Sequences are x = (x(0), x(1), …) with values in a declared value set V; readouts are exact. "Agree on the first N terms" means x(k)=y(k) for 0 ≤ k ≤ N−1.
- **Horizon.** The *horizon* of a class pair (𝒜, ℬ) is the least N such that every a∈𝒜, b∈ℬ agreeing on N terms are equal.
- **Sharpness.** A horizon N is *sharp* when some a≠b agree on N−1 terms.
- **Topology.** V^ℕ carries the product of discrete topologies, also called the prefix or finite-information topology. Its basic open sets are cylinders [σ] = {x : x extends σ}.

**Linear classes over a field K**

- LR_n(K) is the set of sequences annihilated by p(S) for some monic p of degree ≤ n. Here (Sx)(k) = x(k+1) is the shift, and p(S)x = 0 means x(k+deg p) = −Σ_{j<deg p} p_j x(k+j) for all k ≥ 0.
- LR(K) = ⋃_n LR_n(K).
- A constant term p_0 = 0 is **allowed**: nilpotent and delay parts are included.
- For x ∈ LR, Ann(x) = {f ∈ K[t] : f(S)x = 0} is a nonzero ideal. Its monic generator μ_x is the *minimal polynomial*, and ord(x) := deg μ_x.

**Founding pair**

- a(n) = 1/(n+1).
- b_H(n) = 1/(n+1) for n ≤ H, and b_H(n) = 1 for n > H.

---

## FH-1. Readout-only decidability equals pointwise continuity (deterministic, adaptive)

**Domain and definitions.**

- X ⊆ V^ℕ is a declared class, Y a set of target values (discrete), and T : X → Y the target.
- A *deterministic adaptive finite-readout protocol* is a decision tree 𝒟. Each internal node is labelled by an index i ∈ ℕ and has one child per answer v ∈ V; each leaf carries a label in Y. No computability is assumed.
- *Terminating on X* means the run on every x ∈ X reaches a leaf after finitely many queries.
- Q(𝒟,x) denotes the finite set of indices queried on input x.
- *Deciding T* means the leaf reached on x is T(x), for every x ∈ X.

**Theorem FH-1.**

- **(a) Transcript lemma.** If y ∈ X agrees with x on Q(𝒟,x), then 𝒟 follows the same path on y and outputs the same leaf.
- **(b) Characterisation.** A terminating protocol deciding T on X exists iff T is *continuous at every point of X*. Continuity at x means: there is a finite Q_x ⊂ ℕ such that every y ∈ X with y|Q_x = x|Q_x has T(y) = T(x). When such a protocol exists, a prefix-reading one exists too: it reads x(0), x(1), … and stops at the first N with T constant on [x|N] ∩ X.
- **(c) Discontinuity points.** If T is discontinuous at some x* ∈ X, then *every* terminating protocol errs on x* or on some y ∈ X that agrees with x* on all indices ≤ max Q(𝒟,x*).
- **(d) Tail-closed classes.**
  - Hypotheses: (i) X is closed under tail splicing, meaning x, z ∈ X and N ∈ ℕ imply x|[0,N]·z|[N+1,∞) ∈ X; (ii) T is a tail target, meaning T(x)=T(x') whenever x and x' ∈ X differ at finitely many indices; (iii) T is non-constant on X.
  - Conclusion: T is discontinuous at **every** point of X, so every terminating protocol errs, and does so near every point.
- **(e) Founding pair.** Let X = {a} ∪ {b_H : H ≥ 0} and let T be the regime label: LIMIT on a, FINITE on every b_H. Then T is discontinuous at a, so no terminating deterministic adaptive protocol decides the regime.

**Proof.**

- (a) Induction on depth. At each node the queried index lies in Q(𝒟,x), so the answers coincide and the same child is taken.
- (b) "⇒": by (a), Q_x := Q(𝒟,x) witnesses continuity at x. "⇐": the prefix reader stops on x at the latest at N = 1 + max Q_x, and its leaf value is correct by the stopping rule.
- (c) Let N = max Q(𝒟,x*). Discontinuity gives y ∈ X with y|[0,N] = x*|[0,N] and T(y) ≠ T(x*). By (a) both runs output the same value, so one of them is wrong.
- (d) Fix x and finite Q ⊂ [0,N]. Pick z with T(z) ≠ T(x) and splice y = x|[0,N]·z|tail. Then y ∈ X, y differs from z at finitely many indices so T(y) = T(z) ≠ T(x), and y agrees with x on Q.
- (e) b_H agrees with a on [0,H]. Since T(b_H) ≠ T(a), apply (c).

This independently re-proves the founding §9 certificate, including the adaptive case. ∎

**REFUTED: the PI's weaker hypothesis does not work for adaptive protocols.** The hypothesis was: "for each finite query set, two members agree on it but differ in target".

- **Pointer class (receipt).** X = {x_{k,β} : k ∈ ℕ, β ∈ {0,1}}, where x(0) = k, x(k+1) = β and every other entry is 0. The target is T(x) = β.
- The weak condition holds: for any finite Q, take k with k+1 ∉ Q; then x_{k,0} and x_{k,1} agree on Q.
- Yet the two-query adaptive protocol "read k = x(0), then output x(k+1)" decides T exactly.
- So the existential-pair condition characterises only **non-adaptive** protocols, where one finite Q is fixed in advance and the argument is immediate. The adaptive characterisation is the *pointwise* condition (b) at a single base point. The founding argument uses exactly that, since it fixes a as the base point.
- Tests: `test_pointer_class_refutes_existential_pair_condition_for_adaptive`, which checks every Q ⊆ [0,7] with |Q| ≤ 4 and k < 40.

**Status.** (a)–(d) are CLASSICAL in substance: decidability with certainty corresponds to clopen or continuity (Kelly, *The Logic of Reliable Inquiry*, 1996, ch. 3–4; Weihrauch, *Computable Analysis*, 2000, on continuity of realisers). The present proofs are given here. The pointer refutation is PROVED, with tests.

**Hostile models (one hypothesis dropped at a time).**

- *Bounded H.* For the family {a} ∪ {b_H : H ≤ H₀}, a single query at H₀+1 decides. The test is `test_bounded_family_mutation_is_decidable`.
- *Non-terminating protocols* are excluded by definition. A protocol that reads forever "decides in the limit", which is FH-5/FH-12 territory, not certainty.

**What this buys.** An exact criterion: the regime is finitely decidable iff the target is locally constant in the declared class. **What it does not establish:** anything about a specific source. For one known pair (a, b_7), the single query x(8) discriminates.

**Interoperability.** Input: (class X, target T, protocol). Output: either a continuity witness Q_x, or a fooling pair (x*, y) with identical transcripts (`fool_protocol_on_founding_pair`, `run_protocol`).

**Next falsification opportunity.** Find a class where adaptive protocols beat every prefix reader in *query count*. They do: pointer-type classes. A sharp query-complexity separation is left open.

---

## FH-2. Randomised protocols cannot beat error 1/2 at a discontinuity point

**Setting.**

- A randomised protocol is a family of decision trees 𝒟_r indexed by coin strings r ∈ (Ω, P).
- It is assumed to terminate P-almost surely on x* ∈ X.
- T is discontinuous at x*, as in FH-1(c).

**Theorem FH-2.** For every δ > 0 there is y ∈ X with T(y) ≠ T(x*) and

  err(x*) + err(y) ≥ 1 − δ,  where err(z) := P[𝒟_r(z) ≠ T(z)].

Hence max(err(x*), err(y)) ≥ (1−δ)/2, so no randomised protocol achieves worst-case error bounded below 1/2 on X. If Ω is finite and every run on x* is finite, one may take δ = 0, giving err(x*) + err(y) ≥ 1.

**Proof.**

1. M(r) := max Q(𝒟_r, x*) is finite a.s. Choose N with P[G] ≥ 1−δ, where G = {M ≤ N}.
2. Choose y agreeing with x* on [0,N] with T(y) ≠ T(x*).
3. On G the run on y equals the run on x* (FH-1a).
4. The events {𝒟_r(x*) = T(x*)} and {𝒟_r(x*) = T(y)} are disjoint.
5. Therefore P[correct on x*] + P[correct on y] ≤ P[G] + 2P[Gᶜ] ≤ 1 + δ. ∎

**Status.** PROVED (a standard coupling argument). Test `test_randomised_error_sum_is_at_least_one` uses exact enumeration of 8 coin strings and gets err sum ≥ 1. A **mutation** that lets H fall inside the query range drives the sum below 1. **Boundary.** This says nothing about Bayesian priors over H. A prior can make the expected error small, so a Bayesian guarantee is a different claim. **Interop.** Input: protocol with a finite coin space. Output: exact err-sum certificate (`randomized_error_sum`). **Next falsification opportunity.** One-sided-error variants (Las Vegas or Monte Carlo) on promise classes.

---

## FH-3. Linear recurrences: horizon exactly n + m, over every field, with degenerate cases

**Theorem FH-3** (K any field; n, m ≥ 0).

- **(a) Upper bound.** If a ∈ LR_n(K), b ∈ LR_m(K) and a(k) = b(k) for 0 ≤ k ≤ n+m−1, then a = b.
- **(b) Sharpness.** For every (n,m) ≠ (0,0) there are a ∈ LR_n(K), b ∈ LR_m(K) agreeing on exactly n+m−1 terms, with a(n+m−1) ≠ b(n+m−1). The pair is integer-valued and identical in form over every field:
  - m ≥ 1: b(k) = C(k−n, m−1), where C(x,r) = x(x−1)⋯(x−r+1)/r! is the generalised binomial; a(k) = b(k) for k < n and a(k) = 0 for k ≥ n. Then a is annihilated by tⁿ, b by (t−1)^m, and a(n+m−1) − b(n+m−1) = −1.
  - m = 0, n ≥ 1: a(k) = C(k, n−1) (annihilated by (t−1)ⁿ) and b = 0.
  - (n,m) = (0,0): both sequences are 0. The horizon is 0, and "sharpness" is vacuous.
- **(c) Same-class corollary.** Within LR_n the horizon is 2n, and it is sharp for n ≥ 1.
- **(d) Exact horizon for restricted families** (FH-3b). Let 𝒫 and 𝒬 be sets of monic polynomials, with S_𝒫 = ⋃_{p∈𝒫} ker p(S) and S_𝒬 likewise. The exact horizon of (S_𝒫, S_𝒬) is

  **N\* = max_{p∈𝒫, q∈𝒬} deg lcm(p,q)**   (the supremum, possibly ∞).

**Proofs.**

- **Lemma 1 (kernel dimension).** For monic f of degree D, ker f(S) is D-dimensional. The initial-value map x ↦ (x(0),…,x(D−1)) is an isomorphism, because the recurrence determines the rest.
- **Lemma 2 (sum of kernels).** ker p(S) + ker q(S) = ker lcm(p,q)(S).
  - "⊆" holds because lcm(p,q) is a multiple of each of p and q.
  - ker p ∩ ker q = ker gcd(p,q). One inclusion is from Bézout: gcd = up+vq, so if p(S)x = q(S)x = 0 then gcd(S)x = 0; the other is because gcd divides p and q.
  - Dimensions: deg p + deg q − deg gcd = deg lcm. So the inclusion is an equality.
- **(a) and the "≤" half of (d).** a − b ∈ ker lcm(p,q)(S), of degree D ≤ n+m. It vanishes on its first D initial values, so it is 0 by Lemma 1.
- **(d) "≥" half.** Let p, q attain D = deg lcm(p,q) ≥ 1. By Lemma 1 there is d ∈ ker lcm(S) with d(0..D−2) = 0 and d(D−1) = 1. By Lemma 2, d = a + b' with a ∈ ker p(S) and b' ∈ ker q(S). Put b := −b'. Then a − b = d, so a and b agree on D−1 terms and differ at index D−1.
- **(b).** Take p = tⁿ and q = (t−1)^m. They are coprime in every field because 0 ≠ 1, so deg lcm = n+m.
  - Explicit check: (S−1)C(k,j) = C(k,j−1), so (S−1)^m kills every integer-valued polynomial of degree < m in k.
  - b(k) = C(k−n, m−1) vanishes at k = n, …, n+m−2 and equals 1 at k = n+m−1.
  - a vanishes from n onward.
- **(c)** is (a)+(b) with m = n. ∎

**What changed from the PI's statement.**

1. Confirmed: n+m is exact for all n, m ≥ 1 over ℚ.
2. Extended: the same integer pair is extremal over **every** field (char p included), and for n = 0 or m = 0 (not both).
3. Correction: sharpness depends on the allowed polynomial family. The exact constant is max deg lcm (FH-3d).
   - **Receipt:** over GF(2), restrict to invertible recurrences (nonzero constant term, so no nilpotent or delay part). The only order-≤1 polynomials are 1 and t+1, so the classes are the constant sequences, and the (1,1) horizon is **1, not 2**.
   - For (1,2), (2,2), (1,3) and (2,3) over GF(2) the invertible horizon is again n+m, using coprime pairs such as (t+1)ⁿ and t^m+t+1.
   - Test: `test_restricted_polynomial_families_follow_max_lcm_degree`, which compares an exhaustive maximum against the predicted max deg lcm.

**Tests.**

| Test | What it checks |
|---|---|
| `test_extremal_pair_all_fields_and_degenerate_cases` | ℚ, GF(2), GF(3), GF(5); 0 ≤ n, m ≤ 6 |
| `test_exhaustive_gf2_gf3_gf5_horizon_is_exactly_n_plus_m` | Exhaustive for every sequence of order ≤ n, ≤ m: GF(2) with n, m ≤ 4; GF(3) with n, m ≤ 2; GF(5) (1,1) and (1,2). "Distinct" is certified independently of FH-3 by the pigeonhole length p^{n+m} on joint states. The maximum agreement found was exactly n+m−1 every time. |
| `test_small_integer_exhaustive_over_Q` | Coefficients and initial values in {−1,0,1}, orders ≤ 2 |
| Mutation | A checker with horizon n+m−1 is fooled, and the non-monic "recurrence" 0·x = 0 accepts everything |
| Holdout | (10,13), (17,3), (0,21) |
| `test_bm_matches_independent_bruteforce_holdout` | Berlekamp–Massey is cross-checked against an independent rank-solvability brute force |

**Status.** (a) is CLASSICAL (the uniqueness part of Padé / partial-realisation theory; Kalman 1979; Berlekamp 1968 and Massey 1969 for the LFSR form). (b) and (d) are PROVED here; I expect they are known, and claim no priority.

**Hostile models.**

- Drop "monic": the leading coefficient may vanish, every sequence qualifies, and there is no horizon.
- Drop the order bound: see FH-5.
- Allow approximate readouts: see FH-6(e).

**Boundary.** This holds inside LR_n by declaration. Agreement on n+m terms does **not** show that a source *is* in LR_n.

**Interop.**

- Input: two exact prefixes plus declared order bounds (n, m), or declared polynomial families.
- Output: either an equality certificate (agreement on max deg lcm terms) or the extremal witness (`extremal_linear_pair`, `poly_lcm_degree`).

**Next falsification opportunity.** Characterise N\* for natural restricted families (stable, positive, or real-rooted recurrences). FH-3d reduces each to a max-lcm computation.

---

## FH-4. LTI systems and Markov parameters: SISO, MIMO, feedthrough, Kronecker, Cayley–Hamilton

**Setting.** z_{k+1} = Az_k + Bu_k, y_k = Cz_k (+ Du_k), with A ∈ K^{n×n}. The Markov parameters are h_k = CA^kB for k ≥ 0, matrices of size p×q.

**Theorem FH-4.**

- **(a) Cayley–Hamilton ⇒ recurrence.** Every entry sequence of h satisfies the monic recurrence χ_A of order n. So for SISO systems, {Markov sequences with dim ≤ n} = LR_n(K): "⊇" by the companion realisation, "⊆" by Cayley–Hamilton.
- **(b) Scalar Kronecker.** For a scalar sequence x, rank of the infinite Hankel matrix [x(i+j)] = ord(x) (∞ iff x ∉ LR).
  - Proof: the rows are S^i x. The map f ↦ f(S)x from K[t] onto the row space has kernel Ann(x). So the rank is dim K[t]/Ann(x) = deg μ_x, or ∞ if Ann(x) = 0.
  - Combined with (a), this gives Hankel rank = minimal recurrence order = minimal SISO state dimension.
- **(c) Horizon.** Systems with state dimensions ≤ n and ≤ m, SISO or MIMO of any size p×q, have equal Markov sequences iff h_k = h'_k for 0 ≤ k ≤ n+m−1. The constant **n+m is sharp for every p, q ≥ 1**: zero-pad the FH-3 SISO pair into entry (1,1). Padding does not change the state dimension.
- **(d) Same class.** 2n Markov parameters determine the whole impulse response of a dim-≤n system, and this is sharp.
- **(e) Feedthrough off-by-one.** In the convention (D, CB, CAB, …) with h_0 = D, the horizon is **n+m+1 parameters**, sharp: the sequence (D, a) for equal D.
- **(f) MIMO Kronecker / Ho–Kalman.** The block-Hankel rank equals the minimal realisation dimension (Ho–Kalman 1966; Kalman–Falb–Arbib 1969). I cite this and do not re-prove the block version.

**Proof of (c).** Each entry of h − h' is annihilated by χ_A·χ_{A'}, of degree ≤ n+m, so FH-3a applies entrywise. Sharpness: FH-3b realised by companion systems of dimensions n and m (test `test_siso_extremal_pair_realised_with_dims_n_and_m`). ∎

**Tests.**

- Random rational A (n ≤ 4): BM order ≤ n (Cayley–Hamilton), and Hankel rank = BM order (scalar Kronecker).
- MIMO zero-padding keeps the horizon sharp.
- Feedthrough mutation.

**Status.** CLASSICAL [Kronecker 1881; Cayley–Hamilton; Ho–Kalman 1966]. The sharpness constructions are PROVED here.

**Boundary.** The horizon counts Markov parameters of *declared-dimension* systems. Finer structural data, such as observability or controllability indices, could shorten it. I have **not** proved an index-refined horizon (see the open list).

**Interop.**

- Input: Markov sequence plus declared dimension(s).
- Output: equality certificate after n+m parameters; Hankel-rank lower bound via `hankel_rank`, consistent with `carrier_hankel_bounds`.

---

## FH-5. Unknown dimension: identifiable in the limit, never finitely certified (the central statement)

**Setting.** The class is LR(K) = ⋃_n LR_n(K), read prefix by prefix. Definitions:

- A **learner** maps finite prefixes to conjectured sequences.
- It **identifies x in the limit** if its conjecture equals x for all sufficiently long prefixes (Gold 1967).
- A **certifier** maps prefixes to {wait} ∪ {halt with a conjectured sequence}. It is **sound** on a class if, whenever it halts on a prefix of x, the conjecture equals x.

**Theorem FH-5.**

- **(a) No horizon.** For every N there are x ≠ y ∈ LR(K) agreeing on N terms: x = 0 and y = δ_N, with ord(δ_N) = N+1. More strongly, for every x ∈ LR and every N, x + δ_N ∈ LR agrees with x on N terms. Hence every point of LR is non-isolated: LR has no isolated points.
- **(b) Limit identification by an explicit time.** The *conservative minimal-order learner* works as follows: keep the current conjecture while it is consistent; otherwise switch to a minimal-order recurrence consistent with the prefix (Berlekamp–Massey) together with the observed initial values.
  - On every x ∈ LR with d = ord(x), its conjecture equals x for every prefix length t ≥ 2d.
  - It changes its mind at most 2d times.
  - Over K = ℚ it is computable (exact arithmetic).
- **(c) Stabilisation time 2d is optimal for every learner.** For every learner and every d ≥ 1, some x ∈ LR_d still has a wrong conjecture at t = 2d−1. Reason: the FH-3 extremal pair with n = m = d shares the prefix of length 2d−1.
- **(d) No sound certifier halts anywhere.** If a certifier halts on x|t with conjecture x, it halts identically on x + δ_t ∈ LR, which has the same t-prefix, so it is unsound. A sound certifier on LR therefore halts on **no** member. The same holds for any target that is discontinuous everywhere on LR, by FH-1(d).
- **(e) No uniform mind-change bound.** For every learner identifying LR in the limit and every k, some x ∈ LR forces at least k mind changes.
  - Adversary: start with 0. Wait until the learner conjectures the current finite-support sequence; this happens because it identifies that sequence in the limit. Then add an impulse beyond the current time. Repeat k times.
  - Each round forces a change, and every finite sum of impulses is in LR.
- **(f) Declared bound collapses everything.** On LR_n, "wait until t = 2n, then halt with the BM conjecture" is a sound certifier halting on every member, with zero mind changes after commitment, and t = 2n is optimal by (c).

**Proof of (b) (key lemma: uniqueness for prefixes of length ≥ 2d).**

- Let μ = μ_x, with degree d, and let t ≥ 2d.
- Let g be any monic recurrence of degree r ≤ d consistent with x|t. Let x' be the sequence generated by g from x(0..r−1).
- Then x' ∈ LR_r, x ∈ LR_d, and x' agrees with x on t ≥ r + d terms. By FH-3a, x' = x.
- So g annihilates x, hence μ | g. Since deg g ≤ deg μ and both are monic, g = μ.
- Consequently the minimal consistent order at time t is exactly d and the minimal consistent recurrence is unique. The conservative learner's conjecture (if it had been refuted it is replaced by μ; if not refuted it is a minimal consistent recurrence, hence μ) equals x.
- Conjectures name sequences injectively: two distinct minimal-order conjectures cannot generate the same sequence, by the same divisibility argument.
- Changes occur only at t ≤ 2d, so there are at most 2d of them. ∎

(d) and (e) are adversary arguments as stated.

**Precise slogan (PROVED for LR(K)).** *LR(K) is identifiable in the limit, with correct stabilisation by time 2·ord(x). No stopping rule can certify that stabilisation has occurred, at any time, on any member. A declared order bound n restores a uniform certificate at time exactly 2n.*

**Tests.**

- `test_exhaustive_learner_stabilises_by_2d_with_at_most_2d_changes`: every sequence of order ≤ 4 over GF(2) and of order ≤ 2 over GF(3).
- **OBSERVED:** both bounds are attained for every d in these ranges. The worst stabilisation time is exactly 2d, and the worst mind-change count is exactly 2d; for d = 1, the constant sequence c ≠ 0 forces 0 → (c,0,0,…) → (c,c,c,…). Sharpness of the 2d mind-change bound for all d is **CONJECTURED** for this learner.
- Others: `test_no_learner_is_right_on_both_extremal_sequences_at_2d_minus_1`, `test_every_halting_certifier_is_unsound` (t = 0..29), `test_adversary_forces_any_number_of_mind_changes`.

**Status.** Identification in the limit by enumeration and the impossibility of certification are CLASSICAL in form (Gold 1967; Osherson, Stob & Weinstein, *Systems that Learn*, 1986; Kelly 1996). The constants (2d, 2d, 2n) and the LR-specific proof via FH-3 are PROVED here.

**Remark (topology, CLASSICAL).** LR(ℚ) is countable and metrisable (as a subspace of ℚ^ℕ) and has no isolated points, by (a). By Sierpiński (1920) it is homeomorphic to ℚ. It is also dense in ℚ^ℕ: every prefix extends to a finitely supported sequence.

**Boundary.** The learner identifies the *sequence*. It does not decide universal properties of that sequence (FH-13). The guarantee "by time 2d" uses the unknown d, so it is not a stopping rule.

**Interop.**

- Input: prefix stream.
- Output: conservative conjecture trace with mind-change times (`conservative_learner_trace`, `mind_changes`), and a refuting witness for any proposed stopping time (`certifier_counterexample`).

---

## FH-6. The founding pair inside the linear theory

**Theorem FH-6.**

- **(a) a has infinite Hankel rank; a ∉ LR(ℚ).** det[1/(i+j+1)]_{i,j<N} = c_N⁴ / c_{2N} ≠ 0, where c_N = ∏_{k<N} k!.
  - This is the Hilbert-matrix case of the Cauchy determinant det[1/(x_i+y_j)] = ∏_{i<j}(x_j−x_i)(y_j−y_i) / ∏_{i,j}(x_i+y_j), with x_i = i and y_j = j+1.
  - By FH-4b, a lies outside **every** LR_n, including eventual (nilpotent-part) recurrences.
- **(b) Exact order of b_H.** ord(b_0) = 1. For H ≥ 1, ord(b_H) = H+2 and μ_{b_H} = t^{H+1}(t−1).
  - Proof: b_H = 1 + f, where f(k) = 1/(k+1) − 1 for k ≤ H and 0 after.
  - For H ≥ 1, f(H) = −H/(H+1) ≠ 0, so μ_f = t^{H+1} (a finitely supported sequence whose last nonzero entry is at H).
  - μ_1 = t−1, and t^{H+1} and t−1 are coprime.
  - If g(S) kills 1+f, then g(S)f = −g(S)1 ∈ ker t^{H+1} ∩ ker(t−1) = 0, so both components are killed. Therefore μ = lcm = t^{H+1}(t−1).
  - (For H = 0, f = 0.)
- **(c) Every member of LR_n breaks the law 1/(k+1) at some index ≤ 2n.**
  - The (n+1)×(n+1) Hankel matrix of any x ∈ LR_n has rank ≤ n. If x agreed with a on indices 0..2n, that matrix would equal the nonsingular H_{n+1}(a).
  - The bound is sharp: H_n(a) is invertible, so there is a **unique** x_n ∈ LR_n agreeing with a on exactly indices 0..2n−1. This is the "order-n mimic", a Padé/Prony fit.
- **(d) Exact first defect of the mimic.**
  a(2n) − x_n(2n) = det H_{n+1}(a) / det H_n(a) = **(n!)⁴ / ((2n)!·(2n+1)!)**.
  - Proof: H_{n+1}(x_n) and H_{n+1}(a) differ only in the (n,n) entry, which is index 2n.
  - The determinant is affine in that entry, with coefficient equal to the cofactor det H_n(a).
  - det H_{n+1}(x_n) = 0 by (c).
  - The ratio of Cauchy determinants simplifies to the stated factorial expression.
  - Values: 1/12, 1/180, 1/2800, 1/44100 for n = 1..4.
  - Asymptotically δ_n ~ (π/2)·16⁻ⁿ (Stirling: 1/C(2n,n) ~ √(πn)/4ⁿ). The exact δ_n·16ⁿ = 1.33, 1.42, …, 1.5611 at n = 40, increasing towards π/2 ≈ 1.5708.
- **(e) Precision corollary.** An observer reading indices 0..2n with absolute precision ε > δ_n cannot exclude LR_n using a's data: x_n is exact on 0..2n−1 and within δ_n at 2n. Excluding dimension n from this horizon requires about 4n bits of precision at index 2n. With exact readouts, 2n+1 terms suffice.

**Consequences for the two-regime discrimination with a declared dimension bound n.**

- **Limit-only branch is excluded.** The law "x = a forever" has no member in LR_n, for any n.
- **Model failure is finitely refutable.** If the observed prefix agrees with 1/(k+1) on indices 0..2n, the declaration "source ∈ LR_n" is refuted. The dimension bound turns "limit-only" into a finitely refutable *model-class failure*, decided at 2n+1 exact observations.
- **Which b_H remain admissible.** b_H ∈ LR_n iff H = 0 (n ≥ 1) or 1 ≤ H ≤ n−2. Equivalently, the finite-surprise members surviving the declaration are those whose deviation comes at or before index n−1.
- **Hostile reading.** The dimension bound does **not** exclude the limit-only *regime* in general. For example, 2⁻ᵏ has order 1, is nonzero everywhere and tends to 0. It excludes the particular law a. Inside LR_n the general regime question becomes a Skolem-type question (FH-13).

**Tests.**

- Hilbert determinants for N ≤ 10, by elimination versus the closed form.
- BM complexity of a's 2N-prefix is exactly N for N ≤ 12.
- ord(b_H) for H ≤ 15, with an annihilator check.
- The mimic for n ≤ 9: exact 2n agreement, the exact deviation formula, and the determinant-ratio identity.
- The admissibility criterion.

**Status.** (a) CLASSICAL [Cauchy 1841; Hilbert 1894]. (b)–(e) PROVED here. **Boundary.** These are statements about the declared exact model classes. They do not say that any physical or arithmetic defect is linearly generated.

**Interop.** Input: law 1/(k+1) and declared n. Output: guaranteed refutation index 2n, the exact mimic, and its exact defect (`harmonic_mimic`, `harmonic_mimic_deviation`, `founding_b_order`).

**Next falsification opportunity.** Compute where |x_n(k) − a(k)| first exceeds ε for k > 2n, giving a precision–horizon trade-off curve.

---

## FH-7. Deterministic autonomous finite-state machines: horizon n + m − 1 (one less than linear)

**Setting.** Machines (Q, δ: Q→Q, λ: Q→O, q₀) with |Q| ≤ n, and output sequences o_k = λ(δᵏq₀). |O| ≥ 2 for sharpness.

**Theorem FH-7** (n, m ≥ 1).

- **(a)** Outputs of machines with ≤ n and ≤ m states that agree on the first **n+m−1** terms are equal.
- **(b)** This is sharp.
  - Machine 1 is an n-state chain q₀→…→q_{n−1}↺. Its outputs are s(0..n−2) and then 0 forever.
  - Machine 2 is an m-cycle with s(k) = [k ≡ n−2 (mod m)].
  - They agree on indices 0..n+m−3 and differ at n+m−2.
- **(c) Bit-count versus state-count.** A k-bit carrier has ≤ 2^k states. Two carriers of k and k' bits therefore have horizon exactly 2^k + 2^{k'} − 1.
  - Witness: the k-bit saturating counter gate outputs 1 only when the counter is all ones. Compared with the 0-bit constant-0 carrier, it first deviates at index 2^k − 1 = n+m−2 with n = 2^k, m = 1. It is exactly extremal.
  - A dimension-k linear carrier, by contrast, has horizon linear in k (FH-3).
  - Hostile extension: with a description-size budget (k-bit Turing-machine programs), the first deviation can be delayed to the busy-beaver function of k, which grows faster than every computable function [Radó 1962]. No computable horizon exists.

**Proof 1 (Fine–Wilf).**

- Outputs are ultimately periodic with preperiod t_i and period p_i, where t_i + p_i ≤ n_i.
- After T = max(t₁, t₂), both are purely periodic. If they agree on T + p₁ + p₂ − gcd(p₁,p₂) terms, then by Fine–Wilf (1965) the common block has period g = gcd, so both tails are g-periodic and equal.
- Maximising T + p₁ + p₂ − g under the constraints gives ≤ n+m−1.

**Proof 2 (linear algebra, the "hyperplane lemma").**

- Encode outputs one-hot per symbol and set x_k = (e_{δᵏq₀}, e_{δ'ᵏq₀'}) ∈ ℚ^{n+m}.
- The difference sequence is w·x_k with x_{k+1} = Mx_k.
- Every x_k lies in the hyperplane {Σu − Σv = 0}, so the Krylov space has dimension ≤ n+m−1. The difference therefore has linear complexity ≤ n+m−1, and FH-3a applies with the zero sequence.

This second proof is the reason determinism costs one dimension less than general linearity. ∎

**Tests (exhaustive).**

- `test_exhaustive_horizon_is_n_plus_m_minus_1`: every binary output sequence of ≤ n-state machines for n, m ≤ 6 with n+m ≤ 10, and ternary sequences with n+m ≤ 7. The maximum first-difference index is exactly n+m−2 in every case.
- The enumeration of output sequences is cross-checked against brute machine enumeration for n ≤ 3 binary and n ≤ 2 ternary.
- `test_hyperplane_lemma…`: the maximum linear complexity of differences is exactly n+m−1 for n, m ≤ 4.
- Extremal pairs for n, m ≤ 9, with mutation: a horizon of n+m−2 is fooled.
- Counter gate for k ≤ 7.

**Status.** CLASSICAL in substance (Moore 1956; Fine & Wilf 1965). The two-machine autonomous constant n+m−1, the explicit pair, and the hyperplane explanation are PROVED here.

**Boundary.** State count is a *declared* bound. A physical "size" in bits gives an exponential horizon, and description size gives no computable one.

**Interop.** Input: declared state bounds. Output: equality certificate after n+m−1 outputs, or the explicit extremal machines (`extremal_machine_pair`, `counter_gate`, `rho_first_difference`).

---

## FH-8. Machines with inputs: Moore n+m−2 input symbols, Mealy n+m−1

**Theorem FH-8** (n, m ≥ 1). Initial states of Moore machines with n and m states that are distinguishable at all are distinguished by an input word of length **≤ n+m−2**, that is, by n+m−1 outputs including the initial one. For Mealy machines the bound is **≤ n+m−1** input symbols. Both are sharp, already for a one-letter input alphabet, by the FH-7 pair.

**Proof (Moore 1956 refinement).**

- Work in the disjoint union, which has N = n+m states.
- Let ≡_k be agreement on all words of length ≤ k. Each strict refinement increases the class count. If ≡_{k+1} = ≡_k, the relation is stable forever.
- Moore case: ≡_0 has ≥ 2 classes if any output differs, so stability is reached by k ≤ N−2.
- Mealy case: start from ≡_1, which gives ≤ N−1. ∎

**Tests.**

- Exhaustive over all 2-letter, binary-output machines with N ≤ 3: the maximum separator length is N−2 for Moore and N−1 for Mealy.
- Random holdout at N = 4, 5, 6: 400 machines each, all state pairs.
- Chain sharpness.

**Status.** CLASSICAL [Moore 1956, Gedanken-experiments; Gill 1962]. **Boundary.** This presumes resettable or independent copies of the two machines. On a single destructively probed copy see CARRIER_RELATIVE_TARGETS §3, where executable access can fail at every horizon.

---

## FH-9. Weighted and probabilistic automata: three exact constants

**Setting.** f(w) = α M_{w₁}⋯M_{w_k} β over a field. The classes are:

- **WA**: arbitrary weighted automata over the field.
- **Rabin PA**: α a distribution, each M_σ row-stochastic, β ∈ ℚⁿ arbitrary (acceptance values).
- **Generative HMM**: α a distribution, M_σ ≥ 0 with Σ_σ M_σ row-stochastic, β = 1.

**Theorem FH-9** (n, m ≥ 1 states). Automata agreeing on all words of length ≤ L are equivalent, with these exact constants:

| Class | L (sharp) | Sharpness witness |
|---|---|---|
| WA over any field | **n+m−1** | One-letter companion automata of the FH-3 pair |
| Rabin PA | **n+m−2** | Deterministic FH-7 pair; also a genuinely stochastic 2+2 example (below) |
| Generative HMM | **n+m−1** | Deterministic generative FH-7 pair; also a stochastic 2+2 example (below) |

**Proof.**

1. Form the difference automaton: α' = (α, −α_B), β' = (β; β_B), M' = diag(M, M_B). Let V_k = span{α'M'_w : |w| ≤ k}.
2. If V_k = V_{k+1} then V_k = V_∞.
3. Let k₀ be the first length of a differing word. Then V_{k₀−1} ⊂ β'^⊥, the chain V₀ ⊊ … ⊊ V_{k₀−1} is strict, and dim V₀ = 1. So k₀ ≤ dim β'^⊥ = n+m−1. This is the WA case.
4. **Rabin.** α'M'_w·(1;1) = αM_w1 − α_BM^B_w1 = 1 − 1 = 0 for every w. So V_∞ ⊂ β'^⊥ ∩ (1;1)^⊥, which has dimension n+m−2 unless β' ∥ (1;1), and in that case both functions are the same constant. Hence k₀ ≤ n+m−2.
5. **HMM.** Here β' = (1;1) is already the vector being tested, so there is no second constraint and the WA bound is attained.
6. The BFS used in code keeps only words that are new to the span. The minimal differing length is attained by a kept word: if every kept word of length k₀ had zero difference, the span would lie in β'^⊥. ∎

**Correction to the brief.** "n+m−1" is right and sharp for weighted automata and for generative HMMs. For **Rabin-type probabilistic automata** (stochastic letter matrices, the setting of Paz 1971 and Tzeng 1992) the same proof gives the **sharper n+m−2**, with sharp examples.

I have **not** re-checked whether Paz or Tzeng state n₁+n₂−1 or n₁+n₂−2. Treat any literature constant as unverified by me. The proved statement is the one above.

**Stochastic receipts (exact rationals).**

- Rabin pair A, B:
  - α = (1,0), β = (0, ¼), M_y = [[0,1],[1,0]] for both.
  - M_x^A = [[¼,¾],[0,1]] and M_x^B = [[¼,¾],[½,½]].
  - They agree on all words of length ≤ 1 and differ at xx: 15/64 versus 9/64. k₀ = 2 = n+m−2.
- HMM pair H1, H2:
  - H1: α = (½,½), M_a = [[0,½],[0,¼]], M_b = [[¼,¼],[½,¼]].
  - H2: α = (¼,¾), M_a = [[0,0],[¼,¼]], M_b = [[½,½],[0,½]].
  - First differing word: aba. k₀ = 3 = n+m−1.
- Both pairs were found by seeded exact random search. Over 20 000 sampled 2+2 pairs per class, k₀ never exceeded 2 (Rabin) or 3 (HMM).

**Tests.**

- The span algorithm matches brute-force word enumeration on 120 random WAs.
- One-letter extremal pairs for n, m ≤ 5. Mutation: these are not Rabin PAs, and they exceed n+m−2.
- Rabin deterministic extremal pairs, plus 300 random Rabin PAs, all ≤ n+m−2.
- Stochastic receipts.
- HMM deterministic extremal pairs for n, m ≤ 5.

**Status.** WA bound CLASSICAL [Schützenberger 1961; Carlyle & Paz 1971; Paz 1971; Tzeng 1992, algorithmic form]. The Rabin n+m−2 refinement and the three sharpness families are PROVED here (no priority claimed).

**Boundary.** Equality of word functions says nothing about equality of hidden states, which is target-relative descent (CARRIER_RELATIVE_TARGETS §1). Probabilities here are model numbers, not frequencies observed from a source.

---

## FH-10. Effective moduli: exact worst-case limit oscillation 2μ(N−1)

**Setting.**

- μ : ℕ → ℚ_{≥0} is nonincreasing.
- C_μ = {e ∈ ℝ^ℕ : |e_i − e_j| ≤ μ(min(i,j)) for all i,j}. If μ → 0, every member converges.
- L(e) = lim e. The fibre of a prefix p = (p_0..p_{N−1}) is K_p = {e ∈ C_μ : e|N = p}.

**Theorem FH-10** (N ≥ 1).

- **(a) Exact fibre.** K_p ≠ ∅ iff p is internally consistent: |p_i − p_j| ≤ μ(min(i,j)) for i, j < N. In that case
  L(K_p) = ⋂_{j<N} [p_j − μ(j), p_j + μ(j)]
  exactly. The set is nonempty because it contains p_{N−1}.
- **(b) Worst case.** sup_p ω_L(K_p) = **2μ(N−1)**, attained by the constant prefix 0 with limits ±μ(N−1). The minimax error radius ω/2 = **μ(N−1)** is attained by the midpoint (CARRIER_RELATIVE_TARGETS §4).
- **(c) No modulus.** On the class of all convergent sequences, every prefix has limit set ℝ: extend by e_n = L for n ≥ N. So ω = ∞ for every N.
- **(d) Founding pair under μ(k) = 1/(k+1).**
  - a ∈ C_μ, and a's own prefix of length N has limit set exactly [0, 2/N], so it is itself extremal.
  - b_0 ∈ C_μ and b_1 ∈ C_μ.
  - b_H ∉ C_μ for H ≥ 2: |b_H(H) − b_H(H+1)| = H/(H+1) > 1/(H+1).
  - So the class {a} ∪ {b_H} ∩ C_μ = {a, b_0, b_1} is finite, and the regime is decided at index 2 (b_1(2) = 1 versus a(2) = 1/3).
  - The prefix (1, ½) of b_1 has limit set [0,1], which attains 2μ(1). The founding pair at H = 1 is an extremal witness.

**Proof.**

- "⊆": take j < N and m → ∞ in |p_j − e_m| ≤ μ(j).
- "⊇": for L in the intersection, e = p·(L, L, …) satisfies every constraint: prefix pairs by consistency, (j, tail) by L ∈ I, tail pairs trivially.
- (b): μ nonincreasing gives |I| ≤ 2μ(N−1), and the constant prefix attains it.
- (c), (d): direct computation. For a ∈ C_μ: |1/(i+1) − 1/(j+1)| ≤ 1/(min+1). ∎

**PI's conjecture "2μ(N−1)": CONFIRMED exactly.** The index convention is N observed terms, last index N−1. The per-prefix oscillation is min_j(p_j+μ(j)) − max_j(p_j−μ(j)), which can be strictly smaller than the worst case.

**Tests.**

- Exhaustive over all prefixes of length ≤ 3 on the grid {−1, −¾, …, 1}, for four moduli (harmonic, geometric, square, flat). The test checks the interval exactly, including that endpoints and midpoint are realisable and that points ε outside are not.
- Worst case attained.
- Mutation: the claim "2μ(N)" is exceeded.
- The founding-pair facts.
- The unbounded case.

**Status.** PROVED (elementary); the error radius ω/2 is CARRIER_RELATIVE_TARGETS §4. **Slogan.** *A finite prefix plus a proved modulus identifies the limit to accuracy μ(N−1). A finite prefix alone constrains nothing.*

**Boundary.** A modulus is a *proof obligation about the whole tail*. It cannot be read off the prefix, by FH-1. Boolean targets such as "L = 0" or "e_n ≠ 0 ∀n" stay discontinuous inside C_μ whenever 0 is interior to the limit interval (see FH-11).

**Interop.** Input: prefix plus declared modulus. Output: exact interval certificate (`modulus_limit_interval`, `eventually_constant_in_class`).

---

## FH-11. The verifiability asymmetry: topology and arithmetical complexity of the two regimes

**Setting.**

- X = ℚ^ℕ, with the product of discrete topologies. This is a zero-dimensional Polish space homeomorphic to Baire space.
- A decidable failure predicate fail(n, v). Examples: v ≠ 1/(n+1), or v = 0.
- Fin = {x : ∃n fail(n, x(n))}.
- Lim = {x : ∀n ¬fail(n, x(n))} ∩ c₀, where c₀ = {x : x(n) → 0}.
- Promise class Π = Fin ∪ Lim.

**Theorem FH-11.**

- **(a) Complexity.** Fin is (effectively) open, Σ⁰₁. ∀n ¬fail is closed, Π⁰₁. c₀ is Π⁰₃ (∀k ∃N ∀n≥N |x_n| < 1/k), so Lim is Π⁰₁ ∩ Π⁰₃ = Π⁰₃.
- **(b) Π⁰₃-completeness off-promise.** For fail(n,v) := (v = 0), Lim is **Π⁰₃-complete**.
  - Membership: (a).
  - Hardness: reduce P₃ = {z ∈ 2^{ℕ×ℕ} : ∀m ∀^∞n z(m,n) = 0}, which is Π⁰₃-complete [Kechris, *Classical Descriptive Set Theory*, 1995, §23.A, as I recall the reference]. The continuous map is y_k = 2^{−k} + z(m_k,n_k)/(m_k+1) along an enumeration k ↦ (m_k,n_k) of ℕ×ℕ.
  - Every y_k > 0, so y never fails. Also y → 0 iff every row of z is eventually 0.
  - Consequently, by Kelly's characterisation (limiting verifiability = Σ⁰₂, limiting refutability = Π⁰₂, relative to background knowledge), **off-promise Lim is neither verifiable nor refutable even in the limit**, by any method, computable or not.
- **(c) Relative to the promise.** Lim = Π ∖ Fin is relatively closed. Assume the richness condition R: ∀n ∃v fail(n,v). Then Lim has **empty interior in Π**: any Lim-prefix extends to a Fin point.
  - Consequently: Fin is verified with certainty (a witness halts the search), Lim is only refutable, and no Lim point is ever finitely verified.
  - For the founding pair, Π = {a} ∪ {b_H}, a is the unique non-isolated point, and b_H → a.
- **(d) Collapse criterion.** For a background class K ⊆ Π, the regime is decidable by a terminating protocol iff Lim ∩ K is clopen in K (FH-1b). Model-class restrictions that collapse it:
  1. K ∩ Lim = ∅ with a uniform witness bound. Example: K = LR_n with the law 1/(k+1), where every member fails by index 2n (FH-6c).
  2. K has a uniform horizon N (LR_n, ≤ n-state machines, weighted automata of bounded dimension). The label is then a function of x|N. This is **topological** decidability only; computing the label can still be open (FH-13).
  3. K ∩ Π is finite. Example: modulus μ = 1/(k+1) gives {a, b_0, b_1} (FH-10d).

**Status.** (a) and (c) are CLASSICAL in content: verifiability = Σ⁰₁/open and refutability = Π⁰₁/closed, as in Kelly (1996, ch. 3–4), Vickers (*Topology via Logic*, 1989) and Smyth (1992, "Topology", Handbook of Logic in CS) on observable properties as open sets; Gold (1967) for the learning frame. (b): hardness reduction PROVED here, relying on the classical completeness of P₃. (d) PROVED.

**PI's classification:** "Σ⁰₁ versus Π⁰₁ ∩ Π⁰₃" is **correct**. Sharpened: Lim is exactly Π⁰₃-complete off-promise, and relatively Π⁰₁ (closed, empty interior) on the promise.

**Boundary.** The Borel classification is about the declared observation topology. It is not a statement about provability of any particular instance.

**Test.** `test_pi03_reduction_formula`, a finite sanity check of the reduction (positivity, decay, and persistence of a bad row).

---

## FH-12. Three strictly separated finite-horizon properties of a class

For K ⊆ V^ℕ with V countable:

| Property | Topological meaning | Example | Fails |
|---|---|---|---|
| H1 uniform horizon N | prefix map injective at length N | LR_n (N = 2n); ≤ n-state machines (2n−1) | — |
| H2 finite certification (sound certifier halting on all of K) | every point isolated in K | {δ_N : N ≥ 0}: halt at the first 1 | H1 (δ_N and δ_{N+1} agree on N terms) |
| H3 identification in the limit | K countable | LR(ℚ); {0} ∪ {δ_N} | H2 (0 is a limit point) |
| — | — | 2^ℕ (uncountable) | H3 |

**Theorem FH-12.** H1 ⇒ H2 ⇒ H3. Each implication is strict, by the table. H2 ⟺ every point is isolated, and H3 ⟺ K countable.

**Proof.**

- H2 ⇒ isolated: a halt on σ with output x gives [σ] ∩ K = {x}, by soundness and because halting is prefix-determined.
- Isolated ⇒ H2: halt when [σ] ∩ K is a singleton.
- H3 ⇐ countable: Gold's enumeration learner. H3 ⇒ countable: the limit map is injective into the countable set of conjectures indexed by V^{<ℕ}. ∎

**Status.** CLASSICAL [Gold 1967; Osherson–Stob–Weinstein 1986]. Mind-change complexity versus Cantor–Bendixson rank is classical too (Freivalds & Smith 1993; Luo & Schulte 2006; de Brecht & Yamamoto). I cite these without re-proof and with uncertainty about exact statements. LR(ℚ) is perfect, so it has no finite or ordinal mind-change bound (FH-5e).

**Test.** `test_impulse_class_certifiable_but_no_uniform_horizon`.

---

## FH-13. Identification is not universal verification (statement and citation only)

1. **CLASSICAL, Skolem–Mahler–Lech** [Skolem 1934 over ℚ; Mahler 1935; Lech 1953 in characteristic 0]. The zero set {k : x(k) = 0} of x ∈ LR(K), char K = 0, is a finite set together with finitely many arithmetic progressions. The progressions are effectively computable [Berstel–Mignotte 1976], so "infinitely many zeros" is decidable. Lech's own example shows SML fails in characteristic p.
2. **Skolem problem** ("∃k x(k) = 0?" for exactly identified rational x). It is decidable for order ≤ 4 [Mignotte–Shorey–Tijdeman 1984; Vereshchagin 1985]. It is **open in general** to my knowledge. Recent work gives conditional decidability (e.g., Bilu–Luca–Nieuwveld–Ouaknine–Purser–Worrell, "Skolem meets Schanuel", 2022) and results for restricted classes. **I have not verified the current frontier;** treat this as uncertain. Hence, inside LR_n(ℚ), FH-3 and FH-5 identify the sequence after 2n terms, but the finite-counterexample regime "∃k e_k = 0" is exactly the Skolem problem.
3. **Limit clause is decidable once identified** (PROVED sketch). For identified x ∈ LR(ℚ), x → 0 iff every root of μ_x lies in the open unit disk.
   - ⇒: take the maximal modulus R ≥ 1 and the maximal multiplicity among roots of μ_x with |λ| = R. Divide by k^D Rᵏ. What remains is a nontrivial sum Σ c_i z_iᵏ with distinct unimodular z_i, whose Cesàro mean of |·|² is Σ|c_i|² > 0, so it does not tend to 0. Every root of μ_x carries a nonzero coefficient.
   - The disk test is exact (Schur–Cohn / Jury). Not implemented here.
4. **Finite-state contrast** (PROVED, tested). For an n-state deterministic machine, "symbol σ never appears" is decided by the first **n** outputs. This is sharp: the chain machine shows σ first at index n−1. For LR_n over a finite field F_q, the first q^n terms decide "∃k x(k) = 0", since the state orbit lives in F_qⁿ.

**Boundary.** Identification gives the *object*; whether its universal properties are effectively decidable is a separate question, open in general for the Skolem problem. **Test.** `test_symbol_search_bound_is_n`.

---

## FH-14 (stretch). First-order polynomial recurrences: horizon d + 2

**Setting.** x_{k+1} = f(x_k) and y_{k+1} = g(y_k), with f, g ∈ K[t] of degree ≤ d, d ≥ 1. K is a field with at least d+1 elements for sharpness.

**Theorem FH-14.** Agreement on the first **d+2** terms forces x = y. The bound is sharp.

**Proof.**

- Suppose x and y agree on indices 0..d+1.
- If the prefix x_0..x_{d+1} has a repeat x_i = x_j with i < j, both sequences are periodic from i with the same values, by strong induction, so they are equal.
- Otherwise f(x_k) = x_{k+1} = g(x_k) at the d+1 distinct points x_0..x_d. Since deg(f−g) ≤ d, f = g.
- Sharpness over ℚ: f(t) = t+1 and g(t) = t+1 + t(t−1)⋯(t−d+1). Both orbits from 0 are 0, 1, …, d, and then they differ at index d+1 (d+1 versus d+1+d!). ∎

**Tests.**

- Exhaustive over GF(5) and GF(7) for d = 1, 2. "Distinct" is certified by pigeonhole at length p²+1. The maximum agreement is exactly d+1.
- ℚ extremal for d ≤ 6, with mutation.

**Status.** PROVED (elementary). **Open.** Order r ≥ 2 polynomial recurrences of degree d. The delay-coordinate points can lie on a degree-≤d hypersurface, so the vanishing-ideal chain need not decrease at each step. For d = 1 the orbit is invariant under the line it lies on (shown in my notes, not formalised). No general horizon formula is claimed.

---

## Open / unproved but promising

1. **Mind-change sharpness.** The conservative BM learner uses exactly 2d mind changes in the worst case for all d (OBSERVED for d ≤ 4 over GF(2) and d ≤ 2 over GF(3)). Is there a learner over LR_d, with unknown d and a conjecture always required, that uses fewer?
2. **Index-refined MIMO horizon.** I conjecture κ+ν' or similar, built from observability and controllability indices. CONJECTURED, no proof.
3. **Precision–horizon curve.** Find the first k > 2n with |x_n(k) − a(k)| > ε, and look for a query-times-precision lower bound for refuting LR_n from samples of a.
4. **Order-r polynomial recurrences** (FH-14 open part).
5. **Literature check.** Do Paz and Tzeng state n₁+n₂−1 or n₁+n₂−2 for probabilistic automata? Not verified by me.
6. **Query-complexity separation.** Adaptive versus prefix-reading protocols on natural (non-pointer) classes.
7. **Bridge to §9's "probe gap".** The theorems show which *model-class declarations* turn the two-regime problem clopen. Whether any physically grounded carrier admits such a declaration remains an empirical obligation, and nothing here addresses it.

## What this report does NOT establish

- Every result is relative to declared exact model classes, and finite searches are evidence only for the enumerated models.
- No result here bears on RH, on π-normality, on actual physical carriers or brains, or on any claim that finite observations prove universal statements.
- A finite search over models is not a proof of the general theorem; the general theorems rest on the paper proofs above.
- No CI run is claimed beyond the single local test command listed at the top.

---

## Erratum added by the principal investigator after adversarial review (2026-11-14)

The text above is the workstream's report as delivered. The hostile referee
([OPUS_IV_HOSTILE_REFEREE.md](OPUS_IV_HOSTILE_REFEREE.md)) found the following; the report body
is left unchanged so the corrections stay visible.

- **FH-6, "Which b_H remain admissible" (R-22).** The clause "equivalently, the finite-surprise
  members surviving the declaration are those whose deviation comes at or before index n−1" is
  false at `n = 1`, `H = 0`: `b₀` has order 1 and first deviates at index 1. The preceding
  criterion (`H = 0`, or `1 ≤ H ≤ n−2`) is correct.
- **Tests (R-23).** `test_no_learner_is_right_on_both_extremal_sequences_at_2d_minus_1` and
  `test_declared_dimension_admits_b_H_iff_H_le_n_minus_2` could not fail as written. Both were
  replaced by tests of the falsifiable premises.
- **FH-14 (R-28).** The explicit witness `g = f + t(t−1)⋯(t−d+1)` needs characteristic `0` or
  `> d`; over other fields with at least `d+1` elements sharpness follows by interpolation.
- **Attribution (R-29).** FH-7 is the unary case of Moore's 1956 theorem; the uniqueness lemma in
  FH-5 is Massey's minimal-LFSR uniqueness at length `≥ 2L`.
