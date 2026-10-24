# Infinite selection and the selected occupation law

Date: 2026-10-24. Parent: PR #272 at 6e8fa8b77886b13f1f533ed8083fd88c849d14b3.
Authority: paper proofs and exact finite controls; no new formal-kernel or
academic-priority claim. Pi normality remains OPEN. The circle has circumference
one and geodesic diameter one-half. W1 uses this metric. Probability TV distance
is half the L1 difference; signed-measure TV norm is full total variation.

Exact source identification is already available. This dossier asks whether
increasingly exact selection commutes with averaging indefinitely many
observations, and states the precise infinite signed-measure convergence gate.

## 1. A sharp finite-to-infinite selector theorem

### 1.1 Exact base-b cylinder theorem (PROVED)

Let b>=2, x in the circle, and let I_k(x) be the canonical half-open base-b
cylinder of depth k containing x. Let lambda be Haar probability and

    nu_(x,k) = b^k 1_(I_k(x)) lambda.

The cylinders decrease to x, so nu_(x,k) converges weakly to delta_x as k
increases. Define, for N>=1,

    mu_(N,k) = (1/N) sum_(n=0)^(N-1) (T_b^n)_* nu_(x,k),
    L = min(k,N),
    rho_L(x) = (1/L) sum_(n<L) delta_(T_b^n x),

where the term L*rho_L is zero when L=0. Then

    W1(mu_(N,k), (L/N)rho_L(x)+(1-L/N)lambda)
       <= (b^L-1)/(2N(b-1)b^k)
       <= 1/(2N(b-1)).

**Proof.** At n>=k, the pushed cylinder measure is exactly Haar: T_b^k maps
its uniform interval onto a full unit interval, and later maps preserve Haar.
At n<k it is uniform on an arc of length b^(n-k) containing T_b^n x. Couple
that interval to its selected point. Its mean real distance to any point in
the interval is at most half the interval length; circular distance is no
larger. Summing these couplings and their weights gives the geometric sum.
No asymptotic theorem or independence assumption is used. QED.

The same proof applies to **every fixed nonautonomous affine forcing**

    y_(n+1)(a) = b y_n(a)+r(n+1) mod1,
    y_0(a)=a.

Condition a uniformly on I_k(a0). Each n-step map is multiplication by b^n
followed by a rotation. Therefore the same finite inequality holds with
rho_L the selected forced history starting at a0. In particular the exact
BBP forcing can be retained in every candidate history. Only the finite
initial-state selector is relaxed; the exact initial state is recovered in
the limit.

### 1.2 What the theorem proves about triangular limits

If k(N)->infinity but k(N)=o(N), then mu_(N,k(N))->lambda **for every x**.
This includes a uniquely selected constant orbit. Meanwhile nu_(x,k(N))
converges to delta_x. Thus increasingly exact source selection plus Haar
statistics of the finite-depth ensemble does not identify the occupation law
of its limiting selected path.

If the selected orbit has occupation law nu and k(N)/N->a in [0,infinity],
then the theorem gives the exact limit

    mu_(N,k(N)) -> min(a,1)nu + (1-min(a,1))lambda.

For a>0, rho_(min(k,N)) has the same limit nu. For a=0 its weight vanishes,
so no selected-orbit limit is needed.

At x=0 this family gives min(a,1)delta_0 plus the remaining Haar mass. These
limits are invariant under every integer multiplier, including tripling, but
are non-Haar whenever a>0. For 0<a<1 they even have positive average entropy.
The all-scale collision requirement in the inherited nonergodic rigidity
argument is precisely what excludes the atomic part.

For the first-digit zero indicator there is a simpler exact formula:

    mu_(N,k)([0,1/b)) = L/N + (1-L/N)/b       (x=0).

The true selected frequency is one. This formula supplies a completely
rational finite falsifier for an illicit limit interchange.

These statements do not prove a general computational impossibility. They
show exactly what a particular natural source-selection/mixing construction
computes, including the depth/horizon dependence that cannot be discarded.

## 2. Authentic BBP enclosure extension (independent audit, PROVED)

Write the authentic unwrapped source and positive tail as

    U_0=0, U_n=16 U_(n-1)+r(n),
    alpha=pi/16, 16^K alpha=U_K+T_K,
    0<T_K<B_K, B_K=1/((8K+1)(8K+2)).

Define the source-only rational interval

    I_K = [16^-K U_K, 16^-K(U_K+B_K)].

It contains alpha and has length ell_K=16^-K B_K. The intervals are strictly
nested. Lower endpoints increase because r(K+1)>0. Their scaled upper-endpoint
gap is

    16B_K-r(K+1)-B_(K+1)
      = integral_0^1 t^(8K)(1-t)[16-t^8-P(t)] dt >0,
    P(t)=4+4t+4t^2+2t^3+t^4.

For 0<t<1, P(t)<15<16-t^8. Thus the nesting is rigorous at every K>=0.
Their intersection is the actual alpha. No pi digits were supplied.

Let nu_K be uniform probability on I_K, reduced modulo one, and average its
first N T16-images. At time n the projected interval has length

    L_n=16^(n-K) B_K.

A uniform real interval of arbitrary length L>0, reduced modulo one, has
exact total variation from Haar

    TV = frac(L)(1-frac(L))/L <=1/(4L).

Here TV is half the L1 density distance. Proof: writing L=m+r, the density is
(m+1)/L on an arc of length r and m/L elsewhere. The two absolute deviations
integrate to 2r(1-r)/L. This formula holds even when L<1.

Put D_K=1/B_K and R_K=ceil(log_16 D_K), computed by exact integer inequalities.
At n=K+R_K the interval length is at least 1 and below 16. Later lengths grow
by 16, so the sum of their TV bounds is at most 4/15. W1 is at most one-half
TV on the circle.

### 2.1 Uniform effective-depth theorem

Let H_K=K+R_K and L=min(N,H_K). All images with n<L still have length below
one, so couple them to the first L selected orbit points. Later images couple
to Haar. This proves

    W1(mu_(N,K), (L/N)rho_L(alpha)+(1-L/N)lambda)
       <= B_K(16^L-1)/(30N16^K) + 2/(15N) * 1_(N>H_K)
       <= 2/(3N).

The last constant is safe and not claimed optimal. This gives a uniform
O(1/N) mixture law at the effective selection depth H_K. Replacing the effective-depth prefix by the first min(K,N) selected points
costs an additional O(R_K/N). The analytic
tail supplies about 2log_16 K extra selected iterates, not an unexplained
statistical improvement.

Exact independent checks of nesting and the TV formula passed. The checked-in
[selection-limit receipt](PI_PATH_SELECTION_LIMIT_RECEIPT.json) additionally
retains 240 cylinder cases, seven authentic source-window cases and 65 nested
BBP enclosures against an independent Machin interval. These checks calibrate
the instruments; the proofs above carry their universal quantifiers.

## 3. Concentration and normalization cannot be erased by phase cancellation

### 3.1 Signed selector norm tax (PROVED)

Let P be a probability prior, let A have prior mass p>0, and let w be any
integrable complex density supported on A with integral w dP=1. Then

    ||w||_2^2 >=1/p.

Proof: 1=|integral_A w|^2 <=P(A) integral_A |w|^2. Equality is attained by the
positive uniform density 1_A/p. If 0<=epsilon<=1 and only |integral_A w|>=1-epsilon is known,
the lower bound is (1-epsilon)^2/p. Negative or complex signs do not improve
this concentration cost relative to the declared prior.

For the Haar prior and a base-b depth-k cylinder, p=b^-k. For the
authentic BBP interval with that same prior,

    ||w||_2^2 >=16^K (8K+1)(8K+2).

This is a norm/normalization statement, not a lower bound on computational
runtime or a universal prohibition on some other representation.

### 3.2 A selector's small unnormalized amplitude is not orbit cancellation

Suppose a finite constraint projector P_N(h) vanishes except on one selected
history h*. With prior averaging and Z_N=E P_N nonzero,

    E[P_N F]/Z_N = F(h*).

Equivalently E[P_N F]=Z_N F(h*). Exponentially small Z_N can express only the
rarity of one legal history among all enumerated histories. It gives no bound
on the normalized selected observable F(h*). If all histories describe one
physical source through different coherent observer coordinates, any source
observable is constant on that fiber; the same factorization applies after
summing arbitrary gauge amplitudes, provided the normalizing sum is nonzero.

For unit phase weights a(h), normalization by Z=E a produces total variation
1/|Z| on the raw history space. A bound on an unnormalized oscillatory sum
must therefore retain the denominator before it can estimate a selected
correlation. A positive post-projection delta measure can still be perfectly
well defined.

### 3.3 Exact signed extension criterion (PROVED using classical Riesz)

Let A be a finite alphabet and let mu_N be finite signed or complex measures
on A^N whose marginals are projectively consistent. There is a finite
countably additive signed/complex Borel measure mu on A^{mathbb N} with
these marginals if and only if

    sup_N ||mu_N||_TV < infinity.

The extension is unique, and its total variation equals that supremum.

**Necessity.** Every finite cylinder partition has variation at most
||mu||_TV, and its atom masses are exactly those of mu_N.

**Sufficiency.** On the algebra of locally constant continuous functions,
define L(f)=sum f(a)mu_N(a) whenever f depends on the first N letters.
Consistency makes this independent of the chosen depth. The uniform TV bound
gives |L(f)|<=M||f||_infinity. Locally constant functions are uniformly dense
in the continuous functions on the compact product space: uniform continuity
allows approximation by sufficiently deep cylinder functions. L therefore
extends uniquely to a bounded linear functional on all continuous functions.
The classical real or complex Riesz representation theorem supplies the
unique finite regular Borel measure. Its cylinder integrals recover mu_N.
For each N, a modulus-one cylinder function choosing the conjugate phase of
each nonzero atom attains ||mu_N||_TV; hence the functional norm and variation
are exactly sup_N ||mu_N||_TV. QED.

The same argument applies to a closed finitely branching history space by
extending finite measures by zero off the permitted histories. Positivity
and total mass one supply the bound automatically. Signed normalization
alone does not. This theorem concerns finite countably additive measures;
distributional or oscillatory Feynman-type regularizations use other
topologies and require their own convergence theorem. Nothing here rules
those possibilities out.

### 3.4 A normalized coherent family with no finite signed extension

On binary words of length N, assign product weights with one-letter weights
2 and -1. At every depth the total mass is (2-1)^N=1. Marginalizing the last
letter preserves every earlier weight, so the family is exactly projectively
consistent. Its total variation is (2+1)^N=3^N.

No finite countably additive signed measure on the infinite binary path space
has these cylinder marginals. Its total variation would have to dominate the
variation on each finite cylinder partition, hence be at least 3^N for all N.

Thus a proposed infinite path-amplitude sum needs an actual convergence or
operator framework. Positive finite-dimensional path laws do not suffer this
particular defect; normalized complex/signed amplitudes need additional norm
control. This is not a claim that every physical quantum construction must be
a signed path measure, or that no other infinite operator limit can exist.

## 4. The authentic odd carrier already has unique backward histories

Every authentic r(n) and y_n has odd reduced denominator. On G_odd, the odd
rational torsion subgroup of the circle, multiplication by 16 is an
**automorphism**. Consequently x->16x+r(n) is a bijection of G_odd.

For c=a/q in lowest terms, q odd, the sixteen full-circle preimages are
(c+j)/16, j=0,...,15. Exactly one has odd denominator: it is the unique j
satisfying a+jq=0 mod16. The other fifteen have a nontrivial power of two in
the reduced denominator.

Therefore an inverse-circle path sum over all sixteen branches introduces
histories outside the authentic rational carrier unless those completion/cover
coordinates are explicitly part of the observer model. The unique odd branch
is fully compatible with an unresolved real carry-frequency problem. Its
label depends on the actual numerator/denominator residues; uniqueness does
not estimate their distribution conditional on real closeness.

This automorphism does not have a continuous inverse for the inherited circle
topology. For odd q=15 mod16, c=1/q tends to zero, while its unique odd inverse
is (q+1)/(16q), tending to 1/16. Passing to the compact circle completion
creates the additional inverse branches. Boundedness of the rational carrier
must not be confused with completeness or compactness.

This is an application of inherited odd-torsion injectivity, not a new source
mixing theorem. With exact forcing and initial zero, each finite forward
history was already uniquely specified before any interference construction.

## 5. A legally selected nonnormal source that the generic projector must accept

Use the inherited positive moment source

    T_n*=1/((n+1)(n+2)),
    r*(n)=16T*_(n-1)-T_n*>0,
    U_0*=0, U_n*=16^n/2-T_n*.

It has one exact forward history, a positive continuous Hausdorff kernel,
infinite Hankel rank, and infinitely many authenticated odd-prime births.
Its selected constant is 16T_0*=8, and its fractional states are
1-T_n* for n>=1, converging to zero. An exact finite-history selector accepts
it just as it accepts the true BBP forcing.

This source differs from the fixed BBP four-pole rational function and does
not claim the latest full BBP valuation profile. The inherited PAB positive
analytic construction additionally preserves that entire profile and any fixed
finite normalized dyadic precision, but changes the rational-function source
class. These controls are complementary; neither preserves the conjunction
of every exact BBP hypothesis.

## 6. What #270 and #272 still require

1. **Exact source selection is already available.** The recurrence plus y0=0
   supplies one rational state at every time. Nested BBP enclosures supply the
   selected real boundary constant. A new projector must produce an estimate,
   not just re-establish this uniqueness.
2. **The base-three route needs both real hypotheses.** The positive collision
   exponent must survive all fixed scales with source-uniform constants (or
   the stated prefix-uniform density of contracting scales). A single terminal
   saving is insufficient. Tripling must preserve the SAME selected empirical
   law. A new base-three formula or a source-compatible relabeling proves
   neither premise.
3. **The latest Pascal/height work is source-specific but not statistical.**
   Its valuations, exact p-poles and denominator growth exclude specified
   countermodels and exact integer locking. The resulting real separation is
   exponential, below the prescribed polynomial collision radii. It does not
   bound the number of close pairs or their centered carry branches.
4. **Positive average entropy is not enough in the nonergodic setting.** The
   cylinder-mixture countermodel gives a non-Haar invariant law with a Haar
   component. The inherited all-scale collision bound removes such a residual
   via domination and repeated Haar subtraction; deleting that hypothesis
   reopens the gap.
5. **Unique geometry, unique path, and unique invariant law are distinct.** A
   single selected history generally is not invariant under time shift: fixing
   the initial state and a nonautonomous forcing index breaks that shift
   closure. A unique invariant law on a periodic carrier is a uniform atomic
   law, not Haar on the full circle. Additional independently proved structure
   must identify the invariant law as the correct Haar law.


Implementation: [source_selection_limits.py](../../observational_succ/source_selection_limits.py).
Reproducer: [source_selection_limit_probe.py](../../scripts/source_selection_limit_probe.py).
See the [validation record](PI_PATH_SELECTION_VALIDATION.md) for the exact run scope.
