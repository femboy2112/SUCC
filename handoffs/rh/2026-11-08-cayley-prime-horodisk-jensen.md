# RH research handoff candidate: source-anchored Cayley prime oscillator and Jensen circle pin-bed

**RESEARCH ONLY — RH PROVED: NO.** Draft SUCC non-main PR. Intended base SUCC `main@43a607818907120d4cdab73d240f5b4d7700b63f`; replace with verified exact PR head on review. The RH repo is **read-only** for this round. This handoff is not published as a proof and should not be imported without native verification.

## The actual export

1. **Classical exact geometry:** `w=(s-1)/s` sends `Re(s)=1/2` to `|w|=1` and true Euler region `Re(s)>1` to tangent `D(1/2,1/2)`. `F(w)=2xi(1/(1-w))` is analytic in full `|w|<1`, but `log F` is globally holomorphic iff RH. Euler/Gamma gives an actual source log in the small horodisk only.
2. **Certified-format zero exclusion lemma:** Jensen defect `J(r)=1/(2pi)int log|F(re^iθ)| =sum_{|a|<r}log(r/|a|)`. If a genuinely rigorous arithmetic upper bound `exp J(r)<r/r0`, there are no nontrivial ξ zeros with `|(rho-1)/rho|<=r0`. Program computes exact integer cap **given** such a certified bound, not its arithmetic proof.
3. **Strong explicit negative theorem:** half-density altered prime factors `prod_{p<=P}(1-p^(1/2-s))` have finite zeros all Re(s)=1/2, but their infinite-prime Euler-region limit `1/zeta(s-1/2)` has zero at s=3/2, w=1/3, on the *boundary of its own* convergence horodisk, not the critical line. Mertens' theorem gives `log P * E_P(3/2) → e^(-gamma)`. This kills the false inference that unit-circle zeros of every finite root-of-unity-like factor establish RH upon an infinite product limit. **Changed source explicitly quarantined:** these are not genuine zeta Euler factors.
4. **Authored tests** in `observational_succ/xi_cayley_prime_pinbed.py` / `tests/test_xi_cayley_prime_pinbed.py` use exact Fraction for geometry, fake normalized symmetric Xi polynomials with off-line zeros at `1/4,3/4`, and on-line zeros at `1/2±i/2`. They compare exact Li coefficients, Jensen counts, and the original finite Euler product with full Gamma/pole to numerical zeta at Re(s)>1. Numerical contour winding does NOT prove any zero-free region without rigorous analytic error.

## Context and source check

- SUCC `observational_succ/euler_gamma_li_bridge.py` and `handoffs/rh/2026-10-24-euler-mascheroni-completed-li.md` already offer source-grounded finite Li coefficients and a stronger finite-jet adversarial changed-source example. Reuse, don't duplicate or promote finite coefficients to all-degree positivity.
- The actual logarithmic Euler region is `Re(s)>1`, not `Re(s)>1/2`. The functional equation is original completed `xi(s)=xi(1-s)`; it does not create a positive completed Weil quadratic form.
- This geometry is compatible with the RH repo's ongoing prime–Archimedean coupled second-jet/Weil sign frontier but **does not solve its global arithmetic positivity**.
- Never insert nontrivial zero locations into the construction. Fake polynomials are explicitly synthetic; fake composite six, wrong prime exponent shift, missing Gamma, or arbitrary observer phase rotations are mandatory controls.

## Missing theorem and next decisive probe

An original-prime, half-density-correct, full Gamma/pole, source-anchored inequality proving the global Jensen defect vanishes (or an independent Weil-positive/Suzuki nonnegative realization) across every radius. A first strictly new finite-radius result would require a sound validated numerical/analytic upper bound on `exp J(r)` that excludes ξ zeros in a disk radius not already covered by the classical Euler zero-free region. Without rigorous error, the observation remains a heuristic.

**Status:** CLASSICAL geometric and Mertens counterexample; PROVED CONDITIONAL Jensen certificate; UNVERIFIED original-source radius extension; RH OPEN. Scholarly novelty and priority NOT claimed. Please consult SUCC research `PROOFS.md`, claim ledger and exact-head validation before RH repo integration.
