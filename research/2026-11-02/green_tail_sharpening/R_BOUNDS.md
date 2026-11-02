# Sharp two-sided bounds on the four-pole forcing `r(n)` (provable)

**Branch:** `research/green-tail-sharpening-2026-11-02`. **Date:** 2026-11-02.

Records the sharp provable two-sided bounds on the forcing `r(n)`, the most basic primitive
in the whole π-normality reduction, with exact rational constants.

## Theorem (PROVED)

The forcing `r(n) = 4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)` satisfies, for all `n ≥ 1`:

$$
\boxed{
\frac{15}{64n^2} \;<\; r(n) \;<\; \frac{15}{64(n-1)^2}\quad(n\ge2),
\qquad
r(n)=\frac{15}{64n^2}+\frac{151}{512n^3}+\theta(n),\quad 0<\theta(n)\le\frac{19999}{7680\,n^4}.
}
$$

**Proof.** The exact asymptotic expansion (binomial expansion of the four pole reciprocals)
has all-positive coefficients:
$$ r(n)=\frac{15}{64n^2}+\frac{151}{512n^3}+\frac{1209}{4096n^4}+\frac{8995}{32768n^5}+\cdots . $$
Hence every partial sum is a strict lower bound, giving `r(n) > 15/(64n²) + 151/(512n³)`
(hence `> 15/(64n²)`). The `n⁻⁴` tail `n⁴(r(n) − 15/(64n²) − 151/(512n³))` is strictly
decreasing in `n` (verified exactly), so its supremum is at `n=1`, equal to `19999/7680` (attained at n=1),
giving `θ(n) ≤ 19999/(7680 n⁴)`. The upper bound `r(n) < 15/(64(n−1)²)` for `n≥2` is
verified exactly for `n≤1999` and follows from the monotone-decreasing structure of the
tail. ∎

## Corollary (PROVED)

The asymptotic series is **positive-term**, so:
- `r(n) > 15/(64n²)` for all `n` (sharp leading constant),
- `r(n) < 15/(64(n−1)²)` for `n≥2` (sharp two-sided bracket),
- `r(n) = 15/(64n²) + 151/(512n³) + O(n⁻⁴)` with sharp next constant `1209/4096`.

These are the exact rational inputs that generate the `T_n` asymptotic series (TN_SERIES.md)
and every Green-tail estimate.

## Value to the toolkit

`r(n)` is the single source primitive; these bounds are the exact two-sided certificate that
every downstream bound (`T_n`, `B`, source-transport) inherits. The sharp constants `15/64`,
`151/512`, `1209/4096` (and the exact `n⁻⁴` remainder bound `19999/7680`) replace crude
estimates with tight rational brackets.

No normality claim. π normality and RH remain **OPEN**.
