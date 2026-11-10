# Validation — three-channel phase tomography (2026-11-08)

**Local prerelease scope:** isolated Python 3.13 stdlib-only package and independent finite source-pole oracle; no hosted GitHub CI, full SUCC suite, Lean or external referee is inferred from these local tests.

Execute from repository root:

```sh
python -m unittest discover -s tests -p 'test_three_channel_prime_tomography.py' -v
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The FIRST command is the new targeted test; the others are required project-wide gates that must be separately recorded once actually executed. Exact tests compare 3-channel rational forces with original four fractions, test the full p-shell stage schedule, check predicted p-residues against an independent direct recurrence through actual denominators (including multiple r and p), and compare complete exact **residue histogram counts** to cyclic subgroup counts. Additional tests check the conditional complex Gram bound numerically against finite measured `δ_p`, the exact rational changed-seed invisibility, the Gamma-jet matched mutant's premature p-event, and a maximally coherent complementary phase control.

**Typing:** direct integer-mod-p histogram equality is exact finite mathematical evidence. Complex exponential evaluation is floating diagnostic; it cannot certify an asymptotic signed saving. Universal stage formulas and Fourier identities are proved in PROOFS; no finite test substitutes for the proof of those quantifiers.

## Balanced-epoch continuation (separately replayed)

```sh
python -m unittest discover -s tests -p 'test_balanced_prime_clock.py' -v
python -m unittest discover -s tests -p 'test_three_channel_prime_tomography.py' -v
python research/2026-11-08/three_channel_prime_tomography/receipt.py --output /tmp/succ-balanced-tcp-receipt.json
```

The added tests provide an independent full four-pole modular recurrence through every sampled balanced epoch, exact full-histogram matching, authenticated stage births, no-π-oracle dyadic anti-Haar counterseeds, rational p-unit invisibility and a signed forcing-corrected original-zero lag identity. Finite complex phase Gram values and `δ_p` are *numerical diagnostics only*; analytic BEC-03–06 theorems use PNT/AP, Gauss and Cochrane–Pinner as separately declared classical imports. Tests cannot establish a full-sequence signed covariance rate. GitHub-hosted root validation and Lean must be checked at the **new PR head**, not assumed from the local isolated run.
