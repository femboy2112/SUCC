# Delta / Gamma validation

Commands executed from the isolated `SUCC-final-clausen` worktree:

```
python research/2026-11-05/selected_orbit_final_pin/front_delta/regularized_cut.py
python research/2026-11-05/selected_orbit_final_pin/front_delta/test_regularized_cut.py
python research/2026-11-05/selected_orbit_final_pin/front_delta/verify_receipt.py
```

The probe completed all four preregistered fresh epochs `17,29,53,89`, two
radii `1/2,3/4`, six source/seed models, four cuts and the actual endpoint
energy: 48 source/radius/epoch rows. The final focused suite passed **8 tests**
in 0.228 seconds. This worker did not run the full repository suite; that is
reserved for the coordinator's integration head. No hosted CI result is
claimed here.

The first run used system mpmath 1.2.1, below the repository's declared
`mpmath>=1.3,<2` range. The coordinator then supplied the isolated declared
environment `/tmp/succ-final-pin-venv-20261105` with mpmath **1.4.1**. Under that
Python, all 8 focused tests passed again (0.203 seconds), and an exact-byte
copy of the generator replayed the entire 48-row probe in a temporary
directory. The historical receipt was preserved. The replay was
**byte-identical**, SHA-256
`102325f0a70ae561c75743be720fbe7f219a33e3264d01877ec5bca4e6d27d16`.
All **816 rational intervals** and every literal-carry digest were identical.
Thus the finite result is also reproduced in the declared dependency range.

`verify_receipt.py` checks all 816 exact interval orderings/signs, all 48
finite-cut transport bounds using the rational upper bound `pi<22/7`, exact
zero means at `K=A`, all eight original/`1/5` row equalities, and the generator
hash. Its optional second receipt argument verifies exact endpoint overlap
and reports byte and interval equality. The source hash matches the actual
generator bytes. No original sample is relabeled fresh by this replay.

The first test run had one test-oracle error and one test-oracle assertion
failure: mpmath interval conversion does not accept a bare Fraction in a
multiplication, and the nearest period-5 rational reduces by a factor 33.
The tests were repaired to use explicit outward rational conversion and to
check that the reduced denominator divides `16^5-1`. No probe implementation
or observed receipt was changed to make these checks pass.

At `r=1/2`, displayed values below are rounded summaries; the exact rational
interval endpoints in FINITE_RECEIPT.json certify the signs.

| A | Original actual energy | Original cut K=2A interval | One-pole mutant actual energy |
|---:|---:|---:|---:|
| 17 | -0.010790728 | [-0.008064784,-0.007887705] | +0.029524050 |
| 29 | -0.005959785 | [-0.007919100,-0.007812227] | +0.003588650 |
| 53 | +0.008790879 | [+0.009000371,+0.009059926] | +0.005061434 |
| 89 | -0.006769339 | [-0.006807319,-0.006771541] | +0.002409337 |

Thus finite nonnegative regularized energy is not a source-authentication
test: the selected source has negative certified samples while the exact
first-pole mutant has positive samples. Neither fact settles either source's
asymptotic distribution. The same-source coherent and unforced controls remain
strongly negative, approaching `log(1/2)`; period-5 remains strongly negative.
Rational seed `1/5` has exactly the same pair observations as zero.

## Independent implementation checks

The tests compare recurrence against a direct weighted rational source sum;
compare a short-arc midpoint enclosure against an independently implemented
Fourier integral with an analytic tail; test the cross sign on `Q=15/16` and
future integer-period cancellation; compare root-grid energy against the
finite product identity; check exact-coincidence energy and nested Green
enclosures; and check the explicit endpoint transport bound. These are
independent computational forms but share the mpmath elementary-function
library. They are not independent arithmetic libraries.

Static interval audit after the run:

- Exact endpoints are decoded from mpmath's `(sign,mantissa,exponent,bits)`
  representation as signed `mantissa*2^exponent`, using Fraction throughout.
- `iv.pi`, `iv.cos` and `iv.log` are interval operations; no ordinary float
  feeds a consequential sign, bound, rational source state or carry.
- A rational endpoint is separately divided in interval arithmetic and its
  outward lower/upper endpoint is used when constructing a source interval.
- Kernel arguments reduce an exact integer from the rational lower endpoint,
  preserving orientation and the full interval width.
- The midpoint error bound encloses the analytic second-derivative supremum;
  the interval radius uses its upper endpoint.
- Green-tail correlations are not assumed independent: separate intervals
  enlarge pair ranges conservatively. Periodic and coherent seeds use source
  tails, not imported pi digits. The rational `1/5` control retains the full
  unwrapped seed before circle projection.

The implementation trusts mpmath's directed interval elementary arithmetic;
it is not a formally verified numerical kernel. No finite receipt proves the
unpaid all-epoch source-selected inequality.
