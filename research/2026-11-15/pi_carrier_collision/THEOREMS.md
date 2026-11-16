# Source-coupled random collision frames and detection dose

## Scope, notation, and authority

Write e(t)=exp(2 pi i t), with t in turns. The authentic four-channel source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\qquad U_{n+1}=16U_n+r(n+1).
\]

The completed phase is U_n+T_n=16^(n-1) pi for n>=1, where
T_n=sum_(j>=1)16^(-j)r(n+j). Its continuous-character transport to U_n is
inherited from the signed Gamma--BBP Green dossier. The target remains
W_B(h)=B^(-1)sum_(B<=n<2B)e(hU_n)->0 for every fixed nonzero integer h.
The all-scale arithmetic assertion is OPEN.

These results concern explicitly defined mathematical probes, not particle
production, a physical quantum source, or a new force. The random probe
parameter is chosen externally and recorded; it is not inferred intrinsic
randomness of the deterministic BBP successor.

PC-01 credits inherited echo algebra. PC-02--06 are source-specific frame
specializations and their bounds. PC-07--08 are classical probability
identities and controls. PC-09 is a detection corollary of an inherited
arithmetic theorem, with its unextracted onset retained. PC-10 states the
remaining proof cut. Academic priority is not claimed for generic frame,
Gamma, concentration, conditioning, or amplification results.

## PC-01. Matched two-tap probes retain the target phase

**PROVED; inherited algebra, new declared probe use.** For any integer h,K,
every n>=0, and every real seed s in the same forced recurrence,

\[
(h-16K)U_n(s)+KU_{n+1}(s)=hU_n(s)+Kr(n+1).
\]

This is immediate substitution. More generally, polynomial division gives
A(z)=A(16)+(z-16)B(z) for every integer polynomial A. With E the forward
shift, A(E)U_n=A(16)U_n+B(E)r(n+1). This identity and its source/seed
boundaries already occur in BBP_ECHO_DELAY_TRANSPORT.md and its module.

Set t_n=r(n+1), c_n=e(hU_n), and define the coherent block response

\[
F_{B,h}(K)=\frac1B\sum_{n=B}^{2B-1}c_n e(Kt_n).
\tag{1}
\]

Every summand is an exact integer two-tap character of the actual lifted
recurrence. K changes a known source modulation while h stays fixed.
At h=0 the phase target and seed are erased. For any h, removing e(Kt_n)
samplewise returns e(hU_n). This is a source-preserving readout identity,
not a bound on the mean of the returned phases.

Computing (1) directly requires access to the original B phase values.
No cheaper collective instrument, physical interference apparatus, or
quantum computational advantage is supplied by writing the coherent sum.

## PC-02. Source spacing fixes a cubic resolution scale

**PROVED for the original four channels.** For n>=0,

\[
t_n=\int_0^1x^{8n}(1-x)A(x)\,dx,\qquad
A(x)=x^4+2x^3+4x^2+4x+4.
\]

The numerator identity is (1-x)A(x)=4-2x^3-x^4-x^5. On [0,1],
15x^4<=A(x)<=15 and
8x^7<=(1-x^8)/(1-x)<=8, with the quotient continuously extended at 1.
Therefore

\[
\frac{240}{(8n+12)(8n+13)(8n+14)}
\le t_n-t_{n+1}
\le\frac{240}{(8n+1)(8n+2)(8n+3)}.
\tag{2}
\]

Indeed, the difference integral contains (1-x)^2 A(x)(1+...+x^7);
bound its polynomial factor between 120x^11 and 120 and use
integral x^m(1-x)^2 dx=2/[(m+1)(m+2)(m+3)].
The integral also shows each difference is positive and decreases with n.

For B>=2, the minimum adjacent spacing among n=B,...,2B-1 is
delta_B=t_(2B-2)-t_(2B-1), and

\[
\delta_B\ge d_B:=
\frac{240}{(16B-4)(16B-3)(16B-2)},\qquad
|t_n-t_m|\ge d_B|n-m|.
\tag{3}
\]

Moreover t_B<=15/[(8B+1)(8B+2)]<=1/6. These differences are their
circle distances: no wrap is hidden. The matching upper/lower bounds show

\[
t_n\sim\frac{15}{64n^2},\qquad
\delta_B\sim\frac{15}{256B^3}.
\tag{4}
\]

The first limit follows from the same integral with
15x^4<=A<=15. Thus a B^2 source modulation can be macroscopically visible,
while adjacent clock separation has a B^3 scale. The B^2/B^3 source and
step scales themselves are inherited IMW results; the frame use below
supplies a quantitative reconstruction interpretation.

## PC-03. Gamma--Poisson and finite triangular probe frames

For a probability law on integer K, use the column
v_K=(e(-Kt_n))_(n=B)^(2B-1), so F(K)=v_K^*c/B, and set
G=E[v_K v_K^*]. This fixes the complex-conjugation convention:
G_nm=E[e(K(t_m-t_n))].

### Gamma--Poisson choice

**PROVED.** Choose an external T~Gamma(shape 2, scale Lambda), Lambda>0,
and K conditional on T~Poisson(T). Then

\[
\Pr(K=k)=\frac{(k+1)\Lambda^k}{(1+\Lambda)^{k+2}},
\quad
\mathbb E e(Ku)=[1+\Lambda(1-e(u))]^{-2}.
\tag{5}
\]

The Gamma integral proves the probability generating function; this
classical identity and its causal-count interpretation are inherited.
Here it specifies a new probe policy. It does not identify the original
Oily grade/source joint law with an auxiliary Gamma--Poisson coupling.

Since

\[
|1+\Lambda(1-e(u))|^2
=1+4\Lambda(1+\Lambda)\sin^2(\pi u),
\]

and sin(pi u)>=2u for 0<=u<=1/2, (3) gives, n!=m,

\[
|G_{nm}|\le
\frac1{1+16\Lambda(1+\Lambda)d_B^2|n-m|^2}.
\]

Both sides of a row contribute at most twice the positive-index sum.
Using sum_(l>=1)l^(-2)<2, every off-diagonal row sum is strictly below

\[
\eta_\Gamma=\frac1{4\Lambda(1+\Lambda)d_B^2}.
\tag{6}
\]

G is Hermitian with diagonal 1; the row-sum norm bound proves

\[
(1-\eta_\Gamma)I\le G\le(1+\eta_\Gamma)I.
\tag{7}
\]

The choice Lambda=ceil(1/d_B) has eta_Gamma<=1/4 and mean K=2 Lambda.
This is an O(B^3) intensity law. Its unbounded support has exact tail
Pr(K>M)=q^(M+1)[1+(M+1)p], with p=1/(1+Lambda), q=1-p.
Finite truncation or rejection changes the law and must be charged.

### Bounded triangular choice

Choose independent U,V uniform on {0,...,M-1}, and K=1+U+V. Thus every
probe has 1<=K<=2M-1, and its law is triangular. A fixed integer shift
of this law only unitarily conjugates G and does not improve its spectrum.
The character modulus is

\[
\left|\mathbb E e(Ku)\right|
=\left|\frac{\sin(\pi Mu)}{M\sin(\pi u)}\right|^2.
\]

Consequently the off-diagonal row sum is strictly below
eta_F=1/(M^2 d_B^2). Taking M=ceil(2/d_B) gives eta_F<=1/4.
This is a fully bounded positive integer probe law with the same cubic
resolution scale. It is a separate law, not a truncation of (5).

## PC-04. A finite random design succeeds with calibrated probability

**PROVED using the cited matrix Chernoff theorem.** Let either population
frame above satisfy (1-eta)I<=G<=(1+eta)I, 0<=eta<1. Draw s independent
K values from that same law. Repeated equal values may occur by chance;
copying one draw s times is a different, inadmissible dependence model.
Put Ghat=s^(-1)sum_j v_(K_j)v_(K_j)^*.

For 0<epsilon<1,

\[
\Pr\{(1-\epsilon)G\not\le\widehat G
       \text{ or }\widehat G\not\le(1+\epsilon)G\}
\le 2B\exp\!\left[-\frac{s\epsilon^2(1-\eta)}{3B}\right].
\tag{8}
\]

Proof: whiten each row, X=G^(-1/2)vv^*G^(-1/2). Then EX=I and
0<=X<=(B/(1-eta))I because ||v||^2=B. Apply Tropp's matrix Chernoff
Corollary 5.2 to sum X. The scalar exponent bounds are
(1-epsilon)log(1-epsilon)+epsilon>=epsilon^2/2 and
(1+epsilon)log(1+epsilon)-epsilon>=epsilon^2/3 on [0,1].
A union bound and conjugation by G^(1/2) give (8).
Independence is between rows; coordinates inside a row are strongly
dependent functions of the same K, as the theorem permits.

For 0<delta<1, s>=3B log(2B/delta)/[(1-eta)epsilon^2] suffices for failure at
most delta. The exact implementation replaces the natural logarithm by
the least integer L with 2^L>=2B/delta, then takes the ceiling of
3BL/[(1-eta)epsilon^2]. Since exp(-L)<=2^(-L), its rational budget is
conservative without using a floating-point logarithm.

For eta<=1/4 and epsilon=1/2 the successful empirical Gram obeys

\[
\frac38 I\le\widehat G\le\frac{15}{8}I.
\tag{9}
\]

Its condition number is at most 5; the measurement matrix condition
number is at most sqrt(5). The sufficient count is O(B log(B/delta)).
This is a sufficient sampling bound, not an optimal lower bound.

### A coherent all-scale probability-one statement

At each B>=2 use the recommended population frame with eta<=1/4,
epsilon=1/2, and delta_B=1/[B(B+1)] in (8). For every B0>=2,

\[
\Pr(\text{every frame at every }B\ge B_0\text{ satisfies (9)})
\ge 1-\sum_{B\ge B_0}\frac1{B(B+1)}
=1-\frac1{B_0}.
\tag{10}
\]

Therefore almost surely only finitely many frame designs fail. No
independence between different B is required for this union-bound
argument. Within each B the stipulated independent draws are required.
The event is uniform over all vectors c, hence over every source phase
vector and Fourier target h using these nodes. This probability-one
result concerns eventual detector conditioning, not normality of pi.

## PC-05. Frequency spread, not a large central frequency, pays resolution

**PROVED lower bound for uniform full-vector linear reconstruction.**
Let K have finite variance V and let delta_B be the closest source-node
spacing. The corresponding two-column principal Gram has eigenvalues
1+|m(delta_B)| and 1-|m(delta_B)|, where m(u)=E e(Ku).
After multiplying by e(-E[K]u),

\[
1-|m(u)|
\le1-\Re\mathbb E e((K-\mathbb EK)u)
\le2\pi^2u^2V.
\]

The last inequality is 1-cos x<=x^2/2. A vector supported on those two
columns gives

\[
\lambda_{\min}(G)\le2\pi^2\delta_B^2 V.
\tag{11}
\]

Hence V=o(B^6) prevents a uniform positive lower frame bound as B grows.
For Gamma--Poisson shape 2, V=2Lambda(1+Lambda); for the triangular
law, V=(M^2-1)/6. A fixed or diverging frequency offset has no effect.
These statements concern the declared unrestricted coefficient-vector
inverse. They are not computational lower bounds for pi, for a special
one-dimensional nonlinear source family, or for estimating only its mean.

## PC-06. Stable recovery, Haar transport, and universal detector energy

**PROVED.** Assume (7) with 0<=eta<1. For every c with |c_n|=1,

\[
\frac{1-\eta}{B}\le\mathbb E|F(K)|^2
=\frac{c^*Gc}{B^2}\le\frac{1+\eta}{B}.
\tag{12}
\]

This holds equally for the authentic phase vector and the locked vector
c=(1,...,1). Thus small total detector energy is universal at high
resolution; it cannot certify cancellation of the original mean.
Keeping the labelled complex outputs gives exact recovery:

\[
c=B G^{-1}\mathbb E[v_K F(K)].
\tag{13}
\]

For a successful finite design replace G and the expectation by Ghat
and the sample mean. This identity retains phases between channels;
replacing the outputs by their magnitudes does not implement (13).

Let a_j^*=v_(K_j)^*, A have rows a_j^*/sqrt(s), and suppose reported
normalized echoes have errors e_j. Define y_j=[F(K_j)+e_j]/sqrt(s),
and recover c_hat=B A^dagger y. With l=lambda_min(Ghat)>0,
least-squares recovery satisfies

\[
\|\Delta c\|_2\le\frac{B}{\sqrt l}
 \left(\frac1s\sum_j|e_j|^2\right)^{1/2},\qquad
|\Delta W_B(h)|\le\sqrt{\frac B l}
 \left(\frac1s\sum_j|e_j|^2\right)^{1/2}.
\tag{14}
\]

Proof: the response vector divided by sqrt(s) is Ac/B,
and ||A^dagger||<=1/sqrt(l).
For the mean apply the norm of the constant vector sqrt(B).
The dimension factors are essential. Conditioning alone gives no fixed
absolute error budget for normalized aggregate readouts as B grows.

For any unitary clock-Haar transform H, put d=Hc and A_H=AH^*.
Its Gram is H Ghat H^*, so the same frame bounds hold. If the first
Haar row is B^(-1/2)(1,...,1), then

\[
d_0=\sqrt B\,W_B(h),\qquad
\sum_{j\ge1}|d_j|^2=B(1-|W_B(h)|^2).
\tag{15}
\]

These Haar coordinates resolve the temporal phase vector, distinct from
the source-coordinate x Haar expansion in #641. The frame is an explicit
finite bridge because its inputs are now the actual recurrence phases.
It still does not force energy out of the constant coefficient.
The oriented escape statistic is separately

\[
\frac1B\sum_n(1-\Re c_n)=\frac{\|c-\mathbf1\|_2^2}{2B}.
\]

There is consequently an exact calibrated detector for this narrower
target. Keep the complex difference from the locked reference,
D_B=E|F_c(K)-F_(mathbf1)(K)|^2. Then

\[
\frac{B D_B}{2(1+\eta)}
\le A_B:=\frac1B\sum_n(1-\Re c_n)
\le\frac{B D_B}{2(1-\eta)}.
\tag{15a}
\]

This follows by applying (7) to c-1. It preserves the interference cross
term. A difference of the two separate energies does not equal D_B;
for example globally rotating c multiplies F_c by the same phase and
leaves its raw energy unchanged. For a family with a uniform
eta<=eta_*<1, at h=1 a uniform positive lower bound
on B D_B is equivalent to R0 within these stable constants; obtaining
that source-specific lower bound is still
the arithmetic task. Equation (15a) is a calibrated equivalent target,
not a new source estimate.

For source-node errors |Delta t_n|<=epsilon_t, each character incurs
error at most 2pi|K|epsilon_t. For independently bounded two-tap state
errors epsilon_n,epsilon_(n+1), the bound is
2pi[(|h|+16|K|)epsilon_n+|K|epsilon_(n+1)].
Exact rational reduction of the phase before numerical evaluation avoids
one floating-point amplification; it does not make a physical sensor exact.

## PC-07. A forgotten Gamma clock can manufacture cancellation

**PROVED classical control, with declared independent clocks.** Let z_n
be arbitrary deterministic unit phases, and tau_n independently follow
Gamma(shape alpha, rate lambda), alpha,lambda>0. For real angular
frequency omega, report Y_n=z_n exp(i omega tau_n). Then

\[
m=\mathbb E e^{i\omega\tau}
=\left(\frac{\lambda}{\lambda-i\omega}\right)^\alpha,\qquad
|m|=(1+(\omega/\lambda)^2)^{-\alpha/2}.
\]

The power uses the continuous Gamma-integral branch. Thus forgetting
the clocks scales the mean by m. Even z_n=1 has an arbitrarily small
mean as |omega| grows. All its nonzero integer phase harmonics vanish
in that limit, giving a uniform limiting rotated output law.

Retaining tau gives exact samplewise demodulation exp(-i omega tau)Y=z.
For forgotten clocks the unbiased estimator Zhat=(Nm)^(-1)sum Y_n
has exact mean-square error

\[
\mathbb E|\widehat Z-N^{-1}\sum z_n|^2
=\frac{|m|^{-2}-1}{N}.
\tag{16}
\]

This follows by independence and summing the N individual variances
1-|m|^2. If a retained clock has error at most epsilon_T, its phase
demodulation error is at most min(2,|omega|epsilon_T).
The exact code supports integer alpha and rational omega,lambda.

This convention uses a positive phase exp(i omega T); donor #640 uses
the opposite sign for one off-diagonal density-matrix entry. The two
multipliers are conjugates. Both quadratures and the declared orientation
must be retained. #640's alpha=2, omega=lambda example has a nonzero
imaginary coherence even though its real quadrature vanishes.

An all-tests lower bound also exists on a declared statistical class.
Take densities with respect to normalized circle Haar measure dtheta/(2pi)
and a nonzero integer h. Input densities 1+/-epsilon cos(h theta),
0<epsilon<=1/2, have
TV distance 2epsilon/pi. After independent clock convolution their TV
distance is multiplied by r=|m(h omega)|. The one-sample chi-square
divergence is at most 4epsilon^2 r^2 because its denominator is >=1/2.
For N independent samples, chi-square is at most exp(4N epsilon^2r^2)-1.
TV<=sqrt(chi-square)/2 implies that equal-prior testing error <=1/4
requires N>=log(2)/(4epsilon^2r^2). This is not a computational lower
bound for the already authenticated BBP source.

## PC-08. Detection probability carries an event-rate obligation

**PROVED.** On a finite block let A be the mean of
1-cos(2pi hU_n). Independently draw an index uniformly, then accept with
probability [1-cos(2pi hU_n)]/2. Each trial has success probability p=A/2.
For M fresh independent trials,

\[
\Pr(\text{at least one hit})=1-(1-A/2)^M.
\tag{17}
\]

For an integer M>=1 and 0<delta<1, this is >=1-delta exactly when
A>=2(1-delta^(1/M)). Thus growing M can compensate a vanishing event
rate; probability tending to one is not a uniform positive lower bound
on A. Replaying one realized trial does not obey (17).

The same-forcing counterseed s=-pi/16 has U_n(s)=-T_n. Equation (4),
the summable Green weights, and dominated convergence give
T_n~1/(64n^2). For h=1 and the dyadic block [B,2B),

\[
p_B=\frac1{2B}\sum_{n=B}^{2B-1}(1-\cos(2\pi T_n))
\sim\frac{7\pi^2}{98304}B^{-4}.
\tag{18}
\]

Indeed 1-cos(2pi T)~2pi^2T^2, and
B^3 sum_(B<=n<2B)n^(-4)->integral_1^2 x^(-4)dx=7/24.
For any fixed target confidence, the required dose is asymptotic to
[-log(delta)]/p_B, of order B^4. This control can have high detection
confidence while its completed orbit is identically zero.
It changes the seed and does not refute a zero-seeded theorem.

The exact implementation encloses the finite counterseed escape using
inherited rational T intervals and rational small-angle bounds. The
asymptotic constant above has a separate written proof.

If indices instead have known positive propensities q_n, the unbiased
uniform-block observable is f(n)/(Bq_n), not f(n). Its second moment is
B^(-2)sum |f(n)|^2/q_n. This states the cost of adaptive concentration
on favorable observations; zero propensities generally prevent recovery.

## PC-09. An actual zero-seeded detector can be amplified

**PROVED COROLLARY OF INHERITED ARITHMETIC, with unextracted onset.**
GLOBAL_BRANCH_COERCIVITY.md GB-12 proves that there exists m_2>=4096
such that, for m>=m_2 and integers 1<=|h|<=m^2/64,

\[
\left|\sum_{n=m+1}^{8m}e(hU_n)\right|<7m-\frac1{14}.
\tag{19}
\]

Its proof uses the exact zero-selected Green identity and the classical
irrationality-measure bound mu(pi)<15/2; it computes no numerical m_2.
This dossier does not improve (19).

For a uniform index in that 7m-point block, the phase-sensitive acceptance
rule in PC-08 has

\[
p_m=\frac1{14m}\sum_{n=m+1}^{8m}(1-\cos(2\pi hU_n))
>\frac1{196m}.
\]

The inequality follows from Re sum<=|sum|. Thus for 0<delta<1,
M=ceil(196m log(1/delta)) fresh trials give success >1-delta.
For the same-forcing counterseed, T_n<1/(64n^2) yields

\[
p_m^{\rm counter}\le
\frac{\pi^2 h^2}{4096(m+1)^4},\qquad
\Pr(\text{counterseed hit})\le M p_m^{\rm counter}.
\tag{20}
\]

For each fixed h!=0, choosing delta=1/m gives authentic success
>=1-1/m and counterseed false-hit O_h(log(m)/m^3). This is an honest
source-sensitive separation with a growing dose and an unextracted
onset. It does not distinguish the source from all nonnormal sequences.
In particular, the source success uses order m log m trials rather
than a scale-independent lower event rate.

The phase coin is a specified mathematical instrument. Implementing it
requires exact or certified phase access and accounted errors; its
existence supplies no free physical measurement or computation.

## PC-10. Remaining signed arithmetic cut

**OPEN.** A detector that uniformly controls the authentic oriented
escape A_B away from zero at all large B would establish R0. The
all-mode mean cancellation W_B(h)->0 would establish base-16 normality.
PC-03--06 prove stable access to the full phase vector under declared
probe laws; PC-09 proves a weaker, scale-expensive separation. None
supplies either missing uniform arithmetic estimate.

Candidate improvements must preserve the original four channels, zero
seed, signed target, randomization labels, and reconstruction error.
If the uniform mean itself is rewritten using (13), the resulting
criterion is an equivalent reformulation until an independently proved
bound on that signed dual functional is supplied. Small detector energy,
small forgotten-clock mean, or a high success probability with an
unbounded dose cannot substitute for it.

The mathematical probability-one statement earned here is (10):
eventual faithfulness of an explicitly constructed family of detectors.
It does not change the deterministic arithmetic target's truth.
