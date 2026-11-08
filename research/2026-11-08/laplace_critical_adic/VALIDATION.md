# Validation — LAPLACE CRITICAL (2026-11-08)

## Reproducible local scope

- Environment: Python 3.13.5; mpmath 1.3.0; SymPy 1.14.0 present but not used by new source mathematics. Original SUCC main GitHub source read-only, pinned Main XXI `43a607818907120d4cdab73d240f5b4d7700b63f`. Parent PR #558 `46b96e61ea8a309546b399da328c9bfcc077ada2`. The full Git repo cannot be cloned here (DNS/network unavailable); no full >12k native suite, provenance/observer/ordinal gates or new Lean kernel run is claimed.
- New tests: **23/23** methods PASS. Combined local with archived #556 and #558 research tests: **56/56 PASS**, including original-source exact Fraction, cofactor p-character, source clocks and adversarial counterseed controls. Complete raw output in `LOCAL_TEST_LOG.txt`.
- Local test fixture: a minimal API-compatible `observational_succ.duck_bbp` source was used in the isolated tree and checked against an independently reassembled original four-pole Fraction formula. **This fixture is NOT published/committed**. The committed new module imports canonical `observational_succ.duck_bbp.forcing` and #558's `adelic_additive_gluing.local_additive_fraction`.
- Commands: `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v`; `PYTHONPATH=. python research/2026-11-08/laplace_critical_adic/receipt.py --verify`; analogous `spectral_receipt.py --verify`; `python -m compileall -q` on the four new Python files. All successful; initial rough draft tests included an incorrect test expectation `2.001 exp(-N/A)` for a rigorous tail whose exact prefactor is `2t/(1−exp(-t))>2`; the test was repaired to `2(1+t)exp(-N/A)` and passed. The mathematics/implementation of the tail budget was unchanged.

## Frozen fresh numerical probe

`PREREGISTRATION.md` was the branch's **first commit**, before evaluating the new source-only critical Laplace probes. It specifies A=160,320,640 and lambda=1/64,1/8,1 (nine cases). `FINITE_RECEIPT.json` records their exact integer h=lambda*A², N=18A, 60-digit complex values from a *separate four signed-pole source formula*, double-precision implementation comparison below 3.3e-15, and a rigorous **truncation** bound <=3.06e-8. The complex numerical phase evaluations are **not outward-rounded interval certificates**; all finite numbers are finite diagnostics. No finite trend validates the universal limit, which is proved separately in `THEOREMS.md` using dominated convergence.

## Preseen spectral diagnostic

`SPECTRAL_DIAGNOSTICS.json` replays A=32,80,192,320 with primes 73,193,457,769. Those epochs were seen in PRs #556/#558, so they are explicitly PRESEEN, not independent holdouts. The fraction readouts use the original zero-seeded four poles and p-adic fractional parts; discrete time Fourier computations use Python complex double. `K=8` complement high-mode energies are 0.3402, 0.7943, 0.9273 and 0.9376. These make the naive **absolute high-energy decay** route unattractive, without refuting its asymptotic hypothesis. All signed overlaps are computed with cross terms; no false independence assumption.

## Proof authority / remaining debt

- All new asymptotic theorems are **paper derivations** with elementary calculus, exact Fraction identities and classical DLMF/Gamma/Abel inputs. No new Lean formalization or external scholarly referee; no proof-of-priority claim.
- Existing #496 already establishes the bounded Abel/Cesàro bridge; #554's prime prefix estimate is a **declared, separately imported conditional** input, not re-proved by the local DFT test.
- π base-16 normality, genuine original-zero signed Abel residue, signed high-spectrum overlap decay and RH all remain **OPEN**.
- Source / test SHA256: `c1b71f7d3ed15eac0a74b9f1b6fb7544f88ab3db40af13db84addd0fb3238a1b` / `98d24a733a2ebc7fe4bd36cf8dea6da59fa30557aa04c8e2b1b5a312aa98c12e` at tested snapshot. Publication Git blob identities must be rechecked after push; do not claim it beforehand.
