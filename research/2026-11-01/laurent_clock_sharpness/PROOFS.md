# Original four-pole Laurent clock: a sharp seed-uniform phase-transport boundary

**2026-11-01 — research-only paper derivation, exact rational witnesses.** Stacked on PR #454 (`a3802f2c1574362a4fb38cc85ab149a0ccb847f2`). The authentic four signed BBP poles and the actual selected state `U_0=0` are unchanged. The coherent comparator below is explicitly a *different real initial state*, not a point in the original finite rational-state register. No π normality, RH, physical quantization, or new Lean theorem is claimed.

## LCS-01. Exact source and residual, every fixed order

Let

\[
r(z)=\sum_{a=1}^4\frac{w_a/8}{z-p_a},\quad
(w_a)=(4,-2,-1,-1),\quad(p_a)=(7/8,1/2,3/8,1/4).
\]

The exact original source state obeys `U_0=0, U_n=16U_(n-1)+r(n)`. For any fixed integer `d>=1`, define

\[
a_m(j)=\sum_a(w_a/8)(p_a-j)^m,\qquad
F_{n,k}=\sum_{j=1}^k16^{k-j}r(n+j),\qquad
F^{[d]}_{n,k}=\sum_{j=1}^k16^{k-j}\sum_{m=1}^{d-1}\frac{a_m(j)}{n^{m+1}},
\]

with the sum empty when `d=1`. This extends the parent PR #454 notation; `d=1` is the completely uncompensated PR #435 case. Put `R_{n,k}^{[d]}=F_{n,k}-F_{n,k}^{[d]}`. The finite geometric identity

\[
\frac1{n+u}=\sum_{m=0}^{d-1}\frac{(-u)^m}{n^{m+1}}+\frac{(-u)^d}{n^d(n+u)}
\]

and `Σw_a=0` give the independent **exact rational expression**

\[
\boxed{R_{n,k}^{[d]}=\frac{16^k}{n^d}\sum_{j=1}^k\frac1{16^j}
\sum_a\frac{(w_a/8)(p_a-j)^d}{n+j-p_a}.}\tag{1}
\]

The verification module computes (1) by a different route from `F-F^[d]` and checks equality on exact rational source times, including a source-coordinate holdout.

## LCS-02. A strict sign and a nonzero leading coefficient at EVERY order

Set `u=j−7/8>0`. The pole offsets are `j−p_a=(u,u+3/8,u+1/2,u+5/8)`. Hence

\[
8(-1)^d a_d(j)=4u^d-2(u+3/8)^d-(u+1/2)^d-(u+5/8)^d<0
\]

for every integer `j>=1` and every `d>=1`. Therefore

\[
\boxed{(-1)^{d+1}a_d(j)>0},\quad
c_{d,k}=\sum_{j=1}^k16^{-j}a_d(j),\quad
\boxed{(-1)^{d+1}c_{d,k}\ge |a_d(1)|/16>0}.\tag{2}
\]

The infinite leading constant `c_d=Σ_(j>=1)16^-j a_d(j)` converges absolutely and is **nonzero of the same sign** for every fixed `d>=1`. Each `c_d` is rational, because

\[
c_d=\sum_a\frac{w_a}{8}\sum_{m=0}^d\binom dm p_a^{d-m}(-1)^m M_m,
\quad M_m=\sum_{j>=1}j^m16^{-j}\in\mathbb Q.
\]

Exact first values, obtained without an infinite numerical sum, are

| `d` | `c_d` |
|---:|---:|
| 1 | `1/64` |
| 2 | `-7/512` |
| 3 | `55/4096` |
| 4 | `-595/32768` |
| 5 | `8551/262144` |

These signs and constants are source-sensitive. Replacing the four-pole forcing invalidates the sign and the subsequent sharpness certificate.

## LCS-03. Uniform Laurent remainder AND derivative envelopes

For every fixed `d>=1` and each `k>=1`, put `M_q=Σ_(j>=1)j^q16^-j`, `c=c_(d,k)`. Each offset `u=j−p_a` obeys `0<u<j`, and `Σ|w_a|/8=1`. After dividing (1) by `16^k`, define the analytic function for real `x>0`

\[
R_d(x,k)/16^k=x^{-(d+1)}C_{d,k}(x),\quad
C_{d,k}(x)=\sum_{j=1}^k16^{-j}\sum_a(w_a/8)(p_a-j)^d\frac{x}{x+j-p_a}.
\]

Termwise differentiation of the *finite* sums proves, for all real `x>0`,

\[
|C-c|\le M_{d+1}/x,\quad |C'|\le M_{d+1}/x^2,\quad |C''|\le2M_{d+1}/x^3.
\]

The product rule yields the following **uniform in k, exact all-x bounds**:

\[
\boxed{\left|\frac{R_d}{16^k}-\frac c{x^{d+1}}\right|\le\frac{M_{d+1}}{x^{d+2}}},\tag{3}
\]
\[
\boxed{\left|\frac{R'_d}{16^k}+\frac{(d+1)c}{x^{d+2}}\right|\le\frac{(d+2)M_{d+1}}{x^{d+3}}},\tag{4}
\]
\[
\boxed{\left|\frac{R''_d}{16^k}-\frac{(d+1)(d+2)c}{x^{d+3}}\right|\le\frac{(d+2)(d+3)M_{d+1}}{x^{d+4}}}.\tag{5}
\]

Because (2) bounds `|c|` away from zero independently of `k`, equations (4)–(5) show that for all sufficiently large real `x`, uniformly in `k`, the first derivative has a nonzero fixed sign, the second derivative has the opposite sign, and the first derivative is monotone. The threshold is **fixed after d**, not assumed numerically certified for every d. The finite oracle verifies the actual signed derivatives at independent rational holdouts.

## LCS-04. Monotone small-derivative sum lemma (elementary)

Write `e(t)=exp(2πit)`. Suppose a real `C²` phase `f` on `[a,b]` has `f'` of constant sign and monotone, and `λ<=|f'|<=1/2` with `λ>0`. Its consecutive increments `Δ_n=f(n+1)-f(n)` have that same sign, are monotone, and obey `λ<=|Δ_n|<=1/2`. The exact identity

\[
e(f(n))=\frac{e(f(n))-e(f(n+1))}{1-e(\Delta_n)}
\]

allows discrete summation by parts. Since

\[
\frac1{1-e(t)}=\frac12+\frac i2\cot(\pi t),
\]

the coefficients vary monotonically along a vertical line when the signed `Δ_n` are monotone. For `|t|<=1/2`, `|1-e(t)|=2|\sin\pi t|>=4|t|`. Endpoint terms plus the total variation are bounded by `4/(4λ)`. Including the remaining final endpoint proves the safe bound

\[
\boxed{|\sum_{n=a}^b e(f(n))|\le 2+1/\lambda}\tag{6}
\]

for integer endpoints, with the harmless `+2` covering intervals with one or zero differences. This is the elementary first-derivative exponential-sum test, explicitly restricted to the near-zero derivative regime; it does **not** assert nonstationary cancellation when the derivative approaches an integer resonance.

## LCS-05. Sharpness theorem: the coherent counterseed detects the next clock wall

Keep the **same authentic four-pole forcing**, but mark the distinct **real** seed

\[
 s_*=-\alpha,\qquad \alpha=\sum_{j>=1}16^{-j}r(j)=\pi/16.
\]

Its exact trajectory is `U_n(s*)=−T_n`, where the original positive Green tail `T_n` satisfies `T_n=O(n^-2)` and `Σ_nT_n<∞`. This completed point is `0`, rational and nonnormal, and this altered seed is not in the original finite rational zero-seed register.

Let the source-corrected lag score be

\[
D^{[d]}_{h,k}(N;s_*)=\sum_{n=1}^{N-k}e\left(h[(16^k-1)U_n(s_*)+F^{[d]}_{n,k}]\right),\qquad
L^{[d]}_{N,K}(h;s_*)=\frac2{KN}\sum_{k=1}^{K-1}\left(1-\frac kK\right)\Re D^{[d]}_{h,k}.
\]

Write `C_(h,k)` for the ACTUAL lag correlations using `U_(n+k)-U_n`, and `L^C` for their identically weighted real score. Fix any `d>=1`, integer `h!=0`, and real

\[
\boxed{d+1<c<d+2},\qquad K_N=\lfloor c\log_{16}N\rfloor.
\]

**All-horizon limiting theorem:**

\[
\boxed{\lim_{N\to\infty}L^C_{N,K_N}(h;s_*)=1},\tag{7}
\]
\[
\boxed{\lim_{N\to\infty}L^{[d]}_{N,K_N}(h;s_*)=\frac{2(d+1)}c-\frac{(d+1)^2}{c^2}},\tag{8}
\]
\[
\boxed{\lim_{N\to\infty}\big(L^C-L^{[d]}\big)=\left(1-\frac{d+1}{c}\right)^2>0.}\tag{9}
\]

**Proof.** The true coherent lag is `U_(n+k)-U_n=T_n-T_(n+k)`, so

`|C_(h,k)(N;s*)-(N-k)|<=2π|h| Σ_(n>=1)T_n=O_h(1)`

uniformly in `k`, giving (7) for `K=O(logN)`. For the corrected lag the exact phase is

\[
(16^k-1)U_n(s_*)+F^{[d]}_{n,k}
=T_n-T_{n+k}-R_d(n,k).
\]

Set `ℓ=log_16N`. For fixed small `δ>0`, ignore `n<δN` at normalized cost at most `δ+o(1)`, uniformly in `k`; on the remaining bulk `T_n-T_(n+k)=O_δ(N^-2)`.

For `k<=(d+1-ε)ℓ`, (3) implies `R_d(n,k)=O_(d,δ)(N^-ε)`, hence `D^[d]/N=1+O(δ)+o(1)` uniformly in this low band.

For `(d+1+ε)ℓ<=k<K_N`, (2), (4), (5) show that the phase `f(x)=-hR_d(x,k)` has monotone derivative of fixed sign. Because `c<d+2`, its derivative is uniformly `<1/2` on `[δN,N-k]` for sufficiently large N. Its absolute derivative has a lower bound `λ_(N,k)>=c_(d,h,δ)16^k/N^(d+2)`, so (6) gives uniformly over the high band

\[
\frac1N\left|\sum_{\delta N\le n\le N-k}e(-hR_d(n,k))\right|
\le O_{d,h,\delta}\left(N^{-1}+\frac{N^{d+1}}{16^k}\right)
=O_{d,h,\delta}(N^{-\epsilon})+O(N^{-1}).
\]

Adding back the small `T_n-T_(n+k)` phase changes the normalized sum by `O_(h,δ)(N^-2)`. Thus the high-band normalized score has magnitude `<=δ+o(1)`. The transition band has `O(εℓ+1)` lags, bounded termwise by one. Since `K_N/ℓ->c`, its total weighted contribution is `O(ε)`. First take `N->∞`, then `δ->0`, then `ε->0`. The weighted Riemann sum from `k/K in [0,(d+1)/c]` gives

\[
2\int_0^{(d+1)/c}(1-t)dt=\frac{2(d+1)}c-\frac{(d+1)^2}{c^2}.
\]

This proves (8) and (9). The proof uses the exact source leading sign and nonzero coefficient, not a fitted finite phase profile.

For `d=1,c=5/2`, (9) gives `1/25`, recovering original Main XVIII PR #435's sharp coherent-transport barrier. **NEW generalizations:** `d=2,c=7/2` gives limit `48/49` and gap `1/49`; `d=3,c=9/2` gives limit `80/81` and gap `1/81`. The correction order can be any fixed positive integer. No assertion is made at `c>=d+2`, for order d depending on N, or for the actual selected `U0=0` without an independent proof.

## LCS-06. What is refuted, and what remains open

PR #454 supplies vanishing *absolute/seed-uniform* phase-transport budgets when `K≈(d+1)log_16N` at each fixed Laurent order d>=2. Equations (7)–(9) prove this leading coefficient is **sharp for a seed-uniform vanishing transport theorem at the next larger logarithmic scales**: for any c in `(d+1,d+2)`, a genuine same-four-pole real counterseed has a definite positive transport defect. Extending the seed-uniform transfer just by truncating one more source series cannot avoid paying its new residual phase.

This DOES NOT prove that a source-selected, literal-zero seed estimate is impossible beyond the clock, does not give an unconditional negative or positive conclusion for π normality, and does not show any physical information scrambling mechanism. It clarifies that the new carrier-relative entropy and higher-order signed lag representation in PR #454 is an *instrument* whose fundamental seed-uniform precision has a sharp obstruction.

The next productive question is whether the exact zero boundary produces a genuinely new joint source/phase inequality **inside** a compensated clock; the source angular relative period (#452) might supply extra structure only if a source-attested signed estimate and adversarial seed test are produced. Avoid a new equivalence-only repackaging.

## Provenance and mathematical inputs

- Original SUCC four-pole source, Green tail and selected zero boundary: Main XVIII, PR #440/#442 and original #454.
- The `d=1` logarithmic barrier in PR #435 is inherited; the present d>=2 proof uses its low/high-band philosophy but new all-order exact derivative coefficients and a finite signed phase countermodel for every d.
- Elementary geometric remainder, rational Eulerian power sums, Abel summation, sine chord lower bound, source-tail summability, and Riemann integration. All are classical tools; no academic priority claim.
- All new assertions are paper proofs and exact rational controls, not a Lean theorem. No new all-horizon signed saving is claimed for the original zero seed.
