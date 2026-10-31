# Analytic front execution, provenance and scoped verdicts

All new files are under this directory in the isolated child of PR417.
The original source, zero seed and parent proof files are unchanged.
`ANALYTIC_TRANSPORT.md` contains the full paper arguments; tests are finite
implementation checks, not replacements for those proofs.

| ID | Statement and verdict | Evidence | Exact boundary / next obligation |
|---|---|---|---|
| A01 | Rational Markov enclosure for original pi/16: PROVED LOCAL | Orthogonality proof, exact rational code, separate Gram--Schmidt/Jacobi-CF oracle | Requires actual positive Hausdorff source measure; no arbitrary source substitution |
| A02 | Original error <188/(225*3600^d), selected phase precision transport: PROVED LOCAL | Monic Chebyshev norm proof and all tested exact norms | Better asymptotic rate; coarse uniform bound is worse at d=1,2; no cancellation |
| A03 | Minimal d-atom positive zero-seed rational-boundary control matching 2d source values: PROVED LOCAL | Gaussian exactness, rational recurrence, all-horizon signed bound | Changed source, not authentic four poles; no new blanket prefix no-go claim over #408/#415 |
| A04 | Uniform rational finite-lattice error bound for completed-zeta derivatives: PROVED LOCAL / classical specialization | Gaussian tail and integration-by-parts proof; 54 numerical calibrations | Bounds analytic truncation only, not floating rounding; does not establish zero-line positivity |
| A05 | Entire corrected germ identifies positive prime-power measure; every finite jet admits a positive fake: PROVED LOCAL | Exponential-moment uniqueness, exact Pascal annihilator; 5 germ derivatives and 12 fake orders checked | Fake violates von Mangoldt divisor law already at n=2; no alternate zeta/Euler product |
| A06 | These carrier maps alone force pi-normality or selected cancellation: REFUTED as a generic implication | Same-source coherent seed and A03 rational-boundary controls | Stronger source/seed premise and actual selected signed inequality still needed |

A05 was refined analytically after reading #421/#423 and before its exact
probe: the new discriminator uses changes at powers of 2 with binomial
coefficients, rather than repeating their flat-asymptotic shadow. The proof
and expected positive/negative outcomes were reported to the principal
researcher before the corresponding test execution. It does not replace
the original preregistered controls.

## Executed commands

From this directory (the receipt wrapper pins cwd, launch head, UTC times,
memory limit, one numerical-library thread, exit code and SHA256):

    python3 run_receipt.py --name focused --timeout 120 -- python3 -m unittest -v test_resolvent.py
    python3 run_receipt.py --name resolvent-probe --timeout 120 -- python3 probe.py
    python3 run_receipt.py --name independent-oracle --timeout 300 -- /media/leah/SPANKBANK/SUCCYBOI/SUCC-zero-dispersion/.venv/bin/python independent_oracle.py

* **13 focused tests PASS**, 0.325 seconds unittest time. The earlier
  exploratory 12-test run also passed; it is not counted as additional tests.
* Exact source coefficient regrouping at 300 times; all moment orthogonality
  checks d=1..8; fresh enclosures d=11,14,19; two changed-positive-source
  families; finite two-atom exactness/rank failure; original-prefix Gaussian
  controls and exact zero-seed recurrences; rational aliases; twelve exact
  positive prime-weight jet countermodels.
* Separate SymPy implementation uses Gram--Schmidt and a Jacobi continued
  fraction, rather than the implementation's Hankel linear solve and
  polynomial-quotient formula. Centers, polynomials and norms agree exactly
  at d=1,3,6,11,14,19. A 110-digit mpmath pi value lies in all corresponding
  rational enclosures; the focused suite separately proves enclosure overlap
  by a rational original-BBP tail, without supplied pi digits.
* **54 theta derivative calibrations PASS** across six points, three
  truncations and orders 0,1,2; fresh regimes include complex arguments.
  The rational uniform strip bound is proved analytically; these mpmath
  comparisons are not rigorous rounding enclosures.
* Five corrected zeta-germ derivatives agree with the positive-exponent
  formula and independent prime-power enumeration up to 10000, inside the
  proved tail budget. Symbolic `(z D)^k[z(1-z)^K]` confirms the finite-jet
  annihilator at five fresh orders without importing the binomial routine.

No mathematical test failed in this front. There was no new dependency
installation, Lean run or independent external referee. Same-model reasoning
and shared classical source identities remain common provenance. Root native
suite, source gates and hosted CI are reported by the principal researcher.

## A concrete finite certificate

At d=19 the center uses r(1)..r(38); the sharper interval uses r(39).
Its rational width is approximately `1.2273677707814088e-71`; the center
denominator has 3179 bits. After multiplication by 16^n, interval width is
less than 1/16 for n<=57. This is a width certificate, **not** a guarantee
that all those circle intervals avoid a digit seam. Exact numerator and
denominator data are retained in `receipts/resolvent-probe.log`.

The arithmetic cost is visible: polynomial coefficients and denominators
grow; no linear-time or optimal information-complexity claim is made.

## Read-only provenance

All 46 files in the parent universal_nz_carrier directory are pinned by
commit and byte hash in this front's manifest. Important overlapping inputs:

* #417: source density, Hasse first tangents, theta normalization, scalar
  reflected prime identity and source finite part.
* #415: different order-two Stieltjes rational cubature and finite-prefix
  countercontrols. The broad prefix-to-normality failure is inherited.
* #420: source-weighted circle/Gamma/Green instruments; no shared operator
  with the new Hausdorff resolvent is assumed.
* #421: full spectral residue tower and source/phase truncation cost; all
  polar data leave an entire remainder. Different truncation architecture.
* #422: Bernoulli prime denominators and finite-cycle moments.
* #423: snapshot kernel criterion and complete convergent germ versus
  formal asymptotic data. The general identity-theorem claim is inherited.

Primary literature URLs actually retrieved this round are recorded with the
manifest. No large quotation or scholarly-priority claim is used.
