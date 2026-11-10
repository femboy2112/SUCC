# Exact source isolation, growing carry memory, and hostile covariance

Status: **PROVED LOCAL paper arguments**, with bounded exact checks. The source
is always labelled. Statements C2/C3 use the unchanged four-pole BBP forcing;
C4 deliberately changes it. No new zero-source covariance upper bound is proved.
These are separate same-model proof and implementation bearings, not scholarly
independence. No worldwide novelty or Lean certification is claimed.

## C1. Exact finite source certificates can isolate zero

A universal assertion that finite memory cannot authenticate rational zero is
false: an exact authenticated `U0=0` is finite data. The obstruction concerns
access precision and omitted domain conditions, not memory size alone.

Let s=a/q be reduced rational, q>0. For a prime p, equality of canonical
p-principal parts `[x+s]_p=[x]_p` is equivalent to s being p-integral. If a finite
set S contains **every** prime dividing q and s is p-integral for every p in S,
then q=1: any prime factor of a nontrivial reduced q contradicts integrality.
Thus s is an integer. Adding |s|<1 proves s=0. At any later time n the same
argument applies to the difference 16^n s, provided the complete support claim
is made for that difference. Testing only odd places is insufficient unless
the seed denominator is independently known to be odd: s=2^(-k) has zero odd
principal parts for every odd prime, yet is not zero.

This distinction is exact. A terminal **union** of allowed primes is weaker
than chronological support: a prime allowed because it is born late must not
be silently admitted at time zero. If the initial support must equal the
original initial support, it is empty and already forces a rational seed to
be integral. A no-new-primes certificate is an extra universal domain statement,
not something inferred from having inspected finitely many positive coordinates.

### Sharp height threshold

Fix denominator bound Q≥1, finite prime set E, and nonnegative integers k_p.
Assume `v_p(s)≥k_p` for p in E. Put

    N=product_(p in E) p^(k_p),
    q*=max{q≤Q : gcd(q, product_(p in E)p)=1}.

For every nonzero such reduced s,

    |s| ≥ N/q*.                                           (C1)

Indeed its denominator is coprime to E and therefore ≤q*, while its nonzero
numerator is divisible by N and has absolute value at least N. Equality is
attained by s=N/q*. Consequently |s|<N/q* isolates zero exactly, and the strict
inequality cannot be weakened to ≤. With E empty this is the familiar 1/Q
threshold. With E={2}, it is 2^K divided by the largest odd denominator ≤Q.

An exact height bound changes the identification problem. The unbounded rational
family is dense and has no such positive gap. Fixed height, growing height,
short program description, and finite memory are different resources.

## C2. The exact BBP carry cylinder and a linear growing-memory obstruction

Write U_n=U_n(0), x_n={U_n}, C_n=floor U_n and
κ_n=C_n−16C_(n−1). The source recurrence gives for every real seed s

    U_n(s)−U_n=16^n s.

Suppose the observer retains C0=0 and the exact carry transcript κ_1,…,κ_J.
This is equivalent to retaining C_0,…,C_J. Its exact seed fiber is

    0 ≤ s < σ_J,
    σ_J=min_(0≤n≤J) (1−x_n)/16^n.                         (C2)

Proof: equal floors require `−x_n≤16^n s<1−x_n` at every n. The n=0 lower
constraint is s≥0, which implies all other lower constraints. The upper
constraints give C2. At s=σ_J a minimizing constraint crosses an integer, so
the half-open boundary is sharp. Without C0, adding any integer to the seed
preserves the later κ sequence; the initial lift must not be dropped.

### A completely elementary uniform lower bound

Let L(m)=lcm(1,…,m). We use `L(m)≤4^m`. One proof is induction: the prime-power
valuation formula gives

    L(m) | binom(m,floor(m/2)) L(ceil(m/2)).

For each prime, any prime power absent from the latter lcm but ≤m is larger
than both half sizes and contributes one valuation to the binomial; there is
at most one extra power. Also the central binomial coefficient is ≤2^(m−1)
for m≥2 (two equal middle terms for odd m; the two adjacent terms together
dominate the middle term for even m). The induction gives at most 4^m in both
parities. The case m=1 is immediate.

Every original pole denominator through n is at most 8n, so the reduced
denominator d_n of U_n divides L(8n). Hence

    1−x_n≥1/d_n≥16^(−4n),
    16^(−5J)≤σ_J≤16^(−J).                                (C3)

This bound is deliberately elementary and not claimed optimal. The exact
quantity σ_J in C2 is sharp.

Now use the prior AR-01 construction with B=2A−1, eta=1/8, any finite
2-adic precision K_A, and all observed odd primes through 8B, plus any fixed
additional odd primes. Choose

    J_A=floor((A−1)/5).

The constructed positive rational seed satisfies

    s_A <16^(−A)+(1/8)16^(−B)
        ≤(9/8)16^(−A)<16^(−5J_A)≤σ_(J_A).                (C4)

Therefore it preserves **every exact integer carry through J_A**, a memory
prefix growing linearly with A, while its unwrapped prefix error is at most
`(9/8)16^(J_A−A)→0`. It still matches all prescribed prime principal parts and
2-adic bits, and retains the prior coherent-epoch signed lower bound. PE9/PE14
therefore imply, for every fixed nonzero h,

    local_prime_mean_A→0,    Cov_A(shadow)→1.              (C5)

This is one different seed for each epoch, not a fixed nonnormal rational seed.
Every seed is nonzero and introduces new denominator support in this particular
AR construction. Exact zero or complete chronological support rejects it.
The result strengthens fixed-prefix memory to a specified growing prefix; it
does not prove that every conceivable growing memory schedule is inadequate.

The construction also has modest description cost. For P consisting of all odd
primes through 8B, `2 product(P)≤2 L(8B)≤2·4^(8B)`. The AR denominator obeys
q<ceil(2^(K_A)16^B/eta)+2 product(P). Thus its binary length is O(B+K_A) for
fixed eta, despite matching every listed local coordinate. With K_A=2A, a fixed
program and the integer A describe the construction in O(log A) input bits.
This is a statement about a concrete algorithm, not an unproved incompressibility
claim or a time-complexity bound. Small program description does not force small
bilinear covariance.

## C3. Sharp precision-versus-horizon tradeoff

Assume the same known affine forcing but an unknown real seed. At each observed
time n≤J, an unwrapped readout reports the authentic value with permitted absolute
error ρ_n>0. With arbitrary bounded errors, the common-transcript seed fiber is

    |s|≤R_J,    R_J=min_(n≤J) ρ_n16^(−n).

At time T≥J the minimax worst-case error of any estimator based on this entire
transcript is **exactly** `16^T R_J`. The center estimator attains it; the two
endpoint seeds yield states separated by twice that amount, proving necessity.
The conclusion holds over rational seeds as well when the bounds are rational;
over dense rational fibers the same supremum applies more generally. If only
circle output is requested, the exact minimax radius is

    min(16^T R_J, 1/2),

because the possible output phases form a circular arc until they cover the
circle. Unlimited storage of the same reports cannot shrink this fiber.
For one time-J measurement of accuracy ρ, the lifted future error is
`16^(T−J)ρ`: the exponential loss is exact, not just an upper conditioning bound.
Supplying an exact seed tag, a sharp rational height bound as in C1, or another
genuinely distinguishing measurement changes the fiber and invalidates this
countermodel. This is not a claim that the already-authenticated source is
mathematically uncertain.

## C4. Both marginals zero, finite support, and perfect predictability still fail

This is an explicit **changed-forcing** control with literal zero boundary.
Fix distinct odd primes p,q and put t=n mod pq. Define

    z_n=floor(t/q)/p−floor(t/p)/q,
    r̃(n)=z_n−16z_(n−1),    Ũ_0=z_0=0.

Then Ũ_n=z_n exactly. It is a perfectly predictable period-pq finite-state
source with denominator support contained in {p,q}; the forcing has the same
support. Its true canonical p-principal part is floor(t/q)/p. Therefore

    a_n=e(floor(t/q)/p),    b_n=e(−floor(t/p)/q)

are exactly the principal and complementary real characters. Over every full
period, each p-th root occurs q times in a and each q-th root occurs p times
in b. Both means are **exactly zero**, while Cov(a,b)=E e(z_n).

Since `pq z_n=(t mod p)−(t mod q)`, the Chinese remainder theorem gives

    E z_n²=(2p²+2q²−3pq−1)/(6p²q²).                      (C6)

This follows by adding the two uniform residue variances and the squared
difference of their means. Using cos(2πx)≥1−2π²x² and π²<10,

    Re Cov(a,b)≥1−20(2p²+2q²−3pq−1)/(6p²q²).             (C7)

For p=3,q=5 this is 91/135; for p=13,q=17 it is 48001/48841>0.9828. For primes
both tending to infinity the bound tends to one. For each fixed pair, all-time
averages tend to their periodic means, so this is a fixed-source asymptotic
counterexample to the general implication, not merely an epochwise array.
It has constant finite support, finite-state causal prediction, exact zero
initial value, and a short explicit description. Those hypotheses do not imply
decorrelation. The source is not the original four-pole forcing, and the oracle
explicitly rejects it at n=1. No counterexample to π normality is claimed.

This model also distinguishes marginal cancellation from conditional structure:
the two factors almost cancel their phases pointwise. The bilinear covariance
keeps that relation; replacing it by independent marginals loses it.

## PE9/PE14 and numerical-instrument audit

No substantive defect was found in PE9 or PE14 under their stated assumptions.
The audit independently checked the first/second pole chronology, complete
multiplicative cycles, the elementary bad-order count, fixed-epsilon PNT/AP
coverage, exact interval-overlap weight, and the complex convergence step in
PE14. The primary Bourgain–Konyagin PDF was re-opened and printed Theorem 2.1
on page 78 checked: the normalized subgroup estimate used in PE9 is supported.
[Primary paper](https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf).
Neither an effective epoch threshold nor a numerical gamma is thereby supplied.

The root interval/source implementation was checked separately. `instrument_audit.py`
uses independent non-quadrant rational Taylor evaluation and a separately rounded
Machin enclosure. Its narrow intervals must be **contained** in the root boxes.
The source tests include unreduced denominators, negative numerators and prime
powers. The final JSON records exact audited file hashes. This is calibration
plus source inspection, not a formal proof of the program.

The sparse spectral probe is also sound under its finite experiment contract:
normalized DFT gives W=Σ ahat_k bhat_(−k). The sum of the largest s upper energy
endpoints bounds maximum capturable energy from above, while the sum of the
largest s lower endpoints bounds it below. Subtracting these in the opposite
directions from the norm enclosure gives the valid best-s residual enclosure,
even when interval uncertainty leaves the coefficient ordering unresolved.

**Remaining gap:** prove the original, literal-zero complementary covariance
tends to zero. None of these identification, precision, support, prediction or
local-marginal facts supplies that estimate. π base-16 normality and RH are OPEN.
