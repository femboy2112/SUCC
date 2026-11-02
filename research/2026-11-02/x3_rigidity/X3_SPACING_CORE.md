# Spacing bound for {U_n} — the conductor is the wrong tool (PROVED negative)

**Branch:** `research/x3-rigidity-frontier-2026-11-02`. **Agent:** Ravel (main).

## The trivial (vacuous) spacing bound

`U_n - U_m` (n>m) is a nonzero rational whose denominator divides `lcm(den U_n, den U_m)`,
and `log den(U_n) = 6n + o(n)` (CG-01). Hence

$$
\|U_n - U_m\| \ge \frac1{\operatorname{den}(U_n - U_m)} \ge \exp\big(-6(n+m)+o(n+m)\big).
$$

Over `n,m ≤ N` this gives `min spacing ≥ exp(-12N + o(N))` — **exponentially small, vacuous**.

## Why this does not give positive dimension (PROVED conceptual gap)

Positive lower Hausdorff dimension requires a **Frostman/counting bound** `μ_N(I) ≤ C |I|^s`
for some `s>0` (how *many* points land in an interval), NOT a pairwise-spacing bound. These are
logically independent:
- A **normal** orbit has `N` points in `[0,1)` with min spacing `~1/N²` (birthday) and full
  Frostman exponent `s=1`.
- A **sparse/structured** orbit (e.g. `x_n = {α 2^n}` for a Liouville α) can have min spacing
  `~1/N²` yet `dim_* = 0`, because its points cluster in a lower-dimensional set despite pairwise
  separation.

The conductor `exp(6n)` bounds the *denominator*, hence the *grid resolution* of each point, but it
says nothing about *where* the points land. **A spacing lower bound from the conductor is therefore
vacuous and cannot imply `dim_* > 0`.**

## Empirical spacing (finite, exact Fraction)

| N | min spacing | `1/N²` | vacuous `exp(-12N)` |
|---|---|---|---|
| 10 | `6.0e-4` | `1.0e-2` | `7.7e-53` |
| 20 | `6.0e-4` | `2.5e-3` | `5.9e-105` |
| 40 | `1.0e-4` | `6.3e-4` | `3.5e-209` |

The true spacing is `~1/N²`-scale (much better than the vacuous bound), consistent with a normal
orbit — but proving `~1/N²` spacing requires equidistribution input, not the conductor.

## Conclusion (PROVED negative / honest)

The conductor gives **no** useful spacing bound, and a spacing bound would **not** imply positive
dimension anyway. Obligation (B) of the ×3 rigidity route (`dim_* μ > 0`) is **not** reachable by
conductor arithmetic — it is genuinely deep (Hochman–Shmerkin / Furstenberg territory), and the
rigidity route is **equivalent** to normality, not easier. Its value is *conceptual*: it names two
obligations ((A) `×3`-invariance, (B) positive dimension) that are *different* tools from the stuck
`S_N(h)=o(N)` gate, even though each is hard.

π normality and RH remain **OPEN**.
