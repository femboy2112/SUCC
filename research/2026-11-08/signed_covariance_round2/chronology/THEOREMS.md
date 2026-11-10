# Authenticated prime-history laws and the chronological boundary

Status: **PROVED PAPER relative to PE1--PE9 and its declared classical BK/PNT
inputs**. Finite exact tests are separate. This note supplies a new local
source/history theorem within the inspected SUCC frontier, not full real Weyl
cancellation or a worldwide novelty claim. Literal U0=0, all four signed poles,
unwrapped rational states and chronological pole births are unchanged.

Write e(x)=exp(2 pi i x). Fix p=1 mod8, g=16 modp, m=ord_p(16),
L=(p-1)/4, n0=L+1, n_p=(p+7)/8 and I={n0,...,2L}. The authentic source has

    x_n=[U_n(0)]_p=(4 g^(n-n_p) modp)/p

for n_p<=n<=2L. Its next p-pole is at 2L+1. Let xi=4g^(n0-n_p) modp.
Define the *periodic extension* x~_(n0+r)=(xi g^r modp)/p for every integer r.
This extension is a comparison object, equal to actual x_n only on the clean
lifetime. In particular, it is not silently substituted past the next birth.

For p=p_A selected by PE, m>p^(1/3) and the inherited classical
Bourgain--Konyagin input gives

    |m^-1 sum_(r modm) e(c g^r/p)| <= delta_p=p^(-gamma)

for every c !=0 modp, with gamma>0 independent of p and c. No numerical gamma
is supplied. All finite algebra below also holds for split primes of small
order; the asymptotic consequence uses the selected good primes only.

## CH1. Complete lag-moment classification: the missing resonance charge

For any integer lags t_1,...,t_d>=0 and integers h_1,...,h_d, define

    H(h,t)=sum_j h_j 16^(t_j).

There is the exact identity

    E_(n in I) e(sum_j h_j x~_(n+t_j))
      = m^-1 sum_(r modm) e(xi H(h,t) g^r/p).                 (CH1)

Thus the left side equals 1 if p divides H, and has modulus <=delta_p
otherwise. This applies to all lags and coefficients simultaneously.

**Proof.** On the circle x~_(n+t)=16^t x~_n; replacing each phase by its
canonical representative changes h_j times it only by an integer. Sum and
use that I comprises L/m complete periods. The coefficient vanishes exactly
when p|H, since xi is nonzero modp. Apply BK only in the remaining case.

Let T(x)={16x}. The Haar trajectory law is the pushforward of Lebesgue measure
under x -> (T^(t_1)x,...,T^(t_d)x). Its same Fourier moment is

    integral_0^1 e(H(h,t)x) dx = 1_(H(h,t)=0).               (CH2)

Consequently the finite clock's history law differs in that moment by at
most delta_p unless H is a **nonzero multiple of p**. In that alias case the
difference is exactly 1. A sufficient uniform alias-free condition is

    sum_j |h_j|16^(t_j) < p.

This includes every fixed lag/coefficient family for all sufficiently large
p. It is essential to distinguish the integer resonance H=0 from modular
aliasing H=kp !=0. The vector (-16,1) at lags (0,1) has H=0 and moment 1
at every p. The vector (p,0) has nonzero integer H and also moment 1, whereas
its Haar trajectory moment is 0. Independent uniform circle coordinates are
therefore the wrong limiting law.

For fixed d and lags, CH1--2 imply weak convergence of the local history law
to the Haar T-trajectory law: finite trigonometric polynomials approximate
continuous functions uniformly on the finite torus, and each of their finitely
many Fourier moments converges. This is deterministic averaging over the
selected authentic source's time indices. It is not randomization of the
BBP seed, nor does it identify the full real trajectory with this local law.

## CH2. Nonlinear causal observers: retain all source-resonant characters

Let a declared history observer be represented by an absolutely convergent
Fourier series

    F(z_1,...,z_d)=sum_(h in Z^d) c_h e(sum_j h_j z_j),
    K=sum_h |c_h| < infinity.

The coefficients and lags may be selected using prior history; the following
bound is pointwise and uniform, so no probabilistic independence assumption is
needed. Split the indices into integer resonances H=0, nonzero modular aliases
0!=H in pZ, and nonresonances p not dividing H. Then

    |E_I F(x~_(n+t_1),...,x~_(n+t_d))
          - integral_0^1 F(T^(t_1)x,...,T^(t_d)x) dx|
    <= sum_(0!=H in pZ)|c_h| + delta_p sum_(p not dividing H)|c_h|. (CH3)

**Proof.** Absolute convergence permits termwise finite averages and integrals.
Integer resonances cancel exactly between the two laws. Each modular alias
has difference exactly 1, and each remaining difference is bounded by BK.
Apply the triangle inequality to the coefficients only after this exact split.

For an alias-free finite observer menu with total variation K_A, the comparison
error is <=delta_(p_A) K_A. A bounded-memory observer does not automatically
have a small K_A, and arbitrary learned functions may have aliases. For
example F(z)=e(pz) has K=1 and discrepancy 1. This is a real sensor-bandwidth
cost, not a physical nonlocality theorem. This estimate compares **local
history laws**; it does not control the cross-covariance with the original
complement b_n=e(h(U_n-[U_n]_p)).

## CH3. An elementary, quantitative hexadecimal cylinder theorem

Let mu_p=m^-1 sum_(r modm) delta_((xi g^r modp)/p). Define

    D_p = 1/p + delta_p H_((p-1)/2),
    H_k=sum_(j=1)^k 1/j <= 1+log k.

For every half-open interval [a,b) subset [0,1),

    |mu_p([a,b))-(b-a)| <= D_p.                             (CH4)

**Proof with the finite-field Fourier normalization exposed.** Let J be the
consecutive integer residues k in {0,...,p-1} with a<=k/p<b; let N=|J|.
Its normalized discrete Fourier coefficients satisfy

    fhat(h)=p^-1 sum_(k in J) e(-hk/p),
    |fhat(h)| <= 1/[p |sin(pi h/p)|]
                  <= 1/[2 min(h,p-h)]   (h !=0 modp).

The first inequality follows from the finite geometric sum and |sin|<=1 in
the numerator; the second uses sin(pi u)>=2u on 0<=u<=1/2. Since p is odd,

    sum_(h=1)^(p-1)|fhat(h)| <= H_((p-1)/2).

Fourier inversion gives mu_p(J/p)=N/p+sum_(h!=0)fhat(h) E_mu e(hx).
The nonzero moments have modulus <=delta_p. Finally
|N/p-(b-a)|<=1/p by counting a half-open arithmetic progression. This proves
CH4 without importing a discrepancy theorem or an unstated constant.

A d-digit hexadecimal word w in {0,...,16^d-1} is obtained by observing
floor(16x), floor(16Tx),...,floor(16T^(d-1)x). The exact concatenated word is
floor(16^d x). Its cylinder is [w/16^d,(w+1)/16^d). Therefore, writing
P_(p,d) for the law of this word along the periodic local clock and U_d for
the uniform law on its 16^d words,

    max_w |P_(p,d)(w)-16^(-d)| <= D_p,
    TV(P_(p,d),U_d) <= min(1, 16^d D_p/2).                  (CH5)

This is a distribution theorem for an entire finite causal transcript; it
keeps the nonlinear digit thresholds rather than replacing them by a few
spatial Fourier observations.

## CH4. Transfer to the actual source history, with the next birth charged

Let J_A={A,...,2A-1}, p=p_A, and epsilon_A be PE's exact weight distance
sum_n |1_(J_A)(n)/A-1_I(n)/L|. For 1<=d<=L, let P^actual_(A,d) be the law
of the d successive local digits read from the **actual** values
x_n,x_(n+1),...,x_(n+d-1), starting at n uniform in J_A. Then

    TV(P^actual_(A,d),U_d)
       <= epsilon_A/2 + (d-1)/L + min(1,16^d D_p/2).        (CH6)

The bound may of course be clipped at 1.

**Proof.** Pushforward by the same actual transcript map contracts total
variation, so changing the start-time law from J_A to I costs <=epsilon_A/2.
On I, actual and periodically extended transcripts agree except possibly
when n>2L-d+1. There are d-1 such start indices. Coupling at the same n
costs at most (d-1)/L. Apply CH5 to the periodic extension and the triangle
inequality. This explicitly pays for every transcript crossing the next
p-pole; no artificial periodicity is assigned to the whole source.

In particular, for integer d_A>=1 satisfying

    16^(d_A) p_A^(-gamma) log p_A ->0,
    16^(d_A)/p_A ->0,

one has TV(P^actual_(A,d_A),U_(d_A))->0. These conditions imply d_A=O(log p_A),
hence (d_A-1)/L_A->0; epsilon_A->0 is PE's proved coverage theorem. One simple
sufficient choice is d_A <= c log(p_A) for any fixed
0<c<min(gamma,1)/log16. No numerical c or gamma is claimed.

Although gamma can be replaced by min(gamma,1) harmlessly, the separate 1/p
term is retained so the quantifiers do not depend on an implicit restriction
on the imported exponent. Fixed d is a special case.

The full real BBP digits do not appear in P^actual_(A,d). The theorem is
source-authenticated and source-selected, but its carrier is the changing
p_A-principal component. It supplies neither H2* nor LS for the full zero
source, and it does not pay the remaining signed complement covariance.

## CH5. Exact information horizon and finite sensor aliasing

The periodic local clock has m distinct states, each equally weighted. Its
word law has support of size at most m. Consequently, with M=16^d,

    TV(P_(p,d),U_d) >= max(0,1-m/M).                        (CH7)

If M>=p then distinct p-grid points lie in distinct word cylinders, so

    TV(P_(p,d),U_d) = 1-m/M.                               (CH8)

**Proof.** If S is the observed word support, P(S)=1 and U_d(S)=|S|/M<=m/M.
This gives CH7. When M>=p, a cylinder's width is <=1/p, hence contains at
most one of the distinct clock points. Then |S|=m and P(w)=1/m on S.
Summing absolute differences on S and its complement gives CH8 exactly.

Thus d-log_16 m ->+infinity forces TV->1. The finite clock cannot simulate
arbitrarily long Haar transcripts, despite all fixed transcripts becoming
uniform in the selected-prime limit. This is an exact support obstruction,
not a claimed sharp location of the transition between CH5 and CH7; the
proven sufficient range and the necessary range do not coincide.

Finite precision is also explicit. Every clock point v/p, v!=0, has distance
at least 1/(pM) from every M-grid word boundary: |v/p-k/M| is a nonzero
integer divided by pM because p is odd and M=16^d. A certified initial-phase
error <1/(pM) therefore preserves its d-digit word. This is a sufficient
worst-case precision requirement, not an optimal per-point requirement.
Reading each current local digit separately has the weaker sufficient bound
1/(16p) per sample. Future multiplication can amplify an initial phase error;
these two acquisition models must not be conflated.

## CH6. Increasing exact carry memory isolates a fixed source; it gives no rate

For real s let U_n(s)=U_n(0)+16^n s, C_n(s)=floor U_n(s), and
kappa_n(s)=C_n(s)-16C_(n-1)(s). Put

    sigma_J=min_(0<=n<=J) (1-{U_n(0)})/16^n.

The previously proved finite carry-cylinder statement is

    C_0(s)=0 and kappa_n(s)=kappa_n(0) for 1<=n<=J
       iff 0<=s<sigma_J.                                  (CH9)

Here sigma_J>0 and sigma_J<=16^(-J). Therefore a **single fixed real seed**
that matches C0 and all these carries along unbounded J is necessarily zero.
If C0 is discarded, the exact fiber is instead

    union_(k in Z) [k,k+sigma_J),

and its infinite intersection is Z. All integer seeds preserve every carry;
they change the unwrapped initial state. Proof: equal carry differences imply
C_n(s)-C_n(0)=16^n C_0(s). Subtract k=C_0(s), then use CH9 for s-k.

This gives a precise inverse-limit discipline. Horizon-dependent seeds s_A
in the prior CF-A construction can approach zero, retain increasingly long
finite carry prefixes, and have future covariance tending to 1. That does not
produce one fixed nonzero seed in the intersection: the future observable
also moves to later epochs, where its Lipschitz constant grows like16^(2A).
Pointwise source isolation is not a uniform convergence theorem for those
moving observables.

Canonical rational p-principal parts have been defined only on rational
states. They cannot simply be assigned to an arbitrary irrational real seed.
A separate real/p-adic shadow model requires a declared common transport;
calling its independent coordinates one authenticated real source would
change the carrier. This note makes no fixed rational nonnormal seed claim.

## CH7. Learning more local digits forces prime leakage toward one

This finite statement applies to **any** empirical circle sample x_r and any
nonzero integer h; it is instantiated below with the authenticated clean
p-clock. Let M=16^d and let P be conditional averaging over the word cells
w_r=floor(M x_r). Write a_r=e(hx_r), mu=E a. Then

    E|a-Pa|^2 <= pi^2 h^2/M^2,
    ||Pa-mu||_2^2 >= 1-|mu|^2-pi^2 h^2/M^2.              (CH10)

The second quantity is the centered prime leakage of this history feature
space. For each fixed h!=0, source-selected p-clocks with mu->0 and
d->infinity have leakage tending to1. If h varies with the clock, the sufficient
additional condition is |h|/16^d->0, together with mu->0.
Thus an observer can learn almost the entire local phase while the transcript
law itself approaches uniform; informative local memory is not a small-leakage
certificate for complementary cancellation.

**Proof.** In word cell w, use the reference phase
c_w=e(h(w+1/2)/M). Since |x-(w+1/2)/M|<=1/(2M) and
|e(u)-e(v)|<=2pi|u-v|, one has |a-c_w|<=pi|h|/M.
The conditional mean Pa minimizes mean squared error among cell-constant
complex functions, so E|a-Pa|^2<=E|a-c_w|^2<=pi^2h^2/M^2.
Orthogonal decomposition gives

    1=E|a|^2=E|Pa|^2+E|a-Pa|^2,
    ||Pa-mu||_2^2=E|Pa|^2-|mu|^2.

Subtract to obtain CH10. No distributional or typicality hypothesis was used.
The upper bound may be clipped at1. On the selected clock, mu is bounded by
the available uniform nontrivial subgroup estimate; hence the asserted limit.

For a second complex sample b with |b_r|<=1, retaining the bilinear covariance
convention, conditional averaging also gives the exact signed decomposition

    Cov(a,b)=Cov(Pa,Pb)+E[(a-Pa)(b-Pb)],                  (CH11)
    |Cov(a,b)-Cov(Pa,Pb)|
       <= (pi|h|/M) sqrt(E|b-Pb|^2) <= pi|h|/M.          (CH12)

Indeed all mixed projection/residual terms have average0, cell by cell.
Cauchy--Schwarz is applied to the residual product after the exact split.
This is a useful finite reduction to signed conditional means, but the
remaining coarse covariance still has to be estimated from the original
source. Increasing d makes the residual small by making the feature space
more informative about a; it does not force the coarse signed term to vanish.

The control b=conjugate(a) proves the distinction exactly:

    Cov(a,b)=1-|mu|^2,
    Cov(Pa,Pb)=E|Pa|^2-|mu|^2,
    E[(a-Pa)(b-Pb)]=E|a-Pa|^2.

Its coarse covariance tends to1 as the local phase is learned. This is an
explicit changed-complement control, not the authentic BBP complement.
The prior same-forcing wrong-seed constructions separately show why local
history laws alone fail to authenticate the needed cross-channel sign.

Finite checks also use the sharper data-dependent inequality

    E|a-Pa|^2 <= 4pi^2h^2 E|x-Px|^2 <= pi^2h^2/M^2.       (CH13)

The first inequality follows by expressing conditional variance as the mean
squared difference of two samples in the same cell, divided by2, and applying
the chord bound. For the second, a variable in an interval [l,u] has variance
at most (u-l)^2/4: (x-l)(u-x)>=0 gives
Var(x)<=(u-Ex)(Ex-l)<=(u-l)^2/4. This elementary argument works with finite
weighted samples and includes singleton cells. Exact rational checks may use
pi^2<10 to obtain the computable bounds40h^2 E|x-Px|^2 and10h^2/M^2.

CH10--13 are laws of a finite observer/projection, not a claim of physical
nonlocality, source randomness, or bounded mathematical memory implying Haar
arithmetic. Their p-clock specialization preserves the original source.

## The arrow that remains unpaid

CH1--5 upgrade the authentic local marginal theorem into coherent finite
history laws, nonlinear observer bounds and a quantified information horizon.
They do not estimate

    Cov_A(e(h[U_n]_pA), e(h(U_n-[U_n]_pA)))

for original U0=0. The same local-history law persists for the prior wrong
rational seeds whose denominators avoid p_A. Thus even complete local
history typicality fails to imply the selected cross-channel signed estimate.
A useful next theorem must control the complement *conditioned on*, or signed
against, these source-selected histories, while retaining full source
chronology. A bounded-resolution or bounded-memory approximation alone is
insufficient without a proved leakage/residual budget.

Provenance: PE1--9 at parent1990b051, original selected_orbit.py, and
Bourgain--Konyagin (2003), Theorem2.1 (printed p78),
https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf.
Finite Fourier inversion, geometric sums, coupling/TV contraction and
trigonometric approximation are classical identities/tools, proved or scoped
above. New asymptotic source instances are paper proofs, not Lean-certified.
**Pi base16 normality: OPEN. RH: OPEN.**
