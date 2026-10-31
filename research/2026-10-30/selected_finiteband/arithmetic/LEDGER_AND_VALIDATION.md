# Arithmetic result ledger and validation

| Candidate / route | Result and exact domain | Status | Boundary / next obligation |
|---|---|---|---|
| Positive finite-prefix/finite-jet spoofing | PR408 SF02–04 already establishes the broad zero-seed positive nonnormal obstruction | INHERITED PROVED LOCAL; initially rediscovered, provenance corrected | Do not count broad no-go as new; prior shift-filter controls also give stronger relative closeness and dyadic coherence |
| Order-two Stieltjes source representation | Explicit positive ν, rational moments and unchanged BBP Green transform | PROVED LOCAL | Representation alone gives no cancellation |
| Positive rational atomic cubature | For all M≥1,J≥0, at most D=M+J+1 rational positive nodes match the M actual source values and J+1 moments | PROVED LOCAL | Different construction from PR408; source has additional double poles |
| Source-aware minimum atom count | Every positive atomic rule exact on this function space needs ≥ceil(D/2) atoms | PROVED LOCAL by signed Wronskians, Rolle and double-zero witness | Rational upper D not asserted sharp; no selected Fourier consequence |
| All-horizon exact Green constants | Every constructed mutant obeys g(n)≤(8n+1)^−2, lag≤16/(8n+1)^3, sum≤17/648<1/32 | PROVED LOCAL | These source-tail inequalities cannot distinguish the nonnormal mutant |
| Finite-band / CRT / carry identification | Full rational state list through M exactly matches; every function of that list agrees | PROVED LOCAL | Completed π phases are not asserted equal; global four-pole membership distinguishes source |
| All-jet repair | Positive rival with all moments inherits exponential moment, hence same measure | PROVED LOCAL | Restores source identification, not a signed estimate |
| Fresh SC06 actual joint-phase test | 18 prime/frequency cases,3675/4038 lag distances≥1/20; all pass≥half | OBSERVED exact finite | No uniform prime-window or all-horizon bound;318 primary-far/full-near compensation events retained |
| Wrong/same-ratio, rank-matched sources | Slip counts111,115,116 versus authentic119 over128 lags | OBSERVED, asymptotic AMBIGUOUS | Passing finite lag-density test neither authenticates BBP nor proves normality |
| Seven-pole null and dyadic alias | Null0/128 slips; same-forcing dyadic shadow retains35 tested odd-primary projections and has tiny lag distances | INHERITED controls replayed | Null changes source; alias changes seed and eventually equals original circle orbit; no false asymptotic rational-translation failure |
| p19 / p73 disappearances | p19 zero at10..16, returns8/19 at17; p73 vanishes at274 | INHERITED exact controls replayed | Denominator presence may not be presumed |
| Selected finite-band normality premise | No new authentic all-horizon upper bound derived | DARK | Use full global four-pole arithmetic and selected boundary to bound actual signed cofiber interaction |

## Executed checks

- `focused-green-final`: **12 tests PASS**, covering seven exact positive
  rational witnesses, finite-prefix/source agreement, recurrence and tails,
  positive source decay, source-discriminator after prefix, and p19/p73.
  Earlier12-test runs are retained and not double-counted.
- `discovery-replay`: four witnesses (M,J)=(2,1),(3,2),(4,1),(4,3).
- `holdout-replay`: fresh dimensions (1,5),(5,2),(6,0), with a different rational
  node-grid resolution. Output bytes exactly match the saved witness inputs.
- `oracle-final`: separate symbolic Laplace series, SymPy matrix inversion,
  combined-source direct unrolling. Seven witnesses, seven moments,18 full
  joint-phase hashes/counts and p19/p73 all independently reconstructed.
  The oracle does not import `quadrature.py` or `crt_probe.py`.
- `chebyshev-exact`: eight fresh exact rational Wronskian determinants match
  the proved sign; this is finite calibration of the unrestricted proof.
- `crt-final`:18 new native first-prime windows at primes1201,1213,1229,1237,
  1249,1277 and h1,3,7. Every case eligible L≥sqrt(p). The minimum certified
  slip fraction is33/38 at p1249,h3. These are finite observations only.
- `cylinders-review-final`: separate paper reconstruction and exact checks of
  the neighboring cylinder/Stoneham front:16,984 transition configurations,
  768 constant-word positions,100 period01 positions,2048 exact grid bounds,
  six Stoneham stages. Details in `CYLINDERS_REVIEW.md`.

All bounded command metadata records actual UTC timestamps, argv, cwd, Python
runner version, parent SHA, exit code and SHA256 of raw stdout/stderr. Commands
use the existing Python3.13 environment in `SUCC-zero-dispersion/.venv`; the
receipt wrapper uses system Python3.12. No dependencies installed. LP discovery
uses SciPy/NumPy, but proof authority and witness acceptance are exact rational
algebra. `run_receipt.py` is an unchanged copy of the principal research runner.
No mathematical test failed. A read-only guessed historical `transport/` path
was absent; the actual `arithmetic_barrier/arithmetic/` path was then used.
The initial unqualified novelty assessment was corrected on reading PR408;
its full dossier is pinned in the source manifest.

No new Lean result, external referee, full-suite or hosted-CI claim is made by
this subfront; those repository gates belong to the principal integration.
Same-model review is complementary evidence, not independent authority.

## Reproduction

From the repository root, use the known environment:

```sh
../SUCC-zero-dispersion/.venv/bin/python -m unittest discover -s research/2026-10-30/selected_finiteband/arithmetic -p 'test_*.py' -v
../SUCC-zero-dispersion/.venv/bin/python research/2026-10-30/selected_finiteband/arithmetic/independent_oracle.py
../SUCC-zero-dispersion/.venv/bin/python research/2026-10-30/selected_finiteband/arithmetic/crt_probe.py
../SUCC-zero-dispersion/.venv/bin/python research/2026-10-30/selected_finiteband/arithmetic/chebyshev_probe.py
```

The primary-paper [Bayer–Teichmann abstract](https://arxiv.org/abs/math/0502473)
was inspected for cubature provenance. It is not used as a black-box proof of
rational nodes or of the ECT lower bound; both arguments are supplied locally.
