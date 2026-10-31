# Executed validation and authority

Parent403: `5f350af7808532e55d74e80c948c02bb385c6e70`.
Branch: `research/zero-boundary-dispersion-2026-10-30`.
Everything added is under this directory; all source contracts and archives
remain byte-identical. No merge, force push, release or main mutation.

## Repository gates

| Gate | Actual result | Evidence |
|---|---|---|
| Full repository unittest discovery | **10,008 PASS**,977.825s unittest,986.179s wrapper | [log](receipts/full-suite.log), [metadata](receipts/full-suite.json) |
| Required provenance | PASS,72 items | [log](receipts/provenance.log) |
| Foundations / ordinal | PASS / PASS | [foundations](receipts/foundations.log), [ordinal](receipts/ordinal.log) |
| Mathematics graph | PASS,51nodes60edges | [log](receipts/math-graph.log) |
| Mathematics catalog | FAIL in child and untouched exact403 baseline | [child](receipts/math-catalog.log), [baseline](receipts/baseline-catalog.log) |
| Inherited source manifests | PASS,262 files unchanged;14 ancestry edges | [audit](receipts/source-audit.log) |
| Inherited401 artifact validator | PASS,128 artifacts and nested receipts | [log](receipts/inherited-artifacts.log) |
| Parent403 focused tests/oracle |12PASS;9Green points and15windowsPASS | [tests](receipts/parent-tests.log), [oracle](receipts/parent-oracle.log) |
| Inherited adversarial transfer suite |19PASS, including biased product laws, Champernowne, Kempner/de Bruijn, full Walsh and Stoneham2/3/5 | [log](receipts/inherited-adversaries.log) |

The catalog is a pre-existing stale-catalog failure, not a regression or a
passing gate. The native suite's intentional temporary-catalog diagnostic and
unchanged Python escape warnings are retained in the raw log. The full run
used an isolated ignored `.venv`, Python3.13.13, mpmath1.3.0, numpy2.5.4,
sympy1.14.0, scipy1.18.1, one numerical thread,1024MiB and2400s timeout.
No new research tests are silently counted in the10,008 native tests.

## New checks

**54 focused tests PASS:**11 root moving-frequency +16 Diophantine
+13 CRT +14 spectral. Front metadata records the exact interpreter versions;
some front tests use system Python3.12.3. Separate oracles retain their own
versions and provenance rather than being presented as one independent run.
The31 inherited focused tests (12parent403 +19adversarial transfer) are
reported separately from these54 new tests and the10,008 native tests.

- Root:15 separately unrolled exact signed-deficit witnesses and two symbolic
  resolvent checks; five rational Machin/Taylor high-frequency source-sum
  certificates. [Tests](receipts/moving-tests.log), [oracle](receipts/moving-oracle.log),
  [high band](receipts/high-band-oracle.log).
- Positive-slip union:12 fresh short-prefix exact unions,1,548 forward-grid
  comparisons, authentic exclusions and coherent inclusions. [Raw receipt](receipts/cylinder-union.log).
- Diophantine:18 fresh authentic windows,12 sparse interval rows,12 entire
  coherent windows,36 continued-fraction folding comparisons; separate
  prefix/Machin/separation/digit-budget/symbolic oracle.
  [Detailed authority](diophantine/VALIDATION.md).
- CRT:48 fresh full/primary/cofiber rows,24 eligible SC-06 cases, minimum
  slip fraction39/44; two exact dyadic shadows;41 filter certificates;
  five full-prime-power shortcut refutations; p19/p73 preserved.
  Independent integer-orbit oracle checks48rows,12cylinders and27,786
  prime-valuation LCM cases. [CRT dossier](crt/CRT_DOSSIER.md).
- Spectral:36 rational interval Gram certificates, all below1;17 authentic
  finite-floor1 counterexamples. Separate100-digit oracle verifies the
  intervals, not their rigor. Golden/Oily, quartic jets, native3marks,
  noncommuting Walsh/carry loops and Stoneham2/3/5 controls executed.
  [Detailed authority](spectral/VALIDATION.md).
- Complementary arithmetic implementation:1,260 LCM cases,26 moving filters,
  1,024 field-inclusion checks, five exact extension degrees and three
  annihilator polynomials. [Review](ARITHMETIC_REVIEW.md),
  [receipt](receipts/arithmetic-review-calibration.log).

## Formal scope and retained failures

Lean4.14 compiled `diophantine/NoWrap.lean`. Its two declarations prove only
denominator-cleared integer no-wrap and finite iteration, with reported
axioms `propext`, `Quot.sound`. Real nearest-integer phases, irrationality
exponents, source integrals and asymptotic results are not formalized there.
The initial nonexistent-lemma compiler failure and source snapshot remain.

The spectral probe initially failed only when serializing fractions beyond
Python's4300-digit output limit. Its source and traceback remain; the repair
uses rigorously outward-rounded endpoints, and the final oracle passed.
Retrospectively recorded front command metadata is explicitly labeled as
recording time; it is not an invented execution timestamp.

Reviews share model/context lineage. The spectral review of the Diophantine
file predates its later Shallit extension; that extension was independently
read against the primary paper by root and its fold tested against Euclid.
The arithmetic review predates the final explicit h!=0 annotation in the
cylinder section; root checked that strengthening of the stated domain.
Root's [spectral review](SPECTRAL_REVIEW.md) pins the final spectral dossier.
No external referee or whole-theorem Lean certification is claimed.

## Live repository and hosted checks

[Initial](receipts/initial_remote.json) and [refreshed](receipts/refreshed_remote.json)
metadata pin390–403. All heads are unchanged and all remain open drafts.
At refresh,390/391/395–402 have four successful workflows each. PR403 has
three successful workflows and full validation in progress. For392–394 no
runs were returned, including the [all-event API check](receipts/sibling_all_event_ci.json);
this is not a passing status. New child exact-head CI is reported in its PR
after push; these parent snapshots do not certify the child.

`SOURCE_MANIFEST.json` indexes the completed package.
`validate_artifacts.py` checks inventory, bytes, nested sources, receipt
outputs, local links and the explicitly retained failures. It does not
certify the mathematical claims.
The first final audit remains as `artifact-validation.*`; the subsequent
`artifact-validation-final.*` audits the added inherited-control receipts.
Both audit pairs are explicitly excluded from the manifest's self-hash cycle.
