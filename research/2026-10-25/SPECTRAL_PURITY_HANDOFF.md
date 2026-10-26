# Spectral Purity handoff: the surviving conductor-flat estimate

The completed round is [Operation Spectral Purity](OPERATION_SPECTRAL_PURITY.md).
Do not repeat its finite identities as a new normality theorem. The exact
original source, zero anchor, integer lift, four signed poles and correlated
prime channels remain mandatory. Main and historical artifacts are unchanged.

The new unconditional arithmetic result removes every conductor-growth step
from the signed Fejer sum at the predetermined schedule

$$
H_N=\max\left(2,1+\left\lfloor\sqrt{\lfloor\log_2N\rfloor}\right\rfloor\right).
$$

Use the monotone history conductor
$Q_n=\operatorname{lcm}_{1\le j\le n}\operatorname{den}(r(j))$.
The next sufficient theorem, now restricted to conductor-flat steps, is

$$
\limsup_{N\to\infty}\frac2{N^2H_N}
\sum_{\substack{1\le m<N\\Q_{m+1}=Q_m}}
m(q_{m,H_N}-H_N)\le0.
$$

It is OPEN. Negative defects are allowed. Every finite horizon uses one
common width $H_N$. The omitted birth sum has an explicit vanishing bound,
and the rank boundary also vanishes. Thus proving this estimate really
would close the spectral target and, via the authenticated Green transfer
and Weyl criterion, prove base-16 normality.

The next arithmetic argument must use the actual four-pole numerators and
their propagated complementary phases on the existing-conductor timeline.
Three failed shortcuts have durable receipts:

1. New-layer traces fix the full past but do not dominate the selected
   embedding. Authentic $n=2,H=p=3$ gives trace 3 and selected innovation
   greater than 5; $n=14,p=109,H=4$ is a separate holdout.
2. Even the entire authentic common-conductor tower permits a positive
   counterfeit with every fixed Fourier mean tending to 1.
3. Any fixed finite prefix, endpoint jet, all positive moment signs, odd
   denominators and all fixed leading moving bands can coexist with a
   rational periodic seed. The exact global four-pole identity fails in
   that construction. Do not turn the quantifier into one mutant matching
   every prefix or infinitely many exact endpoint derivatives.

A useful candidate must exclude both distinct counterfeit families through
proved hypotheses. Their separately preserved features must not be silently
combined into one stronger counterfeit. Source uniqueness is already known;
the new inequality must use it quantitatively.

Reproduce the finite instruments with

```bash
python scripts/spectral_purity_probe.py --verify research/2026-10-25/spectral_purity_validation/finite_receipt.json
python -m unittest discover -s tests -p 'test_spectral_purity_*.py' -v
python scripts/check_spectral_purity_lean.py --help
```

The Lean checker needs the pinned mathlib dependency cache and runs serially.
It establishes ten finite real-kernel declarations, not the complex Fourier
interpretation, Green analysis, prime-count asymptotic, or normality theorem.
See the [validation receipt](SPECTRAL_PURITY_VALIDATION.md) for actual
commands, hashes, failed attempts and delivery state. Recheck live PR heads
and source hashes before continuing on another fresh descendant branch.
