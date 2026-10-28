# Circle → line: source-relative stability of SUCC virtual paths

**2026-10-28.** Research-only child of [PR #352](https://github.com/femboy2112/SUCC/pull/352) at fixed parent SHA \`f7baa52f0052a29687cf729d1cbe9e1bcc828dc6\`. The original OLZF-04 divisor fibers and PCR-02 Pólya birth law are retained unchanged. These elementary statements are proved in their stated domains; academic novelty, formal Lean validation, a zeta-zero spectral realization, RH and pi normality are **UNVERIFIED / OPEN**.

## Recover the actual source

For positive integer n, SUCC uses
$$\mathcal H_n=\operatorname{span}\{|a,b\rangle:ab=n\},\qquad
\omega_n=d(n)^{-1/2}\sum_{ab=n}|a,b\rangle,$$
and the source-imbalance observable
$$D|a,b\rangle=\log(a/b)|a,b\rangle.$$
For a genuine prime p and exponent j≥0 let m=j+1, L=log p, and |k>:=|p^k,p^(j-k)> (0≤k≤j). Then D|k>=(2k-j)L|k>, and the source state is the uniform sum over k. This is the precise object, not a zeta-zero eigenstate.

## CSL-01: exact source fidelity under circle-to-line tilt

For real t and epsilon, put
$$\phi_{t,0}=e^{itD}\omega_{p^j},\qquad
\phi_{t,\varepsilon}=\frac{e^{itD-\varepsilon D}\omega_{p^j}}
{\|e^{-\varepsilon D}\omega_{p^j}\|}.$$
The co-moving squared fidelity compares with the legitimate phase-transported source:
$$F_{p^j}(\varepsilon)=|\langle\phi_{t,0},\phi_{t,\varepsilon}\rangle|^2.$$
The phase t cancels. Writing r=p^(-2 epsilon)>0, the amplitudes of the tilted state are proportional to 1,r,...,r^j and therefore
$$\boxed{F_{p^j}(\varepsilon)=
\frac{(\sum_{k=0}^j r^k)^2}{(j+1)\sum_{k=0}^j r^{2k}}.}$$
Geometric sums give, for epsilon≠0,
$$\boxed{F_{p^j}(\varepsilon)=
\frac{\coth(|\varepsilon|\log p)\,
\tanh((j+1)|\varepsilon|\log p)}{j+1}.}$$
For epsilon=0 the fidelity is 1 for every j. For j≥1 and epsilon≠0, strict Cauchy–Schwarz gives 0<F<1; for j=0 the one-dimensional fiber has F=1 always.

**Exact limit:** for every fixed p and nonzero epsilon,
$$F_{p^j}(\varepsilon)\sim\frac{\coth(|\varepsilon|\log p)}{j+1}\longrightarrow0.$$
The normalized nonunitarily tilted vectors become asymptotically orthogonal to the original marked source as prime-power depth increases. This is a sequence of finite-fiber limits, not the existence of an infinite physical state. The surviving tilted distribution is generally geometric rather than every path vanishing.

## CSL-02: narrow coherence window, noncommuting limits

Set epsilon_j=c/((j+1)log p), with fixed real c. Then for c≠0
$$F_{p^j}(\varepsilon_j)=
\frac{\tanh|c|}{j+1}\coth\Big(\frac{|c|}{j+1}\Big)
\longrightarrow\frac{\tanh|c|}{|c|}.$$
The c=0 limit is 1. Thus the boundary-layer width is 1/((j+1)log p), and the two limits do not commute:
$$\lim_{\varepsilon\to0}\lim_{j\to\infty}F=0,\qquad
\lim_{j\to\infty}\lim_{\varepsilon\to0}F=1.$$
The elementary inequality 1/x<coth(x)≤1/x+x/3 for x>0 yields a finite-depth error at c>0:
$$0\le F-\tanh(c)/c\le c\tanh(c)/(3(j+1)^2).$$
The upper inequality follows by differentiating (1+x²/3)sinh(x)-x cosh(x); its derivative is x(x cosh x-sinh x)/3≥0.

## CSL-03: the native Pólya law forces a derivative correction

The inherited PCR-02 two-channel Pólya birth matrix P_m has column k supported on output k,k+1 with weights (m-k)/(m+1) and (k+1)/(m+1). Define v_m(r)=sum_(k=0)^(m-1) r^k|k>. An exact row calculation gives
$$\boxed{P_m v_m(r)=\frac m{m+1}v_{m+1}(r)
+\frac{1-r}{m+1}\frac{\partial v_{m+1}(r)}{\partial r}.}$$
Indeed, in output row ell≥1 the residual from (m/(m+1))r^ell equals ell(1-r)r^(ell-1)/(m+1). Output row 0 fixes any scalar proportionality to m/(m+1); row m then forces r=1. **For every r>0 distinct from 1, the native P_m does not propagate the tilted geometric profile up to scalar.** Repetition of a fixed nonzero real tilt would require a correction at every grade or an explicitly altered source operator. At r=1 the derivative disappears and the original uniform source is selected.

This is the operational meaning of “persistent selective path realization.” It does not prevent valid unitary phase-gauge transport when the gauges and channel are transported together as in PCR-03. A real tilt changes path weights and cannot be called a passive basis change.

## CSL-04: Fourier circle vs hyperbolic line, operator domain

The inherited source character is entire in z:
$$\chi_{p^j}(z)=\langle\omega,e^{izD}\omega\rangle
=\frac{\sin((j+1)z\log p)}{(j+1)\sin(z\log p)},$$
interpreting removable values by the finite exponential sum. For real t, e^(itD) preserves Hilbert norm. Yet chi_p(t)=cos(t log p) can vanish on the unit circle; cancellation of a matrix coefficient does **not** mean state-norm loss.

For z=i epsilon the character becomes the sinh ratio and grows with prime-power depth for epsilon≠0; a nonunitary tilt is not a normalized correlation. On the direct-sum Hilbert space ell²(N×N), D is self-adjoint multiplication by log(a/b). e^(itD) is unitary for t real. For epsilon≠0, e^(itD-epsilon D) is an unbounded operator with a dense natural domain: its action on a basis vector |p,1> or |1,p> has norm p^|epsilon|. Even the marked p-fiber vector obeys
$$\|e^{-\varepsilon D}\omega_p\|^2=\cosh(2\varepsilon\log p)\to\infty.$$
After separately renormalizing the marked two-path state, its minority-path probability is 1/(1+p^(4|epsilon|))→0 as p→infinity. This is selective history reweighting, not the entire field “going to zero.”

## CSL-05: the conditional RH boundary—not an RH proof

If every nontrivial zeta zero rho corresponded to a **nonzero** positive-norm vector v_rho and a uniformly bounded two-sided group W(u) with W(u)v_rho=e^(u(rho-1/2))v_rho for all real u, boundedness for both signs would force Re rho=1/2. If all zeros were represented, RH would follow.

**Missing theorem:** construct that complete zero-to-mode map, its domain, a source-authenticated inner product, completed gamma/pole contribution and boundedness from SUCC's actual arithmetic. D's diagonal eigenvalues log(a/b) are not zeta ordinates. Identifying epsilon with Re rho-1/2 is at present only a proposed dictionary, **not** a derived equivalence. The finite Euler product and Dirichlet series are absolutely convergent only for Re s>1; analytic continuation must not be replaced with a limit of normed source vectors in the critical strip.

## CSL-06: adversarial controls prevent a fake RH proof

For every 1<a<cosh 2 define
$$G_a(s)=a+\cosh(4(s-1/2)).$$
On the critical line G_a(1/2+it)=a+cos(4t), a Fourier transform of the positive measure a delta_0+(delta_4+delta_-4)/2. Nevertheless its simple zeros are
$$s=1/2\pm\operatorname{arcosh}(a)/4+(2k+1)\pi i/4,$$
off the line and inside the critical strip for an **open** interval of a. They persist under small variations of a: analytic-zero structural stability differs from boundedness of a normalized dynamical eigenmode. This is not a counterexample to RH; the source is not the true Euler/Gamma data.

The companion PR #352 already shows: a non-Pisot rational clock p+1/p can preserve exactly the zeta zero divisor; a fake independent primitive 4 also preserves the zero divisor while corrupting original arithmetic coefficients; an actual Pisot clock collision beta_11^7=beta_29^5 loses prime history without original labels. Such controls must remain. The native two-channel torus deformation gives zeta(s-tau)zeta(s+tau), not the authentic single zeta: silently substituting it would be source replacement.

## Verdict / research debt

**PAPER-PROVED LOCAL:** exact path fidelity, sharp scale, noncommuting limits, native Pólya derivative defect, unbounded real tilt. **CLASSICAL CONDITIONAL:** complete positive two-sided spectral representation would force RH. **REFUTED SHORTCUT:** generic positive Fourier correlation or analytic-zero structural stability forces critical-line zeros. **UNVERIFIED:** a source-complete map from completed-zeta zeros to the actual SUCC path evolution and a suitable Weil-positive invariant form.

Next discriminator: recover the authentic prime powers, gamma place, completed explicit formula, true source-derived pairing, and reject G_a/fake-4/non-Pisot controls without inserting the critical-line condition. Reference mathematics: NIST DLMF §27.4 (https://dlmf.nist.gov/27.4), Taylor spectral theorem (https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/chap8.pdf), Bombieri–Lagarias 1999 (https://doi.org/10.1006/jnth.1999.2392).