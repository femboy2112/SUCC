# Separate proof audit of the gap-sensitive source conductor theorem

**Verdict:** GP-I, its local-uniformity claim, the two displayed coefficient
improvements, and GP-K survive this audit, conditional only on their explicitly
imported classical PNT-AP and the already-proved source survival theorem PF-05.
This is a separate same-model derivation and implementation, not external
refereeing, a Lean proof, or independent empirical evidence for pi normality.
The ordered Gamma response identities also survive direct algebraic review.

Reviewed source: [GAMMA_PRIME.md](GAMMA_PRIME.md), against the preserved
`research/2026-11-04/frobenius_prime_saturation/PROOFS.md` (PF-01--05)
and `research/2026-11-04/gamma_prybar/front5/front5_proofs.md` at parent
`db9fb4b84672050efa79b13377f1e73364598a14`.
The audit was initially blind to the constructor's executable implementation.

## 1. Pulse arithmetic and endpoints

An original injection occurs exactly when `8j-c=mp`, where
`c in {7,4,3,2}` and the coefficients are `{4,-2,-1,-1}`.
Since each odd residue modulo 8 is its own inverse, multiplying the four
allowed denominator residues `{1,4,5,6}` by `p mod 8` gives:

| `p mod 8` | Allowed `m mod 8` |
|---:|---|
| 1 | 1,4,5,6 |
| 5 | 1,4,5,6 |
| 3 | 2,3,4,7 |
| 7 | 2,3,4,7 |

Thus the two multiplier sequences in GP-H are correct; no averaging over
Galois embeddings entered this derivation.
For a consecutive pair `(a,b)`, the robust exact sufficient interval is

\[
 8t<bp,\qquad ap+7\le8n.
\]

The actual offset `c_a<=7` ensures pulse `a` has occurred by `n`; the positive
offset of `b` ensures that pulse occurs after `t`. No intervening source pole
exists. Endpoint adjustments relative to `(8t/b,8n/a]` are bounded in terms of
`a,b`, so cost `O(log n)` in prime logarithmic mass per fixed band.

Two adjacent multiplier gaps cannot double count: the later band's upper
endpoint is at most `8n/b`, strictly below the earlier band's lower endpoint
`8t/b`. The two residue classes modulo 4 are disjoint. Fresh primes lie above
`8n` in the split class or `4n` in the inert class; inherited-band upper
endpoints lie at or below those thresholds. All three disjointness assertions
needed to add the masses are valid.

## 2. Source survival and exceptional loss

For fixed `x>0`, an active band satisfies `b-a<=3` and `b>(1+x)a`, hence
`a<3/x`. There are finitely many. All their primes are at least `c_x n`
for a positive constant `c_x`; eventually `p^2>8t` and every pulse is simple.
PF-05 then supplies `v_p(U_n)=-1` for every such inherited prime at all
sufficiently large `n`. This is a genuine all-large-`n` use of PF-05,
not an inference from the finite checks.

With no injections between `n` and `t`,

\[
 p(U_t-U_n)\equiv(16^{t-n}-1)pU_n\pmod p.
\]

Thus a surviving source prime disappears from the difference denominator
**if and only if** it divides `16^{t-n}-1`. All distinct exceptional primes
across every band form a product dividing that one integer. Their total log
mass is at most `(t-n)log16`, paid once. There is no justification for charging
this loss separately to each band, and the proof correctly does not do so.

The fresh bands are `(8n,8t-7]` for `p=1 mod4` and `(4n,4t-1]` for
`p=3 mod4`. Their primes have no pole at `n`; PF-05 gives a simple pole at
`t` for all sufficiently large `n`. Their mass is `6(t-n)+o(n)`.

## 3. Analytic input and uniformity

The exact imported input is

\[
 \theta(y;4,a)=y/2+o(y),\qquad a=1,3.
\]

For an explicitly read official source, see Andrew Sutherland's
[Oberwolfach prime-gaps lecture, “The prime number theorem in arithmetic progressions”](https://math.mit.edu/~drew/PrimeGapsOberwolfach1.pdf).
It states the weighted theta asymptotic for fixed coprime residue classes.
Only the fixed modulus 4 is used here; there is no claim about growing moduli,
short intervals of sublinear length, or GRH.

On `x in [delta,1]`, all active multipliers satisfy `a<3/delta`; the number
of potential bands is bounded and their endpoints remain fixed positive
multiples of `n`, up to a uniform compact range. The `o(n)` PNT-AP error is
therefore uniform in their endpoints. A band opening or closing at a breakpoint
has the same positive-part formula with an `o(n)` error. PF-05 can be applied
with one lower prime cutoff for the entire compact range. This proves the
stated local uniformity. It gives no uniform claim as `x` approaches zero.

The resulting mass is exactly

\[
 (6-\log16)x+4\sum_{(a,b)}(1/a-(1+x)/b)_+.
\]

Root subsequently observed the elementary strengthening

\[
 6x+\max\{4\sum_{(a,b)}(1/a-(1+x)/b)_+-x\log16,0\}.
\]

It follows by discarding a negative inherited lower bound while retaining the
fresh primes. This improves the endpoint `x=1` from `8-log16` to 6. The
original weaker theorem is valid; the strengthening changes neither the
`x=1/4` gain nor the global minimum at `x=1/2`.

## 4. Coefficients and exact minimum

Independent enumeration from the **raw denominator residues**, rather than
copied multiplier lists, gives rational parts before subtraction of `x log16`:

| x | Rational part |
|---:|---:|
| 1/4 | 1301/252 |
| 1/3 | 4951/945 |
| 3/7 | 2405/441 |
| 1/2 | 79/14 |
| 3/4 | 27/4 |
| 1 | 8 |

At `x=1/4`, subtraction of the four-band value yields `23/126`.
At `x=1/3`, it yields `4/105`.
The four-band function is convex and its slopes on either side of `1/2`
are respectively
`6-log16-1-4/3-4/9-4/7 <0` and `6-log16-1-4/7 >0`.
It therefore has the stated global minimum. Every added band is nonnegative.
At `x=1/2`, positivity requires `b>3a/2`, and `b-a<=3` forces `a<6`.
The only strictly active pairs are `(1,4)` and `(4,7)`; `(2,3)` and `(6,9)`
are at equality. All extra bands vanish. Hence GP-K is exact for the stated
method, including the root's nonnegative-mass strengthening.

This is not an upper bound on the actual source denominator. It is a ceiling
on what this specific lower-bound expression can guarantee in the worst
macroscopic lag.

## 5. Independent exact finite verification

[gamma_independent_audit.py](gamma_independent_audit.py) uses only the standard
library. It builds the original recurrence with **unreduced integer LCM states**,
not the constructor's Fraction recurrence. Pulse multipliers are generated from
`8j-c=mp`; no supplied multiplier list is trusted. Difference denominators are
computed by a final integer gcd. [GAMMA_AUDIT_RESULTS.json](GAMMA_AUDIT_RESULTS.json)
records the exact output.

Completed: 12 source-passport checks, six rational coefficients, 150 exact
piecewise-linear breakpoint comparisons on `[1/100,1]`, and the four separate
prime-divisibility windows below. The logarithm interval for the finite
breakpoint comparison is certified with the positive atanh series for log 2.
The all-`x` minimum remains a paper proof, not an extrapolation of that finite grid.

| `(n,t)` | Fresh survivors | Inherited survivors | Exceptional divisors |
|---|---:|---:|---:|
| (31,39) | 9 | 20 | 0 |
| (83,110) | 23 | 43 | 1 |
| (137,205) | 54 | 51 | 1 |
| (211,422) | 167 | 56 | 0 |

Every actual exceptional prime divided `16^(t-n)-1`; their combined product
divided that integer in each window. Finite source cancellations were counted
separately (none occurred in these selected bands); their absence is not used
to promote PF-05 to an all-prime finite theorem. These were audit holdouts,
not evidence about an asymptotic R0 margin. No assertion failed in this checker.

## 6. Ordered Gamma response review

`(log f)'/8` has exactly the original four coefficients after the shift
`z+j-1`. Collecting the coefficient of each `log H(z+k)` gives GP-C, including
`N=1`. The balanced leading asymptotics give `log f(z+j-1)=O_K(1/j)`;
geometric weighting permits local uniform differentiation. The positive
moment polynomial expands to `4-2t^3-t^4-t^5`, exactly the four source terms.
It proves GP-F's sign and decreasing-tail bound on the stated real domain.
The exponential seed quotient is exact; its logarithmic derivative is a
constant and all higher derivatives vanish. The claimed hidden factor is
therefore a valid limited observability obstruction. It does not prove
source-selected Fourier cancellation.

**Next falsifier:** an omitted multiplier residue, a repeated prime in two
counted bands, a late PF-05 survivor whose difference loses a prime without
`p | 16^d-1`, or a lower value of the precisely declared envelope. None was
found. A centered-numerator estimate remains an additional arithmetic theorem.
