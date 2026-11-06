# Selected zero-boundary signed-lag attack — results and obstructions

**2026-11-01, research-only (post-Main-XIX).** Frozen: `U_0=0` literal, four signed poles
`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`. No Lean theorem; no external review. **No π
normality, no RH, no signed-saving claim.** The honest outcome of this round is one refuted
intermediate lemma, one representation-identity classification, and one resolution-ceiling
obstruction — it narrows the search without advancing the gate.

Notation as in Main XIX LCS: `U_n(s)` the orbit with real seed `s`; `T_n=∑_{m≥1}16^{−m}r(n+m)`
the Green tail; `U_n(0)=16^{n−1}π−T_n`; `U_n(s_*)=−T_n` for `s_*=−π/16`. Signed lag
`D^[d]_{h,k}(N;s)=∑_{n≤N−k}e(h[(16^k−1)U_n(s)+F^[d]_{n,k}])`,
`L^[d]_{N,K}=(2/KN)∑_{k<K}(1−k/K)Re D^[d]_{h,k}`, `e(t)=exp(2πit)`.

## SZB-01 — The exact zero-seed reduction (the thing to attack)

Because `U_n(0)=U_n(s_*)+16^{n−1}π`, the zero-seed corrected lag phase splits exactly:

    (16^k−1)U_n(0)+F^[d]_{n,k} = [(16^k−1)U_n(s_*)+F^[d]_{n,k}] + 16^{n−1}(16^k−1)π
                               = [(T_n−T_{n+k}) − R_d(n,k)] + (x_{n+k}−x_n),

where `x_m={16^{m−1}π}` are the base-16 digits of π read from position `m−1`, and
`16^{n−1}(16^k−1)π ≡ x_{n+k}−x_n (mod 1)`. **Status: exact identity (PROVED LOCAL).** Hence at the
compensated clock `K_N=⌊(d+1)log_16 N⌋` the zero-seed score is the counterseed's corrected score
(whose transport defect `→0` at `c=d+1`, Main XIX LCS/§CRE-08) plus the **Fejér-weighted lag
autocorrelation of π's hex digits**. Proving `limsup_N L^[d]_{N,K_N}(h;0)≤0` for every fixed `h≠0`
would prove base-16 normality of π — so it is the gate, and a route must add genuinely new content,
not restate it.

## SZB-02 — REFUTED intermediate lemma: no one-sided (positivity) shortcut

**Proposed lemma (tested):** "at the compensated clock, the corrected zero-seed score is
sign-definite: `L^[d]_{N,K_N}(h;0)≥0`, and each per-lag corrected correlation
`Re D^[d]_{h,k}/(N−k)≥0`." A positivity like this would reduce the gate to a one-sided estimate.

**Refuted (numerical certificate, `probe.py`/`COMBINED_LOG.txt`).** For `d∈{2,3}`, `h∈{1,3,5,7}`,
`N∈{16384,65536}`: the minimum per-lag corrected correlation is **negative in every one of the 16
configurations** (e.g. `d=2,h=1,N=16384,k=4`: `−0.0106`; `d=3,h=5,N=16384,k=5`: `−0.0099`), and the
aggregate `L^[d]` itself takes both signs across the grid (e.g. `−0.00079` vs `+0.00032`). There is
no free positivity to exploit; the Fejér/Cesàro nonnegativity of the two-sided kernel does **not**
survive the one-sided-plus-diagonal observable used here. **Status: REFUTED (scoped to the tested
grid; a sign-oscillating quantity has no one-sided bound of this form).**

## SZB-03 — Front B: the angular-period identity is SEED-BLIND (representation identity)

The Main XIX AC-13 decomposition `P(t)/(16−t^8) = 1/(4(1+(t−1)²)) + G'(t)`, `G` vanishing at `{0,1}`,
gives the **source** period `∫_0^1 P/(16−t^8)dt = π/16` (reproduced to 40 digits). This identity
involves only the source `r`; it does **not** involve the seed. Two orbits with the **same source**
(hence the same AC-13 identity) but different seeds realize completely different digit
distributions:

- zero seed: `U_n(0)=16^{n−1}π−T_n` (digits of π; normality OPEN);
- completed point `q=1/5` (`s=1/5−π/16`, same four-pole forcing): `16^n≡1 (mod 5)` ⇒ `{U_n}→1/5`,
  so `|S_N(h)|/N → 1` — **nonnormal** (verified `=1.0000` at `N=4000`, `h=1,2,3`).

Because the angular-period identity holds **identically** for both, it cannot distinguish a normal
from a nonnormal orbit of the same source. **Classification: representation identity, not a
normality mechanism** (the commutator of "angular reparametrization" and "clock shift" carries no
seed information — both are determined by the source `r` and the linear recurrence, which fix only
`π/16`). This is the honest verdict the Main XIX handoff's Front B anticipated; it is corroborated
by the existing countermodels (the Beta eight-moment mutant FP-04B and the cross-ratio refutation
AC-14: same period-level data, different normality). **Status: NEGATIVE / representation identity.**

## SZB-04 — Front C: within-cell signed phase is the gate at a shifted harmonic

At cell resolution `k` (`M=16^k`), the within-cell phase of the zero seed is governed by
`{16^k U_n(0)}`; the corresponding signed statistic at harmonic `h` is
`S_N(h·16^k) = ∑_n e(h·16^k·U_n(0)) = ∑_n e(h·{16^{n+k−1}π}·…)`, i.e. the Weyl sum at harmonic
`h·16^k`. By digit-shift invariance `S_N(h·16^k)` has the **same** magnitude as `S_N(h)` on a
shifted window (verified: `|S_N(h·16^k)|/N` is `0.0073` for `h=1` and `0.0018` for `h=3`,
**independent of `k=1,2,3`**). So "within-cell control at resolution `k`" is literally `S_N(h·16^k)=o(N)`
— the gate at a higher harmonic. The Main XIX resolution ceiling `D_{N,k}≥max(0,log(M/N))` forces an
affordable resolution to satisfy `M≤N`, i.e. `k≤log_16 N`; beyond it the entropy deficit is
mandatory. **No seed-specific signed leverage emerges below the ceiling. Status: OBSTRUCTION.**

## SZB-05 — The remaining discriminator (what every available tool lacks)

Three independent tool-routes are now each shown insufficient *for a structural reason*:
- **seed-uniform transport** — a positive defect `(1−(d+1)/c)²` on the counterseed (Main XIX LCS);
- **angular period** — seed-blind (SZB-03), fixes only `π/16`;
- **entropy / within-cell** — equals the gate at a shifted harmonic, ceiling-blocked (SZB-04);

and the one-sided positivity shortcut is refuted (SZB-02). Each route is either *seed-blind* or
*gate-equivalent*. The only route not excluded is a **genuinely seed-specific signed estimate** that
uses the exact literal boundary `U_0=0` and the resulting diagonal rationality of the orbit — i.e.
an argument that is sensitive to *which* completed point the orbit has (π's digits vs. `1/5` vs. the
counterseed), not merely to the source or the period. No tool in the current stack supplies that
sensitivity. **Status of π base-16 normality and the gate `∀h≠0: S_N(h)=o(N)`: OPEN.**

## Hostile controls exercised

Same four-pole forcing with completed point `q=1/5` (nonnormal, `|S_N|/N→1`); the counterseed
`s_*=−π/16` (completed point 0); and (inherited) the dyadic near-zero and prime-smooth `q=3^a5^b`
families and the order-2 de Bruijn sequence. Each defeats a seed-blind or one-resolution route,
consistent with SZB-02..04. Finite experiments here do not prove any all-horizon limit.
