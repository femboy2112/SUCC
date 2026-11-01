# Operation UNIT-TO-UNIT: exact original BBP successor / analytic boundary forge

**Status:** new additive SUCC research experiment based on Main XVIII and read-only PRs #437–#439. This package does NOT assert base-16 normality of π or RH. Its main deliverable is a **source-authenticated, path-aware, finite-to-analytic transport** for the unchanged four-pole recurrence `r(n)` with literal zero seed.

Start with [PROOFS.md](PROOFS.md) for exact definitions, paper derivations and boundaries, [SOURCE_MAP.md](SOURCE_MAP.md) for the no-silent-quotient discipline, [CLAIMS.md](CLAIMS.md) for scoped statuses, [NEXT.md](NEXT.md) for the next signed cancellation experiment, and [VALIDATION.md](VALIDATION.md) for what was actually run.

## Results

- **Finite reversible LEGO:** The BBP forcing is a finite signed Pascal combination of positive rational unit finite-difference atoms `a_k` for every integer n; the zero-seeded BBP states are an exact lower-unimodular **extruded Pascal-16 transform** of these atoms.
- **Analytic completion:** The same `a_k` have independently computed Beta/Gamma representations, a genuine positive Hausdorff source measure and a sharp absolutely convergent Newton expansion for `Re z>-1/8`.
- **Green unit-to-unit seam:** `15 tau_k + tau_(k+1)=a_k` with a unique bounded solution and the exact alternative rational expansion `π/16 = Σ (-1)^k a_k/15^(k+1)`, including alternating certified intervals.
- **Paid real-circle transport:** A moving `J=2M` rational unit-jet approximation to π/16 agrees with its selected base-16 orbit's first M real-circle Fourier observations within `< (33088/23625)|h|(16/225)^M`. This is uniform in M, not normality.
- **Path history:** Ordered words in successor/dilation can have the same affine endpoint and different intermediate journeys. A nontrivial toy path charge proves that endpoint quotient can lose a path observable. A source-attested charge would be an additional theorem, not an automatic implication.
- **Operator naturality:** On the FULL positive Hausdorff moment tower, exact successor `A` and dilation `B_m` satisfy `A B_m=B_m A^m`; output moment k costs input depth mk.
- **Hostile positive-measure control:** Two honest positive measures indistinguishable through moment degree m-1 differ at first moment after dilation m; no shallow finite moment “duck test” preserves this target.
- **Optional Pisot colored-unit example:** `Z[φ]` supplies a genuine two-dimensional algebraic carrier with `V_φ S_1=S_φ V_φ`, Fibonacci matrix transport and a contracting conjugate. It is not imported as a theorem about π.

## Reproduce

```sh
python -m unittest discover -s tests -p 'test_unit_seam_forge.py' -v
```

Tests are stdlib and exact Fractions, with a distinct independent rational-source/recursion oracle. Optional SymPy checks were executed separately. No original production modules, historical math proofs, formal/Lean files or workflow files are changed.

## Source typing

Original `r(n)` and `U_0=0` are mathematical source facts. The exact integer-shift path monoid is not rationally complete; BBP uses rational localization. The positive analytic moment space is a specific real/complex completion, **not** a p-adic completion or a universally correct continuous lift. Fourier phase is nonlinear: `e(sum a_k)=product e(a_k)`, not `sum e(a_k)`. Any normality claim must control signed time averages of the complete original source.
