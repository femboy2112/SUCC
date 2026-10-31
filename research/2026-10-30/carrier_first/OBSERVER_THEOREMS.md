# Finite observers: exact adequacy, finite-horizon transport, and memory cost

Status: local paper proofs using classical contraction, coupling and rational
approximation. No novelty claim. PR414 already proves fiber adequacy and the
stationary KL/entropy identity. Here the added content is an explicit finite
sample transport with resolution and endpoint errors, and an autonomous-state
cost theorem. Neither verifies the missing selected arithmetic bound.

## O1. The least future-refining observation

For a map F:C->C and observation q, define q_L(c)=(q(c),...,q(F^(L-1)c)).
An observation p determines those L outputs exactly iff each p-fiber is
contained in a q_L-fiber. Proof: apply the elementary fiber criterion to the
tuple; conversely read the tuple on each fiber. Thus q_L is the coarsest such
refinement, unique up to relabeling its image.

For T_b(x)={bx}, x in [0,1), greedy coding, q_m(x)=floor(b^m x), the q_L
fibers are exactly the half-open cylinders of length m+L-1. Their number is
b^(m+L-1): overlapping outputs recover all these digits, and these digits
determine every output. A closed deterministic quotient refining q_m must
therefore distinguish all infinite digit sequences, hence all x. There is
no finite closed quotient of the unrestricted carrier preserving even one
digit. This is not a prohibition on a finite-information observer interacting
repeatedly with its carrier; each contact can supply new information.

## O2. A finite empirical branch certificate, without stationarity

Let x_0,...,x_N in [0,1) obey x_(n+1)=T_b x_n, b>=2, N>=1.
Fix k>=0. Let C_(d,v) count n=0,...,N-1 with
d=floor(b x_n), v=floor(b^k x_(n+1)); put C_v=sum_d C_(d,v).
Define the **rational, actual empirical digit transport cost**

    rho_(k,N) = 1/(b N) sum_v sum_(j=0)^(b-2)
                    |sum_(d=0)^j C_(d,v) - (j+1) C_v/b|.

Let mu_N=N^-1 sum delta_(x_n), lambda Lebesgue probability, and use ordinary
interval Wasserstein distance (not its circular variant). Then

    W1(mu_N,lambda) <= [b rho_(k,N) + b^(-k) + 1/N]/(b-1).       (O2)

**Proof.** Use inverse branches f_d(y)=(d+y)/b and the fair operator
P nu=b^-1 sum_d (f_d)_*nu. It contracts W1 by 1/b and fixes lambda.
Let mu_N^+=N^-1 sum delta_(x_(n+1)); W1(mu_N,mu_N^+)<=1/N by coupling
the N-1 common atoms and the two endpoints.
Replace each future y by the midpoint of its length b^-k bin. The actual
joint law of d and future bins and its product with a fresh uniform digit
have the same future-bin marginal. For a fixed v, the W1 distance of their
digit distributions on {0,1/b,...,(b-1)/b} is the sum of absolute cumulative
mass differences divided by b. Averaging gives exactly rho_(k,N).
Undoing both midpoint replacements costs at most b^(-k-1) in total. Thus

    W1(mu_N,P mu_N^+) <= rho_(k,N)+b^(-k-1).

Triangle inequality and contraction give
W1(mu_N,lambda) <= rho+b^(-k-1)+1/(bN)+W1(mu_N,lambda)/b,
which proves O2. No stationarity, stochastic sampling, or independent prime
marginals were assumed. The actual deterministic record supplies C.

For comparison define D_(k,N)=sum_(d,v) C_(d,v)/N log(b C_(d,v)/C_v),
omitting zero terms. Conditional coupling and Pinsker give
rho <= (b-1)/b sqrt(D/2), hence

    W1(mu_N,lambda) <= sqrt(D_(k,N)/2)
                     + [b^(-k)+1/N]/(b-1).                    (O2a)

The empirical sampling floor is explicit:

    D_(k,N) >= sum_(v:C_v>0) (C_v/N) log[b/min(b,C_v)].        (O2b)

Indeed each conditional distribution has at most min(b,C_v) nonzero cells,
so its entropy is at most log min(b,C_v). If every future bin is a singleton,
D=log b exactly. Taking unlimited future precision in a finite record thus
cannot be substituted for the invariant-law conditional entropy of PR414.

## O3. Application to the authentic source, with the unproved input exposed

Use precisely U0=0, U_n=16U_(n-1)+4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).
The positive future correction T_n has sum_(n>=1)T_n<1/32: the regrouping
r(n)=6/[a(a+3)]+4/[a(a+4)]+5/[a(a+5)], a=8n-7, gives
T_n<(8n+1)^-2<1/(64n²), and sum n^-2<2. The completed states
y_n={U_n+T_n}={16^(n-1)pi} obey the exact radix law. Apply O2 to
x_j=y_(j+1), and write B=[16rho+16^-k+1/N]/15. Then, for integer h!=0,

    |N^-1 sum_(n=1)^N e(hU_n)| <= min(1,2pi|h|[B+1/(32N)]). (O3)

This follows by testing against the 2pi|h|-Lipschitz periodic character and
paying the actual Green-tail chord error before reducing modulo one. Thus
there is no unlicensed interval-W1 estimate across the circle seam.
For integer H>=2 the selected Fejer energy also satisfies

    F_(H,N) <= min(H,1+(2pi²/3)H(H²-1)[B+1/(32N)]²).         (O3a)

The coefficient uses sum_(|h|<H)(1-|h|/H)h²=H(H²-1)/6.
These are proved conditional finite estimates with actual empirical inputs.
**No theorem here makes rho small for the authentic source at unbounded N.**
Even a fixed-frequency useful upper bound needs a nontrivial bound on rho.
Moving k with N is constrained by O2b; the missing source-to-record estimate
has not been replaced by a fair auxiliary model.

## O4. Selected autonomous-state cost (not digit entropy)

A clockless deterministic Moore emitter consists of S internal states, one
initial state, a fixed transition on states, and one base-b output per state.
No uncounted external clock, oracle or input is permitted. If it emits the
first N digits of an irrational alpha satisfying

    |alpha-p/q| >= c q^(-mu) for all integers p, q>=1,

then

    S >= (N+log_b c)/mu.                                    (O4)

Proof: the infinite output of such an emitter has preperiod a and period p
with a+p<=S. Its rational value beta has denominator dividing b^a(b^p-1),
hence denominator <b^S. Agreement on N digits gives |alpha-beta|<=b^-N,
including possible alternate rational expansions. Combining the inequalities
proves O4. If the emitter has more states than observed positions the same
bound is trivial after replacing c by min(c,1). Rational affine changes
preserve finite irrationality exponent, with a changed positive c.

The published Zeilberger--Zudilin 2020 bound mu(pi)<15/2 therefore gives

    S_N({pi}) >= (2/15)N-O(1)

for the original completed BBP digit record. This is an actual selected
boundary distinction: the coherent seed completes to zero and needs one
state; rational aliases of the authentic boundary retain the lower bound.
The constant in O(1) is not numerically certified here. The number of memory
bits required is only at least log2 N-O(1), not a linear number of bits.

This elementary consequence is not a new irrationality or normality theorem.
The nonnormal beta_3=sum_(j>=0)16^(-3^j), whose exponent is3 by the exact
determinant-separation proof in PR405 DP03, also has linear autonomous-state
cost and coherent limiting Weyl averages. Thus linear state cost is decisively
insufficient for dispersion. An algorithm with a growing integer clock is
outside the fixed finite-state model, not a counterexample to O4.

For any finite word w of length N the exact minimal S is

    min_(1<=p<=N) max(p,1+max{i>=p:w_i != w_(i-p)}),          (O4a)

where the empty maximum is p-1. For a candidate p, choose a=S-p; its suffix
is p-periodic iff no mismatch occurs at i>=a+p. This proves both directions,
and supplies an executable independent prefix check.

## Controls and authority

Constant and periodic carriers, full-support biased laws, periodic de Bruijn,
and source-modified null systems obey O2. That universality makes it an
instrument, not a source-selection certificate. A period-(k+1) de Bruijn cycle
has D=0 at depth k but remains nonnormal; its small W1 is allowed by the
explicit resolution remainder. Negative source/seed examples do not refute
the exact original BBP realization. The rational state API retains clock,
integer lift, source label and literal carries separately from completed words.

Classical sources checked live: [Cousot and Cousot 1992](https://www.di.ens.fr/~cousot/COUSOTpapers/JLC92.shtml)
for abstraction provenance; [Zeilberger and Zudilin, published 2020](https://msp.org/cnt/2020/9-4/moscow-v9-n4-p06-p.pdf)
for the only external Diophantine input. No 2026 exponent claim is used.
Read-only PR414 e4773979802cf0ef3a8d46444acb6bc5966788a9 supplies the
stationary theory; PR405 6cf5050ff2cfd92e7a0c8876da5233be6ff117f5 supplies
the sparse control. Independent code below means separate implementations,
not independent mathematical authority or a new Lean theorem.
