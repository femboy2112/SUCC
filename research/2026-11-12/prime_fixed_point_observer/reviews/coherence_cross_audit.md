# Cross-audit: arithmetic coherent sectors and source semantics

Scope: [ARITHMETIC_COHERENCE.md](../ARITHMETIC_COHERENCE.md), AC-02,
AC-05, AC-06 and AC-07, inspected against the unchanged
`twin_transport.py` fresh-record definition and the original recentering
in [COMMON_ROOT_AND_LIMITS.md](../COMMON_ROOT_AND_LIMITS.md), Section 1.
The audit was performed by a separate same-model agent. It is an
independent implementation and derivation, not external peer review or
independent source provenance. No imported or earlier implementation was
modified by this audit.

## Verdict

The four statements survive within their declared domains. I found no
algebraic defect in their proofs. The necessary qualification is the
separation between preserving a deliberately encoded logical space and
intertwining an authentic arithmetic observable. The explicit prime
projection control below quantifies that qualification.

### AC-02: exact record sectors

At a proposed prefix multiplier `a/b` in lowest terms, the prior accepted
conditions ensure `ak/b` is an integer. Then acceptance is exactly
`bq | ak`, hence `bq/gcd(a,q) | k`, since `gcd(a,b)=1`. This remains
valid when later requirements make the proposed sector empty; the
induction is conditional on satisfying the prefix.

The least positive candidate `A`, the lcm of all accepted moduli, proves
the stated emptiness criterion in both directions. If a rejected modulus
divides `A`, it divides every accepted multiple. If none does, `A` itself
satisfies every accepted and rejected condition. No density assumption,
coprime-modulus CRT claim, or least-period claim is being inserted.

### AC-05: the general common-range encoding and its converse

The crucial cross term is indeed zero:
`K_g K_h^*=K_g P_g P_h K_h^*=0` for `g!=h`. Overlap of their **output**
ranges does not invalidate this identity; the adjacent projections are
onto their disjoint **input** record sectors. On the common output space,
`K_h K_h^*=Q_h` is identity whenever its coefficient is nonzero. This
proves isometry and the displayed fixed-record factorization.

For the converse, the isometric-channel hypothesis supplies a specified
isometry `V`, so each pure marginal factors with the same chosen system
vector `Vu`. Applying this to sums of orthogonal inputs forces the same
environment vector, including its relative phase. The one-dimensional
case is immediate. Boundedness and continuity cover infinite closed
codes; the environment has only finitely many record coordinates at a
finite horizon. Finally `sum_h K_h^*K_h=I` reconstructs the input as
`J_c Vu`, and `V(C)` is closed. This proves completeness for uncorrected
isometric channels. It does not classify all CPTP-correctable codes.

### AC-06 and AC-07: intermediate domains survive ratio cancellation

Every prefix must be integral. Coprimality of each proper pair is what
makes prefix integrality equivalent to actual local acceptance. The lcm
of reduced prefix denominators is therefore exact. It cannot be replaced
by either the reduced final denominator or the product of the local
denominators; the two orderings of `(2,1)` and `(3,2)` are valid opposing
controls.

For the infinite-route statement, run the finite prefix from its least
positive all-success label `L_N`. Each proper step decreases a positive
integer by at least one and the last label `M_N` is positive. Thus
`L_N-M_N>=N` is valid without uniform bounds on the parameters. Together
with lcm monotonicity, it proves the fixed all-success intersection is
exactly the root line. The asserted strong limit and norm-one witness
follow from the exact partial-isometry product. The note correctly keeps
this separate from indefinitely coherent rejection sectors and from
encodings that change with the chosen finite horizon.

## Explicit reference check and pure erasure

The code vectors `c_1=(3 epsilon_3+4 epsilon_2)/5` and
`c_2=(3 epsilon_6+4 epsilon_4)/5` are orthonormal. Applying the literal
single `(3,2)` branch operation to the unnormalized reference state
`c_1 tensor |0>_R+c_2 tensor |1>_R` gives exactly

\[
 (\varepsilon_2|0\rangle_R+\varepsilon_4|1\rangle_R)
 \otimes(3|0\rangle+4|1\rangle)/5.
\]

Dividing the density by two normalizes the maximally entangled input.
The present arithmetic/reference density is the corresponding rank-one
projector and has purity one. This checks reference preservation directly,
without relying on an uncorrelated-state test or the other implementation.

In contrast, the reference state
`epsilon_2 tensor |0>_R+epsilon_3 tensor |1>_R` becomes
`epsilon_2 tensor (|0>_R|1>_record+|1>_R|0>_record)`.
After tracing the record and dividing by two, the joint current density is
`|epsilon_2><epsilon_2| tensor I_R/2`. Its purity is `1/2`; the arithmetic
marginal is pure but the logical information resides in the record.

## Source-semantic countercontrol: the code does not intertwine primality

The source convention is load-bearing:
`e_(k+1) -> epsilon_k`. Thus the authentic prime projection in centered
coordinates is

\[
 \widehat P_{\rm prime}\varepsilon_k
 =\mathbf1_{k+1\text{ prime}}\varepsilon_k.
\]

The first code vector mixes original source labels 4 and 3; the second
mixes original source labels 7 and 5. With `J|j>=c_j` and
`V|1>=epsilon_2`, `V|2>=epsilon_4`, direct exact calculation gives

\[
 \boxed{
 J^*\widehat P_{\rm prime}J
 =\begin{pmatrix}16/25&0\\0&1\end{pmatrix},\qquad
 V^*\widehat P_{\rm prime}V=I_2.}
\]

The first diagonal discrepancy is `9/25`. The coherent encoding theorem
remains true: the chosen **logical** coordinate survives exactly. The
unmodified authentic prime projection is not the same logical observable
before and after this encoding. Replacing primality of `k+1` by primality
of `k` would silently change the source. One may transport a chosen
observable to the output, but that transport and the resulting arithmetic
meaning must be stated; preservation of the code does not supply a new
prime-pair estimate.

## Actual checks and reproducibility

An independent standard-library probe, importing neither arithmetic probe
nor `twin_transport`, completed **107,153 exact assertions, exit 0**.
It checked 88 schedules: every length-0 through length-3 schedule over
`(2,1),(3,2),(5,2),(7,5)`, and three longer schedules with parameters up
to 101. Basis regions included `0..128`, source-selected multiples of
each prefix lcm, and the fixed labels 997, 1009 and 104729. It checked
every proposed record on `0..96`, the emptiness test, direct backwards
reconstruction, the reference factorization, and pure erasure. These
finite checks calibrate the formulas; the written proofs supply the
universal statements.

Observed group counts:

```json
{"code_orthonormal":3,"joint_inverse":23760,"prefix_admission":11880,
 "prefix_descent":88,"prefix_integer":88,"prefix_output":1174,
 "pure_erasure_reference":2,"reference_current_density":1,
 "reference_current_purity":1,"reference_factorization":1,
 "reverse_integrality":8905,"sector_emptiness":625,
 "sector_membership":60625}
```

The source-prime discrepancy was verified separately by three exact
assertions; it is not included in the 107,153 count. The complete saved
[independent probe](coherence_cross_probe.py) combines those two already
executed sets. Its final replay passed **107,156 assertions, exit 0**, as
recorded in [COHERENCE_CROSS_REPORT.json](../receipts/COHERENCE_CROSS_REPORT.json).
No test region was added in that packaging replay. It also pins the probe
and inspected source hashes. Reproduce from the repository root with:

```bash
python research/2026-11-12/prime_fixed_point_observer/reviews/coherence_cross_probe.py
```

The following compact replay reproduces the schedule/sector portion using
literal integer paths:

```python
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm

def walk(seq, k):
    x, flags, ok = k, [], True
    for q, r in seq:
        if x % q:
            flags.append(1)
            ok = False
        else:
            flags.append(0)
            x = x // q * r
    return tuple(flags), x, ok

def cell(seq, h):
    a = b = 1
    yes, no = [], []
    for (q, r), bit in zip(seq, h):
        s = b * q // gcd(a, q)
        if bit:
            no.append(s)
        else:
            yes.append(s)
            a, b = a * r, b * q
            g = gcd(a, b)
            a, b = a // g, b // g
    return lcm(*yes) if yes else 1, no

pairs = ((2,1), (3,2), (5,2), (7,5))
seqs = [s for n in range(4) for s in product(pairs, repeat=n)]
seqs += [((11,7),(13,5),(17,3),(19,11)),
         ((101,97),(97,89),(89,83)),
         ((29,17),(43,31),(17,3),(31,2))]
for seq in seqs:
    ratio, L = F(1), 1
    for q, r in seq:
        ratio *= F(r, q)
        L = lcm(L, ratio.denominator)
    M = ratio * L
    assert M.denominator == 1 and L - M >= len(seq)
    for k in list(range(129)) + [L,2*L,3*L,997,1009,104729]:
        h, f, ok = walk(seq, k)
        assert ok == (k % L == 0)
        if ok:
            assert f == M * (k // L)
        x = f
        for (q, r), bit in reversed(tuple(zip(seq, h))):
            if not bit:
                assert x % r == 0
                x = x // r * q
        assert x == k
    for h in product((0,1), repeat=len(seq)):
        A, no = cell(seq, h)
        assert (walk(seq,A)[0] != h) == any(A % s == 0 for s in no)
        for k in range(97):
            assert (k % A == 0 and all(k % s for s in no)) == (walk(seq,k)[0] == h)
print("88 schedule and sector families PASS")
```

The independent reference calculation is the coefficient expansion given
above and uses only fractions `3/5`, `4/5` and normalization `1/2` at the
density level. No numerical tolerance or floating-point eigenvalue test is
involved. The channel-construction note was also clarified to require a
fixed input-independent initial mixed carrier, or a known encoding already
included in its declared isometry `W`; arbitrary pre-existing input/carrier
correlations do not automatically define a single channel on all inputs.
That was a prose correction only: the separate coherent-channel receipt
remains 696 exact passing assertions on unchanged code.
