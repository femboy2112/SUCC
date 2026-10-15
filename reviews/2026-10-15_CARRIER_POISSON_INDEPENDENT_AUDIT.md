# Carrier-to-Poisson audit: compact quotient proof and normalization controls

**Date:** 2026-10-15. **Baseline audited:** `d239c27d3759de71de316180f48dfc097be6aff5`.
**Status:** internal mathematical reconstruction by a separate task agent; not independent peer review. Classical results, with explicit proofs and exact finite controls. No originality claim for adelic duality or Poisson summation.

The audit read `AGENTS.md`, `provenance/README.md`, `provenance/IMPORT_MANIFEST.json`, both October 15 Pontryagin/solenoid manuscripts, the existing hostile audit and claim supplement, and the Tate/Weil handoff. The founding import is pinned to `FuckingRH@ba075348b7bcc66d938b3e0ca96c26e95bba340a`; no imported or archival file is modified here.

## 1. Verdict and actual corrections

The six requested interfaces survive the reconstruction below, on their stated mathematical domains. The compact-quotient route proves Poisson without invoking ordinary real Poisson. It shares Haar normalization, rational reciprocity and real Schwartz Fourier theory with the existing coset route; these are not two statistically independent witnesses.

Two qualifications to the earlier text should be retained:

1. **A false necessity claim:** the AS-04 row in the earlier manuscript says rational scales, rather than integer scales alone, are necessary for spanning. Integer scales **with rational translates** already span. If `D=a/b>0` in lowest terms, then
   \[
   \mathbf1_{u+(a/b)\widehat{\mathbb Z}}
     =\sum_{j=0}^{b-1}\mathbf1_{u+(a/b)j+a\widehat{\mathbb Z}}. \tag{1.1}
   \]
   This is the disjoint decomposition of \(\widehat{\mathbb Z}\) modulo \(b\widehat{\mathbb Z}\), scaled by \(a/b\). For example, \(\tfrac12\widehat{\mathbb Z}=\widehat{\mathbb Z}\sqcup(\tfrac12+\widehat{\mathbb Z})\). Rational scales remain a useful native interface. **REFUTED:** their necessity for spanning. **PROVED:** their sufficiency and integer-scale sufficiency. Restricting both scales and translates to integers would fail.
2. **A compressed compactness argument:** a half-open fundamental domain is not itself compact. Use the continuous surjection from the compact set \([0,1]\times\widehat{\mathbb Z}\) to the quotient. The half-open set \([0,1)\times\widehat{\mathbb Z}\) supplies unique representatives and covolume, not compactness by itself. This repairs exposition, not the theorem.

There is also a source-convention distinction: Tate's 1950 thesis defines its basic additive character with real minus / finite plus, then uses its **conjugate** in the forward Fourier transform (Theorem 2.2.2). SUCC names the forward kernel itself \(\psi\), with real plus / finite minus. Thus the actual forward kernels agree. There is no mathematical sign defect here; the additive character and the chosen Fourier kernel must not be confused when importing formulas.

## 2. Objects, conventions and source provenance

Let
\[
 Z_f=\widehat{\mathbb Z}=\prod_p\mathbb Z_p,\quad
 A_f=\prod'_p(\mathbb Q_p,\mathbb Z_p),\quad A=\mathbb R\times A_f.
\]
Use the restricted-product topology, \(\operatorname{vol}(\mathbb Z_p)=1\), real Lebesgue measure, and
\[
 \psi(x)=\exp\!\left(2\pi i\left[x_\infty-\sum_p\{x_p\}_p\right]\right),
 \qquad \widehat f(y)=\int_A f(x)\psi(xy)\,dx. \tag{2.1}
\]
The principal-part sum is finite. For rational \(r\), elementary CRT gives \(\sum_p\{r\}_p-r\in\mathbb Z\), so \(\psi(r)=1\). Under this transform, inversion has **negative** character: \(f(x)=\int_A\widehat f(y)\psi(-xy)\,dy\).

The test space here is exactly the usual algebraic restricted tensor space
\(\mathcal S(A)=\mathcal S(\mathbb R)\otimes_{\rm alg}\mathcal S(A_f)\), where \(\mathcal S(A_f)=C_c^{\rm lc}(A_f)\). It is not all continuous functions on the completion or an arbitrary completed tensor product.

**Classical analytical dependencies:** Haar measure; Fourier theory on \(\mathbb R\), including preservation of its Schwartz space; compact-group character orthogonality; continuous-character duality of \(\mathbb R\); and the Stone–Weierstrass theorem (or, equivalently here, compact-group Fourier inversion with absolutely summable coefficients). No zero positions enter any object.

## 3. Reconstructing the carrier and its full dual

### Proposition A: principal parts and the compact quotient

The principal-part map \(\operatorname{pp}:A_f\to\mathbb Q/\mathbb Z\) has kernel \(Z_f\) and is onto. To check the kernel, multiply a finite sum of p-primary fractions by a common denominator and reduce modulo each of its prime-power factors; a nonzero p-primary summand cannot cancel the others. Diagonal rational representatives establish surjectivity. Hence
\[
 A_f=\mathbb Q+Z_f,\qquad \mathbb Q\cap Z_f=\mathbb Z. \tag{3.1}
\]
The open subgroup \(\mathbb R\times Z_f\subset A\) therefore maps onto \(A/\mathbb Q\), with kernel diagonal \(\mathbb Z\). The induced map
\[
 (\mathbb R\times Z_f)/\mathbb Z\longrightarrow A/\mathbb Q \tag{3.2}
\]
is a continuous open bijective homomorphism, hence a topological isomorphism. To avoid any unproved Hausdorff premise, observe first that \((-1/2,1/2)\times Z_f\) intersects diagonal \(\mathbb Q\) only at zero. Thus diagonal \(\mathbb Q\) is a discrete, closed subgroup of the Hausdorff topological group \(A\).

Every class has a unique representative in \([0,1)\times Z_f\). The image of \([0,1]\times Z_f\) covers the quotient, proving compactness. The half-open representatives have measure one, proving covolume one. Both assertions are topological/measure-theoretic conclusions, not point-counting experiments.

### Proposition B: every continuous character is a rational frequency

A continuous character of \(Z_f\) factors through some finite quotient: choose a circle neighborhood of one containing no nontrivial subgroup, pull it back under the character, and choose an open subgroup \(mZ_f\) inside the pullback. Its image is a subgroup in that neighborhood and therefore trivial. Characters of \(Z_f/mZ_f\cong\mathbb Z/m\mathbb Z\) have labels in \(\tfrac1m\mathbb Z/\mathbb Z\). Thus \(Z_f^\vee=\mathbb Q/\mathbb Z\).

A character of \(\mathbb R\times Z_f\) is
\(e^{2\pi i\lambda t}\chi_r(z)\), with \(\lambda\in\mathbb R\) and \(r\in\mathbb Q/\mathbb Z\). It kills diagonal \(\mathbb Z\) precisely when \(\lambda+r=0\pmod{\mathbb Z}\). Consequently \(\lambda=q\in\mathbb Q\) and \(r=-q\), giving all quotient characters
\[
 \chi_q([t,z])=\exp\bigl(2\pi i[qt-\operatorname{pp}(qz)]\bigr). \tag{3.3}
\]
The dual of a compact group is discrete, so \((A/\mathbb Q)^\vee\cong\mathbb Q_{\rm discrete}\). Character separation can also be checked directly: in the representative \(0\le t<1\), use frequency one if \(t\ne0\), and use a prime-power denominator detecting a nonzero residue of \(z\) if \(t=0\). This is not an algorithm with a uniform deadline for equality of arbitrary profinite programs.

### Proposition C: self-annihilator without assuming the quotient-dual answer

Suppose \(y=(y_\infty,y_f)\in A\) satisfies \(\psi(qy)=1\) for every rational \(q\). Choose rational \(r\) with \(y_f-r\in Z_f\), and subtract diagonal \(r\). This preserves the condition by rational reciprocity. Testing integer \(q\) now forces \(y_\infty-r=k\in\mathbb Z\). Subtract diagonal \(k\). The remaining point is \((0,z)\), \(z\in Z_f\).

If \(z_p\ne0\) for some prime \(p\), choose \(j\ge1\) with \(z_p\not\equiv0\pmod{p^j}\). At \(q=p^{-j}\), every other local component is integral, whereas the p-component contributes
\[
 \exp\bigl(-2\pi i(z_p\bmod p^j)/p^j\bigr)\ne1,
\]
a contradiction. Hence \(z=0\) and \(y\in\mathbb Q\). The reverse inclusion is rational reciprocity. Thus
\[
 \mathbb Q^\perp=\mathbb Q. \tag{3.4}
\]
This direct proof does not use the surjectivity of Pontryagin self-duality. To get the full \(A\simeq A^\vee\), restrict a finite-adèle character to \(Z_f\), remove a rational-multiplier character realizing that restriction, then identify the residual character of \(A_f/Z_f\cong\mathbb Q/\mathbb Z\) with a multiplier in \(Z_f\). Local nondegeneracy gives injectivity; standard compact-open duality gives the topology. Tensor with \(\mathbb R^\vee\cong\mathbb R\).

## 4. Reconstructing the complete finite test domain and Fourier transform

### Proposition D: uniform invariance and finite coset support

For \(g\in C_c^{\rm lc}(A_f)\), its nonzero set is closed as well as open (at any zero, local constancy gives a zero neighborhood), hence equals its compact support. Cover that support by finitely many cosets \(x_i+K_i\) on each of which \(g\) is constant, where every \(K_i\) is a compact open subgroup. Their intersection \(K\) preserves every such coset and its union, so \(g(x+k)=g(x)\) for all \(x\in A_f,k\in K\), including points off the support.

There is an integer \(d\ge1\) with \(dZ_f\subset K\): the restricted-product neighborhood basis imposes lower valuation bounds at only finitely many primes. The support meets finitely many cosets of \(dZ_f\), by compactness and discreteness of \(A_f/dZ_f\). From (3.1), \(A_f=\mathbb Q+dZ_f\), so each coset has a rational representative. This proves the desired finite rational-coset span, and the stronger integer-scale span in §1.

### Proposition E: amplitude, dual subgroup and phase

For any rational \(D>0\), rational product formula and additive Haar normalization give
\[
 \operatorname{vol}(DZ_f)=\prod_p |D|_p=D^{-1}.
\]
The annihilator of \(Z_f\) is itself: a nonintegral p-component is detected by the profinite projector supported at \(p\). Thus \((DZ_f)^\perp=D^{-1}Z_f\). Translation and compact-subgroup character orthogonality now give
\[
 \widehat{\mathbf1_{u+DZ_f}}(y)
   =D^{-1}\psi_f(uy)\mathbf1_{D^{-1}Z_f}(y). \tag{4.1}
\]
The Fourier phase is negative in the finite component under (2.1). This proof works at every finite-adèle argument, not only diagonal rational probes. At diagonal \(y=m/D\), the phase is \(e^{-2\pi ium/D}\).

For \(f=\varphi\otimes\mathbf1_{u+DZ_f}\), the previous manuscript's route is therefore correct:
\[
 \sum_{q\in\mathbb Q}f(q)=\sum_n\varphi(u+Dn),\qquad
 \sum_{q\in\mathbb Q}\widehat f(q)
   =D^{-1}\sum_m\widehat\varphi_+(m/D)e^{-2\pi ium/D}.
\]
Real Schwartz Poisson identifies these absolutely convergent sums. Finite tensor linearity covers the complete stated domain.

## 5. Second proof: compact quotient Fourier inversion, with quantitative tails

This route does **not** invoke ordinary real Poisson. Let \(f=\sum_{j=1}^J\varphi_jg_j\in\mathcal S(A)\), and define
\[
 P_f(x)=\sum_{q\in\mathbb Q}f(x+q). \tag{5.1}
\]
We prove all convergence and inversion premises explicitly.

### Lemma F: uniform absolute periodization on compact sets

Every compact subset of \(A_f\) lies in \(M^{-1}Z_f\) for some positive integer \(M\): these open subgroups form an increasing cover after passing to factorial denominators. Choose such \(M\) containing all \(\operatorname{supp}(g_j)\). On a compact set \(C\subset A\), choose \(L\in\mathbb N\) and \(R\ge0\) with \(x_f\in L^{-1}Z_f\), \(|x_\infty|\le R\) for every \(x\in C\). A nonzero summand requires \(q\in(ML)^{-1}\mathbb Z\). Write \(H=ML\) and
\[
 B_b=\sum_j\|g_j\|_\infty
          \sup_{t\in\mathbb R}(1+|t|)^b|\varphi_j(t)|<\infty,
 \qquad b>1.
\]
For integer \(N>2HR\), ordinary integral comparison gives the explicit bound
\[
 \sup_{x\in C}\sum_{|n|>N}|f(x+n/H)|
 \le \frac{2B_b(2H)^b}{b-1}N^{1-b}. \tag{5.2}
\]
Indeed \(|x_\infty+n/H|\ge |n|/(2H)\) in this tail, and \(\sum_{n>N}n^{-b}\le N^{1-b}/(b-1)\). Equation (5.2) proves local uniform absolute convergence; \(P_f\) is continuous and rational-periodic and descends to the compact quotient.

By Proposition E and real Schwartz Fourier theory, \(\widehat f\in\mathcal S(A)\). The same lemma at \(C=\{0\}\) gives
\[
 \sum_{r\in\mathbb Q}|\widehat f(r)|<\infty. \tag{5.3}
\]
Thus the candidate inverse Fourier series below converges uniformly and absolutely on the whole quotient. Its tail can be bounded by (5.2) applied to a finite tensor decomposition of \(\widehat f\). These are genuine seminorm-controlled approximation bounds, not inferred from sampled agreement.

### Lemma G: unfolding identifies every Fourier coefficient

Let \(F_0=[0,1)\times Z_f\), a measure-one fundamental domain, and \(r\in\mathbb Q\). Since \(f\in L^1(A)\), the identity
\(\int_{F_0}\sum_q|f(x+q)|\,dx=\int_A|f|\,dx<\infty\)
justifies unfolding. Rational reciprocity gives
\[
 \begin{aligned}
 c_r&=\int_{A/\mathbb Q}P_f(x)\psi(rx)\,dx\\
 &=\sum_q\int_{F_0}f(x+q)\psi(rx)\,dx\\
 &=\int_A f(z)\psi(rz)\,dz=\widehat f(r).
 \end{aligned} \tag{5.4}
\]
The change of variable uses \(\psi(rq)=1\); this is exactly the source arithmetic condition a wrong single-place phase loses.

### Proposition H: inversion and Poisson

Set
\[
 H_f(x)=\sum_{r\in\mathbb Q}\widehat f(r)\psi(-rx). \tag{5.5}
\]
It is continuous by (5.3). Character orthogonality shows its plus-convention Fourier coefficient at \(r\) is \(\widehat f(r)\), just as for \(P_f\). Their difference therefore has every Fourier coefficient zero. Characters (3.3) separate quotient points, form a conjugation-stable algebra, and include constants. Stone–Weierstrass makes their finite span uniformly dense in the continuous functions on the quotient. Approximate the conjugate of the difference by such finite sums to obtain that its squared \(L^2\)-norm is zero. Continuity then gives \(P_f=H_f\) everywhere.

At \(x=0\),
\[
 \boxed{\sum_{q\in\mathbb Q}f(q)=\sum_{q\in\mathbb Q}\widehat f(q)}. \tag{5.6}
\]
Both sums are absolutely convergent. More strongly, (5.5) is the full translated Poisson formula. The inverse sign in (5.5) is necessary; setting \(x=0\) alone cannot test it.

**Independence boundary:** the coset proof uses ordinary real Poisson; the quotient proof uses compact-quotient Fourier uniqueness. Both use the same arithmetic carrier and Haar measure. Same-model reviews and shared source assumptions must not be counted as independent experimental confirmation. These are two mathematical dependency routes, not a probability-of-truth calculation.

## 6. Hostile receipts and execution boundary

`tests/test_carrier_poisson_audit.py` checks the following finite consequences exactly, reusing existing SUCC source and cyclotomic implementations:

| Mutation or claim | Decisive finite receipt | What remains analytic |
| --- | --- | --- |
| Noninteger scales are necessary | Equation (1.1), including nonrational profinite-projector points; exact Fourier refinement | Universal statement follows from quotient decomposition, not test count |
| A positive inverse Fourier sign is harmless | On a translated delta in \(\mathbb Z/5\mathbb Z\), it reconstructs the reflected point | Full quotient inversion needs (5.2)–(5.3) |
| Real plus / finite plus preserves rational reciprocity | \(q=1/3\) has total phase \(2/3\), rather than zero | No analytic estimate needed |
| Omitting prime 3 is harmless | At \(q=1/3\), no remaining finite place cancels real phase \(1/3\) | No analytic estimate needed |
| The dual subgroup is \(DZ_f\) | \(D=2,y=1/2\) belongs to the true annihilator but not the mutant | No analytic estimate needed |
| Any represented profinite point can be uniformly zero-tested | Any finite prime-power query horizon misses a projector at a fresh prime | No universal deadline follows from character separation |

The new tests do not numerically approximate an infinite adelic sum. Existing rigorous Gaussian interval tests remain the receipt for an incorrect Haar multiplier. Analytic theta/Mellin continuation and signed Weil identification are separate tasks; none is proved by the additive Poisson identity alone.

**Observer-relative statement:** the completed carrier admits mathematical duality and a finite symbolic proof of Poisson. Given a finite test presentation and explicit Schwartz seminorm bounds, (5.2) is a quantitative truncation procedure. An arbitrary Schwartz function with no effective bounds is not automatically a computational input. Arbitrary completed profinite points need not have finite names. None of these statements classifies RH as SimpleField, IdealHardField or FuckedField.

## 7. Sources actually checked and reproducibility

- **Original primary source:** John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, 1950 thesis, [Rutgers-hosted scan](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf), §2.2 (additive convention); §§4.1–4.2 (carrier, self-annihilator, compact quotient); Lemmas 4.2.2–4.2.4 (inversion, periodization and Poisson). Relevant scan pages 10 and 40–42 were rendered for sign/formula inspection. Historical attribution belongs here. This audit rewrites the proofs in the rational case and supplies its own bound (5.2).
- **Author-hosted contemporary exposition:** Bjorn Poonen, [*Tate's Thesis*](https://math.mit.edu/~poonen/786/notes.pdf), 2015, §§5.4–5.5, Lemma 5.6 and Theorem 5.7. Inspected the periodization and unfolding premises, with PDF pages 28–30 rendered. This is a modern exposition of the same classical theorem, not separate mathematical provenance for Tate's result.
- Jordan Bell, [*The Pontryagin duals of Q/Z and Q and the adeles*](https://jordanbell.info/LaTeX/mathematics/Qdual/Qdual.pdf), author-hosted derivation, consulted for the duality conventions. The present rational-frequency classification and direct annihilator proof are written out above.

```sh
python -m unittest discover -s tests -p 'test_carrier_poisson_audit.py' -v
```

**Observed validation:** the command above completed with all **6 tests passing** on 2026-10-15 (Python runtime supplied by this workspace). Parent-task provenance/full-suite/CI receipts remain separate; this note does not infer any GitHub CI result.

**Next falsification opportunity:** carry the fixed inverse phase and conductor-sensitive finite coset maps through an odd primitive character. A centered even Gaussian alone cannot expose a conjugation mistake that reflection hides. This is precisely why chi4 is a necessary next normalization crucible.

RH PROVED: NO
