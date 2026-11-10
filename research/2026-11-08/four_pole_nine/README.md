# Operation FOUR-POLE NINE: 3–4–5 pole triangle × nine-channel algebra × source-selected π

**Draft research on SUCC Main XXI (`43a607818907120d4cdab73d240f5b4d7700b63f`), 2026-11-08.** Frozen BBP source and literal zero seed unchanged. **π base-16 normality OPEN. RH OPEN.**

The user's `four signed poles -> three relative channels -> 3²=9` idea has three **different** exact realizations, plus one important firewall:

1. **Positive 3–4–5 arithmetic source:** `r(n)=6/[a(a+3)]+4/[a(a+4)]+5/[a(a+5)]`, `a=8n−7`. The offsets form a Pythagorean right triangle; the fixed-multiplicity integer template is **uniquely** determined by its first two jets `(15,59)`. Three scalar source clock readouts recover all three coefficients by an invertible Cauchy matrix.
2. **Genuine 3-torus arithmetic phase:** the original zero-seeded orbit is the sum of three positive component recurrences, so the π Weyl mode is their **third-order diagonal Fourier character**, with a three-valued real carry seam. The `d=3` and `d=5` components are each 2-adically half-integral but pair to an integral original source and history. **Pairwise nine-entry information alone does not determine the third-order phase**: a finite exact roots-of-unity countermodel proves it.
3. **Nine-dimensional real operator algebra:** the balanced four-pole coefficients span a three-dimensional hyperplane. Its endomorphisms split `9=1+3+5` under an explicitly chosen Euclidean metric. A source-clock projection produces a **strictly nonzero, exact, rank-two skew chronological commutator** with a rational Vandermonde norm and `O(a^-6)` asymptotic. It is a **source-position observer defect**, not a verified signed π cancellation estimate.
4. **Authentic golden correction, not an invented 1/9 explanation:** the universal Gamma(2) disk response `|(2−e^{iθ})^{-2}|=1/(5−4cosθ)` has sharp floor `1/9` even for a TWO-pole source. The exact original source's continuous-clock mixed-Poisson fixed point instead has a **source-specific golden drift** `q_a=φ^-2+59(5−√5)/(150a)+O(a^-2)`, fixed by its `(15,59)` pole jets. This makes the source visible beyond its universal Gamma limit but does not give real signed cancellation.

**Research objects:** [full paper proofs](PROOFS.md) · [claim ledger](CLAIM_LEDGER.md) · [next theorem](NEXT.md) · [validation](VALIDATION.md) · [exact symbolic receipt](INDEPENDENT_EXACT_RECEIPT.json) · [finite signed diagnostics](FINITE_SIGNED_DIAGNOSTIC.json).

**Source and tests:** [`observational_succ/four_pole_nine.py`](../../../observational_succ/four_pole_nine.py) and [`tests/test_four_pole_nine.py`](../../../tests/test_four_pole_nine.py). Standalone symbolic oracle and finite probe are in this directory; no archived imported source, `formal/`, provenance, workflows or main-facing indexes were modified.

**Reproduce:**

```sh
python -m unittest discover -s tests -p 'test_four_pole_nine.py' -v
python research/2026-11-08/four_pole_nine/independent_sympy_oracle.py
python research/2026-11-08/four_pole_nine/finite_signed_probe.py
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
# Full root suite (run separately against a stable exact branch checkout):
PYTHONPATH="$PWD" python -m unittest discover -s tests -p 'test_*.py'
```

The local isolated source package has no full SUCC worktree; root provenance/foundation/ordinal/full-suite and hosted CI must be recorded as **unrun** until independently executed. The exact SymPy oracle and root-discoverable focused tests were executed locally. No source-selected all-epoch covariance saving is claimed.
