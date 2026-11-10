# Scale covariance × finite-place/real gluing for the **original** BBP source

**Research checkpoint, 2026-11-08. π base-16 normality: OPEN. RH: OPEN.**

This work begins from the user's stronger proposal: all observation scales must be mutually compatible; a continuously realizable analytic place should be pinned by authenticated finite-place observations. We use *source-typed* scale arrows, exact adelic arithmetic and explicit disambiguation tests. "Thermodynamically open" below is an **analogy for an unbounded family of observation scales**, not a physical heat-flow theorem or an assumption of randomness. External classical inputs are labeled.

## Typed objects, source and frame maps

Freeze `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_(n+1)=16U_n+r(n+1)`. Equivalently `r(x)=P(x)/D(x)`, with

`P(x)=120x²−89x+16`, `D(x)=(2x−1)(4x−1)(8x−7)(8x−3)`.

For an observation origin `n≥0` and integer step `k≥1`, define the **unwrapped source transport**

`F_(n,k)=sum_(j=1)^k 16^(k−j)r(n+j) ∈ Q_(>0)`, and
`R_(n,k)(u)=16^k u+F_(n,k)` on the real or rational unwrapped state.

Do NOT confuse these affine transport maps with invertible maps on the fractional circle (`×16` there is a covering). For real `x>0` the same **specified rational** `r(x+j)` makes `F_(x,k)` a smooth real-analytic interpolation of the source frame transport. It is not a canonical p-adic interpolation at arbitrary real `x`.

### ASG-01 — exact compositional / naturality cocycle (PROVED LOCAL)

For all nonnegative integer `n`, positive integers `j,k`, and every seed `s` for which the recurrence is interpreted,

`U_(n+k)(s)−16^k U_n(s)=F_(n,k)`;
`F_(n,j+k)=16^k F_(n,j)+F_(n+j,k)`;
`R_(n+j,k) ∘ R_(n,j)=R_(n,j+k)`.

Proof: substitute the original recurrence or partition the finite forcing sum after `j` steps; the seed drops out of the defect, but is retained in the state. The cocycle also holds for real `x>0` when using the **declared original rational interpolation**. It does not assert scale invariance of the real Fourier marginals.

### ASG-02 — original four-pole **uniform all-scale** second jet (PROVED LOCAL)

Let `a=15/64`, `b=151/512`, `c_k=(16^k−1)/64` and

`beta_k=−7/8+2k/(16^k−1)`, `−7/8<beta_k≤−89/120<0` for every `k≥1`.

**Quantified claim**: for **every integer `n≥1` and `k≥1`**, without any bound relating `k` to `n`,

`| (n² F_(n,k)/c_k) − 1 − beta_k/n | ≤ 298/(25 n²)`. **(ASG2)**

In particular `F_(n,k) = c_k n^(−2)(1+beta_k/n+O(n^(−2)))`, where the big-O has an absolute constant independent of `k`.

**Proof with the constants paid.** Set the four original pole offsets `b_i=(7,4,3,2)` and weights `c_i=(4,−2,−1,−1)` in `r(y)=sum_i c_i/(8y−b_i)`. Exact cancellations give `sum c_i=0`, `sum c_i b_i=15`, `sum c_i b_i²=151`. Expanding each reciprocal after its quadratic geometric term, for every `y≥2`,

`r(y)=a/y²+b/y³+E(y)`, with

`|E(y)| ≤ [sum_i |c_i| b_i³] / [8^4 y^4 (1−7/16)] = (1535/2304)y^(−4) < y^(−4)`.

Normalize the k source steps with the geometric probability weights

`w_(k,j)=15*16^(k−j)/(16^k−1)`, for `j=1,...,k`.

Then `sum w=1`, `E_w[j]=16/15−k/(16^k−1)` and `E_w[j²]≤272/225` (the truncated geometric law is stochastically bounded by the full positive geometric law). Elementary Taylor bounds, valid for **all j≥0**,

`|(n+j)^(−2)−n^(−2)+2j n^(−3)|≤3j²/n⁴`,

`|(n+j)^(−3)−n^(−3)|≤3j/n⁴`,

and `|E(n+j)|≤1/n⁴` give

`|F_(n,k)/(sum_j 16^(k−j)) − a/n² − [b−2a E_w[j]]/n³|`

`≤ [3a(272/225)+3b(16/15)+1]/n⁴ = (447/160)/n⁴`.

Divide by `a=15/64`, and compute

`(b/a)−2 E_w[j]=151/120−32/15+2k/(16^k−1)=beta_k`.

The resulting normalized error is `447/160 × 64/15 = 298/25`, proving ASG2. All four original signed poles matter: the `151` coefficient is changed by the explicit matched-leading-source mutant in the tests.

### ASG-03 — uniform logarithmic pressure and Euler–Mascheroni seam (PROVED LOCAL, classical product formula)

For `n≥16` and **every k≥1**,

`| log[64 n² F_(n,k)/(16^k−1)] − beta_k/n | ≤ 16/n²`. **(ASG3)**

Proof: write the exact normalized rational as `1+beta_k/n+epsilon_(n,k)` using ASG2. Since `|beta_k|≤7/8` and `|epsilon|≤298/(25n²)`, for `n≥16` the absolute departure from 1 is at most `(7/8+298/400)/n=1.62/n≤0.102`. Thus `|log(1+x)−x|≤x²`, and `298/25+1.62²<16` controls the whole logarithmic remainder.

For each fixed `k≥1`, the **honest absolutely convergent** real constant

`C_k = sum_(n=1)^infinity { log[64 n² F_(n,k)/(16^k−1)] − beta_k/n }`

exists. For `N≥16`,

`|sum_(n≤N)log[64 n² F_(n,k)/(16^k−1)] − beta_k H_N − C_k| ≤ 16/N`.

Since `H_N=log N+gamma+O(1/N)`, the sum is

`beta_k log N + beta_k gamma + C_k + O_k(1/N)`.

**All-scale version (not just fixed k):** for *any* schedule `k_n≥1` of integer scale steps, the accumulated renormalized error from time `M≥16` obeys

`|sum_(n=M)^N {log[64n²F_(n,k_n)/(16^(k_n)−1)]−beta_(k_n)/n}| ≤16 sum_(n=M)^N n^(−2) ≤16/(M−1)`.

If `k_n=max(1,ceil(log_16 n))`, then `sum_n (beta_(k_n)+7/8)/n` converges, and the common harmonic leading term is `−(7/8)H_N` plus a finite offset. This is a genuine source-derived `gamma` occurrence under harmonic regularization, **not** evidence that gamma causes Fourier cancellation; its finite constant can absorb changes of regularization.

**All finite places.** Every `F_(n,k)` is positive rational and nonzero. Let `|·|_p=p^(−v_p(·))`. The classical product formula of Q gives **exactly**, with only finitely many nontrivial primes for each rational,

`log F_(n,k) + sum_(p prime) log|F_(n,k)|_p = 0`.

Writing `P_fin(n,k)=sum_p log|F_(n,k)|_p`, ASG3 therefore yields

`P_fin(n,k)=2log n−log c_k−beta_k/n+O(16/n²)` (uniform in k after removing `log c_k`).

The finite-place ledger pins the **absolute Archimedean magnitude** of this *rational transport defect*. It does NOT pin the real-circle phase `exp(2πih U_n)`; valuative magnitudes do not encode that character. The product formula is classical (Tate's thesis / adelic arithmetic), not newly invented here.

### ASG-04 — finite place **really can pin the analytic source**, within a source class (PROVED LOCAL)

Declare the source model class `g(x)=P(x)/D(x)` with the **frozen original denominator** `D(x)` above, integer numerator `P(x)=a x²+b x+c`, degree≤2, and coefficient height `max(|a|,|b|,|c|)≤120`.

At prime `p=41`, the denominators `D(1),D(2),D(3)` and the Vandermonde determinant `2` are p-adic units. Knowing the rational source's three p-adic values `g(1),g(2),g(3)` **mod 41²** reconstructs `P(1),P(2),P(3)` modulo 1681, and hence `(a,b,c)` modulo 1681 by second differences. Since `1681>240`, each coefficient has a *unique* representative in `[−120,120]`. Using the actual source yields exactly

`(a,b,c)=(120,−89,16)`.

This proves the entire specified analytic rational continuation `P(x)/D(x)` (for every real `x` away from poles) from **three finite-place source samples**, under the declared pole/degree/height contracts. Each sample is computed from `duck_bbp.forcing`, no π oracle; `n=4,7,31,10000` are holdouts, not interpolation points.

The model-class restriction is essential. If the analytic-place continuation is allowed to be arbitrary real-analytic, then `g_epsilon(x)=r(x)+epsilon e^(−x)sin(pi x)` agrees with the original forcing at **every integer x**, and all integer source histories and finite-place rational source observations, while differing on noninteger real x. This is an explicit **non-identifiability countermodel** to unrestricted analytic interpolation. `g_epsilon` is not claimed to be a rational or p-adic analytic continuation.

### ASG-05 — source-specified all-place *magnitude* still does not select zero-seed Fourier cancellation (REFUTED universal shortcut)

The exact defects F, their cocycle, uniform jet and full finite-place pressure are **seed independent**. For the genuine zero seed the completed real phase is `16^n (pi/16)`. For the coherent seed `s_* = −pi/16`, the state instead satisfies `U_n(s_*) = −T_n -> 0`, so its epoch mean `W_A(h;s_*) -> 1` for every fixed h, even though *all F_(n,k)* and their exact adelic pressure are identical. This is a logically decisive real counterseed to `all-scale source defect/pressure -> real Haar`.

There is also an **entirely rational, no-π-oracle finite-epoch control**: put `N=2A+10`, `M=8A+80`, `alpha_N=sum_(j≤N)16^(−j)r(j)` and `s_A=−floor(2^M alpha_N)/2^M`. Each s_A is dyadic (p-integral for odd primes); the original-source real selected history on epoch `[A,2A)` has

`(1/A)sum_(n=A)^(2A−1)|U_n(s_A)| ≤ 2^(−80)/(15 A) + 16^(−10)/[225 A (2A+11)^2] + 1/[15(A+1)^2] -> 0`.

Proof uses the exact Green completion, `alpha−alpha_N≤16^(−N)/[15(N+1)^2]`, the geometric sum `sum_(n=A)^(2A−1)16^n=(16^(2A)−16^A)/15`, and `T_n≤1/[15(n+1)^2]`. Therefore `|W_A(h;s_A)−1|≤2π|h|` times this bound. These epoch-dependent s_A share the all-prime source defect F and every odd-p **p-primary channel history** on any p-admissible finite sample, but **do not** share the 2-primary seeded state and are **not** a single fixed alternative seed. Do not claim the pointwise uniform `2^(−80)` term tends to zero; only its *mean* does. This is the same type of hostile control used in #554, independently replayed here.

### ASG-06 — exact signed source/complement *variation* gate (PROVED CONDITIONAL; premise OPEN)

Assume the genuinely balanced, four-stage prime selector and local mode estimate of **draft #554**, with `p_A≡1 mod8`, `p_A~(12/5)A`, `m_A=ord_(p_A)(16)`, `p_A∤h`, `delta_(p_A)=o(1)` and

`E_A = delta_(p_A) + 4 sqrt(p_A)(2+log m_A)/A = o(1)`.

On the **actual** original epoch `[A,2A)`, write exactly `a_n=e_p(h sum_d C_(d,p)(n))` and `b_n=e(h[U_n−(sum_d C_(d,p)(n))/p])`, so `a_n b_n=e(hU_n)`. The four scalar first-shell stage coefficients are `4,7/2,33/10,47/15`, all nonzero mod the eligible primes when p∤h. Every prefix `[A,t)` meets at most four genuine source stages. #554's incomplete subgroup Gauss bound therefore gives, without replacing the actual temporal window by a full p-shell,

`max_(A≤t≤2A)|sum_(n=A)^(t−1) a_n| ≤ A delta_p + 4 sqrt(p)(2+log m) = A E_A`.

For any unit complex complementary sequence b_n, **discrete Abel summation** yields

`|W_A(h)| ≤ E_A [1+TV_A(b)]`, where
`TV_A(b) = sum_(n=A)^(2A−2)|b_(n+1)−b_n|`.

Consequently an **as-yet-unproved**, very strong source-selected `E_A[1+TV_A(b)] -> 0` condition suffices for π base-16 normality. This condition is *not* claimed likely: the finite original epochs have `TV_A` of order A and the bound is numerically vacuous there. For a coherent counterseed with `|W_A|->1`, this inequality forces `TV_A ≥ (1−o(1))/E_A−1`, exposing the missing high-variation phase complement. **This new elementary Abel wrapper is an obstruction/diagnostic, not a replacement for #544/#554's more promising signed covariance.** External subgroup and prime selector hypotheses remain those in draft #554, subject to its published review corrections.

### ASG-07 — heat/thermodynamic observer firewall (CLASSICAL, REFUTED as normality lever)

An externally prescribed observer heat flow with time `t_A -> infinity` gives the circle Fourier coefficient `exp(−4π²h² t_A)W_A(h) -> 0` for every fixed nonzero h **for every input sequence**, including the coherent counterseed. It is observer-induced washing-out, not evidence that the authentic source is normal. "Thermodynamic openness" must refer to a source-derived *signed* effect if it is to help prove π normality; no physical entropy production or energy transfer is established here.

## Dependency/provenance and claim limits

- **Primary internal source:** `observational_succ.duck_bbp.forcing` (original four signed poles, frozen), with independent four-fraction test oracle; `integer_bbp_carrier` for literal carry interface (read-only); `selected_orbit` and Main XXI π frontier (read-only).
- **New branches studied read-only:** #544 (carry integer-lift + signed Poisson innovation) and #554/#552 (actual-epoch balanced prime clocks / three-channel pulses). BEC-05's `p∤h` qualification and BEC-08's averaged counterseed repair are explicitly observed.
- **External classical background:** product formula for Q (Tate's thesis); Bailey–Crandall on BBP/Hypothesis A; Fourier/Abel summation. No claim of academic novelty of these classical ingredients.
- **Not obtained:** source-selected upper bound for `R^bal_(A,h)` of #554, signed `W_A(h)=o(1)`, all-epoch Fejer energy decay, or π normality. New theorems here are source magnitude, interpolation rigidity and conditional variation, NOT the missing real signed cancellation.
