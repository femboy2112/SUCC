# Operation SHARP CLOCK — source-native all-order Laurent transport obstruction

**Research-only DRAFT child of [PR #454](https://github.com/femboy2112/SUCC/pull/454)** at `a3802f2c1574362a4fb38cc85ab149a0ccb847f2`. This additive package neither modifies original source/seed nor introduces a second SUCC category spine.

## Main mathematical result

For the authentic four signed BBP poles and the **explicitly changed real initial state** `s*=-π/16`, let `F^[d]` be the Laurent lag correction through order `n^-d` (with `d=1` the empty correction). For **each fixed integer order `d>=1`, each fixed `h!=0`, and every real `d+1<c<d+2`**, the source-corrected signed-lag score at `K_N=floor(c log_16 N)` converges to

`2(d+1)/c - ((d+1)/c)^2`,

while the true same-forcing coherent lag score converges to `1`. Thus their gap tends to the **strictly positive** number

`(1-(d+1)/c)^2`.

The inherited `d=1` case is Main XVIII PR #435. The `d>=2` cases are the new advance. The original-four-pole leading Laurent coefficient `c_d` is nonzero at every order, with sign `(-1)^(d+1)`; the proof uses exact derivative/monotonicity bounds and a near-zero derivative exponential-sum lemma. Exact rational controls are executable and independent of the parent implementation.

**Consequence:** PR #454's vanishing seed-*uniform* source transport windows at coefficient `(d+1) log_16 N` have a **sharp coefficient barrier**. Extending them to larger coefficients using only the same truncated Laurent normal form is false for a genuine same-forcing real orbit.

**Not proved:** a barrier for the literal selected `U0=0`, a selected signed saving, base-16 normality, RH, a physical quantum law, or any claim that `d` can grow with N without new uniform analysis.

## Reproduce (from repository root)

```bash
python -m unittest discover -s tests -p 'test_laurent_clock_sharpness.py' -v
python research/2026-11-01/laurent_clock_sharpness/finite_probe.py --check
python research/2026-11-01/laurent_clock_sharpness/symbolic_probe.py
```

The 15 new unittest methods stress hundreds of exact Fraction identities and hostile controls. The optional SymPy oracle checks 25 derivative/limit/source identities through a different calculation. The retained receipt is a finite diagnostic, not the universal proof authority.

Start with [PROOFS.md](PROOFS.md), [CLAIMS.md](CLAIMS.md), [VALIDATION.md](VALIDATION.md), and [NEXT.md](NEXT.md).
