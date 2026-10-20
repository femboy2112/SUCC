# Primitive ABC-triple ris-moments: a $t<1/2$ bound and a pointwise non-uniformity obstruction

**Date:** 2026-10-19. **Track:** independent SUCC arithmetic (Moonshot D, Academic Main V Thinker-Dome); separate from the completed-Weil / RH signed-Schur program.
**Branch:** `research/amv-moonshot-d-abc-moment-2026-10-19`, based on SUCC `main` at `455600a2e013895c36238a3a97e0f470fd7ba197`.
**Code:** `observational_succ/abc_triple_moment.py`, `tests/test_abc_triple_moment.py`.
**Base studied:** `observational_succ/abc_clock_families.py` (ris, `ABCTriple`, the `ris^θ` Dirichlet-convolution lemma **ABC-CLK-02**, the `X^(8/5−…)` baseline **ABC-CLK-03**, conditional-Haar **ABC-CLK-01/09**).
**Firewall:** **ABC OPEN. RH PROVED: NO.** No new exceptional-set exponent, no competitive abc result, no Weil-sign claim. Exact (integer/`Fraction`) only; no float is used as a certificate.

## 0. Domain, objects, definitions, quantifiers

A **primitive triple** `(a,b,c)` has `a,b>0`, `a+b=c`, `gcd(a,b)=1`; this forces pairwise coprimality, hence
`rad(abc)=rad(a)rad(b)rad(c)` and the exact identity

$$\operatorname{ris}(abc)=\frac{abc}{\operatorname{rad}(abc)}=\operatorname{ris}(a)\operatorname{ris}(b)\operatorname{ris}(c),\qquad \operatorname{ris}(n)=n/\operatorname{rad}(n).$$

For a real parameter `t ≥ 0` the object of study is the **ordered** primitive joint ris-moment

$$S_t(X)\ :=\ \sum_{\substack{a+b=c\le X,\ a,b>0\\ \gcd(a,b)=1}}\operatorname{ris}(abc)^t ,$$

where the index set `a+b=c, a,b>0` is read literally: for each `c` we run `a=1,…,c−1`, `b=c−a`. Each unordered pair is counted twice except the diagonal `(1,1,2)`; the number of ordered terms is `Σ_{c≤X} φ(c) ~ (3/π²)X² = Θ(X²)`. (`ordered=False` gives the unordered `a≤b` variant; every statement below holds verbatim for it, halving the constant.)

The central question (posed as OPEN in `ABC_CLOCK_GREEN_TAO.md` §5 for `t∈[1/3,1)`):

$$\textbf{(Q)}\qquad S_t(X)\ \le\ C_t\,X^2\quad\text{uniformly in }X\ge2,\ \text{for a nontrivial }t>1/3?$$

We study it at **`t = 2/5`**.

**Exactness note (AGENTS.md item 8).** For rational `t=p/q` with `q>1`, `ris(n)^t` is an irrational `q`-th root, so `S_t(X)` is generally irrational. The exact code objects are: the integer **ris-spectrum** `{R : #triples with ris(abc)=R}`; integer moments `S_0, S_1, …`; and **certified rational two-sided enclosures** `[lo, hi] ∋ S_t(X)` built from exact integer `q`-th-root brackets (sound interval arithmetic). No float is a certificate anywhere.

## 1. Partial theorem (PROVED LOCAL) — the bound holds for all `t<1/2`, in particular `t=2/5`

> **Theorem ABC-TMB-01 (coprime ris-moment bound, `t<1/2`).** For every rational `t` with `0 ≤ t < 1/2` and every `X ≥ 2`,
> $$\boxed{\,S_t(X)\ \le\ M(t)\,M(2t)\,X^2\,}$$
> where `M(θ)=∏_p (1 + (p^θ−1)/(p²(1−p^{θ−1})))` is the **ABC-CLK-02** `ris^θ` moment constant, finite for `θ<1`.

**Proof.** Group by the top: `S_t(X)=Σ_{c≤X} ris(c)^t · I(c)` with the inner additive correlation
`I(c)=Σ_{a=1}^{c−1},\ \gcd(a,c)=1} ris(a)^t ris(c−a)^t`. Dropping the coprimality constraint only enlarges a nonnegative sum, so `I(c) ≤ Σ_{a=1}^{c−1} ris(a)^t ris(c−a)^t`. By **Cauchy–Schwarz**,

$$I(c)\ \le\ \Big(\sum_{a<c}\operatorname{ris}(a)^{2t}\Big)^{1/2}\Big(\sum_{a<c}\operatorname{ris}(c-a)^{2t}\Big)^{1/2}=\sum_{n<c}\operatorname{ris}(n)^{2t}\ \le\ M(2t)\,c,$$

the last step being **ABC-CLK-02 at exponent `θ=2t`** (requires `2t<1`). Therefore

$$S_t(X)\ \le\ M(2t)\sum_{c\le X} c\,\operatorname{ris}(c)^t\ \le\ M(2t)\,X\sum_{c\le X}\operatorname{ris}(c)^t\ \le\ M(2t)\,X\cdot M(t)\,X\ =\ M(t)M(2t)\,X^2,$$

the last step being **ABC-CLK-02 at exponent `θ=t`** (requires `t<1`). The **binding** constraint is `2t<1`, i.e. `t<1/2`. Since `2/5<1/2`, the bound holds at `t=2/5`. ∎

**Exact exponent algebra, and where uniformity fails.** Any Hölder split of the inner correlation into two `ris`-moments uses conjugate exponents `r,r'` with `1/r+1/r'=1` and needs `t·r<1`, `t·r'<1`; the symmetric Cauchy–Schwarz choice `r=r'=2` minimises `max(r,r')=2`, forcing `2t<1`. So **`t<1/2` is the exact ceiling of this method.** At `t≥1/2` the Euler factor `1/(1−p^{2t−1})` in `M(2t)` diverges (`2t−1≥0`): there is **no finite constant** — the route is not merely unproven, it **cannot be uniform**. The prior three-fold Hölder route (`abc_clock_families` §2/§5, `ris(abc)^t=ris(a)^t ris(b)^t ris(c)^t` then Hölder-3) needs `3t<1`, i.e. `t<1/3`; **this Cauchy–Schwarz route strictly improves `1/3 → 1/2`** and settles the `t=2/5` instance of **(Q)**.

**Status:** **PROVED LOCAL** (elementary; `M(t),M(2t)` finite by ABC-CLK-02). Registered additively as **ABC-TMB-01**; no historical ABC-CLK ID is renamed.

### Explicit rational constant (ABC-TMB-02)

`S_t_constant_upper(t)` returns an exact `Fraction` `C_t ≥ M(t)M(2t)` for `t<1/2`, via per-prime rational upper bounds on each Euler factor (exact `q`-th-root brackets), a finite product rounded up onto a fixed grid, and a rigorous rational tail `∏_{p>P}(1+a_p) ≤ 1/(1−τ)` with `τ ≥ Σ_{p>P} a_p` and `τ<1` (cutoff `P` auto-selected). For `t=2/5`:

```
M_up(2/5) = 3906171083714215030810897 / 2102697918200000000000000  ≈ 1.8576948   (true M(2/5) ≈ 1.6744)
M_up(4/5) ≈ 92.252                                                              (true M(4/5) ≈ 18.903)
C_{2/5}   = M_up(2/5)·M_up(4/5) ≈ 171.376
```

This constant is **honestly non-optimal** (the `4/5` tail bound is loose because `4/5` is close to the convergence edge `1`); it is a rigorous *upper* bound, not a sharp constant. The empirical ratio (below) is `≈0.69` at `X=256`, two orders of magnitude under `C_{2/5}`. **Status: PROVED LOCAL** (rigorous rational upper bound). `S_t_constant_upper` **raises** for `t≥1/2`, which is exactly the method wall.

## 2. Exact finite evidence (TESTED MODEL) — census is evidence, not proof

Exact ordered primitive-triple census, `t=2/5`, certified rational enclosure of `S_{2/5}(X)/X²` (head of `growth_table`):

| `X` | primitive triples (ordered) | `S_{2/5}(X)/X²` (certified `[lo,hi]`) |
| ---: | ---: | --- |
| 8   | 21     | `0.40439768…` |
| 16  | 79     | `0.45487196…` |
| 32  | 323    | `0.56611585…` |
| 64  | 1259   | `0.58933570…` |
| 128 | 5021   | `0.65938677…` |
| 256 | 19947  | `0.69294483…` |

(Each enclosure width is `< count/10⁹`; e.g. at `X=256` the bracket is `[0.6929448377901611, 0.6929448380945282]`.) The ratio rises slowly with shrinking increments, consistent with convergence to a finite limit `≤ C_{2/5}`; it is nowhere near the `X²` bound's constant.

**This finite census is EVIDENCE, not a proof of a uniform bound.** A finite exact enumeration cannot certify an all-`X` inequality (AGENTS.md items 4, 5, 8). The *proof* of uniformity for `t=2/5` is Theorem ABC-TMB-01, independent of the table; the table only witnesses that the constant is modest.

## 3. Obstruction (PROVED LOCAL) — no uniform *pointwise* moment bound; deep prime powers

> **Obstruction ABC-TMB-03.** There is no uniform *termwise* (pointwise) moment bound: `sup{ris(abc) : primitive, c≤X} → ∞`. Hence any proof of `S_t(X)=O(X²)` **must** rely on sparsity/averaging, never on a per-triple bound; and the naive "treat `ris(a),ris(b),ris(c)` as independent `O(1)` factors" heuristic is **false pointwise**.

**Explicit hostile family (deep prime power / extreme imbalance), computed exactly.** The dyadic tower `(1,\,2^k−1,\,2^k)` is primitive (`gcd(1,·)=1`) with `ris(2^k)=2^{k−1}`, so `ris(abc) ≥ 2^{k−1}=c/2 → ∞`:

```
k=1  c=2     b=1     ris_abc=1
k=2  c=4     b=3     ris_abc=2
k=3  c=8     b=7     ris_abc=4
k=4  c=16    b=15    ris_abc=8
k=5  c=32    b=31    ris_abc=16
k=6  c=64    b=63=3²·7   ris_abc=96      (ris(63)=3 lifts the term)
k=7  c=128   b=127   ris_abc=64
k=8  c=256   b=255   ris_abc=128
k=9  c=512   b=511   ris_abc=256
k=10 c=1024  b=1023  ris_abc=512
```

A single term `ris(abc)^t ≥ (c/2)^t` is **unbounded in `k`** — no uniform termwise bound exists. Even richer: the exact pointwise maximiser of `ris(abc)` for `c≤128` is `(32,49,81)=(2^5,7^2,3^4)`, `ris=16·7·27=3024`; for `c≤600` it is `(169,343,512)=(13^2,7^3,2^9)`, `ris=13·49·256=163072` — **all three slots** simultaneously deep prime powers.

**Honest boundary (why this is an obstruction, not a counterexample).** The tower's *total* contribution is `o(X²)`: exactly,

```
Σ over tower (1,2^k−1,2^k), c≤1024, of ris(abc)^{2/5}  ∈  […, 49.1546…]   while X²=1048576,
```

ratio `≈ 4.7×10⁻⁵`, and `power_tower_contribution_enclosure` shows this ratio *shrinks* as `X` grows (`4096²` gives a strictly smaller ratio, `< 10⁻³`). So the deep-prime-power family does **not** refute `S_{2/5}(X)=O(X²)` — Theorem ABC-TMB-01 proves that bound. What it refutes is **pointwise/termwise uniformity** and the independence heuristic. This is the precise sense in which a *naive* moment bound cannot be uniform: the per-triple quantity is unbounded, and the `X²` bound survives only through averaging, exactly as ABC-TMB-01's Cauchy–Schwarz + ABC-CLK-02 structure requires.

**Moving-modulus note.** The exact finite Fourier projector `modular_additive_count`/`residue_clock_indicator` (`abc_clock_families`, ABC-CLK-13) handles `a+b≡0 (mod m)` at a *fixed* modulus with the anti-alias guard `m > max(max A+max B, max C)`. A *growing-modulus* linear-forms estimate — the analytic ingredient that would be needed to push past `t=1/2` — is **not** supplied here (see §5).

## 4. Quantitative comparison with the published 2026 benchmark

The elementary exceptional-set exponent **ABC-CLK-03**, `N_ε(X)=O(X^{8/5−ε/[5(1+ε)]+η})`, and this moment program are **strictly inferior baselines**, not competitive results. The 2026 paper

> C. Bernert, T. Browning, J. D. Lichtman, J. Teräväinen, *Bounds on the exceptional set in the abc conjecture*, <https://arxiv.org/html/2410.12234>

proves (Thm 1.3) `N_λ(X) ≪_{λ,δ} X^{3/5+δ}` for `0<λ<1`, and (Thm 1.2) `X^{(23λ+3)/40+δ}` for `0<λ≤2`. Our `ε>0` exceptional condition is `λ=1/(1+ε)<1`, so **their `X^{3/5+δ}` vastly outperforms** the `8/5` baseline. Their prime-power anatomy (Lemma 2.2) plus Fourier/geometry-of-numbers machinery is **prior external research**. **We make no novelty, priority, or best-known claim.** This is the same verdict already recorded as **ABC-CLK-12 REFUTED** (priority) in `docs/CLAIM_INDEX.md`; ABC-TMB-01 is an *interior-`t` moment* statement, a different and smaller target than BBLT's exceptional-set exponent, and does not approach it.

## 5. Firewall, caveats, and the exact open obligation

**Local-independence is NOT global-independence.** ABC-CLK-01/09 give conditional `p`-adic Haar clock laws and a profinite Gibbs threshold `E H_{loc}^s<∞ ⟺ s<1` — statements in a declared *profinite probability model* for a *fixed finite* set of primes. They are **not** independence assertions for `ris(a),ris(b),ris(c)` of actual integer triples in a bounded box. ABC-TMB-03's exact maximisers (all three slots deep powers at once) are a concrete witness that integer triples are correlated in a way the local product model does not see. Nothing here promotes local independence to global independence over integer triples.

**No Weil / RH leakage.** ABC-TMB-01 is an elementary density-type `O(X²)` moment bound. It does **not** identify with the signed completed Weil distribution, does not establish positivity, and does not bear on RH (cf. ABC-CLK-08 REFUTED-as-inference). ABC and RH remain **OPEN**.

**Exact open obligation (ABC-TMB-04, OPEN).** Decide **(Q)** in the regime `1/2 ≤ t < 1`:

$$\textbf{OPEN:}\qquad \exists\,C_t<\infty:\ S_t(X)\le C_t X^2\ \ \forall X,\quad\text{for some (or every) }t\in[1/2,1)?$$

The Cauchy–Schwarz route provably **cannot** reach it (`2t≥1 ⟹ M(2t)=∞`). A positive answer needs a genuinely new ingredient — a growing-modulus / moving-prime-support correlation estimate with a uniform high-`ris` tail (the BBLT-style Fourier/geometry savings), **not** obtainable from fixed-modulus CRT or the finite census. A negative answer needs an explicit family of primitive triples whose exact contribution is `ω(X²)`; the deep-prime-power families of §3 are `o(X²)`, so they do not suffice and the question stays open. **Next verdict-changing probe:** a rigorous upper bound on the second additive correlation `Σ_c (Σ_{a<c} ris(a)^{1/2} ris(c−a)^{1/2})` at the edge `t=1/2`, or a sieve/geometry majorant for the balanced high-`ris` stratum.

**Status ledger (this document).**

| ID | Claim | Status |
| --- | --- | --- |
| ABC-TMB-01 | `S_t(X) ≤ M(t)M(2t)X²` for all `0≤t<1/2` (incl. `t=2/5`); Cauchy–Schwarz + ABC-CLK-02; binding `2t<1` | **PROVED LOCAL** |
| ABC-TMB-02 | Explicit rational `C_t ≥ M(t)M(2t)` (non-optimal); `C_{2/5}≈171.38` | **PROVED LOCAL** |
| ABC-TMB-03 | No uniform *pointwise* moment bound; `sup ris(abc)→∞`; deep-prime-power families are `o(X²)` (obstruction, not counterexample) | **PROVED LOCAL** |
| — | Exact `S_{2/5}(X)/X²` census, `X≤256` | **TESTED MODEL** |
| — | Elementary `8/5` baseline competitive with BBLT `3/5+ε` | **REFUTED** (= ABC-CLK-12) |
| ABC-TMB-04 | `S_t(X)=O(X²)` for some/every `t∈[1/2,1)` | **OPEN** |

Claim IDs registered additively under the fresh prefix **ABC-TMB** to avoid any auto-census collision with ABC-CLK; no historical ID renamed. `IMPORT_MANIFEST.json`, frozen dossiers, and archival originals are untouched. YEAN is untouched; no Lean was run for this work (formalization debt noted).
