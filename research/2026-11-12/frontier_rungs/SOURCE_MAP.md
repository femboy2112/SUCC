# Source map — frontier rungs round (2026-11-12)

What this round rests on, and how each external statement was verified. Grades:

- **READ-AT-SOURCE** — a helper instance read the statement in the paper, an author preprint or the
  abstract on 2026-11-12 (text extractions kept outside the repository; they are receipts of a
  reading, not redistributed here).
- **SECONDARY** — quoted from a survey, a review or a later paper.
- **CLAIMED / UNVERIFIED** — an unrefereed 2026 claim; never used as an input.
- **NOT FOUND** — searched for, not confirmed.

The reading was done by a same-model helper; it is a citation check, not refereeing. A
READ-AT-SOURCE grade says the statement is in the source, not that its proof was checked.

## Frozen source and internal results

- Frozen four-pole source, zero seed, completed point `π/16`: unchanged from
  `docs/PI_FRONTIER_CONTRACT.md` and `provenance/IMPORT_MANIFEST.json` (not modified by this round).
- `research/2026-11-11/innovation_arithmetic_decoupling/` (IAD-01…09, SWT-00…06, ZSC-01…07): the
  parent dossier, repaired again in this round after a second independent re-audit (see
  VALIDATION.md).
- `docs/PI_NORMALITY_FRONTIER.md` §4–§5 (Main XXIV): the canonical target `W_(N,h)`, the Basel shell
  quantity `B_A(h)`, the sixteen-child operator `Q = C T_*`, the defect `D` and the inequality
  `W_1 ≤ (16/15)D + endpoint term` (re-derived for shell segments in LIMIT_FACES LMF-04).

## Literature used as IMPORT

| Statement | Source | Grade | Used in |
|---|---|---|---|
| For integers `a, b, c` with `0 < |a/b| < 1`, `b ≥ 2`, `c ≥ 1` and `𝓛(ac, bc) ≠ ∅`: `|log(1 − a/b) − u/(bc)^m| ≥ (bc)^(−(Λ(a,b,c)+ε)m)` for all `u` and `m ≫ 1`, with `Λ` given by explicit formulas (1.3)–(1.6); `Λ(1, b, 1) < 2` for `|b| ≥ 12`; table values `Λ(1,2,1) = 4.622103`, `Λ(1,12,1) = 1.999208`, `Λ(1,13,1) = 1.963420` | T. Rivoal, *Convergents and irrationality measures of logarithms*, Rev. Mat. Iberoam. 23 (2007) 931–952, Theorem 1 and the table of §1 | READ-AT-SOURCE (author's PDF) | RDT-07 |
| "for all `b ≥ 2`, we only know the trivial upper bounds `ν_(e,b) ≤ μ_e = 2` and `ν_(π,b) ≤ μ_π ≤ 8.1`" (`ν = 1 + v_b`); `B_n(x) ≥ log n / log(μ_x + ε) + O(1)` for the number of 1-bits | T. Rivoal, *On the bits counting function of real numbers*, J. Aust. Math. Soc. 85 (2008) 95–111, §7 and eq. (1) | READ-AT-SOURCE | frontier analysis (status of `v_b(π)`) |
| `|α − a/b| < c/b²`, `gcd(a,b) = 1` ⟹ `(a,b) = (r p_(m+1) ± s p_m, r q_(m+1) ± s q_m)` with nonnegative `r, s`, `rs < 2c` | A. Dujella, *Continued fractions and RSA with small secret exponent*, Tatra Mt. Math. Publ. 29 (2004) 101–112, Theorem 1 (arXiv cs/0402052); after R. T. Worley, J. Austral. Math. Soc. Ser. A 31 (1981) 202–206 | Dujella READ-AT-SOURCE; Worley SECONDARY | RDT-03 (sharp constant only; a self-contained weaker form is proved locally) |
| For an irrational algebraic `α`, every `ε > 0`, every integer `b ≥ 2`: `|b^m α − u| ≫_(ε,b) b^(−εm)` (ineffective) | D. Ridout, Mathematika 4 (1957) 125–131, as quoted in Rivoal 2007 §1 and Rivoal 2008 | SECONDARY (original not read) | calibration: `v_b = 0` and L2 for algebraic irrationals |
| For an algebraic irrational `ξ` of degree `d`: `nbdc(n, ξ, b) ≥ c_1 (log n)^(3/2) (log log n)^(−1/2) (log 6d)^(−1/2)` for `n ≥ c_2(ξ, b)` | Y. Bugeaud, J.-H. Evertse, *On two notions of complexity of algebraic numbers*, Acta Arith. 133 (2008) 221–250, Theorem 3.1 | READ-AT-SOURCE | calibration |
| For `y` algebraic of degree `D > 1` the number of 1-bits among the first `N` binary digits exceeds `C N^(1/D)` for large `N` | D. H. Bailey, J. M. Borwein, R. E. Crandall, C. Pomerance, J. Théor. Nombres Bordeaux 16 (2004) 487–518 | abstract READ-AT-SOURCE; the constant only SECONDARY | calibration |
| If `μ(ξ) = 2` then `p(n, ξ, b) − n → ∞`; does not cover π (Remark 6) | B. Adamczewski, Math. Ann. 346 (2010) 107–116, Theorem 1 | READ-AT-SOURCE (arXiv 1205.0961) | frontier analysis |
| `liminf p(n,ξ,b)/n ≥ 1 + (1 − 2μ(μ−1)(μ−2))/(μ³(μ−1))`, nontrivial only for `2 ≤ μ < 2.1914…`; `e`: `liminf ≥ 9/8` | Y. Bugeaud, D. H. Kim, Ann. Sc. Norm. Super. Pisa (5) 17 (2017) 931–947, Theorems 1.4, 1.5 | READ-AT-SOURCE | frontier analysis |
| `μ(ξ) < 5/3 + 4√10/15 = 2.5099…` ⟹ `p(n, ξ, b) − n → ∞`, sharp | Y. Bugeaud, D. H. Kim, Trans. Amer. Math. Soc. 371 (2019) 3281–3308, Theorem 4.6 | READ-AT-SOURCE (arXiv 1510.00279v3) | frontier analysis |
| For multiplicatively independent `r, s` and every irrational `ξ`: `p(n,ξ,r) + p(n,ξ,s) − 2n → ∞` | Y. Bugeaud, D. H. Kim, Ann. Inst. Fourier 67 (2017) 2225–2235, Theorem 1.3 | READ-AT-SOURCE | frontier analysis (the one unconditional two-base statement that applies to π) |
| If the denominators of three consecutive convergents are, for infinitely many indices, divisible only by a fixed finite set of primes, the number is a Liouville number. (Not true for every irrational.) | P. Erdős, K. Mahler, J. London Math. Soc. 14 (1939) 12–18, Theorem 2 | READ-AT-SOURCE (scan) | RDT-03 remark |
| `‖(3/2)^k‖ > 0.5803^k` for `k ≥ K` effective (Habsieger: `0.5770^k`; Dubickas: `0.5769^k`; Beukers: `2^(−0.9k)`) | W. Zudilin, J. Théor. Nombres Bordeaux 19 (2007) 311–323, Theorem 1 and historical overview | Zudilin READ-AT-SOURCE; the earlier ones SECONDARY | disposal of the misattributed "0.79" (below) |
| `μ(π) ≤ 7.103205334137…` | D. Zeilberger, W. Zudilin, Moscow J. Comb. Number Theory 9 (2020) 407–419 (arXiv 1912.06345) | READ-AT-SOURCE | `v_16(π) ≤ 6.1033` |
| `μ(log 2) < 3.57455391` | R. Marcovecchio, Acta Arith. 139 (2009) 147–184, Theorem 1.1 | READ-AT-SOURCE | comparison in RDT-05 |
| `|π − p/q| > q^(−42)` for positive integers `p`, `q ≥ 2` | K. Mahler, Indag. Math. 15 (1953) 30–42, Theorem 1 | READ-AT-SOURCE (reprint) | ZSC-04 (unchanged) |
| Hypothesis A; "`({b^n α})` has a finite attractor iff `α` is rational"; rational ⟺ periodic attractor for `Σ p(k)/(b^k q(k))` | D. H. Bailey, R. E. Crandall, Experiment. Math. 10 (2001) 175–190 | READ-AT-SOURCE (author preprint) | frontier analysis |
| Baker's theorem (qualitative and the 1975 quantitative form `|Λ| ≥ (eB)^(−C)`) | via J.-H. Evertse's lecture notes; Baker–Wüstholz 1993 covers only homogeneous forms with integer coefficients | SECONDARY (originals not read; dependence of `C` on the degrees of the coefficients unresolved) | ZSC-06(e) (qualitative form only). **Still not read at source.** |

## Corrections of earlier recollections

- **"Rhin 1987: `‖2^k log 2‖ ≥ 2^(−0.79k)`" was a false recollection** (recorded as unconfirmed in
  the previous round's NEXT.md). The exponent `0.79` belongs to `‖(3/2)^k‖` (`0.5770 = 2^(−0.79336)`,
  Habsieger; Dubickas). Rhin's 1987 paper is, by its zbMATH review (SECONDARY, paraphrased), about
  unrestricted measures (`μ(log 2) ≤ 4.076…` and others). No published bound `‖2^k log 2‖ ≥ 2^(−ck)`
  with `c < μ(log 2) − 1` was found; Rivoal 2007 gives `c = 3.622103` for `log 2` and says so.
- The previous round's CARRY_FLUX (ZSC-04, comparison paragraph) said that L2 and L3 are open for
  algebraic numbers as well. L2 holds there by Ridout's theorem (re-audit finding); corrected in
  CARRY_FLUX.

## Unrefereed 2026 claims (CLAIMED / UNVERIFIED — not imported, not used)

- "The irrationality exponent of π is 2" (`openai/math` preprint dated 2026-09-24, Theorem 1.1,
  ineffective). Status as in the previous round: no independent kernel acceptance on record. By
  ZSC-01 its truth would give `v_16(π) ≤ 1 + ε` and no saving; by Bugeaud–Kim 2017 Theorem 1.4 it
  would give `liminf p(n, π, b)/n ≥ 9/8` (a conditional remark, not a claim of this dossier).
- A self-published note claiming `μ(log α) = 2` for positive rational `α ≠ 1` (about October 2026,
  pseudonymous author). Unreviewed.
- Y. Bai, arXiv:2609.11276, claiming `μ(π) ≤ 7.101862832357`. Unreviewed.

## Not found / not verified

- Any restricted bound for `log 2` at powers of two in the literature below `μ − 1`. RDT-05 of this
  round derives one from a tilted Legendre family; Rivoal 2007 §7 suggests that such a refinement
  should exist. **No novelty is claimed**, and the literature search is not exhaustive.
- A statement in the literature that positive density of digit changes is unknown for every
  algebraic irrational and every classical constant. The absence is an absence of evidence in what
  was read, not a sourced fact.
- The digit-change bound `nbdc(n, π, b) ≫ log n` as a published statement for π (it follows from
  Rivoal 2008's mechanism and is ZSC-04 here).
- Ridout 1957, Worley 1981, Beukers 1981, Dubickas 1990, Habsieger 2003, Salikhov 2008, Baker 1975
  and Baker–Wüstholz 1993 at source; Bugeaud's 2012 book.
