# π-frontier audit strengthening — four obligations sharpened

**2026-10-27 · audit branch `research/pi-proof-forge-integration-audit-2026-10-27` (child of PR #324 `fca58d3e`).**
Additive to the authoring round: this file does **not** edit any frozen source, any
`research/2026-10-27/*` dossier authored by the #324 chain, or any source-hashed receipt.
It records independent, calibrated strengthenings of four open/loose obligations flagged by
the hostile audit (handoff `CLAUDE_PI_PROOF_FORGE_INTEGRATION_RESULT_2026-10-27.md`).
**π base-16 normality and RH remain OPEN.** No Lean kernel authority is claimed for any
infinitary statement. Receipts: `tests/test_pi_frontier_strengthening_audit.py` (9/9 OK natively).

Source (frozen, re-expressed not mutated):
`r(x)=4/(8x−7)−2/(8x−4)−1/(8x−3)−1/(8x−2)=A(x)/D(x)`,
`A(x)=120x²−89x+16`, `D(x)=(2x−1)(4x−1)(8x−7)(8x−3)`, `U₀=0`, `Uₙ=16Uₙ₋₁+r(n)`.

---

## 1. The 2-adic isometry, in closed form (upgrades #321 BW-1: finite-verified → PROVED on all of ℤ₂)

The chain inherited `v₂(Φ(x)−Φ(y))=v₂(x−y)` from PR #321 as a **finite-verified** fact
(`n=0..199`). It is in truth a three-line parity theorem, and it proves *more* than was claimed.

**Theorem ISO-1 (PAPER-PROVED, all of ℤ₂).** `r : ℤ₂ → ℤ₂` is a 2-adic isometry:

$$v_2\!\big(r(a)-r(b)\big)=v_2(a-b)\qquad(a\neq b\in\mathbb Z_2),$$

and consequently `Φ(x)=Σ_{s≥0}16^s r(x−s)` is a 2-adic isometry, `v₂(Φ(x)−Φ(y))=v₂(x−y)`.

**Proof.**
1. **`D` is a 2-adic unit on all of ℤ₂.** Each factor is odd: `2x−1,4x−1,8x−7,8x−3 ≡ −1,−1,−7,−3 ≡ 1 (mod 2)` because `2x,4x,8x∈2ℤ₂`. The four rational poles `1/2,1/4,7/8,3/8` have denominators `2,4,8` (non-units), so none lies in ℤ₂; hence `r(x)=A(x)/D(x)∈ℤ₂` for every `x∈ℤ₂`.
2. Write `N(a,b):=A(a)D(b)−A(b)D(a)`. Then `r(a)−r(b)=N(a,b)/[D(a)D(b)]` with unit denominator, so `v₂(r(a)−r(b))=v₂(N(a,b))`.
3. **The quotient is odd.** `N(a,b)=0` at `a=b`, so `(a−b)∣N` in `ℤ[a,b]`; write `N=(a−b)·Q`, `Q∈ℤ[a,b]`. Reduce mod 2: `A(x)≡x` (since `120≡0`, `−89≡1`, `16≡0`) and `D(x)≡1` (product of four `≡1` factors). Hence `N≡a−b (mod 2)`, i.e. `(a−b)Q≡(a−b)` in the integral domain `𝔽₂[a,b]`; since `a−b≠0`, `Q≡1 (mod 2)`. Because `ℤ₂→𝔽₂` is a ring homomorphism, `Q(a,b) mod 2 = Q(a\bmod2,\,b\bmod2)`, so `Q(a,b)` is **odd for every** `a,b∈ℤ₂`. Thus `v₂(Q)=0` and `v₂(r(a)−r(b))=v₂(a−b)`.
4. **Lift to `Φ`.** `Φ(x)−Φ(y)=Σ_{s≥0}16^s[r(x−s)−r(y−s)]`. By step 3, `v₂(r(x−s)−r(y−s))=v₂((x−s)−(y−s))=v₂(x−y)=:v`. So the `s`-th term has valuation `4s+v`: the `s=0` term is exactly `v`, every `s≥1` term is `≥v+4>v`. The ultrametric gives a unique minimum, so `v₂(Φ(x)−Φ(y))=v`. ∎

**What this adds.** (i) `r` *itself* is the isometry — not merely the infinite-past `Φ`; the whole fact is the parity `Q≡1 (mod 2)`, which is `A≡x, D≡1`. (ii) The finite fallback "`Uₙ≡Σ_{s<k}16^s r(n−s) (mod 16^k)` is an isometry" is the truncation of step 4 and inherits the same proof. (iii) It stays a **2-adic** statement — no real-circle/Weyl content (SB-4 shows finite/2-adic rigidity cannot reach normality).

**Calibration (exact).** `A(x)≡x`, `D(x)≡1 (mod 2)`, `(a−b)∣N` exact, `Q(a,b) mod 2 = 1` on every residue class; `v₂(r(a)−r(b))=v₂(a−b)` on 3999 integer pairs and the `Φ`-truncation on 2997 pairs, 0 mismatches; off-by-one valuation control true nowhere.

---

## 2. #319's Diophantine input: certified by EITHER published μ(π) bound; only the effective constant is conditional

The `#317/#319` block bound `|S_N(h)|≤N−(log₈N)/14+O_h(1)` uses, at step **GB-11** of
`GLOBAL_BRANCH_COERCIVITY.md`, a lower bound `|π−p/q|≥C·q^{−s}`. The precise picture — correcting
a first-pass over-read of mine (an adversary pass refuted it; receipt below):

- **The real barrier is the collision exponent `8`, not `15/2`.** GB-10 manufactures `|π−p/q|≤4·16^{−8m}` with denominator `q=15|h|·16^m`. GB-12's own band caps `|h|≤m²/64` (polynomial in `m≈log₁₆q`), so `16^{−8m}=(15|h|)^8\,q^{−8}` with `(15|h|)^8=q^{o(1)}`: the manufactured approximation has effective quality `q^{−8+o(1)}`. A contradiction with `|π−p/q|≥C q^{−s}` needs `16^{(8−s)m}` (exponential in `m` when `s<8`) to beat `(4/C)(15|h|)^s` (polynomial in `m`), which holds past some onset `m₂(s)` **iff `s<8`**. The dossier's `15/2` is only a convenient value strictly between `7.1032` and `8` (`8−15/2=1/2` squares the `16^{m/2}` into GB-11's tidy `16^m`); it is **not** the threshold.
- **So the type is certified by EITHER published bound.** Both Salikhov 2008 (`μ(π)≤7.6063`) and Zeilberger–Zudilin 2020 (`μ(π)≤7.103205334137`, arXiv:1912.06345v2; *Moscow J. Comb. Number Theory* **9** (2020) 407–419) satisfy `μ(π)<8`, so **either** licenses the `−(log₈N)/14` order. ZZ-2020 is **not** logically required; it only **lowers the onset** `m₂` (illustration at `C=1`: `m₂=44` for Salikhov, `9` for ZZ, and **no onset** at `s=8`). *[This corrects my earlier "requires the 2020 improvement / Salikhov insufficient" claim — refuted by the structure theorem above; the convenient `15/2` is not load-bearing.]*
- **What is genuinely unextracted:** the **effective constant `C`** in `|π−p/q|≥C q^{−s}` (equivalently the onset `m₂`). `C` exists — irrationality absorbs the finitely many exceptional reduced denominators — and the dossier labels it CONDITIONAL rather than computing it. It is a definite positive number once an effective `q₀(ε)` is substituted: `C = min( C_tail(ε,q₀),  min_{1≤q<q₀} min_p |π−p/q|·q^{s} )`.

**Reclassification of obligation #2.** From *"rests on an uncertified Diophantine constant"*
to: **the `−(log₈N)/14` order is licensed by a published irrationality theorem — either
Salikhov-2008 or ZZ-2020 clears the real barrier `μ(π)<8` — so only the additive `O_h(1)`
onset constant `C(h)` is unextracted: conditional, not open.**

**Calibration (log-space, exact mechanism).** onset exists ⇔ `s<8` (`m₂=44` at Salikhov 7.6063, `9` at ZZ 7.1032, `30` at the dossier 7.5, **None** at `s=8.0` and `s=8.01`); `7.1032<7.5<7.6063<8`.

---

## 3. SB-1 geodesic Lipschitz constant: `2π|h|` per slot, `4π|h|` for a shared coordinate (closes #4)

SB-1 reads `|Σ wₙ[f(Xₙ)−f(Yₙ)]| ≤ B·Σⱼ L_{j,N}`, `L_{j,N}` the coordinatewise geodesic
Lipschitz constant. For the circle character `e(h·)=exp(2πih·)` on the geodesic metric
`d(x,y)=min(|x−y|,1−|x−y|)`,

$$\sup_{x\neq y}\frac{|e(hx)-e(hy)|}{d(x,y)}=2\pi|h|\quad(\text{attained in the limit}),$$

so a **single-slot** observable has `L=2π|h|` — exactly the character corollary, and exactly what
the repo test uses (distinct frequencies on distinct coordinates): **no numeric break**.
The understated case is a **shared coordinate**: when the same circle coordinate is fed to two
slots, the observable is `g(x)=e(hx)·e(hx)=e(2hx)` with geodesic Lipschitz constant
`2π·(2|h|)=4π|h|` — twice the per-slot value, because the shared displacement moves `f` through
both appearances. For a coordinate appearing in `d` slots with per-slot frequencies `h₁,…,h_d`,
the SB-1 **budget** (triangle inequality) is `2π·Σᵢ|hᵢ|`, and the **sharp** coordinatewise
geodesic Lipschitz constant is `2π·|Σᵢ hᵢ|` (the frequencies add *algebraically*): these agree
only when the `hᵢ` share a sign. For two equal-frequency slots (`+h,+h`) both give `4π|h|` — the
value a `2π|h|` prose understates; for a cancelling pair (`+h,−h`) the observable is `e(hx)e(−hx)=1`,
true constant `0`, while the budget still reads `4π|h|`. So `2π·Σ|hᵢ|` is the correct **upper
bound** SB-1 needs (no numeric break), but "`4π|h|`" is sharp specifically for the shared-sign
case the flag was about.

**Calibration (exact numeric sup).** single-slot sup/`|d|` `= 2π|h|`; same-sign two-slot sup `= 4π|h|` (`h∈{1,2,3,5}`); cancelling pair `+h,−h` → constant observable, sup `= 0 < 4π|h|` (budget not sharp under sign cancellation).

---

## 4. The gate *is* base-16 Weyl of π — a bird's-eye reduction (firewall, NOT progress)

From the master identity `Uₙ=16^{n−1}π−Tₙ`: `e(hUₙ)=e(h·16^{n−1}π)·e(−hTₙ)` and
`|e(−hTₙ)−1|≤2π|h|Tₙ`. With `W_N(h):=Σ_{n≤N}e(h·16^{n−1}π)`,

$$\boxed{\;|S_N(h)-W_N(h)|\le 2\pi|h|\sum_{n=1}^{N}T_n\le 2\pi|h|B<\tfrac{2\pi|h|}{15}\quad(\forall N).\;}$$

(The echo-transport theorem with the identity filter.) Hence, **for each fixed `h`**,
`S_N(h)/N→0 ⇔ W_N(h)/N→0`: the per-mode gate is exactly the `h`-th Weyl sum of the orbit
`{16ⁿ·hπ} mod 1`. Quantifying over **all** `h∈ℤ∖{0}` (the Weyl criterion), the full gate
`∀h≠0: S_N(h)=o(N)` is therefore equivalent to equidistribution of `{16ⁿπ} mod 1` — the textbook
base-16 normality of π. (A single fixed `h` is necessary, not sufficient, for normality.)

**Consequence (firewall, not a step toward it).** The BBP carrier is **normality-neutral** at the
fixed-`h` Weyl level: the recursion contributes only a bounded `O_h(1)` correction, so no shortcut
to normality can come from the linear recursion/tail structure alone (consistent with the
echo-transport LTI no-go and SB-4). This bounds effort honestly — a fixed-`h` elementary argument
cannot yield `o(N)` without proving π normal.

**Sharpened smallest obligation (now using ISO-1).** By ISO-1 + CRT-1, the bin
`{n≤N : [Uₙ]_{16^k}=a}` is **exactly the arithmetic progression** `{n≡Φ_k^{−1}(a) (mod 16^k)}`.
So the SB-3 energy `E_{N,M}(h)=(M/N²)Σ_t|Σ_{n≡t (M)}e(hUₙ)|²` is literally the **L²-energy of
`e(hUₙ)` across arithmetic progressions mod `M=16^k3^L`**. The open obligation is precisely:

> prove this AP-energy `→0` along some admissible `M=M(N)=16^k3^L=o(N)`,

with the decay forced by genuine cancellation between `e(hUₙ)` along the coprime-modulus APs.
Fixed `M` gives `E=Θ(1)` (`z≡1⇒E=1`); any finite-frequency band is defeated (SB-4); so `M` must
grow while staying `o(N)` — the content no finite or 2-adic identity supplies.

**Calibration (mpmath on true π, instrument recovers π to `<10⁻³⁰`).** `max_N|S_N(h)−W_N(h)|≤2π|h|B` for all `N≤1200`, `h∈{±1,2,3,5}`; the gap is a real fraction (`≈0.72` for `h=1`) of the bound.

---

## Verdict

| # | Obligation (before) | After this audit | Status |
|---|---|---|---|
| 3 | 2-adic isometry finite-verified (`n=0..199`) | closed-form proof on all ℤ₂ via `Q≡1 (mod 2)`; proves `r` itself | **PAPER-PROVED (ℤ₂)** |
| 2 | "uncertified Diophantine constant" | real barrier is `μ(π)<8` (collision exponent); EITHER Salikhov-2008 or ZZ-2020 clears it (`15/2` is a convenient intermediate, not load-bearing); only effective `C`/onset unextracted | **CONDITIONAL (not open); order licensed** |
| 4 | SB-1 prose Lipschitz `2π` | sharp: `2π|h|` per slot, `4π|h|` shared (budget `2π Σ|hᵢ|`) | **CLOSED (cosmetic, no numeric break)** |
| 1 | gate `S_N(h)=o(N)` | `⇔ W_N(h)=o(N)` = base-16 Weyl of π; carrier normality-neutral; obligation = AP-energy decay | **OPEN (famous); sharpened** |

π base-16 normality and RH: **OPEN.** Firewall: **INTACT** (no frozen source / dossier / receipt touched; additive file only).

**Reproduction.** `PYTHONPATH=/home/leah/SUCC python -m unittest tests.test_pi_frontier_strengthening_audit -v`
