# Validation receipt (local, research-draft only)

**Source:** exact local research files in `research/2026-10-30/prime_stroboscope/` over merged Main XVI `e18ba565ca540adb7edf3292f5593929e76d91c5`. Exact remote Git blob identity must be checked after upload. No publication, main merge or hosted CI claim.

## Executed

- `python -m unittest discover -s . -p 'test_*.py' -v`: **15/15 PASSED**, raw output in `focused_tests.log`. Covers source pole passport, both prime classes, 4 collision p-residues, prime clock exactness, coefficient involution, mutation/no-uniqueness controls, exact CRT decomposition, p=73 numerator cancellation, p-integral seed blindness, complete p-period, and finite selected-π occupancy.
- `python independent_oracle.py`: **PASS**. Distinct exact big-Fraction recurrence + event-sum source calculations, 46 authentic `(p,k)` cases; 3 coefficient families -> **138** independently cross-checked modulo-p equalities; five CRT decompositions. Raw output `independent_oracle_receipt.json`. This is independent *implementation*, not independent reasoner or peer review.
- `python selected_occupancy.py`: EXACT Fraction certificate for 256 pure π hexadecimal bins, `finite_selected_occupancy.json`. **0 ambiguous at grid 16**, counts `[17,18,18,15,14,12,16,18,19,24,13,13,14,16,13,16]`; **2 ambiguous at grid 256** under same simple Green-tail bound (n=1,2). Independently checked all 256 grid-16 labels against `mpmath` π at **410 decimal digits**, 0 mismatches; numerical cross-check is not the source of the exact certificate.
- `python -m compileall -q prime_stroboscope.py test_prime_stroboscope.py independent_oracle.py selected_occupancy.py`: **PASS**.
- External mathematical inputs: original BBP formula, classical Euler criterion + quadratic reciprocity `(2/p)`, Fermat's little theorem, CRT and Dirichlet progressions; no unpublished external theorem treated as proven from test output.

## Not executed / not warranted

- Repo-wide commands `python scripts/verify_provenance.py`, full `python -m unittest discover -s tests -p 'test_*.py'`, `observer_foundations_probe.py`, `ordinal_succ_report_probe.py` (requires independent full repo workspace and validation).
- Exact-head GitHub Actions and new Lean kernel proof.
- Blind independent mathematical referee or theorem-priority/novelty certification.
- Infinite signed cancellation or all-horizon arc occupancy of π.

An important negative control is `p=73,k=4`, where the earlier source prefix numerator contains p and the remote selected rational denominator loses the expected p conductor. Another is an altered four-pole vector preserving the ratio A=-4C, which survives the modular shadow and therefore blocks any claim of uniqueness of the original BBP source from this condition alone.
