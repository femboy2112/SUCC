# All-time source congruences, exact precision loss, and Gamma jets

**Authority:** local paper proofs. They identify the fixed four-pole source;
they do not bound a real Weyl sum. Let c=(A,B,C,D) be integer coefficients
at offsets (1,4,5,6), with zero seed. Differences of sources are allowed in
the statements below; the authentic source itself remains unchanged.

## TI-01. Four measurements characterize all-time congruence

Put d(n)=(2n−1)(4n−1)(8n−7)(8n−3), an odd integer at every integer n, and
N_c(n)=4d(n)r_c(n). Direct multiplication gives an integer cubic. Its Newton
coordinates at n=1 are Cc, where

```
C = [  60   15   12   10 ]
    [1032  804  744  692 ]
    [2496 2304 2240 2176 ]
    [1536 1536 1536 1536 ].
```

For every k>=0, the following are equivalent:

1. r_c(n) belongs to 2^k Z_2 for every n>=1;
2. the same holds at n=1,2,3,4;
3. all four entries of Cc are divisible by 2^(k+2);
4. U_n(c) belongs to 2^k Z_2 for every n>=0;
5. the same holds at n=1,2,3,4.

**Proof.** Since d(n) is odd, source divisibility is exactly N_c(n)=0
modulo 2^(k+2). The integer Newton expansion is
N_c(n)=sum_(j=0)^3 (Cc)_j binom(n−1,j). Four initial values and their four
forward differences are related by unimodular integer matrices. Hence four
values suffice for every positive integer n. The orbit recurrence and its
inverse r_c(n)=U_n−16U_(n−1) preserve the ideal 2^k Z_2. This also proves
the finite four-sample equivalence for the zero-seeded orbit. QED.

This sharpens the parent all-horizon mutant construction by classifying the
*entire* congruence lattice. It does not say four finite-precision samples
identify unbounded coefficients. Four exact rational samples were already
used in `observational_succ/bbp_source_memory.py`; that fact is inherited.

## TI-02. Sharp nine-bit coefficient loss

The integer Smith diagonal of C is (1,4,192,30720); its 2-primary exponents
are (0,2,6,11). This is certified without relying on a black-box Smith
implementation: the gcds of all j-by-j minors, j=1,2,3,4, are
(1,4,768,23592960). Their successive quotients give the stated diagonal.
The determinant is nonzero.

Consequently, if two integer coefficient vectors agree in the four
observations modulo 2^k, k>=9, then their coefficient difference is in
2^(k−9) Z^4. To see this directly, C^(-1) has largest denominator
2-adic valuation 11; multiply Cc by the inverse and use TI-01.
An explicit sharp vector is

```
w = (-51,3200,-6825,3696),   Cw = (0,0,0,30720).
```

Its entries are not all even, while r_w(n) is divisible by 2^9 at every
integer time, with valuation exactly 9 at n=4. Multiplying by 2^(k−9)
proves the nine-bit loss cannot be improved uniformly on this coefficient
class. This vector is a signed difference source; no positivity claim is
made for it.

**Height repair.** If each candidate coefficient has absolute value <=H,
then 2^(k−9)>2H suffices for unique identification from the first four
source/orbit residues modulo 2^k. Without a height restriction no finite
precision suffices. With all precisions, the four exact Z_2 observations
identify c. These are source-authentication repairs, not normality inputs.

## TI-03. All derivative orders preserve the age-family blindness

Let e=(1,−3,1,1), K(n)=r_e(n), and c_t=c_auth+t e with t=2^(k+2), k>=1.
The parent's factorization
K_kernel(q)=(1−q)^2(q^3+3q^2+2q+1) proves positivity and matched rank for
t>=0. For every x in Z_2 and every j>=0,

```
v2(K^(j)(x)) = j−2+v2(j!),
v2((r_ct−r_auth)^(j)(x)) = k+j+v2(j!).
```

**Proof.** The derivative of the offset-4 term is
−3(−1)^j 2^j j!/[4(2x−1)^(j+1)], with valuation j−2+v2(j!). The
offset-6 term has valuation 2j−1+v2(j!), and both odd-offset terms have
valuation at least 3j+v2(j!). The first is uniquely minimal, so there is
no cancellation. The formulas hold on all Z_2, not just integer samples.
In particular, adding arbitrary fixed-precision derivatives does not repair
the parent identification failure. Exact jets can discriminate.

For the affine Morita *unit* logarithmic derivative, the difference is
t[(8x−7)^(-1)+(8x−3)^(-1)]. Its jth derivative has valuation

```
k+3+3j+v2(j!).
```

Indeed the two odd denominators agree modulo 4, so their inverse (j+1)th
powers sum to 2 modulo 4. Moreover the complete unit-ratio quotient is

```
H_2,ct(x−1)/H_2,auth(x−1) = [(8x−7)(8x−3)]^t,
v2(H_2,ct/H_2,auth − 1) = k+4.
```

The bracket is 5 modulo 8; the elementary repeated-squaring valuation
v2(a^(2^m)−1)=m+2 for a=5 mod8 proves the assertion. Thus even the unit
factor, beyond its logarithmic derivative, stays blind at fixed precision.
This is the integer-affine Morita ratio, not fractional-argument Gamma_2.

## TI-04. Exact boundary repairs the one-parameter failure

The inherited authentic theorem is C_auth=sum_(j>=0)16^j r_auth(−j)=0 in
Q_2 (October 27 `BBP_BINWINDOW_ZERO_BOUNDARY.md`). For the age direction,
v2(K(−j))=−2 at every j. Hence C_e converges with v2(C_e)=−2: its first
term is uniquely least in valuation. Therefore

```
C_ct = t C_e,  v2(C_ct)=v2(t)−2 for nonzero integer t.
```

Within the age-matched family, the *exact* zero backward boundary identifies
t=0; finite precision does not. Likewise the exact second source jet
Q_ct''(0)=−59+14t identifies t. A single prime13 first-birth residue
distinguishes the prescribed power-of-two mutants because 13 does not divide t;
it does not identify arbitrary t, since multiples of 13 survive that test.

## TI-05. Complete finite 2-adic dynamics remains non-identifying

For an integer coefficient source, the parent integrality condition is
B+2D=0 mod4. Under it, r_c(n)=P_c(n)/d(n), P_c in Z[n], and modulo 2
P_c(n)=D n + constant, while d(n)=1 modulo 2. All nonconstant coefficients
of d are even; all degree>=2 coefficients of P_c are even. Thus

```
v2(r_c(x)−r_c(y))=v2(x−y) for all x,y in Z_2, x!=y,
    if and only if D is odd.
```

For D odd the divided difference numerator is odd, proving the equality;
for D even the image has one parity and cannot be an isometry. The convergent
stationary solution F_c(x)=sum_(j>=0)16^j r_c(x−j) is then an isometry too:
the first difference has strictly least valuation. Its zero-seeded orbit
is U_n(c)=F_c(n)−16^n F_c(0). Hence at each fixed precision it eventually
inherits complete finite permutation cycles even when F_c(0)!=0.
All positive mutants above have D odd. Recovering those cycles cannot
authenticate the source or establish real-circle mixing.

The original authentic isometry and zero boundary are inherited, not new
claims. The new result here is the coefficient-class criterion and its
explicit compatibility with complete-Gauss/fixed-precision hostile controls.
