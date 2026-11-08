# Independent selector review: stronger order and quantitative epoch coverage

Reviewer: chronology front. Parent research baseline1990b051. This review is
independent algebra/proof checking after the root proposed the stronger selector;
it is not blind discovery and not independent scholarly refereeing. The reviewed
arithmetic argument is reproduced in full here. The new Cochrane--Pinner input
is source-audited by root; this reviewer independently checks its substitution,
not its proof. No floating-point prime decision is required.

## Exact implementation-compatible selector

For p odd prime put b(p)=floor(log_2 p)+1, its positive integer bit length.
Fix a positive integer C. Call p admissible when

    p=1 mod8,  m_p=ord_p(16),  m_p^3>p,
    m_p^2 b(p)^(2C)>p.

The cubic condition preserves the prior PE good-prime family even at finite
sizes. For all sufficiently large p it is redundant: p^(1/6)>b(p)^C implies
sqrt(p)/b(p)^C > p^(1/3). The second condition is exactly the strict real
inequality m_p>sqrt(p)/b(p)^C, expressed with integer arithmetic.

Define p_A^C as the largest such prime <=4A whenever one exists. For any
fixed B with 0<B<2C, it exists for every sufficiently large A and

    0<=4A-p_A^C <= 4A/(log(4A))^B.                         (S1)

No statement is made that the selector is defined at every small A. Exact
source implementations must reject undefined cases rather than fabricate a
prime. The definition is source-independent and does not inspect pi digits.

## Elementary exceptional-order count, with the missing log factor retained

For an integer M>=1 let V_M=product_(j=1)^M(16^j-1). Then

    log V_M < (log16) M(M+1)/2 = 2(log2) M(M+1).            (S2)

Every odd prime with ord_p(16)<=M divides V_M. If K such primes are at least
X/2, their product divides V_M, so

    K log(X/2) <= log V_M < 2(log2) M(M+1).               (S3)

This is sharper for near-X primes than counting every prime divisor by log2.

Let H=X/(logX)^B. Eventually H<X/2, so p in [X-H,X] has b(p)>=log_2(X/2).
After the eventual redundancy of the cubic condition, every inadmissible prime
in this interval has

    ord_p(16) <= sqrt(X)/(log_2(X/2))^C.

Take M as the floor of the right-hand side. Equations S2--S3 give

    #bad primes in [X-H,X] = O_C(X/(logX)^(2C+1)).         (S4)

The floor is harmless; M tends to infinity. This count includes all residue
classes, hence also bounds the excluded primes in1 mod8. It uses no Artin
conjecture, GRH, or typical-order result.

## Analytic prime input and the actual coverage rate

The classical fixed-modulus quantitative PNT states

    pi(x;8,1)=Li(x)/4+O(x exp(-c sqrt(logx)))               (S5)

for a fixed c>0, with constants for modulus8. An authored primary exposition
checked live is Ze'ev Rudnick's 2015 course notes, *Primes in arithmetic
progressions: fixed modulus*, Section2, printed page2:
https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf.
The displayed statement applies to every fixed coprime residue class and
fixed modulus. This is a declared classical import stronger than the previous
Kedlaya qualitative PNT reference, not a consequence of finite prime tests.

Subtract S5 at X and X-H. Since logt~logX uniformly on [X-H,X],

    pi(X;8,1)-pi(X-H;8,1)
       = (1+o(1)) X/[4(logX)^(B+1)].                     (S6)

Indeed Li(X)-Li(X-H)=integral_(X-H)^X dt/logt~H/logX, and the two PNT error
terms are o(H/logX): exp(-c sqrt(logX)) beats every fixed inverse logarithm.
Because B<2C, S4 is o(S6). Thus at least one admissible prime lies in
[X-H,X] for every sufficiently large X. Taking X=4A proves S1 for the largest
selector. The argument is uniform over all large A, not merely a subsequence.

Let L_A=(p_A^C-1)/4 and retain PE's clean interval I=[L_A+1,2L_A+1), actual
J=[A,2A), and exact normalized weight distance epsilon_A. The source chronology
and cycle theorem remain unchanged, since p_A^C is still1 mod8 and cubic-good.
PE's elementary overlap estimate gives

    epsilon_A <= 4(A-L_A)/A = (4A-p_A^C+1)/A
               <= 4/(log(4A))^B + 1/A.                 (S7)

This is the new all-epoch gluing rate. It does not alter the pinned source,
and it does not assert a numerical threshold beyond which S1--S7 begin.
Constants and thresholds may depend on the fixed C and B.

## Independent substitution audit for the explicit subgroup input

Assume the root-audited Cochrane--Pinner input bounds the normalized nontrivial
subgroup character by

    delta <= min(1, sqrt(p)/m,
                 lambda p^(1/4)m^(-5/8),
                 lambda p^(1/8)m^(-3/8)),
    lambda^8=256/9.

Then its exact eighth-power rational upper cap is

    delta^8 <= min(1, p^4/m^8,
                  (256/9)p^2/m^5, (256/9)p/m^3).         (S8)

For every admissible prime the last term implies

    delta <= lambda p^(-1/16) b(p)^(3C/8).               (S9)

The exponent is 1/8-(1/2)(3/8)=-1/16; the logarithmic factor is3C/8.
Strictness of the selector only improves this non-strict bound. The roots of
S8 can be enclosed with integer eighth-root arithmetic; no real-number test
is needed for finite certificates. Root is responsible for checking the
classical theorem's subgroup range, normalization, lambda, and whether all
three terms apply simultaneously. This review does not infer global validity
from a paper abstract.

On actual epochs the local marginal then has the proved conditional-on-that-
import rate

    |E_J e(h[U_n(0)]_(p_A^C))|
       <= 4(log(4A))^(-B)+1/A
          +lambda (p_A^C)^(-1/16)b(p_A^C)^(3C/8)

uniformly in p_A^C not dividing h, for every sufficiently large A. This is a
local-source estimate with explicit exponents and a logarithmic epoch cost;
it is not a power saving for the full real Weyl mean.

## Consequence for this front's source-history theorem

CH1--CH6 are stated for any available uniform nontrivial subgroup cap delta.
Substitute S9 and S7 into them for the stronger selector. In particular the
local d-digit transcript satisfies

    TV <= epsilon_A/2+(d-1)/L_A
          +(16^d/2)[1/p_A^C
             +lambda(p_A^C)^(-1/16)b(p_A^C)^(3C/8) H_((p_A^C-1)/2)].

For every fixed alpha<1/16, integers d_A<=alpha log_16(p_A^C) give TV->0.
This is a numerical exponent for the **local** history information horizon,
conditional only on the declared classical theorem, with no unspecified BK
exponent. Its necessary support horizon remains log_16 m_A, so the bound is
not sharp. It does not supply original-zero complementary covariance decay.

Verdict: selector and coverage derivation **SURVIVE** independent paper review.
S8--S9 algebra **SURVIVES**; applicability of the CP input is root's separately
recorded primary-source check. Pi base16 normality and RH remain **OPEN**.
