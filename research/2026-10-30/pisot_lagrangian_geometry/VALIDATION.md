# Validation and authority — Operation Pisot-Lagrangian (2026-10-30)

## Exact mathematical controls

- Positive: A and B unimodular, quadratic Pisot eigenvalues and conjugate contractions; nonzero C=AB−BA.
- Positive: H=(BA)^−1AB with H³=−I and H⁶=I, integral Eisenstein P and invariant discriminant -3 quadratic form.
- Positive: det A<0 blocks one-step real exponential; two-step positive flow with K²=I, J²=I and bracket proportional to C.
- Positive: variational minimum action on a declared one-square field with W=[[9,9],[9,16]]; direct 8×6 exact rational minimizer independently reproduces the Schur/least-norm formula.
- Source authentic: r(n)=R(8n−7) agrees with inherited rational BBP four-pole expression on explicit integers; original−Gamma fake difference exactly negative with -59 jet.
- Negative: B=A² is a flat commuting control. v=0, f=0 is insensitive to a nonflat linear connection. A+2I is non-Pisot. Original-source curvature energy does not know the BBP seed, hence cannot imply selected signed Weyl cancellation.

## Actual runs / limits

- **Executed locally, Python stdlib full independent calculation:** 15/15 exact tests passed, including six independent 6×6 rational normal-equation solves and matched fake comparisons; local auxiliary source in working artifact. These local files are not a full SUCC checkout; no full-suite claim.
- **Executed locally, committed pure-stdlib exact probe:** 9/9 tests passed. Exact local/Git blob parity VERIFIED: ce68fe06fcded27a8ae2bde925d69e2d694679b8.
- **Executed locally, separately committed independent oracle:** six 8×6 rational least-squares evaluations agree with the closed-form Schur result. Exact local/Git blob parity VERIFIED: d0cbf09bb0124e880cf9f363b876ddbad88fdb5c.
- **Executed locally, independent SymPy matrix and least-squares oracle:** H, P, all characteristic polynomials, commutator, q_H, one-step/two-step group data, exact BBP R(a) Laurent coefficients, variational values for anchors (0,0), (1,0) and source 47/15 all independently agreed.
- **Not run/claimed:** full root repository unittest suite (10k+), provenance and source scripts in a full checkout, GH hosted CI, Lean proof, external mathematical referee, physical measurement. Do not promote on test count alone.

The tests verify a finite *declared* lattice action and exact original-source readout. They do not verify a source-natural choice of the two Pisot links, a physical spacetime model, universal non-Pisot decomposition of dynamics, π normality or RH.

### Reproduction

From research/2026-10-30/pisot_lagrangian_geometry, run:

~~~sh
python -m unittest -v proof_probe.py
~~~

The paired manuscript gives full paper derivations for every statement. Review main branch HEAD and the separate draft PR ancestry before integration.
