# A single chronological arithmetic frame with opposite real collision energies

Exact paper derivations, with classical fixed-modulus PNT. A countermodel concerns
an explicitly altered rational initial condition under the identical BBP forcing.
The principal orbit always means the four original poles and the literal seed zero.

Write U_n=16U_(n-1)+r(n) unwrapped, Q_n=lcm den(r(j)) up to n, and [x]=x mod 1.
Use the circle distance, ordered-pair J of the question, and natural logs.
Every sufficiently large integer A is allowed; n runs over I=[A,2A) in Z.
Only the asymptotic application requires q=q_A, K=K_A.
In this note P_A is never used to denote a prime product.

## Chronologically silent old primes

Let S be any subset of the primes p=5 mod 8 in (4A,8A-11] and H their product.
For p in S the pole 8j-3=p occurs once at j=(p+3)/8 <= A-1, with
p r(j)=-1 mod p. The other pole denominators at all times through 2A-1
are 1,4,5,6 mod 8. Multiples 2p and 3p are respectively 2,7 mod 8 and
cannot occur. The next possible multiple 4p exceeds every denominator in
the epoch. Thus p occurs to exponent one in Q_(A-1), and never appears in
any forcing denominator throughout I. The source gives, at every n in I,
c_(p,n)=p U_n mod p = 16^(n-j)*(-1) mod p, a nonzero class.
There are no statistical assumptions on c. Taking all candidate primes gives
log H=A+o(A) by the classical PNT in the progression 5 mod 8. All p=1 mod 8
first-pole passports and all p=3 mod 4 inert passports are disjoint from S.

For seed b/H let z=16^A b mod H. The shift on I is
[U_(A+i)(b/H)−U_(A+i)]=[16^i z/H]. At p in S the new scalar c'_(p,A)
equals c_(p,A)+z/(H/p) mod p. It vanishes for exactly one z class mod p.
For every z avoiding these forbidden residues define a group automorphism G of
Q/Z by multiplying the p-primary component at each p in S by a p-adic unit
congruent to c'_(p,A)/c_(p,A) mod p, and by acting identically at every other
prime. For instance choose the least positive integer representative of the unit.
The finite order of the epoch's p-components is p. At A the automorphism
takes [U_A] to [U_A(b/H)]. All [r(n)] on I are fixed. It follows by the
exact recurrence that G takes every [U_n] on I to [U_n(b/H)]. On the cyclic
clock of order Q_(2A-1) a single invertible CRT multiplier represents G.

Consequently the two trajectories have equal reduced denominators for EVERY
integer linear combination of epoch states (and fixed epoch injections), including
all pair differences and higher finite differences. They satisfy precisely the
same additive relations among these labels in Q/Z. The actual primary components
at every non-erased prime agree for every time, including before A. Real integer
carries must be recomputed for each world, and their actual values can differ.
Any observer retaining the orientation of an erased p before/during this epoch
can distinguish a shift with nonzero p-primary part.

## Coherence under a vanishing fraction of erased prime orientations

Fix 1<=L<A. Put M=A+L, alpha_M=U_M/16^M. For n<=M the exact finite future
R_(n,M)=16^n alpha_M-U_n is positive for n<M and
0<=R_(n,M)<1/(64n²) for n>=1 by the original positive BBP Green tail.
Take as candidate z all integers in the closed interval centered on
H{−16^A alpha_M}, with radius H/(16 A² 16^L). Write its size as W.
The union bound removes at most W Σ_(p in S)1/p + |S| integers, because
one residue per p is forbidden. For a candidate remaining, choose
b congruent to 16^(−A)z mod H. There is an integer k and a real e with
16^A(alpha_M+b/H)=k+e, |e|<=1/(16 A² 16^L). The first L epoch phases
are represented by 16^i e−R_(A+i,M), 0<=i<L. Their real diameter is
at most 2*16^(L-1)|e|+1/(64A²)<1/(32A²). The tuning used only finite exact
BBP inputs. In particular, whenever W(1−Σ1/p)>|S| there is a seed on the
same automorphism fiber with

    J_(A,q)(b/H) >= q(L/A)^2 (1−q/(32A²))      (2<=q<=32A²).

If all candidates p are used, any fixed c in (0,1/log 16) permits
L=floor(cA): W=exp[(1−c log16+o(1))A] and Σ1/p=O(1/log A).
This gives a positive constant times q on every sufficiently large epoch.
Deleting the first-pole births loses at most O(1) energy at q=q_A.

There is also a sparse option. Set L=ceil(A sqrt(K_A/q_A)). Select candidates
in increasing order until log H>=L log 16 + 6 log A. PNT ensures enough
for all large A. Overshoot is at most log(8A). Then W≫A^4 for the above
interval, Σ1/p=o(1), and J/K_A>=1−o(1). Only O(L/log A)=o(A/log A)
raw prime orientations have been erased, with total lost log modulus o(A).
Replace L by ceil(A(K_A/q_A)^(1/4)) to obtain J/K_A → infinity while
still erasing o(A/log A) primes. Every ordinal/conductor of every integral
multi-time combination remains fixed on I for this sparse option as well.
This excludes any fiber-uniform o(K_A) conclusion from these data.
The selected seed b=0 in that fiber remains the unresolved point.

## Typical and coherent paths coexist in the same full silent-prime fiber

Here use the full S, integer q>=2, q comparable to log A. Under the uniform
choice of ALL b mod H, for any fixed n,n+d in I, d>=1, the gap samples an
affine regular grid of size N_d=H/gcd(H,16^d−1). Indeed the seed term is
16^n(16^d−1)b/H and 16 is a unit. For f=q(1−q||x||)_+ the integral is one
and the total variation is 2q. Comparing an integral on each grid cell to
its left endpoint gives |mean(f)−1|<=2q/N_d.

Write m_p=ord_p(16). The elementary product bound

    #{p in S : m_p<=R} log(4A) <= log product_(1<=j<=R)(16^j−1) = O(R²)

holds even when a prime divides multiple factors. With R=floor(A^(1/3)),
summing log p/m_p for m_p<=R contributes O(R²), and the rest
contributes O(A/R). Thus Σ_(p in S)log p/m_p=O(A^(2/3)).
Summing log gcd(H,16^d−1) for d<=A gives at most
A Σ log p/m_p=O(A^(5/3)). Only O(A^(2/3)) lags have log gcd >= (log H)/2.
Each such lag contributes O(q/A) to normalized energy. The remaining
off-diagonal lags have grid error <=2q/sqrt(H); diagonals contribute q/A.
Thus the uniform unconditioned mean is 1+O(q A^(−1/3)+q/sqrt(H)).
Acceptable b exclude at most Σ1/p=O(1/log A) of the seeds. Since J>=0, the
conditional mean is <=(1+o(1))/(1−O(1/log A))=1+o(1). In fact J>=1 for every
seed: let f(t)=q/A times the number of epoch phases in the arc [t,t+1/q);
the circle integral of f is one and that of f² equals J by arc intersection.
Cauchy gives J>=1. Markov on J−1 therefore gives J=1+o(1) in probability
on the denominator- and relation-preserving fiber. This is a seed average;
the literal b=0 has no certified distribution within it.

## Optional stronger denominator-only control, allowing erased p-pulses

In place of silence take all primes A/16<p<=3A. For large A they have p²>16A
and all are born by A (original pole support, AS-01/PF-04). PR #497 PF-04 with
epsilon=1/32 ensures v_p(U_n)=-1 simultaneously over all n in I. That input
can also be reduced to a fixed finite exact test. Write 8j-b=mp for
b in {7,4,3,2} with weight w_b=4,-2,-1,-1. At these primes,
16^(−n) pU_n mod p is the partial sum in increasing m of
w_b (2|p)^m/(m 2^((m+b)/2)), b congruent −mp mod 8, m<=256.
This follows from Euler's criterion and m+b even. For each of the four odd
classes mod 8 the supplied rational script checks every one of the 128
nonempty prefix sums is nonzero. For sufficiently large p, no denominator or
nonzero numerator of that finite family is divisible by p. This alternate
paper-plus-finite-arithmetic proof is unnecessary for the silent-prime theorem.
At each p the shifted trajectory need only avoid zero at each pulse segment,
excluding O(1) classes z mod p (there are <=256 pulses). Every other prime
component is identical. Thus in the preceding interval sieve replace Σ1/p by
O(Σ1/p) and |S| by O(|S|). Here log H=(47/16+o(1))A, strictly above A log 16,
which permits L=A by taking M=2A. One can match the FULL reduced denominator
at every epoch time and keep the ENTIRE epoch diameter <1/(32A²). This argument
alone gives no joint denominator assertion on pairs, since these erased primes
can pulse during the epoch. Five small specified epochs lacked enough capacity
after excluding exceptional primes, as recorded; their failures limit the
finite observations and do not contradict the asymptotic PNT proof.

## Scope and probe

Older #492 AS-02 rounds the seed against the completed boundary near time zero
and authenticates the seed denominator and future birth passports. Here one
rounds on the epoch-entry grid, inverts the radix on an odd cofactor, enforces
surviving primary units, and uses a single automorphism for an entire epoch.
#487's locally compatible ghosts need not obey the full forced rational recurrence.
All our seed competitors do. An oriented prime-local residue is retained outside
the erased set; a unit relabeling within it preserves all orders but changes the
orientation relevant to the real embedding. In both full and sparse constructions
it is exactly this lost orientation, correlated with the authentic old numerator,
that the next successful sieve must bound. Equidistribution, selected real
collision decay and any independence of prime characters all remain open.

Internal priority boundary. Main's 2026-10-31 seed_superposition SS01--04
treat continuous cylinders and finite dyadic grids. Main's 2026-11-02
mobius_mirror MM-12 averages the second moment over an arbitrarily chosen
odd prime of adequate order. In 2026-11-02 line_sheet_gamma LS-12--15 and
#485 GL-06, products of clean-prime unit averages give small signed short-
window or short-lag Galois kernels. The first two already establish generic
seed cancellation, and the last two already supply a chronological primary
unit action. Here the averaging family is the **original bounded-height
source-generated old-prime fiber**, with every complete multi-time order
preserved, the full dyadic energy at all lags controlled in its mean, and
coherent changed seeds constructed in the very same fiber. All four methods
share radix orthogonality. No external or exhaustive repo priority is claimed.
The zero seed occurs in the conditional ensemble (all original coefficients
are nonzero). This gives it weight 1/product(p−1), which is much too small
to infer pointwise control.

## A stronger conditional occupancy law by disjoint radix words

Let S be the full silent set, q=16^K/2 on the stated schedule, and
m=16^(2K)=4q². For a uniform seed among admissible b mod H, outside a
fraction O(Km exp(−c A/(K³m))) for some absolute c>0 and all sufficiently
large A, one has simultaneously for **every** circle interval I of length 1/q

    | q/A * #{n in [A,2A): [U_n(b/H)] in I} − 1 | = O(1/K + q/m).

Endpoints can be assigned either way, and all constants are absolute.
Consequently the conditional mean J tends to 1 by a second proof. The
coherent seed has a fixed-fraction block in one short arc even though
almost every denominator- and relation-compatible seed passes Target B.

Proof. First take all b uniformly. Partition the epoch into four adjacent
blocks of lengths floor(A/4) or ceil(A/4). At a block start B the completed
point [16^B(alpha+b/H)], alpha=pi/16 from the original source, is uniform
on a translated H-grid because H is odd. Couple it to a uniform real circle
point Y by adding an independent uniform offset in [0,1/H). For every i in
the block the original finite phase [U_(B+i)(b/H)] and [16^i Y] differ in
circle distance by at most

    eta = 16^ceil(A/4)/H + 1/(64A²) = o(1/m).

Here log H=(1+o(1))A and log(16)/4<1. This is deterministic for every
offset in that interval. It uses the same forcing and the same marked
completion alpha for all b, adding only the declared seed.

For a Haar Y, the event that [16^i Y] lies in a specified one of the m equal
half-open cells is a specified word of 2K consecutive radix-16 digits.
On each residue class i mod 2K these words use disjoint iid Haar digits.
The count in that class for one cell is exactly binomial(N,1/m), where
N is the size of the class and N >= c_0 A/K for large A. For deviation
at least N/(Km) the two-sided binomial Chernoff bound gives probability
<= 2 exp(−N/(3K²m)). Equivalently this follows by Markov on
(1−1/m+exp(t)/m)^N and its lower-tail counterpart. Union bound over 2Km
class/cell pairs and four blocks gives the declared exceptional probability.
The couplings for different block starts can reuse the same b; the union bound
requires only each marginal to be Haar.

If the test passes, summing classes gives, in each block of length D,
between (1−1/K)D/m and (1+1/K)D/m hits in each cell for its Haar orbit.
Any interval of length 1/q enlarged by eta in both directions is covered by
at most m/q+4 cells, and the concentric interval shrunk by eta contains at
least m/q−4 complete cells, for large A. These cover bounds sandwich source
occupancy in the original interval; summation over the four blocks proves
the claimed relative error for every interval at once. Any bad discrete
seed forces the coupled Haar test to fail for every choice of offsets, so
the same probability bound applies to the discrete seeds. Unit conditioning
changes it by a factor at most (1−Σ1/p)^(-1)=1+o(1). Finally the sliding-arc
identity above and J<=q imply the conditional mean convergence as well.
There is no unidentified coin flip for the actual b=0 in this theorem.
The two seed-ensemble proofs differ in method but share the original
source embedding and the same silent-prime modulus.

## A mixed angular denominator identifies the exceptional zero seed in the fiber

For the original sources r and r_ang of #499 PQ-4, run the identical radix
recurrence for U and Y. Their common seed s=b/H preserves the original exact
radial difference Y_n(s)−U_n(s)=Y_n(0)−U_n(0). Here H is any squarefree
product from the silent set. For every such s (lowest terms or otherwise),

    gcd(den(2Y_A(s)−U_A(s)), H) = den(s),    when den(s)|H.

Proof. For p in S there is just one positive multiple of p among any raw
eight-tap denominators through time A since 2p>8A. It occurs in tap j=5
at j_p=(p+3)/8<=A-1. The original coefficient there is −1, while the angular
tap is −1/2. All tap coefficients are p-integral. At seed zero the mixed
forcing 2r_ang−r has *zero* fifth tap, so p is absent from the mixed state
denominator at time A. For a common shifted seed the mixed state is
2Y_A(0)−U_A(0)+16^A s. As p does not divide 16, its denominator contains
p iff p divides den(s). Both H and den(s) are squarefree; multiplying gives
the assertion. Equivalently, 2Y−U is half the inherited dual V at seed zero.
The classifier compounds that known projection with the constructed fiber,
giving it the quantitative meaning of a seed-denominator measurement.
The alternate combination 3Y−U leaves tap −1/2 at j=5 and has every donor
prime in its denominator at the true seed. For common shifts this mixed
denominator is a strict discriminator within the one-frame hostile worlds.
The point b=0 can already be named before taking the measurement; no
Archimedean upper bound on its energy follows from classifying the point.

The statement concerns common seed perturbations, and a reset common shift
at epoch entry with denominator dividing H obeys the same algebra. The two
source expressions share exact provenance and statistical independence plays
no role. For nontrivial b, the single-frame automorphism furnished above
cannot also take all authentic angular states to the common-seed perturbed
angular states, as it would preserve the mixed denominator in contradiction
to this calculation.

At entry A even imposing both original **individual** reduced denominators of
U_A and Y_A permits the coherent construction. To match Y_A's denominator,
exclude one further residue mod each donor p (the nonzero value c_(p,A)/2
must stay nonzero after shift). Outside S the shift has zero primary part.
To additionally require shifted seed to have exact denominator H, exclude
zero mod each p as well. The preceding interval union bound with three
forbidden classes per prime still leaves candidates. Thus original-only,
angular-entry-only and their joint *marginal* denominator conditions all
admit coherent competitors. The arithmetic of the **linear combination**
2Y_A−U_A distinguishes them. This proof concerns the angular marginal at
entry A only: some angular p-pulses occur later within [A,2A).

## One missing orientation already suffices for a bounded conditional mean

Fix any p from the full silent set and retain the authentic raw orientation at
every other prime. The following even allows arbitrary fixed admissible labels
at those other donor primes: first choose a fixed translate of the seed fiber,
then vary only s by b/p (b mod p). This preserves all the non-p labels, the
actual forcing and the single-frame joint denominator profile upon excluding
one forbidden residue mod p. Write T=ord_p(16). For integer q>=2 the exact
energy bound is

    1 <= E_admissible J <= p/(p−1) * [1+q/A+2q/p+q/T].

Indeed at each lag d not divisible by T the unconditioned p-grid mean differs
from 1 by at most 2q/p, by the variation estimate above. For d divisible by T
the gap stays fixed, with value at most q. Counting times by residues mod T,
the total number of off-diagonal ordered pairs with that property is at most
A floor((A-1)/T) <= A²/T: for each time at most ceil(A/T)−1 other times
belong to its residue. Diagonals contribute q/A. Dropping one forbidden b
from a nonnegative sum costs at most p/(p−1); the sliding-arc lower bound
holds pointwise. Every p has T>=log(p+1)/log16, hence every single-prime
conditional mean is O(1) at the logarithmic mesh. Furthermore, for at most
O(A^(2/3)/log A) of these primes is T<=A^(1/3), by the elementary product
bound in the full-fiber proof. There are ~(A/log A) primes in the full
set. For every remaining prime the upper bound gives conditional mean
1+O((log A)/A^(1/3)). All constants are independent of the other fixed
labels. This conclusion requires no Artin-type conjecture.

Thus one may orient every prime but one at its exact **selected** value and
still prove the desired energy scale on average over the p−1 survivors. For
the authentic slice the preceding mixed denominator test isolates the
literal b=0 among those p−1 survivors. The outstanding obligation is a
point evaluation estimate, e.g. for some such p(A), J(0)<=C_A E_admissible J
with C_A=o(K_A), from the joint signed chronology of the b=0 class. This
last inequality is open and, given the proved bounded mean and its lower
bound, is equivalent in asymptotic strength to the original energy goal.
What improved is the number of *unfixed* coordinates in its averaged
comparison. The multi-prime coherent counterseed does not itself imply
that a given one-prime slice through zero contains any bad seed.
