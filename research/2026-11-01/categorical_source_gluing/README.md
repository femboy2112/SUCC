# Categorical source gluing: recover the lift, synchronize the histories

**2026-11-01 — additive research bundle; not pushed, not merged.**

Pinned upstream: SUCC PR #447, `6fedcbe445f856878ecb1b1d9a0a84ad97a77e2e`.
Observed main: `4eb411e3730a9e7b95480369a438b89d9a433a4b` (Main XVIII).

## Main result

For the unchanged original source

```
r(z) = 4/(8z-7) - 2/(8z-4) - 1/(8z-3) - 1/(8z-2),
R(z) = (8z-7)^4 / ((8z-4)^2 (8z-3) (8z-2)),
U_0 = 0,  U_(n+1) = 16 U_n + r(n+1),
```

the scalar source projection R does not support a descended rational successor.
Nevertheless the TWO-observation map `z -> (R(z),R(z+1))` is birational onto its
image. An explicit rational inverse Z(u,v) is supplied as a coefficient certificate.
Its denominator is certified nonzero at z=0 and for every real z>=1, so the inverse
chart works at EVERY original source integer, not merely at tested horizons.

Consequently the exact source-labelled dynamics can be realized on observed data:

```
(u,v,U) -> (v, R(Z(u,v)+2), 16 U + r(Z(u,v)+1)),
(u0,v0,U0) = (2401/96, 1/480, 0).
```

This is a genuine repair of the representation, not a contradiction of the old
one-coordinate no-go. For arbitrary complex points use normalization of the delay
curve, not an assertion that the raw pair is globally one-to-one.

## Other completed pieces

* Original cover monodromy S4, but deck group TRIVIAL; S4 does not act as deck
  transformations on the original four-sheeted sphere.
* Coherent lifted path composition and a concrete complex-algebraic counterexample
  to naive fiber-product gluing; a future-observation quotient criterion.
* Covariant transport of source points, clock, differential AND tangent unit.
* Exact Fourier naturality of the authentic affine BBP word, with compatible
  growing odd-conductor embeddings and an all-horizon Hilbert realization.
* A precise remaining obstruction: the selected real-circle harmonic is a point
  trace in the compact dual, not a bounded L2 observable.
* Complete radix-16 branch isometries, rather than an invalid even-register
  permutation; source/seed/path mutation controls.

See `PROOFS.md`, `CLAIMS.md`, `VALIDATION.md`, `SOURCE_MAP.md`, and `INTEGRATION.md`.

The canonical category spine remains
`observational_succ.operational_yoneda_descent.ObservationPathCategory`.
`repo_adapter.py` imports it; it does not replace it. Its full-repository integration
check is explicitly skipped in this partial local environment.

## Reproduce

From a complete repository or this extracted bundle root:

```sh
python research/2026-11-01/categorical_source_gluing/cover_certificate.py
python research/2026-11-01/categorical_source_gluing/independent_polynomial_oracle.py
python research/2026-11-01/categorical_source_gluing/frame_and_monodromy_audit.py
python -m unittest discover -s tests -p 'test_categorical_source_gluing.py' -v
```

The symbolic generators use SymPy 1.14.0 in the observed environment; the independent
polynomial verifier and unit tests require only Python's standard library and the
committed certificate. A complete SUCC checkout is needed for the optional category
integration test and the full repository validation.

**Not established:** new selected signed cancellation, pi normality, RH, an intrinsic
BBP heat/Feynman probability measure, a canonical equality between an SO(3) sphere
rotation and the full arithmetic Fourier transform, Lean certification, external
peer review, or hosted CI on these new files.
