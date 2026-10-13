# SWM-X08 independent arithmetic review

Reviewed immutable integration base:
`a4fa7c372662f7c17502c58ea78121ec864c22b2`. This second-generation investigator
read E33, E34, E36, E38, A06, F41, their relevant implementations and the
scoped Lean arithmetic file before writing new independent oracles.

## E33: finite cyclic frame centralizer — SURVIVES

Commutation with the full successor forces h(x)=x+c, even before assuming
bijectivity. Such a map on a finite cyclic carrier is automatically a
bijection. Its square with D_a commutes iff (a−1)c=0 mod m. Bezout gives
the common solution set c=j m/g with g=gcd(m,{a−1}), exactly as claimed.
Empty slopes, slope 1 and m=1 are included. A slope 2 kills the stabilizer;
odd slopes on an even clock preserve translation by m/2. On N_0, the
source hypothesis a≥2 is essential: successor plus D_1 allows h(n)=n+c.
Prime labels play no role in this proof and cannot be authenticated from
the affine relation alone.

The independent oracle enumerates every permutation at m=1,...,8:
**46,233 permutations**, then checks all action squares for seven slope
families, **56 cases**. It compares the actual permitted frames with E33's
gcd output. All agree. The new bridge additionally classifies every lawful
successor quotient, which is a different question from frame automorphisms.
The E33 Lean module proves only its declared natural-affine and generic
no-classifier lemmas; it does not prove the cyclic gcd classification.

## E36: convolution-log support — SURVIVES

The load-bearing domain is a **commutative unital Q-algebra**, with a(1)=1.
Locally nilpotent augmentation at each coefficient makes log and exp
finite coefficientwise. The Euler factors for a multiplicative function
are formal series in separate prime variables; log of their product is the
sum of their logs. Conversely exp of a sum of prime-local series is the
product of their exponentials, proving coprime multiplicativity. The
argument works even with zero divisors in the Q-algebra. It cannot be
copied without change to characteristic p, where the required divisions
may be unavailable.

At horizon N, every divisor contributing to n≤N is itself ≤N, so the same
equivalence is genuinely finite-prefix relative. It provides no statement
about unseen coefficients. The stronger ray identity b(p^k)=a(p)^k/k,
together with mixed-support vanishing, gives complete multiplicativity by
the ordinary formal geometric-series identity. E36's implementation tests
the equivalent coefficient-ray law a(p^k)=a(p)^k and reports mixed support
as a separate gate; it does not silently conflate those gates.

The independent implementation here uses literal convolution powers,
**not the production Omega recurrence**. It checks all 2,048 binary
coefficient prefixes a(2),...,a(12) and 128 fixed-seed rational prefixes
through 30. Every coefficient agrees with production and every mixed-log
support verdict agrees with direct coprime-pair multiplication. The seed
is 800836. These **2,176 cases** test a rational subdomain; the proof above,
not the sample count, supports the Q-algebra statement. There is no
source-gate, Gamma-completion, conductor or Weil positivity inference.

## E38: covariance-only source authentication — SURVIVES

The two source prefixes a(n)=1 and a'(n)=1 except a'(6)=−1 have identical
termwise squared magnitudes. Every statistic constructed solely from these
weights and a common phase-independent feature family is identical. Yet
b(6)=a(6)−a(2)a(3) is respectively 0 and −2. Thus the Boolean mixed-log
predicate is not constant on a covariance fiber and cannot factor through
that report. This is a domain-wide no-classifier theorem, not a claim that
classification is impossible on an externally authenticated singleton
source family. Keeping phases or using phase-dependent features changes
the report and lies outside the no-go hypothesis.

The independent covariance oracle uses the pair-difference identity

$$\operatorname{Cov}(X)=\frac{1}{2M^2}\sum_{i,j}w_iw_j
(X_i-X_j)(X_i-X_j)^\mathsf{T},$$

with M=sum_i w_i, rather than production's centered-feature formula. For
N=6, w_n=1/n and features (v_2(n),v_3(n)), both source prefixes give

$$\begin{pmatrix}200/441 & -10/343\\-10/343 & 390/2401\end{pmatrix},$$

whose determinant is 25700/352947>0. Positive definiteness survives the
phase mutation. This independently reproduces the nondegenerate witness.
The generic no-classifier Lean theorem was inspected: its hypotheses are
exactly equal reports and unequal Boolean targets. Arithmetic covariance
equality and the b(6) values are not silently promoted to Lean theorems.
No zero locations were supplied; no completed Weil form was constructed
or shown negative.

## Cross-check of the new theorem

Three independent finite algorithms agree for every partition through
carrier size 8: period detection, complete successor-word signatures, and
joint transition refinement. Both separate-repair orders are checked;
the nonlinear C_4 mutation disproves an unrestricted absorption rule.
The C_3 prime-dilation loop separately disproves automatic centrality.
These controls test two different invariants: quotient information and
action-group structure. They must not be collapsed into a single success
label.

Primary arithmetic context was independently reopened on 2026-10-13:
[Cuntz's original affine-semigroup paper](https://arxiv.org/html/math/0611541v1)
and [DLMF §27.4](https://dlmf.nist.gov/27.4). The paper proof is self-contained;
these sources supply classical context, not authority for unproved SUCC
extensions. Novelty remains unverified.

## Validation record

The initial probe failed because the independent checker used `Scalar.real`
and `Scalar.imag` instead of the repository's `Scalar.re` and `Scalar.im`.
This was an interface error in X08 and was corrected before the receipt
was generated. The first new Lean compilation required explicit relation
arguments to resolve higher-order elaboration; no theorem hypotheses were
weakened. Final checks performed on 2026-10-13:

| Command | Observed result |
|---|---|
| `python scripts/swarm_x08_probe.py --output research/2026-10-13/SWARM_ATLAS/X08_RECEIPT.json` | Exit 0; all independent oracle checks passed; receipt regenerated after final scope update |
| `python -m unittest discover -s tests -p test_swarm_x08_arithmetic_actions.py -v` | Six tests passed in 2.611 seconds, including full receipt replay |
| `python scripts/verify_provenance.py` | Exit 0; 72 entries, 17 byte-identical archives, 55 namespace migrations |
| `python scripts/observer_foundations_probe.py` | Exit 0 |
| `python scripts/ordinal_succ_report_probe.py` | Exit 0 |
| Lean 4.14.0 on `formal/Swarm_X08AffineRepair.lean` | Exit 0; three new general natural-source stability lemmas |
| `#print axioms` for all three new Lean theorems | Each reports no axioms |
| Lean 4.14.0 on `formal/Swarm_ArithmeticTransport.lean` | Exit 0; independent recompilation of the original six scoped arithmetic lemmas |
| `git diff --check` | Exit 0 |

The official Lean compiler uses the session's narrow procfs executable-path
compatibility shim; its kernel is unchanged. Full repository tests are
reserved for root integration. No CI success is claimed by this local run.
