# Γ16 validation and provenance boundaries

**Input:** 40,960 previously source-certified hexadecimal fractional digits of π from SUCC #561/#565, re-used verbatim, SHA-256 including newline `c4010a291cf411147dd1a6a65104bd4cf995a4d931b6dfefb9fd9277f8434527`. No new digit extraction or fresh holdout; not an independent proof of BBP itself. The scalar count matrix is directly calculated from the archived bytes, not copied from a prior theorem statement.

**Added implementation:** `observational_succ/bbp_gamma16_matrix.py`, standard library only, no original source changes. It imports frozen `duck_bbp.forcing` only for two-step source checks and frozen `balanced_prime_clock` for optional prime-stage labels. The independent plotting/oracle scripts use NumPy/SymPy from SUCC's declared `research` extras. The standalone focused unit tests are `tests/test_bbp_gamma16_matrix.py`.

Reproduction from repo root (Python >=3.10):

```sh
python -m unittest discover -s tests -p 'test_bbp_gamma16_matrix.py' -v
python research/2026-11-09/gamma16_yoneda/experiment.py --output /tmp/succ-gamma16-replay.json
python research/2026-11-09/gamma16_yoneda/independent_oracle.py
PYTHONPATH=. python research/2026-11-09/gamma16_yoneda/plot_matrix.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

**Local isolated validation actually executed:** 25 focused tests pass, Python 3.13.5; independent NumPy fft2 vs direct finite character expansion and independent SymPy g=1..4 source endpoint jets and g=2 original rational pole regrouping pass. Deterministic experiment receipt generated twice and compared byte-for-byte. Source numerator equals original four signed fractions on tested times, but the offline scratch copy of `duck_bbp.forcing` is an *exact formula test-only stub*, **not** an independent native repo suite. The repo head's full required test/provenance/Lean/hosted CI has NOT been executed locally; check the exact hosted PR SHA before claiming a full-suite pass. Reused data and same-model tests are not blinded independent witnesses.

**Exact vs diagnostic:** The 16×16 integer counts, orthogonal Frobenius-split energies, prime-stage variance, grouped source pole identities and q-Gamma polynomial recurrence are exact. Complex Fourier-mode magnitude, plotted heatmaps, NumPy FFT and high-order condition numbers are float diagnostics. Classical DLMF q-Gamma recurrence is an external input, independently linked. A positive Laplace matrix/gamma limit never certifies selected real signed decay.

**Important deliberately retained failed command:** the first direct execution of `plot_matrix.py` without `PYTHONPATH=.` failed to import the root package; rerunning with the documented path succeeded. A second attempt handed a NumPy-integer matrix to the strict exact integer API, which correctly rejected its non-built-in integer types; the script now retains the original built-in integer counts for the theorem and converts only for display. These are environment/type errors, not mathematical failed theorems.

**Figures:** `pair_counts_16x16.png` and `fourier_modes_16x16.png` show **reused finite data**; they are not proofs or independent experimental samples.
