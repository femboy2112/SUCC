# Next — the single strongest falsifiable obligation

**π normality remains OPEN.** This file names one obligation, why it is the right one, what would
count as progress, and what would refute it.

## The obligation: WALL-16

> **Bound the base-16 Diophantine exponent of π from the four-pole source.**
> Prove, using the BBP source structure and not only a general irrationality measure, an explicit
> `v* < 6.1033` such that for all large `n`
>
> ```text
> ‖16^n x‖ ≥ 16^(-v*·n)        (x = π/16),
> ```
>
> equivalently: a run of literal carries `κ = 15` (or of hexadecimal digits `0`/`F`) starting at
> time `n` has length at most `v*·n + O(1)`.

**Why this one.** By IAD-08, *every* estimate this programme is looking for — a Weyl bound for one
mode, a bound on a single lag correlation, with any fixed saving `η > 0` on all large shells —
implies `‖16^B x‖ ≥ c·B·16^(-B)`. So no source-selected signed estimate can be proved by a method
that does not, along the way, prove WALL-16 with `v* ≤ 1`. The refereed record is `v* = 6.1033`
(from `μ(π) ≤ 7.1032`), with no base-restricted improvement known. WALL-16 is therefore the first
rung that any successful mechanism must climb, it is strictly arithmetic, and it is stated in the
carry language of the rational source (RIO-11, SWT-03).

**Ladder of thresholds.**

| `v*` | Meaning | Status |
|---|---|---|
| `6.1033` | general irrationality measure | refereed record (import) |
| `< 6.1033` by a BBP argument | first source-specific Diophantine gain | **OPEN — this obligation** |
| `1 + ε` | would follow from `μ(π) = 2` | unrefereed claim exists; not imported |
| `1`, sharp with a `log` gain | necessary for any fixed-saving shell estimate (IAD-08) | OPEN |
| `0` | necessary for normality | OPEN |

**What would count as progress.** Any proof of `v* < 6.1033` that uses the forcing, the zero seed
and the complete place census (all three are needed: see the table closing OBSTRUCTIONS). The
argument must visibly fail for the coherent seed, for the IAD-07 hijack seed and for the AT-07
forcing; an argument that goes through for any of them is wrong.

**What would refute or redirect it.**

- A same-forcing seed family that satisfies every source-side carry constraint currently available
  (RIO-09/10, IAD-09) and has 15-carry runs longer than `v·n` for every `v < μ(π) - 1` would show
  that the source structure recorded so far yields nothing beyond the general measure, and that a
  new invariant is required before WALL-16 can be attacked.
- An independent kernel check of the unrefereed `μ(π) = 2` formalization would move the starting
  line from `6.1033` to `1 + ε` and make the sharp borderline the live obligation.

## Falsifiable finite companion: SEAM-FREE

> **Conjecture (finite-checkable).** For the literal zero seed, `κ_n ≠ 16` and `ε_n = 0` for every
> `n ≥ 0`; equivalently `{16^n x} ≥ T_n` for all `n`, i.e. the hexadecimal digits of π are exactly
> the shifted literal carries, `d_n = κ_(n+1)`, with no seam event ever.

Heuristic expectation of the number of events beyond `n` is `Σ_(m>n) T_m < 1/(64n)`. Verified for
`n ≤ 3200` in this dossier (see PROBES). One event at any `n` refutes it. It is strictly stronger
than the seam-density statement `ρ(N) = o(N)` of SWT-03, which is itself OPEN and strictly weaker
than normality.

## Second-priority obligations (not the single strongest)

1. **Sufficient mesoscopic gate (IAD-06).** `limsup_B Re c^U_(jℓ_0(B))(B) ≤ 0` for every fixed
   `j ≥ 1`, `ℓ_0 = ⌈(2+δ)log_16 B⌉`. Sufficient for mode `h`; by IAD-08(b) it is beyond WALL-16
   with `v* ≤ 1`.
2. **Band extremal constant (O-7).** Turn the floating-point LP into an exact dual certificate and
   identify the constant (numerically `1/√5` at ratio `3/2`).
3. **Verify or replace the imports** flagged in SOURCE_MAP (Graham–Kolesnik statements not seen;
   the `(log B)^(3/2)` range quoted from memory in O-4).

## Next verdict-changing probe

Build and kernel-check the published Lean development claiming `μ(π) = 2` (it was scanned, not
built, by the literature helper). Outcome A: it checks — import it with its exact statement, set
the WALL-16 starting line to `1 + ε`, and attack the sharp borderline in the carry language.
Outcome B: it fails or cannot be reproduced — the starting line stays `6.1033` and the first
source-specific gain is the obligation.
