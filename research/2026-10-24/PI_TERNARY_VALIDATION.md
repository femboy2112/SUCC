# Weighted ternary Pascal: validation, provenance and authority

**Date:** 2026-10-24. **Parent:** draft #272 at
`6e8fa8b77886b13f1f533ed8083fd88c849d14b3`.
**Branch:** `research/pi-ternary-weighted-pascal-2026-10-24`.
**Pi normality, authentic all-scale real collision saving and source-law
prime symmetry remain OPEN.** No new Lean authority is claimed.

## 1. Required repository gates

All four required AGENTS.md gates passed locally under Python3.12.14:

| Gate | Actual result |
|---|---|
| python scripts/verify_provenance.py | exit0;72 items,55 namespace migrations,17 byte-identical research archives |
| python -m unittest discover -s tests -p test_*.py | exit0; **7,797 tests passed**,708.096 test seconds,711.693 process seconds |
| python scripts/observer_foundations_probe.py | exit0 |
| python scripts/ordinal_succ_report_probe.py | exit0 |

The [full log](PI_TERNARY_FULL_SUITE.txt) and
[input-hash metadata](PI_TERNARY_FULL_SUITE_META.json) preserve the actual
run. [Provenance](PI_TERNARY_PROVENANCE.json),
[foundations](PI_TERNARY_FOUNDATIONS.json) and
[ordinal](PI_TERNARY_ORDINAL.json) preserve the other gate outputs.

Both the new production module and all36 unit tests were frozen before the
full discovery run and have identical before/after SHA256 values:

- observational_succ/pi_ternary_pascal.py:
  `32823cfabfca58498424d2ac13f83e3e3a8049640bf0530f6cddccec2e669b96`.
- tests/test_pi_ternary_pascal.py:
  `845d73f602e8b28fb096898fae2230015bb004397d5fd44e723e3198409ebc7c`.

The late all-prime differential and coherence additions are paper results
with a separate standalone probe. They did not alter those two frozen files.
The final [focused replay](PI_TERNARY_FOCUSED.txt) passes all36 tests;
the final [namespace replay](PI_TERNARY_NAMESPACE.txt) passes all15 guards
after registering all28 TPG claim rows. This separately covers documentation
and registry additions made during the full run.

## 2. Exact finite instruments

Four standalone calibrations executed **43,928 exact assertions in total**.
These are assertion counts across potentially overlapping finite evidence;
they are not43,928 independent mathematical claims.

| Instrument | Exact assertions | Scope and receipt |
|---|---:|---|
| [Primary source/filter probe](../../scripts/pi_ternary_pascal_probe.py) | 3,313 | [Receipt](PI_TERNARY_RECEIPT.json): original rational recurrence, signed and positive kernel certificates, Machin bounds, dyadic differences, permutations and carry controls |
| [Carry calibration](../../scripts/pi_ternary_carry_calibration.py) | 26,165 | [Output](PI_TERNARY_CARRY_CALIBRATION.txt): exact cylinder cuts and opposite-side witnesses, biased binary probabilities and four-phase control |
| [Independent polynomial calibration](../../scripts/pi_ternary_translator_calibration.py) | 5,523 | [Receipt](PI_TERNARY_TRANSLATOR_RECEIPT.json): literal polynomial convolution, endpoint obstructions, reset sources, positive moments and28 Machin comparisons |
| [Late convex-chart calibration](../../scripts/pi_ternary_convex_probe.py) | 8,927 | [Receipt](PI_TERNARY_CONVEX_RECEIPT.json):14 integer bases, literal Newton identities, exact pair similarities, derivative truncations, inverse-chart permutations, clock composition and failed canonical product coherence |

All decisions use integers or Fraction arithmetic. Decimal strings in the
primary receipts are outward-rounded display summaries, not decision inputs.
The Machin real oracle is independently derived from alternating arctangent
series. No pi digits choose or alter the source initial condition or forcing.

The primary difference calibration covers starts0..8 and orders1..24; the
extended region covers starts19,31,64 and orders25..72. Its independent kernel
oracle has its separately recorded smaller grid and extended orders25,31,41,
56,72. Origin coefficients extend through96; full finite permutations are
checked modulo2 through1024. An early constructor valuation exploration
overlapped some extended orders, as disclosed in
[the contract](PI_TERNARY_HOLE_CONTRACT.md). This is an independent-oracle
extended comparison, not an untouched statistical holdout.

The late convex probe checks bases2,3,4,5,7,9,11,13,16,17,31,37,257,65537,
coefficients through32, all pairs among indices0..24, derivative truncations
at six specified integer arguments, and six Machin-certified source orders
through64. Normalized charts for2,3,4,5,7,11,13,16 are checked throughmod256.
Its source-index maximum is320, within the401 generated values. The infinite
analytic derivative is a paper theorem; these finite truncation checks do
not replace convergence or inverse-function arguments.

## 3. Negative controls and development corrections

The instruments preserve unfavorable conclusions:

- Dropping the real integer lift changes the quarter-filter phase by3/4;
  the independent base81 control retains its2/3 canonical phase discrepancy.
- The positive unsigned ternary transform has certified absolute error above1
  at order128. Its asymptotic divergence is proved separately.
- The biased binary law has positive collision dimension and fast carry
  synchronization but a permanent tripling one-bit defect3/26.
- P3 squared is not the canonical P9; their first Newton coefficient
  valuations2 and3 disagree. Endpoint congruences alone also fail to guarantee
  an interior kernel bound.
- The reset source preserves its source profile, but the new forcing's first
  difference has valuation2, versus0 for the original forcing.

One primary probe development run stopped before doing assertions because
direct script execution did not place the repository root on sys.path for
the inherited independent oracle import. The probe now derives its repository
root from its own path. The complete fresh run then passed all3,313 assertions.
The production module and36 unit tests were unchanged by that correction.
No failed mathematical control was suppressed or relabeled as a proof.
The first artifact-checker pass also counted a valid LaTeX row-spacing token
as a display-math opening. Restricting that check to delimiter-only lines
resolved the false alarm; that mathematical document was unchanged. A later
link pass caught unformatted multiplication-map notation as a Markdown link;
putting the notation in math formatting corrected the document link.

Two wording clarifications arose in the final same-model audit: the analytic
inverse proof calls2R a correction term because it can include a linear
coefficient; the O(k^-2) product comparison is explicitly limited to products
of the positive affine family, since the diagonal81 filter has another
endpoint contact. Both clarified statements are in the final proof.

## 4. Paper audit and classical inputs

Constructor, adversary and translator first worked from the inherited source
dossier separately. Subsequent cross-audits checked denominator minima,
uniform dyadic profiles, normalization, fixed-parameter endpoint asymptotics,
the positive reset forcing, finite lookahead, collision cross terms, and the
nonergodic residual argument. Two agents independently audited the final
root coherence proof and the late convex probe. Their verdicts were PASS
with the wording clarifications above.

These are **same-model audits, not independent external refereeing**. The
universal results have displayed mathematical proofs; finite checks calibrate
implementations and catch sign/carry mistakes. No new Lean theorem,
independence theorem, or scholarly-priority claim is made.

Primary source inputs were opened and matched to their hypotheses: DLMF's
binomial theorem, Doty--Lutz--Nandakumar Theorem4.3/Corollary4.4 for rational
affine normality preservation, Becher--Slaman for the power-base and independent-
base boundary, and Bourgain--Lindenstrauss--Michel--Venkatesh Theorem1.3 for
the nonergodic Rudolph--Johnson statement. Their direct links are in the
[synthesis](PI_TERNARY_SYNTHESIS.md). No generic positive-entropy conclusion
was substituted for the required all-scale collision/residual argument.

## 5. Repository and publication scope

The attachment was a pointer to the authentic repository; its text was read
from the supplied workspace copy. Prior conversation context, live main and
draft272 were checked. Sibling273 at
`8d89711db77fea81920321d32f831eed3dec1e68` was inspected for its history-
preservation boundary and not merged. Main remained at
`e648df3e4fca73ab6b942232b5ca4b310e9cac08` at the final prepublication check.

The new branch adds the source instruments, proof dossiers, finite receipts
and TPG claim supplement. Existing source modules, imported originals and
historical claim rows remain unchanged. Index, ledger and roadmap additions
are pointers to the new scoped claims. The final artifact audit verifies
Python compilation, local links, receipt hashes and the28 registered rows.

The work is submitted as one research draft commit stacked on272. Hosted CI
is separate from the completed local gates and must be reported from actual
returned run states. No merge, tag, release or change of historical defaults
is part of this continuation.
