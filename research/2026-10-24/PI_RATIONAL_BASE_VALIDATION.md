# Rational-base BBP research validation and authority

**Research-only 2026-10-24, stacked on draft #275.** Exact parent SHA 7c5d5b8856a1d132fb941ae40c946c0565918b36. No main merge, release, archived source edits, new Lean declarations, or π-normality claim.

## Actual local execution

- **13 new focused unittests passed:** python -m unittest discover -s tests -p 'test_*.py' -v, isolated with the new production module. This tests rational p/q digit/value roundtrip, 3/2 and 11/10 examples, all modulo p^L suffix decoders on finite small powers, exact Pascal additive sums, canonical word p under radix p/(p−1) for p=2..29, original zero-initial BBP literal source recurrence, independent binomial-vs-difference oracles through k=41, exact dyadic decimal valuations through k=79, base11-to-base10 operator identity, 11^L period, integer carry history and genuine p=137 selected real pair counts.
- **37,814 counted exact predicate checks** in the deterministic standalone probe, executed as PYTHONPATH=. python scripts/pi_rational_base_carry_probe.py --output /tmp/rbp.json. Predicate count is a finite calibration counter, not a theorem count or a number of independent samples.
- Independent rational Machin interval for π: 560 terms for each arctangent, with omitted alternating-term endpoints. Verified interval width less than 10^(−400); its precision suffices to certify floor(16^(n−1)π) decisions on all five selected finite windows p=73,137,281,521,1153. All tested literal BBP integer lifts match those integer prefixes; no all-time claim.
- Real signed Pascal decimal approximants certified for k=1..64 with alternating exact error sign and |error|<(2/3)^k π/16, separate from the symbolic source derivation.
- Authentic centered pair carry fractions, including both endpoints and all ordered diagonals, evaluated at p=137,281,521 and τ=1/4,1/16. For p=521 τ=1/4: matching literal modulo-11 lift class has (E,Z)=(1911,307) including 195 diagonal pairs, (1716,112) offdiagonal; different lift class (17116,1044). This is calibration, not 1/16 retention theorem.
- All three new Python files compile. Probe output was replayed byte-identically. The first development Newton recurrence had an indexing mistake caught by independent binomial tests, and the initial too-short Machin interval was replaced by a rigorous adequate one. A wider pairwise probe exceeded local execution budget; its larger one-point windows were retained and p=1153 pairwise data are not claimed.

## Audit hashes (Git objects verified against tested bytes)

| File | Git blob SHA-1 | SHA-256 |
| --- | --- | --- |
| observational_succ/pi_rational_base_carry.py | 9d0b5e06d080cc75e4ce9523f51166e702c0c34f | a22296ee5f77fc049696026730ca59b6affc75760f5e798e85c5b7c0caea1638 |
| tests/test_pi_rational_base_carry.py | acbe9eade879b2ae241921c56f17f9ee78f00434 | ab884ec6ea5fec4b94bf8d5cd3e3db40acc9ad021b75de5e71bdb0686b060366 |
| scripts/pi_rational_base_carry_probe.py | 645a910c0a5f5c74cc3f83cded31373b85de4381 | fab02b20efd793299e8978b9cebabb8eb76be24e6f93932d660d1aa5a0e10823 |

The exact Git blob objects were matched to the successful local files *before* the new tree was assembled. The full probe outputs have 5 authentic residue windows, 6 genuine signed-pair rows, 64 decimal intervals and 4 prime-11 clock orders. Re-generate with the command above to inspect every unfavorable case.

## Required SUCC gates and remaining research

The entire SUCC checkout was **not** available in the sandbox; direct Git network access failed DNS resolution. Accordingly **the repository-wide 7,000+ unittest discovery, scripts/verify_provenance.py, scripts/observer_foundations_probe.py, and scripts/ordinal_succ_report_probe.py were NOT run locally on this branch.** The GitHub-hosted CI runs on the published head must be checked separately; do not infer their outcome from earlier parent PR checks.

Papers use classical rational-base theory, p-adic finite-word maps, positive BBP moments, finite Fourier inversion and an explicit finite-state Markov countermodel. No independent external mathematical referee or new Lean kernel authority. **The real 1/16 retention, source-specific mixed Fourier decay and π normality remain OPEN.**

External source anchors: [Akiyama–Frougny–Sakarovitch integer rational bases](https://www.irif.fr/~cf/publications/AFSwords05.pdf), [Morgenbesser–Steiner–Thuswaldner adelic Fourier results](https://arxiv.org/abs/1203.4919). The latter concern pattern counts in integer rational-base expansions and cannot be silently applied to the selected BBP orbit.
