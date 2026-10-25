# BBP TWISTED-PAIR OBSERVERS — source-coherent differentials, dual clock transport, and the selected π gap
## 24 October 2026 · Research-only proof forge

**Parent:** SUCC main e648df3e4fca73ab6b942232b5ca4b310e9cac08,
the consolidated Academic Main IX π/circle/BBP/prime-clock frontier.
**Separate ongoing draft:** PR #266 lag/carry rigidity, not a parent and not
silently integrated here. Read its current head separately.
**Authority:** elementary exact paper proofs, independently tested
integer/Fraction arithmetic, and the published BGK subgroup estimate
as an EXTERNAL theorem. No new Lean proofs in this branch.
**π normality in base 16, 2, 10 or absolutely: OPEN.**
Scientific novelty outside SUCC: UNVERIFIED.

## Motivation and physical analogy, carefully typed

On an actual electrical twisted pair, a differential receiver subtracts the
two wire voltages. Common-mode noise cancels when the two lines experience
similar coupling; the twists reduce systematic imbalance. No statement about
stochastic independence or a physical π experiment follows from the analogy
(Analog Devices, *Understanding Common-Mode Signals*; Campbell Scientific,
*Minimizing Noise in Sensor Signals*, white paper).

On the circle, common additive phase becomes a common MULTIPLICATIVE phase
after z=exp(2πix). Two coupled mathematical observers compare phases by
z_a*conj(z_b). Their data are different from absolute phase readouts.

The genuine BBP source is
    r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2);
    y0=0; y_(n+1)={16*y_n+r(n+1)}.
In a p=8m+1 first-birth window, n=m+1+t, 0<=t<Delta=3m,
the existing exact source theorem is
    y_n={4*16^t/p+w_t}, with every w_t p-free,
    w_(t+1)={16*w_t+r(m+2+t)}.
Define c=4h, e(x)=exp(2πix), and the RELATIVE GALOIS family
    Z_t(a)=e(c*a*16^t/p)*e(h*w_t), a in F_p^*.
These are mathematically lawful conjugates in the extension generated
by zeta_p; only a=1 is the selected actual BBP source. The other labels
are NOT independent physical observations and do NOT preserve y0=0
as separate actual starting states.

## TPD-01 — affine common-source SUCC and its observer torsor

For any abelian circle A=R/Z and any common forcing f_t, solutions
x_(t+1)=b*x_t+f_t and x'_(t+1)=b*x'_t+f_t obey
    delta_(t+1)=b*delta_t, delta_t=x_t−x'_t.
Different drives f,g give
    delta_(t+1)=b*delta_t+(f_t−g_t).

Thus the solution family is a torsor over homogeneous base-b paths:
"source-consistent" comparison cancels the truly common drive.
It does NOT imply delta=0, shortness of delta, or mixing of either
absolute path. In particular a zero difference at one time remains
zero only if the drives continue to agree.

If the two wires are interchanged at each time, the signed difference
changes sign. Keeping the orientation connection
    sigma_t=s_t*s_(t+1), s_t in {+1,-1},
and parallel-transporting the sign recovers the original difference up
to one UNKNOWN GLOBAL initial orientation. Without that connection,
alternating wire swaps can manufacture fake signed cancellation even
for an underlying constant quarter-turn signal.
The UNORIENTED squared chord is swap-invariant, and its future obeys
the established Chebyshev polynomial F_b. This can lose the chirality
required by complex signed correlations.

## TPD-02 — source-coherent Galois two-wire cancellation

For any nonzero integer h, odd p=8m+1 prime, distinct a,b in F_p*,
and EVERY actual BBP complementary w_t,
    Z_t(a)*conj(Z_t(b))
       =e(4h*(a-b)*16^t/p).                           (2)
In additive phase coordinates this is
    delta_t(a,b)=4h*(a-b)*16^t/p mod1,
    delta_(t+1)=16*delta_t.
Triple overlaps satisfy delta_ab+delta_bc=delta_ac exactly.

No assumption of randomness, p-free independence, or smallness of
w_t appears. The mathematical differential obeys an authenticated
source-invariant SUCC law despite arbitrary absolute common phases.

**Caution:** comparison between the FULL selected observer y_t(1)
and the p-only observer u_t instead gives w_t; it is a different
pair with a different information contract. Do NOT identify these
two differential constructions.

## TPD-03 — the contragredient "twist" is forward SUCC × backward FUCC

Let a_t=a0*16^(-t) in F_p*, so
    a_(t+1)=16^(-1)*a_t,
    a_t*16^t=a0.
Then
    Z_t(a_t)=e(4h*a0/p)*e(h*w_t).

For ANY s,t in the authenticated p-free window,
    Z_t(a_t)*conj(Z_s(a_s))
       =e(h*(w_t-w_s)).                               (3)

Therefore temporal DIFFERENCES of the actual p-free complement can be
read without knowing the initial wire label a0: the unknown source
choice produces one global phase which cancels in the comparison.

An alternative non-moving source match works for arbitrary lag d:
take a=16^d*b (mod p). Then
    Z_t(a)*conj(Z_(t+d)(b))
       =e(h*(w_t-w_(t+d))).                            (4)
At a full local return d=L=ord_p(16), a=b, so even the
selected fixed embedding can cancel its local clock in that lag.

**Exact target-relative sufficiency.** If one observes the coherently
label-transported record Z_t(a_t) for unknown but FIXED a0, the
reconstructed source-selected complex Weyl-window sum differs only
by a common unit phase:
    sum_t e(4h*16^t/p)*Z_t(a_t)
      =e(4h*a0/p)*sum_t Z_t(1).
Consequently the *magnitude* of the signed selected window sum is
exactly recoverable even without a0. This is a representation/decoder
identity, NOT an estimate making that magnitude small.
The changing a_t is an explicitly costed time-dependent observer
choice, NOT a single global Galois automorphism of the entire history.

## TPD-04 — balanced opposite wires, source product, and uniform decoder

The unordered opposite-embedding pair {Z_t(a),Z_t(-a)} has
    Z_t(a)*Z_t(-a)=e(2h*w_t),
    Z_t(a)+Z_t(-a)=2*e(h*w_t)*cos(theta_t),
    theta_t=2π*(4h*a*16^t/p).
Thus the pair PRODUCT reconstructs the common source at doubled
frequency, independent of wire orientation/label order.
The paired SUM reconstructs e(h*w_t) when theta_t is known up to
sign and cos(theta_t)!=0, as always for odd p and p-nontrivial
theta_t; however a single cosine can be as small as ~1/p.

Use TWO unordered balanced pairs, ±a and ±2a, to avoid this problem.
For every real theta, letting x=cos(theta),
    max(|cos(theta)|,|cos(2theta)|)
      =max(|x|,|2*x²−1|)>=1/2.
Proof: if |x|>=1/2 we are done; otherwise 2*x²<1/2 and
|2*x²−1|>1/2. Choose the better pair. If each complex
wire value has additive error at most epsilon, the recovered
e(h*w_t) has error at most 2*epsilon. This is a UNIFORMLY
conditioned four-channel source decoder insensitive to swapping
the conductors WITHIN either known opposite pair.

It requires the source-justified two pair identities and actual
conjugate-channel access. A single labelled channel has a trivial
matched-phase demodulator; the four-channel value is stability
WITHOUT within-pair orientation labels.

## TPD-05 — exact finite Galois-differential chord moments = Kummer moments

Average over ORDERED distinct labels (a,b) in (F_p*)².
Require p not dividing h. For every nonzero d in F_p, precisely p−2 such pairs have a−b=d.
Therefore their DIFFERENTIAL phase is uniformly distributed over
the p−1 nonzero pth roots, independently of t and w_t.

Let D_ab=|1-Z_t(a)*conj(Z_t(b))|². For k>=1,
    D^k=sum_(j=-k)^k (-1)^j*C(2k,k+j)*z^j.
Root-of-unity orthogonality including removal of z=1 gives
    E_(a!=b) D_ab^k
      = [p/(p−1)] *
        sum_(|j|<=k, p|j)(-1)^j*C(2k,k+j).           (5)

In particular, for 1<=k<p,
    E D_ab^k = [p/(p−1)]*C(2k,k);
for k=p (p odd), the first alias adds exactly -2 INSIDE the bracket:
    E D_ab^p=[p/(p−1)]*(C(2p,p)−2).
For k=0 the mean is 1, not p/(p−1).

The familiar C(2k,k) is exactly the circle's Haar squared-chord moment
and its FULL-PRODUCT Kummer prime-carry integer. Formula (5) is an exact
finite p-primary observer-pair identity, not a statement about π's
absolute time-orbit statistics. The factor p/(p−1) records exclusion
of zero differential. At p=b+1, the first p-grid alias moment 2p
matches the first b-covering ADDITIVE carry moment 2(b+1);
b=16,p=17 is a source-specific double-threshold alignment, not a
normality theorem.

Independent executable oracle: expand all cyclotomic character
coefficients for a=1..p−1, reduce with
1+zeta+...+zeta^(p−1)=0, and recover the rational moment.
Tests include p=17,41,73,97 through k=p.

## TPD-06 — UNCONDITIONAL DIFF-PHASE equidistribution on good prime clocks

Let L=ord_p(16). In the p-free window Delta=3m is a multiple of L.
For good p with L>=p^gamma, external Bourgain–Glibichuk–Konyagin
(Kowalski 2024 exposition, Theorem 1.1) establishes constants
C_gamma,nu_gamma>0 such that for ANY a!=b, fixed nonzero h, any
fixed nonzero Fourier integer j with p>|jh|,

    |(1/Delta) sum_(t<Delta)
       e(4*j*h*(a−b)*16^t/p)|
       <= C_gamma*p^(-nu_gamma).                       (6)

The bound is UNIFORM in the two allowed Galois observer labels,
and holds for ANY actual complementary BBP source w_t because
that source cancels pointwise in the relative observation.

Consequently, for each FIXED k>=1 and sufficiently large p>k,
    |(1/Delta)sum_(t<Delta)D_ab(t)^k − C(2k,k)|
       <= (4^k−C(2k,k))*C_gamma*p^(-nu_gamma).        (7)

This is a real time-averaged, all-good-prime DIFFERENTIAL
equidistribution theorem with a quantitative imported analytic
power saving. It is a TRIANGULAR FAMILY indexed by p, not
normality of a single fixed irrational real.
The absolute selected phases Z_t(1) remain uncontrolled.

External BGK citation:
E. Kowalski, *Exponential sums over small subgroups, revisited*
(2024), Theorem 1.1, https://arxiv.org/abs/2401.04756.
No independent derivation of BGK is claimed.

## TPD-07 — a complete channel Gram is exactly BLIND to the common source

Here p must not divide h. Define the Delta × (p−1) matrix
    A_(t,a)=Z_t(a), t=0..Delta−1, a=1..p−1.
Since |e(hw_t)|=1, each common factor cancels in every
time-same pairwise channel inner product:
    (A*A)_(a,b)/Delta
       =(1/L)sum_(s<L)e(4h*(b−a)*16^s/p).
It is ENTIRELY INDEPENDENT of all complementary w_t.

Let C be its L×(p−1) underlying character matrix. Exact finite
root-of-unity orthogonality gives the L×L row Gram
    C C* = p I_L − 1_L 1_L*.
Its nonzero eigenvalues are p (multiplicity L−1) and
p−L (multiplicity1). Consequently the normalized
(p−1)×(p−1) channel Gram has EXACT spectrum:
    p/L,    multiplicity L−1;
    (p−L)/L,multiplicity 1;
    0,      multiplicity p−1−L.

Its rank is exactly L, however complicated the true BBP
complementary source is. Even complete EXACT knowledge of
that channel Gram cannot identify the common w_t, so cannot
force source-selected π normality.

Individual source-authenticated labelled complex channels
DO carry w_t and can be demodulated (TPD-03/04); this is
a distinction between raw observations and a lossy
gauge-invariant statistic, not an information paradox.

## TPD-08 — a p-free source counterfeit refutes differential→normality

Take a finite window and choose any desired TARGET selected phases
theta_t (for instance theta_t=0 for maximal coherence).
Choose a sufficiently fine q-grid, gcd(q,p)=1, and first solve
    h*w_t ≡theta_t−4h*a0*16^t/p mod1,
then round the solution w_t to the nearest q-grid point.
The selected phase error is <=abs(h)/(2q); all w_t remain p-free.
Define lawful p-free synthetic forcing
    f_(t+1)={w_(t+1)−16*w_t}.
Then the source-independent pair differential (2), all
co-rotating dual identities (3), all channel Gram data
(TPD-07), and all the good-prime BGK differential bounds
remain unchanged. But the selected channel a0 is
arbitrarily close to a CONSTANT, hence its normalized
complex sum is arbitrarily close to one.

This synthetic forcing is NOT the exact four-pole BBP source;
the example refutes only an overbroad deduction from
p-freeness/common-mode cancellation, not π normality.
Exact rational tests use p=41, q=101 and 15 source steps.

A still simpler asymptotic caution: a p-free rational
initial w0 can be chosen exponentially close to -4a0/p;
under ZERO synthetic forcing the homogeneous dynamics
tracks the anti-clock for any prescribed FINITE window,
provided its initial denominator is sufficiently huge.
Low forcing complexity is not a statistical mixing law.

## TPD-09 — the actual remaining π theorem and minimal next probe

The true selected BBP window is the fixed a=1 channel:
    W_p(h)=sum_(t<Delta)e(4h*16^t/p)*e(h*w_t).
Previous SCE/PSC results bound the pure local p sum and
Galois averages, but the source-specific SIGNED high
overlap J_(p,d)(h), or the selected collision statistic
K_p(1), remains UNVERIFIED on an unbounded good-prime
family. Source-coherent DIFFERENTIAL equidistribution
can hold simultaneously with arbitrarily bad
absolute-selected coherence (TPD-08).

The useful future route is no longer "randomize observer
wires until the phases cancel". That would produce an
ensemble effect even for artificial nonnormal sources.
Instead:

(1) Use the paired Galois source to decode exact temporal
    w_(t+d)−w_t via coherent contragredient label transport.
(2) Derive a genuinely BBP-specific quantitative constraint
    on how those differences correlate with the local
    multiplicative clock; source-index forcing, carries,
    and initial state y0=0 are mandatory.
(3) Retain SIGNED complex phase information rather than
    replacing it solely by chord magnitudes or absolute
    prime-edge path costs.
(4) Prove that the resulting signed high-mode inner
    product, or selected-source collision entropy excess,
    has a vanishing all-horizon bound.

A potential tool is source-aware discrete van der Corput
using matched cross-time Galois wire pairs (4) instead of
unmatched absolute trajectories. The exact phase factor
is known; its SUM is still not bounded by these identities.
Any imported subgroup estimate must verify the weights'
actual source structure before claiming a π cancellation result.

**Verdict: we proved a precise two-observer common-mode theorem,
a uniformly stable balanced decoder, a quantitative
differential-arithmetic moment theorem, and an exact Gram/source
no-go. We did NOT prove π normality.**


## TPD-10 — one authenticated curvature reading fixes the unknown input wire

The co-rotating observer record is
    psi_t=4h*a0/p + h*w_t mod 1.
Because w_(t+1)=16*w_t+r(m+t+2) mod 1, its exact
source CURVATURE is
    kappa_t=psi_(t+1)−16*psi_t mod 1
           =h*r(m+t+2)−60h*a0/p mod 1.              (8)

The unknown starting wire a0 contributes one
CONSTANT finite p-primary offset to every curvature readout.
Hence kappa_t−kappa_s=h*(r(m+t+2)−r(m+s+2)) mod1
is independent of the unknown wire label.

If one ABSOLUTE curvature reading is available with the
actual authenticated rational BBP forcing r at that time,
and p does not divide h, then p=8m+1>=17 implies
gcd(60h,p)=1. Define the integer
    z=p*{kappa_t−h*r(m+t+2)}.
The initial Galois wire is recovered exactly by
    a0=−z*(60h)^(-1) mod p.                       (9)

Thus paired temporal differences are source-observable
without the initial label, while ONE authenticated absolute
source/curvature comparison fixes the missing label.
This is an identifiability theorem, not an entropy or
statistical cancellation theorem. Tests cover actual
source windows p=17,41,73,97, a0=1,2,3, every
admissible time and mutated non-p source readings.

Identifying the selected source is NOT proving that its
absolute signed Fourier averages vanish. The latter is
the still-open π normality obstruction.


## TPD-11 — ZERO complement forcing still permits maximal finite absolute resonance

The p-free fake in TPD-08 need not have a complicated synthetic drive.
For any authentic p-primary source clock, any selected label a0,
and any prescribed finite horizon N, choose the p-coprime denominator
    q=p*16^N+1.
Choose w0 on the q-grid nearest to -4a0/p; then
    ||w0+4a0/p||_T<=1/(2q).
Define the ENTIRE complement trajectory by the simplest possible
homogeneous law, with **zero forcing**:
    w_t={16^t w0},    0<=t<N.
Every w_t remains p-free, and
    ||4a0*16^t/p+w_t||_T<=16^t/(2q)
       <=16^(N-1)/(2q)<1/(32p).
Thus the full selected observer looks almost FIXED for the entire
finite N-step window, even though its p-primary differences and
the complete pair/Galois frame machinery remain exact. The initial
p-free conductor is astronomically large, which is a genuine
observation/resource cost: the construction requires exponentially
precise *initial* phase selection.

This example is NOT the BBP source: it replaces both the
p-free initial condition and all later authentic rational
forcing by zero. It proves a useful no-go: coherent common-mode
rejection + all-pair differential equidistribution + a minimal
homogeneous source law do not entail selected normality on
any finite horizon. Authentic source INITIAL DATA and the
actual nonzero forcing remain load-bearing.

Finite exact oracle tests replay q, every p-free denominator,
zero-forcing recurrence and the full error budget for p=17,41,73.
