# Verification / provenance report

## Tested state and source

Exact branch base: Tenacious D #571 head 1597ddab8c4dab909b84e698eb47008b5e3ae46f. Frozen A512 protocol GitHub commit **9af9f3d3106d4a05785a7cf51dc94a47781a9ad6**, created before this round inspected n>=513 source states. Earlier SUCC branches, however, already published much larger certified π prefixes (#567 up to 131,072): the A512 epoch is NOT a globally blind or newly discovered π digit holdout. Its protocol is a within-round nonretrospective measurement specification only.

Production code on GitHub imports ORIGINAL unchanged observational_succ.duck_bbp.forcing and tail_interval and the inherited #571 source_certified_digits. No source/pole/seed/archive/Lean/workflow/import-manifest/main changes.

**Isolated local Python 3.13 suite:** 23/23 tests PASS, exact source core/test import by the two files in this branch plus prior #571. One deliberately incorrect exploratory assertion about the magnitude of a wrong seed was observed FAIL and repaired to the correct rigorous 1/10<|s|<1/4; the source and main formulas were unchanged. There are no hidden passes claimed.

Local setup used a clearly marked **test-only substitute duck_bbp.py**, because this environment did not contain a full SUCC checkout. It copied the exact source polynomial and proven rational positive tail formula, not included in any commit. The identity was independently checked against original four signed fractions for n=1..512; all code and tests uploaded match the exact locally tested Git blob SHA1:

- observational_succ/bbp_parity_pressure.py: e818287a42cc9ee8cf0522fef612e116f19edf8a
- tests/test_bbp_parity_pressure.py: 70c90c9325324c7f0786c2aae4236ed3dd53cbdc
- tests/test_bbp_parity_holdout_512.py: 7f506cd31659f9d42d3f4232a1353d97557e539f

The local focused suite explicitly tests odd denominators, original zero source n=1..512, independent unwrapped Fraction recurrence, exact Q/CRT reconstruction, prime p first-shell coordinates, signed parity covariance at A32 p73/A128 p313/A256 p617, periodic/only-even/parity control, continuous-Weyl-vs-Walsh type mismatch, Fourier norm on six odd moduli, sharp integer pressure floor and nonnegative excess, odd-denominator p-integral wrong-seed behavior, source h=8 projection and original finite all-depth word counts.

## Frozen A512 internal replay

- Source times n=512..1023, 512 actual observations; p=1217 chosen by primality-only balanced ratio and fixed first-shell stage cut.
- 516 fractional digits starting at source digit time n=512 certified independently by two **algorithmic** rational approaches: (1) exact per-time recurrence plus source positive tail interval and (2) one global outward 1040-term original BBP rational interval. All digits match, SHA256 de490f103f307780a0cdc92f93a3e11873d26c71cd328d6de9b7a62f932fa58d (uppercase no newline).
- All 512 source-time parity factorizations, selected local p mean, real mean, complement mean, signed covariance, no tail boundary crossings, p support, p collision pressure, four word-pressure levels and exact source odd-denominator shadow are replayed in tests/test_bbp_parity_holdout_512.py.
- Fixed local tests and the 512 replay together: **23/23 PASS**, includes 5 explicitly heldout replay tests.
- Full 12k+ native SUCC suite/provenance/foundations/ordinal/Lean on the exact new final head were NOT independently executed locally. Check the actual final-head hosted workflow status; do not replace checks with claims.
- Standalone exact modular tests and finite arithmetic establish observed identities; they do not certify unbounded p_A, original zero-selected o(1), global π normality or scholarly novelty.

## Independent input boundary

#554 BEC03..06 and Cochrane–Pinner finite-field estimates are imported as conditional mathematical hypotheses, NOT independently proved or formalized here. Their uniformity in p-dependent additive frequencies matters to PPP-04. No new signed all-epoch zero-seed covariance estimate is claimed. Same-model scientific review and this second rational algorithm are not independent mathematical witnesses.
