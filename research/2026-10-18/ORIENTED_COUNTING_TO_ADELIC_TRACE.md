# Operation MINUS BEFORE COUNTING: exact Möbius, projective, Tate and Connes transport

**18 October 2026.** Parent: research/connes-oriented-local-trace-2026-10-18 @ 64aa0810d9016c9c6948034d0543424f46db011e (draft PR #169). Continuation: research/oriented-mobius-adelic-descent-2026-10-18. These results combine classical mathematics with new-to-SUCC formal interfaces. No new mathematical priority claimed. **RH PROVED: NO.**

**Goal.** Determine whether a choice of negative orientation can turn positive counting into the arithmetic Möbius inverse, and whether the resulting projective prime state admits a source-faithful mapping into genuine Tate/Connes local traces and ultimately the original signed completed Weil distribution. Every proposed identification must preserve true p^k, normalized Haar, test domain, Archimedean Gamma/pole/contact and χ conductor, without reading zeros.

## OM-01: Negative counting precedes the signed number line (PROVED CLASSICAL)

Start from finite sets, isomorphisms, disjoint union, empty object, singleton, and Cartesian product. They exist before a signed numerical chart. The universal additive group completion K0(FinSet,disjoint union) represents a formal difference [A]-[B]. In finite cardinal charts use pairs (a,b), with equivalence (a,b)~(c,d) iff a+d=b+c. Addition is componentwise; negation exchanges components; the induced multiplication is (a,b)*(c,d)=(ac+bd,ad+bc). Only afterward identify (a,b) with integer a-b.

Thus choosing the negative orientation first is an additive group automorphism. **But it is NOT a unital multiplication-preserving ring automorphism:** reversal sends the distinguished unit 1 to -1, while (-1)*(-1)=+1 is not -(1*1). This already distinguishes additive counting conventions from the fully specified arithmetic source.

## OM-02: Möbius inversion is exactly parity-conjugated counting on the Boolean skeleton (PROVED)

Let P be any finite set of actual primes. On B_P={0,1}^P define Z(a,b)=1 when a<=b coordinatewise, otherwise zero. This positive incidence-zeta matrix accumulates all inclusion relationships. Let J(a,a)=(-1)^{sum a_p}. The Möbius inverse M=Z^-1 satisfies

    M(a,b)=(-1)^{sum(b_p-a_p)} if a<=b, else 0.

On one Boolean coordinate,

    Z_1 = [[1,1],[0,1]], J_1=diag(1,-1),
    M_1 = [[1,-1],[0,1]] = J_1 Z_1 J_1 = Z_1^-1.

The full P-coordinate matrices are tensor products of these two-state matrices. Therefore for EVERY finite P,

    M = J Z J = Z^-1.

**This exactly realizes the hypothesis that negative-first counting can be isomorphic to positive counting via orientation**—provided the source really is squarefree Boolean incidence and every operator/test is transported. The signs are forced by the inverse-of-accumulation constraint, not selected by fitting desired RH values.



**Positivity vocabulary firewall:** Z having entries in {0,1} is *coordinatewise nonnegative incidence data*, not a Hermitian positive-semidefinite matrix. Indeed Z_1 is not symmetric. The identity M=JZJ proves equivalence of an inverse under orientation, NOT Weil's self-adjoint positivity. Orientation alone does not make a non-Hermitian incidence operator into a positive quadratic form. Any future Hilbert/Weil functor must prove the actual adjoint and pairing identities on its declared test domain.

## OM-03: Prime squares give the first decisive failure (PROVED COUNTERMODEL)

On a FULL prime-valuation chain 0,1,2 (states 1,p,p²):

    Z    = [[1,1,1],[0,1,1],[0,0,1]]
    Z^-1 = [[1,-1,0],[0,1,-1],[0,0,1]]
    JZJ  = [[1,-1,1],[0,1,-1],[0,0,1]].

The true Möbius coefficient μ(p²)=0, while the parity-conjugate zeta coefficient at the 0→2 step is +1. In operator language on the full local ladder, Z=(I-V)^-1, Z^-1=I-V, while JZJ=(I+V)^-1=I-V+V²-... . These coincide in the Boolean truncation only because V²=0 there; actual FUCC has V_p²|1>=|p²> nonzero.

So a single sign convention does NOT automatically implement complete prime-power inversion. The arithmetic Liouville phase λ(n)=(-1)^Ω(n) differs from μ(n) at every squareful n. Also JSJ for original successor S:n→n+1 has variable edge phase λ(n)λ(n+1), equal to -1 at n=1 and +1 at n=2. All SUCC and FUCC actions must be transported coherently; not just a chosen Hilbert norm.

## OM-04: The p+1 projective model is exact CONDITIONING of the full local Tate valuation law (PROVED)

For β>0 put r=p^-β. The source-justified normalized valuation law on k>=0 is

    P(k)=(1-r)r^k;  P(k>K)=r^(K+1).

Condition on the event k<=1. Then P(0|k<=1)=1/(1+r) and P(1|k<=1)=r/(1+r). At β=1 (the squared half-density scale), the conditional masses are p/(p+1), 1/(p+1): EXACTLY the existing signed projective two-sector state. This is a constructive local bridge from complete Tate shells to P^1(F_p).

This is NOT the same as a coarse-graining of positive valuation: P(k>=1)=1/p, not 1/(p+1). The conditional model **discards the k>=2 tail of mass 1/p²** before renormalizing. At β=2 the conditional boundary probability is 1/(p²+1), not 1/(p+1). A two-state representation by itself cannot intertwine the entire genuine unilateral prime shift: p² must be recovered by lifting to the full valuation tower.

For β>1, the actual unramified local Tate Mellin factor is L_p(+)=1/(1-p^-β); the coherent ε=-1 phase on k changes its LINEAR Mellin series to L_p(-)=1/(1+p^-β), although squared probabilities are unchanged. Globally on Re(s)>1, uniform minus full-tower Euler is ζ(2s)/ζ(s), squarefree Möbius product is 1/ζ(s), and original positive Euler is ζ(s). They are three DIFFERENT arithmetic functions. For primitive χ_-3 the ramified p=3 factor is 1; integer χ(3)=0 does not mean a p-adic Hecke character takes zero values on Q_3^×.

## OM-05: A full p^k radial lift of the p+1 tree, triple-normalized (PROVED LOCAL)

The Bruhat–Tits tree for PGL2(Q_p) is (p+1)-regular. With a root and no backtracking, N_0=1, N_k=(p+1)p^(k-1) for every k>=1. The p+1 first step and subsequent p forward branches prove this by induction. Using the declared first-sphere/forward ratio N_1/p=(p+1)/p,

    ((p+1)/p)/N_k = 1/p^k  for all k>=1.

Taking positive square roots yields EXACTLY p^(-k/2), including p²,p³,... rather than only the first jet. The project code also cross-checks ALL genuine prime-power labels through a declared finite horizon against the pinned original von-Mangoldt tape (including p² and p³, rejecting composite 6). It independently compares (i) this radial amplitude squared, (ii) the authentic Connes p-adic off-identity squared half-density C_p(p^k)^2, and (iii) the norm of the genuine single-p-place Tate idèle p^k, all equal to p^-k. This is not a proof of an intertwinining representation on the full trace test space, nor does geometry uniquely prescribe the chosen normalization; it is a source-checkable candidate with exactly the required magnitude.

The primitive log clock is supplied by the already-established [H,V_p]=log(p)V_p, H|n>=log(n)|n>. Together this recovers the *magnitude* log(p)/p^(k/2) of the original Weil prime-power term. Signed distribution and identity-contact remain absent.

The symmetric radial adjacency in normalized sphere basis has first-edge weight sqrt(p+1) and every later edge weight sqrt(p). Its difference from sqrt(p)(V+V*) is rank two at levels (0,1), with eigenvalues ±(sqrt(p+1)-sqrt(p)); the defect is INDEFINITE. It must not be equated by analogy to Connes' canonical identity principal value or the real Γ factor. Parity J|k>=(-1)^k|k> conjugates adjacency to its negative; it doesn't make adjacency itself PSD.

## OM-06: Genuine Connes local compact-open test, NOT a point sample (PROVED CLASSICAL)

Take rational u0 != 0,1 and a genuine p. Pick integer radius exponent r strictly larger than v_p(u0) and v_p(1-u0). The ball B=u0+p^r Z_p is a compact-open subset of Q_p^× avoiding u=1. On it, |u|p and |1-u|p are constant. Normalize additive Haar vol(Z_p)=1 and multiplicative Haar d^×u=du/((1-1/p)|u|p).

The actual off-identity Connes local geometric distribution has factor |1-u|p^-1. Its pairing with the genuine test indicator 1_B is exactly

    integral_B |1-u|p^-1 d^×u
      = p^-r / ((1-1/p)*|u0|p*|1-u0|p).

This is an equality on the ENTIRE compact-open ball, not an empirical finite sampling claim. Finite linear combinations with rational coefficients preserve the identity. Independent enumeration of finite unit residues recovers Haar volumes for rational unit-center balls.

Inversion u→u^-1 maps B onto u0^-1+p^(r-2v_p(u0))Z_p, preserves normalized multiplicative Haar and the symmetric scalar C_p(u)=|u|p^1/2/|1-u|p. Thus the exact square of the half-density pairing is inversion invariant. The unsymmetrized |1-u|p^-1 scalar need not be. This constructs a STRICTLY LOCAL, AWAY-FROM-IDENTITY trace-test interface. Principal-value/contact at u=1, global operator trace class, full Fourier normalization and Weil sign remain UNVERIFIED.

## OM-07: Uniform negative-first prime parity fails true global idèle-class descent (PROVED NO-GO)

The finite local valuation parity product χ_f(x_f)=product_p (-1)^vp(x_p) is a continuous character of the restricted finite idèle group. It is well defined since almost all idèlic coordinates are p-adic units. On any diagonal positive rational q it equals λ(q)=(-1)^Ω(q).

To descend to an idèle-class character using only a continuous unitary positive-real Archimedean character χ_inf(x)=x^(it), the product must equal 1 on all diagonal positive rationals. For q=2 and q=3 it requires 2^(it)=3^(it)=-1. Hence t log2=(2a+1)pi and t log3=(2b+1)pi for integers a,b, so log2/log3 is rational, contradicting unique prime factorization. Thus **the uniform unramified -1 at every prime is not canceled by one continuous Archimedean unitary norm phase**.

This statement DOES NOT preclude global Hecke characters with nontrivial ramified unit characters and conductors. Valid all-place norm characters have χ_v(x)=|x|_v^(it), whose product on diagonal q is 1 by the rational product formula. Their local prime phases are p^(-it), which are NOT a universal -1. The code verifies exact prime-log coefficient cancellation with no floating logarithm approximation.



## OM-09: EXACT negative counting cancels every finite-place Euler factor and leaves the real Gamma (PROVED CLASSICAL, convergent domain only)

This supplies a more faithful realization of the user's cancellation hypothesis than the free phase sign or an auxiliary positive covariance. Define the ordinary divisor-summation operator Z(n)=sum_{d|n}f(d) and its arithmetic Möbius inverse M by Dirichlet convolution. Unique factorization proves for all n>=1,

    sum_{d|n} mu(d) = product_{p|n}(1-1) = 1 if n=1, else 0.

No spectral data enter. For Re(s)>1, all Dirichlet series and Euler products below are absolutely convergent:

    zeta(s) * (sum_n mu(n)n^-s) = 1
    zeta(s) * product_p (1-p^-s) = 1.

On the actual Tate source, the completed meromorphic factor before xi-polynomial removal is Lambda(s)=Gamma_R(s)zeta(s), with Gamma_R(s)=pi^(-s/2)Gamma(s/2). Multiplication by the genuine full Möbius Dirichlet series yields

    Lambda(s) * (sum mu(n)n^-s) = Gamma_R(s)

on the convergent half-plane. This is a mathematically exact **finite-place cancellation leaving the Archimedean contribution**, not a claim that Gamma is itself a globally positive spectral quadratic form.

For ANY finite set P of original genuine prime places and beta even integer >=2, the exact rational identity

    product_{p in P}(1-p^-beta)^-1
    * product_{p in P}(1-p^-beta) = 1

is independently reconstructed from the original Tate shell implementation. The real factor Gamma_R(2m)=(m-1)!pi^-m is retained symbolically (integer coefficient, integer power), and original Tate zero-mode residues (-1,+1) are checked instead of forged. This is not a numerical approximation to Gamma.

Mutations fail: substituting projective p+1 norm factor (1+p^-beta) does NOT cancel a true Euler factor, and substituting uniform full-tower (-1)^k phases gives 1/(1+p^-beta), also not an inverse. Omitting even one original prime from the positive side while retaining its Möbius inverse leaves a real residual factor (1-p^-beta) rather than pure Gamma. A fake prime 6 is forbidden as an Euler place.

**Why this is not RH:** The Dirichlet series for 1/zeta(s) is absolutely convergent only for Re(s)>1. Its meromorphic continuation has poles at the zeros of zeta; a single formal incidence inverse is not automatically a bounded self-adjoint source operator on critical-line test functions. Multiplication by 1/zeta across unknown zero locations can be an illicit unbounded inversion. Furthermore the completed signed Weil distribution has Gamma, poles/contact and prime spectral couplings on a declared test space; the scalar identity Lambda(s)/zeta(s)=Gamma_R(s) is not a trace equality or an all-test positive factorization. It is a necessary arithmetic source cancellation datum, not a proof of Weil positivity.

Reproduce via observational_succ/mobius_tate_gamma_remainder.py and tests/test_mobius_tate_gamma_remainder.py (independent n<=250 divisor inverse, all genuine p-places in finite stages, gamma and omitted-prime source controls).



## OM-10: The correct repair of the p² sign paradox is a Koszul exterior resolution (PROVED CLASSICAL)

The full integer multiplicative carrier is not an exclusively Boolean lattice. For a finite authentic prime set P let R=Q[x_p:p in P] be the polynomial algebra, containing EVERY monomial x^alpha and all p^k. Adjoin the exterior module E with anti-commuting generators theta_p and theta_p∧theta_p=0. The Koszul chain groups K_j=R tensor Lambda^j(E) carry the graded differential

    d(f theta_{p1}∧...∧theta_{pj})
      = sum_{a=1}^j (-1)^(a-1)
           (x_{pa} f) theta_{p1}∧... omit theta_{pa} ...∧theta_{pj}.

The commuting x_p and anti-commuting theta_p imply d²=0 for every finite P. Fix a valuation multidegree alpha in the polynomial grading, meaning the polynomial part of a wedge basis vector for subset S is x^(alpha -1_S). Exactly those S⊆supp(alpha) occur. On this fixed-alpha fiber the differential is simply alternating exterior deletion with coefficient ±1. If alpha≠0, choose its least active prime p0 and let h be wedge multiplication by theta_p0. Exterior anticommutation gives the explicit contraction

    d h + h d = I.

So the complex is **acyclic in every nonzero prime-power multidegree**; only alpha=0 retains H0=Q. It follows that its alternating count is

    chi(alpha) = sum_{S⊆supp(alpha)} (-1)^|S|
               = 1 if alpha=0, else 0.

This is the exact full integer arithmetic identity sum_{d|n} μ(d)=δ_{n,1}. At n=p² the two chain states x_p² (degree 0) and x_p theta_p (degree 1) are mapped bijectively by d: this gives 1−1=0 WITHOUT deleting the actual p² state, repairing the earlier false J Z J coefficient. The squarefree nilpotent exterior variables are auxiliary CANCELLATION generators; polynomial prime exponents remain completely unbounded. This is the precise categorical mechanism suggested by “negative counting before the number line.”

The full polynomial (“bosonic”) Hilbert series is prod_p(1-z_p)^-1. The signed exterior super-Euler series is prod_p(1-z_p). Their product is identically one. At z_p=p^-s, Re(s)>1, this is the genuine all-powers ζ(s)/ζ(s) cancellation; it is NOT uniform minus phase ∏(1+p^-s)^-1. Reversing the entire exterior chain orientation by J=(-1)^homological degree conjugates d to -d and leaves homology unchanged. With original multiplicative unit, fixed Weil tests and idelic source this does NOT grant arbitrary sign/gamma choices. The exterior model is classical Koszul resolution, not new academic priority.

The source code proves d²=0, dh+hd=I, exact integer Euler cancellation for all finite prime dimensions/multidegrees, and source conditions. An INDEPENDENT rational Gaussian elimination oracle recovers each boundary rank: for m active primes, rank(d_j)=binomial(m-1,j-1), j>=1. Removing the required wedge sign at degree two yields d²=2 rather than zero, a hostile calibration. Genuine p^k, p²q, p²q³ and composites are retained; fake local prime 6 is rejected.

## OM-11: Koszul-Hodge positivity and the ORIGINAL arithmetic log generator (PROVED AUXILIARY)

Equip each fixed multidegree exterior fiber with the standard positive Hilbert inner product, making the ordered wedge basis orthonormal. Write iota_p for contraction and epsilon_p for exterior creation. The Clifford relation is

    iota_p epsilon_q + epsilon_q iota_p = delta_pq I.

Thus if d=sum_{p|n} iota_p and d*=sum_{p|n} epsilon_p,

    Δ = d d* + d* d = omega(n) I,

where omega(n) is the number of DISTINCT prime divisors. This is an EXACT positive-semidefinite Hodge Laplacian, strictly positive on each fiber except n=1. The same exterior signs that created negative chain counts now cause the off-diagonal terms to cancel, giving a positive operator.

There is also a source-weighted, **fiberwise** factorization: set

    Q_n = sum_{p|n} sqrt(v_p(n) log(p)) iota_p,
    Q_n* = sum_{p|n} sqrt(v_p(n) log(p)) epsilon_p.

The same Clifford identity proves

    {Q_n,Q_n*} = (sum_p v_p(n) log(p)) I = log(n) I.

Therefore the known SUCC logarithmic arithmetic generator H|n>=log(n)|n> has a rigorous graded source-positive factorization in an enlarged exterior Hilbert carrier. The relative signs are load-bearing: they force the off-diagonal cross terms to vanish. This is NOT the original polynomial-R-linear Koszul differential (weights depend on each n), and it is not the signed Weil quadratic form or RH. It is an exact construction of a distinct positive source operator, with the missing Weil identification clearly visible.

There is an honest infinite arithmetic Hilbert-carrier completion of this AUXILIARY construction. Let E_n be the finite-dimensional exterior fiber with basis indexed by subsets of the DISTINCT primes dividing n, and let H_aux=direct_sum_{n>=1} E_n. Put Q=direct_sum Q_n initially on the dense finite-integer-support core. The direct sum of finite-dimensional Q_n operators is a closable densely defined operator; the closure's adjoint is the direct sum of Q_n* with its natural domain. On the common finite-support core one has Q²=0 and {Q,Q*}=H, where H acts diagonally by log n. The positive quadratic form extends to D(H^(1/2)) and satisfies

    ||Q psi||² + ||Q* psi||² = sum_n log(n) ||psi_n||² >= 0.

The standard diagonal multiplication operator H is positive self-adjoint on its maximal domain, so the core identity determines an actual closed positive quadratic form; it does NOT produce the completed Weil form. This is a scoped all-integer Hilbert realization, not a mathematical global adelic/archimedean trace or RH proof.

Independent exact rational Clifford/matrix controls verify {iota_p,epsilon_q}=delta_pq and a fully weighted example with weights 2,3,5 producing Laplacian (2²+3²+5²)I=38I. The log weights are handled symbolically, no fabricated floating interval certification. The source integer n can be recovered from unique factorization for every tested multidegree.

## OM-08: The remaining authenticated RH-hard square (UNVERIFIED)

Prior SUCC research/2026-10-15/ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md constructs the original signed completed finite-Gamma Weil W_J on all C_c² tests with genuine prime powers, real Gamma, pole/contact and source-domain controls. We have NOT derived a Connes global trace distribution equaling that same W_J, including the canonical identity singularity and its analytic limit, from the positive projective/radial source; still less have we proved universal positivity.

Precisely missing: (1) PGL2 spherical/radial to GL1 idelic scaling intertwiner on the *complete* local Schwartz/Hecke test space, including the finite rank boundary defect; (2) global Fourier- and Haar-normalized principal-value trace including u=1, all finite places and the REAL Archimedean Γ and poles; (3) exact distribution equality with original W on the full source test space, not only matching p^k magnitudes; (4) an independently constructed positive factorization of that identical signed source functional, not the auxiliary Gram. The fourth is the RH-hard condition.

**Verdict-changing controls:** p² orientation inverse failure; n=6 fake place; original successor parity nonconstant edges; χ_-3 ramified p=3 with correct odd Gamma; all-prime local negative phase vs standard ζ; pairwise inverse compact-open trace with actual normalized Haar; approach u=1 with canonical principal-value normalization; compare the full completed Weil and Connes traces on common tests with quantified tails and proper sign.

## Source provenance and tests

Imported classical mathematics: incidence Möbius inversion, Grothendieck K0, p-adic Haar, Tate local Mellin, PGL2 Bruhat–Tits spheres, real continuous characters, rational product formula, unique factorization. Primary mathematical references: Alain Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, Selecta Math. 5 (1999), arXiv:math/9811068; Connes–Consani, Weil positivity and Trace formula, the archimedean place, arXiv:2006.13771 (updated 2026), with the restricted Sonin compression; J. Raimbault, Arbre du groupe PGL2 et opérateurs de Hecke (2016); Tate's thesis (1950/1967 reprint) with normalized real Gaussian and finite 1_Zp.

Implementation (standard-library exact arithmetic, no zeros): observational_succ/oriented_mobius_adelic.py; radial_projective_trace_bridge.py; full_prime_tower_transport.py; connes_compact_open_test_bridge.py; mobius_tate_gamma_remainder.py; koszul_prime_cancellation.py. Six matched independent test suites, a source claim supplement, and dedicated CI for Python 3.10 and 3.13. Execution receipts are restricted to actual GitHub CI results at exact commit SHA, not inferred from finite proof examples.

**No RH proof, no new global trace formula, no new academic priority.**
