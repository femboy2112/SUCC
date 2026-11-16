# Principia Observatoris × π Frontier — What the BBP seed actually is

**Research note, 2026-11-14.** **Source:** review of the authentic SUCC zero-seeded four-pole carrier, its exact rational compiler, source moduli and the author's question whether the coherent anti-π counterseed even belongs to the carrier's admissible source. **Verdict:** the counterseed is a valid *solution of an enlarged symbolic recurrence*, but not an admissible initial condition of the original proper rational BBP source. The rational-affine seed module admits a much sharper *singular-locus* classification for base-16 normality. These are source-typing and classical normality-equivalence results, **not a π normality proof**.

## 1. Three different levels of seed admissibility

Let

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
P_n=\sum_{j=1}^n16^{-j}r(j),\quad x=\sum_{j\ge1}16^{-j}r(j)=\pi/16.
\]

1. **Authenticated single source / selected root:** `r` as written, exact unwrapped `U_0=0`, `U_n=16 U_{n-1}+r(n)=16^n P_n∈Q`. The source *constructs* its rational finite states from the empty prefix; seed zero is part of its mathematical passport. The completed point is `x` and no free homogeneous term exists in the selected source.
2. **Broader rational-seed finite-carrier family:** same forcing and any fixed `s∈Q` gives `U_n(s)=16^n(P_n+s)∈Q`, but **not the selected source** unless `s=0`. The completed point is `x+s`. This is a different realization, not a gauge transformation of the fixed pair `(r,0)`.
3. **Completed symbolic seed module:** `M=Q+Qx`, coordinates `s=a+bx` with `a,b∈Q` and unique coordinates by the imported irrationality of `π`. The coherent counterseed `s=-x` is `(a,b)=(0,-1)`. It can be written as a finite symbolic expression and is a *computable real*, but is not rational and cannot be represented as an **exact rational finite state**. Calling it "impossible to prepare in principle" would be unjustified; it is simply outside the declared finite-carrier and proper-rational-source contracts.

For all `s` the recurrence identity is

\[
U_n(s)=16^n(P_n+s),\qquad T_n=16^n(x-P_n),\qquad
U_n(s)+T_n=16^n(x+s),\qquad Z_n(s)=16^{-n}U_n(s)-P_n=s.
\]

For `s=-x`, `U_n(-x)=-T_n` is irrational at **every finite n** (as `x` irrational and `P_n` rational), and the entire completion vanishes. Its initial state encodes the exact negative analytic source completion. This is a source-tuned *anticipatory boundary condition*: it cancels the mathematical series that the origin-locked recurrence is intended to accumulate. It cannot be authenticated by the zero-origin certificate. It is still a legitimate mathematical hostile control for any proposed theorem that **forgets the seed and claims validity for all real solutions**.

## 2. Exact rank collapse in the symbolic seed module (CLASSICAL + PROVED ALGEBRA)

**Theorem SRC-01 (rank-locus classification).** For `s=a+bx∈M`,
\[
\xi(s):=x+s=a+(1+b)x.
\]
Write `N_16(ξ)` for normality in base 16. Then the classical **Wall theorem** (normality is preserved under translation by rationals and multiplication by nonzero rationals) gives:
\[
\boxed{b\ne-1\Longrightarrow N_{16}(\xi(s))\iff N_{16}(x),
\qquad b=-1\Longrightarrow \xi(s)=a\in\mathbb Q\text{ is nonnormal}.}
\]
**Proof:** The affine map `y↦(1+b)y+a` is invertible with rational inverse iff `1+b≠0`. Wall's normality theorem applies to the map and to its inverse. When `1+b=0`, the completed value is rational, with an eventually periodic digit expansion, never normal. □

**References:** [Wall's theorem, quoted in *Descriptive Complexity in Cantor Series*, Theorem 1.3](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/descriptive-complexity-in-cantor-series/19EAD3B2B426D3826A9405DFB7D81); classical [Wall normality/Weyl characterization](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/19EAD3B2B426D3826A9405DFB7D81/S0022481221000773a.pdf/descriptive-complexity-in-cantor-series.pdf). The claim imports the classical result; finite tests below only check the affine coefficient algebra and exact source identities. No academic priority for rational-normality invariance is claimed.

The exceptional set is **exactly** the affine hyperplane `b=-1`. For example:

| Seed `s` | Completed number `ξ=x+s` | Rational finite state? | Normality relation |
|---|---|---|---|
| `0` | `x` | Yes, authenticated | Open for π |
| `1/16` | `x+1/16` | Yes, wrong origin | Equivalent to π; phases agree for `n>=1` |
| `-P_N` for fixed `N` | `x-P_N` | Yes, wrong origin | Equivalent to π (for fixed N) |
| `x` | `2x` | No (symbolic completion) | Equivalent to π |
| `a-x` | rational `a` | No (symbolic completion) | Unconditionally nonnormal |

**Interpretation:** the counterseed does not demonstrate a generic failure of normality among rational source-preserving seed modifications. It **annihilates the nonzero coefficient carrying the source's completed transcendental point**. The rational affine group `Q^× ⋉ Q` acts by normality-preserving transformations; setting the slope to zero is a *noninvertible degeneration*, not a member of that group. Do not identify this normality-preserving action with an authenticated physical/source gauge: the completed number changes, and the original finite states, integer carries and other targets need not be preserved.

**Important limitation:** the weak R0 shell condition is **not** identical to normality and need not be invariant under all rational-affine transformations. The `b=-1` locus gives rational nonnormal completed values, but some rational periodic orbits can pass R0 while failing normality. The classification above is for **full base-16 normality**, not every rung of SUCC's frontier.

## 3. The actual source gauge is a paired forcing/seed transformation (CLASSICAL SUCC IMPORT)

Source moduli ZSC-06, in [CARRY_FLUX.md](../../2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md), provide a more important answer to "what is the seed with respect to the carrier?". A rational polynomial source is a pair `(g,s)∈Q[z]×Q`, with
\[
r_g(n)=\int_0^1 z^{8n-8}g(z)dz,\quad G(z)=\frac{g(z)}{16-z^8},\quad
\xi(g,s)=s+\int_0^1G(z)dz.
\]
The authentic proper source has
\[
g_\pi(z)=4-2z^3-z^4-z^5=(1-z)(z^2+2)(z^2+2z+2),\qquad s=0.
\]
For any **rational polynomial** `h`, set `a_h(n)=∫_0^1z^{8n}h(z)dz` and transform
\[
\boxed{(g,s)\mapsto\bigl(g-(16-z^8)h,\;s+\int_0^1h\bigr).}
\]
Then
\[
U'_n=U_n+a_h(n),\quad T'_n=T_n-a_h(n),\quad \xi'=\xi,
\]
so this is an actual **source-representation gauge**, unlike a seed-only shift with forcing fixed. The source integrand compensates the moved initial contribution. Both seeds remain rational. In general the literal finite carries, poles and seams are **not** invariant, although completed π-normality is.

The proper form `deg g≤7` is the **unique representative of each gauge class** by polynomial division by `16-z^8`, so `s` is a meaningful invariant *in that normalized source representation*. The authentic `(g_π,0)` is proper. An alleged `s=-x` with unchanged `g_π` is **neither** proper rational-source data **nor** in the rational-polynomial gauge orbit of `(g_π,0)`; it changes the completed point from `x` to zero.

**The independent hostile source is not gone:** SUCC ZSC-06 also constructs a **different** proper zero-seeded rational polynomial `g_0=8-8z-4z²-8z³-2z⁴-2z⁵+z⁶` with completed point zero. This genuine *broader-source* counterexample shows that zero seed and properness **alone** do not imply normality. It is excluded from the genuine four-pole source by the source polynomial, and additionally fails `g≥0` and `g(1)=0`/`r_g(n)=O(n^-2)` conditions that the actual positive BBP integrand satisfies. The source-to-period rigidity via Baker quoted in ZSC-06(e) is an imported theorem and is not independently audited here.

This matters: **the right proof domain is the authenticated original `(g_π,0)` or another carefully stated source class that excludes actual hostile sources for mathematical reasons**. Removing `s=-x` from that domain is valid; removing every adversary merely because it is inconvenient is not.

## 4. Finite rational shadow: the obstruction that survives in the larger rational seed family (PROVED)

For each integer horizon `N≥1`, precompute the rational **wrong seed** `s_N=-P_N` using the first `N` original forcing values. Then for all `0≤n≤N`,
\[
\boxed{U_n(s_N)=-\sum_{j=n+1}^N16^{n-j}r(j),\qquad U_N(s_N)=0.}
\]
Since `r(j)` is positive and decreasing,
\[
-\frac{r(n+1)}{15}<U_n(s_N)\le0\quad(0\le n\le N).
\]
In particular, choose `N=2B` and consider the shell `B≤n<2B`. For every fixed integer mode `h`, `\cos\theta≥1-\theta²/2` implies
\[
\boxed{\operatorname{Re}\frac1B\sum_{n=B}^{2B-1}e(hU_n(s_{2B}))
\ge1-2\pi^2h^2\Big(\frac{r(B+1)}{15}\Big)^2
=1-O_h(B^{-4}).}
\]
So **no all-seed, all-shell R0 margin with onset/constant uniform across all rational seeds is possible.** The argument uses rational exact states throughout and the original four-pole forcing. The seed changes with `B`, however, so it does **not** refute any all-large-shell theorem for a **fixed** rational seed, much less for the selected origin `s=0`. Each fixed rational-seeded completed number remains rationally translated from `x`, so its *normality truth value* is precisely the same as that of π by SRC-01.

This is an instructive source/probe distinction: finite precomputed future compensation can produce arbitrarily long coherent observations without proving permanent nonnormality. It is not an alternative *unprepared canonical initial boundary*.

## 5. Corrected use of countermodels and next proof gate

**SRC-02 (REFUTED GENERAL INFERENCE):** "The nonnormal coherent seed shows that the authentic original four-pole zero-seeded source might be nonnormal, or that no theorem based on the same rational forcing can establish its normality." This does **not** follow. The counterseed is outside the canonical source and outside the proper rational source gauge, and the fixed-rational-seed family has normality *equivalent* to the original question.

**SRC-03 (RETAINED HOSTILE CONTROL):** "A proposed statement that discards the source start altogether and applies unchanged to every real seed of the same forced recurrence cannot imply uniform signed cancellation or normality." The coherent completed zero point is a decisive counterexample to *that generalization*. Finite rational shadows separately refute a **uniform-in-seed finite-onset margin** even within the rational family.

**SRC-04 (PROVED CONTRACT, NOT NORMALITY):** The original proper source `(g_π,0)` is singled out by the rational integrand, genuine four signed poles, unwrapped zero origin and exact source path. Source moduli permit gauge changes only **paired with compensating forcing changes**, keeping `ξ` fixed. The normality-preserving rational affine group on completed points is a *different* symmetry.

**NEXT falsification-grade research target:** Use the source-intrinsic positivity/factorization of `g_π=(1-z)K`, its exact zero boundary, proper representative, prime cofactor and integer carry structure to obtain a signed anti-locking inequality for the **fixed** original zero state, e.g. Main XXV R0. Show the hypotheses exclude `g_0` (source mutant), the non-rational singular affine counterseed, finite rational shadow `s_{2B}` (moving source), and shifted finite-state aliases **without** unjustifiably asserting uniformity across them. Authenticate source identity first; the missing estimate is still a genuinely asymptotic real phase inequality.

### Claims and limitations

- **CLASSICAL / PROVED ELEMENTARY IN SCOPE:** exact recurrence/seed/tail/source-gauge identities, rational-shadow identities and their `O_h(B^-4)` coherence bound; uniqueness of polynomial proper form as a gauge section.
- **CLASSICAL IMPORT:** Wall's rational-addition and nonzero-rational-multiplication normality theorem; π irrationality; authentic BBP identity and source positivity.
- **SUCC IMPORT NOT INDEPENDENTLY REPROVED:** ZSC-06 source-moduli null line, Baker-dependent global period-space rigidity.
- **OBSERVED FINITE:** exact Python Fraction tests; independent rational gauge/shadow oracle.
- **UNVERIFIED / OPEN:** base-16 normality of π, R0/R1, positive-density selected digit changes, uniform source-signed cancellation, physical interpretation of the mathematical source.

### Provenance

- [SUCC PI_FRONTIER_CONTRACT](../../../docs/PI_FRONTIER_CONTRACT.md)
- [SUCC ZI-01–03 exact seed contracts](../../2026-11-10/circle_line_lr_observer/zero_anchor_identity/THEOREMS.md)
- [SUCC ZSC-06 rational polynomial source moduli](../../2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md)
- [SUCC Main XXV source rank and R0](../../../docs/PI_NORMALITY_FRONTIER.md)
- [Original GA/GFT bridge draft](https://github.com/femboy2112/SUCC/pull/631), whose overbroad counterseed interpretation this note corrects.

No historical files, source contracts, original forcing, or main-branch mathematics are modified.
