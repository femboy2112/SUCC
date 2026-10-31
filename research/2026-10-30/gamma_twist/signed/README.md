# Signed Gamma/CRT campaign

The strongest proved result here is a sharp limitation on source-only
energy arguments. For the authentic four-pole forcing, fixed nonzero h,
and growing windows `A -> infinity`, `L -> infinity`, `L<=CA`,

\[
\inf_{s\in\mathbb R}\frac1L\sum_{n=A}^{A+L-1}
\big[1-\cos(2\pi h(U_{n+1}(s)-U_n(s)))\big]
\sim\frac{\pi^2h^2}{512L}\sum_{n=A}^{A+L-1}n^{-6}.
\]

The fixed coherent seed `s=-pi/16` asymptotically attains this floor. A finite
version reduces the nonlinear minimization to an exact quadratic projection
after proving that every minimizing phase has a unique small lift. Fifteen
rational/interval certificates and a separate nonlinear numerical oracle
validate the instrument. This is **not** a zero-seed signed saving.

[SHARP_SEED_ENERGY.md](SHARP_SEED_ENERGY.md) contains the proofs, the exact
full-cofiber recurrence, the universal source floor, the sharpened inherited
Gamma comparison, and the surviving selected-phase obligation.
[ROUTE_LEDGER.md](ROUTE_LEDGER.md) records method verdicts and validation.
[PREREGISTRATION.md](PREREGISTRATION.md) fixes the finite hypothesis inventory.

The actual zero seed passes 36 fresh eligible SC-06 tests at p701..857 and
h=1,3,7; all rigorous energies exceed 1/4. Six p13/p73 rows are calibration.
The 18 absolute-value Gauss-completion bounds are all vacuous. Exact searches
exclude all translated q-grids with q<=ord_p(16) and error<=1/p² in the full
p701,709,733 windows. Normal and nonnormal controls are retained; the failed
conductor2 immediate-collapse assertion is preserved and repaired explicitly.

**Validation:** 16 focused tests pass. A separate common-denominator and
100-digit oracle checks 461 states, 42 selected energy intervals, 15 minimum
intervals, and three shortest-arc calculations. The oracle is an independent
implementation/representation within the same model family. The rigorous
interval trigonometric instrument is inherited unchanged from PR399 and is
not counted as independent of its own source.

Reproduce focused tests from this directory:

```sh
python -m unittest discover -v -s . -p 'test_*.py'
python run_probe.py
python approximate_grids.py
python independent_oracle.py
```

For new raw command receipts use `python validate.py --suffix replay`; it
refuses overwriting existing outputs. The independent oracle verifies the
preserved probe receipts. Repository-wide gates belong to the root campaign.

π base-16 normality, SC-06, and RH remain open. No new Lean or external-referee
authority is asserted. The author's Harmonic/Golden/Euler--Mascheroni triangle
and Oily--Macaroni provenance are preserved; no geometric constant is used as
an unproved signed-arithmetic premise.
