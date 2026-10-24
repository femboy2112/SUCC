# Cyclotomic selected-source interference: twisted clocks and the dyadic cost

**Research status, 24 October 2026.** This file is written on the child of
PR #257 at `5435497dc77a313d1ebbc56ac96c11e593db2619`. The sibling
PR #256 was read at `66fcb6f61b2851371bfe58ba6db74bdeacb46ef0`; its files
and assumptions are not silently merged. Their common ancestor is repaired
BBP PR #252 at `364962ac0c0e8fb4d06c37468a5d50336d68a9ee`.

The results below are **paper proofs**, with exact finite implementations
and formal scope recorded separately by the execution report. The sole deep
external estimate used here is the unweighted finite-field subgroup theorem
of Bourgain--Glibichuk--Konyagin (BGK). The extension to every temporal
character is derived below, rather than assumed for arbitrary weights.
Scholarly novelty is unverified. **PI NORMALITY PROVED: NO.**

## 1. Source audit and notation

Put `e(x)=exp(2*pi*i*x)` and retain the authentic source

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), n>=1,
    y_0=0,  y_(n+1)={16*y_n+r(n+1)}.

Its bounded Green tail satisfies

    16*T_n-T_(n+1)=r(n+1),
    T_0=pi/16,
    0<T_n<1/((8n+1)(8n+2)), n>=0.

The last bound follows from the source kernel fact
`0<g(t)/(16-t^8)<1-t` for `0<=t<1` and its beta integral.
The tail is strictly decreasing. These are authenticated parent results,
not new normality hypotheses.

Let `p=8m+1` be prime, `L=ord_p(16)`, `Delta=3m`, and `B=Delta/L`.
Supplementary quadratic reciprocity gives `(2/p)=1`, hence 16 is an
eighth power and `L|m`. The first denominator divisible by p is
`8(m+1)-7=p`; its coefficient is 4. The next event is at `n=4m+1`.
Consequently, throughout the **actual** window `n=m+1,...,4m`,

    y_(m+1+t)=4*16^t/p+w_t mod 1,  0<=t<Delta,

where `w_t` is the unique p-prime-to torsion complement. Its denominator
is coprime to p and

    w_(t+1)=16*w_t+r(m+2+t) mod 1, 0<=t<Delta-1.

This rederives the source split used by sibling #256. In particular, the
small size of `r(n)` is not a small ordinary time increment of `w_t`:
the increment contains `15*w_t`. No bounded-variation hypothesis follows.

Fix an integer `h!=0`, and assume `p` does not divide h. Define

    u_s=e(4*h*16^s/p), 0<=s<L,
    v_t=e(h*w_t), 0<=t<Delta,
    mu=(1/L)*sum_(s<L) u_s,
    z_s=(1/B)*sum_(b<B)(v_(bL+s)-v_(bL)), 0<=s<L.

Then the actual mixed term of #256 is

    I_p(h)=(1/L)*sum_(s<L)u_s*z_s,
    W_p(h)/Delta=mu*(1/B)*sum_(b<B)v_(bL)+I_p(h),
    W_p(h)=sum_(n=m+1)^(4m)e(h*y_n).

All complex signs and the complementary source remain present. The
frequency `4h` is nonzero modulo p; primes dividing h are excluded from
these subgroup estimates, and are finitely many for fixed h.

## 2. Uniform multiplicative twists from unweighted subgroup cancellation

This elementary consequence is useful because it controls every character
of the temporal clock, with no assumption `L>sqrt(p)`.

For any cyclic subgroup `H=<g>` of `Fp*` of order L, any `a!=0 mod p`,
and `k in Z/LZ`, put

    Uhat_a(k)=(1/L)*sum_(s<L)e(a*g^s/p)*e(-k*s/L),
    epsilon(H)=max_(c!=0 mod p) |(1/L)*sum_(x in H)e(c*x/p)|.

**Theorem CSI-01 (uniform twist transfer).**

    |Uhat_a(k)|^2 <= 1/L+(1-1/L)*epsilon(H).

The maximum is over a finite set, so the statement is finite and exact;
no numerical estimate of epsilon is needed for the proof.

**Proof.** Expand the square and set `d=s-t mod L`. Since `g^L=1`,

    |Uhat_a(k)|^2
      = L^-2 * sum_(d<L)e(-k*d/L)
                    * sum_(t<L)e(a*(g^d-1)*g^t/p).

At `d=0` the inner sum is L. At every other d, `g^d!=1`, so its
coefficient `a*(g^d-1)` is nonzero modulo p and its modulus is at most
`L*epsilon(H)`. Triangle inequality gives the result. QED.

For finite certification one can replace epsilon(H) by the smaller

    epsilon_a=max_(1<=d<L)
                    |(1/L)*sum_(t<L)e(a*(g^d-1)*g^t/p)|,

when `L>1`. The zero-frequency coefficient also satisfies the separately
sharper `|Uhat_a(0)|<=epsilon(H)`.

For good primes `p=8m+1` with `L>p^(1/3)`, BGK gives constants `C,nu>0`
independent of p, a and k such that `epsilon(H)<=C*p^(-nu)`. Hence

    sup_(a!=0,k) |Uhat_a(k)|
       <= sqrt(1/L+(1-1/L)*C*p^(-nu))
       <= sqrt(p^(-1/3)+C*p^(-nu)).

This is a power saving for **all temporal character twists of the authentic
p-clock**, not just its constant character. In multiplicative notation
the twist is the character `chi(g)=e(-k/L)` of H. It is not an arbitrary
complementary BBP weight.

The exact square expansion is independently testable by integer residue
enumeration followed by certified roots of unity. The asymptotic BGK input
is an external theorem, not proved by those finite checks.

## 3. A quantitative bound on the actual interference, with its unpaid factor

For a complex vector `f=(f_0,...,f_(L-1))`, use normalized Fourier coefficients

    fhat(k)=(1/L)*sum_(s<L)f_s*e(-k*s/L),
    ||f||_A=sum_(k<L)|fhat(k)|.

Finite orthogonality gives the signed pairing identity

    (1/L)*sum_(s<L)u_s*z_s=sum_(k<L)Uhat(k)*zhat(-k).

**Theorem CSI-02 (actual-source spectral budget).** With the authentic z
from section 1, and
`delta_p=sqrt(1/L+(1-1/L)*epsilon(H))`,

    |I_p(h)| <= epsilon(H)*|zhat(0)|
                 +delta_p*sum_(k!=0)|zhat(k)|
              <= delta_p*||z||_A.                         (1)

The second inequality uses `epsilon<=delta_p`, which follows from
`0<=epsilon<=1` and
`delta_p^2-epsilon^2=(1-epsilon)*(epsilon+1/L)>=0`.

Equation (1) is a genuine estimate for the full signed mixed term; it
retains the exact BBP complementary sequence. It becomes asymptotically
nontrivial only after a suitable upper bound for its actual Fourier mass.
In particular,

    ||z||_A=o(1/delta_p) implies I_p(h)->0.               (2)

Statement (2) is a sufficient condition, not an asserted property of BBP,
and not a new proof of normality. The phase-alignment information discarded
in (1) can still be decisive. A large upper bound from (1) does not prove
that I_p is large.

For comparison, Parseval gives only `||z||_A<=sqrt(L)*||z||_(2,normalized)
<=2*sqrt(L)`. Combining that generic bound with BGK need not save anything.
Thus the extension to all multiplicative twists does **not** license an
arbitrary bounded weight theorem.

The elementary Abel alternative is also exact. For one block, let
`U_j=sum_(0<=s<j)u_s`. Then

    sum_(s<L)u_s*(v_s-v_0)
       =U_L*(v_(L-1)-v_0)
          -sum_(s<L-1)U_(s+1)*(v_(s+1)-v_s).

A bound on full-period `U_L` alone does not bound every prefix `U_j`.
Even a good prefix bound must still pay for the actual complementary
variation. Those are distinct unproved inputs in the BBP application.

## 4. The actual Green source perturbs the complementary spectrum very little

Let `n_b=m+1+bL`. For each block define the exact source-straightened phase

    eta_b=w_(bL)+T_(n_b) mod 1,
    f_b(s)=e(h*16^s*eta_b), 0<=s<L,
    z^0_s=(1/B)*sum_(b<B)(f_b(s)-f_b(0)).

The complementary recurrence and the exact backward Green equation give

    w_(bL+s)+T_(n_b+s)=16^s*(w_(bL)+T_(n_b)) mod 1,
    v_(bL+s)=f_b(s)*e(-h*T_(n_b+s)).

**Theorem CSI-03 (BBP spectral perturbation budget).**

    ||z-z^0||_A
      <=2*pi*|h|*(sqrt(L)+1)*(1/B)*sum_(b<B)T_(n_b)
      <2*pi*|h|*(sqrt(L)+1)/((8m+9)*(8m+10)).           (3)

Also, for `I^0=(1/L)*sum_s u_s*z^0_s`,

    |I_p(h)-I^0| <=4*pi*|h|*T_(m+1)
                  <4*pi*|h|/((8m+9)*(8m+10)).          (4)

**Proof.** For one block, `|v_(bL+s)-f_b(s)|<=2*pi*|h|*T_(n_b+s)`.
Monotonicity bounds these errors by `2*pi*|h|*T_(n_b)`. Parseval and
Cauchy--Schwarz imply `||q||_A<=sqrt(L)*||q||_(2,normalized)` for any
length-L vector q. Subtracting its value at s=0 adds a constant vector,
whose Fourier A-norm is exactly the modulus of that constant. Average
the resulting bounds over b to obtain (3). The pointwise centered error
is at most `4*pi*|h|*T_(n_b)`; pair it with `|u_s|=1` to obtain (4).
The strict rational bounds follow from the actual BBP beta envelope. QED.

Since `L<=m`, (3) is `O_h(m^(-3/2))`. The actual rational forcing therefore
does not itself create a growing Fourier regularity cost on these windows:
it differs negligibly from a free expanding complementary orbit. But the
free initial phases eta_b are selected by the same unresolved source.
Their Fourier mass or signed alignment has not been bounded here.

The exact tail in eta_b is essential to this statement. Replacing it by
a low-order rational approximation at the initial time incurs the factor
`16^s`; a uniformly accurate free orbit over L steps requires paying that
amplification. No inexpensive finite-precision reconstruction is asserted.

Combining (1) and (3) gives the explicit source-faithful bound

    |I_p(h)| <=delta_p*(||z^0||_A
                +2*pi*|h|*(sqrt(L)+1)/((8m+9)*(8m+10))). (5)

The unpaid quantity is now stated exactly. This result must not be
described as a sublinear bound for the actual pi Fourier sums.

## 5. Exact forcing and every odd-prime clock can coexist with a coherent window

The following control is stronger than the unforced coprime-clock example
in sibling #256: it retains the entire BBP forcing forever, all odd-prime
primary components at every time, and eventual equality with the authentic
trajectory. It changes one declared source premise: the selected initial
state `y_0=0`.

For any real initial lift delta, write

    y_0(delta)={delta},
    y_(n+1)(delta)={16*y_n(delta)+r(n+1)}.

Induction and the Green recurrence give

    y_n(delta)-y_n(0)=16^n*delta mod 1,
    y_n(delta)+T_n=16^n*(delta+T_0) mod 1.              (6)

Fix a nonnegative integer q, let `K=4m+q`, and choose an integer c nearest
to `-16^K*T_0`. Put `delta_K=c/16^K`. Then

    |delta_K+T_0|<=1/(2*16^K).                         (7)

This selection can be made from certified BBP, Machin or polygon intervals;
no supplied pi digits are needed. Ties cannot occur because T_0 is
irrational. The interval selector must refine until a unique nearest cell
is certified, rather than treating a floating approximation as proof.

**Theorem CSI-04 (dyadic finite-window saturation).** For all n and every
odd prime ell, the Q/Z ell-primary components of `y_n(delta_K)` and
`y_n(0)` are identical. For all `n>=K`, the full states are identical.
Yet, writing

    W'_p(h)=sum_(n=m+1)^(4m)e(h*y_n(delta_K)),

one has

    |W'_p(h)/(3m)-1|
       < 2*pi*|h|/((8m+9)*(8m+10))
           + pi*|h|*(16^(4m+1)-16^(m+1))/(45*m*16^K)
       < 2*pi*|h|/((8m+9)*(8m+10))
           + pi*|h|*16^(1-q)/(45*m) =: E_(m,q,h).     (8)

**Proof.** The difference in (6) is dyadic. Its odd-prime primary parts
are zero, including every higher odd-prime-power component. It is an
integer for n>=K. For the phase estimate, (6)--(7) and the elementary
`|e(x)-1|<=2*pi*|x|` give

    |e(h*y_n(delta_K))-1|
       <=2*pi*|h|*(T_n+16^n/(2*16^K)).

Average over the 3m indices, bound their tails by `T_(m+1)`, and sum
`sum_(n=m+1)^(4m)16^n=(16^(4m+1)-16^(m+1))/15`. This gives (8).
No asymptotic or sample extrapolation is used in this proof. QED.

The p-clock, its order L, its closure, and every local multiplicative
character sum are exactly the same for this changed initial state.
The complementary recurrence still has precisely the authentic forcing.
Let I'_p be its mixed term. Since the anchor term has modulus at most
`|mu|<=epsilon(H)`,

    |I'_p(h)-1| <=E_(m,q,h)+epsilon(H).               (9)

Thus, along good primes, `I'_p(h)->1` for every fixed h!=0 and fixed q.
This is a proved family of source-typed finite-window controls, not a
counterexample to pi normality and not a fixed changed source with
persistent exceptional asymptotics.

The quantifier order is crucial:

    for every growing window there exists a dyadic initial state
    making that window coherent;
    for every fixed dyadic initial state there is a finite time
    after which its orbit equals the authentic orbit exactly.

Consequently, every fixed changed state has the same normality verdict as
pi's authentic state. In fact there is an exact future-equivalence theorem.

**Theorem CSI-05 (complete odd-primary data and finite coalescence).** For
any two rational initial lifts a,b under the same forcing, the following
are equivalent:

1. Their canonical ell-primary components in Q/Z agree for every odd prime
   ell, retaining the full ell-power component.
2. The reduced denominator of a-b is a power of two.
3. Their forced trajectories agree at every sufficiently large time.
4. Their forced trajectories agree at at least one time.

If the denominator is `2^s`, their first common time is exactly
`ceil(s/4)`. Every odd-primary observation at every time agrees in this
case; conversely agreement of all odd-primary components at any one time
already implies condition 1.

**Proof.** Write the reduced denominator of a-b as `2^s*q`, with q odd.
Canonical primary decomposition in Q/Z gives condition 1 exactly when
q=1. The trajectory difference is `16^n*(a-b)` modulo 1, so it vanishes
exactly when `2^s*q` divides `16^n`. This is possible exactly when q=1,
and first occurs at `4n>=s`. Multiplication by 16 is invertible on each
odd-primary subgroup, giving the assertion about any observation time.
QED. This proof uses the common forcing but does not require its BBP form.

Thus complete odd-primary data determine an eventual trajectory class
among rational initial states. They do not determine its finite prefix
or a bound on its coalescence time. What fails is a **uniform finite-window
saving** based only on the forcing and odd clocks, with no control on the
dyadic depth of the selected initial state relative to the window. This is
precisely the information a finite source-blind prime-clock argument must
pay for. No claim is made that a finite subset of odd primes determines
the same eventual class.

## 6. A quantitative cost forced by the hostile family

Apply CSI-02 to the changed-state centered complementary sequence z'.
Equations (8)--(9) imply

    ||z'||_A >= max(0,1-E_(m,q,h)-epsilon(H))/delta_p.   (10)

Because `delta_p->0` and `E_(m,q,h)->0` along good primes, the Fourier mass
cannot be uniformly bounded on this exact-forcing, identical-odd-clocks
family. If z' has r nonzero temporal Fourier coefficients, Parseval and
`|z'_s|<=2` give `||z'||_A<=2*sqrt(r)`, hence

    r >= max(0,1-E_(m,q,h)-epsilon(H))^2/(4*delta_p^2). (11)

This makes the missing weight hypothesis in a twisted subgroup argument
quantitative. A claim of uniformly bounded complementary spectral mass
from the source forcing plus odd-primary data is refuted by an explicit
family satisfying those premises. A claim restricted to the exact initial
state zero is not refuted and remains open.

## 7. Exact mixed-interference moments inside one odd-clock class

This subsidiary identity audits source selection at the level of the
actual mixed observable, rather than only at the level of the full circle
Weyl sum. It does not furnish a pointwise cancellation estimate.

Let `s=v_2(|h|)` and choose `K>=4m+floor(s/4)+1`. Average over the finite
dyadic initial states `delta=c/16^K`, `0<=c<16^K`. Every state retains all
odd-primary source components and coalesces with the original orbit by K.
Let `I(delta)` denote its mixed term using the same p-clock. The complete
average is mathematical; no claim is made that its exponentially many
source probes are provided at no cost.

**Theorem CSI-06 (source-fiber second and fourth moments).** Put

    V=|u_0-L*mu|^2,
    M2=(L-1+V)/(B*L^2).

Then the exact grid averages obey

    E_delta I(delta)=0,
    E_delta |I(delta)|^2=M2,
    E_delta |I(delta)|^4
       =2*M2^2-(L-1+V^2)/(B^3*L^4).                (12)

In particular,

    M2 <= (1+2*epsilon(H))/Delta + epsilon(H)^2/B,
    E_delta |I(delta)|^4 <=2*M2^2.

**Proof.** Expand I(delta) as a Fourier polynomial in delta. At a time
`n=m+1+bL+s`, its coefficient is `u_s*v_(bL+s)/Delta` for s>0. At a
block start it is `(u_0-L*mu)*v_(bL)/Delta`. All associated frequencies
are `h*16^n`. They are nonzero and distinct modulo `16^K`, so their
characters have zero mean and are pairwise orthogonal on the grid. The
sum of squared coefficient magnitudes is
`B*(L-1+V)/Delta^2=M2`.

For the fourth moment, different unordered pair sums of these frequencies
remain distinct modulo `16^K`. Indeed, after cancelling common terms,
let j be the least exponent where the two multiplicities differ. Its
coefficient is plus or minus 1 or 2, so the 2-adic valuation of the
difference is `s+4j` or `s+4j+1`. Since both multisets have cardinality
two, `j<=4m-1`; this valuation is strictly less than 4K. Thus only the
two pairings survive fourth-moment expansion, with the duplicate diagonal
subtracted once. For coefficients c_n, this gives
`2*(sum|c_n|^2)^2-sum|c_n|^4`. Here the last sum is
`B*(L-1+V^2)/Delta^4`, proving (12). Finally,
`|u_0-L*mu|<=1+L*epsilon(H)` gives the stated upper bound. QED.

These exact moments vanish along good primes, independently of the
authentic complementary phases, even though CSI-04 selects a dyadic
origin with `I(delta)` approaching 1. Therefore conditional averaging
over states with **identical complete odd-clock data** still cannot select
the initial state zero. The hidden source change is now visible inside
one eventually-coalescent class. Conversely, no conclusion of exceptional
infinite behavior follows from choosing a different member of that class
at each growing p.

The independent executable
`scripts/cyclotomic_fiber_moment_oracle.py` constructs the authentic
trajectory directly from the common BBP forcing, without importing the
new selected-source implementation. It verifies the full signed
coefficient formula and equality of rational phase-coefficient maps for
the second and fourth moments at `(p,h)=(17,1),(17,-2)`, and the second
moment at `(41,1)`. Its deterministic receipt includes the exact maps and
source hashes. It uses no floating arithmetic and does not enumerate the
`16^K` origins. These are finite independent certificates of the algebra,
separate from the all-prime paper proof and external BGK theorem.

## 8. Higher prime powers and CRT boundaries

The source audit at #256 identifies the first p^2 birth and the finite
return defect `(16^m-1)/p mod p`. Those exact algebraic identities do not
place the full complementary weight inside a subgroup of the field Fp.
BGK as used in CSI-01 is a prime-field theorem. It is not silently applied
to a composite conductor or to Z/(p^k)Z. Exact CRT decomposition preserves
the product of source-labelled additive characters, but does not make
the factors statistically independent.

The dyadic control preserves every higher odd-prime primary component as
well. Therefore adding any finite collection of return identities for those
torsion components does not repair the uniform finite-window obstruction.
A raw p-integral unwrapped lift or a literal integer-carry history is a
different readout and is not automatically preserved; the live-source
addendum below gives the exact distinction and a finite-precision extension.
Carrying the dyadic/source-state label resolves the ambiguity; it does not
by itself prove cancellation for label zero.

## 9. Verdict and remaining arithmetic work

The positive progress is an unconditional extension of authenticated local
BGK cancellation to **every multiplicative clock character**, together
with a quantitative bound for the full actual interference in terms of
its measured temporal Fourier mass. The specific BBP Green kernel supplies
the small rational spectral-perturbation budget (3), using the exact tail,
the selected boundary value and the correct source recurrence.

The strongest hostile result keeps the actual forcing and all odd-primary
clocks while producing near-maximal interference on an arbitrarily large
selected window. Its precise omitted premise is the initial state zero;
its eventual coalescence prevents an illicit infinite counterexample claim.

No bound `I_p(h)->0` for the authentic initial state has been obtained.
No growing-lag signed aggregate estimate for authentic pi has been obtained.
The next source-specific arithmetic task is to control the actual
complementary spectrum or its signed pairing with Uhat for y0=0, rather
than asserting that small forcing, local closure, a Haar ensemble, or
coprime CRT labels supply that control. A proof for one fixed h changes
the pi cancellation ledger. A proof for every fixed nonzero h would close
the existing prime-window/Weyl route, with its separately stated PNT-AP
and source-transport dependencies.

## 10. Incomplete local windows: a genuine consequence, with the weight cost retained

The uniform twist theorem also controls incomplete local clock intervals,
which were not covered by the complete-period estimate alone. This result
does not require an assumption on the complementary source.

**Lemma CSI-07a (normalized completion cost).** For integers `L>=1` and
`0<=T<=L`, set `q_s=1` for `0<=s<T` and zero otherwise, on Z/LZ. Then

    sum_(k!=0)|qhat(k)|<=log L,
    ||q||_A<=T/L+log L<=1+log L.                    (13)

All logarithms here are natural. For L=1 the nonzero sum is empty. For
L>=2, the geometric-series formula and sine concavity give

    |qhat(k)| <=1/(L*|sin(pi*k/L)|)
              <=1/(2*min(k,L-k)), 1<=k<L.

If `L=2J+1`, pairing k and L-k bounds the sum by H_J. The elementary
convexity estimate

    1/j <= integral_(j-1/2)^(j+1/2) dx/x

gives `H_J<=log(2J+1)=log L`. If `L=2J`, the same pairing gives
`H_(J-1)+1/(2J)<=log(2J-1)+1/(2J)<=log(2J)`.
The final inequality follows from `log(1+x)>=x/(1+x)` for x>=0.
The zero coefficient is T/L, proving (13).

**Theorem CSI-07b (all incomplete p-local intervals).** In the source
regime of section 1, for every starting offset r and every integer J>=0,

    |sum_(s=0)^(J-1)e(a*16^(r+s)/p)|
       <=J*epsilon(H)+delta_p*L*log L,               (14)

provided `a!=0 mod p`. Negative offsets can be read using modular inverses;
the source application only needs nonnegative offsets inside its window.
For `0<=T<=L`, the sharper prefix form is

    |sum_(s<T)e(a*16^(r+s)/p)|
       <=T*epsilon(H)+delta_p*L*log L
       <=delta_p*L*(1+log L).                        (15)

**Proof.** Fourier pairing of u with the interval indicator, CSI-01, and
(13) prove (15), separating the zero mode. Replacing a by `a*16^r` does
not change the subgroup or the bounds. Split J into full L-periods and
one remaining prefix; each complete period costs at most L*epsilon(H).
This gives (14). QED.

Along good primes, `epsilon(H)<=C*p^(-nu)` and
`delta_p<=sqrt(p^(-1/3)+C*p^(-nu))`. Since `L<=m=Delta/3`, (14) is
`o(Delta)` uniformly for `0<=J<=Delta` and all nonzero a modulo p.
For any fixed positive fraction of a period it also gives o(J). No
relative cancellation is claimed for arbitrarily short J.

In particular, the **authentic p-local factor** of the noncyclic lag sum
has length `J=Delta-d` and coefficient `a=4h*(16^d-1)`. Its magnitude is
o(Delta), uniformly over the growing nonresonant lags `0<d<Delta`.
For p not dividing h, the excluded lags are exactly `L|d`; at these lags
the local factor is identically one and the sum equals Delta-d. The full
BBP lag also contains its complementary phase factor, so this local
theorem is not a bound for the full signed pi lag correlation.

**Corollary CSI-07c (Abel bound with actual complementary variation).** Put

    V_p=(1/B)*sum_(b<B)sum_(s<L-1)|v_(bL+s+1)-v_(bL+s)|,
    A_p=(1/B)*sum_(b<B)|v_(bL+L-1)-v_(bL)| <=2.

Using the exact Abel identity in section 3 and (15),

    |I_p(h)| <=epsilon(H)*A_p
                 +(epsilon(H)+delta_p*log L)*V_p
              <=2*epsilon(H)
                 +(epsilon(H)+delta_p*log L)*V_p.    (16)

This controls incomplete local prefixes before paying the actual weight
variation; it does not assume a weighted BGK theorem. The generic bound
`V_p<=2*(L-1)` does not make (16) tend to zero. The actual recurrence
contains `15*w_t+r(m+2+t)` in its ordinary phase increment. Small forcing
alone therefore supplies no upper bound of the required strength for V_p.

The dyadic coherent family gives a rigorous hostile cost. Combining
(9) and (16), for its variation V'_p,

    V'_p >= max(0,1-E_(m,q,h)-3*epsilon(H))
                  /(epsilon(H)+delta_p*log L).       (17)

Here L>=2 for the eligible primes. The denominator tends to zero, so no
uniformly bounded complementary variation follows from the exact forcing
and complete odd-clock data alone. As before, this varying-initial-state
family does not refute a theorem restricted to the authentic initial zero.

For the authentic initial state itself, finite exact circle distances
already give appreciable variation. At h=1, the inequalities
`4*||w'-w||_T<=|e(w')-e(w)|<=(44/7)*||w'-w||_T` yield the following
outward integer bounds without floating arithmetic:

| p | L | lower bound for V_p | upper bound for V_p |
|---|---:|---:|---:|
| 17 | 2 | 1 | 2 |
| 41 | 5 | 4 | 8 |
| 73 | 9 | 9 | 15 |
| 97 | 12 | 11 | 18 |
| 113 | 7 | 5 | 8 |
| 193 | 24 | 22 | 37 |

These bounded exact checks are diagnostics, not an asymptotic lower or
upper bound. No useful all-prime estimate for authentic V_p has been
proved here. The genuinely new controlled quantities are the incomplete
**local** clock intervals and nonresonant local lag factors in (14)--(15).

## 11. Live sibling p-squared update: provenance and carry audit

**Dated addendum, 24 October 2026.** During this run sibling PR #256
advanced from the initially audited `66fcb6f61b2851371bfe58ba6db74bdeacb46ef0`
to `0683f8f166b9106ab8405a2d6538415b5ac84ba3`. The exact Git objects
`BBP_CYCLOTOMIC_WITT_LIFT.md`, `bbp_cyclotomic_witt.py` and its tests were
read and audited. This branch does not merge that commit or import a new
analytic assumption from it.

The new theorem is correct for its explicitly **filtered** source: retain
only the p-squared-divisible BBP impulses, start that filtered channel at
zero, multiply its unwrapped phase by p squared, and reduce modulo p squared.
With `M=(p^2-1)/8` and `q_p=(16^m-1)/p mod p`, its four endpoint transports
are `5M,2M,M,0`; successive group endpoints differ by `8M+1`. Since
`16^M=1+p*q_p mod p^2`, both its transport shear and signed source shear
follow by finite expansion. This is not the entire BBP p-primary phase:
the filtered channel omits lower-order p impulses.

There are three different observations to keep separate:

1. **Canonical p-primary Q/Z state, at every odd p-power:** preserved by
   every dyadic initial perturbation, exactly as proved above.
2. **The new source-filtered C_k:** preserved because its retained forcing
   impulses and zero channel initial state are unchanged. Even if the
   global dyadic initial lift delta is included before scaling, its
   contribution `p^2*16^n*delta` is zero modulo p squared since delta is
   p-integral.
3. **A raw p-integral unwrapped lift or literal integer carries:** not
   generally preserved. The unwrapped difference is `16^n*delta`, without
   the factor p squared. Where the p-integral reductions are defined, it
   can be nonzero modulo p squared even after the circle states coalesce.

An exact witness is `p=17`, `delta=1/16`, `n=1`. The authentic and changed
unwrapped values are `47/15` and `62/15`. Their circle states are both
`2/15`, but their reductions modulo 289 are respectively 138 and 139;
their first integer carries are 3 and 4. The filtered p-squared stream has
events `37,145,181,217` and endpoint `C_1=19` in both cases. Thus claiming
preservation of every imaginable carry-augmented observer would be false.

The new sibling dossier describes an endpoint-gap mutation control; its
inspected test file does not explicitly instantiate that particular wrong
gap. An independent exact audit witness is `p=17`, `C_1=19`: the correct
second endpoint is `C_2=175`, whereas replacing the transport factor
`16*(1+8*p*q_p)` by `16*(1+3*p*q_p)` gives 124. This is an additional
finite audit witness, not a modification of sibling archival authority.

**Corollary CSI-08 (finite modular lift probes have an explicit precision
cost).** Let `D=product p_i^(a_i)` be any prescribed odd modulus, collecting
a finite list of required odd-prime-power congruences. Let ell be the least
nonnegative integer such that `16^ell>=D`, choose `K=4m+ell+q` with q>=0,
and choose c nearest to `-16^K*T_0/D`. Set

    delta=D*c/16^K,
    |delta+T_0|<=D/(2*16^K)<=1/(2*16^(4m+q)).

The same proof as CSI-04 gives the unchanged coherence budget E_(m,q,h).
For each specified p_i and every n,

    U_n(delta)-U_n(0)=16^n*delta in p_i^(a_i)*Z_(p_i).

Thus the specified typed p-adic congruence readouts of the unwrapped lifts
are preserved wherever defined; if the full lifts themselves have p-poles,
the displayed assertion is still a well-defined congruence of their
difference. The proof is simply that `16^K` is an odd-prime unit and D
contains each required power. All Q/Z odd-primary parts remain unchanged,
and coalescence occurs by K. The extra dyadic precision cost is exactly
the sufficient ell with `16^ell>=D`.

This finite-CRT construction does not claim preservation of literal integer
floors or the complete carry history. Nor does it preserve every modulus
at once: the modulus D is fixed before choosing the state and precision.
It supplies a source-typed finite probe obstruction, not an infinite
counterexample. BGK remains a theorem about the prime field Fp; neither
this congruence control nor the sibling filtered p-squared shear licenses
its application to arbitrary composite conductors or weights.

## External theorem source and authority

BGK: Bourgain, Glibichuk and Konyagin (2006), *Estimates for the Number of
Sums and Products and for Exponential Sums in Fields of Prime Order*,
DOI `10.1112/S0024610706022721`. The precise uniform statement and a full
proof are also in Emmanuel Kowalski, *Exponential sums over small subgroups,
revisited*, version 2, Theorem 1.1:
<https://arxiv.org/html/2401.04756v2>.
For every gamma>0 it supplies constants C_gamma,nu_gamma>0 for all prime
fields, all subgroups of size at least p^gamma and every nonzero additive
frequency. Here gamma=1/3. Those constants are not numerically instantiated.
The mixed-weight extension, Green perturbation and dyadic control above
have their own displayed proofs; no arbitrary-weight BGK theorem is cited.
