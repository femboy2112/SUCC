# Scoped cross-agent mathematical review

**Reviewer:** signed-CRT research agent, separately assigned to audit arithmetic, transfer and
root finite-circle work. This is a distinct reasoning pass with access to the completed proofs;
it is not a blind referee, external peer review, or Lean verification. The reviewed byte hashes
are recorded in `independent_review_receipt.json`.

**Verdict:** no blocking mathematical issue found within the statements and code audited below.
No claim that the campaign proves normality, or that a finite probe substitutes for the proofs.

## All-class and prime-power transport

Independently write `q=8(l-1)+s`, `t=L-q`, actual offset `delta=Qs mod8`, and last offset
`d*=QL mod8`. Then

```
M-j = [Q(L-q)+delta-d*]/8,
k-l = [t-s*+s]/8,
(M-j)-(k-l) = [(Q-1)t+s*-s+delta-d*]/8.
```

This verifies the exponent identity in AT-01, including the changed reflected support for
classes 3/7. Raising 16 to that difference gives
`2^((Q-1)t/2) * 2^((s*-s+delta-d*)/2)`. The latter exponent is integral because odd Q
preserves the parity of s. For `S_a=1+p+...+p^(a-1)`, the first factor is
`[2^((p-1)/2)]^(S_a*t)`. Since `S_a==a mod2`, Euler's criterion supplies exactly the class
weights in the table. At Q class3 the authentic weights are `(8,4,4,-1)`; at class7 they are
`(-32,-16,-16,4)=-4` times that list. Even a gives Q=1 mod8 for every odd p.

The bound `p>L` implies `QL+6-d*<pQ`: the excess is at most5, while Q>=p> L>=6.
Thus no omitted denominator has valuation greater than a. Q-divisible denominators have
multipliers q<=L, exactly the 4k claimed events. Coefficients being p-integral is necessary
and is explicitly assumed.

For AT-02 the integer `theta=(chi*2^((p-1)/2)-1)/p` satisfies the exact identity
`2^((p-1)/2)=chi*(1+p*theta)`. Hence the exact relative factor is
`w_s*(1+p*theta)^(S_a*t)`. Because `S_a==1 modp`, its first correction is
`p*theta*t*w_s`. Summing `(L-q)c'_s/q` yields
`L V_k - (sum c'_s)(16^k-1)/15` exactly. The valuation a-1 layer contributes pR;
all lower layers have an explicit factor p². This independently verifies AT-4 with its
stated sign and normalization. It also explains why a naïve lift cannot discard the regular
layer at a=1. A direct modular calculation using original denominators, without importing
the arithmetic implementation, checked 24 admissible (p,a,k) cases across all four classes;
all agree modulo p². These checks support, but do not replace, the derivation.

AT-03's small exceptional cases are legitimate: for Q=3 the unique first top-layer source
denominator is6 at n=1, giving -1/2 mod3; for Q=5 it is5, giving -1 mod5. Larger Q use a gap
at most5 before the next native denominator, strictly smaller than the pQ barrier. The birth
residues are p-units for every odd p. The p47 native-return exception at k1 is real;
at k2, `r(2)=106/819==10 mod47` repairs it within the domain p>14.
The reflected packet zero at p19 is correct: its q4 residue is -19/6 and its q7 residue is
130/21, so absence persists exactly until the next encounter. The p11 first-window length2
versus order5 correctly refutes the transplant of the native full-period guarantee.

For AT-04 the numerator/resultant arithmetic was re-derived: the four resultants are
`4P(1/2)=6`, `16P(1/4)=20`, `64P(7/8)=1920`, `64P(3/8)=-32`. The six pairwise linear
resultants have absolute values `2,6,2,20,4,32`, with no odd factors outside3 and5.
This is a one-source-term passport only; the dossier correctly retains cross-time p19/p73
cancellation. The fixed-support moment equations independently give
`B=(19C+15)/2`, `D=-(15+13C)/2`, `Q''=-61C-120`, so the extra -59 moment really fixes C=-1.
AT-05's seed blindness follows from the literal factor p^a and is restricted to p-integral
rational seeds, correctly excluding the irrational coherent seed from modular reduction.

## Denominator-grid and bounded-posterior obstructions

For the plus prime set, p>2n+2 excludes the next event `(p+1)/2` through n+1; its upper bound
puts the first event at or before n. For the minus set, `3p>8n+8` excludes both possible next
indices `(3p+7)/8` and `(3p+3)/8`, while p<=4n-1 puts `(p+1)/4<=n`. In both cases p² exceeds
the largest source denominator through n+1. There is exactly one source p-pole, so its
nonzero transported residue survives in U_n. Multiplication by15 preserves it because p>5;
r(n+1) is p-integral. Thus the claimed difference valuation is exactly -1.

Subtracting two translated q-grid coordinates proves `den(U_(n+1)-U_n)|q`, and choosing the
first point as the translation proves attainability. The natural-log asymptotic coefficient
11/3 is correct: the plus interval has length6n+O(1), the minus interval length4n/3+O(1), and
each progression class has theta-density1/2. The invoked fixed-modulus PNT is a classical
external theorem, explicitly identified rather than inferred from finite prime counts.

For TR-03, choose n0 so G_n>=exp(3n). Any block containing a tail edge n,n+1 with
`n>log(CN)/3` exceeds the entire budget CN, because M>=1. Every such edge must therefore be
a cut, forcing N-O(log N) blocks, each contributing at least1 to the second budget. This
works even when the partition is chosen separately at each horizon. It excludes the stated
exact natural-surrogate architecture, not approximate surrogates or normality itself.

Stoneham constants were checked as a separate recovery: stage length `(c-1)c^j`, period
`c^(j-1)`, multiplicity c(c-1), and at most `c^(j-1)|I|+3` enlarged-arc sites produce the
stated all-horizon bound. Paying 2*pi*|h| times the total stage tail gives pi*|h|/8.
The frequency divisibility exception in the exact stage character sum is retained.

The posterior Radon--Nikodym derivative is correctly oriented:
`dmu_(a_k)/dmu_(a_N) = [R(a_N)/R(a_k)] exp(8(N-k)x)`.
It is essentially unbounded because the authentic density is positive on every interval in
x>0. A bounded nonnegative likelihood with positive expectation has a bounded normalized
density and therefore cannot give this reverse posterior while retaining the same X.
The claims explicitly allow unbounded reweighting and changed latent-variable instruments.

## Root finite_circle.py interval proof

The integer intervals represent values divided by SCALE. Multiplication uses all four corner
products, then floor/ceil; division by a positive integer rounds outward; negation reverses
endpoints. Every operation therefore encloses the exact real operation, including intervals
that cross zero. Squaring via generic interval multiplication can widen the result but is safe.

Machin's identity and alternating-series errors give a genuine rational pi enclosure. After
reducing the rational turn to [-1/2,1/2], its actual angle has absolute value at most pi<22/7.
The cosine polynomial ends at degree50 and sine at51. The code's Taylor remainders use
orders51 and52, respectively; these are conservative Lagrange bounds because all derivatives
of sin/cos have modulus<=1. The outward interval endpoints of the angle may slightly exceed
pi, but that does not invalidate the remainder: the exact angle being enclosed remains
bounded by pi, and the polynomial interval includes its polynomial value.

The finite BBP lookahead is positive; the remaining exact tail is bounded by
`16^-lookahead/(8(n+lookahead)+1)^2`. Using the midpoint adds at most
`pi*|h|*(hi-lo)` character error per phase, by the chord/angle inequality. Paying the total
error separately in both coordinate intervals is conservative. `isqrt` gives floor/ceil
Euclidean-norm bounds; the final six-decimal normalized endpoints round outward again.
Circle wrap in the lifted positive-tail interval is handled by periodic characters and
modular occupancy-bin labels. The coherent completed counterseed has normalized modulus1
exactly and correctly fails the quarter bound.

As an additional implementation check, 105 rational turns (including exact quarter turns,
negative turns and seeded large-numerator cases) were compared with 100-digit mpmath:
all 210 real/imaginary values lie in the root intervals. These are numerical cross-checks,
not the authority for the interval proof. No production or other-agent file was edited.

## Supplement: independently reviewed sharp conductor-growth argument

The subsequently proposed sharpening is mathematically sound under the explicit order of
limits below:

```
log den(U_n) = 6n+o(n),
log den(U_(n+1)-U_n) = 6n+o(n).
```

Here den means the positive reduced denominator and log is natural logarithm. This is a
selected rational-conductor theorem, not real-circle anti-concentration.

Fix **a constant** 0<epsilon<1 and let K=ceil(1/epsilon)+1. For a prime p>=epsilon*n,
every p-divisible native denominator through time n is p*q with q<8/epsilon, hence belongs
to one of at most K condensed packets. Eventually p>8K+7 and p²>8n; these two requirements
justify applying AT-01 to any of those finite packets and ensure only first p-power poles.

For the last encountered quotient `q=8(l-1)+s`, the p-primary state, multiplied by an
invertible power of16, is the rational partial shadow

```
H_(l,s) = 16 V_(l-1) + sum_(s'<=s) c'_(s')/[8(l-1)+s'].
```

To see this directly, use the canonical end clock M_p(l) in AT-01 and omit its future
p-poles. The same termwise exponent calculation applies to every retained term. If n lies
after the canonical end but before the next birth, the required multiplier is a negative
power of16 modulo p, still a legitimate unit. No unexplained positivity is assigned to an
F_p residue: positivity is used only to prove that the fixed rational H is nonzero.

For classes1/5, the authentic partial source starts with the positive term4/(8l-7), then
subtracts the remaining three positive fractions. Every partial value is at least the final
r(l)>0. Inductively V_(l-1)>=0, so all H are positive. For class3, the first three source
terms are positive, and the final subtraction1/(8l-1) is smaller than the first positive
term8/(8l-6); its full source w(l)>0. Again every H is positive. Class7 is exactly -4 times
class3, so every H is negative. Thus all 16K partial shadows are nonzero rationals.

Their numerator and denominator prime divisors form a finite exceptional set depending on
epsilon. Once n is sufficiently large, every p>=epsilon*n exceeds every exceptional prime.
Hence every such prime whose first source birth has occurred survives with v_p(U_n)=-1,
uniformly over all n after that threshold. This uniformity is valid because the library of
partial shadows is finite; it is not inferred from sampled primes.

Born primes have total logarithmic weight

```
theta(8n;4,1) + theta(4n;4,3) + O(log n) = 6n+o(n).
```

The O(log n) accounts for the small residue-class-dependent endpoint offsets. Discarding
primes below epsilon*n loses at most theta(epsilon*n)=epsilon*n+o(n). Thus
`liminf log den(U_n)/n >=6-epsilon`, and letting the **fixed** epsilon decrease to zero gives
liminf>=6. The denominator divides the lcm of all native denominators. Its first-prime-power
weight is at most the same born-prime sum. Every higher-power contribution comes from
p<=sqrt(8n), and is at most log(8n) per such prime, for total O(sqrt(n)*log n)=o(n).
This proves limsup<=6 and the first equality.

For the difference, `U_(n+1)-U_n=15U_n+r(n+1)`. Discard the fixed primes3,5 and primes dividing
one of the four native denominators at n+1. The latter have total logarithmic weight at most
the log of their product, O(log n). Every other surviving large prime still has valuation-1
in the difference. The same lower limit follows; its upper bound follows from the lcm through
n+1 (or the product of the two reduced denominators). This proves the second equality.

**Essential qualification:** the proof gives no explicit error rate or effective threshold.
The exceptional numerator set grows with K, so one must not replace the fixed epsilon by an
n-dependent epsilon(n) without further control. The limit statement does not require that
replacement. Finite calibration checks all512 partial shadows through32 packets and gives
sample denominator logarithms near6, with an explicitly non-proof label in
`conductor_growth_review_receipt.json`. No sign failure, constant error, or hidden source
mutation was found in this argument.


## Final fixed-filter corollary review

The final SHARP_CONDUCTOR_GROWTH.md section5 (CG-03) also survives independent review.
For a fixed integer polynomial P, direct unrolling gives

```
P(E)U_n = lambda U_n + sum_(t=1)^d b_t r(n+t),
lambda=P(16), b_t=sum_(j=t)^d c_j*16^(j-t).
```

Every b_t is an integer. If lambda is nonzero, primes dividing it cost only a fixed
logarithmic weight, and the4d native source denominators cost O_P(log n). Away from those
primes, the previously proved comparable-prime valuation-1 survives the sum. The lcm through
n+d gives the matching upper bound6. If lambda=0, the prefix disappears and the fixed
rational source sum has denominator bounded by a constant times (n+d)^(4d). P=0 is correctly
handled with den(0)=1. Clearing a fixed denominator also justifies the stated extension to
rational coefficients. The polynomial/degree must remain fixed; the dossier explicitly
excludes moving lags and n-dependent coefficients. This is a conductor dichotomy, with no
signed-character conclusion.

One interpretation correction was made in the signed-CRT documents during integration:
SC-06 is a more limited signed-window target, not a claimed logical consequence of global
normality. Normality alone does not visibly control every sublinear moving window. The
conjecture, threshold, sampled primes, and receipts were unchanged by that wording repair.
