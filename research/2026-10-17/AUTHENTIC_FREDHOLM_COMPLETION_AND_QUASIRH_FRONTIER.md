# Operation GAMMA-COMPLETION: source-certified finite Fredholm matrices and a repaired hidden fifth mode

**Date:** 2026-10-17. **Repository:** femboy2112/SUCC, independent research branch stacked on draft PR #160 @ `b9bb7324e7e7ccbc51e6fe3c5af61d08e238911e`. Original signed completed Suzuki source protected Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`. Original one real Gamma, correct contact, true prime-power 2 with half density, and BOTH completed pole channels remain intact. We do not use nontrivial zero coordinates, substitute new arithmetic weights or change the frozen source. **RH PROVED: NO; original full first-prime signed positivity OPEN.**

## C-01. Exact original finite Gamma and Fredholm feature reduction

At `a=1/2` in zero-exterior primitive coordinates `F=Vu`, the original signed finite-
Gamma source is

\[
H_J=(c_J-C_\infty)I-w(T_b+T_{-b})-K_J+2|c\rangle\langle c|-2|s\rangle\langle s|,
\quad b=\log2\in(1/2,1),\quad w=\log2/\sqrt2,
\quad c=\cosh(x/2),\ s=\sinh(x/2),
\]

with `c_J=sum_{j<J} 4/(4j+1)` and `K_J` the positive sum of `J` authentic OU Green operators having kernels `exp(-[4j+1]|x-y|/2)`. **J is a positive finite mode count; `H_infinity >= H_J` as a quadratic form** by source OU positivity. The first-prime partial shift `A_b=T_b+T_{-b}` satisfies `A_b^3=A_b` on the original continuum zero-exterior domain but not after arbitrary cell compression. In particular

\[
(\gamma I-wA_b)^{-1}=\gamma^{-1}I
 +\frac{w}{\gamma^2-w^2}A_b
 +\frac{w^2}{\gamma(\gamma^2-w^2)}A_b^2
\]

for `gamma>w>=0`. The two completed polar rank-one signs above are original.

Let `P_N` be actual orthogonal averaging on `N` equal cells (length `h=1/N`), and use the archived source derivation

\[
\|K_J-P_NK_JP_N\|\le\frac{2J}{\pi N}<\frac{2J}{3N}=:\varepsilon.
\]

Write `b∈[b-,b+]`, `w∈[w-,w+]`, `C∈[C-,C+]` as unchanged original SHA-verified source intervals. Choose the **exact rational** safe reference

\[
\bar w=(w_-+w_+)/2,\quad
\bar\gamma=c_J-C_+-\varepsilon-(w_+-w_-)/2,\quad
B_0=\bar\gamma I-\bar w A_b.
\]

Since `||A_b||=1`, the actual `B_J-epsilon I >= B_0`, and source parameters are tightly enclosed; `gamma>w` is checked, not assumed.

Use raw cell indicators `chi_i=1_{cell_i}` and two actual polar feature functions `c,s`, comprising `Phi=(chi_0,...,chi_{N-1},c,s)`. With normalized-cell OU matrix `M_ij=<chi_i/sqrt(h), K_J chi_j/sqrt(h)>`, source intervals `[Mlo,Mhi]` yield a **Loewner** majorant

\[
M\preceq M_{mid}+\rho I,\qquad
\rho=\max_i\sum_j(M_{ij}^{hi}-M_{ij}^{lo})/2.
\]

Define the rational symmetric feature-weight block

\[
D=\operatorname{diag}_{\rm block}
 \bigl(-N(M_{mid}+\rho I),\ +2,\ -2\bigr).
\]

The factor `N=1/h`, not `N²`, comes from the normalized-cell projection. Then the complete finite-rung signed source satisfies the **genuine-source** lower form

\[
H_\infty\succeq H_J\succeq B_0+\Phi D\Phi^*.
\tag{C1}
\]

Crucially **the signs are preserved**: first `N` negative OU feature weights, the positive cosh completed pole, the negative sinh completed pole, and both original contact/prime masses included in `B_0`. The surviving original infinite-Gamma remainder is POSITIVE, so no upper-tail subtraction is needed for a lower positivity certificate.

The full operator `B_0` is strictly positive and has the degree-two explicit inverse above. Its source feature Gram

\[
W=\Phi^*B_0^{-1}\Phi
\]

is an `(N+2)×(N+2)` symmetric matrix, with every entry a finite *outward rational interval*, computed from integrals of:

- cell overlaps and shifted cell overlaps under the TRUE irrational `log2` interval, not an integer-shift approximation;
- exact two-edge overlap from `A_b²=1_edges`;
- `chi_i` paired with authentic cosh/sinh polar channels, shifted and unshifted;
- source-exact squared polar integrals and cross parity; and
- the rational coefficients of the full cubic inverse.

Source exponential integrals use the protected series evaluation. The tiny irrational `b` enclosure width is explicitly paid using a conservative derivative Lipschitz bound; intervals are outward-rounded.

For a strictly positive `B_0`, the finite-feature equivalence is

\[
\boxed{B_0+\Phi D\Phi^*\succeq0
\iff \ W+WDW\succeq0.}\tag{C2}
\]

Indeed decompose the transformed Hilbert space into the span of `B_0^{-1/2}Phi` and its orthogonal complement, where the operator is the identity. This holds even for signed `D`. If `W` has a kernel, interpreting positivity on `Ran W` via the `W+WDW` quadratic is still valid, without assuming an unjustified inverse of `W`.

The implemented `authentic_fredholm_feature_gram(J=8,N=16)` constructs **all 324 interval entries of `W`, the entire signed `D`, and the rigorous finite matrix interval-error envelope** from the archived original source. This is an actual source-evaluated matrix, NOT a claimed positive Fredholm certificate. The current generic `J=8` sufficient test is expected to return `INCONCLUSIVE`: the source itself has certified negative low tests at this Gamma depth. Source tests refuse any fabricated `source_positivity_certified=True`.

Any eventual verified rational Loewner certificate `W+WDW >=0` at some actual `(J,N)` proves the FULL first-prime signed source nonnegative on every lawful smooth test at `a=1/2`, *without a Legendre compact zero-shift inverse*. This implication is sound and one meaningful certificate is enough for **this one radius**. The construction currently does not produce such a PSD certificate, let alone one uniformly over all radii.

## C-02. Genuine *fifth*-mode obstruction at the previously certified `J=64` four-mode crossing

Parent GB-08 proves the true four-low `A_(4,64)>0` and `A_(4,63)` is indefinite. **That does not mean `H_64>=0`.** A new exact integer-rational fifth-mode test reveals the next obstruction:

\[
 u=6P_1(2t)-10P_3(2t)+4P_5(2t)
   =3t(2t-1)(2t+1)(84t^2-19).
\tag{C3}
\]

Its endpoint traces vanish: `u(-1/2)=u(1/2)=0`. It is odd, hence genuine mean-zero, and belongs to `H^1_0(I)`; smooth compact tests approximate it in that norm.

Direct rational polynomial integration independently gives

\[
\boxed{\|u\|_2^2=2136/77,\qquad\|u'\|_2^2=1296.}\tag{C4}
\]

The *original*, unchanged source evaluator computes the six signed same-parity low entries for `(1,3,5)` at `J=64`. Its exact interval combination is

\[
Q_{64}(u)=36G_{11}+100G_{33}+16G_{55}
-120G_{13}+48G_{15}-80G_{35}.
\tag{C5}
\]

A strict negative upper endpoint is a bona fide **finite-Gamma truncated source** witness, not a negative witness of the complete Weil form. The executable adapter `authentic_fifth_mode_completion` FAILS unless it certifies that strict negativity against the frozen original source.

## C-03. Entire infinite Gamma tower returns the missing positive energy

Here we derive an **unconditional exact tail inequality for every endpoint-zero `u∈H¹_0(I)`**, not just the chosen source vector. The true omitted Gamma rung `d=4j+1`, `alpha=d/2`, has the exact full-line Fourier energy

\[
Q_{\Gamma,j}(u)=\frac{16}{d^3}
\int_{\mathbb R}\frac{|\widehat u(\xi)|^2}{1+4\xi^2/d^2}\,d\xi
\succeq \frac{16}{d^3}\|u\|_2^2
-\frac{64}{d^5}\|u'\|_2^2,
\tag{C6}
\]

by `1/(1+x)>=1-x` and Plancherel. The ordinary zero extension of `u` is in `H¹(R)` precisely because `u` vanishes at the endpoints. If that hypothesis is removed, the derivative norm of the zero extension need not be finite—an explicit negative control. The authenticated Gamma source coefficients here are those of **one real** Gamma completion, never a synthetic heat bath.

For `d_J=4J+1`, integral comparison of decreasing positive rational series gives

\[
\sum_{j\ge J}\frac{16}{(4j+1)^3}\ge\frac{2}{d_J^2},
\quad
\sum_{j\ge J}\frac{64}{(4j+1)^5}
\le\frac{4}{d_J^4}+\frac{64}{d_J^5}.
\]

Thus the complete infinite original positive Gamma remainder obeys the fully **finite rational** lower bound

\[
\boxed{
Q_{\Gamma,\ge J}(u)
\ge\frac{2}{d_J^2}\|u\|_2^2
-\left(\frac4{d_J^4}+\frac{64}{d_J^5}\right)\|u'\|_2^2.
}\tag{C7}
\]

For `(C3)` and `J=64`, this lower amount is exactly

\[
T_{64}^{lo}=
 \frac{2(2136/77)}{257^2}
 -\left(\frac4{257^4}+\frac{64}{257^5}\right)1296
 >\frac{838}{10^6}.
\tag{C8}
\]

The parent original-source Gamma upper bound remains

\[
T_{64}^{up}=\left(\frac2{257^2}+\frac{16}{257^3}\right)\frac{2136}{77}.
\tag{C9}
\]

**The decisive strict gate** is

\[
\boxed{Q_{64}(u)<0< Q_{64}(u)+T_{64}^{lo}\le Q_\infty(u).}\tag{C10}
\]

This is NOT an RH counterexample; the completed source positively repairs a hidden fifth-mode deficit. On local independent numeric diagnostics (not used as proof), `Q_64(u)≈-0.0007397`, and `Q_∞(u)≈+0.000113`. GitHub frozen-source CI determines whether the rigorous intervals actually verify both signs before marking C-02/C-03 source-proved.

**Why meaningful:** previous source first certified a 4×4 positive Gamma prefix at J64; this gives a transparent 5-dimensional obstruction *at exactly the same prefix*, together with a short, proof-producing infinite-Gamma completion whose net sign is opposite. It is not an arbitrary finite-matrix mutant, and it precisely locates where finite observational resolution gives the wrong all-test impression.

## C-04. Quasi-RH — rigorous certificate schema, NOT a one/two-step RH proof

For any rational first-prime radius `a` admitting the authentic source cut, a positive certified finite **Fredholm** packet `(J,N)` implies positivity of the complete original signed quadratic form on that fixed source window, by (C1)–(C2). The full Weil criterion requires positivity on *all* support radii. A sufficient meta-condition is

\[
\tag{QRH+}
\forall a\in\mathbb Q_{>0}\ \exists J,N<\infty:
\qquad [\text{original source-complete finite Fredholm packet at }a,J,N\text{ certifies strict PSD}].
\]

Under a rigorously generalized genuine prime-power tape and source Gamma/polar estimates at each radius, `(QRH+) => original Weil positivity => RH` (the latter is Suzuki/Weil's imported classical criterion). **This is a conditional QUASI-RH-style finite-proof schema, not an RH theorem.** Its universal premise is RH-hard and not supplied or established for any radius in this branch. At `a=1/2` even a successful finite certified `W+WDW>=0` is still pending. Existence of strict positive finite-rung packets at all radii could be stronger than RH in the presence of zero margins. It is scientifically misleading to say only one or two *easy* steps remain.

The alternative exact refutation semidecision is source-certified negativity: if RH were false and the classical distribution/test correspondence is effective, an actual negative compactly supported rational approximation eventually has a finite original Gamma-prefix upper-tail certificate. This is a computable *search principle* conditional on correct source evaluation, not the proof of nonexistence of such witnesses.

## C-05. Adversarial checks / provenance

1. **Wrong source**: reject foreign SHA, missing real Gamma, wrong prime2 tape and fake composite n=6.
2. **Wrong sign**: retain negative OU matrix and negative sinh pole with positive cosh pole in *actual* signed D, never invent a universal positive covariance.
3. **False `N²` cell factor**: correct feature weight for raw indicators is `N M`, where M is the *normalized* OU cell matrix.
4. **Source-interval algebra**: Gershgorin rational OU majorant and width of true log2 interval in every shifted feature; a zero-width rounding/symmetric source chart is not implicit.
5. **Endpoint trace**: Gamma-tail *lower* needs H¹ zero extension, unlike weaker upper bounds for arbitrary L² u.
6. **Truncated source negativity** is not original-source negativity; original Γ tail is **positive** and dominates selected fifth-mode finite deficit.
7. **Finite Gram negative** is inconclusive about actual original source since it is a sufficient lower packet; no false RH disproof.
8. **Source N/J budget**: original parent `gamma_cell_interval_matrix` has J<=40/N<=32 and auth archived source; adapter intentionally uses J8/N16 to keep independently auditably small matrix.
9. **Unbounded radius**: original module source tape valid only within declared radius; don't pretend an all-radius source detector is implemented.
10. **Independent mathematics**: exact polynomial norms, rational Gamma Fourier inequality, and local numerical diagnostics are independently written; GitHub SHA-pinned source arithmetic validates provenance but does not kernel-prove infinite distribution identities.

## C-06. Next decisive RH-facing mathematical step

Compute and certify an actual positive Fredholm packet for the **complete first-prime** signed source, not merely rank-five tests. Its `W+WDW` can be made significantly more efficient than O(N²) generic interval Gershgorin by using the true prime2 banded lag/phase geometry, parity block, and exact ODE Green factorization for each OU rung. At J~10³,N~10³ the observed low signed eigenvalues are near 10⁻⁶, so a generic `O(J/N)` K compression bound cannot close the sign; an eigenvector/residual certificate with *source-specific regularity* and positive high-sector bounds is required.

Even a source-certified strictly positive complete first-prime form would not prove Weil positivity at later prime thresholds. A noncircular **all-radius source transfer theorem** must also be found. That second requirement is not a small bookkeeping step: it currently contains RH-hard information.

**Claim status:** finite algebra EXACT; C-01 paper conditional on inherited certified K-cell norm error and archived source; C-02/03 source-adapter status determined by actual hosted CI; C-04 OPEN universal premise; **RH OPEN.** Main, import archives and original source unchanged. Draft non-main PR only.

### Exact source-hostile reference budget repair

The original initial hosted source gate rejected `J=8,N=8`: the generic compression allowance `2J/(3N)=2/3` EXCEEDS the first-prime positive cubic-swap baseline gap `~0.4135`, so no positive reference inverse is licensed. **This was a correct model failure, not a source positivity obstruction.** The guarded source adapter now requires `N>=14` and uses `N=16`, where `2J/(3N)=1/3` and the reference gap remains positive. A new explicit regression confirms that the underresolved N8 source packet is rejected. Positive Gram is still NOT assumed.

## C-06. A four-dimensional completed-source positivity theorem beyond the original four low modes [EXACT FROZEN-SOURCE GATE]

The one-vector C-03 certificate extends **uniformly over a four-dimensional linear family** of legitimate endpoint-zero mean-zero tests. Define

\[
U_{odd}=\operatorname{span}\{P_1(2t)-P_3(2t),\ P_3(2t)-P_5(2t)\},
\quad
U_{even}=\operatorname{span}\{P_2(2t)-P_4(2t),\ P_4(2t)-P_6(2t)\}.
\]

Every vector in both spaces is a true original test (or an H¹ limit of smooth compact tests) with zero endpoint traces and mean zero. Because the archived source is reflection invariant, mixed odd/even source entries vanish identically. Exact rational polynomial integration gives the **full** L² and derivative Grams, including cross terms:

\[
M_o=\begin{pmatrix}10/21&-1/7\\-1/7&18/77\end{pmatrix},\quad
D_o=\begin{pmatrix}20&0\\0&36\end{pmatrix},
\qquad
M_e=\begin{pmatrix}14/45&-1/9\\-1/9&22/117\end{pmatrix},\quad
D_e=\begin{pmatrix}28&0\\0&44\end{pmatrix}.
\]

Let `A_(J,sector)` be the original finite Gamma J signed two-by-two Gram on the pair of difference modes, computed **directly from six archive-authenticated complete signed source entries** in each parity. From the same Fourier source tail inequality (C7), on each whole sector we get the genuine **matrix Loewner lower**

\[
\boxed{A_{\infty,sector}\succeq
 A_{64,sector}+\frac2{257²}M_{sector}
  -\left(\frac4{257⁴}+\frac{64}{257⁵}\right)D_{sector}.}\tag{C11}
\]

The executable source adapter performs a **full outward rational 2×2 determinant test** for each sector: diagonal lower endpoints strictly positive and

\[
\boxed{\det_{lower}=L_{11}^{lo}L_{22}^{lo}-\max(|L_{12}^{lo}|,|L_{12}^{hi}|)^2>0.}
\]

If the exact original source passes these independent strict determinant inequalities, then

\[
\boxed{Q_{a=1/2}^{\mathrm{original},\Gamma_\infty}(u)>0
\quad\forall u\in U_{odd}\oplus U_{even}\setminus\{0\}.}\tag{C12}
\]

This tests true **mixed correlations**, not four unrelated positive diagonal readings. The fifth-mode witness (C3) lies in `U_odd` because
`6P1−10P3+4P5 = 6(P1−P3)−4(P3−P5)`.

**Independent numerical discovery (not the proof):** with the original Gamma/prime/contact/polar formula and 2,048 spatial cells, the smallest generalized low eigenvalue for `(C11)` at J64 is about `+1.5e-6` in the odd sector and `+2.5e-5` in the even sector. The authentic outward rational determinant checks are therefore genuinely nontrivial and fail closed if the source intervals are not sharp enough. No claim about directions orthogonal to these four vectors, 6a=1/2 complete operator, S4, arbitrary radius or RH follows.

This is the next meaningful finite-dimensional **quasi-RH laboratory**: a subspace where the entire infinite Gamma bath can be controlled with a short, source-faithful uniform Loewner proof rather than enumerated to infinity. Extending `(C11)` to a cofinal family of increasingly rich exact source subspaces with uniformly effective positive margins remains **OPEN and RH-hard**.

### Source-dimensional PSD oracle repaired (hostile audit)

The original parent `finite_gamma_fucc_fredholm.psd` explicitly rejects matrices larger than seven rows because it exhaustively checks **all** principal minors in its finite synthetic model. Feeding the 18-dimensional actual-source Fredholm packet to that bounded oracle would be a category/type error, not source negativity. We therefore independently implement exact rational **strict** LDL positivity (`strict_PD_fraction_gram`) for any finite symmetric square packet. Strict positive pivots are a SOUND sufficient Loewner certificate; nonpositive pivots return INCONCLUSIVE rather than a negative original-source witness. An exact test covers an 18×18 positive identity and adversarial indefinite/singular controls. The full source matrix is still computed at J8,N16 and remains a sufficient lower packet, not itself the original spectral operator.
