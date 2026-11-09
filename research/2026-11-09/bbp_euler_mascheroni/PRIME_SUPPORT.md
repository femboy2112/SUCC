# Two prime-support clocks: source pole births versus universal q-divisor denominators

**Boundary:** Prime-factor support of rational terms is not the same mathematical object as the prime support of an irrational real number. π and γ have no canonical finite rational prime-factor decomposition. Statements here concern integer/rational denominators and rational coefficients of logarithms.

## Source-pole clock

The four poles of the original forcing are `(8n−7,8n−4,8n−3,8n−2)` with coefficients `(4,−2,−1,−1)`. At time n=7, its last pole is 54=2·3³; the reduced source r(7)=5273/911547 has v3=−3. At n=8, the last pole is 62=2·31 and reduced r(8)=776/179645 has v31=−1. Earlier source times have at worst 3² in their reduced denominators and no 31. Therefore the exact 8-step source block `R_8(1)` necessarily preserves v3=−3, v31=−1 despite all signed interference: no other term can cancel the uniquely most p-singular birth.

The normalization 

`C_g = 64 R_g(1)/(16^g−1)`

contributes v3(16^8−1)=1 at g=8 and v31(16^8−1)=0 (since ord_31(16)=5). Hence v3(C8)=−4 and v31(C8)=−1. The exact fully reduced denominator is

`665391252178290169344635447625`

with factorization

`3^4 · 5^3 · 7^2 · 11 · 13 · 17^2 · 19 · 23 · 29 · 31 · 37 · 41 · 53 · 61 · 257 · 65537`.

There are clearly many primes besides 3 and 31. The final two Fermat factors 257 and 65537 arise from the radix normalizer `16^8−1`, not uniquely from the original four-pole source.

## Universal q-Gamma/Lambert clock

For q=1/16, the canonical q-Euler constant has `sum_{n≥1}1/(16^n−1)` inside its defining expression. Prime31 enters denominators at n=5 (order of 16 mod31). The prime-power 27 first divides `16^9−1` (order of 16 modulo27 is 9). These event times do not agree with the *original source* n=7 and n=8. For any odd prime p, some n satisfies p|16^n−1, so the universal q series is not a selective filter for the BBP source.

The same Lambert series is `sum_{m≥1}tau(m)/16^m`, with tau(m) the number of divisors. Here tau(27)=4 and tau(31)=2. Coefficients of this series reveal multiplicative arithmetic, but are not amplitudes of original zero-seed π digits.

## Mellin rational-log clock

At integer positive Laplace clock a, the exact Mellin first-jet correction relative to gamma is `1+sum_p L_p log p` with rational `L_p` evaluated by the original pole and blocking data. At a=1,g=8, the **unique** logarithmic contribution from original denominator 62 gives the coefficient `L_31=−1/(62 R_8(1))`, which is nonzero. This identifies a genuine source birth that cannot be detected by looking at the q-integer blocker alone. But a log-prime coefficient in an auxiliary source moment does not bound a real-circle Weyl sum or imply equidistribution.
