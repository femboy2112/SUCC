# Learning as a signed, phase-preserving quotient

**Status: PROVED FINITE/PAPER. Original-zero signed covariance: OPEN.**
These statements develop the positive interpretation of CH7: a more informed
observer can remove reconstructible carrier phase and expose the complementary
response, even as the response's correlation with the carrier increases.
They do not infer arithmetic cancellation from the amount of information learned.

The algebra below is classical finite conditional expectation and unitary
conjugation, proved here with the sharp constant needed by the source instrument.
The contribution within this dossier is the source-compatible quotient, its
exact conditioning constant and a signed refinement ledger. No worldwide
novelty or new general category is asserted. The observer is the existing SUCC
finite transcript map; its fibers define the partition used below.

## QS1. The learned quotient is an optimal approximation of the source signal

Let `(Omega, mu)` be a finite probability space with positive atom weights.
Write `E` for expectation, `||f||²=E|f|²` and
`<f,g>=E(conjugate(f)g)`. Let `F` be a partition of Omega into nonempty cells,
and `P=P_F` conditional averaging on those cells. Let `a` be a unit complex
phase, `|a(omega)|=1`, let `b` be any complex function, and put `z=ab`.
Define multiplication `M_a f=af` and

    Q_(a,F) = M_a P_F M_conjugate(a),
    s_F = Q_(a,F) z = a P_F b.                              (QS1)

Then `Q_(a,F)` is the orthogonal projection onto

    V_(a,F) = {a f : f is F-measurable}.

In particular `s_F` is the unique best mean-square approximation to the
full source signal `z` among all local-phase-modulated transcript functions:

    ||z-a f||² = ||b-Pb||² + ||Pb-f||²,                     (QS2)
    ||z-s_F||² = ||b-Pb||².

**Proof.** Multiplication by a is unitary, so unitary conjugation of the
self-adjoint idempotent P is the orthogonal projection onto the indicated
image. The expression for Qz follows from `conjugate(a)z=b`. Pythagoras for
`b=Pb+(b-Pb)` proves QS2, including uniqueness up to zero-weight atoms.

Precisely, the Hilbert quotient `L²(Omega)/V_(a,F)^perp` is identified
isometrically with `V_(a,F)` by Q. This is a mathematical quotient relative to
a specified transcript and carrier phase; the underlying source z is unchanged.
`Pb` contains the part
of the complement visible to that observer; the omitted component is
orthogonal to the allowed model class. The model is an empirical conditional
response, not automatically a strictly-past causal prediction rule.

## QS2. A sharp constant compares quotient learning with learning the signal

For a cell C write `mu_C=E[a|C]` and `v_C=1-|mu_C|²`. Then

    ||P_F-Q_(a,F)||op² = max_C v_C.                        (QS3)

The maximum is over occupied cells only. Thus, for every b,

    ||P_F(ab)-a P_Fb||²
       <= sum_C Pr(C) v_C E[|b|²|C].                      (QS4)

If `|b|<=1`, this is at most

    V_a = E|a-P_Fa|² = sum_C Pr(C) v_C.                   (QS5)

**Proof of the exact constant.** On each cell with its conditional probability
inner product, P is the rank-one projection onto the unit vector 1, and Q is
the rank-one projection onto the unit vector a. If `v_C=0`, those ranges agree.
Otherwise, on their two-dimensional span, direct expansion of the two
rank-one projectors gives `(P-Q)²=v_C I`; on the orthogonal complement both
projectors vanish. Consequently the cell operator norm is `sqrt(v_C)`.
This is attained already by the unit input 1, because
`||(P-Q)1||²=||1-a conjugate(mu_C)||²=v_C`. The whole space is an orthogonal
direct sum of cells, so its norm is the maximum cell norm. Apply this cellwise
to `z=ab`, noting `|z|=|b|`, to obtain QS4 and QS5.

For any circle samples x, any fixed nonzero integer h, any integer M>=1,
and cells `floor(Mx)`, take `a=e(hx)`, where `e(t)=exp(2 pi i t)`.
Each cell has width at most 1/M. Comparison with its midpoint phase and
`|e(u)-e(v)|<=2 pi |u-v|` gives

    max_C v_C <= min(1, pi² h²/M²).                       (QS6)

The same conclusion holds for a rotated circle partition: choose a continuous
lift on each circular cell, including a cell crossing 0. For the exact local
digit transcript M=16^d, increasingly accurate knowledge of a therefore makes
the learned quotient `aPb` uniformly close, as an operator, to the ordinary
conditional source signal `P(ab)`. This statement holds for every complement,
including the authentic complement and coherent hostile complements.

The small difference in QS4 is a rigorous candidate for the user's "remaining
difference": it is the noncommutation error between learning and demodulating.
Its exact controlling quantities are the cell phase variances v_C. No universal
Euler--Mascheroni value follows from this finite identity; a proposed gamma
asymptotic requires an additional, specified normalization and source theorem.

## QS3. The signed mean survives the quotient with a controlled error

Let `W=E z`, `a_F=Pa`, `b_F=Pb`. The exact identities are

    E(Pz) = W,
    W - E(s_F) = E[(a-a_F)(b-b_F)],                       (QS7)
    Cov(a,b) = Cov(a_F,b_F) + E[(a-a_F)(b-b_F)],           (QS8)

where `Cov(f,g)=E(fg)-(Ef)(Eg)` is bilinear, without a conjugate.
Consequently

    |W-E(s_F)| <= sqrt(V_a V_b),
    |Cov(a,b)-Cov(a_F,b_F)| <= sqrt(V_a V_b),              (QS9)

with `V_b=E|b-Pb|²`. Moreover `E(s_F)=E(a_F b_F)`.

**Proof.** Conditional expectation preserves the mean. Cellwise, the mixed
products between a cell-constant function and a conditional-mean-zero
residual have mean zero. Expand `ab` and retain those terms; Cauchy--Schwarz
bounds the residual product. Subtract the unchanged product of means for QS8.

For unit b and digit cells this gives the deterministic error
`|W-E(s_F)|<=pi |h|/M`, independently of any mixing premise. Thus learning
can indeed sharpen the signal by removing a rigorously small nuisance error.
The surviving signed quantity is `E(a_F b_F)`. Its smallness is a source
question. Retaining it is essential; bounding only the removed error would
replace the intended signal by zero without a mathematical reason.

It is possible for QS9's mean error to be exactly zero while the reconstruction
error `||z-s_F||` is 1. For instance take a constant on each of two cells and b
equal to +1 and -1 equally within each cell. Then Pb=0, z has unit modulus,
and W=0. A precise mean estimate and recovery of the whole trajectory are
different achievements.

## QS4. Refinement reveals a signed scale decomposition

Let `F_0 subset F_1 subset ... subset F_D` be nested transcript partitions,
with F_0 trivial. Hold the same a,b,z fixed throughout. Put
`a_d=P_d a`, `b_d=P_d b`, `s_d=a b_d`,
`Delta a_d=a_(d+1)-a_d`, `Delta b_d=b_(d+1)-b_d`.
Then the projections `Q_(a,F_d)` have nested ranges and

    ||z-s_d||² = ||z-s_(d+1)||² + ||s_(d+1)-s_d||²,
    ||s_(d+1)||² - ||s_d||² = ||Delta b_d||².              (QS10)

The signed covariance is resolved by the exact increments

    Cov(a_(d+1),b_(d+1))-Cov(a_d,b_d)
       = E[(Delta a_d)(Delta b_d)],                       (QS11)
    Cov(a,b) = sum_(d=0)^(D-1) E[(Delta a_d)(Delta b_d)]
               + E[(a-a_D)(b-b_D)].                      (QS12)

Increments at different depths have bilinear mean zero, as well as being
orthogonal for the Hermitian inner product, since each earlier increment is
measurable at every later level. Their individual signed contributions obey

    |E[(Delta a_d)(Delta b_d)]|
       <= ||Delta a_d|| ||Delta b_d||.                   (QS13)

The unsigned norms in QS10 improve monotonically. The complex increments in
QS11 and their real parts need not have a monotone sign. This preserves the
information needed to seek cancellation between depths instead of charging
every learned correlation as a positive cost. If F_D consists of singletons,
the final residual vanishes exactly, so QS12 is a finite exact accounting
identity. It is not an estimate of that sum for the authentic source.

**Proof.** Unitary conjugation preserves nested orthogonal projections and
their Pythagorean energy identity, yielding QS10. Expand the two conditional
products at adjacent levels. Cross terms have mean zero by conditional
centering. The means of a_d,b_d are independent of d, proving QS11. Sum it,
then use QS8 for the last residual. Cauchy--Schwarz gives QS13.

## QS5. Exactly which gauges are removed

For any F-measurable unit phase g, change the split by

    a' = g a,  b' = conjugate(g)b.

The physical signal z is unchanged, and multiplication by g commutes with P.
Therefore

    Q_(a',F)=Q_(a,F),
    a' P b' = a P b,
    (Pa')(Pb')=(Pa)(Pb).                                 (QS14)

This proves the learned quotient depends only on the orbit of the carrier
phase under transcript-measurable gauge changes. A different gauge at every
atom is not an allowed invariance unless F sees those changes. For example,
on two equally weighted points let F be trivial and a=b=(1,-1). Then z=1,
but aPb=0. With g=a the transformed split is a'=b'=1, and a'Pb'=1. The source
signal is invariant while the chosen finite instrument changes. The gauge,
memory partition, phase anchor and source signature therefore remain declared.

Changing the selected prime is not automatically covered by QS14: the ratio
of the two local phases must be F-measurable, or its transport error must be
bounded separately. This prevents an arbitrary split from creating a
spuriously universal "residual constant".

## QS6. Original-source instance and the remaining theorem

Retain the immutable source

    U_0=0,
    U_n=16 U_(n-1)+4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).

On each epoch J_A={A,...,2A-1}, with uniform time weights, select the proved
prime p_A and write

    a_n=e(h[U_n]_pA), b_n=e(h(U_n-[U_n]_pA)), z_n=e(hU_n).

The original rational state and integer carries are untouched. Use F_A given
by a declared local-phase digit transcript, or any authenticated observer
fiber refining it. For M_A=16^(d_A) with fixed h and d_A tending to infinity,
QS6--9 give

    W_A(h;0)=E_J[(P_F a)(P_F b)]+o(1).                    (QS15)

With the earlier proved local marginal `E_J a ->0`, also

    W_A(h;0)=Cov_J(P_Fa,P_Fb)+o(1).                       (QS16)

Here the error is explicit: at most `pi|h|/M_A` in QS15, and at most that
plus `|E_J a|` in QS16 for unit b. No assumption that b is predictable or
independent of a is used. Thus a genuinely source-specific signed estimate
for the coarse conditional product, or for the scale contributions in QS12,
would complete the already audited covariance-to-Weyl step. Such an estimate
for every fixed h!=0 and every sufficiently large integer A remains OPEN.

There is an exact finite saturation point on a clean p-clock: its distinct
phase values are k/p, so M>=p makes `floor(Mx)` distinguish every distinct
local phase. Then a is F-measurable, Q=P and the demodulation discrepancy is
zero. Times with the same local phase can still have different complements;
`V_b` need not be small. On an epoch consisting of complete local periods,
these fibers are exactly the time classes modulo `ord_p(16)`, and Pb is the
earlier folded complement. This identifies the new quotient with that
existing object rather than introducing a second incompatible construction.
The statement is restricted to the clean prime clock: later pole births can
change its denominator and require the actual new phase support to be used.

These reductions refine the instrument and isolate the signed target. They
are not a weaker conjecture already settled by the projection algebra.
The control b=conjugate(a) gives z=1 and W=1, while

    E(s_F)=E|Pa|²=1-V_a ->1.

In this control a growing learned correlation is exactly successful signal
recovery. The original-zero source may give a different signed outcome; the
same projection theorem deliberately works for both, so arithmetic must
decide that difference.

## Provenance and next discriminator

Dependencies inspected: AGENTS.md and docs/METHOD.md; CH7 at pinned parent
`a974db527c19708006b9f6d7f0ca01d08d1e0524`; covariance_forge CFS5; original
prime/source transport and signed normality handoff. QS7--9 include the prior
CH7 conditional covariance identity; they are retained here to fix its relation
to the new conjugated projection. No external theorem is required beyond the
finite algebra proved in this note. Independent exact Gaussian-rational tests
in this directory exercise QS1--14, including sharpness, refinement, sign
failure and gauge mutation. They do not test an infinite-source theorem.

The highest-value discriminator is the source-selected signed depth ledger
`E[(Delta a_d)(Delta b_d)]`, with exact phase transport and the remaining
within-cell defect retained, compared with matched coherent wrong-seed
controls. A repeatable normalization involving Euler--Mascheroni must first
identify which of these scalar quantities it describes and demonstrate
stability under the declared observer changes.

**Pi base-16 normality: OPEN. RH: OPEN.**
