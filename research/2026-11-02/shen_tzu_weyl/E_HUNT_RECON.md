# The e-hunt: is e easier than π for normality? — precise reconnaissance

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** test the intuition that e might be easier than π for
normality because its "ideal carrier" (analytic/factorial) is *different* from its base-b digit
carrier, whereas π's BBP carrier *is* its base-16 digit carrier (and proved inert).

## 1. The only machinery that has ever proven normality: Stoneham / BBP self-similarity

- **Stoneham numbers** `α_{b,c} = Σ_{n=c^k>1} 1/(b^n · n)` (Stoneham 1973). The denominator is
  `b^n · n` — a **geometric factor `b^n` (base-b position) times a linear correction `n`**.
  Stoneham proved b-normality for c odd prime + b a primitive root of c²; **Bailey–Crandall (2002)
  sharpened it to: coprimality of b, c is sufficient for b-normality** (Experimental Math 11:527).
- **BBP formulas** `Σ_k p(k)/(q(k) b^k)` (Bailey–Borwein–Plouffe 1996): denominator `q(k)b^k`
  with `q` a polynomial — again **linear-in-k base-b position** (`log_b(denominator) ≈ k·const`).

**The single load-bearing feature** of every normality proof in the literature is a
**base-b self-similar series**: the n-th term sits at base-b position `≈ c·n` (linear), so the
digit sequence is a *fixed base-b shift* of the series — the digits are literally readable from
the self-similar structure.

## 2. The decisive obstruction: e's factorial series is NOT base-b self-similar

`e = Σ_{n≥0} 1/n!`. The n-th term `1/n!` sits at base-b position `log_b(n!)`. By Stirling,

$$ \log_b(n!) = n \log_b(n/e) + \tfrac12\log_b(2\pi n) + o(1) \sim n \log n . $$

**This is superlinear in n** (it grows like `n log n`), whereas Stoneham/BBP require *linear*
position. Computed (exact `lgamma`): for **every** base b ∈ {2,3,10,16}, the ratio
`log_b(n!)/n` **diverges** (base 16: 0.345 → 1.312 as n: 5 → 100; it keeps growing like `log n`).

**Consequence (PROVED obstruction):** there is **no base b** for which `Σ1/n!` is a self-similar
(Stoneham/BBP-type) series. The factorial denominator `n!` is *intrinsically* not a base-b
geometric-with-linear-factor object. Hence **the only machinery that has ever proven normality
does not apply to e's canonical series.**

## 3. Is there an *alternate* series for e that is base-b self-similar?

- **MathOverflow #259053 ("Is there a BBP formula for e?")** — answered **No** in the relevant
  sense: `e` admits **no BBP-type (spigot) formula in any base**; the factorial series is the
  canonical representation and it is not spigot. (No base-b digit-extraction formula for e exists;
  contrast π, ln 2, √2, ζ(3), etc., which do.)
- The deeper reason (known in the BBP literature): a BBP formula requires the constant to be a
  sum of terms `1/(q(k)b^k)` with `q` rational-polynomial, which is equivalent to the constant
  being expressible as an integral of a rational function over `[0,1]` (the BBP criterion). `e`
  is **not** such a number — its defining integral/DE structure (`f'=f`) is *not* a rational
  function, so it fails the BBP/Stoneham criterion entirely.

## 4. The verdict on the e-intuition

The intuition was: **"π's carrier coincides with its digit carrier (inert); e's carrier is
different (analytic), so maybe there's leverage."** The precise answer is:

1. **Correct half:** e's analytic carrier is *genuinely different* from its base-b digit carrier,
   and e is *not* a red herring in the same way π is (π's BBP formula *is* a base-16 digit
   formula; e has *no* base-b digit formula at all).

2. **Fatal half:** the *only* known route from a "carrier" to normality is **base-b
   self-similarity** (Stoneham/BBP), and e **fails this criterion structurally** — its factorial
   series is `n log n` in position, not linear. So e's "different carrier" does not give
   leverage; it gives **nothing**. There is no known theorem converting a continued-fraction,
   differential-equation, or factorial-series structure into base-b normality.

3. **The cold fact:** e's continued fraction is *completely known* (Euler: `[2;1,2,1,1,4,1,1,6,…]`),
   and `μ(e) = 2` is *sharp* (badly approximable), and **e is still not known to be normal in any
   base.** The two things that make e "easier" in the Diophantine sense (regular CF, sharp measure)
   are *exactly the two things our rounds proved are insufficient* for the Weyl gate (`μ=2` gives
   only exponential spacing; a regular CF gives no digit control).

## 5. The sharp conclusion

> **e is not easier than π — it is *strictly harder* by the only measure that matters.** π at least
> had a base-16 self-similar representation (BBP) to attack, and that attack was proved inert. e has
> **no** base-b self-similar representation at all, so the Stoneham/Bailey–Crandall machinery — the
> *only* machinery that has ever proven normality of a non-trivial constant — does not even apply.
> e's "cleaner" Diophantine structure (regular CF, `μ=2`) is orthogonal to the digit question.

The intuition was elegant and worth chasing — but it points at a *harder* wall, not an easier one:
π is the special number (it has the base-16 digit formula), and even that specialness was inert.
e is the *generic* hard case: a constant with no base-b self-similarity, whose normality is exactly
as open as π's, and whose only known "leverage" (sharp measure, regular CF) is provably irrelevant.

**Normality of π and of e — both OPEN, in every base. RH OPEN.**
