# Pascal generates ternary powers: source theorems and the normality frontier

**Date:** 2026-10-24. **Branch:** `research/pi-ternary-weighted-pascal-2026-10-24`.
**Parent:** draft #272, `6e8fa8b77886b13f1f533ed8083fd88c849d14b3`.
**Main inspected:** `e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
**Authority:** paper proofs, named classical inputs, exact finite checks.
**Real half-retention, one-sixteenth retention and pi normality remain OPEN.**

## 1. What the question produced

The elementary answer is exact:

\[
\sum_{j=0}^k\binom kj2^j=(1+2)^k=3^k.
\]

The same triangle generates every integer power by weighting its entries.
At row4, for example, the weighted terms are1,8,24,32,16, summing to81.
This is the classical binomial theorem, not a new normality argument; see
[DLMF1.2.2](https://dlmf.nist.gov/1.2.E2).

Applying the weights to the authentic source, instead of merely to numbers
2^j, produces three substantive source theorems in this round:

1. **A positive Pascal construction for every prime**, with quadratic real
   error, exact dyadic derivative, normalized analytic isometries, and coherent
   changes of chart. The base-three filter is(13+2E)/15.
2. **A diagonal Pascal construction for81=3^4**, with minimum possible
   denominator3 among all positive powers of3 in the fixed-polynomial
   mechanism, and the complete unchanged dyadic source difference profile.
3. **A weaker conditional symmetry target:** the four binary phases can be
   averaged before testing tripling invariance. The positive all-scale
   collision hypothesis still has to be proved for the original source.

There are also sharp adverse results. Minimum denominator4 for multiplier3
has an unavoidable slow error; naive binary deblocking can amplify the tail
exponentially; and a non-atomic positive-dimensional binary law can retain
all the elementary Pascal/carry identities while failing tripling invariance.

The full proofs are in the [constructor dossier](PI_TERNARY_CONSTRUCTOR.md),
[denominator/reset dossier](PI_TERNARY_TRANSLATOR.md),
[prime-chart/coherence dossier](PI_TERNARY_CHART_COHERENCE.md), and
[adversarial dossier](PI_TERNARY_ADVERSARY.md).
[TPG-01--28](../../docs/CLAIM_SUPPLEMENT_TERNARY_PASCAL.md) indexes their scope.

## 2. Source, context, and the exact obligation

The actual source remains

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_{n+1}=16U_n+r(n+1),\quad y_n=\{U_n\}.
\]

With alpha=pi/16,

\[
U_n=16^n\alpha-T_n,\qquad
T_n=\int_0^1t^n\,d\rho(t),
\quad d\rho(t)=\frac{g(t^{1/8})}{8t^{7/8}(16-t)}dt,
\quad g(x)=4-2x^3-x^4-x^5.
\]

The inherited dyadic interpolation F is an analytic bijective isometry and
has exact uniform differences
\(v_2(\Delta^jF(z))=\nu(j)=2j-s_2(j)-1\).
Those results concern the unwrapped rational source in the dyadic metric.
An unconditional real half-retention estimate was not established previously.

This continuation read the attached repository pointer, relevant prior
conversation context, the live parent and main, and the newly available
sibling [draft273](https://github.com/femboy2112/SUCC/pull/273) at
`8d89711db77fea81920321d32f831eed3dec1e68`. That sibling is not merged here.
Its [history-preservation proof](https://github.com/femboy2112/SUCC/blob/8d89711db77fea81920321d32f831eed3dec1e68/research/2026-10-24/PI_HISTORY_PRESERVATION.md)
shows why an existential slowly growing history schedule merely restates
tripling symmetry. Its positive-history gcd observation already permits
prime-power symmetry as a conditional target. The new contribution here is
the explicit low-degree authentic source filter, sharp denominator cost and
dyadic arithmetic, not a claim to have first noticed that81 is coprime to16.

The unresolved real step is still a source-selected statistical estimate:
positive collision exponent at all required scales, together with invariance
of the same limiting law under an independent multiplier, or the stronger
direct cumulative carry-loss target. Constructing an orbit in another base
does not give that invariance.

## 3. Positive Pascal filters give the bounded differential explicitly

Fix \(q\ge2\) and choose odd \(d\) with \(q\le16^d\). Put

\[
a=(q-1)/(16^d-1),\quad P_{q,d}(E)=1-a+aE^d,
\]

\[
Y_{q,d}(k)=\sum_{j=0}^k\binom kj a^j(1-a)^{k-j}U_{dj}
=q^k\alpha-N_{q,d}(k),
\quad N_{q,d}(k)\sim\frac1{64a^2d^2k^2}.
\]

All weights are nonnegative and sum to1. The formula therefore has no coefficient
amplification of compatible absolute input errors. It is an average of real
source values, not an assertion that their phases are independent.

Let \(\delta=v_2(q-1)\). The coefficients of its dyadic interpolation \(\mathcal Y\) are
\(C_j=a^j\Delta_d^jU_0\), with

\[
v_2(C_j)=\nu(j)+j\delta,\qquad
v_2(C_j/j!)=(\delta+1)j-1.
\]

The second identity makes the differential completely explicit. The j=1
derivative term has valuationdelta; every higher term has valuation at least
2delta+1. Thus, everywhere onZ2,

\[
|\mathcal Y'(z)|_2=2^{-\delta},\qquad
|\mathcal Y(x)-\mathcal Y(y)|_2=2^{-\delta}|x-y|_2.
\]

After normalization \(H_q=2^{-\delta}\mathcal Y\), every chart is an analytic
bijection/isometry ofZ2. Its higher-difference profile is
nu(j)+(j-1)delta; onlydelta0 preserves the original profile exactly.

For base3, this says

\[
Y_3(k)=15^{-k}\sum_j\binom kj13^{k-j}2^jU_j,
\quad Y_3(k)=3^k\alpha-N_3(k),\quad N_3(k)\sim225/(256k^2),
\]

with dyadic derivative of norm1/2 everywhere. For primes2,3,5,7,11,13,
the respective distance factors are1,1/2,1/4,1/2,1/2,1/4 and the reduced
filter denominators are15,15,15,5,3,5. This is a uniform distortion bound4
for that finite list. The general construction covers all primes with a
prime-dependent finite factor; normalization makes each chart isometric.

Base11 provides a particularly small local alternative:

\[
(U_n+2U_{n+1})/3=11U_n+2r(n+1)/3.
\]

It uses two source states and a modulo3 integer-lift label. Its real source
error is alreadyO(n^-2). Statistical preservation of the original law by
this output remains open, just as it does for3 and81.

## 4. Coherence is proved at the chart level, with binary clock compatibility

Normalized transitions
\(\Phi_{p\to q}=H_q\circ H_p^{-1}\) are actual analytic isometries and obey
\(\Phi_{q\to r}\circ\Phi_{p\to q}=\Phi_{p\to r}\).
This is an exact coherent family, anchored to the authentic F because the
canonicalq16,d1 choice isP=E and H16=F.

Binary clock regrouping also has a precise version:

\[
C_{16\to4}=H_4\circ[2]\circ F^{-1},\quad
C_{4\to2}=H_2\circ[2]\circ H_4^{-1},\quad
C_{16\to2}=H_2\circ[4]\circ F^{-1}.
\]

These maps compose exactly; their dyadic scales are1/2,1/2 and1/4.
On source values they send U_n toY4(2n) toY2(4n). In the real metric all
three approximate16^n alpha withO(n^-2) errors. This is a concrete
compatible16-to4-to2 construction.

The scope matters. All charts have dyadic domain. This is not a continuous
field embedding from each Qp intoQ2. Canonical polynomials do not multiply
by base label: P3^2 is notP9, and their source dyadic scales even differ.
One can choose commuting prime-filter products for exact polynomial
composition, but the canonical derivative formula must then be reanalyzed.
The complete distinctions and a finite-polynomial fourth-root obstruction
are proved in the [coherence dossier](PI_TERNARY_CHART_COHERENCE.md).

## 5. The diagonal of Pascal gives81 with the whole original source profile

The second construction uses

\[
P_{81}(E)=1+E\Delta/3=(E^2-E+3)/3.
\]

On the exponentially growing signal its value is81. On the tail its value
is1-t(1-t)/3, between11/12 and1. Therefore

\[
Z_k=\sum_{j=0}^k\binom kj3^{-j}\Delta^jU_j
=81^k\alpha-M_k,\qquad M_k>0,\quad M_k\to0.
\]

This is the diagonal(start=order) of the original Pascal difference table.
The signal term at depthj is240^j/3^j=80^j, and its weighted row sums to
(1+80)^k=81^k. The same diagonal acts as-t(1-t) on the positive real tail.

The new Newton coefficients are exactly3^-j Delta^j U_j, so the complete
nu(j) profile and dyadic isometry survive without normalization. This is
stronger profile preservation than the positive affine ternary chart.

The denominator3 is globally minimal across all fixed rational polynomial
filters reaching any3^m with vanishing absolute remainder. Denominators1
and2 fail the endpoint at1. At denominator3 the endpoints require4 dividingm;
m4 is attained by the displayed quadratic. No claim is made that every
multiple of4 can be attained with denominator3.

At the origin the error is only asymptotic to
Gamma(1/8)(3/k)^(1/8)/32. A fixed source shift n>=2 repairs that rate:

\[
S_k^{(n)}=P_{81}(E)^kU_n-81^kU_n
=81^kT_n-M_{n,k},\quad S_0^{(n)}=0,
\]

\[
M_{n,k}\sim9/(64k^2),\qquad
S_{k+1}^{(n)}-81S_k^{(n)}\sim45/(4k^2).
\]

The rational source retains its full dyadic profile, and the new forcing is
positive and completely monotone. Its forcing profile is different: its
first difference has valuation2, versus0 for the original forcing.
For n2 the represented constant is16pi-205826/4095. Classical rational
affine preservation gives the same base81 normality status aspi, and the
power-of-base theorem identifies base81 withbase3. These statements do not
identify arbitrary empirical laws or transfer base3 normality tobase2.

The quadratic also has a short norm interpretation. For
omega=(1+i sqrt11)/2, omega^2-omega+3=0 and16-omega=conjugate(omega)^5.
ThusP81(t)=norm(t-omega)/3 andP81(16)=3^4. This algebra explains its
positive real kernel; it does not give independence or equidistribution.

## 6. Costs and failed shortcuts are part of the result

| Source filter | Multiplier | Universal division label afterk iterates | Real absolute error at the origin | Dyadic behavior |
|---|---:|---:|---|---|
| (E-1)/5, inherited | 3 | 5^k | exponential5^-k timesk^-1/8 | k-th value has valuationnu(k); no isometry assertion |
| (E-4)/4 | 3 | 4^k | constant timesk^-1/8 | normalized valuationv2(k)-2k |
| (13+2E)/15 | 3 | 15^k | 225/(256k^2) asymptotically | similarity factor1/2 |
| (E^2-E+3)/3 | 81 | 3^k | constant timesk^-1/8 | full original source profile |
| Same81 filter after fixed shift>=2 and reset | 81 | 3^k for the filter numerator; retain the explicit reset term | 9/(64k^2) asymptotically | full original source profile |

The cover statements concern universal readout across unrestricted integer
lifts; they do not assert uniformity of actual carry labels. A single local
application needs only the fixed cover, whilek iterates need itsk-th power.
The quarter filter is denominator-minimal for base3, but every fixed
denominator4 filter has even errorOmega(k^-1/8). Denominator5 is the least
allowing exponential decay, and1/5 is the optimal exponential rate there.

The direct positive row based on U_j/8^j has spectral value3 but error
\(\int(1+t/8)^kd\rho(t)\sim81(9/8)^k/(64k^2)\), which grows.
This follows from the endpoint at1, with logarithmic slope1/9. Its
order128 error is certified above1. The rational binary deblocking
B_(4n+s)=2^sU_n has a separate failure: its tail has four fourth-root
branches. Unsigned Pascal amplifies its error like(15/4)2^k/k^2, while
the integer filter2E-1 has error asymptotic-(45/64)(-3)^k/k^2.
No statement about the remainders' fractional-part distributions follows.

## 7. The real statistical gap can be made more precise

On the circle, tripling already has an exact division-free readout:
T3x=x+T2x. Predicting its firstm binary output bits fromm+L input bits
fails precisely on the two alternating lengthL suffixes. Their Haar mass
is2^(1-L). Adjacent00 clears a carry,11 sets it, and01 or10 propagates
it. Efficient finite carry synchronization does not imply law preservation.

An exact non-atomic control demonstrates the difference. Let the binary
bits be independent with probability1/4 of1. This law is invariant under
T2 andT16 and has positive all-scale collision exponentlog2(8/5). Its
mass in[0,1/2) is3/4; after tripling it is33/52. The discrepancy is3/26,
despite exponentially small long-alternation probabilities.

The four-phase law

\[
\overline\mu=\tfrac14(\mu+(T_2)_*\mu+(T_4)_*\mu+(T_8)_*\mu)
\]

is automatically T2-invariant whenmu isT16-invariant. Ifmu has a positive
all-scale collision exponent, so doesmu-bar, with an explicit constant
proved by convexity and Cauchy-Schwarz. It is sufficient to prove tripling
invariance ofmu-bar. Rigidity then givesmu-bar=Haar; dominationmu<=4mu-bar
makesmu absolutely continuous, andT16-invariance plus Fourier decay gives
mu=Haar. The raw symmetry condition is strictly weaker, asdelta_(1/5)
and its uniform four-phase orbit show.

For the actual windows the new symmetry estimate is

\[
\frac1{4N}\sum_{n\in I}\sum_{r=0}^3
\left[e(3\cdot2^rh y_n)-e(2^rh y_n)\right]\longrightarrow0
\quad\text{for each fixed nonzero integer }h.
\]

It permits cancellation across the four binary phases. This estimate remains
open. The finite-block formulation in the adversarial dossier bounds its
carry-boundary error automatically under the collision hypothesis, but leaves
an explicit block-law discrepancy to be proved.

Alternatively, the local modulo3 source outputs for11 or81 can be compared
with the same original window law. Their source approximation errors are
alreadyO(n^-2). No statistical comparison is supplied by those identities.

The classical nonergodic rigidity input only guarantees a Haar component
from positive average entropy. The all-scale collision bound permits repeated
subtraction of that component and rules out a zero-dimensional residual.
This extra step is retained; terminal-scale saving and positive entropy alone
are not substituted for it.

## 8. Proof authority, validation, and the next target

The [validation record](PI_TERNARY_VALIDATION.md) states actual executed gates,
finite ranges, hashes and development corrections. Production and tests were
frozen for the full discovery run; the late all-prime/coherence additions
are paper results with their own exact standalone calibration. They do not
silently enlarge the authority of the36 unit tests.

The next consequential arithmetic result is a quantitative bound on the
four-phase symmetry defect or the local11/81 output-law discrepancy, together
with the positive all-scale real collision estimate. The inherited direct
one-sixteenth retention criterion remains an alternative. The new prime
charts, positivity and exact dyadic derivative do not yet bound that real
conditional carry frequency.

Primary external inputs used here are the
[binomial theorem](https://dlmf.nist.gov/1.2.E2),
[rational affine normality preservation](https://web.cs.ucdavis.edu/~doty/papers/fsdra.pdf)
(Theorem4.3 and Corollary4.4),
[power-base equivalence and independent-base boundary](https://math.berkeley.edu/~slaman/papers/bases.pdf),
and the precise [nonergodic Rudolph--Johnson theorem](https://www.math.ias.edu/~akshay/research/blmv.pdf)
(Theorem1.3). The new source identities and local reductions have their
displayed proofs. No claim of scholarly priority, new Lean checking, or
independent external refereeing is made.
