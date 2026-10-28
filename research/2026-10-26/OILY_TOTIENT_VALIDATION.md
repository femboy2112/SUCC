# Oily–Macaroni Totient verification ledger (2026-10-26)

**Theorem types:** CLASSICAL (Möbius inversion, Beta/Gamma derivatives, geometric PGF), PAPER DERIVED (PR #309 authentic-packet conditioning, connected complex Mellin limit, explicit third-order golden-centering coefficient, and selected phase representation budget), EXACT FINITE (Fraction polynomial log moments and root-character identities), NUMERICAL ONLY (complex quadrature and convergence holdouts), OPEN (source-selected signed Weyl saving/π base-16 normality/RH).

## Local isolated run

```
PYTHONPATH=<worktree_root> python -m unittest discover -s tests -p 'test_oily_macaroni_totient.py' -v
PYTHONPATH=<worktree_root> python scripts/oily_macaroni_totient_probe.py --write
PYTHONPATH=<worktree_root> python scripts/oily_macaroni_totient_probe.py --verify
```

This new **16-test** focused suite passed in the isolated development tree. Exact modular Möbius values, independent Beta-log quadrature, exact finite packet kernel identity and compiler bound, source-time Mellin holdouts, the third-order limit, nonzero dyadic Fourier coefficients, counter-grading and all-no-claim flags were checked. The deterministic JSON receipt was written and replay-verified.

**No full native repository suite is claimed locally.** This research branch **stacks on PR #309**, whose author reported 8,794 passing tests; the new full combined native suite, provenance/observer/ordinal gates and hosted exact-head CI are separate requirements. The branch must not be merged without verifying their actual statuses and reviewing PR #309's own head and ancestry.

## Independent positive and negative controls

- Classical Möbius projector was independently checked by direct truncated positive grade sums.
- Full primitive complex Mellin integral was compared to a separate grade-by-grade polynomial integral under high-precision `mpmath`; numerical tolerance was bounded by the **proved positive packet tail** for purely imaginary Mellin exponent.
- Rational finite log moments were compared against direct integral evaluation, with a `1e-50` tolerance (numerical diagnostic, not certificate).
- A regraded variable $J'=\lfloor J/2\rfloor$ changes dyadic primitive probability from $4/9$ to $9/25$ while leaving the original **ungraded** sum of packet masses unchanged.
- A true fully centered mixed third cumulant has **zero** leading $1/n$ coefficient; the Oily–Macaroni signal depends on the **particular golden center** selected by the declared PGF.
- The dyadic primitive Fourier coefficient has a **uniform positive modulus lower bound** $4/25$, so it cannot alone cancel a coherent selected arithmetic orbit.
- The original source with changed initial state $U_0=-T_0$ retains all positive grades but has phase means tending to one. This is a **paper-level** no-go, not a tested finite proof of nonnormality of the authentic zero-seeded orbit.

## Exact-head CI and status

To be populated from actual GitHub Actions runs after pushing the draft PR. Never confuse a successful predecessor run with the new research head.
