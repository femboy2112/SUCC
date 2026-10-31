# N/Z carrier research validation — 2026-10-30

## Baseline and provenance

Live main verified at `e18ba565ca540adb7edf3292f5593929e76d91c5` (Main XVI). Recent draft PR #415 `f650aab0c8710b502f3e08ec1cb2b351c26b2b3f` (Codex), #414 `e4773979802cf0ef3a8d46444acb6bc5966788a9` (observer/carrier), #413 `f316d1b1e87291a89c4d4034ccf27a947e7088ad` (Fibonacci), #410 `5a54cd1a4200f3b0e673f6c3feecff76bf6b6dc6` (DeepSeek) read/reviewed as distinct unmerged inputs. `docs/OPERATIONAL_TRIANGLE.md` and `AGENTS.md` on main read. No other branches have been merged into this universal carrier research.

## Exact tests and independent checks

From this directory:

```sh
python -m unittest -v test_carrier_probe.py
python independent_oracle.py
python verify_manifest.py
```

- **24/24 focused exact Python tests PASS**, output `tests.log`. Uses only stdlib Fraction/integer/combinatorial algorithms and finite theta bound comparisons.
- Independent SymPy/mpmath oracle PASS, receipt `independent_oracle_receipt.json`: 16 independently evaluated negative integer zeta values; 70-digit functional-equation derivative at -1; independently sieved 50,000-term prime-power cutoff with analytic tail bound; four theta tests; 16 Gamma moment integrals; original BBP four-pole prefix sums.
- Hasse negative integer `-m` exact finite difference/Stirling/Bernoulli identities checked through m18 by the stdlib suite; the separate SymPy route covers m0..15.
- Exact original BBP source regrouping checks n1..200 and original selected first eight hexadecimal fractional digits from rational source+positive tail, without importing decimal pi digits.
- Finite branching source correction / unique-lift identities checked symbolically with rational fractions and hostile observer-fiber counterexample.

**Authority:** elementary written algebra plus classical analytic identities from published NIST DLMF and Hasse/Euler/Poisson references; exact finite computation calibrates code but does not certify analytic continuation independently. The oracle is a distinct implementation, not an external blind referee. No source-selected pi normality or RH proof.

## Source and archive safety

All additions live in one new research directory. Existing source files, original four signed poles, `U0=0`, historical theorem contracts, and workflows unchanged. Complete SHA256 and Git blob SHA1 manifest is generated over file bytes and validated separately; manifest excludes itself. New focused tests are **not** part of inherited 10,008 native tests unless explicitly added to the root suite later.

**Not run / not claimed:** entire native SUCC root 10k+ tests on this new branch, repository provenance/foundations/ordinal probes in a full clone, Lean formalization of the new N/Z paper claims, hosted exact-head CI before PR runs finish, external expert review, mathematical priority certification, final RH or pi normality proof. Existing stale mathematics catalog on parent research is a known baseline concern; do not silently promote it or assert it was repaired.

## Scientific firewalls

1. The universal carrier is a formal arithmetic category, not a demonstrated physical universe.
2. Gamma interpolation and Hasse continuation are CLASSICAL and do not imply fresh selected-phase inequalities.
3. Negative integer zeta values are analytic continuation outputs; the ordinary `sum n` remains divergent.
4. The convergent prime-weighted reflection uses s=2, not invalid evaluation of an Euler product at s=-1.
5. Fibonacci/Pisot is a specific path recursion, with a nonPisot alternative.
6. Theta functional equation is known and does not prove RH.
7. Positive observer Gamma laws are distinct from the concrete pi digit distribution; model fairness is unverified for selected BBP.
8. Existing PR #415 improves source-to-phase transport, not the missing selected signed Fourier energy bound. This research does not claim to have improved that bound.