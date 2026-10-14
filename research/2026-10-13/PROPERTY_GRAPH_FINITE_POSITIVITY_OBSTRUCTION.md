# BOOTSTRAP theorem — finite positive observation does not identify the global sign

**Date:** 2026-10-13 (America/New_York). **Branch:** `research/property-proof-graph-bootstrap-2026-10-13`, stacked on PR #59 at `b7fbba74fedd6e6734b1d2b129a72bdff4dd9843` (which itself descends from `main` `6e0d88f1b235b85188393bbcd64ac0436cb71a70`).

**Claim status:** PROVED LOCAL (elementary classical Hilbert-space algebra, explicitly realized); NOT a new mathematical-priority claim. **RH PROVED: no.** No zeta zero is read, constructed, or guessed.

## Theorem B-01: a hidden negative direction survives every fixed finite observer

Let `H = ell^2(N)` over the reals (complex version uses absolute squares), and let `P_M` be orthogonal projection onto `span(e_M)`. Define bounded self-adjoint operators

`A_plus = I, A_minus = I - 2 P_M`.

For every finite horizon `K < M`, denote by `E_K = span(e_1,...,e_K)` and `P_K` the corresponding projection. Then:

1. `P_K A_plus P_K = P_K A_minus P_K = P_K` exactly, as operators on E_K.
2. Both global operators have norm 1 and are self-adjoint.
3. `<x,A_plus x> = ||x||^2 >= 0` for every x in H.
4. `<e_M,A_minus e_M> = -1`; therefore A_minus is not positive semidefinite.
5. Every source/probe restricted to E_K gives identical complete quadratic observations under both operators. No amount of *repetition of those same restricted probes* identifies the unseen negative direction.

**Proof:** `P_K P_M=0` for M>K, so compression agrees. `A_minus` has eigenvalue -1 on e_M and +1 on its orthogonal complement; `||A_minus||=1`, and its quadratic value at e_M is -1. All steps are exact. QED.

**Meaning:** checked finite Gram matrices can all be positive on a declared observation menu even when the global operator is indefinite. This is a *probe-adequacy* obstruction, not a proof that infinite positivity is inaccessible.

## Theorem B-02: what actually lets positivity pass to the limit

Suppose A is **one fixed bounded self-adjoint operator** on H and every finite-dimensional compression `P_K A P_K` is positive semidefinite for **every K**, where `P_K -> I` strongly. Then A is positive semidefinite.

**Proof:** For any x in H, let x_K=P_K x. Since A is bounded, `<x_K,A x_K> -> <x,A x>`. Every term on the left is nonnegative by the hypothesis for every K, so the limit is nonnegative. QED.

This demonstrates precisely what the finite-countermodel does NOT refute. A valid all-K estimate or a core/closed-form version *can* certify global positivity. Obtaining that global estimate for an **authenticated completed Weil quadratic form** is the hard RH-facing obligation. Finite computations at K=10^10 are still only finite computations.

**Unbounded-form caveat:** if the candidate arithmetic form is unbounded or distributional, do not reuse this bounded-operator proof. Supply the actual form domain, closability/core, continuity or lower-semicontinuity in the correct topology, compatibility of truncations, and a justified passage to limits.

## B-03: contrasting structural rigidity and global observability

The established zero-centered SUCC PR #59 proves finite reciprocal-cell clock identities and perfect arithmetic interpolation on every finite integer prefix. It also exhibits LCM blackout cells far beyond each finite prefix. Those facts are compatible: every finite observer can interpolate its observed world, while each finite family of clocks retains unobserved cells.

Likewise B-01 provides indistinguishable finite corners with different global signs. These are **different failure mechanisms**:
- **Phi/pathway:** the allowed observer lacks a probe accessing the negative direction.
- **Sigma/source map:** even an exhaustive declared observation menu need not establish that the measured form is the authentic Weil source.
- **Analytic transport:** finite positive corners cannot certify a global kernel without compatible all-K or domain-correct limit arguments.

Do not infer any connection between the *particular* artificial A_minus and the actual Weil form. The former exists exclusively as a negative control.

## Reproducible finite checks

Implementation: `observational_succ/property_obstruction_controls.py`.

Tests: `tests/test_property_obstruction_controls.py`.

```sh
python -m unittest discover -s tests -p 'test_property_obstruction_controls.py'
python -m unittest discover -s tests -p 'test_succ_property_graph.py'
python scripts/verify_succ_property_graph.py
```

The exact rational test deliberately samples K=1..100 and M>K; the theorem above, not those samples, provides universal proof.

## Next verdict-changing probes

1. Produce an **all-K source-first inequality** for a well-specified completed kernel, rather than extrapolating sampled Gram matrices.
2. Establish that the candidate form is the **actual completed Weil form**, including prime powers, Gamma, pole and conductor contributions on a valid test-function domain.
3. Reproduce its sign without importing a zero list, and break the argument with fake-composite, non-Euler, wrong-half-density and wrong-Gamma mutants if it is source-blind.
4. If candidate positivity is identified only on a subspace, provide a density/core theorem and a continuity/closedness argument extending the sign to the needed domain.

**Dependence firewall:** B-01 is true in many unrelated Hilbert spaces. It supplies no evidence for RH itself and cannot substitute for the missing Weil identification.
