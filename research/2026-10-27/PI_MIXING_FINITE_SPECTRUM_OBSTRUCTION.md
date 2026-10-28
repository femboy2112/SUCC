# Primary-source audit and a mixing finite-band counterfeit

## Primary-source audit

Primary sources opened directly on 2026-10-27:

1. David H. Bailey and Richard E. Crandall, *On the Random Character of Fundamental Constant Expansions*, author preprint dated 3 October 2000, published Experimental Mathematics 10 (2001), 175–190. https://www.davidhbailey.com/dhbpapers/bcrandom.pdf ; DOI https://doi.org/10.1080/10586458.2001.10504441 .
2. Jeffrey C. Lagarias, *On the Normality of Arithmetical Constants*, arXiv math/0101055v2 (25 August 2002 upload, manuscript headed February 16, 2001 version). https://arxiv.org/pdf/math/0101055 ; DOI https://doi.org/10.1080/10586458.2001.10504456 .

Exact scope (paraphrases, not quotations): BC Hypothesis A applies to proper rational forcing, no positive-integer poles, integer base, and zero initial state. Its finite-attractor/uniform alternative is conjectural. Their displayed pi recurrence is precisely the original canceled four-pole source in this repository. Lagarias Theorem 3.1 proves orbit-shadowing for arbitrary real epsilon_n tending to zero; every real admits such an expansion, so shadowing cannot supply normality. Theorem 3.3 identifies finitely many trajectory limit points with rationality. Section 4 separates the weak dense-orbit dichotomy from the strong uniform-orbit dichotomy. Theorem 5.2 characterizes the rational-forcing G-series by a denominator split into rational linear factors; Theorem 5.3 gives rational-or-transcendental special values for distinct rational linear poles. Those statements are not Fourier cancellation estimates.

The single authentic-source instance of Hypothesis A is equivalent to the normality target, since pi is irrational. This is already explicitly recorded in `research/2026-10-24/PI_HYPOTHESIS_A_SYNTHESIS.md`; it is not a new reduction. Likewise the rational-coboundary pole-orbit obstruction is already proved in `research/2026-10-23/CYC03_BBP_FOUR_POLE_LANE.md`. More surprisingly, `research/2026-10-24/PI_SOURCE_GENESIS_NONCOBOUNDARY.md` already gives positive rational non-coboundary sources with rational selected carriers. Do not rediscover either as this round's advance.

## New scoped obstruction: even mixing, full support, and finite irrationality type do not repair a finite Fourier band

**Status: PROVED on paper; principal proof audit completed.** This is a changed-carrier dynamical counterfeit, not an authentic-source counterexample, and no external priority is asserted.

For every H >= 1 choose an odd integer q > H. Define

- p_0 = 1/8 = 15/120;
- p_d = 7/120 for d = 1,...,15;
- independent identically distributed digits D_i with this distribution;
- X = sum_{i>=1} D_i 16^{-i};
- J uniform on {0,...,q-1}, independent of all digits;
- Y = (J+X)/q, and mu_q = law(Y).

Then mu_q is an invariant, strongly mixing probability measure for T(y) = {16y}. It has full topological support, is nonatomic and singular with respect to Lebesgue measure. Its Fourier coefficients satisfy

    mu_q_hat(h) = 0                      if q does not divide h,
    mu_q_hat(q ell) = nu_hat(ell)         otherwise,

where nu is the biased Bernoulli radix law of X. In particular,

    Re mu_q_hat(q) >= (1/15)(1-7*pi/120) > 49/900 > 0.

There are therefore irrational, digit-dense, nonnormal radix-16 carriers alpha for which every fixed nonzero mode |h| <= H tends to zero, while mode q has limiting modulus greater than 49/900. Moreover their limiting law is strongly mixing rather than the nonergodic finite grid in SB-4. Requiring mixing or full support of the limiting law cannot justify a finite-mode bootstrap.

### Fourier calculation and non-Haar bound

For every integer h,

    E exp(2 pi i h Y)
      = (1/q) sum_{j=0}^{q-1} exp(2 pi i h j/q)
        * E exp(2 pi i (h/q) X).

The finite root sum is zero unless q divides h; if h=q ell it is one. Independence of the radix digits gives the convergent product

    nu_hat(1) = product_{k>=1} f_k,
    f_k = sum_{d=0}^{15} p_d exp(2 pi i d/16^k).

The k=1 root sum is f_1=p_0-p_1=1/15. Also E D_1=120*(7/120)=7. For k>=2,

    |f_k-1| <= 14*pi*16^{-k},
    sum_{k>=2}|f_k-1| <= 7*pi/120.

Since |f_k|<=1, telescoping finite products and then taking their limit gives

    |product_{k>=2}f_k-1| <= 7*pi/120.

Hence Re nu_hat(1) >= (1/15)(1-7*pi/120) > 49/900, using pi<22/7. This exact lower bound is independent of q. No numerical approximation is used.

### Invariance, factor map, and genuine mixing

Use the probability space Omega = Z/qZ x {0,...,15}^N with uniform state and iid digit law. Let

    S(j,d_1 d_2 ...) = (16j+d_1 mod q, d_2 d_3 ...),
    F(j,d) = (j + sum_i d_i 16^{-i})/q.

Then F(S(j,d)) = T(F(j,d)). Indeed write 16j+d_1=q a+j', and expand 16F=a+(j'+X')/q. The exceptional value X'=1 has probability zero. Since 16 is invertible modulo q, uniform j remains uniform after j ->16j+d_1 for every digit d_1. The new state is independent of the unused iid tail. Thus S preserves the stated product measure and F pushes it to a T-invariant mu_q.

For state mixing define the q by q stochastic matrix

    P(j,j') = sum_{0<=d<16: 16j+d = j' mod q} p_d.

It is doubly stochastic. Choose m = ceil(log_16 q), so 16^m >= q. After m updates,

    J_m = 16^m J_0 + W mod q,

where W ranges over all m-digit base-16 integers 0,...,16^m-1. Given any j,j', choose W to be the representative in 0,...,q-1 of j'-16^m j. Its m-digit word has probability at least (7/120)^m. Hence

    P^m(j,j') >= (7/120)^m for every j,j'.

Put eta=q*(7/120)^m, which lies in (0,1), since q<=16^m and 16*(7/120)=14/15<1. Then

    P^m = eta U + (1-eta)Q,

where U has all entries 1/q and Q is stochastic and preserves uniform distribution. Consequently, in total variation,

    ||lambda P^n - uniform||_TV
       <= (1-eta)^{floor(n/m)}

for every state law lambda. This is a precise finite-state Doeblin bound, however weak numerically.

A cylinder event A depending on J_0,D_1,...,D_a leaves, after time a, a possibly biased state law J_a, but the later digits remain iid and independent. For a cylinder B depending on the state and b next digits and n >= a, the above bound gives

    |P(A intersect S^{-n}B) - P(A)P(B)|
       <= P(A)*(1-eta)^{floor((n-a)/m)}.

Finite cylinders generate the sigma algebra. Approximate arbitrary measurable A and B in measure by cylinders; the inequality and measure preservation imply strong mixing for all measurable events. The factor T on Y therefore inherits strong mixing. No independence of deterministic radix lag coordinates is asserted.

The map F is one-to-one outside the zero-measure set of radix endpoint ambiguities: J=floor(qY), X={qY}, and the nonterminating/non-15-terminating digit expansion of X recovers the sequence. The map is thus also a measure-theoretic isomorphism up to null sets, although only factorhood is needed for mixing.

### Full support, singularity, and actual irrational counterexamples

All p_d are positive, so every finite radix cylinder for X has positive probability. Therefore nu and mu_q have full support. Since max p_d < 1, the probability of any fixed infinite digit string is at most (max p_d)^k for all k and hence zero; both measures are nonatomic.

With nu-probability one, the frequency of digit zero is p_0=1/8. Lebesgue-almost every X has zero frequency 1/16. Thus nu is supported on a Lebesgue-null set, and mu_q is supported on the finite union of its translates and scales (E+j)/q, also null. This establishes singularity without invoking entropy.

Mixing implies ergodicity. Applying the pointwise ergodic theorem to the countable family of Fourier characters and rational intervals yields a common full-mu_q-measure set of generic alpha. Countably many rationals have mu_q-measure zero. For these irrational alpha,

    lim_N N^{-1} sum_{n=0}^{N-1} exp(2 pi i h 16^n alpha)
       = mu_q_hat(h) for every integer h.

Full support makes every rational open interval have positive limiting visit frequency and hence makes the orbit dense. The q-th coefficient bound proves nonnormality. These are genuine infinite counterexamples to finite-band-plus-mixing logic, not finite samples. The probability model constructs their existence; it is not claimed as a law for pi.

### Finite irrationality type survives: an elementary Frostman/Borel--Cantelli bound

The maximal digit probability is 1/8. Every level-k radix interval has nu-mass at most 8^{-k}=(16^{-k})^{3/4}. If an interval I has length r with 16^{-(k+1)}<r<=16^{-k}, it meets at most two level-k intervals, ignoring endpoints of zero mass. Thus

    nu(I) <= 2*8^{-k} <= 16*r^{3/4}.

The finite lift implies

    mu_q(I) <= 16*q^{3/4}*|I|^{3/4}.

For any tau>8/3 the sum of the mu_q-masses of all approximation intervals |x-p/Q|<Q^{-tau}, Q>=1 and p relevant to [0,1], is bounded by a constant times

    sum_Q Q^{1-(3/4)tau} < infinity.

Borel--Cantelli, followed by a countable intersection over rational tau>8/3, shows that mu_q-almost every alpha has irrationality exponent at most 8/3. Since mu_q is nonatomic, these alpha are irrational almost surely; Dirichlet gives the usual lower bound 2. This is an elementary finite-irrationality theorem, not an imported claim that every biased Bernoulli point has exponent two.

Intersect this full-measure set with the generic set above. The resulting alpha are irrational, digit-dense, generic for a full-support strongly mixing non-Haar law, kill every first H Fourier modes, retain mode q, and satisfy mu(alpha)<=8/3<15/2. Thus finite irrationality type strong enough for #319 also fails to repair the finite-mode bootstrap.

### Retaining the exact four-pole forcing at a changed fixed selector

For any alpha in the common full-measure set just constructed, put

    V_n = 16^{n-1} alpha - T_n, n>=0.

Then V_{n+1}=16 V_n+r(n+1) with the exact original four poles, and V_0=(alpha-pi)/16 differs from zero because alpha lies in [0,1]. By the summable Green tail,

    N^{-1} sum_{n=1}^N e(hV_n) -> mu_q_hat(h)

for every fixed h. The completed carrier alpha has irrationality exponent at most 8/3, so the fixed-h irrationality/template reasoning of #319 is compatible with this counterexample after its carrier-dependent onset. Do not claim a uniform onset in h from #319.

These V states are generally irrational and are not the authentic rational U history or its 2-adic clock. The conclusion sharply isolates the zero selector and rational history as the information that a successful source-specific proof must actually use. This does not refute a theorem that uses that information.

### Proper lag targets

For fixed nonnegative lags ell_j and integer frequencies h_j, write K=sum_j h_j 16^{ell_j}. The deterministic lag graph has exact character target

    integral e(sum_j h_j T^{ell_j}(y)) d mu_q(y) = mu_q_hat(K).

This is not product Haar. Haar itself would give one when K=0 and zero otherwise. The annihilator E-16 has K=0 and target one under both measures. Strong mixing concerns separated events or centered observables: for a fixed h, the long-lag uncentered Fourier correlation tends to |mu_q_hat(h)|^2. It therefore remains positive at h=q even though the centered correlation decays. No independent-coordinate interpretation is used.

## Boundary

This construction changes the carrier; its Green-shifted V sequence obeys the original four-pole forcing with a fixed nonzero selector, not U_0=0. It does not refute Hypothesis A. It refutes a proposed inference even after adding dense orbit, ergodicity, full support, strong mixing, or finite irrationality type to finite-mode cancellation. The authentic-source theorem must exclude these measures via a genuinely source-specific signed estimate; no such estimate is supplied here. The explicit distribution and common full-measure set prove simultaneous existence, not a certification of any individual finite sample. This is not a probability law for pi.
