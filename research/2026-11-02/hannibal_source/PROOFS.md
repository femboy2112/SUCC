# Hannibal: actual near-pair exclusions, with the unpaid core retained

Parent: PR #476, `1478b51cf1370411aea6ec42c09d080598384528`.
These are paper proofs, not compiled Lean theorems. Pi normality is OPEN.
No external scholarly priority claim. In particular, the Diophantine method
below is classical and shares ancestry with the repository's logarithmic
coherence-loss arguments. Parallel #472 was read, not imported or merged.

## Contract and dependencies

For every integer n>=1 retain

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U0=0, U_n=16 U_(n-1)+r(n),
    X_n=16^n*pi/16, T_n=X_n-U_n, 0<T_n<1/(64n^2).

Distance ||x|| is distance to the nearest integer; e(x)=exp(2*pi*i*x).
All actual rational phases and literal carries below use this source. The
target remains sum_(n<=N)e(hU_n)=o(N) for EVERY fixed h!=0 and ALL N.

The four-pole identity implies, for n>=1,d>=1,

    0<f_(n,d):=r(n+1)-r(n+d+1)<15/(64n^2).             (H0)

Positivity follows from the inherited exact integral
r(n+1)=integral_0^1 t^(8n)(1-t)(4+4t+4t^2+2t^3+t^4)dt.
The upper bound is WM-05's positive polynomial certificate. T_n decreases
strictly, either by its positive integral or its positive decreasing series.
These inputs were proved in the ancestor source/lag and mirror dossiers;
they are dependencies, not new independent corroboration.

## Phase 0: hostile WM-01 through WM-08 audit

| Claim | Verdict and check | Restriction retained |
|---|---|---|
| WM-01 | SURVIVES: B(1/t)=1/B(t); rotate the forced dynamics as well | Conjugates sum to 2 cos, not zero |
| WM-02 | SURVIVES: commuting Mobius maps preserve {0,infinity}; reflection requires c^15=a_n^-2; 2(r2-r3)=133558/765765 | Only a fixed Mobius centralizer is excluded; no approximate/time-reindexed prohibition |
| WM-03 | SURVIVES: combine both even poles to -(3n-1)/((2n-1)(4n-1)) | Odd denominators forbid exact pairs, not approximate pairs/polygons |
| WM-04 | SURVIVES: TJ=J0T, JJ0=R_(1/16), then Fourier radix reduction | Original empirical J-invariance is unproved |
| WM-05 | SURVIVES: primitive determinant >=1/8; telescope Ward at h=16^v*g | Never divide when 16 divides h; Ward is valid for changed seeds too |
| WM-06 | SURVIVES: nonnegative pair kernel dominates every subset; ladder shift error <=2k | PSD alone fails; no cancellation inferred from positivity |
| WM-07 | SURVIVES: squared tail-norm error <=pi^2*m^3/(12288*A^4); arbitrary partial epochs and dyadic gluing | Required denominator is log m, not log A |
| WM-08 | SURVIVES: 2S=sum paired characters and chord bound gives pi*c | Finite feasible matchings are not source-derived asymptotic rules |

The principal read the complete proofs and antecedents #451/#453/#474/#475.
A separate agent reconstructed the WM/MSA constants and implications, with
exact finite sanity checks. This is a separate reasoner pass on one shared
source lineage, not a blind external referee or independent source family.
No defect requiring an ancestor edit was found. Frozen files are untouched.

## H-01: annular near-pair bound on every original epoch

**Theorem (paper proved, forcing-derived).** For ALL integers A>=64,
64<=m<=A, let K=floor(log_16(m/4))>=1. For each integer 1<=d<A,

    H_d := #{A<=n<2A-d: 1/(8m)<=||U_(n+d)-U_n||<=1/m}
          <= ceil((A-d)/(K+1)).                       (H1)

Both annulus endpoints are included. More precisely, any shell hit at n
forces the next K lag positions outside the CLOSED radius-1/m arc.

**Proof.** Choose the initial centered representative delta in [-1/2,1/2).
The unwrapped q-step affine value is

    z_q=16^q*delta-F_q,
    F_q=sum_(i=0)^(q-1)16^(q-1-i)*f_(n+i,d),
    0<F_q<(16^q-1)/(64A^2).                         (H2)

It represents the actual lag modulo one: subtraction of the two original
recurrences proves this, including their integer carries. For 1<=q<=K,

    |z_q| < 16^q/m + (16^q-1)/(64A^2)
            < 1/4+m/(256A^2) < 1/2.

Thus z_q IS the centered representative; no wrap or branch assumption has
been omitted. If delta<0, |z_q|>16^q/(8m)>=2/m. If delta>0, since m<=A<=A^2,

    z_q > 16^q*(1/(8m)-1/(64A^2))
          >=7*16^q/(64m)>=7/(4m)>1/m.

Consequently successive shell starts are separated by at least K+1. There
are A-d admissible starts, proving (H1).

Writing A-1=a(K+1)+b, 0<=b<K+1, the ordered shell count obeys the exact bound

    H_ordered <= (K+1)a(a+1)+2(a+1)b
              = 2 sum_(L=1)^(A-1) ceil(L/(K+1))
              = O(A^2/log m).                        (H3)

An observed shell hit additionally certifies min(K,2A-d-1-n) actual excluded
future starts inside the epoch. These exclusion packets are disjoint for a
fixed d. If their total is B_d, the total radius-1/m lag count satisfies
V_d<=A-d-B_d. `annulus_census` records B_d and all clipped endpoints exactly.

**Coverage and exceptional set.** The entire strict inner core

    C_inner=#{(n,t) in [A,2A)^2: ||U_n-U_t||<1/(8m)}

is unpaid, including the A diagonal pairs. Exactly
P_(A,m)=C_inner+H_ordered. No positive fraction of actual pair mass is known
to lie in the shell. At m~log A the shell ceiling is O(A^2/log log A), itself
larger than the requested o(A^2*log log A/log A). Iterating shells does not
repair this: the finer-core mass and accumulated errors have no small bound.
The explicit slow mesh first reaches 64 at j=64 (A=2^64). The finite annulus
census therefore uses the preregistered auxiliary meshes 64 and 256; it does
not pretend that the new slow-mesh observations m=8,16 exercise K>=1.

**Hostile control.** The SAME forcing with seed 1/5-pi/16 gives
U_n*=16^n/5-T_n modulo one. For n,t>=A its lag distance is
|T_n-T_t|<1/(64A^2)<1/(8m). All pairs occupy the unpaid core and H-01 still
holds. This theorem is not a zero-seed discriminator. Its new delivery is
an explicit temporal exclusion/count budget, not a normality criterion.

## H-02: original-selected exclusions for every lag on a dilated window

**Theorem (paper proved, original source).** For EVERY fixed integer h!=0,
there exists A0(h) such that for ALL integers A>=A0(h) and ALL integers
64<=m<=A, with k=floor(log_16(m/64)),

    #{(n,t) in [A,32A)^2: m||h(U_t-U_n)||<=1}
       <= (31A)^2-2A(k+1).                           (H4)

For EACH lag 1<=d<=A there are at least k+1 distinct excluded unordered
pairs, in a consecutive backward packet; both endpoints lie in [A,27A].
The onset is existential; no numerical A0 is asserted.

**External input with its exact quantifiers.** Zeilberger and Zudilin,
*The irrationality measure of pi is at most 7.103205334137...*, corrected
v2, arXiv:1912.06345v2, Moscow J. Comb. Number Theory 9 (2020), 407–419,
proves a bound strictly below 8. We use ONLY its consequence

    exists Q0: forall q>=Q0, forall p in Z,
                  |pi-p/q|>q^-8.                    (H5)

This also holds for unreduced fractions: large reduced denominators use the
theorem; finitely many bounded reduced denominators near pi have a positive
minimum distance, while fractions outside a fixed neighborhood are harmless.
No average over p,q, exceptional source set, or uniformity in growing h is
assumed. This classical input is not a new pi irrationality result.
Primary source checked: https://arxiv.org/abs/1912.06345v2 .

**Proof of uniform lag coverage.** Fix h. For each d=1,...,A put

    q=|h|(16^d-1)16^(2A-1), so q<|h|16^(3A-1).

Suppose ||q16^j*pi||<=1/32 for EVERY j=0,...,24A. Choose nearest integers
b_j, errors epsilon_j=q16^j*pi-b_j. Then
|b_(j+1)-16b_j|=|16epsilon_j-epsilon_(j+1)|<=17/32<1,
so the integer is zero and epsilon_j=16^j epsilon_0. Hence

    |q*pi-b_0|<=16^(-24A)/32<q^-7                  (H6)

for all sufficiently large A, uniformly in d. For example the strict second
inequality follows once |h|^7/32<16^(3A+7). Also q>=15|h|16^(2A-1), so Q0
is reached uniformly. Equation (H6) contradicts (H5) multiplied by q.

There is therefore a t in [2A,26A] with
||h(X_(t+d)-X_t)||>1/32. Since ||16^j x||<=16^j||x||,
for j=0,...,k,

    ||h(X_(t-j+d)-X_(t-j))||>1/(32*16^j)>=2/m.

Here k<=A, so all packet starts are >=A. The original decreasing tail pays

    |h| |T_(t-j)-T_(t-j+d)|<|h|/(64A^2)<1/m

once A>|h|/64, uniformly in m<=A. Every corresponding ORIGINAL lag is
strictly farther than 1/m. Endpoints are <=t+d<=27A<32A. Within each lag the
k+1 pairs are distinct; different positive lags cannot duplicate an unordered
pair. Counting both orientations excludes 2A(k+1) ordered pairs, proving H4.

**What was gained and what was not.** This pays an actual selected-real
exclusion budget Omega(A log m), simultaneously for a dense family of lags.
The remaining budget is still almost (31A)^2. It gives NO upper bound of
the required order on [A,2A), NO all-prefix Weyl decay, and NO improvement
of the ancestor logarithmic Fourier-coherence deficit: the backward packet's
chord sizes decrease geometrically. It is a limited arithmetic consequence,
not a rebranding of the target as an assumed premise.

**Source discriminator.** For changed seed 1/5-pi/16, all completed lag
differences are integers and all original lag distances in this window are
<1/(64A^2). That control violates H4 for h=1 and large A. The proof's q*pi
step uses the actual zero-seed completion; it is unavailable for that control.
Finite irrationality measure is not a normality theorem; this corollary is
not claimed to characterize pi or to exclude every nonnormal changed seed.

## H-03: carry and finite-cylinder mirror bookkeeping

For B=16^ell, ell>=1, let I_a=[a/B,(a+1)/B), 0<=a<B. Exactly on the circle,

    J(I_a)=((B/16-a-1)/B,(B/16-a)/B].                 (H7)

The open/closed endpoint reversal is essential. Nonboundary points therefore
map to cylinder index B/16-a-1 modulo B. The endpoint a/B maps to the RIGHT
endpoint (B/16-a)/B; interpreting both intervals as half-open would be false.

For x_n={U_n}, write B*x_n=a_n+u_n, 0<=u_n<1. The authentic finite-cylinder
recurrence, including the carry, is

    a_(n+1) = 16a_n+floor(16u_n+B*r(n+1)) mod B.      (H8)

At equality the floor chooses the upper cylinder. This follows by scaling
the literal source step; `literal_carry_relation` verifies the same map on
exact states. Neither (H7) nor (H8) assigns equal weights to inverse branches.
For centered lag differences retain
kappa=c_(n+d+1)-c_(n+1)+eta_(n+1,d)-16eta_(n,d), where eta centers the raw
phase difference. Dropping eta is the inherited exact n=1174,d=130 failure.

These bookkeeping identities support the audits, not a new asymptotic
mirror estimate. The measured W_N and antiphase costs remain finite evidence.
For the finite matching, sort pairs (h*U_n mod1,n), rotate the ranks by N/2,
and map back to time indices. At even N this is an involution covering every
time exactly once, with unmatched mass zero. The receipt hashes that actual
permutation and encloses its exact rational cost; (22/7) times the outward
upper endpoint is a rigorous finite Weyl ceiling. Rank fitting is explicitly
not an arithmetic explanation of an all-horizon vanishing cost.

## H-04: failed shortcuts and exact controls

The proposed deterministic IID-mean ceiling E<=1+(m-1)/A is a falsifiable
candidate, with development counterexamples retained in FINITE_RECEIPT.json.
The IID expectation is not a deterministic bound even for random samples.
Its failure does not refute the much weaker target E=o(log m).
For example ORIGINAL A=256,m=8 has counts
[33,28,42,28,36,36,26,27], so E=4209/4096>4208/4096=1+7/256.
This is an exact source counterexample, not an iid simulation. Early A=2,16
also fail; these development failures are not hidden by the fresh declarations.

Prime-clock/cofactor locking is retained explicitly: choose original clean
p=41, times 8..15, a_n=4*16^(n-6) mod41, and C_n=U_n-a_n/41. Its denominator
is coprime to 41. Replacing C_n by -round(Q*a_n/41)/Q, Q=1009, keeps that
denominator property but puts every selected phase within 1/(2Q) of zero.
The new source is different; no averaging theorem for these clocks controls
the original C_n. In particular the usual arithmetic large sieve cannot be
applied merely by calling time samples distinct residues: its separated
sampling points/weights and required averaging are not supplied here.

Exact tests cover coherent delta_0, uniform 15th roots (h=15 coefficient 1),
conjugate +/-1/6 (mean 1/2), antipodal positive pairing, finite-history mutants,
the cofactor lock, PSD matrix [[1,-1],[-1,1]] with full sum zero/subset one,
and rational mirror resonance 16|h. No floating sign is a proof receipt.

## Dependency DAG and verdict-changing discriminator

    authentic four poles + U0=0 -> exact rational states/carries
    authentic forcing --------> H0 -> H-01 annulus count
    BBP completion + H5 ------> H-02 dense-lag exclusions
    original tail ------------> H-02 transport to actual U
    original bin energy ------> WM-06/07 -> all-prefix Weyl -> normality
           ^
           | E_A=o(log m_A), m_A=max(2,2^floor(log2 j)), A=2^j
           | OPEN: neither H-01 nor H-02 supplies this arrow

Front A is unresolved after an actual annulus/count attempt and exact source
probes. Front B has exact endpoint/carry identities and finite W_N, no decay.
Front C has finite feasible permutations, no source-derived vanishing budget.
Front D has no new signed contraction; no spectral gap or seed average is
asserted. Front E provides executed exact oracles and hostile controls.
Front F keeps this ledger and the core exceptional mass explicit.

The next discriminator is to bound the ACTUAL positive Green-tracking core
and its entries, jointly over lags. An upgrade must pay both that core and
the shell at o(A^2 log m/m), or yield a directly signed source estimate.
The annulus result itself cannot be promoted by another change of basis.

| ID | Status | Provenance/contact | Boundary / next probe |
|---|---|---|---|
| WM audit | DISCLOSED paper audit | Shared ancestors; principal plus separate reasoner | No original asymptotic premise proved |
| H-01 | DISCLOSED paper inequality | Exact source forcing and rational tests | Core wholly unpaid; test entry frequencies |
| H-02 | DISCLOSED paper inequality | Zero-seed BBP + classical H5 | Dilated window, existential onset, sparse exclusions |
| H-03 | DISCLOSED exact identities | Original carries and cylinder endpoints | No empirical symmetry; count matching cylinders |
| IID ceiling | REFUTED when exact receipt says false | Original rational data; development selection | Stronger than requested target |
| Finite receipts | OBSERVED exact finite results | Three code paths, one source family | Same-team declaration; not asymptotic evidence |
| E_A=o(log m_A), W_N->0, signed decay | UNVERIFIED / OPEN | No source-specific full bound | Required for target conclusion |
| Pi normality | OPEN | No status promotion | No compiled proof or external referee claimed |

Epistemic audit: kappa/contact is the literal source with full rational
embedding; sigma/source correctness is checked by independent evaluation
paths and controls. Phi/survival of finite tests is not truth for infinite
quantifiers. Rho/mission pressure does not alter claim status. All computational
routes share the same arithmetic source, so their count is not independent
source corroboration. No physical quantum interpretation is used.
