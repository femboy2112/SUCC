# Operation Gamma -> Haar: rigorous infinite-to-finite Fourier window bridge

2026-11-02. Research only, additive follow-up to draft PR #461. Cross-check current unit–unit differential in draft #463. Original BBP four signed poles and literal U_0=0 are immutable. Base-16 normality of pi, signed Weyl cancellation, RH, and a positive asymptotic Haar-wavelet saving remain OPEN.

## GH-01: The original BBP forcing is an exact Gamma differential

Use e(t)=exp(2*pi*i*t) and the original four signed terms

r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
U_0=0, U_n=16U_(n-1)+r(n), alpha=sum_(n>=1)16^(-n)r(n)=pi/16.

Put c=(4,-2,-1,-1), d=(1,4,5,6),
G(t)=product_i Gamma(t+d_i/8)^(c_i), and H(t)=G(t+1)/G(t).
Gamma(z+1)=z Gamma(z) gives H(t)=product_i(t+d_i/8)^(c_i), hence

  r(n)=(1/8)*(d/dt) log H(t) evaluated at t=n-1.       (1)

For 1<=a<=b,

  sum_(n=a)^b r(n)=[(log G)'(b)-(log G)'(a-1)]/8.         (2)

For the FULL source-weighted lag F(n,k)=U_(n+k)-16^k U_n,
k>=1, exact summation by parts gives

  F(n,k)=(1/8) d/dt [
    log G(t+k)-16^(k-1)log G(t)
    +15 sum_(j=1)^(k-1)16^(k-j-1)log G(t+j)
  ] evaluated at t=n.                                    (3)

Proof: substitute the Gamma recurrence in each r(n+j), weight by
16^(k-j), and telescope. These are authentic source identities, not
character cancellation estimates. In the digamma expression for log G,
the common Euler–Mascheroni -gamma term cancels because sum_i c_i=0;
it is not an independent phase parameter of this unrenormalized ratio.
Classical source: NIST DLMF https://dlmf.nist.gov/5.5.

## GH-02: A genuine all-M positive infinite Gamma/Beta tail certificate

The original four-pole positive polynomial factors exactly:

  P(u)=4-2u^3-u^4-u^5
      =(1-u)(u^2+2)(u^2+2u+2).

Direct Beta integration reproduces every signed source value:

  r(n)=integral_0^1 u^(8n-8) P(u) du.                    (4)

For alpha_M=sum_(n=1)^M 16^(-n) r(n), M>=0, monotone
integration of the infinite geometric series yields

  alpha-alpha_M=(16^(-M)/16)
    integral_0^1 [u^(8M) P(u)/(1-u^8/16)] du.           (5)

Since 4(1-u)<=P(u)<=15(1-u), and 1<=1/(1-u^8/16)<=16/15,
the following two-sided rational bounds hold for EVERY integer M>=0:

  16^(-M)/[4(8M+1)(8M+2)]
  <=alpha-alpha_M<=16^(-M)/[(8M+1)(8M+2)].              (6)

This is an all-horizon statement, proved analytically rather than
extrapolated from finite tests. It is a specialization of SUCC's already
developed positive Gamma/Beta source carrier, not a novel Gamma theory.

There is also a closed finite-source integral:

  U_n=16^(n-1) integral_0^1 P(u)
        [1-(u^8/16)^n]/[1-u^8/16] du.                    (7)

## GH-03: One finite rational Gamma truncation controls EVERY finite Fourier window

For every fixed integer h and every subset I of {1,...,M}, the
Lipschitz character bound |e(s)-e(t)|<=2*pi*|s-t| and (6) prove

  sum_(n in I)|e(h16^n alpha)-e(h16^n alpha_M)|
  <=2*pi*|h|*(16^(M+1)-16)/
     [15*16^M*(8M+1)(8M+2)]
  <epsilon_(M,h):=32*pi*|h|/[15(8M+1)(8M+2)].          (8)

The TOTAL error of an entire M-sample prefix and EACH of its finite
windows is O_h(M^(-2)), not M times an independently assigned phase
error. All alpha_M and 16^n alpha_M are exact rational numbers,
and the source zero seed is unchanged. This proves that infinite Gamma
structure can pin finite windows down to arbitrarily high precision.
It does NOT make their complex amplitudes cancel.

## GH-04: Exact SUCC differential / Haar signed block-energy identity

Let N=2^J, z_n=e(h16^n alpha), and partition [1,N] at a
scale L=2^j into adjacent pairs of L-sample blocks. Let A and B
be their signed complex amplitudes, retaining the actual phase.
Define child energy E=Sum_pairs (|A|^2+|B|^2),
Haar-difference energy W=Sum_pairs |A-B|^2, and
parent energy Pparent=Sum_pairs |A+B|^2. Then

  Pparent=2E-W.                                        (9)

Hence simply knowing W>=0 (or positivity of source Gamma jets) gives
NO saving. The exact quantitative content required is a lower bound
W>=delta*E with delta>0. There is no such proved source-selected
asymptotic bound in this branch.

Let E^M,W^M be the same window energies computed from rational
alpha_M. Since the sum of all pointwise complex errors is at most
epsilon_(M,h), disjoint block partitions and
||a|^2-|b|^2|<=(|a|+|b|)|a-b| give, at EVERY level L,

  |E-E^M|<=2L*epsilon_(M,h),
  |W-W^M|<=4L*epsilon_(M,h).                             (10)

For rational complex approximants with a CERTIFIED total pointwise
error eta (including the Gamma tail and rational sine/cosine Taylor
remainders), exact rational energy estimates Ehat,What satisfy

  |E-Ehat|<=2L*eta+eta^2,
  |W-What|<=4L*eta+eta^2.                                (11)

Thus a strictly positive rational comparison

  What-(4L*eta+eta^2) > delta*(Ehat+2L*eta+eta^2)        (12)

is a FULLY RIGOROUS finite certificate for W>delta E at that
particular (N,h,L). It does NOT imply the same inequality at unbounded
horizons. The separately reproducible finite-certificate code uses
Machin arctan and rational Taylor enclosures, never preloaded pi digits.

## GH-05: Conditional ALL-PREFIX Haar bootstrap (not a normality proof)

For EACH fixed nonzero h, suppose there exist theta_h in (0,1),
delta_h in (0,2], and J_h such that for all J>=J_h, each
aligned dyadic pair of L=2^j blocks inside {1,...,2^J} satisfies

  |A-B|^2>=delta_h*(|A|^2+|B|^2)                         (13)

whenever ceil(theta_h*J)<=j<J. This is a NEW OPEN
SOURCE-SELECTED INEQUALITY, stronger than base-16 normality.

Writing k=ceil(theta_h J), q=1-delta_h/2<1, iterating (9)
from the bottom mesoscopic windows to root gives

  |S_(2^J)(h)|/2^J<=q^((J-k)/2).                         (14)

Powers-of-two-only saving would NOT establish full normality. To
handle EVERY prefix m<=2^J, split [1,m] into its aligned dyadic
binary-block decomposition. A block of size 2^j, j>=k, has
absolute sum <=2^j q^((j-k)/2); smaller blocks use trivial length.
Therefore

  max_(m<=2^J)|S_m(h)|/2^J
    <=2^(k-J)+sum_(j=k)^J 2^(j-J)q^((j-k)/2)->0.        (15)

Proof of the limit: let j=J-t; for fixed t the summand
2^(-t)q^((J-t-k)/2)->0, and the sum is dominated by
the summable 2^(-t). Arbitrary horizons lie between consecutive
powers of two, so S_N(h)=o(N). If (13) holds for every fixed
h!=0, classical Weyl proves base-16 normality of pi and the
source Green transport transfers it to the original U_n.

GH-05 is a paper-proved implication only. The ALL-N source-selected
premise (13) is UNVERIFIED and might be false for the original pi
orbit; normality alone need not imply it.

## GH-06: Gamma source can be perfectly coherent on the wrong seed

Take altered real seed U_0*=1/5-alpha under the SAME four original
poles. The completed point is q=1/5, since
U_n*=16^n/5-T_n. All G(t), H(t), P(u), Gamma moments and Gamma
derivatives are IDENTICAL to the authentic ones. But the completed
Fourier orbit e(h16^n/5)=e(h/5) is constant because 16=1 (mod 5).
Thus A=B in every window pair, W=0 and E>0 for all N,L.
The common-Gamma identities cannot certify (13) without using
the exact original zero boundary/real-circle phase. Draft #463
supplies an additional all-positive high-order source differential
with a coherent changed-source shadow.

## Finite execution, scope and falsifiable next step

The accompanying full staged package (available in the chat artifact)
has 13/13 local exact tests passing and eight finite rational
Machin/Taylor Gamma-Haar certificates at:
(M,h)=(64,1),(128,2),(128,9),(128,11),
(256,1),(256,3),(256,5),(256,7);
all showed W>0.01*E at L>=16 at those finite horizons.
The (128,2/9/11) modes were selected before exact enclosure runs;
the 256 modes had prior exploratory evaluation; neither constitutes
independent blind evidence. At (256,5,L=128) the approximate
ratio is only ~0.028326, a warning against assumed uniform margins.

This is NOT π-normality and no theorem is promoted.
The next discriminator is to prove or refute a source-derived
all-scale estimate of type (13), preserving the signed off-diagonal
terms inside A-B. An all-time Gamma source identity without the
selected real phase, isolated prime clocks, high conductor, or an
arbitrarily accurate finite sample cannot provide that inequality.
If (13) fails, explore averaged bad-window energy with separate
ALL-PREFIX control, rather than changing the normality criterion.

Provenance: Main XIX 81045770234a114247e43eb08ae5c6d446e9514a;
parent WEYL BORG PR #461 head bd5d2544bea8037df6d52fc3b64eb8fe7adf5979;
unit–unit-SUCC draft #463 is a parallel research branch.
Do not merge, tag, release, or promote proof status without authorized
review and full tests.
