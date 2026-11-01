# Exact finite outcomes and limits of inference

All 23 predeclared interval cases completed. The raw exact fractions, per-lag real sums, weights and source hashes are in `finite_receipt.json`. The table below rounds endpoints outward; decimal values are displays, not the certificates.

The three parent intervals at N=512,1024,1536 intersect the independently constructed intervals. The clipped source budget improves the corresponding rigorous squared-Weyl upper bounds from approximately 0.472/0.353/0.317 to below 0.271/0.254/0.251. These are finite upper bounds, not measured Weyl magnitudes or asymptotic saving.

| N | K | h | Selected signed interval (outward display) | Squared-Weyl upper (outward) |
|---:|---:|---:|---|---:|
| 512 | 4 | 1 | [-0.0037857083, -0.0037857082] | 0.2707091609 |
| 1024 | 4 | 1 | [-0.0091548208, -0.0091548207] | 0.2530433129 |
| 1536 | 4 | 1 | [-0.0075330265, -0.0075330264] | 0.2505947700 |
| 769 | 4 | 3 | [0.0123533607, 0.0123533608] | 0.2903214776 |
| 769 | 4 | 5 | [0.0079297321, 0.0079297322] | 0.2937213298 |
| 769 | 4 | 7 | [0.0013923511, 0.0013923512] | 0.2935316802 |
| 769 | 4 | 11 | [0.0006037833, 0.0006037834] | 0.3031764728 |
| 2048 | 5 | 3 | [-0.0010134288, -0.0010134287] | 0.2262581998 |
| 2048 | 5 | 5 | [-0.0049129570, -0.0049129569] | 0.2301738540 |
| 2048 | 5 | 7 | [0.0030427842, 0.0030427843] | 0.2445037867 |
| 2048 | 5 | 11 | [0.0020296915, 0.0020296916] | 0.2539012738 |
| 4096 | 6 | 3 | [-0.0018996674, -0.0018996673] | 0.2027305318 |
| 4096 | 6 | 5 | [-0.0034129992, -0.0034129991] | 0.2122040017 |
| 4096 | 6 | 7 | [0.0069561074, 0.0069561075] | 0.2315177361 |
| 4096 | 6 | 11 | [0.0063022470, 0.0063022471] | 0.2454895499 |
| 1024 | 17 | 3 | [0.0003361983, 0.0003361984] | 1.1565753472 |
| 1024 | 17 | 11 | [0.0035148150, 0.0035148151] | 1.2418019712 |

**Fresh positives matter.** All four fresh harmonics at N=769 have strictly positive signed scores. At N=2048 and 4096, h=7 and 11 are positive while h=3 and 5 are negative. Thus the earlier three negative h=1 observations cannot justify a universal finite nonpositive inequality. None of these signs refutes or proves the asymptotic selected limsup target.

At K=17 the instrument measures deeper 3/5 conductor classes, but the resulting Weyl upper exceeds one. That bridge is vacuous at these finite inputs. We retain the measurements and do not report them as a nontrivial bound.

## Signed conductor contributions at N=1024,K=17

Each entry is the sum of the actual weighted real lag intervals in the indicated valuation class of the cofactor `16^k-1`. For the full frequency `h(16^k-1)`, add `v3(h)` and `v5(h)` respectively. It retains signs; class support alone is not a bound.

| h | (v3,v5) | Signed contribution (outward display) |
|---:|---|---|
| 3 | (1, 1) | [0.0074372799, 0.0074372800] |
| 3 | (1, 2) | [-0.0037940324, -0.0037940323] |
| 3 | (2, 1) | [-0.0033181098, -0.0033181097] |
| 3 | (2, 2) | [-0.0005218397, -0.0005218396] |
| 3 | (3, 1) | [0.0005329000, 0.0005329001] |
| 11 | (1, 1) | [0.0004137024, 0.0004137025] |
| 11 | (1, 2) | [0.0022319221, 0.0022319222] |
| 11 | (2, 1) | [0.0012023632, 0.0012023633] |
| 11 | (2, 2) | [0.0005086542, 0.0005086543] |
| 11 | (3, 1) | [-0.0008418271, -0.0008418270] |

## Normal-control calibration

The infinite Stoneham controls include the full omitted-series error; the code does not call the finite rational truncation normal. Classical base-16 normality of alpha_(16,3) and alpha_(16,5) is supplied by Bailey–Crandall, [Random Generators and Normal Numbers, Corollary 4.9](https://www.davidhbailey.com/dhbpapers/bcnormal.pdf). At N=256,K=4, alpha_(16,5) has a rigorously positive h=5 score above 0.26019. A demand for nonpositive scores at every finite horizon would reject even this known-normal control.

## Instrument execution history

The first independent sweep was stopped before it emitted a receipt because cubing exact source denominators made the tiny-angle enclosure unnecessarily expensive. The traceback located the cost in rational gcd arithmetic. The repair encloses each exact phase in an outward 2^-96 dyadic cell and propagates the full interval; it discards no error. Exact-root, huge-denominator and independent-parent comparisons passed again. The complete sweep was then rerun using the repaired bytes whose SHA256 values are embedded in `finite_receipt.json`. The interrupted attempt is not counted as a completed measurement.

## Analytic versus finite authority

The counterseed clock limit, dyadic shadow theorem, conductor spectrum and two-scale criterion equivalence are proved in the accompanying papers. The finite sweep validates instruments and exposes hostile signs. It supplies no all-horizon zero-selected cancellation theorem, no kernel proof, and no RH result.
