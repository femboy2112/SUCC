# Noether × Radix-Ward — exact-source validation receipt

**Research date:** October 30, 2026. **Status:** DRAFT research branch stacked on exact PR #402 commit `384fe179250a172c2e667c387fdb55bf9589e7a0`, rooted in Main XVI. All additions confined to this new research folder. Original four signed poles, U_0=0, archives, production, workflows, root proof and claim contracts unchanged.

## Executed exact arithmetic tests

Commands in standalone Python 3 environment:

    python noether_probe.py
    python radix_ward_probe.py
    python -m compileall -q noether_probe.py radix_ward_probe.py noether_independent_oracle.py radix_ward_independent_oracle.py

**Exact stdlib tests:** `18/18 PASS` in 0.084 s plus `10/10 PASS` in 0.049 s; compileall PASS.

`noether_probe.py` uses only Python `Fraction` and explicit Gaussian-rational arithmetic. Its tested claims include original four-pole forcing, source-corrected/carry-lifted seed invariant, continuous affine constrained-action symmetry and cotangent Noether charge, zero scalar-phase loop holonomy, nonzero branch-winding information, real symmetric 3D bond-time graph U(1) charge, exact local current flux and source defect, gauge rechart, exact quadratic energy/work, continuous-time observer+field energy cancellation, 59² first coefficient, source-fitted Ward vacuity and real standing/constant mode counterexamples.

`radix_ward_probe.py` exact integer/Fraction tests include all `k<=16` equal-summand frequency uniqueness for four time frequencies, the first `k=17` collisions, their arithmetic `r_q-r_p` phase/carry labels and multinomial `17` versus `289` weights, the first unbalanced 16-to-1 moment, general small-base (b=2,3,4,5) calibrations, exact low balanced moments, nonzero 15-torsion selection and exponential seed cylinder transfer.

### Standalone exact executed code blob hashes

| File | Git blob SHA-1 of **executed local bytes** |
|---|---|
| `noether_probe.py` | `0ba3e9ca6fbbd77bd78ff39a860a2e3c48d0044f` |
| `radix_ward_probe.py` | `bbbfaaba93de20bc6780fe47424efdf8f169a189` |
| `noether_independent_oracle.py` | `7868140d146b6936577731154e6dcd64c82a162b` |
| `radix_ward_independent_oracle.py` | `de1f26a8bb54ae7d9fe217af400b950ad1efad5c` |
| `NOETHER_RADIX_WARD.md` | `d2cc8c05fb47401d68022bea59732af1d90f6793` |

Verify remote GitHub blobs again after committing: a local Git hash is not itself proof of a remote upload. No test counts are transferred to bytes that differ from these hashes.

## Independently authored symbolic/high-precision routes

Command `python noether_independent_oracle.py` **PASS** using SymPy, rational BBP source R and a distinct symbolic derivation of the coupled observer/field Euler–Lagrange energy cancellation, discrete wave EL, cotangent affine symmetry, exact source recurrence and 59² mass jet. mpmath 70-digit checks confirmed the first 16-to-1 source-only resonance and exponentially localized seed-cylinder Fourier average. Printed original source resonance for N=6, h=1:

    (4.639398327388934461417285277 - 1.247161880760353207691262681j)

Command `python radix_ward_independent_oracle.py` **PASS** using an independently implemented 90-digit group-algebra expansion and original exact rational U_n. For N=4, h=1:

    first 34th balanced moment = 1480129751586117359.131913...
    offdiagonal source contribution = 511.1319134836238660722069...
    first 17-factor unbalanced source moment =
      (2.643699118134018423888197 - 1.118714784913380678667413j)

The 34th full expansion agreed with the independently grouped pair-collision source formula to less than `1e-58`. This is a fresh mathematical implementation, but both use the same four-pole source and are not independent blind referees.

**Disclosed early oracle defect:** the first SymPy oracle run built the source rational function with native Python integer `/` operations at integer arguments, silently introducing binary floating approximation and failing an exact recurrence assertion. I replaced these divisions with `SymPy.Integer(...) / ...`, reran the full oracle, and retained the failure history. The initial failed byte version is not counted as a PASS.

## Scope: what has **not** been established

- No new `o(N)` signed Weyl estimate for `U_0=0`, no base-16/base-3 normality theorem, no RH or physical 3+1 gravity, no experimentally grounded Noether symmetry for actual π digits.
- No physical source-to-bond coupling deduced from carrier alone. The declared wave/observer action is a mathematical model and the 59² bond coupling is intentionally inserted.
- No Noether-II/Gauss constraint for a dynamical 3+1 gauge field. The executed local gauge rechart is spatially varying but time-independent; a complete local spacetime gauge model needs temporal gauge links and gauge equations.
- **Not run:** SUCC root `scripts/verify_provenance.py`, full `unittest discover`, observer foundations, ordinal report, math memory rebuild, hosted exact-head CI, Lean checks, external blind mathematical review. The current environment uses separately authored standalone exact tests, not a full repository checkout.

**Verdict:** the mathematics provides a sharp new *Noether and radix-carry observability instrument*, together with rigorous limits. All global seed-smeared Ward moments are seed-blind, and a hindsight-defined Ward current is tautological. A genuinely original-source-selected, zero-seed-sensitive long-range bound remains the missing test.
