# Prime layers, denominator loss and actual time differences

Research note at the source contract of #497/#499. All claims below are paper arguments. Exact finite tests are additional checks. The source seed equals zero, and the radix equals 16. No external referee or priority claim.

## Individual taps determine every top digit

Put j(i)=1+(i−1 mod 8), b(i)=ceil(i/8), and let w have eight rational entries. Set
$$
 T_n(w)=16^n\sum_{i=1}^{8n}16^{-b(i)}w_{j(i)}/i.
$$
This is the literal zero-seed source, with original taps P=(4,0,0,−2,−1,−1,0,0). For odd a mod 8 write c(a)=+1 at 1,7 and −1 at 3,5. Set
$$
 (S_aw)_l=c(a)^l2^{(j(al)-l)/2}w_{j(al)},\qquad
 L_a(s)=\sum_{i=1}^s16^{-b(i)}(S_aw)_{j(i)}/i.
$$
Here rational powers of two have integer exponents by parity. For ANY odd prime p at which the taps are integral, Q=p^e with e≥1, and 8n<pQ,
$$
 \boxed{Q T_n(w)\equiv 16^n L_{Q\bmod 8}(\lfloor8n/Q\rfloor)\pmod p.} \tag{1}
$$
Every term on both sides is integral at p after grouping the left side as displayed. To prove it, discard terms with Q not dividing i after multiplication by Q, and write i=Qk for the others. In the local ring modulo p,
$$
 16^{b(k)-b(Qk)}
 =2^{-(Q-1)k/2}2^{(j(Qk)-j(k))/2}
 \equiv c(Q)^k2^{(j(Qk)-j(k))/2}.
$$
Euler's criterion gives the sign because (Q−1)/(p−1) has the parity of e and c(p)^e=c(Q). This works at 3 and 5 even with two pole events in one native step. p=2 requires a different analysis. The chronological normalized pulse at the event Qk, time b(Qk), is the ordinary rational representative
$$
 C_a(k)=c(a)^k2^{(k+8-j(ak))/2} L_a(k)
$$
of its class after removing the external time factor as in (1). At p=3,5 different terms in the same native step must all be included by (1); this last single-event description is used only when p>7 or the event is isolated. For a full return n=kQ with p>8k, (1) and 16^Q≡16 give Q T_{kQ}(w)≡T_k(S_aw). The monomial operators form a representation: the permutation composes, the exponents telescope, and intermediate indices preserve parity. In particular each is an involution. For e=1 this independently recovers the #499 group and its true all-tap return; its four-pole prime-power specializations have precedent in the October 30 arithmetic-barrier note. Equation (1) retains arbitrary partial endpoints and every rational tap.

Direct substitution gives S_1P=S_5P=P and S_3P=S_7P=−B/2 for B=(0,8,4,4,0,0,−1,0). Projecting with chi(a)=+1 at 1,5 and −1 at 3,7 yields A=(2P+B)/4=(2,2,1,0,−1/2,−1/2,−1/4,0). Write U_n=T_n(P), Y_n=T_n(A). Thus QY_{kQ}≡chi(p)^e Y_k throughout the full-return domain. A p-integral seed is invisible on the multiplied left side at this precision, while seed 1/Q changes that residue by 16^n. If the short return on the right is itself initialized at a seed z, it acquires 16^k z. Consequently a congruence between both aligned, seeded sides detects a p-unit z; the raw top residue measures the zero-seed short return regardless of any p-integral seed in the long orbit. Modulo p² the discarded terms may contribute. Neither the seed nor a second precision digit is recoverable from (1).

## Signs, denominator constants and a window that actually vanishes

Every block of P has strictly positive nonempty prefix sums of w_j/(8k+j) after its first nonzero tap, since its first positive coefficient 4 equals the sum of the magnitudes of the later negatives at strictly larger denominators. B has the same property starting at position 2 (the later negative weighs 1). For A the leading 2 already exceeds the total later negative weights 5/4. Earlier completed blocks have the same sign. Thus L_a(s) for P has sign + at classes 1,5 beyond their first event s=1 and − at 3,7 beyond their first event s=2. For A its sign is chi(a) for every s≥1. Multiplying by the chronological factor in (1) gives the universal event signs for both sources, including the chi_2(a)^s twist. This single block comparison avoids case induction. The reduced transfer 2/(1−t+t²/2) has a two-state realization by the coefficient recursion and a nonsingular minor det[[2,2],[2,1]]=−2. This rules out a one-state rational linear transfer, with no assertion about a finite carry automaton.

**All rational taps.** For fixed w∈Q^8,
$$
 \lim_{n\to\infty}\frac{\log\operatorname{den} T_n(w)}n
 =2\sum_{a=1,3,5,7}\sum_{s\ge1}
 \frac{\mathbf 1_{L_a(s)\ne 0}}{s(s+1)}. \tag{2}
$$
For a fixed s, the primes with floor(8n/p)=s lie in (8n/(s+1),8n/s]. Eventually p²>8n there. The finitely many exceptional numerator or denominator primes of the fixed nonzero rationals L_a(s) disappear as n increases. The fixed-modulus prime number theorem contributes one quarter of the length of this interval per class. The logarithmic contribution of prime powers of exponent two or greater costs O(sqrt(n)) by the elementary Chebyshev bounds (alternatively O(sqrt(n) log n) suffices). A fixed coefficient denominator contributes at most its logarithm beyond the lcm of 1,...,8n. The tail s>S costs O(n/S)+O(sqrt(n)) by Chebyshev. Truncate, let n tend to infinity and then S tend to infinity. Genuine P gives 2(1+1+1/2+1/2)=6 and A gives 8. For P first birth requires p≤8n for p≡1 (4) and 2p≤8n for p≡3 (4), with exact alignment automatically encoded by the last tap at 8n. At generic p>7 the first original tap has index j(p)=1,5 for the split classes and j(2p)=6 for the inert classes. For A every odd class has a nonzero coefficient at its first tap; for generic p>7 it is isolated at this step. For every fixed epsilon>0, eventually every eligible p>epsilon n has valuation exactly −1, by the same finite list of nonzero L_a(s); this does not assert unconditional finite survival.

The mutant w=(1,−2,0,0,0,0,0,0) gives L_1(2)=0. At every sufficiently large n, all p≡1 (8) in (8n/3,4n] occur in a source denominator but cancel in T_n. This removes n/3+o(n) logarithmic mass in this window alone. It refutes saturation for generic taps and makes the nonzero partial projections material.

**The exponent is rational for every nonzero source.** Suppose w has r nonzero taps. For each a and l in {0,...,7}, put H(k)=L_a(8k+l), k≥0. Exactly eight new terms give
$$
  H(k+1)-H(k)=16^{-k}\sum_{i=l+1}^{l+8}
     \frac{16^{-b(i)}(S_aw)_{j(i)}}{8k+i}.
$$
As a rational function of k the sum has r distinct simple poles, each with nonzero residue, hence its numerator is a nonzero polynomial of degree at most r−1 after clearing the r linear factors. If H(u)=H(v)=0 for integers 0≤u<v, its first differences sum to zero on u,...,v−1. At least one real zero of that numerator lies in [u,v−1], since the denominator and 16^{-k} are positive there. The intervals between successive sampled zeros are disjoint. Thus H has at most r zeros, including a possible k=0. Per class there are at most 8r zero windows with s≥1. In particular (2) equals the finite rational expression
$$
    c(w)=8-2\sum_{a}\sum_{s\ge1:\,L_a(s)=0}\frac1{s(s+1)}
      \ \ge\ \frac{8}{8r+1}>0.
$$
The lower bound removes the largest 8r terms for each class. The locations of these windows need not be bounded independently of w.

The zero-window mechanism even survives within the full chi_{−4} eigenspace. Use the independent vector E defined below, and for any preassigned s≥2 put w=L_1(s;E)A−L_1(s;A)E, making the tap argument explicit in L. Here L_1(s;E)>0 by the same positive-leading-block argument. The vector has nonzero odd taps at all four odd positions. For every a, L_a(s;w)=chi(a)L_1(s;w)=0 exactly. Thus every generic prime in (8n/(s+1),8n/s] cancels from its endpoint even though it appears in the cumulative conductor. Its loss in logarithmic mass is 8n/[s(s+1)]+o(n). This zero-seeded source has the same character relation as A, a nonzero transcendental period by the eigenspace proof below, and a strictly smaller denominator exponent. The nonvanishing argument for A uses more information than its character alone.

## Quantitative deficit for both genuine endpoints

For P or A write M_n=lcm of the reduced denominators of the n complete forcing moments and D_n=den T_n. Then
$$
  0\le\log(M_n/D_n)\ll n^{2/3}. \tag{3}
$$
All constants are absolute for these two fixed taps. Let x=8n. A common denominator for L_a(s) is C·16^{b(s)} lcm(1,...,s), where the fixed C clears all transformed tap denominators. The absolute values of the partial sums are bounded uniformly by geometric convergence. Therefore log max(1,|num L_a(s)|)≤C'(s+1) by Chebyshev's lcm estimate. For p>x/B with p²>x, a canceled genuine source prime has nonzero L_a(floor(x/p)), and divides its numerator by (1). Coprime distinct such primes with the same a,s divide the same numerator, so their total logarithmic charge is O(sum_{s≤B}(s+1))=O(B²). Remaining primes cost O(x/B) for first powers. All higher powers cost O(sqrt x) since their primes are ≤sqrt x, their maximum powers are at most x times a fixed tap denominator, and pi(sqrt x) log x=O(sqrt x). Choose B comparable to x^{1/3}. All bounds use elementary Chebyshev estimates, independently of any PNT error. A single canceled large prime additionally obeys log p≤C'(8n/p+1).

## Actual pair denominators: a row estimate

Put G_{m,n}=den(T_n−T_m), 0≤m<n. Then G_{m,n}|M_n. Uniformly in n,
$$
 \frac1n\sum_{m=0}^{n-1}\log\frac{D_n}{\gcd(D_n,G_{m,n})}\ll\sqrt n,\qquad
 \frac1n\sum_{m=0}^{n-1}\log\frac{M_n}{G_{m,n}}\ll n^{2/3}. \tag{4}
$$
Proof: allow the full prime-power mass for p≤sqrt(8n), at logarithmic cost O(sqrt n) per row average. For p>sqrt(8n) dividing D_n there is only a simple pole, and t=pT_n mod p is nonzero. The prime disappears in G_{m,n} exactly when pT_m=t mod p. As m increases, split [0,n) at steps having a p-divisible tap denominator. There are at most 1+floor(8n/p) runs. On each run the value multiplies by 16; if nonzero, returns to t recur with spacing ord_p(16). Hence its total count is at most n/ord_p(16)+1+8n/p. Write k=ord_p(16). Each product of distinct primes of order k divides 16^k−1, so
$$
 \sum_{2<p\le8n}\frac{\log p}{\operatorname{ord}_p(16)}
 \le\sum_{k\le\sqrt n}\frac{\log(16^k-1)}k+
 \frac{\vartheta(8n)}{\sqrt n}=O(\sqrt n).
$$
The remaining terms after summing the count times log(p)/n are O(1+log² n), by comparison with the integer harmonic sum. This proves the first inequality. For each pair log(M_n/G)≤log(M_n/D_n)+log(D_n/gcd(D_n,G)); use (3).

For the actual dyadic epoch A≤m<n<2A, summing (4) and discarding other nonnegative terms gives mean log(M_n/G_{m,n})=O(A^{2/3}) over the off-diagonal pairs. Thus for each u>0 the exceptional fraction with log(M_n/G)>u is O(A^{2/3}/u). For most pairs, in particular, the logarithm of the difference denominator is (8+o(1))n for Y, or (6+o(1))n for U (e.g. u=A^{5/6}). The arithmetic obstruction is narrowed to the **centered reduced numerator**. A nearly full denominator still allows a gap of 1/G, far below 1/log A.

This yields a direct, one-sided removal from the actual triangular energy. Take u=A^{2/3}(log A)^2. A single ordered pair contributes at most q_A/A², and by symmetry the exceptional off-diagonal pairs contribute O(q_A A^{2/3}/u)=O(1/log A) at q_A=O(log A). The diagonal contributes q_A/A. Thus the target J=o(K_A) is equivalent to the same bound on pairs with n≠m and G_{m,n}≥M_max(m,n) exp(−u), indexing the conductor by the later time. This is a rigorous saving on the discarded part of the original energy. On the remaining, density-one population, the numerator estimate is still open.

## Uniform all-lag bound on the selected primal

For odd primes p≤x, d≥1 and k=ord_p(16) dividing d, prime mass with that k is at most min(k log16, (x/k)log x) because p≡1 modulo k. Therefore the union of all p≤x dividing 16^d−1 has log mass ≤tau(d) sqrt(x log16 log x). For d=O(x), the elementary divisor bound tau(d)=O_delta(d^delta), all delta>0, makes this o(x) uniformly. Large d will only need fresh primes.

For n=m+d with 0<d≤m, all newborn angular primes 8m<p≤8n enter G_{m,n}, except total log loss O(n^{2/3}) by (3), up to first-birth constants. Add disjoint *shared* windows
$$
         8n/(j+1)<p\le8m/j,\qquad j=1,2,3,
$$
when nonempty. These three windows are disjoint. The two reduced residues are 16^m and 16^n times the same nonzero L_a(j), modulo p. All these factors have bounded numerators and denominators as j is fixed. Their shared primes survive except divisors of 16^d−1, of total logarithmic mass o(m). Thus, writing t=d/m, uniform classical PNT on all endpoints gives
$$
 \log G_{m,n}/m\ge 8t+8\sum_{j=1}^3(1/j-(1+t)/(j+1))_+ -o(1).
$$
This convex piecewise linear function is minimized at t=1/3: its slope below 1/3 is 8(1−1/2−1/3−1/4)<0, immediately above it is 8(1−1/2−1/3)>0. Its value there is 52/9. For n≥2m the newborn range alone gives at least (8−o(1))(n−m), uniformly by the PNT since n−m≥n/2. Consequently
$$
 \liminf_{m\to\infty}\inf_{n>m}\frac{\log G_{m,n}}m \ge 52/9
$$
for the actual Y. The archived November 2 macrolag theorem concerns U. Its two disjoint windows for p≡1 mod4 likewise add; for n≤4m their combined length weighted by PNT-AP is 3m+3d before subtracting shared divisors of 16^d−1. This already gives a constant at least 3 for U; the preceding proof of (4) is stronger for the pair population. No inequality here lower-bounds an actual circle gap at the scale 1/log m.

## The full character eigenspace excludes rational-period source mutants

Besides A, take E=(0,2,0,0,0,−1/2,0,0). Both satisfy S_aw=chi(a)w. There are at most two degrees of freedom: positions 4 and 8 are fixed at a=3 and force zero; orbit {1,3,5,7} and orbit {2,6} each contribute at most one dimension. Hence A,E span the whole rational eigenspace. For w=xA+yE let F(w) be its completed interval integral with denominator 1−t^8/16. The two rational kernels are 4/((t−1)^2+1) and 2t/(1+t^4/4). Direct antiderivatives give F(w)=x pi+2y arctan(1/2). For a common denominator h, the exponential exp(i h F(w)) is (-1)^{hx} ((2+i)/(2−i))^{hy}. Its valuation at the Gaussian prime 2+i rules out F(w)=0 unless hy=0, and then hx=0. The classical Hermite–Lindemann theorem gives transcendence of F(w) for every nonzero rational character source. Thus an exact zero/rational completed period cannot occur in this two-dimensional family. This conclusion does not exclude a nonnormal transcendental period.

## Residual, countermodels and falsifier

The top digit (1) ignores any rational seed integral at p; the seed 1/5 is invisible at generic p yet rotates real phases. The two-source-window mutant above disproves an arbitrary-tap saturation argument. The archived coherent shadow in research/2026-11-02/macrolag_prime_witness exhibits exponential gap denominators with concentrated phases. A reduced numerator equal to 1 is coprime to every possible gap denominator. The row estimate uses ordered times of the actual orbit, but neither the order bound nor the nonzero universal rational pulse estimates the distance of that numerator to the nearest multiple of its denominator. The verdict-changing probe is a signed or small-centered-numerator estimate over the large-denominator pair population, including pairs in the same genuine epoch, compared to cofactor or wrong-seed rivals. No improvement to the order of the target triangular energy is established by (1)–(4).

## Literature and finite authority

Fixed-modulus PNT, Chebyshev estimates, the divisor bound, Euler's criterion and Hermite–Lindemann are classical. Shiu studies the LCM deficit for harmonic numbers, Wu and Chen study denominator divisibility and density for the same sums, and Wu and Yan treat unweighted progressions. Van Doorn studies nonmonotonicity for families of generalized harmonic sums. These are relevant precedents for extracting divisibility from harmonic prefixes. Their statements concern different weights or questions; this comparison establishes no world-priority claim for (1)–(4).

* P. Shiu, [The denominators of harmonic numbers](https://arxiv.org/abs/1607.02863).
* B.-L. Wu and Y.-G. Chen, [On the denominators of harmonic numbers](https://doi.org/10.1016/j.crma.2018.01.005).
* B.-L. Wu and X.-H. Yan, [On the denominators of generalized harmonic numbers. II](https://doi.org/10.5486/PMD.2024.9691).
* W. van Doorn, [On the non-monotonicity of the denominator of generalized harmonic sums](https://arxiv.org/abs/2411.03073).

The companion standard-library probe has no SUCC arithmetic imports. Run the script prime_layers_probe.py in this directory and compare stdout with PRIME_LAYERS_RECEIPT.json. Exact finite scope: 2,607 layer comparisons, 58 mutant prime-window comparisons, and all earlier m for both authentic endpoints at n=83,211,389,631. The angular p=71 at n=211 and original p=281 at n=631 really cancel and obey the numerator-charge rule. These calculations share the declared inputs with the theoretical analysis and carry no independent scholarly or hosted CI authority.
