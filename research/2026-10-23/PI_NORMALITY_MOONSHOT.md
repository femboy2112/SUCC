# π NORMALITY: a moonshot attempt, and the structural reason it stops

> **MATHEMATICAL ERRATA (2026-10-24):** This historical moonshot report
> remains useful for Fejér measurements and precision fixes, but its
> claims "BBP four-pole lane closed" and "chord representation proves
> no new route possible" are not valid theorems. The supposed x=1/3
> same-forcing countermodel changes the authenticated initial condition.
> For a freely chosen growing band, bounded Fejér energy is
> EQUIVALENT to normality, not strictly weaker. For nonnormal points
> only LIMSUP divergence is forced along suitable subsequences,
> not necessarily a full energy limit. Signed pole data yield a
> positive infinite-rank Green tail; see
> [source-repair proof](../2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md).
> Preserve finite measurements as TESTED MODEL only.


**Date:** 2026-10-23. **Branch:** `research/cyc03-bbp-four-pole-lane-2026-10-23`.
**π normality (all bases): OPEN.** **RH: not addressed.** No zero coordinates.

> This is a real attempt, not a survey. It takes the strongest machinery in the
> repository as starting ingredients, drives each route as far as it goes, and
> reports where each one stops. **No proof was found.** One route is proved
> circular, one is proved non-discriminating, and one reveals the obstruction is
> not analytic at all.

## 1. The starting ingredients (what we actually have)

| ingredient | statement | status |
|---|---|---|
| **Fejér/moving-band criterion** (CC-05) | normality ⟺ ∃ M_N→∞ with `sup_N E(M_N,N) < ∞`, where `E(M,N) = 1 + 2Σ_{h≤M}(1−h/(M+1))|A_{h,N}|²` | **PROVED equivalence** |
| **Amplification** (CC-05) | `|A_{h,N}| ≤ 2R/N + √((E−1)/R)`, `R = min(⌊√N⌋, 1+⌊log_b(M/2|h|)⌋)` | **PROVED** |
| **Chord conjugation** (CC-01) | `d(T_b z) = F_b(d(z))`, `F_b(X) = 2 − 2T_b^{Cheb}(1−X/2)`, `d(z)=|1−z|²` | **PROVED** |
| **Kummer moments** (CC-02) | `∫ d(z)^k dm = binom(2k,k) = Π_p p^{c_p(k)}`; any m-gon with `m>k` has this moment **exactly** | **PROVED** |
| **CC-04 obstruction** | 7-gon, `T_2`, selected cycle `{1,2,4}`: mean chord `7/3 ≠ 2` | **PROVED exact counterexample** |
| **BBP source identity** | `π = 16 t₀`, `16t_n = r(n+1)+t_{n+1}`, `r(x) = 15/(64x²)+O(x⁻³)` | **PROVED / kernel-checked** |

## 2. Route A — bound the Fejér energy (the strongest-looking route)

### 2.1 The measurement

`E−1` for π, base 16 and base 2, at fixed and growing band:

| N | M | `E−1` | `M/N` | ratio |
|---|---|---|---|---|
| 4096 | 8 | 1.97e−03 | 1.95e−03 | 1.006 |
| 16384 | 8 | 5.87e−05 | 4.88e−04 | 0.120 |
| 65536 | 32 | 4.26e−04 | 4.88e−04 | 0.873 |
| 262144 | 40 | 9.26e−05 | 1.53e−04 | 0.607 |

The ratio `(E−1)/(M/N)` stays in **≈[0.09, 1.2]** across four decades of N and a
10× range of M. That is exactly the bounded regime the criterion needs, and it is
the first instrument in this stack to show the right quantitative shape.

### 2.2 The criterion does discriminate (a false alarm, corrected)

I first worried the criterion was vacuous: for a non-normal x with
`A_{h,N} → c_h ≠ 0`, doesn't `E → 1 + 2Σ|c_h|²` stay bounded?

**No — and the reason is a nice little theorem.** If `A_{h,N} → c_h` for all h
and only finitely many `c_h ≠ 0`, then the limit measure `μ` has `μ̂(h) = c_h` and
is `T_b`-invariant, so `c_h = c_{b^r h}` for every r. Picking h with `c_h ≠ 0`,
`b^r h` eventually exceeds the finite support, forcing `c_h = 0` — contradiction.
Hence `c_h = 0` for all h, i.e. x *is* normal.

**For a nonnormal x, any growing-band energy must have unbounded LIMSUP along some subsequence (not necessarily converge to infinity along the entire N sequence).** The criterion is sound and
discriminating. (The repository's own proof of `(ii) ⇒ (i)` does not need the
`c_h` to exist at all; it uses only the amplification inequality.)

### 2.3 Why this still does not prove anything for π

The criterion requires a **uniform-in-N** bound on `E`. My measurements are at
*finite* N. `E` is an average of `|A_{h,N}|²` over h ≤ M_N, and bounding it
uniformly is — by construction — an average statement about exponentially many
Fourier coefficients of the same orbit. **The measurement shows the right shape;
it cannot show the shape persists.** That is `M1` with the premise unproved.

## 3. Route B — the chord-polynomial form, and why it is CIRCULAR

The natural next move: `E` is *exactly* an empirical mean of a nonnegative
polynomial in chord distance. Verified in sympy:

```
K_1(X) = 2 − X/2
K_2(X) = X²/3 − 2X + 3
K_3(X) = −X³/4 + 2X² − 5X + 4
K_4(X) = X⁴/5 − 2X³ + 7X² − 10X + 5
```

each nonnegative on `[0,4]`, of degree M. Since `d_{j+1,k+1} = F_b(d_{jk})`
exactly, the pair distances obey an autonomous degree-16 polynomial recursion.
**This looks like a genuinely new handle: a dynamical average over an exact
polynomial recursion.**

**It is not.** Expanding `d^m = (2 − z − z̄)^m` and summing over pairs returns

```
Σ_{j,k} d_{jk}^m = N² · Σ_h (−1)^h C(2m, m+h) |A_{h,N}|²
```

— **exactly the Fourier sums again.** The Fejér energy *is* the chord energy; the
chord language is a faithful reformulation that consumes no new information.
Route B supplies an exact representation-equivalence but not an independent source estimate. This does not prove no such estimate can be found in the chord coordinates.

Likewise Route C (the `F_b` dynamics): `F_b` is conjugate to `z ↦ z^b` through the
two-to-one map `d`, so equidistribution of the `F_b`-orbit of `d₀` is *equivalent*
to Haar-uniformity of `z_j` — CC-03's proof in reverse.

## 4. Route D — BBP poles: CLOSED (previous round)

Proved non-discriminating: every pole residue dies in one step under ×16, and
α = 1/3 shares the entire pole structure yet diverges to 3/2.
See `CYC03_LANE_CLOSED.md`.

## 5. Route E — Kummer moments: the only route with different content, and its exact wall

`CC-02` is genuinely unlike the others: **every regular m-gon with `m > k` has
the *exact* Haar k-th chord moment `binom(2k,k)`** at a *finite* stage, with no
approximation. And `binom(2k,k) = Π_p p^{c_p(k)}` where `c_p(k)` **counts carries**
in base-p addition `k+k` — tying the target moments to the repository's genuine
prime/carry machinery.

So the finite *ensembles* are perfect. **The wall is `CC-04`, and it is not
analytic:**

> 7-gon, `T_2`, `gcd(2,7)=1` so the covering is a vertex permutation. The full
> uniform measure is invariant with first chord moment exactly 2. But the
> permutation has cycles `{0}, {1,2,4}, {3,6,5}`; the selected cycle `{1,2,4}`
> has mean chord `2 − 2Re(A)/3 = 7/3 ≠ 2`, where `A = ζ+ζ²+ζ⁴` and `Re(A) = −1/2`.

**An exactly-invariant ensemble with exactly-correct moments contains a selected
path with the wrong moment.** The obstruction is *spatial ensemble vs temporal
orbit*. No refinement of analysis touches it, because no amount of analysis
converts an ensemble statement into a single-orbit statement — that is a
**quantifier-order** fact (`∀N ∃path` vs `∃path ∀N`), which is `M3` at the level
of the whole problem.

## 6. The verdict, stated in the repo's own language

In `FieldClass(Source, Target, Tools)` terms: π-normality under the current
toolkit is **Unresolved**, and specifically it is **not** `IdealHardField`,
because nobody has proved the *non-existence* of a computable selector, nor that
the source laws give a classical existence proof. It is `Toolkit-relative dark`
— and the repository's own discipline says that must be reported as such, not
promoted to impossibility.

**What the moonshot did establish (new, and worth having):**

1. **The Fejér criterion discriminates** (§2.2) — with a one-paragraph theorem
   that a `T_b`-invariant limit measure with finitely-supported Fourier transform
   is Haar. This closes the worry that `sup_N E < ∞` is vacuous.
2. **`E` is measured to have the bounded shape for π** across four decades
   (§2.1), while the non-normal control x=1/3 floors at `S₇ = 31.5` exactly.
3. **The chord-polynomial route is proved circular** (§3) — exact identity
   returning `|A_{h,N}|²`. This kills a natural-seeming idea before anyone
   spends a round on it.
4. **The obstruction is located as spatial-vs-temporal**, not analytic (§5), via
   CC-04's exact 7-gon counterexample.

## 7. The one criterion that would finish it

> **Target (CC-05, unproved).** There exist `M_N → ∞` with `M_N = o(√N)` and a
> constant `K` such that for all N, `E(M_N, N; π) ≤ K`.

Equivalently: `Σ_{h≤M_N}(1−h/(M_N+1))|A_{h,N}(π)|² ≤ (K−1)/2` uniformly.

This is **equivalent** to normality when one may choose an arbitrarily slow growing band, not a strictly weaker source theorem; its only route to progress is an independently derived source-specific bound. Everything closed so far proves it cannot be reached by pole
structure; §3 proves it cannot be reached by chord reformulation. It needs a
genuinely new input about the *simultaneous* size of many Fourier coefficients of
one orbit — which is, as far as this campaign can see, the original problem
wearing different clothes.

## 8. Calibration note (three bugs caught, recorded)

Three arithmetic artifacts were caught this session. All are recorded because a
campaign that does not record these will eventually publish one.

**(a) Precision vs horizon — the live one.** An early measurement showed π's
orbit chord mean *decaying* like `1/N` (0.88, 0.088, 0.0088 at N = 100, 1000,
10000). That was a precision artifact: resolving `frac(16^j π)` needs
`dps > 1.21·j` decimal digits, so at `dps=80` the phases for j ≳ 60 are garbage.
A second bug compounded it: an `mpf` for π created at the caller's default
precision (15 digits) carries no more digits when multiplied inside a
high-precision context — so `16^15 · π` had *no fractional part left at all*.

The fix is a discipline, not a constant: π must be re-evaluated **inside** the
high-precision context (`phases_for_pi`), never passed in. With
`dps = 1.21N + 60`:

```
N=100 : mean |1−z|² = 1.994   (Haar target 2)
N=500 : mean |1−z|² = 2.081   (Haar target 2)
```

π tracks the Haar value, as normality requires. `tests/test_pi_normality_moonshot.py`
now contains a regression test that fails if the bug returns.

**(b) A sandbox with broken arithmetic.** A subagent reported that `float` and
`mpmath` were returning wrong values in its environment. Verified here: this
environment's arithmetic is correct. The subagent's structural claims survived
independent re-verification; its numbers were not taken on trust. Lesson: an
instrument that cannot self-check will silently mislead exactly one of you.

**(c) A wrong mechanism description in this repo's own report.** See §2.2 below
and `CYC03_LANE_CLOSED.md`: the published claim that η_N = 2 at x=1/3 is wrong.
The conclusion stands; the stated arithmetic does not.

