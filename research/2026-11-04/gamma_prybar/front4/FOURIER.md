# A finite large-sieve inequality across the quadratic crossover

**Authority:** paper proof with elementary summation by parts. No Lean receipt, independent referee or priority claim. Source is the literal zero-seeded four-pole recurrence in the campaign contract. All estimates also hold after arbitrary real seed changes with the same forcing. Constants below are absolute. Let $e(x)=\exp(2\pi ix)$ and $c_A(t)=A^{-1}\sum_{A\le n<2A} e(tU_n)$ for integer $A$. 

**F1.** For all sufficiently large integer $A$, all integers $1\le |h|\le A^2$, all real $L\ge1$, let
\[
 D=\{j\ge1: L A^2\le |h|16^j\le A^3\}.
\]
Then
\[
 |c_A(h)|^2+\sum_{j\in D}|c_A(16^j h)|^2
 \le 1+O\!\left(L^{-1}+ (\log A)^{3/2}/A\right).
\]
In particular for fixed nonzero $h$ and $L=\log A$, $|D|\sim\log_{16} A$ and the mean square across these sparse moving frequencies is $O(1/\log A)$. The minimum modulus is $O((\log A)^{-1/2})$. This gives a signed frequency estimate for the actual selected trajectory, with a restricted scope: the saving is averaged over moving frequencies, and its proof is seed-blind. This is beyond #491's subquadratic transport range. It gives no bound tending to zero for fixed $h$.

**Proof.** By conjugation take $h>0$. For $j\in D\cup\{0\}$ put
\[
 S_j(m)=\sum_{\ell=0}^{j-1}16^\ell r(m-\ell),\quad S_0=0.
\]
Exact affine iteration gives $16^j U_{m-j}=U_m-S_j(m)$, including all original pole terms and the unwrapped integer lift. With normalized counting measure on $I=[A,2A)\cap\mathbb Z$, set $v(m)=e(h U_m)$, $b_j(m)=e(h S_j(m))$, $a_j=\langle v,b_j\rangle=A^{-1}\sum_I v\overline{b_j}$. Shifting endpoints gives $|a_j-c_A(16^jh)|\le 2j/A$. Only this endpoint error uses a restriction of the time interval.

Here the actual arithmetic forcing supplies the spacing between *test vectors*. Write
\[
 r(s)=\int_0^1 u^{8(s-1)}(1-u)B(u)\,du,\quad
 B(u)=(u^2+2)(u^2+2u+2),\quad 4\le B(u)\le15.
\]
Let $d_s=r(s)-r(s+1)$. It is strictly positive and decreasing, by multiplying the moment integrand by $1-u^8$. Since $1-u\le1-u^8\le8(1-u)$ and $\int_0^1u^a(1-u)^2du=2/[(a+1)(a+2)(a+3)]$,
\[
 \frac8{(8s-7)(8s-6)(8s-5)}\le d_s\le
 \frac{240}{(8s-7)(8s-6)(8s-5)}.
\]
For $k>j$ in the index set, the absolute consecutive increment of $f(m)=h(S_k(m)-S_j(m))$ equals
\[
 \delta_m=h\sum_{\ell=j}^{k-1}16^\ell d_{m-\ell}.
\]
Its sign in $f(m+1)-f(m)$ is negative. Its magnitude decreases with $m$. All $k\le3\log_{16} A$, and for large $A$, all indices $s=m-\ell$ obey $6A\le8s-7$ and $8s-5\le16A$ on $A\le m<2A$. The last term gives the lower bound, while the entire geometric sum gives the upper bound
\[
 \lambda=\frac{h16^k}{8192 A^3}\le\delta_m\le\frac{240 h16^k}{216\cdot15 A^3}<\tfrac12.
\]
For completeness, the monotone-increment first-derivative test here follows from
$e(f(m))=[e(f(m))-e(f(m+1))]/[1-e(-\delta_m)]$.
For $t\in[\lambda,1/2]$ the reciprocal denominator has constant real part $1/2$ and monotone imaginary part of magnitude $|\cot(\pi t)|/2$.
Summation by parts therefore gives the endpoint terms plus variation $O(1/\lambda)$, also on any subinterval. In normalized form
\[
 |\langle b_j,b_k\rangle|\ll A^2/(h16^k).
\]
This pays for spacing of the explicitly constructed test functions. No real spacing of the $U_n$ was assumed.

List the high depths in ascending order $k_1,\ldots,k_d$. Their frequencies satisfy $h16^{k_i}\ge LA^2 16^{i-1}$. In row $i$ at most $i$ lower-index entries (including index zero) contribute $O(i16^{1-i}/L)$ and the higher entries contribute a geometric tail $O(16^{1-i}/L)$. Row zero has off-diagonal sum $O(1/L)$ as well. The Gram matrix therefore has operator norm at most $1+C/L$ by the row sum bound. Dual Bessel gives $\sum_j |a_j|^2\le1+C/L$ since $\|v\|_2=1$. The endpoint error has Euclidean norm $O((\log A)^{3/2}/A)$. The triangle inequality in $\ell^2$ and squaring prove the claim.

**F2. The crossover is real.** With the same forcing and seed $s_*=-\pi/16$, the unwrapped orbit is $V_n=-T_n$, where the exact Green tail is
\[
 T_n=\sum_{k\ge1}16^{-k}r(n+k)
 =\int_0^1 u^{8n}(1-u)B(u)/(16-u^8)\,du.
\]
Consequently $c_A^{V}(h)\to1$ at every fixed $h$. In contrast, uniformly for integer $1\le H\le A^3$,
\[
 |c_A^{V}(H)|\ll \min(1,A^2/H).
\]
Indeed $T_m-T_{m+1}$ is positive decreasing by the same moment argument, bounded below by $\tfrac12/[(8m+1)(8m+2)(8m+3)]$ and above by $16/[(8m+1)(8m+2)(8m+3)]$. Thus $H(T_m-T_{m+1})\asymp H/A^3$ and is $<1/2$, so the same telescoping proof applies. This control has cancellation on *every* superquadratic frequency through $A^3$ and has $J_{A,q_A}\sim q_A$. In particular F1's leading constant 1 (including the low coefficient) is sharp uniformly over seeds when $L\to\infty$.

The fixed counterseed also gives the exact transition profile: if integers $H_A/A^2\to t\ge0$ then $c_A^V(H_A)\to\int_1^2 e(-t/(64u^2))\,du$. Indeed $B(u)/(16-u^8)$ is continuously differentiable on $[0,1]$ and has value 1 at $u=1$, so the integral for $T_n$ equals $1/[(8n+1)(8n+2)]+O(n^{-3})$. The convergence then follows by a Riemann sum. For $t>0$ the integrand is continuous and nonconstant, so the modulus of its unit-length average is strictly below 1.

The epoch-dependent *source-native* control of #492 AS-02 enjoys the same superquadratic savings up to an additive $O(\log A/A)$. Specifically put $M=2A$, $B_A=\mathrm{lcm}_{j\le A}\mathrm{den}\,r(j)$ and $s_A=\mathrm{nint}(-B_A\alpha_M)/B_A$ with $\alpha_M=16^{-M}U_M$. #492 AS-01 gives $B_A>4A^2 16^{2A}$ eventually and $T_M<1/(64M^2)$. Hence $|16^n(s_A+\pi/16)|\ll16^{n-M}/A^2$ on the entire epoch. For $H\le A^3$ throw away the last $\lceil 2\log_{16} A\rceil$ samples, at cost $O(\log A/A)$; the phase error on the remainder is $O(A^{-1})$. The short-arc bound AS-4 of Theorem AS-02 in SOURCE_NATIVE_SEED.md gives $J\sim q_A$. Same forcing and growing prime conductors survive this test. The first invalid inference is transferring unweighted high-band decay backward across the quadratic crossover.

**F3. Fixed-lag scope.** Every fixed integer stencil $P(z)=\sum_{j=0}^d p_j z^j$ obeys
\[
 \sum_{j=0}^d p_j U_{n+j}=16^n (\pi/16)P(16)-\sum_{j=0}^d p_j T_{n+j}.
\]
The same identity holds for any seed $s$ with $\pi/16$ replaced by $s+\pi/16$. For fixed $P,h$ the character error on a dyadic epoch relative to the completed orbit of $(\pi/16)P(16)$ is $O(|h|\sum_j|p_j|/A^2)$. If $P(16)=0$ the epoch character tends to 1, for every seed. If $P(16)\ne0$, demonstrating all fixed character decays of that orbit is itself equivalent to normality of $\pi$ (normality is invariant under nonzero integer multiplication). For a short proof of the reverse implication, any subsequential weak limit of the original completed full-prefix orbit measures is $\times16$-invariant and pushes forward under $x\mapsto P(16)x$ to circle Lebesgue measure. Such a limit is absolutely continuous: the image of a Lebesgue null Borel set under finite integer multiplication has outer measure zero, and its preimage contains that set. Riemann–Lebesgue plus $\widehat\mu(h)=\widehat\mu(16^j h)$ then gives Haar. This discusses the all-h, full-prefix converse. For the single fixed pair lag $P(z)=z^d-1$, van der Corput accordingly exposes shifted frequencies, with no automatic cancellation.

**Prior art and correction.** The exact affine transport below $o(A^2)$ appears in #491 RT-1–3 and #496 AE-5. Main's 2026-10-25 SUCC_INTERNAL_MATRIX_WALK.md IMW-04–05 already identifies $n^2$ and $n^3$ as critical for the local forcing and its increment. F1 controls a sum over a logarithmic number of signed means through explicit finite chronological test-function spacing. #496's Gamma(2) Abel kernel and nonzero Mellin multiplier do not by themselves establish boundary vanishing. #491 COUNTERMODELS.md AT1 says a constant limit of $qP/A^2$ fails to be $o(K_A)$. Since $K_A\to\infty$, that sentence is incorrect. Surrogate finite epochs establish neither such a limit nor its failure.

**External audit.** Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions*, Theorem 3.1 gives the rationality/finite-attractor result unconditionally; Theorem 1.1's normality claim assumes Hypothesis A. [Authors' text](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf). Lagarias, *On the Normality of Arithmetical Constants*, Theorem 3.1, Lemma 3.2, Theorem 3.3 and ensuing remark (1), show that vanishing perturbations and orbit shadowing admit arbitrary real completions including irrational nonnormal ones. That argument does not refute the restricted rational-function dichotomy (Theorem 4.1 is conditional). [Primary text](https://arxiv.org/pdf/math/0101055). Bailey–Crandall, *Random Generators and Normal Numbers*, Theorems 4.6, 4.8 and Corollary 4.9 pay for exponential sums along whole or long incomplete modular cycles in specific coprime prime-power/composite-power denominator families and spacing hypotheses, proving generalized Stoneham normality. Source-generated, frequently changing BBP cofactors lack that verified orbit-length input. [Authors' published text](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf).

**F4. Sharp cost of retrieving the original signed mean from a high frequency.** For any integer frequency $t$ let $M_A(t)$ be $A^{-1}$ times the maximum of $|\sum_{n\in I}e(tU_n)|$ over contiguous subintervals $I$ of the epoch. For $j\ge0$ and $H=|h|16^j\le A^3$,
\[
 M_A(h)\le j/A+(1+C H/A^2)M_A(H)
\]
with an absolute $C$ for large $A$. On an arbitrary interval first discard the at most $j$ samples $m<A+j$. On the rest use $e(hU_m)=e(h16^jU_{m-j})e(hS_j(m))$. All required partial sums of the first factor lie in the original epoch. The second factor has modulus one and total variation at most $2\pi |h|S_j(A+j)$ by monotonicity of $S_j$. For $s\ge A$ the moment bound gives $r(s)\le15/[(8s-7)(8s-6)]$, so $S_j(A+j)\ll16^j/A^2$. Partial summation proves the estimate.

For the coherent seed, F2's telescoping applies on every subinterval. Applying the reverse estimate just proved to $h=1$ and using $M_A^V(1)\to1$ yields the sharp two-sided bound
\[
 M_A^V(16^j)\asymp \min(1,A^2/16^j)\qquad (0\le j,\quad 16^j\le A^3).
\]
Hence a bound that merely matches this coherent rate leaves a full obstruction. A concrete discriminating target for the zero seed is the following. For each fixed integer $h\ne0$ and dyadic $A$, choose $j=\lfloor\log_{16}(A^2\log A/|h|)\rfloor$ for large $A$. Prove $M_A(16^j h)=o(1/\log A)$. This improves the coherent rate at its measured scale; it is an **open sufficient hypothesis**. The reverse estimate gives $M_A(h)=o(1)$, and dyadic subdivision, including the last partial epoch, gives the full-prefix Weyl gate. Dual Bessel in F1 controls an unweighted full-epoch mean square and supplies neither this rate nor the maximal estimate. For fixed $h$ the same sharp coherent lower bound follows using $M_A^V(h)\to1$. The #492 source-native control differs on all subinterval means by $O(\log A/A)$ for $H\le A^3$ and likewise fails the target at $H\asymp A^2\log A$.

**F1 maximal strengthening.** The same bound in F1 holds with every $|c_A|$ replaced by $M_A$, even though each frequency can choose its own maximizing subinterval. For each depth choose such an interval $I_j$. After shifting $m=n+j$, clip $I_j+j$ to the epoch, losing at most $j/A$ per coefficient. Multiply $b_j$ by the indicator of the clipped interval. A Gram diagonal is then at most one, and every off-diagonal inner product is precisely the previous chirp sum restricted to the intersection of two intervals. That intersection is empty or an interval, so the same first-derivative bound and geometric row estimate apply. Bessel and the same endpoint error finish. In particular the *maximal* mean square through the high ladder is $O(1/\log A)$ at $L=\log A$. The F4 gap is localization and rate: the retrieval cost grows like $16^j|h|/A^2$, whereas an unweighted sum over logarithmically many depths only gives some small coefficient at an uncontrolled depth. The sharp coherent control obeys both estimates.
