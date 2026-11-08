# Round 2: quantified local history, stronger observers, and the unpaid signed gate

**Pi base-16 normality: OPEN. RH: OPEN.** This is the current additive
handoff for draft#544. Pinned parent research:
`1990b05117d84b33094c8e0f53f7d19b60f48060`; pinned main:
`d32342d375f44ddf62221ad6aff2f534abdc0a03`. Earlier dossiers remain intact.
Everything new is under this namespace; the source and shared catalogs are frozen.

## What this round actually proves

The original source remains

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`,
`U0=0`, `Un=16U_(n-1)+r(n)`.

The strongest improvement is a combination of an explicit original-source
local estimate and a strictly relaxed conditional observer budget:

- [EC1–2](EXPLICIT_CLOCKS.md) select a deterministic prime p<=4A with
  `p=1mod8`, `m=ord_p16`, `m³>p`, and `m² bit_length(p)^(2C)>p`.
  Elementary order counting and quantitative fixed-modulus PNT give
  `4A-p<=4A/log^B(4A)` eventually, for fixed0<B<2C. The exact original
  source's complete prime clock still covers the epoch up to an explicitly
  bounded weight error. Cochrane–Pinner's classical theorem gives the
  uniform nontrivial local-character bound
  `delta <= (2/3^(1/4)) p^(-1/16) bit_length(p)^(3C/8)`.
  Its finite eighth-power cap is computed with rational arithmetic.
- [CQ1–2](cube/THEOREMS.md) retain the final cyclic shift exactly:
  `||a||_(U^j)^(2^j)=D + mean_(nondegenerate preceding shifts)|S(c)|²`,
  with normalization stated in the proof and `D=1-(1-1/m)^(j-1)`.
  The signed identity yields a squared subgroup error and proves that
  local cyclic cube decay holds **iff** `2^j=o(log p)`.
- [CQ6](cube/THEOREMS.md) consequently bounds the prime leakage into any
  adaptively selected s Fourier modes by `[s(1/m+delta²)]^(1/4)`.
  The old sufficient rate `s(1/m+delta)->0` becomes
  `s(1/m+delta²)->0`, with the **same** complementary Fourier residual
  required to tend to zero. With EC this permits
  `s=o(p^(1/8)/bit_length(p)^(3C/4))`. The original residual premise is
  still unproved. This relaxes conditional theorem debt; it does not pay it.

For C=2,B=3, actual-epoch local marginal error is O(log^-3 A), with exact
finite gluing and classical constants retained. No numerical PNT threshold
is supplied. Quantitative PNT also improves gluing for the old selector;
the strengthened selector is what supports the stronger order-based explicit
subgroup estimate. None of these estimates is an estimate of e(hUn) itself.

## Source-relative learning and its obstruction

[CH1–7](chronology/THEOREMS.md) classify all local history Fourier moments:
the surviving coefficient is `sum_j h_j16^t_j modp`. Universal dynamical
relations and modular aliases are separated. Original selected-prime digit
transcripts approach the Haar ×16 trajectory law in total variation, including
lengths `d<=alpha log_16 p` for each fixed0<alpha<1/16 under EC. Exact circle
coordinates are dynamically coupled; independent circle coordinates are not
claimed. The finite support obstruction is `TV>=1-m/16^d`, with equality
once16^d>=p.

Learning these digits also reveals almost the entire local phase. For the
word-cell projection P and fixed h,

`E|a-Pa|² <= pi²h²16^(-2d)`,
`||Pa-Ea||² >= 1-|Ea|²-pi²h²16^(-2d)`.

Thus local-prime leakage tends to one as the observer learns more. The exact
conditional covariance split retains the remaining coarse signed term; its
sign is not supplied by the learning theorem. Nonlinear cube observations have
an independently proved certificate with coefficient variation and residual
costs. These results extend the earlier LY finite-history framework without
introducing new category classes or claiming physical nonlocality.

## The exact remaining proof chain

Use J=[A,2A), the selected prime p and fixed h!=0. Put

`a_n=e(h[Un]_p)`, `b_n=e(h(Un-[Un]_p))`.

Then `W_A(h;0)=Cov_J(a,b)+(Ea)(Eb)` and `|Ea|<=eps_A+delta_CP->0`.
Consequently **original-zero signed covariance decay is equivalent to full
Weyl decay**. [H5](hostile/THEOREMS.md) supplies explicit all-integer-A
prefix gluing, original Green-tail transport, and the normality implication.
Checking only dyadic powers of two is insufficient; a countermodel is given.

The promising alternate attack target keeps exact forcing in each lag:

`k_l=h(16^l-1)`, `F_l(n)=sum_(j=1)^l16^(l-j)r(n+j)`,
`Gamma_l=Cov_J(e(k_l[Un]_p), e(k_l(Un-[Un]_p)+hF_l(n)))`,
`R_A,h(H)=(2/H)sum_(l=1)^(H-1)(1-l/H) Re Gamma_l`.

For1<=H<=m and p not dividing h, [H2](hostile/THEOREMS.md) proves

`|W_A|² <= (A+H-1)/A * [1/H+R_A,h(H)+(1-1/H)(eps_A+delta_CP)
                         +(H²-1)/(3HA)]`.

Choose `H_A=min(m_A,floor(sqrt A))` with EC. Every overhead tends to zero
and has an explicit finite bound. The remaining theorem is exactly

**For every fixed h!=0, limsup_(all integer A→infinity) R_A,h(H_A)<=0.**

This is **OPEN**. The fixed-small-block argument proves that this prescribed
one-sided signed gate is equivalent to normality, not a weaker conjecture
already settled by the local estimates. Its advantage is that it retains
signed interference and avoids demanding a sparse or accurately learned
complement. It is an attack target, not a claimed normality advance by renaming.

| Arrow | Establishing result | Hostile weakening | Status |
|---|---|---|---|
| Literal source -> unwrapped chronology and exact forced lag | Original recurrence; H2; narrow Lean transport | Altered poles or omitted F_l fails | Proved finite/paper; transport kernel checked separately |
| Chronology -> covering prime clocks | PE genealogy plus EC1 | Crossing a later pole birth breaks the frozen clock | Proved with quantitative PNT import |
| Prime clocks -> local nonlinear/history bounds | EC2, CQ1–6, CH1–5 | Modular resonances and critical cube depth persist | Proved paper with CP/BK imports as stated |
| Learned observer -> signed certificate | CQ3–6, CH7 | B=conjugate(a) remains maximally resonant | Proved conditional; original residual OPEN |
| Original zero -> R<=o(1) or Cov->0 | No theorem supplied | Same-forcing coherent shadows have energy and R tending to1 | **OPEN** |
| Signed gate -> full Weyl | H1–3, EC4 | Excessively large H invalidates converse without the support factor | Proved reduction |
| Full Weyl -> base16 normality | H5, exact original Green tail, classical Weyl | Sparse epoch sampling is insufficient | Proved reduction |

## Experiments and verification

[Experiments](EXPERIMENTS.md) retains all156 preregistered lag-energy cases,
raw outward rectangles, exact forcing/covariance reconstruction, and128
matched wrong-seed rejections at H>=4. There are152 cases eligible for the
nonresonant local bound; the other four still have valid exact finite-energy
identities and are explicitly marked. No exponent was fitted or promoted.

Independent finite algorithms verify source powers, cube coefficient
histograms, fourth moments, chronological transcripts, Gaussian-rational
energy identities, interval containment and the new selector. Shared source,
model, classical imports and interval engine are disclosed in
[provenance](PROVENANCE.json), [validation](VALIDATION.md), and scoped reviews.
The [claim ledger](CLAIM_LEDGER.md) and [failed attempts](FAILED_ATTEMPTS.md)
separate new paper results, classical inputs, finite evidence and open claims.

Reproduce into a fresh directory:

```sh
python research/2026-11-08/signed_covariance_round2/validate.py --output /tmp/succ-round2-replay
```

`--full` additionally repeats the unchanged native suite. The earlier native
pass is reused only with an explicit unchanged-input comparison. New research
tests, kernel checks and hosted CI remain separately reported.

The next single theorem most likely to change the verdict is a source-derived
one-sided bound for R at H_A above, uniformly in every sufficiently large A
for each fixed h. A larger memory, another local marginal theorem, or further
finite agreement alone will not establish it.

**Pi base-16 normality: OPEN. RH: OPEN.**
