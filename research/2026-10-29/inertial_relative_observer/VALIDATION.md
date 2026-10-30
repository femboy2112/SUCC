# Validation / reproducibility / trust boundary

**Research date:** October 29, 2026. **Parent exact source:** SUCC draft PR #375 `bcc86f1f5edcb9696ae11451fb6dffede1530434`, which inherits signed original #371/#370 and the prior original BBP source; separate sibling PR #373 reviewed read-only. This research changes **no** original forcing, archived source, source manifest, FQID/claim namespace, production code or CI workflow. It is additive only. **π-normality and RH remain OPEN.**

## Executed, exact local scope

| Run | Actual result | Source and receipt |
|---|---|---|
| Exact standalone source probe | `RELATIVE_PROBE_STDLIB_PASS` | `relative_observer.py`, [`source_probe.log`](source_probe.log) |
| Full **available staged research** unit discovery | **66/66 PASS**: 32 inherited #375 archive tests + 34 fresh `test_inertial_relative_observer.py` checks; Python 3.13.5 | [`stdlib_staged_tests.log`](stdlib_staged_tests.log) |
| Independent mpmath oracle | **PASS** at **210 decimal digits**, original rational polynomial A/D, 4-pole partial fractions, independent Green tails, uniform-in-lag bound, pure lacunary phase comparison, modular energy, coherent source controls, Gamma/digamma closed memory, direct BBP rational integral, selected golden memory point and non-invariant aliases | [`independent_oracle.py`](independent_oracle.py), [`independent_oracle.log`](independent_oracle.log) |
| `python -m compileall -q research/2026-10-29/inertial_relative_observer tests/test_inertial_relative_observer.py` | exit code 0 | Python 3.13.5 |
| Original source mutation/alias controls | EXACT: original 4 poles (Fraction), one/multilag recursions, `0` versus `1/15`, later `1/240`, source reorientation, source clock `15`, rational future tail intervals and pi/16 enclosures | Scoped tests (not independent arithmetic source witnesses) |
| Independently evaluated source first-correction constant | 210-digit agreement of **three methods**: Gamma/digamma, original rational integral and 16-adic Green tail | Note: all three still ultimately share the same four-pole source; they are not three source-independent witnesses |

**Environment:** See [`PYTHON_ENV.txt`](PYTHON_ENV.txt). A complete live SUCC checkout was unavailable (GitHub host DNS from local runtime failed). Instead the 17-file research archive of parent PR #375 supplied only its exact earlier staged research/probe/tests, not all repo dependencies. The root `AGENTS.md` gates (`verify_provenance`, full native unit discovery, observer and ordinal probes), math-memory catalog checks, Lean, hosted exact-head CI and external peer review **WERE NOT RUN OR CERTIFIED by this staged local execution**.

## Corrected provisional oracle runs (not hidden)

- Initial 120-digit `mpmath` calculation compared two huge algebraically equivalent unwrapped values at n+k≈50 to absolute tolerance `1e-70`. Numerical cancellation left a residual `~4.6e-69`, an over-strict precision setting for that implementation, **not a mathematical counterexample**. Re-run at 210 digits with a deeper 165-step Green tail; independent oracle passed.
- The golden-weighted memory series initially stopped at 179 terms but was checked against a `1e-145` absolute tolerance. Its genuine positive omitted tail was about `4.5e-82`. Corrected the finite cutoff to 240 terms with tolerance `1e-105`; the independent integral matched within this properly declared truncation budget. These numerical runs have **no authority over the infinite exact theorem**.

## Scoped logical authority

- **Proved paper (classical ingredients):** circle-source covariance, 15-torsion quotient, all-lag finite rational recurrence, asymptotic invariant-measure rigidity, true relative normality criterion, Green-tail telescoping bound, exact Gamma/digamma memory constant, complete relative Eisenstein energy. Each proof and domain appears in [`README.md`](README.md).
- **Tested:** finite exact identities, independent high-precision integrals, finite source energies and hostile changed seeds. These are finite computations and do not imply anything about the actual unknown infinite Fourier limit.
- **Still UNVERIFIED:** a new signed `o(N)` Weyl estimate on the original zero-seeded BBP source, actual π-normality or nonnormality, independent scholarly novelty, kernel formalization, physical implementation of the hypothetical absolute-origin-free sensor.

## Review-before-merge and repository safety

Work on a non-main branch and review as a **draft PR**. Preserve the parent head, immutable historical four-pole source and `U0=0`, recorded counterexamples, and math-memory claim authority. The file hash manifest [`STAGED_RECEIPT.json`](STAGED_RECEIPT.json) pins all newly created research and executed source/test/log content; actual remote blobs must be checked after GitHub commit. Do not confuse a committed test transcript with hosted-CI success.
