# Exact equivalence: pi base-16 normality as Haar genericity of a selected four-step 2-adic Collatz orbit

**20 November 2026.** Elementary theorem inherited from classical Bernstein--Lagarias parity conjugacy and the definition of base-b normality. This is **NOT** a proof of normality or of general integer Collatz termination. Original BBP four signed poles, zero seed and exact completion retained.

## Definitions

Let `D={0,...,15}^N` with shift `shift(d_1,d_2,...)=(d_2,...)`, and product measure giving every digit independent uniform probability 1/16. Set `A(d)=sum_(j>=1)d_j16^(j-1)` in `Z_2`. This is a homeomorphism from the full symbolic space onto `Z_2` with its usual 2-adic topology, carrying the fair product measure to Haar probability `m_2`. The real digit evaluator is `R(d)=sum_(j>=1)d_j16^(-j)` in `[0,1]`. It is **continuous** on the full symbolic space, but non-injective at the usual terminating/infinite-F pairs. Let `Q:Z_2 -> Z_2` be the full Collatz parity homeomorphism, `Phi=Q^-1`, and let `C` be the shortcut Collatz map on ALL `Z_2`. The maps satisfy `Q C^4=S_16 Q`, where `S_16` removes the least significant 4-bit nibble.

For the genuine four-pole BBP source with literal zero seed, its completed real number is `x=pi/16` by classical BBP. Let `d_pi` be the canonical infinite hexadecimal digit sequence of x (nonterminating and not eventually F because pi is irrational). Define the **selected** 2-adic Collatz companion `alpha_pi=Phi(A(d_pi))`.

## Theorem NC-01 (exact normality transport; classical consequence)

The following are equivalent:

1. Mathematical pi is normal in base 16.
2. The selected canonical symbolic digit word `d_pi` is generic for fair 16-symbol Bernoulli measure under the one-sided shift.
3. The selected 2-adic parity address `A(d_pi)` is generic for Haar on `Z_2` under `S_16`.
4. The selected 2-adic Collatz state `alpha_pi` is generic for Haar on `Z_2` under `C^4`; precisely, for every continuous `f:Z_2 -> C`,

   `lim_(N->infty) (1/N) sum_(n=0)^(N-1) f(C^(4n)(alpha_pi)) = integral_Z2 f dm_2`.

**Proof.** Normality is exactly every finite digit word of length k having asymptotic frequency 16^-k (finite radix prefix pi/16 versus pi irrelevant). These cylinder frequencies characterize weak convergence to the product measure on the compact one-sided symbolic space. The map A bijectively transports these cylinders to congruence classes modulo 16^k in Z_2; each has Haar measure 16^-k. The 2-adic parity homeomorphism Phi transports Haar to Haar because it induces a bijection modulo every 2^m (parity cylinders are single residue classes). It conjugates S_16 to C^4. The equality of the four notions follows by pushforward, change of variables and the cylinder basis. No unknown normality premise has been used to define the maps.

## Theorem NC-02 (the SUCC phase/R0 observable transported exactly)

Define `h(a) = R(A^(-1)(Q(a)))` in `[0,1]`, using the **full** symbolic word associated with `Q(a)`, and define the continuous real-phase test observable

`g(a)=1-cos(2*pi*h(a))`.

Then for every integer B>=1,

`(1/B) sum_(n=B)^(2B-1) g(C^(4n)(alpha_pi)) = (1/B) sum_(n=B)^(2B-1) [1-cos(2*pi*{16^n*pi/16})]`.

The right side is SUCC R0's shell statistic. Consequently R0 is **equivalent**, with no asymptotic approximation, to a strictly positive liminf of the selected orbit's four-step Collatz **continuous test average**. Its Haar benchmark is `integral_Z2 g dm_2=integral_0^1 (1-cos(2*pi*t))dt=1`. The selected-source positive liminf remains **UNVERIFIED**.

For any fixed integer frequency k, the analogous test `a |-> exp(2*pi*i*k*h(a))` yields the exact original circle Weyl shell mean on the selected four-step orbit; proving all nonzero averages vanish remains base-16 pi normality itself, not an independent theorem.

## Theorem NC-03 (operational source and countermodel firewall)

The conjugacy holds for EVERY possible infinite hexadecimal word, including an all-zero word. At all-zero word, `alpha=Phi(0)=0`, and the selected C^4 orbit is constant, not Haar-generic. At all-F word, `alpha=Phi(-1)=-1`, again a locked orbit (the real evaluator identifies 1 with 0 modulo 1). A rational periodic or factorial-sparse nonnormal word yields another legal two-adic Collatz path. The only reason the pi companion is distinguished is its original authenticated four-pole source and literal U0=0; the universal conjugacy alone has no source-specific signed anti-locking estimate.

The selected companion alpha_pi has not been shown to be a positive integer. Therefore this exact equivalence **does not assert anything about positive integer Collatz termination**. Normality of the selected pi word remains an open point-genericity problem, despite Haar mixing of the ensemble under the 2-adic Collatz transformation.

## Credits / next discriminating proof

The parity conjugacy is classical: D. J. Bernstein and J. C. Lagarias, *The 3x+1 Conjugacy Map*, Canadian Journal of Mathematics 48 (1996), 1154--1169, https://doi.org/10.4153/CJM-1996-060-x . Source-specific BBP finite/analytic bookkeeping is credited to SUCC #677-#680. The theorem is a change-of-representation of an open statement, not a new bound. A genuinely new advance must supply an **independently BBP-derived** signed estimate on `g(C^(4n)(alpha_pi))` (or the source cofactor/prime heads) that fails on the locked wrong-seed control and is not obtained by fitting the already unknown pi phase average.
