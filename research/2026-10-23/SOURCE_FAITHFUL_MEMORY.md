# Exact carry memory and minimal future linear realization

**Authority:** paper proofs and independent exact rational finite witnesses.
No Lean claim for this manuscript. Classical projection/realization mechanisms
are specialized here to the authenticated arithmetic successor. Academic
priority is unverified.

## M1. All future compressed actions

On H=ℓ²(N≥1), S e_n=e_(n+1). Let J_a e_m be the normalized uniform vector
on the a addresses a(m−1)+1,...,am, and A_a=J_a*. For a≥2, n=aq+r,
0≤r<a, direct intersection of translated blocks gives the bounded-operator identity

    F_n := A_a S^n J_a = (1−r/a) S^q + (r/a) S^(q+1).             (M1)

Proof: each initial block has a−r addresses landing in its q-th successor
block and r in the next. Each pair of normalized block amplitudes contributes
1/a. This proves the matrix elements on every basis vector and hence the
operator identity by boundedness. In particular F_0=I and F_a=S, whereas

    C := F_1 = (1−1/a)I+S/a,
    F_2−C² = −(S−I)²/a² ≠ 0.                                 (M2)

The nonzero claim follows by applying (S−I)² to e_1. It holds at a=2 as well.
Thus the exact one-step compressed successor is not an exact future simulator.
Replacing F_n by C^n is a different process, with fresh averaging at every step.
The discrepancy is a future-action defect, not an error in the block isometry.

## M2. Exact memory elimination

For any Hilbert space, bounded T and orthogonal projection P, set Q=I−P.
For initial v_0 in ran P, write x_n=P T^n v_0 and y_n=Q T^n v_0. Then

    x_(n+1)=PTP x_n+PTQ y_n,
    y_(n+1)=QTP x_n+QTQ y_n,   y_0=0.

Induction eliminates the hidden state:

    x_(n+1)=PTP x_n + Σ_(j=0)^(n−1) PTQ (QTQ)^j QTP x_(n−1−j). (M3)

For arbitrary y_0 add PTQ(QTQ)^n y_0. This is a finite algebraic identity at
every n; no infinite series, stationarity or Markov assumption is used. The
kernel's first term can be signed even when T is unitary. For the carry source,
P=J_a A_a and T=S, (M3) reconstructs (M1) exactly. Omitting QTP is justified
only with a genuine invariance condition; small current observational error
does not supply that condition.

## M3. A sharp minimal realization in a declared phase fiber

This section uses an explicitly different comparison: bilateral block Fourier
fibers, or equivalently a formal substitution of scalar z for the coarse shift.
It does NOT diagonalize the unilateral S of M1. Define the a×a carry matrix

    T_a(z)e_r=e_(r+1) (r<a−1),  T_a(z)e_(a−1)=z e_0,
    u=a^(−1/2)(1,...,1),  f_n(z)=u* T_a(z)^n u.

The matrix is unitary for |z|=1. For all complex z and n≥0, the same counting
proof gives f_n(z)=(1−r/a)z^q+(r/a)z^(q+1). As a formal power series,

    Σ_(n≥0) f_n(z)t^n = N_a(t,z)/(1−zt^a),
    N_a(t,z)=Σ_(r=0)^(a−1) ((a−r)+rz)t^r/a.                    (M4)

**Theorem.** For z≠0,1, every finite-dimensional time-invariant linear
realization f_n=c*R^n b requires dimension at least a, and T_a(z) attains a.
For z=1 the minimum is 1. This is a statement about exact all-time scalar
responses in a fixed phase fiber, not about all possible nonlinear encodings.

Proof: at any root t of 1−zt^a, t≠0,1 and

    N_a(t,z)=(z−1)²t / [a z(1−t)²] ≠ 0.

To verify, use the finite geometric sum and its derivative, then substitute
t^a=1/z. Thus numerator and denominator have no common root. The denominator
has degree a with a distinct roots since z≠0. A d-dimensional realization has
generating function c*(I−tR)^(-1)b whose reduced denominator has degree at
most d (adjugate formula). Therefore d≥a. The displayed carry matrix provides
the upper bound. At z=1, f_n=1 for all n, so dimension 1 suffices and zero
dimensions cannot give f_0=1. No minimality statement is made here at z=0.

At a=2,z=−1, f_n=1,0,−1,0,1,...; one-step compression gives c=0 and
incorrectly predicts every later response zero. The exact hidden kernel has
k_0=−1 and k_j=0 for j>0, yielding f_(n+1)=−f_(n−1). This null first
response is a particularly cheap decisive test of discarded memory.

The Hilbert tensor environment also has a conditional dimension lower bound:
if each quotient block must embed isometrically into |m>⊗E, its a orthogonal
source vectors require dim E≥a. Without this fiber-preserving condition,
abstract separable Hilbert isomorphisms invalidate such a dimension argument.

## M4. What this repairs and what it leaves open

The carry register supplies an exact finite internal realization per coarse
fiber. Equivalently one can retain a convolution memory kernel. These are two
representations of future dependence, not permission to call the visible map
lossless. On a fixed source and observation, minimal behavioral quotients and
minimal linear realizations answer different questions; their minimality
categories must not be conflated.

The [heat manuscript](SOURCE_FAITHFUL_LIMITS_HEAT.md) computes
J_a* L_ε J_a=a L_(aε). Exponentiating this compressed generator loses the
hidden memory, whereas compressing the original heat evolution retains it.
The resulting distinct diffusion limits are a quantitative continuation of
M2, with their analytic hypotheses supplied separately there.

The exact memory mechanism is classical. Relevant primary sources are
[Ho–Kalman 1966, original NASA record](https://ntrs.nasa.gov/citations/19670049337)
and [Chorin–Hald–Kupferman 2000, author copy](https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf).
The former concerns minimal state realization; the latter projection and
unresolved memory. Our proofs above are elementary and do not invoke their
theorems without checking hypotheses. The source-specific formulas, explicit
false-step witness and integration with SUCC's preservation ledger are the
contribution of this round, not a claim to invent memory or realization theory.

## Executable calibration

`source_faithful_memory.py` implements three routes: quotient-moment formula,
labelled companion matrix evolution, and exact hidden-state elimination.
Tests compare them at radices 2,3,5,7 and phases −1,1,2/3. Radix 11 and
composite 6 are holdout/mutation controls; rational z=2/3 is an algebraic
parameter, not a unitary physical phase. Exact Hankel determinants verify
finite minimality witnesses and the constant-mode rank drop. Universal
minimality is proved by M4's reduced denominator argument, not these tests.
