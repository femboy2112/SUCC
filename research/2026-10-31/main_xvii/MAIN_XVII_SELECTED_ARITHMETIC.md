# Operation Main XVII — the selected-arithmetic attack (directive §V)

**Research-status. The principal target was NOT reached; this is the honest ledger of the attempt.**
π base-16 normality, the signed Weyl gate `T_N(h)=Σ_{n≤N} e(hU_n(0))=o(N)`, and RH remain **OPEN**.
Everything below is a sub-result, an obstruction, a certified finite measurement, or a next-test
specification. No new source-selected signed cancellation theorem is claimed.

## 0. Representation and the two targets

`U_n = 16^{n−1}π − T_n`, `0 < T_n < (8n+1)^{-2}`, so `e(hU_n) = e(h·16^{n−1}π)·e(−hT_n)` and, since
`T_n → 0`, the gate `Σ e(hU_n(0)) = o(N)` **is** base-16 normality of π.

- **Primary target (dyadic block saving).** For fixed `h≠0`, find `η_h>0`, `A_h` with
  `|Σ_{n=A}^{2A−1} e(hU_n(0))| ≤ (1−η_h)A` for all `A ≥ A_h`. This is a fixed-fraction saving on the
  dyadic blocks of the π base-16 Weyl sum. **Not reached** (see §4).
- **Secondary target (finite-band certificate).** `F_{H,N} = Σ_{|h|<H}(1−|h|/H)|N^{-1}Σ_{n≤N}e(hU_n)|²
  = N^{o(1)}` at `H ≍ N^{1/3}`. The integrated `codex_finite_band_crt`/`cylinder` work supplies the
  classical bridges FB-01/FB-02/FB-04 and the conditional FB-03; the required **source-selected**
  finite-band energy estimate is **OPEN** and is not advanced here.

## 1. The established toolkit (integrated, re-read, calibrated)

- **Conductor growth (CG-1, PROVED LOCAL):** `log den(U_n) = 6n + o(n)` via PNT in arithmetic
  progressions. **NO-GO TR-03:** exact rational grids force per-block boundary cost `N − O(log N)`,
  excluding the exact-grid Stoneham transfer. Conductor growth is **seed-blind and phase-blind**
  ("large denominator is compatible with proximity to any real phase").
- **Prime-frame stencil (#424 ST3/ST4):** `A_n = Σ_p β_{p,n} log p`, `|U_n − A_n| ≤ 1/(120n³)`,
  `Σ|U−A| < 1/315`, `|Σe(hU) − Σe(hA)| < 2π|h|/315`. A faithful reduction, not a saving.
- **Per-window form SC-06:** for an eligible native prime `p` (`p≡1,5 mod 8`), first-birth window of
  length `L = ord_p(16)`, primary residue `a_j = c_p 16^j mod p`, cofiber `v_j` (so
  `U_{b_p+j} ≡ a_j/p + v_j mod 1`), define
  `E_p(h) = (L−1)^{-1} Σ_{j=0}^{L−2}[1 − cos(2πh(U_{b+j+1}−U_{b+j}))]`. The path inequality **SC-6b**
  gives `|S_p(h)|/L ≤ √(1 − ((L−1)/2L)E_p(h))`, so `E_p ≥ 1/4` forces `|S_p|/L ≤ √(7/8) < 1` — a
  window-sum saving. SC-06 (uniform `η_h>0`) is numerically robust but has no uniform proof.
- **The decisive countermodels:** the coherent seed `s*=−π/16`; the SC-05 same-forcing
  block-coherent seed; and **AT-07**, the published seven-pole null `z=w−2r` (`E_0=0`,
  `−1/(8n+1)<E_n<0`, coherent, nonnormal) that *nevertheless* has `v_p(E_{⌈Q/8⌉})=−a` for every odd
  prime power. Any valid saving must **exclude** these — so it must use the specific four-pole
  forcing, not generic "zero seed + deep conductors."

## 2. NEW sub-result (NET-XVII-1): a rigorous primary-only saving

Split the lag-one increment phase into primary + cofiber:
`h(U_{b+j+1}−U_{b+j}) ≡ h(a_{j+1}−a_j)/p + h(v_{j+1}−v_j) (mod 1)`, with
`a_{j+1}−a_j ≡ 15 c_p 16^j (mod p)`. Define the **primary-only** energy
`Ẽ_p(h) = (L−1)^{-1} Σ_{j=0}^{L−2}[1 − cos(2πh·(15c_p16^j mod p)/p)]`.

> **Proposition (primary-only saving).** For every `h` with `p ∤ 15c_p h`,
> ```
> Ẽ_p(h) ≥ 1 − (√p + 2)/(L − 1).
> ```
> Hence if `L > √p + 2`, `Ẽ_p(h) > 0`, and SC-6b applied to the **primary** phases gives a strict
> saving `|S̃_p(h)|/L ≤ √(1 − ((L−1)/2L)Ẽ_p(h)) < 1`.

**Proof.** `Σ_{j=0}^{L−1}[1 − cos(2πh·(15c_p16^j)/p)] = L − Re Σ_{g∈⟨16⟩} e_p(15c_p h·g)`, where
`⟨16⟩ ⊆ F_p^*` is the order-`L` subgroup. The classical subgroup/Gauss bound gives
`|Σ_{g∈⟨16⟩} e_p(αg)| ≤ √p` for `α≢0`: writing `m=(p−1)/L` and `1_{⟨16⟩}(x)=(1/m)Σ_{χ|_{⟨16⟩}=1}χ(x)`
(orthogonality over `F_p^*/⟨16⟩`), one gets `G_p(α)=(1/m)Σ_{χ|_{⟨16⟩}=1} g_χ(α)` where each nontrivial
`g_χ(α)` is a Gauss sum of modulus `√p` and the trivial character gives `−1`; the `1/m` average of `m`
terms then yields `|G_p(α)| ≤ (1+(m−1)√p)/m < √p`. Dropping the single `j=L−1` term (bounded by 2) and
dividing by `L−1`:
`Ẽ_p(h) ≥ (L − √p − 2)/(L−1) = 1 − (√p+2)/(L−1)`. ∎

This isolates the entire proof debt into the **cofiber cross-term** `E_p − Ẽ_p`: the primary
component of the window already saves, by a classical subgroup bound, exactly in the SC-06 order
regime `L > √p`.

**Scope / what it is NOT.** It bounds the *primary* energy only. It does **not** bound the full
window sum `|S_p(h)|` — the cofiber can *enlarge* it (SC-02: at the short-order `p=13`, `|S_13|≈1.99`
exceeds the primary `|P_13|≈0.835`). It is not a saving on dyadic time-blocks and says nothing about
`o(N)` or normality.

## 3. Certified numerics (calibrated instrument, independent second method)

A calibrated instrument (exact `U_n` via common-denominator integers; FFT subgroup sums; mpmath
50–80 digit cosines; a second `2sin²` route agreeing to `≤1e-50`) returned, with every calibration
passing (π/16 to >100 digits; Gauss modulus `√p`; `0 < 16^{n−1}π − U_n < (8n+1)^{-2}` to n≤1000;
window congruence `0` failures over ~270k entries):

| quantity | scope | result |
|---|---|---|
| subgroup bound `M(p)=max_{α≠0}|G_p(α)| ≤ √p` | 493 eligible primes ≤ 8000, all α | **0 violations**; worst `M/√p = 0.620` (p=2609) |
| `|G_p(α)|/√p` at `α=15c_p h` | all, h=1,3 | ≤ 0.599 (h=1), 0.611 (h=3) |
| **NET-XVII-1** `Ẽ_p(h) ≥ 1−(√p+2)/(L−1)` | 922 eligible-order cases, h=1,3 | **0 violations**; min margin **+0.0346** (p=7829); min `Ẽ`=0.578 |
| **SC-06** `E_p(h) ≥ 1/4` | **425 fresh windows** (700–8000, +orig), h∈{1,2,3,5} | **0 below 1/4**; min `E = 0.8366` |
| SC-05 coherent control energy | window A=80..120 | `≈ 1e-14` (uncoordinated: 1.12) |
| AT-07 seven-pole null energy | window 80..120 | `≈ 3e-9` (coherent; scales h²) |

This extends the dossier's 16-prime SC-06 certification to **425 windows × 4 harmonics** — a
certified improved finite bound, with the honest ceiling that it is finite (p ≤ 8000) and gives no
asymptotics in `p`.

## 4. The sharpened obstruction (a conjecture of mine, REFUTED by the data)

I conjectured the cofiber erosion `|E_p − Ẽ_p|` is controlled by the cofiber total variation
`V = Σ‖v_{j+1}−v_j‖`, so that `V = o(L)` would upgrade NET-XVII-1 to full SC-06. **The data refutes
the usefulness of this route**, and corrects my guess in both directions:

- `V/(L−1) ≈ 0.25` — the cofiber variation is `≈ L/4`, **not** `≈ L` as I had guessed. (My Main-XVI
  recollection that "V is large" was wrong at the scale that matters.)
- Yet the Lipschitz bound `|E−Ẽ| ≤ 2πh·V/(L−1) ≈ 1.4` (h=1) to `4.2` (h=3) is **vacuous** against the
  measured erosion `≤ 0.30`: it is 5–80× too loose. A total-variation bound is therefore the **wrong
  functional**, independently of whether `V` is small.
- The cofiber *second moment* is the tell: `Σ‖v_{j+1}−v_j‖²/(L−1) ≈ 0.083 ≈ 1/12` — exactly the
  variance of a uniform circle step. The cofiber increments behave empirically like **independent
  uniform-random circle steps**; the erosion is non-sign-definite (sometimes `E>Ẽ`, sometimes `E<Ẽ`),
  reaching ~0.3 per case but never conspiring to drive `E` below `1/4`.

**Consequence.** SC-06 reduces to a *non-conspiracy / equidistribution* statement for the cofiber
lag-one increments `v_{j+1}−v_j` (a second-moment bound, **not** a TV bound). That non-conspiracy is
precisely a miniature mixing statement — and AT-07/SC-05 prove coherent same-conductor-depth sources
exist, so it **cannot** follow from the primary residues, the zero seed, or the conductor depths
alone. This is the exact missing ingredient, now pinned to an `L²` cofiber estimate.

## 5. The precise missing hypothesis and the next falsification test

> **NET-XVII-2 (next target).** For eligible `p` with `L ≥ √p`, prove a source-derived lower bound
> on the *joint* lag-one energy that controls the cofiber second moment, e.g.
> `(L−1)^{-1} Σ_j ‖h(v_{j+1}−v_j) + {primary}‖² ≥ η_h`, equivalently an off-diagonal bound on
> `Σ_{i≠j} e_p(h(a_i−a_j)) · e(h(v_i−v_j))` beating the trivial `L²` only via the **joint**
> primary×cofiber character sum (SC-3's `Σ|ŵ_l|` route is vacuous; SC-4's frequency-averaged
> identity does not fix `h`). The instrument to build next: the exact joint `(a_j, v_j)` character
> sum at fixed low `h`, tested first on Stoneham `c=3/5` (where the source hot-spot bound exists) to
> calibrate, then on the authentic four-pole windows — predeclaring that `s*=−π/16`, SC-05, and
> AT-07 must fail it.

## 6. Firewall

NET-XVII-1 is a rigorous classical sub-result (subgroup Gauss bound) about the *primary* component of
a per-prime window; it is not a saving on the full sum, on dyadic blocks, or on `o(N)`. SC-06 remains
an OPEN uniform statement (numerically certified, not proved). The dyadic block saving (primary
target) and the finite-band certificate (secondary target) are **not reached**. No new signed
cancellation, π normality, or RH is claimed. Regression: `tests/test_main_xvii_primary_saving.py`.
