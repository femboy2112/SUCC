# Operation Minimal Carrier — the `4` from a minimal primitive pole grammar

**Draft, research-only.** Pinned parent SUCC PR #383 at `e02933591e7b7486376acb9847e00fd01d9ae498`. No main merge and no source/seed modifications. The original π base-16 normality conjecture and RH remain OPEN.

This round asks whether SUCC's reciprocal source center `4` can be *selected*, rather than noticed post hoc, using the author's primitive two-stage/carrier-minimality hypothesis. It achieves a **conditional exact selection theorem** and three independent arithmetic/analytic bridges. It also proves a sharp **signed cancellation no-go** for the resulting source-only logarithmic twist.

## Read in this order

1. [`RESEARCH.md`](RESEARCH.md): complete definitions, proofs, arithmetic Gamma/totient connection, strict countermodels and mathematical scope.
2. [`NEGATIVE_CONTROLS.md`](NEGATIVE_CONTROLS.md): why higher-weight centers, source mutations, φ-only matches and logarithmic twists do not prove π normality.
3. [`CLAIMS.md`](CLAIMS.md): scoped claim statuses, derivations and falsifiers.
4. [`VALIDATION.md`](VALIDATION.md): actual local executions, original source pins, raw receipts and hosted-CI limits.
5. [`NEXT.md`](NEXT.md): proposed zero-seed-sensitive signed carry transfer and its falsification criterion.

## Exact discoveries

- Primitive positive-integer four-pole source grammar: three equally spaced positive channels, balanced base pole, reciprocal root center aligned with middle pole. **The unique minimum total coefficient mass is 4**, at negative weights `(2,1,1)`, center-to-gap ratio `4`, source shifts `(3,4,5)` in unit spacing, and inversion scale `16`.
- At native BBP source clock `a_n=8n-7`, subtracting the asymptotic reciprocal log gives two explicit positive unit-length integrals on the line with denominators `24n-6` and `40n-20`, detecting the outer prime poles `3` and `5`.
- Exact finite Gamma product and an Euler–Mascheroni-renormalized constant `K≈0.0522061421970576`; **rigorous rational error <7/(180N)**. The older golden Oily constant `λ−γ` is distinct, even though both contain the same Euler finite part.
- Exact CRT multiplicative isomorphism of the eight units modulo `15=3·5` and modulo `16=2^4`; an **exact 16×16 hybrid Gaussian-unit-character + even-digit Walsh observation basis** retains every hexadecimal state. Higher Fermat stage `255/256` is a counterexample to extending group equivalence from equal totients. The complete basis is not a normality theorem.
- Independently reconstructed authentic BBP polynomial resultant/discriminant have exceptional primes only `2,3,5`.
- Source-only log reweighting changes every bounded normalized phase average by only `O(log N/N)`. Even the accumulated **complex phase** has coherent Cesàro modulus `1/sqrt(1+(c/15)^2)>0` for every fixed `c`, including the actual same-forcing coherent seed `−π/16`. Thus **no signed Weyl saving has been established**.

## Reproduce with Python

```
python minimal_pole_gamma.py
python fermat_unit_bridge.py
python -m unittest discover -s . -p 'test_*.py' -v
python independent_oracle.py           # SymPy 1.14
python numerical_holdouts.py           # mpmath 1.3, numerical only
python certified_interval.py           # exact Fraction interval and tail
```

The two arithmetic implementations and all focused tests require only Python's standard library. The independent oracle needs SymPy, and high-precision observations need mpmath. The full SUCC repository is not cloned into this local workspace due outbound Git DNS restrictions. Native `AGENTS.md` root gates and hosted exact-head CI must be run/reviewed separately before any integration.
