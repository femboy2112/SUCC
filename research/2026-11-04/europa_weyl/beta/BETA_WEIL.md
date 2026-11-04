# From the marked angular source to the signed beta distribution

This is a research result at the #499 source (4ff640637d18b8161599402f7c6ba23388a63652). The frozen conductor-one zeta checker in `observational_succ/source_weil_interface.py` describes a different target. We use the primitive odd character of conductor four. All integrals below are over the declared coordinates; nothing uses numerical zero ordinates.

## Finite source, exact Mellin interpolation

Let the primal have the eight taps of PQ-4, seed zero and multiplier 16. Put
\[
 K(t)=\frac4{1+(1-t)^2},\qquad D(t)=1-t^8/16,
 \qquad P(t)=D(t)K(t).
\]
The source at block n is the integral of \(t^{8(n-1)}P(t)\) on [0,1]. Thus the first N chronological blocks give the polynomial
\(K^{[N]}(t)=P(t)\sum_{j=0}^{N-1}(t^8/16)^j\).
Use the endpoint reversal x=1−t of the marked oriented unit segment and normalize by K(1)=4. This selects a particular coordinate, not a property of all reparametrizations. The reflected polynomial and its Dirichlet transform are
\[
 Q_N(x)=K^{[N]}(1-x)/4
       =\frac{1-16^{-N}(1-x)^{8N}}{1+x^2}
       =\sum_{m=1}^{8N-1}b_{N,m}x^{m-1},
 \qquad B_N(s)=\sum_m b_{N,m}m^{-s}.
\]
It really is a polynomial: both roots of the denominator are roots of its numerator. Each index N uses only the first N blocks of the declared source. Integrating either coordinate proves exactly
\[
 B_N(1)=\frac{16^{1-N}}4Y_N.
\]
This last normalization uses the zero seed. A scalar Y_N alone does not encode all the coefficients of the polynomial. Its construction uses the marked source blocks.

The infinite reflected transfer is \(Q(x)=1/(1+x^2)=\sum_{m\ge1}\chi(m)x^{m-1}\) for |x|<1, where \(\chi(2m)=0\), \(\chi(4m+1)=1\), \(\chi(4m+3)=-1\). On substituting x=exp(−u), the usual Mellin integral, initially for Re(s)>1, yields
\[
 \beta(s)-B_N(s)=\frac{16^{-N}}{\Gamma(s)}
   \int_0^\infty u^{s-1}\frac{e^{-u}(1-e^{-u})^{8N}}
                                      {1+e^{-2u}}\,du.                 \tag{1}
\]
The integral converges holomorphically for Re(s)>−8N by its behavior at zero; at infinity there is exponential decay times a power of u. Thus (1) continues through this half-plane. In Re(s)=σ>0 its absolute error is bounded by \(16^{-N}\Gamma(\sigma)/|\Gamma(s)|\), uniformly up to a constant on compact subsets. Pointwise accuracy here alone gives no bounds on fractional parts after multiplying by \(16^N\).

**Exact negative special values and sharp boundary.** For each integer \(0\le j<8N\), \(B_N(-j)=\beta(-j)=E_j/2\), with \(\sum E_jz^j/j!=1/\cosh z\). At the next integer,
\[
 \beta(-8N)-B_N(-8N)=\frac{(8N)!}{2\,16^N}.
\]
Indeed \(1/\Gamma\) vanishes at the first 8N points. The integrand apart from \(u^{s-1}\) has Taylor leading coefficient \(u^{8N}/2\); subtract this term on [0,1] to continue its Mellin transform across −8N with residue 1/2. Since 8N is even, the linear coefficient of \(1/\Gamma(s)\) there is \((8N)!\). Finally, the untruncated heat kernel is \(e^{-u}Q(e^{-u})=1/(2\cosh u)\). Its Mellin residues, divided by Gamma, give the asserted Euler numbers (odd ones vanish). This proves the first failure for every N. For N=1, \(B_1(1)=109/140\) and the first mismatch is exactly 1260 at s=−8.

This is a transport from the *source kernel*. It gives point interpolation at distinct negative integers, not equality of successive derivatives at one point. The exact finite complex Euler series transformation applied at i reproduces this truncation; high forward differences annihilate polynomial inputs of degree below 8N. The negative-integer termination is therefore a specialization of classical Euler transformation. The declared block cutoff and the endpoint normalization are supplied by the source.

## Primitive completion

The reflected coefficient sequence defines a completely multiplicative character of conductor 4. The values +1 and −1 on 1 and 3 distinguish residues modulo 4 that coincide modulo 2, proving primitivity. It is odd. For the convention \(e(v)=\exp(2\pi i v)\) its Gauss sum is \(e(1/4)-e(3/4)=2i\). Thus the root number is \(2i/(i\sqrt4)=1\). In particular the ramified Euler factor at 2 is 1.

For a direct derivation, put \(T(v)=\sum_{n\ge1}n\chi(n)e^{-\pi n^2v/4}\). Poisson summation on each residue class gives \(T(v)=v^{-3/2}T(1/v)\). Specifically take the Fourier kernel \(e(-x\xi)\). The transform of \(x e^{-\pi v x^2/4}\) is \(-i(4/v)^{3/2}\xi e^{-4\pi\xi^2/v}\). The mod-4 class sum is \(2i\chi(k)\) at frequency k/4, and the factor from Poisson is 1/4; the full integer sums on both sides are twice T. The Mellin transform in \(v^{(s+1)/2}dv/v\) is
\[
 \Lambda(s)=(4/\pi)^{(s+1)/2}\Gamma((s+1)/2)\beta(s).
\]
The transformation and rapid decay at both ends continue it to an entire function and give \(\Lambda(s)=\Lambda(1-s)\). Direct integration of Q gives \(\beta(1)=\pi/4\), hence \(\Lambda(1)=\Lambda(0)=1\). Equivalently \(\beta(0)=1/2\). The negative odd trivial zeros of beta cancel the Gamma poles in the completion.

## A signed distribution on one specified test space

Let \(g\in C_c^\infty(\mathbb R;\mathbb C)\),
\(H(z)=\int g(x)e^{izx}\,dx\), and use \(g(x)=(2\pi)^{-1}\int H(t)e^{-itx}\,dt\).
For the nontrivial zeros counted with multiplicities, set
\[
 W_\chi(g)=\sum_{\Lambda(\rho)=0}H((\rho-1/2)/i).
\]
The ordinates in this definition may be complex. On each bounded horizontal strip H decreases faster than any inverse power in the real direction, by integration by parts, so the zero sum converges absolutely by standard zero counting. The evaluation requires no zero ordinates on the arithmetic side. The signed formula in these conventions is
\[
 W_\chi(g)=g(0)\log(4/\pi)
 +\frac1{2\pi}\int_{\mathbb R}H(t)\Re\psi(3/4+it/2)\,dt
 -\sum_{p,k\ge1}\chi(p)^k\frac{\log p}{p^{k/2}}
           \{g(k\log p)+g(-k\log p)\},                         \tag{2}
\]
where p ranges over primes and \(\psi=\Gamma'/\Gamma\). Only finitely many powers hit a compact support. Pole contribution is zero. The constant uses the conductor and real Gamma normalization once each. The odd shift is 3/4 at the central line; replacing it by 1/4 gives the even-parity form.

For the derivation take \(F(s)=H((s-1/2)/i)\). The residue theorem for \((\Lambda'/\Lambda)(s)F(s)\) on lines c and 1−c (1<c<2 suffices), followed by the functional equation, gives the right-line integral of \((\Lambda'/\Lambda)(s)[F(s)+F(1-s)]\) with measure ds/(2πi). Standard horizontal heights avoiding zeros and rapid transform decay justify the contour limit. On that line, the Euler logarithmic derivative is the absolutely convergent Dirichlet series with coefficients \(-\chi(p)^k\log p\). Each vertical integral gives \(p^{-k/2}g(\pm k\log p)\) by inversion of the exponentially tilted test. Shift just the Gamma/conductor integral to 1/2 (no poles in this strip). The two gamma terms, after t↦−t in one, combine to the displayed real part. The conductor contributes twice its half constant. This also proves (2) on general complex g, with no evenness restriction.

For the Weil quadratic form use \(g=f*\tilde f\), \(\tilde f(x)=\overline{f(-x)}\). Then \(H(z)=\hat f(z)\overline{\hat f(\bar z)}\). Positivity of (2) on this entire class is the global Weil criterion for the beta GRH. Under GRH all terms on the zero side become squared moduli. Neither this conjecture nor zeta RH is established by these constructions. The linear distribution takes both signs even on nonnegative g; this does not assert the existence of a negative quadratic test.

Away from the origin the archimedean term has density
\(-e^{-3|x|/2}/(1-e^{-2|x|})\). This follows from the convergent subtraction
\[
 A(g)=(\log(4/\pi)-\gamma)g(0)
 +\int_0^\infty\frac{e^{-u}g(0)-e^{-3u/4}(g(u/2)+g(-u/2))/2}
                      {1-e^{-u}}\,du.                            \tag{3}
\]
The integrand is bounded at zero. This time-domain formula retains the contact term. As a calibration take a nonnegative smooth bump of height 1 at log(p), bounded by 1 and supported within radius 1/64 there, for p=3 or 5. These supports lie above log 2, hit only that prime power, and miss the origin. The density has magnitude less than 1 there. Therefore \(-1/32<A(g)<0\). The two intervals for \(W_\chi(g)\) derived from exact rational outer bounds for logarithms and square roots are [0.603,0.635] at 3 and [−0.752,−0.719] at 5. Omitting the minus sign of the Euler term reverses this test. At 9 the local atom has the same Euler sign as at 5, and 2 has zero weight.

## A finite-rank obstruction that survives the source marking

If \(f\in C_c^\infty(I)\), where I is any interval of length \(0<\ell\le1/2\), set \(g=f*\tilde f\). Its support lies in [−ℓ,ℓ], below the first surviving Euler atom log 3. Also \(g(0)=\|f\|_2^2\) and \(\Re g(v)\le g(0)\) by Cauchy–Schwarz. Split (3) at u=2ℓ. The portion above this cutoff contributes exactly \(-g(0)\log(1-e^{-2\ell})\). On \(0<u\le 2\ell\le1\) use \(e^{-3u/4}-e^{-u}\le u/4\) and \(1-e^{-u}\ge u/2\); the loss is at most \(\ell g(0)\). Since \(1-e^{-2\ell}\le2\ell\), \(\log(4/\pi)>0\) and \(\gamma<1\), we obtain
\[
 W_\chi(f*\tilde f)\ \ge\ [\log(1/(2\ell))-1-\ell]\|f\|_2^2.       \tag{4}
\]
For ℓ=1/16 the coefficient exceeds 15/16. Thus the signed completed form is **strictly positive on an infinite-dimensional local test space, unconditionally**. In particular if D maps this space linearly into *any* finite-dimensional complex space of dimension d, then a nonzero f in the kernel of D violates any proposed identity \(W_\chi(f*\tilde f)=Q(Df)\) for a form Q with Q(0)=0. One explicit construction uses any d+1 disjoint bumps in I and solves the homogeneous d-row linear system. This applies to all finite source conductor operator spaces, independently of their magnitude and of the chosen state. It does not obstruct a restricted finite test domain or a family of maps with an infinite limit. A proof on restricted domains must specify the map, measure and convergence of the signed values before applying (2).

A second obstruction uses the actual first two-point dyadic epoch. Shift the primal seed by s, preserving its entire forcing, reflected kernel, beta distribution and local Frobenius character. The observed separation \(Y_3-Y_2\bmod1\) is 66050246/66927861 at s=0 or 1/5, but 37366877/66927861 at s=1/7. The latter is unequal even up to sign. Consequently the absolute two-point Fourier coefficient at h=1 changes, since its square is \((1+\cos(2\pi(Y_3-Y_2)))/2\). For a one-point epoch the optimized defect modulus is always identical. This controls the seed dependence of the state and the limits of a factorization via the reflected kernel alone. It does not rule out a zero-seed theorem that uses additional chronological information.

## Verdict, reproducibility and source contact

Source DAG: original eight taps → character projection in the actual source module (#499) → chronologically truncated polynomial → oriented endpoint reflection and normalization → Dirichlet polynomial B_N; separately its s=1 specialization → exact selected epoch endpoint. Infinite reflected coefficients → primitive character → Euler logarithmic derivative and theta completion → signed distribution (2). No equality between empirical Gram and (2) is inserted. Existing root work handles the number of signed Euler coefficients recoverable exactly from one truncated kernel.

The source-dependent finite interpolation and earliest failure are paper-proved. Formula (2) and its elementary consequences have classical authority. The honest local comparison is (4) and the two-point seed counterexample. The open step for the real circle is cancellation after the rescaling \(4\cdot16^{N-1}B_N(1)\), uniformly across actual chronological windows. The exact bounds in (1) concern the unrescaled beta family. A verdict-changing signed bridge must give a family of source-marked test maps, preserve the Euler and Gamma terms and avoid the kernel obstruction in (4); for normality it must bound the actual dyadic selected energy. The construction is source-faithful at all N; proof derivation and regression code share the original source and are not independent academic confirmation.

Run `python3 europa_probe.py` here to regenerate `receipt.json`. Integer arithmetic verifies the registered special-value ranges, Dirichlet series division through 275, seed controls and rigorous single-atom enclosures. The executable evaluates finite arithmetic and the two test intervals. The general distribution identity and (4) have analytic proofs above, not formal certificates. A mended diagram or a sign match does not upgrade the real-circle status.

Primary literature and overlap:

- A. Weil, *Sur les « formules explicites » de la théorie des nombres premiers* (1952), original general formula and positivity criterion. [Transcription](https://denisevellachemla.eu/transc-Weil-1952.pdf).
- J.-F. Burnol, *Sur les formules explicites I : analyse invariante* (2000), expressly studies short-support positivity; the principle behind (4) has precedent. [Article](https://doi.org/10.1016/S0764-4442(00)01687-6).
- J. Sondow, *Analytic continuation of Riemann's zeta function and values at negative integers via Euler's transformation of series* (1994), and J. Guillera / J. Sondow on the Lerch transcendent (2008). Finite-difference special values and Mellin continuation have prior art. [Sondow](https://doi.org/10.1090/S0002-9939-1994-1172954-7), [Guillera–Sondow](https://arxiv.org/abs/math/0506319).
- D. Barsky, V. Muñoz and R. Pérez-Marco, *On the genesis of BBP formulas* (2021), for complex BBP and angular identities. [Publisher](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/198/4/114065/on-the-genesis-of-bbp-formulas).
- NIST DLMF §25.15 independently specifies the primitive Dirichlet L-function convention, Euler product and functional equation. [DLMF](https://dlmf.nist.gov/25.15).

No academic priority is asserted for this source-specific composition, constants or truncation. No hosted CI, formal compilation, or outside expert review is represented by the local receipt.
