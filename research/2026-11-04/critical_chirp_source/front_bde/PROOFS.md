# What the prime clocks and radial control do at the critical frequency

Status: paper proofs and explicit changed-forcing countermodel. The original
zero-seeded signed ratchet remains OPEN. All characters below use
`e(x)=exp(2 pi i x)`, forward source time, and the same positive integer H.

## BDE-1. The endogenous radial source passes the critical ratchet

Let U be the original four-pole, zero-seeded source. Let W be its Frobenius dual,
with W_0=0 and

    W_n=16 W_(n-1)+rsharp(n),
    rsharp(n)=8/(8n-6)+4/(8n-5)+4/(8n-4)-1/(8n-1).

Set d=rsharp-2r and Z=(2U-W)/4. The primal angular source in #499/#500 is
Y=(2U+W)/4, so Z=U-Y is precisely their endogenous radial control. Its zero
completed period, from the exact rational logarithmic derivative identity PF-6,
gives the smooth extension

    Z(x)=(1/4) sum_(k>=1) 16^-k d(x+k),  x>=1.

For every integer A>=128, H=A^2 Lambda positive integer, and 1<=Lambda<=A/2,
the maximal subinterval mean obeys

    M_A^Z(H) <= C sqrt((Lambda+log(2A))/A).                 (BDE-1)

The absolute constant does not depend on A,H or the subinterval. In particular,
for EVERY fixed integer h != 0 and the original prescribed H_A(h),

    Lambda_A M_A^Z(H_A)
       = O((log A)^(3/2)/sqrt A) -> 0.                    (BDE-2)

Nonetheless `A^-1 sum_[A,2A) e(h Z_n) -> 1` for each fixed h, and the inherited
radial theorem gives `J_(A,q_A)(Z)/q_A -> 1`. Thus the critical ratchet is NOT a
source-free normality criterion. This is a signed estimate on an actual
zero-seeded sibling source, not a saving for U.

Proof of the derivative bounds. Direct expansion of the eight rational taps gives
`d(x)=15/(8x)+53/(64x^2)+O(x^-3)`. More generally, for m=0,1,2,3,

    d^(m)(x)=(15/8)(-1)^m m! x^(-m-1)+O_m(x^(-m-2)).

One can derive this by differentiating each geometric expansion
`1/(8x-c)`, with its remainder uniformly bounded for x>=2. Differentiation of
the tail is valid by domination by `C_m 16^-k (x+k)^(-m-1)`. The geometrically
weighted first moment is finite, hence

    Z^(m)(x)=(-1)^m m!/(32 x^(m+1))+O_m(x^(-m-2)).

A completely explicit uniform remainder, valid for x>=2, is

    |Z^(m)(x)-(-1)^m m!/(32 x^(m+1))| <= C_m x^(-m-2),
    C_m=(m+1)! [1/30+(167/3840)(16/9)^(m+2)].

Indeed the signed rational taps have sum 15 and sum |c|e=167, so the mean
value theorem bounds the error in d^(m) by
`(m+1)! (167/64)(16/9)^(m+2) x^(-m-2)`. The discounted zeroth and first
moments are 1/15 and 16/225, giving the displayed C_m. In particular
`C_2=18413/6561` and `C_3=5708452/295245`. Since
`32 C_2<128` and `(16/3)C_3<128`, on [A,2A] for every A>=128,

    H Z''(x) in [Lambda/(256A), Lambda/(8A)],  Z'''(x)<0. (1)

Here the lower constant uses `Z''~1/(16x^3)` at x=2A, with a factor-two
margin. The upper constant uses x=A with the same margin.

An elementary differencing proof avoids importing a black-box derivative test.
Write f=HZ and lambda=Lambda/A. For a positive shift d and an overlapping
subinterval, g_d(x)=f(x+d)-f(x) has decreasing derivative between d lambda/256
and d lambda/8. If d<=1/lambda, then g'_d<=1/8. Therefore

    |sum e(g_d(n))| <= C/(d lambda).                       (2)

To verify (2), the successive phase increments theta_n=g_d(n+1)-g_d(n) are
monotone and lie in [d lambda/256,1/8]. Put z_n=e(g_d(n)) and
`b_n=(1-e(theta_n))^-1=1/2+(i/2)cot(pi theta_n)`. Discrete summation by parts
in `z_n=b_n(z_n-z_(n+1))` bounds the sum by two endpoint terms plus total
variation of b_n. Monotonicity of cot gives `O(1/(d lambda))`, also for an
interval of one point after enlarging the constant.

For N points, set L=min(N,floor(1/lambda)); if N=1 the conclusion is immediate.
Cauchy--Schwarz applied to the L translated zero-extended copies gives

    |S|^2 <= (N+L)/L [N+2 sum_(1<=d<L) |C_d|]
          <= C (N+L)/L [N+lambda^-1 log(2L)].             (3)

If N>=floor(1/lambda), the right side is
`O(A Lambda+A log(2A))`. If N is smaller, it is
`O(N+(A/Lambda)log(2N))`, at most the same bound for Lambda>=1.
Divide its square root by A and maximize over the subinterval. This proves
(BDE-1). At the prescribed depth, `log A/16<Lambda<=log A`, so (BDE-2) follows.
The expansion Z_n=1/(32n)+O(n^-2) proves the fixed-character assertion directly.

**The first invalid inference exposed.** The radial forcing is
`r_Z=(2r-rsharp)/4=-d/4=-15/(32n)+O(n^-2)`, not the original
`15/(64n^2)+O(n^-3)` forcing. An F4 inequality with the original amplification
`1+C H/A^2` would contradict (BDE-2) and the fixed-h limit one. Its variation
budget cannot be transferred to this channel: the radial completion has
variation of order 1/A, rather than 1/A^2. The original retrieval theorem remains
intact. A demand that the radial source must fail *this particular* ratchet is
therefore a mismatched-source control. It remains a valid hostile control for
height, spectral, Cayley-reference, and coarse-occupancy arguments.

## BDE-2. Existing sparse reset theorem implies the sharp critical obstruction

The parent's `front3/SPARSE_RESET.md` already constructs a single zero-seeded
changed forcing f with arbitrarily long exact authentic prefix, O(log N) changes
through N, positive decreasing injections, exponentially small defects, exact
state denominators and the stated newborn-prime windows. It proves, for fixed
dyadic rational C and c>0,

    V_n=16^n C-T_n+O(exp(-cn)).

For all sufficiently large n, 16^n C is an integer. Uniformly over an epoch,

    |e(H_A V_n)-e(-H_A T_n)|
        <= O(A^2 log A exp(-cA)).

The difference between the two maximal means is at most that same bound
(triangle inequality in both directions). Consequently CC-02 gives, for EVERY
fixed h != 0,

    Lambda_A M_A^V(H_A) -> 256/pi.                        (BDE-3)

This is an explicit corollary of two inherited theorems, not a new construction.
It refutes promotion from those arithmetic/source-window invariants to the
critical little-o estimate. The complete original forcing at every time rejects
the mutant. It does not refute a theorem with that stronger hypothesis.

## BDE-3. One omitted prime can retain the coherent critical threshold

There is also a DIFFERENT single rational changed-forcing source f, V_0=0,
which agrees with any prescribed finite authentic prefix and has all of:

* f_n>0 for all n; f_n=r(n) outside O(N/log log N) reset indices through N.
* f_n=r(n) at every first occurrence of every prime in the genuine forcing
  (including, in particular, every designated 8n-7 prime birth).
* For every n and every prime p != 3, both V_n-U_n and f_n-r(n) are p-integral.
  Thus the complete principal parts in Q/Z_(p), not every p-adic digit, agree.
  The same holds for every lag.
* Every reduced state denominator is exactly authentic. Every intrinsic
  forcing-prefix LCM is exactly Q_N. Only O(log log n) of the least singular
  ternary polar digit positions can differ at time n.
* On each sufficiently large epoch, all but O(A^(3/2)) ordered pairs have
  exactly the authentic reduced difference denominator.
* For every fixed h != 0, simultaneously for this single recurrence,

      |M_A^V(H_A(h))-M_A^(-T)(H_A(h))|=O((log A)^-4),    (BDE-4)
      Lambda_A M_A^V(H_A(h)) -> 256/pi.                  (BDE-5)

This trades away the exponentially small/monotone forcing defects of BDE-2 in
order to preserve all nonternary principal parts at all ages. It does NOT
assert that V itself clusters at the coarse mesh or that its fixed-h means tend
to one. It is a direct obstruction to the critical ratchet from the listed
one-prime-incomplete data. The signed corrections below can instead be centered,
but the nonnegative choice makes positivity immediate.

Construction. Choose a sufficiently large first reset t_0 beyond the requested
prefix with t_0=86 modulo 105. Write

    m_t=floor(log_16 t),
    D_t=largest power of 3 <= m_t^6,
    B_t=largest power of 16 <= t^2,
    K_t=least nonnegative integer with 16^K_t >= D_t.

For the infinite theorem choose t_0 so large that `D_t<8(t-1)/27` for every
t>=t_0. Such a threshold exists because D_t=O(log^6 t). The next reset is

    t'=t+105 max(1,floor(log_16(m_t)/105)).

All resets lie in the same progression. Eventually their gaps are asymptotic to
log_16(m_t), so their number through N is O(N/log log N): there are at
most sqrt N resets below sqrt N, while every subsequent gap is bounded below
by a fixed positive multiple of log log N. Also eventually
`16^(t'-t)<=m_t`. Set e_n=0 between resets, and at reset t form the rational

    x_t=16 V_(t-1)+r(t),
    L_t=sum_(k=1)^K_t 16^-k r(t+k),
    a_t=nearest_integer(D_t B_t (x_t+L_t)),
    k_t in {0,...,D_t-1}, B_t k_t = -a_t (mod D_t),
    e_t=k_t/D_t,  V_t=x_t+e_t,  f_t=r(t)+e_t.

For D_t=1 use K_t=0 and the empty tail. The asymptotic proof uses D_t>1.
The inverse of B_t exists modulo D_t; all operations are rational and finite.
Nearest-integer ties may be broken toward +infinity. No supplied pi digits
enter. This version uses O(log log t) future injections; no causal claim is made.

The tail identity and CC-01 give

    0<T_t-L_t=16^-K_t T_(t+K_t)
             <1/(64 t^2 16^K_t).

Hence the exact reset bound is

    ||B_t(V_t+T_t)|| <= 1/(2D_t)+1/(64D_t)
                       =33/(64D_t).                    (4)

Before the next reset, Z_n^*=V_n+T_n satisfies Z_n^*=16^(n-t)Z_t^*.
For n in [A,2A), its preceding reset has t/A between 1-o(1) and 2, uniformly.
For every fixed h and sufficiently large A, B_t divides H_A(h), because

    H_A(h)/|h| > A^2 log A/(16|h|) > t^2 >= B_t.

Moreover the integer multiplier H_A/B_t is O(log A), since B_t>t^2/16.
Multiplying (4) by this integer and by 16^(n-t), and using
`16^(n-t)<=m_t`, `D_t>m_t^6/3`, gives

    ||H_A(V_n+T_n)||=O(log A * m_t/D_t)=O((log A)^-4).

The Lipschitz estimate for e and the maximal-sum triangle inequality prove
(BDE-4); multiplying by Lambda_A=O(log A) and using CC-02 proves (BDE-5).
The same recurrence works for all h: only the sufficiently-large-A threshold
depends on h. There is no selection of a new mutant after choosing h or A.

Arithmetic protections. At t=86 mod105, 8t-7 is divisible by 3, 8t-3 by 5,
and 4t-1 by 7. Every odd prime in the first/third/fourth raw denominator has
already appeared: a split p first occurs as p in an odd channel at an index
at most (p+7)/8; an inert p first occurs as 2p at (p+1)/4. Except for the fixed
small primes, the displayed proper factors bound p by respectively 8t/3,
8t/5,4t/7, all giving an earlier occurrence. In the second raw denominator
4(2t-1), every odd factor p<=2t-1 first occurs before t by the same formulas.
The prime 2 is never in a reduced original forcing denominator, and no reset
introduces it. Thus no reset is any first-prime birth. Full forcing remains
literal at all such births, not merely its promoted residue.

Every intervention has ternary denominator <=D_t. The D_t are nondecreasing,
so V_n-U_n lies in (1/D_t)Z between t and t', and has no nonternary polar part.
The inherited T1 bound for n>=11, `d3(U_n)>8n/27`, makes this discrepancy's ternary
height strictly smaller than the authentic one. Therefore addition cannot
cancel the leading ternary pole; every state denominator agrees exactly.
The discrepancy also affects only the O(log D_t)=O(log log n) least singular
ternary polar digits. The equality of forcing-prefix LCMs follows either from
`den(e_t)|Q_(t-1)` or from the exact identity that the state-prefix LCM and
forcing-prefix LCM are equal in any integer-radix zero-seeded recurrence.

For pairs in [A,2A), the perturbation of their lag has ternary denominator
at most `D_*=O(log^6 A)`. If `d3(U_n-U_t)>sqrt A`, this perturbation cannot
alter any prime exponent of the reduced gap denominator. The inherited T3
occupancy theorem bounds, for each t, the other indices with
`d3(U_n-U_t)<=sqrt A` by O(sqrt A). Summing yields O(A^(3/2)) possible exceptions.
Their possible normalized tent contribution at q_A is O(q_A/sqrt A)=o(1).
This is an exact denominator assertion outside a quantified set, not a bound
on the realized Archimedean numerator.

## Gaussian/Cayley scope and source ledger

The radial signed estimate BDE-1 distinguishes smooth zero-period radial motion
from the original critical source. It does not use denominator growth. The
one-prime mutant BDE-3 matches all p != 3 principal parts, including every
split-prime component and every inert component other than 3, so any proposed
signed transfer using only those data cannot force the critical little-o.
It does not preserve the full Gaussian source formula, or the omitted 3-primary
numerator. A proof using those finer hypotheses has not been refuted.

The #502 Cayley map and Cauchy reference are lawful coordinate changes. Their
projector overlap and tangent algebraic degree depend only on the reduced
state denominator, and therefore BDE-3 preserves them exactly at each time.
No claim that it has the angular scalar kernel as its full forcing is made.
Likewise exact coarse occupation for U remains open: an interval chart or
reference density does not turn the p-adic occupancy T3 into real occupancy.
