# Reproducibility and scope — origin spectral fingerprint

**Scope:** research added to a new draft stacked on #554. No imported archive, old proof, main branch, old receipt, frozen formula, or workflow modified. Base #554 head pinned `90711d2e9dc73020acbc4cde1ad058b62ef54a4d`; verify parent again before merging. This standalone research module uses only Python stdlib `fractions`, `cmath`, `math`, `collections`. It never supplies π digits as inputs.

## Run focused checks from a SUCC checkout

```sh
python -m unittest discover -s tests -p 'test_origin_spectral_fingerprint.py' -v
python research/2026-11-08/origin_locked_spectral_fingerprint/receipt.py --verify
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

Only the **focused suite and receipt** have been executed locally on an isolated research package; the other root commands require a complete SUCC checkout and must not be preclaimed. Hosted GitHub workflows are separate exact-head evidence.

## Independent mathematical controls

- Original four poles evaluated both as four signed fractions and as the independent reduced rational polynomial, exact Fraction equalities. A separate independent SymPy calculation verifies the altered forcing numerator is a polynomial in `(n-1)` with coefficients `[956160, 6481248, 18115920, 26982632, 23101644, 11385848, 2998376, 326148]`, all positive, over a denominator positive at every integer `n>=1`. This is an extra symbolic confirmation, not the source of the paper positivity proof.
- All finite path/origin invariants checked for positive/negative rational seeds and several time/future splits, without π as a numerical oracle.
- **32-digit independent validation:** exact rational original-BBP interval, from positive Q(x) and green tail, overlaps an independently evaluated rational Machin identity `π/16=atan(1/5)−atan(1/239)/4`. Both certify the same base-16 cylinder. This is a digit certificate, not a normality test.
- Finite periodic sidebands q=1/5,1/7,1/17,1/257; exact rational exponents, complex DFT inversion and Parseval tested with declared floating tolerance (not interval certificates).
- Exact rational 257-primary mutant source fingerprint. Mutant source positivity is proved for **all n** in THEOREMS, not inferred from 200 finite test rows.
- The `E_2−E_1` digit energy is independently checked as an exact Fraction conditional-square sum, and finite complex Walsh Plancherel is a numerical cross-check; the periodic simply-normal countermodel has maximal two-digit line.
- Critical spectral contrast: exact phase rational inequalities on multiple epochs and the independent **all-A paper proof** `Re D_A≤13/16` for all A≥24, with explicit continuum transport error ≤5π/A. Floating critical Fourier sums only corroborate.
- Source-changing null coboundaries and rational seed shifts are **different controls**; no unintended source replacement is claimed.

## Important negative checks

- The arbitrary-real-seed coherent completion `s*=−π/16` kills any seed-blind normality inference; source invariant P survives but completed α changes.
- For each finite A, a rational counterseed constructed from **only the actual source partial sum** `s_M=−P_M` makes the observed epoch almost coherent, despite exact same four poles and p-primary source component. This does not disprove the actual zero-seed normality conjecture.
- A different positive rational source can have exact same P and the same asymptotic zero-seed normality verdict, proving the necessity of source-local authentication beyond digits.
- A fixed finite hierarchy of digit Walsh modes cannot prove normality, and a source-space model fingerprint at frequency ~A² does **not** bound any of #544's fixed-h original real signed sums.

**Ledger authority:** Paper theorems and exact algebra are derivations to review; finite outputs are `OBSERVED FINITE`; classical Wall and finite Fourier are external sources. No Lean kernel checks or external scholarly review of these new statements. Claim labels in CLAIM_LEDGER.md.
