# BBP fixed-point computational graph: resonance and statistical boundary

**Research status:** Additive, draft-only source-derived paper mathematics and a finite symbolic probe. Based on live source-first causal-weld [PR #579](https://github.com/femboy2112/SUCC/pull/579) at `3f1b67d6c319bf4ee9f42941da829cd1f778a3af`, which in turn descends from [PR #576](https://github.com/femboy2112/SUCC/pull/576) and audited Main XXII. No merge, release or priority claim.

**Start here:** [RESEARCH_NOTE.md](RESEARCH_NOTE.md) · [Exact symbolic probe](bbp_graph_shapes_probe.py) · [Validation and claim scope](VALIDATION.md).

The original BBP data is unchanged:
```math
R(n)=\frac4{8n+1}-\frac2{8n+4}-\frac1{8n+5}-\frac1{8n+6},
\qquad \pi=\sum_{n\ge0}16^{-n}R(n).
```

The source-derived analytic root (K_z(x)=P(x)/(1-zx^8)) with (P(x)=4-2x^3-x^4-x^5) has the algebraic resonance
```math
\operatorname{Res}_x(P(x),1-zx^8)=(1-z)(1-16z)^4.
```
At the authentic parameter (z=1/16), the classical BBP integral reduces exactly to a quartic rational function, with angular and logarithmic primitive whose net logarithmic boundary term vanishes.

**Six constrained graph faces:**

1. **R-01** fourfold factor cancellation at (z=1/16); classical BBP partial-fraction reduction, not claimed novel.
2. **R-02** exact order-four holonomic equation for the generating function of the four poles.
3. **R-03** linearly independent rational decimations (R(16^k n)): an obstruction to naive finite-dimensional linear decimation closure.
4. **R-04** Abel orbit-measure fixed point with contraction only for (ho<1); non-Haar invariant boundary measures remain possible.
5. **R-05** explicit positive quadratic-decay polynomial source with matching fourfold resonance but selected value 1 and a nonnormal orbit; blocks generic-resonance arguments.
6. **R-06** exact endpoint oscillator identity; its frequency gain is canceled by the restoring prefactor, so it yields no signed Weyl decay.

**Validation:** `python research/2026-11-10/bbp_graph_resonance/bbp_graph_shapes_probe.py` (Python 3.13.5, SymPy 1.14.0, 21 assertion families PASS, including 400 exact coefficients and 25 decimation pole sets). No full-repository tests or Lean kernel receipts are claimed on this branch.

**Open critical junction:** Construct a *source-selected* constraint linking the analytic root to the chosen invariant measure of the radix-16 orbit, and prove nontrivial fixed-h signed decay. This must reject coherent wrong seeds and the explicit polynomial-resonance counterfeit. **Original-zero hexadecimal parity balance, π base-16 normality and RH remain OPEN.**
