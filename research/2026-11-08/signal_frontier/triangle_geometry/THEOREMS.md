# Pascal histories realized by golden arcs, with their source measures retained

**PROVED PAPER; finite exact checks and separately labelled numerical geometry.**
Pi base-16 normality and RH remain **OPEN**. The construction strengthens the
user's triangle proposal into a source-decorated refinement map. It also
identifies exactly which geometric probability identification fails.
The source-specific separation below concerns the declared Pascal observer;
it is not a distribution theorem for the deterministic BBP orbit.

## GT1. Binary histories have an exact golden interval realization

Put alpha=(sqrt(5)-1)/2, so alpha+alpha²=1. Fix an integer k0>=0 and the
root interval I_empty=[0,alpha^k0]. For a word w, let I_w=[l_w,l_w+L_w]
and define its children by

    I_(w0)=[l_w,l_w+alpha L_w],
    I_(w1)=[l_w+alpha L_w,l_w+L_w].                      (GT1)

Use half-open intervals when assigning probability, with the final right
endpoint assigned consistently. For a word of length m with j ones,

    L_w=alpha^(k0+m+j),
    sum_(|w|=m)L_w=alpha^k0,
    sum_(|w|=m,grade(w)=j)L_w
       =binom(m,j)alpha^(k0+m+j).                        (GT2)

**Proof.** Each zero multiplies length by alpha and each one by alpha².
The children cover their parent with disjoint interiors because alpha+alpha²=1.
Induction gives the partition; grouping the binomially many words of grade j
proves the last formula. Thus the normalized geometric grade law is precisely
Binomial(m,alpha²), since alpha^(m-j)(alpha²)^j=alpha^(m+j).

This is a functor on the existing word-prefix observation category: send a
word to its interval, and a prefix arrow w→wv to the inclusion I_(wv)⊆I_w
in the category ordered by reverse inclusion. Identities and composition
are inclusions. No replacement category API is needed. When source measures are
attached as below, each object retains its actual measure and source
signature; each arrow retains its actual posterior update. Only the spatial
carrier is realized differently.

The grade quotient is not a faithful spatial functor. For example 01 and10
have the same length alpha³ (k0=0) but distinct interiors: their left
endpoints are alpha² and alpha. Keeping only j erases their positions.
Their retained source posteriors nevertheless coincide in the exchangeable
sensor below. Spatial history and latent-source sufficiency are different
questions.

## GT2. Every finite refinement has exact integer-clock coordinates

Every endpoint belongs to Z[alpha], because GT1 uses addition and multiplication
by alpha starting from alpha^k0. If t=A+B alpha with integers A,B, then

    e(t)=e(B alpha),       e(u)=exp(2pi i u).             (GT3)

Thus each vertex is an exact golden-rotation clock point with integer label B.
For any finite collection of endpoints, let B_min and B_max be its extreme
clock labels. Choose N=max(0,-B_min). All vertices are then read at nonnegative
integer times N+B, within horizon N+B_max, on the same circle. This realizes
the original configuration after a common rotation e(N alpha). Retaining the
anchor transports every phase back by e(-N alpha).

This is a finite causal acquisition theorem: the observer waits until the
largest required time, then evaluates the recorded configuration. It does
not say that the order of prefix refinement is already the physical order
of clock visits. Finer finite frontiers may require a different N; comparing
them requires the displayed anchor transport. An infinite refinement does
not fit into one finite acquisition horizon.

For the three-vertex return triangle, put a=alpha^(k+1), b=alpha^(k+2),
c=a+b=alpha^k, k>=2. Its phases0,a,c are golden clock points since

    alpha^r=(-1)^(r-1)(F_r alpha-F_(r-1)).               (GT4)

The relative integer labels are0, (-1)^k F_(k+1), (-1)^(k-1)F_k.
GT3 supplies a shared causal offset even when a label is negative.
This uses actual integer times, without replacing BBP source time by a
rotation clock.

## GT3. The positive BBP posterior refines on the very same arcs

For a **fixed** source parameter a>0, preserve the original positive kernel

    Q(x)=4-2e^(-3x)-e^(-4x)-e^(-5x),
    R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),
    mu_a(dx)=e^(-ax)Q(x)dx/R(a),   x>0.

It is positive, continuous, and normalized; Q(x)>0 for x>0, Q(x)<=4.
This is exactly the existing operational-triangle source, and
R(8n-7)=r(n) for the authentic four-pole recurrence. Set f(x)=e^(-8x),
g(x)=1-f(x). Conditional on the retained latent X, observe independent
bits with probabilities f(X),g(X). For a word w of length m,grade j, attach

    M_w(dx)=f(x)^(m-j)g(x)^j mu_a(dx),
    q_w=M_w((0,infinity)),      nu_w=M_w/q_w.             (GT5)

All q_w>0. The source-labelled arc is (I_w,M_w,source_signature), and

    M_w=M_(w0)+M_(w1),
    sum_(|w|=m,grade=j)M_w=binom(m,j)f^(m-j)g^j mu_a.   (GT6)

The latter is exactly the measure-valued Pascal row. For a suffix v, the
morphism w→wv carries the multiplier
f^(length(v)-grade(v))g^grade(v), together with the interval inclusion.
The empty suffix gives multiplier1; concatenation multiplies these factors.
Thus identities and lawful composition are preserved in both coordinates.
This supplies a refinement-preserving realization, not just matching scalar
weights.
For any bounded measurable source observable A(w,x), enumerating words and
then placing their measures on labelled intervals equals the direct
labelled-interval sum. It commutes because the same measures are retained.
For finite depth, one possible spatial representation is

    dPi_m(t,x)= sum_(|w|=m) [1_(I_w)(t)/L_w] dt M_w(dx).

The coarsening kernel that replaces a child position by a uniform point of
its parent, while retaining x, sends Pi_(m+1) to Pi_m. Merely forgetting a
label need not do so; literal Pi_(m+1)=Pi_m is not claimed. Its cylinder
masses and latent posteriors obey GT6 exactly. These consistent cylinder
masses define the infinite address law in GT4 below.

Geometry and source probability coincide conditionally only when f(x)=alpha
and g(x)=alpha². Indeed first-level lengths are alpha,alpha², while the
conditional probabilities are f,g; equality at every cylinder follows
exactly from that one condition. In the authentic continuous source it holds
at the single point x*=-(log alpha)/8, a mu_a-null event. Positivity of both
measures is not equality of the measures.

The circle realization also carries the declared unwrapped BBP history,
integer carries and literal zero seed as extra marks. The interval location
alone has no map recovering these marks. Erasing them is a different functor,
and no source-selection theorem is asserted after that erasure.

## GT4. Exact Lebesgue decomposition and almost-sure source learning

Let mu be any probability law on finite x>0 and use the same conditional
Bernoulli sensor. Let nu_mu be the pushforward of its infinite binary address
law under the nested-interval limit. This limit exists uniquely because
L_w<=alpha^(k0+m)→0. Let ell denote normalized Lebesgue measure on the root
arc. Then

    nu_mu = mu({x*}) ell + nu_sing,
    nu_sing is singular with respect to ell.            (GT7)

In particular the authentic fixed-a law nu_(mu_a) is **singular** with respect
to arc length. This concerns a fully specified auxiliary circle law, not
{16^(n-1)pi} or e(U_n).

**Proof.** Under ell, cylinder probabilities are the products of alpha and
alpha², so the decoded address bits are iid with probability of one alpha².
Under the source conditional on X=x they are iid with probability g(x).
For each p in(0,1), their empirical frequency tends p almost surely. For
completeness, at sample sizes n=k² Chebyshev bounds the deviation probability
by1/(4k² epsilon²); the sum is finite. The first Borel-Cantelli lemma gives
convergence on those squares. Between successive squares, the change in an
empirical frequency is bounded by2(2k+1)/k²→0. Intersect over rational
epsilon>0. This proves the needed strong law. Conditional integration gives
it jointly for every prior mu.

Interval endpoints with multiple binary addresses form a countable set.
Every individual infinite address has conditional probability0 for p in(0,1),
and hence zero mixed probability; ell also assigns endpoints zero. Away from
these endpoints the address is measurable and uniquely decoded. Thus the set
of points whose address frequency is alpha² has ell-measure1, and source
measure mu({x*}). Conditional on X=x*, every cylinder has its exact geometric
length, giving ell itself. The remaining source component is supported on
the complementary ell-null set. This proves GT7.

Moreover the infinite address learns the latent source exactly almost surely:

    X = -(1/8) log(1-lim_m grade(w_m)/m).                (GT8)

This is a genuine historical-learning theorem under the declared stochastic
sensor. It neither identifies arbitrary real X from finite-precision finite
readings nor asserts that the physical BBP orbit samples those bits.

**Fixed-prior discipline.** The law mu must be held fixed across all prefixes.
The native diagonal a_m=8m-7 changes that law with m. Its finite rows do not
automatically form a projective family. For example the probability of an
initial zero under depth1 prior mu_1 is R(9)/R(1), whereas the marginal of
that bit under a depth2 prior mu_9 is R(17)/R(9); they differ (exact oracle).
Thus GT7 cannot be applied to the native diagonal without a new compatible
transport. The other triangle front treats that different limiting regime.

## GT5. A quantitative finite source/arclength discriminator

Let q_(a,m) be the authentic fixed-a grade law and b_m the geometric law
Binomial(m,p*), p*=alpha². Use TV(P,Q)=sup_E |P(E)-Q(E)|. For every integer
m>=1 and every0<eta<=alpha/4,

    TV(q_(a,m),b_m)
      >=1-4eta/[alpha R(a)]-1/(2m eta²).                 (GT9)

A negative lower bound is simply uninformative. For each fixed a, choosing
eta=(alpha R(a)/(4m))^(1/3), once this is <=alpha/4, yields

    TV(q_(a,m),b_m)
      >=1-(3/2)[4/(alpha R(a))]^(2/3)m^(-1/3).           (GT10)

**Proof.** The variable p=g(X) has density

    w_a(p)=(1/[8R(a)])(1-p)^(a/8-1)
                  Q(-(log(1-p))/8),   0<p<1.

On |p-p*|<=2eta, the condition eta<=alpha/4 gives
alpha/2<=1-p<=3alpha/2<1. Since a>0 and Q<=4,
w_a(p)<=1/[alpha R(a)]. Hence that interval has source probability at most
4eta/[alpha R(a)]. Let E={|J/m-p*|<=eta}. Conditional on any p outside the
2eta interval, E forces |J/m-p|>eta, whose probability is at most
1/(4m eta²) by the binomial variance. Therefore q_(a,m)(E) is at most the
source interval probability plus1/(4m eta²). Under b_m, E has probability
at least1-1/(4m eta²). Subtract to prove GT9. Optimizing the displayed sum
proves GT10.

The same bound applies to the depth-m spatial laws because grade is a
measurable function of their labelled partition. It is a source-specific
finite separation from **geometric arclength**, with all constants visible.
It does not bound the signed covariance of the authentic zero-seeded orbit.
It is not uniform when a grows with m: R(a)~15/a², so the constant in GT10
can grow. This is exactly where an unjustified native-diagonal promotion
would fail.

### A separate native-diagonal finite theorem

The changing native prior does admit a finite comparison, without claiming
an infinite projective path law. For every a>0,m>=1, Markov and Chebyshev give

    TV(q_(a,m),b_m) >=1-4/(m alpha)
             -2[1-R(a+8)/R(a)]/alpha².                 (GT10b)

To prove it, take E={J>=m alpha²/2}. Under b_m, Chebyshev gives
Pr(E)>=1-4/(m alpha). Under the source, the exact mean is
EJ=m[1-R(a+8)/R(a)], so Markov bounds Pr(E) by the second displayed cost.
Subtract. Since

    R(a)=(15a²+121a+240)/[a(a+3)(a+4)(a+5)],

putting a=8m-7 shows the right-hand side tends1 with error O(1/m).
More precisely, m times its subtracted error tends
4/alpha+4/alpha²=12+8alpha. This is an actual native finite-row separation
from geometric arclength, not an infinite-law inference. It follows directly
from the authenticated source mean and uses no fitted limit. The root's
independent Markov/Chebyshev derivation is credited for GT10b.

A sharper exponential native separation uses the same event without throwing
away its generating function. Let m>=2, a=8m-7 and t=ceil(m alpha²/2). Then

    TV(q_(a,m),b_m) >=1-2^(t-1)(1-alpha²/2)^m
             -(2/3)^t R(a-4m)/R(a).                    (GT10c)

All terms in this finite bound belong to Q(alpha). For the source,
1+g(X)/2<=exp(4X), so E[(3/2)^J]<=E exp(4mX)=R(a-4m)/R(a);
a-4m=4m-7>0. Markov gives the last term as an upper bound for Pr(J>=t).
For the geometric law, E[2^(-J)]=(1-alpha²/2)^m; on J<t one has
2^(-J)>=2^(-(t-1)), proving the other cost. Subtract as before.

Writing p*=alpha², this error is at most

    beta^m+C_m gamma0^m,
    beta=2^(p*/2)(1-p*/2)<1,
    gamma0=(2/3)^(p*/2)<1,
    C_m=R(4m-7)/R(8m-7)→4.                             (GT10d)

Here gamma0 is a decay base, unrelated to the Euler–Mascheroni constant.
The first strict inequality follows from log(1-p*/2)<-p*/2 and log2<1.
Thus native finite rows separate from golden geometric grade weights at an
explicit exponential rate, even though they are not one projective path law.
The observed exact finite separation is a diagnostic for the wrong source-map
identification, not signed decay of e(hU_n).

## GT6. Chord defects, area, and their resolution scaling

For k>=2, let a=alpha^(k+1),b=alpha^(k+2),c=a+b=alpha^k, and let R>0.
The inscribed triangle with phases0,a,c has chord deficit and Euclidean area

    Delta_k=2R[sin(pi a)+sin(pi b)-sin(pi c)]
      =8R sin(pi a/2)sin(pi b/2)sin(pi c/2)>0,
    Area_k=2R² sin(pi a)sin(pi b)sin(pi c)>0.            (GT11)

The deficit identity follows by applying the sine sum and difference
identities. The area follows from side lengths2Rsin(pi a),2Rsin(pi b),
2Rsin(pi c) and Area=product(sides)/(4R), or directly from a determinant.
In particular

    Area_k/(R Delta_k)
      =2cos(pi a/2)cos(pi b/2)cos(pi c/2)→2,
    Delta_k/alpha^(3k)→pi³R alpha³,
    Area_k/alpha^(3k)→2pi³R² alpha³,
    Delta_(k+1)/Delta_k→alpha³,
    Area_(k+1)/Area_k→alpha³.                           (GT12)

These are asymptotic scaling laws, not exact finite cubic recursions.
For an explicit error envelope, with x_i=pi(a,b,c)/2,

    alpha³ < Delta_(k+1)/Delta_k
          <=alpha³ product_i(1-x_i²/6)^(-1).            (GT13)

Replace x_i by pi(a,b,c) for the area ratio. The denominators are positive
for k>=2. Strict concavity gives sin(alpha x)>alpha sin(x), while
sin(x)>=x(1-x²/6) and sin(alpha x)<=alpha x give the upper bound.
Thus the ratio approaches alpha³ from above. Curvature is geometrically
recoverable as1/R=4Area/product(sides); its equality to any source posterior
statistic is not asserted. At fixed absolute readout error, shrinking these
triangles makes curvature inversion ill-conditioned, as the preceding
Fibonacci calibration theorem quantifies.

## GT7. Farey triangles use a different metric and boundary map

Adjacent convergents F_(k-1)/F_k and F_k/F_(k+1), k>=2, have determinant±1.
Their mediant is F_(k+1)/F_(k+2); these three distinct rational cusps bound
one Farey ideal triangle in the upper half-plane. The boundary map to the
unit disk is the Cayley map

    C(x)=(x-i)/(x+i),  x in R;       C(infinity)=1.       (GT14)

It is injective on the extended real boundary. The map x↦e(x) is not an
acceptable substitute: rational cusps0 and1 would coincide. Cayley transports
the hyperbolic metric and geodesic arcs. In curvature−1 units every ideal
hyperbolic triangle has area pi: for the canonical upper-half-plane triangle
(0,1,infinity), integrate dx dy/y² over0<x<1 and y>sqrt(x(1-x)) to get
integral_0^1 dx/sqrt(x(1-x))=pi; a real Möbius isometry sends every ideal
triangle to this one. The ordinary Fibonacci chord areas in GT12 instead
tend0. They cannot be identified by an area-preserving isometry.
Cassini/mediant integer algebra is shared; the metrics and boundary maps
remain declared. No Gamma field is needed for this assertion.

## Claims, hostile controls, and the next theorem

| Claim | Status and receipt | Boundary |
|---|---|---|
| GT1–3 | Proved finite/paper; exact arc and posterior oracle | Faithful at history level, not after grade-only spatial collapse |
| GT4 | Proved fixed-prior infinite theorem | Continuous-source auxiliary arc law is singular; not BBP orbit law |
| GT5 | Proved source-specific finite TV separation; separate native bound GT10b | Fixed-a bound and changing-prior finite bound are distinct |
| GT6 | Proved geometric identities and asymptotics | Numerical holdouts do not supply the proof |
| GT7 | Classical Farey/Cayley geometry with explicit maps | No Euclidean/hyperbolic metric identification |
| Source masses equal golden arc lengths | Refuted: exact fixed-a row comparison and GT9 | Both remain positive |
| Native diagonal rows automatically projective | Refuted: R(9)/R(1) !=R(17)/R(9) | Needs separate source transport |
| All posterior information survives grade-circle masses | Outside this construction; other front supplies explicit aliases | Posterior marks must be retained |
| This triangle proves original-zero covariance decay | OPEN and not implied | Coherent wrong seed shares positive source and geometry |

The next arithmetic bridge must relate the retained, source-authenticated
signed BBP characters to these posterior-decorated histories by an actual
map and a proved signed estimate. Keeping original U0=0 as a label is
necessary authentication, not itself an estimate. The coherent seed−pi/16
has the same positive-source observer and calibrated geometry but e(hU_n)→1;
our construction neither discards that distinction nor claims to solve it.

Dependencies: docs/OPERATIONAL_TRIANGLE.md and its original finite source
implementation; existing Farey/Gauss module; preceding Fibonacci geometry.
No frozen files, source contracts, or shared catalog are modified. These are
new-to-this-dossier compositions and scoped estimates using classical
methods, with no claim of worldwide novelty or external scholarly review.
