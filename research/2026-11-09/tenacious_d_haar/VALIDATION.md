# Validation, source binding and exact proof scope

**Local isolated execution (Python 3.13):** PYTHONPATH=. python -m unittest discover -s tests -p 'test_haar_successor_junction.py' -v gives 15/15 PASS after correcting one *test expectation*: the all-zero path's j=1 gradient seam is 30, not zero. The failure and correction were preserved in the research process; no theorem was changed.

The **exact committed Git blobs** for production module and test file matched the original locally tested bytes: source 1e3eb3bbbd98f83055d9dba549da0e372acd5df5; tests 4d56e41d1cd671b8d1ba0c609a4fef36cef35974. The exact-source test fixture is **NOT committed**.

**Fixture disclosure:** the local isolated test environment did not contain the whole SUCC checkout. Its test-only duck_bbp.py fixture copied just the canonical original forcing polynomial and rational tail interval; its two formulas were checked against the independent four-signed-pole partial fractions and the canonical core retrieved from main. On GitHub, committed code imports the production observational_succ.duck_bbp (source sha 34cb7b64f6975e05586ec220a4655961a8e7b636). No test-only duplicate was pushed. Source unchanged.

**Tests and controls:** source poles n=1..199, original first 18 outward-certified hexadecimal digits of pi, real source intervals at A=16,N=64 and A=32,N=128, independent finite Fourier DFT, exact rational L2/gradient/seam energies, outgoing rational W1 square-root bounds, shifted-sample endpoint correction, constant-zero path, period-16 false one-digit Haar, periodic de Bruijn(16,2) false two-digit Haar, alternating h=8 sharp upper successor inequality, exact dyadic source counterseed at A=64 with 68 zero digits via 105-term source tail, sampling lower bound, temporal SUCC vacuity, invalid inputs.

**Exact versus approximate:** Fraction checks and isqrt square-root upper bounds are exact. The one complex-character DFT test is an independent floating diagnostic (tolerance 1e-10), with mathematical Parseval separately proved. Decimal W1 displays are diagnostics from rational midpoints, with outward source half-widths recorded. No extrapolation from finite numbers.

**Not yet certified by this file:** full native test suite, root provenance/foundation/ordinal probes, Lean formalization, scholarly priority, or external referee. Check live hosted workflows on the exact branch/PR head separately and state their results as they actually finish.

Main and pre-existing provenance, formal and archive files untouched; new source code and tests are additive only.