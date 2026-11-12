# Prime Interferometer: reconstructed companion and new replay

This preserves the mathematical substance of the immediately preceding
Goldbach / Haar conversation and connects it to the new fixed-point and
cylinder work. The implementations and receipts here were reconstructed and
executed in this round. They are not represented as the unavailable prior
ZIP's original bytes or execution history.

## Midpoints, radicals, and split integers

For n>=2, binary Goldbach at 2n is equivalent to the existence of an integer
`0<=d<=n-2` with both n-d and n+d prime. The unit 1 is excluded as a midpoint
of two positive primes. At a prime midpoint, d=0 is a witness; composite
midpoints require a noncentral pair.

In the same range the principal-branch radical identity

```math
n=\sqrt[3]{((n+id)/2)^3}+\sqrt[3]{((n-id)/2)^3}
```

is exact. The arguments of `(n±id)/2` have absolute value <pi/4, hence their
cubes stay within the principal cube-root inversion sector. This identity
also holds for non-prime-compatible d; the radicals do not supply the prime
pair. The original `4=cuberoot(2+11i)+cuberoot(2-11i)` follows from
`(2±i)^3=2±11i`.

The split-integer algebra `Z[j]/(j^2-1)` maps into Z x Z by
`a+jb -> (a+b,a-b)`. Its image is precisely the pairs agreeing modulo 2;
the inverse is `a=(x+y)/2,b=(x-y)/2`. Therefore

```math
\mathbb Z[j]/(j^2-1)\cong\mathbb Z\times_{\mathbb F_2}\mathbb Z.
```

For `z=n+jd`, its projections are n±d and its norm is
`z conjugate(z)=n^2-d^2`. Since both factors are >=2, the statement
`Omega(n^2-d^2)=2` is equivalent to both projections being prime. This is
the same total-degree-2 condition used in the cylinder construction.

## Local CRT factors and the global gap

For an odd prime ell, the forbidden displacement classes solve
`d=±n mod ell`. There is one class if ell divides n and two otherwise.
At ell=2 there is one class. For any finite collection of primes the Chinese
remainder theorem multiplies these exact local densities. Normalizing by
the two individual prime-avoidance densities gives the convergent product

```math
\mathfrak S(2n)
=2 C_2\prod_{\substack{\ell\mid n\\\ell>2}}
\frac{\ell-1}{\ell-2},\qquad
C_2=\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right).
```

To check the formula, at an odd ell not dividing n the factor is
`ell(ell-2)/(ell-1)^2`. Replacing it for ell|n multiplies by
`(ell-1)/(ell-2)`; the ell=2 factor is 2. The infinite generic product
converges positively because the omitted quantities are O(ell^-2).
This is the classical Goldbach singular-series expression, recovered from
the midpoint source. Local admissibility does not prove a prime pair inside
the required finite interval.

## Pair states, Haar blocks, and Fourier projection

For two labelled registers define

```math
|\Gamma_N\rangle=\sum_{\substack{p+q=N\\p,q\text{ prime}}}|p,q\rangle.
```

Its squared norm is R(N). When nonzero, the normalized state has R(N) equal
Schmidt coefficients: the map p -> N-p is one-to-one, so both sides of the
displayed expansion are orthonormal. Its Schmidt rank is R(N), and its
entropy is log R(N), with the logarithm base declared by the chosen entropy
units. This is an entanglement statement about the constructed register model.

Exchange pairs unequal representations, with the sole possible fixed
representation `(n,n)`. Hence `R(2n)=2G(n)-1_P(n)`, and
`R(2n)=1_P(n) mod 2`. PFO-09 gives the stronger operator decomposition:
reflection has symmetric and antisymmetric two-point Haar states with
eigenvalues +1 and -1.

For `F_N(alpha)=sum_(p<=N) exp(2pi i p alpha)`, ordinary character
orthogonality also gives

```math
R(N)=\int_0^1F_N(\alpha)^2e^{-2\pi iN\alpha}\,d\alpha.
```

The integral keeps precisely the paths with the specified sum. A different
beta-expansion of the same pair is a new presentation, not another pair state.

## Fresh Haar replay and the parity convention

The preceding conversation's coarse-baseline table corresponds to **zeroing
the singleton prime-2 endpoint while keeping all displacement coordinates**.
The new receipt separately records fully unfiltered arrays, parity-filtered
arrays on the original grid, and the parity quotient. Their witness counts
agree for n>2, but their marginal baselines can differ.

All entries below are exact fractions, not numerical fits:

| n | G(n) | Filtered full-grid baseline | Filtered full-grid detail | Quotient baseline | Quotient detail |
|---|---:|---:|---:|---:|---:|
| 100 | 8 | 15/4 | 17/4 | 15/2 | 1/2 |
| 256 | 11 | 2279/256 | 537/256 | 2279/128 | -871/128 |
| 1024 | 25 | 23427/1024 | 2173/1024 | 23427/512 | -10627/512 |
| 4096 | 76 | 260669/4096 | 50627/4096 | 260669/2048 | -105021/2048 |

For example the **unfiltered** n=100 baseline is 125/32, with detail 131/32.
It is different because its negative-side marginal still counts the prime 2.
This resolves the convention rather than silently mixing table definitions.

The parity-filtered finest Haar band equals G(n)/2. That contribution already
contains the unknown overlap; treating it as independent positive evidence
would be circular. The quotient detail can be strongly negative.

## Fresh CRT / Haar lower certificates

At n=1024, the full unordered witness count is 25. In these samples all
25 witnesses lie in the relevant screened interior.

| Cell width | z=3 lower | z=5 lower | z=7 lower |
|---:|---:|---:|---:|
| 128 | 2 | 11 | 21 |
| 64 | 6 | 17 | 22 |
| 32 | 9 | 17 | 22 |
| 16 | 13 | 21 | 24 |
| 8 | 21 | 25 | 25 |
| 4 | 25 | 25 | 25 |

The full cell rows, both upper and lower bounds, and exact Haar bands are
reproduced by `prime_observer.py` and `probe.py`. The receipt includes all
dyadic widths down to 1 and cutoffs 2,3,5,7. Upper bounds apply to the
**screened interior**, not automatically to the full pair count.

At z=2 and width128, a coherent zero-overlap source matches every marginal
cell count, including total positive-side count137 and negative-side count171.
At z=3 and width64 the lower certificate is6, so this stronger observer
forces at least six interior witnesses. This is a finite certificate.

PFO-12 adds a new improvement: preserve the shared d=0 value instead of
treating its two appearances as independent positions. At midpoint9 a cell's
lower bound improves from0 to1. The midpoint1024 counterfeit remains valid
because its center is absent from the parity-screened set.

## The exact outstanding theorem

The program can decide any one finite pair question and refine its certificate
to the exact answer. Proving that every even input has a witness requires a
uniform source-dependent bound. Neither the local singular series, the
existence of the prime enumerator, the complete single-cylinder spectrum, nor
the availability of arbitrarily fine finite certificates supplies that bound.

See `NEXT.md` for the dependency cut and the explicit test that any proposed
new transport estimate must pass.
