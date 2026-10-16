# SUCC × FUCC → Tate–Mellin: certified source triangle, exact finite valuation cone, and escaping Euler observer

**Date:** 2026-10-16. **Parent:** draft PR #145, head `b8e147d8d53d4c3bd2e48d1f0ad06f3e59bf1b21`; stacked on PRs #142 and #141. **Branch:** `research/tate-mellin-prime-fucc-escape-2026-10-16`. **Research classification:** classical harmonic/probability mathematics made source-explicit, with exact finite arithmetic and rational paper error certificates. No originality priority is asserted for standard Tate, Gamma, Euler, Poisson, prime-reciprocal divergence, or finite quadrature theorems.

**RH PROVED: NO.** Signed Weil/Suzuki global positivity: OPEN. No nontrivial zero ordinate is ever an input. Finite numerical readouts are **not interval certifications**; the separate analytic error envelopes are pure `Fraction` objects.

## 0. Object and source-map contract

We ask for an actual, quantified finite-source interface aligning (i) the factorial positive moment law; (ii) Beta/exponential finite SUCC clocks; (iii) Dirac log lattices; and (iv) **authentic** arithmetic FUCC prime valuation carriers, *before* attempting the completed Weil distribution.

Notation:

* `Gamma_R(s) = pi^(-s/2) Gamma(s/2)`, `Lambda(s) = Gamma_R(s) zeta(s)` (meromorphic completed zeta **without** the factor `s(s−1)/2`).
* `a=n+1`, `n in N_0`, `sigma=2a>=2` unless an explicit different domain is stated. `t` is a real Fourier coordinate, so the complex spectral input is `s=sigma+2it`.
* Natural SUCC: `S(m)=m+1`. Genuine prime FUCC: `V_p(m)=pm` with `p` verified prime; `V_p S=S^p V_p` is the original *flat affine* square.
* Gamma probability source `X~Gamma(a,1)`, density `x^(a−1)e^(−x)/Gamma(a)`; its log characteristic is `Gamma(a+it)/Gamma(a)`.
* Arithmetic source `N` on positive integers, whose **canonical** multiplicative decomposition uses prime valuations `K_p=v_p(N)`; additive-N cutoff and prime-valuation box cutoff are **not** the same finite source.

All finite clocks are *declared probability sources* or mathematical quadrature charts. No claim that a finite embodied observer physically samples every infinite factor, and no interpretation of randomly indexed Beta clocks as authentic arithmetic prime FUCC operators.

## TMF-01. One exact completed Mellin characteristic source (CLASSICAL / PROVED PAPER)

For `sigma=2a>1`, define

\[
\mathbb P_\sigma(N=m)=\frac{m^{-\sigma}}{\zeta(\sigma)},\qquad
X\sim\mathrm{Gamma}(a,1),\qquad X\perp N.
\]

Unique factorization and the absolutely convergent Euler product give *independent*, infinite-coordinate geometric prime valuations

\[
\mathbb P_\sigma(K_p=k)=(1-p^{-\sigma})p^{-k\sigma},\quad k\ge0.
\]

Because `sum_p p^(-sigma)<infinity`, only finitely many `K_p` are nonzero almost surely. Thus `N=prod_p p^(K_p)` is a finite positive integer almost surely, with exactly the stated zeta law. Set

\[
W=\log(X/\pi)-2\log N.
\]

Then the **exact, normalized Tate–Mellin characteristic identity** is

\[
\boxed{\mathbb E e^{itW}
=\pi^{-it}\frac{\Gamma(a+it)}{\Gamma(a)}
\frac{\zeta(2a+2it)}{\zeta(2a)}
=\frac{\Lambda(2a+2it)}{\Lambda(2a)}.}\tag{TMF.1}
\]

It follows directly from independence, the Mellin integral, and the true Euler product. This *is* a positive-characteristic-function/positive-Gram realization **on `Re(s)>1`**. It is NOT a Weil-criterion argument, a `xi` realization, or an extension to `Re(s)=1/2`.

**Real Tate normalization is load-bearing:** for the Gaussian test `f_infty(x)=e^(−pi*x²)`, with `d^×x=dx/|x|`,

\[
2\int_0^\infty e^{-\pi r^2}r^{s-1}\,dr=\Gamma_{\mathbb R}(s).
\]

At `s=2a+2it`, the substitution `x=pi*r²` produces the shape-`a` probability law, with the precise phase `pi^(−it)`. The probability source is the normalized Gaussian **tilted by the Mellin weight**: it is not the unweighted Gaussian probability distribution.

## TMF-02. Beta/Exp and Dirac charts converge to the same real-place source (PROVED PAPER / exact bounds)

**Beta/exponential chart:** from parent FGF-7/7B,

\[
\Phi^{\beta}_{n,M}(t)=\pi^{-it}M^{it}\prod_{k=n+1}^{M}\frac{k}{k+it},\quad M>n.
\]

`-log B_k~Exp(rate k)` where `B_k~Beta(k,1)`, so the two descriptions are the **same finite probabilistic source in different coordinates**. Parent FGF-7 gives the exact rational bound, for `T<M+1`,

\[
B=\frac T{2M}+\frac{T^2}{2M(1-T/(M+1))}<1
\implies\sup_{|t|\le T}|\Phi^{\beta}_{n,M}(t)-\Phi_n(t)|
\le\frac B{1-B}=:E_\beta.\tag{TMF.2}
\]

**Independent finite Dirac source:** let `d>0` be rational, `L<0<R` integers, `a=n+1`,

\[
g_a(u)=e^{au-e^u},\quad C=\int g_a(u)du=\Gamma(a)=n!,\quad
S_{L,R}(t)=d\sum_{j=L}^R g_a(jd)e^{itjd}.
\]

The exact, *finite* normalized positive probability source has

\[
\Phi^D_{n,d,L,R}(t)=\pi^{-it}\frac{S_{L,R}(t)}{S_{L,R}(0)}.
\]

This uses the Gamma log-grid shifted by `−log pi` in the original `Gamma_R` log variable. **At finite resolution it is not identical to the unshifted lattice of DGC**, although both tend to the same target and the source origin is explicitly declared. It avoids arbitrary choice of a complex-valued normalization: its DC is strictly positive by construction, and `Phi^D(0)=1`.

For `|t|<=T`, the cellwise `W^{1,1}` quadrature inequality yields

\[
\left|d\sum_{j\in\mathbb Z}g_a(jd)e^{itjd}-\Gamma(a+it)\right|
\le d\int|\partial_u(g_a(u)e^{itu})|du
\le d(2a+T)\Gamma(a).\tag{TMF.3}
\]

For `L<=−1` the left omitted lattice tail is bounded by `e^(aLd)/a`; for `Rd>=a−1`, the monotone right tail is bounded by `Gamma(a) 2^a exp(−exp(Rd)/2)` using the Gamma MGF at `1/2` and Markov. Let `P_J(x)=sum_(j=0)^J x^j/j!`, for `x>=0`. Since `P_J(x)<=e^x`, define **rational** normalized-tail envelopes

\[
\delta_L=\frac{1}{a!\,P_J(-aLd)},\qquad
\delta_R=\frac{2^a}{P_J(P_J(Rd)/2)},\qquad
\delta=\delta_L+\delta_R.
\]

If `2ad+delta<1`, divide by the independently lower-bounded finite source DC to get

\[
\boxed{\sup_{|t|\le T}|\Phi^D_{n,d,L,R}(t)-\Phi_n(t)|
\le \frac{d(4a+T)+2\delta}{1-2ad-\delta}=:E_D.}\tag{TMF.4}
\]

All numbers in `E_D` are rational, with no numerical Gamma/pi evaluation or rounding assumption. The exact *analytic* finite sum has a certified error; an ordinary mpmath printing of its value is **not** an outward-rounded numerical certificate. The bound is deliberately conservative (`O(d)`); prior BGD provides exponentially sharper Gaussian de-aliasing bounds under its stronger chart hypotheses.

The shared phase `pi^(−it)` has modulus 1, so the **two finite sources** satisfy `sup_(|t|<=T)|Phi^D-Phi^beta|<=E_D+E_beta`. They are **not** asserted to be the same finite source; only their limiting target agrees.

## TMF-03. Genuine prime-FUCC truncation and a rational error (PROVED PAPER)

At `sigma=2a>1`, let the finite prime source include **all actual primes** `p<=P`, and condition each geometric valuation `K_p` to the finite range `0..K`. Its finite characteristic function is

\[
\Phi^{\rm Euler}_{P,K,\sigma}(t)=
\prod_{p\le P}
\frac{\sum_{k=0}^Kp^{-k\sigma}e^{-2itk\log p}}
{\sum_{k=0}^Kp^{-k\sigma}}.
\]

For each prime, conditioning causes total-variation error exactly `p^(−sigma(K+1))`. By a product coupling, omitting all primes `p>P` costs at most `sum_(p>P)p^(−sigma)`, bounded by the full integer integral tail. The characteristic-function error is at most twice the coupling mismatch probability, hence **uniformly for all real `t`**:

\[
\boxed{\left|\Phi^{\rm Euler}_{P,K,\sigma}(t)
-\frac{\zeta(\sigma+2it)}{\zeta(\sigma)}\right|
\le 2\sum_{p\le P}p^{-\sigma(K+1)}
+\frac{2P^{1-\sigma}}{\sigma-1}=:E_P.}\tag{TMF.5}
\]

`E_P` is **exact rational** when sigma is integer. No zero lookup, no unverified Euler factor, and no fake composite is a source label. Positive mutational controls must not inherit the word "authentic".

## TMF-04. Fully source-labelled completed-zeta band transport (PROVED PAPER)

Multiply either finite real chart by the finite Euler source. All factors are characteristic functions of declared positive finite or finite-product laws, so their magnitudes are at most 1. A triangle inequality gives

\[
\boxed{\begin{aligned}
\sup_{|t|\le T}\bigg|\Phi^D_{n,d,L,R}(t)\Phi^{\rm Euler}_{P,K,2a}(t)
-\frac{\Lambda(2a+2it)}{\Lambda(2a)}\bigg|&\le E_D+E_P,\\
\sup_{|t|\le T}\bigg|\Phi^\beta_{n,M}(t)\Phi^{\rm Euler}_{P,K,2a}(t)
-\frac{\Lambda(2a+2it)}{\Lambda(2a)}\bigg|&\le E_\beta+E_P.
\end{aligned}}\tag{TMF.6}
\]

For a finite Fourier/Mellin basis `t_1,...,t_r` with `|t_i−t_j|<=T`, set `G_ij=Phi(t_i−t_j)`. Both finite and limiting positive-source Grams are PSD; every entry difference is <=epsilon, whence `||G_finite−G_target||_op<=r*epsilon` (Frobenius bound). This is a **true source-typed operator-norm estimate** for the *positive Mellin-source test basis*, and still **NOT** an identification of the signed Weil Gram.

**Representative exact-rational certificate** (run the accompanying receipt): `n=0`, `d=1/120`, `L=−840`, `R=840`, `T=2`, `P=97`, `K=5`, `M=500`. The derived bounds, displayed as approximate decimals only for readability, are

* `E_D ≈ 0.05275287828`; `E_beta ≈ 0.00605244376`; `E_P ≈ 0.02111060964`.
* Completed Dirac error `<= 0.07386348793`; completed Beta error `<=0.02716305341`.
* Dirac/Beta comparison `<=0.05880532204`; all exact Fraction bounds are in the receipt, **not** inferred from these decimals.

## TMF-05. Hyperbolic FUCC coordinates are exactly the finite natural-SUCC carrier (EXACT)

For `H>=1` define the **hyperbolic** valuation cone

\[
\mathcal V_H=\{(k_p)_p\in\mathbb N_0^{(\mathcal P)}:
\prod_p p^{k_p}\le H\}.
\]

Fundamental arithmetic gives a bijection `1<=m<=H <-> nu(m) in V_H` and for any `sigma>1` (indeed any scalar `s`) the finite identity

\[
\boxed{\sum_{m=1}^H m^{-s}
=\sum_{\alpha\in\mathcal V_H}
\prod_p p^{-s\alpha_p}.}\tag{TMF.7}
\]

This is an **exact, entire-in-s** equality of finite Dirichlet polynomials, not merely approximate. In contrast, the *rectangular* prime box `p<=P`, `0<=k_p<=K` includes e.g. `m=12` even when natural SUCC is cut at `H=6`; it is not the same finite observer carrier. This distinction is a source/provenance requirement, not a computational inconvenience.

For the direct natural-SUCC source `D_H(s)=sum_(m<=H)m^-s`, normalize by `D_H(sigma)`. Standard integral comparison gives

\[
\sup_t\left|\frac{D_H(\sigma+2it)}{D_H(\sigma)}
-\frac{\zeta(\sigma+2it)}{\zeta(\sigma)}\right|
\le\frac{2H^{1-\sigma}}{(\sigma-1)D_H(\sigma)}=:E_H.\tag{TMF.8}
\]

Thus the finite **SUCC enumeration** and prime-rectangle **FUCC enumeration** differ by at most `E_H+E_P`, again uniformly in `t`. This is a dependency-distinct finite implementation check of the same arithmetic Dirichlet source (not independent empirical proof of the zeta theorem).

SUCC transported through the valuation bijection is **not** a coordinatewise prime increment: `nu(m+1)` may rewire all prime factors (e.g. `nu(8)=3e_2`, `nu(9)=2e_3`). The map `V_p S=S^p V_p` still holds on the original integer carrier, with the appropriate admissible-path gate near finite horizons. No nonzero categorical holonomy is established.

## TMF-06. Prime-FUCC logarithmic cumulants recover true von Mangoldt jets (CLASSICAL / exact rational coefficients)

Let `q=p^(-sigma)`. The geometric valuations give

\[
\mathbb E K_p=\frac q{1-q}=\sum_{k\ge1}q^k,\qquad
\operatorname{Var}K_p=\frac q{(1-q)^2}.
\]

Consequently, in `Re(s)>1`,

\[
\boxed{-\frac{d}{ds}\log\prod_{p\le P}(1-p^{-s})^{-1}
=\sum_{p\le P}\sum_{k\ge1}(\log p)p^{-ks}.}\tag{TMF.9}
\]

This is precisely the authentic prime-power von Mangoldt data, with `Lambda(p^k)=log p`, `Lambda(4)=log 2`, and coefficient zero at 6. The truncated `k<=K` deficit per prime is exactly `q^(K+1)/(1−q)` **times log p**. The module stores those coefficients as rational objects indexed by authenticated `p`, without pretending that logarithms themselves are rational.

**Compact-support continuation of the *prime impulses*:** for every finite integer horizon `H`,

\[
J_{1/2,H}(f)=\sum_{p^k\le H}\frac{\log p}{\sqrt{p^k}}f(k\log p)
\]

is an exact finite source-labelled formula for any supplied test values at those addresses. It reads no zeros. It is not the entire completed Weil distribution: Gamma, pole, contact, reflection, topology and signs must be added, with a rigorously declared test domain. Extending the support to infinity destroys finite total mass: `sum_p log(p)/sqrt(p)` diverges, since eventually its terms dominate `1/p`, whose prime sum diverges.

This explains why **finite prime-jet access survives** a boundary where the naive global positive Euler probability model fails. It supplies input data, not the missing Weil sign theorem.

## TMF-07. Sharp positive-Euler source escape for `0<sigma<=1` (CLASSICAL / PROVED PAPER)

For *any* finite cutoff `P`, geometric prime source `N_P=prod_(p<=P)p^(K_p)` still exists at any sigma>0. Let `B>=1` be fixed. For `p>B`, the event `N_P<=B` forces `K_p=0`. Thus for `0<sigma<=1`,

\[
\boxed{\Pr(N_P\le B)
\le\prod_{B<p\le P}(1-p^{-\sigma})
\le\prod_{B<p\le P}(1-p^{-1})\longrightarrow0.}\tag{TMF.10}
\]

Euler's divergence `sum_p 1/p=infinity` forces this product to vanish. The finite *conditioned* geometric exponents `0<=K_p<=K` for **any K>=1** obey the analogous bound `prod_(B<p<=P)p/(p+1)->0`. Both finite rational products are executable diagnostics valid simultaneously for **all** `0<sigma<=1`.

Therefore **no tight weak limit on finite logarithmic addresses** exists for this positive-prime family; `log N_P -> +infinity` in probability. If `U` is any independent tight real-place logarithmic source, then `U−2log N_P -> −infinity` in probability. Proof: for any real level, split the event between `U>A` and `2log N_P<A+level`, then use tightness followed by TMF.10.

This is a rigorous no-go for **the declared positive, normalized Euler probability passage** across `sigma<=1`. It is NOT a no-go for analytic continuation, signed Weil distributions, mathematics, RH, or physical observers. In particular, at `sigma=1/2` the Gamma density can still exist, but it cannot independently normalize the escaping Euler mass into a probability distribution on R.

## TMF-08. Finite SUCC prefixes force actual cross-prime correlations (EXACT finite / CLASSICAL limit)

Under the full zeta source for `sigma>1`, distinct prime valuation events `A_p={p divides N}`, `A_q` are independent. Under the **finite hyperbolic** SUCC prefix with weights `n^(-sigma)/D_H(sigma)`, they are generally *not* independent.

For `H=6`, `sigma=2`, `p=2`, `q=3`, exact rational calculation gives

\[
\boxed{\operatorname{Cov}_H(1_{2\mid N},1_{3\mid N})
=-\frac{10800}{4118023}<0.}\tag{TMF.11}
\]

Even though `n=6` is now permitted, the global natural cutoff still correlates the two prime clocks. At `H=5`, their simultaneous activation is impossible and covariance is strictly negative. For general H, conditioning on `N<=H` differs in total variation by at most `R_H/zeta(sigma)<=R_H/D_H(sigma)`, where `R_H<=H^(1−sigma)/(sigma−1)`. As global covariance is 0, the finite covariance magnitude is <=`3R_H/D_H(sigma)`. This is an exact finite-world coupling bound. It converges to zero only after controlling the natural source tail at `sigma>1`.

At `sigma<=1` the full normalized zeta source does not exist, so promoting prime independence from finite boxes to a global positive law is not lawful. This is a good **law-of-small-numbers/source-map** test for SUCC rather than an RH proof or a new prime-correlation asymptotic.

## TMF-09. Adversarial completed-source firewalls (EXACT)

1. **Fake composite 6:** genuine finite source with p=2,3 gives Dirichlet coefficient of 6 equal 1. Appending an illegal independent Euler base 6 changes that coefficient to **2**. Both finite models have positive coefficients and positive characteristic Grams. Hence **positive covariance does not authenticate Euler arithmetic**.
2. **Wrong first Euler weight:** using `alpha_2=3/2` changes coefficient of n=2 from 1 to 3/2; it may still define a positive normalized finite source. The mismatch must be detected before any positivity claim.
3. **Wrong real parity:** normalizing the even real Gaussian at `s0=2n+2` gives `pi E[r²]=n+1`; shifting the Tate test by `|r|` (odd local factor) changes it to `n+3/2`. A mistaken `2pi` scale instead gives `(n+1)/2`. All are exact rational signatures after the pi rescaling.
4. **Pole removal is not an automatic positive multiplier:** for `P(s)=s(s−1)/2`, the normalized scalar at `s=2+2i` has squared modulus **10>1**. Hence `P(2+2it)/P(2)` is not itself a characteristic function. This does **not** establish that any whole product with `P` is non-positive; it simply blocks the inference that multiplication by the completion polynomial automatically preserves probability-positive structure.
5. **Finite factorial counterfeits and phase gauges** remain valid hostile cases from parent PR #145; the new source labels do not magically remove them.
6. **No shared-provenance inflation:** Beta and finite exponential delays are the *same* law, the Dirac chart is a distinct positive quadrature source with the same target, the integer Dirichlet sum and genuine FUCC valuation product are two coordinate/decomposition routes for the same arithmetic source. These are useful different implementations, not independent physical attestations.

## TMF-10. What did and did not change for signed Weil (STATUS BOUNDARY)

The prior repository already gives the complete classical signed Weil distribution, with source authentication and signed prime/Archimedean/pole/contact terms (see `docs/CLAIM_SUPPLEMENT_CARRIER_TATE_WEIL.md`, CTW-07 through CTW-14), as well as scoped Suzuki high-subspace positivity (`docs/RESEARCH_FRONTIER_2026-10-15.md`). This branch adds **positive-source** Tate-Mellin transports and explicit compact prime-power data, but it does **not** identify any positive characteristic Gram with that signed distribution.

The unresolved low Schur sign `S0=A−R0`, all-support test-domain transport, and source-derived completed Weil sign are unchanged. Assuming that source-positive Gamma×Euler on `Re(s)>1` implies signed Weil positivity would be a circular/non sequitur leap. RH remains open.

### Priority next-round experiments and falsifiers

* **Test-function diagram:** carry explicit compactly supported smooth log tests through local Tate/Poisson and the completed signed Weil distribution with quantified Gamma tails, both residues, contact, and authentic half-density. Distinguish *distribution on tests* from a positive probability law.
* **Counterfeit intercept:** use the fake 6 and changed `alpha_2` to verify that the signed prime-power atomic coefficients change; positive Grams must **not** pass source identification.
* **High/low Schur:** on a specified compact support, identify the exact signed Weil form and its certified low/high blocks; use independent outward interval bounds before any finite eigenvalue/sign promotion.
* **Hyperbolic versus box controls:** compare prime-valuation rank and natural cutoff at new larger holdouts and moving windows; quantify the finite prime covariance induced by natural prefix restriction.
* **Formalization:** Lean/YEAN targets: `TMF.7` hyperbolic valuation bijection, finite Beta/Dirac triangle assumptions, prime Euler total-variation coupling, and the escape quantifiers in `TMF.10`. Proof in a standard formal system is **not yet delivered**.
* **Identity stress:** distinguish gamma `a=n+1` even anchors from odd-parity Gamma shifts, characters, and non-Euler Dirichlet mutants. Any proposed extension to the critical strip must preserve source law and be allowed to return an obstruction.

## Reproducibility, scope, and provenance

Fresh **native, non-archival** files:
`observational_succ/tate_mellin_prime_transport.py`,
`tests/test_tate_mellin_prime_transport.py`,
`scripts/tate_mellin_prime_transport_probe.py`,
`research/2026-10-16/SUCC_FUCC_TATE_MELLIN_SOURCE_TRIANGLE.md`,
`research/2026-10-16/TATE_MELLIN_PRIME_TRANSPORT_RECEIPT.json`,
`docs/CLAIM_SUPPLEMENT_TATE_MELLIN_PRIME_TRANSPORT.md`.

Run targeted tests and receipt:

```sh
python -m unittest discover -s tests -p 'test_tate_mellin_prime_transport.py' -v
python -m unittest discover -s tests -p 'test_factorial_gamma_fucc.py' -v
python scripts/tate_mellin_prime_transport_probe.py --verify
```

No background CI claim. All numerical evaluations must be scoped as **OBSERVED only**; mathematically guaranteed rational bounds are derived above. Full repository CI >10 minutes is a separate queued GitHub workflow; do not claim success unless it completes. Historical imports remain untouched.

### Sources / dependency families

* Parent SUCC: `research/2026-10-16/FACTORIAL_GAMMA_FUCC_SUCC.md` (FGF-1–10), `DIRAC_SUCC_GAMMA_CONTINUUM.md` (DGC-1–5), `GAMMA_BAND_UNIFORM_DEALIAS.md` (BGD-1–7).
* Existing SUCC completed test identification: `docs/CLAIM_SUPPLEMENT_CARRIER_TATE_WEIL.md`, `research/2026-10-15/TATE_TO_WEIL_DISTRIBUTION.md`.
* Classical Tate local and global zeta integrals: Tate (Princeton dissertation 1950; printed 1967); expository lecture §7 *Tate's Thesis and Applications* (Fourier Analysis on Number Fields, https://webusers.imj-prg.fr/~julien.marche/Ref_GL_GT/Fourier_Analysis_on_Number_Fields.pdf).
* Classical Euler product / divergence of reciprocal primes, Weierstrass–Gamma/Poisson and elementary total-variation couplings: **imported** theorems, proofs as stated above for the particular source charts. Independent implementations help catch arithmetic mistakes but do not confer originality on these identities.
