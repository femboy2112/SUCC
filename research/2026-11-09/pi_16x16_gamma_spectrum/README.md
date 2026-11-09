# π's 16×16 transition matrix — complete spectrum, inverse modes, γ boundary

**2026-11-09 · SUCC draft research · π base-16 normality OPEN.** This branch extends source-exact 2-adic spatial Haar PR #566 and reads #562/#565/#560 without merging them. See [THEOREMS.md](THEOREMS.md) for full proofs and exact scope.

- Source-certified **131,072** original BBP hexadecimal digits, with two separate finite outward guards; the preceding 65,536-digit SHA matches PR #566 exactly. `CERTIFIED_HEX_131072.txt` is a finite evidence stream, not a random-digit oracle.
- Complete prior, disjoint held-out and whole-prefix **16×16 real chronological digit-pair matrices**, with row-stochastic eigenvalue spectra, 225-mode mixed Fourier projections, anti-frequency difference mode, entropy, and singular spectra, in [FINITE_SPECTRAL_HOLDOUT.json](FINITE_SPECTRAL_HOLDOUT.json).
- **Strong exact eigenvalue no-go:** a strictly positive doubly stochastic but non-Haar 16×16 matrix has exactly Haar's entire eigenvalue spectrum {1,0×15}, and even squares to Haar. Its nonzero nilpotent generalized eigenvector/singular mode hides the two-digit bias. Eigenvalues alone cannot prove normality.
- **Rigorous numeric-independent spectral bounds:** exact rational Dobrushin coefficients of the original, new and whole matrices are all <1/2; γ≈0.577 is not a nontrivial eigenvalue of any measured transition matrix.
- **Falsified holdout:** the earlier inverse-frequency excess (99.2nd percentile of 1200 matched-count shuffles) did **not** replicate (22.3rd percentile) in the preregistered unseen next 65,536 digits. No stable π signal established.
- The canonical source's Euler–Mascheroni term lives in its **infinite** harmonic/Laplace finite part (#560), not in a fixed rational finite-state transfer spectrum. An infinite-depth source-weighted spectral construction remains an interesting **UNVERIFIED** hypothesis.

Implementation: `observational_succ/bbp_spectral_gamma.py` (stdlib, exact), `tests/test_bbp_spectral_gamma.py` (root-discoverable), and [reproduce.py](reproduce.py) (opt-in full original-source replay). Validation and honest gaps in [VALIDATION.md](VALIDATION.md); next decisive source/carry tests in [NEXT.md](NEXT.md).
