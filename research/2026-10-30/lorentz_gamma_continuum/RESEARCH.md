# SUCC Lorentz–Gamma continuum: exact null-cone gluing and an asymmetric rapidity spectrum

**Research-only paper proofs with independently scoped finite checks.** Mathematical statements are about the declared source/Pascal process; the π digit orbit is deterministic, not sampled by its auxiliary Bernoulli sensor. Parent #391 exact head `7ce94d38479c22c3d427753812e38207515dc868`. Preserve the author's harmonic–golden–Euler–Mascheroni triangle and Oily–Macaroni as provenance and a source/observer specialization, not as universal Lorentz laws.

## 0. Object, coordinates, what "Lorentz" means

Put `(a,b)` for the counts of zero and one outcomes. At lattice time `n=a+b`, grade `j=b`, the sideways coordinate is `t=a+b, x=b-a`, so null coordinates `t-x=2a`, `t+x=2b`, Minkowski quadratic form `t²-x²=4ab`, and causal metric `dt²-dx²=4 da db`. An elementary Pascal step increments either `a` or `b`, hence follows one of the two null directions. A continuous 1+1 boost acts by

`(a,b) -> (a exp(-eta), b exp(eta))`, preserving `ab`; its generator is `L=-a d_a+b d_b`.

No nontrivial boost preserves the entire positive integer lattice: images of both basis unit steps would require `exp(eta)` and `exp(-eta)` to be positive integers, so both equal 1. This is **Lorentzian causal kinematics**, not Lorentz-invariant probability dynamics, physics, Minkowski spacetime as a claim about reality, or a quantum theory.

## 1. Authentic source partition — four-Beta formula (LG-01)

Start at the original source `X~mu_1(dx)=exp(-x)Q(x)dx/R(1)`, with

`Q(x)=4-2 exp(-3x)-exp(-4x)-exp(-5x)`,  `R(s)=4/s-2/(s+3)-1/(s+4)-1/(s+5)`,  `R(1)=47/15`.

Set `f(X)=exp(-8X)` and `g(X)=1-f(X)`. For integer counts `a,b>=0`, a particular ordered word has probability `Z(a,b):=E[f(X)^a g(X)^b]`; its grade mass is `C(a+b,a) Z(a,b)`. The same integral gives **positive continuous counts** `a,b>=0`:

`Z(a,b)=R(1)^(-1) integral_0^infty exp(-(1+8a)x)Q(x)(1-exp(-8x))^b dx`.

Substitute `y=exp(-8x)`, so `dx=-dy/(8y)`, `exp(-x)=y^(1/8)` and `Q=4-2y^(3/8)-y^(1/2)-y^(5/8)`. Euler's Beta integral gives the exact, original-pole identity

`Z(a,b)= [4 B(a+1/8,b+1)-2 B(a+1/2,b+1)-B(a+5/8,b+1)-B(a+3/4,b+1)]/[8 R(1)]`.

It is positive and real analytic for `a,b>=0`, with a holomorphic continuation at least on `Re a>-1/8`, `Re b>-1` (all terms individually represented by convergent Beta integrals there). For `b` a nonnegative integer, expand `(1-f)^b`: `Z(a,b) = R(1)^(-1) sum_(k=0)^b (-1)^k C(b,k) R(1+8(a+k))`, exact rational for rational `a>=(0)`. In particular `Z(n-1,0)=r(n)/R(1)` is the original native zero-spine survival.

The likelihood identity `f+g=1` gives the exact continuous Pascal shift equation

`Z(a,b)=Z(a+1,b)+Z(a,b+1)` for every `a,b>=0`.

Define the Gamma binomial `C(a,b)=Gamma(a+b+1)/[Gamma(a+1)Gamma(b+1)]` and the endpoint density/mass label `W(a,b)=C(a,b)Z(a,b)`. At integer `(a,b)`, it is the authentic grade probability. The source measure-valued `C(a,b)f^a g^b mu_1` obeys the Pascal *backward* update for all real `a,b>=1`:

`M(a,b)=f M(a-1,b)+g M(a,b-1)`,

because `C(a,b)=C(a-1,b)+C(a,b-1)` and both terms have the same `f^a g^b` density after update. Do not integrate `W(a,b)` against Lebesgue `db` and call it a continuous outcome probability without explicitly choosing/normalizing a measure; it is an interpolation of discrete endpoint masses.

## 2. Why this continuum is selected, and why naive analytic interpolation is NOT (LG-02)

The *positive fractional likelihood semigroup* is pointwise unique under the explicit assumptions: for each latent `x>0`, a continuous strictly positive family `F_t(x)` satisfying `F_0=1`, `F_{s+t}=F_s F_t`, `F_1=f(x)` has `F_t=f(x)^t`. Proof: `log F_t` is continuous additive, hence equals `t log f(x)`. The success family analogously is `g(x)^t`; commuting both gives `f^a g^b`. The Gamma multiplicity is the standard positive log-convex factorial interpolation (Bohr–Mollerup) used in the binomial expression; this regularity is a **separate declared requirement**, not a consequence of mere lattice agreement.

**Explicit countermodel.** For any `0<epsilon<1`, put

`W_epsilon(a,b)=[1+epsilon sin(2 pi a) sin(2 pi b)] W(a,b)`.

This is positive and real analytic, agrees with `W` at *every integer lattice point*, agrees along both whole null axes, and preserves the unit-shift Pascal recurrence because the multiplier is 1-periodic in each coordinate. But it differs at fractional `(a,b)` and **fails the two-parameter positive semigroup law**. Thus neither lattice samples, Pascal recursion, positivity, nor the entire boundary axes alone uniquely defines a continuum. This is the required hostile control for the user's "analytic continuation" insight. Avoid claiming ordinary analytic continuation from integers is unique (integers have no finite accumulation point).

## 3. Fractional-success rank; harmonic and Euler finite part (LG-03)

Fix `b>=0`, set `L=1+8a`, and take `a->infinity`. Near `x=0`, the authentic source has

`Q(x)=15x-(59/2)x²+O(x³)`,  `g(x)=8x-32x²+O(x³)`.

Therefore

`Q(x)g(x)^b=15*8^b x^(b+1)[1-(59/30+4b)x+O_b(x²)]`.

Apply the Laplace substitution `y=Lx`, dominated on compact `b` intervals by the exponentially decaying positive kernel. This yields the exact two-term boundary asymptotic:

`Z(a,b)=[15*8^b Gamma(b+2)/(R(1) L^(b+2))] [1 - (b+2)(59/30+4b)/L+O_b(L^-2)]`.

With the posterior `nu_(a,b)(dx)=f^a g^b mu_1(dx)/Z(a,b)`, the scaled random variable `Y=L X` converges in distribution to `Gamma(b+2, rate=1)`; the Laplace transforms converge to `(1+s)^(-b-2)` for each `s>=0`. For integer `b`, this is a **source-specific rank shift by the actual success count**; for noninteger `b` it is the fractional posterior continuation. The limiting rank 2 at `b=0` is the original four-pole zero spine.

Differentiate the Laplace asymptotic in `b` (justified by local uniformity in `b` and integrable logarithmic factors). Since `d_b log Gamma(b+2)=psi(b+2)`, the exact renormalized directional response is

`lim_(a->infinity) [d_b log Z(a,b)+log(1+8a)-log 8]=psi(b+2)`.

At integer `b=m>=0`, `psi(m+2)=H_(m+1)-gamma`, so Euler–Mascheroni is the finite-part of the continuous rank/likelihood response, not a third independent primitive. Source-specific coefficient 59 survives at the next boundary order and would be missed by a `Q_fake=15x` Gamma-matched source. The `b` derivative at zero is right-sided as a physical fractional count but obtained from the analytic extension through b=0.

## 4. Golden locus is a marked cross-section, not a boost law (LG-04)

Launch a separate `k(a)`-trial observation fan from `nu_(a,b)`, with `8k(a)/L -> theta>0`. The limit is the Gamma–Poisson PGF `G_(r,theta)(z)=[1+theta(1-z)]^-r` for `r=b+2`; the limit is pointwise in real b (not a claim of a fixed real number of actual fractional trials). Mark the **declared branching/extinction** fixed point `q=G(q)`. With `lambda=phi^-1`, previous Main XVI TG-11 proves the exact golden locus

`q=lambda^r  <=>  theta=theta_star(r):=lambda/(1-lambda^r)`.

Along this *observer-tuned* curve the Laplace rate is constant `theta(1-q)=lambda`, and the rank contrast is `psi(b+2)-lambda^(b+2)`. For b=0 and native clock theta=1, `psi(2)-lambda²=(1-gamma)-(1-lambda)=lambda-gamma=Omega_OM`.

Thus the original harmonic / golden / Euler triangle occupies a genuine marked boundary/cross-section of the Beta–Gamma continuum. **The golden condition is not forced by boost invariance**; it selects a family of observer clocks. Altered b at the native clock theta=1 do not automatically retain golden coincidence. The historical name and provenance are preserved.

## 5. Lorentz boosts, the two original null exponents, and an analytic Fourier strip (LG-05)

For each `rho>0` define the hyperbola `a=rho e^-eta`, `b=rho e^eta` and the source-weighted Gamma-Pascal endpoint interpolation

`W_rho(eta)=W(rho e^-eta, rho e^eta)`.

The causal Minkowski quadratic `t²-x²=4rho²` is exactly invariant under `eta` translations. But the source **weight is not Lorentz invariant**. It has the following *two unequal null tails*:

`W_rho(eta) ~ [225/(3008 rho²)] exp(2eta)`,  as `eta->-infinity`;

`W_rho(eta) ~ [Gamma(1/8)/(2 R(1) rho^(1/8))] exp(-eta/8)`, as `eta->+infinity`.

Proof of left: `a->infinity`, `b=rho²/a->0` and `b log a->0`. Apply LG-03 with b->0; `C(a,b)->1` and `Z(a,b)~15/[R(1)(8a)^2]`. Since `15/(64 R(1))=225/3008`, obtain the left amplitude.

Proof of right: `b->infinity`, `a=rho²/b->0` and `a log b->0`. Each original Beta term obeys `B(a+c,b+1)~Gamma(a+c)b^(-a-c)` by the classical Gamma ratio formula. The smallest original exponent is c=1/8 and coefficient 4, which dominates the other c in {1/2,5/8,3/4}. Also `C(a,b)->1`. Therefore `W~4 Gamma(1/8)/(8R(1)) b^-1/8`, yielding the right amplitude.

The left exponent `2` arises from the cancellation `4-2-1-1=0` at the **small-X** boundary, leaving the rank-two zero-spine; the right exponent `1/8` arises from the original large-X tail of mu_1 and the first authentic BBP offset. The remaining original offsets `1/2,5/8,3/4` appear as subleading powers in the right-null Beta expansion, making this a source-sensitive *anisotropic null spectrum*.

Define a declared rapidity Fourier/Mellin observer `F_rho(k)=integral_{-infinity}^infinity exp(-i k eta) W_rho(eta) d eta`. Because of the two proved positive tail equivalents, it converges absolutely and depends holomorphically on `k` throughout the **sharp maximal absolute-convergence strip**

`-2 < Im(k) < 1/8`.

For `k=x+i y`, `|exp(-ik eta)|=exp(y eta)`; the tails are integrable iff `y>-2` at negative infinity and `y<1/8` at positive infinity. Outside or at either edge absolute convergence fails (weights remain positive). This is a rigorous analytic strip for the *auxiliary boosted endpoint field*, not a claimed bound on Fourier transforms of selected π digits.

An exact weight transport cocycle is `A_eta(a,b)=W(e^-eta a,e^eta b)/W(a,b)` and `A_(eta+xi)(a,b)=A_eta(e^-xi a,e^xi b) A_xi(a,b)` with the appropriate ordering. It is a scalar coboundary and carries no nontrivial phase holonomy. The infinitesimal boost generator on log W is

`L log W=(b-a)psi(a+b+1)+a psi(a+1)-b psi(b+1) -a d_a log Z+b d_b log Z`.

The generator is typically nonzero: the continuous coordinate boosts are **not** symmetries of the source probability. Do not infer a Lorentz invariant field theory, light propagation, or gravitational geometry.

## 6. Information curvature is NOT the causal Lorentzian metric (LG-06)

The posterior is an exponential family in the two log-likelihood statistics `log f` and `log g`. Therefore the Hessian of the log-partition is the covariance / Fisher information matrix:

`d_i d_j log Z = Cov_{nu_(a,b)}(T_i,T_j)`, `T_1=log f=-8X`, `T_2=log g=log(1-exp(-8X))`.

It is positive definite on the original full-support positive source. In particular the mixed entry is strictly **negative**: `log f` strictly decreases with X and `log g` strictly increases, so the covariance is negative (use an independent copy X' and the exact covariance difference formula). This is a Riemannian information metric, **distinct from the Lorentzian causal metric** `dt²-dx²=4da db` used to parametrize the lattice. A mixed covariance is not a negative eigenvalue, a Lorentz signature, or a quantum/physical curvature. The exact boost-likelihood scalar cocycle remains flat as an exact-gradient transport.

## 7. No π-normality implication, next discriminating lamp (LG-07)

Everything above is the auxiliary retained-latent source geometry. The selected deterministic BBP phase still satisfies `e(hU_(n+1)(s))=e(h r(n+1))e(16h U_n(s))` and the authentic boundary is `s=0`. The same-source coherent counterseed `s*=-pi/16` shares all the positive continuum and the Lorentz/Mellin strip but has `U_n(s*)=-T_n->0`; hence **source-only continuum/Lorentz/Gamma/golden results cannot certify selected cancellation**.

A next bridge must use a source-derived, zero-seed-sensitive signed intertime relation involving selected phases *and* literal carry, with calibrated rational-translation controls and fresh fake-source/seed holdouts. Merely taking the new rapidity Fourier transform, prescribing a conformal weight, or inventing a boost-covariant phase does not count. π base-16 normality, RH, and physical Lorentz symmetry remain OPEN/UNVERIFIED.

## External classical sources and provenance

- NIST DLMF §5.12 (Euler Beta integral, Beta/Gamma identity): https://dlmf.nist.gov/5.12
- NIST DLMF §5.11(iii) (Gamma ratio asymptotic): https://dlmf.nist.gov/5.11
- NIST DLMF §5.2 and §5.5 (digamma, Gamma functional equation, Bohr–Mollerup): https://dlmf.nist.gov/5.2 ; https://dlmf.nist.gov/5.5.iv
- Original SUCC positive four-pole / zero-spine and original signed phase: parent #391 and `docs/OPERATIONAL_TRIANGLE.md` on Main XVI.

All identities above are new-to-this-program combinations of classical tools and the original source. Independent scholarly priority is unverified.
