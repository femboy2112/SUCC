# RBP: rational-base integer carries, Pascal decimal source and π-normality boundary

**2026-10-24. Research-only. Parent draft [#275](https://github.com/femboy2112/SUCC/pull/275) at 7c5d5b8856a1d132fb941ae40c946c0565918b36.** The BBP source is kept at U_0=0 with its original four-pole forcing. No π-normality proof, new Lean kernel authority or academic priority claim. Paper algebra, classical inputs, exact finite probes and open estimates are separated.

| Claim | Domain and precise quantifiers | Status | Evidence or falsifier |
| --- | --- | --- | --- |
| RBP-01 | Every coprime integers p>q≥1 and N≥0 have a unique finite p/q integer expansion via qN_i=pN_(i+1)+a_i | CLASSICAL | Akiyama–Frougny–Sakarovitch; exact rational-base roundtrips |
| RBP-02 | For p=q+1, every canonical finite word gives N=Σ_j q^(−j−1)Σ_(i≥j)binom(i,j)a_i | PROVED PAPER | finite Pascal binomial identity; exact Fraction checks |
| RBP-03 | Integer p in rational base p/(p−1) has LSD-first digits 0,1,...,p−1 | PROVED PAPER / VERIFIED FINITE | canonical quotient chain; tested p=2..29 |
| RBP-04 | Length L_(p/q)(N)=log N/log(p/q)+O_(p,q)(1) for N→∞ | PROVED PAPER | two-sided floor-contraction bounds |
| RBP-05 | For every fixed depth L, p/q low digit words biject Z/p^LZ; explicit inverse N≡q^(−L)Σa_i p^i q^(L−1−i) mod p^L | PROVED PAPER | telescoping and congruence induction; exhaustive small powers |
| RBP-06 | The rational-base 11/10 integer prefix is an 11-adic digit address while its real evaluation has denominators 10^i | PROVED TYPED DISTINCTION | RBP-05; not a Z_2↔Z_5 field isomorphism |
| RBP-07 | For actual BBP y_n={U_n}, C_n=floor U_n and literal c_n=floor(16y_(n−1)+r(n)), C_n=Σ16^(n−j)c_j | PROVED PAPER | authentic source recurrence, independent Fraction check |
| RBP-08 | ord_(11^L)(16)=5⋅11^(L−1) for every L≥1; index exactly two in (Z/11^L)^× | CLASSICAL / PROVED PAPER | ord_11=5, v_11(16^5−1)=1 and odd-prime LTE |
| RBP-09 | The low L rational-base 11/10 digits of literal C_n, and their multiplicative character cocycle, are exact source-labelled finite observers | PROVED PAPER | RBP-05, RBP-07, finite character factorization |
| RBP-10 | In five declared finite selected windows, C_n equals floor(16^(n−1)π) | CERTIFIED FINITE ONLY | independently enclosed Machin rational intervals; near-one boundary elsewhere OPEN |
| RBP-11 | With H_11=(I+2E)/3 and V_j=H_11^jU_0, k-th Pascal difference Σ(−1)^(k−j)binom(k,j)V_j=(2/3)^kΔ^kU_0 | PROVED PAPER | exact operator binomial theorem; independent source test |
| RBP-12 | For every k≥1, D_k=10^kπ/16−(−2/3)^kR_k with 0<R_k<π/16 | PROVED PAPER / CERTIFIED FINITE | inherited positive BBP Hausdorff tail; rigorous Machin oracle k≤64 |
| RBP-13 | v_2(D_k)=3k−s_2(k)−1 for every k≥1 | INHERITED PAPER PROFILE | #272 Mahler valuation, multiplier (2/3)^k, verified k≤79 |
| RBP-14 | All q with 1≤q≤15: H_(q+1)−I=(q/15)Δ; geometric real error for q<15 | PROVED PAPER / INHERITED GENERALIZATION | exact consecutive multiplier factorization; q=15 lacks geometric gain |
| RBP-15 | For actual source-selected W and integer C_n, p/q digit-cylinder observable is a finite mixed real/p-adic Fourier character average | PROVED PAPER | exact roots-of-unity orthogonality, not an estimate |
| RBP-16 | Five exact source-window residue histograms and joint phase-vs-11-digit counts | VERIFIED FINITE | finite calibration values and reproducible oracle; no rate |
| RBP-17 | True centered pair gate kappa=0 split by same/different literal C mod11, with diagonals retained and reported separately | VERIFIED FINITE | p=137,281,521, tau=1/4 and 1/16, exact Fractions |
| RBP-18 | Uniform p=11^L suffix words of integer prefixes for every fixed L can coexist with a base16-nonnormal real number | PROVED PAPER COUNTERMODEL | binary {0,1} digit-driven finite irreducible Markov chains; source changed |
| RBP-19 | Marginal 11/10 word fairness alone implies π hexadecimal normality | REFUTED AS SOURCE-AGNOSTIC IMPLICATION | RBP-18; does not refute a theorem using actual BBP coefficients |
| RBP-20 | Authentic selected mixed-source Fourier cancellation, or source-specific real 1/16 loss at every required scale | OPEN | source forcing, initial state, selected pair mask and signed characters all essential |
| RBP-21 | Whole SUCC repository test suite or Lean kernel proof on the new published tree | NOT CLAIMED | isolated local 13 tests + counted exact predicate checks; hosted CI separately |

**Steelman–crucible–verdict:** the additive rational-base representation is exact and the source gives a genuine p=11 lift, but the real/pi digit-frequency conclusion requires a new signed BBP estimate. Do not substitute the known rational-base integer digit-frequency theorem, Haar ensembles or finite equalities for this selected-source estimate.

[Research synthesis](../research/2026-10-24/PI_RATIONAL_BASE_BBP_SYNTHESIS.md) · [Production](../observational_succ/pi_rational_base_carry.py) · [Tests](../tests/test_pi_rational_base_carry.py) · [Probe](../scripts/pi_rational_base_carry_probe.py) · [Validation](../research/2026-10-24/PI_RATIONAL_BASE_VALIDATION.md).
