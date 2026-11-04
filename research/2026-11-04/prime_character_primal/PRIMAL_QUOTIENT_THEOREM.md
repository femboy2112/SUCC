# Prime-Frobenius character quotient: the two-state Gaussian primal BBP

**Research-only paper theorem, 2026-11-04.** Parent #497 at
4383bd31340af700e312f13d7ef28af090c152d5.
The first source/character preregistration is f41b75c8fbb28ef52e6e696f492ec7e6193e0c65;
the second all-prime/angular saturation preregistration is f1723146dd5141d65a3891cca95fe9418a7ff37a.
These were pushed before their respective new holdouts. Early discovery calculations are
development observations, NOT blind confirmation. π normality and global novelty are OPEN.

## Source contract

The authentic BBP numerator is P(t)=4−2t³−t⁴−t⁵, with taps
p=(4,0,0,−2,−1,−1,0,0). Its original forcing and zero seed are

r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2),
U₀=0, Uₙ=16Uₙ₋₁+r(n).

For any rational eight-tap vector w=(w₁,...,w₈), let
r_w(n)=Σ_{j=1}⁸ w_j/(8(n−1)+j) and define U⁽ʷ⁾₀=0,
U⁽ʷ⁾ₙ=16U⁽ʷ⁾ₙ₋₁+r_w(n). No real π digits are supplied to this construction.

## PQ-01: a TRUE four-class source action, not a guessed quotient

Let G=(ℤ/8ℤ)×={1,3,5,7}, χ₂(a)=(2/p) for p≡a mod8:
χ₂(1)=χ₂(7)=1, χ₂(3)=χ₂(5)=−1.
Define j_a(l)∈{1,...,8} as the least positive residue of al mod8,
with residue zero represented by 8. The rational monomial operator on
ALL eight-tap sources is

 (S_a w)_l = χ₂(a)^(8−l) 2^((j_a(l)−l)/2) w_{j_a(l)},  1≤l≤8.       (PQ-1)

All powers of two here are exact rational; their exponents are integers.

**Prime-event proof of the formula.** For p≡a mod8, a source p-pole
appears at n=(mp+8−j_a(m))/8 where the original denominator is mp.
At the end of each block m=8k+1,...,8k+8, the chronological source time
is (k+1)p. Euler's criterion for 2 modulo p gives exactly the multiplier
in (PQ-1) for the injection from m to that block's endpoint. Fermat gives
16^p≡16 modp across adjacent full blocks. Consequently, for ANY rational
tap vector with p-integral coefficients, for k≥1 and prime p>8k,

    p U⁽ʷ⁾_(kp) ≡ U⁽S_a w⁾_k (mod p).                         (PQ-2)

The p times the state is p-integral because all original denominators are
less than p²; both sides admit legitimate residues. This is a selected
p-local CONGRUENCE, not a real-circle source identity or Galois average.

**Group-law proof.** The tap position permutation satisfies
j_b(j_a(l))=j_ab(l). Its power-of-two factors telescope:
(j_a(l)−l)/2+(j_ab(l)−j_a(l))/2=(j_ab(l)−l)/2.
The signs combine because χ₂ is multiplicative and j_a(l)≡l (mod2),
so χ₂(b)^(8−j_a(l))=χ₂(b)^(8−l). Hence

             S_a S_b = S_ab,  S_1=I, S_a²=I.                 (PQ-3)

This is a genuine ℚ-representation of the Klein four group on ℚ⁸,
not a formal involution invented for the original π vector.
Its four character-isotypic dimensions are 4,2,1,1 for
1, χ₋₄, χ₈, χ₋₈.

## PQ-02: quotient the original BBP from its own prime shadow

The original source is fixed by S₁ and S₅. Its two inert-class
transforms agree:

       S₁p=S₅p=p,     S₃p=S₇p=−p♯/2,

where p♯=(0,8,4,4,0,0,−1,0) is the SECOND, classical BBP 2π
numerator. Thus the prime shadow RECOVERS the second source;
it need not be given as an oracle.

The group-ring character idempotents

Πχ=(1/4)Σ_{a∈G}χ₋₄(a)S_a and Π₁=(1/4)Σ_{a∈G}S_a

split the actual two-dimensional source orbit module
M=span_Q{p,S₃p} into a χ₋₄-anti-invariant line and a
trivial-character invariant line:

p_ang=Πχ p=(2p+p♯)/4=(2,2,1,0,−1/2,−1/2,−1/4,0),

p_rad=Π₁p=(2p−p♯)/4=(2,−2,−1,−2,−1/2,−1/2,1/4,0),

p=p_ang+p_rad, S₃p_ang=−p_ang, S₃p_rad=+p_rad.   (PQ-4)

The other two character projectors annihilate this original p.
Important: this SOURCE prime-class action is NOT identical to
the H/G central spectral idempotents of the earlier
ℚ(√2)×ℚ(i) minimal source realization.

## PQ-03: the actual primal angular form

Put D₈(t)=1−t⁸/16 and
F(t)=(2−t²)/((t−1)²+1), for 0≤t≤1.
Exact rational polynomial identities give

 P_ang(t)/D₈(t) = 4/((t−1)²+1),

 P_rad(t)/D₈(t) = 2 (d/dt)log F(t),

 F(0)=F(1)=1.                                            (PQ-5)

Hence the radial period along the original source interval vanishes,
while the χ₋₄ anti-invariant angular period is

        ∫₀¹ 4 dt/((t−1)²+1) = π.                         (PQ-6)

The period functional on M has kernel EXACTLY the radial eigenspace.
Thus its quotient M/span(p_rad) is canonically isomorphic to the
angular character eigenspace WITHIN THIS DECLARED SOURCE MODULE.
This is NOT a claim that all π formulas have a unique primal source.

The projected kernel reduces further:

K_ang(t)=4/((t−1)²+1)
        =(2+2t+t²)/(1+t⁴/4)
        =2/(1−t+t²/2).                                  (PQ-7)

Its impulse begins (2,2,1,0,−1/2,...), with exact
c_(m+4)=−c_m/4. A 2×2 Hankel minor [[2,2],[2,1]]
has determinant −2; the reduced denominator has degree two.
Thus minimal reachable/observable RATIONAL linear dimension is exactly 2,
not 1. One Gaussian complex state suffices:

u=(1+i)/2,  u²−u+1/2=0, u⁴=−1/4, u⁸=1/16.

The polar quotient u/|u|=(1+i)/√2 gives the oriented circle
angle π/4. The source and its observation interval supply the
normalization; the circle has not been assumed to be Haar.
The signed-base-4 integral produces the CLASSICAL primal formula

π = Σ_{k≥0}(−1/4)^k [2/(4k+1)+2/(4k+2)+1/(4k+3)].       (PQ-8)

The arctan, null BBP and signed -4 identities were already known to
SUCC's October 26 TWO_QUADRATIC_ATOMS work and published literature.
The new-to-SUCC content is their construction from the GENUINE
prime-Frobenius character representation.

## PQ-04: the primal remains an admissible odd-denominator arithmetic source

Although its eight taps have denominators 2 and 4, the complete
projected moment (glue FIRST) simplifies to

r_ang(n) =
(30720n⁵−63232n⁴+45792n³−13892n²+1641n−48) /
[(4n−3)(4n−1)(8n−7)(8n−5)(8n−3)(8n−1)].               (PQ-9)

Every displayed denominator factor is odd for integer n≥1.
Thus the zero-seeded Y_n=16Y_(n−1)+r_ang(n) always has
odd reduced denominator and retains the lawful unique odd-inverse
circle branch. The source is EXACT, not an isolated Galois character.

The angular source has leading +15/(32n), radial source −15/(32n),
whose sum recovers the original accelerated r(n)=15/(64n²)+O(n⁻³).
The primal is simpler analytically but its raw source force decays
only like 1/n. The radial source is an exact conditioning counterterm.

## PQ-05: original/primal selected real current and Weyl transfer

Define Y=U⁽p_ang⁾, Z=U⁽p_rad⁾, and V=U⁽p♯⁾.
Exact identities give U_n=Y_n+Z_n,
Y_n=(2U_n+V_n)/4, Z_n=(2U_n−V_n)/4.
The inherited authentic PF-8b source proof gives for ALL n≥1:

               0<Z_n<1/(32n+16).                       (PQ-10)

Hence the original and primal fixed-frequency Fourier sums differ by

 |Σ_{n≤N}e(hU_n)−Σ_{n≤N}e(hY_n)|
 < (π|h|/16)H_N = O_h(log N).                            (PQ-11)

Their normalized Weyl limits are identical. Consequently the
UNPROVED assertion "π normal base16" is EQUIVALENT to
"the primal 2-state zero-seeded Y has fixed-h Weyl decay for all h≠0".
This is a source-specific reduction, not a proof of that decay.

For the actual selected triangular pair energy
J_(A,q)(X)=(q/A²)Σ_{n,t∈[A,2A)}(1−q||X_n−X_t||)_+,
the same strictly positive radial bound yields

         |J_(A,q)(U)−J_(A,q)(Y)|
         ≤ q²/(32A+16) = o(1) at q≈log A.             (PQ-12)

Thus the selected-current front can be transferred to the rank-two
Gaussian primal WITHOUT replacing original temporal samples by a
Haar branch ensemble. The missing signed/current bound remains open.

## PQ-06: angular p-pulses, and a NEW sharp 8N denominator theorem

For a∈G and source p-pole multiplier m=8k+l with 1≤l≤8, define

f_a(l)=χ₂(a)^l 2^((l+8−j_a(l))/2).

The universal rational primal p-event normalizer has the exact formula

C_ang,a(8k+l) = χ₋₄(a) f_a(l)
    [Y_k+(1/16)Σ_{j=1}^l w_ang,j/(8k+j)].              (PQ-13)

**Proof:** transport from the previous full block, factor f_a(l),
and use S_a p_ang=χ₋₄(a)p_ang to rewrite each partial injection.
For every k≥0 the bracket is STRICTLY POSITIVE: Y_k≥0 from the
positive original projected source; the first positive tap 2/(8k+1)
dominates the total possible later negative contribution

  2/(8k+1) − 5/[4(8k+5)]
  = (24k+35)/[4(8k+1)(8k+5)] >0.

Therefore every primal p-pulse is nonzero and its forced sign is

         sign C_ang,a(8k+l)=χ₋₄(a)χ₂(a)^l.             (PQ-14)

The angular source has a nonzero tap at ALL four odd positions
j=1,3,5,7. Consequently all generic odd primes p≤8N−7 are born
by original source time N. For every fixed ε>0, any such source
prime p>εN eventually has simple p-poles, bounded number of events
m≤8/ε+O(1), and a nonzero universal normalizer belonging to one
of finitely many fixed nonzero rational numbers. For all sufficiently
large N, p exceeds every prime dividing the finitely many normalizer
numerators/denominators; hence v_p(Y_N)=−1.

The angular source cumulative conductor M_ang(N) divides the odd
part of lcm(1,...,8N) and contains all generic p≤8N−7.
By the classical PNT and the above genuine selected-state survival,

 log den(Y_N) = (8+o(1))N,
 log M_ang(N) = (8+o(1))N.                              (PQ-15)

Parent #497 proves log den(U_N)=(6+o(1))N.
Thus the source-attested character quotient INCREASES denominator
complexity even though it REDUCES minimal transfer dimension:

 log[den(Y_N)/den(U_N)] = (2+o(1))N,
 0<U_N−Y_N<1/(32N+16).                                (PQ-16)

This is an exact arithmetic trade-off and a compelling finite/analytic
radial-cancellation effect; it is NOT a real-circle equidistribution
or numerical entropy theorem. Small-prime finite exceptions are allowed.

## Source access, hostile controls and authority

- Genuine local p reduction requires p>8k and p-integral tap coefficients.
  It does not authorize averaging over prime classes as if different p
  were independent chronological orbit samples.
- The original zero seed is essential: a rational seed 1/5 is invisible
  to these p congruences at generic p>5, while it changes real phases.
- A one-tap mutation breaks original χ₋₄/trivial purity; false quadratic
  character signs break genuine p-residue predictions.
- The radial null is NOT a zero finite state; Z_n>0 for every n≥1.
- The rank-two rational generating-function kernel is NOT a finite-state
  automaton for the unbounded-denominator source-time carry process.
- Structural proof verification: universal algebraic group law, strict
  positive p-pulse argument, exact rational symbolic kernel identities
  and classical PNT. Finite exact tests are calibration, not universal proof.
- Literature: D. Barsky, V. Muñoz, R. Pérez-Marco, *On the genesis of BBP
  formulas*, Acta Arithmetica 198 (2021), 401–426; MathWorld
  *BBP-Type Formula*. These establish BBP/arctan/null rearrangements,
  not necessarily the source-prime character action. Global academic
  priority remains UNVERIFIED.

**Claim statuses:** PQ-01–PQ-06 paper-proved within exact source
hypotheses and classical PNT; arithmetic/oracle tests observed;
source-selected real current J=o(log log A), Weyl decay, π normality,
RH, and world-first originality NOT CLAIMED.

**Full local tested package:** SUCC_Prime_Character_Primal_2026-11-04.zip,
with prime_character.py, symbolic_oracle.py, probe.py, 26 focused tests,
source receipts and detailed proofs. The upload bridge may place this
full package outside the GitHub working tree; do not claim remote tests
have run until the individual source files are imported and verified.
