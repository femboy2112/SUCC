# What the angular boundary and the aligned prime tests can determine

All statements below concern the exact primal Y with zero initial state and the eight projected taps of #499 unless another seed is explicitly named. Put e(x)=exp(2πix), X_n=16^(n−1)π for n≥1, and use circle distance in the triangular energy. Results are paper derivations with finite exact controls; no independent external peer review is claimed.

## An all-orders rational correction from the actual two-state source

**Theorem B1 (paper proof).** For integers n≥1 and m≥1 put
$$
 B_j(n)=\frac{(2j)!}{4(8n+1)(8n+2)\cdots(8n+2j+1)},\qquad
 C_m(n)=\sum_{j=0}^{m-1}(-1)^j B_j(n).
$$
Then
$$
 0<(-1)^m[X_n-Y_n-C_m(n)]<B_m(n).
$$
Indeed block n+1 of the eight-tap stream starts at Taylor degree 8n. The complete angular period is the integral of the kernel in #499. Removing n complete blocks and multiplying by 16^(n−1) leaves
$$
 X_n-Y_n=\tfrac14\int_0^1\frac{t^{8n}}{1+(1-t)^2}\,dt .
$$
Apply the *finite* geometric identity to 1/(1+u) with u=(1−t)^2. The signed remainder has integrand t^(8n)(1−t)^(2m)/[4(1+(1−t)^2)]. Its strict bounds follow by integration and the elementary integer beta integral. In particular X_n−Y_n is positive and less than 1/[4(8n+1)]. The displayed formula requires no digit input to produce C_m.

Fix h∈ℤ and m≥1. The coefficients
$$
 e(hX_n)-e(h(Y_n+C_m(n)))
$$
have magnitude at most 2π|h| B_m(n)=O_h,m(n^(-2m−1)). Thus the difference of the two signed power series extends to the unit circle with 2m−1 continuous derivatives (uniform absolute convergence of each derivative). For m=1 this gives a bounded loss in **all unnormalized partial sums** and a continuously differentiable boundary difference. It subtracts an explicit angular endpoint bias. It gives no value for the shared leading boundary residue. C_m is an observer correction; inserting it into the arithmetic forcing would change the source.

A linear number of local moment terms gives analytic continuation of the *difference* past the boundary. Set m=4n; the error integrand is bounded by [t(1−t)]^(8n)/4 ≤16^(−4n)/4. Thus the generating-series difference for the rational correction C_(4n)(n) is holomorphic for |z|<16⁴. With m=n² its integrand is at most (4/(n+4))^(8n)/4 by maximizing t^(8n)(1−t)^(2n²). This makes the difference entire. The number of rational terms grows with n in both statements. Both corrected and completed series can still share the same unknown singular boundary.

For the uncorrected phases, (1−r) times the radial-series difference tends to zero by O_h((1−r)log(1/(1−r))). Thus the bounded-sequence Abel/Cesàro theorem in #496 transports the same cancellation gate to Y. The gamma-window theorem #498 singles out an individual original injection; it does not measure the accumulated old-cofactor address. The finite line-to-circle ambiguity of #493 is an independent choice about the observer. Here the circle, oriented character e(hx), time origin, and translation to the authentic integral are all declared; uniform Haar is absent from those assumptions.

## Full aligned prime tests and a growing collection of coherent impostors

Write the same-forcing rational-seed variant as Y_n(s)=Y_n+16^n s. Fix an odd prime p>8k, k≥1, χ=χ₋₄(p), with s p-integral. The raw left projection pY_(kp)(s) mod p is independent of s. The aligned difference satisfies instead
$$
 pY_{kp}(s)-\chi Y_k(s)\equiv-\chi16^k s\pmod p
$$
by (PQ-2) and (PQ-4) of #499. In particular one aligned test detects 1/5 at every eligible p>5. This rectifies a possible reading of the generic-seed sentence in PQ-06: it is the raw mass at kp that is seed-blind. A finite collection of aligned tests at primes P detects a rational seed unless each prime divides its reduced numerator (when every prime is eligible). At k=1, testing all eligible primes identifies zero among fixed rational seeds. Finitely many tests already suffice given a certified bound H for the absolute numerator when the prime product exceeds H.

**Theorem B2 (paper proof, assuming the denominator asymptotic and conductor divisibility of #499).** Let 0<c<4−log 16, with natural logarithms. For every sufficiently large integer A there is a nonzero bounded rational seed s_A with odd denominator dividing den(Y_A) such that ALL self-aligned tests for primes 8<p≤cA and ALL k with 8k<p hold. The complete same-forcing path on the epoch [A,2A) stays within
$$
 R_A=1/[4(8A+1)]+O(\exp[-(8-2c-2\log16+o(1))A])
$$
of 1/5 on the circle. Hence for any q≥2 its radius-1/q normalized triangular energy satisfies J≥q(1−2qR_A)_+. At the target schedule q≈log A this lower bound is q(1−O(q/A)). The seed can in fact be chosen with 0<s_A<3·16^(−A) using only observations through A. Every witness is a wrong seed, even when the finite arithmetic tests and the cumulative conductor from time A onward are correct.

*Construction.* Set B=2A−1, Q=den(Y_A), P=product of all primes 8<p≤cA, and delete all their powers from Q to get D. By the prime number theorem log P=(c+o(1))A. By the odd LCM divisibility of #499, higher powers in Q have logarithmic mass O(sqrt(A)log A), since the number of possible base primes is at most sqrt(8A) and each contributes at most log(8A) beyond its first power. Consequently log D≥(8−c−o(1))A. Set
$$
 s_* = 1/5-Y_B/16^B,\qquad
 s_A=\frac P D\operatorname{round}(D s_*/P).
$$
The seed construction uses only rational taps. Since Y_B/16^B→π/16 and 0<π/16<1/5, s_A→1/5−π/16>0. Its reduced denominator divides D and its reduced numerator is divisible by P. Its difference from s_* is ≤P/(2D). Initially allowing the seed as an extra denominator has no effect on the cumulative conductor past A since den(s_A)|Q.

For A≤n≤B the identity
$$
 Y_n+16^n s_*=16^n/5-\sum_{j=1}^{B-n}16^{-j}r_{ang}(n+j)
$$
is exact. Each of these forcing terms is positive: the positive taps dominate the later negative taps in every block (#499 PQ-06, or integrate t^(8n) times its positive numerator). The partial sum is ≤the full tail X_n−Y_n from B1. Since 16≡1 mod 5, the claimed radius follows by adding 16^B P/(2D); any pair distance is at most 2R_A. The authentic selected seed is literal zero. This theorem changes the order of neither quantifier: for each epoch there is a possibly different mutant; it yields no fixed rational impostor surviving infinitely many aligned primes.

**Epoch-start construction and early invisibility.** The preceding argument needs a rational prefix through B. To eliminate that look-ahead set H=Y_A+C_(4A)(A), j=ceil(H−1/5)+1, and s_*=(j+1/5−H)/16^A. Thus 1≤16^A s_*<2. Again round to the P/D grid. By B1, |X_A+16^A s_*−(j+1/5)|<16^(−4A)/4. At time n∈[A,2A) this discrepancy on the circle is at most 16^(n−A) times the initial discrepancy plus 16^n P/(2D) from rounding. Subtract X_n−Y_n to recover the claimed R_A; the new analytic error is at most 16^(−3A)/4 and is absorbed. Since P/D=o(16^(−2A)), eventually 0<s_A<3·16^(−A). Consequently for each δ∈(0,1) every earlier n≤(1−δ)A differs from the authentic real orbit by at most 3·16^(−δA). The construction keeps its exact nonzero initial rational state, so reading that datum exactly still distinguishes the rival immediately. The observer receives no completed digits: H uses Y_A and elementary rational moments. Extra preregistered epochs A=83,131,167 test this construction separately.

**Old-cofactor strengthening with integer lifts.** If an a priori size bound on the real seed is dropped, the threshold extends to every c<8−log 16. At time A the translated D-grid {Y_A+16^A j/D mod 1 : j mod D} has covering radius 1/(2D) because 16 is a unit mod D. Choose j whose phase is within that distance of Y_A+16^A s_*, then add an integer multiple of D to j to make j≡0 mod P. Coprimality of D and P permits this. This preserves every circle phase at integral times. For n≥A the new perturbation is ≤16^(B−A)/(2D) on the circle, exponentially small for c<8−log16. The proof allows the initial real lift to grow, exactly where the previous theorem imposed a stronger restriction.

**Four-pole and primal old conductors together.** Let G=gcd(den U_A, den Y_A). Both divide the odd part of lcm(1,…,8A), whose logarithm is (8+o(1))A. Since den U_A and den Y_A have log sizes (6+o(1))A and (8+o(1))A, the product identity for gcd and lcm yields log G=(6+o(1))A. Repeat with Q=G. Using the same rational seed in U and Y and keeping the zero-seeded radial channel Z, the exact relation U_n(s)=Y_n(s)+Z_n transfers the near-1/5 estimate with at most 1/(32A+16) extra radius. Its denominator adds nothing to either cumulative conductor after A. The bounded seed theorem now holds for 0<c<3−log16. The integer-lift version holds for 0<c<6−log16; taking c=2 includes **every eligible primal aligned return with kp≤2A**. For each such prime the s-shift is zero mod p at every p-integral early observation and its p-normalized return equals the authentic one. For the original-source action S_a use the authentic transformed source on the right: p U_(kp)(s) equals the original right side; any p-integral scalar multiple of the shift on that right side also vanishes mod p. These claims concern the declared congruences, not exact equality of rational prefix states or survival of the same reduced denominator of each individual state.

**Observer discrimination.** A one-time inspection of the literal zero seed rejects all these mutants. Theorems about signed cancellation must quantitatively use that datum. Verifying selected local tests at Θ(A/log A) primes, every eligible multiplier k simultaneously, retaining the exact old denominator grid and the authentic forcing, still admits maximal energy on each prescribed epoch. This result puts a lower bound on the information demanded of any proof based solely on those tests. It does not show that larger prime suites suffice. A verdict-changing probe would exploit an upper bound for the *actual* old-cofactor, centered on the ancestral numerator, finer than the surviving prime-multiple mesh, and use it at enough time pairs to bound J.

## Recovery of the selected logarithmic deficit, with priority correction

**B3 (inherited mechanism; angular transfer).** For each fixed integer h≠0 and all N≥2,
$$
 |\sum_{n=1}^N e(hY_n)|\le N-c_0\log N+O_h(1)
$$
for some absolute c₀>0. #403 already has a stronger-constant version for U, and the sparse-digit barrier is in the repository's zero_boundary_dispersion/diophantine work. A direct transfer of the *adjacent jumps* avoids spending an O_h(log N) error on the whole sum.

Put α=15hπ. Its irrationality exponent is <8 by the Zeilberger–Zudilin theorem and invariance under multiplication by a fixed nonzero rational. For every sufficiently large m some j∈[m,8m] has ||16^jα||≥1/32. Otherwise the signed representatives in (−1/32,1/32) multiply by 16 with no wrap (the possible integer difference has absolute value ≤17/32<1). This gives a rational a/16^m approximating α with error <16^(−8m)/32, impossible infinitely often. Reduction of the fraction only strengthens the contradiction, and the denominators of a convergent sequence of rational approximations to an irrational tend to infinity. The completed adjacent jump is 16^jα for n=j+1. B1 gives ||h(Y_(n+1)−Y_n)||≥1/64 for large m at this n. The two unit summands lose at least 2(1−cos(π/64)) from two by triangle inequality. Take disjoint pairs from m=9^t, discarding the first finitely many and the last incomplete window. One may take c₀=2(1−cos(π/64))/log 9. Abel summation also gives an unnormalized Abel deficit of order at least log(1/(1−r)) compared with the trivial sum; the *normalized* deficit from this bound tends to zero.

For context the comparison α*=Σ_{j≥0}16^(−3^j) has irrationality exponent 3. Its coprime truncations have denominators d_j=16^(3^j) and errors in [d_j^(-3),2d_j^(-3)]. For a rational a/q choose the first j with d_j²≥4q. If it equals the truncation, the error is ≥q^(-3). Otherwise denominator separation gives error ≥1/(2qd_j), with d_j≤(4q)^(3/2) for large q. The truncations attain exponent 3 in the limit. Each digit at a position v≤N contributes at most Σ_(r≥1)16^(−r)=1/15 to Σ_(n<N)||16^nα*||. The digits v>N together contribute at most Σ_(v>N)16^(N−v)/15=1/225, counting even all possible future positions. Thus |Σ e(16^nα*)|≥N−O(log N). This hostile control pays the sharpness debt of the transferring argument. It has different forcing and does not test primal arithmetic.

## Sources and reproduction

- [#499: PQ-02 through PQ-06](https://github.com/femboy2112/SUCC/blob/4ff640637d18b8161599402f7c6ba23388a63652/research/2026-11-04/prime_character_primal/PRIMAL_QUOTIENT_THEOREM.md). The signed taps, angular integral, aligned congruence, and denominator asymptotic enter explicitly.
- [#493](https://github.com/femboy2112/SUCC/pull/493), [#496](https://github.com/femboy2112/SUCC/pull/496), [#498](https://github.com/femboy2112/SUCC/pull/498). Proof-file Git blobs 6ab8c97605194ca2676b42bacae8c473bbca30d7, 311ed09dbde6fbbc3f905d36e0fcaa81ffbc884d, f3ed7f0a9d87111052ccad12e0a9aacc3903e2b5 respectively.
- [#403](https://github.com/femboy2112/SUCC/pull/403), [#479](https://github.com/femboy2112/SUCC/pull/479). Prior source-selected logarithmic saving and different lag exclusions.
- D. Zeilberger and W. Zudilin, [The irrationality measure of π is at most 7.103205334137…](https://msp.org/cnt/2020/9-4/moscow-v9-n4-p06-p.pdf), Moscow Journal of Combinatorics and Number Theory 9 (2020). Only the published bound <8 is used.

Run `python3 probe.py` from this directory. Its exact rational result can be compared byte-for-byte with RECEIPT.json. Direct eight-tap rational evolution checks all finite phase and p-residue predictions, including the altered seed. For old conductors A=79,107,149 all three radius criteria passed. For the tail checks the direct future partial sums include a rigorous upper bound on the omitted terms. The three stages share mathematical source data and software authorship. No independent scholarly priority, hosted execution, or long-time cancellation is asserted.
