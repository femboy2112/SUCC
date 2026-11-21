# BORG–MAHLER theorem dossier: guarded chart, double completion, and radial source spectrum

**Types first.** Original SUCC BBP source and literal `U_0=0` stay fixed. `W`, `C`, `T`, `Q(t)`, `F(z)` and their various `2`-adic, real, polynomial and symbolic completions are distinct maps. All statements here are classical imported or elementary paper consequences in stated domains. Their assembly is new to this SUCC branch; no research priority or external formal review is claimed.

## BM-01: exact boundary for the Mahler 3/2 *observer chart* (PROVED paper, classical source)

Let `T` multiply `g+r` by `3/2`, take integer part `g'` and fractional remainder `r'`. Here `g in Z`, `r in [0,1)`. Let `b = g mod2 in {0,1}`. Define `W(g)=(3g+b)/2` and `R_b(r)=(3r-b)/2`. Put `J=[0,1/2)`.

**Theorem.** If `r in J`, both `T(g,r)=(W(g),R_b(r))` and `R_b(r) in J` hold if and only if

`(b=0 and 0<=r<1/3) OR (b=1 and 1/3<=r<1/2)`.

**Proof.** If `g=2k` then `3(g+r)/2=3k+3r/2`. Its integer part is `3k`; the next remainder lies in `J` iff `0<=3r/2<1/2`, i.e. `r<1/3`. If `g=2k+1`, `3(g+r)/2=3k+3/2+3r/2`. For `r<1/3` its integer part is `3k+1` (not `W(g)=3k+2`) and remainder is `1/2+3r/2 in [1/2,1)`; for `r>=1/3`, the integer part is `3k+2=W(g)` and remainder `(3r-1)/2 in [0,1/4)`. All endpoints are exact with the specified half-open J. QED.

**Guarded dynamics:** Define `D={(g,r) in Z x J: the above parity guard holds}`. On D the chart equals the true rational multiplier and lands in `Z x J`. On failure the *chart* stops, not the true T trajectory. `tau(g,r)=inf{n>=0: T^n(g,r) notin D}` is a boundary hitting time, with `tau=infinity` allowed. For positive `xi=g+r`, `xi` is a Mahler Z-number **iff** `tau=infinity`. This is an equivalence of definitions, **not** a proof that Z-numbers exist or do not exist.

**Carry/coordinate defect at the boundary.** For the odd branch with `0<=r<1/3`, the true integer is `W(g)-1` and the true remainder is `R_1(r)+1`; the integer/remainder defects cancel exactly, preserving the full rational value even though the W chart has ceased to be a lawful integer-plus-fraction decomposition. For even `r>=1/3` inside J, the coordinate formulas are still correct but their output exits J. These are *different boundary types* and must not be combined into one fictitious physical discontinuity.

**Sharp hostile inputs:** `(2,1/3)` has true successor `(3,1/2)` (the W integer remains right but J fails). `(1,1/4)` has true successor `(1,7/8)` while W predicts integer `2` and remainder `-1/8`. At `(1,1/3)`, the W branch is admitted and successor `(2,0)`. These three cases discriminate a genuinely guarded chart from unguarded `W` substitution.

## BM-02: finite survivor intervals with exact boundary certificate (PROVED paper)

Fix `g0>=0` integer and horizon `N>=0`. Set `g_(k+1)=W(g_k)`, `b_k=g_k mod2`, `a_0=1`, `c_0=0`, `a_(k+1)=3a_k/2` and `c_(k+1)=3c_k/2-b_k/2`. Then *hypothetical* remainder `r_k=a_k r_0+c_k` for the W chart. Define

`I_N(g0)=J intersect intersection_(k=0)^(N-1){r0 : L(b_k)<=a_k*r0+c_k<U(b_k)}`

where `(L(0),U(0))=(0,1/3)` and `(L(1),U(1))=(1/3,1/2)`. Because `a_k>0`, every pulled-back guard is half-open interval. Their intersection is either empty or a single rational half-open interval, computable exactly by `max` of lower and `min` of upper rational bounds. Induction using BM-01 proves `I_N(g0)` is *exactly* the set of starts producing N lawful Z-chart steps.

Examples: `I_0(0)=[0,1/2)`, `I_1(0)=[0,1/3)`, `I_2(0)=[0,2/9)`. For `g0=1`, `I_1=[1/3,1/2)` but `I_4=empty`. For `g0=13`, `I_4=[35/81,13/27)`, a nonempty interval with known first four steps. Such a finite interval is never presented as proof of infinite survival.

## BM-03: one history, two distinct completions (MAHLER 1968; proved within guarded domain)

On an N-step guarded path, define `S_N=sum_(j=0)^(N-1) b_j(2/3)^j`. Iterating `r_k=(2/3)r_(k+1)+b_k/3` gives

`3r0 = S_N + 3*(2/3)^N*r_N`, with `0<=3r0-S_N< (3/2)*(2/3)^N` in ordinary real arithmetic.

Iterating `g_k=(2/3)g_(k+1)-b_k/3` gives

`S_N+3g0=3*(2/3)^N*g_N`, so `S_N ≡ -3g0 (mod 2^N)` in `Z_2` (all denominators are odd).

For **one infinite guarded path**, `S_N -> 3r0` in `R` and `S_N -> -3g0` in `Q_2`. These limits are not numbers in the same ambient field; no equality `3r0=-3g0` is asserted. An observer with finite rational data can recover convergent approximants in both places with *different* error norms. Original primary source: Mahler 1968, pp. 314–315.

## BM-04: Fibonacci necessary language and an exact hostile π prefix (CLASSICAL + finite SUCC source)

For an infinite guarded orbit, every suffix `m` satisfies `sum_(j>=0) b_(m+j)(2/3)^j =3r_m <3/2`. If `b_m=b_(m+1)=1`, the left side is at least `1+2/3=5/3`, contradiction. Thus `11` is forbidden at *all suffixes*; length-N binary words subject **only to that necessary rule** count `F_(N+2)` by the recurrence `A_(N+2)=A_(N+1)+A_N` (`A_0=1,A_1=2`). Its adjacency matrix can be `[[1,1],[1,0]]`, with growth rate the golden ratio. **The no-11 subshift is NOT an iff characterization of Z histories.** Mahler's original bounds exploit additional restrictions.

SUCC #681 independently certifies from the original BBP source and original zero seed `pi/16` starts `0.3243F6A8885A..._16`. Under #681's declared low-bit-first nibble journal the first nibble `3` maps to `1100`. By the just-proved necessary condition **this selected symbolic journal cannot be the parity sequence of a Mahler Z-number**. No contradiction: every binary journal is still a legal 2-adic W history. This is a sharp rejection of a *literal Z-identification*, not a theorem about π digits beyond the certified prefix.

## BM-05: two different W/C 2-adic inverse charts (PROVED paper, classical symbolic method)

On `Z_2`, put `W(g)=(3g+(g mod2))/2` and shortcut Collatz `C(g)=g/2` if even, `(3g+1)/2` if odd. Each integer-valued branch is `2`-adically continuous on its parity cylinder. Both admit contracting inverse branches:

- `W`: `f_b(y)=(2y-b)/3` for `b=0,1`.
- `C`: `h_0(y)=2y`, `h_1(y)=(2y-1)/3`.

Each branch contracts by `1/2` in 2-adic norm. Therefore for every infinite binary word `b_0b_1...`, the inverse compositions define unique 2-adic states `Phi_W(b)` and `Phi_C(b)` with prescribed chronological parities; continuous inverses exist and give `Phi_W∘sigma=W∘Phi_W` and `Phi_C∘sigma=C∘Phi_C`. Hence `Phi_W∘Phi_C^(-1)` is a 2-adic homeomorphism conjugating C to W. Their *same raw integer* orbits do not generally agree (`2` gives `W` parity `011` versus `C` parity `010`). The first N bits determine residues modulo `2^N` only.

Explicit inverse series:

`Phi_W(b)=-sum_(j>=0) b_j*2^j/3^(j+1)` in `Z_2`,

`Phi_C(b)=-sum_(j>=0) b_j*2^j/3^(s_(j+1))`, where `s_(j+1)=sum_(i=0)^j b_i`.

A source-selected finite word `3243F6A8885A` yields 48-bit residues `0x0E8F0415EFC3` for W and `0x138D4B466283` for C. Only the latter was previously reported in #681. These are **constructed** source-labelled addresses, not a real-to-2-adic identification of π, and not a positive-integer Collatz conjecture.

## BM-06: exact radial Mahler potential and the 0→1→5 phase boundaries (PROVED paper, Jensen / argument principle)

Original BBP Mellin numerator and its derived polynomial from #678:

`Q(t)=4-2t^3-t^4-t^5=(1-t)H(t)`;

`H(t)=(t^2+2)(t^2+2t+2)` has four complex roots all of modulus `sqrt(2)`, while `1-t` contributes a root of modulus `1`. For `rho>0`, define

`m_Q(rho) = (1/2pi) int_0^(2pi) log|Q(rho*exp(i theta))| d theta`.

By Jensen's formula applied to the degree-five polynomial with leading coefficient `-1`, this equals the sum over the five roots `alpha_j` of `log max(rho,|alpha_j|)`. Thus:

```
m_Q(rho)=log4                   0<rho<=1,
        =log4 + log(rho)        1<=rho<=sqrt(2),
        =5 log(rho)             sqrt(2)<=rho.
```

At `rho=1`, the function is continuous and has a slope jump `0→1`. At `rho=sqrt(2)`, it has a slope jump `1→5`. On the three **open** regimes, derivative wrt `log(rho)` equals root-count winding `0,1,5`; the Hardy Toeplitz Fredholm index is `0,-1,-5`. At the two critical circles `Q(rho e^{i theta})=0` somewhere and winding/index are **undefined** (although the logarithmic potential remains finite/continuous). The base measurement `M(H)=exp(m_H(1))=4`, `M(Q)=4`, and the complementary `K(t)=(t^8-16)/H(t)` also has `M(K)=4`, so `M(H)M(K)=16`.

**Interpretation:** This is *auxiliary radial analytic evolution with sharp source-selected boundaries*. It is a lawful scalar source invariant and matches the existing #678 index; it is **not** the original chronological BBP recurrence, nor an intrinsic physical scalar energy law. A source-mutant preserving only low Taylor data may destroy the equal-radius four-root threshold.

## BM-07: native source-time F is D-finite but NOT standard k-Mahler (PROVED corollary, imports Bézivin)

Define the original source-time generating function `F(z)=sum_(n>=1) r(n)(z/16)^n`, where `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`. The exact rational expression is

`r(n)=(120n^2-89n+16)/((2n-1)(4n-1)(8n-7)(8n-3)) =15/(64 n^2)+O(n^(-3))`.

Because `r(n)` is rational in n, the coefficient sequence `a_n=r(n)/16^n` satisfies a polynomial-coefficient first-order linear recurrence: if `r(n)=N(n)/D(n)`, then

`16 D(n+1) N(n) a_(n+1) - D(n) N(n+1) a_n=0`.

Thus F is P-recursive-coefficient / D-finite. It is not rational: rational generating functions have eventually constant-coefficient recurrences and coefficients equal to finite sums of `P_j(n)lambda_j^n`; a nonzero sequence with asymptotic `a_n ~ (15/64)*16^(-n)n^(-2)` cannot be such a sum (at the maximal exponential rate, polynomial-amplitude trigonometric sums cannot decay as n^(-2)). Bézivin's theorem says a D-finite formal `k`-Mahler function for any integer `k>=2` is rational (as republished/proved by Bell–Coons–Rowland). Hence F is **not** a finite-order standard `k`-Mahler function. This says nothing about a different auxiliary functional-equation model with a different generating function.

## BM-08: p-adic Mahler *expansion* is a separate imported instrument (IMPORTED / NO FALSE TRANSFER)

For continuous `f:Z_p→Q_p`, Mahler's interpolation theorem expands `f(x)=sum_(j>=0) (Delta^j f)(0) binom(x,j)` with coefficients tending to zero p-adically. SUCC #17 already imports it as finite difference clock machinery; #272 derives exact dyadic bounds for the native BBP forcing. This basis is a **coordinate system for sufficiently continuous observer outputs**, not a statement that the 3/2 Z-number real remainder map extends continuously across its failed guard, nor that it determines signed real phase of the zero-seeded π orbit. Legacy #599 imports Mahler's irrationality lower bound; the source-specific exponent barrier remains intact.

## BM-09: separation from the actual π statistic (OPEN / conditional)

Freeze the true SUCC source:

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U_0=0, U_n=16U_(n-1)+r(n), U_n+T_n=16^n pi/16`.

No currently constructed map intertwines either guarded Mahler 3/2 *real* chart or the radial `m_Q(rho)` flow with the actual source-selected π real phase `theta_n={16^n pi/16}` in a way that enforces signed shell cancellation. Any such map must preserve the entire source/seed, integer carries, remainder, moving-clock orientation, and normalization. The false seed `s=-pi/16` shares source `Q`, `m_Q`, source clock, and infinite source-complexity but has permanently locked completed real phase; it is a fatal counterexample to **source/seed-blind** normality claims. **Strong canonical boundary-frequency counterexample.** Define `N_k=2^(2^k)` for integers `k>=2` and

`x=1-15*sum_(k>=2)16^(-N_k)`, so the *canonical, nonterminating* base-16 digits of `x in (0,1)` are F at all positions except an isolated zero at each `N_k`. Since `N_(k+1)=N_k^2`, a sufficiently late shell `[B,2B)` contains at most one zero; the density of nibble digits with internal `11` is therefore at least `1-1/B` and tends to 1 uniformly over late B. For `n` between zeros, the real phase is

`theta_n={16^n x}=1-delta_n`, where `delta_n=15*sum_(N_j>n)16^(n-N_j)`.

Choose shell starts `B_k=2N_k`; then every `n in [B_k,2B_k)` precedes the *next* zero `N_(k+1)=N_k^2` by at least `N_k^2-4N_k` digit positions. Therefore `0<delta_n <= 16^(1-(N_k^2-4N_k))`, and `1-cos(2pi theta_n)<=2pi^2 delta_n^2` uniformly on that shell. Consequently `A_(B_k) -> 0` even though the density of local `11` events tends to 1 on every late shell. This refutes **every-shell positive 11-density ⇒ R0** for arbitrary canonical real digit sequences. It does not change π's authentic source (indeed this x is a hostile alternative source). The weaker constant-F expansion ambiguity is not used.

**R0 must still be proved** for the original zero-seeded π orbit:

`liminf_(B→infty) [B^(-1)sum_(n=B)^(2B-1)(1-cos(2pi*16^n*pi/16))] > 0`.

The Mahler finite chart and source spectral boundaries are diagnostic tools, **not** a proof of that inequality. Full normality and RH remain open.
