# Countermodels and hostile controls — RENORM transport

Every control is an exact-arithmetic computation (Fractions mod 1; `mpmath` only at the final
`e(·)`). Two independently implemented oracles (rational mod-1 and odd-conductor integer modular)
agree to the rounding floor. **A finite-`A` numerical trend is not an asymptotic proof**; every
row that is an *observation* says so. π base-16 normality and the signed Weyl gate stay **OPEN**.

## What each control must do

A proposed source-selected bound must (i) hold for the genuine source, and (ii) **fail** for at
least one nonnormal/foreign control — otherwise it is source-blind. The table records what each
control does to the two quantities in play: the **RENORM-1 identity/bound** (RT-1/RT-2) and the
**high-band second moment** `M(A,H)=Σ_{1≤|h|≤H}|c_A(h)|²`.

| Control | Construction | RENORM-1 identity | High-band moment `M/K` | Discriminates? |
|---|---|---|---|---|
| **Genuine** | `U_0=0, U_n=16U_{n-1}+r(n)` | holds (`ε` = r-forcing) | small, drifts down with `A` (e.g. `M(256,64)/64≈0.0046`) | — (reference) |
| **x=1/5 fixed point** | `x_n≡1/5` (`frac(16/5)=1/5`) | bare relation holds with `ε=0`; **r-forcing `ε` formula is nonzero** (0.00018–0.0092), flagging it is not an r-orbit | **`|c_A(h)|=1 ∀h`, `M/K=1.0` exactly, no decay** | **YES** — exact counterexample to any universal high-band smallness bound |
| **Changed seed `U_0=1/7`** | same `r(n)`, nonzero seed | holds to `~1e-62` (seed-independent; adds period-3 rotation `16ⁿ/7`) | stays BBP-small (`M/K≈0.004–0.013`) | **NO** on the moment; perturbs individual `|c_A(h)|` (ratios 0.5–3.0). *Rotation, not a nonnormal orbit.* |
| **Scaled mutant `s·r(n)`** `s=3,5` | linearity ⇒ `U'_n=s·U_n` exactly | holds, `c'_A(h)=c_A(sh)`, gap `0.0`, worst ratio `0.730` | equidistributing (passes the same tests at rescaled freq) | **NO** — confirms RT-2 is general, not a fingerprint |
| **#487-style counterfeit** `x_n=1/5+r(n)` | clusters: `r(n)<6e-5` for `n≥64` | n/a | **`|c_A(h)|≈1 ∀h`; near-pair count `=C(A,2)` (every pair)**; `M` ratio cf/gen grows `61.7→128.9` with `A` | **YES but one-sided** — rejects clustering counterfeits; does not uniquely fingerprint the source |

### Key exact numbers

- **x=1/5:** `c_A(h)=e(h/5)`, `|c_A(h)-e(h/5)|≤3.4e-60`; `M(A,H)=H` exactly for all tested `(A,H)`.
- **Two-oracle agreement (C3):** rational-mod-1 vs odd-conductor-integer give byte-identical phases;
  `c_A(h)` agree to `1.7e-49` (dps=50) / `1.9e-79` (dps=80) for `h∈{1,3,7,16,50,100,200}`. The
  conductor `M=lcm(denoms)` is **odd** at every `A` (the four BBP terms' 2-adic parts cancel).
- **Precision audit (C3):** RENORM-1 worst `0.980873` (at `A=200,h=1`) and corrected accumulated
  worst `0.923240` (at `A=128,h=3,j=1`) reproduce exactly and are **stable dps50↔dps80** — no float
  artifact; both bounds hold with 0 violations.
- **Near-pair (AT1):** genuine off-diagonal count `= 2A(A-1)/q` to within ~4% (equidistribution
  level); `x=1/5` pinned at `A(A-1)` (every pair). `gen/[1/5]=2/q` exactly.

## Attack obstructions (Phase 2 — Outcome B, no false proof)

- **AT1 near-pair route `P_A(q_A)=o(A²K_A/q_A)` — OBSTRUCTION.** (i) `K_A=⌊log₁₆ log A⌋=0` for every
  `A<e¹⁶≈8.9e6`, so `q_A=1/2` and the literal criterion is vacuous on all affordable `A`. (ii) At
  meaningful `q`, `q·P_A(q)/A² → ~2` (genuine ≈ equidistribution), never `o(K_A)`. **The near-pair
  reformulation reduces to — and loses a `K_A` factor against — the open Weyl bound `Σ_{A≤n<2A}e(hU_n)=o(A)`
  it was meant to bypass.** First failing step: the energy step, where genuine `P_A(q)≈2A²/q` gives no
  sub-equidistribution saving. *Not a shortcut.*
- **AT2 branch-current contraction — OBSTRUCTION.** The exact identity
  `E_{K+1}-E_K=16^{K+1}Σ_{w,j}(μ_A(wj)-μ_A(w)/16)²` holds, but a source-selected decay of the
  child-current deviation requires the `(K+1)`-th hex digit to be equidistributed **conditional** on
  the first `K` — finite-window normality of π's hex expansion, which is OPEN. The recurrence gives
  only the deterministic `×16` shift plus `r(n)=O(1/n²)` (leading `1/n` coefficient
  `4/8−2/8−1/8−1/8=0` exactly): **no mixing, no random carries, no spectral gap** — the forbidden
  assumptions. The `×16` shift is the *same* one `1/5` obeys. First failing step: assuming
  digit-independence. *Not a shortcut.*

## Methodological corpse (do not re-walk)

- **Changed-seed is not a nonnormal contrast.** For rational `s`, `frac(16ⁿ s)` is a measure-preserving
  rotation (`16≡1 mod 3,5`), so `U_0=1/7` only rotates the orbit; it cannot test normality. The *only*
  genuine nonnormal contrast among these is the degenerate `x=1/5` fixed orbit.
- **RENORM-1 "holds" is not source evidence.** It holds for every `U_n=16U_{n-1}+f(n)` with small `f`
  (and for the changed seed, to `1e-62`). Passing it certifies the *recurrence form*, not the seed or
  the four-pole source.

**Net:** no control tested here isolates the genuine BBP orbit from an arbitrary *other* equidistributing
orbit; the clustering counterfeits and `1/5` are rejected, but the separation that matters —
genuine-source high-frequency cancellation — is exactly the OPEN gate. No status is promoted.
