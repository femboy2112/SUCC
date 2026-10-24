# Pascal / BBP source: validation and authority record

**Date:** 2026-10-24. **Parent:** draft #270 at
`3acd547ff122368d5694efdab029b3156a292d8a`.
**Branch:** `research/pi-pascal-mahler-source-2026-10-24`.
**Main rechecked:** `e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
No archived source was edited. Main, historical claim rows, and existing draft
heads are preserved. The separate #269 donor was read, not merged.

## 1. Required repository gates

All commands used `/workspace/scratch/bc13a8eed687/succ-venv/bin/python`
(Python 3.12.14), from the SUCC checkout.

| Gate | Executed result | Receipt |
|---|---|---|
| `scripts/verify_provenance.py` | Exit 0; 72 items, 55 mechanical namespace migrations, 17 byte-identical research archives | [provenance JSON](PI_PASCAL_PROVENANCE.json) |
| Full `unittest discover -s tests -p 'test_*.py'` | Exit 0; **7,761 tests passed**, 722.219 test seconds, 725.895 process seconds | [full log](PI_PASCAL_FULL_SUITE.txt), [metadata](PI_PASCAL_FULL_SUITE_META.json) |
| `scripts/observer_foundations_probe.py` | Exit 0; scoped existing finite foundations probe | [foundations JSON](PI_PASCAL_FOUNDATIONS.json) |
| `scripts/ordinal_succ_report_probe.py` | Exit 0; scoped existing finite ordinal probe | [ordinal JSON](PI_PASCAL_ORDINAL.json) |

The three new production modules and their three test files were frozen before
the full run. Subsequent additions were proof documents, the standalone exact
probe, claim registration, and navigation pointers. The final focused replay
and namespace replay below cover those relevant integration risks. No new
production changes were made after the passing full run.

## 2. New instruments and focused replay

The 52 new tests comprise 21 source/Mahler tests, 15 real-kernel/filter tests,
and 16 positive-moment/averaging controls. The final replay of
`test_pi_pascal_*.py` passed all 52 in 1.025 seconds, exit 0:
[focused log](PI_PASCAL_FOCUSED.txt).

After registering PJT-01 through PJT-28, all 15 claim-namespace collision tests
passed in 0.044 seconds, exit 0: [namespace log](PI_PASCAL_NAMESPACE.txt).
No historical claim ID was renamed or promoted.

The standalone probe command is

```sh
python scripts/pi_pascal_probe.py --output research/2026-10-24/PI_PASCAL_RECEIPT.json
```

It passed **13,553 exact assertions** in 1.826 seconds. Every numerical
decision uses integers and `Fraction`; decimal strings are outward-rounded
display only. The [receipt](PI_PASCAL_RECEIPT.json) contains grouped counts,
finite ranges, rational fingerprints, source hashes, and all retained adverse
outcomes. The executable is [pi_pascal_probe.py](../../scripts/pi_pascal_probe.py).

### Distinct oracles and disclosed ranges

- Calibration: starts 0 through 16, orders 1 through 16 (272 pairs).
- Reserved region from the frozen contract: starts 19, 31, 64, 127;
  orders 17 through 40 (96 pairs).
- Literal original four-pole fractions and forward unwrapped values provide
  a distinct oracle for the reciprocal-product and beta implementations.
- A 256-term-per-arctangent Machin enclosure provides an independent real pi
  oracle. Its alternating-series bounds and all source amplification factors
  are retained exactly. No pi digits construct a source or countermodel.
- Minimal-degree thresholds and sharpness are checked at nine precisions
  through 256 bits, with original values and an independent backwards source
  evaluator. Rational and negative dyadic starts have separate checks.
- Odd-prime factor counts cover 3, 5, 7, 11, 13; the p3 four-pole cancellation
  is retained rather than replacing a sum valuation by its termwise minimum.
- Ten multiplier cases compare the signed filters with direct scaling at
  six orders. The direct filter's better real error and the Pascal base-2
  filter's larger division cover remain visible.
- A positive polynomial-density countermodel certifies depth 12 at normalized
  precision 17. Positivity and real carry tests beyond that depth concern
  its globally defined real moments, not unproved later dyadic jets.

The initial probe run caught a missing closing parenthesis in the new script.
That syntax error was corrected before the first passing receipt. Later
extensions added explicitly disclosed post-discovery checks; they are not
retroactively described as preregistered held-out data. A one-shot link audit
also identified the not-yet-created validation file; the final artifact audit
runs after this file exists.

## 3. Bounded final source-specific checks

The final recurrence/height exploration produced two additional proof dossiers
without editing production code or unit tests. Its checks are labelled
post-discovery in the receipt:

- Literal forcing/source values verify the order-four and order-five
  recurrences at every center 4 through 96, including the integer carry
  relation obtained from fractional parts.
- Integer base-31 filters are enclosed against the independent Machin oracle
  at six orders through 64.
- For every source index 1 through 192, the two fresh-prime denominator
  families are checked and the exact common odd-lcm divisibility is verified.
  No growth exponent is fitted from these samples.
- Thirteen primes test translated Pascal filters inside their first source
  windows, along with the annihilating-filter and p5 exceptions.
- The p89/order35 origin-row cancellation is retained exactly. This rejects
  the invalid promotion of a translated-row theorem to every row at the origin.

The source values in these controls are built from the original four-pole
formula. The all-order proofs, minimality proofs, entire-kernel construction,
and prime-height asymptotics are mathematical arguments in the dossiers;
finite arithmetic does not establish their universal quantifiers.

## 4. Adversarial and cross-audit disposition

The three research lanes used the same model. Their separate constructions,
different exact implementations, and cross-audits improve error detection;
they are **not independent external mathematical refereeing**.

The source lane audited the real-kernel proofs, beta constants, asymptotic
regimes, integer-filter criterion, and rational cover costs. Two small scope
clarifications were incorporated: translated-window limits fix all of q,d,k,
and universal carry-readout necessity is across unrestricted integer lifts.

The real-kernel lane audited the entire positive-moment countermodel, including
moment stabilization, rationality, uniform dyadic precision and literal carries.
The adversarial lane independently calibrated the finite constructor by a
different rational linear algebra calculation and supplied the next-jet failure
of the depth-2 model. That failure is an intentional negative control.

The late prime-height report received a separate mathematical audit and an
independent original-forcing check of its delicate p89 and p5 cases. Both source
and kernel lanes inspected the exact probe's Machin signs, index ranges,
interval containment and certificate boundaries. Their reviews found no
substantive mathematical or implementation defect at the stated scope.

The final artifact audit checks Python compilation, all 13 hashed input files,
local document targets, balanced math/code fences, and the 30 exact registered
claim rows. Its machine result is [artifact audit](PI_PASCAL_ARTIFACT_AUDIT.json).

## 5. Authority and unresolved work

**PROVED at paper level:** exact authentic dyadic finite differences and their
optimal polynomial approximation; positive beta/tail identities; coherent
base filters with explicit carry costs; minimal recurrences; fresh-prime
filter restrictions; height bounds with identified classical PNT input;
the stated countermodels and averaging obstruction.

**VERIFIED_FINITE:** all test and probe outcomes, including the concrete phase
gap and cancellation examples. These are calibration/falsification receipts,
not evidence of an asymptotic normality exponent.

**OPEN:** actual real-source conditional half retention, the cumulative
four-bit excess estimate needed for one-sixteenth contraction, same-law
tripling or times31 invariance, and pi normality in the requested bases.

No formal Lean authority, theory-independence result, scholarly priority,
external peer review, or mathematical conclusion from CI is claimed.
The eventual published tree must be compared with the locally staged tree;
remote workflow status is reported separately from these completed local gates.

## 6. Final paper-only followups

After the first draft commit, the arbitrary-positive-constant extension of
the moment construction was separately derived and audited. Its
[full proof](PI_PASCAL_PRESCRIBED_CONSTANT.md) explains exactly why rational
Newton coefficients still give rational integer source and forcing values,
although the real density corrections and tail moments may be irrational.
A specific Liouville constant gives a transcendental, nonnormal real source
with empirical circle law delta0 and almost complete central retention.

This followup changes proof documents, claim navigation, the PJT registry
and their validation receipts. The three production modules, three test files, standalone exact probe,
13 receipt inputs and all finite assertion counts remain unchanged. PJT-29
is paper authority; no numerical construction of its irrational density is
claimed. The namespace guard is replayed after its registration, and the
artifact audit includes the new document and its SHA-256. This avoids implying
that the earlier finite controls prove the stronger infinite construction.

The newly available sibling #271 was also read at exact head
`4eafc6151e9a494f2aea8ec79ca6cf5608152c80`, without merging it. Its analytic
Taylor remainder passed the read-only audit. PJT-30 records the additional
bound removing only the forcing phase with error less than 1485/28 while
retaining the exact selected mask. The constant and sign were checked by
separate algebraic derivations; this is another paper corollary, not a new
finite cancellation result. The final namespace guard covers all 30 rows.
Its replay passed all 15 tests in 0.047 seconds, exit 0:
[final namespace log](PI_PASCAL_NAMESPACE_FINAL.txt).

The prescribed-constant proof also includes the finite-prime corollary:
all nonnegative integer source values can match any fixed finite set of
prime-place precisions while the real constant remains arbitrary. Odd-prime
global analytic interpolation is not asserted. The updated artifact audit
records this paper's hash; the finite numerical receipt is unchanged.
