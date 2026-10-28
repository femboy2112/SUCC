# Full-source delay collision theorem at 7, with 11 and 241 holdouts

Research proof dossier, 2026-10-27. Source pinned to PR325 commit `95ee2f1fab851afe1517d8ec5a0589885842426f`; inherited forcing and zero seed unchanged. This is a **genuine arithmetic proof step**, not real Fourier cancellation or pi normality. Validation is recorded in PI_PRIME7_ROUND2_VALIDATION.md; no Lean proof is asserted.

## Hole contract and earned boundary

Initial candidate: the complete signed source, observed at consecutive inputs, removes numerator-mirror ambiguity at all 7-adic depths in a manner capable of forcing signed real correlation saving.

The first clause is now precisely proved: three consecutive complete projective source values determine time modulo every power of 7; two values have exactly one unordered exceptional pair. In fact the single full source has **more**, not fewer, collisions than its numerator: `(12L+7)7^(L-1)` versus `(6L+7)7^(L-1)`. This is genuine source-specific arithmetic, retaining all poles. The required extra clause about real signed correlation is **OPEN**, and the two-delay energy gate is proved asymptotic to the already obstructed time-residue energy. The step removes a plausible but false automatic-cancellation inference.

Quantifiers: all integers L>=1, all residues of natural time x,y modulo p^L, p in {7,11,241}. Output is P^1(Z/p^L Z), interpreted as primitive numerator/denominator pairs modulo units. Inputs are affine time residues, **not** all P^1 input points. The source is

    A(x)=120x^2-89x+16,
    D(x)=(2x-1)(4x-1)(8x-7)(8x-3),
    R(x)=[A(x):D(x)], r=A/D.

For d>=1 define the source delay code

    F_d(x)=(R(x),R(x+1),...,R(x+d-1)),
    C_d(p,L)=#{(x,y) mod p^L : F_d(x)=F_d(y)}.

The exact all-level results are:

| p | C_1(p,L) | C_2(p,L) | C_3(p,L) |
|---|---|---|---|
| 7 | (12L+7)7^(L-1) | 7^L+2 | 7^L |
| 11 | (10L+17)11^(L-1) | 11^L+2 | 11^L |
| 241 | (240L+257)241^(L-1) | 241^L | 241^L |

The p=7 proof below is independently readable from a seven-entry exact table. The holdouts use the same general lifting proof with finite certificates; the script computes every residue at the holdout primes. Those finite certificates justify only the finite hypotheses; the Hensel/Morse argument performs the infinite lift.

## 1. Complete pole handling and the exact p=7 table

A(x)=(x+1)^2+1 mod7, hence A is a unit on every affine 7-adic input. Therefore the **reciprocal chart**

    s(x)=D(x)/A(x)

is defined on all Z_7. It represents the same projective source R(x), including each denominator pole as s=0. Consequently R(x)=R(y) modulo 7^L iff s(x)=s(y) modulo 7^L. No pole is discarded or assigned a spurious finite value.

| x mod7 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| s(x) | 0 | 3 | 0 | 0 | 0 | 1 | 4 |
| s'(x) | 2 | 0 | 6 | 6 | 3 | 0 | 5 |
| (s(x),s(x+1)) | (0,3) | (3,0) | (0,0) | (0,0) | (0,1) | (1,4) | (4,0) |
| (s(x),s(x+1),s(x+2)) | (0,3,0) | (3,0,0) | (0,0,0) | (0,0,1) | (0,1,4) | (1,4,0) | (4,0,3) |

The two critical residue classes are 1 and 5, and s''(1)=s''(5)=5 mod7. These are simple critical points, with distinct source values and no other residue preimage of either critical value.

For auditing derivatives, with W=A'D-AD',

    W=-122880x^5+259584x^4-215040x^3+87800x^2-17744x+1427,
    W=-2(x-1)(x+2)(x^3+x^2+x-2) mod7.

The cubic has no root in F7; W'(1)=W'(5)=1 mod7, and s'=-W/A^2.

## 2. Local exact counting lemma

Let f have integral Taylor coefficients on a p-adic residue disk, p odd, with unit denominator in the chosen projective chart. The authentic rational charts satisfy this condition. A unit derivative alone for an unrestricted analytic function would not suffice.

* If f' is a unit on the disk, f is an isometric bijection from that input disk onto the output residue disk. Indeed the difference quotient is a unit for unequal points in the disk; successive Hensel lifting is bijective at every finite depth.
* If f' vanishes at its center modulo p and f'' is a unit, Hensel gives a unique critical point c in the disk. Write

      f(c+t)=f(c)+b t^2(1+t H(t)),  b=f''(c)/2 a unit, t in pZ_p.

  The unit `1+t H(t)` has a unique analytic square root congruent to 1 modulo p. The coordinate `w=t sqrt(1+t H(t))` is an isometry/permutation of pZ_p, because it is t+O(t^2). Thus equality of f values modulo p^L is equivalent to equality of w^2 modulo p^L.

The number of square-collision pairs on pZ/p^L is exactly

    K_p(L)=[1+(p-1)(L-1)] p^(L-1).

Proof: `(w,z)->(u,v)=(w-z,w+z)` is bijective on `(pZ/p^L)^2`. For u=0, v has p^(L-1) choices. For each a=v_p(u) in {1,...,L-1}, there are `(p-1)p^(L-a-1)` choices of u and p^a choices of v satisfying uv=0 modulo p^L. Every a contributes `(p-1)p^(L-1)`. This includes L=1 without exceptional convention.

More generally, suppose each critical residue is simple and its output value has only that one residue preimage. Let k be the number of critical residues, and C_1(p,1) the one-level ordered collision count. Each noncritical pair of residue disks contributes p^(L-1), and each critical disk replaces its former contribution p^(L-1) by K_p(L). Therefore

    C_1(p,L)=[C_1(p,1)+k(p-1)(L-1)] p^(L-1).       (1)

This is an exact local-to-all-level theorem, not a fit to numerical counts.

At 7 the four simple pole disks all map bijectively onto the same source disk, contributing 16*7^(L-1). The remaining regular disk (x=6) contributes 7^(L-1). The two critical disks contribute `2(6L-5)7^(L-1)`. Their sum is `(12L+7)7^(L-1)`.

## 3. Two delays: precisely one exceptional unordered pair

At 7 the two-delay code has only the off-diagonal residue pair {2,3}. Within any fixed input residue disk, at least one of s'(x), s'(x+1) is a unit: the only critical classes 1 and 5 are not consecutive. Therefore if x=y modulo7 and F_2(x)=F_2(y) modulo7^L, then x=y modulo7^L. This accounts for exactly 7^L diagonal pairs and no other same-disk pairs.

For the two different disks x=2, y=3, apply multivariate Hensel to

    H(x,y)=(s(x)-s(y), s(x+1)-s(y+1)).

Its Jacobian at (2,3) is

    [[6,-6],[6,-3]] mod7,

with determinant 4 mod7. Thus there is exactly one solution (a_L,b_L) modulo7^L lifting (2,3), for every L>=1. The transposed solution is the only other off-diagonal pair. Consequently C_2(7,L)=7^L+2, with exactly one fiber of size two, every other fiber of size one.

Unordered finite examples, retained as exact checks rather than proof:

    L=1: {2,3}
    L=2: {24,30}
    L=3: {220,324}
    L=4: {563,2382}
    L=5: {4783,10167}.

The limiting off-diagonal collision is an actual pair of distinct 7-adic inputs. It does not disappear at deeper modulus. Therefore the plausible assertion “two consecutive full source values are already injective” is refuted.

## 4. Three delays: exact time reconstruction

The table of triples modulo7 has seven different rows. Hence equality modulo7^L first forces x=y modulo7. The local unit derivative from one of the first two coordinates then forces x=y modulo7^L. Thus F_3 is injective at every finite depth and is an isometric embedding of Z_7 into the triple product with the maximum projective chordal metric.

Three is the minimum number of consecutive full-source observations for this exact all-depth statement, since the preceding section exhibits the two-sample collision at every level. This result is specific to the complete source and its actual affine successor, not to an artificial Gaussian imaginary-time direction.

## 5. Holdout certificates at 11 and 241

At 11, A has no zero residue, so the same global reciprocal chart s=D/A works. Its values and derivatives are

    s:  2,5,7,0,7,0,0,8,8,10,0,
    s': 1,0,3,3,8,2,7,1,1,4,3.

There is one simple critical class, x=1, whose source value is unique. The one-level source collision count is 27. Formula (1) gives `(10L+17)11^(L-1)`. The only two-delay off-diagonal pair is {2,4}. In reciprocal coordinates the determinant is `-3*2+8*3=18=7 mod11`; in the standard finite/infinite chart used by the script it is 3 mod11. Both are units, as required. Three-delay residues are all distinct; local two-delay immersion holds. Therefore C_2=11^L+2 and C_3=11^L.

At 241, a global reciprocal chart cannot be used because A has a double root x=152 modulo241. The script uses finite chart r=A/D whenever D is a unit, and reciprocal chart D/A at the four pole residues. The full finite certificate is:

    one-level C_1=497;
    sole critical input x=152, simple, with uniquely attained output r=0;
    two-delay map injective on all 241 affine residues;
    at least one derivative of the first two samples is a unit at each residue.

Formula (1) gives `(240L+257)241^(L-1)`. The same local immersion plus one-level injectivity gives C_2=C_3=241^L at every depth. This separates numerator-root ramification at 241 from source delay ambiguity.

## 6. Exact comparison with time-residue energy

For arbitrary complex phases |z_n|<=1, n=0,...,N-1, q=p^L, define

    Z_t=sum_{n<N,n=t modq} z_n,
    E(N,q)=(q/N^2) sum_t |Z_t|^2,
    G_d(N,q)=(q/N^2) sum_v |sum_{n<N,F_d(n)=v} z_n|^2.

At p=7 or 11, the two-delay exceptional pair (a_L,b_L) gives the exact **signed** identity

    G_2(N,q)=E(N,q)+(2q/N^2) Re(Z_aL conjugate(Z_bL)),

and consequently

    |G_2(N,q)-E(N,q)| <= 2q ceil(N/q)^2 / N^2
                            <= (2/q)(1+q/N)^2.       (2)

The sign is not assumed negative. At all three primes G_3=E exactly. At 241 already G_2=E exactly.

Thus for any q(N)=p^L(N) tending to infinity with q(N)=o(N), the two-delay full-source energy gate is equivalent to the time-residue energy gate. The three-delay gate is identical at every finite N,q. This precise transfer proves that deeper complete-source delay conditioning does not evade #327's normal finite-type moving-energy obstruction. It also shows why deleting pole classes or pretending two-source injectivity would give an incorrect identity.

The authentic phases z_n=e(hU_n) satisfy (2), but the same theorem holds for the coherent control z_n=1 and the future-selected changed-seed solution V_n=-T_n. In the latter, all four original poles, every source delay code, and every lemma above remain unchanged, while phases tend to 1. Consequently no source-delay collision theorem alone can justify a real signed saving. The zero seed must enter an additional argument, not merely be listed in the setup.

## 7. Remaining precise lamp

A useful next claim would have to control a signed real phase quantity whose proof actually uses U_0=0 and fails at V_0=-pi/16. The weakest source-pair energy statement capable of proving normality still requires, for every fixed h!=0, a schedule q=o(N) with G_d(N,q;h)->0; (2) proves this route is exactly the old moving time-residue gate up to O(1/q). Its novelty tax is not paid by source-delay reconstruction.

What is newly established is the exact arithmetic geometry: all full-source critical disks, their complete collision law, the persistent isolated two-delay intersection, and the minimal three-delay reconstruction theorem. Real selected cancellation remains Dark. The next falsifier for any proposed arithmetic-to-real bridge is the unchanged-four-pole future-selected control; a bridge not excluding it is invalid before numerical pi data are examined.

## Probe and claim ledger

`pi_full_source_delay_probe.py` uses only exact integer modular arithmetic. It certifies the finite hypotheses at p=7,11,241, checks complete counts through 7^5 and 11^3, preserves the noninjective two-sample controls, and checks that the source-only count is not incorrectly replaced by the numerator count. It does not approximate real phases.

* PROVED: local critical-disk collision formula and its all-level lift.
* PROVED: C_1,C_2,C_3 at p7; holdouts by the same proof plus exhaustive finite certificates.
* PROVED: signed energy identity (2), with full intersection and pole handling.
* REFUTED: two-delay source injectivity at 7 and 11.
* REFUTED: automatic collision reduction when replacing A by full projective r; at7 its ramified slope doubles.
* OPEN: source-and-zero-seed real Fourier cancellation; pi normality.
