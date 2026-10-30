# Exact Green-mixture descent: the order-statistic Oily triangle is a mixture of original BBP atom sheets

**Research date:** October 29, 2026. **Source hierarchy:** merged SUCC Main XIV `ec2fbe3`; PR #367 `b6a3815` for the original single-forcing Laplace-convolution microfield; sibling PR #368 `e5660f0` for the accepted triangular order-statistic tail field, original conditional two-geometric packet law, and its signed source controls; current child PR #369 for the Gamma rank sheet. New result is a compatibility theorem between two **different positive finite carriers** and reconciliation of their previously different first corrections. No archival source, actual initial BBP seed, or historical claims are changed. π normality and RH remain OPEN.

## 1. Two source passports, one underlying four-pole function

For `t>0`, define the ORIGINAL source polynomial-in-exponentials

`Q(t)=4-2e^(-3t)-e^(-4t)-e^(-5t)`.

Its Laplace transform is the authenticated original signed forcing function

`R_F(a)=int_0^infinity e^(-at)Q(t)dt=4/a-2/(a+3)-1/(a+4)-1/(a+5)`.

Set `r(k)=R_F(8k-7)` for `k>=1`. The original arithmetic recurrence is `U_0=0`, `U_(k+1)=16U_k+r(k+1)`; no changed source or forcing is introduced.

The positive *future Green tail* of PR #368 is

`T_n=sum_(j>=1)16^(-j)r(n+j)=int_0^1 x^(8n) R_P(x)dx`, for `n>=0`,

where `R_P(x)=[4-2x^3-x^4-x^5]/(16-x^8)` for `0<x<1`.

Do not conflate the single-forcing Laplace `R_F(a)` with the positive Oily tail kernel `R_P(x)`: they are different functions built from the same original polynomial.

## 2. Exact source-to-source disintegration, at every n (new comparison)

PR #367 uses the single-forcing probability law

`mu_b(dt)=e^(-bt)Q(t)dt/R_F(b)`, `b>0`.

PR #368 uses an observed source `X_n in (0,1)` with law

`P(X_n in dx)=x^(8n)R_P(x)dx/T_n`.

Set `Z_n=-log X_n` (a **coordinate transform**, not a new random path) and define

`p_(n,j)=16^(-j)r(n+j)/T_n`, `j>=1`.

**Theorem GMS-1 (all-time exact mixture).** For every `n>=0` and measurable `B subset (0,infinity)`,

`P(Z_n in B) = sum_(j>=1) p_(n,j) mu_(8(n+j)-7)(B)`.

All terms are strictly positive, the weights sum to one, and the equality is an equality of probability measures, not an asymptotic analogy.

**Proof:** `x=e^(-t)` converts the PR #368 density to

`e^(-(8n+1)t) Q(t)dt/[T_n(16-e^(-8t))]`.

Expanding the positive geometric denominator, with Tonelli,

`1/(16-e^(-8t))=sum_(j>=1)16^(-j)e^(-8(j-1)t)`.

The numerator then equals `sum_(j>=1)16^(-j)e^(-(8(n+j)-7)t)Q(t)dt`, whose `j`-th mass is `16^(-j)r(n+j)` and normalized density is `mu_(8(n+j)-7)`. QED.

**Full graded packet coupling:** In addition to the latent *future index* `J_f=j` and the Laplace microstate `Z`, set `X=e^(-Z)` and conditionally generate original Oily packet grade `J_packet` using the two geometric stages with rates `u(X)=X-X^2/2`, `v(X)=X^2/2`. This reproduces the full PR #368 `(X,J_packet)` marginal and its authentic `p_j(x)` density. The latent future index and packet grade are **not** asserted independent. This is a valid joint realization of the positive source, **not** an identification of its latent paths with deterministic pi digits.

## 3. A genuine recursive update of the virtual future-source field

The first mixing weight is `p_(n,1)=r(n+1)/(16 T_n)`, and the exact Green recurrence is

`T_(n+1)=16T_n-r(n+1)=16T_n(1-p_(n,1))`.

Therefore, for every `n>=0`, `j>=1`,

`p_(n+1,j) = p_(n,j+1)/(1-p_(n,1))`.

**Theorem GMS-2 (drop/reindex/renormalize).** The next positive field is precisely the original future-index law conditioned on `J_f>=2`, with index relabelled `j -> j-1`. Under that relabelling, the component measure itself remains unchanged because `8((n+1)+(j-1))-7=8(n+j)-7`.

This is a true recursive source-field update using *only* original BBP data. The recursive operation drops the already passed future slot, but does not assert that an actual digit-path collapse was observed. It is a deterministic reshuffling/normalization of the source forecast, not physical feedback. The original signed seed remains independently necessary.

**Finite exact controls.** For `D>=2`, `T_n^(D)=sum_(j=1)^D16^(-j)r(n+j)` satisfies `16T_n^(D)-r(n+1)=T_(n+1)^(D-1)`. Thus the finite-truncated normalized source also obeys the same drop/reindex law with `D-1` new terms. The *pointwise* positive density truncation equals

`sum_(j=1)^D16^(-j)x^(8(n+j)-7)Q(-log x)
 = x^(8n+1) R_P(x) [1-(x^8/16)^D]`, `0<x<1`.

These are literal rational polynomial identities after replacing `Q(-log x)` by `4-2x^3-x^4-x^5`, and are checked on exact rational grids, not inferred from floating-point data.

## 4. The first-order correction mismatch actually glues EXACTLY

The two positive carriers have distinct natural scaled observations.

**Single forcing / PR #367 + child #369.** For `b>0`, let `Z~mu_b`, `V=bZ`, `g(v)=log v-exp(-lambda v)` and `lambda=(sqrt(5)-1)/2` (marked Oily golden selection). The previous theorem gives

`E g(V)=Omega_OM-[59/30]*(1+2lambda^4)/b+o(b^(-1))`.

**Future order-statistic / PR #368.** Let `X_n~x^(8n) R_P(x)/T_n` and put `a=8n`, `Y=a(1-X_n)=a(1-e^(-Z_n))`. PR #368 obtains the independent paper-level first correction

`E g(Y)=Omega_OM+(6lambda-19/2)/a+O(a^(-2))`.

We now derive the *difference* from the exact mixture without fitting a coefficient.

**Step 1: original four-pole source shape.** Within each future mode `j`, `b=a+delta_j`, `delta_j=8j-7`. The full-source single-forcing shape correction contributes

`C_source = (59/30)(1+2lambda^4)`

with negative sign in `E g`. The `59` is exactly `-Q''(0)` and survives independently of the golden reference selection.

**Step 2: future Green clock shift.** Since `r(n+j)~15/(a+delta_j)^2`, the mixing weights converge to `w_j=15/16^j`, and `E_w J_f=16/15`. Therefore

`E_w delta_J=8*(16/15)-7=23/15`.

We evaluate `aZ=(a/b)V`, with `a/b=1-delta_j/a+O(delta_j^2/a^2)`. Since the Gamma(2) boundary has

`E[V g'(V)]=1+2lambda^4`,

rescaling gives the additional negative correction

`C_clock = (23/15)(1+2lambda^4)`.

The `O(1/a)` changes in the mixing weights multiply the same leading observable `Omega_OM` and sum to **zero**, because the weights remain normalized; the geometric tails have finite moments and justify the expansion after truncating large `j`.

**Step 3: nonlinear observation coordinate.** The actual order-statistic coordinate is not `aZ`, but

`a(1-e^(-Z)) = aZ-(aZ)^2/(2a)+O((aZ)^3/a^2)`.

For `g'(v)=1/v+lambda exp(-lambda v)` and boundary `V~Gamma(2,1)`,

`E[V^2 g'(V)]/2 = 1+3lambda^5`.

This produces

`C_coordinate=1+3lambda^5`.

**Theorem GMS-3 (three-source-term first-jet reconciliation).** For the authentic original four-pole source,

`C_source+C_clock+C_coordinate`
`=(59/30+23/15)(1+2lambda^4)+1+3lambda^5`
`=(7/2)(1+2lambda^4)+1+3lambda^5`
`=9/2+7lambda^4+3lambda^5`
`=19/2-6lambda`.

The last equality is EXACT in `Q(sqrt(5))` because `lambda^2=1-lambda`, `lambda^4=2-3lambda`, and `lambda^5=5lambda-3`.

Hence our source-mixture route **independently reproduces the first correction of the different PR #368 finite carrier**:

`E g(Y)=Omega_OM-[19/2-6lambda]/a+o(1/a)`.

A genuine difference between the two finite carriers is accounted for by **three separate, source-specific, explicitly quantified operations**, rather than hidden behind the shared limit constant. Exact quadratic-field arithmetic verifies the coefficient; independent mpmath integrals check finite `a=40,160,800`. Rigorous derivation of the `o(1/a)` remainder uses the original source exponential tails (geometric in `j`) and Gamma logarithmic integrability; PR #368's independent endpoint expansion provides the stronger `O(a^-2)` remainder without being used to *define* these three coefficients. Scholarly priority and Lean authority remain unverified.

| First-jet source | Signed contribution to `a(E g(Y)-Omega_OM)` | Approximation |
|---|---|---:|
| Original four-pole shape | `-(59/30)(1+2lambda^4)` | -2.5405322661 |
| Green future-clock relabelling | `-(23/15)(1+2lambda^4)` | -1.9807539702 |
| Nonlinear `1-exp(-Z)` observation | `-(1+3lambda^5)` | -1.2705098312 |
| **TOTAL** | **`6lambda-19/2`** | **-5.7917960675** |

## 5. What this actually buys for the selected path

We have obtained a faithful commuting **source marginal square**: accepted rank-two uniform order statistics ↔ original positive Oily tail law ↔ geometrically weighted future-mixture of original single-forcing Laplace atoms, with an explicit recursive tail-conditioning operator. The first-order signed *observable in positive source space* is now consistent across both representations, including the `59/30` four-pole correction and the golden coordinate.

However, all three positive carriers and their mixture weights depend only on original source time and **not** on the BBP initial selector `U_0`. The coherent original-forcing counterseed `U_0=-pi/16` has `U_n=-T_n->0` and fails equidistribution, while sharing every positive field identity above. Therefore the established source isomorphism has not supplied the needed **joint carry/phase coupling**. `Omega_OM` and the coefficient `19/2-6lambda` are NOT signed Fourier decay bounds. Pathwise normality remains an open independent arithmetic obligation.

Next test: construct an original zero-seed-labelled operator that couples the observed digit carry (or an equivalent signed phase record) to the latent `J_f, Z, J_packet` microstate sheet. The coupling must be derived from the original deterministic recurrence—not an arbitrary conditional distribution—and must differ on the coherent counterseed. Require a verifiable `o(N)` signed Weyl estimate or a genuinely weaker sufficient arithmetic lemma, plus hostile source-jet and ordering mutants. Any gauge-invariant Gram spectrum or scalar rank weighting remains seed-blind by the companion child #369 no-go.

## 6. Reproduction and authority

Local self-contained cross-PR Python suite: **9/9 tests passed**, including exhaustive finite rational kernel identities, truncated Green normalizer recursion, normalized future-index drop/reindex, exact quadratic-ring first-jet matching, source-forcing passport, changed-seed independence, and numerical authentic-order-statistic first-jet holdouts. The numerical quadratures are observations, not universal proof certificates. A full native SUCC checkout, Lean, independent peer review, and hosted CI have not been run for this cross-PR child.

Primary references are the exact pinned sibling original-source dossiers PRs #367 and #368 and classical Euler/Gamma facts (NIST DLMF Chapter 5). This cross-source comparison is **new-to-program, paper-proved**, not independently established scholarly priority. No merge or source/claim promotion is authorized.
