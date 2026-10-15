# Part II: a genuine SUCC/FUCC action on zero-centered residue observers

**Branch:** research/zero-centered-residue-observers-2026-10-13. Parent mathematical object: [zero-centered residue-clock dossier](ZERO_CENTERED_SUCC_RESIDUE_OBSERVER.md). **RH PROVED: no.** Arithmetic theorems and exact code, not a global analytic obstruction.

## Constructions and typed transport

Let H_w=ell²(N,w) with w_k=1/[k(k+1)] and residue-clock observations r_n(k)=(k mod n)/n for n>=2, with r_1=0. The physical integer-carrier operations are S(k)=k+1 and V_q(k)=qk (q>=2); no physical/quantum state identification is assumed. Their *contravariant pullbacks* on observers are

  (T_S f)(k)=f(k+1),      (T_q f)(k)=f(qk).

This is the actual operator induced by changing the index of an observer's readings, not an invented unitary transport. Since V_p S = S^p V_p on integer addresses, their pullbacks satisfy the reversed composition law

  **T_S T_p = T_p T_S^p**.

Multipliers commute: T_p T_q=T_q T_p=T_(pq). (ZCR-F01, PROVED LOCAL.) This is a source-free affine semigroup relation and **does not select primes on its own**.

## FUCC quotient-clock theorem (ZCR-F02, PROVED LOCAL)

For integers q,n>=2 put d=gcd(q,n), q'=q/d, n'=n/d. Reduction of qk modulo n gives exactly

  **T_q r_n(k) = r_(n')(q'k)**,

where r_1=0. Proof: (qk mod n)/n = ((q'k mod n'))/n' by removing the common factor d. The result holds for composite q as an algebraic identity; **calling q a prime jet additionally requires primality authentication**.

For a genuine prime p and exponent a>=1 this specializes to

  **T_p r_(p^a) = r_(p^(a-1))**.

At a=1 the clock becomes the zero observer r_1. Thus viewing SUCC from an arithmetic residue clock exhibits an exact *prime-power filtration*: multiplication by p lowers the p-adic observation resolution by one rung. This is structurally relevant to the earlier SUCC/FUCC prime-jet program, without claiming a Weil form.

## Hilbert operator norm theorem (ZCR-F03, PROVED LOCAL)

These pullbacks are **bounded, but not unitary**, on the correct weighted Hilbert space.

For any positive integer q>=2,

  ||T_q f||² = sum_(k>=1) w_k |f(qk)|²
            <= [sup_(k>=1) w_k/w_(qk)] ||f||²
            = q² ||f||²,

because w_k/w_(qk)=q(qk+1)/(k+1), strictly below q² and approaching q² as k->infinity. Testing delta-functions supported at qk and letting k->infinity makes the inequality sharp, so **||T_q||=q**.

Similarly w_k/w_(k+1)=(k+2)/k, maximized at k=1, so **||T_S||=sqrt(3)**.

These are genuine source-derived operator norms. The maps discard part of the input sequence: T_q sees only indices divisible by q, and T_S omits index 1. Neither is a unitary change of reference frame, even though each has a perfectly lawful categorical composition rule.

## Hostile controls and boundary

- Exact grid tested: q=2,3,5,6,7; n=2,3,4,5,6,8,9,12,16,25; k=1..29. Composite q=6 verifies the algebra **without** being mislabeled as a prime.
- Genuine-prime ladder tested for p=2,3,5,7; exponents a=1..4; k=1..12. Input p=6 is rejected by the prime-jet interface.
- Norm-ratio monotonicity and strict non-unitarity tested against exact rational source arithmetic.
- No nontrivial-zero inputs. The operator pullback does **not** intertwine automatically with the Mellin functional or the ordinary SUCC prime eigenket; a source-derived intertwiner and its domain remain **UNVERIFIED**.
- No uniform-positive Weil form, global L² convergence, completed gamma/poles or RH proof is obtained.

**Next discriminating test:** characterize whether a source-authenticated bounded intertwiner between these residue-clock pullbacks and the prime-dilation Hilbert representation exists. The naive assertion that pullback is isometric is **REFUTED** by ||T_q||=q>1. Any proposed RH bridge must preserve correct weighting, signs and analytic-source provenance rather than pretending the nonunitary map is unitary.
