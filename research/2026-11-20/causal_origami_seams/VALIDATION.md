# Validation receipt: causal origami seam research

**Scope:** exact finite tests of the **new research directory only**, no other SUCC code edited. Parent assumed pinned #676 `c910be34f935be7b3c1c4c6344648a5b5ca9d34a`. Validation happened in an isolated local Python container; full SUCC repo not checked out. Claim statuses depend on the proofs in THEOREMS.md, not on finite test counts.

## Executed clean final commands

```bash
python -m compileall -q seam_model.py test_seam_model.py independent_audit.py
python -m unittest discover -p 'test_*.py' -v
python independent_audit.py
```

- **Focused stdlib unit tests: 32/32 PASS**, `0.018 s` (local `focused_tests.log`; independent machine times vary). Main fixture families: exact prime clocks, original and mutant first-pole p-primary marks, gap-Hankel determinant and future-robust anti-diagonal, rational-weighted Hankel, original BBP forcing and tail, exact analytic-backward-shift, finite root Fourier alias, full/separating and incomplete observational quotients, source-seed circle alias and append-only origami inverse.
- **Independent SymPy/mpmath oracle: PASS**, with **28 exact original/mutant p-primary assertions**, **12 exact gap-Hankel determinants** for markers 1,4,5, **5 high-precision analytic Mellin-germ versus independent source-series comparisons**, **15 high-precision finite root-of-unity DFT inversions**, **4 finite Bertrand-style prime-interval calibrations**, and **one source-tail asymptotic jet** (f(1)=1, f'(1)=2, n^-3 coefficient −7/512). 105-digit working precision. Numerical tolerances were specified as `<1e-98` in the code; the script executed all assertions and saved raw error magnitudes to [independent_audit_receipt.json](independent_audit_receipt.json).
- **All three research Python files compile.** `independent_audit.py` does not import `seam_model.py`; tests and independent audit use different algebraic implementations. They were authored by the same model, **not blinded independent referees**.
- **Internal relative Markdown links** are checked; backlinks to other repository areas were inspected at their cited paths in prior GitHub reads. Inline code such as `G_n^[M](z)` is not a Markdown hyperlink. No external tests/CI/formal proof runs claimed.

## Development-time repaired failures (retained as audit notes)

1. Initial trial fixture mistakenly listed the prime 31 clock as 127; exact formula gives `(31²+7)/8=121`. Corrected the expectation; the source routine was right.
2. Initial Bareiss implementation coerced rational Hankel entries to `int`, turning `4/p²` markers into zeros. Repaired it with exact common-denominator clearing before integer elimination. Independent SymPy oracle now certifies matching rational and integer source-mark cases.
3. Initial standalone audit used an invalid no-argument SymPy `Rational()` as a summation zero. Corrected to `Rational(0)` before the clean, complete audit.

These failures were **tooling/fixture defects**, not refutations of the mathematical theorems; final successful tests were rerun after fixing them. No unrun historical test is represented as passing.

## Theory-versus-test firewall

**Proof-based statements:** final coalgebra uniqueness (classical), quotient action-graph conjugacy, Hardy backward shift, original four-pole Mellin tail, two-term asymptotic, exact Fourier alias, prime-square determinant, infinite Hankel rank and autonomous state lower bound. The latter uniform Ω(√N) argument uses the classical Bertrand postulate; it was not reproved or machine checked.

**Imported theorem:** Fabry gap theorem ⇒ natural boundary of the source-selected prime-square projection at its exact radius. Finite tests cannot verify a natural boundary, and no claim of a first-principles new proof of Fabry is made.

**NOT run / NOT claimed:** SUCC's full >14,000-test inherited suite; `scripts/verify_provenance.py`; `scripts/observer_foundations_probe.py`; `scripts/ordinal_succ_report_probe.py`; hosted CI, Lean, external referee, full BBP source external physical verification, all-shell signed π saving, π base-16 normality, RH or any quantum / thermodynamic interpretation.

## Reproducibility and scope hashes

The independent audit receipt contains SHA-256 digests of `seam_model.py`, `test_seam_model.py`, and `independent_audit.py`. At publishing time, all remote GitHub blob SHA-1s must be checked against `git hash-object` of the exact locally tested files. Validation of the new directory does not certify the entire ancestor PR stack.
