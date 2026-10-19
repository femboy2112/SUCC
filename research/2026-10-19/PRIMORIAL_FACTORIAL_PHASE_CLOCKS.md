# Prime phase clocks: backward primorial/factorial reconstruction and a radical-depth completion gap

**Checkpoint 2026-10-19.** Stacked on research/rad-ris-prime-gated-succ-2026-10-19 at eeadf00729dafff3c784251c969ec2afd331818f. New-to-project presentation of classical arithmetic and topology. **ABC: OPEN. RH: OPEN. Genuine signed Suzuki S4: OPEN. Academic priority: UNVERIFIED.**

## 0. Steelman and exact clock semantics

At a newly visited positive integer n, each *declared genuine prime* q supplies an ordinary cyclic clock C_q=Z/qZ, state n mod q and update +1 mod q under SUCC. All clocks share the source time n; our chosen origin is the phase-1 target. Define forward phase slip

\[
 \delta_q(n)=(n-1)\bmod q\in\{0,\ldots,q-1\}.
\]

A perfect phase-1 lock at q is delta_q(n)=0. The finite set of clocks must be declared **before ranking** primes. For any finite clock set P and a prime p>max(P), the raw sum originally proposed is

\[
 C_P(p)=\sum_{q\in P}(p\bmod q)=|P|+\sum_{q\in P}\delta_q(p).
\]

Since no q in P divides p, the minimum possible raw sum is |P|. It occurs iff p=1 (mod q) for every q in P. We also preserve the normalized forward cost mean_q(delta_q(p)/q) and normalized circular cost mean_q(min(delta_q(p),q-delta_q(p))/q). The reference/orientation is a declared S:+1 character-clock convention, **not a quantum interference experiment**; averages do not become truth weights. Cross-window comparisons require common P, or a separately declared normalization and budget.

**Verdict:** excellent constructive finite-window arithmetic problem; not an all-lower-primes infinite lock or a theorem about actual temporal oscillators.

## 1. Exact RAD/RIS return-map theorem (PPC-01)

For a *genuine prime* p>2, every synchronized lower-prime clock is a factor of p-1:

\[
 \boxed{\{q<p:\;q\text{ prime},\ p\bmod q=1\}=\operatorname{supp}(p-1).}
\]

Its count is omega(p-1), the number of **distinct** prime factors. Its support product is rad(p-1). Its multiplicity beyond support is ris(p-1). At a synchronized prime q,

\[
 v_q(p-1)=1+v_q(\operatorname{ris}(p-1)).
\]

Thus the depth of a phase-1 lock mod q^a is exactly the q-adic valuation of p-1, not just a boolean residue. This recovers the earlier RAD/RIS chart on the **predecessor** of the observed prime. It is an identity sourced by genuine integer factorization, not a uniform ABC bound.

Two distinct legitimate objectives should not be conflated:
- *Total lock count*: omega(p-1), which may reward primes outside the first k clocks.
- *Initial prime-prefix depth*: d(p)=max{k: p=1 (mod M_k)}, where M_k is the product of the first k primes.

Example: p=870871 is prime and p-1=2*3*5*7*11*13*29. It has 7 synchronized prime clocks, but the first unaligned prefix clock is 17, so d(p)=6. On the other hand p=120121 has p-1=4*30030, so d(p)=6, rad(p-1)=30030 and ris(p-1)=4. A maximum count alone does not mean the **first** k clocks are all locked.

## 2. Backward wheel construction and its limit of inference (PPC-02)

Let q_1=2,q_2=3,... be the genuine primes, and M_k=prod_{i=1}^k q_i. CRT gives

\[
 \boxed{\delta_{q_i}(n)=0\ (\forall i\leq k)\iff n=1+tM_k,\quad t\in\mathbb Z.}
\]

If p=1+tM_k is prime, we have a verified k-clock synchronized prime. Conversely, for a fixed k, **Dirichlet's theorem on primes in arithmetic progressions**, with gcd(1,M_k)=1, guarantees infinitely many prime members; this is an *external theorem*, not a consequence of the finite wheel search.

The first prime witnesses for increasing k (t listed separately) are:

| k | first k-clock modulus M_k | first prime p=1+tM_k | t | primality of M_k+1 |
|---|---:|---:|---:|---|
| 1 | 2 | 3 | 1 | prime |
| 2 | 6 | 7 | 1 | prime |
| 3 | 30 | 31 | 1 | prime |
| 4 | 210 | 211 | 1 | prime |
| 5 | 2310 | 2311 | 1 | prime |
| 6 | 30030 | 120121 | 4 | **30031=59*509 composite** |
| 7 | 510510 | 4084081 | 8 | composite |

The table is finite, reproducible exact primality/CRT arithmetic. It does **not** establish that infinitely many M_k+1 (Euclid numbers) themselves are prime; the t freedom is essential. Every factor of 1+tM_k is outside the first k prime clocks, but the number may still be composite. The "fully aligned implies prime" inference is decisively refuted by 30031.

**Density scope.** For *fixed* k, the prime number theorem in arithmetic progressions gives number of primes p<=x, p≡1 mod M_k asymptotic to li(x)/phi(M_k). Hence among primes the **limiting relative proportion** is 1/phi(M_k), with phi(M_k)=prod_{i<=k}(q_i-1). This is an external analytic theorem for a **fixed** modulus. Letting k=k(x) increase is NOT licensed by this pointwise asymptotic and requires uniform-in-modulus estimates.

## 3. Factorial controls higher prime-power clock return times (PPC-03)

For each integer m>=2, write F_m=m!. Its q-adic exponent is given by Legendre's classical formula

\[
 v_q(m!)=\sum_{j\geq1}\lfloor m/q^j\rfloor.
\]

If p=1+t m! is prime, then p≡1 (mod q^a) for **every** q^a dividing m!. In contrast M_k holds each selected prime only once. For instance 5!=120=2^3*3*5; every p≡1 (mod 120) is aligned mod 8, 3 and 5, whereas 30 only requires alignment mod 2, 3 and 5.

The candidate m!+1 is not necessarily prime: 5!+1=121=11², 6!+1=721=7*103. Dirichlet supplies prime p≡1 (mod m!) for *fixed* m, e.g. 73=3*4!+1. Finite search failure at a chosen multiplier bound says nothing about infinite existence. A candidate with p<=sqrt cutoff receives an exact trial-factor witness before being called prime.

## 4. Full lower-prime perfect lock is impossible beyond 3 (PPC-04)

**Theorem:** the only prime p whose residue is 1 modulo **every** prime q<p is p=2 (empty condition) or p=3.

**Proof:** let p>=5 be prime and let q be its immediately preceding prime. Since p is odd, 2 | p-1, and q is odd. A perfect lock would also require q | p-1; hence 2q | p-1. Bertrand's postulate, applied to the integer (p-1)/2, gives a prime in ((p-1)/2, p-1), so q>(p-1)/2, i.e. 2q>p-1. Contradiction. Directly check p=2,3. QED.

Thus "all lower primes at 1 every time a prime appears" is not a realizable infinite integer sequence. But **every fixed finite window** can be synchronized at infinitely many primes by Dirichlet. These two distinct quantifier orders must not be collapsed.

## 5. Even all necessary sieve clocks have only finitely many perfect primes (PPC-05)

A less demanding adaptive clock window is P(p)={q prime: q<=sqrt(p)}. Such clocks suffice to test primality by divisibility, but requiring them *all at phase 1* is still too strong.

**Theorem (complete classification):** the primes p satisfying p≡1 mod every q<=sqrt(p) are exactly

\[
 \boxed{2,\ 3,\ 5,\ 7,\ 13,\ 19,\ 31.}
\]

**Proof:** list directly the primes p<49. For p>=49, put q=largest prime <=sqrt(p), r=next prime>q. Then q>=7 and p<r². We establish q#>r² for every prime q>=7:

Base q=7: 7#=210>11²=121. Inductive step: assuming q#>r², the next primorial is r#=r(q#)>r³. The prime s following r satisfies s<2r by Bertrand, while r>=11>4, so r³>4r²>s². Thus r#>s². By induction, q#>r²>p. If every q'<=sqrt(p) were a phase-1 clock, q# would divide the positive integer p-1<q#, impossible. Direct finite cases p<49 give precisely the displayed seven primes. QED.

**Scope:** classical Bertrand + elementary induction. The runtime search up to 10,000 is a separate test, not a purported proof beyond that interval.

## 6. Why primorial and factorial towers are NOT the same completion (PPC-06)

For k increasing, the integer residue system Z/M_kZ is a CRT product of **first-degree prime fields**:

\[
 \varprojlim_k\mathbb Z/M_k\mathbb Z
 \simeq\prod_{q\ \mathrm{prime}}\mathbb F_q.
\]

No q² divides any M_k, so the inverse system never supplies even the second q-adic digit. It is NOT the full profinite completion. In fact, via reduction mod every q, it is the semisimple quotient of the full profinite integers by their Jacobson radical.

For factorials, every fixed positive integer d divides m! for all sufficiently large m. Thus {m!} is cofinal in the divisibility-directed system of moduli, and

\[
 \varprojlim_m\mathbb Z/m!\mathbb Z
 \simeq\widehat{\mathbb Z}\simeq\prod_q\mathbb Z_q.
\]

This is the actual whole-prime-power completion: both support and arbitrarily deep digits. The term "Jacobson radical" in the ring quotient and the integer radical rad(n) are mathematically **different** radicals.

A finite **prime-to-prime distinguishing probe**: p=31 and p'=61 both equal 1 mod 2,3,5, but 31≡3 mod4 and 61≡1 mod4. They are identical to the 30-wheel's phase-1 first-digit observation, but q²=4 separates them immediately. The same phenomenon persists at every fixed k: CRT produces the two compatible odd residue classes 1 and 1+M_k modulo 2M_k; each is coprime to 2M_k, so Dirichlet gives infinitely many genuine primes in each class. No fabricated prime-source symmetry is required.

## 7. A true "asymptotic phase-lock" theorem and its failure mode (PPC-07)

Two facts which initially sound contradictory coexist:

1. Every fixed k admits infinitely many primes congruent 1 modulo M_k.
2. No prime p>=5 is congruent 1 modulo *all primes smaller than p*.

The apparent tension is resolved by **different quantifier orders** and completion topologies.

Choose a strictly increasing sequence of primes a_k≡1 (mod M_k) using Dirichlet. Then for every fixed q, a_k≡1 (mod q) eventually. Hence the images of a_k converge to the unit 1 in the squarefree product \prod_q F_q. We can force a_k≡3 (mod 4) for every k>=2 by choosing a_k≡1+M_k (mod 2M_k), a reduced residue class. Such a sequence **cannot** converge to 1 in full Zhat, because its 2-adic mod-4 coordinate stays 3.

In contrast, choose increasing primes b_m≡1 (mod m!), again by Dirichlet. Every fixed d eventually divides m!, so b_m→1 in **full** Zhat while b_m→+infinity in the usual real magnitude. There is no contradiction: real and profinite notions of closeness are inequivalent; these are sequences of *different primes* and not one prime satisfying all finite constraints simultaneously.

This is a valid constructive-existence theorem **conditional on the externally proved Dirichlet theorem**, not a claim that finite experiments prove the infinite sequence or that a physical supertask has completed.

## 8. ABC crucible: the most tempting conclusion is false (PPC-08)

For a prime p>2, take the trivial primitive additive triple 1+(p-1)=p. Because gcd(p,p-1)=1,

\[
 \operatorname{rad}(1\cdot(p-1)\cdot p)
   =p\operatorname{rad}(p-1)>p.
\]

Hence its ABC quality log(p)/log(p rad(p-1)) is **strictly less than 1**, regardless of how beautifully the prime clocks synchronize. In fact, more aligned *distinct* primes usually increase the product rad(p-1); the prime phase score alone cannot serve as an ABC excess witness in these triples. This explicitly kills the mistaken bridge "phase-1 prime -> exceptional ABC quality" for 1+(p-1)=p.

A less tautological hypothesis may involve structured **nontrivial** primitive sums a+b=c where c has high residual multiplicity while source clock-phase alignment controls the supports of a and b. Such a proposed inequality must be proved independently of ABC, not optimized on examples then presented as a universal theorem. RH/Weil positivity requires original authenticated prime-power, Gamma and pole data and is not implied by these congruence scores.

## 9. Crucible and acceptance criteria (PPC-09)

- **Composite Euclid mutant** 30031=59*509 is aligned with the six prime clocks 2,3,5,7,11,13 but not prime.
- **Ghost prime pair** 31 and 61 share all three first-digit clocks 2,3,5 but differ at 4; radical-phase data is not a full p-adic completion.
- **False all-lower statement** killed by previous-prime obstruction using Bertrand.
- **False infinite sqrt-window statement** killed by explicit q# growth proof and complete finite classification.
- **Support/depth confusion** killed by factorization of 120121-1 and contrast 31/61 and 870871/120121.
- **Invalid clock sources** composite q, reordered q, duplicate q, and candidate not prime rejected by the typed implementation.
- **Inference firewall** no ABC, GRH, RH or genuine Suzuki source-sign certificate follows. Existing M4 S4 source remains unresolved; paper Dirichlet and PNT-AP are external theorems, not new Lean work.

**Next discriminating mathematical program:** (i) use a *fixed* k, source-authenticated prime characters and Legendre valuations to derive exact distribution of phase-window costs, not merely a fitted leaderboard; (ii) test against rotations 1→−1, repeated prime powers and fake-composite clock defects; (iii) study uniform prime occurrence as k grows only with explicit analytic errors and an accepted PNT-AP/GRH or other precisely scoped dependency; (iv) discover a genuine, nontrivial inequality on primitive a+b=c that survives the 1+(p-1)=p negative control. The first three explore clock/source representation; the fourth alone approaches ABC.

## 10. Reproduction

Python module: `observational_succ/prime_phase_clocks.py` (typed integer budget, exact trial primality, CRT residues, Fraction scores); independent test `tests/test_prime_phase_clocks.py` (separate sieve and divisor oracles, fixed-window search exhaustiveness, actual phase-1 prime witnesses, false inputs, negative controls). The full repository status is determined by hosted CI rather than inferred from an isolated local run.

~~~sh
python -m unittest discover -s tests -p 'test_prime_phase_clocks.py' -v
python -m compileall -q observational_succ/prime_phase_clocks.py tests/test_prime_phase_clocks.py
~~~

Sources:
- Dirichlet theorem and PNT in progressions: [Kedlaya, ANT 5.4](https://kskedlaya.org/ant/chapter-5.html); [Garrett, primes in arithmetic progressions](https://www-users.cse.umn.edu/~garrett/m/algebra/notes_2023-24/21.pdf).
- Prime primorial +/- 1, Euclid numbers and the non-universal primality of M_k+1: [Prime Pages](https://t5k.org/top20/page.php?id=5&lang=en), [OEIS A018239](https://oeis.org/A018239).
- Full profinite integers = product q-adic integers: [nLab](https://ncatlab.org/nlab/show/profinite+completion+of+the+integers), [Jordan Bell, Profinite completion](https://jordanbell.info/LaTeX/mathematics/profinite/).
- Fundamental theorem of arithmetic, CRT, Legendre's formula and Bertrand's postulate are classical dependencies; the exact complete proof steps used here are displayed above.
- Existing SUCC unit/prime flat correspondence and RRT-01–10 RAD/RIS theorem dossier are explicitly **dependencies**, not independent mathematical provenance.

**Publication boundary:** NO priority proof, no physical phase measurement, no hidden zero oracle, no new claim to have proved ABC, GRH, or RH.
