# The original Gamma tail has a retained Laplacian and explicit endpoint layers

**Date:** 2026-10-18. **Parent:** PR177 at `f309d910`, following PR174 and PR171. **Frozen original source Git blob:** `0cc8510b71d178fc79e8d410a86d8b6014cf9178`. The original source files are unchanged. **Verdict:** a proved source-specific tail lemma and exact rational implementation; the tested first-window S4 sign remains **OPEN**. RH is not proved.

This lane studies a genuine analytic obstruction in `ORIGINAL_CONTINUUM_RESIDUAL_SCHUR.md`: treating the whole missing Gamma action as an error discards its leading differential response. We retain that response and account explicitly for the endpoint layers. The resulting remainder is smaller on all four parent-fitted J24 trial vectors. Nevertheless, the complete signed Schur lower becomes worse. This distinguishes uncertainty reduction from an improved positivity certificate.

## 1. Exact theorem, including the actual domain

Let I=(-1/2,1/2), a=1/2, and let h be real-valued in H^4(I) with h(±a)=h'(±a)=0. The second and third endpoint derivatives need **not** vanish. For each authentic original real-Gamma rung set

\[
d_j=4j+1,\quad \alpha_j=d_j/2,\quad
(E_\alpha h)(x)=\int_I e^{-\alpha|x-y|}h(y)\,dy,
\quad \Gamma_j=\frac4{d_j}I-E_{\alpha_j}.
\]

Write S_p(J)=sum_{j>=J}d_j^{-p}, a_J=16 S_3(J), and Gamma_tail,J=sum_{j>=J} Gamma_j, with the same original normalization as PR177. For J>=1:

\[
\boxed{\quad \Gamma_{\mathrm{tail},J}h=-a_Jh''+\mathcal R_Jh.\quad}
\tag{GTR-1}
\]

Define d=4J+1 and, for real u,v,

\[
N_J(u,v)=\sqrt{u^2+v^2+2\max(uv,0)\,d e^{-d/2}}.
\]

Then the following bound holds in the **entire continuum L²(I)**:

\[
\begin{aligned}
\|\mathcal R_Jh\|_2\le{}&
8N_J(h''(-a),h''(a))\sqrt{S_3(J)S_4(J)}\\
&+16N_J(-h'''(-a),h'''(a))\sqrt{S_4(J)S_5(J)}\\
&+64S_5(J)\|h''''\|_2.
\end{aligned}
\tag{GTR-2}
\]

For each fixed h, the leading endpoint term is O(J^(-5/2)), the next endpoint term is O(J^(-7/2)), and the bulk term is O(J^(-4)). For h in H^4_0(I), both endpoint terms vanish. This is a statement about the original Gamma action; it does not make the contact, prime or polar channels positive.

For complex-valued h, the same theorem holds with the squared endpoint norm replaced by `|u|^2+|v|^2+2 max(Re(u conjugate(v)),0) d exp(-d/2)`. The implementation uses real rational polynomial basis vectors. Its real symmetric Loewner matrix certificates extend to complex coefficients by splitting a coefficient vector into real and imaginary parts; no complex endpoint formula is silently inferred from `uv`.

**Proof.** Twice integrating by parts in y gives, for a sufficiently regular f,

\[
E_\alpha f=\frac2\alpha f+\frac1{\alpha^2}E_\alpha f''
-e^{-\alpha(x+a)}\left(\frac{f(-a)}\alpha-\frac{f'(-a)}{\alpha^2}\right)
-e^{-\alpha(a-x)}\left(\frac{f(a)}\alpha+\frac{f'(a)}{\alpha^2}\right).
\]

Apply this first to h, whose first two traces vanish, then to h''. It yields the exact identity

\[
\begin{aligned}
\Gamma_jh={}&-\frac{16}{d_j^3}h''-\frac{16}{d_j^4}E_{d_j/2}h''''\\
&+e^{-d_j(x+a)/2}\left(\frac8{d_j^3}h''(-a)-\frac{16}{d_j^4}h'''(-a)\right)\\
&+e^{-d_j(a-x)/2}\left(\frac8{d_j^3}h''(a)+\frac{16}{d_j^4}h'''(a)\right).
\end{aligned}
\tag{GTR-3}
\]

Young's convolution inequality gives ||E_{d_j/2}||<=4/d_j; hence the bulk norm is bounded by 64 S_5(J)||h''''||. For an endpoint pair,

\[
\|u e^{-d_j(x+a)/2}+v e^{-d_j(a-x)/2}\|_2^2
=\frac{u^2+v^2}{d_j}(1-e^{-d_j})+2uv e^{-d_j/2}
\le\frac{N_J(u,v)^2}{d_j}.
\]

The last inequality uses that t e^{-t/2} decreases for t>=d>=5. It retains the benefit of opposite endpoint signs without assigning an imaginary phase. Finally,

\[
\sum_{j\ge J}d_j^{-7/2}\le\sqrt{S_3S_4},\qquad
\sum_{j\ge J}d_j^{-9/2}\le\sqrt{S_4S_5}
\]

by Cauchy–Schwarz. Summing the norm-convergent terms proves (GTR-1)–(GTR-2). Sobolev approximation extends the integration-by-parts identity to the stated domain. In the executable certificate h is an exact polynomial, so no numerical domain inference occurs. ∎

## 2. Rational enclosure and the whole signed source

The new module `observational_succ/gamma_tail_resolvent_refinement.py` evaluates exact polynomial norms and traces. For p=3,4,5 it encloses S_p(J) by a 256-term rational sum plus the elementary integral bounds

\[
\int_{J+N}^\infty(4t+1)^{-p}dt
\le\sum_{j\ge J+N}(4j+1)^{-p}
\le\int_{J+N}^\infty(4t+1)^{-p}dt+(4(J+N)+1)^{-p}.
\]

Each finite summand is rounded **outward** to the declared 10^-24 rational grid. The entire rounding cost is paid. An upper enclosure of e^(-d/2) is the reciprocal of a finite positive Taylor sum for e^(d/2). Square roots use the parent's upward rational square-root routine. Thus the code has rational enclosures, not floating proof inputs; the displayed decimals below are summaries.

If [a_lo,a_hi] encloses a_J, the midpoint action -a_mid h'' is retained and an additional error ((a_hi-a_lo)/2)||h''|| is charged. This is essential: an approximate coefficient is not silently used as the exact infinite sum.

The full original finite source action remains exactly the parent expression

\[
H_Jh=(\sum_{j<J}4/d_j-C_\infty)h-\sum_{j<J}E_{d_j/2}h
-w A_{\log2}h+2\langle\cosh(x/2),h\rangle\cosh(x/2)
-2\langle\sinh(x/2),h\rangle\sinh(x/2).
\]

There is one real Gamma, the original contact, **both opposite polar signs**, and true prime-2 weight w=(log2)/sqrt2. The new wrapper rejects any parameter dictionary differing from the authenticated original values and provenance. Neither a covariance surrogate nor nontrivial zero positions enter construction.

The parent exact three-piece polynomial approximant p_J is replaced by

\[
\widetilde p_J=p_J-a_{\mathrm{mid}}h'',\qquad
\|H_\infty h-\widetilde p_J\|_2\le\epsilon_{\mathrm{finite}}+\epsilon_{\mathrm{GTR}}.
\tag{GTR-4}
\]

All projection and integration remain in the original primitive L² space, with Q_E=I-Pi_{degree<=3}. No discrete spatial norm replaces that continuum norm.

## 3. Tail energy and original Schur lower

The independent Fourier multiplier inequality

\[
\frac{16\xi^2}{d(d^2+4\xi^2)}
\ge\frac{16\xi^2}{d^3}-\frac{64\xi^4}{d^5}
\]

gives, for every linear combination of lawful trial polynomials,

\[
q_{\Gamma,\mathrm{tail}}(h)\ge a_{\mathrm{lo}}\|h'\|_2^2
-b_{\mathrm{hi}}\|h''\|_2^2,\qquad b_{\mathrm{hi}}\ge64S_5(J).
\tag{GTR-5}
\]

The code uses this **whole 2x2 Loewner lower** only if it is PSD; otherwise it uses the independently valid zero tail lower. It does not take the positive part of an indefinite matrix.

With the inherited source-conditional all-high coercivity kappa=63/500 or 153/500, the same variational identity and Young inequality as PR177 give

\[
S_4|_\pi\ge A_{J,\mathrm{mid}}-\operatorname{diag}(\text{row radii})+T_J
-\frac{1+\eta}{\kappa_\pi}\widetilde M
-\frac{1+1/\eta}{\kappa_\pi}\Big(\sum_i\epsilon_i^2\Big)I,
\tag{GTR-6}
\]

where tilde-M is the exact full-continuum Gram of Q_E tilde-p_i. The new lemma does not reprove the inherited all-high coercivity. Conclusions using (GTR-6) inherit that hypothesis. Exact 2x2 principal-minor checks determine the reported certificate sign. A negative lower remains **AMBIGUOUS**, not a negative original Weil witness.

## 4. Paired results: smaller error is not automatically a better Schur lower

For a fair comparison, both routes use **identical parent-fitted coefficients**, identical exact source J, identical Taylor budgets M=(80,128,184), identical original q_J intervals, and eta=1/4. The parent route fits before seeing the retained-tail residual. All displayed entries are rounded views of rational certificates.

| J | Derivative parity | Parent lower diagonal | Retained-tail lower diagonal | Verdict |
|---:|---|---|---|---|
| 8 | odd | (-0.0274289870, -0.0269724582) | (-0.1719638497, -0.1686942472) | AMBIGUOUS |
| 8 | even | (-0.0127028756, -0.0122454410) | (-0.5473225459, -0.5455037618) | AMBIGUOUS |
| 16 | odd | (-0.0021816843, -0.0018372468) | (-0.0025014972, -0.0017923257) | AMBIGUOUS |
| 16 | even | (-0.0022378006, -0.0019154606) | (-0.0040707773, -0.0036532618) | AMBIGUOUS |
| 24 | odd | (-0.0009810781, -0.0005687345) | (-0.0010839771, -0.0005289661) | AMBIGUOUS |
| 24 | even | (-0.0012647738, -0.0009414402) | (-0.0014750548, -0.0011165478) | AMBIGUOUS |

At J24 the paired matrices are approximately

\[
L_{\mathrm{parent,odd}}=\begin{bmatrix}-.0009810781&-.0004125703\\-.0004125703&-.0005687345\end{bmatrix},\quad
L_{\mathrm{retained,odd}}=\begin{bmatrix}-.0010839771&-.0006595336\\-.0006595336&-.0005289661\end{bmatrix},
\]

\[
L_{\mathrm{parent,even}}=\begin{bmatrix}-.0012647738&-.0008437744\\-.0008437744&-.0009414402\end{bmatrix},\quad
L_{\mathrm{retained,even}}=\begin{bmatrix}-.0014750548&-.0011349593\\-.0011349593&-.0011165478\end{bmatrix}.
\]

The parent fitted coefficients at J24 are (197/4096,118/4096) and (222/4096,208/4096). The four action error budgets change as follows (the finite-source approximation error is negligible at the shown precision):

| Original low index | Parent omitted-tail bound | Retained-tail remainder bound |
|---:|---:|---:|
| 1 | 0.0022661213 | 0.0012557913 |
| 3 | 0.0016385007 | 0.0008115250 |
| 2 | 0.0029144471 | 0.0022748071 |
| 4 | 0.0025376531 | 0.0019497292 |

The new nominal continuum residual includes the actual leading Gamma response. That response increases the projected Gram enough that the reduced uncertainty does not compensate. This is a concrete counterexample to the proposed *certificate heuristic* “smaller tail error necessarily improves the original signed Schur lower.” It is not a counterexample to positivity or to the variational identity.

An additional **fit**, not a holdout, minimizes the retained-tail projected residual in the same one-correction family. At J24 its worst diagonal is about -0.0014592522 (odd diagonal pair -0.0010718702,-0.0005247282; even -0.0014592522,-0.0011011718), still AMBIGUOUS. J8 and J16 were also tested and remained AMBIGUOUS. No favorable selection is presented as independent validation.

## 5. Calibration, adversaries and reproducibility

The new tests independently check the exact OU ODE and both Robin endpoint conditions, then check (GTR-3) coefficient by coefficient against a full finite polynomial/exponential resolvent decomposition. Reversing the left third-derivative sign fails this identity. H²-clamped examples with nonzero h'' and h''' traces incur nonzero endpoint costs; H⁴-clamped examples have exactly zero endpoint costs. Non-clamped primitives, floats, invalid shells and altered source parameters fail closed.

A fresh unfitted primitive h=(1-4x²)^4 provides two held-out original-source checks:

1. At J=7, the entire original signed pairing from the archived exponential/Legendre integrator intersects the independently bounded finite piecewise-polynomial action pairing, including Gamma/contact/prime/both poles.
2. The original J=13 to J=23 Gamma shell difference intersects the retained-Laplacian prediction with the proved remainder budget. Omitting the leading Laplacian or reversing its sign produces disjoint intervals and is rejected.

These use a different analytical implementation of the same frozen source. They establish method diversity, not independent source provenance. The polynomial and shell depths were not fitted in the J8/J16/J24 comparison.

Commands:

```sh
python -m unittest tests.test_gamma_tail_resolvent_refinement -q
python scripts/gamma_tail_resolvent_refinement_probe.py --source --verify
python scripts/gamma_tail_resolvent_refinement_probe.py --source --verify --compare --output gamma-tail-resolvent-full.json
```

The default probe is small; `--compare` explicitly requests the more expensive paired signed source calculations. The output file contains the full rational certificates, not merely the displayed decimals. The first-window sign stays OPEN unless both source parity certificates actually pass; RH remains unproved even if a bounded first window eventually passes.

## 6. Claim ledger and remaining obstruction

| Claim | Status | Boundary and next falsifier |
|---|---|---|
| GTR-1–3 original tail resolvent identity and endpoint bound | DISCLOSED: paper proof, exact polynomial checks | H⁴(I)∩H²_0(I), one original real Gamma; test a different smooth clamped family |
| GTR-4 rational full-source residual enclosure | DISCLOSED within inherited finite-source adapter | Exact original contact/prime/two-pole source; fresh full-source holdout required after adapter change |
| GTR-5 whole-span authentic tail energy lower | DISCLOSED: multiplier derivation | Loewner inequality on H²_0; no positive-part clamping |
| GTR-6 Schur lower | CONDITIONAL on inherited source all-high kappa theorem | Does not establish that theorem or any all-window positivity |
| Smaller J24 tail remainder on all four parent-fitted columns | OBSERVED, exact finite scope | Does not imply a smaller full projected residual |
| First-window S4 positivity | UNVERIFIED / OPEN | Every tested complete lower fails to certify; no negative original witness |
| Novel general operator theory | NOT CLAIMED | OU resolvent integration and Schur algebra are classical; contribution is the audited source-specific endpoint lemma and negative experiment |

The live obstruction is now sharper: a generic tail norm was not the only cost. The true leading tail response moves the residual in an unfavorable direction for these fitted trials. A verdict-changing next probe would use a larger boundary-controlled high response family and optimize a **signed variational certificate**, paying endpoint and bulk costs during selection. Alternatively, a genuinely source-specific directional inverse bound could replace the scalar 1/kappa penalty. Merely taking more terms, reducing one fitted residual, or omitting endpoint layers does not supply that missing theorem.
