# Complete selected finite-band and CRT experiments

**OBSERVED FINITE / rigorous interval certificates.** These computations do
not prove an asymptotic estimate. The ordinary high-precision oracle is a
separate implementation check, not the authority for the enclosures.

## Integer enclosure algorithm

`certified_band.py` uses only integers and exact fractions, with scale S=2^128.
For a requested horizon N it builds a BBP enclosure at 4N+192 bits. The positive
series is `pi=sum_(n>=1)16^(1-n) r(n)`. Each truncated term is rounded down;
adding one unit per term and one for the bounded geometric remainder encloses
the full value. No supplied digits of pi enter the construction.

The completed phase at time n is extracted in one common real lift from both
endpoints. Subtract a 40-term original Green interval with remainder
`16^-40 r(n+41)/15`. A shared integer shift handles circle seams without
discarding an endpoint. Every resulting interval encloses the actual U_n(0).

For |angle|<4, the cosine polynomial through degree126 and sine through127
have respective errors at most `4^127/127!` and `4^128/128!`, both below1/S.
Every polynomial operation is rounded outward by exact integer floor/ceiling.
To obtain powers of a unit phase, use a complex center and Euclidean error
disk. If generator error is R/S and old power error E/S, the new error is at
most `(E+R+ceil(ER/S)+2)/S`. This follows from the true generator's modulus
one, the old center norm at most1+E/S, and less than sqrt(2)/S rounding error.
This avoids uncontrolled error growth from dependent rectangle products.

Sum real/imaginary intervals, square them outward, then apply the positive
weights `2(H-h)/(HN²)` and add the exact constant Fourier coefficient1.
Decimal endpoints are directed outward again. The code retains the full
dyadic endpoints, not just rounded display values.

Seven focused tests include exact recurrence containment, 300 source-pole
identities, rational Machin enclosures, rational unit-circle powers, seams and
Green tails. A separate 85-digit direct four-pole recurrence/Fourier oracle
checks nine fresh (N,H) combinations. A complementary review reconstructs the
algorithm and checks another4,004 exact powers and four further energy cases;
see [kernel/ROOT_INTERVAL_REVIEW.md](kernel/ROOT_INTERVAL_REVIEW.md).

## Predeclared calibration and holdout

| N | H | Certified enclosure |
|---:|---:|---|
|256|128|[1.464344785506,1.464344785507]|
|1024|512|[1.459511477113,1.459511477114]|
|4096|512|[1.107927975730,1.107927975731]|
|8192|128|[1.013623796304,1.013623796305]|
|8192|512|[1.059243283524,1.059243283525]|

N=8192 was held out until implementation tests passed. At N=1024,H=512 the
same-forcing coherent seed instead gives [508.224461156721,508.224461156722],
and the periodic01 completed-boundary seed gives
[254.116767226350,254.116767226351]. These are forced representations with
the original tail retained; their completed energies have the exact bounds
in the paper. All nine calibration, two holdout, nine oracle and six hostile
control rows are preserved under `receipts/`.

## Full signed interaction on fresh frequency holdouts

`signed_windows.py` declares p=1201,1213,1229,1237,1249,1277 and h=11,13
before evaluating the full complex averages. Birth times and period lengths
are exact; the finite candidate is squared mean modulus below1/4. All twelve
enclosures pass. The largest is below0.024455718831.

`signed_windows_oracle.py` independently computes rational source states,
splits each into canonical p-primary part a and p-integral complement v,
verifies the complement's denominator, and evaluates BOTH factors
`e(h a)e(h v)`. Their sum agrees with the directly reconstructed full phase
at85 decimal precision and lies inside the integer certificate. Neither
factor is discarded, averaged independently, or interpreted as random.
For example p1201,h13 has full squared mean about0.02331 while its primary-only
value is about0.001503. An unweighted primary estimate does not explain the
actual product.

The windows overlap heavily in time and share one source and implementation
family. They are not six independent mathematical authorities. No all-prime
bound, fixed-h limit, pair coverage, or normality is inferred. The arithmetic
front additionally records exact primary-far/full-near restorations, p19/p73
conductor disappearances, odd-primary aliases and source mutants.

## Reproduction

Run from the repository root; every actual command also appears in its JSON
receipt. For example:

```sh
python3 research/2026-10-30/selected_finiteband/certified_band.py --horizons 8192 --bands 128 512 --output /tmp/selected-band-replay.json
python3 research/2026-10-30/selected_finiteband/signed_windows.py
```

The second command rewrites its own deterministic data artifact; use a fresh
checkout or compare the stored hash before replaying. Original historical
source files are never written. Same-model review is not external refereeing.
