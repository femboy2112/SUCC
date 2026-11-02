# X3 spacing bound for the rational BBP orbit {U_n}

**Branch:** `research/x3-rigidity-frontier-2026-11-02`. **Date:** 2026-11-02.
**Scope:** obligation (B) sub-target 1 of `X3_RIGIDITY.md` — a spacing lower bound for the
rational orbit `{U_n}`, the most concrete provable sub-result toward positive dimension.
**Reproducible script:** `spacing_verify.py` (same directory).

> **Status at the top, brutally honest:** the *only* spacing bound that is actually provable
> from the explicit rational structure is `min_{n<m≤N} ‖U_n − U_m‖ ≥ 1/Q` with
> `log Q ≤ 8 N (1+o(1))` — i.e. `≥ exp(−8N(1+o(1)))`. This is **trivial and vacuous**: it is an
> *exponential* lower bound, strictly weaker than polynomial, and it does **not** imply positive
> Hausdorff dimension. Every attempt to upgrade it to polynomial (or even to `exp(−o(N))`)
> reduces, provably, to a **signed-Weil cancellation estimate** of exactly the kind that is
> OPEN in this program. The spacing route is *not* a free lunch; it is the same gate in a
> different costume. No unproven bound is asserted. Details and the exact reduction below.

---

## 1. Setup and the exact identity (PROVED, standard BBP)

Define

$$ r(j)=\frac{4}{8j-7}-\frac{2}{8j-4}-\frac{1}{8j-3}-\frac{1}{8j-2}, \qquad U_n=\sum_{j\le n}16^{n-j}r(j),\quad U_0=0. $$

This `r` is the standard **BBP (Bailey–Borwein–Plouffe)** forcing with the index shifted
`k=j-1`: the classical identity is

$$ \pi=\sum_{j\ge 1} 16^{1-j}\, r(j). \tag{BBP} $$

Multiplying by `16^{n-1}`:

$$ 16^{n-1}\pi=\sum_{j\ge1}16^{n-j}r(j)=U_n+T_n,\qquad T_n=\sum_{j>n}16^{n-j}r(j). \tag{1} $$

Since `r(j) ~ 3/(2j)` and `16^{n-j}` decays, `T_n → 0`; in fact `T_n = O(1/(15·16)·3/n)`-order,
`T_n = O(1/n)`, and `Σ_n T_n` is absolutely convergent (the dossier's `B < 1/32`). Hence

$$ U_n = 16^{n-1}\pi - T_n, \qquad \|U_n - \{16^{n-1}\pi\}\| = O(1/n)\to 0. \tag{2} $$

**Status:** (1), (2) are PROVED (classical BBP + elementary tail estimate). Verified numerically
in `spacing_verify.py` (`T_n · n → small constant`).

---

## 2. The conductor: `den(U_n)` grows exponentially (PROVED)

Each `r(j)` is a rational with denominator dividing `lcm(8j-7, 8j-4, 8j-3, 8j-2)`, four odd
integers near `8j`. Therefore (multiplying out the `16^{n-j}` weights, which are powers of 2
and hence coprime to all odd denominators):

$$ \operatorname{den}(U_n)\ \big|\ \operatorname{lcm}\big\{8j-7,\ 8j-4,\ 8j-3,\ 8j-2\ :\ 1\le j\le n\big\} . \tag{3} $$

The RHS is the lcm of `4n` odd integers `≤ 8n`. By the prime-number theorem,
`log lcm(1,\dots,M) = M(1+o(1))` (Chebyshev's `ψ(M) ~ M`), so

$$ \log \operatorname{den}(U_n) \le \psi(8n)(1+o(1)) = 8n\,(1+o(1)). \tag{4} $$

**Empirically** `log₂(den U_n) ≈ 8.6n` (the `4n` odd factors up to `8n` have lcm with log₂ ≈ 8n
up to the usual constants; the reduced denominator is within a factor `n^{O(1)}` of it). The
prompt's `log den = 6n+o(n)` (and the prior `X3_SPACING_CORE.md`'s citation of CG-01) is a
**natural-log** statement: `ln den(U_n) ≈ 5.96n ≈ 6n`, matching `log₂(den) ≈ 8.6n` via
`ln = log₂ · ln 2`. The base conventions differ (`ln` vs `log₂` vs `log₁₆`); the *only* feature
that matters is:

> **The conductor/denominator of `U_n` grows exponentially in `n`, with rate `Θ(n)`.**

**Status:** (3) PROVED (divisibility, exact). (4) PROVED (Chebyshev `ψ(M)~M`). No numerics needed.

---

## 3. The spacing bound — what is *actually* provable (PROVED, and vacuous)

For `1 ≤ n < m ≤ N`, write the difference exactly:

$$ U_m - U_n = \frac{A_{nm}}{Q_{nm}}, \qquad Q_{nm}>0,\ \gcd(A_{nm},Q_{nm})=1, \quad A_{nm}\in\mathbb Z. $$

By (3), `Q_{nm} | lcm{…, j≤m}` and so `log Q_{nm} ≤ 8m(1+o(1)) ≤ 8N(1+o(1))`.

On the circle, `‖x‖ = dist(x, Z)`, we have for `A ≠ 0`:

$$ \|U_m-U_n\| = \left\|\frac{A_{nm}}{Q_{nm}}\right\| = \frac{\min(|A_{nm}\bmod Q_{nm}|,\ Q_{nm}-|A_{nm}\bmod Q_{nm}|)}{Q_{nm}} \ge \frac{1}{Q_{nm}}. \tag{5} $$

Therefore, **unconditionally**:

$$ \min_{1\le n<m\le N}\|U_n-U_m\| \ \ge\ \exp\big(-8N(1+o(1))\big). \tag{6} $$

This is a genuine, rigorously derived lower bound — and it is **useless** for the dimension
program, because it is *exponential*, and `exp(−8N)` → 0 far faster than any `N^{-C}`.

**The "rational alias" caveat is exactly the case `A_{nm}=0`.** Then `U_n = U_m` exactly
(as rationals on the line, i.e. `‖·‖=0`), and (5) fails. For the *circle* orbit of `{16^{n-1}π}`
aliases are exactly `n,m` with `{16^{n-1}π} = {16^{m-1}π}`, i.e. `16^{m-1}π − 16^{n-1}π ∈ Z`,
i.e. `16^{n-1}(16^{m-n}-1)π ∈ Z` — which cannot happen for irrational `π` (a multiple of π is
never an integer). So **for the true orbit `{16^{n-1}π}` there are no aliases**; aliases can only
appear in the rational approximation `{U_n}` if two truncations accidentally coincide mod 1,
which the exact computation shows does *not* happen for `n<m≤60` (no `A=0` pair found; the
earlier `0.000` in a float run was precision loss, not an alias — see §5).

**Status of (5),(6):** PROVED, with the stated `o(1)`. The bound is sharp *in form* (a rational
with denominator `Q` can sit at distance exactly `1/Q` from 0), but it is **vacuous** for the
intended purpose because it is exponential.

---

## 4. The exact gap between "spacing lower bound" and "positive dimension"

### 4.1 A polynomial spacing bound would still not imply `dim_* > 0`

**Counterexample (classical, and numerically confirmed in the script).** Let

$$ X = \left\{ \frac1k : k\ge1 \right\}\cup\{0\}. $$

The minimal spacing of `{1/k}_{k≤N}` is

$$ \min_{k<\ell\le N}\left|\frac1k-\frac1\ell\right| = \frac{1}{N(N-1)} \sim \frac{1}{N^2}, $$

i.e. **polynomial spacing `~ N^{-2}`**. Yet `X` is a countable set, so its Hausdorff dimension is
`dim_H X = 0`. A sequence with *perfectly good* polynomial spacing can have zero dimension.

The mechanism: spacing lower bounds control the *local* separation of the *first N* points, but
Hausdorff dimension is about the *global* scaling of covering numbers `N(ε)` as `ε→0`, i.e. about
`#\{n: \|x_n-x\|<ε\}` summed over **all** `n`, not just `n≤N`. The set `{1/k}` has polynomial
spacing among its first `N` elements, but it has **exactly one** accumulation point (0), so all
mass concentrates there. A spacing bound prevents *pairs* of close points but not *one-sided
clustering toward a single limit*.

**General principle.** `min_{n<m≤N}‖x_n−x_m‖ ≥ N^{-C}` says: among the first `N` points, no two
are closer than `N^{-C}`. This is compatible with the entire sequence being a Cauchy sequence
converging to a point (spacing `~1/N²` for `1/k`), which has zero-dimensional closure. Positive
lower dimension requires the *opposite*: that the points **spread out** — that for small `ε`,
`N(ε) ≳ ε^{-s}` for some `s>0`, i.e. the points are **uniformly non-concentrated**, not merely
**pairwise non-coincident**.

### 4.2 What additional input is needed (the exact missing arrow)

The correct object is a **Frostman / box-counting lower bound**:

$$ \mu_N(I) \le C\,|I|^s \quad\text{for some }s>0,\ \text{all intervals }I, \tag{7} $$

or equivalently a **covering-number / energy** lower bound. Spacing is a *pairwise* condition;
(7) is a *simultaneous* non-concentration condition. The missing input is any of:

1. **A two-point correlation upper bound** `#\{(n,m): n<m≤N,\ \|U_n−U_m\|<ε\} ≤ C N^2 ε^s` — this is
   *strictly stronger* than `min spacing ≥ N^{-C}`, and it is equivalent (by the standard
   second-moment / energy method) to a positive-dimension statement.
2. **A Weyl/difference bound** `Σ_{h≠0}|Σ_n e(h U_n)|²` small, or any **signed** cancellation —
   which is *precisely* the OPEN signed-Weyl gate `S_N(h)=o(N)` that this rigidity route was
   designed to avoid.
3. **A Hochman–Shmerkin / Furstenberg input** on the ×16-orbit of a point with finite
   irrationality measure (the hope flagged in `X3_RIGIDITY.md` §3) — this is the genuine new
   leverage, but it is **not** delivered by a spacing bound.

**The reduction (this is the honest content of the task).** Suppose a polynomial spacing bound
`min spacing ≥ N^{-C}` were proven. Does it help? *No*: by §4.1 it does not imply `dim_*>0`, and
by the converse (a `dim_*>0` Frostman bound of course implies `min spacing ≥ N^{-C/s}`-type
estimates), the spacing bound is the *strictly weaker* shadow of the target. Proving the spacing
bound is **not** a stepping stone unless the *method* generalizes to two-point correlations — and
every candidate method (see §5) hits the same signed-cancellation wall.

---

## 5. Why the trivial `1/Q` bound cannot be upgraded (the exact obstruction)

From (5) the actual spacing is

$$ \|U_m-U_n\| = \frac{r(A_{nm},Q_{nm})}{Q_{nm}}, \quad r(A,Q)=\min(A\bmod Q,\ Q-A\bmod Q)\in\{1,\dots,\lfloor Q/2\rfloor\}. $$

The trivial bound uses `r(A,Q) ≥ 1`. Empirically (§6) the spacing is `~10^{-4}` while `1/Q ~ 10^{-96}`
at `N=40`, i.e. `r(A,Q) ~ 10^{92}`: the reduced numerator of the difference is a huge integer whose
residue mod `Q` is *generic* (essentially uniformly distributed in `[0,Q]`, hence `r(A,Q) ~ Q/2`).
To prove `r(A,Q) ≥ Q·N^{-C}` (a polynomial spacing bound) is to prove that the *specific* integers

$$ A_{nm} = Q_{nm}\,(U_m-U_n) $$

do **not** land near a multiple of `Q_{nm}`. But `A_{nm} = Q_{nm}(16^{m-1}-16^{n-1})\pi - Q_{nm}(T_m-T_n)`,
and whether `Q_{nm}·16^{n-1}(16^{m-n}-1)\pi` lands near an integer is **exactly** a question about
the continued-fraction / Diophantine approximation of `π` scaled by `16^{m-n}-1` — i.e. about
`‖(16^d -1)π‖` for `d = m-n`. Controlling this for all `d ≤ N` is a **signed Weyl-type** estimate
`Σ_d e((16^d−1)π)` in disguise. This is the same cancellation that is OPEN. There is no free
upgrade; the rational structure gives `1/Q` (exponential) and nothing more without new input.

**Status:** this §5 is a *reduction argument* (not a theorem), explicitly labeled as such. It shows
the spacing bound is **equivalent in difficulty** to the signed-Weyl gate, up to the `o(1)` terms.

---

## 6. Exact verification (reproducible, all arithmetic exact)

Script `spacing_verify.py` (exact `Fraction` throughout; circle distance computed exactly, no float
rounding). Key outputs:

**Minimal circle spacing `min_{n<m≤N} ‖U_n−U_m‖` (exact rational):**

| N  | min spacing | arg `(n,m)` | `log₁₀` spacing |
|----|-------------|-------------|-----------------|
| 10 | `5.9947e-04` | (7, 8)     | −3.22 |
| 20 | `5.9947e-04` | (7, 8)     | −3.22 |
| 30 | `5.3103e-04` | (11, 22)   | −3.27 |
| 40 | `1.0422e-04` | (1, 39)    | −3.98 |
| 50 | `1.0422e-04` | (1, 39)    | −3.98 |
| 60 | `1.0422e-04` | (1, 39)    | −3.98 |

**Empirical growth:** the minimal spacing is *decreasing* (roughly like `N^{-α}`, `α` between 0.3
and 1 in this tiny range), and — decisively — sits at `~10^{-4}`, i.e. **polynomial**, while the
proven `1/Q` lower bound sits at `~10^{-96}`. The observed spacing is *consistent with* polynomial
behaviour **empirically**, but this is a finite observation over `N≤60`, **not** a proof, and it
tells us nothing about whether the true asymptotic is polynomial, sub-polynomial, or exponential.

**Trivial-bound gap (exact), the crux:**

| N  | pair | `‖A/Q‖` (exact) | `1/Q` | `log₂ Q` |
|----|------|-----------------|-------|----------|
| 20 | (7,8) | `5.9947e-04` | `9.68e-20` | 63.2 |
| 40 | (1,39) | `1.0422e-04` | `3.87e-96` | 317.0 |

The reduced numerator `A` has `r(A,Q) ~ Q/2` (generic), so the true spacing exceeds `1/Q` by a
factor `~Q` — the bound (6) is loose by the full conductor width. **No alias** (`A=0`) occurs for
`n<m≤60`; the exact computation confirms the orbit `{U_n}` has `N(N-1)/2` distinct fractional parts
for all `N≤60`.

**Counterexample check:** `{1/k}` has min spacing `= 1/(N(N−1)) ≈ N^{-2}` (polynomial) but
`dim_H = 0` — confirming §4.1.

---

## 7. Claim ledger

| ID | Claim | Status | Evidence |
|----|-------|--------|----------|
| X3-SP-1 | BBP identity `π=Σ16^{1-j}r(j)`, `U_n=16^{n-1}π−T_n`, `T_n→0` | **PROVED** | classical BBP + tail estimate; `spacing_verify.py` |
| X3-SP-2 | `den(U_n) | lcm{8j−7,8j−4,8j−3,8j−2:j≤n}`, `log den ≤ 8n(1+o(1))` | **PROVED** | divisibility exact + Chebyshev `ψ(M)~M` |
| X3-SP-3 | `min spacing ≥ exp(−8N(1+o(1)))` (via `‖A/Q‖≥1/Q`) | **PROVED** (but vacuous) | (5),(6); exponential, weaker than polynomial |
| X3-SP-4 | No rational alias for `n<m≤60` | **PROVED** (finite) | exact computation, all `A≠0` |
| X3-SP-5 | Empirical minimal spacing `~10^{-4}`, decreasing | **OBSERVED** (finite, `N≤60`) | exact rational distances |
| X3-SP-6 | Polynomial spacing bound `min spacing ≥ N^{-C}` | **OPEN / NOT CLAIMED** | reduces to signed-Weyl; §5 |
| X3-SP-7 | Positive lower dimension `dim_*μ>0` | **OPEN** | spacing bound insufficient (§4.1) |

**Boundary (what is NOT established):** no polynomial spacing; no Frostman bound; no
two-point-correlation bound; no positive dimension; π-normality and RH remain OPEN. A polynomial
spacing bound, even if proven, would *not* imply `dim_*>0` (§4.1 counterexample).

---

## 8. Cheapest next step

The spacing route's only hope is to **bypass** the pairwise-to-simultaneous gap: attack the
**two-point correlation / energy bound** directly (equivalently a Frostman bound), not the spacing.
Concretely: bound `#\{(n,m): n<m≤N,\ \|U_n−U_m\|<ε\}` for `ε` below `N^{-1}`, using the
continued-fraction structure of `(16^d−1)π`. This is the *genuinely different* (rigidity/Furstenberg)
lever flagged in `X3_RIGIDITY.md` §3, and it is where the finite-irrationality-measure input
(`μ(π)<15/2`) could bite — a spacing bound alone provably cannot.

---

*Ravel — spacing bound PROVED but vacuous; the honest gap to `dim_*>0` is a Frostman/energy bound,
not a spacing bound. No push, no unproven bound.*
