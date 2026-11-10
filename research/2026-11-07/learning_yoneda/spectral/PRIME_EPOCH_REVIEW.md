# Independent spectral review of the source-prime epoch theorem

Review target: `../arithmetic/PRIME_EPOCH_THEOREM.md`, PE1–PE11.
Reviewed content SHA256:
`683abd11cbf009660bd28c84ffe5a8e6d8319cbc96ad19bdf6a43263deb4b774`.
Reviewer: the spectral subagent, separately assigned by the root. This is
another same-model reasoning pass, not independent scholarly peer review.
No new large numerical run or Lean verification was performed for this review.

**Verdict: the stated mathematical implication survives.** The following
load-bearing steps were separately reconstructed.

1. For p=1 mod8, the first four positive pole occurrence candidates are
   `(p+7)/8`, `(p+1)/2`, `(5p+3)/8`, `(3p+1)/4` for factors
   `8n-7`, `2n-1`, `8n-3`, `4n-1`. The next `8n-7` occurrence uses9p.
   Hence the first two source-pole times are exactly those in PE1.
   The first residue is4/p, nonzero, with no earlier p-denominator.
2. `16^((p-1)/4)=2^(p-1)=1 modp`; the order therefore divides L.
   `[L+1,2L+1)` lies in the first clean lifetime, contains L integers,
   and covers an integer number of full cosets. The phase coefficient
   in PE4 is nonzero when p does not divide h.
3. If an odd prime p<=x has order at most p^(1/3), it divides one of
   `16^j-1`, j<=floor(x^(1/3)). The product's base-two logarithm is
   less than `2M(M+1)`. Its distinct-prime count gives the asserted
   O(x^(2/3)) bound, which is negligible compared with x/logx.
4. Fixed-epsilon PNT intervals in1 mod8 retain good primes for every
   sufficiently large x. This proves the largest-good-prime ratio limit.
   It does not assert a quantitative shrinking-gap theorem or convergence
   rate for that selector.
5. The stated Bourgain–Konyagin import matches Theorem2.1 on printed page78:
   subgroups of size at least p^delta have a uniform nontrivial additive
   character saving with a positive delta-dependent exponent. The primary
   PDF was opened independently during this review. Applying delta=1/3
   is legitimate. [Primary paper](https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf).
6. For uniform measures on two finite sets, the overlap mass is their
   intersection size divided by the larger cardinality. The L1 weight
   difference in PE7 is exactly twice one minus this quantity. With
   L<=A-1, the intersection is `max(0,2L+1-A)`, including the endpoint
   correction. Thus the clean interval covers all but o(A) terms of
   the actual dyadic epoch and the error tends to zero uniformly in h.
7. The factorization `a_n b_n=e(hU_n)` is exact. The covariance in PE10
   is explicitly bilinear rather than Hermitian. Its difference from the
   original Weyl mean is bounded by the proved local mean, since |E b|<=1.

One notation clarification was requested: define multiplicative order and
the exceptional-prime count only for odd primes, since ord_2(16) is undefined.
The selector itself already excludes this exceptional prime, so this does
not affect the proof or conclusion.

The local theorem advances the #529 component: actual chronological
prime-character cancellation is now available on every sufficiently large
original epoch, with a deterministic prime selector and uniform nonzero
local frequencies. It is not merely a finite subgroup ensemble substituted
for the history: the clean source chronology proves equality with the
subgroup average, and the overlap argument transfers it to the epoch.

The claim remains strictly local. Any fixed rational seed has identical
p_A-principal parts once p_A avoids its fixed denominator. Thus this result
does not isolate the literal zero seed, bound the complementary covariance,
or prove any full real Weyl saving. PE12 retains the remaining normality
obligation exactly. No worldwide priority claim was checked or established.

**π base-16 normality: OPEN. RH: OPEN.**
