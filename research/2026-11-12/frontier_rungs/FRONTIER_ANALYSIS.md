# The π normality frontier after the rungs round — analysis and next obligation

Round 3 (2026-11-12). **π base-16 normality, the source-selected signed estimate, (CH), R1 and R0
are OPEN.** This file is an analysis: it says where the frontier stands, which rabbit holes were
followed in this round and what each returned, and what the next obligation is. It proves nothing
itself; every mathematical statement cited has its proof, status label and falsifier in
[LIMIT_FACES.md](LIMIT_FACES.md) (LMF), [RESTRICTED_EXPONENT.md](RESTRICTED_EXPONENT.md) (RDT) or
the parent dossier's `CARRY_FLUX.md` (ZSC) and `THEOREMS.md` (IAD). Literature statements carry the
grades of [SOURCE_MAP.md](SOURCE_MAP.md).

## 1. The target, unchanged

With the frozen four-pole source, literal zero seed and `Y_n = 16^n·π/16`
(`docs/PI_NORMALITY_FRONTIER.md` §4): for every nonzero integer `h`, `W_(N,h) → 0`. Equivalently,
in the language of this round (LMF-01(e)): the only weak-* limit of the shell measures
`ν_B = B^(-1) Σ_(B≤n<2B) δ_({Y_n})` is Lebesgue measure. Write `M(ξ)` for the set of those limits; it
is a nonempty, compact, connected set of `×16`-invariant measures and depends only on the completed
point (so not on the source gauge of ZSC-06).

## 2. The ladder, bottom to top

Each rung is the statement that `M(π/16)` misses a set of invariant measures — a closed face of
the simplex for R0, (CH) and (CH_k), a union of fifteen faces for R1, a dense non-closed face for
(AM) (LMF-02, LMF-03). All implications below are proved for every real number; each is strict, with an
explicit witness.

| Rung | Digit statement | Signed statement | Excluded from `M` | Status for π |
|---|---|---|---|---|
| L1 | infinitely many digit changes | — | — | known (irrationality); explicit: runs `≤ 41n`, `≥ log_42 N − 2` changes (ZSC-04, Mahler import) |
| L2 | a change in every large shell `[B, 2B)` | — (Diophantine: endpoint exponent 1 at `15·16^m`) | — | **OPEN** |
| **R0** | positive lower shell density of **binary** digit changes | `limsup_B Re W_B(1) < 1` | `δ_0` | **OPEN** |
| R1 | — | `limsup_B |W_B(1)| < 1` | each `δ_(j/15)` | **OPEN** |
| R2 = (CH) | positive lower shell density of hexadecimal digit changes | `limsup_B Re W_B(15) < 1` | the simplex on the fixed points | **OPEN** |
| (CH_k) | positive density of `n` with `d_n ≠ d_(n+k)` | `limsup_B Re W_B(16^k − 1) < 1` | the simplex on points of period dividing `k` | **OPEN** |
| (AM) | all (CH_k) | a saving at every mode | every finitely supported measure | **OPEN** |
| (E) | — | — | every measure of zero entropy | **OPEN** |
| (N) | normality | `W_B(h) → 0` for all `h ≠ 0` | everything but Lebesgue | **OPEN** |

`(N) ⟹ (E) ⟹ (AM) ⟹ (CH_k) ⟹ (CH) ⟹ R1 ⟹ R0`, and each density rung with density `c` forces a
restricted Diophantine exponent `≤ (1−c)/(1+c) < 1` at its own denominators (ZSC-02(d), LMF-03(a)).
L2 is not on this chain below (CH): it is implied by (CH) and by a restricted exponent `< 1` at
the denominators `15·16^m`, but it neither implies nor is implied by R0 (the point `1/3 = 0.555…`
has R0 and no digit change at all; a point with one change per shell between long runs of `0` and
`F` has L2 and fails R0).

Two things changed in this table during the round.

- **The bottom signed rung is lower than (CH).** The previous round named (CH) as the weakest
  statistical statement of the signed family; the re-audit found that false, and LMF-03 identifies
  what lies below: R1 and R0. **R0 is the real part of the canonical Main XXIV target at its first
  mode**, `limsup Re W_(B,1) < 1`, and it is equivalent to an elementary statement: the binary
  digits of π change with positive lower density on shells — equivalently, π has no sparse
  alternating signed-binary representation on any large shell.
- **Each rung has a threshold in the canonical units** (LMF-04, LMF-05): for shell measures,
  `limsup W_1(ν_B, λ) < 1/4` or `limsup D(ν_B) < 1/4` implies R1 (and R0); `< 1/60` implies (CH);
  `< 1/(4(16^k − 1))` implies (CH_k). For prefix measures: `D_N < 15/256` eventually implies R1,
  `D_N < 1/256` implies (CH). Normality is `D → 0`. So the open signed statements are no longer
  "prove `o(1)`": the first of them is "keep the sixteen-child Haar defect of every late shell below
  **one quarter**". The coherent control has `D = 15/32`; a generic point has `D ≈ B^(-1/2)`; the
  holdout shells of this round read `0.003–0.006` (an instance, not evidence).

## 3. Rabbit holes followed, and what each returned

### 3.1 Restricted exponents (the WALL-16 probe of the previous round) — Outcome B

The previous round asked whether any bound `‖b^m ξ‖ ≥ b^(-cm)` with `c < 1` is proved for an
element of the period space `V`, starting from a recollection attributed to Rhin for `log 2`.

- The recollection was false: the `0.79` belongs to `‖(3/2)^k‖` (SOURCE_MAP).
- **A restricted exponent below 1 is nevertheless proved inside `V`.** Rivoal (2007, READ-AT-SOURCE)
  proves `|log(1 − 1/b) − u/b^m| ≥ b^(-(Λ+ε)m)` with `Λ(1,b,1) < 2` for `|b| ≥ 12`. The number
  `ξ_* = log(16/15) = Σ_(n≥1) 16^(-n)/n` is the proper zero-seeded source with the single pole `8n`,
  a nonzero element of `V`, and `Λ(1,16,1) = 1.8813` (evaluated from his formula): `v_16(ξ_*) ≤ 0.8813`.
  RDT-07 extends the bound to the denominators `15·16^m` and `2^M` and concludes **L2 for `ξ_*`**:
  which places `ξ_*` on rung L2 of the ladder. (CH) for `ξ_*` is OPEN.
- **What a restricted gain is** (RDT-01, RDT-02): from a linear form `Aξ − B = I`, the bound at
  denominators `g·b^m` beats the unrestricted bound from the same form by exactly the `b`-adic
  imbalance `∏_(p|b) p^((v_p(A) − v_p(B))^+)` (for `m` beyond an explicit `m_0`). A single form
  whose integer-normalised error is `≥ 1` is silent at every `m`, however large its imbalance; the
  asymptotic criterion needs the classical `α > δ`. Partial sums of a BBP-type series do not
  certify their own digits, in any base (RDT-04).
- **`log 2`** (RDT-05): a tilted Legendre family has the imbalance `2^((b−c)n)` and, with the usual
  prime savings, gives `v_2(log 2) ≤ 2.3814`, below the unrestricted record `μ − 1 = 2.5746` and far
  above 1. No novelty is claimed.
- **π** (RDT-06, RDT-08): in the convergent one-pole Gaussian families the imbalance falls on the
  constant term (a 2-adic shadow: `log_2(i) = 0`), so they bound `‖2^m/π‖` and give for π exactly
  the unrestricted exponent (OBSERVED on seven families; the bound for `1/π` is CONDITIONAL). Any
  `x` for which the argument of `1 − x` is a nonzero multiple of `π/4` — as it must be for
  `x ∈ Q(i)` — has modulus `≥ 2^(-1/2)`, with equality exactly at the BBP point `(1 ± i)/2`: the
  effective base of the π-line is `√2`, against `≥ 12` needed by the import.
- **Verdict.** The mechanism that pays the Diophantine cost inside `V` uses a non-unit at the prime
  2 in the argument of a real logarithm close to 1, and a large effective base. The π-line has
  neither. Not claimed: that `v_16(π) < 1` is false or unprovable. `v_16(π) ≤ 6.1033` remains the
  record; Rivoal 2008 states that only the trivial bound is known.

### 3.2 Is the Diophantine axis enough? — No, and the literature agrees

- ZSC-01 made `v_16 < 1` necessary for any saving. It is not sufficient: W1 of ZSC-05 has
  `v_16 = 0` and no saving; the witnesses of LMF-03 separate every rung with `v_16 = 0`.
- Calibration (SOURCE_MAP): for algebraic irrationals `v_b = 0` (Ridout, ineffective), so L2 holds,
  and still the best known count of digit changes is `(log N)^(3/2)(log log N)^(-1/2)`
  (Bugeaud–Evertse); a positive density of digit changes was not found in the literature for any
  algebraic irrational or classical constant. For π the best published statements are of order
  `log N`.
- So the open rungs R0–(N) are **medium-scale** statements: they concern runs whose length tends to
  infinity more slowly than their position, which no Diophantine exponent sees. `ξ_* = log(16/15)`
  is now the cleanest test object: an element of `V` where the Diophantine cost is paid up to
  savings `η ≤ 0.126` (and (CH) densities `c ≤ 0.063`), so that below those values only the medium
  scale remains.

### 3.3 Block complexity — a parallel ladder that does not reach π

Adamczewski (2010) and Bugeaud–Kim (2017, 2019) convert small irrationality exponents into
complexity lower bounds (`p(n) − n → ∞` below `μ = 2.5099…`; `liminf p(n)/n ≥ 9/8` at `μ = 2`).
Their thresholds are far below the proven `μ(π) ≤ 7.1032`, and Adamczewski says explicitly that π
is out of reach. The one unconditional statement that applies to π is two-base: for multiplicatively
independent `r, s`, `p(n,π,r) + p(n,π,s) − 2n → ∞` (Bugeaud–Kim 2017). Complexity counts distinct
blocks, not frequencies: a Sturmian word has positive change density and minimal complexity. The two
ladders are logically independent; nothing here imports from that one.

### 3.4 Continued fractions

RDT-03: a run of equal digits of length `L` from position `n` is a rational approximation with
denominator dividing `15·16^n` and error `≲ 16^(-L)/q`; if L2 fails at `B` then `15·16^B` (up to
a bounded factor) is a bounded combination `r q_(m+1) ± s q_m` of consecutive convergent
denominators of π (Worley–Dujella form), and runs longer than their position are convergents
followed by an explicit large partial quotient. So L2 for π would follow if such `{2,3,5}`-unit
values occurred only finitely often (the converse is not proved). Rivoal's Theorem 3 is a statement of this kind (the convergent
denominators of `log(1 − a/b)` are eventually not integral powers of `bc`, for `b` large). Erdős–Mahler
(1939) forbids three consecutive `S`-unit denominators for non-Liouville numbers; one at a time is
not excluded for π by anything known.

### 3.5 The carry and source side

No new constraint. The π-line `A_π + ρA_0` of ZSC-06 adds multiples of the null orbit to the
states and changes carries and census without changing `M`; the hostile source `g_H` stays hostile.
The exact kernel of the carry dictionary now has kernel authority (§3.6).

### 3.6 Proof authority

A Lean 4 check (pinned toolchain and mathlib, `lean/`) gives kernel authority to 33 exact statements
of the parent dossier: the ZSC-06 null relation (partial fraction, factorisation `16 − z⁸ = K·m`,
coefficient vector `A_0`, the vanishing integral), both parts of the ZSC-02 locality lemma for
every real number, and the ZSC-03 renewal lemma for the four-pole forcing with every real seed.
Nine mutated statements are refuted. Nothing statistical, Diophantine or asymptotic is
kernel-checked.

## 4. What a proof must survive now

In addition to the controls of `docs/PI_NORMALITY_FRONTIER.md` §7 and of NEXT.md in the parent
dossier:

- an argument for R0, R1 or (CH) that uses only a restricted exponent, of any size, is wrong
  (LMF-03 witnesses have `v_16 = 0`);
- an argument for R1 must fail for `ξ = 1/15` and for every point whose shells approach one fixed
  point; an argument for (CH) must fail for the two-digit run point `1^k 2^k …` (R1 holds, (CH)
  fails);
- a threshold argument must reject the coherent seed (`D = 15/32`, `W_1 = 1/2`) and must not
  confuse the fifteen fixed points of the circle with the sixteen points `j/15`, `0 ≤ j ≤ 15`, that
  shell measures approach on the interval (the error in this round's own provisional threshold);
- a restricted-exponent argument for π must explain why it does not apply to the forms of RDT-06,
  where the imbalance sits on the wrong coefficient.

## 5. The next obligation

> **R0 for π.** There are `c > 0` and `B_0` such that for every `B ≥ B_0` at least `cB` of the
> binary positions `m ∈ [4B, 8B)` satisfy `b_m ≠ b_(m+1)`. Equivalently `limsup_B Re W_(B,1) < 1`;
> equivalently `δ_0` is not a limit of shell measures; sufficient: `D(ν_B) ≤ 1/4 − ε` on all late
> shells.

It is the weakest open statement of the signed family, it is phrased in the canonical observable at
its first mode, and it is implied by every other rung. Its necessary Diophantine cost
(`‖2^m π‖ ≥ 2^(-((1−c)/(1+c))m − 4)`) is itself open, so R0 for π is beyond the present reach of
this dossier; the honest intermediate targets are:

1. **(CH) or R0 for `ξ_* = log(16/15)`.** An element of `V` where the Diophantine cost is paid
   (up to `η ≤ 0.126`). Any proof there must be a medium-scale argument, which is the missing kind. A refutation
   (an element of `V ∖ {0}` whose shells approach `δ_0`) would end the conjecture that the class
   `V` is uniformly normal.
2. **A restricted exponent for π below the unrestricted one.** By RDT-02(b) this is exactly a
   convergent family of forms `A_n π − B_n` with `v_2(A_n) − v_2(B_n) ≥ cn`; or a proof that the
   2-adic shadow of RDT-06(a) is general, which would close this route.
3. **Explicit thresholds for the import.** `m_0(g, ε)` in RDT-07 and `m_0` in RDT-05 are not
   computed; an explicit version would turn L2 for `ξ_*` into a statement with a starting index.

Falsifiers: one late shell of π with `D(ν_B) ≥ 1/4` does not refute R0 (the threshold is
sufficient, not necessary), but a sequence of shells with `Re W_(B,1) → 1` does; a counterexample to
any displayed inequality of LMF or RDT refutes that statement, not the data.
