# Preregistered extension — exact prime-window denominator product and asymptotic readout cost

**2026-11-06, add-on to original SUCC holographic-triangle PR #534.** This conjectured strengthening was DERIVED after the first 19-test suite and before executing any of the NEW window-product tests. It is NOT a blind mathematical discovery; the theorem was hypothesized from source-pole factorization and is committed before the new empirical probes. Existing original preregistration and results remain intact.

## Quantified candidate

For each integer n>=2, define P_n as the product of all primes p with

`4*n < p <= 8*n - 7` AND `p mod 4 == 1`.

Claim: for the ORIGINAL authentic four signed poles with literal U0=0, `P_n` divides the reduced denominator `d_n` of U_n (equivalently its real fractional part). Proof candidate: p>4n means none of `2j-1`, `4j-1` for 1<=j<=n can be divisible by p, and `8j-7`, `8j-3` are strictly less than `2p`; p can enter only as a literal first power at a unique j. For p mod8=1 this is `8j-7=p`, j=(p+7)/8<=n; for p mod8=5 it is `8j-3=p`, j=(p+3)/8<=n. The nonzero coefficient of this unique pole is 4 or -1, hence no cancellation in the source convolution and v_p(U_n)=-1.

By the classical prime number theorem in arithmetic progressions mod4, the weighted log-prime sum in this moving interval is `(2+o(1))*n`, so `log d_n >= (2-o(1))*n` for all sufficiently large n. Therefore `log2 d_n >= (2/log(2)-o(1))*n`, i.e., exact denominator-certified real readout demands LINEAR 2-adic precision at every sufficiently large original time, while finite complete census over N observations requires at most logarithmic depth. These are mathematical statements about the declared readout method, not a normality proof or a universal bound on any other algorithm.

## Fresh exact windows, frozen before their outcomes

Run window-product divisibility checks for `n=(8,16,32,64,128,257)` with independent prime enumeration and exact Fraction `U_n`; count contributing primes, record bit-length of P_n versus d_n, and verify `v_p(U_n)=-1` for every p in the window. A second oracle should reconstruct U_n by summing the original partial fractions rather than using the accumulated state function. Check a mutant control changing the first pole from weight 4 to 0: it should remove p≡1(mod8) births, while p≡5(mod8) births survive, showing source-weight dependence. Keep all original tests and source/carry constraints frozen.

PASS if the divisor theorem survives all exact checks and a complete all-n algebraic proof is written; the asymptotic conclusion may invoke PNT-AP explicitly as a CLASSICAL assumption, not local computation. FAIL if any n exhibits a window p whose pole cancels in the original state; preserve the exact counterexample. Finite checks cannot replace the universal divisor argument.
