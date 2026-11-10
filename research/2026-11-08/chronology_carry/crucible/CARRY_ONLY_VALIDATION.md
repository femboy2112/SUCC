# Actual carry-only innovation: postregistration instrument check

This is an exploratory check on the **same existing holdout**, not another
fresh source prediction or a fitted model. It evaluates the EI1 signed
innovation for h=1,3 and k=1,2,3 using literal carries alone, before comparing
it to any observed full phase. The source interval is the clean clock
I=[55003,110004], N=55002. The source signature remains the four signed
poles and literal U0=0.

The observer updates S_n=(16S_(n-1)+kappa_n) mod16^k, starting at S_0=0.
Every literal carry is propagated before reduction. The preparation builds
actual transition character counts for n=55003,...,110003. Its direct EI1
formula is

    D=(1/N) sum_(j=0)^(k-1) [
       A_(j,k) sum_n e(h16^j S_(n+1)/16^k)
       -A_(j+1,k) sum_n e(h16^(j+1)S_n/16^k)].

It does not obtain D from the observed phase mean or from a telescope of g.
A separate calculation of the retrodictive g mean and Poisson endpoint
then verifies that identity. The implementation uses70-digit interval
trigonometry and retains every signed level contribution. Reference
conditional zero is checked through the coefficient identities valid for
all states, plus four explicit states at each h,k. The coherent fixed state
S=16^k-1, incoming carry15, is separately checked against e(-h/(2*16^k)).

No carry at110005 was available or requested. The omitted final transition
is charged by the last full phase's modulus1/N. Source retrodiction and
the Poisson endpoint give the valid finite comparison

    |W_I-D| <= (4k+1)/N + pi|h|16^-k
                          +pi|h|/[32(55003-k)^2].

The source phases are accessed only in the separate comparison command.
The prepared carry-only receipt was hashed first:
`db31008d38ba0aa65c9448dcb9988c91d4d9ec62daf4f2e8d0f8ae1f31941d1f`.
Raw receipts retain the source-file hash, carry-stream hash, exact rational
interval endpoints, counts hashes, normalization and implementation hash.

All six source comparisons pass. Displayed bounds are rounded upward;
the comparison actually requires the difference's upper endpoint to be
below the proved budget's lower endpoint.

| h | k | Memory bits | Observed difference upper | Source budget upper |
|---:|---:|---:|---:|---:|
|1|1|4|0.000120745|0.196441|
|1|2|8|0.000033659|0.012436|
|1|3|12|0.000017902|0.001004|
|3|1|4|0.001323967|0.589140|
|3|2|8|0.000074952|0.036980|
|3|3|12|0.000009729|0.002538|

There were no incoming literal16 carries in this held-out interior. Exact
synthetic unit tests nevertheless exercise carry16 propagation, reject
invalid source digits and unsupported depth, check the final endpoint's
timing, and reject zero/resonant frequency misuse. **Two new tests pass**.
This instrument uses the same authenticated carry receipt as the original
run, so it is not independent source evidence. Its direct formula is a
separate implementation from the earlier empirical predictor and generic
Poisson compiler.

Reproduce with the existing environment containing mpmath:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/2026-11-08/chronology_carry/crucible/carry_only_innovation.py prepare --source research/2026-11-08/chronology_carry/model/HOLDOUT_55003.json.gz --output /tmp/carry-only-prepared.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/2026-11-08/chronology_carry/crucible/carry_only_innovation.py compare --source research/2026-11-08/chronology_carry/model/HOLDOUT_55003.json.gz --prepared /tmp/carry-only-prepared.json --output /tmp/carry-only-comparison.json
```

This verifies an actual source-to-observer transport with known error. It
does not prove that the observer's signed mean decays, and the finite
small means are not promoted to all epochs or all frequencies.

**Original-zero signed innovation decay: OPEN. Pi normality: OPEN. RH: OPEN.**
