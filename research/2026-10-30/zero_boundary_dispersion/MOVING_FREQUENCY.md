# Two different source-forcing frequency thresholds

**PROVED LOCAL, paper.** These estimates preserve the authentic four poles.
They apply to every real seed, including zero, and therefore supply no new
fixed-frequency selected-boundary theorem. Their purpose is a nontrivial
signed bound in an explicit moving-frequency regime, and a sharp warning
against transferring that result to fixed h. No literature-priority claim.

Use r(k), U_n(s), T_n, D_n and e(t) as in parent403. Write
Q(x)=2(1−exp(−3x))+(1−exp(−4x))+(1−exp(−5x)).

## MF-01: exact two-sided source estimates

For y≥0, y exp(−y)≤1−exp(−y)≤y. Thus
15x exp(−5x)≤Q(x)≤15x. Integrating against
exp(−(8k−7)x), for every k≥1,

    15/(8k−2)² ≤ r(k) ≤ 15/(8k−7)².

Multiplying Q by 1−exp(−8x), the same argument gives

    240/(8k+6)³ ≤ r(k)−r(k+1) ≤ 240/(8k−7)³.

These are genuine all-index inequalities, not fitted asymptotic series.
The upper bounds refine nothing in parent403; the lower bounds enable the
declared bands below. They are consistent with r(k)~15/(64k²).

## MF-02: unit-phase source variance transfer

For any M≥1, A≥0, real seed s and integer h, set

    S = Σ_(n=A)^(A+M) e(h U_n(s)),
    Q_h = Σ_(n=A)^(A+M−1) e(h r(n+1)).

Then

    (M+1) − |S| ≥ (M − |Q_h|)/289.                 (MF2)

Proof: choose a unit ζ with Re(conj(ζ)S)=|S| (arbitrary if S=0).
Let z_n=e(hU_n). The literal recurrence gives
q_n=z_(n+1) conj(z_n)^16. Therefore

    |q_n−ζ^(−15)| ≤ |z_(n+1)−ζ|+16|z_n−ζ|.

The Euclidean triangle inequality over the edges bounds the sum of the
squared left sides by 289 Σ_vertices |z_n−ζ|²
=578[(M+1)−|S|]. Its minimum over a unit target is
2[M−|Q_h|]. This proves MF2. No stochastic independence or seed averaging.
The abstract inequality is generic; the actual BBP application is MF-03.

## MF-03: an explicit fractional signed saving at quadratic frequencies

For every positive integer A divisible by4, every integer h with

    A²/2 ≤ |h| ≤ A²,

and **every real seed s**, the authentic forcing satisfies

    |Σ_(n=A)^(2A) e(hU_n(s))|
       ≤ A+1 − (81/34694450) A.                   (MF3)

Proof: conjugation reduces to h>0. Take M=A source edges n=A,...,2A−1.
In the first quarter n≤5A/4−1, MF-01 gives
r(n+1)≥15/(10A−2)²≥15/(100A²). In the last quarter
n≥7A/4, it gives r(n+1)≤15/(14A+1)²≤15/(196A²).
Consequently each early/late source phase difference belongs to

    [ (15/2)(1/100−1/196), 15/64 ] = [9/245,15/64].

There are (A/4)² unordered such pairs. For ||t||≤1/2,
1−cos(2πt)=2sin²(π||t||)≥8||t||². Put δ=9/245.
For the A unit source phases,

    A²−|Q_h|² = 2 Σ_(i<j) [1−cos(2πh(r(i+1)−r(j+1)))]
               ≥ 2(A/4)²·8δ² = A²δ².

Thus A−|Q_h|≥Aδ²/2. MF2 yields Aδ²/578,
which is exactly 81A/34694450. Every inequality is explicit, including
the smallest A=4. No π irrationality input is needed.

### MF-03B: a wider high-frequency band with a larger saving

For every integer A≥2 and 1≤|h|≤A³, there is also the explicit bound

    |Q_h| ≤ min(A, 256 A³/(15|h|)).

Consequently, whenever 512A²/15≤|h|≤A³ (a nonempty band for A≥35),

    |Σ_(n=A)^(2A) e(hU_n(s))| ≤ A+1−A/578.

Here is a complete elementary first-difference estimate. If unit phases
z_j=e(f_j) have monotone increments Δ_j=f_(j+1)−f_j in
[λ,1−λ], 0<λ≤1/2, put
a_j=(1−e(Δ_j))^(−1)=1/2+(i/2)cot(πΔ_j).
Summation by parts gives

    Σ_(j=0)^(M−1) z_j = a_0 z_0+(1−a_(M−2))z_(M−1)
                         +Σ_(j=1)^(M−2)(a_j−a_(j−1))z_j.

The endpoint norms sum to at most csc(πλ); monotonicity bounds the interior
variation by cot(πλ). Their total is at most2/sin(πλ)≤1/λ.
The one-term case is automatic. For BBP conjugate if necessary so that
Δ_j=|h|[r(n+1)−r(n+2)] is positive. The positive Laplace representation
shows these increments are decreasing. MF-01 puts them in
[λ,15/32] with λ=15|h|/(256A³)≤15/256; in particular they lie in
[λ,1−λ]. The preceding bound followed by MF2 proves the claim.
This is the elementary monotone-phase estimate applied to the actual forcing;
it is not a bound for the prime-primary character alone.

## MF-04: cubic frequencies force a fractional lag-energy floor

For every integer A≥2 and integer A³/2≤|h|≤A³,

    Σ_(n=A)^(2A−1) [1−Re e(h(U_(n+1)(s)−U_n(s)))]
       ≥ (A−1)·225/(32768·289)                  (MF4)

for every real s. Indeed MF-01 for k=n+1 gives, on the A−1 source
differences n=A,...,2A−2,

    15/512 ≤ |h|[r(n+1)−r(n+2)] ≤ 15/32 <1/2.

Apply the inherited SG-02 chord inequality with factor1/289 and
1−cos(2πt)≥8||t||². The constant is 8(15/512)²/289.
Parent403's variance inequality additionally gives a signed saving equal
to one fourth of this lag-energy bound. MF3 reaches a lower frequency scale.

## MF-05: sharp scale obstructions and typed controls

At the coherent same-forcing seed s*=−π/16, U_n=−T_n. Since
T_n<(8n+1)^(−2), if |h_A|=o(A²),

    (1/(A+1)) Σ_(n=A)^(2A) e(h_A U_n(s*)) → 1.

Thus a seed-uniform constant fractional saving cannot extend below the
quadratic scale. Similarly D_n≤16/(8n+1)³ implies the coherent mean lag
energy tends0 whenever |h_A|=o(A³); cubic is the corresponding lag scale.
These are different observables, so there is no contradiction between MF3
and MF4. At fixed h the same seed has summable lag energy.

The authentic zero boundary satisfies MF3/MF4 because *all* real seeds do.
Rational translations and exact/eventual circle aliases legitimately pass.
Zero forcing fails the source lower bounds and can remain exactly coherent.
Positive age/jet-matched mutants with the same leading decay can also have
quadratic/cubic thresholds (with recalibrated constants). These estimates
cannot authenticate the original coefficients or imply normality. They use
the original forcing's real variation, not a signed CRT interaction.

The missing fixed-frequency SC-06 bound is unchanged: replacing h~A² or
h~A³ by fixed h makes the available source-side phase variation vanish.

## Calibration and independent route

`moving_frequency.py` evaluates exact source/prefix fractions, exact circle
distances and rational lower bounds for phase variance. `moving_oracle.py`
uses separately unrolled prefixes and a symbolic integral decomposition.
`test_moving_frequency.py` checks the preregistered bands, hostile zero-source
control, source mutants, coherent Green enclosures and exact rational aliases.
Neither finite probe is the authority for the unbounded statements above.
