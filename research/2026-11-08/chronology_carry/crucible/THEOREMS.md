# Causal carry prediction: timing, unavoidable residuals, and source selection

**Status: PROVED PAPER, with exact finite controls.** These are supporting
observer and adversarial results. They do not prove cancellation for the
literal zero seed. General mathematical novelty is not claimed.

The source remains

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U_0=0, U_n=16U_(n-1)+r(n).

Write C_n=floor(U_n), x_n=U_n-C_n and
kappa_n=C_n-16C_(n-1). This is the **literal chronological carry**, not the
different critical triple carry in `observational_succ.selected_orbit`.
Every complex phase below uses e(t)=exp(2 pi i t) in one fixed frame.

## HCP1. A future carry is a high-quality phase measurement

The exact identity is

    kappa_(n+1)=floor(16 x_n+r(n+1)).

Consequently a known next carry restricts x_n to the half-open interval

    [ (kappa_(n+1)-r(n+1))/16,
      (kappa_(n+1)+1-r(n+1))/16 ) intersect [0,1).

For D>=1, let F_D(n)=sum_(j=1)^D 16^(D-j) r(n+j), and
K_D=sum_(j=1)^D 16^(D-j) kappa_(n+j). Exact unwrapped transport gives

    x_(n+D)=16^D x_n+F_D(n)-K_D.

The D future carries therefore locate x_n in an interval of length at most
16^(-D). Its midpoint phase estimates e(h U_n) with absolute error at most
pi |h| 16^(-D), by |e(u)-e(v)|<=2 pi |u-v|. Additional intermediate
constraints may shorten that interval. No stochastic assumption is used.

Thus a high score from a supposed current-time predictor using
kappa_(n+1), or a still later carry, can be direct target leakage. A causal
current-time feature must use indices <=n. This does not forbid future
observations in a declared retrospective observer; it changes the theorem
being tested. The full known zero source permits exact replay at any time,
so an information lower bound cannot be asserted for that singleton carrier.

## HCP2. Full past carry memory can leave an almost full circle unresolved

Fix base b>=2, D>=1 and arbitrary real affine forcing f_1,...,f_D. For an
unknown starting circle coordinate y in [0,1), define

    V_j(y)=b^j y+R_j, R_0=0, R_j=b R_(j-1)+f_j,
    kappa_j(y)=floor V_j(y)-b floor V_(j-1)(y).

Retain the entire carry transcript through D. Let g be any complex-valued
function of that transcript, and let h be any nonzero integer. With Lebesgue
measure on y,

    integral |e(h V_D(y))-g(kappa_1,...,kappa_D)| dy
       >= beta_(b,D),
    integral |e(h V_D(y))-g(kappa_1,...,kappa_D)|^2 dy
       >= beta_(b,D),

where

    beta_(b,D)=1-(1+b+...+b^(D-1))/b^D
              =(b-2)/(b-1)+1/((b-1)b^D).

**Proof.** The last floor map partitions [0,1) into at least b^D-1 full
intervals of length b^(-D), plus possibly two endpoint pieces. For each
j<D the earlier floor map has at most b^j internal boundaries. Remove
every full final interval that contains any earlier internal boundary.
At least b^D-1-sum_(j=1)^(D-1)b^j full intervals remain. On each, the entire
transcript is constant and {V_D} runs affinely once through [0,1).

For a unit-circle uniform phase z, integral|z-c|>=1 for every complex c:
the integral is convex and rotation invariant as a function of c, so its
value at the rotation average c=0 is minimal. Equivalently average the
triangle inequalities for all rotations before integrating. Also
integral|z-c|^2=1+|c|^2>=1. Nonzero integer h preserves this uniform law.
Each retained interval therefore contributes at least its length to both
integrals. All omitted contributions are nonnegative. QED.

For b=16 the lower bound is 14/15+1/(15*16^D), regardless of how much past
memory is stored. Integer forcings give a sharper value1: all b^D final
cells are full and the current phase is exactly independent of its past
digits. The displayed lower bound is not claimed optimal for general
noninteger forcing.

This is an **ensemble obstruction to a uniform prediction principle**.
It is not a claim about the empirical time average of the selected zero
seed. The theorem also does not bound a folded residual from below:
folding can cancel individual prediction errors.

## HCP3. The authentic late forcing strengthens the ensemble floor to 1-o(1)

Start a window at integer t>=1, with its initial circle coordinate y uniform
on [0,1). Use the authentic forcing f_j=r(t+j), for 1<=j<=D. This is a
deliberate same-forcing seed family, not a replacement for the literal zero
source. Known times, the forcing and deterministic clock labels may be
included in g; additional measurements of the unknown y may not.

Put

    T_j^(D)=sum_(k=j+1)^D b^(-(k-j)) f_k, 0<=j<=D,
    eta=sum_(j=0)^(D-1) T_j^(D), b=16.

Then, uniformly in D and every function g of all D past carries,

    integral |e(h V_D)-g(kappa)| >= 1-2 eta,
    integral |e(h V_D)-g(kappa)|^2 >= 1-4 eta,
    eta <= (1/15)sum_(k=1)^D r(t+k) < 1/(15t).

Bounds below zero can be replaced by zero. Predictions may be projected to
the closed unit disk: this decreases distance to every unit target, so it
suffices to prove the estimates when |g|<=1. If an ideal ordinary digit
word is absent from the literal carry domain, extend g to it by any value
in that disk. This does not change its actual loss.

**Proof.** Define the finite corrected ancestor
xi=y+R_D/16^D. Then

    Z_j=16^j xi=V_j+T_j^(D), Z_D=V_D.

Its ordinary digit carries d_j=floor Z_j-16 floor Z_(j-1) depend only on
the first D base16 digits of {xi}. The current phase e(h Z_D) is uniform
and independent of that finite digit word: on each interval
[w/16^D,(w+1)/16^D), substitution u=16^D xi-w proves this directly.
Translation makes {xi} uniform. Hence the ideal digit predictor has L1
loss at least1 and squared loss at least1, by HCP2's circle calculation.

Let B_j=floor Z_j-floor V_j. Since 0<=T_j^(D)<1, and {V_j} is uniform,
Pr(B_j!=0)=T_j^(D). Also B_D=0. The identity

    d_j-kappa_j=B_j-16B_(j-1)

shows the two entire carry words agree unless at least one B_j is nonzero.
The probability of a mismatch is at most eta. For |g|<=1, each loss is in
[0,2], or [0,4] after squaring; replacing the input word changes its
expected loss by at most2 eta or4 eta. This proves the first two bounds.

Finally, interchange the finite sums:

    eta=sum_(k=1)^D r(t+k) sum_(ell=1)^k 16^(-ell)
       <=(1/15)sum_(k=1)^D r(t+k)
       <(1/15)sum_(k=t+1)^infinity k^(-2)<1/(15t).

The strict source bound 0<r(n)<1/n^2 for n>=2 is the inherited four-pole
bound; it also implies every T_j^(D)<1. QED.

**What this changes.** Increasing past memory does not produce a generic
predictability advantage under the same late forcing. A successful
zero-source carry predictor must exploit an independently proved
source-selected relation. This supplies an explicit benchmark and a
source-map warning; it proves no lower residual for the single zero orbit.
It must not be used to reject a successful finite zero-source measurement.

## HCP4. Exact finite carry matching permits opposite future phases

For the literal source prefix through J, let

    sigma_J=min_(0<=j<=J) (1-{U_j(0)})/16^j >0.

The inherited exact carry-cylinder theorem says that C_0=0 and all carries
through J agree exactly with the zero source iff 0<=s<sigma_J. Choose N>=J
such that 16^N sigma_J>=1. Then s_0=0 and
s_1=1/(2|h|16^N) both belong to that fiber, and their time-N h-phases are
exact negatives. Any estimator constant on the fiber has worst-case error
at least1. Choosing the center0 attains1 once the phase image covers the
circle, which occurs under the displayed condition. Thus the minimax
complex-plane radius is exactly1 in this regime.

Odd denominators and any finite set of local arithmetic tests do not repair
this observer statement. Fix K>=0 and a finite set P of odd primes. Choose
M a positive multiple of 2^K product_(p in P)p, and set

    q=2|h|16^N M+1, s_1=M/q.

Then q is odd, q=1 modulo every p in P, gcd(M,q)=1, and
0<s_1<1/(2|h|16^N)<=sigma_J/2. The seed therefore preserves the entire
prefix, has v_2(s_1)>=K, and is p-integral at every p in P. Its difference
phase from zero is within 1/(2q) turns of a half-turn. The squared minimax
radius for just these two candidates is at least1-5/(2q^2), using pi^2<10.
Both are rational same-forcing sources; they are not both literal-zero
sources. The nonzero seed introduces additional denominator support.
An exact zero tag, or a complete source-support requirement, rejects it.

This refines the old carry-cylinder obstruction into a phase-prediction
receipt. It does not turn horizon-dependent seeds into one fixed nonnormal
rational seed. No claim is made about the seed1/5.

## HCP5. Honest accounting for a frozen predictor, and the remaining gap

On a clean clock of m states and q replicas, define

    f_r=(1/q)sum_(j=0)^(q-1) e(h U_(n_r+jm)),
    F_r=(1/q)sum_j g_h(history_(n_r+jm)),
    a_r=e(h x_r/p), B_r=conj(a_r)f_r, V_r=conj(a_r)F_r.

Here g_h has been frozen using earlier data and accesses only the declared
current/past carries on the holdout. Then

    W=mean f, rho=mean|f-F|=mean|B-V|,
    |W|<=|mean F|+rho.                                  (HCP5)

This is a deterministic inequality; train/holdout separation licenses no
probabilistic confidence interval without an additional model.

If V is put through canonical zero-extension Fourier analysis, QCO4 yields
the retained resonance (m/p)mean F and total quotient certificate

    K_p |mean F|, K_p=(m/p)(1+beta sum_O|G_O|)>=1,
    beta=min(1,sqrt(p)/m).

Thus the arithmetic certificate is rho+K_p|mean F|. It is valid and does
not directly read the holdout target W, because F was independently
constructed. But for this particular representation it is never better
than HCP5's direct predictor certificate rho+|mean F|. A finite numerical
saving over the original atomwise cost is not extra arithmetic cancellation.
The next useful theorem must independently bound the selected-source rho
and mean F, or use a genuinely different noncanonical representation with
cheaper signed orbit sums. Small training error alone supplies neither.

Do not apply HCP3 to rho: q-fold cancellation can make rho much smaller
than the mean individual error. Conversely a small rho alone does not
prove cancellation: F_r=f_r=1 gives rho=0 and W=1. The coherent inverse
B=conj(a) is the exact finite hostile control. The real same-forcing seed
s_*=-pi/16 approaches this coherent phase by the authentic Green tail,
but has no canonical rational p-principal part in this framework.

## Proof-chain and provenance audit

The inherited all-epoch chain was read at starting head
`19d98078b60e47092c9b9d050a70b6b7eabb7cd2`; fetched main was
`43a607818907120d4cdab73d240f5b4d7700b63f`.

1. The clean clock is the authentic p-principal component only between its
   declared pole births. A periodic extension outside that lifetime is a
   comparison carrier and cannot silently replace it.
2. QCO1 requires a genuinely proved character weight for each full atom.
   Multiplying by an arbitrary carry-cell indicator changes the atom. A
   free Weil bound for that masked phase is invalid without further proof.
3. The original covariance and Weyl means differ by the product of the
   local and complementary means. The proved local marginal decay makes
   covariance decay and Weyl decay equivalent for every fixed h!=0.
4. Every sufficiently large integer epoch A must be covered. Decay on only
   the selected finite test clocks, or only A=2^j, does not give the stated
   prefix theorem. The archived sign-halves bounded-sequence counterexample
   explicitly refutes the dyadic-only weakening.
5. The signed lag gate uses exact F_ell(n), H_A<=m_A, H_A->infinity and
   H_A=o(A). Discarding F_ell requires the archived exponential aperture
   error. A large-aperture E_H->0 result alone can be false evidence even
   for f=1. These conditions survived the present paper audit.
6. Green-tail transport gives the exact original-source phase difference;
   Weyl equidistribution gives all hexadecimal word frequencies. No new
   gap was found in these downstream reductions under their stated
   quantifiers. The original-zero signed bound remains the unpaid step.

Actual sources inspected, all read-only:

- [QCO1--5](../../frontier_connections/crucible/THEOREMS.md): signed clock
  quotient and linear-equivariant rank-one selector obstruction.
- [C1--3](../../covariance_forge/crucible/THEOREMS.md): rational source
  isolation, sharp finite carry cylinders and precision horizon.
- [CH3--7](../../signed_covariance_round2/chronology/THEOREMS.md): local
  digit histories, inverse-limit discipline and local prime leakage.
- [H1--6](../../signed_covariance_round2/hostile/THEOREMS.md): signed
  energy, exact forcing transport and all-epoch equivalence.
- [EC1--4](../../signed_covariance_round2/EXPLICIT_CLOCKS.md): quantitative
  selected clocks and explicitly retained asymptotic overhead.
- [Earlier finite carry experiments](../../covariance_forge/EXPERIMENTS.md):
  failure of a different, same-window Hilbert projection certificate.

The new train/transfer experiment is distinct from those earlier tests;
shared source, model family and inherited inequalities are counted once.
The present results concern observer fibers and source-faithful controls,
not physical nonlocality or mathematical randomness of pi.

**Original-zero signed covariance: OPEN. Pi base16 normality: OPEN. RH: OPEN.**
