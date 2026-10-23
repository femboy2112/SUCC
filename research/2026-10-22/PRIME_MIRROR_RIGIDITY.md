# Prime-mirror rigidity and finite-probe obstructions

Date 2026-10-22. **CLASSICAL / PAPER PROVED elementary reconstruction**, with
**PROVED LOCAL / EXACT FINITE** regression controls. No priority or Lean claim.
Definitions and reference completion are in [foundations](ARITHMETIC_ER_EPR_FOUNDATIONS.md).

## B1. The exact arithmetic mirror

For every beta>1 and every prime p,

    (V_p⊗I)Omega_beta = p^(beta/2)(I⊗V_p*)Omega_beta.

Proof: the left coefficient at |pn,n> is Z^-1/2 n^-beta/2. On the right only
the summand m=pn survives, with coefficient
p^(beta/2)Z^-1/2(pn)^-beta/2. They agree, and both series converge in norm
because V_p,V_p* are bounded. The orientation is essential: changing the
factor to p^-beta/2 fails already at |p,1>. The right unscaled vector has norm²
p^-beta; the factor restores normalisation. Composite m obeys the same identity
with m^(beta/2), but calling m=6 an independent prime coordinate is invalid.

## B2. Complete complex rigidity theorem

**Theorem.** Fix a scalar c_p in C for every genuine prime. There is a nonzero
vector Psi_a=sum_n a_n|n,n> in H⊗H satisfying all prime mirrors

    (V_p⊗I)Psi_a = c_p(I⊗V_p*)Psi_a                       (B2.1)

iff every |c_p|>1 and sum_p |c_p|^-2<infinity. When these conditions hold,
all such vectors form one complex line, with

    a_n=a_1 product_p c_p^-v_p(n),
    ||Psi_a||²=|a_1|² product_p(1-|c_p|^-2)^-1.           (B2.2)

A normalised solution is unique up to overall phase; |a_1|² is the reciprocal
Euler product. There is no assumed positivity, continuity or prior
multiplicativity of amplitudes.

**Proof.** If c_p=0, (B2.1) and isometry of V_p force Psi=0. Otherwise comparing
the orthonormal coefficient |pn,n> gives a_n=c_p a_pn for every n. Repeatedly
remove prime factors; unique factorisation gives (B2.2) and shows that a_1=0
would force all a_n=0. Conversely the displayed formula satisfies every
coefficient relation; boundedness makes coefficient equality vector equality.
Writing q_p=|c_p|^-2 and summing nonnegative squares over finite-prime smooth
integers gives product_(p in F)(1-q_p)^-1. If q_p>=1, even the p-power
subseries diverges. With all q_p<1, monotone convergence over increasing F
therefore gives the stated norm product. This product is finite iff
sum_p -log(1-q_p)<infinity, iff sum_p q_p<infinity: q<=-log(1-q), and after
finitely many terms q<=1/2 and -log(1-q)<=2q. This proves necessity,
sufficiency, and uniqueness. QED.

This is a direct unique-factorisation/Euler-product theorem, not a claim that
mirror equations alone authenticate an unknown physical prime source.
Relabelled or composite generators require a fresh relations presentation.
For example treating 2,3,6 as independent coordinates counts 6 twice; actual
multiplication forces c_6=c_2 c_3 whenever the nonzero full reconstruction holds.

## B3. Phase information, degeneracies and equivalences

Write c_p=r_p exp(i theta_p). The amplitude phase is the completely
multiplicative character exp(-i sum_p v_p(n)theta_p), times the global phase.
All one-side reduced densities depend only on r_p. Two states with distinct
phase characters therefore have the same entanglement spectra and all diagonal
number statistics, but generally different mirror equations for the fixed V_p.
The unitary D e_n=exp(-i sum_p v_p(n)theta_p)e_n on one side transforms the
positive-amplitude state to this state. It simultaneously conjugates each
V_p by exp(-i theta_p). Thus equivalence is valid only if the source/probe
basis transformation is transported too; it is not equality at fixed probes.

Coincident reduced eigenvalues allow alternative Schmidt bases. This does not
weaken B2, which fixes the actual number basis and multiplication operators.
It prevents reconstruction of that basis from the reduced density alone.

A general bounded operator X has a right mirror on the vector only when the
formal transpose-weighted operator M=rho^(1/2) X^T rho^(-1/2) is well-defined
on the needed domain and extends appropriately. Indeed coefficient comparison
of X rho^(1/2) with rho^(1/2) M^T gives this formula. For X=V_p it reduces to
M=p^(beta/2)V_p*, a bounded operator. An arbitrary bounded X need not have a
bounded mirror: X=V_p* gives a bounded mirror p^-beta/2 V_p here, but maps
moving small basis indices up to much larger ones can violate uniform
weight ratios. Example X e_(2k+1)=e_(2^k), k>=1, zero elsewhere, is a bounded
partial isometry and its formal mirror has coefficients
(2^k/(2k+1))^(beta/2), unbounded. The modular construction in A5 supplies the
correct unbounded-domain framework, not permission to ignore this failure.

## B4. Exactly what finitely many prime constraints determine

Let P be a finite set of primes with nonzero c_p. Every n has a unique
n=r s, where r has no prime factor in P and s is P-smooth. All solutions of
the mirrors for p in P have exactly the form

    a_(rs)=b_r product_(p in P)c_p^-v_p(s).

Proof: remove only factors in P. The recurrence never changes r, so b_r is
arbitrary and the converse is immediate. A nonzero square-summable solution
exists iff every |c_p|>1; then its norm² is

    [product_(p in P)(1-|c_p|^-2)^-1] sum_r |b_r|².

Consequently finitely many prime constraints leave an entire ell² space of
unobserved rough-source amplitudes. Example: b_1!=0, all other b_r=0 gives a
normalised P-smooth-only source. It obeys every selected prime mirror globally,
but for any q outside P violates the desired q-mirror at |q,1>, because a_q=0
and a_1!=0. A finite list of matched prime *coefficients* is even weaker.

**Probe closure:** to infer a_n from a_1, it suffices to know the recurrence
on the edges of one prime-factor path from 1 to n. To infer all amplitudes,
one needs a connected spanning family of these coefficient edges (or an
independently proved universal recurrence). To identify the whole Hilbert
vector also requires its summability and the fixed basis/completion. Any
finite edge set misses some vertex and permits an amplitude mutation there.
Independent full mirror constraints for every prime provide one sufficient
closure; they are stronger than observing a finite set of expectation values.

## B5. Composite-amplitude mutation: exact receipt

Starting from a_n=n^-1 (beta=2 before normalisation), change only a_6 to 2a_6.
Do not change a_1,a_2,a_3 or any other prime amplitude. For p=2 the residual
coefficients a_n-2a_2n occur at n=3 and n=6; for p=3 they occur at n=2 and
n=6. For every other prime p, the equation at n=6 also detects the mutation
if its coefficient a_(6p) is probed. Thus “only p=2 or p=3 can detect an
error at 6” is false for the complete global operator equations, though those
are the two incoming factorisation edges. Finite cutoff N=42 checks p=2,3,5,7.
Normalising the entire vector multiplies every residual by one common factor
and does not erase a nonzero defect.

## B6. Exact cutoff residual and nonmonotone convergence

Set Z_N=sum_(n=1)^N n^-beta and
Omega_(beta,N)=Z_N^-1/2 sum_(n=1)^N n^-beta/2 |n,n>, embedded in full H⊗H.
With M=floor(N/p), the **full-space** residual is exactly

    R_(N,p)=[(V_p⊗I)-p^(beta/2)(I⊗V_p*)]Omega_(beta,N)
           = Z_N^-1/2 sum_(n=M+1)^N n^-beta/2 |pn,n>,
    ||R_(N,p)||² = (Z_N-Z_M)/Z_N.                         (B6.1)

All n<=M coefficients cancel; all remaining left outputs leak beyond the
right truncated input's matching support. For beta>1 and M>=1, the integral
test gives

    ||R_(N,p)||² <= M^(1-beta)/[(beta-1) Z_N] → 0.

For M=0 the residual squared is exactly 1. The residual need not decrease at
every integer N: p=2,beta=2 gives 1/5 at N=2 and 13/49 at N=3. The changing
floor makes such oscillations unavoidable. This is a verified exact negative
control, not a floating convergence anomaly.

If BOTH operators are compressed to H_N=span{e_1,...,e_N}, the same mirror
identity is **exact at every finite N**: the leaked left terms have also been
discarded. Therefore a finite matrix zero residual does not certify infinite
normalisability or convergence. At beta=1 it is still exactly zero in the
compressed model, although the infinite coefficient vector is not in H⊗H.
The module exposes `output_cutoff` so this false-positive mechanism is testable.

For beta>1, the separately normalised infinite/cutoff TFDs satisfy

    |<Omega_beta,Omega_(beta,N)>|²=Z_N/zeta(beta),
    ||Omega_beta-Omega_(beta,N)||²=2(1-sqrt(Z_N/zeta(beta))).

The missing mass is bounded by N^(1-beta)/[(beta-1)zeta(beta)]. These are
analytic truncation error bounds, not a claim of monotonic mirror residual.

## B7. Exact oracle, controls and outstanding boundary

`observational_succ/arithmetic_tfd.py` uses Q(i) without floating arithmetic.
Its thermal oracle covers integer amplitude exponents s>=1 (beta=2s), whereas
the paper proves all real beta>1. It verifies sparse full-output operators
against an independent rational tail sum, compares prime enumeration with the
pre-existing source oracle, directly performs a finite partial trace, and
retains phase, orientation, composite-source, zero-vector and leakage controls.
Run:

```sh
python -m unittest discover -s tests -p 'test_arithmetic_tfd.py' -v
python -c 'from observational_succ.arithmetic_tfd import probe; print(probe())'
```

Fourteen tests pass in the lane's local run (including weighted-transpose
orientation and complete-instrument no-signaling controls). Exact command receipts and
final commit scope belong in the integrated research receipt; this statement
is not a claim about CI. No paper theorem was established by those fourteen tests.

Next verdict-changing probe: a separately specified code intertwiner must
transport at least a noncommuting authenticated arithmetic operator pair,
with an erasure-access law that survives changed phase and rough-source controls.
B2 alone fixes a state in one source presentation, not a spatial bulk.

Quantitative extension: [Prime mirror stability](PRIME_MIRROR_STABILITY.md) proves
a global gap, finite-prime kernel projection, and an analytic-tail fidelity certificate.
