# BBP expanded into causal-volume rules

**Research-only continuation of draft #635**, pinned at `e14d46c17a65e1e5f231c619657b9332caa181c0`. The original four poles, `U_0=0`, archives and main are preserved. [Full proofs](THEOREMS.md) distinguish classical ingredients, inherited source results, this round's deductions, and finite checks.

The user's proposal was to replace every BBP constituent with its causal-volume form, then look for cancellations that can become generic reasoning rules. This round builds an executable finite fragment of that program. It also proves where the rational linear fragment stops closing when the actual signed phase is observed.

## The central results

The forcing `r(n)` is a Laplace observation of the positive, signed-channel kernel

\[
q(t)=4-2e^{-3t}-e^{-4t}-e^{-5t}.
\]

The j-th source power has the exact inverse-Laplace kernel `q` convolved with itself j times. Its direct `4^j` channel expansion reduces to **4j pole/order slots**, and its low Taylor coefficients cancel:

\[
q^{*j}(t)=15^j\frac{t^{2j-1}}{\Gamma(2j)}+O(t^{2j}).
\]

For j=2 the complete expression is

\[
16t-\frac{134}{15}
+\left(4t+\frac{34}{3}\right)e^{-3t}
+te^{-4t}
+\left(t-\frac{12}{5}\right)e^{-5t}.
\]

Its constant, linear and quadratic terms cancel exactly, leaving `75t³/2` first. The full kernel remains available; the Gamma endpoint does not replace the source.

For the discrete accumulator `G_b f(n)=sum_(k=1)^n b^(n-k) f(k)`, the reusable product law is

\[
\boxed{(G_bf)(G_cg)=G_{bc}[fG_cg+gG_bf-fg].}
\]

The radix multiplies, and the diagonal term is subtracted. This generates an associative algebra of finite labelled causal words. The original BBP square and cube compile into 26 and 164 collected words. A fixed polynomial degree d has a rational linear state of dimension d+1.

The actual phase `z_n=exp(2πihU_n)`, for any fixed nonzero integer h, has **no eventual finite linear recurrence over C(n)**. This extends the inherited fresh-prime endpoint argument through a fixed-number-field degree bound and algebraic coefficient descent. It leaves the exact nonlinear rule `z_(n+1)=exp(2πih r(n+1)) z_n^16` intact. Nonrecurrence does not imply cancellation; a coherent prime-root control is included.

## Rules that can be reused

| Operation | Exact rule or retained information |
|---|---|
| Multiply Laplace observations | Convolve their lag kernels; do not multiply kernels pointwise |
| Compose Gamma volumes at a common decay rate | Add the positive depth parameters by the Beta identity |
| Multiply discrete causal sums | Multiply radices and retain the negative equal-time correction |
| Include a nonzero seed | Retain the homogeneous product and all mixed seed/source terms |
| Multiply finite causal words | Use the terminating graded quasi-shuffle recursion and collect identical labelled words |
| Apply an affine step to polynomial reports | Use the finite triangular binomial matrix |
| Take a phase | Use the character law after forming the exact lift; it is a nonlinear observation |
| Apply fractional weights before taking a phase | Retain integer lifts modulo the reduced weight denominators |
| Apply a forward Gamma filter to raw BBP states | Require tempering rate `λ>15`, or subtract the exact unstable boundary at rates `0<λ≤15` |
| Move between Mellin and shift descriptions | Retain endpoint terms and `EN=(N+1)E` |

The rate-one Gamma filter is valid on the bounded Green tail and on unit phases. It diverges on the raw exponentially growing real states. With tempering rate λ>15 there is an explicit convergent source formula. At smaller rates the unique homogeneous subtraction is `16^n π/16`; an arbitrary approximate boundary is insufficient at infinite depth. These are precise domain rules, not a physical-gauge identification.

## Executable artifacts

- [bbp_volume_algebra.py](../../../observational_succ/bbp_volume_algebra.py): rational labelled words, graded products, source evaluation, polynomial lifts, exact phases/carries and Gamma convergence guards.
- [bbp_gamma_kernel_algebra.py](../../../observational_succ/bbp_gamma_kernel_algebra.py): exact signed partial fractions, inverse-Laplace Gamma kernels and endpoint jets, with explicit finite budgets.
- [THEOREMS.md](THEOREMS.md): all-domain mathematical statements and proofs.
- [CLAIM_LEDGER.json](CLAIM_LEDGER.json): assumptions, scope, evidence, controls and remaining debt.
- [PROVENANCE.md](PROVENANCE.md): precise inherited mechanisms and primary references.
- [VALIDATION.md](VALIDATION.md): executed counts, independent reconstructions and reproduction commands.
- [NEXT.md](NEXT.md): the remaining signed estimate and the probe that would change the verdict.

Example, from the repository root:

```python
from observational_succ.bbp_volume_algebra import bbp_expression, bbp_channels, evaluate

u = bbp_expression()                    # four signed poles, radix 16, zero seed
square = u.power(2)                      # 26 source-labelled causal words
states = evaluate(u, bbp_channels(12), 12)
assert evaluate(square, bbp_channels(12), 12) == tuple(x*x for x in states)
```

The assertion is a finite replay of a proved rule. It is not an infinite signed-cancellation test. The compiler preserves an explicit source table and resource budget; it does not treat an unexecuted infinite expansion as received observation.

## Research verdict

**Survives:** expansion produces useful, exact generic rules and an authenticated joint algebra for finite BBP state, phase and carry operations. It also reveals a provable change in linear closure at the phase observation.

**Remaining target:** control the complete original signed temporal sums, with growing phase/carry information retained. Neither a Gamma marginal nor a finite polynomial normal form currently supplies that estimate. No base-16 normality or RH claim is made.

**Companion work:** concurrent [draft #636](https://github.com/femboy2112/SUCC/pull/636) develops the polynomial-Mellin normal form, finite-difference Gamma faces and a signed moving-Mellin bound. Its exact theorem commit was inspected here; its code and test counts are not included in this branch. The provenance note explains how its Gamma(k+2) difference hierarchy differs from this round's Gamma(2j) convolution hierarchy.
