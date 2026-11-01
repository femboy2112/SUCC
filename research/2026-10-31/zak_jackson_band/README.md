# SUCC research — a finite analytic band that reads arithmetic prefixes

**Operation ZAK–JACKSON BAND (ZJB), October 31, 2026.** Additive child of PR #438, parent exact SHA `6a23d0735f30c68200a93ff4725c54c0cc8b5975`, integrated Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`. Source: untouched BBP four signed poles and **literal original** `U_0=0`; all other q are explicitly *changed seeds*. No π normality, RH or new Weil positivity proof is claimed.

**Proved source-specialized bridge.** A finite trigonometric flat-top filter retains **every** Fourier alias `|ell|<=16^M+2` exactly, discards all aliases `|ell|>5*16^M-2`, and interpolates the intervening aliases with nonnegative rational weights. Applied to the source-authenticated analytic BBP lift, its signed Zak band `B_(N,M)(q,h)` satisfies

    | B_(N,M)(q,h) - sum_(n=1)^M exp(2*pi*i*h*U_q(n)) | < 99*|h|

for **every** `N>=M>=1`, every nonzero integer `h`, and every *constant-horizontal* `q in [3/16,1/4]`. This includes the genuine `q=pi/16` and the coherent changed seed `q=1/5`. The bound is genuinely uniform in M,N and is a transport estimate, **not** a source-specific signed cancellation theorem. The constants are not numerically sharp and short-horizon use may be vacuous.

**New explicit obstruction.** With the same original four poles but altered seed `q=1/5`, the high-alias complement *outside* the exactly retained frequency interval necessarily has modulus greater than `N-M-99|h|-11|h|/56`. Thus exponentially moving aliases, and their **signed** interactions, cannot be discarded merely because the continuum integral cancels.

**Canonical continuum selector.** Given the authentic source Green T and *chosen* finite-horizontal-action axiom, a periodic normalized lift Q is forced to be constant. Together with the literal zero seed this selects `Q=pi/16`. The action requirement is an extra mathematical hypothesis, not something finite arithmetic magically entails.

**Actual executable package:**

- `PROOFS.md`: exact finite Fourier coefficients, analytic derivative bounds, all-horizon <99|h| proof, high-alias coherent counterfeit and source-relative finite-action selector.
- `CLAIMS.md`: theorem/status ledger and hostile controls.
- `SOURCE_MAP.md`: arithmetic source/analytic lift/band/exact trace typing, with precise changed-seed and altered-source boundaries.
- `NEXT.md`: new source-selected signed cofiber proof obligations (what would actually prove normality).
- `VALIDATION.md`: exact local run and independent oracle scope.
- `jackson_band.py`, `independent_oracle.py`, `tests/test_zak_jackson_band.py`: exact Fraction/integer checks, unique import loader, no production imports.
- `finite_probe.py`, `NUMERICAL_DIAGNOSTIC.json`: optional numpy/midpoint numerical sanity checks, **not** proof or claimed precision enclosures.

The canonical frontier remains `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`; original source and analytic bridge from PR #438 and PR #437 are inherited. **Main, imported historical sources, formal kernel and CI workflows remain untouched.**

**Additional source-derived analytic orthogonality:** Successive cell stationary-frequency windows are disjoint by a strict gap `>|h|(3*16^n-1)`. The entire one-dimensional Zak slice obeys `|int |Z(t,0)|² dt - N int psi² dt| < 8/(75*pi*|h|)` for both original and coherent counterseed. Continuous near-orthogonality does **not** control the N-scale point seam at q=1/5. Proof J25–J31.
