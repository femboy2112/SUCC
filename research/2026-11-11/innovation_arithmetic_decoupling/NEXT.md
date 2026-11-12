# Next — the single strongest falsifiable obligation

**π normality remains OPEN.** This file names one obligation, why it is the right one, what would
count as progress, and what would refute it. It was rewritten in the continuation round
(2026-11-11, ZSC): the previous obligation WALL-16 is kept below as a necessary condition, with
its ladder corrected by ZSC-01.

## The obligation: (CH)

> **Positive density of digit changes.** Prove that there are `c > 0` and `B_0` such that for every
> `B ≥ B_0` at least `cB` of the positions `n ∈ [B, 2B)` satisfy `d_n ≠ d_(n+1)` in the
> hexadecimal expansion of π — equivalently (ZSC-03), that the literal carries
> `κ_n = ⌊U_n⌋ - 16⌊U_(n-1)⌋` of the zero-seeded rational source change value at `≥ c'B` of the
> times in every large shell.

**Why this one.**

- It is **sufficient** for the primary target of the programme at one specified mode:
  `(CH) ⟹ limsup_B |W_B(1)| < 1` and `limsup_B |D_(B,1)| < 1`, with the explicit saving
  `c/65793` (ZSC-02(c)). It is the only *density* statement in this dossier shown to imply a
  saving at mode 1.
- It is **equivalent** to a real saving at the single mode `h = 15` (ZSC-02(a,b)). It is not the
  weakest signed statement: a fixed saving at mode 1 is strictly weaker (witness `ξ_(1/2)` of
  ZSC-01 Remark 4: `c_B → 0` on a sequence of shells, yet `limsup |W_B(1)| < 1`); the rungs below
  (CH) are identified in `research/2026-11-12/frontier_rungs/LIMIT_FACES.md` (R0, R1).
- It is a statement about escapes of the `×16` orbit from its fifteen fixed points `j/15`, in the carry
  language of the rational source, with no tail and no seam hypothesis.
- It is far below normality (`c_B → 15/16`), and far above what is known: the best explicit all-`N`
  count is `≥ log_42 N - 2` changes among the first `N` digits (ZSC-04, from Mahler's bound), and
  for irrational algebraic numbers `≫ (log N)^(3/2)(log log N)^(-1/2)` (Bugeaud–Evertse).

**What it costs (necessary conditions, proved).**

| Statement | Needs, at denominators `16^m` or `15·16^m` | Status of that input |
|---|---|---|
| L2: one change in every large shell | endpoint `‖15·16^m x‖ ≥ c·16^(-m)` (`v ≤ 1`, no ε) | OPEN; `μ(π) = 2` would give `1 + ε` only |
| L3 = (CH) with density `c` | exponent `≤ (1-c)/(1+c) < 1` (ZSC-02(d)) | OPEN; **no bound on `μ(π)` can supply it** (`v_16 ≤ μ - 1`, `μ ≥ 2`) |
| any fixed saving `η` at any mode | exponent `≤ (2-η)/(2+η) < 1` (ZSC-01) | OPEN; same remark |
| decay at one mode | exponent `0` (ZSC-01, Remark 3) | OPEN |

The refereed starting line is still `v_16(π) ≤ 6.1033`. WALL-16 ("a BBP-specific bound below
`6.1033`") therefore remains a necessary first rung, but ZSC-01 changes its reading: the wall that
matters is not the borderline `v = 1` with a logarithmic gain, it is `v < 1`, and that region is
unreachable by any theorem about the unrestricted irrationality exponent. A proof must work at
the restricted denominators themselves.

**What would count as progress.**

1. (CH) for π, or for **any** nonzero element of the period space `V` of ZSC-06 (`log 2`, `log 3`,
   `√2·log(1+√2)`, … are proper zero-seeded sources of the same class). None is known.
2. L2 for π: a digit change in every shell `[B, 2B)`.
3. A restricted exponent `< 1` at denominators `16^m` or `15·16^m` for any nonzero element of `V`.

An argument for (CH) must fail for the null source `A_0`, for the hostile source `g_H` (zero
seed, positive `O(n^(-2))` forcing, complete census, completed point 2), for W1, W2 and for the
Shallit point. An argument for L2 must fail for `A_0`, `g_H` and W2. An argument for target 3
must fail for `A_0`, `g_H`, W2 and the Shallit point. W3 satisfies all three targets and is a
positive control; W1 satisfies L2 and target 3; the Shallit point satisfies L2. (Corrected
2026-11-12 after the re-audit: the earlier sentence demanded failure on all of W1–W3 and the
Shallit point for every target, which is false.)

**What would refute or redirect it.**

- A nonzero element of `V` with change density tending to 0 would refute the natural conjecture
  that (CH) holds throughout `V \ {0}` and would make the forcing coefficients themselves the
  missing invariant.
- A proper zero-seeded source outside `Q·A_0` with rational completed point is impossible by
  ZSC-06(e); an exhibited one would mean an error there or in the use of Baker's theorem.

## Falsifiable finite companion: SEAM-FREE (unchanged)

> **Conjecture (finite-checkable).** For the literal zero seed, `κ_n ≠ 16` and `ε_n = 0` for every
> `n ≥ 0`.

Verified for `n ≤ 3200` earlier and re-observed for `n ≤ 2600` here. One event at any `n` refutes
it. The density form `ρ(N) = o(N)` stays OPEN and is **demoted** (ZSC-05, ZSC-07): it is logically
independent of (CH) and of the wall for seeded carriers of the authentic forcing, and by ZSC-03
the one seam-related fact needed downstream — the letter 16 has density zero — is unconditional.

## Second-priority obligations

1. **Re-read Baker's theorem at source** and replace the from-memory quotation in ZSC-06(e); then
   record the effective irrationality exponent for the class `V \ {0}` if a usable statement
   exists.
2. **Sufficient mesoscopic gate (IAD-06)**, unchanged; by ZSC-01 it requires exponent `< 1`.
3. **Band extremal constant (O-7)** and the Graham–Kolesnik import (IAD-04x), unchanged.

## Next verdict-changing probe

The previous round proposed kernel-checking the unrefereed Lean development of `μ(π) = 2`. The
literature preflight of this round found no independent kernel pass on record (see SOURCE_MAP),
and ZSC-01 shows that even a confirmed `μ(π) = 2` yields `v_16 ≤ 1 + ε` and therefore **no**
saving, no (CH) and not even L2. That probe is no longer verdict-changing for this programme.

The probe that would change the verdict is on the other side: **search the class `V` for a
restricted-denominator construction.** Concretely, for the simplest element (`log 2`, where
Padé-type approximants with denominators `2^a·d_k` are classical), determine whether a bound
`‖2^m log 2‖ ≥ 2^(-cm)` with an explicit `c < 1` is proved in the literature (the helper could not
confirm the recollected value `c ≈ 0.79` attributed to Rhin 1987) and, if so, whether its method
transfers along the four-dimensional family `{K·q}` of ZSC-06(d) to the π-line. Outcome A: such a
bound exists and transfers — the first source-class statement below the wall. Outcome B: it
exists for `log 2` and provably uses a structure the π-line lacks — that structure is the named
missing invariant. Outcome C: no restricted bound below 1 exists for any element of `V` — L2 is
open across the whole class and is the honest frontier.
