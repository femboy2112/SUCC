# SUCC — Operation Minimal Carrier: why four, the 3×5↔16 arithmetic mirror, and the Gamma logarithmic completion

**2026-10-29 · DRAFT MATHEMATICAL RESEARCH.** Parent: SUCC draft #383, exact head `e02933591e7b7486376acb9847e00fd01d9ae498`. Independent sibling #372 is only background. This dossier adds no historical BBP edits, new theorem priority, physical inference or selected π-normality claim. The true source `r(n)` and its marked zero seed remain unchanged. Original research motivation: investigate whether the fixed point `a=4` of the source's continuous reciprocal inversion follows from primitive/minimal splitting and why its outer primes 3,5 meet the circle/line, Gamma, harmonic, and golden Oily machinery.

## Steelman — an *axiomatically minimal* grammar, not a universal claim that nature must use four

A minimality claim needs an explicitly selected category and cost. Here is a mathematically falsifiable one. Consider positive real `a,d,m` with `m>d`, and strictly positive integer primitive weights `p,q,r`. Declare the *three nondegenerate equally-spaced channels* to have delays `m-d,m,m+d` and give their collective neutral base pole the balancing coefficient `W=p+q+r`:

\[
R_{m,d;p,q,r}(a)=\frac{W}{a}-\frac{p}{a+m-d}-\frac{q}{a+m}-\frac{r}{a+m+d}.
\tag{MC-1}
\]

The chosen preparation **cost** is total positive negative-channel weight `W`; the gap `d` is a declared unit of spacing. Requiring all three channels and integer weights matters. This is not Kolmogorov complexity, not a theorem that the first prime imposes a physical splitting law, and not justified by a minimum over all conceivable source grammars.

This family does have a positivity theorem:

\[
Q_{m,d;p,q,r}(x)=p(1-e^{-(m-d)x})+q(1-e^{-mx})+r(1-e^{-(m+d)x})>0\quad(x>0),
\]

\[
R(a)=\int_0^\infty e^{-ax}Q(x)\,dx.
\tag{MC-2}
\]

Moreover `Q(x)=(mW+d(r-p))x+O(x²)`, so `R(a)~S/a²`, with `S=mW+d(r-p)>0`. The *source-normalized* `aX` converges to `Gamma(2,1)` under `mu_a(dx)=exp(-ax)Q(x)dx/R(a)` (prove using Laplace transforms). Rank two is caused by cancellation of the `1/a` residue and first-order positivity; it does NOT, by itself, fix the pole spacings, golden parameter or π digits.

## Theorem MC-01 — primitive reciprocal-center rigidity

Put `u=m-d`, `v=m`, `w=m+d`. Clear the four denominators. The numerator `N(a)=S a²+L a+C` has

\[
S=pu+qv+rw=mW+d(r-p),\qquad C=Wuvw=Wm(m²-d²).
\]

Its two algebraic root shifts (possibly complex for general parameters) have product `rho=C/S`. Asking that the *reciprocal* center of those shifts coincide with the middle pole is exactly `rho=m²`. Direct subtraction gives

\[
\boxed{\rho-m²=\frac{md\,[m(p-r)-dW]}{S}},
\quad\text{so}\quad
\boxed{m/d=W/(p-r),\quad p>r.}
\tag{MC-3}
\]

For all `p,q,r` positive integers and `p>r`, `p≥2`, `q≥1`, `r≥1`, so `W≥4`. If equality `W=4` holds, the ONLY possible triple is `(p,q,r)=(2,1,1)`, giving `m/d=4`. With the **primitive integer spacing** `d=1`, the unique minimal member of this declared class is

\[
\boxed{R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}},
\qquad\boxed{m=4,\quad m²=16.}
\tag{MC-4}
\]

This is a bona-fide conditional uniqueness/minimization theorem. No base sixteen or center four is inserted into the minimization constraints. The coefficient/two-stage grammar, integer cost and equal-spacing requirements are axioms informed by the already authentic BBP source. **Alternative models are possible:** `(p,q,r)=(4,1,1),m/d=2`, `(3,2,1),m/d=3`, `(2,2,1),m/d=5` all satisfy reciprocal alignment at higher weight. Scaling `d` carries the solution to `m=4d`; no absolute length scale is canonical without choosing a unit. Deleting a channel or allowing arbitrarily small real weights destroys the claimed uniqueness/minimum.

For the actual minimally selected source, the numerator is

\[
N(a)=15a²+121a+240=15(a+\alpha)(a+\beta),
\quad\alpha\beta=16,
\quad\operatorname{Disc}(N)=241,
\]

with `alpha,beta=(121∓sqrt241)/30` and positive real root shifts. The positive near-origin slope is `S=2·3+4+5=15=16−1`; thus the same *selected* grammar gives rank-two Gamma scaling, the inversion center and the BBP-specific 15 simultaneously. These are **not independent premises proving normality**; they are consequences of one already source-motivated class.

## Theorem MC-02 — outer-prime two-channel logarithm of the ACTUAL arithmetic clock

Let the authentic inverse-source logarithm of #383 be

\[
\mathfrak D(a)=\log\frac{R(16/a)}{R(a)}-3\log\frac a4
=\log\frac{16(a+3)(a+5)}{(3a+16)(5a+16)}.
\tag{MC-5}
\]

It is an odd hyperbolic function in `u=log(a/4)` and has fixed point `a=4`, but `a↦16/a` does **not** map the native sequence `a_n=8n−7` to itself. Its first two values are `exp D(1)=128/133<1`, `exp D(9)=2688/2623>1`.

Now **follow the actual arithmetic clock**, not an invented time reversal. The bounded inversion defect tends to `L=log(16/15)`. Define the renormalized native increment

\[
\eta_n=L-\mathfrak D(8n-7).
\]

A direct rational factorization proves, for EVERY integer `n≥1`,

\[
\boxed{\eta_n=\log\frac{24n-5}{24n-6}+\log\frac{40n-19}{40n-20}}
=\int_{24n-6}^{24n-5}\frac{du}{u}+\int_{40n-20}^{40n-19}\frac{du}{u}.
\tag{MC-6}
\]

This is an actual source-faithful circle/reciprocal-to-log-line **two-channel** law: after the central pole four cancels, the only residual clocks have slopes `24=8·3` and `40=8·5`. The two *elementary* channels can also be written as

\[
\eta_n=2\operatorname{artanh}\frac1{48n-11}+2\operatorname{artanh}\frac1{80n-39}.
\]

The primitive source prime factors appear in their exact denominators, and

\[
\frac1{24}+\frac1{40}=\frac1{15}=\frac1{16-1}.
\]

This is a rigid harmonic relation of the selected 3,4,5 geometry. It is not an assertion that observer semantics dynamically cause arithmetic carries.

### Rigorous universal remainder and certified finite intervals

For every real `x>0`, `1/(x+1)<log(1+1/x)<1/x`. Apply it to `x=24n−6` and `x=40n−20`, and use `(24n−6)≥18n`, `(40n−20)≥20n`. This gives the strict **all-index** proof inequality

\[
\boxed{\frac1{15n}<\eta_n<\frac1{15n}+\frac7{180n²}.}\tag{MC-7}
\]

The series has the stronger explicit asymptotic

\[
\eta_n=\frac1{15n}+\frac{313}{14400n²}+O(n^{-3}),
\tag{MC-8}
\]

checked independently by symbolic series and derived by expanding the two elementary logarithms. In particular, the finite harmonic-renormalized sums `K_N=sum_(n≤N)[eta_n−1/(15n)]` are strictly increasing, absolutely convergent, and satisfy

\[
\boxed{0<K_\infty-K_N<\frac7{180N}\quad(N≥1).}\tag{MC-9}
\]

The executable `minimal_pole_gamma.py` gives **fully rational** upper/lower bounds for each log using the positive `atanh` series with a geometric remainder, then adds MC-9. This supplies genuine finite proof intervals without borrowing numeric high-precision evaluation as a universal proof.

## Theorem MC-03 — exact Euler–Gamma product on the native BBP clock

Put `w_n=exp(−eta_n)=(15/16)exp D(a_n)`. Then the logarithmic two-channel identity is equivalently

\[
\boxed{w_n=\frac{(n-1/2)(n-1/4)}{(n-5/24)(n-19/40)}}.
\]

Using only the recurrence `Gamma(z+1)=z Gamma(z)`, obtain the **exact finite** product

\[
\boxed{\prod_{n=1}^{N}w_n
=\frac{\Gamma(N+1/2)\Gamma(N+3/4)}{\Gamma(N+19/24)\Gamma(N+21/40)}
\frac{\Gamma(19/24)\Gamma(21/40)}{\Gamma(1/2)\Gamma(3/4)}.}\tag{MC-10}
\]

The classical Gamma ratio asymptotic, independently documented by NIST DLMF §5.11(iii), gives

\[
\prod_{n≤N}w_n\sim C\,N^{-1/15},\qquad
C=\frac{\Gamma(19/24)\Gamma(21/40)}{\Gamma(1/2)\Gamma(3/4)}.
\]

Since `H_N−log N→gamma`, the **exact source-dependent Euler finite part** is

\[
\boxed{K_\infty=
\log\frac{\Gamma(1/2)\Gamma(3/4)}{\Gamma(19/24)\Gamma(21/40)}-\frac\gamma{15}
=0.0522061421970575965121096958\ldots.}\tag{MC-11}
\]

The two positive components are independently meaningful:

\[
K_3=\log\frac{\Gamma(3/4)}{\Gamma(19/24)}-\frac\gamma{24},
\quad K_5=\log\frac{\Gamma(1/2)}{\Gamma(21/40)}-\frac\gamma{40},
\quad K_3+K_5=K_\infty.
\]

Numerical values (independent high-precision observations only): `K3≈0.01904860901811`, `K5≈0.03315753317895`; the sum is independently bounded by MC-9 with **rational endpoints**. At `N=128`, fourth-order `atanh` enclosures put `K_infty` strictly between `0.05203674351103067` and `0.05234056295547751` (decimal display of an exact rational enclosure); for larger N the bound contracts at rate `O(1/N)`.

This provides a precise discrete harmonic ↔ continuous Gamma completion based on the *real BBP forcing*, with no synthetic Gamma choice. It is classical Gamma mathematics specialized to this source, not a proof of the global selected digit dynamics.

## Oily–Macaroni and the golden parameter — two readouts, not a forced identity

From the original separately selected **two-stage Oily packet**, set `lambda=(sqrt5−1)/2`; its harmonic/Gamma readout is `Omega_OM=lambda−gamma`. The native reciprocal-log completion instead gives `15K_infty=15 log Gamma_ratio−gamma`. Their common `−gamma` cancels in the cross-comparison:

\[
\boxed{15K_\infty-\Omega_{OM}
=15\log\frac{\Gamma(1/2)\Gamma(3/4)}{\Gamma(19/24)\Gamma(21/40)}-\lambda
\approx0.74227380910750.}\tag{MC-12}
\]

**Not zero.** A rigorous sign witness does not require numerical Gamma evaluation: the fourth-order rational certificate `K_12>1/20` gives `15K_infty>3/4`, whereas `lambda<3/4` and `gamma>0` give `Omega_OM<3/4`. This refutes an accidental assertion that the two Oily constants must coincide. They are different source-rooted observables with an exact shared Euler part; their possible interaction with the *selected signed BBP phase* remains an open problem. Also, the numerator lives over `Q(sqrt241)` while the golden fixed point lives over `Q(sqrt5)`. The fields are different, and no algebraic identification is supplied.

## Theorem MC-04 — exact prime/2-adic unit-group bridge, but NOT whole-digit dynamics

The original centered pole pair satisfies `3·5=15=16−1`; its unit groups have identical cardinality and **abstract multiplicative structure**:

\[
\boxed{(\mathbf Z/15\mathbf Z)^\times\cong (\mathbf Z/3\mathbf Z)^\times\times (\mathbf Z/5\mathbf Z)^\times\cong C_2\times C_4\cong(\mathbf Z/16\mathbf Z)^\times.}
\tag{MC-13}
\]

An explicit all-eight-element isomorphism is obtained as follows. For a unit `x mod15`, let `epsilon` be 0 or 1 according as `x mod3` is 1 or −1, and let `k∈{0,1,2,3}` satisfy `2^k ≡x mod5`. Set

\[
f(x)=(-1)^{\epsilon}5^k\pmod{16}.
\]

Exactly 64/64 pairwise products are respected, and all eight group characters `(-1)^(u epsilon)i^(v k)` give an orthogonal basis. **This correspondence is not canonical**: it requires generator choices and does not extend to an isomorphism of the full 15- and 16-element rings, their additive successors, or their BBP radix evolution. The eight **nonunits** of the base-16 alphabet are not represented by the eight-unit bridge; they carry an essential part of any digit-normality test.

The bridge also has a precise hostile holdout. In the Fermat product tower, both `phi(255)=phi(256)=128`, but `(Z/255)^×` has exponent 16 and `(Z/256)^×` has exponent 64. They are **not** isomorphic. More generally, if `F_0,...,F_(k−1)` are prime, `2^(2^k)−1=prod F_j` has a unit group with `k` nontrivial cyclic 2-power factors, versus two factors for `2^(2^k)` when `k≥2`. At stage k=2 (`15↔16`) these are both `C2×C4`; at k=3 (`255↔256`) only the cardinality survives. See primary arithmetic background in Keith Conrad's *Fermat Numbers and Their Factors* and the elementary Chinese remainder theorem.

### Constructive extension — a COMPLETE 16-state Gaussian/2-adic observation chart

The preceding 8-unit isomorphism need not throw away half the digit alphabet. We can supply an exact **orthogonal basis of the full 16-state observation space** without claiming that this basis causes temporal mixing.

For each odd digit `d∈{1,3,...,15}`, use `f^(-1)(d)` to obtain `epsilon∈Z/2` and `k∈Z/4`. The eight unit characters are

\[
B_{u,v}(d)=(-1)^{u\epsilon(d)} i^{vk(d)},\qquad (u,v)\in(\mathbf Z/2)\times(\mathbf Z/4),
\]

and set `B_(u,v)(d)=0` on the even digits. For each even digit `d=2k`, `k∈{0,...,7}`, take the **eight 3-bit Walsh characters**

\[
W_j(2k)=(-1)^{\operatorname{popcount}(j\mathbin{\&}k)},\quad j=0,...,7,
\]

and set `W_j(d)=0` for odd d. Stack the eight unit rows and eight even rows into a Gaussian-integer matrix `B∈M_16(Z[i])`. CRT character orthogonality and the 8-by-8 Walsh–Hadamard identity prove

\[
\boxed{BB^*=8I_{16},\qquad f=\tfrac18 B^* (Bf)\quad\text{for EVERY }f:\{0,...,15\}\to\mathbf C.}
\tag{MC-13b}
\]

The source-adjacent outer prime information is thus packaged together with a **complete 2-adic even-digit sector**. There are no missing letters or lost one-digit observables. The executable `fermat_unit_bridge.py` uses exact Gaussian-integer pair arithmetic and checks all 256 Gram entries and exact reconstruction for a hostile nonconstant complex input vector. This is an algebraic chart change; it does **not** prove either simple normality of π's 16 digits or full base-16 block normality. Source-derived cross-time transition/carry constraints are still missing.

### Cross-source exceptional primes (independent algebraic passport)

The *same* authentic forcing has the exactly equivalent rational map in its integer clock variable `n`:

\[
R(8n-7)=\frac{A(n)}{D(n)},\quad
A(n)=120n²-89n+16,\quad
D(n)=(2n-1)(4n-1)(8n-7)(8n-3).
\]

An independent SymPy calculation of the **unchanged** polynomials yields

\[
\operatorname{Res}(A,D)=-2^{15}3²5²,\qquad
\operatorname{Disc}(D)=2^{24}3²5².
\tag{MC-14}
\]

So the exceptional reduction primes of this particular polynomial passport are exactly `2,3,5`, consistent with (but not derived by) the 3×5↔16 split. These discriminant/resultant facts are algebraic source fingerprints; generic prime 2/3/5 spectral or π-normality claims would require a separate theorem.

## Theorem MC-05 — logarithmic Oily twist cannot force signed Weyl cancellation

The product exponent has a tempting `1/15` information-decay rate. **This is a source-only scalar** and consequently cannot discriminate the original seed from the coherent same-forcing counterseed.

For every bounded complex sequence `|z_n|≤1`, and every `N≥1`, since `0<w_n<1` and `1-e^(−eta_n)≤eta_n`,

\[
\boxed{\left|\frac1N\sum_{n≤N}w_nz_n-\frac1N\sum_{n≤N}z_n\right|
\le\frac{H_N/15+7\pi²/1080}{N}=O(\log N/N).}\tag{MC-15}
\]

Thus this normalized source weighting has **exactly the same** limiting Weyl mean as the original selected orbit for every seed, including coherent nonnormal ones. This reproduces/strengthens the inherited scalar-representation firewall with a new explicit source weight.

Even the stronger-looking *accumulated complex logarithmic phase*

\[
A_n=\sum_{k≤n}\eta_k,\qquad V_n(c)=e^{icA_n}
\]

cannot kill coherence. For every fixed real `c`, the exact Gamma product gives `A_n=(log n)/15+C_Gamma+o(1)`, with `C_Gamma=log[Gamma(1/2)Gamma(3/4)/(Gamma(19/24)Gamma(21/40))]`. Therefore

\[
\boxed{\frac1N\sum_{n≤N}V_n(c)
=\frac{e^{icC_{Gamma}}N^{ic/15}}{1+ic/15}+o(1),
\quad\lim_{N\to\infty}\left|\frac1N\sum V_n(c)\right|=\frac1{\sqrt{1+(c/15)²}}>0.}\tag{MC-16}
\]

Proof: use the finite Gamma-ratio asymptotic and the Riemann sum `N^-1 sum (n/N)^(it) -> int_0^1 x^(it)dx=(1+it)^-1`. The same limit holds after multiplying by the **authentic coherent counterseed's** phase `exp(2π i h U_n(-π/16))`, which tends to 1 at rate `O_h(n^-2)` because `U_n(-π/16)=-T_n` and `T_n≤(8n+1)^-2`. With the seemingly natural `c=15`, the modulus tends **exactly `1/sqrt2`**, not zero. The logarithmic twist contributes a real new phase geometry but cannot prove normality by itself.

The actual still-open target is for the authentic **zero seed**

\[
N^{-1}\sum_{n≤N}\exp(2\pi i h U_n(0))\to0\quad\forall h\in\mathbf Z\setminus\{0\}.
\]

All source- or inversion-only identities are shared with the coherent `-π/16` counterseed. A further, source-authenticated **signed literal-carry / nonunit-sector / seed-zero** coupling with independently provable Fourier saving is required. The q=3 branch triangle inherited from #383 faithfully retains the orbit and is not itself a saving. Don't turn the 15↔16 group correspondence into a digit theorem without a full 16-state and inter-time transport.

## Actual reproduction and authority

- `minimal_pole_gamma.py`: source-parametric exact rational source, primitive minimization classifier, native log factors, finite Gamma-product identities, and **rational certified interval** for `K_infty`.
- `fermat_unit_bridge.py`: exact CRT unit-group isomorphism and finite characters, with hostile 255↔256 order classification.
- `test_minimal_pole_gamma.py` and `test_fermat_unit_bridge.py`: source mutation and full exact tests, including real zero-seeded BBP prefix rationals.
- `independent_oracle.py`: independent SymPy source/resultant/discriminant/gamma-rising/clock exact checks; imports neither implementation module.
- `numerical_holdouts.py`: high-precision Gamma ratio, Euler finite part and coherent logarithmic twist; these observations do not prove the universal statements.
- `VALIDATION.md` and raw receipts: actual commands, run counts and limitations. The universal claims above have full paper proofs separate from finite tests. **No Lean kernel proofs, native full-suite success, peer review or academic priority** are asserted for this additive branch.

External prior-art context: [NIST DLMF Gamma ratios](https://dlmf.nist.gov/5.11.iii), [NIST DLMF digamma/Euler](https://dlmf.nist.gov/5.7.ii), [Keith Conrad, Fermat Numbers and Their Factors](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/fermat-numbers-and-factors.pdf). Neither the π normality proof nor a physical information-minimality axiom is established here.
