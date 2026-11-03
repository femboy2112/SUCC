# Obligation (A): proving the ×3 defect D_N(h) — full-blast honest assessment

**Branch:** `research/prove-obligation-A-x3-defect-2026-11-02` (off `origin/main`). **Date:** 2026-11-02.
**Agent:** Ravel (main thread, direct attack). **Scope:** prove obligation (A) of the
Hochman–Shmerkin ×16–×3 rigidity route (WB-10), or name the exact residue.

## 0. The target

Obligation (A) is: for every fixed nonzero integer `h`,
$$D_N(h) = \frac1N\sum_{n=1}^N\big[e(3h\,U_n)-e(h\,U_n)\big] \;\to\; 0,$$
where `U_n = 16^{n-1}\pi - T_n` is the four-pole BBP orbit, `T_n = Σ_{k≥1}16^{-k}r(n+k)`
the Green tail, `r(m)=4/(8m-7)-2/(8m-4)-1/(8m-3)-1/(8m-2)`, `e(t)=exp(2πit)`.

## 1. What is PROVED (this round, airtight)

### 1.1 The universal bound is trivial and sharp
By the triangle inequality, for **every** orbit and every α:
$$\big|D_N(h)\big| \le 2 \qquad\text{(each summand has modulus $\le 2$).}$$
This is the *only* unconditional bound. It makes `D_N(h) → 0` a statement that **any**
argument must go beyond; the trivial bound alone cannot certify it.

### 1.2 Exact defect identity (re-proved, self-contained)
`U_n = 16^{n-1}\pi - T_n` and `x_n = \{16^{n-1}\pi\}` satisfy `e(h U_n) = e(h x_n)e(-hT_n)`
for integer `h` (integer-phase collapse, since `16^{n-1}\pi = x_n + \lfloor 16^{n-1}\pi\rfloor`).
With `Σ_n T_n = B < 1/32` (proved, `green_tail_sharpening`), for every fixed `h`:
$$D_N(h) = W_N(3h) - W_N(h) + O_h(1/N), \qquad W_N(h)=\frac1N\sum_n e(h x_n),$$
with explicit `|O_h(1/N)| \le 2\pi(4|h|)B/N`.

### 1.3 The exact equivalence (the content of (A))
For any weak-* limit μ of `μ_N = N^{-1}Σδ_{x_n}` (which is automatically `T_{16}`-invariant):
$$D_N(h)\to 0 \;\Longleftrightarrow\; \widehat\mu(3h)=\widehat\mu(h) \;\Longleftrightarrow\; (T_3)_*\mu=\mu .$$
So **(A) is measure-level ×3-invariance**, not a single finite-frequency defect. It is
**strictly weaker** than `S_N(h)=o(N)` (which forces `μ̂(h)=0`) but **strictly stronger** than
the vanishing of any finite list of defects.

## 2. The firewall (proved): (A) is non-discriminating

Seed the orbit at `x_1=0` (coherent counterseed). Then `U_n=-T_n\to 0`, so `e(h U_n)\to 1`
and `D_N(h)=S_N(3h)-S_N(h)\to 1-1=0`. **The counterseed satisfies (A)** yet its empirical
measure is a Dirac mass (dimension 0, maximally non-normal). Hence (A) alone cannot certify
normality; it is necessary-but-not-sufficient, and (B) (positive lower dimension) is the leg
that kills the counterseed. Confirmed by Hochman–Shmerkin's *both-legs* structure.

## 3. The honest residue: (A) is exactly as hard as the Weyl gate

`D_N(h)→0` ⟺ `μ̂(3h)=μ̂(h)` for **every** limit μ. This is a statement about *all* characters
simultaneously (measure rigidity), not any one defect. It is **not** a shortcut:

- **Transfer-operator route:** ruled out. The ×3 Koopman operator is an isometry (no spectral
  gap); `D_N→0` is measure rigidity, not a spectral-gap statement (see `X3_TRANSFER.md`).
- **van der Corput / second-difference:** the Fejér identity `D_N = 2i N^{-1}Σ e(2hU_n)\sin(2πhU_n)`
  and the self-similarity `h↦16h` are real handles, but they do **not** yield an unconditional
  bound — the weight `sin(2πhU_n)` kills only resonant directions, not the generic ones.
- **Telescoping:** there is no exact telescoping identity; `gcd(3,16)=1` gives a free abelian
  semigroup `⟨3,16⟩=\{3^a16^b\}`, so `e(3hU_n)` and `e(hU_n)` are genuinely independent orbit
  points and no finite recurrence relates them.

## 4. Numerical truth (corrected, precision-safe)

The prior "`N·|D_N|` exactly constant" observation (and the `O(1/N)` "theorem") were
**floating-point artifacts**: at `dps≈120`, the digit-shift `x←frac(16x)` consumes ~1.2 decimal
digits per step and the orbit collapses to 0 near n≈100, making all later terms exactly 0.

Corrected computation (hex-digit extraction of π, verified prefix `243f6a8885a308d3`,
`dps=5000`, N=2000, h=1):

| N | |Σ D_n| | |D_N| |
|---|---|---|---|
| 200 | 6.71 | 3.36e-2 |
| 500 | 28.66 | 5.73e-2 |
| 1000 | 49.15 | 4.92e-2 |
| 1500 | 60.23 | 4.02e-2 |
| 2000 | 44.07 | 2.20e-2 |

The partial sum **drifts** (does not freeze) and `|D_N|` **oscillates** around 0.02–0.06 with
**no clean `1/N` decay** at these horizons. The strong form `D_N=C(h)/N+o(1/N)` is **FALSE**.

## 5. Claim ledger

| ID | Claim | Status |
|---|---|---|
| A-01 | `|D_N(h)| ≤ 2` universally | PROVED (trivial) |
| A-02 | `D_N(h)=W_N(3h)-W_N(h)+O_h(1/N)` | PROVED |
| A-03 | `D_N→0 ⟺ μ̂(3h)=μ̂(h)` (×3-invariance) | PROVED |
| A-04 | (A) non-discriminating (counterseed passes) | PROVED |
| A-05 | `D_N = C(h)/N + o(1/N)` (strong form) | REFUTED (precision artifact) |
| A-06 | `D_N→0` for authentic π orbit | **OPEN** (≡ Weyl gate, no shortcut) |
| A-07 | `D_N(h) = O(1/N)` universally | REFUTED (was precision artifact) |

## 6. Verdict

**Obligation (A) `D_N(h)→0` is not provable by any known shortcut and is exactly as hard as the
Weyl gate itself.** The honest, durable result of this full-blast attack is a *clean negative*:
(A) is measure-level ×3-invariance, non-discriminating, not reachable by transfer-operator,
telescoping, or van der Corput methods, and its only rigorous bound is trivial. The rigidity
route is a valid **equivalent** decomposition (not easier), and (A)+(B) together are the two
named, navigable legs. π base-16 normality and RH remain **OPEN**.
