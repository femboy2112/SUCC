# A source-preserving algebra of BBP causal volumes

**Date:** 2026-11-15. **Parent:** draft #635 at `e14d46c17a65e1e5f231c619657b9332caa181c0`.

The question is whether expanding BBP into its causal-volume constituents produces reusable reasoning rules. The answer is **yes, within a declared algebra**. Expansion exposes several distinct products and observation maps. Their lawful rules retain the source labels, clock, boundary condition, and integer lift. A finite polynomial calculus exists; the actual phase sequence cannot close in any finite linear recurrence with rational functions of time as coefficients, even with complex constants. This last statement is an algebraic obstruction, not a cancellation estimate.

“PROVED” below means a mathematical derivation within its displayed hypotheses, with separate finite implementation checks. It does not mean a Lean proof or external peer review. Classical identities and inherited source mechanisms are identified in [PROVENANCE.md](PROVENANCE.md). No academic priority is claimed.

## VA-01. The fixed source and its literal Gamma expansion

For integers n>=1 fix

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Write a_n=8n-7, d=(0,3,4,5), c=(4,-2,-1,-1), and

\[
q(t)=\sum_d c_d e^{-dt}
=2(1-e^{-3t})+(1-e^{-4t})+(1-e^{-5t}).
\]

For real a>0,

\[
\mathcal R(a)=\sum_d\frac{c_d}{a+d}
=\int_0^\infty e^{-at}q(t)dt
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)}.
\]

Thus r(n)=Rcal(a_n). Every pole is the elementary causal-volume integral

\[
\frac1{a+d}=\frac1{\Gamma(1)}\int_0^\infty e^{-(a+d)t}dt.
\]

This is an exact identity, not a stochastic model for the digits. The source is positive because q(t)>0 for t>0, although its four exponential channels have signed coefficients. Its endpoint cancellation is q(0)=0, q'(0)=15. Euler's integral and the Laplace product/convolution law are classical; this exact signed source and its Gamma(2) endpoint are inherited.

## VA-02. Products of the source produce a finite Gamma-kernel calculus

For every integer j>=1, absolute integrability and Fubini give

\[
\boxed{\mathcal R(a)^j=\int_0^\infty e^{-at}q^{*j}(t)dt.}
\]

The convolution is over **independent lag coordinates with their sum fixed**. Replacing it by the pointwise product q(t)^j changes the object. Since Rcal(a)^j is a proper rational function with the four distinct poles -d, each of exact order j, it has the unique partial-fraction expansion

\[
\mathcal R(a)^j=\sum_{d\in\{0,3,4,5\}}\sum_{k=1}^{j}
\frac{C_{j,d,k}}{(a+d)^k},\qquad C_{j,d,k}\in\mathbb Q.
\]

Consequently

\[
\boxed{q^{*j}(t)=\sum_d\sum_{k=1}^j
C_{j,d,k}\frac{t^{k-1}}{\Gamma(k)}e^{-dt}.}
\]

There are 4j labelled coefficient slots; some lower-order coefficients can vanish. The highest coefficient at pole d is c_d^j, so the pole itself is never lost. This collapses the 4^j channel choices in a direct product expansion into a finite exponential-polynomial basis. It preserves the full source, rather than only its asymptotic Gamma shape.

The leading simplex volume follows from q(t)=15t+O(t²) and repeated Beta convolution:

\[
\boxed{q^{*j}(t)=\frac{15^j}{\Gamma(2j)}t^{2j-1}+O(t^{2j}),\quad t\downarrow0.}
\]

Equivalently, all Taylor coefficients of degrees 0 through 2j-2 in the signed partial-fraction inverse cancel. The coefficient of degree 2j-1 is 15^j/(2j-1)!. This is an actual all-order cancellation rule. It concerns the **lag kernel**, not the temporal Weyl sum.

### A complete square, with nothing hidden in an asymptotic symbol

At j=2,

\[
\begin{aligned}
q^{*2}(t)={}&16t-\frac{134}{15}
+\left(4t+\frac{34}{3}\right)e^{-3t}
+t e^{-4t}
+\left(t-\frac{12}{5}\right)e^{-5t}.
\end{aligned}
\]

The constant, linear and quadratic coefficients cancel, and

\[
q^{*2}(t)=\frac{75}{2}t^3+O(t^4)
=225\frac{t^3}{\Gamma(4)}+O(t^4).
\]

The displayed full kernel, which is positive as a convolution, retains its signed channel decomposition. Keeping only its Gamma(4) leading term would discard source information.

### A quantitative normalized Gamma statement

Let T_1,...,T_j be independent variables with the **declared** density e^{-at}q(t)/Rcal(a), a>0. Independence is an assumption of this convolution construction, not inferred from BBP digits. Put Y=a(T_1+...+T_j). Since

\[
15t-\frac{59}{2}t^2\le q(t)\le15t,
\]

the nonnegative kernel obeys q^{*j}(t)<=15^j t^{2j-1}/Gamma(2j). Set

\[
Z_{a,j}=\left(\frac{a^2\mathcal R(a)}{15}\right)^j\in(0,1).
\]

The unnormalized scaled density

\[
g_{a,j}(y)=\frac{a^{2j-1}}{15^j}e^{-y}q^{*j}(y/a)
\]

is pointwise bounded by the Gamma(2j,1) density and has mass Z_(a,j). Hence, with total variation defined as one half the L1 distance,

\[
\boxed{\operatorname{TV}\bigl(Y,\Gamma(2j,1)\bigr)
\le1-Z_{a,j}\le\min\left(1,\frac{59j}{15a}\right).}
\]

Proof of the first inequality: write the Gamma density as Z_(a,j) times the normalized source density plus a nonnegative remainder of mass 1-Z_(a,j). For the second, integrate the lower quadratic bound to get 1-a²Rcal(a)/15<=59/(15a), then use 1-z^j<=(1-z)j for 0<=z<=1. This is a source-specific consequence of a classical envelope argument, not a signed digit-frequency theorem.

## VA-03. The discrete causal product has a radix grade and a diagonal correction

For a commutative scalar algebra, positive scalars b,c, and arbitrary finite source sequences f,g, define

\[
(G_b f)_n=\sum_{k=1}^n b^{n-k}f_k,\qquad (G_b f)_0=0.
\]

Let F=G_b f and H=G_c g. Then

\[
\boxed{(G_b f)(G_c g)=G_{bc}\bigl[f(G_c g)+g(G_b f)-fg\bigr].}
\]

Proof: F_n=bF_(n-1)+f_n and H_n=cH_(n-1)+g_n imply

\[
F_nH_n-bcF_{n-1}H_{n-1}=f_nH_n+g_nF_n-f_ng_n.
\]

Both sides have zero initial product, so solving this first-order recurrence proves the identity. The subtraction corrects double counting of two inputs arriving at the same discrete time. At b=c=1 this is the classical inclusive-sum Rota–Baxter identity of weight -1. At b=c=16 its outer radix is **256**.

For nonzero initial values F_0=u,H_0=v, the exact rule is

\[
F_nH_n=(bc)^nuv+G_{bc}[fH+gF-fg]_n,
\]

where the forcing uses the **full seeded** F,H. Adding only the homogeneous uv term to an otherwise unseeded formula omits mixed seed/source terms.

### Continuous counterpart and the distinct Gamma-depth rule

For f,g in L1([0,T]), finite T>0 and real decay rates lambda,mu>=0, let

\[
J_\lambda f(t)=\int_0^t e^{-\lambda(t-s)}f(s)ds.
\]

The product rule is

\[
(J_\lambda f)(J_\mu g)
=J_{\lambda+\mu}[fJ_\mu g+gJ_\lambda f].
\]

There is no diagonal term for ordinary Lebesgue integration: the equal-time diagonal has measure zero. Separately, the fractional causal kernels

\[
k_{\alpha,\lambda}(t)=1_{t>0}e^{-\lambda t}t^{\alpha-1}/\Gamma(\alpha)
\]

satisfy k_(alpha,lambda)*k_(beta,lambda)=k_(alpha+beta,lambda), alpha,beta>0, by the Beta integral. Composition adds **depth**, whereas multiplication of two first-order responses adds **decay rates**. These rules cannot be interchanged. For example I_2(1)^2=t^4/4 while 2I_2(I_2(1))=t^4/12; an arbitrary fractional integral is not the ordinary weight-zero Rota–Baxter operator.

## VA-04. A terminating, associative word algebra implements these rules

A letter contains a positive rational radix b and a commutative monomial f in named source channels. The word (b,f)w denotes G_b(f eval(w)); the empty word denotes 1. Source labels remain distinct even when two chosen numerical rows happen to coincide.

For A=(b,f)A' and B=(c,g)B', define the bilinear word product

\[
\begin{aligned}
A\star B={}&(bc,f)(A'\star B)
+(bc,g)(A\star B')\\
&-(bc,fg)(A'\star B').
\end{aligned}
\]

The empty word is the unit. Recursion decreases the sum of input lengths, hence terminates. VA-03 inductively proves eval(A star B)=eval(A)eval(B) for every finite source table. Identical words are collected with rational coefficients.

This formal product is associative and commutative. One proof first changes the minus collision to a plus collision. The positive-collision product enumerates ordered partitions with strict order within each formal input word: at each output position multiply the radices of **all currently active heads**, including unconsumed heads, and consume a nonempty subset, multiplying the consumed source labels. The description is independent of parenthesization. The length sign map epsilon(w)=(-1)^(length(w))w transports the negative-collision product to the positive one; every collision decreases the output length by one. This formal strict-order argument proves associativity of the product used for inclusive evaluation, including multiplicities.

The resulting collected expansion is a normal form **for this defined free word product**. It is not a complete equality solver after specialization to rational source functions, and is not a decision procedure for arbitrary analytic identities. The implementation declares separate depth, horizon, and term-count budgets and rejects over-budget requests. Zero source rows, accidental identities, and extra integration-by-parts relations can identify different formal words after evaluation.

The original BBP expression is exactly

\[
U=4G_{16}p_1-2G_{16}p_4-G_{16}p_5-G_{16}p_6,
\quad p_d(n)=\frac1{8(n-1)+d}.
\]

Its square collects into 26 words and its cube into 164 words in this representation. These finite counts are implementation observations, not dimensions of a minimal semantic model. VA-02 supplies the lag-kernel expansion of all pointwise forcing products that appear in the words.

## VA-05. The polynomial observables close in a finite rational system

There is a literal ordered-volume realization of these grades. Let

\[
f_n(x)=(4-2x^3-x^4-x^5)\sum_{j=1}^n16^{n-j}x^{8(j-1)}
=(16^n-x^{8n})R(x),\qquad f_0=0.
\]

This finite polynomial is nonnegative on [0,1], and its integral is exactly U_n. Symmetry and the measure-zero collision diagonals imply

\[
\boxed{V_{n,k}:=\frac{U_n^k}{\Gamma(k+1)}
=\int_{0<x_1<\cdots<x_k<1}\prod_{i=1}^k f_n(x_i)\,dx_1\cdots dx_k.}
\]

Set V_(n,0)=1. This is the ordered volume in the proposed expansion; its clock is still the actual BBP n. The complete generating function has the exact identities

\[
\mathcal S_n(t)=\sum_{k\ge0}V_{n,k}t^k=e^{tU_n},\qquad
\mathcal S_{n+1}(t)=e^{t r(n+1)}\mathcal S_n(16t).
\]

These hold formally and as entire functions for each fixed n. Evaluation at t=2pi i h gives the actual phase. No bound uniform in n is inferred from truncating the volume grade.

For any fixed integer d>=0, let v_n=(1,U_n,...,U_n^d)^T. The binomial theorem gives

\[
v_n=A_d(n)v_{n-1},\qquad
(A_d(n))_{k\ell}=\binom{k}{\ell}16^\ell r(n)^{k-\ell}
\quad(0\le\ell\le k\le d),
\]

and zero above the diagonal. These are rational functions of n. Thus every polynomial observable of degree at most d, with rational-function coefficients in n, has a rational first-order system of dimension d+1. Taking d+2 consecutive output rows over Q(n) gives a linear dependence, hence a scalar recurrence of order at most d+1, away from finitely many poles. No minimal-order claim is made.

For the state itself, q_n=r(n+1)/r(n) is defined for all n>=1, and

\[
\boxed{U_{n+1}-(16+q_n)U_n+16q_nU_{n-1}=0.}
\]

For every integer k>=1, the causal power hierarchy is also explicit:

\[
\boxed{U_n^k=G_{16^k}\left[
\sum_{j=1}^k(-1)^{j+1}\binom{k}{j}r^jU^{k-j}
\right]_n.}
\]

It follows from U_n-r(n)=16U_(n-1), with the zero initial condition. Each forcing power r^j has the 4j-slot continuous kernel of VA-02. These two clocks have an explicit map between them; they are not identified merely because both involve Gamma.

## VA-06. The actual signed phase does not have finite linear holonomic closure

Fix an integer h!=0, and define z_n=exp(2pi i h U_n). Then:

\[
\boxed{\text{There are no finite }d\text{ and }a_0,...,a_d\in\mathbb C(n),
\text{ not all zero, with }\sum_{j=0}^d a_j(n)z_{n+j}=0
\text{ for every sufficiently large integer }n.}
\]

In standard language, z is not P-recursive, even allowing complex polynomial coefficients. The proof extends the inherited PG-09 prime-birth noncancellation lemma; the original prime-birth mechanism is not new here.

**Step 1: a fresh prime cannot be absorbed by a fixed number field.** Let p=8b-7 be prime, p>5 and p not dividing h. For i<b every source denominator used by U_i is less than p. At b,

\[
U_b=4/p+B_b,\quad
B_b=16U_{b-1}-2/(p+3)-1/(p+4)-1/(p+5),
\]

with p not dividing the reduced denominator of B_b. Let M be the least common multiple of the denominators of B_b and the earlier U_i. Then p does not divide M. All previous phases and exp(2pi i hB_b) lie in E=Q(zeta_M), while z_b=exp(2pi i hB_b) zeta_p^(4h).

For any fixed number field K, a K-linear relation ending in a nonzero coefficient of z_b would put zeta_p in KE. But

\[
[E(\zeta_p):E]=p-1,\qquad [KE:E]\le[K:\mathbb Q].
\]

It is impossible when p-1>[K:Q]. The cyclotomic degree follows from coprimality of p and M and the usual degree formula phi(Mp)/phi(M)=p-1.

There are arbitrarily large primes p==1 mod8 by an elementary argument. Given finitely many such primes, choose an even integer N divisible by all of them. Any prime divisor q of N^4+1 is odd and new, and N has multiplicative order exactly 8 modulo q. Hence q==1 mod8. This avoids an unnecessary use of Dirichlet's theorem.

**Step 2: descend any alleged complex recurrence to one number field.** Clear the rational-function denominators of a hypothetical recurrence. Its finitely many polynomial coefficients are complex unknowns in a homogeneous linear system, one row for each sufficiently large n. Every row entry is algebraic, since U_n is rational and z_n is a root of unity. Choose a finite row basis over the field of algebraic numbers. A nonzero minor shows this basis has the same rank over C. Thus a nontrivial complex kernel implies a nontrivial algebraic kernel, which satisfies every row. The finitely many algebraic coefficients lie in one number field K.

Reselect the largest shift e with nonzero polynomial coefficient in this algebraic relation. Choose a fresh prime endpoint b so large that b-e lies in the eventual recurrence range, the leading coefficient is nonzero there, p does not divide h, and p-1>[K:Q]. Specializing the relation at n=b-e contradicts Step 1. This proves the boxed statement.

**Boundary:** the exact nonlinear rule remains

\[
z_{n+1}=e^{2\pi i h r(n+1)}z_n^{16}.
\]

The theorem excludes finite **linear** closure over rational functions of time. It does not exclude nonlinear finite programs, growing cyclotomic carriers, or useful analytic estimates. It does not prove temporal cancellation: the control eta_n=exp(2pi i/p_n), for successive primes p_n, has the same nonrecurrence obstruction but eta_n tends to 1 and its normalized sums tend to 1.

## VA-07. Phase and carry are lawful nonlinear extensions of the algebra

Write U=A+theta, A an integer and 0<=theta<1. An integer-radix affine step (b,f) sends

\[
C=\lfloor b\theta+f\rfloor,\qquad
A'=bA+C,\qquad \theta'=b\theta+f-C.
\]

The phase rule exp(2pi i hU')=exp(2pi i hf)exp(2pi i hU)^b is exact for integer h. A general noninteger b does not descend to the circle without choosing a lift.

Chronological affine composition is

\[
(b,f)\circ(c,g)=(bc,bg+f).
\]

Its carry obeys C_composite(theta)=b C_first(theta)+C_second(theta_after_first). Separately the additive section defect

\[
\kappa(x,y)=\lfloor\{x\}+\{y\}\rfloor
\]

satisfies kappa(x,y)+kappa(x+y,z)=kappa(y,z)+kappa(x,y+z). The carry is therefore a structured correction that makes composition consistent; deleting it changes the represented real state.

For a finite index set, rational weights w_j and integer h, phase after a real weighted sum has the exact factorization

\[
e^{2\pi ih\sum_j w_jU_j}
=e^{2\pi ih\sum_j w_j\theta_j}
e^{2\pi ih\sum_j w_jA_j}.
\]

It descends from arbitrary **fundamental** input phases exp(2pi i U_j), equivalently U_j modulo one, alone iff every h w_j is an integer. Otherwise the minimal independent integer-lift information for coordinate j is A_j modulo den(h w_j), in reduced form. Necessity follows by changing just A_j by one; sufficiency follows because adding the displayed denominator changes the exponent by an integer. Observing only exp(2pi i h U_j) for |h|>1 forgets additional fractional information and is a different descent problem.

For authentic U_1=47/15, the weight 1/2 gives phase exponent 17/30 modulo one. Dropping its integer lift 3 gives 1/15 instead: a phase error of exactly one half turn.

At integer Gamma depth m>=1 and rate 1, w_j=binom(j+m-1,j)/2^(j+m). For fixed h!=0 the required denominators obey

\[
\operatorname{den}(hw_j)\ge
\frac{2^{j+m}}{|h|\binom{j+m-1}{j}}\longrightarrow\infty.
\]

Thus no one finite carry modulus suffices at all grades for arbitrary finite-support lift changes. This is a quotient-descent theorem, not permission to alter the fixed BBP seed. Earlier repository work already identifies the finite rational-filter carry obstruction; the all-grade Gamma statement makes its growth explicit.

## VA-08. Gamma filtering has an exact source-dependent convergence threshold

For real alpha,lambda>0 define the normalized weights

\[
w_j^{\alpha,\lambda}=\frac{\Gamma(j+\alpha)}{\Gamma(\alpha)j!}
\frac{\lambda^\alpha}{(\lambda+1)^{j+\alpha}}.
\]

They sum to one. On bounded sequences the future shift E has norm one, and the positive Gamma filter is

\[
F_{\alpha,\lambda}(E)
=\sum_{j\ge0}w_j^{\alpha,\lambda}E^j
=\left(\frac{\lambda}{\lambda+1-E}\right)^\alpha.
\]

The last formula represents that series only in its domain. An algebraically defined inverse outside the domain does not extend the positive averaging operation.

Use the inherited authentic kernel and Green decomposition

\[
R(x)=\frac{1-x}{(2-x^2)(x^2-2x+2)},\quad
T_n=\int_0^1x^{8n}R(x)dx,\quad
U_n=16^n\xi-T_n,\quad \xi=T_0=\pi/16.
\]

Tonelli gives the exact bounded-tail transport

\[
\boxed{F_{\alpha,\lambda}(E)T_n
=\int_0^1 x^{8n}R(x)
\left(\frac{\lambda}{\lambda+1-x^8}\right)^\alpha dx.}
\]

Also (16-E)T_n=r(n+1), and (16-E) commutes with this filter on bounded sequences. This is a lawful deterministic map between the original source and a Gamma-volume kernel; it does not posit that arithmetic phases are sampled from a positive latent law.

For the **raw original states**, the full positive future sum sum_j w_j U_(n+j) converges if and only if

\[
\boxed{\lambda>15.}
\]

Indeed U_(n+j)~16^(n+j)xi, while w_j behaves as a positive constant times j^(alpha-1)(lambda+1)^(-j). At lambda<15 the terms grow exponentially. At lambda=15, the remaining positive series is proportional to sum_j (alpha)_j/j!, whose partial sums equal (alpha+1)_M/M! and diverge for every alpha>0. Terms can tend to zero at the threshold when alpha<1; the series still diverges.

For lambda>15 the constructive formula is

\[
\boxed{\sum_{j\ge0}w_j^{\alpha,\lambda}U_{n+j}
=16^n\xi\left(\frac{\lambda}{\lambda-15}\right)^\alpha
-\int_0^1x^{8n}R(x)
\left(\frac{\lambda}{\lambda+1-x^8}\right)^\alpha dx.}
\]

For 0<lambda<=15, the subtracted series sum_j w_j[U_(n+j)-16^(n+j)c] converges **if and only if c=xi**. Then it is exactly minus the bounded-tail integral. A nonzero boundary error, however small, leaves the divergent homogeneous contribution. For lambda>15 every c is summable, so this uniqueness assertion must not be extended past the threshold.

The rate-one Gamma filter from #635 is valid on bounded observables and tails. Applied forward to raw U it is outside its declared contraction domain. At integer shape m its algebraic scalar resolvent (2-16)^(-m) exists, but is not the value of the divergent positive series. Retarded finite-prefix filtering and filtering the already-formed unit phases are separately valid operations. Neither is interchangeable with exponentiating a filtered real lift.

## VA-09. Mellin translation retains endpoint terms and operator order

Define M(f)(n)=integral_0^1 x^(8n)f(x)dx. For an integrable f,

\[
E\mathcal M(f)=\mathcal M(x^8f).
\]

For a fixed n>=0, suppose f is locally absolutely continuous on (0,1], has finite endpoint f(1), both x^(8n)f(x) and x^(8n+1)f'(x) are integrable, and x^(8n+1)f(x) tends to zero at 0. Integration by parts gives

\[
\boxed{(8n+1)\mathcal M(f)(n)=f(1)-\mathcal M(xf')(n).}
\]

The endpoint f(1) is part of the rule. Taking f=1 immediately detects an omitted boundary. The source R has R(1)=0, but its differentiated descendants need not have zero endpoint.

For N multiplication by n and E forward shift, EN=(N+1)E. This is the elementary skew-shift/Ore relation. Moving n and E past each other as if they were commuting symbols changes the calculation. The exact zero seed in the discrete Green rule and the endpoint term in Mellin integration by parts are different boundaries, both retained.

## What has and has not been obtained

The constructive result is a reusable algebra with exact source-kernel reduction, a graded causal-sum product, a bounded symbolic compiler, finite polynomial lifts, and explicit phase/carry and convergence rules. The all-order Gamma endpoint cancellation and the non-P-recursiveness theorem locate a precise change of representation between the rational state and its signed observation.

The unresolved task remains a source-specific uniform estimate on the actual signed sequence, for example sum_(n<N) exp(2pi i hU_n)=o(N) for every fixed nonzero integer h. The present results do not supply that estimate. A productive next use of the algebra would preserve the growing phase/carry information while reducing the complete signed correlations with a certified error. A formal expansion, a positive Gamma marginal, a changed-seed control, and a finite numerical sum cannot substitute for that estimate.
