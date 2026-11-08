# Validation and provenance

Starting research pin: `525d7c87dd1016aeeea4ac9cd1366cbb935a0441`.
Read-only fetched main: `43a607818907120d4cdab73d240f5b4d7700b63f`.
Only this directory was edited by the archive/crucible front.

Executed successfully from the repository root:

```
python research/2026-11-08/frontier_connections/crucible/qco_oracle.py --output research/2026-11-08/frontier_connections/crucible/ORACLE.json
python -m unittest discover -s research/2026-11-08/frontier_connections/crucible -p 'qco_oracle.py' -v
PYTHONPATH="$PWD" python research/2026-11-08/frontier_connections/crucible/source_quotient.py
python research/2026-11-08/frontier_connections/crucible/energy_review.py
```

The first source replay failed before computation: an inherited module had
put its own `oracle.py` earlier on `sys.path`, so importing `cosets` selected
the wrong module and raised ImportError. The local module was renamed
`qco_oracle.py`; the replay then completed with exit0. This was a module-name
collision, not a changed mathematical source or a discarded adverse result.

Six focused unit tests passed. The exact-count oracle and nine-case
independent de Bruijn oracle both passed. The source replay recomputed four
complete affine DFTs,26,324 coefficients, with inherited integer error
radii; all32 slope-orbit sums and four retained coefficients contain their
direct interval predictions. `SOURCE_QUOTIENT.json` hashes the exact input
source receipts and replay code, and retains unwrapped-state/carry hashes.

Independence: exact coefficient-count identities use no phase evaluator or
FFT; the de Bruijn oracle uses a separate Euler-circuit construction. The
source replay shares prior interval phase/FFT code and the existing source
boxes, and is explicitly **not independent source evidence**. All agents
share a model family. The paper proof supplies universal quantifiers;
finite cases check implementations and falsifiers only.

Root owns aggregate validation and publication. This front did not run the
native full suite or new Lean checks and makes no hosted CI claim.
