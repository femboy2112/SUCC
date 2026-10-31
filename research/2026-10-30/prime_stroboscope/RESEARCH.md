# SUCC — Prime stroboscopy: an original-four-pole modular source certificate

**Domain and authority:** paper-level exact arithmetic; `p` an odd prime congruent to `1` or `5` modulo 8; the **unchanged** original four-pole BBP rational prefix with `U_0=0`. This is a new-to-project formalization, not a claimed original contribution to the mathematical literature. Nothing here proves the base-16 normality of π or a signed real-circle Weyl estimate. Main starting state: `e18ba565ca540adb7edf3292f5593929e76d91c5` (Main XVI). PR #395 has a rigorous Stoneham source-grid occupancy certificate; #390–#394 and #396 are read-only neighboring research, not silently included in this branch.

## 1. The authentic rational orbit

Let `Delta=(1,4,5,6)` and `c=(4,-2,-1,-1)`; set

\[
r(n)=\sum_{\delta\in\Delta}\frac{c_\delta}{8(n-1)+\delta},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

All `U_n` are EXACT rationals. The original BBP identity is `U_n = 16^{n-1}π−T_n`, where `T_n>0` is the positive Green tail; it is **not** the same as an integer-only recurrence. We write `x≡y (mod p)` for rational numbers whose *reduced denominators are prime to p*: reduction in `Z_(p)/p Z_(p) ≅ F_p`. This is not a congruence of arbitrary rationals with p in their denominator.

For prime `p≡1 (mod4)` and `k≥1`, define
\[
\boxed{N_p(k)=\frac{(4k-1)p+1}{4}},\qquad p>8k-2.
\]
`N_p(k)` is an integer and `8N_p(k)−2=p(8k−2)<p²`. Every source denominator seen through time `N_p(k)` is strictly smaller than `p²`. Consequently `pU_(N_p(k))` is p-integral and can be reduced modulo p.

## 2. PS-01/02 — exact prime-shadow theorem and coefficient involution

**Theorem.** Let the four coefficients be p-integral rationals `(A,B,C,D)` at offsets `(1,4,5,6)`, and denote the resulting recurrence by `U^c`. Put

\[
\mathcal J(A,B,C,D)=(-4C,B,-A/4,D).
\]

Then for `p>8k−2`:
\[
\boxed{p\,U^c_{N_p(k)}\equiv
\begin{cases}
U^c_k& p\equiv1\pmod8,\\
U^{\mathcal J c}_k& p\equiv5\pmod8,
\end{cases}\quad(\bmod p).}
\]

Note `\mathcal J²=id`. The original BBP vector is a fixed point of `\mathcal J`, since its first and third coefficients satisfy `A=-4C`. Thus **for every prime p≡1 (mod4), p>8k−2,**
\[
\boxed{pU_{N_p(k)}\equiv U_k\pmod p.}\tag{PS-01}
\]

**Proof, term by term.** Unroll the real recurrence as `U_N=Σ_(j=1)^N 16^(N−j) r(j)`. In `pU_N mod p`, only denominators divisible by p survive. Such a denominator has the form `pq`, with `q<p` because `8N−2<p²`. For each integer `q` from 1 through `8k−2` whose residue `q mod8` belongs to `Δ`, exactly one pole contributes (regardless of which `p mod8` class): its source clock index is the unique integer `j` satisfying `8(j−1)+δ=pq`, where `δ ≡ pq (mod8)` belongs to `Δ`.

Write `q=8(l−1)+δ_q`, `δ_q∈Δ`, `1≤l≤k`, and compare the remote multiplier `16^(N−j)` to the original `16^(k−l)`. Direct algebra gives
\[
\boxed{E:=(N-j)-(k-l)=
\frac{(8k-2-q)(p-1)+\delta-\delta_q}{8}.}
\]

When `p≡1 mod8`, `δ=δ_q`. The supplementary law `(2/p)=+1` implies
`16^E=2^{(8k−2−q)(p−1)/2}≡1 (mod p)`; the pole coefficient is unchanged. All contributions reconstruct `U^c_k`.

When `p≡5 mod8`, `(2/p)=-1`, and multiplication by 5 permutes the four offset classes. The exact mapping table is

| `q mod8` | original offset | actual offset `5q mod8` | `16^E mod p` | resulting original-offset coefficient |
|---|---|---|---|---|
| 1 | 1 | 5 | `−4` | `−4C` |
| 4 | 4 | 4 | `1` | `B` |
| 5 | 5 | 1 | `−1/4` | `−A/4` |
| 6 | 6 | 6 | `1` | `D` |

For example, when `q≡1 mod8`, `8k−2−q` is odd and `δ−δ_q=4`, so `16^E=2^{(odd)(p−1)/2+2}=-4`. The other rows follow identically. This constructs `U_k^{\mathcal Jc}` exactly, completing the proof. The only external classical dependency is Euler's criterion plus the supplementary quadratic-reciprocity law for 2; the rest is integer arithmetic. ∎

**Coefficient rigidity.** `\mathcal Jc=c` exactly iff `A=-4C`; `B,D` are unconstrained. For an integer vector, if untransformed equality `pU^c_{N_p(1)}≡U^c_1` holds for all sufficiently large primes `p≡5 mod8`, then `A=-4C`: the k=1 difference is `-(21/20)(A+4C)`, and a nonzero rational can vanish modulo only finitely many primes outside its denominator. **This identifies one arithmetic ratio, not π uniquely.** The mutant `(4,0,-1,0)` satisfies the ratio; the mutant `(5,-2,-1,-1)` does not. For `p≡1 mod8`, no coefficient-selection restriction arises from this stroboscope.

## 3. PS-03 — prime-conductor birth and four original pole encounters

For any prime `p≥13`, `p≡1,5 mod8`, the first denominator containing p occurs at
\[
b_p=\begin{cases}(p+7)/8,&p\equiv1\pmod8,\\(p+3)/8,&p\equiv5\pmod8.\end{cases}
\]
The first four p-divisible pole events then occur in chronological order at
\[
b_p,\qquad m_4=(p+1)/2,\qquad
m_5=\begin{cases}(5p+3)/8,&p\equiv1,\\(5p+7)/8,&p\equiv5,\end{cases}
\qquad m_6=(3p+1)/4=N_p(1).
\]

Their exact p-primary residues are

| Event | `p≡1 mod8` | `p≡5 mod8` |
|---|---|---|
| birth | `pU_(b_p)≡4` | `pU_(b_p)≡−1` |
| at 4p | `pU_(m4)≡7/2` | `pU_(m4)≡7/2` |
| at 5p | `pU_(m5)≡33/10` | `pU_(m5)≡−66/5` |
| at 6p | **`pU_(m6)≡47/15`** | **`pU_(m6)≡47/15`** |

These are congruences in `F_p`; denominators 2,5,10,15 are invertible for eligible primes. The proof is repeated `pU_n≡16pU_(n−1)+p r(n)` with the factor `16^((p−1)/8)=(2/p)` and the corresponding shifted exponents. The final residue equals `U_1=47/15` in both classes. There is no cancellation of the new p-denominator up through `m6` (all displayed residues are nonzero for eligible primes). Hence new primes are genuinely born in the reduced denominator of `U_(b_p)` and survive at least through `N_p(1)`. Classical Dirichlet progressions give infinitely many such births.

**A full local p-period is present before the first collision.** Between `b_p` and `m4−1`, no new p-pole is encountered, so
`pU_(b_p+j) ≡ c_p 16^j (mod p)`, `c_p=4` or `−1`. Its period is `d_p=ord_p(16)`, and because `16=2^4`, `d_p | (p−1)/4` for `p≡1 mod4`. The number of steps before the first collision is `3(p−1)/8` for `p≡1 mod8` and `(3p+1)/8` for `p≡5 mod8`, both exceeding `(p−1)/4`. There is thus always at least one complete multiplicative-subgroup orbit in the rational p-primary fiber.

A complete period of nonzero frequency `h` has additive Gauss-period sum
`Σ_(j=0)^(d_p−1) exp(2πi h c_p 16^j/p)`, bounded by `√p+1` by the classical character expansion. This can be useful when `d_p≫√p`, but no such order lower bound for all eligible primes is asserted, and incomplete periods require separate bounds. **It is NOT a bound on the full real-circle phase `exp(2πihU_n)`**.

## 4. PS-04 — why p-primary normality does not transfer to the selected real circle

At the remote stroboscopic time, write a reduced rational `U_N=A/(pD)` with `gcd(p,D)=1` and `p` present in the denominator (equivalently `U_k mod p ≠0`). Chinese remaindering gives uniquely
\[
\boxed{U_N\equiv\frac{a_p}{p}+\frac{b_D}{D}\pmod1},\qquad
 a_p\equiv AD^{-1}\equiv U_k\pmod p,\quad b_D\equiv Ap^{-1}\pmod D.
\]
Thus
\[
 e(hU_N)=e_p(h a_p)\,e_D(h b_D).
\]
The strobe theorem determines the **first** factor. The second is the changing complementary-conductor phase, which may correlate arbitrarily with the first from the viewpoint of our present estimates. Controlling only p-primary Gauss periods does not constrain the full character sum. An arbitrary complementary phase can even cancel the p-component phase exactly, giving a coherent product; source-specific control of the actual complementary phase is the missing test.

**Explicit denominator cancellation:** `U_4=1428806141948/111035925` and its numerator has factor `73`; at `p=73,k=4`, `U_k mod p=0`, and the far-time `U_(N_p(4))` has no p-factor in its reduced denominator. An assumption that *every* distant stroboscopic index has a new p-denominator is therefore false. The theorem states congruence, not universal nonzero residue.

**Seed firewall:** changing the initial state to any p-integral rational `s` changes the remote orbit by `16^N s`, so `pU_N(s)≡pU_N(0) (modp)`; this p-primary transport cannot recognize the original zero seed among such controls. In particular it is NOT the missing selected π normality theorem. It is genuine source-specific arithmetic transport with a marked information-loss boundary.

## 5. PS-05 — a certified finite occupancy measurement of the selected π orbit

The exact BBP identity gives
`U_n=16^(n−1)π−T_n`, `T_n=Σ_(j>=1)16^(−j) r(n+j)`. The authentic positive Laplace kernel satisfies `Q(x)<=15x`, hence `r(n+j)=R(8(n+j)−7)<=15/(8n+1)^2` for `j>=1`. Summing the geometric tail yields
\[
\boxed{0<T_n<(8n+1)^{-2}.}
\]
Let `u_n={U_n}` be exact rational and `ε_n=(8n+1)^{-2}`. The actual pure radix-circle phase `{16^(n−1)π}` lies inside the circular interval swept from `u_n` to `u_n+ε_n`. If the closed interval meets only a single equal bin, the true bin is **certified without input digits of π**.

For `n=1..256` every one of the 16 equal hexadecimal bins is unambiguous. The certified counts are

`[17,18,18,15,14,12,16,18,19,24,13,13,14,16,13,16]`, summing to 256. The implementation uses exact `Fraction` only; a separate 410-digit mpmath check matched every bin, but that numerical agreement is only an independent finite calibration. For 256 equally sized bins, exactly the first two indices are ambiguous under this conservative same bound; the implementation returns sets of all possible bins, not false single classifications.

**Scope:** an exact finite prefix certificate cannot establish a constant-factor occupancy bound for every N and every interval. Stoneham's normality proof possesses an all-stage bounded-multiplicity theorem; the new prime strobe possesses only *sparse modular self-similarity*, not an all-horizon real-circle bound. No π-normality status promotion.

## 6. The next verdict-changing instrument

Build a **multi-prime real-phase CRT coupling** with the authentic four-pole source. For each eligible p and k, record exact `(p-primary residue, cofactor phase, carry, time, Walsh sector, source posterior)` rather than independent prime marginals. Search for a nontrivial source-derived bound on their mixed signed correlation, first on complete p-period windows and then across enough times to control empirical interval occupancy. Falsify on coherent original-forcing `s=−π/16`, matched source mutants, p-primary-only alignments and normal Stoneham controls. Correct the overgeneralized Main XVI instruction to require failure for all rational periodic seeds; rational translations preserve integer-base normality and integer changed seeds can preserve literal carries.

Current tools expose *p-fiber transport* and *finite selected real-circle occupancy* separately. The bridge between them is an **access/probe gap**, not an established impossibility and not a proof that π normality is independent of any axioms.

## Source references (context, not independent priority proof)

- Original BBP formula: Bailey, Borwein & Plouffe (1997), *Mathematics of Computation*, doi:10.1090/S0025-5718-97-00856-9; formula and independent presentation: https://www.mathworks.com/company/technical-articles/computing-pi.html .
- Supplementary law for `(2/p)` and Euler's criterion: classical quadratic reciprocity; formal mathlib documentation: https://imperialcollegelondon.github.io/FLT/docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.html .
- Normal calibration: existing SUCC draft #395 `research/2026-10-30/frame_reset_crucible/` (Stoneham c=3,5 and nonnormal c=2), *not* merged or modified here.
- Prime-spectral obstacles: existing main SUCC `docs/CLAIM_LEDGER.md`, `research/2026-10-27-ravel-prime-ladder/`, and the previously integrated selected BBP carry/phase dossiers.
