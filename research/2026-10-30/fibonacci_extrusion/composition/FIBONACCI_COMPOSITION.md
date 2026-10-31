# Fibonacci extrusion: fresh composition, retained memory and the triangle

**PROVED LOCAL, paper authority.** Original signed four-pole source and zero
arithmetic boundary are unchanged. These results describe declared positive
source arrows. They do not assume that pi digits are independent draws.
Leah / femboy2112 retains the original Harmonic / Golden / Euler-Mascheroni
triangle and Oily-Macaroni provenance. No scholarly priority is asserted.

Set Q(x)=4-2e^(-3x)-e^(-4x)-e^(-5x),
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),
mu_a(dx)=e^(-ax)Q(x)dx/R(a), a>0. Thus R(8n-7)=r(n).
Write m_a=-R'(a)/R(a), v_a=R''(a)/R(a)-m_a²>0,
lambda=(sqrt5-1)/2, phi=1/lambda, F_0=0,F_1=F_2=1.

The independent convolution arrow of parent FC07 has a harmonic correction.
The point of the present round is that extrusion requires specifying *which
copies survive into the next arrow*. Fibonacci integer counts alone do not
specify this. We prove a uniform joint-rank result, then compare two exact
extrusions and their distinct accumulated/absolute triangle observables.

## FIC01: a dimension-free harmonic correction

For iid X_1,...,X_k with law mu_a, let S_k=sum X_i and

    K_k(a)=E log S_k-E log X_1-[H_(2k-1)-1],  k>=1.

For every integer k>=1 and real a>=5,

    |a² K_k(a) - (1379/900)(k-1)/(2k+1)| <= 1627/(45a).       (1)

For k>=2, K_k(a)>0 by parent FC07. Unlike its fixed-k asymptotic,
(1) is uniform over arbitrarily large k. In particular, for **any** sequence
of integers k_j→infinity and real a_j→infinity,

    a_j² K_(k_j)(a_j) → 1379/1800.                           (2)

At the declared native Fibonacci schedule k_j=F_j, a_j=8F_j-7,

    F_j² K_(F_j)(8F_j-7) → 1379/115200.                      (3)

The source does not select this schedule merely because it is valid.

**Proof with explicit uniform remainder.** Parent FC07 derives the exact
mixture X=G/(a+T), with G~Gamma(2,1) independent of T~nu_a. The untilted law
of T has density [2 1_(0,3)+1_(0,4)+1_(0,5)]/15, variance
sigma²=1379/900. Its tilted law has density proportional to (a+T)^(-2).
For iid T_i put z_i=-log(1+T_i/a), and independent
w_i=G_i/(sum G_j), so w~Dirichlet(2,...,2). Then exactly

    K_k(a)=E[ log(sum_i w_i exp(z_i)) - k^(-1)sum_i z_i ].    (4)

The range of the z_i has length at most L=log(1+5/a).
For fixed w,z, the third derivative of log(sum_i w_i exp(t z_i))
is the third central moment of a probability law supported in that interval;
its absolute value is <=L³, uniformly in t and k. Taylor at t=0 therefore
has remainder <=L³/6. Averaging the linear term gives zero. The exact
Dirichlet moments E w_i²=3/[k(2k+1)], E w_iw_j=2/[k(2k+1)] for i!=j give

    |K_k(a) - (k-1)/(2k+1) Var_nu(log(a+T))| <= L³/6.       (5)

This also holds at k1 (where the actual remainder is zero).
Put x=5/a<=1. The tilted density relative to the original law lies between
(1+x)^(-2) and (1+x)^2. The identity Var(Z)=inf_c E(Z-c)², followed by
the independent-pair formula for variance and the derivative bounds of log,
gives

 sigma²(1+x)^(-4) <= a² Var_nu(log(a+T)) <= sigma²(1+x)^2.

Since 1-(1+x)^(-4)<=4x and (1+x)^2-1<=3x,

    |a² Var_nu(log(a+T))-sigma²| <=20 sigma²/a.

Use (k-1)/(2k+1)<1/2 and L<=5/a in (5). The resulting constant is
10 sigma²+125/6=1627/45. This proves (1) without interchanging a fixed-rank
limit with a growing-rank limit. Equations(2),(3) now follow directly.

The same proof works for any bounded nondegenerate rate mixture, with its
own variance and support bound. Consequently this identifies the original
source's coefficient within the declared family, not the whole source or
selected seed. The rank-matched two-pole mutant has variance3481/2700;
a higher-jet-matched mutant can share the original leading coefficient.

## FIC02: the two Fibonacci arrows are different

**Fresh convolution.** Start nu_1=nu_2=mu_a and define
nu_(n+1)=nu_n*nu_(n-1), using independent copies at each convolution.
Induction gives nu_n=mu_a^(convolution F_n). A concrete coherent realization
of these marginals is Z_n=X_1+...+X_(F_n) from one iid sequence: the block
added to Z_n is independent of Z_n and has law nu_(n-1), but it is *not*
the previously realized Z_(n-1).

**Retained memory.** Take only two iid source draws X,Y, set W_1=X,W_2=Y,
and perform the literal path recursion W_(n+1)=W_n+W_(n-1). Then for n>=2,

    W_n=F_(n-2)X+F_(n-1)Y.                                 (6)

Thus both arrows have the same Fibonacci mean F_n m_a and the same initial
laws at n1,2,3, but

 Var(Z_n)=F_n v_a,
 Var(W_n)=[F_(n-2)²+F_(n-1)²]v_a=F_(2n-3) v_a, n>=2.       (7)

At n4 the variances are3v_a and5v_a. The Laplace transforms are
L_a(t)^(F_n) and L_a(F_(n-2)t)L_a(F_(n-1)t), respectively, with
L_a(t)=R(a+t)/R(a). This is an exact failure of the claim that equal
Fibonacci counts determine the extrusion. No approximation is involved.

The normalized limits are

    Z_n/F_n → m_a in L² and almost surely,
    W_n/F_n → lambda² X+lambda Y in L² and almost surely.    (8)

The first follows either from iid averaging or FIC03's summable Chebyshev
bound; the second follows directly from Binet. Its limiting variance is

    (lambda^4+lambda²)v_a=(5-2sqrt5)v_a>0.                   (9)

This is a precise load-bearing role for the golden eigenvector: it fixes
the surviving memory weights, rather than merely labeling a chosen time.
The arithmetic BBP update is neither stochastic recursion asserted here.

## FIC03: the reciprocal Fibonacci constant is an exact fluctuation budget

Let C_F=sum_(n>=1)1/F_n (the duplicated value F1=F2=1 is intentional).
For the fresh coherent realization in FIC02, Tonelli and (7) prove

    E sum_(n>=1)(Z_n/F_n-m_a)² = v_a C_F.                  (10)

No independence across the different n is needed. For each N>=1,

  0 < C_F-sum_(n=1)^N 1/F_n
      <=2/F_(N+1)+2/F_(N+2),                              (11)

because F_(j+2)>=2F_j and each parity tail is geometric. This provides an
exact rational enclosure and the explicit probability estimate

 P(exists n>N: |Z_n/F_n-m_a|>=epsilon)
     <= (2v_a/epsilon²)(1/F_(N+1)+1/F_(N+2)).               (12)

The finite total expected error also implies its samplewise sum is finite
almost surely. Thus C_F does real work: it controls the full extrusion's
fluctuations at the declared Fibonacci ranks. For reused memory the total
expected squared error is infinite by (9), and (12) is false in general.
This is a source-sampling theorem, not an estimate for BBP phase errors.

## FIC04: distinct extruded Oily anchors

Put ell_a=E exp(-lambda a X)=R(a(1+lambda))/R(a) in(lambda²,lambda),
and define the natural log-minus-Laplace readouts

 D_n^fresh(a)=E log(aZ_n)-ell_a^(F_n),
 D_n^memory(a)=E log(aW_n)-E exp(-lambda aW_n).

Both start from the same rank-two source contrast, whose a→infinity limit
is the author's Omega_OM=lambda-gamma. Their time-extruded finite parts differ:

 lim_n [D_n^fresh(a)-n log(phi)] = log(a m_a)-log(5)/2,
 lim_n [D_n^memory(a)-n log(phi)]
     = E log[a(lambda²X+lambda Y)]-log(5)/2.                (13)

For fresh averaging, log expectations converge as follows. The mixture
couples X_i>=G_i/(a+5), so
E[(Z_n/F_n)^(-1)]<=(a+5)F_n/(2F_n-1)<=a+5.
Together with its bounded first moment, the inequality
|log x|²<=C(x+x^(-1)) gives uniform integrability of logs. L² convergence in
(8) then yields expectation convergence. For retained memory, eventually
both normalized coefficients lie in a fixed positive interval, making
log(W_n/F_n) dominated by a constant plus |log(X+Y)|. The Laplace terms
vanish by dominated convergence. Finally log F_n-n log(phi)→-log5/2.

The separation between the two finite parts is the strictly positive
source-dependent Jensen gap

    J_a=log m_a-E log(lambda²X+lambda Y)>0.                 (14)

It has a concrete moment lower bound. Set V=lambda²X+lambda Y,
s²=Var(V)=(5-2sqrt5)v_a. Taylor's integral remainder for -log gives
u-1-log u >=(u-1)²/[2(u+1)²] for u>0. Cauchy-Schwarz therefore gives

    J_a >= s^4 / {2 E[(V²-m_a²)²]} >0.                    (15)

Here s^4 means (Var V)². All moments on the right are finite, and at
rational a its value lies in Q(sqrt5). This is an explicit all-a lower
bound separating the two arrows.

At the Gamma boundary aX,aY→independent Gamma(2,1). The same mixture couples each scaled variable between aG/(a+5) and G, which justifies convergence of all displayed logarithmic moments. Define
V_G=lambda²G_1+lambda G_2. Direct partial fractions give

 E log V_G = -gamma+5+2sqrt5-[(19+7sqrt5)/2]log(phi).        (16)

For a derivation, the rates are A=phi² and B=phi and the Laplace transform is
(1+lambda²t)^(-2)(1+lambda t)^(-2). Its density is

 (9+4sqrt5)[2e^(-Ax)+x e^(-Ax)-2e^(-Bx)+x e^(-Bx)].

Integrate each log term using the Gamma integral. The total mass is one;
the x terms contribute5+2sqrt5; the coefficient of log(phi) is
(19+7sqrt5)/2. This proves (16) without numeric fitting. Fresh averaging's
corresponding boundary is log2. The strict limiting gap is

 log2+gamma-5-2sqrt5+[(19+7sqrt5)/2]log(phi)
     = 0.1358174619631668687...                              (17)

The displayed decimal is calibration; a rational interval is separately
certified. Gamma's explicit -gamma survives in the retained-memory absolute
anchor but disappears from fresh averaging's limiting log mean. Neither
behavior can be read off from the starting Omega scalar alone.

## FIC05: the source clock distinguishes the extrusion arrows

Let E_s denote normalized multiplication of a probability density by e^(-s x),
s>0. Directly from the source, E_s mu_a=mu_(a+s). This clock commutes with
fresh convolution:

    E_s(mu_a^(convolution k))=mu_(a+s)^(convolution k).       (18)

For a weighted retained-memory endpoint V=cX+dY, c,d>=0 not both zero,
endpoint tilting instead replaces the two input laws by mu_(a+sc) and
mu_(a+sd), independently (a zero-weight input is immaterial). There exists
**any** common source-age shift t>=0 giving the same endpoint law as
E_s V if and only if all the strictly positive weights equal one value w;
in that case the unique shift is t=sw. In particular, the same shift t=s
commutes exactly when each nonzero weight is1. Unequal Fibonacci memory
weights therefore cannot be repaired by a different scalar source clock.

**Proof of necessity, including possible accidental output coincidences.**
The original Q(x) tends to4, so the moment-generating function of mu_a is
finite exactly for real theta<a. Let w=max(c,d)>0. The mgf threshold of V
is a/w; the threshold after endpoint tilt is a/w+s. The threshold after
a common input-age shift t is (a+t)/w. Equality of endpoint laws forces
t=sw. The source mean m_u is strictly decreasing because m'_u=-v_u<0.
At this forced shift, the endpoint-tilted mean is
c m_(a+sc)+d m_(a+sd), whereas common-clock mean is (c+d)m_(a+sw).
Each nonzero term of the former is at least the corresponding term of the
latter; it is strictly larger for a positive weight below w. Thus unequal
positive weights are impossible. Sufficiency for equal weights follows by
factorization of the exponential tilt. This proves the entire classification,
not merely a mismatch of selected moments.

For Fibonacci weights c=F_(n-2),d=F_(n-1), n>=3, the same-clock mean defect
has the exact positive formula

 D_n(a,s)=F_n m_(a+s)-c m_(a+cs)-d m_(a+ds)
   =c integral_(a+s)^(a+cs) v_u du
       +d integral_(a+s)^(a+ds) v_u du.                    (19)

It vanishes at n3 and is strictly positive for n>=4. The mixture gives
v_u=E[2/(u+T)^2]+Var[2/(u+T)]>=2/(u+5)^2, so

 D_n(a,s)>=2c[1/(a+s+5)-1/(a+cs+5)]
            +2d[1/(a+s+5)-1/(a+ds+5)]>0, n>=4.           (20)

All terms in (19),(20) are rational for rational a,s. The first exact
witness is n4, c1,d2, a17,s3/7. A pure Gamma source also exhibits the
unequal-weight obstruction: this is a distinction between declared arrows,
not a certificate identifying the original four-pole source.

## Scope, controls and provenance

The prior Fibonacci information-clock paper already derives the matrix
spectrum, Lorentz mark, source KL jets and harmonic offset gamma-log5/2.
The prior Pascal sheet already has Fibonacci diagonals. Neither is counted
as new here. Parent FC07 gives the source-mixture proof and fixed-rank bound;
FIC01 is its explicit uniform-rank extension. Binet, Gamma integrals,
Dirichlet moments, reciprocal Fibonacci sums and basic probability tools are
classical; the displayed source-typed assembly and comparisons are proved
here, without a scholarly-priority claim.

The positive Gamma control, wrong bounded rate mixture, retained-memory
countermodel and original coherent changed arithmetic seed are mandatory
controls. All FIC statements are unchanged by that seed change. A signed
normality theorem therefore cannot follow from FIC01--05 alone. In particular,
the Fibonacci source correction is summable, not a positive-density phase
saving. A source-to-selected-phase coupling still has to be proved.

Primary formula context: [NIST DLMF5.4](https://dlmf.nist.gov/5.4),
[5.9](https://dlmf.nist.gov/5.9),[5.12](https://dlmf.nist.gov/5.12).
Classical reciprocal-sum literature includes
[Greig, Sums of Fibonacci Reciprocals, Fibonacci Quarterly15(1977)](https://www.fq.math.ca/Scanned/15-1/greig2.pdf).
Only convergence and the elementary bound(11), both proved here, are used.
No irrationality theorem about C_F is a premise. Source paths/commits are
pinned in SOURCE_MANIFEST.json. The shared-model separate oracle is
computationally distinct, not an independent external proof authority.
