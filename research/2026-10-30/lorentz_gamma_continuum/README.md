# Operation Lorentz–Gamma Continuum — the source-faithful interpolation between Pascal tiles

**Status: DRAFT / research-only, 2026-10-30.** Stacked on exact SUCC [PR #391](https://github.com/femboy2112/SUCC/pull/391), head `7ce94d38479c22c3d427753812e38207515dc868`; original immutable BBP source and `U_0=0` unchanged. SUCC's physical Lorentz invariance, selected π-digit normality, and RH are **not claimed**.

## Answer to the research question

The integer null coordinates `(a,b)` count zeros and ones in the **auxiliary retained-latent** Pascal process; its causal metric is `ds²=4 da db` under `t=a+b,x=b-a`. The rigorous continuous extension uses the **same original four-pole likelihood** multiplied to real powers, normalized through an *exact four-Beta-function identity*:

`Z(a,b) = E_{mu1}[exp(-8aX)(1-exp(-8X))^b]`

`= [4 B(a+1/8,b+1)-2B(a+1/2,b+1)-B(a+5/8,b+1)-B(a+3/4,b+1)]/[8 R(1)]`.

The real-graded Pascal endpoint interpolation is `W(a,b) = Gamma(a+b+1)/[Gamma(a+1)Gamma(b+1)] Z(a,b)`.

**New exact mathematical structures:**

- A continuous positive likelihood semigroup uniquely extends the integral path labels. The Gamma-binomial counts preserve the real-shift Pascal recursion. Smooth lattice interpolation alone is decisively **nonunique**; an explicit positive, 1-periodic, axis-preserving multiplier supplies a hostile control.
- With `a->infinity` and fixed real `b>=0`, the conditional source has scaled shape `Gamma(b+2,1)`. Differentiating in the continuous success direction gives the renormalized limit `psi(b+2)`; for integer `b`, this is `H_(b+1)-gamma`.
- The historical Oily–Macaroni `lambda-gamma` appears at the source-derived `b=0, r=2` and separately marked golden endpoint readout. The golden rank/clock locus extends this mark to other fractional `b` only when the observation clock is **declared/tuned**, never through automatic Lorentz symmetry.
- On each boost hyperbola `a=rho*exp(-eta), b=rho*exp(eta)`, the **positive continuous endpoint weight** has asymmetric rapidity tails `~C_- exp(2eta)` at negative infinity and `~C_+ exp(-eta/8)` at positive infinity. Its rapidity Fourier/Mellin transform is holomorphic on the sharp absolute-convergence strip `-2<Im(k)<1/8`. These exponents distinguish the opposite original BBP source boundaries; they prove **boost symmetry breaking**, not physical Lorentz invariance.
- The posterior log-partition Hessian is a positive-definite Fisher/covariance metric with negative off-diagonal covariance, while the Pascal cone has an independent Lorentzian causal metric. Do **not** confuse them or infer curvature from an exact gradient cocycle.

## Sources of authority

Primary classical inputs: [NIST DLMF §5.12 Beta integral](https://dlmf.nist.gov/5.12), [§5.5 Bohr–Mollerup](https://dlmf.nist.gov/5.5.iv), [§5.11 Gamma asymptotics](https://dlmf.nist.gov/5.11), and [§5.2 Gamma/digamma](https://dlmf.nist.gov/5.2). Original SUCC source/clock and limit are from the parent #391 and `docs/OPERATIONAL_TRIANGLE.md`. No original academic novelty or external peer-review claim.

Read [`RESEARCH.md`](RESEARCH.md) for scoped proofs and [`CLAIMS.md`](CLAIMS.md) for falsifiers. Reproduce with:

```sh
python -m unittest -v test_null_continuum.py
python independent_oracle.py
```

The full SUCC root gates, hosted CI, formal Lean, and independent external peer review are **not** claimed on this child branch. Next step: selected signed BBP transport with the *real* `U_0=0` and full carry/frequency ladder, not source-only spectral decoration.
