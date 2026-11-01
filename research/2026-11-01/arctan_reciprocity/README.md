# Operation ARCTAN × IRRATIONAL MIRROR — source-native one-quadrature normality gate

**Status:** research-only additive mathematical package stacked on SUCC categorical source gluing (PR #450). Every exact original four-pole BBP source and literal `U0=0` remains unchanged; no new π-normality or RH proof, quantum claim, new Lean certificate, or external scholarly priority.

## Why the arctan reciprocal is useful

The identity `atan(t)+atan(1/t)=sign(t)*pi/2` induces a projective circle reflection `t -> 1/t`. On its own the reflection has a rational half-turn axis and is too weak: a nonuniform ×16-invariant Cantor digit measure is also exactly invariant under it.

But the **original BBP source at n=2** gives `r2=106/819`. Rotate the reciprocal involution by the corresponding rational projective circle rotation:

```
J(t)=(106-819*t)/(819+106*t)
M=[[-819,106],[106,819]];  M*M=681997*identity
```

The angular axis `beta=atan(106/819)/pi` is *irrational*, although this is a rational Möbius map. Its Gaussian-rational phase `gamma=(659525+173628i)/681997` has infinite order. Its nontrivial commutator with `x -> 16x` is rotation by `gamma^15`.

The original BBP empirical circle measure is **asymptotically ×16-invariant with an explicit original-source O_h(1/N) error**, so *if* one proves asymptotic invariance under this single irrational mirror, π would be base-16 normal. The next open target is one real signed projection per harmonic:

```
lim_N (1/N) sum_{n<=N} Im[(819-106i)^h * exp(2pi*i*h*U_n)] = 0
for every fixed integer h >= 1; original four signed poles, literal U0=0.
```

This conditional gate and its finite quantitative inequality are fully derived in `PROOFS.md`; the open signed bound is NOT assumed. Its coefficient and mirror commutator denominator are **exact Gaussian-integer and rational computations**. No π input or numeric trigonometry is needed to certify the axis has infinite order.

## Files and reproducibility

- `PROOFS.md`: full derivation, categorical type/branch firewall, counterseed and nonuniform rational-axis controls.
- `arctan_mirror.py`: original source orbits as Fractions; rational projective mirror; Gaussian coefficients and exact denominator-square certificates; finite source error budgets; optional second geometric π/16 axis.
- `symbolic_probe.py`: independent SymPy source/dlog, projective/Cayley, reciprocal and ×16 audits.
- `finite_probe.py` and `FINITE_DIAGNOSTICS.json`: **16 finite mpmath diagnostic cases only** on authentic U_n (n=32/64/128/256, h=1/3/5/7).
- `tests/test_arctan_reciprocity.py`: root-discoverable stdlib tests, including the signed inequality and hostile rational-axis Cantor measure.
- `CLAIMS.md`, `SOURCE_MAP.md`, `VALIDATION.md`, `NEXT.md`: status and next proof obligations.

```
python -m unittest discover -s tests -p 'test_arctan_reciprocity.py' -v
python research/2026-11-01/arctan_reciprocity/symbolic_probe.py
python research/2026-11-01/arctan_reciprocity/finite_probe.py
```

Do not merge into main, promote claims, publish, tag or release automatically. No production modules or original proof contracts are edited.
