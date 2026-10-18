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

Taking positive square roots yields EXACTLY p^(-k/2), including p²,p³,... rather than only the first jet. The project code independently compares (i) this radial amplitude squared, (ii) the authentic Connes p-adic off-identity squared half-density C_p(p^k)^2, and (iii) the norm of the genuine single-p-place Tate idèle p^k, all equal to p^-k. This is not a proof of an intertwinining representation on the full trace test space, nor does geometry uniquely prescribe the chosen normalization; it is a source-checkable candidate with exactly the required magnitude.

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

## OM-08: The remaining authenticated RH-hard square (UNVERIFIED)

Prior SUCC research/2026-10-15/ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md constructs the original signed completed finite-Gamma Weil W_J on all C_c² tests with genuine prime powers, real Gamma, pole/contact and source-domain controls. We have NOT derived a Connes global trace distribution equaling that same W_J, including the canonical identity singularity and its analytic limit, from the positive projective/radial source; still less have we proved universal positivity.

Precisely missing: (1) PGL2 spherical/radial to GL1 idelic scaling intertwiner on the *complete* local Schwartz/Hecke test space, including the finite rank boundary defect; (2) global Fourier- and Haar-normalized principal-value trace including u=1, all finite places and the REAL Archimedean Γ and poles; (3) exact distribution equality with original W on the full source test space, not only matching p^k magnitudes; (4) an independently constructed positive factorization of that identical signed source functional, not the auxiliary Gram. The fourth is the RH-hard condition.

**Verdict-changing controls:** p² orientation inverse failure; n=6 fake place; original successor parity nonconstant edges; χ_-3 ramified p=3 with correct odd Gamma; all-prime local negative phase vs standard ζ; pairwise inverse compact-open trace with actual normalized Haar; approach u=1 with canonical principal-value normalization; compare the full completed Weil and Connes traces on common tests with quantified tails and proper sign.

## Source provenance and tests

Imported classical mathematics: incidence Möbius inversion, Grothendieck K0, p-adic Haar, Tate local Mellin, PGL2 Bruhat–Tits spheres, real continuous characters, rational product formula, unique factorization. Primary mathematical references: Alain Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, Selecta Math. 5 (1999), arXiv:math/9811068; Connes–Consani, Weil positivity and Trace formula, the archimedean place, arXiv:2006.13771 (updated 2026), with the restricted Sonin compression; J. Raimbault, Arbre du groupe PGL2 et opérateurs de Hecke (2016); Tate's thesis (1950/1967 reprint) with normalized real Gaussian and finite 1_Zp.

Implementation (standard-library exact arithmetic, no zeros): observational_succ/oriented_mobius_adelic.py; radial_projective_trace_bridge.py; full_prime_tower_transport.py; connes_compact_open_test_bridge.py. Four matched independent test suites, a source claim supplement, and dedicated CI for Python 3.10 and 3.13. Execution receipts are restricted to actual GitHub CI results at exact commit SHA, not inferred from finite proof examples.

**No RH proof, no new global trace formula, no new academic priority.**
