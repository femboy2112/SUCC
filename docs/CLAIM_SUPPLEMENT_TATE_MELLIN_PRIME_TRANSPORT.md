# Claim supplement — SUCC × prime FUCC source-labelled Tate–Mellin transport

**Branch:** `research/tate-mellin-prime-fucc-escape-2026-10-16`; stacked on PR #145, then #142 and #141. **Research dossier:** [full TMF source triangle and adversarial proofs](../research/2026-10-16/SUCC_FUCC_TATE_MELLIN_SOURCE_TRIANGLE.md). **RH PROVED: NO.** Academic precedence retained for Tate, Euler, Gamma, probability and characteristic-function mathematics.

| ID | Scoped status | Claim / boundary |
|---|---|---|
| TMF-01 | CLASSICAL / PROVED PAPER | For sigma=2(n+1)>1 the independent rate-1 Gamma source and authentic prime-geometric zeta-distributed N yield the exact *positive characteristic function* `Lambda(sigma+2it)/Lambda(sigma)` |
| TMF-02 | PROVED PAPER / exact Fraction | Independent finite Gaussian log-Dirac probability chart, properly phase-shifted by `-log pi`, has a fully rational normalized finite-event error bound; Beta and Exp are one finite source in two coordinates, not independent evidence |
| TMF-03 | PROVED PAPER / exact Fraction | Finite authentic Euler-prime geometric valuation source approximates normalized zeta ratio uniformly in spectral frequency; bound via two independent total-variation truncations |
| TMF-04 | PROVED PAPER / exact Fraction | Certified band-uniform **combined Gamma_R zeta** error `E_arch+E_prime`; finite probability-Gram operator difference <= dimension times entrywise bound. This is *not* signed-Weil positivity |
| TMF-05 | CLASSICAL / exact finite integer | Natural prefix n<=H bijects with product-cutoff prime valuation cone and matches its complete Dirichlet polynomial; rectangular FUCC box is a different finite source |
| TMF-06 | CLASSICAL / exact rational coefficients | Independent prime-geometric cumulants recover genuine von Mangoldt prime-power jets and explicit truncated tails; finite log-support half-density weights are source-typed |
| TMF-07 | CLASSICAL / PROVED PAPER | For all 0<sigma<=1, positive normalized Euler valuation products escape every finite integer/log region, even with finite geometric-depth cutoff >=1; no tight positive limiting log-source, **not** analytic-continuation or RH impossibility |
| TMF-08 | EXACT FINITE / classical asymptotic | Natural prefix H=6 produces strict covariance `-10800/4118023` between p=2,p=3 activation despite independence under the full sigma>1 zeta law; universal conditioning bound and cutoff caveat |
| TMF-09 | REFUTED SHORTCUT / exact mutations | Fake base 6 duplicates coefficient at 6; alpha_2=3/2 corrupts coefficient 2; both maintain positive probabilistic Gram. Wrong parity, wrong pi, and standalone pole polynomial fail their distinct normalization controls |
| TMF-10 | UNVERIFIED boundary | No typed equality of positive probability Gram to complete signed Weil/Suzuki form. Missing true low Schur sign and all-test positivity, plus completion/contact/pole provenance |

**Controls:** exact natural vs prime-hyperbolic equality; box-vs-hyperbola mismatch; phase and source-chart distinction; fake 6, changed first Euler coefficient, Gamma parity, pi scale, pole-removal polynomial; 0<sigma<=1 mass escape; finite joint prime dependence; seeded fresh spectral holdouts (numerical calibrations only). No false claims about academic priority, global source authentication by finite prefixes, physical transfinite computation, or RH.

**Reproduction:** `python -m unittest discover -s tests -p 'test_tate_mellin_prime_transport.py' -v`; `python scripts/tate_mellin_prime_transport_probe.py --verify`. Existing FGF, DGC and BGD tests remain dependencies in the stacked PR; long full-suite GitHub CI is reported separately.
