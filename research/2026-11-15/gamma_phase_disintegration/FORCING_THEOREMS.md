# GP-F — Authentic forcing: global phase retention and zero-free Mellin domain

**Status:** PROVED LOCAL (paper proofs; classical dependencies identified).
**Scope:** the normalized positive forcing law, with explicit Fourier convention.
See `PROVENANCE.md`, `CLAIM_LEDGER.json`, and `VALIDATION.md`.

## 0. Novelty and scope

The exact forcing Mellin transform is inherited from `research/2026-10-26/OILY_MACARONI_SOURCE_MELLIN_HILBERT.md`, section 2. The positive Gamma-2 mixture is also inherited (including the Green mixture in `OILY_MACARONI_SOURCE_BRIDGE.md`, sections 6–8). Source infinite divisibility, root pairing and fractional convolution subdivision are inherited from `research/2026-10-29/recursive_carrier_triangle/ATOMIC_SOURCE_AND_INTERACTIONS.md`; they must not be reported as new.

What the present elementary argument adds is a **global real-frequency, uniform-in-source-time lower multiplier bound**, an explicit source correction confined to a right half-plane, a global Mellin phase chart, and finite-band reconstruction conditioning. The source scalar transform in `research/2026-10-29/oily_logarithm/RESEARCH.md`, section 3, was only asserted to have a local nonzero joint Fourier–Mellin chart. This result concerns its pure Mellin axis, and does not prove global nonvanishing in that two-variable joint family.

No conclusion is claimed for the coherent Green-tail mixture merely from the forcing result. No result here identifies auxiliary source moments with the arithmetic orbit phase, recovers a forgotten seed, supplies R0, or proves normality.

## 1. Definitions and domain

For every real a>0 put

    q(t)=4−2 exp(−3t)−exp(−4t)−exp(−5t), t>0,
    R(a)=4/a−2/(a+3)−1/(a+4)−1/(a+5).

For original BBP time n>=1, a=8n−7 and R(a)=r(n). The probability density

    p_a(t)=exp(−at)q(t)/R(a), t>0

is positive and integrates to one. Let X_a have this law, and Y_a=a X_a. We use **positive** Fourier phase

    Φ_a(ω)=E exp(iω log Y_a)=E Y_a^(iω), ω real.

Write v_3=2, v_4=v_5=1 and ℓ_d=log((a+d)/a)>0. Define

    D_a(ω)=4/a−Σ_d v_d/(a+d) exp(−iωℓ_d),
    S_a=Σ_d v_d/(a+d),  R(a)=4/a−S_a>0.

Euler integration of the four signed channels gives the inherited exact identity

    Φ_a(ω)=Γ(1+iω) D_a(ω)/R(a).                 (1)

All four integrals are absolutely convergent on this line; cancellation is never used to justify an invalid interchange.

## 2. Global right-half-plane theorem and Gamma sandwich

**Theorem.** For every a>0 and every real ω,

    Re [Φ_a(ω)/Γ(1+iω)] >= 1,
    |Γ(1+iω)| <= |Φ_a(ω)| <= |Γ(2+iω)|.         (2)

In particular Φ_a(ω) never vanishes at a finite real frequency.

**Proof of the lower bound.** The finite sum in D_a belongs to the closed disk of radius S_a centered at zero. Therefore D_a belongs to the disk centered at 4/a of radius S_a. Since 4/a−S_a=R(a)>0, the entire disk lies in the right half-plane and Re D_a>=R(a). Equation (1) proves both the right-half-plane bound and the lower modulus bound.

**Proof of the upper bound.** The inherited positive rate decomposition is

    q(t)=t ∫_0^5 w(u) exp(−ut) du,
    w(u)=4 on [0,3), 2 on [3,4), 1 on [4,5].

Let ν_a(du)=w(u)(a+u)^(-2)du/R(a), a probability measure. Conditionally on u, X_a is Gamma(shape 2, rate a+u). Thus

    Φ_a(ω)=Γ(2+iω) ∫(a/(a+u))^(iω) ν_a(du),  (3)

whose final integral has modulus <=1. This proves the upper bound. No stochastic independence across arithmetic times is asserted.

With g_1(0)=g_2(0)=1, the explicit envelopes are

    g_1(ω)^2=π|ω|/sinh(π|ω|),
    g_2(ω)^2=(1+ω²)π|ω|/sinh(π|ω|).

They follow from the classical Gamma modulus and recurrence. The result is an exact source application of those formulas, not a new abstract Gamma identity. It is uniform over all a>0, including all original BBP times.

The corrected rate factor Ψ_a=Φ_a/Γ(2+iω) therefore obeys

    1/sqrt(1+ω²) <= |Ψ_a(ω)| <= 1.            (4)

This is compatible with moving-frequency limits that have zeros: if ω grows, its lower bound tends to zero. It is also compatible with inherited fixed-frequency Gamma-2 convergence as a tends to infinity.

## 3. A global continuous phase, without discarding windings

Since D_a lies in Re>0, its principal argument is globally well-defined and continuous. Equation (1) admits the continuous logarithm

    Log_0 Φ_a(ω)=logΓ(1+iω)+Log D_a(ω)−log R(a),

where logΓ is its analytic branch on Re z>0 normalized by logΓ(1)=0. The continuous, unwrapped phase is

    arg_0 Φ_a(ω)=Im logΓ(1+iω)+Arg D_a(ω).

The source correction obeys

    |Arg D_a(ω)| <= arcsin(a S_a/4) < π/2.

This controls only the correction relative to Γ(1+iω); it does not bound the total unwrapped Gamma phase. Replacing this continuous logarithm with the principal argument of the full Φ can lose winding information.

## 4. Finite-band Fourier recovery and its exact limitation

On L²(R), use Fourier convention fhat(ω)=∫f(y)exp(−iωy)dy and define

    (C_a f)(y)=E f(y+log Y_a).

Then (C_af)hat(ω)=Φ_a(ω) fhat(ω). The nonzero multiplier makes C_a injective. For every Ω>=0 and every f with Fourier support in [−Ω,Ω], Plancherel and (2) give

    g_1(Ω)||f||_2 <= ||C_a f||_2 <= ||f||_2.

For Ω=0 the usual band subspace is trivial as an L² space; the scalar formula is interpreted continuously. For Ω>0 the inverse on this band has operator norm at most

    [sinh(πΩ)/(πΩ)]^(1/2).                    (5)

Here g_1 decreases on the positive axis: d log(g_1²)/dω=1/ω−π coth(πω)<0, because x cosh x−sinh x>0 for x>0.

This is an explicit reconstruction theorem for the **full output function C_a f**, not for one scalar expectation. It is not a bounded inverse on all L². To see this, take unit functions whose Fourier support is in [N,N+1]. The upper Gamma-2 envelope tends uniformly to zero there, so their images have norm tending to zero. As Ω grows, the sufficient inverse factor in (5) grows asymptotically as exp(πΩ/2)/sqrt(2πΩ). Thus the transform preserves exact information while strongly attenuating high frequencies and amplifying recovery error.

Applying an injective auxiliary transform to source data cannot recover a separate quantity never encoded in that data. All changed seeds have exactly the same p_a and C_a; hence this theorem does not close the source-to-selected-orbit bridge.

## 5. Larger zero-free Mellin domain, including an authentic boundary

Set M_a(z)=E Y_a^z. Since q(t)~15t at zero and decays after the a tilt, M_a is analytic on Re z>−2. For Re z>−1 the inherited expression is

    M_a(z)=a^z Γ(z+1)/R(a)
      * [4 a^(−z−1)−Σ_d v_d(a+d)^(−z−1)].   (6)

If σ=Re(z+1)>0, the absolute value of the leading term is 4a^(−σ), strictly greater than Σ_d v_d(a+d)^(−σ). Thus the bracket is nonzero. Gamma has no zeros. Therefore

    M_a(z) != 0 whenever Re z>−1.             (7)

This half-plane is simply connected, so it has a unique analytic logarithm fixed to zero at z=0. No conclusion about all of the larger convergence domain Re z>−2 is claimed.

**Additional source boundary theorem.** If a>0 is rational (in particular a=8n−7), then M_a is also nonzero on Re z=−1.

At z=−1 the Gamma pole in (6) is removable and the value is

    M_a(−1)= [Σ_d v_d log(1+d/a)]/[aR(a)] >0. (8)

For z=−1+iω with ω!=0, Gamma(iω) is finite and nonzero. A vanishing bracket would require

    4=Σ_d v_d exp(−iωℓ_d).

Equality in the triangle inequality forces each of the three phases to be one. Write a=p/q in lowest positive integers, and let A=p+3q, B=p+4q, C=p+5q. The phase alignments imply that ω log(B/A) and ω log(C/B) are nonzero integer multiples of 2π. Because both logarithms are positive, the ratio is a positive rational; hence for some positive integers k,l,

    (B/A)^l=(C/B)^k, or B^(k+l)=A^l C^k.

But gcd(B,A)=gcd(B,C)=1 since gcd(p,q)=1. Any prime divisor of B divides the left side and not the right side, contradiction. Thus no nonzero ω produces a boundary zero.

This boundary result is specifically stronger than the general one-gap class below. It supplies no quantitative lower bound along the whole boundary, where near-alignments remain possible.

## 6. General class and hostile control

The real-axis sandwich and open zero-free half-plane apply without alteration to

    q(t)=Σ_{j=1}^m v_j (1−exp(−d_j t)), v_j,d_j>0,
    R(a)=Σ_j v_j[1/a−1/(a+d_j)].

The proofs use exactly the same dominant least-rate channel and Gamma-2 rate mixture, with w(u)=Σ_j v_j 1_[0,d_j](u). They do not characterize the original BBP source uniquely and cannot certify its seed.

The rational-boundary conclusion does not extend to every member of this class. For the one-gap kernel q(t)=1−exp(−dt), formula (6) has exact zeros at

    z=−1+2π i k/log((a+d)/a), k any nonzero integer.

This is a calibrated mutation that preserves positivity and the Gamma-2 endpoint yet loses the authentic three-rate nonalignment on the convergence-strip boundary. It is an appropriate negative control for any implementation of the boundary theorem.

## 7. Source versus Green

The Green-tail law mixes forcing components over j with geometric weights. Its characteristic is a coherent sum of individually nonzero characteristics with different phase centers. A general sum of nonzero complex numbers can vanish, so (2) and (7) cannot be transported to the Green mixture by positivity of mixing weights alone. The inherited Green transform and moving-frequency formulas remain valid but need their own estimates.

## 8. Checks actually executed

A separately implemented mpmath diagnostic at 70 decimal digits compared:

- signed-channel expression (1),
- finite-interval positive rate quadrature (3),
- direct positive-kernel quadrature for selected frequencies,
- both Gamma envelopes and the right-half-plane bound,
- the one-gap boundary-zero control.

Parameters a in {0.1,1,9,17,89,997}; frequencies {0,0.37,−2,2π,10,2πa}; direct positive-kernel quadrature at 0.37 and −2. **157 diagnostic assertions passed.** Maximum discrepancy divided by |Γ(2+iω)| was about 7.97e−70. These are numerical consistency checks, not interval certificates or universal proof. The preceding written inequalities supply the mathematical proof.

## 9. Primary classical references inspected

- NIST DLMF 5.2.1, Euler integral and zero-free Gamma: https://dlmf.nist.gov/5.2.E1.
- NIST DLMF 5.4.3, imaginary-axis Gamma modulus: https://dlmf.nist.gov/5.4.E3.
- NIST DLMF 5.5.1 and 5.5.3, recurrence and reflection: https://dlmf.nist.gov/5.5.E1.

Proofs of the source bounds above are original derivations in this round; classical Gamma identities and inherited source representation are expressly credited.
