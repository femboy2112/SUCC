# Operation Causal Lorentz Gluing (CLG)

**Research-only strictly additive child of SUCC PR #481** pinned
`7237c2ae8b7b98557f39e47e8988b033404b587a`.
The original four signed BBP source and literal `U0=0` are untouched.

**What is mathematically earned:** exact four-bit/source-step 2-adic precision
cone; inherited F(t) source-isometry expressed as an exact observer-frame
conjugacy; canonical source-algebra cotangent lift into split `(4,4)` geometry;
source-selected eighth-return **auxiliary** Lorentz factor
`gamma=257/32`, `beta=255/257`; exact frame composition and hostile no-go
showing local congruence cannot determine selected real phases.

**What is NOT earned:** a physical value of c, GR curvature, a new signed
real Weyl saving, π normality, RH, or canonical equivalence of the BBP
generating-coefficient clock with the source recurrence clock. The two c-like
quantities are typed separately. Gamma is classical Lorentz gamma, **not**
Euler's gamma function or a tested dynamical law of real π digits.

Files: `PROOFS.md` (full derivations/status), `SOURCE_MAP.md` (typed arrows),
`NEXT.md` (verdict-changing attack), `CODEX_HANDOFF.md` (execution),
`PREREGISTRATION.md`, `EXACT_RECEIPT.json` (exact integers),
`independent_symbolic.py` (SymPy independent implementation),
`causal_lorentz.py` (stdlib Fraction source/dual/frame instrument),
`probe.py` (preregistered finite replay), and two focused root tests.

Run from a genuine checkout:

```
python -m unittest discover -s tests -p 'test_causal_lorentz*.py' -v
python research/2026-11-03/causal_lorentz_gluing/probe.py --verify
python research/2026-11-03/causal_lorentz_gluing/independent_symbolic.py
```

The inherited parent #481 source is used **read-only** through its existing
research module. Not a new production package or independent theorem kernel.
