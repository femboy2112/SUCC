# Independent adversary — causal negative orders and source zeros

## Source state and hole contract

Starting source: clean SUCC commit `55bcde3d0c5ceb47d50cb499bd39f4a97c96bfc5`. This bearing uses the `find-math-shaped-holes` and `the-aletheia-method` proof-audit discipline. It begins independently of the new implementation; later root proposals are identified explicitly. No imported source, seed, radix, or regulator is changed.

The exact hole is whether the normalized positive-time kernels admit a unique causal extension to negative analytic order, what structural hypotheses supply that extension, and whether the original BBP source then has the negative-even zeros of zeta. The strongest surviving result is an entire convolution group of **causal distributions**, together with a source-specific factorization whose real zero set is a finite consecutive block. Density and compactness do not supply the missing analytic structure; positivity of measures does not survive negative order; noisy positive data do not stably determine arbitrary negative values.

Acceptance requires a proof of the distribution-valued extension and its uniqueness, retained boundary terms and source channels, an original-source parity discriminator, and an explicit stability limitation. A changed source is admissible only as a labelled model-class control, never as a refutation of a theorem fixing the canonical source.

Read provenance: `provenance/IMPORT_MANIFEST.json`; the existing Oily dossier; `bbp_volume_algebra/THEOREMS.md` and its provenance; and the literal inherited `observational_succ/euler_bbp_regulator.py`. Pinned Git blobs:

| Baseline artifact | Blob |
|---|---|
| `observational_succ/euler_bbp_regulator.py` | `22b5fe976dc16a8945c2b72f5acaa77f0970fd44` |
| `research/2026-10-26/OILY_MACARONI_SOURCE_MELLIN_HILBERT.md` | `593e08ffbc0220d546d7b7dabc58d3244b831eda` |
| `research/2026-11-15/bbp_volume_algebra/THEOREMS.md` | `359cd4b7002c30090417b6958add138cfc59c315` |

The existing ten `tests.test_euler_bbp_regulator` tests were rerun successfully before new instrumentation. The normalized Gamma distribution calculus is classical; the source-specific synthesis does not claim scholarly priority.

## Frozen finite probe domain

The following grid is declared before writing `independent_audit.py`:

- Literal source ages `1/7, 1, 11/3, 17, 101`; face counts `k=0..10`; negative orders `m=0..24`. Compare direct signed powers with an independent Taylor-jet calculation, including all predicted zero and strict-sign regions.
- Full native regulator `rho=1/16`; face counts `0..10`; negative orders `0..24`. Compare geometric power moments with derivatives of the independently expanded quotient kernel. Preserve all four source channels.
- Causal signed difference orders `m=0..8`, test monomial degrees `0..12`, and spacings `1,1/2,1/4,1/16`. Calibrate exact finite differences against Stirling coefficients. Check total variation and the attained worst-case error for observation tolerance `1/100`.
- Positive finite sampling nodes `1,2,3,5,8`; unseen targets `-1,-2,-7`. Construct exact interpolation rivals with zero discrepancy on every sample and discrepancy one at the target.
- Entire-noise controls at negative targets `-1..-6`, integer decay strengths `1..8`, and positive orders `1,2,3,5`.
- Mutants to reject: erase the contact term at a negative integer because `1/Gamma` vanishes; reverse the signed-difference orientation; replace its signed weights by positive weights; declare no noise amplification; claim negative-even zeros for the original source; extend the consecutive zero block by one extra endpoint; drop an original exponential channel; and discard the initial value when composing integration and differentiation.

No new production module will be imported. These finite checks calibrate identities and discriminators; the universal results below are proved separately.

## A1. The strongest causal extension theorem

Let \(\mathcal D'_+\) denote distributions on the real line with support in \([0,\infty)\). For \(\Re s>0\), define

\[
\langle\Phi_s,\varphi\rangle
=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}\varphi(t)\,dt,
\qquad \varphi\in C_c^\infty(\mathbb R).
\]

This Gamma normalization is not probability normalization: the positive real kernels have infinite total mass on the whole half-line. Their causal support and local integrability are the relevant properties.

**PROVED, classical distribution calculus.** There is a unique weakly entire \(\mathcal D'_+\)-valued extension agreeing with this formula on the right half-plane. It satisfies

\[
D\Phi_s=\Phi_{s-1},\qquad
\Phi_s*\Phi_z=\Phi_{s+z},\qquad
\Phi_0=\delta,\qquad \Phi_{-m}=\delta^{(m)}\quad(m\ge0).
\tag{A1}
\]

**Construction and proof.** For any integer \(N\ge0\) such that \(\Re(s+N)>0\), put

\[
\Phi_s=D^N\Phi_{s+N},\qquad
\langle\Phi_s,\varphi\rangle
=\frac{(-1)^N}{\Gamma(s+N)}
\int_0^\infty t^{s+N-1}\varphi^{(N)}(t)\,dt.
\tag{A2}
\]

Integration by parts proves that the definitions for \(N\) and \(N+1\) agree: the boundary power in \(\Phi_{s+N+1}\) vanishes at zero because \(\Re(s+N)>0\), and the test function has compact support. Each formula is holomorphic on its indicated half-plane and the half-planes cover \(\mathbb C\). The extension is supported in the same causal half-line. Uniqueness follows by applying the scalar identity theorem to every test-function pairing. Agreement on any positive real interval would also suffice **within this declared holomorphic class**.

For positive real parts, the convolution identity is the Beta integral on a finite lag simplex. For general parameters, choose large integers \(N,M\), commute distributional derivatives with convolution, and reduce to the positive-order identity. Convolution is defined for arbitrary pairs in \(\mathcal D'_+\): addition is proper on their supports over each compact target set. Since \(\Phi_1\) is the Heaviside distribution, \(D\Phi_1=\delta\); further differentiation gives the negative integers.

The classical framework is explicitly used in Epstein and Morava, [*Tempering the Polylogarithm*](https://arxiv.org/pdf/math/0611240), pp. 2 and 5. The elementary chart proof above states the normalization and test-space assumptions directly. Gamma's poles and the zeros of its reciprocal are recorded in [DLMF §5.2](https://dlmf.nist.gov/5.2).

The analytic order becomes negative while **time support remains nonnegative**. This is a genuine realization of negative algebraic operations using causal supports, provided signed distributions and their limiting topology are allowed. It is not negative elapsed time or a negative probability density.

### Boundary terms are part of the inverse

For a smooth function on the right half-line,

\[
D^m(Hf)=Hf^{(m)}+
\sum_{j=0}^{m-1}f^{(m-1-j)}(0)\delta^{(j)}.
\tag{A3}
\]

The distribution convolution law retains these contacts. If one instead uses only the ordinary derivative on \((0,\infty)\), the reverse composition loses the initial Taylor polynomial:

\[
I^mD^mf=f-\sum_{j=0}^{m-1}f^{(j)}(0)t^j/j!.
\]

Already \(f(t)=1+t\) gives \(IDf=t\), with the initial value one missing. Thus a causal inverse is exact in the augmented boundary/distribution space; throwing away that boundary destroys the inverse property.

For \(\lambda>0\), the probability-normalized Gamma family is
\(\mu_s^\lambda=\lambda^se^{-\lambda t}\Phi_s\). Its negative integer extension is

\[
\mu_{-m}^\lambda=\lambda^{-m}(D+\lambda)^m\delta.
\]

The factor \(\lambda^{-m}\) must be present if probability normalization is claimed. The unnormalized tempered kernel is simply \((D+\lambda)^m\delta\).

## A2. Forward support survives; positivity of measures does not

For \(m\ge1\), \(\delta^{(m)}\) is not a positive distribution. Let \(\chi\ge0\) be smooth, compactly supported, and equal to one near zero. The nonnegative test

\[
\varphi_m(t)=\chi(t)\bigl(1+(-1)^{m+1}t^m\bigr)^2
\]

satisfies

\[
\langle\delta^{(m)},\varphi_m\rangle=-2m!<0.
\tag{A4}
\]

Distributional limits of positive measures remain positive on every nonnegative test, so no sequence of positive measures can converge to \(\delta^{(m)}\). More generally, for real \(s<0\), the Laplace transform \(p^{-s}\) of \(\Phi_s\) increases with \(p>0\), whereas the Laplace transform of a positive causal measure is nonincreasing. Thus the extended family is positive exactly at real orders \(s\ge0\).

There is nevertheless an exact forward-support approximation:

\[
A_{m,\varepsilon}
=\varepsilon^{-m}\sum_{j=0}^m(-1)^j\binom mj\delta_{j\varepsilon}
\longrightarrow\delta^{(m)}\quad\text{in }\mathcal D',\quad \varepsilon\downarrow0.
\tag{A5}
\]

Every sample lag is nonnegative. Taylor expansion, or the iterated fundamental theorem of calculus, proves the limit. The signs are essential: the pairing is \((-1)^m\) times the ordinary forward difference of the test function. Reversing the first-order stencil approximates \(-\delta'\).

The total variation and exact worst-case observation-error gain are

\[
\|A_{m,\varepsilon}\|_{\rm TV}=2^m\varepsilon^{-m},\qquad
\sup_{|e_j|\le\eta}\left|\varepsilon^{-m}\sum_j(-1)^j\binom mj e_j\right|
=2^m\eta\varepsilon^{-m}.
\tag{A6}
\]

The alternating errors \(e_j=\eta(-1)^j\) attain the bound. If \(|\varphi^{(m+1)}|\le M\) on \([0,m\varepsilon]\), the bias from the exact derivative is at most \(m\varepsilon M/2\), because the mean sum of coordinates on the unit \(m\)-cube is \(m/2\). Shrinking the causal step reduces this bias and amplifies fixed observation error. A convergence theorem from noisy samples therefore needs a quantitative noise/regularity hypothesis.

There is also no nontrivial inverse **within positive causal measures**. If positive measures \(\nu,\eta\) supported in \([0,\infty)\) satisfy \(\nu*\eta=\delta_0\), positivity forces both supports to be \(\{0\}\). They are reciprocal scalar multiples of \(\delta_0\); among probability measures both are \(\delta_0\). The distribution group in (A1) is a larger space, not a hidden inverse already present in the positive-measure cone.

## A3. Exact uniqueness requires a law; sampled positivity is insufficient

For finitely many positive sampling points \(s_i\), the entire functions

\[
F(s)+c\prod_i(s-s_i)
\]

agree at every sample and can take arbitrary values at an unobserved negative target. Prescribed finite jets can be matched by increasing the corresponding multiplicities. Entire regularity alone does not repair finite identification.

Even knowing **all positive integer kernels**, positivity for all positive real orders, probability normalization, and entire distribution-valued dependence does not identify the negative extension. The following stronger control retains all those properties. Use rate one and let

\[
\mu_s=e^{-t}\Phi_s,\qquad
h(s)=\frac1{\Gamma(1-s)},\qquad
u(s)=1-e^{-h(s)^2},
\]

\[
\Psi_s=(1-u(s))\mu_s+u(s)\delta_0.
\tag{A7}
\]

The scalar functions and distribution family are entire. For every real \(s>0\), \(h(s)\) is real and \(0\le u(s)<1\), so \(\Psi_s\) is a positive probability measure. At every positive integer \(n\), \(h(n)=0\), hence \(\Psi_n=\mu_n\). At zero both families equal \(\delta_0\). But \(h(-m)=1/m!\), so \(\Psi_{-m}\ne\mu_{-m}\) for every \(m\ge1\).

What fails is the convolution law. At \(s=1/2\), \(u(s)>0\), so \(\Psi_{1/2}*\Psi_{1/2}\) has a positive atom at zero; \(\Psi_1=\mu_1\) has no atom. This is a discriminating probe for the missing composition structure, not a competing Gamma convolution semigroup.

By contrast, an exact positive-order germ together with weak holomorphy gives the unique extension by (A2). The derivative or convolution law also propagates integer inverse information in the augmented distribution algebra. Those laws are mathematical premises to prove from the construction, not consequences of a dense drawing or a finite list of matching shapes.

### Uniqueness does not imply stable extrapolation

Fix a negative target \(-m\), \(m>0\), and let

\[
g_N(s)=2^{-N(s+m)}.
\]

Each \(g_N\) is entire, \(g_N(-m)=1\), and
\(\sup_{s\ge a}|g_N(s)|=2^{-N(a+m)}\to0\) for any positive real \(a\). Thus arbitrarily small errors over an entire positive real half-line can conceal an order-one negative-target discrepancy. This refutes continuity of unrestricted analytic extrapolation in that positive-data supremum norm. It does not contradict exact analytic uniqueness. A common growth bound, a restricted model class, or quantitative moment/regularity control is additional information needed for stability. The exact source formula, once authenticated, supplies much more information than noisy observations alone.

## A4. Compactness can recover inverses only with the right geometry

Density alone supplies no path. A continuous map from \([0,1]\) into \(\mathbb Q\) is constant, since its image is connected and a nontrivial real interval contains irrational points. A countable dense subset can therefore contain no nonconstant paths.

Compactness alone is also insufficient: the Cantor set is compact and has no nonconstant paths. Even compactness plus connectedness and a dense path-connected subset is insufficient. The closed topologist's sine curve

\[
S=\{(x,\sin(1/x)):0<x\le1\}\cup(\{0\}\times[-1,1])
\]

is compact and connected, and the graph part is path connected and dense. A path from its vertical segment into its graph cannot exist. Take the left endpoint of the positive-horizontal component of an alleged path that contains its graph endpoint. As that component approaches its left endpoint, continuity of the horizontal coordinate forces arbitrarily close points with \(\sin(1/x)=1\) and \(-1\), contradicting continuity of the vertical coordinate. Thus even a dense connected exploration can acquire a closure with unreachable path components.

**Strong repair, proposed by root and checked here.** If the ambient object is a compact Hausdorff **topological group**, then \(g^{-1}\) belongs to the closure of the positive powers of \(g\).

For an identity neighborhood \(W\), choose a neighborhood \(V\) with \(V^{-1}V\subseteq W\), and cover the compact group by finitely many translates of \(V\). Among sufficiently many powers \(g^{Lj}\), two lie in the same translate, so some \(g^n\in W\) with \(n\ge L\). Since \(L\) is arbitrary, there are arbitrarily late positive returns near the identity. Multiplying by \(g^{-1}\) shows that positive powers approach \(g^{-1}\). In a compact metrizable group this can be expressed by a sequence; for general compact groups the neighborhood/closure argument or nets must be used.

This preserves the user's geometric intent: an explicitly reversible compact group action can approximate inverse actions using positive powers. It gives no recurrence-time bound and no finite exact inverse unless further structure supplies one. A finite cyclic group can give exact inverses and still have no nonconstant continuous paths. Conversely the map \(x\mapsto0\) on compact \([0,1]\) loses its input permanently, so compactness of a general causal system does not supply an inverse.

Path connectivity also does not imply holomorphy. The map \(z\mapsto\overline z\) is continuous on the connected plane and fails the complex derivative test. Analytic continuation requires a holomorphic germ and a compatible domain, with singularity and monodromy conditions where relevant. The distribution family (A1) has an explicit entire construction; no topological spiral substitutes for that construction.

## A5. Original BBP source: no negative-even zero pattern

Keep the literal source

\[
q(t)=4-2e^{-3t}-e^{-4t}-e^{-5t},\qquad a>0.
\]

The normalized Mellin readout initially equals

\[
F_a(s)=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}e^{-at}q(t)dt
=4a^{-s}-2(a+3)^{-s}-(a+4)^{-s}-(a+5)^{-s}.
\tag{A8}
\]

The equality follows termwise for \(\Re s>0\); its right side is entire and supplies the continuation. The combined unnormalized integral already converges for \(\Re s>-1\) because \(q(t)=15t+O(t^2)\). At nonpositive integers,

\[
F_a(0)=0,\qquad
F_a(-m)=4a^m-2(a+3)^m-(a+4)^m-(a+5)^m<0\quad(m\ge1).
\tag{A9}
\]

Every shifted positive base strictly exceeds \(a\), and the three negative multiplicities sum to four. In particular,
\(F_a(-1)=-15\) and \(F_a(-2)=-30a-59\). This is an unchanged-source counterexample to inferring negative-even zeros from the Gamma(2) endpoint or from positivity of the lag kernel.

The full native family retains the radix regulator:

\[
B(s)=\sum_{n\ge0}16^{-n}F_{8n+1}(s),\qquad
H(t)=\frac{e^{-t}q(t)}{1-e^{-8t}/16}.
\]

Uniform geometric domination on compact parameter sets makes \(B\) entire. Its exponent-one value is the inherited BBP identity \(B(1)=\pi\); changing the exponent changes the analytic report, not the actual original forcing. The negative values are

\[
B(0)=0,\quad B(-1)=-16,\quad B(-2)=-112,\quad B(-3)=-880,
\]

and \(B(-m)<0\) for every integer \(m\ge1\).

**Regulator boundary.** The inherited `euler_bbp_regulator.py` also treats the distinct unregulated family at regulator one. Its analytic exponent-zero value is \(15/8\), whereas each literal exponent-zero summand vanishes. The native regulator \(1/16\) has \(B(0)=0\). Removing the regulator changes the convergence and boundary problem; a zeta/Hurwitz comparison must not silently identify these two values.

## A6. The surviving Gamma-shape/zero theorem is stronger and more precise

Apply the authentic finite face \((1-e^{-8t})^k\), \(k\ge0\):

\[
H_k(t)=H(t)(1-e^{-8t})^k,\qquad
B_k(s)=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}H_k(t)dt
\]

where the integral converges for \(\Re s>-k-1\), with the reciprocal Gamma factor interpreted analytically. Initially the integral formula may be used on \(\Re s>0\). The independently derived finite-difference identity is

\[
F_{a,k}(-m)=(-1)^{k+1}
\left(2\Delta_8^k\Delta_3+\Delta_8^k\Delta_4+\Delta_8^k\Delta_5\right)a^m.
\tag{A10}
\]

Mixed forward differences of order \(k+1\) annihilate polynomials of degree at most \(k\). Their cube-integral representation is strictly positive on \(a^m\), \(a>0\), for \(m\ge k+1\). Consequently the negative integers are zero exactly for \(0\le m\le k\), followed by strict sign \((-1)^{k+1}\). The first nonzero value is

\[
F_{a,k}(-(k+1))=(-1)^{k+1}15\,8^k(k+1)!.
\]

### Exact real zero set from a positive mixture

Root subsequently proposed the following refinement of (A10); the measure construction and analyticity were independently checked here. Let

\[
w(v)=2\mathbf1_{[0,3]}(v)+\mathbf1_{[0,4]}(v)+\mathbf1_{[0,5]}(v).
\]

Then \(\int w=15\) and

\[
q(t)=t\int_0^5w(v)e^{-vt}dv,\qquad
1-e^{-8t}=t\int_0^8e^{-ut}du.
\]

Push the positive product measure

\[
\left(\sum_{n\ge0}16^{-n}\delta_n\right)
\otimes w(v)dv\otimes\operatorname{Leb}_{[0,8]}^{\otimes k}
\]

forward by \(\lambda=1+8n+v+u_1+\cdots+u_k\). Call the result \(\mu_k\). It is supported on \([1,\infty)\), has mass \(16\,8^k\), and has every polynomial moment because the discrete weight decays geometrically. Directly,

\[
H_k(t)=t^{k+1}\int e^{-\lambda t}\mu_k(d\lambda).
\]

The Mellin identity is therefore

\[
\boxed{B_k(s)=(s)_{k+1}L_k(s),\qquad
L_k(s)=\int\lambda^{-s-k-1}\mu_k(d\lambda).}
\tag{A11}
\]

Since \(\lambda\ge1\), compact parameter sets are dominated by a fixed polynomial moment, so \(L_k\) is entire. Since the measure is positive and nonzero, \(L_k(s)>0\) for **every real** \(s\). Hence

\[
\boxed{\{s\in\mathbb R:B_k(s)=0\}=\{0,-1,\ldots,-k\},
\quad\text{all simple}.}
\tag{A12}
\]

There is no conclusion here about the nonreal zeros of \(L_k\). The first contact is

\[
B_k(-(k+1))=(-1)^{k+1}16\,8^k(k+1)!.
\tag{A13}
\]

The local lag shape is \(H_k(t)=16\,8^kt^{k+1}+O(t^{k+2})\), producing Gamma\((k+2)\) under a large Laplace tilt. Thus, for this **full authenticated family**, the shape corresponds to \(k+1\) consecutive real zeros. It does not select only even integers or create an infinite zeta parity pattern.

The analogous convolution-power result is also source preserving. From \(q(t)=t\int we^{-vt}\), the simplex formula gives

\[
q^{*j}(t)=t^{2j-1}\int e^{-\lambda t}\nu_j(d\lambda),
\qquad \nu_j\ge0,\quad \nu_j(\mathbb R)=15^j/\Gamma(2j),
\]

with compact support. After a positive age tilt its normalized Mellin readout has exactly the consecutive simple real zeros \(0,-1,\ldots,-(2j-2)\), its first negative contact is \(-15^j\), and all subsequent negative integer values are negative. This proves the signs independently of a partial-fraction compiler.

Adding infinitely many unscaled faces does not produce zeta: \(B_k\to0\) locally uniformly on \(\mathbb C\). On a compact parameter set choose \(k_0\) large enough that the literal integral is integrable at zero for every parameter there. For \(k\ge k_0\), a common integrable majorant applies, while the extra face power tends to zero at every positive \(t\). Dominated convergence proves the locally uniform limit. Any normalization intended to retain a nonzero limit is an additional construction with its own domain and convergence obligations.

## A7. What actually supplies zeta's negative-even zeros

The zeta source is a different positive heat kernel,

\[
K(t)=\frac1{e^t-1}=\sum_{n\ge1}e^{-nt},\qquad
\zeta(s)=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}K(t)dt,
\quad \Re s>1.
\]

The source formula and domain are [DLMF 25.5.1](https://dlmf.nist.gov/25.5#E1). The regularized germ

\[
K(t)-\frac1t+\frac12
\]

is odd, because \(K(-t)=-1-K(t)\). Thus its positive even Taylor coefficients vanish. Subtracting the pole and a finite Taylor jet in the Mellin integral shows that the normalized value at \(-m\) is \((-1)^m m!\) times the coefficient of \(t^m\) in \(K(t)-1/t\). This yields zeros at negative even integers \(-2,-4,\ldots\), while the constant coefficient \(-1/2\) gives \(\zeta(0)=-1/2\). Equivalently the same parity is explicit in the sine factor of [DLMF 25.4.2](https://dlmf.nist.gov/25.4#E2); [DLMF §25.10](https://dlmf.nist.gov/25.10) states the trivial zeros.

The required extra structure is the source's exact regularized parity, or the corresponding completed functional equation. Gamma alone has no zeros. Reciprocal Gamma vanishes at all nonpositive integers, but Mellin poles can cancel those zeros, as the unchanged BBP source in (A9) demonstrates.

A labelled model-class mutation makes this distinction sharp: adding \(\varepsilon t^{2n}e^{-t}\), \(\varepsilon>0\), to \(K(t)\) keeps positivity and the leading \(1/t\) singularity but changes the normalized value at \(-2n\) by \(\varepsilon(2n)!\). It changes the zeta source and therefore is not a counterexample to zeta's theorem. It refutes only the weaker claim that positivity and the same leading Gamma/pole shape force that theorem.

## Executed receipts and implementation audit

The independent command completed with exit code zero and `result: PASS`:

```sh
python research/2026-11-15/causal_negative_orders/independent_audit.py
```

| Instrument | Actual executed scope |
|---|---:|
| Source faces: direct signed powers versus Taylor jets | 1,375 identities |
| Full native family: geometric moments versus quotient jets | 275 identities |
| Native first nonzero contacts | 11 identities |
| Forward causal stencil versus Stirling coefficients | 468 identities |
| Exact stencil total variation | 36 identities |
| Attained observation-noise amplification | 32 identities |
| Negative distributions on nonnegative test functions | 8 strict negative pairings |
| Finite positive-sample interpolation rivals | 18 checks |
| Entire-noise positive-data controls | 192 checks |
| Declared false-rule mutations | All 8 rejected |

The script emits the complete JSON receipt, including original-source values and all mutation witnesses. It uses exact integers/Fractions, no random seed, no zeta evaluations, and no production imports. Its two source routes share the literal authenticated source but use different decompositions; they are independent implementation checks, not independent source provenance.

After that run, root requested a direct review of `observational_succ/causal_negative_orders.py` and its new tests. The finite APIs and their advertised limits were inspected: order at most 64, face at most 24, exact rational input guards, regulator strictly below one, and inherited convolution power at most 12. No mathematical correction was found. These limits bound degrees and loop counts; the bit complexity still depends on supplied integer/Fraction sizes. The script above remains independent of this production module.

## Claim ledger and next discriminant

| Claim | Status and boundary |
|---|---|
| Unique entire causal extension of the specified positive-order kernel germ | **DISCLOSED**, in the weakly holomorphic distribution category |
| Negative integers realized by signed differences at forward lags | **DISCLOSED**, distributional limit with explicit noise gain |
| Positive measures alone contain nontrivial causal inverses | **REFUTED**, support argument and nonnegative-test witness |
| Dense/compact exploration entails a connecting path or holomorphy | **REFUTED**, explicit topological and analytic countermodels |
| Compact reversible group action approximates its inverse through forward powers | **DISCLOSED**, closure statement; no time bound or generic causal-system inference |
| All positive integer Gamma kernels identify the entire negative extension without a composition law | **REFUTED**, positive normalized rival (A7) |
| Exact analytic uniqueness ensures stable noisy extrapolation | **REFUTED** without a further function-class bound |
| Original BBP Gamma shape forces negative-even zeros | **REFUTED**, original \(B(-2)=-112\) and all-order sign proof |
| Authentic face family has exactly a consecutive block of simple real zeros | **DISCLOSED**, positive-mixture factorization (A11) |
| Zeta parity follows from its exact regularized heat-kernel symmetry | **DISCLOSED**, classical source-specific statement |

The next useful discriminator is a proposed **source-preserving** map that carries the BBP kernel's complete signed channel and boundary data to a completed arithmetic heat kernel while proving the necessary symmetry. Matching one Gamma shape, increasing the number of vanished low jets, or drawing a compact spiral does not supply that map. For a physical/noisy observer, a separate quantitative stability contract is also needed before analytic negative-order values are certified from measured positive data.

## Root synthesis review receipt

Reviewed `THEOREMS.md` CN-01 through CN-11 at SHA-256
`b4741aaddce2934bcf35af792b46a0674480b27ed790c89b60016939b0488b42`.
The CN-06 positive-mixture factorization, exact real-zero set, strict signs,
first contact, and fixed-face normalization were checked. CN-07's
convolution contacts and the distinctions involving the actual selected
chronological phase were checked. CN-08's stated local-uniform limit was
also reviewed directly: both the positive and inverse moment tail bounds
support its compact-parameter expectation argument.

No mathematical correction to those claims was found. A minor CN-10
clarification was requested: explicitly state the branch and fixed-radius
convention for its Hankel loop, as in [DLMF 5.9.2](https://dlmf.nist.gov/5.9#E2),
instead of referring to an unstated branch. Shrinking the loop radius to
zero requires a separate convergence restriction; the fixed loop formula
does not. Root was also supplied the stronger positive normalized rival
(A7) for inclusion. This receipt refers to the displayed file hash;
subsequent edits require a fresh review/hash.

Production file inspected: `observational_succ/causal_negative_orders.py`,
SHA-256 `c980f9e470f7540dca55800d2b2d1a2957ce14939c0934fc6cb37da891e06df1`.
Independent script executed: `independent_audit.py`, SHA-256
`63442e2a9ec68017febbece4363140e8c5c5ae274fe1a508644ed42dd6f04f0f`.

### Closing refresh — PASS

The final theorem file was reread at SHA-256
`112634fd9d370be421b5ca4d9619c9ea01fd259b8cdbd4ecef6f97f422db04f1`.
It resolves the Hankel branch/fixed-radius clarification and includes
the positive normalized rival (A7), the explicit compact-parameter
construction of the entire source-depth group, and eventual-in-grade
moment bounds. The added Weyl relation \([D,X]=I\) and
\(X\Phi_s=s\Phi_{s+1}\) are correct with their stated distributional
domains. Convolution depth, derivative order, Mellin order, and
chronological source time remain correctly distinguished.

The newly included, explicitly inherited Pascal/Hasse aggregation was
also reviewed. Its positive kernel sum is \(1/(e^t+1)\); local normal
convergence follows from the displayed fixed-face majorant and geometric
grade weights. Its finite negative-integer formula and parity are valid.
Applying the identical weights to the authentic BBP faces instead gives
\(H_{1/16,0}/(1+e^{-8t})\) and the exact value \(8\) at order \(-2\),
so no source identification is being inferred from common grade weights.

The final production module was inspected at SHA-256
`da162c3e1bc91d70f260c5ae1e16d13200ddb793d21673de518975132cc88cc0`.
Its four added Pascal/Hasse/mixture APIs implement those finite formulas.
The native-mixture bound \(m\le25\) keeps every required face
\(k<m\) within the existing face bound 24; the universal Pascal APIs
retain the order/grade bound 64. The order-zero empty native sum is
correct. No new production import was added to the independent audit.

**Closing review verdict: PASS.** No unresolved mathematical correction
was found in the refreshed file versions. The stated stability,
positivity, source-comparison, and selected-phase limitations remain
material boundaries, rather than outstanding defects in these claims.
