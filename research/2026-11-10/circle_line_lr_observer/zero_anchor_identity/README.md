# SUCC — Zero-Anchored Dedekind Fingerprint and Signed-Observer Bridge

**Research draft, 2026-11-10/11.** Additive continuation of the exact SUCC #596 head `88cd40b478ec823151cb6c08b04b67596efb3ada`. The original signed four-pole BBP source, literal `U_0=0`, imported provenance, Lean, workflows and main are unchanged. Nothing here proves pi base-16 normality, original-zero parity balance, or RH.

## The object

The source-selected number `x=pi/16` is represented by a *certified, effective rational Cauchy name*, not an approximate pi constant:

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`;
`P_n=sum_(j=1)^n 16^(-j)r(j)`;
`I_n=(P_n,P_n+r(n+1)/(15*16^n))`.

Every interval strictly contains the same source-selected limit, and `width(I_n)<16^(-n)`. The **classical BBP identity** identifies its 16-fold multiple with geometric pi. A *different* rational interval name from SUCC #595's Euclidean-circle beta recurrence provides a second computational witness, yielding strict finite intersections whose width tends to zero. Finite agreement is a check; the identification of both mathematical limits is an imported theorem, not established by agreement alone.

The distinguished **zero source section** is `U_0=0`, `U_(n+1)=16 U_n+r(n+1)`. The recovery observable `Z_n=16^(-n) U_n-P_n` is identically zero at every clock on that section. This is not enough if the observer forgets unwrapped states. Preserve *all* clock, source, winding and seed coordinates.

### The irrational counterseed does not get to escape

Extend seeds to the exact rational module `Q + Q*x` using pairs `(constant, coefficient)`. Because pi is irrational, this is a free two-dimensional `Q`-module. The module enables finite and *exact* algebraic checks even for the coherent counterseed `s=-x`, which previously lived outside rational-only seed code. That seed has completed phase `16^n(x-x)=0` for every n but recovered seed `(0,-1)`, and is rejected by a literal-zero anchor. The rational seed `s=1/16` has phase aliases for n>=1 but recovered seed `(1/16,0)` and is also rejected.

A decidable seed-normal-form test is claimed **only** inside this declared module; general computable-real equality remains undecidable. Full rational-affine seed equality uses the **imported classical irrationality theorem**, not finite approximation.

### The finite algorithm can reach arbitrary π precision, not print π in finitely many steps

For any rational `epsilon>0`, finite source refinement gives a certified interval of width `<epsilon`; the mathematical intersection of all those closed intervals is a singleton `x`. Every rational comparison against `x` is eventually resolved because x is irrational. The rational-cut presheaf `Y_x(q)=[q<x]` and any productive Stern–Brocot path are thus recoverable without executing an infinite program. There is **no** uniform stage bound for comparisons with every rational q and no decision procedure for comparing arbitrary computable reals for equality.

## Normality machinery is *not* erased

`zero_anchor.py` attaches to the **same** source-locked x:

1. The exact phase and integer-carry chart `theta_n={16^n x}`, authenticated real tail `T_n=16^n(x-P_n)`, and finite hexadecimal word counts.
2. Strict rational bounds for the smooth Weyl observer, the moving-epoch Weyl observer, and #593's distinct 2:3 joint Fourier observable. Error bounds are quantitative; signed decay remains OPEN.
3. Exact rational midpoint computation of #591's interval-metric `D_N=W_1(mu_N,Qmu_N)` and its adjacent-block **signed CDF overlap** `Omega_M=(D_M^-+D_M^+)/2-D_(2M)`, plus rigorous source-selected absolute error bars.

The CDF error bound is **conditional on each finite phase interval staying within one radix-16 chart**. This is certified before transport. Without that condition, circle translation followed by interval cutting jumps at rational branch seams and the supposed universal Lipschitz estimate is false. The test suite contains a concrete seam counterexample.

The program gives exact finite diagnostics and a faithful input interface for the missing source-derived signed estimate, **not** that estimate itself. Normality is not inferred from the root's uniqueness, the output's accuracy, or positive finite overlap.

## Focused reproduction

```
cd research/2026-11-10/zero_anchor_identity
python -W error -m unittest -v test_zero_anchor.py
python -m compileall -q zero_anchor.py test_zero_anchor.py
```

Only Python stdlib `fractions.Fraction`, `dataclasses`, `collections`, and `unittest` are used. No decimal pi, float, BBP digit table, mpmath, or trigonometric call enters a certificate.

- [`THEOREMS.md`](THEOREMS.md): source/seed uniqueness, affine clock, Yoneda/cut, phase budget and signed Haar error proofs.
- [`HOSTILE_GATES.md`](HOSTILE_GATES.md): precisely scoped adversarial controls and missing normality claims.
- [`VALIDATION.md`](VALIDATION.md): local focused tests, raw receipts, and repository-integration limits.
- [`zero_anchor.py`](zero_anchor.py): standalone exact rational witness construction.
- [`test_zero_anchor.py`](test_zero_anchor.py): executable calibrations and mutation controls.

**Scope:** proved paper statements under named classical inputs + 20 finite unit tests; no Lean formalization, no mandatory whole-SUCC suite, no independent external referee. Source-level integration into #591/#592/#593 is an interface proposal until their branch ancestry is reconciled.
