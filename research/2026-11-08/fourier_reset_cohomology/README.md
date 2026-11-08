# Operation Fourier–Gamma Return / BBP word spectroscopy

**Status:** genuine finite integer/Fourier theorems, original zero-source finite observations, and classical iid reference theorems. **π base-16 normality OPEN; original real signed covariance OPEN.** Do not infer a physical feedback mechanism from an exact normalization identity.

This round tests the user's conjecture that the signed interference of BBP digit patterns might become more tractable in its *own arithmetic Fourier space*, and asks whether the statistical walk ever exactly returns to zero.

**Principal finding:** the digit-character Fourier algebra has primitive conductor/rank levels `(2,1), (4,2), (8,4), (16,8)`. The first 16,384 previously certified original-source π digits exhibit **157, 5, 0, 0 exact spectral returns**, respectively. The full 16-bin imbalance has **zero exact full returns** on the same prefix. This is compatible with the iid reference: low-dimensional simple walks recur, higher-dimensional walks are transient. **No iid hypothesis about π is asserted.**

**Real transform:** word-character step functions on the circle have real Fourier support on an explicitly determined base-16 congruence class. This bridges digit-word Fourier analysis with ordinary ×16 orbit Fourier modes. The remaining source-specific cost is the tail of the sharp digit step-function spectrum and visits near radix-cell boundaries.

**Energy transform:** `E_k-E_(k-1)` splits exactly into **four nonnegative primitive conductor sectors**; the cyclic sliding-word counts are a divergence-free de Bruijn circulation, with exactly `16^k-16^(k−1)` zero-mass degrees of freedom. Those facts reveal the natural representation and remove redundant coordinates but do **not** prove signed long-term cancellation.

**Gamma:** the iid order-four (rank-two) return law has an elliptic generating function and exact sharp finite part `(EulerGamma+log16)/pi`; it is the *critical reference layer*, not the original BBP phase selected by U0=0.

- [Full theorem dossier](THEOREMS.md)
- [Evidence and controls](FINITE_RECEIPT.json)
- [Claim ledger](CLAIM_LEDGER.md)
- [Validation](VALIDATION.md)
- [Next falsifiable probe](NEXT.md)
- Focused local validation: **19/19 passed**; full checkout/root/hosted tests pending.

- Run `PYTHONPATH=. python -m unittest discover -s tests -p 'test_bbp_word_spectroscopy.py' -v`.
- Run `PYTHONPATH=. python research/2026-11-08/fourier_reset_cohomology/experiment.py --n 16384 --shuffles 16 --out /tmp/fourier_reset.json` using the inherited certified digit file.

**Original four BBP poles and the literal zero seed are frozen; this PR changes neither main nor #544/#557.**
