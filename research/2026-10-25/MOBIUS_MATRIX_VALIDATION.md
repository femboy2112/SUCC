# Möbius matrix validation and access boundary

**Parent:** `461942c0bf616518e668d236d1c6b1596665a7dd` (PR #296).
**Working environment:** Python 3.13.5, mpmath 1.3.0, SymPy 1.14.0.
**Scope:** a locally mounted, partial source snapshot of the pinned IMW module,
its original test module, and this new additive research. This is **not a full
Git checkout**. No complete-repository, Lean, or hosted-CI success is claimed.

## Actually executed

1. Read live parent PR, AGENTS.md, METHOD.md and the π Frontier Contract through
   the GitHub connector. Inspected sibling #297's explicit matrix handoff at
   `eca4462ee4d62642b15c4af672136aa5bcacd00b`; did not import or merge it.
2. Public Git networking in the container failed DNS resolution. GitHub
   connector access worked. The two downloaded dependency texts were rebuilt
   locally and checked by exact Git-blob SHA, not assumed identical:
   - `observational_succ/succ_internal_matrix_walk.py`:
     `fa1abb9dbeee0d7b4d9972e3b0e40a5feaed3c9e`;
   - `tests/test_succ_internal_matrix_walk.py`:
     `061f587ee9ea9c6319c55b5f6051d7ac67f97dac`.
3. Baseline: **23 inherited tests passed** before the new test suite.
4. Final combined discovery in this **partial snapshot**: **64 tests passed**,
   consisting of **41 new + 23 unchanged inherited**. Raw
   [combined log](mobius_matrix_receipts/combined_tests.log) records all names
   and the actual final result. This must not be described as the full SUCC
   8,000-plus-test sweep merely because the command uses `unittest discover`.
5. `compileall` passed for the new implementation, new tests, and probe.
6. Exact deterministic receipt generation and `--verify` replay passed:
   `MOBIUS_MATRIX_EXACT_RECEIPT_VERIFIED`. The receipt records exact source,
   test and probe blob hashes and formal phase-energy hashes.
7. The diagnostic was rerun independently from the combined rational forcing;
   all **60 authentic rows and 3 fixed-counterfeit controls** matched the saved
   JSON. There are 3 training rows and 57 fresh holdout rows. All authentic
   rows passed the predeclared finite band E<=4K/N (maximum observed N E/K was
   approximately 2.70527603088); all three nonnormal-control rows failed it.
   These are 80-digit numerical diagnostics, not certified infinite bounds.
8. SymPy independently reduced the source gap to
   `(5696n^3+7672n^2+2910n+225)/(64(2n+1)(4n+3)(8n+1)(8n+5))`.
   All coefficients and all denominator factors are positive for n>=1;
   the paper proof uses that exact rational identity, not sampled positivity.

## Mathematical/control calibration

The new tests include complete small-period pole counts, p3/p5 exception
residues, product-poset inverse multiplication, exact atomic reconstruction,
all four commuting growth/restriction directions, source/anchor mutations,
integer-carry erasure, empirical noncommuting projections, exhaustive short
sign-sequence transport controls, complete balanced Boolean interactions,
primitive-clock orthogonality, missing-residue rejection, singleton overfit,
known cosine values, and exact-forcing changed-seed/fixed-nonnormal controls.

The negative empirical interaction for **authentic BBP**, N=3 and masks5/7,
is certified by rational Machin/Taylor enclosures. The same code is calibrated
on known cyclotomic cosine values. Numerical evaluation in the diagnostic is
kept separate from that interval certificate. Matrix PSD follows from an
explicit sum-of-squares derivation; formal Q[Q/Z] is not treated as an ordered
field or a complete cyclotomic quotient.

## Required gates NOT executed here

| Gate | Exact scope/status |
|---|---|
| `python scripts/verify_provenance.py` | **NOT RUN:** complete inherited repository/provenance tree not locally present. Original remote tree is retained by additive Git-tree construction, which does not substitute for this gate. |
| Full repository `unittest discover` | **NOT RUN:** only the 64-test partial snapshot is reported. Run on the full installed final checkout. |
| `python scripts/observer_foundations_probe.py` | **NOT RUN:** corresponding inherited dependency tree unavailable locally. |
| `python scripts/ordinal_succ_report_probe.py` | **NOT RUN:** corresponding inherited dependency tree unavailable locally. |
| Lean compilation / kernel proof | **NOT RUN:** no new Lean file or authority claimed. |
| Final-head hosted CI | **SEPARATE LIVE GATE:** inspect after publication; no success asserted here. Parent combined-status endpoint returned no status entries, not proof of green checks. |

Reproduction on a full checkout:

```sh
python -m unittest discover -s tests -p 'test_mobius_refined_matrix.py'
python -m unittest discover -s tests -p 'test_succ_internal_matrix_walk.py'
python scripts/mobius_matrix_probe.py --verify
python scripts/mobius_matrix_probe.py --diagnostics
# Then run the four AGENTS.md gates after matching the repository installation.
```

No source archives, original source implementations, default branches, license,
tags, releases, or existing PR heads are changed by this research commit.
Use a new non-main branch and a draft PR stacked on #296. Global claim-ID
namespaces are not modified; the descriptive local claim ledger is explicitly
scoped to this dossier and should be integrated additively by a maintainer.

**Scientific verdict:** finite instrument and paper results survive their
stated controls; empirical unordered interaction positivity is refuted;
source-selected asymptotic cancellation, π normality, and RH remain open.
