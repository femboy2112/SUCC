# Discrete root, analytic root and higher-order return

The following classical structures give an explicit realization of the authorial cycle, not a uniqueness theorem or an assertion that all SUCC observers have these completions.

## PRF-07. Marked multiplicative carrier and exact double dual

Let N_+={1,2,...}. Complete its cancellative multiplication monoid to the discrete group G=Q_+^times. Unique factorization identifies G with the direct sum of Z over primes; the positive cone of exponent vectors is the original N_+. With finite-prime groups G_k=Z^k under zero-coordinate inclusions, G=colim G_k (not an infinitely elapsed computation). The Pontryagin dual K=Hom_cont(G,T), with compact-open topology, is the product of circles over primes, the inverse limit of finite tori under coordinate projections. The character of n is chi_n(z)=prod_p z_p^(v_p(n)), a finite monomial.

Pontryagin biduality identifies G with the continuous characters of K via g -> evaluation at g. In this case there is also a short proof of the nontrivial surjectivity: continuity of a character at identity gives a neighborhood restricting only finitely many coordinates whose image is in a sufficiently small arc; the subgroup varying all other coordinates maps into that arc, hence trivially (a circle subgroup contained in a small arc is trivial). The character factors through a finite torus, whose characters have integer exponents. Evaluation is therefore surjective and injective (single-coordinate tests). Mark the prime labels, nonnegative cone, and successor on N_+ if the original structure includes addition. The bare group or character space alone does not recover unlabelled addition. The return is a canonical topological group isomorphism for this discrete topology, not an isomorphism between R and Q_p. A different topology changes the dual.

Reference: Morris, [Pontryagin Duality and the Structure of Locally Compact Abelian Groups, duality theorem](https://doi.org/10.1017/CBO9780511600722.007).

## PRF-08. Bohr logarithmic clock, exact asymptotic and finite conditioning

The one-parameter flow z(t)=(exp(-it log p))_p has Haar equidistribution on every finite prime torus. For any nonzero integer exponent vector a, unique factorization gives omega=sum a_p log p !=0, and the normalized symmetric time average of exp(-it omega) is sinc(T omega)->0. Approximation by trigonometric polynomials gives the claim; cylinder functions are uniformly dense in continuous functions of the compact product, giving weak convergence there too. This concerns continuous time, not arbitrary discrete integer-time sampling. No RH is used.

For a finite Dirichlet sum F(s)=sum_{n<=N} a_n n^(-s),

\[
 a_m=\lim_{T\to\infty}(2T)^{-1}\int_{-T}^T F(it)m^{it}\,dt .
\]

The finite-time Gram matrix G has G_mn=sinc(T log(n/m)), diagonal 1. Consecutive labels have gap log(1+1/n)~1/n; their 2x2 condition number is (1+|sinc|)/(1-|sinc|), asymptotic 12 n^2/T^2 for fixed T and n->infty. For 1<=m,n<=N, |log(n/m)|>=|n-m|/N by the mean value theorem. The off-diagonal absolute row sum is <=2NH_(N-1)/T, so by Hermitian row norm bound the spectrum lies in [1-delta,1+delta] for delta=2NH_(N-1)/T. T>=4NH_(N-1) gives condition number <=3 for N>=2. Infinite exact reconstructibility does not pay uniform finite access cost.

Reference: Hedenmalm, Lindqvist and Seip, [A Hilbert space of Dirichlet series and systems of dilated functions in L^2(0,1)](https://arxiv.org/abs/math/9512211). The finite Gram bounds follow directly here, not a new priority claim.

## PRF-09. Quarter-turn and Gamma transport with honest domain

For n>=1 define O_s(n)=exp(-s log n), s=sigma+it. The quarter circle s=r exp(i theta), theta in [0,pi/2], sends real magnitudes n^-r into phase n^-ir. At theta=pi/2 every absolute magnitude is 1, so log-magnitude readout is simultaneously zero on N_+; phases can distinguish labels. One fixed phase readout may alias; the full analytic clock separates. This is a magnitude-null display in an enlarged complex-valued observer space, NOT the same as a path switching between inequivalent rational absolute values (Principia Intermedia #692).

For a finite coefficient family a_n, theta(u)=sum a_n exp(-nu), F(s)=sum a_n n^-s. For Re(s)>0 Euler's Gamma integral and substitution v=nu give

\[
 \int_0^\infty u^{s-1}\theta(u)\,du=\Gamma(s)F(s).
\]

Changing u=e^x rewrites it as the Fourier transform with positive sign of e^(sigma x) theta(e^x). Infinite sums require absolute integrability/interchange hypotheses, e.g. sum |a_n| n^-sigma<infty. The direct Mellin integral generally fails on Re(s)=0 (unless cancellations/other conditions); there the quotient is taken through justified continuation for finite F, not naive substitution into a divergent integral. At Gamma poles a quotient/continuation must be interpreted appropriately. Gamma itself is not a Euclidean quarter-turn. The phase/magnitude change of complex observation parameter is the rotation; Gamma normalizes the Mellin/Fourier relation. Along fixed sigma and large |t|, Stirling gives |Gamma(sigma+it)|~sqrt(2pi)|t|^(sigma-1/2) exp(-pi|t|/2). Dividing a Gamma-weighted numerical signal can amplify high-frequency errors exponentially; the signal and noise model must be declared.

References: NIST DLMF [5.2.1](https://dlmf.nist.gov/5.2.E1), [5.11](https://dlmf.nist.gov/5.11).

## PRF-10. Exact FUCC action/analytic clock and quantitative root return

On H=ell^2(N_+) let e_n be the source basis, V_m e_n=e_(mn) for integer m>=1 (isometry), D e_n=(log n)e_n with self-adjoint domain {x: sum (log n)^2 |x_n|^2<infty}, U_t=exp(itD). Directly on the basis,

\[
 U_t V_m=m^{it}V_m U_t,\qquad [D,V_m]=(\log m)V_m
\]

on finite support for the unbounded commutator (also on the invariant domain). The norm-one diagonal unitaries form a strongly continuous group. The clock's root selector is

\[
 A_T=(2T)^{-1}\int_{-T}^T U_t\,dt,\quad P_1=|1><1|,\quad
 \|A_T-P_1\|\le \min(1,1/(T\log 2)).
\]

Proof: take the strong vector integral, whose diagonal entries are 1 at n=1 and sinc(T log n) otherwise. The uniform positive spectral gap log 2 yields the bound for every n>=2. This strengthens the previous strong-limit claim to norm convergence. It does NOT claim operator-norm Riemann integrability of U_t or finite exact evaluation of the integral. Alternatively, if the real attenuation semigroup exp(-aD) is available, its norm-distance to P_1 is exactly 2^-a for a>0. Both are finite-precision paths with a certified error, not finite equality.

For any fixed m, P_m can similarly be selected by averaging m^-it U_t; the nonzero minimum spectral gap delta_m=min_{n!=m}|log(n/m)| is positive, equal to log((m+1)/m) (also m=1). The norm error <=1/(T delta_m) deteriorates with m. Thus identity selection is uniformly stable in this one sense while high-index reconstruction is expensive.

With declared access to adjoints (V_n^* divides an index by n if divisible, otherwise zero), set E_mn=V_m P_1 V_n^*. Then E_mn e_k=delta_nk e_m and E_mn E_kl=delta_nk E_ml. These are literal matrix units. Their span is the finite-support matrix algebra, strongly dense in B(H): if Q_N projects to first N coordinates, Q_N A Q_N -> A strongly for bounded A, by boundedness and Q_N -> I strongly. Consequently the von Neumann algebra generated by all V_m,U_t is B(H): it contains the adjoints and the integral selector by strong closure, all finite matrix units, then their strong limits. This is an exact operator-algebra theorem for the stated closure, not an executable finite list of all bounded operators; many have no computable descriptions. Forward multiplication alone does not generate these adjoints/limits. No infinite object is made finite merely by calling it a tool.

## PRF-11. Finite exact return and operational bridge

For a fixed finite carrier {1,...,N}, let P_N be all primes <=N, q>floor(log_2 N) an integer (for N=1 handle the trivial case). For each p define the exact finite valuation-phase tool Z_p e_n=exp(2pi i v_p(n)/q)e_n. The finite average q^-1 sum_{j=0}^{q-1} Z_p^j is the diagonal test v_p(n) ==0 mod q, by root-of-unity orthogonality. The product over P_N is exactly P_1 on this finite carrier: the exponent bound removes modular aliasing and unique factorization supplies a nonzero valuation for every n>1. This is a finite algebraic projector, representable with cyclotomic arithmetic, using *declared access* to prime-valuation phases; not a claim that a single real clock sample implements it. Truncated shifts V_m^(N) and their adjoints then realize every E_mn exactly by the same formula. The full finite matrix algebra has N^2 matrix units.

At insufficient q, 1 and 2^q alias whenever 2^q<=N (unless additional observations are used). Refinement q removes aliases. This is a direct bridge between finite analytic completion and a higher-order basis, with a finite constructive witness. If phase tools, arithmetic shifts, their adjoints, and compositions/linear combinations are enumerably available, a finite script for P_1 and any specified E_mn exists and can be checked exactly at the fixed N. PRF-04 supplies a fair a.s. discovery policy, conditional on lawful repeatable execution, not an unconditional discovery theorem for the full infinite algebra.

A second finite calibration: if the observer has complete diagonal span D_N, an acquired action A with A_mn !=0 for m!=n yields E_mm A E_nn=A_mn E_mn. This direction is orthogonal to D_N in the Hilbert-Schmidt metric tr(X*Y). If the available transition graph is strongly connected, composing along paths and rescaling nonzero coefficients yields all matrix units. Conversely lack of directed reachability blocks a unit in this generated algebra: products are sums over admissible directed paths. Diagonal mastery is not mastery of transitions. This is a literal orthogonal innovation, not a deduction from the geometry of a sigmoid learning curve.

Finite witness transfer lemma: suppose a candidate linear operator is in the strong closure of an algebra of finitely constructed operators, and a finite readout L(A) depends continuously on finitely many matrix coefficients, with L(A) separated by a positive margin from the rejection set. Then some finite constructed approximation is accepted by that readout (continuity/definition of closure). If the set of such finite constructions and a robust certificate verifier are effective, PRF-04 applies. No transfer for arbitrary exact equality, uncomputable closures, uncalibrated instruments, or vanishing margins. On a declared finite-dimensional observed row space a strict rank increase has a nonzero determinant witness and an open neighborhood; one can certify it with rigorous error bounds. This does not turn an asymptotic cancellation theorem into a finite certificate without additional argument.

## PRF-12. Ordered transport, cocycle, optional braiding

On H define W_(m,t)=V_m U_t. From PRF-10,

\[
 W_{m,t}W_{n,s}=n^{it}W_{mn,t+s}.
\]

For grades g=(m,t), h=(n,s) in G x (R,+), c(g,h)=exp(it log n) is a bicharacter. The operator representation above uses m,n positive INTEGERS; if a group representation is required, use bilateral multiplicative translations on ell^2(G) and the same D=log coordinate, rather than treating isometries as unitaries. On grades, c(g,h)c(gh,k)=c(h,k)c(g,hk) by distributivity of log and t; ordered exchange ratio c(g,h)/c(h,g)=exp(i(t log n-s log m)) is a retained transport phase. With a specified common frame and chronological convention, identical endpoint grades can retain distinct accumulated phase.

For complex vector spaces graded by G x R (algebraic grading suffices), choose braiding on homogeneous vectors v_g tensor w_h -> c(g,h) w_h tensor v_g. Bilinearity gives both hexagon laws and nonzero scalars give an inverse. The double braiding is c(g,h)c(h,g), not the exchange ratio. The alternating bicharacter c(g,h)/c(h,g) is a different, symmetric-in-the-categorical-sense choice (double braiding identity). The observed operator cocycle does not uniquely force the non-symmetric one-sided choice, nor prove that physical braiding occurs. Without declared transport, no phase.

Define the returned enriched model as the original marked carrier plus the certified duality maps, operator actions, ordered history and optional graded category. Forgetting the extra data recovers the original marked carrier (object-level statement; define model morphisms preserving markings before asserting a forgetful functor or categorical equivalence). Strict enrichment is witnessed on the finite diagonal-versus-transition example: different arrows share an old endpoint report but differ in an enlarged readout. Double duality by itself is involutive and adds no information. This addresses the proposed finite-place -> analytic-place -> higher-order finite-place cycle, not a theorem forcing arbitrary repeated categorical levels.
