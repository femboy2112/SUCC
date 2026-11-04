# Pair denominators and the real cofactor obstruction

## Object and input

Take the zero-seeded rational angular carrier of PR #499, with taps
`(2,2,1,0,-1/2,-1/2,-1/4,0)` at integer denominators
`8(n-1)+j`, and recurrence `Y_n=16Y_(n-1)+r_ang(n)`. Write
`D(n,t)=den(Y_t-Y_n)` in lowest terms; integer shifts leave it invariant.
All logarithms are natural. In a single epoch let A <= n < t < 2A, d=t-n.
The bounds below are uniform in the indicated indices. Standard inputs are PNT
and the elementary divisor estimate tau(d)=d^{o(1)}. PQ-06's single-state denominator
asymptotic is used only to interpret the typical-pair bound as 8t+o(A).
The uniform top-window result and the quantitative mean bound are independent of PQ-06.

## PS1 (PROVED). Uniform upper-window sieve on the selected differences

For every prime p>5 with 4t < p <= 8t, exactly one denominator in the
source interval [1,8t] is divisible by p: the integer p itself. Its odd
tap is nonzero modulo p, its valuation is -1, and its birth time is
ceil(p/8). Later multiplication by the unit 16 preserves that simple pole.
If p>8n, it occurs in Y_t but not Y_n, so p divides D(n,t) exactly once.
If p<=8n then 16^d Y_n and Y_t differ by a p-integral rational, so
p divides D(n,t) exactly once if and only if p fails to divide 16^d-1.

The total log-weight of lost top primes is O(A^{1/2+o(1)}), uniformly
for every d=1,...,A-1. To see this take R=floor(A^{1/2}). A lost
prime has order r=ord_p(16) dividing d. For each divisor r<=R the
log mass of eligible primes is at most log(16^r-1)<=R log(16).
For each divisor r>R, the primes are 1 mod r; the eligible integers
<=16A number at most 1+16A/R. Multiplication by log(16A) and summation
over the tau(d) divisors of d gives the bound. The divisor estimate follows directly, for every
eta>0, by bounding a+1<=p^{eta a} on all sufficiently large primes p
and absorbing the finite product of sup_{a>=0}(a+1)p^{-eta a} elsewhere.

By PNT, theta(8t)-theta(4t)=4t+o(A), uniformly in the epoch.
Thus the top-window contribution to log D(n,t) alone is **4t+o(A)**,
and all selected phase pairs are distinct for all sufficiently late epochs.
Every such pair avoids every exact rational gap of reduced denominator
<=exp((4-delta)t) for each fixed delta>0, eventually. This is a lower bound
on denominators. A rational with denominator D can be just 1/D from zero.

For q exceeding the epoch's cumulative conductor the circular triangular
energy is exactly q/A (the diagonal only), by distinctness and grid spacing.
This ultrasmall length scale differs from 1/log A by exponentially many scales.

## PS2 (PROVED). Actual-state denominator loss has square-root mean

Let d_t=den(Y_t), and define H(n,t)=log[d_t/gcd(d_t,D(n,t))].
This measures the exact log mass of prime powers present in the selected
state's denominator but missing in the pair difference. Uniformly for each
fixed n in [A,2A),

    sum_{t=n+1}^{2A-1} H(n,t) = O(A^{3/2}).

Proof. All d_t divide 4*lcm(1,...,16A) by the eight-tap representation.
Primes p<=4 sqrt(A), including all higher powers, cost O(sqrt(A)) per t:
there are O(sqrt(A)/log A) such primes and each contributes O(log A).
Larger primes have only simple poles. For one such p write v_t=pY_t mod p,
which always exists. A loss requires p dividing d_t (v_t nonzero) and
v_t=v_n. If v_n=0 there are no losses. Otherwise, divide the later times
into intervals beginning at source p-events (or n+1 at the left
boundary). There are O(1+A/p) intervals because at most 16A/p integer
multiples of p could occur as denominators. Within each interval the
residue evolves by multiplication by 16. A single interval of length L
contributes at most 1+L/ord_p(16) matches with v_n, also valid for
zero intervals where no nonzero match is possible. Summing **lengths**
gives O(1+A/p+A/ord_p(16)) matches over all later t.

For F(x)=sum log p over odd primes p<=16A with ord_p(16)<=x, we have
F(x)=O(A) by Chebyshev, and F(x)=O(x^2) for x>=1 from the product of
16^j-1 over 1<=j<=x. Integrating F(x)/x^2 from 1 to infinity and
splitting at sqrt(A) yields

    sum_{2<p<=16A} log p / ord_p(16) = O(sqrt(A)).

Indeed each indicator of x>=ord integrates against x^{-2} to 1/ord.
Also sum_{p<=16A}(log p)/p=O(log A) by partial summation of
theta(x)=O(x). Thus the prime-log charge for all later t is
O(A + A log A + A sqrt(A)), including the small primes; this proves PS2.
The order-sieve argument is general after the authentic source has supplied
its sparse pole events and conductor bound.

For every u>0, at most O(A^{3/2}/u) later times per n have H>u.
Take u=sqrt(A) log^2 A. Outside that set, the **same prime-power factors**
shared by d_t and D have product at least d_t exp(-u), and the lost set
contributes only O(q/log^2 A) to the symmetric actual epoch tent energy.
For any fixed delta>0, PQ-06 gives log d_t=8t+o(A) uniformly on the
epoch, and the upper bound log D(n,t)<=psi(8t)+O(1)=8t+o(A) follows
from the common conductor. Thus for each n, **all but O_delta(sqrt(A))
later t** satisfy |log D(n,t)-8t|<=delta A. Counting bounds can be
vacuous for n with very few later times; no constants depend on n.

## PS3 (PROVED). The whole generic p-adic principal part can be spoofed at once

For every A choose H=2A, a power 3^L >= A^2 16^H, and s the closest
multiple of 3^{-L} to -Y_H/16^H. Evolve the exact same angular forcing
with initial value s to get Y'_n=Y_n+16^n s. For **every time n**, not only
within the chosen epoch, Y'_n and Y_n have the same class in Q_p/Z_p for
**every p other than 3**. Hence all integer linear combinations have the
same classes there too, including all differences, all pole orders
and every negative-power digit. This does not assert equality of integral
digits or equality of p-adic numbers. Reduced 3-adic height can exceed
the native conductor; this countermodel complements #492's different
native-conductor impostor. The seed depends on the requested finite epoch.

Every true angular force satisfies 0<r_ang(j)<=5/(8j-7):
the positive first tap 2/(8j-7) exceeds the sum of magnitudes of
the three negative taps; the positive weights sum to 5.
For A<=n<H,

    Y'_n = 16^n(s+Y_H/16^H) - sum_{j=n+1}^H 16^{n-j}r_ang(j).

The error in the first term is at most 1/(2A^2) and the positive
sum is at most 5/(15(8A+1)). The entire real orbit in this epoch therefore
lies in an interval of diameter delta_A=1/(3(8A+1))+1/A^2. For q>=2 its
circular triangular energy satisfies J' >= q(1-q delta_A), hence J'/q ->1
when q=O(log A). Consequently all generic local observations above, even at
full time alignment, cannot certify the desired mesh saving uniformly
over rational odd seeds. The original zero boundary distinguishes the two.
An arbitrary selected real signed estimate still needs that boundary.

## Actual remaining cut

Use the circle norm ||x||=dist(x,Z), q=q_A>=2 and e(x)=exp(2pi i x).
For c_A(h)=A^{-1} sum e(hY_n), Fourier series of the periodized tent
gives J=1+sum_{h!=0} sinc(pi h/q)^2 |c_A(h)|^2 (sinc u=sin(u)/u).
The tail beyond q^2 costs O(1) because |c_A|<=1.
Thus the **weighted** truncated moment is equivalent to J=o(K_A) as K_A
tends to infinity. The equally spaced q-cloud has J=1 but amplitude 1
at every multiple of q, invalidating a converse for the unweighted moment.
Take real fractional parts before comparing phases. Using the enormous
unreduced Y_n and ordinary absolute gaps would instead trivially discard
off-diagonal pairs and give a false proof.

Write g_nt/D_nt for a reduced gap modulo 1 with g centered. The diagonal
costs q/A. PS1 removes every eventual exact off-diagonal alias. PS2
removes at most O_delta(A^{3/2}) pairs with atypical log denominator
height at tolerance delta A; their total energy is O_delta(q/sqrt(A))=o(1).
**Thus, at the actual mesh one may discard every low-height outlier
uniformly, at o(1) additive cost.** More sharply one may discard every
pair with H>sqrt(A) log^2 A at O(q/log^2 A) cost, without PQ-06. For each fixed delta>0 it suffices to
bound the tent-weighted count among pairs with |log D_nt-8t|<=delta A.
The unresolved count still depends on |g_nt|/D_nt. No estimate here
shrinks that main contribution below o(K_A). The PS3 preload passes all
generic-prime tests while concentrating the centered numerators.

## Rival ledger and scope

* A single newborn top prime enforces exact distinction. A returning old
  prime at a lag divisible by its order can cancel identically. PS1 counts
  the latter and gives a uniform quantitative repair.
* Full macroscopic denominator growth for most pairs is proved in one
  selected embedding. PS3 is a rational chronological wrong-seed family
  that simultaneously passes the principal-part tests and almost maximizes
  the real defect. This pinpoints the missing centered carry estimate.
* Next falsifier: preregister a proposed bound on the weighted real count
  with near-full denominator height, then run both the selected zero
  seed and PS3 on the same epochs. A route using only the generic
  principal parts must give the same inputs on both, despite their real
  freedom. Full real normality and the true source's logarithmic-mesh
  bound remain OPEN. A plausible route to a bound must also quantify
  dependence on the source-native small-prime height and the literal seed.
* The exact finite arithmetic checks compare polynomial and summed-tap
  forces, predicted prime survival and reduced differences. The 3-power
  control uses no external digits. Preregistration and receipts are local
  provenance. No external referee or academic novelty claim.

References: SUCC PR #499, sections PQ-02, PQ-04–PQ-06 (equations
PQ-4, PQ-9, PQ-12–PQ-15), SHA
4ff640637d18b8161599402f7c6ba23388a63652; PR #491 e21ff757, repaired
Fourier direction; PR #492, source-native rational wrong-seed control.
Classical selected-orbit context: Bailey & Crandall (2001),
https://doi.org/10.1080/10586458.2001.10504441 ; Lagarias (2001),
https://arxiv.org/abs/math/0101055 .
