# Gamma–prime attack: an ordered boundary response and the full pole-gap ceiling

Status: paper derivations, with the exact finite checks recorded below. No new
signed statistical saving, R0 proof, normality proof, external refereeing, or
worldwide novelty claim is made. The source is the literal four-pole recurrence
with `U_0=0`. The parent inspected was Main XXV
`db9fb4b84672050efa79b13377f1e73364598a14`.

## 1. What the archive already supplies

The useful genealogy is not “Gamma implies randomness.” It is the following
sequence of proved, typed maps.

| Archival object | Actual map/result | First unpaid arithmetic step |
|---|---|---|
| October 25 MGB-06 | A Gamma quotient has successor logarithmic derivative `8r(n)` | Its ordinary tail is not the discounted BBP Green tail |
| November 4 GP-04 | The corrected Gamma interval and the newborn-prime coset uniquely pin each original forcing injection | The accumulated state's cofactor is exponentially larger than the forcing cofactor |
| November 4 PF-03–05 | Frobenius pulse transport reproduces original/dual rational BBP sources; `log den(U_N)~6N` | A large denominator gives no useful centered real numerator bound |
| November 4 PCQ-06–07 | The angular quotient differs from the original by `O(1/N)`, preserves fixed-mode statistical gates, and has conductor exponent 8 | Real closeness and prime complexity do not supply chronological cancellation |
| November 4 Prybar front 1 | Same-forcing rational seed fibers preserve complete denominator data and can be coherent; their averaged behavior is good | A virtual or seed average does not select the authentic zero fiber |
| November 4 Prybar front 5 | Every sufficiently late pair has a large reduced difference denominator; the best displayed uniform coefficient is `79/14-log(4)` | Its centered numerator remains uncontrolled |

The precise files are:

- `research/2026-10-25/MOBIUS_GAMMA_BOUNDARY_REPORT.md`, MGB-06 and MGB-15.
- `research/2026-11-04/gamma_pigeonhole/PROOFS.md`, GP-04–06.
- `research/2026-11-04/frobenius_prime_saturation/PROOFS.md`, PF-01–06.
- `research/2026-11-04/prime_character_primal/PROOFS.md`, PCQ-06–07.
- `research/2026-11-04/gamma_prybar/front1/COFACTOR_PROOFS.md`.
- `research/2026-11-04/gamma_prybar/front5/front5_proofs.md`.

These are all present at the inspected parent. The latest-prime-residue/
old-cofactor distinction is already explicit there; it is not newly discovered
in this round.

## 2. One ordered Gamma boundary response retains source, seed and chronology

For `Re z > -1/8`, choose the analytic logarithms agreeing with the real
logarithm on the positive real factors, and put

\[
H(z)=\frac{\Gamma(z+1/8)^4}
 {\Gamma(z+1/2)^2\Gamma(z+5/8)\Gamma(z+3/4)},\qquad
f(z)=\frac{H(z+1)}{H(z)}
=\frac{(z+1/8)^4}{(z+1/2)^2(z+5/8)(z+3/4)}.
\]

The Gamma recurrence is a classical input (NIST DLMF 5.5.1); the source
identification is inherited MGB-06. Direct differentiation gives

\[
\frac18(\log f)'(z+j-1)=r(z+j).
\]

Define the chronological response

\[
R_{N,s}(z)=e^{8\,16^Nsz}
\prod_{j=1}^{N}f(z+j-1)^{16^{N-j}},\qquad R_{0,s}(z)=e^{8sz}.
\tag{GP-A}
\]

Then, exactly,

\[
R_{N,s}=R_{N-1,s}^{16}f(z+N-1),\qquad
\frac18(\log R_{N,s})'(0)=16^Ns+U_N(0)=U_N(s).
\tag{GP-B}
\]

The initial factor `R_{0,0}=1` is the literal zero authentication. The weights
`16^(N-j)` retain chronology: an unordered product of the injections would
discard those weights. The product also has the exact Gamma-boundary form

\[
R_{N,0}(z)=
\frac{H(z+N)\prod_{k=1}^{N-1}H(z+k)^{15\,16^{N-k-1}}}
 {H(z)^{16^{N-1}}}.
\tag{GP-C}
\]

This follows by collecting the coefficient of each `log H(z+k)`. It is a
reconstruction identity, not a cancellation theorem.

The normalized analytic boundary is

\[
Q_s(z)=\exp\!\left(8sz+
\sum_{j=1}^{\infty}16^{-j}\log f(z+j-1)\right).
\tag{GP-D}
\]

The series and its derivative converge locally uniformly in the displayed
half-plane, since `log f(z+j-1)=O_K(1/j)` on every compact set `K`.
Consequently

\[
\frac18(\log Q_s)'(0)=s+x,\qquad x=\pi/16.
\tag{GP-E}
\]

For real `z>=0`, the discounted derivative error is bounded explicitly:

\[
0<\frac18(\log Q_0)'(z)
 -\frac{16^{-N}}8(\log R_{N,0})'(z)
<\frac{16^{-N}r(z+N+1)}{15}.
\tag{GP-F}
\]

For a proof of positivity/monotonicity, directly integrate the original source:

\[
r(z+j)=\int_0^1 t^{8(z+j-1)}
(1-t)(4+4t+4t^2+2t^3+t^4)\,dt.
\]

This is positive and decreasing in `z+j`; bound the omitted terms by their
first value and sum the geometric weights. At `z=0`, multiplication by
`16^N` recovers precisely the already authenticated Green tail. Thus this
transform pays its error instead of introducing a new phase port.

### An exact hidden factor, and its limited meaning

For any real seeds `s,t`,

\[
R_{N,s}/R_{N,t}=e^{8\,16^N(s-t)z},\qquad
Q_s/Q_t=e^{8(s-t)z}.
\tag{GP-G}
\]

The finite responses therefore have identical meromorphic divisors and identical
principal parts of their logarithmic derivatives at every finite pole. All
derivatives of order at least two of `log R` and `log Q` are seed-blind. The
missing information is a zero-free exponential factor, equivalently the constant
term of the logarithmic derivative. For `s=-x`, (GP-E) is zero and the completed
orbit is identically zero. For `s=0`, it is `x`.

This is an exact obstruction to **pole/principal-part data alone** selecting the
phase dynamics. It does not say that full boundary values, growth normalization,
the original seed, or the first logarithmic derivative cannot distinguish them.
They can. It also does not turn the authenticated value `x` into a statistical
estimate for its radix orbit. The general seed blindness is inherited; (GP-A–G)
put it into one explicit ordered Gamma response.

The four-pole cancellation `4-2-1-1=0` removes the leading `1/n` term of the
forcing, leaving `r(n)~15/(64n^2)`. It also cancels the common additive Euler
constant in the balanced digamma derivative. These facts give a summable
transport error. They do not make the exponential phase sum signed-cancel.

## 3. A stronger ratio-dependent arithmetic inequality, and an exact ceiling

This is the actual additional arithmetic lemma of this note. It extends the
four retained no-injection prime bands in Prybar front 5 to **every** such band,
and determines the optimum of that entire band-counting method. Its conclusion
is about reduced denominators, not R0.

Let the increasing sequences of possible original pulse multipliers be

\[
\mathcal M_+=\{8k+1,8k+4,8k+5,8k+6:k\ge0\},\qquad
\mathcal M_-=\{8k+2,8k+3,8k+4,8k+7:k\ge0\}.
\]

They apply respectively to primes `p=1 mod 4` and `p=3 mod 4`, as proved by
the exact four original denominator offsets (PF-01). Let `G_+` and `G_-`
be the consecutive pairs `(a,b)` in these sequences. Define, for `0<x<=1`,

\[
\mathcal C(x)=(6-\log16)x+
4\sum_{(a,b)\in G_+\cup G_-}
\left(\frac1a-\frac{1+x}{b}\right)_+.
\tag{GP-H}
\]

Every pulse gap is at most 3. A term can be positive only if `a<3/x`, so
this is a finite sum at every positive `x`.

**Theorem GP-1.** For any sequence of integer pairs `n<t<=2n` with
`n->infinity` and `(t-n)/n->x` for a fixed `0<x<=1`,

\[
\liminf \frac{\log\operatorname{den}(U_t-U_n)}n\ge\mathcal C(x).
\tag{GP-I}
\]

The estimate is locally uniform for `x` in compact subintervals of `(0,1]`.
It uses the existing PF-05 macroscopic prime survival theorem and classical
PNT in the fixed progressions modulo 4. It supplies no effective numerical
onset, just as those inputs do not supply one here.

**Proof.** Write `d=t-n`. Fresh split primes in `(8n,8t-O(1)]` and fresh
inert primes in `(4n,4t-O(1)]` were absent at `n` and survive at `t` by PF-05.
They contribute `6d+o(n)` to the log denominator of the difference.

For each consecutive pair `(a,b)` in one of the two pulse sequences, primes
in the corresponding progression and in

\[
8t/b+O(1)<p\le8n/a-O(1)
\]

have already received pulse `a` by `n` and do not receive the next pulse `b`
until after `t`. Retain only intervals of positive limiting length. There are
finitely many at fixed `x`, and all their primes are `p>>n`, so PF-05 says
`pU_n mod p` is nonzero for sufficiently large `n`. The recurrence yields

\[
p(U_t-U_n)\equiv(16^d-1)pU_n\pmod p.
\]

Thus such a prime survives unless it divides the **single** integer `16^d-1`.
All bands in one progression are disjoint, and the two progressions are
disjoint. Fresh bands are disjoint from these old-prime bands. PNT-AP gives
their total pre-exclusion mass

\[
4\sum_{(a,b)}(n/a-t/b)_++o(n).
\]

The product of the distinct excluded primes divides `16^d-1`, costing at most
`d log16` across the entire collection, not once per band. Combining the fresh
and inherited masses proves (GP-I). Bounded endpoint offsets cost `O(log n)`
per band. Uniform PNT errors on fixed macroscopic intervals and the finite
number of relevant bands prove the local uniformity assertion. QED.

**Corollary GP-1+ (root-agent strengthening).** Fresh primes survive independently
of the estimate for inherited primes. The inherited contribution is nonnegative,
even when the crude `d log16` subtraction exceeds its pre-exclusion mass. Thus
(GP-I) remains valid with the stronger envelope

\[
\mathcal C_+(x)=6x+\max\left\{
4\sum_{(a,b)\in G_+\cup G_-}
\left(\frac1a-\frac{1+x}{b}\right)_+-x\log16,\ 0\right\}.
\tag{GP-I+}
\]

This improvement was supplied by the coordinating root agent after the original
derivation: retain the fresh contribution and truncate only the inherited lower
bound at zero. For `x=1`, it gives coefficient 6, compared with `8-log16` in
(GP-I). At `x=1/4` and `x=1/2` the inherited bracket is positive and the two
envelopes agree. No estimate of the centered real numerator follows.

**Concrete improvement.** For `t/n->5/4`, the full envelope gives

\[
\liminf\frac{\log\operatorname{den}(U_t-U_n)}n
\ge\frac{1301}{252}-\log2.
\tag{GP-J}
\]

The earlier four-band expression at that ratio is
`1255/252-log2`. The gain is exactly `23/126` in the coefficient of `n`.
For `t/n->4/3`, the gain is `4/105`. These are improvements to particular
macroscopic-lag denominator bounds; they do not improve the uniform-in-lag
constant and have no asserted real-spacing consequence at logarithmic mesh.

**Theorem GP-2 (exact method ceiling).** The complete expression (GP-H)
satisfies

\[
\inf_{0<x\le1}\mathcal C(x)=\mathcal C(1/2)
=\frac{79}{14}-\log4.
\tag{GP-K}
\]

**Proof.** Keep only the four gaps `(1,4),(2,3),(6,9),(4,7)`. Their expression
is precisely the convex piecewise-linear lower envelope already used in
Prybar front 5. At `x=1/2`, its left slope is

`6-log16-1-4/3-4/9-4/7 < 0`,

and its right slope is `6-log16-1-4/7 > 0`. It therefore has its global
minimum at `x=1/2`, with value `79/14-log4`. Adding the other nonnegative
terms cannot lower that minimum. At `x=1/2`, positivity of a term requires
`b>3a/2`. Since `b-a<=3`, this requires `a<6`. Directly listing the two
sequences below 6 leaves exactly `(1,4)` and `(4,7)` positive; all extra
terms vanish. Equality follows. QED.

The ceiling concerns this precisely declared use of all source no-injection
bands and the common `16^d-1` loss. It is **not** an upper bound on the true
difference conductor, nor a no-go theorem for new arithmetic. The next
improvement must exploit injection-containing intervals, the arithmetic of the
exceptional divisor `16^d-1`, or a new centered-residue fact. Merely adding
more of the omitted no-injection bands cannot improve the existing worst-lag
constant.

The strengthened envelope has the same minimum: `C_+>=C`, and equality holds
at `x=1/2` because the inherited bracket there is
`37/14-log4>0`. Thus (GP-K) holds with `C_+` as well.

### A tested escape from the ceiling: factoring the common loss

The root agent proposed using `16^d-1=(4^d-1)(4^d+1)` and the fact that an
inert prime `p=3 mod4` cannot divide `4^d+1`: such a divisor would make
`(2^d)^2=-1 mod p`. This restriction is valid, but the corresponding capacity
calculation does **not** improve the minimizing ratio. At `x=1/2`, the surviving
candidate bands before divisor exclusion have masses

| Band | Prime class | Pre-exclusion log mass |
|---|---|---:|
| `(3n,8n]` | `1 mod4` | `(5/2)n+o(n)` |
| `(12n/7,2n]` | `3 mod4` | `n/7+o(n)` |

Both factors `4^d-1` and `4^d+1` have logarithmic capacity
`d log4=(log2)n+o(n)`. Their combined capacity is less than the split-band
mass, since `2 log2<5/2`. A feasible worst-case allocation assigns the full
capacity of both factors entirely to the split band and zero loss to the inert
band. It respects the extra residue restriction and still spends the complete
`d log16` budget. Even the stronger hypothesis that **no** inert prime is lost
would not improve this particular total-loss estimate at its minimum.

This is a feasible allocation of bounds, not a claim that the authentic divisor
sets actually realize it. To improve the theorem through this factorization,
one needs a new arithmetic upper bound on the split primes in `(3n,8n]` dividing
`4^d-1` or `4^d+1`, or on their combined logarithmic mass. The residue-class
fact alone supplies no such upper bound. Higher 2-adic factorization can further
restrict inert losses but leaves this all-split allocation available.

## 4. What would pay the remaining debt

The Gamma response retains everything, but its first logarithmic derivative
still produces the actual selected `U_n`. An estimate for it is needed.
A legitimate prime-window proposal must control the **combined** character

\[
e\left(4h16^j/p\right)e(h\beta_{p,j}),
\]

where `beta` is the actual accumulated complementary rational state. Neither
factor may be resampled. At early post-birth times, the forcing itself already
creates substantial cancellation between its `4/p` term and its cofactor; an
assumption that the cofactor is slowly varying or independent would discard
the phenomenon one is trying to study.

No such nonfactorizing all-scale inequality was proved in this pass. A theorem
claiming R0 from the Gamma divisor plus the conductor envelope is killed by
the same-forcing coherent seed and by the exact denominator-preserving
rational seed fibers already constructed in Prybar front 1. They are auxiliary
wrong-seed systems, not source-authenticated counterexamples to pi.

The strongest surviving direction is therefore a **signed old-cofactor /
zero-boundary correlation estimate**, not additional denominator growth.
Its numerical diagnosis must freeze the full cofactor and integer lift, compare
the original zero selector against coherent rational seed controls, and use
fresh shells. A good finite result alone cannot give the all-shell quantifier.

## 5. Preregistered finite verification and claim ledger

Before the checks below: verify `(log f)'/8` against the four partial fractions
symbolically; verify the weighted logarithmic derivative for horizons 1–7;
verify the seed derivative and all second-derivative blindness symbolically;
enumerate all pulse gaps relevant to `x=1/4,1/3,3/7,1/2,3/4,1`; check the
stated rational coefficients and the exact active-pair list at `x=1/2`.
The wrong first pole coefficient must fail the source identity. These tests
are algebraic checks, not a numerical R0 experiment or asymptotic proof.

| Claim | Authority | Boundary |
|---|---|---|
| GP-A–G | Exact algebra and locally uniform analytic convergence; Gamma primitive inherited | Reconstruction and an explicit seed-blind class of instruments |
| GP-1 / GP-1+ / GP-J | Paper derivation from PF-05 and classical fixed-modulus PNT | Improved ratio-dependent conductor lower bound, no signed saving |
| GP-2 | Elementary exact convex-envelope proof | Optimum of one declared arithmetic method only |
| Any implication to R0 | OPEN / NOT CLAIMED | Requires a source-selected centered-residue inequality |

External reference for the Gamma recurrence:
<https://dlmf.nist.gov/5.5.E1>. The fixed-modulus PNT-AP input and its scope
are inherited explicitly from PF-05; ordinary PNT alone would not justify
the separate split/inert counts.

Executed finite results: **20 symbolic/envelope check cases PASS** (16 original
and 4 root-strengthening cases) and **751 direct prime-divisibility implications
PASS**. The direct prime checks were additional
non-blind regression checks, not part of the preceding preregistration. The
direct recurrence used exact `fractions.Fraction`, and its pole events were
enumerated from the four raw denominators, independently of the two multiplier
lists. No assertion failed in this run. The prime checks were conditional on
the actual finite nonzero principal part; finite exceptions to PF-05 were not
silently suppressed into an all-prime finite claim.

| `(n,t)` | Fresh-prime checks | Inherited no-injection checks |
|---|---:|---:|
| `(127,158)` | 28 | 76 |
| `(191,254)` | 50 | 89 |
| `(257,385)` | 103 | 93 |
| `(311,622)` | 232 | 80 |

The rational parts of (GP-H), before subtracting `x log16`, were exactly
`1301/252`, `4951/945`, `2405/441`, `79/14`, `27/4`, and `8`, at
`x=1/4,1/3,3/7,1/2,3/4,1`, respectively. Reproduction of the arithmetic part:

```python
from fractions import Fraction as F
from itertools import pairwise
from sympy import primerange

seqs = [[8*k+a for k in range(100) for a in residues]
        for residues in [(1,4,5,6), (2,3,4,7)]]
pairs = [p for seq in seqs for p in pairwise(seq)]
expected = [(F(1,4), F(1301,252)), (F(1,3), F(4951,945)),
            (F(3,7), F(2405,441)), (F(1,2), F(79,14)),
            (F(3,4), F(27,4)), (F(1), F(8))]
for x, wanted in expected:
    value = 6*x + 4*sum(max(F(1,a)-(1+x)/b, 0) for a,b in pairs)
    assert value == wanted
    active = [(a,b) for a,b in pairs if F(1,a) > (1+x)/b]
    assert all(a < 3/x for a,b in active)
    if x == F(1,2):
        assert active == [(1,4), (4,7)]

ends = [(127,158), (191,254), (257,385), (311,622)]
U = [F(0)]
for n in range(1, 623):
    U.append(16*U[-1] + F(4,8*n-7) - F(2,8*n-4)
             - F(1,8*n-3) - F(1,8*n-2))
count = 0
for n,t in ends:
    for p in primerange(7, 8*t):
        if p*p <= 8*t:
            continue
        born = [j for j in range(1,t+1)
                if any((8*j-c) % p == 0 for c in (7,4,3,2))]
        if not born:
            continue
        if born[0] > n and U[t].denominator % p == 0:
            assert (U[t]-U[n]).denominator % p == 0
            count += 1
        elif born[0] <= n and not any(j > n for j in born):
            if U[n].denominator % p == 0 and pow(16,t-n,p) != 1:
                assert (U[t]-U[n]).denominator % p == 0
                count += 1
assert count == 751
```

The symbolic identity was checked using
`cancel(diff(f,z)/(8*f)-r(z+1)) == 0`; changing the first coefficient from
4 to 3 fails that equality. Horizons 1–7 independently collected the weighted
logarithmic derivatives and compared them to the weighted four-pole source.
The seed quotient's first and second logarithmic derivatives were checked
symbolically as well. The executable companion `gamma_prime_probe.py` preserves
these cases and adds four exact checks of which branch of (GP-I+) applies, using
a rational `atanh(1/3)` enclosure for `log2`. Its deterministic receipt is
`GAMMA_RESULTS.json`. Run `python research/2026-11-12/leah_gamma_twist/gamma_prime_probe.py`
to replay and compare the receipt; `--write` intentionally refreshes it.
The default receipt-comparison replay and Python compilation both passed.

No full repository suite is asserted by this subtask; the coordinating agent
owns integration validation.
