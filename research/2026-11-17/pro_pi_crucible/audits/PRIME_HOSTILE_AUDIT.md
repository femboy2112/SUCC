# Hostile audit: effective BBP prime survival

**Audited object:** `/workspace/scratch/d2afcbfb001f/prime_scratch/EFFECTIVE_PRIME_SURVIVAL.md`, read during the present operation. **Prior-art comparison:** `research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md` at main `81be6b897ae980b801a3b9de9e22ef81e8360bfb`.

**Authority:** a separate same-model line-by-line derivation and independently written exact edge checks; not external peer review, not Lean, and not an independent arithmetic source. The audit changed no repository or prime-agent files.

## Verdict

The finite certificate EPS-01, shrinking cutoff EPS-02, and denominator-saturation bound EPS-03 survive this audit. I found no mathematical counterexample or load-bearing gap. Two minor wording/completeness improvements are recommended below. Neither changes the result.

1. In the 4j-lane denominator bound, replace `at most k-2` by `at most max(0,k-2)`; k=1 gives a numerator factor 2, not a negative denominator exponent.
2. To make the effective threshold completely explicit, put `c=2-40 log(2)/A>0`. Choose integer n_A with `log n_A>=max(2,2/c)` and check `c log n_A-2 log log n_A+2 log A-log19>=0`, together with `A n_A/log n_A>max(7,sqrt(8n_A))`. The first expression, Y, and Y/sqrt(n) are then nondecreasing for all n>=n_A. This explains why a finite threshold check proves the all-later quantifier.

## 1. Four-lane normalization

Writing the original forcing as

`4/(8j-7)-1/[2(2j-1)]-1/(8j-3)-1/[2(4j-1)]`

is exactly correct. For p odd with p^2>8n, all native denominators are <8n, so each p-divisible denominator is kp with k<p and contains p exactly once. After multiplication by p, every other term vanishes modulo p. The normalization by `16^(n-(p+1)/2)` is a unit, including negative exponents.

For the 8j lanes, direct expansion gives

`4(j0-j)=((4-k)(p-1)+8-k-b)/2`.

Euler's criterion for 2 has sign +1 in classes 1,7 mod8 and -1 in classes 3,5. Since k is odd, `chi^(4-k)=chi`. This yields precisely the two displayed 8j coefficients. The 4j exponent decomposes as `(2-k)(p-1)+(3-k)`; the coefficient -1/2 yields `-2^(2-k)/k`. The 2j exponent is `2(1-k)(p-1)+2(1-k)`; its coefficient gives `-2^(1-2k)/k`.

No source lane or sign is missing. The congruence remains valid before the reference time j0.

## 2. Entry orders and signs

For p=1 mod8, the two 8j lanes have k=1,5 mod8. For p=5 they exchange these classes and chi changes sign, leaving the same positive series `4*16^-l/(8l+1)` and negative series `-16^-l/(8l+5)`. The 4j and 2j series are also exactly as stated. The first birth is the +4 term in both cases.

For p=3 mod8, the 8j lanes give the negative k=3 series and positive k=7 series; for p=7 they exchange. The 4j lane contributes `-2*16^-l/(4l+1)`, and its k=1 term enters first. Comparing the actual event times verifies the claimed birth formulas in all four classes. Subsequent authentic initial segments are covered by the stronger arbitrary-later-subset bounds.

The constants recompute exactly:

`4-(1/5+1/6+1/2)*(16/15)=692/225>0`;

`-2+(1/14)*(16/15)=-202/105<0`;

`(2+2/3+1/2)*(16/15)=152/45<64/15`.

The finite number of positive or negative terms makes the stated absolute upper bound strict. This proves nonzero rational F for every admissible chronological entry pattern. The manuscript correctly does not infer nonzero modulo p without the height argument.

## 3. Height bound and finite certificate

Every k is at most K=floor((8n-2)/p)<p. The 8j coefficients require at most floor(K/2) powers of 2 in their denominators. The 4j event condition gives 2k<=K, and the 2j condition gives 4k<=K. Using max(0,k-2) in the former and 2k-1 in the latter proves the common bound. Hence the reduced denominator D divides `2^floor(K/2) Lambda_K` and is prime to p.

With F=A/D in lowest terms and `0<|F|<64/15`,

`|A|^2<(4096/225)*32^K<19*32^K`.

Thus `p^2>=19*32^K` gives `0<|A|<p`, with no problematic equality case. F is nonzero modulo p. Because the original rational state has p-valuation at least -1, the nonzero principal part proves valuation exactly -1.

## 4. Elementary LCM lemma

For t=ceil(K/2), the exponent of a prime in Lambda_K/Lambda_t is at most one: two newly acquired powers would require a scale increase greater than two. Any prime in the quotient has a power q in (t,K]. Its q-term in the factorial-valuation expression for `binom(K,floor(K/2))` is exactly one, and all other terms are nonnegative. The quotient therefore divides the binomial coefficient.

The induction is valid at K=1 and K=2. For K=2m the binomial upper bound is 4^m. For K=2m+1, its two equal middle binomial coefficients sum to at most 2^(2m+1), so each is at most 4^m; t=m+1<K for m>=1. Both cases yield Lambda_K<=4^K. No prime number theorem or hidden asymptotic result enters.

## 5. Shrinking cutoff

For Y=A n/log n, `K<=8log n/A`. The sufficient inequality follows from

`2log p-log(19*32^K) >= (2-40log2/A)log n-2loglog n+2log A-log19`.

The leading coefficient is positive exactly when A>20log2. Eventually Y>max(7,sqrt(8n)), so every prime in the claimed range meets all other EPS-01 hypotheses. The monotonic threshold recommendation above pays the effective all-later quantifier directly. Taking a countable sequence of A decreasing to 20log2 proves the limsup assertion; no uniformity in A at the endpoint is claimed.

## 6. Native denominator and small-prime powers

The collapsed source fraction has the stated numerator `120j^2-89j+16` and an odd denominator. Also 2r(j) has denominator dividing the LCM of the four odd native denominators. Since multiplying a rational with odd reduced denominator by 2 leaves its reduced denominator unchanged, Q_n divides L_n.

For p>Y under EPS-03, p^2>8n and `p^2>Y^2>=19*32^(8n/Y)>=19*32^K`, so all born primes beyond Y survive. They occur only to exponent one in L_n. Every lost factor is therefore supported at p<=Y.

The first-power logarithmic loss is bounded by `log Lambda_floor(Y)<=Y log4`. All extra powers have p<=sqrt(8n); counting at most sqrt(8n) primes and charging each at most log(8n) is crude but valid. Thus the claimed `Y log4+sqrt(8n)log(8n)` bound follows. Since `(log n)^2/sqrt(n)->0`, Y=A n/log n yields O(n/log n). Small primes and existing cancellations are accounted for, not silently excluded.

## 7. Strict novelty relative to CG-01 and remaining boundary

CG-01 already proves sign nonvanishing for each fixed condensed packet and survival for primes p>=epsilon n after an unspecified threshold depending on fixed epsilon. It explicitly does not control the exceptional numerator set uniformly as packet depth grows. It already proves rate 6 and the fixed-filter dichotomy.

The new work supplies an explicit exponential numerator-height bound in the growing quotient depth K. This justifies p of order n/log n, and bounds the native-denominator loss by O(n/log n) without PNT. Those are strict quantitative refinements of the cited prior statement. They are not a new derivation of rate 6 and do not prove wall density, R0, or signed Weyl cancellation.

In particular, all principal parts remain unchanged by adding any integer to a rational state. The new theorem constrains the authentic reduced fractional denominator but does not yet constrain the terminal integer quotient. The stated exact source and literal zero seed are retained, but the argument itself also works for a fixed rational seed outside its denominator primes; it is not a zero-seed selection mechanism.

## Exact edge checks

An independently written Fraction script (no imports from the prime agent's code) checks primes 11,13,17,23, covering all four classes, at every born time before their p^2>8n boundary. It compares direct original recurrence residues to all four normalized lane formulas, verifies sign/height bounds, and checks certified survival. It also checks the LCM divisibility and bound at selected endpoints adjacent to powers of two. Output is in `../evidence/prime_independent.txt` (integration-adjusted path; final replay: `../evidence/prime_independent_final.json`). These finite checks supplement the derivation above; they do not prove the universal result.
