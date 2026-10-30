# Fibonacci observations: when extrusion reveals arrows and when it hides them

**PROVED LOCAL**, with classical ingredients identified below. Parent PR408
is `7b5a2b4534aa5e71865046ca8d3f723d8002b9fe`. The author's harmonic/golden/
Euler–Mascheroni triangle and Oily–Macaroni retain Leah / femboy2112 provenance.
No new selected signed bound, physical universal category, external referee,
Lean certification or scholarly priority is asserted.

The precise answer depends on the realization map. Fibonacci translation of
an observable adds only two degrees of freedom. Fibonacci sampling of a
discrete generating function is complete but unstable. Fibonacci moments of
a continuous source are incomplete, even when both authentic BBP marginals
are retained. Keeping compositional products repairs the last defect.

These are explicit statements about arrows, not evidence that a constant by
itself encodes every unseen arrow. The conditional-iid sensor and the selected
arithmetic trajectory remain separately typed.

## FA-01: an entire Fibonacci/Lucas time family still misses a native arrow

Write F_0=0,F_1=1,F_(n+2)=F_(n+1)+F_n, L_n=2F_(n+1)−F_n, and
lambda=(sqrt(5)−1)/2. For every j>=0,n>=1,

    F_(j+n)=F_n F_(j+1)+F_(n−1) F_j.

Thus all translated Fibonacci and Lucas grade observations belong to
span_Q{F_j,F_(j+1)}. Adding every such translate to the parent triangle gives

    V=span_R{1,H_j,lambda^j,F_j,F_(j+1)}.

Consider the parent's native posterior grades at times m and m+d. Its joint
support consists of i<=k<=i+d, 0<=i<=m. With fixed margins the cycle space
has dimension m(d−1), by parent CA-02. The elementary basis cycle at (i,k)
has signs + at (i,k),(i+1,k+1) and − at (i,k+1),(i+1,k).

**Theorem.** At m=6,d=5 there are distinct strictly positive source-labelled
joint arrows with the same full endpoint posteriors and all V×V readouts.
Consequently every two-time product of translated Fibonacci/Lucas,
harmonic, golden, and their affine triangle combinations can agree although
the arrow differs. This holds at every a>0 for the original positive source.

**Proof.** Marginal constraints dispose of the constant. The remaining
rational probes H,F,F_next supply nine rational product constraints.
Their six ordered products with lambda^j supply at most twelve rational
constraints, because lambda lies in Q(sqrt5). The lambda×lambda product adds
at most two. There are therefore at most23 constraints on24 rational cycle
coordinates. A nonzero rational null vector exists. Exact elimination in the
probe gives rank23, so the declared witness leaves one free cycle coordinate.
The larger fresh support m=7,d=5 has rank23 and dimension28.

Normalize the induced edge array Z by max|Z_ik|=1. At a fixed source X=x,
let p=1−exp(−8x), t=1−p and M=m+d. The native conditional joint mass is

    C(m,i) C(d,k−i) p^k t^(M−k).

Add (1/2)p^M t^M Z_ik. Row and column sums remain unchanged pointwise in X.
The ratio of the perturbation magnitude to any allowed native entry is at
most1/2; positivity follows for every0<p<1. All V×V readout defects vanish
pointwise in X by construction. Integrating against the authentic mu_a
preserves both complete (X,J) posterior marginals and all declared readouts.
At rational a its nonzero scale is the exact rational

    epsilon_a=(1/2) E_mu[(1−exp(−8X))^M exp(−8MX)].

The dossier's oracle computes these integrals independently by Beta products.
Euler's common additive constant and Omega_OM=lambda−gamma provide no
additional constraint after the margins have been fixed. They remain valid
absolute anchors. This is not a claim that arbitrary nonlinear functions of
F_j or H_j agree: those can distinguish the arrows.

**Boundary.** The native conditional-iid update is changed. This is a
counterexample to identification from the stated observations, not an
alternative authentic BBP trajectory. The original forcing and U_0=0 are
untouched. If the conditional-iid law is independently verified, it supplies
information absent from the scalar snapshots.

## FA-02: Fibonacci PGF sampling repairs discrete arrows, at a precision cost

Let q_n=lambda^(F_(n+2)), n>=0. These are distinct numbers in(0,1), decreasing
to0. For a joint grade law J on N_0×N_0 define

    G_J(q,r)=sum_(i,j>=0) J_ij q^i r^j.

**Finite theorem.** If the support lies in{0,...,u−1}×{0,...,v−1}, the u×v
matrix M_nm=G_J(q_n,q_m), 0<=n<u,0<=m<v, uniquely determines J.
Indeed M=CJD^T with C_ni=q_n^i and D_mj=q_m^j. Their Vandermonde determinants
are products of nonzero node differences. Thus J=C^−1 M D^−T, exactly in
Q(sqrt5) for rational J. The main test uses elimination; the separate oracle
uses Lagrange polynomial coefficients in SymPy's algebraic-number field.

**Countable theorem.** Every finite signed measure on N_0×N_0 is determined
by the full grid of these samples. Its power series is analytic on the open
unit bidisk. For each fixed sampled r, the one-variable identity theorem at
the accumulation point q=0 gives uniqueness in q. Fixing q and applying the
same theorem in r gives uniqueness of the entire series, hence every
coefficient. In one variable the constructive coefficient peeling is

    p_k=lim_(n→infinity) [G(q_n)−sum_(j<k)p_j q_n^j]/q_n^k.

The limit has arbitrarily large noise amplification. It is not an effective
finite-precision inference about an unbounded support.

**Uniform stability obstruction.** For any M>=0 define two arrows supported
on rows M,M+1 and columns M+1,M+2. Put mass1/2 on the two increasing diagonal
edges for A and on the two opposite edges for B. They have identical margins,
fit the native d=2 grade support, and have total variation distance1. Yet

    |G_A(q_n,q_l)−G_B(q_n,q_l)|
      = (1/2) q_n^M(1−q_n)q_l^(M+1)(1−q_l)
      <= (1/2) lambda^(2M+1)

uniformly in every n,l. Mixing both with the same strictly positive native
finite joint law retains a fixed chosen fraction of this total variation
distance and makes every allowed edge positive. Hence no uniform inverse
modulus in total variation exists for this whole class under absolute sample
error. Fibonacci's rapid exponent growth worsens individual conditioning;
the exact uniqueness theorem would hold for any nodes accumulating inside
the analytic domain. Golden/Fibonacci is not uniquely selected by it.

## FA-03: all Fibonacci powers miss continuous arrows with authentic marginals

This theorem rotates the realization rather than treating its measurement
coordinates as interchangeable. Put z=exp(−8X), for the authentic positive law

    mu_a(dx)=exp(−ax)[4−2exp(−3x)−exp(−4x)−exp(−5x)]dx/R(a), a>0.

Its density on0<z<1 is

    w_a(z)=z^(a/8−1)[4−2z^(3/8)−z^(1/2)−z^(5/8)]/[8R(a)].

Because 1−z^r>=r(1−z) for0<r<=1,

    w_a(z)>=15 z^(a/8−1)(1−z)/[64R(a)].                 (1)

An independent exact polynomial certificate puts z=t^8: eight times the
bracketed source minus15(1−t^8) is

    (1−t)^2(17+34t+51t^2+52t^3+45t^4+30t^5+15t^6)>=0.

**Theorem.** For every a>0 there are distinct positive continuous-carrier
couplings J_+,J_− with both marginals exactly w_a(z)dz and with

    integral x^(F_n) y^(F_m) dJ_+
      = integral x^(F_n) y^(F_m) dJ_−       for all n,m>=2.

In fact a Fibonacci power in either coordinate makes the perturbation
invisible even if the other coordinate uses an arbitrary bounded observable.
All one-place source observables, including every existing harmonic/Gamma/
golden/Oily readout, agree because the full marginals agree. Nevertheless
the mixed fourth moment is strictly different.

**Constructive proof.** Choose an integer L>=max(0,a/8−1). In L2(0,1), let h
be the residual of t^q, q=L+6, after orthogonal projection onto the closed span
of monomials with exponents

    A={L+2} union {L+F_n+2:n>=2}.

It is essential that4 is not a Fibonacci number, so q is absent. For a finite
initial set A_N the exact squared residual norm is the classical Cauchy-Gram
formula

    d_N^2=1/(2q+1) product_(alpha in A_N)
                         [(q−alpha)/(q+alpha+1)]^2.   (2)

For completeness, the moment Gram matrix has entries1/(alpha+beta+1).
Orthogonal projection makes the squared distance the quotient of the Gram
determinant with q adjoined by the old Gram determinant. The Cauchy
determinant product cancels to(2). Alternatively, the residual's Mellin
transform is exactly

    H_N(s)=C_N product_(alpha in A_N)(s−alpha)
              /[(s+q+1) product_(alpha in A_N)(s+alpha+1)],
    C_N=product_(alpha in A_N)(q−alpha)/(q+alpha+1).     (3)

The residue at s=−q−1 is1, and zeros at the alpha give all orthogonality
relations. Equation(3), implemented without Gram elimination, is our separate
finite oracle.

The nested projections converge in L2 to the closed-span projection. The
infinite product in(2) is strictly positive: no factor is zero, and the tail
factors before squaring are

    1−(2L+13)/(F_n+2L+9),

whose deficits have finite sum. Fibonacci's recurrence gives F_(n+2)>=2F_n;
thus the reciprocal Fibonacci series converges. This convergence, not an
assumed mystical property of its numerical value, is load-bearing here.
Consequently h is nonzero, orthogonal to every specified monomial, and
<h,t^q>=||h||_2^2>0.

There is an effective rational lower certificate. If the finite product stops
at Fibonacci index N and

    S_N=(2L+13) 2[1/F_(N+1)+1/F_(N+2)]<1,

then

    d_N^2(1−S_N)^2 <= ||h||_2^2 <= d_N^2.              (4)

Indeed the two parity tails of reciprocal Fibonacci numbers are bounded by
geometric series of ratio1/2, and product(1−u_i)>=1−sum u_i. The tests retain
strict positive rational certificates at N=24, including fresh L=12,29.

Now integrate twice, with an endpoint weight:

    g(z)=z^L integral_z^1 (t−z)h(t)dt.

Cauchy–Schwarz gives

    |g(z)|<=||h||_2 z^L(1−z)^(3/2)/sqrt3,
    ||h||_2<=1/sqrt(2L+13).

The finite polynomial versions converge uniformly to this g. Fubini yields,
for each integer k>=0,

    integral_0^1 z^k g(z)dz
       = <h,t^(k+L+2)>/[(k+L+1)(k+L+2)].              (5)

Thus the integral vanishes for k=0 and k=F_n, but at k=4 it equals

    I_4=||h||_2^2/[(L+5)(L+6)]>0.                    (6)

Let delta=15/[128R(a)]. By(1) and the choice of L,

    |delta g(z)|/w_a(z)
      <= 1/[2sqrt(3(2L+13))] < 1/2.

Define the two joint densities

    J_±(x,y)=w_a(x)w_a(y) ± delta^2 g(x)g(y).          (7)

They are at least(3/4)w_a(x)w_a(y)>0. Equation(5) at k=0 preserves both
marginals exactly. The Fibonacci moment statements follow by factorization.
Equation(6) gives the strictly positive difference

    integral x^4 y^4(dJ_+−dJ_−)=2 delta^2 I_4^2 >0.

This completes the all-horizon statement; finite tests check its ingredients
and rational certificates without pretending to compute an infinite density.

**Precise type.** These are two different couplings of authentic independent-
draw source marginals, replacing the independent arrow by another positive
arrow. They are not the original conditional-iid path law, not changed
four-pole forcing laws, and not a counterexample to π normality. Their
unchanged marginals make them stronger source-observation controls than a
Gamma-matched fake, but no assertion of arithmetic admissibility is made.

## FA-04: Zeckendorf composition restores the missing information

Every nonnegative integer k is a sum of distinct nonadjacent Fibonacci
numbers F_j,j>=2. The greedy construction proves existence: if F_j<=k<F_(j+1),
the remainder is smaller than F_(j−1), so the next selected index is at most
j−2. It terminates and provides the canonical Zeckendorf decomposition.

For a source coordinate z, the pointwise observable product

    product_(j in Z(k)) z^(F_j) = z^k

therefore recovers every ordinary moment from a declared composed observable.
If two finite joint measures agree on all such products in both coordinates,
they agree on all bivariate polynomial moments. Bernstein polynomial
approximation on[0,1]^2 then gives equality against every continuous function,
hence equality of measures. This is a sufficient complete family of joint
observations, not a theorem saying isolated measurements provide those
products for free.

The FA-03 aliases are separated already by 4=3+1 (F_4=3 and F_2=1;
the omitted **exponent**4 is not a Fibonacci value): retain the product of the
F_4 and F_2 probes at each endpoint, and the mixed fourth moment differs by
the explicit positive amount above. An observation of E[z^3] and E[z]
separately does not give E[z^3 z]. This is exactly the missing same-coordinate
composition information.

There is a real distinction here between *linear span* and *observable
algebra*. Fibonacci sampling is too sparse for the former on a continuum;
its compositional closure is complete. Multiplication of observables is not
automatically stochastic composition of causal kernels, nor a physical
experiment. The lawful operation and retained joint information must be
specified by the carrier model.

## Literature, prior program, and remaining signed obligation

Classical Müntz/Gram mechanisms are not new claims. Primary context:
Borwein–Erdélyi, [The Full Müntz Theorem in C[0,1] and L1[0,1]](https://doi.org/10.1112/jlms/54.1.102),1996; their research paper
[Lacunary Müntz systems](https://www.cecm.sfu.ca/~pborwein/PAPERS/P65.pdf),1993.
Our exact positive-coupling application is proved above. Almira's author
[survey](https://pages.cs.wisc.edu/~deboor/sat/papers/10/10.pdf),§2.1, provides
an independently inspectable exposition of the Gram quotient. The browser
could read the survey; the very large Borwein PDF open hit a tool size limit,
so no uninspected theorem from that PDF is used as a necessary premise.

Inherited sources: parent CA-01–04 for grade arrows; October13 positive-carrier
II Fibonacci cat system for the distinction between field, behavior and
carrier; October30 Fibonacci epicycle dossier for the declared S/S² clock,
golden contraction, and its explicit failure to identify a native BBP clock.
These older results are credited, not recounted as new discoveries.

The reciprocal Fibonacci sum is used here as a convergence threshold for
observation completeness. Lambda sets a declared analytic sampling scale.
Fibonacci/Lucas translation controls finite rank. Gamma/Euler/Oily one-place
anchors survive the coupling aliases; they do not supply the omitted mixed
moment. Each constant has a mathematical job with a declared domain.

The next genuine arithmetic obligation is unchanged: identify a composed
observable with the authentic zero-boundary selected signed character, and
prove a uniform saving that fails for the same-forcing coherent seed. None
of FA-01–04 establishes that bridge. Source-only observations survive the
changed seed s=−pi/16; rational circle aliases must remain acceptable to any
normality statement. π normality and RH remain OPEN.
