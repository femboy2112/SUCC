# Operation parity pressure — exact CRT winding × signed prime/local parity

**2026-11-09, research-only child of SUCC #571 at 1597ddab8c4dab909b84e698eb47008b5e3ae46f.** Original signed BBP four poles, literal U0=0, provenance, archive, formal contracts, workflows and main unchanged. **Pi base-16 normality: OPEN. Original zero-selected real parity decay: OPEN. RH: OPEN.** Proofs are paper derivations backed by exact rational regressions, not external refereeing or new Lean certificates.

Prior inputs: SUCC #544 signed chronology, #554 balanced prime Fourier BEC-03..06, #562 complete global CRT winding, #563 real prime slip, #564 moving digit boundaries, #565 conditional Haar, #571 two-road wavelets. Classical references: Bailey–Crandall, Experimental Mathematics 10 (2001); Lagarias, Experimental Mathematics 10 (2001); Cochrane–Pinner, Quarterly Journal of Mathematics 62 (2011), https://doi.org/10.1093/qmath/hap041. Scholarly novelty/priority is not claimed.

## PPP-00: h=8 TYPE FIREWALL

The **continuous** Weyl character e(8x)=exp(2πi8x) is not the **discrete hexadecimal-digit parity** (-1)^floor(16x). The latter is the h=8 Walsh/Rademacher character on the 16 CHILD DIGITS. Its real-circle Fourier expansion has all frequencies m congruent 8 modulo 16 with coefficient 16/(πim), m nonzero. This follows by integrating the step function over the sixteen digit intervals; at jump boundaries use the declared half-open digit convention. Hence a bound on only continuous Weyl frequency 8 does NOT establish digit parity balance.

For a finite digit law p(a), its parity mean P=sum_a (-1)^a p(a) is the h=8 child Fourier coefficient. Under the child digit successor S_16, the h=8 character has eigenvalue -1. The signed successor gradient I-S_16 doubles this mode: the exact h=8 contribution to successor-wavelet energy J_0 is 4P². It is a single deliberately selected signed projection, not the full Haar word L² energy E_k forced upward by finite-sample occupancy.

## PPP-01: original four-pole source parity clock (PROVED)

The exact source is

~~~text
r(n)=(120n²−89n+16)/
 ((2n−1)(4n−1)(8n−7)(8n−3))
U0=0; U_n=16U_(n−1)+r(n).
~~~

All denominator factors are odd and the numerator mod2 equals n mod2, so r(n)=n mod2 in Z_2. The multiplier 16 kills every previous residue modulo2. Consequently U_n=n mod2 for all n>=1. This is an identity for the 2-adic value of the **unwrapped rational state**, NOT its real integer part or hexadecimal digit. Any rational seed with odd denominator has the same U_n mod16 for n>=1 because the added 16^n s is divisible by16 in Z_2. Thus this clock is not zero-seed selective.

## PPP-02: all odd primes + global winding + real tail (PROVED)

Choose the canonical positive odd common source denominator Q_n=lcm(den(r(1)),...,den(r(n))), and integer A_n=Q_n U_n. Q need NOT be the reduced denominator. By PPP-01, A_n=n mod2. For each maximal prime-power m=p^v parallel Q, define k_(m,n) as the canonical residue of A_n times (Q_n/m)^(-1) modulo m in 0,...,m−1. Let theta_(m,n)=k_(m,n)/m, and let ell_n=floor(sum_m theta_(m,n)). Then CRT reconstructs the single real positive fractional numerator:

~~~text
b_n=A_n mod Q_n
   = Q_n * (sum_m theta_(m,n) − ell_n).
~~~

Every Q_n/m is odd, hence b_n=sum_m k_(m,n)−ell_n modulo2. From floor U_n=(A_n−b_n)/Q_n we obtain floor U_n=n+sum_m k_(m,n)+ell_n modulo2.

Define the authentic positive BBP future tail T_n=sum_(j>=1)16^(-j) r(n+j), with rigorous bound T_n<=r(n+1)/15, and epsilon_n=floor({U_n}+T_n) in {0,1}. The classical BBP period identity U_n+T_n=16^(n−1)π gives the exact SIGNED PARITY IDENTITY

~~~text
(-1)^floor(16^(n−1)*π)
  = (-1)^(n + sum_(m||Q_n)k_(m,n) + ell_n + epsilon_n). (P2)
~~~

For n>=2 the left side is the parity of the (n−1)-th FRACTIONAL hex digit. Switching the source epoch [A,2A) to the fractional-digit epoch costs at most 2/A on a normalized signed sum. This indexing and continuous-vs-discrete frequency distinction are mandatory.

## PPP-03: exact one-prime signed real/complement covariance

Let p_A be #554's genuine balanced first-shell prime p≈12A/5, with v_p(Q_n)=1 throughout [A,2A). The coordinate k_(p,n) equals the original source p-primary phase pU_n modp, which equals #554's diagonal sum of its three true positive source channels. Define signs

~~~text
a_n=(-1)^k_(p_A,n)
b_n=(-1)^(n+sum_(m!=p_A)k_(m,n)+ell_n+epsilon_n)
s_n=(-1)^floor(16^(n−1)*π)=a_n b_n.
~~~

For authentic source chronology, mean(s)=mean(a)*mean(b)+Cov(a,b) exactly, with no probabilistic independence assumption or dropped old cofactor. If local mean(a)=o(1), then real parity balance is equivalent to zero-seed signed Cov(a,b)->0. This gives parity balance ONLY, not full first-digit Haar or base-16 normality.

## PPP-04: genuine prime-side parity saving from inherited BEC (PROVED CONDITIONAL)

For any odd p define eta_p(k)=(-1)^k on canonical representatives k=0,...,p−1. Its finite ADDITIVE Fourier transform is

~~~text
eta_hat_p(t)=(1/p)sum_k (-1)^k exp(-2πi t k/p)
            =2/[p*(1+exp(-2πi t/p))].
eta_hat_p(0)=1/p.
sum_t |eta_hat_p(t)| <= 2+log p.                       (P4)
~~~

Proof: the geometric series numerator is 2 because p is odd. Each magnitude is 1/[p|cos(πt/p)|]. Sin concavity bounds it by 1/|2t−p|; summing odd harmonic denominators yields 2+log p.

Now take precisely #554 BEC-03/04/05/06 as declared **conditional source-specific input**, including quantitative fixed-modulus PNT/AP, imported Cochrane–Pinner subgroup character bounds and the genuine four-stage prime clock. Its uniform (also p-dependent-frequency) additive character inequality states for every nonzero t modulo p_A:

~~~text
|mean_[A,2A) exp(2πit k_(p_A,n)/p_A)| <= err_A
err_A=delta_(p_A)+4sqrt(p_A)(2+log m_A)/A
m_A=ord_(p_A)(16), p_A~12A/5, err_A log(p_A)->0.
~~~

Fourier inversion then gives, for the *real original-source local p coordinate*,

~~~text
|mean_[A,2A) (-1)^k_(p_A,n) −1/p_A|
 <=(2+log p_A)*err_A = o(1).                         (P5)
~~~

This is an **arithmetically nontrivial LOCAL PRIME PARITY estimate** under the inherited deep input, not an unconditional new proof of #554 or a real-digit normality theorem. Combining P5 and PPP-03 yields:

~~~text
|mean_[A,2A) s_n|
 <=1/p_A+(2+log p_A)*err_A+|Cov_A(a,b)|.             (P6)
~~~

The last original zero-seed real/prime complementary covariance remains OPEN.

## PPP-05: four-stage multiplicative support and arithmetic pressure

The same authentic BEC first p-shell has exactly four chronological source-birth stages. Within each, k_(p,n)=16^(n−birth)*c_s modulo p for one stage coefficient c_s. Thus the selected local p observations lie in at most four cosets of the multiplicative subgroup H=<16> of order m=ord_p16. Consequently, the number of occupied p residues M <=min(A,4m). For the positive empirical p collision energy E_p=p sum_u (count_u/A)^2−1, Cauchy-Schwarz gives

~~~text
E_p>=p/M−1>=p/min(A,4m)−1.                       (P7)
~~~

This concentration lower bound coexists with P5's **small signed parity**; high positive pressure need not imply large signed Fourier response. If m=o(p) the lower bound can grow, but no claim is made that the balanced selector always has m=o(p). The finite p=1217,m=38 example confirms this coexistence.

## PPP-06: exact integer pressure law, no randomness premise

For N actual k-word starts in B=16^k potential cells, let c_w be integer occupancies. Define E_k=B Σc_w²/N²−1 and write N=qB+r with 0<=r<B. Exact integer algebra yields

~~~text
E_k=r(B−r)/N²
  +(B/N²) Σ_w (c_w−q)(c_w−q−1).                   (P8)
~~~

The second summand is nonnegative because every integer t obeys t(t−1)>=0. The first is the SHARP finite integer occupancy floor (attained by balanced counts q or q+1). Define the Rényi-2 effective occupancy V2=N²/Σc_w²; then 1+E_k=B/V2. For B>N the identity simplifies to

~~~text
E_k=B/N−1 +(2B/N²)Σ_w binomial(c_w,2).           (P9)
~~~

First term = unavoidable sample-resolution floor; second = excess repeated-cell collisions. Even a normal sequence can have rapidly growing E_k at B~N² because the first term is N−1; this is not a theorem of arithmetic confinement. Increasing BBP denominators creates a finer available rational grid. Strong source-specific **prime** support restrictions do exist in PPP-05, but must be distinguished from this universal empirical floor.

## PPP-07: local Haar does not descend to global parity (PROVED COUNTERMODEL)

Let Q be any odd composite and use the artificial probability law uniform on EVEN canonical integer representatives b in [0,Q). The global representative parity is identically +1. For each odd m|Q put L=Q/m (odd). The number of even b congruent to r modulo m equals (L+(-1)^r)/2, hence

~~~text
Pr(b=r modm)=(L+(-1)^r)/(Q+1)
TV(local_m, Haar_m)=(m²−1)/(2m(Q+1)).             (P10)
~~~

All fixed local marginals can be arbitrarily close to Haar as Q/m increases, while real canonical parity stays perfectly biased. This explicitly refutes the shortcut from prime-by-prime Haar to Archimedean parity without the global section/winding. Even the topological reason is visible: the integers b and b+m have identical residue modulo odd m but opposite parity.

## PPP-08: exact original-source odd-denominator coherent counterseed

For any A>=2, odd selected p, N=2A+16, let alpha_N=Σ_(j<=N)16^(-j)r(j) (rational original source), D=p16^(2A+48)+1 (odd, p-integral), and rational s_A=-floor(D alpha_N)/D. No pi digit oracle. With alpha=π/16 and the positive original-source tail,

~~~text
0<alpha+s_A<1/D+16^(-N)r(N+1)/15.
0<16^n(alpha+s_A)
  <16^(-41)/p+16^(-9)r(N+1)/15<1/16
       for A<=n<2A+8.                            (P11)
~~~

All real completed digits on that epoch equal ZERO. But the original four-pole forcing is intact; 16^n s_A is 2-adically divisible by16 and p-integral, so **the entire local p-primary history and the parity clock are identical** to zero seed. The wrong seed is epoch-dependent, not an allegation about π. Its real signed covariance is 1−mean(a)^2, which reaches 16383/16384 at the p=1217 holdout, versus the actual original-zero observed 641/16384. This is an exact refutation of seed-blind local-to-real cancellation.

## PPP-09: preregistered original-source A=512 holdout (OBSERVED FINITE)

Frozen protocol commit 9af9f3d3106d4a05785a7cf51dc94a47781a9ad6 preceded reading n>=513. The deterministic balanced selector picked p=1217, ord_p16=38. At source n=512,...,1023, exactly 512 states:

~~~text
mean local p parity sign      -1/128
mean real completed parity     5/128
mean complementary sign        1/128
signed covariance             641/16384
source-tail boundary crossings    0
visited p-local residues          76 / 1217
local positive collision E_p  2051009/131072 (~15.648)
coherent wrong-seed covariance 16383/16384
~~~

The certified 516 hexadecimal digits from fractional source digit index n=512 have SHA256 (uppercase ASCII, no newline): de490f103f307780a0cdc92f93a3e11873d26c71cd328d6de9b7a62f932fa58d.

Independent **implementation routes** (not independent mathematical source) agree: original unwrapped rational recurrence plus outward future-tail at each n and a single global outward 1040-term BBP rational interval. Both certify all 516 digits exactly, no π digit oracle.

The N=512 observed word energies for k=1,2,3,4 equal 231/8192, 235/512, 63/8, 257/2. Their sharp occupancy floors are 0,0,7,127; excess terms are 231/8192,235/512,7/8,3/2. The pristine A=512 source receipt and negative controls are frozen in HOLDOUT_512.json. These are finite diagnostics only, not an all-epoch decay estimate.

## Verdict and next decisive theorem

PPP-01..03,05..08 are elementary within declared carrier domains; PPP-04 is a valid **conditional transfer theorem** only if the inherited #554/BEC all-frequency bound is sound; PPP-09 is OBSERVED FINITE. Seed-blind local-to-real parity, h8 digit/Weyl confusion and pressure→normality shortcuts are REFUTED with explicit receipts.

**Still OPEN:** prove, for every sufficiently large integer A with the genuine balanced p_A and literal U0=0,

~~~text
Cov_A[ (-1)^k_(p_A,n),
       (-1)^(n+Σ_(m!=p_A)k_(m,n)+ell_n+epsilon_n) ] -> 0.
~~~

This would prove a *single parity balance theorem for pi's hexadecimal digits*, not full base-16 normality. The proof must use source-zero selectivity and control the real prime-complement/winding correlations, and must fail the odd-denominator p-integral coherent shadow.

