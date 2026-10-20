# Goldbach major arcs — singular-series finite transport + Siegel–Walfisz benchmark

**Operation:** Proof Forge III, Part VI (Goldbach major arcs with real error terms).
**Lane:** F (harmonic analyst).
**Branch / worktree:** `research/pf3-lane-goldbach-2026-10-20` in `/home/leah/SUCC-pf3-gb`.
**Date:** 2026-10-20.
**Module:** `observational_succ/goldbach_circle.py`. **Tests:** `tests/test_goldbach_circle.py` (25 pass, 0 fail).

**BINARY GOLDBACH: OPEN.** Nothing here asserts it. The minor-arc estimate is the open
difficulty and is explicitly left open. RH is not used; no zeta-zero ordinate appears anywhere.

---

## 0. AGENTS.md status labels used

- **CLASSICAL** — a statement that is standard, established mathematics (Hardy–Littlewood singular
  series; Siegel–Walfisz).
- **PROVED LOCAL** — proved here, exactly, on the stated finite window / truncation, with a machine-checked
  receipt (exact `fractions.Fraction` equality), *not* a new global theorem.
- **CONJECTURED / OPEN** — a predicted asymptotic shape with no proof available to this lane.
- **IMPORTED** — depended upon as an external theorem, cited, not re-proved here.

Every claim below carries: domain, definitions, hypotheses, quantifiers, status, derivation/receipt,
provenance, adversarial countermodel, and the next falsification opportunity.

---

## 1. Preserved identities (unchanged)

The additive identity and the singular-series enclosures are **preserved exactly** (not touched by this lane
except by the docstring correction in §3):

> **GC-01 (CLASSICAL; PROVED LOCAL).** With `e(x)=e^{2πix}`, `F_N(θ)=Σ_{n=1}^{N-1} Λ(n) e(nθ)`,
> `R_Λ(N) = Σ_{a+b=N} Λ(a)Λ(b) = ∫_0^1 F_N(θ)² e(−Nθ) dθ = [z^N] F_N(z)²`.
> **This is `F²`, not `|F|²`.** The `|F|²` object extracts the *difference* diagonal `Σ_{a−b=N} Λ(a)Λ(b)`,
> identically `0` on the window — the BS-G1 firewall. (`R_Lambda_from_fourier_poly`, `R_Lambda_from_dft`,
> `difference_diagonal`, `fourier_identity_check`; tests unchanged.)

> **GC-02 (CLASSICAL object; CONJECTURED asymptotic).** `𝔖(N) = Π_p 𝔖_p(N)`,
> `𝔖_p(N) = 1 + 1/(p−1)` if `p|N`, else `1 − 1/(p−1)²`; `𝔖(N)=0` for odd `N`. Certified rational two-sided
> enclosure `singular_series_enclosure(N,P)` via the tail bound `Π_{p>P}(1−1/(p−1)²) ∈ [1−1/(P−1), 1]`.
> (`singular_series_local_factor`, `singular_series_truncated`, `singular_series_enclosure`; unchanged.)

---

## 2. The one proved transport lemma — GC-03 (CLASSICAL; PROVED LOCAL)

> **Lemma (finite singular-series transport).**
> Let `N` be **even** and let `P ≥ P₀(N) := max{ p prime : p | N }`. Define
> `T(P) = Π_{2<p≤P}(1 − 1/(p−1)²)` (so `2·T(P)` is the upper value returned by
> `twin_prime_constant_enclosure(P)`) and the **exact rational transport factor**
> `K(N) = Π_{p|N, p odd}(p−1)/(p−2)` (`odd_prime_transport_factor`, over DISTINCT odd primes).
> Then the truncated Goldbach singular series factorises **exactly**:
>
> &nbsp;&nbsp;&nbsp;&nbsp;**`𝔖_{≤P}(N) := Π_{p≤P} 𝔖_p(N) = 2 · T(P) · K(N).`**   *(approximation error = 0, exact in `Fraction`)*
>
> Consequently the **full** singular series obeys the certified two-sided enclosure
>
> &nbsp;&nbsp;&nbsp;&nbsp;**`2·T(P)·(1 − 1/(P−1))·K(N) ≤ 𝔖(N) ≤ 2·T(P)·K(N)`**,
>
> with certified **relative width ≤ 1/(P−2)**. For odd `N`, `𝔖(N) = 0`.

**Domain / quantifiers.** `∀` even `N ≥ 4`, `∀` integer `P ≥ P₀(N)`. (For odd `N`: both sides `0`.)

**Proof (pure finite Euler-product algebra; no analytic input).**
`𝔖_2(N) = 1 + 1/(2−1) = 2` (as `N` even). For an odd prime `p`:
`p∤N ⇒ 𝔖_p = 1 − 1/(p−1)² = p(p−2)/(p−1)²`; `p|N ⇒ 𝔖_p = 1 + 1/(p−1) = p/(p−1)`.
Start from the base product `Π_{2<p≤P}(1−1/(p−1)²) = T(P)`. For each odd `p|N` (all `≤ P` by hypothesis),
replace its `(1−1/(p−1)²)` factor by the enhanced `(1+1/(p−1))`; the per-prime replacement ratio is
`[p/(p−1)] / [p(p−2)/(p−1)²] = (p−1)/(p−2)`, and the product of these over the odd `p|N` is `K(N)`.
Hence `𝔖_{≤P}(N) = 2·T(P)·K(N)`. The enclosure follows from the elementary convergent-tail comparison
`Π_{p>P}(1−1/(p−1)²) ≥ 1 − Σ_{n>P} 1/(n−1)² ≥ 1 − 1/(P−1)` and `≤ 1`. ∎

**Status:** CLASSICAL identity (it is the standard even-`N` Euler-product reduction of 𝔖), PROVED LOCAL here as
an exact machine-checked receipt.

**Error term (honest).** The **identity** `𝔖_{≤P}(N) = 2·T(P)·K(N)` has **zero** approximation error (exact
`Fraction`). The only inexactness in the enclosure of the *full* `𝔖(N)` is the Euler tail, bounded exactly by
`1/(P−1)` (relative width `≤ 1/(P−2)`). No floating point enters the certificate.

**Hypotheses that are load-bearing.**
- `N` **even** (else `𝔖(N)=0`; the `p=2` factor vanishes).
- `P ≥ P₀(N)`: **required.** If some odd `p|N` exceeds `P`, its enhanced factor `𝔖_p > 1` is simply absent from
  the base product and the identity is false. Enforced: `singular_series_via_transport` raises
  `GoldbachCircleError` when `P < P₀(N)`.

**Imported-theorem dependencies: NONE.** Only elementary finite algebra plus the convergent-tail comparison.
No Siegel–Walfisz, no RH, no zeta zeros.

**Independent cross-check (two routes agree).** `singular_series_via_transport(N,P)` (base-constant route) equals
`singular_series_truncated(N,P)` (direct Euler-product route) exactly, and
`singular_series_transport_enclosure(N,P)` equals `singular_series_enclosure(N,P)` exactly — verified for
`N ∈ {6,10,14,18,22,30,42,100,210,2310}`. This is the Lab-Notebook "two blind paths" discipline: the transport
factorisation and the direct product are genuinely different computations that must, and do, coincide.

**Adversarial countermodels (all handled).**
- *Drop `P ≥ P₀(N)`* → identity fails (missing enhanced factor); guarded by a raise, tested (`2·101`, `P=50`).
- *Multiplicity confusion* → `K` uses DISTINCT primes; `K(6)=K(18)=2`, tested.
- *Odd `N`* → `𝔖=0`; both transport functions return `0`, tested.

**Next falsification opportunity.** Extend the transport to `𝔖_t(N)` for the `t`-fold Goldbach / Waring-type
singular series and check the exact `K_t(N)` factor against the direct `t`-fold Euler product; any mismatch
refutes the generalisation.

---

## 3. Docstring correction — `twin_prime_constant_enclosure` (what was wrong)

**Reproduced before trusting** (scratch check, `P=20000`, exact `Fraction`): the function's upper value is
`1.3203297… ≈ 2·C₂` (`C₂ = Π_{p>2}(1−1/(p−1)²) ≈ 0.6601618`). It does **not** equal `𝔖(2q)` for any finite odd
prime `q`: measured ratios `𝔖(6)/2C₂ = 2`, `𝔖(10)/2C₂ = 4/3`, `𝔖(14)/2C₂ = 6/5`.

**Verdict: the CODE was RIGHT, the DOCSTRING was WRONG.** The code correctly computes a certified enclosure of
the base constant `2·C₂`. The old docstring asserted *"2·C₂ is `𝔖(N)` for `N = 2·(an odd prime)` with the prime
> P"* — a false identification. The true relation (now in the corrected docstring, and encoded by GC-03) is

&nbsp;&nbsp;&nbsp;&nbsp;`𝔖(2q) = 2·C₂·(q−1)/(q−2)`  (q odd prime),  and generally  `𝔖(N) = 2·C₂·Π_{p|N, p odd}(p−1)/(p−2)`.

`2·C₂` is only the **limit** of `𝔖(2q)` as `q → ∞`. The corrected docstring keeps the base constant explicitly
DISTINCT from the full singular series and points to `odd_prime_transport_factor` / `singular_series_via_transport`.
Tests pin `(q−1)/(q−2) = 2, 4/3, 6/5` for `q = 3,5,7` exactly, and assert `𝔖(2q) ≠ 2·C₂`.

(The pre-existing `ARITHMETIC_FRONTIER.md` §7.3 already described the function correctly as bracketing `2C₂`;
only the in-code docstring carried the erroneous identification. No behaviour changed.)

---

## 4. Major-arc benchmark under IMPORTED Siegel–Walfisz (`major_arc_benchmark`)

This is the **quantitative major-arc benchmark** (Part VI item 3). It is a STRUCTURAL benchmark: it assembles,
with honest labels, exactly what Siegel–Walfisz does and does not give, and keeps the one exactly-certified
piece (the singular series, via GC-03) separate from the ineffective analytic input.

**Setup / definitions (stated precisely).**
- **Size parameter:** even `N ≥ 4`.
- **Carrier / exponential sum:** `F_N(θ) = Σ_{n=1}^{N-1} Λ(n) e(nθ)`, `e(x)=e^{2πix}`, on the circle `ℝ/ℤ`
  (period-1 wraparound). **Target:** `R_Λ(N) = ∫_0^1 F_N(θ)² e(−Nθ) dθ` — the `F²` carrier, not `|F|²`.
- **Major-arc cutoff:** `Q_SW = ⌊(log N)^A⌋` for a fixed `A > 0`. Major arcs `𝔐(a,q) = {θ : |θ−a/q| ≤ 1/(qN)}`
  over `q ≤ Q_SW`, `(a,q)=1`, `0 ≤ a < q`. **Width:** half-width `1/(qN)` (as exposed by `farey_major_arcs`).
  **Disjointness:** distinct Farey centres `a/q ≠ a'/q'` with `q,q' ≤ Q_SW` are separated by `|a/q−a'/q'| ≥
  1/(qq') ≥ 1/Q_SW²`; with half-widths `1/(qN) ≤ 1/N` the arcs are pairwise disjoint once `N ≥ 2Q_SW²`
  (comfortably true since `Q_SW = (log N)^A ≪ N^{1/2}`).

**IMPORTED THEOREM (Siegel–Walfisz).** Fix `A > 0`. Uniformly for `q ≤ (log x)^A` and `(a,q)=1`,
`ψ(x; q, a) = x/φ(q) + O_A( x · exp(−c_A √(log x)) )`, where `ψ(x;q,a) = Σ_{n≤x, n≡a (q)} Λ(n)`.
Provenance: standard (Davenport, *Multiplicative Number Theory*, §22; via the Siegel–Walfisz theorem).

**CRITICAL HONESTY — the error term is INEFFECTIVE.** The constant `c_A` (and the `O_A`-implied constant)
depends on a *possible Siegel zero* and is **ineffective**: no computable numerical value is available. Hence the
major-arc asymptotic yields **no numerical certificate** (AGENTS.md discipline 8: finite precision is not a
certificate without a rigorous, *independently derived* error bound — which an ineffective constant is not).
`major_arc_benchmark` therefore returns the analytic-asymptotic fields as **labelled strings**, never as a float
posing as a bound.

**BOUNDED UNIFORMITY (the explicit warning asked for).** Siegel–Walfisz controls **only** `q ≤ Q_SW =
(log N)^A`. One must **NOT** infer a uniform arbitrary-`Q` major-arc asymptotic from it. The major arcs with
`(log N)^A < q ≤ N^{1/2}`, and the whole minor-arc complement, are **not** controlled by Siegel–Walfisz. This is
precisely why Siegel–Walfisz **alone does not prove binary Goldbach**.

**Approximation error (what each term is).**
1. *Prime-distribution error* (per major arc): `O_A(N exp(−c_A √log N))`, **ineffective** → not certified.
2. *Singular-series truncation error* `𝔖(N) − 𝔖_{≤P}(N)`: **exactly certified** by GC-03 — relative tail
   `≤ 1/(P−2)`, returned as `singular_series_bracket` (an exact `Fraction` pair) and
   `singular_series_truncation_rel_error_upper = 1/(P−2)`.
3. *Minor-arc contribution:* **OPEN** for the binary problem.

**Source restrictions.** Λ is the true von Mangoldt weight (no fake composite, no matched non-Euler surrogate).
`R_Λ` is the ADDITIVE convolution `Λ *₊ Λ`, generated by `F_N²` — never `|F_N|²`, never the MULTIPLICATIVE
`(−ζ′/ζ)²` (the `arithmetic_interactions.illegal_interchange_witness`, `N=5`, firewall). No zeta zero is used.

**Status.** Major-arc asymptotic SHAPE: CLASSICAL. Its error term: IMPORTED + ineffective → **not a
certificate**. Singular-series bracket: PROVED LOCAL (exact). Minor arc: **OPEN**.

---

## 5. What stays open (stated plainly)

- **Binary Goldbach: OPEN.** The binary **minor-arc** estimate — showing the minor arcs contribute
  `o(𝔖(N)·N)` — is the open difficulty and is **not** attempted here. (Ternary Goldbach is Vinogradov's
  theorem; the binary minor-arc smallness is unknown.)
- The Siegel–Walfisz major-arc error is **ineffective**; even the major-arc asymptotic is not a numerical
  certificate. This lane does not assert a uniform arbitrary-`Q` major-arc asymptotic.
- No claim that `R_Λ(N) ~ 𝔖(N)·N`. `goldbach_main_term_enclosure` returns only the CONJECTURED prediction;
  `singular_series_comparison_evidence` is finite-sample float EVIDENCE, not a certificate.

---

## 6. Provenance / receipts

- Code: `observational_succ/goldbach_circle.py` — new GC-03 block: `odd_prime_transport_factor`,
  `singular_series_via_transport`, `singular_series_transport_enclosure`, `major_arc_benchmark`; corrected
  docstring of `twin_prime_constant_enclosure`. All pre-existing functions and GC-01/GC-02 identities unchanged.
- Tests: `tests/test_goldbach_circle.py` — new `TestSingularSeriesTransport` (7) and `TestMajorArcBenchmark` (2).
  **Before:** 16 tests pass. **After:** 25 tests pass, 0 fail (all previously-passing tests still green).
- Validation run: `PYTHONPATH=/home/leah/SUCC-pf3-gb python -m unittest tests.test_goldbach_circle -v` → `OK`
  (25 tests); `python -m compileall -q observational_succ` → clean for `goldbach_circle.py`.
- Everything exact (`fractions.Fraction` / sympy). A float is never a certificate.
