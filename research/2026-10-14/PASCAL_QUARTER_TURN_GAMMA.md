# Pascal quarter-turn, fractional SUCC, and the completed Gamma heat bridge

**Origin:** maintainer's proposed 90-degree rotation of an infinite-to-finite Pascal-triangle SUCC, 2026-10-14 New York time. **Parent:** SUCC `research/suzuki-source-boundary-wavefront-2026-10-13` exact head `a10d994cf2c4013f43c9c6d91103d247e667739f`, stacked on zero-centered/property-graph/periodic-tail branches. **Status:** CLASSICAL algebra/probability/analysis reorganized in an explicit source-typed construction; PROVED LOCAL finite algebraic identities and source-preserving affine lift; TESTED FINITE exact rational implementation. **No new academic priority claimed, no physical carrier authenticated, no nontrivial zero used, no global Weil identification. RH PROVED: no.**

## 0. Distinguish three different rotations

1. **Combinatorial quarter-turn:** Transpose the infinite Pascal matrix `P[n,k]=C(n,k)` to read a global sequence through finite factorial moments. This is *not* an inverse, and it is a metric adjoint only for compatible chosen pairings/domains.
2. **Fractional-depth SUCC:** Reindex the triangle as a Pascal quadrant `A(r,k)=C(r+k,k)` and extend an integer depth along a row to positive real depth via a positive convolution semigroup. Gamma enters by normalization.
3. **Metaplectic/Fourier quarter-turn:** Normalize Pascal paths to a symmetric random walk, prove a diffusive Gaussian limit, apply Fourier phase-space quarter-turn and Mellin; the exact canonical Archimedean factor `pi^(-s/2) Gamma(s/2)` appears.

A literal rigid rotation of an integer array proves NONE of (2)/(3). Each transformation has a different admissible source/cost/analytic domain. In particular a normalized real-valued random walk can escape at 2-adic places while remaining a valid rational-valued finite source at every finite stage.

## PG-01. The two-axis Pascal lattice (PROVED LOCAL; classical)

For `r,k>=0`, put `A(r,k)=binom(r+k,k)`. For `r+k>0`,

`A(r,k)=A(r-1,k)+A(r,k-1)`, extending A by 0 at negative indices; A(0,0)=1.

Both axes have constant boundary values 1. The double generating series, for |x|+|y|<1, is

`sum_(r,k>=0) A(r,k) x^r y^k = 1/(1-x-y)`.

This is a well-defined graded incidence/path-counting algebra, and coassociative polynomial Hopf coproduct `Delta(t^n)=sum_k binom(n,k) t^k (tensor) t^(n-k)` provides a precise way to split a global path between two observer components. It is classical, not a completed RH object.

## PG-02. True transpose, finite factorial moments and metric debt (PROVED LOCAL; classical)

On finitely supported sequences `b` the transposed matrix is

`(P^T b)_k=sum_(n>=k) binom(n,k)b_n`.

If `B(z)=sum b_n z^n` has radius of convergence **strictly greater than 1** (not merely an analytic continuation near z=1), the power series may be differentiated term by term at `z=1`, giving

`(P^T b)_k=B^(k)(1)/k!`.

For a geometric probability source `b_n=(1-q)q^n`, `0<q<1`, we obtain

`(P^T b)_k=(q/(1-q))^k`.

In particular `q=1/2` maps a positive, summable infinite source to the constant-one output across every finite `k`. This is a legitimate infinite-to-finite **moment** readout under its convergence contract, not the execution of infinitely many measurements by one finite automaton.

**Sharp domain obstruction:** `b_n=1/(n+1)` belongs to `ell^2(N)` but `(P^T b)_0=sum_n 1/(n+1)` diverges. The bare transpose is not everywhere defined, let alone bounded, on the ambient `ell^2` carrier. If the domain carries positive diagonal weights `W`, the finite Hilbert adjoint is `P^*=W^-1 P^T W`, not `P^T`. Exact rational tests verify this and refute naive quarter-turn-as-unitary. The infinite adjoint requires its own dense domain and operator closability proof.

## PG-03. Fractional-depth Pascal–Gamma semigroup (PROVED LOCAL; classical)

Let `alpha>0` and set

`c_alpha(k)=Gamma(alpha+k)/(Gamma(alpha) Gamma(k+1))=(alpha)_k/k!`.

For positive integer `m`, this is the row `binom(k+m-1,k)` in the rotated Pascal quadrant. For `|z|<1`,

`sum_(k>=0) c_alpha(k) z^k=(1-z)^(-alpha)`.

Therefore, by multiplying generating functions and comparing coefficients,

`sum_(j=0)^k c_alpha(j)c_beta(k-j)=c_(alpha+beta)(k)`.

On weighted `ell^1_rho` with norm `sum_k rho^k|f_k|`, `0<rho<1`, the convolution operator `T_alpha f=c_alpha*f` is bounded with `||T_alpha||=(1-rho)^(-alpha)`, positive, and `T_alpha T_beta=T_(alpha+beta)`. It is a strongly continuous positive semigroup in alpha on this carrier (checked via dominated power series / uniformity on compact alpha intervals).

In particular `c_(1/2)*c_(1/2)=c_1=(1,1,1,...)` and `T_(1/2)^2=T_1`. Two half-depth summation operators compose exactly into one full summation. At rational alpha, this identity is checked in exact Fraction arithmetic for several independent pairs and degrees k<=23.

Generalized hockey-stick identity: `sum_(k=0)^m c_alpha(k)=c_(alpha+1)(m)`.

A standard mesh scaling `I_h^alpha f(t)=h^alpha sum_(k=0)^floor(t/h) c_alpha(k) f(t-kh)` converges for suitable continuous compactly supported f to the Riemann–Liouville fractional integral `1/Gamma(alpha) int_0^t (t-u)^(alpha-1) f(u)du`. For f=1, the exact hockey-stick identity plus the classical Gamma-ratio asymptotic immediately gives `t^alpha/Gamma(alpha+1)` as h->0. The general fractional-calculus limit is a CLASSICAL analysis claim here, not inferred merely from finite tests.

**Semigroup uniqueness conditional statement.** If for each `z` in (0,1) an alpha-indexed generating function `C_alpha(z)` is positive, continuous in alpha, satisfies `C_(alpha+beta)=C_alpha C_beta`, and `C_1(z)=1/(1-z)`, then `C_alpha(z)=(1-z)^(-alpha)`. This follows from the continuous Cauchy exponential functional equation. It uniquely selects the positive fractional semigroup GIVEN the declared unit summation law and generating-function setup; it does not select a physical carrier or a test state by itself.

## PG-04. Actual integer SUCC/FUCC affine lift (PROVED LOCAL; new-to-SUCC interface)

Let `S(n)=n+1`, `V_p(n)=pn`, starting at `n=0`, and `p>=2`. For words of length N containing precisely k occurrences of Vp, count each endpoint `m` in a polynomial:

`F_[N,k]^(p)(z)=sum_(words w) z^(endpoint_w(0))`.

When appending S the endpoint increments by 1; when appending Vp the endpoint multiplies by p. Hence

`F_[N+1,k]^(p)(z)=z F_[N,k]^(p)(z)+F_[N,k-1]^(p)(z^p)`.

The ordinary Pascal shadow is `F_[N,k]^(p)(1)=binom(N,k)`. For p=2, N=3, k=1, `F=z^2+z^3+z^4`, which retains the three different arithmetic endpoints. At N=5,k=2, the address 6 has coefficient 2 (distinct words sharing a source endpoint). Exact tests compare every polynomial to a completely independent enumeration of all primitive words for p=2,3,6 and N<=5.

**Authenticity gate:** composite 6 obeys the same affine recursion. It is not a new Euler prime, and a prime-place source must reject it via separate primality certification. This is not the q-binomial theorem: `Vp S=S^p Vp` is an affine braid, not scalar q-commutativity.

## PG-05. Pascal random walk -> Gaussian -> quarter turn -> completed Gamma (CLASSICAL; analytic proof)

Define the probability measure

`mu_N=2^-N sum_(k=0)^N binom(N,k) delta_((2k-N)/sqrt(2 pi N))`.

Under the angular Fourier convention `Ff(omega)=int f(x)exp(-i omega x)dx`, its characteristic function is `cos(omega/sqrt(2 pi N))^N -> exp(-omega^2/(4 pi))`. Under the cycles Fourier convention `F_2pi f(xi)=int f(x)exp(-2 pi i xi x)dx`, it is exactly

`hat(mu_N)(xi)=cos(sqrt(2pi/N)*xi)^N -> exp(-pi xi^2)`.

By Levy's continuity theorem, `mu_N` converges weakly to the probability density `g(x)=exp(-pi x^2)`. It is the time-one heat kernel `h_1(x)` for `D=1/(4pi)` in `exp(t D d²/dx²)`. Fourier is a quarter-turn in standard symplectic phase space, and `hat g=g` under the cycles convention. Finally, for Re(s)>0,

`int_R |x|^(s-1) exp(-pi x²) dx=pi^(-s/2) Gamma(s/2)`.

The last step follows from Euler's Gamma integral by `u=pi x²`. **Careful**: weak convergence of measures alone does NOT establish convergence of singular discrete Mellin moments for every Re(s)>0; if N is even there is an atom at zero, so negative powers can be undefined. For Re(s)>1, standard subgaussian uniform integrability permits positive-power moment convergence; the full displayed Gamma formula is an identity of the limiting continuous density, not an unproved termwise limit.

With independently authentic Euler data `prod_p(1-p^-s)^-1`, `Re s>1`, the standard global completion is `pi^(-s/2)Gamma(s/2) zeta(s)`. The construction does NOT derive the true Euler primes, completed pole removal, a unique physical source, the Weil sign, or RH.

**Local finite-place obstruction:** the boundary weight `2^-N` goes to zero in the Archimedean norm but has 2-adic norm `2^N -> infinity`. The rational product formula is valid for each finite N, yet real weak convergence does not yield a simultaneous restricted-adelic completion. Any global SUCC gluing must explicitly account for this normalization debt.

## PG-06. The DIRECT Suzuki bridge: OU Gamma bath as heat-time Laplace of Pascal limits (CLASSICAL exact identity; source-context new-to-project)

Let `h_u(t)=(4 pi u)^-1/2 exp(-t²/(4u))` for u>0: the whole-real-line heat kernel of time u and diffusivity one. Under angular Fourier `hat h_u(omega)=exp(-u omega²)`. For alpha>0,

`exp(-alpha |t|) = 2 alpha int_0^infty exp(-alpha² u) h_u(t) du`.

**Proof:** Take angular Fourier transforms. The right side transforms to `2 alpha int_0^infty exp(-u(alpha²+omega²))du=2alpha/(alpha²+omega²)`, exactly the Fourier transform of `exp(-alpha |t|)`. Both are L¹ and continuous, so equality holds. Alternatively apply the elementary Gaussian/Laplace subordination formula. Rational alpha and omega give an exact rational Fourier-multiplier equality, verified independently by Fraction tests.

The Suzuki paper/previous SUCC Wavefront branch has, on mean-zero `H_a=L²_0(-a,a)`, the **authentic positive Gamma bath**

`B_a=sum_(j>=0) alpha_j^-2 P_a R_(alpha_j) P_a`, `alpha_j=2j+1/2`,

where `R_alpha` is the restriction of convolution with `exp(-alpha|x-y|)` to `(-a,a)`.

Consequently one has the exact positive operator representation

`B_a=P_a [int_0^infty W(u) H_(u,a) du] P_a`,

`W(u)=2 sum_(j>=0) alpha_j^-1 exp(-alpha_j² u)>0`,

where `H_(u,a)` is the *compression/restriction of the WHOLE-LINE heat convolution* to the interval. It is NOT silently replaced by the Neumann heat semigroup on the interval; the two have different boundary behavior. The integral converges as a positive operator (indeed in norm on finite a); summing termwise is justified by positivity and `sum_j alpha_j^-3<infinity` using the whole-line heat contraction bound.

This identifies a **concrete Pascal -> diffusive heat -> resolvent OU -> Suzuki Gamma bath** chain. The representation is classical Fourier/Laplace functional calculus, newly made explicit as a source-typed SUCC handoff candidate. It supplies a new geometric origin for an already proved-positive *part* of Suzuki's operator, not positivity of the complete Weil form.

The full authentic Suzuki operator additionally carries `-C K_a`, oppositely signed rank-one pole terms, and signed prime-power translations (`SUZUKI_SOURCE_WAVEFRONT_ROUND_001.md`, SW-4). No claim about those signs is obtained by the new Pascal representation. The RH-hard task is a sign-controlled domination/Schur-complement comparison in the correct operator/test-function domain, not proving that the Gamma bath is PSD.

## PG-07. Even-step Gamma poles are a regulated infinite SUCC ladder (CLASSICAL, separate construction)

NIST DLMF §5.8 supplies the Weierstrass product

`1/Gamma(z)=z exp(gamma*z) prod_(n>=1) (1+z/n) exp(-z/n)`.

The factors `exp(-z/n)` are indispensable convergence counterterms. Put `z=s/2` to obtain poles of Gamma(s/2) at s=0,-2,-4,... . The pole sequence is an even-step ladder, consistent with a 2-unit SUCC perspective; the *existence of that ladder alone* does not force the real completed zeta factor, functional equation or RH. This construction is distinct from the fractional-summation and heat-limit routes, even though each leads to Gamma.

## Falsifiers and next work

1. **Adjoint trap:** test `P^T` against `W^-1 P^T W` on a nonuniform Hilbert carrier. Bare transpose fails.
2. **Source trap:** affine recursion accepts composite 6 but authentic prime-place construction rejects it.
3. **Regularity trap:** some `ell²` inputs give divergent sideways moment; no unconditional infinite observer.
4. **Finite/adelic trap:** normalized Pascal weight `2^-N` blows up at p=2, despite a good real Gaussian limit.
5. **Global Gamma trap:** Fourier self-duality alone does not uniquely determine the distinguished test state. The symmetric binomial heat-generator selection is an explicit additional assumption, and the real-place normalization must still be source-identified.
6. **Suzuki sign trap:** heat mixture is positive, but pole and prime-shift parts have nontrivial signs and may not be dropped. Heat compression is not the heat semigroup with an invented boundary condition.

**Next verdict-changing theorem target:** construct the actual source-typed intertwiner from the *affine* Pascal groupoid, with arithmetic prime/authentic phase, to the completed Archimedean heat-resolvent bath and signed Suzuki operators. Start with finite prime window `log2/2<a<log3/2`, verify action/metric/boundary commuting diagrams and a full-space form estimate controlling the negative translation coupling. The two limits (Pascal mesh -> 0 and Suzuki interval a -> infinity) need separate uniform bounds; do not commute them on intuition. None of PG-01..PG-07 proves RH.

## Reproduction

Run from project root:

`python -m unittest discover -s tests -p test_pascal_gamma_turn.py -v`

`python scripts/pascal_gamma_turn_probe.py --output /tmp/pascal_gamma_turn.json`

Checks are exact rationals for finite statements. Infinite CLT, Fourier/Gamma integral, Beta/Vandermonde and subordination are classical paper derivations; they are NOT formally verified in Lean by this branch. Scholarly originality not assessed.

**Sources:** NIST DLMF §5.2 Euler Gamma integral https://dlmf.nist.gov/5.2 ; NIST DLMF §5.9 Gaussian Mellin https://dlmf.nist.gov/5.9 ; NIST DLMF §5.8 Gamma product https://dlmf.nist.gov/5.8 ; generalized Vandermonde https://planetmath.org/GeneralizedBinomialCoefficients ; classical metaplectic/Fourier quarter-turn e.g. https://pmc.ncbi.nlm.nih.gov/articles/PMC9581872/ ; source-specific Suzuki arXiv:2606.09096v3 https://arxiv.org/html/2606.09096v3 ; original SUCC variable proto-unit and Mahler dossiers on main; Suzuki SW-4 on parent branch `a10d994`.
