# Source paths and observer histories: validation and authority

**Date:** 2026-10-24.
**Branch:** research/pi-path-selection-interference-2026-10-24.
**Current parent:** #272 at 6e8fa8b77886b13f1f533ed8083fd88c849d14b3.
**Initial test parent:** 8f2e6f852efafb4a0c871418c97ed819b1217d7d.
The [parent update record](PI_PATH_PARENT_UPDATE.json) shows that the
intervening commit changes only nine proof/navigation/receipt files.
No upstream Python source or tests changed. Historical archives are preserved.

## 1. Required repository gates

Commands run from the SUCC checkout with Python 3.12.14 at
/tmp/succ-twisted-venv/bin/python. The full suite also receives the repository
root through PYTHONPATH and the same virtual environment through PATH, so
subprocess checks use the declared dependencies.

| Gate | Executed result | Receipt |
|---|---|---|
| Provenance verification | Exit 0; existing archival contract verified | [provenance](PI_PATH_PROVENANCE.json) |
| Full unittest discovery | Exit 0; **7,826 tests passed**, 718.016 test seconds, 721.783 process seconds | [full log](PI_PATH_FULL_SUITE.txt), [metadata](PI_PATH_FULL_SUITE_META.json) |
| Observer foundations probe | Exit 0 | [foundations](PI_PATH_FOUNDATIONS.json) |
| Ordinal SUCC report probe | Exit 0 | [ordinal](PI_PATH_ORDINAL.json) |

The three small gate exit codes, commands and durations are preserved in
[PI_PATH_REQUIRED_GATES.json](PI_PATH_REQUIRED_GATES.json). Their finite
authority is inherited and scoped; passing them is not a normality proof.

The four new production modules and their four test files were frozen before
the single full run. Its metadata hashes those eight files and verifies
that they remain unchanged. Proof documents, the standalone post-discovery
structure probe, claim registration and navigation were completed separately.
The final namespace and artifact checks cover their integration.

## 2. Focused implementation verification

The complete new focused suite passed **65 tests in 1.301 seconds**, exit0:
[focused log](PI_PATH_FOCUSED.txt).

| Instrument | Tests | What the checks can establish |
|---|---:|---|
| Finite source projector | 25 | Exact characters, selector dependence, prefix marginals, carrier maps and integer-lift controls |
| Source selection limits | 16 | Rational enclosure construction, exact wrapped interval observables, effective-depth budgets and norm/variation controls |
| Positive history stationarity | 9 | Exact finite kernels, gcd distinctions, signed and degenerating-mixture failures |
| Circle history transport | 15 | Rational primal/dual certificates, independent assignment oracle, geodesic costs and preservation inequality |

The stationarity tests compare 65 kernel certificates with independent
functional-graph cycle counts, including noninvertible finite maps.
The transport tests independently enumerate all assignments for small
equal-weight measures; duplicated atoms supply unequal rational masses.
These checks are substantive controls of the formulas, not universal
proofs of the paper theorems.

## 3. Standalone exact receipts

### Finite projector

[PI_PATH_PROJECTOR_RECEIPT.json](PI_PATH_PROJECTOR_RECEIPT.json) records
90,280 candidate paths at moduli 3, 5, 7, 9 and horizons 1 through 4, plus
14,641 held-out paths at modulus 11/base 5. These are factorized character
checks. A separately disclosed Cartesian oracle actually enumerates
1,354 dual tuples over 52 candidate paths. The distinction is retained.

It also records 140 backward-dual observable checks, 1,412 prefix marginal
checks and 43 authentic rational BBP states checked independently against
the literal four-pole recurrence. Missing initial selection, nonunit phase,
wrong normalization, denominator poles, quotient/inclusion confusion and
integer-lift loss are retained as hostile controls.

    python scripts/source_path_projector_probe.py > research/2026-10-24/PI_PATH_PROJECTOR_RECEIPT.json

### Source selection and occupation limits

[PI_PATH_SELECTION_LIMIT_RECEIPT.json](PI_PATH_SELECTION_LIMIT_RECEIPT.json)
retains **240** cylinder combinations: four bases, five source depths,
four horizons and three exact sources. Base 5 is the prespecified holdout.
The constant-source rows preserve the false limit-interchange behavior.

Seven authentic enclosure/horizon rows retain exact mixture budgets and
independent Machin enclosures. Sixty-five depths 0 through 64 check strict
nesting and containment. The continuous periodic observable x(1-x)
has Haar mean 1/6 and circle Lipschitz constant 1; exact integral checks
calibrate the proved transport bounds without claiming one observable
determines a measure.

    python scripts/source_selection_limit_probe.py --output research/2026-10-24/PI_PATH_SELECTION_LIMIT_RECEIPT.json

### Prespecified actual-source transport

[PI_HISTORY_TRANSPORT_RECEIPT.json](PI_HISTORY_TRANSPORT_RECEIPT.json)
retains all nine combinations of primes 137, 281, 521 and history depths 2, 4, 8.
They were declared in the frozen contract before measurement. Every cost
is an exact rational, with outward decimal enclosures for display.

The independent assignment calibration compares 374 measure pairs and
actually enumerates 2,715 permutations. All 351 measured source states are
independently reconstructed with initial zero and the literal four poles.
The state-sequence hashes, exact source-to-pi tail budgets and all adverse
controls are retained. No monotonicity or decay rate is inferred.

    python scripts/source_history_transport_probe.py > research/2026-10-24/PI_HISTORY_TRANSPORT_RECEIPT.json

### Post-discovery structural controls

[PI_HISTORY_STRUCTURE_RECEIPT.json](PI_HISTORY_STRUCTURE_RECEIPT.json)
is explicitly post-discovery. It enumerates 1,469 joint path/dual atoms,
checks 115 literal terminal marginals with 1,435 terminal pairs, and
compares exact cyclotomic mass with the variation from atom count times
complex atom modulus.

It also retains all four 3-power-grid rows at K1 through K4. Exact radix
invariance, the nearest-coarse-grid tripling cost, the history decomposition
and the fixed-point component are checked separately. The asymptotic
failure of a too-fast averaging schedule is a paper proof, not a fitted
conclusion from four rows. The changing-denominator raw-amplitude
obstruction is likewise labelled paper authority.

    python scripts/source_history_structure_probe.py > research/2026-10-24/PI_HISTORY_STRUCTURE_RECEIPT.json

## 4. Cross-audit, corrections and scope

Three collaborating research lanes supplied different constructions and
adversarial checks. The root read the derivations and integrated the results.
These agents used the same model; their cross-audits are **not independent
external mathematical refereeing**.

The independent audits checked the finite projector's backward signs and
noninvertible-base domain; authentic circle inclusion versus residue
reduction; separate integer-carry authentication; the signed extension
criterion; both effective-depth constants; the all-fixed-scale
Portmanteau direction; nonergodic rigidity; good-prime coverage; and the
full source-window-to-every-prefix implication.

The strongest audit correction was conceptual: an existential slowly
diverging history schedule is equivalent to the old tripling premise.
This is now explicit, with a converse bound and a too-fast-grid control.
For fixed positive mixtures, gcd greater than one gives the weaker
3^d-invariance condition, still sufficient for the stated rigidity route.

Other corrections incorporated before publication:

- A handwritten expected transport cost for delta at 1/5 was 1/5; the
  independent unique-Dirac coupling gives 1/4. The test expectation was
  corrected before freeze; the transport algorithm did not change.
- The cylinder receipt has 240 cases; an early prose tally of 600 was
  corrected to match the actual product of ranges.
- The approximate concentration statement now specifies 0<=epsilon<=1,
  and cylinder/BBP prior masses are explicitly for the Haar prior.
- The original source forcing stays in the true selected law and masks.
  Tail amplification under a growing history depth is explicitly budgeted.

The latest prescribed-constant parent addendum received a separate read-only
paper audit. Its arbitrary real constant, rational source values versus
irrational tail moments, finite-prime congruences, Liouville occupation law,
successor-conditioned carry 15 and near-total central retention were checked.
It changes the exact four-pole forcing; its authority is paper-only.
SPS-25 extracts the all-time primary-phase consequence and explicitly proves
that the constructed complementary phases can asymptotically compensate
the authentic observed phases. It does not assert that behavior for the
authentic BBP complement.

## 5. Final integration and authority

After registering SPS-01 through SPS-25 and retaining the latest PJT-01
through PJT-30, the namespace replay passed all **15 tests in 0.043 seconds**,
exit0: [namespace log](PI_PATH_NAMESPACE.txt). The final
[artifact audit](PI_PATH_ARTIFACT_AUDIT.json) covers Python compilation,
receipt source hashes, local links, balanced fences and all 25 exact claim
rows. These checks establish file consistency, not mathematical truth.

**Earned:** exact source and operator identities, universal mixture and
variation bounds at paper level, classical inputs with their hypotheses,
scoped counterexamples, conditional normality closure and exact finite
measurements.

**Open:** authentic real all-scale retention, authentic source-law
preservation, the stronger selected collision/Fourier saving, and pi
normality. No new Lean theorem, foundational independence result, external
review or mathematical conclusion from hosted CI is claimed.

Publication uses one consolidated commit and draft pull request. The remote
tree will be compared with the tested/staged local tree. Hosted workflows
are reported separately from completed local validation.
