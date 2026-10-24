# The natural-number carrier and the internal BBP machine

**Date:** 2026-10-24. **Research-only:** proposed descendant of SUCC draft #277 at `5d51f9329149cdbf0db1fce3065924c681f64de6`, inheriting #274 (`d942c4707d750f788f39acb137a04e871a93e0a6`), #273 (`8d89711db77fea81920321d32f831eed3dec1e68`) and #272 (`6e8fa8b77886b13f1f533ed8083fd88c849d14b3`). **π normality and its independence remain OPEN.** No kernel-checked Lean proof or priority/novelty claim.

## 0. Steelman: stop allowing an application to redefine its carrier

For the mathematical source of π, **the primary arithmetic carrier can be the natural-number successor** `(N,0,S)`, `S(n)=n+1`. Its chosen actual BBP history is one function of that carrier, not a putative selection over independently sampled prime histories. The BBP recurrence is an **internal computational realization**, not the ontology of the carrier. Its prime-torsion, dyadic, Pascal and circle observables are derived from that one history; the Lucas rank/support transform is a separate auxiliary combinatorial probe, not secretly identical to source residues.

This is a mathematical carrier model, **not** a claim that physical reality is literally `N`. The key object is an explicit commuting map, not a metaphor. The classical universal property of `N` supplies uniqueness of the orbit map once the pointed endomap is specified. Ordinary Gödel/Cantor encodings supply single-natural representations without any asserted computational speedup.

The earlier slogan “the primes must be in order” was incorrect: a *finite* primary decomposition in `Q/Z` does not need a prime ordering. The chronological source update matters. Prime births are an optional filtration of an observer's finite records, not a law that makes reality exist.

## 1. An entirely natural-number BBP automaton (NCB-01--04)

The original authenticated forcing is

$$
r(j)=\frac4{8j-7}-\frac2{8j-4}-\frac1{8j-3}-\frac1{8j-2}
=\frac{P(j)}{D(j)},\qquad j\ge1,
$$

$$
P(j)=120j^2-89j+16,\qquad
D(j)=(2j-1)(4j-1)(8j-7)(8j-3).
$$

Write `j=t+1`, `t>=0`. Then `P(j)=120t^2+151t+47>0`, and `D(j)` is a product of four positive odd integers, so `D(j)` is strictly positive and odd.

**A total state map on N³:** let `s=(n,a,t)` represent the rational number `a/(2t+1)`, not merely its circle residue. Set `j=n+1`, `d=2t+1`. Define

$$
\boxed{F(n,a,t)=\left(j,\;16aD(j)+dP(j),\;\frac{dD(j)-1}{2}\right).}
$$

The third component is in `N` because the product of odd numbers is odd. Thus `F:N³ -> N³` is **total**, given by primitive-recursive integer operations. If `q(s)=a/(2t+1)`, elementary fraction arithmetic gives

$$
\boxed{q(F(s))=16q(s)+r(n+1).}
$$

In particular, with `s₀=(0,0,0)`, define the source section `i(n)=F^n(s₀)`. Then

$$
\boxed{i(0)=s_0,\qquad F\circ i=i\circ S,\qquad q(i(n))=U_n.}
$$

The first coordinate of `i(n)` is `n`, so `i` is injective, and the actual state graph `i(N)` is an invariant copy of `(N,S)`. The section is unique by natural-number recursion. Neither `i` nor `F` selects among alternative π candidates; the four-pole forcing and initial zero have already determined this one orbit.

Encode `(a,b)` with the standard Cantor pairing `⟨a,b⟩=(a+b)(a+b+1)/2+b` and its integer-square-root inverse. The double code `E(n,a,t)=⟨n,⟨a,t⟩⟩` is a bijection `N³ -> N`; therefore

$$
\widehat F=E\circ F\circ E^{-1}:N\to N,
\qquad \widehat i=E\circ i,\qquad
\widehat F\circ\widehat i=\widehat i\circ S.
$$

This is an **exact single-N realization**. It is not a conjugacy between `S` and `F` on the *whole* state space, only on the authentic embedded orbit. No efficiency or π-normality follows from using one natural number to encode a triple.

### Concrete source states

| n | Raw a | Raw odd denominator d | Reduced U_n |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 |
| 1 | 47 | 15 | 47/15 |
| 2 | 1852434 | 36855 | 205826/4095 |
| 3 | 581991218235 | 723647925 | 615863723/765765 |

The automaton deliberately does **not** reduce `a/d`: retaining the integer lift avoids silently discarding the carry coordinate relevant to rational filters.

## 2. Every local observer can read the same state (NCB-05--08)

All state denominators are odd. Therefore `q(s)` lies in the localization `Z_(2)` and has a well-defined image modulo every `2^k`:

$$
\rho_{2,k}(s)=a\,d^{-1}\pmod{2^k},\qquad d=2t+1.
$$

At every `s`, the exact square commutes:

$$
\boxed{\rho_{2,k}(F(s))=
16\rho_{2,k}(s)+P(n+1)D(n+1)^{-1}\pmod{2^k}.}
$$

This is a factor of the *timestamped* state machine; there is no independent `2`-adic chronology. For each prime `p`, the usual `p`-primary homomorphism `λ_p:Q/Z->C_{p^∞}` similarly obeys

$$
\boxed{\lambda_p([q(F(s))])=
16\lambda_p([q(s)])+\lambda_p([r(n+1)]).}
$$

This holds for arbitrary source states, not just the selected graph. Evaluating these observers **along** `i(n)` makes every `p`-local history arise from one and the same `n`. The finite primary sum of `[U_n]` equals its real rational circle phase, without an imposed ordering of primes (inherited JPC-02--05).

Pascal signed differences `Δ^k U_n` are arithmetic functions of consecutive source states `i(n),...,i(n+k)`. This uses integer coefficients and therefore commutes with primary torsion projections. Lucas support and residue operators, by contrast, act on the combinatorics of natural indices `(n,k)`; their precise source bridge must be stated and proved before using them to control carry frequencies. This preserves the honest distinction established by PLQ-02 and its residue-vs-support mutant `C(2,1)=2 mod3`.

## 3. π is a limit of finite rational outputs, not a primitive state (NCB-09--12)

By induction,

$$
U_n=\sum_{j=1}^n16^{n-j}r(j),
\qquad
\alpha_n=\frac{U_n}{16^n}=\sum_{j=1}^n\frac{r(j)}{16^j}.
$$

The classical BBP identity identifies `α=lim α_n=π/16`. The identity is an **imported classical result**, not derived from the new coding. The positive source kernel gives `r(j)>0` and strict decrease in `j` (the integral `r(j)=∫_0^1 t^{8(j-1)} (4-2t³-t⁴-t⁵)dt` has a strictly positive factor on `(0,1)`). A direct **elementary polynomial bound** does not require approximating π:

$$
8D(j)-j^2P(j)
=3976t^4+7801t^3+5227t^2+1307t+73>0,\quad t=j-1.
$$

Thus `0<r(j)<8/j²` at every `j>=1`. Define the exact positive future tail

$$
T_n=\sum_{j=1}^{\infty}\frac{r(n+j)}{16^j},\qquad
0<T_n<\frac8{15(n+1)^2},\qquad
16^n\alpha=U_n+T_n.
$$

The rational enclosure

$$
L_{n,m}=\sum_{j=1}^m16^{-j}r(n+j),\quad
L_{n,m}<T_n<L_{n,m}+\frac{r(n+m+1)}{15\,16^m}
$$

is certified solely from the source and strict monotonicity. It shrinks to one point as `m -> infinity`. For fixed `n`, the hexadecimal digit of `α` at position `n` is `floor(16{U_n+T_n})`; once the two rational endpoints fall in the same floor-16 cell, that digit is certified. They must eventually do so because `16^n π/16` is irrational (classical irrationality of π), hence cannot lie exactly on a rational cell boundary. **Every individual digit is computably certifiable.** This does not give a uniform bound on certification depth, much less a normality theorem.

### An exact analytic change of frame

The tail also obeys `T_(n+1)=16T_n-r(n+1)`. Therefore translating the time-dependent rational circle state by the actual tail produces

$$
\Phi_n(u)=u+T_n\pmod1,
\qquad \boxed{\Phi_{n+1}(16u+r(n+1))=16\Phi_n(u)\pmod1.}
$$

This is an **exact nonautonomous conjugacy** of the BBP affine cocycle with multiplication by 16. It uses a future-defined real tail and is **not** itself a finite-time readout. Its rational enclosures are effective.

For nonzero integer `h`, writing `e(x)=exp(2πix)`, the Lipschitz inequality and the elementary bound `sum_{k>=1}1/k²<2` imply

$$
\boxed{\left|\frac1N\sum_{n=0}^{N-1}e(hU_n)
-\frac1N\sum_{n=0}^{N-1}e(h16^n\alpha)\right|
<\frac{32\pi|h|}{15N}.}
$$

This is **weaker** than SUCC's existing sharper source-to-π Fourier transfer (JPC-16); it is a convenient independent proof from the simple rational polynomial bound. By Weyl's criterion, equidistribution of `{U_n}` is equivalent to base-16 normality of `α`, hence to hexadecimal normality of π. This establishes equivalence, not cancellation: bounding the **selected** Fourier sum remains the missing theorem.

## 4. Crucible and precise counterexamples (NCB-13--16)

1. **Delete time and forcing, use naked T₁₆:** at `n=0`, `{U₀}=0`, but `{U₁}={47/15}=2/15`, while `{16U₀}=0`. The bare circle shift does not realize the rational BBP source. The corrected timestamped cocycle does.
2. **Forget the integer lift, attempt rational division:** `u=1/7` and `v=8/7` represent the *same* circle phase. Yet `{u/5}=1/35` and `{v/5}=8/35`, so dividing is not well-defined on `Q/Z`. Our natural-state numerator and odd denominator retain the missing data.
3. **Force a globally backward 2-adic step:** although every original source state is 2-integral, the backward formula `(u-r(1))/16` maps the *admissible forward* state `u=0` to `-47/240`, not 2-integral. Thus a global inverse endomap on `Z_(2)` is unavailable even though the special anchored source history may extend backwards by source-specific cancellation. `N` has the faithful one-sided direction; extending to `Z` demands an explicit backward domain.
4. **Mistake carrier universality for normality:** the same N³ method can implement `r(j)=0`, giving constant rational phase 0, a decisively non-normal source. “Everything encodes in N” is a representation theorem, not a statistical theorem.

These controls separate **pathway construction** (solved) from **actual selected-source frequency discrimination** (OPEN). They also prevent a circular “BBP is conjugate to a radix shift, therefore it mixes” inference: a fixed point of an expanding circle map need not be normal, and the unique selected orbit may be atypical.

## 5. Verdict, provenance, next falsifier

**Disclosed/PROVED PAPER:** an internal N³ model with an exact natural-number section, Cantor coding, rational source, and commuting dyadic/primary observers; the tail conjugacy and elementary explicit error bound. **CLASSICAL input:** BBP formula for π/16, rational-function identity, universal property of N, CRT, irrationality of π, Weyl's criterion. **OBSERVED FINITE:** 18 new unit tests, 3,195 exact standalone checks, independent Machin-arctangent rational oracles for selected positions, with complete 65-method small-worktree replay. **UNVERIFIED:** any π-specific Fourier cancellation, real 1/16 frequency, independence or novel deep theorem.

The decisive next probe should live on the **unique graph i(N)**. Build a reproducible bounded-range signed observable for the literal BBP carry, transport it through the authentic N-state (not arbitrary Haar draws), and test whether *adding* source-indexed Pascal/Lucas and p-adic probes reduces the worst unresolved mixed Fourier residue compared with every proper subfamily. Every ablation must retain the same integer lift, exact n-axis and independent future holdouts. A correlation bound would need a source-specific analytic argument, not just a computation. Compare directly with sibling #271's complete four-bit Walsh jet and current JPC-18 mixed-prime hole.

Repository sources: `observational_succ/bbp_source_memory.py`, `observational_succ/bbp_two_adic.py`, `research/2026-10-24/PI_JOINT_CARRIER_INTERFEROMETRY.md`, `research/2026-10-24/PI_JOINT_CARRIER_LIMIT_ORDER.md`, `research/2026-10-24/PI_PASCAL_LUCAS_QUOTIENT.md`, draft #271 `PASCAL_CARRY_INTERFEROMETRY.md`, `docs/FOUNDATIONS.md`. No imported history or archival file was modified.
