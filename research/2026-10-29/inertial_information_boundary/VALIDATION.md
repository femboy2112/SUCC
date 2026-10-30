# Validation and authority of the inertial information boundary instruments

**Date:** 2026-10-29 (America/New_York).
**Parent commit:** `b6a3815ceb505de0b1f570eae3ff5be75cdbe99c`.
**Python:** 3.12.14. The repository's declared mathematical dependencies were
available through `/tmp/succ_triangle_deps`; the checkout root was also on
`PYTHONPATH` so probe subprocesses could import the package.

The paper proofs establish their quantified mathematical statements. The
receipts below check exact finite implementations and scoped regressions.
They are not Lean certificates or proofs of the authentic signed BBP limit.

## 1. Exact mechanisms and separate implementations

The production module uses integer and `fractions.Fraction` arithmetic for
preparation maps, recurrence histories, code lengths, conserved charges,
source values, and phase exponents. It never substitutes floating point for
an exact phase-identity verdict.

The separate oracle does not import the new production module. It reconstructs
the prefix parser, affine composition, valuation threshold, and shifted
coherent source. It shares the pinned native source function for an explicit
source passport comparison. Both implementations were produced in one
research session; this is implementation separation, not independent source
provenance or external review.

The predeclared grids and mutation witnesses are preserved in
[independent_oracle.json](receipts/independent_oracle.json). The oracle passed
**159,192 exact assertions** and rejected **13/13 deliberate mutants**.
Of that total, 140,715 assertions are pairwise prefix comparisons. Other
groups check 6,825 affine preparation compositions and their costs, literal
absolute and relative phase kernels, causal future-pulse controls, exact
source values, and the coherent countermodels. Counts measure checks, not
independent mathematical discoveries.

The production probe passed **966 checks**, including 840 heldout phase
quotient checks, 80 certified KL/boundary checks, 20 certified optimum-mass
brackets, a conditional-information mutation, and three regression assertions
for retaining endpoint precision. See
[production_probe.json](receipts/production_probe.json).

## 2. Rational certificates for logarithms and KL bounds

For positive rational `x`, the probe computes `x=2^k*y` with `1<=y<2` and
`t=(y-1)/(y+1)`. The identity

$$
\log y=2\int_0^t\frac{du}{1-u^2}
       =2\sum_{j=0}^{m-1}\frac{t^{2j+1}}{2j+1}+E_m
$$

has the exact enclosure

$$
0\le E_m\le
\frac{2t^{2m+1}}{(2m+1)(1-t^2)}.
$$

The remainder follows by bounding every denominator in the positive tail
below by `2m+1`, then summing its geometric factor. The same series encloses
`log 2`; multiplying its interval by a negative `k` reverses the endpoint
order. Combining it with the interval for `log y` gives a rational enclosure
of `log x`. No floating-point operation supplies a certificate.

Binary KL and chain-rule intervals use rational arithmetic on these
enclosures. The optimum-mass bisection moves an endpoint only after a strict
certified comparison with the exact budget. If an interval is inconclusive,
the series precision increases; it cannot be treated as a favorable verdict.
Finite decimal output is rounded outward from the rational endpoints using
integer floor and ceiling. Those displayed endpoints therefore contain the
true quantity, rather than merely reporting an approximate evaluation.

### Audit correction and regression

A read-only mathematical audit found a potential false-failure in the first
probe version. A bisection endpoint could be accepted using 48 or 96 series
terms, but the final assertion recomputed its interval with the coarser
24-term default. The coarser interval could become inconclusive and reject
an otherwise valid bracket. This was a robustness issue, not a false positive
mathematical certificate and not an observed failing production receipt.

The corrected probe retains the accepted endpoint enclosure and its
precision. Its regression sets `epsilon=1/4`, first midpoint `5/8`, and an
exact rational budget halfway between the 24-term and 48-term certified
upper KL bounds. The 48-term enclosure accepts the midpoint while the old
24-term final check would reject it. The retained-certificate implementation
passes all three regression assertions. The raw receipt records this
distinction explicitly.

## 3. Reproduction commands and required gates

Run from the repository root with declared dependencies installed and the
checkout importable by any child processes. The exact local commands and
timings for the short gates are in
[required_gates.json](receipts/required_gates.json).

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_inertial_information_boundary.py' -v
python -m unittest discover -s tests -p 'test_recursive_carrier_triangle.py'
python scripts/inertial_information_boundary_oracle.py --output /tmp/inertial_oracle.json
python scripts/inertial_information_boundary_probe.py --output /tmp/inertial_probe.json
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

| Gate | Result | Receipt |
|---|---|---|
| Original provenance | PASS | [provenance.log](receipts/provenance.log) |
| New focused unit tests | PASS, 24/24 | [focused.log](receipts/focused.log) |
| Parent triangle unit tests | PASS, 25/25 | [parent_triangle.log](receipts/parent_triangle.log) |
| Independent exact oracle | PASS, 159,192 assertions; 13/13 mutants rejected | [independent_oracle.json](receipts/independent_oracle.json) |
| Production rational certificate probe | PASS, 966 checks | [production_probe.json](receipts/production_probe.json) |
| Observer foundations probe | PASS | [foundations.log](receipts/foundations.log) |
| Ordinal report probe | PASS | [ordinal.log](receipts/ordinal.log) |
| Full repository unittest suite | PASS, 9,832 tests in 946.558 seconds | [full_suite.log](receipts/full_suite.log), [full_suite.json](receipts/full_suite.json) |

The full-suite log may include `STALE/MISSING mathematics catalog` from the
negative test that deliberately changes a temporary fixture and requires
the checker to return one. That expected diagnostic is not a unittest error
marker; the completed runner summary determines the gate result.

The initial staged whitespace check reported Markdown hard-break spaces and
an extra final blank line. These were normalized in the new documents and
the staged check was repeated successfully. The initial diagnostic is kept
in [initial_diff_check.json](receipts/initial_diff_check.json); it affected no
mathematical statement or executed Python file. Catalog and local-link
preservation checks are in [catalog_check.json](receipts/catalog_check.json).

## 4. Source and status preservation

The inherited source files and executed new Python bytes are pinned in
[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json). The original `U_0=0`, four-pole
source, archival import manifest, historical claims, and generated memory
index are preserved. Only the claim catalog is regenerated to discover eight new research
documents. Its 1,990 historical claim rows, 203 claim-supplement entries,
176 registered namespaces, 162 existing warnings, and all 1,130 earlier
source-document entries are preserved. The source-document count is 1,138.
The four executed Python files compile and match their manifest hashes;
local links and Markdown math/code delimiters were checked.

The parent PR's four reported hosted workflows succeeded on exact parent
head `b6a3815ceb505de0b1f570eae3ff5be75cdbe99c`. That observation is context;
it is not a hosted result for this new branch. Hosted checks for the published
head must be reported separately from these local receipts.

The mathematical stop condition is satisfied by the scoped preparation,
information, causality, and observation results and their controls. The
authentic signed cancellation theorem remains `UNVERIFIED; OPEN`.
