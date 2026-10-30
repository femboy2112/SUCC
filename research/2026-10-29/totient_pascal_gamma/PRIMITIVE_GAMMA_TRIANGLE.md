# Primitive Totient Selection of the Authentic Pascal–Gamma–Golden Triangle

Research date: 2026-10-29. Research-only child of SUCC draft PR #370 at exact head 4d4d49b575b476cc33f762d2b6a7fd6d1b924655 (ancestry #369/#367). No change to the original four signed BBP poles, U_0=0, historical claim registry, original archives, or main. Pi normality and RH are OPEN. None of these models asserts a physical stochastic generation of pi digits.

## 1. Exact source-typed finite input

Use Q(x)=4-2exp(-3x)-exp(-4x)-exp(-5x)>0 and R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5), with a=8n-7, r(n)=R(a), and the positive authentic carrier mu_a(dx)=exp(-ax)Q(x)dx/R(a).

The *declared Pascal sensor* from PR #370 conditionally draws J_n~Binomial(n,1-exp(-8X_n)) for X_n~mu_a. Define Z_n=2aX_n. Exact rational finite grade probabilities are

q_n(j)=binom(n,j) [sum_{k=0}^j (-1)^k binom(j,k)r(2n-j+k)] / r(n).

More fundamentally, its exact TWO-VARIABLE transform is

L_n(z,t)=E[z^(J_n)exp(-tZ_n)]
= [sum_{k=0}^n binom(n,k) z^(n-k)(1-z)^k R(a+2at+8k)] / R(a).

For rational z and t>=0 this is a rational identity of the original four-pole source. Conditioning on X, expanding the binomial, then applying its exact Laplace transform proves it.

## 2. Pascal--Poisson--Gamma joint law: the rank is *derived*

Since Q(x)=15x-59x^2/2+O(x^3), Y_n=aX_n converges to Gamma(2,1). Given X_n, the n-trial count converges conditionally to Poisson(Y). The **joint** transform tends to

L(z,t)=1/(2-z+2t)^2.

Thus P(J=j,Y in dy)=y^(j+1)exp(-2y)dy/j!, and after setting Z=2Y:

P(J=j)=(j+1)/2^(j+2),   Z | J=j ~ Gamma(j+2,1).

Therefore the harmonic/Gamma rank j+2 is not assigned by hand. The limit has Cov(J,Z)=4. The *older original Oily packet joint law* shares the grade marginal but has limiting independence between its grade and Gamma boundary, and hence has cross-covariance zero. **Do not conflate these joints.**

## 3. Möbius primitive selector on the triangular ranks

For integer q>=1 let chi_q(j)=1 if gcd(j,q)=1 and zero otherwise. The exact arithmetic identity is chi_q(j)=sum_{d|gcd(j,q)}mu_arith(d).

Define C_q(z)=sum_{j>=0}chi_q(j)(j+1)z^j/2^(j+2). Inherited Oily-totient results yield

C_q(z)=(1/4) sum_{d|q} mu_arith(d)
 [1+(d-1)(z/2)^d]/[1-(z/2)^d]^2.

The new nonfactorizing *joint primitive transform* is

K_q(z,t)=E[chi_q(J) z^J exp(-tZ)]
=(1+t)^(-2) C_q(z/(1+t)).

The masses m_q=C_q(1) are source-weighted primitive probabilities, not the ordinary Euler totient fraction phi(q)/q. Examples:
m_2=m_4=m_16=4/9, m_3=29/49, m_6=416/1323.

## 4. Harmonic / inverse-golden / Euler--Mascheroni is now an observable

Let lambda=(sqrt(5)-1)/2. Since (1+lambda)^(-1)=lambda, for Gamma(r,1)

D(r)=E[log Z-exp(-lambda Z)]=psi(r)-lambda^r
=H_(r-1)-gamma-lambda^r  (integer r>=1).

At r=2 this is lambda-gamma, the original named Oily--Macaroni constant. Totient selects **ranks** through J:

D_q=E[log Z-exp(-lambda Z) | gcd(J,q)=1]
=[sum_{j>=0}chi_q(j)(j+1)2^(-j-2)(H_(j+1)-gamma-lambda^(j+2))] / m_q.

A useful all-q integral formula is

D_q = [1/m_q] int_0^1 [m_q-u C_q(u)]/(1-u)du
      -gamma-lambda^2 C_q(lambda)/m_q.

For q=2, the primitive grades are odd and the conditional density of Y is
(9/8)y[exp(-y)-exp(-3y)]. Consequently:

D_2=1+log 2+(log 3)/8-gamma-9lambda^3/(4-lambda^2)^2
   =1.09095215299287252639384... .

This is a source-marked mathematical selection from the triangle, not an assumption about the actual deterministic digit orbit.

**Noncommuting operations control:** the unconditioned Oily PGF G(z)=(2-z)^(-2) has the interior fixed point lambda^2. For every q>1, the normalized primitive PGF C_q(z)/m_q has no interior fixed point on (0,1), because its support is in j>=1 with positive weight for j>1; it is strictly below z on (0,1). The golden marker must be fixed from the original unconditioned source BEFORE primitive conditioning. A claim that the primitive grade PGF separately forces lambda is refuted.

## 5. Full 2x3 factorial interaction

With A=chi_2(J), B=chi_3(J), and F=log Z-exp(-lambda Z), the complete four conditional cells (not merely marginal estimates) are:

A B    P(A,B)                E[F | A,B]
0 0    0.278155706727135     0.240358723462685
0 1    0.277399848828420     1.312930569542242
1 0    0.130007558578987     1.452243500342295
1 1    0.314436885865457     0.941572076684938

The conditional factorial contrast E[F|11]-E[F|10]-E[F|01]+E[F|00] is approximately -1.5832432697369138845. For cutoff M=150, the omitted unnormalized first moment is bounded by (M^2+5M+8)/2^(M+1)<9e-42. The high-precision decimals are observations, not rigorous rounding intervals. This is a nonadditive classical conditional response, not evidence of physical gluons.

Inherited original-Oily packet source produces a different primitive log-shadow coefficient H_q=2C_q(1)-C'_q(1): H_2=-4/27, H_6=352/27783>0, a genuine sign change. Do not promote it to a signed pi-phase estimate.

## 6. Exact first *authentic-source* correction

Write a=8n-7, m_n=P(J_n odd), and D_n=E[log(2aX_n)-exp(-2lambda aX_n) | J_n odd]. The original Q''(0)=-59 enters through c=59/30.

m_n=4/9+(271/405)/a+O(a^-2).

D_n=D_2+C_BBP/a+o(a^-1), where the exact coefficient is

C_BBP=-1095871/150+(3266527/1000)sqrt(5)-(271/160)log 3
     =-3.49101889214273981409853... .

For a direct proof, put y=aX and F(y)=log(2y)-exp(-2lambda y).
The source density is y exp(-y)[1-c(y-2)/a+O(a^-2 polynomial(y))], while the odd-grade likelihood is
W_0(y)+W_1(y)/a+O(a^-2 polynomial(y)),
W_0=(1-exp(-2y))/2,
W_1=exp(-2y)(7y+4y^2).
The expansions may be integrated with exponentially dominated remainders after splitting off large y. Let
I_k(v)=k!v^(-k-1)[H_k-gamma+log2-log v]-k!/(v+2lambda)^(k+1).
Then T_0=[I_1(1)-I_1(3)]/2, and
T_1=7I_2(3)+4I_3(3)-(c/2)[I_2(1)-2I_1(1)-I_2(3)+2I_1(3)].
With m_0=4/9, m_1=(22-2c)/27=271/405,
C_BBP=(T_1-m_1D_2)/m_0.
This simplifies to the displayed closed expression.

Hostile positive mutant Q_mut(x)=15x has the SAME leading Gamma(2)/Oily law, but c=0 and first correction approximately -1.4115435740708651424834. Thus the finite correction contains genuine four-pole information. This is a positive-source fingerprint, not a signed Weyl saving.

## 7. Signed phase / literal carry interface, with no-go

For the original zero-seeded U_n, define z_m(h)=exp(2pi i h U_m(0)). The finite primitive readout is K_(n,q,h)=sum_(j=0)^n q_n(j)chi_q(j)z_(n+j)(h). This retains the selected phase, including the exact lag forcing:

U_(n+j)(s)=16^j U_n(s)+sum_(k=1)^j 16^(j-k)r(n+k) (mod 1).

For a **source-absolute** carry probe, retain literal integer
kappa_m(s)=floor(16{U_(m-1)(s)}+r(m)), and the 16-class (or full integer-carry) tensor
T_(n,q,h,c;s)=sum_j q_n(j)chi_q(j)1_{kappa_(n+j)(s)=c}z_(n+j)(h;s).
Summing c recovers K. This is an exact source-labelled finite instrument, not a theorem about carry frequencies.

For q=2, the limiting unnormalized grade filter C_2(S)=4S/(4-S^2)^2 satisfies
(16-8S^2+S^4)C_2(S)z=4Sz.
The inherited PR #370 TV(q_n,w)<=22/n gives the uniform finite version
|16K_n-8K_(n+2)+K_(n+4)-4z_(n+1)|<=1100/n, n>=3.

More sharply, for L>=3 and N>=1, any bounded |z_n|<=1 obeys
|N^-1 sum_(n=L)^(L+N-1)K_n -(4/9)N^-1 sum z_n|
<=56/(27N)+(44/N)sum_(n=L)^(L+N-1)1/n.

Thus primitive-grade filtering alone is a *stable reformulation* of the selected Weyl mean, never an independent proof of cancellation. The coherent same-forcing seed s=-pi/16 has U_n(s)=-T_n->0, so z_n(s)->1 and the primitive readout tends to 4/9; all positive-source and selected-rank identities still hold. Even a nonzero four-cell interaction and source-specific first jet do not overcome this counterexample.

## 8. Next precise proof obligation

Derive a noncircular, zero-seed-sensitive SIGNED bias on the *complete literal-carry-resolved primitive tensor* for q in {2,3,5,6,10,15,30}, preserving every Walsh/Pascal fourth-order interaction and the original four-pole rational forcing. Attack conditional carry laws rather than assuming Haar mixing. Ablate U_0=0 against 15-torsion shifts and the coherent s=-pi/16 seed; preserve wrong-pole and Gamma-matched mutant controls. An all-N theorem must beat the trivial O(1) normalized Weyl bound and survive fresh hostile holdouts. Nothing herein proves base-16 normality of pi or RH.

## 9. Validation / provenance

A locally executed standalone exact-Fraction research suite passed 13/13 tests, including the original-four-pole finite joint source, q=2/3/6/16 Möbius projection, absolute-literal-carry tensor, and changed-seed lag controls. A separate SymPy/mpmath 48-digit oracle checked finite n=25/100/250 for the original source and Q_mut, the selected first correction, complete 2x3 cells, and analytic omitted-tail budget. **These uploaded remote research paragraphs are reauthored from the verified local files; no byte-identical GitHub-head tests, Lean, full native SUCC suite, or hosted CI have been run.**

Primary classical identities: NIST DLMF 5.4.E14 (digamma / harmonics), 5.2.E1 (Gamma integral), 27.5.E3 (Möbius inversion). SUCC inherited sources: research/2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md; research/2026-10-24/PASCAL_CARRY_INTERFEROMETRY.md; draft #370 Pascal-source lift. Full local source/receipts are provided separately as an exact tested research bundle.