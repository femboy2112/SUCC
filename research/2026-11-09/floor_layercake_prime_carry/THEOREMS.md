# Floor layer-cake × prime-birth carry × source-twisted Fourier arcs

**Research date:** 2026-11-09. **Scope:** an additive child of SUCC draft PR #563 at `49eb8b857509826d528ce14a8ec98f3ab794e751`. Original four-pole BBP forcing, `U_0=0`, literal real carries, prime-clock passports, integer lifts, and frozen imports remain unmodified. **Base-16 normality of π: OPEN; original-zero signed carry-slip covariance: OPEN.** Elementary calculus/Fourier ingredients are classical; the source-typed assembly is a local SUCC research contribution, not an academic-priority assertion.

## FLP-01 — floor integration is an exact threshold sum (CLASSICAL / finite algebra)

For a measurable integrable weight `g(x)>=0` and nonnegative measurable `f(x)` with finite weighted integer part, Tonelli gives

\[
\int \lfloor f(x)\rfloor g(x)\,dx
=\sum_{k\ge1}\int_{\{f(x)\ge k\}}g(x)\,dx
=\sum_{j\ge0}j\int_{\{j\le f(x)<j+1\}}g(x)\,dx.
\]

The last expression is the original "integer-weighted continuous integrals" viewpoint. The `>=` convention gives exact boundaries. For a signed `f` the positive/negative parts must be separated; we only apply this form to nonnegative carry arguments.

For `x∈[0,1)`, `0≤r<1` set `κ_r(x)=floor(16x+r)`. Then

\[
\boxed{\kappa_r(x)=\sum_{j=1}^{16}\mathbf1_{x\ge (j-r)/16}}.\tag{FLP-1}
\]

Lebesgue integration gives exactly

\[
\boxed{\int_0^1\kappa_r(x)\,dx=\frac{15}{2}+r}.\tag{FLP-2}
\]

Its **17 literal-carry** probabilities are `P(κ=0)=(1−r)/16`, `P(κ=j)=1/16` for `1≤j≤15`, and `P(κ=16)=r/16`. Reducing modulo 16 gives an **exactly uniform distribution on 16 symbols for every fixed r**, despite the exceptional literal carry 16. This uniform statement is for the *Lebesgue reference*, not for the deterministic π path.

## FLP-02 — a fully signed threshold representation of the actual carry character (PROVED)

Fix integer `h` with `h mod16!=0`, let `q=exp(2πih/16)` and `F_(r,h)(x)=q^(κ_r(x))`. The discrete telescoping identity is

\[
\boxed{F_{r,h}(x)=1+(q-1)\sum_{j=1}^{16}q^{j-1}\mathbf1_{x\ge(j-r)/16}}.\tag{FLP-3}
\]

The Haar reference vanishes *exactly*: `∫_0^1 F_(r,h)(x)dx=0`. Therefore for any original integer epoch `I` of length `A`, with `x_(n-1)={U_(n-1)(0)}` and the authentic `0<r(n)<1` for all `n≥2`, the real selected character obeys the **exact centered moving-threshold identity**

\[
\boxed{\frac1A\sum_{n\in I}e\!\left(\frac{h\kappa_n}{16}\right)
=(q-1)\sum_{j=1}^{16}q^{j-1}\frac1A\sum_{n\in I}
\left[\mathbf1_{x_{n-1}\ge(j-r(n))/16}-\left(1-\frac{j-r(n)}{16}\right)\right].}\tag{FLP-4}
\]

The source dependence is *inside* the moving thresholds, not in an after-the-fact constant. This is a signed finite formula: taking absolute values of the 16 contributions before summation destroys possible cancellation. It does **not** by itself show the right side is small on the zero seed.

## FLP-03 — one exact Fourier residue class, with the original source as a phase twist (PROVED)

The function `F_(r,h)` is periodic in x and obeys `F_(r,h)(x+1/16)=q F_(r,h)(x)`. Its integer Fourier coefficients, with `\widehat F(m)=∫_0^1F(x)e(−mx)dx`, are

\[
\boxed{\widehat F_{r,h}(m)=
\begin{cases}
\displaystyle \frac{16(1-e(-h/16))}{2\pi i m}\;e\!\left(\frac{mr}{16}\right),&m\equiv h\pmod{16},\\[3pt]
0,&\text{otherwise}.
\end{cases}}\tag{FLP-5}
\]

Here `e(y)=exp(2πiy)` and the `m=0` coefficient is zero because `h` is nontrivial modulo16. **Proof:** compute separately on the 16 subintervals `[j/16,(j+1)/16)`. The geometric sum over j is zero unless m≡h mod16; the common one-cell integral gives the displayed numerator. Since `F_(r,h)(x)=F_(0,h)(x+r/16)` as a periodic function, the forcing translates coefficients by `e(mr/16)`.

For the actual original BBP time-varying r(n), the source phase is therefore the exact factor

\[
\boxed{e\!\left(\frac{m r(n)}{16}\right)\quad\text{for every surviving }m\equiv h\ (16).}\tag{FLP-6}
\]

This is the **literal source-twisted, arithmetic-progression Fourier space** requested by the user's integral idea. SUCC's older FRH-08 already establishes the *unshifted* spectral-support congruence for digit-character step functions. FLP-5 adds the explicit source-dependent shift for the actual literal carry. The coefficients decay only like `1/|m|`; they are not absolutely summable, so a sharp infinite Fourier expansion cannot be freely interchanged with the selected orbit average.

## FLP-04 — rigorous Fejér smoothing and its exact unpaid boundary occupation (PROVED)

Let `σ_H F` denote the usual order-H Fejér mean with Fourier weights `max(1−|m|/H,0)` and `H≥2`. Let

`δ_(n)=dist_T(x_(n-1)+r(n)/16, (1/16)Z/Z)`.

When `δ_n>0`, the standard positive Fejér kernel satisfies

\[
|F_{r(n),h}(x_{n-1})-\sigma_H F_{r(n),h}(x_{n-1})|
\le\min(2,1/(H\delta_n)).\tag{FLP-7}
\]

The bound follows by restricting the kernel to shifts of circular distance ≥δ_n, using its pointwise upper envelope `1/[4H||t||²]`. At a threshold take the trivial upper bound 2. For any fixed `0<ε<1/32`, define the actual **source-moving** bad-boundary count `B_(I)(ε)=#{n∈I:δ_n<ε}`. The signed carry character is represented by the finite Fourier progression with error

\[
\boxed{\left|\frac1A\sum_{n\in I}F_{r(n),h}(x_{n-1})
-\sum_{\substack{|m|<H\\m\equiv h\ (16)}}
\left(1-\frac{|m|}{H}\right)\frac{16(1-e(-h/16))}{2\pi im}
\frac1A\sum_{n\in I} e\!\left(mx_{n-1}+\frac{mr(n)}{16}\right)\right|
\le\frac{2B_I(ε)}A+\frac1{Hε}.}\tag{FLP-8}
\]

Every term is a **source-typed signed** Weyl character; the remaining analytic expense is explicit occupation near moving radix boundaries. Finite arithmetic tests do not control its all-epoch asymptotic. Increasing H while leaving ε fixed does not magically discharge the missing source boundary count.

## FLP-05 — exact real/prime floor threshold slip and genuine source births (PROVED ALGEBRAIC; inherited p-clock regime)

Let p be an odd prime satisfying #497's simple-pole passport. Define `c_n=[pU_n]_p` and `j_n=[p r(n)]_p` as canonical residues in `0,...,p−1`, with the original seed zero. Then

\[
 c_n=16c_{n-1}+j_n-pz_n,\qquad
 z_n=\sum_{q=1}^{16}\mathbf1_{c_{n-1}/p\ge(q-j_n/p)/16}.
\]

The true real carry is `κ_n=Σ_q 1_{x_(n-1)≥(q-r(n))/16}`. Hence the **exact slip** is

\[
\boxed{\kappa_n-z_n
=\sum_{q=1}^{16}\left[
\mathbf1_{x_{n-1}\ge(q-r(n))/16}
-\mathbf1_{c_{n-1}/p\ge(q-j_n/p)/16}\right].}\tag{FLP-9}
\]

With real complementary coordinate `b_n=x_n-c_n/p` this gives the inherited exact update

\[
\boxed{b_n=16b_{n-1}+r(n)-j_n/p-(\kappa_n-z_n).}\tag{FLP-10}
\]

This is a *discrete–continuous floor integration* of #563's existing real/prime slip identity, not a new bound on its average. It places all prime-birth jumps, even when `j_n/p` is O(1) and real `r(n)` is O(n^-2), inside the same 16 comparable moving threshold integrals.

**Sharp hostile seed control:** take the same forcing but change the initial state by rational `s=1/5`. Since `16^n ≡1 mod5`, the real circle phase shifts by exactly `1/5` at all times, so each *literal real carry residue modulo16* changes by **3 or 4** at every time n≥2. Yet for every odd prime `p≠5`, all p-primary residues and injections (hence all p-carries) are identical because the seed shift is p-integral. This proves the prime floor-threshold system **alone** does not select the original zero real history. The old #563 coherent/dyadic hostile seeds remain separately applicable.

## FLP-06 — the positive four-pole source has an exact floor Laplace transform (PROVED; not real orbit sampling)

Let the already authenticated positive BBP field be `Q(x)=4−2e^(−3x)−e^(−4x)−e^(−5x)`, `R(a)=∫_0^∞e^(−ax)Q(x)dx=4/a−2/(a+3)−1/(a+4)−1/(a+5)`, with probability law `μ_a(dx)=e^(−ax)Q(x)dx/R(a)`, `a>0`. For any `L>0`, `|z|≤1`, put `M_(a,L)(z)=E_(μ_a)[z^(floor(LX))]`. Splitting the positive integration domain into `[j/L,(j+1)/L)` and evaluating the four exponential antiderivatives gives the exact closed formula

\[
\boxed{M_{a,L}(z)=\frac1{R(a)}\sum_{(d,w)=(0,4),(3,-2),(4,-1),(5,-1)}
\frac{w[1-e^{-(a+d)/L}]}{(a+d)[1-z e^{-(a+d)/L}]}.}\tag{FLP-11}
\]

A derivative at z=1 or layer-cake tail sum gives the expected integer floor,

\[
\boxed{\mathbb E_{\mu_a}\lfloor LX\rfloor=
\frac1{R(a)}\sum_{(d,w)}\frac{w}{(a+d)(e^{(a+d)/L}-1)}.}\tag{FLP-12}
\]

The four *signed* poles remain intact even though the sum defines a positive measure. At native scaling `L=a→∞`, `Y=aX ⇒ Gamma(2,1)` from the positive simple source zero. Therefore for |z|≤1,

\[
\boxed{M_{a,a}(z)\longrightarrow
\frac{1-2e^{-1}+e^{-2}z}{(1-e^{-1}z)^2}.}\tag{FLP-13}
\]

That limit **is not a Haar digit-character law**: its numerator has no zeros on |z|=1, so averaging these auxiliary floor characters does not produce the selected π Weyl cancellation. The Gamma rank-two limit is shared with a simpler two-pole positive source; the limiting PGF alone is not source identifying. The rank-two log moment `ψ(2)=1−γ` still exists, but no intrinsic Euler–Mascheroni term enters FLP-13 until a log/Mellin observable is explicitly introduced.

## FLP-07 — inherited source correction budget and remaining arithmetic target

The original positive forcing has `r(n)≤C/n²` for n≥2 with `C=1920/2457` (inherited #520 AC-01). For every fixed m=1 and original epoch start A, the source-induced change from `floor(16 x_n)` to `floor(16x_n+r(n+1))` occurs at most `E≤ceil(A/L_A)` times, where `L_A=floor(log_16(15(A+1)²/C))`, under the inherited admissibility condition. Consequently

\[
\boxed{\left|\frac1A\sum_{n=A}^{2A-1}e\!\left(\frac{h\kappa_{n+1}}{16}\right)
-\frac1A\sum_{n=A}^{2A-1}e\!\left(\frac{h\lfloor16x_n\rfloor}{16}\right)\right|
\le 2\left|\sin\frac{\pi h}{16}\right|\frac{\lceil A/L_A\rceil}{A}=O_h(1/\log A).}\tag{FLP-14}
\]

This is a **seed-uniform** transport, not a zero-seed-specific normality estimate. The coherent wrong seed has zero corrections yet maximally nonnormal real phase, as already documented in #520. It shows exactly why the floor-integral interface is *useful representation geometry* but not itself the missing theorem.

**Verdict-changing probe:** prove a new, original-zero bound on the signed centered moving-threshold sums in FLP-4/FLP-9, or on `B_I(ε)` at a source-compatible shrinking scale **together with** the signed Fourier-character sums in FLP-8. Demand distinct performance on the coherent same-forcing counterseed, rational p-unit seed and period-p completions. The obvious uniform-phase integral cannot be substituted for the realized orbit because that would assume the conclusion at the source-selection boundary. All-epoch real complementary-phase covariance remains OPEN.

## FLP-08 — source-twist resolution barrier at the quadratic clock (PROVED)

The exact source factor in FLP-5 is useful **only if the observer has enough frequency resolution to see it**. For every nontrivial integer h mod16 and any Fejér cutoff H≥2, the unforced smoothed digit character is `σ_H F_(0,h)` and its authentic forcing-shifted counterpart is `σ_H F_(r,h)`. From FLP-5,

\[
\begin{aligned}
\left|\sigma_H F_{r,h}(x)-\sigma_H F_{0,h}(x)\right|
&\le \sum_{\substack{|m|<H\\m\equiv h\ (16)}}
\left|\widehat F_{0,h}(m)\right|\left|e(mr/16)-1\right|\\
&\le 2\left|\sin\frac{\pi h}{16}\right|r\,\#\{m:|m|<H,\ m\equiv h\pmod{16}\}\\
&\le 2\left|\sin\frac{\pi h}{16}\right|r\left(\frac H8+1\right).
\end{aligned}\tag{FLP-15}
\]

The single-frequency step uses `|e(t)-1|≤2π|t|` and `|\hat F_0(m)|=16|sin(πh/16)|/(π|m|)`; the frequency-count bound is elementary. Thus for original times n∈[A,2A) and `0<r(n)≤C/A²`,

\[
\boxed{\sup_x\left|\sigma_H F_{r(n),h}(x)-\sigma_H F_{0,h}(x)\right|
\le 2\left|\sin\frac{\pi h}{16}\right|\frac{C}{A^2}\left(\frac H8+1\right).}\tag{FLP-16}
\]

In particular, **every Fejér observer with `H=o(A²)` loses the direct forcing translation at the level of its bounded continuous readout**. This conclusion is true for every possible circle orbit; it is an *instrument-resolution* obstruction, not π digit equidistribution. Detecting the `O(A^-2)` forcing at constant spectral phase requires Fourier frequencies of order at least `A²` (up to constants); that is the same order as #555's independently derived **relative-source** spectral resolution threshold. At `H≈A²`, the Fejér boundary occupation payment in FLP-8 is still unpaid: larger frequency resolution alone does not establish signed cancellation.

**Calibrated countercontrol:** the exact *unsmoothed* step function can jump by one carry at a microscopic threshold for arbitrarily small positive r; hence there is no uniform `O(Hr)` bound for the unsmoothed carry itself. The good result concerns the declared Fejér-regularized observer. Floating finite tests corroborate FLP-15 for n=100/256 and H through1024; proof is analytic, not inferred from these tests.

## Reproduction, source provenance, and independence

- Original source: preexisting `observational_succ/duck_bbp.py` (imported, unchanged); original prime clock and #563 PBC-01–06 (read only); #520 AC-01/02 (read only); #559 FRH-08 Fourier alias rule (read only).
- Additive code: `observational_succ/bbp_floor_layercake.py`, `tests/test_bbp_floor_layercake.py`.
- Focused test method: `python -m unittest discover -s tests -p 'test_bbp_floor_layercake.py' -v` from the repository root. A *local* isolated shim of `duck_bbp.forcing` supplied the identical polynomial source formula during initial testing; the shim is **not** committed or presented as a full official checkout.
- Integer `Fraction` tests are exact for threshold/carry and p-primary chronology. The independent piecewise Fourier integration and Gamma-floor transform use floating arithmetic only as diagnostics. They are not interval certifications or all-horizon normality evidence.
