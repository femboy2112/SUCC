# Exact probes, controls and reproducibility

The universal claims are paper theorems. The following computations check
finite implementations, constants and declared falsifiers. No finite
observation is treated as a proof of a limit.

## 1. New focused suite

From the repository root:

~~~sh
PYTHONPATH="$PWD" python -m unittest discover -s tests -p 'test_pro_pi_*.py' -v
~~~

The recorded final focused run has **27 passing test methods**.

| Module / imported test class | Count | Coverage |
|---|---:|---|
| test_pro_pi_borwein_inverse.py | 8 | Exact kernel mean, rational extrema, interval inverse, atoms, original source and wrong sign/shift/coefficient mutations |
| gamma_source_probe.py via arithmetic test module | 9 | Positive source kernel, chronological telescoping, preserved residues, all-F/0 blocks, exact norm and leakage, coefficient mutation |
| flat_lock_probe.py via arithmetic test module | 7 | Prefix seam, rational tail selection, source errors, positivity/decrease, radix lock, exact norm, negative high-order difference |
| ProPiArithmeticTests | 3 | Prime certificate, elementary LCM bound through 256, one global 80-state integer gauge |

The root tests import the standalone Gamma and flat-lock classes explicitly,
so they are included in ordinary repository unittest discovery. The
standalone scripts remain directly executable.

### Prime implementation and fresh subtask holdouts

The seven preselected probe clocks were 17,33,65,129,257,513,1025.
The probe performs 1,665 exact normalized-principal-part comparisons,
988 sufficient-cutoff survival checks and 1,662 sign-mutation rejections.
Known cancelled primes 19 and 73 are retained, as are the finite holdout
cancellations at (129,37), (257,47), (513,113). None satisfies the sufficient
height certificate. These are arithmetic probe holdouts, not previously
unseen pi digit regions or an asymptotic normality holdout.

~~~sh
python research/2026-11-17/pro_pi_crucible/prime_survival_probe.py
python research/2026-11-17/pro_pi_crucible/prime_independent_audit.py
~~~

The separate standalone edge implementation imports no author probe code.
It checks every born time under p^2>8n for p=11,13,17,23: **128 cases**,
plus **17 LCM cases**, totaling 145. Both implementations retain the same
source and theorem formulas; they are not external mathematical witnesses.

### Borwein implementation controls

The exact interval-integrated inverse is checked on 198 rational intervals.
Wrong sign, missing half-turn and coefficient 1/7 in place of 1/8 are
required to fail. One-atom and nonunit radix-fixed controls remain non-Haar;
uniform grids provide a separate positive calibration. The supremum
algorithm also checks independently selected rational origins.

Source shells B=3,7,15,31 check the literal recurrence against the direct
finite weighted sum, exact rational maxima and the finite discrepancy
inequality. They are implementation calibration, not a new digit experiment.

The parent #657 maximizer and this maximizer agree exactly on ten configurations.
Both use piecewise quadratic interpolation, at different sampling points.
To reproduce without checking out or merging the donor branch:

~~~sh
git show 7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf:tests/test_borwein_bbp_sweep.py > /tmp/pro_pi_parent_sweep.py
python research/2026-11-17/pro_pi_crucible/compare_sweeps.py /tmp/pro_pi_parent_sweep.py
~~~

The sharp energy theorem is analytic, with a positive compressed-mass packet
proving optimality of exponent 1/5. Four rational constant identities and
a separate same-model proof audit are preserved. No new implementation of
the #663 energy was needed or claimed; its pinned implementation is credited.

### Flat counterfeit and moment-cone rejection

H-04's order-100,000,000 negative difference is established by retaining two
exact rational perturbations and bounding the rest by a geometric majorant.
It is not a computation of one hundred million source terms. The exact
rational upper bound is below -1/10^15 by integer cross multiplication.
The positive-moment counterfeit and the flat counterfeit are tested
separately; their incompatible preserved hypotheses are never combined.

## 2. Pinned parent replays actually executed

| Pinned source | Test file | Result |
|---|---|---|
| #657 | test_borwein_bbp_sweep.py | 9 pass |
| #662 | test_terminal_wall_crucible.py | 13 pass |
| #657 | test_bbp_pole_telescope_oracle.py | 10 pass |
| #657 | test_matched_nontele_locked_source.py | 8 pass |

The evidence directory records their exact extracted paths, commands and
outputs. These total 40 focused parent tests. #663's 24-test receipt was
inspected but is not represented as a local replay of those 24 tests.

## 3. Repository gates and environmental controls

The mandatory provenance, observer-foundations and ordinal-report gates
passed on the clean baseline and again after the new code was added.
The full-suite command, its resource bounds, the initial timeout/import
error, its targeted diagnosis and configured rerun are recorded separately
in VALIDATION.md. A timeout is never counted as a pass.

The initial full-suite error was in an unchanged baseline subprocess that
could not import observational_succ without PYTHONPATH. Its script, test
and imported module were byte-identical to pinned main. The targeted
11-test module passed after supplying the repository root in PYTHONPATH.
No baseline code was edited to make it pass.

The printed STALE/MISSING mathematics-catalog message came from a fixture
that intentionally changes a temporary catalog and expects a nonzero stale
check. It is not itself a failed repository-catalog assertion.

Lean was not on the local PATH. No Lean theorem, formal certificate,
blind external review or full donor-branch integration is claimed.
