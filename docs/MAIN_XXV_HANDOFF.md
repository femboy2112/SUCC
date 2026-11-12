# Main XXV — resume below the canonical target

This handoff continues the [Main XXIV handoff](MAIN_XXIV_HANDOFF.md), whose source equations,
interfaces and missing theorem are unchanged. **π base-16 normality, the source-selected signed
estimate, R0, R1, digit-change density (CH), original-zero parity balance, universal completed
Weil positivity, Goldbach and RH remain OPEN.** Definitions and status: [frontier](PI_NORMALITY_FRONTIER.md)
§9. Scope and corrections: [claim supplement](CLAIM_SUPPLEMENT_MAIN_XXV.md). Exact commits, trees
and receipts: [integration audit](SUCC_MAIN_XXV_INTEGRATION_AUDIT_2026-11-12.md) and
[manifest](SUCC_MAIN_XXV_INTEGRATION_MANIFEST_2026-11-12.json).

## 1. What is new, in one table

| Tool | Entry point | What it establishes | What it does not |
|---|---|---|---|
| Fejér schedule, innovation/history split, adelic no-go | [THEOREMS](../research/2026-11-11/innovation_arithmetic_decoupling/THEOREMS.md) (IAD-01…09) | the schedule is free; the innovation cancels alone only in a mesoscopic lag window; "decoupling" is the completed lag correlation; one missing place suffices for a coherent hijack | any saving for the zero seed |
| Saving–exponent law, digit-change rung, carry renewal, source moduli | [CARRY_FLUX](../research/2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md) (ZSC-01…07) | a fixed saving forces `v_16 < 1`; (CH) ⟺ real saving at mode 15; the letter 16 has density zero in every carry stream; gauge of sources; zero seed ⟺ `π/16 ∈ V` | (CH) |
| Limit faces and thresholds | [LIMIT_FACES](../research/2026-11-12/frontier_rungs/LIMIT_FACES.md) (LMF-01…06) | the ladder R0 ⟸ R1 ⟸ (CH) ⟸ (CH_k) ⟸ … ⟸ normality with witnesses; thresholds `1/4`, `1/60`, `1/(4(16^k−1))` in `W_1` and `D` | that any late shell of π is below a threshold |
| Restricted exponents | [RESTRICTED_EXPONENT](../research/2026-11-12/frontier_rungs/RESTRICTED_EXPONENT.md) (RDT-01…08) | transference at `g·b^m`; `v_16(log(16/15)) ≤ 0.8813` (import) and L2 for that element of `V`; `v_2(log 2) ≤ 2.3814` | any restricted bound for π below `6.1033` |
| Kernel-checked carry lemmas | [lean](../research/2026-11-12/frontier_rungs/lean/README.md) | ZSC-02 locality, ZSC-03 renewal, ZSC-06 null relation | anything statistical |
| Prime fixed-point observers (pinned snapshots of active work) | [observer](../research/2026-11-12/prime_fixed_point_observer/README.md), [cylinder](../research/2026-11-12/prime_fixedpoint_cylinder/README.md), [Scott defect](../research/2026-11-12/scott_relative_defect/README.md), [carrier](../research/2026-11-12/carrier_first_goldbach/README.md) | elementary operator and category identities for prime fixed points, exact finite certificates, reformulations of Goldbach | Goldbach, or any estimate; see the supplement for corrections |

## 2. The exact statement to prove next

Let `z_n = {16^n·π/16}` and `W_B(h) = B^(-1) Σ_(n=B)^(2B-1) e(h z_n)`.

> **R0.** There are `η > 0` and `B_0` such that `Re W_B(1) ≤ 1 − η` for every integer `B ≥ B_0`.

Equivalent forms (all proved, for every real number): there are `c > 0`, `B_0` with at least `c·4B`
positions `m ∈ [4B, 8B)` at which consecutive binary digits of π differ; `δ_0` is not a weak-*
limit of the shell measures; `limsup_A Re B_A(1) < 1` for the Basel shell quantity of
[frontier](PI_NORMALITY_FRONTIER.md) §4. Sufficient: `D(ν_B) ≤ 1/4 − ε` for all large `B`.
R0 is implied by every other rung and by the Main XXIV theorem at `h = 1`.

Necessary for R0 with density `c`: `‖2^m π‖ ≥ 2^(−((1−c)/(1+c))m − 4)` for large `m` — a restricted
exponent below 1 at powers of two, **OPEN** for π. So a proof of R0 must contain a new Diophantine
fact about π at dyadic denominators *and* a medium-scale argument; the first alone is not enough
(explicit points have exponent 0 and fail R0).

## 3. Intermediate targets, each falsifiable

1. **R0 or (CH) for `ξ_* = log(16/15) = Σ_(n≥1) 16^(-n)/n`.** A proper zero-seeded element of the
   period class `V` whose restricted exponent is `≤ 0.8813` (import) and for which every large
   shell contains a digit change. The Diophantine law no longer excludes savings `η ≤ 0.126` there.
   A proof must be a medium-scale argument. A sequence of shells of `ξ_*` approaching `δ_0` would
   refute the conjecture that `V ∖ {0}` is uniformly normal.
2. **A convergent family `A_n π − B_n` with `v_2(A_n) − v_2(B_n) ≥ cn`** (a restricted exponent for
   π below the unrestricted one), or a proof that the 2-adic shadow of RDT-06(a) together with
   `v_2(A_n) ≤ v_2(B_n) + o(n)` holds for every family built from Gaussian logarithms.
3. **Explicit starting indices** `m_0` for RDT-05 and RDT-07, and an interval enclosure of
   `Λ(1,16,1)`.
4. **Read Baker's theorem at source** (ZSC-06(e) still quotes it from secondary sources).

## 4. Controls every argument must survive

Those of [frontier](PI_NORMALITY_FRONTIER.md) §7 and §9, and in particular: the coherent seed
(`D = 15/32`); the null source and the hostile zero-seeded source `g_H` of ZSC-06; points with
`v_16 = 0` failing each rung (LMF-03); `ξ = 1/15` (R0 holds, R1 fails); the two-digit run point
(R1 holds, (CH) fails); the Shallit point (`μ = 2`, no saving); W3 of ZSC-05 is a *positive*
control (it satisfies (CH)).

## 5. Replays

```sh
export PYTHONPATH="$PWD"
python scripts/main_xxv_research_gate.py --out <directory outside the checkout> \
    [--lean-dependency-project <prebuilt formal/mathlib_bridge>]
python scripts/main_xxv_manifest.py --check docs/SUCC_MAIN_XXV_INTEGRATION_MANIFEST_2026-11-12.json --integration HEAD
python scripts/main_xxiv_research_gate.py --out <directory outside the checkout>   # Main XXIV dossiers, unchanged
```

Finite replays are instance checks. Neither a passing probe nor a shell below a threshold changes
the status of an open claim.
