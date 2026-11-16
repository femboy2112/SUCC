# BBP causal-volume algebra: translation, source history and exact kernel bridge

**Date:** 2026-11-15. **Source baseline:** `e14d46c17a65e1e5f231c619657b9332caa181c0` (#635). **Status:** proved algebra within the domains below; bounded exact implementation checks. This is a source-specific assembly of classical mechanisms, with no scholarly priority claim. It supplies no estimate of cancellation in the selected BBP phase and no proof of normality.

The useful bridge is concrete: a power of the authentic rational forcing is a continuous convolution of its authentic positive lag kernel. The nominal expansion into `4^j` signed channel products reduces to at most `4j` exponential-polynomial basis functions. The arithmetic Green clock, continuous convolution lag, Gamma shape, and Mellin exponent retain separate types.

## 1. Source authentication and the new exact interface

Use the literal four signed channels

\[
(d_i)=(0,3,4,5),\qquad(c_i)=(4,-2,-1,-1),
\]

\[
R(a)=\sum_i\frac{c_i}{a+d_i}
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)},
\qquad r(n)=R(8n-7),\ n\ge1.
\]

The original BBP paper gives the signed series and its integral proof in Theorem 1, equations (1.2) and (1.4): [Bailey, Borwein and Plouffe, *On the rapid computation of various polylogarithmic constants*](https://www.davidhbailey.com/dhbpapers/digits.pdf). In this repository, the exponential source representation and its endpoint jets were already explicit in [OILY_MACARONI_SOURCE_MELLIN_HILBERT.md](../../2026-10-26/OILY_MACARONI_SOURCE_MELLIN_HILBERT.md), sections 2–3.

For real `t >= 0`, define

\[
Q(t)=4-2e^{-3t}-e^{-4t}-e^{-5t}
=2(1-e^{-3t})+(1-e^{-4t})+(1-e^{-5t}).
\]

Thus `Q(0)=0`, `Q(t)>0` for `t>0`, and

\[
Q(t)=15t-\frac{59}{2}t^2+\frac{243}{6}t^3+O(t^4).
\]

For `Re(a)>0`, termwise integration of the finite sum gives

\[
R(a)=\int_0^\infty e^{-at}Q(t)\,dt.
\tag{K1}
\]

### K2 — exact finite convolution reduction

**Claim, proved:** for every positive integer `j` and `Re(a)>0`,

\[
R(a)^j=\mathcal L[Q^{*j}](a),
\qquad
Q^{*j}(t)=\sum_{d\in\{0,3,4,5\}}\sum_{k=1}^j
C_{d,k}\frac{t^{k-1}e^{-dt}}{(k-1)!},
\tag{K2}
\]

where the rational coefficients are the unique principal-part coefficients

\[
R(a)^j=\sum_d\sum_{k=1}^j\frac{C_{d,k}}{(a+d)^k}.
\tag{K3}
\]

**Proof.** The product of the absolutely convergent Laplace integrals in (K1) can be integrated over the positive orthant, then grouped by the sum of the `j` lag variables. This is the standard convolution integral over a simplex. At each `-d`, `R` has a genuine simple pole of residue `c_d`; hence `R^j` has a genuine pole of order `j`. Its proper rational partial-fraction expansion has exactly the four possible pole locations and no polynomial part. Finally

\[
\int_0^\infty e^{-at}\frac{t^{k-1}e^{-dt}}{(k-1)!}\,dt
=\frac1{(a+d)^k}
\]

by the Gamma integral. Both kernels are continuous and of exponential order, so uniqueness of the Laplace transform gives their equality without a numerical inversion. The pole-order functions are linearly independent, because any zero linear combination would have a zero principal part at every pole.

The Gamma identity is [DLMF 5.9.1](https://dlmf.nist.gov/5.9#E1) with `mu=1`, `nu=k`, `z=a+d`; the required hypotheses are `Re(k)>0` and `Re(a+d)>0`. The monomial convolution rule is the Euler Beta integral [DLMF 5.12.1](https://dlmf.nist.gov/5.12#E1), with both Beta arguments of positive real part.

This is a change from exponentially many channel products to a linearly growing **basis**, not a claim that every basis coefficient is nonzero. In fact `C_(4,1)=0` when `j=2`. The highest coefficients are always `C_(d,j)=c_d^j`, so no source pole disappears. An integer convolution power is not the pointwise power `Q(t)^j`.

### K4 — exact origin cancellation

**Claim, proved:** the coefficients in degrees `0,...,2j-2` of `Q^{*j}` vanish, and

\[
Q^{*j}(t)=\frac{15^j}{(2j-1)!}t^{2j-1}
-\frac{59j15^{j-1}}{(2j)!}t^{2j}+O(t^{2j+1}).
\tag{K4}
\]

**Proof.** For nonnegative integers `m,n`,

\[
(t^m*t^n)(t)=\frac{m!\,n!}{(m+n+1)!}t^{m+n+1}.
\]

Convolving the first nonzero monomial `15t` in every factor gives the first term. For the next term, select `-(59/2)t^2` in exactly one of the `j` factors and `15t` in the others. All remaining terms have strictly higher total degree. This proves the cancellation to every integer order, rather than extrapolating from a finite jet table.

For example,

\[
\begin{aligned}
R(a)^2={}&\frac{16}{a^2}-\frac{134}{15a}
+\frac4{(a+3)^2}+\frac{34}{3(a+3)}\\
&+\frac1{(a+4)^2}+\frac1{(a+5)^2}-\frac{12}{5(a+5)},
\end{aligned}
\]

\[
Q^{*2}(t)=16t-\frac{134}{15}
+\left(4t+\frac{34}{3}\right)e^{-3t}
+te^{-4t}+\left(t-\frac{12}{5}\right)e^{-5t}
=\frac{75}{2}t^3+O(t^4).
\]

### Exact construction, budgets and controls

[bbp_gamma_kernel_algebra.py](../../../observational_succ/bbp_gamma_kernel_algebra.py) implements (K2)–(K4) with `Fraction` arithmetic and no production symbolic-algebra dependency. At pole `-d`, put `z=a+d` and write

\[
zR(z-d)=c_d+\sum_{m=1}^{j-1}
\left[\sum_{e\ne d}\frac{c_e(-1)^{m-1}}{(e-d)^m}\right]z^m
+O(z^j).
\]

Raise this truncated polynomial to power `j`; its coefficient of `z^(j-k)` is `C_(d,k)`. This follows because `R(z-d)^j=z^(-j)[zR(z-d)]^j`. Matching all principal parts leaves a rational function without finite poles; decay at infinity forces that difference to vanish.

The implementation accepts `1 <= j <= 12` and Taylor degrees `0 <= m <= 64`. Each expansion preserves all `4j` labelled slots, including zeros. A `GammaKernelPower` derives its terms from its power, rather than accepting unverified caller-supplied terms. Positive Laplace arguments must be exact Python integers or `Fraction` objects; floats and booleans are rejected. Power zero would require a delta distribution, outside this ordinary-kernel interface. The constructor uses `O(j^3)` rational operations and `O(j)` working coefficients per pole; bit costs still depend on the integer sizes.

Public interface:

```python
from fractions import Fraction
from observational_succ.bbp_gamma_kernel_algebra import source_kernel_power

kernel = source_kernel_power(2)
kernel.terms                    # eight labelled PoleTerm values
kernel.laplace(Fraction(7, 3))  # exact value of R(7/3)**2
kernel.taylor_coefficients(3)  # (0, 0, 0, Fraction(75, 2))
```

[test_bbp_gamma_kernel_algebra.py](../../../tests/test_bbp_gamma_kernel_algebra.py) deliberately uses different decompositions from the Laurent constructor:

- For every implemented power `1,...,12`, clear the complete rational denominator and compare global polynomial coefficients against the power of the literal original numerator.
- For all twelve powers, compare degrees `0,...,28` against direct Beta convolution of the literal original `Q` Taylor series. This independently covers all claimed origin cancellations and the next nonzero coefficient.
- Check six positive rational Laplace holdouts for each power: 72 exact comparisons. Check the known first and second expansions, all highest-pole residues, and the degree-64 source coefficient.
- Turn the signed residues positive, move a pole, and substitute a pointwise kernel square. Each mutation fails the relevant identity or cancellation. Exercise type, range, immutability and constructor guards.
- When available, independently run SymPy `apart` for powers `1,2,3,5`; these checks are optional and are not the only validation route.

**Observed local run:** `python -m unittest tests.test_bbp_gamma_kernel_algebra -v` passed all eight tests in 1.007 seconds, including the optional SymPy oracle. The finite run validates this implementation at its declared budget; the algebraic proofs above establish the unlimited-integer identities. This is not a report about the parent branch's full test suite or hosted CI.

### K5 — quantitative Gamma comparison, a classical source corollary

This section records a useful consequence without claiming that Gamma endpoint limits are new to the repository. The October 26 Mellin source work already proves the authentic shape-two endpoint limit, quantitative convergence, complex transport, and source-matched countermodels.

For real `t>=0`,

\[
0\le Q(t)\le15t,\qquad Q(t)\ge15t-\frac{59}{2}t^2.
\]

These follow by applying `1-e^(-x)<=x` and `1-e^(-x)>=x-x^2/2` to the four positive difference terms. Hence

\[
0\le Q^{*j}(t)\le\frac{15^j t^{2j-1}}{\Gamma(2j)}.
\]

Let `T_1,...,T_j` be independent with density `e^(-at)Q(t)/R(a)`, where `a>0`, and let `Y=a(T_1+...+T_j)`. Put

\[
h_a(y)=\frac{a^{2j-1}}{15^j}e^{-y}Q^{*j}(y/a),\qquad
Z=\left(\frac{a^2R(a)}{15}\right)^j.
\]

Then `integral h_a=Z`, the density of `Y` is `h_a/Z`, and
`0<=h_a(y)<=g_(2j)(y)=e^(-y)y^(2j-1)/Gamma(2j)`. The overlap integral of `h_a/Z` and `g_(2j)` is at least `Z`, yielding, with total variation defined as half the `L1` distance,

\[
d_{\rm TV}(\mathcal L(Y),\Gamma(2j,1))
\le1-Z\le\min\left(1,\frac{59j}{15a}\right).
\tag{K5}
\]

For the last inequality, set `z=a^2R(a)/15`. The source bounds give `0<z<=1` and `1-z<=59/(15a)`, while `1-z^j<=j(1-z)`. This is a probability law for explicitly independent lag variables. It does not identify them with successive selected BBP digits or with repeated observations of one retained hidden variable.

## 2. Graded finite Green algebra and the seed correction

Work over a commutative coefficient ring, with fixed integer origin `m`, and central grades `b,c`. Define the inclusive, zero-seed Green operator

\[
(G_b^m f)_n=\sum_{s=m+1}^n b^{n-s}f_s,\qquad n\ge m.
\]

No division by a grade is needed; powers with exponent zero are the ring unit. For `Y=G_b^m f`, `Z=G_c^m g`,

\[
YZ=G_{bc}^m(fZ+Yg-fg).
\tag{G1}
\]

**Proof.** Subtract `bc Y_(n-1) Z_(n-1)` from the product of
`Y_n=bY_(n-1)+f_n` and `Z_n=cZ_(n-1)+g_n`. Expressing the result in terms of the current states gives `f_nZ_n+Y_ng_n-f_ng_n`. The product's initial value is zero. Thus the recursion reconstructs it uniquely.

The term `-fg` removes the double counting of the inclusive equal-time event. For the BBP grade `b=c=16`, the product grade is `256`. Keeping grade 16 changes the recurrence.

This is exactly the **Rota–Baxter family identity of weight -1**, with grade multiplication as the semigroup law. It is not a new abstract identity: see Wang, Zhang, Zhu and Chen, [*Free nonunitary Rota-Baxter family algebras and typed leaf-spaced decorated planar rooted forests*](https://www.degruyterbrill.com/document/doi/10.1515/math-2020-0059/html), introduction equation (2). The repository already had the ungraded inclusive weight-minus-one identity in [summation_snapshot_arrows/README.md](../../2026-10-30/summation_snapshot_arrows/README.md), SA-04. The present practical extension keeps the changing grade, origin and source labels together.

For nonzero seeds `Y_m=y`, `Z_m=z`, formula (G1) must be corrected to

\[
YZ=(bc)^{n-m}yz+G_{bc}^m(fZ+Yg-fg).
\tag{G2}
\]

For finitely many factors `Y_i`, with grades `b_i` and forcings `f_i`, put `B=product b_i`. Inclusion-exclusion gives the finite rule

\[
\Delta_B\!\left(\prod_iY_i\right)
=\sum_{\varnothing\ne I}(-1)^{|I|+1}
\left(\prod_{i\in I}f_i\right)
\left(\prod_{i\notin I}Y_i\right),
\quad \Delta_B W_n=W_n-BW_{n-1}.
\tag{G3}
\]

Reconstruction adds `B^(n-m) product_i Y_i(m)`. This follows by expanding `product_i(Y_i-f_i)=B product_iY_i(n-1)`.

The corresponding homogeneous functions `H_b(n)=b^(n-m)` obey

\[
H_bH_c=H_{bc},\qquad H_bG_c^m(f)=G_{bc}^m(H_bf).
\]

For a **fixed** grade and origin, the decomposition

\[
Y_n=B^{n-m}Y_m+G_B^m(\Delta_BY)_n
\]

is unique as a seed/forcing representation of a sequence. This does not imply a unique symbolic expression across different grades, rational source identities, integrations and analytic continuations.

### Polynomial lifts

For `U_n=bU_(n-1)+r_n`, either of the following exact expansions can be used:

\[
U_n^k=b^kU_{n-1}^k+
\sum_{j=1}^k\binom kj b^{k-j}U_{n-1}^{k-j}r_n^j,
\]

\[
U_n^k=b^{k(n-m)}U_m^k+
G_{b^k}^m\left[\sum_{j=1}^k(-1)^{j+1}\binom kj r^jU^{k-j}\right]_n.
\tag{G4}
\]

The bridge to section 1 is now exact: every forcing factor `r_n^j` in these formulas can be evaluated as `Laplace[Q^{*j}](8n-7)`. The remaining `U` factors and Green chronology do not disappear under that substitution.

## 3. Formal word products: sound normalization and associativity

Let a word be empty, or `A=((b,f),A')`, where `b` belongs to a commutative grade monoid and `f` is a monomial in a commutative source alphabet. Interpret the empty word as `1` and a nonempty word as `G_b(f eval(A'))`. Work in the rational vector space freely spanned by these formal words.

For `A=((b,f),A')` and `B=((c,g),B')`, define recursively

\[
\begin{aligned}
A\star B={}&((bc,f),A'\star B)
+((bc,g),A\star B')\\
&-((bc,fg),A'\star B'),
\end{aligned}
\tag{W1}
\]

with the empty word as unit and bilinear extension. Each branch decreases the total operand length. This is a terminating recursive construction; it is sound under Green evaluation by (G1).

**Associativity proof by ordered blocks.** Tag the letters of every operand by its input chain. Form all ordered partitions of the tagged letters into nonempty blocks such that each chain appears in strictly increasing block order. Thus no block consumes two letters from the same chain. Immediately before a block, every unfinished chain has a current head. Output a letter whose grade is the product of **all current head grades**, and whose source monomial is the product of the letters **consumed in this block**. Give the resulting word the coefficient

\[
(-1)^{L-q},
\]

where `L` is the number of original letters and `q` the number of output blocks, then collect equal words.

For two input chains, the first block consumes the first head, the second head, or both, reproducing the three terms of (W1). For any parenthesization of several inputs, restriction of a global ordered partition to each grouped subset gives its inner partition; removing empty restrictions gives the outer partition. Conversely these nested partitions reconstruct the global partition uniquely. At each block, multiplication of all unfinished head grades and of the consumed monomials is unchanged by grouping. Collision signs multiply to `(-1)^(L-q)` because the inner block counts cancel. Therefore the collected formal-word polynomial is independent of parenthesization. Commutativity follows by permuting input chains, and the empty partition supplies the unit.

Equivalently, the length-sign map `w -> (-1)^len(w) w` converts (W1) to its positive-collision version. Both descriptions are finite algebra, not asymptotic or analytic claims.

**Normalization scope.** This proves associativity and deterministic product normalization in this presented formal word algebra. It does not prove that distinct collected polynomials remain distinct after substituting the actual four rational channels. For example, source partial fractions and specialized unit channels introduce further identities. No claim is made that this is a confluent decision procedure for every mixture of Green, Gamma, Ore, floor and analytic expressions.

**Observed finite corroboration:** a separate inline implementation checked all 2,197 associativity triples and 169 commutativity pairs among the 13 words of length at most two over the three letters `(2,x)`, `(3,y)`, `(5,z)`. It also checked 169 pairs for the weak-to-strict consecutive-block contraction map. These finite checks are implementation diagnostics; the ordered-partition argument is the universal proof. This inline diagnostic is not used as a published reproducibility receipt or as an independent source of mathematical authority.

## 4. Continuous order, Gamma shape and discrete collision are different

For continuous functions on an interval, fixed origin `m`, and real rates `lambda,mu`, let

\[
(J_\lambda f)(t)=\int_m^t e^{-\lambda(t-s)}f(s)\,ds.
\]

At finite `t>=m`, direct differentiation and the zero initial condition prove

\[
(J_\lambda f)(J_\mu g)
=J_{\lambda+\mu}(fJ_\mu g+gJ_\lambda f).
\tag{C1}
\]

The grade law is now rate addition, and there is no discrete collision term: the equal-time diagonal has zero two-dimensional Lebesgue measure. Nonzero initial conditions add the homogeneous product `exp(-(lambda+mu)(t-m)) y_m z_m`. The separable-kernel context is classical; [Guo, Gustavson and Li, *An algebraic study of Volterra integral equations and their operator linearity*](https://arxiv.org/pdf/2008.06756), Theorem 2.9, treats continuous separable kernels `K_omega(x,t)=k_omega(x)h_omega(t)` with nowhere-zero `k_omega` and common origin, as matching twisted Rota–Baxter operators. Their Example 2.12 includes the exponential kernel. Equation (C1) itself also follows from the displayed first-order differential equations.

Separately, tempered fractional kernels

\[
k_{\alpha,\lambda}(t)=\mathbf1_{t>0}\frac{t^{\alpha-1}e^{-\lambda t}}{\Gamma(\alpha)}
\]

obey `k_(alpha,lambda)*k_(beta,lambda)=k_(alpha+beta,lambda)` for positive real shapes and a common rate, by the Beta integral. This is composition in **shape**. It is not (C1), which is a pointwise-product identity for first-order Green integrals. For example, at origin zero, the untempered order-two integral has `I_2(1)=t^2/2`; its square is `t^4/4`, while `2 I_2(I_2(1))=t^4/12`. Thus one cannot impose the ordinary first-order shuffle identity on every fractional integral.

The finite four-pole expansion above concerns **integer convolution powers** of `Q`. It does not establish that arbitrary fractional powers of `R` have a finite pole basis, or that every putative fractional root is a positive source law.

## 5. Operational dictionary and boundary terms

| Object or operation | Exact translation | Domain / retained information |
| --- | --- | --- |
| `r(n)` | `R(8n-7)=Laplace[Q](8n-7)` | `n>=1`; continuous lag is not arithmetic time |
| `R(a)^j` | `Laplace[Q^{*j}](a)` | Positive integer `j`, `Re(a)>0`; signed coefficients retained |
| `a -> a+8` | Multiply the lag kernel by `exp(-8t)` | Actual BBP source-age shift |
| `-partial_a R` | `Laplace[tQ](a)` | `Re(a)>0`; differentiation justified by exponential decay |
| `aR(a)` | `Laplace[Q'](a)+Q(0)=Laplace[Q'](a)` | First boundary jet is zero |
| `a^2R(a)` | `Laplace[Q''](a)+15` | Second boundary contribution is nonzero |
| `G_bf G_cg` | `G_(bc)(fG_cg+gG_bf-fg)` | Common discrete origin, zero seeds |
| Continuous first-order integral product | Equation (C1) | Common continuous origin; no diagonal mass |
| Equal-rate Gamma-kernel composition | Add Gamma shapes | Positive shapes; continuous convolution |
| Pointwise observation products under an integral | Usually a product measure | A shared hidden variable and independently redrawn variables differ |

The shift algebra is an Ore algebra: with `(Ef)(n)=f(n+1)` and multiplication `M_f`,

\[
E M_f=M_{f(n+1)}E.
\]

For the source age, `T_8 M_a=M_(a+8) T_8`. The difference in operator order is essential. [Kauers, Jaroschek and Johansson, *Ore Polynomials in Sage*](https://arxiv.org/pdf/1306.4263), section 2, gives the general relation `Xa=sigma(a)X+delta(a)` for a ring endomorphism and a compatible sigma-derivation; its shift and derivative examples supply this standard context. These rules act on rational functions away from their poles. They do not justify dropping the boundary terms of causal inverses.

The rational logarithmic potential also has an exact Mellin bridge:

\[
\mathcal V(a)=\frac{a^4}{(a+3)^2(a+4)(a+5)},\qquad
\partial_a\log\mathcal V(a)=R(a),
\]

\[
F(s,a)=\int_0^\infty t^{s-1}e^{-at}Q(t)\,dt
=\Gamma(s)\sum_d c_d(a+d)^{-s}.
\tag{M1}
\]

Termwise Gamma integration first proves (M1) for `Re(s)>0`, `Re(a)>0`, with principal powers. The full combined integral is analytic for `Re(s)>-1` because `Q(t)=O(t)` at zero. The apparent pole at `s=0` is removable since `sum c_d=0`, and its value is

\[
F(0,a)=-\log\mathcal V(a),\qquad F(1,a)=R(a).
\]

The logarithm here is the analytic branch `sum_d c_d Log(a+d)` on the right half-plane; for real `a>0` it is the ordinary real logarithm. In that real domain this is also the convergent Frullani formula
`-log V(a)=integral_0^infinity e^(-at)Q(t)dt/t`. The repository already has source Frullani and Mellin mechanisms; this dictionary records their exact relation rather than claiming a new general Mellin theorem.

## 6. Inherited mechanisms that must not be rediscovered as new results

### Rational potential and marked first jet

[UNIVERSAL_N_PASCAL_GAMMA_ZETA.md](../../2026-10-30/universal_n_carrier/UNIVERSAL_N_PASCAL_GAMMA_ZETA.md), UN-06, already gives the potential `V`, its logarithmic derivative, and the exact finite Gamma quotient

\[
\prod_{n=1}^N\mathcal V(8n-7+u)
=\prod_i\left[\frac{\Gamma(N+q_i(u))}{\Gamma(q_i(u))}\right]^{c_i},
\qquad q_i(u)=\frac{1+d_i+u}{8},\quad u>-1.
\]

UN-09 also gives the radix-weighted carrier

\[
B_0(u)=1,\quad B_{N+1}(u)=B_N(u)^{16}\mathcal V(8N+1+u),
\quad U_N=\partial_u\log B_N(u)|_{u=0}.
\]

Its marked first jet is indispensable: multiplying the initial carrier by `1+su` preserves its value at zero and finite prime valuations there but changes the state by `16^Ns`. An unmarked scalar or valuation snapshot does not authenticate the original zero-seed state.

### Native q-Gamma radix blocking

[bbp_gamma_matrix_deformation/THEOREMS.md](../../2026-11-09/bbp_gamma_matrix_deformation/THEOREMS.md), SGM-05, already records

\[
P(x)=4-2x^3-x^4-x^5,\quad
K_g(x)=\sum_{j=0}^{g-1}16^{g-1-j}x^{8j}
=\frac{16^g-x^{8g}}{16-x^8}.
\]

For `g>=1`, `q=x^8/16`,

\[
K_g(x)=16^{g-1}\frac{1-q^g}{1-q}
=16^{g-1}\frac{\Gamma_q(g+1)}{\Gamma_q(g)},
\qquad
K_{g+h}=16^hK_g+x^{8g}K_h.
\]

The Gamma-ratio step is [DLMF 5.18.7](https://dlmf.nist.gov/5.18#E7). Here `0<=q<=1/16`; the endpoint `q=0` is read continuously. No native `q -> 1` limit occurs. This blocking algebra and the continuous-lag convolution algebra require their explicit displayed map; the presence of the word Gamma does not identify them.

### Carry retains its floor and chronology

With `x_n={U_n}` and `kappa_n=floor(16x_(n-1)+r_n)`,

\[
x_n=16x_{n-1}+r_n-\kappa_n.
\]

The block carry is

\[
C_{n,g}=\sum_{j=1}^g16^{g-j}\kappa_{n+j},\qquad
C_{n,g+h}=16^hC_{n,g}+C_{n+g,h}.
\]

These are inherited cocycle mechanisms: [finite_field_superposition_triangle/RESEARCH.md](../../2026-10-29/finite_field_superposition_triangle/RESEARCH.md), FFT-C, and [joint_carry_cocycle/PROOFS.md](../../2026-11-03/joint_carry_cocycle/PROOFS.md). A forcing-dependent carry is an integer and is not automatically restricted to the digit set `0,...,15`. Flooring after an average is generally different from averaging individual carries.

### Phase non-P-recursiveness is a corollary of existing prime birth

[pisot_gamma_gluing/PRIME_BIRTH_STRICTNESS.md](../../2026-11-02/pisot_gamma_gluing/PRIME_BIRTH_STRICTNESS.md), PG-09, already proves the decisive stronger local obstruction. At a prime birth `p=8b-7>5`, with `p` not dividing the nonzero integer frequency `h`, one has `U_b=4/p+B_b`; the complementary part and every previous `U_i` have denominators prime to `p`. Hence no rational linear relation with a nonzero coefficient of `e(hU_b)` can involve only these past phases.

For the elementary field input, [Keith Conrad, *Cyclotomic Extensions*](https://kconrad.math.uconn.edu/blurbs/galoistheory/cyclotomic.pdf), Theorem 2.5, gives the degree `phi(N)`; Theorem 3.4 gives the cyclotomic intersection rule. In particular, for `p` not dividing `M`, the relative degree of `Q(zeta_(Mp))` over `Q(zeta_M)` is `p-1`.

Thus an eventual finite-order phase recurrence over `Q(n)` is ruled out by taking a sufficiently late prime birth beyond the finitely many zeros and poles of its nonzero leading coefficient, then applying PG-09. Arbitrarily large primes `1 mod 8` can be supplied without a density theorem: the Fermat numbers `2^(2^k)+1` are pairwise coprime, and a prime divisor has `ord_p(2)=2^(k+1)`; for `k>=2` it is `1 mod 8`. This is an explicit consequence of the inherited prime-birth theorem, not a replacement for a source-selected phase-cancellation estimate.

## 7. Verdict and next discriminating use

**Disclosed within the stated mathematical domain:** the finite graded Green product and seed laws, formal-word associativity, the authentic four-pole convolution reduction, exact origin cancellations, and the quantitative independent-lag Gamma comparison. The core abstract mechanisms are classical; the runnable signed source-power interface is the concrete contribution of this file set.

**Observed:** the bounded implementation tests described above. Different algorithms constrain the same coefficients, but sharing the original source is intentional authentication, not independent experimental evidence.

**Still open:** whether these exact reorganizations produce a new useful bound on the selected zero-seed BBP phase, its carry correlations or normality. An all-order Gamma endpoint description alone cannot decide that question, and source perturbations preserving finitely many jets remain a control.

The next useful falsification target is a proposed source-dependent inequality after the polynomial Green lift: retain the full `U` and carry dependence, substitute the exact signed `Q^{*j}` forcing kernels, and test whether the claimed contraction survives coherent-seed and source-matched countermodels. A simplification that removes those distinguishing variables has changed the question.
