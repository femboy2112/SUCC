# Maximally non-repeating source != merely injective orbit
**Source:** SUCC clock-genesis chain #157 → #162 → #165 → #166. Independent offshoot; the original analytic Suzuki/Weil source is untouched. **RH PROVED: NO.**

## 1. Steelman: two nonrepetition notions

(A) **Free deterministic orbit:** T^a x != T^b x whenever a != b. A short law T(n)=n+1 on the source N is enough; this contains almost no per-step algorithmic novelty.

(B) **Maximally algorithmically irreducible realization:** for an infinite binary history x, fixed universal prefix-free machine U and all n, K_U(x|n) >= n-c, where x|n is the length-n prefix and c is a constant. This is the classical Levin–Schnorr criterion for Martin-Löf randomness. The infinite property is **not decidable from a finite sample**. The exact realized symbols are incompressible, not necessarily the transition rule, statistical law, or all observations. A fair-coin source can have a simple distribution despite an incompressible outcome. A single nonrepeating orbit does not imply B.

For a finite alphabet, "no finite block repeats ever" is impossible: there are only |alphabet|^k blocks of length k. A Martin-Löf random sequence almost surely has every finite word infinitely often. Maximal nonrepetition must therefore be specified in terms of **information density/incompressibility**, not absence of repeated local patterns.

## 2. Theorems and countermodels

**MSN-01 (CLASSICAL):** Every Martin-Löf random binary x is non-eventually-periodic (an eventually periodic sequence has a finite program generating its prefixes from n, whence K(x|n)=O(log n), contradictory to K(x|n)>=n-O(1)). Consequently the rooted shift orbit {shift^n x} is free. Importantly the full source *state* for the deterministic shift is the whole infinite tape x; the shift map itself is computationally simple. This is a model of maximal realization complexity, not a claim about actual physical sources.

**MSN-02 (CLASSICAL, clock no-go):** A Martin-Löf random binary x contains every finite binary word. Its shift orbit is thus dense in the full one-sided shift X={0,1}^N. The full shift contains the fixed state 000..., and if q:X->C_m is successor-equivariant then at that fixed state q(z)=q(Tz)=q(z)+1 mod m, impossible for every m>1. Therefore the orbit closure of an algorithmically random source has **no nontrivial continuous cyclic factor**. On the orbit alone the formula q(T^n x)=n mod m exists; it does not continuously descend to its full compact closure. No source clock observation may silently confuse these statements.

This *separates* (i) actual nonreturn, (ii) algorithmic incompressibility, (iii) globally realizable **continuous** clock quotients. Maximum algorithmic source novelty guarantees (i), but **does not imply (iii)**. It can coexist with maximum entropy of the full shift and an extremely simple carrier transition.

**MSN-03 (EXACT FINITE COUNTERMODEL):** A binary de Bruijn cycle B(2,k), period 2^k, contains every possible k-word exactly once in its cyclic period; yet its infinite periodic extension is computable and fails (i), (ii). Thus any finite "all distinct observed length-k windows" or finite local-entropy test fails as a global freeness/randomness certificate. Constructed independently and compared to brute-force product enumeration for k<=6; tested through k=8.

**MSN-04 (PAPER/FORMAL):** If an exact decoder d satisfies d(o(x))=x for every source state, o is injective. More generally exact target reconstruction requires ker(o) subset ker(target), not injectivity on irrelevant hidden distinctions. Source-incompressible states demand large *lossless description length*, not an inverse for every coarse-grained task. Formal standalone Lean proves the exact decoder lemma.

**MSN-05 (PAPER/FORMAL):** If T has a fixed point and target clock transition has none, no equivariant map X->Clock exists, irrespective of continuity. Standalone Lean specializes this to the two-symbol full shift and two-cycle. For arbitrary m>1 the identical one-line fixed-point argument applies.

**MSN-06 (COUNTING, not recognition):** At most 2^(n-c)-1 binary programs have length < n-c, and hence at most that many distinct n-bit strings can be produced by such programs. This counts candidate descriptions, but gives no algorithm to certify the true K(x|n) or ML randomness of an observed infinite source.

## 3. No-ghost boundary

Instrument construction under a declared fresh-state/splice program is not equivalent to an externally source-equivariant continuous measurement. A random/full-shift external carrier can possess a **free orbit** but have no continuous map to any nontrivial cyclic output, even while independent observer instruments C_m can be built.

Conversely, an odometer has all compatible finite cyclic factors and a simple deterministic transition, and need not have positive algorithmic entropy rate. Neither entropy nor information density identifies the arithmetic clock source Ẑ, its Haar calibration, or any Weil positivity.

The distinction is source *state versus mechanism versus observation*. Saying "there is nothing to model except the data" is correct for exact realization of an incompressible tape, but not for its transition law, probability law, partial invariants or resource-bounded predictions.

## 4. Falsifiers and authority

- Negative control: periodic de Bruijn period contains all blocks at any fixed order; finite novelty does not prove free orbit.
- Negative control: full shift has fixed points, even while a chosen random orbit is free and dense; no continuous universal clock factor.
- Positive control: rooted cyclic quotient C_16 -> C_8 is lawful; C_16 -> C_3 is not.
- Positive control: injective reports allow exact target decoding on attained finite records; collision of two unequal sources in one report prohibits full reconstruction.
- Program-count experiment: combinatorial bound is **not** K computation.
- External classical facts relied upon: Levin–Schnorr and ML-random ⇒ every finite cylinder recurs. These require a formal proof if upgraded to a stand-alone verified ML theorem. Lean file does **not** prove Kolmogorov complexity.

Relevant references: Levin–Schnorr criterion (https://doi.org/10.1016/j.jcss.2015.04.004); classical de Bruijn circuits and perfect necklaces (https://doi.org/10.1016/j.aam.2016.05.002).

## 5. Next verdict-changing test

Ask which source access grammar can certify a lawful modular factor without imposing one as an axiom. For genuine random/full-shift external observation, no continuous finite clock factor is possible: this is a boundary **for that carrier and morphism category**, not a general impossibility of SUCC arithmetic or of external phase clocks. To escape it, explicitly enlarge the source (e.g. add a clock coordinate), and audit what new information and causal access were assumed. Probe entropy, rank, and topological quotient as **separate coordinates**; never collapse to one "randomness score."

## Validation / integration

- Source-independent standard-library module and adversarial tests.
- Lean 4.14.0 standalone finite obstruction and decoder kernel, separately compiled in pinned CI.
- Immutable inherited original arithmetic/Gamma sources; no new RH claim.
- Branch is stacked on #166, review before integration with other drafts.
