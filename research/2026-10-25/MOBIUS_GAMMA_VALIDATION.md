# Boundary/Gamma validation and authority record

Date: 2026-10-25 (America/New_York). Parent PR #297 at
`eca4462ee4d62642b15c4af672136aa5bcacd00b`.
Branch: `research/mobius-gamma-boundary-2026-10-25`.

All mathematical implementations and tests were finalized before starting
the full discovery run. Subsequent work was proof documentation, receipt
serialization and this validation record. The original source modules and
archives were not modified. Main and sibling PR #298 were not merged or
changed. No new dependency or workflow was added.

## Checks observed in this environment

| Check | Result |
|---|---|
| Parent resonance-control / signed-Gamma / zero-one-Gamma baseline | 58 tests passed, 1.705 s |
| New source/Gamma/seam tests | 53 tests passed as part of the combined focused run |
| New tests plus claim and Academic VII namespace guards | 71 tests passed, 1.447 s |
| Required full unittest discovery | PASS: 8,448 tests in 836.625 s, exit 0 |
| Source provenance | PASS: 72 items; 17 byte-identical archives and 55 mechanical migrations |
| Observer foundations probe | Exit 0, raw JSON preserved |
| Ordinal report probe | Exit 0, raw JSON preserved |
| Exact receipt generation and independent replay | PASS: 24 construction/authority inputs hashed |
| Receipt mutation setting normality_proved=true | Rejected, exit 1, explicit receipt mismatch |
| Large signed rational serialization round-trip | PASS, exact hexadecimal numerator/denominator |
| Independent analytic oracles | Four boundary-window holdouts; Gamma interval containment; six q-Gamma quotient cases, 80 decimal working precision |
| Nonlinear equivariance holdouts | 144 exact transported-map identities; seed-fixing and shifted-seed controls |
| Documentation link/math-delimiter checks | 10 files checked; no missing local targets or unmatched display delimiters |
| Byte compilation and staged whitespace check | PASS |
| New Lean authority | None claimed |

The analytic-oracle values are floating-point consistency observations.
Universal claims instead rest on the displayed proofs and certified rational
tail/error bounds. In particular the moving-boundary asymptotic is proved
by a summable boundary-layer limit, not extrapolated from its four holdouts.
Finite source coefficients, cyclicity defects, character enclosures,
reciprocal-word transport, Gamma product compensation and q-product tails
use exact integer/Fraction arithmetic.

The five new test modules contain 14 seam, 13 Gamma-primitive, 13 twisted
digamma/Euler, 7 q-Gamma and 6 boundary-layer tests. Their combined 53 tests
cover positive, negative, null and mutation cases. The additional 18 tests
are existing namespace guards, not new mathematical evidence.

Raw logs and the independent numerical receipt are under
[mobius_gamma_validation](mobius_gamma_validation/). The mathematical
receipt is [MOBIUS_GAMMA_RECEIPT.json](MOBIUS_GAMMA_RECEIPT.json).

## A serialization failure preserved and repaired

The first receipt generation hit Python 3.12's default 4,300-decimal-digit
integer-to-string limit while serializing exact sums of rational logarithm
intervals. The immediate verification repeated that failure; the initial
mutation probe then had no receipt to read. All three outputs are preserved
as `receipt_*_initial_failure.log`. They are not successful validations.

The repair changes only receipt encoding: rationals exceeding 8,192 bits
are stored as explicit hexadecimal numerator/denominator objects. The
interpreter's conversion guard stays enabled, no value is rounded, and a
large signed rational round-trip is checked independently. Generation,
replay and false-normality mutation then passed their respective success
or required-rejection conditions. This was a serialization issue, not an
analytic theorem failure. The corrected script is itself source-hashed.

The current deterministic receipt SHA-256 is
`a0fe97b0553b02023be5d05fcb323efc2a53dbf8588d120d823449f543ec2306`.
After intentional changes to a hashed proof or construction input, regenerate
and independently replay the receipt; do not edit its hash by hand.
The earlier successful replay before strengthening the equivariance theorem
is preserved separately; the final hash covers that stronger proof.

## Reproduce

Install the checkout and declared test dependencies into an isolated
environment. This run reused the already correctly installed Python 3.12
environment from the parent round; the previous missing-editable-install
failure was not repeated.

```sh
python -m pip install -e '.[test]'
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python scripts/mobius_gamma_boundary_probe.py --verify
```

For the new narrow suite:

```sh
python -m unittest tests.test_bbp_twisted_boundary tests.test_bbp_gamma_boundary tests.test_twisted_digamma_boundary tests.test_qgamma_seam tests.test_bbp_twist_boundary_layer -v
```

No local check supplies a claim that hosted CI has already passed on a
future commit. Parent #297's five returned hosted workflow runs were all
successful at the live read; this branch has its own separate hosted state.
The publication is batched as one branch push and one stacked draft PR.

## Scope

The code and proofs distinguish the authentic source and initial zero,
same-forcing changed-initial controls, sign-twisted source observables,
reference offsets, Gamma gauges and source-independent seam products.
No finite constant identity or positive moment certificate is promoted to
signed orbit cancellation. Pi normality, RH and logical independence remain
open. Agent audits share model and repository provenance; they are not
independent external peer review.
