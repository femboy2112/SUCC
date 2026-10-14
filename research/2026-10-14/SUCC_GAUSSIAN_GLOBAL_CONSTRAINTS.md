# SUCC-GAUSSIAN — authentic finite-prime boreholes and bounded global curves

**Source pin:** SUCC PR #73, \`research/source-interaction-adelic-analytic-gluing-2026-10-14@9405013730d8b11d016e42736146243a77ff3d5e\`. Sibling PRIME-SPHERE/Suzuki branches are context, not merged ancestors. **RH PROVED: NO.** Classical tools: completed Jacobi theta, Bargmann–Fock RKHS, Gaussian-process conditioning, Rouché's theorem, analytic identity theorem. This is a source-aware new-to-SUCC assembly, not a claim of academic priority or external physical verification.

## G1. Why there are three different Gaussians

(a) The **source Gaussian** \`e^(-pi x²)\` at the real place is an authentic test state of the theta/Poisson construction. (b) Pascal's diffusive Gaussian/heat kernel and Suzuki's positive Gamma/OU operator are *analytical dynamics*. (c) A Gaussian process is an OPTIONAL prior over candidate global curves. These are not equivalent objects. Statistical credible bands never become proofs of arithmetic without a separate source-derived constraint.

## G2. Proven whole-plane Gaussian-Fock energy bound for the ORIGINAL completed zeta

The exact parent theta source gives
\`xi(s)=1/2+s(s-1)J(s)/2\`,
\`J(s)=int_1^infty psi(t)[t^(s/2-1)+t^((1-s)/2-1)]dt\`,
\`psi(t)=sum_(n>=1)exp(-pi n²t)\`.
Define \`F(z)=xi(1/2+z)\`; its authentic functional equation gives \`F(z)=F(-z)\`. The source formula becomes
\`F(z)=1/2+(z²-1/4)int_1^infty psi(t)t^(-3/4)cosh(z log t/2)dt\`.

For t>=1, elementary \`pi>3\` and \`n²>=1+3(n-1)\` imply \`psi(t)<2exp(-3t)\`. Calculus yields \`log t<=sqrt(t)\`, and Young yields \`|z|sqrt(t)/2 <= |z|²/8+t/2\`. Therefore the absolute value of the integral is below \`(4/5)e^(-5/2)e^(|z|²/8)<e^(|z|²/8)\`; hence
\`|F(z)| <= (1+|z|²)e^(|z|²/8)\`.

In classical Fock space \`||F||²=pi^-1 int_C |F(z)|² e^(-|z|²)dA(z)=sum_n n!|[z^n]F|²\`, polar integration gives a fully explicit SOURCE-DERIVED bound
\`boxed: ||F||² <= int_0^infty(1+u)²e^(-3u/4)du=260/27\`. (G2)

The even Fock kernel is \`K_even(z,w)=cosh(z conjugate(w))\`. This is a hard analytical regularity bound for the actual arithmetic Xi, not a GP prior.

## G3. Certified zero-free disk without reading zeros

The parent theta proof gives \`F(0)=xi(1/2)>59/120\`. By the even Taylor/Fock Cauchy–Schwarz inequality,
\`|F(z)-F(0)|² <= (260/27)(cosh(|z|²)-1)\`.
The exact positive-term inequality \`cosh(x)-1<=x²/[2(1-x²/12)]\` for \`x²<12\`, at \`R=47/100\`, yields
\`(260/27)R^4/[2(1-R^4/12)] = 2537434120/10756082871 < 3481/14400=(59/120)²\`.
Therefore **the genuine xi(s) has NO zeros in the CLOSED disk \`|s-1/2|<=47/100\`**. This is a deliberately small, classical-style disk, dramatically weaker than known global zero data; not RH.

## G4. Gaussian boreholes from finite real Euler observations

For integer \`sigma>=2\`, a complete finite menu of genuine prime places \`p<=P\` gives the exact positive product \`Z_P(sigma)=prod_(p<=P)(1-p^-sigma)^-1\`. Every omitted positive integer has some factor >P, hence
\`0<=zeta(sigma)-Z_P(sigma)<=P^(1-sigma)/(sigma-1)\`. Multiply by the correctly normalized \`sigma(sigma-1)Gamma_R(sigma)/2\`, which is a rational times a power of pi^-1 for integer sigma, to get an exact rational interval for **the real global xi value**. The code authenticates every p, rejects composite 6 and missing primes, and does not extend a divergent Euler sum into Re<=1.

Now choose the nowhere-zero even analytic gauge \`H(z)=exp(-z²/2)F(z)\`. Its RKHS norm is the same bounded source norm, and its real-axis kernel is the **symmetrically reflected squared-exponential Gaussian**
\`k_even(x,y)=[e^(-(x-y)²/2)+e^(-(x+y)²/2)]/2\`.
The second term is imposed by Xi's functional-equation symmetry, not fitted to borehole data. The unit kernel length is a *declared Hilbert metric*, not an empirical covariance estimate.

For an exact observation \`H(x)=y\`, with \`G=k(x,x), k=k(z,x), T=k(z,z)\`, Hilbert-space projection gives the SHARP possible-value interval
\`|H(z)-(k/G)y|² <= (B²-y²/G)(T-k²/G)\`, \`B²=260/27\`.
The implementation accepts a finite-prime **interval** for y, propagates all errors by rational Taylor/Gaussian kernel enclosures and rounds the square-root upward. P=11,sigma=3 gives \`0.5733324272...<xi(3)<0.5753054225...\`; for the target H(12/5) the certified radius is <0.219 instead of an unconditional radius >2.19. Source uncertainty remains large and allows negative values; no conclusion about RH or positive signs is drawn.

The same projection matrix formula on finitely many samples gives conditional GP mean and variance **if a prior is explicitly declared**. GP sample paths generally do not have finite native RKHS norm; the deterministic source Xi bound does not license interpreting it as a GP sample.

## G5. Rouché contour counts and the no-unique-curve theorem

If the source has certified even Taylor prefix \`P_d(z)=sum_(j<=d)a_j z^(2j)\`, Fock norm bound B² yields the exact missing tail
\`|F(z)-P_d(z)|² <= (B²-sum_(j<=d)(2j)!|a_j|²)*sum_(j>d)R^(4j)/(2j)!\`
on \`|z|=R\`. The sum has a rational geometric upper bound based on its first term. If a selected known monomial dominates all other known terms plus this upper bound, Rouché proves the **exact number 2j of zeros in the disk**. The code handles that strict inequality without looking up any zeros.

**Necessary negative theorem:** finite point values, finite jets, symmetry and an energy cap with slack never uniquely select an entire curve. Explicit invisible even Fock polynomials are
\`h(z)=z^(2(d+1))prod_i(z²-x_i²)\`, yielding continuum-many nearby curves with identical finite reports. Only full-source germ identity on a nonempty OPEN subset of the Euler half-plane (as PRs #72/#73 already prove) selects a unique analytic continuation by the identity theorem. This is a distinction between hard allowed-model geometry and GP probability.

## G6. Scope and next tests

Mathematically, the source Gaussian offers a way to convert finite SUCC place data into rigorous **global analytic evaluation tubes**, and, with stronger certified jets, **Rouché zero-count regions**. It does not make the set of admissible whole curves finite, derive the Weil sign, or show any off-line zero impossible globally.

Next tasks: source-certified higher even Xi Taylor jets from full theta with rational quadrature and derivative tails; multi-probe complex-valued interval matrix inversion; genuine conductor/parity chi4 controls; comparison against Suzuki's signed original Weil form rather than arbitrary PSD Gaussian covariance. The full original-source/domain matching requirements stay active. No zero-list oracle, Lean result or independent academic priority is claimed.
