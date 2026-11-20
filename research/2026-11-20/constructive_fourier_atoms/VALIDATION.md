# Validation and precise authority — Constructive Fourier Atoms

## Executed locally on final candidate bytes

Working folder: `research/2026-11-20/constructive_fourier_atoms/` on a **new research-only draft branch**. Commands executed on the exact working files before GitHub upload:

```sh
python -m unittest discover -s . -p 'test_causal_fourier.py' -v
python independent_audit.py
python -m compileall -q causal_fourier.py test_causal_fourier.py independent_audit.py
```

- **25/25 scoped unittest methods PASS** (0 skips, failures, errors).
- **Independent SymPy/mpmath audit PASS**. `independent_audit.py` uses no imports from `causal_fourier.py` and reconstructs original BBP four poles, Mellin polynomial `Q=(1−t)H`, first-two-atom gap coefficient `2491/12579840`, complete 3/5 finite clock tables, odd-prime valuation identities and the original-vs-mutant prime-square residues using separate arithmetic and numerical representations.
- Audit counts: **5,303 clock/valuation exact assertions**; **244 prime-square authentic-vs-mutant exact residue assertions**. Four Mellin–Fourier integral vs 67-term causal-source series comparisons at 75 decimal digits have absolute differences below `1.1e−75`; a separate `π/16` evaluation at zero frequency passes its declared precision threshold.
- Standard library module, unittest module and optional audit compile without errors.
- Local Markdown relative links and JSON receipt parse are checked during packaging. SHA-256 per file and GitHub blob readback/check of the final commit should be recorded after publication; never infer verification merely from a create-file success message.

## What the tests cover

`test_causal_fourier.py` tests the exact radix-16 successor, p=3/5 LTE isometries, complete CRT clock cycles, finite inverse clocks, Fourier eigencharacters and orthogonality, exact **unitary** clock-to-state basis change, counterexample to naive additive-state eigenfunctions, the 2-adic attractor and 2-adic clock noncontinuity, rational product formula, original BBP source poles, source-time positivity/gap/variance controls, source-seed blindness, matched-jet mutant, exact affine phase products, order-sensitive frequency transport, finite source/tail compensation, locked counterseed, terminal error, radix Koopman frequency dilation, and unwrapped seed aliases.

The external audit independently checks source formula/pole polynomial and numeric Mellin–Fourier integral at selected frequencies. It is not an independent mathematical referee, a proof assistant, or an asymptotic π-shell experiment.

## Deliberately not executed / not claimed

- `AGENTS.md` mandatory inherited root test suite (`~14k` tests): **NOT RUN** (the full repo was not cloned; network-disabled container).
- `python scripts/verify_provenance.py`, `python scripts/observer_foundations_probe.py`, `python scripts/ordinal_succ_report_probe.py`: **NOT RUN** (the full repo was not cloned). No protected paths were modified.
- Hosted GitHub CI, independent human referee, Lean kernel checking: **NOT CLAIMED**.
- New certified late π-shell holdout, universal signed all-shell estimate, R0, π normality, RH: **NOT RUN/NOT PROVED**.
- Any physical energy, real-world nonclassical coupling or intervention: **NOT TESTED**.

## Reproduction

Tests are deterministic and require Python 3.11+ standard library. Optional independent audit requires SymPy 1.14 and mpmath 1.3. Its original source formula is independently reconstructed within the script. Reproduce with the commands above from this directory. The exact raw unittest output can be regenerated; `independent_audit_receipt.json` is committed as a replayable, scoped receipt.

**Authority:** elementary/classical paper proofs for CFA-01–09; local executable finite calibration of the implementations; CFA-10 entirely unverified. No finite test is used to assert a universal theorem about π digits.
