# Fibonacci arrows meet the native radix16 source

**PROVED LOCAL** refers to the paper derivations below, with exact finite
checks and a separate computational oracle. **OBSERVED** marks finite phase
counts. No independent external referee, Lean certification, scholarly
priority, new fixed-frequency asymptotic saving, π normality or RH proof is
claimed. This is an additive child of PR408 at
`7b5a2b4534aa5e71865046ca8d3f723d8002b9fe`.

The author's Harmonic / Golden / Euler–Mascheroni triangle and
Oily–Macaroni Ω_OM=φ^(-1)−γ retain Leah / femboy2112 provenance. This front
asks what an asserted Fibonacci time arrow would have to do to the **actual**
source and selected boundary, not merely to its positive Gamma limit.

Write F0=0,F1=1,F_(k+1)=F_k+F_(k−1), λ=φ^(-1), and

    r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2),
    U0=0, U_n=16U_(n−1)+r(n).

A changed seed is denoted U_n(s); it never silently replaces U_n(0).

## FA01 — the exact local place where linear clocks agree

Let M=[[1,1],[1,0]], the Fibonacci transfer in the coordinate convention of
this paper. It is conjugate by coordinate exchange to the matrix in the
prior `fibonacci_epicycle_demon/RESEARCH.md`.

For any integer m>=1, the complete set of row vectors over Z/m satisfying

    L M = 16 L

is

    L=(16t,t), 239t=0 (mod m).                              (1)

There are exactly gcd(m,239) such rows. Over Q or R, only L=0 exists.
Over Z/239^a with a>=2 every solution row has both coordinates divisible by
239^(a−1), so no primitive row modulo239 lifts to a primitive row at the
next precision while the radix remains16.

**Proof.** Write L=(x,y). The second coordinate equation gives x=16y;
the first then gives239y=0. The same calculation over Q/R gives y=0.
Equivalently det(M−16I)=239 and its integer Smith factors are1,239.
Primality of239 follows by testing the primes2,3,5,7,11,13 below sqrt239.
No claim about nonlinear/time-dependent arrows is made.

The same proof works for any integer radix b>=2: the complete rows are
(bt,t) with (b²−b−1)t=0. Thus239 is native to the **chosen radix16**
comparison, not uniquely to π. For b2 the determinant factor is1 and no
nonzero modular row exists; b3 gives5 and b10 gives89. These are matrix
compatibility factors, not the exceptional-prime passports of the BBP poles.

The golden root itself does lift: x²−x−1 has value239 at16 and derivative31,
a unit mod239. If x_a is its root modulo239^a near16, the unique next digit
is

    x_(a+1)=x_a+239^a d,
    d=−[(x_a²−x_a−1)/239^a](2x_a−1)^(-1) mod239.           (2)

Expanding the polynomial proves (2) directly. The second-precision lift in
this chosen residue class is x2=44231 modulo57121, not16. Thus lifting the
Fibonacci eigenvalue changes the clock. The other eigenvalue mod239 is
−15. Exact exponentiation gives ord239(16)=119 and ord239(M)=238; these
finite group facts are not a conjugacy of the original real selected orbit.

The apparent resonance has a further exact footprint:

    16^k−16F_k−F_(k−1)
      =239 sum_(j=1)^(k−1)16^(k−1−j) F_j,  k>=2.         (3)

To prove it, use M^k=F_k M+F_(k−1)I and divide x^k−F_k x−F_(k−1)
by x²−x−1, or induct directly. The right side is strictly positive.
The factor239 is the arithmetic mismatch of the two characteristic
polynomials. Its appearance here does not identify it with the239 in a
Machin arctangent formula; those are different derivations.

## FA02 — the authentic forcing breaks the local homogeneous match

The original recurrence gives, **for every seed s and every n>=0**,

    U_(n+2)(s)−U_(n+1)(s)−U_n(s)
      =239U_n(s)+D_n,
    D_n=15r(n+1)+r(n+2)>0.                              (4)

All four poles remain present in D_n. Positivity follows from the exact
kernel Q(x)=2(1−e^(−3x))+(1−e^(−4x))+(1−e^(−5x)). Since
15x e^(−5x)<=Q(x)<=15x, integrating against exp(−ax) gives

    240/(8n+14)² <= D_n <= 240/(8n+1)².                 (5)

The lower bound deliberately uses a common larger denominator for both
positive terms. It is strict for the authentic kernel. This is a summable
source defect, not a signed saving.

Already at n=0,

    D0=38599/819,    D0 mod239=198.                     (6)

All denominators in (6) are prime to239. Thus even where the homogeneous
linear clocks resonate, the authentic zero-boundary orbit is not an
unforced Fibonacci orbit. For n=0..57, all states in (4) are239-integral,
so ordinary reduction is legitimate; after conductor birth it must be
replaced by an explicitly scaled rational reduction.

The first239-conductor birth is exactly at **n=60**:

    239 U60 ≡ −1/2 ≡119 (mod239).                     (7)

**Proof with denominator hypotheses.** The first multiple of239 in the
four denominator progressions occurs in8n−2 at n60 (denominator478).
The other first appearances are n90 in8n−3, n120 in8n−4, and n210 in8n−7.
Thus U0,...,U59 are239-integral, and239r60 reduces to−1/2; the multiplied
previous state reduces to0. The residue is nonzero, so the denominator
cannot cancel. This is an authentic source-local arithmetic fact. It does
not determine the complementary real phase.

The parent shift-module classification supplies an exact status check.
For P(z)=z²−z−1,

    P(16)=239,
    P(z)=239−(16−z)(z+15),
    α_P=239π−16[15r(1)+r(2)].                          (8)

Here α_P belongs to the **derived filtered source**, reset to zero seed;
it is not the original source. The unreset observable P(E)U_n starts atD0.
Equation (8) therefore preserves equivalence to π's unresolved normality
question, rather than annihilating it. Conversely −P is positive on[0,1]
and gives a positive filtered source with the same unresolved equivalence.
This positive mutation distinguishes an arithmetic classification from a
source-identification theorem.

For characters, (4) is only

    e(hU_(n+2))/(e(hU_(n+1))e(hU_n))
      =e(239hU_n)e(hD_n).                              (9)

The source error tends to1, while the full selected factor e(239hU_n)
remains. Discarding it would discard exactly the unresolved signed problem.

## FA03 — what Fibonacci interval tiling does and does not assemble

For any bounded complex sequence z_n, greedily subtracting the largest
Fibonacci number gives N=L1+...+Ls, with nonconsecutive Fibonacci indices
and successive lengths at most half their predecessors. Indeed the remainder
after subtracting F_k is less than F_(k−1); the next admissible length is
at most F_(k−2), and2F_(k−2)<=F_k. Applying the same argument repeatedly
proves existence and the decay needed here; uniqueness is not needed.
This is the classical Zeckendorf decomposition mechanism; see the primary
research treatment by [Kologlu, Kopp, Miller and Wang](https://arxiv.org/abs/1008.3204).

Set A1=0,A_j=L1+...+L_(j−1). The exact assembly inequality is

    |sum_(n=1)^N z_n|
       <= sum_j |sum_(n=A_j+1)^(A_j+L_j) z_n|.          (10)

If the indicated blocks satisfy a power bound C L_j^α, α>0, then

    |sum_(n=1)^N z_n| <= C N^α/(1−2^(−α)).             (11)

This is a finite conditional inequality, not an authentic bound. At α=1
one may use the sharper CN directly. The tests certify the elementary
square-root cost with the conservative rational constant4.

The usable asymptotic version must retain **which translations are covered**.
Put B(L,C)=max_(0<=A<=CL)|sum_(n=A+1)^(A+L) z_n|. For any0<δ<1, discard
all greedy blocks shorter thanδN. They form a terminal tail of total length
at most2δN. Every retained block has A_j<=N<=L_j/δ, hence

    |sum_(n=1)^N z_n|
       <= sum_(L_j>=δN) B(L_j,1/δ)+2δN,  if |z_n|<=1. (12)

There are at most1+log2(1/δ) retained blocks. Thus
B(F_k,C)=o(F_k) for every fixed C is sufficient for cancellation; after
letting N grow, sendδ to0. Applied at every integer h to z_n=e(hU_n),
this is an **unproved/equivalent criterion**, not a normality proof.

A tempting stronger demand is wrong as a necessary condition: even a normal
base16 number contains zero words of arbitrary lengths. A zero word of
lengthL+K makes L consecutive pure-radix phases at most16^(-K). Consequently
no o(L) bound uniform over *all* starting positions can hold for every normal
number. Such intervals may start far beyond any fixed multiple ofL; the
A<=CL restriction matters. A constant fractional saving on one Fibonacci
window per scale supplies neither (12) nor an improving product of savings.

The parent logarithmic slip theorem, applied to A=F_k, remains logarithmic:
a bounded number of neighboring Fibonacci intervals covers[A,8A), and there
are only O(log N) such scales. Reindexing that theorem does not strengthen it.

## FA04 — a normal path can have coherent Fibonacci snapshots

Write a real x in base16 with digits d_j, j>=1, and start from **any normal**
x. For each k>=2 replace digits in positions

    F_k+1,...,F_k+k²

by0, leaving all other digits unchanged. Call the new numberβ. The number
of edited positions up toN is O((log N)^3): F_k grows geometrically, so only
O(log N) starts precedeN and sum_(k<=K) k²=O(K³). Overlaps only reduce
this bound. A word of lengthm changes its occurrence indicator only if it
meets an edited position; at mostm starting positions are affected per edit.
Thus every fixed word frequency changes by o(1), and **β is still normal**.
This direct substitution proof is elementary; related stronger modification
results are established by [Aistleitner, On modifying normal numbers](https://www.math.tugraz.at/~aistleitner/Publications/Modified_normal_numbers_revised_2.pdf).

Yet

    0 <= {16^(F_k) β} <=16^(−k²),
    e(h16^(F_k) β) ->1 for every fixed integer h.        (13)

The number0 has identical coherent limits, and its first k² observed digits
at these snapshots agree exactly withβ's. Thus Fibonacci sampled coherence
is compatible with both normality and nonnormality. These are radix16 paths,
not merely arbitrary circle rotations.

Embed this control in the **same authentic forcing** by choosing
s=(β−π)/16. The source identity is

    U_n(s)=16^(n−1)β−T_n.

At n=F_k+1 its characters still tend to1 by (13) and T_n->0, although the
full path is normal. The coherent seed−π/16 gives the corresponding
nonnormal control. Both preserve the entire positive-source
harmonic/golden/Euler/Fibonacci geometry. Neither is U0=0, so this is not a
counterexample to the authentic selected trajectory. The original boundary
must remain an explicit input to every claimed inference.

## FA05 — the golden direction is an actual conditioning obstruction

Cassini's identity gives, for every real x and k>=2,

    ||x|| <= F_k ||F_k x|| + F_(k−1) ||F_(k+1)x||,       (14)

where ||.|| is distance to an integer. It follows by writing
1=(-1)^(k−1)[F_k²−F_(k−1)F_(k+1)] and using the circle triangle inequality.
This is the precision cost for reconstructing a unit step from two
consecutive Fibonacci lags.

The exact identity

    F_k λ−F_(k−1)=(-1)^(k−1) λ^k                      (15)

follows from λ²=1−λ and induction. For k>=2 both sampled distances equal
λ^k andλ^(k+1), but ||λ||=λ²>0. Therefore a scale-independent replacement
of the growing coefficients in (14) is impossible. Indeed any estimate
||x||<=C_k(||F_kx||+||F_(k+1)x||) requires
C_k>=λ²/[λ^k(1+λ)], of orderF_k. The golden ratio is load-bearing here:
it is a concrete near-kernel direction of the lag-observation map.

For squared chord energies, 1−cos(2πF_kλ)=O(λ^(2k)) while the unit-lag
energy is positive; the necessary comparison constant grows as F_k².
This rotation is a control for the general lag-comparison theorem, **not**
a model of the original ×16 orbit. Any source-specific improvement must
exclude its mechanism using a valid extra hypothesis, not assume its absence.

## Fresh signed calibration and the smallest remaining obligation

The declared intervals[F_k,F_(k+1)), k7..15 at h1,3,7 and fresh k16 at
h11,13 give **29 exact configurations**. Distances of the complete rational
lag phase from integers exceed1/20 in3744 of4142 frequency-time observations;
each individual count exceeds half. These are OBSERVED finite counts.
The first three configurations atF7=13 have8/8 slips; the longest holdouts
have555/610 and545/610. All counters retain the full phase; no primary/cofiber
independence assumption is made.

The same-forcing coherent seed has
||hΔU_n||<=16|h|/(8n+1)^3<1/20 throughout every tested window, hence zero
slips there. A separate oracle reconstructs all29 authentic counts from a
6644-bit rational Machin enclosure and24-term rigorous Green-tail intervals;
no ambiguous classifications occurred. This is method separation, not a new
independent proof authority.

The actual unresolved task is to prove a selected signed estimate on the
macroscopic blocks in (12), or the parent's full signed CRT/repunit-energy
certificate, from the exact original source and U0=0. A half-slip count at
one frequency would itself give only a fixed saving, not normality. The
Fibonacci resonance theorem identifies an exact local obstruction, while
the snapshot and conditioning controls prevent false extrapolations.
None supplies the missing all-horizon selected cancellation inequality.
