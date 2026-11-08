# Three preregistered rounds: observations and falsifiers

These are finite interval certificates. Their endpoint integers have common
denominator 2^80. The source starts at literal zero and is computed unwrapped;
all controls are explicitly labeled. See [instrument proof](INSTRUMENT_PROOF.md).

## Round one: the actual remaining covariance

Protocol was pushed at `fd925707` before root measurements. All32 cases
(8 epochs times h=1,2,3,5) satisfy the finite candidate |Cov_A|<=4/sqrt(A).
There are12 pilot and20 holdout/stress cases. The largest observed
sqrt(A)|Cov_A| is approximately1.658; this is a descriptive statistic, not a
fitted future constant. The asymptotic covariance estimate remains OPEN.

| A | selected p | ord_p(16) | Certified |Cov_A(1)| upper bound | Matched shadow Re Cov_A(1) lower bound |
|---:|---:|---:|---:|---:|
|32|113|7|0.088081|0.764673|
|64|233|29|0.059375|0.968976|
|128|457|19|0.065636|0.997276|
|257|1009|126|0.074898|0.980140|
|509|2017|84|0.035036|0.968298|
|1021|4073|509|0.048654|0.998800|
|2039|8089|1011|0.020403|0.997334|
|4093|16369|682|0.017124|0.999999|

Displayed bounds are rounded outward. Raw rectangles retain the signed real
and imaginary parts of W, both marginal means, and the bilinear covariance.
The matched shadows preserve the selected prime channel exactly and the
declared early carries/2-adic data. Their literal-zero and source-support
authentication both fail. In particular, the highly coherent control at4093
is not a near-normality claim about an altered seed. Each horizon has its
own rational counterfeit.

Three direct modular source sums per epoch independently verify24 selected
states. The unit tests compare141 complete small states against the inherited
Fraction source and test principal parts separately. Source hashes and exact
seed integers make the full finite histories reproducible.

## Round two: a promising sufficient premise actually fails

Protocol was pushed at `42f9ed6d` before spectral measurements. Fold the
complement over the repeated clean prime clock, and allow the **best**
s=floor(sqrt(m)) Fourier terms, selected with full knowledge of the data.
The proposal was that the normalized L2 prediction error is at most1/2.

| p | m | repeated cycles | Original best-sparse error squared, h=1 | Verdict for h=1 and2 |
|---:|---:|---:|---:|---|
|281|35|2|>0.256093|REFUTED in both cases|
|617|77|2|>0.312273|REFUTED in both cases|
|1009|126|2|>0.353608|REFUTED in both cases|
|1601|100|4|<0.161348|passes these finite cases|
|2017|84|6|<0.107627|passes these finite cases|

All ten matched-shadow cases reject the same approximation threshold. Every
DFT coefficient is interval-enclosed; Parseval gives a bound valid for **any**
s-element support. Thus the six original-source failures cannot be repaired
by choosing a more favorable support of that size. Direct signed products
and the full signed cross-spectrum agree within their independent rectangles.

The result is a productive failure. Uniform prime-clock Fourier cancellation
is valid, but this simple sparse model does not automatically supply the
missing original-source complement estimate. Higher replication can reduce
the folded norm in these examples; PE's order selector only guarantees
m>p^(1/3), so it does not establish that the replication count tends to infinity.
Neither high-replication success nor low-replication failure is an asymptotic
claim about the selected orbit. Overlapping source times are disclosed in
the second preregistration; these are fresh spectral probes, not wholly new
independent source datasets.

## Round three: actual causal carry-history models

Protocol was pushed at `0d0d57a9` before measurements. At A=383,769,1543 and
h=1,2,3,5, test memory lengths0,1,2,3 plus diagnostic singleton cells. Current
carry information is available after the current update; these are causal
observation features, not strictly past-only martingale predictors.

All12 original-source cases refute the proposal that one of the four carry
models gives the sharp CFS-5 **certificate expression** at most1/2. This does
not assert that the true Weyl modulus exceeds1/2. It means this feature menu
fails to certify that threshold, despite the small measured signed mean.
The receipts retain prime leakage, complement prediction error and both
orthogonal terms for every model. A separate coherent control remains at1
through all partition refinements; a nonresonant four-point control is
certified near0. Thus the instrument can detect a real saving when present.

The useful conclusion is specific: these short carry-memory menus do not pay
the remaining signed estimate. It is not a general impossibility result for
learning observers. [A separate exact control](PREDICTOR_BOUNDARY.md) shows why
full cancellation need not imply that a cheap chirp-prediction certificate exists.

## Reproduction

From the repository root, with its Python requirements installed:

```sh
python research/2026-11-08/covariance_forge/run_experiment.py --stage pilot --output /tmp/covariance-pilot
python research/2026-11-08/covariance_forge/run_experiment.py --stage holdout --output /tmp/covariance-holdout
python research/2026-11-08/covariance_forge/run_experiment.py --stage stress --output /tmp/covariance-stress
python research/2026-11-08/covariance_forge/run_spectral_probe.py --output /tmp/covariance-spectra
python research/2026-11-08/covariance_forge/run_history_probe.py --output /tmp/covariance-history
```

Elapsed times change on replay; mathematical endpoints, source hashes and
control seeds are deterministic. The stress epoch completed locally in
about40–59 seconds in the recorded runs. Spectral raw files are compact JSON
to keep the receipt footprint small; summary indices hash every raw file.
