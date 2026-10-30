# Seed-alias classification and the carry obstruction (Operation Main XVI, P2 + P3)

**Status:** PROVED (exact finite arithmetic over ℚ; the one irrational counterseed in
high-precision mpmath), with an independent modular-arithmetic oracle. Repairs an over-generalized
control contract in the Main XV handoff and delivers the Main XVI obstruction. **π base-16/base-3
normality and RH remain OPEN.**

## SA-1. The affine seed law

For the authentic clock `r(n) = R(8n−7)` and `U_n(s) = 16 U_{n−1}(s) + r(n)`, `U_0(s) = s`:

> **Lemma.** `U_n(s) = U_n(0) + 16^n s` for every `n ≥ 0`.

**Proof.** `D_n := U_n(s) − U_n(0)` satisfies `D_0 = s` and `D_n = 16 D_{n−1}` (the forcing `r(n)`
cancels), so `D_n = 16^n s`. ∎ (Exact check: `test_triangle_genesis_repair.py::P2…::test_affine_law`.)

Consequently the selected circle phase `e(h U_n(s)) = e(h U_n(0))·e(h·16^n s)` depends on the
changed seed only through `16^n s (mod 1)`. The whole classification follows from the arithmetic of
`16^n s (mod 1)`.

## The seven distinguishability classes

Let `e(x) = exp(2πi x)`. Authentic seed is `s = 0`. Fix an integer `h ≠ 0`.

1. **Unwrapped source / initial-boundary information.** The *real number* `U_n(s)` (before `mod 1`),
   i.e. its integer part together with the seed `s` itself. This is the finest datum; everything
   below is a quotient of it. The authentic contract `U_0 = 0` lives here.

2. **Exact circle-phase alias — `s ∈ (1/16)ℤ`.** If `s = k/16` (`k ∈ ℤ`), then
   `16^n s = k·16^{n−1} ∈ ℤ` for all `n ≥ 1`, so `e(h U_n(s)) = e(h U_n(0))` for **all** `n ≥ 1` and
   all integers `h`. The circle phase cannot tell `s` from `0` at any observed time `n ≥ 1`.
   (`test_class2_exact_alias_1_over_16`.)

3. **Eventual circle-phase alias — `s ∈ ℤ[1/16]`.** If `s = k/16^v` (lowest terms, `v ≥ 1`), then
   `16^n s ∈ ℤ` iff `n ≥ N₀ := ⌈(4-adic val of the denominator)/4⌉`. For `n ≥ N₀` the phase is
   identical to authentic; for `n < N₀` it is not. Onset is exactly `N₀` (e.g. `1/256 → N₀ = 2`,
   `1/65536 → N₀ = 4`). (`test_class3_eventual_alias`.)

4. **Constant-character twist — `s = p/q`, `q | 15` (`gcd(q,16)=1`, `16 ≡ 1 mod q`).** Then
   `16^n ≡ 1 (mod q)`, so `16^n s ≡ s (mod 1)` for **every** `n`, giving
   `e(h U_n(s)) = e(h p/q)·e(h U_n(0))` with a single global unit `e(hp/q)` independent of `n`
   (`q ∈ {1,3,5,15}`; e.g. `s = 1/3, 2/5`). More generally for `gcd(q,16)=1` the twist is periodic
   with period `ord_q(16)` — constant exactly when `ord_q(16) = 1`, i.e. `q | 15`. A seed with
   `q ∤ 15` (e.g. `s = 1/7`, period `3`) is a genuinely *periodic* (non-constant) twist, an
   eventually periodic orbit that **is** distinguishable (next row). (`test_class4…`,
   `test_periodic_twist_q7_is_not_constant`.)

5. **Absolute phase vs Weyl-sum magnitude.** For a constant twist (class 4) the whole sum picks up a
   global unit: `T_N(h)[s] = e(hp/q)·T_N(h)[0]`, hence `|T_N(h)[s]| = |T_N(h)[0]|` for **every** `N`
   and `h` (exact; `test_class4_constant_twist_magnitude_invariant`). So the Weyl-sum **magnitude**
   `|T_N(h)|` is blind to class 4, while the **absolute phase** `arg T_N(h)` is not. Magnitude is
   also blind, at every observed time, to classes 2–3 (identical phase ⇒ identical sum).

6. **Integer-lift / literal-carry information.** The carry `κ_n(s) = 16{U_{n−1}(s)} + r(n) − {U_n(s)}
   ∈ ℤ` records the integer wrap discarded by `mod 1`. It **distinguishes** class-2/3 aliases: `s`
   and `0` can share every circle phase for `n ≥ N₀` yet have different carry sequences (e.g.
   `s = 1/16`: identical phases `n ≥ 1`, but `κ_1` differs). The carry recovers part of class-1
   information that the circle phase destroys. (`test_carry_distinguishes_exact_alias`.)

7. **Genuine coherent nonnormal counterseed — `s* = −π/16`.** `U_n(s*) = U_n(0) − 16^{n−1}π = −T_n`
   (the BBP tail `0 < T_n < 1/(15(n+1)²)`), so `U_n(s*) → 0` and the selected phase
   `e(h U_n(s*)) = e(−h T_n) → 1` is **coherent**, while `{U_n(s*)} → 1⁻` has eventually-constant
   leading hex digits `F,F,F,…` — maximally **nonnormal**. This is the sharpest trap: same forcing,
   wrong seed, coherent phase, nonnormal orbit. Verified two independent ways
   (`test_counterseed_collapse`; oracle `counterseed_phase`): `T_8 ≈ 2.2e−4 → T_40 ≈ 9.6e−6`,
   `|phase−1|: 1.4e−3 → 6.0e−5`.

### Distinguishability matrix

| observable \ class | 2 exact alias | 3 eventual | 4 const. twist | periodic twist (q∤15) | 7 coherent `s*` |
|---|---|---|---|---|---|
| **circle phase** `e(hU_n)` | blind `n≥1` | blind `n≥N₀` | sees (global unit) | sees | sees (→ coherent) |
| **Weyl magnitude** `|T_N(h)|` | blind | blind | **blind** | sees | sees iff π normal* |
| **absolute phase** `arg T_N(h)` | blind | blind | sees | sees | sees |
| **literal carry** `κ_n(s)` | **sees** | **sees** | sees | sees | sees |

\* magnitude separates `s*` from authentic only *given* `|T_N(1)[0]| = o(N)`, i.e. only if π is
normal — which is the open question. This is why `s*` must be a **required-failure** control, not a
proved separation.

**Summation convention (n ≥ 1).** All sums `T_N(h) = Σ_{n=1}^{N} e(h U_n(0))` and the alias
statements above run over **observed times `n ≥ 1`**; the seed `U_0 = s` is the boundary datum, not
an observed term, and is excluded. The class-2/3 magnitude-invariance rows depend on this: including
the `n = 0` term, `s = 1/16` and `s = 0` differ (`U_0` differs, so `|Σ_{n≥0}|` differs — e.g.
`|diff| = 0.30` at `h = 1`). Class-4 twists are magnitude-invariant even with `n = 0` (the global
unit `e(hs)` factors out of every term including `n = 0`). So a reader must not run an `n = 0`-inclusive
sum on a class-2/3 seed and mistake the seed term for a genuine separation.

## Corrected control slate (repairs the Main XV handoff table)

The Main XV handoff demanded a candidate signed estimate **fail** for "rational changed seeds …
eventually periodic". That is over-generalized: classes 2–3 are *observationally identical* to the
authentic orbit under the circle-phase/Weyl readout the estimate itself uses, and class 4 is
*magnitude-identical*. Demanding a valid theorem fail on a seed that its own readout cannot
distinguish from the authentic one would force the theorem to contradict itself. Replace the single
"rational changed seeds → NO" row with:

| Control | Must a valid `|T_N(h)|`-type estimate FAIL on it? | Reason |
|---|---|---|
| Authentic `s = 0`, four signed poles | **NO** (it is the claim) | the authentic orbit |
| Coherent same-forcing `s* = −π/16` (class 7) | **YES** | the real trap: coherent, nonnormal |
| Exact / eventual circle alias `s ∈ ℤ[1/16]` (classes 2–3) | **NOT REQUIRED** | circle-identical to authentic for `n ≥ N₀`; a magnitude estimate *cannot* separate them — demanding failure is self-contradictory |
| Constant-character twist `q | 15` (class 4) | **NOT REQUIRED** | `|T_N(h)|` is exactly seed-invariant; magnitude-identical to authentic |
| Periodic twist `gcd(q,16)=1, q ∤ 15` (e.g. `1/7`) | **YES** | genuinely magnitude-distinguishable eventually-periodic orbit |
| Gamma-matched fake `Q_fake = 15x`, wrong/sign-flipped poles, parity/totient projection, i.i.d.-reset sensor, Kempner/de Bruijn digit controls, independent holdout | **YES** | source-structure mutants / nonnormal holdouts (unchanged from Main XV) |

The principle: a control is a *required failure* only for seeds the estimate's own observable can
actually separate from the authentic orbit. Source-mutant controls test the **declared hypotheses**
(four poles, `U_0 = 0`, native clock); they are not obliged to break every valid general lemma.

## P3. The carry obstruction (OB) and its limitation

> **Obstruction (OB).** The literal carry `κ_n(s)` separates circle-aliased seeds (classes 2–3):
> for `s ∈ (1/16)ℤ∖{0}` the orbits are circle-identical for all `n ≥ 1` yet `{κ_n(s)} ≠ {κ_n(0)}`.
> Hence the circle-phase alias is only a *circle-level* coincidence, not an arithmetic-trajectory
> coincidence — the full source trajectory is recoverable from the integer-lift marks.
>
> **But** `κ_n(s)` is a ℤ-valued source / integer-lift readout; under `s → s + ℤ[1/16]` it shifts by
> its own exact integer amount and conveys **no bound on** `|T_N(h)|`. The carry therefore
> distinguishes arithmetic trajectories that the Weyl magnitude aliases **without supplying any
> signed cancellation**.

**Why this is the honest outcome (and what it forbids).** The directive asked whether keeping the
source posterior, endpoint grades, radix-16 carry bins, Walsh sectors and `q=3/q=6` orientations
yields a *noncentral signed observable* that distinguishes actual arithmetic trajectories and
improves signed cancellation. The classification answers precisely:

- a **noncentral / absolute-phase** observable *can* distinguish class-4 twists (it reads `arg`), and
  the **carry** observable *can* distinguish class-2/3 aliases — so a distinguishing observable
  exists;
- **but** it is exactly an *invertible representation* (carry = part of the discarded integer lift)
  or a *source/absolute-phase scalar*, not a translation-invariant bound on `|T_N(h)|`. By the
  distinguishability matrix, any functional **determined by the magnitudes `{|T_N(h)|}`** (equivalently
  invariant under the global unit `e(hp/q)` — as a magnitude bound must be) is **blind to class 4**,
  and any functional of the circle phases alone is **blind to classes 2–3 for `n ≥ N₀`**. So no
  functional that is itself a bound on `|T_N(h)|` in this operative sense (magnitude-determined, or
  phase-only) can separate the aliased/twisted seeds. (The negation is *not* claimed for an arbitrary
  bundle: the pair `(\{|T_N(h)|\}, \{κ_n\})` trivially "contains" both a magnitude readout and the
  separating carry — but that bundle is not a bound on `|T_N(h)|`; its separating power lives entirely
  in the carry coordinate, which supplies no `|T_N|` saving. The honest statement is the scoped one
  above and the Limitation below, not a universal "no observable does both".)

This matches the standing SUCC obstructions (`SK2-B/C`, TG-06/08): recovering phases or carries is
observability/representation, and the universal seed-smearing zero `∫₀¹ H(u;s) du = 0` holds for
**every** seed including `s*`. The carry adds integer-lift resolution, not a Weyl saving.

**Limitation (explicit).** OB is a negative result. It does **not** produce a source-authenticated,
selected-history-sensitive bound on `|T_N(h)|`; it proves that the natural carry/noncentral
enrichments cannot be such a bound. `T_N(h) = o(N)` (equivalently `Sbar_N(h) = o(1)`) for the
authentic BBP orbit — π base-16 normality — remains **OPEN**, and no step here is evidence for it.

**Map to the authentic four-pole source.** Every object above uses the authentic `r(n) = R(8n−7)`
with the four signed poles `R(a) = 4/a − 2/(a+3) − 1/(a+4) − 1/(a+5)` and `U_0 = 0`. The affine law,
the carry, and the counterseed identity `U_n(−π/16) = −T_n` are all exact consequences of that
source; `s*` uses the genuine BBP tail `T_n`. No frozen source file, pole set, or seed is modified.

**Checks.** `seed_alias.py` (exact ℚ classification + carry), `independent_oracle_xvi.py` (modular
onset / `ord_q(16)` / convolution orbit / mpmath counterseed),
`tests/test_triangle_genesis_repair.py` classes `P2SeedAliasClassification`, `P2CoherentCounterseed`,
`P3CarryObstruction`, `CrossCheckIndependentOracle`.
