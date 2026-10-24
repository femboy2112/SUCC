# OPERATION MINIMAL GENESIS — first carries, minimal frames and the BBP information diode

**Date:** 2026-10-24. **Research-only**. Branch
research/minimal-genesis-first-carry-2026-10-24, stacked on the
source-faithful circle-origin research PR #257 at exact observed
head 5435497dc77a313d1ebbc56ac96c11e593db2619. PRs #256/#258
(another separate sibling research family on #254) are consulted,
not silently imported or credited as kernel-checked premises.

**Claim authority:** independently derived elementary PAPER proofs,
exact integer/Fraction finite tests, a declared isolated local harness,
and separately inspectable final-head CI. No new Lean theorem
admitted. All lacunary-moment, Hausdorff Green and shift-operator
ingredients have classical ancestry; independent mathematical
novelty is UNVERIFIED. **π normality remains OPEN in every base.
RH, completed signed Weil positivity and physical origin symmetry
are not established.** Source faithfulness and numerical resemblance
are not asymptotic proof.

## 0. The precise minimality conjecture and the falsification rule

A short generating program and a minimal physical-action trajectory
are different properties. Neither is inherently a randomness
principle. The basic circle map T_b(x)=bx mod1 is one of the simplest
expanding deterministic laws; Haar is its unique absolutely
continuous invariant probability. That DOES NOT make each selected
orbit Haar-generic.

Instead of asserting "nature takes the simplest path" universally,
this round proves three scoped versions:

(1) **Minimal base-b carries:** exactly where deterministic
orbit phases cease to mimic independent Haar phases.
(2) **Minimal finite observer clocks:** the least number of
modular origin samples needed to capture a declared high moment.
(3) **Minimal causal Green section:** the unique finite-energy
backward solution carrying the exact signed BBP source, and a
proof that it cannot intertwine linearly or continuously with
the autonomous expanding phase law.

The signed full-source π cancellation problem remains separate.

## MG-01. Exact low-order independence illusion (CLASSICAL / PROVED PAPER)

For integers b>=2, N>=1 let
    P_(b,N)(x)=sum_(j=0)^(N-1) exp(2πi b^j x).
For integer k>=0 set
    M_(b,N,k)=int_0^1 |P_(b,N)(x)|^(2k)dx.

Fourier character orthogonality yields exactly
    M_(b,N,k)
      =sum_(s>=0) W_s^2,
where
    W_s=sum_(a_0+...+a_(N-1)=k; sum a_j b^j=s)
                  k!/(prod_j a_j!).

Define the comparison with N independent uniform unit phases:
    D_(N,k)=sum_(a_0+...+a_(N-1)=k)
                   (k!/(prod a_j!))^2.

**Sharp theorem:** for EVERY N and every 0<=k<=b,
    M_(b,N,k)=D_(N,k).                                (1)
In particular
    int |P_(b,N)|^(2k) <=k!*N^k
and the normalized origin ensemble satisfies
    Haar{|P_(b,N)(x)|/N>=eps}
       <=k!/(eps^(2k) N^k), 1<=k<=b.

**Proof.** A k-term multiset representation of
an integer using powers 1,b,b²,... has nonnegative
occupancies a_j with sum k. Replace b copies of
b^j by one b^(j+1) until all digits <b.
The canonical digits are unique; each carrying step
reduces the token count by exactly b−1. If k<=b,
there can be at most one carry. At k=b, a carried
representation must normalize to a single base-b
digit b^u, and its only possible reverse carry
to b terms is uniquely at level u−1. Therefore
two distinct representations with exactly k<=b
tokens cannot have the same integer sum. Fourier
orthogonality thus leaves ONLY equal multisets,
so M=D. For the upper moment bound, every
ordered k-tuple has at most k! ordered matching
permutations. QED.

This is a finite-order joint Haar-ensemble statement;
it is NOT an independence theorem for all joint
distributions and says NOTHING about pointwise π.

For b=16 this gives exact independent-phase
agreement through every EVEN moment of order <=32.
It extends the inherited PR #257 exact fourth
moment and PR #249 carry-sensitive joint moments
without equating their differently typed observables.

## MG-02. The first detectable additive carry, with its EXACT excess

At k=b+1 the first nontrivial equal-sum
representations appear:

    b*b^i + b^(i+g)
      = b^(i+1) + b*b^(i+g−1),  g>=2.

Each side has b+1 terms. This is the smallest
possible equal-length genuinely distinct
multiset identity among positive base-b powers.

**Exact closed theorem**, for N>=2:
    M_(b,N,b+1)−D_(N,b+1)
      =2(b+1)(N−2)
          +(b+1)^2 (N−2)(N−3).                    (2)

For N=1 both moments agree, excess 0.

**Proof, including b=2.** With k=b+1, a
nontrivial collision can arise only from a
canonical base-b number of digit sum TWO,
which admits two DIFFERENT one-step
reverse carries. Such a number must have
two distinct unit digits at exponents
1<=u<v<=N−1. Reversing at u yields b tokens
at u−1 and one at v, with (b+1) distinct
ordered arrangements. Reversing at v yields
one at u and b tokens at v−1. If v=u+1,
all b+1 tokens of the second representation
occupy exponent u, with ONE arrangement;
otherwise its weight is again b+1.
There are (N−2) adjacent (u,v), and
(N−2)(N−3)/2 nonadjacent pairs. Each
unordered collision contributes 2*w_A*w_B
to the square of the character-sum count,
proving (2).

For b=2 a canonical single nonzero binary
digit can also arise after TWO carries from
a 3-token representation, but the reverse
splitting history is unique as an unordered
multiset; it creates no cross-collision.
For b>=3 two carries would leave zero or
negative canonical digit sum. QED.

Hexadecimal source-exact examples:
    N=3: excess 34;
    N=4: excess 646;
    N=5: excess 1836;
    N=100: excess 2,750,566.

The N=3 full 34th moment equals
399769750195999 versus independent baseline
399769750195965. Independent exhaustive
ordered-tuple oracles validate smaller bases
and the same combinatorial coefficient.
All claims hold for ANY Haar-sampled
origin, not for the selected π source.

The relevant research literature is classical
lacunary trigonometric series / additive
frequency-relation combinatorics (Kac,
Salem–Zygmund and Aistleitner et al.,
Probability Theory and Related Fields 2025,
doi:10.1007/s00440-025-01405-5).
Do not claim independently established novelty.

## MG-03. Minimal modular origin clocks (EXACT FINITE)

A full q-torsion frame reproduces Haar M_(b,N,k)
exactly iff its k-power frequency sums remain
distinct modulo q (for k<=b). All expansion
coefficients are positive, so even one alias
STRICTLY inflates the grid moment.

There are precisely
    S=C(N+k−1,k)
different k-token source multisets.
Therefore any alias-free full-grid clock
must have AT LEAST S labels:
    q>=C(N+k−1,k).                               (3)

The elementary *safe* construction
    q>k*b^(N−1)
is sufficient, but very far from optimal.
Search exhaustively over candidate q>=S,
rejecting every q causing a frequency alias;
optionally require gcd(q,b)=1 to make T_b
a genuine permutation of its finite clock.

Exact, reproducible minimal **UNIT** clocks:
    (b,N,k)=(16,3,2): q*=7,
              (16,3,3): q*=13,
              (16,3,4): q*=23,
              (16,3,16): q*=277,
              (16,4,2): q*=19,
              (16,4,3): q*=47,
              (16,4,5): q*=173.

For 16,3,16 there are 153 distinct
source multisets. Without the unit
constraint a q=274 grid works; it is NOT
an invertible base-16 source clock.
With gcd(q,16)=1 the first legal q is
277, and every smaller admissible q>=153
is rejected by an exact integer modular
collision witness. Both reproduce the
exact 32nd Haar moment at those dimensions
when the declared source action is lawful.

This is a substantial finite observer cost
improvement over q>4096. It does NOT
resolve source-selected π or imply
normality from a finite sample protocol.

For N=100 and k=16, even the absolutely
necessary number of distinct source
labels is 14,980,162,794,189,827,475.
An N-step time/origin proof cannot ignore
the rapidly growing resource requirements.
It may exploit a smaller *target-relative*
probe grammar if that reduction is proved
instead of assumed.

## MG-04. Unique finite-energy causal BBP Green section (PROVED PAPER)

The genuine BBP forcing is
    r(n)=4/(8n−7)−2/(8n−4)
           −1/(8n−3)−1/(8n−2), n>=1.
It is positive, rational and O(n^-2).

On H=ell²(N_0), define the unilateral
LEFT shift (L t)_n=t_(n+1), ||L||=1.
For b>1, the bounded causal Green
operator is the norm-convergent Neumann
resolvent

    G_b=(bI−L)^(-1)
       =sum_(j>=0)b^(−j−1) L^j.

The SOURCE-SELECTED section is

    T=G_16(r(1),r(2),...),
    T_n=sum_(k>=1)16^(-k)*r(n+k).

It uniquely solves
    16 T_n−T_(n+1)=r(n+1)
within ell², and indeed within ell¹.

**Sharp stability:** for every 1<=p<=infinity,

    ||G_b f||_p <= ||f||_p/(b−1).                   (4)

The bound is SHARP, including on ell²:
take unit-valued source blocks supported on
n=0,...,M−1. The output is
G_b f(n)=(1−b^(−(M−n)))/(b−1)
within the support, so the ratio of
ell² norms tends to 1/(b−1).
The unique finite-energy conclusion holds
because any two recurrence solutions differ
by C*b^n, and that belongs to ell² only
when C=0.

For finite K, the source Section
T_n^K=sum_(j=1)^K 16^(-j)r(n+j)
has the EXACT rational residual
    16 T_n^K−T_(n+1)^K−r(n+1)
      =−16^(-K)r(n+K+1).                           (5)

This is a mathematically precise version
of a "minimal lawful path": the unique
finite-energy causal source trajectory.
It is source typed and not the
physical least-action principle.

**Hostile limitation:** the positive fake
tail T_n*=1/[(n+1)(n+2)] is another unique
ell¹/ell² solution for its own positive
O(n^-2) forcing r*(n)=16T*_(n−1)−T*_n.
But 16T*_0=8 is a rational fixed circle
phase. The same minimal-energy
mechanism can produce a NONNORMAL source.
What distinguishes π is the EXACT four-pole
forcing, not energy-minimality alone.

## MG-05. A no-go for a STATIC source-to-digit Hilbert morphism

Use the DISTINCT BBP spectral carrier
H_G=L²((0,1),dmu), with dmu the genuine
strict positive Hausdorff Green measure
derived in PRs #252/#254, and the
multiplication operator (U f)(u)=u f(u).
Since mu({1})=0, U^n f->0 STRONGLY
for all f by dominated convergence.
Yet ||U^n||=1 for all n, because
the spectrum extends arbitrarily near 1.
It is FALSE to assume uniform operator
norm contraction.

On the circle Hilbert H_T=L²(R/Z,Haar),
the Koopman map K_b f=f o T_b
is an ISOMETRY, because T_b preserves
Haar measure. It need not be unitary.

**No bounded linear intertwiner theorem.**
If J:H_G->H_T is bounded and satisfies
    J U=K_b J,
then J=0. Indeed
    ||J f||=||K_b^n J f||
           =||J U^n f|| ->0
for every f.

This explicitly rules out a large but
tempting class of time-independent
source-morphism claims. It does NOT
rule out time-indexed interfaces,
unbounded operators, distributions or
nonlinear boundary evaluation.

**Stronger continuous nonlinear no-go.**
Let H be a connected real Hilbert space
and U a strongly stable bounded linear
operator (U^n f->0). If a continuous
map Phi:H->R/Z obeys
    Phi(Uf)=T_b(Phi(f))
for all f, then Phi is CONSTANT,
and its value is a fixed point of T_b.

Proof: Phi(U^n f)->Phi(0); equivariance
says T_b^n(Phi(f))->Phi(0).
Since Phi(0) is fixed, expansion by b
near the fixed point implies every
convergent orbit is EVENTUALLY fixed.
Thus Phi(H) belongs to the countable
set union_(n>=0)T_b^(-n)(Fix(T_b)).
A continuous image of the connected
Hilbert space inside a countable circle
subset is a singleton. QED.

In fact, for a map only defined on
{U^n f:n>=0} union {0}, continuity
at zero already forces Phi(f) to be
preperiodic. Consequently a continuous
time-equivariant static map sending
the genuine strongly decaying BBP
source vector to irrational π phase
is impossible: π is irrational and
cannot have an eventually fixed
T_b orbit.

This uses π's IRRATIONALITY, not
its unknown normality. It identifies
a typed transport impossibility,
not a statistics/cancellation theorem.
The genuine BBP correspondence
    y_(n+1)={16 y_n+r(n+1)}
    {y_(n+1)+T_(n+1)}={16^nπ}
is correctly NONAUTONOMOUS / moving
origin and evades the no-go.

## MG-06. Source-blind least action selects a nonnormal orbit

Take the most obvious nonnegative
geometric step action
    A_N(x)=sum_(j=0)^(N-1)
       |exp(2πi b^(j+1)x)
           -exp(2πi b^j x)|², N>=1.

Its minimum is exactly zero, achieved
iff (b−1)x=0 mod1; the b−1
fixed points are rational and
NONNORMAL. For b=16, all 15
source-free zero-action minimizers
are periodic, not Haar-generic.

So "the universe takes the simplest
or least-cost path" is not an
available source theorem for π.
It must specify WHAT action or
optimization is being minimized
and why the TRUE authenticated
four-pole π source satisfies its
load-bearing hypotheses.

## MG-07. The remaining legitimate π normality frontier

There are three distinct mathematically
closed results here:

(1) Haar-ENSEMBLE lacunary moments
    and their first base-b carry;
(2) minimal cost to represent those
    moments in a finite origin grid;
(3) unique finite-energy Green section,
    with an impossibility of a
    static continuous time-equivariant
    source-to-digit map.

NONE yields a bound for the π-selected
signed Fourier sums
    sum_(j<N)e(h*16^j*π).

The current sibling research PR #258
already decomposes authenticated
BBP p=8m+1 prime-window sums into
a p-local Bourgain–Glibichuk–Konyagin
controlled sector and a signed
complementary high-mode overlap
J_(p,d)(h). That overlap is a
target-sufficient scalar, not an
absolute prime-word path cost.
Its actual-source decay remains OPEN.

A maximally correlated complementary
clock v_t=conjugate(u_t) is itself
generated by a simple one-step
multiplication rule, but makes
sum u_t v_t=maximal. This is
an inherited #258 adversarial
witness that simplicity/low
description length is not
automatically decorrelation.

The strongest next mathematical
objective is a new, authentic-source
noncircular signed estimate for
that complementary BBP overlap,
or for the π-selected cyclotomic
lag C_d(N;π). Test candidate claims
against rational Green counterfeits,
3-adic periodic clocks, fixed
origin x=0, p-primary masks,
and the new minimal-moment-clock
alias controls. If a proposed
source->phase functor is both
time-homogeneous and continuous,
MG-05 invalidates it and
saves an entire failed research round.

**Status:** a useful proof and negative-result
addition to SUCC, not a resolution of
π normality, not a statement about
nature's universal optimization, and
not a license for an RH claim.
