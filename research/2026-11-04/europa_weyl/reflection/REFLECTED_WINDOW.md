# Which signed Euler coefficients can one finite BBP prefix recover?

For N full chronological angular blocks, write w for the character projection of the original signed taps, P(t)=Σ w_j t^(j−1), and Q_N(x)=P(1−x)Σ_{k<N}((1−x)^8/16)^k/4. The reversal exchanges the marked endpoints of [0,1]; the scalar is the exact angular kernel at 1. An arbitrary reparametrization of the interval need not have these coefficients. The source-derived identity
$$
 Q_N(x)=\frac{1-16^{-N}(1-x)^{8N}}{1+x^2}
$$
is a polynomial of degree 8N−2. The local object in this theorem is a finite polynomial with its full marked taps. Its integral gives the zero-seeded lift, but knowing its integral alone does not determine its coefficients among arbitrary polynomials.

**Theorem (strict decoding threshold).** Let λ∈(0,4) solve 8H(λ/8)=log 16 with H(x)=−x log x−(1−x)log(1−x). Let g=log((8−λ)/λ). The first degree l at which [x^l]Q_N lies at distance ≥1/2 from χ₋₄(l+1) is
$$
 l=\lambda N+\frac{\log N}{2g}+O(1).
$$
Here λ≈0.8802229155 and g≈2.090456507. This is the failure threshold of this specified coefficientwise nearest-integer decoder. The rational source law, if supplied, permits exact extrapolation; this threshold imposes no information-theoretic limit on all algorithms.

Indeed the signed error, up to an overall sign, is 16⁻ᴺ times the alternating sum of binomial coefficients at l,l−2,l−4,… . For l≤4N its magnitude lies between 16⁻ᴺ times the first coefficient minus the second, and 16⁻ᴺ times the first. Binomial entropy bounds give exponentially small error uniformly below (λ−ε)N and exponentially large error for l/N in compact subsets of (λ,4). For |l−λN|≤C log N the ratios are uniformly bounded by a geometric progression, and Stirling's formula gives the stated first-crossing estimate. Uniform monotonicity of the binomial upper bound excludes earlier crossings; using a large fixed multiple of log N makes the interval between bulk and transition estimates explicit. The precise constant and the polynomial correction to the first crossing follow in the adjacent referee calculation.

For any recovered prefix a(1),…,a(L), use c(1)=0 and recursively solve (c*a)(n)=a(n)log n, where * is divisor convolution and a(1)=1. The resulting c(p^k)=χ₋₄(p)^k log p and all other c(n)=0 follow from multiplicativity and log n=Σ_{d|n}Λ(d). No prime oracle is necessary for the recursive direction; the supplied implementation exponentiates this equation into exact positive rational numbers. The factor p^(−k/2), the overall minus sign and the reflected logarithmic test positions enter when applying these values to the completed signed distribution. Together with the independently derived conductor and Gamma term this computes the distribution exactly on tests supported in [−log L,log L].

Without integer rounding the finite Dirichlet logarithmic derivative has a different threshold. REFEREE.md proves a two-sided total-variation asymptotic with leading constant on its moving window. MARKED_TRANSPORT.md constructs a finite reverse map and measures its sensitivity. The empirical Haar defect requires the chronologically selected points; the norm estimate here is on logarithmic arithmetic test coordinates.

## Identification with classical Euler transformation

Take the forward difference Δf(j)=f(j+1)−f(j), z=i and v=z/(1−z). The real coefficient functional
$$
 f\longmapsto\sum_{k=0}^{8N-1}\Re\left(\frac{v^k}{1-i}\right)\Delta^k f(0)
$$
has polynomial Q_N. Indeed on f(j)=x^j with x real, its complex geometric sum equals (1−[v(x−1)]^(8N))/(1−ix); v^8=1/16. Taking the real part proves polynomial identity, hence identity of the coefficient functional on complex sequences by linearity. Applying it to (j+1)^(−s) is exactly the finite Dirichlet polynomial of the Mellin note. For negative integral s, the classical annihilation of polynomials by high forward differences explains the exact interpolation through 8N−1, including the sharp first failure. The existence of such termination is a classical Euler-transform specialization. The normalization by native chronological blocks, the quantitative arithmetic-tape error and the transport to the marked source are separate claims. [Guillera–Sondow, Lerch series continuation](https://arxiv.org/abs/math/0506319).

**Finite checks.** A Horner reversal of the projected original tap sequence and an integer binomial-error recurrence agree coefficientwise on all preregistered degrees. N=29,53,101,197 give first strict decoding failures at 27,48,91,175 respectively. A second implementation uses long division from the opposite end of the polynomial on different block counts. Generating-term sign, orientation, prime-power weights and actual failure beyond the window are all tested. See REFLECTION_RECEIPT.json and REFEREE_RECEIPT.json.
