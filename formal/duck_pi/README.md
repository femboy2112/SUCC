# Pinned Duck / π proof project

This project builds with Lean 4.14.0 and the exact mathlib/transitive revisions
in `lake-manifest.json`. It is a research proof project, not a new installed
proof-authority registry. See the [actual receipt](../../research/2026-10-21/DUCK_PI_KERNEL_RECEIPT.md).

```sh
lake exe cache get
cd ../..
python formal/duck_pi/check.py --output /tmp/succ-duck-pi-kernel
```

Run from a committed checkout. The checker binds inputs to HEAD, removes stale
project oleans, compiles the sources, exports actual types and axiom dependencies,
and runs semantic mutations with positive controls. It records complete compiler
logs, source/type hashes and generated finite certificate proofs. Failed modules
and blocked controls remain failures; a successful JSON field is never accepted
as independent authority.

| Source | Scope |
|---|---|
| `../DuckPrinciple.lean` | Declared commuting actions and finite words; arbitrary state/action types |
| `../DuckObserver.lean` | Observable quotient, universal descent, finite relation validator soundness |
| `BaileyCrandall.lean` | Exact rational source, summability, geometric tail and clocked orbit |
| `BBPIntegral.lean` | Classical BBP identity via calculus and dominated termwise integration |
| `PiSource.lean` | Actual `Real.pi` identity and source-sensitive circle transport |
| `LogisticFactor.lean` | Continuous onto circle/logistic semiconjugacy and noninjectivity |
| `Normality.lean` | Canonical overlapping blocks, interval distribution and separate Fourier/Haar predicates |
| `WeylBridge.lean` | Character cancellation to continuous-test Haar limits |
| `HaarBoundary.lean` | Empirical probabilities and null-boundary observation frequencies |
| `HaarIntervals.lean` | Canonical circle cylinders and conditional Fourier-to-normality chain |
| `AsymptoticTransport.lean` | Actual BBP shadowing, Haar transport and conditional pi normality |

The receipt, rather than this module inventory, determines which exact revisions
have actually compiled. No source-specific Fourier cancellation is assumed
silently, and no declaration concludes unconditional π normality. The standard
allowed axiom set is `propext`, `Classical.choice`, and `Quot.sound`; the recorded
set is inspected separately for every declaration.
